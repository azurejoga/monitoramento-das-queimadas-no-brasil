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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f664412-2a4f-352a-9826-b5f3ea3bd51f | -5.0684 | -43.66932 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 17973b5a-a58f-3ac4-8df8-1f07c3178431 | -5.06759 | -43.66446 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 648f73c7-0bc7-3acc-ad42-2312e84e056d | -4.93235 | -43.67497 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 07b36a02-bb43-35bc-9743-256c11e27289 | -4.92965 | -43.67844 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 00b11ef5-5f0d-33c2-a206-87e956b4d27d | -4.84538 | -43.36908 | 2024-10-25 16:52:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41b39673-c15e-3a50-b77c-32fe2b8a1e45 | -4.80162 | -43.79086 | 2024-10-25 16:52:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 432b5fb7-fcc2-3acd-92a1-f280bdadbf54 | -4.78234 | -43.64427 | 2024-10-25 16:52:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 372a7e6a-d019-351c-b756-a49357b21885 | -4.7679 | -43.95701 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b19b6937-dca3-3b51-8552-f2183086ae13 | -4.65406 | -43.7539 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7e5675f8-9dfb-3ede-8a42-ddfb2cee21d1 | -4.57537 | -43.60005 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5235463b-c41f-3325-84d7-1eed1b497ab6 | -4.57289 | -43.5985 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2efec81e-5d3c-350c-b862-ba4f40c69c35 | -4.56332 | -43.56939 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 16aada9d-bd91-3fa7-8e8e-1ccd324a85f6 | -4.5625 | -43.56437 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a0a5d396-bc2d-3b85-869c-5022a31c3c48 | -4.5578 | -43.56515 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c16e8c0d-f738-37f9-a3e9-33a08aaa91ef | -4.55697 | -43.56013 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 292d40a9-3b55-3f5d-9b1e-0770b0669a61 | -4.55166 | -43.5867 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| efcbd52f-b234-33ab-a8cb-805bcf6d63c8 | -4.54695 | -43.58745 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 25fcba03-818c-3b92-8001-a8083454c3fd | -4.54612 | -43.58243 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 768c5e17-f51a-38df-bc12-b0897776edb1 | -4.53792 | -43.96255 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 591306b0-5182-38bd-872c-deb7d91628d3 | -4.53748 | -43.9597 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd05b1dd-b9d1-3df9-8f98-5e1add5e7e08 | -4.53069 | -43.42923 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 39b17c83-24e7-3b3b-a1a5-d724bb5ee682 | -4.51949 | -43.42061 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bff9f7ff-6e5a-35ac-8e8a-9b3de84d2aee | -4.48461 | -43.56176 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c41cda02-e138-3c05-91fd-fc2c6eff0c13 | -4.48168 | -43.55347 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d15ce720-15fe-3112-953d-6c5c13a831a5 | -4.46018 | -43.94818 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86ac8e31-57f0-3401-b51f-679139fa1b54 | -4.74887 | -44.1008 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e358d5a3-d12a-31ba-8c8f-f18f4a90bb48 | -4.73977 | -44.18663 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7b7d3c02-b4d3-3827-89f9-5207e68f4ab6 | -4.73907 | -44.09768 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f72e24ec-dac7-3305-b829-b142b619047f | -4.72492 | -44.59252 | 2024-10-25 16:52:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 257a4167-3816-3a97-a2bf-932725029051 | -4.70664 | -44.42364 | 2024-10-25 16:52:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 415ba15a-0437-3145-9318-c9de8ad10108 | -4.62363 | -44.66381 | 2024-10-25 16:52:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cb018a9d-43dc-3cb0-91ee-5cf79bde8534 | -4.62295 | -44.65961 | 2024-10-25 16:52:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5b7a1728-428b-31f7-8a46-7c3a66111912 | -4.61927 | -44.66455 | 2024-10-25 16:52:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 30aa38c0-4729-397b-b6e3-5d6e2245113a | -4.13606 | -43.243 | 2024-10-25 16:52:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2a66005b-c9cb-3950-ac34-7fa6b9782d6b | -4.13352 | -43.07644 | 2024-10-25 16:52:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 673c4935-d5ba-359d-a7b2-948b078bee11 | -4.09745 | -43.27287 | 2024-10-25 16:52:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c556ff07-2510-3307-8a9b-18ccf5b1443d | -3.99184 | -43.28735 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e3ce604c-4453-38de-aa7c-2a044ef11220 | -4.18387 | -43.21046 | 2024-10-25 16:52:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 054357ef-c39b-321a-9fb0-bdd459054a7b | -4.13121 | -43.24377 | 2024-10-25 16:52:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7dc9f12b-9b48-38a3-957a-8d3552e394eb | -4.08514 | -43.25824 | 2024-10-25 16:52:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 7b7dd9a8-80e6-37f8-a661-49fcc4662576 | -4.08029 | -43.25903 | 2024-10-25 16:52:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| cf2e8801-daab-364c-ae19-d3d06b89d507 | -4.00863 | -43.18793 | 2024-10-25 16:52:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 743c901d-d515-3b0f-8875-d60b847ee1b1 | -3.99097 | -43.28194 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e8e7aea1-3b1d-3e71-9ec7-36c5231963cc | -3.89628 | -43.27224 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 076af7c1-3d86-3e2a-96f9-b627933ae255 | -4.18588 | -43.21261 | 2024-10-25 16:52:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 507db775-d1a0-3841-a876-26c165d69055 | -4.0836 | -43.25691 | 2024-10-25 16:52:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 3accaca5-b53b-30c7-8f39-bc003f854e62 | -4.36034 | -43.26122 | 2024-10-25 16:52:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| cf5cd714-c436-3855-8c95-bba0f218992a | -4.33049 | -43.26064 | 2024-10-25 16:52:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 5cb0066d-d5da-33a7-9dce-3190e0564700 | -4.32697 | -43.26371 | 2024-10-25 16:52:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69c1c298-5e21-3cbd-83a2-312b093c2126 | -4.28592 | -43.74064 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1c89fb95-2c1d-3110-9f6c-e8896c83b447 | -4.28124 | -43.74139 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ead796d2-340d-3ec2-8cc0-ecf0de1ab9a7 | -4.27943 | -43.74387 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| bb6f321d-7083-33f1-923b-192d753f9f49 | -4.27657 | -43.74213 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4e89557c-595f-3b4d-b574-d576179b2288 | -4.16775 | -43.31434 | 2024-10-25 16:52:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fb1b8f0b-1a46-3786-bc3e-88ba7dda4081 | -4.13358 | -43.34702 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4f72b6b9-8d13-37fc-a0d8-89286462c908 | -4.13271 | -43.34183 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 277bc6ce-070d-37cc-b489-de12e87b5ed6 | -4.09605 | -43.27151 | 2024-10-25 16:52:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5f0e8731-6915-3f19-a840-b4c222c2db31 | -4.08943 | -43.75956 | 2024-10-25 16:52:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3bfcc7fd-5e98-31e1-9455-453b1c6175ad | -4.07536 | -43.32019 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8c004b39-96fc-3e7b-be22-8569760da804 | -4.01052 | -43.9352 | 2024-10-25 16:52:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f1f21cd4-c9e3-39c0-b0f6-56b5cd6d5b80 | -3.99005 | -43.28537 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d61b5dca-2b4a-3dc8-8cb9-bb1b5a09e396 | -3.77939 | -43.40229 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| ff9fd060-617d-3231-9750-cc91f27fd0b0 | -3.77856 | -43.39716 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7a237f61-15b0-338c-a64f-e83f3d3dced8 | -3.77456 | -43.40306 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d7a0cb36-fa06-3785-8cfa-90b3dac7727c | -3.77372 | -43.39784 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b1802e98-5ce3-31c2-a3b7-9f02edea2077 | -3.61979 | -43.96035 | 2024-10-25 16:52:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 80bb3b99-6ddd-380d-9ae8-9602842adc38 | -4.13657 | -44.15422 | 2024-10-25 16:52:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f87ee8e2-389a-37da-a4a9-038abdf71394 | -4.13579 | -44.14957 | 2024-10-25 16:52:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 02e44109-88be-3e23-88da-de80cfd5774f | -4.13563 | -44.15254 | 2024-10-25 16:52:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d9e0b083-0476-3c8a-9d52-c0e6270fc2b9 | -4.02753 | -44.09378 | 2024-10-25 16:52:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 68f0d40c-0d1d-3887-b776-bde0ecf0d6de | -4.02711 | -44.09217 | 2024-10-25 16:52:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 01a6400c-e07f-3319-bc4e-aa136eb89421 | -3.85694 | -44.0294 | 2024-10-25 16:52:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5e96e4da-9ede-38d1-bb1c-2e3946a7cb09 | -3.84172 | -44.08096 | 2024-10-25 16:52:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0b418581-e154-30d4-a40c-48cea73502c8 | -3.84093 | -44.07615 | 2024-10-25 16:52:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7923ae18-97dc-3c30-b546-94ef5ff2b8fd | -3.83253 | -44.08247 | 2024-10-25 16:52:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0a75275e-803f-37e7-bcce-ec6b5de038e5 | -3.71581 | -44.03151 | 2024-10-25 16:52:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 1ce1618a-b271-3005-be25-a4214d837789 | -3.58516 | -44.01088 | 2024-10-25 16:52:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 09f532a2-5956-3302-8834-7e1e9e3bb5bd | -3.58127 | -44.0085 | 2024-10-25 16:52:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 78884f2f-4d96-3fcc-89bd-6430cdac7521 | -4.36058 | -44.60061 | 2024-10-25 16:52:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fdad049a-3814-3e44-a5b6-fc5f611c8a89 | -4.35907 | -44.33972 | 2024-10-25 16:52:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f4508943-bf58-3cf0-a8b9-d3d8117172db | -4.33403 | -44.63117 | 2024-10-25 16:52:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e0c4a5d5-3c7b-3f63-b522-c9f6fe587f3f | -4.32964 | -44.63187 | 2024-10-25 16:52:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 96bc7fd5-c136-31ca-b877-1192e7332a82 | -4.32915 | -44.63032 | 2024-10-25 16:52:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f1788f0b-9aa9-31ff-acc2-26cf4a9e152b | -3.82295 | -44.37282 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 3712842d-a150-3e86-8133-386f66c261bd | -3.81405 | -44.51697 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| fe89b211-7031-3d2f-9191-844b65ab7cc0 | -3.75004 | -44.32398 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dbdc7544-9e57-3d11-865f-9008f7e04aae | -3.73575 | -44.34987 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 427d096a-9638-3e0f-a0b8-52847152f1a1 | -3.73499 | -44.34531 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 57fff0c1-a9fc-3cc6-a077-4230c52c1d31 | -3.73409 | -44.34852 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 66014887-f3ef-3dbe-9012-775ceceb49a4 | -3.71439 | -44.37035 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f49d93bb-64fe-307a-81fd-d8ea62ba92df | -3.79987 | -43.23299 | 2024-10-25 16:52:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 3e66ad65-1430-367a-a155-ca70337a4802 | -5.91598 | -43.92303 | 2024-10-25 16:52:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| fb35ffe8-6097-3e91-ab15-aa62e1125b8c | -5.91149 | -43.92379 | 2024-10-25 16:52:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 7a8339e6-2257-3858-a73a-51db59be6149 | -5.88153 | -43.68616 | 2024-10-25 16:52:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9eab8b96-035a-3f99-99cd-cf8cb1eebf97 | -5.82767 | -43.72873 | 2024-10-25 16:52:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4c30e524-1ef8-35fb-9f71-6c649a8d453f | -5.81614 | -43.60501 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 3d1c52fe-be93-3eec-9174-0bd2eb0a95d9 | -5.80633 | -43.88668 | 2024-10-25 16:52:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0a7686ec-24dd-3d4c-b591-09dc6f181705 | -5.80556 | -43.88201 | 2024-10-25 16:52:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 097d7763-5bed-3321-bfff-65351d4843f3 | -5.8054 | -43.42841 | 2024-10-25 16:52:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f3fdc405-45b3-3b34-8ac1-8d437e4b5741 | -5.72836 | -43.80983 | 2024-10-25 16:52:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |


[Clique aqui para ver as próximas entradas](README170.md)
