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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c481384-fae4-33e1-abd1-f9790de5a729 | -19.63916 | -56.56799 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f0c0a74c-a941-3a17-854c-847adab6f07a | -19.63671 | -56.56573 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 60ff06e9-b613-3e5c-b352-db5ead5b570b | -19.59074 | -56.53202 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 059648c6-ae06-3128-ae8c-30240e5ad162 | -19.587 | -56.53145 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7d97fbbf-c23b-397f-9a6b-475c23a57394 | -19.58327 | -56.53088 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 20a12654-e128-3f90-a7cf-e3720b154db6 | -19.57953 | -56.53032 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1d05818a-df85-3f30-9e94-22ab4546e05b | -19.57516 | -56.53444 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0b0ec09b-b26e-3491-9c5d-0604824f61f9 | -21.42541 | -57.24257 | 2024-10-02 05:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 209b81c0-380d-3eb7-8cb8-ef77cdaacfd5 | -21.4211 | -57.24664 | 2024-10-02 05:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6713de85-8452-35c2-9860-faef39012f69 | -21.41742 | -57.24615 | 2024-10-02 05:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7170f98-7d59-3b6b-a771-0b45f5b46b39 | -21.41373 | -57.24565 | 2024-10-02 05:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e51de597-5f4d-3d5c-b85e-acb887a35bf4 | -17.42203 | -57.86071 | 2024-10-02 05:14:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 89302e89-241c-3c87-9673-41155f257239 | -19.13961 | -57.51083 | 2024-10-02 05:14:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 23936a08-86cb-301f-8010-b3a7d454638c | -19.1355 | -57.51422 | 2024-10-02 05:14:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 55bec675-e9a4-3072-9bb6-d2347a60c8b1 | -19.12593 | -57.50508 | 2024-10-02 05:14:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 279e80e5-1b98-3d7a-bc05-50758ae7e949 | -19.11422 | -57.51099 | 2024-10-02 05:14:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2367b6b6-c9ff-333f-81bb-50d94b3eae20 | -19.11232 | -57.49879 | 2024-10-02 05:14:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cfa68f55-a3fa-3f8f-998a-ed241a88d7b0 | -19.11178 | -57.50262 | 2024-10-02 05:14:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7c6cbb27-090e-35ed-9b5f-406ef51e5505 | -19.10996 | -57.48978 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 36c9c79d-0f26-3d1d-a832-b026dce13684 | -19.10936 | -57.49409 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 39c0d520-d106-3264-aac1-17551a710996 | -19.10879 | -57.49813 | 2024-10-02 05:14:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1f885047-fcc8-34c9-aac2-be3fc887ccda | -19.10824 | -57.50197 | 2024-10-02 05:14:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 07c60f1d-9f75-3363-b776-c2efffd6c799 | -19.10643 | -57.48913 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8270970a-42a2-3923-a7a7-ac2f03121894 | -18.71851 | -57.33873 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 71b39955-a3e1-328a-b60a-2213f5bfd063 | -18.71554 | -57.33398 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fca9ab32-0e5f-3aa7-9586-887031f4a1f9 | -18.71495 | -57.33817 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a404af24-3564-300f-b640-8b00e69ceea4 | -18.70131 | -57.33175 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e00a32c8-791f-33e7-8c25-de39cd1b7d3a | -18.7007 | -57.31018 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ad491333-d0ee-3723-9df3-2f7e7da9d147 | -18.70011 | -57.31439 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f49fd99c-0e90-3d6e-a1c5-010214433b2c | -18.69714 | -57.30962 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cf138591-eceb-3873-83c1-fad28d11c4ec | -18.69655 | -57.31383 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 24d9eac5-d2f1-35b9-9061-84ffe21e5cee | -18.69596 | -57.31804 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 46ea8276-65dc-3e67-a524-5d5c4b42188c | -26.74603 | -51.72329 | 2024-10-02 05:16:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0394dc07-2ee6-32af-a3c1-5f276826e2ce | -26.75674 | -51.72797 | 2024-10-02 05:16:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d8121e78-0a86-3c32-8a18-bca8f5cf62ff | -26.75122 | -51.72758 | 2024-10-02 05:16:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a13b9423-ca2f-3b86-b891-e4c7f4796b12 | -3.13656 | -49.42529 | 2024-10-02 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 7c12858d-ed0d-31d5-b00c-234c996000b8 | -3.13474 | -49.42659 | 2024-10-02 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| c133d987-97fa-373f-a7da-1896971e0b8a | -3.12955 | -49.42424 | 2024-10-02 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1d0ab30f-9020-3617-a689-d9bfd213ff72 | -2.96108 | -49.36513 | 2024-10-02 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5adbce6-70d7-3815-aa03-11086f015bdd | -2.95555 | -49.36593 | 2024-10-02 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 42adb62b-7683-3578-afd7-1cf82cdf5d34 | -2.95408 | -49.36395 | 2024-10-02 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ae16852-fdf4-3c3f-bb79-7094fcd20807 | -2.65448 | -54.62205 | 2024-10-02 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d423bc2-dc56-3f8f-9d38-4fc76b74406d | -2.65405 | -54.62495 | 2024-10-02 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02e18085-69aa-377f-8d91-22d8aa292f81 | 2.3114 | -61.28427 | 2024-10-02 05:31:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66f4c099-2259-3ce7-85ea-542743400cf7 | -7.10489 | -71.78977 | 2024-10-02 05:33:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65871437-994d-3c4f-bba2-b98d5fe70883 | -7.21307 | -72.32034 | 2024-10-02 05:33:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a81f8036-9b3e-31ae-99d6-343b18930eea | -7.21359 | -72.31733 | 2024-10-02 05:33:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 156f339d-e858-3a64-b641-444dba2fc4bb | -7.88363 | -71.7206 | 2024-10-02 05:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bc7b2bb-8d44-352d-bc3d-8e99896bed2a | -8.00625 | -71.30364 | 2024-10-02 05:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07b35ad5-025d-3314-963e-4bb1390dcbf2 | -8.06923 | -71.2742 | 2024-10-02 05:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4292c9df-2d91-30f4-8669-369afc4d27c9 | -8.07305 | -71.27996 | 2024-10-02 05:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b1a5e05-5560-39ae-b20f-d63aad8be961 | -7.28809 | -64.65897 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9506243-561a-39ad-a873-3b14fbbea6b3 | -8.80562 | -64.25798 | 2024-10-02 05:33:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42cc9cde-087c-394d-b2c1-e7366383b01e | -8.80286 | -64.25398 | 2024-10-02 05:33:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3f93107-d662-3e03-8f24-6447f80ec793 | -9.2997 | -65.34392 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09b5b18a-74af-3279-825b-40f1e2e19616 | -9.29914 | -65.3475 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1c3f750-4cb2-33ca-b4ce-bcd7402aa2d3 | -9.29857 | -65.35109 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04f205b8-4196-3ee8-827f-25f4fc7a759c | -9.29693 | -65.33986 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4a6d631-ee94-3cfa-834c-96fa14eb6d5a | -9.29636 | -65.34343 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e17b861c-c27b-3c4e-b15f-4cf8cabda194 | -9.29579 | -65.34699 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7726451-7f6e-340e-add4-2d82d588ce2b | -9.29522 | -65.35056 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46e7fbef-662e-3d92-a834-618c9c170e95 | -9.20068 | -64.59624 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09ba5b40-ca29-3c99-8080-99dff28cce59 | -9.19958 | -64.60323 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f552fcc9-c170-331f-b2e8-e0438edfdbf4 | -9.14076 | -65.31436 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7362e44-d7e3-3228-b33b-4b57f7619cd1 | -9.14019 | -65.31792 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be7d1e72-57e5-3110-b7b9-1babd4c8272b | -8.99518 | -64.41322 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91636701-68fe-3a02-86d3-9d35ff49aeb9 | -8.99463 | -64.41669 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33152769-52b0-3dc0-be9d-49426ba146f1 | -8.99187 | -64.41268 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97292980-60af-352f-a461-35215a367ffe | -8.95268 | -64.36007 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 97fa88de-4964-31a1-ad29-c97094832cb1 | -8.95213 | -64.36355 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a162685c-383f-33ec-8046-ef9b6f5b43be | -8.94937 | -64.35954 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f290cb99-5758-30d0-851d-de8756b77359 | -8.94882 | -64.36301 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3842e77-0939-3d35-b47e-391c121858e3 | -9.98539 | -64.76869 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec24e73b-ad21-367e-9bcd-5fca0f89242f | -9.98484 | -64.77217 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7942a97d-5354-3f2e-88fa-8569a88ea1f6 | -9.96994 | -64.78053 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbeaca90-c5b0-3f7a-bbab-a2cf1c1ba03f | -9.96773 | -64.77301 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 221986e9-90e4-3e78-85c4-0b1c863c5975 | -9.96718 | -64.7765 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7767f47-3574-32a8-a15b-3b38a6fae063 | -9.96663 | -64.77999 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3320bad5-6eb8-3f43-91e9-205634687484 | -9.96442 | -64.77248 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b0549c0-02b7-3125-ad5e-d5ea193b2f93 | -9.96387 | -64.77597 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17d36993-2d53-3698-94c5-d0dfae9743fb | -9.96332 | -64.77946 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e454148-487d-3017-b4b0-d0371781093e | -9.89202 | -64.6711 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca0b861c-1a52-3d61-b275-d33d0fda2b40 | -9.89147 | -64.6746 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a09370d-d257-3107-8de7-4d097c3ec6b5 | -9.88816 | -64.67406 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d503651-9c20-3a0c-bb22-a7c7ba6c4a44 | -9.87825 | -64.69386 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74abcbee-5750-33f4-b15c-563f66c86f9a | -9.87494 | -64.69333 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dabbac8-5eab-334a-a73f-1270f86d697f | -9.57443 | -64.40259 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de7650a3-9596-3a02-ab49-f7b690bca33d | -9.47845 | -64.68697 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51643164-309c-3829-991f-4b2dd10c6009 | -9.47514 | -64.68645 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 066a40b9-2243-334e-9cd9-ba5e49195250 | -9.96873 | -64.93822 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0de4cc96-cc73-3f20-a17a-5553706efefc | -9.96541 | -64.93769 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70a350a0-40b9-311e-83a5-8e02b0b80e79 | -9.95109 | -64.89945 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4aa777dd-1799-33d5-b857-0b9187c2e02e | -9.95053 | -64.90295 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 145afb84-b0a3-3626-bb39-0ada50e5dbb0 | -9.94998 | -64.90646 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e4414b23-2117-3091-8f51-980bccd1f399 | -9.94942 | -64.90996 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| daadf982-097d-3aac-b17d-d4aac180627b | -9.94886 | -64.91347 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 98dc70ee-5717-3412-abfc-bd70af08e356 | -9.94831 | -64.91697 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 154d4ab1-c90c-31b7-ba8e-5649815db7df | -9.94722 | -64.90242 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c6eb7d1c-a432-3163-bda5-20c3fb9cbddf | -9.94666 | -64.90592 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2528dc6e-9c23-3d04-92f3-eac3d04b43b5 | -9.94611 | -64.90942 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README165.md)
