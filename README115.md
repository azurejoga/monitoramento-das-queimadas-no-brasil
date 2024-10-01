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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b3c2958-655d-314b-9efd-deeb246c80d6 | -12.70756 | -54.10046 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99bca978-ee6a-36d4-bd98-67d47fe211c1 | -12.70598 | -54.09696 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78dca215-04ea-3f13-a3e7-6de3b8e0bf98 | -12.70158 | -54.09101 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7493fc32-ed80-3450-817c-056f221991e3 | -12.69226 | -54.09059 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54254be6-2a4b-3305-8966-9cb12e18c57d | -12.68867 | -54.09005 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c91b04b1-aad8-31f5-9919-71101b8440e4 | -12.68712 | -54.02537 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26081b57-7090-30b9-aa0f-17d10e00b3ef | -12.68352 | -54.02482 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 616ee97c-5677-357b-8e7b-0430647e0e2d | -12.68272 | -54.08059 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ebede24e-e47e-3df6-996f-c74d40fa0fbb | -12.68211 | -54.08475 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adee6f73-93f2-314e-bfbd-30209206e111 | -12.68167 | -54.0375 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e564a36-fe99-3240-84fd-3e82247a0efa | -12.67975 | -54.07586 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc573866-4ccf-398d-b05a-a8919e8a5281 | -12.67325 | -54.04485 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de81ba9f-5a90-3616-9843-6104e7cec29e | -12.67257 | -54.07478 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be6ba721-3c5f-3d7d-9325-a776505a05bb | -12.67203 | -54.05326 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 574ead41-563a-3069-a353-2f33e031f080 | -12.66898 | -54.07424 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a583428f-1668-3612-8aca-ba5a91278c13 | -12.66722 | -54.06112 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcce7676-7741-3ff5-b7ac-0ac35ac98d8b | -12.666 | -54.0695 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 687b0490-1e6e-3b9c-bb28-4b398e2dd57e | -9.65496 | -53.58782 | 2024-10-01 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32568bf1-4980-36d8-ac72-7d27dd4e4b1c | -9.65141 | -53.58728 | 2024-10-01 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdc00e43-3bbc-3e53-af30-3707d44bc6cf | -9.63441 | -53.58216 | 2024-10-01 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 443c72bf-de13-3f6d-946b-961699c037b3 | -9.63025 | -53.58566 | 2024-10-01 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a5b698-37c3-3154-9218-204a62b4651f | -10.23804 | -54.24427 | 2024-10-01 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07ebaace-dfbd-35fb-92e3-d33814d6f552 | -10.23457 | -54.24372 | 2024-10-01 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a52f880e-ea0c-3b41-8f74-9fb1bfeb0b6e | -11.39023 | -55.186 | 2024-10-01 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29fa2bcc-53f0-3554-af7b-718f2b9f3360 | -11.38328 | -55.11662 | 2024-10-01 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65c80eb7-8b39-3f43-9827-2e9203c16602 | -11.37932 | -55.11983 | 2024-10-01 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82dc1bda-d7de-3bbe-8f4b-ff11cfb13f2e | -11.37592 | -55.11931 | 2024-10-01 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98b2394e-aae2-3170-8a68-f49a9aae51b7 | -11.37537 | -55.12302 | 2024-10-01 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6ba5305-d902-32e5-91a5-2099fab2add6 | -12.31221 | -54.1137 | 2024-10-01 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7ea811a-b696-3bcb-bfac-9edb8c3f885d | -12.3116 | -54.11787 | 2024-10-01 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a3c810f-6bdc-31d2-85e7-162d49e58899 | -12.311 | -54.12204 | 2024-10-01 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66a1671d-5dab-32b5-ad8f-4eca94714336 | -12.30804 | -54.11734 | 2024-10-01 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e65b9bc9-5de9-3d3f-bc4a-345883642e4f | -12.30743 | -54.12149 | 2024-10-01 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13cb6249-7086-37c4-b523-ad9e257c8162 | -12.68684 | -54.66759 | 2024-10-01 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 735ce6b8-1d70-36c9-848a-3e166857d828 | -14.17478 | -54.6572 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d854021b-0015-387b-b76a-7e5b9b52a187 | -17.16808 | -56.19802 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b26a4a55-79ae-3bee-962f-41c88b093c41 | -17.16755 | -56.15416 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c0386517-f5e9-3cb2-b155-178550a54643 | -17.16697 | -56.15806 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ba5aa50f-cbdf-368f-8d90-999da1729d9c | -17.16582 | -56.16584 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3822cd56-aa16-3c4d-a972-0abc615b0437 | -17.1658 | -56.18971 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2d18a58f-098a-3ee0-b80e-f47e7c9bd00b | -17.16525 | -56.16974 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4a050be1-84d3-30b9-b7de-2670670740c2 | -17.16465 | -56.19748 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 088d9e66-fdd8-363e-b1f3-f6e331548cb4 | -17.16352 | -56.1814 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f13a9330-9128-379a-85a2-85392f554b52 | -17.16237 | -56.18917 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 35c5dfef-b113-359b-b5cc-fced23309d2b | -17.16182 | -56.16919 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| c76534d2-c878-3b3d-aab9-c717d8d2f975 | -17.16124 | -56.17309 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| c97d97e6-fbb9-3b07-b691-2efca23386ea | -17.16122 | -56.19693 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 40e749ce-77c3-3a4d-b21a-a00656af5ebf | -17.16067 | -56.17697 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 5003f3e4-4b68-3c89-9856-09d86bd26d55 | -17.15781 | -56.17255 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 6307e002-a382-3686-b86e-552b0d3ecefe | -17.15779 | -56.19639 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| f19dd35c-954c-3be0-91d6-f922e023730e | -17.15724 | -56.17643 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 2729c5c5-ca1e-3572-a934-3fd356e3f605 | -17.15609 | -56.1842 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| e5f1f9f8-00ce-3c2b-9234-604c4569233f | -17.15437 | -56.19585 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 24d042f5-ed9e-3a80-bcd0-76d6b653abec | -17.15323 | -56.17977 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fbd4e94c-cf9d-3413-8e21-2eb3eabf4f80 | -17.15209 | -56.18754 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b6538f73-4591-3e4b-93ec-8703749676ec | -17.15151 | -56.19142 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 660bb0eb-4cd3-3af1-ae33-d69fbce59a6f | -17.14808 | -56.19088 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 81773a76-469c-3f05-8049-1e0ec081dfb0 | -17.14751 | -56.19475 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a0bf21f1-d605-3c0d-9305-81f52eae2b97 | -17.14694 | -56.19863 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d537499d-300c-32a2-97fc-c2fd460690cc | -17.14637 | -56.17867 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f8db261b-92ea-32fa-b091-de5b258efe2d | -17.1418 | -56.18591 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2f4c8ea1-adc6-364a-93b0-1823cb24c277 | -17.1378 | -56.18924 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8fc195dc-3de8-3f7c-9842-5b659039cc7a | -17.13666 | -56.197 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 57bc9652-2b0a-3b57-84bd-96e92702eb1d | -17.13151 | -56.18427 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1781d9d9-c0cd-33a8-b094-0b1b77808b98 | -17.13094 | -56.18816 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 481fd9e3-ab8d-342b-9b70-ded78601ba99 | -17.12465 | -56.18318 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3ff7461e-f30b-3ece-8003-8322db55f852 | -17.12179 | -56.17875 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 02c74310-5dda-3026-9982-2e9ed72d8290 | -20.02929 | -55.98967 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bfaf1e10-4c82-3d07-a4f5-71472fb160d0 | -20.02632 | -55.98486 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 9ba3350d-9c03-3fea-bbd2-aeb27b2264b8 | -20.02573 | -55.98911 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 027365dc-31ca-393e-91f6-e28034f03951 | -20.02515 | -55.99335 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4ba09caf-98f0-3f98-bce2-0a0b8e520540 | -20.02323 | -55.98545 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 98c23933-bb86-37bb-880d-0072da87a455 | -20.02277 | -55.98429 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d526addd-5cd9-3888-bec6-fd31723e8727 | -20.02263 | -55.98969 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e5605581-bfe8-3c2b-9161-db680c6f8902 | -20.02219 | -55.98854 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c865b38c-6487-37bc-b37a-432ccf198e5a | -20.02203 | -55.99393 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 03c1f73b-66c5-37ab-a035-eff4923f24e7 | -20.0216 | -55.99279 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e6f7d2c2-c5f4-3899-b96f-fef6856a98ff | -20.02029 | -55.98064 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 582e3b5e-1658-3111-8174-692c9bc7c91f | -20.0198 | -55.97947 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| eb9063f6-b3e8-37b8-bc3d-d3841a3e904c | -20.01968 | -55.98489 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e2116b17-8a20-384c-a49a-c2817cf0ef2e | -20.01922 | -55.98373 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f3265569-b330-33b7-9a82-3eab0a95b271 | -20.01908 | -55.98913 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6a5ee7da-99ff-3660-8d9d-4cfbbfaeb153 | -20.01863 | -55.98798 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e8899651-31bc-39c0-bb30-5457ca76228c | -20.01674 | -55.98008 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 95efccc7-d7ab-3374-aaf6-de5e13f132b0 | -20.01613 | -55.98433 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 90e820af-2d7b-3fe2-81e5-e7bd70dee1ff | -20.01553 | -55.98857 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1945805c-9f58-3fca-8f69-3cf983008204 | -20.01259 | -55.98376 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 48645a85-2df3-3f35-98b3-19a3acdc99df | -20.01198 | -55.988 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7ac4bdbe-1351-35f0-8c4e-e771f5135e6d | -19.66877 | -56.47345 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3b002995-dc00-39bb-8b4e-279b844e9c92 | -19.65433 | -56.47525 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 8b19107f-6338-3a21-8c5c-4db23790c4a5 | -19.65376 | -56.47928 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 963cf20d-5599-3af0-85bd-3947e743a065 | -19.65318 | -56.48331 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a9f4d122-6164-31fc-b116-a31dabeedb15 | -19.64917 | -56.51149 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f5108089-e071-3197-a38e-a1a4c5e46259 | -19.64116 | -56.56763 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e3cb0848-009c-3d52-b2d8-f9e32b7079d1 | -21.04091 | -57.51276 | 2024-10-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7a8566ef-9325-37a8-95ce-e0e90ef42218 | -21.03018 | -57.51493 | 2024-10-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0c58361c-efed-3e8b-87c4-ed57ef5c5184 | -21.02679 | -57.51437 | 2024-10-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e41497cc-ea1c-33a4-8691-310cfd1f26d9 | -21.00253 | -57.51423 | 2024-10-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3b39d86e-d716-3036-9726-886935e829c5 | -20.99914 | -57.51364 | 2024-10-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b450f253-274f-3ac7-99f4-4c944ddfbf37 | -20.99576 | -57.51305 | 2024-10-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |


[Clique aqui para ver as próximas entradas](README116.md)
