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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99c43360-e7ce-3ebf-97c4-16329c36991a | -5.50044 | -46.3754 | 2024-09-27 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 213e3e1e-0043-38e9-8dc1-4da2d517a93d | -5.75974 | -45.80185 | 2024-09-27 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcc34b28-2a41-350f-8b53-6d18995630ea | -5.75913 | -45.80538 | 2024-09-27 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 610e963b-6ce1-3281-a0cc-c75dd74c2c68 | -5.75373 | -45.80453 | 2024-09-27 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e073653-a223-37b5-9f65-f2cd387e1ffd | -5.75312 | -45.80802 | 2024-09-27 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18b9d696-b967-3ce8-bb3c-6f88814aba85 | -5.74769 | -45.80735 | 2024-09-27 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2318d7f1-c9e3-382b-b217-d1273e240d2f | -5.57994 | -46.15227 | 2024-09-27 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44282f9a-d613-320f-92a2-2af8059e22b5 | -5.57932 | -46.15578 | 2024-09-27 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a858a552-c450-3cdc-a44a-995dc6b2892a | -5.42286 | -45.47797 | 2024-09-27 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a2bc0346-a26b-3a4b-afc5-ffd23cca4989 | -5.42205 | -45.47551 | 2024-09-27 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b0856f2-e8e4-3a8a-8de3-d3f1797c73bb | -5.42146 | -45.47881 | 2024-09-27 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ad3a92f-ceaa-3e1e-bcdd-1d2d5f749abb | -5.41756 | -45.47705 | 2024-09-27 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d459556d-1490-3905-a84e-435864d02ce4 | -5.25022 | -45.9623 | 2024-09-27 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e78ffb0d-087d-35bc-954d-560f6b433b85 | -5.23964 | -45.4412 | 2024-09-27 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fffbfd17-b6a0-39bd-b154-5944fc64ef49 | -5.23908 | -45.44442 | 2024-09-27 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c70b2b21-f41e-3596-a48f-94247aa45947 | -5.23851 | -45.44766 | 2024-09-27 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1786ebd5-826d-3c0c-9b6f-c812c36378fe | -5.23434 | -45.4403 | 2024-09-27 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc9733fd-4d93-3acb-ad0e-0e833b4a1c12 | -5.23376 | -45.4436 | 2024-09-27 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33d8bdfe-01f3-3231-a09e-c0ca3356ef88 | -7.60067 | -46.36477 | 2024-09-27 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb754cd0-8592-3110-adf9-d45ab3af03c8 | -7.59525 | -46.36382 | 2024-09-27 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a44a7be3-c099-3bba-afee-848d15346dc5 | -7.27894 | -46.6115 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d98f1d47-019a-334c-9e93-489de874390f | -7.27818 | -46.6106 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d43c9ff3-92b3-3519-8134-a354c81fda5d | -7.27343 | -46.61036 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 469bc6fa-ed72-33d7-b622-3a5641230ad6 | -7.27279 | -46.61403 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 17723aa8-7b57-3ac9-9515-487ae5691d0f | -7.27267 | -46.60947 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e68bee1-e240-3155-9659-1b252c646592 | -7.272 | -46.61311 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18a63ba8-88b7-3dd7-89bc-9ca42588af60 | -7.26727 | -46.61292 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e7f58c7-1a6c-3eed-926c-31d328fade7a | -7.26661 | -46.61666 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e08bd0b6-0f8d-3be0-83cc-0a1a9d92533f | -7.26648 | -46.612 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a6d0fc1d-6344-3720-8f78-19347db0d7be | -7.26579 | -46.61575 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2948dcb-5bed-31d2-be5f-3a22483f32c6 | -7.09763 | -46.44934 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5d5f26db-6818-39a4-88e6-88afd2994f09 | -7.09758 | -46.45003 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a2aa3d1a-6da2-3c8e-b996-7059f92acd23 | -7.09691 | -46.45329 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f472cb46-29e1-349f-971c-3ad1dd7d4888 | -7.09689 | -46.45401 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 82025119-d38b-3717-9257-c6f9ca776b65 | -7.09216 | -46.44824 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 086a0f70-e48a-3ee2-8500-520813e3a352 | -7.09211 | -46.44889 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e376e1e5-51bf-333e-a795-64dc27440cc3 | -7.09145 | -46.45213 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d7cc4bd-2341-3f64-ac7b-7db1753da4b3 | -7.09143 | -46.4528 | 2024-09-27 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f222198-9645-33b9-8f74-38efac736f22 | -6.83948 | -46.43474 | 2024-09-27 03:47:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d3135f9-92fe-3972-8a15-c51afd12e9aa | -6.83886 | -46.43824 | 2024-09-27 03:47:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0fdfe10-f252-3139-bb83-32ff09394274 | -6.66316 | -46.34161 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13373c8b-f08e-30ea-afd6-1fadbd0047e6 | -6.66251 | -46.34537 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a11b3295-6681-3e8e-b4af-2a80027b9568 | -7.82661 | -45.49713 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93059840-f1b1-3d46-98a6-e83951c35186 | -7.82153 | -45.49616 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70ff93fd-6503-3a37-b2c6-887728afb6c9 | -7.81642 | -45.49534 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b427cc7-ccd0-37d7-aea3-3eca1af5226f | -7.32628 | -46.05879 | 2024-09-27 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2ab73ba-cc22-3e06-8f5d-e28ff3196f5b | -3.21496 | -46.78982 | 2024-09-27 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 05cbd87d-8169-347c-b644-9a905b944adf | -3.21423 | -46.79415 | 2024-09-27 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| ba7d3a9c-5e7c-351c-b6db-3d35a3d917ba | -3.21349 | -46.79853 | 2024-09-27 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| b6300d6d-2717-39f0-ae11-6d1c5662dc90 | -2.72514 | -46.73949 | 2024-09-27 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6f8463c-af4d-3873-874d-3d4b3fd97084 | -2.71989 | -46.73392 | 2024-09-27 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5044dcb5-7225-3f92-aa55-1615f0e42e78 | -2.71389 | -46.73283 | 2024-09-27 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1c7f7240-b145-307f-bb2a-4d9bf25bd15d | -2.35262 | -46.45843 | 2024-09-27 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 88504758-5dc2-3614-b5e2-7c5db2991745 | -2.35189 | -46.4627 | 2024-09-27 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3a038218-835b-34e9-b051-e82dd9db97cf | -2.34941 | -46.45785 | 2024-09-27 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c0e987a-9a71-3ba7-bc12-546d68e55a43 | -2.34871 | -46.46213 | 2024-09-27 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65b33971-c8d8-3a5e-9d95-7541149c66f9 | -4.48813 | -46.31396 | 2024-09-27 03:47:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3629796-30eb-3599-9917-051ab239474f | -4.4875 | -46.31763 | 2024-09-27 03:47:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2811eaa4-892f-3e20-b131-ba50b040418d | -4.48243 | -46.3131 | 2024-09-27 03:47:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94e1ef02-171d-3a87-880f-ffea660c8aa1 | -4.48178 | -46.31686 | 2024-09-27 03:47:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eeb2c116-43d1-39f2-ac96-0cf9d9735ba2 | -4.47675 | -46.31205 | 2024-09-27 03:47:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11e2c65f-d959-3323-9be7-198bdead5899 | -4.13709 | -46.6944 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 79656dba-3dd4-30dc-a54a-d3019cfe1592 | -4.1364 | -46.69852 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 690694c7-eee6-3fbe-abd9-b446daf5e228 | -4.13606 | -46.69361 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2d265b33-b098-3dda-b5f0-c20fcd234b22 | -4.13532 | -46.69782 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d237fe97-dbb2-3d8d-a752-bbc12e96504a | -4.13133 | -46.69282 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96585020-eb92-3546-b4ae-0a1110273f3b | -4.1306 | -46.69712 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d86a2038-6736-3980-afd6-86faa1cb8b1f | -4.1303 | -46.69206 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c065058b-1070-3093-860d-c15088fb22cb | -4.12955 | -46.69635 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca4e0ede-f9b7-3208-a30d-8814e525cd36 | -4.12556 | -46.69121 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42da743b-f3c2-3d24-9b1a-3cf217f30fcf | -4.10681 | -46.8021 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cab17c18-8a62-3107-aaf7-7fd4056e038a | -4.10608 | -46.80637 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abf1d1f5-ca22-35a7-a6d4-6613cccd7be7 | -4.10532 | -46.81091 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2f395a1-8a37-394b-9d5f-e30a180962b1 | -3.91767 | -46.44042 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba75cb8b-b781-3b71-9e69-d89424689be2 | -3.91699 | -46.44445 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a02e593-dbff-3936-b21d-977cb09e3067 | -3.91629 | -46.44851 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd29af1b-b618-3570-87ef-7f9003b3d5d6 | -3.91559 | -46.4526 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b96a0fdb-b35a-3c75-b288-ed34df06672b | -3.9149 | -46.45667 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90baeae0-7a6f-3c43-8eb4-396d318281bc | -3.91421 | -46.46072 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02b3c0b1-c772-3365-89eb-de641fcbf03f | -3.9119 | -46.43938 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a62832f2-f504-39d3-9042-9ce050bc1c05 | -3.90909 | -46.45578 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 26f988a4-b4b5-3e31-9288-0d4e908a1143 | -3.90841 | -46.45976 | 2024-09-27 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7419a609-9ef9-3ad4-adc3-e9acc1e1a29e | -6.08959 | -47.66476 | 2024-09-27 03:47:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d4f0006-6677-33a4-b99b-6b40e2bea7a6 | -6.08876 | -47.66944 | 2024-09-27 03:47:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 840457c3-089d-3747-805e-544e643be6da | -7.77063 | -47.11824 | 2024-09-27 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abc78d2c-b373-3ce7-b318-4f87fca61126 | -7.76496 | -47.11719 | 2024-09-27 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06f81954-9596-3804-bd35-82db8b377e2b | -7.51563 | -47.56679 | 2024-09-27 03:47:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7633058-3eab-31fa-a8db-85bea0775f7a | -7.50979 | -47.56562 | 2024-09-27 03:47:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80dc0f3d-1e4a-3f0b-bd81-ccf4ffab7ce4 | -7.01608 | -46.81644 | 2024-09-27 03:47:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eda625c9-93da-366a-8a90-16721cd715b2 | -7.0154 | -46.82025 | 2024-09-27 03:47:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67cc5d0b-2d8f-3a66-abd4-889280ddadb8 | -7.01341 | -46.81493 | 2024-09-27 03:47:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc91ab4c-96b7-328f-9e81-12ff2f72f7ef | -7.01271 | -46.81871 | 2024-09-27 03:47:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e14334e0-b07e-3154-9751-6a6f4c74be9c | -2.16479 | -47.95183 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7fb1a50f-8142-37b6-944a-192ddb2aa5ad | -2.16386 | -47.95741 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52e0b51f-c662-3e4c-ba98-ef78823e8ae2 | -2.35546 | -47.60672 | 2024-09-27 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 3d8e53ea-9d25-33f8-8246-b578c27d502d | -2.35458 | -47.61202 | 2024-09-27 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 80a27316-410b-3a51-b0e2-120d4e7ab55e | -2.35371 | -47.61729 | 2024-09-27 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 07973c60-41e8-3d93-85cb-93eb628248e5 | -2.34909 | -47.60559 | 2024-09-27 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 8754adef-42dd-3036-91ba-ae2f51ec31d2 | -2.34822 | -47.61084 | 2024-09-27 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| a568b152-1aa7-382d-a68e-a5e806dd57be | -4.63092 | -48.53932 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README56.md)
