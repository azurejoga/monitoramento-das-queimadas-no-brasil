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
| b9f65a96-f08e-3817-8156-072a060ac6a7 | -19.71431 | -56.85919 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0a5163f1-6bf8-3664-bd96-ca5e72da0029 | -20.31898 | -57.81781 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 02e46e69-2ccf-37d4-bf04-22fd9cfdcb07 | -22.32506 | -47.13483 | 2026-01-26 04:31:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e089f519-beb1-3d17-9bb4-203f524cdb14 | -21.95015 | -47.42258 | 2026-01-26 04:31:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6e4c208f-9ca9-3eaf-bd40-e7f83eb63af5 | -19.62615 | -57.34229 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c5964bb5-1b4e-3d79-8e34-53a2984a2148 | -20.3131 | -57.82222 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a0a35679-d755-371e-b899-a0c819a6db6b | -19.69996 | -56.83316 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6741b356-556c-3367-b790-0159fc0ad0a3 | -19.42591 | -51.83052 | 2026-01-26 04:31:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab8c981e-a48f-372e-a8c0-03719bf2c313 | -19.67476 | -57.17421 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| df363d3f-afae-3d5b-89a2-27a09da03d85 | -19.72276 | -56.84067 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a6e4541f-1cec-36ed-84f8-2bcc05728d9d | -18.77909 | -57.65537 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| abbeabf5-bcd5-3ae0-8430-90be2d89febb | -18.77796 | -57.66106 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d0ce2342-0ee4-332f-b8c4-14f6f9066e38 | -25.20948 | -51.39144 | 2026-01-26 04:31:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 18a118f7-b34a-3ef1-baa4-8528f4c2e015 | -19.70919 | -56.83771 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 99fad33e-39fa-3989-ac47-2e4b43bab244 | -23.33011 | -53.11835 | 2026-01-26 04:31:00 | NOAA-21 | TAPIRA | PARANÁ | Brasil | 4126900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ccf4de74-4562-3055-bb97-8f99d622c70a | -19.71786 | -56.86506 | 2026-01-26 04:31:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d71efbc1-cba1-3d02-abe9-c0323d95595e | -19.62147 | -57.34126 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5750d8ac-5dac-3294-9999-01779bfa0f17 | -20.32373 | -57.8189 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2f1ce35c-d6b2-3984-b981-4db22c6b9a26 | -18.82539 | -57.71614 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 7660ff84-d318-3563-9847-53f112dbe192 | -19.70781 | -56.86797 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 07330ddf-5d25-3490-8af2-5139c8b83556 | -19.66899 | -56.84671 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5bccfb84-0a55-3abb-9c9b-dccd06a30bb6 | -19.70448 | -56.83416 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ab762896-4b88-3fe8-b5ab-3bbf20842cec | -18.82169 | -57.70934 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 83c062c2-b486-38b2-aca4-6973f571693f | -19.69449 | -56.83705 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5942d5f7-742c-34f6-9674-d569632861ec | -22.48693 | -47.00722 | 2026-01-26 04:31:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 788469cc-1687-30b6-899e-b9d16bbb5d0d | -19.70682 | -56.87286 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 434d8949-2a1d-39de-ba38-a87dd7cd0936 | -19.68996 | -56.83605 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1e0887cc-6f61-31f2-a7df-104698eaa3ea | -25.20617 | -51.39081 | 2026-01-26 04:31:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 92de675a-9828-337b-afb3-b4ca0804fbfd | -19.66446 | -56.84572 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 12853d69-edfe-3dc4-a0f8-5e96401d2d72 | -21.94963 | -47.41988 | 2026-01-26 04:31:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 37eafd30-84c7-3ca4-8a02-9e4345577975 | -20.91812 | -56.37721 | 2026-01-26 04:31:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 868a15b9-5613-3a4d-8930-72f7d397b08e | -18.8474 | -57.73302 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| b997251a-0f57-3ed8-b0cf-f1f5ea0f549b | -22.32151 | -47.13429 | 2026-01-26 04:31:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0f7ffc3-2c53-3df8-bdc0-7aaedfaea6d8 | -20.91897 | -56.37288 | 2026-01-26 04:31:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d1b1aac-0cff-3666-9024-4ca2b6f204b4 | -19.67938 | -57.17524 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3888fc3b-870e-3857-838f-1fe956a93f45 | -20.31785 | -57.8233 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b30a1c54-b392-3943-a395-39f02a5e5845 | -22.32092 | -47.13863 | 2026-01-26 04:31:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ac10a75-9767-34d1-ad09-3a5544bc0b20 | -19.64673 | -57.26497 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d2820843-7abd-3117-9878-b4690b35c7d7 | -19.69544 | -56.83216 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c02af9ad-1a6a-3b2e-ad03-227b2f51a9e3 | -19.62975 | -57.34859 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 76fb3e5e-c679-3927-a230-3815361e9df2 | -20.42311 | -53.22793 | 2026-01-26 04:31:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef756061-86e1-321d-a71d-4c3f4fe913b5 | -19.70467 | -56.83672 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9c3e6bc9-78bd-3a8f-a256-15e0d6f3aeeb | -19.67373 | -57.17932 | 2026-01-26 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 19fe271e-0920-3de7-b42a-a41d050aac2b | -19.71371 | -56.8387 | 2026-01-26 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 51e034b8-22ba-3cd7-a2ce-42e9d1ba51f7 | -26.90418 | -52.88014 | 2026-01-26 04:33:00 | NOAA-21 | NOVA ERECHIM | SANTA CATARINA | Brasil | 4211405 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 853e57e6-42dc-30fb-8c9e-23fd6c9ffefd | -28.10349 | -50.50826 | 2026-01-26 04:33:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 792d79c7-b526-3e58-82b7-158aaba33c13 | -27.33351 | -48.87479 | 2026-01-26 04:33:00 | NOAA-21 | SÃO JOÃO BATISTA | SANTA CATARINA | Brasil | 4216305 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8dcd2ee7-c47f-31b3-b3b7-b961423dd725 | -28.32127 | -51.90405 | 2026-01-26 04:33:00 | NOAA-21 | CIRÍACO | RIO GRANDE DO SUL | Brasil | 4305504 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dea70eed-138b-3c89-8a6c-93ceb76b5de8 | -26.82776 | -51.38186 | 2026-01-26 04:33:00 | NOAA-21 | MACIEIRA | SANTA CATARINA | Brasil | 4210050 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b03de5a6-654e-37ed-a973-daeb337231ad | -26.05481 | -53.57912 | 2026-01-26 04:33:00 | NOAA-21 | SANTO ANTÔNIO DO SUDOESTE | PARANÁ | Brasil | 4124400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 084d9f2d-579c-33ff-89f1-88ddb84cb6b7 | -30.89145 | -52.93752 | 2026-01-26 04:33:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| aa1bd170-0fcb-3724-9829-be131d8269bb | -28.10408 | -50.50429 | 2026-01-26 04:33:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54fa8cd2-ed21-3f25-a449-0e25c7171c4b | -30.8908 | -52.94155 | 2026-01-26 04:33:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 70e6c047-35bf-3ba8-8e4a-00b1ac8fdf56 | -19.7242 | -56.8408 | 2026-01-26 04:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 6cbfb217-69d6-3a20-b9b9-995828363765 | -19.7041 | -56.8436 | 2026-01-26 04:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 65ae44cc-f339-351e-9bf3-1a8181a3c089 | -19.7242 | -56.8408 | 2026-01-26 04:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 83d10b75-115d-329d-958e-50f5af627794 | -19.7041 | -56.8436 | 2026-01-26 04:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 39a6d0b7-e9cc-35dc-b59e-fcc3b1ec5144 | -3.26374 | -42.54585 | 2026-01-26 04:55:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 632d24fc-0b9f-318a-ab42-5682068e6a08 | -3.26321 | -42.54938 | 2026-01-26 04:55:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80c072fe-a6f6-3f3d-8f12-a25076fd01bc | -4.74867 | -46.65453 | 2026-01-26 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18120f02-6afe-3f72-a280-528c10dc2c13 | -2.23311 | -45.3909 | 2026-01-26 04:55:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61cf394c-536c-3796-990e-b24497eb44d6 | -3.00243 | -52.87188 | 2026-01-26 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7e51fd94-bc24-378a-b0fc-6f0881c0c169 | -7.54162 | -46.02327 | 2026-01-26 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 295a0fc4-570f-3931-9c19-aca2fbeb7042 | -9.28936 | -48.58849 | 2026-01-26 04:57:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 094ae23c-7d30-327d-b3ad-43e752f7ff44 | -16.44415 | -58.16406 | 2026-01-26 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 34ddd4a4-f470-32da-ba49-d587292750b4 | -16.44341 | -58.1683 | 2026-01-26 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6383b994-563e-3f14-9f76-c48989f072c9 | -16.43982 | -58.16761 | 2026-01-26 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bd9016c8-db6d-3d3b-af73-a2c861357b5c | -16.44056 | -58.16338 | 2026-01-26 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 76a73c07-84cb-3c9c-98a1-c72c2ca7a7f0 | -19.61195 | -57.31932 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3625a71e-3385-391c-9103-755d7349c74e | -19.66682 | -57.32558 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5cd5ce27-617b-3e0e-93aa-df24314e444f | -19.61406 | -57.32759 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fedbe9fc-6352-3c38-adbe-4f882587345c | -22.55029 | -55.64218 | 2026-01-26 05:01:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b84f7948-ae52-3044-9cca-39e68af747ff | -19.66131 | -57.31669 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e5a45df9-bc3c-3cb7-b5b5-2ab3af7ab3bb | -19.61131 | -57.32314 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e187df51-3965-3e86-a9c0-4f5326ef3438 | -19.71528 | -56.86381 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b39e5109-d804-32ad-963c-bc0cd7eb9a96 | -19.69943 | -56.83397 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 94481918-1049-3110-a1c4-cf1654f78ea0 | -19.61259 | -57.31551 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f2628b27-1d02-341c-adf0-3c21b0ec596d | -19.71834 | -56.84511 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a03db5a3-47bf-31e9-a48d-3934c138ff91 | -18.84575 | -57.73717 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| b501a978-5d2f-37f7-82a1-1df7a525123e | -19.66484 | -56.8469 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 98265912-1847-3912-b9c3-2a6d2f2beaad | -19.65559 | -57.28813 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 72619926-d89b-36f7-9b4e-08ed9178093d | -19.72231 | -56.84198 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.4 |
| 06e0daa0-f029-3887-8377-bf844938a2c4 | -18.81873 | -57.70772 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7af0d16a-067c-3b81-9281-52ebae7b2a17 | -19.61303 | -57.29202 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 87b607d2-22ef-311c-a02b-7a5425c4de45 | -19.61156 | -57.27997 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ab804367-5e35-3460-8afa-5675483d913c | -18.84509 | -57.74112 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f6f0adac-4245-399c-931f-164053aaa312 | -19.6147 | -57.32377 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 24759c57-7702-39d7-a09e-db30a16fac83 | -19.66311 | -57.17989 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 28e2b205-61e2-33f4-ab34-ccec2b179cc2 | -19.66809 | -57.31795 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| aec57aab-d580-38e9-9417-d7b933a0c41f | -20.91802 | -56.37722 | 2026-01-26 05:01:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2abe09b-2dc6-309c-849f-d48ae25dad14 | -19.65856 | -57.31225 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 77b84de4-dcba-3fcc-91ef-33f0f9075a5e | -19.7217 | -56.84572 | 2026-01-26 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 534a9c38-ed50-32ab-bc08-86dc47d4bc52 | -19.65157 | -57.35424 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cf7289f1-abac-3e54-927e-8a75e8f39059 | -19.63929 | -57.28119 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| febed215-c043-382a-895a-f054ff47aa4f | -18.82084 | -57.71624 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 3dab9b9b-4f39-3fb9-b82d-06d0b59f7f02 | -19.65771 | -57.35933 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8c6f9f3d-5998-3caa-ad3b-5ce581c7e8d3 | -20.31594 | -57.81148 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| a769f747-aa4f-38f5-8df6-3f99f71b3509 | -19.6745 | -57.17419 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 11978176-1e1a-3a53-be7d-21c095521e01 | -26.05374 | -53.58176 | 2026-01-26 05:01:00 | NPP-375D | SANTO ANTÔNIO DO SUDOESTE | PARANÁ | Brasil | 4124400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d174830e-ea7f-316d-8e9d-e4ce1dec7bba | -19.66195 | -57.31287 | 2026-01-26 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |


[Clique aqui para ver as próximas entradas](README5.md)
