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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a531ed73-8999-3a80-83fd-f29ba4f25357 | -9.45307 | -46.71965 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa6e953b-f33e-331d-81f3-0b745ade9f3e | -5.98304 | -43.70848 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 462b8a35-742d-3ccd-8b54-b214be32157a | -8.49812 | -44.72007 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f73dbdb-9240-3254-93e2-3011529c727d | -3.37406 | -44.20131 | 2025-09-10 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e4f3cd9-b16b-3ca3-87d2-30a83bfa47f7 | -8.52221 | -45.7098 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4f1efc32-3fc6-3237-8c69-26231e93a363 | -6.39004 | -44.42979 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20317420-94b1-3a61-aa60-c0c92f381666 | -6.3057 | -43.32446 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3da137a-9391-3621-aa20-6a1fd720a245 | -8.43135 | -49.11747 | 2025-09-10 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15c8b87c-4738-3db1-98eb-24d1c4d8f0b1 | -5.59181 | -42.90768 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ab4fb96-e277-37f8-8093-aac4fb0b8687 | -9.439 | -46.71706 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 42ce1c72-db87-30fa-bcfa-d63ed3e510ec | -7.19369 | -44.899 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd030dc2-e476-3d32-bf32-fc169c6433ef | -8.07049 | -50.18843 | 2025-09-10 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 55fc12b0-2bb6-3242-b5e5-09869b791add | -9.07719 | -46.96952 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8a67c84-b239-3c91-b314-939b8f3bce53 | -6.34939 | -43.65304 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5299c5f2-fb3c-380a-89a7-b0d25731539d | -5.73161 | -45.28122 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e64ede8-1b19-31f7-993f-23dfef3a0a0f | -6.09647 | -44.777 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdc3b42b-52a4-3c30-a85d-1362cb54f162 | -4.72813 | -44.45734 | 2025-09-10 04:14:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ed08e58-920a-3c71-9124-af4c9597f7d5 | -7.38676 | -44.83796 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb9d2875-87d5-3f10-ab9b-7cb2b7a857ef | -5.40315 | -48.85093 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57d31e91-f9b9-3f79-9470-f05e4bff13e2 | -8.04881 | -48.68568 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 7ee0bd0f-dbe8-3ad3-8907-d09d0497ec06 | -5.93662 | -45.81961 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65aa6fce-9043-31ac-a147-8b1c919f026b | -7.10682 | -50.76328 | 2025-09-10 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc936085-0d65-3f5b-a38a-31858b5ce9d2 | -9.71435 | -46.83096 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67be167f-eb4b-369d-b449-292dac84da91 | -7.13678 | -44.50587 | 2025-09-10 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4214581-7b1f-35c0-a6e3-9dbe0eef4166 | -9.82824 | -46.04232 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f2f68a3-fed1-3dd1-9f8d-704ed4e0be59 | -8.06707 | -50.18855 | 2025-09-10 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 62eba01c-7738-3d82-a6a5-59c692e84d80 | -5.67034 | -43.90118 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ba39103-f929-351e-9d9d-5f397ffa9525 | -9.01144 | -49.54112 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e9083f3-5c1c-3bb9-a382-ab75b2ba3403 | -7.55878 | -44.65669 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb99c98d-2f3a-3dcb-ac69-a1df15be66ab | -9.31528 | -46.71825 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3810b2bf-6b9d-3441-aa68-a8dfc73c56c2 | -6.34055 | -47.09661 | 2025-09-10 04:14:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f0fce0a2-b610-3809-bee5-899d2465a6fb | -5.74458 | -47.47976 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b646c4fa-5bb7-37a5-ac90-51b0beb6f0e0 | -9.43968 | -46.71296 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 16c6aa2e-57c6-3f04-b23a-6605aa778348 | -8.26133 | -49.92781 | 2025-09-10 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b16fd50-c652-3f18-aa31-398dd843828e | -6.66388 | -44.54648 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c466383-f95a-37c5-af98-160b382c72b6 | -7.35561 | -44.30582 | 2025-09-10 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 535f05da-847d-30d6-a240-cbfd02ade9e2 | -9.60684 | -45.762 | 2025-09-10 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8bd08ba-3a1d-3ec3-bfe8-2098a6cf120f | -6.38553 | -44.45825 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfac33c8-09da-3d61-bc6f-aedf5d58d239 | -8.47764 | -47.2968 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0db821c0-ceae-3926-9884-36fbc52a4e40 | -8.67101 | -45.74493 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 647cebe3-1692-376f-a920-a00771296867 | -6.68684 | -51.41395 | 2025-09-10 04:14:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4beb0c0a-e0e4-3a9a-9b00-5d0cfb91b2d6 | -5.23757 | -43.45148 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eb75dc7-35a5-3c1e-aa70-78b72ca3aed8 | -6.20829 | -45.61706 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e97cb6a9-66c6-3926-b703-3eca946fee84 | -9.10006 | -46.98712 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3c6accb7-9c9e-3427-8526-1313a2b4348f | -5.20722 | -43.7095 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d531418f-b0a0-3867-a417-2c24113d49ac | -9.21559 | -50.53509 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ea4bc95-e232-3c74-8090-26862f59e48b | -6.86142 | -47.93666 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aab48513-c0b2-3756-a21b-c6d676487b78 | -6.4247 | -44.48665 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d89f8dd8-0c75-3145-b040-59b6ec034b46 | -9.0739 | -45.70994 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a56d6dc-d448-3557-9dc3-0cbc78125033 | -6.20886 | -43.5277 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe530549-e7b9-302a-80ad-c5f73a7e0af6 | -9.06344 | -45.73124 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d97fef6d-9078-3c9b-8562-d286c2279c49 | -9.06003 | -45.73068 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b48ac610-ee45-3566-a4fc-81c28a864da5 | -4.8387 | -45.35427 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a80e021-73b3-33f0-b16c-f8761c8c1c5d | -5.20421 | -45.43386 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7b9f1ed-3f75-36dd-b030-0ab267f512d3 | -9.21643 | -50.5472 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bddece3f-6de5-3c73-b1d4-d7914e801e87 | -7.4931 | -48.23138 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ce3150f-419a-3d4c-9066-16dcf8579a6c | -7.85387 | -46.01783 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b15af1a-6f2e-3dfb-9799-f6017aa59269 | -5.53067 | -44.33393 | 2025-09-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9da873ea-d91e-3af8-8d4a-293b3f2ca44f | -7.55935 | -44.65315 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7284b0b1-622d-3caf-b295-9a2d57d72140 | -6.68341 | -44.55317 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3326a71-a0a6-3713-ab59-680a7268b696 | -7.83967 | -45.40969 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b5a436c-1fd0-36dc-981e-44f8e93cd82c | -6.06915 | -43.31499 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 35b9bf67-afbd-34e4-9e2c-3922f122ad31 | -8.4092 | -49.09869 | 2025-09-10 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca99ec07-4aad-310e-8efa-a2aba59002ce | -8.71116 | -45.30159 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f79bf52-12b3-368b-91d5-0fe3c995b1a9 | -6.58872 | -44.01145 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da2f1c45-6c72-3635-9eb7-b7f325bfb05d | -6.20767 | -45.62095 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e191dbef-e69b-396c-91bd-236f909ff244 | -8.34563 | -45.05767 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55f2770e-ee0b-3792-a7e8-9c9f1331d9c0 | -6.84669 | -44.91758 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8dad84e1-b6d8-3134-85bf-afa463af5736 | -5.10314 | -43.04916 | 2025-09-10 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69aa6298-d1cf-3ff9-907d-b0375004439e | -7.46511 | -44.94256 | 2025-09-10 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8fb711c-95cb-3caa-aedf-c0cec0353117 | -6.40845 | -44.40002 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df67b8c8-16d0-3731-a876-32a3dafc8e5c | -6.02862 | -43.65884 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6742e4e8-e9c3-3769-879e-3ad297756a9b | -8.85024 | -47.26993 | 2025-09-10 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caf985d1-e3ff-3eb4-85d4-e5b104ad87a1 | -5.93748 | -42.78566 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3ef11816-2a67-35bd-b1e2-156b95e07828 | -9.0699 | -45.71307 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02029935-6b64-38ff-b568-c725399929b3 | -2.34869 | -47.59118 | 2025-09-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a283b3c-d4ae-30f3-bd01-297d6c6360ab | -5.44608 | -42.79319 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f84af7fe-84ed-37af-944f-43e72cedd20e | -6.44342 | -44.04879 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b3b0f46-480e-3f8a-a39c-2176767cf5c6 | -5.71335 | -45.41882 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54b3bef8-737a-3d7b-b787-265b9645a1b6 | -8.37767 | -45.00776 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4641398b-77ee-31e7-812f-0de1e31d99b6 | -7.84307 | -45.41021 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5f0c557-9271-34ff-8601-4f26a8cd64a6 | -5.67416 | -43.35836 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0915fab6-c0fa-3a41-bcaf-78e7cfbd1dfc | -6.38301 | -42.54313 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16304126-80fe-3a96-9e1c-f91823a8f99a | -5.58006 | -45.04165 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1b390b4e-55d8-3e9f-9968-e20b48fbe661 | -7.31191 | -44.15183 | 2025-09-10 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 439bd764-0b52-349b-8928-c498ad802227 | -6.19763 | -42.46799 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 506102c8-a390-303d-9a5a-e4e707135388 | -6.82708 | -44.88865 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da5b3c9c-1a41-3e60-8152-46f7915a8be5 | -5.41524 | -43.44801 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d97c396-2ac1-3b26-bde6-6fa3a56f39cd | -6.28728 | -44.21793 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78386f3f-dad8-3bae-ad0b-d266189a44ca | -5.75083 | -47.46594 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdda9926-829c-3a5a-ac1c-cc27f7fc8872 | -5.89225 | -43.42089 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 236f031a-6a17-3408-905e-da0f74800f09 | -9.46318 | -46.43224 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3dee96b-9183-3565-85d8-15c0685d34b4 | -5.67302 | -43.34406 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6d5ed5b-c8d2-3453-8631-abcfb4a3e3d1 | -7.78623 | -46.0947 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0f230fd-6ee8-30c8-bcea-5f1eaea35387 | -8.99708 | -46.07222 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46b6ff38-2a1e-3990-aa94-862f66a796c1 | -6.17493 | -43.37754 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aaef2d7e-5429-3c12-b930-cbdb825f32e7 | -6.19944 | -43.50148 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7b539d72-2c73-396c-973c-4e997b36af86 | -6.54588 | -43.72364 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 519252e4-f38c-3ea6-a832-e76dd1336545 | -7.71239 | -44.78008 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 544a2721-c5b5-3815-99a3-fbbcd062e2ee | -6.39674 | -42.60978 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README26.md)
