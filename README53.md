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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d25b07db-2a70-33ec-8c5d-ac43cb48b8e6 | -3.53244 | -53.51289 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20ab6a20-a2a5-32a5-821a-457b3d576b14 | -1.27053 | -55.70521 | 2024-12-02 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23a60aa4-dc0b-3dcd-a238-e63b57925238 | -2.34019 | -53.86521 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43bf9a6f-6f92-30a4-8cce-ad90b99c144a | -4.77293 | -46.43133 | 2024-12-02 04:48:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7228cddf-7c9e-3de4-883e-a62543ab7f25 | -2.45879 | -53.62952 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67a96f21-4f89-359a-b18f-630eb912b132 | -3.24998 | -53.63683 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f0c34a3-569b-3bd9-b394-847947c5507d | -1.73496 | -52.78099 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5de8af7a-0acb-3617-8889-390b6b90ddf0 | -3.58591 | -50.52007 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ecad3f6-cd64-3ef0-bcad-fea5773ce579 | -2.83832 | -53.97994 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5d124a7-7ed2-3615-81e0-14dd091a651e | -4.10488 | -50.72001 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a658185-2be4-3f44-b460-925933f08946 | 1.1182 | -55.995 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6db371a-cabc-363b-8cf5-0dc6de78cedc | -3.49387 | -53.82247 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25d11f89-daa6-369f-8931-7bbe5529825b | -2.75967 | -54.11668 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbd98362-bc13-35d9-a804-eb78255d2c1d | -1.63383 | -53.86016 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 512d7787-0a73-35c9-80a5-e05a985db990 | -3.58646 | -52.0546 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcac25e0-52e3-3788-95b1-152a0358977b | -1.20684 | -52.08394 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ba482c7-ca5b-3373-a407-076e9b99e309 | -2.83818 | -54.10497 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7aff1d58-bf2b-30ef-b156-758c88bbe1fd | -1.23249 | -51.61815 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2f23b8f-49b5-3b41-9e3d-dd9328f1195a | -4.21052 | -46.37708 | 2024-12-02 04:48:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7efe21ec-8a32-35ab-93e7-b6eb4c7875d8 | -3.86891 | -50.16697 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96dff0a4-c216-3e9c-be44-79bbbff918a4 | -3.40353 | -51.24978 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63d31902-7d26-3414-b0b2-f0eb613ace7d | -2.85294 | -54.07977 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e322790-dfe7-3e0f-a90c-d1d5ae8769ec | -3.70068 | -47.123 | 2024-12-02 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0e9328b-9a7d-3291-b071-bf82bd2115cc | -4.08882 | -48.31896 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dae043a6-8ba2-3c15-a9bb-004805c68a6e | -2.91417 | -54.12092 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95adf538-12f3-3c6a-81d9-158ff30ca767 | 1.11468 | -55.99921 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f749c4c-7aaf-34bd-8da6-2e893ea0e42f | -1.36661 | -51.39271 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf97785c-427c-3f24-aecc-1ecf6d3b4b95 | -2.58732 | -54.2179 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59ab8ddf-dd1e-3c91-9217-55dcb8fd22f0 | -2.43831 | -50.49263 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ba6ebd5-354c-3c51-9ba7-4b57cc81b7f0 | -3.10684 | -54.05163 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6f9fa26-4fcb-32cd-8b42-073e9df78d8e | -1.90983 | -52.8629 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dd361bf-7bac-3462-9875-6e5d4adeef2b | -4.59684 | -50.82806 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1437838-939e-30ae-b8be-48a36fdebd4c | -1.06189 | -53.63578 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7dba47c-5a7a-379f-9575-4b204f7c7269 | -1.32456 | -51.68155 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53611653-9507-3804-8b13-a5897f1170ca | -3.36691 | -50.35435 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5f39575-3aab-39b0-b0b3-8163eebe5bd7 | -2.37213 | -46.07276 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a06cf4ab-cb84-3d53-a5b9-85ce5751b3f1 | -2.59543 | -53.96208 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ec9a2c5-d6da-3e8a-8418-d0901eb4e81a | -3.10717 | -53.76251 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d249fb86-3c67-3c14-b5a6-e36d9f67f3e7 | -2.77667 | -49.21599 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17f6c16c-8b3b-38e6-b147-a9d3991fb7c0 | 1.10061 | -56.01611 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 18c567c7-6945-3655-8060-4778f687be07 | -3.80465 | -51.00921 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e566381d-d2fe-34c1-ae16-ab356860faa8 | -2.71503 | -60.0195 | 2024-12-02 04:48:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c52f353b-b2c1-307b-bf27-82174b2577f6 | -2.86984 | -53.93023 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8aedb8cb-8917-318c-a223-d091f6a70767 | -3.06406 | -53.81413 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c71ca0f8-5821-3ee6-99db-1d13684b388c | 1.0995 | -56.00891 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35edb0b0-4939-3533-b1d5-4f1076ffde2c | -0.61485 | -51.70135 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 133642d8-0207-3d19-98cc-00ddbfbd85b3 | -1.86902 | -51.30956 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3a0a5eb-4cc7-3a8a-926a-79433da4b40c | -2.66258 | -46.12617 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a698d2a-ed82-336f-b7f0-b647c6603c78 | -2.28299 | -45.74541 | 2024-12-02 04:48:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ceb892-dc97-3177-ac73-70707087ca3f | -2.43425 | -46.67304 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87ee91b1-1984-32af-a333-634e096d43fe | -3.0529 | -51.05978 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9641b39-1caf-322e-92db-67a660951ab1 | -1.21881 | -54.19518 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6ae0a60-e14b-39e5-babb-d8604cfdf837 | -2.36504 | -53.86524 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4febb3c9-e0de-317a-af67-7d84132cc19d | -1.77613 | -55.2749 | 2024-12-02 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25403aab-f7a3-3ed0-8feb-f77c75e31adf | -3.06777 | -50.57093 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8860651-29ad-3e3c-acb1-3ed12e00147f | -2.48012 | -46.56888 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4147c8b-ba69-399e-8b0d-cb0bfe182ec8 | -3.46455 | -50.26992 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 709048cc-478c-38c4-a26e-248e9a653c74 | -3.28614 | -50.63017 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27aca39b-1965-3454-9405-e293cdf4259a | -3.96435 | -52.17698 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b2f87ca-2b22-339b-a2ca-a04894529e61 | -2.46323 | -53.71019 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33fdc458-beab-358b-8957-31c2d1e3e6c9 | -3.45778 | -50.26888 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5064bc79-e96a-3a34-94ce-9b3f21cd73a5 | -2.89604 | -48.58747 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37ccf45a-25c4-3ff3-8fee-ea52d96fbb95 | -3.25402 | -49.90886 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcc55080-2dd9-3f36-ac5b-cf68d3f6e3a2 | -3.42709 | -53.88853 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f0f0ab7-12d7-3b1d-94f9-e2fa30b2a9c6 | -2.9668 | -53.89919 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bd4620e-066a-32b8-ab97-24610e899442 | -2.04634 | -51.19668 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93477064-59a8-355c-a4d4-2bdc2e6b8fe5 | 2.42785 | -60.65666 | 2024-12-02 04:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34e88b5d-123d-3304-bdad-15243f0b5265 | -2.68134 | -46.60918 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07f1b990-b635-3e8e-9e9f-f9f481fbba88 | 1.10006 | -56.01251 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 4d0359ee-24fc-3e6a-9913-cccc791de37e | -4.03628 | -50.56328 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6963f131-732c-351b-8321-70a4cc91210c | -3.09643 | -54.05005 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d71d2ad2-eb06-33d8-923d-99716d23272f | -3.93112 | -50.98209 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed5fa937-8c21-398f-ae9a-3308e5403c77 | -3.7216 | -52.27323 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34d20e5a-22be-30cc-a716-d9a4fd59e896 | -2.26388 | -50.72017 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4687535c-90f2-3cb6-909c-a01599cd87e9 | -2.44702 | -54.01105 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3c6c16e-6a12-3e9e-8171-dfe3ab359204 | -1.62278 | -53.86229 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af1b9769-0210-3bec-8d84-0b6a353bb204 | -3.09151 | -54.01423 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53944c0d-8bb2-3f2e-84af-6fdebda64aa8 | -3.26953 | -51.10793 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28f89628-0e3d-34ac-8708-b50e26d7c853 | -2.45536 | -53.629 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 50e2a8a3-5ff7-36ae-bb02-386b789d7048 | -1.1737 | -53.42133 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29495898-48c4-3865-873e-473fe1a27c6b | -2.03971 | -54.65907 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9629caca-1c53-3d0a-9921-abd12ec4c5fe | -1.39125 | -53.55489 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3683451e-6c72-3625-b059-3e0743268465 | 1.13978 | -55.97322 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20e3ecab-faff-3cf7-8741-314367e25c18 | -2.96916 | -53.92211 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a54f41ae-f641-31bd-807b-2d57bb89faa3 | -4.25697 | -50.85196 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9cb7e327-23eb-30bb-b68c-d06ce546c79b | 1.21025 | -56.02465 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 603805e4-fc2b-30c8-9099-c999dd323604 | -1.4356 | -54.52282 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 700d4ce9-e933-35c2-8174-eec1bb80e054 | -2.45478 | -53.63271 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83d9717e-4ef7-3a14-8aa0-12be8232ed49 | -0.23408 | -53.75895 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 197ad30d-16df-3350-83d0-41e428a53fda | -2.9701 | -51.43607 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c6b781d-dae0-3fc0-97dd-6cb6764aaec8 | -4.01271 | -49.94295 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 564b3b0a-766c-3df0-8a9b-3c09ae4856d6 | -2.52723 | -54.25655 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41c313f2-55e6-3c8f-9e52-300889c8201d | -1.98658 | -53.13267 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cb01b74-c7aa-376e-af81-1b4eee4c2213 | -2.55437 | -53.40255 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb0a9d27-444d-37f8-9f0b-6cf598030de3 | -2.38021 | -53.6592 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19641416-5bef-3969-a539-d8b896d79d21 | -3.98418 | -49.90026 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 737782b0-5a15-3f05-ab8c-2865f8e8265b | -3.18095 | -54.33548 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3960147-6a8b-396f-a40d-baf26412e221 | -4.12289 | -53.81382 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f3d2b25-ef97-3361-8c4e-227e0878e151 | -2.61773 | -54.07941 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| deb0cc97-4aca-3799-a715-d126736dd1eb | -4.01213 | -49.94668 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README54.md)
