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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44b5c6ca-af0c-3a36-8688-20be2fb1b635 | -15.8872 | -43.46066 | 2024-11-27 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61272299-4331-3f6e-a0c9-383a2f2cebc5 | -9.5173 | -42.99553 | 2024-11-27 03:57:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10a61526-4649-371f-9919-171cfe14ce55 | -10.05601 | -48.0647 | 2024-11-27 03:57:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1f10137-dcaf-3b96-8fa1-ea4fe16f85a2 | -9.17084 | -47.82991 | 2024-11-27 03:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d95c182-6fbe-3a09-b608-9ea2a368c962 | -7.98188 | -49.69217 | 2024-11-27 03:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc94d08d-5f9a-3d39-b030-c98079602145 | -12.02427 | -49.54143 | 2024-11-27 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08d886f1-b12d-3a0f-9105-4518bb34a5fd | -11.73775 | -47.24383 | 2024-11-27 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e2cb918-d079-3ac0-ab1c-32bacfd00106 | -9.17592 | -47.8309 | 2024-11-27 03:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2764fada-db0a-3867-af3e-43ef91f86e7d | -9.12456 | -47.70961 | 2024-11-27 03:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61695c87-a03d-34a1-b5e6-17b2aa2ba1d5 | -15.89422 | -43.4619 | 2024-11-27 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6e8ac80c-fbeb-372c-a8c4-7d859ef74f14 | -12.02832 | -49.54199 | 2024-11-27 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ad7c085e-e0da-316b-8fef-2fab9f62a73f | -15.88933 | -43.46943 | 2024-11-27 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed16d1c0-21ea-3584-9f76-3aa5113eafaf | -10.38068 | -47.50845 | 2024-11-27 03:57:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e7b1c01d-79c1-3f77-bfc1-6bacdf99a716 | -15.88582 | -43.46881 | 2024-11-27 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46c2183c-886a-3d52-b4d5-9dacad9ca1d5 | -12.02967 | -49.54256 | 2024-11-27 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f16f213-b64d-31b6-97cf-7ad05bb5106a | -10.0266 | -36.18196 | 2024-11-27 03:57:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 286f0977-2d3b-302f-9707-bd36d67daf80 | -12.90169 | -48.51497 | 2024-11-27 03:57:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efd8bef2-c67b-3201-8d61-2084715cc04e | -10.75986 | -47.51713 | 2024-11-27 03:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e8b61f2-23a6-3937-bfef-0da16700efba | -15.8914 | -43.45721 | 2024-11-27 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8af9ddb6-6d45-37c6-9be1-31dd59319f2b | -8.39877 | -49.17644 | 2024-11-27 03:57:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95088244-131a-34e4-b9df-3c5838c63822 | -12.03036 | -49.53906 | 2024-11-27 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8aa6b96d-bdde-300d-b5ab-fb054481402c | -8.40251 | -49.17279 | 2024-11-27 03:57:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcb9b2ab-a62a-39a8-ae8d-324714488897 | -10.53247 | -49.05131 | 2024-11-27 03:57:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e258ea7e-fd0b-3b26-bb3d-e17652c48e6c | -7.98679 | -49.69137 | 2024-11-27 03:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 697b64fc-1c49-3f9b-a134-745307640903 | -11.73307 | -47.24297 | 2024-11-27 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6682c882-3735-3247-a710-68ac74febaff | -17.55242 | -46.54433 | 2024-11-27 03:59:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 697b3f8e-da25-3d16-b3ab-9f684ba46d7b | -20.89627 | -48.9598 | 2024-11-27 03:59:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8ac6df32-f1d1-3242-8805-ee734d7d6c4f | -16.68009 | -43.88411 | 2024-11-27 03:59:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1993e31d-8030-3923-bbf6-dd6630e4ea58 | -16.2079 | -45.86785 | 2024-11-27 03:59:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dc151e8-5860-3a0e-a629-2681c671b278 | -21.49409 | -46.02741 | 2024-11-27 03:59:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6c2c7801-6f3e-3933-989a-aff8b140469c | -21.21664 | -48.64988 | 2024-11-27 03:59:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f645d701-9c53-3519-9ee4-9251c03b83a8 | -21.53541 | -45.31038 | 2024-11-27 03:59:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 253560ed-045c-3cc0-9884-49be97370b5f | -17.77863 | -42.80842 | 2024-11-27 03:59:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 591ca5b4-3204-3af6-aa26-c27a8b9d2bcc | -17.75417 | -42.89387 | 2024-11-27 03:59:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b66cdce1-16d9-3c9a-a34d-4d7bbfa59e6b | -19.60414 | -40.057 | 2024-11-27 03:59:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 41e8ad5e-8f01-3d34-aabd-3becade21230 | -20.52207 | -47.33273 | 2024-11-27 03:59:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69ace33a-6c8c-3cdc-8482-bcb2140babd9 | -21.44369 | -48.69862 | 2024-11-27 03:59:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44620068-12ab-359b-90b3-dc2bea0fd93d | -18.01123 | -54.00697 | 2024-11-27 03:59:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a69c7e3-f6a5-350a-9c66-04107724718c | -16.70312 | -46.07601 | 2024-11-27 03:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bf25b594-59a3-3899-a60d-c4a50732a221 | -18.71002 | -47.47929 | 2024-11-27 03:59:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4db7fa47-6ef5-3127-9f57-bd6b3ad9d2c4 | -20.38479 | -47.47913 | 2024-11-27 03:59:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a651c0a9-4507-33c5-8539-364226052ee4 | -19.51602 | -44.64708 | 2024-11-27 03:59:00 | NOAA-21 | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50438a5f-7b7d-3ecc-ba10-367789d9f81c | -19.51398 | -44.27667 | 2024-11-27 03:59:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e97a4d5f-d8cf-3c89-b9dc-c7fc3a4ec0ce | -20.96769 | -42.91525 | 2024-11-27 03:59:00 | NOAA-21 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d8c476e9-7b4b-3e19-aad4-9a5f4a018920 | -19.17487 | -40.14042 | 2024-11-27 03:59:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 63cda9eb-77ef-3098-8dad-e64af6636d7b | -18.19336 | -40.32704 | 2024-11-27 03:59:00 | NOAA-21 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f37fa172-7852-357d-a74a-35a4cd4424d6 | -18.01221 | -54.00932 | 2024-11-27 03:59:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0cca12b3-e901-3a64-ae7d-f1da1bc0fa17 | -16.2333 | -46.50726 | 2024-11-27 03:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14dd1e3d-7122-3feb-9cd8-b3ae4a9d2826 | -19.4383 | -44.33923 | 2024-11-27 03:59:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9eef810-da43-3144-a9bb-ca3d28afd6c7 | -20.90226 | -43.82009 | 2024-11-27 03:59:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 82402f39-369e-3778-963e-789d1f629316 | -20.66874 | -47.42362 | 2024-11-27 03:59:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5a6516e-cd64-3e23-a3ed-4de51fdd7356 | -17.73611 | -39.5228 | 2024-11-27 03:59:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 301cecd5-1746-34cc-8f21-4c4ff20e334c | -21.94109 | -42.27156 | 2024-11-27 03:59:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a395fe61-46f8-32af-8f0f-e1e282596bf4 | -20.85571 | -49.87326 | 2024-11-27 03:59:00 | NOAA-21 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3fd37e45-7517-3a81-9674-33742e49cb1f | -19.76961 | -48.93577 | 2024-11-27 03:59:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad2d1c6f-7c2b-372e-b7c9-fc5ba5bcf1c5 | -17.22909 | -54.43796 | 2024-11-27 03:59:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf8c43e7-0148-3a82-8ee1-7ed2c4ec3a05 | -17.37849 | -42.48397 | 2024-11-27 03:59:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c82f44a7-eab3-3110-b80d-4de04cda901c | -18.27374 | -48.21941 | 2024-11-27 03:59:00 | NOAA-21 | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad5b7941-784f-32cb-8687-73dc2564852c | -19.33457 | -41.34924 | 2024-11-27 03:59:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b3dbe387-5852-3e96-911f-0a2f294cd532 | -18.01756 | -54.00852 | 2024-11-27 03:59:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3c709d7-0faf-3c0f-8357-3de6fe8c54cf | -20.9966 | -51.79155 | 2024-11-27 03:59:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 81f04c1d-fe53-31b8-8ad8-cbcc1c403418 | -19.85016 | -43.84354 | 2024-11-27 03:59:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e9951010-1b69-33c3-864f-918a851c63ed | -22.7875 | -43.75906 | 2024-11-27 03:59:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 66736cfd-7c41-3911-850c-643fe60c0407 | -20.97796 | -47.21383 | 2024-11-27 03:59:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 588996f5-76ae-3a4c-8ed8-f2527bea462f | -16.84106 | -46.66806 | 2024-11-27 03:59:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d7cc8706-8298-3354-939e-109053bc14e5 | -20.97869 | -47.20998 | 2024-11-27 03:59:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b47fb243-20c8-3f1e-abdc-d4fd5ecec4a5 | -18.62033 | -44.54441 | 2024-11-27 03:59:00 | NOAA-21 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1d0d256-7fb8-383e-9d4b-7023f5fd894c | -21.00037 | -45.43619 | 2024-11-27 03:59:00 | NOAA-21 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe4b884e-4e89-385b-b350-5cb79444b334 | -17.22779 | -54.44371 | 2024-11-27 03:59:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c4cfbee-f8a9-31c1-a7a6-65f5c0a2656f | -20.38554 | -47.4752 | 2024-11-27 03:59:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f3d3c26-59f1-3b79-8afd-b7015e159458 | -20.90842 | -47.39972 | 2024-11-27 03:59:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 111ab650-c592-396f-a74b-9083c894ae7a | -19.60809 | -40.05373 | 2024-11-27 03:59:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 09e30eb7-fc3d-3aa7-9b46-e74485e364d1 | -21.44469 | -48.70175 | 2024-11-27 03:59:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3836c85e-5045-327f-81a5-e2e1b78ec6e2 | -19.6047 | -40.05318 | 2024-11-27 03:59:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7e07324d-30c3-3e4e-9c95-d4fe64cbfe82 | -19.20815 | -45.37588 | 2024-11-27 03:59:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a628664c-93a0-3a95-b95b-f841a064364b | -17.28995 | -46.27947 | 2024-11-27 03:59:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a8c3643-1fe9-305e-a552-dbbebe7b618f | -20.76653 | -46.76747 | 2024-11-27 03:59:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1b415ba7-8e9d-305f-b619-913eecf60bbe | -20.37358 | -47.11617 | 2024-11-27 03:59:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90cbdb9b-dc5b-3ea6-8d9b-01b98884af65 | -16.83586 | -42.51343 | 2024-11-27 03:59:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41fba60e-5afb-3063-a745-a59cdc0e0fb4 | -20.77305 | -47.16314 | 2024-11-27 03:59:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87c6d01b-2abf-33d7-8cc3-123a50585aac | -20.38885 | -47.48004 | 2024-11-27 03:59:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| caff5a83-3433-354f-854b-c60a36e01401 | -21.62654 | -43.46559 | 2024-11-27 03:59:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 16996b8b-18fb-3848-98de-3ce4edd2ea65 | -18.0135 | -54.00373 | 2024-11-27 03:59:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f109f71-8717-3460-b087-b850ad4e9582 | -21.06101 | -41.81061 | 2024-11-27 03:59:00 | NOAA-21 | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 37287bbc-81c1-34a9-917d-95c5610c6a8f | -21.448 | -48.69951 | 2024-11-27 03:59:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa328fbd-f4ca-31a5-836b-36d04ed7f187 | -20.90911 | -47.39605 | 2024-11-27 03:59:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ca9d4de-775e-3e07-82e5-c4dce53b082f | -4.23 | -50.8774 | 2024-11-27 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ba60e6c6-ef7c-35f8-ba1d-daf0b98a419c | -3.1691 | -48.4394 | 2024-11-27 04:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 2441c0b6-9407-34e7-8230-2dde47e24d75 | -3.9674 | -48.0851 | 2024-11-27 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| de77e2ee-4b02-30bb-9534-cc782cb8a422 | -2.8347 | -54.1125 | 2024-11-27 04:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 5abf4b8c-4159-3c5e-ab58-8969508ff5ae | -3.1876 | -48.4387 | 2024-11-27 04:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0fd27e5e-8250-3cb8-a6b3-5afbdbbf0f15 | -4.2299 | -50.8983 | 2024-11-27 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2f90653f-a5d7-3c0e-bdd3-0ea738ea85dd | -5.9788 | -45.3621 | 2024-11-27 04:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 485ae0d3-42d8-39f2-acf4-57ce7cf01dbe | -3.1692 | -48.4179 | 2024-11-27 04:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 5ece6386-76af-311c-a545-fe1a800e2d48 | -3.0948 | -53.2791 | 2024-11-27 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 94171e8c-b811-38be-b74a-36b83001944f | -22.9841 | -50.4019 | 2024-11-27 04:00:00 | GOES-16 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 69.7 |
| ec673bf1-5fe0-3827-bbad-d70c3758ca41 | -4.2115 | -50.8782 | 2024-11-27 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 2d4147d6-1d1b-39b5-b986-ac001bb680a3 | -3.1133 | -53.2381 | 2024-11-27 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f7fbaa1a-5311-3f32-a7b4-66398e8aea21 | -3.0949 | -53.2385 | 2024-11-27 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 95e03c8a-45c8-39c9-a304-b4f33463860e | -4.2114 | -50.899 | 2024-11-27 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |


[Clique aqui para ver as próximas entradas](README31.md)
