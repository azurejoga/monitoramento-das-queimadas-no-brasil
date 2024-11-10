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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90d75d66-2850-3d38-948c-5bbd1e2ed602 | -5.56353 | -47.77843 | 2024-11-10 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c5409c91-6ed2-3457-a60d-1d6a50fb90df | -2.36919 | -48.54083 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed9d7d16-6176-359a-ab80-ce177de0a81f | -3.12943 | -50.43785 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 1534d56b-6df7-309d-bde2-f4a4a40ef29f | -2.72662 | -51.71641 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 519048b2-b4e7-3a35-901c-6b3e7f6abbd6 | -4.85909 | -43.97137 | 2024-11-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 084eec58-4e71-3f65-8e20-8426a61db37a | -3.71047 | -50.43709 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54774168-020a-30da-a4aa-b123d02567ce | -4.11839 | -45.70555 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3839767c-de7d-3fe4-91d3-c9297e2be291 | -3.24214 | -50.30023 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1263d1be-37a0-30a8-b362-a8074927c6e9 | -3.24158 | -50.27282 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8303a77e-d6a1-3588-981b-357cfacdc7d8 | -3.03517 | -48.04568 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b55e463-d736-3ea7-b03f-8a313e7615b2 | -4.43737 | -45.91209 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6ef22b9-8268-3054-86e0-07bdbf4804cb | -3.24396 | -46.47271 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0e95df9-f9ea-39cc-8af5-a2144a31ed93 | -4.6328 | -49.08876 | 2024-11-10 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 639cd919-61f2-3b1a-b666-a211d9466496 | -2.93216 | -52.77723 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 05e4fd21-043e-396a-9b07-0e190be16bbe | -1.30513 | -54.67446 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 74b8e5dd-f6c3-3915-af0a-089eb37df479 | -2.67408 | -51.82101 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1eaa12b8-f012-3128-ac61-b0939cfc9da7 | -1.13777 | -54.10824 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2fa0609e-1261-3aa3-8dc0-fdf314310c86 | -5.01286 | -45.03886 | 2024-11-10 04:14:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c319c34f-60a1-324c-880e-c4524b5294c9 | -2.10009 | -46.5399 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5764b39c-c919-3d09-9629-db61a059f37e | -5.07294 | -49.62851 | 2024-11-10 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15e91e8b-498f-34bb-90a7-7d372bf0bdfe | -3.78753 | -47.73011 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60d9d029-5b79-3fae-9d4d-ad43c7719df3 | -4.27465 | -50.67432 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c99de5c3-dad1-3755-9445-e51ac268c5a6 | -2.14148 | -46.69082 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db39d1c9-0d89-31ce-9f2b-7979d1f0b91f | -2.24873 | -53.67232 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 704fbbeb-5f53-32e6-9439-22c08b092f28 | -3.84406 | -44.12871 | 2024-11-10 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1708501-2685-35d7-93a5-0d94ec376217 | -2.89992 | -46.82757 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26dc4d2f-1771-3986-8429-13668d9d2be3 | -2.42015 | -51.95676 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7bb5c58b-81d5-3d0b-b5aa-5e88b123905a | -4.10119 | -45.69872 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d155545d-0560-3459-bda3-0a10c4626cc6 | -1.6228 | -52.53858 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c8added-9f27-34c3-9429-99b792d853c7 | -2.32059 | -53.8768 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d30a96e3-2b1d-3195-8282-81b619e85bee | -3.25034 | -48.75827 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0160f2f-eadd-35ab-a556-7a81d849c343 | -1.48033 | -51.74787 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f986a0a-7b0a-3620-820b-e577a057b852 | -3.2664 | -46.31024 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad1d3f3f-35e4-32d0-a6ee-339439f8d8bd | -3.78581 | -47.74054 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0484c1d6-0176-3c55-886e-6aab918700be | -2.98073 | -50.30333 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0269d4bb-7718-335d-b815-069f054944d5 | -5.56829 | -47.77404 | 2024-11-10 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b454d994-1011-3fa5-a71f-07d801651682 | -5.11419 | -49.92205 | 2024-11-10 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 548da1b3-8ac1-34db-8985-9b867d1c6302 | -2.35205 | -48.92771 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d9d54e9-bdae-3acd-8473-29a97718e3b1 | -2.87981 | -49.22386 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c25e658-a43b-30f9-b05a-b43904b4ce03 | -0.29071 | -51.72572 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 933ca77b-4aaf-3fb2-b2ac-68a9ae4b6e63 | -4.01463 | -48.30138 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 422c3a40-486d-3a5c-9251-ebecf50ae844 | -2.21081 | -47.74756 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eede11f0-34ce-34ff-b574-d30015af919e | -2.46233 | -48.83041 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e28bc1a9-3e18-3ba5-af8e-80d1274192d8 | -3.61727 | -47.51881 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89a96d64-d08a-34b2-94d4-ab2f7a51553b | -3.31296 | -51.66141 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d073a952-266d-3014-b243-294492d87ee7 | -2.61824 | -51.29715 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19884861-f5e3-31f3-b7e3-606655c36730 | -2.41907 | -53.66985 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 09ecdcf2-e4fb-32df-b9a5-34b71f0c80a6 | -4.07457 | -46.06807 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 09a9a90c-1b31-36e1-86c9-80b44c77373e | -5.45593 | -43.26749 | 2024-11-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0be5fbe5-268a-3f63-a1a0-a4e2886f3563 | -6.45244 | -42.74577 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0468b69a-2274-3f4d-823c-1a07116c2994 | -2.56683 | -47.34869 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba0bd28b-3d6a-31ad-b53e-b486106e5181 | -4.37543 | -45.57454 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fef26f57-ac95-35a2-8b8f-97159ba66200 | -2.31241 | -46.08462 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bd0ae21-8036-34ee-beb7-6523c1b4cccb | -3.59258 | -42.85115 | 2024-11-10 04:14:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8bf0a42-bf50-3c3a-b031-2d9ee95a5e21 | -3.29365 | -43.54174 | 2024-11-10 04:14:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 139b194c-fbe0-3764-b200-425987ac06eb | -2.8582 | -48.44533 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b16edcd4-725e-33a7-9785-cf37cc2f2552 | -2.23694 | -53.78362 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54f791c9-9b4e-3a02-b288-51e9844d3b13 | -4.12796 | -46.84265 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b371500c-7ba4-3792-be3d-bd3fc122f7d4 | -2.53085 | -47.38507 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f40dfac-39c4-3f3d-9f2f-07bf2702625f | -2.08415 | -46.79467 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad7c8108-773f-3614-9032-959ab1f8855d | -3.48147 | -48.2415 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f978e0c8-36e3-3ffe-8470-036e20d821cf | -3.31662 | -44.39602 | 2024-11-10 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0af7d658-1ce0-3858-869f-fc64a0d396c2 | -4.16642 | -46.59976 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b46062a2-f47b-3a79-9336-5c3f41083c62 | -2.31128 | -48.79075 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3101a71-8932-3ec8-8bb1-65515bdbec85 | -5.93596 | -42.76397 | 2024-11-10 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 124da4fa-e4e0-336a-8e14-a585856496af | -5.28186 | -45.37599 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bea74ddb-7484-3c4d-a091-5a6ee6dd30be | -3.34468 | -50.35499 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be49c2b0-926a-3d9d-9026-20af4227c758 | -3.24787 | -50.20312 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 571cbe80-7a75-37f5-bfe3-ef000988d369 | -4.69705 | -49.62786 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 910d5948-5542-3840-9d98-4d1307b6f3fb | -5.36833 | -47.91815 | 2024-11-10 04:14:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 316d8568-2bd0-3e9a-9756-43586aafb0b4 | -2.76316 | -49.35848 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| da147f9c-8f74-31fb-909c-1c1df208d138 | -3.95916 | -46.70866 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8fd36afb-5224-320c-bcea-5d187c6f4c4f | -2.96083 | -48.01885 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd770ee4-5dc9-38c0-89a7-d62d84682ec8 | -2.67511 | -51.82507 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24c945cc-c345-37f9-9f59-d3d18dcb8d3a | -2.62004 | -46.16584 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a10bc97-1452-372c-8772-09e58b66e81a | -3.38831 | -51.46547 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 379cc902-2d48-3d23-a5e4-659d60079f5c | -1.42757 | -52.27641 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f7ff8c2-fed7-3706-aa0f-39150a38212c | -5.15661 | -44.24298 | 2024-11-10 04:14:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19ecc257-d8c2-364a-818b-bcf241d8f5ab | -1.47103 | -55.65215 | 2024-11-10 04:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e6d5d8b4-0076-3273-9182-d2281db61330 | -3.97386 | -48.17414 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a7fb5a5-35d5-379e-a6f3-8dc331f23bdc | -1.53809 | -52.20598 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dab23345-e252-3c32-9e61-e77a05d36e78 | -1.7658 | -45.61146 | 2024-11-10 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2386bdaa-5aa9-3561-926f-3a744fd05b31 | -4.05788 | -49.20946 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5f2864f7-4f1c-3d82-8689-3f4a097d5a85 | -4.35163 | -45.6321 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a36d5697-d248-3532-92c4-d11da98d9cdb | -3.44259 | -50.30478 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ca5cb85e-c5a3-3f3f-b708-7e1ec953b4e3 | -5.55332 | -41.65307 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ddeda6af-9c66-3e2d-91d9-d8dde43bcc41 | -3.1051 | -49.42624 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1c44299-250f-32a2-a704-554daddc7df5 | -2.87359 | -51.48124 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d9d09c71-3f67-39f5-8300-7813236c0c58 | -5.18048 | -46.18835 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dbe0026-3205-335d-b84c-71262715c97a | -0.46433 | -52.02515 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 125159d5-9c81-3246-a108-bfbd3ecc3e50 | -2.87094 | -50.40699 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f4fa6c3e-15fd-3f0a-b3a5-3df2e2164b54 | -1.34047 | -54.6242 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b22360e-3494-30a2-ac6a-317908683fac | -2.09083 | -46.52385 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9333ccc3-a6df-37fc-8320-99af2e55090b | -5.29934 | -47.88953 | 2024-11-10 04:14:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 166eeb58-bad6-3abb-9b0c-bcc47fae7692 | -5.23674 | -44.07775 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7a1ce5d-2217-31e9-9b85-d51afb081d95 | -3.20246 | -49.46461 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 63a5db46-02e4-3269-80e6-567244d177a5 | -2.38763 | -46.78437 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0cb748a7-e9a0-3470-b788-96b7248db90f | -1.28401 | -53.7135 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| bd2b1111-df4a-3112-9b5f-38dfabaedc1e | -2.24151 | -53.79468 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f841a0ef-095d-38e5-b890-e589282b3b0c | -2.3998 | -46.50784 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README33.md)
