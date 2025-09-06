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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 243599c9-9994-3310-bc33-373918ea5c0c | -15.6508 | -52.3228 | 2025-09-06 00:15:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 26d6e392-2ab0-3dcb-95ef-b8920c7394d0 | -16.135099 | -52.978298 | 2025-09-06 00:15:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 01bcf4be-1319-30cf-a2b4-1f07d520989d | -12.2843 | -53.874298 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c43fd7c0-85eb-3b73-a575-9ea634d8fc72 | -12.698 | -48.919498 | 2025-09-06 00:15:00 | METOP-B | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e4d2402-6dee-3740-a44f-cadae6d0474b | -11.4453 | -54.558701 | 2025-09-06 00:15:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a79bd3d-504f-3f6e-876f-75e4b373f162 | -7.1254 | -48.540199 | 2025-09-06 00:15:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a026bf9e-f200-3f10-9fa8-ff736b73a9aa | -6.6356 | -52.831402 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5af3a457-a02e-3e38-a4a3-052c7f71b1db | -21.927799 | -46.672901 | 2025-09-06 00:15:00 | METOP-B | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3619b7ca-27e4-3928-a126-db69f9e368b7 | -5.7253 | -43.0415 | 2025-09-06 00:15:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 359c2c3a-9ceb-30ad-928c-e2197898d766 | -5.9914 | -53.2659 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e2c7d78-8f47-3b73-90b8-15f341d5d12e | -5.6822 | -51.995399 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b702d3b-e421-3e19-af89-8f56d8572842 | -6.341 | -49.541599 | 2025-09-06 00:15:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54fc693b-a3ff-3c16-b14f-81fae0392452 | -15.3835 | -52.929798 | 2025-09-06 00:15:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab979768-7e08-3bb2-81ad-ac083ca44121 | -13.393 | -43.4025 | 2025-09-06 00:15:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 06b3fdee-14d6-3c67-a5ab-c080c109ada7 | -9.5081 | -49.523602 | 2025-09-06 00:15:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e94dfee-dd34-362a-8d83-7bb6fc711cd5 | -6.1081 | -44.6175 | 2025-09-06 00:15:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71074b8c-1e1b-340f-8242-de952043b330 | -5.806 | -46.732399 | 2025-09-06 00:15:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7baec350-97aa-3bc0-b445-a8b09d46ff81 | -10.0369 | -50.5751 | 2025-09-06 00:15:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0942302c-4261-35cf-918e-40b17b8e1b1a | -8.158 | -48.321602 | 2025-09-06 00:15:00 | METOP-B | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3423ee06-5dec-3b6b-9284-745b70a87d18 | -5.7683 | -43.6562 | 2025-09-06 00:15:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dece2dad-c5af-314c-930b-396987f7db2c | -2.9642 | -49.506599 | 2025-09-06 00:15:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68f82c22-aff7-37a6-b72f-d018bcf99457 | -15.3791 | -52.907398 | 2025-09-06 00:15:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d2705ca-0e16-3b66-9b97-417d84ef7ce3 | -12.3063 | -53.881802 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdaee1a1-45ea-3d71-9e04-96d7e645ef8a | -11.4284 | -52.242599 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94c71e16-4e5f-3e20-b084-394bc8677b93 | -12.289 | -53.897499 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02fd1c5f-58b7-392a-9d06-3cdb86b41a7b | -10.9066 | -52.049099 | 2025-09-06 00:15:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9dead4fb-99b2-3f73-bf36-305bd61b29f8 | -11.8032 | -47.806801 | 2025-09-06 00:15:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a3d99b2-ec5b-3e0a-b12b-63a77fa20419 | -9.8866 | -48.127399 | 2025-09-06 00:15:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1bf3218-5464-343e-b129-2cfa6c43a2e7 | -22.639999 | -49.2383 | 2025-09-06 00:15:00 | METOP-B | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d4f8e25a-3e55-3c95-bbc0-867d42a3a3c3 | -6.8579 | -50.892399 | 2025-09-06 00:15:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc22141-5b4b-357d-8cca-f68db3466d2c | -16.104601 | -50.520401 | 2025-09-06 00:15:00 | METOP-B | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c9912458-58b1-3287-8e77-e36f02366834 | -8.1445 | -46.9939 | 2025-09-06 00:15:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2435cdf8-1e44-37f5-b047-6c3aeea46987 | -9.642 | -48.875099 | 2025-09-06 00:15:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 042baa3b-cb94-3e05-a1e9-d4b18d42bc37 | -14.3753 | -48.123299 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ed8437d1-0631-3058-8383-5f995d81d15f | -5.1169 | -44.958599 | 2025-09-06 00:15:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f7cad95-b63d-3666-aea2-4621cf8e2e3a | -13.3522 | -48.1506 | 2025-09-06 00:15:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f76edd39-aa6a-359f-96c0-ec69611cd1dc | -16.0965 | -45.7248 | 2025-09-06 00:15:00 | METOP-B | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2f375887-f9a5-3fb8-8162-40c5e3b3e9fd | -5.781 | -44.760201 | 2025-09-06 00:15:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8189819b-5159-3c0d-a7f9-6c1b993186ad | -23.226 | -47.093399 | 2025-09-06 00:15:00 | METOP-B | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2d51713c-be5a-35c6-b714-ea9cb070e59e | -5.5283 | -45.398701 | 2025-09-06 00:15:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5795d77c-302b-34a0-8aa5-2e59a6bac59c | -13.651 | -46.311798 | 2025-09-06 00:15:00 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aff00af0-d562-3220-9ef4-0a8c570f8ea0 | -3.4901 | -49.5998 | 2025-09-06 00:15:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b44a06f0-5034-3586-8275-895628efe45a | -6.6429 | -52.865101 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d822dbb2-d11e-3c6e-9869-f0763dfa25bf | -8.322 | -51.381001 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0c43791-6dfa-3d35-b17a-d77dad3e925f | -5.3556 | -46.566898 | 2025-09-06 00:15:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58c857f9-e74b-38f5-b20c-3547e846051b | -5.9854 | -53.2855 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 015d2e09-013f-3d5b-b4ea-8fc082595d3c | -2.4265 | -46.864201 | 2025-09-06 00:15:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff1b53c9-e797-39dc-9fc0-35a8ebce837b | -6.5348 | -51.993999 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 818c547e-d362-3107-8d98-2839ab651ab3 | -5.7298 | -52.024799 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea6a3ce-c70a-36f4-b344-3d88ed7fd49b | -6.6454 | -52.8293 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9742835b-ee4f-3e56-a70d-c75a6d85be5e | -2.6507 | -49.5327 | 2025-09-06 00:15:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c80ec90-2759-30b2-ac9d-3549a9da9b4d | -16.3374 | -51.777199 | 2025-09-06 00:15:00 | METOP-B | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1bd6f3d-e333-3d0b-88b1-294803c13bee | -9.6007 | -48.368 | 2025-09-06 00:15:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e94cbbb-66c2-38bb-9773-10d60a66a05c | -15.1563 | -46.446701 | 2025-09-06 00:15:00 | METOP-B | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0a74fc23-005b-3b23-946e-7d4a8877227c | -9.4846 | -49.3246 | 2025-09-06 00:15:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26f210f2-6a6f-30cf-bb8f-6d239eb28ef6 | -19.009399 | -42.923698 | 2025-09-06 00:15:00 | METOP-B | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 667b4cca-cbe7-3094-8cd1-91c76dc5eacf | -5.756 | -53.834099 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4978ec07-76a1-3273-b55f-d31073b9eebc | -12.3039 | -53.8703 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 525e757e-d1e1-30e7-94d7-155973bae9b3 | -11.4478 | -54.571201 | 2025-09-06 00:15:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5f516e-291f-3933-9c81-658783bff309 | -18.2474 | -45.979198 | 2025-09-06 00:15:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ef670a7c-a3f9-3ebb-84fa-25a59517cb49 | -4.2895 | -42.923 | 2025-09-06 00:15:00 | METOP-B | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 71155a65-d73e-3c48-806a-56e24e009a0b | -14.381 | -48.055302 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3bab02c8-8daa-3c32-8762-5dc8e8633e73 | -10.3985 | -44.357899 | 2025-09-06 00:15:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7bd52cd0-5eb4-32d5-bbd7-305c4dff93a4 | -6.0983 | -44.619801 | 2025-09-06 00:15:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd282069-5229-3819-9f64-10a8b4e33841 | -9.5775 | -46.946999 | 2025-09-06 00:15:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11a172f0-fda4-3930-9c2e-97e389c5616f | -5.6641 | -46.0728 | 2025-09-06 00:15:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64236920-3e30-3974-8f29-eb66ff7eeb31 | -12.7603 | -54.834 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 52d33f3b-b5a5-3e8a-b675-6f39db0edfd3 | -7.595 | -45.465599 | 2025-09-06 00:15:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a841d5b-08e4-3458-b507-90e6225f64fe | -10.9567 | -48.213299 | 2025-09-06 00:15:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b2b150f-ced6-36c1-a849-ca46a34b0d19 | -5.7314 | -52.032398 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae405f8-44ab-34a1-8e95-e5924ab18f55 | -3.0458 | -50.831501 | 2025-09-06 00:15:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92cf4d98-727e-3f8b-85fc-5e357889e57a | -12.8171 | -54.8652 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c9b5f515-81fe-319a-a278-006897880305 | -8.2378 | -47.356701 | 2025-09-06 00:15:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0626e63-b676-3233-8dd0-7c5b40cfd044 | -5.771 | -53.6199 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 774a871c-5e6a-3805-a1b6-5a6fff6af568 | -8.6726 | -47.953701 | 2025-09-06 00:15:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b104864-b76a-30e1-b77e-e4b5394ca202 | -4.5949 | -47.293598 | 2025-09-06 00:15:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fe07b18c-ca81-30ac-a43f-749f45206729 | -14.8765 | -48.1572 | 2025-09-06 00:15:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7a136f60-7a04-37db-acd6-85b682dafa7a | -17.951 | -51.801498 | 2025-09-06 00:15:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 058db482-31c0-3a99-ab61-d9786846473d | -14.3738 | -48.116299 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 63b99c2e-3d34-32cb-bf14-bbdd2c6f59aa | -15.5268 | -53.614601 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0387ddaf-ad8d-3cc3-9659-bc8815e3fd88 | -11.0893 | -47.793701 | 2025-09-06 00:15:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fff7ea03-701f-3909-8ac9-8b2b4f37863a | -5.8467 | -51.716 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce9149a1-42db-3c82-a092-274eb530cc6a | -3.549 | -49.0844 | 2025-09-06 00:15:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64e068ba-a0b3-31f0-afab-116abe5c4de4 | -7.3015 | -49.507702 | 2025-09-06 00:15:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 393a1701-6c83-35d3-97ce-313a46d8bb99 | -3.1255 | -54.933399 | 2025-09-06 00:15:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd171ce-74d0-333d-bd93-d35d5a0a16e2 | -21.183599 | -51.768902 | 2025-09-06 00:15:00 | METOP-B | PAULICÉIA | SÃO PAULO | Brasil | 3536406 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a4c5b3a-f02c-372a-894d-45eddb22d287 | -5.6751 | -52.196999 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc5f12d0-5c81-31dc-b4ab-c0d9631aff12 | -7.4833 | -50.324501 | 2025-09-06 00:15:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 588e88ea-a269-3ec1-92cd-1d7d7337cab1 | -4.8012 | -45.150398 | 2025-09-06 00:15:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7154bb3-a282-3f9f-ac4b-b1a7016d908c | -3.7492 | -49.332199 | 2025-09-06 00:15:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41433eba-678b-399f-a684-ea136a8aca05 | -12.755 | -54.8069 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50f5fc8b-97c5-3331-b033-395a9ce9479a | -6.8563 | -50.885201 | 2025-09-06 00:15:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9256aac-3632-34ba-92d3-4a8b4fdd3a65 | -11.0221 | -55.032001 | 2025-09-06 00:15:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d06e347e-f7e0-3817-9ffe-70975132450c | -6.4092 | -44.0159 | 2025-09-06 00:15:00 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b4af02f-6e71-3e9a-83d1-ddf3db683041 | -5.6735 | -52.189301 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc94dade-19ae-34d2-8bfe-3da2644a4bab | -12.7034 | -48.056301 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 169fc317-5179-34b6-a5e6-e7289a58e526 | -19.2115 | -44.358398 | 2025-09-06 00:15:00 | METOP-B | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6afd8f35-7c05-31b3-ac97-9a4948551d38 | -5.7285 | -43.055 | 2025-09-06 00:15:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d5e4c590-c3b4-3158-b46b-eaf32bc35b1d | -12.3109 | -53.905102 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 284e847f-ac43-3207-ac34-8c501251b722 | -12.7132 | -48.0541 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
