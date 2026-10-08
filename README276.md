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

## Dados Diários - Página 276

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 775c9c0a-80c7-3d12-b093-7cf3dd538d79 | -10.88045 | -47.60741 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a6395e7d-9f56-3191-9aa4-a182cd42fe09 | -11.24798 | -46.27272 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e96bd94e-201a-3d7b-be92-174af273eef5 | -10.7565 | -46.60437 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a50a2b0d-72e9-3414-a4c9-b205e961b5ea | -10.93175 | -45.38639 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 1070aa59-480c-3f1c-9914-c135f563742c | -10.90621 | -37.85442 | 2026-10-08 16:18:00 | NPP-375 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7d7b9621-53bd-30b2-a840-7c84cb627402 | -7.21191 | -37.75392 | 2026-10-08 16:18:00 | NPP-375 | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e0c81c5b-8e21-3254-bceb-4af1ab6e97ff | -13.37542 | -43.87872 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ef3bfd1e-06a5-31b3-abf6-7fd1ce8612ea | -13.70949 | -49.12796 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cce16aa0-e7e6-37fd-91fa-8dd0dff9a423 | -11.40473 | -46.69882 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb18786b-1528-3dd0-84ab-fbded28c7f19 | -13.97331 | -44.83807 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 56d21580-0bbb-309c-b483-a59e97dd00c8 | -8.95879 | -45.16051 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 5188e6be-1090-3302-bf4c-ba17cbfd51e9 | -8.54767 | -46.91714 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9b9f51ba-6e6a-3f43-9d0b-d7a65a657da3 | -10.33778 | -46.23409 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b04a30e-1cc7-3d01-ac4e-86fcda5665ab | -8.40903 | -45.79088 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 882040da-97b7-3ca8-9673-e91005844f15 | -9.87775 | -44.86679 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 358.3 |
| f6581cf6-525f-3d6f-bda2-278a3e6f7bb4 | -10.52453 | -47.26006 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e62e42c-c7f0-30fd-b211-04d9ea881f55 | -8.94411 | -45.18491 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 951ba940-4db3-3790-a62b-ce09d0b56c72 | -11.61949 | -43.61586 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 32d9f6d8-00bb-3d24-b7fd-99d547e8a2f6 | -8.93017 | -45.1824 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 331.6 |
| 90f4f5dd-f726-39e8-be0a-8faea582ad9e | -12.24791 | -44.74594 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 4cf1333e-1a96-3f70-ac5f-03622a025a5a | -10.50175 | -47.28994 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b11c1a13-222f-38c4-a902-f8766db93476 | -12.16011 | -44.71372 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 27ea5756-93a6-31c4-9857-b72cef0140f3 | -8.93844 | -45.17676 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 263be51a-3f69-3907-b64a-f311b54a4e5d | -9.88925 | -44.85192 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c11d6afe-1b0f-3aac-ac4f-0104f520638b | -13.18721 | -43.50005 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 71604456-0cdd-33f9-852e-cd7971ceeb70 | -11.76514 | -45.56918 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d35bde34-35d9-3dea-8fa7-1ac0fb116c77 | -10.5889 | -47.30327 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28afe9c5-43c4-39bf-a86c-e80cbf4f481d | -10.58433 | -41.20267 | 2026-10-08 16:18:00 | NPP-375 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 3a6d2efa-1438-3ecc-bd4a-007b3d2e3752 | -13.96114 | -44.85493 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 07808824-328a-3c8e-a953-56de934b4e9d | -7.37568 | -37.9916 | 2026-10-08 16:18:00 | NPP-375 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2538a1a2-0634-3f21-9b59-b767fe8f43a5 | -11.33594 | -46.68891 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 93246834-9efa-313c-bb26-b36d9f1834d7 | -9.878 | -44.86148 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 440.1 |
| 9ec39e81-2234-3cd3-b58c-a6be39a51997 | -11.73278 | -43.5078 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 175b7302-dd63-3030-a5ab-067de269a906 | -11.63403 | -43.59848 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d0e4ad5c-5b03-32d2-bb86-5375981482cd | -11.40001 | -46.70251 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5b1979df-539c-3faf-a1fb-cf79614e4e75 | -11.24412 | -46.25197 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 62115807-2677-36dd-96f6-53ce03ab72bd | -8.93583 | -45.19051 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 56b6a408-25ab-3a6c-9c11-6936fdefcd05 | -11.7345 | -43.64268 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 3f21d690-7bc3-3107-8a75-6137b3d46531 | -13.9543 | -44.85373 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9d8a5387-eb44-3aa2-a4db-c51c4b7ea014 | -10.58361 | -47.30383 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e3e07dd3-eab3-3ddf-b428-af0920fe2b00 | -8.49974 | -41.26241 | 2026-10-08 16:18:00 | NPP-375 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 1ce17118-d971-3d27-9f59-22a8c695dd0b | -8.60576 | -45.62756 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d3ef1775-1108-3401-a8f2-dc9b52ec51e5 | -11.39557 | -47.56723 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c96cacdc-95d2-30bc-9bbc-cda2eee55ad1 | -8.96493 | -47.54636 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b8e41d4-63bf-3029-a563-0a9b97d3672a | -11.23375 | -45.24494 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 14319419-dac5-3c8a-8fa2-a5b32eb32331 | -13.03727 | -47.16372 | 2026-10-08 16:18:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 487fa04c-df5c-3976-a9ff-a260404237ec | -11.59504 | -43.65418 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| cabf9c3c-e679-3944-b73d-5abb964359e8 | -11.96566 | -47.76693 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 16acb0fb-e989-3ce6-8953-d312a13a8b46 | -11.84442 | -48.09789 | 2026-10-08 16:18:00 | NPP-375 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 252b1829-6567-3c1b-84d1-cd40fafea05f | -11.24513 | -46.24986 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3d3b33c7-278d-33c6-a4d7-f71558fbfc6c | -11.58875 | -43.67052 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 6efb4035-d7fb-3af9-a145-7b20729bb177 | -10.25169 | -49.67934 | 2026-10-08 16:18:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1d25c406-02af-369f-935a-9c1575b73de9 | -11.10914 | -43.9972 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d25038d1-521c-34c1-b1e9-0969b365a505 | -8.75549 | -47.57584 | 2026-10-08 16:18:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81c87cd4-ed92-3937-864f-777c4122e4b6 | -8.29379 | -45.73212 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 533df7fc-9aaa-360f-978c-66efaa000195 | -11.2494 | -45.25693 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ca037e53-3cb7-304b-be9a-2f8f7fc3b2f5 | -13.12494 | -46.36107 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 0b98e71b-fed5-3c56-8976-c3e12c9d29fb | -9.35028 | -45.42136 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 318dcc58-aa94-3e61-83c9-81442d2c1398 | -10.45238 | -47.2798 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| a4f9c67b-8388-35f8-9ae3-262f00991e9a | -12.1779 | -44.81492 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9ea64d45-f320-3430-972f-85152d72295b | -10.45404 | -47.29288 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| d73d30fa-d6e6-3358-aed7-80854b7d3833 | -10.16884 | -44.67359 | 2026-10-08 16:18:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5c9af217-3080-3e3b-819a-c46b16f4a32b | -9.93842 | -43.56211 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 3537948f-876e-3af3-8570-d1d59a8ac638 | -9.88215 | -44.86611 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 224.3 |
| d8e99342-efa2-337c-9e23-58e5b35fb0e8 | -10.80551 | -47.33303 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| acdb91e7-c4c4-3199-8366-c9f3191f0e96 | -11.20166 | -49.42625 | 2026-10-08 16:18:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ce49ab44-3893-3879-9f5d-c2dffce5e9de | -7.23131 | -37.94584 | 2026-10-08 16:18:00 | NPP-375 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 20.6 |
| a33d88f9-fa9d-3e49-a0dc-27f54711ffa8 | -8.94557 | -45.13692 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 43027300-e99c-3b08-bbac-e7ac33002200 | -9.8912 | -44.79933 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 7077ab98-dc1a-3805-83a9-00227b1d0777 | -11.09246 | -47.51525 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ffaa664-e7f3-36e4-8151-fdae792dee0b | -12.23885 | -44.74714 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2a6e4b81-7424-3658-9874-2e9f6990caf8 | -10.00902 | -45.51117 | 2026-10-08 16:18:00 | NPP-375 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac3bdac3-f1e9-37c7-b454-5bfb68cb4476 | -8.28459 | -45.73075 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 6800ef5c-bbbd-3a2c-950c-3f30f3a3110d | -10.5815 | -47.2873 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ad92f6f2-e385-373e-9c29-55d0957e7742 | -10.38228 | -46.30677 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 68d49993-69cc-3d1c-a9e6-f28957a3c24e | -8.55564 | -35.8706 | 2026-10-08 16:18:00 | NPP-375 | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c30b2bfc-ecf0-3b79-b932-fb1a0ee6d176 | -9.84344 | -47.46861 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f9fcd1c3-f97f-35a3-92c9-c9e3606e2242 | -8.75597 | -47.5773 | 2026-10-08 16:18:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf0865c0-0088-3132-83d5-9c8fb29b908d | -9.74551 | -46.95219 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e476411b-30c0-36d5-9a31-edc9bca42e47 | -13.55116 | -49.14697 | 2026-10-08 16:18:00 | NPP-375 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b436860c-d345-3d0c-b1c2-cd2e1f5c5c5c | -12.28161 | -45.31186 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9a752981-7e73-375f-adf9-8b0626a7b8df | -8.92957 | -45.17803 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2be79b09-32c5-3735-a6a9-067beccdc094 | -10.07416 | -46.00367 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 50b975ae-ca0b-3239-8f90-a824d4fe0b1d | -8.17802 | -39.69168 | 2026-10-08 16:18:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b2c04651-e33c-3abf-98ac-d3d9a1782efb | -11.84812 | -47.30149 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3552afb6-f85c-39f8-a889-d34b2ca3381e | -9.94111 | -46.81562 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 78fe3dd8-77ea-34cf-bd9b-cfb8c4e4007a | -10.50701 | -47.28926 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 02b8f3d5-80c8-3b1e-a3a9-eb8d4572cc7c | -8.80259 | -49.01281 | 2026-10-08 16:18:00 | NPP-375 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 132815c4-c110-393a-b776-9b3d030d6bcb | -9.75711 | -44.79554 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4f9a8e3d-f520-3cc9-86f7-cf1788669387 | -12.22686 | -44.76611 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a543e25e-64f6-31da-acf6-5b2b2d7f8107 | -11.2377 | -46.24144 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| ef1b3138-853f-36d7-82b7-53b729bedfe9 | -10.03979 | -45.60028 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0ba98db8-a828-3333-90b5-09351e1f5fb6 | -11.08162 | -44.0171 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 2794945a-b189-3ba7-bf0d-525a23677a06 | -9.43813 | -41.73861 | 2026-10-08 16:18:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f626bfb6-ee46-3f58-8121-ea2735fca323 | -9.93891 | -43.56566 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 50588c6b-3c5e-39ea-8b6e-d3944fcf29ef | -10.68427 | -47.83083 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5d62a26f-b751-343e-810d-eb9752c096d0 | -11.83444 | -43.52511 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| ef08ee08-8dc3-3f64-9b6e-27987af91603 | -8.28681 | -45.71489 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 83db0f36-2b79-3e58-88f6-ac60d6a53b62 | -11.8008 | -43.5261 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b1f69fbd-e789-3803-b93b-b90e3b4f282c | -8.89063 | -45.39367 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |


[Clique aqui para ver as próximas entradas](README277.md)
