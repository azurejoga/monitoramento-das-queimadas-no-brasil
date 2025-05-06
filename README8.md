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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37478560-dd4f-3b64-8e5a-42f88d589071 | -13.04831 | -53.71014 | 2025-05-06 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62438e8a-03c0-353a-bff5-a0cc0c916f17 | -17.15111 | -54.01611 | 2025-05-06 04:46:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa9b9127-da11-33f8-a004-98f831d42eb4 | -15.08026 | -48.94423 | 2025-05-06 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60c95455-3637-3998-be85-1eb6d5c418ce | -23.60084 | -49.01034 | 2025-05-06 04:49:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 99d77498-8e5f-3ad7-a24a-35a78d316a44 | -21.03 | -48.98931 | 2025-05-06 04:49:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f22642a5-ae04-399a-8785-8301188cbd6d | -23.60156 | -49.00946 | 2025-05-06 04:49:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 420251df-3dd3-3c4a-9943-22b4816a0017 | -20.17371 | -54.39921 | 2025-05-06 04:49:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b7fc927-3106-3dfa-af40-46d94e3dd4e4 | -21.72544 | -56.10884 | 2025-05-06 04:49:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad57a2e0-7be8-3b58-a0b5-9717a24e15bf | -21.03407 | -48.98984 | 2025-05-06 04:49:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6b309426-a592-3eb8-8a0d-601313a2f0e1 | -21.03453 | -48.98603 | 2025-05-06 04:49:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0e73c103-a0cd-3d11-bf9c-4a3691373dac | -23.04468 | -49.89559 | 2025-05-06 04:49:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 37b357d2-94c2-3768-a13c-cd87f8bd1aa5 | -21.03042 | -48.9858 | 2025-05-06 04:49:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f76b0768-75e7-3c5e-afab-4c71a96e1133 | -24.24343 | -50.73981 | 2025-05-06 04:49:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fe2ed1de-5a7a-3568-bdf2-8541a796825a | -21.18336 | -53.18109 | 2025-05-06 04:49:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 805eff68-3e9e-3527-b4c8-cb67e890b795 | -21.3644 | -48.62778 | 2025-05-06 04:49:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 45a12fb2-2b8f-3b84-a858-282bd548b594 | -21.034 | -48.99012 | 2025-05-06 04:49:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0048bd51-3721-3e9b-b269-1eb386ec73c9 | -20.98575 | -56.66078 | 2025-05-06 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e496a66-a72a-3ed8-8ed2-8b7d1608e141 | -22.90636 | -49.69011 | 2025-05-06 04:49:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e9109ea0-b437-3eb7-af88-eb523b48d654 | -21.02993 | -48.98959 | 2025-05-06 04:49:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c350896f-ffa0-38af-8e38-5d21425c660b | -23.03911 | -50.44205 | 2025-05-06 04:49:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8cc26318-c30f-31de-b535-01496bf16488 | -22.25291 | -54.78082 | 2025-05-06 04:49:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0b6cf2df-6479-31f4-a9f3-b2dbc8f2e7e2 | -21.82573 | -53.6128 | 2025-05-06 04:49:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff4f1da8-b87c-3cc1-8d40-1767df0934bb | -20.47773 | -53.67395 | 2025-05-06 04:49:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 058a7a6b-9c84-3bf8-b475-6598277277ad | -22.53909 | -48.81364 | 2025-05-06 04:49:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fddbc164-eb84-3af3-a633-afcf8eae2415 | -21.03449 | -48.98631 | 2025-05-06 04:49:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 86932462-a9ff-33ed-8038-1970df8ce51c | -22.66861 | -49.80997 | 2025-05-06 04:49:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff008968-d8d7-31f6-a628-9f7623a3215d | -22.04197 | -47.93326 | 2025-05-06 04:49:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96f098a6-187f-3787-8008-08f86facaba2 | -21.72481 | -56.1127 | 2025-05-06 04:49:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee99019f-6077-3340-bbb4-33348a15c3f8 | -23.60133 | -49.00629 | 2025-05-06 04:49:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c56c889-249e-3629-ae3f-4632a76f7749 | -23.52509 | -47.83444 | 2025-05-06 04:49:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| db00af67-92f7-3bc8-a7ee-d20017798e39 | -23.26755 | -55.35892 | 2025-05-06 04:49:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e7071cb1-2230-364d-a479-4e51decfb615 | -23.6011 | -49.01354 | 2025-05-06 04:49:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| cf16364b-d31a-356b-b276-e16410d4dafd | -23.5219 | -47.83523 | 2025-05-06 04:49:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| eba6ea8d-8273-3dd9-bbb6-9f7238fe0780 | -21.72207 | -56.1082 | 2025-05-06 04:49:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d4e99c3-1922-3f6c-8643-6c9fd79c711c | -23.52058 | -47.83376 | 2025-05-06 04:49:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 698df14c-ca27-3b69-94eb-3856e32b0099 | -21.03046 | -48.98552 | 2025-05-06 04:49:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 184092d8-d0f6-37c2-af8d-40a29e08e6e7 | -23.60203 | -49.0054 | 2025-05-06 04:49:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe56eb13-104d-308b-ad67-a082d98f7d04 | -21.72143 | -56.11207 | 2025-05-06 04:49:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67127d02-56f9-3498-8b74-fa2aa1e7adab | -21.30558 | -55.63774 | 2025-05-06 04:49:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0bbaacd3-11bd-3abb-a67f-de78996ab991 | -23.60183 | -49.00219 | 2025-05-06 04:49:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60e01b40-bcac-3250-ba62-449e6921448f | -21.72582 | -56.11243 | 2025-05-06 04:49:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fb3cd67-c998-30c1-bdfa-374afec83928 | -20.76419 | -46.76873 | 2025-05-06 04:49:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 92dbb9b9-4205-3fd3-a805-07b469011b81 | -21.24562 | -48.61621 | 2025-05-06 04:49:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fae7da72-153c-32a6-a4b9-647187b20747 | -21.72647 | -56.10858 | 2025-05-06 04:49:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1131b7f7-f078-35cf-be7d-a07f5dab66ea | -21.02967 | -55.64652 | 2025-05-06 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4cfb41e-96f2-3e22-b795-99b89dea0fe3 | -21.36858 | -48.62831 | 2025-05-06 04:49:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c44be02e-bf40-3cc4-9547-50e4326293ca | -21.82515 | -53.61659 | 2025-05-06 04:49:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7b51836-e4a6-3e32-9c89-01554cd3291c | -23.60034 | -49.01443 | 2025-05-06 04:49:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| dede7bc5-3b60-39a9-8c98-ee67463d69bf | -23.6025 | -49.00129 | 2025-05-06 04:49:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e768751-ab9b-3665-bd95-272b287a3846 | -23.59665 | -49.00972 | 2025-05-06 04:49:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3e365f53-1504-32e5-8320-4d979dbb9162 | -28.63457 | -55.9922 | 2025-05-06 04:51:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 960be69a-203a-3feb-83c0-81f1ca3fac40 | -29.77892 | -51.17715 | 2025-05-06 04:51:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 5033034c-9525-3a6f-aa95-d2b0d3db5489 | -29.39595 | -51.65131 | 2025-05-06 04:51:00 | NOAA-20 | BOA VISTA DO SUL | RIO GRANDE DO SUL | Brasil | 4302253 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aef9b9a7-515a-38ea-94f6-eaf79a4b3313 | -28.97582 | -52.24681 | 2025-05-06 04:51:00 | NOAA-20 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6d29936b-1bbf-33b1-ac62-8d3e9538f911 | 0.59759 | -60.46558 | 2025-05-06 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f30746e-491d-3107-9408-24eed61c82a8 | 0.59816 | -60.4692 | 2025-05-06 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03e5000d-8366-333a-b742-2cc1298a2fd9 | -11.39665 | -52.94687 | 2025-05-06 05:36:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22b762f3-1b97-3171-9e3b-66b025befd46 | -11.39604 | -52.95195 | 2025-05-06 05:36:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3313c50-ddd9-318e-b3ba-a74f5030a72e | -9.92635 | -59.92879 | 2025-05-06 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7f8069c-7240-3866-990c-d8dc7f7687ac | 0.5984 | -60.4682 | 2025-05-06 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db253c0b-b3c0-3822-a96e-68bcdab628b2 | -13.046 | -53.72469 | 2025-05-06 06:10:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 63556daa-df9b-3c34-93f2-f2cfc3864a21 | -5.16641 | -45.10336 | 2025-05-06 06:10:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 115a0e91-ebfb-3836-808e-4447eeb10b89 | -11.3965 | -52.94949 | 2025-05-06 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5d19613e-086e-341b-acf9-a7c9b9d2dc4a | -23.59323 | -49.00368 | 2025-05-06 06:14:00 | AQUA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 74ab6373-57ae-3dd9-a446-995c644d5029 | -6.5631 | -51.1126 | 2025-05-06 07:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 7b97c839-e4b9-3067-8015-81fd36e378ab | -6.8485 | -42.7979 | 2025-05-06 12:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| fbfecb25-5b3d-39c5-ad2e-c855e6c91511 | -6.8485 | -42.7979 | 2025-05-06 12:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| e81d4048-f0bd-33e5-849f-187d473df428 | -6.8485 | -42.7979 | 2025-05-06 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| dd872bb8-7fe3-37cf-b8a2-b9cd204cb988 | -6.6023 | -44.7684 | 2025-05-06 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 43284482-a79a-33ca-8a68-27b21991cce2 | -6.8485 | -42.7979 | 2025-05-06 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.2 |
| 2f2338f7-7174-3801-99f4-a0446979091b | -9.193 | -45.3342 | 2025-05-06 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 7cb13de3-b2d8-3a93-8714-2e34cdf8ceeb | -6.6211 | -44.7668 | 2025-05-06 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ad2e06c7-3815-3519-9216-352e0dbf1b99 | -12.8355 | -47.4117 | 2025-05-06 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 1e78aafa-462f-327c-804a-301c6b758ee1 | -6.6023 | -44.7684 | 2025-05-06 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 138.9 |
| b67adfd3-70b5-35cf-b7ec-73dbac39dd90 | -12.8355 | -47.4117 | 2025-05-06 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| a8103177-2e03-3da8-836f-faf1def147d9 | -6.6211 | -44.7668 | 2025-05-06 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 0d3c2d90-4855-3c47-807b-79542aad0aaa | -6.8485 | -42.7979 | 2025-05-06 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 151.3 |
| 1fdf7f90-564a-3079-a716-20b8f4050b50 | -6.8485 | -42.7979 | 2025-05-06 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.1 |
| fcec177e-d6a2-34d7-99aa-6310f45fa35e | -9.193 | -45.3342 | 2025-05-06 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 067170be-d8ef-3468-bc5a-99e157de851f | -6.6211 | -44.7668 | 2025-05-06 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 9dd43c23-ece2-3141-ad8f-e2f24fe1dc07 | -6.6208 | -44.7896 | 2025-05-06 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 523bc975-7a11-39df-910f-a4cdbbd83137 | -12.8355 | -47.4117 | 2025-05-06 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 13b407c4-dcda-324a-be0b-52304534bf66 | -6.6023 | -44.7684 | 2025-05-06 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| b43fba58-931a-36a1-9db6-c4bd2d4e93ed | -9.193 | -45.3342 | 2025-05-06 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 9350356c-d0e3-3cf9-814d-7aa3d5104362 | -12.8355 | -47.4117 | 2025-05-06 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 63227428-4869-34aa-a02d-9f6db35cd42b | -6.6023 | -44.7684 | 2025-05-06 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| cca28d73-d368-3631-839e-addd7d2640f9 | -6.6211 | -44.7668 | 2025-05-06 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| ab67e98b-e6b0-3ef6-b954-cd81008edc39 | -6.8485 | -42.7979 | 2025-05-06 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 171.0 |
| b3fa2cd9-2290-3df6-a18c-dfc6044f50dd | -6.6211 | -44.7668 | 2025-05-06 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 49db6667-e448-34ec-9c69-0b0337f8cf1f | -6.6023 | -44.7684 | 2025-05-06 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 5e5cc377-91c9-331a-9190-60062f11cf0c | -12.8355 | -47.4117 | 2025-05-06 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| feb76133-1104-352e-9552-b3c356bcf956 | -6.6208 | -44.7896 | 2025-05-06 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 1ac8798f-9422-3334-b7d3-ebe3ec47ad1f | -9.193 | -45.3342 | 2025-05-06 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 35000655-a542-3621-a368-80ea7d6841c1 | -6.8485 | -42.7979 | 2025-05-06 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.2 |
| 53de2aa3-8bf3-33de-ac91-27d8e410c5a5 | -6.8485 | -42.7979 | 2025-05-06 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 148.5 |
| b3fb8250-6dc3-3a59-ad66-c1c3a63a79c6 | -6.6023 | -44.7684 | 2025-05-06 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 33c007e4-bd17-3f21-a3a8-cf89421af4df | -6.6211 | -44.7668 | 2025-05-06 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 588494ca-d17f-3f64-adb0-474e5d6057af | -12.8355 | -47.4117 | 2025-05-06 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| b92ce2f8-dec2-3ae2-ab4a-6378e4c45b2d | -9.193 | -45.3342 | 2025-05-06 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 928da399-1b7d-3223-aae8-1b050fd86136 | -18.4279 | -54.7129 | 2025-05-06 13:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 89.8 |


[Clique aqui para ver as próximas entradas](README9.md)
