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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ad6c9bb-fe8b-3172-921e-a664421a959b | -13.9278 | -44.8576 | 2025-09-14 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 8981889f-1ec3-357d-9df5-de1a6b8598be | -18.9845 | -48.6073 | 2025-09-14 12:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 95.6 |
| c0a67f52-ce30-3102-8bfd-e72768b1f3ad | -12.6824 | -54.6968 | 2025-09-14 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 16f4e3d3-bf42-39f1-a7ed-731bbbc4f3d3 | -8.9551 | -46.175 | 2025-09-14 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| df68679c-7729-3d42-ae6c-44a4a51ecb60 | -9.0166 | -45.8077 | 2025-09-14 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 36fcf35f-0223-360b-94bb-f40d8d6791d7 | -8.9179 | -46.134 | 2025-09-14 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 9c4c8f6d-7a14-33d8-8885-767c46299109 | -8.9079 | -45.457 | 2025-09-14 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| bfd9d7d8-705c-3978-98b4-a9ea0fe5e61c | -12.7017 | -54.6744 | 2025-09-14 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 356074c9-c067-3425-8f85-13eeb5f88bc2 | -8.9362 | -46.177 | 2025-09-14 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| aca4765c-d29e-30ba-a663-ea3e502cf4d2 | -8.979 | -45.7892 | 2025-09-14 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 50a7fd5b-b574-30c9-8a5b-0abb34418df3 | -11.8103 | -50.4785 | 2025-09-14 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 66b72097-2aa5-37ff-9483-ac845691beb9 | -12.6636 | -54.6782 | 2025-09-14 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| a8cbd8f5-63bb-3bf1-a63d-3d0e415008a0 | -12.8212 | -47.1445 | 2025-09-14 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 608c847f-49b1-39f8-a677-a2d5ec202472 | -8.7683 | -46.0373 | 2025-09-14 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 438.1 |
| 70882a89-37bb-35ce-9b53-bc1db0152d60 | -14.1917 | -46.1552 | 2025-09-14 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 469269b4-e034-3216-b4e1-9ee9fd4de86e | -12.7671 | -48.0236 | 2025-09-14 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 45f73dca-1c14-3003-a558-412119430871 | -12.6826 | -54.6763 | 2025-09-14 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 60c10308-60ac-3b1d-915a-e28858cf83cd | -6.9986 | -44.5512 | 2025-09-14 12:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c553ef42-b6b5-3a7e-a7eb-4f79c341ab49 | -6.9798 | -44.5529 | 2025-09-14 12:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| bea97864-9aba-3754-8a9a-25e2566bd0a1 | -8.9173 | -46.179 | 2025-09-14 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 8ebcaf65-f976-37a6-a3b3-1a8fa8e63fc6 | -13.9473 | -44.8541 | 2025-09-14 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 580a412c-d3b5-3145-b31b-7eeceb6a5e81 | -8.9793 | -45.7665 | 2025-09-14 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b60d2e83-9cac-3c57-9380-0ca58e28a093 | -8.9371 | -46.1094 | 2025-09-14 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 332490aa-9307-3447-b8b0-dde05f3a1dc8 | -14.3285 | -46.1088 | 2025-09-14 12:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 29d25e32-b381-3383-b22c-4bcfbded6cff | -18.9851 | -48.5844 | 2025-09-14 12:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 6edbcc8d-1a3a-3f0e-9eda-f4be567f536f | -8.9976 | -45.8098 | 2025-09-14 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 290.8 |
| 28b52337-6268-3dcb-8046-edb3f75bf534 | -8.9365 | -46.1545 | 2025-09-14 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c9632260-e5e7-3369-aab5-27b4b9d677bf | -14.2102 | -46.1979 | 2025-09-14 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 01724871-5703-3e7b-ac37-77e2d818b7d6 | -11.502 | -50.7699 | 2025-09-14 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| db65de0c-62b5-3031-99b0-1ac51d7fd3a9 | -14.1912 | -46.1782 | 2025-09-14 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 81338739-ebcc-3c23-97c9-f967815d26e0 | -11.5017 | -50.7912 | 2025-09-14 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| f6eb465a-9be0-3d49-8dbf-6766d56fa6fc | -12.8208 | -47.1671 | 2025-09-14 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 272.0 |
| f41aa6c2-412f-3332-886c-8833007b677e | -8.9368 | -46.132 | 2025-09-14 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 5f056dd1-ea29-3b92-a1f2-b53e8d2de7f6 | -12.9294 | -54.7333 | 2025-09-14 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 140.3 |
| bb6a0b2a-231d-3f86-90f9-fd01bde65c6a | -8.8109 | -47.1272 | 2025-09-14 12:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e088f552-9e1c-30b1-806c-d2f66953f2ed | -12.8019 | -47.1474 | 2025-09-14 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a366892c-f8b3-3314-99cb-d173922a6722 | -14.1722 | -46.1585 | 2025-09-14 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 5149f251-9eb0-3593-9429-3a175243a46e | -13.9478 | -44.8306 | 2025-09-14 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| d8ff3733-c100-39b2-ac03-adfcb521566e | -14.2107 | -46.1749 | 2025-09-14 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 126.2 |
| ee89832c-d91d-384c-88c3-8e1be89b99e4 | -8.768 | -46.0598 | 2025-09-14 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 95dd6f05-8d78-3fea-b28a-206f7672d04a | -14.329 | -46.0857 | 2025-09-14 12:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 8d2bc7d7-3935-353c-a543-c94dafaba0d2 | -12.7675 | -48.0013 | 2025-09-14 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| bc7019c6-cfaf-33be-8a83-e0d6c37ab2a3 | -8.9979 | -45.7871 | 2025-09-14 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 192.7 |
| c5f04fd1-2e31-3bc0-a9fd-d8f93372f91d | -14.1917 | -46.1552 | 2025-09-14 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 9a2ca18f-865f-3d4d-884e-bf4c48ae336d | -14.2107 | -46.1749 | 2025-09-14 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| aa24720a-34e0-3835-8f24-808a0749aca5 | -11.8103 | -50.4785 | 2025-09-14 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 36e00798-aa7a-3b6d-b9c5-d56709cb8ad0 | -12.7871 | -47.9764 | 2025-09-14 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 85ec7aa8-7164-306a-b74d-935817126b20 | -12.6826 | -54.6763 | 2025-09-14 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| b61c18d6-911b-3dac-84d2-074e72634583 | -10.8991 | -45.4656 | 2025-09-14 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| b8806fa6-c476-3bca-ba29-510f4f6a6be6 | -10.9286 | -47.2 | 2025-09-14 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 77f6d0c9-66cd-3eb8-81cb-c335320e3331 | -12.7671 | -48.0236 | 2025-09-14 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 23bfb373-6dde-310c-91b8-c2c214fe5378 | -8.9365 | -46.1545 | 2025-09-14 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e4346e9c-a3d4-3e52-a48d-0c16df80f517 | -8.9979 | -45.7871 | 2025-09-14 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 9c1a5963-33ef-313e-8dbd-b2cc2d3526f3 | -14.4779 | -47.3368 | 2025-09-14 12:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 03cd53c9-4165-319a-a0c7-15ea7c0bf081 | -12.5795 | -45.6591 | 2025-09-14 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| f79d05be-acbe-36ec-8fd0-313da5cf80d5 | -14.3285 | -46.1088 | 2025-09-14 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 295.0 |
| 2c510a91-48ba-3fca-8706-935f734b5438 | -13.9283 | -44.8341 | 2025-09-14 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 74219812-fb08-315e-9a3c-87ead272da7f | -12.8208 | -47.1671 | 2025-09-14 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 8bbcca24-6b6a-3b2a-840d-2c2aeaa59573 | -12.8019 | -47.1474 | 2025-09-14 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 97eaaf4c-c2b9-38a9-9f97-6329d5bf308c | -6.9986 | -44.5512 | 2025-09-14 12:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a3ed126c-2362-328b-b1a2-5c531de2580c | -18.9845 | -48.6073 | 2025-09-14 12:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 1ae4d7ef-e354-335d-80f4-904add053c66 | -6.9798 | -44.5529 | 2025-09-14 12:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 94b1c0db-e138-3b63-9bd1-9572d9664ea5 | -8.7683 | -46.0373 | 2025-09-14 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| de854a15-f825-3bbf-9853-131477c5377f | -14.1912 | -46.1782 | 2025-09-14 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a0a0be76-99e6-3109-ba6a-70e4af071bc7 | -13.9478 | -44.8306 | 2025-09-14 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| aed485cd-4150-3799-900d-958549230bfe | -10.929 | -47.1776 | 2025-09-14 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d2b6e7e5-ebcf-33e3-b817-73c675538f2a | -11.502 | -50.7699 | 2025-09-14 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 677d0b57-48f2-3b93-8016-dc7e44b2f54c | -14.3747 | -52.927 | 2025-09-14 12:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 24222333-8096-3a56-962c-3853e69ef120 | -11.4827 | -50.7934 | 2025-09-14 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| de53b727-5fd1-3998-bcfc-38353ee7c9d8 | -8.9976 | -45.8098 | 2025-09-14 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| bf824a3e-0c60-36a7-af74-9be8848be691 | -8.9368 | -46.132 | 2025-09-14 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 164.8 |
| bdc618bd-1e91-36e4-bec5-a97cdbe90fc0 | -12.8212 | -47.1445 | 2025-09-14 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 41eb790e-baae-3856-8c4d-b3c52d73cba5 | -8.9362 | -46.177 | 2025-09-14 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 7397a70a-9408-3933-b23a-5d73ef06c687 | -18.9851 | -48.5844 | 2025-09-14 12:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 4d48323b-e27b-3a4a-982b-32761c5822e1 | -13.9473 | -44.8541 | 2025-09-14 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 201.3 |
| f1957a7f-12dd-3362-a933-9054f8a803e3 | -14.2102 | -46.1979 | 2025-09-14 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 55987e94-d0b7-3e53-9a93-8239b244e6fa | -12.6824 | -54.6968 | 2025-09-14 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| cbdd2e12-c61d-3a93-a45d-949f8fef7774 | -11.483 | -50.772 | 2025-09-14 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| f66ae21d-e43b-3fdf-8295-f4c1d34ad9f2 | -12.7017 | -54.6744 | 2025-09-14 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 41ab6305-4af8-3135-8cd7-048a91cc1a75 | -10.9452 | -47.3538 | 2025-09-14 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e99fa172-3798-3135-a078-771eadf315cd | -8.979 | -45.7892 | 2025-09-14 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| f46ac327-7528-334d-8071-595853949653 | -12.9294 | -54.7333 | 2025-09-14 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 155.1 |
| 0ecd660c-2584-34e6-b41f-60efc1042d86 | -11.5017 | -50.7912 | 2025-09-14 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e78478cc-f24d-3cf2-8d83-afc551392f9e | -8.4334 | -47.2306 | 2025-09-14 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b6dbea46-c37e-385c-8c7f-ae60da2d8b31 | -14.3095 | -46.089 | 2025-09-14 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f88a947a-d0b6-348c-a472-5cd63128e807 | -13.9278 | -44.8576 | 2025-09-14 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 0b71a411-984e-33a9-aae6-040f7869ad04 | -12.6636 | -54.6782 | 2025-09-14 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| ca91b557-8456-369a-9970-5915f3bf1a8a | -8.9371 | -46.1094 | 2025-09-14 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9ab6c8ee-4c29-3093-ac06-1cf733d6298b | -8.9173 | -46.179 | 2025-09-14 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 35ebcdd9-4f92-3ab9-bcd9-3be291c5df37 | -8.9079 | -45.457 | 2025-09-14 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.4 |
| adf9fb10-2c11-371e-aac0-b07087e7ac2d | -14.1917 | -46.1552 | 2025-09-14 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| a0afbbb7-739a-3b69-93cf-04e7d35b34d5 | -15.7786 | -53.482 | 2025-09-14 13:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 2a750796-09ac-3c3a-b5f3-93f8027ee28d | -8.1383 | -43.6764 | 2025-09-14 13:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 40640ee7-74d8-31f3-9ce1-b8e3b1f65053 | -9.7389 | -46.8728 | 2025-09-14 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 00e04b97-24d3-3b71-b8e9-7fbd524d1dd3 | -14.1722 | -46.1585 | 2025-09-14 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a9884838-8168-3dd6-a6c9-bdf0d3b5978b | -11.502 | -50.7699 | 2025-09-14 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 413ff7ae-ab18-3147-89f6-80fd86e0a8eb | -8.7683 | -46.0373 | 2025-09-14 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 3329c4ef-e2fe-3c83-ad2a-7dda8c998389 | -14.2917 | -45.0964 | 2025-09-14 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 8ae6d79e-eab0-3873-a6d0-82d566c0f3d8 | -12.7871 | -47.9764 | 2025-09-14 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 28b9eb7c-73e6-390e-a8af-c98393b251d5 | -11.293 | -50.793 | 2025-09-14 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |


[Clique aqui para ver as próximas entradas](README83.md)
