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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fee710a5-014e-3ebe-a4f7-b857bfe1fe74 | -14.76758 | -47.15029 | 2026-10-07 16:35:00 | NPP-375 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 93857425-6db8-3961-a3df-31cd48b38129 | -11.73888 | -43.4241 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 13ac375e-e889-3a50-b115-f0d88f4ee456 | -12.23108 | -44.72725 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 16e07b01-2666-3e3b-b485-5181c668d74c | -13.75547 | -48.3898 | 2026-10-07 16:35:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c1d18fa8-247d-30c7-9bef-f29962ef83d3 | -18.38853 | -40.31759 | 2026-10-07 16:35:00 | NPP-375 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| 76fe5786-ed93-326f-a147-ce5c309e9c85 | -11.22883 | -45.28438 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2f7acf48-e62b-3f42-bb50-c316db2f2807 | -11.72169 | -43.42316 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f4b4d3e4-f244-3987-bf72-a8daa3fe32bd | -14.43522 | -41.13537 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| d2f188be-eddc-3e7e-95e0-4078935e2b58 | -13.89315 | -49.13111 | 2026-10-07 16:35:00 | NPP-375 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9592b6bb-98cd-3df7-b411-584f5d7e8196 | -11.63926 | -43.68649 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 5e900a58-dcb3-365d-882d-2e0d3f168dc2 | -11.23731 | -44.85766 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 85bc811b-702a-3fd3-8f8a-ced4fd9f1143 | -12.19377 | -44.77577 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e8f0e2f8-68af-37ca-b529-6b5a07f1e6c3 | -11.83869 | -47.37873 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 18056323-48d2-34e5-bd2d-f9deb3057619 | -11.25771 | -45.18929 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ca554282-67d5-338c-8d7b-b45d5fab991f | -11.23176 | -45.27998 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| e1315805-f293-3f82-9933-9206b20fa83c | -14.24247 | -41.39489 | 2026-10-07 16:35:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 2b3a1893-7d95-36c5-9bcc-75b7c6c60ebd | -11.77374 | -43.54215 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 3385897d-45c7-38f7-9b74-dfc25bead676 | -13.66623 | -42.45414 | 2026-10-07 16:35:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 9bdc5184-6ab5-35b2-acb7-e413aef352b7 | -10.96095 | -40.44941 | 2026-10-07 16:35:00 | NPP-375 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 780e165c-516f-30be-9550-e822d728bfa9 | -12.1771 | -44.78217 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 37709bcd-dbbd-3547-9b98-315c2ec21576 | -11.80775 | -43.51869 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| daf0d38b-9f49-3cea-825f-bade87f8b320 | -20.15686 | -42.03034 | 2026-10-07 16:35:00 | NPP-375 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 49161793-30f0-34b6-a47b-2b36ab771ace | -11.84728 | -43.54077 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| cac6484b-2e56-3410-a9d7-1d2bec6a5eea | -17.79531 | -44.42239 | 2026-10-07 16:35:00 | NPP-375 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ca39b53c-d7d0-3e31-84d0-190d46ca1938 | -11.85203 | -47.32932 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 92356827-3cb9-3ef6-a1af-a02e676fb493 | -12.17609 | -44.75116 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5e9c2970-f17c-3ac7-b339-4f0fd1bf5d41 | -11.23675 | -44.8539 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d2de94cd-f5d2-313c-ad1a-1a09b52a9682 | -13.18594 | -47.88419 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bb9e6f8e-8ef0-3d7d-acea-1ad8a7c0f409 | -12.17487 | -44.76691 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 543.1 |
| 6baafa95-c56c-3469-9f6d-37cf3f0f4e3f | -16.84904 | -40.5904 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| c1aab525-2ffd-3f96-a3ca-3fdb073ab036 | -10.96447 | -40.44882 | 2026-10-07 16:35:00 | NPP-375 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f9fd89cd-75af-3c0f-b121-42d56d0e9df7 | -11.72734 | -43.65841 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 8936359c-0f17-370a-949d-640bcaf2137d | -16.85181 | -40.58611 | 2026-10-07 16:35:00 | NPP-375 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| abdd2017-1418-314c-91f2-54685c6c4737 | -11.6369 | -43.68392 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 7e91cb9a-dd67-3e25-a982-1744872dba04 | -11.76711 | -46.70771 | 2026-10-07 16:35:00 | NPP-375 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| a9e6334b-363a-3814-a44a-385fe14d32f4 | -11.22737 | -45.28059 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c809a51f-529d-30ba-8aca-ebd7fb731ef6 | -17.42043 | -39.81734 | 2026-10-07 16:35:00 | NPP-375 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 28a8d863-413e-3daa-9041-798cc95713fa | -12.99025 | -47.0655 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 6f103e39-2ff8-38d0-85eb-9fbb7393493a | -12.22091 | -44.72119 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1bb60753-0fc7-3554-bab2-cd9e612bb100 | -12.22421 | -44.72831 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a5a239f1-4a92-3070-956e-10521d7dbd9d | -12.82851 | -45.56261 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a00b4e66-2004-3c12-985a-0e957452938c | -12.33333 | -47.06211 | 2026-10-07 16:35:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d6c0548b-1509-3451-80bf-0ebfb7e0e3f5 | -11.22717 | -45.27277 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dd9e3a64-7056-35b6-a7da-e9e95d6d2be4 | -13.35875 | -43.86473 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 371c9311-d194-38d2-b2d0-ca82e28626b9 | -11.64434 | -43.67473 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| aa303964-2332-30c2-b5fa-0786099e06e0 | -21.90517 | -41.36821 | 2026-10-07 16:35:00 | NPP-375 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a66f3a05-a4a8-3647-96e6-d8d987cd2a9b | -18.03871 | -44.57721 | 2026-10-07 16:35:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2857b284-5467-37eb-b733-6975ba7912af | -17.8939 | -42.49118 | 2026-10-07 16:35:00 | NPP-375 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 460e0eb1-4a6c-3c63-ae63-d87465fbbf13 | -12.17776 | -44.76258 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0c6d44de-dd4f-3587-9656-888edf9b4270 | -11.25425 | -45.18984 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fc8b1607-5cb8-3954-93a4-2339326e1bce | -12.163 | -44.73374 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| bab75ea1-c3e5-3f45-8e14-5e1eea97d79e | -14.10251 | -41.53326 | 2026-10-07 16:35:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fde8fde1-6dad-3d36-8926-0909daf0ede2 | -13.38799 | -43.87527 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8879bcc8-23f9-3d89-b020-191124580fd9 | -12.1732 | -44.75549 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5cfb5692-3aeb-380c-a8c2-a81f68f07ab7 | -11.73397 | -43.50471 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7d288c76-9865-3f49-b1f8-280a2fae9de8 | -11.22772 | -45.27665 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| de83fbcc-ca44-37fd-a8a6-096737fb1e62 | -12.16588 | -44.72941 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1ede19b8-5342-32c0-96b3-0e9ecd9c0844 | -15.78307 | -55.08262 | 2026-10-07 16:35:00 | NPP-375 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b7c7b848-0c41-3da9-852a-be1732dbf84a | -10.45353 | -36.84181 | 2026-10-07 16:35:00 | NPP-375 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| deda93a9-50c7-3860-b42c-fea619432d14 | -11.59985 | -40.09153 | 2026-10-07 16:35:00 | NPP-375 | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 68eff5cf-5873-3ee2-bd11-96d77306a991 | -12.41239 | -38.21075 | 2026-10-07 16:35:00 | NPP-375 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 3991a170-2e9b-30f0-ad10-3df588506296 | -12.17654 | -44.77835 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3a15d355-06a8-3cb8-a3eb-2ea2c3c35aa3 | -11.84445 | -47.30686 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8b459efe-998a-3a68-bfad-f8c979b45092 | -12.33602 | -47.05973 | 2026-10-07 16:35:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 185457f6-5429-3d71-b8fa-a8e2ab96e6ec | -12.20375 | -48.42719 | 2026-10-07 16:35:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| eebb2612-0bbd-3327-9f6c-a6a33046494e | -13.10811 | -49.00338 | 2026-10-07 16:35:00 | NPP-375 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c4355f86-3a95-323b-b2dd-5382773171ff | -15.25633 | -48.51614 | 2026-10-07 16:35:00 | NPP-375 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cf7a5415-c108-3001-b800-8b4002f4e7ae | -10.94996 | -39.27824 | 2026-10-07 16:35:00 | NPP-375 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2320796d-9879-351b-912c-5488cf94da3b | -11.73451 | -43.50826 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f6cbe8ae-c526-32e7-bd40-b2dcbe51294b | -12.44461 | -47.80809 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bf65709e-a7bd-3411-b9b3-81980bf25c86 | -13.69408 | -49.11146 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dd1a2354-96f7-37d6-b5bd-19df4c2d3a92 | -12.17599 | -44.77454 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| dec4cf3b-ae29-359c-b724-7d5cf75478da | -20.33606 | -41.57065 | 2026-10-07 16:35:00 | NPP-375 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| fc36b13b-c8c7-377e-85df-3890b4f05f91 | -13.88892 | -39.52026 | 2026-10-07 16:35:00 | NPP-375 | NOVA IBIÁ | BAHIA | Brasil | 2922755 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 371fe2f7-8228-3dc7-87e1-d799c29beb32 | -13.68777 | -49.0983 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 49427a0a-a64e-325c-8bfc-866c4d720f03 | -11.62058 | -43.62106 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 283.7 |
| d333af89-922a-3224-8084-636762457d56 | -13.59265 | -43.17019 | 2026-10-07 16:35:00 | NPP-375 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 018e8b78-f68f-3f4d-a8b3-6da97c22dd45 | -11.64381 | -43.67118 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 904297cc-73f2-3510-83d5-bca04f4a8bbc | -18.13501 | -42.66224 | 2026-10-07 16:35:00 | NPP-375 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7eec5f7a-d90c-36da-99e2-ac7e857e66e0 | -11.85889 | -40.19882 | 2026-10-07 16:35:00 | NPP-375 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9ca6baaa-cb1a-3fa5-aa00-b740de53ae02 | -19.21424 | -43.14426 | 2026-10-07 16:35:00 | NPP-375 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ba6113a1-ded1-3538-9a9f-5b91d8c2f4b1 | -11.77086 | -46.70712 | 2026-10-07 16:35:00 | NPP-375 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3e09611c-5790-3d0f-9e88-1e8594544430 | -19.01359 | -39.88152 | 2026-10-07 16:35:00 | NPP-375 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 31872ef7-4f43-331c-bd31-9e68cfa43188 | -11.38643 | -37.62669 | 2026-10-07 16:35:00 | NPP-375 | UMBAÚBA | SERGIPE | Brasil | 2807600 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 940d7ce5-f277-31fe-8877-591ea0fe32e8 | -17.88516 | -41.5112 | 2026-10-07 16:35:00 | NPP-375 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a6cf5202-999e-34b9-ba40-61953f6e5a22 | -11.51643 | -42.67595 | 2026-10-07 16:35:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 4d27df31-91c6-3513-b4bd-6cdf46963394 | -12.17999 | -44.77784 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 312.2 |
| 82d7ea08-8718-3676-b7c0-74b09d003225 | -12.83268 | -45.56622 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ad4505da-4ac5-37e1-891f-44df1086f998 | -11.22416 | -44.86357 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a353423b-9b89-33a5-a70c-a288bf59f413 | -11.51499 | -41.70639 | 2026-10-07 16:35:00 | NPP-375 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| fca7c5bd-d0a4-32af-b4b1-fffbe4417fcd | -14.4912 | -41.60086 | 2026-10-07 16:35:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0e9282aa-0b5f-3b1e-b374-8603565a3826 | -11.75066 | -38.44887 | 2026-10-07 16:35:00 | NPP-375 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 695f83ee-c60e-3a60-b6ac-edc6e2c7d919 | -11.71797 | -43.64162 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| af89b670-e37e-308f-ab94-8ec745e1b32f | -11.22606 | -45.26505 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d56fac20-6b66-3031-9f0c-0e9e18fd09d6 | -14.84759 | -47.31805 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f6221cff-e300-34bf-9a67-5c787d1aff7a | -11.22843 | -45.25681 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 73de044b-7e7e-3323-a630-e3ca7d1f4e1a | -14.77312 | -48.81878 | 2026-10-07 16:35:00 | NPP-375 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1fc3699a-f163-3405-862e-cd0b23a53581 | -11.47163 | -43.39806 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| fdef5bb5-7b24-3ece-8d41-a11909fefdd6 | -11.124 | -44.60866 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4d0ffa02-907e-3270-86d9-1b57b1a4642d | -12.19597 | -44.64744 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README180.md)
