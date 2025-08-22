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
| 8156de2c-5f62-3966-9ea6-9b6593cb91f4 | -14.90613 | -47.98258 | 2025-08-22 11:57:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 05058dc2-a9f2-3c43-b4c9-0cfc71ff8377 | -12.13437 | -42.74134 | 2025-08-22 11:57:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 20.7 |
| c9dc2320-9162-3d14-a9b6-a8b9467b8d95 | -14.73271 | -41.67212 | 2025-08-22 11:57:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 8492abb5-133a-3629-9f45-106721b7317b | -13.39762 | -46.23077 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| fa744b95-2a0a-3904-8607-0b0d60049dfd | -15.5846 | -43.80328 | 2025-08-22 11:57:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b459922e-d5bb-3ed4-9a77-d446f708f970 | -11.31599 | -44.9502 | 2025-08-22 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6cf979cf-ccd3-3c04-9ee8-1b98ddd0a300 | -12.67784 | -44.9645 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| f11cd2b0-4922-3747-a2e3-0c211b296067 | -14.70815 | -45.11054 | 2025-08-22 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bb6fe0cc-fc0b-3cab-bcf3-f3668cf329da | -12.59573 | -42.23666 | 2025-08-22 11:57:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f59f6d9b-86f1-3736-9d64-6826a4e0ee97 | -13.94229 | -41.97903 | 2025-08-22 11:57:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| cb56200e-318b-3b45-bd16-f2feaab0833c | -14.09194 | -43.90755 | 2025-08-22 11:57:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 44ec6eae-7b0a-324c-8469-5b6ceb20346d | -18.28016 | -45.55578 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 42d8e0d0-832f-3533-b3fd-4912d0b3d87d | -13.93182 | -43.86999 | 2025-08-22 11:57:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 446f29d7-8df7-384f-a8d6-f7ceedd778da | -13.1766 | -43.79348 | 2025-08-22 11:57:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c16da940-e570-3b52-a75f-8420cc1617c8 | -13.45704 | -47.06151 | 2025-08-22 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5f9a6449-5b04-37bc-8c33-2190a5d3b138 | -14.8326 | -47.9445 | 2025-08-22 11:57:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 93583143-5b13-32e9-a8b7-f96c8a4a1098 | -10.73917 | -48.24928 | 2025-08-22 11:57:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| b1eeb13b-3eb5-3574-8d9f-5d239d8dbe3b | -13.40526 | -46.22482 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e3e923b4-0b20-3c8c-921c-9c727a2bb4b4 | -13.15047 | -42.54898 | 2025-08-22 11:57:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 34.9 |
| e1606bca-b579-3870-8f19-35575f5fb8d5 | -12.65136 | -45.33123 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 1f513f09-5066-39d1-afdb-7c7b8d8fc9cd | -11.87944 | -42.90383 | 2025-08-22 11:57:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 0d5c2b11-3838-3b0b-b522-1456338a5b8d | -12.94117 | -46.17353 | 2025-08-22 11:57:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5d93c311-d382-3885-ae7c-bb5d12d2de5f | -14.52174 | -47.85529 | 2025-08-22 11:57:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| be2a928f-bcd8-3a04-bbf7-58611145ee22 | -15.15684 | -47.9529 | 2025-08-22 11:57:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e3988d5b-af49-3bbb-ba61-25c6dbeebd6d | -13.04484 | -46.33202 | 2025-08-22 11:57:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2a91ecc8-90d2-33bb-8a26-b0810ff9e01e | -14.8973 | -47.96237 | 2025-08-22 11:57:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 69133afc-9264-39e0-9c79-67bd90c07dbe | -11.81378 | -44.25381 | 2025-08-22 11:57:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 44683da5-2203-3d93-ab61-32e8c9381b49 | -12.98723 | -45.21928 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 273.1 |
| 00645774-49fc-3b4d-a6c6-702624e9bdb5 | -15.57672 | -43.54889 | 2025-08-22 11:57:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| bb9f3a01-4e88-36da-8f41-ad12e3e1e5e9 | -11.87679 | -44.38049 | 2025-08-22 11:57:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7adbfc3e-b8cc-33da-98d6-166b25cb411a | -15.62454 | -46.1781 | 2025-08-22 11:57:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5122e5ac-2805-37e1-a403-3561696123ee | -14.69395 | -45.07433 | 2025-08-22 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2170970e-619e-367a-a6fb-76fadf052bca | -12.96025 | -46.28354 | 2025-08-22 11:57:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 1102d034-ea2d-3d3e-8871-69c4bdc0e7ab | -18.79594 | -40.14672 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 0c1f47a7-2c45-337a-8d7e-4482c01d202e | -13.0055 | -45.23439 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2cb3e9d0-1f02-32dd-9bd4-b687e7e6443f | -12.99728 | -45.22089 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 8e4a2c85-3d83-3244-bc78-66865967842f | -13.45959 | -47.04552 | 2025-08-22 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6a5c23ff-7c72-3a7a-9a21-1279c6ace670 | -12.31668 | -49.9887 | 2025-08-22 11:57:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 82e894c1-f48a-3c81-b4d6-ebb8c1b25bed | -10.8622 | -50.83505 | 2025-08-22 11:57:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 1e23d027-82c5-3eee-876e-6af357b24fc8 | -11.31787 | -44.93825 | 2025-08-22 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 66279645-d0b0-322b-aa83-fea64de3f2a0 | -13.39531 | -46.24479 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9701aa56-ec0b-368d-a331-400fcac329ab | -14.14449 | -41.85501 | 2025-08-22 11:57:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 72e3b739-c11a-32f5-a1aa-0e645f24ac2e | -14.15682 | -42.40875 | 2025-08-22 11:57:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 840c18fb-b982-3fb4-b5b4-4c89da6b7d2e | -12.96249 | -46.26971 | 2025-08-22 11:57:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 845880d7-ab9b-3b76-81ba-5532229898dd | -13.30078 | -43.1515 | 2025-08-22 11:57:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| cb9edf91-c77e-3ea7-ac96-ea4dea5ce475 | -13.74725 | -44.69592 | 2025-08-22 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| d0bbb16e-06f3-3cc8-9e63-383037443276 | -13.50294 | -47.05918 | 2025-08-22 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 4fd8368a-9dc9-3dd5-b519-c46f23651adf | -14.77376 | -45.40705 | 2025-08-22 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| dd2df14e-472d-3a54-b5ad-15053929b56a | -14.83562 | -47.92654 | 2025-08-22 11:57:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 362a842e-ae4d-39ec-81d5-309f1ed89d38 | -12.67769 | -44.9707 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| e5ebc704-bb45-3308-bc5c-85416c6f2de2 | -12.67607 | -44.97614 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| f8962f42-234b-3970-97af-592fd9e25173 | -17.36299 | -42.17166 | 2025-08-22 11:57:00 | TERRA_M-M | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6de31245-9c54-3311-946c-b3940d9292c6 | -13.13556 | -46.90575 | 2025-08-22 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9e3acfdd-5329-3ecc-8623-0a237ae92609 | -12.99911 | -45.20902 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| b4433df8-6dba-3df8-8017-ed9159591cfd | -12.98907 | -45.2074 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 281f8202-a617-30b4-9f78-7ac793f1d646 | -12.31229 | -50.00929 | 2025-08-22 11:57:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| d137f941-604c-3e31-b954-5436c2e5fd49 | -13.45735 | -47.05139 | 2025-08-22 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 051421a8-6258-35ba-9e63-2b0929f889f0 | -13.00616 | -45.22845 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| b4f941bc-7fde-3c7c-879f-eaa516a173e5 | -12.75597 | -39.51797 | 2025-08-22 11:57:00 | TERRA_M-M | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| dbc31943-ab9c-3c9b-a470-cd5b58f147fc | -15.1355 | -48.11783 | 2025-08-22 11:57:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 65c7dead-1cb9-3b0e-ba11-d74323be50ea | -13.00732 | -45.22251 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d5748094-711c-3345-a0d3-0126e9bad6f2 | -14.76154 | -45.22979 | 2025-08-22 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 154aab64-627f-3e57-97f8-feff3c7dcfd9 | -13.04251 | -46.34635 | 2025-08-22 11:57:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0c039d7b-fa4f-34dc-a8cc-bce56493218b | -14.77559 | -45.39546 | 2025-08-22 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5547644b-ef9f-3a43-9cb8-9b393973f62e | -18.36523 | -47.06312 | 2025-08-22 11:57:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 27a5c632-404a-38a1-a269-5cca203dc93c | -14.75888 | -45.23439 | 2025-08-22 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 42a304e6-89cd-38cc-92ef-508e584992a4 | -12.95804 | -46.29714 | 2025-08-22 11:57:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 9939a88f-d1a5-3dbc-a576-1de4a57f62c9 | -11.79879 | -44.94736 | 2025-08-22 11:57:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b93b1d6a-5f7d-3472-b9a6-21af1c38c9ed | -14.75975 | -45.24101 | 2025-08-22 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 56d862b8-51b5-3143-8a6e-3d535c291e01 | -14.09343 | -43.89768 | 2025-08-22 11:57:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 75977751-75fa-3ada-8ec6-41acba9506fb | -10.86831 | -50.80116 | 2025-08-22 11:57:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| d959f911-f497-3a06-bafa-9175c7be6d9f | -14.14578 | -41.84595 | 2025-08-22 11:57:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 8d66c8fc-beef-3cc9-9b11-cd1b9f1127c6 | -13.14912 | -42.5581 | 2025-08-22 11:57:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a3f77f61-8ad3-3780-b44d-8d7ca6c9d241 | -13.15211 | -40.66432 | 2025-08-22 11:57:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 16.8 |
| e141835d-6d39-3836-ae44-28073be91b59 | -10.87096 | -50.82909 | 2025-08-22 11:57:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 5a08cee1-ebd9-3b85-8c89-48f710a59376 | -14.70368 | -45.07578 | 2025-08-22 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| f9d44e43-9610-3e1a-ad14-878146a70ef8 | -12.96475 | -46.25579 | 2025-08-22 11:57:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d3bff944-a437-3e37-8793-0a2e3040b1a7 | -12.6533 | -45.31899 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e60aa640-3fd4-3488-8ee1-a59d7039ac95 | -12.9524 | -46.2876 | 2025-08-22 12:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b6ef7899-a8cd-34b9-b96c-b273e788ce20 | -12.2938 | -50.0121 | 2025-08-22 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3524694d-ded5-37b4-997f-801ba192b4d4 | -12.9925 | -45.202 | 2025-08-22 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| f649b851-0159-3ebd-97d3-db2e285d0f3f | -14.5063 | -48.8307 | 2025-08-22 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 298.7 |
| d311148a-192c-302d-905d-1d5293ef04fb | -12.9921 | -45.2252 | 2025-08-22 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 7aa046eb-d7b0-3c87-b184-c08aa39bd72f | -12.3129 | -50.0097 | 2025-08-22 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 52e91a32-6999-3fcd-a8ce-879e2a23b751 | -20.12463 | -41.55645 | 2025-08-22 12:00:00 | TERRA_M-T | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 69a26297-2b5f-3e24-9ba0-b56b65f03466 | -21.90115 | -47.24599 | 2025-08-22 12:00:00 | TERRA_M-T | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 579eb663-330d-3d92-9fe3-f0645cc9a94a | -21.3891 | -45.45437 | 2025-08-22 12:00:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| 77c2bc3b-8c57-381b-ba94-76b4e0c0b755 | -22.69501 | -43.74529 | 2025-08-22 12:00:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| b83b4b49-c1bf-38dd-a029-de03a97417d2 | -19.32383 | -45.07278 | 2025-08-22 12:00:00 | TERRA_M-T | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| fff0d1c4-e9c7-39d3-8825-9268ed148b6b | -20.87729 | -41.90777 | 2025-08-22 12:00:00 | TERRA_M-T | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| b61fbf18-45aa-358d-80ff-0385eadf9082 | -23.477 | -46.22005 | 2025-08-22 12:00:00 | TERRA_M-T | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 5fba0506-989c-383f-8067-27b099b84105 | -20.45832 | -41.67123 | 2025-08-22 12:00:00 | TERRA_M-T | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 96c294e9-f1c0-3d34-bae1-2cfdbc576df7 | -20.29557 | -46.63657 | 2025-08-22 12:00:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 31.9 |
| e37a9cb7-d3b5-383c-a200-8fa6bce8130e | -20.75207 | -41.8873 | 2025-08-22 12:00:00 | TERRA_M-T | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 03c6a3ef-550c-3e60-a365-20d0b94a6776 | -21.96203 | -44.97115 | 2025-08-22 12:00:00 | TERRA_M-T | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| b68815b6-8307-38a2-8746-799469aed968 | -20.75345 | -41.8771 | 2025-08-22 12:00:00 | TERRA_M-T | DORES DO RIO PRETO | ESPÍRITO SANTO | Brasil | 3202009 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 245a9d1e-75ad-3b52-9174-6fe806765c13 | -21.38752 | -45.46449 | 2025-08-22 12:00:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| da187d79-9845-3942-bcd2-15d30d83511c | -20.45698 | -41.6814 | 2025-08-22 12:00:00 | TERRA_M-T | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| cd902442-7b0c-3849-bc37-9d9bbc6f4e7e | -18.97469 | -46.60936 | 2025-08-22 12:00:00 | TERRA_M-T | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d72454fa-3743-3950-898c-5506c17ed93d | -23.30443 | -47.46241 | 2025-08-22 12:00:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |


[Clique aqui para ver as próximas entradas](README66.md)
