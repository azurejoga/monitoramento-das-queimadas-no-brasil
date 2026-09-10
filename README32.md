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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89da7f9e-7ef1-3296-863b-cd8f33db2e07 | -2.73097 | -57.61917 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3feac74b-78d7-32a2-bcd0-17ec632b03b6 | -2.89021 | -48.2761 | 2026-09-10 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4260746-dd25-3b0c-a0e0-b8fc29cbd609 | -5.75944 | -45.08792 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 503a1039-f595-3a50-9638-e6359b54fda9 | -7.50225 | -45.27343 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75c5c1b9-1650-38a6-b38b-c5ae6971295c | -3.3792 | -50.4031 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e662b20-6b48-3881-a363-41f787006d53 | -5.77318 | -45.08498 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 065f74a6-5ceb-33a8-9fd1-4ef7ff472202 | -6.25521 | -51.67029 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df685482-ef9e-3d51-ba9f-93cfda1b51dd | -6.24077 | -51.68038 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b01c19dd-6032-386e-8d7d-0e3ece282fe8 | -7.50893 | -45.27378 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d385231e-38fa-3749-aa71-21160a3e9c1d | -4.36359 | -47.78094 | 2026-09-10 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 896ddcde-4455-37bc-9528-a8c6c426fffe | -2.93184 | -50.47073 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe1f9038-6be4-3ecd-9417-a7a6c625b91b | -6.16246 | -44.63986 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 23cf4aa4-a209-37fc-bc72-9c9880734ba4 | -3.66273 | -58.89623 | 2026-09-10 05:10:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 288a8872-ea64-36b6-aa64-71f4d0ed2b82 | -2.9437 | -50.48112 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d88506b-bb2d-38ae-921f-cbcc19961d20 | -2.94274 | -50.46115 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2107e625-07d5-314d-b4e6-5a70d9f9c1ad | 0.26174 | -51.43692 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db44d251-4c31-332d-995d-cde86b3500a7 | -6.25352 | -51.68215 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fe05495-b882-353d-a05d-273d467d7673 | 0.24844 | -51.45659 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e1d9b1cf-5462-3bdc-b5ee-a3ed9b8a4a17 | -3.899 | -59.601 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3b2d0a0-71f8-3701-a9f2-49da59716a2f | -4.39527 | -55.77975 | 2026-09-10 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79f2c010-2cf1-3f76-9660-fe3e892335e4 | -4.86107 | -56.01873 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fdf9b054-2114-3a68-81dc-29c825616e7f | -4.86161 | -56.01522 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| efdc15a0-492e-3a7e-9cf0-44fe5f2888ea | -6.76068 | -45.47454 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94e2d597-e9a9-3b72-a120-913f30c83ae8 | -2.94191 | -50.46358 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e053155-c700-36d0-9578-9847ccec9138 | -6.09505 | -44.13691 | 2026-09-10 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9407fd36-b8fd-3259-9a3c-10f7eca31177 | -6.76946 | -44.56828 | 2026-09-10 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e5d01d9-f624-3f1b-99b8-739ac9d205fb | -7.25977 | -45.35572 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 95294c3a-ede7-3149-b480-7794a805c8a6 | 0.24528 | -51.46217 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ea1ef88-097b-31c2-8bc6-95a562ed3a03 | -5.76746 | -45.07817 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 6a8c821b-d323-38e9-be3b-2bfb6347ed95 | -6.16325 | -44.63388 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| da507ac7-6303-31a4-b4ab-5765be608ebb | -5.76518 | -45.09454 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 9bef008d-a93e-3da6-9f90-e750ecb78f50 | -5.37731 | -46.29247 | 2026-09-10 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 63832091-fc31-3283-89d6-9c91771a47ed | -5.37313 | -56.02449 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e1ffe06-b1a2-3a51-b223-88e4fd4fcffe | -3.55408 | -48.18345 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d7cd907-9cae-3348-8120-add9edad546f | -7.48828 | -45.27748 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4934f43-3d88-30d7-ad70-3fc8bd2af0de | -5.48126 | -45.13267 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2885fc65-2571-3f63-9df8-a6b7a084b3ad | -2.73394 | -51.37727 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7017d374-2dc4-37bf-b9e7-a13efedf61b1 | -2.35755 | -52.69165 | 2026-09-10 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b6c38be1-126c-3933-ab24-b2875ed861a5 | -2.93966 | -50.48222 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e95f7480-55bc-3e98-abf1-5c17ae0960b7 | -2.70658 | -49.51133 | 2026-09-10 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8800ed2f-befd-3804-b641-f444a1422718 | 0.24688 | -51.46966 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 05c3a8b8-3af5-39cd-86ab-92428be44793 | -1.19103 | -55.71921 | 2026-09-10 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8cb4b40-7b50-30bc-8eb1-f999248af1cc | -5.77396 | -45.0794 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 460e04e0-9d54-3d65-9e08-9cc92d67a3f3 | -4.36409 | -47.77744 | 2026-09-10 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e6149ff2-eb29-3683-9354-42582808fe45 | -2.71148 | -59.76847 | 2026-09-10 05:10:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 276e3a3e-879f-3730-85e3-d4e709546424 | -6.16921 | -44.64078 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e0004bbd-9434-3d3e-9b29-535bd014054d | -2.7332 | -57.62667 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b6b3db0-4fdf-3606-a180-9994d68642db | -3.21438 | -53.94537 | 2026-09-10 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20d1b40d-409e-392c-9556-aa85a2738026 | -3.41323 | -59.23263 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 61031e21-7b06-3f4c-a8c3-9abf224e22ce | -7.49422 | -45.28353 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8077729-b199-3af9-b850-87c3b535fec5 | -4.85827 | -56.01468 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 20df8ad3-d1db-3d52-9d84-b7e15eb3608c | -5.37258 | -56.02805 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60085047-02b9-3bbc-a171-34954947914c | -7.50964 | -45.26836 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53e5f5ed-c71b-3653-89fe-bc52bf4087e1 | -6.25913 | -53.11654 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c3a8128-4c1e-3ebb-a4c7-af9c379fd474 | -6.24446 | -51.68492 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a87776-2e3c-3aa1-9c28-a1dc5279fe89 | -5.27676 | -55.96561 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c580a85-c8a5-3a82-b966-e0fb2d054be1 | -6.16843 | -44.64671 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 04554207-2aa7-32b3-80a5-de209d912d12 | -2.73207 | -57.61219 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddb1c920-0730-3eea-a89a-d1e818e9aeb8 | -2.93711 | -50.46896 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c13ff5db-9fc8-3ea2-a5d7-4b41b12952c3 | -4.86255 | -47.40582 | 2026-09-10 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9a4bf26-9598-3b96-945d-f0e1f9e12501 | -4.85992 | -56.00397 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71b32214-9f6a-3dd8-8485-01359bd0670d | -3.43805 | -59.25618 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecf8d635-780e-3046-b102-fbe68009de2b | -5.28738 | -55.9636 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 449d5510-179b-38d7-8e81-fad04d00d37b | -2.74896 | -60.23427 | 2026-09-10 05:10:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f0a0f25-99fb-389b-807f-521050809c80 | -2.93494 | -50.47976 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82bec6a9-ed89-3277-8649-9b016af96184 | -2.94126 | -50.46779 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53d93a7c-3154-32ab-a13c-ee0e700254c4 | -6.16167 | -44.64588 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 0eb4d1f4-5ee4-31d1-a042-f6bda93a0075 | -6.24021 | -51.68433 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 616cba19-f6b7-3467-a13c-a39f75066147 | -5.774 | -45.07325 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 25eec8ee-b3ed-39a2-bcb7-c5ebc7e036d3 | -3.59517 | -59.07748 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 042dc6c8-ffca-3501-a361-242f72ded882 | -3.89838 | -59.60493 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ddc67ef-5a2a-34f3-b478-e14ca0c62666 | -2.73708 | -57.6237 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7f967680-8927-3e07-932f-4c10d3f7f214 | -5.27731 | -55.96204 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51c6661b-30a3-3573-bc08-963454a233d4 | -3.18182 | -57.89048 | 2026-09-10 05:10:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb3d0a9b-c877-31da-8944-f00aa20d7006 | -6.24558 | -51.67703 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afff02e7-04fd-35aa-8495-c44d786d6600 | -3.49781 | -59.57223 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cde625cd-a548-3a68-b80d-b4da45fb3ca2 | -6.24133 | -51.67644 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e84d8d44-71b2-3154-9ca0-1075c7371db4 | -3.54935 | -48.17954 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b1666d8-60aa-36f8-8654-aa13189fbae9 | -6.16999 | -44.63491 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 069e545a-6e7c-3057-817c-cb8e0d722a7d | -5.60575 | -44.84735 | 2026-09-10 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| df72eb12-d1ea-3570-b379-fe631e65cdc5 | -1.31396 | -54.22153 | 2026-09-10 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d092bc5-a071-3391-90ff-2012b8a2a891 | -3.42064 | -58.31699 | 2026-09-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83416688-252c-3750-aed5-c766c449990d | -2.93869 | -50.48452 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 609f229d-3864-32e6-a56a-f9367f366588 | -5.38309 | -54.44595 | 2026-09-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cd82c05-a448-3e40-a725-b23d2deccb00 | -4.20476 | -60.00217 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faf6b122-ec2e-328f-b320-3e5a5a3c5d3e | -5.37935 | -46.2914 | 2026-09-10 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e802746b-ee7b-33d6-b398-f0e8d53fb1ce | -5.76668 | -45.08375 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| bb41f0fb-98d1-3c61-afa9-6b0c8b0df50f | -1.4755 | -47.27199 | 2026-09-10 05:10:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ed4c888-fbe1-3aa4-a8e1-67c15fa8de26 | -2.93589 | -50.47739 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 319fc8cb-c3a1-3bbc-98c0-79fc5e170ae7 | -2.93835 | -50.46046 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65880634-c314-39d8-946b-a2f61528daa3 | -5.11749 | -46.00496 | 2026-09-10 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2e7e2ca9-36c9-34b9-8e3d-c06eff17d18a | -2.85844 | -49.53605 | 2026-09-10 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 883a62e4-6774-3697-8e52-68b50e4fae28 | -1.7243 | -55.74557 | 2026-09-10 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 643b130f-25ee-3e02-a12b-f106f1c75454 | -2.93314 | -50.46224 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06f5803d-dc02-3f02-bffd-155b57a6f005 | -2.41733 | -49.34565 | 2026-09-10 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 058e1c20-fd5b-3cc2-8a2f-f854db9e17d0 | -2.73598 | -57.63068 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f0b71bde-6cf2-31a4-8639-b5b6eae85e85 | -1.03662 | -53.73456 | 2026-09-10 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f206f222-4e9f-35f0-9306-9d81552321b7 | -3.37853 | -50.40746 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b2f7d13-1061-31cd-98c5-49e0c1a6c855 | -4.08271 | -56.30363 | 2026-09-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41117481-4635-371b-a878-63d6d3193112 | -6.10249 | -51.7395 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README33.md)
