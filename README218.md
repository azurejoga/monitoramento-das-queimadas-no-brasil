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
| 14af02e7-a31b-33c6-900d-633b7047a4b5 | -9.0149 | -67.7423 | 2024-10-03 14:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| a6554b6b-beb8-3360-8997-3b8db2162617 | -9.3833 | -68.3256 | 2024-10-03 14:26:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 205.1 |
| 8450ec66-0406-3ba9-922f-97a02a2e7334 | -9.4368 | -64.5419 | 2024-10-03 14:26:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 00eef18e-8d82-3249-8501-e206b833ab7c | -9.5824 | -50.1797 | 2024-10-03 14:26:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ab90459f-bc43-3fcb-b237-380216b9a106 | -9.4018 | -68.3252 | 2024-10-03 14:26:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 911449ca-78bb-3914-aa21-459e834447c7 | -9.3834 | -68.3071 | 2024-10-03 14:26:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3a4f723c-85ad-3d02-8a6b-be0ef2e134d7 | -9.3832 | -68.3441 | 2024-10-03 14:26:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 70e57fbf-97fa-3a5d-b0b7-44c0971fbfd7 | -9.5772 | -46.2639 | 2024-10-03 14:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 2868fbce-b49c-3099-8dc3-412d62fdb777 | -9.4567 | -68.5458 | 2024-10-03 14:26:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 9e240511-703e-3a90-8361-27ae8de09c3e | -9.4566 | -68.5643 | 2024-10-03 14:26:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 77b40400-3f34-3c90-9ae0-fa10c7375a64 | -9.4752 | -68.5639 | 2024-10-03 14:26:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 60.6 |
| dcddae3d-7358-3601-815a-02651a73848e | -9.6012 | -50.1779 | 2024-10-03 14:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7feed274-634e-30da-8ecd-89f10dde76ef | -9.4753 | -68.5454 | 2024-10-03 14:26:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 48.4 |
| c9a9bd87-bf1d-3a59-9216-138a7cf7cc8c | -9.7541 | -64.2853 | 2024-10-03 14:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c6703843-470e-38b2-991d-9d5d36688342 | -10.0418 | -48.2097 | 2024-10-03 14:26:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 209.6 |
| a327d13c-91fa-364b-a8f7-8f6cd55c7976 | -10.0415 | -48.2316 | 2024-10-03 14:26:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 573e7d2c-a29f-3705-907e-96be3deaaee1 | -10.0229 | -48.2117 | 2024-10-03 14:26:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| acbeafa7-3d1b-3821-a286-36e6962b3a4d | -10.0226 | -48.2337 | 2024-10-03 14:26:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 168a5dc1-47d8-3175-8d7c-6eba4c38387a | -10.2384 | -47.6817 | 2024-10-03 14:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 844093be-2db1-3aaa-bb53-a92decc29349 | -10.2195 | -47.6839 | 2024-10-03 14:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| bb2ce66d-db70-36f6-87fa-a2cf49b1a790 | -10.2574 | -47.6796 | 2024-10-03 14:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 300.9 |
| 3304e9a3-602e-372f-b916-d7956f2564dc | -10.6981 | -46.1287 | 2024-10-03 14:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 3d53a5b7-5c4f-3b47-8c5a-f8f60d5cdd59 | -10.6794 | -46.1085 | 2024-10-03 14:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 841c3d98-e8a9-399c-9b2d-5e33edbb7e38 | -10.6116 | -48.0795 | 2024-10-03 14:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 9e0881d2-9d5e-3479-ac10-aefc090c52cb | -10.5926 | -48.0817 | 2024-10-03 14:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 2f81520d-acb5-3eaa-9537-aa30cd6678c8 | -10.7315 | -47.6683 | 2024-10-03 14:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| eddcf991-ba62-362c-bb49-0abc2ad3a69c | -10.6505 | -53.6994 | 2024-10-03 14:26:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 66e38513-9a20-3ed7-80ed-92f9b4ccb80b | -10.6317 | -53.7011 | 2024-10-03 14:26:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 59e964ae-f7e3-3e2c-8020-e10996ff0762 | -10.6319 | -53.6805 | 2024-10-03 14:26:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b12f4faa-aefe-3621-8d0f-d8e233e4b7bb | -10.8906 | -45.9905 | 2024-10-03 14:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 1673a319-a2aa-3c29-996a-1435e6ac580a | -10.7122 | -47.6927 | 2024-10-03 14:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| cd65c657-7a79-3a38-9e35-07ad4eefc9be | -10.7319 | -47.6461 | 2024-10-03 14:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 0560db5a-467d-39e7-bcf2-01417bac8949 | -10.7056 | -64.1516 | 2024-10-03 14:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 0b296e81-47c8-39cf-a3e9-a29cbb5a4f44 | -10.9769 | -46.5443 | 2024-10-03 14:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c333666a-523e-3759-85d2-d07dd7b0487d | -10.7613 | -61.5376 | 2024-10-03 14:26:08 | GOES-16 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| aff2b712-683a-3581-b30f-c38bb3059c1d | -11.1575 | -45.9779 | 2024-10-03 14:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| e40bcba7-dbe1-301f-9276-6309e8c834fb | -11.2959 | -46.8399 | 2024-10-03 14:26:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| aefbe688-887d-364c-af5e-388d0ab9819c | -11.6238 | -64.1099 | 2024-10-03 14:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b1511ea8-4970-3c49-9a1f-e25fd6d86858 | -11.6052 | -64.0728 | 2024-10-03 14:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3e00a593-43e6-3330-b47a-de24b00d9d5d | -11.9737 | -47.3986 | 2024-10-03 14:26:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 3371452d-d274-3207-9aae-4235ba50b170 | -12.0131 | -47.3263 | 2024-10-03 14:26:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 98f9f73a-5cf1-3314-9173-91ed88100a29 | -12.1406 | -50.0524 | 2024-10-03 14:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 2ddb57ad-2597-3b5f-9bbf-3dd38badb2c4 | -12.3292 | -54.0954 | 2024-10-03 14:26:16 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7dda17cc-d13b-346d-948d-f3a8a93d6d51 | -12.5329 | -53.1212 | 2024-10-03 14:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 378b3ef5-5130-376a-9808-d0769ee840e2 | -12.552 | -53.1191 | 2024-10-03 14:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4c9b3d55-9811-35af-9b79-0d8b12505411 | -12.7812 | -50.5973 | 2024-10-03 14:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 53d848b4-814a-3845-b49d-68e8eaf179a8 | -12.762 | -50.5997 | 2024-10-03 14:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f54e139e-98df-3e7f-aa1c-251948692e90 | -12.9831 | -51.129 | 2024-10-03 14:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 61185a26-51bb-3cf3-b714-3de75bbd2328 | -13.0406 | -51.1218 | 2024-10-03 14:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 25721301-1e39-348d-93ac-b13fa93e4175 | -13.198 | -48.6267 | 2024-10-03 14:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 4872409e-fa50-3344-957d-da2695867c7a | -13.0402 | -51.1432 | 2024-10-03 14:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 64873ef2-e054-3cee-afc0-b9f2b4c0d7a1 | -13.1787 | -48.6295 | 2024-10-03 14:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 47bca232-618e-3d35-90f8-31ba3adc02a7 | -13.5954 | -51.2011 | 2024-10-03 14:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| aa120d3a-e5a5-3870-8f22-553e8c2474f4 | -13.615 | -51.1771 | 2024-10-03 14:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.7 |
| e6760c19-9d6e-331c-a843-b4d70f545044 | -13.6146 | -51.1986 | 2024-10-03 14:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 59d0d9fb-0af9-3876-8de9-4ad2acb60409 | -13.6342 | -51.1746 | 2024-10-03 14:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 49fb796d-1d38-370c-a352-f7a88aab9898 | -14.0202 | -45.0747 | 2024-10-03 14:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 7258034e-6594-3493-ba78-df0948780c41 | -14.0397 | -45.0713 | 2024-10-03 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 71219319-fc8f-3849-afef-9639c84feb8b | -14.0392 | -45.0947 | 2024-10-03 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 683.5 |
| c094eea8-8c40-3657-a3b3-6cbb6a62087f | -14.7017 | -48.7559 | 2024-10-03 14:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 4d94b195-62d8-3691-82cf-14b90273ffe4 | -15.143 | -48.0819 | 2024-10-03 14:26:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 10aaa906-e0f7-3e87-a1b8-a6f7ee4495f4 | -18.7663 | -43.387 | 2024-10-03 14:26:50 | GOES-16 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 154.3 |
| 6124091d-ba27-3d95-aa34-478eb21dabb6 | -18.8406 | -42.9235 | 2024-10-03 14:26:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 224.8 |
| 65d05d5a-c8d9-348c-a886-9287f2b29a48 | -18.9733 | -43.2104 | 2024-10-03 14:26:51 | GOES-16 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.5 |
| 969a1a6c-d40e-323f-b125-c61e7e94c9a9 | -19.0148 | -43.1749 | 2024-10-03 14:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 252.0 |
| 9e4fd83d-ec96-329c-83d2-b7744e6e0e48 | -19.2962 | -42.5779 | 2024-10-03 14:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.6 |
| f9d0d0bc-0fa3-3ef9-a0dc-2b135f39089d | -19.6993 | -42.0384 | 2024-10-03 14:26:54 | GOES-16 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.5 |
| f70c929e-4533-3cab-bf99-d392f2a96537 | -3.3084 | -42.691 | 2024-10-03 14:35:25 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 0b656792-1dc4-3a57-9f0f-c9d554e00567 | -6.0235 | -44.5632 | 2024-10-03 14:35:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 48824bec-7c4a-318e-86cc-b27d1d431dad | -6.0048 | -44.5647 | 2024-10-03 14:35:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| d2643ea3-5545-31ad-ba46-c4c5add8d2f8 | -6.2565 | -41.8538 | 2024-10-03 14:35:41 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 346525cf-b82f-3ef1-b8d8-2e8a1f56ae70 | -6.3196 | -43.0335 | 2024-10-03 14:35:42 | GOES-16 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 2dd5f567-7bb9-3005-a74d-6167a824be28 | -6.3008 | -43.0351 | 2024-10-03 14:35:42 | GOES-16 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| cfb518ec-05ac-3277-9b65-17f53b47b2df | -6.9479 | -47.6668 | 2024-10-03 14:35:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 807a4260-b78a-3841-9006-c416d9ea3536 | -6.9075 | -44.2836 | 2024-10-03 14:35:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 2feebe3c-032d-326c-934e-85a19bd10528 | -6.9685 | -49.4378 | 2024-10-03 14:35:46 | GOES-16 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 3b9272e8-3dd7-3676-8d60-d974c5127e4c | -7.0367 | -42.8036 | 2024-10-03 14:35:46 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 8b4eac4b-91e5-3d17-8ff8-50206bff00e6 | -6.9666 | -47.6653 | 2024-10-03 14:35:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8403c124-0da1-3170-98bf-75417466fa8a | -7.6444 | -42.4342 | 2024-10-03 14:35:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 380951d5-feb3-32b2-8b5b-f9bc628826d6 | -7.4734 | -61.4037 | 2024-10-03 14:35:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 62b9b36d-2c1b-3c63-8611-09691e3ee72b | -7.6441 | -42.458 | 2024-10-03 14:35:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 864a081d-c66f-3cf5-ae1b-55e8ad080be0 | -7.7321 | -46.1393 | 2024-10-03 14:35:50 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 2f0687b6-493f-3d50-988e-051bd7f97bd2 | -7.8778 | -50.0087 | 2024-10-03 14:35:51 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 0aba6d61-5c1a-3459-a4ac-33a063fe8a23 | -8.194 | -46.8102 | 2024-10-03 14:35:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 999b47ea-dca2-352d-b3a7-b7353b70c273 | -8.1762 | -43.6723 | 2024-10-03 14:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 68adad3f-253f-3f0a-a3b0-08146cdcc3c1 | -8.1759 | -43.6957 | 2024-10-03 14:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 9341baf9-0e86-3d7b-b364-cb46027f1510 | -8.1859 | -44.3901 | 2024-10-03 14:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 7e16a52a-6391-384b-9d65-d5fe7c50d8a8 | -8.1937 | -46.8324 | 2024-10-03 14:35:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 3873e1c0-4ab2-3bee-afc3-4179e43bd73e | -8.157 | -43.6977 | 2024-10-03 14:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 139.2 |
| 427b6dda-d270-399f-8636-e83d1b248c44 | -8.4259 | -46.2968 | 2024-10-03 14:35:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f2808722-c4aa-3ba2-84e2-92b98aff7c04 | -8.6113 | -46.5243 | 2024-10-03 14:35:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4ae9cc2a-cb17-361e-9dfe-48715a1b11c4 | -8.7033 | -45.2289 | 2024-10-03 14:35:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e6e77c86-b055-3b4c-a309-a3d3113e4138 | -8.7603 | -45.1999 | 2024-10-03 14:35:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ec838c69-afbe-33e9-9bde-045e62695462 | -8.742 | -45.1563 | 2024-10-03 14:35:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 94da3f2d-f14f-359b-9827-d997f277af8c | -8.6302 | -46.5224 | 2024-10-03 14:35:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 823f96c4-cdaf-3eb1-a782-078f3f5f80c0 | -8.8179 | -45.1252 | 2024-10-03 14:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| d2a078c6-1f07-32ba-8d4d-a3c996b8232a | -8.649 | -66.6767 | 2024-10-03 14:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 3edbdca0-eada-3477-93cf-4dcfffb1ff9d | -8.6675 | -66.6762 | 2024-10-03 14:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 67d48d9b-20e9-3a1a-9a2a-4a5bc518ad5b | -8.8562 | -62.2223 | 2024-10-03 14:35:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ec7c2ed3-0cc3-3fc0-b697-d8c6ed107157 | -8.9674 | -45.2456 | 2024-10-03 14:35:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |


[Clique aqui para ver as próximas entradas](README219.md)
