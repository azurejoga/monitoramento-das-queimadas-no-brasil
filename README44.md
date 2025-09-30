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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 192f0c6f-c6f3-33e1-8f7c-d28b743a53c6 | -13.2154 | -50.9715 | 2025-09-30 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 5ec59425-82ec-3925-a530-0c76146f1693 | -4.9102 | -43.4666 | 2025-09-30 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 111eb117-4ea0-3090-9ec8-aeffa0497440 | -22.5205 | -44.597 | 2025-09-30 03:50:00 | GOES-19 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| 4cbc4509-5781-3358-b8ea-90711695c6f6 | -11.1546 | -54.126 | 2025-09-30 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 201.7 |
| fa93b16b-f440-3825-a760-fa489d701b5b | -19.73152 | -49.65599 | 2025-09-30 03:51:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0c65c457-5917-3d21-80c0-8072eb1556d8 | -21.76972 | -45.09722 | 2025-09-30 03:51:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 06abdb79-fbce-3b87-bde2-07f3af099d9c | -20.61184 | -46.18975 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e78d4d64-e95b-3caf-bc83-adbeaa181a89 | -22.51617 | -44.5987 | 2025-09-30 03:51:00 | NOAA-20 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| fe30a60a-46e4-3eda-85df-9258193dcf76 | -21.09082 | -45.33778 | 2025-09-30 03:51:00 | NOAA-20 | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d2a4723a-0867-39ca-a08d-e4e069c59cb0 | -19.89227 | -42.62926 | 2025-09-30 03:51:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 262dab18-d915-36b5-adbf-4a077493be42 | -22.33624 | -49.47974 | 2025-09-30 03:51:00 | NOAA-20 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 65178914-7139-3142-999c-4a41c1301e8a | -19.18236 | -46.0449 | 2025-09-30 03:51:00 | NOAA-20 | MATUTINA | MINAS GERAIS | Brasil | 3141207 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40cc42f2-177c-3cd0-9087-a73dab197290 | -22.33689 | -49.48194 | 2025-09-30 03:51:00 | NOAA-20 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8518c84d-f934-3ffa-a557-f1644b10e357 | -21.09013 | -45.3415 | 2025-09-30 03:51:00 | NOAA-20 | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4c7c655b-eaa0-32c8-abcf-694164a66c33 | -20.10029 | -45.31854 | 2025-09-30 03:51:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a6487e0-b4cb-3412-a54b-b3b61889337c | -19.97668 | -41.91131 | 2025-09-30 03:51:00 | NOAA-20 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ae5b5ea6-dfaa-3557-8028-1f086c9431ea | -23.23734 | -46.15632 | 2025-09-30 03:51:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d10e39ec-11f9-3b2c-a25b-0bd85a673174 | -20.05676 | -41.32815 | 2025-09-30 03:51:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d3822a3a-627e-353a-8c25-a0ddbb468967 | -20.04262 | -41.32972 | 2025-09-30 03:51:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4c9d9302-a09a-3e51-a308-af2933314731 | -20.6164 | -46.18594 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2de87d1d-cd51-35d4-9b55-0ad584f0d7dd | -20.62135 | -46.18311 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99aea61b-94a5-36d6-a3ac-cffe6e0bd658 | -21.93418 | -42.79649 | 2025-09-30 03:51:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69114fa3-f7de-3700-8619-ecfae94a73a9 | -20.53016 | -43.13355 | 2025-09-30 03:51:00 | NOAA-20 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c954520f-5ff6-3fe1-bfd2-eb73a14f97c7 | -21.61647 | -44.05983 | 2025-09-30 03:51:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6273a00e-1fa2-3c27-9703-ef8c8c777eda | -20.4162 | -43.34842 | 2025-09-30 03:51:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 195d9fa9-f363-309b-a87d-c24a261429b7 | -20.41824 | -43.35798 | 2025-09-30 03:51:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 170baf6b-525d-373f-87e6-5c04d06acca8 | -19.30362 | -46.24316 | 2025-09-30 03:51:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 114774ec-19a9-3b0d-992d-4d499ceef793 | -19.30276 | -46.24752 | 2025-09-30 03:51:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4bbd7a2-ef8a-3a2a-919d-4906929f7976 | -21.62382 | -44.06134 | 2025-09-30 03:51:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 520d2e7a-7396-3a25-be9d-d882d06b22e2 | -19.90917 | -41.98034 | 2025-09-30 03:51:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 90d3b8d8-a7f3-3ccc-b11c-252997be411a | -21.9307 | -42.79586 | 2025-09-30 03:51:00 | NOAA-20 | ALÉM PARAÍBA | MINAS GERAIS | Brasil | 3101508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5d1315f4-f839-3591-ac73-56a01f1a33e0 | -22.84828 | -45.44829 | 2025-09-30 03:51:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ddeb467f-3ab3-34e1-9020-66c2ac72992f | -20.04327 | -41.32578 | 2025-09-30 03:51:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f8e4fb2c-8419-34be-b32e-ae931d7f6b84 | -21.16175 | -43.61726 | 2025-09-30 03:51:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9cfb6c43-a802-3aee-a6aa-1d2c4befde39 | -19.55691 | -44.95294 | 2025-09-30 03:51:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72d29d72-d375-3714-a7c3-0ca7879b10a8 | -19.69643 | -43.69257 | 2025-09-30 03:51:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 895cc186-0b14-35d7-8a46-784043e26c22 | -19.85378 | -43.8154 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d12e2048-f07d-3caf-ad47-24b0360ceb42 | -20.7451 | -47.14692 | 2025-09-30 03:51:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c230b6c-1b61-31e6-b417-d1a19084624d | -20.62223 | -46.17868 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcc9f2df-00aa-30df-9140-0d6f9026679a | -21.40189 | -44.27481 | 2025-09-30 03:51:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 22e4b60e-da8b-3e9a-9ce2-8edec2a14abb | -20.23911 | -41.62846 | 2025-09-30 03:51:00 | NOAA-20 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 76ec7673-1504-36f2-a244-ff6eb184985f | -21.89383 | -45.75733 | 2025-09-30 03:51:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fa11d5e4-4024-3987-9635-2ec1bc94dfc1 | -20.4273 | -46.171 | 2025-09-30 03:51:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a87552c-24df-35a6-94cd-efcdb8cb7a06 | -20.74224 | -47.147 | 2025-09-30 03:51:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 060b851c-b0d1-3f37-a2e4-d6cd9a0eb1b0 | -20.96237 | -46.29373 | 2025-09-30 03:51:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f2dbea7d-9946-3311-93c2-cef5ce6a0680 | -22.51346 | -44.61357 | 2025-09-30 03:51:00 | NOAA-20 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 6fd54a57-6ab0-3fc1-854c-5ac99fe0eebb | -21.47576 | -44.36307 | 2025-09-30 03:51:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8142e4fb-35a4-3870-b881-2cae9b4a41a1 | -20.39431 | -43.68325 | 2025-09-30 03:51:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 71c9fa7a-960c-3cbd-a088-e026808e18dd | -22.0627 | -45.64313 | 2025-09-30 03:51:00 | NOAA-20 | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1aa07b2e-3a53-3214-b4c9-1d42dd8384da | -19.86553 | -44.55737 | 2025-09-30 03:51:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 457e8a9f-400f-359b-8f1c-c305e0d1ea7b | -20.06204 | -46.79858 | 2025-09-30 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78eca2b4-08cb-36bf-818d-3353fb0a394e | -23.56668 | -46.38554 | 2025-09-30 03:51:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40ec828b-95af-35e3-8ddd-5821ac18445f | -19.60009 | -45.88911 | 2025-09-30 03:51:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 964c2dd7-ff21-3042-928a-e3560f896266 | -19.69357 | -43.68711 | 2025-09-30 03:51:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ba14253e-b18e-365c-bce6-e218c127fef3 | -20.42104 | -43.36324 | 2025-09-30 03:51:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25d490f3-5225-30f6-ab18-3044c5e92bf5 | -20.61065 | -46.19281 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef5f6047-a231-344d-951d-6cc334690695 | -20.09093 | -43.90204 | 2025-09-30 03:51:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d83d32cc-7054-3d38-8979-6776ff7b1311 | -23.23073 | -46.78302 | 2025-09-30 03:51:00 | NOAA-20 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0cbd8c92-569c-34e8-83fc-a4750aa4f00b | -21.88981 | -45.75649 | 2025-09-30 03:51:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dc11af6b-0e63-3dc6-95f4-46000af973fa | -19.85391 | -43.8091 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 93d0e773-4ba7-3db5-b4c0-64c14d96b860 | -22.02108 | -42.20678 | 2025-09-30 03:51:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a99bc4ad-d20c-3655-be00-c0a33a063dcf | -19.85178 | -43.8053 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a00b24b2-d1c5-3c7a-b8f3-89faf9c4693a | -20.09623 | -45.31782 | 2025-09-30 03:51:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f879377c-2751-3c50-a2f9-41c19a483f03 | -19.85592 | -43.81954 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| da1b8b79-0d12-3051-aa88-81142ca2fded | -20.2872 | -46.23792 | 2025-09-30 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ef62f4b8-29c2-3efd-a261-ee16b6e27e4a | -22.51814 | -44.60918 | 2025-09-30 03:51:00 | NOAA-20 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| a8697b90-4591-3915-9a7b-53686fcd3a2b | -19.85749 | -43.81622 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 848602e0-bf54-315f-81c5-76a75a1ca5a5 | -22.33122 | -49.48388 | 2025-09-30 03:51:00 | NOAA-20 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d767aa29-f395-3b54-8e35-c69f4ef9410d | -21.89003 | -45.75333 | 2025-09-30 03:51:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 76b4078b-324e-3cb9-b194-c4a2b654e2be | -20.08627 | -43.90642 | 2025-09-30 03:51:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 512d9302-44a2-3649-a627-51e8172bbd44 | -22.51242 | -44.59802 | 2025-09-30 03:51:00 | NOAA-20 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d7dc0e50-53ec-35ae-ad65-e93439897765 | -19.85592 | -42.58755 | 2025-09-30 03:51:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 896cfb6f-8c92-38dc-bba2-ec51d90eba73 | -21.33566 | -46.73109 | 2025-09-30 03:51:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ba7bd94f-de2e-3292-ae6b-17ccc5848cc7 | -20.61245 | -46.0719 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb6871f3-4f31-3c75-b2b7-2fdc5cf77430 | -20.61105 | -46.19386 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 836b3c88-848c-3637-bfde-687eb8fad456 | -22.49642 | -45.76816 | 2025-09-30 03:51:00 | NOAA-20 | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| be4d8f6a-435c-3bdc-a0d2-c8de7c1905bd | -19.59881 | -43.82255 | 2025-09-30 03:51:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4a9e622b-1d0b-367a-91e1-9ba0c90612d6 | -19.73231 | -49.65233 | 2025-09-30 03:51:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| da2bc5a2-7747-3556-825b-a4f0f3124b3e | -19.85092 | -43.80996 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0796fd3c-ada1-3dd9-94ad-3d86f2ee695c | -19.94142 | -41.6437 | 2025-09-30 03:51:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| a0c67c14-498a-39c5-be09-49439f4c9b83 | -22.02041 | -42.21073 | 2025-09-30 03:51:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e88cac57-ac19-3b3d-82c3-7d85ecd8dd1c | -21.89334 | -45.75801 | 2025-09-30 03:51:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1feda742-8676-347a-a589-03284b0d557a | -19.59588 | -45.88816 | 2025-09-30 03:51:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e410661e-cfd7-3af4-94ae-aee1232db864 | -21.73708 | -44.61758 | 2025-09-30 03:51:00 | NOAA-20 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 09fc0558-498d-36df-9d17-c68d1cb7e79f | -23.23686 | -46.15649 | 2025-09-30 03:51:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 17fddb0a-44f2-3aa5-970c-573485c5843f | -20.05001 | -41.32694 | 2025-09-30 03:51:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| c0cbb6e5-60f3-3609-b0aa-62f87b038a24 | -22.172 | -46.74063 | 2025-09-30 03:51:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 6e1ad726-82b1-3c5c-87ce-aae783a06804 | -19.85005 | -43.8147 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 3a4dbd89-bbd0-357f-aaae-4b9ad55c86f5 | -23.19768 | -49.97866 | 2025-09-30 03:51:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 01ffa5a7-41c5-3480-832a-c6b19311fc2b | -21.25811 | -43.85416 | 2025-09-30 03:51:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4ab8b9e3-78e1-3a60-a985-694d74d8fa9a | -21.0915 | -45.33413 | 2025-09-30 03:51:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 746dcd17-f483-3ef2-835b-6f6f0b15140a | -19.86016 | -42.58411 | 2025-09-30 03:51:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b140303f-6234-3783-8e3e-7aaaf26c8576 | -21.22362 | -47.1344 | 2025-09-30 03:51:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 07ceffd0-bafc-3def-99de-e90e31ce6616 | -19.94209 | -41.63974 | 2025-09-30 03:51:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| a1e39fe6-4d45-3a68-9ada-eb4ef7887c08 | -19.86067 | -44.56183 | 2025-09-30 03:51:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9a406071-f978-34dd-83fb-a95251c9a416 | -21.25847 | -43.85618 | 2025-09-30 03:51:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 253e7577-bd18-3917-a809-2d67199f715b | -21.6193 | -44.06528 | 2025-09-30 03:51:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f2f990f6-7c6e-3455-8f61-0ef48368c037 | -21.22801 | -47.13554 | 2025-09-30 03:51:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2da830b7-0958-32fe-9701-d39276f2e713 | -20.05612 | -41.33198 | 2025-09-30 03:51:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 97c3b739-a5eb-3620-aa36-079cd20ced75 | -21.31326 | -46.75355 | 2025-09-30 03:51:00 | NOAA-20 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README45.md)
