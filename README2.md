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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8349cad5-642f-30a3-a4bf-08665a555a7b | -2.81 | -52.94 | 2024-11-06 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dab2b5f8-1a60-3796-b2e2-569844379d87 | -3.71 | -41.69 | 2024-11-06 00:00:00 | MSG-03 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 810d852e-6113-3de7-b59f-563fb89617ea | -6.49 | -47.46 | 2024-11-06 00:00:00 | MSG-03 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58578c72-9cd4-3d73-b4fe-26f3780aa1cd | -6.46 | -47.51 | 2024-11-06 00:00:00 | MSG-03 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3b34ccd-ff85-3681-b7ae-08df7c3e6be8 | -6.49 | -47.51 | 2024-11-06 00:00:00 | MSG-03 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a41bacb-e578-343a-9c9f-8f204ffa6080 | -2.84 | -52.94 | 2024-11-06 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa6c38ba-0719-3e93-903e-cd47c3bd95be | -2.81 | -52.88 | 2024-11-06 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd4f2694-5700-3e85-8669-5fb9bc4ea8ef | -0.8355 | -52.8503 | 2024-11-06 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0157cb82-424c-3180-95d7-d01d6f2c2cd7 | -6.1414 | -43.9794 | 2024-11-06 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 0185efa7-d473-3228-b48b-b9b5da7dcfb8 | 3.6184 | -51.3162 | 2024-11-06 00:10:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 83.2 |
| ad7bf2df-c75d-390b-bdf0-ec87d5b309f6 | -0.8539 | -52.8298 | 2024-11-06 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 1ad0e0d3-b93a-3068-861c-f851d77f5470 | -5.5445 | -43.7012 | 2024-11-06 00:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1f670ff1-269c-3b0f-8d26-749b040c3df7 | -3.5631 | -47.3847 | 2024-11-06 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9756d774-5a99-3c2c-8f3f-d6ad0777089a | -2.2505 | -46.484 | 2024-11-06 00:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 89a786b8-6049-38c6-ae1f-0516dc262d21 | -3.1786 | -50.6016 | 2024-11-06 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| fd4912b9-d75f-3782-bea0-ba36d3239a4a | -6.1041 | -43.9593 | 2024-11-06 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 9ff187b5-e404-3619-8747-7d847a868d7f | -3.0023 | -53.4232 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| a3e3c3ee-cb2e-3a4c-b807-464d8f4dc786 | -3.5447 | -47.3636 | 2024-11-06 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 01c5c07b-641f-3d6d-a63b-25df8ac70cba | -2.764 | -53.2062 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 1b04027e-5398-3313-bcb6-cf44ea4a337e | -6.1226 | -43.9809 | 2024-11-06 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 191.1 |
| c3699c0c-a90c-3cf7-b221-b63991d08ba5 | -23.93 | -54.0787 | 2024-11-06 00:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| fa7b9014-01f7-36b5-9e1c-77c1413a3b6d | -3.7068 | -41.6758 | 2024-11-06 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| abc3e115-f188-33ee-b498-28cc4fbde0b9 | -3.0023 | -53.4434 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 40fd2613-1b4f-348a-821e-b40361391b4a | -3.5261 | -47.3644 | 2024-11-06 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 41f24126-e144-3864-b0e9-0df38af467a6 | -3.526 | -47.3862 | 2024-11-06 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 80d3ecf0-db65-3061-8e46-c370e3f1bd94 | -3.7255 | -41.6748 | 2024-11-06 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 5f723733-1dd7-3c02-bd16-076bfefecb8c | -4.4715 | -50.6583 | 2024-11-06 00:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 46ae32df-ff77-31fd-bf2e-036d31964af8 | -3.9669 | -48.1716 | 2024-11-06 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 433f8034-2c9b-36e8-90c6-17a8275d9501 | -4.1432 | -43.5822 | 2024-11-06 00:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a71f0a1c-a9eb-3812-96ec-e0befb541342 | -1.2739 | -54.5587 | 2024-11-06 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 4e2f488f-bc5e-3e86-9eea-98d371caa924 | -6.4827 | -47.4827 | 2024-11-06 00:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 73260b1e-46d2-3c8f-b4a1-2b6a06b2ced5 | -3.2231 | -53.3972 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f2de759f-f178-3f27-84e0-06a921137fe6 | -6.5012 | -47.5033 | 2024-11-06 00:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 294.9 |
| e8f41a3a-2e86-3dd0-87c5-f40c2e8f2500 | -2.8065 | -51.4855 | 2024-11-06 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 98df5abb-39a0-3098-8362-0e78416b7314 | -2.8662 | -45.5977 | 2024-11-06 00:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 9f7bd808-878f-33ca-a004-aeb93299f44c | -1.2922 | -54.5585 | 2024-11-06 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 58857760-1745-3fec-bc56-2463d07df65f | -3.7254 | -41.6987 | 2024-11-06 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| ad99f9c0-71d2-3dcd-9f94-317f77da8b0d | -2.7639 | -53.2265 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 36aa3843-3746-33c9-b234-f839caaba20e | -2.1746 | -53.7036 | 2024-11-06 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 2f24b5fa-1b37-39b0-b230-bb8e89b6906e | -5.675 | -45.9232 | 2024-11-06 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 1d2144d2-1c0d-35c8-9ad8-7c4721a85cd2 | -6.5016 | -47.4594 | 2024-11-06 00:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 51ef3e91-533a-38d8-8e5d-f68a205e0c6b | -3.0213 | -53.2607 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| c60bd51a-b179-37a1-a048-b75b6f3c9e38 | -1.2922 | -54.5784 | 2024-11-06 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 1b289c88-304c-38e1-a2b1-ec434c1d6e8f | -6.4909 | -44.6633 | 2024-11-06 00:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 728aa2e6-6e28-3510-87b6-cceb29351215 | -3.1802 | -50.2032 | 2024-11-06 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| a93f8e36-74cf-399d-b07f-02aea4f5410c | -2.6764 | -51.8189 | 2024-11-06 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 52356585-b8fd-3525-ae29-de1f5e41e352 | -2.7243 | -54.1552 | 2024-11-06 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 8595cc2e-132d-3eae-a751-226e30052e54 | -23.9517 | -54.0521 | 2024-11-06 00:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 70.5 |
| b7e9e658-55b7-3217-ad37-d4e59053393a | -5.6561 | -45.9468 | 2024-11-06 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 429180db-7a16-3cf6-ae25-ca85c344f21a | -3.0607 | -52.5066 | 2024-11-06 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| faecb71f-8d21-394e-9984-0548b8bc9795 | -3.7066 | -41.6997 | 2024-11-06 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 7199324f-e74f-3a8a-9c9d-73dd5356f3d9 | -4.0666 | -46.9466 | 2024-11-06 00:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 367b77e8-10cb-380a-82b3-d2b302797c6c | -3.2415 | -53.3967 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| b486ed15-1eac-3de8-a8d8-1024a4f7279a | -3.0397 | -53.2603 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| e26fea63-f184-3d05-9558-d7a46e961f90 | -4.2165 | -53.5686 | 2024-11-06 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| eb703f12-087c-3c70-96ce-ac8dfdd65cee | -2.8506 | -49.4744 | 2024-11-06 00:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 9117e67b-7b91-377e-a393-8e7dac50f123 | -5.6748 | -45.9456 | 2024-11-06 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 923fc035-bdea-3bdd-bef2-1c0d083ec198 | -2.6764 | -51.8395 | 2024-11-06 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c6b437eb-7914-330f-96c0-7dfe35a993c1 | -4.1246 | -43.5833 | 2024-11-06 00:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| d5007f5d-7187-3447-96f3-2fb0f9843176 | -0.8355 | -52.8299 | 2024-11-06 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 92508fb4-5fd8-3d41-ab18-9d977d621586 | -3.0214 | -53.2404 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 48e4d004-92e1-37a1-80ef-f7707e434cad | -3.5305 | -50.3387 | 2024-11-06 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| ede72337-0b38-3d51-b340-3603227aa647 | -3.6788 | -50.2284 | 2024-11-06 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| bd06f3b6-3e63-3fcc-95c3-3fc884f55f53 | -3.1617 | -50.2038 | 2024-11-06 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 513e6182-682e-3d98-beab-955402402a94 | -2.6131 | -54.5381 | 2024-11-06 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 2c50e306-22e4-36f9-8536-7ec4fd512fb5 | -3.0212 | -53.281 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 10b98cf3-9918-3f0c-854c-5e9cfdb1d955 | -3.7564 | -45.9422 | 2024-11-06 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| faa4b784-2b4e-30aa-a583-5816448de15e | -3.5446 | -47.3855 | 2024-11-06 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 269.9 |
| 4b5741a2-44ea-3b83-9b75-7376beb776aa | -5.5632 | -43.6998 | 2024-11-06 00:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| dcf6a4fb-411c-341c-a26e-74bcf2b6a6bb | -6.5014 | -47.4813 | 2024-11-06 00:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 471.1 |
| b4a46080-a0da-3948-9025-04bda0407454 | -6.5096 | -44.6618 | 2024-11-06 00:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 8efef07b-3a02-3072-ac04-313b0cb0647a | -5.6563 | -45.9244 | 2024-11-06 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c9722c56-c25b-3926-a1a2-cb7ed99a002b | -3.2054 | -53.2153 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 460b9953-7573-3ba5-b448-7966bd2f6213 | -2.2691 | -46.4614 | 2024-11-06 00:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 46617c0c-7941-3f7d-a142-83b9d2af441c | -2.7244 | -54.1351 | 2024-11-06 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 67da77ea-9caa-3524-8b24-be3cbab5532a | -3.0207 | -53.4227 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 2aaf384e-2aeb-3c83-afaa-108b18393dd8 | -0.8539 | -52.8501 | 2024-11-06 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| be837df5-be42-3a62-b002-d0b1759e0720 | -2.658 | -51.8194 | 2024-11-06 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a576736c-01ec-39b5-9f46-49cc30b76f13 | -3.967 | -48.15 | 2024-11-06 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f4f8b54f-3da9-3814-8f29-325737990eab | -4.0667 | -46.9246 | 2024-11-06 00:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 776b4806-ab24-3afa-90ed-7275dfc2fde6 | -3.5444 | -47.4073 | 2024-11-06 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 378c57d8-dba5-3d01-81f4-7f6448e56737 | -2.1746 | -53.6834 | 2024-11-06 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 216174cc-e2b6-33cb-9190-c37ed55119b1 | -6.4906 | -44.6862 | 2024-11-06 00:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 1d512c7d-639a-3420-a9d0-e7c42324394f | -3.2053 | -53.2356 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 78c461e4-ec06-37b5-85f5-d26f1cb232e5 | -23.9512 | -54.0744 | 2024-11-06 00:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| 9a577eac-24b4-3bdb-9349-35333d2e7255 | -2.8661 | -45.6201 | 2024-11-06 00:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| d2fb5c93-f8f2-3ec2-84a8-b844e4d3cd26 | -6.1229 | -43.9578 | 2024-11-06 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 6fb1031d-41d6-36a9-9790-953720fa440d | -3.0207 | -53.443 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| da18aa99-cfad-3786-992f-9c8c88507ba9 | -4.5614 | -48.0141 | 2024-11-06 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 3a4d78f1-a755-3855-aa98-8f08aa646384 | -6.5094 | -44.6847 | 2024-11-06 00:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| b643b52e-5826-36be-99bf-2b4e4141081d | -6.1416 | -43.9563 | 2024-11-06 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 08933f5d-d7e8-34e6-97d9-f54397d11294 | -6.4825 | -47.5046 | 2024-11-06 00:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 14cc9c69-c2b9-3d29-826c-ad3534e35846 | -3.0396 | -53.2805 | 2024-11-06 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| b26673a5-f766-33b2-aa2b-adf06d4f92af | -6.1039 | -43.9824 | 2024-11-06 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 710d1385-4e3e-386d-aaa1-84bb93116a31 | -13.83611 | -41.79908 | 2024-11-06 00:13:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 4b641873-4678-364a-935a-fcffadaea775 | -13.82512 | -41.80083 | 2024-11-06 00:13:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| e655938a-f2ec-3469-b2ce-7771f775d927 | -9.89979 | -42.08398 | 2024-11-06 00:15:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 09dfd7b2-a8f8-32ed-b6b1-5b56215d0b67 | -9.5698 | -37.81709 | 2024-11-06 00:15:00 | TERRA_M-M | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1c6064b2-5d56-30e2-97d2-63baaa644317 | -9.0444 | -35.62623 | 2024-11-06 00:15:00 | TERRA_M-M | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 4fc26f66-b7ad-362d-b22d-55d656fd62dc | -10.61283 | -36.9761 | 2024-11-06 00:15:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |


[Clique aqui para ver as próximas entradas](README3.md)
