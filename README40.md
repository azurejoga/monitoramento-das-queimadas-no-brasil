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
| 4601a44d-81aa-3791-ad97-e203e575137c | -3.12245 | -53.7602 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d2d9d5a-310d-38fd-aadf-aea270953e0d | -3.1214 | -53.74478 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83133cca-3d56-33ca-969b-442a3c655c82 | -3.1208 | -53.7485 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e32a28f9-e925-3f04-8a36-6a9d205d13a1 | -3.12021 | -53.75222 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a0a1196-c6c4-34d8-98a2-edd8c0c2fc2a | -3.11962 | -53.75594 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78c66352-5d68-3adf-ae6e-6c2ba8f9526d | -3.11678 | -53.75168 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6c710c0-b545-3fd9-9a12-a682ff71d36a | -2.9362 | -53.69718 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9211d6ca-08f9-37d6-8665-27062415b618 | -2.88076 | -54.79658 | 2024-09-29 04:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57902355-2717-32bd-8447-1eeebad85a37 | -2.83126 | -54.60943 | 2024-09-29 04:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95bb9e4e-aea0-32eb-8083-fe2197675935 | -2.74028 | -54.13297 | 2024-09-29 04:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caac05a1-5844-33ad-8f82-84073e5fdfd8 | -2.64216 | -54.33905 | 2024-09-29 04:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de7a3019-37ac-303e-8410-ca7df8db688c | -2.63516 | -54.26922 | 2024-09-29 04:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8797b761-8537-359a-9401-a859bd574165 | -2.61598 | -54.93189 | 2024-09-29 04:46:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 385f6984-250a-3057-a6e5-64fdc4ee2478 | -2.55541 | -54.60964 | 2024-09-29 04:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7b4298e4-99a0-38e3-922d-e511e02f8056 | -2.55182 | -54.60915 | 2024-09-29 04:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 63d9e2dd-2c14-321b-9339-7dbbfa159d04 | -1.68902 | -55.66517 | 2024-09-29 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbd8f5d3-b7be-3073-9608-42b096611b40 | -1.67051 | -55.13916 | 2024-09-29 04:46:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71056f62-a17c-3517-8a86-e3c22b0a2ee9 | -1.66982 | -55.14359 | 2024-09-29 04:46:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12eb4dff-6a16-3860-9b02-760cb10434e2 | -1.53802 | -55.17012 | 2024-09-29 04:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12481550-6c5a-3905-8a12-483679205dc1 | -2.24176 | -55.81162 | 2024-09-29 04:46:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66cd69a6-e258-331b-8664-ac88942e33b7 | -2.68527 | -57.51184 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bb3462d-e70f-3f78-8ece-6542e5ebd019 | -2.68164 | -57.50717 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 879dbf5e-a853-39f8-b70e-a115eeb9f442 | -2.68101 | -57.51114 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74eaa6f3-0d5e-3e8b-a1e2-e7a2044c0111 | -2.67376 | -57.50179 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e808e07e-159c-3d7d-9635-4a89da7aa0bd | -2.67312 | -57.50577 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70d6c40d-6817-3ba7-9a35-b28cbb789bc3 | -2.6695 | -57.50109 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a59e12fc-e7bb-3d99-b118-968fe6a5f8b1 | -2.66886 | -57.50507 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84c07c6a-0d18-3f41-b5dd-7de4f2047dfc | -2.66524 | -57.5004 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4c0e5f3-1d69-3af4-8936-3f48c2189f20 | -2.6646 | -57.50438 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f02ea00-0a6e-34a0-97ee-d5dd28fe1df7 | -2.66034 | -57.50369 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ab16bc4-860a-3fdf-9a17-2d2f6582de4f | -2.6597 | -57.50767 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abe2236a-901a-379a-be46-d44e2136508c | -2.65608 | -57.50299 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 987561a7-2734-3dde-a7ae-fb1cdb5085f0 | -2.65544 | -57.50697 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74eef4be-d6c5-3405-b9d3-4b83ff1c6e5f | -2.65479 | -57.51096 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eba2e6c4-9f4f-30cd-9165-cd8c74382a7e | -2.65182 | -57.5023 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d4d12d7-da3a-3d04-a1b9-a8478163157e | -2.65118 | -57.50629 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5131c73-7579-37f6-b246-4b48907d7f67 | -2.65053 | -57.51027 | 2024-09-29 04:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a8cba78-f2a1-3757-8d53-edac97af947a | 4.30943 | -60.9307 | 2024-09-29 04:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edcc0057-30d1-3dbf-b8ce-3005814f678a | -10.25293 | -43.56586 | 2024-09-29 04:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52f3dcf5-0eb3-31a9-a3d0-0d41b3ff47d7 | -10.25245 | -43.56963 | 2024-09-29 04:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a73c9f-c22e-371a-af65-c282b2662141 | -10.25101 | -43.58107 | 2024-09-29 04:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c647a54-b50f-3dc6-bdab-bc973d045595 | -10.25052 | -43.58495 | 2024-09-29 04:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6e75847-567f-3ba9-90c1-83c10a8c1a8c | -8.43445 | -41.93134 | 2024-09-29 04:49:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 870b0155-6cdc-3406-bca4-1391b66d2e2d | -8.43389 | -41.93572 | 2024-09-29 04:49:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 54120c90-4077-383b-8d7d-cdd4b93caf89 | -8.42886 | -41.92717 | 2024-09-29 04:49:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 45706461-ebe7-3f01-8a09-bf0e80e9d44f | -5.94507 | -43.28316 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 03359823-7b3d-3c44-9f98-1a21e84ec5da | -5.94052 | -43.39064 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b296e3a7-6d46-3e21-a924-6fe5dfd5fd4e | -5.93974 | -43.28245 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b8681a5f-e080-39bd-9654-6118e733e90e | -5.9357 | -43.38661 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc16e073-3399-350d-9ed4-a458e04f44d4 | -5.93441 | -43.28169 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 64a4dd20-c04e-3b10-88c5-0fd700fc76e4 | -6.43288 | -43.34991 | 2024-09-29 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9f377dd-3c3b-36b2-b6c7-79398f66aa1b | -6.43243 | -43.35318 | 2024-09-29 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fa212ce-ae4c-30c2-8f35-a4fb9204ef18 | -9.28538 | -43.49784 | 2024-09-29 04:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6738078b-19a0-3c38-98e8-8f59c12c9ca4 | -9.28491 | -43.5015 | 2024-09-29 04:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8bd8b41a-9f98-3afc-82ab-173aa1be6d95 | -9.28445 | -43.50514 | 2024-09-29 04:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 53c7abcb-de93-37ce-8a9d-465ec2c78cc8 | -9.27987 | -43.49713 | 2024-09-29 04:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5432ce20-b95a-3dd9-b071-579878454409 | -9.2794 | -43.50079 | 2024-09-29 04:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7f10a406-c733-35a0-807e-1ed6c82a9732 | -9.18411 | -43.41391 | 2024-09-29 04:49:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 52f7ddf7-a099-3124-96b9-41bef3990052 | -8.72138 | -44.0201 | 2024-09-29 04:49:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c0a5083-3528-3091-81b0-901bec5ab27f | -8.72095 | -44.02326 | 2024-09-29 04:49:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16f63fd7-73a8-3ec7-b080-2c3cc399de4a | -8.71568 | -44.02252 | 2024-09-29 04:49:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4885412e-1832-3228-bdf2-694b402a5a68 | -9.94299 | -44.04084 | 2024-09-29 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a3221e0-af61-3558-be5d-066328fa65ce | -9.93761 | -44.04023 | 2024-09-29 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1ae2bea-b677-3878-b9bb-b27a0ce8fdf9 | -9.93716 | -44.04361 | 2024-09-29 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8c6a991-f188-30a3-9117-aaebfb919160 | -10.25897 | -43.56282 | 2024-09-29 04:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 012421a3-bd6d-3baf-8cb6-e7a724d00d3c | -10.25849 | -43.56658 | 2024-09-29 04:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae49022c-f1c0-3542-9d44-0d5c38ec7fdd | -10.25656 | -43.58181 | 2024-09-29 04:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e59e1cc1-2692-3a4b-aa8b-36646a1f0e4e | -10.25606 | -43.5857 | 2024-09-29 04:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1a8101f-dea1-3b5d-8646-dc512a52d5a7 | -10.25341 | -43.5621 | 2024-09-29 04:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca5e0468-5ff3-31ac-b0ed-d795ed027ab9 | -10.24546 | -43.58034 | 2024-09-29 04:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 460b6854-85cf-36f5-a43c-06b932291e82 | -12.08722 | -44.18876 | 2024-09-29 04:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8581c57e-19d1-3556-b228-dd8c862c25b0 | -12.08136 | -44.19129 | 2024-09-29 04:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 075cf08a-e1bb-3ffe-ac7e-387b1777dd71 | -11.88104 | -43.81654 | 2024-09-29 04:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5411d0c-3071-359e-a401-0a5a84abc1c7 | -11.88057 | -43.82027 | 2024-09-29 04:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfd1a541-fcf5-3322-b711-55d5164c1dfb | -11.8801 | -43.82404 | 2024-09-29 04:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38d94524-5914-3fa0-add0-30ec5249ed78 | -11.87984 | -43.81622 | 2024-09-29 04:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 236957e6-a36c-384c-ada6-4f62c2f00474 | -11.87939 | -43.81997 | 2024-09-29 04:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b6fa0030-f58c-38a2-b54c-180341140014 | -11.87895 | -43.82374 | 2024-09-29 04:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0c05d97-a318-35df-995c-45ae0f7c3e28 | -11.87545 | -43.81582 | 2024-09-29 04:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0034c178-5fac-3d4d-b34c-15b28a43cfc1 | -11.87499 | -43.81955 | 2024-09-29 04:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14a1173f-74d8-3b8c-9e3b-eb307dbcca12 | -12.58396 | -43.83466 | 2024-09-29 04:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 020a4698-faf1-3549-bb32-e24ec56b43b6 | -12.5835 | -43.83847 | 2024-09-29 04:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ed3f027-3364-3350-a674-ac72e8e143fe | -12.58304 | -43.84227 | 2024-09-29 04:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1f1373f-d21a-3628-ae17-9a433f08c362 | -6.3968 | -44.78869 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9f7784dc-1b90-3975-a263-79da08191c1d | -6.3933 | -44.78591 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 42a74fe8-45cc-3720-b1f4-e98109b66e64 | -6.39271 | -44.78251 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c63e2c3f-2885-3756-b477-5cbe69528ddb | -6.39253 | -44.79126 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fb23be93-94fa-3e1d-8ca5-6ebaacbd62ff | -6.39196 | -44.78795 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1ebf50a2-ab4f-385f-9b7e-8a7ff3a0aa3f | -6.07746 | -44.70717 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 93babd0c-7bdb-302b-a87b-04035edf145b | -6.07263 | -44.70635 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7322282e-ca64-354e-acc7-185b13380357 | -6.07188 | -44.71157 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 963dc0e5-1787-3fd6-96e1-06fefb4ee5c4 | -5.89552 | -44.95008 | 2024-09-29 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 434752f7-2832-361e-af18-bffe8ae46612 | -5.8948 | -44.95509 | 2024-09-29 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8398c648-0e6d-368f-a72e-39d607cbfe48 | -6.5114 | -43.78315 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfaccdfe-6267-38d5-894b-960f87895314 | -6.50616 | -43.78272 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33e56989-4a94-345d-8810-c454ebc3c847 | -6.50571 | -43.78594 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 599ddc68-3b70-3fc3-bd25-deb57d8aa33c | -6.344 | -43.79949 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad85057c-93be-35a5-a867-a0a37090bb31 | -6.3436 | -43.80237 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bd222a8-b26a-32a3-9338-e04db875aacc | -6.33844 | -43.80152 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e9db206-48e6-39cd-9c59-f6440fce369a | -6.26233 | -43.76731 | 2024-09-29 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README41.md)
