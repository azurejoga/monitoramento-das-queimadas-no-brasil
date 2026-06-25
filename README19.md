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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a051a476-d606-32b5-b847-4822eb5cf1a0 | -7.7498 | -44.6184 | 2026-06-25 06:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 453437c5-25e2-37e8-9d67-c0ead0556ebc | -7.7412 | -44.62025 | 2026-06-25 06:57:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 0d0e8ec8-5409-3588-b591-a4fe4c783707 | -6.98573 | -42.87262 | 2026-06-25 06:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 6c62842f-8ef7-32c8-93c2-4346edf5001d | -6.9888 | -42.87727 | 2026-06-25 06:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.2 |
| 5f4317a5-57a0-387a-8ec7-5c6bf77fc247 | -7.75647 | -44.62239 | 2026-06-25 06:57:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 2a419f3e-5da2-37df-8669-573c052b6aee | -8.68061 | -47.86284 | 2026-06-25 06:57:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0dba8edd-3162-32a4-9d00-a2d88839e07a | -10.396 | -56.75622 | 2026-06-25 06:59:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2508cedb-9c71-3118-ad2a-e88b26c67875 | -9.48316 | -57.30966 | 2026-06-25 06:59:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3904f822-00c7-30fa-89c4-ef71148eabce | -10.12764 | -52.10886 | 2026-06-25 06:59:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 17f93d5e-6397-3d2e-ad87-c675dc24436f | -10.39423 | -56.76719 | 2026-06-25 06:59:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 81da5576-23de-38d7-9956-bafcbac3e824 | -9.48118 | -57.32186 | 2026-06-25 06:59:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d3c26e34-a5d6-3dd6-929b-a843a39be72f | -12.13563 | -48.26587 | 2026-06-25 06:59:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a0916249-46d5-3b6b-b76a-9828811443be | -9.49334 | -57.31134 | 2026-06-25 06:59:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| b3443cb8-be3a-3061-8326-a92628145a0c | -7.7498 | -44.6184 | 2026-06-25 07:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 0826b092-53db-3f7e-bd94-633452773a68 | -7.7498 | -44.6184 | 2026-06-25 07:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 07733a5d-7ba6-3d63-baee-53763ae7cb47 | -7.7498 | -44.6184 | 2026-06-25 07:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 9e667a59-f3fb-3ab3-8a87-06336526c532 | -7.7498 | -44.6184 | 2026-06-25 07:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 89d8dc84-188b-350c-bc35-ae9d744b1be3 | -6.43694 | -37.12807 | 2026-06-25 11:08:00 | TERRA_M-M | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 216b673b-486a-353d-af2d-6129dae47a75 | -6.43563 | -37.13713 | 2026-06-25 11:08:00 | TERRA_M-M | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 765c0fb0-4a6e-3fc8-89dc-5200db909aad | -6.56373 | -38.27863 | 2026-06-25 11:08:00 | TERRA_M-M | VIEIRÓPOLIS | PARAÍBA | Brasil | 2517209 | 25 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 2ed6a29a-6782-35c5-94bf-6d23d31b754e | -10.21939 | -46.33274 | 2026-06-25 11:10:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| d39446d0-1129-326a-a9f2-e0910f446a62 | -11.87334 | -43.80362 | 2026-06-25 11:10:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 6956ca82-7a3d-3ea2-bac0-6f11a9b69828 | -11.87385 | -43.79756 | 2026-06-25 11:10:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 2c18102e-b66c-3a93-a760-5fd1ffc9c631 | -11.87677 | -43.7835 | 2026-06-25 11:10:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 44999377-fd46-35f8-b0d4-b659f127c191 | -13.45377 | -44.04078 | 2026-06-25 11:13:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 39.3 |
| f0bde631-46ce-38b9-a6b2-4e25e3eb6a0e | -15.04642 | -42.42884 | 2026-06-25 11:13:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| c4c80b79-7325-35ac-84dd-a7482d785f0c | -14.14501 | -41.94789 | 2026-06-25 11:13:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 894c1daa-94b7-3fe6-9bda-bbd0b06c61f7 | -15.77956 | -39.21978 | 2026-06-25 11:13:00 | TERRA_M-M | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7101ebff-1ae9-3f58-9a68-b2aa0299390c | -15.0514 | -42.4213 | 2026-06-25 11:13:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 4023e6df-ec32-3d71-ab6d-2c08d26e0fab | -18.78791 | -40.22406 | 2026-06-25 11:13:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 49f0f0e5-658b-32be-a3c1-e6ed9c3d0375 | -18.78938 | -40.2143 | 2026-06-25 11:13:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 4a653f79-3d36-350d-b1f1-9b5e5670fafb | -12.7562 | -44.4724 | 2026-06-25 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| e4e4c805-6b71-3340-a994-61bd714b1d20 | -6.9791 | -42.9034 | 2026-06-25 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| f3907eab-78ad-3a56-8544-80ed7542f56a | -7.7498 | -44.6184 | 2026-06-25 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e8d17dff-71b8-3e1e-a2a3-47c1cb80ef7d | -9.79273 | -56.94053 | 2026-06-25 12:49:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| bc5ec06c-d8a4-3f98-9fc6-bec81153ba46 | -11.8973 | -51.73064 | 2026-06-25 12:49:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| f65c0f6a-2971-3a70-8d68-27ae7d986cdc | -10.39867 | -56.78132 | 2026-06-25 12:49:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 0b4ca84f-b63d-3e4d-a449-37e2ab3e264f | -11.88999 | -51.76255 | 2026-06-25 12:49:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| fab84699-ab73-3c3e-a5b3-ed8b7c5b233d | -11.27768 | -53.93967 | 2026-06-25 12:49:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0e636cb6-8457-3016-bf48-9de3123523f9 | -9.41797 | -63.1963 | 2026-06-25 12:49:00 | TERRA_M-T | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc0669a5-e575-3472-aff9-b35f38a17ca5 | -10.4005 | -56.76656 | 2026-06-25 12:49:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 5147a9b5-b9f4-3c62-a3af-aaef4fa6e925 | -10.16602 | -56.62609 | 2026-06-25 12:49:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| a6715292-85c6-33ac-b2bf-57ca23381644 | -10.39893 | -56.77495 | 2026-06-25 12:49:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| bfe9fdeb-8070-3b77-b7bc-3388c8f16d25 | -9.49468 | -57.31969 | 2026-06-25 12:49:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 021f5852-9ab6-39e7-b940-d1e71737be33 | -10.38419 | -56.71296 | 2026-06-25 12:49:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f56d391e-34b8-39a6-839e-e2a28a71459b | -11.8943 | -51.72335 | 2026-06-25 12:49:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 2161c6eb-7c9b-3851-9ecf-f136cac98cc1 | -10.38931 | -56.76491 | 2026-06-25 12:49:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 9ea5faf4-201b-348e-b208-fe5263f42e1a | -10.38775 | -56.77334 | 2026-06-25 12:49:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 40f6db28-80e8-39c5-bafd-1cbef9062cab | -9.48981 | -57.31311 | 2026-06-25 12:49:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 6c38d8a0-5be2-35c0-bd05-e0576d5a322b | -10.40088 | -56.76013 | 2026-06-25 12:49:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 3c4334b9-d564-3e8e-ae0e-41caa21ea784 | -7.7498 | -44.6184 | 2026-06-25 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 7a9bbdf8-09b6-33ff-b9b1-032689db4978 | -6.9791 | -42.9034 | 2026-06-25 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 06bab4b1-78df-35cb-81df-a7f5dd6f8b63 | -11.8868 | -51.7452 | 2026-06-25 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 14cbe3e8-5d21-3d4f-a276-0ebd1f6d6186 | -7.7498 | -44.6184 | 2026-06-25 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| cd79927c-6261-3694-b7e2-9cd1dc37ddea | -6.9791 | -42.9034 | 2026-06-25 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| f3158ecc-246e-3ca4-94cd-6a6824a63c77 | -7.7498 | -44.6184 | 2026-06-25 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| efaacb76-580b-3abb-8008-6beb9f90545d | -6.9791 | -42.9034 | 2026-06-25 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 006ecefb-6b3a-34e1-a305-23144ca9bd40 | -7.1861 | -42.907 | 2026-06-25 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 4741c3fa-c36e-3dcc-a333-cdd55f9f0caf | -7.7498 | -44.6184 | 2026-06-25 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ef663ad9-1368-3d26-bc65-0570fd2aa356 | -12.7562 | -44.4724 | 2026-06-25 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 503.1 |
| a3b9d26c-a46d-3687-8884-503bca2d7210 | -8.2344 | -48.1927 | 2026-06-25 13:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 411a340a-87ee-3c0e-9dfc-76f6733319c6 | -11.8868 | -51.7452 | 2026-06-25 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b264445b-dd6a-31f9-8312-ce496ee53a4c | -6.9791 | -42.9034 | 2026-06-25 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| b22db1fc-4753-3b8e-9777-cf04f426d70b | -6.3036 | -44.6557 | 2026-06-25 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b8bc862d-3b93-30bc-9962-197cab49a76b | -7.7498 | -44.6184 | 2026-06-25 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d16b3cc2-4702-3f5e-b124-d95d3c66d826 | -6.3036 | -44.6557 | 2026-06-25 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 5d53b867-cd48-3266-b8d9-764d6ee968c8 | -6.9791 | -42.9034 | 2026-06-25 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 92a56712-7058-3d6f-b36b-4d3a1bef7302 | -6.3036 | -44.6557 | 2026-06-25 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| fc57c85f-9bfc-3a64-b458-409221932fdc | -3.5462 | -43.5663 | 2026-06-25 13:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| bbcce307-be4b-3c49-a966-3b39068d6ea1 | -6.9791 | -42.9034 | 2026-06-25 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 2f864eb9-57a9-392b-b26e-711b9107acfc | -7.7498 | -44.6184 | 2026-06-25 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d9012c1f-90f5-3c8e-b72b-b18846756e4a | -6.9979 | -42.9016 | 2026-06-25 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| b36684ad-4a7f-30ea-97ef-28cceece2ba2 | -6.3036 | -44.6557 | 2026-06-25 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 302a7544-81a0-3869-9a47-98ac47b3792c | -6.9791 | -42.9034 | 2026-06-25 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 1f51358f-31a0-3499-97d5-dab095ceb412 | -6.3036 | -44.6557 | 2026-06-25 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 81d1ed11-e4e4-3e75-8e0a-e677f4a0a3fd | -6.9979 | -42.9016 | 2026-06-25 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| a2bbcb4c-4e58-3cf9-81b1-4c38348cbe06 | -11.8868 | -51.7452 | 2026-06-25 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 8ef01348-ecef-3195-ab46-f16cf55bc4b7 | -7.7498 | -44.6184 | 2026-06-25 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 4527bce0-4049-3252-b395-de224590a381 | -6.3036 | -44.6557 | 2026-06-25 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| fe9310b8-c37b-3a25-a04f-82c50711c1aa | -10.3569 | -50.06 | 2026-06-25 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| b4afd5e1-f84e-35fb-8597-97eaf1d40327 | -6.9793 | -42.8798 | 2026-06-25 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 63f90ce2-96c5-3b01-87f2-a5b56973904c | -11.8868 | -51.7452 | 2026-06-25 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 3f6812da-f5c4-3998-8cba-fbf3b91fa72a | -6.9791 | -42.9034 | 2026-06-25 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 21e05054-3699-3438-af7d-d7c3e7b6ef7d | -7.7498 | -44.6184 | 2026-06-25 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b9b1fdc2-3ee1-34a0-9d00-8e44ecce39d3 | -6.9791 | -42.9034 | 2026-06-25 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| b32961eb-869b-381f-a787-c1d1902671f9 | -7.7498 | -44.6184 | 2026-06-25 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8c36d1bd-a1cf-30b1-b43f-0d0d8a432f15 | -6.3036 | -44.6557 | 2026-06-25 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 4f8c67ae-c3a4-3f13-ae80-970eef3487ee | -6.9979 | -42.9016 | 2026-06-25 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| a4ea54cf-9d62-32da-8dd2-cee1dd70daa7 | -11.8868 | -51.7452 | 2026-06-25 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 53256cb3-196e-37e7-a2ee-2143768ce4e5 | -10.3569 | -50.06 | 2026-06-25 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c49c4821-7a7b-31c1-8f1d-bb0087bb64ad | -11.8868 | -51.7452 | 2026-06-25 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 18fd47ce-58d1-3046-99c7-892859d3eff7 | -8.3218 | -47.1307 | 2026-06-25 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e0c50829-db8e-37a0-859e-4cbf8aeb88a1 | -6.9793 | -42.8798 | 2026-06-25 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 4493f33f-e559-36cd-a9aa-b3da2e7b49a6 | -6.3036 | -44.6557 | 2026-06-25 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 869f3c25-5750-3beb-9137-7d37ed0d3b59 | -10.6061 | -47.1727 | 2026-06-25 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 0d26160d-ddb8-3347-8d0d-a7b84952bffe | -6.3036 | -44.6557 | 2026-06-25 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 83441651-51b2-3937-bc23-4aa38a86671a | -7.7498 | -44.6184 | 2026-06-25 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 97590eb8-4e66-37cc-8897-7a09b6ce4335 | -10.6061 | -47.1727 | 2026-06-25 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| b6761d51-e785-36c2-8486-9647c7e1cf5b | -11.8868 | -51.7452 | 2026-06-25 14:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| eac4156e-3c59-3157-bf30-1842d5638071 | -6.9979 | -42.9016 | 2026-06-25 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |


[Clique aqui para ver as próximas entradas](README20.md)
