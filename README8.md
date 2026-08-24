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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6eebcf0d-38d6-371a-aeba-c5b64d6e2cbb | -7.3791 | -45.8119 | 2026-08-24 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8b4fec8f-a6ac-3f21-9853-b56b0971d20c | -7.7706 | -61.1061 | 2026-08-24 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 62ae362a-363b-3068-b8dd-a9411dfe5479 | -7.36 | -45.8361 | 2026-08-24 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 22c3d33b-9eec-33a4-988a-e6c28be6d03c | -15.266 | -52.8111 | 2026-08-24 02:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 59bd2c6b-d960-334f-8b83-aae0bfe5b392 | -14.9392 | -52.664 | 2026-08-24 02:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f5862f65-c1df-304c-bcea-117ff454c2d7 | -9.0492 | -50.7801 | 2026-08-24 02:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 10c4c33c-7787-39bf-a21f-99e6f6c72e2c | -17.4236 | -48.8462 | 2026-08-24 02:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 4d701ed3-da3b-3174-94db-c0bb7d005d46 | -9.0061 | -65.3813 | 2026-08-24 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| d93b663c-5941-3d37-8f67-a17d75d36471 | -17.4435 | -48.8425 | 2026-08-24 02:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 1653925e-2b75-3263-9733-f0c8b3af6a90 | -12.0938 | -50.6166 | 2026-08-24 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.0 |
| ebf1123a-514c-34b1-b830-5c4c22bc198b | -12.1417 | -43.3945 | 2026-08-24 02:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| a4eb3001-8ef5-3bbc-8913-5dc8a7cde405 | -17.444 | -48.8199 | 2026-08-24 02:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 170.5 |
| aed10646-3111-3bba-b0c9-62359af60fe0 | -8.5892 | -49.9926 | 2026-08-24 02:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ce511a58-6a9d-382e-893c-e041ee3aad24 | -7.3603 | -45.8136 | 2026-08-24 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 45427e63-40b7-330b-befa-1bc1dfb6da01 | -12.0941 | -50.5951 | 2026-08-24 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 53d54dc4-e1fc-3e1e-b841-ed28a75da6a9 | -17.444 | -48.8199 | 2026-08-24 02:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 44520818-607d-3c51-8415-3b0e4bb6af88 | -17.4236 | -48.8462 | 2026-08-24 02:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 8caf0626-9576-33e8-8fd2-c16de7c47286 | -7.6849 | -63.3443 | 2026-08-24 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f9562e77-8bb2-3c4d-aa7f-42101f236018 | -17.4435 | -48.8425 | 2026-08-24 02:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 5408fb79-029a-37d6-8c49-09efb39ee295 | -22.9664 | -51.7723 | 2026-08-24 02:40:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| d800bb23-801e-3884-aa72-d883286b487c | -17.4241 | -48.8236 | 2026-08-24 02:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 241.2 |
| 5e8c422a-d75b-31e5-b40a-ae36c8fbf43e | -7.685 | -63.3255 | 2026-08-24 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 3f960034-3faf-36f5-acbf-2485d27133f0 | -22.9454 | -51.7768 | 2026-08-24 02:40:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 172.6 |
| 4e294f66-27ce-3c4e-a779-6eedd28142be | -7.3603 | -45.8136 | 2026-08-24 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 8a9c76b4-30de-33a7-bc52-376be0e98c18 | -22.9448 | -51.7995 | 2026-08-24 02:40:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 51.6 |
| a97b413a-984c-3e87-a9cf-2785fc670ff8 | -7.2443 | -49.8654 | 2026-08-24 02:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 31a96089-7278-3f67-8ddf-2061bf61cb62 | -9.0061 | -65.3813 | 2026-08-24 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c45126b5-3a61-3c64-816d-e2c85d15211e | -22.946 | -51.7541 | 2026-08-24 02:40:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 51.4 |
| 38be4a59-00d7-3642-b34b-29d377123481 | -15.3441 | -52.7793 | 2026-08-24 02:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 36514135-d771-349b-b723-33a0a10e670b | -7.7706 | -61.1061 | 2026-08-24 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| cea7bd66-e859-38c2-8990-85bafe6bd480 | -7.3791 | -45.8119 | 2026-08-24 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c778b986-76e1-3f3f-a03b-e809040fa713 | -15.3636 | -52.7767 | 2026-08-24 02:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| b5844354-d980-3a2e-b433-525cf6cc5843 | -17.4241 | -48.8236 | 2026-08-24 02:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 553.2 |
| 33a71974-d5af-37ca-9d98-9898ccc6f4a3 | -9.0494 | -50.7589 | 2026-08-24 02:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 9d4b1e00-bc3f-3c82-86d3-d057b1b979a7 | -6.6048 | -58.3838 | 2026-08-24 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 41b5e2ef-f730-3301-8fc5-763270352246 | -12.0941 | -50.5951 | 2026-08-24 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| d856c616-f543-3d67-bd07-f4413d2a01f3 | -12.0938 | -50.6166 | 2026-08-24 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 269933f0-0695-3bd3-a0d5-47b22ce1949e | -17.444 | -48.8199 | 2026-08-24 02:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 264.5 |
| 35c5bf06-4127-3d3e-9a3c-0294c75e4b9e | -7.2624 | -49.9278 | 2026-08-24 02:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 87b5c05f-0514-395b-b804-fbfffffdb145 | -7.2443 | -49.8654 | 2026-08-24 02:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e28768ef-c1c7-36c7-ac23-f230f0725d05 | -7.3603 | -45.8136 | 2026-08-24 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 02627da0-c49e-3722-a95b-175c727e3bbb | -9.0492 | -50.7801 | 2026-08-24 02:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ea02f7dd-a623-35d4-95f7-518133f78419 | -22.9664 | -51.7723 | 2026-08-24 02:50:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 137.5 |
| 0dfdd8f6-7be7-3b90-91c0-dcbb6d807827 | -22.9454 | -51.7768 | 2026-08-24 02:50:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 134.6 |
| ceaf3fb5-b47a-3c68-a7fd-b31ea55533db | -15.3441 | -52.7793 | 2026-08-24 02:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| ed26afb3-c485-3e30-88bc-9c9ff60beb03 | -17.4236 | -48.8462 | 2026-08-24 02:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 481.4 |
| b8bf9366-c772-34c2-bbe5-9101b1c9d2da | -17.4435 | -48.8425 | 2026-08-24 02:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 301.8 |
| 54c2bb8f-aea1-361c-9f1d-a26636d26dd8 | -22.9664 | -51.7723 | 2026-08-24 03:00:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 46.9 |
| 7ec31534-4552-3253-8c81-f02d5a98f690 | -7.6665 | -63.3261 | 2026-08-24 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c56654b3-8fd5-3fbe-975d-0bfbf23eaa9a | -12.1132 | -50.5929 | 2026-08-24 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 790bd8f9-5d9b-3b15-9c9e-9eaf4bb2b040 | -17.4247 | -48.801 | 2026-08-24 03:00:00 | GOES-19 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| d4abab22-3084-30fb-827e-61e35c83f85a | -7.7034 | -63.3249 | 2026-08-24 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 24fbc92c-ddac-30f9-80cf-fa2767d42654 | -7.2626 | -49.9066 | 2026-08-24 03:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| bb37c21b-b0d6-376c-b596-7c140052797f | -7.2811 | -49.9265 | 2026-08-24 03:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 5eb68a3e-b656-3997-8e6f-006eef2d2052 | -17.4241 | -48.8236 | 2026-08-24 03:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 534.4 |
| e7a416e7-272f-3b5f-82d3-df7fb3a78473 | -7.685 | -63.3255 | 2026-08-24 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 5ffa9b09-6c33-3225-8507-10547908ff78 | -6.8491 | -52.505 | 2026-08-24 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| d4d0f8e8-e7cf-39a7-b054-37051b420bf8 | -9.0061 | -65.3813 | 2026-08-24 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4ad7f632-a36f-3a69-a380-c5cce3e8ad63 | -7.6849 | -63.3443 | 2026-08-24 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 621b6193-fd68-3441-92dc-f017bbecf83e | -12.0938 | -50.6166 | 2026-08-24 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 723b90d9-468e-3fda-95ba-5520aac98fbf | -7.2813 | -49.9052 | 2026-08-24 03:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 595d700c-4e0b-32fe-8e09-ace84eb1ed23 | -7.3603 | -45.8136 | 2026-08-24 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 133dacb2-5090-31c5-acdf-32302adf8b2e | -12.1128 | -50.6143 | 2026-08-24 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 57992e9f-e304-39ae-934d-dfdf7ff12954 | -6.3505 | -54.7665 | 2026-08-24 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 5e05291c-e563-355e-a56a-8ea1257d3d1a | -17.4236 | -48.8462 | 2026-08-24 03:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 522.3 |
| ca89a691-ce90-3a68-8687-ebf92b725143 | -17.444 | -48.8199 | 2026-08-24 03:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 257.6 |
| 802ca311-234f-348b-9f46-a7aea828d478 | -8.9876 | -65.3819 | 2026-08-24 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d8af0ff0-fa19-3511-bcf4-8683ff6dce82 | -7.2443 | -49.8654 | 2026-08-24 03:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 3309caff-f06f-3751-8eba-88c89fd00456 | -7.2624 | -49.9278 | 2026-08-24 03:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| ada3bf7b-6989-327e-9076-f303cd25da96 | -12.0941 | -50.5951 | 2026-08-24 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 208bc368-5aa9-3b6b-8860-5a58a055d94e | -22.9454 | -51.7768 | 2026-08-24 03:00:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| 886c7005-3c2e-3384-a623-3a62968bcc89 | -17.4435 | -48.8425 | 2026-08-24 03:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 275.7 |
| 2dcc5da3-1c17-3073-90dd-def590b39dc1 | -11.09999 | -38.59782 | 2026-08-24 03:06:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4b8ce003-903a-3914-9568-5dced7e07890 | -11.09879 | -38.60365 | 2026-08-24 03:06:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7a5fcaed-907b-3981-8fe7-90cb748306ba | -19.00575 | -42.13222 | 2026-08-24 03:08:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9a0dd080-989e-30dd-9295-0bf08eb97a1f | -19.00754 | -42.12495 | 2026-08-24 03:08:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ac054956-bced-3e6f-afef-a65607ed00cb | -19.01461 | -42.12685 | 2026-08-24 03:08:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 63dffb2e-ffa5-31ba-a07f-b5c1ed1825b3 | -19.01285 | -42.13401 | 2026-08-24 03:08:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f66d816-1524-30da-a3bc-fb7334a24ad3 | -14.3123 | -53.2081 | 2026-08-24 03:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 2bd5285e-e515-356b-bca4-af315808bd59 | -12.1132 | -50.5929 | 2026-08-24 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d95abd78-5537-33e3-9600-2c4f0425dcf8 | -12.0938 | -50.6166 | 2026-08-24 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 237.3 |
| 49235176-0063-3645-b1d9-dda64d242d3e | -12.1128 | -50.6143 | 2026-08-24 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 7aacb60a-0c20-3f97-b065-69b114494dcf | -7.6665 | -63.3261 | 2026-08-24 03:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1b77692e-7bd7-3d13-9a11-ca9f552cca80 | -9.0061 | -65.3813 | 2026-08-24 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 05608938-1f6b-3c41-b1af-8bb9de834284 | -17.4435 | -48.8425 | 2026-08-24 03:10:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 9e700283-9cba-36f3-937a-36c2544a629e | -17.4236 | -48.8462 | 2026-08-24 03:10:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 218.0 |
| 7f198895-780b-3aa9-b1d6-ce330cf34afb | -17.444 | -48.8199 | 2026-08-24 03:10:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 174.7 |
| d83d3637-a768-380c-9efb-75a8b6f89b63 | -22.9664 | -51.7723 | 2026-08-24 03:10:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 50.2 |
| cf8d9dfc-4d2c-3fab-a54a-0690405b87f7 | -17.4241 | -48.8236 | 2026-08-24 03:10:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 238.1 |
| 4e750f68-c64b-3824-b16f-e1b86bcc4391 | -7.3603 | -45.8136 | 2026-08-24 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 43742e99-9175-3637-b4a7-3e1cf9fccceb | -12.0941 | -50.5951 | 2026-08-24 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| b4735935-33db-3029-9aab-52dc74b63a71 | -17.44 | -48.81 | 2026-08-24 03:15:00 | MSG-03 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 16e56454-0c6c-32e6-9187-54b350835a8a | -17.44 | -48.86 | 2026-08-24 03:15:00 | MSG-03 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0060569f-dff9-3f09-a690-34526f33ba98 | -17.41 | -48.85 | 2026-08-24 03:15:00 | MSG-03 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c955fc1-6b81-31ab-9a1f-6123983bcabf | -17.444 | -48.8199 | 2026-08-24 03:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| cecadece-e5ea-353c-a0f8-3b7a60324ee7 | -17.4241 | -48.8236 | 2026-08-24 03:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 115.8 |
| f44b2272-cd65-3106-96f0-9ffe15e52976 | -9.0061 | -65.3813 | 2026-08-24 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4a287508-da76-3cb3-b80f-b187f3f5c88d | -7.9047 | -63.6753 | 2026-08-24 03:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7c10559d-117c-396b-a62a-fa563e52ac1e | -7.9046 | -63.6941 | 2026-08-24 03:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 7d2ec90a-22db-3fe7-8aa8-33d2656edfd5 | -12.0938 | -50.6166 | 2026-08-24 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 294.2 |


[Clique aqui para ver as próximas entradas](README9.md)
