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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7df553e-1186-38c1-b848-23f50ed39575 | -4.40158 | -49.6346 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7dcaedcf-f299-3e3b-a200-b142b68f8281 | -4.39476 | -50.3232 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23dfbb46-5267-3ca3-90a1-a529dadc789a | -4.26724 | -50.67045 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5be9712-2c24-3011-acb3-33781f3a8eb3 | -4.26662 | -50.6746 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40b79fac-d65a-3acc-81c0-506ad96dcd21 | -4.26351 | -50.66548 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b6327aff-cf87-357e-9af1-19a1d24a8144 | -4.26287 | -50.66972 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| c5bd5b5a-7402-3c80-8618-315addc6f674 | -4.26225 | -50.6739 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| eb911dd6-60bb-35c7-8e59-7ab662382de9 | -4.26163 | -50.67806 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7da92a01-22f3-3bbd-b61d-7faa3ed374fd | -4.25913 | -50.6648 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 925e9cbd-8721-3d82-9038-83457f5d1000 | -4.25851 | -50.66903 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 771abf5e-d743-3cff-8b37-4d063c9af8df | -4.25788 | -50.67323 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| c03c3aed-3cf9-3be1-a6dc-76b9f205bac6 | -4.25476 | -50.66413 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ce3ab25-47b8-3483-9b4e-2d693c89ccb2 | -4.23731 | -50.69159 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba63cc94-084a-3288-9fd8-9f3ea7553475 | -4.09988 | -50.52637 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72e4f48d-26ce-3e60-af72-badcd03d2d06 | -4.09923 | -50.53068 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c26deb85-5106-3a82-87d0-7734c452ec1e | -4.08159 | -50.52816 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2038b7c4-554b-3710-911b-b1a0dc1b03d1 | -4.07785 | -50.52307 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d313f59c-ac71-371b-9342-263674ce321e | -4.07719 | -50.52747 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10377f3b-51c4-302e-998d-1f70c88abaea | -4.07655 | -50.53176 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 085ab3b0-d971-3a64-94e6-e69819dedd2e | -4.075 | -50.00843 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93a2e2bf-e350-3bae-9163-7f63a3bd110b | -4.07429 | -50.01307 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 73c53d4b-f6f7-3f27-97f1-f9b4aaf8ee92 | -4.07361 | -50.01763 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8925657e-352b-3d4a-aa6f-485c92fec935 | -4.07009 | -50.04087 | 2024-10-30 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 78d79106-06bf-36de-89fe-236134b4f391 | -4.06974 | -50.01235 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 51a224bd-d6ba-3ccd-b953-9bdd8e54e5e9 | -4.06905 | -50.01694 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 2303648a-5ea0-3a99-a758-e319303eef46 | -4.06835 | -50.02155 | 2024-10-30 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dac8ae3f-bc87-317c-99c0-c382f19d38b5 | -4.06553 | -50.04024 | 2024-10-30 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 74d2fd01-6b33-316f-8ec8-53fc75991a19 | -4.06448 | -50.01628 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c006dd61-945a-33ed-8516-007b422ce1f4 | -4.06377 | -50.02097 | 2024-10-30 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d263921-96d1-3d68-9faf-05aa0556de32 | -4.04196 | -50.55273 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4b4da6a-60d6-36de-ae5b-bf843997a474 | -4.04133 | -50.55704 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 559bf587-77a5-3c20-adf1-ef4380820e88 | -4.03756 | -50.55212 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b36f37b4-12b8-3324-9b9b-15a1bcff5230 | -4.03693 | -50.55643 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7a6d9f1-13ab-39f9-a464-b95a0e4b2f9b | -3.9351 | -49.74883 | 2024-10-30 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a751f6b-537d-3c9c-9a8b-7fed4aa3a6db | -3.86632 | -49.99257 | 2024-10-30 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ef61ac0-17a6-38c1-b689-314c4dba10f3 | -3.79679 | -49.86276 | 2024-10-30 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3c013e6-e9e9-345a-bcc5-ddc238ab68b0 | -3.79219 | -49.86207 | 2024-10-30 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5b2418c-9320-38c6-9c75-cc45bd2f2bb5 | -3.77519 | -49.97913 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9d05b76-4037-3eec-8547-eb74cfe9bac7 | -3.73813 | -50.06429 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07554d70-57ef-3298-bf3d-13b1c284f61f | -3.73009 | -49.8064 | 2024-10-30 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 684b41fe-6cb0-308b-becb-b12102f7e51f | -3.66993 | -50.11917 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef1be36a-124a-3a1a-a8be-19560a91617b | -3.66612 | -50.11382 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59dfde69-6f56-3153-9e2d-f898a601fd96 | -3.66544 | -50.11844 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aae0d58d-f809-3bde-ba3a-912f0bd0c215 | -3.66476 | -50.12302 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebe41c79-3172-33a8-bd9e-3f82896f9728 | -3.65497 | -50.15842 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff377392-f322-3d6f-b1a9-1960151056af | -3.65431 | -50.16291 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fb9c367-5bf4-3865-a664-36b41666a833 | -3.65365 | -50.16737 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a39bc7b1-c788-3c78-8cfd-3fdbb34bfeca | -3.64982 | -50.16224 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2be7189-1ede-3352-b775-65e888bea0f4 | -3.64916 | -50.16674 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e34a288-3ea0-3859-a990-a559ed46a146 | -3.62806 | -50.17004 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e1069f0-a339-3c11-a089-e54a6d2ce90f | -3.65336 | -50.44463 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3670dbaa-47f1-3fd9-ac42-19a4341a1723 | -3.64896 | -50.44395 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3af2d39-3429-3c02-af74-8fb302455137 | -5.46941 | -50.53351 | 2024-10-30 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6603bcf2-439c-32ce-a04f-654c329fffbf | -5.46584 | -50.65158 | 2024-10-30 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f77762fa-dec2-3ed3-95e2-08bc781f6b47 | -5.29403 | -50.57109 | 2024-10-30 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69e54fe3-8cf6-3fca-9249-fa7fe2ac3f3a | -2.1961 | -51.41494 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b1aa88d-4729-322e-98ad-4c2f7c50d29b | -0.12814 | -51.29731 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9e2bb1a-4f10-3213-8c1c-13209d8cbba9 | -0.10276 | -51.30737 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 697d6e78-4ffd-3697-864d-9dfd732092f4 | -0.1022 | -51.30871 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 856af112-42d8-3f2c-9200-7b430f8af7f9 | -2.19777 | -50.58161 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ff47b1b-d3e4-3236-a635-75d14e9bba48 | -2.19657 | -50.58958 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d199e96b-e50a-37e3-b8dc-c9c6b2c46a2a | -2.19597 | -50.59357 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc54c262-5959-3d0a-a961-7b7849ae773c | -2.19537 | -50.59755 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb2373e8-8ac2-3dba-998b-8e3c33348c65 | -2.19291 | -50.58495 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6538498-4058-33fc-b4ae-23bcd245f100 | -2.1639 | -50.63329 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f2ecc58-67e4-3e50-8064-89e54f4808b2 | -2.16024 | -50.62871 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dc81547-5f19-379e-8cb3-02f2e7349eb1 | -2.15618 | -50.79988 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed864eb4-c296-3ee6-9e84-4281d950b4ee | -1.96848 | -50.72514 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92ac4d0c-0ba6-36f7-8580-28b002b725a8 | -1.96427 | -50.72448 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df1a8cc8-0c7b-30f4-96c9-ffa9343c4e87 | -1.86116 | -50.99559 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef6f340-e0fa-3cb9-9133-7ea016945adf | -1.42131 | -51.6032 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81eb938e-e35b-3031-a57e-39ebac631d64 | -1.41737 | -51.60259 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7515d15a-db60-3ad1-aac3-e5e73501270c | -2.19717 | -50.58559 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffb8eddf-96ab-3313-96ef-591209178be7 | -2.19231 | -50.58894 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a43f1d4-2434-37fb-a4f6-75be1b0673cb | -3.39385 | -52.05422 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ac5ee8f-9f00-362b-81af-a093a28add7a | -3.39165 | -50.80631 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f2fc061-8944-3874-b9c6-8db6a9bd4e8b | -3.26371 | -51.02267 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1efb895-8a61-3c55-8961-e54c0c830045 | -3.2595 | -51.02206 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8a33710-ba52-3e5e-8dba-592d06490a67 | -3.23501 | -50.7321 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30c97ab2-7bec-3aac-9878-c8023233b744 | -3.23369 | -50.7313 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4a31564-05b9-318a-8758-3522bd169b4d | -3.22355 | -51.0324 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b98388a5-b9c0-3167-8a69-6c58c2ce83f8 | -3.20846 | -51.01836 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 554e1e13-c7b5-33a7-a5b2-69b496b40baf | -3.20594 | -51.37221 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecb1d70f-b984-3036-89b8-32ea7f74c1e5 | -3.20425 | -51.01778 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cc16824-07dc-30ad-916e-74079fd3f50d | -3.20303 | -50.82574 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40f506eb-7d6e-33b1-9d05-cd0b03a7e62c | -3.18651 | -51.36191 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f970516-39dc-3ede-bbb0-227b7dbac316 | -3.18625 | -51.25204 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54bb6a1d-fdee-33a7-9e19-fd694b5a287e | -3.18315 | -51.15942 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f98929e2-c769-3211-935c-6aaa9ca853a6 | -3.18249 | -51.22068 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19553ad4-0cd7-3237-9cfe-5f3ed9a2688d | -3.17617 | -50.59832 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b727427-52c0-3d8e-b84a-3b79c2d98535 | -3.17246 | -50.59356 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 598ff9fc-e690-32e5-a314-9f839321a3ef | -3.17123 | -50.60178 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8946e587-a0c1-3892-b013-b2e83535ab20 | -3.16814 | -50.5929 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d2fd3637-5a0a-3f9c-b163-55bfc6e03f17 | -3.16691 | -50.60112 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 88751bc1-59bf-3b22-9adc-25b24cfb097f | -3.15953 | -50.62103 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92e34917-59fb-33a7-ad8a-da54de4ba9e9 | -3.15888 | -50.5957 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c70be624-416a-3d6f-9b96-fa7cd1043acf | -3.15516 | -50.59095 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d44674a-d0d2-3122-bad8-55ef8937e322 | -3.15461 | -50.62446 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 903a0517-b4c5-38f9-8f6d-7821fcc75116 | -3.15455 | -50.59506 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fb14863-ddce-3a4f-b788-95af4fa4b797 | -3.154 | -50.62853 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README88.md)
