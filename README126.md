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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b98e5fd2-015a-33db-aad2-b1497eb01a2f | -21.58943 | -47.87112 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| eb0e7c77-f9b1-3dd5-bfc5-9f44f1a70e1a | -21.5893 | -47.83671 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 542ad1c5-a842-357a-a005-ec7acafd9390 | -21.58893 | -47.84122 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fa16c87-7d5e-3b3a-8061-15b25bd0ee68 | -21.58854 | -47.84581 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f77b8d8-df67-3dd6-a18a-8d39d3c6537c | -21.58816 | -47.85045 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e8972d1a-8bbd-31d1-990e-b5c6570a472a | -21.58777 | -47.85508 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5c5f372e-38e0-320e-8885-982a54b4b39c | -21.58738 | -47.85971 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 58c11bf6-5b96-3798-8937-d445623dcc2e | -21.58716 | -47.82957 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 73d136e1-1261-3d19-b080-3438657ad927 | -21.58699 | -47.86435 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ac0ce9db-b9a4-3b6d-bc5b-8df6ea815816 | -21.58677 | -47.83391 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f729a1e5-71d8-3736-ba66-f06e09730714 | -21.5866 | -47.86901 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 745d259f-854f-36b2-8a69-3d183aaf5cff | -21.58638 | -47.83824 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c83be47-6deb-3cb5-8d02-520db82df8e4 | -21.58597 | -47.8428 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e707c91a-9807-3862-a355-f4102873de22 | -21.58472 | -47.85658 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0abb317e-8683-3b98-a7d0-df07fc6086eb | -21.5843 | -47.86119 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 7e55b278-17bb-330a-a765-11a306c6bb2b | -21.58389 | -47.86583 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 945d6e3e-d39e-394c-9667-d63c35804a53 | -21.58331 | -47.83625 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3566793a-fd5f-3167-b25c-572274a15239 | -21.58293 | -47.84078 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f25add97-e697-3c10-b5ac-982656db8b49 | -21.58141 | -47.8591 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 299371f3-7bb8-3fa2-9416-f7f08b65ae58 | -21.57997 | -47.84243 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 473e5850-e8e5-334a-9d92-2495cd982ce9 | -21.57874 | -47.85609 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3f8212da-6923-36fb-a5be-a9e6d27da611 | -21.57833 | -47.86069 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e7092877-4b48-3edf-8d9b-e157e67deb0f | -22.4898 | -48.36089 | 2024-10-01 05:08:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d0a0d68-b20c-335e-b43b-3a8a835049e8 | -22.43831 | -48.41032 | 2024-10-01 05:08:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fe44e51-346a-39d8-a59f-d4cabd6bcfa0 | -16.63204 | -47.6327 | 2024-10-01 05:08:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b347a91-a071-3e66-8265-2512fee18acc | -16.5162 | -48.05263 | 2024-10-01 05:08:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79b59247-6984-373c-85ca-061a0905855a | -16.51066 | -48.05185 | 2024-10-01 05:08:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 541da2eb-a1fb-3bd5-83ef-b14410ec77fd | -16.51022 | -48.05598 | 2024-10-01 05:08:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 75b00ea6-fa62-3429-bb07-b880e52fc571 | -15.77161 | -48.49817 | 2024-10-01 05:08:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b17a9fd0-6c59-3d41-9e69-e8b65ae6cfbd | -15.77118 | -48.50187 | 2024-10-01 05:08:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36b25e8f-4fcc-3443-b67d-925a2b6b98d8 | -15.56965 | -47.85445 | 2024-10-01 05:08:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bc510fa-b97a-38f8-a598-8ed41969bd07 | -15.36539 | -47.58808 | 2024-10-01 05:08:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d319a4b3-e4c9-3f72-bc95-f1672c2c557f | -15.36494 | -47.59207 | 2024-10-01 05:08:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c55bd41-8d14-3cdf-81d6-691db79224c2 | -15.36297 | -47.58914 | 2024-10-01 05:08:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62c6be3e-98dc-3890-9bdd-c4b69eb14ee6 | -15.35975 | -47.58732 | 2024-10-01 05:08:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 020d7430-2498-3a49-ac5c-18aeffda73fa | -15.35733 | -47.5884 | 2024-10-01 05:08:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6483639-469c-3c0c-ae86-7f7482f0a4fd | -18.6549 | -49.00097 | 2024-10-01 05:08:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5d2cc37-5690-392d-b1bb-27bb196970e7 | -18.38376 | -48.22215 | 2024-10-01 05:08:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af0aa469-3cac-392a-abae-c253f64b0101 | -18.04234 | -48.59636 | 2024-10-01 05:08:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ffc27a3c-401c-309e-90d6-550053b31358 | -18.04197 | -48.59993 | 2024-10-01 05:08:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bf354afe-4c02-384a-971c-63238bb00010 | -19.67664 | -48.79403 | 2024-10-01 05:08:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 31da325c-c1c8-31da-96a7-a7fb3164146f | -20.82858 | -49.63645 | 2024-10-01 05:08:00 | NOAA-21 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 12c00c37-910e-361d-af0a-a4acb35c369d | -20.82329 | -49.63575 | 2024-10-01 05:08:00 | NOAA-21 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 175b8a92-be5b-367b-b7c0-e509253c5336 | -20.65672 | -48.7721 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3a717ce2-5cd7-3954-87ff-82de863ea76c | -20.65596 | -48.77972 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8da2d2b1-6f00-3b70-8c03-9774fa4420c0 | -20.65562 | -48.76967 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e13f4157-72ee-3415-95a0-75795e34dae2 | -20.65115 | -48.77136 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f1ba275d-ed1c-31e5-b3e0-b638e98cf959 | -20.65077 | -48.77516 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0b85ef60-7158-3a30-aa7f-fe4fcaa0d249 | -20.6497 | -48.77271 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 367ea23e-6850-37e1-b833-a113fa4c9bf2 | -20.64747 | -48.7514 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7fbbf921-a293-302b-a3ac-9bb6c6c244cb | -20.64626 | -48.74869 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a7197c9e-99fb-34e2-8d31-8ef35a7e8b92 | -20.64588 | -48.75277 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 571097ff-dcb9-3aa5-800f-077901fd3b0b | -16.07345 | -50.38055 | 2024-10-01 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c4d5daa8-5fab-3d53-8f5f-a528b2fb3e54 | -20.6419 | -48.75061 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 91f1529c-15d2-3729-bbdc-a94b6a5e62ab | -20.6415 | -48.75469 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 6fa06a8b-ad3b-3350-8375-59f96830ba7b | -20.63593 | -48.75393 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e7a6bbaf-51db-3277-ac73-b73a508c040d | -20.63554 | -48.75785 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6a03098d-0033-3555-b6c0-7ca5677e749d | -20.63036 | -48.75301 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5b8ca14b-972f-3dc4-9412-a33707d43f5f | -20.62998 | -48.75697 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a1f498ab-1c8f-3852-931d-70eb51431a92 | -20.62959 | -48.76088 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c6a7d637-de4d-38c3-824a-1a61c1dfe074 | -20.6248 | -48.75214 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0f01e87d-03c4-3aac-b9ac-550388ea09b2 | -20.62442 | -48.75606 | 2024-10-01 05:08:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5387afc6-6ebd-31a2-af65-e4022f08f253 | -22.37935 | -49.31216 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5fa7c8e9-5a19-31e7-a9be-c8c882899b1a | -22.37897 | -49.31623 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8068cd61-254d-3470-8c59-51f6e2a1706c | -22.37718 | -49.33513 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| e41e1ab5-be5e-3179-aa2c-5ac0afd072c3 | -22.37682 | -49.33893 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 104598f7-75d9-3b3c-9abd-0691f16ff1f8 | -22.37646 | -49.34277 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| c815f546-561a-36cd-8d2f-cc69ce4bdc37 | -22.37461 | -49.30334 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| f0a6802b-3bf1-370a-9a38-1182d3a8ab64 | -22.37425 | -49.30728 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 73d2fb4a-f944-388e-b83f-c1ee7afabd90 | -22.37387 | -49.31124 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 97caa17b-9d2d-375e-8283-7f033fbe7039 | -22.37349 | -49.31532 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 4ddba907-b200-365a-84f5-a124ea701dbc | -22.3731 | -49.31945 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 2f9c9892-600a-365b-a252-b40e807c2101 | -22.37238 | -49.32714 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 0efa08ab-c61a-3092-9116-720c131b3249 | -22.37203 | -49.33092 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 72f437b9-f07a-3602-93e5-a2b35bc12cb2 | -22.37167 | -49.33469 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 7be94e98-e0c6-3b9b-905f-cabda39c29e3 | -22.37131 | -49.33851 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| b5f10542-b2fe-3e74-9244-dbc2059dd11c | -22.37094 | -49.34246 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| c423b3bc-3c0c-3568-8a28-d15db2405e5f | -22.36912 | -49.3026 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| a5742eaa-dfb4-37f1-946a-14da202df752 | -22.36875 | -49.30655 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 2acdd548-1be9-3320-b582-d0d81e3ea4b9 | -22.36838 | -49.31053 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 012bbf59-b005-380a-aeb4-035e43660277 | -22.368 | -49.31456 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 72e7a6b5-917b-3bfd-a2aa-68c75bee47cc | -22.36762 | -49.31866 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| e7dc6ee5-8957-307e-98f4-1fbe6265caee | -22.36725 | -49.32263 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| c29d0e1f-0c1b-30f6-a04a-d96924112435 | -22.36689 | -49.32651 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 538152d2-28ba-3595-9587-b5b07f59afa4 | -22.36652 | -49.33038 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| b86d7c40-9945-398d-914a-4ef640e78fcd | -22.36616 | -49.33427 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 41c905d0-95da-3ca1-89b2-54d36e4e7d86 | -22.36579 | -49.33815 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| e219ef89-3399-3755-91da-e90135431a08 | -22.36543 | -49.342 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 2eee321f-dff3-3856-bc13-03bb56a0af60 | -22.36323 | -49.30608 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5c098015-58ce-3430-91b1-f9aec1a778c8 | -22.36286 | -49.31004 | 2024-10-01 05:08:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c2b4939c-d117-345a-873e-3e30a0ac8675 | -22.3625 | -49.31398 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 12387ae3-f2b6-3bea-88d4-3f8574e2a32e | -22.36213 | -49.31787 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2f08fb47-f777-3235-94c1-a81a9b316553 | -22.36177 | -49.32179 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 65721cab-8514-3744-bfa2-70552852a8cc | -22.3614 | -49.32573 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| 4871592e-1413-30d0-badd-03fdfb1ecb5b | -22.36103 | -49.32968 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| 798d8590-61df-3d8f-83d4-513c46e9e7a5 | -22.36066 | -49.33366 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| a0b467ce-65bb-3ad3-b4fb-2d07a6656b29 | -22.36029 | -49.33761 | 2024-10-01 05:08:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 26212f69-3bac-3aa7-afe8-bf38e8b6a165 | -21.38145 | -48.47095 | 2024-10-01 05:08:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a3d3ae8-61af-3a60-b5d9-fea09aeb159d | -21.38109 | -48.4749 | 2024-10-01 05:08:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3653c988-ecd4-39de-99ce-537559407dbf | -21.38072 | -48.47887 | 2024-10-01 05:08:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README127.md)
