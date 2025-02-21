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
| 00ec3fff-d250-3200-8678-931d5b403e1d | -6.8681 | -34.9313 | 2025-02-21 00:00:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 251.7 |
| 3ee92f02-9128-3760-a2fa-e4740391666c | -6.8678 | -34.9589 | 2025-02-21 00:00:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 226.9 |
| 4ebf05e6-b2da-38d9-88cd-386648c8d768 | -6.89 | -34.93 | 2025-02-21 00:00:00 | MSG-03 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9bc20ffe-42a2-360d-a883-17a10b193535 | -17.9461 | -39.8683 | 2025-02-21 00:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 111.4 |
| 53869ce6-2e36-316a-a2bb-0434247534bb | -17.9664 | -39.8626 | 2025-02-21 00:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 125.6 |
| 1a96c899-70c8-3f3f-bbb2-cf2c72ec7c9a | -7.0758 | -35.0968 | 2025-02-21 00:30:00 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 103.5 |
| 9459f4f4-c246-3abc-bbd3-40fa7004abd1 | -7.0949 | -35.0943 | 2025-02-21 00:30:00 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 110.9 |
| b431b2db-762d-31b3-be67-40f165189c25 | -7.0949 | -35.0943 | 2025-02-21 00:40:00 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 198.3 |
| e8207405-6426-3b9a-b5d9-f96631fd8614 | -7.0758 | -35.0968 | 2025-02-21 00:40:00 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 270.9 |
| 8245c92d-df64-3b8f-a0ec-ece31d8699ab | -7.0754 | -35.1243 | 2025-02-21 00:40:00 | GOES-16 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 112.9 |
| 025c94a4-f1fe-359d-a237-3a4b47865f6c | -20.228901 | -44.3559 | 2025-02-21 00:41:00 | METOP-C | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2686b124-5a75-360a-afe6-34d5837c5a84 | -22.9249 | -43.726101 | 2025-02-21 00:41:00 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85b79a65-1522-3158-9fc3-c8dc7d882618 | -15.7403 | -43.1469 | 2025-02-21 00:41:00 | METOP-C | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| db6a58f9-7cb1-3be0-8a55-6b8b154a4a0e | -12.8099 | -45.005798 | 2025-02-21 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc5770eb-5721-30ef-8dad-9d2d6c4c4f2c | -20.466299 | -43.2728 | 2025-02-21 00:41:00 | METOP-C | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d8a7194e-a92f-3e6a-aa58-a139a57efac1 | -6.2204 | -48.0611 | 2025-02-21 00:41:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40a74575-4041-3bd7-bbeb-35c55694d4fa | -20.7255 | -44.270302 | 2025-02-21 00:41:00 | METOP-C | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf42fb60-7ab0-3fec-b64f-69d9ec78a81f | -14.4412 | -45.630001 | 2025-02-21 00:41:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f888369c-2c89-33ee-b26b-a1c94b4ee37d | -17.4688 | -47.008099 | 2025-02-21 00:41:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a29bdf15-8b49-3476-886f-a8a47795981b | -20.3183 | -46.497601 | 2025-02-21 00:41:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| efc1a97c-3da8-35c1-8cb8-ae7eb523f1b3 | -22.924101 | -43.310001 | 2025-02-21 00:41:00 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6f3dec3f-fa77-3665-b8fd-46c94b56bc44 | -20.210699 | -46.522999 | 2025-02-21 00:41:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6ef700e6-4bd0-31f5-9fb7-fa4a07ad2073 | -20.723801 | -44.262901 | 2025-02-21 00:41:00 | METOP-C | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3db68411-bb43-38c1-bf3f-442016cd4703 | -14.4445 | -45.644402 | 2025-02-21 00:41:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b8097f5-daab-30c6-aa8c-ef9509f19437 | -20.212299 | -46.530499 | 2025-02-21 00:41:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 717832de-7054-3f45-825e-679656cc188c | -20.9505 | -42.9977 | 2025-02-21 00:41:00 | METOP-C | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd024a32-1f5a-3b76-a9ab-7f6880cf9fb8 | -20.227301 | -44.348499 | 2025-02-21 00:41:00 | METOP-C | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 903bc080-b297-3d6a-bb72-0a840988bd2b | -20.2139 | -46.537998 | 2025-02-21 00:41:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 57f57e1d-4b94-3423-be6e-72143b6a702f | -12.8081 | -44.998199 | 2025-02-21 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc06a4c2-6680-3375-ad45-9986e4400dc9 | -20.319901 | -46.5051 | 2025-02-21 00:41:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5c4f6c58-b59b-3078-9188-445eb76492f6 | -21.0695 | -43.198799 | 2025-02-21 00:41:00 | METOP-C | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 60ca0c15-43fb-34e3-a3b8-479cba930d62 | -14.4683 | -47.910599 | 2025-02-21 00:41:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 792bca7d-3d1d-3658-b788-9522a6cc87a0 | -17.0625 | -45.044601 | 2025-02-21 00:41:00 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d35555b1-1066-3857-aea1-326ddb355e76 | -11.8627 | -46.941399 | 2025-02-21 00:41:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 948553d9-4cb8-39c3-91ee-60942c63f4de | -17.4704 | -47.0154 | 2025-02-21 00:41:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e84f4167-f399-3961-8338-73082a5d053f | -20.952299 | -43.0056 | 2025-02-21 00:41:00 | METOP-C | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5a79dde1-7f32-307c-810e-1e389495320d | -17.0609 | -45.0373 | 2025-02-21 00:41:00 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 07b573a5-9ecb-354b-bd6a-00b1e5e8937a | -14.4428 | -45.637199 | 2025-02-21 00:41:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a6b90cd-7c71-3b6a-bdd0-7d1e70801629 | -21.06137 | -43.20272 | 2025-02-21 00:47:00 | TERRA_M-M | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 0d6fa64c-600b-3b8d-8086-9b8fa785504b | -20.71174 | -44.27263 | 2025-02-21 00:47:00 | TERRA_M-M | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 09fae9d2-8038-34e7-b3ec-8b8ba8b217c9 | -20.72102 | -44.27115 | 2025-02-21 00:47:00 | TERRA_M-M | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 035d76a4-5167-3fa4-8631-3642c1a638a0 | -22.85009 | -42.7665 | 2025-02-21 00:47:00 | TERRA_M-M | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| e7740590-1333-3dd8-87ec-80905ac2ef02 | -14.43797 | -45.63515 | 2025-02-21 00:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e2ebc11d-a854-3655-b526-09a4765d0f8c | -14.42867 | -45.63663 | 2025-02-21 00:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 598cfb93-905e-3e7b-ab17-80e8e2ba4646 | -14.45197 | -47.91569 | 2025-02-21 00:49:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d8cf1b27-f649-3cde-b589-8e717ffcc34a | -20.4558 | -43.27135 | 2025-02-21 00:49:00 | TERRA_M-M | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| c503facf-a373-3b53-b6b3-3bb9393e84d1 | -20.21567 | -44.35795 | 2025-02-21 00:49:00 | TERRA_M-M | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 2a17a414-9438-3f21-bddf-b4151e2c59be | -20.30469 | -46.49549 | 2025-02-21 00:49:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1440d279-2b4a-3a07-96a3-8263498b6e01 | -20.2004 | -46.5372 | 2025-02-21 00:49:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| da66fce8-09c0-3c1f-86f2-9e80b2334113 | -20.306 | -46.50486 | 2025-02-21 00:49:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ebee5ea1-2bed-3c0c-8fa4-81697c7ad888 | -17.05347 | -45.04044 | 2025-02-21 00:49:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0f57c55b-9275-3117-b08b-8c03ffe42e58 | -20.1991 | -46.52784 | 2025-02-21 00:49:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| eb8ce9f7-9cae-38fe-a094-602b99530c2b | -14.43948 | -45.64531 | 2025-02-21 00:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7139369b-6327-3d90-bacf-b2a2f4e4b4cc | -20.22494 | -44.3563 | 2025-02-21 00:49:00 | TERRA_M-M | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 6f85f592-0ada-3329-b7c4-5d8817f2c777 | -17.45783 | -47.00891 | 2025-02-21 00:49:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fa61a47d-e8b9-3c46-8a1c-7bd7002bde33 | -20.96107 | -48.81331 | 2025-02-21 00:49:00 | TERRA_M-M | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 5ecff116-fd1e-39b7-9229-4665dbb18c52 | -20.1978 | -46.51848 | 2025-02-21 00:49:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 53ee1b2b-4a6c-3bee-810d-45413af2b9b8 | -12.35235 | -47.99084 | 2025-02-21 00:49:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 67920170-d031-31da-843e-8c8657f97414 | -13.19535 | -50.93761 | 2025-02-21 00:49:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f495801-fdf9-3875-b864-7f1b6d5db287 | -12.79539 | -45.00368 | 2025-02-21 00:49:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ad4a0ca2-1cfa-3276-825e-1edda97fe793 | -12.80693 | -45.01338 | 2025-02-21 00:49:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e9ab636a-1b70-3e8d-9646-7d406835cef3 | -14.11229 | -45.6699 | 2025-02-21 00:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a894342c-09b5-39ed-806d-dd25dd0d2eba | -11.86142 | -46.93876 | 2025-02-21 00:49:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7b8eb6d0-0c8d-3f4f-8386-9bbd8fe8e0e7 | -11.85238 | -46.94011 | 2025-02-21 00:49:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6f5d2ffe-fbf4-34a8-9db5-78a96c2246ec | -10.46943 | -49.09494 | 2025-02-21 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d96856ab-500f-365c-9e61-c31a66e22745 | -6.21408 | -48.06646 | 2025-02-21 00:52:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 517f5a0c-63d0-311a-86cf-b4dbc451ac7c | -9.7961 | -64.795898 | 2025-02-21 01:27:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 46e32571-8be5-3886-9475-367917c8d2f9 | -20.4172 | -41.3429 | 2025-02-21 01:50:00 | GOES-16 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| 88f38be0-afc1-33c7-a08a-f9f55da40362 | -20.4164 | -41.3689 | 2025-02-21 01:50:00 | GOES-16 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| bcffb2a9-d4d2-33fb-bb5a-6b5922f57390 | -6.4079 | -35.1529 | 2025-02-21 02:10:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 117.3 |
| 588f3e03-d52d-32c2-bc83-f14f10412c9a | -6.4075 | -35.1803 | 2025-02-21 02:10:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 142.7 |
| d317e83f-37dd-395b-b2a9-17fc60c0ba73 | -18.2019 | -49.5306 | 2025-02-21 02:20:00 | GOES-16 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| f4b29d0f-b2f7-3379-a114-4e33e937cc40 | -6.3888 | -35.1552 | 2025-02-21 02:20:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 122.6 |
| 1fbafcf1-532b-38d0-8e19-053e6cc3ba3b | -6.3885 | -35.1826 | 2025-02-21 02:20:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 121.5 |
| a8306cf4-1507-3f3c-b701-3428a9211b0c | -7.3995 | -35.1631 | 2025-02-21 02:20:00 | GOES-16 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 105.2 |
| fa00d546-5dca-3a1f-a555-902352bf4572 | -9.3982 | -35.56526 | 2025-02-21 02:49:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 30ba11d1-dd82-3d02-bd18-1d8ef9ab073f | -9.39179 | -35.5638 | 2025-02-21 02:49:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 324e159f-6adc-3568-99ff-cac1707f3c0b | -9.18768 | -35.61618 | 2025-02-21 03:42:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2aefa596-4b7f-30fa-b290-126015282bf3 | -7.37395 | -37.42372 | 2025-02-21 03:42:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| de1af419-40f6-3b6b-baff-cc3a794f6d10 | -8.47098 | -35.32482 | 2025-02-21 03:42:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 175c2ccf-3e69-3670-8f96-ae71e0d34d17 | -7.47737 | -34.84456 | 2025-02-21 03:42:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a7d83e20-c170-39ab-96ad-17258f75d3ba | -8.46821 | -35.32083 | 2025-02-21 03:42:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6d91333d-44b7-39c9-a66c-328319c48e58 | -8.67827 | -36.23928 | 2025-02-21 03:42:00 | NOAA-21 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dcd8bd1f-9027-3f4c-a4ca-481127e3ffc3 | -7.26741 | -35.88531 | 2025-02-21 03:42:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e47f4d9d-fdb5-319a-ac0a-af975fbea9f3 | -6.57467 | -37.81094 | 2025-02-21 03:42:00 | NOAA-21 | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 07edfc27-f390-3ee0-bae4-705a0bca15f4 | -8.47152 | -35.32134 | 2025-02-21 03:42:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2dde0d2d-b1b3-36d5-9a94-bb108f7d620d | -7.58657 | -35.41123 | 2025-02-21 03:42:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 14df8c31-ce96-3a48-8f73-79cdc3617141 | -6.46352 | -36.66037 | 2025-02-21 03:42:00 | NOAA-21 | ACARI | RIO GRANDE DO NORTE | Brasil | 2400109 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4679fc80-b1c4-33b4-a160-a051745a5178 | -7.42269 | -35.13074 | 2025-02-21 03:42:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9dce539d-3584-3aa8-a505-a575a92f34cd | -14.43774 | -45.63375 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92951de1-93b8-3439-ab60-31267ba15ece | -14.44073 | -45.82638 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bccaf04e-43d3-3f9a-8127-6754f483df9a | -12.80243 | -45.00875 | 2025-02-21 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cc13aa9-77c1-3dfd-ad2a-064965953f89 | -14.44218 | -45.63775 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1c1f938-0fa8-35d7-9a3a-5c600d76f972 | -11.41388 | -40.62622 | 2025-02-21 03:44:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 45701d4b-846f-34ad-9046-d3169d819f94 | -14.43272 | -45.63276 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9be84b09-6239-39ec-b29f-7b410e39e036 | -12.18147 | -39.45382 | 2025-02-21 03:44:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9b80ec3f-3770-3bbe-bd0d-c4f568b3ddb8 | -12.16065 | -44.18451 | 2025-02-21 03:44:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c4ea9e7-45f5-3f81-89a4-921415c19d6e | -14.4333 | -45.62975 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 264d0eac-eec5-30ec-96c1-b413ccd8dbe7 | -14.42828 | -45.62875 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64ab7efa-8bc9-3763-b450-47b58b742710 | -14.43716 | -45.63675 | 2025-02-21 03:44:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
