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
| a21cdc41-49bf-31c6-a6d3-a85052188088 | -12.49073 | -48.03485 | 2026-09-13 00:03:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3e54f5ff-2193-3a14-9f31-5f86189323be | -11.84209 | -46.39932 | 2026-09-13 00:03:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7e584b48-d318-3a8c-b3b1-5e1df3dc0cf3 | -10.91924 | -48.3406 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bc591061-d5d9-3166-a48d-d072486f4808 | -12.12275 | -48.97924 | 2026-09-13 00:03:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2379aef7-cc21-311f-96f4-30e2edbe993b | -11.04066 | -47.17335 | 2026-09-13 00:03:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0989eb34-0a77-35c8-9035-1c337a1afb1b | -10.33859 | -48.00853 | 2026-09-13 00:03:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 11cef0a3-dc59-3c7d-941b-8028b1e885ab | -10.69291 | -54.16079 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.2 |
| ce7a860e-628a-38b4-8b01-3cfdd2713210 | -9.81513 | -43.4808 | 2026-09-13 00:03:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 8378f72e-af71-322b-aa45-a4ded46511a1 | -9.36431 | -50.09144 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3a95e9c6-9e0d-386e-a7bf-a939f2e4f4d1 | -10.94763 | -57.18091 | 2026-09-13 00:03:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a42b5b2e-38f5-35bc-b63a-034de5a95a2d | -12.67019 | -54.66228 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 3e6252d2-8aa2-33fb-9b99-ad206e3193c9 | -12.67522 | -54.74211 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| e383bdc6-6df7-36f6-aa7b-d68eb7c611a3 | -14.95389 | -47.52642 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 942a62e2-ec2a-35f6-9cd2-23fd765c550f | -9.37437 | -50.09916 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2215e2fc-83e8-3ca8-b481-9de9fea430e3 | -13.29694 | -51.72136 | 2026-09-13 00:03:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| adf4483e-32c4-3668-9cdf-18577cff0f64 | -15.5655 | -53.79054 | 2026-09-13 00:03:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e3b42855-5975-3feb-8fb6-798fa67f04c4 | -10.45771 | -48.65955 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 323d202a-3777-3719-95bf-67c7564c71c5 | -9.91888 | -47.97783 | 2026-09-13 00:03:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 382c10d6-9e7a-3a3b-aa24-9af64cc1ecec | -11.08724 | -50.853 | 2026-09-13 00:03:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 190ac69b-8d20-3891-a015-2236ecdeebd4 | -16.98258 | -49.72809 | 2026-09-13 00:03:00 | TERRA_M-M | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 1121fb3d-70d8-32db-b7f0-7e547eab4e52 | -8.81454 | -46.91174 | 2026-09-13 00:03:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cac093af-c88f-306d-9ace-97688aca3449 | -12.49201 | -48.04394 | 2026-09-13 00:03:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 13727804-fa90-398c-ada5-b7b543060958 | -12.86167 | -44.3936 | 2026-09-13 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 783d27b7-5217-3e74-b933-12eda7181309 | -9.41711 | -50.14804 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 817b0dac-6c02-3667-beeb-f2812050909e | -12.69075 | -54.73355 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 471ac2eb-0447-3ce5-adde-32f3e63ddee3 | -13.55653 | -49.49328 | 2026-09-13 00:03:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5b43aff6-1150-35c3-bb58-691c7c78b515 | -10.96713 | -58.95401 | 2026-09-13 00:03:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 32729489-a55a-3a9e-ae41-c1583212d227 | -15.63394 | -43.33525 | 2026-09-13 00:03:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 91000ce9-a052-33c8-928e-704e6741da88 | -13.74916 | -42.61464 | 2026-09-13 00:03:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| d0db61d8-d0ba-3e41-8f78-fe94f869feb7 | -10.97946 | -49.70715 | 2026-09-13 00:03:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0338be91-050f-37a6-87a1-1b2c8dd147ef | -10.5278 | -51.36849 | 2026-09-13 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 09ee0aef-8b3a-3f1f-a7b8-50391be69b68 | -15.05529 | -47.1959 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 44f5d474-60b3-3771-99db-e329fd25c68d | -11.2506 | -54.14299 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c8465d6a-466d-3822-9727-a0e88dc4f4b9 | -14.82972 | -48.15242 | 2026-09-13 00:03:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2592ed3d-c1f3-3e50-9964-467dbea08021 | -10.82298 | -50.59975 | 2026-09-13 00:03:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fc9b7ebe-0140-3bde-aa67-6cc9100f37d4 | -11.81045 | -46.38211 | 2026-09-13 00:03:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bc96abd7-d25c-30b0-8ae3-d8b350786b3c | -10.46402 | -48.64022 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c6885833-b29e-3405-a82a-49950e40d757 | -10.09941 | -48.86386 | 2026-09-13 00:03:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e93dce52-dedb-3dbb-8eca-21ead6432244 | -9.41466 | -50.13007 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| aefb4c57-78b9-3956-8d01-2b58e92c4669 | -10.93064 | -48.35742 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0ba690f9-9541-3917-8e01-f25693e479ee | -10.95057 | -48.35762 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 001794c9-8edf-30ef-b611-c85ddac7a12f | -12.68751 | -54.74053 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| fb800a34-0c7c-3b95-82fe-112d15b8ec92 | -10.68365 | -54.18746 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8f790133-1a72-300b-8775-71fa83fb7b94 | -11.81202 | -46.39285 | 2026-09-13 00:03:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c172c7da-0dd7-344f-822c-21c87250ae91 | -11.06504 | -49.72591 | 2026-09-13 00:03:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9049b159-d2b3-3b50-9059-2eaa303e41e1 | -12.6607 | -54.72509 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 8848430d-f8eb-3943-ad14-90edb0fc01e4 | -10.89311 | -47.82339 | 2026-09-13 00:03:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a8f37da7-a73e-3214-a72b-b68f97c933ad | -9.37681 | -50.11711 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 56bd74ca-610c-389f-b533-3f2ab25dfdd7 | -10.08551 | -46.83715 | 2026-09-13 00:03:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0aa2bc50-468c-3b2f-8656-a909d1242ac4 | -10.75464 | -46.23827 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bad2f3b4-b707-34da-ab62-8a7f74317f6c | -13.7582 | -42.5944 | 2026-09-13 00:03:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 3d0330d4-0eac-3585-bb35-4a6f5766e4e6 | -15.55556 | -53.80919 | 2026-09-13 00:03:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 9a15dadb-4942-3f7a-9dfe-c5c1d7206e28 | -12.18012 | -44.02394 | 2026-09-13 00:03:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1f09e435-4c13-30b9-83e1-f31ffa40570b | -10.75627 | -46.24928 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 9da2d26c-268b-3cbe-91cd-f1a0333c2379 | -13.53971 | -45.66593 | 2026-09-13 00:03:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d99ba5c6-6a57-37b7-90c6-2be4f6143bfe | -10.68181 | -54.17204 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 350.5 |
| f96cc0fb-ae82-3386-863b-ceafcbb4d419 | -13.50534 | -47.19327 | 2026-09-13 00:03:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 86bb21b1-b673-304d-b11d-284024e8d81a | -10.50346 | -51.30544 | 2026-09-13 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c13eeab-38dc-384c-b6e1-eb89ad9c8981 | -9.59349 | -46.72285 | 2026-09-13 00:03:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5d61712d-ee26-350d-a338-01b6dd34a3c7 | -9.81791 | -43.49871 | 2026-09-13 00:03:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| e773adb7-5270-387d-9ca5-c0b097df0b46 | -11.35408 | -46.7853 | 2026-09-13 00:03:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c89252a2-fd4f-37e0-be9a-3e7eb5518984 | -11.62165 | -49.82268 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7cb9ac3e-b3a0-3523-867f-c10df53b83ca | -12.15069 | -48.96887 | 2026-09-13 00:03:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5e1090dd-22b9-3b5d-8852-b7f98817896f | -9.94815 | -48.50724 | 2026-09-13 00:03:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 239f29ef-d2be-3057-9adf-9e29757e334c | -14.83097 | -48.16148 | 2026-09-13 00:03:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7b30cb7b-48f0-37a4-a679-6633089f765b | -11.29413 | -44.1825 | 2026-09-13 00:03:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0bd96f65-d649-33d7-a0fe-6a9d4ec09d84 | -11.35552 | -46.79535 | 2026-09-13 00:03:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3e69db7c-92f2-36dc-9636-6417838fe710 | -11.81357 | -46.40339 | 2026-09-13 00:03:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 13ea1540-d02a-33e5-8ad6-ac914e9414e2 | -12.68057 | -54.75375 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 0784e590-d005-399c-aa4f-50d4de7f5217 | -13.81582 | -49.0863 | 2026-09-13 00:03:00 | TERRA_M-M | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bc932d73-59ff-3e79-9cdb-6b1163e2b6d4 | -15.57347 | -53.80136 | 2026-09-13 00:03:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| b4cac821-0b25-33e4-a489-c74028d88feb | -15.05396 | -47.18656 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a7d104a1-9346-37b6-a032-f64b9c0581fb | -13.10637 | -44.64013 | 2026-09-13 00:03:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9b1643ef-65bf-3951-a9e0-7b6a08a2a5b4 | -9.37559 | -50.10813 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 6218ef7c-1d2f-36ff-a139-2935cb73bbc1 | -11.72264 | -46.73955 | 2026-09-13 00:03:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 7e11435c-356d-3ff3-a561-2c62d376756b | -14.96274 | -47.52503 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 74cd5c91-6774-3b40-bc61-feff9c3b0549 | -9.41344 | -50.12109 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2a990bf1-85da-3052-a5af-d4490b4b32b4 | -10.31248 | -45.28055 | 2026-09-13 00:03:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 435ec472-a3ef-389a-ba3f-38d5d2ce5a74 | -9.38566 | -50.11586 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a42ce07c-560a-335b-9145-4ee3eb5b4288 | -9.8477 | -48.52487 | 2026-09-13 00:03:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a2b83792-f65f-353b-ae6c-9bd4ca35b8b2 | -10.51161 | -51.3663 | 2026-09-13 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f95a53c3-922a-3d61-9683-aa3a26d31732 | -10.55177 | -51.33385 | 2026-09-13 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 47e056ad-65fa-39f1-b6b3-2accebbe2821 | -10.95944 | -48.35636 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2a3f363f-d4c9-3dbb-ab1b-3f7eff36acbd | -10.53709 | -51.36682 | 2026-09-13 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 8f5f7580-ac7a-3041-9938-5dda9d096fac | -12.67296 | -54.72344 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 683a1f4d-3e09-3a17-824f-e0ee431e2abc | -10.30212 | -45.28276 | 2026-09-13 00:03:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 91799004-2078-3914-b7c7-4f49d5de073a | -10.94597 | -57.18748 | 2026-09-13 00:03:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 09ec11b2-0c3c-357f-9b8c-c01f06b78f70 | -13.75399 | -42.60167 | 2026-09-13 00:03:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 135.3 |
| 0005560b-e31c-329d-9821-3462d608f509 | -10.45645 | -48.65056 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0ba17673-d3cd-34a8-b033-130ccecf9797 | -11.34476 | -46.787 | 2026-09-13 00:03:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 00bd6255-9406-3979-87bb-14de58f9678c | -13.61248 | -47.88701 | 2026-09-13 00:03:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c751ffd0-caa1-3d46-b139-b409f630b2b3 | -9.40581 | -50.13132 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e43b4f48-a980-3a17-ae60-de84f89dad57 | -11.34644 | -48.16338 | 2026-09-13 00:03:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cebc537a-52e8-3ead-a5f9-ed07b7389405 | -10.95959 | -58.98544 | 2026-09-13 00:03:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 152cb1d3-425d-3b93-9565-b2cffd910417 | -10.52649 | -51.35835 | 2026-09-13 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 03b04bc0-8d09-3daa-893b-a9360e499e38 | -12.67844 | -54.73499 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 206.1 |
| fcbb8896-dc04-301c-95b5-f47662c12f15 | -13.81459 | -49.07719 | 2026-09-13 00:03:00 | TERRA_M-M | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 23547f29-2492-30bc-afaf-37abe866c276 | -12.66406 | -54.71799 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 2d95f9b7-95cc-3cd8-8ec9-e0af4f7b622b | -14.82218 | -48.1628 | 2026-09-13 00:03:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3067f0bf-1976-3961-9f60-c85eacf19750 | -14.82092 | -48.15373 | 2026-09-13 00:03:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README3.md)
