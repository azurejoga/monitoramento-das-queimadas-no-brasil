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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7ccdb63-1193-35db-bda8-9ec593d7c849 | -12.3208 | -47.2389 | 2025-10-14 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 8abb61f7-8195-38ac-a4a4-894a03c61ab3 | -11.4197 | -44.0496 | 2025-10-14 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4c964a2f-65e9-37a7-b8c4-a380cc717338 | -11.6839 | -44.2673 | 2025-10-14 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 72fd08e0-26a5-316d-a6da-dddfd9a89b50 | 1.7667 | -55.8031 | 2025-10-14 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4c917ac5-dc3e-39ca-aab3-1fae7eb32a18 | -12.938 | -47.0597 | 2025-10-14 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 835ed57e-27f6-34a8-8186-cb824c8ed112 | -4.6511 | -43.1104 | 2025-10-14 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 279.9 |
| 0a43e7ce-dd85-3381-a4fe-d0cb66da6c53 | -12.3592 | -47.2335 | 2025-10-14 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 04560316-dff4-3c86-b6ef-f7753a083826 | -10.1551 | -46.8919 | 2025-10-14 14:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| b32900d9-3e7a-3fad-9ede-55712032348a | -13.0747 | -46.949 | 2025-10-14 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 171.9 |
| b03c5ea4-9d1d-3e16-a3ca-c8d268a636bd | -13.6886 | -43.34 | 2025-10-14 14:00:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 3c5950d5-e1a1-3dc8-beef-b00fe7f7a1b0 | 1.7667 | -55.7833 | 2025-10-14 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 6cf72ccd-a690-3d84-94d4-60552bb802a9 | 1.8768 | -55.7029 | 2025-10-14 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 15cd127b-de12-3fb1-b83f-977770c50e3e | -13.0936 | -46.9688 | 2025-10-14 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| ecc7908e-08ed-3b73-ae9f-b54cdcd70aab | -11.525 | -43.516 | 2025-10-14 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 265.8 |
| 75700797-9959-3da6-bf49-6f84b35e7a88 | 1.8768 | -55.6832 | 2025-10-14 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f91bcb71-6479-3aff-ba11-9822f0032a9e | -12.9188 | -47.0626 | 2025-10-14 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 2b3a4146-1d6e-33b3-b3ab-c015a36fb66e | -12.34 | -47.2362 | 2025-10-14 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| c3e1485e-24a4-34f8-a4b7-c0d3b848627d | -12.9192 | -47.04 | 2025-10-14 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 1c912a84-ed45-3e89-b5b8-ccab5feb5451 | -11.8005 | -46.3433 | 2025-10-14 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 86604ba7-7654-3a07-9ac6-a77d4ac84433 | -12.3208 | -47.2389 | 2025-10-14 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 7681077c-57ee-3cbe-bbce-b237356906f4 | -13.094 | -46.9461 | 2025-10-14 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 210.9 |
| 7ecde038-00b0-39e6-9ae2-47c6e1cebaa5 | -5.4187 | -40.9841 | 2025-10-14 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 139.1 |
| 378e342b-2ddb-34d5-8f98-e9b04788cc68 | 1.8768 | -55.7029 | 2025-10-14 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 39734028-7db9-3856-9db4-dd8dfe8e0352 | 1.8768 | -55.7227 | 2025-10-14 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 6098e5f4-e969-338f-8cef-a1e582c26b8c | -13.094 | -46.9461 | 2025-10-14 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 0d97230a-fdaf-3da4-9445-9941375a87e2 | 1.4451 | -50.8488 | 2025-10-14 14:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f272913c-6636-3ba0-a90b-f378f4d9761b | 2.2245 | -55.8949 | 2025-10-14 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 47040093-f907-3008-b021-4a93bcd17f2f | -12.3592 | -47.2335 | 2025-10-14 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 7fef2b84-1d4e-33a1-a4ff-72d672399bcf | -12.0118 | -45.2161 | 2025-10-14 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 3ad3aaaf-08a2-3d2d-9912-1d450dae9d98 | -4.6881 | -43.1547 | 2025-10-14 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 12bba2f3-89d1-3db9-8395-7926391e8b87 | 1.7667 | -55.7833 | 2025-10-14 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 167.1 |
| abecd99c-891e-3d9a-8646-5f20f2bd8e67 | -4.9715 | -42.8082 | 2025-10-14 14:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 01472b32-90e4-3978-97bd-ef69f36cf90e | -4.6698 | -43.1092 | 2025-10-14 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 304.2 |
| b4e28dd1-18d6-39e7-81c0-a3b8e23149fd | -13.0747 | -46.949 | 2025-10-14 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 8d5e37ae-0ccb-3e7e-b7e1-122850124c2b | -12.9188 | -47.0626 | 2025-10-14 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 78555c7a-39b6-3815-b635-ae482d5a54bb | -12.9192 | -47.04 | 2025-10-14 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 9165208c-339e-3fc6-a0b2-b2a2a2c9b809 | -12.34 | -47.2362 | 2025-10-14 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| c3129f46-c8cd-3dfa-9acb-d260a77d8509 | -12.938 | -47.0597 | 2025-10-14 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c51105c5-586b-3878-8cc6-89db3a328fc9 | 1.7483 | -55.823 | 2025-10-14 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ba5f401c-e3be-3605-9403-97e65ef1e493 | -11.7219 | -44.285 | 2025-10-14 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| d2362d84-0aee-3bb3-ba02-b7d024ce1161 | -4.6511 | -43.1104 | 2025-10-14 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 384.1 |
| eb382f6c-f156-3d38-9c17-7bfb6c259fbe | -12.8995 | -47.0655 | 2025-10-14 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f50357b3-c08f-3b0c-ade1-93de5aa6bf19 | 1.8768 | -55.6832 | 2025-10-14 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8a0279fb-e07d-3ebd-b414-9ef526a45ce4 | -4.6509 | -43.1337 | 2025-10-14 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 838.9 |
| b2d7ae66-5b83-398c-bd30-cac0122edaf2 | 1.7851 | -55.7831 | 2025-10-14 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6cc2b7f0-906d-3f23-99b0-a8dbce42cc9e | -12.3208 | -47.2389 | 2025-10-14 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| b826648d-de73-309b-bbf1-fedc7edc57d8 | -11.8005 | -46.3433 | 2025-10-14 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c66615e2-a25f-3d9e-99e6-a1bd79bdf18b | -5.4187 | -40.9841 | 2025-10-14 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| 09bf8095-47e0-3eae-9534-6a126fcc63df | -5.4187 | -40.9841 | 2025-10-14 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| 35732d21-c6f7-373a-ac84-88a547ddcd14 | -10.1524 | -44.552 | 2025-10-14 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 7438fd78-1cb1-301c-9800-116fd1eea58c | -13.1129 | -46.9658 | 2025-10-14 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 15422e6c-f36c-30fc-8702-0893a1b5f18f | 1.8768 | -55.6832 | 2025-10-14 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| e4e5d8ef-c9e7-32c2-a23d-b85ec93ed57e | -6.4448 | -41.8368 | 2025-10-14 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 196.1 |
| af1dfc7b-258d-378d-a898-89d8f0622418 | -12.938 | -47.0597 | 2025-10-14 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 4ef57128-a76e-32af-bbd2-86e5516f00b4 | -4.6509 | -43.1337 | 2025-10-14 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1326.0 |
| d7724aaf-5799-32d5-bbfd-ea5fb86b4c85 | 1.8768 | -55.7029 | 2025-10-14 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8be896ef-c496-3cd2-85d6-5d1acb2c0188 | -4.6698 | -43.1092 | 2025-10-14 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 273.2 |
| 5394d5fa-2438-335f-91c0-ed9d45fac48b | 1.8952 | -55.6829 | 2025-10-14 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 1d94c1f8-21db-3158-b293-b0d204b4c710 | -4.6511 | -43.1104 | 2025-10-14 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 435.7 |
| 451ec8ef-365e-3717-9676-7eebcc1d086b | -6.0786 | -44.6733 | 2025-10-14 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| da3b3d82-c1f6-356c-be14-1b23d8db2b5f | -12.3592 | -47.2335 | 2025-10-14 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 57d6b738-23cf-3063-8309-0dbaaedd1b5d | -12.3208 | -47.2389 | 2025-10-14 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 901f9309-6fcf-3733-b9be-187013b53473 | -12.34 | -47.2362 | 2025-10-14 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| f91e1399-b40c-3b3d-a1e1-eddc729f709a | 1.8768 | -55.7227 | 2025-10-14 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 88d2eea9-2b21-3910-874f-ac38bb49ac28 | -4.6881 | -43.1547 | 2025-10-14 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 879364f7-22c4-32b7-a563-e5f426a8b970 | 1.7667 | -55.7833 | 2025-10-14 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| bb8e7a35-e4b0-3724-8987-0356bd028195 | -3.7629 | -41.6728 | 2025-10-14 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 1108f946-55d0-3e75-8eae-a292d132ca3d | -12.9385 | -47.0372 | 2025-10-14 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a7cb497d-166f-33bb-a7a2-a43e3861dc56 | -5.8705 | -42.8828 | 2025-10-14 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 159.3 |
| c4b481d3-b1cc-3b1f-abdf-e664431f3730 | -4.6694 | -43.1559 | 2025-10-14 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 477.1 |
| 69fa5c9e-965e-3b8c-82fe-a09023e73282 | -5.9562 | -43.7396 | 2025-10-14 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| f98e18ac-c4e0-3fbb-a1da-6bd5cf5e71cb | -12.9192 | -47.04 | 2025-10-14 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c85a0058-1d14-3ec8-b692-bf523f37213c | 1.7851 | -55.7831 | 2025-10-14 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bc052dea-3011-34f6-8b6a-dcc9a72d6100 | -3.3812 | -43.039 | 2025-10-14 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a6035eea-a0fe-3bea-9874-4c6038b8d6ee | -4.856 | -43.214 | 2025-10-14 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| ae743543-2176-3992-a7e7-a540ef6829b8 | 1.1135 | -50.9984 | 2025-10-14 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e9036db1-89d1-3137-b831-3c1a98758b0e | -13.1133 | -46.9432 | 2025-10-14 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 6c2c5304-f7d1-3a54-add7-476b9a5ef462 | -12.8995 | -47.0655 | 2025-10-14 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 265fdc5b-5235-3adc-9118-4841ddef01a8 | 1.7483 | -55.823 | 2025-10-14 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| c9d02bdb-6e0e-3831-b40e-0c03ae311e31 | -5.8705 | -42.8828 | 2025-10-14 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 168.7 |
| 095679c4-57fc-338a-8692-c8589046ba59 | -4.6509 | -43.1337 | 2025-10-14 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1519.8 |
| f980489b-b87d-3675-9353-eb7ff6daecf7 | 1.8768 | -55.7029 | 2025-10-14 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 9e074a82-d46f-397f-8754-d58edd34954e | 1.8768 | -55.6832 | 2025-10-14 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| a808fd9c-d43d-3001-a574-9913af728c70 | 1.8952 | -55.6829 | 2025-10-14 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9ee81826-b320-3af1-96be-57e0a928a4d8 | 1.7851 | -55.7831 | 2025-10-14 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| af92c855-0c48-3495-a91a-515a8b855e2e | -6.0786 | -44.6733 | 2025-10-14 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| f4e535f1-fb09-3e43-b568-8539b56172f3 | 1.8768 | -55.7227 | 2025-10-14 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| f76dc925-42f4-3229-b7cc-8effdefd0325 | -6.426 | -41.8385 | 2025-10-14 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 157.5 |
| c0c5496a-9105-3ac3-9a65-3cb03a898d8e | 1.7667 | -55.8031 | 2025-10-14 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 36ccafaf-6b1d-3394-acfc-a005582bd711 | -6.4448 | -41.8368 | 2025-10-14 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 250.3 |
| a899d15e-2100-38be-88cf-03b8dfe19a4c | -5.2678 | -43.2093 | 2025-10-14 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| f4b2d111-2ffe-3368-9fd9-416193a9e905 | -6.2104 | -42.6898 | 2025-10-14 14:40:00 | GOES-19 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 68542d1e-4404-3cbd-84b9-08a807368558 | 1.7667 | -55.7833 | 2025-10-14 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 28d5c6ac-110a-3a0a-8657-dd0612cd47e5 | -4.6881 | -43.1547 | 2025-10-14 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| dc09f09d-01c6-374c-8c64-037c085335e5 | -4.6511 | -43.1104 | 2025-10-14 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 512.7 |
| 6e404fa3-fd79-357b-9bea-29e7f7b85be9 | 1.7483 | -55.823 | 2025-10-14 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |


