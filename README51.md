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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a860ec8-8b24-387f-bd9b-5310b302f681 | -4.11238 | -48.02015 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1011398c-546a-388e-a283-5faa825b84fa | -4.50355 | -45.40091 | 2025-10-16 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ba19611-bc75-3bc8-ad70-02fff0a72ab1 | -5.72517 | -44.28434 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 186157e9-141c-3d02-a781-fbacd8793cd3 | -5.32208 | -44.84033 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26c3abf1-9eb3-3efa-830f-3942eafedf6f | -7.34235 | -43.86351 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d0b72e47-7305-3ded-b006-36cbaac1a492 | -5.88534 | -42.78099 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2d526a95-d67a-3f07-9a2b-b405d9f9ddd3 | -5.96652 | -47.21123 | 2025-10-16 04:38:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e882894f-7cab-31f4-902b-d18e2ad940e2 | -2.44448 | -49.36969 | 2025-10-16 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 123eeab3-965d-3e54-b6bc-c1b7db56743f | -6.38685 | -41.93337 | 2025-10-16 04:38:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b126a5cd-6574-35c9-92b7-c2449e6f0b9d | -7.00489 | -43.74419 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e25e4e81-06a8-39b8-9a63-97c12f5e48d8 | -6.53451 | -44.69149 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9d5b6c3-f29f-36a8-9451-33e44d52dd51 | -8.2495 | -44.13684 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0618500-96e0-3dd3-85bf-c885446150ba | -5.45836 | -41.0161 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9c16b0fd-f518-34fa-a46f-3dea98d08e48 | -4.77383 | -48.66909 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb13ca2b-9e78-3cac-b6e3-1a61452cba82 | -6.04779 | -44.24481 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a13f027-03bd-32b2-ad20-5d0bdd803bd9 | -4.97365 | -43.60323 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81d8eb33-20d7-3208-9052-35fa4e544ef2 | -5.66238 | -45.96139 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08fec690-52d1-36ee-93da-67cc81c262ac | -6.17167 | -43.43819 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3198ae60-9bd4-3a9a-a8c2-bc9aea277111 | -4.09911 | -48.01809 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cb5cb63-9a68-354c-a5f1-bdb3a50c000b | -3.86274 | -50.04855 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73a3434a-c649-3904-9434-4f8b6d1f6095 | -5.49253 | -48.94762 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7cc05ed6-573d-36f0-8de6-6db12ba415aa | -6.13885 | -41.75188 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c577bfbd-f092-391e-949a-3db2aa8c92bd | -5.34548 | -43.52726 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7291ba07-49c8-3193-8e2f-fab674ab622e | -5.42167 | -44.23471 | 2025-10-16 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64d0266e-3fee-30dd-899f-cdbff3c06880 | -5.83986 | -42.34265 | 2025-10-16 04:38:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 70fd8d59-fa4f-3edd-b902-96d8b16da59e | -7.1487 | -44.37837 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7394c4e4-c485-32f0-94a9-2b77438eb76d | -5.87971 | -42.82031 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6d6094e-008d-3dd7-a7c7-b47fd91f5d77 | -3.88001 | -51.94436 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cb3eaad-d864-394b-970d-0de56808f94e | -3.01547 | -45.38454 | 2025-10-16 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 81b0b771-8094-3139-a440-3f69f0e9ad61 | -6.80505 | -44.65328 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e38ad43-863f-3801-9447-d460b66921fd | -4.84498 | -42.78625 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79bb825d-f68f-36a2-828e-be4c9ccece20 | -5.9139 | -42.83446 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 460cd535-ee06-35f7-afc0-ea2755c10a8b | -6.19309 | -44.10909 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 019ce2c5-6b96-395e-bad7-4e0c876355d4 | -3.15029 | -49.42794 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 753d57b4-bc5f-3539-bfa9-3d55b44ab004 | -4.32891 | -46.5391 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50bf4733-d6d3-3ddb-96a0-57bf71fb2188 | -3.65631 | -51.75198 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfe21f97-985d-3459-9ccc-cb3f018a294f | -3.38559 | -50.26955 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b28b393-bc78-382c-84af-564ccd4e36fb | -5.45775 | -41.0245 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 679ee695-539a-351f-ba10-3c927900f5b8 | -3.51486 | -52.49173 | 2025-10-16 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3cdb7f52-7bd8-30bb-9ec3-6a61bb9fedc2 | -5.44416 | -41.00857 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ff8666f0-b184-3671-8898-03a6bb93e0c3 | -6.48414 | -48.7635 | 2025-10-16 04:38:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 286f514f-989d-3946-b9e8-092edd2cf713 | -7.47533 | -42.67655 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a5c22043-c928-3386-b0a1-00919aefeb20 | -3.01611 | -45.38033 | 2025-10-16 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 463cdbf3-23c1-3830-865f-4ea2e86663f9 | -4.67616 | -49.33643 | 2025-10-16 04:38:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51c8b801-8da5-3f41-9c38-c2f7c4b65427 | -6.20105 | -42.60893 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8480a3f2-0b43-3784-ab07-316eb883d4e5 | -7.00898 | -43.74553 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 73f48200-5702-3238-832f-0e0ffffdee06 | -3.33183 | -53.24291 | 2025-10-16 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c9fd094-3efd-3962-838e-386306b304dd | -6.14689 | -44.7382 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62f22055-a861-321d-80c4-ac2e3af89ce0 | -7.27747 | -42.95012 | 2025-10-16 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2db6677a-00ff-315c-9015-036ea8bd7ac4 | -5.51378 | -43.20253 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26f47e09-7ff7-3fea-a638-6113dd7bd914 | -5.60111 | -47.49352 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05ebb725-4294-3bb1-b4fd-20db94cababe | -6.22159 | -41.55148 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2ee4c598-cf3d-3b3c-b1a2-863d16f26a43 | -5.87209 | -43.88524 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30aec7ab-60a9-3710-9bf1-d82a651b18a6 | -7.10931 | -44.71154 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6177ce2-bdcc-322b-8000-0c836af4a505 | -8.21812 | -43.99566 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e725d617-201a-33fe-9e98-0ed52dec8dcd | -6.50371 | -44.4639 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c7a0dd4-c382-3942-b541-9a048226aee7 | -5.6041 | -44.25913 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e204e9b-367a-3343-b303-175c911bb77e | -2.95028 | -49.33589 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e900919-fff6-3ef8-bea2-0d604c1b4d24 | -4.50723 | -45.40146 | 2025-10-16 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac7191ec-fd04-37a8-a480-1748e73f725b | -4.93003 | -47.08463 | 2025-10-16 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b230e40d-943e-323b-a7e6-9a0ce6f82e31 | -6.4048 | -45.3538 | 2025-10-16 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c606602-d343-3d49-97a0-3a3b574040d4 | -7.07881 | -44.95131 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 80442270-be2a-30d1-996b-dfa1f8037420 | -2.87646 | -50.7383 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 791a174f-fd46-3b6d-93d4-50478657d9b1 | -4.37588 | -43.38217 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 163288c5-b40d-35ce-9a3b-590c1823b033 | -7.07491 | -44.95061 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b75fe282-05a1-3ea0-883f-67a7f8a7f709 | -4.37928 | -47.26463 | 2025-10-16 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c28f8fd9-0b9b-3173-adf1-1078383558d7 | -4.71976 | -46.15778 | 2025-10-16 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd87b273-1d5f-302f-b402-80eb631d3dca | -6.57113 | -42.95776 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f90228a-0bbe-3c28-94b4-c2ed55f29d99 | -6.00617 | -43.12471 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ff11283-1b83-30a5-9749-bd0349c31c5d | -3.59419 | -43.04596 | 2025-10-16 04:38:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5778b15c-b112-3734-9fdb-4fcea9fa2cbe | -4.9231 | -45.89464 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91b0cb6a-a4a6-3046-8ab3-051e0bad91aa | -7.04076 | -42.73782 | 2025-10-16 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 5d3d071c-23d0-350f-ab7e-151bda31d3e7 | -8.25461 | -44.10175 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a6e7e62-f2f1-3605-a6c6-1ebd0241dc6a | -5.89835 | -44.27309 | 2025-10-16 04:38:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16e8df07-7ccf-3cd7-9b1c-eabace824bdb | -5.40935 | -40.89454 | 2025-10-16 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3110e663-2f2c-3868-97c6-de56d0ab38ef | -8.25555 | -44.06572 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90281b61-06aa-313b-8c12-51ba9afbc20a | -4.56852 | -49.71561 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 517430d2-93a0-3c8c-b25d-451d823c4ea9 | -5.25086 | -43.22346 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3fcb406-41eb-3791-ba53-e4b40a73a19b | -5.43019 | -44.2324 | 2025-10-16 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 66123b52-0674-36b4-9627-ebb47a784113 | -4.38005 | -43.38283 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 969c6ed6-06ab-3934-b0a1-3f7d3b15f5e6 | -7.2781 | -42.94566 | 2025-10-16 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 743d5d24-3c3b-35e7-bf65-ec9ddc6a58ba | -6.03272 | -44.31839 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 152bcde6-5d41-34fd-9a58-4e8a6f8a2555 | -4.96254 | -45.09924 | 2025-10-16 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0f5b33f-427b-3e99-90b5-45e044421bdd | -2.87303 | -50.73776 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 85987c74-3afe-3fc0-a371-892170e33ebe | -7.95586 | -44.13988 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62dcf46d-0a81-3eea-9305-fb64a5654506 | -8.24299 | -43.33691 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 16a4da7c-019d-3e9d-9bb5-b89e9024f4ab | -6.06675 | -41.91217 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c0e9e3e3-f47c-32e2-9658-c973e3d78bc4 | -5.30071 | -43.86263 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66d41458-43fb-3503-b3d7-e9ece04de3ad | -7.44047 | -44.75069 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2053c6e-aaec-3083-a918-4fe250294960 | -5.26234 | -48.30542 | 2025-10-16 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82669e01-91e8-30c9-a515-19fc1ac53c92 | -5.69725 | -43.54527 | 2025-10-16 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad82baee-35fa-368b-8613-5e2c9afef184 | -8.25395 | -44.0808 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4920d7de-2c4f-3db7-8782-9630ada0d5de | -5.8392 | -42.34729 | 2025-10-16 04:38:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7a0fee38-411c-3418-8ed9-50274cf02a31 | -4.29055 | -48.5794 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ce02998-bbe1-3828-ad07-fc084b9a41b0 | -5.8644 | -43.88023 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 645392ec-344c-3e53-a033-5b56c31ff01a | -5.3546 | -43.75406 | 2025-10-16 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b8866d30-fb09-3774-9e75-a7d367b8a779 | -7.67204 | -42.37225 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 252da88c-4e8d-3cb5-bde3-b125bf29e8a8 | -5.40717 | -40.90996 | 2025-10-16 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6950ce9b-ff02-3e04-a9e6-cc033d8f4806 | -6.06496 | -41.89116 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7dca22f1-3a43-3fed-af1f-78dd1c31e393 | -7.927 | -44.12399 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README52.md)
