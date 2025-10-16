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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f13efbc4-cb4b-3788-b31e-d269cd6c82b3 | -5.41179 | -40.91357 | 2025-10-16 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| baeeb3c9-243d-31ff-9821-458c6d91ac8c | -4.72331 | -46.15833 | 2025-10-16 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0f8121dd-70d8-3066-9408-3b13656c5b6c | -7.39699 | -39.69159 | 2025-10-16 04:38:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 51.0 |
| 9f29cb43-a8b7-39cb-9bdb-cce0cf730edf | -8.19211 | -43.31837 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 197495bf-03a9-31fd-994a-f0d5ad5e4eea | -7.56004 | -43.91272 | 2025-10-16 04:38:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1f45090-c3ce-315a-abba-16d5af2c51c9 | -4.56643 | -44.00706 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfd7f638-0ac4-3566-9f7d-a5e347f12cb4 | -4.39258 | -43.38464 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96acccb5-27a2-34e6-8f02-7aa5491f65e6 | -4.82837 | -45.65709 | 2025-10-16 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79486268-9bfb-339b-9501-c0a0443d71e9 | -5.41432 | -45.64536 | 2025-10-16 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e802b891-678a-3613-8309-0f533c97fee4 | -8.22123 | -44.00424 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66593af4-4029-3440-9b65-026f5d87405b | -7.03543 | -41.81348 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 781514e4-abbc-35c1-af9a-8f0a5c823667 | -5.7292 | -41.31905 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8ed782b8-e53c-3acf-bf4f-e6cb8bb8c80d | -4.28725 | -48.57889 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d22edcd6-9251-3cfa-b856-1c8682272a69 | -6.57432 | -42.96027 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca9d4b6b-e74d-3f69-ac08-b742e249f406 | -5.96944 | -42.88379 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 07da223d-3130-3eb8-9117-93745aa4678a | -3.01185 | -45.38399 | 2025-10-16 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4bc73b6f-aa3b-3a56-955a-0ddbf1c01b64 | -1.11341 | -54.06368 | 2025-10-16 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4d00a7e-5e0a-345a-8100-adf0ab69a8cd | -5.2534 | -41.0215 | 2025-10-16 04:38:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 33f56491-8807-301f-b990-059a00709601 | -8.25231 | -43.34079 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7f84c334-7214-34b4-84cd-904b7213cedd | -6.56926 | -42.96408 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 271dfe1d-5b06-30b3-ac4a-7d8d2ed44eff | -7.19028 | -42.3624 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2645302f-3db4-3819-ba09-2d9f5e04177c | -6.2244 | -44.5954 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 972a3a07-3592-3681-983f-a747197f93f3 | -4.49987 | -45.40031 | 2025-10-16 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3e2cc9d-c9cc-362b-bb00-2b743f9456f8 | -6.46885 | -41.84155 | 2025-10-16 04:38:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 02f03bdb-951d-3577-b319-a511cc792e02 | -8.25187 | -43.33816 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9600638f-2f2a-3891-92f2-bf5bf9f5d692 | -6.55067 | -43.91725 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eba526fa-3cdf-3799-b96b-8f4800848fd1 | -2.71008 | -49.86441 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 75599193-bd87-3ae3-9c2e-6091edba6add | -7.41212 | -44.7497 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5f872b5-110d-3ce5-9980-19838da8a894 | -3.55756 | -50.12394 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fc5b8d6-6185-3259-bdcd-017e82b3d577 | -8.07049 | -45.42087 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b805320-c5b2-3731-9153-41e3807cca27 | -4.42023 | -42.88177 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1349721-7482-3f2e-92ac-03ea69d314f4 | -7.58093 | -42.6918 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e75a70a1-82cf-3061-92ea-5c5872469764 | -6.16079 | -40.89999 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d5d8b6b7-75b2-39b8-8c34-fdcc7280b17b | -5.3247 | -44.8341 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd28eca9-d9a9-39a2-9d56-2bf4a6356862 | -7.10142 | -41.52425 | 2025-10-16 04:38:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c5b797d5-c754-324d-b32a-85a33fab1f9d | -2.44779 | -49.3702 | 2025-10-16 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3b889555-c894-307d-b0e0-e2b921990fd8 | -5.32663 | -43.94157 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f193b6d-a6ab-37b0-b0a9-378127731a25 | -6.22803 | -55.63467 | 2025-10-16 04:38:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f646371-9ac1-310a-8e26-474b3b669298 | -4.39145 | -43.39228 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 1c032b65-e192-32e2-bf1b-70a0fefd6c46 | -7.24457 | -49.51807 | 2025-10-16 04:38:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e821afd9-2de0-3cc0-b0dd-33bc8783adca | -5.65024 | -45.96818 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1905b47-b144-3db5-b25b-d50f38a394ba | -7.06 | -45.05375 | 2025-10-16 04:38:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c7dd57a-1ce2-3160-b1eb-d6e1678911c1 | -6.06854 | -44.30901 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a9579cd-8207-3594-96ac-a3704ceb78f1 | -5.6286 | -43.92581 | 2025-10-16 04:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72fb1866-70e6-3ffc-a573-87bc897f14a9 | -6.45154 | -43.38309 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9745ad5b-2834-3c17-8431-ef6af2602c13 | -2.87705 | -50.73456 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02169bd7-b300-3746-b0f1-3d8c0a2b5b00 | -4.84624 | -48.77255 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f1c9414-2bfb-35a3-8950-f028b283bf8d | -5.14716 | -45.21163 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aca435a8-5a6b-3ce9-af4b-6b49c761fab4 | -5.88205 | -43.8749 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c12c7516-f254-3d32-8ca2-cd698b865ef7 | -6.56411 | -42.97478 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 760f9ba6-a5ad-3636-aa70-b8f053913201 | -6.05129 | -44.24904 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3a4984f-d4a2-3bb9-8af1-83d528efdc15 | -4.67733 | -44.09937 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edb72584-dfb9-383d-9bab-b49571dba49b | -3.07677 | -49.5048 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae01f629-3693-3789-afa5-b7872a7910aa | -8.25007 | -44.13295 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db2601a3-21d7-3d67-9240-64be028d188b | -6.71926 | -47.79346 | 2025-10-16 04:38:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c9fcf10-dffc-3789-90ae-a1e0ac77518c | -6.26039 | -42.89697 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8309eb2c-2a6f-3372-9dcc-5c1b28bd5bd0 | -6.40789 | -45.35903 | 2025-10-16 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cdfc368-487e-3cc1-9bbb-ae6afc355f25 | -6.33342 | -45.49839 | 2025-10-16 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb4b0c24-dbce-35fa-9078-3226ad0f5719 | -5.34388 | -43.74093 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d0bf3fc-157b-3d82-87ea-26abe9225e35 | -6.07397 | -47.12642 | 2025-10-16 04:38:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 788a67a0-a75a-3941-ba6e-417a384cf867 | -3.68646 | -47.63095 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b1248a0a-d880-32af-9fd4-dbaf9cb2adae | -3.45692 | -50.09372 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58bbe192-94df-3410-80e2-94bb98fc7f87 | -2.27083 | -47.19213 | 2025-10-16 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 598f59ea-6b93-3347-b633-66e3b989dafe | -3.68536 | -47.63799 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cacc0193-bd2c-3f8b-a982-8a03089dc6e9 | -4.84954 | -48.77306 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a371931-2af9-361a-9edb-bbb01973dd73 | -6.36793 | -41.49164 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e8ccaba0-1564-31d3-87ef-7a064b9e5f0b | -4.28396 | -48.57838 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ec48f94-82e5-37fb-b33f-067799be5199 | -7.95059 | -44.14704 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1533e542-a7cf-3983-972f-da0b80fc4af1 | -6.30326 | -44.12399 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa36ade6-7f47-3433-a466-c0db883cd12f | -4.35969 | -46.77749 | 2025-10-16 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c750764-31f2-3c7c-b1a7-0cf8860335ad | -6.45211 | -43.37913 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30ebebc2-001b-3602-8007-152b8e0fa03b | -7.95113 | -44.14317 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bc467cc7-487d-3541-9e2e-2ac9af13d5cd | -3.48258 | -52.85837 | 2025-10-16 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 037b1be0-74a5-3dbe-ab7a-1e25ac42c695 | -7.94774 | -43.26442 | 2025-10-16 04:38:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 37d33c34-2dca-328c-b361-b89d8c1d4fb0 | -4.94137 | -48.63922 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d68d4163-8db0-3e16-9895-4ba2bcc94db8 | -5.32378 | -42.9003 | 2025-10-16 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 82ee07e1-e7ad-3488-a623-ae56ae4942f6 | -6.59878 | -43.92202 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b05b258d-56b1-3cef-842d-95d4bcc8a4b2 | -3.47152 | -50.02333 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc441a66-80e4-37eb-9d41-947ff8ed35cc | -5.87657 | -43.8549 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95ba8657-33e3-3e58-a7bb-9c092c31f435 | -6.91279 | -44.08148 | 2025-10-16 04:38:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95a832c8-e3fd-3961-ae08-4dd3c25961e7 | -7.09882 | -45.27307 | 2025-10-16 04:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc272ea9-df93-3c79-b347-6b2ffb23fea1 | -6.10198 | -40.88556 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c69003ad-a5b4-3a44-81a2-12cccbba68d0 | -6.31446 | -44.71662 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e8a4789-4a47-3194-ab3d-a506950bd76c | -3.66698 | -50.27302 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2153d51a-6582-35d4-909b-2897cacca022 | -5.53311 | -41.32698 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5e47b8f6-67ea-3703-b3bc-86669036d04b | -3.83983 | -50.97512 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1441b13-ef82-33ea-8185-ec632ae8b16e | -2.87479 | -50.72655 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31d3ceca-090f-33d4-a7e3-68cb01ed0818 | -7.41161 | -44.75327 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3cea8ab-6900-3e7d-bdbc-c3bc812d8be6 | -5.31609 | -44.24412 | 2025-10-16 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33c2ca09-f6e5-37ce-91e4-e45f81f66e94 | -5.88598 | -42.77652 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e200dff8-2e8c-3384-9fa6-824d7482cde7 | -7.53789 | -42.06776 | 2025-10-16 04:38:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d8a35e0-68a1-36c3-976c-72f471938c1e | -5.68355 | -48.96746 | 2025-10-16 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5a8ba07-6316-3604-8e9a-afcc1f4850cd | -4.76248 | -40.87044 | 2025-10-16 04:38:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| afcf3b7d-b677-31ee-8b1d-a83347098b23 | -6.39192 | -41.48058 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c50567a4-ed37-354f-97fb-5c4389c0e241 | -3.30637 | -50.16847 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f70f8d95-6edf-399f-892b-af81d6d7e042 | -7.24511 | -49.51462 | 2025-10-16 04:38:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| debb3c5d-a098-3167-b1b3-0bbb7ef66d68 | -2.4816 | -48.57202 | 2025-10-16 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19466fc1-f6af-3886-8d7a-4614519c247a | -6.52797 | -44.73743 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e3d10b8-1a45-324e-8043-98863dca6594 | -5.72083 | -44.52362 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f2c68c9-8576-31c7-9423-0a6d6eeec3e5 | -8.25348 | -44.10956 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README58.md)
