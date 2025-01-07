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
| 57ee7fab-1805-3a25-9b79-4fae506852c3 | -12.36351 | -52.49001 | 2025-01-07 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15f29a2f-7ebd-3613-9638-10b61bd5291c | -21.88181 | -56.11077 | 2025-01-07 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 574c1743-2dd1-3eba-b205-7be68325c455 | -21.56484 | -54.20529 | 2025-01-07 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc60cdfc-9eb8-3129-91ed-a69dc6a657f9 | -21.55851 | -54.20012 | 2025-01-07 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75103902-5e46-3e8b-a48c-2cff54779ef5 | -24.08246 | -51.02198 | 2025-01-07 04:55:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4020d5cd-e17c-3336-af26-2e5e48a3d5d2 | -21.54165 | -48.63532 | 2025-01-07 04:55:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd272bb0-c6d0-35c4-baee-7f706a00f989 | -21.55505 | -54.19953 | 2025-01-07 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8438aa58-2b16-3bf8-b29b-d04e2e3af7da | -24.08295 | -51.01781 | 2025-01-07 04:55:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b61e628b-f09a-374b-8a86-b88a90eec2fc | -20.70635 | -55.32008 | 2025-01-07 04:55:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 803c26f0-6ccc-3379-9973-e71fb1011817 | -23.58002 | -51.44889 | 2025-01-07 04:55:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bd4f4c6b-5157-3ae8-b4c8-566fb3ffc7cf | -19.33606 | -54.16795 | 2025-01-07 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80e34d1c-defd-39fc-b090-f62899182ca6 | -29.47479 | -56.42587 | 2025-01-07 04:57:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 674686c0-96e6-32a6-9554-6725d0554b40 | -29.61863 | -51.95687 | 2025-01-07 04:57:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3541995b-5d14-36f8-be3d-7b547a1316f8 | -29.62289 | -51.95749 | 2025-01-07 04:57:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 600c46e1-3cfa-3eba-bf9f-561f15f38175 | -29.47279 | -56.42728 | 2025-01-07 04:57:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 6d2e7989-9068-3e27-ae04-b920549fc26a | -27.37291 | -51.65043 | 2025-01-07 04:57:00 | NPP-375D | CAPINZAL | SANTA CATARINA | Brasil | 4203907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a7eaae8a-6afb-3f83-89bd-2089949611d5 | 3.91133 | -60.50079 | 2025-01-07 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3150620-4112-360c-b94f-28d1708e1930 | 4.32677 | -60.82032 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 229eb909-2efe-3fb3-8e18-b0d4d35a0ad1 | 3.94845 | -60.20971 | 2025-01-07 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffdff427-dbd8-3cc3-a9d4-e6cd882c2309 | 3.6631 | -60.67364 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e2d8a7c-3e64-309b-923d-f46ba963765a | 3.67481 | -60.70006 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f350c5f2-e3d9-30f0-a423-0c2da5b12f9a | 3.70829 | -60.61526 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1140ac89-3091-3718-b9b4-a4e1a15106ba | 3.73632 | -60.59458 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a5d0fd9-2e5c-3017-a79d-68e3a6924b05 | 4.35136 | -60.87959 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54143e44-bdc7-3640-8ded-0786001d457d | 3.73936 | -60.59185 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 335cf4f9-826e-3c40-91ff-5c9246755886 | 4.34751 | -60.88026 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39b13d69-2cce-3de8-9c71-67a628fe51e4 | 3.73564 | -60.59004 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c2c1239-b5d9-3bfc-a89d-b84700afdeac | 4.13663 | -59.85122 | 2025-01-07 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b82be32-421a-32e9-9cb6-5f21b8f4ee72 | 3.7356 | -60.59243 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc66f99e-641b-3511-b32b-e1eb32732f21 | 4.34295 | -60.87617 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f980482-f97a-3147-a1e4-91e5bb5fe413 | 4.32504 | -60.82318 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcab2a61-9f39-361d-a76e-d6540c4f7cbe | 4.3087 | -60.81934 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96564fce-147f-3cf3-94f8-c2ca70626ca1 | 4.32751 | -60.82531 | 2025-01-07 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3365fd33-d0b8-3e09-ae19-fd1dbd88f732 | 2.60803 | -61.314 | 2025-01-07 05:12:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90ed479b-9349-3632-a022-0a5a08087df8 | 1.34722 | -60.03456 | 2025-01-07 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf3fba14-933c-385f-a850-f3db5a65284c | 1.3514 | -60.03803 | 2025-01-07 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bcf0595-b39d-3323-bf99-347267d5044b | 2.03012 | -60.88069 | 2025-01-07 05:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c917641-b50d-3c36-a0d9-a5a6673f436e | -4.06438 | -54.70729 | 2025-01-07 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81e58e0a-2ff3-39dd-a0dd-1037a08d246b | 0.59642 | -60.46713 | 2025-01-07 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cedfc696-5e41-3911-bb20-109c9f8168d4 | 2.02638 | -60.88129 | 2025-01-07 05:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dfe7d4e-e06d-3c29-9325-34972a5205a3 | 1.35077 | -60.03403 | 2025-01-07 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77916e88-5e18-3503-aae9-dcc467a1e4f1 | 2.02942 | -60.87621 | 2025-01-07 05:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a24d33d6-afda-33f4-bdfd-ecfa5ffde9d0 | -8.52752 | -35.74428 | 2025-01-07 05:16:00 | AQUA_M-M | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| af1f96bb-42c6-3e9a-88c1-a14b37d5858a | -5.61227 | -42.82678 | 2025-01-07 05:16:00 | AQUA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6e918b82-6c6e-3ee4-a7ff-1efec503929d | -8.52724 | -35.7395 | 2025-01-07 05:16:00 | AQUA_M-M | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| ec14c340-b9ed-3ae7-a27e-226d8dff2be3 | -12.35322 | -52.4919 | 2025-01-07 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce46ff6c-f290-3267-b0b5-8c581884c694 | -9.28279 | -56.89412 | 2025-01-07 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c9c3e3a-daf9-3855-b5bf-42afd2983a77 | -9.93324 | -59.93864 | 2025-01-07 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c131f699-85bb-3836-a4f1-c88adcfacecf | -12.36292 | -52.49317 | 2025-01-07 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| df2155c4-a961-31b9-b30a-a88ac3f95a74 | -12.36847 | -52.48845 | 2025-01-07 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dc894abd-55db-3648-88df-c0de5e7f8182 | -12.36777 | -52.49383 | 2025-01-07 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3875cef8-682d-34be-adfe-b8ebb66c7ed2 | -12.36361 | -52.48781 | 2025-01-07 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 504585b2-3806-3f20-9eba-ef8c3d5dc3ae | -12.35807 | -52.49254 | 2025-01-07 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfe2a6dc-2044-3a42-b636-73cbaa4984bc | -20.96512 | -49.76183 | 2025-01-07 05:18:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6b9ea67b-ec6b-37d2-a9bc-b64f435c1f5a | -20.95917 | -49.75574 | 2025-01-07 05:18:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a214f515-ed4a-342f-9a48-efaf95116ecb | -20.71793 | -55.56156 | 2025-01-07 05:20:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3607f24-92ec-36a1-84cd-9d45b011e05d | -21.55537 | -54.20167 | 2025-01-07 05:20:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf91ddf3-1ec6-3d2f-a494-598635ef61d7 | -20.70567 | -55.323 | 2025-01-07 05:20:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afeaadf4-2e89-398d-a788-625d02d56159 | -21.56026 | -54.20235 | 2025-01-07 05:20:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 987cdff0-241e-3a9d-9d70-604168d84d86 | -21.56087 | -54.19657 | 2025-01-07 05:20:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 32431d2a-3f2b-3623-b655-5ce06e2ce298 | -21.56454 | -54.20861 | 2025-01-07 05:20:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6befc191-d012-382c-981d-2b18bbd4c560 | -21.55598 | -54.19591 | 2025-01-07 05:20:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 512cdbff-ce03-3e32-b348-e58986af2916 | -24.08302 | -51.02097 | 2025-01-07 05:20:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2105d35e-2209-393e-991d-e3e1c8c4d524 | -21.87934 | -56.11676 | 2025-01-07 05:20:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab1fa054-d086-3e7a-b9c5-ec67cb8a47a7 | -21.87985 | -56.11245 | 2025-01-07 05:20:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8057ff9f-b385-35b7-9511-ddca5d582a86 | -27.37429 | -51.65503 | 2025-01-07 05:20:00 | NOAA-20 | CAPINZAL | SANTA CATARINA | Brasil | 4203907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f31a3bed-9f6d-35aa-b27f-f7b41865c88f | 4.30605 | -60.81841 | 2025-01-07 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f56834e0-2df9-3e91-94f1-aa93030f125f | 4.34116 | -60.87234 | 2025-01-07 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6d498255-a436-3652-bd07-38f92e4461ce | 4.34167 | -60.87543 | 2025-01-07 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ff2ef5cb-5d6c-3d77-996d-01cca7b56a16 | 4.34779 | -60.88092 | 2025-01-07 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7649076-1e06-3e74-95cb-3ec311ba1b05 | 2.02836 | -60.88071 | 2025-01-07 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b35b87d9-c976-3cb5-908a-2c3c3f7f017d | 3.65526 | -60.67312 | 2025-01-07 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30eddd05-280a-3df4-8575-3289d3223402 | 1.34636 | -60.03282 | 2025-01-07 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9a59f73-ae1e-3f58-962b-62a08410e3d5 | 2.02783 | -60.87747 | 2025-01-07 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fc314fe-2a0b-3265-b61d-3d00878e9378 | 2.60759 | -61.31213 | 2025-01-07 06:05:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cfeee2e-1ded-3330-9e0a-22318cc2207f | 3.66045 | -60.6722 | 2025-01-07 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c89f37e-2ca4-378c-ba73-f849aa0cc132 | 1.3476 | -60.04044 | 2025-01-07 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4d97c5d-c2ac-332f-ac5a-326d5ad26089 | 1.34698 | -60.03667 | 2025-01-07 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75a42225-710a-3b65-8b6c-bc31374f26f4 | -9.9291 | -59.90532 | 2025-01-07 06:07:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c840922-adae-33a0-b146-2f18a6f48b74 | 1.34742 | -60.02617 | 2025-01-07 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dc12db2a-77bb-3102-9d46-81b1ee2d3e9c | -6.00286 | -47.90794 | 2025-01-07 12:55:00 | TERRA_M-T | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e87e0e39-b5d5-3a10-a3ec-5d3f07113f90 | -24.62563 | -53.32245 | 2025-01-07 12:59:00 | TERRA_M-T | CAFELÂNDIA | PARANÁ | Brasil | 4103453 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 84cde08a-9af1-37b5-948b-bb92e4037b87 | -21.55508 | -54.2018 | 2025-01-07 12:59:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b0cf374f-65c8-36d5-a7b4-77319332e5a6 | -21.41054 | -55.08174 | 2025-01-07 12:59:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 28f8a111-d8dc-387f-b78b-b7119b15e6f0 | -20.87249 | -54.46777 | 2025-01-07 12:59:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 30b8b023-465a-3cb0-8373-0289e396d596 | -21.55642 | -54.19224 | 2025-01-07 12:59:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5b957cff-c368-314a-ac7f-ff0b91712f63 | -21.21052 | -53.16227 | 2025-01-07 12:59:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 652307c8-fb27-36e9-b57e-77f956fda336 | -18.8827 | -54.01882 | 2025-01-07 12:59:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e5f3b99f-272c-3c60-b491-ce4756af76f3 | -23.4228 | -55.37555 | 2025-01-07 12:59:00 | TERRA_M-T | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 790a7552-2d2c-3d72-83a7-1eb0b9680e01 | -21.56398 | -54.2032 | 2025-01-07 12:59:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1da784db-ba69-3845-a6e6-f151c57bcbbe | -22.41066 | -54.34018 | 2025-01-07 12:59:00 | TERRA_M-T | VICENTINA | MATO GROSSO DO SUL | Brasil | 5008404 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 0bb56359-d4cd-36bc-ad73-0851defbdfb9 | -20.73458 | -52.03719 | 2025-01-07 12:59:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b43ebbcd-5bb5-341f-8383-e821ebec1e0c | -21.20917 | -53.17233 | 2025-01-07 12:59:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 04b123f6-b970-3164-ad22-f8feb226ea6b | -23.99712 | -53.76741 | 2025-01-07 12:59:00 | TERRA_M-T | IPORÃ | PARANÁ | Brasil | 4110607 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| aec628a2-a8e2-3c02-a777-17dc48a1c19a | -22.14665 | -53.03167 | 2025-01-07 12:59:00 | TERRA_M-T | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 464d2e2b-0309-30ea-afc3-0034674fdebf | -16.71932 | -53.93256 | 2025-01-07 12:59:00 | TERRA_M-T | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a233c61-f581-300a-a8ba-c258e4047169 | -22.1453 | -53.04198 | 2025-01-07 12:59:00 | TERRA_M-T | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 99f6640d-7137-398c-816c-fa0dcf5fa5bb | -26.07771 | -53.71554 | 2025-01-07 13:01:00 | TERRA_M-T | SANTO ANTÔNIO DO SUDOESTE | PARANÁ | Brasil | 4124400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 36b77e8e-c026-363c-b17d-918667c61647 | -26.58889 | -52.09615 | 2025-01-07 13:01:00 | TERRA_M-T | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 18ee88bc-ba60-3ca3-8dab-67be09bf2e43 | -7.8223 | -37.6174 | 2025-01-07 13:30:00 | GOES-16 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 126.1 |


