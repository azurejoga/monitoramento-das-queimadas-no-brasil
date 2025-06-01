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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ccf707f-a258-34ac-b160-e145fc28db21 | -20.15249 | -49.6144 | 2025-06-01 04:59:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 186b4015-9aa7-33dc-b232-8509a4a53982 | -17.75669 | -52.4376 | 2025-06-01 04:59:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f29cad39-2d8d-3a8e-9b75-302a0412acaa | -11.79812 | -41.19465 | 2025-06-01 05:01:00 | AQUA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 7168a8a7-0b0e-30e3-bc2d-58bbcc7974b0 | -11.79692 | -41.18767 | 2025-06-01 05:01:00 | AQUA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 3caa5867-facc-3921-a937-5be9d7e18ff7 | -25.19791 | -49.32404 | 2025-06-01 05:01:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c9220cf-6120-354b-968e-523f23179258 | -25.19243 | -49.32691 | 2025-06-01 05:01:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 00893086-045a-3249-89da-ead4d5631001 | -24.24117 | -50.73847 | 2025-06-01 05:01:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dbd7717d-2144-3a80-ab55-442c3ada0358 | -12.72342 | -54.97784 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5850239f-1929-3c06-bf70-0550bdbf582d | -10.3007 | -57.14075 | 2025-06-01 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8090ca7b-fbb6-3c1f-9dfb-60b03a74698d | -11.42963 | -55.00604 | 2025-06-01 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ca829bb-c52b-3a29-a4db-c0c742694126 | -12.72315 | -54.98012 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0c9b1fa9-4e1a-36a0-bee4-b8f52d21e0c5 | -11.07662 | -54.77879 | 2025-06-01 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aea74b28-e063-344b-8fc6-dbf2d6662462 | -10.82749 | -56.9535 | 2025-06-01 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5d8ff0b-3ad7-3f89-9619-9f764a3a7138 | -11.71 | -56.45573 | 2025-06-01 05:50:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0713bd0-e821-3ff0-9641-6e257ff49a11 | -9.37278 | -64.45441 | 2025-06-01 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cb17c82-1152-36b5-b480-302f18bfa010 | -10.83024 | -56.9529 | 2025-06-01 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3370d340-58c4-3192-b7e4-bec5a65aa72d | -11.07733 | -54.77223 | 2025-06-01 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd2e2f7a-aebc-349b-ad98-d1cb28570ce3 | -12.71697 | -54.9726 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4781d40f-0e5b-31bd-9fb3-99ca0c67ff03 | -11.4364 | -55.00713 | 2025-06-01 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfddab41-8f04-3a0d-96a1-1d33f67a8525 | -11.07609 | -54.77651 | 2025-06-01 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fe11093-49f1-35bb-9819-f4ee71c4336e | -11.44517 | -55.00644 | 2025-06-01 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e6a56e9-290a-3b12-b6a5-4e1c8e0ace9b | -10.82971 | -56.95742 | 2025-06-01 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35a2102e-c079-3f9a-8de3-cfd63d3b3d48 | -11.08976 | -54.77862 | 2025-06-01 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa4e395c-403c-36c0-b582-a180c253c1ac | -10.82919 | -56.96188 | 2025-06-01 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a33cabc5-3078-3d29-b437-24bd05fe58c9 | -12.12662 | -54.60227 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dfc8649c-403b-387d-a500-5e1ad0191661 | -12.08681 | -54.57618 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34218444-4c4c-3bcf-8619-379690ae13b0 | -10.82265 | -56.94347 | 2025-06-01 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3049f0ae-de8f-329a-8fe2-5f5509223f17 | -9.93261 | -59.90105 | 2025-06-01 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 017307af-75aa-38be-8704-8bf823c10bc1 | -11.44318 | -55.00814 | 2025-06-01 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 297a8c53-6f5a-3a12-b181-3022b53e2a0b | -9.93192 | -59.90641 | 2025-06-01 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7a1a0902-777b-35cc-83b3-7a79fe47cdb3 | -14.02982 | -55.13923 | 2025-06-01 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 367cde7b-765d-31fa-a64f-580d2f957732 | -14.03051 | -55.1324 | 2025-06-01 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 961574db-0b0b-38e1-be51-bf872cce62c8 | -12.12596 | -54.59269 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02f4d913-46b3-386e-98c5-42d221565bb6 | -12.53036 | -57.19895 | 2025-06-01 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7986bf9a-dcd5-3258-9725-3ced183875a2 | -11.08345 | -54.77991 | 2025-06-01 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1cc26634-a9cd-3bb5-a9eb-c12a630fdccf | -10.82533 | -56.94284 | 2025-06-01 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d86f14cd-207c-3df2-a863-6c1204c43075 | -12.12526 | -54.59951 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 90f19498-9232-31cb-b56e-528c778d8be5 | -12.0861 | -54.5828 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d3c3a64-d720-3c53-8998-7ff709a8ab42 | -11.08216 | -54.78412 | 2025-06-01 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 333bfd2a-54c5-3d9d-baae-5bd4fda43121 | -12.53141 | -57.18963 | 2025-06-01 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1d70aa0-7a1a-3d07-bfa7-8e40a7a30b6c | -12.71652 | -54.97699 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c591af53-57d9-3a08-a9a3-d5197ffbebdf | -11.08292 | -54.77758 | 2025-06-01 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fa2c836-9b8f-3a68-b98f-fb86de7b5fd8 | -9.92843 | -59.90555 | 2025-06-01 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 1c5682dc-450d-3da2-b61d-f4ebc0d8bd45 | -10.83291 | -56.95885 | 2025-06-01 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f619147-8cb2-347e-af8c-4c9bbf296cbd | -12.53089 | -57.19427 | 2025-06-01 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 552e20f7-24ed-3ff5-8633-527ab9c07a25 | -12.53246 | -57.18042 | 2025-06-01 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d83e950c-5c75-3fe9-ac47-7deabd90d37a | -11.45195 | -55.00744 | 2025-06-01 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8efc22e7-5354-3154-886f-0d8427b84c64 | -11.08417 | -54.77333 | 2025-06-01 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e01772b1-c480-3a7e-8fe4-75a047459942 | -9.92916 | -59.90022 | 2025-06-01 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6a9a61f5-51cc-377d-a0b8-a528556b01b5 | -10.29483 | -57.13993 | 2025-06-01 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0db8887-8dcb-3d86-a9f0-d8bcab38af30 | -11.07685 | -54.76997 | 2025-06-01 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e317d2c0-1b2c-3635-9aea-ea41c8296fe4 | -11.47004 | -61.94354 | 2025-06-01 05:50:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85ed7934-32d8-3a54-ab8e-a028a7bd1984 | -12.72388 | -54.97345 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f80e8da8-7954-3a4a-81ec-b935428a948a | -10.82481 | -56.94732 | 2025-06-01 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44d63430-045d-38c1-9db5-20be88ecd6ec | -12.7241 | -54.97122 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eb6acceb-861b-3162-8bd5-0bb46a497fc5 | -12.12736 | -54.59551 | 2025-06-01 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2e70f23b-9a86-3fad-b021-2d880fbf67fa | -11.08368 | -54.77103 | 2025-06-01 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fed7069-c76f-32d6-ae60-028cc5a478b3 | -9.92717 | -59.90334 | 2025-06-01 06:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c8ad9de9-3c48-380f-9d3d-18733a6dbcb2 | -9.93447 | -59.90428 | 2025-06-01 06:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 299dff8c-4f9c-3dcc-9ff1-493c70148ca3 | -9.92711 | -59.89405 | 2025-06-01 06:40:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 572063a7-b8a2-33a9-abbb-4ad3e884adfc | -12.71791 | -54.96663 | 2025-06-01 06:40:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 68176d54-6773-38b8-969c-692f0e73324e | -12.71625 | -54.97347 | 2025-06-01 06:40:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 726cf84d-84f9-3af1-87e0-a50bf4d79cd4 | -9.92576 | -59.90316 | 2025-06-01 06:40:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| ae4114d8-cf0b-3d85-a44e-2ba3bf1fc976 | -2.87099 | -42.09384 | 2025-06-01 12:02:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 793ea1c6-c755-3781-844e-67f01172c215 | -4.41771 | -37.80328 | 2025-06-01 12:02:00 | TERRA_M-T | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 0efb0f4c-8ddf-3823-a62e-a9deb963ccb1 | -5.43385 | -38.57124 | 2025-06-01 12:02:00 | TERRA_M-T | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9cbac5a0-a3ec-3194-98b6-a1d2ddf94186 | -7.2833 | -44.39485 | 2025-06-01 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d0f7d6b2-147a-3e7c-8f19-6ec22cdf883c | -9.19584 | -38.80039 | 2025-06-01 12:04:00 | TERRA_M-T | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 53608a05-2c28-3d9b-957b-da7438cbfbeb | -7.25009 | -43.23982 | 2025-06-01 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b7e46a60-2c6b-3635-b71d-0e9d457a726a | -7.28285 | -44.40015 | 2025-06-01 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 7e40feaa-5de5-374b-bf80-9be910877354 | -13.71321 | -45.25528 | 2025-06-01 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 81045632-a548-376f-968c-74f872eeb4aa | -7.29335 | -44.39631 | 2025-06-01 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 1455c143-a25c-324e-97b4-892427b7a3ae | -8.68111 | -46.63723 | 2025-06-01 12:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5cbfa775-a4b7-35d0-bc36-581f704a1098 | -14.66284 | -45.40303 | 2025-06-01 12:04:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| cfe4bd8f-8f29-3607-8147-1804503015df | -7.29157 | -44.40792 | 2025-06-01 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 383.6 |
| 5cd53b64-6618-3eb1-94e5-ab5ed9eb39b1 | -13.73167 | -42.75618 | 2025-06-01 12:04:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| ece0dc4e-497f-35c1-8ced-47085d78a223 | -13.73036 | -42.76521 | 2025-06-01 12:04:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f0257b3f-0506-3549-9a73-0a0c3bf1fbea | -13.71146 | -45.26635 | 2025-06-01 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| d5ae5b8b-5f31-3630-b130-b88e72c1c1c9 | -8.14163 | -41.1804 | 2025-06-01 12:04:00 | TERRA_M-T | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 92ad34b2-03b4-3f47-8e36-6b5dc7808e0b | -7.24861 | -43.24989 | 2025-06-01 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d7fb307e-3c36-3465-b2f3-444d096a635d | -7.28457 | -44.38853 | 2025-06-01 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 477e0ad1-ea42-38a2-a350-cb0cb4d67c47 | -13.6646 | -45.42299 | 2025-06-01 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 99afc8dc-7fe5-309a-8d48-bcdefff54aa7 | -13.91606 | -46.86227 | 2025-06-01 12:04:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8cb1558a-c505-3363-86d8-066bb6832f33 | -18.87812 | -46.46703 | 2025-06-01 12:06:00 | TERRA_M-T | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8ef213ec-ccde-396e-a2f6-f6e07c608eb2 | -18.87995 | -46.45574 | 2025-06-01 12:06:00 | TERRA_M-T | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d8061f8e-2599-3e3a-86bd-449fd0fd22cd | -7.2389 | -43.2309 | 2025-06-01 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.8 |
| f27faa26-27b9-3605-bcdf-85c2bb648273 | -7.2819 | -44.4106 | 2025-06-01 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| feca1cf1-a6b2-3362-9b52-96095eeb3a6f | -7.2198 | -43.2561 | 2025-06-01 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 600e3339-b106-3457-8ac4-76064315a482 | -7.2386 | -43.2543 | 2025-06-01 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 186.7 |
| b7eb081b-1a26-3bdc-816a-4d09e22687cd | -7.2819 | -44.4106 | 2025-06-01 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b274b587-3c40-3e1c-9dee-db48cfbdc335 | -7.2389 | -43.2309 | 2025-06-01 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 2dea6e97-a1e9-37ec-8c67-a0c69d93037c | -7.2386 | -43.2543 | 2025-06-01 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| cb88856d-0ea9-39c9-9f09-ac99bfefbc34 | -7.2819 | -44.4106 | 2025-06-01 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c02156e8-f838-3d4c-af13-0ec5d37ba876 | -7.2389 | -43.2309 | 2025-06-01 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 0568f548-dbb7-3a2d-89b0-e2a8d986f636 | -7.2198 | -43.2561 | 2025-06-01 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 7ba91f95-b94f-3aca-90f4-ffd1f5b34431 | -7.2386 | -43.2543 | 2025-06-01 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 7c0ff2ec-7df2-3939-a8d3-440eb20159ca | -10.6163 | -46.5 | 2025-06-01 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c4741236-1648-3cf6-90b7-4c1cad002c4c | -7.2386 | -43.2543 | 2025-06-01 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 692c4ed6-a7d1-3887-aab4-f281ff9c594d | -7.2389 | -43.2309 | 2025-06-01 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 8863db2e-ff49-398b-bdcb-6e8309cfa334 | -7.2389 | -43.2309 | 2025-06-01 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |


[Clique aqui para ver as próximas entradas](README15.md)
