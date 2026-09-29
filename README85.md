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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 465ae625-2ade-3f93-a84b-0e4c45a52b95 | -11.8078 | -50.6499 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 87df351d-c9b2-3c0a-a1b5-12ace3289124 | -9.6865 | -58.1062 | 2026-09-29 15:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| b6a980b9-22ee-369a-9991-123b944363d2 | 1.9241 | -50.8202 | 2026-09-29 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e77c26d6-f3e2-3bb7-b0d7-b39a91b2bac0 | -12.2901 | -50.2496 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 14085072-72f7-3689-b7d5-0c3c99b85fcd | -11.7887 | -50.6521 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 45716c2c-6b59-33de-97f3-21afd775d02b | -17.6585 | -46.5355 | 2026-09-29 15:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 4dcc70cd-0e2f-3da0-bb06-0a417b1f667a | -11.9402 | -50.6987 | 2026-09-29 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 9f04bcdc-760f-3a58-8860-6c2071c2646d | -11.9742 | -50.9722 | 2026-09-29 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 7fca64d8-9d8e-3217-b42d-6acecc824bd5 | -11.9551 | -50.9743 | 2026-09-29 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5660a0df-d92b-30bb-9c90-7612dad8bc42 | -9.7051 | -58.1247 | 2026-09-29 15:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 75f8a650-b4bc-3170-96ca-d91a1de6d331 | -15.735 | -46.0384 | 2026-09-29 15:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 220.7 |
| e8b7deb2-03f9-3e62-9f8a-feb0ec188fb0 | -12.2123 | -50.3451 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| da9cc72c-e433-3c78-8e45-19186e427614 | -15.3998 | -47.9261 | 2026-09-29 15:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 0334d307-a891-3baa-8226-07f9120de3c2 | -1.3008 | -49.0826 | 2026-09-29 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 53fbd4c8-7120-3640-93cc-8ced70e73d3a | -11.8608 | -50.9212 | 2026-09-29 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| f84454c1-4ab3-395e-b3d1-1f36e0c7b40d | -9.9266 | -60.7171 | 2026-09-29 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 8dc113da-515c-3230-a078-35ce5b938e00 | -11.7697 | -50.6543 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a3e00a29-7a8a-376f-8118-680c394f6aea | -12.0997 | -50.2297 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 555d6528-e9f8-3049-af45-c118e7390969 | -14.1309 | -46.2801 | 2026-09-29 15:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 834.0 |
| 38d916d3-abf3-3ab8-968f-02cfbf573f80 | -9.1337 | -49.9656 | 2026-09-29 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 3a3a3185-9cc3-3ef9-9de8-5a5e1074d8e5 | -12.2696 | -50.3381 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| c9829131-8197-31c8-abde-ebc86b418779 | -9.4813 | -46.3646 | 2026-09-29 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 83bf1d0a-2735-3eb8-8d4e-94da62eaa17b | -12.0369 | -50.6019 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5859a3b4-2412-364a-a101-fed632e8eb2b | -11.77 | -50.6329 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 6e5fec29-77af-36ed-acba-2bd2ec2e4cc0 | -11.1324 | -50.0839 | 2026-09-29 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a8ef25cb-e315-3b1b-acde-63b736c74a4d | -18.1144 | -44.3988 | 2026-09-29 15:10:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 179.5 |
| bd5a277c-db50-3d20-aa28-1fe1e0333b88 | -3.3688 | -59.4079 | 2026-09-29 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3570bd49-f0b3-3465-83de-e5135aec78e2 | 1.8403 | -55.6244 | 2026-09-29 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 4db8a6f1-f13d-3753-9161-088a46a002e7 | -11.9619 | -50.5251 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b2c2c8d8-58a9-3de9-a17a-c76a73601e55 | -11.1514 | -50.0818 | 2026-09-29 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3b4f1fe1-61f0-3f9a-a575-8cfdb1d28252 | -12.3679 | -50.1539 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 2a53040d-2432-36bb-b9dd-1365abf034e7 | -18.1158 | -44.3503 | 2026-09-29 15:10:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 700b7a2e-8212-3430-a75b-57333fe3c4d2 | -12.0987 | -50.2943 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 954b513e-2a8a-3660-8b08-3991a0c6da9b | -12.1178 | -50.292 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| ae187486-c8e8-344a-9f94-0c54ff0a15d9 | -10.3707 | -61.2513 | 2026-09-29 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0d629127-94ee-3a67-8788-e71381d9e827 | -14.3886 | -52.1 | 2026-09-29 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 130.8 |
| a755c927-1990-3a6c-b5b6-4135a6a20eda | -11.8802 | -50.8977 | 2026-09-29 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 6246b0ff-ab6e-38a7-944f-1e34bd4e7831 | -11.1907 | -45.1274 | 2026-09-29 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 7c00d3b1-304f-3829-9243-952f56859385 | -8.3614 | -45.424 | 2026-09-29 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| c868e81f-dc16-3064-93dc-a836bc43ddfb | -5.13559 | -37.09631 | 2026-09-29 15:12:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c2b54837-bf17-3a85-8620-71f81c6b6c19 | -4.97679 | -37.39134 | 2026-09-29 15:12:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| ff1ae871-2164-37b3-a134-f1cb35e24c06 | -5.13489 | -37.09133 | 2026-09-29 15:12:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 80a605b3-4693-3bf1-888f-c6df31a4758e | -4.15321 | -39.11997 | 2026-09-29 15:12:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 41.1 |
| 1d7f4445-288a-33f1-8577-5f6ba5cec172 | -5.73 | -45.14 | 2026-09-29 15:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f78fdfe1-e1eb-36c2-bbc5-1759237b9a55 | -5.76 | -45.19 | 2026-09-29 15:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa533663-30f4-33af-b0db-ed9e072834d1 | -9.75 | -36.97 | 2026-09-29 15:15:00 | MSG-03 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 2af3907d-5d33-3b11-ba6f-e49288d6a77e | -5.73 | -45.18 | 2026-09-29 15:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42abd187-1917-3d17-8dd3-ca63eb3800a3 | -9.0437 | -49.6317 | 2026-09-29 15:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f5997ff1-5a85-311a-a288-a5a0fca72188 | -12.1747 | -50.3066 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 4b58cb56-923a-3f3d-85c5-67ea8b9a66ba | -15.3807 | -47.9068 | 2026-09-29 15:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| db56342a-bc5a-3bdd-a0c0-2eb50b76c0e8 | -11.8675 | -50.4718 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| d43f30de-390b-380c-a410-99b472594c51 | -11.0101 | -50.6958 | 2026-09-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| b694359a-3c1e-39bb-bac7-309b0269103d | -3.2955 | -59.4284 | 2026-09-29 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 91d2e6da-d315-37d4-ab62-cf0446d38dc6 | -12.0365 | -50.6233 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 3d070c86-e690-3de3-ac23-9b74b266d920 | -12.0175 | -50.6256 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ee96e104-99be-31ef-8021-80fb30bee2ff | -10.2065 | -50.0113 | 2026-09-29 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1dec046e-d771-3898-8b44-74525efe54b7 | -10.8851 | -50.1539 | 2026-09-29 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b42de0a0-b7f9-3a7c-b23b-2d54c0009658 | -20.8369 | -57.7101 | 2026-09-29 15:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 118.5 |
| f91b2305-51cb-3eed-84ec-09d345d58f14 | -12.2894 | -50.2927 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 709f618c-56a9-3e2b-82e2-4c7fac6542d9 | -11.1517 | -50.0603 | 2026-09-29 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| a93adcf7-7088-3c59-ba97-b32727b5339f | -12.0126 | -50.9464 | 2026-09-29 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 66a5870a-1aa9-3f31-84b4-c0170be9fd78 | -12.1027 | -50.0355 | 2026-09-29 15:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 431ed4ee-c296-3a92-9338-1de9262b2f2c | -11.1514 | -50.0818 | 2026-09-29 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 4dc1eaea-be5c-3918-9523-4c04da276084 | 1.8587 | -55.5846 | 2026-09-29 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0a70754a-d78a-34ba-be89-77bc55e21fd3 | -12.1744 | -50.3282 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 74c11c51-59ec-3141-9f53-9cae507bbc67 | -12.8847 | -44.8015 | 2026-09-29 15:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 9193d369-aa5a-3751-b728-9dbae69df832 | -20.817 | -57.6919 | 2026-09-29 15:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 138.5 |
| b7efca83-65dd-348d-a87f-b83fdadb201e | -20.9159 | -57.8246 | 2026-09-29 15:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 132.1 |
| 447a3d6d-cbca-3e59-9beb-4c362f1d8a31 | -10.3894 | -61.2502 | 2026-09-29 15:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 7a039053-fdfa-3af6-b3d0-31fff14c768e | -1.3193 | -49.061 | 2026-09-29 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 0fa7a4f6-17fe-3553-b32c-41e5a64c08c1 | -11.8618 | -50.8572 | 2026-09-29 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 62e4e099-f212-3e81-9064-d275186e609b | -11.8481 | -50.4955 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b76f3947-332f-3bb4-9b26-f772298bee3e | -12.1734 | -50.3927 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 277dbdb7-451e-3d1d-b38e-b1fdb54b76b8 | -12.0362 | -50.6448 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 7913dda0-431c-3d7a-bebb-274c4c66fa0b | 1.9241 | -50.8202 | 2026-09-29 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ca13b85f-f487-39fe-a3d4-2fd090965391 | -12.0369 | -50.6019 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 688da81b-0403-3f48-b466-db306c6558fe | -12.0129 | -50.9251 | 2026-09-29 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| e0953823-7844-32d7-8e10-76133200bfbd | -10.9725 | -50.6785 | 2026-09-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c939916b-0e38-3572-82fc-b5505d191e8b | -12.2901 | -50.2496 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 126e7e60-dfe3-354f-b7cc-29131150a2e8 | -11.8659 | -50.5791 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 91707d06-49f8-3a9a-ab9d-033890beb94d | -11.171 | -50.0366 | 2026-09-29 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 30fe0910-3640-3910-bbc1-9e5655856894 | -10.9912 | -50.6978 | 2026-09-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| eaef17b1-9765-3909-8491-c962645124a9 | -11.8992 | -50.8955 | 2026-09-29 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 29febaad-3a9a-3ec2-b01c-b503b1483db5 | -12.2699 | -50.3166 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1c362737-f869-36b0-9be4-d0a36c4a9561 | -10.1878 | -49.9918 | 2026-09-29 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 5bca9ebc-0155-3388-a076-0cc7164bbf44 | -10.2254 | -50.0093 | 2026-09-29 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 14a04d07-5369-3da5-abf4-0ff4efeaea58 | -6.9795 | -71.7732 | 2026-09-29 15:20:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 122.1 |
| dde533e4-5497-34b7-bf48-5149e6b20a0b | -1.3008 | -49.0826 | 2026-09-29 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 41b2cb88-5dc7-33e7-b22e-76478aac719c | -12.2693 | -50.3597 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c0f62de6-d5d9-3987-bfa5-d6364e8fabb1 | -11.1707 | -50.0581 | 2026-09-29 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 8e0e0a7d-1530-32db-944a-2d83314b7137 | -12.2897 | -50.2712 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| dae82607-2fdf-391c-8332-9410e18e7fcf | 1.9425 | -50.8199 | 2026-09-29 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ce36f31d-49a7-358d-96bd-9fc52af06418 | -15.3802 | -47.9294 | 2026-09-29 15:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a90a327b-c16d-3f73-a0ef-5bd9ee6c65b1 | -12.0123 | -50.9678 | 2026-09-29 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 6901278d-b4fb-38b8-aeae-b63cbbccaeeb | -12.2502 | -50.362 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| fbfea7df-6196-3446-b1e2-757001fe5bba | -11.8799 | -50.9191 | 2026-09-29 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 0b908af8-6af4-3564-ad83-5e081019d89c | -20.6905 | -57.9607 | 2026-09-29 15:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.9 |
| 135d5506-28e8-3552-86be-4ae230125e18 | -11.9231 | -50.5724 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| dd31372c-bc01-3008-abcf-8a0a97d8bc9c | -10.9864 | -49.6915 | 2026-09-29 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 7a19299f-c860-3689-a498-728b3fb34b3c | -11.8427 | -50.8594 | 2026-09-29 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |


[Clique aqui para ver as próximas entradas](README86.md)
