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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34b45dd1-15a1-3fa7-82d7-affba72c22b5 | -12.9292 | -54.7538 | 2025-09-14 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 348.0 |
| dff9f854-0228-32f5-937f-2a6eaf83378d | -8.9979 | -45.7871 | 2025-09-14 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 15da2fa4-59dc-30e9-af43-0fb8a9b5b9c3 | -11.2927 | -50.8143 | 2025-09-14 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 957b2fdf-1bf1-3dc6-b64e-8bbf294d427d | -11.2698 | -51.093 | 2025-09-14 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 0e775501-2c30-3531-bfaa-1301508ca5de | -15.2186 | -50.129 | 2025-09-14 14:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| ef4f07f9-4f0c-342a-8439-7dc0daac2022 | -8.6436 | -44.0396 | 2025-09-14 14:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| f3028d45-9675-307e-9f02-5e9dba9b59ac | -11.8094 | -50.5428 | 2025-09-14 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 496c7df7-99ef-3b8b-a79b-a5ed653cda4b | -11.4097 | -43.5336 | 2025-09-14 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 892ea9a6-31d1-3c4a-9224-a2e0d79fc86b | -10.9477 | -47.1976 | 2025-09-14 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 4aefff22-bd38-3eeb-8cc9-8726f90d07d0 | -11.7894 | -50.6093 | 2025-09-14 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| d2fd7c49-4d7e-3d66-878f-478fc7af85a3 | -11.7706 | -50.5901 | 2025-09-14 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6f18a11b-5524-3373-8411-4d3548c48a4d | -14.2107 | -46.1749 | 2025-09-14 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 4a3724fd-16f8-3849-bf7d-9ebb7c0ce2b6 | -12.1048 | -47.5592 | 2025-09-14 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| aaadcc92-d06e-39a8-923c-3a77fd612774 | -10.9096 | -47.2023 | 2025-09-14 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 89351935-7694-30eb-a040-b87c55016d5e | -8.9365 | -46.1545 | 2025-09-14 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 7ed11b49-a7b7-3af4-b355-1800e10d77a0 | -11.6945 | -50.5988 | 2025-09-14 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3095eda1-6a42-3cd7-8bab-c1ad2b42d008 | -12.8208 | -47.1671 | 2025-09-14 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 4c50f6ab-0340-3863-ac92-0c57d7d04a93 | -11.2695 | -51.1142 | 2025-09-14 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| e0ed4f1e-d289-3e4a-9a5b-fe7bd95b27c2 | -8.9079 | -45.457 | 2025-09-14 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 074fbc18-39c3-3cc5-bc28-18fc3876754b | -14.329 | -46.0857 | 2025-09-14 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 253.5 |
| d86afe30-5901-3e22-bc24-9a73fc46ee6f | -8.9976 | -45.8098 | 2025-09-14 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1d3dba68-3ae1-3eb9-a342-1bb2d9e3c249 | -11.6243 | -46.5936 | 2025-09-14 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 64765dd7-3f0f-3180-8513-f75836548d67 | -13.5096 | -51.7451 | 2025-09-14 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| d521a587-58d2-3f05-b099-82cc5c35fb3e | -13.9283 | -44.8341 | 2025-09-14 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 487cf096-f102-3f2c-b596-655bf8d49b69 | -9.0193 | -47.0394 | 2025-09-14 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| e032cf67-9366-32aa-ad6d-f477c94f81da | -15.18 | -50.113 | 2025-09-14 14:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f05eee4a-e66e-3737-afb8-4df7a6f1b110 | -13.9278 | -44.8576 | 2025-09-14 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 55d6a317-8746-31f3-bb6d-9777e06d6ef8 | -11.2924 | -50.8356 | 2025-09-14 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| eabf8622-78a4-3c17-9b7c-18b4ceaed28a | -12.442 | -46.8847 | 2025-09-14 14:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| cfda2ddb-38ea-373f-a7cb-7b32af83001b | -10.7579 | -44.7721 | 2025-09-14 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 820658e7-541a-36e8-ab83-2b3e4e2518cc | -12.1427 | -47.5763 | 2025-09-14 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 164.6 |
| b1c31794-fe7d-3729-98a5-b9341baeb60d | -8.979 | -45.7892 | 2025-09-14 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| ff98ce5e-8426-336d-b52e-865508eb3636 | -10.9182 | -45.463 | 2025-09-14 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 258.9 |
| 6ef4a379-2584-3e9b-b494-edc55599ea51 | -10.75 | -46.4607 | 2025-09-14 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 9d831ff9-f4f1-39f3-ae35-e7bb89b2e2c6 | -11.3123 | -50.7696 | 2025-09-14 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| fe709124-d3a9-3e5b-8e0a-b26c1a56e28c | -11.5238 | -50.5754 | 2025-09-14 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 2ebe98f9-21b1-3795-935e-584e93c877ff | -6.3165 | -43.3381 | 2025-09-14 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4e85b174-dc16-3fd9-93d0-701bdd9d8685 | -14.3747 | -52.927 | 2025-09-14 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d0717878-40a2-3053-a0af-cc2606eeb2e7 | -6.9798 | -44.5529 | 2025-09-14 14:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 41935d14-d069-34df-8fb2-a47acab9b9c2 | -10.7472 | -50.5533 | 2025-09-14 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 9cb02bed-8efc-3432-b2a2-6896af7b1c6c | -11.3262 | -51.1293 | 2025-09-14 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 5717cc51-8959-3ed4-ac05-eb28b547fe19 | -11.751 | -50.6351 | 2025-09-14 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 00920bd3-7ab7-3a79-aa05-bf5b4b04dbb2 | -10.7285 | -50.5339 | 2025-09-14 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 4f23925b-5d4e-3f29-a8b5-a97e179ce220 | -12.0784 | -44.7199 | 2025-09-14 14:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 44d407b8-db8f-33d9-af2d-45c94f6064fa | -12.9482 | -54.7519 | 2025-09-14 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 2958220d-709c-37aa-bf2e-d62c8bbebf0a | -11.2888 | -51.0909 | 2025-09-14 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3b680ce3-689c-3fb6-ba97-9269b882352c | -12.9485 | -54.7313 | 2025-09-14 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 82e65434-459c-3f45-b2d4-1dc188d2341c | -8.9368 | -46.132 | 2025-09-14 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 162.1 |
| c24da557-105d-35d5-8f7c-c0451f08fb59 | -12.9101 | -54.7558 | 2025-09-14 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 4000010b-44b6-384a-9b04-13ca7d6e9cda | -10.7664 | -50.5299 | 2025-09-14 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e79b2dff-7938-3897-9d68-a79abbcc4100 | -11.2885 | -51.1122 | 2025-09-14 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3e29194e-94ec-3a40-8ff8-34f8c3804735 | -13.5876 | -51.6715 | 2025-09-14 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 81ebac4e-d7e6-3a32-8614-f8895004de31 | -14.394 | -52.9245 | 2025-09-14 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 0e359560-8f1b-3ea5-84d9-2803ac66e8b3 | -14.4137 | -52.901 | 2025-09-14 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| becde583-7b0f-3780-98fd-77dd6f783daa | -11.1237 | -50.7049 | 2025-09-14 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 609aaed9-859f-3f5e-bb01-406d9de5492b | -8.9076 | -45.4797 | 2025-09-14 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 02ac2e13-23f8-3636-83fd-3d1106af60da | -9.019 | -47.0616 | 2025-09-14 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 47be3efa-4e9b-3a56-97e0-c2698c49fa5f | -8.7683 | -46.0373 | 2025-09-14 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 70c1b3e3-574e-3f8d-9b13-ea28351e0b8f | -10.7104 | -50.4718 | 2025-09-14 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 51892f61-94f5-38a5-aed4-8511840c663b | -14.3285 | -46.1088 | 2025-09-14 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 052b9970-5498-3ecd-aed8-cec5c346152c | -15.7782 | -53.5031 | 2025-09-14 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| f5c50eac-7b3c-3677-805b-1dcd3054d4a0 | -12.1067 | -51.0208 | 2025-09-14 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ce96469e-01ae-3eae-9ccd-9977f8eb4396 | -10.8991 | -45.4656 | 2025-09-14 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.4 |
| f3bb2add-0ace-34eb-a6cb-8d7a2bf02a05 | -11.8284 | -50.5406 | 2025-09-14 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d978bec7-e7c3-321d-a87b-c88dc8e6d0bd | -8.4145 | -47.2324 | 2025-09-14 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8198a676-7ea9-34fe-9dc3-0138bdcc1668 | -10.3696 | -50.5283 | 2025-09-14 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 7cd4961b-1f50-33f8-8179-4ed66baefc28 | -10.7474 | -50.5319 | 2025-09-14 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 6f939529-8af5-31cc-ac7a-94453ba82c8c | -15.1995 | -50.1101 | 2025-09-14 14:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| fcbb04b9-9529-38b5-a6f1-0c4f73b5f81f | -12.7671 | -48.0236 | 2025-09-14 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 7bf22701-d8dd-38f6-85e0-ebf51bc7913b | -13.9468 | -44.8776 | 2025-09-14 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 220.1 |
| ca1d0173-a6b2-3ec8-af20-567871d4b054 | -12.8019 | -47.1474 | 2025-09-14 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 6426cda5-b59b-34e3-86df-80606dbe0804 | -12.7675 | -48.0013 | 2025-09-14 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e0af22cc-c622-3117-a560-d75df1667874 | -12.0852 | -47.5842 | 2025-09-14 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 90b07146-aeb9-3a33-aa9c-0f3d77e7267d | -7.5267 | -44.3874 | 2025-09-14 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f0058cc7-91b2-3969-a3ae-ab2a9c5cccca | -16.0061 | -47.9329 | 2025-09-14 14:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 92.0 |
| d569c27b-787a-3760-8ada-22904ec060c7 | -15.1991 | -50.132 | 2025-09-14 14:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 31d04d4a-63bd-3788-b8e4-d2d221ca5050 | -11.0563 | -51.4751 | 2025-09-14 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 450436c2-6c4c-3d01-b5e6-9bc615f87741 | -10.9286 | -47.2 | 2025-09-14 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| c3dc58e3-89dd-3453-a1da-1fd22912859c | -11.2933 | -50.7716 | 2025-09-14 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 2406fddb-090c-3d84-8aef-cb3755a66d60 | -10.5586 | -51.9661 | 2025-09-14 14:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 8ad158d0-dc75-328b-894b-1a0031ceac7d | -10.7683 | -46.5034 | 2025-09-14 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| af54d764-6e3f-3706-a96e-7ee2acce6a75 | -11.293 | -50.793 | 2025-09-14 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| fd751981-4d06-357c-9d9b-f3be1d3cf5ed | -7.1912 | -44.1195 | 2025-09-14 14:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 386175ba-7d92-3479-857d-e8781e7cb927 | -12.7827 | -47.1502 | 2025-09-14 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| efb995c3-4a50-3ee6-8c42-59fc21376fac | -11.5028 | -43.6846 | 2025-09-14 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| a3f16fe6-39ca-3f25-80cd-4467cf04a067 | -11.3831 | -47.3429 | 2025-09-14 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d497d964-e1b7-3802-8b5e-d4e804832047 | -6.9764 | -43.1387 | 2025-09-14 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 360844a9-e79a-33bb-9ec8-67b9bc8f2c1c | -13.9473 | -44.8541 | 2025-09-14 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| c5125d28-3605-3d65-8b5b-f7467bbcd5fb | -8.1386 | -43.653 | 2025-09-14 14:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 7f74467e-93d3-3df0-87dc-60574900155d | -15.0477 | -47.9856 | 2025-09-14 14:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d1df6baf-91d6-3f05-8e04-c883ec7e0ef6 | -9.8646 | -50.1951 | 2025-09-14 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4cc6982f-ccc8-38a8-8ed6-93b6e5d1998a | -7.5281 | -47.642 | 2025-09-14 14:20:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| c3153125-1b20-374e-acfd-f55fcf2b1b74 | -8.7871 | -46.0353 | 2025-09-14 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 195.4 |
| a88401b6-c59d-38a7-b8ae-f399e0a313e7 | -7.5269 | -44.3644 | 2025-09-14 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d25d9b83-4efb-35d9-894d-8aabda0fdd52 | -11.353 | -43.495 | 2025-09-14 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 4f114e49-0dd2-34b9-9140-b25b5bd58c3b | -8.6404 | -45.7122 | 2025-09-14 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 2edd6b98-f0ba-3c94-b05b-258a1a27767b | -8.4143 | -47.2545 | 2025-09-14 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 611f576a-b4e0-3003-939d-4462aa2f55aa | -12.0856 | -47.5618 | 2025-09-14 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 17a3d935-f079-3772-ac54-bb124e275bf7 | -10.5459 | -51.4844 | 2025-09-14 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| c8920c40-1b1d-3237-ac49-aa5f7aa5a349 | -12.9103 | -54.7352 | 2025-09-14 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 231.8 |


[Clique aqui para ver as próximas entradas](README90.md)
