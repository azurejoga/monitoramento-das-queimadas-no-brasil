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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6ccfe99-04f9-37eb-b33d-75b61747d8b2 | -1.82575 | -50.90924 | 2024-12-01 05:25:00 | AQUA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cbb4282e-6d5d-3d77-b8c9-05c0ca846d0a | -3.26366 | -53.64373 | 2024-12-01 05:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 8df85d83-f2ab-35ce-be53-42b923552a59 | -4.55378 | -43.295 | 2024-12-01 05:25:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| d7a9aff4-3fab-3b26-9099-170ff67796d7 | -2.90217 | -51.57694 | 2024-12-01 05:25:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7df6b521-cafe-3c39-ab12-022f6666b8da | -4.89525 | -41.32037 | 2024-12-01 05:25:00 | AQUA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 0c9171a8-893d-36e7-8e72-36f249866f5f | -3.25995 | -50.04948 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e69004cd-1156-35c8-837d-21a781796b0c | -6.18932 | -44.42118 | 2024-12-01 05:25:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 44d6bbec-515c-37b0-87b6-cd7531f19d16 | -3.48286 | -50.3169 | 2024-12-01 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 218b5b49-1ed0-393d-abda-284e772af53d | -3.14974 | -45.3668 | 2024-12-01 05:25:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 2e3694df-58ec-3181-938f-fbda05f80a59 | -4.4083 | -48.58592 | 2024-12-01 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 44ba0ce7-fc3b-3d9f-9ea7-2c3939d3ed25 | -1.28083 | -47.90415 | 2024-12-01 05:25:00 | AQUA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2f2c1cf4-9682-391d-b755-e63b15e55dbb | -5.42224 | -45.10849 | 2024-12-01 05:25:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 114e17e1-a5f0-3f33-b697-4e722522be94 | -2.66074 | -51.87465 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 26b2f2c6-db55-30e9-a862-fad89d3b723e | -3.05908 | -51.05765 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 622af12e-e8ac-35e0-9f78-22f8cc4b454b | -3.85128 | -40.98515 | 2024-12-01 05:25:00 | AQUA_M-M | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| a0a23cf1-b397-3852-a854-090489721b85 | -2.9914 | -45.5705 | 2024-12-01 05:25:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 5e349756-4049-337d-b5b8-aff84fc4921f | -3.5384 | -50.39862 | 2024-12-01 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4cf9350e-3502-3b8a-9b82-0b031a562e8f | -4.09489 | -44.85038 | 2024-12-01 05:25:00 | AQUA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5730e1e4-7570-3548-8db2-6c8a251c3cdc | -3.30646 | -53.84985 | 2024-12-01 05:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| de815b8b-8c1d-34de-a7b6-a35dde9c7e4d | -3.92272 | -45.07657 | 2024-12-01 05:25:00 | AQUA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f673800b-3900-3195-916d-66fd21ae9437 | -4.04141 | -46.92963 | 2024-12-01 05:25:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a2272cfa-c4d7-301f-8658-0e273f5f6df5 | -4.53175 | -45.70343 | 2024-12-01 05:25:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7daaa7e3-bc65-3be8-8920-12f9eab416d5 | -3.53949 | -50.40435 | 2024-12-01 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 018254ed-a724-30ca-b1d6-51fe5a83026e | -3.68332 | -51.81472 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 228dc067-2b97-3d8f-a073-2d9c54b3a75b | -3.85175 | -46.54008 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 398f0208-dcff-3810-8609-1a6a0f89d572 | -3.99773 | -44.75653 | 2024-12-01 05:25:00 | AQUA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| aff76d7a-b8a4-344e-b900-85772d3b7749 | -3.4674 | -50.26439 | 2024-12-01 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| c94550c4-2104-3bee-b10c-0440a12c89f1 | -3.26931 | -50.20743 | 2024-12-01 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 0021afac-16fc-327e-86ce-309498cbffd1 | -3.99908 | -44.74745 | 2024-12-01 05:25:00 | AQUA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 2cbac6ce-2ad9-339a-9d84-d85ffc9dbb05 | -4.54414 | -43.29364 | 2024-12-01 05:25:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 56be8d78-97d1-3717-87aa-fa8298ff0ef0 | -4.39871 | -49.77314 | 2024-12-01 05:25:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7fb0033d-4d9a-34f6-ad78-1e646383cf80 | -3.13266 | -45.98035 | 2024-12-01 05:25:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 34dd2ce0-2a40-379a-826e-9cc5eb5a136d | 0.94558 | -50.74246 | 2024-12-01 05:25:00 | AQUA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c7a9b7cb-1c19-30a1-b668-6bee9135d451 | -2.62935 | -46.19216 | 2024-12-01 05:25:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 910fc295-2672-3cf0-9504-ea77463a1bf6 | 0.99228 | -50.24238 | 2024-12-01 05:25:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2859f131-d7b2-3b5d-8f63-4e04c73838bb | -3.69276 | -51.81134 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| f91f8087-cc26-3afb-8db9-8bafb19d44f4 | -2.64798 | -51.87283 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3df8408b-3921-3d7a-8618-93b1c0656768 | -3.15105 | -45.358 | 2024-12-01 05:25:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 46faa136-4590-3d42-9ee8-e8b21666dbc1 | -2.10018 | -47.62347 | 2024-12-01 05:25:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 22a7263d-7a1b-32b2-bb0b-8e29fd9fa9ce | -2.28342 | -45.60581 | 2024-12-01 05:25:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 11dc386f-4dd4-3258-9355-d54fe90625f8 | -3.14842 | -45.37559 | 2024-12-01 05:25:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 73ea7e10-3197-31d9-84fa-cce88a814f0c | -3.85311 | -46.53115 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bc564230-2648-3089-87d1-6fd79cff3067 | -2.74653 | -51.73788 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 0ca6e2b1-3038-3179-bfbe-f5fd84dd23c0 | -4.55562 | -45.7249 | 2024-12-01 05:25:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 810770ec-714e-3e43-b827-1bf4f7efe77f | -6.28762 | -43.84818 | 2024-12-01 05:25:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7849679a-e3af-3e64-8e33-84a8e4061213 | -3.12836 | -54.50057 | 2024-12-01 05:25:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 67114e0e-7047-322f-a391-63105fb1af0b | -2.47206 | -46.56527 | 2024-12-01 05:25:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 40ef70ea-c370-328a-9d85-044cd9fc34a9 | -4.03244 | -46.92836 | 2024-12-01 05:25:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f8224ec4-18b3-3d13-a182-693828e31d31 | -4.17955 | -48.61532 | 2024-12-01 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 1550a39e-3e62-35b1-a641-8e8194b21b8e | -3.50654 | -53.83892 | 2024-12-01 05:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| fde5e0f6-a5a1-32ac-a2a9-5b91bc19088f | -4.31937 | -48.08686 | 2024-12-01 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 09059d94-75d8-30ac-bc68-ba126c780936 | -2.98257 | -45.56921 | 2024-12-01 05:25:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| f5c06360-8bef-3b9e-bf3a-fbba2965b66a | -0.60208 | -51.69283 | 2024-12-01 05:25:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c4931e2a-2df9-3116-9326-9b0ceefd5f7c | -3.69565 | -51.8173 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 324b003e-55b8-34cf-894a-db863daa9e60 | -4.55693 | -45.71608 | 2024-12-01 05:25:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 0119e3d8-26bb-3756-9981-2b07c1809995 | -6.71595 | -47.26383 | 2024-12-01 05:25:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8225a325-9e73-34fb-be0d-7a361d5e2e9b | -3.81583 | -46.59195 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ffe79865-7d77-3387-b593-e8dd044a2aca | -3.13959 | -45.37431 | 2024-12-01 05:25:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 90495298-ced0-3cd4-bb72-1e2a75973620 | -3.7546 | -52.26556 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| bbe2a65a-e263-3f2b-b961-34fc057d2600 | -2.46173 | -46.57301 | 2024-12-01 05:25:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ef6df1ae-043e-3d46-a71a-96e965b29447 | -2.98126 | -45.57798 | 2024-12-01 05:25:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 529a09d7-52d5-3985-9b5b-e848b22227f4 | -4.31045 | -48.20901 | 2024-12-01 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 574823c6-e408-3b8a-9d26-5671aadfd7f9 | -3.06751 | -50.98071 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 39db533b-7db4-3140-a8a8-ad1de8e8eacd | -2.29225 | -45.60709 | 2024-12-01 05:25:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fc5603c5-4e43-30e8-8f85-1a1f54c5027c | -4.01247 | -46.99987 | 2024-12-01 05:25:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 04d45f3e-5584-3737-ad5a-986422cd8570 | -3.97713 | -46.74735 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cb8ed876-746c-35c3-a6ab-584bf0b859b9 | -2.65924 | -51.88174 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 9c379e12-4a9e-3f24-bd18-1e9720d1314c | -3.27146 | -50.19324 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 78e378f6-ed5c-3185-a189-a861f47c2340 | -1.82834 | -50.89246 | 2024-12-01 05:25:00 | AQUA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 093dd3ee-11a3-3e40-9222-5e7549464d0b | -3.82254 | -46.54728 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5634dfb-646c-3fa5-8f98-ce4601e5084c | -3.1415 | -45.98164 | 2024-12-01 05:25:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 23a09202-2df0-3085-9099-3c29c981f531 | -2.99008 | -45.57927 | 2024-12-01 05:25:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2a90ae6a-7e51-3205-ba0d-84f520313add | -3.25321 | -53.61573 | 2024-12-01 05:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| dbce8e7f-90f9-36c5-aaf0-8a7daa13fb80 | -1.32326 | -51.95586 | 2024-12-01 05:25:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| ab8b333a-a1b5-3dc1-ab00-5160c5e29ce7 | -2.80703 | -53.04712 | 2024-12-01 05:25:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| bf168bf2-1fd8-371a-ae6e-15cd1ea6636a | -3.85582 | -47.05808 | 2024-12-01 05:25:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 98e247bc-694d-3801-b165-8a5314348c21 | -4.26811 | -48.35986 | 2024-12-01 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cd6a7b5e-92b6-3703-b32e-078bf09f8f78 | -3.82472 | -46.59328 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 71cdfd04-3b45-3df3-91f4-86565368cfed | -3.79074 | -46.69814 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6e1a4377-fc86-341b-bb0a-d3e6e672818e | -3.05447 | -51.06245 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 25322b46-cd06-37d4-9290-c7e79edd94be | -2.65503 | -46.57684 | 2024-12-01 05:25:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bb4de416-0619-395d-95ab-b2206a4e5855 | -2.80624 | -45.9348 | 2024-12-01 05:25:00 | AQUA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 469fe60c-33aa-3d57-869c-d7c134ceadff | -1.71694 | -52.61438 | 2024-12-01 05:25:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f5d7a9c4-ce3d-39f7-a0b0-2c716e8f4e17 | -2.99735 | -51.06519 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| afd50953-6778-39af-b4fd-4b462de69930 | -2.71376 | -46.12872 | 2024-12-01 05:25:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8a6fc080-4b86-360e-88d6-1a751f4fc5a8 | -2.66231 | -51.86246 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 03fcacfa-5b45-357d-9fcf-bc1bec2e9e81 | -3.40762 | -51.96737 | 2024-12-01 05:25:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 91708674-3811-33d9-bf44-953a0df3a57e | -2.67779 | -46.60789 | 2024-12-01 05:25:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e51d9552-2e45-3c43-afe0-656c6dee68b4 | -2.12539 | -46.53583 | 2024-12-01 05:25:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 51bf703e-125c-336b-a015-1e95baf4860f | -3.13222 | -54.54066 | 2024-12-01 05:25:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| c52d12eb-865c-3786-b06f-0b163e147f51 | -3.12346 | -54.53154 | 2024-12-01 05:25:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| af0f4b5c-1696-32db-811f-d899bce3aeef | -3.11609 | -53.80123 | 2024-12-01 05:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 48beafc4-4a96-318d-b758-8b4d1373b91b | -3.69861 | -51.79875 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| b10f7100-b096-344f-b342-63bc51220c76 | -4.54058 | -45.7047 | 2024-12-01 05:25:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e753393-5c01-32c3-8250-4a751dcbfa10 | -10.65694 | -44.48181 | 2024-12-01 05:27:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 66c5fbe1-4307-3f39-8eed-35196f449900 | -10.65387 | -44.50364 | 2024-12-01 05:27:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47c23efa-4e9b-32e9-b969-0ef6958d256b | -10.6554 | -44.49274 | 2024-12-01 05:27:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 4796e9f4-ff2c-3fcc-b01f-8c4a26b239a3 | -10.66511 | -44.49409 | 2024-12-01 05:27:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 95ca5ea9-5652-3e1c-a267-457f1d1173ec | -10.66665 | -44.48316 | 2024-12-01 05:27:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a80b0740-9537-30d4-a36c-fdf098d92383 | -3.2774 | -53.6383 | 2024-12-01 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |


[Clique aqui para ver as próximas entradas](README99.md)
