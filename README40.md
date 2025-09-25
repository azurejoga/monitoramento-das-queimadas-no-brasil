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
| 157b4aaf-d185-34e5-a848-7f3ba0a6f323 | -8.4987 | -44.9998 | 2025-09-25 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 2de93e74-db70-3b60-8da0-c81bd4812d3c | -12.8487 | -44.6675 | 2025-09-25 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 88408a88-7b62-39ec-bdd0-f980c33ffbc7 | -7.4621 | -41.9041 | 2025-09-25 13:30:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 8d0904f3-241f-37f4-86ae-4abc78f9cb7d | -8.6817 | -44.0121 | 2025-09-25 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| a8986ead-0ae4-38b9-81d3-cc5ad2985fc4 | -11.6814 | -44.4078 | 2025-09-25 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 89a6b2ee-9b4e-3d83-81d9-252dae04c7ca | -4.5163 | -43.6536 | 2025-09-25 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 27c26917-695a-3726-a09c-a04e4b607a97 | -4.4611 | -40.9566 | 2025-09-25 13:30:00 | GOES-19 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 92.3 |
| da4a5fe8-0e67-3ef7-b106-cbcf19e001c3 | -17.9308 | -55.8758 | 2025-09-25 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.9 |
| 2efcf0fe-a76d-3663-8039-936364c73f33 | -5.1972 | -42.6984 | 2025-09-25 13:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 6a460656-5b1c-30c9-8da6-d01a208db02a | -12.8676 | -44.6878 | 2025-09-25 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 205fae3c-77a5-3105-9c8b-5ca66e7a0e4c | -11.6457 | -45.3388 | 2025-09-25 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 278.0 |
| 0c90e6b1-148a-380d-aed7-0ee1c5c06164 | -6.4317 | -43.0942 | 2025-09-25 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 2c46bd7c-0cad-3fea-8770-7c2e7bd16aa1 | -8.8993 | -46.1135 | 2025-09-25 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| e179952a-61c6-3fd9-8cd6-d643eea5dcd5 | -8.8996 | -46.0909 | 2025-09-25 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| fbdeaeb9-8031-307f-a021-163092d49c07 | -5.6069 | -42.9973 | 2025-09-25 13:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| d79e2682-58e9-35d4-aad2-285b8be3c9d6 | -17.9312 | -55.8548 | 2025-09-25 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 2dad2d14-a689-3781-bed0-270cd0e29a43 | -11.4037 | -44.959 | 2025-09-25 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d18beb58-57ed-35c9-a906-6dbc56043925 | -12.5388 | -45.7799 | 2025-09-25 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 427.9 |
| ca0b52e2-b706-3126-b659-969500782413 | -17.9506 | -55.8731 | 2025-09-25 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 3854d9d1-befc-3586-96a5-856b62781760 | -6.2354 | -45.928 | 2025-09-25 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ce719806-3435-3e0e-962a-9c7963ac9ed5 | -15.8029 | -59.4835 | 2025-09-25 13:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c0780e09-a5bd-35c1-aa06-84eb049e4c8d | -15.8029 | -59.4835 | 2025-09-25 13:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| e9d92c28-4431-3912-98b9-84ba4eaf91b9 | -5.0822 | -43.0118 | 2025-09-25 13:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| dda3d9ec-bbc4-31d9-87bb-640e3bca5820 | -11.6266 | -45.3416 | 2025-09-25 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| ac5bacdb-0378-300c-aed6-ac7c2662cfd8 | -17.9506 | -55.8731 | 2025-09-25 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 9a1b1446-69be-37e8-aae3-ed26117924ee | -11.6457 | -45.3388 | 2025-09-25 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 356.2 |
| 0a0834c4-a0a1-3c86-a347-efa0d35c90f2 | -8.8993 | -46.1135 | 2025-09-25 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 70a88b30-b91a-347c-bba3-446a0fb78aef | -8.6628 | -44.0142 | 2025-09-25 13:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 5e0cf2f7-2470-371e-9a79-0149e294265f | -7.3567 | -44.4496 | 2025-09-25 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.8 |
| ae16aaca-bee4-3d9e-83df-0343b808806e | -4.5163 | -43.6536 | 2025-09-25 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 0e2395f8-7845-3d06-8380-46671ebd6d35 | -7.4621 | -41.9041 | 2025-09-25 13:40:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 142.1 |
| bc62ca5a-0fe1-3e4c-a4bf-46445cd68dbf | -11.6818 | -44.3844 | 2025-09-25 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 200.5 |
| a5e03caa-92ac-3a6c-9b27-350f07f875e3 | -6.4317 | -43.0942 | 2025-09-25 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| f9c4edce-d47a-3a89-b786-a6bdb11bf111 | -5.1972 | -42.6984 | 2025-09-25 13:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 06cd8d08-45d7-3518-861e-fd6b2ed7ecba | -11.6622 | -44.4107 | 2025-09-25 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 83478353-be70-3599-9e9b-7a34851541d0 | -12.8676 | -44.6878 | 2025-09-25 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 230.5 |
| 5eba989f-4a81-3e7d-9bb4-aa02af4daccd | -11.6262 | -45.3646 | 2025-09-25 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| b4ed709c-7c0d-3e21-9872-c5b52cd99de4 | -17.9312 | -55.8548 | 2025-09-25 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 0ad4d83f-20da-372d-b314-b9ee228b3c7f | -8.8996 | -46.0909 | 2025-09-25 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| cce2b3ea-6dd8-3fe3-8e4f-981ba35994b5 | -11.6814 | -44.4078 | 2025-09-25 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 286.2 |
| 9d130785-b3a1-357f-8362-9533e704d234 | -5.0824 | -42.9884 | 2025-09-25 13:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 17570f25-8ab8-3dbf-b39b-d08e45bcbafa | -17.951 | -55.8522 | 2025-09-25 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| d4cf89ce-9a34-32a9-984f-e4707a5d3034 | -12.5388 | -45.7799 | 2025-09-25 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 562af97b-c530-311c-b816-4256e0620ae4 | -17.9308 | -55.8758 | 2025-09-25 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.5 |
| 3d00eba6-f7c6-31c1-acf9-bb624d8ccd29 | -6.4131 | -43.0724 | 2025-09-25 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 67f90433-2e4d-369c-b8bb-be5e2335d824 | -8.6631 | -43.991 | 2025-09-25 13:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| ffd21f5a-bd58-3c50-87b4-f8023fec5a77 | -8.8415 | -46.2095 | 2025-09-25 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| bd882be1-c276-3635-bace-95ae3aba48d4 | -12.8483 | -44.6909 | 2025-09-25 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 7f421c75-1310-3762-b093-36e403e09d29 | -6.8836 | -44.7673 | 2025-09-25 13:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 12887abc-f55a-3f8a-aae3-4efb6f91eae5 | -6.4129 | -43.0958 | 2025-09-25 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 777f0d36-2fb8-3d1e-8434-7c9d6bbb15a0 | -8.6631 | -43.991 | 2025-09-25 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 6eafdde2-6ecc-3c27-a59c-963df9e942d0 | -12.8681 | -44.6644 | 2025-09-25 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 6f0ccd44-a60e-394e-b764-84e6d878ebf7 | -15.8029 | -59.4835 | 2025-09-25 13:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 21d11b23-73e0-33d1-a715-a2eac70e2333 | -11.6626 | -44.3873 | 2025-09-25 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| e98656b9-34ad-3673-ba59-814f6b9a4d13 | -11.6818 | -44.3844 | 2025-09-25 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 251.7 |
| 0f85425c-559a-37ab-ab86-67972f70e2e5 | -12.5388 | -45.7799 | 2025-09-25 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 5c66b13f-0edd-33b4-ade0-e7394701b0f1 | -6.4129 | -43.0958 | 2025-09-25 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ed772677-8a29-3260-96f3-1fe2d2a82350 | -6.4317 | -43.0942 | 2025-09-25 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 3b985de0-27e1-3bc6-a4b8-cbcede13322c | -11.6622 | -44.4107 | 2025-09-25 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 7a5e9a1c-2a69-34ff-981c-67ba42b2dfe0 | -8.4987 | -44.9998 | 2025-09-25 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 14a37886-a228-32cb-9f45-c8e814868080 | -4.7974 | -43.5435 | 2025-09-25 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4a0c6214-589b-383d-b5f1-e8f0d318d29b | -8.7894 | -43.0631 | 2025-09-25 13:50:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| e81b7ac5-4f45-38ed-a259-ce126abac9f4 | -15.2819 | -59.4321 | 2025-09-25 13:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 25de792f-94a6-397f-ad19-85b390d47987 | -11.6457 | -45.3388 | 2025-09-25 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 3621b787-cd8e-39d7-b8a5-4433ac5b6735 | -7.4621 | -41.9041 | 2025-09-25 13:50:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 119.9 |
| f138c480-7c4e-36b9-a41d-cf5f45e2b6f4 | -20.5441 | -57.1434 | 2025-09-25 13:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3ebbf124-34ae-348d-9816-b5e2618eb817 | -6.6975 | -44.6232 | 2025-09-25 13:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 1be73a28-4130-3e08-b948-13b4cfb85e07 | -8.8417 | -46.187 | 2025-09-25 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 71b5b4a0-df86-3011-b587-ca8491dc7fe2 | -6.4131 | -43.0724 | 2025-09-25 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 096601b9-0c0a-3f34-8b65-c5ea1715d343 | -17.9506 | -55.8731 | 2025-09-25 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 3508ad7b-71f9-3b5a-985d-164670e296c1 | -12.8483 | -44.6909 | 2025-09-25 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 166.8 |
| e6cbca54-56f7-31a6-936f-73beae3be690 | -17.9312 | -55.8548 | 2025-09-25 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 6366a2cc-6b63-3009-b157-2725e5b6e655 | -12.8487 | -44.6675 | 2025-09-25 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 7770bcac-20e0-3fb5-add7-0e96da311948 | -17.9308 | -55.8758 | 2025-09-25 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.7 |
| 1dc0cfdc-d7a0-391c-a706-d961f1799695 | -8.8996 | -46.0909 | 2025-09-25 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 0495f4d6-3323-378a-9365-316577dfae97 | -12.8676 | -44.6878 | 2025-09-25 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 229.6 |
| 0a6f5700-2cff-3170-9fb0-c3d8f89254d0 | -5.1972 | -42.6984 | 2025-09-25 13:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 7356e601-d512-3c9a-bea7-55d6bb22b11f | -12.5384 | -45.8029 | 2025-09-25 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 239.5 |
| 65999c6f-042a-3a78-bd9e-5edef4a0ae1a | -8.8415 | -46.2095 | 2025-09-25 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| ade4cd18-5c85-3c1f-8f37-6dff7abe3496 | -15.8029 | -59.4835 | 2025-09-25 14:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 17eeb607-ee5a-331b-97af-d0cf72d2682f | -10.313 | -45.2219 | 2025-09-25 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 01c6e159-5d9d-3ad0-8a6e-19bdc6599871 | -8.1324 | -44.1417 | 2025-09-25 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a234784e-a495-3dd2-ae8b-b07a970a8334 | -6.4129 | -43.0958 | 2025-09-25 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ccbe5dd9-b139-399f-a023-adbc3befb9a8 | -12.5388 | -45.7799 | 2025-09-25 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 65849e5b-e6ac-33ab-815d-80e27e6850e7 | -6.8336 | -44.175 | 2025-09-25 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 96109528-3e9a-3cec-98ed-e2cb8dd81f25 | -11.643 | -44.4135 | 2025-09-25 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 05d69a7b-9418-3f25-bdc2-15bdf3ca850b | -9.7851 | -46.2851 | 2025-09-25 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| b8a6757b-f110-3d96-b7a3-6d53758aa7f9 | -12.5384 | -45.8029 | 2025-09-25 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 403.7 |
| 111945db-7189-3f18-b7d3-520795e674ae | -6.8836 | -44.7673 | 2025-09-25 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| fcde222a-d3b3-333a-ac4b-0c0737f16a62 | -17.9506 | -55.8731 | 2025-09-25 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 5b122ae6-ff40-3972-981e-383e94376666 | -11.7006 | -44.4049 | 2025-09-25 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| a928d17e-b87e-3f70-b9c4-5a95e2b7e190 | -12.8483 | -44.6909 | 2025-09-25 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 189.6 |
| fb0d115e-89a3-32df-ad9d-f8e55df87316 | -8.8415 | -46.2095 | 2025-09-25 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 567a2f84-e055-33e0-b3ea-82113d1edb5f | -10.3938 | -46.1444 | 2025-09-25 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 85597d87-34d7-3621-aec0-cc3fb12bee6f | -17.9312 | -55.8548 | 2025-09-25 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.5 |
| fae91126-2e43-3d33-b96c-cf0432977c69 | -6.6975 | -44.6232 | 2025-09-25 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| afd4caa9-a854-3225-9ed5-90c70169b6b8 | -12.8487 | -44.6675 | 2025-09-25 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| d7244786-8df5-37e2-80ca-d2e086beea9f | -9.771 | -45.9484 | 2025-09-25 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 66df0802-5131-3df3-a6c2-371ee27119b1 | -20.7732 | -57.8656 | 2025-09-25 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 5a348dc4-0e38-34f7-b4df-054421c146f2 | -12.8681 | -44.6644 | 2025-09-25 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |


[Clique aqui para ver as próximas entradas](README41.md)
