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
| 3f7c5eeb-1946-34d0-837b-2b3324707346 | -16.74615 | -56.7156 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7f4a4a60-04e7-3247-8184-0fb3dd042eef | -16.74293 | -56.7066 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dffc5b03-e337-3864-8cec-7d8e7c66caf5 | -16.74239 | -56.71081 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 04aafba1-26cb-32f3-b320-a9f66acc134d | -17.15885 | -57.41777 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2b216e07-6516-3e4c-ab5f-b6a5b07cf198 | -17.14037 | -57.43088 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 58ba2dd5-233f-3998-80a8-f4282a7a49cd | -17.13419 | -57.34729 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ea2d3662-02f0-3e1e-a024-64cd95c88197 | -17.11563 | -57.42741 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 63c29237-2f7d-3a11-8e63-6d4f92827150 | -17.11514 | -57.43125 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| e1f0f6dd-3ab2-330b-9b03-41487c6d0f13 | -17.11053 | -57.43451 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5ad979fd-5ef0-3230-b32c-2919001970e0 | -17.10738 | -57.42625 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6076aacb-a47f-30af-a066-182c86d4e54e | -17.1069 | -57.4301 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f44397b9-9af2-3de9-9682-3f04086c79bc | -17.10039 | -57.36282 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d3c69468-6c0e-31d6-85ac-5de4652cda14 | -17.09886 | -57.37441 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ee021cd6-6cf6-3e2e-8e6a-31f540d33cee | -17.09865 | -57.42895 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ea7b907a-5775-39af-80a9-f97cfd09b0b4 | -17.09575 | -57.3661 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1e1ff7c8-1803-3213-b8ea-3ffe5ae70360 | -16.80681 | -57.41671 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8dfa7d30-bf8a-3db8-ae6f-7424b2872d25 | -16.80632 | -57.42052 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ff125305-ade8-3900-bab1-54fd7ab5d2f3 | -16.80486 | -57.43194 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ae9b7fcf-eae6-37c9-889d-5e679d7a9f42 | -16.80367 | -57.40851 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d5cb4b88-ff6e-3a09-ae50-1c6505539896 | -16.80221 | -57.41994 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d8a6ccf2-8c3c-3f51-b3bd-613f7c505aa2 | -16.80124 | -57.42756 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7f3b4392-0dd5-3a16-b33f-bcc5c5d937d1 | -16.80005 | -57.40412 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 38281f12-1d88-3d4b-aca1-5cb81e9ff422 | -16.7981 | -57.41936 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d5690d2f-4a5f-3d19-a19c-5985cafcfcb7 | -16.79713 | -57.42698 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3b2d7051-5cff-3a03-8b64-78962c9aea0e | -16.79616 | -57.43459 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c847ee1c-82ca-31c9-971a-7ece893444c2 | -16.79351 | -57.4226 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| db803351-43de-3494-8680-ba66aadc8dd4 | -16.79303 | -57.4264 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2527c616-849c-3450-8dc0-3c6717428018 | -16.68574 | -57.11381 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2b923215-9671-3c8e-9045-c84b2114e1fb | -16.68259 | -57.10532 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d421181c-0bde-37c0-97aa-61930bdbd99d | -16.68207 | -57.10928 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 256d5428-cfd9-36ba-a6e8-60eec50c3de6 | -16.68104 | -57.11719 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c77c4c89-7123-3b87-b903-f8dbabb49c07 | -16.67892 | -57.10077 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2fd718c4-6681-383f-904a-c188a2775ea0 | -16.67789 | -57.10869 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5da190f6-3646-3cb5-8ab1-ef8fe4e61cfb | -16.67532 | -57.12846 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8cdfcd84-0530-3be7-a40b-e7f8177fdfa9 | -16.67429 | -57.13636 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| fcfbee51-bca2-3e07-a5b2-5babed9dd55c | -16.67422 | -57.10415 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 201f41d8-8298-3093-86d3-36d294ae2ca9 | -16.67319 | -57.11206 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 3a31fd9e-2eea-3d37-af81-168f1e5257e8 | -16.67268 | -57.11602 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 36688648-5676-3055-ab80-c965817687c4 | -16.67216 | -57.11998 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1a4615ba-f2cd-3178-8103-d2cfa659d869 | -16.67165 | -57.12393 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b5d8bb1b-11f9-3558-af99-674e118cc03f | -16.67114 | -57.12788 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a60869bd-a2f9-36e1-932f-c27b21e9ec4f | -16.67063 | -57.13182 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 29089358-2022-3b81-bd7b-3516c131053f | -16.67055 | -57.09961 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 45cc5989-0288-366f-83c4-4bddefe81cf1 | -16.67004 | -57.10358 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4c166eeb-30a6-3ea3-8c4b-5a6984b0ba64 | -16.66901 | -57.11149 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 41039277-0403-3f21-a457-839b713534f3 | -16.66799 | -57.11939 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1f9421e9-d5b0-3014-83f2-74f3e41fbb40 | -16.66747 | -57.12334 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 419fdd7b-367e-30c6-bd2d-74279b2d8f6d | -16.66739 | -57.09109 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 01ebb666-760f-32ec-82bb-2c121527fc98 | -16.66688 | -57.09506 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ad65191a-e4ba-3c46-964b-c2d735f06162 | -16.66636 | -57.09902 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 5e811052-94db-3a73-b8a2-1e24c49ea771 | -16.66483 | -57.1109 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e29572ea-52de-31e3-a701-7f7e95bd9440 | -16.66432 | -57.11485 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 28460d08-069f-3f9a-99b6-1645ae1ef97d | -16.66279 | -57.12671 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 6dc14c13-0b89-3012-a38f-f61bfbe27bf2 | -16.66269 | -57.09448 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 4d54f9cd-ca3f-39bc-9e81-0fc1b3b833d4 | -16.66227 | -57.13066 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 3fd6dcca-e046-3ea0-a518-7bf34fd734e9 | -16.66218 | -57.09844 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 15b65f59-8217-30fc-b6b1-433c95f2c4ae | -16.66167 | -57.1024 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 9abd0925-be22-30c8-900f-17f97a092377 | -16.66014 | -57.11427 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 92ffae47-b49a-340d-a77c-2e0bcb8d7558 | -16.65912 | -57.12218 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| db2edd06-e020-317a-bd0a-05ded17d2ee5 | -16.65861 | -57.12613 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 1f16430e-e955-3c47-a612-eff9e79468b7 | -16.65392 | -57.1295 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 139685a8-a226-378c-9a65-33ca135c6451 | -16.65341 | -57.13345 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a9e41b72-9f7e-351c-9762-2adad1049043 | -17.0395 | -56.8405 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4cd8be84-0219-36c9-99e7-f99f9122bcce | -17.02613 | -56.84291 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| daa290b3-88cd-37ff-bc89-f5db708c27cd | -17.02185 | -56.84234 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ad973c84-f832-3b98-bcd7-6ad282a854ab | -17.00527 | -56.83578 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0030afa9-852b-3236-bd84-24ea441c418b | -16.99366 | -56.71875 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 53372e90-7dfa-39ac-abd4-ae6c859f7165 | -16.98778 | -56.73086 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 97ba4052-9e5a-33ae-bd55-1b3fe502d8ed | -16.98712 | -56.70056 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 466e1cad-abf5-36d7-a69e-ff0a90eae7fe | -16.98485 | -56.7013 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4f491e80-01e5-39f5-b3b3-49b98cdc1fdc | -16.98375 | -56.70979 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 15ad3442-ad89-39c3-b02d-31f4130bb478 | -16.98347 | -56.73026 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9107ba7c-3998-30ee-a573-a2c459bab01b | -16.98177 | -56.70847 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 36b3850a-4439-3860-9236-7314f7106051 | -16.98154 | -56.72672 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| a3932490-da91-3982-8ecc-47a3d546193f | -16.98099 | -56.73094 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 44b4d5c2-1080-3c21-ba34-022799a17885 | -16.97004 | -56.81493 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1f96eab2-90ef-3a50-9967-7dd61d47263e | -16.96882 | -56.81385 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| aeb1c81a-f366-305b-926d-0c844115b122 | -16.96745 | -56.75385 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 961e579c-8690-38d1-b40a-b7cad856121b | -16.96739 | -56.8018 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 42c865ac-db59-34c3-8d73-79cc34fdb792 | -16.96685 | -56.80598 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 66cc1847-20fc-377a-a606-50c0004b7866 | -16.96557 | -56.80487 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 860c48f9-7fb6-3d6d-ad24-9eb8742ab2ae | -16.9631 | -56.80121 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 120303b7-a802-34b1-a5ef-a02a7fda420e | -16.95941 | -56.76233 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2c538b8c-8767-3e21-922c-8e7dfe304aa3 | -16.9567 | -56.78332 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fc49ad5c-dac1-3fcb-a7b3-5e2bdb1ea175 | -16.95295 | -56.77855 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ec57b7e1-e238-301c-aacc-b35bf5377183 | -16.83621 | -57.44793 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 397f057e-1a79-37be-bcf9-fbcbbd5f1655 | -16.83571 | -57.45172 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 435d4d6c-6153-3bab-8ae2-4db197a071bd | -16.83309 | -57.43977 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2dac8465-7152-307a-a544-254748972a4a | -16.8326 | -57.44357 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 335c3565-f44d-3373-a2cd-6776775d9efb | -16.83211 | -57.44736 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 881f9f33-3326-3bed-b8d4-5706b3252844 | -16.82948 | -57.43539 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 2c80a6f1-fd90-3d75-9067-f4e97761474f | -16.8285 | -57.443 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 68f921c1-f3d3-3d3c-8c34-db0433ee2409 | -16.82127 | -57.43425 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ac0cd855-7750-3177-a9cc-eba080c9b62f | -16.82078 | -57.43805 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| aa2ed0bf-5aa8-3a3c-a73c-7f46be1934ac | -16.81091 | -57.41729 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4c87a712-cd29-3c4e-8251-9a61eb67e7a4 | -16.80583 | -57.42433 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c1c0acda-1291-3d76-90b7-85bc9683098d | -16.80534 | -57.42813 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dfd72e6a-8197-33e7-a3eb-9be6410f435a | -16.80437 | -57.43575 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| db614020-9fb4-38be-9c8b-51c1b90d40ab | -16.8027 | -57.41613 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f3481ffb-93b1-36d2-b51b-c2004c7fc6f0 | -16.80172 | -57.42375 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |


[Clique aqui para ver as próximas entradas](README119.md)
