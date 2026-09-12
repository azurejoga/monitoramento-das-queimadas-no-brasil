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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70c4ff3a-a4a7-35a5-a50a-f38d4875dbcd | -6.03953 | -52.21978 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88124664-4ad7-30d2-bd98-484dda10844e | -11.36826 | -46.80072 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 168b9ce4-db5c-3fc1-912f-6b32c0573486 | -6.76393 | -59.42974 | 2026-09-12 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b646d27-0477-335d-b237-78098aa58246 | -6.20165 | -55.26692 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b7dc939-47c8-347d-b9ec-4ea10ff65513 | -9.4639 | -54.93082 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88968bb3-c3f7-3231-a47e-47a6ce46cc66 | -6.88608 | -55.65842 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f062dec6-75b5-391b-9efb-a0d0bfc26539 | -7.196 | -45.92414 | 2026-09-12 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 006f1e87-c7c9-31c4-a377-0470ad6d5f38 | -9.70183 | -53.66616 | 2026-09-12 05:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c30731db-a778-3096-a35b-d5067ecc9d08 | -8.61288 | -55.21682 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aad839f-6ce9-3947-880a-1427bfa6a0a3 | -11.81659 | -46.37398 | 2026-09-12 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8d40573-9fb6-3595-a490-212f3eebd7c4 | -7.96167 | -44.0027 | 2026-09-12 05:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e72f3b55-e8df-3a9b-89a6-3860b82ba4c1 | -6.23479 | -51.69714 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0dad9e6b-49d4-3022-bf3e-61449fc5d203 | -6.854 | -55.25187 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 745fa593-3926-357c-85cd-d789fffbe8af | -9.54911 | -45.47738 | 2026-09-12 05:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4568e234-24f4-372c-a3b6-7e18a6300180 | -6.19943 | -55.2593 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 387bf1b6-0505-337d-82e9-94c6e0f4e210 | -8.53618 | -54.71754 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 320803ec-bb84-364f-8532-4ed6e65b90cd | -10.35019 | -48.09236 | 2026-09-12 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a97bd127-ce40-313c-afc7-a16e544b6107 | -7.92655 | -49.73435 | 2026-09-12 05:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0935851c-6123-32fc-a278-073f1b9f9df6 | -2.73446 | -57.6394 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6eed1715-3c22-372c-8cbc-b736791fc6dc | -5.77721 | -45.09706 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5c8cb3af-795a-3c2f-9aed-8225f7269a21 | -6.116 | -55.64629 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0521c007-7789-390e-b8f4-ae8af5b765c8 | -9.93717 | -48.51912 | 2026-09-12 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5947dd7-2820-3b27-9069-df2419598d7e | -6.23598 | -51.68931 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e9e5042-19a3-3437-806d-3c543e9c3686 | -9.36726 | -48.41866 | 2026-09-12 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b220eb02-be6c-3cfe-a99c-419938646b01 | -11.41668 | -43.94305 | 2026-09-12 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d40aa6d-470b-3177-878f-afd50e5038d9 | -10.55325 | -45.19946 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e788a84-c80e-34d4-bc5f-fac63b55652a | -2.72523 | -57.64766 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51785ae5-f471-3358-ab04-911e034099a7 | -2.72676 | -57.63815 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92662826-7869-33e3-b44b-8a756efacfd3 | -8.4967 | -54.65062 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62350d7f-a654-3316-a2c9-9afc12cc7477 | -5.84835 | -52.05744 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dda3f37b-0228-3530-b872-11ef1bb4fa6b | -7.96224 | -43.99855 | 2026-09-12 05:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31c12a4d-f9ca-369c-a1d1-890b2b01751f | -8.57655 | -54.57023 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a917700c-64a8-38b2-bc54-4a612fe3bcf0 | -5.77619 | -45.09332 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ec016b98-df0d-3f00-91cd-82070e1b375e | -8.1117 | -54.79259 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d815bb8-206d-323d-a1ac-ba9da30467f1 | -6.10673 | -55.65641 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 579008d7-9f97-39e3-9d2a-64bd735d2405 | -10.63641 | -46.11657 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dea5221d-b2bc-3e15-9690-69839b01bba1 | -5.37356 | -56.025 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8119f91-6a1c-349b-956d-f81e3fdc399b | -8.57545 | -54.57721 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4bf3b74-c383-3759-a145-ef1f4f44dd82 | -7.42389 | -46.15424 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e98e499b-3eb0-37c0-bb72-de2daf18d303 | -10.55077 | -45.21829 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| accd2055-b71c-3411-a74b-c48cc9965381 | -5.48367 | -45.12671 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a96b025-7037-38a9-831c-d245b546f92d | -6.87725 | -55.62752 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b67eafe-f380-3457-987b-afc56e855505 | -6.11577 | -52.24194 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9454aa62-eb67-3cac-93ed-5579564b557e | -11.5395 | -44.8955 | 2026-09-12 05:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a527724-a924-3334-8d2c-92f73cfbb23b | -4.86647 | -56.02193 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfa81a4a-442d-3448-91fd-3121537ef5c2 | -5.77284 | -45.08979 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1f6bac36-0820-3715-a8df-49e9ddfdcb5c | -9.18742 | -59.44982 | 2026-09-12 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2800bb8b-d757-359f-84a0-0d63a2d5ad79 | -2.66919 | -57.50798 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e222f336-67a6-328b-a777-a25b74250ac2 | -6.12277 | -55.64741 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efb8a85d-fbe1-3f5e-b96d-db84a7e57ca7 | -7.42347 | -46.15722 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a24955fc-7060-3b37-8245-ec3cad305d9d | -4.36416 | -47.77992 | 2026-09-12 05:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 3065e263-9ec2-3c20-8d09-d5dd736855eb | -4.53969 | -54.93396 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 289f9b38-6934-3baf-86cf-600571e004b7 | -8.32162 | -54.7693 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9707d437-ea32-319b-a744-92459a84989a | -6.20222 | -55.26339 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ab4c70f-64ec-374e-8f8a-a38086e7f0dd | -8.58043 | -54.56727 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d21fe1c-ed94-34c0-8b68-6f6533f17c82 | -6.11778 | -55.63536 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f50a025f-7fe1-39a5-a47e-867eaf2dd8cc | -5.61378 | -44.84795 | 2026-09-12 05:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d19812b7-7e8e-3452-a004-321dc4ba929b | -10.55276 | -45.2032 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34991cb9-5fdb-3bf6-ba35-e16e3a0ecb18 | -7.96055 | -44.01082 | 2026-09-12 05:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1947f8f-7cf4-36a0-abc3-c164c5aaeb3d | -11.37884 | -46.83943 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c84da0d2-06d8-3f26-9625-2535be4c0617 | -6.88329 | -55.65428 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99c4720b-ee2f-337d-9df2-8736ffb61d70 | -9.70111 | -43.39877 | 2026-09-12 05:10:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1ca6f3aa-a11f-3a3f-8681-b4a1bb08aca8 | -9.0358 | -49.81537 | 2026-09-12 05:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f45aba3e-a225-39ed-a9eb-ef91ec641fb3 | -5.48323 | -45.12976 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 688d0055-5e82-340a-9f03-91f3d5c05186 | -4.52841 | -54.96132 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13b040b5-09c3-3569-a9da-9c13223ff13b | -10.82354 | -50.58927 | 2026-09-12 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72fee8ec-8162-3a03-9f84-00cc410785ba | -11.37844 | -46.84246 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c69f91cd-9640-3189-a40f-8215e08d1f67 | -6.20279 | -55.25984 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8201d321-b922-38e4-b486-efb7f61c2b28 | -6.95547 | -44.54422 | 2026-09-12 05:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0c7870f-224c-370c-b658-19c3c45f9195 | -8.07116 | -54.86133 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7f3d851-aba2-3cf9-9155-39c1f875c6ff | -10.53836 | -51.3677 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d916e77f-4648-307b-ac09-0cd1e81bf98d | -7.70476 | -55.37048 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fda77ba2-6a82-3850-b3d5-5063f4acd327 | -4.52227 | -54.95665 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 823447a3-ba75-3937-b64f-32a8d5522405 | -6.50683 | -47.59919 | 2026-09-12 05:10:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef9caabe-368d-3d22-906b-da423615cd09 | -10.22579 | -50.37016 | 2026-09-12 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e2ecb79-ee70-3f20-96ad-8f7d573f4b48 | -10.51376 | -47.90126 | 2026-09-12 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0734590a-887e-3f55-891c-80b70e1053a1 | -4.52505 | -54.96078 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 921ac4f9-c9d5-3cc7-b540-204e58096602 | -5.81983 | -53.80147 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ce16b04-ed14-3126-b0ff-09e1e84fb50e | -5.37071 | -56.02069 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78553bc9-306e-3978-989a-7bd94875cf24 | -4.98225 | -56.13007 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf037f46-d5d7-3b7d-8a26-44521d0004e5 | -8.11447 | -54.7966 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c94e80d3-c6f4-3c55-8805-d6dc106200e0 | -6.66672 | -50.91397 | 2026-09-12 05:10:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04367ffd-91bf-3a67-a77f-f18b8a63814c | -5.85317 | -53.87074 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 403942f6-1e62-32bb-b8d9-644df71c4f86 | -6.07433 | -53.49565 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac561978-1593-321c-800b-8d620a46cecf | -9.23337 | -51.73643 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2c81c58-769f-34fe-9b64-ff067826bf68 | -10.68906 | -54.16341 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a84b6697-5997-38e0-95fc-d68572ff7bde | -5.85262 | -53.8742 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1897ee09-0b81-3810-a449-aeeca68f7dbe | -6.11186 | -55.64603 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 755b4b84-6f1e-376b-8482-8e2f00d4be03 | -9.70451 | -43.39862 | 2026-09-12 05:10:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e1356b85-5d41-3c1f-a590-2a2b75f21ac5 | -5.85832 | -53.87479 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 157cb458-8ffc-321b-9016-ecfc9865d70e | -9.64211 | -49.6792 | 2026-09-12 05:10:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4144e1cc-614a-37c5-a91c-61c33588ee08 | -3.75572 | -61.19669 | 2026-09-12 05:10:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f8a6640-1453-331c-bf37-daa5c7c9006c | -6.06875 | -53.48764 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 252ff2be-c8d1-3685-916e-1761aea60e40 | -10.56007 | -45.20831 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4db11e2-5192-357b-a951-946ab034b343 | -6.84899 | -55.58295 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04c0f7c6-5d5c-30a6-8d74-2d40fae833e8 | -5.9599 | -45.96513 | 2026-09-12 05:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 946c2b34-aec0-3ed7-89e4-48f58b283734 | -9.18655 | -59.45481 | 2026-09-12 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7da3c5b8-5665-37c9-af45-71ba1608ac87 | -3.87882 | -51.1833 | 2026-09-12 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e34593f-b2f8-32b1-87af-73e013e6ab5e | -6.61641 | -58.84696 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd9e4657-5906-3a40-8579-430faf1fc4d5 | -6.62081 | -51.14511 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README38.md)
