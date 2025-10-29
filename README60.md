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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29e58b15-d90b-3fc6-9561-66f41c8de597 | -7.20057 | -47.98304 | 2025-10-29 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3735589-5997-3b4b-80ba-9287e3019256 | -8.55854 | -45.69881 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9c32a39-b5c5-3480-8125-eec8aecd8dd9 | -4.47879 | -43.4429 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c502e26e-5b26-3700-8f5c-1151f53429a0 | -2.94565 | -51.05342 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a665d82-26ac-3d84-960d-c921bbc63631 | -4.20853 | -50.09277 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca96813d-a7ce-3a1e-b2b0-5348d78e2dbd | -6.49729 | -42.23844 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 02f6f01f-a455-3670-b85b-64200dc38e9a | -3.2048 | -51.0052 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 87d36277-b716-3576-8db3-2f2ad0fef90e | -2.42604 | -49.30775 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ce119d85-9920-3888-a520-f0182fdd1c43 | -8.69338 | -47.1389 | 2025-10-29 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b006de40-e5ca-3b30-8f73-3f90ea7b21c0 | -8.02652 | -47.39811 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ed701b1-434c-374c-b25b-3083a1e3c833 | -4.66412 | -46.40035 | 2025-10-29 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 861eab75-4f6b-3672-83be-33dc01b3de85 | -2.225 | -48.37586 | 2025-10-29 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e13d540c-073f-368e-b67f-b0cbf2e31df6 | -6.90541 | -42.86879 | 2025-10-29 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4829c4f8-afd4-346a-9d6d-63d677d76460 | -6.11068 | -41.71467 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c391badf-cde7-3925-bba6-6626f56778c0 | -3.94954 | -49.01852 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77c62895-ded8-3855-890f-a7696e160e91 | -4.20748 | -48.35594 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebe7455d-df61-383d-8f73-14fdbdd735f1 | -6.49095 | -42.24612 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b5ed2e26-446e-371d-9182-fe43114901c1 | -7.64351 | -46.92175 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62ec3331-a5dd-381f-b076-c71444178e63 | -2.93678 | -51.06634 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57488b5d-5a6a-38e3-9f1b-3ba5b4c77b98 | -7.40908 | -48.16013 | 2025-10-29 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5de98ea2-65b6-367c-baf1-49f1223a4ba6 | -7.36856 | -47.63477 | 2025-10-29 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f936ef32-f657-30d5-b8e2-2c6a29227243 | -2.80444 | -49.14889 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4030af75-4d0d-375e-ace5-11bbd3bb463d | -6.14957 | -41.57415 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0ee73d99-dff5-37b4-b346-1e68377f0f84 | -6.46037 | -43.55563 | 2025-10-29 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| deb10db5-81ca-32f4-bed8-45ddfc210469 | -5.67736 | -47.82479 | 2025-10-29 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 469a6915-1d68-3964-ae95-8fe1d0234a6a | -2.4194 | -49.30672 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8f3a26ca-02de-3ace-aa72-0370e798dfc1 | -3.148 | -50.4612 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 514c191a-4d27-3fc1-8f9d-d64175b5e148 | -7.81264 | -46.42041 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b42ae16-ed10-3276-a6c3-c998fcda076c | -4.00957 | -43.28632 | 2025-10-29 04:44:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb8fdade-2bd2-3898-9f20-8a740b4b76a4 | -3.81399 | -48.65824 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0b4b512-a725-35bf-9aba-38c43dd904b8 | -4.29329 | -44.48915 | 2025-10-29 04:44:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 847ecb61-e056-3982-9fdc-d15f88a36355 | -5.6085 | -47.11372 | 2025-10-29 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3104381c-7275-32a1-9e43-cba59ce2042e | -6.54251 | -46.76761 | 2025-10-29 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c56b030-77ca-3961-b4a3-7595dd268cb5 | -3.72416 | -41.57609 | 2025-10-29 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f5ce5fd-7aaa-34d0-a866-cc3bd5e8ee5c | -8.55802 | -45.70238 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c25a2c56-4116-3ae3-b46a-50232427849a | -4.46549 | -50.12286 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b10fda80-3220-3557-b226-0085397f58d7 | -3.11162 | -51.29177 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a5ba975-c697-3ead-8412-c920004c4465 | -5.4148 | -45.21829 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 494184c1-dbb2-39a0-92e3-ecb377297ddc | -7.35385 | -47.63266 | 2025-10-29 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d267a7b-3d2f-31e1-9a03-496626b58bbf | -4.53008 | -46.04277 | 2025-10-29 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a091ead3-1d98-30b7-83f4-8e88c7414147 | -6.23115 | -46.03646 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45102a86-f239-3cb4-bc4f-5c714c6b03a1 | -5.48771 | -42.17017 | 2025-10-29 04:44:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b4e7ada3-5a8b-35d5-ad42-9b4d54cbee4e | -6.48929 | -42.24848 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2aa53b8b-e77a-3500-bb01-1e3c13904881 | -6.88318 | -45.04704 | 2025-10-29 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50ad64d9-c1ad-3c8c-8b25-424c5f29278d | -5.97616 | -46.31945 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d828924-2432-3dae-8cfc-d06d89e476ce | -4.29822 | -49.65278 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbcbaf35-08f6-380b-a809-917c049f9777 | -3.20093 | -51.00815 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e62a2bba-9c7c-3b77-9992-c732f9f96060 | -7.95667 | -47.84905 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a1eea14-a919-3937-b086-8c9288b94398 | -7.07547 | -44.93229 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a4cf111-54ad-3db6-8861-97ae47bf2a36 | -4.10929 | -48.73703 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c16fe5fa-24c9-3793-971d-16e905e3cd86 | -7.07318 | -44.93708 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ba5dac7d-61ab-3fa0-9a56-bd3607d4e7be | -5.42698 | -47.9056 | 2025-10-29 04:44:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4861585-44f3-3eef-8267-2f623518d737 | -4.1545 | -51.07994 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 26b37f22-8af8-3ce0-9951-0dd11d392c70 | -3.96354 | -49.96638 | 2025-10-29 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 478594b2-aebe-33d7-bdf9-9326db88d7e0 | -4.91034 | -48.56698 | 2025-10-29 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59c4e2df-c888-3871-89cc-0e9a1f57f962 | -4.20577 | -50.08881 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 314d31f7-9c4b-385b-b033-99f834ffbb95 | -3.70781 | -45.38754 | 2025-10-29 04:44:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e22e5f49-4419-319e-939c-7de735088f82 | -7.07634 | -44.95756 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7e9f6c7d-6f15-3cea-adfe-e3ea83d7f368 | -7.89065 | -45.6911 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8031483a-dabf-36f4-a486-5b27eb559faf | -3.51758 | -52.83406 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd756daa-79bc-37d5-898e-92166f5f5200 | -5.48542 | -46.44013 | 2025-10-29 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7bf9bd2-1209-3563-9c16-848da754b766 | -8.55433 | -45.69817 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5a5c237-421d-398e-b12a-869719a40b62 | -6.62692 | -47.18155 | 2025-10-29 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 188ea710-63d3-3013-b71d-81aaac3f7390 | -6.95942 | -45.02139 | 2025-10-29 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ec19c32-2991-3e03-ab0b-698ee17dc519 | -8.40658 | -46.93124 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fd4e41c-5117-34af-8a8d-295631bbb3cd | -5.07115 | -47.10913 | 2025-10-29 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bf83e02-284e-3c7b-9775-45f4bb074465 | -1.41417 | -52.67 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 218f7a23-5f79-3d1b-a298-4a8f46f9c45e | -7.34896 | -47.64028 | 2025-10-29 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ed2ba0b-fab3-3e41-ae1f-882c153f477c | -2.43564 | -57.0643 | 2025-10-29 04:44:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a329507e-b801-39a7-951e-474755f216f5 | -6.22672 | -42.53345 | 2025-10-29 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 59e15dba-be00-3fd9-a7ee-3caaaf64c44e | -7.34918 | -43.90901 | 2025-10-29 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 600e6614-9cf4-3b16-9f0c-c9c08dde801d | -7.935 | -45.47429 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54318f95-31f2-352d-8bf3-0fc0a77bb460 | -2.77311 | -48.61074 | 2025-10-29 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ad88494-10f5-3e9e-931b-ed2fea792b3a | -5.41006 | -45.22149 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 106aa06e-6ccd-3798-88a5-73e90e5561ef | -5.52318 | -51.45002 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da83c86a-c5ba-342c-88b2-b7198073ced6 | -8.7629 | -40.61386 | 2025-10-29 04:44:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1db4877b-9174-39cf-8d66-5a42a9cd776d | -3.99526 | -48.32383 | 2025-10-29 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e46d4088-07a9-39d4-85d9-e904113bab0c | -7.81737 | -46.41593 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42678ae4-1612-3667-8a94-b44b0d21509b | -1.21411 | -54.0732 | 2025-10-29 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dbb9610-de45-3475-95bb-7773ea9cbc37 | -3.11668 | -51.21692 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a316475-acff-3006-ae1a-0ae493ddadea | -6.63065 | -47.18212 | 2025-10-29 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c32dd9d0-616d-32b3-b1b6-07841b25d2f1 | -4.59934 | -48.7891 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12802685-8287-3301-b110-fea38de79835 | -7.12865 | -46.98408 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7190f97-affd-35db-9080-5b79726a5278 | -3.35796 | -52.8102 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84e554b3-9fd9-306e-a66f-c82c0fd0e505 | -2.8301 | -49.39552 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d7ff72a-47c2-344b-9786-5dcfe9ab2051 | -4.48284 | -43.44136 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d927b0fc-de98-3eaa-ac0b-78a59460e904 | -5.68093 | -47.82532 | 2025-10-29 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caea0c26-7c2e-38e4-957a-1af82caa0426 | -7.30628 | -46.31591 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4d1a928e-20f6-3f2a-ae52-9cf7e8370519 | -7.89592 | -45.68416 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ddc6b18-9407-3b84-927a-3ffd2ca1561e | -7.36059 | -47.6378 | 2025-10-29 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfcba055-3d32-36e3-b8cb-9ff76ea2da78 | -8.54384 | -50.03794 | 2025-10-29 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bdeb6a7-61f0-33df-b5d0-957a245874ae | -3.81059 | -48.65772 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b0f30da-a86a-3ac9-a2a7-014e95ba3109 | -7.40999 | -47.17422 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7834eed-58b0-3bd3-861d-c38eeb036779 | -5.5013 | -45.96174 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fed28b6c-befb-3057-a751-92b55894ee6d | -7.74586 | -44.72588 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d9b064c-5704-37c6-82a0-f41778c7a491 | -6.96513 | -49.3966 | 2025-10-29 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 342018ed-1156-3cfb-b332-5b44cc438b9c | -7.61362 | -43.58661 | 2025-10-29 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1f60c92b-75a1-3aa5-acc3-f1dc1319e885 | -6.91964 | -46.02792 | 2025-10-29 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07e40893-3de2-3941-af54-980d7077d553 | -6.12815 | -41.7069 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c9295b68-d195-31e0-91d8-6f88e8d8bf73 | -4.48353 | -43.43658 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README61.md)
