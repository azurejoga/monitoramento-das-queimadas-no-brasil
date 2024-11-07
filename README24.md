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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5a1f3cf-4533-3fd5-a932-cd477034b139 | -3.7033 | -48.9986 | 2024-11-07 04:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 30f6feeb-a037-3195-8a44-caf78c2b92a8 | -2.6228 | -51.3038 | 2024-11-07 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 94c452bc-2234-38b8-b77a-8a46dfa7426a | -5.9786 | -45.3847 | 2024-11-07 04:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 6347b5e1-9e73-3ef3-a5e9-8d810dac2962 | -2.8536 | -48.6856 | 2024-11-07 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8640caed-1142-3764-9dbc-d316b89e08bc | -2.82 | -52.9409 | 2024-11-07 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8852759f-c028-3152-a21a-dd27955ae48a | -3.0023 | -53.4434 | 2024-11-07 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| e1963aac-3f09-34ec-a2c6-0ebc571fff30 | -5.034 | -46.8521 | 2024-11-07 04:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5b9f4af2-cfb4-3fa4-bfa2-a22dce4dd083 | -2.82 | -52.9613 | 2024-11-07 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 4b75a640-54e0-3d77-8b63-2f4f3dab4e94 | -5.9788 | -45.3621 | 2024-11-07 04:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 177.3 |
| dffc6f54-4fb0-3336-8d06-d47e53d4228a | -5.9975 | -45.3607 | 2024-11-07 04:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 03c4ec89-1192-3bcb-b7f9-34c260dc8e34 | -3.7033 | -48.9986 | 2024-11-07 04:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f08ae679-3e85-3aa1-a947-7566bb50d387 | -5.9786 | -45.3847 | 2024-11-07 04:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 655a4c58-cf3f-35de-958b-dfd928235fcc | -2.82 | -52.9613 | 2024-11-07 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2311c685-167a-3340-955a-48706f3fc7ee | -3.6602 | -50.2501 | 2024-11-07 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| fac42692-4e89-3f33-bb56-b216261e431b | -2.8201 | -52.9206 | 2024-11-07 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 15b7f8df-79b5-3b5f-9216-aa2dd9ab98e4 | -2.8536 | -48.6856 | 2024-11-07 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| a55f4d21-90be-341a-b26d-e7da61572902 | -5.9788 | -45.3621 | 2024-11-07 04:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 195.5 |
| f1885783-a81d-30bf-9b11-279d2a72f707 | -2.82 | -52.9409 | 2024-11-07 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| fddd1e65-497c-32b8-80ae-4c6258a50e1f | -2.6228 | -51.3038 | 2024-11-07 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| a563170c-9fb2-3db5-8f4e-ea47fe08e9c3 | -2.8537 | -48.6642 | 2024-11-07 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b50426f0-2bca-38b5-8253-c4e2bf8b132c | -5.0342 | -46.83 | 2024-11-07 04:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a2b94653-151f-3721-9eb8-a4a78d4c7ba6 | -5.9975 | -45.3607 | 2024-11-07 04:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 8ddfcf6b-4bc1-3785-9706-140cff81688c | -5.034 | -46.8521 | 2024-11-07 04:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 04ebf745-f70d-385f-a8d0-0494dbbf0fa9 | 3.36475 | -51.29417 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8b1df1d-dade-35e5-bd4f-4eb8842cbb10 | -1.42175 | -46.80227 | 2024-11-07 04:16:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14df568d-a448-3d9b-a8d5-904b38560fb5 | -1.92586 | -46.47989 | 2024-11-07 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e0809c9-9089-3553-a279-1a4fe7748ce1 | -1.19114 | -46.6673 | 2024-11-07 04:16:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98d81eeb-45e4-3fae-85bc-d9e132493320 | -1.35128 | -51.41182 | 2024-11-07 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7015f9f-a8e4-39a6-a67f-7534af81032b | -1.9294 | -46.48043 | 2024-11-07 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8431181-1212-3d06-8520-f19775e9a2af | -1.02186 | -47.06039 | 2024-11-07 04:16:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6d42a2c4-04d1-3478-a8f8-68d62633e2cd | -0.84348 | -52.84261 | 2024-11-07 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42cd2fbf-993f-3f3e-ba02-5e551a5475ef | -2.00566 | -46.82374 | 2024-11-07 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a943a34d-fec4-3b16-bba7-fc1d941b70da | -0.11199 | -51.39571 | 2024-11-07 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7d64980-b87a-3f21-8c64-35893897817f | -0.90668 | -51.65624 | 2024-11-07 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f2457cb-00d5-3049-9500-3cd324a59f87 | -1.80456 | -46.98602 | 2024-11-07 04:16:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92ae5f83-5829-3fed-80db-5695015f5468 | -0.16305 | -51.52579 | 2024-11-07 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9eec0e66-2205-38d4-90af-f46ded6d6a4a | -0.90623 | -51.6591 | 2024-11-07 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89aff9de-c37f-339d-93d8-6f1cb5874084 | -1.80819 | -47.92831 | 2024-11-07 04:16:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bb25ea36-66ec-3394-a6d7-ed7572576c92 | -1.02488 | -47.05829 | 2024-11-07 04:16:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 53bcb94c-ebe3-3a32-b545-4b4201a7c59a | 3.36522 | -51.29734 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e251eeeb-7552-357a-88e7-0dfb5b031f12 | -1.10935 | -46.83441 | 2024-11-07 04:16:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eba5cf64-c5b2-3eef-8844-259caadd37de | -1.85137 | -46.28654 | 2024-11-07 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da84f583-c366-30ee-8638-ded254512be4 | -1.47861 | -47.22139 | 2024-11-07 04:16:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e6e109f-96be-35e4-8beb-7cbed1084244 | 3.49669 | -51.24378 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2193730-28e8-39ec-a6df-f954b246f455 | -1.11724 | -52.26435 | 2024-11-07 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00c5d732-7aec-33c0-a88c-b8b8b50236d2 | -1.85972 | -47.82538 | 2024-11-07 04:16:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b9c35bf-2a24-305f-a351-a0e2d9dc49f1 | -0.84296 | -52.84589 | 2024-11-07 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d1439ab-ff74-38fb-9c84-012d7dbaf490 | -0.84836 | -52.84696 | 2024-11-07 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84b45c8f-8442-3c10-8618-24b5a9562200 | -1.71764 | -45.78009 | 2024-11-07 04:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a14c829-5399-32b3-83ed-7042eae06168 | 3.60344 | -51.31179 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 033aa839-5712-3778-872a-650ab94957f9 | -1.483 | -47.21765 | 2024-11-07 04:16:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc02bced-36fd-36cf-855c-3efa3d9ec890 | -1.62807 | -46.23343 | 2024-11-07 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ea95f8a-0e3f-352a-ab96-ae4b1c43d1b1 | -0.29506 | -51.40378 | 2024-11-07 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa334e6a-75a1-3a1e-b33a-e91d98ccc26a | 1.36132 | -50.94221 | 2024-11-07 04:16:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c55973d-776d-3090-a5cc-90495ec3d9b4 | -1.58274 | -47.56794 | 2024-11-07 04:16:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2161a1c-ae50-3f31-938b-0c44f36bc633 | -1.02418 | -47.06264 | 2024-11-07 04:16:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d0ee307b-f5d4-3d2b-b94b-617b43960a1f | -1.02253 | -47.05603 | 2024-11-07 04:16:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 27182985-5007-3528-8802-13b79e90af24 | 3.35766 | -51.28229 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff969de9-44ba-3b19-9e98-c5780010afec | -1.92649 | -46.47591 | 2024-11-07 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4089b5f-93c5-3f89-b2b9-ef3c1ec85454 | 3.36 | -51.29813 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bc08990-26c5-3b95-ac97-84087fa65ec2 | 3.35859 | -51.28862 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 631860ab-234b-3a2a-9cef-f75e9eabf1f2 | -1.94298 | -47.03231 | 2024-11-07 04:16:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de46d8eb-790b-39f8-99d6-6cc2612c2b9f | -1.58281 | -47.56559 | 2024-11-07 04:16:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c25ea1f-d0a7-33a7-b7ef-361d2f11a29c | -0.90713 | -51.65339 | 2024-11-07 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e07bd991-79c9-3ce2-9015-10656f28bb95 | -1.02119 | -47.0577 | 2024-11-07 04:16:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a0a94838-9b34-3b05-83df-1edb6917b3fa | -1.58658 | -47.56619 | 2024-11-07 04:16:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4990d833-4a8f-31d0-addf-347527ac58d6 | -0.84386 | -52.85027 | 2024-11-07 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d7a3697-3a7d-3fd2-bd78-c7b2ca1d0b34 | 1.35554 | -50.93746 | 2024-11-07 04:16:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4c6a9258-bc4b-362d-988c-9e6e7a6aa972 | -2.86772 | -40.04149 | 2024-11-07 04:16:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e839b206-9ba8-329f-a9ba-b0aaf4e0e873 | 1.75733 | -50.91586 | 2024-11-07 04:16:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e851d4e1-7320-3aaa-b0d1-2afc0f4eaded | 1.77473 | -50.44154 | 2024-11-07 04:16:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c91a57f8-7f59-397d-8b46-c7001975ec29 | 3.49148 | -51.24456 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b4a3487-0259-3f78-8821-2f3a833806ed | -1.11674 | -52.2675 | 2024-11-07 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a5ee88a-c0d1-3163-930d-44932154e5b8 | 3.35812 | -51.28546 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ceae173f-ba8b-3991-969f-600240bdff39 | 1.35639 | -50.94301 | 2024-11-07 04:16:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a04c3214-70a9-3724-aa9a-969386218ed6 | -1.34552 | -51.41646 | 2024-11-07 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6db32cfe-ab8d-39b2-9b51-3090788396a6 | -0.84441 | -52.84693 | 2024-11-07 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ba8304e-080a-3c4e-b73b-3d31ee5ef08e | 0.69525 | -51.44194 | 2024-11-07 04:16:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f26e574a-36a9-3cf1-8820-a2d1061a9f99 | -1.47423 | -47.22513 | 2024-11-07 04:16:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61e5b844-b925-3047-8b17-43c3c3ae2b17 | 0.53227 | -50.80051 | 2024-11-07 04:16:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 532a891a-2ada-33f4-858d-2940f29de96a | 1.77871 | -50.43556 | 2024-11-07 04:16:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5851558c-9e94-3670-9dd0-3cc5cb7153bd | -1.02049 | -47.06206 | 2024-11-07 04:16:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8452803b-0b4e-31a9-aa25-4cc8a6ea7279 | -0.84244 | -52.84923 | 2024-11-07 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2acc93f3-0ab5-38bf-8007-635905d548c3 | 3.60822 | -51.30795 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aa58a32-bdfa-3611-8195-a237c2a29a0e | 0.6957 | -51.44485 | 2024-11-07 04:16:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 690ae0c7-6204-397f-868c-fdf42bf8793f | -1.94662 | -47.03288 | 2024-11-07 04:16:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d1d759a-788c-328d-917f-33d0527bc744 | -1.92232 | -46.47934 | 2024-11-07 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89f4fd9a-a11d-38e2-95d4-a5dd54b6177a | -1.4793 | -47.21704 | 2024-11-07 04:16:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 611292b0-6cc5-3ffb-8772-12ee7c5fb052 | -1.22076 | -46.35923 | 2024-11-07 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3e6f3db-bc2f-3ee5-81cd-d249d6b7bc8f | -1.72108 | -45.78063 | 2024-11-07 04:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f0941c9-82f7-3b1b-a0ac-f88cb82b851b | 0.04523 | -49.52176 | 2024-11-07 04:16:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b43cb679-3427-3c2d-9c0b-78aad6b054c7 | 3.35953 | -51.29497 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a604d5f-8a47-39b8-8dd9-e8f6cca7ba9b | -0.84784 | -52.85033 | 2024-11-07 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b13cc9e3-671e-3990-b61d-bee11f938927 | -1.19288 | -46.66657 | 2024-11-07 04:16:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef50fc5e-b320-386b-9aab-c06650c1ceda | -1.93003 | -46.47647 | 2024-11-07 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 092660d0-b44c-370c-9de0-bf0f2e482268 | 0.04085 | -49.52246 | 2024-11-07 04:16:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98a7cf37-d93f-38fe-a57a-bea57e103727 | -1.68088 | -48.47256 | 2024-11-07 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fd1561a-fcf7-365c-b60c-00063a5975f3 | -1.10906 | -47.28192 | 2024-11-07 04:16:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0cb67701-14df-3958-ac95-5b095bd4db30 | -0.9944 | -47.61131 | 2024-11-07 04:16:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7a46420-d3d0-3c4f-a041-30d8b2db1ad4 | 3.35906 | -51.29179 | 2024-11-07 04:16:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README25.md)
