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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98ac09e0-4d41-357e-a6c6-3b6cbe66f2b4 | -5.86629 | -52.03249 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8b54df5-72e1-34ce-b532-f1a92e6b9ba5 | -13.06589 | -47.39487 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8ea4cec-2996-3422-beaa-24c0d03ae891 | -11.39501 | -51.3828 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41425898-ba02-3bc8-b78d-4a8bd96309b0 | -13.89095 | -47.97921 | 2026-09-20 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ab8a269-68d5-3383-9579-b6945215dedd | -10.27338 | -50.25652 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c3d8000c-7f96-3c23-b102-4d5377f75c58 | -10.31454 | -50.22599 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e46fa05-0943-376f-8e3c-ffdc1cb08c40 | -5.90229 | -52.09318 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8472dadf-9007-3e6a-863d-9b71ba271a68 | -5.87133 | -52.0445 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1424fd60-21fa-30c2-8302-005507ae3db5 | -8.47879 | -46.86352 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e897f50-c52e-3ac2-981c-88cbd06a901f | -8.17441 | -54.76916 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 094d4944-1d8d-39ea-b841-cc8976e2ea9b | -10.41064 | -48.90901 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5eea6f7e-baca-318a-9d18-4b14c189bbf2 | -11.71025 | -54.56649 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db90abdc-21bd-3ce5-a46f-8367c6dd5f1b | -9.28099 | -44.39519 | 2026-09-20 04:40:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ee32f3c-e509-3fbc-a343-011e4dfdc5a9 | -13.24716 | -51.74507 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a55e56d-abed-3164-9665-427ea2655f15 | -9.22866 | -46.23686 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 373f1430-ceac-3556-8129-4aba31216803 | -7.62662 | -46.12057 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d74f1829-c9fa-3e80-b7f3-e603cabb867f | -11.45478 | -45.70653 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c8e6d33-cd9a-3795-b3fe-6b0b1417dede | -11.38339 | -51.38869 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8ab619d-efba-3cc3-9c0b-09853239ce7d | -9.27606 | -48.24351 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c904e5f9-5f56-305c-b9f9-cd67556824d8 | -11.72906 | -54.55483 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9390f9c7-9d46-33f2-824b-4e4f2b0ddda8 | -8.42021 | -54.7319 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b75c62c-8442-3587-888a-69505f86597c | -10.325 | -48.00141 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96c18c06-43f6-32c6-bd47-98bc4a4c5fce | -5.8423 | -53.54147 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60fd7dbc-cbdc-33fd-a425-bf6d2847050f | -6.66201 | -50.89501 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e863d63d-64f1-35eb-b3be-e89079c6ba30 | -6.75587 | -47.92161 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ed839f8-b7a7-30dd-9c34-4ac22d4c2cd5 | -6.94588 | -46.96877 | 2026-09-20 04:40:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b35481c-b5db-3bac-a9fc-815dc364992e | -8.22114 | -45.60849 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5be2c20e-524f-38fe-8199-7e0c879a7240 | -6.45281 | -48.44044 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ae62be0-2604-3029-9646-03934668308b | -11.37712 | -51.38368 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fdfd3ff-1425-398b-913f-46d1e011fc00 | -11.31717 | -47.27779 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e25c6e3-0bf3-38ab-ae9d-c4bb6c6e6de3 | -9.70659 | -45.86777 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc0a8949-f85a-3e42-bb22-b5d19cdb98bc | -13.61257 | -46.97096 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d271aa1d-4937-3f66-b791-13b57cdd406f | -10.45944 | -45.08307 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f992487-763a-3b62-a75c-f18ab2149c2e | -8.61041 | -47.30665 | 2026-09-20 04:40:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7c0defc-9235-30fa-b11b-cf9eb61bac9f | -11.07452 | -49.49745 | 2026-09-20 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b19a9b4b-441d-3849-afad-f5dfeb73065e | -11.45035 | -45.38445 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31ceaa28-da49-32c1-ac12-f23fbe8689ab | -13.31554 | -51.29115 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3707cbc-9148-33a3-9f3f-f059b0407f39 | -11.21801 | -54.08355 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d358b5e8-43ff-3abb-948f-94a0ed102624 | -8.1693 | -54.77266 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d51534ce-678b-34f6-a347-4bb51d9c27e7 | -7.6252 | -46.76728 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44465c93-ec9c-33f5-98a4-09e7c068f769 | -11.0318 | -48.30589 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 145c806f-dbf1-3a5f-a29a-4d842e557c0b | -10.30588 | -50.25793 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b954443-462b-3fc6-9d05-a8092c33d48f | -5.78102 | -57.58317 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfdca2fd-a9de-3e97-bb9b-75f31581bc8e | -12.80903 | -54.05988 | 2026-09-20 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8636310-3369-395b-92de-f393a3ee11ac | -11.03704 | -54.15831 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 586c215f-34b1-3b86-9441-a781bfa9d034 | -11.03148 | -54.14267 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b41563fc-55b4-3085-a950-1f3ca562cc64 | -9.93919 | -53.98394 | 2026-09-20 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32af94b8-b702-3e87-b660-bf0b94232d6f | -10.7823 | -50.8824 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 153eae57-5334-33a2-93c5-9e70a455fbb4 | -11.21892 | -54.07834 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88c881c9-6138-333f-bee9-74bfe51e441d | -6.81206 | -47.88791 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0795368b-d5f4-363b-b475-738c6d292931 | -8.54 | -54.69129 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 621767a9-cba5-379b-a74b-dd8970545635 | -7.87926 | -44.86815 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f40a21e3-a21e-31a8-a66d-486eb06e70ec | -9.93857 | -53.98751 | 2026-09-20 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30d86b94-27c6-3bba-a9c9-8de36dae4f3c | -8.32879 | -50.94571 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65cfedc0-196e-3dca-ae5c-290d0ef2a9fc | -11.23391 | -54.08641 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b1e9af6-7e49-3f79-a0d3-cd0b9bd8653c | -13.62217 | -48.29551 | 2026-09-20 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69994d29-34d4-33a8-a59d-88392752e87a | -9.67484 | -54.32833 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1d3c601-681d-35c5-8b53-8dbae91e3765 | -11.44273 | -45.33194 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f899c69b-4199-3eb9-8b53-89e300a457d9 | -9.79066 | -45.05376 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 462ee06d-6923-38bb-ad16-0354f98ce47f | -5.86579 | -53.52977 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42927c51-711d-3a96-a3b6-f81b5196acb4 | -5.85503 | -52.07155 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 639f0de2-f7a0-3b91-b118-726c57286ee2 | -13.2478 | -51.74125 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de374147-9c60-38bd-968f-44ab546e6946 | -11.32118 | -44.17895 | 2026-09-20 04:40:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2926c18a-1767-3dae-8ff4-c57e93e428f3 | -13.06192 | -47.3978 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59c44efb-bce5-35f9-98a4-1ea872c4874f | -9.04338 | -48.77038 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e597f88f-7eb1-36f4-bc55-2eb33c9cf2bb | -7.7477 | -46.76753 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 757b45e5-c433-34fa-b771-88ab9d081a7b | -11.22777 | -54.07462 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e39643f4-5a96-3ac2-92e3-10c8d18a3b78 | -11.87217 | -49.008 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3add630-fe27-39b3-8edb-6a0b0b3996ce | -10.78414 | -50.87122 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2d8a3207-4042-3350-9676-109bd9a50b91 | -12.56637 | -49.10615 | 2026-09-20 04:40:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e4c9246-3032-3dd3-917e-692975dd823a | -11.43314 | -45.42379 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c41af2e-9623-3bd1-8ecd-fbc7772298fc | -9.26543 | -46.20676 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f889e13-3982-3c9e-b1a4-1136c0d4f242 | -6.77286 | -47.8569 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c2a906c-60db-3df6-89dd-4c7529b6d0c2 | -11.37268 | -51.41062 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 778e0f58-033c-3496-a1c0-21acb770f8c3 | -9.79302 | -45.06338 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5abde57e-e4a3-3018-a251-dfab6c2ba085 | -13.19721 | -51.75266 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e5d6aa3-b02e-3860-a67d-6d0657a06d54 | -10.2728 | -50.26013 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e3745366-3119-342f-a0f8-52dedc76153b | -9.13025 | -45.71667 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02117f75-0816-395e-aba6-a8d1e216982e | -11.45579 | -45.3993 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee2982cc-4891-37ec-be65-e3b900b01582 | -8.79262 | -60.79612 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 95a0fc32-bb68-3c51-9c89-53679d5d8480 | -9.12668 | -45.7161 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6610d081-3d67-3672-8a98-8920698cef24 | -11.00233 | -46.57799 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce559d92-00fa-344e-a81f-acdc4b744dc7 | -7.59637 | -46.72924 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74a0aa01-6644-324a-99be-2b5781c48fec | -8.76624 | -48.71901 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37bc03c7-c2b4-3a76-9198-e6070b2b4bfc | -11.95641 | -50.09959 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89d65d89-7db5-356a-b3b8-f939fae4e97e | -10.87052 | -54.08795 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dbdea76a-77ed-3dba-b031-94d12de37392 | -8.78829 | -48.70829 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4c493a4-539b-3860-9532-eff15002cb7f | -12.65479 | -49.47137 | 2026-09-20 04:40:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d72b1e91-496c-3c30-a793-d4f9c85c2d86 | -7.45165 | -44.73687 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f00eff1f-32f5-3b7e-a876-6767b4c3e864 | -5.83842 | -53.53384 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56a9061c-b02e-3dab-bd8d-ce93332cb594 | -12.65092 | -49.47436 | 2026-09-20 04:40:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 158a228e-d1f6-3f1b-953d-b0605817da2e | -11.21403 | -54.08286 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c4a7e051-92e4-39a6-8e4b-1aa371f2ef5c | -9.21586 | -46.22686 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adfc4afd-6d2b-3b76-b9c7-8959b63ae109 | -12.12015 | -47.02848 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0d1db57-2a15-36f5-806d-6dddda23c78b | -13.9496 | -47.84441 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb2c56a8-bc80-37be-99d4-ad4ba4447f4a | -11.04503 | -54.15986 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2be07c03-06a0-3081-a468-1eb5465c67cb | -8.73088 | -44.87448 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c190a50d-7dfc-3f06-8703-964f6fa3ed15 | -7.11262 | -48.41465 | 2026-09-20 04:40:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 612031df-8f8f-3d18-9675-8baae200476b | -9.05386 | -48.72567 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8faadec6-8bb4-3bb0-ab06-bc262eb28fca | -12.73956 | -46.18467 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README79.md)
