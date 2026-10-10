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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b02e3129-5803-326d-ae75-b16da9bd42ee | -1.278 | -55.75402 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e02f2d8a-90d8-350e-bfa0-0a0ab7d3697e | -3.86971 | -55.8417 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9be594e6-1890-3f80-84a8-cf87d5a6e51b | -7.49952 | -54.99881 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ada1c1f5-f76d-30fb-b7dc-123f820dc260 | -5.71217 | -53.47542 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b5224c3-4558-38c0-af24-c4f48290db30 | -2.508 | -56.14771 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51e11b49-5511-3a1e-8ea0-9263f3d39663 | -6.00437 | -53.4962 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ac81075-5e99-3d44-9f37-afd7f6cb11c4 | -3.03725 | -54.2345 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6485d692-d40e-389e-9868-d795035650f1 | -3.06105 | -59.26814 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 482957a5-2d6d-37d3-b845-4024dacbd6e5 | -3.02148 | -54.0764 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11a49f74-26fd-37d6-adf2-9a472a24d9bd | -3.57522 | -54.6978 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c388ef7-874d-3708-b966-c064b88d8435 | -2.74431 | -54.11023 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62634eb5-fe62-319e-b7ed-aa845f467fde | -3.254 | -54.04565 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80d8cf49-c941-39a1-9dd6-e9196579f4bb | -6.96432 | -44.96107 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a1d2dd6a-1a60-311b-be4e-462ebe8a5da6 | -2.97734 | -54.07654 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0013492-613a-342b-ac65-f0edd94330d8 | -1.92539 | -57.04217 | 2026-10-10 05:04:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e6f189fb-1534-3022-8962-8de59a3f1580 | -6.74944 | -55.07771 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aeacb61-3f7e-3008-b52d-705500b57c8d | -2.83717 | -54.12521 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b7a4554-e30e-3090-b123-79b0e034ee90 | -2.74486 | -54.10677 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06dba4dd-2606-38b3-8a2d-9e62bbdd42a1 | -6.43964 | -55.03926 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65aa84cb-3c9d-3b54-ab80-6eb8671cae4b | -6.01765 | -53.47672 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba026277-35a5-3485-9254-a005840e7bdf | -3.92805 | -56.02856 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce9ac442-9fb6-3c58-94c1-1ee907c4096f | -3.11292 | -53.78013 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 743b4ea2-d3ea-32d0-b1e9-34989b3c0579 | -3.53461 | -54.73811 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 30afb6ac-0048-3c82-b791-e0042c6bd8b7 | -2.47052 | -56.0859 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7481a5d-f911-375c-a423-25082b8e8022 | -5.94827 | -55.34902 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d313b426-1c9e-3ed9-80c0-bc0b00af1eb5 | -3.93091 | -56.03293 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c2decf6-9f35-3822-aa06-a9e3cd8b9265 | -7.22432 | -55.14721 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a41fd19e-1e30-378c-8339-d31989e5ece6 | -3.04899 | -54.03124 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea5d5927-3f0f-30d7-b911-583a93eff31a | -3.01216 | -51.01793 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f8ec09f-8f82-3cf9-94cd-76d8489008c6 | -6.48639 | -55.95254 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 833be85a-41c7-31c3-94d3-15e1db5406c6 | -2.50189 | -56.20753 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ffbd71c-c803-322f-913d-c2d182bf7cae | -3.20562 | -57.86606 | 2026-10-10 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69adc42b-7b61-3fe0-9a7b-6a409f043a20 | -5.69277 | -53.46888 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31e2bc93-141f-3e92-9c92-506a9a7ffe9c | -2.61118 | -51.70548 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a690a083-6063-39cc-a0c8-5d2c45eb7732 | -3.25258 | -54.67605 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 061846fc-f327-3667-a475-eafeafcab6bc | -3.1118 | -54.19307 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa844e5-e373-3c2d-a2a4-18152ef28cfc | -3.00973 | -54.79281 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba9ce895-1d6b-3ccf-9dc5-1a901b260053 | 0.24364 | -60.38229 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e133592-5fb8-3577-8625-7e1943221484 | -8.26133 | -46.41672 | 2026-10-10 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f81d4c26-dc95-389c-94e1-ad395f62da09 | -6.12574 | -55.70576 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 458c5c14-0cc2-388b-b1e5-0b177971dad6 | -3.84679 | -55.78917 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 866131b8-ad11-31e7-83f1-7060b1c14f7a | -2.74813 | -54.04356 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e67bb199-b4f4-3d67-b231-cfc6239f0fd0 | -6.20216 | -53.14464 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04542326-5cc8-3cb0-9903-4b1361ca3b5e | -7.55118 | -48.02232 | 2026-10-10 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b99befc1-4c59-3f38-83ef-25f3b8d62f13 | -3.51805 | -54.64923 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58fbfd74-3774-3320-ba6f-932e86dcb4f0 | -3.31404 | -53.84039 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13e096ee-7303-3cc3-b988-d420f1ca8693 | -3.17843 | -50.596 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc1f289f-8399-311c-a735-2103ae1865d7 | -6.08478 | -55.70283 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d634126-e5a1-36b0-b214-65ffe21476da | -6.31824 | -55.33193 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcaf420b-051e-3aa0-a853-55a78561b44a | -4.40134 | -43.12171 | 2026-10-10 05:04:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2e0afaa-f27e-37d3-a304-b3ccf5ad5799 | -1.88616 | -54.67487 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 00d710c3-d59d-3f1f-a1f0-5b19f423c620 | -3.71979 | -55.46724 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edcba8d3-3b4b-37a3-ada9-f45b07816f2d | -3.27983 | -50.39487 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf0e135b-300c-3bdb-898e-0c96ec4ecb3f | -3.30167 | -54.06765 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 245333f2-dc6c-3d35-8de9-652e4087e263 | -2.89426 | -56.67192 | 2026-10-10 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85e715f0-14b8-33aa-9c8a-6a15c3682cb4 | -3.13494 | -54.3672 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f31ab5d1-f883-399b-accf-31f421301470 | -6.61774 | -59.9435 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89505150-a4aa-3fb9-9be0-0f86ff419c3a | -6.20862 | -45.42786 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3159b6aa-e53a-35c9-8935-7115f7f87d6d | -1.64469 | -54.40137 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a4cdbc55-e956-3cad-b920-3918d33d5da9 | -3.35194 | -50.41306 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea12eb60-fc32-382c-bb41-d9550d0efcef | -3.36262 | -50.48756 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de618872-41bb-3025-adbc-ebbe836338d5 | -2.74542 | -54.12458 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39689af1-1fd4-3806-a444-5d57fe6ae3e2 | -4.16858 | -54.3427 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1babd09b-eb2a-3d00-a891-f27d2dbc7edd | -8.18416 | -46.35044 | 2026-10-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb05f159-39f3-3b4b-a522-bc30460a1a73 | -6.48636 | -53.60737 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e1393ab-91ed-3dc9-bb4a-34003c6d80bc | -6.48463 | -55.96341 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41c06ff6-2522-333e-b859-3147394e46d0 | -5.19276 | -60.3045 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6d9143c-abf2-367e-891c-04ef78c3c8a0 | -5.99279 | -55.37067 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6c1a968-4130-3084-9af6-585529a6b56d | -6.5793 | -53.01619 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cdcdab5-5ef2-30af-8792-abf04adbef5b | -7.02113 | -47.66169 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0eb48c59-48f4-3fd3-9daa-c5c4f7051958 | -6.99807 | -47.72502 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a931a5fc-6b89-38d1-8457-166a780d8339 | -3.20633 | -53.85477 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60556e4c-8a10-3d39-a729-a06d7e46b6b9 | -5.69387 | -53.46187 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa805575-25fe-3749-bab2-4ed732d07f38 | -3.55244 | -54.69059 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7b646ce-6793-39e5-a24f-97e8d03d0570 | -2.51346 | -56.27049 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44e9de00-3f89-3811-a62f-734cd8bbdbf1 | -3.06098 | -54.17086 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e4ef0f6-0c6b-3e94-9398-df7c6e4c7f51 | -7.22792 | -44.16645 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcbf0812-9c53-3da1-b30b-bbb62102c23f | -3.50297 | -53.44027 | 2026-10-10 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e260586a-8e24-3a08-8ed7-eaeeaab8f4a2 | -3.59079 | -54.59983 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7090f0f8-8f6b-3de7-8d75-1e2ceae73617 | -3.87071 | -55.9883 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ecf17785-2d29-3e9f-ab9e-1d1ae6d6a2c5 | -3.88131 | -51.42787 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e16d7ba1-4295-3765-94e4-82f77eb6eff1 | -3.98677 | -54.45972 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed132e8c-b7a0-32d1-81aa-459c54368344 | -0.97126 | -52.45531 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15fc8e31-b220-3a42-b529-cc9a4015801b | -3.09813 | -53.7639 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c270c663-03a8-3c52-b035-5be327fd198a | -3.00453 | -51.02073 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b432b54-b5d9-36fd-8666-d562963c4f12 | -5.07146 | -60.22031 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec8920b9-9f5c-39b9-af5b-16721a34d7ea | -3.31127 | -53.70567 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81613e09-92ce-3de7-9fe7-c854c3c70123 | -5.83902 | -44.92785 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e71bd477-a569-32b7-afa3-944528324036 | -2.72506 | -52.45049 | 2026-10-10 05:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce6b5e49-23f4-375c-b3f6-d6a160de2700 | -3.26531 | -50.39262 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fa73111-7751-3191-a701-8f78df1ac774 | -3.24425 | -54.66391 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ec84db9-add1-3601-8ef0-630621962d46 | -3.13162 | -54.36666 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57a41a04-42ab-31f0-a6c3-8af10164a57a | -4.11769 | -50.97953 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26bd00db-28e2-3944-b463-5562fd7a02e8 | -3.16428 | -54.71947 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 787b223b-8ffc-3076-bdbb-2301439d2ae8 | -3.29908 | -54.67966 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28d80e83-7fab-3904-bbf4-f5b2652fac9b | -2.89216 | -59.21722 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03dde05c-f807-39c4-9c4a-01630a4a3995 | -2.97345 | -54.78348 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cf02114-1f29-39d3-9e01-4044c64598f3 | -7.57348 | -45.6581 | 2026-10-10 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e170cb05-545c-3227-a0ac-fc5066a50112 | -3.12725 | -54.18131 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 19c5023d-35ca-3a76-8ec1-5281bf242e46 | -4.05547 | -50.9636 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README106.md)
