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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 183adac9-f7d5-37f1-a334-d3138d46d899 | -12.8069 | -44.8375 | 2024-10-12 02:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| d16abfc3-1f37-382a-b879-2119825e67ab | -14.3246 | -57.6002 | 2024-10-12 02:46:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 52f821fa-7fc2-3950-8f4f-8f2e6e15fadb | -14.3249 | -57.58 | 2024-10-12 02:46:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7c443c27-2b92-3852-8825-6c77a2ff1ecb | -16.9805 | -57.4404 | 2024-10-12 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| e5e65199-1f3b-3ee8-b686-c117a1d5a26b | -16.9995 | -57.4791 | 2024-10-12 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 531a7e10-8f9f-3476-8321-2ba74176294a | -16.9998 | -57.4586 | 2024-10-12 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| f0e34beb-4475-32d5-b0ad-403cf0ccb39b | -17.627 | -56.3318 | 2024-10-12 02:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 468da319-02ca-3697-a350-b4bb84d82b96 | -17.6467 | -56.3292 | 2024-10-12 02:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.0 |
| 151c6c27-a36f-367c-9f63-dc22b606266b | -17.6471 | -56.3084 | 2024-10-12 02:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 7e9259cf-d8b2-3d14-a2c8-88fb06cc9634 | -17.6478 | -56.2668 | 2024-10-12 02:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 0da84f4b-1de4-3456-98a8-6c26d0a15a66 | -17.6675 | -56.2643 | 2024-10-12 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 0b8bd4fe-cdd4-38d6-90b8-f0913a54e09a | -17.6679 | -56.2435 | 2024-10-12 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 1430fb06-30fe-3595-bcaa-d62586584b83 | -17.6873 | -56.2617 | 2024-10-12 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 7b87d828-ee2e-3439-9da9-e27497af9cc5 | -17.707 | -56.2592 | 2024-10-12 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 61c675c9-e989-3f7f-9180-e7b7981dd8a1 | -17.7074 | -56.2383 | 2024-10-12 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| ce54178a-0f84-30bd-9c79-a867214b7403 | -17.964 | -57.3843 | 2024-10-12 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 51056f29-8f86-39cb-ba2d-ad05b0a4e0e1 | -17.9643 | -57.3637 | 2024-10-12 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 868e23d8-496c-3ac8-9c3b-dce72392c143 | -17.9837 | -57.3819 | 2024-10-12 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 91eca70d-0afa-31ad-b7e8-1c7564ce1794 | -17.9841 | -57.3612 | 2024-10-12 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 96cd2251-7dd0-38be-96f3-865dcd868a95 | -2.77 | -51.3829 | 2024-10-12 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| da44f926-b85c-3645-bc06-d438f43eeb8a | -2.7701 | -51.3622 | 2024-10-12 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 399c78fb-339b-3dc0-9276-fee776929568 | -2.7884 | -51.3825 | 2024-10-12 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 394859c0-ac01-3be4-9012-656344015030 | -2.7885 | -51.3618 | 2024-10-12 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| cf009437-1b86-342c-8332-9241d98a46ed | -2.8254 | -51.3401 | 2024-10-12 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 5d4c5fed-2fe4-32f5-99fa-b525b251a32f | -2.8611 | -51.6699 | 2024-10-12 02:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4cecc77f-2f5a-3eef-9ae6-d54588191c30 | -3.6978 | -50.1225 | 2024-10-12 02:55:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| bcd0ac78-af76-38ac-8e70-1dd00fa571ed | -3.7087 | -47.9227 | 2024-10-12 02:55:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c4a27ab0-518a-31c4-ab89-edab91e8cd17 | -3.7163 | -50.1219 | 2024-10-12 02:55:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 1638ce3f-3be5-35e0-93b7-02536580669f | -3.9265 | -42.4246 | 2024-10-12 02:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| d786bd43-54c0-3472-851e-d38b0a43fb37 | -3.9267 | -42.401 | 2024-10-12 02:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 49.6 |
| 374f0783-a3ea-3dd0-9511-abcacb9592ac | -3.9396 | -46.4229 | 2024-10-12 02:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7ee02b39-ffbc-3006-af36-df817d9fd668 | -3.9394 | -46.445 | 2024-10-12 02:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 3cfe2f81-4772-31de-9ce7-4b18406784c9 | -4.1148 | -48.2515 | 2024-10-12 02:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| b1436e25-3bfe-344f-91d4-6c84e64c3999 | -4.8562 | -45.6838 | 2024-10-12 02:55:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 26e7f487-ddee-3f4d-baea-0a64bd0128c2 | -6.747 | -59.3259 | 2024-10-12 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| e655e107-4e85-3962-8edb-a6fef5194f01 | -6.7469 | -59.3452 | 2024-10-12 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 1ff845ce-02b4-3db2-b275-84f7c5ccc1a2 | -7.8715 | -54.7016 | 2024-10-12 02:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9fffaa7b-e1b6-33f5-a31a-13a73df1758c | -7.8713 | -54.7217 | 2024-10-12 02:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| ef87451e-3a9a-35a0-85e4-ba343fabef87 | -8.4417 | -55.4692 | 2024-10-12 02:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 1861a023-17e8-316f-a608-b182eacc57a1 | -8.4233 | -55.4503 | 2024-10-12 02:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 502ac4cf-d343-3732-a676-585cc205e794 | -8.4231 | -55.4704 | 2024-10-12 02:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 5dad5ed2-435e-3af0-a156-aed93e5f2b9a | -10.4662 | -58.7625 | 2024-10-12 02:56:06 | GOES-16 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4fc08ec4-a05a-3734-a68a-deb18ebfae8e | -10.9506 | -44.653 | 2024-10-12 02:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| b70b04b9-3465-39a7-b164-a41dc5ff73d3 | -11.2719 | -50.9441 | 2024-10-12 02:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| a22bdbff-5bfd-33a3-a7ca-36612e5c2bc3 | -11.8377 | -58.8445 | 2024-10-12 02:56:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| fa3d6825-2274-3f7e-b8e7-f1c8c66607bc | -12.456 | -54.5554 | 2024-10-12 02:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 2ad8eac4-6271-3a97-8c5d-02ef0e0316b2 | -12.4558 | -54.576 | 2024-10-12 02:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4f3fb599-ec89-3386-8ac6-9604736a096e | -12.437 | -54.5573 | 2024-10-12 02:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 819bc786-76c9-3943-9dca-2e9f7593798f | -12.4367 | -54.5778 | 2024-10-12 02:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9ac26f94-3aaa-398f-a196-85dc106c3b07 | -12.7871 | -44.8639 | 2024-10-12 02:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4e9b5418-eafb-3d21-a180-190a34ee88e8 | -12.7875 | -44.8406 | 2024-10-12 02:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| d0c70c7f-e122-3f57-8778-c8748526afcc | -12.8064 | -44.8608 | 2024-10-12 02:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 57229d63-35aa-3163-90e5-b949c74f616f | -14.3249 | -57.58 | 2024-10-12 02:56:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b117054a-9601-3116-a7d6-256d637e4201 | -14.3246 | -57.6002 | 2024-10-12 02:56:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5ea6e914-8d00-335a-8f43-2731c5749704 | -17.6467 | -56.3292 | 2024-10-12 02:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 2a012dcf-a423-3044-b72a-9a3634f7884d | -17.6471 | -56.3084 | 2024-10-12 02:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 42f18ef2-c70d-35e8-9114-7b194c10dc62 | -17.9837 | -57.3819 | 2024-10-12 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.2 |
| 1af653b4-e443-3925-8de7-6a58bd2ca45b | -18.196 | -56.5275 | 2024-10-12 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 0151fbd2-1818-3d15-9da3-ca10a394c0a9 | -2.8254 | -51.3401 | 2024-10-12 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 389a361e-d9ad-3710-ad00-fdf433d4bc4d | -2.7885 | -51.3618 | 2024-10-12 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 638df17f-31f7-38dc-94a0-855eee5c13c5 | -2.7884 | -51.3825 | 2024-10-12 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0b945fbd-569d-3c51-b4fe-36f2241f31e7 | -2.7701 | -51.3622 | 2024-10-12 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f4e9aaca-6e8e-33fc-b696-3cbeb2d39b8d | -2.77 | -51.3829 | 2024-10-12 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 79c39fbc-4477-3184-b0c5-c11e3f813c8d | -3.6979 | -50.1015 | 2024-10-12 03:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| adc981cd-5532-3ffe-8ddf-3701c6699b14 | -3.6978 | -50.1225 | 2024-10-12 03:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| cfa7bdc6-6000-3ad9-90f6-ae55039fae7e | -3.9581 | -46.422 | 2024-10-12 03:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 29fa891e-303e-3257-b9a7-f7acd7178b93 | -3.958 | -46.4442 | 2024-10-12 03:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 5c13da07-76ab-3e75-b54a-02b7f6fe2861 | -3.9396 | -46.4229 | 2024-10-12 03:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 737521ff-08a0-3658-88eb-a7aa29abd53a | -3.9394 | -46.445 | 2024-10-12 03:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 5f0454cc-7693-3fa0-856a-2056ed944933 | -4.1148 | -48.2515 | 2024-10-12 03:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 7b2a2571-78df-3640-b737-d3c643028e78 | -4.3782 | -50.8087 | 2024-10-12 03:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e55a2f7d-c36b-3225-af55-31e3ba82193d | -4.8562 | -45.6838 | 2024-10-12 03:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ae1fbb66-79d7-34fb-831c-8ed8bebd11b3 | -5.3997 | -45.3574 | 2024-10-12 03:05:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 17c305b4-c191-3bd5-96a2-56f061db8a15 | -6.0791 | -44.6276 | 2024-10-12 03:05:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 3ad21b85-d049-3669-bb05-bba15e6847a1 | -6.7469 | -59.3452 | 2024-10-12 03:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 31559b9f-9813-3887-96f1-07bf803593c2 | -6.747 | -59.3259 | 2024-10-12 03:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 46abd357-1cc3-3a8c-a3d7-dcfab5beaf35 | -7.8529 | -54.7027 | 2024-10-12 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 39f19ad4-cd3c-3c81-912f-856dc90ef94f | -7.8713 | -54.7217 | 2024-10-12 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 24d1ce89-a121-3435-836e-419bf8f655a4 | -7.8715 | -54.7016 | 2024-10-12 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 44ca1902-6d55-30fb-957b-176ef5d0f76e | -7.8717 | -54.6814 | 2024-10-12 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 71c39596-37d6-3b2e-9bd6-7a15019745b0 | -7.89 | -54.7206 | 2024-10-12 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| f1072b06-ae56-3b1c-8a21-e5358bdeab6d | -7.8901 | -54.7004 | 2024-10-12 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| c3e8a0b0-b412-3c2e-998f-a26684abd545 | -8.4231 | -55.4704 | 2024-10-12 03:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 446445dd-6b61-3691-8577-0771110da377 | -10.4079 | -61.2685 | 2024-10-12 03:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 75777476-d81d-3b53-afad-b3983e6b0385 | -10.4662 | -58.7625 | 2024-10-12 03:06:06 | GOES-16 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 70dfb920-daa9-34f9-a116-311b85a6d5a9 | -11.3105 | -50.8974 | 2024-10-12 03:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 3dc20dea-7ff5-335e-bbcc-08b74b9b9096 | -11.8377 | -58.8445 | 2024-10-12 03:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e4917ab8-0f4f-3ff3-ba44-989a9f6732c0 | -12.4558 | -54.576 | 2024-10-12 03:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 500a7910-3abe-3b35-95eb-5e4a38ac214d | -12.456 | -54.5554 | 2024-10-12 03:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d86b172d-c523-3e86-89f5-48641deb282b | -12.9461 | -53.5548 | 2024-10-12 03:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3e81c0f8-f4c8-3ccc-96e1-3a3198282d23 | -12.9464 | -53.5339 | 2024-10-12 03:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 220.8 |
| b7c317a7-efa4-360d-a71c-7caebb7ff97b | -12.9467 | -53.5131 | 2024-10-12 03:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 167.0 |
| c0567e14-d0d3-3a60-9d5d-633056ac1d08 | -12.9652 | -53.5527 | 2024-10-12 03:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 7cc166f1-960c-359c-9e5e-7e473830fe2e | -12.9655 | -53.5319 | 2024-10-12 03:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 280.7 |
| 57f88c9f-5f09-3853-abff-c581f7fc24ea | -12.9658 | -53.511 | 2024-10-12 03:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 207.8 |
| c5926a1e-5252-3124-8d4a-354b0bfe50a5 | -14.3246 | -57.6002 | 2024-10-12 03:06:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 92848bee-932b-3772-8450-69dae7e64553 | -14.3249 | -57.58 | 2024-10-12 03:06:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b9134f5d-f79e-35e3-8b4b-52329c8efed4 | -16.9805 | -57.4404 | 2024-10-12 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 5895cdf6-9cd5-32ac-88d6-7b844d149261 | -17.1761 | -57.4585 | 2024-10-12 03:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| ae3177b1-d4eb-3412-82c8-08cabb02b432 | -17.6679 | -56.2435 | 2024-10-12 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.9 |


[Clique aqui para ver as próximas entradas](README33.md)
