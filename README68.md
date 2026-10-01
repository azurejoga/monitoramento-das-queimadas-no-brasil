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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a32630f-89bc-34c8-aade-28e8c65eba88 | -14.88443 | -51.8729 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ee28d5e-a93d-3a7a-ad35-b1ebfe26bc67 | -16.42871 | -47.18118 | 2026-10-01 04:36:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3738544-c1b7-365e-8d0a-0248c0260a6c | -14.08513 | -50.36244 | 2026-10-01 04:36:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 946bb72c-d7ca-3593-963b-8b99f72b0eb3 | -18.48335 | -45.12756 | 2026-10-01 04:36:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd540c2c-4ebf-32d9-9ebf-5e7e3c98e6d4 | -14.39452 | -51.2654 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| d193dd6a-2b0d-30e5-9db7-5f683738be9b | -20.60353 | -47.02973 | 2026-10-01 04:36:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa4d0c1f-7694-3b24-aced-7e951f8de32b | -14.14423 | -51.13379 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 813bdf33-760c-3fc8-a5a8-4aaf01719888 | -18.47378 | -41.42986 | 2026-10-01 04:36:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | MINAS GERAIS | Brasil | 3163300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f80dc6e9-f864-3b2e-8c41-9a93dcb5f98f | -14.87004 | -51.84768 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f7523eb6-2de8-3db9-8971-8e4e1606bc56 | -15.45066 | -42.09944 | 2026-10-01 04:36:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2756c01f-2d09-36ca-98ee-427a6720203f | -19.23394 | -42.94947 | 2026-10-01 04:36:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 41a85008-9350-3d16-9a8d-ea540a31e648 | -14.38675 | -51.28971 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f611a195-a22d-30bf-bbe7-bffe3919d946 | -14.39808 | -51.26604 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| bf823f5b-c469-3e95-87f5-575211be9742 | -16.02347 | -45.12972 | 2026-10-01 04:36:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 576ffce9-2d38-3c16-a53f-4cdeecefc52d | -15.49605 | -46.12004 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d002906-a24e-3b7f-902c-0f869b9a9ce1 | -14.43198 | -51.2536 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3afc428-2bb5-3175-be38-bb6e2fddd083 | -14.87139 | -51.86147 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 512734db-25f8-30b0-a7ad-5c92bc45a30e | -16.13592 | -43.74523 | 2026-10-01 04:36:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c02b15ca-76e2-3386-b882-8dbc8b1f7ac1 | -20.18554 | -50.89835 | 2026-10-01 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6524dfcc-8721-3267-b994-3b72dba206a6 | -19.83731 | -45.02119 | 2026-10-01 04:36:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e952b22e-31dc-3dcc-a284-9d26fa631042 | -13.65441 | -53.93646 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 62620f44-b94c-3b84-a884-3eab9c08c29c | -13.6495 | -53.93969 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 70d6cc72-7d6e-3b07-a05f-b0958be8f1a3 | -18.48713 | -45.1281 | 2026-10-01 04:36:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 801065c9-a66c-3bcb-a727-5772faaa3306 | -15.23004 | -46.14123 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8de23025-4e8c-362e-b54b-fdbb940ff6e0 | -15.84846 | -41.70673 | 2026-10-01 04:36:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ae8ddf0f-d8a5-334f-b702-154027435688 | -20.60378 | -47.02864 | 2026-10-01 04:36:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c44b875-dced-3302-8bd7-c304ebdc068d | -15.77364 | -46.02779 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c433ee60-f2e1-3f97-9792-eab20dcd8cf1 | -14.87427 | -51.8665 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5947205-5233-358b-a3c4-58246928c451 | -15.23716 | -48.56493 | 2026-10-01 04:36:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19b346c3-4e7d-33b5-b7b1-d89fc268ecd6 | -14.13855 | -51.12428 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| edb7fe80-a6bd-3add-ba36-c374aef36315 | -19.22957 | -42.9488 | 2026-10-01 04:36:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1be4cae1-bb54-3ee4-a1c9-ac96f7ecc413 | -14.15413 | -51.1186 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a6fc9f9-20ef-3478-af5a-db3c96b116a0 | -18.8826 | -43.82823 | 2026-10-01 04:36:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e9ff17f-7a79-37cf-997a-d6a797bec598 | -14.41705 | -51.25517 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 780e8c68-117b-3849-a289-49c49de46e2b | -18.09748 | -44.416 | 2026-10-01 04:36:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fae36f0-2858-383a-aad2-fb96c731df33 | -14.39928 | -51.25196 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7170b669-4b5e-3d8b-a044-aad704d139b2 | -14.44265 | -51.25553 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 201896c2-94d2-3230-a9c0-255c6324610f | -17.53877 | -50.74888 | 2026-10-01 04:36:00 | NOAA-20 | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64647a1f-e9ee-3de7-8192-7d32e548fccb | -13.66624 | -53.94291 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 071c5424-6e8a-3eb4-8e40-5ddff2380ab6 | -15.25508 | -44.82092 | 2026-10-01 04:36:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29ba4f11-8848-3591-9ce2-fcab3da2af90 | -14.14988 | -51.12208 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf8770ce-64f8-3260-b2c5-e63abf60a9e6 | -19.03375 | -45.66548 | 2026-10-01 04:36:00 | NOAA-20 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1eafa6c-da06-3726-bc3e-848717192ef6 | -13.65788 | -53.94125 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 81713484-f77f-3c66-bac6-c6f96f8bfc54 | -16.4321 | -47.18173 | 2026-10-01 04:36:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 471d2a24-2049-323b-b354-00f8223409e2 | -14.39568 | -51.2727 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5bcd31a6-2f06-3570-aef8-132140373ef2 | -14.4963 | -48.30999 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8523682-3d71-34da-947c-badd40eb1dc0 | -17.651 | -39.66548 | 2026-10-01 04:36:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 41d6ca87-824f-3ffc-92f0-a4d05f2f714e | -14.39522 | -51.26125 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 716c90ef-9b16-344c-8eff-17ba6fbc5e4c | -20.11229 | -44.39836 | 2026-10-01 04:36:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a7185a43-0830-3391-9019-561321caf482 | -17.09093 | -46.81996 | 2026-10-01 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a0bc065-fec2-35f7-8c2c-0d505492a033 | -16.13658 | -43.74031 | 2026-10-01 04:36:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba7cb7b4-3895-31da-9d86-5f176b843f9c | -14.39573 | -51.25132 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ffa1b31d-1d52-387d-9925-b68ffb663bd1 | -16.42081 | -47.18761 | 2026-10-01 04:36:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a29ceab5-8410-3f05-bcd4-6af29028b815 | -14.38605 | -51.29388 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 44bbbc27-0d9d-3044-980f-d153d5d3b8cc | -15.85239 | -41.71224 | 2026-10-01 04:36:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 70774620-c844-3c89-97b8-9fda5e5643d6 | -14.38535 | -51.29805 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a97b50f1-593f-31b1-bc9f-89ab784f95cf | -15.24945 | -44.83393 | 2026-10-01 04:36:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b28456fe-ba6c-3b1f-a114-9302cc7da5ad | -14.42487 | -51.25231 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8de40c62-98d1-3dc1-9dd1-1f9a722ccf4d | -15.15943 | -46.12705 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 28858d4b-bc19-3231-bc74-5daed0ae9964 | -15.95517 | -41.89494 | 2026-10-01 04:36:00 | NOAA-20 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1258bcc2-237b-32d7-b03f-32f0c462f712 | -18.88217 | -43.83152 | 2026-10-01 04:36:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5521844b-d675-31d5-ac13-3f529c2e7108 | -14.39662 | -51.25294 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| f15fbea0-30fc-3b46-81e9-aefb766b3f08 | -14.14708 | -51.13855 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6e99da39-2ce0-34ee-bb38-6156628919c2 | -15.23351 | -46.14178 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2274419-ed04-393f-a2bb-e8380a7f002e | -14.49299 | -48.30944 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee8b8973-4897-3db9-ac35-d10043883547 | -14.86775 | -51.86079 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adae81d6-f070-383b-8eff-2f8ea201c306 | -18.88105 | -43.83114 | 2026-10-01 04:36:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da98879d-edba-32c7-a00e-49107d016c5b | -14.41493 | -51.24625 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94256930-41fc-3063-b98b-bad8997120c4 | -14.39501 | -51.25546 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f152ee91-990a-3206-ae07-f0f6f032032c | -14.43625 | -51.27147 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4eec421-eda0-3ee5-ae67-92324e98f865 | -15.01236 | -51.40818 | 2026-10-01 04:36:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 429f1bc3-304a-3a53-83d1-da806394b71a | -18.87736 | -43.82722 | 2026-10-01 04:36:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c092e31-fd9a-32eb-adf2-b7b01f323fc1 | -14.48693 | -48.30478 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2012f2c3-de1f-35cb-9381-7a8744b6a28d | -15.95461 | -41.89942 | 2026-10-01 04:36:00 | NOAA-20 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c42dbced-558e-3746-8a62-434ade1e89e2 | -18.12643 | -44.34911 | 2026-10-01 04:36:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afda7a4a-ec37-3acc-988f-b9054f1c9995 | -14.38319 | -51.28907 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d1dd92c1-4039-396e-8ba8-b1b2dba87048 | -14.50243 | -48.29278 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59021cb3-99e3-30ff-9b75-711666bc282a | -13.6453 | -53.93894 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b8f3ea26-00e9-3ac1-b1a7-23a07e869932 | -15.49198 | -46.1235 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c41f39c0-30ff-3c8c-9be0-a771cd4bc8de | -13.65715 | -53.94526 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3986867d-7bcc-3a5e-9fc2-fb029ca9a640 | -18.06716 | -44.52433 | 2026-10-01 04:36:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 163cf0ff-9b8e-3d45-9b46-32e817cb6263 | -15.64505 | -44.71541 | 2026-10-01 04:36:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd2ac397-caf5-35ef-8d10-2bb9dc4601e0 | -14.41777 | -51.25103 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8e2b03d-e1b2-35b1-aee4-a742cdc8020c | -16.02285 | -45.13418 | 2026-10-01 04:36:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4239d21-afe7-30fa-ad45-fa3d2595b40a | -20.85972 | -47.10521 | 2026-10-01 04:36:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8c20ef23-9445-3495-b958-24eef127e352 | -14.37893 | -51.29258 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6edb01b7-58b5-3757-a60f-a4883894420e | -15.92101 | -43.52615 | 2026-10-01 04:36:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb5562d2-6e5c-330d-932d-f052a3083d76 | -18.90267 | -43.79234 | 2026-10-01 04:36:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d2c6a8c-d3b4-30d9-972e-ee9e2df3f05d | -14.44194 | -51.25967 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 206c9c2a-0aa3-332b-b8ed-6e97a87d22d0 | -19.03745 | -45.66598 | 2026-10-01 04:36:00 | NOAA-20 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb16747a-f775-346f-9402-21acbda62cc7 | -14.86564 | -51.85138 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 78478bf6-a3a3-372f-b602-5e7aa3638152 | -16.43153 | -47.1855 | 2026-10-01 04:36:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ec6fadd-8472-35df-b58d-d93db7218413 | -15.23988 | -46.14681 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c056901e-6cdf-3362-9fde-717b5f39be33 | -15.30377 | -42.77814 | 2026-10-01 04:36:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5e24453c-e5c3-3d54-bff4-f5316e5a8be5 | -14.88579 | -51.8867 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 03cbd072-72f5-323b-aef3-af315fbb9f17 | -17.91324 | -45.04132 | 2026-10-01 04:36:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbd205ea-7a2b-38ed-9c2c-88e8ed290998 | -14.4135 | -51.25453 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1f85cc3-f584-3060-be83-c7aee41edc9d | -15.22488 | -46.15218 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbe08085-98f0-3265-bdde-266245f4fdd3 | -15.24047 | -48.56549 | 2026-10-01 04:36:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7428f4b7-4934-3cc0-a877-f47642bbc5f6 | -14.39738 | -51.2702 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |


[Clique aqui para ver as próximas entradas](README69.md)
