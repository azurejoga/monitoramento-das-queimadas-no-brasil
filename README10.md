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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d930bec-77bc-30a9-a39b-5fda00fbbb52 | -2.9108 | -48.254 | 2025-07-30 02:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e29ef22d-eaf8-3991-b55d-d945bf60621e | -8.5211 | -43.3063 | 2025-07-30 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| bd6f290f-1ba4-3ad6-8999-9fffec12b0ef | -11.4776 | -45.1099 | 2025-07-30 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 9f4581e9-bc8f-39f1-829e-b2d21d878cdb | -10.6172 | -45.2282 | 2025-07-30 03:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9225fcf1-8226-3f66-9d0c-40d6a4fed311 | -17.4945 | -46.7321 | 2025-07-30 03:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d67d9851-8921-3370-89d7-9dc0418453c3 | -6.5074 | -56.213 | 2025-07-30 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 5aa7d3ae-71dc-38ed-8931-71fd75f0a10d | -6.5075 | -56.1932 | 2025-07-30 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| b779c704-6deb-3018-ac3b-a4fce198f014 | -6.526 | -56.1923 | 2025-07-30 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 3e6484ef-3911-37c5-9d3d-45c5fed1eaed | -2.9108 | -48.254 | 2025-07-30 03:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| e9643ac6-3c1e-3aff-ad7b-81f89ed639de | -10.6169 | -45.2512 | 2025-07-30 03:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e442932e-30ba-3028-bf18-69b9f53bc243 | -17.4945 | -46.7321 | 2025-07-30 03:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b788468a-1a16-3fbc-a173-c66f0a0287f8 | -6.5074 | -56.213 | 2025-07-30 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9d6153b1-13c9-3d3c-845f-322aabcbe71c | -10.6172 | -45.2282 | 2025-07-30 03:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4448e3b0-5c95-3331-b00e-4c035786bfb7 | -6.5075 | -56.1932 | 2025-07-30 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 861777e2-8518-3e94-a048-0f8e0cffdf1d | -8.5211 | -43.3063 | 2025-07-30 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 42f861f4-745d-3458-b938-70be5cf46d3f | -10.6169 | -45.2512 | 2025-07-30 03:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| e4701fb1-8ea6-3270-86bf-991e8f8102a0 | -6.5258 | -56.2121 | 2025-07-30 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| ea09f1e4-6cec-3f2d-ae48-f3d9a4212eed | -11.4584 | -45.1126 | 2025-07-30 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 5f0ccda5-60cd-33d6-8b7f-e5afceb0199a | -6.526 | -56.1923 | 2025-07-30 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| b2837113-0e27-3b13-a664-ac135cc9d34d | -9.74565 | -37.00386 | 2025-07-30 03:10:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a8d59ff8-f2f3-398f-81fd-6df57953e47f | -9.30228 | -40.25446 | 2025-07-30 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 88623aa5-c772-37f1-b6c7-a2b73328cf02 | -9.30332 | -40.24911 | 2025-07-30 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dfe0d162-749b-33b9-b573-d12a6271677c | -9.75085 | -37.00473 | 2025-07-30 03:10:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a9185d2a-0607-3960-a721-ac2e22eeb0c3 | -9.82881 | -41.49659 | 2025-07-30 03:10:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 06f10158-0aa5-3fc7-89ce-922769e12cfc | -10.5221 | -42.55787 | 2025-07-30 03:13:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 78add297-8128-3d04-a988-e530814296b9 | -15.70993 | -41.9357 | 2025-07-30 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ff1a04c7-46d5-3307-8b6f-89cfee59de66 | -10.52445 | -42.55965 | 2025-07-30 03:13:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4bae84d8-bf24-33d7-ad58-4d8ecf8879b6 | -15.70871 | -41.94125 | 2025-07-30 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 02f291c5-ace6-376b-9afe-4599c010cf1e | -10.52353 | -42.55081 | 2025-07-30 03:13:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| eed33aa4-d85c-312a-9125-f59ede3c4e65 | -15.71335 | -41.94105 | 2025-07-30 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3addfc48-bb12-333c-9f06-283518a1cf8e | -10.52592 | -42.55263 | 2025-07-30 03:13:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 29419e1b-87e7-3d8b-8552-4bd75055e78c | -19.73906 | -42.10229 | 2025-07-30 03:15:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 74822780-39ae-3fa3-897f-3cce02d87718 | -18.5648 | -44.42259 | 2025-07-30 03:15:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 81c6bba7-5363-3769-a582-b4a98a5a0961 | -19.7449 | -42.10403 | 2025-07-30 03:15:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5198f09e-e827-34ac-8ba3-f9872d2b839c | -18.56553 | -44.42331 | 2025-07-30 03:15:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 70524737-5506-3a15-aaa5-64e61aa27597 | -10.6172 | -45.2282 | 2025-07-30 03:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2d0d10df-f2e9-3584-bc70-0438ff785150 | -6.5074 | -56.213 | 2025-07-30 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| e7b72598-2587-394e-827b-289bcf153e13 | -10.6169 | -45.2512 | 2025-07-30 03:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a1c28b58-c50d-391c-ac38-4a3792895977 | -8.5211 | -43.3063 | 2025-07-30 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 1cdf366b-e892-3acc-adb9-fc85c3e07ff7 | -11.4776 | -45.1099 | 2025-07-30 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 9defa471-7086-3d84-ac1d-accc9ffb1363 | -8.5211 | -43.3063 | 2025-07-30 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 1c165e5b-58b6-3890-891f-249c62fc00d3 | -6.526 | -56.1923 | 2025-07-30 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| b4960238-65bc-32c3-b91b-919f6d60cd13 | -6.5074 | -56.213 | 2025-07-30 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| bd36ad7f-093b-3205-acaf-62982c147726 | -10.6169 | -45.2512 | 2025-07-30 03:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 78478aed-f9e6-3332-8e0e-58e24946b49e | -10.6172 | -45.2282 | 2025-07-30 03:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 5fcacc06-1846-32b2-883d-6a93ead06371 | -10.6169 | -45.2512 | 2025-07-30 03:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 5b6f39fc-9c03-3ec8-8a03-070b9990dcab | -6.5258 | -56.2121 | 2025-07-30 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 0ce2825a-e8b1-305c-8bcd-c72823b0a52c | -10.6172 | -45.2282 | 2025-07-30 03:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a609a118-1b4c-3af0-978f-0ee1caa8b207 | -6.526 | -56.1923 | 2025-07-30 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 52724899-7c63-3ad5-94bf-660a023c6493 | -6.5074 | -56.213 | 2025-07-30 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1103de12-44f1-3315-a83d-6f0bb9b44b36 | -8.5211 | -43.3063 | 2025-07-30 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 37541403-6012-38f8-ac57-f79748afe772 | -10.6172 | -45.2282 | 2025-07-30 03:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 66b90e81-5a40-3cbb-906b-598099c42067 | -10.6169 | -45.2512 | 2025-07-30 03:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 789f9b40-8988-3d11-9a62-3967ad3e9583 | -8.5211 | -43.3063 | 2025-07-30 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| e45ee90a-d728-3ef2-9ddf-677d5f970b9f | -2.9108 | -48.254 | 2025-07-30 03:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d4ceb8e7-c026-3409-8206-260c21d4c21c | -6.5074 | -56.213 | 2025-07-30 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5350097c-2d97-3486-b748-dcef017bf52e | -6.526 | -56.1923 | 2025-07-30 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 14c279b3-4ccd-395a-b0fa-ba88fd51ca6f | -6.5074 | -56.213 | 2025-07-30 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| db417fe4-2851-30c7-a8ed-6c5edb6bde3e | -7.7828 | -45.0041 | 2025-07-30 04:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| cf1c8a20-e82a-3e12-971d-f2395ee1a8b6 | -6.526 | -56.1923 | 2025-07-30 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6d740f91-f148-3357-a296-0471fe7c813d | -8.5211 | -43.3063 | 2025-07-30 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ff4744c6-184b-330a-9e08-9848678f591c | -10.6169 | -45.2512 | 2025-07-30 04:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 89d89136-d4b2-34a2-b7b7-9bd79a2bbf8a | -10.6172 | -45.2282 | 2025-07-30 04:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 88b89a88-fc7a-3c5d-b19c-ee4dcae7b59b | -7.7831 | -44.9813 | 2025-07-30 04:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| a9cbc6a6-64b7-3783-a05d-cb6f7ef29cde | -2.80927 | -48.66602 | 2025-07-30 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8861f966-cc38-3b50-9e21-95b371e9e3aa | -3.18282 | -48.8094 | 2025-07-30 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83939bcf-d8b3-38d3-91a7-d22a7c3f9226 | -3.6017 | -44.8022 | 2025-07-30 04:00:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6673c4e-a60f-309d-b74e-ad372ba6cc7e | -3.03259 | -47.86224 | 2025-07-30 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c26fea6-3611-3a3d-bb1b-9ec6c41a0e68 | -3.11304 | -47.00962 | 2025-07-30 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79626a0e-bc85-3132-934a-f804ea90aa64 | -4.05703 | -38.28667 | 2025-07-30 04:00:00 | NOAA-21 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 707341fd-6ac2-38dd-94d8-7260d1dbef19 | -4.38639 | -41.91667 | 2025-07-30 04:00:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 169c69fd-e952-3b0b-8be7-1663ada34d0e | -3.51043 | -43.24674 | 2025-07-30 04:00:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0e7a829f-1a8a-3b2c-92f6-4f7d2ac24409 | -3.99464 | -43.22584 | 2025-07-30 04:00:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15eafed3-c9bd-3d62-9670-453bac0b3504 | -3.43146 | -43.34707 | 2025-07-30 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f59b015-49a5-391d-97e3-9bd9c402d87c | -3.82443 | -41.56748 | 2025-07-30 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f8e32960-617a-3ae3-8443-17431e008f43 | -2.66472 | -47.40942 | 2025-07-30 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec6874af-6a6d-38b1-9d9f-8f51bc6d53b4 | -3.82621 | -41.55628 | 2025-07-30 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b38ecb2e-f5e9-3ea2-967c-a3877ce007aa | -3.03925 | -49.42361 | 2025-07-30 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 722ec69a-c6c1-3f49-9da9-41987ee25594 | -3.0364 | -49.42562 | 2025-07-30 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b13adcf1-e786-3b70-8017-5a4c394b92e4 | -3.6912 | -42.20021 | 2025-07-30 04:00:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7542d363-949d-3f35-b90e-7265da598945 | -3.03207 | -47.86539 | 2025-07-30 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfb1019e-61fe-302f-84e9-ddaaec278183 | -2.90432 | -48.24926 | 2025-07-30 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a06de643-6164-3bfb-8b89-670677446108 | -3.99394 | -43.2302 | 2025-07-30 04:00:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 1841c373-7069-31c1-b6ed-1b26385c1ddf | -2.66518 | -47.40659 | 2025-07-30 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b164dbff-9f97-3db9-b7ac-2b513efef150 | -2.51712 | -47.71523 | 2025-07-30 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f97377ac-b4a0-3b35-98a1-944677dadb83 | -3.82562 | -41.56001 | 2025-07-30 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 199b2486-0c1d-3644-88d3-8ad5c12217a9 | -2.4469 | -47.32678 | 2025-07-30 04:00:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59c63a3c-9109-3883-9782-58e164a4943b | -2.92098 | -48.67537 | 2025-07-30 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2082c23a-5a16-339a-aa94-6c56b35dd589 | -3.03859 | -49.42746 | 2025-07-30 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a95ad92-91aa-39ac-8fb0-adcf7f90e6f5 | -3.82324 | -41.57496 | 2025-07-30 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 81829171-d646-3270-af73-253a0107aac1 | -3.51271 | -43.25625 | 2025-07-30 04:00:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73679a14-8479-33d0-ad7c-9d82c1d63081 | -3.51143 | -47.22278 | 2025-07-30 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24aa9f01-76b7-35f5-89c9-47ec66bc4bd0 | -3.4803 | -43.25766 | 2025-07-30 04:00:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fac62532-e458-35d3-90f8-c2554ce3397c | -3.27517 | -49.13985 | 2025-07-30 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 690f5d86-ab74-3ade-a0a3-709673f2afb5 | -2.44597 | -47.33244 | 2025-07-30 04:00:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3c19610-b6fa-3af7-8d05-d1f04ae25b45 | -3.82503 | -41.56374 | 2025-07-30 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0a0f8e54-1ed8-3414-bf3d-90e36c04017d | -2.80984 | -48.66255 | 2025-07-30 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 148125bf-436a-330c-b77d-5d0c255edd03 | -3.58326 | -47.51881 | 2025-07-30 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd9fb600-08eb-363d-b635-1ae79849235b | -2.92154 | -48.67195 | 2025-07-30 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d8e9c44-b785-3f71-977b-4f743883acb0 | -5.0719 | -37.71619 | 2025-07-30 04:00:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README11.md)
