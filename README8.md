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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ace8ce05-4ba5-3a01-b91c-484534609355 | -3.64322 | -45.74807 | 2025-12-14 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e295e1a-1913-312f-8ea4-8cfe4f3727ab | -4.86557 | -50.82656 | 2025-12-14 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77457913-1ac5-306c-a3fd-daf0e298513c | -4.62334 | -44.87226 | 2025-12-14 04:31:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35359f47-0e3e-3b32-a74a-1e09b1084030 | -1.93103 | -46.43259 | 2025-12-14 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89f6b834-0c8f-3a67-8278-cee678d18039 | -4.69515 | -43.24875 | 2025-12-14 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f06913f-e2f6-3c29-8595-475c1f20a57d | -1.7843 | -54.15209 | 2025-12-14 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25259b37-d007-3476-9e7c-d0f157cede56 | -4.17512 | -46.00258 | 2025-12-14 04:31:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7271363d-272e-38de-874b-784d5c3dc375 | -4.39991 | -43.68451 | 2025-12-14 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ce425a1-7457-3fe9-9b11-333b0e002734 | -2.85182 | -45.39769 | 2025-12-14 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f1ed956-b79e-3d54-be6d-858a29b08d93 | -5.68712 | -46.57413 | 2025-12-14 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85607aaf-64e1-3224-acd2-d8e422d60dfd | -3.14402 | -45.37076 | 2025-12-14 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 153f6f42-9f16-3c27-9677-166cc8bfdb48 | -3.2808 | -45.57814 | 2025-12-14 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a9f0eb4-8efc-3240-b08c-1ae492578603 | -6.12944 | -46.14429 | 2025-12-14 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34e30f25-6fa4-3379-a411-71cb20d2c1ba | -2.25004 | -53.67963 | 2025-12-14 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 90bd7e40-ddd5-3587-9400-fa3d48b5d05f | -3.88259 | -42.51697 | 2025-12-14 04:31:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 89fc0c39-294f-3f14-a4c7-473b4e6291b7 | -4.33999 | -40.27636 | 2025-12-14 04:31:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b2376b9a-41c4-3f24-909b-142c69579b6e | -3.82131 | -44.38546 | 2025-12-14 04:31:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90172985-921e-3619-a47b-53ec234ac160 | -5.98714 | -44.59302 | 2025-12-14 04:31:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74d64de2-1f46-3fc4-8ebc-759a2be735f0 | -1.88061 | -54.68714 | 2025-12-14 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efa1cb14-1ca8-3a4a-8520-1a859d72d1b7 | -2.6653 | -46.89351 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3959456e-8e8a-30ae-88a2-ccd2c3855085 | -1.52391 | -45.68528 | 2025-12-14 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 86d2b88f-64b7-3133-8754-e7a9f25f66c5 | -2.21699 | -45.691 | 2025-12-14 04:31:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 320d0613-4f4b-326a-b297-a7b327b945c6 | -4.9337 | -43.95775 | 2025-12-14 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 771315cf-dc51-366a-8e18-ea67fc965bc2 | -5.66933 | -39.26707 | 2025-12-14 04:31:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dfab4747-6ee9-30d0-9223-e6e130848260 | -4.17718 | -45.67714 | 2025-12-14 04:31:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8cc1fb6-2e67-31bb-a4e0-830ec01d2fec | -2.91774 | -45.224 | 2025-12-14 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9210b3bb-e598-3d8c-833e-d5124c5a5d2d | -2.84093 | -46.72692 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2119c835-a660-344d-a9e2-9d1c83f82aec | -2.28184 | -45.58436 | 2025-12-14 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 173cd1e3-b2f9-3fdc-897a-e794e3c7c991 | -1.41381 | -46.23885 | 2025-12-14 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 162ab986-343f-3607-b31f-b2add2766153 | -4.34704 | -42.1932 | 2025-12-14 04:31:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ef037c3-11db-3065-aa3c-a2adca74f9cb | -5.28951 | -50.94219 | 2025-12-14 04:31:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0eacaab-b929-3181-8c11-8de7412112ad | -3.17025 | -54.97402 | 2025-12-14 04:31:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0c1087f-2fcd-31c9-9656-a145beeacd22 | -3.53617 | -53.02256 | 2025-12-14 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bdbe449-2773-3cb4-ab58-f02661d45d04 | -5.00682 | -42.77562 | 2025-12-14 04:31:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c338989-18f2-33b2-b5ed-03a3cb9fb287 | -3.77393 | -42.10169 | 2025-12-14 04:31:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 518ff80c-e9d6-34c6-8828-6e020568dd71 | -2.11727 | -54.21859 | 2025-12-14 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82998e71-052d-3594-b8b5-f2f28d33e7ac | -2.28672 | -45.58838 | 2025-12-14 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ea3c1d3-b40c-33cc-b364-e112bb49c5aa | -5.39814 | -44.67929 | 2025-12-14 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abadbe7f-2167-3e9a-a315-c05c0ad0bed0 | -1.87319 | -52.60265 | 2025-12-14 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ba6d0fe-1655-33b4-acc5-22280f93df42 | -3.51685 | -52.18983 | 2025-12-14 04:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d03ce40-da8d-3523-8318-f9a430784266 | -5.94434 | -44.45681 | 2025-12-14 04:31:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| abbc60ef-c138-359d-9c24-712f69222d80 | -4.34247 | -43.63472 | 2025-12-14 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7612693d-36cc-315f-82ab-939a59614407 | -10.36798 | -48.89589 | 2025-12-14 04:33:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f7668be-a752-356c-8f87-2c6f1911e1c6 | -8.03892 | -43.09324 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| a536c0ab-dc03-395f-9518-99e969f6ede2 | -8.0384 | -43.09687 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7912dc85-2d02-3a6c-a614-1114eda5b5bd | -9.87107 | -50.56591 | 2025-12-14 04:33:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92e747c0-eadf-38ae-a293-3f9d35a50ed6 | -7.21784 | -43.11085 | 2025-12-14 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 019cead1-90c7-318d-b1e6-19c2c765f23b | -8.04247 | -43.0974 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a04934e7-d3ca-336d-b0ef-1e6706b8301b | -10.54054 | -47.74106 | 2025-12-14 04:33:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 115af28c-beae-390b-8191-daf67b07387f | -11.0901 | -48.25329 | 2025-12-14 04:33:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b55f4a1-50a0-35c3-a3c5-0a13ddfb88bd | -13.06256 | -50.28863 | 2025-12-14 04:33:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f230c94c-db8a-3f19-8446-7e693e6370bb | -8.07633 | -43.15393 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bebf33c7-af1d-3809-9cd1-c83111be5754 | -9.86765 | -50.56535 | 2025-12-14 04:33:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb9ff1f9-8d47-3b17-a62d-196e66371403 | -8.02974 | -43.09931 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 548c9058-fad9-3df4-ba1b-f4bcea358344 | -8.07167 | -43.15326 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2b78b56c-de7c-3c17-94f8-ed6720f3a7a8 | -10.76892 | -44.93821 | 2025-12-14 04:33:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9a0c79b-ab31-33cd-a9b1-4c9e3b87cd13 | -8.03433 | -43.09629 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f934696a-73c2-399a-a009-130142c2fd43 | -10.5536 | -51.6828 | 2025-12-14 04:33:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3e400d3-cc87-382c-82ad-fc7dd86dab95 | -6.71463 | -47.79262 | 2025-12-14 04:33:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ba179bc-1554-3107-8ccc-f94ebc0e633d | -6.59639 | -46.93586 | 2025-12-14 04:33:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9f0f569-4811-37fb-95ff-a333cbac4f43 | -8.07683 | -43.15034 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 02c1d731-248b-3cb9-bb14-f4193d7374c3 | -7.1442 | -44.91079 | 2025-12-14 04:33:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d550739-fc8e-38a2-b55c-259764e09128 | -8.03787 | -43.1005 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 68772485-d6c8-3d5a-9397-5c6d73680842 | -10.36442 | -48.8953 | 2025-12-14 04:33:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ebecb8e-ce8b-3cb4-8d37-2f98cac3e144 | -8.03485 | -43.09267 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ffa5b721-6e89-3e5c-ace5-7699dd3570b4 | -12.20733 | -49.5471 | 2025-12-14 04:33:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6d6de0c-d33c-3aec-a0a7-e5bcbb69b8a9 | -8.03026 | -43.0957 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a3c74ddd-8db1-31f2-9eef-38e8b0907563 | -8.06763 | -43.1526 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| be1ff54f-c474-3406-90d6-2a01e96a9aa5 | -6.71133 | -47.7921 | 2025-12-14 04:33:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88e116f8-ca57-3b78-8ac8-70382a0ed0e4 | -11.09342 | -48.25381 | 2025-12-14 04:33:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 434a33be-fb38-3b24-816a-671ef85243ab | -7.21621 | -43.11135 | 2025-12-14 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 729022b8-ed87-37ae-8d5e-093c12705f14 | -10.76515 | -44.93766 | 2025-12-14 04:33:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f85c0f60-c295-326c-ac0a-66f2845041dc | -8.07572 | -43.1539 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 708a6769-5910-3c63-ba05-94b74ef0dc91 | -8.03381 | -43.09991 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0244b68e-749b-3486-a45c-3c9cb28d1218 | -8.07625 | -43.15031 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 055b8feb-97a0-322b-abec-c17e5972030e | -8.0722 | -43.14966 | 2025-12-14 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ee016e95-67ce-3dbb-a3a8-d70ce625c919 | -11.08955 | -48.25683 | 2025-12-14 04:33:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca66e66a-46ef-33b6-92ea-e8fc74ac5463 | -18.34278 | -54.54348 | 2025-12-14 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e2b2c0b-4cd7-3277-b3b5-06bb79b9f283 | -27.56774 | -49.97374 | 2025-12-14 04:38:00 | NOAA-21 | OTACÍLIO COSTA | SANTA CATARINA | Brasil | 4211751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 01a8a591-92e2-3c29-bbd4-ae36b9660b5f | -28.97248 | -52.43671 | 2025-12-14 04:40:00 | NOAA-21 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d7cb7409-27f8-33eb-88da-f7e30437c287 | -29.00537 | -56.34046 | 2025-12-14 04:40:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 35cd6a28-5ae4-35ae-a2e6-cc7e0a7b3470 | -29.67543 | -53.81287 | 2025-12-14 04:40:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 265672f5-f08c-3595-8b9b-2c6706521365 | -28.97581 | -52.43736 | 2025-12-14 04:40:00 | NOAA-21 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a6f1e10f-c4c7-36b3-8989-7e5804f811f3 | 2.87716 | -60.25974 | 2025-12-14 04:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d846995-8efe-38ef-bbfa-893868d2fdbb | 2.87734 | -60.26228 | 2025-12-14 04:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4055082c-2c5e-358b-a995-15727f133f51 | -0.93443 | -46.89609 | 2025-12-14 04:59:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 08e8a448-b8be-3b79-aadd-3b48a9620f3b | -2.28413 | -53.71526 | 2025-12-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b95eca5-fbd1-31eb-943b-da11a57d5ee6 | -4.69324 | -43.25291 | 2025-12-14 05:01:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28a78d67-017c-3388-8b2b-1e5725c839c5 | -1.02719 | -53.55273 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60f97d30-7c70-3d19-8f2b-75f485bf2532 | -1.02386 | -53.55221 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02b28963-ecf4-3289-bbf8-b2d7e6adcc73 | -2.6641 | -46.89416 | 2025-12-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 711e03cd-4f55-32b3-a484-e79408f98905 | -3.51635 | -52.18614 | 2025-12-14 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3e6436b-b76b-325c-9500-81df9ada2f3d | -1.92159 | -54.40469 | 2025-12-14 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a71c7fff-290a-38c9-a011-991c627736e2 | -1.02332 | -53.55566 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| baafe57c-8e16-39f4-adb4-3e19d3655177 | -4.33804 | -43.6382 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d76390d2-1d68-351c-aa4b-f2996886eff6 | -2.21465 | -45.69341 | 2025-12-14 05:01:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c018384d-3f95-30b3-9a9d-58b4c9277257 | -4.68998 | -43.25074 | 2025-12-14 05:01:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2570a6e5-a05f-3fa6-bbeb-c2de13209011 | -3.3023 | -52.58681 | 2025-12-14 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 466bc1ff-cf8a-38de-8725-c4b852033d97 | -4.68936 | -43.25505 | 2025-12-14 05:01:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d01b8d12-ae58-32cc-b689-a6664748cd09 | -1.02664 | -53.55618 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README9.md)
