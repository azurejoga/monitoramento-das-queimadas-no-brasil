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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b89f6daf-f342-3f1a-9aac-b21348158060 | -6.48924 | -42.22306 | 2026-07-09 03:47:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| bb5e2e51-f19f-3877-adac-0f56f23cb5eb | -7.70873 | -45.17496 | 2026-07-09 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e368fe34-cce1-3fc0-bf0c-146bb777aeef | -4.83516 | -45.34688 | 2026-07-09 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9930da64-3725-32a3-a07e-0789de878fba | -12.84737 | -44.35624 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3ddf55f-c18b-311c-8f23-9d6e3125787e | -12.75431 | -44.52922 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bcb71793-39a9-3369-9046-3ac8e3791b35 | -12.35399 | -47.42669 | 2026-07-09 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5a55a6d-0fa3-3b09-9c42-7588bcdf44f1 | -4.83414 | -45.34634 | 2026-07-09 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e839d091-fbdb-3cd2-a5e4-19054fd36214 | -11.45379 | -47.5953 | 2026-07-09 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a56382d8-ec06-3aa3-bd4e-2b2071d81bec | -13.31337 | -43.71439 | 2026-07-09 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8858b7ad-673b-379d-b33a-08dc3c31285b | -13.75475 | -46.29918 | 2026-07-09 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9fcbb3f-5e58-3049-994d-ab79578a1bbe | -12.84316 | -44.35155 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e223bd9-7b8e-30d8-8b76-cf883f55598a | -10.85188 | -45.04225 | 2026-07-09 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3906aeb5-38cc-3cbc-8c9b-a2e88081f8c6 | -12.92934 | -49.48649 | 2026-07-09 03:47:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 06dce41c-b9f0-3a59-8db2-7366222ee9a3 | -13.76635 | -46.30167 | 2026-07-09 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7eeb7042-4b4a-3f42-bd51-da59256cdf13 | -13.76581 | -46.27511 | 2026-07-09 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbabb976-c205-35bc-92e6-c674934c6c4f | -12.35453 | -47.42132 | 2026-07-09 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93ab6d16-784d-3987-bc20-1b14556fcb68 | -12.84776 | -44.35588 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd67e53b-4fb7-34b9-a289-938aa39e39a7 | -10.86567 | -47.59701 | 2026-07-09 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3fa2edf-cd91-3b91-b754-92c39f640ec1 | -7.72645 | -44.56251 | 2026-07-09 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f749cb61-42d0-3d61-9f57-15dce68b2294 | -7.28805 | -46.25414 | 2026-07-09 03:47:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 398e0d68-9d76-304c-a715-6911baeae3ca | -13.76649 | -46.30571 | 2026-07-09 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cc9a682-ec45-3880-8c8b-fa847c5ee74b | -12.8428 | -44.35192 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 094d7121-e992-3d91-99fa-7476d483a484 | -12.35347 | -47.42656 | 2026-07-09 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 790aa740-1656-3e34-9284-135439bf6570 | -5.91767 | -43.86008 | 2026-07-09 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71d587c3-cf9e-3d27-b09c-dbce18359a9e | -12.84838 | -44.35262 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6832a2f1-49d1-3191-aa01-aa526877cc07 | -12.75366 | -44.53255 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6427f54f-9c37-3eb5-a83f-ed972a2cee02 | -12.84589 | -44.36568 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 131326b1-8ecb-3be3-985e-d508ba5f135b | -6.04023 | -43.87927 | 2026-07-09 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ac534229-c430-3898-9ba5-e34967789913 | -13.76734 | -46.30148 | 2026-07-09 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b24043a-bc61-3025-9971-0996d90a2dd6 | -13.76547 | -46.30592 | 2026-07-09 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 517205bb-dbbf-3480-9443-54a50b755c8d | -12.83146 | -44.35603 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68c46955-93cc-3015-bf3b-91487ad28a6f | -6.0395 | -43.8833 | 2026-07-09 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 738a6b23-94e6-323a-89c0-5b44e43c7ca4 | -4.835 | -45.34136 | 2026-07-09 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0a35869-a8d8-3635-8552-d4addbe550f5 | -12.8389 | -44.37157 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e79045f0-7cc0-3f5e-b18a-9f4f8e49ac8c | -12.84651 | -44.36241 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e969a561-cc36-36f8-8fca-8478624f9297 | -4.58737 | -37.80959 | 2026-07-09 03:47:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ecf140d9-17de-3233-a798-a981b4320548 | -13.27821 | -45.18586 | 2026-07-09 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01b5a5a3-9a92-3d64-a935-fbd5e2d3601a | -13.76722 | -46.2975 | 2026-07-09 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0fcc157-aea3-326b-8108-db625bf84e2f | -12.75829 | -44.53702 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1d4324a6-b2d9-3f46-b66c-87b30578aeb2 | -10.86453 | -47.60264 | 2026-07-09 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1a06ea2a-faf2-3293-94bb-a77611396fed | -10.97665 | -44.68132 | 2026-07-09 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d99bc29-86fa-3793-9135-0e67a8a1419b | -12.17321 | -43.45955 | 2026-07-09 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f74f488-291d-302c-a9a1-c282f296dee3 | -12.75958 | -44.53035 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 53771e44-3941-3db0-8926-7208475c486f | -7.70355 | -45.16931 | 2026-07-09 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 82f18fc5-d0de-3b6e-a797-35970adccbe8 | -13.27347 | -45.18112 | 2026-07-09 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40c04c05-c308-387b-9162-21377a4639c5 | -7.28703 | -46.25961 | 2026-07-09 03:47:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b3e48eb-82ed-3310-aa7c-914afd079ca2 | -12.35508 | -47.42148 | 2026-07-09 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8572c65-36dd-3b89-96d6-da33c608e051 | -11.83108 | -48.24314 | 2026-07-09 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebd5e422-bd4d-39a8-a582-abb877abd938 | -12.84413 | -44.37259 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09b13aef-4303-396c-a31c-63cd98f95ba3 | -12.83878 | -44.37455 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8828817f-745c-377c-afb9-16ff05112be8 | -12.84464 | -44.37226 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eba4d871-f2c0-352a-9c70-19e54ce39a76 | -4.8342 | -45.35219 | 2026-07-09 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| afee21b6-9fec-3380-a3e4-f645db69d980 | -6.04434 | -43.8811 | 2026-07-09 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15be1a5b-f9f7-3243-8ecd-ccd19daf74db | -4.83321 | -45.35168 | 2026-07-09 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9b76f7b7-c10d-3ca2-b0ee-72c57b22cc58 | -6.03865 | -43.87995 | 2026-07-09 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2964c07c-d46d-333b-9378-d25bc18620a4 | -12.34819 | -47.41984 | 2026-07-09 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 334c12c1-4c75-31fc-afad-7ec5e497b041 | -7.72569 | -44.56673 | 2026-07-09 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6deb37e-c97d-3ded-82c4-e494315c6d6e | -11.83275 | -48.24393 | 2026-07-09 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5577a9f0-7f53-3828-9be6-b546d78bea6c | -12.83941 | -44.37125 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 756b59cf-2ee1-385e-9114-7ccf0613b262 | -12.26914 | -43.52192 | 2026-07-09 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08986d54-18ea-3d4f-a62f-ae20e218ec5e | -13.76817 | -46.29731 | 2026-07-09 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb4f6798-0c89-325d-93e4-affeabdf658a | -12.75301 | -44.53588 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 746ba9f0-389c-329e-9707-41e541d127e1 | -7.71039 | -45.166 | 2026-07-09 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0ba8e61e-443d-3e37-8b0d-dd989e7b4aef | -11.83953 | -48.24516 | 2026-07-09 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad5776fe-cbf2-321f-854c-79fcc566c92d | -7.70438 | -45.16483 | 2026-07-09 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e9fe0f16-8fd8-31be-b622-0fb07abd5660 | -11.83785 | -48.24439 | 2026-07-09 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d7b8750-3c12-3710-99cb-52446ff4c725 | -12.84608 | -44.36275 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86a8c404-b554-3501-91e8-d1b0be71fbc1 | -12.75893 | -44.53369 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f938dc0-9af0-3597-ab6b-bd75cb422f54 | -11.45493 | -47.58982 | 2026-07-09 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62c6d856-aadf-36a0-b972-53c05af414d1 | -6.48978 | -42.22001 | 2026-07-09 03:47:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e8ac27e9-b88c-36bf-b8ff-a57c7f9a278d | -13.75574 | -46.29891 | 2026-07-09 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d5327cc-02c3-311c-91ba-c21797a0dbf0 | -6.99742 | -43.11753 | 2026-07-09 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a99f418f-136d-3368-93de-5dcc064b0687 | -12.84543 | -44.36601 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70dd2244-d3c6-3142-b1e6-c94a3435c0c9 | -12.84254 | -44.35482 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f1f17b6-7abc-3c13-82ed-73e49c3bc930 | -4.83606 | -45.34192 | 2026-07-09 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb74424a-d899-3189-9302-bfd46ac68be5 | -12.34764 | -47.42527 | 2026-07-09 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dfe3de6a-3cef-3206-84c6-09c9b2cbf917 | -5.14784 | -37.90927 | 2026-07-09 03:47:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b3311df9-8bcd-3955-b35d-8a9602c3beac | -6.49431 | -42.22396 | 2026-07-09 03:47:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea7a4ec0-5228-3e7a-8391-b96541d4e2c2 | -7.70956 | -45.17048 | 2026-07-09 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 184d531d-7be2-32da-bd5e-b32fda7503fa | -8.72286 | -48.33658 | 2026-07-09 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c732718f-d9de-32e7-b7f5-f72dd4bc716a | -8.71439 | -48.34176 | 2026-07-09 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97569a40-8cc2-35a6-9efd-7d81db54c294 | -21.20608 | -49.21839 | 2026-07-09 03:49:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 91c7e77f-d105-3cd4-a8c2-d8ee6c38a0b0 | -8.35207 | -45.40576 | 2026-07-09 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f9ae0754-8951-3c3c-8547-3e28a6d902bc | -17.96263 | -42.85634 | 2026-07-09 03:49:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35416f1e-bc8a-34e8-bfb1-752c45a09ca5 | -9.45596 | -38.91125 | 2026-07-09 03:49:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e59bc959-cbe7-393a-9505-c32babfddd86 | -8.7215 | -48.3433 | 2026-07-09 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e4f3c8f-e565-3f2c-a9ed-3a290f46af14 | -14.9147 | -43.42789 | 2026-07-09 03:49:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 40b3411c-0f16-3dd1-a158-92b47490201f | -17.48669 | -43.32107 | 2026-07-09 03:49:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5d6208f-0453-3317-8c0d-17d41419dbc0 | -15.95572 | -47.76426 | 2026-07-09 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0f7b73f-7e54-3e43-97e0-b3d3057fe190 | -8.96755 | -48.01521 | 2026-07-09 03:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fab1650-e7ee-3d94-b287-557b0472b10b | -14.91843 | -43.43404 | 2026-07-09 03:49:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 24723a40-d766-360c-85c2-a4ebb72f0cd4 | -8.71916 | -48.34454 | 2026-07-09 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b567b290-cf3b-3d05-af91-282455383016 | -17.59021 | -46.68076 | 2026-07-09 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a5db3b8-26fa-3f85-b38f-3b0f78bc9e93 | -8.71204 | -48.34303 | 2026-07-09 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8862e0c9-b23e-39d1-ba51-d04482001cc7 | -8.1249 | -47.0983 | 2026-07-09 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4de77259-7798-3926-966f-781dad8b541a | -8.11696 | -47.10322 | 2026-07-09 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04037ebb-ea92-3373-a0f8-c516e9d96bb4 | -17.48509 | -43.324 | 2026-07-09 03:49:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 248ef011-5971-38db-83b5-7dce1fa9aadc | -8.35256 | -45.40829 | 2026-07-09 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eac1d79c-27ff-3c06-b7a5-e070416df991 | -14.90997 | -43.42693 | 2026-07-09 03:49:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 5b574aa4-1c12-3888-834f-e7b5eb9d15b6 | -16.43851 | -42.05125 | 2026-07-09 03:49:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README5.md)
