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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e81f491-9f29-38ea-9b41-0e475a8b3733 | -12.29382 | -47.64937 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8a91713-1c36-3aa8-a964-32aa0a4db22b | -12.2928 | -47.65495 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d108214e-4c45-374e-838b-1de87a0f75bd | -12.29126 | -47.64951 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11b534aa-1c3e-3d19-8f9b-e2fe37c5ec3d | -12.2902 | -47.65503 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0096e218-0b47-3984-8602-326ae9ad64da | -12.28895 | -47.64838 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0ffe34d9-d0ba-3243-9782-dfa9d78595a6 | -12.28794 | -47.6539 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 45255dc1-f56d-3abc-b08b-b1c0d3221711 | -12.28692 | -47.65944 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1911ddf5-3eac-32cc-8834-ab3c2d2f442f | -12.2864 | -47.64852 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 61f10ad0-86db-3f4a-bb4a-1d5b607a14fe | -12.28534 | -47.654 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0b215211-e3e8-3651-b42d-bba813688323 | -12.28428 | -47.65957 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1121c17e-c90e-3914-94dd-c5aaeb95cc6d | -12.28409 | -47.64738 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3ce59085-0127-3755-baf7-c2149e3e4874 | -12.28308 | -47.65284 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e9df880b-b9ec-3d31-a3bb-ad8ff161288c | -12.28153 | -47.64751 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c16be7c9-c241-3dd2-92fb-bd7010c5d2e7 | -12.28049 | -47.65296 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fe8c183b-16c6-3744-b7cb-ad052c0d4cf9 | -12.27923 | -47.64635 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 673fc13b-49b8-31bc-99fe-862918a82de2 | -12.27822 | -47.65182 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 820a7be3-aab8-3ec4-b260-40ebf4912f07 | -10.74216 | -47.97458 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f100c15-bbba-3f52-9d80-52ee94a72eb2 | -10.74193 | -47.70316 | 2024-10-02 03:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10e24604-390c-363f-8c67-7490574986cb | -10.74164 | -47.97734 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b273092f-c614-334a-8cbf-81b839170808 | -10.73747 | -47.69909 | 2024-10-02 03:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9c5e16b-5816-374d-8615-9d92787dfa84 | -10.73713 | -47.97314 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2865243-6b68-3df3-94ba-1c51808afaf0 | -10.70068 | -48.36764 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d248cca7-41c6-3858-9dbf-025e65bec5bb | -10.59088 | -48.06038 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bde9da80-a764-3c0c-893c-da439177f580 | -10.5902 | -48.06396 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f185ff35-9fd7-394a-9e01-c363103882de | -10.58955 | -48.06739 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 93de38db-4535-3d37-8b5a-88ffbc0a05fc | -10.58949 | -48.06139 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6db21440-4e66-30b4-8f45-610afc8ca2d4 | -10.58886 | -48.06485 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4bbf417d-fa35-3583-9fa5-721f34d64bd2 | -10.58825 | -48.06818 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9da26777-c9bb-3718-8d94-7030d3945940 | -10.58764 | -48.07156 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 779d0e5f-e753-3d80-ba6e-0823aa160c45 | -10.58567 | -48.05965 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd91c67c-e961-3731-88ce-eb93d2396b46 | -10.58499 | -48.06323 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16d16667-3a08-363d-9704-6126a388068c | -10.58438 | -48.06639 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4dabb38f-f3cc-3539-b849-6c3f49ecfce6 | -10.58422 | -48.06098 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a1700b8-b2b0-3e4e-aade-bfca324d1e3f | -10.5838 | -48.06944 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 37dc30e3-ef77-3e04-92ec-cdac785ce1f9 | -10.5836 | -48.06435 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36ac09ba-1dee-381b-91f4-e2f567102999 | -10.58306 | -48.06735 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 69a6cc4e-d75b-3b36-9908-ea583fbb6d27 | -10.5825 | -48.07038 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3814f470-6c3d-3d87-b1b5-6fc71b89fd83 | -10.56915 | -48.02668 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1a7cf12c-6231-3b35-b69d-f0519a0bf1bf | -10.56856 | -48.02985 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fdfb1801-2754-3796-97ec-f8e040fb096b | -10.56792 | -48.03334 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94f7d8cb-689d-37df-9f09-0e23c4aeb2f2 | -10.56336 | -48.02914 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 432a32cb-39ff-3708-a771-d3da650ece62 | -10.56267 | -48.03286 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5940e23-a2ab-3d29-a260-5d1a153308b7 | -10.55804 | -48.02906 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| becb9f68-10ef-3321-b0ed-d6bd8440c31f | -10.55739 | -48.03258 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88b87b95-4f66-30d9-949a-3100766a8e35 | -10.55211 | -48.03227 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64b5bf97-86ff-33ed-a757-9dc35a0c7793 | -10.5515 | -48.03556 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d90e008-2af3-377e-bd04-dceb98a47411 | -10.55086 | -48.03901 | 2024-10-02 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98f18a8f-3086-36d5-861c-a94c3b5be740 | -10.46214 | -48.19594 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6eba63c4-0fa6-3489-8aa9-338c6cba5bf2 | -10.46201 | -48.19742 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d5af680-5ebd-3c29-9a54-e04e9461b188 | -10.46149 | -48.19956 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49c9ca45-7622-328c-9d0a-0cacd0ed4302 | -10.45934 | -48.24113 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae7d3adb-b95d-3923-b97a-38f797aa9dde | -10.45889 | -48.24236 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e46d9f8e-df1a-3e62-beae-c0a1367178ef | -10.45722 | -48.19326 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53e73dc9-4c4e-3cdd-946d-df3c2796ce83 | -10.45712 | -48.19465 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28526139-c2fe-314c-95c1-03302bba36fe | -10.4566 | -48.19666 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b07f4e9-4c0a-34dc-8b1b-df7fac3be4a8 | -10.45367 | -48.24128 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef7e7627-4ebe-3bd2-92f8-c8d56044ace0 | -10.4535 | -48.24343 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2694e13-f530-3813-bbf4-17e41558c932 | -10.45211 | -48.19258 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acd1611f-6605-3db4-8da4-f9f08e3636d0 | -10.43544 | -48.16478 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c632f4ba-27ba-39a2-a059-9d4651ddbe46 | -10.43013 | -48.16432 | 2024-10-02 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74f1e36b-1bf4-3fc8-8682-50335757749d | -10.22307 | -47.68592 | 2024-10-02 03:53:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f63cef54-dfbf-329c-9301-8dc85b2ffbeb | -10.2225 | -47.68894 | 2024-10-02 03:53:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27ecf228-ad4c-3373-942f-ad2d3fe49641 | -10.00704 | -48.85048 | 2024-10-02 03:53:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc3268e7-bf44-35fa-8f1c-17649a321d0d | -10.00677 | -48.8531 | 2024-10-02 03:53:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6ded5188-c48f-3a15-bb54-b1b7a59915e4 | -10.00635 | -48.85408 | 2024-10-02 03:53:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 837e73a8-fd72-3fb4-89ed-fe3115e14128 | -9.59291 | -50.19572 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1af6ce63-7392-3a26-92fe-4a66314b8e1a | -9.59204 | -50.20028 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db6e5280-751c-39bc-9085-a5bc9a8ee5a3 | -9.5869 | -50.1945 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b44fea83-7fb5-3b67-8032-052f85b25dd7 | -9.58602 | -50.19907 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bbf9d0b-ce8f-3473-bbe1-f8bc79200f1e | -9.58089 | -50.19328 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab923610-db77-3dae-9454-f17878578bc7 | -9.56958 | -50.21953 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6132d40b-d15f-354f-be6c-c9f1d987469c | -9.5687 | -50.2241 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cda82b3-6f88-3ff2-914b-97ae4c610471 | -9.56461 | -50.18057 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| fcf38302-2252-3002-be1f-7f7aa00ee069 | -9.56372 | -50.18512 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| df331432-ab6b-3c74-a13f-3ead6301b839 | -9.56276 | -50.18304 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 13b0d879-3e35-3475-8b2d-359b3081c8a7 | -10.5088 | -49.79089 | 2024-10-02 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c79677b-5920-345c-aca6-3579e8221737 | -10.508 | -49.79503 | 2024-10-02 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1fed8f9-a3d3-3dd9-a947-f0fee7127a33 | -12.15452 | -50.06118 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bedfe7bb-4834-377a-8684-07281ec3b6d9 | -12.15399 | -50.05842 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 36ba57e9-060e-36d9-a306-6dd11b5cbb49 | -12.1537 | -50.06523 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64913429-7834-394d-a61a-976f2f73133b | -12.15321 | -50.06245 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2310b2ec-39a9-37b8-93be-d6e586856dfd | -12.15243 | -50.06651 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e1ffa3d3-4fe8-3c84-bfae-197d20b9ae1c | -12.14962 | -50.05596 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d1b30718-33da-3322-8797-2cff6cc98c83 | -12.14907 | -50.05317 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8c56616-b958-3d7b-95ec-c2a3977d9f19 | -12.14881 | -50.06001 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 899bc471-f1ec-37f5-a62d-ec9ccb69ae22 | -12.14829 | -50.05721 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 106ea66c-5dce-398f-a1b5-71842e31a2ec | -12.14799 | -50.06406 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 291195f2-51a5-34fa-a9df-21047ed8bff2 | -12.14751 | -50.06126 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 623bcb28-f625-3d96-b106-7e8fe1aee793 | -12.14474 | -50.05072 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1d4c342a-db08-3d9c-a888-31a228c48d5f | -12.14337 | -50.05196 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d60b060-9573-3dd7-a47b-d042ea85a9be | -12.13846 | -50.0467 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95e1484c-9227-3238-bbe6-6375ba391bcc | -12.13768 | -50.05075 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c511de6-2052-3e1c-af76-f650b4524cdb | -12.13276 | -50.04551 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 797a68c6-3de7-3aff-b109-ced2a15be8ff | -12.12706 | -50.04432 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ddd36f7-bbda-33e0-b278-ee897993678d | -12.12627 | -50.04836 | 2024-10-02 03:53:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee7293d3-6bde-39c5-8e5f-1a52db2aca90 | -11.15128 | -49.72763 | 2024-10-02 03:53:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1472247-888f-3e92-9217-3bb771a7d1dc | -11.1496 | -49.72871 | 2024-10-02 03:53:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9c0a999-369c-3712-8ecd-ab6aaf759938 | -11.10698 | -49.61266 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3742fd41-87bd-3a97-b674-7f355028f504 | -11.10209 | -49.60756 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 773b2010-f896-31b1-a0f7-2c6bbcdda55f | -11.10133 | -49.61149 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README65.md)
