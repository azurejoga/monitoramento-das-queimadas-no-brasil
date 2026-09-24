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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 943c098b-3666-3ea3-b907-5a19ce65d91d | -7.67494 | -45.49184 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| acf09e02-438d-3e74-942c-7479abea94ee | -3.15677 | -50.82965 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 78d02a6f-bbe7-34c0-b86f-9b156433252a | -7.20109 | -47.45808 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5c2aa808-5dd2-3c4e-9c9b-549cad665cb6 | -6.33428 | -49.86524 | 2026-09-24 04:44:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e81168fa-0911-3c78-aa4f-037c4acba512 | -3.04081 | -51.33314 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08d85776-00a8-31f0-af39-08be0860485e | -2.88734 | -54.08281 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 242d57fe-14fc-373d-86c6-5f71e956541c | -7.41912 | -44.81073 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f3e0f19-e9f2-316d-8cb8-7acafc27b9fa | -1.62062 | -54.91618 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3d7be94-b69a-37b2-bc0e-a22ec4a78c6d | -0.93783 | -47.5528 | 2026-09-24 04:44:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 09bc1f10-b021-3117-8251-f0a784e527ea | -3.44875 | -50.08993 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c7d350f3-0a5b-34d2-92fb-a2bb37802f6f | -7.67392 | -45.47505 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d6cb5de-9bae-3bac-b278-f607f1622a02 | -3.70911 | -54.20821 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 366d1862-742c-3a65-8dc6-23ba1a29cc6b | -3.17824 | -48.01283 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9dae4ff-a340-3c75-88a7-7149765e2888 | -6.60747 | -43.73389 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2950084-d7ba-393f-858c-c28ef16d0e93 | -1.84141 | -54.71803 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| abc869f7-5697-3ef4-aaed-dd6cebf0d03e | -3.95889 | -45.81127 | 2026-09-24 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7805f84c-8aef-3fed-b570-bc76a631f71f | -2.82522 | -46.70629 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0b762cd1-f669-3fab-a044-b248b8dbb081 | -1.39264 | -47.94623 | 2026-09-24 04:44:00 | NPP-375D | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cf5a76a-128d-3db5-bae1-e57694bc04cf | -3.04058 | -50.26605 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90968e74-4fce-32ba-9516-ba52219b168c | -2.79816 | -49.40453 | 2026-09-24 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d60dc5dc-661e-3332-87b6-3593257ab756 | -4.28867 | -55.26511 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1cac116-25a9-3ba5-b411-30ac428414e0 | -5.83606 | -53.85199 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf7bb053-d201-3660-a295-f51f27e89d72 | -5.2256 | -49.22367 | 2026-09-24 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8172bc89-36fa-320b-adc3-785503f6f540 | -7.67809 | -45.47153 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 924f3d0f-b33b-3eaa-9061-e1acf6599968 | -4.65753 | -54.47332 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 300b4ff8-276f-32c8-b647-d88b7e7331c9 | -7.77542 | -44.76767 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50678cd5-7540-3729-8f22-f4fb229b2e56 | -6.21187 | -47.44526 | 2026-09-24 04:44:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a59d05e6-9018-372e-8692-d35ad7f4bc2e | -3.55867 | -43.46383 | 2026-09-24 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a01a491c-921f-329e-b844-35ffc51dbaf1 | -6.57973 | -44.14428 | 2026-09-24 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5e3cb47-8a87-378b-ab65-4ee8242f28eb | -3.09123 | -49.35403 | 2026-09-24 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fe7c769-2701-3b53-ad4f-0d911c2ccbe3 | -3.67865 | -60.58748 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4774257c-35c3-3699-bf76-86eae3a5f400 | -6.33663 | -43.36129 | 2026-09-24 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f66606a-ce68-3297-98d4-7d28f5fc6178 | -3.17655 | -48.02336 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 790238a3-ec6e-355c-a06f-876a97ce7b64 | -7.50521 | -39.2733 | 2026-09-24 04:44:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7bc3c17f-a44d-3e0f-8d31-024fb99aa507 | -6.31415 | -43.79342 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da34062b-849a-357b-87c9-256499d07efc | -5.83469 | -43.06182 | 2026-09-24 04:44:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82bacb09-cfe3-38b4-bbb1-9f6afed2b18a | -2.74267 | -51.54436 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc157f3b-af4b-313c-8abd-4d0954a4c13a | -5.67635 | -45.98357 | 2026-09-24 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68c7a77d-b83a-3dfa-bbff-301dc7a41850 | -6.54414 | -43.08816 | 2026-09-24 04:44:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc6636a6-9d66-3058-8d8c-04ae7eaa478f | -1.1624 | -54.20243 | 2026-09-24 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 970b2ca3-41c1-319d-a517-4ae037918cc4 | -5.0002 | -45.55185 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3af66a57-59ad-37c9-ba0c-f3b3b55da82d | -3.22852 | -54.32135 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42cd2042-184f-312a-a788-aa59edf2b3c1 | -5.98933 | -44.42464 | 2026-09-24 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2f7d67b-5098-3823-808b-e2ff7f6218e8 | -4.11208 | -51.08047 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7cceac81-20fb-3025-94ce-f14a96037139 | -3.2348 | -54.32459 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d95d74f5-893a-349c-82a1-49bbb5b03958 | -7.19108 | -47.45655 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db1fb2b2-983f-315c-ae59-4ac55506d480 | -3.41823 | -54.01393 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a90d5c59-f4c0-3d63-b7ea-e6240878420b | -6.66606 | -52.32177 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f08e26a-20bf-3cf1-b3d8-6004c656bc2c | -2.17636 | -47.10304 | 2026-09-24 04:44:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7eeee4e6-1378-3aba-a925-650e9979bb62 | -5.79499 | -49.97176 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fab1055-7138-34d3-919a-87745fd80283 | -5.83679 | -52.00954 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 427e3298-6be2-3027-b76c-19dcd8ef8141 | -6.78111 | -48.67488 | 2026-09-24 04:44:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63603b52-02d6-326d-bd12-3f4d95c9bcf7 | -5.00078 | -45.54811 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| deba3f76-be68-38d8-a10e-35e6a5fd0a02 | -5.77305 | -45.09653 | 2026-09-24 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| edcabe9e-f345-3dc0-81bb-8118fc607195 | -3.76555 | -43.3995 | 2026-09-24 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38ea7bee-a550-37a9-adcd-67520d22d425 | -5.9212 | -42.98831 | 2026-09-24 04:44:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 346d9b3e-2b27-3bc7-ba62-80269f736d4b | -2.8912 | -54.08835 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec1d031c-c750-3c75-9366-397c04751c9d | -7.42313 | -47.35672 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d841df2-8210-3812-9dbb-2a451f79064d | -3.18382 | -48.0209 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3253a5bd-9827-3240-b2fa-73c62e8ad3db | -6.42908 | -48.46759 | 2026-09-24 04:44:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b584ac6d-f870-3495-a248-13965d4f6dc1 | -5.77597 | -45.10102 | 2026-09-24 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 656e3daa-2da9-3e7e-b23f-f02c5ec4c7ec | -2.29892 | -47.88887 | 2026-09-24 04:44:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5d844f6-f0fa-3ca4-a99e-96aef1e6cd56 | -7.46374 | -44.56684 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bbc468c-1cd9-3bea-a937-7c450cab6b64 | -2.88269 | -54.08204 | 2026-09-24 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f62de428-099e-3498-bbf3-62bb196cd1b1 | -3.44581 | -50.0853 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d358fd8a-c84e-31b4-a390-3fe5697af598 | -4.52703 | -44.03101 | 2026-09-24 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4553ba0-be12-3fc9-8925-b6572e614a65 | -1.33152 | -47.95519 | 2026-09-24 04:44:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 734b3351-cb5a-3bfb-aa85-6fb3fbc48531 | -6.89031 | -43.74358 | 2026-09-24 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6644348f-4dad-3fd0-9a98-3a784d31d9e0 | -5.19938 | -44.6871 | 2026-09-24 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 868ae0aa-a221-337e-9e71-5b930ace97f4 | -4.22284 | -48.61668 | 2026-09-24 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e42d6f0-3589-34f4-a7f4-f1ad46328c98 | -4.02301 | -52.06611 | 2026-09-24 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 57ed183c-05be-308e-b9c0-140c5fd38f33 | -3.55423 | -43.4677 | 2026-09-24 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7270c17-52e7-3fe1-9759-81d669c6b6ed | -5.78562 | -50.20475 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6216cc88-ec15-3243-b4c5-e51351fe554c | -2.88029 | -49.47606 | 2026-09-24 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a0158b7-cff2-3ec7-8995-254f7a943e09 | -3.41981 | -54.00446 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6ae7772-f83c-3fd5-b8f9-5ce3463352a2 | -3.36836 | -50.03278 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7530ae89-4f16-3b21-9ab0-36902a6e7079 | -6.72098 | -44.15534 | 2026-09-24 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| de2dcdd5-54f2-3d58-852b-b1a77c3a015c | -3.8573 | -51.9958 | 2026-09-24 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de1d94eb-460b-3ad0-abd2-03ca73676cbc | -6.33653 | -49.86503 | 2026-09-24 04:44:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b3db53d-ff55-3fd9-9db3-d9af0db68ae9 | -7.67453 | -45.49126 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0cd6de7d-0709-308b-8fca-e545cf2caa71 | -3.45721 | -50.083 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3ba7e1f7-436c-3d24-9fa7-cb1951e38b58 | -6.52737 | -51.50231 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80cb528a-d217-361e-a9be-29bde4ef1537 | -4.47682 | -54.96724 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db4b9156-e2d6-382d-9d58-b69c539c1ab5 | -3.55118 | -43.46269 | 2026-09-24 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b0f434e-62ec-3b95-aed7-835107a0f72e | -3.44607 | -60.57369 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f858e1fb-ccfb-3227-8c79-0300f9417cbc | -2.71083 | -57.50611 | 2026-09-24 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c52c00a-f0b0-3abe-8151-5952d8c54d63 | -5.76891 | -45.09988 | 2026-09-24 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 237330c4-a692-3275-9e92-2c820c0949e5 | -2.82854 | -46.70681 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 994fa4c0-7426-3d3e-a68e-d2312bd45877 | -5.45865 | -47.90591 | 2026-09-24 04:44:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 556cb7d1-a660-3f0b-83d3-794c74b584b2 | -3.45428 | -50.07835 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d84b6071-935a-3d19-832d-c8ba064a8c7d | -6.34249 | -52.74672 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37591a69-4b3b-3615-8807-ed0c8dad6bda | -6.89891 | -43.63195 | 2026-09-24 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a128e3f7-bb70-3e84-8d33-ee6fd29dde92 | -3.18269 | -48.02794 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e75af13-c84b-3afd-888b-6ee32722e041 | -2.33024 | -48.54985 | 2026-09-24 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c3fdb55-304a-3255-a06b-d3891f6474e4 | -4.50343 | -54.95573 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49001ee4-86f6-31df-ba1f-0bc3dd6f63c6 | -7.62063 | -46.80464 | 2026-09-24 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94bd1089-fc4f-3c0b-bd0f-c8d2b598f9d4 | -0.50449 | -49.15033 | 2026-09-24 04:44:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c1a4823-af50-3fcb-b579-eddf2d239f76 | -3.01289 | -51.53209 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13b04624-c563-3490-9f4c-15e3119d57d4 | -6.02613 | -53.89825 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61480d84-05b0-33c3-94b4-daafa10465dd | -6.33311 | -49.86432 | 2026-09-24 04:44:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README48.md)
