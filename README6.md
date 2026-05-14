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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d31daa0-0555-3794-9f42-5415f0e6a346 | -16.26648 | -60.00629 | 2026-05-14 04:55:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c08ece2b-1d48-3a7e-af05-b47726dd8cec | -16.47566 | -55.07397 | 2026-05-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 985e3253-a9a7-3009-9ef3-452a063979a3 | -9.7616 | -55.62174 | 2026-05-14 04:55:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dbb7228-386b-3e22-8074-aed036827109 | -11.74517 | -54.2343 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b53a46e5-0909-39a3-ac48-79679102f40d | -11.7649 | -47.06418 | 2026-05-14 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0b8d5e2b-f5ef-3ecc-ab37-40a3ffab0310 | -11.73352 | -54.24324 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75c49903-16cc-32b0-8d8b-867abca306ff | -10.6662 | -49.71042 | 2026-05-14 04:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 822f56ec-2921-38be-ae10-4b9b07ad7c26 | -16.47623 | -55.07039 | 2026-05-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6d3c3417-3f32-3ccf-961c-4f45710f9ac6 | -11.78939 | -54.0211 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b72ac33-a9a5-316a-b6b0-083cfb003e88 | -12.62205 | -44.51557 | 2026-05-14 04:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7ba129b-3c4f-3f87-8655-4bea7d8d318e | -11.75022 | -54.79375 | 2026-05-14 04:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f68508c0-8387-38b6-b0ad-62012a2cfd13 | -11.62843 | -54.1573 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e40da663-1d5e-384e-a538-50e10280f909 | -11.97985 | -46.7923 | 2026-05-14 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06b710de-c015-3488-8a5f-11005046feb9 | -10.48477 | -49.36018 | 2026-05-14 04:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fced6691-e5d8-3a10-bb73-bbbe55ff9ef6 | -11.18269 | -55.92501 | 2026-05-14 04:55:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d46a94ca-fdc6-3805-9c60-78d0746788e7 | -11.93373 | -54.09552 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 264dae2b-ca0a-3348-808d-3bea15cab549 | -11.97241 | -43.84088 | 2026-05-14 04:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d58616a5-6c1e-39af-85c1-02d5356c0e80 | -11.93317 | -54.09904 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a69f888-54ac-380e-b1e5-e2a6c479702d | -12.61664 | -44.51492 | 2026-05-14 04:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8e67382-65a8-3376-8211-5999c3b10251 | -10.48562 | -49.35804 | 2026-05-14 04:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dc4efbd-6e13-35d5-b8d1-3302707fa959 | -23.39223 | -51.1285 | 2026-05-14 04:57:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f6ce9822-7285-3e79-b90d-0bf3ada2c20d | -23.39262 | -51.12774 | 2026-05-14 04:57:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 393b83db-e25a-31e2-af9c-60af38445a9d | -19.19693 | -49.12797 | 2026-05-14 04:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7974b504-1ae0-3b53-8cb8-91a77bd6e81e | -19.19259 | -49.12741 | 2026-05-14 04:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 059882a5-a3ca-376d-ac41-6cec4d6fc1ea | -18.25211 | -54.61559 | 2026-05-14 04:57:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4890e034-1a9a-32a5-a369-5e692f218020 | -11.17753 | -55.92309 | 2026-05-14 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fd15a89-ab8e-3104-bf12-45829560e42f | -12.45754 | -54.45123 | 2026-05-14 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1fa2e7f-504e-37c4-b891-27f65f75aa1a | -11.18278 | -55.92805 | 2026-05-14 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b83d0d20-be50-32e1-be9f-b08b97790725 | -12.46394 | -54.45205 | 2026-05-14 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b95e2edb-286c-38b3-9a7e-e06b47d4ea48 | -11.18327 | -55.92393 | 2026-05-14 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6fa1cf91-ca26-3cc5-8fc4-c9e1b7794a2b | -19.44008 | -56.56431 | 2026-05-14 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1d5db797-1c55-3c82-9747-3e494dcdca76 | -19.43963 | -56.56915 | 2026-05-14 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c4976b0a-f0ea-35eb-877a-03dc5334189b | -17.04962 | -58.24922 | 2026-05-14 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fa11d618-5ed0-35f1-adbe-cc07519bfffc | -11.76079 | -47.06294 | 2026-05-14 06:31:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 40b647bb-80e2-3efb-8b6e-4710ba801c07 | -10.66446 | -49.71051 | 2026-05-14 06:31:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83e71e77-74a6-328e-b157-acce1fbf3bca | -6.5631 | -51.1126 | 2026-05-14 08:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 7818d93a-cd57-39be-8011-f3b727221d42 | -11.3258 | -39.8253 | 2026-05-14 11:38:00 | TERRA_M-M | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 8e0d5e84-a548-3d34-affa-f29a3c000dc6 | -7.49151 | -44.05814 | 2026-05-14 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d932adce-9c7f-3ff1-b3ff-d85823abba98 | -11.77707 | -43.64938 | 2026-05-14 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 55cc9965-bb4d-3ff2-ac9d-e692b175ff9e | -8.94891 | -45.68159 | 2026-05-14 11:38:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6b23d739-c172-3ebf-8ac7-596e4f282225 | -11.93436 | -43.3853 | 2026-05-14 11:38:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ad46c129-f8fe-3f11-ac0d-788877db5b63 | -8.54584 | -45.97737 | 2026-05-14 11:38:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d8182cbc-ba67-301a-8d54-e808233f772f | -10.64642 | -42.32275 | 2026-05-14 11:38:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 169.1 |
| 1670f364-e957-392e-9aab-f8612b520077 | -8.94725 | -45.69267 | 2026-05-14 11:38:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 821ea2fb-b283-36b6-814f-2deefb32bc33 | -11.32736 | -39.81332 | 2026-05-14 11:38:00 | TERRA_M-M | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ca01382f-4bbb-32c7-8af4-9cfa886ea6d2 | -10.63751 | -42.32151 | 2026-05-14 11:38:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fb810a70-d587-3334-abc0-010c1a274352 | -10.50094 | -46.53352 | 2026-05-14 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8a0b5dde-3af8-320b-b5cb-281a72aec2db | -10.64769 | -42.31368 | 2026-05-14 11:38:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 56.7 |
| 520a3790-f20a-3fad-8273-43a50e6d7186 | -11.93565 | -43.37634 | 2026-05-14 11:38:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 22411244-bfd1-3023-ab7a-28bcb79c6afc | -12.17109 | -45.72738 | 2026-05-14 11:38:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1dd7563a-2c0f-31f0-b35c-a0c5bcd7470b | -11.79992 | -43.61606 | 2026-05-14 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b64c2a7-f9bf-3663-b59a-29a18fc84752 | -11.97055 | -43.83692 | 2026-05-14 11:38:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 21520241-649e-3f4c-856b-24c58657f2ac | -10.64898 | -42.3046 | 2026-05-14 11:38:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 19633220-c58e-3578-911b-f9dada38fa53 | -11.9305 | -43.3812 | 2026-05-14 11:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 949713b2-154e-33c1-a1bf-03098fd69324 | -13.9607 | -46.03578 | 2026-05-14 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| debfc9b2-5a7d-3043-abbd-9f7972f3f6ac | -15.63285 | -43.2951 | 2026-05-14 11:40:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6d4717b1-fa21-3228-a069-37e674992042 | -17.59044 | -43.45007 | 2026-05-14 11:40:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| af55436c-fd34-334a-864e-626bd24cbd4f | -13.95134 | -46.03439 | 2026-05-14 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 497efce1-443a-311b-a8f6-20c4b1ad8be4 | -13.9529 | -46.02415 | 2026-05-14 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3abe3b8d-9f70-3374-afc8-d4bd99deb87e | -15.85227 | -46.5316 | 2026-05-14 11:40:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a300ed06-45e3-3e4e-9df0-d815fa796686 | -15.85069 | -46.54205 | 2026-05-14 11:40:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97d26c63-6466-3686-b731-e1811dc91365 | -13.96226 | -46.02554 | 2026-05-14 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 4eb904d4-bd47-333d-917f-016f8386086f | -22.91899 | -48.68206 | 2026-05-14 11:42:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4db5b7f5-4c55-386a-b383-39ca64f5210e | -11.9305 | -43.3812 | 2026-05-14 11:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 180.3 |
| dacf7f53-13d6-36e3-9edb-2521125de40b | -11.9305 | -43.3812 | 2026-05-14 12:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 1d46d813-6fe6-3360-8dc9-f3cd5c46bf0a | -11.9305 | -43.3812 | 2026-05-14 12:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 9f3334e2-2068-33c4-8c44-7a6d4e0c5f58 | -11.9305 | -43.3812 | 2026-05-14 12:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| b4c79683-8ecb-30c8-a267-354e8a2419f2 | -11.9305 | -43.3812 | 2026-05-14 12:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 3b467019-77bd-374b-84f0-25a8b5e92bb2 | -11.9305 | -43.3812 | 2026-05-14 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 2b5624ee-1248-3d21-8ec4-df63a7b08112 | -11.9305 | -43.3812 | 2026-05-14 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 634d944c-220f-35f1-bd9e-09fea43084ed | -10.6467 | -42.3141 | 2026-05-14 13:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 622.8 |
| b70d51f7-8334-3888-b06d-756cc3bc2867 | -11.9305 | -43.3812 | 2026-05-14 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| dc310bca-6439-304a-ab8c-eb7b55d63fc2 | -10.6467 | -42.3141 | 2026-05-14 13:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 669.4 |
| d9546c04-f2a3-3182-8cec-9730c61983ee | -11.9305 | -43.3812 | 2026-05-14 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| fbae7593-dae3-3bb3-b6da-cc863fd2a7bc | -10.6467 | -42.3141 | 2026-05-14 13:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 571.2 |
| 019df436-7638-3e19-81cb-0b551d61dca7 | -11.9498 | -43.3781 | 2026-05-14 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 7b5d4d8e-0aec-3685-a3da-d589c57f8100 | -11.9305 | -43.3812 | 2026-05-14 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| eddae459-20ac-32dc-a9d6-bf1665eddf2d | -11.9305 | -43.3812 | 2026-05-14 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9fcbd7a0-e794-3f07-bd67-d6fab31d5782 | -10.6467 | -42.3141 | 2026-05-14 13:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 675.0 |
| f15fd904-814e-3c63-b87d-96847c81ed94 | -11.9305 | -43.3812 | 2026-05-14 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 9687d148-9b19-3e1d-90f2-d97e40fb616c | -10.1213 | -47.9374 | 2026-05-14 13:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| b4fbc86d-13c7-3b25-b615-025625be7906 | -11.9305 | -43.3812 | 2026-05-14 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 810c0b48-6df6-3953-8883-367dd5494cbc | -11.9305 | -43.3812 | 2026-05-14 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| d114be88-ff14-3463-afae-72bc2e3bed17 | -12.4875 | -45.4434 | 2026-05-14 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 3c6d9bf7-7434-35e4-ace7-8d046330fa42 | -11.9305 | -43.3812 | 2026-05-14 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 0d6284d0-003d-3b8b-a0b2-58d9ee382fc6 | -12.4875 | -45.4434 | 2026-05-14 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| f05039e2-6663-3e0f-8115-a9f80a4bcaa9 | -11.772 | -43.643 | 2026-05-14 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 19659c39-af52-3c0c-a30b-98e5af0967ed | -12.4875 | -45.4434 | 2026-05-14 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| b23bec3c-1c18-31a5-bae6-8049e44a5829 | -11.772 | -43.643 | 2026-05-14 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 2fb90b94-8b4d-3f9a-a7a8-e8f51ad524fb | -12.4875 | -45.4434 | 2026-05-14 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e8cf5cf2-04b9-3aed-b5e9-0ecb37328439 | -11.772 | -43.643 | 2026-05-14 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| a83542c8-3a4f-36f0-b501-5e0d4dc1f363 | -11.9305 | -43.3812 | 2026-05-14 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 6a155bb4-29d8-3d1b-be34-3258d15e473c | -11.772 | -43.643 | 2026-05-14 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| ac48c919-a0bc-3d07-97a6-cdaf6870bb09 | -11.892 | -43.3874 | 2026-05-14 15:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 2e379279-57cd-34b0-8035-eb3bf478a56b | -11.772 | -43.643 | 2026-05-14 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 22261e62-fbdb-3d9a-b833-876a5eb9bb2c | -11.772 | -43.643 | 2026-05-14 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 04708882-6ded-32aa-870e-e13436bed18a | -11.772 | -43.643 | 2026-05-14 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |


