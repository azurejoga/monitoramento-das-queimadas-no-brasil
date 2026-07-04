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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0285d96a-a5e4-3646-a562-185cca304567 | -10.9209 | -43.0384 | 2026-07-04 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 241.7 |
| dee8a97c-710b-3238-a459-02328101f740 | -10.9401 | -43.0355 | 2026-07-04 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 13544bc9-d768-34b0-b826-72290a365d22 | -10.9205 | -43.0622 | 2026-07-04 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 234.9 |
| 72a8b728-9cdd-3ca9-9f82-9061de0e3fd1 | -10.9397 | -43.0593 | 2026-07-04 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 24084b5f-0151-3ec3-964a-187cc50d8f68 | -13.2398 | -54.3716 | 2026-07-04 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 4daca4cf-0941-324f-98fc-fef915f60b58 | -10.9209 | -43.0384 | 2026-07-04 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.6 |
| 4118a1ce-4b63-3d4c-af8d-19e11d259934 | -12.7553 | -44.5194 | 2026-07-04 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| dd86a956-0acd-3805-a626-7082a550bb60 | -12.7359 | -44.5225 | 2026-07-04 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 2d5021c0-28b9-3082-bc68-61bbb4d2bae0 | -10.9397 | -43.0593 | 2026-07-04 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 919b8db1-5bbb-363a-9a6e-6090ecf34854 | -10.9205 | -43.0622 | 2026-07-04 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| fb47b46e-ec62-3a13-b1ea-d25f8f07db58 | -10.9401 | -43.0355 | 2026-07-04 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.4 |
| ec67c6bc-cd65-39a6-9823-62fb0d42acb6 | -13.2398 | -54.3716 | 2026-07-04 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 10027bf0-b2d2-3cd1-951b-b143522335b4 | -9.37469 | -65.77773 | 2026-07-04 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 48a5eef3-2809-31d9-abec-b324b83118df | -13.2398 | -54.3716 | 2026-07-04 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 919f4dd8-cdee-34d5-a06a-4abeadb1f66f | -10.9209 | -43.0384 | 2026-07-04 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 237.2 |
| 7d4bd275-d6ae-3dbb-b590-12ef64c9357e | -10.9401 | -43.0355 | 2026-07-04 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| c1c07a9e-e6cc-3730-adcb-aeecbd0be01e | -12.7359 | -44.5225 | 2026-07-04 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| dfe0128f-35fa-3055-be0b-94f6f071d3da | -12.7553 | -44.5194 | 2026-07-04 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 8fc4d753-c100-3cf6-9ebe-416e3a9cc538 | -12.7548 | -44.5428 | 2026-07-04 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 78245225-72e8-328d-ae92-a34eac34b803 | -10.9397 | -43.0593 | 2026-07-04 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 600009a0-9375-3524-b94e-6bdd7b5b07ba | -10.9205 | -43.0622 | 2026-07-04 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.2 |
| 7c9f769b-c3c6-318f-aa8c-dbf6a3ca100e | -12.7355 | -44.546 | 2026-07-04 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 8dddec73-b572-3b99-a9bd-407e2d7d382e | -13.2595 | -54.3283 | 2026-07-04 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 5c61271d-ae6a-3021-9968-1a39627c2fa8 | -10.9209 | -43.0384 | 2026-07-04 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 247.1 |
| 61cb5d30-7b25-308a-bea6-7cac2e780822 | -12.7355 | -44.546 | 2026-07-04 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8be7903c-2e5a-3069-bf18-45415186023c | -10.9205 | -43.0622 | 2026-07-04 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 231.5 |
| a120581a-3e72-3d0f-8bb0-4cef251b43ff | -13.2398 | -54.3716 | 2026-07-04 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 773887b2-9bd3-33b4-8198-8bbcee7860ca | -12.7553 | -44.5194 | 2026-07-04 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 05123614-7b4b-30f9-b241-7b0cabafd7cc | -13.2592 | -54.3489 | 2026-07-04 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 7c15a120-878c-3e6b-9cad-8c74526713fa | -12.7548 | -44.5428 | 2026-07-04 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 225.5 |
| 01737d33-4874-3224-9446-50a7b5f7867e | -10.9397 | -43.0593 | 2026-07-04 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| acc00fca-3083-3cde-8902-ab627811e902 | -13.2401 | -54.351 | 2026-07-04 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4467f5a9-48e2-39bf-8f4c-ce046af7f5df | -10.9401 | -43.0355 | 2026-07-04 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 45a90dc2-34a8-3448-ae8f-171787de9829 | -12.7741 | -44.5396 | 2026-07-04 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3e9f23f7-54dd-3e78-93e9-962ecd270858 | -12.7359 | -44.5225 | 2026-07-04 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 0186cec2-975b-360d-b718-44a7452b081d | -12.7544 | -44.5662 | 2026-07-04 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| e4877ecf-bbcf-34e1-8db7-c735c91aee95 | -10.9397 | -43.0593 | 2026-07-04 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.8 |
| a40e2ae7-9954-3fea-a5a9-ca1ea55a5dee | -10.9205 | -43.0622 | 2026-07-04 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 80946f5a-ef6f-3d77-8789-ea90beb6a1bd | -10.9209 | -43.0384 | 2026-07-04 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 291.7 |
| 53e91854-0506-3131-a084-ad4f6ad5ba82 | -13.2404 | -54.3303 | 2026-07-04 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0c3d0291-fa60-374c-ae56-da9590fe08a3 | -12.7548 | -44.5428 | 2026-07-04 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d5a47b25-05b4-3488-bf65-7a292919032a | -13.2595 | -54.3283 | 2026-07-04 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| b7e345d5-2741-33fa-879a-a3e7041f34eb | -13.2398 | -54.3716 | 2026-07-04 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| bcb06d9d-e3bd-3b63-89b8-5ff9266fa948 | -12.7553 | -44.5194 | 2026-07-04 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 92074d80-df4e-3dd4-ac33-3e3ac2a1e1ea | -12.7359 | -44.5225 | 2026-07-04 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 96425f55-54f6-37cd-a1ea-e360da553944 | -13.2401 | -54.351 | 2026-07-04 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 015122be-01e3-31e3-8a1a-7a22c425318b | -10.9401 | -43.0355 | 2026-07-04 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 260.5 |
| d3091836-24fe-36bc-beb6-29fc56d202e9 | -13.2592 | -54.3489 | 2026-07-04 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 216.9 |
| bd26560a-7ebf-32a4-b585-faf463290300 | -12.7553 | -44.5194 | 2026-07-04 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| b34c92a3-faa2-3170-a61c-7a12393d8f47 | -12.7548 | -44.5428 | 2026-07-04 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 6b1ad00a-060b-392c-811e-70c84334f966 | -10.9401 | -43.0355 | 2026-07-04 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 239.9 |
| 4ab4e271-8421-3fb8-af10-b2641d2e97fd | -13.2398 | -54.3716 | 2026-07-04 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a42ec4b0-fff3-3e90-b78e-3c2d031dbea4 | -13.2595 | -54.3283 | 2026-07-04 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 0f977cc1-8e14-31fe-9260-894445084877 | -10.9209 | -43.0384 | 2026-07-04 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 277.8 |
| 97900fcc-be42-3cde-8463-b21f503c957b | -13.2401 | -54.351 | 2026-07-04 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 187596f0-feda-32f2-9f33-5cf30f2c6802 | -13.2404 | -54.3303 | 2026-07-04 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cb198a58-9401-3424-91f9-2cc9f6180fa6 | -12.7741 | -44.5396 | 2026-07-04 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 594b8901-3e70-3fed-aac8-8b23714d3c27 | -13.2592 | -54.3489 | 2026-07-04 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 216.5 |
| db64e7c2-0d52-3a1b-9e2a-99726b472275 | -10.9205 | -43.0622 | 2026-07-04 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 263.9 |
| 0505db1c-bb49-3296-a7ad-b82400e71ffb | -10.9397 | -43.0593 | 2026-07-04 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 241.0 |
| 252a5c78-da04-332c-b4b4-e7662e6d9af9 | -13.2404 | -54.3303 | 2026-07-04 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 90dc508c-bc31-37bf-a63c-c3705660499c | -12.7359 | -44.5225 | 2026-07-04 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| e74813e5-9e97-38ee-84a1-4852170cd379 | -10.9401 | -43.0355 | 2026-07-04 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 224.7 |
| 65b8c470-4056-3fd4-a270-5228fc8fcc85 | -10.9397 | -43.0593 | 2026-07-04 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 26ba2f96-7058-3a73-b43a-17cab6c908ac | -13.2592 | -54.3489 | 2026-07-04 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 206.6 |
| b57e2ad2-de5e-3fb1-925c-23c47f1689da | -12.7548 | -44.5428 | 2026-07-04 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 4bf6cd39-a9a1-3715-8c2d-9e0d9cc2f848 | -10.9205 | -43.0622 | 2026-07-04 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 243.6 |
| 9406ef34-7705-37fe-b782-0da2f11b38bb | -13.2595 | -54.3283 | 2026-07-04 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 59a3750b-31c6-3a84-98fa-f68ae89cbf49 | -10.9209 | -43.0384 | 2026-07-04 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 374.4 |
| f07ebd71-2133-3bdd-a18d-860d8456cf37 | -4.3402 | -47.7645 | 2026-07-04 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 9d00d76b-1bf6-32d0-8bda-2641cb68ba37 | -13.2401 | -54.351 | 2026-07-04 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 0c92a8e0-3f38-3034-9094-85416d4ae624 | -12.7553 | -44.5194 | 2026-07-04 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 135482f5-ac47-3041-9fff-088c3b99c8ab | -4.3588 | -47.7636 | 2026-07-04 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 4b272a00-c74f-34b9-a731-35254da5c5bf | -13.2592 | -54.3489 | 2026-07-04 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 195.9 |
| 48cd2d20-0613-34d2-87ac-7b1386ef8133 | -13.2401 | -54.351 | 2026-07-04 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| cef75fce-0f14-3d2e-9084-fe8135099e39 | -13.2404 | -54.3303 | 2026-07-04 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 9b2fc314-7453-3d0d-a51e-fedc1c7995a9 | -13.2398 | -54.3716 | 2026-07-04 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 4748d43e-41be-3a0e-9799-6ab2bb8a086e | -10.9401 | -43.0355 | 2026-07-04 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.0 |
| f824ab18-5ec3-342e-a56b-0042c084e562 | -10.9205 | -43.0622 | 2026-07-04 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 235.7 |
| 92b2e6a9-585e-3bab-82d0-db825c2cd775 | -13.2595 | -54.3283 | 2026-07-04 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 719b098b-f21b-3dfd-b5b2-555484ef4eab | -4.3402 | -47.7645 | 2026-07-04 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 12dc4a86-645d-37a6-9204-c04eff2b197b | -10.9397 | -43.0593 | 2026-07-04 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| c79bd60c-4b7f-3d1e-8691-bef2779caf39 | -12.7548 | -44.5428 | 2026-07-04 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 70cffd1f-cb8c-368c-bb2f-35f2e5c83901 | -12.7553 | -44.5194 | 2026-07-04 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| eefbfcc7-1602-30c7-ab82-691ec8c9db07 | -10.9209 | -43.0384 | 2026-07-04 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 338.0 |
| d42d11d3-5fa8-3e89-8080-124480dd57ee | -10.9209 | -43.0384 | 2026-07-04 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 255.2 |
| 703816a6-e1ba-3f2b-8c88-a34750e91cc9 | -13.2595 | -54.3283 | 2026-07-04 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 138.0 |
| d48db2e6-5ff4-398a-9adc-3b0a0ac2d771 | -4.3588 | -47.7636 | 2026-07-04 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 170f024e-43a5-313c-bbea-1714f52a1769 | -10.9205 | -43.0622 | 2026-07-04 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 82beab53-c439-3578-862d-cdca9bc8f36a | -12.7741 | -44.5396 | 2026-07-04 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 7a948002-42c2-3622-9f7d-cb286eb7100e | -10.9401 | -43.0355 | 2026-07-04 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| f613eec8-2cf0-3e76-bbf9-9380385155cf | -12.7548 | -44.5428 | 2026-07-04 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| b0b1344e-1058-3682-b0ee-dad81b9fe90e | -13.2401 | -54.351 | 2026-07-04 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 200.5 |
| 7a423a5c-3259-3890-b74a-607751671314 | -12.7553 | -44.5194 | 2026-07-04 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 3f719193-a75d-3089-bede-6ea7d5aafade | -10.9397 | -43.0593 | 2026-07-04 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 56f434a6-f43f-3033-8aed-1a33b1c77a2a | -4.3402 | -47.7645 | 2026-07-04 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| f9dc0bdf-6fde-3ab6-b37b-384449ee695d | -13.2404 | -54.3303 | 2026-07-04 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 212a0d5e-5775-35f2-aff6-345901a94bab | -13.2592 | -54.3489 | 2026-07-04 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 224.7 |
| 0dc61d85-236d-3c3b-8da3-f1b7a6e6dde0 | -13.2398 | -54.3716 | 2026-07-04 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f0bed1df-000d-351c-b4d8-f738fa25c343 | -10.9209 | -43.0384 | 2026-07-04 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |


[Clique aqui para ver as próximas entradas](README5.md)
