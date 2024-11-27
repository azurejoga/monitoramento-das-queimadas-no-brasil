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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23847f6f-2f48-3fab-acfc-c36d8a2af4bd | -2.56263 | -46.41825 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11153e78-7bd7-3342-a7b6-01cd7fd89115 | -1.7181 | -45.37602 | 2024-11-27 04:18:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d4137dd-7fdf-3638-8f0a-447071ac0214 | -2.32142 | -46.1172 | 2024-11-27 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c4a9d49-6600-3e02-909a-55661fcd6069 | -2.26116 | -53.749 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba96cb8b-90f7-304e-994d-4d47f96d89f9 | -1.2676 | -52.22939 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54ea1885-cf06-3f9a-9c63-d09cdca9054a | -2.9334 | -48.01832 | 2024-11-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ee94787-3ed2-3b26-a099-9d3f1bf1b649 | -3.45624 | -49.69593 | 2024-11-27 04:18:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99bc44d1-3ac3-387d-90c0-413e20f48248 | -3.51517 | -50.21969 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90f49e1e-509f-3a85-8c8f-1b244715df56 | -2.60102 | -51.82986 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 18875505-7949-3495-8ded-6234f726ed50 | -3.70978 | -51.80729 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2908c46f-2985-328b-9dcf-fc54bf02d648 | -3.77781 | -46.51193 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d915988-2cee-3c21-8175-bc071b8a05fc | -4.40963 | -44.10894 | 2024-11-27 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8b63163-0112-3f1e-b71c-1841ca2cddc1 | -3.17447 | -48.43204 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 191118dc-170a-3570-b414-28bb708b2c78 | -2.80808 | -54.13409 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c51f3cb0-9e56-3033-827f-177979b201a7 | -3.9793 | -48.06714 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 879be598-6af4-39f0-a075-5ad9d7248782 | -3.99353 | -50.55837 | 2024-11-27 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11a6fe38-de52-3eef-a0b4-429281223af4 | -2.83137 | -46.83884 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 40be5098-ee31-36e1-907d-05f08056f375 | -3.93919 | -47.98206 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54608c06-6814-3b97-a1ad-6a0569d4f86c | -2.42346 | -44.64707 | 2024-11-27 04:18:00 | NPP-375D | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6027bc65-6af6-37d9-8aff-54acd86698a1 | 0.97839 | -50.12727 | 2024-11-27 04:18:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13386a14-1383-3774-9fac-4fa1c54684a7 | -3.11132 | -51.26012 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b912b09b-7332-3066-bd87-681f7431d6bf | -4.17671 | -46.56453 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caf36abd-7fd0-30d3-a724-9fa48d9e28e9 | -2.5791 | -45.47456 | 2024-11-27 04:18:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e65b4a07-b8b8-3ea7-b1f2-7e7eb4724788 | -3.15384 | -49.24701 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d377555-36c1-30b5-9edf-0f07c2fdae5f | -3.11444 | -53.27429 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86953326-4b85-3d1b-a5d7-862edd81f0c8 | -2.70484 | -46.20249 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56feef41-58cc-30c0-9147-bcc0472fe6c7 | -3.34703 | -50.7521 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4b61e47-a1c2-3a07-b587-c5e4b67b030a | -2.78742 | -49.21256 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 837ef5cd-0d44-3ce1-9865-07e3540e859d | -3.97277 | -46.73422 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8d21797-6669-38c3-8a2e-557538a4d83b | -3.17759 | -48.43764 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59764cb1-8099-3034-bb65-c3598d00191a | -2.58141 | -51.92076 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8211cc21-6a75-3339-b2eb-d9a11e9575ba | -4.04983 | -46.83521 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab6c5cd-5d29-395d-8d11-de71e23783dc | -3.71139 | -47.12449 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a3c80d9-ece9-356c-82cb-45adacb9aaf3 | -2.17707 | -46.38845 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 931e9b7e-7f35-3294-bac6-15826a99d5a3 | -2.58466 | -46.18847 | 2024-11-27 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73aa4d66-3a6a-3bc6-8c87-8c2c4f09abd4 | -3.98004 | -48.06262 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b05ae60-a015-36e4-860e-4c9507ad018c | -3.11252 | -51.25368 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88c1682b-6e33-3294-89fa-d0022c6910bc | -4.16912 | -46.07909 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8923ff86-b380-33b1-9bc8-7b3f5f1cb86a | -3.97019 | -48.0751 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42561337-9999-363e-8c8c-0124755477c1 | -3.50252 | -53.81671 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 428277ce-b7b7-350a-9ac5-26d18cfc3c1a | -3.57902 | -41.95877 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 233eb419-bf62-35f9-9f1d-937ff17a29ac | -1.79286 | -52.74646 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14f2a9de-ffe6-3e54-aded-814f48261a17 | -1.72339 | -52.48854 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b8f8adb-404c-380f-b415-a2c2010e0d62 | -4.10494 | -48.24735 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0e02e3d-6d3e-30ec-b7db-f85e6657f04c | -2.82416 | -46.83768 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e48d339e-3d9d-3114-97e9-4fabb8e90566 | -3.57442 | -41.96567 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5025c1ca-a381-3612-88a1-1009ae94653b | -3.09039 | -53.27928 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 554db645-3639-3622-a33e-06450b917810 | -2.99246 | -45.46722 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 212a34e7-5cbf-3f28-86c6-6075d7f853e6 | -3.08983 | -53.28273 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3f015d3-0a3f-30c7-a1a7-4ae547f0b39b | -5.31473 | -43.07565 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9a1ce17-fded-3a26-9628-2b9fd64b86f8 | -4.29874 | -48.19182 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2859d5ab-392c-35f8-bdcc-11350a5d5fc5 | -1.79119 | -52.74514 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74c54018-5dd4-3720-af3d-117f7eddec06 | -3.31107 | -53.75127 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24a06d91-108a-3450-ba47-3ad75fd36fc4 | -3.45971 | -50.83488 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 404e9d29-7d16-3f0b-b93c-faa437095ea7 | -3.19018 | -50.82816 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b11093ec-4480-3bf0-aa33-348078509e5b | -1.88167 | -45.59808 | 2024-11-27 04:18:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca4095d4-c432-37f3-9efa-87905498a7fb | -3.51117 | -50.46434 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 157dd418-4d97-3c43-b125-10d528f4f59e | -3.2966 | -50.54377 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7418257-3a88-3b11-ac18-85697b3ee63f | -3.96713 | -48.06998 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f33ae2af-7c95-3945-8d49-de7866a7625f | -4.54517 | -46.60815 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7dff6c2-d88f-3aa1-96e3-76bd4a9a1f39 | -1.70331 | -45.49124 | 2024-11-27 04:18:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73c6ba3a-d260-3643-b8aa-20bfd1b31273 | -3.39432 | -44.17235 | 2024-11-27 04:18:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63e1e872-68f7-3611-8ff6-84e042dd5a86 | -2.28553 | -47.91573 | 2024-11-27 04:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ba1b721-7174-35a0-8bce-dac01dc7fcd9 | -1.31141 | -51.73582 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b43317e-c3b2-373e-a939-54afbdae0844 | -3.24771 | -46.42003 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09859dcd-22e5-375b-b949-54fa51a0876b | -3.76515 | -46.67911 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e11fd42-0bca-325d-a4b5-54a2f39732eb | -3.21872 | -48.82437 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2064a140-d853-3a58-93b2-dcc408a9f988 | -3.67066 | -53.65525 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3e28492-2dfd-32f3-88ca-d38cd7681aec | -2.83397 | -54.12174 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 55ce9985-d8cf-39c2-b00e-cb056c9344cd | -3.31045 | -53.75503 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf5d81be-ded5-3b75-9816-3bf59be52ed4 | -3.11626 | -53.2636 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0302718a-025d-35c3-bb24-d61a1d4784f6 | -1.36531 | -52.12519 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af258f35-2aae-35d6-ac3d-f45d2d862cd4 | -3.49822 | -53.80787 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8f1042e-fcae-3661-9a51-1b11d6e806f4 | -3.86091 | -40.44283 | 2024-11-27 04:18:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| efd9bdde-11b5-31a2-b250-c4c517133cf4 | -2.61713 | -52.53466 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b54bb721-5908-3d02-acc4-7de2638847d4 | -4.57408 | -41.04358 | 2024-11-27 04:18:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 76cb28ed-d324-3fbb-a1b2-45206020924a | -3.96943 | -48.07971 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a47a5b7-0e00-3a3d-bb31-4e9bf3ceaf02 | -5.22262 | -44.91471 | 2024-11-27 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1db97502-6ffb-3203-b7ca-3c97d2760e74 | -1.76516 | -53.62443 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fb1c9af-8611-3a19-a4c6-94dd477b4de7 | -3.10533 | -53.26188 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a157e949-940b-33e0-b666-19d0de9f691a | -3.24771 | -50.61486 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d006bd29-2b8f-3879-970b-141a956e1e94 | -3.70801 | -50.43954 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15b7c0c0-5668-3959-a284-dc6101ead4b9 | -3.84184 | -49.89794 | 2024-11-27 04:18:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 124bfd07-5884-3fbd-8050-39a5cbfe6eb0 | -3.50185 | -53.82068 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b557976-81aa-3280-bc55-32d6a0766592 | -1.83062 | -47.21586 | 2024-11-27 04:18:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46c53003-a351-32bc-af72-0c7b4103cf08 | -2.54265 | -46.4069 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a81896de-c076-3393-8c43-840503620345 | -3.92443 | -45.84439 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25efa7b5-7267-399e-ac00-1da819083449 | -3.32731 | -53.72289 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6912af39-8aac-3952-a156-0558b686684a | -4.21757 | -48.66281 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 7c40eddb-488f-3641-8305-e255409ee715 | -5.38771 | -42.96186 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 80d95662-e691-3a6d-87f9-05b20ac3222e | -1.26745 | -52.16441 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f907ec3c-7d60-3864-8e3e-b9f49d1d44ac | -3.58554 | -50.37263 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80c12585-4aa5-3ab7-9bbd-896020383adc | -3.03523 | -48.50024 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5b1a37f-5058-3666-bd66-5020d50d72a7 | -2.83858 | -46.83997 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 6717af85-9ef1-3916-8688-f43f6d0be274 | -3.0959 | -50.36828 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a705b05-1f0e-3a84-8033-b08c8e4a0c14 | -3.23065 | -50.31628 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01f3411c-f740-386a-ad33-d3c84ac5a419 | -2.82087 | -46.81187 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b5a9e66-8e6a-3f01-8e37-c945df7c9d48 | -3.16892 | -48.44135 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 2977000b-1483-3c23-87c3-38525133e159 | -4.23625 | -50.01696 | 2024-11-27 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd0b6aff-0cfb-3fce-beb3-0bd1f1947a3f | -3.90013 | -50.60792 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README36.md)
