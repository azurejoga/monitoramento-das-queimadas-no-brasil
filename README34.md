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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31fb83f7-79a7-37fb-8027-f3d2c61e2351 | -2.63249 | -54.28262 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8e80210c-0e9c-3c03-ac3f-e335b3b097fc | -1.20715 | -53.69365 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6178d3a7-84ba-3862-a7ec-26951565e592 | -1.61882 | -52.62402 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ebea735-111e-3868-8dd2-6d021cb70d58 | -2.79463 | -54.07123 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa19f694-1df4-3414-9e75-8b71d09b158c | -1.7663 | -50.74733 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2e5d6cc-5183-3078-8b21-2def8e3c370b | -2.85435 | -54.01163 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc72cd91-94e8-379a-94a7-cec26410884f | -2.58698 | -51.72248 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d2781297-1e65-3900-a977-dced0b2bab3d | -2.18295 | -50.3326 | 2024-11-18 05:03:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ca109d7-ab45-391a-91ed-9426280ed843 | -1.63654 | -52.66957 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e1f1a4b-4f1d-3378-a23d-53359dc30e68 | -1.20455 | -51.76931 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46f1ab1c-54c7-31fd-bb50-9f3bad474fbc | -3.1927 | -45.4458 | 2024-11-18 05:03:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 759bc942-72cb-33b7-aa5d-326751e1b6c6 | -3.09033 | -54.55325 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02a7ae7f-35dc-35f8-8ca8-ec7813547aaa | -3.69157 | -50.11384 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cf1fbea-966a-386e-b55a-b92c58fa313c | -1.42296 | -52.82237 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fb0abba-9909-32ca-883a-5d806d6e8858 | -1.47515 | -51.15675 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b670f14-32e5-3650-a3a8-2c916774dcef | -1.13855 | -51.68412 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02ea117e-5e99-31f2-bc1e-8b99553924a8 | -1.64816 | -52.77178 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1dd501e-6564-3c83-8ff7-cc086f0c32e5 | -2.8332 | -46.6577 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f4cb510-1f04-37e7-86b9-ac358bd57556 | -3.16994 | -46.59716 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 100128d8-26fa-3d71-8127-ef233743d4d0 | -2.33105 | -53.57401 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05469ae7-4782-3dba-944e-f331adadeb5b | -2.865 | -51.79056 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 363ad98a-7fca-3de9-81fa-61ad9a85293c | -2.55852 | -53.99147 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b85504f-6ec7-36d5-9409-4e02feaf1869 | -3.67272 | -50.09946 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dca374d-3e7e-3efc-aa47-17538c645b7e | -1.39832 | -51.99184 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9b06799-3b84-3e07-b13f-8ad0ffa5960c | -3.10475 | -53.10718 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7accc13-b95e-37ef-aaf7-380940617634 | -2.91707 | -54.11517 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16beeb44-42f2-3b96-9b35-aa470458b24c | -3.10188 | -53.1029 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 61847645-622c-3cef-8f85-db1ce0a362a3 | -3.22922 | -53.61836 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d744c0ff-9a5f-35ea-b105-a8a0e6a8fbb5 | -1.1343 | -51.68771 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81081286-37d9-384f-a74e-f7001e09430f | -3.99458 | -49.40381 | 2024-11-18 05:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 946ef5a8-537e-3d96-ad3c-b5ae0a774130 | -3.1704 | -46.59404 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c8cb8a1f-e91f-3864-b2ac-279e686156c2 | -3.18545 | -53.24623 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2da61a1d-eb0c-3deb-a7ea-dfe4a6efc987 | -3.39519 | -53.27385 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ddf339d-31ed-326d-beb7-7ad4bcf50d16 | -1.20622 | -51.78218 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e0277a3-62d3-3423-9dd6-bf7f6fb157f2 | -2.62818 | -46.83228 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba14659b-21bb-3776-a883-a65f51afd3b9 | -3.58406 | -50.52138 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc73b97-4750-3ba5-88c5-76e028785acc | -3.56636 | -50.25697 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d860655e-c573-374a-9235-585c7254aa00 | -2.11112 | -46.48587 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae59b114-c48d-3fbb-97dd-91c96a6caf95 | -3.55299 | -54.57496 | 2024-11-18 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 78d6b9c7-fff9-34c5-a39b-2d1698fa9498 | -2.82629 | -54.04363 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16323251-1cf0-3882-891b-ea2caa00eadf | -2.60279 | -51.79031 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 48b334f7-6189-30c8-b50f-23bec8beb780 | -2.9444 | -48.32884 | 2024-11-18 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71266564-744f-3243-b9df-6a074cc83128 | -1.93613 | -51.08174 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2be966c5-94f0-3f87-a710-a73451b8557a | -2.14681 | -48.95176 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88204274-cd4e-368e-844e-295368efe967 | -1.36575 | -54.16091 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87903068-843d-3fa1-816f-7a4aa748eb25 | -3.22873 | -45.55036 | 2024-11-18 05:03:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 570529a3-c7d3-317d-b2b1-5c8fc11554ca | -2.8689 | -51.78878 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d1bdcb5f-e00f-33f4-b13a-57c86567be9c | -3.42528 | -50.25457 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6c59a58-9f40-3cb1-a1d2-9d24cf2212c0 | -2.44642 | -53.92374 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35006413-c1f9-31b1-9e91-9ecabdd0e18c | -0.8062 | -51.48782 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8bbcb36-d110-36ce-a83a-4a11881866c6 | -1.70529 | -45.83321 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bb14fc77-ffab-30df-a34a-e866f70ebc86 | -2.69754 | -49.28578 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e731b451-ba6a-3e7c-92b4-93195f6f0b3f | -3.04566 | -49.56533 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94dd1678-85fb-322d-a70b-5831ca8da3ba | -1.63594 | -52.67336 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92e93e1a-41d0-371d-9066-0779f242a73e | -2.87416 | -54.87269 | 2024-11-18 05:03:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0820729b-743b-3c09-8808-91e72f4a13ca | -0.89141 | -52.71983 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da1d15db-bea6-3336-bddc-222119f21222 | -3.48863 | -50.24608 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f7eb6fb-06f5-3b81-8ae7-46a5214b6409 | -1.34617 | -55.44291 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 827f59d8-5a64-375f-ac26-35c75593c390 | -3.34215 | -50.49928 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0f94a1db-dee7-340f-bba7-8ed8a3033f33 | 0.28239 | -51.4266 | 2024-11-18 05:03:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e4772f4-9bf4-33df-a469-5a97d7b79147 | -1.71113 | -45.83072 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d405869f-2b85-31e2-9432-a67d610b80e1 | -3.34083 | -53.30745 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73f9db5e-599c-3e1e-a1ae-75e02ada90f8 | 0.11195 | -49.84395 | 2024-11-18 05:03:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce6752c6-2fbc-3e2a-aa95-9ba42274314c | -2.44989 | -53.68745 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9704c485-4e25-33dc-92f5-4b7d0d5f889c | -3.33126 | -50.49057 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8f9ad3d-80b1-3d26-a353-c4fee392d363 | -1.95084 | -53.33154 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3a43216-397a-314a-a096-b12811a02715 | -1.80064 | -54.03264 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 141880b4-f9f4-355f-9b6c-3b16236be882 | -3.82329 | -52.25999 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09689e7b-d055-3697-ba18-9ebab3a135a4 | -2.92088 | -48.95647 | 2024-11-18 05:03:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f618712-e44c-3ccf-9635-b5b057af5119 | -1.20686 | -51.77808 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4782f01-7d05-3572-a377-6d0ddcf35665 | -3.53497 | -54.49382 | 2024-11-18 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51a5bc1c-e358-35b9-9bfb-6c5f78dcfc93 | -3.38948 | -53.26539 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a412132e-ed0d-393c-9fa1-e01fe8abbd82 | -1.20814 | -51.76986 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 444ab089-1983-308f-b3d7-dbaeed5abb07 | -1.61161 | -52.37048 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8325580f-f004-3f03-b1d1-e7e39a0c3f53 | -3.10532 | -53.10343 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cca6e59a-a388-3a51-872a-5fa2d8810739 | -2.58032 | -51.71707 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3b6969ab-9996-319c-a609-47e6e8e4aed3 | -2.46486 | -53.93744 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ac37685-93df-3f51-b0c2-8326e336275e | -2.60022 | -48.30788 | 2024-11-18 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d660c4a8-dd3c-3dc8-90ef-080fc9df2e2e | -0.89427 | -52.72409 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c2532b7-19d0-3ac8-9d8e-97665edc53db | -1.37687 | -52.08284 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07659ef5-280e-30ba-be7b-ecf94733b16e | -0.56337 | -49.53183 | 2024-11-18 05:03:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3d44b99-810b-36d4-a604-9db91a0e9dd5 | -1.44234 | -55.10914 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d14adcc7-12da-359c-91a1-b64f07640485 | -2.81956 | -54.02092 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f15b7bad-0a65-34ff-8004-849629fd9a49 | -1.58419 | -55.8353 | 2024-11-18 05:03:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8891eb0-6999-3b83-8b94-20c13c0e5801 | -1.27169 | -52.12906 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f86efb36-1fed-3b49-9393-aa2779d5db4b | -3.33683 | -53.31063 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50a65373-004e-36a8-b5a6-14cd9c67288f | -1.36593 | -51.11041 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 065e92c4-f6d2-330f-9f5f-3218d2c17809 | -1.29863 | -51.74447 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b046dab0-6bc5-311b-855f-b3106ecc767a | -1.41085 | -52.05125 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 620a94af-d0c3-3fd8-ad9e-ddbbb460cbf6 | -2.40218 | -51.99333 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18553d8d-a848-39df-905f-a56fddbb57ac | -1.22215 | -54.18855 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 350844d5-f52c-36f6-b36b-33dc76625f09 | -2.60093 | -48.30322 | 2024-11-18 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c34e2542-39e1-3b74-9d92-5d9cf785c59b | -1.69486 | -54.12294 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2a41dc1-569e-34e0-acad-6189ae31f509 | -2.58855 | -53.97441 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55e4a419-3429-35fb-946c-df692d4afa3d | -3.51403 | -49.93673 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ac073ae-3f9b-3428-8212-358682c0b281 | -2.86197 | -51.78575 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2c76454a-51e8-33ed-8330-37f97a465bb3 | -1.07455 | -53.36789 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 138266a9-000f-3c07-9884-be5abdab448d | -3.04554 | -54.40399 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dfb0b732-24a5-386e-83e9-5b2d4d84c7a7 | -3.52455 | -50.25504 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad833516-9fb4-3031-85ac-37d6dcb797ae | -3.04608 | -54.40051 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README35.md)
