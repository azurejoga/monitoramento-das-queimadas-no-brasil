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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ecd742d-648e-35db-b150-5445a45afa59 | -6.2253 | -43.55429 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d76c931d-c50b-36c2-8f57-7e49410ea8ca | -5.53524 | -46.42957 | 2025-09-04 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4cceade-9e27-3741-aae4-ecfda9c7b43a | -6.73465 | -42.26625 | 2025-09-04 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| beb9a3e0-832b-36c0-a906-0f6ac7b895ac | -4.78406 | -43.82268 | 2025-09-04 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42f2f217-642f-3004-b81c-5fa1b8465755 | -6.24627 | -45.0471 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a8858f9-f3a4-33ed-a0ae-54a1ed209d4a | -5.97638 | -44.12339 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2e12c79a-a5d4-31a3-86bf-a7de2c16f949 | -6.0846 | -43.284 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8219fbf3-bafb-3177-8521-26f30bf0db7c | -6.05231 | -45.02784 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89f24f5d-3ce8-3a3f-8923-0e6b589b6c0c | -5.69919 | -45.39986 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 721bc87d-a47d-351a-86c3-59413536de71 | -5.87371 | -46.11605 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b2543dd-d223-3236-bbe4-46f8d026c642 | -7.7595 | -43.96805 | 2025-09-04 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a36f8162-2079-3847-b93c-3fdd63224be2 | -5.94475 | -43.03942 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1a599b44-cc0e-38bd-979c-23277ff6677e | -6.79306 | -44.44823 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6c527d6d-c940-3860-ba5e-e3da2599787b | -5.12669 | -41.03993 | 2025-09-04 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b910c406-9371-34f6-a3ac-04c5b0e1a393 | -6.37959 | -43.53835 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 658db743-3769-3b0b-b0c8-70beba4f7034 | -6.54102 | -43.91056 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2f87a78-3c4b-325a-b729-1af1128c99f0 | -6.26839 | -44.50792 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 145c8c70-071e-3bf9-9195-8fe7e6cf967b | -6.67729 | -48.40394 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 492910c1-2320-3cba-9f53-ec6b5ba947e1 | -4.90377 | -41.76352 | 2025-09-04 04:25:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f1ed14c5-7bb9-3cd1-a4d0-7dbf47ec87a5 | -6.03437 | -46.0004 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19c3eb65-b8ed-35aa-a239-93c985444f38 | -4.16241 | -48.77653 | 2025-09-04 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f29a343-555d-3745-a6eb-8508d1e294e4 | -6.79193 | -44.45573 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eedb1fbf-c394-3827-b6e5-e03dd6103004 | -5.8816 | -43.23897 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1e432cb2-4249-3000-87e4-bde5ffd8f39e | -5.74835 | -45.5437 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09c2bcb2-a286-3b67-9f45-968b99d7b477 | -5.70172 | -45.16288 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 429f4dd8-5d49-39f6-9939-f6cc14964196 | -8.05631 | -44.13663 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fe92695-7d69-3061-814d-74079f70eecb | -6.69493 | -48.40309 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3850d5c-daff-3406-bf7a-e191ce647887 | -7.55358 | -45.7205 | 2025-09-04 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47d903a3-177d-31e9-8ced-cc7d8fa88c70 | -6.8719 | -45.57884 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 83b05471-b220-34d4-b133-4d1196c3ce50 | -8.02941 | -44.07543 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1822bf25-097b-3cbc-8c27-889c48987832 | -6.27821 | -43.849 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e73f8827-32cc-3f5e-a6ae-708292b375e6 | -8.0306 | -44.06736 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4135181b-65e9-33d3-a131-6b35f478bf76 | -6.79424 | -44.48677 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d06e6d7-b99f-3756-bfaa-06a92fac9a53 | -7.93286 | -44.93096 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f966fecf-414b-36d2-8b30-4f72f1301b9f | -5.5632 | -45.57521 | 2025-09-04 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 956c813a-7f6b-3e77-9793-e3feac8eb827 | -5.03368 | -42.47719 | 2025-09-04 04:25:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 268f8c3a-c476-3980-baea-e4fed3fdc12c | -5.38938 | -45.9483 | 2025-09-04 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61131b45-1274-34e0-91a1-24247a85cf2b | -6.29673 | -43.3174 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b4e8547-826c-3c74-8724-baeafb172a45 | -6.0573 | -43.41829 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf9b3e20-1320-38a6-b38d-347282c170bd | -6.23128 | -43.53895 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cd38d93-cbcf-37a1-9c30-6153af470bec | -6.26603 | -43.59641 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db2fd709-8ad4-394c-8d56-bca842f94ca7 | -8.02288 | -44.14377 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d441e9a3-83ee-385a-a09f-2bb5874362a8 | -7.80364 | -46.08288 | 2025-09-04 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df754405-21a1-3a1c-b255-2730aacf5b96 | -5.49794 | -45.27213 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 949bab63-755e-3eb8-ba87-488f3fc02663 | -6.49745 | -44.08219 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f531c825-3325-3782-a781-0de4ea423c94 | -8.07388 | -42.95317 | 2025-09-04 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48da180f-2df4-3ffd-a139-be1422f14601 | -6.68793 | -43.87136 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25db4685-70be-3c1f-b51f-112737b81897 | -6.88748 | -44.24544 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce269379-393c-39f0-b185-d692cd0e8b5b | -6.19191 | -44.18212 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 062a9378-9147-3d05-a232-3d1697052674 | -7.41368 | -42.04617 | 2025-09-04 04:25:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f2d7b07d-2bc3-318b-8fdd-d046a15aaca1 | -6.25802 | -43.29195 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7d392b5-be08-32c5-bb51-d40a5034e1ba | -6.82923 | -44.27912 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c6ddb66-3b9c-369f-b16d-b95478cfefc9 | -5.61068 | -45.02576 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6642a85-4262-3b7f-84e5-0d3a631ab05a | -5.52041 | -42.64889 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cdaa952e-04f5-3559-b2fc-2ceceaff62e8 | -6.34279 | -47.56803 | 2025-09-04 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf66ff9a-11ca-3e6a-8c44-af4b564c2f0e | -4.69189 | -43.65327 | 2025-09-04 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01876d57-042a-3eb7-9dcf-70b8a5b1a72b | -6.85859 | -44.27222 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31e6ee5f-e98d-3cab-94a7-21e74a3865ee | -6.05176 | -45.03142 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a08a2ac-8f46-3b3f-9771-ae25e54b6b01 | -6.22236 | -43.54976 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdb4d3e5-7219-33fe-a8e0-0fdbe99cb32a | -5.00399 | -56.2568 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 12365c27-deab-304b-b2a1-4bb63cb2e4b8 | -7.93402 | -44.94624 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2f424af-e788-3a66-9105-981c52156261 | -7.61298 | -46.21713 | 2025-09-04 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19cc37b1-5a7e-3acc-8920-cfdc8a3eae84 | -3.15975 | -48.60654 | 2025-09-04 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31311ba9-4fe4-3647-b9de-527e68eafb1b | -6.22712 | -43.54241 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 208655d9-286c-3773-b650-1e58646afc91 | -5.77934 | -45.25462 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00b7f27d-d278-33b2-adfa-4cb3435105d7 | -6.36479 | -45.62578 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3139f183-ceee-35c5-bdcb-22f24defc2ba | -6.57161 | -48.64531 | 2025-09-04 04:25:00 | NOAA-21 | ARAGUANÃ | TOCANTINS | Brasil | 1702158 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7dc9bbb-a801-319a-8058-2cd1ec82b223 | -5.98277 | -43.82131 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 831d08b6-b5cd-3314-9baa-27e24a8c7322 | -6.17703 | -47.28203 | 2025-09-04 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a73e66c-8fa2-38de-8f99-d13316111581 | -6.54494 | -42.95424 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e24668fd-63df-3a84-85a6-7f3456a66e07 | -7.81724 | -40.17011 | 2025-09-04 04:25:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 128918f3-1028-383f-bbc8-f8c285d0d701 | -5.51607 | -42.65271 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e8e08be2-bf19-3b28-bcb8-566c5924dcb0 | -6.50431 | -43.57659 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf90b007-af50-3fae-b6a5-9c42a7ff10cc | -6.12293 | -42.95029 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| a9a5e345-36c9-3c68-9f36-d63937ce8759 | -5.70614 | -45.15635 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| be5d8fae-3611-3ffc-ae47-c5052e0a7ecd | -7.17669 | -44.92237 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c77896af-aafd-3da5-973c-8196c9e0a246 | -7.72732 | -44.62098 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91b2813e-90d8-337f-b707-13fcd6b9aa97 | -6.26491 | -43.57969 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17da4bc4-da24-3cd7-b911-3da512be58d3 | -4.51745 | -41.96726 | 2025-09-04 04:25:00 | NOAA-21 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0698f00b-5b24-3e8a-99d2-5f09500729e6 | -5.99839 | -44.98343 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca74f20b-e7c5-3fbe-a486-854e44787aa4 | -6.03055 | -46.67788 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 656b6e52-36d8-32bb-be84-eb58c1506044 | -5.79948 | -45.62994 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 055b403a-c123-350a-86e7-760301e969da | -7.48373 | -44.7955 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b438db4c-7421-38ab-b955-0a630779a8b6 | -6.50076 | -43.57607 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| befca025-b91e-3487-89c2-f4b7948f594d | -5.88333 | -43.25188 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57ed7013-90c8-3506-9b02-ac716bf564d8 | -6.83955 | -46.39955 | 2025-09-04 04:25:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4acb88f1-cc63-31ae-b78d-0439b820eb59 | -5.93213 | -43.02462 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ce4a1f5e-37f2-3e68-8a43-fc5a5c2f8de8 | -6.66026 | -43.95952 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66c6760f-bba8-3787-875f-007bca0afe82 | -6.0888 | -43.28044 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 82119b80-2bf4-38c9-92c7-5bec41c6fef0 | -5.67197 | -43.67258 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e11492fb-db91-31d9-8ce5-3b92b675146a | -6.98767 | -46.10442 | 2025-09-04 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e08a8c07-ecd2-3939-857d-aeedd6248225 | -6.88689 | -44.24927 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1515d205-2aa9-3b24-b106-840b57b7e9ec | -6.55165 | -42.95967 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff9d6a03-7cbc-345f-8d9a-c86aa57630c7 | -7.62685 | -42.64478 | 2025-09-04 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d81ff634-06f1-3200-9893-8c4a09ffc89e | -8.02233 | -44.12322 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1cc8d334-44df-3fab-a06a-40e2e32a9cab | -3.22714 | -47.12843 | 2025-09-04 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1751a126-801c-3871-a5c0-e440ca8f51e3 | -6.41336 | -43.26236 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0821627a-9d44-3a5e-a6e7-167bc1fe2c48 | -6.02666 | -46.65959 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c19ac2f7-3688-31c7-b21c-3b1f21166f90 | -5.3817 | -45.95417 | 2025-09-04 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24ea55cd-1203-34a1-aa26-8c39b953666f | -6.73991 | -42.2573 | 2025-09-04 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README30.md)
