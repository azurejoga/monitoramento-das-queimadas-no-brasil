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
| fae557fe-dafc-3431-af44-9c0f22e63158 | -13.0325 | -62.4638 | 2024-10-16 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 4e200fbd-366b-3be6-b2d9-3d632ac9aa6d | -13.0326 | -62.4445 | 2024-10-16 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6981ecb1-8ae2-32cc-860e-09427ae525f3 | -15.661 | -59.9949 | 2024-10-16 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b6b28f43-b2bb-34f3-a954-2a03e651845e | -15.6612 | -59.975 | 2024-10-16 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 426a63fe-2482-33c7-8370-64078cd03348 | -15.6615 | -59.955 | 2024-10-16 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a6591dd5-3bb2-30d5-8e79-b62ba27b083f | -16.3226 | -57.0662 | 2024-10-16 00:26:38 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 40596eec-c649-31a2-96d4-5aa481c45da6 | -17.2439 | -42.6575 | 2024-10-16 00:26:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3ce0d357-3981-3534-b5e2-f227a6f0c070 | -17.2639 | -42.6527 | 2024-10-16 00:26:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 112.1 |
| d497de4b-6aff-37d2-bfae-37abddb5883e | -16.94 | -57.5268 | 2024-10-16 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| d8704f7c-2241-36c4-9702-5d6f450b0f57 | -16.9403 | -57.5063 | 2024-10-16 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| d1b86cc7-afac-3a44-939b-a07daf75e590 | -16.9707 | -56.8264 | 2024-10-16 00:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| d40037f0-8155-3a20-9134-ec2401444511 | -17.0066 | -58.2934 | 2024-10-16 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.1 |
| 669c4865-39ef-30e9-89ef-677308b1e895 | -17.0262 | -58.2912 | 2024-10-16 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 4b823db0-dace-3a23-9cf3-72eff9acaeb9 | -17.0485 | -56.8581 | 2024-10-16 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 597d66ba-f00b-3580-b3f5-2885e8791114 | -17.0682 | -56.8558 | 2024-10-16 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 730870c4-2175-35ca-a6ae-a353b6ba8403 | -17.0779 | -57.47 | 2024-10-16 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 2b5034cc-ea48-39a7-bccd-f38cac3c365f | -17.1754 | -57.4995 | 2024-10-16 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 2da565d1-5225-3490-9614-cef1c0931550 | -17.1758 | -57.479 | 2024-10-16 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 3f65bdc4-9978-32a0-b396-757ddda119fb | -17.1951 | -57.4972 | 2024-10-16 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.6 |
| f29ce354-8ea4-3317-b91e-21b49deca21a | -17.1954 | -57.4767 | 2024-10-16 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 71d5349c-55b3-3db5-b8ee-0165afb13b8f | -17.2157 | -57.4334 | 2024-10-16 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| e6aa3ef1-a46f-3519-ae85-70854692f16a | -17.2177 | -57.3102 | 2024-10-16 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.3 |
| b55aaf2e-e8a6-36f7-97a3-54f1206afb34 | -18.2544 | -56.5821 | 2024-10-16 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 236.7 |
| d52a6223-5d7e-37b3-806b-640c61a325b9 | -18.2548 | -56.5613 | 2024-10-16 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.8 |
| d489c002-213b-348e-bc14-cd8e05b820de | -18.2742 | -56.5795 | 2024-10-16 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 185.2 |
| 77ead64f-9945-3f70-9eb9-b2370184063a | -18.2746 | -56.5587 | 2024-10-16 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 01a7b6e7-1106-34cb-a51f-b919038c0139 | -19.5615 | -56.968 | 2024-10-16 00:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 157.8 |
| f482400b-8c00-3775-a876-e0d4e4de8d35 | -19.5619 | -56.9471 | 2024-10-16 00:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.5 |
| eac14cc5-b316-3aa9-9d70-9a760992e82b | -19.5816 | -56.9653 | 2024-10-16 00:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 168.9 |
| 94b3d309-fb81-3b4a-ba8b-778eecfc02f8 | 1.0016 | -52.2164 | 2024-10-16 00:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 54.4 |
| be7f2fdb-3354-3ac5-bd88-c3a6e98fe82f | -3.1098 | -54.2464 | 2024-10-16 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| b89bd6eb-0847-341e-b675-846f34d2d263 | -3.1099 | -54.2263 | 2024-10-16 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 01e0d0ac-b3ce-385f-bbbc-8ea0ec3e2bd0 | -3.11 | -54.2063 | 2024-10-16 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 7abb6b6b-dc33-3454-89fc-b4a684519228 | -3.1282 | -54.2459 | 2024-10-16 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4478a7a0-d4b7-3d79-8f96-1a2d9f9cee4f | -3.1283 | -54.2259 | 2024-10-16 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 7991a6ce-b57d-3e39-8a4f-3f0109f46962 | -3.2225 | -48.9306 | 2024-10-16 00:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c25b0b97-5c23-3e6b-9562-5e355c1cd44b | -3.2226 | -48.9092 | 2024-10-16 00:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 6d5f87d3-ff29-376a-ada0-81666e3225f9 | -3.2695 | -50.9327 | 2024-10-16 00:35:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 6c5c6e29-62f8-3ce7-a28e-3e843cf79e8a | -3.2879 | -50.9529 | 2024-10-16 00:35:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8d929521-f823-3b15-9a81-e59bae7f8e1b | -3.288 | -50.9321 | 2024-10-16 00:35:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 96908365-eecb-38f9-a28b-15307cce2f98 | -3.4104 | -44.5599 | 2024-10-16 00:35:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| fc84e77d-3281-3352-b17b-bd6e1570e63e | -3.5107 | -43.2429 | 2024-10-16 00:35:26 | GOES-16 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 7aa03892-c81e-37d7-96f2-a11acf279606 | -3.958 | -46.4442 | 2024-10-16 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 96.4 |
| cd9ce5ca-1268-3e79-a341-be76c6fec14c | -3.9581 | -46.422 | 2024-10-16 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.1 |
| ba9ba403-e4d5-3673-8693-45f85ea1225d | -5.2306 | -47.9566 | 2024-10-16 00:35:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6a3a6d1a-59bb-3ded-8752-e6d5ecb6688c | -5.5178 | -46.9109 | 2024-10-16 00:35:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 6bcf30bc-e04c-3f45-b5d5-d22d1f3ccee3 | -5.5179 | -46.8889 | 2024-10-16 00:35:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 189.3 |
| da0e7c2d-b7d5-31c0-ada1-c26f8e653650 | -9.1328 | -47.0054 | 2024-10-16 00:35:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 45e15a76-d863-33b0-8597-180fec9d2619 | -9.1331 | -46.9831 | 2024-10-16 00:35:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 574778b4-64f2-313c-8a33-0c762514b632 | -9.1706 | -47.0014 | 2024-10-16 00:35:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| be692877-e374-3f09-a4c1-b018a245f831 | -9.1727 | -65.4132 | 2024-10-16 00:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| d79d3cd4-1664-3a2c-980b-eca018e3badb | -9.1728 | -65.3945 | 2024-10-16 00:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 1edd8ac2-8416-3396-ae8b-b63fd15b9061 | -10.145 | -36.1406 | 2024-10-16 00:36:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| eb43f08d-1bd0-3dd9-a49d-6bd70d8df77f | -9.9588 | -47.3816 | 2024-10-16 00:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 5f9e9551-2b00-3260-8b76-490b11d3fd3a | -9.9777 | -47.3795 | 2024-10-16 00:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 48080b3a-6bb0-3b0e-b99c-3c0f64ff73da | -10.2628 | -47.3024 | 2024-10-16 00:36:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 19dbdf1c-8edf-3512-80c5-0a2692281a6e | -11.6915 | -65.2432 | 2024-10-16 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8b697035-df3f-3a11-980e-4568719c27f2 | -11.6917 | -65.2243 | 2024-10-16 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 4c4244b2-9efb-33fb-bdab-6dc90486d61a | -11.6918 | -65.2054 | 2024-10-16 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 28cf13c9-b404-3327-b1bd-80fb08cc7231 | -11.7103 | -65.2424 | 2024-10-16 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7b7cb40a-54c9-3cef-8309-3a638eab6294 | -11.7104 | -65.2235 | 2024-10-16 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 19cabe1a-47d3-3cef-bb10-457140a3348c | -11.9381 | -64.8729 | 2024-10-16 00:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2ce57b7e-a006-33d1-96bb-521072988c17 | -12.004 | -63.5199 | 2024-10-16 00:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 79fe48f9-ac1e-35c1-bb88-51a6f8841735 | -12.0041 | -63.5008 | 2024-10-16 00:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 39b57576-7a39-383f-bd21-dab2c9b42f13 | -12.0228 | -63.5189 | 2024-10-16 00:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9fa973c1-2496-38e7-af31-2e65ce0505f9 | -12.3795 | -63.7103 | 2024-10-16 00:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 5d915d0d-d0d2-30e4-b573-46e861895cef | -12.3982 | -63.7284 | 2024-10-16 00:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 8438c2b0-d16c-340f-863a-d77eb0f4c23f | -12.3983 | -63.7093 | 2024-10-16 00:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 167.2 |
| c5a059db-12d7-3dcc-a7f1-6b70cce46130 | -12.4979 | -63.034 | 2024-10-16 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| b1ce1720-f027-3a55-b823-1d95177b3326 | -12.4981 | -63.0148 | 2024-10-16 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| bf8d62c0-71a7-3a38-be93-12e6312ee8e6 | -12.5149 | -63.2822 | 2024-10-16 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| abbafb7c-b3e5-3f5d-8776-528770e55963 | -12.5168 | -63.0329 | 2024-10-16 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 14ada0af-d913-3b97-8788-1ae67769bda4 | -12.517 | -63.0137 | 2024-10-16 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 1a39f6b0-f727-30a4-9eed-d2370b8c45ed | -12.5338 | -63.2812 | 2024-10-16 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 1ed87f64-e8a8-3844-9561-eec33ef58527 | -12.5339 | -63.262 | 2024-10-16 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 950fab8b-5cd4-30e8-ae03-f6e73619f571 | -12.5527 | -63.2801 | 2024-10-16 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4ea3ddb5-de9c-3c4c-8f8d-8fb03c33b87b | -12.8607 | -62.6092 | 2024-10-16 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 10bebb1d-e3ba-3f65-9430-27cf476008d1 | -13.0325 | -62.4638 | 2024-10-16 00:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 2ea56af8-1e82-30ed-bb04-1c95f24ac624 | -13.383 | -46.947 | 2024-10-16 00:36:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f4ff2a99-f9cb-3782-bf17-92a647accbce | -17.2439 | -42.6575 | 2024-10-16 00:36:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 89214181-e242-3fe4-b8e4-43a733de8f98 | -17.2639 | -42.6527 | 2024-10-16 00:36:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 625fb369-98f9-366e-8282-73ae12ccd287 | -16.9707 | -56.8264 | 2024-10-16 00:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 574606d2-60b1-3fcd-857b-c52a1184e1b2 | -16.9711 | -56.8058 | 2024-10-16 00:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 742d9757-47b5-3fbe-b864-6dafe9783bef | -17.0063 | -58.3137 | 2024-10-16 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| daf70671-d991-3313-b305-7f65f41d48cd | -17.0066 | -58.2934 | 2024-10-16 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 229.4 |
| b37ba2ca-4ff7-3f83-bc4c-6d5033c40a7a | -17.0258 | -58.3115 | 2024-10-16 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.3 |
| 59019fae-8a65-3571-b284-22684fe3c44a | -17.0262 | -58.2912 | 2024-10-16 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 317.8 |
| 2ac9c2fb-b364-3a7f-9f03-1e7c5d14274c | -17.0265 | -58.2708 | 2024-10-16 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 82915ebc-1eb2-3af5-93dd-7eb56c70591b | -17.0682 | -56.8558 | 2024-10-16 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| c17f0d42-f2b5-30bc-9256-77f66f165932 | -17.1754 | -57.4995 | 2024-10-16 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 0329cfe0-da24-325c-97b6-648c24a58065 | -17.1758 | -57.479 | 2024-10-16 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 436de993-898c-37c0-abdf-63cb81a65c7e | -17.1951 | -57.4972 | 2024-10-16 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.7 |
| cfa75abc-5907-306e-bc79-2748d2757986 | -17.1954 | -57.4767 | 2024-10-16 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.8 |
| df8c63f8-0cf1-397d-9a86-8dbac95c56fc | -17.2081 | -56.6946 | 2024-10-16 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 8646e705-6a98-394e-a14f-330452b0a967 | -17.2157 | -57.4334 | 2024-10-16 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| f50511bc-f721-3cd6-9894-91fd5792807a | -17.2177 | -57.3102 | 2024-10-16 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| f082d89e-2d78-37bd-bb32-beb6200a44af | -18.2544 | -56.5821 | 2024-10-16 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 247.1 |
| 4c21dfda-b4e9-3434-bfc0-fe181bb53523 | -18.2548 | -56.5613 | 2024-10-16 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.2 |
| 7572aa32-b486-3d42-be8f-9aa422bd5f9f | -18.2742 | -56.5795 | 2024-10-16 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 212.4 |
| c1e007d5-fc2a-30c3-97a4-1b937a6a40cd | -18.2746 | -56.5587 | 2024-10-16 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.4 |


[Clique aqui para ver as próximas entradas](README4.md)
