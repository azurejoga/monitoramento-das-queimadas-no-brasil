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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77179262-62ae-397f-a1c4-026d13767fa8 | -17.11464 | -56.38513 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0b408789-4bc3-32fb-87df-a41a205890cf | -17.10913 | -56.39349 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3c1be934-e87a-3354-aad3-8de88a869e2c | -17.10472 | -56.39289 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6720744a-04f8-3326-aa96-29606484595d | -17.10139 | -56.38333 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a4aa38a4-bad7-30a9-864a-fb9282b6d5b4 | -17.10084 | -56.38783 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 78228c05-ec51-3f19-81ff-192c4850c3a5 | -17.1003 | -56.39229 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ac9645fc-d5f4-3765-bd59-bbe7c0acbd04 | -17.08604 | -56.21005 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3ea63c17-419e-3185-b04b-9b30a3d08ec8 | -17.08045 | -56.37323 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bfc963d0-0528-39fe-8324-488de50a323b | -17.07987 | -56.37773 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7d5160c6-3340-3c59-a9ef-cb09116ee7c6 | -17.07985 | -56.37576 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d06d0c2d-a17d-3ad9-abd9-f06d9e365d92 | -17.07931 | -56.38026 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 48fa0365-d4fc-384a-a9fa-473a6dc96a03 | -17.0793 | -56.38221 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1477ddd2-a6e3-3b6a-9a96-bdfb8c317abd | -17.05385 | -56.40594 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 371eab2f-0dd6-331f-9c48-b7fff8ad207a | -17.04945 | -56.40534 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e7e0840f-3ef8-32cc-a279-575b418b64d4 | -16.97692 | -56.20015 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 64d716ee-ca4e-322e-8806-f709594f6c28 | -16.97635 | -56.20473 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| aad75f66-f0bb-31a8-a499-d88cb73d1b5f | -16.97304 | -56.19494 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 01d4dd85-6d07-36f9-9c06-835485c070c1 | -16.97246 | -56.19954 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1fc212aa-99b0-335b-9734-fbaa75981283 | -16.96858 | -56.19431 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fe90321f-9b90-3074-863f-821b92482f3c | -11.91783 | -55.9161 | 2024-09-30 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a7f2ac6c-0f03-3314-886e-2051306bf73c | -11.91359 | -55.91555 | 2024-09-30 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e6a30c51-0216-38fd-b814-036cc362d2b6 | -13.03975 | -57.30282 | 2024-09-30 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39e19b56-b82c-3213-851b-10e59bebf16e | -13.75344 | -56.47956 | 2024-09-30 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1233de8e-f1b6-3c42-8b57-14dcf4c64f82 | -12.77888 | -56.9936 | 2024-09-30 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 753559fc-bbe0-346b-8873-d08b42fbc0fa | -12.7749 | -56.99297 | 2024-09-30 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a4002ef-939b-3925-8de7-3cf392faf37b | -12.6171 | -56.48354 | 2024-09-30 05:25:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aca27df2-2576-375a-85db-7ca61bf5696e | -12.6135 | -56.47921 | 2024-09-30 05:25:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5eaad0b9-3318-3eb5-8635-6b03b45bfebd | -12.61298 | -56.48297 | 2024-09-30 05:25:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a1da9d74-93d8-3762-928a-c9a261a44ffa | -12.61246 | -56.48672 | 2024-09-30 05:25:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 045ab9a5-ba9b-3dd1-a532-1ab56e357210 | -12.58324 | -56.97902 | 2024-09-30 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6195135a-7d22-3e3c-aa54-7016e5f1e195 | -12.58276 | -56.98256 | 2024-09-30 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d4fcd2b-62b2-3684-a91b-bd1e6fb59de6 | -12.57925 | -56.97846 | 2024-09-30 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 237c687b-9a0c-3154-9189-1771d3206cc1 | -12.49831 | -55.74001 | 2024-09-30 05:25:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7296ca9c-5f5d-3ef2-938a-f07c9e78b243 | -16.48382 | -57.38642 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 44e44172-6e2e-390b-be92-d654da93ba49 | -16.48332 | -57.39021 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a3c691c7-f6df-33ae-a177-9715405dc112 | -16.48193 | -57.43241 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 61af5f5f-7318-3fdb-837c-11cf158b2dab | -16.47972 | -57.38583 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2f937f0b-265e-3d3a-b495-8b18f8613759 | -16.47923 | -57.38963 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 131e4bf7-007e-3251-a8eb-43ec80e82fae | -16.47873 | -57.3934 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 34dd0162-0cc5-372b-b233-358d24d2e8c8 | -16.47784 | -57.43184 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b49cba20-8eae-3c1d-88bc-f5185f8e64d0 | -16.47735 | -57.43563 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 317dae91-0e64-333f-9100-7a015e99333f | -16.47562 | -57.38525 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 63dc2738-50b5-3e94-8551-5358207078af | -16.47513 | -57.38905 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 93a57b92-c800-3ff8-a807-4e270bd26f78 | -16.47326 | -57.43504 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a8c595c1-405b-30a1-9ed1-7ad652888851 | -16.47152 | -57.38467 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 993f89d4-c795-3e97-a77b-a73bf5aa9b11 | -16.46756 | -57.41495 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 19886d5f-817f-331c-bc58-186058b01621 | -16.46545 | -57.39922 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d0edc345-f704-3ced-9fed-4f1ee6b9814b | -16.46397 | -57.41058 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 37a9ed52-24e6-3332-aef4-cdb605f2ef30 | -16.46347 | -57.41436 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6896ce4e-02ea-379f-91a2-80f961e29c2a | -15.94545 | -57.1898 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 69c8842c-7aa6-3e28-84bc-ffe2cb9b28ae | -15.94493 | -57.19378 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6339d261-18c6-33b8-b618-8ebcc30e047e | -15.94079 | -57.19337 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1f9e1a1e-ce0a-31ea-b939-d081c265ae7b | -15.93195 | -57.1969 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f66f22c-0416-3006-94fc-65522b7dc6e2 | -15.92527 | -57.18359 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c5950bc-3ee2-3008-bb24-04013d98ad60 | -15.92169 | -57.17876 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7d67c718-2e2c-3c01-89e1-5b59d71cbc64 | -15.92111 | -57.18332 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b0e9fc84-0d48-3e18-8846-f02d41e038fa | -15.91715 | -57.21413 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c628b64-4b03-385e-8564-f3db3a5125f5 | -15.91695 | -57.18309 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1941c9ee-758a-3d75-8797-bfdf6cbe5751 | -15.91394 | -57.20652 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 509961ae-8c00-30fa-a8a6-c538cd7f5b84 | -15.9135 | -57.20996 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f885904c-84a8-3488-83f3-f0129396d5f9 | -15.91304 | -57.21351 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8e6a51b-1cd0-39d4-bf85-e80dce663ecd | -15.91279 | -57.18285 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2a151456-de8b-3d5f-83c2-46b89b72e8fe | -15.90984 | -57.20584 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 050c9f00-c52f-3e77-8a42-f1137fa1c16a | -15.90939 | -57.20937 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32ee538d-8179-3663-8480-0586c33618aa | -15.90892 | -57.21299 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81d2d2b0-e9bc-387d-843b-da87c2212212 | -15.90812 | -57.18657 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c78612ea-b048-372a-a14e-b6d655ff3368 | -15.90575 | -57.20506 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d01436af-7ba8-3667-9ac7-a48df949ae0a | -15.90528 | -57.20873 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a773c0c-ac20-310c-8c65-a019f6ae3850 | -15.90351 | -57.18981 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e029dcc-a1f1-3ba8-8af5-403a2a2f23f8 | -15.90302 | -57.19365 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 14b03c80-2e05-3d3b-a9b0-49988f6f3ee5 | -15.90255 | -57.19735 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6cd3147e-b34f-360d-8739-79bc261667d5 | -15.9021 | -57.20085 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 619096f1-e3b1-3e5a-a0f1-97e515a20ddd | -15.90164 | -57.20443 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b91d97ab-813c-335b-be90-1f63460ddb5c | -15.89892 | -57.19296 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c00d3da9-2270-3fdf-acea-e3dbc03fe5ce | -15.89845 | -57.19661 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e463d67-b293-39e0-bc67-a9d0b5c15ff2 | -15.89799 | -57.2002 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9dd17538-db27-3ea1-83f4-13268b1da359 | -15.89522 | -57.19753 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a6132869-7242-31ca-b39b-33c4153f592d | -15.89435 | -57.19593 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 877c4406-df87-30c6-b2ce-cc9cb8cd34f9 | -15.89388 | -57.1996 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| eb331607-87ad-3df8-b316-03bee1c214fd | -15.8916 | -57.19323 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7332b608-f06b-335b-9061-88bcaeea9c33 | -15.89111 | -57.19691 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 29e7dd5f-af18-3e07-b3f6-8fc483f47bd0 | -15.89071 | -57.1916 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b46fdfb1-ea22-377f-be2c-643344f6d9aa | -15.89023 | -57.19528 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d90ff438-a479-3286-b138-d2df9c440b44 | -15.57516 | -56.91848 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b45a609-efd7-3409-9b07-9d86ca1f3344 | -15.57095 | -56.91825 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7668cc4e-f0e9-3b5e-a8e6-779294fc7d48 | -15.56787 | -56.90928 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b2758a20-1f57-3f9c-b6cc-d9e9c3a6fd8c | -15.56731 | -56.9136 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c94553d-3394-3e25-98b7-6e9d2079876b | -15.56366 | -56.909 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ada93a5f-d1d3-3e1e-af09-6a6ade5f942c | -15.56308 | -56.91349 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 378df5ae-b9af-3b1b-bd1a-fe6b63923c65 | -15.55942 | -56.90896 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 836d6b94-e9c1-3b2a-b8f6-4c9450613735 | -15.55517 | -56.90899 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fe40f8fa-b726-3af8-bd64-09000422b699 | -15.54729 | -56.90419 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4902926a-8b0a-3919-b9b0-4a6bcc50f6e1 | -15.54624 | -56.91236 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 52bd5379-bddc-33f1-a64f-39de671b2aac | -15.5431 | -56.90379 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2aed28c4-972d-37cf-ab53-f0289e7259b6 | -15.54257 | -56.90787 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 413b74ce-02fb-3c05-a59d-59a379e20dc7 | -15.54206 | -56.9118 | 2024-09-30 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb9d1586-75a5-3ee8-bc49-f7bf78179d9b | -16.60932 | -57.34841 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 199c650f-30eb-3100-9ffa-98f4cb507046 | -16.59697 | -57.34665 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5daed519-64d8-3f66-b7fa-7b7047788979 | -16.52096 | -57.35134 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6a49d982-2ed9-33c1-9513-85fbd835d3c7 | -16.52048 | -57.35516 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |


[Clique aqui para ver as próximas entradas](README67.md)
