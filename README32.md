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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ebd60ec-7ba3-3e1b-923e-05398cb2738e | -15.20591 | -42.36213 | 2024-10-29 03:49:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e2c4a889-5e41-3e2f-880c-2feac8de43c8 | -15.20514 | -42.36654 | 2024-10-29 03:49:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| be502a0a-daf4-397a-8925-a07bbbd4b8fb | -14.94984 | -43.34889 | 2024-10-29 03:49:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 057a9736-de56-32ef-b29f-da365d5a3568 | -14.94895 | -43.3539 | 2024-10-29 03:49:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aec08582-bd88-3044-bac3-e72883bc477f | -14.94596 | -43.34816 | 2024-10-29 03:49:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a12fa5f9-37ea-3462-b161-2177d4d246e1 | -14.84967 | -42.79299 | 2024-10-29 03:49:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a49d96af-b390-3572-9e48-99676d78b0ab | -14.47659 | -43.35617 | 2024-10-29 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a570ab8-f35e-3140-936b-0f83c1f1a0f6 | -14.47617 | -43.35955 | 2024-10-29 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c061592e-e3e7-33e1-b82c-8b745ff74848 | -14.47567 | -43.36127 | 2024-10-29 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1afd83ac-b26d-3719-b4c0-e4e7bb593ea6 | -16.42261 | -43.5097 | 2024-10-29 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a2b2dce-b608-3894-a06a-d605696addf1 | -16.04118 | -43.72178 | 2024-10-29 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edb26f8b-c83b-3692-90c6-8d41d81db5fb | -16.04045 | -43.72456 | 2024-10-29 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7ad3c26-5d3c-36aa-8610-b34479da90a4 | -16.04025 | -43.72688 | 2024-10-29 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb43236e-f032-3fc3-9928-9addbe1cc62f | -15.67966 | -43.22972 | 2024-10-29 03:49:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6231400f-ee1c-31d4-9d6a-53cf2ffeb80f | -15.44874 | -43.62768 | 2024-10-29 03:49:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8fd36c07-4c31-3957-97dc-1b8de4190796 | -15.44782 | -43.63282 | 2024-10-29 03:49:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 44e79dec-fa2a-3af0-a9c2-cca474ec4297 | -15.44483 | -43.62691 | 2024-10-29 03:49:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e24edc10-1c8f-3027-b0ad-1f9ac77870d4 | -7.88085 | -42.95633 | 2024-10-29 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a73f476-a72d-3bc4-887b-b0f19d33aa60 | -7.87661 | -42.95566 | 2024-10-29 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b7b5a130-fe77-3893-857c-b0d9dfc1db49 | -7.85509 | -43.13469 | 2024-10-29 03:49:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d8428145-b55a-36bc-a4a3-393a59b8efc0 | -7.80301 | -43.18071 | 2024-10-29 03:49:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 79ffdbde-07f4-371b-b6d5-5b42a7ced36d | -7.60605 | -43.66671 | 2024-10-29 03:49:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c55b25e-10a9-34ab-985c-9699c17bcec4 | -8.71433 | -44.01903 | 2024-10-29 03:49:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 051946e7-3b7a-3208-86a5-d9cc44a5f2ef | -8.36899 | -43.64539 | 2024-10-29 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc3f1189-5a2d-3d96-b9f4-c99da2b70b9c | -8.36822 | -43.64982 | 2024-10-29 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92c18166-3f5c-3921-a3a1-141411f9e4fa | -9.52811 | -43.01865 | 2024-10-29 03:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ffb9a699-d79b-3344-8652-75d5418544d1 | -9.52747 | -43.02245 | 2024-10-29 03:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14f4ddca-ee18-3e42-a8d6-22e3189771e9 | -9.52598 | -43.01748 | 2024-10-29 03:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02580759-ae66-3ccd-8d6b-f0ca688f825c | -9.5253 | -43.02128 | 2024-10-29 03:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb970971-82a7-32ef-b51f-7f54a913c8cb | -9.79734 | -43.88066 | 2024-10-29 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d95d5378-ecaa-320d-bf30-fe11961de3fe | -9.71851 | -43.91884 | 2024-10-29 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 33aa1f30-038a-3621-9e54-dff2f13e4878 | -13.73416 | -44.05587 | 2024-10-29 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f214278f-98bf-31ca-b8a0-4da12a04cd11 | -13.73006 | -44.05496 | 2024-10-29 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4818cd0e-907f-3eaa-b399-e6dd1a5d428e | -13.67155 | -44.06075 | 2024-10-29 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 386247d3-b9e2-3777-b8da-25d6eff6b620 | -14.87528 | -44.11465 | 2024-10-29 03:49:00 | NOAA-20 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa873142-e2e6-34ce-a00c-44d33fc67c4f | -14.87491 | -44.11457 | 2024-10-29 03:49:00 | NOAA-20 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a948499-ba68-3a76-adaf-7ed7a2a7e20e | -14.597 | -44.26466 | 2024-10-29 03:49:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccdac85f-485c-3ed6-8dfd-c2f0ecb40b2f | -14.5929 | -44.26374 | 2024-10-29 03:49:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf9974e5-4164-3a99-abb2-aed8c31ba73b | -14.59222 | -44.26749 | 2024-10-29 03:49:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8ddecfa-f0d7-3487-8db1-64543e8a69a5 | -14.19595 | -43.72536 | 2024-10-29 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3debf1ce-b1c6-3885-bd63-92ac85e87cb9 | -14.16442 | -44.65758 | 2024-10-29 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dea5464-382f-3505-85ea-5646c570bd58 | -14.16365 | -44.66178 | 2024-10-29 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 314c08ff-bb80-3da3-ac9e-e28f7c91ba4f | -14.14834 | -44.0793 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| d33475ec-784c-3486-8b59-90f49ce101cc | -14.14423 | -44.07851 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| fec3b59f-0972-3bdd-af1d-260897fd193f | -14.14354 | -44.0823 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 3d030085-89da-3409-b2c1-4eed32b27b29 | -14.14013 | -44.07771 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 89584178-07b2-3649-a6d6-58fb0ac86343 | -14.13944 | -44.08151 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ca6eabae-23b8-3280-980f-2de0ceae6811 | -14.13169 | -44.35972 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 481bb0fb-9aac-3865-8429-594892275f73 | -14.12821 | -44.35505 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b198807b-3a9b-3ede-8dec-e6c23d7fb1e3 | -14.1275 | -44.35897 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 456bdc29-72f6-3636-bd6e-5c588a8be0c4 | -14.11639 | -44.10144 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c13e3ed-964d-3997-9f6e-688e853b07ad | -14.11472 | -44.10033 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0ecbf18-027f-338c-a178-fd42848ffe9f | -14.08349 | -44.26941 | 2024-10-29 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f26a8de6-8a99-3590-8b07-dea135051a50 | -13.9923 | -44.01983 | 2024-10-29 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 143992fd-31e7-33b0-8698-fba5af7db032 | -13.88768 | -43.97318 | 2024-10-29 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d8ea1011-a748-3334-b479-009470b407fc | -13.88701 | -43.97694 | 2024-10-29 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d1c7cea5-c3af-3886-9a06-53a2b48e0d74 | -13.8604 | -43.98355 | 2024-10-29 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 284950bc-3cba-3877-ae2a-aff631d61bb5 | -13.85698 | -43.97899 | 2024-10-29 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1b8b909-d310-3981-85be-7ad23445588f | -13.8563 | -43.98277 | 2024-10-29 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d48b6bee-45f6-3819-abd4-2017aff5fc04 | -13.85562 | -43.98653 | 2024-10-29 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 381ec4ef-e311-30bb-b430-f33b612c81ad | -15.43436 | -44.17138 | 2024-10-29 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e9ac019-3082-3e2e-ae4f-1a45d11c5f2f | -7.61273 | -45.27276 | 2024-10-29 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 692b63c6-97b8-3cf1-848b-19253d87e121 | -7.61267 | -45.27171 | 2024-10-29 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53fd8c6e-855b-3bdd-afb7-70018da5395d | -7.41785 | -44.7996 | 2024-10-29 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d456b9f-72f6-37d4-b2df-add20785d09e | -7.413 | -44.79886 | 2024-10-29 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8086621-f1b6-3d2f-9639-1378849bce74 | -7.40718 | -44.80357 | 2024-10-29 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da9cff0b-a8a8-3f31-8f89-b2294c225edf | -9.18985 | -45.21457 | 2024-10-29 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 105b35e2-3026-3cb9-bcc4-a5a1c8d8a65c | -9.12317 | -44.4248 | 2024-10-29 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2430589-3fa7-3dc4-8631-ce4bf40284f9 | -9.11861 | -44.42387 | 2024-10-29 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6ac1968-0cde-3634-846f-fbf3a871c025 | -8.92119 | -44.58543 | 2024-10-29 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53bb52a6-0942-36e9-8027-551dbb71ad9f | -8.91995 | -44.58285 | 2024-10-29 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c1e70c5-8d6b-3265-8eb8-e30c10e62d40 | -8.91654 | -44.58465 | 2024-10-29 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd0623fb-f1ec-3a33-9531-20108b9caa48 | -8.76473 | -44.72419 | 2024-10-29 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0650fd8-f8c1-36c7-a685-7b7517a35840 | -8.75713 | -44.71227 | 2024-10-29 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5378ace6-bc4a-33ae-b8f4-94153cb5ede5 | -8.75623 | -44.71735 | 2024-10-29 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13fc13da-179a-34eb-a545-15ac9202c3fc | -8.75243 | -44.71138 | 2024-10-29 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6950d246-8ff8-3fe5-8dde-6481e90f73a8 | -8.75154 | -44.71648 | 2024-10-29 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73f40c72-92cd-3f80-a2dc-b407bcbd1014 | -13.62413 | -45.58075 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79f50f02-dd60-3e58-8aab-624ac36579fd | -13.62347 | -45.58269 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dba2ac9-4708-3763-8368-7f1a219dca35 | -13.61499 | -45.57899 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 230f59f4-69f9-3b92-8818-da500a543b52 | -13.6141 | -45.58381 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac32dea0-eb19-3083-a8a3-f46ef8648602 | -13.60954 | -45.5829 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c4c63b6e-bf0a-30ce-9910-0b8f9e7a198b | -13.60777 | -45.5925 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 24459734-8dda-3eb5-881e-9f380c4ae246 | -13.60688 | -45.59731 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6eb71de6-9d30-300f-a53c-1a75dd619b2f | -13.60497 | -45.58198 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c22bee49-6205-3f32-9a5e-8fb2f72da6c6 | -13.60409 | -45.58677 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ddbbbcc-3ac6-3d66-967c-49bbc0713eeb | -13.6032 | -45.59158 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 91e0b943-f3dd-388b-a5f3-d8f692c00b40 | -13.60231 | -45.59641 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e99e3d38-bba2-3038-939b-f5c7d9554b31 | -13.6004 | -45.58108 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f996a571-e402-3576-b89c-c275eb79f840 | -13.59951 | -45.58588 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1f995fab-aab4-3f08-ad93-63cca2d11c8f | -13.59773 | -45.59552 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ecf8da85-00f8-37b1-97f6-0469bd48b55c | -13.69647 | -46.128 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcb99ef6-b09f-3873-a9dd-70637e6544b7 | -13.69077 | -46.13216 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2168ff7-8c68-34af-8a98-86776b4a0c21 | -13.68981 | -46.13729 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca0109a5-3f9e-3aee-9827-6bebadafbbc2 | -13.68799 | -46.12094 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b6faca3-0992-3a36-a902-a5afa78a7fbe | -13.68606 | -46.1311 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28eddbd4-1639-3872-8197-daadaccdf27b | -13.6851 | -46.1362 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0199421-70d2-3604-b9c1-7204b17f2039 | -13.68414 | -46.1413 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9de80df-e924-3eec-8c46-475f578066dc | -13.68328 | -46.1199 | 2024-10-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b8ea400-3b84-370c-a5d0-3592f30f0ed7 | -14.16044 | -46.16011 | 2024-10-29 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README33.md)
