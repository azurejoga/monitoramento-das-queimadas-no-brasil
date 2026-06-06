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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7e19514-fdcd-347c-ad1b-a86c0da13006 | -12.50702 | -46.28938 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13ffec89-4bdf-3195-9338-ccd55be692f1 | -11.79412 | -56.99655 | 2026-06-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78919c21-16a9-3394-986c-6db123bba3c6 | -10.85341 | -53.74039 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a56f628-1a04-37d0-81ba-41dbbb9661f9 | -9.90353 | -47.48123 | 2026-06-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a6827d4-e98b-3e22-9833-2869626f9145 | -11.54858 | -52.80115 | 2026-06-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f47bc26d-91e7-3220-8933-1feed93388ae | -12.4993 | -46.30142 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 93a0d90c-2560-3977-9351-644d79570a2d | -11.54963 | -52.79347 | 2026-06-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10ea1894-64c8-3af9-8c2d-5f96b8bfbd8f | -10.14534 | -48.07793 | 2026-06-06 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90c76dba-6979-3310-8432-dafa37da945d | -11.55744 | -52.79853 | 2026-06-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3952102e-ae9c-3f82-8b52-16911e2506ed | -12.2928 | -57.38534 | 2026-06-06 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5ea23b2-6484-3593-bb0d-b5fd9eca0b50 | -12.73547 | -54.20705 | 2026-06-06 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3789a1a1-cc74-37b8-a174-dfcdf8b6b0eb | -12.50643 | -46.29457 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb904ce1-302d-3854-83d6-878240a9d06c | -10.82152 | -56.60453 | 2026-06-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fae70a5-fb21-3b19-8c90-e5c295149b73 | -9.09623 | -50.61092 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecaaf28a-8183-31e5-b3c5-9ada27353607 | -8.93143 | -45.67464 | 2026-06-06 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f822859e-3282-3280-96ce-de191794f6fa | -11.00809 | -54.31477 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce5fb284-8654-3e0b-b5ce-30217f0b3dc8 | -12.06667 | -48.4273 | 2026-06-06 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f3334e3-107b-3c12-8707-c887cd7a02ff | -11.56215 | -52.79523 | 2026-06-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5da704af-7143-3860-a48d-169427884e9e | -10.2347 | -51.66168 | 2026-06-06 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca95404a-3e2b-3248-a9b7-e20f931ebdae | -11.55797 | -52.79466 | 2026-06-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b6767b1-aa2f-3d22-98c9-45156680525c | -11.6352 | -55.17705 | 2026-06-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f9b3382-b611-362b-8c81-7433d69a32e1 | -11.04287 | -44.32303 | 2026-06-06 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 052ece60-fbd1-3bd3-90a2-7c533e71362a | -12.50581 | -46.30208 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69110497-53f7-3d91-ad53-04b30e69f02e | -11.5491 | -52.79731 | 2026-06-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3594620-e4ae-3536-a86a-25dd3d42bc54 | -10.91415 | -54.13217 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e918d6dc-e32e-3c0e-8b15-c5a7366d46b6 | -12.29669 | -57.38225 | 2026-06-06 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6102511c-a45e-3201-9274-1b22ae8216c8 | -9.08156 | -50.61386 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6e8ec3a-4d9a-3094-937a-c73f1a857d2a | -12.49988 | -46.29602 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 137c9c09-3bd5-3749-9e06-c6a3e15f1b76 | -10.51054 | -51.94249 | 2026-06-06 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67e650f5-2e2a-3dba-b56e-92ff18261a7b | -9.0969 | -50.60588 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c44fbbf8-3391-3e8f-bd5a-1fa8ece9238f | -9.16803 | -58.06441 | 2026-06-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31cda667-e8ee-3d1a-972e-de3886aa94af | -12.5075 | -46.28641 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8d704c9-cf16-3398-a41d-fed46436d274 | -12.5076 | -46.28431 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8582646-5907-31fc-9bd3-8ed8e91426f2 | -11.79075 | -56.99602 | 2026-06-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 175e267a-4508-314e-9d6a-a4117f35c3ec | -14.22613 | -45.80338 | 2026-06-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a2f3c5e1-56fd-3ad4-aa6c-7cc5279fe067 | -10.84953 | -53.73981 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56d6339a-dfcc-3a69-873b-87467da79f6c | -11.5538 | -52.79408 | 2026-06-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 023afb84-f08f-3bca-aa61-b5e4fd6b3f96 | -8.46684 | -47.00063 | 2026-06-06 05:12:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c288483b-9d46-3aa6-b916-72cf43888d43 | -11.05506 | -56.92021 | 2026-06-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb977bd7-034e-3742-9a08-d5c6a0dba836 | -10.14727 | -48.08067 | 2026-06-06 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 814b622a-b0a7-3f04-ad00-6c6df08c4f42 | -12.50694 | -46.29156 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a1ef26f-36bf-3108-ad7b-1828ac709d7e | -9.00393 | -47.43694 | 2026-06-06 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a772205f-9a3b-3d71-b002-9fd417c33685 | -10.23516 | -51.66006 | 2026-06-06 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1a123cb-d0f7-3619-a0b3-744e371ff8bb | -8.86858 | -50.18935 | 2026-06-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dd7b103-180d-3c51-b7e3-e92c657dd540 | -12.50101 | -46.28554 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7bf2e644-736a-3b63-99c4-551b9d4d6ec3 | -10.90209 | -54.13519 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 768b2e18-3807-31fa-96e5-563f6d809028 | -13.40269 | -46.60364 | 2026-06-06 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 71e0d60b-0d57-3ca5-be79-2eb748f7d051 | -9.20537 | -58.06752 | 2026-06-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 936738b4-f19b-3376-ae80-52c7442480f5 | -10.51189 | -51.94159 | 2026-06-06 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26c4c3ee-3646-3955-b76c-af87223fd382 | -10.19103 | -52.64916 | 2026-06-06 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b65ef2af-b282-3ccf-8112-b353c3961287 | -10.57243 | -57.32181 | 2026-06-06 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 444bdb54-39d0-38ca-8fd1-6513b6b788ad | -10.00469 | -48.67477 | 2026-06-06 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cd5e6fc-1a03-3b16-be39-4088fdf64b0b | -9.17133 | -58.06493 | 2026-06-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6741cbf-e706-39b5-b865-04704b8c3b27 | -12.49994 | -46.29379 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d5c53320-3c4e-3a3b-bce9-9bcce0d99da9 | -10.85271 | -53.74541 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a500a1b0-5ec8-323e-a276-858d12535b38 | -8.86787 | -50.1946 | 2026-06-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d07f4c0-9367-3534-be98-12e604b39921 | -10.86189 | -53.73653 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5140b053-6ded-337b-8e65-a4ea3c442102 | -10.14166 | -48.07977 | 2026-06-06 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e165a532-7856-3da2-a550-6f1c6e4633a3 | -11.56161 | -52.7991 | 2026-06-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d647efc8-2ff5-3f95-8d77-480ca6ba55fb | -10.91481 | -54.12747 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebcc92d4-681f-3f1e-bf61-28010a26a581 | -9.07819 | -50.60327 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 09c658cc-6f8b-33bb-9994-413a4f8f1024 | -11.63882 | -55.17759 | 2026-06-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3913b92d-20e1-3e51-8e1d-3af14ea3aac3 | -12.50816 | -46.27948 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f41db227-caf4-301f-8df2-04eb14ad4f2f | -13.49812 | -56.56639 | 2026-06-06 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bacc7507-e2a0-3a57-a9bf-e1a8b46852d4 | -14.2453 | -58.44616 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4943d753-a686-3eab-b507-e536d05d2d9f | -13.49409 | -56.56978 | 2026-06-06 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63e94b18-293e-3994-afaa-d164e8fe7cc6 | -12.77428 | -59.00322 | 2026-06-06 05:14:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b4abff7-37b9-3850-b7c2-f0c1760db084 | -16.59717 | -58.23686 | 2026-06-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 97d83651-ff2b-3e50-9e61-110380210e38 | -19.75008 | -53.55114 | 2026-06-06 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 55b5d2b9-a564-3ea6-99fb-5cbd252af689 | -13.95322 | -53.96243 | 2026-06-06 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df864f7f-a610-340c-b35c-2b67e1883518 | -16.59772 | -58.23315 | 2026-06-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b049ac6a-44bd-3176-9827-e53fa0d6cd7a | -14.77517 | -52.68308 | 2026-06-06 05:14:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c819ce02-2a1f-3747-86b1-6dfa7b72cb16 | -13.60209 | -56.5973 | 2026-06-06 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 490c6e9e-2282-38ad-8533-9852fbc7f94b | -18.00038 | -54.28307 | 2026-06-06 05:14:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8a00b7e-5404-3a1c-82dc-225895de5b84 | -14.46407 | -54.89272 | 2026-06-06 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49b27470-2b66-39ec-a84d-370a4fc59568 | -14.0796 | -58.88093 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7b39a57-24f0-3d34-a919-b0bbc8c7d042 | -14.22782 | -45.80209 | 2026-06-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 517b7f8e-e814-35b5-b0bb-c42c35ca457c | -19.75062 | -53.54661 | 2026-06-06 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d45cb282-8f84-3705-b87f-430bafe47bd6 | -14.77573 | -52.67871 | 2026-06-06 05:14:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 640cc7f1-8ebb-30ee-9fcd-3d49fec16de6 | -14.26956 | -58.44279 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ff63147-e80a-3a98-a0ca-a6bb04185524 | -14.26902 | -58.44636 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 948b3209-ea80-3cd1-bd29-0c3416c8051d | -14.07905 | -58.88446 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2d62aad-80f7-3a5b-bd16-e843d5af289d | -14.21208 | -57.42688 | 2026-06-06 05:14:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f19d992a-34d0-374b-bc9a-25bfb6568ffc | -14.24915 | -58.44313 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27bbf526-7814-39ce-8f1b-91e820f85eb8 | -14.17543 | -58.94339 | 2026-06-06 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85928756-8e89-3e90-b403-5c7cc7c2f21d | -16.60108 | -58.23369 | 2026-06-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 75011c5c-b5a6-3c55-8442-0079c8e9149e | -14.24833 | -47.97436 | 2026-06-06 05:14:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f9138b4-a6a7-35f5-97b6-9b17efe0237d | -16.14803 | -58.49265 | 2026-06-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b6cffdac-ca85-3564-a585-805679a7ca72 | -15.39116 | -55.91155 | 2026-06-06 05:14:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e68f3eeb-bb21-38e9-9af7-da13876ad8dd | -14.22162 | -45.79493 | 2026-06-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 19e679aa-5aa8-3d6b-9dd8-aedfe4cca27d | -19.74117 | -53.55011 | 2026-06-06 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 72fe05d5-1997-3311-9d31-fa6fd45f9c0a | -19.73618 | -53.55416 | 2026-06-06 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfb1ae40-ef23-3800-a715-60d38e454f58 | -19.17204 | -55.1824 | 2026-06-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 695b0b47-68c7-3814-9cbe-9acca3344fb0 | -16.14081 | -58.49522 | 2026-06-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 55bb8cfb-6628-38e2-814c-cfb0f4762f7f | -14.46027 | -54.89217 | 2026-06-06 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 32303808-f2b4-3a52-bc41-981f2333ff98 | -14.77077 | -52.68254 | 2026-06-06 05:14:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c1e1834-3853-386e-9cfa-2037cd6b7c11 | -14.24784 | -47.97892 | 2026-06-06 05:14:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61b7c7d1-ce25-3aa1-994d-5171929f2934 | -18.00453 | -54.28363 | 2026-06-06 05:14:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cef6a703-491c-3ea6-b62c-7e37a7d1f679 | -19.74171 | -53.54552 | 2026-06-06 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 26ce579b-2331-33ac-9da5-22230974de69 | -15.4482 | -55.87571 | 2026-06-06 05:14:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README12.md)
