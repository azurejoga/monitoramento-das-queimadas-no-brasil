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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6d8a420-eb40-3bce-af53-cef14e70e496 | -23.32604 | -50.87664 | 2025-09-06 03:53:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| f685165f-5323-30a3-93dd-859cdd328797 | -22.25112 | -48.75411 | 2025-09-06 03:53:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.9 |
| 49946351-6c33-3828-bd74-a20fa614c6a2 | -24.51546 | -50.74881 | 2025-09-06 03:53:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1a1f78da-adbb-3f31-b426-6eb2120efe96 | -22.2761 | -48.03323 | 2025-09-06 03:53:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63d790cf-53fc-321f-aa2b-b106eace3865 | -22.24762 | -48.74723 | 2025-09-06 03:53:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| f95f6fa0-665a-37cd-9f2c-88bedb4e676a | -22.6579 | -46.82763 | 2025-09-06 03:53:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| cdf01ffe-6d65-36e8-a725-1e6f5bcb9037 | -23.19269 | -50.34462 | 2025-09-06 03:53:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ecc8e0cb-e928-38ed-b6dd-da187448af8d | -22.12257 | -46.63275 | 2025-09-06 03:53:00 | NOAA-21 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 08f3ec27-d36f-3346-a400-606bf3ffa6e4 | -22.78123 | -50.61928 | 2025-09-06 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 432f71d1-6739-3e0d-9aa1-d568074a7c70 | -21.76793 | -47.27491 | 2025-09-06 03:53:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 04cca891-b840-39e4-95c0-9cc6ca9c753c | -22.78201 | -50.61568 | 2025-09-06 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4820aa37-7153-3722-b88a-f2312b76a4dd | -23.42533 | -47.04333 | 2025-09-06 03:53:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 68432422-7a9a-3ca0-bb60-2949dc45c319 | -22.78052 | -43.04222 | 2025-09-06 03:53:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ff5543dc-b1dd-3601-9dd1-e7226fc24ba3 | -21.83689 | -46.4584 | 2025-09-06 03:53:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3f07841d-6fdf-37e5-8ca8-9d418e89e98c | -23.42758 | -47.03833 | 2025-09-06 03:53:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d6519ed8-0e19-3983-a8b8-8b68461e7f11 | -19.9051 | -57.9213 | 2025-09-06 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| cca63d79-6c5d-30a0-9ff2-264a76b25276 | -14.1797 | -53.0774 | 2025-09-06 04:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 86f6e208-9bea-35ba-8504-73b423682d58 | -13.0044 | -54.8282 | 2025-09-06 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 149a9629-7789-3473-869a-bd95676e36e9 | -19.9047 | -57.9421 | 2025-09-06 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 8a29aff1-1b16-3f1f-aedc-a303535af41d | -14.1993 | -53.054 | 2025-09-06 04:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 3cbc442a-4c4a-30cf-bec5-87adfb6a7563 | -12.9665 | -54.8116 | 2025-09-06 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8a84e7cd-3151-325e-a2b6-c7289309e960 | -14.18 | -53.0564 | 2025-09-06 04:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 2a5f13ac-fb3f-3fc5-bcc9-cf63703d0273 | -19.9047 | -57.9421 | 2025-09-06 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 62e16c33-e6b8-3f34-a634-3e63a91edccc | -19.9051 | -57.9213 | 2025-09-06 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 2b64df5c-0ef1-30b2-80dd-e7d83bdcc1a5 | -2.47185 | -47.77306 | 2025-09-06 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17c7789b-262a-3936-9879-1fb8d1070142 | -2.77659 | -41.79985 | 2025-09-06 04:14:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6fc1839-8a43-3b26-a212-d8f0116f8e94 | -2.56177 | -47.70116 | 2025-09-06 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f023f810-69c1-3f64-bfe9-951b8ef9486d | -2.4712 | -47.77697 | 2025-09-06 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b11a9efe-ed8a-3d10-a0d5-bda10e00ebb4 | -2.77326 | -41.79934 | 2025-09-06 04:14:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d442c0f-d050-38e2-89ea-54b4564fecf6 | -2.77604 | -41.80331 | 2025-09-06 04:14:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f87aa1b9-a916-3a7c-82ec-a3cd2eb417ac | -3.11573 | -40.83577 | 2025-09-06 04:14:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37a09485-9bd8-3f23-945a-66ad57d565e3 | -2.77271 | -41.8028 | 2025-09-06 04:14:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd8d1432-6bff-3adc-ad4c-be00a0d71b2d | -3.11234 | -40.83524 | 2025-09-06 04:14:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f9753393-05c3-35db-a77a-6af16ce290ea | -13.72035 | -46.91341 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89716c69-ed11-3286-b411-7c2de19be911 | -5.82977 | -43.97403 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2143891-4938-3fd8-8eb3-09bb12dc781d | -4.56701 | -40.34505 | 2025-09-06 04:17:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 82fc6a6b-7aa8-36f6-8d80-5ce9bdbc5005 | -8.45349 | -45.03743 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c1e66a30-7889-3ae8-878a-8a9206d3fc28 | -6.25309 | -42.42941 | 2025-09-06 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 36b50d4c-4d48-3aa7-bec6-044bef996afe | -6.27825 | -53.44257 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0cc54eb-34bd-3fed-9c47-e410acfa323b | -5.21426 | -43.69562 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| daaa5326-fb88-3350-83e5-7ba0634bb20a | -6.91443 | -43.81047 | 2025-09-06 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68bd5754-3bf4-3cb8-a904-e8fcdbd67f9e | -15.18181 | -47.98904 | 2025-09-06 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f5b4cca-7002-3364-8265-51313ec38155 | -4.63409 | -42.52732 | 2025-09-06 04:17:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7f81844f-9e8e-3304-8ec1-7b459d81c78f | -13.29119 | -46.84346 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7c8c43d-21ac-3531-a476-74bd1436a0f2 | -5.908 | -43.35344 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47fb5071-d8c7-3c60-9d63-c0266e054bd0 | -3.9667 | -43.23975 | 2025-09-06 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 429ec53f-d9cc-350b-bb10-887e37e15300 | -13.75091 | -46.93146 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2c1d613-1af0-398c-8a79-99701a08ed01 | -12.93255 | -48.04456 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7cb68e3-ce89-30be-b3a6-8749a83adf90 | -12.95639 | -54.78871 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22681d2f-2ceb-3675-80e6-e0dae8c7421e | -6.22191 | -42.60657 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e192179-4a6a-3e1f-8cf9-b50d20c37705 | -12.95969 | -54.78484 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f484b217-2920-3f14-9a72-81f55b7fc951 | -9.80152 | -48.33173 | 2025-09-06 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05a7683a-b1f1-38fc-bf6c-d1f840c8f127 | -13.01984 | -46.65385 | 2025-09-06 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e94f596e-359b-3ccb-b2e2-e45102f7822a | -3.36782 | -49.16083 | 2025-09-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe2716bf-8cec-332f-9be1-48a249b6cb53 | -14.79678 | -48.11438 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e5dfe1d-646e-332d-a85f-1e539f14e87c | -6.03513 | -43.69971 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43c79015-44ef-3701-ab61-e1564a6785ba | -8.06876 | -52.37676 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 622546dd-bcee-3a41-a9c1-8caebc39c29b | -5.97745 | -53.6028 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6addf50a-14c8-3b30-9201-c9d1376e8af7 | -13.00172 | -54.83872 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02d02a46-6ee4-36c1-9dd6-bb3f8d772c58 | -6.15544 | -43.1794 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 838c4c92-c58a-35a9-9ca7-d38129b636ec | -15.9803 | -42.38634 | 2025-09-06 04:17:00 | NPP-375D | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c2852099-4dd8-32dd-bfc4-96b7e19e5999 | -5.72825 | -45.36891 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 983d8efb-d2ba-37be-bc54-ca558742a332 | -15.18064 | -47.98601 | 2025-09-06 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6c48942-a502-3390-acc7-469efb288390 | -9.78173 | -46.905 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18471310-a81e-38de-8d13-1d9d7ad87975 | -3.38227 | -47.61557 | 2025-09-06 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6daae745-c83a-3764-8ede-fc20ba0a77c7 | -6.23665 | -43.28458 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03d8b4c3-6562-3b76-b3ff-bf7d31c0cf46 | -3.42808 | -49.04837 | 2025-09-06 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d551c92-1053-30b3-9fec-6a3b8d9419a4 | -4.50024 | -42.88571 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d962d9d-6cb7-30a6-b4fb-af5e336a6c83 | -8.93725 | -48.65008 | 2025-09-06 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e64f4865-6659-361b-bc9c-c70118f6a26e | -4.86332 | -50.82623 | 2025-09-06 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5bf66452-e0cb-36a0-9e4a-75a7a44dc16d | -9.7057 | -49.48518 | 2025-09-06 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| df1304c7-a0c8-3567-826c-a124fa4a7271 | -10.02456 | -48.34003 | 2025-09-06 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8668740d-220c-3241-8bc5-4002ac35068d | -3.69139 | -49.57216 | 2025-09-06 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3d2b761-d303-366d-a32b-98ba35f33e4b | -5.91121 | -43.22575 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6260bce4-7fcd-3480-af74-97de9d0756f5 | -6.0693 | -43.29694 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6dc3b3c5-89b7-3401-a8db-b0b3f2eddb49 | -16.91758 | -45.74722 | 2025-09-06 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd080c74-ed39-34e7-b2be-12f5706eb9c6 | -6.38422 | -43.0161 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 177da254-18ab-3699-a1c8-2cd964e28f6d | -9.70924 | -49.48981 | 2025-09-06 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0e208318-5058-3b98-869d-095f6e6c6783 | -6.51419 | -43.07189 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff442338-0ce1-3b48-96af-0c0b0965537a | -6.16775 | -44.30916 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dd6ebabf-15d4-3dbf-8be5-531e44c9e318 | -5.8714 | -46.10242 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca3f5a85-c0d7-3314-ae45-46326c8c74a5 | -6.17983 | -53.26223 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61d30b71-8be4-39c1-924a-f9da0cf8ac38 | -6.012 | -46.6992 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9b9fb4e-b8c9-3e8d-b778-594af875357f | -12.95091 | -54.79932 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7177f12f-fcca-37e2-865a-37e621139ef7 | -6.24052 | -43.28163 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e09a230c-aab4-3e3b-ac4b-4b88af5c8df8 | -6.51752 | -43.07242 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0a41844-4149-3e84-9381-02bd1727b5d4 | -5.71979 | -45.44395 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4741915e-3712-36ad-a04b-425f4bd9472f | -5.75619 | -45.53057 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e665549-2627-3806-ae49-e16bbbbed13b | -3.24261 | -50.8087 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3a2b2a6d-7027-3bbd-b40e-ec92dc3038bb | -8.08562 | -45.32283 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4530ac93-ac38-38de-95d7-3b87e2c1b8fd | -13.00408 | -54.82682 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 83bddd6f-f83e-379d-a4d8-1fd25846df50 | -13.00895 | -54.83189 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d1efaa40-1f04-3558-9364-192b1fe965b5 | -6.22524 | -42.60709 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 065a6193-b3c4-3f45-9e11-0cd0f0bc1a18 | -16.91425 | -45.74664 | 2025-09-06 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e7ee138-d8f7-3b93-a63a-245982ebee01 | -15.53987 | -48.40435 | 2025-09-06 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 974e0c4b-8711-30dd-993f-ec889bc30292 | -10.06633 | -48.06706 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fab6a6a4-6b98-3bba-809b-b750e3a6992d | -8.64128 | -45.74607 | 2025-09-06 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7ea4ef7-f6e9-38d5-8916-67df98a02d9c | -5.74865 | -42.75597 | 2025-09-06 04:17:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0ad47c87-c7a6-389d-b3b3-799e1b73c893 | -8.88315 | -47.2574 | 2025-09-06 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e031ae0-e12a-3c9d-b757-e3b19bf8477b | -6.91237 | -44.16796 | 2025-09-06 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README31.md)
