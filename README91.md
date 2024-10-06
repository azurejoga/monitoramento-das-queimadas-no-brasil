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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dca001f-12fb-3b66-b6e4-6b407952165f | -19.83154 | -46.44429 | 2024-10-06 04:21:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e780bfc3-d4c9-32af-8762-4e1139a4031f | -19.83099 | -46.44805 | 2024-10-06 04:21:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7760a6d-9d53-3878-a0c2-d94baac7556a | -19.82874 | -46.44003 | 2024-10-06 04:21:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0bfe5a1a-aa63-3087-a4b2-195944fab0ac | -19.82818 | -46.44376 | 2024-10-06 04:21:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d93994d4-f012-377f-9d55-b3aa01801424 | -19.61373 | -46.25543 | 2024-10-06 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d81fbe07-f8ce-3caa-981b-0ea63b1aac66 | -19.61316 | -46.25922 | 2024-10-06 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66a1f313-0e35-3be3-98bf-6c9cbb49531a | -21.08295 | -45.7235 | 2024-10-06 04:21:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 19f8c65f-aa22-3b84-b468-deeb04d7693d | -21.78429 | -46.18951 | 2024-10-06 04:21:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 84895530-f543-322c-91bb-f452f390cedb | -21.78145 | -46.18493 | 2024-10-06 04:21:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 2eec3925-8fa2-34bd-8925-563492fdc475 | -21.78087 | -46.1889 | 2024-10-06 04:21:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 8e8a5246-c187-3ede-9b7f-d24a993a4650 | -21.60834 | -46.00636 | 2024-10-06 04:21:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 188e1055-5928-3b2f-9505-22a9ccad2079 | -20.98307 | -46.0751 | 2024-10-06 04:21:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 701e03de-7ad8-3304-9777-4ed5dbab6c5f | -23.30738 | -47.1075 | 2024-10-06 04:21:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5b5b4568-3e39-3056-99bc-2668c03b43ba | -23.11567 | -46.93603 | 2024-10-06 04:21:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fd1543d2-e4b4-3f9f-a601-94265fdc40ed | -22.96981 | -46.97265 | 2024-10-06 04:21:00 | NOAA-20 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9a662430-8b53-36d2-84a4-02f814791b6f | -22.75788 | -47.00978 | 2024-10-06 04:21:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 83e7d592-0440-353d-949b-a6094f1828f0 | -22.73645 | -47.03777 | 2024-10-06 04:21:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 86276989-ecd2-3b1c-9121-9f55e803f5de | -17.63323 | -46.98244 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 849421ae-1e7a-35d3-b994-17e11748eec9 | -17.63266 | -46.98606 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1ee5f23-a2f7-352b-aab9-6b1fabb5f3f8 | -17.63217 | -46.96745 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 541d1c6d-1e79-3317-91ad-c69df6840a68 | -17.6316 | -46.97106 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2f23bf6-2ae1-3578-bbf1-83f32861c145 | -17.63104 | -46.97467 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b4eff4a-afd1-3197-b9d6-1b95d9c1065e | -17.62991 | -46.98189 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a15ed3a0-22fd-3fe1-aa16-d25d72ee02e6 | -17.62942 | -46.96328 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46e2574f-e298-3f71-b710-7c93a90bd28c | -17.62886 | -46.96689 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c4e7dc2-bd50-338c-903f-e55f27126d71 | -17.62829 | -46.9705 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4facf19d-e37f-3b62-a12a-bf86c3452fbe | -17.62611 | -46.96272 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdfc9d8b-691f-30ca-b142-3df2a4e1cd93 | -17.6228 | -46.96216 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23387e8f-c660-3927-89d4-4bfdd9b07d24 | -17.62005 | -46.95799 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b1aea1a-b1ea-3df1-b1af-5b47f8fec76f | -17.61949 | -46.9616 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35fa4930-91e7-35f4-8b64-87144f041a14 | -17.61562 | -46.96465 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64a726a8-6c2e-3631-82f7-09092e1beabd | -17.60463 | -46.94796 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e0e9634-7084-3c20-b137-9a31cf5b1e69 | -17.58095 | -46.92544 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d33fedf-bd57-3b08-830c-39ec902ba9cd | -17.57983 | -46.93267 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c7449e6-6a2f-30d4-8cff-d2744f8cb295 | -17.57767 | -46.9258 | 2024-10-06 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bd507be-0012-388d-b052-fa4a48bf5513 | -16.99282 | -47.08264 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa8e6958-ed67-3a26-85c2-0240274e2505 | -16.96946 | -47.12287 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca45ce62-611c-3b49-9061-483c0f235c74 | -16.96889 | -47.12647 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c20435e-e781-3f11-8a25-8fb55dae6a3d | -16.96559 | -47.1259 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c966b4a-f13d-3afd-a364-5cc6cfb5fc61 | -16.96285 | -47.12175 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eae96f87-a718-3d15-b774-185fd0b72bc0 | -16.95954 | -47.12119 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2202b017-a779-37a1-9342-53774f8c9e46 | -16.95567 | -47.12422 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea641342-b6a7-3095-b617-75761841ba9a | -16.95236 | -47.12366 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce2c3a2e-b40b-3456-882b-a4d358f2a33c | -16.94906 | -47.12309 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba8cca52-0bb3-3c50-8cbf-945559d3b73b | -16.94849 | -47.12669 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fe91de7-466e-3c70-b9f2-06ca2b5915f0 | -16.93696 | -47.11367 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fce380c-c450-34f2-88c0-41c0a40b50e3 | -16.93679 | -47.15788 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e486bfe3-b044-3487-95cc-239303f84c34 | -16.92743 | -47.15259 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2114944-9ea2-34e0-a970-6b27617318db | -16.91742 | -47.17302 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 830a5a6a-934a-3369-a003-02d372a6f901 | -16.91685 | -47.17661 | 2024-10-06 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c165c83-f956-3f85-b92a-789f02e5ae2b | -16.91468 | -47.16886 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf305d17-eb05-3887-8c5b-e76027cb5712 | -16.91412 | -47.17245 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| afaca042-974d-366e-9a72-87d1e558d068 | -16.91355 | -47.17605 | 2024-10-06 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c62998f8-c888-35e1-b40c-3453b9f6623d | -16.91307 | -47.15752 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38ba8244-f4d8-3092-9e84-a80ad81be6d4 | -16.90977 | -47.15696 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f8973bff-8eaa-371c-8dfa-2b553196d0d4 | -16.9092 | -47.16056 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0dffe6a-1441-31b4-a322-b1b46fb55ac1 | -16.90864 | -47.16415 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 74e3e645-c3b2-3093-8906-260e458748cb | -16.90807 | -47.16774 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 60c18b7a-6464-3057-ab3e-6a108e58129a | -16.9075 | -47.17133 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c7a7e099-8ae0-3153-8b83-44069a4cbe84 | -16.90476 | -47.16718 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ca962b8c-97a7-3d12-b297-be56fb6d46f9 | -16.9042 | -47.17076 | 2024-10-06 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| bb41b45c-06ca-3941-a704-aa82f6a80d71 | -17.41351 | -46.31825 | 2024-10-06 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73d8cbcd-33b0-31c1-afc5-3151ea660f29 | -16.91931 | -46.37566 | 2024-10-06 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8caf969f-7eea-30d2-8fe9-77ea9e0a8ec5 | -19.07149 | -47.01115 | 2024-10-06 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25fbed50-b502-3fa9-a8ac-8ed43272dd8a | -19.06873 | -47.00694 | 2024-10-06 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a21a0ab-043c-3a67-9526-86f0a21cfde4 | -19.06817 | -47.01059 | 2024-10-06 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5121fc02-dfe9-35a8-99a7-fd825f2d1fb8 | -18.88222 | -46.62954 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02977913-804e-3978-adc2-344d1016de94 | -18.87889 | -46.62898 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1920c7ef-290f-3b3c-9c15-fc0410567c16 | -18.64911 | -47.23841 | 2024-10-06 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d5f3287-b35f-317a-b251-6b466f7f1f10 | -18.47911 | -47.39254 | 2024-10-06 04:21:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e2596db-69a9-3cfe-bed1-51aac18fc98e | -18.4758 | -47.39196 | 2024-10-06 04:21:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1b1adb4-6ea2-30df-aadd-3da4e57b1b59 | -18.45731 | -46.65793 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6fa7431-a4c0-3f97-8169-8d0988c17fbd | -18.45674 | -46.66162 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9969b2bc-64ac-3a17-aa61-3e1fdddf6dd5 | -18.45619 | -46.66527 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d61ede6-2df1-3841-8243-fc88a4e0f5c2 | -18.4501 | -46.66048 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8ff6430-f790-3118-9bfa-b7af0676d8ab | -18.44678 | -46.6599 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96e1b364-2547-3246-a234-d1b4393364e5 | -18.44621 | -46.66358 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ea4a66e-3444-374f-99d0-4982d0564d49 | -18.4429 | -46.663 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5833524-f693-3735-90f0-ecace44c879f | -18.44234 | -46.66666 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ef7577e-ec39-39d3-a88e-44696d8fcdf5 | -18.44178 | -46.67031 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca8f8b93-23bd-37da-9a85-74a6d570d560 | -18.31216 | -47.56857 | 2024-10-06 04:21:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 529ff569-7f2f-3c1c-85bc-4e0232623137 | -18.30886 | -47.568 | 2024-10-06 04:21:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27703f1d-14f2-31bc-bd7b-d60583cde44e | -18.30498 | -47.57106 | 2024-10-06 04:21:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5afc78c1-0c3c-34d4-942c-8d7e44e0145f | -18.593 | -46.38956 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a2f47f8-f002-3a20-b0d8-389f26253f54 | -18.59245 | -46.39326 | 2024-10-06 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bf363a5-c92e-3c95-9760-04cc01c49a5b | -20.51759 | -47.49192 | 2024-10-06 04:21:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 0a8cfcd8-299d-313b-881f-373a03f9e1d7 | -20.51484 | -47.48766 | 2024-10-06 04:21:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b639798c-bded-3fc2-a0a1-cb5b48a07d33 | -20.51427 | -47.49134 | 2024-10-06 04:21:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| af6c552a-de92-3d3c-a4f4-249ae1a36e9f | -20.31363 | -47.20736 | 2024-10-06 04:21:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 09d5ec06-ec9d-3dd4-948f-0038a3417711 | -20.1966 | -47.46003 | 2024-10-06 04:21:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9c874fb-2f54-3455-8426-0e322da81e13 | -20.19272 | -47.46312 | 2024-10-06 04:21:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dda232fb-da3d-3d1b-8d69-f0408a6be4a5 | -19.96148 | -46.8265 | 2024-10-06 04:21:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf13a51b-b9c4-3583-bc7d-601017c2df11 | -19.95816 | -46.82589 | 2024-10-06 04:21:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd7d697e-aa88-312e-aede-0d34f9c6c5b0 | -19.95483 | -46.82529 | 2024-10-06 04:21:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce94eaa3-4b91-3395-af5e-530c0c27dd9b | -19.8765 | -47.8783 | 2024-10-06 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34749b8e-21df-3b39-adbd-a6e5a897611e | -19.85895 | -47.86018 | 2024-10-06 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e7c7bf0-b73d-3315-9026-f6401d5ddf70 | -19.85838 | -47.86383 | 2024-10-06 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56a40e28-9e1c-3f10-8329-9f3cf9d5d1aa | -19.85565 | -47.85959 | 2024-10-06 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75b37566-d880-3ec5-bed9-7e842296e845 | -19.84961 | -47.85477 | 2024-10-06 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dd3281e-ca0d-30b8-8c5d-69b67453c096 | -19.84903 | -47.85843 | 2024-10-06 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README92.md)
