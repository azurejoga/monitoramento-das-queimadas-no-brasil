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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20c1fdbd-7a7d-3d9f-b89a-38321c852bc8 | -10.33235 | -37.13935 | 2026-04-05 02:53:00 | NOAA-21 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 427833c0-20d4-3203-81cb-84d8f704a298 | -10.33092 | -37.14623 | 2026-04-05 02:53:00 | NOAA-21 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5ff1e683-ce14-3b28-bb9f-8fa68c6c811b | -12.48362 | -43.64745 | 2026-04-05 03:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| daa30346-a2a9-3a7b-8e91-decabe77dceb | -12.48313 | -43.6484 | 2026-04-05 03:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1b24f0c-d58b-3d1e-a22c-53a3826bdf4d | -12.48444 | -43.64213 | 2026-04-05 03:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10dcb81c-776d-34d1-b54d-91c2a6bd361a | -10.33282 | -37.14504 | 2026-04-05 03:25:00 | NPP-375D | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 97f91e48-e091-3402-8779-07514ec05761 | -10.33358 | -37.1467 | 2026-04-05 03:25:00 | NPP-375D | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3a23ddc2-f6eb-346f-a0be-f7961bb5a723 | -10.33371 | -37.13998 | 2026-04-05 03:25:00 | NPP-375D | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3ed49d87-aa9b-3ed1-adf1-e2eba5b550b1 | -10.33451 | -37.14163 | 2026-04-05 03:25:00 | NPP-375D | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5e824bc0-e8df-3c0c-ad44-89094c4d401c | -12.4899 | -43.64997 | 2026-04-05 03:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 907aad79-a4fb-35ae-bf3f-b1f7518c480d | -9.72443 | -37.19929 | 2026-04-05 03:25:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f70b01a2-a9be-3a6e-94b6-dab975a6e4ae | -5.72901 | -35.54522 | 2026-04-05 03:45:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77bd4e3a-8b81-34b0-8f8c-731aa9e77957 | -5.71414 | -35.63871 | 2026-04-05 03:45:00 | NOAA-20 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1b4c3040-5190-38ae-9371-7d6e0f78f5a0 | -8.79565 | -36.36796 | 2026-04-05 03:45:00 | NOAA-20 | SÃO JOÃO | PERNAMBUCO | Brasil | 2613206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0c3c3205-89aa-3bd9-a825-9609649f8469 | -8.84448 | -36.55199 | 2026-04-05 03:45:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5de6d9d-e154-3a2e-9cc3-8d8dfadf028f | -12.05123 | -45.21596 | 2026-04-05 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed03a799-0e61-3290-a38b-781cbf7179b8 | -12.04165 | -45.2219 | 2026-04-05 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 797a04fa-93fd-3267-bc7c-234e7aa7af8a | -12.04557 | -45.21799 | 2026-04-05 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5894778-186c-3778-8759-54f47af77cd3 | -12.05064 | -45.21901 | 2026-04-05 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4510b4dc-2839-3f43-821a-eb010f471d06 | -9.60348 | -36.90356 | 2026-04-05 03:47:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a9d6839-9980-3ebc-99b0-1bbb056bcf97 | -12.03658 | -45.22088 | 2026-04-05 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03bf57a6-16b9-3d0b-a960-06d1e57bb299 | -10.33355 | -37.13937 | 2026-04-05 03:47:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9baafb63-1095-3a76-bc2c-1a361d3b4f65 | -12.20996 | -38.98001 | 2026-04-05 03:47:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c0f86706-ccc3-3c53-8a4f-e55161f38283 | -12.0473 | -45.21987 | 2026-04-05 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08ddb818-5c2a-36a5-a345-eef4a76666cd | -19.60219 | -40.07481 | 2026-04-05 03:47:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be15ccc3-34fc-3c85-b659-f35c8f9ac3c5 | -12.04787 | -45.21682 | 2026-04-05 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed3b81a1-44f2-35d5-ac0b-01043385ec08 | -12.04498 | -45.22103 | 2026-04-05 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab474930-3d26-3a93-bbfa-fec42b70e205 | -12.03093 | -45.22291 | 2026-04-05 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc628edb-07e0-394e-a742-d234d810b82b | -10.33297 | -37.14293 | 2026-04-05 03:47:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| afdcdf75-6245-36c3-8af9-ab9ecf747ad1 | -12.04222 | -45.21885 | 2026-04-05 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c986776-e80f-356b-946d-8a656d03d3ea | -16.58583 | -43.38531 | 2026-04-05 03:49:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb8fc3e9-57d5-3edb-bde3-ed2bc742f261 | -12.03928 | -45.2193 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7e102c4-ab7e-318a-9cfe-31fd4cb7de35 | -12.03489 | -45.2233 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02cc9226-7027-34cd-8dc8-38ab58cc262d | -12.0305 | -45.2273 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5787d06d-69b4-3d1a-a24d-d4e1d0d2e1e3 | -12.02741 | -45.22218 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f9cdf19-a3d0-379c-8ac2-a2abe25ccb3c | -12.0474 | -45.21585 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e17ead04-c5be-317b-b351-8a62edfaabc1 | -12.03862 | -45.22386 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3badf223-88ae-3916-843b-b854bb61325d | -12.03115 | -45.22274 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f68d5dc-77a0-3462-8192-9a4f887d9b94 | -12.05114 | -45.21642 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59f364c6-58dc-3870-980c-892e825acd41 | -12.03554 | -45.21874 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb1d0046-8465-31af-a07d-7effa6239048 | -12.04675 | -45.22042 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12b320df-a761-3ffd-9482-282f7f852a2e | -11.91887 | -47.53213 | 2026-04-05 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 2f2f8168-41c8-3a78-a2e6-e3f52654e00e | -12.05049 | -45.22098 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2afbdb2a-36ae-3fe9-9c38-0e6ee0890cf5 | -12.04301 | -45.21986 | 2026-04-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5793d093-56fb-3422-adb6-a1da80f429cd | -15.28656 | -43.07014 | 2026-04-05 04:36:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ca4497cb-7f53-3327-adc7-24c13b0cea61 | -15.28381 | -43.0727 | 2026-04-05 04:36:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 88eb38ba-9252-32f0-bbc8-d065207ed0ea | -16.58626 | -43.38533 | 2026-04-05 04:36:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dff7b70b-db5b-3ce5-8e58-5fc465828fa7 | -17.1362 | -47.32484 | 2026-04-05 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 534ebcd8-09a6-3329-a224-7cdfce01bb10 | -15.28207 | -43.06956 | 2026-04-05 04:36:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 768c035b-8de2-3c16-8461-06da3c14d829 | -15.2844 | -43.06814 | 2026-04-05 04:36:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4a1a496a-8160-37b3-bc28-0bbc9c8fd0f3 | -16.58684 | -43.3807 | 2026-04-05 04:36:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7580ba57-ab29-31f9-b3ef-232decead032 | -15.28263 | -43.06498 | 2026-04-05 04:36:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 108a94cc-54ef-3e2d-98f7-fca2f39b46d9 | -17.13679 | -47.32064 | 2026-04-05 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 247143b3-9c38-377a-a08b-36641092a398 | -20.99396 | -56.09762 | 2026-04-05 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e13ec479-8417-346f-8cae-738783cd4d63 | -25.04624 | -53.6307 | 2026-04-05 04:38:00 | NOAA-21 | SANTA TEREZA DO OESTE | PARANÁ | Brasil | 4124020 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1b51bc26-d333-39f1-8d65-7c927f9e712f | -22.74282 | -51.38749 | 2026-04-05 04:38:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5fbe7546-2052-3fea-a2c9-b17fb6999552 | -21.21165 | -55.64778 | 2026-04-05 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aae65991-509e-3ceb-9ce6-b7f03412eb1e | -18.80046 | -48.54591 | 2026-04-05 04:38:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cca5caa-5750-3596-a929-34d7dc4133d0 | -19.40301 | -49.54363 | 2026-04-05 04:38:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed03e70f-c070-34fa-bd23-2ca49e8d653f | -21.04659 | -54.30825 | 2026-04-05 04:38:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a819408d-8282-33ec-9332-edc12b049e14 | -22.7434 | -51.38375 | 2026-04-05 04:38:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| eeed43ba-a32b-398e-b969-887045a89581 | -26.05668 | -53.58139 | 2026-04-05 04:40:00 | NOAA-21 | SANTO ANTÔNIO DO SUDOESTE | PARANÁ | Brasil | 4124400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a9efd077-b11a-38fe-88cd-a2d28a48e4bc | -12.02633 | -45.22693 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63e80ae3-7dd6-3196-807a-b3a59d6fd596 | -12.05078 | -45.21781 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d48804d-a00a-3d70-90fb-b90bf9bb69b0 | -12.02613 | -45.22636 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce57a297-a9a5-3019-9b3c-4ee3feb52a33 | -12.03879 | -45.22035 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b8ce21f-33a8-3655-a5f2-5eeface9f6d0 | -12.03238 | -45.22307 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0edcef74-2115-3ace-ac14-e5aa177163cb | -12.02714 | -45.2183 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d6d6f58-7d1b-3b86-9c6c-ee784b3cb145 | -12.05127 | -45.21376 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50476d20-a65c-3150-a2d2-c481ad2d39b1 | -12.03928 | -45.21631 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5702850-e701-3afc-9c6b-832cfc19540e | -12.03304 | -45.2196 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f99af646-fd31-3e63-a20b-d37f21a64cbe | -12.04503 | -45.21706 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82e81011-fb89-3521-9fe3-1487b4e92c27 | -12.02106 | -45.22211 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06c76530-0125-3ea7-a671-da423e3405fa | -12.03289 | -45.21904 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b770146-adc1-39b3-9828-53fc8d23da10 | -12.02089 | -45.22158 | 2026-04-05 05:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 636792e0-2ade-36f8-979b-4a0bc9956689 | -15.28744 | -43.06397 | 2026-04-05 05:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8012378d-379f-3d50-a3f3-303ca378605b | -15.27997 | -43.0696 | 2026-04-05 05:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a20f54ba-bf6d-3774-96a6-33a20f513e9f | -15.28061 | -43.06335 | 2026-04-05 05:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4f212e0d-35ef-3979-a013-e7d73c68a0de | -17.13579 | -47.32601 | 2026-04-05 05:08:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db8d32ea-ca45-3625-8047-310934919ef0 | -15.28196 | -43.06316 | 2026-04-05 05:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d5270cf1-26f1-3dfc-9e98-876748b92e68 | -15.28137 | -43.06943 | 2026-04-05 05:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.7 |
| de89714c-7d29-3053-9931-9f474ee00e2e | -20.09514 | -57.22206 | 2026-04-05 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2d22dda-cafc-397c-b7d0-44cb90e588a4 | -15.28681 | -43.07018 | 2026-04-05 05:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 90897bd5-986c-33bf-a052-6965f967c153 | -17.13618 | -47.32251 | 2026-04-05 05:08:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5998ea3-97d7-3b94-8bff-070a8f2fe8e6 | -21.04652 | -54.30833 | 2026-04-05 05:10:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ef70a3b-c5b9-38f0-8bc9-6d6a23e7986a | -21.67721 | -51.38195 | 2026-04-05 05:10:00 | NPP-375D | FLORA RICA | SÃO PAULO | Brasil | 3515806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 488478de-91fd-3f3d-8899-9282f8baaf04 | -21.20897 | -55.64669 | 2026-04-05 05:10:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80f2bbe5-93f6-32bd-bc63-1d56e1c44e37 | -12.36743 | -64.00671 | 2026-04-05 05:27:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f7ec12a-d748-3e09-97da-f65b1836e10e | -12.48858 | -43.64379 | 2026-04-05 06:20:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6ad73d57-be8d-3d22-98ef-5f95728e7e5b | -15.28817 | -43.06297 | 2026-04-05 06:20:00 | AQUA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 331c9633-aa09-306f-9ef2-1beff2da2b02 | -6.768 | -45.50059 | 2026-04-05 12:23:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b9ebaf63-e447-32af-8d5f-d41aa4bb1c86 | -6.74935 | -47.82549 | 2026-04-05 12:23:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 638fec33-0d0e-30c8-b053-268d79a0d097 | -20.86442 | -54.3138 | 2026-04-05 12:29:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 88d7288b-2959-3a12-bd99-e7eddc5d4087 | -21.10816 | -55.22809 | 2026-04-05 12:29:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8a5b8dc8-a7d8-37d7-86c7-ad03617d8e66 | -20.99581 | -56.09127 | 2026-04-05 12:29:00 | TERRA_M-T | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f0276e8a-43fb-3e1e-9dcc-54fddac4fd0a | -20.99447 | -56.10067 | 2026-04-05 12:29:00 | TERRA_M-T | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |


