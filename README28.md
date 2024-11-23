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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5caee48a-b9ae-3c7d-9e74-93ee72d8bf7f | -1.20657 | -51.75242 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e186d92d-cec5-3651-9d0c-c18f9db29429 | -2.53921 | -46.37117 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a230289-9db0-392d-8c8e-06114813d2f2 | -1.26034 | -53.36766 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9ca0e2a-7cc7-37b9-9e0d-dc028b7bf32b | -2.44685 | -49.08372 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 784d9598-3a58-301e-bd80-d14b195512f1 | -1.24911 | -53.36583 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21bbfbe5-8d6f-3353-a3dc-ef9efeb4c16a | -3.18392 | -46.55273 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dec1bd64-a2a4-3d96-b085-c517b739d0e3 | -2.14714 | -50.91998 | 2024-11-23 04:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ecc42524-ead5-39c3-aac2-c356fd7e575a | -2.19276 | -48.21014 | 2024-11-23 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06422c89-c555-3300-98b8-66dd808b1653 | -2.65646 | -46.13919 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2cf370d-c75a-392d-8289-d8b2f62a9422 | -2.67076 | -46.16109 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8801f8f2-7b63-38cf-a589-30535cc0217a | -2.69431 | -46.19238 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cfec715-c678-3498-bd1d-e910a2ea79f4 | -1.62228 | -52.43528 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f12fbb16-f6c9-33a3-b7bf-ed9c94797349 | -1.2437 | -51.74652 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cce58e00-4eca-3cc2-985c-c6fcd2d91ced | -2.6937 | -46.19622 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b894538b-1762-39fc-8d79-576c33025d2c | -3.34118 | -45.17069 | 2024-11-23 04:16:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 589651ea-9a13-32d3-9056-c90b925b00fa | -2.81952 | -45.16217 | 2024-11-23 04:16:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a71a88b-997c-3c83-92ed-ae0af7f9ed66 | -2.44544 | -46.55204 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d3d2f00-dc0d-3b92-acc1-604ee95b1b87 | -2.56747 | -46.5573 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be5a99de-7d85-39f9-b253-fdbbf49709b1 | -2.6518 | -46.57484 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49e2d484-9394-30d5-8d3b-13cec1f098e0 | -2.44896 | -47.03007 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cb442d4-38f9-394d-8932-f51c0f40e09c | -1.40188 | -46.52979 | 2024-11-23 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 623c61ce-ca4e-3b53-a7b8-43136270d0aa | -2.66381 | -46.16 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4305edf4-e8a6-3e6e-8621-6cc134105729 | -1.6254 | -52.6139 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f017b8e-6a03-3cce-b11b-696c5ab07614 | -2.50909 | -46.21557 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62e718ad-cdd4-3556-ad86-9ce08345d945 | -1.62064 | -52.60973 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d9d5fb2-f1e1-3916-9970-3d498ff226b3 | -1.25646 | -51.76357 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 47d9cfda-1d9f-34e2-9e04-03d490ed49af | -1.12399 | -53.40663 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75c62b0f-4f28-36f8-84f1-0059babe7f7e | -3.07655 | -45.97085 | 2024-11-23 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45ae86df-0412-38c6-b196-66622913b8f3 | -1.72124 | -52.71842 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86a882cd-9925-36eb-b163-7ffee85c5556 | -1.44731 | -53.39577 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 024bc94d-1945-31b7-8ebf-2059440f4e48 | -1.62268 | -52.43333 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c574eea4-17ad-3c55-8980-c621fbbe59cc | -2.60161 | -46.24913 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f694767-8ad0-3a59-9157-37be47667f11 | -2.70181 | -46.28059 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d929a9dd-02c2-3200-8fa9-ce02d50e5614 | -2.66095 | -46.15562 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40fdac96-b80a-317e-91bb-c6a17e8eab30 | -2.69788 | -46.26016 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4433b779-1bfa-380d-9819-c2cc79c16f62 | -1.4467 | -53.39956 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c95a27a9-6d6b-35f6-91b4-b33f0a66ebfd | -1.60614 | -52.60622 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dd83acc0-a09c-3f61-a2cd-6a334a1fd378 | -1.50873 | -52.04225 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daab7fbf-b949-3393-9610-5a6ed7d3322c | -2.74867 | -46.00572 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b70e80fa-bb5c-3178-88f9-4125fc41eb48 | -2.51394 | -46.21553 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71900bf4-f835-3cc7-a1f6-fad5449bcdcc | -2.22303 | -46.40101 | 2024-11-23 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01b32c54-0e8f-36dd-bdc0-d32edaee3d1e | -1.19436 | -51.77044 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a239e568-f680-3f74-9a3f-ada5a719f338 | -2.37757 | -46.96002 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6085c0b7-0e8e-3379-a70e-f67f53cda02c | -0.25614 | -51.5761 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5db0cb75-0e50-31c2-b74e-61b4515a1a73 | -2.73266 | -46.08482 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 873b843b-f842-3769-991b-1486f5be72cb | -2.66504 | -46.15232 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e134d1be-c679-32eb-833e-ea0b90498c54 | -3.17462 | -46.54321 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04d79a86-2b4d-3710-9ae0-435ce5843a0e | -1.20181 | -51.97407 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcd6a14b-e237-363b-903b-19e53e576408 | -1.74471 | -52.37881 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cc60791-fd47-3f82-ac29-24c629bf0a60 | -1.7351 | -46.69206 | 2024-11-23 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ab1f9a4-d31d-385a-b9cb-7dc9d414a6e2 | -2.59917 | -46.26466 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e363b815-7e37-3963-bd9c-5b1d9a768449 | -2.70088 | -46.0837 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b14510e-85e8-3343-b3a9-51e34972bad8 | -1.43176 | -53.38512 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| febd6b6f-d3a8-3ed7-811a-46350507aa87 | -3.20219 | -42.90551 | 2024-11-23 04:16:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df46e06e-a338-3796-a124-52e6621cbbad | -3.14693 | -45.92437 | 2024-11-23 04:16:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1984548e-4fb0-3a70-a7ee-3603b4c06dfe | -2.64104 | -46.23522 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6016daee-27cf-3684-b04e-284d2b2f6b03 | -1.22908 | -51.74112 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7866f321-db23-3604-a05d-d60ee424299d | -2.67242 | -46.24022 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c136800-4ef8-3324-9a51-f628b0000e2e | -0.23917 | -51.61883 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0e707e4-a06b-3c69-bcad-155acdf684a5 | -2.76438 | -48.60739 | 2024-11-23 04:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a31fb4d-e5ae-32e8-be26-cd541f1f9f91 | -1.9381 | -49.52866 | 2024-11-23 04:16:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7e57e72-3f02-3264-ba20-d7e28e6080a5 | -2.20353 | -46.686 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccb13e57-70db-3110-ad02-1e614c00724d | -2.6628 | -46.14408 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ef09fd7-4791-3aee-8cc0-1200cb94d276 | -3.10182 | -45.98613 | 2024-11-23 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afe422e6-e555-3949-a038-3e4dcf423737 | -1.60052 | -52.59963 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d1aff42c-113b-3d87-bc74-0a390d175fe2 | -1.19185 | -51.93843 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07fcd616-a3a7-3b26-bff9-dba79cc442ac | -1.1246 | -53.40283 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b355e1d1-d449-35b6-954e-7a13c75797af | -2.23559 | -48.26947 | 2024-11-23 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af4eac21-9330-3a71-9e8c-c391556c7ccb | -2.25239 | -48.99715 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bfb0182-8220-3f80-8970-cc8c2dec760f | -1.28447 | -52.26173 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bd5ed6e-a40f-318c-8dad-f8eeb2e7b9d1 | -1.13936 | -53.40196 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 803cdce6-ca56-3c78-8283-cc3ec97f8364 | -2.61298 | -46.19958 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af8a01cf-a703-3aff-a2c0-92fb8bf56f8b | -2.55171 | -46.54325 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d3372a5-7726-32a5-95b5-4a71593ae99c | -1.19087 | -51.94446 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7437a32e-ebe6-3c39-8acc-3941bce5a3be | -2.44378 | -46.53948 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f030a47-b871-3798-a5df-0bb6c83a6c48 | -1.62921 | -53.31484 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15cb324b-ec40-3086-801c-315f750e5a49 | -2.41779 | -46.03654 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96fd9a4a-bb7c-3fda-865a-5016f7d8956d | -1.63879 | -52.09811 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffc75be2-f9d8-347f-ae70-2ad6f858b2a9 | -2.87659 | -45.25895 | 2024-11-23 04:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 894aaf54-a127-3abe-982a-d10d21b78930 | -2.69309 | -46.20007 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 473c7031-7b9e-3131-9053-8a3db1911d92 | -2.70332 | -45.97934 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 179e6443-65dd-31ee-9500-edbdcd1b8230 | -2.6994 | -46.04842 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e281b3d0-1a94-3c93-8a43-63c8cb5130c7 | -2.54816 | -46.54269 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdb2e545-d9cf-336e-b6ce-9faaaa750c7e | -1.78018 | -53.63268 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 079b867e-8a81-3fb8-bbd3-cf3adad61b65 | -2.59557 | -46.19679 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fd34c10-636c-3426-97d9-aeec12a3d5a0 | -1.73724 | -52.72108 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14fadf3f-18c4-317a-abdf-9c44ad088ae6 | -2.61724 | -46.26362 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 843869cf-e989-3300-b497-c5a30f6963d1 | -2.66073 | -46.2463 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dac41c0-a231-36da-a8a1-07e036dc45bc | -0.41586 | -51.59985 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 746d16cd-07dd-3e0e-b322-574dc4d925f0 | -1.67528 | -53.20637 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf7810b0-0a61-3d4e-ba20-0f083eea835f | -1.04967 | -51.7421 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cfded64-b77f-3aaa-958b-413b0a965a53 | -1.60528 | -52.6038 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ec97498-cdb6-36ab-b9ec-b64b3220687d | -1.27825 | -54.53907 | 2024-11-23 04:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6805008e-bc01-33dc-a485-7d889262283e | -2.55754 | -46.55231 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 138b874c-d55f-3aef-ba3d-bb9887aa8525 | -1.7019 | -46.23838 | 2024-11-23 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d0607e8-39b2-3230-a3e2-177185238bc1 | -0.93594 | -52.42309 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 098a28af-b9c2-3db8-9e07-efa83261d2ee | 1.37339 | -55.94385 | 2024-11-23 04:16:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3d871ec-4cef-31c8-a08c-ceeffb8f7f49 | -2.64118 | -46.57316 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8abe4496-b415-33fe-92e4-ef31cddbf707 | -2.57107 | -46.55857 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7911c9a-4fe0-3709-9d6d-0413fa205495 | -3.26647 | -45.13008 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README29.md)
