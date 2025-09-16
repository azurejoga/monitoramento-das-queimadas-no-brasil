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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b541c3e8-40d1-3e21-9c99-6d5a820ada3e | -12.62924 | -45.77079 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b3ebb677-2548-3a5f-bdc0-11aa8fb3aab8 | -10.71028 | -46.5145 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e82f5cfa-1055-3839-82ce-73ed7673dee2 | -10.72284 | -44.75146 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fe6dceec-14b8-3805-a14f-f326e797931f | -11.14094 | -45.34335 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 430f5455-0710-3e61-99dc-0b5e5b548b82 | -12.06176 | -46.56622 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac02eae5-805a-3cbf-884d-aec725486b52 | -10.71193 | -46.50385 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 84f16411-d7bb-3e38-b072-10ef9482b308 | -12.61542 | -47.98791 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa873447-c03e-33a9-bc9f-f660b641abc2 | -9.73566 | -55.37637 | 2025-09-16 04:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 086b1a93-e723-3d2b-bfcb-c3902c8bc2bc | -12.9315 | -47.96296 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5d9764e-6b41-3da4-b904-0c4b9d4eedfa | -11.23159 | -49.40582 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b6690a2-04b1-3744-b032-08a59e757bb7 | -7.69079 | -44.49461 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f440b1f-630c-355f-b2f8-c6cc234f2462 | -7.79134 | -46.1593 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37d5b9dd-1ccc-3672-bbc1-a230434e3efc | -10.7173 | -44.73938 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 585abadf-7f0a-3936-9e67-3b56f9d88e99 | -8.97212 | -44.19325 | 2025-09-16 04:29:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abfe1293-6818-3edd-807e-f3c021ea8b6f | -8.89126 | -46.18879 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5fd63f8-93b8-32bf-a52d-c32a30c34021 | -8.03468 | -49.83574 | 2025-09-16 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e523de9c-75d9-32da-bc01-45a879d0c427 | -12.60179 | -45.70514 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d4512c1-d852-3e9b-9b7f-70643fc0f1a5 | -9.18646 | -47.04331 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d77a11d-0f41-374c-a27d-b920c38df3f7 | -12.82047 | -47.22889 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37df8f67-1542-358b-b937-cf6bd7fafeef | -7.99179 | -45.65701 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c69be13-f691-39e8-a410-aff2f48b0422 | -12.1732 | -43.57566 | 2025-09-16 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8dc2ea5-b5c6-311c-8363-a2a52665f071 | -10.72075 | -44.76402 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fe4da9b-9a02-359c-9411-629e827aadd0 | -12.9541 | -47.96331 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6fda69f1-af5c-3d9e-80d9-91f95d358d88 | -10.88415 | -47.79604 | 2025-09-16 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26205e1d-d0a2-3818-b1b0-f6983502ceed | -11.10761 | -45.33032 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 139fb2b9-3099-3cab-b8fa-1cf80bed71b9 | -11.13003 | -45.3455 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ed9a5960-f71d-3cd6-bc23-70bf8986f418 | -8.83899 | -47.94611 | 2025-09-16 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 215d6797-8fa8-319e-aa55-94080c2c5e90 | -9.05008 | -44.83927 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 37b7e909-2841-30c6-80d1-189cccb87edc | -10.17961 | -45.31534 | 2025-09-16 04:29:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09890fdc-c0e1-3c6b-8f90-517b685743be | -8.42228 | -44.97906 | 2025-09-16 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 62508b78-a4eb-3989-944e-d8ee99d6426d | -12.2924 | -46.40653 | 2025-09-16 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a68e09e-9660-3973-866d-d155956356be | -12.61486 | -47.99145 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 957199a1-571b-3cbd-8c44-dc49d4f5f5b6 | -10.72169 | -44.75922 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6c971237-0c68-39bc-ae1b-2654e94bb999 | -11.07663 | -49.75397 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f599a60b-8705-3869-b8e4-acfd10a1a58f | -9.85737 | -46.45665 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04f6d2db-7fc4-3bf0-9068-4755e746f0e4 | -12.76079 | -47.9678 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e5276485-f353-3902-a5cd-338121ad0841 | -9.06741 | -47.03098 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 43f6b010-a389-35ad-8c8e-1ac75647f426 | -11.50349 | -43.70966 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac15405b-bb42-307f-b1ea-0462c085ba5f | -9.05641 | -44.8441 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2811c8c9-ff76-3f06-ae5c-0e9f1d49f147 | -8.09352 | -50.15591 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f262252-be9d-31ff-9c2f-b00ff697a445 | -11.02175 | -45.06268 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| decabdf0-77c2-3c37-8549-7d2c5b96d366 | -8.62052 | -45.72197 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e060c152-67d0-378b-a938-bc2bf944a110 | -10.71373 | -44.76291 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88cd59be-e802-3043-99a0-d6437727d0dc | -9.10938 | -46.93376 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26fa6c5e-b07a-3fd4-884c-47dc3c991ce6 | -12.77523 | -47.96292 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5a11bbc-1b54-31f1-9649-06960d8a540c | -11.13749 | -45.34281 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05fc1a0a-eadf-3bbd-afaf-b01a4c8c1dd8 | -11.96701 | -46.77864 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1112c76-48df-3332-9a73-a15d6b6c9c79 | -8.96777 | -45.76124 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 015b6106-a03b-3a55-8863-8ff6322584c2 | -7.40953 | -49.99852 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e0a719d4-52b8-3185-9a50-7848b6c4be9a | -12.64714 | -47.9604 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ef9833f-68c6-30a1-b0d1-219da2365258 | -11.43484 | -46.94196 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c879be9-bc0f-3f86-866a-ec1b9e254c4e | -11.46097 | -46.92794 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37a1fdac-e468-31de-87cc-f32c557ef2da | -11.63762 | -46.58811 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9860f837-201b-3571-9c50-1e676e86d31a | -8.04174 | -48.66581 | 2025-09-16 04:29:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b4a0e0f-72c1-3f05-a26a-3a0ee6775f45 | -12.66256 | -47.71225 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db33a55c-ebde-3f70-bc72-4721bb184a38 | -8.1404 | -43.64494 | 2025-09-16 04:29:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7788aba-acd1-369b-a243-53875704c327 | -12.04661 | -46.53068 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc0f7d5d-4bfc-345d-b53c-418f34e4a67c | -8.15466 | -43.67241 | 2025-09-16 04:29:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d1fe15f-8611-3726-a2f7-7b0dcb647149 | -8.39815 | -47.25781 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b240afc9-e07a-319b-8783-dfc79e116a9c | -12.29633 | -46.40344 | 2025-09-16 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56382df4-706d-3795-947d-bbd8c917ba30 | -12.68096 | -47.98413 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26e3a6bc-4fdf-381b-9a4d-0d67655ed791 | -12.95799 | -47.96033 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c19361ed-5335-3a64-bd2a-385d86d10be3 | -10.66609 | -48.76341 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f268b7d-d7e5-33c7-b7dc-b0b5a89aa2e1 | -11.1145 | -45.33142 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c91b2237-a238-3205-b4d9-97c684064a37 | -11.13289 | -45.32658 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c2c753a-2716-366d-ba6b-486e5cc3f9bb | -10.63727 | -48.74767 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddd21234-dd92-3c34-ba7d-b2e6727943fb | -12.6644 | -47.93778 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b0e4c14-676c-3f2d-bcbf-2262535b568d | -8.11544 | -48.27326 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1580ed5-b3a6-3a6c-99b8-89a172305d44 | -12.85114 | -47.90975 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ad6f914-4619-372b-a9c5-a428f88f7c5d | -13.20694 | -47.30561 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f22077f2-c0e5-3295-ad16-32ec92fea4f2 | -7.84175 | -43.85595 | 2025-09-16 04:29:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8171e844-8f4d-3133-990b-2dee62aa6320 | -8.90008 | -46.15403 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d42e6dc-23fb-31a2-ae22-0f12f4475e7f | -12.63371 | -48.00184 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6a3083d-81f4-3c70-b1d5-adeafccf9684 | -12.6622 | -47.93015 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 663be6fd-2c97-37d9-b80e-8b4ab153c868 | -12.79452 | -44.7423 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87b4ef29-3aab-3635-8107-8408806304c5 | -11.45374 | -46.93042 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e21ed2f-652f-3281-801b-0a5441760cf4 | -10.16062 | -46.14068 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 101d5292-83cf-3b6d-83b4-2f18eca71bba | -11.45485 | -46.92334 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f486b16-93df-3791-827a-9a5b2af24119 | -9.53977 | -46.30156 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a41d34d-eb2d-3c51-a8d5-194e5cc1d3c5 | -11.12772 | -45.33743 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31ab2f4b-84e4-3cf8-bb9c-ad4af9d0a060 | -7.73398 | -45.30315 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7db4a2e-89ae-3701-94bc-1965d387e5d3 | -8.59401 | -46.34336 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22d505ad-6ff0-36ad-8b99-02db8e190f0e | -13.02289 | -47.96008 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db706c86-6cfb-35d9-9b39-b559c8a964e6 | -8.20124 | -45.54738 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49199f23-a791-378e-93fe-b0cbb146aa13 | -11.72015 | -46.4764 | 2025-09-16 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97e9f65a-8d7c-3d96-8598-7d843b6a00ed | -11.44541 | -46.93997 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9953ed72-c81d-320f-9ae4-615bd20dc44a | -9.06464 | -47.02694 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2863803d-d4d7-390c-8fe0-7085c8ce9679 | -10.19391 | -46.15657 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b805aba0-808f-3b37-ba31-d6d47d2c7a2c | -12.84015 | -47.2025 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| defe3fde-8eda-3f35-8616-649eab200329 | -12.53715 | -45.87717 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e7b0769-f3c6-30d8-b211-b73ef3d2e6c7 | -7.67979 | -44.68086 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9c8664b-6e26-3893-9d7d-9f9060cc8438 | -8.98034 | -46.25337 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 392d2c4b-6868-3c39-aa0f-241a92a63b5b | -12.69971 | -47.7365 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2e22dfd9-47a7-334c-9e7f-fe35688a7c72 | -11.59923 | -46.96824 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 28ce8b2a-69c5-334b-ab1f-331bd31a1216 | -9.09852 | -44.85776 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 614f9f92-713b-361f-9ef3-02266d7bb699 | -7.39846 | -49.99668 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5f61e6f6-9957-3c2a-8a76-c4a8483d347f | -10.42015 | -50.64459 | 2025-09-16 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d66c2078-fa5b-3d08-b798-ce7626e53d85 | -13.00461 | -47.94617 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a1a1862-b3ca-3a9b-afd2-194a47084e7b | -11.43151 | -46.94143 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d69808f-9d4d-3d15-bec0-24ecb3774050 | -9.14543 | -46.94311 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README44.md)
