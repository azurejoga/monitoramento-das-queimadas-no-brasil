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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66504d42-3a66-3f6a-87dc-82d77ef2ada9 | -20.30637 | -46.46408 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9067ad5b-1b86-3222-bd74-d416d0c9ca46 | -22.07293 | -55.99059 | 2026-08-18 04:06:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c9e0d44b-94ac-3c4d-9ddd-9aaa94fd00ba | -23.40622 | -46.42277 | 2026-08-18 04:06:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3080a4d7-4ba1-3a76-9dcc-a75ced19d90c | -20.29991 | -46.45876 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a50f691-a484-31df-80aa-c248e5bcd569 | -20.5952 | -45.93053 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31ca67c9-5a3a-33d3-b832-33dab04eec51 | -20.29708 | -46.47485 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8c22768e-4947-35b2-8432-06d30d584bef | -18.84798 | -47.13788 | 2026-08-18 04:06:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31f3113c-3010-3200-8046-f7f7c7428c69 | -22.06749 | -55.98584 | 2026-08-18 04:06:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7b61a85b-44a0-35fd-8e11-951f7243dc89 | -22.93843 | -43.38783 | 2026-08-18 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f9987e16-89a0-34a8-baf5-8bff186836f7 | -20.59941 | -45.92694 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44a85bc9-d51f-331b-bc2b-743cf9826715 | -20.62202 | -45.92739 | 2026-08-18 04:06:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84fb3ada-86ca-3d23-9314-14a01167d8b2 | -20.61724 | -45.91347 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dfa53a1-b62f-3690-b862-0cd1f724f276 | -20.60962 | -45.91596 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 301b70c2-9561-30a6-9052-c2fd4b944dd0 | -20.29923 | -46.46266 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3e04fdf-f05a-3659-95b6-9f2e976993cf | -20.62071 | -45.9142 | 2026-08-18 04:06:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4692f21a-e0cf-3921-8222-7f3ccc7196b7 | -18.67467 | -48.17842 | 2026-08-18 04:06:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 326ba113-bd10-36db-bdca-8af6ea3c30b9 | -19.79225 | -43.91711 | 2026-08-18 04:06:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e803a79-8a47-325a-bbf0-78c6ae04a857 | -21.41883 | -45.46466 | 2026-08-18 04:06:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b385089e-a561-3cc8-94f4-805fce007d58 | -18.94938 | -48.09884 | 2026-08-18 04:06:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 422da35c-c489-30e9-9277-efff07652092 | -27.88529 | -53.29895 | 2026-08-18 04:08:00 | NOAA-21 | PALMEIRA DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4313706 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5dac6cb1-e0da-3c97-bd15-fbc3dcc81e39 | -6.8411 | -58.9939 | 2026-08-18 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| be2d3ea3-b8e9-3e62-8346-be66d88b8706 | -14.8033 | -46.6453 | 2026-08-18 04:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 1c716be5-da05-36fa-8966-f2c10678f831 | -11.5279 | -46.6518 | 2026-08-18 04:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 61f18638-239b-39bb-9d5d-db9dff947216 | -14.1821 | -52.93 | 2026-08-18 04:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 63e755d9-be2d-3aa2-a58c-061e22bfb93d | -11.5282 | -46.6292 | 2026-08-18 04:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| f4791b3f-9ea1-345e-bdc7-5adcbc6182cb | -14.1631 | -52.9113 | 2026-08-18 04:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 2aead3ce-35e0-3b84-bf09-3e476240ee0a | -6.7478 | -59.1716 | 2026-08-18 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 5991efef-3e19-3b20-9312-fb95967fd352 | -8.102 | -61.3404 | 2026-08-18 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 12f3c4a4-d6cf-3954-bae9-096a93d3dea8 | -8.604 | -50.3527 | 2026-08-18 04:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 02e056e6-d5d6-37c7-8803-59656cc9c826 | -6.841 | -59.0132 | 2026-08-18 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c972f4e0-7861-3f95-a278-246b2ad9d9bc | -14.1824 | -52.9089 | 2026-08-18 04:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 091fc495-632c-32ac-bc1e-84949b8fd94c | -14.8228 | -46.6419 | 2026-08-18 04:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 0b0fd06b-123e-3d19-ba25-81b19cd21c9b | -8.5853 | -50.3543 | 2026-08-18 04:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5313a76f-2bd1-3877-9f1b-4aeed908d04e | -14.8233 | -46.619 | 2026-08-18 04:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b0b00736-22fd-3607-bc34-2c33b6320332 | -6.748 | -59.1523 | 2026-08-18 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 85bf6242-a544-31e6-a860-a98bbf5e5912 | -8.4899 | -48.821 | 2026-08-18 04:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 48.3 |
| b1a82f83-3705-35b8-ab19-15fdf5194424 | -6.7477 | -59.1909 | 2026-08-18 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 82f4244e-7dca-3728-92b3-7fc029c20b92 | -6.8594 | -59.0125 | 2026-08-18 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| cd136df9-a73c-37cd-b2d6-a6f2c581d9c4 | -8.57 | -54.73 | 2026-08-18 04:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dbfbfc6-f933-3b02-9726-b14593d80619 | -6.8411 | -58.9939 | 2026-08-18 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| c143a98a-dd30-34cc-a489-c8c4d4b8b295 | -6.748 | -59.1523 | 2026-08-18 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 67a84f14-4cab-3391-a2f6-f8d38aab31c2 | -14.1821 | -52.93 | 2026-08-18 04:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 155.2 |
| c7691ceb-44d6-3d80-b9f6-304be1b5706e | -14.2014 | -52.9276 | 2026-08-18 04:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| dee50003-b418-3b24-9e44-0a246b0aab2e | -6.841 | -59.0132 | 2026-08-18 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 1956002a-c696-34f5-91c7-b7c0b1b0d5a3 | -14.1631 | -52.9113 | 2026-08-18 04:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f41d38a6-f8e1-3748-8dee-6159902c56e3 | -8.6042 | -50.3315 | 2026-08-18 04:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 6836c9ef-7f73-3389-8d72-2ad97982bff8 | -8.604 | -50.3527 | 2026-08-18 04:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a6f978a6-5486-3e0b-bc3c-2137c0338c9f | -8.4899 | -48.821 | 2026-08-18 04:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 48.5 |
| af98da92-28dd-3776-b61c-9786b58d42f9 | -14.8233 | -46.619 | 2026-08-18 04:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 2854dc87-f9e5-3b90-8d7e-0e726961defa | -14.8228 | -46.6419 | 2026-08-18 04:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 67a56302-4732-384f-bd3d-c9b07afce4bd | -14.1824 | -52.9089 | 2026-08-18 04:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 136.2 |
| ef31a947-d061-3287-99c0-bcdfd0fb8c3c | -14.8033 | -46.6453 | 2026-08-18 04:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b4b66d9c-bec5-3bd6-8ab4-358334472129 | -6.7478 | -59.1716 | 2026-08-18 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 7777aa59-eed3-3524-accc-7d9368410d7f | -14.1824 | -52.9089 | 2026-08-18 04:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 0eb859fd-291e-39ee-8de4-a887190a77be | -14.8228 | -46.6419 | 2026-08-18 04:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| ccd8b5dc-4d59-34ce-ba45-bd3043ae3341 | -14.1828 | -52.8878 | 2026-08-18 04:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 38eafb39-7bd2-3357-8b20-c08a5c5258aa | -11.5282 | -46.6292 | 2026-08-18 04:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 82851c65-7790-3947-a055-2c27f7ede4b8 | -14.1635 | -52.8902 | 2026-08-18 04:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 802eabc6-f64a-3762-8b92-48ff630b60a5 | -6.8594 | -59.0125 | 2026-08-18 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 96b62b52-1029-3250-9957-a42190b2ccca | -6.748 | -59.1523 | 2026-08-18 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| bd021a7e-d77a-3b7c-a4d4-51783a595296 | -6.8411 | -58.9939 | 2026-08-18 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| fd83af9c-ec38-3edf-800d-b07479efdc12 | -6.7663 | -59.1708 | 2026-08-18 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 7a0f709e-769f-3709-9c62-7ab497361416 | -14.1821 | -52.93 | 2026-08-18 04:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 135.7 |
| cabea9c0-3787-3699-876f-193e47f7f95e | -6.7478 | -59.1716 | 2026-08-18 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 22a5f3f6-2db3-3a6a-bf31-ddf96a1e86eb | -6.841 | -59.0132 | 2026-08-18 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 243dbe9b-66db-3b44-94ca-cb7f1ffe5e9f | -8.604 | -50.3527 | 2026-08-18 04:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| be6f8aa1-e2ca-3084-931c-f1c39b3e5fe6 | -8.5853 | -50.3543 | 2026-08-18 04:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 79f8a89e-0957-33d5-b2da-5d60b8c09054 | -14.8233 | -46.619 | 2026-08-18 04:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 324c0182-1ed2-3067-8f60-a72d7eca6cff | -14.8033 | -46.6453 | 2026-08-18 04:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 364373d8-16cb-36cd-accc-c585af758c68 | -14.1631 | -52.9113 | 2026-08-18 04:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 767d799e-6a95-3147-9d81-b5f1e05fcefd | -4.15333 | -38.41388 | 2026-08-18 04:36:00 | NPP-375D | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7b4c7db0-d6cc-30ed-975c-f8fa64dd0378 | -2.57933 | -49.44237 | 2026-08-18 04:36:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbd9dd80-744b-3e8a-9539-ae7f023b5914 | -4.15253 | -38.41906 | 2026-08-18 04:36:00 | NPP-375D | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dc83d81c-37fa-33ab-aa97-7c62f9b1bc4a | 2.16061 | -50.72355 | 2026-08-18 04:36:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b634382-6bfc-38ec-9f5b-77f24c5d978d | -2.49727 | -48.13607 | 2026-08-18 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5a89731-58c6-3ee4-9110-f20521d76eab | -3.2392 | -43.22538 | 2026-08-18 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a1914d8-7bcd-3e46-aff8-b38d77d91b4c | -3.56404 | -43.20132 | 2026-08-18 04:36:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46e61c0b-9e05-37c7-ae48-ed613c885739 | -2.49665 | -48.14001 | 2026-08-18 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11c73fc6-10e8-30f5-a461-dee5049a9258 | -4.15243 | -38.41466 | 2026-08-18 04:36:00 | NPP-375D | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b8a97573-5c60-376d-aa65-540a383cd846 | -8.49263 | -54.91105 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d96c5ab-1616-3d73-a608-c801516184d2 | -9.77641 | -46.71796 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7833dbd9-28a8-31e0-ae45-88c92a8f0e26 | -8.2124 | -55.01494 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85f14356-4df0-33dd-973b-b8f8e53e988a | -3.26572 | -49.52116 | 2026-08-18 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67880094-f1cc-391c-9532-4f8867b8c999 | -8.57253 | -54.70236 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fa5c9d78-b9df-3460-8e7f-b33e1a8d46c0 | -8.56767 | -54.72912 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 1d2da6db-d82d-361b-9fe7-314e27dfcc36 | -7.81541 | -44.60924 | 2026-08-18 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d0b62f2-bf2d-357c-a6f0-1543ab186aa4 | -8.33167 | -46.47734 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46b03a56-8b77-3271-89f1-5d8a9be9c0c4 | -8.21529 | -55.02752 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc58cae8-5388-358d-a6a1-c2b2ee357e8b | -8.56248 | -47.39355 | 2026-08-18 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2daf5079-7df8-3e15-87e9-63899fbf99ed | -6.84522 | -59.01146 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| af48d83d-387c-3bfd-ac16-5160ae7fc75b | -6.84411 | -59.01741 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 423e3a20-7e30-3718-bff3-cffb491f3ab7 | -4.49397 | -42.55899 | 2026-08-18 04:38:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 204c98bb-c1c0-396f-ab9d-6250a77e9ea4 | -9.19432 | -49.96848 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 39405223-7fc1-354e-b6ea-f17c09318d2d | -6.18558 | -47.81189 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19254c2c-71c9-3538-8e6e-8171603c1b73 | -7.56458 | -55.56126 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 313177e5-35ca-3d6d-9976-d470633ed9fc | -8.3278 | -46.4803 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4878bb0b-a823-381a-bc69-884510a5db1a | -8.59299 | -50.3448 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 50f9ab64-78ad-3ec8-b385-7bc91f418ed8 | -3.26124 | -49.52507 | 2026-08-18 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ab49ba3-88d8-311f-ab2f-7c1df1b74da2 | -8.588 | -54.69992 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 824bac19-3387-3026-9ab2-e78a3f8cb0aa | -7.82003 | -44.60218 | 2026-08-18 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README18.md)
