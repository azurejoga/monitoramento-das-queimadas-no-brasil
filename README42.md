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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cafe819-d2e4-3926-9793-8b6d05eed085 | -14.66674 | -48.40701 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d81c4659-a313-3d7d-9ba2-4eda5659fa54 | -20.137 | -42.41197 | 2025-10-28 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b8a8543e-f40b-3c2b-991d-6670be420c62 | -19.5429 | -43.90557 | 2025-10-28 04:17:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 167783f1-762a-3664-b47b-6dbe20f3e6b8 | -15.21017 | -47.2131 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 432f8597-5009-302c-a03e-5bd93218feb3 | -14.53524 | -47.98689 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7f18f0c-86f9-303a-af3b-deaa163ff4ef | -16.1398 | -45.09968 | 2025-10-28 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc435aff-f7de-341c-8937-ec4012600e3c | -14.81578 | -46.70706 | 2025-10-28 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a8a699f-d2c8-3fe6-92b9-10690816a41b | -14.78354 | -44.98399 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a4ed8b5-99a0-338f-a978-a4811d629aa5 | -14.30234 | -44.53761 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8917165f-bcae-3df7-8774-cad6b6730235 | -14.43856 | -44.79575 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f831da25-9b9c-3cde-a621-2adaacc8f92c | -13.7465 | -48.42009 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f57cad0-6306-3563-9707-83fd5319e5fd | -15.18892 | -47.21327 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 433d49eb-c91a-34a4-85b4-bc8901dc73d8 | -18.05429 | -45.09673 | 2025-10-28 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3fb721a-178c-3b22-acc3-84cb0c11e9ff | -13.07233 | -48.21166 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a5a038f-595c-36d2-9f8a-4ffcdcae4dfd | -13.87757 | -48.49153 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36ac9e8e-6027-3aab-9bed-e79d00578d72 | -19.30315 | -44.37596 | 2025-10-28 04:17:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d297c12d-c2a8-3bdb-9206-c15f06b94e03 | -13.31619 | -47.69891 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cea45382-3a47-392d-9abc-9b292af213c4 | -13.22296 | -47.10479 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5ae3673-eb96-3df0-a718-2bbe20571575 | -13.54208 | -49.57321 | 2025-10-28 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0f858b1-332f-3446-843e-bc4c8b516d83 | -13.12788 | -47.25788 | 2025-10-28 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21d4f9d8-aa2d-3ed4-a99e-61fb5211e9e7 | -14.53302 | -47.97823 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d6e80b9-97f5-3e93-8ff2-3563700c8765 | -13.31337 | -47.68541 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfce69cd-fc04-3efc-9e1d-3c6558293358 | -13.43125 | -47.37822 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2c0493d-1dca-3c7b-b367-96aaba652dd3 | -15.20607 | -47.21646 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85afdd7b-c7b3-3be3-84b2-999fb26d6a9f | -14.56166 | -47.98301 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c658ecc1-a43f-306a-a209-ecba5ab7d806 | -14.67039 | -48.40765 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9de5a0ad-1239-3cfa-b631-a79407bb872d | -13.63299 | -47.03553 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 9333ecdb-74f7-3490-90bd-c42057af07e6 | -14.72853 | -47.35814 | 2025-10-28 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8269623-3ca8-3254-b127-0f5fcbe4afe5 | -14.94264 | -43.43934 | 2025-10-28 04:17:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e5921240-3811-35b2-bd47-668436b7b0bb | -14.43017 | -49.42146 | 2025-10-28 04:17:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40b6acaa-4956-3431-bccc-b869a30ef502 | -13.39369 | -48.51401 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b328055-9908-3978-ba7d-9f894df9f1a4 | -13.5571 | -49.58069 | 2025-10-28 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91f9c5d2-0c17-3b59-866c-f1e75a926136 | -18.2236 | -42.9259 | 2025-10-28 04:17:00 | NOAA-21 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b636b0f8-eafd-3e69-b6df-3811a962fb30 | -17.69347 | -43.95646 | 2025-10-28 04:17:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d2b336f-dd4c-3471-803a-c954fbd9d190 | -14.31311 | -46.51316 | 2025-10-28 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03644910-4b2c-3c0e-8434-0007b85704aa | -14.43142 | -47.84844 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 044bc8a6-60a9-38c1-9fca-883e2e4c5649 | -18.05395 | -42.53607 | 2025-10-28 04:17:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4ee4a9e7-ac40-300c-a26e-c2d3f0ccdaf4 | -18.93101 | -44.21232 | 2025-10-28 04:17:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7688add0-a636-38b5-b685-aa9a0ffacebe | -13.53631 | -47.16531 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0d18228-a202-3d3d-b7e9-2c5bdb41ff1c | -13.56804 | -48.52236 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 913cf95b-0945-37a0-99e5-0fe7e5561e49 | -13.85793 | -43.77961 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13a55605-0aea-36b7-a5d3-239a611c6540 | -14.43078 | -47.85217 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3ef4f9d2-67bb-33a0-8db4-4a0587aed237 | -15.20265 | -47.21576 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f938609c-4b35-333e-8b91-4a18cc99d159 | -15.46908 | -43.05717 | 2025-10-28 04:17:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ae2e96b2-b915-3823-aa28-b58a4c2557b9 | -13.69106 | -48.46316 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3623f330-28fc-39f6-a2c9-ad28aa6eccfd | -15.15041 | -46.59776 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b04c598a-4f0f-3a17-ae6c-c4bcf18b1952 | -14.29683 | -44.52945 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4252450c-a189-39cd-b349-c88175b352f3 | -14.78298 | -44.98753 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 291324d7-9d82-3b90-8300-11064290332e | -13.78953 | -48.502 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78eb28af-479a-374f-aec5-a1c192ebaaf9 | -13.7965 | -48.66325 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5d38194b-7b2c-33fe-9702-ad12a98a98a5 | -14.4172 | -47.8674 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a94e043b-bddd-33c4-aa7f-034c1c3c8da4 | -13.73064 | -43.99041 | 2025-10-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6a0011f-ec0c-3b77-9649-e18a46283042 | -14.42533 | -49.42608 | 2025-10-28 04:17:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcfa8f13-9321-31a1-a856-381adf891a7e | -13.88051 | -48.49661 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb2bef30-b2b4-33e9-bd51-3df4b2d3bbd5 | -15.23193 | -47.94953 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c654455e-d0aa-3dee-ac0f-425ed4f47405 | -13.22217 | -47.08819 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1929cec1-b35e-381a-b14b-5053cfc6652f | -13.87437 | -48.51003 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89393baa-bbca-3684-9bd5-50481a044b99 | -13.31558 | -47.694 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1abe6b5a-d2df-3a0f-aa8d-6d2f5727fd48 | -14.76652 | -44.96299 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e906483b-700f-3789-8ae3-573bc1a17c00 | -14.42555 | -49.4187 | 2025-10-28 04:17:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de850d75-0b0b-34ad-ab5c-2a605981d02a | -13.54409 | -47.14054 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 408d95a9-1ce7-3d72-9a19-f1434ce9fc4c | -18.92762 | -44.21176 | 2025-10-28 04:17:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54844a0a-913d-396a-af12-3127ff184af9 | -13.36691 | -47.39289 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bd6167e6-b8bb-3b61-8d95-c2a0e0d152c8 | -13.66396 | -47.63518 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fef03c24-d8db-3667-9e2d-6e08994d1903 | -14.25016 | -48.11909 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27cf2191-8cb1-3699-b4a0-c59f5aa2eb69 | -13.56692 | -48.55125 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9a757ff-d9a5-381c-b450-b89d6c21d814 | -15.57745 | -43.20253 | 2025-10-28 04:17:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 37b3ec5b-cc33-320f-a00f-0bf187d3196a | -14.65217 | -48.40435 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4d9b009-7863-3055-b074-655b031c0bff | -14.41275 | -47.915 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d2a8bf7-c05d-3c94-a259-a11ed231e239 | -15.15315 | -46.60214 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 522eedda-3597-3ffe-aa44-29caaf71560c | -15.18547 | -47.21274 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d70bf1f7-62bf-3b98-b426-7a9da3aea7b2 | -13.6121 | -47.03256 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29b83f5c-6c64-3dac-a690-a9c18486461a | -14.41931 | -47.855 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5b74b86-d998-3702-a48f-57c8124ba508 | -15.15624 | -46.5834 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ec58ba77-e648-3f5e-8dc7-e3834de6eb8d | -15.96851 | -43.01862 | 2025-10-28 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54afe818-851a-31da-bb73-ca914216d6ac | -13.61622 | -47.02922 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74a4d173-0743-3576-ac32-06bf8a0c2b4b | -13.87832 | -48.48721 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1dee1801-4a09-3e60-80ba-9c3faa03dc33 | -13.85738 | -43.7832 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a6f584b-8f7e-38b9-ae6d-65604bc640ad | -15.19706 | -47.20688 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0acf663a-2fb4-3918-96e7-c3212b07914a | -16.593 | -43.5141 | 2025-10-28 04:17:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c35d1c4c-4e9f-31bf-937c-90f62d0175ec | -13.94421 | -48.41331 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe1c4c66-11e7-3c97-977c-ce5872cd6ee1 | -30.58629 | -50.57752 | 2025-10-28 04:19:00 | NOAA-21 | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| fc397df4-6645-3e7d-913b-581dd79cfb23 | -30.11812 | -52.08519 | 2025-10-28 04:19:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| aa0699e4-99fb-31ec-85a6-61890070f547 | -9.4553 | -46.8819 | 2025-10-28 04:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d8947b6f-ab83-397c-8d00-d9e74d9a1dcb | -4.4632 | -43.2386 | 2025-10-28 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 1bb3a5f2-7051-3662-9b5d-be7140ebf5bd | -11.2798 | -45.5052 | 2025-10-28 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 567c911c-569e-354a-9242-9761c200c68e | -10.5872 | -49.7998 | 2025-10-28 04:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 90372126-f589-3587-8bd4-e4d86fe26423 | -3.0158 | -45.3679 | 2025-10-28 04:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| c1961059-715a-3552-8cf6-ac1d9220edbc | -3.0344 | -45.3672 | 2025-10-28 04:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| f680f57b-ca40-3047-be7e-2c1f4be8b42b | -7.9693 | -46.7423 | 2025-10-28 04:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 05e62ce9-4825-3ab2-8f9c-ffcb399eeb4e | -10.5875 | -49.7782 | 2025-10-28 04:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 7d213f4c-157e-3ff9-87b6-083109ed72a6 | -7.8225 | -46.444 | 2025-10-28 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| fcc77712-ff7d-3ae1-b0b2-d8060bb41380 | -3.0158 | -45.3679 | 2025-10-28 04:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8c910093-4133-3c56-a781-ce69bd07ebba | -11.299 | -45.5025 | 2025-10-28 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| fa6438d8-a0ed-33fe-b497-638db50a5dc5 | -7.9693 | -46.7423 | 2025-10-28 04:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 72c17b88-30d4-38dc-b8c9-591469684757 | -3.0344 | -45.3672 | 2025-10-28 04:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| b87df86a-ca98-39f4-a9c5-e34614fb3470 | -8.646 | -45.2806 | 2025-10-28 04:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 2a6040db-3d67-300c-b625-4df59833751e | -4.4632 | -43.2386 | 2025-10-28 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| ad8a34c1-efe4-3e85-9530-d83175aa4f8f | -7.8035 | -46.4681 | 2025-10-28 04:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| e179721b-73ec-3936-bf8f-288e85c22fd0 | -7.8223 | -46.4664 | 2025-10-28 04:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |


[Clique aqui para ver as próximas entradas](README43.md)
