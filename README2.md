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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d1b9629-b186-3182-a829-4fafca7ca958 | -10.7654 | -53.5451 | 2026-07-01 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 50df03ac-7e64-3cbb-825c-b00ef042ec3a | -8.593 | -48.0288 | 2026-07-01 00:30:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 9bee0e36-64fd-3015-a1d9-28d143b0b575 | -8.5933 | -48.0069 | 2026-07-01 00:30:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| fef83c56-743f-36ab-86d2-5b25cf2f6354 | -12.7746 | -44.5162 | 2026-07-01 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 7bcafad6-4971-36b3-922a-f8234c811d52 | -5.8058 | -43.7975 | 2026-07-01 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 8b64ae41-515a-360a-bba3-217a6bcec46d | -12.7755 | -44.4693 | 2026-07-01 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 380.5 |
| bb7199dc-3eda-3247-a7b5-92f7e59febff | -3.5043 | -48.039 | 2026-07-01 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1dd321a5-3ef2-3575-a525-9007edc04568 | -10.3822 | -49.5849 | 2026-07-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| b394e8db-970d-3144-834f-79d500ceda31 | -10.1237 | -52.0905 | 2026-07-01 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c83bc7a8-2943-32a0-a346-cf1114766df6 | -12.7557 | -44.4959 | 2026-07-01 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 484.5 |
| 77541a84-0917-3cd7-a411-509d8c4b4bcc | -10.6784 | -54.5356 | 2026-07-01 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| ac0242a9-fac9-338d-96e4-787f2a8077dd | -10.439 | -49.5789 | 2026-07-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| fee20f8f-5898-3a04-a823-9996aa31edaf | -12.4283 | -58.4048 | 2026-07-01 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 9c948ec8-9d45-326d-b2f8-04d92d634aec | -12.7553 | -44.5194 | 2026-07-01 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 95ae79fe-c19f-330b-922a-9d658b4311c1 | -16.368 | -56.6514 | 2026-07-01 00:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| eb820566-797f-3cd6-9550-6c9b9c5af01d | -17.712 | -46.7798 | 2026-07-01 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a58ed0a6-f7fc-3d45-b02e-4fdb729d0317 | -11.5528 | -47.4546 | 2026-07-01 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e5d9f27c-52c7-3d1f-a84f-ab6764ae08ad | -16.3677 | -56.672 | 2026-07-01 00:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 6b5f35bc-06ab-3b77-9cb3-7927725dd296 | -17.7114 | -46.8031 | 2026-07-01 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 8366be66-260b-36b4-a57b-c860e8e778f8 | -12.4285 | -58.385 | 2026-07-01 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 87ec6114-3425-3e6e-9846-98c15bba54e2 | -11.6286 | -59.0169 | 2026-07-01 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9baad4d4-e430-379e-9ef1-c2e0a3df5b21 | -12.7562 | -44.4724 | 2026-07-01 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 181.3 |
| b26f1f56-4071-39dc-8893-14a7e7e557d7 | -12.4096 | -58.3865 | 2026-07-01 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| fd9a733a-8ffa-3072-af7c-7750974570b1 | -10.9205 | -43.0622 | 2026-07-01 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 86d262ec-fc25-300c-9029-1f21b7408c66 | -9.6037 | -56.9276 | 2026-07-01 00:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 85807c51-339e-30b5-91d7-97055fed0554 | -8.6121 | -48.0051 | 2026-07-01 00:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 5b51f475-777c-38c7-9201-be395006d236 | -11.5337 | -47.4571 | 2026-07-01 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4aef93e0-fcd2-315d-b8b7-f361be186add | -12.7751 | -44.4927 | 2026-07-01 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1239.6 |
| 4d09ce3b-2d62-3722-8fd0-7eca952c6bee | -8.5933 | -48.0069 | 2026-07-01 00:40:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 6f889d1f-bb18-3ae5-944d-7186851a57b9 | -10.7657 | -53.5245 | 2026-07-01 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 4c4de914-a57f-3a18-bdf9-2a39154c3168 | -11.5528 | -47.4546 | 2026-07-01 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| c0e0e3c6-dc94-321b-99d2-48ba684aee0d | -12.7755 | -44.4693 | 2026-07-01 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 582.3 |
| 72c7f725-9f49-315a-bf11-37008e972314 | -17.7114 | -46.8031 | 2026-07-01 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 437f89b3-e44b-3c3d-8c6b-d1b51e5a3e26 | -12.7746 | -44.5162 | 2026-07-01 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| cd804438-25f4-3a3a-8a23-2f83aaa979d8 | -12.4094 | -58.4063 | 2026-07-01 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| f28d1b9c-6cb0-3b3f-b4ea-ccac21ebb501 | -10.7654 | -53.5451 | 2026-07-01 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| bd80eb82-df16-33f7-87d2-e83029773613 | -11.5532 | -47.4323 | 2026-07-01 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| beb3aeb1-eeb0-3ee6-9800-f54777500b4d | -12.4283 | -58.4048 | 2026-07-01 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 39dd029f-5856-3579-9fc3-9518ff501dd5 | -12.4285 | -58.385 | 2026-07-01 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 7fce69c3-8d17-3c8a-91cb-2c8a06007da0 | -10.1237 | -52.0905 | 2026-07-01 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 4241fc95-9b74-3dd0-9b48-8eec68884674 | -12.4096 | -58.3865 | 2026-07-01 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 9c79ccd2-4711-373f-ac6e-bcd6b2b706e5 | -11.6286 | -59.0169 | 2026-07-01 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 38fb1d82-a203-3720-a145-3c7b8fd8b752 | -16.368 | -56.6514 | 2026-07-01 00:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| f86c0e7e-53e2-3e46-9c10-e1fd599c25ba | -5.8058 | -43.7975 | 2026-07-01 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 25b9081d-d09f-308a-bb44-648e2e4f3991 | -8.1254 | -47.8749 | 2026-07-01 00:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| ea1d1575-1eb2-3304-9d66-54371626350a | -12.7557 | -44.4959 | 2026-07-01 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 507.2 |
| cf3fd6c7-412e-32a4-bb3a-0d44928053c0 | -9.6037 | -56.9276 | 2026-07-01 00:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| db0875a8-193d-3633-8dd9-5a4eb76aab88 | -17.712 | -46.7798 | 2026-07-01 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d5ba1b37-7044-3738-ae9e-150700da6047 | -10.439 | -49.5789 | 2026-07-01 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f22b6ae5-1ec5-3a4f-92d5-7b265b922e1a | -10.9205 | -43.0622 | 2026-07-01 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 080df7bb-a953-3746-8dcf-3fbbde4b388f | -11.5337 | -47.4571 | 2026-07-01 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| a7113cd0-607f-325d-b347-ac5bd8732a86 | -12.7553 | -44.5194 | 2026-07-01 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 3a7ea4e8-1418-34f1-b7f6-df51955a4de7 | -8.1251 | -47.8968 | 2026-07-01 00:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 5d43ff32-5dbe-33ed-8a88-71101cb2d8a7 | -8.1442 | -47.8732 | 2026-07-01 00:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 1ce7983e-a566-3c8b-be94-44a6ab9bdf3f | -3.5043 | -48.039 | 2026-07-01 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 4594c4eb-375a-3fd5-8e50-44d4c916b3a0 | -12.7562 | -44.4724 | 2026-07-01 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 8ed37fda-8a44-3335-9f1f-bdb6b49fc84f | -16.3677 | -56.672 | 2026-07-01 00:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| be0f7314-c9b2-30cc-aa45-df26961432ea | -10.3822 | -49.5849 | 2026-07-01 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 573b90f6-cb15-3938-ac70-485d8e826d9c | -12.222 | -56.5668 | 2026-07-01 00:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e26ee711-574c-3e01-9ea9-f8699501bb24 | -10.6784 | -54.5356 | 2026-07-01 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3a6f5718-908d-328c-a81c-d7207ce4fb7f | -9.6037 | -56.9276 | 2026-07-01 00:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f40ff94a-41e9-3ef3-9211-abcd7ea44dc8 | -11.6286 | -59.0169 | 2026-07-01 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 37255506-9fb7-3e97-8eac-3e63ccc552d8 | -8.1251 | -47.8968 | 2026-07-01 00:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| a2e25db9-6c79-3485-a73c-e2506ad49bf3 | -5.8245 | -43.7961 | 2026-07-01 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 51a39ac3-0fee-3e3b-8be1-4f2ec2228717 | -16.368 | -56.6514 | 2026-07-01 00:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 993fd6a4-b1f9-3a69-8fea-9b11262f0f41 | -10.1237 | -52.0905 | 2026-07-01 00:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 4e48b649-64ae-352f-8643-cff721560d04 | -11.5528 | -47.4546 | 2026-07-01 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 317fa614-53aa-3a42-a655-6b3cb179a702 | -12.4094 | -58.4063 | 2026-07-01 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 8cc2f79b-603a-3524-8c80-534dd418326e | -17.712 | -46.7798 | 2026-07-01 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 26c18ca9-ab63-3ab0-bdd2-37b5f3e72431 | -8.5933 | -48.0069 | 2026-07-01 00:50:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 029294d8-446a-3ec8-a659-757e2643de00 | -10.439 | -49.5789 | 2026-07-01 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f79dd666-23b0-3069-9c27-ccb92e14e2d7 | -7.7156 | -45.9388 | 2026-07-01 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| e30097f2-98af-3a8c-83f2-4f2c71f0809f | -10.7654 | -53.5451 | 2026-07-01 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 6f1964d0-ef58-3adb-8283-b5585a7bdbcd | -8.6121 | -48.0051 | 2026-07-01 00:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 87ac0120-493b-3d22-aa9c-6ab2fb970740 | -5.8058 | -43.7975 | 2026-07-01 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b9977632-4709-3708-9624-12e107c88eb2 | -11.5337 | -47.4571 | 2026-07-01 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| eac48c8b-6659-3664-8c60-46e89bc5ff8a | -3.5043 | -48.039 | 2026-07-01 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| cf2dfc7b-681c-3a6e-befc-4bb97a4ffdf5 | -10.6784 | -54.5356 | 2026-07-01 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 7da38d4e-87a4-3642-9da7-9d4a8c3ef94b | -12.4285 | -58.385 | 2026-07-01 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 01abcce5-41c0-375a-a1b7-b92ff80910b6 | -12.4096 | -58.3865 | 2026-07-01 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 9b8dd730-5b8f-30cc-b7a0-9e6953031a90 | -12.4283 | -58.4048 | 2026-07-01 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| f5a94125-4d7e-3625-8ca1-039a5f14e550 | -8.1254 | -47.8749 | 2026-07-01 00:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| bef1bc27-63cb-3028-97fd-459e0105370a | -19.51349 | -52.75227 | 2026-07-01 00:58:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5b9cf84b-c544-3cd5-b1ad-6dfe4e07f742 | -16.36541 | -56.65546 | 2026-07-01 00:58:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.3 |
| 88425133-6eb7-31b2-a2f0-df993f4236c0 | -21.09628 | -57.46019 | 2026-07-01 00:58:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9fe8e575-1aa8-3a5c-9922-22b2ae094bde | -16.35493 | -56.65731 | 2026-07-01 00:58:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| f223d478-0eaf-33d3-a9b8-b389ef31b069 | -16.36751 | -56.66868 | 2026-07-01 00:58:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 65ea12f6-21e1-30fd-8e82-ef5480418764 | -21.09789 | -57.47073 | 2026-07-01 00:58:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 031e5a01-950b-3b45-8cdc-8f6625e0d714 | -16.35705 | -56.67054 | 2026-07-01 00:58:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.9 |
| 2d421be3-ca48-39f5-b828-48aa4a140220 | -16.13576 | -58.50428 | 2026-07-01 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 42175ccf-b78b-33a2-8044-6fa6ffc332f4 | -8.1254 | -47.8749 | 2026-07-01 01:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 47268130-59b9-37ae-b740-608887be7e4b | -10.1237 | -52.0905 | 2026-07-01 01:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ee791b05-d87c-3057-bbb9-bf8daa397aa6 | -11.5528 | -47.4546 | 2026-07-01 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 54a9e28d-7fda-3990-888b-0230a7be62e3 | -11.5337 | -47.4571 | 2026-07-01 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ea6607d7-e0a1-3c87-b041-3a3212db2840 | -8.1251 | -47.8968 | 2026-07-01 01:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e688c595-f36f-314b-bbab-382d87973c55 | -12.4096 | -58.3865 | 2026-07-01 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 681a1ea1-f53a-338f-95c4-ba18b2f2696e | -5.8058 | -43.7975 | 2026-07-01 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 14225644-d4ed-33f9-a94f-37fbbc185880 | -8.5933 | -48.0069 | 2026-07-01 01:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 84a5b8bd-cdc5-3206-98a7-6adc3e63bb52 | -12.4285 | -58.385 | 2026-07-01 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 7284209d-2ce7-3fa6-9243-8c7e3caeb3a3 | -3.5043 | -48.039 | 2026-07-01 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |


[Clique aqui para ver as próximas entradas](README3.md)
