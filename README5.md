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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8e476f5-effb-31d9-9391-d8c4930df8fa | -3.47981 | -43.65616 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 335.1 |
| e05a139e-7531-35dd-904c-db94b2241757 | -4.0216 | -45.54631 | 2025-11-06 00:15:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 936be584-5a69-3711-a29f-73c1d93d9202 | -3.93031 | -47.71067 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eab78d95-9502-3948-a700-a587bd77d3d7 | -4.25869 | -45.19768 | 2025-11-06 00:15:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7145de8a-37ae-3a12-b84d-bd5842d1954b | -3.55769 | -50.03154 | 2025-11-06 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d078a9f0-d24a-37f8-be3d-6dddf0ce1cce | -3.38732 | -49.22536 | 2025-11-06 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 95ea43aa-fe76-316d-b0b7-952b8355c9a3 | -2.83039 | -49.64609 | 2025-11-06 00:15:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| db7c4dd0-bf9d-3c58-99bf-cb227d0307b9 | -2.62216 | -49.23642 | 2025-11-06 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0d7a6796-7518-35db-9768-9d89bf8e1e83 | -2.87877 | -45.14931 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6de5e354-0a77-3343-ba33-8db1eef937a2 | -4.58209 | -48.47776 | 2025-11-06 00:15:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| ed54725c-a00a-3bcf-8c91-7ad67f62de89 | -3.38216 | -44.06925 | 2025-11-06 00:15:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 03638a2e-dbee-38bb-a5c6-d9c9a4a8c9e6 | -3.83402 | -44.40131 | 2025-11-06 00:15:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 9bb0a02c-9fa7-3c4c-bf49-959b27b87d85 | -3.4747 | -43.68721 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6d4105f1-1102-312b-b75d-4ab41ee6620b | -3.90535 | -42.55632 | 2025-11-06 00:15:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| e3de8b49-1128-3169-bf1f-c72bd094001d | -3.11733 | -51.19983 | 2025-11-06 00:15:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ce8704ba-810a-3520-b3d9-9f8213fbf9cc | -4.04535 | -46.99351 | 2025-11-06 00:15:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 217.1 |
| 6db660a8-8e25-3004-8e25-c09027e125ec | -2.98145 | -52.81954 | 2025-11-06 00:15:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| b463b78c-7d12-3829-adb8-987651b772c3 | -2.9899 | -52.81264 | 2025-11-06 00:15:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 1e8ed2c6-a8bd-3a4e-9575-173551f81b1b | -4.97876 | -49.59271 | 2025-11-06 00:15:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4e941132-c3a5-3fce-a75b-d9fbdbcc8a57 | -3.00655 | -40.22646 | 2025-11-06 00:15:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| bb44b434-eeee-3857-9083-458726e861bf | -3.96835 | -43.78604 | 2025-11-06 00:15:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 69b2a6d5-ae8f-3eda-8d73-ca23285b64d3 | -3.48916 | -43.6548 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d954f480-ee6d-3e5c-b08f-830b494de516 | -3.23925 | -48.8212 | 2025-11-06 00:15:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0433b168-f252-3228-ae2e-9c0d29b0b988 | -3.39133 | -44.06794 | 2025-11-06 00:15:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 2aab8e1b-3564-388c-bfb9-f5647439df34 | -2.97941 | -52.8367 | 2025-11-06 00:15:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| cc812df5-db32-3194-a781-074dd716b710 | -3.825 | -44.40261 | 2025-11-06 00:15:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3b2a747f-2f83-38d1-a8b9-807e06ba7044 | -3.92324 | -47.7074 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| e7d8b817-56b4-3cfc-8b72-ba7ca324da0c | -4.10344 | -48.02804 | 2025-11-06 00:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 5517f95f-d0d6-36e5-97a5-ca0e9ad47d71 | -4.83232 | -48.58413 | 2025-11-06 00:15:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5b068126-62fe-3417-8a49-54ff85ed1a66 | -3.91629 | -42.98019 | 2025-11-06 00:15:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 76276a0d-935e-3cb0-b9f8-e300b37c0270 | -3.17136 | -44.4062 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c0fc7c25-e6c0-336d-bf69-dc4d28b1289e | -4.59383 | -46.56362 | 2025-11-06 00:15:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fcbd430d-390f-3675-b778-e532be3dfab9 | -4.03631 | -46.99479 | 2025-11-06 00:15:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 152.9 |
| d49a1e48-5437-3cee-beda-a38466776d2e | -3.41916 | -52.77556 | 2025-11-06 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| b25397c7-4fc1-311d-b3df-acef63f7cd3b | -3.41375 | -52.76981 | 2025-11-06 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 27d6e875-1714-32b7-99de-8eb0ea6446f4 | -2.98054 | -48.71273 | 2025-11-06 00:15:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c587b853-602f-3114-bc6d-af00f47079de | -3.46903 | -43.6475 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| f3d7269f-dba2-382d-ae23-879ae73a8403 | -3.04921 | -49.51624 | 2025-11-06 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 700974a9-5b17-3155-9bcd-b101bd510b80 | -3.423 | -54.02028 | 2025-11-06 00:15:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 39007688-d561-3dad-a8b5-a01454bb8889 | -3.14414 | -50.28547 | 2025-11-06 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 81955365-4867-344f-89e1-9bf2d6c11b0c | -3.59064 | -49.44331 | 2025-11-06 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bc907712-8381-39da-89f6-638d05145073 | -3.17007 | -44.3969 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 4ffa2747-3fcc-3584-8255-feccb59dcfe3 | -4.2497 | -45.79809 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1d3019d7-7b73-3701-97d0-f36883e00de9 | -4.04048 | -46.08835 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 25.1 |
| e6762a21-8b6a-3617-9c93-c00b629d8647 | -3.90375 | -42.54502 | 2025-11-06 00:15:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| a67170a8-cf28-3a0b-9c6a-d814eb972bb7 | -2.89548 | -50.48135 | 2025-11-06 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 9339787d-39a1-3463-8c4c-89303c8886af | -3.83617 | -49.81205 | 2025-11-06 00:15:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bd22f797-7860-34f4-800d-f2132003a28a | -4.84376 | -48.59402 | 2025-11-06 00:15:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cc0e5c57-c26e-3c26-80da-c33f7a8d0d1d | -2.92974 | -49.16973 | 2025-11-06 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5e08c512-b5d6-3e32-814b-57e525b6b737 | -4.57227 | -48.47906 | 2025-11-06 00:15:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8054fe8c-1edd-3668-92f3-bde2327ed568 | -3.77887 | -51.67185 | 2025-11-06 00:15:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 1490a03c-8384-36de-a09c-cc0ab5b2b1b6 | -4.23146 | -45.9413 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 921307dc-745b-35ee-a179-ebeefa6c3430 | -3.98492 | -47.29382 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 25e17972-fd23-31ec-b5df-8b0bc8330f68 | -2.99702 | -40.24543 | 2025-11-06 00:15:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 33.0 |
| 8c773392-3219-31cd-9924-82bb136cb04c | -3.72851 | -50.70427 | 2025-11-06 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d6a6d963-ff53-3ec1-8d8a-612049bfbe4c | -2.79196 | -50.31548 | 2025-11-06 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 8d33a101-1dfb-3ae6-ad8a-e52fdb319650 | -3.43389 | -42.55069 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 28e8e9d5-a911-3dc4-9f3d-68082c6eee7c | -3.70224 | -49.90393 | 2025-11-06 00:15:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| fe2910db-4ffc-3793-b158-8b747ee99ca2 | -3.44684 | -50.21996 | 2025-11-06 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1d5fb593-91c4-309c-8804-20d78de343bb | -4.26532 | -45.11549 | 2025-11-06 00:15:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7d897404-cfa9-331d-9522-253e4f7542bb | -3.92187 | -47.69753 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 980cb19c-0a42-3806-bebd-0067a954cb64 | -4.48576 | -45.97766 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de317e50-7df5-3398-995b-cbc3dd26fa05 | -2.45065 | -49.02373 | 2025-11-06 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b1bbf9be-f3bd-3156-998f-8937ca915847 | -3.78348 | -49.43002 | 2025-11-06 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 177.9 |
| 6d265360-6d9c-31d9-b788-060c2336e7ad | -4.37813 | -48.69935 | 2025-11-06 00:15:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8db8f866-9a05-384a-9509-5e173e83249d | -3.4611 | -43.6588 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7cb64d8b-9fbb-3c30-bc06-0d2017038919 | -3.77759 | -51.25431 | 2025-11-06 00:15:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f9d6dc1b-9a2c-39ec-90ca-85bfb8b42dcd | -3.98809 | -47.99842 | 2025-11-06 00:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 810ea902-f025-37c3-af99-4dfb49b936cf | -2.99449 | -40.22823 | 2025-11-06 00:15:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 971e9a84-cb4e-354a-8bc0-192b5d5530c5 | -4.25091 | -45.80688 | 2025-11-06 00:15:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 602c302f-c3bd-3315-ac82-0fb1024ac229 | -3.45391 | -50.0241 | 2025-11-06 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6e797286-2405-36e6-94cc-bf9bfef20730 | -3.78134 | -51.6903 | 2025-11-06 00:15:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1a1525f8-96cd-377d-af91-c22c7c96a5dc | -3.98621 | -47.30329 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| e575c7bc-670c-31ed-9f54-38afb99f86b6 | -3.03889 | -49.51762 | 2025-11-06 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f7411be5-e427-30db-8d03-738af810032b | -3.8938 | -42.54644 | 2025-11-06 00:15:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| bd68887e-768c-3ef0-adff-6fe8308a1d4b | -2.89839 | -53.1278 | 2025-11-06 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0b0d1b37-de62-3402-aedb-dedbd3680743 | -3.92898 | -47.70077 | 2025-11-06 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| c2ae3d72-d9bd-3f9f-a2ae-d461e2f1467d | -3.46252 | -43.66868 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0ba3cf0a-ba38-3e2b-9b51-39faf1bbceba | -3.9123 | -42.97621 | 2025-11-06 00:15:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a17aa52f-af76-34ac-88bb-025510b50369 | -4.98057 | -49.60613 | 2025-11-06 00:15:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8a609c45-5945-35d1-b915-5552ec0ad92c | -4.11292 | -48.02669 | 2025-11-06 00:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 671526bb-aff3-30e6-915e-9ae737fbbef0 | -3.5857 | -46.06588 | 2025-11-06 00:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 98387c0d-ed07-309a-8f85-d5a8bf8ae627 | -3.62854 | -43.54108 | 2025-11-06 00:15:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 05c33259-99bf-3220-b522-ef6dead53897 | -4.10202 | -48.01764 | 2025-11-06 00:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c0dfe0c1-3cbc-3a3a-b023-773fa6e97f04 | -3.47839 | -43.64618 | 2025-11-06 00:15:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 5c7a1701-b0d8-35df-afcd-11307035db21 | -3.62076 | -43.52809 | 2025-11-06 00:15:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cc73a43c-b9c4-365a-9776-7eaf6031f07f | -3.78517 | -49.4423 | 2025-11-06 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| db606470-66f0-31f0-b36b-2be48a5e9725 | -3.44537 | -45.65205 | 2025-11-06 00:15:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| def10a9a-71b8-34e4-85df-ce8d1ed8c036 | -3.62215 | -43.53807 | 2025-11-06 00:15:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| f5faba5f-1bb9-39ed-a426-4160bc9ddd4d | -3.89542 | -42.55774 | 2025-11-06 00:15:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5448481a-0d39-36f2-9126-ec7e0c8b34a0 | -4.84226 | -48.58295 | 2025-11-06 00:15:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| ac3a99fb-dac3-3a7e-bd98-331275d88ca3 | -4.3062 | -50.56881 | 2025-11-06 00:15:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b3404278-fcb5-3919-b0ef-8fd1bc748375 | -3.26548 | -40.02822 | 2025-11-06 00:15:00 | TERRA_M-M | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 5f0fd003-dfec-34bc-a580-d31442337bc6 | -3.4069 | -50.27432 | 2025-11-06 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 7ccd0f35-fd40-392f-be28-8e5a856f6ae5 | 2.61682 | -51.01579 | 2025-11-06 00:17:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 32ddebe5-554c-3e9a-b33b-1d8938db9bc1 | -4.7198 | -46.5384 | 2025-11-06 00:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 109.7 |
| d48e33f0-57ee-37ab-843f-04c396b281dd | -3.4712 | -43.6392 | 2025-11-06 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 265.6 |
| b7501e36-fa11-3128-8721-0a956e2ec2c1 | -4.7012 | -46.5394 | 2025-11-06 00:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 945c607d-c5db-3cb1-b502-99f1bd84aa88 | -3.4899 | -43.6383 | 2025-11-06 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 97bc29e1-88fa-35b2-b143-d1c16b509f60 | -4.7014 | -46.5173 | 2025-11-06 00:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 143.2 |


[Clique aqui para ver as próximas entradas](README6.md)
