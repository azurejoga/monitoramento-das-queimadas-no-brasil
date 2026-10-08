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

## Dados Diários - Página 218

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a2ddc0b-2dd9-3aac-957d-21de079932ff | -2.7796 | -54.0937 | 2026-10-08 14:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 298fdc8b-4d74-30de-8376-816e9d8f14ab | -11.3986 | -47.5635 | 2026-10-08 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 0386102d-a4e7-3bf8-9aed-33d744c1e158 | -12.7111 | -45.8223 | 2026-10-08 14:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| d4dec78d-87e7-345d-90cc-575847dd783c | -18.05 | -44.5582 | 2026-10-08 14:50:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 8c605782-7c91-3fb3-8e4d-825c8447801c | -6.988 | -59.123 | 2026-10-08 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| c292e70d-3475-3e03-9727-c86fbbc04888 | -8.1876 | -54.7219 | 2026-10-08 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| f638e196-ee55-3972-9d56-96c2b9481fcb | -11.2083 | -45.217 | 2026-10-08 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a8fcbe4a-1fb0-35a2-b674-3714954dd03d | -2.7981 | -54.0732 | 2026-10-08 14:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| c1e1dd1f-0725-31ce-9c4f-36f635425a19 | -6.6901 | -45.3519 | 2026-10-08 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 9f81c86b-0fad-309f-a004-7c903607693b | -12.1729 | -44.7983 | 2026-10-08 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| a071b2ab-54c6-34b7-8abd-45fa107bd80c | -9.7881 | -44.7828 | 2026-10-08 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| e5d31dc6-0c31-3a7b-b5fc-68ad05ab1ba3 | -9.1015 | -45.1164 | 2026-10-08 14:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 219.7 |
| 5b65e83d-d68b-3f98-965b-0856b6b79a38 | -8.9054 | -63.3378 | 2026-10-08 14:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e62c05ae-ec0b-332a-af57-0cac338292c3 | -6.3836 | -52.7169 | 2026-10-08 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f9c568e7-b19c-331e-8872-f88d5cdbe12b | -5.7319 | -41.6589 | 2026-10-08 14:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 193.8 |
| 8053926f-ea1c-3710-bcfc-64124409166c | -13.1641 | -54.3178 | 2026-10-08 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 224.7 |
| ec447187-2bec-3768-9e7d-818827056d1d | -9.4819 | -66.7836 | 2026-10-08 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 79e2dece-de68-3ec3-ac51-99551ab872c2 | -5.372 | -44.1751 | 2026-10-08 14:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| afab2e44-321c-30f1-86f2-acc9349bbd57 | -9.4751 | -64.3336 | 2026-10-08 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d16de1f6-bee6-3113-a5d8-338ea25dd6ee | -8.2621 | -54.717 | 2026-10-08 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 6db45292-3f57-3501-b4db-ec4dc92205d6 | -8.5921 | -67.0491 | 2026-10-08 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 6a4335c1-3933-3ff0-8e3c-acaa4f2103bd | -13.1639 | -54.3385 | 2026-10-08 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 222.1 |
| 78a10757-f6da-3d37-a43e-bfe964bc1d1c | -2.8346 | -54.1326 | 2026-10-08 14:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 047a382a-b5f6-3a9d-9fdd-9247288c6e98 | -10.4337 | -47.2824 | 2026-10-08 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 196.5 |
| c87a885b-b981-37c5-a218-47aca1fa936b | -2.798 | -54.0933 | 2026-10-08 14:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 17525a6f-c052-36a6-a56d-565d21aff490 | 1.6937 | -55.6263 | 2026-10-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ca2a8d84-4b4b-30c1-b04f-76644e0b0329 | -7.0892 | -52.6753 | 2026-10-08 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 25521ae8-04cd-37b3-a7c7-a2f59a2b42ee | -2.8347 | -54.1125 | 2026-10-08 14:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| bbfbfeac-501e-3d0b-b4fd-8d882efa5599 | -1.494 | -54.5363 | 2026-10-08 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 236.4 |
| 9b347e32-5166-38dc-9526-867f13e73b70 | -6.2355 | -52.6841 | 2026-10-08 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f7ad72a4-00e8-39f5-b998-ef11f4e2b89e | -6.4392 | -52.7138 | 2026-10-08 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c4d63af9-922a-397f-9dc1-d8519d5af61e | -8.969 | -45.1313 | 2026-10-08 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 368.3 |
| 7ec44c6e-b3dc-35fc-adee-717c1e6eb2ca | -8.1113 | -50.9417 | 2026-10-08 14:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f73ac005-decb-3002-a04a-12498c961997 | -6.7366 | -55.1274 | 2026-10-08 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 26a68162-04d9-34e2-a50f-6289990192c6 | -1.5302 | -54.8151 | 2026-10-08 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| f6b39ddb-77fd-3c84-9b76-58068d519ddf | 1.6385 | -55.785 | 2026-10-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b63f29e4-f452-323d-b491-c08fd4979d15 | -6.7368 | -55.1074 | 2026-10-08 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7d21ca3d-7ad5-33c1-b0bb-0144acaa2c9d | -10.4914 | -47.231 | 2026-10-08 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 76bc265f-15c6-31e5-9d77-f2386e5f870e | -9.9018 | -44.7917 | 2026-10-08 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 32fb1432-00f8-3d97-989d-d375daadaca8 | -12.0448 | -43.434 | 2026-10-08 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e2e559a3-f07b-306a-98ef-25b382781b3b | -6.2158 | -52.849 | 2026-10-08 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| af095d30-fc3c-3237-a9da-9eedc738e58a | -1.5306 | -54.5558 | 2026-10-08 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 977de27f-141b-3e6e-bee2-fa9513220c77 | 1.6568 | -55.8242 | 2026-10-08 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3cc46758-bdef-3db7-b3c8-dc16958a84ac | -11.2661 | -45.1859 | 2026-10-08 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| a085b344-6d9f-3b45-8785-1fda7f1fed99 | 1.7672 | -55.5463 | 2026-10-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 869c3d88-2050-395c-b52c-9adce0898a58 | -9.8015 | -47.8186 | 2026-10-08 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8e4c4261-4678-3809-8b3e-a035ae4278b4 | -7.8876 | -55.0023 | 2026-10-08 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 67ddc7b0-b9af-3d7d-9b2e-3d5352470c0e | -7.4697 | -42.8315 | 2026-10-08 14:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 193.9 |
| 0aa98623-1751-3d81-8560-710ee055f1a1 | -8.1115 | -50.9206 | 2026-10-08 14:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| e759adba-eaac-3ac1-9922-b30d4a49b35d | 1.6937 | -55.6461 | 2026-10-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 99c5a375-2adb-3cf5-ba96-71eeab4bf901 | -11.7742 | -43.5245 | 2026-10-08 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| f6505d1f-9f7d-3ae3-b97f-d46adbfcfe63 | -5.8801 | -45.9537 | 2026-10-08 14:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 634476cd-3fb8-330d-9fa7-fee1f6577643 | -4.3471 | -43.8021 | 2026-10-08 14:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 03677b34-db71-318c-8a8a-a70a173eea55 | -8.1996 | -46.3415 | 2026-10-08 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 1d7638cd-4e64-3b1b-b26f-0fc617eb8e77 | -8.6292 | -67.0111 | 2026-10-08 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 342544e6-a643-3b7b-be2c-ca2dba2ffd0d | -10.9766 | -45.3865 | 2026-10-08 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| de08d5fa-d295-3b0c-9f3e-dc3f975f1a97 | -6.3283 | -55.3276 | 2026-10-08 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| fd0e79f9-c4d3-3dce-a438-e5a23483316f | -9.4492 | -44.6167 | 2026-10-08 14:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| af3d69bf-9ab7-3e31-b5e8-23e77c9e1e3f | -1.5118 | -54.8153 | 2026-10-08 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| d136e263-ac22-3382-a3d4-2466e10eccb4 | -10.5094 | -47.2956 | 2026-10-08 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| aaa582ba-96e7-33f9-9fd0-c2f35942d96f | -11.3937 | -46.6922 | 2026-10-08 14:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b2be5552-5371-3900-aad8-abd64260ba0e | 2.7641 | -60.0106 | 2026-10-08 14:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 33115a80-5161-30fc-9669-fe7cd3d0d54f | -11.3103 | -44.8337 | 2026-10-08 14:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 248.2 |
| 61c08285-55d0-3da3-b088-2730f385d1ea | -18.0493 | -44.5824 | 2026-10-08 14:50:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 5d33c3a7-7014-305e-b371-4a06c0486872 | -8.5313 | -46.911 | 2026-10-08 14:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 165.5 |
| c4bb5a17-ef1a-31d2-a745-8f5fd016f979 | -12.1545 | -44.7547 | 2026-10-08 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 207b1006-2bd6-39a8-ace4-6c1c4123a0f4 | -7.89 | -54.7206 | 2026-10-08 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 34693623-690f-3c5b-8eb4-2deabf07ef8f | -2.0447 | -54.3085 | 2026-10-08 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 49ed452d-446e-36d1-a905-629deb07a0b6 | -11.4507 | -43.3854 | 2026-10-08 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 346.8 |
| bbeaedf8-0b94-3194-8920-a58c26f305e0 | -6.3232 | -46.5459 | 2026-10-08 14:50:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f8ee4728-9e63-3b27-b9a4-dda7aca309a8 | -4.3285 | -43.8032 | 2026-10-08 14:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ef601779-d7dc-3795-9528-9ae41dfbcca4 | -9.4306 | -44.5959 | 2026-10-08 14:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 93adfdcb-42c0-3300-a478-534f3681a59a | -1.4569 | -54.7761 | 2026-10-08 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 4f59b32c-c96d-3593-bf01-a17524080e34 | -3.1951 | -42.9538 | 2026-10-08 14:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 74dc4def-f5d3-3b44-8fbe-d6cbcac2b82a | -10.9575 | -45.389 | 2026-10-08 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 3432b8b2-8918-3ebf-a828-a13bcebbac55 | 1.7121 | -55.6063 | 2026-10-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| da93e895-e43e-30da-bb4c-27c7412ffd25 | -8.0578 | -45.6131 | 2026-10-08 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 33f778b9-0316-3813-90d9-bd9957913711 | -4.1457 | -43.2103 | 2026-10-08 14:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| dbf8390c-5dd7-330e-8ba4-50fd6e695473 | -1.4118 | -48.9318 | 2026-10-08 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a810b3be-c69f-397c-abb2-f5aad5e10b23 | 1.7671 | -55.5661 | 2026-10-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 17f20940-8f4f-3067-9135-cb47ef7eb61c | -1.4756 | -54.5365 | 2026-10-08 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 4f505bc9-f784-3a47-aa6e-ba731cdff12a | -1.6213 | -55.1321 | 2026-10-08 14:50:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| b0fb07a1-3444-33bc-8694-ce4eb38e9286 | -11.4503 | -43.4091 | 2026-10-08 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 19d5e150-6c27-3353-b416-239d4b7686e2 | -1.135 | -48.8928 | 2026-10-08 14:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 06dfe4fb-be99-3096-baba-ed295071f2f5 | -7.0706 | -52.6764 | 2026-10-08 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3bec0b46-5bb6-3d70-bb19-f5511a79c39c | -1.3277 | -55.4327 | 2026-10-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| f228013f-15b3-3a69-9f98-9504be479d56 | -8.0769 | -45.5886 | 2026-10-08 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 256.2 |
| 1c5c4449-2a25-3fc0-a5aa-49c4f3e2dc4d | -13.69 | -49.085 | 2026-10-08 14:50:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| dc544c58-b00e-359c-8c00-ec5ebf063b3f | -12.1967 | -57.1103 | 2026-10-08 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9bdfb2e6-7e2e-36fa-9a52-a227a5bcbb87 | -8.6106 | -67.0486 | 2026-10-08 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 333.5 |
| 04f1a72c-56d8-311f-9e16-503377993923 | -10.4527 | -47.2801 | 2026-10-08 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 190.9 |
| b3816b0d-8980-3f14-8d70-3d00b831c256 | -7.3286 | -50.8314 | 2026-10-08 14:50:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 1e56513e-6ca5-3466-8fe1-66c851ce22fd | -8.9501 | -45.1334 | 2026-10-08 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 908.4 |
| 3d164ab6-854e-3139-8538-979ee1602718 | -1.4569 | -54.7562 | 2026-10-08 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 65128ae3-f417-3099-b2ee-c1a236c7e327 | -8.2181 | -46.362 | 2026-10-08 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 240.9 |
| 9a02d2b9-9abd-3672-b546-0274e4bc7f26 | 2.1083 | -50.8375 | 2026-10-08 14:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 77.4 |
| e32f2fcf-6981-3174-9ad0-dfebd0740399 | -1.8803 | -53.9701 | 2026-10-08 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 2813a7d8-c48a-39d0-a9bc-f8ccdf6acb74 | -10.6912 | -47.8278 | 2026-10-08 14:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| ef2b1c8f-58d3-35c1-9552-656bff78874f | 1.6568 | -55.8045 | 2026-10-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 06746b0e-3b58-3cee-81c8-35c32d538aba | -11.7932 | -46.7733 | 2026-10-08 14:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |


[Clique aqui para ver as próximas entradas](README219.md)
