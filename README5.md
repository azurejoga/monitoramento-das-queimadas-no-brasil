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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40b6c45f-1a8c-3415-bc97-5d1aef7bfff6 | -6.087 | -44.628601 | 2024-10-12 00:24:20 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74ff0ade-999d-3419-b037-77b94c7f2220 | -6.0756 | -44.623798 | 2024-10-12 00:24:20 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3eeebf5f-2f2d-3f18-8092-5c3a03c82d4f | -6.0772 | -44.630901 | 2024-10-12 00:24:20 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62436575-c7e0-3fd0-9baf-3c4ac26ddcc6 | -6.0788 | -44.638 | 2024-10-12 00:24:20 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0221f51b-e7a4-3bb5-8d25-fd92d1254a4a | -6.0674 | -44.633099 | 2024-10-12 00:24:20 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe932797-541e-3e32-82dc-8f2043e34318 | -6.069 | -44.640202 | 2024-10-12 00:24:20 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 166cc8cf-aef2-3d9d-a29c-c507f65efdb8 | -6.1264 | -44.937901 | 2024-10-12 00:24:20 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9cf634c-39b7-395e-9076-d19a5f997851 | -6.1279 | -44.944901 | 2024-10-12 00:24:20 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed2ba28b-bde4-3a19-bbe0-54e96ef1a5c9 | -7.0825 | -49.240799 | 2024-10-12 00:24:20 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d321458-c958-3ca9-971c-f88cf87883fa | -6.3674 | -46.143101 | 2024-10-12 00:24:21 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be36253c-6a71-3e46-8483-c9ef3a3258bc | -5.7203 | -43.7906 | 2024-10-12 00:24:23 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10f6efec-227c-3491-aa33-dc66d4727450 | -5.7105 | -43.7929 | 2024-10-12 00:24:23 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d88d4fe-0b1f-33bd-b4d9-48f0f4d37547 | -5.1191 | -41.6814 | 2024-10-12 00:24:25 | METOP-B | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9678201b-ee0d-3367-a901-1ed5f5eba58e | -5.5945 | -43.961399 | 2024-10-12 00:24:25 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9bd38e06-5cad-3add-a3b5-b61428b4f666 | -6.4516 | -47.536598 | 2024-10-12 00:24:25 | METOP-B | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e76d375a-56b1-3b4b-9602-71de2efa625b | -6.4533 | -47.5439 | 2024-10-12 00:24:25 | METOP-B | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43c27c44-8e88-3d1d-ab8e-8c46fec5333b | -6.5133 | -47.815102 | 2024-10-12 00:24:25 | METOP-B | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6acabab-89b3-3d0f-a110-27b7f30f85a0 | -6.5149 | -47.822498 | 2024-10-12 00:24:25 | METOP-B | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f383c457-05c7-3a26-aa26-efbdeecccba7 | -6.0689 | -46.281601 | 2024-10-12 00:24:26 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f027cce7-65ad-344e-9546-cba617b91281 | -6.4248 | -48.252899 | 2024-10-12 00:24:28 | METOP-B | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e0dfd88b-2c63-3d26-81e8-869796f41de9 | -6.4265 | -48.260601 | 2024-10-12 00:24:28 | METOP-B | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 03b44bbf-426c-3549-9564-a52f9707edc3 | -6.4282 | -48.268299 | 2024-10-12 00:24:28 | METOP-B | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c0b6d68c-45be-3c8a-8b94-bc112a1ed05f | -5.5626 | -44.679901 | 2024-10-12 00:24:29 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89a580cd-438f-37f7-9f79-3eae03d0c463 | -5.5642 | -44.687 | 2024-10-12 00:24:29 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fee4230f-acab-357f-9ae8-fc386d7ca430 | -5.5528 | -44.682098 | 2024-10-12 00:24:29 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e154f852-a2c0-3d2f-b15f-3ea3f2246f19 | -5.5544 | -44.689201 | 2024-10-12 00:24:29 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6898e6a7-e92b-39f9-abfe-647ebd4a6bd2 | -5.5561 | -44.696301 | 2024-10-12 00:24:29 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5c0f906-cc31-3c99-8c3f-bc2de1aee326 | -5.8918 | -46.3643 | 2024-10-12 00:24:29 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57351c10-d8bf-358e-9109-4ed983a62210 | -5.8496 | -46.222401 | 2024-10-12 00:24:30 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff99779d-1530-39e1-b0a8-40c2c3a35d81 | -5.8511 | -46.229198 | 2024-10-12 00:24:30 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a71ebd2b-f5c0-3bb4-93c8-ad8fcd5bd4b2 | -5.8804 | -46.359501 | 2024-10-12 00:24:30 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 939f17f1-b43a-30af-b989-e3fb19c47a6c | -5.8819 | -46.366402 | 2024-10-12 00:24:30 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea3a910-d127-3c5d-a789-5ccfb85c9bde | -5.4554 | -45.3881 | 2024-10-12 00:24:33 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ea1a907-adb7-3104-8982-d97169ccc99d | -5.457 | -45.395 | 2024-10-12 00:24:33 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6629573d-d534-3f10-a763-9f19a5cf0601 | -5.4585 | -45.401901 | 2024-10-12 00:24:33 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfaed1b3-26a6-3fd2-b1ff-8d605417e2be | -5.663 | -46.4007 | 2024-10-12 00:24:33 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63eba2c7-2163-3912-88ff-01f053b56de0 | -5.6646 | -46.4076 | 2024-10-12 00:24:33 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d3b0561-f2d4-301f-a71f-1e93415d44bb | -5.6661 | -46.414398 | 2024-10-12 00:24:33 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41e66368-83ac-3255-9f97-827a946aba63 | -5.3804 | -45.193699 | 2024-10-12 00:24:33 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e043e25e-2f04-39e2-ae62-9b536f908f77 | -5.382 | -45.200699 | 2024-10-12 00:24:33 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20c683b4-06ff-3c77-a9fa-60c5d9571723 | -5.4036 | -45.341599 | 2024-10-12 00:24:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d294b530-397f-37a8-8f61-2735507c6ce0 | -5.4052 | -45.348499 | 2024-10-12 00:24:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81138dae-bc63-36ff-bf97-35c98cbe86d0 | -5.4068 | -45.3554 | 2024-10-12 00:24:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a4d39d6-28a6-37ea-80cb-26f483b5d9a8 | -5.3938 | -45.3438 | 2024-10-12 00:24:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c305b891-c19b-36bd-b999-70c9f041379c | -5.3954 | -45.3507 | 2024-10-12 00:24:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9064163-9993-389c-905e-027112246f35 | -5.8465 | -47.405899 | 2024-10-12 00:24:34 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 607369f1-87a4-30dd-9b23-b83d4e47a93a | -5.2407 | -44.759998 | 2024-10-12 00:24:34 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6adae105-f825-35b6-b1f4-4944d49c06db | -5.8367 | -47.408001 | 2024-10-12 00:24:34 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9a0cd7e-a757-3381-bc31-596078d40711 | -5.575 | -46.2836 | 2024-10-12 00:24:34 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e710e97-851d-32eb-a68f-f737058101d0 | -5.3248 | -45.402901 | 2024-10-12 00:24:35 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86256707-1b3c-3f1d-a3f3-38a7a7a46725 | -5.3263 | -45.409801 | 2024-10-12 00:24:35 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0badb7de-1db0-34aa-8f5d-d777777ff01c | -5.315 | -45.405102 | 2024-10-12 00:24:35 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8ff89b5-4c56-3727-8110-77fc3e2436df | -5.3509 | -45.563702 | 2024-10-12 00:24:35 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03abb912-350c-3b69-8c03-a9b52efbc236 | -5.3524 | -45.570499 | 2024-10-12 00:24:35 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e47e8d35-b9f9-3a82-8d92-32cde6783065 | -5.0887 | -44.816601 | 2024-10-12 00:24:37 | METOP-B | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50ec3537-7c9b-37e2-9e32-ee6131b651fb | -5.2528 | -45.585602 | 2024-10-12 00:24:37 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe8653d1-2f6c-3591-bf40-c24f249a562a | -5.2543 | -45.5924 | 2024-10-12 00:24:37 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55c71360-833d-3d2a-8fd6-7058eb115f0d | -5.293 | -45.900902 | 2024-10-12 00:24:37 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15c2b5d2-ccf6-31ec-86e8-2c8338746559 | -5.1799 | -45.5368 | 2024-10-12 00:24:38 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5cbe8fa-8d28-308f-8b22-c078505ea64a | -5.8358 | -48.657902 | 2024-10-12 00:24:39 | METOP-B | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b14136ff-796c-3859-9d48-aada12586dd5 | -5.8375 | -48.665699 | 2024-10-12 00:24:39 | METOP-B | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6efc480d-4e01-3c7f-91d4-bc3ea4dd83fe | -5.66 | -47.909401 | 2024-10-12 00:24:39 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 880c2b16-c01b-30e2-bf9b-4b5a536c5ce3 | -5.6616 | -47.916698 | 2024-10-12 00:24:39 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8727a3c9-41f8-358e-9b93-7fc6a4800875 | -5.6502 | -47.911499 | 2024-10-12 00:24:39 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7173670-9ee2-3faa-8aed-90fd7b7eb68f | -5.6518 | -47.9189 | 2024-10-12 00:24:39 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e8c5c7a-c3c5-3aa1-ba30-124d00e3cc5a | -5.8571 | -48.988201 | 2024-10-12 00:24:39 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d065c33-f835-31d2-a81a-7f70024d5acc | -4.7133 | -44.074699 | 2024-10-12 00:24:40 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd29622d-fec2-37a6-9d5c-486d9703257c | -5.1725 | -46.1432 | 2024-10-12 00:24:40 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a365bdec-b758-37a7-a5b0-5bc9b45d83a1 | -5.174 | -46.150002 | 2024-10-12 00:24:40 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad86b654-f57f-3b3e-af1a-0950f638efc4 | -5.0933 | -45.837502 | 2024-10-12 00:24:40 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc0214dc-1a49-308c-8731-53142e8ec068 | -5.0948 | -45.844398 | 2024-10-12 00:24:40 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93911a00-b10b-3f24-a5e4-b2095fdea07d | -5.1627 | -46.145401 | 2024-10-12 00:24:40 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1709b791-f2e0-3e09-9a74-580886c7501f | -5.1642 | -46.152199 | 2024-10-12 00:24:40 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 057195b5-3b88-3047-8ee8-b7d779a521b0 | -5.1168 | -46.170101 | 2024-10-12 00:24:41 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f5b4882-e69a-3199-bb00-24a240234d54 | -5.1183 | -46.176899 | 2024-10-12 00:24:41 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ccd3131-5bbe-38a0-9f66-8ccd22dafe52 | -5.1198 | -46.183701 | 2024-10-12 00:24:41 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f42bd41-42a4-306d-b3bf-be3a13fbdfff | -5.1085 | -46.179001 | 2024-10-12 00:24:41 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 341df87e-3480-3d81-8881-3dda822ba03a | -5.0725 | -46.064999 | 2024-10-12 00:24:42 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28537c78-200e-3427-a2c0-4eb82b584c16 | -5.5211 | -48.071301 | 2024-10-12 00:24:42 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74a8a888-debe-3b1e-8838-438c7531ec16 | -5.5228 | -48.0788 | 2024-10-12 00:24:42 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dad8780f-0f44-3824-a77b-f471b22c485e | -5.5113 | -48.073502 | 2024-10-12 00:24:42 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbf88133-8a01-347d-b707-8cbebcbd5bbe | -5.513 | -48.081001 | 2024-10-12 00:24:42 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56d6e6b9-39d9-31f1-88e4-b2123bc37bf1 | -4.9275 | -45.6511 | 2024-10-12 00:24:42 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41b23900-682a-334d-975d-fd06fae48137 | -4.9291 | -45.658001 | 2024-10-12 00:24:42 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26a18bcd-af51-3bb0-8a21-00604cc0e99e | -5.4132 | -47.909801 | 2024-10-12 00:24:43 | METOP-B | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5a62fcf-41df-3f5f-8f53-905ab8edb4f8 | -5.4149 | -47.917099 | 2024-10-12 00:24:43 | METOP-B | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36b814c0-5012-3b51-8968-925c54e927ff | -5.4051 | -47.919201 | 2024-10-12 00:24:43 | METOP-B | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efc9cbbe-bf27-3438-bcfe-6a22a1888da7 | -3.7078 | -40.705799 | 2024-10-12 00:24:44 | METOP-B | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2db9802b-e1ad-3fd2-88e2-56f8433fae9e | -3.7597 | -40.972198 | 2024-10-12 00:24:44 | METOP-B | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 935a60e5-b90c-3820-b584-67be11804bda | -3.7623 | -40.983501 | 2024-10-12 00:24:44 | METOP-B | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 743b81b9-5cf0-316b-9356-e188bf4cea63 | -4.8588 | -45.666401 | 2024-10-12 00:24:44 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c68e7e4-62b6-3ee5-b8a1-825fa856c76c | -4.8604 | -45.673302 | 2024-10-12 00:24:44 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0536ba68-417b-32c1-a962-fb4ecac6c53d | -4.862 | -45.680199 | 2024-10-12 00:24:44 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1256bb6d-e050-3252-823d-b289407f3a92 | -5.0945 | -47.172298 | 2024-10-12 00:24:45 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41c3192d-ecc7-3e02-9ca0-fe064e717de8 | -5.096 | -47.179298 | 2024-10-12 00:24:45 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15981fa6-1cb4-3347-80d7-193a3286a867 | -5.2709 | -48.056499 | 2024-10-12 00:24:46 | METOP-B | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8fa1f8a-60b6-3764-aa62-d2501da9b6c9 | -5.2726 | -48.063801 | 2024-10-12 00:24:46 | METOP-B | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68979280-ce5e-3cba-a9ef-c5eaf51cd8d2 | -4.9797 | -46.797699 | 2024-10-12 00:24:46 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dd7fcb6a-132e-30d3-820d-7f2779abec38 | -5.2546 | -48.029202 | 2024-10-12 00:24:46 | METOP-B | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 325f09b2-568f-3c77-9baf-f75ae2cd3e73 | -5.2562 | -48.036499 | 2024-10-12 00:24:46 | METOP-B | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
