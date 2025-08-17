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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cd86a74-abc2-3d77-bac3-0b17c0111372 | -9.93054 | -60.46457 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92b7f7d5-df57-3414-824d-3a71c47e2858 | -13.43664 | -56.78191 | 2025-08-17 05:06:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9afc0cf-e35a-3dd0-bf3e-1bdb020c023f | -13.0091 | -56.86708 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b18e38c-a9d5-36a0-9a55-84e177ddb68a | -8.87975 | -68.51886 | 2025-08-17 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 712c65da-5a0e-3920-aa4e-afa477b13546 | -10.96607 | -49.56929 | 2025-08-17 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a145385-3596-3cfe-9ad1-0a833c55e457 | -12.57351 | -47.04778 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09e2b54e-822f-369d-aa69-3276a632af8a | -14.18374 | -45.31641 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2b86f5f-0f0c-393f-ae2a-9701797fb7d7 | -9.16426 | -59.61342 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75f093d9-9925-3034-b709-d5c4744b998f | -9.19801 | -59.63151 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 776fdbac-1b9f-35e7-8e0e-6991a436c82d | -9.18095 | -59.64573 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24b31e87-6148-3bd6-b5c6-31f2118afc19 | -10.31207 | -52.55844 | 2025-08-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8c7713e-d708-3158-a21e-0ab2cbc284d5 | -11.3648 | -61.84841 | 2025-08-17 05:06:00 | NOAA-21 | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c70d18d-4f8d-3ff5-bffe-98c9c72e9efd | -12.99805 | -56.87259 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9402a2a4-67c8-379e-867f-402105fa5542 | -9.19443 | -59.63094 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fdc0b0c8-fba0-34bf-a625-6c102da4163f | -8.9953 | -60.49858 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f7da1bf-115a-34a5-9efb-460ce69475f0 | -8.30766 | -55.11027 | 2025-08-17 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f297af-ad3f-3bc8-b28b-81a5675d1244 | -10.10918 | -57.7693 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c80ead59-3f76-3e41-84ca-7abab29e4d58 | -7.42534 | -60.59605 | 2025-08-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 615c2e26-64f0-31c3-86ae-5766464bcbb8 | -9.55811 | -63.66513 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b52a019-df42-395f-acbd-e965cc16a8a7 | -9.50794 | -60.52501 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| babea5e1-c6d3-307d-80f6-fdd1c198e48a | -13.57355 | -46.98555 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed0104a2-0802-370d-b4d0-841825309de9 | -13.59081 | -47.7671 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 080309c8-3b68-3974-90a7-2173aae2edbf | -13.57965 | -46.98388 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 644cfc57-3260-3e52-8645-3e2fdac3d69a | -9.55355 | -63.66432 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6471d9bc-815e-3519-a098-867506b6efb4 | -12.19044 | -47.24169 | 2025-08-17 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b81a6220-136b-39ca-bca7-8daee5295cee | -14.93252 | -47.06085 | 2025-08-17 05:06:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60a0ce5e-b3ae-3717-b0bf-102206b0ad85 | -10.83995 | -45.36629 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6566636d-fc5b-3a52-a3cb-fca972f6d30e | -13.42936 | -57.02895 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9922051a-a8d9-3a05-8ecf-36b1df68bcbf | -9.14522 | -58.29445 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7937c12-8e6f-3126-8f7e-8834ceee05c5 | -8.23747 | -61.46979 | 2025-08-17 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| adf50b72-6412-3a60-a11b-a39875bfc961 | -10.10975 | -57.76575 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d9882c0-0389-3706-a415-763c4fb673a4 | -12.13131 | -47.90525 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 035b13e1-4ac8-376a-adec-187c75950c35 | -9.51315 | -60.53991 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e2e5ba7-f778-3d8e-a130-776e0198b7ef | -13.6142 | -47.75908 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d26d6bb-bc6b-35a4-9d50-52a21586af74 | -8.99302 | -60.51597 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c0fe0b7-38a2-3807-a446-ab120c3eec3c | -12.69548 | -46.97739 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f15fd0b-5085-39af-8fe9-0b1bf0a650cf | -10.82731 | -45.32457 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 288509a5-cbc9-35fb-a382-830948e132b3 | -10.83622 | -45.35572 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bfd6631-dc63-30db-ba7e-64860c52cf0e | -13.15907 | -55.71513 | 2025-08-17 05:06:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7c56c20-65e2-3f92-88b5-269103b73ee7 | -12.13508 | -47.91873 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bac38d06-5295-3a56-927a-2a76da9b28f0 | -13.00687 | -56.85946 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c7e0f1b-501f-361b-8fec-d78bc421a57a | -11.35642 | -55.39993 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58224749-4892-36cd-b44f-7bd80ade6186 | -14.32409 | -53.42439 | 2025-08-17 05:06:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00773f54-6a86-3600-8abf-a9e315d5c900 | -13.4474 | -45.88312 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16b694ac-2c02-3b7d-9284-8e104b43743c | -12.99746 | -56.85433 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a7b88ea-8ec1-3b69-b008-8c06bc675515 | -9.16509 | -59.63046 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe90e414-21ac-341f-ac7c-70ddadf1e8bb | -8.79754 | -52.07643 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 911d1b44-34f5-31fc-8c93-1d75aa1703dd | -13.57929 | -46.98698 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4402d9cf-cc64-3cf3-a9a8-7d15da5aa3e8 | -11.36087 | -61.84771 | 2025-08-17 05:06:00 | NOAA-21 | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 634e9176-cf10-3cf8-a099-22242fde94b8 | -9.26474 | -60.77222 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 770c662f-57c3-3fd9-9f02-5c468dcb6742 | -8.89589 | -60.74532 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ce610ed-9710-3f98-9e5c-90f0c6cffd7e | -9.18454 | -59.64627 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 366c7658-62dc-3e33-bf5a-ee12c55a6f54 | -13.58549 | -46.98435 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02fbbbf7-4578-377f-ad55-d7b94892d32b | -9.00054 | -60.51718 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a3f57ec-50c4-3fcb-87f5-515e78c8c82d | -10.11365 | -57.76274 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbca6148-983b-36a0-af50-e75f5f7cba60 | -8.23405 | -61.46548 | 2025-08-17 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c241569-6b97-3186-b3d0-422c8231e7de | -11.57096 | -47.26459 | 2025-08-17 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a9a959d-72cc-33b5-bddd-f5209cabbeed | -13.61163 | -47.78097 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa11c12f-984b-31b4-bae6-e87d48aa9424 | -8.98028 | -60.49608 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| af159a03-769a-333c-b40b-78ee6efd88e9 | -13.00632 | -56.86301 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 582e50a2-94a8-34c5-ab5b-8c8bddb78f0c | -12.82463 | -45.99023 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6f5c324-a9f8-3b13-b9d9-996c7b344400 | -9.21163 | -59.63809 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45799409-d0ac-374d-a1c6-6694657da005 | -12.14119 | -47.91353 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b0a7901-1cda-3929-b0b8-414c227cff35 | -13.4391 | -45.88741 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e055e4a-d204-31ba-be31-6d572ee5e8aa | -13.58997 | -47.77436 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b3e38c0-aaa1-38ee-b189-b4d43899bd6d | -9.5079 | -60.54836 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb9858ce-8be6-3d13-acaf-a9d31f430482 | -9.22237 | -59.63987 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8560d85-fc69-3da1-a8aa-ead9055e40b0 | -10.43322 | -60.28776 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59a8185b-ab17-3655-b067-9d2a285de349 | -12.89758 | -46.12068 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| defa1c66-9c8e-3c8b-95e9-96bbaf822a16 | -11.36668 | -55.42422 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 631d6371-2241-3a9b-ad09-a1c1a489c12a | -9.16152 | -59.62985 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ac6a5a9-4538-3963-8511-b6c6acee07d5 | -9.99645 | -65.28394 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82e77c1a-025c-35d9-b7cf-d8e5f8996b71 | -9.50643 | -60.53408 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15e202ed-5d71-3da7-8df3-dc3f1faddec6 | -14.59449 | -47.95432 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b6d392c9-dc50-37fa-944e-03105a5c794e | -12.8904 | -46.12991 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6ec6b73-1f62-3157-8d04-ebe9f8ed35e6 | -9.55285 | -63.66645 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1389c4af-73f0-3901-ab14-1a8570b20c8b | -7.21854 | -60.38839 | 2025-08-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e60fe64-bc5e-3322-9fdb-a86c7fd4d3d0 | -11.35753 | -55.39251 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ecf5eb7-06f6-37e0-97b4-7ccecb1b3424 | -9.76218 | -67.53474 | 2025-08-17 05:06:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da9d48d5-f4cb-359f-9567-b47f83d927bb | -11.37007 | -55.42474 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9544eac-9454-315b-ba64-b262471b14d4 | -8.99364 | -60.53493 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91ff65eb-1f74-3930-acbf-50d69877fca1 | -8.99819 | -60.53094 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4027d742-fe08-3f4c-9b67-f877540ee4cc | -10.11251 | -57.76984 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbd42d8b-2e6e-3e2c-99f6-4b760e22e247 | -10.83919 | -45.33112 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 911f2e3f-0d56-33c2-9292-e35fab8f5f8f | -9.60812 | -65.37312 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d25e8cd7-7f69-36e5-aeb7-d3700f127bb3 | -13.60076 | -46.90181 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2e6307b-0dbe-359d-9154-7f1187ae4397 | -8.99521 | -60.52573 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fba9685-e4df-3aa8-8bcb-2cb2b0241329 | -13.43964 | -45.88239 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6dbd553-f1d3-3d2b-a21d-f4ca809fc13c | -8.87703 | -68.51303 | 2025-08-17 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4de392b5-824b-3aa5-9b95-86adb20c7585 | -13.6047 | -47.74418 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c04010b-040c-3d61-b0e9-356b9fb35056 | -13.00191 | -56.86958 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e6bed51-ccaa-375e-bad1-2b274a48e89e | -9.50714 | -60.55292 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ced5986f-ee1e-384f-bd39-1776341fd6ae | -10.83562 | -45.36063 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c5d6ca6-df99-33ee-8538-2d368dcd4cec | -13.65953 | -53.70317 | 2025-08-17 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1c66427-900c-3a93-bc39-e5cebd5af9bb | -11.57049 | -47.26836 | 2025-08-17 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c85f12cf-8995-3282-98e1-eaaa91adcd2b | -10.35806 | -64.50742 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 58b70a05-f466-31cc-b566-8e903553943a | -7.42228 | -60.5906 | 2025-08-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f10d6622-40be-3182-be55-14f7d5f6e42d | -9.26553 | -60.76751 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e42e70e6-56e0-38e7-b465-90072a206f2a | -10.84954 | -45.33771 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d74e424-d816-362e-930f-2ffc5de28ca8 | -11.36155 | -55.41207 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README29.md)
