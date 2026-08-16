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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1210ba22-2681-32a2-8e19-32f67fcceaf0 | -8.9785 | -60.5349 | 2026-08-16 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c71cd07f-ca87-3f2d-a884-245178c46207 | -12.0282 | -46.4471 | 2026-08-16 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 29062cf2-965f-322e-83b5-4d50600190f9 | -6.7123 | -58.9412 | 2026-08-16 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 486ee575-3f30-3f82-9c7a-6fa8a35c84c6 | -8.9601 | -60.5165 | 2026-08-16 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 15a9a3f5-8180-37a5-b3ed-f457678e269c | -8.446 | -62.6752 | 2026-08-16 05:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.0 |
| b2e8ad45-49ab-39b2-9d93-f7b405d96293 | -8.4459 | -62.6942 | 2026-08-16 05:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ca971b06-e401-3ee0-8ed7-2444eb693e81 | -12.0286 | -46.4244 | 2026-08-16 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b1035a46-53ff-3f31-badf-258be0e5ee2a | -6.6377 | -59.0795 | 2026-08-16 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| caba1329-a773-3ec5-a24f-27d7dac3bef9 | -12.0091 | -46.4498 | 2026-08-16 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| edbe21f1-6585-370d-a2ff-a8b7f232f76d | -20.5083 | -50.12622 | 2026-08-16 05:21:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e06be830-56d3-3e6e-8492-318029189776 | -22.21376 | -48.62745 | 2026-08-16 05:21:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fbb5d97c-8bdb-3197-b6d9-11ab176e94b7 | -20.32637 | -46.72808 | 2026-08-16 05:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 878682e5-9b14-32bb-be75-f4ec951ad3c5 | -20.33323 | -46.72382 | 2026-08-16 05:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca766543-8a0b-348b-9643-4982cf83413c | -20.32689 | -46.72243 | 2026-08-16 05:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ba37b9a-4ca3-340e-96eb-b92f9e03329a | -20.33463 | -46.72484 | 2026-08-16 05:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f9d11af-abe7-350d-814c-25af06f5ad41 | -22.21954 | -48.62872 | 2026-08-16 05:21:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8eee2e07-f61e-32c1-9e94-feef19b839d7 | -20.32825 | -46.72376 | 2026-08-16 05:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 664cd4dd-52c0-32fc-b865-311dd96cf843 | -20.41171 | -51.36833 | 2026-08-16 05:21:00 | NPP-375D | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d06acb52-78c2-37c6-a4c5-c55e212309b1 | -18.92385 | -51.39251 | 2026-08-16 05:21:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2428926-77d5-3c37-8757-b871e45ed9fb | -21.79484 | -57.33724 | 2026-08-16 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05360c2d-5e00-3a4b-8bf0-1a8409a74bd9 | -21.53261 | -46.76069 | 2026-08-16 05:21:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 27c48985-2a86-3189-8d60-db7a21494e25 | -18.7259 | -51.01106 | 2026-08-16 05:21:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f44ce9fd-e313-361c-b610-1c8b25796a09 | -18.73068 | -51.01176 | 2026-08-16 05:21:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74fa3e2e-73dd-345a-b1ee-99bc1e2200b3 | -18.72686 | -51.01048 | 2026-08-16 05:21:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 799a1e74-148e-3998-af58-b714c60a85fc | -18.73132 | -51.00613 | 2026-08-16 05:21:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| efa3ba04-6168-3d79-95ad-b214b52ae394 | -20.50854 | -50.1256 | 2026-08-16 05:21:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 378c37f8-ee67-3282-a9a9-cb670ff5f87b | -20.50887 | -50.12231 | 2026-08-16 05:21:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 831008d3-dc1d-3c5a-a593-8f8a11c87dbb | -22.79513 | -51.39515 | 2026-08-16 05:21:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8663799f-86ca-3f4c-b181-4a0f3b2dd80d | -22.21996 | -48.62415 | 2026-08-16 05:21:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 775761d7-c097-3a44-a4b9-332d71f324a4 | -20.32777 | -46.7295 | 2026-08-16 05:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 846104fb-44dd-31a6-9fcf-4c6b152ff665 | -20.50866 | -50.12294 | 2026-08-16 05:21:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddf509d5-d0fc-327d-9fb6-b8b0bb1e1e09 | -18.73164 | -51.01115 | 2026-08-16 05:21:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f9fcff20-f09a-3d9a-bae1-1ea417bcd61a | -8.9785 | -60.5349 | 2026-08-16 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4b34ef64-f73f-3154-826a-2ddea26bed02 | -8.4275 | -62.676 | 2026-08-16 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6b66b001-ed95-3503-b27b-6fb1ae75dfb0 | -6.7123 | -58.9412 | 2026-08-16 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 50e267a2-19b5-38f4-aa22-3a91c43759a1 | -12.0282 | -46.4471 | 2026-08-16 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 1ccae001-a4b9-3cef-89e3-b91d0bf2c13a | -8.9787 | -60.5156 | 2026-08-16 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| b6c21f2f-5587-36ff-8788-a9e01e4bfc44 | -12.0087 | -46.4725 | 2026-08-16 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b050f4b6-fb53-3162-83d3-caf4f95e21a2 | -6.3137 | -43.6178 | 2026-08-16 05:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 2ec61e73-a211-3226-8a99-b44f70c577f2 | -8.96 | -60.5358 | 2026-08-16 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 283c2569-d4b1-3118-83e4-69711b700482 | -6.6377 | -59.0795 | 2026-08-16 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 64c89961-31a2-3fc5-a759-c13e319b342f | -8.446 | -62.6752 | 2026-08-16 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 05ada32a-d806-35cf-9f41-8dd8f0284fef | -8.9601 | -60.5165 | 2026-08-16 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| ede596c7-bb6b-3c6e-ad3e-6df25523b35e | -12.0095 | -46.4271 | 2026-08-16 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 50d55880-6cb2-3f30-b16e-cc2e9b7a2276 | -12.0286 | -46.4244 | 2026-08-16 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 026212b0-5e05-342b-ad5f-9e74a5a31e39 | -12.0091 | -46.4498 | 2026-08-16 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 4d8485bf-d9f4-3a7e-a664-7ffd2289533e | 1.58168 | -55.78567 | 2026-08-16 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26affc02-ee4b-3c28-9f07-af9759fd4493 | 1.58086 | -55.78065 | 2026-08-16 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 460f78cc-ac13-37c8-9624-a50ac402f06b | 1.58004 | -55.77562 | 2026-08-16 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a51ddb6e-9865-3fbc-a274-770dbd4bb39f | -6.82123 | -56.45699 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d3fcd32-869d-3f60-990e-9b497f1b6097 | -6.84375 | -56.42297 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b8a314b-42c0-38aa-a083-8c1942126026 | 0.69665 | -59.49737 | 2026-08-16 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 491cf12b-8d03-378f-8196-a9070f4ff344 | -6.60128 | -56.36547 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f876d4a7-f4d8-3dad-9601-bcf9c2749b6c | -6.6364 | -56.39545 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b1b91e1-4f12-397b-815c-11690fe9e7c4 | -2.9569 | -49.2761 | 2026-08-16 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 623c4f94-1c33-3dbd-864d-12d4ff955bda | -6.823 | -56.44481 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49ea338a-356b-39be-b6a9-2b84394f38ee | -6.78445 | -55.84151 | 2026-08-16 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54e6f874-d2a7-3ff9-b62d-fbda3d7fd54d | -2.49745 | -56.06118 | 2026-08-16 05:33:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c4d9a87-8feb-34d2-bac8-44bac93e0369 | -6.82241 | -56.44888 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0eb439b5-6e8a-36b2-8cf6-1ec2361f3c10 | -6.5988 | -56.35221 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54a1ab8f-9a64-3808-ac3f-7783f7d91910 | -6.85053 | -56.43657 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9eeae1b3-259d-3b7f-b6e1-e1757d341f7d | -3.94504 | -59.62841 | 2026-08-16 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93df7cd1-338f-35e4-be59-5f5662b7f1ad | -6.83767 | -56.43452 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8047b862-04a0-357b-b67f-edbd908cf760 | -2.50064 | -56.05787 | 2026-08-16 05:33:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3a2e5bf-7799-3135-9d79-24d455f3c4de | -6.85665 | -56.42483 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6576fa7d-19ea-342f-9ef8-db960e63945d | -6.84195 | -56.43521 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e3ca53e-c65b-3c5e-9f56-21ffbf459a84 | -2.76647 | -48.57589 | 2026-08-16 05:33:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9987ed3-0bf5-3bfe-bdab-af3030d265a3 | -6.84016 | -56.44739 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5fb454e-264f-380f-9f09-7fd3c0fb1b1a | -3.5181 | -58.94991 | 2026-08-16 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd17d649-d432-33ae-b487-303cc02ad331 | -2.36343 | -60.08377 | 2026-08-16 05:33:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d5e8b16-e3a1-3921-a5ce-67311f5eda55 | 0.96987 | -60.40789 | 2026-08-16 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 077c1706-8e4d-39bb-b176-6f7bd2c28deb | -6.82729 | -56.44549 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 764d4a64-c00e-3229-a029-09c575e3bd60 | -6.86036 | -56.42949 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73772379-d68b-3c97-8f74-916fee108820 | -6.54539 | -56.54137 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d153bbb-bbed-33e2-b79f-864cf1be40d2 | -6.85975 | -56.4336 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f39aa4b-a887-3fa9-a5e6-1ae4ce2bf3b4 | -6.37374 | -58.33024 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a652991-cb05-3de5-af7a-2095ca816dac | -6.82491 | -56.46173 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dbb56d5-f5a5-36e2-8f23-00aea72ba7b7 | -6.81754 | -56.45222 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9619d7ce-389a-358f-95f7-e44f37105277 | -6.2482 | -55.62022 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f3f2b3ba-7ab1-382a-a48d-4d483da84d19 | -6.86467 | -56.43002 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c53e51ea-5a77-3f70-89f0-8c7fe5678d2a | -6.86771 | -56.40955 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17317a2a-9878-304e-bbd7-c08bd23a0fec | -6.59939 | -56.34815 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 000cba69-df9e-33a7-974f-f0b10e89538f | -6.85174 | -56.42837 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b81a137-b7f2-3780-827b-d0a4c09362c7 | -6.82789 | -56.44139 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2611b2fd-9f21-363f-ba10-2e027b2bd972 | -6.83588 | -56.44671 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| deb0b311-3fce-3bdb-acc6-d14d47fb4c05 | -6.82919 | -56.46241 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8a11501-bf9b-378a-8a11-3e39037f0df5 | -3.28995 | -56.99273 | 2026-08-16 05:33:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77663443-eabe-35e0-b462-1bc27b978b0c | -0.00321 | -60.57133 | 2026-08-16 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd9f784f-cdfa-3d20-87a0-6fc469067f2d | -3.94101 | -59.63164 | 2026-08-16 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e80bdff-e4ae-3f15-ad2e-acc8f891616b | -6.3782 | -58.32619 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9108097-4cb1-3d1e-8aae-e05c6b85f5a4 | -6.63214 | -56.39456 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a065c0bf-86eb-3dc1-89d1-bedb72b940d8 | -6.84624 | -56.4359 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 563b71ba-21d7-358f-91b5-c78735311845 | -6.12883 | -55.81118 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40ef3a2d-4a85-31c6-aac0-6b3a97f154b8 | -6.83086 | -56.42101 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a0694be-0812-3f4b-86f8-9bf08348b825 | -3.23557 | -61.16809 | 2026-08-16 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eff5dbb7-07d7-368c-94fc-41374f5fe826 | -6.37102 | -58.32275 | 2026-08-16 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 367df979-6eee-3fb8-9326-19d1ceddefd7 | -6.83707 | -56.4386 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d50b198-42bd-365c-89d1-2410cf9a6272 | -6.81208 | -56.45966 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac9ebaed-de11-3403-95bd-5bee651c42f3 | -6.83346 | -56.46317 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a15c0dde-1776-3fe1-9001-5a6230a360cc | -6.84685 | -56.43178 | 2026-08-16 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README47.md)
