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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 862d1a18-ab65-3106-aef1-8bd8a7d415cb | -2.27585 | -53.78122 | 2026-01-06 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| becd23ad-7a8d-32e9-a2f2-13cc3d3cb4ca | -2.11245 | -53.48409 | 2026-01-06 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44315aed-3c8d-355c-801b-4ddbe994eef0 | -2.72028 | -54.54893 | 2026-01-06 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f861680-afb2-357a-922f-3c40e1ea5097 | -2.0085 | -53.21298 | 2026-01-06 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a108bca0-1b32-31c1-ba6c-b7bea1055ff2 | -1.82011 | -54.16388 | 2026-01-06 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 719cd458-92a7-38b2-94dd-614702aada6e | -2.27522 | -53.7855 | 2026-01-06 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed985419-cda9-333a-9a14-fea7d8b84450 | -2.28113 | -53.78653 | 2026-01-06 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 947f1fb6-eec9-31be-badc-bd78acdc2e44 | -2.72083 | -54.54527 | 2026-01-06 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df265fa5-db95-31ba-9ea6-06044bcf59e0 | -2.88019 | -52.57151 | 2026-01-06 05:42:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32baf644-c5fc-35a8-a66c-1ed19f3ceeeb | -16.0663 | -60.07121 | 2026-01-06 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b12e4547-07cd-3684-9fe1-4626729cb63a | -20.52612 | -58.00954 | 2026-01-06 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 416ff0bf-5f61-3a3e-955e-c1cd82aef7b0 | -20.51427 | -58.0124 | 2026-01-06 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fa506652-fb31-367a-943e-e4e1b8f8a804 | -16.04802 | -59.21981 | 2026-01-06 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1576fcb-89c8-3cf0-ba2b-736133481c9c | -20.5204 | -58.00888 | 2026-01-06 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ac442876-c4f5-3801-b3d6-b218e1de79c9 | -15.62116 | -57.33628 | 2026-01-06 05:46:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f875dc67-3285-31c7-bee4-b3d123942892 | -20.53226 | -58.00601 | 2026-01-06 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6109270a-0948-3a08-b7d7-2c3c4fd4ace0 | -16.04296 | -59.2196 | 2026-01-06 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16cf58cd-973c-3457-a43f-d2bf1d819aaa | -14.9283 | -59.90392 | 2026-01-06 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4f14d84-80e1-3331-9d0f-4c1a6cdbef3a | -15.6875 | -59.65865 | 2026-01-06 05:46:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbc255a9-275f-3a79-a836-4e3e7dd850c5 | -17.65487 | -56.45108 | 2026-01-06 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 115ab6ac-0515-31be-b648-4933339c8638 | -17.65441 | -56.45591 | 2026-01-06 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ab7fd991-27cf-3b1f-8c1a-418788d8715e | -14.92892 | -59.89882 | 2026-01-06 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61a59185-9517-3883-bf8a-03aea9fec989 | -16.04329 | -59.21679 | 2026-01-06 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8226b3d2-6d74-3d4c-bd71-012e3c3073a9 | -16.04769 | -59.22257 | 2026-01-06 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7167ddf1-b259-3615-9a25-b4a9431b09db | -16.59741 | -58.21456 | 2026-01-06 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 37d85ad8-f643-3089-8b0a-87788fdb2fa6 | -21.53971 | -57.53231 | 2026-01-06 05:48:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3287b17-9a1b-3acc-99cc-5c890eaa1b9c | -21.53675 | -57.53468 | 2026-01-06 05:48:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c646c7d-6538-38b6-9480-bf3c6101ae89 | -21.54313 | -57.53036 | 2026-01-06 05:48:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32b08fdc-91d8-3cc0-8a35-7301e79a81b8 | -21.54269 | -57.53563 | 2026-01-06 05:48:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2cf1fd4-9fe5-3e5a-b74f-59342ae195a3 | -21.53922 | -57.53769 | 2026-01-06 05:48:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf91a2ce-f52a-375e-b1fc-b28af728eefd | -3.6962 | -43.4432 | 2026-01-06 05:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1f694e9d-71ce-3693-8b5a-4f0bba19df9d | -3.6962 | -43.4432 | 2026-01-06 06:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 61bbc547-53ec-31e6-ac54-3ca2ea69b437 | 2.54038 | -60.56999 | 2026-01-06 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d970fef0-bac6-3036-acd5-1a44ee5ae097 | 2.54612 | -60.3595 | 2026-01-06 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 732da0a0-63a4-3d5d-a106-e2d5427be335 | 2.54461 | -60.35722 | 2026-01-06 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39a63399-820a-3857-803c-f68e2bfaf0a6 | 4.50857 | -60.62629 | 2026-01-06 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbd86230-ff3b-313c-a23d-1c9b058e547f | 3.53764 | -61.01499 | 2026-01-06 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 419efe4d-fad2-3293-8f05-16819ce06293 | 2.83724 | -61.32466 | 2026-01-06 06:09:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c6a70aa-1401-3363-9a40-7298b349499f | 4.27099 | -60.68722 | 2026-01-06 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e78a9df-c68a-38ed-a3b2-5fcfff359b01 | 2.54672 | -60.36303 | 2026-01-06 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 172398f8-0506-3bef-89c5-ed6c5d231826 | 2.54629 | -60.57239 | 2026-01-06 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29704127-7c55-34e1-9f95-1bb598b86819 | 4.1552 | -60.4516 | 2026-01-06 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4630a1ad-518e-392c-939e-3fae1c5459f8 | 3.53662 | -61.00894 | 2026-01-06 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 480fea09-8765-3b06-ab31-15734c266d98 | 4.52376 | -60.62164 | 2026-01-06 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6347506-986c-3124-b602-28790d0cd75e | 4.15139 | -60.45199 | 2026-01-06 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbc0ebd0-a007-3f55-888a-aa60e352f5bf | 2.54552 | -60.35594 | 2026-01-06 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e41f4f7-5bb7-3967-b3c9-955d9967e688 | 4.51758 | -60.61678 | 2026-01-06 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89cbc02d-6372-304b-b6c3-607a186565be | 2.54518 | -60.36079 | 2026-01-06 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b13a96be-8c4b-384c-9e8d-46da35113ee5 | 4.5233 | -60.61897 | 2026-01-06 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a5dd99c-fbf6-32ea-a6b4-42ad0b2452fd | 4.27628 | -60.68704 | 2026-01-06 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 602b6c01-ab74-3d81-8501-1afd0605ac3b | 2.55154 | -60.35844 | 2026-01-06 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 265effa5-cb73-3e5a-8876-91f4a0daa6e4 | 3.54174 | -61.00803 | 2026-01-06 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8feaf51a-9f1b-37b4-92aa-118a722cddba | 4.51339 | -60.62337 | 2026-01-06 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b17bbc2-8e82-3e47-9705-72b40f70a9db | 3.53713 | -61.01196 | 2026-01-06 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f9e4468-4456-3cfc-8ab5-36548ff7fa17 | 4.51809 | -60.61971 | 2026-01-06 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c776aa1-0b95-3845-a232-19c4ccfeb8fc | 4.52284 | -60.61634 | 2026-01-06 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| db312f03-d7a7-361f-9323-9298e827240f | 4.51385 | -60.62598 | 2026-01-06 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbf5820a-272d-31c8-b69b-893d14d78400 | 4.51857 | -60.62244 | 2026-01-06 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6fd488e1-9c83-3901-9184-a7e7abe6b7d5 | -3.6962 | -43.4432 | 2026-01-06 06:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| bdfa90e2-8d27-3e7c-b231-187b741ace29 | -3.6962 | -43.4432 | 2026-01-06 06:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| b49008d9-9b79-3e7e-9c54-8c5b4dbf7ce2 | -2.27718 | -53.78366 | 2026-01-06 06:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d08a42d6-2585-3ce8-a6c7-98f1ff692226 | -2.80721 | -54.43876 | 2026-01-06 06:52:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41c61743-cd14-3065-a5a9-e0c5f6179c5c | -2.09044 | -53.50699 | 2026-01-06 06:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ab7b00c6-8980-39f5-a9e4-105466421def | -2.00221 | -53.21331 | 2026-01-06 06:52:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3524c5a7-ad9a-3a62-8de6-47a345c7a50d | -2.08879 | -53.51791 | 2026-01-06 06:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 37af729e-b813-3811-a2aa-b5d78587d4f0 | -17.65224 | -56.45235 | 2026-01-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 07fc27d0-e412-3622-a0eb-df561cc6c122 | -5.00751 | -38.09067 | 2026-01-06 11:34:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 550f2604-7c63-39ca-a29f-854f1070e20c | -3.19583 | -40.09992 | 2026-01-06 11:34:00 | TERRA_M-M | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| e10a5a5e-f6e2-3baa-8b10-86b9e56e2331 | -6.91907 | -36.69943 | 2026-01-06 11:34:00 | TERRA_M-M | EQUADOR | RIO GRANDE DO NORTE | Brasil | 2403400 | 24 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 7ae2aae5-58b9-362b-8c4d-7bd8411739cd | -6.38675 | -36.87374 | 2026-01-06 11:34:00 | TERRA_M-M | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 0c78c057-f2c7-3161-b4ea-a3c02e83fcba | -7.30914 | -35.22704 | 2026-01-06 11:34:00 | TERRA_M-M | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 43.6 |
| 01fb91b5-1050-3506-8ae1-0000cab592f3 | -7.30754 | -35.22098 | 2026-01-06 11:34:00 | TERRA_M-M | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 1deb18fb-2d8f-3c4f-b3f4-5d11b7ef15b8 | -2.86539 | -40.70311 | 2026-01-06 11:34:00 | TERRA_M-M | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ef2de87e-7120-3d4b-a3ae-ec79e1cf88d4 | -5.00625 | -38.09949 | 2026-01-06 11:34:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c305c818-d31b-3de2-840a-cac0e6cd439f | -7.9358 | -38.24381 | 2026-01-06 11:36:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 53e60456-d54e-36c3-8ea3-33637822cb25 | -14.07036 | -39.49456 | 2026-01-06 11:36:00 | TERRA_M-M | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 75fa1bcb-1833-3089-9f07-5c997949b38d | -7.07814 | -40.60365 | 2026-01-06 11:36:00 | TERRA_M-M | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 3e319c47-d018-3193-a003-015b8d3a39a1 | -8.66195 | -39.42478 | 2026-01-06 11:36:00 | TERRA_M-M | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 726dade9-9766-3c21-a488-5008f57fd832 | -8.19046 | -37.80886 | 2026-01-06 11:36:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5e474027-f3e4-3170-9293-15cc78a23684 | -14.11006 | -39.4783 | 2026-01-06 11:36:00 | TERRA_M-M | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 8655b99c-f2a7-3273-801f-9583a807c807 | -8.43325 | -36.92946 | 2026-01-06 11:36:00 | TERRA_M-M | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 93e3af96-40a9-3676-8777-69adc9a1dcb5 | -8.19176 | -37.79962 | 2026-01-06 11:36:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| de72b182-0d16-33a7-ae34-a2e6eb61fb9f | -7.52889 | -37.9263 | 2026-01-06 11:36:00 | TERRA_M-M | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 51839496-87b8-34fc-9743-874b03fce509 | -7.93453 | -38.25282 | 2026-01-06 11:36:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 95998ef3-a777-36b1-aeb3-fe29d145bbe1 | -8.66324 | -39.41589 | 2026-01-06 11:36:00 | TERRA_M-M | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 8eebbef7-7469-351f-a4eb-7a81e6a138b1 | -14.11135 | -39.46907 | 2026-01-06 11:36:00 | TERRA_M-M | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 2db3e029-7b53-30fc-9d7c-2e3ca7d9f95d | -8.43184 | -36.93961 | 2026-01-06 11:36:00 | TERRA_M-M | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 0e9e3492-e733-3218-880f-a7732c9de164 | -15.6175 | -39.22658 | 2026-01-06 11:38:00 | TERRA_M-M | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 930f3407-9e24-3d79-ae2f-3e21a49f8f86 | -7.5328 | -37.9143 | 2026-01-06 13:50:00 | GOES-19 | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 102.7 |


