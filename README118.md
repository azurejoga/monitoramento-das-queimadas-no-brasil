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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d0f4ca7-7507-3d6f-bdf4-6205e1fd909d | -2.85273 | -50.48454 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5aeb4c1c-403a-3c87-ab22-3d5c7343ccf4 | -3.50637 | -54.60413 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3a90bc7d-2712-39c6-ae9a-f34e1890afd0 | -3.0944 | -53.721 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 2d418d36-c362-34ad-8a4b-c9123fb16c03 | -3.05446 | -54.21272 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 181a71e6-3f12-3e14-938b-6190a7f29a4a | -7.22989 | -55.1929 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3abb0226-85b1-3940-86f0-527f29e6d3c3 | -4.1603 | -60.78408 | 2026-10-05 17:15:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 4c8019fa-df8c-3fcb-b02e-379cb5440c41 | -6.71203 | -66.49286 | 2026-10-05 17:15:00 | NPP-375 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 63078e06-591d-3fa0-8aba-2152a266bae8 | -3.07733 | -49.54754 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 190014f5-0bf3-35e9-b2ca-d3f15f535192 | -3.27873 | -54.177 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 461576f1-2f1b-33f0-bd37-10e8664efc13 | -6.25592 | -52.84627 | 2026-10-05 17:15:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 954db64e-65ab-3c2f-8cf6-a227c9fa67b3 | -4.91585 | -41.74564 | 2026-10-05 17:15:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| c155ac38-db7a-388d-b065-ecce41d973e5 | -4.86498 | -43.46702 | 2026-10-05 17:15:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5d44ed2a-2c79-386d-9cdf-80f77cac5de7 | -4.20446 | -53.46682 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| de4ad670-731b-33a7-9832-65b470485942 | -2.47423 | -49.40845 | 2026-10-05 17:15:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 083d2802-6566-31cd-911b-d1794a96404b | -3.5868 | -55.40306 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 40bfa970-5c4d-33f1-9a9e-482596ea18ec | -8.61762 | -66.98377 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dea1e605-5192-3400-82ec-02ab238624fd | -7.92384 | -41.10438 | 2026-10-05 17:15:00 | NPP-375 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 62dc7a5e-6b72-3b64-a6ad-d61e821af989 | -3.05778 | -54.21222 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 46c9d2b0-3b7a-33ad-98b9-e69293edbaa4 | -6.82893 | -58.59062 | 2026-10-05 17:15:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a97dd967-1f75-3870-91e2-1e033a70087f | -8.66312 | -54.5407 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 0453a6aa-d4de-3c27-a976-7c8e576fd703 | -9.40169 | -65.89632 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7e036f2d-e185-3080-9174-24a080ae8193 | -6.59728 | -41.58201 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 40.0 |
| e05e66d0-3257-3482-9414-f4dd66f79e02 | -6.79123 | -66.66624 | 2026-10-05 17:15:00 | NPP-375 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 7264ed6b-0114-3a7d-ab8f-d6529e3fb3ea | -3.14101 | -53.72069 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 824eeb9f-4672-37e2-927c-e5ef6a1fd8bc | -4.37068 | -55.42085 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 71cc2923-2b59-3850-a6e0-0e8ffb399e98 | -6.84973 | -41.80192 | 2026-10-05 17:15:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 32.3 |
| e2d487cc-856d-352f-b634-9b17484175c5 | -3.31914 | -53.84214 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0961ae2c-8859-3bed-b60b-8bcbd04e5f51 | -9.88174 | -64.17745 | 2026-10-05 17:15:00 | NPP-375 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ba024bc8-26fb-3aa9-a51f-0a3d17ad98ce | -4.33964 | -44.38384 | 2026-10-05 17:15:00 | NPP-375 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b86a77ce-4d98-3118-9c0e-9b6b09b8bccc | -3.23366 | -54.34679 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 391b1be7-19d0-3028-a184-14616267ba37 | -2.36713 | -44.92566 | 2026-10-05 17:15:00 | NPP-375 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfc806e6-2a72-37fe-ab08-6428a4761317 | -8.53885 | -54.59332 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 91111534-9455-316e-bea1-5387e78b04a2 | -3.04993 | -54.22752 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 349aec45-9c9f-3521-aa3a-6c98be0dffa2 | -8.32484 | -45.4663 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5257536f-f61f-3b14-b942-7535ec830019 | -9.12385 | -65.91332 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 36652b0c-0f95-3e43-85d6-12169525fd22 | -9.34406 | -65.32469 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7b17795e-7b2d-3a1a-9979-7c35a31cb77b | -3.23033 | -53.88398 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 0cb7532c-3711-31dd-8a91-01535c553aae | -4.31114 | -54.69102 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cd5ca1c1-e383-3c5b-bb53-319682faca78 | -7.54681 | -46.72566 | 2026-10-05 17:15:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 14c20053-a1be-34ea-8432-dd67effccf81 | -7.55675 | -66.18762 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5df91089-7ea1-3c06-b3b5-fb25f222a520 | -4.45407 | -54.96523 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0f8fbb4e-11ee-3d3a-8da2-bf97bfc7a280 | -8.89939 | -47.59449 | 2026-10-05 17:15:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9161dfe-cefd-3a76-91b7-c510dfcc29f5 | -8.34695 | -49.72262 | 2026-10-05 17:15:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55b26ed6-002a-364b-98c0-a0a2581cbb99 | -8.52723 | -54.5911 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 750c124c-fb33-3233-8f22-0fdcefe3a249 | -2.78608 | -51.66731 | 2026-10-05 17:15:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 219317d7-b9f2-3c36-b246-f9e1373dd318 | -3.09987 | -53.74117 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 03f0f322-b0e4-3ebd-8190-53c4a18c6720 | -5.89694 | -55.5303 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f7527869-6981-3106-907f-1aae447ef34d | -5.18228 | -42.81627 | 2026-10-05 17:15:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0bbc2d8a-99a5-375f-a702-cad04d4e79cc | -9.11106 | -65.35813 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| e9d7ad8a-c1ac-3001-b2a7-cc15cbc68ea7 | -3.28152 | -54.17305 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a39f7bac-ba0d-3c27-b1b3-aa5ed1a9b06b | -3.52003 | -54.62682 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0c9c977d-1d70-3581-a0a6-13fd2a5cb493 | -3.10159 | -53.73024 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 17831dff-dc6d-3570-9527-b21cce8188f4 | -3.67308 | -55.95316 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| dd1300c4-2782-3921-aa0d-a0e2832fb048 | -9.14569 | -65.54819 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 37691049-ea96-31f6-b58a-02dfd882bc73 | -6.72747 | -44.27485 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| acab2714-a35a-398e-b479-eda2aa8abbdf | -9.79785 | -49.3064 | 2026-10-05 17:15:00 | NPP-375 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2ad497f3-2a1d-3480-bd07-176f7a25a5d3 | -8.42858 | -55.00111 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 775668ab-1353-3a68-92a5-779b7d699de1 | -9.16289 | -45.12791 | 2026-10-05 17:15:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 17c72f44-ab58-3426-88de-530bdfd93023 | -6.32808 | -43.81647 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cc0c325-b667-334a-90e2-a72bce98ff76 | -3.57863 | -55.56126 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f72bdfb6-4bc9-3f71-97e2-d1f8300a603c | -3.09706 | -53.73839 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| ef2e04e5-5235-3c20-8b6d-d9f5f77c8208 | -4.21059 | -53.46232 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e69f80a8-89d5-34bf-831b-40964b690969 | -3.05717 | -54.16573 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fcf4e021-28fd-3e5d-ad04-d5058dcb2a48 | -5.12413 | -43.99382 | 2026-10-05 17:15:00 | NPP-375 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6b3550e4-e298-30cf-8e50-459f30b4d887 | -3.08689 | -49.53011 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e52393af-1d0e-353b-b250-dc659623588e | -8.78142 | -47.55985 | 2026-10-05 17:15:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2ed4e961-f61b-3c7f-b037-14bc422540bb | -4.46076 | -54.96423 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a5ad261f-a40b-39fb-8c55-a38d592eca02 | -6.85147 | -41.79352 | 2026-10-05 17:15:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 10a4d902-6a4f-36a7-8b25-d9edd68d76ca | -4.78845 | -42.57709 | 2026-10-05 17:15:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 5290f58c-238e-319a-a82c-2761c79ab8ae | -3.28484 | -54.17254 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b2d9817-a280-3f14-89f8-457908922560 | -3.23537 | -53.87258 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e9c24fe7-85fe-314a-a4f9-fa527bea039a | -3.98797 | -55.81949 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3210ae13-c07c-3148-b96c-e6434458af22 | -4.13662 | -44.98719 | 2026-10-05 17:15:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a4068e8b-c79f-30ae-92e9-ecd8f7bf8361 | -3.04515 | -53.88827 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ee29c56a-4c1c-3a3c-9f16-8d2f97649067 | -3.5167 | -54.62733 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| cab6f4ce-f638-3930-85ba-47fbe5ccca76 | -4.78762 | -42.57231 | 2026-10-05 17:15:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| ff7da1c1-77d0-3a17-841d-e1ee802383f0 | -4.05566 | -54.03984 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| e1cbc7f4-537b-3539-8c03-c4fb0524f1ea | -3.09248 | -54.1745 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 8117a3d0-4b5d-3a0b-8bc0-6be512e18a00 | -4.11759 | -54.42259 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7cfc1e00-7ccd-3058-afe0-01da9a94ba54 | -9.15792 | -45.12815 | 2026-10-05 17:15:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| afeb2c63-1334-3ae2-8353-74d853d3148d | -9.34054 | -65.84805 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ff9eec6b-831f-3bdb-8c3b-cc9f6c1c3703 | -9.40777 | -65.88954 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7ca91998-51d2-36e2-9473-42524b25d1f4 | -9.30598 | -60.89872 | 2026-10-05 17:15:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ae687e17-5f6a-310c-86d0-dd098df32869 | -6.3281 | -55.71398 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1b58424a-dd43-35a2-8392-d373e28de4ff | -6.72062 | -44.27839 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| c88f1b8f-b0e7-3a87-8323-e85afbc08251 | -8.65458 | -54.5531 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 81888ad2-2f82-30aa-b550-325f9e77a730 | -3.31994 | -43.94603 | 2026-10-05 17:15:00 | NPP-375 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 81bce242-e8b6-3cf6-b01d-6adf43b102d0 | -3.2766 | -50.40646 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0dcb6e41-ed88-393f-a6bb-718aad7a4062 | -3.09558 | -53.71336 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 16a1d1ca-d517-3727-a91a-e23138fd389c | -3.35934 | -43.38668 | 2026-10-05 17:15:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 98142022-353c-39bd-8692-72c4abe62608 | -6.70893 | -45.2271 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dd0c27ee-a598-30b4-b101-45c916f54a53 | -2.67693 | -49.03083 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 39251799-bc29-3c72-b325-a86d6a8c1981 | -3.86187 | -55.97698 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9eeb646a-23d8-3b7c-8f54-192c3e89d6cb | -3.1032 | -53.74066 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 484007f2-81f2-3c3d-9b94-201cd47476a2 | -2.99144 | -51.00648 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| b2d6c280-6c8c-3408-8e79-a7acabb9ec0a | -9.03735 | -45.16815 | 2026-10-05 17:15:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 103d50b2-451c-3fa6-8f3e-9427c1666ba9 | -4.90845 | -41.74419 | 2026-10-05 17:15:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 4adaff89-a701-3ba7-9fec-d98d4d4913a2 | -3.6754 | -55.94532 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 61e43b35-70bf-3d8b-a9c9-b1f675a6cb19 | -3.08026 | -54.18341 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 1e9cfa0c-d297-3f71-b6d1-7a5eb59910f8 | -3.82287 | -41.807 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |


[Clique aqui para ver as próximas entradas](README119.md)
