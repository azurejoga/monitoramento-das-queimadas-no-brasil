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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58fb17b9-25c0-34b3-81b1-97858f7b5bfb | -15.95821 | -50.23034 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbb55fab-ce1e-350b-b742-7c06419ab99a | -14.36789 | -47.31658 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e3ea50c-9dd0-39a0-9c8d-546fee5739f5 | -13.8776 | -44.45439 | 2025-09-10 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67ec9e2a-281e-3809-94d0-79b166d5f657 | -15.13064 | -52.40049 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| baf42dbf-bfde-3095-b79c-ca6c1323454a | -10.74668 | -48.91756 | 2025-09-10 04:17:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0f93ab1-d6e2-3c34-930c-a1be849e4aa8 | -12.08092 | -45.47482 | 2025-09-10 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71005864-ccd6-3abb-b83f-0440fc67ccd9 | -15.79906 | -41.41825 | 2025-09-10 04:17:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c08ac022-63a8-3cbb-ba8f-97ca1ec37dab | -13.82584 | -43.85952 | 2025-09-10 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 852517a5-b3a1-3f5d-a8b3-fad68e55d193 | -17.32187 | -46.756 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a4071a8-48fb-375e-9e4a-f7d9a7f9b5b3 | -11.95354 | -46.64988 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 088669a4-04bf-3def-9e34-287ac1c2143d | -11.34355 | -46.53336 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3cd450f-6324-3fd7-a56f-25bce3e10aca | -11.28963 | -53.94537 | 2025-09-10 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85dcb07a-be1b-38b7-ae04-465dcd1660ba | -13.90971 | -47.96208 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 297e035b-43a9-392b-ae8e-2198aa748216 | -16.44997 | -51.97731 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee48de6a-b265-3802-a748-5fd8bc66429b | -15.77806 | -47.40215 | 2025-09-10 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7e8ed9e0-f658-347d-a4e2-4bdb4790ae94 | -15.00372 | -48.0293 | 2025-09-10 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 285970d7-2e6e-37ba-8a20-aa2de3b356f5 | -14.89991 | -55.86505 | 2025-09-10 04:17:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa924d5a-0a77-341a-91e4-e33c01d4e8b8 | -12.99623 | -48.0191 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79087559-2a76-3689-99c2-655df5101903 | -14.92403 | -55.92217 | 2025-09-10 04:17:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c45f420-d5ca-364e-a798-9683af71e238 | -23.03146 | -50.10779 | 2025-09-10 04:17:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 3a14901c-fb8c-3158-9356-c9cf4030adee | -10.56806 | -49.44334 | 2025-09-10 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a12c6aa3-3e20-31ed-9c5d-00bfa3896dd7 | -20.55259 | -47.62249 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a11336f1-a31a-3d96-97a1-e61081598d41 | -10.97272 | -46.79918 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc6df5e8-373e-3c70-b8e9-f64225ee9461 | -20.10885 | -47.81723 | 2025-09-10 04:17:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73b003f9-ffa9-33f6-b4cc-e80e84d71dd5 | -17.74915 | -44.48425 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26f76bcc-ea4e-3b49-a384-9bc624975d59 | -16.4594 | -51.97474 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86210705-4fa7-3e48-8341-7c2fef8a8d2a | -12.08901 | -43.32859 | 2025-09-10 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 830865cb-465c-3c97-bbf9-4bb06e967806 | -10.55795 | -51.49968 | 2025-09-10 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ff0de4f-7839-382f-a798-ab3b4c7b4f36 | -11.84214 | -46.75005 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d3c6029-937d-3486-9e2c-e2fdb716afd4 | -11.53706 | -47.31488 | 2025-09-10 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9877acc1-0b11-3a63-b538-25c18a3e423d | -15.81178 | -52.23219 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e63f36a9-b57f-38ca-8e95-6da73b0f4e7f | -10.57825 | -52.04647 | 2025-09-10 04:17:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52d43c81-cec0-3df1-94de-22ab2998f592 | -11.46484 | -43.63262 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 87ab4f31-ba2c-3e42-a978-20b0ed376adf | -12.41557 | -44.71546 | 2025-09-10 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 20e0d61f-d76a-3000-9514-dd8edac55c55 | -11.11683 | -48.41429 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8c56b40-d4a2-3bc7-a946-56fe33d30c7d | -15.80747 | -52.25495 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0663fed-5119-363d-94d8-8c1e36843120 | -13.0049 | -48.01162 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23af91ca-53cd-336a-b632-05fe568677e0 | -16.2885 | -45.67952 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1d1940d-90f0-3bf0-be64-2fdcbc1294ff | -20.15932 | -47.69814 | 2025-09-10 04:17:00 | NOAA-21 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ee2d2be-f192-3f89-a173-b3be2f190015 | -21.74914 | -48.7883 | 2025-09-10 04:17:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d54c186e-3ddb-3eaf-93ec-f9eb8ac947ad | -22.54362 | -43.55112 | 2025-09-10 04:17:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f6913b3c-ead7-33b4-a4d3-9d8ace73f01f | -11.20669 | -54.98409 | 2025-09-10 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| afb0174b-d9ff-3e5c-be57-bce3b57bd332 | -10.14751 | -46.17498 | 2025-09-10 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fecc27b8-1bea-32bd-9a0c-f9caee4ac217 | -11.29087 | -53.94941 | 2025-09-10 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3106571f-4284-3bf5-a39f-fd1d53e73422 | -15.80635 | -52.23652 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1aef24b-be41-383d-a2be-9139c0b27bbf | -15.10396 | -50.08144 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d7762a3d-b0c3-30bc-9498-cf0b6b9aebe4 | -21.31933 | -43.88573 | 2025-09-10 04:17:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| fa33e58e-0133-359b-ab54-36080f88b32f | -15.20551 | -46.24039 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9da668c9-d560-3e4d-8c05-3761661f54a5 | -12.20759 | -53.86952 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 018f8896-0946-3180-aebe-d117fed62c02 | -20.53225 | -47.64197 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cc0076f-87c5-3f9a-9c90-5c21119345ed | -15.72147 | -46.22772 | 2025-09-10 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 911a302a-c007-3360-b2f7-15afb1bccabc | -11.7695 | -50.58958 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43d0563d-a3df-3400-9d38-2bc800232c1b | -13.17654 | -47.24648 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16c0199d-0638-314e-90a6-15fbdd38ee0b | -22.19825 | -56.0259 | 2025-09-10 04:17:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34fb5b4c-80f5-30f6-9518-cd957de4c561 | -12.92823 | -54.79483 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43275b98-9a41-3b2d-bbde-47b24f4a507b | -13.19365 | -45.28345 | 2025-09-10 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4003e7b8-3dee-3bb5-968c-b76ccb89513e | -14.3094 | -44.8734 | 2025-09-10 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f7fcfc8-081c-31b8-9d1f-322b22b68a8a | -12.94334 | -54.80569 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 142eba88-1ba8-324a-907c-6facf5189c5c | -11.80527 | -46.76428 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b7298c1-8474-3b24-afac-23f0b49bdf13 | -11.12079 | -45.11329 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fdd35a40-c059-3a1d-bef1-6121b75bf6e5 | -16.2852 | -45.67896 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 193dffd1-a83c-3830-aa9a-1777cba490cf | -22.8772 | -48.13607 | 2025-09-10 04:17:00 | NOAA-21 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 630e438e-c8e1-32c9-a676-1cfeca7d3923 | -20.12589 | -47.69205 | 2025-09-10 04:17:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb00246a-168b-39ef-a0b7-6c38a9aa4805 | -17.7497 | -44.48056 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b66e0634-0963-3ca3-b240-70f03b6f8574 | -12.676 | -44.96351 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3343f73-4bd1-3430-91f8-08b96aca538d | -11.15815 | -48.35438 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35cde0f3-01c2-3842-a38e-483637e6d0b4 | -16.57579 | -49.22874 | 2025-09-10 04:17:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17824719-94b7-3ef8-938d-63be76cc2df8 | -11.46053 | -49.27012 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a56774fe-92e1-3b6b-9f27-79315eee26ff | -20.10488 | -47.8204 | 2025-09-10 04:17:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0797bc2f-3c8b-3242-a511-c21060cba7d6 | -11.13472 | -48.35551 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c157681c-0b56-3274-b7b3-1e0c2d7f5fce | -12.94259 | -54.80952 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9aa02623-b11d-3594-bbd2-8709e1a80b5d | -12.17698 | -50.62251 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 812be5b4-f8f7-32b4-87c7-5c55967356a0 | -16.67504 | -49.39471 | 2025-09-10 04:17:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 60205d6b-9e6b-3d73-a7bc-44222fde7376 | -13.79747 | -46.29406 | 2025-09-10 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ecd9a25b-00a1-39b3-a9e1-e2ab4e60bbac | -14.36503 | -47.31247 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e96f23d6-042d-3c01-aa2d-084d843ebd45 | -11.82024 | -46.75378 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90bf43a5-02b5-3260-9478-d8bcc97d3e2f | -16.62797 | -49.77485 | 2025-09-10 04:17:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f363283-9a9c-327f-bf68-2cf166322feb | -12.00313 | -50.98304 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b38eee6d-007e-396b-8a1a-5a64c55b8eef | -12.85086 | -52.94559 | 2025-09-10 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 390bf20f-560c-385b-8691-ab5e873d6deb | -12.14381 | -44.8437 | 2025-09-10 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ca540ec-442d-3310-af24-d4709f33111f | -15.10785 | -50.08234 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bbc06021-efce-31aa-9a94-bd99b33c38b3 | -15.87658 | -52.2054 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56dd64b4-118e-35bb-8443-7fddfb9fcfc7 | -17.85284 | -44.20431 | 2025-09-10 04:17:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f4d1e7e-0950-3bff-8689-2b0508266b3e | -11.84929 | -46.77118 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4197be0b-225c-3d98-b9fc-edbd1266f9c0 | -16.6936 | -44.34683 | 2025-09-10 04:17:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf5c8047-9429-304a-876b-7c04bbdc95ca | -16.71065 | -47.65355 | 2025-09-10 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 155211ca-e3b4-35fb-b8f6-875d43a48192 | -11.15908 | -45.27939 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c18728e-6b74-3d6b-b031-102e1030ee1c | -22.86772 | -46.40257 | 2025-09-10 04:17:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1c21c031-7260-3578-b181-0e69d5de3524 | -10.60139 | -43.30101 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b4e67d6d-72f2-30ba-90cf-20221a8f429e | -16.04305 | -49.97813 | 2025-09-10 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e12b3ebe-f4d1-3c55-a47c-2d353ba0d8b4 | -15.47296 | -53.04472 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 131450bc-51d7-3f85-a432-4245ee1b4655 | -11.85056 | -46.76347 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 554188d4-df3b-3f6f-88ce-ab8dd3894855 | -12.92941 | -54.75972 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1ef68808-cd0f-3c82-ad2a-af52ee32fce7 | -21.29374 | -45.96107 | 2025-09-10 04:17:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dd8a95c5-1e8c-39f1-9fa4-d6fa249af27e | -16.45739 | -50.67011 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1ea559d0-8939-30de-852e-0c5fdfaec2b4 | -20.13135 | -47.70076 | 2025-09-10 04:17:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1216b53d-6a8c-32f6-8f0a-2971c1cb198a | -10.0142 | -51.70345 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3d7ca8fa-c236-3fe0-af6a-eb890ee3a71b | -11.95506 | -46.662 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cab0a227-053f-3117-b5d3-a393459780fa | -11.13929 | -48.35146 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58e72578-85dc-3d73-9a0f-94e827446ff2 | -21.12571 | -42.91803 | 2025-09-10 04:17:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |


[Clique aqui para ver as próximas entradas](README43.md)
