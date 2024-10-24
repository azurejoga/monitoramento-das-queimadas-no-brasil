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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efafed16-bb22-3b1e-9cf9-2949b112bd39 | -3.64073 | -54.68166 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dcffc928-0375-308e-a7e7-a13cac6f26be | -3.6399 | -54.6867 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9780603d-b61e-3445-9607-1a26b008d23a | -3.63596 | -54.68095 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17e09273-a2a1-3bff-9a1b-374ddf6eb16b | -3.63514 | -54.68599 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd87db57-9070-3f28-a687-08f1dda28f49 | -4.13004 | -55.02562 | 2024-10-24 04:32:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 748e5b74-87af-3236-a58a-50f9738c8fad | -4.12562 | -54.61336 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86ba5014-433a-3438-a76c-578c83200167 | -4.09514 | -54.29165 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18b4e962-1059-3720-bacc-dcfe0ad45775 | -4.09433 | -54.29644 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27fa4017-a9a0-33e7-839b-bdf13133ae18 | -4.09058 | -54.26256 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0b51a96-3ce3-3044-8a36-19b2746d64dc | -4.09054 | -54.29097 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91780b88-efbb-35af-8563-24271da7ae00 | -4.08981 | -54.2672 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7088a024-a4d5-321a-b546-54855990c253 | -4.05443 | -54.28142 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ce02e54-0c26-31b6-adba-e0dcbf9ca392 | -4.05438 | -54.28226 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 08f04a48-9074-30b9-9906-6a2206f7a55b | -4.03868 | -53.87042 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| feb40f3e-5458-33f5-a6f2-084a3f05eded | -4.00975 | -54.38183 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b18367d0-6721-3380-8568-6cd561ef929a | -4.00898 | -54.38652 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ebcebe1-4511-3f86-b038-d87963a42872 | -4.00515 | -54.38095 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 127ae1a6-efc2-383f-814d-3729a4cc6b26 | -4.00435 | -54.3858 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e093fdee-a30c-3bc5-8b59-95cf1c42044b | -3.99539 | -54.46924 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 353f2fc9-6f7e-38c3-bd4b-71790d775016 | -3.99152 | -54.46376 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 28101845-7321-3256-9ce8-8bf681dfcc3b | -3.99071 | -54.46865 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b1dd7597-8aad-3121-9a6a-b1a91990843d | -3.98215 | -54.34793 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7252eaf6-12a8-3199-bd90-3155e38dc0fb | -3.98136 | -54.35271 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf1b1679-6f96-3afb-8a57-987f00fb7e98 | -3.97752 | -54.34729 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 227bd7a0-8e96-353c-87af-07585786821e | -3.97657 | -54.0937 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f57628a3-cc48-3da7-b639-e08c0a4b6fde | -3.96754 | -54.43557 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c1f5831-5034-35fe-9e35-d3e854f54c97 | -3.96671 | -54.44057 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8569d1bd-b66d-34f7-beaf-0ea6a1e596f1 | -3.88908 | -54.14304 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dfef0c4c-315e-3a82-8f4b-f078fe6a410d | -3.88452 | -54.14233 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 727a1685-d344-3ef2-bf5c-5a4e02572133 | -3.86131 | -55.35156 | 2024-10-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbb79d1f-8bb5-3139-92de-3ba69c356595 | -3.81972 | -54.55641 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdfb2b51-85bf-37ad-809b-1f6d68fdaf40 | -3.8074 | -54.47096 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9880b1fb-9954-3eb6-847d-a45a6880a9e3 | -3.80583 | -54.46788 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84fb2154-7443-3cfb-8902-490b8e345c05 | 1.56224 | -55.6644 | 2024-10-24 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93e14c5b-ba85-3a5f-94fc-727535da3117 | 1.55673 | -55.66528 | 2024-10-24 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bb8d2e4-3cc4-3608-8fe1-5c793b3defc5 | -2.02968 | -55.89331 | 2024-10-24 04:32:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8b941576-9cd5-31f1-aafd-dd8f1cca0bdd | -1.96465 | -56.43633 | 2024-10-24 04:32:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9643e438-9299-31f1-944d-14ca210bed5d | -1.96405 | -56.43988 | 2024-10-24 04:32:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2db469f-f872-3b32-bc57-ae89d5696aef | -1.85755 | -55.3004 | 2024-10-24 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4770b8af-482f-3050-9eda-1342dafc3d29 | -1.85704 | -55.30352 | 2024-10-24 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1583049-413a-3f4f-be10-fe92de1996a4 | -1.80697 | -55.40027 | 2024-10-24 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8b04c89-cea6-37f0-abba-b96113d17386 | -1.70942 | -55.04456 | 2024-10-24 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db8a392b-5f5e-3b46-a104-33c34eb9ecff | -1.70894 | -55.0475 | 2024-10-24 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ddd3d31-ffc7-3fc1-9c1a-a0261da9b018 | -1.6935 | -55.11072 | 2024-10-24 04:32:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 029b8841-d13f-3285-87fd-2b07881e8ee6 | -1.60132 | -55.84435 | 2024-10-24 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf4a5ef1-ae7b-3303-b633-ff4390c1a06b | -1.5436 | -55.89668 | 2024-10-24 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3995e0ad-ba20-3636-a6a5-5e653b92bb9f | -1.54304 | -55.90008 | 2024-10-24 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a2dc4f7-b042-35c0-abe8-8598717c2132 | -1.54162 | -55.34849 | 2024-10-24 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad63c18c-29f4-353f-a49d-3e9970e76f07 | -1.4901 | -55.09824 | 2024-10-24 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94323ee7-0357-3958-b4f9-aeed0ecf03b9 | -1.48456 | -55.10035 | 2024-10-24 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b482a536-99a4-3cd0-8d04-fd06da191750 | -1.17691 | -55.70348 | 2024-10-24 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80dd9713-347c-3b55-893c-80e9627b91e8 | -1.17639 | -55.70671 | 2024-10-24 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7670b8ac-2a02-3992-a667-ee7a45850546 | -3.62885 | -55.50748 | 2024-10-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc8208a6-a0e4-331b-86e0-35fa937e105f | -3.6243 | -55.50375 | 2024-10-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6f4c38e-5e5d-3270-bf27-5c6d566779b5 | -3.62381 | -55.50671 | 2024-10-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8529241-d307-378c-97e4-263813ba4574 | -3.61926 | -55.50301 | 2024-10-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c03381b-3cf0-3b27-802d-8f32447087cc | -3.6134 | -55.41364 | 2024-10-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44351637-89da-3362-9ebc-b049ef635cf2 | -3.60771 | -55.5104 | 2024-10-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 77042bb0-bd03-3308-a505-b7382a3dd2ca | -3.60723 | -55.51332 | 2024-10-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5e5573d6-6196-3618-84d5-26a0b1d53163 | -3.60674 | -55.51626 | 2024-10-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8dc1cb4c-d0e0-3e52-8086-b0f384b1b59d | -2.48447 | -55.71525 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 873406c2-e72a-3e9f-90eb-99fdd21c16bf | -2.48398 | -55.7183 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3bfc213-03fe-3d0b-b546-a2061a9b0a0e | -2.48348 | -55.72134 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5aaf0714-e2d5-3372-a568-27a48a950a0d | -2.48298 | -55.72437 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb62a0fe-ea74-3795-808a-5a9a8cfbb2fe | -3.90435 | -55.39823 | 2024-10-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ba4b399-9586-3865-834d-57b20b58acd1 | 1.03216 | -59.60598 | 2024-10-24 04:32:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be973ff5-23a2-3099-af31-7072dbf3dde1 | -11.99278 | -43.91494 | 2024-10-24 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04c2679f-0770-3bb3-a173-5823659b346f | -7.8461 | -45.43653 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 026e37d4-db39-314b-8b50-cc69c0003b2f | -10.28582 | -36.32154 | 2024-10-24 04:34:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d6f411f5-813b-3ab5-89de-85cbd25999b2 | -10.28514 | -36.32714 | 2024-10-24 04:34:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fd8fb981-e623-3863-8c80-30c505c61177 | -10.28491 | -36.32561 | 2024-10-24 04:34:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 77c3a348-cb44-37b1-bda1-e8115a0d5d29 | -8.1472 | -37.38692 | 2024-10-24 04:34:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab6c3c9e-7b5b-31d1-ab21-0977fa289c61 | -8.14664 | -37.39132 | 2024-10-24 04:34:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9152abb4-7e97-348c-8692-04ef4ce49f2d | -8.1434 | -37.38982 | 2024-10-24 04:34:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 415aad52-c67f-3abe-b72e-46a6a022f6b0 | -7.93363 | -39.91005 | 2024-10-24 04:34:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb37df8f-b5ae-30f8-a70b-a0432e62cd2e | -7.93324 | -39.91292 | 2024-10-24 04:34:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b5a9342-2c79-32f7-9630-80243e9b3124 | -7.33514 | -39.32811 | 2024-10-24 04:34:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7e5f4737-8ffa-3250-b4f9-fb31034c7274 | -7.33472 | -39.3311 | 2024-10-24 04:34:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f51a353f-41ea-3685-b08b-b8f5f935e801 | -7.30261 | -39.14183 | 2024-10-24 04:34:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 61180200-d918-3cd5-aebc-ce9dfd622ac5 | -6.73572 | -40.47771 | 2024-10-24 04:34:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ebfdad1d-2f04-3e52-be84-dd89bb7db7ba | -6.73498 | -40.48285 | 2024-10-24 04:34:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e27e5d1e-f954-32af-bec6-6f0aa713b1f4 | -6.73426 | -40.49916 | 2024-10-24 04:34:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e824f3d3-f410-3049-86d4-ee7dedd5c253 | -6.73424 | -40.48797 | 2024-10-24 04:34:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2da874d3-196c-3a71-b1b0-ca68eb4f5640 | -6.73276 | -40.49819 | 2024-10-24 04:34:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| cc2c930e-37ba-3097-8d4e-24936a9364a1 | -6.73231 | -40.47804 | 2024-10-24 04:34:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e6fcfd55-3087-3ac6-ad49-8396996bdecb | -6.73162 | -40.48318 | 2024-10-24 04:34:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a5279b77-7e6c-36ee-90ff-60e240859adb | -6.73097 | -40.47716 | 2024-10-24 04:34:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5d88ceda-2188-34ae-982f-7dbe28884b1e | -6.73023 | -40.48228 | 2024-10-24 04:34:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 68a08201-70bf-34e2-8c7c-ce853e00d927 | -6.87892 | -41.91681 | 2024-10-24 04:34:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7c067e12-1195-34c3-89ff-662be063a207 | -6.93992 | -40.84449 | 2024-10-24 04:34:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1a669e97-6483-36b8-a79c-d87763dc4434 | -6.93924 | -40.84937 | 2024-10-24 04:34:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1cc94832-863a-381b-b8ab-55c120198936 | -6.93527 | -40.84388 | 2024-10-24 04:34:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7493d6a-aa41-3cf0-976d-3e44b0bf1544 | -6.93459 | -40.84877 | 2024-10-24 04:34:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ddc337fc-2378-3df0-bb67-f4e2029629a1 | -11.99251 | -43.083 | 2024-10-24 04:34:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7ce7c4fd-204b-3023-9e82-958835269e3f | -11.5602 | -42.18844 | 2024-10-24 04:34:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 751caf91-49f0-328f-923d-6335ab3b8b78 | -13.71602 | -42.8911 | 2024-10-24 04:34:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 11fb55aa-5b26-3185-9d38-26593a7ac1e0 | -13.70329 | -42.88462 | 2024-10-24 04:34:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d2ffcdae-6a2d-3bc3-8b2f-20691a837dd9 | -13.63245 | -42.53225 | 2024-10-24 04:34:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f84aed20-c338-38c4-bfc2-23a3157ff2a0 | -13.07176 | -43.01911 | 2024-10-24 04:34:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31b75169-f83e-373d-ab3e-6ff785720c0d | -12.66045 | -43.24185 | 2024-10-24 04:34:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
