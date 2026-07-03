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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 421016b8-3a54-3cd7-ab71-c2d37efe1b17 | -11.31357 | -54.46967 | 2026-07-03 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad2a80b5-02e7-331e-8c33-cac453b582ef | -11.85384 | -48.24597 | 2026-07-03 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a5cf386-197f-35c4-8035-adf048e5df9a | -11.44141 | -46.53331 | 2026-07-03 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2a28a9b1-d0a6-3e10-9462-aba2dd1e9a62 | -11.41631 | -56.06786 | 2026-07-03 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a614331-687b-309b-91b7-e4851627d7b3 | -12.50971 | -48.26097 | 2026-07-03 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 656c3123-0bfc-30fd-8853-d71b56cd6d5b | -12.75519 | -44.52277 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 029163e4-c35a-34ca-937c-902cfa75e870 | -9.20181 | -58.04712 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed2cb5ef-b2e3-323f-a394-8c0841b5ab62 | -12.78262 | -59.88246 | 2026-07-03 05:06:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8db38cdb-f1ce-3b3e-807d-e74eb6c499e6 | -11.32107 | -54.46685 | 2026-07-03 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3be5063a-7236-3bb6-bd02-548ccee18557 | -12.3757 | -54.45755 | 2026-07-03 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a17b366c-454a-3324-9d2d-9f1ab2b06c99 | -11.35137 | -55.41972 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cf0ddcd-7891-32ee-9e03-99a8b5e1644e | -9.07651 | -65.42039 | 2026-07-03 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f84b0ee-5f1c-3e2f-93e4-6d4eef7bb92e | -11.44188 | -46.52954 | 2026-07-03 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 065170b1-36e6-3747-8286-93609717c94c | -11.34801 | -55.41918 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a971a1cd-3887-3981-9fff-e5037c4a5422 | -12.49845 | -43.80743 | 2026-07-03 05:06:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c3d9e24-c9a3-30cf-bbcb-12f388578e1a | -11.41462 | -56.05674 | 2026-07-03 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95750efa-1aff-3b43-ab0e-470400731903 | -8.70015 | -54.57714 | 2026-07-03 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 9d177daf-6604-3733-a7d0-d91429e3546c | -12.08991 | -57.14312 | 2026-07-03 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 040e414d-fae2-37d8-a25a-8d7b430435cd | -10.12992 | -52.09748 | 2026-07-03 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad25d054-158b-323f-ab4b-fb2a245b7dd9 | -12.51211 | -48.28395 | 2026-07-03 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf27ddd3-275c-3796-afae-4905f282cd26 | -11.62949 | -50.36663 | 2026-07-03 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ad35c16-f574-3bed-955f-f2422f7ad546 | -11.5043 | -54.50471 | 2026-07-03 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e71f96e-eb93-3bc6-99ad-3a6a6bc0734c | -11.41848 | -56.05373 | 2026-07-03 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1727578f-f41a-343b-8a6a-59c703c93ea6 | -11.63842 | -59.01465 | 2026-07-03 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 641feb6a-44e2-365d-aebb-9795ddf9530f | -9.95442 | -49.28726 | 2026-07-03 05:06:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b875066-c774-36e8-8814-d49b900a94e2 | -13.98958 | -47.44641 | 2026-07-03 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f810256c-3cf9-3c3a-a547-d05d6014ddf4 | -9.1773 | -58.06222 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d33147d-9392-36a5-8369-a9bc9dde5358 | -11.34639 | -55.43005 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ebaf794-5f15-3dec-b679-652188708fac | -9.07592 | -65.42365 | 2026-07-03 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2218a290-79da-3a32-9b20-89d4b1a2a0cd | -12.74695 | -44.52616 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 80cadac4-9906-3cbc-9593-43c2df4a1274 | -11.64874 | -50.38882 | 2026-07-03 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45b3aeb2-d0c9-33a3-be8b-a5d705cf9f27 | -12.50735 | -48.28004 | 2026-07-03 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cf1ba0f-b573-3615-a288-c00e33f9fd42 | -10.94689 | -43.05373 | 2026-07-03 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 24011312-ee15-306d-9f0e-9bd645c49d3d | -12.75233 | -44.53856 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 20bd38bd-07a9-3f08-afea-1bab7e37face | -9.18689 | -58.06754 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe57e27e-04ea-311c-aeaf-5257f82ab9fd | -9.09095 | -59.40398 | 2026-07-03 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff4f12d0-0827-39e1-a2fa-b67e484e20b3 | -11.62949 | -50.36359 | 2026-07-03 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4648e439-f864-38bd-b390-9e6865cabb03 | -12.74861 | -44.52195 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| be1541d7-4311-3917-ad99-0ea8508bb8e1 | -10.94338 | -43.04044 | 2026-07-03 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 7d9cd88b-416f-31d2-a1ae-01eabed24e19 | -10.83971 | -49.38471 | 2026-07-03 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| accc4660-ed12-309d-85e7-c17a592f4792 | -9.26173 | -57.86925 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c974a4c-8eb4-3d4b-9f0b-93d5f97e90a2 | -9.19045 | -58.05282 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ababd78-947c-3d26-902d-5c76173fb174 | -12.79048 | -54.8825 | 2026-07-03 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf88604f-6e48-386b-891e-9776126a5e4e | -14.41345 | -44.59233 | 2026-07-03 05:06:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d1d7e409-47e4-39c9-ad9e-a070c146e28a | -11.79559 | -57.00187 | 2026-07-03 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e788fab-49dc-376d-a974-0a37b9c118e9 | -10.12288 | -52.0914 | 2026-07-03 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b1ac44b-dd10-39a0-9c72-264ae31608c2 | -11.34303 | -55.42952 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3a69d20-bd0e-3f3f-aa1e-2d048d5d8c0c | -9.17613 | -58.06958 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d292f340-356e-38bc-b205-01b5c2385700 | -12.50529 | -43.80839 | 2026-07-03 05:06:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61a7cf93-4bc3-3e84-855c-d2005f27cc6e | -11.53471 | -46.64261 | 2026-07-03 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1b55153-5771-3d46-97c5-e4513e47000d | -10.12605 | -52.09689 | 2026-07-03 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88327502-0813-3bdd-80cb-129cbf39fd24 | -14.41743 | -44.59107 | 2026-07-03 05:06:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e75bf24-5294-36fa-a113-66b646804b1c | -11.34693 | -55.42643 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0418338e-1df6-3685-9d27-b00bbaad1512 | -9.02739 | -59.53215 | 2026-07-03 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03319c6a-42a9-314f-a66e-1dd854f4b77e | -12.74732 | -44.5335 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 65f80916-2646-3f74-9acf-8fb912a8872f | -8.6996 | -54.58078 | 2026-07-03 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 397336cc-d9f4-3c16-a11a-de0c0fa01610 | -22.79459 | -49.34869 | 2026-07-03 05:08:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e4d41bc-34d7-3631-b99b-a8ed2b18408f | -19.50897 | -52.7344 | 2026-07-03 05:08:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f825ddeb-6d10-3820-9c87-134aa720bd7b | -17.71632 | -46.78638 | 2026-07-03 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 818cf19e-8725-3bb6-a84d-41d86430d004 | -21.10807 | -49.0024 | 2026-07-03 05:08:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 437b5dea-e298-333e-b650-3f2ddf698dc6 | -17.71782 | -46.78231 | 2026-07-03 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26d9e912-7f20-36f8-9c7e-1974ca6f12ef | -19.50848 | -52.73851 | 2026-07-03 05:08:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f1ed2b4-d0f3-3920-8b00-ef7c4455fca3 | -19.51271 | -52.73905 | 2026-07-03 05:08:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1bd08a4-5a50-3477-a6c8-b8f3a1774f98 | -18.63991 | -51.83218 | 2026-07-03 05:08:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c28b338c-656d-352b-bb90-96be799dfdc3 | -16.77046 | -48.52314 | 2026-07-03 05:08:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e53b389-52cc-34b5-af71-b5ee46ef89b1 | -18.41436 | -53.2905 | 2026-07-03 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5c9c12b-5bb0-3046-ae8a-fb5fcf134480 | -21.11393 | -48.99929 | 2026-07-03 05:08:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 08ce9e47-2cc2-3746-ba81-e97d6f265f5b | -18.48148 | -54.10391 | 2026-07-03 05:08:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0de440f-e226-3405-8fe8-fa4397115e9f | -16.77324 | -48.52563 | 2026-07-03 05:08:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 124ed3f7-4738-3b1b-8b0c-baa1265933c5 | -16.7736 | -48.52225 | 2026-07-03 05:08:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34096be0-d15c-3736-996c-f5658006dc29 | -14.41547 | -60.20398 | 2026-07-03 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30ba2f47-aa5d-3370-96e9-e9abd13c9052 | -16.77584 | -48.52382 | 2026-07-03 05:08:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abff725b-ca4b-32bf-b27d-31d4fb0438e1 | -19.51223 | -52.7431 | 2026-07-03 05:08:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2299f05-e8db-3ecd-a27d-f6e7864dd345 | -19.50851 | -52.73549 | 2026-07-03 05:08:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0766869a-1bd3-3f86-8f61-59cc4da9d79e | -17.71738 | -46.78697 | 2026-07-03 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b58c7c7-cc99-3baa-98ab-4d317544d3ce | -21.10843 | -48.99858 | 2026-07-03 05:08:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e023fba1-1c39-3c12-8490-e60063a1d09d | -12.7548 | -44.5428 | 2026-07-03 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| bfff5975-1a0c-355b-a929-ce53f373c667 | -10.9588 | -43.0565 | 2026-07-03 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e2032c14-f8b3-3ec3-a258-f36a6f6236b1 | -12.7553 | -44.5194 | 2026-07-03 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 228.7 |
| 803a3f22-eac6-3a7f-a557-3fd54f701d9e | -10.9593 | -43.0326 | 2026-07-03 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| eed9294d-7832-3425-8cb5-86055881d01e | -10.9401 | -43.0355 | 2026-07-03 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.8 |
| f9680620-692f-308b-8948-dd83f1c8d8fa | -10.9397 | -43.0593 | 2026-07-03 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 204.3 |
| 65337dee-c76b-3a41-bdfb-7046f1558b10 | -5.7945 | -45.0586 | 2026-07-03 05:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 1b3a837f-a8db-3911-a110-82ecd2dc47dc | -12.7557 | -44.4959 | 2026-07-03 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a4635858-5d75-3066-bc1b-20dc1b2cb799 | -12.7557 | -44.4959 | 2026-07-03 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 296dcc73-0d84-368d-8d30-dc3577a4b8ea | -10.9401 | -43.0355 | 2026-07-03 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 3d79b526-08a2-3098-93d1-2e549b7705af | -10.9397 | -43.0593 | 2026-07-03 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| ac9c7502-d9b4-343e-893d-a86f7471ab59 | -5.7945 | -45.0586 | 2026-07-03 05:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| edab23cd-eab1-3922-b728-2ab7bb7cd990 | -10.9593 | -43.0326 | 2026-07-03 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3b6cb929-8d8a-34d6-a44f-f5b2f05252c5 | -10.9588 | -43.0565 | 2026-07-03 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e76beb89-18c0-3e79-8842-6fb143bf9bb4 | -12.7553 | -44.5194 | 2026-07-03 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 959af86a-cac0-3027-849c-6d16eeff415d | -10.9593 | -43.0326 | 2026-07-03 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a7387b06-dd73-36d8-a110-751fd74ae80b | -10.9588 | -43.0565 | 2026-07-03 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 04d5c1d5-2d43-3853-80b2-98d0e753f10a | -10.9397 | -43.0593 | 2026-07-03 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| c75758b4-1a9d-3b0a-ac59-28a281b477b2 | -5.7945 | -45.0586 | 2026-07-03 05:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 97f82cfa-cdd4-358d-88e6-a6be58e36f10 | -12.7553 | -44.5194 | 2026-07-03 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 1ef5e331-eb44-373f-b2bf-e0160404af47 | -12.7548 | -44.5428 | 2026-07-03 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 8a20aa3c-5581-3aed-aa7c-8f35dedf97c5 | -10.9401 | -43.0355 | 2026-07-03 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| f97ba45b-8918-3690-b31c-3cf10837d25a | -12.7557 | -44.4959 | 2026-07-03 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 2fd94f7a-34b7-38d0-8146-825e5e4accfb | -3.50749 | -48.03837 | 2026-07-03 05:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README18.md)
