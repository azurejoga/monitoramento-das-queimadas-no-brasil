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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12389638-425f-36da-9401-48ffd06941ef | -21.65473 | -48.62177 | 2025-11-28 04:36:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d0483f6-19f6-3f52-8f28-8ef5530e2e61 | -20.46791 | -47.47851 | 2025-11-28 04:36:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5f13632-7fad-3edf-a3c8-69d0777f71b5 | -20.45099 | -50.01022 | 2025-11-28 04:36:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2260da1-aad0-3e6c-b28c-c5a2353896f6 | -22.76199 | -50.35749 | 2025-11-28 04:38:00 | NOAA-21 | CÂNDIDO MOTA | SÃO PAULO | Brasil | 3510005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 909856ea-84bb-33e5-927f-95787276f9c5 | -24.62896 | -51.52877 | 2025-11-28 04:38:00 | NOAA-21 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 88d16a13-7524-3237-94bb-aa69280950dd | -22.19601 | -56.01064 | 2025-11-28 04:38:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26b40fc8-9e9f-3259-abca-739df98ce5d7 | -21.99947 | -49.10111 | 2025-11-28 04:38:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 609a03a1-e742-3081-bba2-5ebaae1e9911 | -21.44046 | -54.57045 | 2025-11-28 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f03a1150-c2f9-376e-9d02-75239be56f5f | -21.44403 | -54.57117 | 2025-11-28 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3590e398-31e6-3d7b-ae74-d91e8fcb9397 | -22.47639 | -49.11992 | 2025-11-28 04:38:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 153f8eed-d8b5-3cda-b67f-641dfa3ce64f | -24.62564 | -51.52813 | 2025-11-28 04:38:00 | NOAA-21 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3b7bd23c-0a5b-3429-b0d8-f13efbebfd33 | -27.68652 | -48.75026 | 2025-11-28 04:38:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1100896a-7000-3c40-848a-2a7c79bb98c0 | -24.62955 | -51.52492 | 2025-11-28 04:38:00 | NOAA-21 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 593698d4-8486-3e1d-b53e-b61d84ef0090 | -27.38428 | -51.39798 | 2025-11-28 04:38:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a30159b7-1302-3f22-9b2e-bd47b746a442 | -22.47581 | -49.12404 | 2025-11-28 04:38:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66014585-8068-3eb0-a833-467324685d85 | -21.44124 | -54.5661 | 2025-11-28 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98b361a3-8c2a-3480-aa9c-8d726567e929 | -27.38487 | -51.39391 | 2025-11-28 04:38:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 915fe0d8-5a9a-3ff7-a0a0-111bc09c2b09 | -27.13626 | -51.20647 | 2025-11-28 04:38:00 | NOAA-21 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6599610a-0605-34bf-bc0a-5d5fc8d06f59 | -21.08608 | -56.12131 | 2025-11-28 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2830beb3-7431-3bcd-9e52-928dc5027c94 | -26.4849 | -52.09832 | 2025-11-28 04:38:00 | NOAA-21 | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d5b87192-ea62-3e6f-be4c-e9533a30145b | -22.19221 | -56.00988 | 2025-11-28 04:38:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 245fa6d1-de9e-3fae-969a-79916a5ed525 | -22.97988 | -48.6656 | 2025-11-28 04:38:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2567b18e-601b-399e-b9eb-86e3fa03c5c7 | -23.02534 | -47.49002 | 2025-11-28 04:38:00 | NOAA-21 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6d1d503d-4cb6-3d24-9bb8-08d027829d29 | -28.142 | -48.80027 | 2025-11-28 04:38:00 | NOAA-21 | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3921edc6-ca6c-3ed0-ab95-3439dcaa1092 | -23.98114 | -49.64457 | 2025-11-28 04:38:00 | NOAA-21 | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 641612ad-d44c-34c3-ae84-dec2f882cdbe | -27.3809 | -51.39738 | 2025-11-28 04:38:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9d66069c-a11a-3f3c-a2e2-6f28c571c984 | -23.96038 | -49.76762 | 2025-11-28 04:38:00 | NOAA-21 | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 5121395c-761c-360b-a959-1d0ac860ee06 | -22.96144 | -48.69374 | 2025-11-28 04:38:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4a83ae1-7a23-3f0e-8d87-cb7e1b54c8b2 | -22.4793 | -49.12463 | 2025-11-28 04:38:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61769e36-9346-3172-b1b9-5e6f0a54b139 | -23.77054 | -48.13504 | 2025-11-28 04:38:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d074eab6-f4c8-3a01-a800-402bc10fe47f | -22.74882 | -52.13961 | 2025-11-28 04:38:00 | NOAA-21 | PARANACITY | PARANÁ | Brasil | 4118105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d70a1b78-bc84-3188-a8a8-98afe501a303 | -31.47268 | -51.25103 | 2025-11-28 04:40:00 | NOAA-21 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 587f04d9-9829-3758-bb90-d02e92be3c30 | -31.47557 | -51.25618 | 2025-11-28 04:40:00 | NOAA-21 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| a9985f8a-822a-3de9-9774-522fb11750f8 | -29.62152 | -56.26258 | 2025-11-28 04:40:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 9369fb23-471e-3579-a20a-0775c1059597 | -31.47328 | -51.24654 | 2025-11-28 04:40:00 | NOAA-21 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 35187eb5-4b62-3f0e-bab1-a6bdb2a7284e | -29.34506 | -52.40254 | 2025-11-28 04:40:00 | NOAA-21 | BOQUEIRÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4302451 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 609918dc-69af-31ce-b1af-230798896a4d | -31.64147 | -52.42557 | 2025-11-28 04:40:00 | NOAA-21 | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| e543e3ee-5c79-3b10-a91c-13e489661876 | -31.47618 | -51.25169 | 2025-11-28 04:40:00 | NOAA-21 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 01c14d06-95f5-315f-866f-4d6a67fcdd90 | -29.349 | -52.3992 | 2025-11-28 04:40:00 | NOAA-21 | BOQUEIRÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4302451 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 789d5791-f126-3930-9f8e-734e9b087191 | -2.6181 | -47.3521 | 2025-11-28 04:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 554ef45b-9815-3972-84f9-c9ee7f677fa6 | -1.25938 | -54.68124 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78f398bb-28f8-3440-9e42-085d1bf2b26d | -2.64833 | -46.96111 | 2025-11-28 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2873be3-fce3-370d-b9fb-390ff8d89320 | -2.43166 | -50.26191 | 2025-11-28 04:59:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4384128-a45c-332e-9ea2-557a6d620876 | -2.80906 | -46.76106 | 2025-11-28 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 539906e8-15b0-36b3-9a12-b5a69928bdf7 | -2.99289 | -43.84226 | 2025-11-28 04:59:00 | NPP-375D | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ad4652b-e330-3c93-b7b3-a996f4270ee0 | -2.70976 | -48.35123 | 2025-11-28 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15000b6a-775a-334b-bbd1-19aa19df8c73 | -2.70469 | -47.41228 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f5a02c3-dffc-3d0a-adca-31a2aafb2864 | -1.24919 | -54.05912 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d4e0f6b-5593-3511-ba2f-dffdbe231791 | -2.65656 | -46.96682 | 2025-11-28 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d29109f-2a0a-372d-b548-53c156cf66ef | -1.93899 | -54.5147 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07718ed2-60e3-38fe-90fe-a8e7d70fecc6 | -2.99257 | -45.42383 | 2025-11-28 04:59:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fd2c3aa-fbb3-3f4f-b8d9-0cf5677b8a74 | -2.27306 | -47.09787 | 2025-11-28 04:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b7d44b3-c961-3fb4-a499-54e1b7fedcc9 | -2.70964 | -47.40884 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 578a241f-6e86-38ce-a032-5c0c8c3ecfd9 | -2.61953 | -47.35399 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d44e1b63-e012-37ce-8b17-5fc6da2224ae | -3.86532 | -42.27476 | 2025-11-28 04:59:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0a24aea3-d674-3c93-b5c6-a90787f7b0b3 | -3.34954 | -45.4277 | 2025-11-28 04:59:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c33286d-675d-3f57-aa8f-e4bf650d91c9 | -2.70224 | -47.39948 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67498f49-b621-3d3b-941e-86955491effa | -1.64938 | -52.04037 | 2025-11-28 04:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb6a76e0-f49a-3e40-bad4-7da0fad938a9 | -1.36007 | -55.43738 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c177e87-e70e-3f46-b448-daa43a39eb2d | -2.42361 | -45.74167 | 2025-11-28 04:59:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29eecb01-00e1-3649-b77c-7381beee6391 | -1.15938 | -54.07405 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f4e8cdc-a3d7-3056-aa53-79cb15679659 | -2.62511 | -47.34659 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a841545b-e274-37e5-ba7d-7d11c512d847 | -1.47943 | -54.20301 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71213b7f-416d-31aa-b96d-f0a9f60863d2 | -2.15927 | -50.62691 | 2025-11-28 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6933020-7fd8-35f1-b493-912abf664f1a | -1.47552 | -54.20601 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5aca4ec1-91b0-3875-a490-5f98ba574618 | -2.71856 | -45.21397 | 2025-11-28 04:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56102621-2815-3211-b6b1-8a1b9e827426 | -1.2464 | -54.05512 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 622f08cb-9c82-332a-af59-8153e1cb6241 | -2.62385 | -47.35467 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e36230a3-e437-32f8-a025-fdaf20b22258 | -2.14678 | -53.64798 | 2025-11-28 04:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7f25e039-09ba-3319-895c-b051b34ee102 | -1.33427 | -53.22009 | 2025-11-28 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62903878-a1f3-371f-9242-98fc744a90b2 | -2.41833 | -47.23391 | 2025-11-28 04:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc4cd3ca-05ae-32ec-812e-84e563deb3e5 | -2.6115 | -47.34863 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51f6bfd5-a316-34fc-811d-883f5a19bb4f | -1.50022 | -54.70396 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 19b09a7f-9087-3394-a60c-a3d238c6042c | -1.54206 | -55.36339 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cf6b69e-50e9-3d64-b15f-eea9c0ba65cf | -1.90628 | -46.28087 | 2025-11-28 04:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ae4ef4f-0bd6-30b3-bf0f-cbed22a3417f | -1.33372 | -53.22353 | 2025-11-28 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfa990b1-7701-390d-9c9c-9317a0a30464 | -2.57747 | -49.09187 | 2025-11-28 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 170aa0f8-552a-33f1-a8ce-b9d030d29b3b | -2.4233 | -47.23058 | 2025-11-28 04:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7987fc05-f803-3ec8-9121-662bdf0bc133 | -2.61521 | -47.35332 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec644214-0e93-3801-98f1-497c53808ee9 | -2.69778 | -49.55605 | 2025-11-28 04:59:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdb5b6c3-3b48-3f5f-92a8-baa7c3578fc4 | -1.39887 | -55.42371 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f193b4ab-b6ac-3ed0-ac89-ad3b6306baec | -2.7092 | -48.35479 | 2025-11-28 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a5c3b9f-8449-3c39-8e6a-fbf97e8cb34b | -1.34035 | -53.22456 | 2025-11-28 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9a68aee-d680-390c-9302-c939f3731457 | 0.66081 | -51.53772 | 2025-11-28 04:59:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5cb05bc-0205-3a9c-acfa-4463977b03c1 | -2.71027 | -47.40476 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eec8462f-4e5c-3323-a8fc-a61679bf751f | -1.83587 | -55.34615 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9463dfd2-def7-3218-9507-ea6205e983c0 | -1.18513 | -52.51854 | 2025-11-28 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3281936-01c2-337c-9da2-09ffe84f93b5 | -2.61708 | -47.34117 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bff57c3-5e96-38cb-b786-07c931ab1102 | 1.90179 | -50.90391 | 2025-11-28 04:59:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a31e8c2-a87a-3787-b4eb-b23116d1af35 | -1.25097 | -52.63508 | 2025-11-28 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db76a61c-a82c-30bc-95af-438b7e71082d | -2.62078 | -47.34594 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2f6d892-bc20-38f8-964b-559b6e83e284 | -1.25995 | -54.67759 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 909fcf0b-2c2f-3f58-9d98-14d73b155752 | -2.64767 | -46.96547 | 2025-11-28 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12e8aa21-6d0c-361f-9550-c1c251da403e | -1.34431 | -55.4466 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 405bc7e9-ea4a-3694-913d-3a2183bc0131 | -2.7474 | -47.13379 | 2025-11-28 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec9c225a-b35f-3cd6-874a-848ab239422c | -1.49682 | -54.70345 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2880a041-8e06-355a-bd2a-9b878944430c | -2.70408 | -47.41629 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61e83c7a-f85e-3cd2-b864-b072a666c592 | -1.33813 | -53.21716 | 2025-11-28 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f00528d7-98fb-3f4a-b817-cb4cd4e1c1e3 | -1.34143 | -54.60445 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63da9259-f1d0-3505-8fad-e00fbab415f3 | 0.45894 | -60.44866 | 2025-11-28 04:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README16.md)
