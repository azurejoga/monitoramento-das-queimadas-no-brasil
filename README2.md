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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfeb6a56-79e5-3914-b318-50a9e5998ed3 | -7.80865 | -44.1908 | 2025-02-27 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faa434ce-c6fb-3102-b1d9-0da4b6d94a68 | -7.80928 | -44.18706 | 2025-02-27 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 318c02d5-67c6-32d8-85a7-5bbd1994e90e | -10.48487 | -42.42092 | 2025-02-27 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 41ec6430-af17-322d-ab71-d5cb1fd42e52 | -9.79827 | -41.96688 | 2025-02-27 03:55:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0f3df871-7dc5-31ed-b98e-64adeef18e34 | -10.53263 | -42.42807 | 2025-02-27 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10cc4c33-740d-34f8-9b6d-157e9dce6f08 | -6.96917 | -43.01273 | 2025-02-27 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0760996e-54ce-3401-be87-dd5a6d12e3dc | -7.05141 | -44.34891 | 2025-02-27 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff1e63bd-7444-30dc-835e-c1afa65d4144 | -9.87379 | -37.12904 | 2025-02-27 03:55:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6be7bb33-3209-3197-8908-786f4604866d | -8.1209 | -43.14421 | 2025-02-27 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51f617e8-e9bf-3a06-9fd8-6aa9d37864db | -6.95799 | -43.00918 | 2025-02-27 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 955baff3-4fbb-37d0-840d-3b52f10c11ac | -10.53526 | -42.42947 | 2025-02-27 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2e062d31-e78a-39a4-9ed7-433f352857de | -10.53192 | -42.43222 | 2025-02-27 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c3c6d500-82e2-3dd1-b4a2-91dc0d7c004c | -7.80513 | -44.18637 | 2025-02-27 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72cb1420-c146-3817-9835-f5ed7284c919 | -8.6482 | -36.77559 | 2025-02-27 03:55:00 | NPP-375D | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8dd05bc3-499d-38ac-801f-386c55a4fd0c | -7.0592 | -44.35453 | 2025-02-27 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6ce43f2-de89-3d21-99f7-165262e62b8e | -7.285 | -43.72311 | 2025-02-27 03:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0949967c-4016-3825-9168-e5178ff52463 | -6.96969 | -43.0111 | 2025-02-27 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 90b4f1c4-1477-32c4-9a67-83aa01ecdc4c | -7.05497 | -44.35374 | 2025-02-27 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a6e6806-db5b-377c-b204-47e55b3a6293 | -7.05564 | -44.34972 | 2025-02-27 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e38526e-0c81-3d55-9562-18f69b5682c4 | -10.53166 | -42.42886 | 2025-02-27 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bd204731-4931-3712-b0e5-095d559f32b3 | -6.9739 | -43.00847 | 2025-02-27 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e60a0538-272d-3c50-850e-169d12173b18 | -6.96527 | -43.01207 | 2025-02-27 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 17a92565-fe91-37a3-9a77-4dad007f9aed | -8.11318 | -43.1429 | 2025-02-27 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ace96b28-6fc1-351b-8713-cc06b6268460 | -6.96611 | -43.00717 | 2025-02-27 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4be94fc0-6776-36de-964e-8ae76dced485 | -6.97358 | -43.01179 | 2025-02-27 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 813bf602-d26e-3366-b4dc-3f0ef15b6376 | -9.8143 | -36.99593 | 2025-02-27 03:55:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0ee619ea-6414-3b6b-897c-9e1ec10b890c | -10.48847 | -42.42153 | 2025-02-27 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bb443756-7ce7-3812-b8a2-de08196ad384 | -10.49573 | -40.39169 | 2025-02-27 03:55:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a884ba3c-95e6-32d2-b882-cc861d80a457 | -8.45572 | -36.38078 | 2025-02-27 03:55:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 91ce533d-7294-3d21-b314-d7893ec33a09 | -8.11398 | -43.13806 | 2025-02-27 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fb3c1838-ccc2-368f-a507-c0b735ec20ba | -6.17226 | -44.38932 | 2025-02-27 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58840c3f-ef01-3d01-8d78-ebb895b14282 | -10.69527 | -37.04926 | 2025-02-27 03:55:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 83f1816f-c4c5-35dd-8cbb-3b43e48db88a | -6.96579 | -43.01046 | 2025-02-27 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 410c3653-5ba6-335f-8903-2898ed128c78 | -8.11704 | -43.14355 | 2025-02-27 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cdd6cbf5-ed43-3053-95e7-06f6ac1e8ddf | -15.37442 | -43.71917 | 2025-02-27 03:57:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c006a8c-b8fe-3de7-b601-41b46548d85c | -17.67687 | -42.74033 | 2025-02-27 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0210c6d5-a5aa-3690-b5a6-ba576fdf8180 | -15.50122 | -44.77396 | 2025-02-27 03:57:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7255e2a-f941-3050-9bbf-0706e4e88c78 | -18.90385 | -45.04152 | 2025-02-27 03:57:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c190d142-165d-3635-ae10-85a5795a9933 | -15.08789 | -42.44666 | 2025-02-27 03:57:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 79f68f28-c296-376d-a93a-719cf99e0cac | -19.43662 | -44.3404 | 2025-02-27 03:57:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5247b30b-7ad5-36b7-8488-6bb71b9986a5 | -16.68275 | -43.88255 | 2025-02-27 03:57:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6de8b530-1998-396a-8b7e-7affd6b95aa7 | -16.34751 | -43.69596 | 2025-02-27 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3650ad7-690e-38ad-a1c2-a9094f20474c | -20.43072 | -42.70811 | 2025-02-27 03:57:00 | NPP-375D | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 30ff768f-956d-3dc8-b298-5a7c015230eb | -14.0416 | -41.45731 | 2025-02-27 03:57:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 947a4473-99a0-3c55-8c7c-a855cb7221fb | -17.77754 | -42.80895 | 2025-02-27 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f11d9d08-8100-31c5-8415-71ee37be68bd | -18.58801 | -46.58391 | 2025-02-27 03:57:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42fc7581-15e9-39c4-ba45-1530eb090286 | -15.34839 | -42.10475 | 2025-02-27 03:57:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6b5d2ea8-96a2-313c-a813-e95d0468b663 | -15.34499 | -42.10418 | 2025-02-27 03:57:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 88ea7749-59d0-368b-88bf-7aba4ade77a2 | -13.813 | -43.34057 | 2025-02-27 03:57:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f0a4821-c7e9-3e84-b731-872d80061398 | -17.30126 | -46.29359 | 2025-02-27 03:57:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e029bd1-1150-371c-a2d8-cb06cc984ceb | -18.58789 | -46.58352 | 2025-02-27 03:57:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ec9028b-e680-3e48-bda0-e5aeeda76096 | -20.4167 | -43.55331 | 2025-02-27 03:57:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| f2f11a0c-352f-3485-920f-74016887c61b | -17.67624 | -42.74414 | 2025-02-27 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 966d54de-6f59-32e6-ab42-04b27d57efe8 | -16.68108 | -43.88387 | 2025-02-27 03:57:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f79d2b0-2f21-3542-b193-53f682c5a1e1 | -19.90703 | -45.23857 | 2025-02-27 03:57:00 | NPP-375D | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6e71a13-dab3-36ac-a43c-33ec8f547818 | -20.31597 | -46.73311 | 2025-02-27 03:59:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f57ffbcb-3dfd-3787-9157-28d0ecd9270a | -22.74058 | -42.84657 | 2025-02-27 03:59:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 26e114e9-130a-3d5a-a2e3-f4dda8f418e4 | -22.8456 | -42.31727 | 2025-02-27 03:59:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 96119b9f-3820-3f38-88bd-90782bf23154 | -23.20437 | -46.60265 | 2025-02-27 03:59:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d43f1c7-2210-3316-9dc7-c031f0250392 | -22.27164 | -42.73405 | 2025-02-27 03:59:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 754d3de2-a592-3655-866a-9622d6fe90d7 | -21.8626 | -43.08265 | 2025-02-27 03:59:00 | NPP-375D | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| df579038-6a5e-32ac-ba11-9b21f2b61aa9 | -22.67474 | -42.85824 | 2025-02-27 03:59:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bb5d4d05-158b-3097-8f28-18a1e68efe69 | -22.55619 | -42.79433 | 2025-02-27 03:59:00 | NPP-375D | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 588cae6b-8b80-3e7a-9f56-da48977cce7f | -21.04954 | -47.78215 | 2025-02-27 03:59:00 | NPP-375D | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 41.4 |
| c110793b-056b-39c9-925a-893ebed15804 | -25.61444 | -49.35007 | 2025-02-27 03:59:00 | NPP-375D | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7503aafc-18e0-3568-8321-9a4f561b99b0 | -22.85789 | -42.98054 | 2025-02-27 03:59:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 67a702d4-6db8-30d4-9221-bc03a73fba38 | -21.62752 | -43.46861 | 2025-02-27 03:59:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| da2be413-4a46-328a-871b-d01e62cc3ae8 | -23.50719 | -47.3754 | 2025-02-27 03:59:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9eb8f950-10ac-30b7-aa19-9d76d893288b | -22.65369 | -43.29462 | 2025-02-27 03:59:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3bfa8491-eef2-3dc6-96c0-83a8be2a90e1 | -22.9564 | -46.78788 | 2025-02-27 03:59:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6cca85a6-a276-3de2-9b97-b764ea938b10 | -22.78684 | -43.7558 | 2025-02-27 03:59:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c1beed33-1802-3472-be19-c7ba8ef97019 | -22.64674 | -42.24776 | 2025-02-27 03:59:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f68b4220-20db-35b2-9546-8d9d620f3e68 | -22.92363 | -45.41544 | 2025-02-27 03:59:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 231f001f-f1f8-37f9-a925-9e2fc88c6080 | -21.04877 | -47.78614 | 2025-02-27 03:59:00 | NPP-375D | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 748b9649-1710-3eaa-afba-77e19d5cce62 | -22.64341 | -42.24716 | 2025-02-27 03:59:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3f4a3edc-3d8c-3516-812b-21e7db786728 | -22.67868 | -42.8551 | 2025-02-27 03:59:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9f9526f4-8e94-3df1-9355-feb965d9f572 | -21.34821 | -48.6489 | 2025-02-27 03:59:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1cd4cb74-240e-3d41-9ecc-fb25c627fafe | -23.5659 | -47.88073 | 2025-02-27 03:59:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 43533353-ee63-3b13-99b8-d514427f186b | -22.90256 | -43.75313 | 2025-02-27 03:59:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8328fcdb-c885-3f92-a19a-1d786d3bb08a | -22.78547 | -43.38196 | 2025-02-27 03:59:00 | NPP-375D | SÃO JOÃO DE MERITI | RIO DE JANEIRO | Brasil | 3305109 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 58a29fa2-3d00-3d1b-84b1-e18464fde4ed | -20.30693 | -46.73737 | 2025-02-27 03:59:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f74a6f8-7c1b-3217-b8a2-cd337cd0e75a | -23.99078 | -48.32588 | 2025-02-27 03:59:00 | NPP-375D | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 06730163-5770-3022-be8b-77881ecf5e0b | -23.40738 | -46.55565 | 2025-02-27 03:59:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b26c4a7-c9c0-36fc-a027-78a9057a465b | -21.34908 | -48.64439 | 2025-02-27 03:59:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0e408390-7b3e-3480-a621-0f1d90ae77fc | -22.85381 | -42.54648 | 2025-02-27 03:59:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1638059f-f2e0-301e-9537-75c5967a9220 | -21.86595 | -43.0833 | 2025-02-27 03:59:00 | NPP-375D | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 72bfa8eb-c7af-39bf-a683-c423c973fbf2 | -22.85048 | -42.54586 | 2025-02-27 03:59:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8b331b1d-691e-38fc-aeab-32df30bafc72 | -20.76498 | -46.7687 | 2025-02-27 03:59:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d51e9fa-ae08-3a23-83c6-b67cfe0fd807 | -22.27225 | -42.7303 | 2025-02-27 03:59:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dbd442e5-4e7a-31b3-b72c-3ca233e68491 | -22.65672 | -42.24959 | 2025-02-27 03:59:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 33ca60e2-a825-3e8f-9be4-e8924ecd1029 | -21.4785 | -45.24548 | 2025-02-27 03:59:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b1d4a86d-e74e-3db4-ad4e-072324b9d120 | -23.29735 | -46.68739 | 2025-02-27 03:59:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a3dcfec0-6192-3aac-a8db-4c51aea48a61 | -20.90016 | -43.82097 | 2025-02-27 03:59:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7728d34e-48bc-3515-b857-d5295adc18d2 | -22.644 | -42.24342 | 2025-02-27 03:59:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 374ad669-ab08-3a71-9a61-b0b215d2b55c | -22.92006 | -45.41471 | 2025-02-27 03:59:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 875f082f-dd6e-359b-9ea3-da76a1ea060b | -22.67535 | -42.85447 | 2025-02-27 03:59:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7cc7a4a9-dcda-3ff3-8224-e9c0369ca865 | -21.34796 | -48.646 | 2025-02-27 03:59:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3c931e71-484d-343b-85f9-b041d0a98b5a | -20.31199 | -46.73242 | 2025-02-27 03:59:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2dac85b-c529-3c2a-b00b-93e748ca2f1b | -22.54 | -48.81114 | 2025-02-27 03:59:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9c5353d-1666-3369-8fa5-d5815357d297 | -21.0553 | -47.777 | 2025-02-27 04:00:00 | GOES-16 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 83.8 |


[Clique aqui para ver as próximas entradas](README3.md)
