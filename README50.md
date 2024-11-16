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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed8d9b4a-4a10-3451-9bc0-aee2c9f709a6 | -3.89419 | -50.07533 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b2d747a-cd8a-382c-ae96-67c8499e5ea1 | -4.22171 | -46.81709 | 2024-11-16 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02710713-2274-3853-89be-973f86d1fe84 | -6.30636 | -39.48645 | 2024-11-16 04:50:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f944ef18-609a-3a55-9766-e25c31697b69 | -3.91284 | -49.03974 | 2024-11-16 04:50:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22e3ac29-725e-33fc-ad52-d0e584262893 | -4.37414 | -45.62177 | 2024-11-16 04:50:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4dc3246-2b59-3929-a776-54e77f38027b | -4.23164 | -50.67787 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ba2608d-08a1-3c50-895d-486576b1ec6f | -3.88059 | -52.2698 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d2c6802-1f9b-3deb-bd32-d77e3f357478 | -3.58179 | -50.5316 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5dbddb5a-71cb-3f08-94ef-9195dc1e6b0a | -3.61226 | -52.22742 | 2024-11-16 04:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a31707e-c8cc-346e-adb4-4ae0678eccc2 | -4.28302 | -48.20439 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0657cc5c-cf32-303c-a64d-63c122817667 | -5.91053 | -46.23245 | 2024-11-16 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93a0695f-c3be-3516-94b1-12b3c505d0fe | -4.22435 | -50.68042 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d801ada2-55f4-34f8-99e4-e0dacfc2ed8c | -4.90798 | -44.03679 | 2024-11-16 04:50:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25b99166-bed1-3264-9c34-aa430128e234 | -3.9506 | -49.75712 | 2024-11-16 04:50:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6544f559-f70f-3585-b237-fb041f76db54 | -3.24157 | -53.51786 | 2024-11-16 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0a5277d-f8a8-3f63-aceb-e9642f0f92a6 | -4.81139 | -42.91953 | 2024-11-16 04:50:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 615cd5e7-5b6f-3e76-a9af-121920d781a0 | -3.52808 | -50.78906 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de4cff18-8249-3cc7-b06d-29dad8a1c590 | -5.34783 | -45.57117 | 2024-11-16 04:50:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16c680f9-9e51-3dfb-8371-70545a031194 | -4.21554 | -47.22021 | 2024-11-16 04:50:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd7ca89a-3b23-310c-9e83-f9650d4a512c | -4.29945 | -48.07079 | 2024-11-16 04:50:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc135467-7691-3516-9690-0c80f1b7da38 | -4.37543 | -50.71856 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd30cb58-211f-3545-89b0-972899b1e3d1 | -9.12008 | -44.42484 | 2024-11-16 04:50:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7200e04f-3af4-3326-aeca-88d6a94c3f4f | -3.74015 | -50.18872 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0fabb35-f363-3a34-9674-5bf17b44042e | -4.36967 | -45.62116 | 2024-11-16 04:50:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcfccfbf-ecef-317b-9a08-ef06724be0fd | -3.23508 | -53.62455 | 2024-11-16 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bad5d33-d337-3bce-af70-7a0e6176717e | -4.28233 | -48.20895 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae53b10a-0883-3a4c-8d47-34adbbeb8861 | -3.56737 | -51.64668 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3120cf55-3fbb-3959-b67a-cff5059a8bf0 | -4.53695 | -43.5644 | 2024-11-16 04:50:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84cef002-abdc-3c12-8644-2be62c563330 | -8.28557 | -45.97471 | 2024-11-16 04:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7129d0d7-52b8-3162-8d10-a600818f7c9b | -4.21953 | -47.22083 | 2024-11-16 04:50:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a6ddae4f-0f0c-301c-b63c-16f901996285 | -3.74412 | -50.18556 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f27631fa-8cdb-3c60-a535-8827a26ff71a | -8.28491 | -45.97939 | 2024-11-16 04:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d5e4c1f-6611-3117-8ca0-bdbc6d4cb9ae | -4.72976 | -48.11623 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 72def8a7-f418-3ff3-9f03-6833ba34dc93 | -3.74356 | -50.18923 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af35bf1c-dca0-3042-bba9-721402feb020 | -3.56752 | -50.2375 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec648f4c-93c4-3e54-b014-404e87378405 | -5.15834 | -47.93657 | 2024-11-16 04:50:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54facfc8-2107-3514-9558-85a68625d69c | -4.29804 | -48.08007 | 2024-11-16 04:50:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16685bce-a530-3832-b554-3100ab8b9f62 | -2.96642 | -53.88155 | 2024-11-16 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13bdc969-ea37-3248-a696-03d3b1ba0825 | -4.21812 | -46.813 | 2024-11-16 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d82f3137-1459-3df3-aec4-179ecdb50bc7 | -3.57447 | -50.51213 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db6b3fb2-3619-3262-8eb8-8b9376d5c620 | -4.21901 | -47.22428 | 2024-11-16 04:50:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d9d58f4-08e7-3866-9fc3-e16ddee6f170 | -2.96078 | -54.16344 | 2024-11-16 04:50:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7aa8ca2-5a39-31d6-bb38-7c501fab8bc0 | -4.14966 | -50.77215 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e6decea-ae55-3c49-a306-681e659b74bf | -3.46559 | -51.62343 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db60cbcd-701c-3da9-a6f2-202b1b21c719 | -4.46236 | -50.65821 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa9b2d96-cdd4-359b-9108-7a6078f1372b | -8.28095 | -45.97401 | 2024-11-16 04:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9514110d-d3f9-39fb-807e-d441d7026660 | -5.79393 | -42.54066 | 2024-11-16 04:50:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 61da8966-ceda-3c27-b775-18f1d2e09db4 | -7.43861 | -46.93462 | 2024-11-16 04:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b1ee47f-8dc9-3599-b211-7aca2515480c | -3.24437 | -53.52205 | 2024-11-16 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4de62a7-ec9d-3a9f-acfb-4adb7fd96970 | -3.69253 | -50.10992 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4b48458-9b6f-30ad-ab23-b5f73943bc37 | -4.55106 | -45.75999 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9b7259f-a3f7-3120-8e3c-882528b0e011 | -4.90335 | -44.03341 | 2024-11-16 04:50:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2b8ec3a-6cde-31bd-9929-fe00d5aa96a5 | -6.16439 | -41.16005 | 2024-11-16 04:50:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7d4971ab-0f97-3a96-9e96-ad26fa11c2e6 | -4.21502 | -47.22367 | 2024-11-16 04:50:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00a8d61c-76ec-3050-b964-d64217bb0d9c | -3.69195 | -50.11361 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e359c07-e333-3a02-9a11-61030f99f9ad | -4.29832 | -48.10373 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac152d8b-297b-3cf2-873e-25da4b27148d | -5.23942 | -44.91236 | 2024-11-16 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cbbb526d-d934-37ea-af72-372d7f5891ee | -3.69311 | -50.10622 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1c3e2ef-07ee-3f69-8c6b-8a03298d637f | -3.81631 | -51.38116 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2e045c55-ea7e-37c8-a618-a57d72b3127a | -3.24099 | -53.52151 | 2024-11-16 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1043b9cd-4d8e-32f6-b260-bbedb2e6c4b4 | -5.79449 | -42.53675 | 2024-11-16 04:50:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13efde8e-3d37-3617-ba8a-b121ba5e8a7f | -10.54117 | -44.67852 | 2024-11-16 04:50:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69c30650-3fd9-3b1d-90fa-9a713df3d8c7 | -4.22491 | -50.67685 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a11b4aa3-e1a4-3edd-834a-3356d9bec2cd | -6.02541 | -48.03375 | 2024-11-16 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 05539805-fa4a-3bee-a0f3-7c5879b5f0ed | -4.22005 | -47.21736 | 2024-11-16 04:50:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0174e0bf-6eab-352f-98bf-1ad816160a14 | -3.89361 | -50.07904 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| addf5d33-65df-3600-92a9-87b62d33f437 | -5.90679 | -46.22754 | 2024-11-16 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea7c06ec-acef-3d3e-bc3f-335eedaa34df | -3.55959 | -50.24372 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ceb68a6-7e1d-31cf-93cd-2c26da4c50e7 | -3.54572 | -51.59042 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba6ce75a-5e18-3a9b-9506-142c5b1ddf72 | -6.64155 | -47.34487 | 2024-11-16 04:50:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6909c33a-482f-38e1-b734-13057a504a9f | -3.53101 | -51.64103 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 32c1be38-0800-36d0-8c24-a68915e4f390 | -4.37879 | -50.71908 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25734750-6c99-3a25-b759-0de98a9a4a33 | -4.26797 | -48.20214 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7f4eac0-95db-3905-8f03-1b9c2f6bf0b3 | -3.57091 | -50.23804 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f04c9636-18bc-3d1d-b30d-f4d316799dd7 | -3.58572 | -50.52855 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7396803-f5e4-333b-aa41-bc1e0958bf95 | -3.56694 | -50.24115 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdcfc5f0-8829-35e3-ac0c-027bfda8eb46 | -3.6095 | -52.22347 | 2024-11-16 04:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c70f1eba-18a5-3070-855b-9e245e5e318c | -4.13409 | -49.36711 | 2024-11-16 04:50:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a867289-9ce3-3617-897f-7891b35834da | -5.69904 | -45.67303 | 2024-11-16 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 301d7176-25f7-3225-bc94-4d71b0e5994c | -6.8227 | -46.77873 | 2024-11-16 04:50:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 867a9eaf-7911-3a27-871a-7ef400383717 | -3.5377 | -51.49033 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c64efc2d-3c19-3a11-b4e8-d99487de6c9d | -4.36368 | -50.81553 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3e9315c-7ba9-33bb-878f-1ebdec41c324 | -4.9157 | -44.78524 | 2024-11-16 04:50:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 474a3854-beb3-33a6-8b97-227bf3e35009 | -3.57502 | -50.50854 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4244bb30-8faa-3312-91f1-f294253e01b6 | -4.98943 | -44.31769 | 2024-11-16 04:50:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| afe0202a-6fe5-3e11-a8f5-612102ea4bc2 | -4.55203 | -48.01388 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bd06f902-3b51-3f62-8372-a2e86ada13d4 | -3.88458 | -49.9786 | 2024-11-16 04:50:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 187d02e5-eed1-35e5-b7c4-6aea6469737b | -3.57034 | -50.24168 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2ad1353-1541-3ca3-bc49-e7884f78584c | -8.27635 | -45.97324 | 2024-11-16 04:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02282720-9e54-3227-87f3-1dc3d201d753 | -6.43985 | -47.86121 | 2024-11-16 04:50:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 42bd8469-a5f6-3ba0-a460-46dc59a13940 | -3.54518 | -51.59387 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9faafb35-f789-39f6-a4bc-ad7bcd2c27b0 | -4.9088 | -44.03115 | 2024-11-16 04:50:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ac9afd3-3daf-34a7-b238-6317904641cf | -4.13293 | -47.23877 | 2024-11-16 04:50:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b79fd6f-372a-3ae8-a063-f6a7911cc89c | -3.54101 | -51.49084 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8907879a-2937-31c0-a891-523aedd87ed2 | -3.71575 | -51.8493 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e520ca9-96fe-3fca-8187-99f32b478b10 | -3.76427 | -52.14557 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d803580a-8699-3702-b5b8-1f7fa740fe80 | -3.71959 | -51.84638 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c7f1975-7007-3115-9761-95edee6a4d48 | -4.99436 | -44.3184 | 2024-11-16 04:50:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8e11f575-dd5c-306d-bff6-589250fa5055 | -3.53965 | -51.58595 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f972915-1a8a-3fdd-aa6d-f59b7139e5a5 | -3.52753 | -50.79259 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README51.md)
