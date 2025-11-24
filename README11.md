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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f3e9b5e-2ce9-382b-8ceb-0749a8f0859d | -1.09446 | -54.1032 | 2025-11-24 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dacb3bc-b52b-3c6a-bf9a-957533fd4cb4 | -2.88196 | -45.26295 | 2025-11-24 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5985d4ae-17e1-3dc8-95d9-52cfaa87f348 | -2.79484 | -45.36556 | 2025-11-24 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9bf8c50-f697-32a9-9f3c-4319553fa228 | -3.81128 | -43.35854 | 2025-11-24 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4506f544-9ee3-3b8c-9e92-72f32a0e9afe | -1.20525 | -47.92245 | 2025-11-24 04:55:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75a90545-487e-3484-b0e0-8ce14ecc19db | -2.88159 | -48.99519 | 2025-11-24 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55ad2b7e-ac3d-3fc6-909d-33115d1b6ac1 | -2.873 | -51.80421 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a853449f-56d0-3ce1-87e9-13c554cadc39 | -2.8826 | -51.80941 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 116865f5-0169-369a-bb62-4a0c25767f34 | -0.26103 | -48.79787 | 2025-11-24 04:55:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72957c00-9127-3760-a088-7bbc33936192 | -1.49244 | -54.81521 | 2025-11-24 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bfc21da3-95b9-3b2b-87ed-17b03eb8b581 | -1.14227 | -54.14663 | 2025-11-24 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0048648c-24f9-3154-b3a0-2564bafcf275 | -2.87413 | -51.79694 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7b9d554-cf8b-3d40-8642-3fcce74f734e | -3.58932 | -40.97533 | 2025-11-24 04:55:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7602015e-5cc8-3e94-96a6-d8d9447ab3fc | -2.14504 | -53.6504 | 2025-11-24 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e7e118f-35f2-343d-be61-7fcf65058a8f | -2.8713 | -51.79277 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca3a1bc8-7467-3a20-a7d4-8633820cc238 | 3.11207 | -60.76715 | 2025-11-24 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f98acbde-1fa9-3311-a9a8-8e998135dfeb | -2.95393 | -48.59934 | 2025-11-24 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef759ad1-b9e6-326f-a035-64e0a386f631 | 3.80573 | -60.19374 | 2025-11-24 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7859e02e-3871-3628-8ea8-d4e78d2a0fb9 | -2.48542 | -47.83422 | 2025-11-24 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77e74cb1-2bc3-3052-a318-8ec80507f9ec | -2.2801 | -53.80593 | 2025-11-24 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2dac82e7-5969-3101-ba3c-15fb440f014e | -4.26411 | -40.85929 | 2025-11-24 04:55:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c68dd404-3cb7-3167-b87d-e50f2de6d2a4 | -2.87921 | -51.80889 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0343f1a8-3e2c-38fa-b2b5-920280b0f843 | -3.71298 | -44.00923 | 2025-11-24 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a668c551-a45d-3b7a-9315-d0e43b5ec6b2 | 0.06933 | -51.09541 | 2025-11-24 04:55:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10c1eb5d-d3bd-3ab8-b8a4-3d0558463271 | -1.14561 | -54.14711 | 2025-11-24 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f898aab-079f-3e28-8d92-9b5437b70024 | -2.16254 | -45.98954 | 2025-11-24 04:55:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98eef44c-a018-3fb7-86b2-aff257d2c790 | -1.33612 | -53.17856 | 2025-11-24 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a733e5f0-edde-3fa4-be32-36da21fb7f5b | -2.92609 | -48.23698 | 2025-11-24 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98788d61-a555-3d70-82e1-ab645bac7b56 | -0.79305 | -52.48459 | 2025-11-24 04:55:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfae5fb5-4027-3a5a-a070-72ffef6dffb8 | 3.11298 | -60.77338 | 2025-11-24 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82acd58a-5b59-39d1-8c5e-33812c1ed1df | -2.2974 | -53.91122 | 2025-11-24 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 379a9a81-a627-3291-86c2-3070fa980cb8 | -2.94994 | -48.59875 | 2025-11-24 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af586c35-3afb-376d-884e-e8a3283bdc52 | -2.88203 | -51.81303 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d925b297-02db-3896-aaab-bd6375ec2ee6 | -2.28615 | -55.46992 | 2025-11-24 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b87c71f9-2d70-3cc6-b0f2-71653dcfd0ce | -2.76821 | -48.95078 | 2025-11-24 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cef9afe0-a4ed-39ef-ac5f-d505482f6dc0 | -1.75648 | -53.89325 | 2025-11-24 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b08d800-7217-3576-8ad0-569d94ce56f2 | -2.77137 | -49.64254 | 2025-11-24 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11d1238f-2fcc-30b6-96e9-fe43ef9849c9 | -2.87582 | -51.80836 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 355c252a-cd9e-3240-a067-f61233417997 | -1.66585 | -50.46116 | 2025-11-24 04:55:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fc0e560-5b4d-3ce6-bd61-2177abcf862e | -1.33282 | -53.17804 | 2025-11-24 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3fe5ec13-ce90-3121-9338-1ebb49bea92f | -2.71821 | -51.89138 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91de2b3b-5a98-39de-8832-1a95ab7c31e4 | -3.17659 | -50.24329 | 2025-11-24 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9dcbb95c-da55-339b-914c-4a795dcd196d | 2.33848 | -50.77877 | 2025-11-24 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b53b5bcc-12e5-34f0-9604-022e6c4067c0 | -3.21867 | -45.93486 | 2025-11-24 04:55:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 12bc3978-3b7f-3292-b364-9dc23acf1e15 | -2.79569 | -45.35989 | 2025-11-24 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e33ee68d-ab7e-3f53-900e-24a2575aed25 | -2.88034 | -51.80163 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 767c50b2-39a7-3ced-90bf-90e6445d31c4 | -3.27497 | -46.04713 | 2025-11-24 04:55:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ec5e550-ddcc-379f-8e35-e9c46af1418e | -1.8292 | -45.57513 | 2025-11-24 04:55:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96f2727e-3849-3577-b277-1c47a6c7094e | -4.26327 | -40.86535 | 2025-11-24 04:55:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| a403ed93-51b7-3670-b37f-1925a00b032b | -0.26556 | -48.79383 | 2025-11-24 04:55:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6daa5dec-8665-3828-a424-6b2df64642a3 | -2.1451 | -46.4119 | 2025-11-24 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42519e09-74e4-3501-9997-a3f7e7eea639 | -2.49521 | -51.81716 | 2025-11-24 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4ae79a1-cc14-3f53-9e05-1b732f4d4a77 | -2.88486 | -51.81718 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1befd529-fe6e-35e9-a39a-b31aa5d2d900 | 3.3126 | -60.08375 | 2025-11-24 04:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b5ba20f-2da5-3c05-a518-6e276913757f | 2.0368 | -55.8152 | 2025-11-24 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed65368c-370f-370a-be94-8ee1224a8dcf | -0.91965 | -47.74967 | 2025-11-24 04:55:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 400a2b09-e2cd-3c75-9615-65df15e6f6c4 | 3.30951 | -60.08797 | 2025-11-24 04:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0aeed362-164d-3c84-bbf2-502d1eda5aa2 | -0.18666 | -50.10416 | 2025-11-24 04:55:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 549c862b-ccfd-3cf8-925f-5d1ed8b0bbce | -3.28925 | -43.40152 | 2025-11-24 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7cfbbb8-df93-3989-9a55-08ea5c923437 | -3.27022 | -46.04628 | 2025-11-24 04:55:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4018b1ab-8744-350f-ab7f-1fb88b9b2a51 | -2.79521 | -51.76271 | 2025-11-24 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd908d05-8d1b-37da-b5f7-458fa3a1fa70 | -3.71283 | -44.00959 | 2025-11-24 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5cda9ef-1c9c-3f8c-87e3-66a6c987e30d | -2.13215 | -53.43011 | 2025-11-24 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5dfdee58-caab-3f84-9975-a708b7843a71 | -3.18023 | -50.24383 | 2025-11-24 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c5cc37e-41a9-39a0-8ee3-3e5c2cf8c0c3 | -1.04972 | -53.54836 | 2025-11-24 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 585afc94-4960-3041-a014-b136efee06e9 | -2.12776 | -53.43646 | 2025-11-24 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e61252a1-804a-3705-a4bd-ccdd19f68ae1 | 2.03314 | -55.81576 | 2025-11-24 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12bcf8f6-b614-3819-9a18-cabd1dc824d4 | -2.87356 | -51.80057 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 085cd25e-d1c3-3378-b154-0292e128823e | 3.11253 | -60.77026 | 2025-11-24 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00d8f91e-0ba6-3fa3-8257-07d28f075127 | -3.3964 | -47.5709 | 2025-11-24 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35911d83-958a-38d9-941b-31a1e1695a28 | -2.72789 | -53.20721 | 2025-11-24 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bfecade-9a2f-3006-ab70-5752be43f796 | -1.29711 | -52.32588 | 2025-11-24 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f59ed39-ec72-3a54-8802-b7f4d6dc080f | -4.26808 | -40.86843 | 2025-11-24 04:55:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 02cc7388-dea7-32a7-8178-e48d8f1ee9a7 | -2.69814 | -49.51352 | 2025-11-24 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0d726f4-a61a-3ee0-88b9-be934d0074af | -2.87695 | -51.80111 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a7c692d-6757-329d-854f-52183d8849bd | -3.59493 | -40.98362 | 2025-11-24 04:55:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b3e480a9-5ad0-388b-9bb1-3974d0f13c89 | -2.27679 | -53.80542 | 2025-11-24 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a09694b2-28ae-37bb-9808-a07d145fecee | -2.80068 | -45.36053 | 2025-11-24 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dcb4f51-b2d2-3f9d-aeda-8f9dd9638f6a | -0.95114 | -46.87868 | 2025-11-24 04:55:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e43c14d0-e1cf-3615-b471-e2a8ea6c46d3 | -3.21948 | -45.92966 | 2025-11-24 04:55:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b6b2b1c6-2186-3b13-b00d-29d15280a7b9 | -2.92665 | -48.23336 | 2025-11-24 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1a266fb-8a06-334d-b1c7-f35b303af3e5 | -2.13545 | -53.43063 | 2025-11-24 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5db6fa09-b9a5-3d92-8de0-da03678d3476 | -3.21878 | -50.16633 | 2025-11-24 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51d1a742-0116-314e-a332-e68dfe2deac3 | -4.23968 | -48.90004 | 2025-11-24 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6628151-9e61-359b-b382-1449128108f5 | -4.11831 | -50.07692 | 2025-11-24 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d793ab2-65fd-3baf-8ecc-7818185fe4b3 | -3.85844 | -48.97925 | 2025-11-24 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93d60cc6-bf4c-3033-87b3-4b6aa1a51e88 | -4.52431 | -45.61044 | 2025-11-24 04:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32c33b3a-0988-3255-ae1c-74bf8e2ec870 | -4.67041 | -50.40575 | 2025-11-24 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d91857e-532a-38a0-b0ab-0b79842649bb | -5.81606 | -48.68501 | 2025-11-24 04:57:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63f6df6d-7014-3739-a79d-1ec6d7c1daf5 | -4.82422 | -43.83029 | 2025-11-24 04:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a0004b01-5d0a-3a2f-ad42-bcabfd967bd0 | -3.69786 | -47.67868 | 2025-11-24 04:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5993ef8e-bd03-3478-83ed-df509a72b53d | -4.52807 | -45.61958 | 2025-11-24 04:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2b87413-df0a-3817-9f3d-e504379a8609 | -3.62742 | -53.62343 | 2025-11-24 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 497458d2-4d45-3b35-9517-13be51b0ccbb | -3.93895 | -50.51947 | 2025-11-24 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34363f0b-ce9d-3410-9748-94a71310a356 | -5.93059 | -45.57676 | 2025-11-24 04:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c228e44-502a-3209-ac16-87f77e0131af | -4.10125 | -49.07169 | 2025-11-24 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e3342c3-5268-32e8-b2dd-fd77e429b246 | -3.62416 | -52.49723 | 2025-11-24 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6fa5e0b-b286-3ebf-a983-28d36008fc8b | -4.03042 | -48.87927 | 2025-11-24 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62488284-fb50-3e78-ae53-6a1099077fc4 | -4.15914 | -48.58289 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 760881b6-a102-3e7c-9f95-4ae1479694a4 | -4.06367 | -50.98238 | 2025-11-24 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
