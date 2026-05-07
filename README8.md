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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68fa9efd-61da-3f51-a740-a4a84b1535d6 | -10.63636 | -48.00905 | 2026-05-07 05:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f42b4536-be98-3f8d-867c-be68d8285aa2 | -10.63713 | -48.00786 | 2026-05-07 05:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 31a7be73-ecdf-3aa4-ba21-e0e2edaf6d20 | -11.61765 | -48.05347 | 2026-05-07 05:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9a46dd1-e629-3736-b017-9e3f522c4fb4 | -12.3481 | -50.02061 | 2026-05-07 05:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fcb3fdb-a926-3745-87f6-1472b13587e0 | -12.34596 | -50.01548 | 2026-05-07 05:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16ef2687-aca9-38c4-8633-973396ca41ba | -11.60293 | -48.05807 | 2026-05-07 05:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f48de07d-e55c-348a-b631-c98590f8bf19 | -11.73551 | -54.80727 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9599da05-7fd6-35f4-9dec-f74868e27f5f | -11.61218 | -48.05627 | 2026-05-07 05:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b73de6e7-318c-32df-b271-cc26cefa110e | -11.73672 | -54.79799 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2516d1c8-f3ae-3fa8-978a-c392920b4e3b | -10.63261 | -59.419 | 2026-05-07 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28ee1f5e-a677-3b5c-849a-5fe2849a5f1b | -11.60991 | -48.05918 | 2026-05-07 05:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a389b7b5-b60b-3b26-8e99-8f8385989175 | -11.43786 | -55.10193 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7b254c5-6774-3dc5-b9d1-deac1509cd7f | -12.34539 | -50.02052 | 2026-05-07 05:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10368405-8a8e-3cf8-a29b-7429730a975d | -10.63604 | -59.41954 | 2026-05-07 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6103694e-3c14-3681-9afe-951db83f962e | -11.73157 | -54.80199 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bf866f9-4c71-32de-8898-ba3ef6b02e22 | -11.74068 | -54.80323 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58e67d50-2159-3394-9ea5-e25738d226a9 | -18.78057 | -51.94131 | 2026-05-07 05:27:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 076b75e3-1465-34b3-8abe-afbcd801d545 | -12.50233 | -58.47139 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 410a018f-4395-3bcb-bbff-2b6452bd9182 | -18.44306 | -54.70764 | 2026-05-07 05:27:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f6c348dd-5a64-3d1d-9021-eb220cb13a0e | -11.8408 | -57.84631 | 2026-05-07 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d77ccefd-398e-3f73-a868-057079ba9312 | -13.213 | -47.88374 | 2026-05-07 05:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ef92496-8151-3df4-bedb-eee9132ad6b9 | -18.43836 | -54.70407 | 2026-05-07 05:27:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed732adb-5ea2-3cd6-8107-9ef1b1e9cfe3 | -13.21233 | -47.89032 | 2026-05-07 05:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff54534e-888c-3ace-8bb0-d4be903444b6 | -12.49374 | -58.47903 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 821043a8-7ecb-361c-a9f1-d12edb160704 | -12.49803 | -58.47523 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 114c023d-6a54-3185-a6d6-93469b40637e | -11.83706 | -57.84577 | 2026-05-07 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b28da91-a961-3be2-8f59-92d68cd425db | -16.60236 | -58.24175 | 2026-05-07 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e438f371-65d9-3167-adfb-c172ef147f11 | -13.71565 | -56.88113 | 2026-05-07 05:27:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d27bb972-7228-3618-9118-cf9c2a377c2f | -16.16447 | -58.48705 | 2026-05-07 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cffb249b-c0d9-3543-b44c-3fb07e45223f | -14.14649 | -52.89508 | 2026-05-07 05:27:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db22c01e-815b-34b9-b8c2-c7ad49ffadbf | -12.50598 | -58.47192 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd36a984-6de2-37bf-90d7-f93ae4bbeea6 | -13.94213 | -54.80347 | 2026-05-07 05:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b977112-ae40-3029-a8b6-ce5987a98186 | -12.76478 | -58.99131 | 2026-05-07 05:27:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd32d4b7-0fb4-35cc-ace3-5c0bc1b183a9 | -14.86038 | -48.56163 | 2026-05-07 05:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12c24b88-39a9-3494-aa3a-55dd40d3d86e | -18.43801 | -54.70716 | 2026-05-07 05:27:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ace70c28-335e-3a62-a424-9b087c3fe8c8 | -12.77633 | -59.00373 | 2026-05-07 05:27:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dab94d9-82c3-3fb4-be5d-b7685902c7cd | -12.49868 | -58.47086 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0afa32e1-74d4-350f-a3dc-1bc1ecbab429 | -12.50168 | -58.47576 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d17f6ff-5d73-354d-9817-36153657c761 | -12.4931 | -58.48338 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78d11dff-d3eb-381b-a28e-7542dc368ae0 | -13.21043 | -47.88301 | 2026-05-07 05:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66044bea-84ba-369e-802c-7d9efaf4432d | -12.50039 | -58.48449 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7174a30-e470-3a9d-94c4-0cf003684e1f | -16.15998 | -58.49134 | 2026-05-07 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0f56cefd-9869-3b2b-82b2-7956f53eef06 | -12.49739 | -58.4796 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad851a6a-c88e-36ae-9896-2e404a5885ea | -12.50104 | -58.48013 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 496265d2-c9c1-3e40-a0e8-ac96ce4fd2d4 | -12.77929 | -59.00839 | 2026-05-07 05:27:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34412ca5-f6fd-3843-ac2a-ce3e4527e66c | -18.43766 | -54.71025 | 2026-05-07 05:27:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f920ce55-4123-3013-9896-b46fb620c69c | -12.76416 | -58.99545 | 2026-05-07 05:27:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| baa2ca67-aff7-3ede-84eb-a7b70314c7a5 | -13.93744 | -54.80275 | 2026-05-07 05:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73d3e338-f2ac-32a5-a654-7c11347868ac | -12.49438 | -58.47468 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38bfebe7-7f75-3447-b6b2-df50d9b9712d | -18.33129 | -54.52458 | 2026-05-07 05:27:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c68c8b0f-8297-39e7-8330-4afc5f5cce54 | -18.43871 | -54.70096 | 2026-05-07 05:27:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ea36897-24fc-3430-b885-b3fdffce5999 | -12.50533 | -58.4763 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5567349d-1ad4-3b1e-9923-ba97d041562d | -12.49503 | -58.47031 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f77fec9d-d39a-329a-a12e-ab03e4e5dc63 | -16.60305 | -58.23673 | 2026-05-07 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6540ce68-448f-3b4c-be79-72bf3e77cf64 | -11.84143 | -57.84801 | 2026-05-07 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28e56247-d818-3ffe-b644-3c49f236c42b | -12.49675 | -58.48394 | 2026-05-07 05:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d637ee4-6497-32e1-bcb5-9255a4eb457c | -14.86102 | -48.55518 | 2026-05-07 05:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaa753aa-9df8-3a23-9ed5-0ff7086f5d68 | -16.16829 | -58.48763 | 2026-05-07 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ee9b4de1-610d-3f3d-99fd-022749e6c4fa | -18.43333 | -54.70346 | 2026-05-07 05:27:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 216db8f7-37f4-3faa-bede-6a050384ffeb | -12.77573 | -59.00785 | 2026-05-07 05:27:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e71e1ee2-25bf-30fa-b5e4-7201e4afd991 | -13.20974 | -47.88938 | 2026-05-07 05:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ab0c4c8-2dce-3234-8b8d-76550d96f074 | -13.15398 | -56.80635 | 2026-05-07 05:27:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab01738d-25b3-3da7-a241-303cd5b4cace | -19.94798 | -54.38123 | 2026-05-07 05:27:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbfd1e91-d50c-3b60-b4da-502eef841191 | -19.94762 | -54.38464 | 2026-05-07 05:27:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cae824cb-e577-35f2-8bf3-59ecaa1d99c9 | -16.16379 | -58.4919 | 2026-05-07 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 72e43030-3157-32c2-83a9-58f832eef03a | -16.59847 | -58.24118 | 2026-05-07 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 067dd221-7f53-3f3d-aa8e-85162fb75209 | -16.16761 | -58.49247 | 2026-05-07 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 17247147-c8e2-3307-8594-430e929812c3 | -12.77216 | -59.0073 | 2026-05-07 05:27:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6116d2d5-f318-3be0-a531-ad09ea218c05 | -18.44341 | -54.70454 | 2026-05-07 05:27:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 20aa0cfc-b542-3a69-92d7-ea43b69f81ed | -13.18147 | -52.69551 | 2026-05-07 05:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05b3a05a-db8d-341e-9564-e0cbd41197b2 | -13.18684 | -52.69617 | 2026-05-07 05:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 628a6f4c-a9a5-3b03-b479-022d101ce654 | -12.76623 | -58.9979 | 2026-05-07 05:27:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69001ced-4fad-3c60-8990-7c8f87134280 | -16.59915 | -58.23617 | 2026-05-07 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f5244375-471e-398e-84fe-a5ed78c22753 | -12.76683 | -58.99374 | 2026-05-07 05:27:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ff9b59f-8fc8-33fb-a319-63c0b3edde62 | -21.95265 | -57.58955 | 2026-05-07 05:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5033250-b028-3f17-ba22-cc03314e2079 | -21.97871 | -57.59388 | 2026-05-07 05:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b44a383b-51fe-34f0-bc9d-71958e41e6ec | -21.97437 | -57.59315 | 2026-05-07 05:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a8053eb-bfa3-3c61-8f9a-7e75b86755e0 | -22.96835 | -52.69532 | 2026-05-07 05:29:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0ba84f08-a4a5-3ee4-b74e-2281bc4bcc7f | -22.97439 | -52.69581 | 2026-05-07 05:29:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e5192c4c-6eee-35f4-a912-331aa8385e6b | -20.71398 | -55.18133 | 2026-05-07 05:29:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 429720a1-61ac-3fc4-a1b0-2aa548a80e37 | -21.95701 | -57.59017 | 2026-05-07 05:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a90b98db-f561-3f04-9f6e-cf3d5efd94da | -11.72949 | -54.8012 | 2026-05-07 06:59:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2af63e22-d928-3ed3-9503-9e84324eb688 | -16.16509 | -58.49015 | 2026-05-07 07:01:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 1d799d7c-22b6-3109-bd72-2231bb938d8f | -18.44368 | -54.70417 | 2026-05-07 07:01:00 | AQUA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cfd022e7-d807-3142-b486-027bda8dfe06 | -18.43383 | -54.70285 | 2026-05-07 07:01:00 | AQUA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d875f9d1-3baa-3f90-95ac-6a8b49e2c3a8 | -12.49306 | -58.47525 | 2026-05-07 07:01:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0be9b239-a820-3735-bbbd-60c93d191654 | -12.1586 | -46.6546 | 2026-05-07 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 67d1a67d-326c-3590-82f0-a8861c51a1af | -12.1582 | -46.6772 | 2026-05-07 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| d5443efa-fe18-3bd5-9c92-cbe0c300d1d9 | -12.1582 | -46.6772 | 2026-05-07 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 9437713a-9140-33d3-aa70-bbca0f8014be | -8.7841 | -44.8315 | 2026-05-07 12:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 2de44cd4-72f5-3461-ae35-0d8fa94cc1e5 | -12.1586 | -46.6546 | 2026-05-07 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 7f07669a-2af6-3a08-9726-6f1290e62e36 | -12.92138 | -49.48082 | 2026-05-07 12:00:00 | TERRA_M-T | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 87a14148-c07f-3cdd-8c73-d7c2dd7cfc0c | -8.6883 | -49.09257 | 2026-05-07 12:00:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 0136bd42-4dbf-3651-959f-b929fb18ed28 | -11.0636 | -49.5042 | 2026-05-07 12:00:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| acc41f5e-c930-3394-9a77-c2cb4d85fd37 | -12.34472 | -50.01281 | 2026-05-07 12:00:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 421a5e32-783f-367d-b73c-e8bd5486ec59 | -12.15661 | -46.67114 | 2026-05-07 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 77a90c1e-9faf-3cc9-a842-4fa749128cb0 | -10.57692 | -47.04367 | 2026-05-07 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f7a705b2-8a86-3062-a107-fe440a864133 | -8.77831 | -44.83892 | 2026-05-07 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| abad7490-2e4a-3e6e-a6e9-5605d872280c | -11.54481 | -42.1896 | 2026-05-07 12:00:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 1c86f549-a37b-3493-89da-8b210bc3cc01 | -12.15797 | -46.66126 | 2026-05-07 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |


[Clique aqui para ver as próximas entradas](README9.md)
