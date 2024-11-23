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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 810b155a-2b42-315c-b354-4162cc2b81df | -5.94705 | -38.32587 | 2024-11-23 04:18:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 05ef7779-671b-35da-9432-a86d3a93b379 | -3.23189 | -54.25551 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da0024e-f19c-3c07-8584-9e68dee1db75 | -4.24361 | -48.69973 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c00a6c84-ab42-30ba-9d59-ee44791ab752 | -4.41816 | -44.11985 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcd4a3f2-9d78-3a1b-8fef-1cab3b4c1a37 | -5.39387 | -46.10698 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae1dec63-97ed-32fe-9d19-70ff017f4389 | -5.92937 | -44.72895 | 2024-11-23 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67687839-6592-3f49-b832-d70a1c780e70 | -6.40052 | -39.12197 | 2024-11-23 04:18:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5771eb1f-f211-3e32-bd33-849204fea76a | -5.46738 | -46.1749 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44bcd9c8-9bee-355d-a35e-468a99cdc16b | -3.08511 | -53.26376 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c445fb6-e840-325a-b5fd-0b16fe85e827 | -5.44321 | -45.58446 | 2024-11-23 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 451083df-e5a5-3ead-8855-b0807ce6c1a4 | -3.11231 | -51.19958 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f88983ba-f477-3f57-8fa0-19069fe16c9e | -2.81059 | -54.03109 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db05bfff-7c23-3265-b6cc-7270566ff68d | -5.75131 | -46.26055 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4759fd7e-00cd-36a4-97a2-034fe6cc6e9e | -5.12858 | -47.03242 | 2024-11-23 04:18:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 57ef0029-8920-3bfb-b88d-773b3c86b76c | -5.98074 | -45.39152 | 2024-11-23 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bea31e7-3ecf-3181-aebd-e5687f94f517 | -4.60924 | -46.49636 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3f15128b-c2dd-3403-b7be-12f0aca5fdae | -3.12215 | -53.10487 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| aba13dfa-1ec2-3649-9939-1b1794555ca6 | -10.57762 | -36.98403 | 2024-11-23 04:18:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 66b15203-73ce-306d-a069-68e8d243b6de | -7.01679 | -39.22155 | 2024-11-23 04:18:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a95808ac-3da8-35cb-b36d-c8e5b69bf6a8 | -6.84289 | -44.38448 | 2024-11-23 04:18:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b128b7a-31f4-3d0e-8ebe-efa4b3056d83 | -6.48293 | -47.50557 | 2024-11-23 04:18:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39a22c26-fe36-3343-b37f-6cd9a27a229e | -6.22385 | -44.82177 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1b7b4f0-822e-3425-ba10-7a380696e5c6 | -3.89048 | -46.66644 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76e9c211-b765-3c30-bb85-eb29aa00e640 | -3.25421 | -54.23339 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa91190c-df09-3272-86b0-6ab672d9119d | -4.36825 | -48.5023 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d70d0ef2-dceb-3da5-bb1a-d558f599dfed | -4.28626 | -48.22038 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6df9c2cc-de6d-3d33-9a0f-b8be06d8c7dc | -3.22681 | -54.25042 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08ffd428-b49f-3054-8249-3c7a3c7c2a00 | -3.11401 | -53.12099 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d120607-6aea-3267-8835-bee027f10b23 | -3.25139 | -54.24971 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61c22ea5-5df9-3e97-be96-3a185d25e1ee | -5.4634 | -46.17799 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c632db5f-b14c-3972-8493-b6ec4a07ccdd | -3.77751 | -46.66999 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 167a140f-9f97-30e2-b9d0-7bbba65f3c01 | -4.41485 | -44.11934 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f0a1b6c-3b50-36cc-a72e-89bac79027ec | -3.66046 | -51.57291 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 581a9598-c910-3dcc-991c-94122134c84c | -3.23328 | -54.24715 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5671af57-0940-3b7f-9e6f-1a82e4c4e1c6 | -6.06335 | -44.69707 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef7a257c-942b-39f4-96dc-4a72e0a4c254 | -4.70763 | -45.81294 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6d7f349-10d1-30ef-8277-bfdcfbbcf4bb | -4.23839 | -48.63351 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93e4ac73-01d4-39f5-8d1b-a4723fb25860 | -4.12265 | -43.23031 | 2024-11-23 04:18:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49de2585-3592-3c2c-a3dd-eef5681432f9 | -3.76062 | -49.93877 | 2024-11-23 04:18:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9b7de77-8eee-3834-a5e0-2caa7ae75a54 | -4.1113 | -42.47131 | 2024-11-23 04:18:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 364d15b9-8f58-3b43-8f2a-ab6f27a7c948 | -3.90111 | -47.94222 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d598f8c-4db5-373d-956e-ed7596828006 | -4.72686 | -43.25206 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a60852c-2d5c-3a3c-b972-e1e98e6ebb78 | -3.24456 | -50.12446 | 2024-11-23 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| df19c50f-dae3-342c-b4ca-27d3fbe5b6f0 | -5.46568 | -43.2433 | 2024-11-23 04:18:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57e8dba9-111b-32cb-a125-c2d18ed5c1c5 | -6.30324 | -46.77849 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c70915-ee3d-3ed2-a63d-63d73ad47239 | -3.90183 | -47.93777 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ac65964-25a7-3b47-a82e-14ebd3a23e50 | -3.25052 | -54.22051 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e43cb9a-9954-31c7-b45a-b6c124682c76 | -4.17733 | -48.63597 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3492fd4-f8f3-35ca-9655-0938320a7301 | -4.08977 | -47.02765 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0d92772-4611-3b54-a2e8-9f67706c324d | -4.83904 | -48.6423 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19c4d28f-0602-3c05-8142-e7f3b818397b | -4.39067 | -40.76363 | 2024-11-23 04:18:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02fd8328-2f2d-326e-923d-55c6e3579746 | -3.23766 | -54.25644 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6bec95e-ceaf-3dbf-8042-9faa64d114fb | -4.02813 | -42.19215 | 2024-11-23 04:18:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dfc92eec-3b92-3703-9899-794fc944ef77 | -3.25489 | -54.22948 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 47ed8f30-773d-30f6-a89d-83d8115d3903 | -5.18764 | -46.14547 | 2024-11-23 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d70ca5d-2100-3ca6-9808-3bbd7b27680e | -6.14269 | -46.68317 | 2024-11-23 04:18:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ddd0ee77-b9f5-3fdc-8bdd-119f9b8bff1b | -4.67274 | -45.6636 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6c17589-fe51-3335-8aef-3e1b6657eaa1 | -3.22174 | -54.24527 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09f3b46d-ef4c-34c2-b7bc-2bd943c9d8e9 | -4.22693 | -46.16691 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e8cd8d3-8cf9-38c8-b589-673f28b82c45 | -5.52691 | -45.78392 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90477619-6060-3d93-bfc2-94b05981d3a8 | -5.46733 | -43.23269 | 2024-11-23 04:18:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dcfa55e-cd60-3e85-8bfc-50a1e949026a | -4.72754 | -45.49328 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ef7b04c-ca27-3e72-9bc8-494371a67cb4 | -4.69451 | -45.85182 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 50c0ab52-9ad0-3b48-8606-901de6568111 | -3.67162 | -51.73855 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8522e293-6c87-3bdb-850b-d70076fec110 | -4.16193 | -43.82613 | 2024-11-23 04:18:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae6e0380-928f-37bb-a595-5fba16580032 | -3.48515 | -48.25324 | 2024-11-23 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61506728-e855-31c1-b084-05f8ce42d12b | -3.48348 | -48.2508 | 2024-11-23 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e0cd046-ce3d-3341-a896-f57dd2a0c907 | -4.60804 | -46.50391 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 4746aad4-0639-3e99-ba64-354478c3c228 | -3.46815 | -48.24812 | 2024-11-23 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9c0e8c51-9881-3f8a-bfba-bb81b6cc7ef5 | -5.14837 | -45.81956 | 2024-11-23 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a8cb4b5-7848-3376-8471-d57d13b214cd | -5.56419 | -43.30888 | 2024-11-23 04:18:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a4ea38e-03f0-3792-9214-4ca1e75883e1 | -6.13976 | -44.73067 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14d8573c-5069-3d09-b2cf-d0a8fbae1600 | -4.1547 | -44.28326 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd3c2435-13e0-3c61-9d12-a3d2f17a40a8 | -4.38967 | -45.80451 | 2024-11-23 04:18:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e10b3a-55ad-3c98-b8e7-62c14f9f7fcc | -4.69303 | -44.40339 | 2024-11-23 04:18:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f572734e-2431-3364-92bc-c00d67492a32 | -5.23059 | -45.10813 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9a47802-b43d-3d27-bded-ae438cd5aedf | -4.1232 | -43.22681 | 2024-11-23 04:18:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13916f35-e842-342f-b761-bd7210dd8336 | -3.75265 | -50.01618 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aeacb0e-4d26-3fd3-b182-d22bc1e2c29b | -4.422 | -44.11692 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 15a230ab-e2f1-3f44-8a4e-21e3672e38ae | -3.23258 | -54.25139 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8611b37b-682e-31d8-9927-b27f8651a7bd | -3.67449 | -47.13842 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3881a56a-327c-34bb-8335-a62002373d2e | -4.69054 | -45.85495 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 028b74e8-c64a-3e9b-a20a-66a14b0f8acb | -6.22715 | -44.82228 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afe3df14-fa76-3a28-844f-2b383fbd7a01 | -4.06691 | -46.8307 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c38f76f-53c3-3fbc-926d-c65400d437dd | -3.17396 | -54.31729 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 472b910b-1311-3327-9d05-2172e387d54c | -6.50001 | -47.04007 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f1a0810d-a734-3033-8fc9-4f810f540c6b | -6.32721 | -46.03477 | 2024-11-23 04:18:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7fe03f9-4dce-3fc3-a5a5-8dea912689e7 | -4.76103 | -44.10017 | 2024-11-23 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f13a9ac7-661d-3730-8790-877e1b4ae8aa | -5.66575 | -42.97691 | 2024-11-23 04:18:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ff555bf9-2502-35bf-9b5e-3940f2355fa8 | -6.06036 | -44.04541 | 2024-11-23 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0de328a-b42a-3920-bb5c-e82a83065e97 | -4.19988 | -46.81432 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 05bcf2d1-ec18-3ce8-9b89-cfc416657819 | -7.64277 | -40.38879 | 2024-11-23 04:18:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae92d727-52ab-3ba4-bd4e-83d152c4c63f | -4.58521 | -46.07402 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb31963f-110b-3412-8905-9c92c03b56ec | -5.42108 | -42.58632 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1671a2d8-b6c7-3f69-84fa-689bf79a2f51 | -7.31196 | -44.94421 | 2024-11-23 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e69b29fe-b8ef-3a70-8f08-b92e5e6deb83 | -4.00258 | -47.91496 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fcedb4a-d9e1-3c54-ac27-a60d9f79e2cc | -3.22638 | -53.93941 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70318290-a948-33a1-9c2e-ed5c219c6430 | -3.216 | -54.24418 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f7a83c7-09fd-3143-99f4-d2082612f137 | -4.69579 | -44.40735 | 2024-11-23 04:18:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40841627-6284-33d8-8a25-c64c17e4b6d4 | -3.96916 | -49.93391 | 2024-11-23 04:18:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README44.md)
