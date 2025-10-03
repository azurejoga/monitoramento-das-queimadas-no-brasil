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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 095291d3-f6de-3b76-b3e6-c00898470b55 | -5.8469 | -43.3995 | 2025-10-03 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e8e1959c-7384-3d4c-83d4-592732de4479 | -5.3851 | -47.2052 | 2025-10-03 01:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 04de6ecd-1451-3717-9744-e8de52a37562 | -11.9163 | -46.2817 | 2025-10-03 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 4dc12545-bc2c-3183-ba6a-ec0bd02a77a4 | -18.7931 | -42.4884 | 2025-10-03 01:00:00 | GOES-19 | SARDOÁ | MINAS GERAIS | Brasil | 3165503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.4 |
| c226f0f9-d77a-3dae-8f8e-0121d2ef27ac | -14.877 | -46.838 | 2025-10-03 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c5095c49-0f72-3911-875b-a65fb2a6db32 | -10.948 | -51.0846 | 2025-10-03 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 6d29f25b-f033-3ee2-b6bb-02e6f170b8d0 | -6.2594 | -45.3636 | 2025-10-03 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 4e3040fe-9339-3322-a771-e1e8f5dbea7f | 1.5103 | -55.8259 | 2025-10-03 01:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 22447670-e7d9-39ca-98c6-741c108b3d06 | -7.9137 | -43.5369 | 2025-10-03 01:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 6cbca589-0a84-3d13-8da4-d553186ce642 | -14.8966 | -46.8346 | 2025-10-03 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 94032236-e334-343c-bb78-d05c4b41bbd3 | -18.8135 | -42.483 | 2025-10-03 01:00:00 | GOES-19 | GONZAGA | MINAS GERAIS | Brasil | 3127503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.7 |
| 18c84c12-2d0d-3b94-8e8c-76fe568bef96 | -4.669 | -45.8066 | 2025-10-03 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 257.2 |
| 6ab5c7ef-2f27-3af1-b86a-ec9ce9d09c0e | -4.6504 | -45.8077 | 2025-10-03 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 140.0 |
| c7ec4457-4f82-34ad-a5ce-907885891b35 | -4.6878 | -45.7832 | 2025-10-03 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d6d3dd2e-109b-3f95-ac5c-eec3da0f83ee | -12.6135 | -46.9499 | 2025-10-03 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 3dd14b94-f662-352c-b7d2-6dac5e7207f0 | -10.2569 | -36.3362 | 2025-10-03 01:00:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 136.8 |
| 96895e1e-6233-3f69-a598-b01e7eddb73e | -4.6692 | -45.7842 | 2025-10-03 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 324.4 |
| e7662ed8-0431-375a-8c1a-83cc4f59b676 | -10.2584 | -50.3692 | 2025-10-03 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 0b7904c5-fecb-30e1-a79d-07fd726bd58f | -6.2408 | -45.3424 | 2025-10-03 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 3b54b421-5b68-3e8c-b9b1-c0eb428b139c | -5.3849 | -47.2271 | 2025-10-03 01:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 2da7ffa1-41ac-3379-81da-2a23db72fbbd | -3.9331 | -47.5655 | 2025-10-03 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 98a41b64-4f64-364c-9544-26d56b08bb0e | -7.7496 | -46.2496 | 2025-10-03 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 3bed7cbd-26a9-3d52-9cd2-6694657bdb65 | -8.6138 | -54.976 | 2025-10-03 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 90a777ea-eb78-34fb-a5e8-ceeb62254f1e | -10.2587 | -50.3478 | 2025-10-03 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| fcee5ffa-9b27-333f-9eb3-349423f7dc34 | -11.9167 | -46.259 | 2025-10-03 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| eb482af9-c238-39d9-821e-fefa8abb32ad | -11.144 | -43.4082 | 2025-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 131.6 |
| 1d88bbd1-c71c-3a44-ac89-b16eaa283b4e | -9.9182 | -43.7212 | 2025-10-03 01:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 26a583db-7475-3233-a3c8-d8073532c474 | -5.6361 | -43.9258 | 2025-10-03 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 8b15c88c-efe9-345a-b651-c1d117837a55 | -5.6176 | -43.9041 | 2025-10-03 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e4baf1fa-8030-3acc-8b1f-bffa68a4f445 | -10.2762 | -36.3327 | 2025-10-03 01:00:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| 37999d4d-7c13-32d6-b92b-3f6c6c7b5578 | -17.595 | -46.6882 | 2025-10-03 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d668df89-390c-3d9a-81a3-de945762d9b3 | -12.6323 | -46.9697 | 2025-10-03 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 79ad2dc0-cb12-3c58-9cab-2db56def9578 | -6.0605 | -44.6061 | 2025-10-03 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 8180edef-6d15-3f74-a977-439a85bb10db | -11.1631 | -43.4054 | 2025-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 89.4 |
| f9c1102e-31f4-39e8-9509-00df94c15fb4 | -8.6324 | -54.9747 | 2025-10-03 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| cbece0e9-b3e4-3d09-be5c-6df7b2902915 | -5.8657 | -43.3981 | 2025-10-03 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 024b4c88-b723-32de-8b5c-25fb223eb38f | -14.9342 | -46.8965 | 2025-10-03 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 125.5 |
| c2e36a90-f33d-32d4-9351-423d9e153e34 | -17.5956 | -46.6648 | 2025-10-03 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 57291211-b14d-3a34-8463-43693e719b9f | -10.2564 | -36.3633 | 2025-10-03 01:00:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.2 |
| 86758365-6c67-345f-949c-b204796094dc | -6.0418 | -44.6076 | 2025-10-03 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e8749fdd-685d-3cfd-a18e-5ce42fdc9a64 | -14.8961 | -46.8575 | 2025-10-03 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 2119a1ea-a8ee-385a-ba48-e65d4e01293c | -4.6505 | -45.7853 | 2025-10-03 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 190.4 |
| 212fe8f1-e720-3ded-8ae6-5b6d4fa42db3 | -11.1444 | -43.3845 | 2025-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 89.0 |
| bd6add4f-0718-3611-81e7-ae6341892bd3 | -6.2406 | -45.365 | 2025-10-03 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 710afe37-1cb5-3631-8bad-62bbc3a31841 | -5.6363 | -43.9027 | 2025-10-03 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 1040931d-b56e-3813-b4ce-fe52515455e4 | -19.7244 | -45.8804 | 2025-10-03 01:00:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 60.1 |
| ad872301-092f-3fbf-af5f-03ffde300038 | -5.6174 | -43.9272 | 2025-10-03 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6310e9a1-dc48-3c68-b6cd-2d59eea68fbd | -6.0416 | -44.6304 | 2025-10-03 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 3cb95135-ea60-3b30-96c5-203c7c835560 | -12.6131 | -46.9725 | 2025-10-03 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 6ee3ad19-0c85-3dc4-885d-c27b6e556499 | -14.8766 | -46.8609 | 2025-10-03 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 42de1756-9bf9-320a-9917-856dcb286b4d | -6.0603 | -44.629 | 2025-10-03 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| d099e7c4-21f9-31b2-a4e8-31a2d165157c | -6.0603 | -44.629 | 2025-10-03 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 62f2c5bf-65f4-31d4-bfa2-d80c42318163 | -8.6138 | -54.976 | 2025-10-03 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 561829f9-f997-38b4-83e9-ec1d9563a1bb | -14.8937 | -46.9718 | 2025-10-03 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 37612d07-0f88-3c7f-a92d-c70d019137b2 | -11.144 | -43.4082 | 2025-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 141.7 |
| 0bc95f7c-2505-3ed5-9cc5-4f6af17329f8 | -10.9667 | -51.1039 | 2025-10-03 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| e0bffe45-08c4-3639-90c6-46b59e5170db | -4.669 | -45.8066 | 2025-10-03 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 203.5 |
| d1f63017-473d-3cf0-856e-5dd5150e761c | -14.8966 | -46.8346 | 2025-10-03 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 4bc2a71e-795a-3921-b3da-873714b0a3a1 | -5.8657 | -43.3981 | 2025-10-03 01:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fdafab83-b667-36a9-8ea2-e23362dfe901 | -7.9137 | -43.5369 | 2025-10-03 01:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 5d31474c-a86a-3bbb-9848-c4eb4c2cac12 | -3.9331 | -47.5655 | 2025-10-03 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| ced9fd0d-d18b-3daf-9ff2-b83850eaba11 | -5.8469 | -43.3995 | 2025-10-03 01:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6fcac106-93c1-3127-ad31-6fc7172168e5 | -10.8739 | -47.0506 | 2025-10-03 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 7ddd35f0-c256-399b-919d-785c969bb615 | -8.6139 | -54.9558 | 2025-10-03 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 72db221d-5927-3461-bfed-877e1563be2c | -14.8961 | -46.8575 | 2025-10-03 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 880847fe-2832-3ea2-ae09-e764070abeab | -6.0605 | -44.6061 | 2025-10-03 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 667be337-2364-3112-b9f3-db1ea975d0b4 | -10.2587 | -50.3478 | 2025-10-03 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9d4a8310-cc33-3551-9538-a8da18d7312b | -13.7769 | -47.5392 | 2025-10-03 01:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 974e3200-e54f-39cf-90cf-ea7cb2ab5a5e | -12.6323 | -46.9697 | 2025-10-03 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |
| e8153863-d9c8-34b3-87ec-5a331689402c | -5.3851 | -47.2052 | 2025-10-03 01:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b3c8caf2-4ba3-3150-bf43-cfd30d04fcf6 | -14.877 | -46.838 | 2025-10-03 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 312c975b-d61a-3355-9f6f-41121efb6adb | -5.6176 | -43.9041 | 2025-10-03 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 9a1a776b-1a22-3508-81a1-94f633cdd444 | -11.1444 | -43.3845 | 2025-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 93.7 |
| a96a855c-7c11-3e46-877c-955101826408 | 1.5103 | -55.8259 | 2025-10-03 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6b92f54d-9a56-3980-958d-0119005c5784 | -11.1627 | -43.4291 | 2025-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 7cfa1061-e39a-3af9-8e06-7b9b9225571c | -4.6504 | -45.8077 | 2025-10-03 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 103.1 |
| d29c8d46-0206-3336-96ce-446473955e12 | -3.9517 | -47.5647 | 2025-10-03 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 6f4584c8-0eea-3ec6-a249-d0b5a1446f6d | -14.9342 | -46.8965 | 2025-10-03 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 1579ca02-6281-3e67-bc75-2e931463c802 | -5.655 | -43.9013 | 2025-10-03 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ee5dc1b2-8ab4-3f22-9f82-e31b93b9cee5 | -10.2781 | -50.3032 | 2025-10-03 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| b9766158-8bbe-3270-a39c-5071459753ab | -4.6692 | -45.7842 | 2025-10-03 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 202.6 |
| 0ea24338-eeca-3ee2-a17d-272bd72264df | -12.6131 | -46.9725 | 2025-10-03 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| a6fd0eb2-91cc-3584-a4a8-71c6dd7d443f | -9.8991 | -43.7237 | 2025-10-03 01:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 0c5a9482-458e-3aa1-b237-a3582152d958 | -9.8772 | -47.8103 | 2025-10-03 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 07a49c60-09eb-371f-8290-84294f68fc48 | -17.5956 | -46.6648 | 2025-10-03 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 89b5eeef-e4a8-3cae-9274-efff2e716bb7 | -9.9182 | -43.7212 | 2025-10-03 01:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| ec4f7926-bee0-3550-9704-1401ebb230de | -12.6135 | -46.9499 | 2025-10-03 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| b9486d20-348c-31ee-b4ff-32a741e06e90 | -6.0418 | -44.6076 | 2025-10-03 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 37fa79cf-f6f7-3776-bdaa-f6027be86aaf | -8.6324 | -54.9747 | 2025-10-03 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 1dd2edde-c6d6-3bca-8c75-f77d3953472d | -11.9163 | -46.2817 | 2025-10-03 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 4ea83d23-696e-3faf-87b0-2219461ae309 | -6.0416 | -44.6304 | 2025-10-03 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| e03e88a9-c578-317d-8e8c-6eacac309ad9 | -5.6363 | -43.9027 | 2025-10-03 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| c7266bdc-d703-31f7-95a0-db31288318aa | -12.6327 | -46.9471 | 2025-10-03 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6da5b90a-ff18-3a2f-95e2-69cbcf734802 | -14.9132 | -46.9684 | 2025-10-03 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 3e392165-593c-361e-8b44-4d55e44bd74b | -10.8742 | -47.0282 | 2025-10-03 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| cf9e0cb8-6980-3ce7-bf62-743cd03e6f54 | -5.6361 | -43.9258 | 2025-10-03 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 9fb929f5-c8c4-3ca2-b388-265052c97099 | -4.6505 | -45.7853 | 2025-10-03 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 116.7 |
| d5c3d2bf-9a4a-3d31-8dbd-b3d752196e57 | -11.1631 | -43.4054 | 2025-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 114.6 |
| fb7f2a8a-5528-3801-8aba-737172b0a0f2 | -18.6837 | -47.823 | 2025-10-03 01:10:00 | GOES-19 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 7901436b-466c-3461-8994-c0fede267629 | -10.8517 | -47.2541 | 2025-10-03 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |


[Clique aqui para ver as próximas entradas](README11.md)
