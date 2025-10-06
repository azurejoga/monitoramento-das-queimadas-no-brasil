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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 027f2c76-8d4c-3987-b078-13c087973f36 | -14.68675 | -48.37448 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 808463ad-4b6b-3585-ae46-369bbb528e5a | -15.22558 | -49.2908 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9a046e24-9bdb-30e1-b455-16d7bc7be7c8 | -15.35507 | -47.99743 | 2025-10-06 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3897c82c-6f32-32ff-ae27-90ba67c4f48f | -13.36499 | -47.57677 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37ab2290-6322-37ca-8952-6b83e3d2547d | -16.00275 | -50.84928 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1098ab2-efb5-30ce-83f9-eb26c1469e4c | -12.91082 | -54.73328 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d853cdf6-ac97-32d0-bf05-00ce9531116a | -18.28236 | -53.32182 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184e0517-2cb0-3220-9243-6273aa970dbb | -12.37727 | -63.73071 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 487cecf3-b1e9-389a-aa04-af8d831532b5 | -12.90408 | -47.299 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53d9a687-b714-3dfe-80f2-794a5c1006e1 | -13.71801 | -48.07993 | 2025-10-06 05:18:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67f51059-b916-31df-917a-0b5e60906b0f | -18.13131 | -53.38738 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 78dc06e8-7922-3967-9713-90679978b03a | -15.23302 | -56.78119 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8683cdfa-bfb8-3e82-983b-1fc237a2d994 | -15.65797 | -53.83935 | 2025-10-06 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 348f5b6f-ee50-31b3-8ce4-06de9c79090f | -12.32239 | -55.12381 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc71c514-d4cc-3a73-b57e-f601085284d5 | -15.22053 | -49.28442 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 45af6f06-a64e-390f-b53d-bffde84d8b71 | -15.56641 | -52.45916 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37e0c725-e8cd-35a7-9659-87cfd7cfec38 | -15.57885 | -52.44071 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e5cf943-1316-3333-b63b-77ba99ca2cc9 | -18.1939 | -53.38098 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69351776-80b3-3a79-8515-939333d5b407 | -11.77243 | -59.27002 | 2025-10-06 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 06f01fed-a701-3e45-8fe6-d43d07f20721 | -11.87591 | -57.82055 | 2025-10-06 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 821b4d41-36ee-3a92-9b6e-7bf65112f221 | -15.22279 | -56.82668 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8b3ca56-bdf5-3e26-99c7-14e1ef354844 | -14.34384 | -47.67887 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 594f4827-ea20-3cf8-8962-56128cf648d7 | -15.98302 | -56.00653 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6981cff6-c56e-34bf-9fba-374c2ad03872 | -12.9103 | -54.73714 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84864153-2b41-30e7-b080-ecd165b58d8e | -14.54121 | -46.95963 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9612346-deff-37bd-be1d-6a90c53e5714 | -12.91498 | -54.73389 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b078daec-1d49-3bd9-8802-527d99ad3105 | -17.83981 | -57.61493 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 371ef6f5-908f-37d1-bd19-98ce4d000d1a | -12.91337 | -47.29724 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b3e6bcf-f175-3f99-901a-c1040069f11a | -16.14581 | -57.57418 | 2025-10-06 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0ff12614-f2eb-3053-93ba-b530b22d3a05 | -14.71427 | -48.36227 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c3f139b-ec13-31e2-ba16-98ebd4aa4f9d | -15.30468 | -56.93184 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb7c2463-7ec0-3904-b310-4519a0704ce4 | -12.29926 | -55.11309 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 761f0a0e-563b-30fa-9329-baa9742ef1cd | -18.1896 | -53.37504 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7dfe363c-2c71-3b62-90eb-becddc8a9ed7 | -15.98702 | -56.0071 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3eabb239-556c-35db-a527-6d59ff79a073 | -10.38261 | -67.96245 | 2025-10-06 05:18:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa40e9a2-ccbf-37e4-9321-53acdaf7d261 | -15.61758 | -52.54263 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1751614c-66a1-3c73-9570-a85d3538a43b | -14.34008 | -47.71611 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 196e2b02-18c5-392a-b64d-3e6a2b972af0 | -15.97902 | -56.00596 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| dcf4441e-1c31-333e-baf1-fcbc23d60ba3 | -13.25723 | -48.4942 | 2025-10-06 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de444009-31b1-3226-91fb-7f7acf02a260 | -15.22604 | -49.2864 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 67c46f24-8bbd-3b26-805b-28995b01336d | -14.8571 | -51.47539 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 846b19a6-c392-3248-8541-0a75de8e49ee | -14.35892 | -47.73061 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21d64139-83a3-38af-acbc-3eb24e448eb6 | -15.5136 | -46.85144 | 2025-10-06 05:18:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d16ab2a1-9aa9-3f4e-bb00-00fdfc3c27ed | -16.01125 | -50.84321 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f92d0bc-acf0-3a4f-a328-c14ebbf86077 | -15.22624 | -49.28914 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10487f6d-89b6-3f36-9bd1-387dc698eeed | -13.08236 | -47.82201 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2dc52f0-981b-3676-b5b0-cdd76c022a3a | -13.05262 | -47.90819 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1249ffd-aa60-3cb1-9146-2b844afed1d1 | -15.21148 | -56.82508 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2f64cfbf-31dc-3987-8b49-16809f469823 | -15.57309 | -52.44608 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d1fb8d2f-d6c2-3d09-a4d0-01892127f44b | -14.34361 | -47.71627 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66f63a04-36d1-3d46-a70a-1a056a59481f | -14.86283 | -51.47265 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7d180ef3-9f30-3818-968e-a9fe2ab7a471 | -14.652 | -56.01433 | 2025-10-06 05:18:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 691a29ba-9281-32cb-ab0e-a3dc6d60e3bb | -15.57381 | -52.44004 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3782facf-b015-3c5b-943a-95c1d1af7d52 | -14.69352 | -48.37609 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8da7b380-1923-310c-bcdf-91a067ecc899 | -13.23471 | -48.46646 | 2025-10-06 05:18:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f0c089f-03de-34ed-99ec-e3991f88e49f | -12.38469 | -63.70946 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6112247a-ada8-309f-94b5-b069d2cd0f43 | -11.83874 | -60.42795 | 2025-10-06 05:18:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3b1895a-e35d-3c94-931c-224648515e5a | -18.11503 | -53.39938 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| adf8c047-042b-3cec-ba34-86f4b29a686e | -13.27187 | -47.83297 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e62952e-9bd7-3df8-9429-44fa6ae2ec18 | -15.35085 | -47.31455 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1cc20bc-0014-3c36-b0c3-d0dcc35c462c | -15.58768 | -52.5363 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eebe6cbf-d3b0-310a-92ea-888712f7b2a8 | -14.93166 | -46.83098 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a60d4f38-7ee1-3c5f-a937-d88dfc8220e2 | -18.17414 | -53.37993 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 82c90f91-72e9-3bd6-809d-95ae9327f232 | -16.0557 | -50.93798 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 180d091c-fdd0-3a75-8f8d-caceebce78f1 | -11.86849 | -56.89012 | 2025-10-06 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb7e3e0d-1a1d-325f-b134-cb76bc67e382 | -15.99977 | -59.52981 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3128f15-09bf-300d-bfb7-6754964f4c5f | -12.94572 | -54.72627 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 578f9e5c-1c93-36d3-b088-e5571781bfe2 | -12.45139 | -54.4065 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f50706c7-b27c-35cb-8248-9abad120844c | -12.38395 | -63.71383 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46d15b8d-3501-3361-a24c-b69669490eb4 | -13.1207 | -48.00347 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3745287b-5df1-3392-8571-f05cb45871b9 | -13.33943 | -48.05274 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79190700-965a-38a5-884b-f20b2fab8ef8 | -14.90905 | -46.84221 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53623732-fae6-3321-9489-b664d38e2829 | -14.68431 | -48.40225 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fd460c16-a559-3715-8475-3b7de67ba007 | -12.31887 | -55.11963 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7d58873-5908-34bf-9eec-0b9588925fbf | -15.56708 | -52.45354 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4a97363-47d4-387f-887b-66fdb51d14f3 | -16.03456 | -50.97556 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e4a6f61-f822-320a-b434-2c57538d079e | -15.99677 | -50.85195 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5130f5a-9d96-3b35-943a-640b7085cbc5 | -17.38787 | -53.59611 | 2025-10-06 05:18:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2037d00e-7a67-3373-bed2-f9a60b5addbe | -14.67095 | -48.39972 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a02dd525-a8ff-3218-9178-3a534ff168fd | -14.33694 | -47.71526 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73539d17-1668-3efd-adc2-b2f575bd0944 | -13.27878 | -47.62562 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29929266-fa1c-3c3d-b9ab-e6a7be15856d | -14.90081 | -51.50577 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 7ebfa00e-2f65-3213-a61c-48bf10afcb90 | -15.74729 | -47.69048 | 2025-10-06 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 857dff5b-f402-3dda-8233-355feb3b51ba | -18.26458 | -53.3294 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 94e33d15-9546-3d7a-9cc9-c1624285ee85 | -14.64414 | -56.01325 | 2025-10-06 05:18:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 684b19d2-8ead-368e-b4a8-3cf43820f840 | -14.75163 | -54.6819 | 2025-10-06 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe372abd-ed0e-3fcb-aef5-897d10a561d8 | -17.2634 | -46.92408 | 2025-10-06 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac60b673-0906-37fc-af4a-cdd47f1683e6 | -15.5919 | -52.5434 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c12bf2e5-d556-3e57-9827-96de18395e5e | -14.92263 | -46.82102 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 99f28e13-031e-3597-a2e4-9e9ae9c84db3 | -14.63632 | -52.53317 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4425bc25-8cfc-3405-8bb9-3ee51f7f69d2 | -13.27444 | -47.62978 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 325ca4ab-64f1-368c-b30a-08bfe854cd40 | -16.00612 | -50.83809 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e92b0e4f-7c22-3a75-b136-48e14174f8e9 | -18.12647 | -53.38622 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a89490ec-8c45-39b2-b3a4-c30ab273aa5d | -15.99189 | -59.53624 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c74178b-c4a3-3e50-85d4-8ea5481b83fb | -13.26342 | -47.84891 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 37fe9747-8809-3aad-86be-fcd95b71dfe0 | -14.89588 | -51.5017 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a7a28464-5f2c-307a-b7cb-6d96e966989a | -15.59623 | -52.55145 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 27a6c713-8eec-39aa-b9d0-bcaa38a068cb | -16.95888 | -52.67727 | 2025-10-06 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b447a81-25a6-3936-a6c2-e8b443415589 | -14.71227 | -48.38459 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fdb5d78d-fe05-3d37-958d-83c2a4f51a6e | -14.64807 | -56.01379 | 2025-10-06 05:18:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README72.md)
