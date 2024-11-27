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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 614c2bab-ffdc-3a1e-be0b-18ac62430f80 | -3.69047 | -50.23013 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2b2d14a-6796-36e7-8066-60469ff3f3c2 | -1.94706 | -45.7281 | 2024-11-27 03:55:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a7e0eed0-fb6c-3558-a7a3-3220504723fa | -3.9676 | -48.06213 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c07382b-a931-3095-b26d-5dde464261eb | -6.38415 | -45.68465 | 2024-11-27 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a571ad7-8213-38c8-a5b4-116e5f8006e2 | -4.13986 | -43.84728 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c68fabe5-6e1e-34cb-be89-bdbe3a47be97 | -3.04475 | -48.51038 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 0a0f41fb-a0a5-3177-9651-e988fb669020 | -4.65655 | -43.81775 | 2024-11-27 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc68edd3-3921-34a3-a58f-ce885e75d96e | -4.17218 | -46.08321 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 458379a7-74a6-3aff-a42f-ae20e274e812 | -4.14014 | -38.70026 | 2024-11-27 03:55:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 379ef133-64a1-33ea-b5af-9e4650ed809f | -4.64732 | -45.93758 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da2718d5-ee57-3e8a-81e5-aa222f147cf7 | -3.88685 | -43.1575 | 2024-11-27 03:55:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 608e5a91-c541-3508-af9d-afb447674d0e | -3.2865 | -41.77497 | 2024-11-27 03:55:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e2d5da51-5b61-3f4e-ad31-b63e3661e350 | -2.50429 | -48.36201 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e5f9b2eb-a2dc-3292-8ae5-a9f8d5486430 | -2.82421 | -46.83122 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8596ec6-080e-3278-8e39-09514e49c793 | -2.53757 | -47.32877 | 2024-11-27 03:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42a3cdb2-6d88-3586-992b-1c910c9d4a53 | -3.04402 | -48.51464 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 2032af5b-f6da-3720-a76a-c117c1b13af0 | -3.96627 | -48.07007 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6401c99a-de89-3448-b86d-d42000b49ead | -2.63037 | -48.43137 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 332cf2d8-5a32-3247-a5dd-2a54da2f2136 | -3.37521 | -50.12033 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3befcb7d-07f1-30dd-b1ed-35785bc20edf | -5.20625 | -40.63389 | 2024-11-27 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 617f986b-78ae-3862-8aa8-1dfe5c822f1e | -4.39335 | -41.70578 | 2024-11-27 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f4ec4ec3-a144-36fe-833b-0d5e9f3f33fb | -4.25171 | -48.6804 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1409a2df-006e-3577-a6e2-857714cddcda | -8.02356 | -37.84812 | 2024-11-27 03:55:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 971b6232-4c7c-35b2-8cd5-d472695803f5 | -3.38962 | -44.1661 | 2024-11-27 03:55:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd5228e8-ae01-300c-b4fa-4f03b4048bdc | -4.40972 | -44.10995 | 2024-11-27 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0345ac7c-c301-3c30-9a6b-bfc6ad0a6439 | -5.84299 | -39.20749 | 2024-11-27 03:55:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| efb74e76-c6ae-355f-ae04-ecef403ab1bd | -3.3933 | -44.17107 | 2024-11-27 03:55:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2df4ffb9-6488-3824-9d9f-35ff662d71b3 | -2.11502 | -46.45848 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| f6f843f3-9868-3227-b027-aa328730283d | -5.98156 | -45.36403 | 2024-11-27 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 12a33a9d-e7a4-3071-af34-00751fb88877 | -4.32677 | -45.89193 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2821d176-8b80-3763-acb8-f982a19ca356 | -3.71073 | -51.79863 | 2024-11-27 03:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a780539e-3559-3788-a754-536ca30dda3a | -3.71764 | -47.12787 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 871bb0d5-a0b5-3d88-9e98-426feea8ddcb | -5.5848 | -42.93155 | 2024-11-27 03:55:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a1d75169-8822-3f44-8973-3a4f00e91eae | -6.99366 | -45.62315 | 2024-11-27 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34f6264c-9c1f-35a4-947a-4f273c8a9877 | -4.21679 | -50.8942 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| da4a0f16-e525-35ef-8bc4-a8996fb37d12 | -2.10331 | -46.56228 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8270b34-9330-37f9-b29a-f11b45f98d21 | -2.90511 | -45.23861 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e57a6b7-a859-305b-a742-6b2c665cabab | -1.54169 | -45.6926 | 2024-11-27 03:55:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 203f844f-76c6-3a61-b0f4-ae5b975dbdf6 | -4.00339 | -47.9163 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7bad40a-f2d1-34e1-8dcb-c84008409ae7 | -3.17061 | -48.44409 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 15f169ab-d00a-32eb-8a97-beac0771e414 | -5.22265 | -44.91212 | 2024-11-27 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 999de024-1351-3bea-9001-ddc3506c74aa | -5.20399 | -40.63415 | 2024-11-27 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c1c4569-3a3e-39e2-b452-d934760156ef | -7.52791 | -37.44661 | 2024-11-27 03:55:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5fde50f1-8072-3f97-afb4-61e6b8fbc60e | -3.68211 | -49.93293 | 2024-11-27 03:55:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e146082-2a5c-3e7a-9230-828fce4751cd | -3.93962 | -47.98745 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 687fb2bb-66a0-3981-8f93-c01b1c491406 | -4.47719 | -46.65859 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f0c41d6-7b39-31e0-bcfd-c319b72830b0 | -7.70608 | -42.99054 | 2024-11-27 03:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b3b59d8-61cd-3e5d-a1c7-f16b8f6f2744 | -6.63304 | -43.86023 | 2024-11-27 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33eb00aa-4ee4-3d2c-86a2-f520000cf599 | -4.44718 | -46.59837 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc5c38c9-875e-37f1-bf5c-ee7af4cf21b5 | -7.14566 | -40.25988 | 2024-11-27 03:55:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11b15f55-380a-321d-87e8-e505eae4219c | -4.40907 | -44.11401 | 2024-11-27 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7920027-2e78-3609-8ed5-ac646cb8540c | -2.53261 | -47.32457 | 2024-11-27 03:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fc74ed7-9622-3635-9b2b-cbe7d589fc59 | -2.04093 | -46.5152 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b984ce8f-31f6-3a69-b707-4336fb3a1378 | -3.26414 | -46.41648 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fe2eee6-8477-38c2-90d0-e8877a16e275 | -3.41481 | -50.20092 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da91d407-b279-3274-ae7a-f2ba52a23957 | -4.68759 | -40.69581 | 2024-11-27 03:55:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e42c40c-f095-3a1d-ba9f-5526333b5445 | -3.97585 | -48.06678 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acb99c65-e83a-3c20-9eec-afaa47f6e5f1 | -1.68083 | -46.91901 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2fe33d71-059f-3887-8ea1-56d7a5282b85 | -4.21853 | -50.90208 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 5842cff4-9a1f-3fa2-899f-27b3d2f4f97e | -6.77449 | -38.29793 | 2024-11-27 03:55:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1093bda2-edd7-37e6-8b0f-73290d79c10b | -3.43885 | -40.83606 | 2024-11-27 03:55:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 86e7e0e1-fb3d-326d-8d7f-adfee6e817f5 | -4.21871 | -48.6625 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 607f6ed8-9328-398f-a682-e43c3e1fde65 | -8.13231 | -44.46753 | 2024-11-27 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17606050-1468-3d03-8797-4b81eb045c08 | -2.42667 | -44.64663 | 2024-11-27 03:55:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b78cf401-94a4-3a01-9022-894cd33d8c69 | -4.40482 | -43.79325 | 2024-11-27 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d0669bd-4d27-3b9f-921e-bb19babc28b9 | -4.09695 | -44.85727 | 2024-11-27 03:55:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4acb04a7-667f-3f66-b91a-3dfb25de508e | -2.53815 | -47.32524 | 2024-11-27 03:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf177215-6181-3d19-a33a-4a33d97dbf06 | -5.18908 | -37.97527 | 2024-11-27 03:55:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92d7d724-8c39-3d68-ab0e-701031ec8802 | -4.04917 | -48.33129 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22282003-6c01-3974-b482-4e8d1f9c5532 | -3.81651 | -47.47439 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c13ed13-d4e3-3675-a117-43ca909582a8 | -8.39756 | -35.17654 | 2024-11-27 03:55:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 305a9b8b-0a85-384e-9f34-38705f3ede9f | -2.83374 | -46.83943 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4561b9ea-83ba-3ecf-8813-a882e088cb1c | -1.94675 | -46.60005 | 2024-11-27 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a49d6042-a626-30eb-b757-0f62d313190d | -6.03661 | -35.36416 | 2024-11-27 03:55:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 57a25c6f-9106-3f02-8b32-ae95d3a0f57d | -2.82002 | -46.8237 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f04c1ff7-ab3a-376f-abd0-2dd90f61f299 | -5.72568 | -46.1667 | 2024-11-27 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3082dfd5-d302-307f-ba59-0b26facae905 | -3.27077 | -44.54308 | 2024-11-27 03:55:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b38334f-f9cb-36e3-8ac6-cf25c1d7f35b | -4.1422 | -43.80704 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d755c627-4234-38bf-b3d7-ef09455a67ae | -7.9809 | -49.69044 | 2024-11-27 03:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1f8eee5-47ef-3bc9-8833-db664739a4eb | -15.883 | -43.46412 | 2024-11-27 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5d7b166-d9c5-3cf3-80f9-c654c60cd8e3 | -12.01888 | -49.54026 | 2024-11-27 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a164f2e6-543e-33a3-a2dd-66e1301e8162 | -10.14 | -36.19775 | 2024-11-27 03:57:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f6ebafc4-4fb9-3d06-a959-09b8572e0d8a | -10.3817 | -47.50289 | 2024-11-27 03:57:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a271a011-e5be-36eb-8b87-108ac9d1748b | -10.53183 | -49.05472 | 2024-11-27 03:57:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa023465-4223-3336-b55b-99520708df97 | -15.89071 | -43.46128 | 2024-11-27 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7480d048-8f30-3fd6-b5a8-21d3a9bfeb23 | -12.02293 | -49.54082 | 2024-11-27 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 010f5e42-0933-33e1-ac71-0f01d9bf4604 | -12.02225 | -49.54438 | 2024-11-27 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bec803fc-658c-3873-be13-70c4ea4cc2d2 | -16.37798 | -42.49963 | 2024-11-27 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acb3d742-a6c1-3562-b7a2-11722038ee48 | -15.88651 | -43.46474 | 2024-11-27 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20505552-228d-3578-976f-1552caa0d5cc | -16.37859 | -42.49591 | 2024-11-27 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afbbacce-75e1-3d23-8c33-72397ae635b9 | -7.85695 | -48.71466 | 2024-11-27 03:57:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da177009-1a05-334d-b904-70c49abfb3b9 | -9.73181 | -48.05877 | 2024-11-27 03:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8692e2b8-8e03-3cc3-bdbd-f73760736950 | -7.85766 | -48.71086 | 2024-11-27 03:57:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 907ff346-7ac6-3e88-8160-4578908bdd68 | -10.02507 | -36.18365 | 2024-11-27 03:57:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e5012270-43da-3154-a447-ae5d5c29bcd9 | -12.02899 | -49.53848 | 2024-11-27 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 270a8d84-e6f1-3d79-9282-9fa463d64cbe | -12.01817 | -49.54382 | 2024-11-27 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78046faf-b1f6-3934-a88a-00fe8087cc07 | -15.89002 | -43.46536 | 2024-11-27 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3ec624b5-f026-39a5-87a6-5b9c72c81dfe | -12.02357 | -49.54497 | 2024-11-27 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ce3b772-cd05-3b05-a5bf-db2360553d93 | -14.11891 | -41.67801 | 2024-11-27 03:57:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0dd0d7eb-f50d-3d94-86a6-38770227c618 | -9.97596 | -36.41481 | 2024-11-27 03:57:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README30.md)
