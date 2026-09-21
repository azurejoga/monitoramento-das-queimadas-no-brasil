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
| 02f61135-51be-30da-bbdc-ace306c68908 | -10.80495 | -50.77618 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 874259f0-cf12-31d8-856b-419e218813fa | -9.82372 | -48.42463 | 2026-09-21 00:20:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b4089b85-2560-3b14-ba02-a24d28f060bc | -10.58631 | -57.47841 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 2151eb62-d1e4-382c-b172-80802c817798 | -9.68771 | -54.33634 | 2026-09-21 00:20:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 35807ca5-17cb-3088-ad70-1e05c1e77c67 | -11.38364 | -51.44404 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 74140913-4e6e-3a85-8f15-306902a69a6d | -11.01799 | -54.15602 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6a97ca58-0606-38bb-9a53-2a3cf0de1246 | -7.71541 | -49.39607 | 2026-09-21 00:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 6820a34c-4a4a-37f4-a788-e79923579abb | -11.27263 | -54.12844 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0c641291-f2bd-3c3c-9186-3a20b8021775 | -10.86834 | -54.07989 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d071134f-89de-374f-84c0-fe34518a6906 | -11.04315 | -57.23219 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e19d5308-dba2-33d7-822e-d90d34de3128 | -7.71309 | -49.38103 | 2026-09-21 00:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 238873df-ae5a-3cf8-9df2-b09adf5b72c2 | -10.88296 | -56.23885 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| ec53c005-eedb-391c-8509-0214d0b67b8d | -10.74654 | -50.80304 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 764209bb-8df0-3e39-9984-685fa3267f85 | -8.17187 | -54.77255 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 9fb7bb49-6861-3967-9e31-bbcedaa48474 | -10.7807 | -50.81387 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 511401bf-09df-314e-89f4-69f733af55cb | -10.67614 | -48.72429 | 2026-09-21 00:20:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1900fbe5-5160-3c1a-b847-91a7d32d05af | -13.27246 | -51.7513 | 2026-09-21 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f28e78bc-9089-393f-85ba-6eb366720369 | -12.67644 | -50.95349 | 2026-09-21 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 32fda10d-f547-3174-90a2-03fa6f9ce2ab | -8.45115 | -46.41087 | 2026-09-21 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 71243d82-ec32-3d84-bc73-d0d8b6a8d9b0 | -10.87202 | -56.22955 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 255c4b35-b096-335f-8437-7489621bbf7f | -10.44323 | -50.34647 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c6fcd9ac-2f4d-3462-8c93-0833ae3d0b27 | -10.41101 | -50.33282 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 67df011d-b6af-3e7e-bda3-966b3cf2477f | -7.88095 | -54.7319 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| add935c4-9846-3f30-a9dd-c2840249cb7b | -8.16149 | -54.82848 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f7c147fe-869a-3f1e-8af8-433dac31c7e2 | -10.38457 | -51.87666 | 2026-09-21 00:20:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| cab31da1-14e0-3e54-ae86-781f81e1bce8 | -10.75628 | -50.80152 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0a36722a-15dd-36fd-b084-7fa8189cda4a | -11.7976 | -51.11956 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 55f9dcbf-39dd-342b-8369-788b00d1a10b | -8.62028 | -55.2262 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0e53c9b-747e-3826-85d4-68b8eaddb1aa | -8.30807 | -46.00671 | 2026-09-21 00:20:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 0d44a9a0-6080-385f-adc7-a7d2a88a4e17 | -11.02438 | -54.13681 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bf48918c-37ed-3aff-9dfc-6d54831e7778 | -10.05888 | -50.24596 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| b32bee27-a3e3-3a4a-88ac-2994880b7c72 | -16.04186 | -52.97269 | 2026-09-21 00:20:00 | TERRA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2ebcb51b-f7c4-322d-a3e7-f3990895569d | -10.81409 | -50.15323 | 2026-09-21 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| c5c751e7-0d50-3d75-9754-7defe58bbe5d | -13.26123 | -51.80162 | 2026-09-21 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 89f5da02-41e6-3e6a-91d8-c37345128621 | -10.87915 | -50.9439 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c09bdeff-eeec-3188-9568-43f3e8101a65 | -12.88735 | -52.09058 | 2026-09-21 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 76e9860a-3b0e-3c46-9489-6c41e826ec7a | -10.79927 | -50.19263 | 2026-09-21 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f8526f93-18bf-3f1c-9981-9a76aa4f4ab3 | -13.8716 | -48.58461 | 2026-09-21 00:20:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 3bfca62a-3a18-351a-86e6-a53fcace5c9b | -11.05333 | -54.151 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 62bd0bcf-ed95-3c8b-9428-34948def0553 | -6.41857 | -56.10587 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7786a6a5-e10b-358e-9d71-762a2b82bd61 | -3.78818 | -60.74622 | 2026-09-21 00:22:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 50ba8bfe-a830-37fa-825a-97816bd7a93d | -3.4872 | -59.60778 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| f3d7e7d3-8c4b-391f-9540-a59f02a28701 | -3.47452 | -59.59559 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f4186c84-49b8-3d63-ab3b-d3fb312583f7 | -4.403 | -55.23588 | 2026-09-21 00:22:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f4a2e67d-b62c-3e27-af12-9c29d8c44d38 | -3.49246 | -59.56537 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 8427194e-a9e4-3fe8-bc19-1925c3280a99 | -6.73194 | -55.09026 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| a85c3065-a107-3ae0-9a15-425f715ddd80 | -6.20915 | -53.5713 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8b561e78-a9c1-3166-9ef1-7d6047938770 | -7.59209 | -57.6923 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| dc014a24-3dbc-38cb-ad0d-41d3d1508526 | -6.10115 | -57.62837 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 418ec7e7-813a-3537-9201-ef98070f7ee0 | -2.88026 | -57.78445 | 2026-09-21 00:22:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e471ca08-8fc9-3d19-bdee-94d604cc8d7c | -3.05814 | -61.27296 | 2026-09-21 00:22:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 916d4212-f2e2-381d-80da-7cf9353f4c25 | -5.97541 | -55.35913 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8bd14298-faf9-3c0c-aaad-c8de1e0ac65c | -3.64223 | -58.87143 | 2026-09-21 00:22:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bf663cdb-a3c6-3969-88b4-c9db548c6d15 | -5.8368 | -53.5466 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 54c0efb8-719d-36a4-948f-5dab0c6db9fb | -2.90136 | -54.18329 | 2026-09-21 00:22:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bfe1de42-7f75-30ac-aad0-343fc331b3e4 | -5.01764 | -56.10009 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 9e768098-bd43-3082-a5f3-14c21ccef23d | -5.7691 | -57.58073 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| f09db1b8-de56-3b43-b330-af4178b644ca | -3.49432 | -59.57897 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0b8338a8-2c07-3ee6-a0f1-87476ff06cbe | -4.87822 | -55.88546 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3236921f-1f36-3c0a-98a0-7723472e872b | -3.6699 | -54.27525 | 2026-09-21 00:22:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b66d961d-0c53-320f-87ee-24689095df1a | -6.11999 | -57.75491 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 4bcb615e-6d6f-35ab-8a4b-ca78fda5ca6f | -3.34774 | -59.85165 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c661d8d4-3f04-3699-8a4e-851696bb8092 | -5.21205 | -56.10758 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| a5c10313-41b6-37e2-a444-69a10bee3e4c | -4.94274 | -55.81567 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0c7f3645-2d39-3c38-9e8d-e85960a79047 | -6.72312 | -55.09152 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| b964f4a7-7385-329a-87a0-7c8aa2b0182e | -6.61935 | -50.06382 | 2026-09-21 00:22:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2ea55c9d-7be8-3623-9e4f-b5692e6c690b | -6.77786 | -55.49371 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e31085b5-78c4-347d-8d2b-1fb7dc1b241e | -7.57764 | -57.65895 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b16844ac-dd87-31ad-8e91-43fa78812335 | -7.32895 | -55.21535 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 37bee5da-7d8f-351c-9d7c-b6c8fa5b1c7a | -6.30984 | -56.05166 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9b9577a7-2ca9-3e88-bcc1-4c96ca95df3c | -6.15499 | -57.71618 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 82af6480-fb43-3f3b-88f4-87a175adf9e3 | -6.66283 | -50.89858 | 2026-09-21 00:22:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9320cbad-bef5-3835-802b-17938b70aeb8 | -1.3266 | -54.66264 | 2026-09-21 00:22:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3b164640-8bcf-34d5-9085-302a71d3c672 | -6.77964 | -55.64117 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8524bf69-6169-3504-956f-51e8f880f930 | -6.31559 | -60.01732 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 069a25f5-ccad-3105-9986-4f070ef49870 | -3.01018 | -54.17101 | 2026-09-21 00:22:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 85df9a3a-0fb2-3249-be10-50bc245d332c | -1.48052 | -49.00494 | 2026-09-21 00:22:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 235ad4bc-dd20-3b42-a24e-d62eba3d1415 | -2.85789 | -54.20467 | 2026-09-21 00:22:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 79a98923-8186-31a6-9d1c-66dd840530f9 | -6.43811 | -59.97871 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 796e09c3-3a60-3be9-9577-a93934837836 | -3.6168 | -56.84397 | 2026-09-21 00:22:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| af8f5aa7-f2a3-3f01-9d43-2213e4d0816f | -3.61472 | -52.19024 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c5c65b43-e975-31af-9a0d-0be09b32f4c5 | -4.09623 | -52.12502 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a504a7dd-f3f1-3490-a457-b4bcd73aed4d | -5.20184 | -56.09968 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cf5266d8-a261-3b35-9172-1c369be8cb95 | -1.35411 | -49.30426 | 2026-09-21 00:22:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| bd599785-e130-3db7-bd9c-177486adfe83 | -6.74198 | -55.0979 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c6402046-93b8-302f-856b-26c9f0025275 | -3.54715 | -58.69497 | 2026-09-21 00:22:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d6b07dde-c587-3f56-b0f7-4326e78d7037 | -3.48164 | -59.56682 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 97b0708f-cedc-338a-8ce4-1ec25d8f94db | -7.244 | -55.60181 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 46973227-791e-3333-93ad-2216a46df33a | -2.42204 | -57.13239 | 2026-09-21 00:22:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5e072c85-f109-31ae-8928-003366daa95c | -5.83801 | -53.49019 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d66bccf8-8510-33b0-89d8-305ca86d0480 | -3.65415 | -58.88224 | 2026-09-21 00:22:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 84f21aef-cb3b-37b0-aa28-c881af3eb3ca | -6.20786 | -53.56219 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 3f134478-b275-3eed-8c9d-a273370bc754 | -3.40302 | -59.58305 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7981feb7-7d4b-30a1-a7c4-1c3834110345 | -6.92784 | -55.65148 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3bb304e5-ffd6-361e-922c-2cd00b79e699 | -3.01144 | -54.18013 | 2026-09-21 00:22:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 385a7901-7fac-3462-8856-74a0e40d728f | -3.60721 | -59.05894 | 2026-09-21 00:22:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5046bcab-32b7-3628-9456-6e0a29af134c | -6.11914 | -57.76081 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bc13a38b-d1e9-31b8-a39c-ded15133f537 | -5.41717 | -60.21835 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 13f88a67-4eb3-3171-be84-760ec97e1af8 | -6.44983 | -59.97704 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| f9173680-5d57-31ea-aa4f-6b2889fc2bec | -5.92344 | -57.67511 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |


[Clique aqui para ver as próximas entradas](README7.md)
