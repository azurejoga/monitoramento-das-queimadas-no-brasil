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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a0608cd-b638-3887-b072-1716201882ad | -12.85567 | -46.94449 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b776ca26-a0ad-3a47-84da-77648b9d043f | -14.05019 | -47.9849 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22c74039-f697-3c79-adb2-f2f311a84565 | -14.56805 | -44.99961 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e221335b-26bc-3a2e-af76-69f7a0aa8aa6 | -15.44002 | -43.64734 | 2025-10-01 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2608010-613c-34b5-9118-7ea1031aeb0c | -13.85749 | -47.95678 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11a14836-7dee-3217-acb3-a69e044b4175 | -12.01798 | -46.6248 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec3bd8f1-5fc2-3590-be09-c5fa9089d81b | -14.10469 | -49.74806 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d20c39b-2381-34b6-8262-5e578604cc53 | -16.08781 | -51.03191 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 074f5165-d966-33a6-a7e5-d778892b5a25 | -13.28383 | -47.22756 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d4610f7-f865-3f47-9e9e-31a093b1a321 | -11.84807 | -44.98627 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| b9182488-9ddf-365e-87d7-d391722995b8 | -15.27228 | -48.01117 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92ce0ebd-46f7-3feb-a99b-9b63041803cc | -9.43367 | -54.71289 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ae28ea4-384d-3e2f-9d81-cc0fdf590639 | -14.73748 | -45.22667 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 381f99e2-1a21-370e-8cb9-4b037835bc08 | -12.39864 | -44.76263 | 2025-10-01 04:21:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fd485b7-1a8d-34d0-a8d9-5c826ef11395 | -10.10349 | -50.22434 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 31d86dc1-eae4-3567-979b-fddf28d3eabc | -15.12379 | -46.45581 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b85cbdbd-95a0-36a5-88e7-c87227955027 | -12.58449 | -41.28079 | 2025-10-01 04:21:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| b71375c5-55ab-3d21-9aa4-b8c519ea0af4 | -13.61764 | -47.63063 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37655190-e95f-37d1-b4e4-79d096b638e3 | -10.0418 | -52.09749 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cb7e500-e2a6-3b76-b376-bf08778b3390 | -11.43129 | -43.50026 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c406b5e3-c436-33f7-ad67-1be7004a6ac9 | -14.90226 | -48.12828 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f81f227e-7e7a-3453-a51c-49a5041063b2 | -15.46303 | -45.88638 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55ef38c5-b2ec-3661-85a4-d5739145fa70 | -15.24394 | -50.08135 | 2025-10-01 04:21:00 | NOAA-21 | MORRO AGUDO DE GOIÁS | GOIÁS | Brasil | 5213855 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ffa4d85-4164-3c75-b0e8-5cb25622f58e | -13.25769 | -48.44133 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 470db557-69c8-3c16-9f34-c240b4fc6d92 | -14.7078 | -48.21717 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d388b4c-f0d2-3850-921d-4877060a15bc | -13.73411 | -48.81529 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 554c49c9-1a39-32f4-85b6-8926f72fc2b8 | -12.08638 | -47.26127 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbe54e1b-3495-371e-a1c6-9e535f3b8124 | -18.33216 | -41.81006 | 2025-10-01 04:21:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a2fdf599-2c85-3093-b84f-3c2a2d8a5756 | -11.60594 | -45.03537 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6b0f8e8-a19e-3d3d-bca3-445a14cf7747 | -11.47085 | -44.98524 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce0d4fcb-f5ae-3a2b-991f-52810971260c | -13.75871 | -47.93599 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebde4a13-adc8-355d-a84a-e2cf7b05634a | -15.38761 | -49.19146 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50dcebcb-719d-3d39-95d0-1f36f0a1d7a1 | -11.84026 | -44.97046 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85d08055-1c5c-3b68-a892-2cbfced6df08 | -12.95266 | -45.16372 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48287047-93a9-320c-8c64-d5236abcd600 | -14.17353 | -46.11496 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc4704ce-9223-3b70-918d-bfa407d28a10 | -11.83639 | -44.97351 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd156e4a-debb-3020-ac72-57cadd2ba4db | -13.1736 | -47.78896 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 240455ff-21b7-3ade-8581-3548eb3ea1df | -15.78824 | -47.70396 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 969b49cf-6812-38b3-a896-28bc4b2b2c9d | -11.08608 | -47.83244 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6059bf95-6108-3a98-86bd-d33226037c13 | -13.9306 | -48.11287 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bb67aa2-45bd-3da3-9ab2-f589ffb42673 | -14.41378 | -44.91064 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e6353e1-c2bc-35dd-8eef-eaadd7ad6663 | -15.78017 | -43.7098 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d0a8df2-d4f7-3c4a-baeb-40dc04f2bc1c | -16.58487 | -45.12888 | 2025-10-01 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bebaac2-bc27-3966-bca8-05873cbd729e | -14.35422 | -47.13232 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fa1c25b-8e6a-307e-b623-38c54edd31e8 | -14.54597 | -48.24339 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09a9833b-2d52-35eb-bb28-ccc9deec92c8 | -10.90989 | -46.50829 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 4f452ba7-7909-3bd4-aef0-afcadbd60147 | -10.63544 | -48.52706 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94b9437e-6d95-3872-be01-4218833ff004 | -10.08258 | -45.62519 | 2025-10-01 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bce8415-4ae2-38e6-ac20-d7ecc453f752 | -13.73624 | -48.69524 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ad4f31c-f830-3676-bde0-b3605e574395 | -13.33289 | -47.85241 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4df3ecce-5619-3e9a-92bf-b449cb663eed | -14.72351 | -48.16307 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ade09081-69f3-3f05-be71-eccbc22934dc | -14.60257 | -47.30562 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8db4172-c08f-3a61-87fe-f863d821ad7c | -11.67813 | -44.28753 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d5ed769-a0d1-3189-bb76-35951de75ef1 | -15.16544 | -49.08831 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 65b72ed0-2c16-307c-8c67-8786b2a9bba6 | -11.59102 | -45.04389 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50cfc82c-4539-3abc-869c-93e3dd4b4a3c | -13.65156 | -48.03173 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1099bd28-95c4-3553-8b94-b6b38c810fd6 | -10.48923 | -49.367 | 2025-10-01 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b99c745a-6098-393b-8528-27501115a8b8 | -16.0862 | -51.04111 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 081db6e7-8f41-38aa-b44e-6a320dca85bb | -13.93399 | -48.11335 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03ce66cf-2a10-365b-8d32-9f84d104a56a | -12.21214 | -47.8067 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8b194f6-a1b0-31af-a89a-089eebbfed68 | -11.36342 | -44.97596 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d117fbe0-aaef-3543-a238-a8e09dd65cae | -12.69311 | -48.56122 | 2025-10-01 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7597f908-2524-3daa-baa4-1b68cd28c395 | -9.51516 | -54.7393 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d01989ee-d524-3db2-9c8d-cf4c688e006a | -15.07876 | -45.07823 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d90f0c8d-f989-3fd9-ad63-659a25d800cd | -12.43402 | -50.18029 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6696059f-38fc-3910-838f-0ffc23f12e53 | -14.54934 | -48.24402 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71f2bca4-791a-3f05-8cf5-ecba73e7c57d | -16.43308 | -42.40911 | 2025-10-01 04:21:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d562c25-08b7-313d-b4c8-376b67ad044d | -13.20725 | -47.45108 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50666e81-7fc0-3a5e-b706-6cba0e8ddaea | -14.43472 | -46.36101 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d086215c-5215-35d4-825c-66a7e0db66fd | -11.42723 | -43.50363 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dafe9ff6-0d5d-3512-9290-3c391ab9f6df | -12.82471 | -50.5765 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ac6cae32-d175-319f-b46c-6d423d19db94 | -16.02557 | -50.90461 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9f87c3b1-129a-3911-9baa-a7f84afa8a0a | -15.94652 | -48.11847 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0624fbf6-e648-33f1-a427-f04f931c996f | -10.20522 | -48.20716 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6530dc8b-ca94-3488-a31d-31dd7062efad | -11.68961 | -45.35316 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d704da1-a714-3072-bde9-5d8d700ce41c | -17.41859 | -45.46104 | 2025-10-01 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06805524-6736-3cdf-b171-4f62b83cc0af | -17.4047 | -47.16435 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcc18171-0a35-3fc2-b9dd-c09aaa9316ab | -14.70882 | -48.12594 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 869b2602-6ae5-3639-ba89-c0583e149f56 | -11.46752 | -44.98471 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6fe478e-ff0d-3bbd-8982-e78c0d929b20 | -9.44783 | -50.89976 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cfc5d878-a56c-33bb-9d36-8aff478e9194 | -14.79296 | -45.77943 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0301e43a-11e8-3cb8-91cf-c93c69341917 | -11.08483 | -47.84016 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 78e1a088-e24f-3f1f-b19f-20048d719c60 | -13.66444 | -48.03778 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d11f6c4-fb81-3579-b834-a1fc9d553294 | -11.07767 | -47.81933 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9dbb3969-2649-3801-b578-e757426ac539 | -14.90349 | -48.12081 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4324d65e-7308-3174-999f-e9645e446975 | -15.36094 | -47.0743 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61c842a1-525f-37fa-890b-3ddd704586d6 | -16.49686 | -43.73362 | 2025-10-01 04:21:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 579873d1-71e1-379a-bb98-824f1eb53057 | -16.25035 | -50.93319 | 2025-10-01 04:21:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c549ea04-10c1-302a-a149-5cd20d3a4839 | -11.84756 | -45.01176 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a61422e-c5f3-3a7e-b8dc-8b7e097b926b | -13.65493 | -48.03232 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37b57864-83d3-3cce-b42e-4c95e166b880 | -13.72997 | -48.69031 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31ebc8e8-9ad2-3dcf-a9eb-37cfa8f5bf12 | -14.89279 | -48.12294 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33771f42-04c6-33a3-a96a-f4b8edda4dc6 | -11.84588 | -45.00056 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5aaf406-a6f2-30dd-b162-44720dda3bd4 | -11.19428 | -47.20244 | 2025-10-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf23424d-3d33-3f40-81b2-7224141ee7cd | -11.94622 | -47.07555 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 775f6d01-4ceb-3813-a78b-ca57a16c2628 | -14.68495 | -45.27879 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 136c7c36-8274-3be7-a76b-70ba9d0069c6 | -15.54439 | -47.86633 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0d36015-79fa-3081-aec2-1f6059649e66 | -10.91712 | -46.48419 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09e1248f-c4e7-31dc-a242-bcec2947b6b0 | -12.87267 | -46.77306 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21e61a0b-b83f-3d7c-b68e-610e97ed00d1 | -15.06685 | -45.0419 | 2025-10-01 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README63.md)
