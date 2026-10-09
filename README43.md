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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f0c97c3-cd2e-3dcb-9971-055215e7d4cd | -2.73903 | -54.13033 | 2026-10-09 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 13628519-7803-3834-88fe-ebb906b47d07 | -3.32679 | -61.26196 | 2026-10-09 00:37:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| eb3cca46-d1d7-3969-8ec9-e2fb11ba95fd | -3.74845 | -59.42139 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ce64d923-6691-3cf7-b64a-d823223c2ff4 | -4.30588 | -60.87521 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f532f4b0-3663-3f95-89a8-a5bc0e1f22b5 | -4.54824 | -54.97558 | 2026-10-09 00:37:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 049e5f7a-9782-33a3-8a33-08fc7011b57c | -3.11459 | -53.80474 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| c677384e-bf25-3820-8f61-af3aa5632ce2 | -4.5812 | -55.72212 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b2aca2da-0798-3647-819a-1db25f2f3d47 | -3.46653 | -59.57729 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8e81086e-31e9-3a34-8e2c-08a2f785c4b5 | -3.82804 | -59.39504 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4ccd1f0a-5be3-354a-a32a-245697396aa4 | -1.40506 | -57.93692 | 2026-10-09 00:37:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 98685883-d6f5-3755-bf47-767368fe94e5 | -3.96596 | -60.00595 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| f081d3ff-7645-311a-adda-ca1a415acaba | -3.32809 | -61.27163 | 2026-10-09 00:37:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 397fb39d-062a-36ee-80c4-5d258de9e599 | -3.47535 | -59.57606 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8d1b85ea-c513-3558-ade8-890c880608f9 | -2.50403 | -56.07127 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 58c8e233-8611-3b24-91a5-5a56e53dfb72 | -3.4326 | -59.54357 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e221e6da-0f3c-3b4e-aad9-164b728d073c | -3.10748 | -53.96766 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 50a86b09-759a-3b60-92a2-8167faf42acc | -2.93343 | -57.92445 | 2026-10-09 00:37:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 90018335-5b27-34a8-8a31-77e217e2a3ad | -3.07627 | -58.09155 | 2026-10-09 00:37:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9710b8f3-c48a-3d3e-88f8-5768b783dd8b | -3.52746 | -54.65988 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 904ff7ea-d999-3964-935a-4f1a11b50561 | -1.77395 | -55.01983 | 2026-10-09 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7300be2d-5b3c-3b28-8142-e6525ebeb29f | -3.48736 | -57.80367 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 023b8dfd-2176-3552-a6ee-80a1d4016570 | -3.89602 | -58.95859 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ea0c9906-1d7e-3e4c-bfff-9e5e1845cdbe | -2.39439 | -57.89676 | 2026-10-09 00:37:00 | TERRA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9bdb2691-9ca7-348c-9022-a68fd1e42108 | 1.21688 | -59.97473 | 2026-10-09 00:37:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1506b292-e967-3088-9fd8-237f13aed5d8 | -2.13069 | -56.70339 | 2026-10-09 00:37:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a0fd325a-f2bb-3a22-a745-e896988c6f6d | -3.21114 | -57.86721 | 2026-10-09 00:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 5d002dab-a1cb-318f-bf82-0d517abecc3a | -3.20409 | -50.81687 | 2026-10-09 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 8fbd47d4-c625-3251-979d-4353e275b3de | -3.98838 | -59.3515 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 7dd5ea58-7252-3062-a035-722468c329bf | -3.72787 | -55.97815 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 15a62448-4955-3add-9113-9873a7d14e23 | -2.9828 | -54.0769 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 02cf2509-0209-39a7-88af-e7a330a09ffc | -3.74852 | -59.61848 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 80fa38f9-51ee-346d-be88-758e8b0fbc5f | -2.52145 | -56.27241 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8dfa45ec-d92c-3d08-9b87-cf2ebafdce9c | -3.36162 | -59.41928 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f02fe738-0787-3ce1-84de-66b46bff6bec | -3.79195 | -59.32849 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b34d0469-6b7d-3803-b411-545b2ee9e690 | -3.52715 | -59.34816 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 1826c774-57aa-3cd4-a3a4-746f614148b6 | -1.55092 | -54.56899 | 2026-10-09 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| ad441336-e9fb-3f2c-ac27-d1250e8740e0 | -2.06576 | -56.87894 | 2026-10-09 00:37:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2d7af157-035e-3c64-881d-777b03b25f04 | -3.29727 | -53.71337 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 979ce29f-1f85-3c2c-9d86-3b3a6198ca86 | -3.09069 | -59.19781 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0c51cdf1-1620-3f1a-bf25-d0882452d2d9 | -6.04519 | -59.91709 | 2026-10-09 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7428cb7a-54eb-36ea-8a6f-03992c6edf10 | -3.85219 | -58.90186 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ce132ef2-5161-3330-a948-7e0e7c737729 | -4.55194 | -54.96919 | 2026-10-09 00:37:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| da7a0c85-a1f4-3ab2-9e1e-4f8189179389 | 4.2566 | -60.91871 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cc562f02-4ad9-3974-974c-252496b24f82 | 4.36927 | -59.82927 | 2026-10-09 00:39:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe8e481f-5cba-31b4-8f85-d857e7c473a1 | 4.451 | -60.97605 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 62d3e48d-66e9-3e5e-b4f2-17bd6f25d022 | 4.23104 | -60.84361 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0daef575-3e14-33ab-afb6-6e84d285fc54 | 4.20115 | -60.71722 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 690a329e-acb1-3b16-bde4-c58ee52931cd | 4.88455 | -60.30607 | 2026-10-09 00:39:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d02d94c1-ba1f-396d-bb71-7f85c52f313b | 4.43703 | -60.94729 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 542f0ee1-a17b-3a9a-b2e9-cdfc4bda8ce0 | 4.44221 | -60.97482 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 1f9de28c-33d1-37fc-9739-807c5e557f19 | 4.44341 | -60.96605 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 17b82e4a-d863-34a1-9c6b-a3de8932fb2f | 4.44462 | -60.95729 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 41.8 |
| b623fe98-ef53-3dcd-841e-89b4a6b759a6 | 3.52223 | -51.26318 | 2026-10-09 00:39:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 312b382b-a723-3cb6-8e3e-3e4df2bd3e95 | 4.43824 | -60.93853 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 51bf4243-1794-3e40-9b54-de4c83ba5fb6 | 2.88515 | -60.29867 | 2026-10-09 00:39:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dc73f2cd-2824-3c07-a24f-24f54abdcc14 | 3.92001 | -61.09489 | 2026-10-09 00:39:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 538db703-2cf8-33e3-9a12-2b5de18f9f13 | 4.2554 | -60.92747 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aff1d911-a403-3510-ac4d-b61fe48ac561 | 4.37051 | -59.82012 | 2026-10-09 00:39:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f612eab4-ac66-360d-a93e-6892f3274cde | 4.43583 | -60.95605 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 52f3c68e-cd31-3860-8180-9023fd679cd8 | 4.01486 | -60.33773 | 2026-10-09 00:39:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9f0a25d9-bbca-3a0a-b87b-4ef25ece1857 | 4.25021 | -60.89993 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 52e8d9e2-be00-334c-a717-d0040f5f4e73 | 4.88335 | -60.31486 | 2026-10-09 00:39:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 3a0f1342-4685-31de-85a0-1f9eb1448487 | 4.26724 | -60.36701 | 2026-10-09 00:39:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c3a3170-aa58-3af8-b723-b905350a1eba | 4.24901 | -60.90871 | 2026-10-09 00:39:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 72211ad8-4fda-32e1-bf8e-068f77c81d3b | -2.7428 | -54.1146 | 2026-10-09 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| c8f2d8a7-d0c1-3e45-9cca-e0caff5ff71d | -4.6282 | -49.2147 | 2026-10-09 00:40:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 647d71df-6538-3c3e-a924-4df2ca2666c2 | -3.7346 | -59.4577 | 2026-10-09 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 6fa6adfa-573d-3387-9edd-61326eb5cf0e | -3.5676 | -54.6946 | 2026-10-09 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 9d015056-6fe3-3687-b717-c60c1f868258 | -5.6932 | -53.487 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0bd83212-665c-3057-b612-27ba3292fdab | -7.2366 | -55.1606 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| bb85a1c0-f5e7-3fd8-9b34-6366d65dc7cc | -3.2577 | -54.0217 | 2026-10-09 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| af683d83-471e-3922-aff5-c203742a3111 | -11.1465 | -54.8006 | 2026-10-09 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a1a9a929-80d7-393a-b5ba-d9e70f96725b | -3.3455 | -50.4078 | 2026-10-09 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 6a4e5ae5-6925-3d10-8040-60eea9afef55 | -8.7423 | -45.1334 | 2026-10-09 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 286831cb-141e-3eab-95cd-0971806b736b | -3.1284 | -54.1857 | 2026-10-09 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 5a62e682-e2fd-38b3-9fa2-438aeff21444 | -7.1995 | -55.1627 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 5706d4f8-242c-3bd9-8bc3-7f23dd611bfa | -13.4922 | -44.3713 | 2026-10-09 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bffcd87f-2ba1-3ca6-9dc5-68db485304cb | -6.7551 | -55.1265 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0263e5c0-905a-3d54-bd1f-114c94beb071 | -12.2348 | -57.0871 | 2026-10-09 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 395f87a2-bfa2-3729-8bd1-4576367a5182 | -3.2945 | -54.0006 | 2026-10-09 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| cde78f46-9666-3621-b88d-b3b4285f10bb | -12.2154 | -57.1287 | 2026-10-09 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 4f2f5f50-c902-31f4-a767-fffe48f2c115 | -12.0058 | -43.464 | 2026-10-09 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 248.7 |
| c1ee2c48-48b1-3127-9a46-680c10b3df4e | -8.7234 | -45.1355 | 2026-10-09 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4785ec62-cf7e-3f98-ad5f-59e6829b3fc6 | -11.8499 | -43.5835 | 2026-10-09 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9c96cc35-4c8e-301c-a47e-9c72e181bba5 | -3.0002 | -54.0684 | 2026-10-09 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 34f668f4-eabd-322a-9af4-5223b0aabebc | -13.1639 | -54.3385 | 2026-10-09 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| cf107687-8279-39b6-8907-0677c2189264 | -7.2179 | -55.1817 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 98a5b20f-d57f-3b9e-8d64-468cf9a5e243 | -3.1787 | -50.5807 | 2026-10-09 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 087ceb46-3d8c-3188-8dfa-01fa69b179e6 | -3.1879 | -58.6433 | 2026-10-09 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| febe9deb-e599-3473-9afc-4effa2577675 | -6.7366 | -55.1274 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 8d61619c-928a-363e-9722-152c2fe8498d | -12.2346 | -57.1071 | 2026-10-09 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 0322685a-8676-3593-97e4-3e138a011b0d | -6.7365 | -55.1474 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 9ad4cad4-a87f-370c-8f88-980a23bab7cc | -7.4443 | -63.5401 | 2026-10-09 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| bc34657e-c219-3a04-88bf-23525a6be3f2 | -3.5493 | -54.6951 | 2026-10-09 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 61e0ee46-2fc7-3732-adf2-cdf35ef8412f | -6.7368 | -55.1074 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9223f700-e1aa-3352-a2a8-9539e0681e90 | -6.0021 | -40.9594 | 2026-10-09 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 523.3 |
| e51bea29-600f-33e3-ad49-a216dbd0ec21 | -8.911 | -45.229 | 2026-10-09 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 269.4 |
| 65a8f101-ae8e-38ad-8af4-226d2e08b2d0 | -7.2367 | -55.1406 | 2026-10-09 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a6e72b24-d99c-3690-9542-2489f1834a75 | -3.0924 | -53.9656 | 2026-10-09 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 359ca1b9-68bf-3889-9827-f1606a5ac755 | -12.0063 | -43.4402 | 2026-10-09 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |


[Clique aqui para ver as próximas entradas](README44.md)
