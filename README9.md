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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 742317c8-4826-30e0-b4a3-115a811f667d | -5.5994 | -45.18044 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79c37b6b-a757-3863-a3ca-3a32cc5f2e18 | -2.58485 | -51.92545 | 2025-07-06 05:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ab7e051-84c4-308d-a017-78705662c8fd | -3.48235 | -48.44444 | 2025-07-06 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e670694b-57e4-3f22-813a-aaf09cac4219 | -3.98163 | -48.41744 | 2025-07-06 05:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85383fc0-8328-306a-b431-81009ef478c9 | -12.0266 | -57.0845 | 2025-07-06 05:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 460a87e0-cfb9-3dfd-a82b-50cf820d5106 | -9.09659 | -47.96167 | 2025-07-06 05:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ec055fc-ca13-3d1d-9595-d83c5d969822 | -11.00819 | -51.6342 | 2025-07-06 05:21:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8331dba0-9ae6-35d5-8de2-fe2f89c30ef5 | -9.92023 | -59.91216 | 2025-07-06 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8c1eb66-c131-3c2b-a67a-8fa3e04bf00b | -10.89125 | -56.45407 | 2025-07-06 05:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21f50f47-ffc3-3584-85cb-1244c24594c0 | -10.04617 | -64.98798 | 2025-07-06 05:21:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2c6e92c-0a51-34e6-9842-de2675393712 | -11.77997 | -62.92715 | 2025-07-06 05:21:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bdaf901-3bc3-3c4e-ab89-97376df46e22 | -10.04679 | -64.98433 | 2025-07-06 05:21:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b7550a7-575e-340e-ad62-296b74ce80e8 | -11.88069 | -58.73837 | 2025-07-06 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d3186b2-b874-36cb-b424-9605da2cafbe | -9.34336 | -58.85004 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9ff76bc-1c7f-30d7-a3ec-e73f58740ad3 | -10.30482 | -57.14514 | 2025-07-06 05:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd1bc75b-102b-348f-90f1-08d6d17859d9 | -9.08965 | -47.96606 | 2025-07-06 05:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be2c4d84-0b69-384c-ab6b-4abd62e24279 | -12.58281 | -56.98428 | 2025-07-06 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47ced467-b8f8-3f22-a296-97ad609ef099 | -11.33075 | -51.45211 | 2025-07-06 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 239cedac-b8ad-3ea5-b2c4-da520f89efda | -11.00858 | -51.63123 | 2025-07-06 05:21:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5eb46df-020e-3d30-9b02-d1debe5b263d | -11.326 | -51.44831 | 2025-07-06 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79c7d010-7d96-3ab4-9c80-6e8700b6b3dc | -11.33035 | -51.45522 | 2025-07-06 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a843c5c-d65f-30fb-8beb-0737385fa4c5 | -7.91715 | -61.55767 | 2025-07-06 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 119fbf21-332d-362b-ab87-20a6ecd08ca2 | -12.0266 | -57.0757 | 2025-07-06 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| ac6d4232-c0a6-3fe0-a84d-92645f915078 | -9.33947 | -58.85305 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1d290f5-ea8b-3c8d-b783-625dad4ca48a | -12.03023 | -57.07624 | 2025-07-06 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 607f3304-cadd-3cf1-b185-e627090b8b57 | -10.94901 | -54.37688 | 2025-07-06 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a053f16-a091-3a12-9384-6628801a1d2c | -11.3359 | -51.4528 | 2025-07-06 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 798e13a3-4619-3878-afeb-9025e3d719aa | -8.31076 | -55.10001 | 2025-07-06 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 595e407c-42db-3125-a6e0-3066c07031c0 | -9.35306 | -58.84399 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c99d874-f33b-3565-af21-b74ce664f1ae | -12.02236 | -57.0794 | 2025-07-06 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e7e72dcb-729a-399b-897d-3dbdf6d69612 | -7.90662 | -61.51265 | 2025-07-06 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b121c9b4-86bd-31d5-83b7-f58112161fdb | -9.01803 | -59.54217 | 2025-07-06 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4edf96cb-1821-3c61-b03f-6e1a81ae585a | -12.57915 | -56.98374 | 2025-07-06 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 866c6d77-0bd9-3a89-a9a7-e1c66aadc89f | -14.84345 | -56.38455 | 2025-07-06 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66e58695-f536-3c43-8063-4a480c14d393 | -11.83791 | -57.75015 | 2025-07-06 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a7c0cb2-78b5-367c-a428-94b9f64cb04c | -10.14751 | -48.14818 | 2025-07-06 05:21:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6058a3ed-a1b8-3ad0-a9d0-73340564511e | -9.34972 | -58.84346 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2cf4b77-7aa0-39a4-bdae-4f4bb2049983 | -15.8828 | -48.33157 | 2025-07-06 05:21:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa3aff7a-86f8-3f2f-8494-7cf502fd0158 | -12.58218 | -56.98864 | 2025-07-06 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88633429-59c5-3e70-8b5f-e7176a85fc78 | -11.32559 | -51.45142 | 2025-07-06 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 974a39e6-e4da-3d05-949d-190ad75e1efe | -11.87731 | -58.73782 | 2025-07-06 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6b88ac7-0657-3e81-8cb4-49e5b5fbe3e7 | -11.98197 | -55.51928 | 2025-07-06 05:21:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14e5b135-e6b5-3394-a5f1-caf096e1609d | -9.28288 | -57.80114 | 2025-07-06 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1707c687-74e0-3668-8a9b-8a8e44568727 | -9.25081 | -57.52684 | 2025-07-06 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ccb873e-8840-32b9-b3b2-5e9a8cd66924 | -11.3355 | -51.45591 | 2025-07-06 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d658692-5b7a-347d-9c07-15c04eb9a5fa | -9.34917 | -58.84699 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3501bb6f-47b6-3d10-8c83-689b7a3a942f | -11.33115 | -51.44899 | 2025-07-06 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9de2bdc6-f569-3f22-8cff-2c2417d8af5d | -9.3553 | -58.85158 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21e080f5-6947-322e-bdab-e83212ada210 | -7.43002 | -60.02983 | 2025-07-06 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b8e56aa-a676-32f1-ab1c-94ee64c6e853 | -12.02298 | -57.07515 | 2025-07-06 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 22de6690-9f85-3f23-9d2c-67f5f52997b6 | -13.00496 | -55.9723 | 2025-07-06 05:21:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72480a71-52fb-3dcf-ba94-9684d8ad1567 | -12.02598 | -57.07996 | 2025-07-06 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 409a8a62-2be0-31ce-94a2-2d591636ccfd | -9.35251 | -58.84752 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 063649ff-3f2b-398e-8107-213a206ceffb | -9.2823 | -57.80487 | 2025-07-06 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd0a498f-7725-31e1-a2a4-260b0451ac6a | -13.00466 | -55.97577 | 2025-07-06 05:21:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8feeca8-712f-3c02-8092-6cb6b2be1dba | -11.97801 | -55.51871 | 2025-07-06 05:21:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f36f1805-e439-39ca-9366-b3519588dc49 | -10.67219 | -56.54796 | 2025-07-06 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12c2062f-1dc5-3046-bb70-28e450c35517 | -11.47059 | -61.94309 | 2025-07-06 05:21:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 232cc3e0-ec68-3568-be39-88b6792a1ff3 | -11.00312 | -51.63351 | 2025-07-06 05:21:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69da0cfd-3e6a-3d60-9185-b3871eb6d7be | -9.34003 | -58.84952 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd56364c-200e-385c-9fb8-83338cb819c3 | -9.33613 | -58.85252 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50bbcab4-7e4a-37a0-8283-1bfa582b477f | -9.36028 | -58.84151 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e2fa8b6-97e2-3684-ba76-e473418a097f | -15.88226 | -48.33705 | 2025-07-06 05:21:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28776e6b-9fb0-3924-8e88-33b645d53526 | -9.93254 | -59.93914 | 2025-07-06 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ce3e0a2b-1e45-3333-ba05-7f79f3e2968d | -9.02003 | -59.54579 | 2025-07-06 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54812ac9-8218-3403-b9c3-ea4ab20b287b | -12.02537 | -57.08419 | 2025-07-06 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 5c4cdd28-ec12-394f-abc5-3523fced053c | -9.70034 | -48.59407 | 2025-07-06 05:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2d58f9b-691d-38ef-87d7-470367f7c572 | -12.58584 | -56.98919 | 2025-07-06 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33eebf71-b6bc-3dee-a0f0-5d23f2d69443 | -12.0296 | -57.08051 | 2025-07-06 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3f43390f-23cc-3117-92b7-0671a00da936 | -12.02899 | -57.08475 | 2025-07-06 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| dd902b5d-f966-3382-adfc-c022742e155f | -9.35749 | -58.83745 | 2025-07-06 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9182332-a862-3507-9ff0-70e964af85f1 | -20.72412 | -56.65449 | 2025-07-06 05:23:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d222e0e-c78a-3a2e-a39b-3a68844e503f | -20.72825 | -56.65524 | 2025-07-06 05:23:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edc210eb-8506-306f-b2c8-06779d1106d7 | -20.20057 | -50.7058 | 2025-07-06 05:23:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 261ab05f-ca8b-37e1-b1a6-da2b40be6f9e | -20.20014 | -50.71035 | 2025-07-06 05:23:00 | NPP-375D | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3bb832c7-d8b8-3d6e-a073-cb7341c68daf | -12.0266 | -57.0845 | 2025-07-06 05:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| fc74d9d8-58d4-37d9-9d94-4653362eaf09 | -12.0266 | -57.0845 | 2025-07-06 05:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d1c39e29-0d7a-38da-aa74-b1ddca2d323d | 0.59799 | -60.46579 | 2025-07-06 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4f9ea26-2ae3-36c5-9018-dac91d35aa75 | -2.90991 | -54.48605 | 2025-07-06 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9198bac9-71da-3dc2-b7e9-cd9330b7d4b7 | -2.9093 | -54.49013 | 2025-07-06 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 407d5ff9-127f-39b8-a971-7e5f5b0995cf | -12.02221 | -57.08405 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1c5d1265-f196-30be-b086-f7ca1de08262 | -11.4708 | -61.94428 | 2025-07-06 05:42:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 27aad223-4731-3caf-ac00-0f697f5f17f9 | -7.91906 | -61.55753 | 2025-07-06 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94191245-5280-39b5-94ea-fdb1aa06c6c2 | -9.91938 | -59.91066 | 2025-07-06 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 380e1341-f1a3-3445-9dc6-a894e11e8267 | -7.42908 | -60.02979 | 2025-07-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6115d678-cc8b-34d8-9a44-3178e6eba2e8 | -12.02187 | -57.08095 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d133aa6b-1b7e-34a7-b793-74bdf17186b1 | -9.93344 | -59.93877 | 2025-07-06 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 639bfec3-5889-3671-81d3-7ffb479de1d1 | -12.02855 | -57.07756 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 97af4fcf-f8af-36b1-81ae-d43c93583b6f | -9.9288 | -59.90508 | 2025-07-06 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bd3d29b-1ccc-339f-b0c1-fd8b865dc95d | -12.02264 | -57.08047 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a74e2e08-998d-3cab-84d9-1d08f0eae5fa | -9.08042 | -64.46124 | 2025-07-06 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a9f55e64-2036-3c2e-a2ed-74d395e967d4 | -11.98155 | -55.52048 | 2025-07-06 05:42:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a659b0c-121b-33a1-bfd4-897d25d6e0e2 | -12.02811 | -57.08121 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 84b53374-7d16-36d9-af09-37209f188ac6 | -10.30371 | -57.14433 | 2025-07-06 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cca1f754-9915-3d0f-95e6-00908df9221f | -9.44342 | -63.20563 | 2025-07-06 05:42:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c82927ec-6177-39df-a040-56f104ce1ac8 | -12.029 | -57.07384 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 03c1868e-b2bb-37fd-8546-6f80fd8e2807 | -10.04583 | -64.98744 | 2025-07-06 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49862ab9-7db4-391d-999e-d417be733e85 | -12.02141 | -57.08451 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cdd8f4b8-c05d-3036-b84f-36a35b064be9 | -9.92907 | -59.93813 | 2025-07-06 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc62daf3-7f3f-32c8-a05f-b087b8020a16 | -12.02233 | -57.07734 | 2025-07-06 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README10.md)
