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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e92d8ae-489f-3936-b355-0cf9f9a1cd8c | -17.23155 | -46.95744 | 2025-08-11 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaaa8f91-9b6f-3af6-871f-1ee07dae7d4a | -22.51567 | -46.79436 | 2025-08-11 03:40:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b4e3cd0a-fd91-3d10-91e1-7d6a5b7a46c9 | -18.62558 | -46.85019 | 2025-08-11 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09d5b91a-80f6-3c0a-85fe-74fecfb9e1c8 | -17.80407 | -42.92372 | 2025-08-11 03:40:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e01c4052-ee40-39e3-8a5f-7cda586deb70 | -21.14873 | -42.9081 | 2025-08-11 03:40:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 51ae120c-a1e5-3322-817e-f65811cdadaa | -17.80837 | -42.9248 | 2025-08-11 03:40:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ccd4e86-e3bd-3dd1-9583-b3757e602304 | -22.51261 | -46.79297 | 2025-08-11 03:40:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 54b64efb-0008-3e36-911b-5a82c659ce65 | -20.60389 | -48.87498 | 2025-08-11 03:40:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cc59bf0d-0d95-3755-aaca-6b790ea552f0 | -21.18133 | -43.93192 | 2025-08-11 03:40:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 43e7ada8-6d46-3620-86bb-1fb00fa44f4c | -19.68633 | -43.84727 | 2025-08-11 03:40:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2624d09-075d-3664-b5bf-87648089d0bd | -19.55407 | -46.58562 | 2025-08-11 03:40:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebb3bae4-8461-3a85-b925-4ff0fc8e5955 | -18.79709 | -43.88018 | 2025-08-11 03:40:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab64e3ba-2e46-3ac6-8bff-cc312704120e | -19.55935 | -46.58687 | 2025-08-11 03:40:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 136d6569-0f09-3298-b7ae-d33610f8eb27 | -18.61849 | -46.85654 | 2025-08-11 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fe46b07b-38bb-3d6b-9de1-a24201fba50e | -19.21347 | -46.80751 | 2025-08-11 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85bee2a1-4042-3f05-89be-9450fb6ccb51 | -19.21425 | -46.80382 | 2025-08-11 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b630d3d-7b56-3f6a-93f2-5a2799c7d340 | -16.29509 | -47.69763 | 2025-08-11 03:40:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| baf5a765-2f0d-3132-a99e-d9eba9bebb02 | -17.92373 | -42.89166 | 2025-08-11 03:40:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17a9de5e-c5ea-3861-8b6e-d9c445c9f277 | -19.42001 | -43.36893 | 2025-08-11 03:40:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4addd150-b23d-30ea-b978-bd6288e2e5eb | -19.60663 | -42.62229 | 2025-08-11 03:40:00 | NOAA-21 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9872d27a-4193-3bfa-9a64-e5711dbf0981 | -18.63105 | -46.85141 | 2025-08-11 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f840377e-91e5-389e-a6e0-8c3294419d79 | -19.41554 | -43.36873 | 2025-08-11 03:40:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 607d63ac-8deb-3045-bce9-6d565b9169d4 | -15.63151 | -48.55167 | 2025-08-11 03:40:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0282f778-78d2-3d2b-9b8a-517b846e394e | -18.63577 | -46.85619 | 2025-08-11 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c126f8a-d913-3845-9417-3a483ecf8ed7 | -16.68576 | -47.63729 | 2025-08-11 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7bc5a8b7-42e7-334a-bf69-8e7b03f57c67 | -19.41634 | -43.36462 | 2025-08-11 03:40:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0e154feb-9897-3ea4-a9b9-db398c38d460 | -15.99254 | -47.50208 | 2025-08-11 03:40:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba79fa95-965c-3970-8e86-5ee222f28c83 | -18.01076 | -43.48326 | 2025-08-11 03:40:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb27f3de-08b2-3919-bd7f-9c7e90c54ebb | -16.40943 | -42.58683 | 2025-08-11 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f74d8bbd-287a-3837-a089-fd7b1907dc25 | -17.23069 | -46.95142 | 2025-08-11 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51296ca1-542f-3241-9542-48c916446d56 | -18.7926 | -43.87906 | 2025-08-11 03:40:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ec55518-a6e5-36b4-8e8a-c1934af8962e | -19.56007 | -46.58347 | 2025-08-11 03:40:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36beaeda-fefc-3994-b3a9-63b92e5260c3 | -18.7982 | -43.87453 | 2025-08-11 03:40:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3758f965-e2fa-3fa9-9c88-c45c9eaddc15 | -16.05061 | -48.48492 | 2025-08-11 03:40:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49d09727-42fe-305f-8967-efad5d4cc21f | -16.39469 | -42.59312 | 2025-08-11 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a7de887-97e9-3d23-963d-cc443a1459a3 | -19.21964 | -46.80506 | 2025-08-11 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 807018f8-446b-3b14-ac03-c2e705b12e3f | -18.61769 | -46.86026 | 2025-08-11 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d65b1227-96e0-3c64-b4e5-b18c8afd9e12 | -17.22699 | -46.95117 | 2025-08-11 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38f6720f-7fcc-3f78-8dfe-96ed8e1e501f | -19.71769 | -49.15154 | 2025-08-11 03:40:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f53d7571-3605-3b5e-80ac-b5ddcc493e21 | -16.30108 | -47.69908 | 2025-08-11 03:40:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cb2dc17-17a1-3e98-8b56-34eefb7fcc46 | -15.53925 | -49.99786 | 2025-08-11 03:40:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b7d4c01-9956-3ad3-9444-a589b9449b02 | -17.95813 | -44.28697 | 2025-08-11 03:40:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f82292a-0e55-37c9-9d13-845c216f4874 | -18.30135 | -43.96286 | 2025-08-11 03:40:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4865cdf-7426-38d7-9043-74785550eaab | -19.90357 | -43.87674 | 2025-08-11 03:40:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| cd9bd4bb-0b27-3efd-94c0-96c35bc0dfc1 | -18.61223 | -46.85896 | 2025-08-11 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 126f8cb9-bc5a-33a0-9792-53ae03a915ad | -22.28362 | -46.59371 | 2025-08-11 03:40:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4dda49ca-962b-39ce-9d73-422a3ae7e505 | -17.79974 | -42.92279 | 2025-08-11 03:40:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0495f78-dd97-38c5-81c1-020e5b8965c5 | -19.77134 | -42.102 | 2025-08-11 03:40:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 72e971e8-39ba-37ff-aa96-5950810a9007 | -16.29572 | -47.70052 | 2025-08-11 03:40:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc72ce76-e82e-3dd9-9a96-636b7de90723 | -16.04248 | -43.82566 | 2025-08-11 03:40:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a602adc-a869-396b-86db-a07bfa64bd11 | -19.21545 | -46.80587 | 2025-08-11 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bc9524a1-42ee-33b7-ae07-2382473b392e | -19.21885 | -46.80881 | 2025-08-11 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8aa971c7-eae9-3f41-894e-13077b89a14b | -19.21626 | -46.80214 | 2025-08-11 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0ef8bcd-4333-36c0-9d01-8b4e49ae3ed3 | -21.78264 | -44.68262 | 2025-08-11 03:40:00 | NOAA-21 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| df523fcc-398a-39bd-b478-31546e2e6f09 | -18.18071 | -47.00265 | 2025-08-11 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 115e3e0c-296f-3f4e-bd2a-d832326ba15d | -17.85637 | -44.42628 | 2025-08-11 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 930c111f-68cc-3be5-83ca-103d0f970693 | -19.08991 | -43.54548 | 2025-08-11 03:40:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac32bc05-2993-3216-8cdf-96c964a8a81d | -18.61304 | -46.85521 | 2025-08-11 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a202b4f0-bde2-378c-976d-a5d2cdfbd05c | -21.17701 | -43.93087 | 2025-08-11 03:40:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ce6cf73b-1563-38d6-86f6-9bf229d59daf | -18.46068 | -45.89977 | 2025-08-11 03:40:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52c9983e-1248-34db-86b4-2094ccc5c9db | -17.91347 | -43.91072 | 2025-08-11 03:40:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba37376c-4e4f-3543-8422-6775584fc96c | -17.2298 | -46.95566 | 2025-08-11 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5be5c7b5-3524-3040-b83d-540717a62a89 | -18.63025 | -46.85518 | 2025-08-11 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5dcaa5d8-362b-3ad3-879c-d6cb19448812 | -16.37913 | -42.53289 | 2025-08-11 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f203b6c-877b-32d7-9980-722fc316178a | -21.15281 | -42.90898 | 2025-08-11 03:40:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 241e827c-df1d-34c9-9a3f-8606e10342b8 | -24.68163 | -51.04163 | 2025-08-11 03:42:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1cb40524-d34f-36ec-b8f2-6e6b8bd8d2a5 | -24.7396 | -50.92064 | 2025-08-11 03:42:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 86955c1c-0557-3ca8-9878-51534a081af8 | -24.87135 | -52.07013 | 2025-08-11 03:42:00 | NOAA-21 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2d00d184-8a43-3494-9ed8-36194e7e8823 | -24.87144 | -52.06446 | 2025-08-11 03:42:00 | NOAA-21 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3a65f871-726e-3e77-af28-1549153c055f | -24.87294 | -52.06388 | 2025-08-11 03:42:00 | NOAA-21 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f7b0d3d1-872f-347f-b937-44eb5c691039 | -29.16187 | -51.96312 | 2025-08-11 03:45:00 | NOAA-21 | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0501815f-7457-3bfd-8fb3-eaffc5a95951 | -6.5858 | -44.541 | 2025-08-11 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 751c73ef-6c2a-34d8-a290-e227c83be54b | -15.4407 | -53.9258 | 2025-08-11 03:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 1f12ade0-e7b9-3d3f-8dd7-957f2f13347a | -5.4825 | -44.374 | 2025-08-11 03:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 3ebcbe07-d7cf-3e3f-b0b3-8881d6aeb229 | -6.5631 | -51.1126 | 2025-08-11 03:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| ba7ff369-4438-3bd8-9f63-df3e1af04604 | -6.5856 | -44.564 | 2025-08-11 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 6e0ea6ca-cb7a-35f5-8140-4847b28e6793 | -5.5011 | -44.3956 | 2025-08-11 03:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| a158dc62-a164-3fd4-bf46-8335491040f1 | -5.5013 | -44.3726 | 2025-08-11 03:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ff7d8411-c00a-3630-aad8-5a937916d638 | -7.0613 | -59.2165 | 2025-08-11 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0cb6fdb9-fb28-3ed6-8e42-4dda20f6bb0e | -5.4824 | -44.3969 | 2025-08-11 03:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 305.5 |
| 00bfa66d-9d1d-3966-9379-e6fcb1e6ae46 | -7.0614 | -59.1972 | 2025-08-11 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 58ba1454-32a7-3d3d-a94d-182d347aeb91 | -15.4212 | -53.9283 | 2025-08-11 03:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b00649d1-6e54-3e8f-83f8-b30241bf3087 | -7.0799 | -59.1964 | 2025-08-11 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ca689c4a-d393-3518-badf-17d68844a7b7 | -7.0799 | -59.1964 | 2025-08-11 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b77a2af2-9984-3ccb-a814-bb69004e9dbe | -5.4825 | -44.374 | 2025-08-11 04:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| cb740652-a12e-37e4-bb6f-c810c91bf199 | -5.5013 | -44.3726 | 2025-08-11 04:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 180aeedc-772f-3596-8528-3f65da01c733 | -5.5011 | -44.3956 | 2025-08-11 04:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2ffd7427-51d1-3251-91e9-de296e5d4ced | -15.4212 | -53.9283 | 2025-08-11 04:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 1c4536eb-c8f3-3cdc-a2b3-a9a75c306ef6 | -6.5856 | -44.564 | 2025-08-11 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8aa3329d-c23c-3ded-87d1-d7352570f256 | -15.4403 | -53.9468 | 2025-08-11 04:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ef5c2512-dca1-327c-80d5-c462f148f573 | -8.5604 | -54.6973 | 2025-08-11 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 706210ee-de63-3438-8f51-4730d8d1dbcf | -15.4407 | -53.9258 | 2025-08-11 04:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 406b2cac-1e5d-36db-b16a-87453326c352 | -5.4824 | -44.3969 | 2025-08-11 04:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 80caffc0-dc15-338d-9d0b-2a64b8006a43 | -7.0614 | -59.1972 | 2025-08-11 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 09228e08-96a9-35af-b1ff-89d0f6629520 | -6.57805 | -44.57665 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e258fb06-0a38-3b1c-bb00-a2d197cf4f3c | -2.33143 | -48.62094 | 2025-08-11 04:02:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7a79785-59ba-3969-8e0f-d06d9e980aa1 | -4.06115 | -46.93377 | 2025-08-11 04:02:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42d2b48e-926f-3b03-ac87-ea719804fc72 | -7.13328 | -44.21188 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51ad8afa-20a8-3c7b-93be-09e2c0a250b3 | -3.50963 | -50.74401 | 2025-08-11 04:02:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8880be4-1ead-306a-bdcf-be9738f4fda5 | -6.57581 | -44.56579 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |


[Clique aqui para ver as próximas entradas](README10.md)
