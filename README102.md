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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1d71087-abc7-37b0-8c89-810f55a035b0 | -11.72035 | -59.28104 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3dea7ba-1387-32ef-b537-6de04c0d11b0 | -11.7198 | -59.28459 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce7364e9-4f7b-3b8e-9a5f-51c4dc97c49c | -11.71926 | -59.28815 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 926d4bef-65e5-377c-a462-dfebafb93be3 | -11.71871 | -59.29169 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ced415e3-ca71-3ede-a640-5772fc098447 | -11.71648 | -59.28406 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86262fb6-d2c9-33d0-b335-740d2f0faba7 | -11.71593 | -59.28761 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3021a90e-6537-32c4-83c6-7d7caf976b18 | -11.71424 | -59.27641 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1818cd9-76cb-3e8a-b655-eba57c2e10fa | -11.71702 | -59.2805 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30b571f0-38a7-32a4-8b39-3655d77d959b | -11.70378 | -59.30022 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8948d647-76ea-37e6-9ec5-9495c90bc45c | -11.701 | -59.29616 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb8ef0dd-baf1-3bf2-9a13-b47c3a4922ce | -13.15324 | -60.41608 | 2024-10-11 05:21:00 | NOAA-21 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d26722aa-8d25-3f5e-83f8-4a3f687011e0 | -13.15269 | -60.41959 | 2024-10-11 05:21:00 | NOAA-21 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fd26483-ae1f-3bb3-9ca2-e39c20769aeb | -15.22906 | -59.59996 | 2024-10-11 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e8b55b6-f668-36d8-9c1b-4a11b3ffe1de | -13.74662 | -60.59974 | 2024-10-11 05:21:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 708dccb1-1194-3eb6-9536-0868ab0f25a3 | -13.74332 | -60.5992 | 2024-10-11 05:21:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89fe062f-33a8-3129-9811-695551f5202e | -14.86603 | -59.86821 | 2024-10-11 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6775c123-fe94-3abc-995b-7819bb81f4d4 | -14.38325 | -59.89448 | 2024-10-11 05:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfbbdc9b-5581-3749-9da5-ff79fb105311 | -14.37992 | -59.89394 | 2024-10-11 05:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 082494c8-e185-3fea-8c27-12163bd6e13b | -14.18607 | -60.2474 | 2024-10-11 05:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d7044c2-8798-3df8-8c4c-fa40b69b6bd2 | -14.18276 | -60.24686 | 2024-10-11 05:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a1d8ccf-ca6e-33f0-ad3c-f5a7027c3c2c | -15.96266 | -59.75663 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1f3da02-5548-361f-9c6f-3dadedebaa92 | -15.96211 | -59.76033 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54db9769-a4b9-37ce-8b25-7f5abeb8e807 | -15.43595 | -60.01082 | 2024-10-11 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 505a42a4-6f99-3496-96b5-4dfeab64c676 | -15.4354 | -60.01445 | 2024-10-11 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 943e8611-fded-3803-883f-c61ac3638845 | -15.43262 | -60.01028 | 2024-10-11 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74916889-cf12-32bc-ae10-ba28ef0f1518 | -15.43206 | -60.01392 | 2024-10-11 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09fdfc49-1c1a-318a-86ec-bb51125e1fbd | -15.42928 | -60.00974 | 2024-10-11 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ca83f63-c977-35d2-8ad6-99b008e4a7f2 | -15.38745 | -59.81683 | 2024-10-11 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 05d9ee1f-57e6-32e7-a99a-baafa7d4ea23 | 3.38496 | -51.33792 | 2024-10-11 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e315b572-0090-3a7e-9b18-ca66041b9152 | 1.97139 | -60.91553 | 2024-10-11 05:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 026d5d4e-39b4-33e6-8f55-24df621989c0 | 1.97058 | -60.91456 | 2024-10-11 05:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f029bf76-fd4b-3a6d-82d2-86e221e9e021 | -5.76831 | -65.94749 | 2024-10-11 05:40:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cd15bac-bdba-3813-9a16-12a84e5223a5 | -2.62345 | -66.35571 | 2024-10-11 05:40:00 | NPP-375D | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 041f5961-d41b-3b65-bd0e-46c7fe06b31e | -2.27708 | -66.42681 | 2024-10-11 05:40:00 | NPP-375D | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9301326-22c1-3d83-a67f-bbf2fd98f652 | -3.16861 | -50.43805 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| af208a14-c721-3635-8201-59a65ccae18f | -3.16366 | -50.43211 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2a09f413-0c2f-3389-b525-35a0b777e064 | -3.16254 | -50.44 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| af059701-9737-3297-af01-d0492c1ce608 | -3.16134 | -50.43705 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 15afabd4-cfe3-362c-88cc-1fcd15a3364f | -3.15526 | -50.43906 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2373bcac-96d3-3c8e-a231-a7368bea16d0 | -3.15414 | -50.44693 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 546d2c34-af1a-3f29-b4f6-e1203579e48a | -3.15403 | -50.43628 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dd9fcd3f-e34f-35ee-b755-9c260f718399 | -3.15287 | -50.44416 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ea2ca838-1208-3de2-a505-ea825fa12fbf | -3.14798 | -50.43806 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bb997cda-efc5-39fc-98f0-9b707ed68685 | -3.14692 | -50.44564 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1698b3d0-3f7e-322c-8631-13cc052fe9c6 | -3.14674 | -50.43539 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 72c4bbf7-0eac-3469-84d5-8bb9af6fe9d4 | -3.14562 | -50.443 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 95f49094-29bf-3616-9754-1c96c5c53952 | -2.37749 | -50.31922 | 2024-10-11 05:40:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38fc3da9-2c22-3f2e-98e5-1b46b6e0110c | -2.37642 | -50.32645 | 2024-10-11 05:40:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f61366e8-5cd3-30a7-a195-932c9689fd4e | -4.83466 | -50.79671 | 2024-10-11 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b98b11d3-40bb-3a49-b415-976029d09043 | -4.83413 | -50.78983 | 2024-10-11 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb2c35fa-ae0a-3277-b2f4-09538f97d231 | -4.83306 | -50.79724 | 2024-10-11 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5dcfb68a-237e-369c-8468-7bdd6b84f6d7 | -4.82737 | -50.79587 | 2024-10-11 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ea7c6271-77f8-39fb-835f-51aa2c08a39e | -4.82579 | -50.79626 | 2024-10-11 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a090f50a-dde6-3b24-8ead-b95c5384d632 | -6.10283 | -51.10109 | 2024-10-11 05:40:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4a97bae-4939-395d-ae36-c682044c0e6f | -6.0963 | -51.09441 | 2024-10-11 05:40:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efd4fcf9-5959-3645-a272-ed974265592b | -5.28759 | -50.98815 | 2024-10-11 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a3121c6-c53c-341b-989f-3c95b0bf8622 | -5.28035 | -50.98716 | 2024-10-11 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9b68454-13e9-3694-90b4-31d1decd4905 | -3.3387 | -50.80592 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0650c24b-d6ce-39d8-92db-2137bb24c737 | -3.33548 | -50.80399 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e16e2d8-562a-3950-ac2b-55bb1899a157 | -3.33156 | -50.80494 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bc36f64-9316-3933-a5de-638e31930fd4 | -3.28195 | -50.94425 | 2024-10-11 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 737b099f-7d6e-3ca5-8c07-172becc2a498 | -3.28096 | -50.951 | 2024-10-11 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b71c21f4-d6c7-3e65-9dd5-1cb68773ca44 | -3.27489 | -50.94321 | 2024-10-11 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8545a86-f343-37ec-bbbd-744a45c601aa | -3.23817 | -50.84716 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4839e7ef-1135-3f51-880e-c2eb6745884c | -3.23497 | -50.84839 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6453a746-a24b-3dc4-b617-c1d62489b095 | -3.23396 | -50.85513 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 616aa3d5-c482-3e4d-9ae5-507c1c12be1e | -3.23103 | -50.84639 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab2b4d73-6154-3d07-bf93-0df863ade4e4 | -3.23009 | -50.85296 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| de5f133f-8827-3012-8bb5-b8d73591ce2a | -3.1666 | -51.3033 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9795f944-9632-3be2-81eb-193967530835 | -3.16565 | -51.30225 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89d6034a-8fa4-376a-ae6a-1ec0faf9bfad | -3.16564 | -51.30969 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f06e63e-85bc-3ddd-9ab0-b1b9cae2224a | -3.16472 | -51.30868 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5307ff9f-13fe-3ff0-a548-a51e0ff70e5a | -2.97547 | -51.35545 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 04dd16f1-0559-3bcc-8b2c-fbbba338b881 | -2.97456 | -51.36168 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| efcfa3c5-d28a-3e1c-bf42-3581ca918328 | -2.97362 | -51.36809 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abbf8fea-01fd-3c21-89ca-858d4ec0d0b7 | -2.96875 | -51.35543 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e479568d-4e19-3244-9273-42547d8ac57c | -2.96778 | -51.36182 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d131a324-364c-3147-98ed-7bf7dcfe8d1a | -2.96768 | -51.3607 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1260a683-9f60-33cd-b432-5fb4f660d4d0 | -2.96681 | -51.36817 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ec05e9b-4bf2-31a8-bce5-70789291bbd0 | -2.96675 | -51.36711 | 2024-10-11 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33cd77d2-74ca-3f02-aeda-1cfabd1101f6 | -2.80843 | -51.00912 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3211ab75-dec4-3279-a64e-7a3be570fa2e | -2.80748 | -51.01566 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18938641-1cc0-378f-99a1-e19a8d99869a | -2.8038 | -51.00908 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 112342b6-b0fc-31c0-bebd-4fa79534fd6a | -2.80281 | -51.01552 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| d245d726-7950-3819-8e74-3cb65cb197cf | -2.80145 | -51.00798 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e889a689-e7bd-344b-a175-d215dfadbaf9 | -2.80051 | -51.0144 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d6e8972b-812b-3c8c-8bd0-254e38b639b1 | -2.64285 | -51.70173 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7be1164-ea41-3808-9e2d-e80448c1ed8e | -2.64197 | -51.70758 | 2024-10-11 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff977551-675f-3f95-8989-8edaa4cdcd52 | -4.08984 | -51.02396 | 2024-10-11 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41a644ac-029e-3b3f-bc2a-dfd4e8414bfa | -4.08893 | -51.03032 | 2024-10-11 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d02ba30c-b88b-3cc4-97de-d3fb18d24b8f | -4.08274 | -51.02285 | 2024-10-11 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35d181a0-9fb9-3fbd-9b4c-84f51c0d186a | -3.92282 | -51.22154 | 2024-10-11 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d1e056e-bab8-3447-8965-6a19bb236480 | -3.92182 | -51.2283 | 2024-10-11 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12e604ad-2688-36d0-9985-ffc86fd37721 | -3.92128 | -51.22102 | 2024-10-11 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9126639d-24a1-3fdd-9dcc-32e7ba2cd774 | -6.40873 | -51.72695 | 2024-10-11 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 528c1d65-13e0-3474-8608-53f7e082c1ce | -6.40956 | -51.72073 | 2024-10-11 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59e377e3-2b06-3afc-b2f9-8533797b49d2 | -6.3181 | -52.78564 | 2024-10-11 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27eff14f-d900-30b5-b41a-9287a7963b36 | -6.31735 | -52.79134 | 2024-10-11 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f1a6911-a49c-3a89-84cc-d6bfcc542477 | -3.32474 | -53.0004 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4c68d4c-51e8-3734-a316-a47c7a403c5b | -1.58983 | -53.34259 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README103.md)
