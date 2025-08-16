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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5996080d-b58d-3da2-9cc3-df0eed0cf610 | -7.38538 | -44.91795 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7032429-a494-3ae0-a8b8-adbc812b489e | -6.55864 | -43.03101 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dd679a92-6a83-3b69-a00c-4ba8349f8798 | -7.56471 | -61.4286 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60068af2-0d68-3a54-b9b7-5358f4180d57 | -5.36685 | -41.23244 | 2025-08-16 04:32:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7dc58e20-c9fd-330c-948b-7baebbca4060 | -7.5361 | -50.52697 | 2025-08-16 04:32:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7bd0cbe-cd9b-3bb8-b7ae-c33f8fd39fa1 | -7.56579 | -49.3037 | 2025-08-16 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e6b1b40-a816-3c67-92e7-d4890a520563 | -7.24419 | -57.63038 | 2025-08-16 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7477f102-3eb4-3a08-827e-8effdc9ad982 | -6.55463 | -43.03042 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a9c42e77-e4cf-3743-8eb4-fb871fa3fc7f | -4.29462 | -48.06163 | 2025-08-16 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 880d01e0-49d8-3cd4-a339-f923ea5af003 | -8.34441 | -44.94704 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78495e71-aae6-3e3a-ae04-a9ec802514d7 | -9.80641 | -48.54403 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa3a3f49-023f-3fc0-879e-67c6d7d67df4 | -7.55249 | -45.42056 | 2025-08-16 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4670504-6519-3d2e-a309-0aac2ee65f17 | -9.83449 | -47.82225 | 2025-08-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 376d8815-f467-3d4e-809c-f710fad30aec | -6.65725 | -58.8219 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bb23ac1-506b-3696-a482-c72124b83813 | -6.94858 | -59.5175 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 213fa61c-5418-331f-9395-af34744b08ee | -7.42444 | -44.8802 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f09e96c-361f-3f98-82f7-50c6393f757f | -7.40133 | -44.8856 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24a1c2a2-2ce5-3649-b87b-8f45240aea12 | -4.07699 | -48.04133 | 2025-08-16 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cd41fa6-0b49-376f-8c5b-bf6108e9025e | -7.91541 | -61.74949 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d74b66af-252e-3d77-9ccb-e0c4b61ff3b6 | -3.35914 | -43.35859 | 2025-08-16 04:32:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 873add5e-c907-3320-8466-e2dfe0a44d30 | -7.13111 | -44.6184 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e44f2fdb-f156-3b49-8dba-66549add0276 | -6.6256 | -60.00428 | 2025-08-16 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b88fffc-50b2-32de-a054-1f4c687fd1f3 | -3.4274 | -43.34359 | 2025-08-16 04:32:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37f532b0-1a43-314a-bc75-09575cfb82ee | -2.50949 | -51.81879 | 2025-08-16 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 216a986e-d881-39ea-a614-7f5691ea1a74 | -7.87262 | -61.82241 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29f6c01f-05fb-3595-9afd-8bbc3af391d4 | -7.40431 | -44.89051 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01035701-67cf-39ec-9b46-63ede04f3194 | -7.52077 | -61.31373 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4638ed38-9006-3e45-90a5-d4b563124064 | -8.29345 | -44.9647 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc7f72b6-65b8-3847-b761-325baabb6406 | -9.1638 | -45.31629 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f52b07f6-b856-39db-93d5-6dc8ff7151c1 | -9.36685 | -47.99079 | 2025-08-16 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a0d0496-9e9c-3ddf-87b3-944f9359369e | -8.10991 | -42.35927 | 2025-08-16 04:32:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5f7a864c-7f3e-333d-9981-01462fdf359a | -5.75701 | -46.66714 | 2025-08-16 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e2afb9cc-e621-388b-820a-e18e897a06df | -2.90575 | -48.25086 | 2025-08-16 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab7689d7-62dc-3fa0-beb4-e115fbc48073 | -7.39344 | -44.88869 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28c08556-ba1b-31b6-bf8f-80d6de970582 | -7.0094 | -44.31511 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09bdd7c0-9594-399c-9dbb-dda687e48c51 | -6.95298 | -59.52819 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cd2914e-c83d-3313-b670-afe3ffae1e8c | -6.55962 | -43.03538 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c5e0ea7e-7836-3e0b-9847-c31fa9935f14 | -8.19021 | -45.02913 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1db5fe55-eb02-318d-844e-c027df76d48d | -8.74708 | -44.04266 | 2025-08-16 04:32:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1626eae0-655e-3b41-a387-a53f0dc6ed72 | -6.96239 | -42.86195 | 2025-08-16 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0d54a5db-aa8c-315d-8a8a-91e3490a0493 | -9.86322 | -47.8302 | 2025-08-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52d2d47b-0e42-3b1f-b1c7-ace2d86ec01e | -9.85656 | -47.82917 | 2025-08-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1db07b08-2cea-39c3-be85-93709da303e5 | -3.73889 | -53.98088 | 2025-08-16 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60707d73-69e7-33ad-9b7c-d95ca5c78c6c | -4.51919 | -47.13262 | 2025-08-16 04:32:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3966306-0869-3bcb-89df-e2ffd22c5fe6 | -8.18357 | -45.02379 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e899f39f-5070-3446-a765-e59a064f22c4 | -7.91668 | -61.74291 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1f7b3edd-6775-3687-a1fe-9b194778004f | -9.33653 | -45.97908 | 2025-08-16 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe98517f-1458-37e4-832e-26af04e357b9 | -8.38055 | -47.01602 | 2025-08-16 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad700c0c-9da2-3792-8839-6b7218f74096 | -9.8075 | -48.53706 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6a00e0a-f56b-398d-9a8b-c59b6646d9d4 | -7.38964 | -44.91426 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8974bb41-cce7-3179-bd2a-4c0e14000583 | -6.94857 | -59.55243 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab759ac8-0054-3d82-8db8-4ced1a283b72 | -8.1793 | -45.02748 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a93f167b-8196-38e1-8f95-04af39374feb | -7.40817 | -44.86468 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ffff20b-e4a6-3bed-b5bf-b97d3cc037f1 | -7.07122 | -59.22792 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ae41c66-49e8-3576-87de-5a5c7b3bb3ff | -7.01246 | -44.32008 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ab0083d-edb1-3ea8-92e5-476a7c8fd0dd | -10.53774 | -42.5518 | 2025-08-16 04:32:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 69889e57-8242-31d2-aed3-76834b68c306 | -8.80003 | -52.03414 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cae86022-c92e-3e6e-ad6f-0a817077ced8 | -5.5707 | -52.0447 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3485c0d6-e866-32ac-bcff-857a7c62ed02 | -3.98612 | -47.88536 | 2025-08-16 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8e671651-2b05-3251-b5e4-8f07d037b507 | -8.94575 | -45.81457 | 2025-08-16 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51d9b9ad-9b5e-39a6-9f28-8b816eb71910 | -7.59457 | -55.19366 | 2025-08-16 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbc3171f-c051-34cf-b75f-46e02bd66f6b | -8.94637 | -45.81053 | 2025-08-16 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce7684d7-3019-3457-a8df-f67915b34a5b | -8.80449 | -52.07563 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23acbcc9-f8d4-3b62-982b-753a4e44d39d | -7.38602 | -44.91366 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 364970f2-1ae3-3bde-b1ad-d702a2a4c5f5 | -7.52979 | -61.3474 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aae7863a-3b13-3943-b2bf-c757a93afc0e | -4.29517 | -48.05816 | 2025-08-16 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04f6f1f3-8aa6-3ef1-b403-2bd72c68945b | -3.3813 | -52.71938 | 2025-08-16 04:32:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1aec31d8-6379-3c63-ab97-413502afd40f | -4.91377 | -43.25561 | 2025-08-16 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 137b199f-52c7-3923-bf44-bb18e1f4d8c2 | -6.9336 | -59.52991 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 298fa3c1-d7bb-3beb-bb14-4ee4efe435dc | -5.92907 | -53.65048 | 2025-08-16 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7913f7af-e341-3aca-aabe-9fbf1ea9cc22 | -7.0143 | -44.31861 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d10cee92-6f4c-33fe-89b7-c9c5e85ae574 | -6.93541 | -59.55479 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1a42a96d-c133-38c7-b02c-db73976ab7fc | -9.02637 | -46.59203 | 2025-08-16 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3e5e85a-c7c6-38eb-84fb-fa31a69def25 | -7.90166 | -61.74658 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bff3b7f-8c86-31a9-a5ce-7013f38bba19 | -9.1668 | -45.32109 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 914e8dec-b94c-3eaa-8800-5b90443a51d0 | -10.24381 | -48.26579 | 2025-08-16 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7723eee0-a3f9-34d6-80ec-1daaf87c840b | -6.6743 | -43.7628 | 2025-08-16 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01ccaaab-6a4a-3da8-8ada-f33c6c69c351 | -7.27071 | -47.90952 | 2025-08-16 04:32:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57face7f-33a9-33b4-a074-f6140b46f630 | -9.85485 | -47.81807 | 2025-08-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe0cce56-ed80-3683-82b8-fae14245ff9c | -6.56115 | -43.02478 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8274f9eb-8189-374e-8041-e06a59619262 | -6.61296 | -42.75117 | 2025-08-16 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e1eaaec4-f210-3487-ba86-1d8db37017ee | -2.5849 | -51.9225 | 2025-08-16 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58e88113-d5ff-334a-8b00-1beb3b282727 | -4.18752 | -48.22242 | 2025-08-16 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03a4fd0a-123e-358c-9bbf-8e5e0e6e8a48 | -6.56516 | -43.0254 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1163f509-19f6-3588-8d29-6f747c808ae2 | -8.18421 | -45.01955 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 897d076a-e5db-3d09-8e5a-5478cfb9246f | -6.66317 | -58.82295 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5bf1189-93c6-38d6-9118-009cd4a3dbe9 | -6.94157 | -59.55591 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 23bd623d-2092-3ba3-b61f-3d518d32a5e3 | -6.55561 | -43.03476 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1d6720bd-6875-3791-ae6a-d9988805c3ca | -6.58346 | -42.23442 | 2025-08-16 04:32:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f06da30-86b2-3822-a6a2-ca0b5def6692 | -8.18657 | -45.02857 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdad15a0-0e09-35e5-9520-644ca419eab6 | -7.81216 | -61.32983 | 2025-08-16 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44c897df-9e06-305a-905a-f0fbbd5386ed | -5.56993 | -52.04949 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b15061ab-83fe-3a89-acb9-4035d1f7eb6e | -9.16317 | -45.32054 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 987d3bfb-a07c-38c3-8f3c-f6fdcc27cb67 | -6.67814 | -43.76336 | 2025-08-16 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76a43d17-31eb-353c-8388-7ad9e986ec87 | -3.82513 | -47.74296 | 2025-08-16 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5555e59f-5a6f-3d38-a6a8-5bfbfa0cafbd | -6.94945 | -59.54762 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 512a2968-f98b-3814-a008-641bd39828a6 | -6.93274 | -59.53456 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0b444d9-1bb4-3c90-bfcb-8a5a0ab0f083 | -7.20727 | -46.24034 | 2025-08-16 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62b660b1-4798-3ac6-91e3-6f80dbf5696a | -6.13525 | -57.93129 | 2025-08-16 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f03ddbda-fb78-3a67-8e2d-8edd28c53e84 | -2.82205 | -49.00412 | 2025-08-16 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README39.md)
