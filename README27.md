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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c4880a0-8fa8-3de5-9a0c-e1a2605df0af | -17.60793 | -57.60352 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6b03aed2-45f4-3b55-a5ce-1141b9bb060e | -17.60613 | -57.58252 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 29f9af14-d481-3b31-b58b-6a21797c0d4a | -17.61716 | -57.61791 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 888ef49a-00d0-325f-9967-21c1cb880c04 | -17.61546 | -57.59701 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b56e0cfb-60c4-37ed-8d13-a3c1707c1220 | -21.1803 | -43.9815 | 2024-11-18 04:16:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c55bfab6-e529-3286-a5e3-5c57d6655db4 | -17.60773 | -57.57459 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 763b3a1c-cae7-361c-9b5d-735e8d106302 | -17.61874 | -57.58242 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| e9699f45-a667-3f4b-92b7-f4231ac54b91 | -17.61611 | -57.59532 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0751830c-2517-3574-afc0-24ba19b951fb | -17.61596 | -57.56642 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 7c9e60a6-d9a7-3e06-b88f-57692c616f1b | -17.61505 | -57.60019 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 77bd10c3-f89a-37ae-9188-2e365cb0f507 | -17.61929 | -57.58069 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 28a97553-9363-3b9c-8308-c37e43b2bd72 | -17.61655 | -57.59214 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 782b164c-2ed4-3a7e-aeda-d7c3bb27fa0b | -24.24154 | -50.74089 | 2024-11-18 04:16:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 683876ac-8a6f-337f-a090-5e913b0d9f5a | -17.61825 | -57.61306 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 30f99222-87d8-3664-ba49-edc9a9ad3c6a | -17.61324 | -57.57919 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| a35efdfd-9916-3540-b088-e1c515b3bdd4 | -17.60473 | -57.61816 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bf2ebc33-e578-3d89-bb77-d9deac3699e1 | -24.96555 | -49.37705 | 2024-11-18 04:16:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 417ce39e-5b52-30e8-8fe3-a42182eb86ee | -17.61268 | -57.58092 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| e8cc4777-8366-32af-9c4b-7174f53beffc | -17.6108 | -57.61967 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7c174e97-dd69-353a-aafa-e9abc347c6a4 | -17.61487 | -57.57124 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 908bae8a-a3e4-32cf-a94c-611104d3f1e1 | -17.61717 | -57.59043 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c2028fa7-4c10-39be-828f-626a212dfdd5 | -22.53738 | -48.81464 | 2024-11-18 04:16:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d2da01e-1347-33c6-9879-2dbaf947d3d0 | -23.40636 | -46.5568 | 2024-11-18 04:16:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 058d8c33-86f6-3dc3-829b-78025a24f1e2 | -17.61378 | -57.57608 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 5a92702d-6a66-3146-8a6b-fd41ada39600 | -17.61437 | -57.60185 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cc4cf558-5fe8-37fb-ad1e-f5ed71b54002 | -19.4368 | -44.34157 | 2024-11-18 04:16:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c5a0621-87a4-3985-adcc-6dff769f4c27 | -17.60825 | -57.57281 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 201d81e8-8cec-3d2c-af3e-6b930fa296cd | -17.60392 | -57.6198 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d3a2c28a-7fa4-3c23-8a65-32bf9a4af5c3 | -17.61218 | -57.58404 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 330ac43e-ddc0-302d-9596-6a6885ffe960 | -27.68386 | -50.89172 | 2024-11-18 04:18:00 | NOAA-20 | CERRO NEGRO | SANTA CATARINA | Brasil | 4204178 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ca993c19-d6c8-32c0-a24c-752c004d332f | -27.57343 | -50.83696 | 2024-11-18 04:18:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 203cb98a-5ef1-3f7d-941c-0906970aeed1 | -25.5237 | -49.27877 | 2024-11-18 04:18:00 | NOAA-20 | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cc9305df-5e31-3e8b-8398-5530b37156e4 | -27.57267 | -50.84127 | 2024-11-18 04:18:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 48e33305-adec-3349-a8bb-56ea6c1ff284 | -27.66253 | -50.8286 | 2024-11-18 04:18:00 | NOAA-20 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d6a4f74d-5acf-3c75-90ca-805eccd2bc55 | -29.60575 | -51.99047 | 2024-11-18 04:18:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 40946665-9e3a-38c3-9d0c-a323be1d777f | -27.65907 | -50.82783 | 2024-11-18 04:18:00 | NOAA-20 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9db227f6-a38e-3e6d-9393-4bd99b99d1a6 | -28.58474 | -49.44084 | 2024-11-18 04:18:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ddbb23aa-8908-3beb-8a61-ca4b67fdb644 | -2.8607 | -51.7937 | 2024-11-18 04:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 0bccb537-e6f3-330d-84d4-1c36179ce8cc | -3.3452 | -50.4917 | 2024-11-18 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f905ae84-ae40-3656-a0c6-195304e0b74d | -3.3116 | -45.6929 | 2024-11-18 04:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 05550f1c-d92d-36b9-a2a0-ce6b4acc0924 | -2.8791 | -51.7932 | 2024-11-18 04:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 7ad4e2f2-fab0-3e9c-bb56-14ce6c498c64 | -1.2964 | -51.7616 | 2024-11-18 04:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2094ec02-5474-3be3-8265-58d1cf8d94a7 | -1.3148 | -51.7408 | 2024-11-18 04:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| b8c08eaf-96c5-37db-a2c0-edd23d1be4b8 | -2.5847 | -51.7181 | 2024-11-18 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f6feddb3-18fd-32ec-8953-6e4676a390d9 | -1.2964 | -51.7204 | 2024-11-18 04:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| bf5813c1-93a2-3051-a40b-ab6c87062041 | -17.6063 | -57.5715 | 2024-11-18 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| 6182f457-2252-32e5-be62-d8b5afd67e5c | -1.2964 | -51.741 | 2024-11-18 04:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 55b2bf56-1d94-3f4c-ba17-0567b062fe76 | -1.2964 | -51.741 | 2024-11-18 04:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 27d3d5cd-41bd-307e-989f-3cb29a9185d3 | -2.5847 | -51.7181 | 2024-11-18 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 7336fd15-c016-33e7-9fed-722a84394d1e | -1.3148 | -51.7408 | 2024-11-18 04:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a51864f4-009f-3600-b334-31a42a930b99 | -3.3452 | -50.4917 | 2024-11-18 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 95939630-8b3e-30c6-9b55-e479d1fe5281 | -17.6063 | -57.5715 | 2024-11-18 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 50d260be-1cec-35d5-b75d-49cdb9e0ced6 | -3.5678 | -50.2534 | 2024-11-18 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 6af42f10-129e-3b3a-ad00-f41362d8cec7 | -17.626 | -57.5692 | 2024-11-18 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| cdd9beba-5e08-3b06-b11a-4be78db53fab | -2.8607 | -51.7937 | 2024-11-18 04:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 18544b26-4375-306a-aca1-dd1832f44d87 | -3.3452 | -50.4917 | 2024-11-18 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 8e16964b-74e8-37fd-af6e-1fc533f9e80c | -1.3148 | -51.7408 | 2024-11-18 04:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5302e856-2792-3b16-8085-077d8d405a2e | -1.2964 | -51.741 | 2024-11-18 04:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| e0b309c0-9594-353d-8b4d-c0a52cc9c582 | -2.8791 | -51.7932 | 2024-11-18 04:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| edd4b4b7-bcfa-3e7d-982a-67625562688a | -3.5863 | -50.2527 | 2024-11-18 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 885ab63a-8073-3425-be10-04c878558c51 | -2.8607 | -51.7937 | 2024-11-18 04:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 0f6ee084-26a5-3a14-856e-fa7fd1d76cdc | -2.8791 | -51.7932 | 2024-11-18 04:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| cba8cd2d-9382-34b2-b5ce-9c5bdb469ff0 | -3.5678 | -50.2534 | 2024-11-18 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6e726039-6f02-325f-9efa-e7194fd088af | -1.3148 | -51.7408 | 2024-11-18 04:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| edc6debd-ce51-30db-a2f7-65ec4a6622d9 | -1.2964 | -51.741 | 2024-11-18 04:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| c3bd577c-5a74-3dea-989e-ccaf9f991d46 | -2.82666 | -46.65674 | 2024-11-18 04:59:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7ce1e4fc-8c64-329a-a709-2baee8273456 | -3.33231 | -44.05275 | 2024-11-18 04:59:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7d6d4212-3063-329b-8f03-07030dfb5fc4 | -1.70037 | -45.81866 | 2024-11-18 04:59:00 | AQUA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 25.7 |
| ac4f7ba8-8388-323f-bf4e-c751d6d394e6 | -7.39958 | -42.76187 | 2024-11-18 04:59:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 8a3123b9-5d36-3b18-8675-f5d12a199413 | -4.94871 | -44.83735 | 2024-11-18 04:59:00 | AQUA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dc94ecf3-a0e2-3a23-a39d-d97984b70cbf | -4.78414 | -40.39964 | 2024-11-18 04:59:00 | AQUA_M-M | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1bc10f79-5a9e-334f-b482-51b89024a12b | -6.3936 | -44.73542 | 2024-11-18 04:59:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ab631a0e-f6a6-304b-b1d5-1daaa6ed6b97 | -4.94744 | -44.84705 | 2024-11-18 04:59:00 | AQUA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 19d4df64-9dd5-3684-9699-f239dd6f480e | -3.16756 | -46.58977 | 2024-11-18 04:59:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 292c555f-3a80-3ae7-87ef-028000eeace5 | -1.2964 | -51.741 | 2024-11-18 05:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| a00c5eb0-2fbc-30d6-9a2b-c73faaab04b8 | -2.8607 | -51.7937 | 2024-11-18 05:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| fcb27891-e6d4-36ed-a828-ad4a74502d4e | -3.5678 | -50.2534 | 2024-11-18 05:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 1ed2ef0e-960e-3279-8b8b-e25b4a07c442 | -1.3148 | -51.7408 | 2024-11-18 05:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d9eb0ddb-0744-387b-a310-33a0f8dc63fe | -3.5863 | -50.2527 | 2024-11-18 05:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 8fb5f220-4adc-3dc5-aaab-08411bd8ce48 | -11.83259 | -47.08597 | 2024-11-18 05:01:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 215d77db-904e-3782-94bc-a820bb50af23 | -2.15941 | -50.70398 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dbc9be1-b739-3000-9a66-b4ce32610516 | -1.07175 | -53.36378 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe3496c7-de50-38b4-b0e3-260cb4661665 | -1.36661 | -51.10595 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3aebd33f-9250-3d88-8a55-b66118e8506b | -2.97743 | -53.85972 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f7259a8-0ae4-3b36-b07d-9678e3e3817e | 0.17067 | -51.26384 | 2024-11-18 05:03:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6074940e-4bf6-3e6c-a363-70cbc0abf746 | -1.44525 | -53.38367 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4045e29-9d20-3758-834a-81775390e5d5 | -3.66283 | -54.65593 | 2024-11-18 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5422b936-45f4-38fe-8a4a-73ec6ff972c8 | -3.10721 | -50.48493 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5b12e0f-11a9-3cc9-bcf6-b4cd2a52ce89 | -3.90401 | -50.08387 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6118092d-8cfa-3d29-83f3-92e9c6c63aaf | -2.74559 | -54.05649 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d60aaa1-2fbc-3969-a31a-af337ce1c5df | -2.57902 | -51.72562 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e66a5c3-31c7-341e-a244-f9eb54d1e69c | -3.18523 | -53.24623 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 59ed6e85-8e9b-3174-ad59-2397d4a3aafc | -3.1451 | -52.9814 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d27cbd60-90d1-3390-8587-4d1167af0cce | -3.3392 | -50.49183 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 98a0e1f7-d255-30f2-a1fa-c5b06b55228f | -1.29631 | -51.73565 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 18f451c7-4920-3410-af64-64491c29818a | -2.50574 | -47.24083 | 2024-11-18 05:03:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65f06bcb-5a95-3c55-8727-c45b0eabc4cc | -3.53374 | -50.2492 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c375f95f-9bce-369b-a9c8-67c64b54b17d | -3.03117 | -54.10364 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9261ecdd-196e-33be-8542-c7f74a0bd8ad | -1.20519 | -51.76521 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28c2c3f8-a508-3b77-afe1-b3540ae7e8bb | -3.045 | -54.40747 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README28.md)
