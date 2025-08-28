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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12f37c1e-eba2-38ea-ada1-1502d02a8a82 | -15.68233 | -52.76127 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22f1e7f5-d41d-365e-82ed-b3d018464154 | -19.46892 | -42.62217 | 2025-08-28 04:10:00 | NOAA-20 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5a6ede42-9a7c-3c7b-b98e-bb3db903ee7b | -19.96789 | -47.52593 | 2025-08-28 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f89af8c6-214b-339b-b362-d5f5802ea643 | -20.1428 | -47.374 | 2025-08-28 04:10:00 | NOAA-20 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdce52d8-55e3-3b26-a6a8-2fefec3eb64a | -18.12679 | -45.20486 | 2025-08-28 04:10:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3432708-c494-3933-94c9-3e3b4f3ee335 | -20.80079 | -44.57662 | 2025-08-28 04:10:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 66b9c717-6f51-30ac-9de5-f4c62c6e9680 | -12.99997 | -56.911 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35fea023-c861-33f1-9bde-57abb4412e5f | -19.37388 | -44.86481 | 2025-08-28 04:10:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45f25e26-1d4a-350e-ae15-8d0d19e0b126 | -23.32667 | -47.84592 | 2025-08-28 04:12:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 450e50fd-f6ff-3e31-bc36-fb1c8533a081 | -23.32737 | -47.84185 | 2025-08-28 04:12:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6e11f3b4-2415-3401-a7de-acd0ca518c17 | -22.90554 | -46.64923 | 2025-08-28 04:12:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 279e0b91-7cab-3f18-b21a-4f93ec2c3567 | -22.68186 | -46.84151 | 2025-08-28 04:12:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eff45a8e-8940-3160-9f22-c346ffe4fa94 | -22.97415 | -54.14112 | 2025-08-28 04:12:00 | NOAA-20 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 36e81cd0-a77f-3176-9a2e-b9a474b2ca5a | -23.5476 | -51.73304 | 2025-08-28 04:12:00 | NOAA-20 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d7e706dd-2266-3063-b566-2991da5dcbb6 | -22.671 | -46.82344 | 2025-08-28 04:12:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f14f6e40-d966-37c1-8dfa-99d61162443d | -22.67849 | -46.84089 | 2025-08-28 04:12:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 738cb0db-1929-3be6-972e-c7bdf43170be | -22.6812 | -46.84545 | 2025-08-28 04:12:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 56bc74dc-57fe-31e3-98b8-68e6194faa86 | -23.54843 | -51.72884 | 2025-08-28 04:12:00 | NOAA-20 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| cd1a35b5-6d33-380b-a321-422a725fb7fd | -29.77761 | -51.17664 | 2025-08-28 04:14:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 9e7cceb6-f708-35a4-a6d7-b171c057b09e | -29.95184 | -51.61506 | 2025-08-28 04:14:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| e0528b1c-656d-333e-9c56-f3d26410dda9 | -29.42961 | -55.62201 | 2025-08-28 04:14:00 | NOAA-20 | MANOEL VIANA | RIO GRANDE DO SUL | Brasil | 4311759 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 8d2f8258-93b4-3900-ba8e-d65e630b12a5 | -9.1155 | -65.7699 | 2025-08-28 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 171.0 |
| aff015ac-86f6-3aed-94a0-5d961a283cf9 | -9.1339 | -65.788 | 2025-08-28 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 4053c4f1-c2df-305f-9c46-1ed3cd722ba9 | -10.5375 | -46.6894 | 2025-08-28 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f2077f27-9413-349d-b175-00ba1c653acb | -6.8774 | -43.5919 | 2025-08-28 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 9454e4fb-4326-3f5f-a540-4daa741d4fa9 | -10.8236 | -60.7633 | 2025-08-28 04:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| baa0635d-d8a3-30d1-9bc2-b8c40161465e | -10.3273 | -46.7821 | 2025-08-28 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a7fb9ffa-131e-3de0-992a-28903120b9dd | -10.8049 | -60.7644 | 2025-08-28 04:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| c1a3992b-617e-3dc2-8705-f5685ef50d53 | -10.4738 | -57.9366 | 2025-08-28 04:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 5e0a0a77-354a-3f7d-b3ec-e73ee886f000 | -6.896 | -43.6135 | 2025-08-28 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 8ed53773-4405-3558-a841-98ca0caf7740 | -9.1154 | -65.7886 | 2025-08-28 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 186.3 |
| 5397ecba-3f4e-3627-b745-ca5ea1af1401 | -6.8772 | -43.6152 | 2025-08-28 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| ed59d314-92f8-3299-b365-7652f715538f | -9.134 | -65.7694 | 2025-08-28 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 5cc77f2c-e00f-39aa-95ca-af06a0966ab3 | -11.3329 | -43.5452 | 2025-08-28 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| dc78cd44-1078-3a22-a4c3-cccd23c7c3ce | -10.4738 | -57.9366 | 2025-08-28 04:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| ecfe60c2-e317-3877-9fa5-7b82271ceb8a | -10.8047 | -60.7837 | 2025-08-28 04:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7a0a60c6-f740-3e5d-ba62-010ee2e9ed67 | -9.1339 | -65.788 | 2025-08-28 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 2a7c17cf-7cd4-3acd-b673-02f7c84e33ec | -6.8772 | -43.6152 | 2025-08-28 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| b5f5e90b-4ae1-3fdd-a4e8-86dd9c22be29 | -10.5375 | -46.6894 | 2025-08-28 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| a59dcaaf-e806-3bb7-b59c-ed5ea18602a3 | -9.1155 | -65.7699 | 2025-08-28 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 227.8 |
| 645a31e5-254b-3d7e-a955-3aba71f1cb1f | -10.8236 | -60.7633 | 2025-08-28 04:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 93326b06-162d-372f-b2c8-73780668caa1 | -10.4736 | -57.9563 | 2025-08-28 04:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1ae0ea9a-fe22-3cfe-8fd2-0830ab9412dd | -6.8774 | -43.5919 | 2025-08-28 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| bc815825-5b79-3bf7-a250-dffccd34ca29 | -9.134 | -65.7694 | 2025-08-28 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| d714b159-ed8a-3243-b2e7-4b06ba6fd504 | -6.896 | -43.6135 | 2025-08-28 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 94bf9d34-2bfa-38ca-b93c-5b7c3f946da2 | -10.8049 | -60.7644 | 2025-08-28 04:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 43b4710e-98d7-3c9a-9657-23fe3ac9fec1 | -9.1154 | -65.7886 | 2025-08-28 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 207.1 |
| 3334bef4-b5fc-3968-838d-87d9dad521b3 | -10.5184 | -46.6917 | 2025-08-28 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0c88f73c-48b7-372d-b4f6-e48c4318d78b | -6.5043 | -35.21949 | 2025-08-28 04:36:00 | AQUA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 537a3cd4-d439-3514-857d-a488464897ec | -6.49932 | -35.19847 | 2025-08-28 04:36:00 | AQUA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 91.4 |
| f1821e1e-96c3-3431-8299-ea5b212a9edc | -6.50826 | -35.19503 | 2025-08-28 04:36:00 | AQUA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| 72e78021-a245-3ee1-99f5-da0a1f8660ef | -10.5188 | -46.6693 | 2025-08-28 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 93adf173-9a44-3a08-ac13-6539e7b82a09 | -6.8774 | -43.5919 | 2025-08-28 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 0270ee86-0c63-3ae4-b0db-2a9b73e9f314 | -10.5184 | -46.6917 | 2025-08-28 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 89fd1e4d-cf9b-39d2-9b1c-a9e983d54767 | -10.4736 | -57.9563 | 2025-08-28 04:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| b8536f29-4761-3334-9705-24cf2709ae5e | -9.1155 | -65.7699 | 2025-08-28 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 197.7 |
| ae510d34-e102-363a-8fdb-01b7918fca61 | -9.1154 | -65.7886 | 2025-08-28 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 224.3 |
| ae8075a0-3e61-3921-9785-cd4634e3c893 | -9.1339 | -65.788 | 2025-08-28 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.2 |
| c08b3302-b5bf-32c9-bb04-716a3b5151d3 | -10.8047 | -60.7837 | 2025-08-28 04:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| bd7f3a0c-9194-3006-a276-1c056b6814d8 | -10.5378 | -46.6669 | 2025-08-28 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| fc00d9e2-8a35-352a-ae6d-dedfb9f2b079 | -10.8049 | -60.7644 | 2025-08-28 04:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 09a4c907-ff00-3f4e-8cf9-c62bc5b7c13e | -14.2761 | -53.0655 | 2025-08-28 04:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 99677624-98b2-3084-9362-4976e49b2580 | -10.5375 | -46.6894 | 2025-08-28 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| c7d93f2c-4481-3a9f-a17c-e5eefa3e0c36 | -7.3955 | -39.6845 | 2025-08-28 04:40:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 4518df2c-2d8d-3285-90db-db90eaf05ac9 | -12.8032 | -48.1516 | 2025-08-28 04:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 64207cb4-33b3-3750-b1e7-e589cc070876 | -7.3958 | -39.6595 | 2025-08-28 04:40:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 82.6 |
| da45fac8-d7b8-3dac-959d-a7dbbe4954c1 | -10.4738 | -57.9366 | 2025-08-28 04:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| af5a1ce9-f450-3b60-9f28-b741332d1d57 | -10.8236 | -60.7633 | 2025-08-28 04:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 49b35023-46b2-3368-80be-8ffd58127343 | -6.8772 | -43.6152 | 2025-08-28 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 5ff55d28-bffe-3036-8c7c-9eb8f7a2f740 | -6.896 | -43.6135 | 2025-08-28 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c9f565a1-3e97-30d7-828e-8b9f9e145f39 | -9.134 | -65.7694 | 2025-08-28 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 8371c06f-68b6-3552-9dfe-879c781dd83f | -8.3082 | -45.1566 | 2025-08-28 04:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| acccc36e-9754-39a8-9b08-06fd4dc1f82a | -10.8049 | -60.7644 | 2025-08-28 04:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 202.4 |
| 8da75f57-e3a8-31c8-8f9a-dfd0b01e3464 | -8.289 | -45.1814 | 2025-08-28 04:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 04efbeb6-a3f7-3a08-941b-9c8a9d1fc88b | -8.2896 | -45.1357 | 2025-08-28 04:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 0b543573-c6fe-3d27-a5d8-05861b373bee | -14.2765 | -53.0444 | 2025-08-28 04:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 41d622ee-aafa-3795-97d9-ec080cd80985 | -7.3958 | -39.6595 | 2025-08-28 04:50:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 820b6c13-d190-38e8-8a84-d1ffbc4f0ae9 | -10.7862 | -60.7655 | 2025-08-28 04:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| de6d55fb-62cf-3c28-89de-052265127047 | -8.2702 | -45.1833 | 2025-08-28 04:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| ad4dabe5-5df4-35e9-bd95-6717cfe1f20a | -9.1155 | -65.7699 | 2025-08-28 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 223.7 |
| 15be7d17-ccf6-3e68-b00e-0954e0c299c7 | -14.2758 | -53.0866 | 2025-08-28 04:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d36f4ea9-970e-328c-9385-1f00a818d358 | -9.1339 | -65.788 | 2025-08-28 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| d4e2ed61-68f0-381c-b125-18ef4c617e88 | -10.8236 | -60.7633 | 2025-08-28 04:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 60913c27-b4cb-325f-9eb5-ae3b3a04ea62 | -8.2705 | -45.1605 | 2025-08-28 04:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 8519d546-189a-3b3d-91d9-8fa187388780 | -7.3955 | -39.6845 | 2025-08-28 04:50:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 7723b2c0-1a68-3561-b315-f30f76c1f94a | -14.2568 | -53.0679 | 2025-08-28 04:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 129.1 |
| bc62c8f8-a063-34ff-a740-0a886a744246 | -6.8774 | -43.5919 | 2025-08-28 04:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 95d01bf9-d0d6-38cb-b1ac-30f88744ab48 | -14.2761 | -53.0655 | 2025-08-28 04:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 426.9 |
| 32a376e5-31c2-3d1b-9c22-d7197aaaaad6 | -6.8772 | -43.6152 | 2025-08-28 04:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 66fb209a-1947-351e-8fff-9ceec1c7911e | -8.2893 | -45.1586 | 2025-08-28 04:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 576.7 |
| cd753fcc-5682-35ad-b95f-52ef28864e9d | -9.134 | -65.7694 | 2025-08-28 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 176.7 |
| 36f5fcc8-4f36-314c-9c6d-7eab9093915c | -9.1154 | -65.7886 | 2025-08-28 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 4d088722-4341-31b8-8503-53a3957b9967 | -14.2572 | -53.0468 | 2025-08-28 04:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 1eee97a3-2ca4-3da5-9fa7-3af2b67cbefb | 0.77604 | -51.33419 | 2025-08-28 04:55:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 555d99ef-9ea4-3520-898b-93bd0642c207 | -2.44616 | -47.32866 | 2025-08-28 04:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7042da55-9c91-3b03-807a-6bda6d4a6b5f | -2.44742 | -47.33095 | 2025-08-28 04:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d43fc44-4364-3802-a2b4-04222414a296 | -0.75353 | -47.75759 | 2025-08-28 04:55:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c604820-8214-337f-8ae4-8f93aea18182 | -2.44369 | -47.32609 | 2025-08-28 04:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 206a488c-e5ca-3769-a267-8bd4530afb9f | -2.44551 | -47.33281 | 2025-08-28 04:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0810e5a5-caca-3ce5-acaf-8c1d7423405f | 1.04678 | -51.21928 | 2025-08-28 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README48.md)
