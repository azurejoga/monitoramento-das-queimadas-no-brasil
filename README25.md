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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ce0eb23-5af5-334a-9d91-8a903477a5dc | -0.06592 | -51.30082 | 2024-10-17 04:10:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7153fd7-b36a-3098-8b46-bc81d63baaa4 | -2.12322 | -50.80266 | 2024-10-17 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8b6ff83-6852-3648-a921-1e3019942320 | -2.21377 | -51.95937 | 2024-10-17 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1aaaafbe-4926-3412-9b65-4036a6971742 | -2.20819 | -51.95846 | 2024-10-17 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1219c87-c6a9-3f9e-9da4-8dbdc24fb1d6 | -2.00375 | -52.10779 | 2024-10-17 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 638c6e03-4f98-34c1-be75-5b32a61a9424 | -2.00312 | -52.11169 | 2024-10-17 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5061861-9b5c-329e-915a-f8a6036dd456 | -1.9981 | -52.10684 | 2024-10-17 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ad2b1cb-9104-3a16-baf0-93312f85f7f9 | -1.71132 | -52.70292 | 2024-10-17 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f82bbc0-9936-3c5f-8ce8-cf79c6560426 | -1.70959 | -52.70185 | 2024-10-17 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 92b9ba4d-fee6-3a8b-b222-aa7709a31563 | -1.70611 | -52.69764 | 2024-10-17 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f928f208-000d-38ab-bf8e-20f21919bab1 | -1.70542 | -52.70193 | 2024-10-17 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b130fe6-7f36-3c81-b5ea-f44f5634fafb | -2.08848 | -53.40622 | 2024-10-17 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6bc1da4-a97b-3bed-855e-04f3e2a6c5b8 | -2.08769 | -53.41095 | 2024-10-17 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d37f71eb-25df-3440-8e6e-c57b9a69645c | -1.13556 | -54.17493 | 2024-10-17 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8656a1f2-c088-3f90-8c94-e16449da89db | -1.13554 | -54.17039 | 2024-10-17 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4b4488b-aca1-38a8-aa56-ee45e55a7a16 | -1.13462 | -54.17586 | 2024-10-17 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f89f4a08-94b1-36ba-914c-3ed80c8bf1e2 | -1.11605 | -53.71363 | 2024-10-17 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 643aed24-31c9-3532-ac25-b0aa581e59d2 | -3.0291 | -39.85627 | 2024-10-17 04:10:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f6cf1aa0-ac65-3264-ae20-2db6b0ea149f | -3.90495 | -40.44839 | 2024-10-17 04:10:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bb1c96f0-1e8a-3470-b6a0-a8e615908d7f | -3.7458 | -40.50491 | 2024-10-17 04:10:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 07eb039a-70df-3b22-9fca-d95befc80c04 | -2.77995 | -42.27209 | 2024-10-17 04:10:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 339b1b7e-9bcb-3376-9ff9-31a6840a7046 | -3.92934 | -42.41719 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b910608f-eb6a-3e0d-a9f4-5d8f1dc60ace | -3.9288 | -42.42063 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 26a860de-636a-3764-92e8-623e20ea6e4d | -3.92826 | -42.42407 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 85275e85-2bf3-3b68-9957-953fa949a768 | -3.92772 | -42.42751 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 456d1d0d-41fb-372b-bb62-48f400d649e9 | -3.92657 | -42.41325 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a49b22d-b723-33fc-8d15-67fce2ddf616 | -3.92603 | -42.41668 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e01f9948-df99-3486-ab41-5ac2b6fda0e2 | -3.92549 | -42.42012 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 47efd9f4-ad1b-3905-8ff3-a2d49c74e513 | -3.92496 | -42.42356 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8c0084de-2a0f-3d46-9741-47a8dca5eb18 | -3.92442 | -42.42699 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 96bc2b06-ffd1-36e1-a7cd-868cafb0ae83 | -3.92327 | -42.41273 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 5fa715b2-758c-363c-981e-8f54d1823517 | -3.92273 | -42.41617 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 8c9be58e-63ed-372c-a237-71d22feeddd6 | -3.92219 | -42.41961 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| b776fe71-d168-32d5-8d67-397929a16849 | -3.92165 | -42.42304 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b24dd5d-e839-3573-aac0-4dd5b9baf01e | -3.91997 | -42.41222 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 41fd96eb-96ab-3704-9940-9916338daef9 | -3.91943 | -42.41566 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 4a4b56e5-a9a6-3250-a94b-dd87100e975e | -3.91889 | -42.41909 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 1d6bc6ad-c4f6-3bfa-a853-2f2925e9bf50 | -3.91835 | -42.42253 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 00760277-5ba4-3454-89f1-d48361df2f5f | -3.91578 | -42.41498 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4335869f-5985-39ee-8255-726cdbf4bc06 | -3.91524 | -42.41842 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c557d038-1f03-35df-b3b1-e41d49c3ce1b | -3.9147 | -42.42186 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cfe4140e-87f2-3bb9-8305-f001a37a03e0 | -3.91416 | -42.42529 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c836c58e-3f45-3ac0-ba9a-5589f1ff406b | -3.91248 | -42.41447 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dd087ed3-6bfb-3050-8c78-bf36b92e5f1a | -3.91194 | -42.4179 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ede8517b-67e1-3b8a-a472-2939081a59c4 | -3.9114 | -42.42134 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8dd2f7c1-25b8-3338-a7a9-d2377a856456 | -3.91086 | -42.42478 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 854fc7a4-3683-3aa6-a1d4-f1a15b80cdb5 | -3.90918 | -42.41396 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ae50b9b-e9a7-326d-90c7-42f09346e5a2 | -3.90864 | -42.41739 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7bec71c8-8f16-3cd1-b7bd-3c1d9961b94f | -3.90587 | -42.41344 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2864c25e-3ec6-37c0-bc16-e6b4ec666b13 | -3.93042 | -42.41032 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 273de775-6bce-32fc-9e27-c919f43ad7aa | -3.92711 | -42.40981 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3bad2b81-ee1e-3002-82ce-a5a066e1ed4c | -3.92705 | -42.38867 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 033fc6de-d108-36b2-aa7c-5f1c3025ebfe | -3.92651 | -42.39211 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 749f7346-6159-30c8-9338-3af0e4213f92 | -3.92543 | -42.39898 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b42cab87-88e9-36ca-b412-1ca9a69d9b0a | -3.92489 | -42.40242 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 439ac83c-da54-3d51-8ffa-24ae87eb2d74 | -3.92435 | -42.40585 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b39bb46b-6eca-3d28-b83e-4766111ee339 | -3.92381 | -42.40929 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 6133b04c-353d-3ef4-8029-4f94debfdf40 | -3.92374 | -42.38815 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9473759c-e56d-36bf-ac64-066c09d11079 | -3.9232 | -42.39159 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9e83889-1845-3aed-8207-630013db4eb3 | -3.92266 | -42.39503 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d4026b1-37ae-3569-9713-a25b8753741d | -3.92213 | -42.39847 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 145b28dc-ac51-3c7b-aee2-c42a51a45bfd | -3.92159 | -42.40191 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 68798bd7-0851-3781-af7b-b76c2df2b6cb | -3.92105 | -42.40534 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1c538b20-1399-36a1-a166-ea14d3f696b9 | -3.92051 | -42.40878 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 459de732-93a4-36e9-92f1-61d104ae3e3b | -3.9201 | -42.38749 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1881195-ac2c-3de3-9777-65b5518ce2e0 | -3.91956 | -42.39092 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d5246988-323f-3f13-a64a-c3c2d7f822d1 | -3.91902 | -42.39436 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6a5a7edc-fb5e-3e5c-9a40-9c8a995a5a0b | -3.91848 | -42.3978 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 878f8031-7969-32c2-9536-d369f042ea38 | -3.91794 | -42.40123 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| 5083779d-3c6b-3ae9-b25c-a8eb01fb4419 | -3.9174 | -42.40467 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| afeebddb-0a9c-3e04-94f0-921f27696ddb | -3.91686 | -42.40811 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| dc8b9cbd-6c73-3ef9-a317-6753b1ea31fb | -3.9168 | -42.38697 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1f292f1-92b5-335a-a2b7-a9c1aecbddb6 | -3.91632 | -42.41154 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| e3374334-12ad-3bc4-9a27-12d81ee13551 | -3.91626 | -42.39041 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 398525e6-3347-3db9-9614-1b3c2c40aeae | -3.91572 | -42.39385 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b54d989f-8d79-3388-acb0-b203c2b055d9 | -3.91518 | -42.39728 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5a6a6029-02c3-3f66-ada1-6c854e3715a6 | -3.91464 | -42.40072 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| c8f90c01-f598-3b6e-ba16-51d0a21ad7a7 | -3.9141 | -42.40416 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| 6244f1dd-5ec6-37e7-b6e4-d0c85a61bf11 | -3.91356 | -42.40759 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 719907ce-036d-3494-8f34-380e21f85682 | -3.91302 | -42.41103 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 379ad0aa-189b-390b-9fb7-144e77058b6f | -3.91296 | -42.3899 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 41306d70-1b0f-3030-893a-9be4b4edcad2 | -3.91242 | -42.39333 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34286f45-76f1-3409-8ea9-6edf1be26ecb | -3.91188 | -42.39677 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 917b8628-c764-3e16-bbda-5e7e1bf2b75d | -3.91134 | -42.40021 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| b1c21642-566c-3958-8ee7-53e5891b4061 | -3.9108 | -42.40364 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| f61ca020-0c0e-3f68-ba6a-dc5d637a15e1 | -3.91026 | -42.40708 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 30018b14-1947-3ee8-8356-f29615a1df54 | -3.90972 | -42.41051 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fba2dd52-23e4-3829-a0f9-564ae3b39edd | -3.90911 | -42.39282 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8afa6ffc-7c6b-3716-a102-32dec1edf6e3 | -3.90857 | -42.39626 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 45871c60-38be-36e9-a6b7-5e67105944ab | -3.90803 | -42.39969 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 49f13f8a-5bfe-3d4b-93e4-185fe3ede804 | -3.90749 | -42.40313 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 59a14df9-6831-339c-845e-b24a059acb53 | -3.90695 | -42.40657 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 153a90ed-f95b-3938-9e67-e0b1b1c05fda | -3.90641 | -42.41 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 233fb545-f7a7-3a24-9973-e6626eba937a | -3.90635 | -42.38887 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9ce138ab-ebc8-326c-b689-fbd8b7d4940c | -3.90581 | -42.3923 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86621744-33ed-3917-9112-18e9955b39d5 | -3.90527 | -42.39574 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0aab6340-c6ac-3b09-8a11-75be00017b1e | -3.90473 | -42.39918 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5ba7f5aa-1e2c-3ac1-b48e-60923f691229 | -3.90419 | -42.40262 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b6b01c5f-de2d-358c-a1f6-e96a2d5bc078 | -3.90365 | -42.40605 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6eefc53-bd55-3096-b8c0-c946b5c4cf6a | -3.90311 | -42.40949 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README26.md)
