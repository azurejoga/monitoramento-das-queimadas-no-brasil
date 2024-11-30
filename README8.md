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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f198d74c-ac01-3344-b4c6-6c436d1f4b59 | -2.02597 | -50.75596 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6752016f-53f4-39d1-93d8-8febe08a714e | -2.01689 | -50.77824 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 818e062e-1d3f-3d2e-a1a2-0068db1e1634 | -3.21777 | -54.18808 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 34dc27d6-b4d8-3a49-b9ba-be61934eaaf5 | -1.47822 | -55.38564 | 2024-11-30 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cd3363b9-41aa-3960-80fa-cf433c3d6178 | -1.82817 | -54.5278 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| a9b4bee3-f459-39ae-8fca-dd5993e862d8 | -2.15347 | -56.02655 | 2024-11-30 01:32:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0d0dbe35-f008-35a5-9ec7-9785d9162d02 | -2.01523 | -50.78408 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 566c6a03-b26a-3b20-8b63-68633fd567a4 | -2.03303 | -52.08384 | 2024-11-30 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c0378011-a6e3-321c-a356-e8e15874ecfc | -1.4739 | -55.12988 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1490b646-8c0f-36cc-9305-9b412af6b359 | -2.60772 | -51.80861 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 2acacbc6-df87-3054-9b01-066406705c4b | -2.59056 | -53.97861 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| ce5a4310-4564-3234-baf7-8669c33ac12e | 0.94353 | -50.73303 | 2024-11-30 01:32:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 6caf2406-9ced-3211-9716-cc148ece959a | -3.2498 | -53.61805 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f5a14f88-44d7-3c23-87e4-02e2256fa6f3 | -2.37846 | -54.33723 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5e43405f-ccf3-3058-ba79-813ce1718742 | -2.86529 | -53.98393 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2b6f7f7f-a6f3-33ca-a21d-2eedbb0bef4e | -2.35573 | -55.87739 | 2024-11-30 01:32:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1e5d2235-f9db-3d13-9574-31169550cb85 | -1.32893 | -55.84829 | 2024-11-30 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3779b915-2f18-308b-b08c-912285080bdb | -2.97235 | -53.29685 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d68d7d81-24d7-37f4-89ea-17687df74130 | -3.64465 | -54.44662 | 2024-11-30 01:32:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 42f7ee9d-0396-3bd6-b5d1-0d9710338730 | -2.90342 | -54.17578 | 2024-11-30 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f0990812-fd4d-3180-a4be-b0f76828077c | -3.49748 | -53.81392 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f613aa90-0a5a-3c31-a2c8-9fcf1edd62af | -1.98544 | -50.68146 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| e60110e8-ecee-32f9-9d6d-45bebe9feb04 | -1.71531 | -52.78283 | 2024-11-30 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 7c5c4ef4-0ed6-341c-84f9-7d601dd2f530 | -3.05744 | -54.04319 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3f6fed1d-546e-3562-a0fc-31c9bb349427 | -1.07342 | -53.64522 | 2024-11-30 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| e38a57bd-11d0-3597-9275-147bd8aa3d5a | -3.79455 | -58.9765 | 2024-11-30 01:32:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 7da55ac1-1fb5-3c79-aef3-5f72ff5e8e92 | -3.23685 | -53.93295 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 1e61a5b5-b647-3681-ab9e-9e3f974f1680 | -2.62303 | -54.2211 | 2024-11-30 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 8727db29-b12a-3799-9094-d1bfdc2bb8b1 | -3.11698 | -53.80637 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 29f926d9-d455-30e8-9553-cd876597da52 | -3.49645 | -53.82046 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e6b48a53-a586-3517-9939-aab591751aaf | -2.58983 | -53.98526 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 076297d1-4ff9-3594-9c5d-80afd6f9b8fa | -2.86845 | -53.99192 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 27910a3a-57c1-3cf2-8dd4-8ca20b940b1a | -0.87782 | -51.72609 | 2024-11-30 01:32:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4595767e-3c58-344a-9d35-bd70a8624cb8 | -3.24912 | -53.9255 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| ac151b41-d341-3649-9198-12d768ecf20b | -1.26904 | -54.55101 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 8b9c1101-17a9-3f9b-9ef5-35a59223905d | -2.86637 | -53.97792 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 79eb762f-031b-3aa5-a3ed-25dd55790503 | 1.18894 | -55.97226 | 2024-11-30 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 8ca65494-99c3-33cf-a8cb-c570169308e9 | -3.10545 | -53.81426 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| ea778280-7212-35cf-96a2-ecd07f706a5c | -1.25633 | -54.53914 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5cb68aa6-4653-3cfd-8211-08061dae7f80 | -3.4954 | -53.79992 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 27ebb004-c18f-372f-bb71-43cc11869104 | -1.99394 | -52.08963 | 2024-11-30 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 279a6e72-b31b-3077-b611-dd0317ea0dc8 | -3.24992 | -53.85424 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| db72c33d-4007-3792-abe6-5c6b6f3c2770 | -3.06163 | -50.33749 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 86fef7a1-66c6-343d-ac8d-80d156a2348f | -3.48642 | -53.81539 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| f10c2bc1-9bdd-3ed3-8394-ac71d9aecdcc | -3.45779 | -54.57574 | 2024-11-30 01:32:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 386e61ac-f147-35bb-9e8d-5a2635ac4d69 | -3.35626 | -49.7703 | 2024-11-30 01:32:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 420aed28-1430-3c16-aebd-dc0ac0cd6435 | -2.9817 | -53.36004 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4a74020c-bcd1-30ec-8b71-ff3c7bc5ff43 | -3.15649 | -53.84374 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e2a833c9-c688-3e60-aee1-3531b01e5508 | -3.24284 | -53.64938 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4318f3b3-247e-3b1f-b063-8920f9551cbd | -1.43944 | -55.25807 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| f8145347-53f8-3930-ac67-0a592f6d48c0 | -1.2455 | -54.5406 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b58acd50-2bcb-3411-8fab-89818191245c | -2.89066 | -54.16376 | 2024-11-30 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 446ce239-2b1a-37fa-b965-3f8fdfc40069 | -3.63416 | -54.44813 | 2024-11-30 01:32:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| a6d99d26-364a-365c-81b7-317fa8cae505 | -3.06163 | -50.33189 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| ff2c8cf0-1086-3864-a060-c12758fb3b98 | -1.44289 | -55.20855 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9c7d62ea-fb3b-3136-bcad-57e2fa9772a6 | -1.44296 | -55.13455 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 1d1c8361-10c6-367c-b13d-ff69ee5ff3b5 | -1.06683 | -53.62272 | 2024-11-30 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 82d656ee-d8cc-362f-be5e-8bdb1936e9f6 | -4.19706 | -50.69275 | 2024-11-30 01:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 79bd7752-ba86-3563-8880-281d74337e0a | -1.62351 | -53.8903 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5f7f00be-7358-3c7f-9a35-45c0f5482e6a | -3.26319 | -53.6314 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e10a4199-cdc3-313a-b704-19ab88ae4f76 | -1.42071 | -55.27306 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fc68927a-4c37-3b98-b9fa-185331c38b7c | -1.09262 | -53.38486 | 2024-11-30 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 457434f8-9a9d-3c47-bb96-427a8c3fb9eb | -3.2407 | -53.63461 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b4fc0c38-677b-39a8-9a94-bc7a4d73b9ee | -3.1454 | -53.84528 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 3a67dbe2-8236-3790-a32a-bb19071b2d37 | -1.04149 | -51.74218 | 2024-11-30 01:32:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 95b0c76e-761c-3488-9ac9-5a5c42160aac | -2.96055 | -50.57623 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 5f015704-d138-373d-ae96-7a75a831ea5d | -3.09518 | -50.35447 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| c46886fc-2f58-3aff-bdd1-00c9c76e86ce | -3.39877 | -50.66824 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 6fa9d488-fda7-36cc-a06b-66ec78256e5f | -1.59004 | -52.2826 | 2024-11-30 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 4afd53d8-a2d6-365a-b9a4-47dd6c0d3a55 | -2.03137 | -50.77611 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| eb2a02da-8bd0-3fea-8359-755f84a89e0a | -1.07113 | -53.62874 | 2024-11-30 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 45a21ae0-a3fc-32d8-825a-a0935246c2d9 | -1.35406 | -54.65758 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 22df2e61-6f21-3396-858c-df3542efb58e | -1.44458 | -55.22056 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bd0a435e-e010-3572-b8f6-4eb3e40c1413 | -3.21584 | -54.17471 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 73ee56a0-f8b5-3365-b195-e264ff56dd00 | 1.19581 | -55.99724 | 2024-11-30 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c1927844-152d-3229-9552-8cc7883bd71a | -1.0851 | -53.64371 | 2024-11-30 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8feea661-be50-3d78-bc72-72a4b4fac192 | -3.4033 | -53.02168 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 73012625-74a2-3fe7-8f9f-154f56061ead | -3.12745 | -53.26221 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b14f524f-37f7-35b5-b3be-8917e54815ae | -2.99324 | -53.35836 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| aa20cb98-c4a9-3e8d-9d1f-1a940f2945d4 | -1.06921 | -53.6389 | 2024-11-30 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 843f4f2a-4e77-36e3-8d33-dd194475c1c4 | -3.46464 | -48.91863 | 2024-11-30 01:32:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| e95582a7-76b3-38b3-b19d-7b2d56b2e17e | -3.59897 | -54.42732 | 2024-11-30 01:32:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8ab58d0b-e8b6-36ed-8950-6a596e301b8b | -3.45598 | -54.56322 | 2024-11-30 01:32:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| ae444e42-451b-3f84-b54a-176e2663ef0c | -0.57797 | -51.70025 | 2024-11-30 01:32:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 36.6 |
| b77b76a7-001e-36c3-b731-a0a14ea77f30 | -1.38048 | -53.64032 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 4ad5c4c2-a5ff-3274-bceb-0ffddc6b2124 | -1.25825 | -54.55268 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d97ac239-91b7-3534-aafc-187d54ea9606 | -2.54976 | -55.22947 | 2024-11-30 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f9f8965d-4748-3986-b4d6-f2760ef84c27 | -3.7371 | -51.83169 | 2024-11-30 01:32:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1ac42399-d0ee-3aa2-b9ea-4971e6cd5f67 | -3.45805 | -48.92677 | 2024-11-30 01:32:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 81ed0ab2-155b-394a-9ffe-f4b1ac43e945 | -3.73155 | -54.22485 | 2024-11-30 01:32:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e7d68b6e-c5d9-3fe8-86ff-3091b0ee411c | -2.41572 | -56.4359 | 2024-11-30 01:32:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ca7d239-b4f1-3a03-9415-ea251f3ed7ee | -3.76942 | -50.1805 | 2024-11-30 01:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 46944007-91eb-3bff-b723-72d37c6ff75a | -3.31954 | -54.18033 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 0172d507-85ee-39d5-95bc-8ffbca80a88a | -1.38278 | -53.65621 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| e9195f5b-2228-38b5-bac4-7d8f0ec46ecd | -3.39418 | -50.31741 | 2024-11-30 01:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 39b28ce7-acf0-39de-b50d-e52ce21e8456 | -2.60162 | -53.97699 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9826a26a-bd9e-3940-9919-ba0dc657664c | -3.19426 | -54.3263 | 2024-11-30 01:32:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5e2b4ced-e790-331c-9731-1ebf2a55eeba | -4.20139 | -50.68626 | 2024-11-30 01:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 19be47f9-baa6-3c84-9901-e7d19c5d4548 | -3.73853 | -51.83788 | 2024-11-30 01:32:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 4a79c03f-6df1-335d-bc91-5452a226079f | -3.73345 | -54.23768 | 2024-11-30 01:32:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |


[Clique aqui para ver as próximas entradas](README9.md)
