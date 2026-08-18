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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4edfd8f9-93fa-387b-b50a-cd8bfdb7ebc8 | -8.95257 | -60.52472 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 438cf1e1-ae7d-32e8-8b98-035198402abd | -6.91853 | -62.90703 | 2026-08-18 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9c2fbd8-8a7f-3edc-adc6-bab11aa63bc0 | -8.18338 | -55.0122 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 807c1dd8-f24a-338b-94f8-116c7874521b | -9.1651 | -59.66751 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd0cd5fb-cf73-3bef-a3d0-43945a0ce447 | -8.57992 | -54.69215 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 077c8b5f-51ee-3975-bab8-cd9a9ae4785c | -8.90335 | -60.55653 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31e87a0d-5126-3ceb-9f77-e509d708567f | -8.90533 | -60.57197 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ae9433a-49d3-3580-a24d-62e94a27dbb7 | -7.55895 | -55.5689 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b051ba8-06cf-331b-a05d-a30e5a4b9f66 | -7.63501 | -55.62601 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4551b739-b7c7-3843-be38-f33021741026 | -7.90875 | -61.72802 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4701877e-7b30-3de7-ac08-da93a5d7905a | -12.40193 | -54.96095 | 2026-08-18 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b5eeccf4-ece7-380b-b7e9-8ee3e832f584 | -9.45498 | -60.294 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 055ede98-ab35-3d5d-a11a-7cbe740a1326 | -9.43047 | -60.43822 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cb446bd5-50b4-35d5-9e01-a8517ed34e67 | -8.09956 | -61.34669 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5a771bed-8211-34a1-ae47-76dc3741b07b | -7.49938 | -60.07646 | 2026-08-18 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84b85eee-6901-3d56-9dab-f976625ccc76 | -12.46871 | -54.19893 | 2026-08-18 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a143fee5-8364-3b4a-9943-6e36eb28d2be | -11.3375 | -55.27184 | 2026-08-18 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b355e82f-7db1-3d75-8c51-b8c094da8b23 | -8.57873 | -54.70148 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 2dd5f02b-a0dd-347d-8a7b-eaa4fd3cb257 | -8.18878 | -55.01727 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c9d88c68-9657-3491-a6ff-f8e4f3476d40 | -7.53657 | -55.58469 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b65956f-aa26-3882-9e4e-9798c498aba1 | -8.57083 | -54.71495 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2cae0bf1-8a23-32f4-942c-90d72dce7463 | -7.50354 | -60.07721 | 2026-08-18 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 283c3c89-c936-36da-a18b-878c0667a0a1 | -7.46933 | -63.64198 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aabdfc2-5460-3dbe-be65-a7b0884a1ea5 | -10.57497 | -63.54708 | 2026-08-18 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fc224f6-0b65-3f42-913b-b475e37ddf1c | -12.94355 | -56.64849 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b7349faa-2501-33e6-bfac-17d03b837d3e | -8.49089 | -54.86173 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d828f36-f46e-3fd5-8147-63395c24ad5e | -11.36314 | -55.42 | 2026-08-18 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6bd4b67-c521-3186-b2ff-7af811419db3 | -13.42854 | -57.07352 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 290315a2-3f77-3e06-84d1-c17ce7fb9fad | -14.05169 | -53.69109 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61631b2c-2262-310b-8c2c-c050225c78c8 | -7.91631 | -61.72915 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 311aeb75-1005-36de-8cc8-271e3004a5ff | -9.42682 | -60.43377 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b80306b-419d-3237-a926-65b08b4c12e0 | -7.38591 | -59.99453 | 2026-08-18 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94322141-8f1e-32a9-88eb-dc85509a3375 | -8.63405 | -54.7048 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34e2334b-5b37-372f-9189-7d1fcee29273 | -8.90013 | -60.5789 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6092676b-b078-3c36-9e41-0bc7502bf41f | -9.59816 | -60.50824 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e35e065-1f58-3ad8-915f-89cd30c383c1 | -8.90228 | -60.56396 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 340b01d7-f9ad-3bbd-bfa5-4ecc3091179d | -8.96084 | -60.52598 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7183b98-80a6-3137-8144-dc4a73213820 | -8.95414 | -60.51345 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e981b7ad-f313-3be5-abd8-b96a0d12c151 | -8.57023 | -54.71961 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| cc72e0c2-354b-31a7-b2be-45960a8f7f98 | -7.61565 | -60.9502 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04086221-7a51-376a-91ec-b35c1608bf4e | -12.47066 | -54.18145 | 2026-08-18 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14f41ec5-0991-343e-aa1d-87b894799508 | -11.71546 | -54.62862 | 2026-08-18 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1aa06965-ffd0-36b3-aa22-54bce72b8017 | -8.96964 | -60.52345 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16f762e2-472a-3474-8ece-cba5ebf75964 | -8.7289 | -62.89759 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a573d8d-aa14-3618-be51-9daefa929b5c | -8.58004 | -54.7396 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 6985a6bc-3eae-3b65-997d-f0c82a7ff2d9 | -9.39619 | -65.95884 | 2026-08-18 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4aef86b6-49cf-306c-904c-bea620ecf2fa | -9.42898 | -60.41831 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 20434f2f-f245-3020-af2f-36465ca25022 | -9.4306 | -60.40671 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29c0b39d-9b8a-3777-a951-895acb07397c | -8.59031 | -54.70777 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a7178bf4-8f81-3885-91ec-39f2fd02ad1b | -9.16979 | -59.69899 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db3b6f79-fe7d-3471-85a8-00320bb30cf6 | -8.95043 | -60.57029 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe20782a-629a-3ec0-afd1-9e2de89ee9ef | -8.73067 | -62.9105 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a4e4509-38b2-3f66-94c9-43b62ea48e3e | -11.32534 | -55.27015 | 2026-08-18 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41de90ea-9599-3dfa-973d-667ece0ba906 | -13.42818 | -57.06741 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f027670-8caf-363b-b890-6598855ff020 | -14.03275 | -53.67116 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6829aa54-4e0a-3981-9dc5-b380faf48866 | -8.95195 | -60.58953 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4ef59f3-f2b3-3842-9f1d-84acba6ce65e | -9.16891 | -59.67245 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ba74ef9-cd2e-3ffd-bb48-a95b0731823d | -8.75277 | -62.90963 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dff8b379-3e72-342f-ae75-b83171486731 | -11.71912 | -54.62984 | 2026-08-18 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 838efce6-91a2-3b30-b6ac-b2da11e8d651 | -9.16452 | -59.67182 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f511e4ad-af0d-355a-9f60-76607df87d1e | -12.94088 | -56.64875 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a24fc85-2405-3473-9acb-08eaff734594 | -8.09182 | -61.34546 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3382966a-7ea5-3634-9f72-ef552e0b46bc | -9.17359 | -59.70397 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23de0731-0620-3016-80bc-9a770e879b08 | -8.9531 | -60.52096 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15672f76-7bc0-31e7-aaa3-6e03363bcbe9 | -7.6063 | -60.95915 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01bd3d33-cdba-3d6b-8e6c-a542cb14c59d | -7.56464 | -55.56958 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc9aedeb-880a-3af9-b64c-054a915087a4 | -10.14386 | -54.27727 | 2026-08-18 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e3cd814-f82b-3b8e-8c5d-6d850384b612 | -7.88531 | -63.76471 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e88c3ee-6c71-354b-8a7c-cff0772a35e2 | -8.94844 | -60.5241 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0755d0fb-ceb6-384b-9ce3-c948e42a8657 | -8.2066 | -55.0196 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fded7341-b260-3dae-b491-66232924cfb6 | -7.88188 | -63.76418 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eff94ea-8fdb-3568-94d6-48f82cf771ac | -8.95404 | -60.57458 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53f54d00-99a9-3c0e-91b3-efc9b7b4a2ef | -7.9043 | -61.73207 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 028663c8-30e2-3502-a4f6-06e1e511b6f1 | -10.57852 | -63.54757 | 2026-08-18 05:44:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3815692d-e036-373a-ade5-ee66744c69fc | -8.95658 | -60.58643 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d897a59-8d0e-3430-8b09-62b7dcc72981 | -13.93676 | -53.92959 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 20dd3afd-83be-3d22-bc80-a8a977d29154 | -9.1692 | -59.70333 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c09cf72c-cc0c-3583-8660-634afaaebf3f | -8.18286 | -55.01631 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6a6aa00-c2a4-3e57-acf2-dc76d2569c1a | -7.56624 | -55.55792 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47b84057-019a-3b2a-9175-f29bfbe61069 | -11.33142 | -55.27096 | 2026-08-18 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 717e2c5b-8813-3a15-a3bb-ed16da1d51fc | -8.94948 | -60.51657 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d6c9b7c-9f2d-39d1-a88e-dee661f3e19f | -8.57752 | -54.71093 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b41b2b72-8ba6-3788-8b0d-228fda993146 | -8.20438 | -55.03685 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e888767f-543f-359b-bb07-704db9d3531a | -7.60956 | -60.82352 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dae38db2-083f-34d9-b33b-398a6f91b4b4 | -9.42466 | -60.44918 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 85e1d5ee-276e-399c-8b08-093723db18f4 | -11.71973 | -54.62469 | 2026-08-18 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59ad3039-cf93-3e7d-a484-9ba0dd3c94a4 | -8.19522 | -55.01416 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 73ba068a-3908-36fe-955c-1181d7fab53b | -9.45443 | -60.29795 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c43443ca-a21d-365e-8a71-124418e84c04 | -12.46785 | -54.192 | 2026-08-18 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a6b8f60-44bd-34a5-b5f0-ad48575936d2 | -9.16013 | -59.67115 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6babe346-d149-3f77-812b-77233b86a1a8 | -8.8583 | -70.84134 | 2026-08-18 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da53e956-6cfe-3cef-a87d-5f8e19063db0 | -8.58183 | -54.72561 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 421be3b0-fca2-3b3f-8ad3-49e3033f7453 | -8.90048 | -60.60565 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 230d0cf2-5c90-3087-b7be-ebb8cae05b95 | -14.0523 | -53.68497 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c54c5874-7024-35d9-aa23-884ac27e32fe | -9.19692 | -60.88871 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba07b3f3-e69e-3811-b517-eb2ebc3cde58 | -8.95456 | -60.57088 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2ed60d3-20c9-3e52-ab0d-5a4280e58028 | -7.60558 | -60.82292 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 854a9349-c8b6-3fb2-93a4-929a61329522 | -8.21196 | -55.02485 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 417641b6-e52f-32a2-903e-ece0afe6f0b4 | -8.76054 | -62.90659 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3a5f7bc-54ca-3369-a88e-bfe26b070f53 | -8.56654 | -54.69999 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README58.md)
