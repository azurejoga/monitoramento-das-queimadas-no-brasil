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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 582bb527-b220-3a95-be21-3a3e9995a0ae | -2.44535 | -47.33105 | 2025-08-30 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3062303-7291-3478-bac7-6ba0780efedd | -6.78553 | -43.78086 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b59a1417-0307-38e8-ab47-3950b32eaba3 | -5.82777 | -46.363 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ba0a547-ab14-3318-aec1-bb7455e0c0c9 | -5.81923 | -46.36663 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e1809338-5824-34d6-9273-a1f268378e19 | -3.62596 | -49.19139 | 2025-08-30 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33282aed-d420-31f4-b871-0929dd6624f7 | -6.00277 | -44.71614 | 2025-08-30 04:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 096ff874-e819-3910-b7d6-11adb49bd3a4 | -2.58622 | -51.92157 | 2025-08-30 04:46:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c44d00c8-0fc5-3ab3-9b1c-fd24fd032f2b | -3.3628 | -43.3719 | 2025-08-30 04:46:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 150e522d-e17e-37b5-860d-bebda5521261 | -4.37426 | -48.06881 | 2025-08-30 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d51d763b-b6d0-33b5-9e1d-47dddf77a7ee | -5.82313 | -46.36723 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e1cf7e63-5f77-3a1b-b6d8-808a822f8d8f | -5.78167 | -42.60082 | 2025-08-30 04:46:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4bf77032-ff41-3be6-acee-b742a495f289 | -3.98536 | -47.88449 | 2025-08-30 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11bd10f6-b0d7-3e5b-aa10-faeef06c51d4 | -3.74022 | -49.04125 | 2025-08-30 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6507ce5-a59f-395b-bd74-85215f62ecf3 | -4.79453 | -47.26556 | 2025-08-30 04:46:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e58bc75-d24b-3dda-85a2-5468dbd172c8 | -6.49267 | -44.39297 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9845815-b121-3c71-8304-8e7a93364c27 | -6.65605 | -43.93555 | 2025-08-30 04:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 690546c9-c4f2-3053-87f4-7220f4c5f45f | -5.88177 | -42.9653 | 2025-08-30 04:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 51664eaa-c49c-3f62-bb50-6a9887d51a0d | -6.80323 | -43.75798 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f822eda7-34c6-3fcd-b611-878f7068de85 | 1.37094 | -50.58361 | 2025-08-30 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b77c400d-d163-3eaa-8269-396090a9353b | -3.7917 | -49.42677 | 2025-08-30 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49b5a3a5-bbf5-38f6-8f79-9403e28616f2 | -5.48029 | -43.51711 | 2025-08-30 04:46:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab749881-a7c5-30a9-914b-8c79aad18e92 | -2.58398 | -51.91364 | 2025-08-30 04:46:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35d11676-06bd-37d8-a6e5-3c984ad3409a | -6.39758 | -45.25241 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e395e438-63ad-394c-9abb-48974d3e3f4a | -5.81998 | -46.36176 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e3977e82-bb64-3c52-ba31-c9c710a9e57c | -6.57028 | -43.68713 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ccab960-f7ce-3362-a635-fda0a7303204 | -6.52255 | -44.86293 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c76fd633-1aa6-354e-9e17-761b535c04bc | -6.42164 | -44.17239 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b25d1d48-8b03-34c0-9b29-fee9eb822578 | -6.17472 | -43.32306 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbd7c9d7-999c-3358-b229-ac5c69f9317d | -6.78153 | -43.77519 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8d6b57b6-bc30-32f8-87c4-c6ae64625dbd | -3.85382 | -48.98592 | 2025-08-30 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 48326c4a-b027-3306-af8f-8516ca82bf3c | -5.61599 | -45.00567 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6402a96c-9a15-3417-94a0-68957103480d | -6.34745 | -44.46357 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 876f4edf-8138-337a-98e2-e7344dd33440 | -6.1787 | -43.325 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 518ecfc7-1fbc-3d1e-8bd7-90165db472ec | -3.07264 | -49.46168 | 2025-08-30 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc709a65-9b83-39aa-8e75-e48ef4dc53e1 | -5.82852 | -46.35811 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1aacc119-bce9-3977-b7b3-e712c29c5e88 | -5.72893 | -43.93599 | 2025-08-30 04:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e17ce9c-b355-367c-96ec-f51c9c217f44 | -6.56408 | -44.22049 | 2025-08-30 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52b150ca-6e5a-33d1-8a66-7012592e7a44 | -5.72434 | -43.93533 | 2025-08-30 04:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db256cac-1eb7-32eb-9cba-89ba58a963f8 | -5.38966 | -51.454 | 2025-08-30 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08f2572f-4298-36e4-9fc3-18cab45e9c0a | -4.41685 | -47.60995 | 2025-08-30 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f638b79-3032-39b2-a335-1b0909ae15ea | -5.75117 | -45.37088 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0df8a177-34d7-3839-87c6-30182c6db117 | -2.89282 | -49.48408 | 2025-08-30 04:46:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0825b38a-b7cb-3f1e-9683-235a23ede95f | -2.34502 | -47.58543 | 2025-08-30 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 63eafb6e-3d3c-3c59-9a23-0bb8d9512b39 | -6.78083 | -43.78017 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a5162df4-06ef-3f45-9336-b121832c110b | -5.87881 | -42.95972 | 2025-08-30 04:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5dbc6cf1-5f87-3e90-8572-92cff61eae89 | -5.82734 | -46.36459 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bd22e557-b6b4-3d7d-a711-188b78d5d50e | -6.4991 | -43.53429 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c3cfc8c-84ea-38a2-96c5-cc17c7a840f7 | -5.88295 | -42.96599 | 2025-08-30 04:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fd8fb303-5eac-3af2-90d7-634b395f7d13 | -6.49757 | -43.54506 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 635b9813-fdcc-3490-8183-2f50fd3d5037 | -5.72186 | -45.53642 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7d940fd-be54-340e-832d-b8173c12d725 | -3.7356 | -48.93782 | 2025-08-30 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3f16ab3-c7f4-395e-9b35-b34412de83a8 | -6.53932 | -43.52549 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 683748b7-201d-32ff-9daa-9b5b96f7c1ed | -6.17551 | -43.31774 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f7bbc6d-d711-3ea5-b9a7-47f2160f2194 | -6.55158 | -44.44043 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b8c357e-1ea6-3767-8a6e-b56a0312ee1c | -6.52195 | -44.86704 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c64a1c85-cd7b-3d82-b250-af36b8e61b80 | -2.4418 | -47.3305 | 2025-08-30 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3faf661a-0932-329d-a02a-84acc476a81f | -5.88077 | -50.2922 | 2025-08-30 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37a11c6f-c31e-3098-8c1c-745da46f7a76 | -3.62541 | -49.19494 | 2025-08-30 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95c04cc0-d8d7-3e59-bd72-23725fbe78b4 | -5.87744 | -50.29169 | 2025-08-30 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9600977a-f042-3314-8440-91332c3e212b | -5.82972 | -44.10309 | 2025-08-30 04:46:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1190ae50-c3ad-3203-a8c3-4a51ccb7a1a0 | -6.17068 | -43.31718 | 2025-08-30 04:46:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5594f848-5557-30c0-b543-26f6703a7c75 | -5.61175 | -45.00495 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 61fbc673-caf5-3d66-8267-e095926d2304 | -6.66361 | -44.376 | 2025-08-30 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 049c6bf5-c253-31f8-9003-ea3ca2def77e | -6.18017 | -44.79005 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78066c02-52aa-34de-b050-b8efcb01c0ce | -2.58562 | -51.92527 | 2025-08-30 04:46:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39f6c307-8aaf-3030-9452-36e765ae15af | -4.3117 | -48.10264 | 2025-08-30 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf5777df-7aad-3b56-99af-987333bd1c44 | -5.61118 | -45.0089 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f64234c5-90da-3d1a-8c31-eeb784dd02eb | -5.42888 | -45.52366 | 2025-08-30 04:46:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1158664e-8471-3186-bf60-8e007969d351 | -3.42171 | -49.0476 | 2025-08-30 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be8f594d-020f-35ff-b1c8-d83a940796c6 | -5.72826 | -45.53761 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3700c49-b29b-3377-a3fb-1cf63440668f | -6.17884 | -44.86092 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bcc095a-a72f-3914-9df8-ad028ac5ef62 | -5.54633 | -42.64429 | 2025-08-30 04:46:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f788a4fa-cdb3-3d80-9e93-64ac51c6f9f2 | -6.16937 | -47.2781 | 2025-08-30 04:46:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac807004-5763-37f8-8e08-b2e0e8f527cd | -5.91619 | -43.42374 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 01263a8b-2d8d-3194-a783-c09bc1285d8b | -6.48819 | -44.39225 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a8aaed6-6ee3-3e38-9c87-a5a2065f284f | -3.21559 | -46.82623 | 2025-08-30 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae63d7f5-b94f-32bf-bb69-acb6b082be2e | -6.21707 | -42.7603 | 2025-08-30 04:46:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9ac5e52e-d8b8-358a-8e93-78482cbf71b5 | -5.9972 | -44.7238 | 2025-08-30 04:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9a0b8977-f5fa-39ec-97c7-fb27a8ff0398 | -3.21925 | -46.82681 | 2025-08-30 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26e2abe4-23c7-397a-b74a-ce2d5a56de91 | -6.39279 | -45.25555 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f2a1851-3ca5-3367-858a-a2ada3f75f76 | -5.87767 | -42.95907 | 2025-08-30 04:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 004a77e2-113e-379f-becc-475051dd2b81 | -6.78483 | -43.78583 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 99ce4939-9d9a-3271-b504-e0516f98a9ee | -5.82416 | -46.35907 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 703d959e-df61-3cce-8bc5-2b6b1c57cc8a | -6.6045 | -43.65025 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c11c9307-0108-31a7-8f8e-e0fda317db5b | -5.96453 | -44.51753 | 2025-08-30 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae1fb16c-5787-3a74-88bc-740dac37757a | -5.81955 | -46.36335 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 09f8192e-2a32-3375-833a-7b3fa3bf7590 | -4.41391 | -47.60532 | 2025-08-30 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4e8ee19-4eb8-3822-87df-7c44df46273e | -2.34151 | -47.58487 | 2025-08-30 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5425f1e-1305-3f39-9b59-6ad079d5d557 | -5.82878 | -46.35479 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d8b75a5-ee3b-3518-8ab1-1a1fb33db062 | -6.6591 | -44.37532 | 2025-08-30 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b43230d0-c392-3d14-8719-7af68575cce8 | -6.17794 | -43.33033 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 2d952cc5-0af2-3119-9583-f90340961775 | -6.18351 | -43.32567 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5863cdf7-d31b-3afa-994e-867ccff8da1f | -3.49051 | -48.94458 | 2025-08-30 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c103fba1-7100-3e0d-b5cb-4a05ad8475e0 | -7.01483 | -42.02945 | 2025-08-30 04:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af6b50ca-9066-37d8-988c-4a55dcb176e0 | -3.62877 | -49.19547 | 2025-08-30 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8802c521-6056-35d1-8079-81b06a79c6a0 | -6.59571 | -43.64413 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ff03ff0c-f60d-38dd-a2b4-b1856c766aa4 | -6.80394 | -43.75298 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 71fd0064-a823-3d89-b157-5c41ece6dda5 | -6.64325 | -44.2517 | 2025-08-30 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 316a2754-8b52-3301-b1c8-e19e71de4a82 | -5.70416 | -45.95714 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00cd950c-1981-37dc-a537-c085e3a67712 | -6.62056 | -43.73922 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README41.md)
