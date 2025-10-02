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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24d267aa-1da5-3152-80d0-89896551afc1 | -9.9447 | -43.77088 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| c1a27e18-5df4-384d-97ae-d7efdc080fa0 | -12.76335 | -50.56301 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5e2b8b29-1d52-3440-a495-ecbe1444ff34 | -15.2215 | -47.16664 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ec064b42-4a5e-315a-b83b-8da9903836cf | -12.82992 | -41.54549 | 2025-10-02 00:11:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 50.8 |
| fb14c86b-b7c8-3530-a83f-f9515e83c808 | -9.93489 | -43.69973 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5f0f5b8b-ccb2-320a-828c-7a59daa5bb57 | -14.85097 | -47.22409 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a2642b70-3b82-370b-b803-2415d7a6bcbe | -13.34828 | -43.67175 | 2025-10-02 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 730bad68-8886-3e59-9064-9ee21a50f1b1 | -9.93221 | -43.74546 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 402.2 |
| cd2f1804-8cf1-396b-a971-ec6cc569a8f7 | -15.17671 | -40.43741 | 2025-10-02 00:11:00 | TERRA_M-M | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 037bc5ff-e50d-3b85-8bb2-0d42482cc27e | -12.64994 | -44.23189 | 2025-10-02 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f6561e7d-3c33-39fb-9e13-f71c98a9b46f | -14.71245 | -48.20913 | 2025-10-02 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 75c3dd01-e7ed-3456-adb3-1bd7f3881ac6 | -13.21791 | -47.35092 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0e733413-ee9d-391f-95f2-b82a8fbb7a4b | -9.95414 | -43.57915 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2b6aa3c3-a972-3d88-9507-8e069aeff064 | -13.33062 | -47.80483 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 935c8b42-3887-3754-8b6d-9c513bb4e865 | -11.14296 | -43.38243 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 4ff6188b-d3d4-3b92-af6c-d05dc7865513 | -14.3601 | -45.97099 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e2f73164-0e22-3abc-86b6-9e9cb9bf521c | -12.70106 | -48.56324 | 2025-10-02 00:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| cbb0f078-2637-3578-a999-37a854d00aad | -13.37174 | -46.63221 | 2025-10-02 00:11:00 | TERRA_M-M | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 75ef192d-9b15-3652-a65b-70bf62bcf31a | -11.81721 | -45.02456 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 85b64f9a-0107-3bfa-b3ac-0831fa52ae8b | -12.93949 | -46.42789 | 2025-10-02 00:11:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0977a49b-3bbd-3245-af01-f84f667aa90d | -12.83145 | -43.8013 | 2025-10-02 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 73809628-d3b5-3cc0-a4a2-ccc1e28cdc74 | -16.87492 | -49.66594 | 2025-10-02 00:11:00 | TERRA_M-M | CAMPESTRE DE GOIÁS | GOIÁS | Brasil | 5204607 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6ee0b293-e192-3136-a86b-534fa08cbe29 | -11.20259 | -47.19751 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0ab533b3-34d5-316e-ac1a-652d8fba6e72 | -9.94882 | -43.67054 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3dff410a-e8fd-3931-9b3a-2ee8eeedec04 | -15.15847 | -48.38472 | 2025-10-02 00:11:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| df961dd3-642b-36c6-8098-7bf70d0d2ea2 | -11.45004 | -44.96141 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4193731e-532f-36c1-b7ad-0282e4b424a8 | -13.33938 | -43.67303 | 2025-10-02 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ae8747f6-4f63-3afc-96f3-ffa7d509a0a3 | -12.36768 | -45.78963 | 2025-10-02 00:11:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| afd8e75f-3923-34ae-a5fb-ac3ccd70552e | -14.97445 | -46.9142 | 2025-10-02 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b6b82279-2631-3ca5-8a20-78874bc2c8af | -11.83301 | -45.00246 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8718e3e6-bff2-354b-9aec-2a2d23c6e2ac | -9.90697 | -43.71013 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 59ec8b34-4f4d-3cd5-8fce-a5d824fe4edf | -12.86831 | -47.01041 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 10d03bd4-c331-3680-92dd-39db98bdf150 | -14.58558 | -46.72673 | 2025-10-02 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| db6acfc8-5d0c-3ac7-9cf9-a6fa36b6045a | -14.33701 | -47.12796 | 2025-10-02 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4ae2a406-dd59-3ffc-b5bd-f32b0812d0e9 | -14.5962 | -46.72535 | 2025-10-02 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| f246c316-f7f9-3e75-909c-f01d96b46f87 | -11.47483 | -45.00707 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| c6c64a35-e560-32e8-8e0c-bb16e2e1f6c8 | -10.65818 | -48.50531 | 2025-10-02 00:11:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 5867229d-8e69-3eca-aee3-298bc7571903 | -13.2053 | -47.33848 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 301d7412-0fd9-3bc5-86e6-c173ca676b68 | -17.11442 | -47.12607 | 2025-10-02 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 09c37857-814a-3cd0-9d5c-add3318d276e | -9.86595 | -46.88805 | 2025-10-02 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| cfec5b93-e232-37b5-81d3-89d9db12c594 | -11.13415 | -43.3837 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 4ba93fe9-f8b7-3834-93d6-a598ecf7658b | -11.4551 | -43.50998 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5ecc26f2-0830-37a1-8676-06e8d1afe4fd | -12.496 | -50.24877 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| abb60b3f-4a5d-39b1-907b-5bee693f7d20 | -11.17059 | -47.28082 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| c0dcba6a-4081-33a4-997e-4d49297ffde1 | -10.35303 | -43.73312 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3a42cb15-e397-3113-95d4-04c426832118 | -17.11257 | -47.11005 | 2025-10-02 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 451f304e-b586-37c1-89bc-7057e50fcc6e | -14.59456 | -46.71188 | 2025-10-02 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 5dfe2245-2c1b-3c2b-ac25-2f519eac6102 | -13.34951 | -43.68093 | 2025-10-02 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ccb13291-48bd-3222-a40d-331d617e4e36 | -12.48547 | -47.26889 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a7552233-6b09-3419-9bf1-a1b758d85f74 | -12.22689 | -43.76296 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e82637ea-d45e-383e-8a21-c448f2a40c8a | -9.94493 | -43.70736 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| ee5e22d6-daf1-3d9c-bc46-996c3dda0cd0 | -11.81589 | -45.01466 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9421953f-0fb8-3ff8-bef9-0953fa12f1bf | -13.2213 | -48.42779 | 2025-10-02 00:11:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ef9349e0-c63a-305b-a58f-2b866987caff | -12.50361 | -50.24256 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 33.2 |
| dec68412-23e9-3e48-b8c3-784f68a60665 | -10.83454 | -46.64405 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| fc209375-b68e-35fd-a80d-effa0519242e | -14.04099 | -48.0 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8916da1b-3698-3099-9349-6a692c88da0d | -14.36785 | -45.95192 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3777365c-a818-3877-88ed-3b97e79ad223 | -13.01136 | -45.23198 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 8b3a8fee-9216-3a1e-9465-0098000af102 | -13.40792 | -43.49822 | 2025-10-02 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cf5730a3-2c30-33be-a99d-26dd9e82d5e6 | -14.32147 | -45.98824 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 2dba9721-c59a-3971-a7de-549908b03ef9 | -11.86994 | -45.01142 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3f383022-3c1b-3986-ba33-77c43fb2e882 | -10.32932 | -45.25908 | 2025-10-02 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 81556ce3-ed9a-3abc-a44f-39124e432697 | -13.42195 | -47.80394 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 991913a3-7dea-3ec0-a444-572c79a3c0f2 | -11.8158 | -47.68671 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7e5b3541-a790-3cc8-af08-8457372dc763 | -11.94412 | -43.91504 | 2025-10-02 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 79e4f6dc-9420-3e08-8781-e338c494f979 | -11.77761 | -46.83621 | 2025-10-02 00:11:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a1df4db8-7cb5-3d1a-8d8d-caeef0e79a55 | -11.35526 | -44.94136 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4069be72-89ba-324f-8fbe-2d67e5a825c8 | -10.81307 | -46.63524 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b0190d69-b783-3196-bb8d-ca94e88f4cd0 | -9.93099 | -43.73657 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 11a8507f-75ad-37f6-84de-77feab395deb | -10.22514 | -50.34963 | 2025-10-02 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| e00d1cb1-3150-3588-84b8-5e645b7fd445 | -11.26984 | -47.8071 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 132d13eb-8f01-3592-b5d0-a1ec80a3b39a | -11.79358 | -44.98771 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e8c1c724-3a8c-396d-9551-645e0533afa1 | -12.83269 | -43.81047 | 2025-10-02 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5ff08f38-5286-3ddc-9e53-f052790c7fab | -13.01944 | -45.22034 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 408e69aa-e1cf-36f7-9671-27caa78f9399 | -9.9476 | -43.66166 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 61b24c26-3e52-3159-a93e-6fc94ac7db96 | -10.88949 | -44.28742 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0cfb5e76-7181-37d7-87fe-7c527a815663 | -12.41117 | -47.49591 | 2025-10-02 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b2b05b8b-8eab-3baa-9b4c-0ba7f678d70b | -10.93376 | -48.58813 | 2025-10-02 00:11:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6cf386bd-f26a-38fa-ae53-128f4da90902 | -9.93466 | -43.76325 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 35.4 |
| ea72bdd6-78a9-359c-a183-8781b1d13fa5 | -11.61711 | -45.04438 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bc972adf-d392-3998-b293-685e16c8080c | -15.77737 | -43.73752 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1ae091f8-e360-37cb-831b-0729d305f0c4 | -12.8012 | -46.86501 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f94ea8eb-2cc2-3a13-a0f6-c959401a72d8 | -11.80409 | -44.99637 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 88f346c1-353b-39ef-934b-ba392bc219a9 | -12.7769 | -44.91499 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5f050173-31e0-3ca9-8786-1ddc704f5a28 | -15.31785 | -46.28613 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2d32d635-3f7d-36fc-bccd-1c6ccb44c6a4 | -13.31761 | -47.20879 | 2025-10-02 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d8d144be-6ca9-36af-b3ac-bc2cdce8f2e8 | -13.00194 | -45.23328 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bae8e3c3-1972-3bfb-96d3-087b12f7f38d | -11.19212 | -47.19873 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ecbfdfff-6060-3a78-9f7e-8eca366bb0c6 | -13.24189 | -47.34214 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9052ae28-d337-3cfc-adcf-17bf2c2fc278 | -9.92854 | -43.71878 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 42.2 |
| dcdca25c-9dd3-3113-9181-c1d3bc9c3d7c | -10.79098 | -45.34435 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 099574d3-1dc8-3bb7-8460-a6b57a802708 | -10.80017 | -44.24078 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3b61977c-9b9f-3072-892f-4fa72f973504 | -14.40721 | -46.10535 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e6930038-552e-30d1-8ef3-b5f6177fab38 | -11.88971 | -40.97752 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 5954b8c6-0209-33d7-a4bb-d5461425242d | -11.35911 | -44.97013 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 895a44fe-3f32-33ce-9cd7-f1b455e896bb | -11.43624 | -43.50358 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4b298d49-4727-349d-90f7-388ccfed2b33 | -11.99764 | -41.14894 | 2025-10-02 00:11:00 | TERRA_M-M | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c54c58ef-7986-360f-9631-219604799365 | -11.38781 | -45.04492 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 5203794d-4089-3ef4-89cc-c79c2b3a04d5 | -13.31174 | -47.83987 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| e54a1c36-e441-380e-81e5-c4001db5bddf | -12.47475 | -47.27029 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |


[Clique aqui para ver as próximas entradas](README5.md)
