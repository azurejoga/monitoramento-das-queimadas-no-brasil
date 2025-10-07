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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65da2bdd-8a26-39d3-84ee-046eaeeeed81 | -15.02605 | -47.55357 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa946b35-7d70-3b45-971c-4839467893ce | -16.00466 | -50.82527 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1ab7f2d-3d62-3d75-a0e6-b3ad1d8b1294 | -15.98327 | -50.8514 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dc1a099-6f13-3b91-adf3-ba91f999dbe9 | -14.9224 | -46.80343 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d757ee82-ab74-3f61-a717-b2c68d839f60 | -17.09225 | -43.38618 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6d5f513-ab62-3c4e-a5b7-ca1ce929d488 | -15.21764 | -49.29582 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a09cf857-fefe-30e6-9896-9365173b9528 | -17.71933 | -40.24216 | 2025-10-07 04:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 98dc1df3-f29a-394e-ae92-acfcdf09349f | -13.37647 | -44.30699 | 2025-10-07 04:38:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca08c2fe-5d47-3e42-bdc1-ae7f82901a69 | -13.30602 | -48.04936 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7453b96c-fd0b-3410-84e1-7cf4a9741885 | -12.94235 | -46.81121 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8747c72a-0a63-3f55-8048-fbd025089011 | -13.6907 | -47.94855 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d0f754e-d380-318b-87c4-8a3451bb6ce6 | -15.22429 | -56.78622 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2df927d7-2b04-3d2c-8d27-7358b433067a | -14.9088 | -51.44028 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 13e865e5-dd3c-32df-b65a-41ba9a4e494f | -13.33307 | -48.03486 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 68c95c6d-694e-357b-9b0e-44cd53869682 | -11.45923 | -51.50781 | 2025-10-07 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a0cf0e9-48ea-3714-864a-f1916285a2df | -14.76882 | -46.05993 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 44cc3910-df80-39e2-997c-05042ee2497c | -11.94725 | -46.45888 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5fd0fc12-5f41-33a1-a1f7-620cd3b51d30 | -10.39496 | -50.30627 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2884c320-2459-32e2-ac53-c57199e96c5e | -15.16945 | -52.77795 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6043630-802d-345f-a3c5-de90575c5bb4 | -10.92093 | -47.07321 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c37d31f-cb87-3e7f-ad7a-5f39623d964f | -10.39217 | -50.30204 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c0f6b179-599d-376e-a33a-b7c7669e6583 | -12.42263 | -45.60909 | 2025-10-07 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79461d56-9053-35ed-bfb5-b80647d52150 | -16.11617 | -48.9392 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 53912b98-c921-3219-b130-543b4fc8fe82 | -12.21596 | -44.24857 | 2025-10-07 04:38:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9767270b-81a6-30a4-a31d-6c360a92efa8 | -15.28687 | -46.33321 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99e8de69-cd6f-3193-be35-19c05571d7ed | -15.99506 | -50.84225 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78271629-51ea-3f9d-a5c4-1f2ec804c505 | -13.78925 | -45.78442 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4068c9fb-a373-326d-a665-140f92304d32 | -13.27441 | -48.07442 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9132cca-98c7-32c6-91cd-5da5f39304ca | -15.36567 | -47.32354 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a65cbec4-1be8-303a-9840-512cb7325c24 | -11.81129 | -45.12654 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 318959f0-d680-3a8d-a59b-fd029a005884 | -10.38818 | -50.30515 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ef452df-2f91-39cd-923c-37ef2e5ddee3 | -14.63929 | -52.53653 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13862a46-fc99-3992-8ae9-af0b1671a03b | -9.14981 | -61.23632 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04d1f0ee-31d0-344d-9840-360bd37446a4 | -10.62207 | -48.70486 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9cada5e0-b3f3-385f-a864-d3212f1e0ca8 | -10.934 | -51.15023 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 592c896b-ca09-3d56-86dd-429c9959ea21 | -11.15207 | -47.75016 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5c90759-c744-3268-ad95-028de4d59eda | -13.2176 | -46.53438 | 2025-10-07 04:38:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84235302-ac2d-392e-be84-611b0f05646f | -13.72252 | -48.19731 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 39c9c749-9d35-386e-869a-9a5018a87621 | -12.61538 | -44.75063 | 2025-10-07 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ce0fb4c6-94d5-384f-a508-7095c3e814db | -15.60795 | -52.57471 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1081c3e3-b883-3a16-b5d8-7a565237ff00 | -11.15903 | -47.92867 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16fa97b2-0824-3c49-be97-9447c1e43d43 | -15.60643 | -47.29524 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8541a503-a1ab-3194-bbac-64f2815ee20c | -15.60036 | -42.37379 | 2025-10-07 04:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e5f33b4-20e8-30e9-83fc-99bb12e62853 | -15.17015 | -52.7738 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32ca2535-6924-3ddc-b69a-fb12d4da21c0 | -12.68014 | -44.3871 | 2025-10-07 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 109743b9-21fa-30e6-baa8-21401469725c | -10.4311 | -50.31981 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 786c0551-5a43-32f7-b7ca-fab508f4269e | -11.03508 | -50.92381 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 4ceecb03-d8fd-3b53-98dd-0bd7f02fa723 | -10.41812 | -50.31388 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2572e1b9-e232-3712-b8df-b6402cad7d3d | -13.14252 | -47.79653 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1d70b2d-2406-3251-abe6-3cd93b05fda6 | -13.66496 | -44.30949 | 2025-10-07 04:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60d0c5b9-929d-361b-900e-2246c82a2d31 | -12.24373 | -47.85909 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1f2ad64-159e-32d5-b6aa-ed797ccbfcbb | -10.74479 | -50.47305 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 77d36bae-b9b1-3e3e-9320-560fe030cdd7 | -14.73659 | -46.0177 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2d1c3ff5-6a23-363b-952a-488f65d0a5d5 | -12.91519 | -54.72418 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89de00aa-e79c-3626-b637-6cde13f9a67e | -15.20083 | -46.38075 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81140aeb-2444-37d2-9d2f-0430e9de6812 | -13.29097 | -47.80434 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f05f64d1-abad-3175-a5d5-4b77d222db46 | -12.24823 | -47.76166 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdff8254-1ffe-3cb1-98f0-8ced995136c0 | -13.26589 | -48.06202 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 372e09ae-9352-3a2e-9b59-23386de5638b | -15.05753 | -42.33752 | 2025-10-07 04:38:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| ed7ac3f1-436d-36bf-88b5-838a4e978dc5 | -10.81771 | -48.59886 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97936967-6420-3794-af49-20d21702a7da | -14.7086 | -48.38477 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 276aacc8-2e61-32d5-a18c-80dec85e0576 | -9.16759 | -59.56237 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ae6df0e-6fb4-3031-b21d-64bd29830155 | -15.60863 | -52.57071 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16f2a05d-a10c-3f10-8e51-042d1b76f5ae | -16.34183 | -47.05613 | 2025-10-07 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81cf46ca-738d-3508-8913-4143d4db60b6 | -13.12773 | -48.01038 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0338dd6f-bd82-350a-bc03-19d01a437018 | -12.18376 | -47.7742 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70cde133-34f0-390a-b3f8-2270cd0743b8 | -14.61532 | -52.54881 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c5b7017-e727-3bd9-8a2f-5785583ddfbd | -11.71745 | -45.37563 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20cb8ed5-f95a-3599-ac48-587b051014d8 | -11.84695 | -44.92241 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a30791ea-e84f-309c-9db3-cc4c5cb50525 | -14.92179 | -46.8077 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd1db169-82c7-3fa3-aa46-282a4633cf50 | -13.59125 | -48.14635 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c7b495e-c1ed-3957-8bd0-a7fefbd099a6 | -11.72325 | -44.43782 | 2025-10-07 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a68e1037-0956-3163-a35c-af4caffd0950 | -14.70072 | -48.39102 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97eb898e-0844-3076-b557-f1f7a0a49d39 | -16.02394 | -50.96997 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec1abbf0-9476-33d1-be87-799814ae1df3 | -12.14298 | -50.87354 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db701442-1a34-3361-bf68-285ec974b091 | -15.60512 | -52.57006 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 844415c3-3966-3269-a118-0cd46df5fcbb | -12.30841 | -55.10984 | 2025-10-07 04:38:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcfe578b-3b9c-3c55-9413-a57842a6c760 | -13.86096 | -43.99141 | 2025-10-07 04:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1ad43428-b404-3067-8a92-e873efa49b66 | -13.28736 | -48.05783 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5d12fb3-5663-3e71-b1eb-8a6ef28eb9dc | -16.06053 | -50.99895 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c32716c-2543-37aa-892e-6043db601ad7 | -10.4082 | -48.10027 | 2025-10-07 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bc401ce-b4e7-3989-8c7a-316f1b8d7b69 | -12.23183 | -47.84617 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef8e9663-3299-3d42-b1b6-1b128759b8c7 | -10.5965 | -54.36582 | 2025-10-07 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baa4aca2-d034-3392-9807-b20eab5e91d5 | -13.08686 | -47.86412 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c8d556c-f3dc-3f11-b916-e2671b079faa | -18.04755 | -43.15533 | 2025-10-07 04:38:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bae76689-fa45-3f4f-acfd-ace87e3c5a57 | -13.27324 | -48.05934 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 126c7573-aac7-39a3-8267-27d80197e1c7 | -14.93108 | -51.47502 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55d0b7c6-d7d3-3083-a4a8-ba65a98c0178 | -15.2143 | -49.29526 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e3bed4f-b19f-38af-859c-fbedcb674fcf | -11.1624 | -47.9292 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e0bce93-d2d3-3e96-b91f-6f7d55ae798a | -12.89281 | -54.75453 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 747e5cd1-ab69-3282-8e5c-29c83fa2ab31 | -15.0754 | -46.64223 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 654a30fd-152c-31dd-a274-1f5f81130712 | -13.3438 | -48.03285 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dea11fa7-643e-3243-bccb-74089a24a549 | -12.98112 | -51.02799 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5bdf11d0-2893-304a-a360-4dedaac3966b | -13.3622 | -47.56421 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f536ce4-a43c-3b18-827e-b6580191c045 | -11.26552 | -48.84449 | 2025-10-07 04:38:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 013e2c07-c305-3611-a055-42908713bc09 | -16.03237 | -51.02395 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0e7ee9b-41d8-3ef8-aaf1-df77e015834a | -10.42991 | -50.32714 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8573f397-dd7f-3cd1-ae15-a922700fe4bd | -15.98662 | -50.85197 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a244283-73e5-304d-97ee-472a09fcabc9 | -10.41133 | -50.31275 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| af6fb862-d4e5-3e72-af29-e8e3702ddce8 | -10.45642 | -48.36117 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README66.md)
