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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b7cfc16-60ab-3116-b785-0634b3060bf8 | -11.15889 | -43.31836 | 2025-12-31 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c883450d-042e-3202-a2bf-32b60882aacf | -14.72572 | -53.97066 | 2025-12-31 04:16:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2142b453-c779-3611-a41f-5c55334c99d4 | -14.78727 | -42.12414 | 2025-12-31 04:16:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7143dfea-f231-30a5-b298-2dcb69e1f560 | -9.85453 | -37.63579 | 2025-12-31 04:16:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 385d8d28-49d0-338f-aab4-9ebab097d6d1 | -15.52216 | -43.55021 | 2025-12-31 04:16:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14f9fcee-3c01-3068-b379-4d033b18bec4 | -14.72839 | -53.9724 | 2025-12-31 04:16:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a5ddb459-ed49-3146-b526-b3eae39a280b | -11.15555 | -43.31783 | 2025-12-31 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6e075d9e-941c-3b36-90fd-be12377951a4 | -16.00501 | -46.95766 | 2025-12-31 04:16:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85aa941d-c81e-33c5-8356-eddb32bf679b | -15.91296 | -42.61659 | 2025-12-31 04:16:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 169c0062-aa38-3842-adf2-f337c0ce27a9 | -12.66564 | -46.76149 | 2025-12-31 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49ad706c-650f-3216-a3a5-0b81efc64397 | -9.52816 | -40.33763 | 2025-12-31 04:16:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fe5200fb-a8c6-345b-86ba-8dc8b91901d9 | -14.72064 | -53.96956 | 2025-12-31 04:16:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c98ba122-c620-30ed-b0dc-12078598fc31 | -12.1465 | -37.97639 | 2025-12-31 04:16:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0d172057-6abf-3486-9859-7237348a17db | -14.72511 | -53.9738 | 2025-12-31 04:16:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe2a7e03-a3a1-344b-95cd-ccb41a592a3d | -12.665 | -46.7653 | 2025-12-31 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 179850bd-64e9-34e2-b01a-cc40f92c2034 | -18.66822 | -42.52821 | 2025-12-31 04:18:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9890cfbc-64cd-32cb-85d7-b3725c5e0080 | -17.52232 | -40.62561 | 2025-12-31 04:18:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c492f5af-b5c4-377b-991c-51cc98eafdc9 | -18.79266 | -47.07426 | 2025-12-31 04:18:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58ebc861-4832-3326-8e0f-e486b698acd3 | -17.70381 | -53.27471 | 2025-12-31 04:18:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ee08be5-8cdf-38a6-a417-b1409beec233 | -17.37857 | -42.62151 | 2025-12-31 04:18:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e29b042f-95eb-3293-a72b-24359bb70ca8 | -20.33099 | -55.92663 | 2025-12-31 04:18:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fc2a5d24-a5a2-3777-ad56-16e4af47264e | -17.37796 | -42.62579 | 2025-12-31 04:18:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a8caa62b-e6d4-3106-9ff2-898cf4abeb5d | -21.55122 | -47.14599 | 2025-12-31 04:18:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ead4e73a-726e-3a2f-a448-1abf05b283d7 | -17.38155 | -42.62632 | 2025-12-31 04:18:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 094bb9a3-7b1d-3955-bcb5-fe4212e1043f | -17.88027 | -43.46103 | 2025-12-31 04:18:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23dcafda-bb77-32ca-bfc8-a387d77a88c8 | -22.19437 | -47.0586 | 2025-12-31 04:18:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62070872-e49c-31ac-ba97-acaefa600a77 | -17.37736 | -42.63005 | 2025-12-31 04:18:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 053118fa-937a-331e-8aa8-78064f8103e5 | -21.71398 | -47.10641 | 2025-12-31 04:18:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27bd471c-fed6-3b2b-bbf0-f480bd8c3697 | -17.70341 | -53.27182 | 2025-12-31 04:18:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43fc3c07-c030-3e11-8571-c5aa3364ece0 | -18.98469 | -46.29651 | 2025-12-31 04:18:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc3ea538-2048-3d15-ba8c-08c80de0b454 | -20.32582 | -55.92543 | 2025-12-31 04:18:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b04c15fd-ca95-303f-b66b-7dad294b4c48 | -16.4818 | -50.90985 | 2025-12-31 04:18:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08179505-498c-32cd-a95b-5e9099e39211 | -16.31258 | -57.56293 | 2025-12-31 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 777a6cec-f65f-38f5-a0e2-6ba5f88c931e | -20.3251 | -55.92482 | 2025-12-31 04:18:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2aec647e-23de-3bc5-aa2d-5c45669cab6f | -17.80056 | -42.5698 | 2025-12-31 04:18:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4cd72a33-c30f-343c-9215-cd9a5493b64d | -17.70797 | -53.27292 | 2025-12-31 04:18:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83caebd8-0375-3b67-be45-36f748d8ccef | -16.30641 | -57.56161 | 2025-12-31 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 69a199c9-6c79-3f1e-acb4-2d3c73baafd7 | -18.22239 | -45.05164 | 2025-12-31 04:18:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63133a46-b4e0-304a-8be1-590a87faee9d | -23.37474 | -46.02929 | 2025-12-31 04:21:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f6feadbb-52cc-3f80-96f4-bf75509aedf7 | -31.98288 | -53.00351 | 2025-12-31 04:23:00 | NOAA-21 | PEDRO OSÓRIO | RIO GRANDE DO SUL | Brasil | 4314209 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| fec117b0-212c-3d55-95f8-f96cd4274701 | -29.73575 | -51.081 | 2025-12-31 04:23:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| bd672f05-1c79-35c5-8a71-e54bc003c490 | -29.88572 | -51.21522 | 2025-12-31 04:23:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 291034ac-1642-32a3-91e0-6ae0ea43658a | -33.71897 | -53.37713 | 2025-12-31 04:23:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| a9857bb7-1539-367d-bf36-6894722753aa | -31.9814 | -53.00143 | 2025-12-31 04:23:00 | NOAA-21 | PEDRO OSÓRIO | RIO GRANDE DO SUL | Brasil | 4314209 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 2c827316-faa9-39d2-980b-e3f045feaba3 | -33.71545 | -53.37621 | 2025-12-31 04:23:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 6061fa8c-6606-36c1-bc64-f0e32971ef47 | -33.71633 | -53.37145 | 2025-12-31 04:23:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| c6273d98-af0a-349f-8218-dcee0dae46a9 | -1.62174 | -45.70856 | 2025-12-31 04:42:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d42c4828-d0dc-37e7-84a3-efa8534358ae | -0.93035 | -46.89457 | 2025-12-31 04:42:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36a108ba-909e-3bc6-9b5c-f6f4dca346a6 | -1.07467 | -47.99579 | 2025-12-31 04:42:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c84ddaf7-3e8c-3d39-aac9-30720afa90d2 | -1.15842 | -53.50867 | 2025-12-31 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f7232b7-aa1f-3359-b6a0-7dff5c65e8f6 | -1.07521 | -47.99234 | 2025-12-31 04:42:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9eef729c-f3f9-3218-821e-f55746eb8f02 | -0.8922 | -47.99509 | 2025-12-31 04:42:00 | NPP-375D | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bdbedab-53b6-3e36-bc4c-409e7f5ed2d2 | -1.07576 | -47.98888 | 2025-12-31 04:42:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cab62a44-df9b-3ca2-b01c-09454a6039d5 | -0.94441 | -46.93721 | 2025-12-31 04:42:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bf16557-c270-3684-8ee0-f044e87f1c3d | -1.07854 | -47.99286 | 2025-12-31 04:42:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f403262-8dec-39a0-bafd-8bd7b97cf27b | -0.93431 | -46.8915 | 2025-12-31 04:42:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aef36fc2-82b8-3e52-8a1b-d8e80557f662 | -0.93374 | -46.8951 | 2025-12-31 04:42:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b19bbad7-65ee-396d-80ae-29e6b7e58c3a | -0.94384 | -46.94079 | 2025-12-31 04:42:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aa5ad2d-3fef-3aa9-8406-17fd81835814 | -0.08789 | -51.28008 | 2025-12-31 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 69c16160-82c5-3fc7-b257-7528221a1dc8 | -0.93487 | -46.88791 | 2025-12-31 04:42:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 784e8521-4cfc-3947-ab68-480d33df354e | -1.07799 | -47.99631 | 2025-12-31 04:42:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3289d1f0-3531-31b1-89d5-04e0d07f97b8 | -1.79048 | -45.90017 | 2025-12-31 04:42:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4be984ca-c5cd-3887-82e5-bc77f4be2a5d | -1.79046 | -45.89901 | 2025-12-31 04:42:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54b951db-ebde-3f34-ae76-7416cf3acf56 | -1.59306 | -45.96307 | 2025-12-31 04:42:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d4eb36f0-38ac-3884-8435-8a07171ce6a9 | -0.93092 | -46.89098 | 2025-12-31 04:42:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33085a54-a19d-30a7-ba7e-60e800d24716 | -2.11365 | -47.11987 | 2025-12-31 04:42:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2e821f2-b4c0-3411-87f2-f73e6b3eb24f | -1.08131 | -47.99683 | 2025-12-31 04:42:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c6899da3-b27c-3536-9ad2-9d05f46fb078 | -8.11899 | -47.99221 | 2025-12-31 04:44:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ded70e76-88bf-37d3-8af6-961a455d3f19 | -4.76491 | -37.82454 | 2025-12-31 04:44:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e50344c3-865e-3119-82b1-2e2dd92e34f1 | -5.75302 | -47.95222 | 2025-12-31 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81ca019f-0bc6-3a86-bf59-eea8fb6ef256 | -4.34688 | -44.82997 | 2025-12-31 04:44:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd93b6a8-50b7-3819-a38a-a832fb86ec69 | -4.32094 | -43.78508 | 2025-12-31 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c641d58-8a94-3147-969f-c45e3c282327 | -3.9733 | -46.60216 | 2025-12-31 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f587ddb4-3e2a-3600-9192-593e7cac33f3 | -2.17772 | -48.01913 | 2025-12-31 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2c591681-6399-3a3e-b3ce-13af9271a136 | -5.32571 | -43.56958 | 2025-12-31 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b250c9cc-a24d-35e1-ab04-5dddc0eaa374 | -4.26061 | -48.83889 | 2025-12-31 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a61c49f9-2274-3170-94ce-86ba69c2128c | -3.87253 | -40.45208 | 2025-12-31 04:44:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f2c26834-0fb5-3f2d-b1cb-a6537dca0ea8 | -6.61694 | -43.73953 | 2025-12-31 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96ee1b8a-106f-36c8-a7f7-8fbf16debaf2 | -2.1366 | -47.99848 | 2025-12-31 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1863051-afd7-354e-9de9-0e459187d9db | -2.17717 | -48.02259 | 2025-12-31 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e344a23-b5a3-30ab-80bb-3d1c06ec7e2b | -4.6112 | -45.67478 | 2025-12-31 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db0e4714-45d6-310c-ad8c-473595c435da | -5.98422 | -44.57222 | 2025-12-31 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8604667d-35fa-3000-8f83-6a918effe90a | -4.31212 | -43.78761 | 2025-12-31 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5030c42d-36a6-3919-88b8-c2615eb516dd | -4.31681 | -43.78445 | 2025-12-31 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16539ccf-2eb2-3cca-aa2e-7c07e7bcc126 | -3.53336 | -43.67233 | 2025-12-31 04:44:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9af4f477-6434-3822-8e94-1355b83b6d2b | -3.53165 | -43.66918 | 2025-12-31 04:44:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 205da400-2f74-341f-85bf-e72085f1da92 | -4.30799 | -43.78693 | 2025-12-31 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1b09aa4-9220-3409-baea-36a44506affc | -4.30856 | -43.78313 | 2025-12-31 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e39ca53d-f259-30e8-b1c6-6a277386b08f | -4.77113 | -37.82545 | 2025-12-31 04:44:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7aebba6d-c4be-3a96-8500-9e2596714e10 | -5.0459 | -47.18621 | 2025-12-31 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b1c68fb-9e92-325d-9c89-1e1bd81aa312 | -6.19514 | -44.62543 | 2025-12-31 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf368df4-fef5-3c1e-9cf9-147aae3f0810 | -6.49195 | -39.03604 | 2025-12-31 04:44:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9a11012d-a2c1-3d7c-a920-b59505246362 | -5.72888 | -45.03769 | 2025-12-31 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a35a7508-253f-34b4-8925-a9d106fe6154 | -2.45227 | -47.78288 | 2025-12-31 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c40edd1b-73f1-341d-a185-4c193b2e76e2 | -4.07519 | -42.88363 | 2025-12-31 04:44:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89f01be9-e864-3f0b-8df8-786365ec6ed5 | -3.34205 | -42.15004 | 2025-12-31 04:44:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c344884d-850a-327b-9fdb-ab337a904803 | -3.3466 | -42.15074 | 2025-12-31 04:44:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76d0d131-e4e6-3306-80f2-1a1583523096 | -5.04813 | -47.1867 | 2025-12-31 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b430a5-64e5-31ff-8038-3f7781f7546d | -5.72354 | -45.04688 | 2025-12-31 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 17f474da-1e99-30aa-bd0d-df66eb9de7e9 | -6.33914 | -43.75064 | 2025-12-31 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
