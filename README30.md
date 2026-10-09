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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 998206e8-03fd-3a2b-9fa0-7ffca8aa2f01 | -8.9659 | -47.533001 | 2026-10-09 00:28:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f005a496-83fa-34af-828e-47cf5496625f | -6.4354 | -55.055099 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6e73288-80dd-38b9-a62a-dc4a53c6ca22 | -2.8184 | -54.106201 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48d5ab4e-326f-3824-a6d8-2045452e6ef4 | -3.349 | -50.408501 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05457b52-f5b1-315f-b2e7-16ded8558266 | -9.7867 | -44.775398 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e2ab1b13-549e-3eca-88a6-0f528032f82f | -11.2174 | -45.2659 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c453a8e-21a6-3971-b7de-537bb5fa90c7 | -12.31 | -47.09 | 2026-10-09 00:28:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa395e9c-28db-321c-ad08-7cc1f0024ae2 | -5.1055 | -46.218899 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f5e263de-a414-32a1-af29-c3b070933067 | -4.9832 | -46.0453 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1e0bbaf-7bc5-3ccb-adc0-f3e34cad0269 | -4.1223 | -46.877998 | 2026-10-09 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef337ec8-58fd-339d-9b6b-87b24b357b22 | -5.0859 | -46.223301 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f525cea-79eb-3976-9567-d6af4d71f337 | -6.4789 | -55.307598 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4742b1-cb23-3bc4-b99c-4765da763a66 | -5.6787 | -53.475601 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35fb84c6-2dca-3909-b898-1e1ceca5c99e | -1.5428 | -54.565701 | 2026-10-09 00:28:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c79ef76f-f07f-3c69-be72-2d67d3c0cfac | -4.7602 | -44.010201 | 2026-10-09 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3ac82b7-af56-372c-a9b5-7a5f3c1ca4c7 | -18.638201 | -41.344398 | 2026-10-09 00:28:00 | METOP-C | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 662d2543-6626-3d81-987e-7ae58a9afe8b | -8.9653 | -45.151901 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3fab7db2-ecc6-30c7-94db-39a3a0231ab3 | -11.7561 | -44.9594 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a4b88b1-d109-3956-8f69-5219ca32edf6 | -4.9145 | -43.257301 | 2026-10-09 00:28:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82afa058-66e8-3f05-9d4d-f9e3460cc4db | -6.152 | -43.386101 | 2026-10-09 00:28:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3511cc9c-afee-39ba-89f0-0fb3ee37f41c | -11.6146 | -43.705299 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c2c7d4b-818b-3ef6-861b-d254aafee8a0 | -3.1057 | -54.1577 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b82a6f15-de32-32dc-a743-fbefc5062977 | -1.1503 | -54.235401 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd394493-c1bc-3e8c-8cb2-9fe78a7c92b6 | -11.1959 | -45.307499 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bca72be4-6e0f-3af8-b414-717ea2e24000 | -11.1876 | -45.3167 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f9fdc423-5ba7-30c3-b8e2-ed432efd13b5 | -3.5742 | -52.687901 | 2026-10-09 00:28:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6e6fb6e-0c00-3fcc-80e2-3b8fd3c4bcd1 | -6.8244 | -39.5467 | 2026-10-09 00:28:00 | METOP-C | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2785cdfc-ba17-36a9-8421-a85caccd757c | -18.068399 | -41.740101 | 2026-10-09 00:28:00 | METOP-C | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab1fd84a-0f93-3194-b57b-1267e4ea706f | -5.9857 | -41.372898 | 2026-10-09 00:28:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| af438809-fc36-3dff-b240-099e0d60a536 | -2.9595 | -49.189201 | 2026-10-09 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5eeb476-9459-3e8c-acee-68bd3feba458 | -11.7603 | -45.482201 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f3b1e94a-4196-3a77-a5dc-06d20569b25e | -11.6211 | -43.5994 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e45f7076-b786-3d1b-8cb0-3897e2365bcd | -2.073 | -46.576302 | 2026-10-09 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caf61510-0955-32a1-8f9e-1eb7244d96f6 | -11.2284 | -45.3148 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98b68192-a64a-39ce-ba4d-26b26fa14416 | -13.206 | -54.366402 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a970c836-b04e-3fcf-9ecf-f8fa494a1a3b | -13.4054 | -43.7314 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 767be6f3-86c5-3aa1-b930-40b248cee698 | -15.4314 | -43.252602 | 2026-10-09 00:28:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 708889cf-9645-3f55-a06d-c04725b58cb9 | -11.7826 | -43.539001 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a63b029a-358d-34ea-b975-056d9e2837c5 | -13.4995 | -44.374001 | 2026-10-09 00:28:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c363ed5f-dc8d-3924-9de6-41208c3b878a | -3.5591 | -54.681 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2049409-52a3-3952-b029-84891099a09b | -1.1106 | -47.7742 | 2026-10-09 00:28:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61e66440-8447-3c9d-b98d-cd0ab5a6eddb | -3.2163 | -42.964001 | 2026-10-09 00:28:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee8d6dcf-f7ef-30d4-b568-7b4b164aeeb1 | -11.6048 | -43.7076 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c28c3c4f-aade-3ba6-ae5f-fdf0d7777abf | -10.3016 | -46.601799 | 2026-10-09 00:28:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bdc2d5f0-8c0b-3cd9-9168-de204aed4d41 | -6.0879 | -43.995098 | 2026-10-09 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02cda23e-009a-37fd-90ae-bc54c38e7851 | -11.4012 | -46.691799 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d29d3366-d3bd-3b60-b2bf-8284dffae2eb | -2.8782 | -54.190701 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b77adfc-2795-3682-8a6e-2c2dfd1b23a2 | -6.7014 | -47.026299 | 2026-10-09 00:28:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 947fc0d2-7073-3aea-a39c-055018ec4863 | -5.6156 | -44.850101 | 2026-10-09 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f35154c-5d6a-3438-83d4-38edcc3d408c | 3.5202 | -51.254902 | 2026-10-09 00:28:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 791fd794-aa7e-3dd6-8a02-984a956e06b3 | -6.7326 | -55.166698 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7aa4151-5022-360e-bb92-39b03a5b4c14 | -12.0306 | -43.450802 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f48edd3-0706-3947-bffc-ea31f4021be6 | -3.0132 | -54.063801 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec7a3c6-fff1-39b4-baf7-70f8095ccd1e | -10.8854 | -44.800499 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 035b8a5c-02dc-396c-8891-b557642b76d1 | -5.388 | -44.2248 | 2026-10-09 00:28:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c8265ba-4f3b-3890-8977-b1656b887a11 | -13.8087 | -44.191502 | 2026-10-09 00:28:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 010a4395-8dda-30c2-b5ae-efa8c4f0fe8b | -5.3954 | -45.909302 | 2026-10-09 00:28:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c6b52e9-3fbd-30b5-a1e5-0e4ce62a4859 | -16.9981 | -41.1824 | 2026-10-09 00:28:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9d5173ec-49df-3c4d-99e4-bf6b1deabffd | -11.9091 | -46.5709 | 2026-10-09 00:28:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4aabc9e-08d2-316b-acaa-9eb1e5ebd8bb | -6.8175 | -39.306999 | 2026-10-09 00:28:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7ecc11fa-9a95-30ba-bd3c-d99db430c189 | -13.3826 | -46.6875 | 2026-10-09 00:28:00 | METOP-C | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 07614fc8-c665-3268-a70f-6f54618b38d9 | -4.9459 | -49.420101 | 2026-10-09 00:28:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cee6be4-9505-330c-9f74-419152706c3e | -11.6064 | -43.714699 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6124a531-f11f-3d32-af7c-2c70106a99c1 | -3.5299 | -54.687302 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a95bd41f-033f-393c-928a-0e4d43c02353 | -1.7803 | -47.142601 | 2026-10-09 00:28:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b890fa7-3689-374c-8a91-b61efecfd6c0 | -6.7121 | -46.030399 | 2026-10-09 00:28:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bb26a07-17e8-343d-af6f-e80286a6c5c5 | -2.8191 | -51.291599 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 197ebfab-b664-3fb2-b6be-a2f866f71466 | -11.6522 | -43.689098 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23b5885d-ce2c-3bd0-a3e6-3c704dd86a0e | -4.5415 | -54.9814 | 2026-10-09 00:28:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b525476-ed5a-3bda-8200-6afac4fb11c3 | -5.6925 | -49.082199 | 2026-10-09 00:28:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb8a1432-4061-3b4d-805a-9b6991e5a9ad | -2.3289 | -48.502102 | 2026-10-09 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7249a144-f2ec-3f4b-b41d-9fd604774752 | -11.7643 | -44.9501 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c59ac5c-ef34-308a-99db-e1bc9a4cb9d5 | -11.0058 | -45.424301 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f128485-99f4-309f-a562-26996f38a59d | -10.0063 | -48.577599 | 2026-10-09 00:28:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a494b4c2-dac1-3ef8-a1ba-d15fca8c1a20 | -3.2407 | -54.030602 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7528da90-ed5e-3cc8-a677-b7cf1005283a | -8.9124 | -45.236401 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c3c1b722-0de5-3336-9fa7-aa6d906a8b82 | -5.4884 | -44.301498 | 2026-10-09 00:28:00 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b963681-c276-391a-ba7d-ee7995194c87 | -9.1012 | -48.801201 | 2026-10-09 00:28:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9adfab-7600-3766-bc55-c8398260339a | -6.0065 | -40.9417 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 30623a92-7e55-3812-afc4-375c0ca44e13 | -13.8745 | -43.799 | 2026-10-09 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4bbfdc2-9d26-37b1-8fa4-c2f2579ac244 | -13.4168 | -43.736099 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c36e8c8-b201-358c-b2de-0c4dd5138780 | -7.397 | -44.745701 | 2026-10-09 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 600fac09-2de7-3f09-87e0-dd7961f6efa5 | -3.5436 | -54.702599 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1bb9d2a-44aa-3ea9-9507-bf1c43dbc894 | -13.2567 | -47.0075 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 570bd4ed-818b-399e-87f8-62914d426b15 | -5.7213 | -41.778599 | 2026-10-09 00:28:00 | METOP-C | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bef213b3-7557-3613-9271-5db725ef2a0d | -8.2886 | -45.711102 | 2026-10-09 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ed45bfa-2a4b-3471-846b-9aeecf0fbf26 | -3.2527 | -50.391899 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2cfe51f-7e9c-32a5-a06c-2bd1a1d79942 | -9.9024 | -44.785301 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 573e3748-1bcf-318f-8c06-79065217356e | -17.613899 | -42.324902 | 2026-10-09 00:28:00 | METOP-C | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c09ee06-0386-33b7-8aeb-3e1b97a033e6 | -3.2287 | -54.6623 | 2026-10-09 00:28:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 827e112c-fe03-39bd-927b-19bbfa0b408f | -14.3943 | -43.817799 | 2026-10-09 00:28:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4cab952a-5a02-3bb0-8142-35a34706c6bd | -9.1224 | -45.843102 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 365b464f-aed7-33ed-9b30-5db4a3ee944f | -8.2125 | -46.831799 | 2026-10-09 00:28:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9ce2d8c-833b-3da6-86e7-2aac878db23b | -7.2108 | -55.178902 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db30e13c-98a6-3f5d-9149-8791c6036eb3 | -5.6197 | -44.377998 | 2026-10-09 00:28:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f57b28f-f61d-3091-a111-a4516cf71c23 | -7.3875 | -45.647202 | 2026-10-09 00:28:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d5922b3-7ac2-3c37-8324-06199df57ff8 | -3.0867 | -53.936001 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab7ae51-d01c-3b0d-bb63-200b0ec5d89a | -3.9028 | -42.112301 | 2026-10-09 00:28:00 | METOP-C | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c194ca6c-5283-3169-bc37-53539b465f11 | -11.201 | -49.4216 | 2026-10-09 00:28:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6ae674-d726-3b9e-b5f3-edd3d97420e8 | -4.3803 | -41.820301 | 2026-10-09 00:28:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README31.md)
