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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 843a5137-648b-3bfb-8152-1840b3d9554f | -10.82587 | -54.05106 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a97549d-7569-3086-8b1d-b32ec47bb882 | -10.62806 | -46.69081 | 2025-06-27 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9baa702d-5597-3b2b-a3bc-23f69b759a17 | -8.47545 | -48.26232 | 2025-06-27 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 352dc949-960c-35e6-a49e-226801cb3cfe | -11.36538 | -48.7093 | 2025-06-27 04:49:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1822d6a3-c531-3d2b-9634-a7ba446bbace | -10.82194 | -53.73109 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcb164cd-e5e3-339c-a18d-606d56ac7be6 | -11.4434 | -54.47385 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e3f5292-bf5b-3b93-a96b-ffcc78c75845 | -11.18338 | -55.91356 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e13a251-7570-3dfe-8881-527786d9b84b | -14.2342 | -45.50698 | 2025-06-27 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e38cf567-ba22-3e48-a909-5342444e46da | -11.05543 | -55.37794 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dff04a61-a9df-354c-870d-b678894c17a8 | -10.86403 | -54.30462 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83647822-e4d3-39d6-8ee0-b9749ba7649b | -11.05907 | -55.37735 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0f437e91-6d4b-3079-8bab-e6666bac872b | -9.97313 | -48.24614 | 2025-06-27 04:49:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a17f6ad6-7e1d-35c5-9d63-3ad110b947d7 | -10.706 | -59.12433 | 2025-06-27 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 774a8a5f-1711-31d0-8926-1f786ef9a20e | -10.83213 | -54.05604 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97838e8f-61df-37a9-a22e-4f11b76a026e | -8.2625 | -47.01187 | 2025-06-27 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e77aa30-f45c-3fa6-9c74-5374800358d5 | -11.57338 | -52.11206 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4e6a4996-7b25-3971-a7db-20fec47f2f57 | -9.06698 | -46.90873 | 2025-06-27 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc3873cd-0585-306e-ab8d-e48fd1e1820a | -10.42306 | -47.51152 | 2025-06-27 04:49:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e725fa4-efd1-31dc-8579-075a43c0a546 | -9.07308 | -49.42371 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b901de6-de23-33a9-b496-2fe6f8df6f37 | -9.8226 | -48.38089 | 2025-06-27 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 80b917ea-6dd0-3b6e-b83f-4cb48b5c46a5 | -9.74943 | -48.04108 | 2025-06-27 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 034cb1ac-9709-35f5-93f9-3a752157c623 | -10.83398 | -54.0447 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7b956f6-14db-321d-8120-4d7f87972472 | -11.18242 | -55.91582 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4e56382-2336-36ca-97ca-5c984c79480b | -11.58582 | -44.66907 | 2025-06-27 04:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a2c5b32-e1d2-3d7d-bbc1-1a06d2aed541 | -9.09319 | -47.96719 | 2025-06-27 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82fb2fbf-cdd7-3875-a4db-da9f94fee506 | -8.47482 | -48.26653 | 2025-06-27 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c2d7ca34-ced7-3567-90e0-9a5282da3aef | -13.06067 | -51.63935 | 2025-06-27 04:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18501541-082a-3877-afb1-1276d0c2496f | -11.77168 | -55.03539 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 656f2350-0827-3f32-b584-da7fa5bfcc20 | -8.67738 | -49.95627 | 2025-06-27 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7385bb72-bdf7-3f31-8b64-c122176cd161 | -8.62358 | -51.57478 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1696c337-88bc-36b5-b629-3186730292c1 | -12.10888 | -54.66263 | 2025-06-27 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3caf4b40-c3de-3dec-901c-590f9f687ce8 | -12.00391 | -47.15883 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6355457c-2a68-382f-a673-5da70412242a | -11.58622 | -44.6732 | 2025-06-27 04:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca141e3f-5c50-304f-b9a0-00fa0c520b8b | -8.48273 | -48.26345 | 2025-06-27 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c5cbbfc1-a759-342a-b37e-0ea9840e3b49 | -11.18106 | -55.92699 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0881f5b1-89e1-3f51-984b-3c1444ff0511 | -10.70978 | -59.1298 | 2025-06-27 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edac20e7-725b-3a48-b16d-ebd93d95b66b | -6.9416 | -42.8834 | 2025-06-27 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| dcf0fca2-37ce-3ec1-ab0d-22f45014e576 | -6.9414 | -42.907 | 2025-06-27 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| ecbc3277-93e1-3889-af2f-fe881b819f78 | -6.9605 | -42.8816 | 2025-06-27 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 250.0 |
| b0b4d4c8-f302-3f49-8846-d02e8c666a37 | -6.9602 | -42.9052 | 2025-06-27 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 313.9 |
| d62e110e-ef73-3594-a248-1a5e18d989e5 | -11.559 | -52.117 | 2025-06-27 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c3d4d1ef-f775-335e-b94e-54e12bed4519 | -11.5969 | -52.113 | 2025-06-27 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 4cf019e3-cde3-3f9d-b212-bd33086d9aee | -11.5782 | -52.094 | 2025-06-27 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| b79e7e75-4936-3403-afa6-3a6761974bc1 | -11.5776 | -52.136 | 2025-06-27 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7d30527d-8bfc-3cf1-957a-eefcdb40a078 | -11.5779 | -52.115 | 2025-06-27 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 253.6 |
| 81f852ca-1bb7-3bb6-828f-ccd02d2a9bf3 | -6.9793 | -42.8798 | 2025-06-27 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.2 |
| bfa00c55-82d8-3c08-8062-6477ab7a044c | -6.9791 | -42.9034 | 2025-06-27 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 169.3 |
| b0f8b523-e0f8-3acd-b21c-6b372dea65a3 | -14.44182 | -48.87018 | 2025-06-27 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b3b13187-fda6-38d5-8a1b-f2d2827b13a5 | -20.92019 | -45.78915 | 2025-06-27 04:51:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b04b6786-411b-3fd0-a114-beff52783e88 | -12.60643 | -57.88166 | 2025-06-27 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60e234ef-ab90-3698-af97-fa905af8605f | -15.62193 | -46.4648 | 2025-06-27 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b01acc6c-20ec-3bb0-8f28-0d287b8300a8 | -14.01486 | -54.48977 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f16c5b6-4aec-35ca-a21f-0d8e4972e8ee | -19.02194 | -57.62016 | 2025-06-27 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 29ea704d-9a3e-376a-95e7-ff351b61b346 | -18.94901 | -39.91365 | 2025-06-27 04:51:00 | NPP-375D | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fd33327e-f01f-34ca-ae86-4f7e9445553c | -14.53422 | -53.8326 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77f91134-4a5b-3954-99f2-de17f306e570 | -21.10971 | -43.80677 | 2025-06-27 04:51:00 | NPP-375D | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 01732f88-9eb8-3a1c-90f0-3783fa0f2799 | -13.94553 | -54.48542 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b952c8bf-fe49-3abf-9e0f-606df59cd686 | -13.14321 | -56.8035 | 2025-06-27 04:51:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 02560082-3bf8-3763-8a6c-a36fe263c2a6 | -19.02292 | -57.62237 | 2025-06-27 04:51:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 16d7bad2-07c1-34f1-a353-798f4a54ec2e | -13.9294 | -54.49814 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b0d82d6-fff2-3ced-a20b-4aad31f9ff37 | -14.31289 | -59.89545 | 2025-06-27 04:51:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f08b5788-40c7-3d91-9cdd-9675eba37d26 | -20.41515 | -43.55108 | 2025-06-27 04:51:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7e55df00-07d6-373e-ae0a-cbf3f5292bbd | -19.58036 | -49.10469 | 2025-06-27 04:51:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 855001b3-9a8a-3bb7-a706-299e9f26ae1f | -11.83204 | -62.76534 | 2025-06-27 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a82947b-6510-39aa-b17a-e104b8e20ea1 | -16.6818 | -43.88329 | 2025-06-27 04:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3a84fd2-e93a-3f27-9f17-28c0c5320cfb | -18.66219 | -55.75428 | 2025-06-27 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a52310bb-40bc-3357-961a-88e6bd10c50c | -14.40671 | -47.88993 | 2025-06-27 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85487199-7d2a-3c2e-a03d-4702d82c1f24 | -20.92629 | -45.78918 | 2025-06-27 04:51:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53d20c83-0e34-3731-bbf7-c5dee43ac8a0 | -13.93809 | -54.48799 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1edcf080-c345-31e8-a919-80c1339b1247 | -16.7093 | -49.35749 | 2025-06-27 04:51:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2c91f7f-fd7c-3af7-8af8-d390d8a93e20 | -17.04692 | -45.88917 | 2025-06-27 04:51:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c555ff2-bb82-361a-a560-67dea7467690 | -13.93281 | -54.49872 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9388c2d0-dad1-3176-9892-b7f692dd8240 | -17.04571 | -43.7726 | 2025-06-27 04:51:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b35e1db-5809-3bfe-8de3-2770e5ceffe9 | -13.94087 | -54.49235 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5bfcdb1-99e6-3151-8bfb-53c9f6a9675f | -14.43802 | -48.86965 | 2025-06-27 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cdd8efe9-36f4-3ba8-a896-c9fd1451ce9f | -14.44249 | -48.8655 | 2025-06-27 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 83bb444a-49ea-3369-ae14-47f80278a540 | -18.65942 | -55.74977 | 2025-06-27 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e8223f4a-c351-3e68-a306-a9df6b8f7ac3 | -12.61054 | -57.8824 | 2025-06-27 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44e893ad-89b8-33d0-aa65-f545a9b4002d | -13.94831 | -54.48978 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f6a1839-684e-308e-9784-59ea03542e4c | -14.5364 | -53.84041 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b349dc31-2245-33f5-b0e7-f0333a1758cd | -14.44557 | -48.86388 | 2025-06-27 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcfefea9-8885-30cb-a5cb-6e869df428e4 | -14.01826 | -54.49035 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d2386e5-a855-3cab-b7d3-946e522ca041 | -12.59411 | -57.87941 | 2025-06-27 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6503391b-cf26-3328-856c-99c6700e7229 | -13.93962 | -54.4999 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d7f9214-d1af-3d0f-b78f-6f0b78c742b9 | -13.94428 | -54.49295 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4fb342e-f3ce-3ba4-9676-484d0dc32d61 | -14.53698 | -53.83678 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1f14fcc-b88b-3fbd-8331-d8cfc2a07122 | -20.41478 | -43.55515 | 2025-06-27 04:51:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 707584f2-8537-3b42-8a49-76b292590be0 | -14.40211 | -47.89363 | 2025-06-27 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 640d7d4e-cd48-3d43-aa5c-b4f3e4ace43f | -13.94365 | -54.49673 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3f5d543-eeea-31a3-9807-3b1f6f35aa51 | -14.312 | -59.9002 | 2025-06-27 04:51:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 584be809-5fab-3c11-aa53-5daf219a15f2 | -21.11102 | -43.80514 | 2025-06-27 04:51:00 | NPP-375D | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3e56ee0-c4fc-3853-becb-d7693614e96c | -16.29128 | -52.92784 | 2025-06-27 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e801708-33a8-368f-bd0a-58432f91384b | -11.83126 | -62.76934 | 2025-06-27 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 365952f6-e4df-3940-b0d6-e11df59478ca | -14.04252 | -50.51907 | 2025-06-27 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca017d7c-9c10-31e2-985f-42d03343c51a | -14.01424 | -54.49353 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df030652-bac6-3d03-b903-e7dc91941d33 | -20.76296 | -46.768 | 2025-06-27 04:51:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e3b32ba-887c-350b-9e9d-405c3ad8820b | -14.53757 | -53.83316 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c042d71d-99bf-36f9-a891-353b586614e1 | -20.92123 | -45.7887 | 2025-06-27 04:51:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7dcd2de-44a3-3f41-976a-65b1c044c817 | -14.4102 | -47.89442 | 2025-06-27 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72f3b957-529e-316a-80ea-53d767d451a8 | -13.14239 | -56.80825 | 2025-06-27 04:51:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README24.md)
