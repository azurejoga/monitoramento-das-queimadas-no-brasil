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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5ea5e2f-9636-30e1-b6eb-fe3f999e7a98 | -20.08193 | -51.33225 | 2024-10-01 04:17:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 594e9001-a206-3549-9bd4-d709fe09eef7 | -20.07299 | -51.33601 | 2024-10-01 04:17:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de29260e-04b5-3e02-8a69-219f102ae03c | -20.07197 | -51.34146 | 2024-10-01 04:17:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4d443e3-b77b-3154-8120-09b7a0224b2c | -21.71608 | -51.64683 | 2024-10-01 04:17:00 | NOAA-20 | PIQUEROBI | SÃO PAULO | Brasil | 3538303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2ee13e2b-1d0d-374e-8ed4-8290b4836b78 | -18.71025 | -57.32276 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0c541311-ceb8-3bb0-ab28-889fa9499a92 | -18.70924 | -57.32728 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d9c131a1-83e7-378b-9983-2cf70d0dd332 | -18.70823 | -57.31629 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| c54ffe04-3007-3b75-baaf-a9355f822e4e | -18.70724 | -57.32083 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e251320e-0c36-3812-8683-cfe649dc155e | -18.70626 | -57.32536 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| cf58e228-d82d-3011-be43-b897e9603aae | -18.7054 | -57.31676 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 93c54030-f6de-38ec-8fcc-0c53fdf9bc9a | -18.70438 | -57.32129 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| a06378d7-1114-306b-afbf-a0127a9d98d8 | -18.70337 | -57.32581 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 0fe4cadf-755d-3c4a-8f4b-43eb5f1c5ef8 | -18.70138 | -57.31932 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| dd3f93f0-9e90-32d9-af4d-3d92ca9954fd | -18.70039 | -57.32386 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 3463d1b3-d41a-3be9-98d9-4688012876e3 | -18.69941 | -57.3284 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| a0d7f5b1-1f79-37eb-9cc7-1c7c4832e167 | -18.69852 | -57.31979 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 706616f0-318a-3c2c-a60f-7df6cedc5e3c | -18.69842 | -57.33294 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 869ec930-b9bd-33ac-a47c-02ecbc7cad25 | -18.6975 | -57.32432 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 66837ea1-4879-374d-b4c5-e64834c9ad69 | -18.69648 | -57.32887 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b4622f49-b286-3a56-a109-3b318cb3304a | -18.69546 | -57.3334 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 70479b9f-d61a-3b62-b138-b38f9f4dce7a | -18.69354 | -57.3269 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2e25a01f-e5b2-3280-8a47-09a615ee8247 | -18.69254 | -57.33145 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9d5d0bcb-ff86-3242-ae6c-b4dc16d1b312 | -18.69061 | -57.32738 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a8d778cd-be16-3b00-897d-a8452b647061 | -18.68959 | -57.33192 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 22810add-c4bd-3644-9899-96ba6f2e5d3f | -18.68667 | -57.32994 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bd221fa9-307e-31a4-aaea-a614baca7706 | -16.17944 | -58.43008 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4ce1769e-5348-31ed-a4b0-b84ffc7f41d5 | -16.17677 | -58.42972 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 16406310-207a-3fb8-86a1-2dc31bf75636 | -16.17161 | -58.43426 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ee991a36-3005-35c0-8cf9-4b5793a3d69d | -17.05985 | -56.76716 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 767e6eaf-1273-3d81-a37d-418321fcbb3c | -17.05889 | -56.77166 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b9c6bb65-5239-340c-b1b4-27ac60a5c6e8 | -17.05773 | -56.76566 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b386ba90-6194-3a52-8ec3-5fbcf62a92b0 | -17.05674 | -56.77013 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 76425d60-7e36-3e20-b003-8ad405d8dd39 | -17.05398 | -56.76575 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| edcc1e24-735d-3aa2-a202-be0892471cde | -17.04908 | -56.75983 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 85a21974-a38e-3cb5-bb1a-ee1156bf2439 | -17.04813 | -56.7643 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c5182866-dd41-3d8b-b96d-59500ba4dcfc | -17.04608 | -56.74501 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 63202380-a70a-3749-b355-732473eb7248 | -17.04513 | -56.74949 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e3b7866f-ca97-371f-868f-7d3cec19ed3d | -17.04118 | -56.73914 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4c50f410-7b35-31df-ac56-a16ce89c4bcb | -16.89524 | -57.70037 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9811275d-c00f-3c46-aa20-6de5fd95a76c | -16.89409 | -57.70553 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| baddfcde-26e3-306a-9def-73c1d7259805 | -16.8924 | -57.69662 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 195c56d5-e28d-3ba4-aa0c-ae86aa634c93 | -16.89128 | -57.7018 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a0e293c7-008e-3c2a-b252-9ad588dc0343 | -16.89065 | -57.721 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b040a4bd-0f1b-37ed-8560-3dba2abaf4f4 | -16.89017 | -57.70698 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 72698b5a-e3db-3f8d-9f1d-8ff908c417aa | -16.88903 | -57.69886 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| da228397-7db9-3e5b-925b-5c2df0c56b9b | -16.88794 | -57.71731 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 84ff90a9-29dc-3a0c-b36b-b9770f4f267d | -16.88788 | -57.70401 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| bda269af-4563-315c-a3d8-40cadcfb3f67 | -16.88682 | -57.72248 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6fb9dcf2-78ad-324c-8f1d-670f15ec5d02 | -16.88673 | -57.70918 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f4053acb-e1cb-33a4-b45f-e872d2dc5fc5 | -16.88558 | -57.71433 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 341fafae-096c-35fd-9a01-bad4769bf4f6 | -16.88443 | -57.71947 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4e701cbd-ddfd-367d-9796-197e87edc790 | -16.88395 | -57.70543 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 853a4822-1b19-3982-8674-601776283dbb | -16.88329 | -57.72462 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9e53889e-23f8-3dec-b837-8d7a3976c516 | -16.88283 | -57.71061 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 3bfe2fe5-9c9c-39e5-a12c-4cce0ce7606c | -16.88061 | -57.72092 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0d17299d-4140-3a4b-ac20-a27389a67ea3 | -16.87153 | -57.70234 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6bdb7c0e-e240-3c6d-9022-f5db7bcefc71 | -16.86924 | -57.69946 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e170962c-3ea0-304c-bbd1-d8d324786f62 | -16.86808 | -57.70461 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cc09e1f5-83f2-369a-94be-6fba9ff8c5d8 | -16.86644 | -57.69563 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 734f83c6-970e-327d-9143-c4d68a90902f | -16.86532 | -57.7008 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f9e8a16f-45e2-37ee-b4bc-f1bac71adbf6 | -16.86303 | -57.69794 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 093f05d2-96ef-30d7-a935-9a4e9f7762d6 | -16.85911 | -57.69926 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ebab8fa4-532e-3896-b05c-dd2286f3122a | -16.85289 | -57.69773 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 58ef9f19-2dd2-394a-a248-d40e299cd23e | -16.7731 | -57.82113 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 20265bfe-3a8a-3b39-ae7a-3f7409b6c4ad | -16.76419 | -57.79013 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bbeafe77-3c00-3d65-b296-423008a73f34 | -16.76304 | -57.79543 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3c5ce590-d19d-305a-8617-fbf8dc2aeb0d | -16.76016 | -57.79025 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ecb2bbc1-26ef-3859-aa27-c23bf3a51b80 | -16.75899 | -57.79551 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| af15a952-7029-35a6-84dc-0133f33a4005 | -16.75781 | -57.80075 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bcf38d78-5ea5-3634-ae01-647df8409246 | -16.75565 | -57.79914 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9897ce79-1ec0-3724-b351-3b57b0c9fbd4 | -16.74725 | -57.41916 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8f7c71a2-74f8-3f05-bead-40955559e632 | -16.74615 | -57.42414 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| cb8fca8e-a4b8-3c28-bd54-011a821b6e29 | -16.74002 | -57.42266 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 2cc540e1-2191-3102-a43c-9ba4d2744cd7 | -16.73892 | -57.42764 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a264db97-ab91-3f78-ac23-c1704cd7265c | -16.73475 | -57.42334 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d7427e52-4578-3d00-83d7-9c79094eb760 | -16.73389 | -57.42117 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 82870fa4-5524-3b4d-ab10-a9a452fe8a4b | -16.73279 | -57.42616 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 46d2948b-92f6-302b-a5d5-6218d3589809 | -16.72862 | -57.42183 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f25fcd4c-d7b9-35f3-b8d1-7068588b415b | -16.72776 | -57.41968 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 985f3620-74a6-37fa-82ef-82f60594d3a3 | -16.72666 | -57.42466 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a008e11c-d806-335d-b645-30c2d8eae2e6 | -16.64849 | -57.29122 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7b83d52c-817b-3e08-8865-07ac4200702b | -16.64745 | -57.29613 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| db9da5f9-46c8-3f63-9956-e48058aed38f | -16.64732 | -57.29254 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7d4c5fd1-83ce-3ee3-8fb2-0dd9f3200981 | -16.64624 | -57.29745 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 681bea25-2c30-3787-ba88-deca9e6a4f2a | -17.1026 | -56.72964 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 556cc0f0-0a0d-3b74-8c45-89b9a60d411e | -17.10044 | -56.72083 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 61b08fc1-5178-377d-ae92-9bd1fcc5b7ef | -17.09951 | -56.72525 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 8c599f29-8df3-3921-bf0b-183dc84bbfb0 | -17.09868 | -56.71941 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 07282ed6-720e-3458-8bbe-6ec150890775 | -17.09858 | -56.72968 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| cf80ecbd-dd50-31b6-b690-0f83545acc37 | -17.09772 | -56.72382 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 0f5a2275-05d2-342e-af44-d724675a864d | -17.09675 | -56.72824 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| c268e7ba-216b-3a65-bf99-83f3460c128e | -17.0946 | -56.71938 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 90f9488a-2e15-385e-9d9d-27d900d835d5 | -17.09367 | -56.72382 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6473d479-061b-3818-8c93-7bb1665b70c4 | -17.09284 | -56.71799 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 74ab5283-cfa9-3911-8687-83d608d98460 | -17.09273 | -56.72827 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 2621298d-eaf2-3984-aee0-daead8740b40 | -17.09187 | -56.72241 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a1d123bf-f428-3581-96c5-8bd21b00f580 | -17.0909 | -56.72684 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| df7a32e1-aec1-3579-906d-43ef4df241fb | -17.08994 | -56.73127 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 15d4562d-1fa3-3deb-aa7d-3298a6b69d89 | -17.08876 | -56.71796 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 63612d90-13a7-37a8-91a7-f549525c580b | -17.08782 | -56.7224 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |


[Clique aqui para ver as próximas entradas](README97.md)
