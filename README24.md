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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d44da7c-0eb1-3c06-8481-ec6b18574085 | -17.72602 | -46.7874 | 2025-09-18 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd632563-fd5b-3f06-9a4c-bfd4a4552211 | -16.72536 | -48.48254 | 2025-09-18 04:17:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8490692-1210-325a-a8b2-c5d0e1509f82 | -15.83482 | -42.7125 | 2025-09-18 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b1dc9e51-3f38-3b61-bbf4-99be6bc49515 | -21.11331 | -49.12727 | 2025-09-18 04:17:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cce53ad2-0dab-3109-af82-7636bb7e1e98 | -17.87633 | -39.83679 | 2025-09-18 04:17:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e22a2bde-0c88-37f6-8226-48e2722c2a51 | -15.75377 | -48.28424 | 2025-09-18 04:17:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c19d782-fe4a-31e2-b20c-42f4bf56d165 | -26.83357 | -52.422 | 2025-09-18 04:17:00 | NOAA-20 | XANXERÊ | SANTA CATARINA | Brasil | 4219507 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7d13271a-41fa-3f4b-b8b8-1efbdb185242 | -21.30174 | -48.55783 | 2025-09-18 04:17:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c0c56e9-3233-3068-a100-0bf8b12b1672 | -18.53999 | -46.05426 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a3d6f07-ed8b-3063-9952-c930005e00de | -16.03176 | -45.16512 | 2025-09-18 04:17:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3c2c4f2-60b1-3fd3-8cc7-90545b61f3c3 | -15.4938 | -44.41429 | 2025-09-18 04:17:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 686f8425-cc2c-33c9-a727-685c1732dbcb | -26.62706 | -51.83431 | 2025-09-18 04:17:00 | NOAA-20 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1b4752b3-def4-3682-8f7b-5fd1a322214c | -18.12568 | -44.65613 | 2025-09-18 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c48349e-131f-3892-91ed-23f5dbb3f033 | -20.79805 | -48.9967 | 2025-09-18 04:17:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 718ec87a-fed8-3fef-8c83-51772deebae9 | -21.22803 | -46.94137 | 2025-09-18 04:17:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bcc83f1-fa70-3ec3-a9a3-682a73107108 | -18.14075 | -44.66994 | 2025-09-18 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eeee726-cc8d-3756-8e78-09f3a084377d | -15.90866 | -43.87859 | 2025-09-18 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fb533862-c0b7-3671-8943-79680ac20d20 | -17.19851 | -45.92571 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 290686f6-658f-3914-97f8-f2dee3c56b0b | -17.33698 | -42.62793 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 70453940-31f2-3589-b941-3295f6c7c7ed | -19.02666 | -48.27796 | 2025-09-18 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| deba71f5-6e72-3dea-a1b5-d384b06a166a | -19.02733 | -48.27401 | 2025-09-18 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 33.4 |
| ae27b23a-fccc-3520-9d73-e8b7d811ac3e | -17.19086 | -45.90956 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 223810ce-3e3c-37e5-b2d0-ca23f8bf3ec8 | -15.97376 | -38.94777 | 2025-09-18 04:17:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c61090db-d64b-3935-b825-f2d33d238ba2 | -19.99441 | -44.31781 | 2025-09-18 04:17:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 30dabd06-1e4c-358b-a837-f736f224ad48 | -18.7576 | -49.32264 | 2025-09-18 04:17:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 78e35373-660e-37af-abc6-05942bf96c7e | -19.90468 | -44.59386 | 2025-09-18 04:17:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9604f680-5b35-33ea-9ad4-12e8e39398c7 | -20.05737 | -50.36865 | 2025-09-18 04:17:00 | NOAA-20 | GUARANI D'OESTE | SÃO PAULO | Brasil | 3518008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| d36cc8ee-1a72-3f01-a7d8-16f2cfe823f3 | -17.34889 | -42.62112 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0353d451-d767-3958-8875-bfb67afffbb4 | -17.87244 | -39.83553 | 2025-09-18 04:17:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0f362a8b-8fdc-3382-b779-cb6541e4f0b6 | -20.88731 | -48.45335 | 2025-09-18 04:17:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1ecfb10-4f06-3906-8be8-d2c9fba1458a | -15.91018 | -43.8777 | 2025-09-18 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 450628a2-96e6-30d4-9b28-a94fc8ad3c47 | -19.63495 | -43.73443 | 2025-09-18 04:17:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de148ec1-b041-3397-93fe-f080c62ec748 | -21.4962 | -45.89978 | 2025-09-18 04:17:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 962da19f-2f20-34c0-b054-1eb0cc6c6fda | -19.5835 | -57.76968 | 2025-09-18 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| eb8ee168-802b-3a01-bdb3-7e944850e442 | -18.6363 | -43.90494 | 2025-09-18 04:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9f3ff81-b1e9-3f5e-b3fe-5a0ad6ca84de | -21.18135 | -50.15464 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 3b7fc964-0d57-3ae7-b54a-e0d25e227a13 | -21.18569 | -50.14861 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 0b8c531e-b565-362f-bffa-40094293da7c | -19.28218 | -47.42863 | 2025-09-18 04:17:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0cdeec42-acf6-318a-9800-ea62cb087b0e | -19.99384 | -44.3217 | 2025-09-18 04:17:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d853d476-ba42-3805-9fb2-b0314c4a1f0d | -17.34406 | -46.81226 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b8bd779-2078-3dd1-af29-9fcf3260c583 | -19.59807 | -44.23298 | 2025-09-18 04:17:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59e3c536-10cf-3c63-9b4b-21b66054ee46 | -19.58628 | -57.78498 | 2025-09-18 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ce954482-0b23-3711-a518-38fc2b7b845b | -16.03064 | -45.17228 | 2025-09-18 04:17:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 004da133-e631-3cb0-a402-c6fe7f098f62 | -19.58107 | -57.80805 | 2025-09-18 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 40d87302-0d33-3079-8d09-e2b55b1d309f | -18.53783 | -46.04641 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 884ac8a4-6852-36f2-9a41-23d9548d7951 | -15.61216 | -42.92179 | 2025-09-18 04:17:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa3a41cf-510b-3d56-a79e-82094776ba1a | -14.5959 | -46.32214 | 2025-09-18 04:17:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bbee431-2b61-39e6-b170-09649dfa9607 | -17.72207 | -46.79049 | 2025-09-18 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49a06224-86d6-3023-8376-98cb7aa64c26 | -17.34769 | -46.79008 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9057f5aa-3d2a-3505-afc7-6bc6df2c5027 | -18.57723 | -45.02828 | 2025-09-18 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2dca9833-6e8b-3919-8da9-9f8268ea4eb5 | -17.17919 | -45.91867 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ed9a172-5f16-365f-bbc5-66fb2c299f30 | -18.53337 | -46.0531 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4de6120-1d87-3dbc-8288-07121e436931 | -22.16875 | -44.74096 | 2025-09-18 04:17:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2e38c82b-d160-3c41-b29e-ff1c755baf44 | -18.53063 | -46.04889 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d1d5055-b248-3d0f-a2c4-77767a059cb8 | -18.97861 | -46.98376 | 2025-09-18 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea82f45b-5fa0-3247-a4c1-7395840f7dec | -19.0349 | -48.27134 | 2025-09-18 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d114d064-e64e-37e4-9545-101d27381508 | -24.50591 | -49.80043 | 2025-09-18 04:17:00 | NOAA-20 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1e248dcb-da07-3e9e-ae36-c1e8b6a5bda8 | -15.91299 | -43.88195 | 2025-09-18 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a15f83ee-7ea5-33c7-9af8-c9839b453dfa | -18.75319 | -49.3264 | 2025-09-18 04:17:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1d0a45a2-b1cd-3ad0-b2c6-25fb47fe037b | -19.57621 | -57.80191 | 2025-09-18 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 01e3276a-6eaf-3bb6-ae5b-85b4f12e1959 | -18.57112 | -45.02351 | 2025-09-18 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 855a319e-9627-3fa9-8df6-5ad497993b43 | -16.28279 | -45.68118 | 2025-09-18 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fa37dcf-4f8b-3845-95cf-85066bcf065c | -16.68986 | -46.94743 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dceab48d-f67f-3eb5-a062-69f2c9e678fd | -16.85891 | -42.26431 | 2025-09-18 04:17:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a14ce883-5589-318d-aa0a-bd971561cea9 | -17.71933 | -46.78619 | 2025-09-18 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c730263f-3176-3395-bac0-b7ac769d9295 | -17.57057 | -43.78573 | 2025-09-18 04:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c46fe96-5063-3b6f-bde6-5167cd91b079 | -20.66538 | -48.74989 | 2025-09-18 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ede53cf-93f2-302e-a05e-dca31fd3b6e3 | -21.30716 | -48.54665 | 2025-09-18 04:17:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5d1c95e-e1da-354a-8bf2-af4f55c2311f | -18.34389 | -43.30168 | 2025-09-18 04:17:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1808219e-2cfc-3c7c-acbf-98dee9e61570 | -19.03835 | -48.27199 | 2025-09-18 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 13f661ce-01a0-3261-809b-33ab5c1f9aaa | -17.19589 | -45.89932 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d60744d-1566-3541-91e1-fa357bc090ac | -17.07476 | -43.19204 | 2025-09-18 04:17:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1065a37-4b81-38ac-bf13-8da06df72d57 | -18.54387 | -46.0512 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3849a519-f02f-3575-b4ee-c8038f00f701 | -20.67015 | -48.75421 | 2025-09-18 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5c35f693-9c88-3511-b366-06fad4f4cf63 | -16.32594 | -43.75997 | 2025-09-18 04:17:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa8e6ae1-0451-3749-b555-dc64179efedb | -19.98186 | -46.74723 | 2025-09-18 04:17:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1389eb0-d09e-3a26-b1d9-4ac305e751a2 | -21.18579 | -50.15086 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 81e3a539-8149-35a2-93bf-0eaee972ff3a | -15.90962 | -43.88142 | 2025-09-18 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07ea8a98-8b87-3e8a-aadb-1186a9071be9 | -14.5953 | -46.32583 | 2025-09-18 04:17:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb68e4fd-2044-3814-8161-e3e38ff4fc73 | -19.58038 | -57.78346 | 2025-09-18 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f2997185-0499-330e-9d6d-f5b15a6c03ed | -21.04972 | -48.84166 | 2025-09-18 04:17:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 19180402-f8ab-3663-8dd9-1a81eec59776 | -21.75363 | -48.1507 | 2025-09-18 04:17:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ece6a25-cb9e-33e9-a115-ea140c1be0a4 | -21.07168 | -45.6128 | 2025-09-18 04:17:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73440e18-9251-3629-ba5b-10dae1d5c9d7 | -18.75681 | -49.32706 | 2025-09-18 04:17:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3169a67c-90cb-3467-a84b-aaa38cf1fc37 | -21.18944 | -50.1516 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a102fb7a-0c6d-3bc4-86f8-f685610450e6 | -17.49887 | -46.74081 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f4d388e-49a0-3b15-99c4-5cbfa3e1aec8 | -19.08047 | -48.29628 | 2025-09-18 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63f04b84-95cb-3ed1-8fb9-23fa3c433d09 | -20.05651 | -50.37348 | 2025-09-18 04:17:00 | NOAA-20 | GUARANI D'OESTE | SÃO PAULO | Brasil | 3518008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 7109f324-7a91-37d6-8fbf-0dd64a5ca678 | -17.17097 | -45.90614 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a0b59ffc-5afe-37ee-90c7-99464b28cbd0 | -15.88831 | -43.46035 | 2025-09-18 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 21798985-2e40-37d3-8bb2-62facc25d726 | -18.5433 | -46.05483 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f379d675-9ebe-3a11-808e-a5e73350625c | -17.01251 | -45.85681 | 2025-09-18 04:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06625041-9812-32d9-ba2b-6d1e0bc3a62a | -18.58879 | -46.55642 | 2025-09-18 04:17:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a074ae80-34dc-30ee-98da-097f37d25573 | -21.16136 | -46.99788 | 2025-09-18 04:17:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18c797ac-d199-381d-82a9-ced6e5294d17 | -19.03078 | -48.27466 | 2025-09-18 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 57c753e8-bf27-3cce-82d4-759033be4e64 | -17.18034 | -45.91145 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9637c7e7-0ee9-3b35-adc5-7e7004287dca | -21.18215 | -50.15013 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 0b2910ce-38b2-3db4-aeb6-bfeae2382bd1 | -16.72179 | -48.48194 | 2025-09-18 04:17:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 316ca143-9730-3f25-b879-aef2f74a1917 | -17.1776 | -45.90728 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec20e80b-1e79-31ca-b4c7-59f425e47cc6 | -18.474 | -48.51193 | 2025-09-18 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README25.md)
