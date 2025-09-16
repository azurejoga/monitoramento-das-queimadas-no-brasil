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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e42156b-8117-360d-b93a-42327cbf3269 | -4.91746 | -48.26267 | 2025-09-16 04:27:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3561868c-6b6c-3e53-be3b-67af0beeb4a3 | -5.92472 | -45.8297 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab123163-5fbe-3ec4-975a-48e9337255d0 | -4.17624 | -48.57031 | 2025-09-16 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dcbb270-ae9d-30b1-8d83-89f88c2005ee | -7.26777 | -46.60449 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01bf8ada-b3f1-3d79-b789-8251eec3d169 | -5.77677 | -45.89216 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0295f17a-e530-3ad1-b798-1bf0efbc711f | -7.27109 | -46.60502 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 877dc2ac-f425-3943-a2a8-dd373ce1df0c | -5.95347 | -45.1964 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a39fbc97-1f1d-383f-bec8-de56a200f9bf | -6.61688 | -44.07937 | 2025-09-16 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03abb8af-c1e7-3462-82f9-48817ebbe858 | -6.68598 | -46.30595 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dca35f09-a7f9-35c5-a5f6-38c3e4873417 | -5.07366 | -41.17231 | 2025-09-16 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2cf850d6-1b80-3bf8-b4d4-33edde4d1f9c | -4.79435 | -49.54507 | 2025-09-16 04:27:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ebc76d6a-b0de-3498-b2e4-623351f6a853 | -3.80664 | -41.57315 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c22a0b1f-d768-380d-9084-2891a7f8f80c | -5.74252 | -43.92801 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a40bc325-d1a8-38a8-a563-0d170b14e772 | -6.62235 | -44.72993 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfeedbb0-b924-3e3e-9d92-8d1cc9f092a4 | -3.81404 | -41.5503 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7aad0dc6-7fe2-3b90-b1c1-fc3b766ec511 | -7.33434 | -44.59159 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f119bade-14cf-3b0b-a5cd-4c10024ee557 | -3.00202 | -47.45231 | 2025-09-16 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9c2bc10-4868-30ee-b932-ee6042ac510e | -3.40354 | -46.90466 | 2025-09-16 04:27:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e1592b29-0b81-38ab-8240-42748667ee35 | -6.14195 | -41.20211 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0558bb94-0b6a-398a-bda2-0d38ae0f705c | -6.9265 | -44.77235 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95eebf67-2f90-31e2-a4d9-a09eb13eb5de | -6.96831 | -44.57131 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11a7812b-4b68-343e-b9b7-d88dea501f92 | -2.57108 | -48.39375 | 2025-09-16 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c3188b2-0966-31c5-b7af-227b44126b3f | -5.34488 | -44.82651 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ffd037f-85b7-3638-b9f8-e18bb9e9f6e5 | -3.65096 | -54.05869 | 2025-09-16 04:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85ad6667-04b2-35ec-ab34-f48648c5c98d | -7.00364 | -45.64079 | 2025-09-16 04:27:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d57b88d2-b256-379f-ade3-3cfb2e7978fc | -6.29081 | -42.38823 | 2025-09-16 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ee0f093-9f2d-3f09-842a-4f0709ef588e | -7.08354 | -44.54663 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dfd5e70-b451-3bb3-a32a-6b69c2de24a4 | -5.99178 | -45.8153 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 194014f3-9c5d-38ae-a476-a7ce7021dbfa | -5.76217 | -43.93883 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1f20f2e-2b35-358a-8a5f-ba4e80d490ef | -3.81429 | -41.57431 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3b318267-5518-3690-ba12-39f88ecd558e | -5.79335 | -45.87343 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ea13919-019d-3b55-be18-c194d4bc67bf | -5.97519 | -45.83406 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3187f3d1-bed4-3a28-814e-8c3ce5b1d7ec | -5.7924 | -45.94075 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d0b59ed-e172-3022-a58a-cb7955e6283c | -7.13602 | -47.97725 | 2025-09-16 04:27:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c36defae-fbb8-3379-a06b-82b4f2ea0c97 | -6.16063 | -43.66919 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5748243-8384-3994-9ad1-61bf0f7fef8b | -5.80014 | -45.93486 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e54fa22-cfa0-3dc1-a562-f941321c92c5 | -7.4211 | -44.8652 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6288d5b8-f065-38b0-9e9f-573adba0de08 | -6.26369 | -43.46935 | 2025-09-16 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc0776d8-5270-3f7e-a356-eefc017b8a5f | -5.51009 | -42.70534 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 72a2554d-70af-3494-a03c-c9593f39f62b | -3.53812 | -52.20422 | 2025-09-16 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9237e19-6772-3a2b-89df-ce7d11984cfc | -5.80688 | -45.70108 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52bf2f2a-f091-3049-a72b-7dfbf3079940 | -6.31155 | -44.21363 | 2025-09-16 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91270761-9537-319b-85b7-87770b57de99 | -5.80293 | -45.93885 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa7ddd6f-5add-3819-b831-f240e55fd6eb | -6.0472 | -43.55984 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 057af665-28d0-3ff3-852d-03bea438c788 | -5.79846 | -45.92398 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d435b4a-83e2-387e-a217-3e4e66fe9d17 | -5.81005 | -44.86154 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1b499c8-70ae-362e-92f0-9ec268120ead | -5.21176 | -45.18265 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ce1a2424-f6bd-38fd-89e8-79bb48ec8cd0 | -5.77458 | -45.90603 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44e5add4-4466-3630-8a22-4fb57f02ec40 | -6.37174 | -44.40949 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| addeb8fe-0fcd-3e04-948f-af8a11640022 | -6.15952 | -45.99503 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ff8a2ef-4a9a-33ed-8f32-772369a749c6 | -4.90728 | -38.00428 | 2025-09-16 04:27:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 388650ad-42fa-38d1-902a-4f7163383436 | -4.45178 | -38.44557 | 2025-09-16 04:27:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ee937d69-2b21-3ff2-af4a-76e196bc50dd | -6.97939 | -44.53817 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ee2f551-23ba-30c8-a46f-9d82bb602bc2 | -3.82427 | -44.10412 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d010440-6503-38b5-ba15-f206f8e43d59 | -6.05901 | -43.55355 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05b058d2-0cc6-355f-9571-20a88901dc8a | -4.181 | -48.57442 | 2025-09-16 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99feabb3-5880-3adc-a95a-0d5dcacd31f4 | -5.78788 | -45.90813 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43b70c66-234b-3117-9399-e69658b8bb14 | -3.21756 | -47.13063 | 2025-09-16 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 55fe315d-e07c-35d6-a231-7a2a7e31923b | -5.08589 | -42.05287 | 2025-09-16 04:27:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0fbe6e42-29d8-34df-b70d-21cf79c2fde6 | -5.52643 | -44.21463 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a306fc4-1496-3a64-b3c5-7453cc29b62e | -6.25781 | -43.46025 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5e58d1b-775c-395c-9a82-95722b706152 | -6.52627 | -51.20186 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af39aad8-a014-3c04-af5e-7ab6a7525fed | -5.9137 | -42.74281 | 2025-09-16 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4bae9104-8ba7-3648-b781-b8756c58e6d8 | -3.82711 | -44.10828 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c896f35-098c-32b0-b0e1-6a29dfdcfd98 | -3.83504 | -44.10208 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b25f8e37-3108-3a99-89aa-d9afa81cdd25 | -6.92141 | -44.80506 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21dec0aa-f371-3eac-88d5-d394d4cd9ba9 | -6.18394 | -41.19787 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 35c6c853-2294-3e4c-89aa-a03cc819366a | -7.27384 | -46.58762 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c49acb5b-e973-3b7c-bdd4-c2e918b01b29 | -5.95683 | -42.73152 | 2025-09-16 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9970bb4b-9fc6-3acb-af96-1fd7e051e1e6 | -5.77908 | -43.92896 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e55ceb02-b934-3734-bcb8-003991ccaa74 | -5.79182 | -43.93867 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c611d11d-53a6-3084-91a4-c7398461b74f | -6.46437 | -46.01437 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f34c29d5-f0e1-3e91-b681-45f059b91cec | -6.52739 | -51.19511 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd57489f-4c33-3410-be59-5ddea879adbf | -3.83052 | -44.1088 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d71ad367-850a-308b-9660-da32632dc5f2 | -6.67027 | -45.54271 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc6634df-821d-3dd8-bb1d-7e37d320f2dd | -5.79413 | -43.9468 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9b331311-e8d4-3fc3-9f56-c418a9a5a1a2 | -5.92499 | -45.72671 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8c7874f-1bc3-3ebe-abf5-3a332c8c6f3c | -3.89656 | -42.51763 | 2025-09-16 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d0cccba-b809-32d0-8b42-f45768ffab66 | -5.90437 | -45.89412 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21c39756-a161-32db-8b33-5848eac48b8d | -6.51022 | -46.21413 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 46aed31e-0913-3a9e-8a1b-827424b8d79a | -7.27717 | -46.58815 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 14d95833-dfe7-3fd7-87ac-89698d179532 | -5.59958 | -45.36087 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2891f28-3ab1-3b57-b0bf-9e2b1076c800 | -7.14658 | -44.33646 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0021d64-d8ae-3ed5-bef0-a8c534c419a8 | -6.96605 | -44.5407 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c57dec8-8b00-39d3-bc1b-36d00115aa80 | -4.15522 | -46.79299 | 2025-09-16 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4349a07d-a6ad-3673-801a-4fe42bfbe361 | -5.89398 | -45.75033 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 833c0ff3-d4fc-3bf4-83bc-292af40a8f21 | -7.366 | -44.29131 | 2025-09-16 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af182d19-b335-3b5b-81e5-109e49c46aa3 | -5.95143 | -42.80809 | 2025-09-16 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d907e58e-7c6c-3ddd-a18c-9cdfd62bf380 | -7.27107 | -46.58361 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a4be1db-1e9b-3d72-bb29-1c59f5a4c6a3 | -6.29012 | -42.39276 | 2025-09-16 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6550425-d8d1-3105-b4ec-cd2956db8acf | -6.14102 | -41.18055 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 68fa92ca-e286-316f-9aff-50fd88570eec | -6.92539 | -44.80192 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bba83869-76ea-3114-ac19-5f31e07b3fa2 | -5.42073 | -43.18918 | 2025-09-16 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c8bcc3a-5d1b-3d5d-a7b4-1e38dee0af16 | -5.92444 | -45.73018 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0dae854-097f-3d56-a67d-28942d670079 | -5.989 | -45.8113 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d9b63e0-36f3-349c-b1f9-644ef38c184a | -6.92707 | -44.76872 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b88aff2f-d2db-317f-bea9-fad619e82bf1 | -3.81571 | -41.56498 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bced5b1d-097b-3262-aed4-a4db198d785b | -5.78009 | -45.89268 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68d60b1b-2ca1-3fcc-bf28-9f0aa12d0886 | -5.63126 | -45.33351 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cecea76f-7d00-399a-9f04-ecf3f7cd8df1 | -7.36947 | -44.29187 | 2025-09-16 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README34.md)
