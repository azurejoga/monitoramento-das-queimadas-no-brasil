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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a1fb967-2db7-30f9-a7cd-426d192112e0 | -21.55626 | -46.97387 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00f096f4-ed6a-3d20-bec1-e5c8d540ddc2 | -21.55178 | -46.98065 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68b5b40c-b2dc-39b7-af97-61bf3486d2f9 | -21.57491 | -46.98486 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 90f5e68c-934c-39ad-b88b-192d9b0704db | -21.57432 | -46.98856 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 93df3c0a-fe8b-337f-bb4f-7e2eb301f9fc | -21.5722 | -46.98055 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4bf7ee88-3967-31c6-8c10-05745c10bb33 | -21.5683 | -46.98365 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6114bb2a-771f-3977-b57d-d373e586ed21 | -21.56169 | -46.98245 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| f4475fbf-6702-3bcc-91b2-05441983eb8d | -21.56015 | -46.97078 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88af022d-354b-3d3c-9112-234d539f28d3 | -21.11695 | -47.23022 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63080645-61b1-3b72-a2db-8629aaba0a21 | -21.11635 | -47.23394 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b37fadb-2a11-3a86-8954-42d5d2eaffc1 | -21.11424 | -47.22588 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3b2f30f-a696-38fd-bc81-1d2ff466e381 | -21.11365 | -47.22958 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25acbd5a-8fb1-3a7b-b196-44a29e7ebd4c | -21.11304 | -47.2333 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0a29506-d1b4-3848-9adf-cb414c5f9b74 | -21.11244 | -47.23704 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a532d91-a288-3a51-8ccd-e74c3a1cd810 | -21.11184 | -47.24077 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da32dce6-7c1b-3afe-aac8-65a8126b18b3 | -21.11093 | -47.22525 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d2e204f-99a2-3fae-94de-d3eb2b5d7a0a | -21.11034 | -47.22894 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 520aa511-e6f9-3459-b219-cdc25e81598a | -21.10974 | -47.23266 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 965f3b63-2f3a-3576-aabb-d9697f14f192 | -21.10914 | -47.2364 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92c56d05-2a16-3df4-b849-fe4565c2cfd5 | -21.10853 | -47.24014 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd143377-944a-353f-a40d-ac6c3af47079 | -21.10763 | -47.22461 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 969da4f2-292e-367b-b422-3fb1e18257d4 | -21.10704 | -47.22828 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7905749e-91eb-3272-95b5-3d1b1bb40e24 | -21.10644 | -47.23201 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3ddd802-771b-36ca-8a53-e09f70cf5950 | -21.10583 | -47.23576 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76ee0ed4-341e-359a-b6bc-119f1bdb9cde | -21.10522 | -47.23951 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e6507ec-34ba-3e65-a2fc-8bd59f506b94 | -21.10432 | -47.22399 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d301ade-7c20-3dae-bc29-dc163cf76345 | -21.10373 | -47.22765 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b401c153-355b-319a-9cfa-59a15fa9f2da | -21.10313 | -47.23137 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8fcdda8-f9ff-326a-8d40-37b3fe0b8422 | -21.10252 | -47.23513 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d003b804-f20d-3aa8-befa-c0f9c9779dd5 | -21.101 | -47.2234 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47d4accf-38c7-3b8f-bdde-44fc26579dc3 | -21.10041 | -47.22705 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1ba6c6b-e7bb-327b-89d8-43b69a73b81b | -21.09921 | -47.23452 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 231a1c88-ebb1-3f8c-aa87-c14e9c2deb9e | -21.0986 | -47.23829 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0e01ef3-8fa9-3244-b917-00de87e97fad | -21.09769 | -47.22281 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 730fd105-b69a-3567-b3ac-0a0799d4afe7 | -21.0971 | -47.22646 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 623a290c-1e62-362a-a45d-3aaff4f11338 | -21.09651 | -47.23015 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7803286d-94a3-3ad4-a6fb-15a2ee2b49ae | -21.09379 | -47.22585 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1ebafdec-8817-3172-8ae9-cf95c3d3fd8c | -21.09319 | -47.22955 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8b20e3e0-7e56-3a0b-a519-914557cb0a94 | -21.09048 | -47.22523 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb2c76ea-fabe-392e-b926-1cc6442f5fe8 | -21.08988 | -47.22894 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7ba88b2-4856-38a9-9319-eb3a22754f02 | -21.08534 | -47.57368 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 530b606e-4d2e-3db7-b6cd-e6fc55a800b4 | -21.08262 | -47.56936 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3e43b68-cc65-3af9-ab84-77ca2ca1bb9c | -21.08201 | -47.57309 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d910bc07-47df-32bb-b0df-5c1ccf8fa8f1 | -21.0814 | -47.57683 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 098a049d-8ddc-3754-b48e-794e6f8ce2d1 | -21.07868 | -47.57249 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40e6e679-3b92-3ec6-ae9d-1baa595c7462 | -21.07807 | -47.57623 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e5866ac-c460-3dca-b491-a7fa3a9addfb | -21.05646 | -47.2458 | 2024-10-09 04:17:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1454fee-28fa-3b3b-9de4-b5d1f336be39 | -21.05585 | -47.24953 | 2024-10-09 04:17:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a828a590-da95-315d-9e3b-1968739892d5 | -21.05254 | -47.24891 | 2024-10-09 04:17:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b06e694-e531-37ad-9562-a4be1a4f8fbc | -21.03237 | -47.58303 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3d774a4-3613-3a8f-b105-c39567b59ba9 | -21.02965 | -47.57869 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8076e68c-e46c-366d-bcb8-d3ba9b98c1a5 | -21.02904 | -47.58241 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d8a7135-c341-316a-b210-c356ff57f8c2 | -21.02632 | -47.57806 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67684678-d327-3185-b1a5-5d062d2f304e | -21.02571 | -47.58178 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 146bdf06-d6d0-35b1-ae3a-544241516f2e | -21.02238 | -47.58115 | 2024-10-09 04:17:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a8fadce-fccf-3084-a522-649abb2a0926 | -21.86479 | -48.39914 | 2024-10-09 04:17:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af7a46af-eb91-37ba-85a3-5b9b388f8ae9 | -21.86414 | -48.403 | 2024-10-09 04:17:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d0e094a-c420-3e9c-8d30-caaa7f917201 | -21.85999 | -48.38626 | 2024-10-09 04:17:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71c1e92e-24aa-3270-b566-1c1983f32dc1 | -21.80066 | -48.35958 | 2024-10-09 04:17:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a59986b-2698-3c28-9605-8253bd217740 | -21.79729 | -48.35894 | 2024-10-09 04:17:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e990ef4-f20b-3181-afb8-01a89caeb4e3 | -21.60902 | -48.28384 | 2024-10-09 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bc3eec2-b677-3759-b84e-8a9948109026 | -21.60566 | -48.28319 | 2024-10-09 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37198b03-8cbc-3bd6-8001-03fb9d6d963c | -21.62296 | -47.70278 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea21bf82-8ad1-331c-bff3-961ef1f3a8ce | -21.62174 | -47.71032 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 16395c15-6076-389b-957e-a942afc677ae | -21.62112 | -47.71411 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 358cbae5-21ec-32c2-8560-15b75f6f3e2e | -21.61989 | -47.72168 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87060d3b-7f32-3e28-bcfd-d6a84f0a9380 | -21.61779 | -47.71348 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0230f144-0b36-3cc9-ba71-0a157727e36e | -21.61718 | -47.71727 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3dd94867-d07f-3868-b139-95fcf64f03e3 | -21.61662 | -47.67846 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8fad187-a250-312e-8491-228b13e65cbe | -21.61656 | -47.72106 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 13968e3b-33e6-32aa-a56f-30df1c382be0 | -21.61595 | -47.72483 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4667ca00-70db-33ed-afbd-a6d1ffea3432 | -21.61391 | -47.67408 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b07b9bf6-b539-3b7c-b3ae-1c57c34dcf7d | -21.61385 | -47.71664 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0a05ab61-1b38-3b81-90cd-3e7c4bda9479 | -21.6133 | -47.67784 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1beec7cf-417b-312d-9a6d-41b47f490945 | -21.61323 | -47.72044 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f4cd60af-58ed-31ae-8c11-f5293e7c75eb | -21.61262 | -47.72421 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1ac7bb37-9fbf-3afc-abb7-bc42b19b4e76 | -21.61058 | -47.67346 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| aeb3dda0-73cd-3628-ae28-6c204ec0ca68 | -21.60997 | -47.67722 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fa538104-e221-36f2-bfe2-7e83f999f66b | -21.6099 | -47.71981 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c82f1292-d33a-3fde-a6bd-138e8d5aa1a2 | -21.60875 | -47.6847 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 213ba9af-8f4f-30dd-8199-7d778f8a7fe8 | -21.60814 | -47.68844 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| def42e32-0b5f-3eaf-9026-6f3c28a4cbf1 | -21.60754 | -47.69218 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9a31bba-2e9e-3975-92e0-5f128ad8936d | -21.60719 | -47.71541 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43103883-d076-3c40-8980-c59558f15d98 | -21.60693 | -47.69593 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 159cb8a6-e439-3f3e-97ab-c2ebc819d193 | -21.60664 | -47.67659 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f03fe4eb-2660-35a3-b6cb-eb13e5b275ff | -21.60658 | -47.71918 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87042456-1e92-306d-8864-e6420db4ca02 | -21.60632 | -47.69969 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6f9a171-5083-331c-a422-88e3295818a3 | -21.60603 | -47.68034 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe165a65-511b-3993-9ac9-01085aa369ad | -21.6057 | -47.70346 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6418269a-4997-3760-984f-eac7fee95d83 | -21.60542 | -47.68408 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af962bc6-a3ee-30d6-b9e8-103709a5faf6 | -21.60509 | -47.70724 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a51d5ba7-11f6-3f7f-9232-c747f403ccba | -21.60447 | -47.71102 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 638b484b-20dd-33b1-9f0f-832754c9be9e | -21.6036 | -47.69531 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e136fd3-faa4-36bb-bba9-a461cc80de2e | -21.60332 | -47.67597 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c16bb578-6460-3aa9-a06d-8236472382f0 | -21.60271 | -47.67972 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f030a362-78b2-3870-ada6-b9cbff34a4bd | -21.60237 | -47.70283 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c92ecfe6-7d9b-311e-a7fc-ccb45f4e3b9e | -21.60176 | -47.7066 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9787e03c-b808-33eb-b18d-01ef1b2f6c46 | -21.60088 | -47.69096 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e171810-a0f4-382f-aff5-2cc89d9951c7 | -21.60027 | -47.69471 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c29aec1f-7777-333b-b962-2cbfc1dfa124 | -21.59843 | -47.70596 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README92.md)
