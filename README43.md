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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40f02bc6-d175-3f34-b0dd-da6346be2943 | -16.41413 | -45.68826 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 116e9e09-cdb3-388f-b1cd-718b08889b92 | -18.05742 | -45.45059 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1473d82-d903-3beb-96d8-b01192731a7d | -16.19716 | -47.86443 | 2025-09-12 04:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e536d840-0012-39a7-a21b-740536c8374f | -11.91926 | -50.71392 | 2025-09-12 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c49b7419-96fe-3668-8e6d-a6a2c6dfd554 | -12.9316 | -47.97992 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bdea229-fdcc-3e12-958d-da50f344ed8c | -14.43759 | -48.42879 | 2025-09-12 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0cc135d9-d5ed-3cf9-8dc5-1714319b6621 | -15.23315 | -44.03612 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8759718-05cf-3150-b701-a4abf1796e66 | -12.99125 | -44.68318 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce11c0a7-901c-3973-ab9f-b68d727da437 | -13.92098 | -47.97559 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 099161df-e094-3248-bad2-7d83fc7dc5ab | -17.94078 | -46.92562 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9c66add-efe2-33b5-bc68-34d06fc517fd | -11.48009 | -49.27479 | 2025-09-12 04:06:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f68c163-0462-3dab-8aa6-d48944f41870 | -15.65674 | -47.04898 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9db9b75-2b5f-3ded-801a-d4d6634ef059 | -11.95427 | -51.17725 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fcc35ece-01b8-34ee-b8f1-0c4ba7e07dd2 | -15.14973 | -52.4712 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1ff5d30a-df43-3ac2-9eee-ee66f278493f | -14.56477 | -48.75737 | 2025-09-12 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29af13e8-a610-3c6f-b00a-51ac762d3252 | -16.66547 | -47.6263 | 2025-09-12 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49ed10fa-6769-3e81-99c4-3d8538e163ee | -15.2284 | -44.04327 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 077cc6d6-365a-3fcd-8f66-15eaf332015b | -18.08371 | -45.42572 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58356744-ea32-3166-9125-3004cb6f5723 | -13.50584 | -40.55956 | 2025-09-12 04:06:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 759cddea-0a7a-325c-908e-31b52775a2cb | -14.40812 | -52.93028 | 2025-09-12 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44269132-421b-3745-8620-f82a4ddd4a06 | -14.42244 | -46.40509 | 2025-09-12 04:06:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ed6df7c-faed-3e58-9b6c-faa54e28d9b8 | -17.91468 | -45.70935 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 81262e59-23d2-3215-b323-44f4267147f0 | -13.35506 | -41.92801 | 2025-09-12 04:06:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 598a0a96-56f7-399d-85a6-c90e3df556c2 | -15.13116 | -48.60171 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2dbf078-5108-3d15-b079-e34e52756ed6 | -16.41778 | -45.68896 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cec9ce9-d207-3604-b530-6a59e4c98fdc | -11.18323 | -55.06693 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e23241b8-2a5e-31aa-820b-0e18a4ec8e12 | -11.52674 | -50.39853 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 9b8f61ce-e022-3e3c-a1d5-625db5b8203b | -14.43117 | -46.4015 | 2025-09-12 04:06:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e071f16d-69e0-3547-8665-ac328095f065 | -11.97413 | -46.65361 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52b3c5d0-2835-3701-9547-a65d980a52ef | -17.21489 | -48.69298 | 2025-09-12 04:06:00 | NPP-375D | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4faa133c-7581-344f-b210-ab328e9aed65 | -13.78172 | -46.29038 | 2025-09-12 04:06:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 43c7b33f-ce5a-35fd-8a7d-1f8d04e27e68 | -17.23995 | -46.75696 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a3729af-26f8-3705-9f02-d1571bba7dae | -11.86038 | -46.76274 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e67d154-abaf-3e4d-ba3c-3a6815a8d2c5 | -17.75565 | -44.4434 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7d7b276-d898-31ee-aac4-29ad1642b193 | -14.18509 | -46.20755 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6a998959-4bc4-3876-9125-0f29b2438f24 | -11.48117 | -49.26896 | 2025-09-12 04:06:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89aedd3b-8301-3cfd-bd55-96b37b112555 | -13.92118 | -47.95107 | 2025-09-12 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8be620de-e53b-356f-b0a8-170b296fdf29 | -11.78764 | -50.56759 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 990b69fe-6f53-340e-b64c-95d08249b9ef | -17.75435 | -44.45121 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d891e6c-35e7-3231-9b54-28b2d30c2541 | -11.69633 | -50.60031 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ee9ab1c-37d1-3c4e-bf41-dd82a020f4c9 | -14.14795 | -44.45332 | 2025-09-12 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03c12361-2b59-3ae6-bdc3-5b7f6fa25d47 | -15.24632 | -44.04245 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00f0a441-f3e4-33bb-920d-1f26d3cb5982 | -17.95046 | -46.9378 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e97436b4-47b6-30df-8fa9-75d249e54052 | -13.2444 | -43.77275 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36298759-47a1-3a1a-874b-1694c8b4f588 | -15.4905 | -47.34602 | 2025-09-12 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4351bc1e-ce2c-341b-a6fe-6bb999e7061a | -12.92718 | -47.97904 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40d65583-fd95-333c-9e7d-e2c62c780d9a | -17.50196 | -44.32693 | 2025-09-12 04:06:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 860a8b03-80f7-36c4-9137-a26bf9491608 | -14.37825 | -47.28955 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35d3b018-6d47-3df0-bdec-56d25266648a | -15.88133 | -48.18924 | 2025-09-12 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f1f51677-b60c-35d1-919b-e15c568d8c83 | -16.08145 | -49.32434 | 2025-09-12 04:06:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7af7a301-0834-3559-8ab0-9d5e4c2ff2a7 | -11.69927 | -48.28682 | 2025-09-12 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f69e4f9f-1fe6-3ab8-9dfc-873828765201 | -14.33185 | -54.12651 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 543906fc-9b72-3c49-958d-b2c087a687bc | -11.99352 | -47.5663 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7062be49-6b0a-3800-a194-afda2350d819 | -18.7025 | -42.83604 | 2025-09-12 04:06:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 991a483d-f26f-34ea-829e-4301d8b01592 | -16.4149 | -45.68384 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14d3f4a2-0b0f-3f55-9d80-ef0a27febeea | -11.85763 | -46.75419 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acb73a8b-1edf-334c-921d-bc33ab21357f | -18.01955 | -46.86042 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b18441ae-0a89-3730-9208-c74cade75508 | -12.00044 | -47.76911 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd9ef7e2-0045-34bb-adaf-933211eef61f | -15.83288 | -42.59494 | 2025-09-12 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b4fa57e5-58d3-3f9c-912d-a7547d213401 | -14.415 | -47.32277 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6c879ae-d585-3033-adc6-c3cd29aef515 | -14.41991 | -46.40203 | 2025-09-12 04:06:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2fb6d5b8-b4d4-321b-9faf-69e248e66591 | -15.12512 | -48.60926 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65379fbd-050a-3fb1-b495-e894fd6f45ce | -12.08199 | -47.59852 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f1f046a-b337-3297-b97b-a1d4f6231b23 | -17.54707 | -44.54346 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52873a1e-42f3-345d-8cd0-0d1b954ce4f0 | -12.86534 | -47.95024 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7cd85899-02be-3b3a-b982-352d95d72ffa | -12.90023 | -47.96 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31390eb7-fbc9-3bf6-bdf0-76d945b2ab46 | -16.84427 | -47.8375 | 2025-09-12 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6810863-90b4-38df-9d67-58e386163af6 | -15.55793 | -41.79357 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b0ba4d1b-b329-36fe-b263-3621ef2cbcef | -16.49417 | -51.9673 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3d6868f-70f6-3b1f-bdbe-79eca72216b5 | -12.88907 | -47.97086 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4bc69f8-ab8a-30c8-96d3-e1b7f068cb8e | -17.55654 | -44.56008 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a2372c1-3404-356c-b49f-a2fc445d3d9a | -11.52806 | -50.39175 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| aa541181-a89e-30a4-877b-d8aff61613b6 | -13.17718 | -47.2696 | 2025-09-12 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 495c88d7-104a-3ed4-837c-db871a69b3ce | -15.11538 | -48.61199 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52b1d51d-87ef-37de-a9bc-086a147decda | -17.47672 | -43.72253 | 2025-09-12 04:06:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fc221f0-b3a5-39a5-8b50-abcae8b47c13 | -11.52243 | -50.59417 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c6de1b5-7608-332a-b656-282033e6b4df | -14.26918 | -54.78014 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55f6fac3-4746-33a1-8fd8-52b30be3da43 | -12.8333 | -47.96188 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19531141-4234-3d11-8ddf-5663519fd5c2 | -11.51634 | -50.38298 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4e3eab9a-ca56-3002-a72a-fc7d9f97e968 | -14.65316 | -42.21264 | 2025-09-12 04:06:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d53c0db6-ab03-3159-a277-0efba9fd082f | -12.50441 | -47.43547 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62c56b6f-1a43-3b5f-bd1f-31c82e376e60 | -11.22317 | -54.89326 | 2025-09-12 04:06:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 15cb4edf-5059-34ea-b1d1-934849b31717 | -15.92055 | -51.7945 | 2025-09-12 04:06:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6f28c8f-779d-3a6c-bae1-ea217d1af94b | -11.19739 | -55.08274 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32cf5e85-484f-3b09-894d-f057f2d70805 | -13.92018 | -47.97982 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f9791db-89ba-3b07-9a53-588911324f91 | -13.90914 | -48.23414 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 772f3807-48b3-3c5f-8599-004ded49bdfe | -17.8211 | -46.73748 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72024cce-2838-34d2-998a-5f8deb63d473 | -17.90613 | -44.60635 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 981208d9-813f-3a19-9fa8-e6cd298b6a8c | -12.45566 | -47.50242 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26c8d6a2-de6f-361e-a15e-73244f3cf448 | -15.79669 | -52.23134 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3399d062-ff68-311c-9514-3fe6532131ff | -15.5292 | -48.55502 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d3758157-99b6-36b8-9b4d-9a2ffd61001e | -17.96479 | -44.46777 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77153523-af84-3b60-9e01-80964143bf58 | -12.08718 | -47.59487 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d39d8b7a-dc2d-3c73-8a17-c0b2971b4a6d | -13.36344 | -41.91838 | 2025-09-12 04:06:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ec5f9c5-a9da-32dc-956e-01fe7622af6e | -14.50327 | -53.91978 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 16576433-9ee3-340e-a8ff-fdb79939851d | -15.53249 | -48.55449 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13c0d0d7-addd-3104-92c1-5864eb731c9c | -15.57998 | -54.76067 | 2025-09-12 04:06:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9f5cdb0-e608-37d1-8213-d1eafcedcf37 | -15.66354 | -47.03419 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c94b18e1-629f-3df4-9762-cc4dcf84563c | -16.41856 | -45.68452 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dd4209b-b456-3330-9607-0bd415309b03 | -16.42428 | -49.04444 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README44.md)
