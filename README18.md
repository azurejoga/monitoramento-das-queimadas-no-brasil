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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4afa34b3-a6af-33fe-b3ff-c1c30c221afc | -17.217699 | -57.300499 | 2024-10-16 01:33:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e36b3c8f-e0af-33fa-84c5-5092cc5917a4 | -17.219299 | -57.307701 | 2024-10-16 01:33:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9ddfacaa-e5f4-322f-bf7e-ad7ffa51cf23 | -17.221001 | -57.314999 | 2024-10-16 01:33:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21923c82-402b-32a4-9bd3-d121bd56e104 | -17.222601 | -57.322201 | 2024-10-16 01:33:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e535581-defc-30fb-bae0-09daf8e46cb2 | -17.1089 | -56.870998 | 2024-10-16 01:33:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89660d2e-53f7-3b9e-aa29-b97e87d90803 | -17.1106 | -56.878399 | 2024-10-16 01:33:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 900a35ea-302b-3aa5-8840-2b506654e323 | -17.2096 | -57.310101 | 2024-10-16 01:33:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3329a2d7-7080-3629-b5a9-5a948d8e157a | -17.0811 | -57.4254 | 2024-10-16 01:33:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6cab6bd-3bd9-3bfe-8b93-32c929bcffad | -17.0893 | -57.461498 | 2024-10-16 01:33:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2476f28-d32c-349d-90ec-b035cad30d6f | -17.071301 | -57.427799 | 2024-10-16 01:33:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8cd5995b-789b-3838-a2a4-7d5b415b828f | -17.0779 | -57.456699 | 2024-10-16 01:33:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8220230d-278a-3323-bd1f-c99be893b147 | -17.079599 | -57.463902 | 2024-10-16 01:33:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4fa55d8-38bb-36d8-ad85-8b5b58492d6f | -17.0812 | -57.471199 | 2024-10-16 01:33:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2092bad-e667-3915-a8b1-8e3835660775 | -17.048401 | -57.3722 | 2024-10-16 01:33:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11cfb5f4-2be3-3e7b-84df-b3be65ecd1bc | -17.0632 | -57.437302 | 2024-10-16 01:33:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a932a392-4eec-32a3-be8c-15e6fb79947f | -17.0648 | -57.444599 | 2024-10-16 01:33:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91847c55-24cd-35a8-98b2-85f8a8241a78 | -16.891899 | -56.736301 | 2024-10-16 01:33:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f3c71738-d266-3128-b9c5-890ddd091cfd | -17.035299 | -57.3601 | 2024-10-16 01:33:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 06872189-0922-3bd1-ba2f-770e617edca0 | -17.0452 | -57.403599 | 2024-10-16 01:33:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c1b77aa9-282e-3207-8143-7ba16abb7ad1 | -17.046801 | -57.410801 | 2024-10-16 01:33:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eb14aa7a-344a-37ee-8cfe-b82c8a36441f | -17.048401 | -57.418098 | 2024-10-16 01:33:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0920daf6-4df3-3431-b829-adb10d1bf26e | -17.0126 | -57.442001 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aaf0e1c4-fce9-3604-8553-bebc340270f4 | -17.014299 | -57.4492 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8e5ccde8-b768-3c96-9542-2d350fb9fc34 | -17.0159 | -57.456402 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d5fd834c-d138-3882-8dec-9264ba52e87c | -17.017599 | -57.463699 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 16534b56-f716-3392-8d11-5cf4cbdf27aa | -17.019199 | -57.470901 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b251527e-f520-37c7-a57c-8f902e5fe450 | -17.020901 | -57.4781 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7db12afb-fbd1-3929-9a0d-b7a1be4e478d | -17.022499 | -57.485298 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6e8dabf-01a7-3ce0-be2b-b66f3339e35a | -16.989901 | -57.478001 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0d01c6ce-55d8-3a17-b41c-9fff4fda1fcd | -16.9916 | -57.485298 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a160e9ac-c07e-3d2c-80f1-e92f3c118cc7 | -16.9932 | -57.4925 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7727d22e-3665-3fcd-87ff-fd90378a4202 | -16.994801 | -57.499699 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7ad31bd-0394-3217-bebc-fb05f1437fde | -16.9965 | -57.506901 | 2024-10-16 01:33:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ecd974b-4ab1-3d39-a303-28ea707fe967 | -17.1544 | -56.8442 | 2024-10-16 01:33:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dda04c07-1efd-300d-bbe8-5bbe1650210f | -17.156099 | -56.851601 | 2024-10-16 01:33:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa1d504b-bfca-3e44-9826-55de457e53e0 | -17.141701 | -56.878601 | 2024-10-16 01:33:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3b0d3acd-13c1-369b-b0f9-5ee3e1012d7e | -17.130199 | -56.8736 | 2024-10-16 01:33:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| adb4d97c-35b6-3a6e-aa2d-cbee3e1fb91e | -17.131901 | -56.881001 | 2024-10-16 01:33:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3389d4e4-6877-3293-91d6-c7f5e32d92ba | -17.017599 | -58.2869 | 2024-10-16 01:33:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 190ebb11-6447-34fd-b9a0-3f9901867131 | -17.019199 | -58.293999 | 2024-10-16 01:33:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79bfdb84-f430-32b9-8d41-f62a68e1724e | -17.0208 | -58.301201 | 2024-10-16 01:33:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2ebb7c7-dd04-33d1-94f7-0880179e5181 | -17.007799 | -58.2892 | 2024-10-16 01:33:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eeef98e5-c8ea-32b3-9335-bc2da818eb80 | -17.009399 | -58.296299 | 2024-10-16 01:33:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4107084a-4b2b-306f-ae85-a9b57552a50c | -17.063101 | -56.851101 | 2024-10-16 01:33:58 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95b34ee7-35cb-3669-ab52-2cf4a539bed2 | -17.0648 | -56.858501 | 2024-10-16 01:33:58 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7db1f915-0ab7-396e-aa32-6e5978d3809c | -17.0665 | -56.865898 | 2024-10-16 01:33:58 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2d075d4a-3f3a-3667-93b4-e7ba9910a2c4 | -17.187201 | -57.483501 | 2024-10-16 01:33:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cdbb6389-c789-369f-a986-14f4114c0a70 | -17.1791 | -57.493099 | 2024-10-16 01:33:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f873c0b8-6bf8-372e-8a44-33b38bdf9c58 | -17.0355 | -57.405998 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc47e398-c1b4-3974-85bc-33479b5045ca | -17.0371 | -57.4132 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cf46133c-65c2-371b-932d-4e02ef194239 | -17.0387 | -57.420399 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 374f09a2-bac5-3d1d-9ba3-3c56360e6a7e | -17.0404 | -57.4277 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2fda5ecf-8f31-3b63-a674-e6c277712ea0 | -17.0191 | -57.379299 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8877443f-e2cb-3f08-979e-10801c1618be | -17.0207 | -57.3866 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d95e1eb9-0e43-3cef-8d02-ea9ba2d834c6 | -17.0224 | -57.393799 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e006435a-9f9c-3c32-a503-9da29a8db8d9 | -17.0257 | -57.408298 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e351d293-b9eb-380a-93de-01f4ef4a6612 | -17.0273 | -57.415501 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 735290eb-8132-37d7-80b4-4a4beebb533e | -17.0306 | -57.43 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 888c4ea3-d4e1-3a8c-970c-d039b9082b30 | -17.032301 | -57.437199 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40884fb0-3fed-3a68-86fd-33dbaccce55e | -17.033899 | -57.444401 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2873e08d-56f4-36e9-a7c4-a5b1e19770cf | -17.035601 | -57.451698 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 238e6757-2a38-35a4-a482-fab03e9be209 | -17.022499 | -57.439602 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 14f07217-a13f-3ff8-bb1b-6d47d7694c50 | -17.0242 | -57.4468 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 34c79005-c6a3-36ed-a039-9981f617e5ee | -17.025801 | -57.453999 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08204474-3a2e-3aad-903a-441166ae0755 | -17.0275 | -57.4613 | 2024-10-16 01:34:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| abb564e6-39be-3941-9302-bf1f14790a89 | -17.004601 | -57.451599 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 25dccfd8-595e-38b0-a539-7aba54d1d799 | -17.006201 | -57.458801 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7571a821-5f2a-3152-83d3-9133fbc63570 | -17.0079 | -57.466099 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2bce27f4-8d0b-354b-b038-fe9a49742175 | -17.009501 | -57.473301 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c432914-1f41-3ccd-b1e7-bdba7a470701 | -17.0112 | -57.480499 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96f4aeb7-8562-3b2a-9b5d-1e963f99dd0c | -17.0128 | -57.487701 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 78815c94-aa6e-3b11-b7c5-8a7420e840c2 | -16.996401 | -57.461201 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08cb807a-db87-3f14-a14f-ce1064251d7f | -16.9981 | -57.468399 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8df6aab5-9f20-3728-bcec-85a468be8e43 | -16.999701 | -57.475601 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0b7b35ad-f902-39bd-a909-8ced170017af | -17.0014 | -57.482899 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6bf573ed-ead0-3f19-a98c-ce1f02788af1 | -17.003 | -57.490101 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5bf67ad6-034f-340d-b597-8e479f534ce3 | -17.004601 | -57.497299 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| da791f4d-28a2-3fe8-8e93-3016f151eba0 | -17.0063 | -57.504501 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2455f173-de01-3976-ad5a-272d7ae2fa4c | -16.981899 | -57.487598 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f2ec3bd-ec6a-30dc-9e56-0dd77c170a81 | -16.9835 | -57.494801 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c2f159c-0034-35f7-8eba-c5e98b2e352c | -16.9851 | -57.501999 | 2024-10-16 01:34:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 559659c2-55bf-3c9b-8148-3c3d459061a1 | -16.955799 | -57.509102 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d558f1b-045c-3e7a-9b98-fbd3121abf20 | -16.9575 | -57.5163 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bca44dc1-707d-3a19-8a5d-0283d05276ff | -16.959101 | -57.523499 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fff94a14-7c8e-38be-b106-bf0899ae64e5 | -16.942801 | -57.497101 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 326e44a8-465b-356e-9b14-ae06246f9273 | -16.944401 | -57.504299 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 175f47a1-383a-3f47-8561-dd0211ccb38d | -16.945999 | -57.511501 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d35b328a-4ae8-3397-8738-30a983990db7 | -16.947701 | -57.5187 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 915c5196-162a-32be-a21f-06aca60edb62 | -16.949301 | -57.525902 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| efdf03cb-9180-3d6d-8524-4d5f32fb5c34 | -16.933001 | -57.4995 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6666d5dd-d161-3907-939c-aaad25e08ebc | -16.934601 | -57.506699 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43bc38fd-2405-3e7e-8c40-d3feb293a48a | -16.936199 | -57.513901 | 2024-10-16 01:34:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bac5086f-29be-312b-b0e5-4bd82f89ce59 | 1.0199 | -52.2162 | 2024-10-16 01:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 3c3c14e8-937e-3e3f-a856-1e4a97917843 | 1.0016 | -52.2164 | 2024-10-16 01:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 39.0 |
| b6847875-bf1e-3f02-9df1-a471f9d9c9ed | -10.8302 | -49.236 | 2024-10-16 01:35:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbb10661-a9e1-3d15-bd29-b6a37fb1c874 | -10.8366 | -49.260101 | 2024-10-16 01:35:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af00e48c-7990-31ea-98bf-b6f8e0d50159 | -10.0009 | -48.635201 | 2024-10-16 01:35:11 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5859b78-8743-3c3d-ba04-3f36249f6a96 | -2.5444 | -47.2231 | 2024-10-16 01:35:20 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 5de05ecb-6017-3a70-bb61-65ad9526256e | -12.7381 | -63.034302 | 2024-10-16 01:35:23 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 89f41caa-5b6b-3b99-98b9-39e6dc87f0cd | -3.1098 | -54.2464 | 2024-10-16 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |


[Clique aqui para ver as próximas entradas](README19.md)
