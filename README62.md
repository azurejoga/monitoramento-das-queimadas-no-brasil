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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2a71932-3ccb-33d8-901c-44b723e32c77 | -7.44975 | -51.82129 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fdfc3b6-b933-3cdb-a9f3-61e6b8dbd3c5 | -7.8495 | -45.39153 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ab68416-a0a3-3846-b17c-44547d507cf9 | -11.68042 | -46.57535 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea5bad9f-0695-3a65-ae5c-e5740533d33d | -8.8846 | -49.9356 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd0deb52-5612-35f5-b4d1-80ebd7f903b1 | -8.89314 | -49.92852 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4773061f-6b72-3e60-a492-98444252eb65 | -7.85286 | -46.06616 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2bfa2407-29f9-3f54-9925-2f75255fe8ef | -5.82348 | -52.33231 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff04169d-e190-36bd-af20-bdbf37976818 | -9.0539 | -47.04546 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd3ede16-cb86-34a9-8da9-ee848a623faa | -9.99256 | -51.72109 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b69f507-2b72-3f99-b707-35e5070890c8 | -6.72573 | -46.90442 | 2025-09-12 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a787f80c-e56a-3cce-b562-64e238b989e3 | -5.1223 | -47.5239 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ecdde61-213a-396d-8a38-90544522fbbc | -10.0914 | -50.39203 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4deb8a20-7fcc-3057-aa90-5339a16ad22e | -11.49348 | -49.27068 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a775aca3-0adf-3234-9bee-43d41dd2bfaf | -11.09634 | -48.40628 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca3db2be-3038-3af8-8b18-2a93280b3759 | -11.90232 | -46.52255 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19fff77d-de10-3d2f-a2f5-e2bcbcc1db4d | -8.17363 | -46.07788 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d10e2a98-1f80-39a6-b675-a668856e6473 | -9.9639 | -51.70016 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d74ab6c-3e6b-321c-8b5e-98b91ea6674f | -7.71991 | -51.07768 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0427f566-6e2c-3bab-8075-d88c3d62df26 | -11.67596 | -46.56001 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da2a88a8-8543-3077-b09c-5f210ff99f85 | -11.86777 | -47.52817 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78292f25-fa58-3ac4-9ff6-5801cf85b0a5 | -11.49703 | -43.64119 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0f58b5a-a21a-34a0-a826-a04a47ecb051 | -6.41825 | -44.50296 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c2a4d35-dcd1-3441-b77f-352902392c53 | -10.42033 | -50.62193 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8ed577b-ea2e-33df-97c7-bab90a58f9ee | -6.83808 | -47.86597 | 2025-09-12 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d42fbe85-b249-3111-8117-604d09b0e2b9 | -11.67598 | -46.58194 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ff89801-10de-32d8-8d4e-69c338993ff0 | -11.19443 | -37.23424 | 2025-09-12 04:25:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 402231da-7802-35df-8de0-9206134ac525 | -7.84601 | -43.88368 | 2025-09-12 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60fb976f-ed31-3c6a-8932-1702f980f224 | -6.26983 | -42.42371 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9dd897ae-b88c-39f8-92e3-9d81048f8b0c | -7.7161 | -50.34337 | 2025-09-12 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3001848-666f-318d-8cba-62d65d46fada | -8.47015 | -47.27674 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4743dd8e-77e6-35e6-89ab-d020d4d23dd7 | -10.65458 | -48.65176 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 790b2563-1431-390d-be0e-e7f721f490b1 | -9.80265 | -47.78323 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb869ddf-cd1b-3b52-9af7-f779848b9fbb | -11.10386 | -51.97803 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97e3dd3a-f6ac-3f89-8a3b-bce5ab3c6083 | -11.69541 | -46.56679 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 81d1013d-c9a6-31fe-92d1-26f8b3940ae9 | -11.53403 | -50.60331 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 24092b75-f06d-3d7a-9a07-159695730a24 | -7.12891 | -44.50293 | 2025-09-12 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b79c29c-5552-3503-bea2-e33264059830 | -6.33985 | -43.04242 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce5c20f2-91bd-31b3-8e5d-c4eb4d4e3b0e | -7.41689 | -50.65091 | 2025-09-12 04:25:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 000fd6e4-72e3-36c2-ab74-a392f95baf43 | -6.40586 | -42.60376 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9c53cf29-1d02-3a6a-9a9a-6a2d14a7ca91 | -6.86505 | -51.96976 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f737d19-1160-3c39-97b8-a9dfe86d8e56 | -6.76751 | -41.59903 | 2025-09-12 04:25:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a902b8c5-165f-30a3-a957-f2acc8a9c697 | -6.42104 | -44.25698 | 2025-09-12 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf4db8f3-dd7d-38db-a818-402aa5bb73a5 | -6.42165 | -44.50352 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cca0b166-f408-3651-abf2-55789a934e44 | -11.66989 | -46.59923 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54afc0a9-ac0c-3058-9719-f5ea2d607842 | -6.30325 | -42.23023 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 1df6fe7c-2cfa-324d-a625-1accdf43c3fe | -6.47523 | -44.01285 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faab1f03-694e-371f-922d-22868c503485 | -11.15195 | -45.31796 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01401d72-4125-3ba8-a2de-2d5e77feb8f3 | -8.16153 | -46.11182 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d5ce32d-7520-3ab9-98b8-68c8d9dd7a56 | -5.94141 | -42.55943 | 2025-09-12 04:25:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 511e9f11-8335-310e-817d-531df8c3b1be | -8.08356 | -50.18221 | 2025-09-12 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| accc8c0f-bfa0-354e-bcec-b47de279c429 | -6.3046 | -42.22099 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fa8932b0-a9f3-349e-95cf-2c3e9cc4c815 | -10.88935 | -45.59261 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6b2fce3-c2ea-3019-a6e1-b471fde267ae | -7.7277 | -44.86536 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98cfbbf9-648b-3060-bebe-ca4f1ff4673d | -5.98471 | -44.72348 | 2025-09-12 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 029d9e27-4384-319b-bd12-d1ab017f720f | -12.12311 | -44.84747 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48618045-be71-3343-b3b5-2e8a347083af | -11.66656 | -46.59868 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24b75839-18da-3c85-9633-2cac75c51b30 | -11.15024 | -45.30609 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f8f5637-679a-32c6-99db-a05e6e5e9c6f | -6.38078 | -43.51244 | 2025-09-12 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5a37232-2935-3353-ba09-36d539a55e4b | -12.24648 | -46.75213 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17c79b02-f99d-3fdd-9b49-df399c5dc26a | -11.18317 | -48.43523 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 65065603-76a7-3a68-8b5e-e4d22901355b | -10.69226 | -48.65405 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79e63a53-9ac2-3bcb-b2fd-e0e40b53be68 | -5.8631 | -48.15325 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a13f816b-fc04-3c6c-b092-b4aab5014ea4 | -10.32152 | -48.80029 | 2025-09-12 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc6e8188-53a1-37df-861f-841e6e7072c1 | -11.69156 | -46.61363 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ec2386d-6fd2-3cbf-888a-d727c40f40e2 | -7.17183 | -48.88501 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 887b24ea-b218-32db-960c-2f5c724cf2f7 | -11.69596 | -46.56322 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3312a721-b777-3960-9883-376f1eef3888 | -6.55807 | -43.95909 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13537e9b-9a3b-3f0c-b8bc-06285302c5ed | -11.98807 | -47.56151 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb6885d4-6f51-3295-a66b-a73e2c4eeb00 | -6.48642 | -43.88134 | 2025-09-12 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d80be085-8730-3172-b6a5-9d5123eea164 | -10.36229 | -50.52121 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 145ec4b4-4900-34a6-91c7-3ec1eaa89c2a | -8.14111 | -49.51625 | 2025-09-12 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eddfdb07-d3ed-3433-bdd2-d999ccc846a7 | -11.48605 | -49.27328 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5154f233-d046-3143-b4d8-0ec4770822f0 | -10.41766 | -49.99594 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c32c73e7-5da0-3f30-8f01-60265c3ea346 | -9.11072 | -47.11531 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e9564ae-5e8f-3bcc-93f7-2605e7c3edc1 | -11.68375 | -46.57589 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e35fe12-2299-3006-9ac6-63aca0aa7e69 | -10.40853 | -50.00687 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 931ade6e-4cc3-32ca-a868-aa45dcbf0a8a | -6.83115 | -45.6526 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 549b8b77-32f4-3df0-980b-0767f06cdf7c | -12.53682 | -44.68951 | 2025-09-12 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1155597-e939-3ba6-bc55-eb2866d1c407 | -9.96879 | -50.38525 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 878b2af4-5bc5-3e1c-81ee-2244d3e554ff | -6.67184 | -44.14705 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 924850bb-8c31-37e3-a676-f4e68af083f4 | -11.19134 | -48.36299 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25607ccf-f2ca-30a6-a189-c1b7a1bc7d3e | -10.1307 | -47.91999 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2267427-5d0b-3fda-93a9-ca9a4cac72da | -6.44627 | -44.07158 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3e8cc7c-51b2-38c5-8ba8-19f63d74b6b5 | -5.11835 | -47.52699 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d835bf82-077c-3139-870d-a9a9d4c20c6e | -9.68297 | -47.55511 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d409899-dfd5-30dd-aaaa-7f36622a5075 | -10.13239 | -47.90943 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2f06407-0651-3d00-acef-45833a3ad29f | -9.06934 | -47.03366 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 337f87c7-d0bb-34be-a943-cee0e5ea12da | -3.82253 | -54.11874 | 2025-09-12 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e13a05b-89be-337f-bc13-77b2f4002f96 | -10.73985 | -48.90279 | 2025-09-12 04:25:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73dac19d-9414-3463-bba1-64c1765f74f8 | -6.82814 | -52.79583 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 084f8d60-52db-38d1-a038-eb3e483a8740 | -11.69373 | -46.55556 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08f7adb1-5dc6-3782-8c0b-3389190e6261 | -9.78465 | -47.85275 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd1927c2-f5e8-3fd8-b982-44c7ec42f127 | -12.00333 | -47.76616 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b28395a-70e3-3202-8d72-2ddccb19ad3a | -10.42244 | -50.6095 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55e89de6-4dce-3dfc-93c8-935f4bd58573 | -8.47347 | -47.27727 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 570c7c6b-57d4-318c-b3d8-3df3e4c53693 | -7.48843 | -54.94834 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cb8e389-ff03-36d9-b9fa-fefe529106c4 | -8.73701 | -47.11547 | 2025-09-12 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb185120-6fc0-3c17-b14a-5b578086df67 | -10.74419 | -48.18329 | 2025-09-12 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 299e9642-b24c-373f-896b-74620375e867 | -11.68543 | -46.58712 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7315c89-cc91-3688-a7d9-0fc5553cf869 | -9.10796 | -47.1113 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README63.md)
