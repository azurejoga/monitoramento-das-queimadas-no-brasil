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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa12731b-11bc-375d-8ed6-948a7f18dbd1 | -13.3192 | -51.6626 | 2026-09-12 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.7 |
| b16a3833-abd0-3823-99ea-230416ccb712 | -8.2203 | -55.2427 | 2026-09-12 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| b8f737fe-967e-3a8c-821e-0af93f2d1472 | -10.2933 | -45.2702 | 2026-09-12 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| d8073144-9179-3663-be5b-b40fd7a423b1 | -7.4595 | -42.1199 | 2026-09-12 14:50:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 20c4cb4f-f38c-36ab-988a-21429efbffcb | -8.0934 | -54.8488 | 2026-09-12 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4e8a4a0e-9160-3590-bdb2-c1b8316be0ed | -2.7331 | -57.6465 | 2026-09-12 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 35947d14-2f9e-37ce-8c4b-aa8e57dba12b | -7.5924 | -45.2044 | 2026-09-12 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 198.5 |
| cc7e68bd-2d9e-3390-b4f3-f72978082519 | -10.7015 | -54.1663 | 2026-09-12 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 222.8 |
| daabfd03-4c49-3aa1-85a6-64faaac84359 | -6.5191 | -47.5895 | 2026-09-12 15:00:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 17dc407e-277f-3be9-8e31-ea8073a7b594 | -6.5002 | -47.6128 | 2026-09-12 15:00:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 8cf99435-0097-3ca0-b6db-2ea0c827a53d | -10.2933 | -45.2702 | 2026-09-12 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 509.9 |
| 15cd092b-ac13-3bca-be9b-7d9dde6d703e | -7.12 | -42.107 | 2026-09-12 15:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 131.7 |
| 4ad181f4-5d44-37d0-bfee-0b55af75b8dc | -6.1046 | -55.6367 | 2026-09-12 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e7eee8bb-4c6e-311a-94e4-4edff202f0fd | -2.6785 | -57.5115 | 2026-09-12 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9ada71fe-29ad-3ea7-b43e-0789b9e1667b | -8.0427 | -43.7798 | 2026-09-12 15:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 5a65aa76-4c54-3177-a173-9cb53a28b6bc | -7.6008 | -46.1288 | 2026-09-12 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 91427a74-6ad3-3269-9fcd-3eafd071d105 | -5.8491 | -49.7662 | 2026-09-12 15:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| dd99aaef-ab1e-3bd1-a9d6-a324e4a099ca | -12.0468 | -49.956 | 2026-09-12 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 06382332-ecc6-3f04-b134-6398bc73c80f | -8.2203 | -55.2427 | 2026-09-12 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b576f0ff-1018-3fa3-9772-7fdbde6c0897 | -3.5953 | -44.8019 | 2026-09-12 15:00:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 27a79960-0d65-3d53-bff0-40c8d56d4d52 | -13.3953 | -51.6956 | 2026-09-12 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 8b14c348-3203-3bb7-9f65-e0332d481220 | -2.7331 | -57.6465 | 2026-09-12 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| c71a0445-deb0-30b2-bcd5-dffd54498545 | -2.7149 | -57.608 | 2026-09-12 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 18ff93d8-3ec2-3005-8149-894c8433281e | -11.4017 | -43.982 | 2026-09-12 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 49746498-a6c0-321c-b419-91f15cc44950 | -12.1388 | -48.9672 | 2026-09-12 15:00:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 8b0fe391-8c3a-3930-b8c8-d5b0a02ef6a3 | -8.7943 | -46.9514 | 2026-09-12 15:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0493b32e-f7ac-31fb-9a9e-628326f9d9e1 | -8.1124 | -54.8073 | 2026-09-12 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 2fc8b62a-bcd7-3819-a391-b2d187bd415e | -2.7331 | -57.6271 | 2026-09-12 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| df5c60bd-82f0-3030-a4d3-e48769c11a71 | -7.5924 | -45.2044 | 2026-09-12 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 83177388-110e-3fd2-99fc-56a150ce24c7 | -2.7148 | -57.6469 | 2026-09-12 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f06235f0-d9e1-3558-8d57-79660be50532 | -10.2171 | -45.2799 | 2026-09-12 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 251a56b5-218a-361e-8512-0d0ec985801d | -8.5415 | -54.7187 | 2026-09-12 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| eff7d3be-9c20-3b44-8763-cdc7c539e137 | -7.9645 | -43.9971 | 2026-09-12 15:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 69702d8a-8ead-38f6-855f-b6e452cd8d47 | -10.2926 | -45.3161 | 2026-09-12 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 343.7 |
| 3259cecc-b5c5-329d-81ed-4b07ded4e8f0 | -8.043 | -43.7565 | 2026-09-12 15:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 168.0 |
| 790c862b-d24f-3a24-a8f1-a893751d7545 | -11.383 | -43.9614 | 2026-09-12 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| aa3bcf36-0d49-3109-95a1-32ead826e1e7 | -10.2739 | -45.2956 | 2026-09-12 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 6c0392c5-7427-3bd0-9f12-4869d57694f3 | -9.7047 | -58.1639 | 2026-09-12 15:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 1dc77808-82ea-3d3a-9f8a-d78ea3ed8047 | -11.0839 | -50.8368 | 2026-09-12 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 6657a679-657e-3ade-8645-c30c156e2ef4 | -8.8132 | -46.9495 | 2026-09-12 15:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 956454df-c6d7-35ef-a5fd-7126064fe623 | -10.6829 | -54.1475 | 2026-09-12 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 35039ab1-eeba-31e4-8dfb-2970128b1ef7 | -3.3504 | -59.4274 | 2026-09-12 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| ef6eb853-2479-3048-a0fa-74ce6f9adbfb | -8.0936 | -54.8286 | 2026-09-12 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| dc3a23c1-bf10-3a1e-990d-4390185e71ae | -6.1993 | -55.2739 | 2026-09-12 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8274ebfc-8e8f-3529-bddc-a7f27ca55180 | -11.3825 | -43.9849 | 2026-09-12 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| c10a4c88-7e33-328e-b739-a30f3237fb7f | -6.7832 | -59.4401 | 2026-09-12 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 206a7d31-a735-3e45-a135-d9fa30f0e506 | -6.7648 | -59.4408 | 2026-09-12 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| da79754c-113e-3724-ae9f-9bf3a40c0cd7 | -10.2206 | -50.373 | 2026-09-12 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| b8cf3676-d49c-308d-96d9-cc0e3fac787b | -10.9491 | -48.3474 | 2026-09-12 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 3d6cd43a-1f6a-3792-8701-d09f206faf59 | -5.1254 | -55.9748 | 2026-09-12 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c1e86cf9-c2db-33f6-9872-f952bff710da | -2.7148 | -57.6274 | 2026-09-12 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 356fae5d-37c5-3d8e-bf1e-c128500036e8 | -6.5004 | -47.5909 | 2026-09-12 15:00:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| d3287b87-d164-3b39-8590-5027a764b47f | -10.6827 | -54.1679 | 2026-09-12 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 212.1 |
| 9343fa1d-30c6-3606-b051-466cdda241b3 | -9.6755 | -46.0047 | 2026-09-12 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ec464222-ce96-3e7d-8e5c-80675916a1bf | -8.5417 | -54.6985 | 2026-09-12 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| cc17a9d1-ca4d-380f-8c62-f56435976bc6 | -7.2147 | -43.7001 | 2026-09-12 15:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| c2ce5688-5934-3c6c-a9f1-9af29f501a65 | -8.1126 | -54.7871 | 2026-09-12 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 21b7852e-6cb4-3d17-90b6-5bab12c41f44 | -5.1439 | -55.9543 | 2026-09-12 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 4b0d0020-5dd0-3fcb-a7c3-996b1ec3f90c | -10.2735 | -45.3185 | 2026-09-12 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 8a2de26e-af85-315d-8b6f-4c3757bfe073 | -2.7148 | -57.6274 | 2026-09-12 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 4725b8f8-836c-3309-b8e5-e6c8be4d257d | -6.5002 | -47.6128 | 2026-09-12 15:10:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 23eb55bd-6587-3005-a036-c9eb90549270 | -11.383 | -43.9614 | 2026-09-12 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 250436c4-6a71-3f2b-a46c-e78f074d9f4e | -6.1993 | -55.2739 | 2026-09-12 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2e8924d4-09d1-3a1f-91a3-7346288f8440 | -5.1438 | -55.9741 | 2026-09-12 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 09784374-50aa-33c9-8145-9971adb56baa | -2.7149 | -57.608 | 2026-09-12 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 83b3f4be-1546-317d-aab2-7f56905fdcfa | -2.6785 | -57.5115 | 2026-09-12 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 015db679-17e0-3757-b493-787d9b9200f9 | -10.2929 | -45.2932 | 2026-09-12 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 188.7 |
| b52d9ec3-3828-3088-ac6b-4b5ef0020469 | -3.3504 | -59.4465 | 2026-09-12 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a9ec14ec-d62e-3778-ad27-df5293dbafcb | -7.1389 | -42.1051 | 2026-09-12 15:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 120.5 |
| 08bdfa7f-8ff2-386c-9957-3cdcde216395 | -10.6413 | -46.1133 | 2026-09-12 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 8d5f53a4-88b0-30e6-9d86-198378775d6e | -6.1046 | -55.6367 | 2026-09-12 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d733706c-8499-362a-be8d-d5704950f895 | -7.2147 | -43.7001 | 2026-09-12 15:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 177dba8c-49a4-3819-add4-586cd8463c03 | -8.5229 | -54.72 | 2026-09-12 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 7131de31-0c1f-38d0-a9df-e46cc3dc6946 | -13.4696 | -48.4994 | 2026-09-12 15:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 845739eb-33dc-3f01-8b86-6bc47a10ecb4 | -9.7892 | -43.4564 | 2026-09-12 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 206f7e22-c0e3-3090-ad9d-deeb8db2591c | -8.043 | -43.7565 | 2026-09-12 15:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 7ee650f9-707b-35e6-b0d5-2ea0321baeb9 | -10.2171 | -45.2799 | 2026-09-12 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 01fd1c5a-e7bb-3003-9d23-75769eb9144e | -8.5417 | -54.6985 | 2026-09-12 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| ad3446bc-245c-3b57-899b-f2308c2e5739 | -8.1124 | -54.8073 | 2026-09-12 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 7d17ba86-a012-3b99-ade6-a3ade13be581 | -3.3504 | -59.4274 | 2026-09-12 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 697f40ea-cb46-3afa-850c-5db6f75d8c29 | -13.3192 | -51.6626 | 2026-09-12 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| bd8b1607-c41a-322f-af4d-75b217cf2bb9 | -8.8132 | -46.9495 | 2026-09-12 15:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9702f5e6-f2df-3cab-b127-18e5ffd57de6 | -10.2735 | -45.3185 | 2026-09-12 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 153883c6-a5da-3182-bf1d-6632a8e7fcb9 | -7.5736 | -45.2062 | 2026-09-12 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 254546e7-ee60-332e-a995-59c58e95ecef | -10.5473 | -51.379 | 2026-09-12 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| bc29e744-86c4-32c6-8b5e-fad60cb38738 | -11.3513 | -45.7922 | 2026-09-12 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 54e0bb83-8d05-380c-8036-0f0d8bc3c11b | -6.1845 | -57.72 | 2026-09-12 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| be16d18e-e083-31c0-a611-270402a20472 | -5.2023 | -49.3348 | 2026-09-12 15:10:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 43c24309-db70-3bf6-a07e-0ffa01780eb8 | -7.5924 | -45.2044 | 2026-09-12 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 154.3 |
| e2851589-fef7-36b0-891f-348fb4617efb | -10.2206 | -50.373 | 2026-09-12 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 177.2 |
| d4b07339-422e-340b-a3fb-bda06ac902d6 | -10.6829 | -54.1475 | 2026-09-12 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 3b8bbd26-3661-3fa4-ae77-c85045ed8d1a | -10.9491 | -48.3474 | 2026-09-12 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| e86adeb4-3d98-3125-83b0-4dda0eed73ef | -5.1254 | -55.9748 | 2026-09-12 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| dcb3373c-9dec-32e9-a384-d9e278e63cc6 | -6.1844 | -57.7395 | 2026-09-12 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c93f779b-ecff-3a40-83d8-55f1f30e03d3 | -6.5189 | -47.6114 | 2026-09-12 15:10:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d1e249d1-ccae-319b-bba9-e1e0b147a44b | -12.0468 | -49.956 | 2026-09-12 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 3d60346a-076b-3f50-8bfe-2da56a203f93 | -9.7896 | -43.4329 | 2026-09-12 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 327c3b07-2837-31db-8fda-ba47d7fcdfe6 | -9.6755 | -46.0047 | 2026-09-12 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| dc28a71e-a343-3a82-a210-b0c0ed6c07dc | -10.2926 | -45.3161 | 2026-09-12 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 693d35f1-3e2f-3663-8010-655244ccde4b | -10.2746 | -45.2497 | 2026-09-12 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |


[Clique aqui para ver as próximas entradas](README64.md)
