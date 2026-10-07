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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a31828e0-cdbe-364a-b84a-1fa5d8949d2f | -0.04819 | -53.25672 | 2026-10-07 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e62a05a1-99b7-351f-b1a3-84c0a0a81eb5 | -3.52401 | -58.75517 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b765110-22da-3719-a72f-472e90a64137 | -2.92235 | -54.10524 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f2c01f1-ee2f-31dc-bdfc-416370c417d6 | 4.14988 | -61.247 | 2026-10-07 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d88b378-233f-37b6-b502-37b1770fcc89 | -3.18264 | -50.57168 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c5c5c3f4-e505-35f7-8a86-45bd6f89f71c | 0.69889 | -51.43454 | 2026-10-07 05:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67153335-0a08-3efa-a899-ab64121c8da9 | -3.80235 | -56.99532 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48f50fbf-c31e-3d7a-a95a-56417fcfa73b | -2.9881 | -51.04758 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 586bd01c-73f0-3806-9cc2-7bffee229d77 | -3.49885 | -54.63647 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d42b52f9-5747-36e0-a561-5fbd4e098765 | -3.10986 | -53.77488 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5c4cf4cb-d05d-3a63-a97d-f1083a3ddfd6 | -3.34894 | -59.51073 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e25df3ed-1264-3f48-8412-030cd56b6de2 | -3.27291 | -50.42468 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84032e29-82a6-36a8-9bd6-f088b5d29702 | -3.12606 | -53.70278 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56029b0c-6463-3e50-963a-e82595bb895d | -3.85728 | -55.99478 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afd73f8b-5787-300d-9d2c-cc75e27263c5 | -3.08197 | -54.27782 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a36221f8-4450-389a-b806-a583124ecc08 | -3.27706 | -50.43294 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e01cddf-e855-3b9e-8b6a-b91be20ee7b8 | -3.67897 | -55.94881 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64dfcb87-e330-3cb6-a97a-44ce960000e4 | 2.44972 | -50.82344 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a229f80f-eb05-3c4a-81b6-e0ce0862ede6 | -3.29991 | -53.86764 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3527ff5c-3d3a-31d1-a22e-d01444c2f937 | -3.47948 | -50.08041 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f5d90fd9-c285-3814-85b4-7362711258eb | 1.76906 | -55.57009 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fdbf76f-900c-3d33-8955-1977a640cd5d | 0.68477 | -60.07855 | 2026-10-07 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95c85de7-80c1-3d27-ab3f-3e6af6568c23 | -2.93117 | -54.15295 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ffa14a8-db59-3193-a6f3-ba7de35314ae | -3.27419 | -50.41582 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88fbad33-d70d-38d1-9e25-68a4bf37712a | -3.00615 | -57.74459 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9240f2c6-e91b-38e2-bc58-02f642a764ba | 2.43644 | -50.84306 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 009b7463-89bf-367a-a5e6-d93658ae51c4 | -2.8548 | -59.21182 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aab0bb58-8e49-3995-93f8-135f207f203b | -3.80593 | -51.03532 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8167b20-34a3-3515-80c2-726759028b32 | -3.08096 | -54.2532 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4ca09ea-551d-336f-bff8-6a66c45da3a4 | 1.82236 | -55.53422 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3735dd39-c840-3e00-8ac5-e9a99842604b | -3.8117 | -51.03678 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8bc659f-e554-382c-955c-b7f729920a1b | -3.58782 | -55.56405 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3576ca91-db5e-3576-9176-3e0978f687bf | 1.71955 | -55.61394 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 5bb5cc5d-6db2-32d7-8241-2deba309e189 | -4.09988 | -52.06872 | 2026-10-07 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c61c0875-32e7-33e6-be68-93990345dda3 | -1.33854 | -55.45818 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81d0f297-941b-3733-ae92-5a368cc37606 | -3.93315 | -54.57648 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 659a0749-6963-353c-9798-41ac3beeb9fc | 3.14141 | -60.59217 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c976585-fed7-3c1b-a259-fc65a0c33590 | -3.09142 | -53.73496 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53b177be-3002-3ca0-b340-da611dad0267 | -3.04155 | -53.93196 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d28ddd7-2bcd-3c11-9bb5-ed631720d0e4 | -3.27484 | -50.41133 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4eb0d041-8a67-364d-8683-78bc95e1211c | -3.54096 | -59.4862 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 197d5730-e4a2-3582-bed5-fa6ffc9db438 | -3.09051 | -54.28406 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f026a1f9-f1cf-3c0c-ab54-b7a9c79e5002 | -2.78929 | -51.67651 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 03e7daff-8be4-3bd7-abbd-88fb9f3c21be | -3.86506 | -55.99989 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4fbe3f3-6c3b-3263-b1c6-db5f22b778d6 | -3.35875 | -50.46984 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98229f29-78c1-3666-901e-631d4c040e63 | -3.97702 | -56.05404 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e419f764-c92b-3f69-8836-495767a04aa9 | -3.5041 | -54.63267 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4764be02-9cda-3b3a-931b-47c468959cae | -3.58957 | -55.56692 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc3ef4d9-7f42-3e24-a57f-02dabe30bb39 | -3.29992 | -54.06464 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad557f67-044c-3e5a-928e-ad96390eaf68 | -0.42219 | -52.0676 | 2026-10-07 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9ee98a0-5bb2-3745-8c16-8991ff423982 | -3.29893 | -54.03885 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a6d9062b-b95f-3555-883f-dec819b16d99 | -3.72974 | -55.98388 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f38672e-c299-3da4-ac97-ea0ee1f298bd | 0.69836 | -51.43123 | 2026-10-07 05:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3aa7ad91-ffe0-3c24-9ada-1de0e3aacfd3 | -3.77584 | -58.5211 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2e6976d-6aa5-3492-b367-eecb6c7f399b | -3.09624 | -53.73569 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25301f70-21a4-3254-85b6-f68993d8712d | -3.50816 | -54.63538 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87d16872-4f86-3ae8-85a3-fc000a9f8dbd | -3.62276 | -55.28327 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1a61713b-380b-31b1-badd-fb70909fbf6c | -2.57426 | -57.79107 | 2026-10-07 05:40:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5352a421-ab97-3f93-9d50-ba810726e5f0 | -3.12551 | -53.76423 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc7ca80b-e18f-3157-9895-0b9f415dced7 | -3.29805 | -59.49901 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aad4f56a-fd0a-3c5e-9c34-5d01788c4856 | 0.66404 | -59.56547 | 2026-10-07 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d868af3-c6ec-37ef-b973-2193572ae262 | -2.99859 | -54.11844 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 919e04b5-ffa8-3ec5-9679-fe930e491320 | -3.27447 | -54.03349 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 1b21c289-02de-3139-bd26-9202219a8766 | -3.53345 | -54.65338 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 020b9b54-519c-39d0-991b-05f0db91c632 | -3.06169 | -54.25475 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edee8f75-8102-3ba8-9e40-9a3e3dbf3d2f | -3.27628 | -54.06107 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a119698-b06e-3e49-9845-b3e375c46717 | -2.71715 | -57.47104 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b6c7427-e08d-356e-b5a0-c27dfccc65cc | 2.7554 | -60.01743 | 2026-10-07 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccbb998f-3720-388b-91e2-f49fe7164d22 | -3.28428 | -54.0723 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8b8f4b04-a3e0-32b7-8687-0c46eb1177d0 | -3.10265 | -53.75793 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b6a01a7-5275-3df0-b48e-43dd90326901 | -4.04211 | -50.9817 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f093f8d-bf09-3d32-afb3-250d61205dda | -2.10294 | -52.05754 | 2026-10-07 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fcc9cf4-4dc1-3300-9a4c-d548b6e6e94b | -2.46994 | -58.07629 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2740217-4315-341f-ad0a-64e6d879b4d0 | -3.73668 | -59.44382 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dba1801c-6954-382b-b18b-c0261ec51c1a | -3.0503 | -54.26733 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 670b323b-bb6f-3c27-96e9-491c0b05b82d | -4.46202 | -54.96972 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63cf8447-2ae3-3bdd-88f9-62afa2abfe26 | -3.07951 | -54.26272 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4404014f-da7d-3ea9-a91e-31a11363a6d5 | -3.73791 | -59.45117 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c983dc6-f8f1-3492-b1a1-14b60b2f9d11 | -3.49588 | -50.09788 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b433ab9e-e900-3cab-a624-7cec975c33b1 | -2.98007 | -54.05016 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cb72984-5aef-3dfa-91d2-15a58c577d91 | -3.39157 | -59.59669 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8b68540-5a7e-34ec-bdc0-bbafa4a2223e | -3.17261 | -58.63184 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fc0c236-22d9-3bfc-910e-26bdad1cb077 | -2.52583 | -58.09764 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89f3e6a9-9706-307c-a18a-2d2461acc4a5 | -3.50963 | -54.6571 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bece3b2c-cf5c-3680-92b1-9c32b6f039d3 | -3.1306 | -57.82212 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 150eed29-a536-3d96-8d60-d4f1ed1da802 | -2.88217 | -54.14871 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef13117a-269e-34fc-a98b-8822ccf530f7 | -3.67586 | -57.06878 | 2026-10-07 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87b8e8f6-9790-32af-802c-34f66f80af96 | -3.70555 | -59.64047 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15e5a479-c85e-3b16-b5d3-aa90b434fd38 | -2.49889 | -56.13326 | 2026-10-07 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27b78589-b944-3844-93f6-61990b21798c | -4.76961 | -50.8143 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 665210f3-28cb-3b68-bcbd-ea5021938247 | -3.27011 | -50.40128 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e8df494-3ffa-3ba2-8df6-c6f3a01238d0 | -3.27302 | -50.41886 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f0c39c3-ac82-3fab-a70a-8eba3bc25ed5 | -2.99614 | -54.103 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20a35e23-962a-3b4c-af45-b0b4986c446e | 2.70621 | -60.57835 | 2026-10-07 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4c73fe3-0918-3cfb-8189-1ba5f3799b77 | -3.44404 | -56.93716 | 2026-10-07 05:40:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d63ac266-4ca7-310a-99eb-66737654df70 | -3.04856 | -53.88616 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c968d0f-e5b4-3786-9807-07412cd9676f | -2.78407 | -51.67136 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f725a444-ee19-31aa-a2d0-fe1719c6f84d | -3.24515 | -56.80251 | 2026-10-07 05:40:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16cc93ca-635e-35cf-b6c8-faacb859d825 | -3.51417 | -54.65786 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 185eaa57-9f21-33d6-8d5e-176d30c4d459 | -4.27135 | -54.87044 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README97.md)
