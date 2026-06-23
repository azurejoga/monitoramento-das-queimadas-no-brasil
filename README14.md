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
| 8e42bff6-85f7-35d9-9894-e538dc47d574 | -11.66828 | -56.76294 | 2026-06-23 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63c14c6a-c75e-331c-bc0f-f3474d536881 | -17.68796 | -47.23424 | 2026-06-23 04:53:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2eb89900-bf85-338f-9c8e-928576f09e32 | -12.3668 | -45.68925 | 2026-06-23 04:53:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb7e8987-0ae2-311b-b409-35dd9f0c71a1 | -12.50241 | -48.26826 | 2026-06-23 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| aea0ea2a-8b8d-3155-adb6-d555d69973d9 | -11.80344 | -52.52291 | 2026-06-23 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c2edc0e-dd8c-3473-ac64-6fc28f822530 | -12.43359 | -58.41194 | 2026-06-23 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dc2bb56f-27d8-38ea-aedd-3fcfc3be6d37 | -16.12259 | -58.49968 | 2026-06-23 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bd7a6815-f0b3-362e-9f05-f35b3d07a880 | -13.50148 | -56.57616 | 2026-06-23 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ee7ed9f-14b9-3387-ac61-8b19da991c84 | -17.93165 | -47.02219 | 2026-06-23 04:53:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 860b6612-3953-3aaf-a199-40a8d6c1af51 | -13.50214 | -56.57224 | 2026-06-23 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61863868-9f76-3e74-b30b-cce3989a8254 | -11.21108 | -54.34315 | 2026-06-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 558735fa-c98e-359a-b678-9bccf0714bd1 | -11.81273 | -52.5241 | 2026-06-23 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a89c1e1f-3b7b-34ea-b936-09e371decf04 | -16.03325 | -43.41461 | 2026-06-23 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24739239-408d-390d-8c4c-f3a9bd9d32f5 | -16.02677 | -43.41841 | 2026-06-23 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7741347b-db11-3b28-a1c7-0ed6ed95f2d8 | -11.80678 | -52.52343 | 2026-06-23 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a9879b5b-23ba-3058-93a0-0f8b0c498b2a | -11.27875 | -55.79123 | 2026-06-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ada058f1-d907-3a3d-b3d4-236dc6b1d0b6 | -12.85304 | -44.36921 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0ae2b8e-c34b-340d-a7ec-4211b85ab49b | -15.38649 | -40.82277 | 2026-06-23 04:53:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7f470574-e708-38c1-b29b-07922540e364 | -11.81219 | -52.52769 | 2026-06-23 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8029fea7-464a-3fc3-be91-da38d50f3d44 | -12.86519 | -44.35994 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6a71e3d8-24ae-31ec-890f-c52e09c77112 | -12.28905 | -57.57153 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2d57ea9-a37a-3260-b8e6-0f66a90d69f6 | -11.51281 | -56.11985 | 2026-06-23 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 654afa6b-a04f-36f0-8239-fef5f691c191 | -12.2883 | -57.57601 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a8dd7d4-c540-3651-9784-f3360fcb4f70 | -13.52276 | -52.17114 | 2026-06-23 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9edc66e8-d7ec-3022-a56e-4d9cf8c314a0 | -11.21164 | -54.33962 | 2026-06-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a79bbf65-8aa9-30a4-877e-338a4d8feb1f | -11.30694 | -54.72387 | 2026-06-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68970a20-9c83-3281-8a5c-60be4806f100 | -12.84844 | -44.36139 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 345d2d22-ea4a-3230-ab84-379f6da1f22a | -11.54612 | -52.78226 | 2026-06-23 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 385e5f5a-b12f-390e-bf48-439b60b3f858 | -11.28158 | -55.79561 | 2026-06-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c29f6a19-0de5-3e0d-8c8e-29055d1055f6 | -12.51946 | -48.29831 | 2026-06-23 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 39cf3a42-c404-3cf3-b6a2-1103af9daddf | -12.88286 | -49.84001 | 2026-06-23 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71a1c3fe-809f-3fd3-bd5e-9628b6b73ed8 | -12.87609 | -44.36124 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac216e03-f55f-3e75-a6c7-920e68e742cc | -12.68506 | -54.57745 | 2026-06-23 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46c4569c-669c-3f99-8717-aa71f848775b | -12.92106 | -49.47543 | 2026-06-23 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f39a2e7a-8eb6-39d5-8ac8-bf5aec81b742 | -10.93363 | -56.84807 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e74d438-1976-3ca3-91b9-756cefb10c3c | -12.11074 | -62.81893 | 2026-06-23 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f15ce290-f27d-30e4-99dd-fe1b634c179f | -12.86017 | -44.35569 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| feafe71c-c639-35ff-b800-2f5fc1242c5f | -12.06973 | -48.42552 | 2026-06-23 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 935c4a3d-3533-3e63-baf4-f83cba39f3a0 | -12.85848 | -44.36991 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 74772af3-5436-3fe4-8131-ccc1f9c7d4d7 | -12.4852 | -43.72642 | 2026-06-23 04:53:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20aabc29-7f17-3c05-ad94-abdd790bc2ab | -12.51531 | -48.29773 | 2026-06-23 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b3674fbe-8fa1-3b6e-9ced-ade68042ab45 | -12.65976 | -47.6734 | 2026-06-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dde69f6-e082-39c9-9120-1e8738ba54f1 | -15.89834 | -59.87799 | 2026-06-23 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3d06403-2e5c-3a6d-aa60-62ab4985ba49 | -12.84802 | -44.36494 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55d738d1-1575-3f27-93db-09966f578db1 | -10.93725 | -56.84871 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dff78b9-f6bd-307a-b914-714a34d1f152 | -12.87566 | -44.36482 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1378814-defe-3196-a279-9738bab8f455 | -11.5428 | -52.78174 | 2026-06-23 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 345af663-6248-3e96-a103-4cf1bccdb757 | -17.93497 | -47.01876 | 2026-06-23 04:53:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0927c04d-7955-37e4-8795-87007977f670 | -12.86894 | -44.37487 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 801a312e-787e-3313-a440-72eb7abf8dca | -11.3036 | -54.72332 | 2026-06-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82761d9c-0712-30f3-8f75-e26e9b209011 | -12.86604 | -44.35281 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fdacbfab-bb4c-363e-ad7e-1dd4641013e8 | -10.27335 | -60.54604 | 2026-06-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b38094c4-7312-3f8d-9801-a11119071ac4 | -12.50604 | -48.27275 | 2026-06-23 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b6e58d29-af9d-37b3-a7e1-01ffcf98c6ae | -11.87128 | -57.83465 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac79457a-1ae2-33c1-990b-8737260a538d | -12.92038 | -49.48038 | 2026-06-23 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cac436b5-c839-3286-b026-6cfdedb1d8bd | -11.30515 | -54.47865 | 2026-06-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f01c9792-6823-3bd7-992d-7ef54cd98ebe | -11.87505 | -57.8353 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23566e7c-fb68-3933-b73a-e89c3ab7ca68 | -11.63008 | -55.18881 | 2026-06-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f9a9500-bd52-3717-8754-528571bfd444 | -12.42972 | -58.41125 | 2026-06-23 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7b0c9f8d-e699-30f9-896a-aaba6160b1b3 | -12.65921 | -47.67756 | 2026-06-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db094c9d-c15e-3138-9ea3-21ccf4f1417f | -14.03484 | -43.87289 | 2026-06-23 04:53:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5952debf-1737-32e3-9fa5-4dd6c20e27c8 | -11.6647 | -56.76234 | 2026-06-23 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b73b8a1e-4669-312c-84b4-c1d2d8e83d83 | -14.55103 | -49.11353 | 2026-06-23 04:53:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eaf95bfc-09fc-3e90-8917-52a9a39de706 | -12.87106 | -44.35706 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 413878d2-dc07-388e-a49d-aaf11785c3c0 | -12.8748 | -44.37196 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d280d5e3-b3be-3925-bcab-73bb1de56deb | -12.42412 | -58.42053 | 2026-06-23 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 127f22d4-12e2-3b77-bf25-23550d387864 | -11.87585 | -57.83065 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5de6db7-6eee-3021-b175-dd2aff18673e | -10.9329 | -56.85239 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68576630-ea0e-32b8-9df4-a3c90311d1f6 | -12.29274 | -57.57219 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 434af791-dabc-39b2-944e-46547e6685c9 | -12.42498 | -58.41555 | 2026-06-23 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31fe8699-b3d7-3476-a973-2f3d15c2d7ac | -12.91265 | -49.47921 | 2026-06-23 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9530f707-3af3-3064-8eba-bed1542e4ab5 | -12.07888 | -54.60176 | 2026-06-23 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04ee7b70-b33a-3a31-a511-1d27da228ec5 | -10.27272 | -60.54458 | 2026-06-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cff91366-9d1c-3725-8945-4d101daab57c | -12.85346 | -44.36566 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 79bae407-c3b4-3bdc-b4a2-ba2eb76ba5d6 | -11.2822 | -55.79178 | 2026-06-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 764cf290-ca1a-395f-94c9-237afda93e86 | -12.03076 | -47.8019 | 2026-06-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecf5104f-88fa-32cd-8595-c6c9388ed813 | -12.65866 | -47.68176 | 2026-06-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ac35beb-d63a-3e84-88fc-0192681daa61 | -18.50013 | -51.59248 | 2026-06-23 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02c1f97a-95fa-3774-82f3-8aadc363ca00 | -20.35366 | -46.61571 | 2026-06-23 04:55:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 067c5034-9b25-389a-bb86-73a975d4a867 | -21.0377 | -46.78709 | 2026-06-23 04:55:00 | NOAA-21 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ba7a0e8-d10e-3cf8-87ef-966fe59d7e26 | -18.49645 | -51.59194 | 2026-06-23 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f7d1005-5440-3cf9-a86f-8e9857a2583c | -18.49277 | -51.5914 | 2026-06-23 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffe23b42-c7a6-3812-9b13-d159860bd364 | -18.50075 | -51.58791 | 2026-06-23 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51770b54-1711-350d-851b-c26a42e43ff5 | -12.8746 | -44.3357 | 2026-06-23 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 6ead3f60-da3c-33db-95c9-18887819d067 | -12.8552 | -44.3389 | 2026-06-23 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b5cc44f0-4df6-300d-962e-37bec9ce5b12 | -12.8741 | -44.3593 | 2026-06-23 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3e28dde0-2f18-320c-b214-cf9fa3070cb1 | -12.8548 | -44.3625 | 2026-06-23 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| d0605dfa-fe63-3fb2-bfdb-d277f4bb0b70 | -12.8741 | -44.3593 | 2026-06-23 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 972edf73-9edf-3a56-a73e-d5bbe10094c3 | -12.8746 | -44.3357 | 2026-06-23 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 4df5cc67-2911-31f0-b79d-051a545fc9fb | -12.8548 | -44.3625 | 2026-06-23 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 1bd16b1e-1e3f-3f5b-8194-e54b026faf31 | -12.8552 | -44.3389 | 2026-06-23 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 99ccbb9f-6377-3a0c-aec8-21d1d2a45b16 | -12.8552 | -44.3389 | 2026-06-23 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8f2907f4-23a5-3f10-b2f9-04877143f951 | -12.8741 | -44.3593 | 2026-06-23 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 362a05c7-4026-3c12-a71e-456968294869 | -12.8746 | -44.3357 | 2026-06-23 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| acb3c906-4ec3-3f85-ad63-64ff4bf543c9 | -12.8548 | -44.3625 | 2026-06-23 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 38102ff6-cab3-33f3-b2d6-a35d0bab7bc0 | 2.58996 | -60.69891 | 2026-06-23 05:23:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed793e9c-3e33-3c58-84e0-1ca5c5c1339b | 2.58928 | -60.69458 | 2026-06-23 05:23:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78bf5a33-a012-35a2-bfcc-a94aca7fb5a5 | -2.7376 | -58.18865 | 2026-06-23 05:25:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00a593ec-4986-38d6-950f-3a92c2f789bc | -5.83025 | -45.06355 | 2026-06-23 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b7ae4ae-84aa-38c8-9d8d-c0ef8b8ba329 | -3.69798 | -53.75587 | 2026-06-23 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README15.md)
