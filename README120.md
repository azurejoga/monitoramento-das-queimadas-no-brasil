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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c07cbf1-0f8a-357b-8a16-a0ff63ceed3e | -14.81164 | -51.43008 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4753d1a6-921d-339f-a45c-753e567cf080 | -14.66984 | -48.09327 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 22c8f3cf-ae1f-3f0b-839d-77abbc7f6f2d | -15.27114 | -47.90902 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8afb769-5792-31ca-ae39-ca36f0ad5e71 | -13.02405 | -43.83825 | 2025-10-03 04:34:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b55f9a60-304d-3fcc-8803-d96e19a3186a | -13.13598 | -47.88681 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4414d807-d84d-3fea-bd30-ec804336a345 | -14.74098 | -48.13488 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4e3cc09-5817-399b-a3d0-06d902e3aa53 | -11.31415 | -53.96043 | 2025-10-03 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2095b73e-2a13-39c3-9216-4aadef8d546b | -13.80058 | -47.56926 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfaedafa-bb02-376f-b51c-f57ebdbcef76 | -18.17888 | -53.28506 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ded9a59a-8f60-3186-ba69-b198bb1b1642 | -13.97185 | -48.17692 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b05b80a-ccad-3837-8f1a-263a8e30f491 | -17.20902 | -46.99358 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aaf696c-c9c7-3363-8921-f42ffae25049 | -14.81844 | -51.43127 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec93cf5c-6154-3b28-a6ae-2252138cf48f | -18.15817 | -53.34147 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 488a7371-3566-36f7-a592-bf3640101381 | -18.21518 | -53.37062 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71671a8d-3409-3f61-9ea5-06c575582f5b | -14.95061 | -47.52226 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 788d368a-91a5-3cd8-986c-d6e5aaafc563 | -14.73304 | -48.11867 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 191f293f-8e46-3411-8ec7-c11741c577b0 | -14.73749 | -48.11203 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40c850ee-87fe-3531-be79-0bd09652b1c7 | -14.64795 | -48.1237 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb301c58-eae1-31c4-a3a7-c5b30dd8f6a3 | -11.28726 | -53.94839 | 2025-10-03 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a9426c9-6f20-349c-962e-e50ac6771b7c | -14.11608 | -44.30869 | 2025-10-03 04:34:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c08966e-e199-3b90-9471-b8e7e7b91942 | -13.38724 | -47.29327 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc703458-8818-3665-8da2-96843a043c08 | -12.62268 | -46.9609 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad80fea1-d98a-30cc-8713-5ce14096925a | -12.6238 | -46.97689 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4ff5257f-52c5-3735-90a8-358ea688c9ea | -14.73414 | -48.11133 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a8c203c5-ec9f-3d9a-bc70-07a59652db2d | -15.33167 | -46.29552 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10f976e3-6c74-3f36-985b-0eac3aff91b3 | -14.91436 | -48.33292 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 696e8c45-56fc-3e1f-b4bd-c5646bd487c7 | -14.29839 | -45.98404 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28e90a2c-5d44-3a28-b0b0-663ddee2b2b3 | -15.25356 | -49.31071 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52ecd155-8b25-38f3-82f5-8369c21b0bd9 | -19.14256 | -41.50126 | 2025-10-03 04:34:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2636deac-6e23-3d02-bc66-af1092d6712e | -13.19307 | -47.79317 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8afcc453-2656-3fee-a5c2-63897eac089a | -12.67568 | -48.57977 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b8410c9-6ea5-3f14-9c2f-127cbd90c33d | -13.58048 | -48.19019 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff130a69-76e4-3523-b733-b6f5ae2c2e9b | -14.11584 | -45.66193 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4b216cf-5846-3143-9b5b-e4ff4e9cf413 | -19.82237 | -46.83431 | 2025-10-03 04:34:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18b6e98f-d9e6-3f59-8795-acf545ec0084 | -17.7533 | -51.83587 | 2025-10-03 04:34:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3137dcc9-6606-3028-b504-1f2b2d8ce401 | -14.42477 | -46.35246 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 60407b32-54df-3e73-af2f-608f75a85bd0 | -13.47875 | -47.2404 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3aaf905a-cd17-3e43-a3a3-99be9875f411 | -15.2774 | -47.91389 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d833b3be-83e7-3cb3-adde-bf109f67c060 | -16.68556 | -53.01609 | 2025-10-03 04:34:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d71f1b1-7b98-369f-a4dd-c12badd68278 | -14.19093 | -46.68975 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d3ee39d-e158-36ab-a602-57107ef32486 | -16.05725 | -51.04838 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e067605-466c-32f4-89da-a9719161ac6d | -14.93566 | -46.88036 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9f419770-1cb7-3698-815e-f036d9c82d7b | -12.71583 | -48.58281 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4acc1eb-2bc3-3924-8060-b6838ec1ce80 | -12.59807 | -49.88976 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 394d267e-33a4-3499-918e-fd4baa336908 | -13.17678 | -47.87793 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6085ef6-0779-301d-b3cd-c34a6b352c68 | -12.36703 | -46.52256 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e692b275-a989-3a02-82ed-19664f98d6ca | -14.93692 | -49.98558 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4762473-1285-3a94-8094-3352d3e25941 | -14.41149 | -46.16118 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b914fb4b-49c4-3698-ae2d-cee585d3cf29 | -14.72843 | -48.11787 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7406a3b-24d1-33bf-aa9e-550062de6ae3 | -14.3331 | -45.87099 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7560c9b0-551a-3eaa-9d22-74b06752c7c8 | -14.87844 | -48.33103 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75e5105f-07df-3e51-939f-757d37fe0fb5 | -14.64882 | -46.81804 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c04b90a3-4baa-339c-aa56-7ba54995f2da | -18.19613 | -53.354 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96381f79-c306-3208-8286-b5f3de63c463 | -15.49912 | -45.92141 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6f1bf98-a0fc-35be-89f7-8535226ad542 | -18.45413 | -43.81277 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5074de86-6ac4-3802-acca-c9b7471a2155 | -13.25268 | -48.42726 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40054074-cd22-3dd0-94f7-0deb00dd544b | -15.21666 | -47.99335 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 79b447fc-a1df-3fc1-af60-2ce9b6e6b2bb | -13.39733 | -47.55142 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 590ea43e-fb34-37de-bdc8-aace4908213d | -12.80727 | -47.03442 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47454065-e41a-3c3d-9fa4-278e82d58de3 | -13.53844 | -47.28882 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db358feb-2830-35a8-ad49-2b26281818e1 | -13.21464 | -47.34901 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03f33708-a391-3879-b402-993806d4242e | -14.29034 | -45.9679 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05c3d9f9-ca9e-37f4-9557-1d78544c9b4a | -16.36269 | -47.01613 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83e20a5b-aebe-3864-b674-1a922f34ea5b | -12.19891 | -47.81922 | 2025-10-03 04:34:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff64797b-d97d-3add-afc3-762542bfec7f | -13.14142 | -47.88366 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a7a89ca-686c-3ec0-98c8-df7179cfc33e | -13.53045 | -47.24829 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23fc09d0-0682-3f04-a4df-3150af097837 | -12.81137 | -46.86504 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 79cd272b-b26f-3810-9950-121158b37f48 | -13.68206 | -48.63137 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38b34db4-838d-37cc-8566-14cf03e54b52 | -14.46633 | -48.41208 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 511ec667-7439-388d-afea-2ba2fc1b762b | -20.11968 | -44.37375 | 2025-10-03 04:34:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7b7ca4ff-7050-37c9-88bf-5c1a8a6c6a86 | -14.68274 | -48.09951 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9cff845c-7b6d-35b7-98ef-90fe04992a33 | -15.70665 | -46.25492 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ecbcc61-4a1d-37a0-b034-59e0a1c52f8c | -13.94149 | -48.13916 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77f2e8c2-e8b5-3a73-baa9-d0ee5e6634f6 | -13.27243 | -47.24128 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 828bcd9b-1465-3d06-9d87-3c74acb1372c | -14.20898 | -46.09073 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70e6022d-ecd6-310b-871a-a379c67c721b | -14.60785 | -54.08652 | 2025-10-03 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f78458ad-cc31-314c-a805-77b1f84b4eba | -14.87621 | -48.34566 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28ae0b94-02c1-33da-b0e7-3764c938a761 | -13.29067 | -47.18972 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09ff07ff-ec76-3663-ae70-17ddec859888 | -15.58736 | -46.91339 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 606d5ec0-1446-370a-bfcb-a428b63ad804 | -13.15944 | -47.90133 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 811ddd5f-2674-3524-b230-585ee1b44987 | -13.39024 | -48.12717 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01a461ff-9124-3a0f-85b8-76b9c9f22968 | -15.94514 | -46.23029 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67bbf4dc-e683-31fb-a67a-3ff3d71c00ca | -14.90141 | -48.33854 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f47e73f-07c7-30f8-b6bd-e5d65dc21166 | -14.19152 | -46.68566 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f57956c-454c-33dc-8a8f-49b990c5926a | -14.56632 | -48.33395 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6498131f-2e8d-3501-8597-851ae22d2ee7 | -13.68539 | -48.63192 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4366283a-06c3-3526-b1c1-8807c650fccf | -14.30507 | -46.01661 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce90ce78-2c67-37fa-97e5-77c40dbc3a8f | -14.93105 | -46.91238 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3e6dfc3a-f85c-346e-9fcb-2937f30f37bc | -13.20087 | -47.83292 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bb26e25-105c-3503-a4db-5fa2cba27660 | -16.05177 | -51.03983 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d8d3646-f755-3a6a-9b66-5d60dbede99b | -15.34758 | -46.26199 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7b85a5e-0c20-30a0-b8f7-9ab491ef4e77 | -15.32799 | -46.29511 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d064874-b839-30cc-9b8f-b2a2e480a2c7 | -17.37432 | -47.14669 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08e317b3-8b1b-3491-baed-d2b49b5bcefa | -14.87841 | -48.30851 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fe42e59e-a28d-339b-8db5-7735565ca017 | -16.0504 | -50.9007 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4d19a71-1df3-3928-a9d8-5d2dc70aee2e | -13.31946 | -47.18578 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56b92821-81ab-377f-9b5a-aa079fc283e4 | -15.667 | -43.2677 | 2025-10-03 04:34:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b7bc4b0d-6c74-3367-b793-7d67508358bf | -12.61117 | -46.96692 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 07560c19-3d70-3de8-aebf-7b6e0962c9a4 | -13.19645 | -47.7937 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f140f9d2-c1a7-377c-923d-80ebe4203715 | -14.42034 | -47.14343 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README121.md)
