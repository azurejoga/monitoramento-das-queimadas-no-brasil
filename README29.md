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
| d59ea428-06bd-323a-9239-534ae81c3c23 | 2.7627 | -60.6378 | 2024-12-11 05:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 82568d9b-fbff-3b22-b25f-da960f60ba65 | -6.118 | -42.5323 | 2024-12-11 05:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| e45e5e02-1bfc-364e-a2d1-3b85b3fab7c8 | -6.1178 | -42.5559 | 2024-12-11 05:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 59d043c7-7ee5-396e-9a7a-606174098c1a | -6.9161 | -43.4952 | 2024-12-11 05:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| f6fc0b88-cd0b-3dbf-9105-03634449fa16 | -12.5423 | -58.3759 | 2024-12-11 05:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 28a360fd-b57e-3941-9df0-c05eebae5ea9 | -6.1368 | -42.5307 | 2024-12-11 05:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 129.7 |
| c89c7310-6aee-3bb2-b66a-f2043a0eb74a | -6.8972 | -43.4969 | 2024-12-11 05:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7186bc3a-44d8-35b5-af42-bb2a0f805eba | -6.9592 | -42.9994 | 2024-12-11 05:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.3 |
| d9619c05-ebb3-3e3c-9172-47b1d28e414b | -12.5617 | -58.3347 | 2024-12-11 05:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 34161e91-d0b9-3d15-a6d0-eac5650010a7 | -12.5425 | -58.3561 | 2024-12-11 05:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 142.6 |
| fb9002a4-fd55-3cba-9167-34117f8d5378 | -12.5613 | -58.3744 | 2024-12-11 05:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 7cee53f7-19a3-3041-ac4a-93c5f42e4c30 | -6.1366 | -42.5544 | 2024-12-11 05:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| ec28b878-2e53-3416-bddf-273b2b109436 | -6.978 | -42.9977 | 2024-12-11 05:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.5 |
| 8fcd154b-c437-3b20-b6fc-86bf3ddf02ae | -6.8972 | -43.4969 | 2024-12-11 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 1e132912-6156-3fe4-89c4-ccfd5c2e54b9 | -6.978 | -42.9977 | 2024-12-11 05:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.7 |
| fb267317-2409-35ca-bc28-32a1218a72bf | -6.897 | -43.5202 | 2024-12-11 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| e8329dd5-adae-3732-b7a2-34c0131b237b | -6.9592 | -42.9994 | 2024-12-11 05:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 017e16de-e082-3700-83a5-edd3d2431731 | -6.9158 | -43.5185 | 2024-12-11 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 17ba8718-bdf7-3a63-9e0b-d6f127e9cbd8 | -6.1368 | -42.5307 | 2024-12-11 05:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 136.7 |
| 7f81a85b-7182-3429-b889-0267f66b0cd5 | -6.9161 | -43.4952 | 2024-12-11 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| dae7af02-c327-3b7a-a7b9-baef32cb7058 | -6.1366 | -42.5544 | 2024-12-11 05:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 86a8069f-e0f5-3c10-97bd-9ab9cc77c574 | -6.118 | -42.5323 | 2024-12-11 05:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 4d7377a2-6663-3eb4-9057-61fc7fc22283 | -6.1178 | -42.5559 | 2024-12-11 05:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| d0bd0b50-a132-312f-8eef-fc48d79c2f78 | -6.1178 | -42.5559 | 2024-12-11 06:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 2d26239e-1fb0-3322-a470-474454c71210 | -6.1368 | -42.5307 | 2024-12-11 06:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 98220c22-c448-3697-909f-652e17880d60 | -6.9158 | -43.5185 | 2024-12-11 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| effd6032-c9c3-347c-a360-844a62d88b38 | -6.118 | -42.5323 | 2024-12-11 06:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 3dd0cdf0-7159-3d36-966f-9e9cd79c9590 | -6.9161 | -43.4952 | 2024-12-11 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 6c76cfb5-0c91-3f5c-960a-239cdd809f56 | -6.1366 | -42.5544 | 2024-12-11 06:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 43dde9b0-fff3-37db-a57d-24f70569657a | -6.897 | -43.5202 | 2024-12-11 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 44a60e47-2da4-3597-b42f-1613de747319 | -6.8972 | -43.4969 | 2024-12-11 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f54075e6-5b98-3ab7-8412-9712b11492c3 | -6.9592 | -42.9994 | 2024-12-11 06:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 146.8 |
| 106add28-0426-3e12-9d98-562414d235e1 | -6.978 | -42.9977 | 2024-12-11 06:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 124.7 |
| 5fa768e7-6058-3aba-9803-e455502da48d | -6.8972 | -43.4969 | 2024-12-11 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f807372f-3118-3ebc-93cf-0ab62f228a8b | -6.1178 | -42.5559 | 2024-12-11 06:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 2b754dea-ea07-3a99-9276-a7fae6857a37 | -6.978 | -42.9977 | 2024-12-11 06:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.6 |
| b933446f-86b9-3cb8-b907-61f57ec7bf7c | -6.1368 | -42.5307 | 2024-12-11 06:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 0a5d3ff6-2756-3ff7-9400-2c401b2205d5 | -6.9161 | -43.4952 | 2024-12-11 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 230.7 |
| 11341aa6-ee07-35ae-a4a1-d997fe1e4ea5 | -6.118 | -42.5323 | 2024-12-11 06:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| 068c690f-34ff-3c7b-8745-0f463ef9286a | -6.9158 | -43.5185 | 2024-12-11 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 8e0c1112-93fe-3485-ba0d-6188068e4999 | -6.897 | -43.5202 | 2024-12-11 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 46155b32-f74e-362f-a13e-0b3f378323dc | -6.9592 | -42.9994 | 2024-12-11 06:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| f6bb4b04-c31e-34e6-b7ff-84c5011a10c2 | 2.75686 | -60.64231 | 2024-12-11 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1c967753-0ed5-3ff7-a01a-0f03a45f0aee | 3.22479 | -61.19409 | 2024-12-11 06:12:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f5ff022-8005-3a04-80dc-ca723a73239b | 2.74574 | -60.64869 | 2024-12-11 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c9df8a0-ee6f-3adf-8b50-1a5a9c1fa7df | 3.23176 | -61.20084 | 2024-12-11 06:12:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2161bd56-a6aa-3504-bc4b-5014528e18ba | 3.23046 | -61.19312 | 2024-12-11 06:12:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 867d4fca-2a05-31f8-af75-46ff4f99df73 | 3.22545 | -61.19798 | 2024-12-11 06:12:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75b73725-f6bd-3a55-87d1-39d396efa585 | 3.23112 | -61.19703 | 2024-12-11 06:12:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 779b0c89-3637-3b85-a888-06220dacc3cd | 2.75757 | -60.64662 | 2024-12-11 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 730b0c5b-fe7d-3e51-a674-d6e7822a1c0a | 2.73436 | -60.39248 | 2024-12-11 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 04078766-fbd0-3bc5-886f-8780a4d51dd7 | 2.74952 | -60.63469 | 2024-12-11 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6df54f4c-bd24-3d24-a386-29d2d1ffdd33 | 2.75544 | -60.63365 | 2024-12-11 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2e59873d-7aa2-310a-9747-6fb2ce0efe02 | 2.75615 | -60.63798 | 2024-12-11 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6226bca0-74f7-3e88-a8a9-0a4d307a854e | 2.75024 | -60.63903 | 2024-12-11 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 535aa147-85f7-3f56-8438-14cb7d2f8d7d | 2.73678 | -60.39526 | 2024-12-11 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bb01ae30-17a3-3c95-971e-d467d370272b | 2.73509 | -60.39697 | 2024-12-11 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 383a792a-fcd9-3d37-a27b-1e92ff1fbd04 | -10.08014 | -64.38334 | 2024-12-11 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf14065d-1904-3752-bf7c-456dd2b16db2 | -6.897 | -43.5202 | 2024-12-11 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 4379c493-e60c-3d9d-bc24-833bf3351bad | -6.1178 | -42.5559 | 2024-12-11 06:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 7ad7f702-0e05-344d-9d80-5c17501b912a | -6.1368 | -42.5307 | 2024-12-11 06:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 125.0 |
| fec1c6ba-028e-316d-997b-f22d277d2636 | -6.1366 | -42.5544 | 2024-12-11 06:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 41811200-df12-3004-b3f2-ba3a570078ef | -6.118 | -42.5323 | 2024-12-11 06:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 92517ad9-ad62-34f1-96ff-34a81d212e68 | -6.8972 | -43.4969 | 2024-12-11 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 5cc2d29b-ac14-390f-a340-3a4d57572dbe | -6.9161 | -43.4952 | 2024-12-11 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 244.5 |
| 997f151f-fb0f-3912-8c27-99f741da4e20 | -6.5631 | -51.1126 | 2024-12-11 06:20:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d7c7f5db-7377-32dd-ac5b-f4811eb3faab | -6.9592 | -42.9994 | 2024-12-11 06:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.4 |
| cbb1a110-3ed2-325d-a8a8-dd7633d6215d | -6.9158 | -43.5185 | 2024-12-11 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 204.8 |
| d968f8fd-461a-3125-a762-84507e2650d9 | -6.9349 | -43.4934 | 2024-12-11 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 6ee2ed58-8b11-3e02-b724-09927bf7733e | -6.978 | -42.9977 | 2024-12-11 06:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.6 |
| b861d91c-dae1-3b03-ab80-27efd80ea16f | -6.1368 | -42.5307 | 2024-12-11 06:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| a747c8af-19af-3e1e-aef8-0e29f1d60a8d | -6.118 | -42.5323 | 2024-12-11 06:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 349a0536-9d62-38e3-b19f-9be39b2e47db | -6.897 | -43.5202 | 2024-12-11 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 82d3ca3e-a437-30ef-be43-ef0794a13592 | -6.9592 | -42.9994 | 2024-12-11 06:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.0 |
| 3c128d89-20c3-3585-84eb-34a8bf5ab44a | -6.978 | -42.9977 | 2024-12-11 06:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 637908d0-6404-3f8b-a717-173474800d34 | -6.9158 | -43.5185 | 2024-12-11 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 224.8 |
| 0a049199-e889-3e30-8820-4c28114308b4 | -6.8972 | -43.4969 | 2024-12-11 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| d3e94155-97c0-3d41-9a67-b0c92baccfa7 | -6.9161 | -43.4952 | 2024-12-11 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 293.0 |
| 48ffc2fe-c32e-3b34-b227-5dcb336fac11 | -6.1178 | -42.5559 | 2024-12-11 06:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| bc8ce2c0-98d4-3537-b69d-5414ad12302d | -6.1178 | -42.5559 | 2024-12-11 06:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 4013f54b-e1bc-3948-8465-0a5f742d63ea | -6.9158 | -43.5185 | 2024-12-11 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 179.9 |
| bec85e29-1343-3e0c-b292-1d40f493c2e8 | -6.1366 | -42.5544 | 2024-12-11 06:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 04486412-2f4e-34c3-9a9e-6f26b207b9ed | -6.9161 | -43.4952 | 2024-12-11 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 203.9 |
| 6300f25a-3139-31fd-af9f-89db949a3387 | -6.9349 | -43.4934 | 2024-12-11 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| ffa571b8-aeaf-3d36-bc05-282d67da7b40 | -6.897 | -43.5202 | 2024-12-11 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 25636e74-1d60-398f-a7c5-736b60f23593 | -6.1368 | -42.5307 | 2024-12-11 06:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 131.5 |
| 798ab7c3-395e-3335-b2fc-7c1dfd3e0c32 | -6.118 | -42.5323 | 2024-12-11 06:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 015b411a-e4d9-3170-86d5-3cb295906534 | -6.9346 | -43.5168 | 2024-12-11 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 7ac9d1d9-d103-3bc1-a197-4b21f5d9545e | -6.9592 | -42.9994 | 2024-12-11 06:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.4 |
| 001e8111-1d1e-370a-8926-fb9108d392f1 | -6.8972 | -43.4969 | 2024-12-11 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e6a252ea-4848-300a-be35-5572f255d073 | -6.978 | -42.9977 | 2024-12-11 06:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.7 |
| 06abcfee-6816-34e3-88d0-3320375293ff | -6.1178 | -42.5559 | 2024-12-11 06:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 619b1e97-a2df-38b8-bbc6-200e14365dc5 | -6.9161 | -43.4952 | 2024-12-11 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 257.0 |
| 09e82426-96b4-3bbe-a377-e4e4da3e4546 | -6.978 | -42.9977 | 2024-12-11 06:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.3 |
| 34db11cd-ffd7-3fe4-9caa-c787cf12c4d5 | -6.8972 | -43.4969 | 2024-12-11 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 00be3a94-18d8-3d3d-b0de-e0b21265018f | -6.118 | -42.5323 | 2024-12-11 06:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| 20543d14-3611-31f2-ac30-136fcce69239 | -6.9592 | -42.9994 | 2024-12-11 06:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 23d55d96-4971-3552-84d8-91ae8a56bb26 | -6.9158 | -43.5185 | 2024-12-11 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 184.3 |
| e8dbcdf2-7754-3143-83a4-86a75df4a8f7 | -6.1368 | -42.5307 | 2024-12-11 06:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| def6a299-ab73-30fe-8626-1e12ec776387 | -6.1368 | -42.5307 | 2024-12-11 07:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |


[Clique aqui para ver as próximas entradas](README30.md)
