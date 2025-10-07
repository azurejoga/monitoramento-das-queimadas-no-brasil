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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e026f8b7-e7fe-392a-81c0-a4aa4bd4a946 | -17.9979 | -45.0011 | 2025-10-07 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 965c6e2f-67ca-3ca4-bf2d-933900185e34 | -8.4336 | -47.2085 | 2025-10-07 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| b2141901-005f-3afe-884e-bedbd89b8309 | -10.0868 | -50.5141 | 2025-10-07 13:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 44e88a52-45fd-3189-8fa4-1831d80bc0fe | -8.6397 | -47.2769 | 2025-10-07 13:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 83bcabb0-2c8c-3a94-834e-5ca8ea49cb4a | -8.1879 | -44.2283 | 2025-10-07 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 334.8 |
| 46b0becf-000a-3eff-b266-6b5d250b351c | -10.1573 | -45.4701 | 2025-10-07 13:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| aa480ff9-7aac-3d85-86d8-a4e96b3d095a | -8.8618 | -46.0949 | 2025-10-07 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3ea6fd3e-af35-3bc8-90d9-2bc87cf8e600 | -8.1882 | -44.2052 | 2025-10-07 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 256.7 |
| 9e2d3e86-8bbc-331b-8ad5-6c25538bfd50 | -12.9426 | -46.8109 | 2025-10-07 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| b5c55567-e5bc-364e-bfed-4d400fab387d | -18.2856 | -45.4587 | 2025-10-07 13:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d37e015c-b3de-3118-a2de-0259acc446db | -12.9615 | -46.8306 | 2025-10-07 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8d678e50-6502-3f0f-abf8-1f7a8a6fddb1 | -10.4746 | -48.3805 | 2025-10-07 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b3c13282-00a6-3b4c-b0c9-9b95f8dc04f6 | -8.0866 | -44.791 | 2025-10-07 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b8b706ea-eac9-34d5-a135-b71b1201be7d | -15.6007 | -52.5529 | 2025-10-07 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b67bfd80-697e-3f13-a5cb-471dbb0bfbe4 | -12.7446 | -50.4945 | 2025-10-07 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 6e8137f1-5bcb-31bc-9ffd-5c449a47a201 | -14.7389 | -46.0138 | 2025-10-07 13:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 134.6 |
| c6f98d3b-5217-3a43-b464-414ab499777d | -14.5057 | -46.9242 | 2025-10-07 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7e5bd21b-1c92-3520-abf8-f5de53105820 | -11.8029 | -45.1087 | 2025-10-07 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 1523a19c-5919-3e08-84ee-7547a2275896 | -11.8447 | -44.9176 | 2025-10-07 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 97097879-ba97-303c-9ea8-e5fc2fcd4632 | -10.1753 | -45.5363 | 2025-10-07 13:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a88d126a-9a74-3df9-9ca9-184d4d31d031 | -11.7833 | -45.1347 | 2025-10-07 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ea2df5e7-ccff-3d66-9af4-840c38ccb0cf | -17.9778 | -45.0057 | 2025-10-07 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 718e73b6-c668-31cb-8b70-ff6a7b7f09e8 | -10.456 | -48.3607 | 2025-10-07 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f631fa1c-cf46-3146-b4fd-b6f2a7ed33a3 | -8.6798 | -47.0738 | 2025-10-07 13:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 173ea7b9-f491-303f-8f9a-b676f91c6e63 | -8.8794 | -47.6722 | 2025-10-07 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 1c321209-7226-378a-a698-09b37a1d3c75 | -10.9303 | -47.0882 | 2025-10-07 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 41dc7de0-2573-36aa-9f52-6539ecf85bb3 | -13.0779 | -47.8234 | 2025-10-07 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| b9dcb31f-0589-3034-98a1-1ba3d9878236 | -12.9619 | -46.808 | 2025-10-07 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 6f732493-53d0-3e5c-a339-e0b528364c46 | -15.3742 | -47.2973 | 2025-10-07 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 090ab754-55ff-35a3-bbad-4bfb8fe10bc7 | -10.4054 | -45.3931 | 2025-10-07 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 0456150e-3517-3d79-b42a-7deec80c186e | -10.1943 | -45.5339 | 2025-10-07 13:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 195.9 |
| a99ed414-35b0-3b33-8492-7066ed9f4779 | -8.4824 | -46.2912 | 2025-10-07 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 6411c4a0-36c3-3983-ad5c-4ce006ad682f | -8.1876 | -44.2514 | 2025-10-07 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| bc5a6a3f-befe-39e9-a1c5-2e7eeac4aa72 | -12.6159 | -44.7519 | 2025-10-07 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| d5c20fbf-613c-3fa1-b4cb-ec97de071095 | -8.8986 | -47.6483 | 2025-10-07 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 41c87d48-6a64-3fcc-b37b-effd9618c2da | -11.7217 | -45.3738 | 2025-10-07 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 6eb49a93-6bb2-37fc-93c2-3f8480ec70e1 | -10.4108 | -50.2683 | 2025-10-07 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c0dd8c64-6d96-36c8-a82e-b94ce814adcc | -15.6202 | -52.5501 | 2025-10-07 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 92bcc4bd-5489-3541-857d-f42392dcf130 | -13.7927 | -45.7627 | 2025-10-07 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 6ae6ba36-d42d-3f08-a4ca-a4ad78fd1950 | -12.4665 | -45.5386 | 2025-10-07 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 065ae3df-9b6c-3b0e-acbe-ee6e1a944a7a | -16.2942 | -50.9868 | 2025-10-07 13:00:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3124f6a7-204c-395b-84a2-897a1717eab8 | -8.5393 | -46.2631 | 2025-10-07 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d162546d-eac3-3052-874a-576fdec95b50 | -10.4058 | -45.3702 | 2025-10-07 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| c7438613-3231-383c-970a-6655f5d59079 | -8.5584 | -46.2387 | 2025-10-07 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 3aea30bd-5601-3490-a0e6-e844a2525f13 | -10.1939 | -45.5567 | 2025-10-07 13:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| db424b41-438c-341f-a9de-6e0d7eb8e79f | -10.4245 | -45.3907 | 2025-10-07 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 275.9 |
| 17bd3e82-6965-379e-b99d-5d8d26dabcba | -14.8641 | -51.4373 | 2025-10-07 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 495e7e2c-ef7b-33b6-9b48-4c9d800ffd04 | -14.2953 | -45.8382 | 2025-10-07 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 265.1 |
| f42072bd-de37-39e8-9d48-e4127f2b78b4 | -8.1055 | -44.7891 | 2025-10-07 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 33953d08-5a4f-3bce-884d-4b46eb1d3369 | -12.9816 | -46.7824 | 2025-10-07 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| df413ea8-17a9-3bf4-ade4-96f89ee9f1a1 | -8.1879 | -44.2283 | 2025-10-07 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 321.3 |
| 02c825a4-d130-36ed-aefd-e5c3f29163ad | -11.7221 | -45.3508 | 2025-10-07 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2ec0e5e3-28c0-3316-8bd7-021f02cdf850 | -13.2232 | -51.6744 | 2025-10-07 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.4 |
| f4388044-2311-3b16-beb6-f33e68f1682a | -13.7927 | -45.7627 | 2025-10-07 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 28376fe0-009e-3913-a2a0-044b52750237 | -12.9101 | -54.7558 | 2025-10-07 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| b6d9a9d2-69b3-339c-8f96-0716b711e960 | -10.4245 | -45.3907 | 2025-10-07 13:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 222.2 |
| a2ee24a8-3d98-331d-9afe-18866e5ca5a0 | -15.2978 | -46.3278 | 2025-10-07 13:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 6bebebb4-45a0-3b91-8764-a85d277812f3 | -10.8919 | -47.1153 | 2025-10-07 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 643b9ca0-7789-34f4-9475-246f0063936f | -13.2654 | -48.0855 | 2025-10-07 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| ac945bb9-ee57-367b-838f-7a832ff250b9 | -17.9979 | -45.0011 | 2025-10-07 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 2d9c7ab3-145a-37f8-865e-08fda128df57 | -11.2433 | -50.2859 | 2025-10-07 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 39ab889d-f1ac-3242-97ea-7a2e6b47391b | -13.3241 | -48.0324 | 2025-10-07 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 15998c41-e139-39f3-816b-252ccaeedf1c | -11.1455 | -54.882 | 2025-10-07 13:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 639.0 |
| a9d7da56-1c6f-3d91-a3ab-7da29fce9e97 | -8.6397 | -47.2769 | 2025-10-07 13:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 66874d49-c9ab-31b6-ac79-4be9c6e1034b | -14.777 | -46.0532 | 2025-10-07 13:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| fa4ac896-c443-377b-a20f-011898a9a32e | -10.456 | -48.3607 | 2025-10-07 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 4b397264-06d6-3ce6-a4e6-b54e3b63facd | -14.6327 | -48.3219 | 2025-10-07 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 246f2160-2aeb-3022-bb5e-2f65951a8bbb | -14.8645 | -51.4158 | 2025-10-07 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 71a412c5-5974-33d0-aa30-e83fc124d993 | -10.9109 | -47.1129 | 2025-10-07 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 9c27fd6c-084b-3703-8805-6498c37f566b | -12.8913 | -54.7372 | 2025-10-07 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 498.0 |
| f0daf930-e891-306a-a07a-ebb19d1015d4 | -13.2426 | -47.2391 | 2025-10-07 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 0ce4e7f7-a161-3ebc-a1a5-89fbfc61116b | -12.4665 | -45.5386 | 2025-10-07 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| b0f61916-233f-38b7-a283-86ab2606d265 | -12.2219 | -44.2308 | 2025-10-07 13:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 66a69b52-abf2-32e4-bf8a-0a1b9eead8f4 | -8.501 | -46.3117 | 2025-10-07 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 475d3686-423b-3187-85a0-6e7fbca7bdae | -8.1807 | -43.321 | 2025-10-07 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 3b1f8f31-eb69-3d74-b015-9b2bf9425cc8 | -8.5007 | -46.3342 | 2025-10-07 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 5dec8d70-50ce-3f5d-8912-58bcbb476ff1 | -13.0939 | -47.9992 | 2025-10-07 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 7af95104-a7ae-3c1c-82e9-fdf1d16a99fd | -11.6855 | -46.3593 | 2025-10-07 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| fac2d97a-ae20-3e03-b9b6-53533e6aaadf | -14.3148 | -45.8348 | 2025-10-07 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 0fa53456-377d-39c7-8035-490c2f4f3fe0 | -11.1453 | -54.9024 | 2025-10-07 13:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 290ac577-59de-3977-9efe-2dde12c750d0 | -12.4669 | -45.5155 | 2025-10-07 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| ed41c7ae-177a-3866-b378-2aa415f949f9 | -14.6322 | -48.3443 | 2025-10-07 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| aa26f03e-7f49-3e2b-87fd-35dbf0eaa314 | -10.3854 | -47.9956 | 2025-10-07 13:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 0e69a476-0dd0-3c9b-9814-7deec3432a36 | -14.8451 | -51.4185 | 2025-10-07 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 98638117-e112-3968-acf3-e152ae21b5d8 | -12.4476 | -45.5185 | 2025-10-07 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 259705e7-72e8-33e7-938e-f810b5dbaa5e | -8.1876 | -44.2514 | 2025-10-07 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| b9bf50c0-914e-35a5-9369-90e7614dfe30 | -9.1786 | -47.84 | 2025-10-07 13:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 2aef363b-4be1-3547-a6b3-ecf831747dba | -10.4054 | -45.3931 | 2025-10-07 13:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| a0f5ac04-7da2-3141-a537-b235615265e3 | -8.4519 | -47.2509 | 2025-10-07 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 480d5aad-9ec5-39ec-abb7-f8b46571ccaa | -8.5395 | -46.2406 | 2025-10-07 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| d0502006-7f59-3a73-80a3-106d6944d894 | -11.8025 | -45.1318 | 2025-10-07 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| fe22a84d-27bf-36a8-b7ef-4ddd7dadbd89 | -15.3737 | -47.3201 | 2025-10-07 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 93143a98-0b74-3e72-bfe4-76ffd165de4f | -14.8641 | -51.4373 | 2025-10-07 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 934c340e-8e36-39b6-9ef3-848b0bf88d4d | -8.1804 | -43.3445 | 2025-10-07 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| 45b27315-dcff-358e-b356-41ea0f9d6b8c | -15.3742 | -47.2973 | 2025-10-07 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e9ae3238-595e-3610-b7da-7565a46807e9 | -11.8029 | -45.1087 | 2025-10-07 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| cb44e47d-5b08-3346-b33c-07859d34e766 | -8.872 | -46.7655 | 2025-10-07 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c8103aab-05c1-35a4-96f1-1fd5bbc50646 | -17.9778 | -45.0057 | 2025-10-07 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 900a3cc1-8fb0-37b0-bd9e-400b727cdd14 | -9.1975 | -47.8381 | 2025-10-07 13:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b712c329-158f-3283-8f3d-9e86aa9577fa | -8.4821 | -46.3136 | 2025-10-07 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |


[Clique aqui para ver as próximas entradas](README120.md)
