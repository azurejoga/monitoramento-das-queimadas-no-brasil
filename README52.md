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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70203447-1947-397b-b346-a485dcb9b869 | -4.96918 | -55.85312 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a82cdeeb-d720-3569-8504-e630c995df34 | -5.98991 | -57.67514 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfd19b7b-83e8-383e-b3a4-cec854c89155 | -3.84331 | -44.05597 | 2026-09-02 05:16:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 824ee33b-7811-380e-b8f7-d6b1d4148c30 | -8.47927 | -54.70327 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bb16d53b-2585-314a-a9e0-b66a32ecf7ed | -4.96693 | -55.84544 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dff1e96-e45b-322c-9995-355b12263bc3 | -6.25345 | -55.41171 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a7262ea-9418-38a0-a2fd-031173c7a3b9 | -5.18011 | -60.28595 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eb60113-8c72-30e8-867c-a83e68c08e24 | -9.44219 | -45.62472 | 2026-09-02 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c54e689-39f8-3345-bc4c-adff4f78b664 | -6.94507 | -56.46065 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 200b713d-1b2c-34d3-825e-6747553ce018 | -3.07353 | -60.73685 | 2026-09-02 05:16:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21341822-5dd9-3127-9940-2901bc3b7902 | -8.45027 | -54.69685 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5852ec8-d9d9-324f-9010-ffc70916fc23 | -8.5029 | -50.30181 | 2026-09-02 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57d4f36e-88c1-394e-a1b9-43ac46ce51f3 | -7.56037 | -61.43011 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4a3c9b5-9e25-35ba-a4fa-56e010adb489 | -6.15401 | -57.77592 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 069e30c7-3148-3a1d-a539-d4069e4d2fa0 | -8.49805 | -50.30114 | 2026-09-02 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1db2eca8-39f9-36c0-9253-b70f49809fda | -7.56384 | -61.36342 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cca2b105-f324-3386-9394-bd3c6e0350e6 | -8.4524 | -54.73392 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ef4dfc4-099f-3746-abe4-b4c9219c71fa | -8.49879 | -50.29579 | 2026-09-02 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f90ad95-6a91-3edf-b944-b6751b07af37 | -6.1491 | -57.91351 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f56e0238-0bb5-33e3-bacd-732ff864a9ca | -2.90725 | -54.15232 | 2026-09-02 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ff76b48-a46c-3bc6-8c19-b07409735891 | -6.07682 | -53.66833 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 880a78fe-d07b-3245-9945-3120c57d8dd9 | -4.16283 | -47.83714 | 2026-09-02 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d10cf25b-1527-3630-9175-3ed339cbc713 | -6.73958 | -56.34109 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6232cee-27cd-331e-a16d-f173ebbafa61 | -6.55406 | -55.13471 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4bf642c-a6f2-31ea-adf6-09522dfb58e6 | -8.27355 | -54.95049 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 440b75cd-1733-39a1-86c7-c9af83833881 | -8.46093 | -54.72651 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2c5af07-e6a6-3d42-8834-43bb16c2d58b | -7.43886 | -61.41555 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dcc0e3e-94e7-31db-85cf-355c68329a61 | -6.15786 | -57.77304 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 86a43b8a-3a7d-3e7d-bc4d-8f7bc28f54b2 | -6.86991 | -59.03833 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04cae8ed-e233-31e8-8549-fb5c4d71ee54 | -2.83628 | -49.51238 | 2026-09-02 05:16:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 745acbc1-0852-38e6-b0db-17df7f03df7d | -8.42712 | -54.70205 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 942c423b-0633-3160-9276-456bfa5f9736 | -8.46885 | -54.72334 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ec2c4d53-8a0e-35b1-84e6-96ccb591ad4d | -5.97662 | -55.70539 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2858783e-e2cc-36c6-a60c-1c40d53ebc22 | -9.15007 | -49.97993 | 2026-09-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45140cb4-11f7-3652-908d-ecf86a493de6 | -6.16008 | -57.78044 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca175d55-8634-37b9-abb7-c90d89498a8b | -6.15122 | -57.75072 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b27acc39-a698-3cfd-a43f-f2b4954a772c | -8.71846 | -52.36542 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2b7eb73-c041-346c-b177-efe868cc6532 | -4.11934 | -51.03517 | 2026-09-02 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d15bbb9-ce95-3b33-a94c-b553a4e14e20 | -3.79945 | -59.29414 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc9bdf4b-8198-31db-b56f-af0223d517ba | -6.68848 | -59.94278 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c37f8817-8f68-3337-abca-f73025503d24 | -8.45366 | -54.72539 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 866c8b9d-0640-34a5-811c-838d59534381 | -7.43958 | -61.41117 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 612e5bb3-bdc3-360e-8063-cdc70fc9ac57 | -6.09199 | -53.80626 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eddc0a78-33f7-38c4-9297-390f8c517bc4 | -7.2138 | -60.67194 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fc788c4-06ce-3086-a698-fc7d200cd4a9 | -6.8072 | -59.10567 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86711c7a-8926-37cd-87ad-b483adbf6fe6 | -6.80989 | -59.56389 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e59db1c3-9b31-31e8-a112-2acf35aa8003 | -3.1209 | -61.23278 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fd3d67f-3b1c-30e7-94ca-e5c37ff521ff | -7.20666 | -60.67083 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4688921-0cb0-3c5c-8afd-28efad7dc8ee | -8.45917 | -54.71321 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 50ce94ca-dcbf-3fb3-9495-3db1268d311a | -7.41313 | -55.16637 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb15e4c9-715f-3783-b5af-42c83ca0b5c8 | -6.93813 | -62.88279 | 2026-09-02 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5ed8db9-b0bb-3306-9cc4-328866fc46c8 | -8.46758 | -54.7319 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6498985e-b0c4-31cc-970b-4933635cc6e6 | -3.61894 | -60.55897 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 90be7532-16b9-379c-bd62-4c4f1bd0f8d0 | -9.00801 | -50.78151 | 2026-09-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| be892b6f-424b-3056-b0ec-a189dcac7504 | -6.15562 | -57.72306 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1be029d-c639-3e72-96d3-3ce5d55c4159 | -8.43976 | -54.7169 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03ba86f7-3603-3751-b244-abfda5199604 | -1.50903 | -54.96517 | 2026-09-02 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 84ae9443-603b-33f8-8919-5c968cd252e3 | -7.35504 | -60.60715 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4da4707a-2175-3e79-94e2-ade32cd1c55d | -6.80653 | -46.20533 | 2026-09-02 05:16:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e8a78c7-bba6-303b-b751-42468080a369 | -6.16063 | -57.77697 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 293ba736-42a4-3358-badc-ad7f8985f6b9 | -6.77101 | -59.43603 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc666859-26a7-3be6-9a55-616ff27bacc8 | -7.45349 | -61.37306 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f76e64f3-f7c1-37d6-b9d6-383854767f81 | -7.53603 | -60.71761 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fbb5c1a2-d78d-3522-b98f-08aa0b318e5d | -7.19684 | -60.68586 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b63de6d-023d-3752-971c-6d66bff8f27a | -1.59164 | -50.43753 | 2026-09-02 05:16:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a9bf6be-e463-3333-829d-2fe68f2162fe | -6.262 | -55.42477 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 758891b5-4486-38ad-b8ea-e13829321870 | -8.12014 | -54.95784 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1e335d0c-ed57-3f6f-a929-e852836feb36 | -8.72847 | -49.59834 | 2026-09-02 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 557a52f5-6985-3f6d-8e89-881c9b5af7f9 | -6.05099 | -53.83781 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 756be4c8-82b9-3960-b556-db7f698b7b6d | -5.86168 | -57.56242 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dac8184-33c4-3c3b-8c63-d7280aab1a46 | -6.37879 | -54.76625 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31e06153-b557-37ae-817b-b6d5bf57059e | -1.50623 | -54.96099 | 2026-09-02 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b0f8748-e382-3068-9468-7643c1f8f587 | -2.49939 | -56.07418 | 2026-09-02 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc7f2741-9cdf-3b70-8cc8-a59c5fd4c4c4 | -6.7676 | -59.43548 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0619c14-52b2-385b-9394-549a67b99f13 | -3.6212 | -60.56832 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff3d2381-08fc-3e83-884a-1f8bb0352a6d | -7.34132 | -60.57994 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd6e8be0-cdac-3884-b484-1eb38c29160d | -6.82139 | -58.86909 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f594fbf-6323-3146-b500-aeb8e9f379fe | -8.4447 | -54.70897 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2324399-939f-3e69-b97a-114561a8b0ab | -3.37832 | -52.79353 | 2026-09-02 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63afba1f-8c53-3b43-91e0-b13a6877e9ef | -5.88888 | -57.75439 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ae3e7a9-0d5d-3d4e-9f1c-19fac4d10fac | -3.84923 | -44.06299 | 2026-09-02 05:16:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50d456a5-b8a0-390f-b2d0-305c7f6ce77b | -6.20228 | -55.42318 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c316a7b-017e-388e-a377-780f9723cbf7 | -6.13129 | -56.38557 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 745d5a57-1588-3a56-a3f6-ff2eba06bc13 | -6.0773 | -57.95857 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c05ac80-31b6-3949-9647-79bca7f3a809 | -2.15973 | -47.48223 | 2026-09-02 05:16:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec319db1-6af3-3ab6-ba7a-ab7e35a6addb | -8.47009 | -54.71493 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32215f95-3f8b-33fe-9a2a-95f47219e980 | -6.75678 | -59.43753 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68e3fcac-8f61-3504-92e9-a8cddb8920b3 | -8.28216 | -54.91803 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c5a03db-336b-342c-afa1-6a4bcff87475 | -5.25152 | -55.91058 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63f75dc6-fece-3530-b55b-3a2c6fb0d2b6 | -8.43313 | -54.71154 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3b929bbc-52df-34dd-a4e4-3d0806709b7c | -7.65168 | -45.8741 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 673e5670-fa39-316c-80b7-e014184aef80 | -8.44586 | -54.70247 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1504f74-e002-3e17-aef7-4aef562b01d7 | -8.44035 | -54.71466 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a112801-a94f-367b-8f8a-e6cf9c363a4b | -6.13872 | -59.89184 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7133dffb-b619-3232-90c3-751d9d936a5b | -5.95131 | -57.68319 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caafcf44-6a56-38a4-9206-1278909b87fd | -1.51017 | -54.95794 | 2026-09-02 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b0e8ddfe-7525-37ae-ad0f-15fa9448b474 | -6.86771 | -59.40228 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566db592-1b7a-306e-bbdc-b27d20d252d9 | -6.55814 | -55.13143 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e78fee-872a-399b-bc65-89d24eaf67cd | -6.18857 | -55.28127 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 412018bb-c124-38ae-be89-68687b682859 | -6.9158 | -59.64547 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README53.md)
