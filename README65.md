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
| c82c1912-0c44-3a97-8a57-d0a82c0b657e | -10.27727 | -54.25358 | 2025-09-01 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da1e55d7-afdd-3c49-9fcc-c4e4221cd985 | -13.33588 | -46.97271 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bef00d15-a4ce-399e-ac3b-80f3936016f0 | -17.15732 | -46.08262 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a11f713c-e8b7-3a27-b66b-116dd452da1f | -14.83614 | -46.73221 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0193ef4c-694d-3f2e-9ede-af6d9b6bdaa4 | -11.96486 | -51.3543 | 2025-09-01 04:34:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7056df93-134e-390c-9372-549f48cecf96 | -11.80242 | -44.94294 | 2025-09-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4670e939-e2dd-3229-a7f9-fb502544646d | -11.45935 | -46.79649 | 2025-09-01 04:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27da05c4-cb24-35f3-868b-b9d4c8632d8a | -14.7608 | -48.17374 | 2025-09-01 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ead0bba-76d0-3837-8448-a3e435ff0f72 | -11.80112 | -44.9441 | 2025-09-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ad9a69e-e904-38b3-abd7-36dba515c469 | -12.56508 | -44.79025 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 033e4d84-cba2-3c33-a7db-a347cfa4278d | -14.78972 | -46.73693 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 102ac58c-9e60-3b8c-8ab3-057aafcbebf8 | -15.32578 | -46.11164 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a9fd695-1d36-3358-ae1d-0fcdaf3ba784 | -11.00132 | -46.93608 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf67c559-4ccf-3617-b74c-7feece1900cc | -9.44309 | -60.57405 | 2025-09-01 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce3eddd2-1797-3b14-b025-897968379a70 | -8.68333 | -62.40769 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1df99597-f507-3253-adbb-c5d090454338 | -15.72569 | -48.98606 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d3b040c3-7583-332b-8dd9-76ff5ba69324 | -12.97602 | -54.76027 | 2025-09-01 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05bc2735-0a1b-3700-b44e-2c5f36036f6d | -13.16542 | -45.28783 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dc6f1d63-db04-3df1-9714-52a4eb24fac0 | -11.5905 | -55.55612 | 2025-09-01 04:34:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d973ebd8-7bc4-3122-96f4-cbda7aff4f6a | -15.2219 | -53.78701 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9482797-3f00-36da-b059-c7e57817dd70 | -11.05515 | -52.04751 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e655e93a-a1b4-350d-b303-1117225751d3 | -15.6989 | -48.91441 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ff8baa7-85e3-3bb0-a1e0-df5b869db342 | -14.04635 | -44.56265 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f25f7670-d1b8-33ad-aa35-838884bd7859 | -15.6961 | -48.9328 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2cd74acd-a592-3f89-ae1a-603cd92b61e5 | -13.54692 | -46.96262 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c950193-e2a0-3013-a2e2-a78929a2d94a | -12.85124 | -48.07063 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75180ec4-79a6-3cbd-9a57-9435522a9bd0 | -15.08271 | -48.12645 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bab8b417-103f-37f2-a551-ef8e8cba0b57 | -14.75799 | -48.16934 | 2025-09-01 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82df6317-f830-3142-9f28-6e4a56ba26fd | -11.33736 | -43.67564 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fcd2d11-efec-3233-96e4-9ba9f81e7b11 | -11.90272 | -46.68137 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf9e2335-27d4-39de-add3-7ee7a4d7ecdf | -14.48627 | -52.98763 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6aca94d-f0ea-328b-a827-671cd65fb8ae | -12.60079 | -48.22031 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4efe0d03-a4c6-3ffb-a608-d7f450543b4b | -13.47673 | -46.97661 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71dcec14-8258-3bf6-a2ff-de50780ace93 | -14.75201 | -46.76936 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8765df2f-3b1b-354f-8837-df0f4783b8d7 | -11.96423 | -51.35812 | 2025-09-01 04:34:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8706f845-fd6a-3228-841f-1fd6ba26f5f5 | -11.04651 | -46.96252 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3559bff9-961e-3132-b4a5-da3592a4aac7 | -15.71224 | -48.89437 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad23a763-853e-32f2-93bc-3bab9d7a079c | -12.62633 | -57.0005 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5be204b3-e55f-3389-bf90-fa946174ba2b | -10.47267 | -51.62959 | 2025-09-01 04:34:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acf11fe6-a57d-3b49-9973-051fcc735acc | -15.23273 | -53.81278 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8155b3c9-2ef8-3254-98ac-45f3d00dc09c | -15.23595 | -53.79444 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79b689c9-59ca-3f11-b87e-00aadc301eb6 | -12.86967 | -48.07338 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b72bb09-dbc3-3014-8e25-2b9994b1b1db | -10.23307 | -51.10818 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d9c6e23-dbe8-3a7a-83dd-adc6435430dc | -14.42519 | -51.67138 | 2025-09-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| cd3967f1-5866-3216-87fb-c9221bb16f67 | -15.70056 | -48.9035 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6625bf9e-8353-3136-9060-3b1be726d253 | -11.03277 | -46.86729 | 2025-09-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe9c5f66-a017-3731-8221-adabeb401cef | -13.52284 | -46.9799 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de91f829-601d-394f-8732-df23fb30386f | -15.22772 | -53.79757 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9f1d694-75f2-3d46-8f2d-6cff947d7d31 | -12.96134 | -48.11678 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2049d130-9f81-3d44-b31b-d6d8fa5bb18c | -12.61397 | -57.01412 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9683f68f-45e7-363e-9fdd-4705789543ba | -13.33529 | -46.97666 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbaa8053-4f71-3fdd-a982-1142c2cf47d7 | -16.15821 | -49.63453 | 2025-09-01 04:34:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76b1a7e9-6251-3748-b488-46f64c93ceb6 | -12.40422 | -46.46281 | 2025-09-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4834fcf9-cffc-3d66-9671-a5aed464ca86 | -14.79295 | -46.72617 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0a8ddcab-6d8c-34cb-8d13-f6a9e522de48 | -14.86298 | -46.77504 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af79e33c-cf77-3f40-a99c-7844330853c1 | -11.47437 | -46.79087 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42af432a-1d88-3cbc-9e87-ec8cf2e2a047 | -11.8722 | -46.70957 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdadf4c5-af9c-31bc-82bd-57c1f8c07f41 | -11.95672 | -45.848 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 732b46ab-e52c-3ca1-b772-cb1ab8a670b5 | -12.82714 | -48.07051 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 384479c0-856e-334c-b9d6-89aa40c25a2b | -12.87551 | -48.17076 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6b605273-7d54-3ba1-8df4-183eda409d25 | -12.77954 | -48.08918 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4784435f-a299-3a54-b5c1-cc3362c02a28 | -11.37373 | -43.61564 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39e8c37b-987c-3efb-bf74-edf07fc033b2 | -13.47854 | -46.98876 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 250d870d-7f78-3a58-97f8-d1dd7bf59264 | -15.10369 | -48.14916 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ac1f15f-63ec-3e78-bf7e-fe90032c7d06 | -12.85905 | -48.06458 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 246c80a7-ae1b-3a96-a67e-f14ffe2cf0ce | -15.23434 | -53.8036 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b460e49d-54e8-3fd2-bd31-9df26ba4b09c | -12.82321 | -48.0737 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2a2e966-c2a5-3671-b705-b4ed019c665b | -11.87362 | -46.70922 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 185e5658-ac37-368c-8af3-4619ce823a2f | -14.84839 | -47.09777 | 2025-09-01 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ddb6c183-f22b-3dbf-bf53-e497b1f1174f | -11.04822 | -46.97436 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0412c77e-6b59-3a4d-b522-e13624c76995 | -12.63109 | -57.0014 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bd28cc1-1ef7-3769-90c2-05b6123ec529 | -11.418 | -46.90808 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44cb63d4-3156-3855-bdd8-2faadfd3d90b | -11.07389 | -52.06771 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45b04cb6-7ca3-3248-9b60-01b157c06c1c | -11.83081 | -51.50775 | 2025-09-01 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1ece1c4-5218-33bd-9f54-fe8bc7031f41 | -15.21673 | -52.33938 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27f9e578-dc68-3b84-8848-98e28bce334b | -10.23654 | -51.10876 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ffe124c1-0848-3dd7-b974-101d53423459 | -13.1727 | -45.2867 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d2abd6e3-8cd7-3560-8639-25dca9bbe3f1 | -13.69211 | -46.88549 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa8bd63c-c8b3-326c-8614-d952df52affe | -8.72113 | -62.4216 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cffd14f-9fe8-31ab-ae21-1a9c5e02a7e9 | -8.76052 | -61.44057 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd678049-d3fe-3aad-8aea-58295bd6d1b8 | -12.91016 | -56.98729 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0aa0862b-fb5f-3f7e-a84f-76f2e43fe27c | -13.70749 | -46.92833 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22fd4146-aa4e-30bb-99ea-026393505ad9 | -13.68031 | -46.86736 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85ae8806-d734-3ee2-87ea-8bcd8fd9f8a6 | -14.27225 | -46.26794 | 2025-09-01 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a179c454-1743-3934-a4a5-4196ff2ae13e | -15.69558 | -48.95873 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| dcd1a7d7-bba6-3e00-99ad-58e66569918b | -13.48789 | -46.99826 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 12c20e78-005c-3ec7-af8d-c5698734acb9 | -13.39004 | -46.95212 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30944494-ff31-3184-8292-86fc564a3219 | -15.23514 | -53.79902 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64ca22a5-ccb2-37a8-a599-36f5174fc3e8 | -13.47911 | -46.98484 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d767e084-b315-3d61-b594-949ee2041e73 | -12.79352 | -48.08779 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 686a13b2-3002-393b-8cbf-c62fa2b68c22 | -11.79508 | -46.43101 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4b963ce7-87b5-3fb7-83ec-0669b9dac470 | -13.32023 | -46.86049 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ec5bf828-5660-3bb3-aa1b-cb101bc98857 | -12.80473 | -48.08199 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41e09203-d5f3-3593-b5ea-c5ed7c7ec865 | -11.78737 | -46.45837 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36692cb4-e8ca-3834-8732-f3176229a83a | -14.04297 | -44.58777 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9f799e2-dcc4-38ef-85d8-8ecb11e7257e | -16.28812 | -52.93719 | 2025-09-01 04:34:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28ca1962-dc63-382e-a198-b419bfa06225 | -11.89349 | -46.74383 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19c84eff-0ace-3b00-ab59-1bf004f4e6d3 | -13.58053 | -46.93391 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73986f1c-1c2b-3a26-a2ce-dd1037f4cd1f | -17.7214 | -44.38377 | 2025-09-01 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57dc569a-24bc-3ea0-b023-b79c0da35654 | -12.65868 | -48.21445 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README66.md)
