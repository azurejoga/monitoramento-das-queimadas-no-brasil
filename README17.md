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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fddbfe80-d703-32ae-b732-ab8f8e39ffd1 | -2.79189 | -52.95109 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a34cd265-58f0-327e-94c2-11166798a388 | -3.41216 | -53.31013 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9da573d1-3aed-3ad2-98dc-3fe3ead4fc91 | -1.81204 | -56.26519 | 2025-11-28 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2e0886a-6b84-339c-b57c-5e5dbb1167e6 | -3.75281 | -46.94831 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ca20eca-f447-3f1f-a05e-c1ff9e7fd6e0 | -4.05578 | -46.56643 | 2025-11-28 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f643ec4-25cf-367a-99c6-b7539c9fd0b1 | -3.75599 | -46.95793 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 27d13628-bbde-36b5-8f4b-02fb38392c2a | -2.74409 | -54.5967 | 2025-11-28 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccc4aba0-095e-3e14-9539-5f2c5d2c76b1 | -3.44556 | -50.54524 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7567e9ce-7282-30ee-8bf9-19e29117e0e1 | -3.32379 | -53.84733 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1295407-abfc-3567-96a4-22397b562c2b | -3.47622 | -52.99055 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e0a583d-2665-3450-8495-eafd56608e18 | -3.06233 | -50.37671 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e54325fd-55b4-30be-834c-a6952a988a7f | -5.06937 | -40.826 | 2025-11-28 05:01:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0a6e33bd-a455-3256-8880-12ed3a49d4cb | -3.40728 | -54.57785 | 2025-11-28 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74db5297-563a-3133-a44e-e569ddde6de6 | -5.28955 | -44.96216 | 2025-11-28 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de764bcf-7aeb-33fb-b3a4-726d22dabbd4 | -2.79521 | -52.95161 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e371bc67-18ef-37c8-9164-47a590f12567 | -3.8612 | -47.03134 | 2025-11-28 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a87d042c-848a-331d-89e5-b0ba0d57e99b | -3.0625 | -50.35133 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91e2a7fb-2289-3713-a994-d36c294e5329 | -2.36605 | -56.11761 | 2025-11-28 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de9e76ca-09fe-35ba-b813-c26272b39942 | -5.56913 | -44.9762 | 2025-11-28 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbced00b-312e-30ca-8a83-9e573b15585c | -4.86344 | -50.82833 | 2025-11-28 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18f0f896-b05a-3e61-b588-dbe0bcd86874 | -2.8659 | -51.7872 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 241e1907-8d32-3a30-b4cf-7bacdce769d0 | -5.35011 | -44.882 | 2025-11-28 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df62f00e-4ed3-3708-a897-da719c53d290 | -3.40138 | -51.84634 | 2025-11-28 05:01:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc85a437-c802-33fd-b84e-125707bdef36 | -4.34034 | -48.63958 | 2025-11-28 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06c2b2f9-4cbe-3271-b9f4-897fa1600cff | -2.89696 | -50.50042 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63336c9c-5032-3f13-ac55-71c7ee639b76 | -3.41662 | -50.15486 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 547e39dd-3d2b-39d8-a330-c19b6d1db5b5 | -3.76184 | -51.03322 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27f57104-3802-3af3-94fb-748f12018328 | -2.73272 | -51.83711 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abaec0af-3039-36d3-87fa-6da372f63116 | -2.83843 | -52.40141 | 2025-11-28 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c9f0a94-75e1-36ca-af2c-13187be39a29 | -3.78643 | -52.37394 | 2025-11-28 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae147f6b-6509-3fec-a78f-a11f91501df6 | -3.46116 | -50.54617 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2253751f-0032-3f4b-a90d-9ecd62d42348 | -3.75983 | -46.96309 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 93123095-faa5-3746-b904-30550aaf1379 | -2.56732 | -54.7594 | 2025-11-28 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afbe1d79-ee3a-37c4-9438-ca9ffff1fa40 | -3.22873 | -50.14291 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27d21af6-9540-3f88-b344-d3a13a603464 | -3.40607 | -53.30564 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7cd39a2a-e89d-3727-a257-dd473a86226c | -3.22808 | -50.14717 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 409fa9e8-eda8-391d-a326-3c6a47ce62e4 | -3.22392 | -50.31937 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 27a678f8-9c41-3689-918d-01cd6419727e | -5.07027 | -40.81957 | 2025-11-28 05:01:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d6956029-5ff3-3b36-87bf-f44e289994f8 | -3.92584 | -50.99621 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b9aca81-0259-3dd9-af7f-546fab8ef31d | -4.94627 | -48.62764 | 2025-11-28 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d840a9be-25e7-3c9a-a373-a143908565db | -3.84565 | -47.04267 | 2025-11-28 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37fbca9c-6e8d-3377-b6c2-171864800e27 | -4.14401 | -46.76499 | 2025-11-28 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf798e06-ed65-3b51-bfe2-86ba05cd8cb5 | -3.92928 | -50.16944 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd7c1d4e-b311-3f64-9237-64dae823e30a | -5.06338 | -40.81856 | 2025-11-28 05:01:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 458c3f98-6f3f-3f3c-bc21-8f1c4ffcd31f | -2.85653 | -53.01061 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f890c7b-2986-30fe-8378-3e78690ab40f | -5.1294 | -43.02398 | 2025-11-28 05:01:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54226274-0a24-30ad-87c5-2a7e7460c550 | -3.02195 | -51.03708 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bdff69e-eda1-32a0-a37c-af23aa95f59a | -3.91266 | -53.82673 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d8d9f33-f294-3cc1-b340-d474047ea8cd | -4.05991 | -54.41114 | 2025-11-28 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97106e3d-a98e-346d-ad0f-55ee0e8728d7 | -4.06047 | -49.43391 | 2025-11-28 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00446060-7009-3ebe-8ce9-4b527a2f91be | -2.95955 | -51.02345 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb704a9f-2efa-3c62-a982-562c9214d902 | -3.96147 | -50.19453 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 914e65de-62fe-3ac9-95ef-429a20fd8b86 | -3.09561 | -51.54349 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f799bd32-425f-3d30-9319-ed1e73db8d31 | -3.40939 | -53.30616 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e36a28d-267d-3d21-9b00-307bf64b3234 | -2.49785 | -51.81657 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a609a84f-d20a-3e0b-8e8c-b9101fcf4d46 | -3.76051 | -46.9586 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f83bc4b5-8859-3a6a-87c8-c75c3d45aa56 | -3.05871 | -50.37616 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab66544d-3662-3a9f-b383-9ba329d868d6 | -4.67493 | -48.86343 | 2025-11-28 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e065ae74-98a0-3e41-b650-47294adc0b71 | -3.6357 | -44.88062 | 2025-11-28 05:01:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23d53958-b3e6-341c-812c-a6f830992d6b | -3.26505 | -51.17054 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5e47957-1819-3913-8749-4b11c01be84b | -3.34875 | -54.09225 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29427d92-8bd2-31c1-8e28-9d64d8fc02fd | -5.75489 | -45.11113 | 2025-11-28 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df916089-9aed-33a3-ab2d-2a96c59ffb51 | -3.28357 | -52.62164 | 2025-11-28 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 922d174c-2f62-39eb-bb9b-c9cb787f9007 | -5.45097 | -44.68969 | 2025-11-28 05:01:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3df11d0d-be95-3862-8fdf-de3eef18fec6 | -3.38426 | -54.12619 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9544ea49-63d3-370f-adb1-f590adf45f7a | -2.8557 | -51.76324 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92524f3a-688a-3fcd-9bb6-18c4f11cd1d5 | -3.27886 | -53.76608 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f66dea60-c3f2-30a0-85c8-57b4992ac4f7 | -3.59933 | -50.42267 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c80b11dc-e3c6-3647-b939-d15a612b00c4 | -3.71527 | -54.08978 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88fbb085-e289-344c-af5b-7a0aeb85cb4d | -6.72393 | -40.81595 | 2025-11-28 05:01:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2da6b689-d64e-3017-8dc2-d0a17805d45a | -2.79135 | -52.95455 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7d83e09-3eba-394e-be90-3146b0c7023a | -2.96245 | -51.02786 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58eb7961-c51a-3ab6-a979-ab5d5d78dcec | -3.22755 | -50.31993 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2d06ec08-ac2d-32e5-9618-8ce1a394e2b9 | -3.78306 | -52.37342 | 2025-11-28 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7731d4b4-2263-3b2e-a282-8c447d6c7aa0 | -4.95039 | -48.62823 | 2025-11-28 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38a7c246-0728-31a4-bfd6-004420fe9c88 | -3.86052 | -47.03585 | 2025-11-28 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d8e2518-e806-39dc-af4c-258941984429 | -3.38237 | -51.49851 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f17cc199-c012-339b-8b35-98e9a18c1041 | -5.13007 | -43.01937 | 2025-11-28 05:01:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dff0afe8-81b9-3d69-8426-331f92167d71 | -3.59161 | -54.05613 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d997b1e0-c0e8-3e22-8024-1ab24e1bef39 | -3.25154 | -50.01886 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0270cfbe-ab1f-34b6-a0d6-22d38e5b5c2d | -2.82168 | -52.39881 | 2025-11-28 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c298f13-40af-3664-8542-5cfd2678967d | -3.52815 | -51.635 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d77bff3f-57b5-3b5d-ae90-efdc618e93d4 | -7.58362 | -55.49406 | 2025-11-28 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d3c6b93-8b3b-3cdd-8ba8-8f2c345d0326 | -2.7413 | -54.59262 | 2025-11-28 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14b27e0c-7350-3aaf-8499-865b6d020e7f | -2.88406 | -52.77728 | 2025-11-28 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89fd0d73-f2dd-3c38-a4a2-4cb2d5199625 | -4.06432 | -49.43452 | 2025-11-28 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a45d426-976e-3f92-967a-629c2891fe03 | -4.41387 | -50.9643 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15f57e8f-d7b8-3c0b-ab6f-6601579238e9 | -2.94053 | -51.4213 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60a98952-f1ee-30dc-9f9a-54d251c5a1d4 | -6.72309 | -40.82233 | 2025-11-28 05:01:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bb44a2d1-f058-3b62-9f97-6ea02d3a6c08 | -2.88073 | -52.77676 | 2025-11-28 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddd40f04-5a7e-33a7-8e44-c51e46f33a27 | -5.53468 | -46.98364 | 2025-11-28 05:01:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 000fb34f-a7f2-3ff6-b379-964b85d791a7 | -5.57208 | -44.97354 | 2025-11-28 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f19cf05-384d-3e46-a644-d78019fec16e | -3.62854 | -53.65158 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09d24afa-ebaa-3d99-b396-77337dbbe900 | -4.29721 | -55.61056 | 2025-11-28 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eceb671c-94a0-36ba-9fea-b0edf0b884a0 | -4.05961 | -46.56069 | 2025-11-28 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ccd371a3-1e00-303f-a5ac-3fcfbe82e556 | -3.36255 | -50.48623 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecd6e85c-fe35-33cb-8862-2d8c76a84475 | -2.92293 | -51.30708 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78d14915-fb72-317b-b2af-2217be1342ea | -3.46358 | -56.31915 | 2025-11-28 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f06f7c2d-60c6-34f4-bba9-fe462578fa85 | -4.34088 | -48.63603 | 2025-11-28 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d2da972-b4e0-3d50-a56f-4514052d5d94 | -4.0618 | -46.55789 | 2025-11-28 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README18.md)
