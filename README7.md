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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a6133c6-7289-3132-824d-2ecdb4f14cc6 | -7.5288 | -61.4015 | 2026-08-26 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9d8b8349-4c37-33f7-9012-c6b369e027b8 | 1.4917 | -55.9837 | 2026-08-26 02:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| f805acd1-ed9d-39fa-83b0-abb5f3dfea9d | -10.3727 | -45.0537 | 2026-08-26 02:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| f0676d57-ff50-3e31-a6ea-4f10b67b091d | -6.641 | -58.4987 | 2026-08-26 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 154.8 |
| b5609daf-e758-366d-a2c3-e41816db0252 | -6.6595 | -58.498 | 2026-08-26 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 9ca70e02-db10-3407-ae1f-40971ba07c9c | -7.0796 | -59.2351 | 2026-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| c11fffab-2dc5-3178-b431-b6a1af348ce8 | -7.0612 | -59.2358 | 2026-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 911d078f-3ae1-3bd8-9f52-f556ddd2a35d | -7.5104 | -61.3832 | 2026-08-26 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 186.7 |
| e2e91079-97ff-368b-8668-3d3b82f10ad3 | -7.0797 | -59.2157 | 2026-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 337f05a5-7de8-37ae-bc09-2ae0be515204 | -7.5289 | -61.3825 | 2026-08-26 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 291.6 |
| b13c69cc-28fe-3f1e-94ce-02e7c4cfcf09 | 1.4734 | -55.9642 | 2026-08-26 02:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 9b6db2cd-bc7b-36b5-b237-7878d293ed2c | -10.7596 | -54.0384 | 2026-08-26 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 213.1 |
| 0eecaf75-4500-3606-a2db-4bf7fddbc3d0 | -7.529 | -61.3635 | 2026-08-26 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 9c81114a-0ead-3030-8ba0-ba8cf9c28861 | -7.0242 | -59.2374 | 2026-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 31134ffe-6964-3b9a-8778-890da7e47c3a | -10.7784 | -54.0368 | 2026-08-26 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 4a28aef5-ff78-36d7-8d46-4ee354827f0a | -6.2676 | -53.3768 | 2026-08-26 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 36c3d2c9-84ae-3226-9db6-8b487e520ca2 | 1.4918 | -55.9443 | 2026-08-26 02:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c45af9d0-2c70-3df5-9de2-356108216365 | -13.2266 | -51.4613 | 2026-08-26 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7e1d343f-74b8-3bdb-8130-49cef5c44f61 | -7.0613 | -59.2165 | 2026-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 178.7 |
| 1efae819-8078-301c-9f9f-07ea0782aff9 | -10.7598 | -54.0179 | 2026-08-26 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 6164678d-0e35-36bf-b92f-94c4b5216623 | -6.6226 | -58.4995 | 2026-08-26 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| fb6aedf7-df76-356c-9ab4-5e97cc51309d | -6.2491 | -53.3778 | 2026-08-26 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| eb966313-0669-3b85-a063-bc3d97c401a9 | -10.7787 | -54.0163 | 2026-08-26 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 3ef42b0c-3fbf-3d1b-a001-76e336bd6fef | -7.0243 | -59.2181 | 2026-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 6487a92a-b6d3-3777-9d09-54eafb84651b | -6.2677 | -53.3565 | 2026-08-26 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 88123aa4-02c8-3408-80a5-02a136dbdf10 | -7.0613 | -59.2165 | 2026-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 4cb35af9-4fa5-3ee9-9216-507323fa2ff3 | -7.5288 | -61.4015 | 2026-08-26 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| d38541ab-21e1-32a9-a89b-0b01839c7b08 | -10.3727 | -45.0537 | 2026-08-26 02:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| ee16c557-11e4-386e-9315-76785f622043 | -7.0243 | -59.2181 | 2026-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1a257c07-a9a6-349f-ae0e-f252934e289f | -6.6226 | -58.4995 | 2026-08-26 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d8352668-e4ef-30d4-af87-c88e152fe933 | -7.0612 | -59.2358 | 2026-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.0 |
| ffdd00ee-fa76-382a-acaa-7acaf5a0b29f | -6.2676 | -53.3768 | 2026-08-26 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 7c133ed4-13f6-39fe-827a-6b65a46793ea | -7.5289 | -61.3825 | 2026-08-26 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 298.1 |
| 17c8e4cb-fae5-357e-870b-82c323896b80 | -7.0242 | -59.2374 | 2026-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| f7dce062-b1d3-3cd9-b17b-cc7b4db2e983 | -6.6595 | -58.498 | 2026-08-26 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e2ed5846-5692-3fa7-9582-c68cd6807781 | -7.5104 | -61.3832 | 2026-08-26 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 184.0 |
| 67f74e83-72f7-3209-8062-55d8766b0803 | -7.0796 | -59.2351 | 2026-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| d9b11029-c6ab-3cbd-9415-8ddbcf18fa92 | -10.7598 | -54.0179 | 2026-08-26 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 46d4d6fd-3cd0-3366-940d-aa45cfa214b6 | -7.0797 | -59.2157 | 2026-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| d840c4eb-2f6c-3d88-aebf-aa789472a86b | -6.2491 | -53.3778 | 2026-08-26 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 7740316f-2c66-34a4-9db9-25ee783c5e77 | -20.2602 | -46.3203 | 2026-08-26 02:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 66.8 |
| d4fef154-e902-342f-b10d-9b1edd8e1dd1 | -6.6409 | -58.5181 | 2026-08-26 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| f718913c-46a5-374b-bd49-429e36a6b6d2 | -10.3723 | -45.0767 | 2026-08-26 02:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b6b3b8b2-c915-3ea5-98be-326cb865d6df | -10.7787 | -54.0163 | 2026-08-26 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 8ac7b4d7-36c0-3eca-80c6-f1821f1f04c8 | -7.529 | -61.3635 | 2026-08-26 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| bde248e5-3ae7-359f-aada-962c610dbfcd | -10.7596 | -54.0384 | 2026-08-26 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 51274304-7448-338c-96a2-88ef7304c11e | -10.7784 | -54.0368 | 2026-08-26 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.8 |
| cd4f9e0f-b4cc-3059-9882-03e46191a65c | -6.641 | -58.4987 | 2026-08-26 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 129.9 |
| f44c97b9-bf17-3fd3-8e80-fd302e29ca2b | -6.6595 | -58.498 | 2026-08-26 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 912bcd13-5c08-3926-b5fb-fcae0f1a11c3 | -12.6836 | -48.4116 | 2026-08-26 02:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e089846b-6f7e-3ab1-ac38-33a42b43f21b | -7.5104 | -61.3832 | 2026-08-26 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 185.5 |
| febfb1e1-87cb-3946-a2df-423e1edc45df | -13.2465 | -51.4162 | 2026-08-26 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 0e8cd286-dd12-33ab-b374-493c470355e7 | -10.3723 | -45.0767 | 2026-08-26 02:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| cd585d69-b4f4-3aed-863e-bfdc1f10aeb9 | -7.767 | -44.7543 | 2026-08-26 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 042f54bf-cfdd-3f6a-b9e4-84b1da75cf0e | -7.5288 | -61.4015 | 2026-08-26 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 735a293c-17a4-3170-94b9-90a15d510f2c | -7.0242 | -59.2374 | 2026-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 984fd19c-4459-3d59-95f1-1eaa80ea2218 | -13.3031 | -51.4731 | 2026-08-26 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 22cede2a-a133-32c0-9bc8-f91b9a50e28e | -7.0612 | -59.2358 | 2026-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 6c40319f-2861-310f-aec7-d1c839fc74cc | -7.0613 | -59.2165 | 2026-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.9 |
| e068698b-1532-3c57-898a-8eab27c3657e | -10.3727 | -45.0537 | 2026-08-26 02:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| f46e13f2-1d8c-3ae5-b253-dce48abf4147 | -14.7981 | -48.7851 | 2026-08-26 02:40:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3f95d34a-6d87-3cc4-aba9-9378db4aacd0 | -6.2677 | -53.3565 | 2026-08-26 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 06c4ac63-13dc-3b98-b3ec-8a515e337a40 | -7.0243 | -59.2181 | 2026-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9fa147ae-bac3-3be6-97bb-c60d3e001c62 | -7.5103 | -61.4022 | 2026-08-26 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| cb61d47a-dd10-3274-8d99-466176009646 | -13.2839 | -51.4755 | 2026-08-26 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 02c03044-bbad-3f35-bded-08c7265324ca | -13.2469 | -51.3949 | 2026-08-26 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 195.8 |
| 58c0503a-9251-3019-afbe-431a46236c26 | -13.3027 | -51.4944 | 2026-08-26 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 81ac662f-e5ce-3c84-be29-37e76c3bcc24 | -7.0796 | -59.2351 | 2026-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ab39c79d-3f07-378b-8706-f6bb38faf176 | -13.228 | -51.3759 | 2026-08-26 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 195.4 |
| e7b93ffc-0329-3ec2-a784-2528d7aaf61c | -7.5289 | -61.3825 | 2026-08-26 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 277.1 |
| 18e63d5d-7221-3580-934a-1f279388d0b7 | -6.641 | -58.4987 | 2026-08-26 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 136.7 |
| df36a162-1fbb-3b6b-af4a-633633f7734b | -10.7784 | -54.0368 | 2026-08-26 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 2b9a0392-4dfd-3e32-bdb5-b2a3184d8789 | -14.7977 | -48.8074 | 2026-08-26 02:40:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3057b083-129e-3640-84ef-d746b7e8d926 | -6.6226 | -58.4995 | 2026-08-26 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ad75d9cd-203c-375c-b4b6-f5de4017694e | -13.2277 | -51.3973 | 2026-08-26 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 392f3374-4fd2-3fb0-b7bf-8d5569315675 | -6.2676 | -53.3768 | 2026-08-26 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 6b674886-5d8e-300a-a08a-6855d52dd08c | -9.6024 | -55.1078 | 2026-08-26 02:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 914e9df1-c3a9-3c92-b52e-85b0e0853c03 | -7.0797 | -59.2157 | 2026-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 4bcdb8e7-2047-3f93-b73d-69512eb47fab | -6.6409 | -58.5181 | 2026-08-26 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 032900b3-4ca3-33ca-964f-b86664e50bd9 | -13.2088 | -51.3783 | 2026-08-26 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f13d416e-466d-3e0d-8227-e0dbd2cb4235 | -10.7787 | -54.0163 | 2026-08-26 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 5caef67a-5454-3b82-903e-5938f5c4380a | -7.529 | -61.3635 | 2026-08-26 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a2dc22d7-00bf-3591-8e1f-247a5d36d636 | -10.7598 | -54.0179 | 2026-08-26 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 41f6ec7b-2072-3cfc-b770-99ef79c1787f | -6.2491 | -53.3778 | 2026-08-26 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 3776990a-54bc-33f4-91d7-ecae53be7f08 | -13.2842 | -51.4541 | 2026-08-26 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 9e844cd2-d4dd-3373-9c46-25987abf7ae5 | -13.2661 | -51.3925 | 2026-08-26 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d05e353d-9690-3b52-9e0d-d40817eeb846 | -10.7596 | -54.0384 | 2026-08-26 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 148.7 |
| d205be56-fc68-33be-b77e-119976d44f04 | -14.7787 | -48.7882 | 2026-08-26 02:50:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| fe3bcd5e-f0ce-3c5a-a86f-71dc1149b111 | -7.5105 | -61.3642 | 2026-08-26 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| dac612cd-7ba4-321d-9550-c0119cb992f3 | -7.0613 | -59.2165 | 2026-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 8f4669d4-0ca2-3189-a626-b0fa63c17451 | -10.7784 | -54.0368 | 2026-08-26 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| c47eda9d-374b-34da-9f70-6902734f43ef | -10.3723 | -45.0767 | 2026-08-26 02:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d897e9bb-b567-39d2-acfd-29ae34ef2f6a | -10.7598 | -54.0179 | 2026-08-26 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 143.0 |
| ba71794b-b4e4-3a36-ab95-bb42a48d6dbb | -13.2842 | -51.4541 | 2026-08-26 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| a5413487-7e2d-3c5a-99ca-58873da8511d | -13.2839 | -51.4755 | 2026-08-26 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 37c40407-3d18-3126-b125-056de211be02 | -13.2277 | -51.3973 | 2026-08-26 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 6ec6a8a4-093f-353f-8f47-f4ece5862e0f | -13.3027 | -51.4944 | 2026-08-26 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 33c0e809-3f0c-360d-8c17-85fc78fdea54 | -13.2469 | -51.3949 | 2026-08-26 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 19959407-7e14-3400-a1a7-f36a1eb17373 | -10.3727 | -45.0537 | 2026-08-26 02:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 5cf5711b-5872-3443-8328-aedf37d06b82 | -14.7782 | -48.8104 | 2026-08-26 02:50:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |


[Clique aqui para ver as próximas entradas](README8.md)
