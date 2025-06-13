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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c75a3ba0-e132-3975-b5d3-d95a40141675 | -11.171 | -46.871201 | 2025-06-13 00:24:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2626e10a-b878-3bd6-9df1-c8d45eed104d | -9.5127 | -40.312698 | 2025-06-13 00:24:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 13773da9-39d8-399e-a604-eefc36f8a83c | -7.2443 | -43.105598 | 2025-06-13 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5486793-1032-37ef-8508-6424714f14b3 | -9.7923 | -36.999001 | 2025-06-13 00:24:00 | METOP-C | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| dd2ff63d-a287-36de-9932-de4f6d46fae7 | -9.8052 | -37.009399 | 2025-06-13 00:24:00 | METOP-C | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| b7b06931-1e5e-3f13-aeca-f203d3e7a6ba | -7.2427 | -43.098701 | 2025-06-13 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 12daea69-3821-3792-ba59-8e3cc5567a64 | -10.6492 | -44.485401 | 2025-06-13 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b4cdb04-819e-38c0-a791-22c4afe078b9 | -9.6639 | -48.773102 | 2025-06-13 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f343881a-5c32-3f5c-b106-1770c99bca14 | -9.847 | -44.717701 | 2025-06-13 00:24:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5cafb6a5-5c96-39bd-b956-843364cfe853 | -6.582 | -45.625401 | 2025-06-13 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d99ad670-bccd-3384-9948-3660cc5c83e3 | -10.6944 | -49.503201 | 2025-06-13 00:24:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9eff2177-1b11-30a2-a66a-6ea15c526cce | -7.2263 | -43.1171 | 2025-06-13 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b46decd-6838-3020-8e61-f2b233f732fe | -13.8929 | -54.628101 | 2025-06-13 00:24:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d090955-a81e-345d-a6c4-b460e6a28056 | -8.8155 | -46.696602 | 2025-06-13 00:24:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3766045a-e176-33db-b102-5002cc50f1a3 | -10.659 | -44.4832 | 2025-06-13 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d7e09aa9-3d8d-3eaf-ad76-4097a99f5133 | -13.8833 | -54.629902 | 2025-06-13 00:24:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f1735ed-1220-3faa-80ae-95e5f2379777 | -13.8775 | -54.597698 | 2025-06-13 00:24:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99eee130-b048-3190-8bad-b0188626efb0 | -7.2165 | -43.119301 | 2025-06-13 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 01457750-49c8-3f06-b550-6d965f272d2b | -10.6917 | -49.490299 | 2025-06-13 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22269cb4-3ee2-355e-a2f5-c0a56fb7a727 | -9.8946 | -46.280899 | 2025-06-13 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45e0b92b-0a9f-3368-b096-5b10616cef1c | -9.8454 | -44.710499 | 2025-06-13 00:24:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2be8f945-f5b7-3a74-8e96-26d93204ce2e | -9.8021 | -36.996601 | 2025-06-13 00:24:00 | METOP-C | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| e90c7d76-a84b-3b39-bdfe-1178f674e041 | -9.6737 | -48.771 | 2025-06-13 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b7b152b-921a-3255-b03a-11abea06d1dd | -10.6606 | -44.490398 | 2025-06-13 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e2ec1432-2a72-3f3d-a2cf-2f80226bf0c7 | -13.0894 | -52.277802 | 2025-06-13 00:24:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67f7e2c5-6739-309a-8ada-798c7d1eb568 | -7.6667 | -43.642502 | 2025-06-13 00:24:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cbd2d505-490a-3978-a2ba-4c9c85f9c0fb | -7.6683 | -43.6493 | 2025-06-13 00:24:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 873053cf-c168-34ac-9884-780d4f9dfb79 | -6.5804 | -45.618198 | 2025-06-13 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e73418a-7a5a-367c-ba41-a44e49c60a55 | -5.6476 | -43.606998 | 2025-06-13 00:24:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f24140d-70ca-3563-bf9c-0f27f080d850 | -9.3954 | -48.424702 | 2025-06-13 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 896d5484-bdf2-311e-8a09-ef17b30059d0 | -13.8871 | -54.596001 | 2025-06-13 00:24:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c32f3d35-1adb-378a-bbf8-80f3ac6fac29 | -13.0936 | -52.2995 | 2025-06-13 00:24:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0b0cd13-3a83-3667-8fbd-0799be24ebb1 | -7.2149 | -43.112301 | 2025-06-13 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ae5b86e8-637f-3fc2-82ca-634e400eb258 | -6.655 | -43.907501 | 2025-06-13 00:24:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb93e19a-af13-34e7-bd2f-18e590daf811 | -9.8883 | -47.812698 | 2025-06-13 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 466efa5b-8e32-301f-9575-222469b449d9 | -8.0731 | -43.121399 | 2025-06-13 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87f8539f-0392-37ac-ba59-77961daa61f2 | -11.1631 | -46.882301 | 2025-06-13 00:24:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9bb45745-a012-3a8f-a38b-14a1788ec46e | -11.5839 | -44.851398 | 2025-06-13 00:24:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1cf22262-f2c7-3b65-a356-c5341ab746a9 | -10.7014 | -49.4883 | 2025-06-13 00:24:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 064c7ebe-6933-3f21-b828-2b2f9d6fe1e8 | -7.2459 | -43.112598 | 2025-06-13 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1f4d5560-e6eb-3eac-b6c7-258060b91c70 | -10.6508 | -44.492599 | 2025-06-13 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa2884e6-d11e-3085-b6c7-3dcc549dd445 | -10.7041 | -49.501202 | 2025-06-13 00:24:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 491227de-9aab-3a76-9228-a94abcebef5d | -8.9524 | -47.2752 | 2025-06-13 00:24:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea4edcb-be20-3437-b203-5f2fba87bdea | -11.1186 | -53.939701 | 2025-06-13 00:24:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a44238cb-afb3-3682-8ba0-016d9b876001 | -6.4952 | -42.855301 | 2025-06-13 00:24:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f9d65520-f127-3d03-ade9-cf3117492810 | -9.7955 | -37.011902 | 2025-06-13 00:24:00 | METOP-C | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 7e50cb84-268b-3503-9ec7-ef005125283f | -10.6439 | -49.407398 | 2025-06-13 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3cb1c1c-0758-3603-a8d7-d75add31f936 | -9.6713 | -48.759899 | 2025-06-13 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03ffb628-2ac9-31df-818d-5f249c60e677 | -10.6466 | -49.419998 | 2025-06-13 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a89b8c08-0d2d-3def-a545-337d91ee9b3f | -23.3388 | -47.6408 | 2025-06-13 00:24:00 | METOP-C | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b6fde13-55c9-3726-82ce-ad86cce265a8 | -7.6981 | -45.7831 | 2025-06-13 00:24:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5abcec7-1379-340d-b96d-5fe448cf2da7 | -6.9493 | -42.900299 | 2025-06-13 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b3659ec-820e-36f5-b7cc-12e3d00c29b9 | -12.1016 | -48.871799 | 2025-06-13 00:24:00 | METOP-C | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2984f45-e848-3fed-a480-e02cf8e8b2b0 | -12.9938 | -40.9277 | 2025-06-13 00:24:00 | METOP-C | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f97abd50-3d6c-37b7-a5d8-8be0effe5459 | -12.2697 | -44.6049 | 2025-06-13 00:24:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75678f03-0c6b-3b8e-a16c-b38fed1be3fc | -11.5555 | -54.548302 | 2025-06-13 00:24:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75cdf4e3-713f-34e0-8e14-0b35b260a288 | -9.8928 | -46.2728 | 2025-06-13 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6362f231-b53a-3c79-ac75-7188d123c945 | -11.1237 | -53.966 | 2025-06-13 00:24:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e344de98-f5a5-3f18-8831-76be09ecaab7 | -10.6302 | -49.4288 | 2025-06-13 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 8e6631aa-5701-30c5-88fe-c371b4a89839 | -11.119 | -53.9446 | 2025-06-13 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ab61e3be-7fd0-3968-9edb-5700caaf3e7f | -9.3927 | -57.5541 | 2025-06-13 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 33575416-f23f-39f1-a93c-acbd6b18e6e6 | -11.1379 | -53.9429 | 2025-06-13 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 0dc617d2-03d1-3b9d-9524-534b31133cbe | -11.5649 | -54.559 | 2025-06-13 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 15f01f1c-0034-3a7f-9779-5534eb7b1b38 | -10.7051 | -49.4853 | 2025-06-13 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| aba4ddb8-a578-36ec-ab86-5b7ae0be37b7 | -9.4114 | -57.5529 | 2025-06-13 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| bb854209-a6e2-345c-93d4-302d626c8512 | -7.2403 | -43.1134 | 2025-06-13 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 52aa5398-b859-3623-8c5d-af759d1ec081 | -13.8867 | -54.6312 | 2025-06-13 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 6d2d292d-83d8-34a8-bfb8-5a26bc8c4018 | -10.6492 | -49.4267 | 2025-06-13 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| dda359be-9eb4-3cfe-ba05-15fff5aa570d | -10.9167 | -56.8336 | 2025-06-13 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7fbff5c5-a8ea-3708-befa-25f4021151fa | -10.9355 | -56.8322 | 2025-06-13 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3cc83fb1-dcac-308b-8e34-9641d8ea54fe | -10.6495 | -49.4051 | 2025-06-13 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 40e00400-e5cd-3495-83a4-08242bd72085 | -13.9059 | -54.6291 | 2025-06-13 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.1 |
| e5411004-1b68-3f7a-aed3-c57ab41dd0fa | -13.9062 | -54.6084 | 2025-06-13 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 8411dbd3-4d9c-3e5e-8004-6cddafe5445d | -10.7048 | -49.507 | 2025-06-13 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| cb7656b0-91d8-3179-9a0a-d202d5e033aa | -11.5647 | -54.5794 | 2025-06-13 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 2f2a4479-4e24-3845-9984-a3235585151f | -8.8165 | -46.682 | 2025-06-13 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ab7ed149-2270-324e-ac50-29e4f6724d36 | -7.2214 | -43.1153 | 2025-06-13 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| ef87f39f-c1e4-3fb0-aa52-3c56662a93ef | -13.9059 | -54.6291 | 2025-06-13 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 1ab97e83-ecbf-3d07-91d8-c17b1bd73369 | -7.2214 | -43.1153 | 2025-06-13 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| d03e8df4-a952-3ad2-aec2-2e1b03f7fd90 | -10.7051 | -49.4853 | 2025-06-13 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 790d1fee-8841-3c99-9c79-bdb3480fe764 | -10.7048 | -49.507 | 2025-06-13 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 44617d23-4b01-378e-922d-747968f8037e | -7.2403 | -43.1134 | 2025-06-13 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| b87b7ec0-8696-352f-a38f-1de3786cca23 | -11.5836 | -54.5777 | 2025-06-13 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 27152567-8f5c-3c44-9665-37a63b2550b6 | -13.8867 | -54.6312 | 2025-06-13 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 5f09f120-79d9-3446-b87b-ba0b90e5adc2 | -10.9355 | -56.8322 | 2025-06-13 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 1fee1caf-ebb5-3a56-a932-83c098fff566 | -9.4114 | -57.5529 | 2025-06-13 00:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 65c0501c-74b7-3df6-93ab-87fab96bf873 | -10.9167 | -56.8336 | 2025-06-13 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 2ed7ba20-d01b-3a3c-9d7d-a0fb3cf3702e | -11.5647 | -54.5794 | 2025-06-13 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| a985bef7-52b1-3d1a-bc61-40ae18eb421f | -7.4575 | -45.5116 | 2025-06-13 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| fed2f233-1a6c-3f02-9058-02ee7c327399 | -13.9062 | -54.6084 | 2025-06-13 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 6a226c98-c901-37d1-9018-b01fcdd43d41 | -11.5649 | -54.559 | 2025-06-13 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9594b3b8-e74a-376d-b82e-abdb2287b0a6 | -10.6492 | -49.4267 | 2025-06-13 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| bea4f3f6-32f1-3e57-b865-f34b5de12440 | -10.6302 | -49.4288 | 2025-06-13 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 00526ba7-be37-343d-8bcf-23c830c688f5 | -7.2214 | -43.1153 | 2025-06-13 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| ad8afd76-ff94-389d-9e77-b3fc1722f1cb | -13.9062 | -54.6084 | 2025-06-13 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 334a0740-ae86-3425-8db4-f23403c9e468 | -13.8867 | -54.6312 | 2025-06-13 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6aaa131a-f73d-36ba-84ea-b6847574b7b6 | -11.5649 | -54.559 | 2025-06-13 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b2b34562-4bc8-3368-bd44-54f2a6325b39 | -10.6302 | -49.4288 | 2025-06-13 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| b4accbb3-bf10-3b6f-bd61-3124b01a7d1b | -10.6492 | -49.4267 | 2025-06-13 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 6c482a8e-d729-3a4b-b288-517e0c15d5a4 | -10.6495 | -49.4051 | 2025-06-13 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |


[Clique aqui para ver as próximas entradas](README3.md)
