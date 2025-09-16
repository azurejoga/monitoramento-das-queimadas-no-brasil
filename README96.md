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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bdb1b5b-57fd-3631-ad29-c2bb759e2082 | -9.7322 | -47.3625 | 2025-09-16 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 225930fe-72a0-3bf3-bc41-4ff69de0d39c | -8.6696 | -46.3842 | 2025-09-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 67f0a3f6-7ac5-3588-bb9e-0895d9f3f1da | -9.7325 | -47.3403 | 2025-09-16 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 4de7d13d-5960-3ad2-9401-7de6f138ba1e | -12.4514 | -49.7111 | 2025-09-16 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 7847467d-0f50-3848-97bb-68e486628aea | -13.9458 | -44.9245 | 2025-09-16 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| cd9fc298-c30e-3c43-be4f-de8a382e1b0f | -9.7445 | -47.8468 | 2025-09-16 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 8f046db8-c300-322c-a813-30a923e05aad | -8.9731 | -46.2405 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 51e9ad63-35b6-34ef-8408-703763f7d0b7 | -11.4853 | -43.5929 | 2025-09-16 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 7d04fd52-bcb2-3aa6-a259-55e0213771ff | -10.6548 | -46.4727 | 2025-09-16 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 551eb3eb-a1e4-3cf8-a97f-7a4a41866375 | -11.0804 | -49.7456 | 2025-09-16 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 9ecd5ffd-37b0-30e0-beb5-481bf21d5ece | -13.2798 | -54.2435 | 2025-09-16 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 0feea414-3f69-3117-9857-9cc182d19c1c | -11.2737 | -50.8163 | 2025-09-16 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| fdb44491-0ac2-3d2d-8d87-57072e04965c | -6.2171 | -43.904 | 2025-09-16 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ede6d4b7-2741-3463-bea5-51429978b327 | -7.2768 | -46.6036 | 2025-09-16 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 216.3 |
| ab81da0b-207a-3428-bec8-9f11306c05b8 | -15.8624 | -59.3779 | 2025-09-16 13:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 5a00bc7a-a0ff-3038-b13b-280767c22d0f | -11.7147 | -46.8964 | 2025-09-16 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 128e37ec-ad7a-3fab-82eb-d6c955d8e445 | -9.7409 | -48.1106 | 2025-09-16 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 2c129fc0-3370-3dd5-8029-b8146670aaf2 | -9.1709 | -46.9792 | 2025-09-16 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| e21e0808-f986-3fc0-80f5-38ce058efe7c | -11.4477 | -43.5514 | 2025-09-16 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 281.2 |
| 3bbfa5ca-556b-39a7-be74-a64ec682d47f | -10.7493 | -46.5058 | 2025-09-16 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| fbeec906-b029-34e0-9c9c-84c979e787b8 | -6.6698 | -45.5118 | 2025-09-16 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 230.3 |
| c96c8c17-54d0-3890-aa6a-f9d760471b15 | -5.8088 | -43.4724 | 2025-09-16 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 76609a57-955b-37f6-9097-520defd18324 | -6.3372 | -43.1492 | 2025-09-16 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 43c353a1-7dad-321b-838b-02fecc7be00e | -7.7229 | -45.3056 | 2025-09-16 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| a6fdd2a3-57c3-3b56-a5c3-85bb3c1d533e | -7.6738 | -44.6717 | 2025-09-16 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 7b9f2b56-3496-3324-af35-7febaa2a9594 | -8.613 | -46.39 | 2025-09-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 275.9 |
| 75e7ec8c-6462-31e6-b62f-3c276c4f74f5 | -6.6696 | -45.5344 | 2025-09-16 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 6b1497fd-cbd6-34b3-842c-7046338450b6 | -8.9259 | -45.5231 | 2025-09-16 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 184.0 |
| ab5da0a7-249c-3e8c-ad9f-9c0092e21973 | -12.6352 | -45.7652 | 2025-09-16 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 201.0 |
| 3eab63a2-41af-38a5-be8c-a03180243d7d | -12.1861 | -44.0958 | 2025-09-16 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| ba766464-8783-3b38-80f5-62934950fcf3 | -8.9356 | -46.222 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 5cf74eb6-aaf5-3775-a569-a784ed570cd7 | -12.1147 | -44.8304 | 2025-09-16 13:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 613ac1df-c25f-31ad-b5f3-6b0be24e5397 | -8.5947 | -46.3471 | 2025-09-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b1c445ee-e250-3a7c-b543-71fd220ef1ba | -14.6143 | -46.3806 | 2025-09-16 13:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| a622fd66-5362-34fa-89f2-bc5cd39968e3 | -6.169 | -41.2114 | 2025-09-16 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 118.6 |
| ccdb6f87-152f-3adb-9746-dfe9fda4ffaa | -11.1299 | -45.3426 | 2025-09-16 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ce7cb33a-a637-3951-92c4-e20b7397f035 | -10.0803 | -48.1616 | 2025-09-16 13:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| e6151efd-194f-33b8-9276-aaa5ba1f4aef | -5.8809 | -45.8641 | 2025-09-16 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 4566885d-a0d8-3e58-8c33-3c7885fd676c | -5.8045 | -43.9364 | 2025-09-16 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1f7d3bf1-8e49-3623-80f9-f90231e868e3 | -11.7342 | -46.8713 | 2025-09-16 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| dea17c02-3d6d-357a-9a88-c3b224fe60e1 | -7.1505 | -47.9786 | 2025-09-16 13:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9723a665-3740-3cb0-a9be-52635a340694 | -13.2027 | -47.3126 | 2025-09-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| b2483ca7-4797-394f-aa54-3a0fdfcc9717 | -13.2224 | -47.2871 | 2025-09-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 58530db4-97a5-3deb-9117-5b6624f7284c | -9.7406 | -48.1326 | 2025-09-16 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 2c606866-873c-3f4f-9cd4-ec88e5ba49c2 | -10.7302 | -46.5082 | 2025-09-16 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 2f0dfd84-4b4b-3241-98e4-333b5e9bcfea | -7.2771 | -46.5814 | 2025-09-16 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4539391b-f6e6-3456-91c9-09a50ae31cfa | -6.9798 | -44.5529 | 2025-09-16 13:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 1c81c3ab-08ed-32d2-830a-6d00031c86b3 | -9.0677 | -44.8225 | 2025-09-16 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| e2ddd92c-b4fb-3002-b9f2-8dc2268c011c | -12.1152 | -44.8072 | 2025-09-16 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 3872f932-9da5-363c-a7cd-0e41bdcdf906 | -12.065 | -46.5323 | 2025-09-16 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a4c22286-3143-3e2a-b8dd-4efa4f05cc08 | -9.152 | -46.9812 | 2025-09-16 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 766fab0a-b751-3aa9-a06e-889ce3c1b536 | -6.337 | -43.1727 | 2025-09-16 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 0fc879eb-5c41-36bd-b262-59e5a2fdc146 | -6.1881 | -41.1855 | 2025-09-16 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| d9964768-86a4-3759-9d11-bb18310a4346 | -8.976 | -46.0152 | 2025-09-16 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| aa9f38c2-be77-3a6f-a152-b9330ca8dddf | -11.2737 | -50.8163 | 2025-09-16 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 0583ca68-5c46-3071-b2db-918570b7b9d0 | -11.0994 | -49.7434 | 2025-09-16 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 6574ad0f-d6d5-30ab-8321-b4139b1a87a8 | -14.6143 | -46.3806 | 2025-09-16 14:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 115e3c1f-7d39-3d6c-8cf8-c3d5a91dfaf3 | -7.4503 | -46.1647 | 2025-09-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 4abbfc50-7cff-313a-8ba2-f28564577f55 | -10.0611 | -48.1856 | 2025-09-16 14:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| cea9ff26-fdfb-3336-acf6-97d180137390 | -8.6696 | -46.3842 | 2025-09-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 55ca44ef-4b5d-3824-bf86-781d25439f4f | -8.9568 | -46.0398 | 2025-09-16 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 0ca12535-086f-3cd6-a2d4-815c4c03d229 | -10.0728 | -48.7086 | 2025-09-16 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 0348adb4-979f-31d3-8530-436a1fd689b3 | -7.0925 | -44.5428 | 2025-09-16 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 0eae4e98-fd20-3dff-9a4c-ccd2ab629981 | -13.2798 | -54.2435 | 2025-09-16 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 68798ffe-e2b4-3901-a41b-c2e153457a45 | -13.2224 | -47.2871 | 2025-09-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 45ebfd9d-7503-359a-ac34-16d835c33946 | -12.6356 | -45.7422 | 2025-09-16 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| f4ba500f-95c3-3a3e-98bd-ffb2a0495682 | -11.0804 | -49.7456 | 2025-09-16 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 94ef569c-b285-3d14-a06f-1da2737c35f5 | -7.676 | -44.4879 | 2025-09-16 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 276c57c1-c493-31aa-be44-3c7c1c8d6a16 | -8.6127 | -46.4124 | 2025-09-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 60452e44-23cd-3a9e-8791-73e28fd0cc41 | -14.329 | -46.0857 | 2025-09-16 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 9cbfa7a3-cae4-3387-b2fe-79d022fc07c0 | -10.9004 | -47.8027 | 2025-09-16 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 9c21979f-e68f-3227-9b39-63b6b7d4d6e2 | -10.7493 | -46.5058 | 2025-09-16 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 1f1a8153-1333-32b8-aac2-5d48b3f3468d | -3.8229 | -44.0833 | 2025-09-16 14:00:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b3322363-b066-3ffe-bdb0-c50abb6ec7cd | -12.9795 | -47.949 | 2025-09-16 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 84eaf5ad-38ac-375a-83e2-e866177acc76 | -7.5269 | -44.3644 | 2025-09-16 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| da330333-5b87-3ef0-9aed-422a61ea8c5e | -7.7229 | -45.3056 | 2025-09-16 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| eae485ee-d678-3e2c-86a5-362f2f090590 | -7.1318 | -47.9801 | 2025-09-16 14:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| aaacafdc-fa79-3024-b186-20434f960cd7 | -11.0617 | -49.7261 | 2025-09-16 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b73a2011-575c-3d25-89d3-a0d1c89f15cd | -12.1147 | -44.8304 | 2025-09-16 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 59bcdb5c-3022-3bae-98f7-92edab708cc3 | -5.7856 | -43.9609 | 2025-09-16 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b2d6f2ff-0807-3e57-a145-3d6f5f6c7fbb | -9.0857 | -44.8893 | 2025-09-16 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 483.7 |
| 143f4a9e-5aa3-3ff7-8ed0-bdfce3a39e37 | -9.0854 | -44.9123 | 2025-09-16 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 424.5 |
| 3c9b1b47-924d-34eb-887b-4c1b4d5c2a6c | -12.8392 | -47.2093 | 2025-09-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2f677aaa-edde-3701-a95e-013c758daf9d | -5.8086 | -43.4956 | 2025-09-16 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| acaee312-d8b5-3390-9448-a8883c055ba6 | -7.2581 | -46.6052 | 2025-09-16 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 20d88969-1c3b-3f4f-ae59-17bc79c1fcab | -13.7862 | -54.9512 | 2025-09-16 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| a4b89384-b7ea-35ab-9824-e0995290b722 | -11.0807 | -49.724 | 2025-09-16 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 300244c2-0767-3162-8687-55ef4543f559 | -8.8795 | -46.183 | 2025-09-16 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e664422d-28e2-32a0-b24c-140ca59d68b0 | -6.3558 | -43.1711 | 2025-09-16 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 244.4 |
| b7db621a-4043-3a00-8d60-921609fed981 | -8.5947 | -46.3471 | 2025-09-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5ee818d2-0a99-3fb4-8b7c-692a2cc5bf80 | -7.5081 | -44.3662 | 2025-09-16 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7a306649-a036-39ab-a30e-1fa47ee25bcc | -12.6352 | -45.7652 | 2025-09-16 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 8d78178b-d5e6-34b9-83a7-248e494d5888 | -8.9571 | -46.0172 | 2025-09-16 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 888be703-768b-3d19-9790-09375de0a901 | -5.7871 | -45.9155 | 2025-09-16 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f7828dc3-b5d3-37b4-95fe-114cfe39848a | -5.9942 | -43.6902 | 2025-09-16 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 60f644cb-1462-3a6f-a51e-cae130e4d407 | -9.7406 | -48.1326 | 2025-09-16 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 5d9c84ea-3af4-3c7c-8776-2b7bf1af85dd | -6.3372 | -43.1492 | 2025-09-16 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| b659a93e-5f5f-3176-a503-0f32587ebb41 | -7.6949 | -44.486 | 2025-09-16 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 11942f0f-437d-3c6a-b012-f6057fbe44f7 | -7.1692 | -47.9771 | 2025-09-16 14:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 1d3bd3c1-7d5b-34e1-a265-face0a9d2225 | -9.7325 | -47.3403 | 2025-09-16 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |


[Clique aqui para ver as próximas entradas](README97.md)
