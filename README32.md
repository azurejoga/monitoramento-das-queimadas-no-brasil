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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06c60483-a685-3225-a724-4bf7f64cd727 | -3.29512 | -50.36603 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce61cabd-8c0f-37ce-90f4-ab5f04a767ac | -2.22075 | -47.72388 | 2024-11-26 04:38:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f231e91d-5b2f-3ded-88de-05c7209edc23 | -2.80587 | -53.0296 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72f79876-cc00-370e-bf0d-1480cca1a1dc | -2.72024 | -46.28943 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 988b4cb7-9d0b-3341-87c0-a61c60fdf572 | -2.96889 | -48.0041 | 2024-11-26 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d714e5e-d0b2-3f86-aa23-dc3d55ed97ed | -2.8014 | -54.11265 | 2024-11-26 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bd41fb1-1274-33a4-8d26-a3725848921b | -6.3707 | -46.77839 | 2024-11-26 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f8adeab-afe9-3fd6-befc-eb97c689c344 | -4.28922 | -48.55775 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bf8da38-16e6-374d-9883-877c95ea3c1a | -8.29872 | -49.09155 | 2024-11-26 04:38:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f133c130-1278-382f-8787-a08ad5996878 | -3.19238 | -49.05474 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2436c511-1b8d-3c9e-ac6e-3349c7b2eddf | -2.31708 | -48.55299 | 2024-11-26 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cc34334-1a31-3aec-a25d-c0caf7d7533a | -3.22949 | -51.61097 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3e77643-077e-3f88-a1b5-ffaf108894d3 | -3.9773 | -48.08601 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| bd16d057-7d43-3793-a6d8-3af295f3c501 | -2.94531 | -48.5594 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62696fc9-c923-3380-8fc3-47c955751221 | -4.11564 | -48.52026 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0f21359-c6c2-3185-a5a9-497558d7347d | -1.89611 | -53.01144 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc9f6ba7-4b29-363b-92d5-1cd1018e9eb5 | -1.72252 | -52.49148 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff37bd11-42b3-3f0e-94ef-42d91e5433fc | -5.949 | -39.66544 | 2024-11-26 04:38:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e65ea269-f3e3-3395-8b6a-a17b64b489ed | -17.6453 | -57.5874 | 2024-11-26 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 115447bb-0231-3b0d-ba2f-415fa145c044 | -3.3938 | -44.1722 | 2024-11-26 04:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 658a4378-8d27-3068-8870-824406da07ab | -3.1877 | -48.4172 | 2024-11-26 04:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f3d6add4-0aca-32ad-91a5-d4856aee2eb8 | -3.1691 | -48.4394 | 2024-11-26 04:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| cc32c727-5d62-3eb1-840e-c115b523d04f | -6.0862 | -48.0339 | 2024-11-26 04:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 57cb6dea-dc40-30d7-9bb8-5626c12588bf | -4.5376 | -43.2807 | 2024-11-26 04:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| efa34809-3a2b-3b28-8c1e-68b19403702b | -3.1876 | -48.4387 | 2024-11-26 04:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| d3eb1c76-1ca9-3deb-a4b2-3350d57c51a0 | -2.8014 | -53.0227 | 2024-11-26 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a658f2ea-f3f7-3c04-a4aa-d053299cb930 | -4.5375 | -43.304 | 2024-11-26 04:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| a3f39ac5-5d18-3e25-848b-996e7ce6f46c | -16.68255 | -43.88685 | 2024-11-26 04:40:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58412331-36a8-30aa-980c-caa80565fe5c | -9.70545 | -60.14743 | 2024-11-26 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feaa52b1-1a7e-339c-b6f7-2cbb924fa6c5 | -15.17956 | -53.06055 | 2024-11-26 04:40:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f25c44d2-d496-3cf0-bb50-24e0ca5c1a28 | -9.92904 | -59.92775 | 2024-11-26 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af7026d1-d298-38d0-8592-e10096a503ae | -14.31056 | -59.93208 | 2024-11-26 04:40:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35ff4cbf-9732-3184-b8c0-829bcb6f1dad | -13.90232 | -51.63308 | 2024-11-26 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 504ecd54-cb20-3661-b482-d3464914c08d | -15.51983 | -56.49754 | 2024-11-26 04:40:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bf46183-cc32-36fa-867a-d77195e463f5 | -9.70472 | -60.15127 | 2024-11-26 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b934a368-6376-38c3-8158-330a1b54537f | -16.67966 | -43.88537 | 2024-11-26 04:40:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28aba4be-3298-3420-9c58-47a447d9f292 | -16.34818 | -43.69706 | 2024-11-26 04:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e4c278d-3f3d-3737-ab0b-21b58991e0ae | -16.02339 | -57.5862 | 2024-11-26 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30fe22a2-fb09-387d-9644-5cb7401ee1fe | -9.92835 | -59.93147 | 2024-11-26 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32b2cbd4-6e15-3ca8-a8fa-6bef4588daf5 | -19.67611 | -49.89999 | 2024-11-26 04:42:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e00248b-7cb5-3330-a5a6-4b1f9088dddb | -17.6345 | -57.58196 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 598da850-3c8e-3a1c-86bb-d8dcab5f9f96 | -17.63721 | -57.59058 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 044b4f92-5370-353f-aa6f-13ffafd7a084 | -19.62064 | -47.17747 | 2024-11-26 04:42:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 17cfa345-623f-3e17-941a-68e7fc6c030c | -17.63792 | -57.5867 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| dcc38e1a-e2a0-3aea-8db2-2918c84770d8 | -20.87497 | -49.79483 | 2024-11-26 04:42:00 | NPP-375D | NIPOÃ | SÃO PAULO | Brasil | 3532702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8c9ac724-6470-3f0b-adf5-43e6c4ee6b6b | -17.63379 | -57.58585 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1753fbf5-a224-367d-9e10-eb6ab3e96811 | -19.02415 | -57.62373 | 2024-11-26 04:42:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 75d33f92-befb-3407-9385-d9edfe17c747 | -22.54075 | -48.81303 | 2024-11-26 04:42:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 006d8bd7-f99a-388e-9a19-06422363e6e5 | -18.11126 | -51.16663 | 2024-11-26 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f498ac66-f6b9-31ec-a52a-9ec54208c752 | -19.02007 | -57.6231 | 2024-11-26 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| ff81ca9c-c76b-3676-8ae8-a68881140bd3 | -17.63862 | -57.58281 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 18bd486d-e8df-3181-a933-3953b3b22886 | -20.70833 | -54.63861 | 2024-11-26 04:42:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3250dbf9-af7e-3e59-ac23-ef597c77d2d6 | -20.45392 | -44.1785 | 2024-11-26 04:42:00 | NPP-375D | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1331ab5d-6186-33ae-89e6-83e57c8ed333 | -20.90695 | -47.39675 | 2024-11-26 04:42:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bd57a82-5ca5-3ea6-8b07-76b47650f3ae | -18.70879 | -49.3536 | 2024-11-26 04:42:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b5fc1c26-1871-375a-87e8-ee1fd4486f15 | -23.01347 | -50.42298 | 2024-11-26 04:42:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b6d104be-54bb-32d4-ad16-befdde76587a | -22.10198 | -49.61235 | 2024-11-26 04:42:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 87ff2917-548f-3a58-a92e-1e3f0626b4af | -18.11461 | -51.16719 | 2024-11-26 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4a79168-f3b9-30e7-8cf0-e51a64a88c9f | -19.56668 | -44.85374 | 2024-11-26 04:42:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 634f4f07-f3f1-3c9f-9f9f-058908749afe | -23.09217 | -50.91046 | 2024-11-26 04:42:00 | NPP-375D | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1cd37b96-49ba-378c-80e8-eef2319dccf2 | -21.56504 | -54.20022 | 2024-11-26 04:42:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa15393b-fa04-354e-a181-07a0c77d106e | -20.32552 | -48.82811 | 2024-11-26 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a010b119-f266-368e-b9b6-72351e2afffb | -17.64687 | -57.59134 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5b9be272-3e03-3551-bf72-2396b997f489 | -19.54843 | -56.71724 | 2024-11-26 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c9d9d169-9421-3467-94ef-8985e976355f | -19.56199 | -44.85303 | 2024-11-26 04:42:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d37d703-f1cc-389a-b692-704462545c3d | -17.72184 | -54.92945 | 2024-11-26 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef48475e-da0f-3fa5-a44e-a1e93063ec64 | -22.10562 | -49.61296 | 2024-11-26 04:42:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1aaa04a5-2a90-32c8-ad0a-72326d66627e | -18.49899 | -51.39211 | 2024-11-26 04:42:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7796d02e-a7a6-32db-ad8d-f7e59efe5e0c | -19.6896 | -51.28897 | 2024-11-26 04:42:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee01c6d4-dd79-329c-bc45-82cfd4c2f778 | -23.74485 | -49.02078 | 2024-11-26 04:42:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6154120-f652-3e68-b8a9-8d0592a63533 | -17.6476 | -57.58747 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| f1fcccd3-cb5d-32f6-8cd6-9a97ec14a7de | -20.40633 | -48.77097 | 2024-11-26 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d511820f-bd40-3ab0-938f-e6dd1c31b743 | -20.32489 | -48.83276 | 2024-11-26 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d0fdeb4-1b03-308b-a669-a2f774b9845d | -20.47752 | -48.72422 | 2024-11-26 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c08e4b0a-3d6b-3a8e-9cca-7154b6dd0187 | -17.56458 | -57.47572 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 34de633c-0cfe-33fe-8f20-45265a447a32 | -21.31746 | -47.40437 | 2024-11-26 04:42:00 | NPP-375D | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f83e6a43-d430-308c-aab4-9838fbd2dd6d | -20.44895 | -44.17785 | 2024-11-26 04:42:00 | NPP-375D | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8d252f69-1ed4-391c-b766-cf969c53bfad | -20.64296 | -56.58719 | 2024-11-26 04:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80a133f2-8e2f-373c-81cf-8c55d266c991 | -17.64009 | -57.58191 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d0c779c5-9db5-37b7-a658-fce54b6bba5f | -18.11183 | -51.16293 | 2024-11-26 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 938dabd9-0fd6-3585-a6d5-9ebc484a0815 | -20.79684 | -53.55204 | 2024-11-26 04:42:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5216be6-42c6-39de-86bf-94d05f1de0d1 | -22.09834 | -49.61171 | 2024-11-26 04:42:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 808e0ecb-2211-3b66-8a0b-b8daeacd2c5c | -18.39467 | -50.99587 | 2024-11-26 04:42:00 | NPP-375D | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b286c627-5d74-3821-a81c-9096d0c4f979 | -23.74934 | -49.01631 | 2024-11-26 04:42:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fc5c300-d6b9-323c-b4b5-234d97f3c2ea | -20.32181 | -48.82758 | 2024-11-26 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b25eb6b5-1eee-3d40-9c0e-46cd033cf75c | -17.65417 | -57.5527 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9bd3fa23-3875-3db5-821c-da12a7e07b7f | -17.64348 | -57.58663 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 45369665-d83d-3d3d-bd01-fcebb7da760d | -18.25544 | -51.26948 | 2024-11-26 04:42:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 473db3b7-b170-3cda-bbbd-16de0cc5cdd5 | -19.19287 | -52.31932 | 2024-11-26 04:42:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3e88c62-5af5-3fba-ac3c-1ff9dc5fc8b9 | -17.64421 | -57.58276 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 92a9c4c3-63ae-3c73-ad21-c1a80dc2c4c8 | -19.83195 | -44.63935 | 2024-11-26 04:42:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7967b24c-bb3e-3832-a993-d6f9760e417b | -22.87579 | -43.60211 | 2024-11-26 04:42:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c7b0195d-ab9b-3aed-a4c0-c6b69d401e2a | -23.33688 | -46.77175 | 2024-11-26 04:42:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3651883-ea8a-3853-8a57-046d49d0880f | -18.61969 | -51.64563 | 2024-11-26 04:42:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e08748f1-38b5-3a0d-a295-77df705ba904 | -17.6345 | -57.58881 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 04dd54e1-1d53-34f3-be16-b426e320f4a6 | -17.63936 | -57.58578 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5e92db6d-e3f3-37cc-88e4-ebf0dd1492fe | -17.65173 | -57.58831 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 1d2cfdf7-e382-3865-a8f2-3b622a016547 | -17.63597 | -57.58107 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 48eda246-500c-3797-b312-77435e500fa9 | -20.80018 | -53.55264 | 2024-11-26 04:42:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ed20bab-f094-3784-9d0e-f0ec71fd11f5 | -18.70523 | -49.35301 | 2024-11-26 04:42:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README33.md)
