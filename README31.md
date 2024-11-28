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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdead816-f724-3665-b27c-480b0377fbf0 | -8.85721 | -39.87963 | 2024-11-28 03:59:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9737d303-5c45-3e5d-b408-2dd393dbf936 | -1.58495 | -52.26876 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d03eb8d0-c135-3ec8-b0cf-1234d91808a8 | -4.0278 | -46.54191 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ab5804b-f57b-370d-b0f3-cc02c5b3b570 | -3.25234 | -48.88846 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c4e049d-dbff-30f5-8cda-752d48e01ed8 | -8.75159 | -35.55482 | 2024-11-28 03:59:00 | NPP-375D | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ee5c834f-42d2-39e8-91ac-b55e40eae98b | -4.01178 | -46.33232 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4b89acd-a81e-3502-baa5-db912058dd49 | -5.32773 | -35.64244 | 2024-11-28 03:59:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25a6ac40-d83e-31ec-ac82-a9f018b138f3 | -2.10603 | -45.34699 | 2024-11-28 03:59:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94cf6f13-780d-307c-86f0-0a6a5387f0c0 | -3.96381 | -48.08095 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e7675848-ae08-3663-993f-34cf6948fb95 | -2.83709 | -51.83917 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a8cb0e61-8b2a-3be3-aa98-d9014a43c493 | -3.37493 | -50.12084 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf1f4bab-82c3-39da-9017-05f67667b3d9 | -3.78287 | -50.13375 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d4ffcad-2a71-313d-bdd6-1332bda6d047 | -6.71085 | -47.26797 | 2024-11-28 03:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1fefffe-70bf-32c2-9c5c-f5360d07e7ac | -3.05933 | -51.30003 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4089bfe1-e7cc-38d2-b979-b37dd9cc000d | -4.00021 | -46.31567 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a19116e-d2ee-3962-8326-e76e603c1c7c | -6.26965 | -46.2464 | 2024-11-28 03:59:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f6e0bde-ce5f-3bf7-94fe-ca7975d3c34e | -2.65078 | -49.50911 | 2024-11-28 03:59:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25d876dd-6a51-370c-80b9-1ef85dd829ed | -6.37792 | -45.69087 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7648b4bd-e527-31bc-a026-1425b1b75ce1 | -7.43456 | -39.76625 | 2024-11-28 03:59:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dfa980f0-715e-3e2f-b0e6-34715061a7e4 | -2.8597 | -46.85558 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 112e5b15-7708-366c-946a-649bc6b0bb22 | -4.0583 | -46.68221 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02d5bbea-c037-3793-a6d5-ac6afd1fce2e | -3.24772 | -50.76937 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 23514fda-793c-38ff-84ed-5564f1f614c0 | -2.85569 | -46.8495 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 746e55ce-1434-384c-8ff9-8d0877e6aab0 | -1.35027 | -51.98504 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d19df5a2-7d88-3f7c-a52d-487be1b47800 | -2.69306 | -51.68521 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9ad1624-6e59-3266-94f7-428820620a69 | -2.89995 | -51.37413 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d0b88e3-7858-39d7-8bec-fd6de5bbc9d2 | -3.33303 | -45.49995 | 2024-11-28 03:59:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa8a6ce7-6270-36c8-989a-0d70756d41c7 | -3.78164 | -50.1284 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bacb74e5-22ab-3ac9-9311-e46302ed82ed | -2.72475 | -48.89746 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0ade85af-d378-35f9-870d-80b87211be0b | -3.2293 | -48.82022 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5c3f3d1-cdad-3bcd-93ca-056a81e19ab0 | -2.91362 | -51.71765 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c6cbcad-4cf6-3dd3-9ec0-2db7ef0b1413 | -3.53977 | -50.18784 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 944e743a-ae7e-3767-abf8-e3cfdf5acfad | -3.69001 | -50.22561 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b362a23-35f5-3e8d-a1a1-a7153888fdef | -6.48306 | -42.81373 | 2024-11-28 03:59:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd9b886a-6de6-3526-b3ab-bffca2b6f978 | -4.66365 | -49.51954 | 2024-11-28 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ed6a307-efbb-33a1-a86a-03ec1cf4e200 | -4.56986 | -45.40854 | 2024-11-28 03:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25cd69d2-a863-3a01-8089-a6d40cd48ed8 | -2.8655 | -46.85096 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c85ddc15-6821-31d2-8bec-12c424a9afc8 | -2.18565 | -52.13247 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62bc299d-f66d-3b62-9ff6-886ef8758691 | -3.04943 | -48.51279 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 867ebef5-4a2b-3b95-be8a-6a38650bc783 | -4.30106 | -48.21187 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2ddbc64-40a9-3288-810b-fd9a4d791b85 | -3.3096 | -50.03124 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53502c0a-baf4-3d65-8cad-7e39fcf96cc4 | -7.69432 | -42.98344 | 2024-11-28 03:59:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| fd8894ca-1cc8-3d63-ae85-79928e5bcdc3 | -5.39209 | -40.65456 | 2024-11-28 03:59:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 55b65f45-3286-33d1-829c-55084d86869b | -3.97618 | -46.73454 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98d6c537-9fff-3762-be86-7762a36e750c | -4.10604 | -48.25149 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d75ae31e-bf6c-3c7b-8f24-75fb86cbbe45 | -2.83509 | -46.83908 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c7d15d7-9402-30b9-b4cd-f41a84a0f7ae | -7.69141 | -42.97879 | 2024-11-28 03:59:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b1b00b8a-5ab0-31b6-9857-db301f2eb531 | -2.98638 | -51.45269 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3d5f0a62-6c7b-3741-b6c8-227c0b301898 | -2.74851 | -48.66193 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6949a38c-aa57-3916-b0c6-bea361f298e0 | -3.27332 | -50.61666 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28e93fee-9577-36f6-af1b-6171da7c8dbd | -2.58137 | -46.98638 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f522486-4cde-3f13-ac77-c72d5e590512 | -4.04997 | -50.87089 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad71fda1-38eb-335a-8fc3-34bf6a6f787c | -2.87434 | -46.8582 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a830f983-d7b3-31bc-8ad5-79705724e6dc | -6.17297 | -42.61269 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 61d0101f-85c7-3b9a-9cce-7f03cf059345 | -2.91072 | -51.71646 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c84649ce-21e2-3af3-a590-75ede0a3a671 | -3.85963 | -40.44252 | 2024-11-28 03:59:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| faf2e900-55eb-33c0-9b6f-1e3526794298 | -7.69497 | -42.97938 | 2024-11-28 03:59:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 30327c37-01b3-383d-919c-2ee444e76b85 | -6.36658 | -45.69042 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a6b7aa6-d9bb-330f-b1df-15e1fc1a0536 | -4.18285 | -44.26692 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37281589-217f-3bda-92e6-b2bca44fd36f | -3.68554 | -49.57157 | 2024-11-28 03:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7071e00b-8ac4-3a46-a01d-b019be25e0bd | -2.32042 | -51.95876 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea70532f-2326-3c3f-9201-8ee6029439e5 | -7.14634 | -39.74604 | 2024-11-28 03:59:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c73aa176-fe8f-3073-8e2b-0928dfaa8d88 | -2.73287 | -48.89949 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 73d52301-a540-3ddb-82d8-95177ae56bc7 | -1.67158 | -52.7381 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f287506-e62b-3c43-b3a0-291ee660e9f7 | -5.33151 | -35.64302 | 2024-11-28 03:59:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9c7ce735-dd0a-313c-9e13-17d367f4d77e | -3.36989 | -50.8318 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 45d9d11e-060f-3ce6-80be-c7347b9cb135 | -4.35183 | -48.68802 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16278cd5-c596-36cf-adbd-4aa626dac265 | -6.17231 | -42.61673 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 91c0ef7a-c950-374a-8067-eaeddd9da318 | -4.73503 | -46.50627 | 2024-11-28 03:59:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4c0c4ad-22bb-3982-82d4-afbdf538824b | -3.86025 | -38.56623 | 2024-11-28 03:59:00 | NPP-375D | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bb500eb9-9eda-3a2d-9d37-634544d1fcd1 | -3.07986 | -48.6649 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0c31f9f-a14e-34d0-8124-24e6b4a77305 | -3.1018 | -50.36474 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d05b91c-69f0-3235-a46e-0f2ba7b2cf6a | -6.32498 | -41.91768 | 2024-11-28 03:59:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4aa60333-cb03-3717-a18b-89aae8dc3938 | -6.47948 | -42.8131 | 2024-11-28 03:59:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa5b848d-a31f-3fa2-bdfc-b5467ccb4472 | -4.30672 | -48.08283 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f59806f0-9f83-3d52-8a5c-463b4f9a87b2 | -2.16993 | -52.13639 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f1fc56c-dd6e-3449-825d-93d480ec181a | -2.72661 | -48.90241 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6dbb800b-70fd-393a-b8d8-6331011c452f | -3.5311 | -50.75496 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0575b75-879d-38bd-b91d-aed2d615d632 | -3.06433 | -49.20152 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e904229-7729-3921-95d5-9cea0c800463 | -4.15597 | -43.81773 | 2024-11-28 03:59:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee3434e7-38cf-3b10-8433-17aa4c954533 | -3.25381 | -50.61837 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e913ef43-a3e7-33d6-a908-2fb202947988 | -6.37723 | -45.69485 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 39fbc303-d316-358b-9893-e8dac5e5c9dc | -6.17719 | -42.6092 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3823c977-0f58-398d-8b9b-f78f883a254e | -2.74792 | -48.66557 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19f9b4c7-8f4c-3da3-a0f2-c04dd30c1e89 | -6.23878 | -42.98458 | 2024-11-28 03:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3c4f1d7-ffd9-36d8-870c-c4393103aa2d | -5.97536 | -45.36702 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2100bb1-bdce-3dc2-97d0-88a9e9cef64b | -6.17878 | -42.62189 | 2024-11-28 03:59:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c58b7890-2461-316e-95da-ca35598aa99d | -1.69162 | -52.5004 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2876f72e-b688-3df0-86e9-740728a92504 | -3.38532 | -50.32367 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ae62711-a5fa-3605-9f04-18198a5ea2e9 | -6.86922 | -44.75809 | 2024-11-28 03:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82cd0e47-baa3-3dc5-850b-bb98be4c827c | -4.19751 | -48.5641 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e95706e-c3a5-308e-9544-75340cc209b4 | -3.83856 | -46.50089 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e14dd809-5536-37fa-8bf9-268625bd7c68 | -9.00005 | -35.99087 | 2024-11-28 03:59:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 90d80270-9987-3421-8f2e-403701282993 | -2.52454 | -50.10743 | 2024-11-28 03:59:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f1e7396-1073-3ccd-aa90-7a9ac60f975c | -5.98209 | -45.35239 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 063938b2-ed45-3194-8ee9-25637d69b921 | -6.03707 | -40.32501 | 2024-11-28 03:59:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cd085039-d19f-3d45-afd6-4ac9fbd6252d | -2.86459 | -46.85638 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3df38627-84ad-3144-9f72-dd7279572cf0 | -2.44026 | -48.24363 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18f887be-a2d4-3b43-8f1c-e2a5738e89e0 | -3.94369 | -46.72396 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01d88ec5-c800-31b0-b7a4-d735166cf8b8 | -2.65057 | -48.50421 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README32.md)
