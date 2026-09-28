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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dd840de-b944-3334-93fa-8b42bfd18a0d | -13.39196 | -40.96736 | 2026-09-28 17:07:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| f1b20d52-a63b-314a-8d22-944aa5e84401 | -17.82878 | -44.39382 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| e2e51376-10be-3c09-810f-33b5dc3f8c65 | -13.45455 | -48.59321 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 417c3a88-42d2-3292-83d7-449f6eca53fe | -13.96958 | -40.46085 | 2026-09-28 17:07:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8dd747a7-67f0-372c-8bc7-cb60f9c1d772 | -15.1074 | -53.89841 | 2026-09-28 17:07:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 440c2c73-de5e-3444-a177-6bd9bc23e0b4 | -12.61489 | -47.32051 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a4229017-a36d-3bc0-960d-8fd71fea2af7 | -15.18097 | -46.1366 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1078d22d-47a9-3ddf-b8c7-4f169db4f5e7 | -13.10015 | -48.20363 | 2026-09-28 17:07:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| cb1ab728-7fe9-366e-b331-ace21de93e9a | -11.38981 | -43.44441 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 405aec0d-5c88-3e05-a4a2-ab8771642c6e | -12.69204 | -47.34961 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 91259a20-fe11-31e3-b2c4-1a5c63095ad3 | -12.68666 | -46.97532 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1b07122c-4e8a-3d53-b1ae-5d70d0d8a0be | -14.80988 | -41.73255 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 212.7 |
| 6aed87d4-1ab0-373d-ba32-142d3d641e56 | -14.44892 | -40.80332 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 7e595576-166b-3c60-a6d6-af7728e6cea9 | -17.89192 | -45.05677 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f6f27233-c63e-370b-b526-60d87e129382 | -13.76509 | -48.52449 | 2026-09-28 17:07:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 84e1d091-439a-3daf-b52d-d5630e4f56cb | -15.6685 | -41.63394 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 96b65e57-797e-3442-95c9-23e6324d78a9 | -17.58086 | -44.37871 | 2026-09-28 17:07:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| ef0108d5-c34d-38d7-9e62-27fcabe75fdf | -17.04002 | -56.57088 | 2026-09-28 17:07:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 19b292c5-0a30-3c61-b160-043291f40680 | -14.438 | -40.61818 | 2026-09-28 17:07:00 | NOAA-21 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b42d2832-dc1e-39a6-abc3-e7331fd4fad7 | -13.48067 | -48.59949 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bbd38b71-0a26-3549-b1e0-00f4b8e318fc | -13.07341 | -47.43039 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1c4c8cdc-23b7-34b4-95a0-18c76f693346 | -14.53709 | -48.31547 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b0651e4b-d700-3b86-9f70-ac55ed1303fb | -13.71658 | -48.82545 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1aa850f3-4d80-3c1b-ac84-8a7032ebcd5d | -13.87416 | -42.12982 | 2026-09-28 17:07:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4baedeaa-9752-3b13-9372-882461e1af72 | -15.16209 | -43.60761 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 56b6bc19-ceab-3e33-8d2d-a358c2e5a1ce | -13.47007 | -48.63469 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 93848917-e8b1-3d18-b1b1-158cc275efd2 | -13.71936 | -48.81779 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b7b018d3-16a7-394c-b0a7-1c1b47026d5d | -13.92595 | -47.85349 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| bd20f91f-47d3-3258-bff5-d9dfec547c17 | -11.63578 | -43.50461 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 2028662f-066e-3ec0-aa65-611dabcbe28c | -12.73721 | -47.27776 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a31d87e2-1dcd-338a-8251-0e170062fa84 | -15.68804 | -47.59937 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5a4aa493-5cfc-3c58-9ca4-7223e36eed2a | -11.71768 | -44.52562 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b3622463-3059-3f1e-a551-029a0bdcb7fe | -18.08596 | -44.53649 | 2026-09-28 17:07:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35229fd0-540c-30ee-b7fc-4923bba579db | -18.18909 | -43.84158 | 2026-09-28 17:07:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 498d5b49-2d55-3b7c-bac0-a3fc526fe923 | -15.0412 | -48.04161 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 43001eb2-b34f-3713-bb18-9fe042f57f35 | -14.32451 | -44.82025 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c0f9bd33-5376-31d5-97e3-71bf495b9c05 | -12.94105 | -46.63595 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 4f4e9d9c-26a4-3a15-8731-ce8e45b45346 | -15.8508 | -41.26812 | 2026-09-28 17:07:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| d5ec9275-4d5b-3d0a-b9a5-d208ef569ee3 | -15.40527 | -47.91837 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 08bd7784-beb1-38d5-91db-b50f9037bc3d | -12.09965 | -45.23095 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 65e590e6-d56e-3ee1-a088-54967bf15666 | -17.35197 | -42.15068 | 2026-09-28 17:07:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 7c86f4b0-5c42-3470-a548-33078c067950 | -15.91683 | -40.98541 | 2026-09-28 17:07:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 118df767-f03d-3ac2-a9d5-d7383d5c840e | -16.80372 | -40.77531 | 2026-09-28 17:07:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 79aed4e7-31dc-3c00-a4c5-035f3be6149a | -15.0673 | -54.60784 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 86acc768-ed4b-3d25-a4a0-3512c66f6c2b | -14.32575 | -44.82657 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 2d2d0f69-90b9-335e-a0d9-ed1316728248 | -12.90746 | -52.06382 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 969ba7c2-a74b-358e-a92e-746f2819b2ef | -14.71683 | -41.86658 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 55326ee1-ee1d-3eda-87c9-8865ff43d9c4 | -14.71772 | -45.56684 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 9a9645e2-5aa6-3cef-94be-6b2afa0e92d0 | -11.2892 | -43.5448 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 4c704800-3ae5-3ff7-9997-e8dce5800d06 | -11.90055 | -47.02173 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 7f1ed743-c655-3b0c-ac5b-cf599ecc8c1e | -13.37755 | -44.02481 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 3e9fbd24-a215-36df-ac51-8b4038d6a5e0 | -12.31484 | -46.40608 | 2026-09-28 17:07:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c63d8738-cd57-31f2-bb84-3f98d071d552 | -14.43783 | -52.12259 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fa594998-5b5a-3b67-ad84-c7d285399303 | -13.16434 | -48.56269 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 942120f1-d070-30bc-a514-96a3ad3536e7 | -16.88604 | -46.90026 | 2026-09-28 17:07:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 25d8a0c3-60ba-33aa-93ad-05553c155e42 | -13.15652 | -48.56312 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b947ecd0-bca7-311e-8fcc-e4028515189f | -12.84054 | -43.39403 | 2026-09-28 17:07:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0cb344cf-d671-3aec-b3ea-3cdbaa74deb3 | -15.2586 | -44.82569 | 2026-09-28 17:07:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3200fd5a-89d7-3dc7-83ea-909fe85c31d6 | -16.98853 | -41.94472 | 2026-09-28 17:07:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 3e98a75d-850a-36bf-b694-d2213223e561 | -15.34697 | -42.16564 | 2026-09-28 17:07:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5fc63157-f5bd-36f6-9a04-724b3fdedfd7 | -13.40506 | -43.44689 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 3583739c-63f0-3151-ba16-3887f850f43d | -13.38584 | -51.32285 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b0e4727e-5c5f-3407-9cf0-24b630c33c84 | -15.71974 | -42.62196 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 647c86b8-83fc-3a3f-be4c-1154ddda4208 | -17.18055 | -51.74157 | 2026-09-28 17:07:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fa487bec-ef8d-3b3d-bf11-e41825388569 | -11.35867 | -43.40992 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1a279218-c710-3175-8a91-804ec8349be4 | -15.15878 | -43.61234 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 07269c16-0747-38a8-a74a-f6b5dd414620 | -13.6909 | -48.81919 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 798243f2-d5d2-3f40-9c43-1eecea054eb0 | -13.97994 | -54.01232 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 563c1424-2ad6-31f4-aad5-2d59d0a259c9 | -18.74934 | -46.22346 | 2026-09-28 17:07:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d529d2f6-d7ce-32b0-b4f4-1f47bc19d4c6 | -12.67509 | -47.35755 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| abbbfe0d-5e45-3bc9-b01b-2532247cc556 | -14.66541 | -41.83294 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| f0388360-52eb-3602-b6b0-5391dc9bbf41 | -15.08014 | -54.60218 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 63fa6bb7-c9f6-38e2-a31c-f0dc2d5044b3 | -15.68527 | -47.6079 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ff1c24f6-dde6-3dd2-9e53-d217a0b6dc5a | -16.44951 | -43.37721 | 2026-09-28 17:07:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 53f1b5b0-2c47-3c4a-9edc-f877f8c908e1 | -15.40657 | -47.90185 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff2a8f17-1cbd-328b-9d3e-c7bd39775ca5 | -15.16328 | -46.14407 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4307d895-76dd-3213-91f6-e6962c6b6ece | -14.11399 | -46.30165 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ce518996-d05b-3b6a-a731-0cc3d9d745a5 | -14.67587 | -41.64198 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| aa7e4fd5-57bf-318c-95b0-01f1d8a0a965 | -15.07291 | -54.59956 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 72c49b80-ec16-361a-8940-fbe1db2e6c39 | -14.09747 | -46.31626 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e4196922-032f-3927-988c-e64e08180399 | -17.82661 | -44.3909 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| a0580da7-c5d6-3ffa-9c81-258c89409ca5 | -14.63317 | -52.11206 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 960afa9d-0757-3218-b3e5-61dc2cdc1f76 | -16.79125 | -43.00967 | 2026-09-28 17:07:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 133045c5-3593-3f68-96cd-beae92f3a5a3 | -11.35953 | -43.41427 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 69255c6c-928a-380a-9953-97715b3326f9 | -19.14977 | -46.53829 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| da637114-6b84-340a-9c3d-55ad832f3838 | -13.9761 | -54.0093 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 93b54e43-bff8-3fad-925f-c0058d02c899 | -17.57968 | -44.3727 | 2026-09-28 17:07:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 19614c9f-3d7e-3055-972d-fc95d0f9541e | -11.90019 | -41.70392 | 2026-09-28 17:07:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0598b6e4-a7ee-351c-b5d6-87be1261aa3a | -14.28867 | -41.58101 | 2026-09-28 17:07:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e85aa775-2752-3db4-94fc-96dbe8d80e13 | -14.61882 | -42.40275 | 2026-09-28 17:07:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 33.9 |
| 85e44b06-e79b-35eb-bb32-3158c8e7ef61 | -15.86523 | -41.275 | 2026-09-28 17:07:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 86cd65b0-daae-3ff1-b89a-538b4813e44e | -13.09761 | -43.51674 | 2026-09-28 17:07:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6f81a48c-9fa6-3376-9fbd-c8b9877ce476 | -14.64167 | -52.12197 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| edea1462-dbcb-3e9a-a716-4a7fac3428dc | -14.3226 | -44.825 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f47ae747-5db1-30f8-9505-1e58857cd3ea | -17.20114 | -46.64679 | 2026-09-28 17:07:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4145084-640b-3f67-98b4-ed417276e261 | -16.1531 | -42.85432 | 2026-09-28 17:07:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 81175702-3939-332d-8efe-204dc0efdef5 | -12.72823 | -47.27913 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 736fdf6c-ca8f-3c2b-935c-6ae169cc310d | -12.57264 | -47.67081 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 778e283d-8fe2-3a17-b874-6fed0b93cd77 | -11.90977 | -47.02006 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5ae6f23a-07ed-3a2c-8a78-5005f781692f | -15.16098 | -43.62312 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 20.1 |


[Clique aqui para ver as próximas entradas](README134.md)
