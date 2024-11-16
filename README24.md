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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07390c65-c763-3bd4-bb17-568e040a8e7f | -30.13081 | -51.59322 | 2024-11-16 04:10:00 | NOAA-21 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| b271ca4f-5b28-3fb6-bcef-7cab0118b5d6 | -28.4164 | -55.72599 | 2024-11-16 04:10:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| ec6dbdc3-ff06-3059-b3ea-31b7e6c7056c | -30.12962 | -51.59917 | 2024-11-16 04:10:00 | NOAA-21 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 0eda5376-f8c6-3943-a473-65fd387d89f0 | -29.28866 | -52.01749 | 2024-11-16 04:10:00 | NOAA-21 | CAPITÃO | RIO GRANDE DO SUL | Brasil | 4304697 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e8a75ac8-1c4e-309a-92c6-6929a563602a | -28.41724 | -55.72245 | 2024-11-16 04:10:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| 9efa177d-62d1-3103-9c60-565273992593 | -15.9025 | -59.2741 | 2024-11-16 04:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 28c85f83-c234-319c-9c30-4f7cdebbad5f | -3.2009 | -45.5405 | 2024-11-16 04:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1e027728-c171-3720-8175-f850b6f36f8b | -3.2753 | -45.5151 | 2024-11-16 04:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b83f3481-52e5-3d77-b94a-fd1f0209816b | -17.5478 | -57.5375 | 2024-11-16 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 11070887-4790-3eeb-880e-e64f8957aa88 | -17.235 | -57.4516 | 2024-11-16 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 3618f91a-7a3a-391b-bc8b-96a0a27981b1 | -2.2299 | -53.6219 | 2024-11-16 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1cffe3a1-cb37-3ed8-af8e-1fead059bb89 | -17.5678 | -57.5146 | 2024-11-16 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| a7057ec6-cf95-353d-9b08-9bfbd8ae09d7 | -15.9219 | -59.2722 | 2024-11-16 04:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1202aa61-9f89-3e05-b2b1-667f886ef7f3 | -3.7393 | -45.6747 | 2024-11-16 04:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 1643b61f-e26a-3766-b171-411160401039 | -17.2547 | -57.4493 | 2024-11-16 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 65dc30a4-1273-3eea-b4a1-27276188d44a | -2.78 | -48.5806 | 2024-11-16 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 458076ca-e48f-3ef8-b81e-cfe77e3e3af8 | -3.2008 | -45.5629 | 2024-11-16 04:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e2ece53a-754c-36c7-90a8-4688b2562b3e | -17.5675 | -57.5351 | 2024-11-16 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| f777a998-9fce-3e71-89d4-269f71955403 | -3.7394 | -45.6523 | 2024-11-16 04:20:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 7973cbe9-09d5-38d3-bc2f-e9959e9d311e | -15.9222 | -59.2521 | 2024-11-16 04:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f04a0176-448d-3705-941e-d3336b94bd2a | -3.2754 | -45.4927 | 2024-11-16 04:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 47d995ff-e190-322c-9271-b8badc3cbb0d | -15.9028 | -59.254 | 2024-11-16 04:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| f992d57d-be23-379b-8971-6f19511d877d | -5.6796 | -35.6418 | 2024-11-16 04:20:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 71.6 |
| a1b7cb10-d70d-3d8d-b435-9ec1769db4d6 | -2.0271 | -53.9477 | 2024-11-16 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f69f5447-feee-3252-a9f3-ed89fdf9b74d | -2.2299 | -53.6018 | 2024-11-16 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 216a74a2-6fff-3839-bb81-80496232b09b | -3.69614 | -50.10835 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e87e8366-f10d-3fac-89d4-8822365541d9 | -3.99221 | -45.86092 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75e3f368-08f7-3e43-9d87-ae767d3893e0 | -2.22518 | -53.60708 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 656478a4-ff4f-3d46-9232-d2321cadef9f | -4.54402 | -42.97621 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8bd83f7-e255-34bc-9d9e-9d291f98ea5d | -3.12302 | -45.7493 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc99e333-11fa-3287-9a9e-a3550caa6633 | -2.55588 | -46.90417 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e1f11e80-0ef4-3719-b738-1b0e2b7f6af5 | -3.11726 | -45.89373 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 040cf629-8d26-36d2-aa7a-db9e01d7d7bc | -5.21625 | -43.78931 | 2024-11-16 04:23:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e8047ba-7bf0-30ba-ba75-2a47cdcc9c96 | -2.58023 | -54.42051 | 2024-11-16 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca2e9c08-475c-3d08-89cb-da52fa51fad8 | -2.63141 | -46.82645 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26faef74-b132-3e66-ae00-0b9de722a94d | -2.28509 | -47.91832 | 2024-11-16 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be1a34ea-bbba-3b06-ae99-cb08d49fbf49 | -4.1156 | -47.97377 | 2024-11-16 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7fcdff3-13a3-36ca-9579-a31f26f527a4 | -3.12392 | -45.89476 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d72e7b3-b3db-3db3-ba82-f2ad5b92a24e | -3.99699 | -46.49656 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb05374f-25a6-3817-8bae-11e9d5516c6c | -4.99159 | -44.32213 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b94f1c15-5b19-305c-997b-52946b18f604 | -4.1288 | -46.94499 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d0d2f6b-cbd4-325f-a219-af466304041c | -1.68477 | -48.46135 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82298f7d-5a69-3053-8698-ca8cff04cfc8 | -2.89922 | -45.34713 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9a7922b5-c8ab-3a96-9763-fe4f1b25c631 | -2.30298 | -46.44875 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d25f6dc8-8388-332c-90bc-c4a3a0fc9616 | -5.2967 | -43.07059 | 2024-11-16 04:23:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 015fb956-2406-3cfa-a22b-1538aecdfae4 | -3.88346 | -45.02274 | 2024-11-16 04:23:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fdb52506-a561-3d40-be41-2561afeac1ac | -3.19164 | -45.55137 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2afa0748-1f92-35b5-a691-7edcfbb0fb00 | -3.5018 | -47.21442 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a44d1112-12ed-3276-8bf5-3cbb8f97f68d | -1.40662 | -51.09141 | 2024-11-16 04:23:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d9c9086-95e7-3d85-b242-1c5427df7751 | -5.00515 | -44.32421 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee6ebf49-8e32-3276-9baa-d44889107320 | -5.67651 | -35.64869 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 4218cf14-e594-3747-aca5-8c6943b927f2 | -4.01097 | -46.53818 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5983912e-1212-3b39-8944-69b29bbfff19 | -2.65627 | -46.17869 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3d25a39-7949-3f54-a2d9-109dcd7dc918 | -2.17834 | -48.55079 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 210165e0-30c8-3563-9568-068b5ae6aaf1 | -2.39498 | -49.03792 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27b65eb9-d26a-325a-8860-712c25fd275d | -3.81027 | -46.90234 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e48404c-c6dc-3edc-9769-4c3f2fac9cb5 | -2.47129 | -44.83837 | 2024-11-16 04:23:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cd58e91-2811-3034-b71f-db540e1bff76 | -4.22074 | -47.2212 | 2024-11-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1b95bb9-2491-3c68-a7bf-47d6e0b5b5fd | -4.22465 | -44.04575 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb9ac98b-1f1b-31e8-916f-5a09aa676b50 | -2.22568 | -48.36796 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a72e9244-f627-3b70-8b30-f71a2ebe3311 | -4.22964 | -50.67791 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 175bbcf4-aaab-300d-92b1-aa46b6492ce4 | -3.03616 | -47.97821 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 372a8057-8701-3587-a720-dc671ee36f31 | -3.69566 | -44.90413 | 2024-11-16 04:23:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c797f11-eb8a-3892-9b78-38a952a2e693 | -2.55645 | -46.90055 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f401d2a7-0507-3e11-9553-22abb1b49ce7 | -4.1577 | -45.43472 | 2024-11-16 04:23:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d098cdff-cc37-3258-ad57-757e2038ead1 | -4.11982 | -46.93628 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 098abd8e-e0c5-37be-b272-70ed0d14c126 | -2.78624 | -45.9561 | 2024-11-16 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cc65515-9ac7-358f-9a9e-8100c080599f | -2.6563 | -46.20024 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 849d2d7c-97a7-3acc-83e4-2fbf22f6c002 | -2.46797 | -44.83785 | 2024-11-16 04:23:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25416743-b8c4-3ecc-b4a4-141792fd8e7f | -2.68236 | -46.70176 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac454b5d-6b2c-33a3-9f93-d5dcba70aa93 | -2.22039 | -46.86346 | 2024-11-16 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9e5e727-5d7c-3704-8e6b-d04c898f6d63 | -3.94241 | -46.40893 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd15da28-c6df-30de-885f-22770c771909 | -3.78107 | -50.10692 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67af4d84-38f4-3bf2-a49c-8fa2fe777e6f | -3.28288 | -45.50968 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ceef163-cd12-32c8-a0f7-4ada2b896538 | -4.01722 | -38.25005 | 2024-11-16 04:23:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c97dfb69-aa14-3b5b-a5d1-3d046e7baac9 | -4.22131 | -47.21758 | 2024-11-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56c12090-a2ef-31e6-b135-b9ba6fccd6f3 | -3.73323 | -45.6579 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f11fd94f-a819-310e-806f-4c38e0ea1ec9 | -2.65017 | -46.19567 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e806ba3-7e8a-3981-b05b-7ec4fe8a28d5 | -3.20656 | -46.67683 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2329a03-c260-3ce0-9f77-aaa4c4dca698 | -3.84817 | -49.44068 | 2024-11-16 04:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e81e560-9660-3492-bfca-8206d06b0406 | -3.37792 | -46.49636 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 952bd607-a8ff-34d5-af70-1acde59c157c | -2.1454 | -46.40952 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58a1c0b3-c868-3d55-bc64-17b43d4cf49f | -3.11635 | -45.98598 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d112f16f-ca5f-30dd-bce6-a5a08f941534 | -3.73215 | -45.6648 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbe289eb-9bde-3d3c-9e93-4fc6c861d526 | -2.97591 | -47.99292 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a9cb357c-926a-33b6-9200-14c516430810 | -3.72605 | -45.66031 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5257d90-7823-33a6-9f3e-c4fa622795c0 | -2.71965 | -47.90655 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87c8edd4-1c22-3e53-9ee2-d01ebffcec4a | -3.24806 | -46.5233 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff1f9cdd-6ee0-3005-ba73-2595e8fec963 | -2.68228 | -46.83453 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc3f9173-da5f-3b7a-9aff-27b98ed81549 | -2.13126 | -46.54246 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c43d7706-afcb-327f-ad47-6718c00c2481 | -2.14092 | -46.39426 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15ddfb2d-54c1-378b-9e3a-4f4c5e99b538 | -3.09912 | -45.96551 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e820f069-7f94-3036-960d-7fb30fb74400 | -2.2303 | -53.6078 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 954c6037-49a1-391b-b6cb-8eea4328008e | -5.6717 | -35.64597 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 13.7 |
| c4ae829c-8354-3588-946c-a2c0872b6816 | -1.70983 | -46.16414 | 2024-11-16 04:23:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0582c3b8-4a86-35eb-865b-c9ee686688c3 | -2.19152 | -46.60688 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af8c881f-3546-391d-b250-22af83fd76a6 | -2.22116 | -50.51172 | 2024-11-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99f005d1-18f8-3d2f-a781-7d0da3613cc1 | -4.90772 | -44.02959 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7940cd23-f168-37f6-b368-b56ac43c8857 | -2.0288 | -46.37642 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c381b072-ff20-373d-bec1-7f7a129365b2 | -4.98876 | -44.31799 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |


[Clique aqui para ver as próximas entradas](README25.md)
