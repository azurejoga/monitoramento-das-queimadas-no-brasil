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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb54a126-cfbc-317f-84ed-94e8e4e20344 | -20.84983 | -54.98212 | 2025-09-08 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 431419d3-7827-3071-b60f-443773c6e4be | -18.16109 | -50.67234 | 2025-09-08 04:55:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99d8bccc-86d7-321f-b682-49379ec678c8 | -16.29843 | -58.0953 | 2025-09-08 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 44bf9038-7350-30d6-bb25-7773dcdfc8c5 | -19.52318 | -47.88179 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 475ec026-c6b2-3f34-9ae6-1257a158afd5 | -18.03046 | -47.10124 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 57a21fa5-381b-3417-8b9e-4be46a5d8040 | -16.30839 | -58.1231 | 2025-09-08 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 08b72f71-be7b-3136-b1d6-fc8fd8863919 | -17.58122 | -49.79339 | 2025-09-08 04:55:00 | NOAA-21 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4496d726-a233-30b0-83c6-f3bd0214da8d | -20.96223 | -48.45733 | 2025-09-08 04:55:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b7072d58-fd19-3951-a2cf-7c810d2849f6 | -19.63641 | -46.57929 | 2025-09-08 04:55:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9edfcd40-2f18-39e2-a58a-83dd008b0174 | -20.46829 | -43.96265 | 2025-09-08 04:55:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 2b4d5d71-1b63-3d9f-8ca7-f5c7ced0187d | -19.45489 | -47.88377 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 66d4463b-2222-35c4-aa21-40cfcd3a60cb | -18.95829 | -46.79533 | 2025-09-08 04:55:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddd693a2-1f1d-3445-9cdc-4ef884cf5116 | -19.59461 | -43.69406 | 2025-09-08 04:55:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66f27cf9-0209-3236-a030-0047d9e81902 | -19.06721 | -49.74018 | 2025-09-08 04:55:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27bab87a-a070-3a6d-b78f-e6f73254ff09 | -19.07142 | -49.74081 | 2025-09-08 04:55:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4daa02f-1e4a-3c21-9e23-1e4423dc58fa | -18.15969 | -50.68309 | 2025-09-08 04:55:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e66047da-a3cf-307b-ba42-cefbe0cdd5c4 | -19.21345 | -43.73549 | 2025-09-08 04:55:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| acefab2d-d46a-394b-b856-81352bf11e5e | -18.4326 | -48.78657 | 2025-09-08 04:55:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7cde094e-b724-34f2-a523-0cc5ad827cd3 | -22.69063 | -46.92879 | 2025-09-08 04:55:00 | NOAA-21 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e0ca7ee9-5539-3b60-a786-8198bc777e78 | -20.96042 | -48.45535 | 2025-09-08 04:55:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 82669455-4c4f-3fd7-885b-477fb8fa5536 | -17.58849 | -49.80227 | 2025-09-08 04:55:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 062f479b-8958-3b0e-be13-264cbfcbd826 | -18.34718 | -51.95763 | 2025-09-08 04:55:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 079ccd3b-ed1f-3487-8523-7ff879171cbb | -19.69676 | -49.28564 | 2025-09-08 04:55:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b416e7a9-3fbb-3bcc-948e-8e3fb1c5f11c | -18.02909 | -47.11373 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7c51c683-7e8d-3b5e-bd76-02a55b7b7544 | -22.69097 | -46.92533 | 2025-09-08 04:55:00 | NOAA-21 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 0d22bfb8-baed-3647-b74e-002d19efe756 | -18.99401 | -46.65773 | 2025-09-08 04:55:00 | NOAA-21 | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c630f063-a2a5-3665-acbe-4109f51e2232 | -19.2072 | -43.735 | 2025-09-08 04:55:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 72d877b0-0c65-3ff9-ac83-3152bc239b29 | -18.10032 | -45.1657 | 2025-09-08 04:55:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bee88c6a-fb8b-3876-bfa4-dbc426882ffa | -19.21161 | -43.7378 | 2025-09-08 04:55:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d96436a8-21ad-3a61-8eb1-15ceb0d9cacd | -18.02491 | -47.106 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8143b1b8-b715-3800-99b4-1da2546bfdf2 | -19.1882 | -42.0794 | 2025-09-08 04:55:00 | NOAA-21 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| a3b001ed-527d-368f-aa5e-7673e4dadf48 | -19.52256 | -47.88717 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 048f978a-5760-3964-b93b-b6650352c493 | -16.29059 | -58.11974 | 2025-09-08 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 468afa02-a9ce-3ca8-ad73-d1bd3c7d2541 | -18.09847 | -45.16485 | 2025-09-08 04:55:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fabf49a-200f-31cf-b3bb-ed363a6bade1 | -20.95751 | -48.45678 | 2025-09-08 04:55:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6b7c08f4-aebc-334c-a5db-601fb74e6169 | -18.09506 | -45.16151 | 2025-09-08 04:55:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41fc4049-af06-37cc-8d07-3fa8e1a55a91 | -17.58485 | -49.79783 | 2025-09-08 04:55:00 | NOAA-21 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9751c253-4fb8-3ec7-a9b1-cd02b08c4b60 | -18.35744 | -43.92658 | 2025-09-08 04:55:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdfa4f1f-b815-336f-94c6-e310251515cf | -18.03747 | -47.08309 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24ddd027-4b80-38b3-9885-5660cee16d8e | -19.52741 | -47.88818 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 205a06ea-1a20-356b-a041-683618baba40 | -19.3551 | -44.52119 | 2025-09-08 04:55:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aecabb31-7f81-3f19-a531-76835e833279 | -18.02343 | -47.11958 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 06caecdb-f5ea-350c-aac2-e5fb444d9d3f | -18.02979 | -47.10735 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| afc28c42-573a-386c-9bc8-058b6ab85a30 | -19.88568 | -44.11272 | 2025-09-08 04:55:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a95be918-2384-305d-a2ec-4f915343634a | -20.85317 | -54.98273 | 2025-09-08 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da4cc4f2-7392-35f7-a11e-24cd9c5de306 | -18.24126 | -46.62102 | 2025-09-08 04:55:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ca9647f-fc39-310f-96b3-8ee8d9366db8 | -20.85374 | -54.97892 | 2025-09-08 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a725be49-1342-3664-9726-e99a52b9af96 | -20.92884 | -45.26699 | 2025-09-08 04:55:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3395a7ba-969e-3920-8253-1caf801431ab | -18.42816 | -48.78589 | 2025-09-08 04:55:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| afa856bb-29ad-3558-9cee-91221a66365c | -20.60171 | -47.84319 | 2025-09-08 04:55:00 | NOAA-21 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 26690746-4820-3c91-9b9c-87785fcac523 | -23.18032 | -47.24713 | 2025-09-08 04:55:00 | NOAA-21 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 30273031-4016-3be5-9369-323772a99ec6 | -18.99437 | -46.65452 | 2025-09-08 04:55:00 | NOAA-21 | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30340a27-62b2-3e34-b090-3168998e5a34 | -18.02374 | -47.10548 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 534cc2e9-de7c-35bb-84b8-b873645aa6c1 | -19.21206 | -43.73269 | 2025-09-08 04:55:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 07312965-f818-366b-a4c9-982a6a6cea26 | -17.63901 | -52.57831 | 2025-09-08 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4024423-54ad-30b6-bfb9-140cad4ae54a | -20.92308 | -45.26619 | 2025-09-08 04:55:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6fc230c4-2796-32a1-a84d-673e9b644d7e | -19.7615 | -48.01263 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c9a32cc-7c63-3571-91ae-f499809f716b | -18.34351 | -51.9571 | 2025-09-08 04:55:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e95e399-b781-3954-84f8-73171c1ceb51 | -22.56553 | -54.92053 | 2025-09-08 04:55:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a207080-bbdd-3d82-9ea6-b24151592eaf | -19.73024 | -47.89812 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 221317a6-26ab-34b1-968e-8212a00720e0 | -17.58438 | -49.80167 | 2025-09-08 04:55:00 | NOAA-21 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77bbba23-3ac8-308d-868e-7b2dcd08b9fa | -18.35132 | -43.92614 | 2025-09-08 04:55:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0fa0a9ac-de95-384b-abd3-29ac2f6f0d26 | -16.3091 | -58.1189 | 2025-09-08 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ad27f28d-5709-326d-a50e-f922d79b7174 | -23.17999 | -47.25055 | 2025-09-08 04:55:00 | NOAA-21 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3559384d-8bdb-3e59-b753-e4d12be3a0ee | -20.72694 | -49.45861 | 2025-09-08 04:55:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 567edb23-e4f2-3c1a-8ad0-e45a35a70ced | -19.53214 | -47.88846 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 81c876fa-3e42-3e9d-9ecd-112671615736 | -18.16039 | -50.67767 | 2025-09-08 04:55:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 738474c7-d64f-3dff-b8dd-893fc7671bc7 | -18.35685 | -43.92603 | 2025-09-08 04:55:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afc76737-2c5c-3533-a2f6-2c5712f4239a | -19.64166 | -46.57974 | 2025-09-08 04:55:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4396ecd7-ffa1-3255-aeb0-60689a64f89f | -19.5232 | -47.88213 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b10981d-b74c-39ea-bc13-149fd1746681 | -19.21394 | -43.73027 | 2025-09-08 04:55:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de1396be-d901-3a48-bc82-3c895a3edd19 | -19.53221 | -47.88884 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 591745e7-307b-3086-b486-295545f88003 | -18.34655 | -51.96218 | 2025-09-08 04:55:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ded8f7e-99c2-3062-8b60-7977906ee09b | -18.43202 | -48.79135 | 2025-09-08 04:55:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f981e330-777d-369d-9f80-9b9c1aa0af86 | -17.4436 | -50.22614 | 2025-09-08 04:55:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb01b9ef-7483-3620-9b50-8cf38df6992d | -19.35839 | -44.52249 | 2025-09-08 04:55:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d098d986-9ff8-3f18-a2c8-a1aa361be98c | -19.60134 | -43.68956 | 2025-09-08 04:55:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 575905e3-f02f-3254-87a3-cb05128a2255 | -22.46761 | -52.10908 | 2025-09-08 04:55:00 | NOAA-21 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 8f0f701b-022a-30b0-a33f-ce2aad749397 | -18.04169 | -47.09051 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b320ba97-cf9f-3e80-b482-ab484df3d40f | -19.528 | -47.88276 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f7eadeb-b9c1-3efe-8019-138b7c44dc0e | -7.3983 | -61.6346 | 2025-09-08 05:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| e9a431f2-e263-3bf7-b486-dffa38161310 | -12.6343 | -56.9725 | 2025-09-08 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 555309bc-ecbc-3006-a667-0070a04470bd | -12.6153 | -56.9742 | 2025-09-08 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 38500f37-efca-3e16-84fa-8eaace06b1dc | -7.3983 | -61.6346 | 2025-09-08 05:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 21731d00-55c9-3d6a-8137-31c0f4190129 | -5.21785 | -43.69767 | 2025-09-08 05:10:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 2e1cfc75-8dc0-3b48-82b8-732c2c5b2915 | -5.22125 | -43.69087 | 2025-09-08 05:10:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 195a3f16-76f3-3462-88aa-6fc03a803ab9 | -7.76166 | -34.89809 | 2025-09-08 05:10:00 | AQUA_M-M | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1e98d434-6fcc-36e3-82a1-8d2f3e316726 | -5.8534 | -43.83895 | 2025-09-08 05:10:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| b416b77c-f6d7-3e64-8d1c-b6b9c3161f3f | -5.87865 | -43.96762 | 2025-09-08 05:10:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 701ac6ee-cb7e-3ea3-bfd2-74d693c1f95b | -5.85281 | -43.84355 | 2025-09-08 05:10:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a711623f-305b-3bd0-af67-60ec8349fbfa | -7.98467 | -44.82465 | 2025-09-08 05:12:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| cde7f8aa-870b-3f89-bf5c-e6e3e5c6ba6d | -10.14447 | -46.22268 | 2025-09-08 05:12:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 4d6ea99a-affd-3f51-a593-d2620ecc0959 | -10.15102 | -46.1855 | 2025-09-08 05:12:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 8885da84-97c2-300d-a828-a2883b6ffd02 | -7.9778 | -44.8306 | 2025-09-08 05:12:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 4552a25c-84f4-3558-97f4-0cd02dccaa90 | -10.1378 | -46.19107 | 2025-09-08 05:12:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| eed06a8e-4566-3dfb-9d55-85c63b6ebab9 | -10.15446 | -46.19354 | 2025-09-08 05:12:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| dd61e268-61d1-3980-9bb6-fa41fcef182d | -10.14761 | -46.23101 | 2025-09-08 05:12:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 929526b8-c25f-31b1-a345-9817e7eb4b46 | -20.59926 | -47.83279 | 2025-09-08 05:14:00 | AQUA_M-M | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 136.4 |
| b0ec5e7f-4177-3e00-9ec0-27cdeeada28b | -19.18895 | -42.0751 | 2025-09-08 05:14:00 | AQUA_M-M | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 81d8c9e5-1df7-3fed-958e-d59801fdbd13 | -16.91469 | -45.80569 | 2025-09-08 05:14:00 | AQUA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |


[Clique aqui para ver as próximas entradas](README76.md)
