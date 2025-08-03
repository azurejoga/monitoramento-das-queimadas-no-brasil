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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1fe6a69-30d0-3c7b-b95a-9393fc8d51d8 | -12.45996 | -47.02952 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8197d461-1b3d-3f2a-89ab-ca66dc275ea2 | -10.48046 | -46.96743 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf091eda-7f94-363a-8f85-0bcdac7466ed | -8.43608 | -45.59995 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03516ee2-da5f-3e0a-bb65-ab95f9b6cf64 | -6.95477 | -44.22679 | 2025-08-03 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 206fb738-86d8-3adc-896a-e8ab684f168d | -7.96219 | -45.11622 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b219c2e7-b725-3635-be1c-ab46b43d28e4 | -6.61915 | -59.95947 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ef763274-107b-30fc-be07-7fb2f5b091f0 | -7.52418 | -61.34085 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9399cc81-e681-3ac5-a9a7-ee114aae1fb3 | -8.0255 | -43.11872 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0e4de86-2d23-3dc4-a498-dc6d8d9a1fb7 | -8.43738 | -45.59626 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd9b3f43-ab86-3f26-b665-68f1ab2fa7f7 | -8.02024 | -43.14124 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 475d7cbc-4d43-3caa-8db0-52ec8b92edcd | -6.67098 | -59.15984 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd27eefd-eb47-3bae-9ed3-136ccbefa890 | -7.99367 | -43.18526 | 2025-08-03 04:53:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6e4c0c4-118b-3c17-8b51-f5d799b40acf | -8.0022 | -43.16427 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 1e25018c-4a54-38ad-8261-9611e4982116 | -6.65084 | -59.10412 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0dab9422-549a-30e6-b84a-21a69f20c6c6 | -6.82171 | -59.26158 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab2f2374-312b-32ab-b5a8-0225b974ecc3 | -12.03178 | -44.02399 | 2025-08-03 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4294c73-2110-35d4-83ac-653961476333 | -12.63152 | -44.51446 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df1f32ae-2e09-3528-9577-c389558f896a | -8.03358 | -43.14267 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 2db982f8-c7d4-355b-843d-efb5e31230d9 | -8.0017 | -43.16794 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3cc0b072-ffb1-3614-b724-75c6d1dde778 | -6.63184 | -59.94812 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b502033-31a3-3bfe-a6ff-8f08cfa2b258 | -7.5161 | -61.32691 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 130173ba-0775-3cd3-a6c6-f334c2abc9d0 | -12.41288 | -47.07061 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28e45a70-4d00-3fb5-ae8d-7eedf3888939 | -7.11189 | -43.48303 | 2025-08-03 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| dcc4d497-1652-3aff-87dd-4436c70b27d4 | -8.02242 | -43.14111 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 073dae3e-3526-3348-a6fb-96f451d1dcb2 | -12.63695 | -44.51521 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdacf79e-6de9-3571-a3c5-2ee0d7ff987d | -7.50878 | -49.74918 | 2025-08-03 04:53:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbc55dd2-f9d1-32b7-89f4-af5f2b023d36 | -8.01975 | -43.14495 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0bc91c6d-cea9-33fe-ab4e-6a8ad824df89 | -7.96029 | -45.11499 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09d34e20-3bbc-39cc-9e8b-6851149da0e3 | -12.62857 | -44.49274 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf30c3a7-feb1-34b0-a66e-a850d213aeba | -12.03226 | -44.0201 | 2025-08-03 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce650016-0eb1-3561-ab82-305195fde8fd | -10.46631 | -47.22737 | 2025-08-03 04:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a587ff8-7000-374f-9b07-499e35e81812 | -9.5851 | -43.84097 | 2025-08-03 04:53:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dd317a03-b5c4-3f6d-a576-d7165fbe6c29 | -12.64192 | -44.506 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c09deb8-3e4a-32ce-a1d1-78e581675d4c | -12.65449 | -44.50689 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb4bf481-15c8-3acb-9151-c929c5149484 | -13.0853 | -47.43447 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9abad307-1038-33a1-9118-d81d8b7fdd95 | -15.5497 | -54.27964 | 2025-08-03 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4d6df726-a2f5-3878-ac21-935e88954807 | -16.72285 | -49.42456 | 2025-08-03 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 195bd569-00df-3ae7-9547-4d2addd96c9c | -13.07194 | -47.43201 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68d2812b-5c48-3495-85c6-68e03d519ae2 | -12.68808 | -48.09452 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c90fc86e-3988-351e-805a-5ea7a96240ba | -20.0841 | -44.00084 | 2025-08-03 04:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ad193e0a-2b89-30a5-80eb-10164a1680d3 | -14.16305 | -45.42932 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8890b3a6-ab0d-3a8f-a316-d0cb3ecf343e | -13.07017 | -47.44537 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 557264d4-9012-3a2c-8e8e-deb9db818cfd | -14.17518 | -45.46038 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60b4fb13-3877-3d4c-8402-169a67e2a070 | -15.55359 | -54.2766 | 2025-08-03 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0378ad21-3280-3d86-b471-89aa5acab3ed | -18.23017 | -44.70585 | 2025-08-03 04:55:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f426b1d-603c-38fb-bca0-c2295b13d632 | -15.54749 | -54.27191 | 2025-08-03 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 451d4512-6920-3acd-84d8-bf5bc49cabad | -12.75552 | -56.57294 | 2025-08-03 04:55:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd6b03b2-c124-3835-aa54-e4a6b2c4a74e | -12.75836 | -56.57758 | 2025-08-03 04:55:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e980f072-dcf2-36e4-8a9e-4ae4c8f15d46 | -16.69987 | -49.39037 | 2025-08-03 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d053cd61-29f9-3160-be6b-a0f64a03fa43 | -17.87817 | -51.68945 | 2025-08-03 04:55:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1f14a42-466d-38df-97e7-b4b2d530de7b | -14.16593 | -45.44941 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c239004-e3f3-3055-bd80-80275fe67e6e | -18.97371 | -48.37375 | 2025-08-03 04:55:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91dbe2fa-d6e2-3c83-b561-bb639e465a09 | -12.03384 | -54.23846 | 2025-08-03 04:55:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94e15e9f-12e1-36a4-9237-26ad7dea40b6 | -12.68285 | -48.10101 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1b6ce8fc-404a-3f55-a916-96a42411717d | -14.00546 | -53.9285 | 2025-08-03 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce4a86db-24a6-3cc1-b3f6-b60aaeb04a3e | -14.17557 | -45.45715 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d99b5dd7-ca32-3ea9-a29e-d3217328b89c | -19.62559 | -43.17443 | 2025-08-03 04:55:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dfaf03d1-8508-36cc-964b-b009258e4a7e | -20.08437 | -43.99833 | 2025-08-03 04:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6daa9e6c-ca89-3d8b-8435-c62d88b20164 | -16.72698 | -49.42516 | 2025-08-03 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e1c052b-6de1-3aaa-b234-0413161273f0 | -12.75485 | -56.57696 | 2025-08-03 04:55:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 209a6524-44d3-35ae-a8e7-c53d67b1538a | -13.20797 | -47.24886 | 2025-08-03 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4a41489-1d72-368c-99d8-01a302eb0bbc | -14.16632 | -45.44617 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb8d68e3-0a4f-316a-98bc-1f9f8d4d98b0 | -14.1671 | -45.43967 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7454554-d93e-39e4-8971-b1fb5274c114 | -14.17479 | -45.4636 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a68e7776-1459-3c82-954e-bcf0bfef21a3 | -18.97364 | -48.37217 | 2025-08-03 04:55:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dd6c655-c352-3cba-bebb-01c7993a46a0 | -18.83809 | -46.44955 | 2025-08-03 04:55:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f5591b13-c3ef-3247-bc86-a60951120e6d | -14.14701 | -45.43066 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c69d863-fdf3-3e7b-ae98-c27557cab1f6 | -14.10177 | -54.00299 | 2025-08-03 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc815526-9f6e-31b6-ad20-d74b721ff683 | -18.23066 | -44.70128 | 2025-08-03 04:55:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 875d7de6-d133-3539-b4e5-89e5e39cb857 | -12.68436 | -48.09002 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00b123c1-58f1-3035-91a0-e5da9a3cc9a9 | -15.60199 | -46.52686 | 2025-08-03 04:55:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05a9dcf9-660b-3fe8-9f4b-79a297468c0b | -14.1418 | -45.43 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 801b5323-a873-3523-9374-f21956257bb6 | -13.02946 | -47.40769 | 2025-08-03 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d558189b-aff5-3a83-9a59-552b40ec7802 | -13.03004 | -47.40319 | 2025-08-03 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d41b60be-ddee-32bf-bc58-4645fa03249b | -20.07816 | -43.99842 | 2025-08-03 04:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 261d15fc-f186-3b55-817a-ca944267ea32 | -13.699 | -41.3733 | 2025-08-03 04:55:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3d08190d-9e7e-35f0-b5a2-8b9f2f159973 | -16.72235 | -49.42846 | 2025-08-03 04:55:00 | NPP-375D | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| af2ed4ef-a9bd-3e3a-b842-c1aa63296cd8 | -15.59429 | -48.50743 | 2025-08-03 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6465ba21-3fc4-314f-9366-2b461e6d2fae | -18.23023 | -44.7078 | 2025-08-03 04:55:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c0ccb50-95a3-31cc-9971-34c0ccdc5521 | -19.6253 | -43.17205 | 2025-08-03 04:55:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4e3f2295-a172-3043-b22f-509207387a30 | -13.67234 | -41.3688 | 2025-08-03 04:55:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 653dba18-cdca-3103-98c9-56afd9598bf9 | -16.71823 | -49.4278 | 2025-08-03 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2eea2121-8241-3815-96ba-1f36c3088a61 | -19.62485 | -43.17702 | 2025-08-03 04:55:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9ca283ea-86ab-3722-aab3-ccd87c60634b | -16.704 | -49.39096 | 2025-08-03 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd39fdf6-39f2-325c-96a1-50ff8e66e6f4 | -12.03051 | -54.23791 | 2025-08-03 04:55:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f211e84-d1d2-3ca0-a14f-d40aa9382d5f | -13.679 | -41.36998 | 2025-08-03 04:55:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 684b3df8-c0f3-3d61-b28e-1c7eeec3f888 | -17.21244 | -44.84871 | 2025-08-03 04:55:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 758e0aa5-f41e-3d59-9c11-c733cb7de68f | -13.07076 | -47.44088 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63656554-5e35-338c-bbfc-9b9ac526897a | -14.37546 | -50.32819 | 2025-08-03 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| bb7c10c6-07c0-3958-ad5f-d3852d1e1aa1 | -14.16671 | -45.44292 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8310312-0f62-3bd9-96cb-8737ef149f78 | -18.93164 | -46.79233 | 2025-08-03 04:55:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2f61809-a0cf-3a7f-844f-5c2073596d51 | -20.08445 | -43.99697 | 2025-08-03 04:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8d68197a-1c55-39dc-b4c7-81754d6bc6f3 | -15.59995 | -54.30244 | 2025-08-03 04:55:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deda7174-1ff8-3fc4-aea6-82e72bf5db5c | -12.68758 | -48.09815 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9d612c9-e600-32e2-a4c9-21d78b32ab36 | -18.23067 | -44.70345 | 2025-08-03 04:55:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ab14c67-7a4f-3e47-8b10-73a0d09ea4e0 | -16.13198 | -46.87595 | 2025-08-03 04:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcf9ef03-6075-383b-a055-2f7268fd8107 | -18.92655 | -46.79195 | 2025-08-03 04:55:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f9d9568-8d0c-3610-a295-6bb61a536442 | -15.54637 | -54.27909 | 2025-08-03 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 69cd6e40-0c50-3137-be38-f06d0e0121b9 | -18.83844 | -46.44635 | 2025-08-03 04:55:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bda2cb0a-a25c-35d1-a681-538d50e06c03 | -13.0725 | -47.42776 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)
