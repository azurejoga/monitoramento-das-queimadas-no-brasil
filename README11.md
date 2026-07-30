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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1704baf6-6c46-3c4b-8417-dfe70cef2c5d | -10.95699 | -49.80819 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c001831-628c-375b-a1bf-47164bd50613 | -9.47539 | -63.27935 | 2026-07-30 04:59:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cef4993-a2d0-36a0-965e-dec6edd80cf4 | -9.47653 | -57.3185 | 2026-07-30 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 640adf81-d106-3c61-91ac-80e73b628b43 | -11.93273 | -43.44149 | 2026-07-30 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8060ab1c-2cee-364f-9bc5-99cc1586e1cb | -11.39105 | -50.12475 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 862e35a5-2cbf-329e-88b3-fdc6ebfa2f85 | -8.82979 | -66.75423 | 2026-07-30 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3530512-f184-34b4-923b-98f9fcb7bac1 | -13.74114 | -51.8914 | 2026-07-30 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e8605d6-9b29-3902-aea8-db349a407682 | -18.2374 | -42.21 | 2026-07-30 05:00:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| 04cca56d-abd0-32cd-82b6-3a294d221dc5 | -10.9397 | -43.0593 | 2026-07-30 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 70b283d6-5a89-3a58-aa63-7e9d7cdc0ba6 | -15.39509 | -55.92339 | 2026-07-30 05:01:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49ca3d18-0663-32ca-82a9-ba23bc3bd17e | -20.57466 | -57.2648 | 2026-07-30 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd5c58e5-0f1a-38b8-baa6-95e73daaf043 | -16.49275 | -54.59414 | 2026-07-30 05:01:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f9dc8fa-873c-379e-8565-bd8af0a0c319 | -18.47466 | -51.72932 | 2026-07-30 05:01:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 037234c8-ea19-3216-b153-64d5b5768c7c | -22.76424 | -43.74711 | 2026-07-30 05:01:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4d593d3d-5e84-3abc-bff0-9fd8c5c6ecb1 | -14.95963 | -56.10055 | 2026-07-30 05:01:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c8b7999-7b0e-31bd-b5cf-42154c5f5e60 | -20.57077 | -57.2679 | 2026-07-30 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 59aabfc5-5100-36a0-9d80-d633c91bdd33 | -21.97823 | -57.59438 | 2026-07-30 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcd09a06-7c95-3bab-8266-4878a93ba192 | -19.17734 | -47.35456 | 2026-07-30 05:01:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3170b8d6-51da-38e1-9bc9-434b61b5daa4 | -18.59754 | -48.20457 | 2026-07-30 05:01:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73e0dc5c-5d8f-38e7-bda3-1def6bbde24f | -18.47918 | -51.72617 | 2026-07-30 05:01:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 148578a9-208e-3c31-9727-75568313f5c8 | -18.35451 | -47.19799 | 2026-07-30 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de33831b-8d6e-3f7b-8515-7f817e3f5aca | -20.64253 | -57.28797 | 2026-07-30 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d0881d8-388e-3879-a006-f2b97ee59738 | -18.35492 | -47.19402 | 2026-07-30 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a3b29e2-9744-3a36-8e41-0f287f8201f9 | -20.78848 | -57.87624 | 2026-07-30 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 596326f0-f6c0-32dc-8e2b-153cbca9d410 | -18.59243 | -48.20394 | 2026-07-30 05:01:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8c3399c-5d97-397f-8eee-b3fbf7c832f5 | -15.3984 | -55.92393 | 2026-07-30 05:01:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ffe2ca7-9581-388f-9e86-2531eb84ace2 | -21.88722 | -56.26257 | 2026-07-30 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96d83882-c64a-3a93-89b8-22b1cdb39da0 | -15.39619 | -55.91626 | 2026-07-30 05:01:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed9441ee-5c28-3ea7-b574-7792b7d6a4f7 | -21.45051 | -55.46236 | 2026-07-30 05:01:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9d45f71-18ad-35b8-89b1-fa5d24813f90 | -20.79238 | -57.87315 | 2026-07-30 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c274f8d6-6830-3153-a7e4-fbb4d08f6cc4 | -19.17773 | -47.35072 | 2026-07-30 05:01:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fe94aee-211c-3e75-b3c3-5d5d6e0a983f | -21.88665 | -56.26645 | 2026-07-30 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e46bb112-d0ab-3eeb-8926-d67f4a056de3 | -20.6182 | -57.29127 | 2026-07-30 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3c70eb1-452d-38df-8e2d-f274977b5b87 | -19.82919 | -48.20493 | 2026-07-30 05:01:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 497279cd-9f16-39d9-9cbd-afca6dffe43c | -19.82885 | -48.20813 | 2026-07-30 05:01:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6fb61b5-2b81-3627-af66-e2cc21e87674 | -22.76286 | -43.74309 | 2026-07-30 05:01:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c6184656-02c6-3071-b193-b99ecd09454c | -19.83436 | -48.20571 | 2026-07-30 05:01:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c72909c-7808-31d2-83a1-8a375eccbaa6 | -22.76331 | -43.73574 | 2026-07-30 05:01:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3ccdf442-d7b4-3800-9c2e-0edd85470e44 | -17.39906 | -47.33314 | 2026-07-30 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fab35832-9a4a-3947-bf7c-50663053169d | -20.6268 | -57.34564 | 2026-07-30 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b5efd13-7614-3669-91a2-5faca598c193 | -20.78575 | -57.87197 | 2026-07-30 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 438ba982-4484-3958-a51d-2b4c3cdfed52 | -22.76476 | -43.73935 | 2026-07-30 05:01:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 7c550c46-130c-35df-baeb-681b87c5eec6 | -21.98212 | -57.59124 | 2026-07-30 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a1930d3-c574-3325-8942-afd9ede78d82 | -20.62152 | -57.29185 | 2026-07-30 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c0c8dc5-5ce6-3122-8c3d-91904842433b | -18.47514 | -51.72559 | 2026-07-30 05:01:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| affe3d23-07fb-3ff2-91aa-38ba131f554b | -14.95632 | -56.10001 | 2026-07-30 05:01:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ef6ebae-9118-30d6-a3f7-373440379312 | -10.9397 | -43.0593 | 2026-07-30 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 8ab1361e-82ec-3517-8a87-3b720b0826ef | -10.9397 | -43.0593 | 2026-07-30 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| ff738ac3-f9b8-321b-952e-6d938946bba4 | -10.9397 | -43.0593 | 2026-07-30 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 7fe57480-f0ef-391d-8ec4-8e22697ae3f0 | 1.67901 | -60.1396 | 2026-07-30 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b2010c4-bf33-3327-98d1-4d860ec6f721 | 1.76996 | -60.22794 | 2026-07-30 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e3b05d9-11b7-3af3-8cd5-00c675b4a3df | 1.76715 | -60.23203 | 2026-07-30 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3725d4c8-b31d-3396-b5ae-e29a0c042bb3 | 0.92397 | -60.53814 | 2026-07-30 05:31:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2efdce36-16e4-36bf-b360-106f8b745dbd | 1.77052 | -60.2315 | 2026-07-30 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fc97a77-2639-3898-83cd-6a19d85a632f | -3.67566 | -49.47971 | 2026-07-30 05:33:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae602127-97d2-3cf1-9e4b-93d379e2d111 | -4.3708 | -47.76883 | 2026-07-30 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b6c5030-35e5-394f-99b5-ca557f6acd21 | -4.19477 | -56.30404 | 2026-07-30 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cba3035-e84b-3bf3-b4e5-26f6d41b31c4 | -6.65142 | -59.11041 | 2026-07-30 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2e7d7469-415a-3d7b-bf16-0d205b0d0d76 | -3.67813 | -49.47815 | 2026-07-30 05:33:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b39d6073-608f-33f2-8009-35d1c2b7d386 | -5.75129 | -51.7076 | 2026-07-30 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6196368a-a123-321d-98af-f4cc46700f2f | -3.18183 | -48.02552 | 2026-07-30 05:33:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e57eafa2-4af5-3022-a716-b6b48018d8fa | -5.75084 | -51.71077 | 2026-07-30 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9039edc4-b3cc-3d5c-9f2f-2934b27c10ae | -4.36815 | -47.76915 | 2026-07-30 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aa55f77-61e3-3942-9b63-ede93a3cd720 | -7.3768 | -57.18182 | 2026-07-30 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 832cdea3-7d92-36eb-82c3-daaa11db7a2a | -6.65823 | -59.11146 | 2026-07-30 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a62881c6-5f56-3ac1-9570-16f88e723231 | -3.68052 | -47.64506 | 2026-07-30 05:33:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbc8e8dc-e0ad-377f-a52e-6c6e4224884d | -3.67504 | -49.48399 | 2026-07-30 05:33:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a147416c-9675-35b1-a6c3-7199fad7e42d | -3.68717 | -47.64602 | 2026-07-30 05:33:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f182ffae-1beb-30c1-84ec-39dd0baf35a9 | -3.6775 | -49.48238 | 2026-07-30 05:33:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f8e9fb96-33c8-3372-8b85-136eed00fc17 | -5.23416 | -56.0081 | 2026-07-30 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d36286c0-2749-3503-95e7-6c68aebf2912 | -5.75175 | -51.70441 | 2026-07-30 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e431a6a-b14f-38a3-8dd5-bb0f564b654c | -3.16574 | -48.13507 | 2026-07-30 05:33:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 494f7ea1-2aa9-378a-830f-d65df6eda606 | -6.65199 | -59.10674 | 2026-07-30 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ee6979f1-19c1-344a-9a25-1b13f7cb1d42 | -3.18261 | -48.02016 | 2026-07-30 05:33:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ccb02c8-33e5-38bc-a679-d2221fa9e493 | -9.06323 | -59.12256 | 2026-07-30 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b38c644a-f1cf-3bf4-8342-5d4025308cd2 | -9.61312 | -47.76425 | 2026-07-30 05:33:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9b3d63b7-f65f-38a2-9d1e-9f69d0054728 | -6.65539 | -59.10726 | 2026-07-30 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 98bd8350-3e15-36e3-8214-6676fbbe7a46 | -6.6588 | -59.10778 | 2026-07-30 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e00c11b7-7816-3cc1-9d92-ef1a2129c020 | -3.17217 | -48.13586 | 2026-07-30 05:33:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f96cc387-f410-3bbe-a6ae-8dbbef598567 | -6.85711 | -56.53027 | 2026-07-30 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6348e0f-e88e-3671-8868-8a8455acce9a | -9.60889 | -47.76489 | 2026-07-30 05:33:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37d16709-3698-3429-8330-99011bef88ef | -5.74557 | -51.71006 | 2026-07-30 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f43cc4f7-58d9-3461-9262-fbab22e58655 | -6.65483 | -59.11094 | 2026-07-30 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ded04029-ed4e-35eb-aea3-fcb4060f6d82 | -9.61604 | -47.7654 | 2026-07-30 05:33:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a8a16d77-98fb-34e2-87f3-f80e822ad27a | -4.36894 | -47.76359 | 2026-07-30 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de5b39f5-4b1f-3084-8c2a-0b2eae0c24cf | -11.97637 | -63.1682 | 2026-07-30 05:36:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f56364ff-1cb2-31b6-b234-4398ae6ed85f | -8.91593 | -64.99884 | 2026-07-30 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09f194c1-3107-3314-b65b-02576ad96f25 | -13.33275 | -54.29025 | 2026-07-30 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00e15181-7ba9-30a1-b883-a266c12e95e9 | -11.41742 | -50.09415 | 2026-07-30 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bba77f69-b8aa-3b05-86c7-94ffadab5d8b | -13.0565 | -60.65511 | 2026-07-30 05:36:00 | NPP-375D | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37447392-3044-3d4c-8d8c-ea9a7f2659b4 | -11.41468 | -50.08944 | 2026-07-30 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 336d051c-c699-353b-bca3-42fe3b5f3bc2 | -12.82825 | -62.14758 | 2026-07-30 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36eca2c9-ba7a-3c8c-a618-3e5273df0c61 | -8.91221 | -64.9982 | 2026-07-30 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1f289b3-795a-390e-8d5a-66aaf3827e37 | -9.92081 | -67.04626 | 2026-07-30 05:36:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f268446-8b8e-3e33-b6c0-f44d11618430 | -11.42042 | -50.09537 | 2026-07-30 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a958dd27-9054-3e2a-8022-ebaf22701c64 | -10.08008 | -60.49585 | 2026-07-30 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 732b14fd-16f3-3e35-9f6d-74abaa20fbb3 | -9.37898 | -58.21032 | 2026-07-30 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3528c82e-ea52-3476-9e5b-a91b24297ad6 | -8.82672 | -66.75828 | 2026-07-30 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 794c4eb1-1303-31ca-84db-abd029b8bbbe | -10.47462 | -62.4507 | 2026-07-30 05:36:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e93162a5-a08a-3d82-bb62-d29f6761affa | -12.73371 | -60.11737 | 2026-07-30 05:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README12.md)
