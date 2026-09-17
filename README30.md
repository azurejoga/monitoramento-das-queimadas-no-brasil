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
| 7610d421-11ac-3d64-8473-aab933035c92 | -9.03888 | -47.75594 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bda7d28-89cd-3038-98c1-566e89ea48dc | -7.13493 | -42.17065 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 96d6c832-bce0-382b-9453-3f1186d36823 | -7.10982 | -41.82499 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6b5d0c92-3a06-36a2-8ca3-7275db33515e | -12.52262 | -45.96574 | 2026-09-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21156c11-90c9-3ba8-a632-71f928253b1e | -10.11543 | -45.57187 | 2026-09-17 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96349302-9e91-354e-b8b2-314bc14446e9 | -12.19425 | -43.4799 | 2026-09-17 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03ef1d2b-205b-38fd-a736-0d3ff9c7783c | -8.85801 | -45.8631 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc788826-aeac-37ac-ade0-5d6206e164c5 | -12.45419 | -50.8223 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b95cc2b7-47e3-3c4a-a5ad-b123ae523f19 | -11.16238 | -42.78995 | 2026-09-17 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 12a4e6ab-4bf7-33f1-a34b-e8e61715066f | -10.82209 | -46.17525 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27cb03ba-2ea2-3384-bfba-f5fa1dbd70a1 | -7.17505 | -42.10518 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 914832ea-8097-36d0-b928-a58b5e5cdc51 | -10.50318 | -46.33538 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65a5fb06-4579-3910-80d4-466be855c6b0 | -9.85402 | -48.3903 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 29e28419-6081-3f0d-ace1-a4ee7a0c7cb5 | -6.67078 | -43.64584 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f1d56f5-7f46-3837-b39f-5b6e9f04f1d1 | -9.8469 | -46.91462 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9784528-ed43-3160-b357-5876751e94da | -7.02571 | -42.06974 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0da7611c-1977-39b7-b00a-a84b1b61fe2a | -7.03317 | -42.07445 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 252bd32e-761a-31d2-b9ad-47013973f076 | -8.25458 | -42.16825 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eed09998-086b-3ca7-be84-cc793387f8aa | -11.64416 | -47.33457 | 2026-09-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fb2ee12-1c5d-38a7-8522-c175caabda82 | -9.56752 | -46.58052 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13154fff-d57e-38f5-90db-ed9763eccd43 | -12.45451 | -45.88058 | 2026-09-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d89482cc-070c-35ec-9d0b-90016974adf6 | -11.13505 | -49.0456 | 2026-09-17 03:55:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ddaa539e-4762-3ceb-a9d3-712c918598ad | -9.11959 | -45.72493 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 6759d1f2-e0ba-3cf3-9f2a-8350755add6e | -7.12287 | -42.16853 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2662321c-2ea9-324f-9db6-6eaf72dcbc6b | -7.12323 | -42.08573 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8649f985-df87-3d28-80ff-26ea9e0a0275 | -7.0831 | -41.77141 | 2026-09-17 03:55:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 196adebd-8251-38d0-bed3-bc146c173481 | -7.37147 | -44.48043 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97725169-7bb0-31c6-80d4-f4154876d8fa | -11.58895 | -46.88041 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4b5dba3-2928-344f-9b1c-3210edd59fe6 | -11.89029 | -47.58091 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfa8a0c5-4572-3919-804f-24fd62b9f8ac | -11.97862 | -52.46448 | 2026-09-17 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42a0dafc-b560-3412-828c-e5b9285e7c34 | -11.3354 | -47.25004 | 2026-09-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 131ca1a1-7e03-305b-a29f-03f669cfb329 | -12.50016 | -50.82683 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b2ccc04-d9b7-344e-bf24-addac224e4b7 | -9.61818 | -45.35076 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2fa0cd25-eca9-3fd6-adf3-f21c33cbc1d8 | -11.53179 | -46.87467 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6064e6c7-1888-3aa6-88c4-203b4cfd5d20 | -12.70787 | -48.27539 | 2026-09-17 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d1e7415-51f9-3021-b8a4-74dd80e45bd2 | -11.27202 | -43.46772 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e285da0-0ab9-3d61-811f-d2e34b475042 | -8.25587 | -42.18456 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 022b2cca-a1da-3ca4-ab8d-baf18849384f | -12.4519 | -50.83321 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b443cfff-0556-316b-812e-6256624b2c45 | -11.8934 | -43.83273 | 2026-09-17 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b24b7d90-27e5-3304-b7fd-b171a38262fc | -7.4621 | -42.10476 | 2026-09-17 03:55:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bec94181-a061-3669-82f1-4da91b742c49 | -7.04389 | -42.04375 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 86447146-f51a-35da-9c85-9ea9f8d97d51 | -12.47868 | -50.83346 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ed8e6339-30cc-3a43-a37e-8e5d6b751a54 | -12.46472 | -50.83606 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 4b1f40b7-7c0d-31bc-a5e1-0d9de60b90ef | -9.60008 | -45.34158 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f7cea6db-54dd-302d-bf61-6449abdf38de | -11.2583 | -43.4499 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b43950c0-31a1-361a-ab36-29929f2820f2 | -11.27611 | -43.46846 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95eac1c6-936d-3843-8fd0-6de69f39ec28 | -12.49036 | -50.84176 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 01cc3852-9fb7-3dbe-8ffc-1902d871fb9d | -12.49224 | -50.86509 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a2404ec-5f3f-3d84-a45c-ce6e8d4ef4b7 | -12.49673 | -45.9155 | 2026-09-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bf979da-bd3a-396c-9a3b-084b5fab986d | -8.27037 | -42.17115 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e586d38d-d38f-3c29-ad2f-a55985039201 | -7.59915 | -46.3222 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d8ff68f-500c-37cc-b027-aabba9c5f54e | -11.20117 | -42.82328 | 2026-09-17 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 90f6a1ca-1405-3c2f-b930-733bb5b7bdc6 | -7.44171 | -45.29187 | 2026-09-17 03:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e510874d-55d0-3dc7-b60f-9fad6e934adb | -12.3763 | -48.46082 | 2026-09-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f1c436f-bcb3-3b4f-930e-a6f3cb48a6b4 | -6.67524 | -43.6467 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9479482f-1e35-35dc-9b84-0bab6ccf1796 | -7.0858 | -41.84699 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5a32268f-cada-3099-a4a7-68a495e69400 | -8.88192 | -36.58597 | 2026-09-17 03:55:00 | NOAA-20 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fea961b1-69c7-3ee3-bf50-c3214f200ad5 | -12.50452 | -50.70926 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a9c60b5d-1ac6-39c7-996a-8e939a3735c6 | -7.12627 | -42.17278 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8bd062f9-e7b9-3943-ac8f-75dd41259415 | -10.30814 | -45.26984 | 2026-09-17 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdb4475c-c4d0-3e50-b392-05bc4ee90b47 | -9.55234 | -45.41501 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f9bcad5-1ea7-3965-8f17-45f6dece1621 | -6.77903 | -48.66245 | 2026-09-17 03:55:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9bcd153-6b6a-3af0-9d17-9b31a8dcd1b2 | -13.3918 | -40.06297 | 2026-09-17 03:55:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8c78e9fe-2981-3dde-9078-cb75ed4680f4 | -12.45533 | -50.81685 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| efbaea97-99a2-37e7-8011-e87c09f7d232 | -12.47968 | -50.92568 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b15e34d-2fae-3197-a093-0ae31753708a | -12.48696 | -50.85817 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c02ece08-7acc-3d97-8924-a6ce000e65c6 | -11.28298 | -43.47738 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2571953-29c2-3c01-9d0a-128f986f4b97 | -7.0263 | -42.0662 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c1051200-f914-3722-8d2e-647f4055a09f | -9.88378 | -48.39197 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8abbfc57-afef-3d3f-a669-8cea44d7f785 | -7.02521 | -44.6256 | 2026-09-17 03:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65dc7c63-f336-318c-8f14-a3b7067b3c97 | -8.85868 | -45.86143 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e93d5326-668b-3807-881c-385fd80aa71d | -12.48322 | -50.81166 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9e02692f-20e9-3f6d-b391-ab7cf5459727 | -13.74343 | -43.756 | 2026-09-17 03:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23bc49fa-fc1d-3cbf-8202-05e656f4c94f | -12.45475 | -50.81682 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| ef40c5b9-b3e7-33e7-ac9f-a29c2063011d | -9.31081 | -40.24517 | 2026-09-17 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2178d178-5b8e-33df-aed3-1a046abd2d8d | -7.08225 | -41.77313 | 2026-09-17 03:55:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f97c22cf-86ae-30b0-848e-b22e3d7c9595 | -13.43597 | -43.81348 | 2026-09-17 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 18edf1c9-4187-3653-b67c-2ad2ffbe7bbc | -7.38023 | -44.51252 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ae19c2e-5f6b-3d33-9516-fc734ddb30d0 | -11.27136 | -43.47142 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91e55a8f-1c14-36ce-b2a4-fef225fd5546 | -10.1194 | -45.57742 | 2026-09-17 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a060fcd-c592-3423-b2c6-40f6bc4567db | -7.97184 | -44.83925 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27421b9f-7fd1-3d91-9b7c-6a5655811996 | -9.88301 | -48.39607 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0a1b334-ae03-3d34-9c8a-3388ee0687be | -7.36677 | -44.47972 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4478ab1a-5e30-34ce-bf6f-f359eb46cc39 | -8.38956 | -42.20432 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 3235b2ac-0f69-3010-a325-098d320413b5 | -11.57039 | -46.86647 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72d39bc3-a447-3a2a-bec5-e0e98ab93d13 | -11.52837 | -46.86484 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53acaa99-f6bb-39c8-8e11-668652d6c3cc | -8.42973 | -47.75324 | 2026-09-17 03:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3eb3a05-6b02-355b-8d3a-3a8833afb7cc | -11.88742 | -47.61229 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09cd303c-8014-37d7-b83e-d509802f4770 | -7.04494 | -42.06157 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4f1304db-e931-3e58-9af0-ec34ee78d3df | -12.44724 | -50.82083 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e8adce2f-10e3-370a-a106-1a7518d0d2e9 | -9.12035 | -45.72704 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ff04b5e4-e491-3b5b-8f79-eff90c8880bd | -8.57988 | -44.57839 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9d103d96-2c5c-3019-8a99-b7d2af72e16f | -12.14633 | -48.26452 | 2026-09-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 540568f5-4690-3649-abd4-938ced5a436a | -11.21209 | -42.83055 | 2026-09-17 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d16b23e7-6c59-37b8-a8d8-fca48f74f62d | -11.88304 | -47.59005 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2589d03-03b2-3238-bdfa-422284ca6d12 | -11.88445 | -47.61174 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3a82a9d-e9ef-31cb-ab44-680cf9504a73 | -8.57901 | -44.58328 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b98aef68-becf-3244-a169-b43746e6e365 | -7.58736 | -46.33391 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 051b1c32-9376-3149-9ea9-ff0487e2800d | -12.49677 | -50.8432 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| d541d6e0-d442-3551-a293-4b1af37b7540 | -12.4473 | -50.85507 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README31.md)
