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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6e8087c-9d3a-3b27-8947-4863f257e8cf | -14.8854 | -52.4167 | 2025-10-17 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| eed1b0d8-d8a9-3fce-b84e-3879edf18a27 | -13.2644 | -47.1007 | 2025-10-17 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 6604e42f-1e87-3058-9c91-6efe472c80de | -3.9822 | -42.4924 | 2025-10-17 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 173.3 |
| 7b4035f6-dd86-3bee-aa4b-4b64714e3cde | -6.7011 | -44.2787 | 2025-10-17 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5a6e5a04-136a-30b7-9485-3ec345020eb4 | -14.4086 | -47.8882 | 2025-10-17 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 341f64a1-4d90-395d-bcc4-adedc1f4b8dd | -10.1063 | -47.6525 | 2025-10-17 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| a8ec1909-dd81-3473-b1ea-75f29de97b57 | -11.3992 | -44.1229 | 2025-10-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 2d1cd1d6-a718-376b-a9cd-4ff0a840d3ca | -5.7992 | -42.4876 | 2025-10-17 14:20:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 6c5b4776-a193-398e-8281-69450d2b3d36 | -4.1525 | -42.1989 | 2025-10-17 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 183.3 |
| 76ffd26b-6002-3f8c-b952-eaab78f88366 | -12.8312 | -44.577 | 2025-10-17 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 9e84cf3a-217c-3eb7-88a9-a0878df63082 | -5.4561 | -41.0054 | 2025-10-17 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 134.2 |
| d45fa104-bb2e-3901-a614-066ed1e2df2e | -12.5342 | -48.1889 | 2025-10-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ca17c1e4-641e-3043-9e38-3be62bc163fd | -14.866 | -52.4193 | 2025-10-17 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a165dc75-fd87-3c63-bea6-0fa089352248 | -12.284 | -47.1544 | 2025-10-17 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 53a60df8-c3f8-3f7d-9ef3-744f84bfc40c | -5.8569 | -42.3407 | 2025-10-17 14:20:00 | GOES-19 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 4bbd2ab1-6337-391a-8e0c-5ba4a32fe471 | -5.2863 | -41.0673 | 2025-10-17 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 145.7 |
| 9797f72d-c762-3700-aed3-c2be827a7ea5 | -6.3919 | -41.5052 | 2025-10-17 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 5d73a64a-9fc5-3942-b1b7-55ccb6c09349 | -6.1532 | -40.9215 | 2025-10-17 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| b9ec52fb-ca9e-3d49-a5ce-e56b7ba58f5a | -11.9516 | -45.3632 | 2025-10-17 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 1661d10b-46ab-33ab-adee-219b9a0899b8 | -11.0214 | -47.3443 | 2025-10-17 14:20:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| f0406442-bf4a-33e4-aed9-eeafd94df007 | -14.8657 | -52.4405 | 2025-10-17 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f7358b3a-15a2-36d8-a84c-684edc109900 | -12.1682 | -45.0539 | 2025-10-17 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| cf3241b2-fd8d-3cb7-9fe9-9c73a51ba7c0 | -13.2447 | -47.1262 | 2025-10-17 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1ba60336-a46a-32d7-b2de-1934a5a70e60 | -10.6028 | -47.3955 | 2025-10-17 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 43ca5cb8-5c5a-3595-ba0a-7f1dbcfca017 | -13.4219 | -47.9511 | 2025-10-17 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c70888b5-880e-3df1-8c55-7bb61c835810 | -12.4678 | -45.4694 | 2025-10-17 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 3d2d1741-87c7-30f3-be65-a16e28e78f7f | -11.3603 | -45.2646 | 2025-10-17 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| c335fdcf-0115-3eef-b7cc-d79a6abb632f | -5.8718 | -44.7801 | 2025-10-17 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 5ddfd448-e4ea-31ca-a9da-e57ab3225d09 | -10.2558 | -44.0273 | 2025-10-17 14:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 18a1d936-b91c-3e04-87c8-e6c59a95333f | -12.487 | -45.4664 | 2025-10-17 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| e5a757ff-0101-397f-9f0f-0074eff4ef55 | -6.411 | -41.4793 | 2025-10-17 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 23d2718f-f0a5-3abc-b340-d669d61efda3 | -5.799 | -42.5112 | 2025-10-17 14:20:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| 26b114a1-0af1-3afa-96b2-30e447f862cb | -11.3996 | -44.0995 | 2025-10-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 800d9f74-f75b-38b7-be48-a3a2991c6328 | -4.4446 | -43.2164 | 2025-10-17 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 59891381-664a-3e1e-8dbb-9b63bdfe0c0c | -12.9607 | -47.9294 | 2025-10-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 43bf37f0-e9f7-3993-be33-88ea7be52f41 | -12.288 | -50.3789 | 2025-10-17 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 7c5f5a2f-291c-3b26-89d1-abd91017353e | -14.1749 | -47.9477 | 2025-10-17 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 5c0e68f4-4eed-39e3-9cd7-6c27ed6c4d78 | -6.4446 | -41.8608 | 2025-10-17 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 08d44d7b-d9ed-3a4e-9817-08ce52a942b1 | -10.8101 | -43.9275 | 2025-10-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c299d5ea-9056-30bd-8567-77deccee2b76 | -6.3921 | -41.4811 | 2025-10-17 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 9059752d-f610-3220-b38d-450da6a2056e | -6.4107 | -41.5035 | 2025-10-17 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| 8f4284e3-ff1a-3f8c-9bad-24f1262a5e99 | -4.1338 | -42.2 | 2025-10-17 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 18ecfde8-a2b8-380f-9790-ef71fef518c2 | -10.9942 | -47.8797 | 2025-10-17 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 044b86ab-d9e3-3af6-8e07-b67c21ab534d | -5.2489 | -43.234 | 2025-10-17 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 123b1a25-0a87-345c-babd-3e1f3551d631 | -9.879 | -47.6779 | 2025-10-17 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| e76d3c28-5b40-3978-9a73-2484c7272732 | -13.4215 | -47.9735 | 2025-10-17 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 75c49464-2243-3c08-ae68-ab432f33636d | -11.4585 | -44.0204 | 2025-10-17 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 9e6ae8b9-7bf1-3e9e-800b-57d5cd94bdf5 | -12.0879 | -47.4277 | 2025-10-17 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 0e9698de-fc66-39e7-a00b-0447f73d9883 | -10.9752 | -47.8821 | 2025-10-17 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| d8cd07ff-62b6-38c7-ab0a-7129addeed4f | -11.4188 | -44.0966 | 2025-10-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 9d77e295-0f92-31b6-a652-35a4219bc8be | -6.2012 | -41.7389 | 2025-10-17 14:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| bd03f64e-d30f-3228-8128-85b2ee7525a9 | -10.8797 | -47.9157 | 2025-10-17 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 90cf4b4f-19a4-36e1-b198-31400078474d | -12.1678 | -45.0771 | 2025-10-17 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 818a6b48-8cda-3468-9120-692c1bff0586 | -9.9828 | -47.0234 | 2025-10-17 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 6a77b969-1e94-3b39-a4ad-9578744223df | -10.5128 | -43.4525 | 2025-10-17 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 714550a7-87ed-3401-98c8-84c4345a84d6 | -13.4408 | -47.9706 | 2025-10-17 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 573413f8-e338-3cfc-be0d-8c4ce2247299 | -18.3739 | -55.4587 | 2025-10-17 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 8b5d9414-dee9-349f-b3fa-d56e469d6c2b | -4.1523 | -42.2226 | 2025-10-17 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 214.6 |
| 804c8ca5-e2e6-359b-beae-be6c4049c681 | -12.9459 | -41.8082 | 2025-10-17 14:20:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 111.8 |
| ec29034e-2247-351f-98d2-54c3b9a1c14d | -9.9831 | -47.0011 | 2025-10-17 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 8e069795-dbc5-31f7-b7d4-41d2d30d29a5 | -14.0905 | -43.6235 | 2025-10-17 14:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 91575f32-caa5-33f1-801d-e872f7531001 | -10.4945 | -43.4079 | 2025-10-17 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1eb3a23d-c689-386a-937a-033ff0b3b364 | -11.5724 | -44.0736 | 2025-10-17 14:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 7eeea0c5-2048-3d90-9b6f-8a2bf8c0705f | -5.8907 | -44.7559 | 2025-10-17 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 11e15c50-e5aa-34fa-9bfe-1d0854589640 | -10.9748 | -47.9042 | 2025-10-17 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| eb7e64e9-5c0b-3445-80ca-01a38f06c78d | -11.0024 | -47.3467 | 2025-10-17 14:20:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 007535f2-2261-3028-a4de-217d71b554a6 | -4.0274 | -44.1877 | 2025-10-17 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| b1c1fd26-a49f-3684-8025-1194a088ef26 | -11.2642 | -45.3011 | 2025-10-17 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 327.6 |
| f452f4b9-ad86-3e24-a1ef-70061f84e64d | -7.9814 | -44.1574 | 2025-10-17 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 191.8 |
| ef6f91d5-b686-3430-8aa9-8ccf66009dd4 | -11.0214 | -47.3443 | 2025-10-17 14:30:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 770f888b-1243-34bf-a23c-9c399b1d4c64 | -6.3924 | -41.4569 | 2025-10-17 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 9818bca6-08f1-35c3-a128-617f5350f60c | -4.0963 | -42.2021 | 2025-10-17 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 126.6 |
| 9747e920-b839-3709-82ef-759ccbffe4f8 | -6.3921 | -41.4811 | 2025-10-17 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 73c805a2-1e6d-3559-9213-2c0f17cc453b | -5.799 | -42.5112 | 2025-10-17 14:30:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| ef36cc22-6786-30b6-8b54-ae236349f225 | -13.2447 | -47.1262 | 2025-10-17 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7656f19e-1bd1-3ca9-94cf-5052b165765b | -5.872 | -44.7573 | 2025-10-17 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 32301701-d6c4-3344-aa41-9a64d9bb8e25 | -10.9938 | -47.9019 | 2025-10-17 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| cd9000c7-5085-34a3-81e2-59e7e0808b5a | -6.823 | -41.705 | 2025-10-17 14:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| d6b83542-a71c-3478-889b-c1cefccff9f1 | -8.2744 | -43.381 | 2025-10-17 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 8c537785-2f8c-3fba-bf07-5f73429d61c1 | -10.2558 | -44.0273 | 2025-10-17 14:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 3b351f38-05e9-359c-8f7a-040de0350123 | -9.9638 | -47.0256 | 2025-10-17 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| c9440b36-53b7-3662-b021-397d3323e837 | -12.0553 | -47.0966 | 2025-10-17 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b76da91b-a81a-3e4a-b9a7-3161e0893172 | -9.7602 | -45.3819 | 2025-10-17 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| df2451fb-f274-3e88-afa6-d30c375c3749 | -8.2185 | -43.3168 | 2025-10-17 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 738885ad-c012-3663-8041-1ea56d163ebd | -6.201 | -41.7629 | 2025-10-17 14:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| b4e87cf2-716c-36a2-a608-1622cf9b024b | -5.8907 | -44.7559 | 2025-10-17 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 3b9d7f2c-7d9c-3fcd-a4f3-b98f272f32d0 | -13.9127 | -45.5808 | 2025-10-17 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4d7ce986-14b7-347c-a7c3-da598153115b | -6.4066 | -41.8882 | 2025-10-17 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 8db9f5e2-1277-3118-ac33-0d8019dd8f8c | -5.2596 | -44.2058 | 2025-10-17 14:30:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 56ce8d30-b054-3025-9986-4edc53f7524d | -10.4941 | -43.4315 | 2025-10-17 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 286.4 |
| 48c3ee29-b222-35df-aeb9-b49f3f04a232 | -13.4383 | -48.1046 | 2025-10-17 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 217e45e1-9fe1-32eb-915d-9be08a2e3589 | -14.1749 | -47.9477 | 2025-10-17 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 3097dfef-73af-365c-bbee-4f8ac6d2d424 | -5.4558 | -41.0297 | 2025-10-17 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 3b12e50e-3388-38ef-8321-6656fd463808 | -10.9189 | -45.4171 | 2025-10-17 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0deed7ad-9443-3907-a598-06261eb9dddc | -6.3542 | -41.5087 | 2025-10-17 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| b450f1fb-a173-34e3-a94c-b2e11b1e49cb | -6.4255 | -41.8865 | 2025-10-17 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 335d9db0-409f-39ad-89d7-35e86464c53e | -11.1419 | -55.1869 | 2025-10-17 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 540bb2fb-21be-3a35-b352-5b82ee355cc3 | -11.4193 | -44.0731 | 2025-10-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 0780b78c-5bf5-3f8f-877f-1496b8a3990e | -8.3119 | -43.4003 | 2025-10-17 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 386.3 |
| 92985df3-01dd-32f1-8b73-f36c687daa8e | -10.4945 | -43.4079 | 2025-10-17 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |


[Clique aqui para ver as próximas entradas](README128.md)
