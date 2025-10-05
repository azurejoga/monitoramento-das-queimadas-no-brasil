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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76ee22ea-9fdd-3702-8554-e80f1ab7c5d6 | -14.67744 | -48.36742 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 02b3b5b8-546e-3416-b505-763063f04c45 | -15.78023 | -49.09029 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70ab67a9-c7e7-3334-828a-fe346bd9bc8c | -14.92299 | -46.85815 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0a1c49df-601a-3aec-bc69-f9eed296def5 | -17.99514 | -51.63403 | 2025-10-05 04:49:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17fcbc54-2e17-32da-a453-f8cc869fee62 | -14.65941 | -48.35384 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 392a1fba-1dda-3256-85ac-80e127e321d5 | -15.77239 | -46.2593 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84c8a3ba-efaa-353a-ac50-39931d27c851 | -15.54776 | -46.81649 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26044bf8-525d-31f6-a346-0a35a332e5f9 | -16.15722 | -57.56938 | 2025-10-05 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0e459793-a004-3ea1-a037-237efe66ac2b | -15.61248 | -46.9462 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ac17624-0fae-30c5-bb57-0b3e88aca7d2 | -15.23788 | -56.76848 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38969930-7f82-3e8a-ba9b-cf354e24e1ff | -15.36399 | -47.98292 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 029dab52-531a-390d-89d7-61bd3ca58aff | -15.57288 | -52.47025 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a62d7e11-5199-3580-8ddc-fb7e0440de68 | -14.01314 | -48.21375 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd80ec5b-4be3-3448-9b7c-cfcb2e2b08cd | -14.58606 | -52.45269 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e29daa9f-43e4-3eb9-a47b-644befafee39 | -12.91992 | -54.73148 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffd7d89e-637c-306a-8e54-e9b30a8bf6e4 | -15.20801 | -46.38765 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a920670a-e131-3493-9589-9e95d47a7448 | -14.32598 | -47.70255 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1ac0158b-84d3-3689-bcff-208d00a6f9b1 | -15.5515 | -46.85675 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb83746f-717c-37e6-b376-b24b7cf1f2bc | -14.95076 | -46.84695 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e852509-5286-33f6-b56f-eb39d010912d | -13.73218 | -48.07657 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 34ccc7e3-db9c-3b53-90a0-5144821c8f46 | -15.30407 | -47.96013 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51b71612-1914-3a66-9682-e022bcb94262 | -18.23303 | -53.34407 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8048bfc5-57d3-3657-a4c3-48bbe6f7bd5b | -16.36969 | -51.47005 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16b4ed40-58b7-372f-8ba9-46434903f9ce | -16.06337 | -50.90725 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 359cd560-7d53-3d58-acb1-6bf45dc50f68 | -14.58165 | -52.45929 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a81ae715-0da7-39ae-9d3f-d420459921ac | -16.66176 | -49.1677 | 2025-10-05 04:49:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b8910cc4-19fa-3894-a4a3-5a69bd54535d | -14.58937 | -52.45323 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6a3d3128-03b4-3a11-b999-d26a30a792d6 | -15.59114 | -52.50649 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cd473785-e40f-353d-b7eb-1bad84fa8ae5 | -14.7605 | -54.65573 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a504359-f0b4-3d6f-b90a-6836c97ffa77 | -14.87473 | -48.15163 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3d040f6-0e62-3e64-8759-8789904d5137 | -16.91774 | -52.04921 | 2025-10-05 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cabca764-eff0-3f32-a3b5-4f1c45a13bae | -14.65617 | -48.34142 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b93eb3b-a90a-3970-ab09-1ee5862bf901 | -16.08657 | -50.91841 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 582e9a55-c1c2-3655-8f31-17980a44fa6f | -16.22393 | -47.4576 | 2025-10-05 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c375717-45c6-3162-8bc0-7e3e2bdc20c7 | -15.34671 | -56.94563 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fcbd6bb4-6bfa-3a46-8c46-bfcb3af1dd67 | -14.66325 | -48.35485 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce2937fa-eb5a-3ad9-9017-66912c51d847 | -14.92834 | -46.91744 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9cd2a69-8615-3feb-bdfd-301697bd403c | -17.87938 | -57.63665 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9c6eb661-8873-3d6e-903e-c730740ad670 | -14.91665 | -46.87314 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dd38ae1-7ec6-391e-bdff-85c82af1190c | -15.52804 | -46.86778 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13f2dac1-ea9e-386d-877a-4caae5b8dccb | -12.9246 | -54.72442 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c7fc819-cb3c-3c05-88b4-8415939229d2 | -19.83662 | -46.52362 | 2025-10-05 04:49:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1705ee85-554a-344d-a58a-de3081457339 | -18.17621 | -53.36057 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e31f1b7-a94a-3d7a-be97-338e7be6f9f5 | -19.94758 | -44.63688 | 2025-10-05 04:49:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 2553eafd-418f-3b97-b3be-92d2ae7c901c | -15.54924 | -49.28079 | 2025-10-05 04:49:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ee1a55e-6102-3bd8-85cb-0dde49f18f67 | -17.88164 | -57.63485 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ee616c14-9853-3cda-bcd4-c07c47337b03 | -16.34186 | -51.46957 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c5a5fd09-4a35-3eb7-8d5a-fc974af1cd54 | -14.88101 | -48.15956 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4e596997-3853-384e-af9c-a57b241fce92 | -14.69067 | -48.26871 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fed243c0-94ac-3e3c-ba8f-a205e1cfdeec | -17.88074 | -57.63978 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 81d3e4f3-6f49-3d27-b938-b04fdbed1baa | -14.95019 | -46.8513 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4311a39-3a62-3048-bb24-407d13427e12 | -16.05244 | -50.9338 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9900fff-dde6-3c4b-bddc-c15e1fdcbbae | -16.01311 | -50.84782 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 574a292a-af5e-3c65-9add-d947e4710c55 | -18.22581 | -53.36886 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd31a691-8c1d-3730-9648-5de158d60112 | -14.3233 | -47.69175 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ab6f3eb-4cdb-31fe-bef0-287b0d4da575 | -18.20103 | -53.35352 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2669beb-9823-3187-a560-deb67ce58b5b | -14.69027 | -48.30152 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bbb0fc2-20ce-3d98-98ed-111fde8c1ffb | -15.29823 | -46.30782 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2eefa8bd-6f45-38cc-b28a-eb5a65e2276a | -18.20761 | -53.37691 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fad30829-431f-3362-8224-9507eb51e01a | -14.33486 | -47.69768 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8bb06ccd-7643-3af8-b9bb-144a8d513981 | -12.94759 | -54.7319 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 310a995e-eca9-3369-ab29-ef0da3ca9e1c | -18.14401 | -53.34812 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef729cc0-6d49-3062-9147-0bb8dab2d5df | -18.18999 | -53.35911 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8d6a6d03-11c9-3428-ad87-9a02f7f96f24 | -13.72108 | -48.0998 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40d98358-77a4-30ef-908d-ff7d4d36620c | -18.17844 | -53.34604 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64b432ac-8238-3694-a0cf-f0e0adf563c2 | -15.37248 | -47.98061 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa3991fd-fe99-3bcc-8762-036eef6683df | -13.7429 | -48.05623 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20adee6e-278b-37a9-b640-a12cd59f0193 | -14.33001 | -47.70318 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5bebe17f-3b0d-3159-8d06-efd259791e70 | -15.3905 | -47.96835 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79674479-18cd-37ea-a4a0-23cbeadbbf3c | -17.88442 | -57.64059 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 37f0e2a4-78e8-3b42-a3a3-9251b22b1d0b | -14.82302 | -54.7701 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a39a046-e322-366e-97d6-b7c5e25275ae | -14.98252 | -49.9971 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 673b56de-a1da-39bc-ac8d-45cba3d8aedb | -17.20508 | -44.44556 | 2025-10-05 04:49:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e83c1ba2-183a-34dc-a369-dffd516a9b02 | -14.74109 | -54.62579 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fafd060-11cf-347c-bf81-680f9853d650 | -17.8469 | -57.6255 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d2031cac-b3b6-3dce-8e5d-037cb21c95fd | -17.91817 | -57.62312 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f1a62c40-1261-38da-8341-8c0bb0c7acc4 | -16.07558 | -50.92083 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43ac24f8-3b25-361c-9d92-61317a2331c7 | -15.9865 | -50.85978 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e658fb86-c71e-3937-8cfd-e073f4ce366e | -16.88244 | -49.39306 | 2025-10-05 04:49:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73d1407c-c026-33ee-90ea-23c35ccc9063 | -14.6688 | -48.28337 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52683151-2f33-361d-a900-110587ca5d2e | -14.75435 | -54.65082 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1326d20d-6518-37cd-8295-9a6e9db0c5ed | -17.32146 | -49.37123 | 2025-10-05 04:49:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfe416ad-a4d0-3d3c-ab25-c77075b10fbf | -13.74149 | -48.06668 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44585186-695f-34c5-bfb0-5da396b3524f | -15.53957 | -46.81121 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87b2c3b8-29c3-3177-a8bf-082d64183842 | -13.73557 | -47.96504 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b7593666-f622-3313-aaf6-2bbf4494d0e8 | -16.08078 | -50.90944 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77f12d7b-448d-3cf6-8e57-3d1c12332d09 | -15.60218 | -52.50098 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6883a864-27ec-3b63-9c06-0c1e8f965a35 | -17.88255 | -57.62979 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1d4c9919-3e48-3b44-895e-703a4c930076 | -18.24899 | -53.35056 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ef9cdd3-3a31-398b-b925-33c145d6d97e | -13.69199 | -48.04763 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db87d8e0-28dd-3378-8480-04f5d5fb4ea5 | -14.88307 | -48.14377 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 004d6362-1304-3ced-b9c2-79ba60cea147 | -12.91711 | -54.72707 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0515217-d1dd-3098-ae58-c8aabad17e46 | -15.8149 | -46.25097 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc075dc3-5345-347e-9588-b60464e0864a | -15.24015 | -56.77724 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e5f0664-1f31-313e-91de-126c05894679 | -14.01 | -48.21466 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0e8bf0b9-8829-3e06-9e9f-f74c25dc40c6 | -14.42441 | -54.94781 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07b7c10e-3dcf-3394-be5e-897af284f6a1 | -15.38582 | -47.94139 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dda46c58-8dd1-339a-b1ca-624d1d02c457 | -15.57784 | -52.46007 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb1763e1-5f9f-398c-84df-cf5febfbc622 | -18.31429 | -47.44227 | 2025-10-05 04:49:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38e18a58-8132-333b-aa0f-5224ead68f90 | -14.05262 | -49.14429 | 2025-10-05 04:49:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README108.md)
