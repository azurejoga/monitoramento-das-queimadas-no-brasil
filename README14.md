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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5fa4616-c8e1-39c0-8749-f3947822eb62 | -11.8939 | -57.1155 | 2026-06-29 15:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 2bdae4f2-9672-3c58-a7aa-38e005f57e91 | -11.9533 | -58.6192 | 2026-06-29 15:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 1fe57ef5-44c9-33fa-92ec-44d175380f2b | -7.8035 | -48.1649 | 2026-06-29 15:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 856d24db-b268-3cd1-a136-9399adc3ec62 | -12.2222 | -56.5467 | 2026-06-29 15:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f8d4fcfe-5940-3780-afcf-f8b361b49138 | -8.0124 | -46.2699 | 2026-06-29 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 8fc62967-d631-3630-b0f9-384a6be38fe6 | -11.2148 | -53.833 | 2026-06-29 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 4e8ce739-fede-3939-b072-79b933ca6042 | -11.0414 | -55.7411 | 2026-06-29 15:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 7edbb196-4df4-397e-a716-bf3c60b3e4cd | -6.8952 | -43.6833 | 2026-06-29 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| a11fcbb5-15e0-3055-a3b3-19f1f7400aa6 | -12.2222 | -56.5467 | 2026-06-29 15:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c0df78dd-9baa-39f0-8651-233044e46007 | -12.5135 | -48.2802 | 2026-06-29 15:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9fc4374e-4fe4-3437-801c-8a27b2ead9e7 | -11.8939 | -57.1155 | 2026-06-29 15:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d2151b93-c7a9-3f00-8a49-ecf59d33ca20 | -17.7126 | -46.7565 | 2026-06-29 15:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 8f425db7-253a-3229-acd2-64d658f8e1f7 | -9.6037 | -56.9276 | 2026-06-29 15:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 1b8b1b21-f470-36a9-9e94-5b0598065b2d | -11.06 | -55.7597 | 2026-06-29 15:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| c4eb22e9-1aaa-3af0-a442-d4045d769d73 | -11.9441 | -57.7091 | 2026-06-29 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 5a6cddea-f93b-31c3-8955-0db4a01bc3bd | -11.5085 | -56.1251 | 2026-06-29 15:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 33e60e8d-074f-3cb7-80b4-912f8c31dce5 | -11.0414 | -55.7411 | 2026-06-29 15:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 01e14a7b-c49d-39c5-85d2-a6617ea919bf | -11.8937 | -57.1355 | 2026-06-29 15:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 7c9e498f-2229-3bf3-b8dd-90eba8b33d2e | -6.497 | -42.238 | 2026-06-29 15:20:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| d8a09f08-a92c-3404-a8fa-4a7a72235c8a | -11.2148 | -53.833 | 2026-06-29 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 6307d446-d65b-3088-acd8-1c1deda2d9b4 | -17.712 | -46.7798 | 2026-06-29 15:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 5977d7ea-278d-3034-a3ec-c883a5356554 | -11.9533 | -58.6192 | 2026-06-29 15:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 2cf14fe8-a19e-36ae-9fe7-6e66d2750c9e | -12.4464 | -58.4825 | 2026-06-29 15:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 657.3 |
| 4a68f539-048a-31e5-b84c-44ebc21bab1c | -17.712 | -46.7798 | 2026-06-29 15:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 71c95887-2ed9-3016-8a09-e07285a2fa45 | -6.497 | -42.238 | 2026-06-29 15:30:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 99878d7d-bd13-3b07-a3e0-548345717e9a | -11.8939 | -57.1155 | 2026-06-29 15:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| aba0f9ef-13c2-31dc-ab2a-681d25a95d16 | -12.2222 | -56.5467 | 2026-06-29 15:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ebe2e800-a631-35a2-9b68-02d00778b5e5 | -11.06 | -55.7597 | 2026-06-29 15:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 181.5 |
| c4671b65-f921-3086-b3d6-9c3d7d74c1a8 | -10.3128 | -57.1367 | 2026-06-29 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 0c10f481-3d9d-3e7a-a943-1bfe968ddb5e | -7.1927 | -47.4941 | 2026-06-29 15:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 39c42476-e030-3b37-b579-b5ed7eff3940 | -9.3327 | -58.0298 | 2026-06-29 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5f254d33-ebbd-301c-8c35-b0e1c932419d | -11.9441 | -57.7091 | 2026-06-29 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 90cef795-0b0f-329e-b244-600c5d134b00 | -9.6037 | -56.9276 | 2026-06-29 15:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |
| 9a02a15e-4c81-3556-b18f-06e8e5fc913d | -9.314 | -58.0309 | 2026-06-29 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 35d676a7-9ac2-3089-96cb-3c7e0989de9b | -11.0414 | -55.7411 | 2026-06-29 15:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5b2c80ad-85f7-34a5-974d-ceb47bd02ef6 | -12.222 | -56.5668 | 2026-06-29 15:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e1a51421-e2a9-3228-89c7-9685b2a766e4 | -12.5135 | -48.2802 | 2026-06-29 15:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 002e9a9d-a5d5-3171-b9fe-c0860d0ddf38 | -11.7196 | -59.344 | 2026-06-29 15:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 2296efd4-4bc4-3588-9bce-c3c588f347e6 | -11.9533 | -58.6192 | 2026-06-29 15:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 9a7f3c09-64cd-37e4-a0aa-4d94bf9aae23 | -11.5085 | -56.1251 | 2026-06-29 15:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 2897f91e-94cc-3366-b2ce-a36e7030aac7 | -11.8937 | -57.1355 | 2026-06-29 15:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 09e46745-cea9-32ed-b441-439b34325380 | -6.8952 | -43.6833 | 2026-06-29 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 7705317e-ecb6-320d-8dcd-f3ee0254c6c9 | -11.2148 | -53.833 | 2026-06-29 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 560a4ae8-19d7-3c62-8449-f6eb4d249f3f | -10.313 | -57.1169 | 2026-06-29 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a024d902-667b-352c-9302-2871043a3194 | -10.9882 | -49.5618 | 2026-06-29 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 27540d68-478c-38b4-bebf-52d34d5683b5 | -14.2516 | -58.8277 | 2026-06-29 15:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 144.2 |
| a63ca380-ac7c-374f-8d32-3953972be7de | -12.2222 | -56.5467 | 2026-06-29 15:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9809c09c-14ba-3f14-a1a5-2b4102b55cfe | -9.314 | -58.0309 | 2026-06-29 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 7a4a33f7-2f02-3fe0-9fe0-0a4451c66fa1 | -11.9533 | -58.6192 | 2026-06-29 15:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 374fd63b-a44e-37eb-b581-47ec637b41b9 | -11.9441 | -57.7091 | 2026-06-29 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 5e93f4a4-d216-32ed-91fd-0d6ddc52a1d3 | -12.222 | -56.5668 | 2026-06-29 15:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| a3668a86-dac2-3425-a521-a4ffea22bbaf | -9.6037 | -56.9276 | 2026-06-29 15:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 77f40b0f-a71a-323a-afc4-8ff42ccf9a5e | -11.9286 | -57.392 | 2026-06-29 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 184013a6-143f-3ace-bbad-40849d3b0d9b | -6.8952 | -43.6833 | 2026-06-29 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| eaaaeea4-922c-33dc-adac-51d340ca2c84 | -11.2148 | -53.833 | 2026-06-29 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| da94a40d-39fc-3706-8b1b-b8929be12a54 | -9.3327 | -58.0298 | 2026-06-29 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| de12907b-5230-3990-b5ba-54522547eeac | -11.8937 | -57.1355 | 2026-06-29 15:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| ffee7455-6143-3e72-b073-d304eaea50da | -11.8748 | -57.137 | 2026-06-29 15:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3f9bd4c7-bc77-34e1-b436-3422d7c91422 | -9.3329 | -58.0102 | 2026-06-29 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 3de94d3c-e29d-3239-9fd3-f8eee67a9cc4 | -11.8906 | -57.415 | 2026-06-29 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| fb71e840-4d22-39ea-94ca-7c7acf012030 | -11.9284 | -57.4119 | 2026-06-29 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 5029e2dc-86e4-3c1e-ad70-4d9cea0dde7c | -11.06 | -55.7597 | 2026-06-29 15:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 235.8 |
| cb7e4b54-13e3-3e85-bd32-aa84a5a5f1c0 | -11.7196 | -59.344 | 2026-06-29 15:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 14b26344-95b0-30ea-910e-a06d67b9dbfe | -11.5085 | -56.1251 | 2026-06-29 15:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| daad1b14-38f5-37d0-92fe-8a8b50214422 | -17.712 | -46.7798 | 2026-06-29 15:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 07984cb1-438b-3766-96bb-fb95e4f1299b | -17.7126 | -46.7565 | 2026-06-29 15:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 4fbd80db-0674-34b6-9c88-5964f564d0fe | -9.3142 | -58.0113 | 2026-06-29 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| a07ab383-50b7-319f-b8bd-314643f1f9a8 | -11.8939 | -57.1155 | 2026-06-29 15:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 7055a05b-1d76-36e8-87fd-40d327cccabc | -6.497 | -42.238 | 2026-06-29 15:50:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| daabe924-00aa-3751-8469-63e154b49d23 | -6.8952 | -43.6833 | 2026-06-29 15:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 0006ba9f-4284-3781-8826-18881c856bd6 | -9.3142 | -58.0113 | 2026-06-29 15:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 76b03e45-f230-35ef-a47d-888e8e723fb7 | -9.314 | -58.0309 | 2026-06-29 15:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 4c2acf13-bd66-35b0-8209-bff7999eccc8 | -8.0928 | -50.9221 | 2026-06-29 15:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b95a91cd-ece2-37f6-806e-0b6fd5364894 | -6.8952 | -43.6833 | 2026-06-29 16:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 1e856146-0d25-3b25-b0b0-166d1f97eb3d | -9.3142 | -58.0113 | 2026-06-29 16:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6302c9aa-8f9d-38ec-b88e-dc482da7cbf3 | -12.4656 | -58.4612 | 2026-06-29 16:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| fa4404c3-f50f-3646-ba6c-7137c51749d5 | -17.712 | -46.7798 | 2026-06-29 16:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 53380669-d22f-3c31-8f39-e2e81d724879 | -12.222 | -56.5668 | 2026-06-29 16:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 1f623aa2-0e72-3a3c-9f5c-cb6a5f1ece1a | -10.2942 | -57.1182 | 2026-06-29 16:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 880fd1ec-0985-3bfd-ad73-4227e193e440 | -11.8939 | -57.1155 | 2026-06-29 16:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| ca8696ca-c67d-3c0b-adb1-cc5258a8f651 | -13.2198 | -54.4356 | 2026-06-29 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 2ce93538-2158-3663-942b-b0dece8f9c2b | -12.2222 | -56.5467 | 2026-06-29 16:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3e54b252-c1a0-343a-a0b4-a68f5533ccb2 | -11.9441 | -57.7091 | 2026-06-29 16:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 250f604b-e734-31c7-b68a-2c180d035055 | -9.314 | -58.0309 | 2026-06-29 16:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| f46007a6-00ee-30cf-95ee-081de2e946bf | -9.6037 | -56.9276 | 2026-06-29 16:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 26f3d577-0de9-374b-ae78-28188fb0359e | -11.8937 | -57.1355 | 2026-06-29 16:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 147.8 |
| fc3282b8-a9a7-3ee6-b7a9-4d73ca8bf949 | -11.8748 | -57.137 | 2026-06-29 16:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e4835a50-28a6-31f0-93bc-ba27cc68c228 | -11.2148 | -53.833 | 2026-06-29 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 1ddb515e-e4ab-3387-8ddc-3de4182acafd | -17.4442 | -47.1582 | 2026-06-29 16:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| cdce0b89-160c-3e75-9e00-3a83c7e691ee | -11.0414 | -55.7411 | 2026-06-29 16:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| ee8abf2f-b032-35de-87d3-b484568bd984 | -8.0928 | -50.9221 | 2026-06-29 16:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 64805250-3bf1-3895-8b7f-46c89aab581b | -6.497 | -42.238 | 2026-06-29 16:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| e53b21fa-d37f-3109-ba13-fdf194d59745 | -11.7196 | -59.344 | 2026-06-29 16:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 40873b84-4f68-369d-aa79-4af407688c59 | -11.9126 | -57.1339 | 2026-06-29 16:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1e5a77ad-7c93-37c9-a30a-5ad2164ee6de | -11.9533 | -58.6192 | 2026-06-29 16:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| f6ac35a9-fa88-38c1-8016-74326a00968e | -9.3329 | -58.0102 | 2026-06-29 16:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 149.2 |
| d7d02633-7249-3a68-9148-790665c51e41 | -11.06 | -55.7597 | 2026-06-29 16:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 267.8 |
| 28d96c9e-0959-33d2-8730-b5ca9e4156c0 | -11.9284 | -57.4119 | 2026-06-29 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 32da764b-8b53-3412-a371-23c7e3abb3cc | -11.8939 | -57.1155 | 2026-06-29 16:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| b62b2fe5-aff7-3d4a-ad27-27cc4e7485db | -8.0928 | -50.9221 | 2026-06-29 16:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |


[Clique aqui para ver as próximas entradas](README15.md)
