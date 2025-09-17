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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b3a9516-e434-3c84-b81a-99d056b19f00 | -8.98586 | -46.26831 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc842583-b018-3255-b777-ee21107e6155 | -7.06395 | -44.34493 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 162c46a6-1f14-3d9f-8038-2c34184d693a | -8.62688 | -46.4458 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c52704c6-6771-348f-b403-bedcfa3898c4 | -5.78364 | -43.91191 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e12bbc7-a4c7-3ebb-af42-16305b19b0b7 | -8.96945 | -46.33632 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d1f9a0b-887d-3e4a-88fd-8e5423dbc5b3 | -6.42163 | -43.60064 | 2025-09-17 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20bd23ce-8b0e-3ce3-a8ff-8d23d506fba9 | -10.943 | -45.50065 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9435efe0-582a-3dc6-979e-92e72fa6dd1f | -5.7719 | -45.90825 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 32791803-bba5-37b6-b1c3-cf4c58ee6a0d | -5.2193 | -45.42564 | 2025-09-17 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f41075a7-a86c-34df-b7d9-d5c97637083e | -8.89589 | -46.1456 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f5faad1-a444-3e0f-9eea-7d97dbe48592 | -5.78323 | -43.75916 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cde199a4-91ad-3431-a986-91a3bc61b0d2 | -9.00814 | -49.7807 | 2025-09-17 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b6315877-f209-34f8-95fa-3adf3a4eec6b | -5.20851 | -45.18269 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3c9f635-630a-3aa2-a9d3-4a653f0f533b | -5.21652 | -42.31956 | 2025-09-17 04:32:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c4b7ee4-bf11-39d9-84c6-3299c1fa3197 | -9.1495 | -46.94273 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f3e1255-535c-377a-a1ef-b62916d73772 | -6.61662 | -45.60455 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1fc52d8-3ef4-3ba7-bb1b-793ab0a4e986 | -6.6091 | -45.5839 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 019fa00a-299b-347f-83ab-8733ee261ffc | -7.67744 | -46.63296 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98934fe9-f16f-3886-be20-8b5836119b9e | -10.62849 | -48.76087 | 2025-09-17 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e169f8e0-a9bb-35ae-9944-d009c91050a0 | -7.33765 | -44.58526 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4c7eefd-cf66-307a-81d7-a694c04f9a24 | -9.07265 | -44.94728 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca2faf45-3652-3240-a0ba-b35ffb12f884 | -6.42804 | -44.37563 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d9b3b2d-7a2b-3878-9df1-08887ffe2b2a | -6.17993 | -41.22124 | 2025-09-17 04:32:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f1790e5-1e3b-355b-b195-2718d2faefcd | -9.59663 | -45.6613 | 2025-09-17 04:32:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75c3102c-203e-30e6-b76e-d05492a076d0 | -8.65829 | -46.40077 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98790e21-58d8-3294-a434-b131d0673ec7 | -9.08797 | -46.93005 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e088ae25-1b68-3b7d-be12-4e8b34a79fd3 | -6.2013 | -45.12341 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 65fd983e-83e5-3eda-becc-080b7ab59922 | -5.628 | -44.82842 | 2025-09-17 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3fa537dd-b2b0-306c-874d-fb2b4abf949c | -8.24937 | -47.58445 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a47a3b3-b5d7-3fe1-9b5e-6cc41ebaba11 | -5.9254 | -43.22342 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 174e0916-e14e-3791-80be-6321c2878ac4 | -7.5765 | -44.58744 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 66bcf776-6479-3e92-a505-21bfb703cd7f | -9.876 | -46.44645 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6e57b0b-fbc9-330e-89fd-487be0b33605 | -6.39532 | -43.34753 | 2025-09-17 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3251daeb-dd04-3e56-87ea-c42622b0e342 | -5.7847 | -43.93043 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1aa9061a-5174-3622-85b9-84d17e4f5699 | -7.68026 | -46.6371 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bcb7412-2980-35b2-81bd-4b802de7b573 | -9.85814 | -46.44769 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1a0d5e2-b19d-3ebc-9594-0a5976d35760 | -3.43768 | -49.13223 | 2025-09-17 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a01fbb62-5c5d-3b0c-af37-04f6fc0c76fb | -9.0932 | -50.52821 | 2025-09-17 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2db52731-8e06-3619-8335-a7adf66e229d | -5.76906 | -45.90405 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c8f4386b-7ae2-31d1-8c67-3abcfed52e2e | -6.10306 | -45.94283 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6e1a1ab-7057-399c-b4d9-0fad2cafc536 | -6.97928 | -44.45759 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 943bd8ea-3e08-383d-b275-881f8a3e5a3e | -9.06112 | -44.8738 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d76d731-f1fc-367e-8293-ea9797a4400e | -8.43494 | -50.04747 | 2025-09-17 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88dff3e6-625a-3ffa-817a-17c66a5b3378 | -8.98054 | -46.26418 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b83320c-a27a-35b0-8750-80bfa985c60f | -7.47889 | -46.10321 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5ee6b42-033a-3118-a2fc-b849d361904c | -6.10267 | -45.94284 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2ea93c0-006a-3e2d-aadc-cd8f39e4b7cd | -5.32759 | -44.99711 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4302b11-da4f-3b77-870b-a7ff977a00f3 | -11.50763 | -43.63193 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f16461b6-8b6a-32f8-9a07-6b4d3571cc83 | -6.44458 | -44.51272 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12eeec85-e14a-314c-abcf-cf2cb018422d | -7.99602 | -45.68619 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ea29898-7e44-3ddb-a883-f0d15b53f4e9 | -7.85806 | -48.17459 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d16eedcf-6837-3db5-ad9d-f466ff57508c | -8.27333 | -49.7883 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f520ba66-c29c-37c7-a1f2-f9aa94c31289 | -10.47498 | -45.15269 | 2025-09-17 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36fa6faf-02d5-3af4-8924-5dcf3f22a827 | -6.5257 | -41.81717 | 2025-09-17 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 078e7c2f-8f92-38e9-827a-0559cd526c40 | -5.80068 | -45.92744 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 214a41cd-06aa-32cb-921d-87bce81b23c1 | -10.41997 | -50.65409 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e24a9c0-9e1b-3e01-9275-119678d741ce | -7.26543 | -46.60038 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1f9d08c-b987-3415-8eae-4431e9a48401 | -8.08602 | -50.16602 | 2025-09-17 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b729ea2-1711-38af-8dff-fbab2dea6e02 | -6.97583 | -44.53197 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb13b5d3-62eb-3ad4-8c6c-7dc1f66bb2ea | -10.34211 | -48.83272 | 2025-09-17 04:32:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 580387f3-35c6-37e4-8cfa-e20c5f7dca07 | -9.06161 | -46.57969 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3f3ba7e-ae47-38a4-829f-b23186286b8d | -7.58346 | -44.56625 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d953304f-00c9-36ff-8ed1-de536e3f7054 | -7.68703 | -44.47262 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 032350cd-2277-3d66-b66e-f25ec0f0cada | -6.86365 | -45.61721 | 2025-09-17 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84faa4a6-6387-32f3-9ea5-7245479a9afe | -5.65898 | -45.05291 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca3ab0e5-e1d4-3bb7-80e5-c37cd1faa9ba | -11.01709 | -48.92391 | 2025-09-17 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d220764a-7a56-3cf1-9758-c4a244afa472 | -6.61373 | -45.60019 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ad07b44-d72d-3041-beb4-13ed6bbf42fa | -6.61903 | -44.74651 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97d093e1-ba06-349a-a35a-bbfffd5c7526 | -10.67703 | -46.52128 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8936b3b3-c988-38dd-9eb7-665aee39615b | -11.47014 | -43.56963 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f74eddf-82ba-3d4a-a949-d80ebc42fe88 | -7.39969 | -50.00801 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9489352-4325-3941-8c30-257e87efce40 | -4.10673 | -48.73913 | 2025-09-17 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b6e7dc2-6bab-3f24-94b4-306f55fa72ae | -9.07855 | -50.31778 | 2025-09-17 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 118d564b-02ec-3f80-adb7-455f10a6e1dd | -10.62959 | -48.75387 | 2025-09-17 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d578ac7a-1290-3cbe-89d5-8f8b9738410d | -6.17867 | -41.23005 | 2025-09-17 04:32:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 774b18fd-30b2-3db1-8dad-1ac9ad35b5e7 | -6.39771 | -43.33501 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ce8401a2-a61a-30ac-a73c-75fceaf5bab9 | -6.92269 | -44.91546 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a867368-27a2-38a6-a63d-8188fb7092aa | -5.6631 | -45.04951 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc68eeed-44ab-3c34-b23d-a5b7dc1d3722 | -5.78297 | -43.91639 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 703572c0-c099-3d2d-a789-ad743b16b0b3 | -7.6561 | -44.47683 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 325f740e-b7eb-3d37-ab79-a716b9257275 | -6.41316 | -42.6557 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8d1c3cc6-d16c-3b25-8bfc-8d7c68a80a9d | -3.69211 | -49.55334 | 2025-09-17 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7edfebfb-53b0-3c04-b202-17422c98b613 | -8.56927 | -46.3643 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f24e3966-14f5-33ff-904f-fb67a4c50b83 | -5.77823 | -49.79912 | 2025-09-17 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f8b1293-88fb-3820-9be7-f8733507d915 | -7.58582 | -44.57552 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e76603ae-0c71-3ea7-bc91-ab9326a648d2 | -6.81032 | -45.61727 | 2025-09-17 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c074adc4-9631-3825-84e9-f9747702cd0a | -9.59307 | -45.66074 | 2025-09-17 04:32:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb6cddf9-d968-34a8-8c63-a715daba29f1 | -7.07633 | -44.55854 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34c768c3-f085-38f8-8957-88d2cf864581 | -3.59898 | -49.45768 | 2025-09-17 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 958ca865-d75f-306f-ae65-17c9c4c369fb | -10.94345 | -45.49941 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe3996a7-42df-37ae-a402-ad4218a3a720 | -10.40251 | -50.63206 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaadfec1-b33b-3ddf-a605-1a2d4e880d73 | -4.68081 | -50.84185 | 2025-09-17 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14c749c2-c0d1-3a25-b11a-faf19763f622 | -10.67762 | -46.51744 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0c79a82-0484-35e8-a053-9259eb11b2ed | -7.6283 | -44.46967 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ac193eb-e7e0-35e2-a666-a5abb1956149 | -9.15524 | -47.01788 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c716b79-aa5d-3439-9003-18903f6d1fc0 | -3.69123 | -49.01668 | 2025-09-17 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83dcbfb6-9e69-394e-beed-a8b1cd86a829 | -5.53151 | -42.18289 | 2025-09-17 04:32:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9d8beb2c-2903-3ad5-ae0b-e6d622b5a462 | -7.26428 | -46.58556 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98926ea5-6e21-30ef-9f73-a27e9afe18b0 | -5.6307 | -51.71249 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a83bd304-8d66-3bc7-8cc8-91cd94f898e4 | -9.86562 | -46.44493 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README35.md)
