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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a667f2f1-4c2f-3a3d-8572-b6de2642e25c | -17.56798 | -57.5213 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c8be9bfa-1dac-35e9-8330-1184ef69e86f | -17.58959 | -57.56221 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ba0ec48b-5e50-382e-83f5-d9b6d1b2db07 | -17.24787 | -57.46059 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6f2d6933-e79b-3706-97d0-27d44a2a9aa1 | -15.95481 | -57.27347 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 027430f5-2a16-3547-925b-d757061727b6 | -17.24719 | -57.46457 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 92298fb3-d9cd-386b-af61-582e4344d94e | -17.56257 | -57.5531 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2a54199c-7e75-3b29-bcd9-b5471e50c5ed | -17.58719 | -57.49213 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 450b781a-561b-378c-bc9e-5623fead5a47 | -17.81785 | -57.37413 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9d8bdc3b-e6a0-33da-83f5-15c7b5070dc9 | -17.66829 | -57.55046 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| b7f6cfb2-e719-33dc-bb45-588a50d81484 | -17.23132 | -57.18714 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 02949f6e-6470-3aa1-847d-8bc06ff011d9 | -17.59811 | -57.46967 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1fde7c87-aea4-3158-bc49-a54d8e6af8fe | -16.94738 | -57.62379 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a13b357a-175b-3b4d-9a97-7e6ccfe539f1 | -17.54933 | -57.52605 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 07e3abe0-21a4-321f-934c-f79fcc985fac | -17.64476 | -57.54201 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e548cc5a-874f-3713-8ce8-394263b75ad2 | -16.1615 | -58.35662 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f4b614bb-3a2e-3f2c-825a-5bbcee2630fa | -17.564 | -57.56569 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 539e570c-5147-3bd2-8a80-1c77d21e567a | -17.56763 | -57.43962 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 24df6925-c743-3021-bf9f-7f284aa42a1f | -16.94389 | -57.62314 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bdc3e085-f549-3914-a4c3-569cbfb879be | -17.58162 | -57.48294 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b2284203-0c5f-3e0b-b694-b2f55c222a2b | -17.6442 | -57.5559 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| f41a4941-0802-365e-8c48-cb778ecbede5 | -17.56806 | -57.5418 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bbd32b37-df51-3685-9ba4-88270d1c86d2 | -16.03892 | -60.11639 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 444fa622-a601-3afb-a6eb-52544883df27 | -17.57084 | -57.54643 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 00679994-7fa2-3402-a685-4f28268e310b | -17.58498 | -57.46315 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8ea850aa-25d7-33d3-947c-48196c64429e | -17.57395 | -57.4652 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| af425b92-a2c4-3fd2-8379-61b807d20d6b | -17.71259 | -57.56275 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7f3edd78-01c7-351e-82db-42dfe2fd104b | -16.00706 | -59.375 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ca4439f-f05d-39fd-8a50-74bf5015abe5 | -16.04227 | -60.12089 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 30dac467-1966-308a-84af-6a850a7b702b | -17.57041 | -57.44419 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9fae18e5-34cc-32b2-bcdd-f11491fc84a0 | -15.95386 | -56.37779 | 2024-11-16 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e1a9fe8d-db98-3d97-aa6c-8fa960a2c934 | -17.58239 | -57.49942 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| dd96ac3a-e134-39f3-9fd1-6a65395d56d6 | -17.23192 | -57.44949 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2dc78738-147a-32bc-b3c7-f658e0652187 | -17.57017 | -57.5504 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8f7e0458-ce60-3d82-9672-4e3fb4a71432 | -17.57865 | -57.43757 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 00ec2458-a109-3bee-8a12-0c496cf81c5b | -15.91596 | -59.27352 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6944ff5a-52b9-3543-8f8b-6ade93836c46 | -17.59878 | -57.46571 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b06fabd3-c2d3-3c1d-8954-c5b48a610f10 | -17.55422 | -57.53925 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 18423426-7125-3e52-a93d-1806e705dce1 | -17.62343 | -57.55205 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ddb9dbee-bda4-31fa-a90b-61ef3cf2144b | -17.61238 | -57.5541 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 30d11785-12dc-3f6c-9b50-e8eb8333b26c | -17.04875 | -57.43462 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 116a7644-2efb-3798-aa31-b4ca107b82f2 | -17.69356 | -57.48563 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bb40c3fd-f36c-3cd2-9209-0b81f1685a2c | -17.63315 | -57.55795 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 9bfb3b1f-1556-33bf-b7fa-d20cb1c4e88b | -17.56114 | -57.54053 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cd12ea28-d0f1-36c2-93ce-06e82763c72c | -17.55985 | -57.56904 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2febb46f-9efe-37c4-be62-c119698f910d | -17.57108 | -57.44025 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b7690303-1ba2-32bb-974a-6d2fed1f2ebe | -17.24298 | -57.44742 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| eab7008c-083b-32b4-bafb-b7ee288c4368 | -17.06596 | -57.41731 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 618b5e58-b7cc-3698-9092-ccbd2d848e73 | -17.66415 | -57.55379 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 17594e58-a297-38e2-914e-6cb34f850096 | -17.23199 | -57.46996 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8342a8a6-a57f-3c1b-9872-b597ee09cd07 | -16.9248 | -57.54481 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c2aaad9a-e9ce-3258-97ae-7cec1e7a4c73 | -17.59131 | -57.48881 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1f43cab8-4a7c-3639-9fe5-c0bc6005c9c0 | -17.58786 | -57.48817 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fc7866be-ed19-3328-ba1d-3fe43b178d00 | -17.61517 | -57.55873 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b3fd7766-a30d-3921-8753-ee628e2caa8b | -17.57144 | -57.52194 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0e6c9a73-264f-35cc-a001-dfd7f0987ee1 | -16.93902 | -57.63059 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ea39101f-297f-381b-8aca-cc8e167823d8 | -16.92132 | -57.54416 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f1814b1f-1c50-340d-9f04-1b14a6ac825c | -15.15866 | -59.72469 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 092e174b-01d8-37bf-8efe-ebdbd8bff49b | -15.9168 | -59.26871 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 88e7dcf2-524e-37d7-b9e5-f6f661c9720c | -17.29463 | -57.31052 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2dd7f4c3-35a6-3730-898f-38e2c18c8a4d | -17.65581 | -57.53996 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| cd17ef92-7f4c-3dac-964e-b1e7516cdc8d | -17.6414 | -57.55128 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| c9dad949-e701-3670-a695-010bdfe1aaeb | -17.2347 | -57.45409 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| a7c6ace4-5098-3bcf-aeba-0be1630e57fc | -17.21908 | -57.19695 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 514d1797-0e04-3322-8404-14945f6d03b4 | -17.58266 | -57.41394 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b1122faa-e936-368b-bf91-289e1dcd9cf6 | -17.56949 | -57.55438 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b3eb1645-d1ad-3d2c-a3ce-dde7375ad953 | -17.23749 | -57.45869 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7f97e9f6-9035-3fcc-aa73-26d8060c7bb2 | -17.59036 | -57.57879 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 2d14aa9a-71f6-3d1d-b07c-1fcf4a9387ca | -17.5716 | -57.56298 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ec984845-13f5-3680-a30c-a9960dbd4806 | -16.04294 | -60.11721 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 78018be5-205e-3142-b80c-850d10aa191e | -16.93553 | -57.62994 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 75ad3b71-f214-33d4-8a71-78fe34e33104 | -17.5821 | -57.4382 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 22322662-bb78-355c-bd23-58301fa259fe | -17.22872 | -57.20271 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| aa373706-b9c9-31e0-8e67-c06f23e2aa60 | -9.70418 | -64.19888 | 2024-11-16 04:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61b95c29-6630-360f-9b11-428f522f420a | -17.23056 | -57.45742 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c77e4f0f-7ad4-384f-9ea3-c1a6f8a83145 | -16.01644 | -59.37359 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 726ab064-0896-3cf5-8ed2-36f1ab919b04 | -15.89378 | -59.26423 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 760c3680-498a-307c-822e-3a6ba38a8da8 | -17.62277 | -57.55603 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7994f647-21f9-3f40-aeae-83bda0933e80 | -17.56889 | -57.57893 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1581f0bf-c09a-3aa8-937d-870a45aba51c | -17.69011 | -57.485 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6a29b6dc-ec75-3cf9-b7b4-26c124fad991 | -17.23335 | -57.46202 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| f600c09b-b210-3132-b27d-951eddc08d59 | -17.23538 | -57.45012 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 00fc41b6-c073-3055-a0a7-98f849a40f92 | -17.62064 | -57.54743 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 29ecdc65-d950-3586-b34b-731559bc59d8 | -17.65105 | -57.45092 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 970ee55b-0714-3750-975f-97c88ee45b07 | -17.58086 | -57.46648 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 301b3cd5-b69b-3b3d-b7cc-de1042536f3a | -23.95187 | -54.086 | 2024-11-16 04:53:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 605e9415-a80f-38e9-aff7-37131720ccf2 | -17.57731 | -57.44546 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1465a184-992f-36eb-810a-d86e7d370afa | -17.6455 | -57.55854 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.1 |
| 88c2b342-9d12-3335-8234-3971e2e4138c | -17.58843 | -57.46379 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 022ee9c5-fa92-386f-afed-bc58fc6295b7 | -17.57861 | -57.58484 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| d1e6a751-0254-3081-a9a9-cb60f8fcb768 | -17.23681 | -57.46265 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 70300841-7a97-34fd-947d-ef6487694759 | -15.95546 | -57.26962 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3cf1dd5e-f83c-3431-ab16-7585f1f68a1f | -17.62422 | -57.56863 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 9f783a1d-d8b9-30d7-9468-9d9ce78ba9b3 | -17.70019 | -57.57276 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 48e7058a-914b-3503-8a6a-fcd69a75503c | -14.53838 | -59.96096 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6743fbdf-9978-36c1-bbcc-69260367da03 | -17.57363 | -57.55104 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 00b10996-f471-3667-b737-e7038b75f30f | -15.95724 | -56.37838 | 2024-11-16 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0c79ad42-df0e-3640-8f85-8fa80768999a | -17.58199 | -57.5649 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d20a7544-0b29-3793-a9ed-67e43e141bc9 | -10.11925 | -65.02779 | 2024-11-16 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5908e680-a8ca-3139-a319-1d52a6273661 | -23.21195 | -55.22705 | 2024-11-16 04:53:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0e552c87-2401-376a-a292-4203d9668148 | -17.56553 | -57.4311 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |


[Clique aqui para ver as próximas entradas](README55.md)
