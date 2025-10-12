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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b67c8ae-a613-3512-a2fb-3f00600859d6 | -3.09577 | -47.01858 | 2025-10-12 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5576420-7729-3d39-abd3-0af15840ca23 | -3.41043 | -52.18216 | 2025-10-12 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed24aa1e-2317-3165-b0dc-55dd8bee0f8e | -7.42514 | -45.165 | 2025-10-12 05:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 199d0e86-e274-3b18-8fec-2cf94066d637 | -5.86316 | -42.86839 | 2025-10-12 05:01:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be591c4f-e8bc-3178-ac52-6c7964b586c8 | -7.26124 | -44.15122 | 2025-10-12 05:01:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d3d0259-fdfa-3f9f-a3a0-97f3b5f09e4d | -3.60427 | -53.33344 | 2025-10-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 741eb081-6fed-3479-8193-bbece67cf231 | -4.27285 | -46.92653 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c7ae90b-a752-3122-afb6-adf21cb6af0a | -3.50598 | -45.84761 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea3d9ba1-cec7-340c-a04b-4c0a7b3572f7 | -6.28354 | -44.41118 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f608bad-194c-3e6f-98ca-358a8d9be6c3 | -6.78749 | -44.52319 | 2025-10-12 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 030daa09-6782-34ba-81cd-d13d6e6de3b5 | -7.36698 | -45.19557 | 2025-10-12 05:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01368b79-a06b-3e9f-b1ae-ce13c197d6e8 | -3.87468 | -42.51188 | 2025-10-12 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6a8f6ca6-5ad5-33d9-a893-11f3b8a75abd | -7.85575 | -44.5218 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b528771-a6f3-3384-8936-721429f5a147 | -6.76831 | -42.83049 | 2025-10-12 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c0c2ccdf-67f2-3804-9360-57a51c6c95d2 | -3.39113 | -50.13772 | 2025-10-12 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc214e6f-dd4c-3a4a-b542-c524998959e3 | -3.56895 | -49.445 | 2025-10-12 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cd3d7f5-f162-3f34-a290-f6e8ea80542b | -5.91581 | -45.42415 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b70550cb-c28c-3530-b3d3-a051f429673b | -7.86467 | -44.88118 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2223fa0-219f-32d8-a38c-1d1667c70490 | -3.50569 | -45.83842 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed7a782d-6aa3-3d85-ae04-26d7e14e75ad | -5.91528 | -45.42799 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 200a5af0-b018-3a5e-8d06-88c89a245cf7 | -6.278 | -43.90724 | 2025-10-12 05:01:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16325f18-0263-3040-ad9a-9cd573935f4c | -2.71705 | -48.36328 | 2025-10-12 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc637a0a-d4dd-3543-9940-bfcdd9df246c | -4.22492 | -50.6345 | 2025-10-12 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93cc6960-2fff-321f-8e19-b41788bd3bf4 | -3.5075 | -45.83768 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a65f1d0a-7c53-3d81-a44c-3ae16d958297 | -2.79312 | -49.62064 | 2025-10-12 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dff372be-bef6-34be-9e35-faf26acbbab5 | -4.61295 | -45.77587 | 2025-10-12 05:01:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6e093f5-f1c8-340a-926a-b3bd5f5dc094 | -3.60283 | -42.75151 | 2025-10-12 05:01:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd582097-419f-3e82-b3ea-85d5a2228279 | -3.53273 | -48.9175 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1177ceb9-f62a-3841-85e5-1f49ddf0663a | -8.19219 | -43.32211 | 2025-10-12 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5455b82f-a621-3fad-9a5a-7494e81c7416 | -3.5091 | -45.85244 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94fbb2b4-a69d-34ca-893a-2d46445025e4 | -2.43615 | -49.36625 | 2025-10-12 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa943117-05c3-3285-9a94-03a8ca2163b3 | -5.36438 | -46.29182 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93eae556-416b-3555-ab12-822920e16cfb | -3.51444 | -45.85318 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 09aec3fc-cf28-344f-9f67-c2db3a20e444 | -5.86985 | -42.86914 | 2025-10-12 05:01:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9028ce31-b8d5-3560-883c-eb56f471a60c | -3.34395 | -42.16326 | 2025-10-12 05:01:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 36397cac-52de-3434-854e-1f9f74bf844b | -7.42309 | -45.16843 | 2025-10-12 05:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae1cc80f-6337-3a3b-8df3-1c0373e76730 | -6.31706 | -44.26214 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48c99c56-f63c-313a-95b6-c4cbbe3fc02c | -0.90306 | -47.55028 | 2025-10-12 05:01:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 05e1b901-4daf-3ac0-a961-2dbcf3cbbbe2 | -4.67724 | -43.25678 | 2025-10-12 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6152d18e-4acf-3354-9995-69875ce6d5a5 | -7.65264 | -42.57906 | 2025-10-12 05:01:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 328ea1a0-0331-3227-aaf6-9e554488b1a5 | -5.91923 | -45.42276 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b269b734-ded5-3a11-a355-76a52c5722b6 | -8.21685 | -43.36703 | 2025-10-12 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 417f840b-c553-3fcb-aa56-e8c2cf4da288 | -3.87387 | -42.51757 | 2025-10-12 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ee390f85-ae62-3f9b-b8ab-6b40b1a422e0 | -7.53926 | -43.84113 | 2025-10-12 05:01:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d880e842-c7f6-378b-a89c-367bf218788b | -7.85644 | -44.52461 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41a37a32-0ae8-32c8-9149-309ad5f8abca | -3.39348 | -50.14864 | 2025-10-12 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f074ca83-475a-3e1c-b7cb-9feb6fe349bf | -3.22433 | -48.92878 | 2025-10-12 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c614eb4b-94cb-3ff7-b7be-8c80aa5a80b3 | -5.3639 | -46.29507 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acabc36a-3408-3209-b76d-6686c07567fd | -3.50862 | -45.85574 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e7dd0113-2054-32d2-823b-97ff1bf5bef1 | -7.80621 | -42.42604 | 2025-10-12 05:01:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 830f7f5b-1027-3e89-a402-d5824d76a31c | -6.76754 | -42.83616 | 2025-10-12 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 394a9bc9-3562-335d-aba6-20e197cff3cc | -6.28418 | -44.40672 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30ace263-8f49-37e6-9080-e5524f6bf32b | -7.85519 | -44.52617 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 050ae657-0102-3ee1-90d3-0d452aac45bb | -2.44439 | -49.36751 | 2025-10-12 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b58bbe1-02cf-32a6-bf29-8434cd499771 | -5.91189 | -45.43348 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 04a49cb6-e55d-3202-8980-73a1ae6e1390 | -7.36756 | -45.19119 | 2025-10-12 05:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43ff415d-1c7b-3f87-864a-059f6d869a08 | -7.80374 | -42.43408 | 2025-10-12 05:01:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ebb6da56-b7aa-3e0f-bf64-e12109799fd6 | -5.85956 | -42.84464 | 2025-10-12 05:01:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 56f42a6c-c7d9-37b3-b3db-9021c19a6a31 | -3.51151 | -45.83586 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| feb7e369-d63d-3e06-a52c-30095c9b17b7 | -3.50329 | -49.05368 | 2025-10-12 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acb4aa8e-b46a-3168-baca-18dc9110a0aa | -3.50496 | -45.85422 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad63ef4b-eb07-3564-902a-4f80a09b5fc5 | 0.25328 | -51.08315 | 2025-10-12 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 293a5df2-9d18-3229-9a0e-35300d5c5b48 | -3.71533 | -52.08349 | 2025-10-12 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aece678a-57da-3b8e-b21d-a71c35a37d15 | -4.42046 | -43.47712 | 2025-10-12 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9ac9c1f-18d4-3f69-b3ad-705e0ea49728 | -7.48804 | -42.76302 | 2025-10-12 05:01:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 852c1391-aa51-3776-a8c7-2721d6bdc879 | -3.42245 | -52.72727 | 2025-10-12 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e24df09-ded6-30f4-a902-6e35d1b326f3 | -6.75687 | -44.65409 | 2025-10-12 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05569251-14b2-3f7d-a3a2-1e860bad5467 | -2.54279 | -47.80721 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 5841dd6e-1fc1-3453-8d8c-c1159c7899b4 | -3.8699 | -42.51615 | 2025-10-12 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b84879d1-c1b6-3cf0-be99-e548b6548165 | -6.75801 | -44.65673 | 2025-10-12 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28d39fba-ceb3-3fd7-a211-beede7c47bd7 | -5.86272 | -42.84287 | 2025-10-12 05:01:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 21371c94-0887-3fba-b486-c8fa4a523af3 | -7.85462 | -44.53062 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e8081a8-da3e-3aa9-a5fd-8d460a693ead | -6.5874 | -44.61915 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 85fdaf72-8dcf-3f4a-be4a-170047ea93c1 | -7.52407 | -44.29825 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9fa216d-808b-3012-8f8c-5aa00906e513 | -3.4379 | -49.83832 | 2025-10-12 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6b81be8-bb78-3c50-bb3b-3382eb4f9b12 | -5.86627 | -42.84534 | 2025-10-12 05:01:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 044f518c-285c-330f-9daa-36112a20b3cb | -2.78702 | -49.57917 | 2025-10-12 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 070395f4-e545-3471-accc-7fa3fc73632b | -7.40182 | -46.94832 | 2025-10-12 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c7ae894-f137-3248-837a-16703c46e480 | -6.76901 | -42.82529 | 2025-10-12 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7fdbd977-2f72-3778-8d8c-cb5fb9cd79ff | -4.22101 | -50.634 | 2025-10-12 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dab826b-420e-3f51-9960-1377b3dba398 | -5.75736 | -46.49529 | 2025-10-12 05:01:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ff34d53-745a-3af1-b06f-fb6d8fcb7c34 | -1.56993 | -60.34167 | 2025-10-12 05:01:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 333ddc78-a350-37bf-8b61-b331bd1e8436 | -6.84428 | -47.3444 | 2025-10-12 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3cbb0a6-bf34-388e-a66b-7d2568fa8ea8 | -2.43916 | -49.37424 | 2025-10-12 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4805ecd7-7e74-3eb5-bb00-09e2957e84ee | -3.51637 | -45.83997 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86f15673-43e1-3d30-8fdd-976d4a973398 | -4.42749 | -43.473 | 2025-10-12 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ee8844e-1159-356a-852e-597993a23191 | -6.58133 | -44.61852 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a212e04-98ea-31dc-84c8-6d3cb6cce0ed | -7.80292 | -42.44061 | 2025-10-12 05:01:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9dced0fb-13b7-3ef4-9dec-b0c42c10aed0 | -3.51782 | -45.82999 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d315645b-bd23-3ed2-aa3c-148c5f461343 | -2.81858 | -48.61222 | 2025-10-12 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f88ee3bb-bfef-3429-90a4-c3a7b552ac1a | -7.80449 | -42.43916 | 2025-10-12 05:01:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 84160981-9933-3b89-825c-ba3481aebc3c | -7.8614 | -44.52679 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c37957b3-3d5a-3a58-b57f-bb617a5b5f37 | -2.7044 | -54.65375 | 2025-10-12 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8638336-b868-3bfe-ad06-f8c08439f679 | -7.88798 | -44.51598 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19c81b3a-7a67-322b-8e47-8d54a343a69b | -3.97327 | -42.84822 | 2025-10-12 05:01:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a49af873-e42e-3723-98ef-eab6a654acd7 | -2.53745 | -47.81133 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 067da35b-0c01-3419-950f-2fbdbf90e77b | -3.60861 | -42.75349 | 2025-10-12 05:01:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c17b3c96-5cf9-3ca2-a8f8-a153baa86849 | -3.50376 | -45.85169 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a10c3f17-0bac-35c6-81c3-bbf722d2789f | -3.54383 | -53.02475 | 2025-10-12 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb30cac1-02f2-325c-a931-41793567661a | -7.05641 | -44.70538 | 2025-10-12 05:01:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README39.md)
