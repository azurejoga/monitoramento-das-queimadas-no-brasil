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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3091cc60-5502-3af3-a7c0-2985a180fe25 | -14.45706 | -43.95587 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a3d80a82-69a8-357d-9d7b-1bc0a8978fe0 | -14.45075 | -43.93896 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b75fa8f0-d24c-3c41-88a0-0865537274da | -11.92425 | -46.77155 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3add66b-92cd-398d-8c15-5fbdbb8c6ee5 | -11.85358 | -46.78553 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4630eab3-a71e-3830-8c87-755a6a457487 | -7.92339 | -54.71873 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0886f26-5a0e-353c-8cf5-d59dd75ab4cf | -10.7347 | -52.02906 | 2026-10-10 04:46:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3bf788a-cf81-35ec-8588-a6fb50d3762c | -13.74188 | -44.3049 | 2026-10-10 04:46:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1f2b3c0-ed0c-3b48-890d-2fecdbbd43e0 | -11.87352 | -43.58468 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4fb8462-4b25-3c11-94fd-10e8757b6bf0 | -14.44759 | -43.93047 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 703dce5c-f9b9-32f8-ba2b-859be24f8360 | -9.11693 | -45.82238 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4807952-66c3-3298-be72-a3468f63624a | -11.75343 | -46.77919 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf38cd2f-fe0b-31cb-802e-19616c18d0c4 | -13.6773 | -49.11542 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 966af2fc-9221-31fa-9168-104fbb99f300 | -11.38944 | -47.58143 | 2026-10-10 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc6f6f44-851f-3dd8-b1bf-7d168c73365c | -14.23669 | -47.30521 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbef829c-8f97-35e8-ad10-4e702458f77f | -10.61257 | -43.26904 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d6c099c8-0105-3e4f-8622-bc2bdc619049 | -11.65499 | -43.67011 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34adfee0-fe37-3d79-9532-ee345d255530 | -7.01117 | -47.6669 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad7b4a6a-9c09-3a1f-8e61-492f741875e8 | -11.37795 | -54.03088 | 2026-10-10 04:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1f9dc0c-ed5b-3a04-990f-a25666580bb2 | -8.30151 | -50.8031 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a2f8c42-ff64-32d4-acb8-5f648ad8cd1f | -9.93917 | -44.89273 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd8109fd-df47-33b3-8b1d-f2a6bedd486a | -9.00785 | -44.36808 | 2026-10-10 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7599248-477b-3cf7-ab07-d9929c48a9a7 | -12.02453 | -43.49186 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bb87d16-16d3-3e1e-97f0-27125071a816 | -13.63159 | -44.42045 | 2026-10-10 04:46:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c50b7dd0-e5bc-3ac8-8197-80abf1d68e09 | -11.46837 | -43.38149 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b12b58e-2775-3ed6-9b94-e0f63f00988a | -12.34133 | -48.19336 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88afc4aa-b3db-36c0-9417-229a7b8a9ad5 | -6.37079 | -55.16121 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d7bf7ec-9b25-3571-9c3d-68621d3dbea8 | -6.93572 | -59.25704 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45781233-eea0-3821-ab78-9917d502a3e2 | -7.03001 | -47.6556 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d021c619-2a7e-34cf-a22b-e8e384c171cf | -11.02552 | -44.02509 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a15db31-789f-3af7-8ed2-3fbb73c34554 | -9.68767 | -47.80711 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71a1ccd4-4f60-35cd-8503-24aa0bfb9e68 | -11.37703 | -47.57207 | 2026-10-10 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8f8602e-5310-3a72-9844-d61217236b19 | -14.81199 | -42.3316 | 2026-10-10 04:46:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ea0b2d2-50a0-3bfc-b640-5adc4d0ef766 | -11.95642 | -43.48393 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4847df42-1a0a-3b00-96af-818626390b51 | -9.12457 | -45.81958 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fefccf3-8714-3a73-8860-c010399ab6d1 | -11.00336 | -47.9571 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1841d1ea-b23c-3544-81a9-4cb95f279d19 | -6.37846 | -56.22123 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 852b4e48-ba79-3e53-acaf-3b46cb54632a | -13.72395 | -49.12312 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ede1d974-af17-3a0f-9585-387b2be5e599 | -11.95802 | -43.47234 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f0cef0e-3bf0-3171-93bb-e84a27590a74 | -14.32526 | -44.6623 | 2026-10-10 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d23aea5d-079a-32b9-ae38-db395250dd92 | -11.96006 | -43.48843 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac67e502-e36c-3296-9db8-7c26d58e5c58 | -13.70289 | -49.08309 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9efabbd9-34c4-37dc-b82b-d5d21c369e6a | -11.08484 | -44.10968 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee1f8ac9-d6ea-39ba-818d-50d97b4c7277 | -10.89392 | -44.80664 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af623ee5-3cbc-3d78-bf38-f8d0aedda8bb | -11.77236 | -46.80516 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88825786-df46-31ba-81b8-4076cc34ad58 | -9.51145 | -54.66829 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1f79d8a-5608-3e56-bf06-f14e49830025 | -7.18427 | -46.54024 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7951d0d9-f2c7-31d7-a75d-dc531228941c | -6.94284 | -59.11056 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a2ee4dca-d62d-3143-bbaa-a0ddca40a49a | -11.02384 | -45.42248 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8632a3f6-85a3-3a0f-9faf-d16e6f632025 | -9.3159 | -47.37344 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 29c3e5ae-e564-3c1c-983e-65e6031f173e | -13.76616 | -48.1346 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84881368-68cd-38db-babc-30f55771f587 | -9.21496 | -45.65346 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a4a2bd1-8d4e-3db3-8f41-ee5f85034e76 | -11.03422 | -44.02107 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7e7f69e-f739-30e8-9f73-a81c6dde40ae | -6.80376 | -52.7833 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64dd81cb-2eba-3c51-a0d8-a6f0f677a04d | -10.41572 | -47.29629 | 2026-10-10 04:46:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35f2d717-7332-3f0e-bdd4-34ffdb2efbcc | -7.00236 | -47.72257 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83cb441f-cb08-3fab-b31d-6d9de56d2805 | -12.36629 | -46.60692 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d87493f-c77a-35de-83fa-3159d7ad52b5 | -6.50739 | -55.36247 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a367c577-ce1b-325c-a7c4-4f24fd674521 | -7.93868 | -49.74543 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cac0203-50ae-3f6a-866c-2b94a877ed9a | -13.17447 | -48.12482 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a3e8d9a-17ad-3979-8173-8c417e6b3999 | -13.73904 | -48.51154 | 2026-10-10 04:46:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81691ffb-014c-38df-afc7-983d6e848035 | -11.76184 | -45.45816 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7697a93-44c9-3078-b856-cb1cbf1367cd | -12.96073 | -44.58546 | 2026-10-10 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9246e2c8-cac0-3dc2-9889-3f9f477d7f6b | -6.31997 | -58.30997 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29660976-2485-3f24-aa88-c5a8be495a3c | -6.94269 | -59.25363 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6a370e2-52ce-3f88-a85a-866ffc3c901a | -9.90196 | -44.78123 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8ca0dde0-5df2-353c-91ba-3ebf64789c48 | -8.66669 | -44.87605 | 2026-10-10 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a37e9b59-e0c2-350a-8e06-59009110a13a | -6.37178 | -56.22937 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b26783-30fb-3253-98dc-440f7536553c | -11.02078 | -45.41778 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70d5619f-955c-37b8-8ecf-c2bc7ade240e | -15.37936 | -41.9007 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5306fe9a-cd80-3095-98df-1ef7cdca974b | -11.83158 | -43.58233 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07f6e5af-8fc9-3d59-bd5b-f210b3528de1 | -8.15247 | -49.43921 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31ce5f93-fac6-3846-a740-9121125eb9c0 | -8.95858 | -47.37624 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdb48aa6-4438-3aa7-92b6-35db48ae26cb | -9.89746 | -45.19965 | 2026-10-10 04:46:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0df5f190-0890-39bb-9805-e77d0cd25e94 | -7.21937 | -55.1548 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dcc44b4a-a10f-39e9-84bb-8f6ca04c0ecf | -6.753 | -55.07845 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ea452c7-9e0e-33aa-a86a-549d16c6e6c6 | -12.37278 | -46.58755 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17b22977-24cb-36b9-bc79-48e50f971d21 | -6.44219 | -55.05988 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b371907f-c4c1-354e-9d1e-3f1f9cc5715f | -11.08736 | -44.12051 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b4734b3b-f892-358b-b8e0-79f603684dc0 | -13.50775 | -48.60788 | 2026-10-10 04:46:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 516886fa-a56d-333a-a5ae-8d9b700ea0ae | -12.12129 | -43.31793 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00c4d7ec-67fb-3c73-b9f2-06a1c7433e3a | -13.15622 | -54.36461 | 2026-10-10 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c84dff2c-6528-3812-9012-571f30a0a27f | -11.89471 | -47.35708 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8b67437-f270-32eb-b777-0bfa98f4bf2e | -6.46325 | -55.50126 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b80905e-74d4-3f5e-998b-e6b6b2609f68 | -7.03944 | -47.66066 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4414d6ae-480d-34b6-aecd-cd5b9e3176d4 | -12.50064 | -51.32329 | 2026-10-10 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fa7269a-a1db-330f-bfe3-49263a5eda61 | -5.18635 | -60.30701 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 640b87a0-cda0-3229-b321-0fd8f3f6978c | -8.19583 | -45.74575 | 2026-10-10 04:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e3a33c0d-8e4f-3b60-a307-7b60e6b1cec9 | -9.01164 | -44.3687 | 2026-10-10 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 520acbce-50b2-3fff-8813-43fe89c39970 | -15.37608 | -41.9274 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 21deb6e2-cf0f-32c0-94aa-355aaec2588f | -11.83982 | -43.61423 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcc42e4e-0da8-3b58-b2b5-0102ded3f274 | -10.4421 | -50.54219 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f89b00a-1e30-3080-896f-f43cfa2c5ffd | -5.99164 | -55.37465 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f185e2f-460c-3424-99ea-3ee45e8d7228 | -12.3003 | -47.04794 | 2026-10-10 04:46:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5f5da05-0437-3c89-bc57-4556452f12bc | -8.25611 | -46.41838 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a9344f8-4a2f-3834-b4fe-39703e6f2e4c | -7.08601 | -52.68538 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf194011-0b6c-397b-af84-768220309c9e | -6.05935 | -53.29124 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4770d53-a2d2-38dc-b96c-a5e10ec2426b | -6.81075 | -59.3204 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5541c183-cbfc-36bb-8ea0-f6ae0cfa52f0 | -11.37648 | -47.57567 | 2026-10-10 04:46:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b604a87e-e53d-3a34-87d2-23d8f3e4295a | -8.23445 | -46.42714 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f4ae9db-f50a-3ee7-a9b9-cd72a46b5132 | -12.04177 | -48.53005 | 2026-10-10 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README73.md)
