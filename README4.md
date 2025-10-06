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
| bca1edd5-1dd9-3ddb-86cf-12187329348d | -13.08267 | -47.84247 | 2025-10-06 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| ed33e9cf-5499-33d9-a732-076d72a82769 | -17.95494 | -57.59239 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 135373bb-7b86-3e5f-bac5-11f1441b33cb | -18.11808 | -53.4085 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 28.3 |
| f875ff16-d16e-3496-a132-51a87619edc0 | -14.90854 | -46.83008 | 2025-10-06 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| dbe8af85-2de5-3441-984e-125d427040c9 | -14.65587 | -48.36153 | 2025-10-06 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 36.6 |
| c249c28a-68d5-3abd-8e43-cc0fda0997f1 | -15.99258 | -56.00468 | 2025-10-06 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2077759b-4252-35c7-a764-be5f18a11781 | -18.00232 | -57.59813 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.4 |
| f43a7a52-62f8-348c-942d-52b6126b4f47 | -15.99397 | -59.53685 | 2025-10-06 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5fb22ab4-47b1-37cd-9d07-f4e960fa1090 | -17.84006 | -57.62493 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 60624d3a-b89d-3706-bcb4-376fa78add08 | -15.22491 | -56.82441 | 2025-10-06 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 90be5911-e648-38a6-88d7-1fa468481f0b | -17.98168 | -57.58841 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 66d50cdf-9b26-3ed2-9967-acf98a92fe0a | -14.89682 | -51.51088 | 2025-10-06 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 48f10674-ee11-393d-9e93-81a01f473e40 | -18.17348 | -53.36891 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 0e9b29c5-797f-3f2a-980d-c46500609521 | -18.25259 | -53.34954 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0488001d-fd9e-3958-b8c3-d5e0cb66a0eb | -17.67518 | -52.25421 | 2025-10-06 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| afc1dabf-c2c7-3b92-b211-e484b88468c3 | -14.67694 | -48.39038 | 2025-10-06 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 64ac4f0f-3882-3f13-83ad-21ce081c4781 | -18.13766 | -53.3999 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 693b04a0-b050-32a8-8cbb-9ef71ffbaf04 | -14.99952 | -56.02516 | 2025-10-06 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7dabf83-7415-37d1-978e-97b8465af845 | -18.11584 | -53.39066 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4bc039c9-8e2a-35f9-8a5c-fd7624f737c4 | -17.95622 | -57.5345 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| f988f7a6-ea38-356b-ba48-2f91c648443c | -16.0631 | -50.93584 | 2025-10-06 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 3d411588-0277-34b8-a730-af43f40338ca | -15.61967 | -52.53971 | 2025-10-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b65b6b52-ee7c-33fb-a2f1-1e978d9f2707 | -17.38815 | -53.59801 | 2025-10-06 01:09:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3d3b4272-b924-3e09-9b9a-5ab5aede8a86 | -17.96512 | -57.53318 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c703c903-ef22-34ed-955a-ea75507327f3 | -14.73924 | -54.64582 | 2025-10-06 01:09:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 549e6151-9c7a-3653-b241-a3bcd155e589 | -16.01186 | -56.01128 | 2025-10-06 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| a924d399-f631-3d09-a53b-bda6e1344589 | -22.07486 | -54.13308 | 2025-10-06 01:09:00 | TERRA_M-M | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 946412d8-c3d2-3c15-8c43-bc9c232d1b6b | -18.1034 | -51.84409 | 2025-10-06 01:09:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 29125480-1bc4-3c4b-a2d9-a1825b77e0c4 | -17.89863 | -57.65466 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a9b21ac2-8924-3161-aecf-a4b8a6b788f6 | -17.96513 | -57.60049 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| e5a5fab9-16a9-3694-9b46-16c0fce39e72 | -17.97531 | -57.60859 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 8067e874-d411-3768-ba3e-73f818c34af1 | -17.93838 | -57.60444 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 65d8595b-f79e-3705-858c-8b99594385d7 | -17.92053 | -57.60693 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| f3d0f2e5-560b-38ad-a822-9bcbaa31ae54 | -18.25067 | -53.33727 | 2025-10-06 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 499ebcab-3e92-3ce9-aa7a-de95b3db96d3 | -14.92654 | -46.83157 | 2025-10-06 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b54b994b-e9d3-30e3-bff2-a90a07ddb8cc | -17.87059 | -57.58173 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 47f7c327-4042-304f-bc09-4be2a98a0244 | -20.8239 | -50.15565 | 2025-10-06 01:09:00 | TERRA_M-M | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.9 |
| f9c376ce-7bbd-3caf-b787-2565eab42dfb | -17.87189 | -57.59129 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.1 |
| 23928527-12d2-3ef8-9eae-8677484bec68 | -21.49862 | -51.56426 | 2025-10-06 01:09:00 | TERRA_M-M | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 3bba72ee-7a82-3d75-a887-0d9f2eb72649 | -18.28048 | -53.33249 | 2025-10-06 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 963b9880-a30b-38d4-a8c1-dafe6d94e103 | -17.68593 | -52.25208 | 2025-10-06 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3cb720c8-641b-3106-b5e2-1addfdf94ec3 | -13.60871 | -48.69316 | 2025-10-06 01:09:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 28.3 |
| e8053256-cda6-3208-aa03-9114e655892f | -17.9934 | -57.59946 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.0 |
| e5750523-4fe3-3235-8675-0df01cd160bf | -15.1886 | -56.83595 | 2025-10-06 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0b3268b8-de70-355c-99b0-8f9f58444752 | -17.92945 | -57.60572 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 3cb57f0b-772d-3672-80a5-a60d6f8e9a9d | -14.61047 | -52.50789 | 2025-10-06 01:09:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 52361a61-c303-3bc7-b1d4-6ca042c48a13 | -18.27866 | -53.32074 | 2025-10-06 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 77d9a8c7-30e7-309d-9a25-17d99c0177d2 | -14.91834 | -46.86289 | 2025-10-06 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 42.0 |
| e77d2ad1-84a2-396e-bea1-76f1f9ef6370 | -14.64694 | -56.01066 | 2025-10-06 01:09:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b6fd6670-87dc-3bad-b0ef-51b83a5cb8b5 | -15.35397 | -48.00056 | 2025-10-06 01:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 8f10ad38-cf9b-34b0-b12b-32902de22baa | -17.99466 | -57.60889 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 65010860-ae7a-32f2-adc7-004fdcb135e1 | -15.23876 | -56.79451 | 2025-10-06 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5638a352-7d7d-38e5-b2e3-4ef71c5669c1 | -17.98708 | -57.55191 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| 6b679011-5072-385a-8282-0009561288ce | -18.1259 | -53.38988 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 20c50418-e2e9-3ffb-b402-14deba9741bb | -14.54948 | -46.96742 | 2025-10-06 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 19157927-2903-30ac-b278-5d132bf47d3a | -17.85148 | -57.64234 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.0 |
| cf3d3946-9ec6-3e56-8503-536626fe6b91 | -14.68812 | -48.38141 | 2025-10-06 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 464ebd2a-98eb-3199-b8e7-fbd8275a6ce9 | -15.99784 | -50.85027 | 2025-10-06 01:09:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1d733b9c-24ba-3443-ad34-6243edc2492a | -18.26873 | -53.32237 | 2025-10-06 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b6290803-8c63-37f3-9c4e-d113c6dd9495 | -14.84923 | -54.2243 | 2025-10-06 01:09:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 9227bda9-e86e-30d5-bc25-1ccb598a284d | -16.0132 | -56.02072 | 2025-10-06 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| b667c8d7-052d-3a45-9ddc-6e18eff25d72 | -14.75553 | -54.68825 | 2025-10-06 01:09:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 571c484f-0961-3e46-a20b-4aad1cdc06ad | -17.9715 | -57.58031 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 82e08cd9-2c12-39dd-9d0e-05443d1b10bb | -20.1166 | -46.36314 | 2025-10-06 01:09:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 6adab1d0-c565-38c3-a56a-f27403812b18 | -15.98362 | -56.0061 | 2025-10-06 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ae237a30-1bee-3ff0-b41f-165e61c25365 | -15.21607 | -56.82576 | 2025-10-06 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cdb36b31-f2f9-39ad-9ee4-241a42aa866c | -18.11769 | -53.40224 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 55fb5741-711e-3d2e-ac2e-948d2977efc4 | -17.37826 | -53.59971 | 2025-10-06 01:09:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b9c01445-3b8e-3847-ad47-adc567541724 | -16.00208 | -59.5252 | 2025-10-06 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9d4d80b4-e6a2-3669-9c15-138623edd3e9 | -13.27697 | -47.8452 | 2025-10-06 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 5df10a7f-2adc-33c8-a40d-742c266fda9c | -18.2706 | -53.33447 | 2025-10-06 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 19.1 |
| f672625c-e5d6-3e07-ad95-20df37002798 | -18.18329 | -53.36649 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 954dd178-6f06-3f04-843e-f846fbfecc36 | -20.62825 | -51.46459 | 2025-10-06 01:09:00 | TERRA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 8e0b7ebd-6dab-3e0b-88a4-26546c38c005 | -20.10873 | -46.36036 | 2025-10-06 01:09:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 52f9aa5c-0729-3eff-8849-6b713f538b4e | -17.9218 | -57.61648 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 666908bb-95b4-3f2c-a194-2797d5d82928 | -14.88178 | -51.49519 | 2025-10-06 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5f9d28b5-8074-3a20-8770-2f03368ff205 | -15.18732 | -56.82686 | 2025-10-06 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e18423e7-2651-3767-a700-47ac0c4f2204 | -18.11991 | -53.42041 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d1772c7f-9da2-3576-ab73-93e4a63b02ba | -17.9676 | -57.55165 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 10b740f4-2d62-3c50-873d-994c10609023 | -15.9086 | -59.51238 | 2025-10-06 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7f750e8c-3ab8-3fc9-87ad-31fc36da856a | -17.6729 | -52.24036 | 2025-10-06 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| d0238f10-831a-3e5f-bb2b-d800a9c1c559 | -17.84128 | -57.63405 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.4 |
| 24c9c685-073d-32d1-9c6c-2e898dd6dfb6 | -21.93334 | -51.8326 | 2025-10-06 01:09:00 | TERRA_M-M | PRESIDENTE VENCESLAU | SÃO PAULO | Brasil | 3541505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 728b9ed3-81ae-30f8-996a-bba2f59a9033 | -16.01035 | -50.84862 | 2025-10-06 01:09:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 34d7a5a3-a67b-3c7b-a4c2-190b1d8b88f5 | -13.26607 | -47.83977 | 2025-10-06 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 33c8edc9-964a-3a9c-81ae-0091aa17b0fb | -21.70162 | -50.09689 | 2025-10-06 01:09:00 | TERRA_M-M | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| c5326fef-d7ee-310e-9cca-f5fca2692e27 | -14.62649 | -52.53605 | 2025-10-06 01:09:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 986a41d6-f4c8-3402-a4ad-1e770d152dbf | -14.64834 | -56.02023 | 2025-10-06 01:09:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3212e4ba-136f-3f3e-a1c0-936d7f61d3d9 | -18.17526 | -53.38036 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 0e600cbc-0c5f-398a-bd01-34e3debeefeb | -17.89735 | -57.64522 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| e3103fb2-325b-3b79-91e8-6f6c30e50c07 | -17.96893 | -57.56134 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 78f3b3c8-e159-3ebd-8b6e-47df2f29b854 | -17.9473 | -57.60314 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| b238d2dd-921a-391c-934a-ff64098d6c6d | -17.94856 | -57.61255 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| bf9966e3-74cf-39da-a382-2e507125c708 | -17.96131 | -57.57216 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| eee7374b-1912-37cf-8e93-c80773005c88 | -14.56479 | -46.6581 | 2025-10-06 01:09:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 44.8 |
| c1566034-ae69-3d8b-8192-d3b70d74cc5b | -15.88165 | -59.37761 | 2025-10-06 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 229ef1e5-71d4-38f8-a9d2-d789f9f483b1 | -17.87952 | -57.64789 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 899e8a61-0dc1-36ed-8c96-7176de3018ce | -17.98582 | -57.54245 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 53fa0c4f-b745-3bee-bfd4-03ed61d2534e | -17.99597 | -57.55046 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.0 |
| c81c7982-0b6f-3ecc-b452-4677b891de71 | -14.86973 | -51.49736 | 2025-10-06 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |


[Clique aqui para ver as próximas entradas](README5.md)
