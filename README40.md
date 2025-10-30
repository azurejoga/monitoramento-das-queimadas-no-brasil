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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fd2e1b6-b2b2-3f5f-b5e8-3a27180d6602 | -3.7942 | -43.90122 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0dd5078d-2c59-3134-bcec-a6e336b1112a | -4.05315 | -44.26526 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bed2e77-2d43-32ed-8a4c-5273390992cc | -1.63133 | -54.22018 | 2025-10-30 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4bc3ee1-aae0-3996-850f-2ddcd47f4da9 | -3.1272 | -49.10073 | 2025-10-30 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6b577c3-0a57-3d11-aa93-dcc2cbeae196 | -3.64359 | -43.97108 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2995d8e-2230-3939-a0ac-6a2b4d07a092 | -3.53286 | -47.55437 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 408b7f3d-b16e-3ec3-80e7-3b4261228875 | -3.78685 | -43.90382 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f9a1f112-984c-3402-bdac-9b988fc51266 | -4.25419 | -43.71457 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 3289fdea-539f-3ad0-8c00-c4edd218e500 | -3.36588 | -42.19686 | 2025-10-30 04:23:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4354dc68-ffe7-33a3-a21b-d1472fe7762e | -2.76542 | -45.39346 | 2025-10-30 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dd4ddca-24f1-3dcf-bf01-c87101bb9d1c | -4.43004 | -43.44095 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cd6fcb1-d884-34f2-a215-98658278b571 | -4.48595 | -43.43652 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3196cfcb-9700-302b-8d7b-253f09f9c17f | -4.82837 | -42.73317 | 2025-10-30 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b282ea8-877b-3cbe-9b0b-fd8a8e0faff4 | -3.55827 | -46.95259 | 2025-10-30 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5afb74f9-6ea1-308d-8980-38176f5ca814 | -4.26103 | -43.71566 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d636b5bf-02c4-3cb6-ae92-0d54aacc6e76 | -4.45879 | -43.23284 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c499b7d7-782a-386d-97e6-ce10c967179a | -10.27455 | -44.56475 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d59391ef-e7b1-3356-b473-91b376ba86a8 | -11.15772 | -43.48091 | 2025-10-30 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd4e4456-1972-3cf4-ab5d-d4bc4689596d | -5.67246 | -43.94546 | 2025-10-30 04:25:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6797527e-2045-3aed-b5d2-f94d8763ed51 | -9.3512 | -50.62437 | 2025-10-30 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c35fb429-71fa-3d4f-bfde-71061355ca6b | -11.5502 | -44.68307 | 2025-10-30 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b5c17af-564a-30db-8934-48c0dcb2066a | -10.61789 | -44.12609 | 2025-10-30 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc6304e3-40a6-31ce-a541-6bed22005d4f | -4.91266 | -45.76012 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 774a0800-324e-3549-996d-29829244dadf | -11.04268 | -47.83887 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a9469d5-e636-3753-96ac-0096c675c610 | -7.12584 | -46.99801 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bd5074f-3373-36bc-9371-84df2f251ce5 | -5.0627 | -45.3242 | 2025-10-30 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31c37c57-a8d8-32fd-b66a-9aa33444de82 | -4.57142 | -46.94406 | 2025-10-30 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f836c72-9487-3c44-90d0-65273b5ab5a1 | -9.04965 | -48.73721 | 2025-10-30 04:25:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff1ea5c9-f289-36a7-8307-852b9306abd8 | -7.35229 | -47.62279 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bd7c0f0-562b-3e0f-9cae-a5d8746160c7 | -11.06034 | -47.53564 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff35799c-7585-3a87-9fe9-2c5fabec3046 | -8.31518 | -45.37007 | 2025-10-30 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8388b01e-2dcb-38b1-82ac-f24d4faa1297 | -10.7611 | -44.73626 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2fda66b-f58f-3951-8710-c224b1d4acd5 | -5.63134 | -44.94773 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19b3ea0d-c3a2-3b18-b43a-1228412aa757 | -11.13449 | -51.08076 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| db920ed3-9ba5-3f69-a6ac-d7ecaa41c1b8 | -10.85754 | -47.8701 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12ba66f4-ee99-398c-af1d-ba3aaf34f943 | -11.91798 | -44.17489 | 2025-10-30 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6e6ff49-77e6-3e93-b523-afc9427c8077 | -9.24049 | -45.56055 | 2025-10-30 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 383ce440-cce7-344c-a824-eaea0c3c014b | -3.73681 | -52.1474 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0490b102-aa66-392a-959d-2102cdf62daf | -4.5599 | -46.33641 | 2025-10-30 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e888437-015a-38f6-831e-00b93c8da8b6 | -7.96237 | -46.71476 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acf8f9e5-4041-3a69-b70c-f7c318d1c371 | -5.80772 | -40.83706 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 9dce753a-4e06-3bce-a47a-8d452136ca6c | -7.96622 | -46.71182 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e18150e-4991-39f5-9615-5cbb77415a1b | -9.27925 | -45.22158 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e696c7c-6162-3e28-828b-f568f66c2fea | -9.84575 | -47.69455 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5d05549-1289-3d98-9bc3-e7aa01058826 | -5.16028 | -42.51785 | 2025-10-30 04:25:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3885bc34-e27e-3297-a148-fa854e267001 | -5.59836 | -49.08102 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e62587f-735e-3f96-948d-249b2703fa24 | -6.10617 | -41.72902 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6e24c08b-2f6c-3aa0-939a-f9eb2b125746 | -10.8603 | -47.87416 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df3e5883-b859-3aef-89a3-2756ecb34be7 | -4.59119 | -47.07806 | 2025-10-30 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a66e5d81-1337-3bb0-8cbe-b05767af3a73 | -5.67775 | -45.88453 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4ad5e40-2104-3f47-b2ec-6c8657856f12 | -10.27688 | -44.57311 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 22b51c9d-addf-39b2-8897-bd2099a7e17f | -6.64054 | -44.61584 | 2025-10-30 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5e0468f-719b-3910-add9-2d0a503d4cf3 | -7.49967 | -46.7404 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82351b3a-5e2c-378a-891f-4be0b5c483c9 | -9.32079 | -43.09595 | 2025-10-30 04:25:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df4eab78-ce32-329c-96d6-36be02df2872 | -6.16403 | -42.40034 | 2025-10-30 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 54cd7bad-4f27-3027-a29e-b05f50b5a723 | -11.16965 | -45.22433 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3ec1a68-e4fe-3839-be71-9d833e23ba8c | -5.50521 | -49.58474 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f57ac05e-a47d-3ea5-b5ae-192bf0999940 | -10.61931 | -47.89292 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5df7102d-fdc1-32e2-b136-6d4f72af8e76 | -5.23651 | -44.29478 | 2025-10-30 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 028f65df-2c19-36e2-bfc2-88c1e364bc01 | -5.43789 | -45.09744 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9660c830-05f1-3cef-a1bc-3b87809532b1 | -6.14553 | -46.34414 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4ceac8b-859a-39c6-a27b-41bec55f9650 | -8.31998 | -47.92878 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 165bc6c8-d2ad-3f3a-88f1-3eb1085ccb8f | -3.84427 | -49.37886 | 2025-10-30 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c74a21c9-6772-3b7a-a045-7b57515e75f9 | -5.57493 | -42.17234 | 2025-10-30 04:25:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 03de3d83-b416-3303-91d1-83e34fd2e6b4 | -4.46755 | -45.7605 | 2025-10-30 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2a33d09-6a9b-31be-a4e7-cfec3f2b9839 | -7.38473 | -43.00817 | 2025-10-30 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 05c0c7ca-bd4c-32bd-820a-3373d3ed2b53 | -6.5183 | -46.90796 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9dce3fba-c240-3e6a-b7a3-c85cc8e5772a | -10.92967 | -50.20616 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebf03048-032f-3478-9bfc-e4eb33042ce8 | -6.13617 | -41.69688 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7199c664-f634-3ef4-a97e-59a1887433c4 | -7.27828 | -46.78645 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09da4730-d71e-38c6-8734-9194473f4363 | -5.58795 | -47.15939 | 2025-10-30 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae7c58aa-798a-3e4d-9f5c-ff263987358c | -8.74236 | -46.50917 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85362854-f026-3eba-b479-b20b0ed37b3d | -3.6596 | -51.71479 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe76971c-8bdf-3835-8567-af7a2d818541 | -6.97974 | -42.66517 | 2025-10-30 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b78bf31c-1536-3793-aaea-fee81395fde6 | -7.31115 | -47.81466 | 2025-10-30 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83807e7f-9a43-3ad4-a4e6-207a8bc5ba52 | -9.90377 | -44.89293 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98f07157-9e02-3b15-991b-5fc14f880a9b | -5.40978 | -46.0115 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a17ec886-4e97-3896-81e0-192a92723e1b | -9.83522 | -47.69646 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c88abee-0dfc-34a2-b5e3-9db8ad2ad5be | -10.98953 | -47.87335 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 037efcaf-bb59-3fa2-bbd2-81ebc7107819 | -8.96175 | -43.988 | 2025-10-30 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2cc7eb6-c86c-3f6a-923b-801c1023b969 | -7.90494 | -45.67587 | 2025-10-30 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ca16aae-b07f-3e29-8936-5f0390a17fdd | -6.21641 | -41.82101 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f0bd5edd-97dc-3ecb-9324-c2aee672bdce | -5.03676 | -43.61545 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0ba79937-6686-3015-98d1-cc1b831f594a | -9.84244 | -44.88402 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d39b0223-e518-38a7-a4db-2de460abeecb | -7.79409 | -46.42495 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 321c15b4-1102-3fbb-bdb2-11fc7454cc21 | -6.63205 | -44.60352 | 2025-10-30 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85be9422-b1de-30f8-83c0-f78471302fe5 | -10.64919 | -47.89786 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e58f990-cd2f-3a4e-9811-6e6ddde8415c | -6.10999 | -41.72988 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c1c28d31-eaaa-329b-8172-c6fc0618770a | -5.20089 | -45.61166 | 2025-10-30 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da42210f-2159-3f52-9e2d-5756bc9a6a5f | -10.85642 | -47.8771 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b63949a-5587-31be-b666-d2879f753f64 | -9.29398 | -48.42041 | 2025-10-30 04:25:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a27f837-ece3-34e7-897e-b4be8b1331b4 | -3.82707 | -51.21817 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9652767-9133-39c9-9094-820af2e91903 | -5.8221 | -40.79696 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4656713-9185-31a9-ae1a-6f9da7cc6f61 | -11.03559 | -47.79792 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dac8bdd8-45c8-3270-8fe4-6443067cc4ef | -6.53394 | -43.57301 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 25e4ff06-f090-3019-b734-46ee5631eb79 | -7.5234 | -42.85531 | 2025-10-30 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a772dbcb-5438-3c64-9a42-460189d7cda0 | -5.84435 | -45.53882 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 040075d0-2241-37c6-913e-5e30a4272370 | -6.56802 | -41.59072 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 796f9e34-60dd-38bf-942f-37e5ca035970 | -7.38663 | -42.47281 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 91ba445c-d493-3c13-aaec-d75b2940cdb2 | -5.1312 | -45.36325 | 2025-10-30 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README41.md)
