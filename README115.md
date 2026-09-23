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
| 423062cb-c577-35e9-9dd8-3415d6222fd9 | -5.27979 | -60.20532 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1076af32-5d6c-3312-9e04-1b5eb5e1c256 | -6.8901 | -55.33264 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f92787eb-5bf0-36a7-9fa3-644feba7946d | -6.46155 | -59.99512 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6c75730-4178-3813-ba42-952f349deb84 | -7.32524 | -55.59826 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0cf4c91-a9ca-34d2-88dd-25efdd530719 | -6.76414 | -59.41916 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ee43507-1310-3a71-99cd-77323ca35266 | -6.58059 | -51.49187 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 274dae9a-d405-348e-a9c9-a239c5518d8e | -6.84134 | -55.27137 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bab04f64-ba15-31d0-bd26-deea7114c550 | -6.42376 | -59.97799 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12d8e6ff-fea9-3407-81b4-fcc1d5186fe1 | -6.13967 | -59.92515 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63766fb3-898a-39a4-a184-4d7ee8b9061c | -6.97123 | -59.69762 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76a5ddd8-d198-39dc-9c5c-25cb14727dd5 | -6.61708 | -59.91528 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 320c5feb-a590-3cae-9cf0-c57bc11ac8b8 | -6.62703 | -59.93839 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 760ddb66-2d48-32b0-9b9c-f198948b66db | -5.96891 | -57.78199 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f09327e-805f-3333-8931-45110f11448b | -7.11363 | -55.1289 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de339679-825f-3c9f-9e2a-5f9324a65c59 | -6.14018 | -59.94321 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5991c4af-91f4-3f99-8b83-1d9277fdfdc9 | -6.68108 | -55.07477 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9102cd8-faf9-3743-8055-6948de2b2282 | -6.45826 | -59.97305 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4970ffed-b5a8-3047-bab6-1b12b572ee57 | -5.4246 | -60.24983 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b01c21e-fc5f-31fb-b9ea-bd51399b1ee6 | -7.61057 | -57.60832 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42f80d69-1e3c-3ab5-96a5-be14178647c0 | -6.80879 | -59.39433 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faaf504e-a1f6-311c-b274-07e1af0e64aa | -6.46604 | -59.96712 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cd8683c-3ba3-3dab-8564-a899e7bc89dd | -6.31007 | -59.94555 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5fb14f1-4384-39a0-990a-2984ee363ee8 | -6.44551 | -59.96741 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 758f0db5-e3ae-326c-88a4-8a6786eea336 | -7.42398 | -49.8582 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9df71fad-8913-3812-a85b-538ff8e88bc2 | -6.85759 | -63.02472 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06098ee1-5c5d-3c7d-99b8-a35bc9433024 | -6.72924 | -59.44522 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2540408e-981c-327b-b6dc-843ed0e7da92 | -6.46267 | -59.98811 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1b336c4-1683-38ce-b32c-9342d3efd050 | -12.14459 | -61.17123 | 2026-09-23 05:25:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edf20895-c385-32e1-a1af-2591b7e3be5e | -6.17783 | -53.29004 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc0b65fb-306e-3c54-b3fc-e8425ef0c743 | -6.62317 | -59.91983 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b95cb1ac-7e07-3332-9e17-70d55adfcd43 | -6.07541 | -57.72869 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfd5b9f8-8ade-3d01-aa2b-0abff3b4aa0c | -6.00588 | -57.67765 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36917373-f2cc-3a1a-93b5-414d226de7fb | -6.29765 | -57.78501 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6420133c-78c9-352a-a9f3-bd00ec4a9396 | -8.287 | -54.77552 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa3aeb68-5604-3bb6-9032-8b62c58ad699 | -6.62149 | -59.93033 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 31a332a4-df56-3bbf-a5ec-8d8859df0cc6 | -8.10648 | -54.77314 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59ccdadb-12a8-30fb-8d59-8549c75556ca | -6.1092 | -59.88446 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79178376-84d9-3290-9d8f-e09c15e4b0f0 | -6.12907 | -59.94864 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b64fa61-4752-392e-adc3-285a98ea31ba | -5.98567 | -57.69663 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9515db79-699c-33fd-9a91-35d1c872742a | -6.6239 | -57.98153 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3de10460-e83d-32e5-90a0-a15d4e2b55f4 | -6.43626 | -55.6189 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e00d287-a1b0-3d7f-a781-0da40d6d7658 | -5.62662 | -60.2056 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27e20544-5015-3c39-9595-21b10a894bbf | -6.90704 | -59.8442 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb462e71-29f2-3246-9e2d-81a509b33dde | -6.642 | -59.93002 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33389af4-5376-3b16-85f4-b0adaead9357 | -5.84694 | -57.62351 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaf823eb-dc51-35fb-9144-1befd1ce0449 | -6.12185 | -59.95107 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abcf1a7a-2ca6-32be-a1ac-0bd1ac70d5cf | -5.14212 | -60.27897 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebd44139-c61a-3116-b22c-60743b625c2c | -6.15546 | -57.95669 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 928fc195-a52c-3f22-be31-202431d4d341 | -6.3367 | -59.94613 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d426d7c-bc0d-3a95-ac41-74bf2645a493 | -6.45199 | -54.98475 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 653e89a9-fa6f-3825-b386-c40ca184a484 | -6.67601 | -58.55638 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 498f1ed8-e593-387b-9a8b-6d64dbedacab | -13.92615 | -47.83529 | 2026-09-23 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cc13cfe-0b7f-3712-9763-d3836f757e60 | -5.26983 | -60.1599 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 559a4b85-f9be-3a3d-ab18-9a3e8c234db0 | -8.25844 | -54.77665 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ae285f6e-9f39-3de3-b92a-5926da6386c5 | -6.13291 | -59.96726 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35a83811-72c0-3046-980d-c74579a0bca8 | -6.6856 | -55.07056 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8efd22eb-ce5c-32b5-b7a0-f95f01de8eab | -5.58244 | -60.20216 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc732a97-b52f-3130-937c-404b80fc1df4 | -8.9007 | -45.9422 | 2026-09-23 05:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 071893a9-ceed-3573-afab-9984704096ea | -6.16405 | -59.94347 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60d07474-f90c-3c82-bcdc-8771facdb776 | -7.42733 | -49.83338 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0af5da3a-db9e-3873-9014-bf04030344d4 | -6.60429 | -59.95269 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff3a5a6a-f3a4-3ca1-b96f-3925c5e06b11 | -6.33111 | -59.95962 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd61c669-2500-31bc-bd2b-656734a94053 | -6.16019 | -57.72726 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f55c13f3-7b49-3bed-bc20-8dd6b121b17d | -6.45493 | -59.97252 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 294f8635-bb2d-3967-a011-c796ce4752aa | -6.66782 | -50.95039 | 2026-09-23 05:25:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be78e042-1762-32a6-b5ab-50afd4322765 | -6.77801 | -59.63088 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 787e3707-4ab1-33b7-85c8-bad95e703417 | -6.66055 | -58.56824 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3da4848f-e8f7-336b-873d-df7f39276b16 | -5.1247 | -60.27986 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b33a820-23c4-3c22-a822-56be7ccf6ce8 | -6.56567 | -55.40641 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a21699d2-e5cd-3424-8c67-48859596bf7d | -6.61482 | -59.95077 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61e54879-2181-36d1-8a6f-1a6c23438a7c | -6.86786 | -59.91983 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df509461-03da-37f1-9310-8e2a8150d70d | -6.74832 | -55.09439 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e8e5be2-daf2-3150-8703-968184ac197c | -7.04191 | -62.93506 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68a4e1f6-4905-3514-b85c-f3d78eb20c98 | -6.45582 | -54.98529 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc10d355-0231-30f7-ab5c-92c1a7e1990e | -7.43695 | -49.84492 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| cddfdb6b-2bcc-3a0b-b690-8328d6cfbc8a | -6.4542 | -54.9873 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4267db9-2ef4-3dec-8553-d696554e9717 | -6.80825 | -59.39779 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b05c6216-d540-3f70-8f26-c80a962714e9 | -7.55467 | -55.0181 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9c06737-29e5-38c1-97a6-447945483218 | -6.61541 | -59.92577 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 53da3252-f914-3732-8383-6ccf0370d6a6 | -6.11253 | -59.88498 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51697c59-9a07-36b6-a2ff-06d877c98fff | -6.69596 | -59.95332 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbb14010-b51e-300c-ba57-23a0a7b6581f | -6.44218 | -59.96688 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c7e8bd6-b80e-3ea9-9568-76a6dfd07586 | -5.43478 | -60.22949 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9540e82e-91f3-36b5-abf7-579e13fa3374 | -7.61 | -57.61201 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3558199b-56d0-3800-9442-7fe4f821fcbe | -6.38929 | -60.02285 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ad19a98-134a-3fc9-8dac-7ec8f92a8f7d | -6.73806 | -59.43243 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d40745e-0039-3eb0-879a-887644373ecd | -6.69985 | -58.92328 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26c6dc5a-f658-3469-bf12-344c8bbd4488 | -6.04024 | -57.82205 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10b7eeff-da8b-3d63-9cf1-57c5732a4057 | -8.28303 | -54.77493 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e8f439f-3645-3af2-a06f-4230406a90fd | -6.12251 | -57.75805 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d6b1999-645d-3ae6-bc1b-e935a7d70ed1 | -6.59464 | -51.32319 | 2026-09-23 05:25:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b73df7e5-75d7-32fe-8ba6-37793649eb29 | -6.73529 | -59.42844 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47861705-8bf8-357f-9eb4-57f1abeadb63 | -6.45282 | -54.9967 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9c8a68d-17ea-37ce-bb2c-82811e142fa2 | -6.73237 | -55.09669 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eedf4d53-3b69-3bb2-883a-aece370f461b | -6.10175 | -57.6703 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fd433f7e-44b4-3b6e-b7ff-db2311b2bf16 | -6.8903 | -59.22285 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c22107cd-8999-3222-b851-f7e37c72ddf9 | -6.69131 | -58.4585 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f9db881-ce98-3bfe-9eec-2c970ed73dea | -6.66822 | -50.94757 | 2026-09-23 05:25:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 118c444e-c460-31fb-ad63-8dab64f0aed0 | -6.61998 | -57.98456 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54c35fa4-4495-38fb-895e-c18c6a71217e | -8.33589 | -50.82586 | 2026-09-23 05:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README116.md)
