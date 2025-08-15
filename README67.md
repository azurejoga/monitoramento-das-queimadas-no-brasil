# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3558dc04-20e2-384d-be90-0e655709e4b6 | -9.17962 | -59.65715 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28f97031-7761-3972-8295-87e79317e86d | -7.59636 | -63.50412 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8bc5981d-1233-3b51-a981-5a6b93e78592 | -7.27757 | -64.69568 | 2025-08-15 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c58d409d-9cc4-37a1-be97-13b90d18df94 | -9.16283 | -59.68392 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f13c1704-f524-3872-b46e-7d1062ef4b9e | -6.89672 | -59.1437 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62db7c1a-21f0-32bd-9fbf-16a7674df28c | -7.95175 | -61.75383 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1572737-5a08-3145-88a0-ee085abd9426 | -9.20386 | -59.66051 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3b13df0-3530-3739-8e2b-1d0bd120cf8b | -6.48527 | -62.93798 | 2025-08-15 06:10:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53320ed8-ba9b-3ff0-b87d-c1d3ec963a11 | -10.32433 | -64.45047 | 2025-08-15 06:10:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa794855-d4f0-3196-8e30-02d74a679164 | -7.12343 | -59.62819 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db685ad2-6cb6-3c66-a9b7-4e310ea48ddc | -7.96387 | -63.46564 | 2025-08-15 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91d3d835-ce2a-3984-8496-626b5ce435e2 | -7.87704 | -61.81851 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbfe7254-458d-34dd-a872-baf54fa3871a | -9.83079 | -60.75947 | 2025-08-15 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38df98ba-237a-3f05-b32d-fad30f472061 | -6.88342 | -59.14192 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e83217fb-ade5-3077-9128-15de1c6e2041 | -6.91588 | -59.1522 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2dd5fe43-4b6b-3477-a123-9edef6250187 | -9.20521 | -59.64918 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1cd3e561-9c28-361a-a838-7598274cd266 | -6.89421 | -59.13737 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63ae9cdd-192b-312d-b276-9518e5abad37 | -7.29141 | -60.62855 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f36ba8a3-b3f6-31c7-b0ea-4ac6fa7ad19d | -6.91076 | -59.13982 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bebb4699-af9f-372c-bcd6-a026de13cdfa | -10.86353 | -62.00448 | 2025-08-15 06:10:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 508c9cba-283c-3a71-94cf-367b2e48ce77 | -9.21208 | -59.66678 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f0d5a17-ff14-3563-a009-266cdca20143 | -7.07742 | -59.21699 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 618708ea-bd6e-3500-8f39-72440485dc9b | -9.39062 | -60.54988 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8d9c8605-55b0-33db-8e04-695c95d7343c | -9.91926 | -60.48346 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5bcd58c-2a29-3d66-8d87-58206541f1f9 | -8.55646 | -63.91915 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac8e966d-80ce-3b52-9930-e347f8552e9f | -8.37255 | -70.14568 | 2025-08-15 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c26c71c-4286-3f9d-bdd3-b4b7d646fa7a | -9.01809 | -61.21944 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01fa1316-3e87-374e-9dad-ee21c62523a7 | -7.11697 | -59.62724 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c5327e9-9c37-30cf-a395-a48f01cb1a0d | -9.16946 | -59.68472 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6edabb71-77db-31ac-80ae-20cb328e9074 | -7.32927 | -60.62392 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68c89f80-5de6-3539-975f-1471f50643c0 | -7.08555 | -59.22995 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27c1dfc6-359a-3513-b852-319182a6e87d | -10.36492 | -67.7128 | 2025-08-15 06:10:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6f710d8-24f8-3c76-8c57-b0613e0ed3f9 | -7.87826 | -61.82711 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcf7a6dc-e112-3bf2-b012-7bed3f3ceedd | -7.29758 | -60.62859 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dc02614-431c-3213-b3c3-b1b721af2fc7 | -6.92468 | -59.53407 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6135243-2fa4-3ed9-a890-6bb1eb2548d1 | -7.31028 | -60.62657 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cee0a94-aead-32f2-8c95-cd2de5a0a833 | -9.50251 | -60.54688 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92d4e0b2-03d6-3f02-b94b-e22dd7fd4229 | -7.52505 | -61.37444 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d49dfe6e-43cf-39d0-bea9-ed15a321d67d | -6.9299 | -59.14853 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52c8fece-a801-3c57-9901-a63406e32fea | -9.38432 | -60.54913 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| edd8129f-2e66-3250-923e-6367e2241727 | -7.58762 | -63.45494 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eede0010-3e95-3156-9f20-b63f5b5c9bd9 | -7.87758 | -61.81456 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 652f74a6-a7ee-33cc-9a0e-9096285945ee | -7.44013 | -60.0229 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c18a3c7c-ba80-32e9-a30e-415643a7c813 | -6.93917 | -59.52573 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31388c4b-2028-3dd4-8a27-0257895451d2 | -6.71436 | -58.82466 | 2025-08-15 06:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 012ca083-096d-3958-9f02-93e3a47cdff5 | -6.93687 | -59.54156 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 27b1e8a5-8d69-3ecc-85a5-96b992ea714b | -7.43378 | -60.02208 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8e70818-064f-3b8d-be47-c816c49b81f9 | -8.40432 | -70.44034 | 2025-08-15 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ea5cf97-805f-328d-a924-11310fb21344 | -6.87712 | -59.83354 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c0076c-ba28-3f7e-bc39-f6d3661c2eb3 | -7.95693 | -61.75862 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae6eaf38-1f4b-3f19-81ad-78fa457cc2c9 | -7.52868 | -61.34414 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bd7c012-50f3-3e9f-99b1-95217aa599df | -7.32246 | -60.62831 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae1e5876-0195-323c-9dfc-bc5eac2c16e5 | -7.52444 | -61.37663 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 522c2d7d-a9b5-30ea-bc20-617c8b4ebe44 | -9.17463 | -59.69714 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99ed7478-38dc-3382-acd3-3cf3ee161375 | -7.53086 | -61.32748 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f1bd1556-5778-36f8-9ba2-ebb5e3c207b3 | -7.32972 | -60.62027 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72a52be6-4364-3411-a3c3-0ac42bc27bee | -6.48485 | -62.94105 | 2025-08-15 06:10:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 76de4c85-872f-3c0c-a273-fea59cb7e2a2 | -6.87862 | -59.83956 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dab6dc7-90a2-340b-877a-80d8cb1168b0 | -11.7367 | -64.8978 | 2025-08-15 06:10:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c238fccf-f538-34dd-b5d3-b089f10666fe | -6.87677 | -59.14112 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3578a3ac-f3b6-353a-aebf-2ab07cc9dedd | -8.3205 | -70.07282 | 2025-08-15 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07aa0079-732f-3a68-a8e6-e87bb130cde1 | -9.15172 | -59.66496 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8cc749e-698c-3f6a-9355-41a02fc3b6e6 | -9.79135 | -61.50551 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2637720-7aa1-34e4-bb40-4db24e522396 | -7.08635 | -59.2241 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| adfb8a14-1a11-3832-9432-51e6d2ec6ba2 | -8.55756 | -63.9129 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 899e3b10-995b-3622-8e7a-5d9b27518e4f | -11.4385 | -61.45629 | 2025-08-15 06:10:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f853f1d-7b39-36e3-a531-d9eae8851646 | -9.15033 | -59.67628 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48561e52-7c66-3f58-9819-4f0990e446fd | -9.16213 | -59.68958 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc6f24e4-e22f-35ae-8c77-29892053a42a | -7.07311 | -59.2222 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03670966-52ea-3865-9b89-7f247feda479 | -6.88854 | -59.15451 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 810e782f-7efb-32b8-9320-7d963f6cb3bb | -6.88833 | -59.13086 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a90e879-a298-3e52-9512-f5764203c4b6 | -7.0848 | -59.2121 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 559a4e2b-9d79-3c1c-abab-171793f402b3 | -7.60867 | -63.52681 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c58ccbed-99ac-3e33-9ece-40906cd2c954 | -6.90486 | -59.13316 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59238e03-9ee5-3a0e-95cb-8eee1d2d5267 | -9.50883 | -60.54758 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b542a47f-59fc-3e49-b24c-8e531cc2d20e | -9.20589 | -59.6435 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b802bab-0979-3222-93a7-beb73c82171e | -7.07817 | -59.21115 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a97e882-c98f-3043-ac7e-fc5b130798f9 | -9.71311 | -66.8311 | 2025-08-15 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31c5dfc1-9cb3-3eac-999f-ae8b27a8d196 | -7.8765 | -61.82243 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45837538-6bd3-3b21-abcb-924233472691 | -10.01043 | -59.2168 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20c868d3-b77e-3db3-92d0-de541d0a7033 | -7.52485 | -61.33281 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40c5c56b-dcd3-38f0-b0e0-dfa419ba9b15 | -9.61507 | -67.2895 | 2025-08-15 06:10:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a89b24c9-c796-390a-bbd5-99d7ee55bb48 | -6.93058 | -59.54099 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| c237a41a-9966-3e4e-be5b-d638c4ef1777 | -7.60687 | -63.50266 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b59fd8bf-123a-3043-b313-9d7fcfc56f5a | -6.93114 | -59.53519 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 37fff44b-a5e1-3f94-a62a-b0cf998411d1 | -6.94845 | -59.99374 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 915434a4-ea12-3e4c-8fe9-9a9bd15baa74 | -7.60908 | -63.52387 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4edfd72d-86c4-3e6c-885b-7b4dd4930e99 | -10.3363 | -64.44868 | 2025-08-15 06:10:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 42827fad-26d0-37e1-a684-39aec3d40661 | -9.83379 | -60.76325 | 2025-08-15 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06b495aa-6c1d-3f9f-9e78-4b382c339613 | -7.94708 | -61.7452 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 361b187e-b2ff-338b-9fca-ca90db7c0361 | -7.52389 | -61.38081 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0a08fed-a508-3c10-aa2e-2c4ac3c4b04f | -7.31038 | -60.62579 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 250b5907-a2a5-35bc-9153-a210c1f91090 | -6.90413 | -59.13879 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 525d8d3c-e811-30c0-961b-e09d1f70513e | -7.29865 | -60.62056 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2ab213f-98e3-311d-8f07-8ec9f9dac7ba | -9.20236 | -59.63698 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 028c6c06-fcdd-382a-b84d-e17c63c656b3 | -9.92037 | -63.1888 | 2025-08-15 06:10:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80274d6a-b28a-3294-bd65-91b0c83bbf90 | -7.4192 | -60.03492 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eced0e6f-3195-3f57-834b-beba28aaaf9d | -7.96264 | -61.75943 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 853fe0a8-5307-3de1-aea7-4cfeddd04940 | -9.17818 | -59.66869 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc0eae76-8f92-3eec-bf72-7a8692129729 | -7.94498 | -61.76089 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README68.md)
