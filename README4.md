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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20a7b1e9-171b-36a5-a3d7-325c12894b33 | -5.38841 | -46.75225 | 2025-11-26 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 69f5c6d6-fb2d-36ad-b0af-1f95a9373520 | -6.58059 | -47.89426 | 2025-11-26 00:13:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6773590a-532d-3a21-977e-6266dcf2a7ca | -3.47406 | -43.43721 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 2d56565e-0870-3f45-9708-ad7a50fd91e9 | -8.06094 | -43.12995 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 82035297-bf2d-3b2e-b167-b92e5d903d45 | -5.29677 | -43.64351 | 2025-11-26 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ac00a0c4-f1dd-3303-a270-d41403b4199a | -4.44727 | -48.76252 | 2025-11-26 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 59431159-fcb0-3ba4-bae5-e399c8036348 | -3.67748 | -43.5763 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8df14d79-5b67-371f-b300-51798c722f36 | -2.85787 | -46.82936 | 2025-11-26 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0069bef7-277f-33a7-82d4-b3e4daf9f084 | -4.17719 | -43.74692 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a21dfeec-448d-316c-8696-c06c3c92c9ca | -6.0465 | -45.83766 | 2025-11-26 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| cd13ab97-96f9-3460-a5f5-8b55d21e84c3 | -4.27108 | -45.12472 | 2025-11-26 00:13:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 6ad56670-9f85-3648-9f4b-287984cbbb3d | -6.12075 | -44.84889 | 2025-11-26 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 42ba8635-93bb-33d2-b2cc-3428f674130a | -2.91085 | -45.48762 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8a2f31f4-57e0-31ff-956d-25b88b795712 | -5.60647 | -46.26233 | 2025-11-26 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 792d9f77-6432-3cf1-a9ed-7ad9cceda600 | -2.9459 | -49.36834 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| efdd22c1-e548-35f1-878c-96fb2b4ea3ca | -2.88246 | -51.81124 | 2025-11-26 00:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 70e8075f-e4c6-3de0-9770-5b21a7499eb0 | -5.17837 | -47.09958 | 2025-11-26 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8a74a527-055c-355e-acf9-da6cdbe16aae | -3.26059 | -51.1855 | 2025-11-26 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| bc41b0bb-0d09-321f-b8b7-9184f6971244 | -2.63778 | -48.45402 | 2025-11-26 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6607ab00-458a-303f-abb6-78b006d6f341 | -4.72238 | -46.46503 | 2025-11-26 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 30.5 |
| a8f01322-9014-330c-a3a8-721b8864605e | -4.30371 | -48.60083 | 2025-11-26 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 846e1693-f214-39ba-8ef9-d4d5d629fad7 | -5.38939 | -47.23434 | 2025-11-26 00:13:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6af2cbe8-066f-3160-b4b4-69435b712ace | -8.16161 | -43.18917 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1020e477-7213-31ab-9b1e-b3d8383be617 | -7.26776 | -42.54287 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2e20e070-ab65-3888-8ad6-2b57cb10d118 | -3.17882 | -48.61943 | 2025-11-26 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 06090e8d-9987-34eb-8b2e-776579da570b | -2.90073 | -45.47996 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ceab4046-6004-3ca4-a10a-09cec788ebea | -3.20982 | -50.20518 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d8dc497a-589c-3cdb-a952-9340548bc6de | -3.20754 | -50.2245 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 6416b06b-59ba-3eb9-97ab-02e0fe31ac88 | -8.06879 | -43.11876 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| c0fd9066-b94c-364e-85a3-1b5607bc6f2c | -4.15434 | -45.15356 | 2025-11-26 00:13:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e1a2fe87-9f22-380a-a3ce-e16f88b1094e | -2.81939 | -46.7595 | 2025-11-26 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8b520ff0-1873-31d5-a967-01b08251ad09 | -6.30264 | -43.78649 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 6c8fd8fd-8de1-37ab-bc07-4962b24b65df | -4.09868 | -45.015 | 2025-11-26 00:13:00 | TERRA_M-M | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 37d98356-b050-38a9-9451-af2230485dbe | -4.2616 | -45.13235 | 2025-11-26 00:13:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 112.4 |
| c2323061-4681-3976-aac7-94920fe92e96 | -6.29933 | -41.92802 | 2025-11-26 00:13:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 19d89d8e-3e7f-32f8-b11e-540f9ca44088 | -5.33362 | -43.56755 | 2025-11-26 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 3e4990a6-84b7-31c0-aeea-1aafb956a0b6 | -3.66797 | -43.57762 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 550a90a5-fd58-3e0d-b02a-038bdedf0891 | -2.71968 | -45.69865 | 2025-11-26 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b434453e-5edd-3aec-862c-9e24bcb0c38b | -6.57708 | -47.90063 | 2025-11-26 00:13:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| cca953c9-7091-3408-99fd-7b7efa1fdc80 | -5.54754 | -46.90501 | 2025-11-26 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 026cc720-ea7e-3524-a489-fc736241c0bf | -8.20535 | -43.03168 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 590a0eab-25a5-3c8f-ab18-a9d367f7e835 | -3.4726 | -43.42665 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 997645b3-7ae8-32ec-ae15-0bab2e34a53c | -2.71846 | -45.6898 | 2025-11-26 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0b1af66d-e045-3c73-a040-9c93461bf8f8 | -4.15714 | -43.71492 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 76d1cd80-da35-377b-8216-1585fad76b9a | -3.00622 | -49.58512 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4e6bd353-9a55-3432-8f37-f287944f843a | -2.92027 | -51.31311 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b8767b65-237f-37dc-97b1-a502bc12a5ca | -2.72682 | -49.78757 | 2025-11-26 00:13:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9d129fac-d199-3f59-9287-62da0d91eec5 | -5.67055 | -46.52209 | 2025-11-26 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7de7d595-0e30-3254-bfff-4295f4cf50ee | -2.75421 | -47.75336 | 2025-11-26 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1a2405e8-9ebb-3b29-820c-664126a3dbd3 | -8.03365 | -43.12031 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 72029243-691a-379e-8424-b149843a7f51 | -3.98073 | -46.02592 | 2025-11-26 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e41faf5d-2fb9-3b6f-9e38-b8d14fd6a253 | -4.14876 | -43.65464 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ac4bee8e-e730-3ff0-8bee-3c1f088dc5a9 | -4.56403 | -43.80821 | 2025-11-26 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b23273a9-58a6-3b9a-a728-a5fcf5084ce4 | -2.89454 | -51.80969 | 2025-11-26 00:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ef968719-b334-3ec3-a859-f79281b8734d | -8.04383 | -43.1425 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| b6c3b591-0053-373b-a842-1548abe5cd3a | -3.16463 | -44.40226 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| ae14b256-12ed-3cfe-9586-dd29f6ad64ea | -2.92871 | -45.14985 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 32.2 |
| fd8ad0e4-76cd-3e1f-84e0-c2fc914c2d34 | -2.8286 | -43.84674 | 2025-11-26 00:13:00 | TERRA_M-M | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cff24e4a-564c-301e-aede-5221054244db | -4.05704 | -48.81814 | 2025-11-26 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 286b0653-2437-3548-b940-6a7ce36d49d3 | -5.40514 | -49.20455 | 2025-11-26 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5cc6a5a2-6d3d-3b12-869e-9a371d6366fd | -4.15853 | -43.72494 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 277da8bc-cc6f-311f-b724-9cb2456f20e8 | -5.77702 | -47.38067 | 2025-11-26 00:13:00 | TERRA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 14f38719-413c-3532-a3ae-eae6d162d15a | -5.2572 | -44.14562 | 2025-11-26 00:13:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 85f6519e-f665-3085-9c02-db8f9ec28eb2 | -4.14037 | -42.92178 | 2025-11-26 00:13:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 6f94ccb6-8a9d-36de-8fd1-d46e7bc79600 | -4.1729 | -43.71698 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 569.3 |
| 8bdf7f04-6180-32a9-8796-4d08c8e90f17 | -4.64316 | -45.22671 | 2025-11-26 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2ffcd6e7-e438-3393-ba99-e62f1aae0c2d | -3.08645 | -45.35964 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 87dc8817-bfbd-3047-a7e8-ed55f82f67bb | -2.28888 | -47.05145 | 2025-11-26 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3db8db26-fe36-3920-82ad-95fe64adbf14 | -8.04097 | -43.12287 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| c41e7955-0c47-3166-a7a1-364be5c063a5 | -4.52493 | -46.63231 | 2025-11-26 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 64340d35-31a9-3523-b783-19a7aeef5e4d | -2.94187 | -45.50447 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8018fe07-dc44-3b43-930f-779cf6e62cd1 | -6.29668 | -41.92265 | 2025-11-26 00:13:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| a074aa37-0e3b-3211-974d-6bb55316a685 | -2.34649 | -45.73045 | 2025-11-26 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e68f71f6-2f4b-3bdc-a382-9e6081b0277d | -5.54948 | -47.11956 | 2025-11-26 00:13:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cc14348c-92aa-3260-9623-e972cf4243a8 | -4.0585 | -48.82906 | 2025-11-26 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b3440002-5c5a-3b33-9002-8076330b1d45 | -2.74355 | -47.13997 | 2025-11-26 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| e78f1070-d383-3654-bb13-103da5d43127 | -4.23133 | -48.45478 | 2025-11-26 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c037ca30-b10a-3723-b055-af15ae56a9e7 | -4.86928 | -49.01305 | 2025-11-26 00:13:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1099a0ec-4491-3142-a4c0-2ad0f8cc26b0 | -3.48252 | -45.88415 | 2025-11-26 00:13:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9c5c098b-049f-3cab-abbe-9c04297ecc91 | -2.2864 | -47.03357 | 2025-11-26 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 09de6d97-a1fb-35a1-b944-cf1ba110af94 | -5.49126 | -47.03224 | 2025-11-26 00:13:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 57226f02-fc9c-3293-af61-35b2ed32a10d | -2.48771 | -45.15928 | 2025-11-26 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 36f5e3af-d648-3cbe-ab7b-a6fa83cb1c27 | -3.72364 | -43.2247 | 2025-11-26 00:13:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d1d15fb0-621b-381a-b9e1-3f7f8c8aae7c | -4.74536 | -46.55623 | 2025-11-26 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f67c974e-9ce5-394b-a426-c4b81da4259c | -6.47232 | -43.5529 | 2025-11-26 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 1083f0cc-22a6-30ef-a796-31c16c8da1ec | -4.65195 | -45.08283 | 2025-11-26 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ea27e688-895a-33e0-9613-1511137ae18f | -6.35327 | -41.39672 | 2025-11-26 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 9124978d-97ac-3f8a-a222-83cacd8f26be | -5.70773 | -47.06601 | 2025-11-26 00:13:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 85054912-682d-37a5-8c49-d9c91854fe74 | -4.92169 | -49.02365 | 2025-11-26 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ba7d19d2-9c01-3d9c-a1d1-27c5c51c8440 | -2.9359 | -49.3697 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9209653d-0bcb-3c7f-b3d6-4991f44c7923 | -2.74231 | -47.13096 | 2025-11-26 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| a9c17447-b0c0-3579-8a9a-2d109626c2c0 | -4.1182 | -44.82762 | 2025-11-26 00:13:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 79f7ef1b-9690-31c3-9c5f-1d53d3c1e378 | -2.7096 | -45.69106 | 2025-11-26 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 06e1a157-0f7f-3f5e-b3e5-829fa8ad0d6d | -4.54904 | -43.29425 | 2025-11-26 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6429902-03aa-382a-8e71-a037a6dabcff | -2.92064 | -48.22391 | 2025-11-26 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| a27f12c4-74b2-3188-97ab-c824964dbebc | -5.335 | -43.57743 | 2025-11-26 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2a289dbf-922a-3e65-8c25-d04ee203c1d3 | -4.138 | -42.91705 | 2025-11-26 00:13:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 32af6a31-7c2f-31b8-b909-97ec2582860c | -2.60395 | -48.13668 | 2025-11-26 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f8b656e8-f2d8-3546-aee7-9d15ae1e39d9 | -5.38813 | -47.22492 | 2025-11-26 00:13:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c35a10c-d603-38b7-884e-3bfba7c75077 | -4.29024 | -44.54167 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README5.md)
