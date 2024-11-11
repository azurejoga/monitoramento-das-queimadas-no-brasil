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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28f89ba9-d139-3406-99e5-31ff5405af89 | -5.9788 | -45.3621 | 2024-11-11 00:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e017da49-d573-311f-9904-5ba65a439042 | -2.189 | -48.3815 | 2024-11-11 00:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| c2b78375-7070-3853-9bd9-03f49a92cc0c | -15.9793 | -59.3267 | 2024-11-11 00:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 1ac90ab5-322b-30d7-9824-9bed8981ea0d | -3.4725 | -43.4074 | 2024-11-11 00:20:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 7fcfc30a-e97f-3a90-a4eb-bfa7cbb29a99 | -3.1458 | -54.4859 | 2024-11-11 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ca5f8295-1d0a-3279-a578-16b6773c226d | -1.2018 | -53.6366 | 2024-11-11 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 18bdcc0d-6c22-3f9d-94ae-f3ef2a31eac4 | -4.11 | -49.1102 | 2024-11-11 00:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| ae3d8623-8301-3913-b4dd-a0253b60291c | -3.1097 | -54.2865 | 2024-11-11 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5cd1e2da-292a-37d8-b074-710767182b48 | -4.1285 | -49.1094 | 2024-11-11 00:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b4983da3-1e65-3031-b358-90e40124649d | -2.2504 | -46.5061 | 2024-11-11 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| ad916102-c9ab-3f82-8037-ab6caca5c108 | -3.0111 | -50.9612 | 2024-11-11 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b9c686b1-2f59-38fd-953e-f3678d7f3570 | -15.9599 | -59.3286 | 2024-11-11 00:20:00 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 211f04f4-09da-300f-a38b-a3cd9601ecb7 | -5.0997 | -45.5344 | 2024-11-11 00:20:00 | GOES-16 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ed066caa-6e62-39eb-baf0-d01cf5684106 | -3.1641 | -54.4854 | 2024-11-11 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 262218c0-348c-383b-a085-011d75989a7e | -15.9788 | -59.3668 | 2024-11-11 00:20:00 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| deb52852-f242-30a0-b43f-947a5b5c1ae2 | -3.0323 | -45.8377 | 2024-11-11 00:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 5452f46e-0622-3c4a-9e90-ae3e4f8558da | -3.1458 | -54.4659 | 2024-11-11 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c5580e7e-6b11-3003-9fbd-9f7941ef4f95 | -3.4537 | -43.4315 | 2024-11-11 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| eb8a7c0c-b355-3b07-8d1d-dfbc88715cd9 | -2.8323 | -49.4325 | 2024-11-11 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 5372c3db-a090-3912-a61c-e65d10774028 | -2.2504 | -46.5282 | 2024-11-11 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 7918a291-2538-320f-91d2-86558b822757 | -3.5346 | -45.7061 | 2024-11-11 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 119.0 |
| fedac8a8-5b8e-3218-a208-6d356a36c842 | -7.4752 | -35.2075 | 2024-11-11 00:20:00 | GOES-16 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 5b13596b-643d-3a2a-868b-f4336987cf5d | -3.5532 | -45.7053 | 2024-11-11 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 55601768-e752-34a2-9efa-d178ba49ef60 | -2.8508 | -49.432 | 2024-11-11 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| bb5a6de4-5e0d-3a69-a7ca-03fd122555f3 | -3.6954 | -50.6262 | 2024-11-11 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| efe13eee-e899-3cbe-8fc0-6ed65d85a628 | -2.4367 | -51.948 | 2024-11-11 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7f6e925b-4af4-3854-a940-47cc6e067468 | -3.32 | -44.0377 | 2024-11-11 00:20:00 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 255ec270-4ab2-3d69-bd6b-60cdfd70e338 | -17.2933 | -57.4857 | 2024-11-11 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 164.1 |
| 4f705723-5ac3-31ba-9646-25cc8637c312 | -3.6859 | -45.2502 | 2024-11-11 00:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 05412cd9-b232-3030-a585-3fd0400f0c70 | -3.2427 | -53.0722 | 2024-11-11 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a54ab7ae-a1f2-328b-9fed-6e8d3d126e52 | -3.0296 | -50.9607 | 2024-11-11 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 1101fe25-ff9b-3903-aff8-c345e7222466 | -2.9716 | -46.9907 | 2024-11-11 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 3bf2dec9-b0d6-3689-a506-87bdcb629e48 | -3.0214 | -53.2404 | 2024-11-11 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c47fa89f-b117-3e31-8fcd-1a1745e43531 | -17.2936 | -57.4652 | 2024-11-11 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| 7cfd742c-2198-375d-9b17-0fd4c2405f12 | -2.4319 | -47.6404 | 2024-11-11 00:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0968280c-9291-3041-a9e2-f60383aab95a | -3.6604 | -50.2081 | 2024-11-11 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 92ba7eea-8651-3e66-9807-7a5ee22669ad | -3.516 | -45.7069 | 2024-11-11 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 1c431d49-5add-3fd6-812a-b56112e3a019 | -2.8324 | -49.4113 | 2024-11-11 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| fc14fd49-349a-3af5-9cba-a22917fdc729 | -3.686 | -45.2276 | 2024-11-11 00:20:00 | GOES-16 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2777ebc8-b840-3376-9a52-61fe6442c1f9 | -3.0295 | -50.9815 | 2024-11-11 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 207.4 |
| 6f82bdc8-6719-320c-9460-c59804d29abf | -4.46729 | -38.75411 | 2024-11-11 00:20:00 | TERRA_M-M | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| e685d6ac-ca9f-3674-bf1c-14b4a71926f3 | -8.9958 | -35.63614 | 2024-11-11 00:20:00 | TERRA_M-M | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| d18b4f07-f9e5-37f5-bb90-01d932534e9e | -4.12664 | -43.58772 | 2024-11-11 00:20:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ee198831-cf1b-3b48-8e67-b064555a40ee | -4.5625 | -44.74796 | 2024-11-11 00:20:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 98c153d5-c9a8-381c-bfb7-f2a8cd5d949a | -5.55173 | -41.65686 | 2024-11-11 00:20:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b8d97635-8385-38a6-a808-e3daea0c2362 | -3.68998 | -45.24668 | 2024-11-11 00:20:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9b292170-81fd-3105-a847-09263a5a987d | -4.12829 | -43.5996 | 2024-11-11 00:20:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38d9289c-58e5-33ac-85cd-6cc850282c6e | -3.68789 | -45.23138 | 2024-11-11 00:20:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 70e8a571-a18a-3172-a46f-e563f579fd42 | -10.69621 | -37.07364 | 2024-11-11 00:20:00 | TERRA_M-M | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 0d7be3c5-9740-38b0-9b20-bc2f8c893281 | -3.67852 | -45.24824 | 2024-11-11 00:20:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8ceced90-0d80-3caf-9583-078e7f608249 | -3.74501 | -45.92104 | 2024-11-11 00:20:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| eba53661-a3d4-353e-ae1e-a2960ab85534 | -5.82182 | -44.12746 | 2024-11-11 00:20:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 3b7eb06e-0550-3be5-b4c8-e8dc9473a445 | -3.53705 | -42.58714 | 2024-11-11 00:20:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| afa51efa-dc7d-3e54-aa9e-7b603cc8ccc1 | -5.37347 | -42.77 | 2024-11-11 00:20:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| bbcb7f01-30c1-3bf1-b081-360076953984 | -3.84911 | -43.80311 | 2024-11-11 00:20:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 20421c8a-9e80-322d-bfa8-2fd51bca1709 | -3.53963 | -43.17742 | 2024-11-11 00:20:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 8e130548-0e20-306a-bb5c-1d7806125434 | -3.73228 | -44.53711 | 2024-11-11 00:20:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e396846f-6aa0-3c7c-af1f-dea37fcd2a68 | -6.98577 | -34.94861 | 2024-11-11 00:20:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| ddbf1b3d-e37c-325d-ba83-fe4a870f9230 | -5.85147 | -38.24665 | 2024-11-11 00:20:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d7f9744f-7ffa-333e-b8de-71ceb9097241 | -4.68113 | -46.37719 | 2024-11-11 00:20:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 21.1 |
| bc558a75-d113-3a0c-8f6a-c52efb115fbd | -8.99756 | -35.64814 | 2024-11-11 00:20:00 | TERRA_M-M | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 8f34facd-ebb9-35cd-9cb5-c40516ddde34 | -5.55304 | -41.66652 | 2024-11-11 00:20:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a5c837c7-4305-389f-9e0c-4057be76d02d | -4.46599 | -38.74485 | 2024-11-11 00:20:00 | TERRA_M-M | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 16.3 |
| f942df0c-33f5-3727-b7d7-ca0d38fcd54c | -3.30862 | -44.03854 | 2024-11-11 00:20:00 | TERRA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| af542c14-c889-389b-b6f1-0ebb07ad2c42 | -3.59506 | -44.554 | 2024-11-11 00:20:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 99309dd2-09e3-36b5-8cbe-815c5c16a082 | -6.73446 | -40.81049 | 2024-11-11 00:20:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 51476a5e-6098-3af5-ba17-f9406210d0d4 | -4.4926 | -44.48295 | 2024-11-11 00:20:00 | TERRA_M-M | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a239dc3e-7013-37a6-8681-b03c4323eeba | -3.74313 | -44.53567 | 2024-11-11 00:20:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7d7e3900-8697-3d42-9922-e110f3e2a02f | -7.09908 | -35.25852 | 2024-11-11 00:20:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Caatinga | 21.5 |
| a46e4d04-cd98-3d5a-a652-181b7248cb4a | -8.46916 | -35.33124 | 2024-11-11 00:20:00 | TERRA_M-M | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 99376115-2ba6-3c6e-b614-8addabc1c029 | -7.09709 | -35.24498 | 2024-11-11 00:20:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| 07db8d41-d73e-3b71-a34a-029324c1b02c | -3.53255 | -45.70257 | 2024-11-11 00:20:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 532139f9-601f-3adb-a216-b20ccd915c36 | -9.65408 | -36.20119 | 2024-11-11 00:20:00 | TERRA_M-M | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 3dfebf47-c9fb-398b-84fa-1dc9d7970046 | -3.45721 | -43.405 | 2024-11-11 00:20:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| ff573639-769f-3ba3-9b77-b51f7d3d1e2c | -3.86745 | -46.0592 | 2024-11-11 00:20:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 2a33268a-4193-37ba-b06d-dcf95a0a09eb | -5.86792 | -39.20996 | 2024-11-11 00:20:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d61f688c-b68e-3db3-b8bc-d6a3aecf3400 | -4.56249 | -44.74171 | 2024-11-11 00:20:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a10d055d-f77d-35f0-8393-3b86290cec39 | -5.48051 | -43.5579 | 2024-11-11 00:20:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 75a1b99f-6454-3fc7-b636-9d6fbb67fab2 | -4.68071 | -46.372 | 2024-11-11 00:20:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 004ac305-3a17-3907-bb10-02e242c2f169 | -3.46872 | -43.41486 | 2024-11-11 00:20:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4aa53e32-6db4-302f-b65a-c8ebbba0fd6c | -5.5602 | -35.58276 | 2024-11-11 00:20:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 80376ec0-f10c-3ae6-ae64-e6925696a9fc | -4.68647 | -46.41663 | 2024-11-11 00:20:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 5f8cb825-5922-3f38-933f-2e8f32310332 | -3.95233 | -46.40494 | 2024-11-11 00:20:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 974c3463-c3c1-380f-a49a-045fb649b4bc | -6.98362 | -34.93454 | 2024-11-11 00:20:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 98a89ed3-47c7-3ed7-a9a5-afe09ed46043 | -3.95535 | -46.41809 | 2024-11-11 00:20:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 045d9126-2b32-32fc-8664-349f86d64a46 | -4.80274 | -40.6931 | 2024-11-11 00:20:00 | TERRA_M-M | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c6f746bf-2426-3371-a5e7-d5a539854909 | -8.99537 | -35.56218 | 2024-11-11 00:20:00 | TERRA_M-M | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 38fff56c-49ba-3966-bc84-b62474b056d0 | -4.08435 | -43.94666 | 2024-11-11 00:20:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 072a3be8-c960-303d-9ddf-2e4f2541881e | -5.94377 | -35.43875 | 2024-11-11 00:20:00 | TERRA_M-M | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6578c0c4-b2b8-3457-a214-b94f05dfdba1 | -4.45695 | -38.74616 | 2024-11-11 00:20:00 | TERRA_M-M | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ec594c65-291f-37e3-8296-e8df632a7959 | -3.45877 | -43.41619 | 2024-11-11 00:20:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 9198a06d-4bff-33db-97de-79c91b5eb0e1 | -4.12879 | -38.70708 | 2024-11-11 00:20:00 | TERRA_M-M | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 45e6fd9e-088e-364a-bcb2-bfa5654e4fe4 | -5.32024 | -43.73135 | 2024-11-11 00:20:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 90b78100-f8de-3dc3-b5f9-adc29a4ed09e | -6.22089 | -37.53742 | 2024-11-11 00:20:00 | TERRA_M-M | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ac05713c-0853-30ae-a95f-7e1ad1a817ec | -6.21677 | -39.40477 | 2024-11-11 00:20:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e9025393-744f-391e-8f1c-4f1a1e418b37 | -3.54028 | -43.56162 | 2024-11-11 00:20:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| dd32ab69-60fd-31ac-bf88-ccd6d984ecdf | -5.56059 | -42.86731 | 2024-11-11 00:20:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 0bc12df0-c66e-35c2-a477-70f8b8e45d43 | -7.10207 | -35.25159 | 2024-11-11 00:20:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Caatinga | 51.9 |
| 2671460e-3356-3e09-b200-0fe871fe3bd4 | -3.69462 | -44.77441 | 2024-11-11 00:20:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f1e2e012-5935-30c5-8294-e9c9a0ecbfc4 | -5.37198 | -42.75905 | 2024-11-11 00:20:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |


[Clique aqui para ver as próximas entradas](README4.md)
