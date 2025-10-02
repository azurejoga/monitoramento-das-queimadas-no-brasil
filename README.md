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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bae23250-7ad9-3616-998b-64ced514c9db | -7.7752 | -42.539 | 2025-10-02 00:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 199.0 |
| 2519f738-4c94-38e4-a2bc-74955e7c835b | -14.3704 | -45.9634 | 2025-10-02 00:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 7b87018e-7853-3f6d-8586-f8dc146adfbe | -7.7755 | -42.5152 | 2025-10-02 00:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| ee26a732-5abe-3e37-819c-f0bf73c99a30 | -6.7213 | -44.1387 | 2025-10-02 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d9697402-e502-3f0e-9c09-668b37db508d | -5.986 | -44.5661 | 2025-10-02 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 0acf30e3-5755-359e-a778-c87e72f0ad57 | -14.3509 | -45.9668 | 2025-10-02 00:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 524bcd66-6e32-3f95-b67e-febba7880394 | -15.2547 | -49.2883 | 2025-10-02 00:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 384807bd-96a4-39a2-892f-903f1994345b | -5.9858 | -44.589 | 2025-10-02 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 176.2 |
| e4137427-7e17-3b58-b4ed-d8ae82ccae10 | -14.3119 | -45.9736 | 2025-10-02 00:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c9a25ef1-5a8e-358b-99f9-6ca48d84013d | -13.1546 | -47.8345 | 2025-10-02 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 48d40346-e30c-3d77-875e-b8b5a52f0603 | -11.175 | -47.2581 | 2025-10-02 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| cc0ef1a7-8840-3c87-a308-7238ab6459b7 | -5.9671 | -44.5904 | 2025-10-02 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 6178bc86-bc41-3686-8d4a-5ecc3db116e8 | -6.0046 | -44.5875 | 2025-10-02 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| db3da330-e25b-34c4-83be-4373a3dd4b96 | -7.7941 | -42.5369 | 2025-10-02 00:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 6b5dd1fb-8727-3703-a81f-b79753ad4eba | -8.575 | -49.5881 | 2025-10-02 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 476683cd-1919-3b86-83e4-2a35d9baf7e7 | -22.5735 | -46.7755 | 2025-10-02 00:00:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 9215632a-fd4e-367f-ba25-abed9c985bca | -11.7691 | -64.8616 | 2025-10-02 00:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 3075d387-6f93-3fb9-b5c9-248af500dc10 | -14.3514 | -45.9437 | 2025-10-02 00:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 6cfab2aa-4288-3851-823b-c49cb27c04a6 | -4.841 | -45.212 | 2025-10-02 00:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4ea1d2e8-04b9-3a99-87a5-bc8e6876b20b | -15.2542 | -49.3104 | 2025-10-02 00:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 927346a1-bf4e-3e20-b7f1-70b8519e7b99 | -15.2742 | -49.2852 | 2025-10-02 00:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 47fa5dcb-edde-31b6-8a78-ce6c5a435ea6 | -8.5748 | -49.6095 | 2025-10-02 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| e197b363-7de9-3e76-a652-0840491851bb | -13.1739 | -47.8317 | 2025-10-02 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f13dded5-0e3f-3c16-8efe-9da949dd4d55 | -4.8596 | -45.2109 | 2025-10-02 00:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 4fb5efe6-da27-3c3e-838f-18654c2abb60 | -14.4065 | -46.0953 | 2025-10-02 00:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ecbb436c-f53a-37ed-824b-841a53db9608 | -5.9856 | -44.6118 | 2025-10-02 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| ab4b1b00-4982-3919-a744-5cf1998b3a98 | -7.7944 | -42.5132 | 2025-10-02 00:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 4db3cbbe-9996-3400-b09a-acb65ff0e84f | -12.4207 | -54.3536 | 2025-10-02 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 4164a067-53fc-3560-83b4-85b3840ad960 | -5.9669 | -44.6133 | 2025-10-02 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 35dfb320-c708-30c2-b74f-51cce5a59f6b | -14.2121 | -46.1058 | 2025-10-02 00:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 45698969-5cbf-3f8f-9c16-471cfa466137 | -20.156 | -42.27734 | 2025-10-02 00:09:00 | TERRA_M-M | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 38fb7504-5d22-355a-bd28-a643c8bff2a6 | -19.35581 | -43.99309 | 2025-10-02 00:09:00 | TERRA_M-M | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 19a5bbbb-0c65-36ff-ad94-904b482500f7 | -20.13257 | -46.35285 | 2025-10-02 00:09:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 088094ea-2791-353b-8ab0-027eb3ff2232 | -22.30547 | -49.60738 | 2025-10-02 00:09:00 | TERRA_M-M | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.5 |
| 402e4a50-57dc-3717-8031-afe037fc2573 | -17.89705 | -41.97613 | 2025-10-02 00:09:00 | TERRA_M-M | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| fd6bad2a-bb9c-3b6f-a20f-b10ff1a9ef55 | -19.04952 | -48.13031 | 2025-10-02 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 40.6 |
| c691c4e9-e4c1-384c-a727-46b1fbd9e4e0 | -18.52525 | -45.04218 | 2025-10-02 00:09:00 | TERRA_M-M | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1570b937-b055-3945-abdc-b7f83a4a94f0 | -22.56298 | -46.79485 | 2025-10-02 00:09:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |
| 07d37fa7-e1c1-335b-96c6-ee068909937a | -22.30522 | -49.60086 | 2025-10-02 00:09:00 | TERRA_M-M | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.6 |
| 890d301b-34dd-3873-acd4-553e39ffc06f | -20.04226 | -44.53754 | 2025-10-02 00:09:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 3f1636f1-7f15-3c63-b5d2-c327834d4be5 | -21.23752 | -44.06015 | 2025-10-02 00:09:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| d5da507a-3eba-3cd9-8158-0f058355154e | -22.57306 | -46.77467 | 2025-10-02 00:09:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 969402fb-8f50-382c-9c07-7164cd629811 | -19.00162 | -43.00889 | 2025-10-02 00:09:00 | TERRA_M-M | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 301c60e1-0199-3959-8030-6a616875a5bb | -18.13896 | -42.39999 | 2025-10-02 00:09:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 6464c294-21b0-3758-86f8-0f8fdcb21f36 | -18.4629 | -40.57021 | 2025-10-02 00:09:00 | TERRA_M-M | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| 56d9d4bb-f940-356e-8548-d5a3e3025cb2 | -18.14022 | -42.40933 | 2025-10-02 00:09:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 37978bbb-a578-3b91-9b0d-dab5a45ed4d5 | -20.88414 | -43.20583 | 2025-10-02 00:09:00 | TERRA_M-M | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| d013b999-4aaf-3f89-a452-a9db056f5678 | -18.84468 | -43.14392 | 2025-10-02 00:09:00 | TERRA_M-M | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.3 |
| 16a3e646-2815-3cc8-91dd-22e72ecdb9b8 | -18.50185 | -44.04369 | 2025-10-02 00:09:00 | TERRA_M-M | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 77c3d9f5-246e-3ded-91fc-cf14cbbee9bc | -19.00923 | -45.00237 | 2025-10-02 00:09:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c324f459-a1d3-382d-88a8-74fe11a5db56 | -19.58018 | -42.58374 | 2025-10-02 00:09:00 | TERRA_M-M | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 13723f87-385c-304c-8967-f53a65935dea | -21.56361 | -45.2731 | 2025-10-02 00:09:00 | TERRA_M-M | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 1208d289-9b3a-3fdc-a4c9-4a587df5879b | -20.70751 | -43.98546 | 2025-10-02 00:09:00 | TERRA_M-M | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 3f5a6d43-b291-32fa-a373-6fa4dd80f613 | -18.55251 | -43.44645 | 2025-10-02 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f441a03e-5578-37e6-812c-39e50b365ee3 | -18.44826 | -44.50024 | 2025-10-02 00:09:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9bc150d6-7132-3c4c-8093-fdb15be1bcc9 | -19.35964 | -40.20381 | 2025-10-02 00:09:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 27db46e9-8405-3c3d-a4b4-403b7fdc00f3 | -19.96442 | -43.72036 | 2025-10-02 00:09:00 | TERRA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 78792bdd-df80-3fe4-8915-2e3e63b619f2 | -19.72647 | -45.89894 | 2025-10-02 00:09:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 781bcb43-024b-396e-9e75-33676e8de1e7 | -19.0029 | -43.01861 | 2025-10-02 00:09:00 | TERRA_M-M | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 20f30b9e-c70c-3b96-a890-017ece9a6515 | -18.4439 | -42.41171 | 2025-10-02 00:09:00 | TERRA_M-M | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 9941180e-9f18-3093-aa5c-2f5b60c6bb19 | -19.88944 | -42.62784 | 2025-10-02 00:09:00 | TERRA_M-M | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| f531e84e-6547-38ca-bd12-6043f198186c | -19.38163 | -45.30236 | 2025-10-02 00:09:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6e28e0b2-5ef4-3528-89ed-279d962a7924 | -22.57502 | -46.79326 | 2025-10-02 00:09:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| e7af3f59-3695-359d-a7db-58879e239f91 | -19.64073 | -44.91739 | 2025-10-02 00:09:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 4a2c608e-6662-317f-99e9-1120397d2045 | -18.05764 | -41.6752 | 2025-10-02 00:09:00 | TERRA_M-M | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 63579688-72ac-3380-9372-14369b05b447 | -19.29063 | -43.74761 | 2025-10-02 00:09:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b6a5c83d-02ca-3596-9b08-863d5fd70fbd | -18.47185 | -40.56875 | 2025-10-02 00:09:00 | TERRA_M-M | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c7075752-a352-3df7-b0aa-19c5f9acc00e | -18.84594 | -43.15361 | 2025-10-02 00:09:00 | TERRA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 213dc572-1cee-312d-9df9-14ebbeaafcae | -20.1157 | -44.39002 | 2025-10-02 00:09:00 | TERRA_M-M | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 61dc81f9-c2e9-3f7a-802b-d25202307c23 | -20.22971 | -43.91246 | 2025-10-02 00:09:00 | TERRA_M-M | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 44129539-4487-371d-8f1c-a956d8d9f19a | -19.46279 | -43.65738 | 2025-10-02 00:09:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 09eec5b2-9cf8-387a-ab7d-6d7e1592bc73 | -18.19189 | -43.57329 | 2025-10-02 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 04d05645-6e36-36d8-8587-b0c224a72bc7 | -19.58033 | -41.90052 | 2025-10-02 00:09:00 | TERRA_M-M | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 2e305898-3b6b-3bf1-aa0c-647fc90af45d | -17.55725 | -44.48254 | 2025-10-02 00:09:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| dd5a9f19-bcd9-3abd-a32d-97d74a4cd161 | -22.81238 | -42.70393 | 2025-10-02 00:09:00 | TERRA_M-M | TANGUÁ | RIO DE JANEIRO | Brasil | 3305752 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 30fed26e-d222-3eec-9192-3fb2602f6648 | -19.35447 | -43.98222 | 2025-10-02 00:09:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 25eb53d2-a88e-37a7-90c6-8284226a0605 | -18.50041 | -44.0325 | 2025-10-02 00:09:00 | TERRA_M-M | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e3037321-c8c3-3f85-99dd-9fd0f5cbb29c | -18.50114 | -43.39963 | 2025-10-02 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 18715b23-5b6b-324a-a46a-130f14aead0e | -19.96313 | -43.70992 | 2025-10-02 00:09:00 | TERRA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 02682099-d291-363a-886f-3733484f90be | -19.95648 | -43.65643 | 2025-10-02 00:09:00 | TERRA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| badac9cc-b49f-3240-b62c-090cefa00426 | -17.54314 | -43.45922 | 2025-10-02 00:09:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c30f5282-59c1-35c0-b995-72ad3ba8984a | -22.56104 | -46.7763 | 2025-10-02 00:09:00 | TERRA_M-M | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.2 |
| ec8ac07e-9418-30ed-9363-4002dee7dea2 | -19.81271 | -45.85305 | 2025-10-02 00:09:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9d24cbba-a234-3f4e-a4af-6d765520ea60 | -19.5712 | -42.58506 | 2025-10-02 00:09:00 | TERRA_M-M | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| c9e8b8e6-8230-3a1f-851b-40b2294ed3fb | -18.50986 | -44.0314 | 2025-10-02 00:09:00 | TERRA_M-M | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f02cde95-093f-352c-b438-bda507f614ca | -18.44687 | -44.4891 | 2025-10-02 00:09:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4fc6c189-eece-39fe-abb1-ed8a073d81ba | -20.33679 | -41.37288 | 2025-10-02 00:09:00 | TERRA_M-M | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 6217f9a1-4fd7-320d-b6a8-4ae8b8245452 | -18.34253 | -41.8011 | 2025-10-02 00:09:00 | TERRA_M-M | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 869b60aa-fd87-3ebd-aafa-4a05b10ad3b1 | -20.70892 | -43.99678 | 2025-10-02 00:09:00 | TERRA_M-M | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 013ff2ac-859f-39e8-92fe-6aa33a504e89 | -19.39352 | -45.3142 | 2025-10-02 00:09:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8a8e663c-5571-3f33-9073-a17640a5d08d | -19.58161 | -41.90991 | 2025-10-02 00:09:00 | TERRA_M-M | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 2ad6da17-efb6-3054-9abb-b404a27aceed | -19.05167 | -48.15069 | 2025-10-02 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 6b160cdb-8566-326f-9ab4-e21260f8be55 | -19.26355 | -47.35268 | 2025-10-02 00:09:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9d9a525b-add1-3ec9-9200-f415abd5a9af | -20.87587 | -46.47136 | 2025-10-02 00:09:00 | TERRA_M-M | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 32.3 |
| d8046bda-2c6d-3e12-baa6-30840a46932f | -18.59228 | -43.04349 | 2025-10-02 00:09:00 | TERRA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 360056c5-f92f-3233-ba86-c9e51ca02a8a | -20.04708 | -41.68225 | 2025-10-02 00:09:00 | TERRA_M-M | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| fd9ea2ba-0363-3007-b3fa-544954a2691b | -19.39195 | -45.3012 | 2025-10-02 00:09:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 486397f4-e109-3d76-8c0a-b5cdaeb0b915 | -20.73582 | -46.03095 | 2025-10-02 00:09:00 | TERRA_M-M | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8da33239-5701-3dd5-b71c-4ccbc9775862 | -19.64113 | -44.92346 | 2025-10-02 00:09:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| e2600f28-4956-383e-9ce8-ea9f5ba19957 | -17.94033 | -42.57141 | 2025-10-02 00:09:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |


[Clique aqui para ver as próximas entradas](README2.md)
