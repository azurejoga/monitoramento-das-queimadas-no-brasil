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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51a27a34-f251-39c3-8c0e-872667733c27 | -10.09759 | -48.132 | 2025-06-12 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e4ae05ad-99f7-3b3c-b453-7f6a336d44b9 | -10.69915 | -49.5077 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98412ffd-c539-3244-8c06-db0b3aabdd07 | -11.74896 | -54.71809 | 2025-06-12 04:29:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9daa56b-3a85-3ce9-b334-217b38269d97 | -10.87449 | -54.74858 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a654cdd3-1914-39dc-8725-f0ac589fcaab | -15.37883 | -47.88604 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bc799be-9354-3217-bb75-75ecf0c32fcb | -10.3632 | -57.23534 | 2025-06-12 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0254549-196c-38e9-b13b-a24032e14f6f | -12.43045 | -54.87019 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7a96952-2bad-3a1c-8261-919999c04da3 | -13.29033 | -57.08729 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 673ded4d-ab68-308d-8fb3-eb1e78d5df57 | -10.75585 | -54.78252 | 2025-06-12 04:29:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 911e346a-81ce-3f71-9e29-b9e9d3306cf1 | -15.92605 | -43.98346 | 2025-06-12 04:29:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b111c367-cdce-3881-aa8f-cb34fe07ce74 | -12.21082 | -49.62506 | 2025-06-12 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23f21a0e-abe5-3cd3-a069-92ce70e22741 | -13.47034 | -56.85898 | 2025-06-12 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2156f666-61cd-36e7-a801-7238ef5f9da8 | -13.29423 | -57.09518 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27f4d9df-67dd-35b5-a986-83a98a8b786b | -12.4654 | -58.47261 | 2025-06-12 04:29:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41a8d9b2-0e5f-31b1-9414-1016c352614c | -14.18055 | -45.48984 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 771b10b9-7a63-3c2d-a8f1-b6f9de81acf3 | -14.1729 | -45.49277 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d9d3e01-9f63-3a19-a755-676e1572e8e6 | -14.18468 | -45.48635 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a00b3f22-93ad-3353-958a-53d80e9f3cd5 | -13.29563 | -57.09392 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b007460-ea53-3258-bc97-676d3f8832da | -13.33081 | -40.30392 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 29c1b7e1-1a68-3a86-ad74-0dad1a6ccd98 | -13.5259 | -47.86257 | 2025-06-12 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a4cc22d-d90a-333b-9819-46deafb15297 | -11.14652 | -48.15011 | 2025-06-12 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a41af73-2f22-35bb-a978-d47eede2f132 | -11.78947 | -54.77353 | 2025-06-12 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7257079e-378a-3f7a-b77e-a08f8960d8f1 | -15.56911 | -47.85448 | 2025-06-12 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed3bbb02-cb48-318c-a78f-ff84daccc60c | -13.28836 | -57.07479 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8ab5e84-172f-3235-a838-325fcacc2723 | -14.84456 | -48.31643 | 2025-06-12 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75a52614-4a9a-3c02-9cd0-2b77c30a612c | -12.05605 | -48.07234 | 2025-06-12 04:29:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3715b038-2cb7-396c-97c8-6f407f218d88 | -14.17642 | -45.49332 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 317bea17-452a-3279-b86f-1442d8f307b6 | -13.88771 | -54.65552 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cf07a3be-a3a2-39fd-8648-d56243934540 | -13.29627 | -57.09056 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1ed04ef1-24b2-3f5e-8bf9-b29d9c2a97c7 | -11.57396 | -51.30806 | 2025-06-12 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6d41106-ebc0-35cc-95b7-d1117340dd6e | -13.90557 | -48.73647 | 2025-06-12 04:29:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28be1e95-e204-3b89-bf89-2c525bd7ec5d | -12.7828 | -48.72739 | 2025-06-12 04:29:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53d42409-deaf-36c3-9d02-670adaba3383 | -12.38656 | -45.76891 | 2025-06-12 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e339de89-3238-368d-98e9-b943298919b0 | -12.82693 | -47.38173 | 2025-06-12 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ea2c3e8-28eb-3e89-a017-73b8993c0352 | -16.12366 | -47.85175 | 2025-06-12 04:29:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75437134-e458-3328-82dd-6646fc097c72 | -11.57474 | -51.30355 | 2025-06-12 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88afa69c-53d8-3ee2-b008-d5172d08fdaa | -11.99736 | -57.21452 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 76b66f08-cef5-3808-99a7-ef1d8cc26c56 | -14.18761 | -45.49094 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90095c30-2aba-370e-9639-25b53c63f27f | -11.56649 | -51.30671 | 2025-06-12 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3faae0dc-0fd6-3130-9ebb-b713c6191f7c | -12.51505 | -57.23827 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 147f4e10-277a-3308-be1b-051107c8daf6 | -13.08952 | -52.28978 | 2025-06-12 04:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cc93b32-9e60-3ed9-ba28-cb88eb057ea4 | -11.77398 | -54.3752 | 2025-06-12 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91cb1b1c-78bd-3859-9423-e307d1cc0262 | -15.38327 | -47.87942 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d38120f3-d1e2-33c7-b44a-39de9589ae03 | -13.88855 | -54.65106 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 781ea548-359a-3843-a29e-3f0ae69fb326 | -16.37623 | -46.8738 | 2025-06-12 04:29:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc2ce554-bf64-3c10-bf70-75e622645874 | -14.65809 | -48.06601 | 2025-06-12 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2447990d-8dbf-3aa0-93f0-1fa5869e3ccf | -13.28903 | -57.06637 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 739d7f20-2e82-386b-a170-11efbcfb7d84 | -14.18408 | -45.49039 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f813b1f-4755-3e41-ab03-a6cdfb72ada0 | -10.30024 | -57.13968 | 2025-06-12 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f15abcf8-8ad7-3640-8a2c-1caaa7a2648a | -11.76863 | -54.37888 | 2025-06-12 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fabccd13-f992-35fd-9b32-7cb234dc33ab | -11.79099 | -54.77703 | 2025-06-12 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 058c62cd-9991-37ae-9b94-b6ee4b275da0 | -12.1063 | -48.87521 | 2025-06-12 04:29:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dc00af0-a3c0-3159-87ec-3c52da884388 | -13.89216 | -54.65627 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5a03c43a-8d70-3d8f-90b5-d91af3980901 | -14.03786 | -55.13456 | 2025-06-12 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aae16cf6-0c55-3e53-bbf6-49d9c1f0f724 | -13.71618 | -58.68134 | 2025-06-12 04:29:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38e5b716-70c1-39de-9b35-c9f8ccaaa91f | -12.23109 | -44.16397 | 2025-06-12 04:29:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9987619e-eda6-36b4-b4ac-759e59b7bb49 | -11.37812 | -55.11162 | 2025-06-12 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b46c386b-f64c-3525-878a-d752a4a57189 | -10.76058 | -54.78337 | 2025-06-12 04:29:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4312fced-5d99-33a4-b8fe-f952d8739979 | -13.65982 | -53.94281 | 2025-06-12 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b044ba1c-aa84-38dd-bf1e-86415c8207dd | -13.29104 | -57.08932 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e07349f3-43d1-3d09-ba9f-c6cadac440e4 | -11.57129 | -47.43633 | 2025-06-12 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f51ba0ef-1a38-3abe-ae9d-b7a8f36918f8 | -12.70433 | -58.03156 | 2025-06-12 04:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dac4e9ac-dbf1-3c9e-804c-92493a492efa | -12.04119 | -54.68677 | 2025-06-12 04:29:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6574a577-71ca-3925-b59f-69bcb11d90b7 | -10.99799 | -50.76215 | 2025-06-12 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5e56be3-1fd4-3ee0-9a11-c71fb7c2fe45 | -11.77627 | -47.401 | 2025-06-12 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4669a490-0c5b-3896-8fc3-2a77b17bd433 | -11.56945 | -51.31191 | 2025-06-12 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f6ac97e-e92c-3ffe-9a48-e59cf2e9feea | -13.89106 | -54.6376 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 927cc49b-f03b-32b8-9db7-a11bcaf2ddc4 | -11.99191 | -57.21352 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5829574e-62ea-3157-85b5-18406e3357dc | -11.57739 | -47.44093 | 2025-06-12 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ab02ed81-b662-3df5-b6b0-c37a4ebce76c | -15.37994 | -47.87888 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4aee156c-e4cc-3586-a846-c4d20084113f | -14.17583 | -45.49735 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfc8a65c-8345-3cad-8058-1fcbb43648a2 | -13.53367 | -47.85658 | 2025-06-12 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e71a7677-a333-3965-a671-28055a93eaed | -14.17409 | -45.48471 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85be3bce-3d80-3919-8720-755942e556f7 | -15.72218 | -43.49316 | 2025-06-12 04:29:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 465caf79-a6d9-3115-9826-00db2dd5f505 | -12.47323 | -58.47257 | 2025-06-12 04:29:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cad4360-87e1-3653-a91a-b444943902bd | -17.10719 | -50.07095 | 2025-06-12 04:29:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ed576ca-78c0-3f90-8765-b6d10273ca88 | -10.86327 | -54.32061 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5481eb2f-bb36-38f5-877c-3d67521c7a50 | -11.99402 | -57.20278 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ae8f74f-506f-3883-92a3-eb1f897b87fb | -13.65663 | -53.94332 | 2025-06-12 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ef12f7b-6484-35d2-9c14-0e74cc84b456 | -13.89022 | -54.6421 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 202f5dbe-4294-3a11-94a5-0f569eea1cb7 | -12.76776 | -44.40646 | 2025-06-12 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e65cddf4-ed68-36e0-9370-760214e3bd75 | -10.36684 | -57.23029 | 2025-06-12 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 179faad3-ee0a-3f12-9080-9ea422ba1d0c | -15.36994 | -47.87724 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7287f1c-9f99-34c4-9678-1895a1b16f78 | -11.57462 | -47.43687 | 2025-06-12 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 56e37e46-8df2-3b32-a4d7-aef4418a805a | -10.8078 | -55.87204 | 2025-06-12 04:29:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4122e9e0-dc16-36c8-a7c2-0224be54fbba | -16.32903 | -48.87671 | 2025-06-12 04:29:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6baf4076-cfda-3fe6-af11-bf0501759348 | -11.00311 | -50.7542 | 2025-06-12 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c54a559-019d-3a8f-88ad-fe9b6b99245e | -10.36677 | -57.50525 | 2025-06-12 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e3b1e7c-8b42-3c59-a5bb-5301e10f04ba | -15.36715 | -47.89514 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1ad7a41-da48-33cc-9a55-92dfb504ec6e | -16.26641 | -48.80293 | 2025-06-12 04:29:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85324377-2d79-3e77-88f9-aaf3ff809847 | -14.16937 | -45.49222 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc744ff0-5cbc-3ebe-afcc-62a2936911f1 | -16.69396 | -49.06788 | 2025-06-12 04:29:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6499e5d1-b51a-320e-bf0d-1bf4b70189e3 | -12.4712 | -58.47393 | 2025-06-12 04:29:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d1ee220-7610-35fc-ab7b-cd0b123177ea | -15.36938 | -47.88082 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4461b2d5-0bf2-3b69-ae32-929c9b4057cd | -13.29232 | -57.08265 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7f7b49d1-c717-3c6b-9510-b7d49e7a739f | -14.18348 | -45.49442 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3478825f-0a02-33ba-a1df-2abc9b370b71 | -12.05492 | -48.07941 | 2025-06-12 04:29:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2296f583-82bc-32bf-b33c-dd342527d31c | -12.23331 | -44.16673 | 2025-06-12 04:29:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4af3c3e9-4bdc-3f17-8f2d-fb1e868b44fc | -13.29231 | -57.07734 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9454ab4-e5b4-3a34-a605-21262f851340 | -16.78733 | -49.11685 | 2025-06-12 04:29:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
