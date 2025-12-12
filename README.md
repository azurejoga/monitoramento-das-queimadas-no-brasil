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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac9b7c78-7874-3fdd-8e0e-645832ae149e | -2.5108 | -51.7817 | 2025-12-12 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| cafcdfd8-3552-3b0f-a658-0a6cda791193 | -12.4325 | -58.0276 | 2025-12-12 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 196.8 |
| a8c25160-ad70-35db-89c4-5c28b67a0fb9 | -2.2169 | -45.4159 | 2025-12-12 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 294.4 |
| e696f536-101f-3d32-bd06-01c745167a36 | -3.2371 | -42.0565 | 2025-12-12 00:00:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| d2ce1922-5594-3c9b-8a2e-51f1f5f38e9f | -1.5153 | -52.7416 | 2025-12-12 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 8f40c360-9375-3605-bc8d-7ebb2e0f2644 | -3.0695 | -45.814 | 2025-12-12 00:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4892847c-4770-332c-98db-d87ffc08235a | -3.1284 | -54.1857 | 2025-12-12 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| fd2185be-0db2-32ee-8161-9eb5d3ba20ce | -12.3943 | -58.0506 | 2025-12-12 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c11d236c-8726-3c07-8e74-5f687b9dd064 | -3.051 | -45.8147 | 2025-12-12 00:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f99c0806-5fd9-3485-8bb5-3c6114944f08 | -4.7448 | -43.081 | 2025-12-12 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| c59a747b-472d-31f3-982b-742312cc73f8 | -2.1984 | -45.394 | 2025-12-12 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 8803e5e4-cc1a-37e4-baed-999366534dae | -3.9699 | -41.5176 | 2025-12-12 00:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| dbd76fa1-b3f4-3e7f-8d65-c023d9413316 | -2.1984 | -45.4164 | 2025-12-12 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 83db2adb-afa0-3172-8667-42fcb2231f4d | -3.0697 | -45.7693 | 2025-12-12 00:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 4f4f4fb1-b5a3-3289-a51d-27720b4a9928 | -6.1117 | -41.2892 | 2025-12-12 00:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 141.0 |
| 5b2e6825-2793-3466-87dc-7f7c7777ed34 | -3.237 | -42.0802 | 2025-12-12 00:00:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a7b59dc8-7f03-3ea9-8bd6-f214b3345091 | -2.1419 | -45.6644 | 2025-12-12 00:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 6bb0a9d5-c986-335d-a992-cabdcc32ca44 | -12.4133 | -58.049 | 2025-12-12 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 329.5 |
| 03f1c9f0-5365-36be-afd4-f1c26d74bcc8 | -1.2494 | -46.7688 | 2025-12-12 00:00:00 | GOES-19 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0ddde938-02e0-3a67-910e-48395eb8f4f5 | -12.3946 | -58.0307 | 2025-12-12 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ed021516-b9f6-3211-a31f-0b595c764ded | -12.4135 | -58.0292 | 2025-12-12 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 346.0 |
| 7aad350f-1c73-3c3f-9bd2-ea794d2acecb | -3.6293 | -45.3878 | 2025-12-12 00:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 92bf893f-df35-378d-840d-71357633ecf2 | -2.2355 | -45.4154 | 2025-12-12 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 205.1 |
| f1b45a4d-7f84-33e4-a444-ea8040606c6e | -6.1306 | -41.2875 | 2025-12-12 00:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| a6c64bab-7a56-3449-afd7-dfaa8deeabb1 | -2.5108 | -51.8023 | 2025-12-12 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| b4e7b41a-189e-352d-8004-10c9d239c029 | -2.487 | -47.7692 | 2025-12-12 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 25cdc33d-4a45-3777-969d-3032f0daf74d | -2.4924 | -51.7821 | 2025-12-12 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| edc0fbf1-741b-3ec5-bb26-5e2397b9e942 | -2.4923 | -51.8027 | 2025-12-12 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 5d0d0646-64a8-3e2c-b7fe-5e55e10b1992 | -4.3856 | -43.6381 | 2025-12-12 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 13092bae-a01e-3203-9436-bd3c75016517 | -1.5337 | -52.7617 | 2025-12-12 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 00b8ec4e-dbb3-36c9-bec2-cfc79597e758 | -6.1308 | -41.2633 | 2025-12-12 00:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 0807f1ca-3783-374f-9b16-df8410f41e41 | -4.7261 | -43.0822 | 2025-12-12 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 2aad7019-8d32-31ee-9e0a-ee5248ffc767 | -3.9511 | -41.5186 | 2025-12-12 00:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 23cb5c61-583a-32b0-86e0-87f03643f679 | -4.4043 | -43.637 | 2025-12-12 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 85366ca3-d66c-33ed-bcbd-6c641bef8bd3 | -1.5337 | -52.7414 | 2025-12-12 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 83079ea3-dada-383b-8124-446d17a578c5 | -2.217 | -45.3935 | 2025-12-12 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 424.5 |
| cf337c42-27a0-316c-b683-93d4c5ef4a12 | -1.2495 | -46.7468 | 2025-12-12 00:00:00 | GOES-19 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| ac885046-6239-328d-9671-55bced415bde | -6.112 | -41.2649 | 2025-12-12 00:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 095aa91f-e4e2-3a36-9abf-8cb1af68ef0c | -3.0696 | -45.7917 | 2025-12-12 00:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 204.6 |
| 41b5597f-583d-3d27-947f-8f01a126057b | -12.4323 | -58.0475 | 2025-12-12 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 183.4 |
| d78045fe-2f04-3b00-9002-6eb43e93ef7a | -4.3858 | -43.6149 | 2025-12-12 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 068b4a39-c167-35e6-8c49-83454b8853a8 | -3.0511 | -45.7924 | 2025-12-12 00:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 6306bddd-1e66-377f-ab81-6bb0ea1f4d1b | -2.2356 | -45.3929 | 2025-12-12 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 234.3 |
| 1a6c4b5d-4d1c-38d2-ab7b-a5df1e0205b9 | -2.142 | -45.642 | 2025-12-12 00:00:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 82c0ac83-dba0-35de-8d23-9f5e2e913186 | -1.5153 | -52.7416 | 2025-12-12 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 6d6f5245-b609-30c1-9ceb-347780a11e74 | -3.237 | -42.0802 | 2025-12-12 00:10:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| df0e29e9-87eb-31c0-a280-0aef1d81be3c | -2.5108 | -51.7817 | 2025-12-12 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 68497806-ff7a-3c85-ad35-173753ce794a | -3.0695 | -45.814 | 2025-12-12 00:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b030e43e-77fc-3dfd-9dc0-a216d18f03a8 | -1.5337 | -52.7617 | 2025-12-12 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| c7c2438a-351f-3514-ba84-d32ef2f1c39e | -6.112 | -41.2649 | 2025-12-12 00:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| f631d1bb-7c78-3afd-a2a0-5d3845762cc7 | -3.051 | -45.8147 | 2025-12-12 00:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 88d83330-2024-3106-b481-1c6d2c85b434 | -3.0696 | -45.7917 | 2025-12-12 00:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 0c653227-0844-3608-b31f-e02869d9d44d | -2.217 | -45.3935 | 2025-12-12 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 354.9 |
| bf4422bc-0fc3-3b62-9bde-553294ad2461 | -4.3342 | -45.7576 | 2025-12-12 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d1bf8640-8002-311a-865b-06be365f8648 | -2.1419 | -45.6644 | 2025-12-12 00:10:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b199ca60-e531-32cc-8c69-655899664ade | -2.4923 | -51.8027 | 2025-12-12 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 8b33e785-5c1c-3b2d-ad76-da21ceb1a25e | -12.4133 | -58.049 | 2025-12-12 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 289.5 |
| 99168090-7df2-3ff0-b9dd-8da4e2673f73 | -4.3527 | -45.7791 | 2025-12-12 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a3a4f858-757f-3925-8268-1c30d254515f | -12.3946 | -58.0307 | 2025-12-12 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 7bdea2dd-f619-365f-9cb7-ef59e38feb6b | -12.4135 | -58.0292 | 2025-12-12 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 372.3 |
| ec95b4cf-2d0f-3249-b39e-2e2c6405286f | -6.1306 | -41.2875 | 2025-12-12 00:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 26ff1fbb-c2c7-3357-9c24-361070e50168 | -2.2355 | -45.4154 | 2025-12-12 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 184.9 |
| 1ccd2d54-08e1-3505-9e73-43a8ee886e87 | -4.3858 | -43.6149 | 2025-12-12 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 3c6913bc-2c03-3830-a2ae-5d0d18fa8a05 | -2.1018 | -53.4223 | 2025-12-12 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 6fc0938f-e5d6-38d4-af43-e04b75bc4d14 | -2.5108 | -51.8023 | 2025-12-12 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 6f216ba1-dd4b-37b7-aaf5-e761ba42de0c | -2.1984 | -45.4164 | 2025-12-12 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 95.7 |
| d9286891-5f2f-3756-b972-317c445686e8 | -4.334 | -45.78 | 2025-12-12 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 86aa1cc0-b2db-328a-8c2d-378ccb58a879 | -12.4323 | -58.0475 | 2025-12-12 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 160.8 |
| e558de0d-78df-36ab-9cae-a7e056c29453 | -2.4924 | -51.7821 | 2025-12-12 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 942b69f2-0630-31e3-be1b-c49913d3d6a2 | -3.0511 | -45.7924 | 2025-12-12 00:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 44dcd0af-b9a1-34d2-8abb-8768dc3a029f | -1.5337 | -52.7414 | 2025-12-12 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 03850449-b673-39f0-bae4-79b6852da735 | -12.3943 | -58.0506 | 2025-12-12 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 79217136-038a-389e-9c1a-4ed5ad311c03 | -2.1984 | -45.394 | 2025-12-12 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 47886dc2-5721-3748-90a0-7e854492da93 | -12.4325 | -58.0276 | 2025-12-12 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 3462f026-d16f-39c1-990d-73965a0a20b6 | -3.6293 | -45.3878 | 2025-12-12 00:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| c00469a9-3a58-3189-ba98-c8da85cd4ff1 | -2.2169 | -45.4159 | 2025-12-12 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 327.1 |
| a3573632-c4c6-37b5-a689-8eb5b503224a | -3.9511 | -41.5186 | 2025-12-12 00:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| ba7b431c-e754-3b03-bf99-af2f9821f9ed | -6.1117 | -41.2892 | 2025-12-12 00:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| ad0627df-1a61-329a-b321-9cbff48d01b8 | -3.0169 | -45.1426 | 2025-12-12 00:10:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 55b72314-2492-3199-b1ab-24de4f0cb8aa | -3.0168 | -45.1651 | 2025-12-12 00:10:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7dd4b7fd-4121-3a11-adf4-55547c777bff | -2.2356 | -45.3929 | 2025-12-12 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 188.1 |
| 93664614-d10e-3e67-86ee-cf91a76a6fbb | -6.1308 | -41.2633 | 2025-12-12 00:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 5a2cfd1e-e402-3bb5-8a97-c6f11919f3cd | -4.3856 | -43.6381 | 2025-12-12 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| c2b19356-afc8-38cf-bc9d-ee8a99b7ec81 | -2.654 | -51.6292 | 2025-12-12 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 086c3a4d-02b7-3326-a196-11e083cb81d4 | -4.3749 | -43.626099 | 2025-12-12 00:14:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0adbcf5e-83c4-3576-84b7-8038afeeee4c | -20.5336 | -42.503899 | 2025-12-12 00:14:00 | METOP-B | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e136e131-3611-391b-bedb-ea3d1725c0cb | -5.4647 | -47.072498 | 2025-12-12 00:14:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68d0971a-0116-34e9-96be-b37c9fc7a632 | -3.702 | -50.935398 | 2025-12-12 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7fa0226-0c89-3855-9bf8-eccc5236bb6c | -2.4422 | -51.922199 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42fdbbf0-11ec-30c2-a60c-bd7976645428 | -2.3319 | -45.773899 | 2025-12-12 00:14:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d47f2c2-b1b8-3e59-ad94-e07cf5a42a61 | -2.4391 | -51.908401 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 035ac62c-ee1f-33f9-afe7-4595f7192510 | -2.5224 | -45.5765 | 2025-12-12 00:14:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 970fe64e-cb60-37f0-ae12-a47ae33ee691 | -19.892401 | -46.021999 | 2025-12-12 00:14:00 | METOP-B | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 11dfa4c4-1ccb-3e97-ab70-4a35daec3ac7 | -12.4286 | -58.002998 | 2025-12-12 00:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48540472-3b38-362f-a7d0-06c6a58f3c4f | -3.6157 | -45.371899 | 2025-12-12 00:14:00 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 72e69df4-c830-3f67-9b73-13ffb1ce51f4 | -3.9589 | -41.507301 | 2025-12-12 00:14:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 177b65a3-6670-3451-877a-8280e8d58a8b | -2.4195 | -51.9128 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b09f97e9-11aa-30b4-b4c9-113011be9a7d | -12.413 | -58.0266 | 2025-12-12 00:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97083d4c-4c85-3c76-8cc4-eaca51438f8d | -3.478 | -50.856201 | 2025-12-12 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 310e3ba5-9413-320a-82fe-5ff007091190 | -6.1102 | -41.258499 | 2025-12-12 00:14:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
