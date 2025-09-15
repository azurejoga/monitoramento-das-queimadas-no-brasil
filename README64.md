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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43c53312-1d4c-342b-bb6b-9c887c835aae | -13.18719 | -47.28311 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e38ab477-40ac-32ad-b4bd-ca2ba67cbd44 | -14.42974 | -53.36756 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67eaf68f-50f0-33f5-84ed-559a0c54e3e2 | -14.81509 | -51.62561 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 28ea77cf-8c5f-375e-b270-b77b3ba2fbd9 | -18.47305 | -46.95128 | 2025-09-15 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9db10656-7980-34fc-bea5-a83de53aff40 | -14.18093 | -46.14748 | 2025-09-15 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 441b5b1a-ec5a-360c-9b5d-48bd639c5bbe | -18.15763 | -49.19822 | 2025-09-15 05:12:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f0696da6-d45e-3689-8687-e186e2bd0b79 | -15.69118 | -54.33872 | 2025-09-15 05:12:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ea2bb96-a730-3ccf-bfbc-2ad48c9181f8 | -10.21411 | -69.0517 | 2025-09-15 05:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68828e18-8c4b-378a-843e-142dd285c8f9 | -14.79787 | -51.60722 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 95f1eaa6-7faa-3feb-b029-c10f378a2f4a | -15.78841 | -52.20444 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f714d20e-2a9d-35d5-bf15-e5f9ee447aab | -14.50135 | -56.51649 | 2025-09-15 05:12:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 171ac3fd-f9c2-3027-bc2b-cf1ccd88f57b | -13.89058 | -48.31237 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd4c7137-19bc-357e-ae3e-a90171c63079 | -14.79724 | -51.61042 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a3c539db-139c-37fe-945f-e485ac837eb0 | -14.93676 | -46.58135 | 2025-09-15 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 175c7647-a95b-370a-b332-e2505cea5a31 | -13.88533 | -48.30625 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 264be545-9de8-3467-a1d7-394e6144b9cc | -18.15689 | -49.20586 | 2025-09-15 05:12:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c68cf21d-8785-3eb5-9faa-09eaa811b9bb | -15.80025 | -53.47495 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd8b4670-69e3-3091-9ed0-e1447122ca1e | -13.89599 | -48.31712 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 590e164c-8de2-372b-8362-29f150ce449d | -12.85879 | -62.12431 | 2025-09-15 05:12:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| debf8eab-c159-350c-8f49-e5ab3579c385 | -16.49547 | -55.15992 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4aa72232-5495-39bb-b702-c8757863fc6f | -12.40884 | -63.888 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 125bde15-6893-3262-bcb5-0e174306785c | -17.40475 | -49.2643 | 2025-09-15 05:12:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ca873e9-211b-3531-969e-de5519de91e8 | -13.75653 | -48.76957 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bb48868-c539-3764-8d60-4b9d011610b5 | -13.18518 | -47.29014 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5dc281ba-1a26-3b55-8999-0a31c64b940a | -13.19334 | -47.28439 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d1b2ef0a-e60e-39e2-9284-ba545543ba59 | -14.82401 | -51.63214 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 91035c5d-8174-3537-9b17-9ea8d99f2066 | -15.77842 | -53.4756 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cd12bcbd-127e-3ddd-867f-b25e2620b440 | -12.7982 | -47.94089 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d50b9ca1-13eb-3bf7-9a84-de64c8852bc5 | -14.28144 | -46.12222 | 2025-09-15 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3722564-0fdb-3934-be0b-50ab8e1ffb98 | -15.79691 | -52.19898 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0d5f93f-0e0a-3482-91ff-44fe670ab0e6 | -14.94338 | -46.58207 | 2025-09-15 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1ed4bdf7-e634-368c-808e-7c54f9e24e47 | -16.7067 | -54.95122 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c59de335-0941-3808-bfc4-03e9ea21ccd9 | -14.80135 | -51.61632 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 6e7bed48-5f0d-33a6-bb18-6d9086a02a94 | -15.80338 | -52.19829 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d90584b6-3c6f-3824-9a26-fff3f969017b | -13.90198 | -48.31684 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 86c03098-fe34-37d8-9f30-0494323fb003 | -14.81446 | -51.63089 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| ae2d0465-6a8d-3828-a65d-7903039e12a0 | -14.9428 | -46.58789 | 2025-09-15 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b3fe621f-05b6-35ef-a98a-5f54b5fb02bb | -11.77646 | -64.94563 | 2025-09-15 05:12:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e416b65-a287-3216-8576-21a88818bce8 | -13.75004 | -48.77596 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 526a078a-d38e-3e1b-9c9e-28b32fb4eb7b | -15.71352 | -53.07045 | 2025-09-15 05:12:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 605fbc74-ec5a-3cd4-bc25-f4cfb134c461 | -12.31978 | -64.08279 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9088953a-a35f-3a19-89ae-f7058ff42d30 | -15.79517 | -52.22581 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 007cc9d9-2c8f-32bf-90cf-d7f283cea6cd | -12.77926 | -47.9796 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 900b0020-3e5b-37cf-b083-559945cbee39 | -14.83356 | -51.6334 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9ebe24ee-7bd7-34ed-b590-40956aa58484 | -13.18767 | -47.27897 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 023cb1b2-ca8c-37c4-86bc-e9c9167b5473 | -15.7933 | -53.46133 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b5ff5391-ef56-3488-8d0f-e2c2c73162a2 | -15.10089 | -52.47844 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e814855b-ecef-340b-b6f9-8bb52fd2eb3a | -15.78472 | -53.46027 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 52624bd4-5260-387d-be3c-6db46d5504bd | -13.173 | -47.28642 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0b5af02-f790-3a35-9814-b61e7906ea5c | -14.20318 | -48.77638 | 2025-09-15 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8ff65ee-1b75-3b56-86d9-70a41f43d143 | -14.14526 | -46.26024 | 2025-09-15 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a79a58a-44b7-367d-afbe-885c7c459a63 | -15.85881 | -59.40558 | 2025-09-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c7f84c8-8863-3e31-b778-d7146a959c5f | -13.18658 | -47.27725 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40a98d09-415e-354f-9859-d2046c4b43b4 | -14.20361 | -48.77248 | 2025-09-15 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d795da3-9a7c-3692-8d6a-a25bf3f7cc22 | -14.8027 | -51.60576 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42a1bbfb-39e2-34ff-8c6a-a6a1891b7c9e | -15.76731 | -52.22189 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf33a670-2e7d-3731-883c-63c61db14de8 | -14.2023 | -48.77163 | 2025-09-15 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d2a3b49-2e5c-337b-ab14-67fd6fdbd3c0 | -14.4345 | -53.36412 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2663b2bd-7259-3d2c-bdf8-145e354bcd2e | -18.47001 | -46.94955 | 2025-09-15 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a9cd44ef-25d4-3cb9-b966-b687df0bd11d | -13.8802 | -48.14071 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80fd061f-1af8-3867-b456-4b50747e3944 | -18.15726 | -49.20202 | 2025-09-15 05:12:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 51c730fb-1f7b-3c9e-aaf6-f7cb98a2c6fc | -15.78902 | -52.19963 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e6db729-8b79-3f94-9e9a-a4f5736f9884 | -13.17403 | -47.28802 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a248d333-4144-374a-9970-e58be351cb76 | -12.42961 | -63.88812 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e65499d0-2d69-32cb-a0aa-49006bbbe045 | -14.20276 | -48.76776 | 2025-09-15 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ad7198c-a69e-347c-9690-6ff0dc537c00 | -13.76555 | -48.77402 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 874e38af-c16a-31c8-9bc1-64c340da669a | -15.78899 | -53.46093 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b824125c-f305-39ec-8762-ef79082566e1 | -12.40819 | -63.89158 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27442cb7-3c8e-3db9-ac2a-2d4f3b788880 | -15.79052 | -52.22519 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9fbc4a3-d2ac-3e78-a724-9bfd8b75ac53 | -16.28588 | -45.68584 | 2025-09-15 05:12:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e691d715-0bbf-3b42-a82f-8546c024f260 | -16.67264 | -49.78165 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38206eed-4bf8-32c6-8468-e05f55ccb8dd | -13.18615 | -47.2812 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 650709a3-2446-3735-8aee-a2ea6f82d82c | -12.78741 | -47.93042 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce85c740-476d-375e-8e21-d5c37ba66b5e | -20.90876 | -55.17221 | 2025-09-15 05:14:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 177d7b32-50f6-3024-9a95-c2a27ee285f9 | -20.23834 | -46.18081 | 2025-09-15 05:14:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8886f549-bd1e-3144-bc03-2846ef538fb6 | -22.61423 | -54.92356 | 2025-09-15 05:14:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 60dc4e6e-35ff-3877-b308-309ee85d4444 | -20.51999 | -55.63757 | 2025-09-15 05:14:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 735dd315-d5dd-3cf1-a860-ef3c9bb12954 | -22.78263 | -46.80089 | 2025-09-15 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c9b40fd6-7f9d-3a6a-ac1f-2e2ebde3b775 | -20.95938 | -54.9854 | 2025-09-15 05:14:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95afba14-0138-3c7d-9fa2-d6e4052890fa | -20.23166 | -46.17408 | 2025-09-15 05:14:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59bb799c-6404-315e-a11d-5280874ebd86 | -20.18726 | -56.08921 | 2025-09-15 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8d2fcc7-a7db-33d5-a30e-6a1d5c6f7bcf | -23.24479 | -47.11441 | 2025-09-15 05:14:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f43d4fe5-5ebe-3d0b-9dc6-e32467548edd | -22.27366 | -56.04829 | 2025-09-15 05:14:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f601b8fd-d99d-3199-8a72-96139864f607 | -20.51935 | -55.64278 | 2025-09-15 05:14:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80c298a8-e23b-379e-aa28-aee6f514ed44 | -20.52107 | -55.64129 | 2025-09-15 05:14:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b4ae4739-0222-332d-84ac-1929cf830845 | -22.28495 | -49.04173 | 2025-09-15 05:14:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99c83875-88b4-31c7-8fb1-dd7e82023b0c | -20.51387 | -55.63446 | 2025-09-15 05:14:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a876765d-d771-34b0-8251-a96ed928580e | -22.04989 | -56.08442 | 2025-09-15 05:14:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0f67a35-72ad-3a6a-bf26-f1b78d1380ac | -20.32891 | -58.08461 | 2025-09-15 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 001d9f56-57df-3022-8cad-761b1ade62fa | -20.75865 | -56.94316 | 2025-09-15 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0bd994b-fd2f-390b-83b2-8346a9351812 | -20.23115 | -46.18094 | 2025-09-15 05:14:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6072edb8-79a4-3af2-93ab-980726c044cd | -23.45942 | -50.80201 | 2025-09-15 05:14:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2106aa14-ab2a-305b-8118-b4255f22984d | -20.2344 | -46.18353 | 2025-09-15 05:14:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 42be9c40-76f1-3152-a9ed-22adfcd380d6 | -22.65862 | -53.11464 | 2025-09-15 05:14:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b4e33ea3-d7f8-3091-b26b-e1247a8fea65 | -18.9778 | -48.58671 | 2025-09-15 05:14:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 89ae5f8d-e568-3fb9-b43c-e9e226062a17 | -24.8387 | -50.35511 | 2025-09-15 05:14:00 | NOAA-20 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a7a614fb-b061-3988-b7e8-a6c7f0e24069 | -20.52611 | -46.87225 | 2025-09-15 05:14:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e53625d-24ef-3bcf-9584-0866f6f3b7c5 | -23.4708 | -47.37725 | 2025-09-15 05:14:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d73977b8-afcc-32d6-b5fc-c4214760423e | -20.51781 | -55.63525 | 2025-09-15 05:14:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97fc60cc-8325-3c08-8930-ff62ac7747fa | -23.47852 | -47.36494 | 2025-09-15 05:14:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README65.md)
