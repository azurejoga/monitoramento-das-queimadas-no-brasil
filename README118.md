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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 524869bb-ab06-342c-95bb-ed9d9459cbfe | -17.01184 | -57.42246 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6c4e3a43-205a-31df-acc6-11c96a622775 | -17.01127 | -57.42644 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d75aba89-29b0-39e1-8d18-80a7c9ffda62 | -17.00929 | -57.42753 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e77a9da3-0e40-3ec8-ac32-2a5647502d1e | -17.00816 | -57.41107 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c33c8b4d-841b-33fc-8419-c6f99b3c0a5b | -17.00698 | -57.41904 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9adfdf56-5e4a-36f8-bd3f-35e0b4f3893a | -17.00523 | -57.43097 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 94298ac2-6907-3017-9989-87d8d06797cb | -17.00234 | -57.42645 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 92c1ecaa-7180-3859-9234-ecdc276ceb29 | -17.00176 | -57.43042 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 22bea8d0-688a-3c41-9bd5-6ca3e6b561a9 | -17.00004 | -57.41795 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1b08d76e-e073-370c-9c31-9968237806ee | -16.99829 | -57.42988 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| eff36efa-9f3f-329a-8a77-4110f1fb147b | -16.99773 | -57.40944 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1c0ea2a2-256a-3ac7-b7f8-b3a88c0957f5 | -16.99656 | -57.4174 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c96b7ebf-ad7d-379e-a1af-c2be195204a4 | -16.99481 | -57.42933 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4b6ab7d9-7823-3114-adae-5ad116fdee99 | -16.9902 | -57.41234 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d4e60620-dd32-3bda-a26d-9479972de4b3 | -17.20117 | -57.45107 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c1a6a3a7-6adf-390d-b353-38363bd66f66 | -17.19886 | -57.44254 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c04632a8-a42c-39fa-8011-77a5e575ddf4 | -17.1977 | -57.45052 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 071f99ea-5477-3d4b-aa28-1000f08953d7 | -17.19711 | -57.45451 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2b71498b-530f-3401-bfa2-5e4dd6d6963c | -17.19597 | -57.438 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 00327642-fddb-3d1e-a7df-2c86d30de27f | -17.19538 | -57.44199 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9664c2c9-1c81-3e65-af3e-d824c767e40d | -17.19249 | -57.43746 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 11094bc6-bdb6-3faa-acdd-35134a6d4683 | -17.19074 | -57.44943 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e1af2823-7e6e-3ad1-8a18-e5609cd1e128 | -17.18958 | -57.45741 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 75997ce8-547c-3106-ba38-ccbb63b14c80 | -17.18901 | -57.43692 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c5fc75c0-cca7-3108-8019-2861684682d1 | -17.189 | -57.4614 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fed5d83f-3f6b-3515-8e86-82e5dae80423 | -17.18727 | -57.44889 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0c03dcab-20a8-335d-a891-eac11be84cf3 | -18.01624 | -57.3586 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 2fc25b01-1ee9-3d9b-9b95-dac415ecc5c2 | -17.18726 | -57.47334 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| fd379b71-60a2-37e1-8bde-ff24572174e7 | -17.18554 | -57.43637 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 31dda3c6-9cac-36a8-9967-99b3d4f34f18 | -17.18495 | -57.44036 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 527165aa-a90d-3ca3-bc4a-a2c11119cc2e | -17.18321 | -57.45234 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d309b309-7bad-37de-9d6d-87df780e37cc | -17.1832 | -57.47678 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 32afadf0-eaf5-3937-a939-1d66bd34b56f | -17.18262 | -57.48075 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 600fc31b-b8cc-3dbe-be37-e114160ae746 | -17.17973 | -57.47624 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 33b3008b-bce5-3fc9-8295-a38c45eda404 | -17.17221 | -57.47913 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 83c1cbd5-60bb-32c1-980b-f485f8f05aae | -17.16932 | -57.4746 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c2ef88c6-1cb3-33e1-806b-5187bf522841 | -17.06859 | -57.44764 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e85c2d8a-44e7-336b-8871-f44e6bdd0daa | -17.02402 | -57.43658 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8ae734ab-0100-3970-b202-c9b5b68cd556 | -17.02055 | -57.43604 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c9fc1849-27ad-330b-8bb4-01ca5b5af8fa | -17.0165 | -57.43947 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0a10bb8a-7500-37c9-9be3-710e98cebb44 | -17.01593 | -57.44345 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a69a5574-3348-3fc3-a514-4ae8b999a59b | -17.0136 | -57.43494 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 452ee2fc-a5d3-3c85-8513-6ba20b49d660 | -17.00519 | -57.45535 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a59440c8-5da6-3d32-ba5b-28d428240b09 | -17.00285 | -57.47121 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 61db7de3-c823-3011-b280-a3b2e7b1d812 | -17.00231 | -57.45083 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 48c07738-19ad-34bb-a78d-9f56ab385856 | -17.0 | -57.44236 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8f6208a7-786a-3c22-8008-75f53b7797c8 | -16.99997 | -57.4667 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 477de8a4-9584-3802-ad8e-8f35fd1f2095 | -16.9988 | -57.47463 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 65d20943-bdbb-3c3c-b8e1-f743adb83788 | -16.99822 | -57.47858 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2a6c819d-5cc9-3ef4-827b-246021ae90ca | -16.99653 | -57.44181 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ace06251-929e-3cbe-88ba-928c524fbb99 | -16.9965 | -57.46616 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4f7a6393-9588-3818-90fd-b572103b973f | -16.9907 | -57.48146 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 08bc91bc-122e-3416-93ec-831dc4935973 | -16.99012 | -57.48542 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| efb13a1b-71d3-34a0-908c-c923fdf522c2 | -16.98782 | -57.47696 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 714a3660-3d93-37bc-9187-7633c4b6e72d | -18.01566 | -57.3627 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.3 |
| dc0aab69-9e7f-334d-9639-df5bcfa6d96d | -16.98665 | -57.48488 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 99b0727e-9511-378f-a28e-a7fd55e821bd | -16.98319 | -57.48433 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 80cd5755-b0ea-3f5f-a4a4-4acf68574c24 | -16.95144 | -57.50765 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 875e58f8-53ed-3425-9779-48f47e69db00 | -16.94855 | -57.50317 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 80affbf8-6b93-3416-a0e3-7bf4be0c3b03 | -16.93707 | -57.7018 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 38ee7811-651b-356c-9fe0-0eb37c7febe0 | -17.22107 | -57.31466 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2178f622-7830-39db-8160-70bfe9448fe7 | -17.21758 | -57.31411 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e076e18e-dc16-31ff-8830-b0112ec59c0a | -17.21699 | -57.31815 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 796c915f-f2cc-3fd8-99ad-c22adbcb48a1 | -17.15146 | -56.84626 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 0b478b84-1319-323d-951e-763e19fd0c16 | -17.14491 | -56.86674 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d505a394-24a7-3cd7-9943-418e5edc57e1 | -17.14371 | -56.87513 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 873bb644-b588-3016-9145-ce2d44f1180d | -17.14194 | -56.862 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4d07fa8d-e242-3b15-a77d-341a0f5fa4e9 | -17.14134 | -56.86619 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 02f1209e-a7a4-3227-8f7d-582d616b7935 | -17.13422 | -56.86509 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 30cbcf10-64a0-3cd4-83e2-6a6bf85155d6 | -17.13125 | -56.86034 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7b5a2067-cfc7-3e14-b04e-2712b5064e21 | -17.13007 | -56.86874 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 3b1638af-b423-36ca-80dc-09f53135c0ef | -17.1271 | -56.864 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 3ab52712-cd17-398f-81a8-9f6cef9c7d0a | -17.12413 | -56.85925 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c0493bd6-a186-3e96-acb8-56ce69cd25b2 | -17.12235 | -56.87185 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9c814dd0-7577-3842-9166-fca7f2c842c8 | -17.11938 | -56.8671 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c92ea0de-9fb1-3d34-a546-d3a877210c5b | -17.1188 | -56.8713 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 08ae42bd-940b-33e4-a9cc-30554bbbafdc | -16.86686 | -57.29613 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b0795ae8-a111-36a1-9f6b-2a58e2391e1d | -18.02678 | -57.36024 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 891c19e5-8eb8-3fda-865e-630357312172 | -18.02327 | -57.3597 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c43282fe-9f4b-3421-ba2b-dfef66370e08 | -18.02269 | -57.3638 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2f024334-a865-340c-b59e-d38aa91ab9a6 | -18.0221 | -57.3679 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6a6d1ba5-2d08-380b-b812-24654186010e | -18.01975 | -57.35915 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 6f815b8c-79d0-3baa-ad70-2c659685fef9 | -18.01917 | -57.36325 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.3 |
| a9367ddf-e511-335c-840e-84dd40deec79 | -18.01859 | -57.36736 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.3 |
| 0dc2018a-db65-36b9-922e-c9c675214f29 | -18.01507 | -57.36681 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.3 |
| c1a6f590-11cf-336f-9643-016d7e48dda8 | -18.01449 | -57.37091 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.6 |
| 7aeefc4c-8303-3da3-bf7c-06f16649ad57 | -18.01272 | -57.35805 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 4dba8981-dc8a-3fc5-9c15-d31c0e130899 | -18.01214 | -57.36216 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aba6eba2-c702-3992-8382-d7839c728eef | -18.01156 | -57.36626 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 41006fa2-aeb9-320e-bbe7-82952b6316f0 | -18.01098 | -57.37037 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c50a6f01-e8ef-3a39-9d3c-00b8aaf5b6fb | -18.0092 | -57.3575 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 6dbeb566-a89d-3bf2-851f-b72e3bb6e3bf | -18.00862 | -57.36161 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 66ed4288-5281-3dbb-b750-6169da1777b8 | -18.00805 | -57.36572 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a0f2514c-56b2-3f87-a635-66ff78742583 | -18.00453 | -57.36516 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2566b19b-c9b8-36ca-8c6e-ba3461046bdc | -18.00395 | -57.36927 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f990f085-ab7a-32fc-a3f8-614e7602323a | -18.00159 | -57.36051 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d6e35e41-a521-3333-887e-dcb4167d25c2 | -18.00044 | -57.36872 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f2129484-76b7-3807-aac6-a2d97e38af2f | -17.99808 | -57.35995 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 161c2dbc-fee1-3ec5-a112-3f416cd5bb40 | -17.99757 | -57.36123 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d3d709d8-84cf-331b-bb59-07044a3f9a51 | -17.9975 | -57.36407 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README119.md)
