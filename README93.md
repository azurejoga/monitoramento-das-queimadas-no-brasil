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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84b3f360-d279-383e-ba5e-ef448073d37a | -1.82578 | -52.02469 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bbec9e0-3c50-3ab1-82dc-9efd148eab14 | -2.7666 | -54.0525 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4a1463f7-d966-3a13-8291-b7a47144dab5 | -4.75733 | -48.36344 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52ee6f22-5f4f-318c-b443-7d767f5afa5f | -2.87104 | -50.32407 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abbd1374-0233-3afc-b93c-de479f0a4587 | -2.46308 | -50.40252 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a05e9ea0-eac8-3d7f-8854-2f41a174a508 | -4.80041 | -44.78248 | 2024-11-09 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c7ba7ef5-0f08-37ea-afbd-b0306e55d74a | -1.236 | -51.77447 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 315432fd-2a12-3fd1-9341-c6663d1bbf39 | -4.06332 | -50.01133 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cda46e56-0a30-3df1-9754-a7abaf7c0fe1 | -3.72517 | -53.40178 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 453fc2f3-ba61-310d-b9af-8747e9f53cce | -3.74683 | -51.94941 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9bc1308-2642-35a4-bf6c-4b8e39077e41 | -4.09187 | -48.50953 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c4a1f7a-6498-336a-92d7-916342b97dc5 | -1.24383 | -51.76844 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6838dac-1365-3317-84bf-f59223ea6fca | -2.83977 | -49.46843 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50a1db20-771f-3217-bb8e-57fc40e2ae4a | -2.31285 | -48.53848 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf57662c-daad-33bc-9e9a-92b0d29571dd | -4.21085 | -50.62554 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 894067e0-6d5f-3792-b6c4-324dd8551731 | -5.19595 | -44.92496 | 2024-11-09 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7610a34f-c471-35e5-a1fe-fe402da26cc5 | -2.8755 | -51.47068 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 325914a8-d9c9-391c-ae49-b827786cc4ec | -2.18501 | -51.73756 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6d88435-2934-30b2-ad52-8b3c552d17dd | -2.55742 | -54.02725 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b9508df-6e7a-332c-86ab-0b2a8152d55b | -3.00475 | -51.44472 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0555c503-2304-34fc-8a22-f12ac38db954 | -0.64354 | -52.38318 | 2024-11-09 04:55:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2f7d9d0-a7d3-370f-bc9e-781541a0513e | -2.23524 | -46.55325 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 918cf040-61e7-38ca-8487-dbae93f9f50a | -1.5219 | -51.3077 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 361945e2-0c00-31d8-8215-e5aa0a22a6a3 | -2.81764 | -48.46867 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00bb6141-c047-3bc2-8f7d-cad1429d713e | -3.11946 | -48.64087 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a309d40-0a55-3d4c-97d0-0326a8803ff8 | -3.09884 | -53.31798 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 23907e0c-b457-33f0-9741-6430ed586544 | -1.19 | -52.15542 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c082956e-eb98-36e0-9ee7-0e32ff9b59fd | -2.57477 | -49.13889 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e7e3aa03-5074-3ee3-ac3f-368f38cb8c41 | -3.183 | -50.59186 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21652d4f-02cd-3746-a98e-50834c64dbdb | -3.53808 | -52.1712 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99e4f8a5-14c2-3840-a8b7-e6d9af3a6268 | -2.1748 | -48.32703 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdee22a0-ca0d-3828-87de-ae443803cf1d | -2.36596 | -46.58477 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d1ac07a-20f7-3ba2-af0b-5adb9afc76d6 | -2.18719 | -53.62749 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff0022cb-aca7-3631-82f1-ba65c7ba9a1f | -3.16061 | -54.48433 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8eb14a4-b664-32a2-b225-d4f5ac728864 | -3.067 | -53.90353 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b48c2b63-a71d-3815-a33e-98b06e054ce4 | -5.25151 | -48.08266 | 2024-11-09 04:55:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 688caa72-a26b-3014-be35-89951e9f019e | -2.70188 | -48.65696 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebadb927-8c8e-31e3-a349-44d46d675c3a | -3.23851 | -53.39614 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 87cf8a42-536d-3dcc-b1b4-f11a228aef4b | -2.15955 | -53.65156 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 349c0fa7-b63b-3181-b56a-14552e721932 | -3.96284 | -48.12583 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b43dcc23-a4c6-3914-99cd-b875d9291964 | -1.68023 | -48.72744 | 2024-11-09 04:55:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6a384e7-3a6b-3a4f-9dd4-7a50b1dca180 | -3.18362 | -50.58787 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd4a9ac5-8195-388d-8267-4a09d7aac887 | -3.5428 | -43.56506 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8140080c-3838-3fc2-8b14-4d1526c938ff | -3.34171 | -50.36175 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bb7d255d-a776-3b97-ae0d-921c17c6a92e | -3.09775 | -53.32487 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c087adaa-edbb-3705-ab1f-922899ffbc86 | -4.23455 | -47.55967 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ab02689-acb5-33c7-8c17-04f26c99e6d4 | -1.45166 | -51.66961 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8123b0a-f466-3745-b7ec-99e38e93b1a4 | -1.52185 | -52.22139 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b0446ae-e4fe-389b-85f9-5a069bc9a084 | -1.25446 | -51.76646 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b95d7519-c83a-3e18-881a-08b952c62310 | -3.91599 | -52.40459 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cce7d48-8c15-30fe-89c4-99c46158b33a | -2.65699 | -48.50896 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b76ac6cb-1475-3b2a-84d0-547fb7e0c894 | -2.79053 | -51.65611 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f9d0979-229d-3043-8687-0cc1bd154ba1 | -1.25055 | -51.76948 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 116ecff3-4031-3bbd-aff4-0a84a5d48bb1 | -2.72944 | -51.71354 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c819fb8-a125-3f84-92e4-40511ac75370 | -2.44146 | -50.25866 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 616e084d-6df9-3075-aaf2-14d17829e726 | -3.28591 | -51.52464 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4d53cf3-ad39-34fb-9771-c29f1ca97807 | -2.84198 | -53.9784 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65bca937-ef92-3bcd-916b-2d8f2768d02e | -5.83666 | -48.78032 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fad40f63-a3a5-315e-9851-c29dac0776d2 | -3.28934 | -51.52517 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71025d6f-4b81-3940-89e8-72b359c7c721 | -2.97172 | -56.88591 | 2024-11-09 04:55:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c709c8e0-3341-3c24-8c8b-4296c25c9448 | -3.02235 | -53.86842 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2705215-8f59-32ff-943f-4a00d3ef6290 | -2.03597 | -48.98297 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac3aba45-b4a7-3c0c-a09e-f34cff6b4258 | -3.21494 | -50.38567 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d908f61-bfff-3da2-ad4b-1f5f9120d23f | -2.40539 | -48.87377 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0de718d-32d7-3594-98c6-56f0533288db | -1.1342 | -54.10383 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba945617-852f-333a-9fdc-b4268efc4319 | -3.28407 | -50.35292 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76c92204-4bb9-3a13-bf5f-e03a4d8f03f4 | -0.84245 | -53.0316 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3d5d426-4a06-308f-b71c-b262e58cf508 | -6.26499 | -44.5423 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bbdcb034-2224-3275-a526-4a053a60bee0 | -2.55239 | -54.01574 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6345ae2-da60-3a31-8677-23cdb76eb5bc | -3.83337 | -46.48542 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b55ab764-d6db-3372-9ff6-5d895e0a85f6 | -3.73086 | -54.22495 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e05e60b5-f029-3745-9710-47be6dd2eb01 | -1.5212 | -52.18201 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fa80e38-5979-3393-9c7f-1b7ba870a256 | -2.94326 | -49.347 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4181f97-87d4-33e0-a8b6-6f07bc6d7026 | -3.34595 | -50.3582 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2054595a-1c64-3914-90e2-424829b616c5 | -3.56884 | -47.37216 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3fd6c6a-713c-32d1-8a33-bb56d3b82238 | -3.25124 | -53.40166 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d4fe693-564e-34db-a9e4-b7ac5164e31f | -3.05216 | -51.06737 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99ad7a6b-f91f-3af8-8bcd-2742c678e438 | -1.19334 | -52.15594 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2401163-024c-3894-8241-1fd078c2e887 | -4.61469 | -49.58142 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ceb66124-73d9-3275-95ec-240b9c3ed601 | -1.52399 | -51.94555 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21260267-9c92-34b2-b895-56298cd18f77 | -1.48096 | -51.74706 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d28e8b7c-4c9a-320b-b481-c46dc8eb028f | -3.2234 | -50.37856 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d47381b-6772-300f-94e7-26df33c01c01 | -5.87001 | -50.30928 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac1afea4-4fe8-3354-811b-3f2145689a9c | -2.86808 | -50.31941 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 760ba568-2113-30ab-b624-e8d1df86c948 | -1.62734 | -52.23751 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ef8e55d-e6ae-3ec3-8840-00a04e241884 | -4.51664 | -45.68135 | 2024-11-09 04:55:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ffeb093-346f-3756-ba27-a2747560bb91 | -2.18383 | -47.9507 | 2024-11-09 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48b989b4-2fab-38f8-b0f9-fa1e8e3778b4 | -2.60068 | -54.02653 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc85206f-d9cb-3e22-8968-f0303fd6a37e | -3.53744 | -49.26012 | 2024-11-09 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b6aaae8-3d9c-3cf7-b61d-d8efa963739a | -2.10859 | -50.66201 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20197907-f650-3259-bc54-620024439c5a | -1.81365 | -52.27754 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1af0d1dc-66ae-3764-92f5-0110c922465f | -1.9736 | -53.13427 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27f733b8-a755-3fc8-8c32-cbcb394778de | -2.79137 | -49.65683 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| dc78d6a9-6aa4-30bd-b36b-1adbfb0b03e0 | -3.88548 | -49.94596 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e9fee92-a2ae-3846-a64f-fc242b4e91a7 | -4.61017 | -49.58549 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d999d630-6443-3428-a982-f19789d2bb27 | -1.91074 | -51.50071 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2975bf6b-9db1-3f38-9617-fa1202b446ba | -2.88748 | -53.97124 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6401983-8d2a-3744-90ed-57e042e4f633 | -3.30273 | -50.08387 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec3a3125-b9ab-337a-8f1b-056e4ba8eb3a | -2.63436 | -46.77522 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6043d3a-ed81-3e10-afce-d8bf1a4905fe | -2.97991 | -50.29309 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README94.md)
