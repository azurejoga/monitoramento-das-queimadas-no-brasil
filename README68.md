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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b836e12b-539f-3e81-ae1d-ee361d898f41 | -15.39514 | -48.00646 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0505188-1912-3f67-a95c-28e52a44e8e9 | -14.74153 | -46.03693 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| b215e23b-dffd-324b-9ab8-39b2885f708a | -18.44629 | -42.61369 | 2025-10-07 04:38:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cac546d1-d2e8-34f8-80bb-4ac2a7453ec6 | -13.04681 | -49.15703 | 2025-10-07 04:38:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e85a6ac4-2914-3ed3-b814-fcd769caa1c9 | -11.38853 | -43.49554 | 2025-10-07 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dfd8c7c-e1f8-3b63-ad2c-ccd2af746ced | -11.02323 | -51.15648 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 96f351a9-423a-3cd2-ad2e-5f93e879c4f0 | -14.77191 | -46.06506 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| c4102d9c-747f-3417-907a-31b7401adaf6 | -18.51685 | -43.90943 | 2025-10-07 04:38:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2338323-c7df-395a-b054-11f192fd8d7b | -11.11847 | -47.21846 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83a3315a-bdbf-3ecf-9ca1-14503c3ba114 | -12.02126 | -47.78727 | 2025-10-07 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48cd0fa2-370f-3865-9e8e-4b11141b7540 | -11.84767 | -44.91722 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9f36b89-2c09-3c95-a220-d831a96655c4 | -10.92988 | -51.1535 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51cf3e7c-c5d7-3ffa-bbe8-1c382dcff584 | -9.1432 | -61.23495 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be3185f1-f12b-3556-a3d4-2689f1938e5f | -12.94588 | -46.81175 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81cd07c3-bb66-3215-a85e-20c5aa8406e6 | -15.02257 | -47.55295 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56ddf31d-12c1-3839-a14b-699c2ce5cf29 | -11.15007 | -54.8802 | 2025-10-07 04:38:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86b660b7-0648-39ab-b2f5-70bb68e51be4 | -10.38319 | -50.29303 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b7a18704-8845-3961-9fcd-3eb0d3bcf1ea | -12.58234 | -48.10931 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c216c83-94ac-3456-a39c-782666f37f12 | -14.77451 | -46.04676 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 798f0ec9-0690-3af3-9bb4-99ae1be59c67 | -13.34045 | -47.56839 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 180f0765-8112-3685-a7ae-78d57f542897 | -10.61375 | -48.67107 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1bfe9a4-a690-3b45-8b02-45a44e2f9265 | -14.96616 | -49.95665 | 2025-10-07 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02e0ce06-da80-397d-aa49-e64eef53f804 | -10.42931 | -50.33081 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4180eefd-5542-3829-897c-c6578d952841 | -13.26731 | -47.57235 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ece78ad-6446-3e7a-bbaf-37683b87416e | -16.36755 | -51.45523 | 2025-10-07 04:38:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a1d87a5-393d-3c24-b29a-67ed3a4c8186 | -10.33249 | -51.22816 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e8584d6-c8c1-3ecd-996d-c37232abbdbf | -14.63065 | -52.50133 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85b24294-16df-3adb-8ac8-aa07d4d9fe17 | -16.34481 | -47.06109 | 2025-10-07 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d2c0383-bc95-38ce-975a-819d19a41be8 | -13.33813 | -47.76985 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 209dac89-34e9-383e-8aab-a5f9c4d7e23f | -11.26342 | -47.77489 | 2025-10-07 04:38:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b141c3ef-e406-3e06-8f3b-5761052a1793 | -13.23944 | -47.23745 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7cb7b1b-a590-32f4-96c4-296eb74c6100 | -15.50554 | -46.82795 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 059e31d4-1ab7-3ae6-8c32-adb7dcb70928 | -13.09765 | -47.99873 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48530b07-e699-3430-b01b-cde8d64acab6 | -13.25319 | -47.16817 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c2eefd4-6eea-3b24-84e6-9ea2ac3e882b | -15.38826 | -48.0053 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ca9b08c-18e6-39f0-baff-73dfc3f73df5 | -17.25065 | -46.93304 | 2025-10-07 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 722be342-c965-3ca1-8296-b932cfd18a03 | -10.39896 | -50.30317 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d1f5e420-89a4-398e-a280-5253a5be07a5 | -14.92006 | -46.87156 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 086b69a0-2615-3d24-ba49-4b6c74f31e45 | -10.42371 | -50.32234 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 76d36753-3194-3986-bc2d-e721343d9f2f | -13.58031 | -51.80489 | 2025-10-07 04:38:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b3a6a4c-99e8-3657-99e0-57b965ba8310 | -13.30941 | -48.04988 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aef62909-43a3-3d73-b082-0f53f7c6f8dd | -11.15771 | -47.75842 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bbec7f6-eb8b-3661-9da6-b9a0d453001c | -12.2375 | -47.85446 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8cf2913-8ac6-3d22-ba1c-b37377668884 | -13.27873 | -47.16438 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82e50c2a-9a77-3386-9c25-159305c433f7 | -10.74759 | -50.47731 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7794c1e4-6f18-3aa5-a83a-04edf425c562 | -14.76588 | -46.0268 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 666acd3f-78b6-326a-9ea7-45a9be10bb99 | -11.71579 | -45.44 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef9b5cfc-cb27-3898-a7db-0d0f731808cb | -12.93885 | -46.78615 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ecb8ce3-2e51-3b50-a256-2a6fe88dc6b3 | -14.90872 | -46.86651 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 523bf2be-a485-3ccf-be21-e6f3c5fcff39 | -11.00471 | -52.31286 | 2025-10-07 04:38:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd66ec7d-4f83-3b3d-86f7-c3feb661a2dc | -11.03433 | -50.91898 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e6d064e9-f828-3661-9115-293bcbfa53d6 | -12.91453 | -54.72786 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73390fb8-3e5d-333b-ac54-23300e9aab06 | -11.1536 | -54.88496 | 2025-10-07 04:38:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6e1bacc-5651-3238-b62d-df2c61520a18 | -14.93072 | -51.41331 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2a07f4e-78e0-39b0-8aba-12da7b524324 | -13.74287 | -48.65682 | 2025-10-07 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df9fd82b-c332-3a8a-8273-1d1e5bdb11c6 | -14.73469 | -46.03127 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4538eaad-9698-3273-b669-b2dc997ccac6 | -12.40724 | -51.14138 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60fddc04-4d57-3122-850f-19ac916c79b3 | -10.4439 | -50.34832 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5911869-35dd-3648-afe7-b52e007a3b39 | -11.74334 | -43.29519 | 2025-10-07 04:38:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 93c5e162-e33c-3241-aefc-42cf5e062d4f | -18.57078 | -44.18582 | 2025-10-07 04:38:00 | NPP-375D | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcf358b2-9dee-3eef-9609-f8ad7694b58d | -11.29495 | -48.26856 | 2025-10-07 04:38:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41b0f8d4-dd84-390e-9be7-ece000589b37 | -14.92595 | -46.80443 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 06f65aa2-6798-34a6-8c42-d473e58e7013 | -17.53081 | -44.31738 | 2025-10-07 04:38:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7a13024-4fd6-3118-aa6f-5f5bdc81f6e6 | -13.29076 | -48.05833 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 486f8a65-b34d-3a3c-bfa9-8900fa4d5f3f | -14.75157 | -46.01983 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16e9cd08-1e1a-34c8-b29f-f1a9138f0d3e | -10.84935 | -47.17752 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 785af0ae-f0e5-367a-b9c4-b0ec1de0bcf5 | -12.23128 | -47.8498 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 783bfad2-41b7-39af-a806-1636a0acf77b | -15.44314 | -49.10159 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7dd2b53-9011-3dcd-b12d-59933b715ae8 | -13.51735 | -48.62807 | 2025-10-07 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0026380-3458-3588-a5a3-4d44956ada48 | -15.91293 | -48.82791 | 2025-10-07 04:38:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab0577a7-1d43-3d9f-893c-83edafb8462f | -16.05897 | -50.98739 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 541f165a-c5e6-341c-a7ad-464d9e66586c | -13.39245 | -47.59687 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 466c16cd-282e-3b24-be21-0f3e332e55ed | -12.37269 | -46.49811 | 2025-10-07 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecd8ce4d-8fed-338f-934e-47361e160eb6 | -13.35535 | -47.56294 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e78ab50f-f019-3e04-ba21-c236be38c802 | -11.21311 | -54.98297 | 2025-10-07 04:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c049ef5-1a9d-3d2f-a5e4-9292010ebdc2 | -11.15794 | -47.95794 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f19bdc0-7615-3b4b-b9c9-53f7d17e93bb | -13.27596 | -48.47893 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a80ce641-2fcd-3423-8177-f91752a9c26f | -13.1357 | -47.79543 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 385d3cea-bc88-3106-983a-b0fc24eb4088 | -15.59808 | -52.56895 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b84fd115-c4ce-3855-8342-ce0ee4802bb9 | -13.36564 | -47.56479 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36b8a6fe-0234-3d66-a12e-6ebc4c61490f | -14.75338 | -46.03417 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdc84351-93a9-371a-afbb-960765de5c46 | -13.05855 | -48.70962 | 2025-10-07 04:38:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44eb1742-a2f6-3b51-835f-3a0754a725a2 | -10.73536 | -49.2924 | 2025-10-07 04:38:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0bd0066-ccab-3859-93d5-09dc47f57ba4 | -14.73532 | -46.02674 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4056bf1c-5eb9-3673-89ad-c477b7258b03 | -15.3894 | -47.99757 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1c7680a-5a53-3b90-a882-a108053e3230 | -13.09082 | -47.86097 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93bf675f-d8f5-37cc-b2b4-032af615ac75 | -12.90778 | -54.74187 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02af8141-9935-373e-b24d-fdb52f6f60a7 | -15.27375 | -46.34557 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 54de1d41-fcf5-32bf-adb4-4c9239399b7a | -13.67129 | -44.05929 | 2025-10-07 04:38:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9baeccc-fad9-3335-8ce0-5bc223d73b6f | -10.45409 | -50.35002 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2b2f24fe-7499-3952-9d08-54c71caf8df6 | -15.6177 | -52.55975 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce3e0a55-6c0f-3f26-bb24-7eaf90547fe7 | -15.22607 | -56.77693 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e246273-de9e-3293-899c-e5ddf545b7a7 | -11.03776 | -50.91956 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| bc549681-893b-3b1d-a4b2-116f0f20bf60 | -14.76523 | -46.03137 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e47f0f0-63c9-3c3d-8621-712905419535 | -15.96889 | -50.83408 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc0d14c0-2db3-3743-82a9-59c172973c78 | -14.92218 | -46.80009 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c9eaede-baf6-3ec0-8012-4f2acad83327 | -12.37037 | -46.49926 | 2025-10-07 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 422e8c40-84ee-3a2d-8b96-77f3b1ff3e9b | -18.27512 | -45.46466 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec4c052b-4014-3606-aaa4-bd362226f7fe | -13.57658 | -48.15155 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06ae9425-755e-3f09-9b3c-e209746fa0c1 | -11.15574 | -54.873 | 2025-10-07 04:38:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README69.md)
