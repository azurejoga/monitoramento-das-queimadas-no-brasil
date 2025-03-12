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
| 0d9e60b0-bb82-3fc7-bb64-1c37f2a3d002 | -19.6136 | -44.13858 | 2025-03-12 04:29:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f2ed6cb-a529-3b9e-8424-1b7d0fb0f097 | -25.78552 | -53.30819 | 2025-03-12 04:32:00 | NOAA-21 | SALTO DO LONTRA | PARANÁ | Brasil | 4123006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ee8ca329-1d38-36a9-9064-d2bf198f3412 | -25.78792 | -53.3073 | 2025-03-12 04:32:00 | NOAA-21 | SALTO DO LONTRA | PARANÁ | Brasil | 4123006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 142cd528-649f-3ae2-8029-cab289b513f7 | -30.35899 | -55.29486 | 2025-03-12 04:34:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 961fafe4-8ad9-3965-ae08-a27871ef0aab | -32.36157 | -52.38026 | 2025-03-12 04:34:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 947ff049-2249-3d88-bbf7-020b21f7afa9 | -30.36251 | -55.29569 | 2025-03-12 04:34:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 506f5701-31b0-33f5-9887-a31267db9d40 | -32.35826 | -52.37955 | 2025-03-12 04:34:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 37519eeb-39de-36e9-8864-86a35347fb8a | -33.13761 | -52.90265 | 2025-03-12 04:34:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| d827ab2d-a046-3c4f-9d3f-4e419b5d3394 | -6.97823 | -35.15496 | 2025-03-12 04:42:00 | AQUA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 0e4204ab-41bf-3220-9710-971bc13d76dd | -6.97676 | -35.16442 | 2025-03-12 04:42:00 | AQUA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| e5fb19ce-fb97-3c3d-a545-e3d45a457648 | -2.04302 | -50.79475 | 2025-03-12 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6d410e8-9cba-3f13-a471-9b2a9e03a4d3 | -13.75642 | -41.86263 | 2025-03-12 04:53:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2fbe452-51b2-3cdb-b60f-849a93b642d7 | -16.68317 | -43.88501 | 2025-03-12 04:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea21b2c9-5dba-3e94-982e-81781d4c9359 | -16.67722 | -43.88409 | 2025-03-12 04:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42522af9-4314-3803-9e01-d123eb44c95d | -12.72586 | -56.98236 | 2025-03-12 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac8f1558-b07d-3bd4-8143-4b5d97be86fd | -12.72516 | -56.98651 | 2025-03-12 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50b4e9a7-3957-3ac3-9ec5-e5113eeb99e9 | -15.26343 | -51.47621 | 2025-03-12 04:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a9e0be2-f659-3989-8793-33d0afca10f5 | -15.26404 | -51.47194 | 2025-03-12 04:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9ef1beb-9113-3a02-b3df-72b9759dd495 | -13.75578 | -41.86825 | 2025-03-12 04:53:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7efa049-ca68-3ace-acb5-039ccc75a58b | -13.75579 | -41.8632 | 2025-03-12 04:53:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 551d5769-966a-33bc-8606-4fe941905910 | -11.45208 | -52.92391 | 2025-03-12 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a274ab0b-4ba6-32c8-8754-595b0f1631bc | -21.25398 | -48.72157 | 2025-03-12 04:55:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b4a5d1e2-4220-39a8-baf5-ac3031523828 | -18.63642 | -47.98074 | 2025-03-12 04:55:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d08f2d8-2933-343e-9cb7-175a836bdaf1 | -30.35732 | -55.29798 | 2025-03-12 04:57:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 4766da05-b306-37ba-830a-a9fd41aad5d4 | -30.36089 | -55.29863 | 2025-03-12 04:57:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 9e84cfc5-d827-39ed-9c0b-98dd5c1a33e7 | -30.3615 | -55.29409 | 2025-03-12 04:57:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| f197e083-a037-3be6-9e9c-03ff8ac6b30a | -1.56499 | -54.01299 | 2025-03-12 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e0e5c94-6c16-3b84-b3bf-763885a0a90e | -2.04275 | -50.79595 | 2025-03-12 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e7b4a66-7393-3897-aba2-ecc532d1902d | -2.04467 | -50.79347 | 2025-03-12 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c2e6651-07e2-3e54-9695-a16cda32171a | -2.04347 | -50.7911 | 2025-03-12 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76f144eb-8a2b-311c-a496-fc6c21d2e819 | -1.77237 | -53.84617 | 2025-03-12 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57f03d80-9968-306b-bc75-319cf49574a7 | -12.72528 | -56.98277 | 2025-03-12 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f2034ae0-279d-3630-bc32-dc48b1ff7a6c | -30.35701 | -55.29485 | 2025-03-12 05:23:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| ffe18ddc-25b9-3bf5-9a81-e2bfe64d23b7 | -30.36206 | -55.29557 | 2025-03-12 05:23:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| ba242348-69da-3f48-9c47-30867240bd89 | -30.36103 | -55.29287 | 2025-03-12 05:23:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| aeea25b7-87b0-3118-81dc-ae3340f3d500 | -30.36077 | -55.29608 | 2025-03-12 05:23:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 122c2b5c-1e0f-3a6d-9563-3d5cdfdb8468 | -30.36179 | -55.29866 | 2025-03-12 05:23:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 4cc495b0-5541-38a5-8960-57c0483e732a | -7.85352 | -44.2349 | 2025-03-12 12:42:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| e7e238ce-c1cf-31d9-bc67-d0956251d4f1 | -7.84691 | -44.22751 | 2025-03-12 12:42:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 328e6bc8-4e80-3f41-8a37-236e47c2097a | -17.56209 | -46.48324 | 2025-03-12 12:44:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3a011a02-af25-34db-8699-7b2c6dbabe7f | -12.26166 | -44.59039 | 2025-03-12 12:44:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 05b364a1-2ef7-3335-a7c4-07f29ed99e5b | -12.52888 | -45.47713 | 2025-03-12 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 2d2fda04-0b43-38cf-bd79-95cc37728ab7 | -17.05395 | -46.92303 | 2025-03-12 12:44:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 8c41e42a-3fce-3265-b336-5e63da8ca6c6 | -13.31991 | -46.75504 | 2025-03-12 12:44:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 76d9ec15-e196-3238-bc1d-150efa30d14b | -8.38502 | -44.04009 | 2025-03-12 12:44:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 97c6467b-9d07-3cbd-b1d6-3ebe9601a814 | -15.37489 | -43.76108 | 2025-03-12 12:44:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 2ede25ef-bb48-37c0-a7c2-b2eb850086fa | -15.38263 | -43.75528 | 2025-03-12 12:44:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 571fef70-4b66-3e6d-983c-06bc8b871a4f | -13.62345 | -47.80165 | 2025-03-12 12:44:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 825999fa-bcb7-39f1-8e49-154ea1edeee3 | -16.37559 | -45.09398 | 2025-03-12 12:44:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e107390c-bb9e-3992-bafb-fc8fae76b577 | -12.53782 | -45.48427 | 2025-03-12 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| cdd5ced5-305b-3fbe-b31e-e00ceb8dc6eb | -12.05146 | -54.38945 | 2025-03-12 12:44:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6d484e17-479a-39d0-8780-20f222079a12 | -17.05226 | -46.93729 | 2025-03-12 12:44:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3813905f-f262-31a1-8683-ac2b59e4db0d | -13.62423 | -47.80836 | 2025-03-12 12:44:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 622bb654-f4fb-3a97-9868-8835958d2ff2 | -10.15301 | -48.00089 | 2025-03-12 12:44:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6414ef90-4ef6-3947-aa09-545b27456162 | -12.52688 | -45.49295 | 2025-03-12 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 102e82f1-678d-34b7-8a78-00cf2ae746f5 | -10.13324 | -47.93651 | 2025-03-12 12:44:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 687c8bb1-4d6e-3988-ae12-c268be89e385 | -8.38203 | -43.96769 | 2025-03-12 12:44:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| ce9aff25-377e-36a7-ba8a-cf6b6c239b06 | -10.40463 | -47.97163 | 2025-03-12 12:44:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1a3fe544-406d-3740-aa93-591778a834fc | -13.00419 | -45.04482 | 2025-03-12 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| d08f570b-839c-325a-b2c5-cedf1dee819c | -11.05746 | -40.58226 | 2025-03-12 12:44:00 | TERRA_M-T | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 2dab7769-91bf-3667-9d42-49b18a06c5ef | -11.76223 | -54.74073 | 2025-03-12 12:44:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0e7c0bb4-1678-3459-9295-9238ac7fb632 | -11.966 | -40.59988 | 2025-03-12 12:44:00 | TERRA_M-T | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 2019f31e-3dd8-38ef-94de-a92e3aec7ee8 | -13.00811 | -44.46281 | 2025-03-12 12:44:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| ae6fd3b1-c510-3fff-84c1-416e8a06a296 | -10.31215 | -48.64597 | 2025-03-12 12:44:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 906253df-4f71-30f4-b5b3-45b688cad0d8 | -10.09162 | -47.49169 | 2025-03-12 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f9996223-2f0b-3ecd-a643-1b338a25119e | -13.96145 | -55.14866 | 2025-03-12 12:44:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b6a0a101-03d3-345b-bbbb-7ba7906659e2 | -11.96125 | -40.59305 | 2025-03-12 12:44:00 | TERRA_M-T | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 7f40b641-8833-3c99-94fd-095b4d37925d | -26.4853 | -49.04897 | 2025-03-12 12:49:00 | TERRA_M-T | JARAGUÁ DO SUL | SANTA CATARINA | Brasil | 4208906 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e6f64aaa-94e0-3342-ace5-e22db7d903f6 | -30.70284 | -52.76517 | 2025-03-12 12:49:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 15.7 |
| 97b4eccd-4fe0-339f-947b-b772574227ae | -13.015 | -45.036 | 2025-03-12 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 6181ce1e-09ab-32a3-abdd-615153babc5a | -13.015 | -45.036 | 2025-03-12 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 660063f5-bc40-3b7e-80ec-3c78543fd515 | -13.015 | -45.036 | 2025-03-12 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 6a79d83b-1ca2-39bf-a71b-5e0d358790e8 | -13.015 | -45.036 | 2025-03-12 14:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |


