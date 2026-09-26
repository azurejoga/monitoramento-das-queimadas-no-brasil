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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f015765d-0ec8-35c7-a054-721e14282ed1 | -9.63472 | -55.13531 | 2026-09-26 04:27:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f49fee07-e975-3dee-b416-c32e2ba97399 | -17.42398 | -53.11976 | 2026-09-26 04:29:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fad41032-0ceb-3378-9f21-2f4b71bdb795 | -19.91037 | -48.25712 | 2026-09-26 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f7d25f5-bc23-39cf-9ee8-bc953255e48a | -16.76165 | -47.25555 | 2026-09-26 04:29:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b1f8f468-fea3-350f-aee1-9501dfaba694 | -16.25854 | -47.80805 | 2026-09-26 04:29:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b52d7ac-7add-3a58-b05e-255adc0d35ec | -20.33968 | -47.49005 | 2026-09-26 04:29:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b96d9a5-609a-32fb-90e6-cf1570912fc6 | -18.84594 | -47.53778 | 2026-09-26 04:29:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24153a3e-bbaa-3605-b230-a20c51e7d31b | -18.25593 | -45.59699 | 2026-09-26 04:29:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44943146-a49d-3b59-ad16-d73a57585712 | -18.53835 | -50.66834 | 2026-09-26 04:29:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bce9b24-3001-32d2-a67a-b8c2438710f9 | -18.24277 | -45.59089 | 2026-09-26 04:29:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85d83c27-3e84-3bf0-a282-af8cd9627110 | -20.49239 | -46.21582 | 2026-09-26 04:29:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| abc505e2-7b22-372c-bedc-cb9807951f4a | -16.56961 | -43.98816 | 2026-09-26 04:29:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dde0c93c-7c57-37aa-abde-d3e7f5c26851 | -16.5624 | -43.98697 | 2026-09-26 04:29:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df96533a-d06d-3c17-b4a7-98716d1d1ce3 | -21.23969 | -48.33496 | 2026-09-26 04:29:00 | NOAA-20 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 574a2a35-e360-32f0-b014-9fbfe165c548 | -18.23189 | -45.59316 | 2026-09-26 04:29:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed14b5c5-06d0-312c-92a2-f42ea3effe0f | -18.53907 | -50.66415 | 2026-09-26 04:29:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44d10537-dd94-3c33-a3c6-97268db827cf | -21.23613 | -45.61988 | 2026-09-26 04:29:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ef5e15e4-5112-37d8-97a8-d8f207c45c96 | -16.06829 | -47.06524 | 2026-09-26 04:29:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf02d94e-e985-305b-82dc-7b06e8cb1b81 | -17.13261 | -50.29592 | 2026-09-26 04:29:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 407809b8-8dd6-3cbf-9f80-ce56639acf3a | -17.37342 | -42.51529 | 2026-09-26 04:29:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f14543ca-1940-3c6e-ab54-b73037a10a30 | -18.24219 | -45.59481 | 2026-09-26 04:29:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc9c6594-7129-3a4b-8e73-d32cb31b8b53 | -18.54189 | -50.66901 | 2026-09-26 04:29:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd45d6d0-7a34-3048-b8a0-491f528ab29d | -19.89478 | -48.26938 | 2026-09-26 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa45e210-40bb-3cd4-bbf7-c2f7d7e7898b | -19.69625 | -49.48342 | 2026-09-26 04:29:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 099f8067-cd16-3a54-bfd8-e751ca158387 | -16.35129 | -47.6981 | 2026-09-26 04:29:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3238a8ea-6eb3-3ca8-9d55-84b853bd6637 | -17.03844 | -56.58475 | 2026-09-26 04:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| bd85fa2a-c8ed-3865-8557-42f9b44af821 | -20.09406 | -57.2102 | 2026-09-26 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24bad60e-b909-334b-b529-eca5bb9c084e | -20.42634 | -47.45949 | 2026-09-26 04:29:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb5edd8a-70f8-3c4a-99f0-e198b9443d46 | -17.55028 | -46.33238 | 2026-09-26 04:29:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c875873a-cb00-3cd2-a992-103247542c96 | -17.10509 | -46.47054 | 2026-09-26 04:29:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd608005-b289-305b-9262-efddd18c8073 | -16.75915 | -45.06171 | 2026-09-26 04:29:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8883874-5fa2-3441-8bab-c0eb71274a93 | -21.54203 | -50.24556 | 2026-09-26 04:29:00 | NOAA-20 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce0419c2-5e0d-3f4b-94ff-da8da5a6971c | -16.90251 | -42.12551 | 2026-09-26 04:29:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0b6c9481-6b84-3e05-a987-86acfedb62e4 | -20.34243 | -47.49434 | 2026-09-26 04:29:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 212b4b0d-5fc1-3e66-bfff-9e9e22c2a23c | -17.0374 | -56.58776 | 2026-09-26 04:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c2ceb7c0-8050-3aad-9eac-46bf3d1958cd | -21.10321 | -46.26705 | 2026-09-26 04:29:00 | NOAA-20 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 88fdf2a9-6ab5-3729-972c-30a18748c89b | -17.13126 | -50.29849 | 2026-09-26 04:29:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 873e9b8f-7564-3195-b658-951f94b27c23 | -19.00609 | -46.47561 | 2026-09-26 04:29:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44d10f7c-1b21-3033-9dad-9fb25a8cfc80 | -19.91095 | -48.25346 | 2026-09-26 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d705064-db96-3037-b152-279e110c383e | -21.49214 | -50.22881 | 2026-09-26 04:29:00 | NOAA-20 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4dc05642-588d-3269-89c5-702c82359cfd | -17.54972 | -46.33607 | 2026-09-26 04:29:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a11290b-47dc-379d-b555-5d6a03d6ff87 | -18.9137 | -46.8581 | 2026-09-26 04:29:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1791f58d-4a87-3931-a70b-fda1e5240e6b | -19.05804 | -46.8247 | 2026-09-26 04:29:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e69b2b80-4c9c-3753-a2f3-5d7d08336f7d | -16.56662 | -43.98326 | 2026-09-26 04:29:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 692baf7a-fbf1-33c3-bf46-2e0bd00e2c68 | -19.89537 | -48.26573 | 2026-09-26 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 861ec013-3587-3404-9296-2774b4919334 | -21.10839 | -45.65636 | 2026-09-26 04:29:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ce802e1d-eb99-3576-bbe3-010cb93b0141 | -16.59097 | -51.07804 | 2026-09-26 04:29:00 | NOAA-20 | AMORINÓPOLIS | GOIÁS | Brasil | 5200902 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae676091-b395-3316-bb27-342f27d875f6 | -19.90979 | -48.26078 | 2026-09-26 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc71b052-455f-3161-9b93-8989948e9c55 | -19.90706 | -48.25652 | 2026-09-26 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec776e83-a33a-36f9-a36f-aa72dbfc0a0c | -15.73242 | -50.79976 | 2026-09-26 04:29:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9dd258dd-25c6-34dd-9193-4716763a098a | -18.25993 | -45.61753 | 2026-09-26 04:29:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c779f836-2a69-3a0b-b849-5130b919e9c7 | -16.75834 | -47.25498 | 2026-09-26 04:29:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33741a0f-7266-3044-8c85-fa4bdbfc72e5 | -16.49079 | -45.98475 | 2026-09-26 04:29:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f73abac8-3ea4-346e-bb93-605772c1f1cd | -18.25936 | -45.62141 | 2026-09-26 04:29:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ca68179-94ae-3c0b-86cf-8049f484c3fc | -19.0547 | -46.82414 | 2026-09-26 04:29:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d584c801-c390-3c55-b0b3-d94a20b0405f | -18.81177 | -48.32787 | 2026-09-26 04:29:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12d2fe03-62fa-357d-906b-849ef8c412ff | -19.45991 | -45.65482 | 2026-09-26 04:29:00 | NOAA-20 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc9f3684-1aed-327f-9a27-65357da284a3 | -18.24906 | -45.59591 | 2026-09-26 04:29:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1535175c-eb8e-39b7-bff4-e9dfc68f06cd | -17.12907 | -50.29523 | 2026-09-26 04:29:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49f94e1b-07db-3af7-a89f-7e0224ea505a | -17.03805 | -56.5845 | 2026-09-26 04:29:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 99db7e8b-afb5-34a3-82d1-bc3f4e4116ab | -16.48744 | -45.9842 | 2026-09-26 04:29:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a58f738-3c9e-3460-9327-5074a72750fb | -21.19004 | -46.93459 | 2026-09-26 04:29:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0fa80542-c85c-3cce-aaf3-dc4eb8e6065d | -15.73611 | -50.80045 | 2026-09-26 04:29:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e008878b-8d29-3edf-a884-93c0f2f8a6a1 | -16.566 | -43.98756 | 2026-09-26 04:29:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5770391-8d04-38ce-a717-4eda8768c0a1 | -17.59219 | -46.56471 | 2026-09-26 04:29:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 305435d5-ccbf-374e-8362-f161b82451b1 | -18.25249 | -45.59645 | 2026-09-26 04:29:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ede9a735-c453-37d1-82ba-170d9b4d8cc7 | -16.57022 | -43.98385 | 2026-09-26 04:29:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 772aaa7c-f4dc-3246-b4e2-0a70008eae55 | -16.5701 | -53.0694 | 2026-09-26 04:29:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cea03e1-42ad-3ef8-bc75-e30488cb6369 | -15.73401 | -50.80169 | 2026-09-26 04:29:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3478d4ea-f883-3e53-9a2a-67339a539f79 | -17.03777 | -56.588 | 2026-09-26 04:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c449dc40-5ffd-3bd9-a371-7b0f156d6333 | -19.90316 | -48.25959 | 2026-09-26 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0f0b0d7f-9771-3629-83f3-74809a108f23 | -16.56301 | -43.98269 | 2026-09-26 04:29:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2867f146-e39b-3f72-bd42-5ab489235dc9 | -21.96085 | -55.94104 | 2026-09-26 04:32:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0f7ab8e-ab84-3bdb-bb92-81c56c5d9442 | -25.63605 | -51.42696 | 2026-09-26 04:32:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e28397fd-bb07-3096-8755-fb8dc8dce6c6 | -26.42068 | -52.35451 | 2026-09-26 04:32:00 | NOAA-20 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3544fa70-b3c4-3546-b42a-f4add5ad0bd4 | -22.02149 | -49.57904 | 2026-09-26 04:32:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3f3e6ab-bc8a-3e34-b1ef-651463ca34c9 | -21.96539 | -55.94008 | 2026-09-26 04:32:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc0fa4a2-da03-3d51-9f2f-f475648ccdac | -21.96537 | -55.94209 | 2026-09-26 04:32:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63fd523a-241f-38e4-ae7f-afa445b96ce0 | -28.06169 | -48.67221 | 2026-09-26 04:32:00 | NOAA-20 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d6dff4e1-f914-3e6d-ac74-8b64622fdbf7 | -22.02211 | -49.57527 | 2026-09-26 04:32:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cc126c88-9b0c-3bf0-8092-d5f7becb2bda | -21.96641 | -55.93707 | 2026-09-26 04:32:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b96483a3-4743-3802-81ea-71c2fb36c19e | -24.88714 | -51.64698 | 2026-09-26 04:32:00 | NOAA-20 | BOA VENTURA DE SÃO ROQUE | PARANÁ | Brasil | 4103040 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a9574828-fc54-314d-ae5e-e878238a78e6 | -23.00432 | -48.62058 | 2026-09-26 04:32:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8622bc9-360b-385b-8e37-1b80e42a560f | -27.01712 | -50.48751 | 2026-09-26 04:32:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| da6e1853-0355-379e-a1bc-039f16e4489d | -27.34061 | -50.73609 | 2026-09-26 04:32:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ed17fd69-e8de-36f5-86d3-b571f9c06b20 | -22.01878 | -49.57463 | 2026-09-26 04:32:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a2202620-e314-3871-a67e-a44ea3cb72bd | -30.88996 | -54.47062 | 2026-09-26 04:34:00 | NOAA-20 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 1f132022-4550-39d9-b3bd-2088070de348 | -29.12622 | -55.62254 | 2026-09-26 04:34:00 | NOAA-20 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 04fbe53a-732f-3744-9720-6cdbfd7fe8dc | 2.71516 | -60.68362 | 2026-09-26 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b26c652-5bb0-3872-acf7-483125d545f3 | 2.35699 | -50.77434 | 2026-09-26 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c9bed37-2d8e-379b-8822-f3a938cf555e | 2.04809 | -50.97737 | 2026-09-26 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eec59d2-04e2-3e88-9332-b1de7f300d1a | 1.29632 | -50.83278 | 2026-09-26 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00c2fec4-d90a-3ebc-a267-d9165143a23f | 1.1439 | -50.74452 | 2026-09-26 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 798c8a6d-01ac-384c-af5b-20139cd85ed6 | 3.97539 | -60.47382 | 2026-09-26 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b54f82b-4430-3024-8db1-30e4ffe8c5c9 | 2.36095 | -50.77371 | 2026-09-26 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37065012-f6d2-38a8-bf8e-6c9fb30286d6 | 2.04731 | -50.97236 | 2026-09-26 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1d9eb6a-47a2-32cd-a75f-68afdb1084d2 | 3.97867 | -60.4696 | 2026-09-26 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| adb24752-cbd2-3568-b6ee-9b5f964e93e3 | 2.23097 | -50.88797 | 2026-09-26 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 934ed3e8-74b1-393d-91dc-136bf7837283 | 2.62606 | -50.89381 | 2026-09-26 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b2a7ace1-a00f-3271-b199-1135a15dbb71 | 2.93598 | -61.26711 | 2026-09-26 05:08:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README21.md)
