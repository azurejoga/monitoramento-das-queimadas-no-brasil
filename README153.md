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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92d79b80-dd36-3293-ba84-72f2475ee3bd | -11.68534 | -47.81084 | 2024-10-04 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65770f81-df35-31c3-bfab-dd1586775824 | -11.68468 | -47.81598 | 2024-10-04 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c6f8e65-fd84-39ad-8738-4e538f79bf4a | -11.67108 | -47.80902 | 2024-10-04 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1878ee23-a780-3543-9485-e3b8e110aafc | -11.32303 | -49.00157 | 2024-10-04 04:57:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8f11386-d117-3d25-9afb-9dfbcf65d122 | -11.25513 | -48.84084 | 2024-10-04 04:57:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8a9837d-0b6b-31f6-bd3e-508bb4fb0685 | -10.87196 | -48.39188 | 2024-10-04 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f492f988-e8a8-32b0-8b22-56c04761c256 | -11.31868 | -49.00096 | 2024-10-04 04:57:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c519bfe-c82e-3173-878b-c40fcd90f535 | -10.87256 | -48.38738 | 2024-10-04 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e8e2f0a0-0a6b-31a1-925b-f9482b6de770 | -13.50041 | -48.63669 | 2024-10-04 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95312b37-968a-3fc4-b65e-c07772ec4f83 | -13.23412 | -48.64203 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc838b49-69a8-3ca2-a8f1-3fac11c55586 | -13.21395 | -48.65366 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14fa1ea2-f3dd-3770-9c85-2de73766f1f9 | -13.20535 | -48.64806 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 041fb9b4-f0d1-390a-9282-341e68d58634 | -13.20478 | -48.65254 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29793613-f20d-3083-99ee-1610ed8f669b | -13.18733 | -48.67962 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e779d9ff-57c8-3fd6-bd79-da9fa001e937 | -13.18271 | -48.67939 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16efb873-8159-3397-80bd-e53a28aff256 | -13.1787 | -48.67437 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 03963de5-c349-3ae0-9310-94a8256246e2 | -13.17695 | -48.6881 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 198d3952-79e9-3e54-b7cc-04cb2ee6e193 | -13.17352 | -48.67853 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4c467cfc-9c5c-3230-9dc7-3d3d5b3b07cc | -13.16491 | -48.66958 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| adb7900e-c251-38bc-818d-359772894804 | -13.16427 | -48.67434 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5bc937d3-e899-3434-b46e-cab206ad7b2a | -13.16365 | -48.67895 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e3ffdca7-31aa-3906-952b-a953bdb30d83 | -13.16296 | -48.64933 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95d736ff-d73c-3aad-aee3-96900087cbf7 | -13.1617 | -48.66167 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed5e378e-5a00-37b4-bc22-32ceeeea54fc | -13.15713 | -48.66094 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3223b725-3447-378e-bfa0-86242ec9c054 | -13.14561 | -48.67868 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0e1eb065-ac5d-3dfb-950c-0ec6637feea2 | -13.14483 | -48.68066 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6c02e7e0-aa75-3228-ad3b-e12778b51854 | -13.21973 | -48.64504 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d8c7c9e-ed40-328d-a015-bd12e0cafb7d | -13.18795 | -48.67482 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f71c2c7e-a8d4-37e9-a5c1-e3311eabea66 | -13.17753 | -48.68356 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 94a399ba-a715-3e9e-9aa2-719a6e53f234 | -13.17498 | -48.63026 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a7fd6806-43a8-33f4-93f4-8bebfef0fe03 | -13.17043 | -48.62935 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3b4ef8f0-caa6-3650-9a49-6486c51be3bd | -13.16876 | -48.64081 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 738ebf28-5ae3-39ba-9623-60f2489f875f | -13.16866 | -48.6434 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8f9d877e-bef3-34cd-a94f-463404a19cd0 | -13.16815 | -48.64539 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5cd5c59b-d561-3e49-be03-e528e49aff9b | -13.16712 | -48.61859 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52548759-1c0d-3884-aa78-485492f865e4 | -13.16588 | -48.62844 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33382385-a89b-322c-8cb3-eb81e1e58ce3 | -13.16562 | -48.66745 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1a85235-9ddc-3d65-9871-803c3cc90266 | -13.16469 | -48.63791 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ddc1fd11-f381-39cc-8de9-00fc1d252d13 | -13.16441 | -48.67704 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e4a5792a-1e18-3387-a52f-1db879c63ca6 | -13.16193 | -48.62275 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ead7468a-a7ba-314c-81c4-71791e4f8b48 | -13.16132 | -48.62761 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec857658-1b0f-3004-871f-75568c4a9251 | -13.15648 | -48.663 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9bb8b56-8a04-3823-a588-174247dcad6e | -13.15592 | -48.6706 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 346e4ee8-e347-3b45-a316-6c4ee99ab895 | -13.15584 | -48.66782 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2f49b4d3-3e91-304d-ad3f-59b0ef57d8ac | -13.15519 | -48.67265 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 72a60ced-e0c2-327e-888f-3d2578aa7f95 | -13.15394 | -48.68208 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 037ac9d9-d93a-3342-9102-530dc16f2ab7 | -13.15016 | -48.67945 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5cc9d73f-419a-3faf-b9eb-e3fc45fdfff9 | -13.15 | -48.67672 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f52bcd6d-364e-389e-bf72-10132f4b00f9 | -13.14028 | -48.67993 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0d03732a-02ad-3fae-b456-5751bfef6737 | -12.48682 | -48.02226 | 2024-10-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ded396f2-5343-3262-b6ce-7725a5a0a48e | -12.26243 | -49.21691 | 2024-10-04 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db456b8f-a564-3ddb-8599-532cf92ced84 | -13.32792 | -49.32322 | 2024-10-04 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 173ef0ed-3913-30b4-ba35-b4bd9543e104 | -13.30775 | -49.30666 | 2024-10-04 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c84e118-8fff-3823-ba7c-08b7b3197b18 | -13.30709 | -49.31183 | 2024-10-04 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8420527-76e1-3bfb-93b2-696f397180dd | -13.22891 | -48.64621 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4632e5c7-8ba1-34bd-9422-9e8de57217cd | -13.20796 | -48.51803 | 2024-10-04 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19fe9032-71cc-3027-bf0b-a0f4b68d2860 | -13.19255 | -48.67519 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c37fd31-969f-33f1-acf1-5b5de082f0aa | -13.18212 | -48.684 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91247e71-e5fc-3721-b621-d53acbeca5cf | -13.17239 | -48.68746 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 189cd2e4-5feb-39b1-b462-1a8194a1cfb5 | -13.17001 | -48.63146 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 452c75f0-4dfb-3fc9-acb1-4ca08cea36a0 | -13.16983 | -48.63415 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2aa49fff-b023-3cba-a41c-deb7ea5be91e | -13.16559 | -48.66448 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 68cdc2b5-50f2-3814-8e0c-2e7074ab8e0f | -13.16547 | -48.63054 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1830061d-2409-367f-9323-db25b6eb6420 | -13.16528 | -48.63321 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40395b03-8d36-31bd-a044-404ae22b65fd | -13.16422 | -48.63994 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f06920af-11cb-3ab1-b7a4-5c37dda04ee3 | -13.1641 | -48.64258 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfa9fe5f-a32c-3d6b-8bee-df8bfebc17a5 | -13.16156 | -48.6249 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbc05325-4dfc-31e1-a61b-db995a72189b | -13.16091 | -48.62975 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a93167cf-8e00-3b28-bc5c-0f138de8a0b6 | -13.16046 | -48.6715 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b2cf70c5-dbf0-359f-8f71-e956059bdfce | -13.15653 | -48.66577 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46b66d69-3e11-371c-8628-9b83eba4b148 | -13.15472 | -48.68018 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8cb0aba1-261a-376f-8dd3-ce2a03fa9031 | -13.14938 | -48.68138 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d7fa63e7-93c6-3feb-8790-9db59d9aa641 | -13.14503 | -48.68328 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2c73c25f-2125-334e-a68b-ffaf91d169ea | -13.49982 | -48.64129 | 2024-10-04 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 03e6265c-8018-338d-9d64-92f655a417a1 | -13.21914 | -48.64963 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7af79fd4-b85a-3eb1-a3bb-41ee3f3d04b2 | -13.20201 | -48.52789 | 2024-10-04 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb69989d-a702-3b97-9b4a-b94feca5f26c | -13.18332 | -48.67461 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec2408f4-3c8c-3233-a93d-25a31c3cc578 | -13.18153 | -48.68868 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 80195883-c578-3d5b-a7ab-242106dd59ab | -13.18018 | -48.62603 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf99d677-6b4e-36a7-b15f-b82e078ea393 | -13.17954 | -48.63111 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b9a04cb-8d9f-3675-ab1c-15b3f806825a | -13.17067 | -48.62656 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30bac15a-d36e-3792-8da3-73064c8d7125 | -13.16938 | -48.63621 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 995cf46f-0e6c-37d7-9aa4-ba52a98ccb08 | -13.16924 | -48.63883 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91617fcd-624f-3adf-b7a7-90a5f1734cbe | -13.16896 | -48.67787 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c044976c-2a42-3129-adfa-defbf34604e6 | -13.16743 | -48.61589 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff450e20-ff32-3a05-a470-1204fcdb1830 | -13.16627 | -48.66234 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd606bf8-f95e-36b3-b676-3818961388f2 | -13.165 | -48.67239 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 36535f5f-312b-3669-815d-c4eb2f19f8d6 | -13.16484 | -48.63526 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78524073-0db0-3d03-812e-9816dfdd1a2c | -13.16351 | -48.64728 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a3cff29-1750-33db-a0da-b0ad4aacac2d | -13.16168 | -48.6589 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ecb9198-f895-379d-ba5a-b76c9d7da706 | -13.15986 | -48.67625 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 60ceac07-2e85-34fa-b3b4-8c9790a38343 | -13.15973 | -48.6735 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 65d56ae1-98b9-39fb-a262-2cb3779610c8 | -13.1591 | -48.67822 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 11506986-a1e3-3da0-b70e-95cb74243c39 | -13.15531 | -48.67545 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0fafd843-8da6-3a7c-b8f6-3e467ae386b0 | -13.15455 | -48.67749 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 14fb9f00-d62b-3074-b4ba-635b6529da25 | -13.14959 | -48.68397 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d4e6f59b-cff7-33a3-a46c-28349dfbd6bb | -14.53558 | -49.2947 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c41bc1a-8e79-305a-9dbb-d671122874a5 | -14.53499 | -49.29926 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf2f685b-65c3-31c8-9016-9d9bb83b6d3d | -14.53168 | -49.28969 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42bc4c4d-6038-3471-aa6d-4ca4062b3863 | -14.52779 | -49.2846 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README154.md)
