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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73bf5afd-3c84-3a29-b930-32836175035c | -17.62806 | -57.57209 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 263f1f74-f29e-3c58-8b31-b5b4b423e694 | -17.58767 | -57.49547 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 57b5d71c-44ba-3a60-b0e1-44ef62ed5de2 | -17.57583 | -57.43926 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 28ff32fa-7330-3473-8d75-f6a1c6834545 | -17.62273 | -57.56729 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 5c183c89-7c63-3746-ad51-c0feef9c3b46 | -17.23988 | -57.44761 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| ab29c244-92c1-3d7f-8f97-755ed787c797 | -17.58401 | -57.47401 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a4eea430-31e4-3f5e-8fff-168d2b056496 | -17.57367 | -57.51894 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f355e21d-073e-3fab-89c6-b57a42f72e9b | -17.62104 | -57.5663 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 5d13089e-ae95-3f36-9679-5fad7d3951b0 | -17.57825 | -57.47332 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 24c9694d-13d0-301a-9441-d937a8eca2cf | -17.58418 | -57.58676 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 5a81f302-b030-39ca-aa2b-83af251175e8 | -17.69103 | -57.57977 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 87703f4b-d4d3-3df6-b6e5-09f8d0d7b877 | -17.63459 | -57.5646 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 405389b7-ac82-39cb-82d8-869681f7baab | -16.94304 | -57.63159 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 953610c2-55fb-3582-8c94-a77d2b244ee0 | -17.63907 | -57.56015 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 0837779d-5d26-3fdb-9cb3-55e5bae64a1c | -17.29047 | -57.52035 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d2e46c36-aaed-34c1-a507-26652b96bbb7 | -17.56757 | -57.46364 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3bc3e8cb-8cfe-36d4-92df-f341b93154ba | -17.57909 | -57.46503 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e0437fc8-abb6-3865-ad39-eb62cdb5d4d2 | -17.59536 | -57.53408 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ee8ab860-b172-3e65-8b34-b08e2e30f47f | -16.9309 | -57.63816 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| eb87496c-f15c-3ab6-9c26-96c4a86c183f | -17.65913 | -57.55091 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 909fc6bf-8369-3877-8cae-a295123430b0 | -17.57333 | -57.46434 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a0b16ef3-06a8-3e48-8a3d-d789e7d51d7a | -17.29089 | -57.51626 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 540115ae-3e8a-3e0d-a72c-2ebf7123170c | -17.23946 | -57.45174 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 6b6df1e7-4830-36b0-88ab-ab3c7cbd025e | -17.23227 | -57.44996 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 2b878e0d-9e23-34cc-8c64-26d19a0a65c0 | -17.56389 | -57.44201 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 9c89609e-a39c-3bf3-bba7-2a3ce6d2ba42 | -17.09412 | -57.4797 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5c132b8f-ea92-3cac-a59c-ee76bfea5c43 | -15.90042 | -59.26476 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ea3953c7-6245-3ad4-b455-fd642d6465aa | -17.62061 | -57.57042 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 0e90b128-12cc-3e1d-8c36-168e24c9b6f8 | -17.23801 | -57.45064 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| b5847ef3-b3f5-31b6-aa01-87d77e8998f6 | -17.31639 | -57.50839 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f5dd6ab8-f0a2-3c6a-abed-e3a3c5918b70 | -17.62846 | -57.56799 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 425c5bca-58a1-3ff9-9f71-ba454db41f8b | -16.93738 | -57.6309 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| fb7295bb-d06d-31f6-9afd-f67b7737c66c | -16.93697 | -57.63488 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bf7c2275-efa4-30ff-a460-71df0f55cc5e | -17.2329 | -57.45929 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| cb0e4af2-e103-3d40-967d-5dee1a147730 | -17.31026 | -57.51177 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3c7ba406-65a6-3e23-a059-a7fbdc659090 | -17.55481 | -57.53337 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 790e6791-7161-3651-8e7b-a8e9b759f1ba | -11.79755 | -62.7728 | 2024-11-16 05:46:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39786096-9957-36f3-a5ec-89b94fe7eb8a | -17.59019 | -57.47054 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8ddaa066-b321-36e9-ba6f-345c413e03e9 | -17.55604 | -57.521 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ed3ae1b9-490d-3242-ae6e-25659ad0729a | -15.89624 | -59.25681 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a720c8b9-8146-3f35-814c-0c8dbf2073f3 | -17.25094 | -57.45317 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| c3cde5e4-d6ab-3832-9ca8-36ea99249655 | -17.25053 | -57.45729 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| a73bb5e0-52a1-3d5d-8b03-6d40ed6ee25f | -17.31464 | -57.51083 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| f86c72ea-bb8c-3745-8adc-f8be29d0905c | -17.56095 | -57.52993 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 689de8c7-7ecb-3068-a279-02544744a090 | -16.96523 | -57.63834 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6e4c8239-4f44-311e-9841-ad2cb7a1f3c8 | -17.59157 | -57.57107 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| d12ff665-21f9-3a9d-8f44-db9b51489920 | -17.69144 | -57.57566 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 4b204779-d1d9-3bff-88b6-483a8fcf5ea1 | -17.82898 | -54.54071 | 2024-11-16 05:46:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 80b58edb-d9c8-3d66-9266-52565bf75482 | -17.58359 | -57.47816 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c69b1fe3-5980-34b8-9ef6-1859164adc2c | -17.61659 | -57.55331 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1bf28f71-c343-3afd-b1fd-a72b8c645b94 | -17.23905 | -57.45587 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| b7b74825-c8b6-3b45-a89d-9e2c8b73ea5d | -17.31107 | -57.50358 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6ea46b6e-c85b-36c7-a807-4b8350d516ce | -17.62275 | -57.54988 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 322c7b7c-f5ae-3344-9589-dabf5b8aedf9 | -17.58202 | -57.43578 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d23dc7af-ca39-3ef9-a086-35e6a68518df | -17.58501 | -57.57859 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 23cd2ca4-5524-302c-8571-982de1400490 | -17.57458 | -57.45182 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| cbb3cf11-d2c2-3571-8be6-64d78a068c98 | -17.64726 | -57.55365 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 9b8eb04b-b3ed-3a89-9359-c3c01b766f51 | -17.57888 | -57.58202 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| d86cdf30-4fa1-39d5-a65e-30389109a203 | -17.62633 | -57.57108 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 0aa03444-cca6-3874-9161-681a047c8a43 | -17.59688 | -57.57586 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 3b5af3dc-4e4a-30a8-af2f-a4f621cab0a5 | -17.65422 | -57.54195 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 4ee3087b-b5a1-3f69-9df4-d09dbc52666b | -17.58076 | -57.44834 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4a8149bc-cc9b-3824-be83-32118257e382 | -17.575 | -57.44762 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2053cedf-0a5a-3dfc-965d-825089a42f66 | -17.63421 | -57.55125 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 275e18bc-834d-3126-9577-83aa7b1aaa70 | -17.29602 | -57.467 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ec5cad4c-b895-3a9d-8290-8f46a98d5214 | -17.63499 | -57.5605 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 241297b9-563c-3fbe-9011-ee0d66c98110 | -17.24479 | -57.45659 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 36bc1dae-9242-31d8-b738-8d062cedf4d1 | -16.0435 | -60.11557 | 2024-11-16 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 99f7d435-d867-300f-8557-bcd50cbdfc6c | -17.23183 | -57.45407 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 26f42527-2dc4-36a0-8bfa-edcf4859ebfa | -17.23713 | -57.45889 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| e27aa939-ae14-31a0-8f6d-596b948c7344 | -17.64072 | -57.56119 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 72f46973-e3e4-33c9-ac13-e01e9489af6f | -17.58317 | -57.48233 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 0e672e00-d56b-39f9-ad1d-ad6280bb6bee | -17.63291 | -57.56359 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 7eb406b7-c0ed-31d7-be01-1ee5da3e28bd | -17.65996 | -57.54265 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 840a2792-af86-3d5a-bee4-bbd6607506ad | -17.25502 | -57.47036 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c642945a-d9d0-3b26-86db-72a47a99dbfe | -17.25627 | -57.458 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0d9e0748-68ac-3882-9934-f74b9d29e065 | -15.90079 | -59.26149 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1e742cd4-84e2-3424-9b43-545384db27dd | -17.58725 | -57.49962 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| fab1eae2-d987-3936-9fbb-bcc1640a3a07 | -15.9058 | -59.26216 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fca34317-99a4-386f-91f3-36f76f31ee95 | -17.2452 | -57.45246 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 7864b6a8-20c8-32d9-b50a-ee637ae75720 | -17.64654 | -57.54438 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a89fe98c-be47-3900-8d25-736163d6aae5 | -17.59561 | -57.58815 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5a9a509f-7440-32e4-b4a8-8e2a5db06a24 | -15.89543 | -59.26387 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ae65be1-0d76-3566-84d8-be3372cbe253 | -17.62805 | -57.55469 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d21e2cff-89ca-3bc0-8b60-cc922dc632c1 | -17.64686 | -57.55777 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.3 |
| c75d7663-9d14-35b1-861e-aa5b15396f7d | -17.69675 | -57.58046 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 3a7c1cd3-748b-358b-931c-2c2928f21474 | -11.91025 | -63.67897 | 2024-11-16 05:46:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d2dcbaa-e38b-3b21-b99a-602e6b42ec1b | -15.90151 | -59.25532 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 858cfa46-e8b8-3004-8bc8-e0e43143e709 | -17.56054 | -57.53407 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9fbbcf81-fb19-337c-a76d-c2c5c9e50397 | -17.61617 | -57.55741 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| fc991ec1-a0db-3edd-89f1-adc374af34be | -15.91049 | -59.2656 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e629e48-dde4-3924-a1f3-ad3bb9291ef6 | -16.93214 | -57.62625 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e1e75fe9-9edb-364d-938d-1462990b8c15 | -17.5815 | -57.49892 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| db7ca577-83b3-3850-9e36-16f2f8c7aab2 | -17.55522 | -57.52925 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 873b62fb-2030-3401-8088-492bfb1457f1 | -17.65381 | -57.54609 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 453c3c58-3858-3775-9816-5303688ebd6a | -17.63248 | -57.56768 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 93d06055-b788-30b5-acf8-aa6990fd5e07 | -17.59603 | -57.58406 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 7f42352f-242a-3d69-9ecf-8955dacf3d0f | -17.56834 | -57.51411 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ce343db3-c07f-3b2f-bb1e-cfaa6c903f40 | -16.9422 | -57.63956 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 92da4533-a09d-39f3-b844-d812fa777015 | -17.64524 | -57.55672 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |


[Clique aqui para ver as próximas entradas](README60.md)
