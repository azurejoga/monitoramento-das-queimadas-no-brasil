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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69682b89-a581-377f-a67e-85c424ed3264 | -16.288 | -45.24667 | 2025-10-06 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56971348-68ac-3e21-8d63-d609cdc5ae5a | -14.92026 | -46.82608 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1762a2e5-50de-38e6-a120-f7c5e51c9ac6 | -15.51732 | -47.3456 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f3bebeb-1a7a-3185-9340-d5d08583141e | -18.87214 | -48.61047 | 2025-10-06 03:38:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f19a0a35-1686-3cda-950f-57ea37b773df | -15.57607 | -47.28082 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d585efd4-8ef1-348f-9cae-f618507e3d1e | -14.55538 | -46.66052 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd5d28b6-b5a3-3ad0-8515-3ec681406eb8 | -20.05848 | -43.42 | 2025-10-06 03:38:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aecd8e5f-5c85-3e72-8217-3d88f140a168 | -14.91428 | -46.8337 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f24e9142-9a46-3649-b885-abb6c5db9720 | -18.02194 | -45.00162 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c39e48e-b5c6-3668-806c-2ebb3478b575 | -15.67554 | -46.28414 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bf8437d0-9d55-35dd-a8be-1aa91cf06cec | -14.67376 | -48.39809 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 16212540-80b0-3b71-b0c4-28c7a0fa47b3 | -15.14603 | -45.72269 | 2025-10-06 03:38:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35d63f2b-ec11-340c-9d18-6b75003810ab | -14.91266 | -46.86284 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a56f6ffa-4b8a-3985-b997-44eaa381db05 | -14.93684 | -47.14325 | 2025-10-06 03:38:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f85da71-eac7-3a67-a015-3582896775ef | -21.40188 | -45.06124 | 2025-10-06 03:38:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| cc4e98e5-647e-3d7c-86b7-6aa62d60528b | -14.55346 | -46.66962 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 423c3cee-e37b-31b9-8dbd-a48becb05e63 | -15.72986 | -46.28577 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3557eb0-271b-3bb5-9bcf-68b63511d6b3 | -15.92231 | -48.62016 | 2025-10-06 03:38:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c8cdd24-bbf2-332b-bda3-b6705e6fdaa9 | -21.38303 | -45.05656 | 2025-10-06 03:38:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3f6f542d-0707-3845-bccd-5de6f8b23145 | -14.54385 | -46.9552 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c686440c-16e2-313d-834c-9c0272b501dd | -18.51466 | -43.91913 | 2025-10-06 03:38:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6de3c98-aef0-3abd-9f83-85bb39d4c2b5 | -20.11495 | -46.3567 | 2025-10-06 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1789d7fb-372c-3136-b1a2-7d3bf3f1e43a | -18.02584 | -45.00084 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aaf67390-e9f1-3c9b-a0c8-8aed361708d9 | -15.64881 | -43.67492 | 2025-10-06 03:38:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63f43351-31b0-3c28-9fee-1742e72f8917 | -15.15698 | -45.74417 | 2025-10-06 03:38:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5644476-640d-3201-90f8-381f4f2612cf | -14.67881 | -48.4064 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 39e85904-a044-3e38-a2a3-49fb65c7cbe5 | -15.8797 | -46.2588 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b25aa8ce-a895-3a13-84b8-1f0d8c8dfe6b | -18.51369 | -43.92404 | 2025-10-06 03:38:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43fd8224-a7f6-3c5f-84d9-3a9c152cdc31 | -13.36187 | -48.04649 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4db942e2-d292-3668-b16c-fdd93b732b15 | -14.68692 | -48.40096 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2063db14-d8b5-3f6e-b4ef-25af767e898c | -15.92262 | -48.61359 | 2025-10-06 03:38:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bd3d3ff-0ea2-3706-b6bb-2e520ebdc7e0 | -19.10647 | -43.61179 | 2025-10-06 03:38:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c764c12c-d58f-3bf6-9e1c-52411859f70c | -21.39021 | -45.04512 | 2025-10-06 03:38:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| ebff6506-5653-3252-84db-9cb163486f4e | -20.7882 | -43.31881 | 2025-10-06 03:38:00 | NOAA-20 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 39cf0a2c-a165-3db4-9fe1-475383b7a880 | -16.28871 | -45.24321 | 2025-10-06 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d961aead-51d6-3a0b-89c2-f9bfd764fecd | -13.49185 | -47.24642 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef25f03a-ebf5-3bdb-a6e8-66d27975f0ac | -14.53581 | -46.96334 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efe0b43b-5fbd-390a-8f52-2ad31d166509 | -13.24783 | -48.46655 | 2025-10-06 03:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d36794b-e160-3b60-9d20-0f2fb687e384 | -15.4385 | -45.87167 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f263cdad-a7f7-344f-b3c1-6b814719e5be | -14.69213 | -48.37745 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fd09c5b-8174-3eca-9a22-e2236773720b | -14.67927 | -48.38298 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 54a6b451-7919-3d0a-862d-3e41bc0d8fee | -15.55946 | -46.84342 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d342cb9-77fd-3e1a-a727-3f99edaf8e2b | -18.39329 | -45.21241 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 71e6a324-c67a-341a-8f0c-4ae705b0d18c | -14.9177 | -46.86873 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3de25657-efbd-3f71-a3b1-09d2ca421e85 | -13.552 | -47.24104 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad6bfb8e-1050-365a-a481-ea04804fe32b | -14.32309 | -47.658 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e13eb52-8158-3884-b60c-d97ddbabfe3b | -15.90743 | -48.83271 | 2025-10-06 03:38:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd05b148-0319-3e4a-bd87-597229536b37 | -15.74627 | -47.69971 | 2025-10-06 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 74fa2cab-c5bc-3665-92e1-778a10e23921 | -15.5548 | -46.8361 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 094c109f-705e-38e1-bd73-686b16ed9406 | -14.26587 | -45.85677 | 2025-10-06 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 759c92ba-0a72-340d-b694-a27256567cda | -15.35085 | -47.99334 | 2025-10-06 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cc929ff-6b5c-3ce8-a145-932c0f38e809 | -18.01207 | -44.99837 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9809d6c0-c19f-30e7-b302-00eafe9116a0 | -15.92366 | -48.614 | 2025-10-06 03:38:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b55a7650-8f2c-3f02-bc45-239ea5a295d6 | -18.27455 | -45.42468 | 2025-10-06 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1321519-f211-3835-b2fc-b02a2a1e5f9a | -14.65911 | -48.38073 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aab907fd-03b8-3636-b2b4-574ed9b05e8e | -15.74706 | -46.26048 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 305df4d4-2314-3eeb-83c6-87ee4ce01c81 | -13.35392 | -48.05128 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc557171-3734-32b4-b15e-4962e28c6dd8 | -13.3602 | -48.03493 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 308c361a-f031-33b1-a15f-36a41fbc90f0 | -14.54285 | -46.95999 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 592c46ce-cef0-3e3b-83e5-71fc73b5ba18 | -14.5504 | -46.65464 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f798b580-c29d-3eb4-ac38-d79919cdc186 | -21.13315 | -45.11324 | 2025-10-06 03:38:00 | NOAA-20 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 47048abf-4974-378e-a19a-db002b1ba7d9 | -14.68435 | -48.39138 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2cd62b5-1d66-3197-8b1d-93501a13ac40 | -14.92799 | -46.82805 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4a50747e-6a43-3dd2-ba7f-f5087195cf39 | -15.3386 | -47.31886 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb1f7f92-eea4-39ee-bd78-05d0a7c9f707 | -13.36849 | -47.57864 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 631c499e-6177-3168-b80a-22fbf2035442 | -20.26917 | -43.63909 | 2025-10-06 03:38:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c5f8d880-087a-36fb-a033-4c740053c292 | -15.24022 | -46.66913 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32f17f98-0d05-3b37-814e-bb557bce4e9e | -15.93057 | -48.6087 | 2025-10-06 03:38:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd620796-4cfb-33fc-aa5a-a2b67c9bea8b | -19.62447 | -45.92052 | 2025-10-06 03:38:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6839c9b2-e7aa-309b-bb7a-8a47417e0344 | -20.34846 | -44.09101 | 2025-10-06 03:38:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a8ad89ec-166e-3600-9bb2-eeb53e2c38c9 | -18.26938 | -45.42362 | 2025-10-06 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8a10889-d622-33c6-925f-a9ef824bca46 | -18.29045 | -45.42587 | 2025-10-06 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c47fa16d-589c-3aa3-9c78-e33ff5e50138 | -19.93569 | -44.63915 | 2025-10-06 03:38:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bf24c305-228e-3d16-b870-1c788aa18483 | -13.37506 | -47.57933 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0cf73216-81dc-327b-9436-afa94026e1f1 | -18.81931 | -44.47376 | 2025-10-06 03:38:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9af458c-2cca-354e-ac1b-dbdf64ccd0a7 | -15.36125 | -48.00668 | 2025-10-06 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9683511a-8be9-3158-a24b-07b51ca45d8f | -21.39013 | -45.04642 | 2025-10-06 03:38:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 0b2df287-dab5-3d41-9217-98225aa73f67 | -14.93176 | -47.13717 | 2025-10-06 03:38:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d983cee-f7a4-3445-ace1-9271f266e713 | -20.49978 | -46.99619 | 2025-10-06 03:38:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f89d2f41-c0ea-3fad-8aa5-0100d021c154 | -18.53744 | -48.2579 | 2025-10-06 03:38:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17792819-9b1e-37ca-9e2d-875961b51380 | -16.32846 | -41.95312 | 2025-10-06 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4e41df15-da32-3495-8447-9caddeb74fe2 | -18.39136 | -45.22191 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b2f979ca-9e82-3087-926f-0537b21c7c69 | -13.3272 | -48.06051 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2ce5be4-8ae3-36ef-9443-3d13859a638e | -19.93443 | -44.6452 | 2025-10-06 03:38:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| b777c428-8aec-3f59-9153-0d19ecbe0613 | -21.3914 | -45.08745 | 2025-10-06 03:38:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 727e7097-f748-37a1-997c-eedbfacae3b3 | -14.56535 | -46.67233 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d126f13b-ea84-3816-aada-63b34784f029 | -21.18501 | -45.61753 | 2025-10-06 03:38:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7c94e62-096d-3a33-8c8b-2aa42feb245b | -13.71995 | -48.07795 | 2025-10-06 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39c8a390-27f6-36d8-8c0e-98bf34806569 | -16.32767 | -41.94693 | 2025-10-06 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 97b72373-d625-3f9a-9daf-8da37b2ecba5 | -13.60674 | -48.69916 | 2025-10-06 03:38:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93bd1e30-0bf2-3ac5-8240-a0e68b3cfb12 | -15.35082 | -46.05219 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99fe1f3f-6a18-36d9-8d74-a7f3f3a29bf2 | -15.25962 | -47.15134 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5787c596-b529-38c4-816a-8e52941c1a9d | -21.18923 | -45.15178 | 2025-10-06 03:38:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2c7f3d48-03ec-3798-a608-9b763889fc0c | -21.10775 | -44.20889 | 2025-10-06 03:38:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c1ebc512-e360-3128-acf1-859c3c2aaf1d | -18.8134 | -44.47817 | 2025-10-06 03:38:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86f4fbee-a02e-353e-a9b3-963ebdad9a64 | -14.70964 | -48.36051 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 96029dae-37a6-3e17-ad9f-1858dfa9f850 | -15.31929 | -47.31945 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b49a9f55-18f3-3eb1-8551-2d70f696c904 | -14.30665 | -45.86088 | 2025-10-06 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8704054-839f-3ba3-be02-d58e4df02e6b | -17.66313 | -44.43995 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6874de2-32d6-3294-9421-2f952f27d19a | -13.35676 | -47.57078 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README19.md)
