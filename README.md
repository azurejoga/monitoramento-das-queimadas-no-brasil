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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6699bd32-eaf9-3b1c-a581-55d788410d24 | -5.3287 | -47.2744 | 2025-10-06 00:00:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 5437c83e-c3c4-3dd9-a97c-52a45da352ed | -4.6318 | -43.1816 | 2025-10-06 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| ef464a7d-f45f-355f-adf2-2f0be29c25fe | -14.8824 | -51.4992 | 2025-10-06 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| f700c04d-dd7b-3897-a19f-8aeb3c003ac0 | -10.8093 | -48.8229 | 2025-10-06 00:00:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| e25a8c15-c2b2-36e6-9100-1a9101a8b253 | -4.6505 | -43.1805 | 2025-10-06 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 228.5 |
| a3de1491-154e-32ef-a7de-8595ee90e302 | -18.0008 | -57.5444 | 2025-10-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.2 |
| cb5c70c3-645b-3c45-b5ac-62d904ab6a2c | -10.4746 | -48.3805 | 2025-10-06 00:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 33097c9a-0ac7-3efd-b917-9331f1ea0288 | -18.1167 | -53.3977 | 2025-10-06 00:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 065c1294-f607-3b95-9c55-4675e8bcd884 | -5.6844 | -44.8165 | 2025-10-06 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9bc998a2-88cb-33c8-9990-0994de864ae7 | -18.5904 | -49.9717 | 2025-10-06 00:00:00 | GOES-19 | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | 117.7 |
| 508c0b36-8591-375e-92d9-a85b1438d045 | -4.6691 | -43.2026 | 2025-10-06 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 3dff82a9-9cc3-34c4-9941-ce731c830a0f | -5.7028 | -44.8607 | 2025-10-06 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 412072dd-4dff-3136-89fa-4a476b0bd10b | -14.9018 | -51.4965 | 2025-10-06 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 37aeaa66-ad53-3509-ac15-27dbb750e81e | -5.6375 | -45.9481 | 2025-10-06 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 1c002170-e7fb-311e-bf4e-dd384e1c968b | -8.5379 | -46.3752 | 2025-10-06 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0fb011f4-99a1-3650-986d-925d1e30b16e | -13.3715 | -47.5564 | 2025-10-06 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| eda3b0c1-bf35-3658-a35e-29e3976fdc83 | -17.981 | -57.5468 | 2025-10-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 0218f0ba-4c9b-3a2b-84c0-a45e18e35e1c | -17.98 | -57.6086 | 2025-10-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 636798ec-43b1-3cb5-946e-f608a2fdd892 | -10.9851 | -51.1443 | 2025-10-06 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 3aad0250-fb35-3943-82e5-21486621d187 | -5.7032 | -44.8152 | 2025-10-06 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 623df85f-380a-3d98-9e49-1c4ec48af873 | -9.8865 | -49.9579 | 2025-10-06 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| d2ebe9e7-88ec-3ff7-a82c-2dc3d3ca9670 | -4.6317 | -43.205 | 2025-10-06 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 64dcacf7-43e2-3bfc-9319-13b6eea47ed2 | -2.5968 | -48.1124 | 2025-10-06 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 9ed07147-870d-340f-8439-886615ca88a9 | -11.2022 | -54.8771 | 2025-10-06 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9cdca404-2da3-3081-8ad0-778229d9b4bf | -17.9803 | -57.588 | 2025-10-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 9d54e4db-a965-3793-81f6-93d6b7e5b104 | -17.9605 | -57.5904 | 2025-10-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 2709d017-748f-3db4-8e46-333a1ec91077 | -8.4858 | -54.7023 | 2025-10-06 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4fa6814f-7984-3763-b4d2-dcfc886b86c4 | -5.6843 | -44.8393 | 2025-10-06 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 2d8149e5-462e-38fb-9274-18c6a81b556d | -8.5376 | -46.3976 | 2025-10-06 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e9ca27e4-6744-311b-b27e-6fce491976b8 | -4.6507 | -43.1571 | 2025-10-06 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| b75e341e-500c-341a-b707-ef2133781b38 | -20.6489 | -51.4905 | 2025-10-06 00:00:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.3 |
| f99ed568-f9d3-3262-b5de-eface4c1f810 | -10.9848 | -51.1655 | 2025-10-06 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f0d4e15b-c4c5-3cfd-a41d-29abf28be63c | -14.882 | -51.5207 | 2025-10-06 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7212bc76-d38a-3b78-bf75-d7a6028e6fb4 | -7.0181 | -42.7818 | 2025-10-06 00:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 89071153-67ac-39dd-a733-c3440302ac0f | -13.371 | -47.5789 | 2025-10-06 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| de6384cd-f4e1-3609-86d9-06408640617a | -17.9998 | -57.6062 | 2025-10-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 645b80e2-722d-355f-963b-aa11d8d2bc9a | -8.184 | -47.6723 | 2025-10-06 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 4ab44155-833c-30c6-a43f-9347c7f427f6 | -12.4472 | -45.5415 | 2025-10-06 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| c772391c-8600-3f61-a55d-380b84ee63ef | -5.3285 | -47.2963 | 2025-10-06 00:00:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 0a8123c7-1a54-3b34-8cdf-63f123b2594b | -12.466 | -45.5616 | 2025-10-06 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 2d81b68c-7223-3184-94cc-64ae7ea7726c | -18.0001 | -57.5856 | 2025-10-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 99ca8e76-775c-3720-95ca-12b8e8628398 | -4.6504 | -43.2038 | 2025-10-06 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 207.5 |
| edf717c6-f51d-3988-8118-78dd0d7dd4cb | -14.6135 | -52.495 | 2025-10-06 00:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 68a2e3fa-8fcf-3e7e-b67d-c9fadbdb5508 | -12.4464 | -45.5876 | 2025-10-06 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f49882ab-25da-3130-ae81-a0708fdc37b0 | -5.703 | -44.838 | 2025-10-06 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| d2236017-566a-3bd3-91b1-6b3471b1c9e6 | -9.9054 | -49.956 | 2025-10-06 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 41f7db88-036e-3d7c-96d3-5bae59810576 | -12.3793 | -63.7294 | 2025-10-06 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 0e39e543-9a50-3e46-a46c-7c842d9f68e5 | -18.1366 | -53.3946 | 2025-10-06 00:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d5f87b1b-6093-322f-926e-dc0e9ca5a3c5 | -14.7096 | -48.3542 | 2025-10-06 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 2dde15fe-c7dc-3000-ba8d-fa0d1d6ba543 | -14.9014 | -51.518 | 2025-10-06 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4c4ba372-9c2e-3d0e-a117-3344427adc91 | -11.1835 | -54.8584 | 2025-10-06 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 6044ecb2-b3ed-3b9c-9391-69eb58e321d8 | -17.8621 | -57.5818 | 2025-10-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| c451a17e-728c-34cd-9af2-f5386d95d823 | -17.8617 | -57.6024 | 2025-10-06 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 93917814-72fc-30b7-a4f8-9587cadeaec4 | -11.2024 | -54.8567 | 2025-10-06 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 3de8c3c5-2e87-3aa9-b3c3-f8a3aecf064e | -12.9103 | -54.7352 | 2025-10-06 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1b803da5-4be0-3b45-a365-956636e44a0a | -8.6141 | -46.3003 | 2025-10-06 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d83e7fb4-c10a-31f0-b283-b82f160bc9b6 | -12.4468 | -45.5646 | 2025-10-06 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 317.5 |
| ff5a7b74-bde4-310a-be6d-c18831fccd28 | -8.4673 | -54.6833 | 2025-10-06 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 75af6d88-1dfd-3021-96df-d85ebf02c1fd | -17.6852 | -52.2398 | 2025-10-06 00:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 5496dbd8-a453-3395-97aa-198fdc6d5a3e | -5.6373 | -45.9705 | 2025-10-06 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 814dad79-bcb0-3244-8a3c-68efb1d2a853 | -8.4671 | -54.7035 | 2025-10-06 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 85bbab84-2888-3fc7-b3f5-c6e0c1f41a52 | -18.5899 | -49.9941 | 2025-10-06 00:00:00 | GOES-19 | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| fa6992da-e7bb-3f5d-9354-6861207686b9 | -17.9998 | -57.6062 | 2025-10-06 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 8d084911-d29f-3864-a6a6-335adfb158b9 | -14.9161 | -46.8312 | 2025-10-06 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| b5a67b17-0144-320e-a3f8-46560246b31d | -14.6897 | -48.3797 | 2025-10-06 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 0e39675b-df8c-337d-8d30-34e3e9dd6d50 | -5.7028 | -44.8607 | 2025-10-06 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5a899620-07b4-3456-9bcd-7befe81d46a7 | -10.8093 | -48.8229 | 2025-10-06 00:10:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| b88a7c21-2aa8-3dac-93ac-775121ebf21c | -12.4468 | -45.5646 | 2025-10-06 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| c5185323-e03b-3c85-bf83-f46c8c01010a | -12.2497 | -49.1932 | 2025-10-06 00:10:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 43f26517-b8fa-3523-8ad3-97b7b95fb3a2 | -5.3287 | -47.2744 | 2025-10-06 00:10:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e54a90e9-ca5d-30b0-b877-5277625a216c | -5.1882 | -46.1557 | 2025-10-06 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 06b6427b-4e69-3499-8825-95c1b8a325fd | -5.6375 | -45.9481 | 2025-10-06 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 2c3f513c-5181-31af-a5f1-f2b7ea9d55d8 | -13.371 | -47.5789 | 2025-10-06 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 38.1 |
| d55acb93-6479-36f5-9633-22d31aa98bd7 | -17.9803 | -57.588 | 2025-10-06 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 5e37b93c-b1d2-3e46-a9b9-4538e3664c6e | -5.7215 | -44.8594 | 2025-10-06 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| c27de85a-a624-3dac-a456-a562c263c0a4 | -14.9014 | -51.518 | 2025-10-06 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| b11cbcab-af54-371d-b220-6b88bf990026 | -14.882 | -51.5207 | 2025-10-06 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 304f6cc9-5243-39b4-8ab2-5cf1d7c1b382 | -14.55 | -46.6662 | 2025-10-06 00:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c72f2ab1-abef-36fa-8699-39c0a893dfd4 | -8.4673 | -54.6833 | 2025-10-06 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| bfa70a27-3676-3829-9b45-6d8cc0ea9968 | -8.1687 | -44.2534 | 2025-10-06 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 4c53831f-2969-3f72-b195-12335b85aaba | -5.2856 | -43.3247 | 2025-10-06 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| ebf5538c-be7e-3af7-8f2f-c40e09358092 | -14.6321 | -52.535 | 2025-10-06 00:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b02b938d-3807-389c-a5e0-e156cf85eddd | -17.6852 | -52.2398 | 2025-10-06 00:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 158ff6e8-ab50-3a55-9c57-10bda4b9e5dc | -18.1366 | -53.3946 | 2025-10-06 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1bfda604-443b-3e8d-b56f-aab845d2ad30 | -17.8621 | -57.5818 | 2025-10-06 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 82e75800-fc5d-3bb5-aa49-4d56aef78041 | -7.0181 | -42.7818 | 2025-10-06 00:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 0f8d7f36-8fc4-33d0-8b10-68cbe4058a4a | -8.4671 | -54.7035 | 2025-10-06 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 049b2340-7b24-38b8-a72f-b22f65cf67b4 | -8.4858 | -54.7023 | 2025-10-06 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 48124032-c659-3d5f-91f9-bce33ce3e02f | -8.1876 | -44.2514 | 2025-10-06 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 8fafada9-554b-377b-9843-98b8b0722567 | -17.8617 | -57.6024 | 2025-10-06 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 80bae7e1-a6cc-3e88-99c0-ea6340746dab | -12.3793 | -63.7294 | 2025-10-06 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 5c933987-8502-3c40-a6a4-8957f7338106 | -14.8824 | -51.4992 | 2025-10-06 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 182.7 |
| e2462f89-f308-3f28-a94d-25fb5ac57eee | -4.6504 | -43.2038 | 2025-10-06 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c4b001ca-9ee9-34ed-b08e-76f35a995ca7 | -12.4464 | -45.5876 | 2025-10-06 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 228f6cc0-fec6-3371-82ea-ce073d7916d1 | -18.1167 | -53.3977 | 2025-10-06 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 5f75ed37-c418-3329-98b6-276a0af9bc0f | -8.6139 | -54.9558 | 2025-10-06 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8e3009c0-0529-3695-b42f-2aae5456327b | -8.1879 | -44.2283 | 2025-10-06 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 46d8a7f9-6e42-393c-8e37-41e3ed49a212 | -4.6505 | -43.1805 | 2025-10-06 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| cd189b4b-d515-3367-8e1e-542aba2aea9d | -14.863 | -51.5019 | 2025-10-06 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| b483210c-d2bc-30dd-98b0-bcca3a281e7f | -6.3855 | -35.4284 | 2025-10-06 00:10:00 | GOES-19 | SANTO ANTÔNIO | RIO GRANDE DO NORTE | Brasil | 2411502 | 24 | 33 | nan | nan | nan | Caatinga | 73.4 |


[Clique aqui para ver as próximas entradas](README2.md)
