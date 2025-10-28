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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b1585a6-8602-364d-887c-a6ed76604fc7 | -12.69944 | -46.32103 | 2025-10-28 04:44:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf7d135e-87e9-3248-9670-26f6b276465e | -15.15269 | -46.60314 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94447c26-b7c4-344e-9f8c-07e0a8bcde2e | -10.56016 | -49.82078 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55e3bc18-f77c-3b3c-949b-df443165a082 | -9.16904 | -44.57803 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfdfe226-3356-3c90-834a-04a331cf1906 | -10.31127 | -47.15971 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b1026fd-1520-3e95-9325-6af422c66081 | -8.18137 | -48.17419 | 2025-10-28 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87f128ee-8084-37a8-a5ce-7b6f91ff61b3 | -9.96426 | -47.0905 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e15a1721-6de4-353d-818b-246828291463 | -10.56462 | -49.83598 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6fd9fd1-2019-324f-9421-3841638f1a4f | -12.39439 | -49.96144 | 2025-10-28 04:44:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efc58030-85ce-331c-aecb-a0ac182c0b4f | -9.36212 | -49.26574 | 2025-10-28 04:44:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88effd3e-d38a-352b-bceb-145c37058b37 | -10.91779 | -50.25711 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6b4be9f-39c3-3973-81dc-9afecb1473c5 | -12.08461 | -45.66841 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d601d19-ecac-303b-a390-6ab4c3ea9e5a | -13.21994 | -47.0879 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3b41185-26b9-36cc-a3ea-eb088eb24974 | -9.35066 | -48.1855 | 2025-10-28 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9b12b33-4c4f-30b4-9e0a-1d63dad36818 | -14.53298 | -47.97828 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1badd07-9d80-3953-9c76-5239b23a57ba | -8.56826 | -47.02209 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7b743ff-06ba-3d79-bf89-36bfb39f3f5f | -8.32216 | -46.82348 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b3aaee9-c57b-3ddb-8606-83036f55130a | -10.58739 | -49.79975 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6a4c3829-76fd-33f9-a4a7-dc59b47833b8 | -10.56293 | -49.8031 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e0f0e40-8363-3524-ae56-4c8812f5a564 | -10.99271 | -50.35896 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85dec0df-4560-35f0-b1ac-9be6f8777a96 | -10.6343 | -42.3177 | 2025-10-28 04:44:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 65d3c410-7bba-3074-8a54-59c6837e8ebb | -13.39356 | -48.51097 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05ad5961-37c2-3150-abf4-7c9fea816915 | -15.20714 | -47.21579 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01f74179-4353-31a7-a42f-a46b5bdc3009 | -7.9308 | -49.74077 | 2025-10-28 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 265ea86f-88d9-3edd-9ae6-399ec11c15fa | -12.05363 | -46.46992 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aaff5773-8ddb-36c8-8039-591df7448f21 | -11.04156 | -47.85555 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 039912db-011c-3c87-98ee-124db2fa77c5 | -13.184 | -48.44444 | 2025-10-28 04:44:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a6c6a59-94eb-3fc7-a83b-e55799c1d87b | -12.97991 | -48.38942 | 2025-10-28 04:44:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e4ae7a4-0cd3-3dd5-a389-e1bba028b9df | -7.92747 | -49.74024 | 2025-10-28 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77293489-2d07-3398-89d8-d847bc81b38a | -13.44712 | -44.10246 | 2025-10-28 04:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9626f1f-91ec-3987-90be-6a1351b2c077 | -8.11267 | -48.82001 | 2025-10-28 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d2ef305-1f30-33a7-a640-e04b57bbc394 | -14.62975 | -48.44497 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58eae559-842c-3d31-ab5e-bdc1b4a4c53f | -10.12852 | -47.70505 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75a53c50-3760-3b80-904d-ddd4ec43d10a | -13.3744 | -47.40671 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c64c9f22-112e-3834-a1e3-70014f4c39e2 | -9.23456 | -45.61172 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 94288ef9-1520-3e7f-a69e-1c9418cfe12a | -8.31667 | -46.83531 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b39eb6d-b771-3218-b126-f985dc276592 | -9.56582 | -46.96748 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c530ae6-de6a-3117-a0bd-a0f9a3cbc782 | -13.66664 | -46.52505 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| acca6be5-a36c-3623-aaad-be695ed43db2 | -14.53718 | -47.98078 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a26126f-fc1f-3695-a5a5-858f6b3096fe | -13.35494 | -46.47169 | 2025-10-28 04:44:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32f09fe0-7266-3c0b-a180-1099ac8ab437 | -9.95335 | -47.08892 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f892b23a-ee74-3878-b81d-897b262c6870 | -10.22104 | -49.84635 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a424bb-3889-3152-807b-b046fc41c9ad | -13.36578 | -47.41388 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2b128cc-d745-3df4-a15e-5d5a08758fd6 | -9.8756 | -49.78425 | 2025-10-28 04:44:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7373866-a549-315f-a18b-23d4b675ddff | -9.96991 | -47.17742 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7306ab1-7e77-3f7e-bd6e-4e2c1c115d78 | -11.02622 | -44.65022 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b14c139-0094-362e-8b70-f652437bd048 | -11.19316 | -51.03692 | 2025-10-28 04:44:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a3c2aab-b805-3e14-86ab-63bfa1068e44 | -9.14838 | -51.29896 | 2025-10-28 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 244bb98a-294f-35d7-a72b-00401a5a3cb4 | -9.22177 | -46.35157 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24a3a2ec-960e-3ad3-bf5c-7fd82bc2aa04 | -10.99493 | -50.36652 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1a64596-e375-3fc4-9c2c-9ae902665407 | -8.71687 | -50.00898 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2676ac85-78c7-38ee-8073-5c22a72cc943 | -15.1494 | -46.59755 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ba891ee-6e62-35fc-bb96-0faeffee1d16 | -13.87856 | -48.49117 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be121bb5-89ea-3005-a35c-ff1cff394dcc | -9.95023 | -47.11014 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 029f4140-94b6-3312-a320-657faf5d39d5 | -14.61309 | -48.40828 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0786d976-ef1c-3af7-94f3-41013373e7ac | -9.99369 | -48.10158 | 2025-10-28 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37451de1-837c-3309-b6e8-7ef4bc880a00 | -13.0422 | -45.8554 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56504039-b915-36f4-aae0-bcf8769feeb2 | -11.92608 | -47.65948 | 2025-10-28 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6ef84f8-176b-33dc-b530-540e525dfa94 | -12.8498 | -47.23264 | 2025-10-28 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3a2862a-b6e0-3fde-89cc-3b35a407f284 | -8.63272 | -44.80056 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c584040-24d8-3269-8a62-a1a25dc42331 | -12.98005 | -47.92639 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 119813e9-a238-3e44-97d2-79e93bfdea65 | -13.66051 | -47.64039 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e08a56e-8336-3d68-becc-c1f84a0b5b0a | -13.5576 | -49.58993 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72fe803f-8588-3638-bd32-a81a45932e4f | -10.73459 | -49.78273 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 53494fe4-4619-3aab-bccf-04e0029c0116 | -9.61281 | -47.78359 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35108cf9-5365-38d1-85f0-e0662bd07058 | -11.28092 | -45.50715 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2d174c78-47ac-3162-b7d8-ec1df8cf7f58 | -11.28041 | -45.51076 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| a08da7cf-e0aa-37e4-9910-c1174d26d215 | -11.03798 | -47.85524 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f31e3cf9-6cde-31d7-987c-303ccee8c135 | -12.2029 | -46.50755 | 2025-10-28 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad5c2f3c-7bd7-3742-b930-5f1654510a34 | -13.79916 | -48.66376 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ca6be40-e49f-3a5c-8d18-00ef3a64c01a | -13.73089 | -43.99071 | 2025-10-28 04:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fe058c6-43c5-3637-884f-c22a22f852a5 | -10.56072 | -49.81725 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07c1fe6f-1b1e-3b29-bfa3-51f50e0fc56b | -13.21862 | -47.09716 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aceee882-eae8-3a47-ab4e-d5342e076ae4 | -9.46194 | -46.86671 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c03a37e9-fe06-3e2a-8d8e-0c6f3f0feae9 | -13.2237 | -47.08863 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1004d131-15e0-30be-aaf7-b19f8be43e3c | -11.53244 | -49.93833 | 2025-10-28 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f193c023-7c42-3da7-b8cf-5ebf4bd161b0 | -13.54569 | -49.57656 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 188f5c85-824f-39c6-a1f3-edd04b08f3b6 | -14.12946 | -46.97891 | 2025-10-28 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f03fd8b-9b04-38c3-a41b-13a497672945 | -11.28852 | -45.51189 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 52c417f5-d85b-3a2f-a76a-b39099a73d08 | -8.6405 | -45.28533 | 2025-10-28 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| ea598e32-5f13-37e6-a552-19f6edb05460 | -10.62795 | -47.90327 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 995ac84d-0dcf-3369-8a26-3dd4e44f0533 | -14.53782 | -47.97643 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44423a20-9342-3797-811a-619a72e75e9c | -9.53847 | -46.97634 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ee70c7b-37dd-33ef-b3d1-ec5efd617bf5 | -9.75864 | -49.56385 | 2025-10-28 04:44:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c00c9cfe-f319-3c08-917e-20dea21af00b | -13.55815 | -49.58631 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f3154d4-058c-37f7-8df0-bf2f12f96e99 | -12.13457 | -46.98757 | 2025-10-28 04:44:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b1ca392-1855-3c3e-bf40-740d1b6ce63a | -12.70337 | -46.32159 | 2025-10-28 04:44:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf84c526-6751-3e32-8343-03d94c8b19ec | -9.95706 | -48.29891 | 2025-10-28 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81681893-d4f2-3573-bb85-8b6307801688 | -13.36948 | -47.41457 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6999d23a-9af8-382c-94fd-42305d6ab157 | -9.54034 | -46.96366 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c5f76b8-39a7-3c17-a014-820f27e0ed26 | -9.53622 | -46.94102 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 695e957d-b59a-3416-8c25-0ddb37ca3969 | -9.01791 | -43.9771 | 2025-10-28 04:44:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18a546b0-7e3f-3cb3-b176-29645a23f01f | -11.74232 | -50.21491 | 2025-10-28 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c2fd5a5-2880-3231-a63a-c1b80d7162ca | -15.17567 | -47.21647 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6560b45-233b-3560-9347-38c0f25c4112 | -14.82234 | -47.41459 | 2025-10-28 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ddd62cb-cedb-38da-9f06-d516cbcfafda | -13.62657 | -47.03703 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 161aca27-08b0-3961-be87-df3d3189d3b9 | -9.99948 | -48.06275 | 2025-10-28 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5f763d8-8469-3340-ab65-d6aedaa63579 | -13.54033 | -44.13752 | 2025-10-28 04:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 492c1e83-a775-3782-8e25-7a3685b6dfe9 | -14.62916 | -48.44903 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e61ec757-a899-38cc-86db-705dbd858548 | -10.92334 | -50.26522 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README63.md)
