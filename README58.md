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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28793f6c-884e-3635-9afd-dbb6ce53a516 | -10.21807 | -50.31814 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93edba37-46e9-33a4-86c5-78284fd298c4 | -11.46667 | -44.95889 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0ba5290-8b9a-3f17-baae-e90041dcb556 | -13.19943 | -47.88399 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 632617c2-7b53-36c8-9ada-e51f30f1ce71 | -9.98198 | -48.78491 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97553121-52d6-3908-9664-7701a1389c97 | -14.22809 | -46.11232 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48394797-cf9c-33dd-b6af-ad5ebd4cc4cc | -14.29545 | -45.8869 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cfa3bff-4408-3473-80d7-fea7c5966284 | -14.1978 | -46.06153 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b10c10d6-c83e-352c-8a3f-f5e76b7abbc8 | -13.14966 | -47.78067 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb508085-2dea-3c11-8be0-548700be84fd | -11.87989 | -45.01476 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc3418ec-4090-372c-a474-282f1afa2f5e | -13.20632 | -47.89117 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3e7bc20-3a57-33dc-89f2-73b348b01c1f | -11.49016 | -44.99743 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e74b1c69-83db-3a4e-86b9-842ae9dde4ae | -13.31972 | -47.19744 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04ad1f06-5755-378a-a4ac-bab095f08f47 | -9.00195 | -47.472 | 2025-10-03 04:12:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 603aa563-2311-372e-92b6-f9a4a370bc7c | -9.95141 | -43.65786 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d960e44-96c2-3f00-b8e5-ff1fc6b36718 | -12.84839 | -46.85609 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cb5938f-7adf-30a8-a4df-8073e511be73 | -13.7565 | -48.07414 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e82588ef-da92-3685-9347-5e0027acdfc4 | -13.34778 | -48.08459 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d18fee22-9bfb-3dae-a3b3-3b072f1d3c7f | -11.60231 | -47.65598 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67981f32-d5fb-30e5-aabd-44d94098dadd | -12.62301 | -46.99722 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 733667f4-c1ab-31bb-9521-d88d81a9b9ec | -14.38145 | -48.48043 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 09758403-96b1-3357-9244-92a41a40dc42 | -15.17284 | -43.62744 | 2025-10-03 04:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 14e37c47-70ba-3c13-8221-7a5cdadf67ab | -11.92313 | -46.27774 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 10a554d8-1296-3a60-8d25-d7194547df17 | -8.8848 | -46.58631 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bd403f2-2cdc-3c50-b7bc-02493f650644 | -11.28041 | -47.83054 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1035d77d-d29c-3a98-9be5-da32f85375c1 | -11.15613 | -47.18082 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9cf0a54-ba6e-3e27-a32d-75c44467568c | -14.44054 | -46.37401 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bff6ba44-9425-327c-9e81-9887d3fd4527 | -13.20099 | -47.80625 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79e7c602-0dc9-3f4d-9311-fa389d386da5 | -11.4676 | -45.01864 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9e5aca8-c34a-3258-b403-897a269043bb | -9.17496 | -48.53379 | 2025-10-03 04:12:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6ce137a-7703-34d8-82b8-70cbb93e3d5d | -10.10737 | -50.35044 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7c2dc51-80f2-3e66-9853-a9b75f633be0 | -11.14077 | -43.37318 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4e9842ca-9904-36d5-85c9-b7f8d18b850f | -11.45972 | -44.95768 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed8a66fd-4e4d-3fc9-9074-5c8e80bdfb85 | -14.28656 | -45.91813 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cab12ce-ac86-3dc1-82bf-a0bd2e794d78 | -11.23208 | -48.20597 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47a1b37e-2dbb-3b4c-97d2-b0cd1aed54f4 | -10.64987 | -48.48385 | 2025-10-03 04:12:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b08a607-3e01-34d5-8b45-8aae7c447d0a | -13.38817 | -47.29083 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1678d624-5395-3d40-848e-e111d144fdf2 | -11.14183 | -47.19361 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0a9197b-bf9d-3b8b-a217-1ce230aaaeb4 | -13.96959 | -48.16421 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c773998b-f5bd-3df9-bb6c-6408ffec564b | -12.63091 | -46.97377 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e1cd0f7-00e7-3897-a454-776ce8bae9fe | -11.12399 | -43.39225 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9e920b8-2f73-3635-90bd-dcef252bc0db | -12.60901 | -46.9654 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 44316e61-6ca3-346d-96d8-3298d6e3b263 | -11.55768 | -47.64656 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ecfcbf2e-6a88-3c69-8986-b2c19529c00e | -11.61612 | -45.06236 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b892767-eef3-3c65-9355-fc3db04060bd | -11.11521 | -47.86724 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd484693-1f03-3627-8c13-9c0175906d03 | -13.43659 | -44.23106 | 2025-10-03 04:12:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 237f989d-3137-3589-8731-4b5914421c5c | -12.75224 | -44.91441 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1466345-2072-315b-9970-8a50a963a3e9 | -13.3094 | -47.57912 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 769a16ef-4b89-3456-b78a-158a01cecfc3 | -13.38724 | -47.29612 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ebe79e6-4c96-3cf6-bcbe-fc3c9475ac9a | -13.24166 | -47.35137 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddc1b606-e490-3660-a80f-c2dadaf6b5de | -12.6355 | -46.96967 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20a13588-7a8a-3f26-9392-98dc4c60c660 | -8.71473 | -47.97786 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf9e9fe8-f514-3d48-8696-707249f5b392 | -10.80991 | -46.74451 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afd756fa-7da1-3413-a1a1-69434a6ba9c1 | -13.77059 | -47.53672 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6fde3728-5076-313d-9eae-cac205bd729a | -10.9225 | -46.71795 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 436a97a8-545c-3639-8783-b190f95e87e4 | -10.97366 | -51.08713 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edf78a31-d206-3fc2-b263-7076c8a0816f | -9.29566 | -45.75076 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cbdf537-522f-3223-97ce-c1ede07cee2b | -12.34444 | -54.15755 | 2025-10-03 04:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd6fe9dc-4116-3d7d-bfe7-9db5b5b1c5cf | -13.02225 | -43.83608 | 2025-10-03 04:12:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90171269-6ab9-3e0f-8e03-cc68b57442e3 | -14.47172 | -44.76461 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8fb90f0b-4040-300e-ac78-57bef54ad867 | -11.81856 | -45.04012 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9b70197-c04b-3d7e-87a0-07053c5d25cc | -9.34218 | -45.72246 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 790db687-c3fa-3188-a1b5-d7ca191334c8 | -12.94088 | -45.10607 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9fe514e-a62a-309c-989f-5d40edc8ea8a | -9.06877 | -46.65442 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c69680a9-bd15-35df-a3e8-ad969095dcd0 | -9.33852 | -45.74424 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09937f11-6f8f-3701-b2d3-41b0a24776de | -9.9149 | -43.73383 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 48a56a23-2876-311b-b916-46305f97e354 | -11.42825 | -39.07483 | 2025-10-03 04:12:00 | NPP-375D | BARROCAS | BAHIA | Brasil | 2903276 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e6bb99f2-d6ca-30e7-ada9-0b94c9fcb215 | -10.87797 | -47.82555 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8641898-cfab-38f6-89c5-d42427f2b98f | -13.77107 | -48.06078 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 403e0de2-5e60-30b8-8767-ff88c91c2119 | -11.90402 | -46.74673 | 2025-10-03 04:12:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1dd46ca-8f50-3861-9f9c-6588e8931795 | -10.93074 | -46.73877 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76c4bcb6-7da9-38d0-a349-566b65c6f923 | -11.14574 | -43.38498 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cfaf5d79-8d5c-3f25-b7f5-c9d81a52426d | -11.16394 | -47.18217 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d37f8f1-9d49-3db4-b330-d9317f93fd95 | -13.21838 | -47.36006 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a3460b4-4d0e-348c-94f8-876153217473 | -13.34211 | -48.11616 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b900067-0bfb-3aef-91f0-e4a3b63dd7ce | -12.6209 | -46.9868 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3b3049a8-d88f-3c55-9388-654b8b900103 | -11.80663 | -45.02597 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 494e9cf1-24cc-321c-8924-8fffb8fa56b3 | -13.33622 | -48.12596 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b8e61b5-4d8b-3caa-8c58-c81a2bf25871 | -8.79423 | -46.67554 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c0768e3-6917-3c73-b8c3-c416c8292ad6 | -13.63864 | -48.67322 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff0a06cf-76f6-3078-ab92-c24c496c2734 | -11.14241 | -43.38439 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 868937b9-0a1a-3623-ba17-603dffeb2db1 | -10.76125 | -45.34107 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d896535-563d-3a03-9925-6358588430d6 | -13.65358 | -47.30368 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9b2dfec-63e5-3515-b357-7b3d38773148 | -10.91155 | -47.04177 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84e47be3-c967-3aca-9b60-f42d1ecbd2a1 | -8.6135 | -54.96979 | 2025-10-03 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b279ced6-9851-3c68-a25c-86896542167d | -11.68274 | -47.49924 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 28ccecb6-6d58-3c96-8af9-3d93e2da6f77 | -12.87246 | -44.62966 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12d80251-75aa-3198-9f27-5d543f5b5cea | -11.48448 | -44.98862 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b92d918f-bbc2-3097-bd6d-ef39cb73b3d6 | -13.77152 | -47.53152 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cee62a7-c550-3165-a36e-8f051081f5ec | -11.45497 | -44.96483 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38d9f188-87e0-3a9b-900c-61979054f298 | -13.95977 | -48.10337 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4b55133-531a-371e-b72b-4d8ffe46025f | -13.76207 | -47.54017 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c7ef395c-1655-373b-8b19-397545bfa0b9 | -10.84975 | -46.62539 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| caa415c3-057c-3406-86c9-9bfd2a39fe31 | -13.51914 | -47.25253 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1e3ee00-3338-306c-ac6d-577d1f782b69 | -11.81359 | -45.02705 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27a0fc61-a0dc-3643-a428-7190d023904e | -11.14231 | -43.40639 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b932fa7f-8cee-346d-ba10-aba95653f0a9 | -12.91696 | -46.36705 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f87ee85-873b-3e2c-bef3-77134b1faf79 | -11.49167 | -45.00981 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 845a9214-f09c-3a54-a6fa-1e69e60fa566 | -13.802 | -48.06097 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5af0d985-724f-3697-be71-35ca8e399177 | -14.10324 | -44.30435 | 2025-10-03 04:12:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d3edf6b-a839-3af6-9dec-ddad5067b363 | -12.8667 | -46.99807 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README59.md)
