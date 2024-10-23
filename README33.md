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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dd8344c-196a-3f13-bb32-d01d0a34c943 | -5.50639 | -43.69678 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87b21287-bf6e-395b-8b28-2f535c498824 | -5.50594 | -43.69985 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfb2f234-0399-3b2a-8eee-2c1501f7c915 | -5.49021 | -43.66249 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b73ba0f9-b1e9-34e0-b574-453741a012b5 | -5.15991 | -43.96031 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc3b1520-27fb-39e2-b879-31dcc9960281 | -5.15951 | -43.96321 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1bb5a9c-19d2-372f-b472-c00ed666216d | -5.1591 | -43.96609 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14f31b55-d22b-3722-bd5c-65358122f916 | -5.15574 | -43.95846 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad6f8232-161d-3dd0-8330-7a80decf159a | -5.15531 | -43.96135 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e716203-a571-39a1-af72-1258e1f78312 | -5.15528 | -43.95654 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e84cf3c5-1892-39cf-b23f-2fdd7a03a4bc | -5.15489 | -43.96424 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b34f1a6-cdf4-31ad-bd53-56ffd00af453 | -5.15488 | -43.95945 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cc3846d-1728-3f81-8875-7e6fc708333c | -5.15447 | -43.96235 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fef556d-e695-34e0-a201-73d630feab68 | -5.15446 | -43.96712 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a4832f0-9d6c-39b9-83e2-05e2a230bb14 | -5.15407 | -43.96524 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ffe8243-8316-3179-b8d0-39ca7a5d077b | -5.15404 | -43.97 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d16f264-0f2a-3f71-93db-8bb7eb8f8217 | -5.15361 | -43.9729 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fcff8d6-a73f-3198-8218-780afe4ec713 | -5.15326 | -43.97102 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| be8855c7-0a4a-3d9c-baec-a79e83ff0c52 | -5.37053 | -44.27983 | 2024-10-23 04:51:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1e330a0-a18f-35e2-95f8-f4fa4849ce8f | -5.29585 | -44.2967 | 2024-10-23 04:51:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fedd247-989a-3727-a81b-8da1015ffee8 | -5.09699 | -44.21862 | 2024-10-23 04:51:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 460e7324-d476-332a-b814-4a5ed46ae7f0 | -7.32193 | -45.28531 | 2024-10-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed0068bc-f48d-371b-a2e8-f1650d6354ed | -7.32132 | -45.2845 | 2024-10-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1818a987-00da-30a1-b0e2-334a2264bb9e | -7.31787 | -45.27938 | 2024-10-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94601190-f767-3199-87ff-d2c7b32226bd | -7.31716 | -45.2846 | 2024-10-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b5d2c8c-03bf-3940-a8c5-a945e3f60a7e | -7.31655 | -45.2838 | 2024-10-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2da9453-288c-3a46-9640-6fd971364ef9 | -7.17086 | -45.13883 | 2024-10-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7f10f02b-92b8-313a-afde-eabe55cfc672 | -7.17015 | -45.144 | 2024-10-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28e905c3-0602-33c5-accf-8a0e8756cf3d | -7.16682 | -45.13264 | 2024-10-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c9e6fdb-f019-3913-a468-44b5ced947cf | -7.16608 | -45.13798 | 2024-10-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd283563-566f-3091-b786-86217e46c2e8 | -6.8394 | -44.38908 | 2024-10-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b041ffb3-5e3f-32ce-bb6b-1063746553aa | -10.44911 | -44.89698 | 2024-10-23 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8cff2144-7999-38b1-8bc8-0560a3c50516 | -10.44399 | -44.89621 | 2024-10-23 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c4a7a9c0-aa03-309c-98d0-16fe0129b60b | -3.11367 | -45.3055 | 2024-10-23 04:51:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bd3b90c-0a7f-31d5-b3ea-e72826deccd4 | -3.11703 | -45.30345 | 2024-10-23 04:51:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e80c97f-767e-3adf-b48d-4ca34f97dcb0 | -2.78864 | -45.1898 | 2024-10-23 04:51:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1caee9dd-13f9-35af-bd74-c23e0b87ebfa | -4.14204 | -45.59324 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2129b38f-af76-3c69-a1ce-eced2782d48d | -4.14138 | -45.59763 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6907fdac-84a9-3ae6-8464-f5298bbd7f31 | -4.13892 | -45.58379 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce9d5b3f-db14-3e34-98d3-ea203be88d4d | -4.1376 | -45.59254 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e9fac9e8-9acb-3a86-ab22-8970070f1c47 | -4.13694 | -45.59693 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ef441593-e704-3ad3-a4f8-a7872968a29f | -4.13185 | -45.6006 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4f0c713c-dcbe-3867-b21a-e1261d8684bd | -4.13119 | -45.60498 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44d7e68f-0088-399f-bda4-bad4449c867b | -4.13069 | -45.57805 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9517e98e-357a-38d8-aa98-6c3ebfbb1e16 | -4.12938 | -45.58678 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 907dd3ef-81e9-37b2-9304-16eebcacc360 | -4.12807 | -45.59552 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 2f936c9f-a1c7-3c00-8eec-5138fdad8a6f | -4.12428 | -45.5905 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a444008b-14b7-39bc-b3d3-7740bebc4e2d | -4.12363 | -45.59487 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 80596869-7a99-35b0-8612-1b08c362364f | -4.12297 | -45.59922 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 247a3639-da17-3ffe-bac0-659868f59b67 | -4.11919 | -45.5942 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d7d0f2f-7ee6-367d-b1a8-3c18f4012bb1 | -3.89304 | -45.66095 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 930f9b80-1e86-3800-aed4-fe12367be569 | -4.75907 | -46.11025 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95c2d5af-9349-3a82-b36e-9927eb394c61 | -4.75846 | -46.11449 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1e2c9577-2de5-32a0-ac81-9e27cea0dcec | -4.66018 | -46.19841 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9eab15a2-a8c6-300e-a275-5be39c2986b7 | -4.65589 | -46.1977 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72f1d5ea-9f4d-32d5-bb9f-c6b93e6b6e1d | -4.96433 | -45.87618 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ae6853f-4546-33ab-85dd-9f61e8f5e751 | -4.96368 | -45.88055 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9479d1e4-1441-3a9b-8d63-26018c988fee | -4.95991 | -45.87562 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6179002a-cde7-3124-b9cc-3cc885800102 | -4.94437 | -45.54612 | 2024-10-23 04:51:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81d649d5-2662-3a3a-88ab-b99b7b7954d4 | -4.90506 | -45.84986 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e94fcb61-bc68-3892-ade4-44abfae4ab6c | -4.90004 | -45.85337 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21dec0b5-8c67-35a0-b13b-de530dc92c7b | -4.89941 | -45.8577 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec25f02b-d90e-3d85-ba9d-607ab70839f9 | -4.86732 | -45.86146 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f320ea01-fc89-3d8f-a0eb-ee083e9eabf2 | -4.86709 | -45.86305 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4219292-cbb5-3ace-aed5-e1edd0c93b40 | -4.8633 | -45.85825 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 01a60f8d-0db2-3a58-bfa0-53c12c5025a0 | -4.86266 | -45.86256 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25819205-f22b-3b02-8675-7565db3cf836 | -4.83741 | -45.8505 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c1fe5c8-0ebf-34b5-a06c-b76ca61e4723 | -4.8002 | -45.70189 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cb5ad3a-e03f-32ce-9ac5-5b8ae3040d5a | -4.77702 | -45.11813 | 2024-10-23 04:51:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78fb6ee7-a068-34eb-80d7-1806f535df0c | -4.77584 | -45.11923 | 2024-10-23 04:51:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20a84c51-ec7a-3f9c-912d-0c4e91295d83 | -4.76006 | -45.76622 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3ad97c5-c4dd-321c-b566-753249fa0c0e | -4.7594 | -45.77058 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| feb5594d-05b6-373b-a436-2c16ddd83d94 | -4.75564 | -45.76545 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cbb04d3-7b32-34de-bbb5-24417bee8155 | -4.75317 | -45.18241 | 2024-10-23 04:51:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e982805-477e-3989-b676-c4d11a2d9ae7 | -4.75248 | -45.1837 | 2024-10-23 04:51:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b9578c6-f2bb-3939-9697-aed3baf7325f | -4.72926 | -45.72921 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d06558f9-f234-34b6-a1e3-fc4403f5c98e | -4.72865 | -45.73338 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f86a079a-7abe-3b17-90ee-cb1049434cec | -4.72548 | -45.72401 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad48fdcd-8cb0-3284-8718-f2181ebd4a8c | -4.72483 | -45.7285 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee0f6d38-b60d-3726-962e-2a2dac54a4bf | -4.7242 | -45.73279 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24b69d9e-5042-3276-b69b-8154c6c0905e | -4.72357 | -45.73706 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77d587e2-dc03-3932-9a06-0614dee35fb9 | -4.7204 | -45.72771 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ef1cd05-9b55-3b2f-a586-680f3939de48 | -4.71976 | -45.7321 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bb18b31-9541-3c96-935c-8caa8aaa558d | -4.71913 | -45.73643 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 910d919c-19a3-35a3-a430-074a5378927a | -4.71536 | -45.73118 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a51fc7d-1fc5-371e-8673-c79f3d829531 | -4.71471 | -45.7356 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 65bbad83-a31e-3393-9c0e-af4ac4d3b8c5 | -4.69074 | -45.86904 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e8fd28e-96f5-32c9-af74-12ffde068fc4 | -4.6901 | -45.87345 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b84acc91-8ac5-378f-9838-95975b3d861b | -4.687 | -45.86388 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2261910-1db4-39be-acfb-6e2ac8aed0e5 | -4.68634 | -45.86838 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0dd0bee-72fe-3ad2-bcba-d15ebdc7d007 | -4.58654 | -45.78043 | 2024-10-23 04:51:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c26656b-b7de-34b5-8ebf-c98b94a9f636 | -4.46331 | -45.88593 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1310579-c498-3801-b9d0-5f08ad4f817c | -4.1427 | -45.58884 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab3a406a-b82d-3296-8ce4-16bf14434703 | -4.13826 | -45.58815 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 61f82b9c-508b-3192-8715-5e8f4c8e238c | -4.13628 | -45.6013 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3839ec5f-de73-365d-bc5a-62e921ee461e | -4.13513 | -45.57874 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93dbb27b-f767-315d-abbf-a7b7b97629da | -4.13448 | -45.58311 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b213c41-7363-3dba-8f25-7ed823e0cfdf | -4.13382 | -45.58746 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5e1c0ca9-8ac1-332f-be51-6357e435206c | -4.13316 | -45.59184 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 0a2ae10e-3f50-36cc-8724-fb45be48109a | -4.13251 | -45.59621 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 838ec112-4e87-3635-b65e-7a5d86a26b14 | -4.13003 | -45.58242 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README34.md)
