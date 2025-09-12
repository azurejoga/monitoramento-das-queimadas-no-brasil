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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c2cf85f-1fd5-341b-ad3c-49f85c608d43 | -15.0974 | -52.4731 | 2025-09-12 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 010aa7dc-c9dd-39fe-ab9b-d043e0769820 | -11.1949 | -48.4277 | 2025-09-12 13:50:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 0bde6d91-7313-3e2c-955a-4fd8cfa6203e | -19.0618 | -48.7281 | 2025-09-12 13:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 9bbe636d-81db-3ae6-bef6-1c1058f2190c | -9.0373 | -47.1041 | 2025-09-12 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 3c3e8580-211a-366a-970e-948bd4144266 | -8.9752 | -46.0829 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 45ac7460-bf39-380e-8975-7f3096bcd8e6 | -10.0943 | -47.1664 | 2025-09-12 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| d4902ffc-2541-311f-8f7b-8edd06353059 | -10.8972 | -45.58 | 2025-09-12 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 637e3035-ca5f-3a2c-9323-e2a8910dbbc1 | -8.4705 | -47.2712 | 2025-09-12 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 53eec2bf-1690-3bc8-909f-d5172cb809ff | -13.2027 | -51.7618 | 2025-09-12 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 8d866b79-a3c2-32da-96bb-6ff26446e3ba | -8.0817 | -50.1836 | 2025-09-12 13:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| a4400f5b-4205-33d0-8304-a5e39eb78ade | -11.9523 | -51.1661 | 2025-09-12 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d7c8c147-c8a2-3b9c-98b2-4a37b27428b2 | -8.9087 | -49.9433 | 2025-09-12 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 95a68400-9a2b-31b6-8092-5fe8ba291a96 | -9.0379 | -47.0597 | 2025-09-12 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a4a06440-86cd-34c2-8050-b4de40d749ba | -16.3623 | -51.4969 | 2025-09-12 13:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 147.7 |
| ab31d4d1-45a9-309d-b164-79852b68555f | -6.1891 | -41.0884 | 2025-09-12 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 451.8 |
| 7b8cfa3d-53d5-3d67-a87e-9ae0f9491a18 | -6.309 | -42.2311 | 2025-09-12 13:50:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| eaf50b88-40f7-3851-b97c-6395130769d6 | -15.1053 | -48.0209 | 2025-09-12 13:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| e580134b-f167-3417-a18c-c2e6970555d2 | -14.3937 | -52.9456 | 2025-09-12 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a15f5cb9-0e9d-3459-8fc7-2bc8b195fb53 | -9.6727 | -47.568 | 2025-09-12 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f5bfdc0e-2114-3305-a251-8d1e224e1247 | -7.2188 | -55.0615 | 2025-09-12 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7e699dcc-f0c5-32fd-a28a-b067adcdfdae | -9.6919 | -47.5438 | 2025-09-12 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 181.6 |
| a0457392-ee3a-3ef6-a74e-e7be7065e80c | -8.096 | -45.5641 | 2025-09-12 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 69397bb3-2970-3df8-a4c6-1ac09087e513 | -12.9294 | -54.7333 | 2025-09-12 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 0c49847e-fb24-3a0d-b21d-b5ab07f57574 | -11.4398 | -48.5733 | 2025-09-12 13:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 358.0 |
| b54ca8a7-d957-35ce-af48-b81ae8c1d103 | -8.1837 | -46.0965 | 2025-09-12 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 0fc3cb5c-b0d1-3bf4-b311-ef96a688836f | -9.9004 | -51.8811 | 2025-09-12 13:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| c732feec-7b42-3214-a3da-c779c45efd28 | -6.8184 | -45.6349 | 2025-09-12 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 3f0692a6-e36f-3f2e-884a-e5e8c37985e8 | -10.679 | -48.6633 | 2025-09-12 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a11387d5-56dd-3cf2-aa02-a4bc293d7d9a | -9.4993 | -46.4299 | 2025-09-12 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c20f41d0-8a67-3d08-88d5-7fbc55cb2b37 | -10.0698 | -50.3668 | 2025-09-12 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 31498e90-7373-3cbf-9ea1-0bb65d92efe7 | -11.9713 | -51.164 | 2025-09-12 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 82997026-e908-3b7b-8a6b-4bd9d8da4db3 | -11.6629 | -46.5658 | 2025-09-12 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 3f2711ff-0b9c-390c-812b-c7477f55184b | -9.9218 | -45.9984 | 2025-09-12 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 480a5d35-64b8-350d-a45c-272bb63c59a6 | -10.9089 | -47.247 | 2025-09-12 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 8a4b35f5-92cc-3cad-a960-1bdc20d44e7b | -6.7503 | -44.9611 | 2025-09-12 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 14381c48-1589-32f9-9b35-72a880d26339 | -8.096 | -45.5641 | 2025-09-12 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| a3e1bd42-08bf-3e2b-b7fd-ad902c9c9634 | -10.1405 | -47.9133 | 2025-09-12 14:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 31ef0f08-c4fb-33cf-bcee-0ed7587a49a4 | -9.7197 | -46.8972 | 2025-09-12 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6a38dde8-af68-3616-b461-15b8de0e8208 | -8.3801 | -46.97 | 2025-09-12 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| c0ac4f18-9e7d-38e3-8629-2cac2f66cd16 | -11.9332 | -51.1683 | 2025-09-12 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 3cf379c6-5f46-3292-a4a4-b25d229d0a93 | -10.7172 | -48.6371 | 2025-09-12 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 7bd7cfc7-2bc9-3d38-b2ea-b37bdfb37ab0 | -11.429 | -43.5307 | 2025-09-12 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 246.2 |
| 09abdab9-af46-39f4-b29b-773969c91324 | -14.374 | -52.9692 | 2025-09-12 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5acff7d9-fa69-3f30-bb6d-8726b3207ea6 | -9.075 | -47.1002 | 2025-09-12 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0a081946-1f23-3d6a-a3ca-82928abf3f67 | -9.057 | -47.0355 | 2025-09-12 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 922c1671-f8ed-3e34-a751-61045ff88bc5 | -6.1891 | -41.0884 | 2025-09-12 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 307.6 |
| cef266fd-f9a9-3ad8-949e-c53e6d502fb3 | -11.377 | -50.2281 | 2025-09-12 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| dd73235b-fe34-361a-b512-fb36a1f9a3d6 | -15.1169 | -52.4705 | 2025-09-12 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| df10ce1b-0046-339f-9da1-ddd7447ef83b | -10.4441 | -50.6059 | 2025-09-12 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 339.9 |
| 97e4ae4c-5d97-39d1-85e0-f88063fb3f23 | -11.9904 | -51.1618 | 2025-09-12 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3afdf014-1fc4-39aa-b5e7-31e2a02ea07c | -15.5822 | -54.7429 | 2025-09-12 14:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| a1ec24a7-15fd-360d-8b4e-f025c0d055cc | -8.4331 | -47.2527 | 2025-09-12 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 115be623-8e18-35c6-ae93-cb9bd2c1fd0d | -11.4208 | -48.5756 | 2025-09-12 14:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6581e836-4e2a-341a-8b0f-4174d5d99135 | -6.1698 | -41.1387 | 2025-09-12 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 81fd11a2-dd56-3574-b975-47555b1752a8 | -15.0978 | -52.4518 | 2025-09-12 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 2138a0c7-3fac-3071-8e54-e60308241794 | -12.9098 | -54.7763 | 2025-09-12 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| e0bad7e3-f361-3c1e-9689-66a4c0f975e6 | -9.0379 | -47.0597 | 2025-09-12 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| e095caa4-4aca-3457-b859-68539cff3aa0 | -10.4252 | -50.6078 | 2025-09-12 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9c776e2d-9a16-3754-a00a-1632e06c3693 | -8.8899 | -49.945 | 2025-09-12 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9c80c6fb-2705-37da-8618-85df931e705a | -6.3278 | -42.2294 | 2025-09-12 14:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 47483498-055d-38ac-99e8-7f04b10f45ab | -11.5235 | -50.5968 | 2025-09-12 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 2df7f6f2-0075-37ea-8b00-92b2656654b9 | -11.1064 | -51.9748 | 2025-09-12 14:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 160.8 |
| fc26fe59-268d-3c60-a6a1-1d8808813a41 | -10.8034 | -50.5899 | 2025-09-12 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c2189859-7103-3769-97f8-d78f3a06cea2 | -11.4477 | -43.5514 | 2025-09-12 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| e874092e-e395-3a8e-8344-0ba099b15aed | -16.9621 | -45.8176 | 2025-09-12 14:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 9d7138cb-4245-3698-acf4-42b914a741b0 | -6.1735 | -42.6221 | 2025-09-12 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| f82ecdd3-2bca-3daa-b4ba-f3262c24db87 | -10.8972 | -45.58 | 2025-09-12 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f42637cf-6c09-3ab9-b285-1bb0ca65fa44 | -8.9371 | -46.1094 | 2025-09-12 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8e1659c5-3796-36a7-bb9c-63694fd673a7 | -12.9294 | -54.7333 | 2025-09-12 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| e4655da9-0ce6-32fc-82ad-23465aaa30cb | -6.7501 | -44.9839 | 2025-09-12 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| e2d8e189-8dbb-3454-845b-bd59022f04c3 | -7.4508 | -44.4407 | 2025-09-12 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 018e0926-2457-3e38-9e03-25173c8554f2 | -8.4328 | -47.2748 | 2025-09-12 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 92851037-b9e0-3ac5-bd23-c724f0b709ca | -7.5232 | -44.6862 | 2025-09-12 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 8c5d11da-04e5-3494-b9ab-0d064305b958 | -10.0943 | -47.1664 | 2025-09-12 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 186.9 |
| ab5c80d8-1a61-304b-a0f0-a0b51c10fc32 | -10.6979 | -48.6612 | 2025-09-12 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 63fdf84a-179b-3140-8446-5656eab991d2 | -11.809 | -50.5642 | 2025-09-12 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b44760ab-0b55-373b-b3ed-da20a3f90be7 | -14.4935 | -53.9181 | 2025-09-12 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 7ecf8b9e-7e3a-3b1e-a2b0-bd9a69a539e9 | -10.1133 | -47.1642 | 2025-09-12 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 4e658bf4-d9d7-339a-ba20-705042fd226c | -15.0982 | -52.4305 | 2025-09-12 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 1dff72dd-8844-39a9-8e38-d370ce4541b2 | -10.4438 | -50.6272 | 2025-09-12 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 350.5 |
| c8f83c44-0aae-3404-9377-029a2accc92d | -9.0373 | -47.1041 | 2025-09-12 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 6b2afc48-6dcd-36dc-b66e-4d7617a3c18f | -6.1923 | -42.6205 | 2025-09-12 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| fd7c6abc-6ba6-3ad5-b3a0-9bdca49cedf3 | -9.0169 | -45.7851 | 2025-09-12 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4acb1c4f-0f67-36f8-bf2c-1049608404db | -11.972 | -51.1214 | 2025-09-12 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 74254e71-8d6a-33bd-baad-8a7744cbd4ea | -9.0382 | -47.0375 | 2025-09-12 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d3903d72-966e-363d-bc28-38c4b040c746 | -6.2588 | -43.4828 | 2025-09-12 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 8c3fbaab-c69e-324d-96d4-694d16157292 | -15.5819 | -54.7637 | 2025-09-12 14:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 0b2f10d2-a0cd-3c51-8067-a628b937d347 | -12.8649 | -62.1268 | 2025-09-12 14:00:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d0b6648a-cbe2-372f-a719-28468648c70b | -6.8369 | -45.6559 | 2025-09-12 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 5edb97f1-c946-3ba5-9960-0e6c5c0ecc9e | -11.4285 | -43.5544 | 2025-09-12 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 485.9 |
| 48eecb2c-271d-38f2-be48-afa403055d46 | -12.9292 | -54.7538 | 2025-09-12 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 219.7 |
| 9f683a9b-01a0-3312-ae36-61e861d6acbb | -15.1249 | -48.0176 | 2025-09-12 14:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 1a509d62-4074-322b-80b3-482226bab21d | -8.2085 | -45.5981 | 2025-09-12 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 807d204c-fa51-3f57-96fb-2c54477738a7 | -10.4249 | -50.6291 | 2025-09-12 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 41e67193-b6ec-302e-b398-d6cdd58a5911 | -13.2027 | -51.7618 | 2025-09-12 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e3cc1037-31ac-3b0b-b55f-e08b8f1a38a6 | -9.4807 | -46.4096 | 2025-09-12 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 703a87c4-c9a5-3861-addd-d1e84f6c3461 | -12.9289 | -54.7744 | 2025-09-12 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| a3f79712-9ca4-3fa0-b3dd-7ad8aa7425f0 | -13.2801 | -51.7099 | 2025-09-12 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.9 |
| d8761a6c-942a-3aa8-a668-e0b5621cbf37 | -14.2732 | -45.053 | 2025-09-12 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9e43ad02-9275-32e3-b781-7efc7027a4da | -15.0246 | -50.1148 | 2025-09-12 14:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |


[Clique aqui para ver as próximas entradas](README134.md)
