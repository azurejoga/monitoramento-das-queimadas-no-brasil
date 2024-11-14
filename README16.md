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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac83c6b2-1dfa-3448-a6f4-8d2550314dd6 | -3.8857 | -46.0923 | 2024-11-14 02:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f726316b-0bf5-3414-8bb6-5aa9bc3a17d9 | -17.5869 | -57.5533 | 2024-11-14 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 34138bd3-56e2-31a1-b354-41666118f1a3 | -1.7922 | -52.1655 | 2024-11-14 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 196.3 |
| 0c91d4eb-b88e-3d4c-bc53-f668ff1e9481 | -17.5872 | -57.5328 | 2024-11-14 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 653db1a6-c8df-3da1-a54b-9a3fcfcc44e8 | -17.6066 | -57.551 | 2024-11-14 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| a053598e-8416-3e09-bacd-99a4ea2e96dd | -1.8106 | -52.1652 | 2024-11-14 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 294.1 |
| 1bc90f2e-fc74-39f8-86d8-ce13d4b9cf01 | -3.271 | -50.5778 | 2024-11-14 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 0a544f48-49ac-35b4-af28-e10e29369ca0 | -1.3894 | -51.1197 | 2024-11-14 02:20:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| b91a710c-ef2f-341f-90f6-617d984b77cf | -17.2543 | -57.4698 | 2024-11-14 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| f0fa1c34-7a98-39a5-8307-3ff946864da9 | -4.0003 | -45.5728 | 2024-11-14 02:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3db421b5-e2b6-3f89-8be1-53c5209dab7d | -1.4078 | -51.1195 | 2024-11-14 02:20:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 647385db-00ef-33e3-a637-0b02c4ca3e0d | -2.8791 | -51.7932 | 2024-11-14 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a61b98cc-8a81-399b-841b-21aeca145af2 | -17.5675 | -57.5351 | 2024-11-14 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 67421a3f-706c-3237-a8af-c52fb8910b36 | -1.7921 | -52.186 | 2024-11-14 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 5ccc8a48-87fd-3e1f-b9c6-9d17c50cf5e3 | -3.714 | -50.6046 | 2024-11-14 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f921890e-511e-3651-9983-4c94a5f7372c | -1.3894 | -51.1405 | 2024-11-14 02:20:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 20d3c67b-70d2-3565-b284-f0a9ae43a09b | -17.6263 | -57.5486 | 2024-11-14 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 7033e90c-0771-3467-ad25-765bd48d48d5 | -6.0472 | -44.0331 | 2024-11-14 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b4dde23d-aa06-305c-a12d-32bf624d32ab | -1.8105 | -52.1857 | 2024-11-14 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 213.9 |
| 92fcfc33-9b41-3a8f-859c-a8aba0a853f8 | -2.2729 | -45.347 | 2024-11-14 02:20:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 79901d77-ff68-3cce-bf9c-94805c0aed34 | -1.3894 | -51.1197 | 2024-11-14 02:30:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c0d51b93-76e6-33a2-ab79-4a3e2ef4f683 | -3.714 | -50.6046 | 2024-11-14 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7de9c039-49f2-35ba-8083-0c9ad40876a4 | -1.7921 | -52.186 | 2024-11-14 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| d43d9d41-f604-3e4f-9d16-cbab9be3292c | -17.5675 | -57.5351 | 2024-11-14 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 3ec9d656-1610-363d-a355-12896b16b450 | -3.1453 | -45.4978 | 2024-11-14 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 42b83614-a766-359a-9334-0a91e0ba8a3b | -1.7922 | -52.1655 | 2024-11-14 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 179.0 |
| 935229ab-d896-3795-87e0-ce51b858dce9 | -2.2729 | -45.347 | 2024-11-14 02:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 5845dd1b-c18c-3f3e-ba81-814af2e65013 | -17.6066 | -57.551 | 2024-11-14 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 99fba0b0-b116-3a8a-9a98-8fa3a9530a6b | -2.8791 | -51.7932 | 2024-11-14 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 19eb2585-3712-3756-b026-6c855145f036 | -1.8105 | -52.1857 | 2024-11-14 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 179.0 |
| e66a41e8-55c1-3811-92e4-f0c66328a0db | -17.5872 | -57.5328 | 2024-11-14 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 418ee80f-fff4-3d8f-b74e-221f2be5916d | -17.6263 | -57.5486 | 2024-11-14 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.5 |
| 64c8e9c1-5ec4-3b7b-b766-7566a5745f2d | -3.1454 | -45.4753 | 2024-11-14 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 85904772-64f0-3bfe-8f7e-b2afc9a12108 | -1.4078 | -51.1402 | 2024-11-14 02:30:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 12090dbc-9c9f-303e-9d3b-1224750ce772 | 1.0663 | -60.5985 | 2024-11-14 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3160d211-ba8c-3c5b-91aa-025d2e9cbe27 | -17.6079 | -57.4688 | 2024-11-14 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.5 |
| 7a1d1191-0e25-3b13-94b7-3bdce932334b | -17.6076 | -57.4893 | 2024-11-14 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| c69de6cd-93f7-33e2-8782-90f23337900c | -1.4078 | -51.1195 | 2024-11-14 02:30:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| bc4e1be3-6bf8-3e1f-bab2-765b136466a9 | -1.8106 | -52.1652 | 2024-11-14 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 267.2 |
| 92600ca2-c13c-3f98-a39d-50679d54aaea | -17.2543 | -57.4698 | 2024-11-14 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 992c12e3-47fe-3bbb-914b-552cbbe6c1d9 | -6.0472 | -44.0331 | 2024-11-14 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 54a333e7-ecd0-37fc-82ce-b1097750d3f4 | 1.048 | -60.5986 | 2024-11-14 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 834e9ceb-bd53-3f51-b51f-17d436d5a7f5 | -17.5869 | -57.5533 | 2024-11-14 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.3 |
| d3fae911-a666-3d75-a285-80dfa4a9493a | -2.2914 | -45.3465 | 2024-11-14 02:40:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2b29b10a-3d25-37fd-975b-09efad104711 | -17.2543 | -57.4698 | 2024-11-14 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 0cf28839-789f-35a2-aaf9-66967415e9bf | -1.4078 | -51.1195 | 2024-11-14 02:40:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8c3d9b9e-22ee-3c55-a408-97b4057cef63 | -17.5869 | -57.5533 | 2024-11-14 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.9 |
| a75d9051-dee2-35b8-82f4-9f73252753d1 | -3.271 | -50.5778 | 2024-11-14 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 032246b1-b8e1-3eaf-82a9-4350cdf22d7a | -4.5614 | -48.0141 | 2024-11-14 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 3c8a9dd3-c524-3fdf-8479-a866504a6011 | -17.7052 | -57.5392 | 2024-11-14 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| df88c854-ffc4-302d-a32a-f58546764746 | -17.6066 | -57.551 | 2024-11-14 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 98df1867-5058-3900-83e1-900c7c0d307b | -1.7921 | -52.186 | 2024-11-14 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 081cd490-0df1-32b1-ac3a-3164d98a7585 | -2.2729 | -45.3245 | 2024-11-14 02:40:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e6a345d1-6b01-3539-83fb-b6c40294d26a | -17.5675 | -57.5351 | 2024-11-14 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| aaa0605d-fa79-3d48-b95e-2d6b3c5bbd27 | -17.5672 | -57.5557 | 2024-11-14 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| ff97f436-2200-3ac0-94e7-b4bae81071a1 | -1.3894 | -51.1197 | 2024-11-14 02:40:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 12f8431d-b373-36a2-8636-56ae5197f035 | -1.7922 | -52.1655 | 2024-11-14 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| 59750dae-7a6a-3723-9f2d-abb161eb5fb1 | -3.714 | -50.6046 | 2024-11-14 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 31806a3e-107e-3499-a848-b98abe6ce121 | -2.8791 | -51.7932 | 2024-11-14 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 838d7245-045c-3388-8ede-864b05800303 | -1.8106 | -52.1652 | 2024-11-14 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 18635091-8e2b-3134-a391-07609b97e75b | -2.2729 | -45.347 | 2024-11-14 02:40:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 209.9 |
| f22d2f8a-5de5-3a6f-8c5e-4332c009aa39 | -6.0472 | -44.0331 | 2024-11-14 02:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 5db9763d-c25c-3372-977f-5c2b8ce61153 | -17.6076 | -57.4893 | 2024-11-14 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 9e72d967-5bdc-3961-9337-0c0295ffdc4e | -17.5872 | -57.5328 | 2024-11-14 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 6977b93e-fe76-3a83-87fd-c26d16462596 | 1.048 | -60.5986 | 2024-11-14 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d6504fcb-1a7f-3e21-b2ec-5d7d1adef0c2 | -1.8105 | -52.1857 | 2024-11-14 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| ad2bdbf5-fb61-37ae-825a-91579d29d092 | -17.5869 | -57.5533 | 2024-11-14 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.1 |
| e93aa1e6-b68b-3ed5-9691-cd74de9e93b5 | -2.2914 | -45.3465 | 2024-11-14 02:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 19c515c7-4dbe-3c87-9f66-0967a2b617fe | -1.8106 | -52.1652 | 2024-11-14 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| b906ebd7-bbbb-37cb-b626-58efbf6fcf96 | -1.8105 | -52.1857 | 2024-11-14 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 18ba2608-31c9-3255-97a7-5769c72a8e99 | -17.2543 | -57.4698 | 2024-11-14 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| cbe2d641-b997-3d02-b532-9807b864be7d | -1.3894 | -51.1197 | 2024-11-14 02:50:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b0693d47-c112-36bb-9408-9c5fc197c26a | -17.6066 | -57.551 | 2024-11-14 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 4e264fe8-76ac-3b5a-874f-14721507de30 | -6.0472 | -44.0331 | 2024-11-14 02:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7c2f507f-24da-3a94-8b7c-e79a4c340db4 | -17.6076 | -57.4893 | 2024-11-14 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.6 |
| 9d8e3314-9152-3176-93cb-c370f5af498d | -1.4078 | -51.1195 | 2024-11-14 02:50:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 275f7526-006a-329c-a250-e8382b662f58 | -17.7052 | -57.5392 | 2024-11-14 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.0 |
| 2fa0d342-13ed-304e-b6ea-afec001ae44c | -1.3894 | -51.1405 | 2024-11-14 02:50:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2bcfd425-424e-31ec-880f-952ffc3bd238 | -3.714 | -50.6046 | 2024-11-14 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| cb15718d-4e33-34bc-8da7-05e9f3efd550 | -4.5614 | -48.0141 | 2024-11-14 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 6aefd705-e2bf-36d6-bd95-43cdbdde64a5 | -17.5872 | -57.5328 | 2024-11-14 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| cf48b63d-5d92-3fe2-9662-7f59868850c2 | -2.2729 | -45.3245 | 2024-11-14 02:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 809df157-08ae-3d8d-81b3-510994594200 | 1.048 | -60.5986 | 2024-11-14 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 75ef6431-6834-327a-a7a2-c511ab001ba1 | -1.7921 | -52.186 | 2024-11-14 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 181fb01d-4c3c-3652-a918-0704509f8e5e | -17.5675 | -57.5351 | 2024-11-14 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| f1cb73ef-aa08-37f2-8a31-5248e1b30712 | -2.2729 | -45.347 | 2024-11-14 02:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 196.5 |
| 7a3b2c83-7274-3b31-9a6b-882e42142687 | -1.7922 | -52.1655 | 2024-11-14 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| ec8f88dd-c008-302e-863e-9ad0a11d938b | -3.271 | -50.5778 | 2024-11-14 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 43b92e54-300f-35cb-936f-854ced15ff1a | -1.4078 | -51.1195 | 2024-11-14 03:00:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 883aeaeb-cfec-3c8b-a6ce-3139bd732cf7 | -17.5872 | -57.5328 | 2024-11-14 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 45786a06-993d-3988-a702-5d7419476bc0 | -17.6066 | -57.551 | 2024-11-14 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| e8a5bbd7-6010-39f5-bdca-cac3abc574e2 | -1.3894 | -51.1405 | 2024-11-14 03:00:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 6f79e1d4-cbf8-3c86-8437-b536dd1923dc | -3.714 | -50.6046 | 2024-11-14 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| fbbac89c-1979-30be-84f5-e6df87205e62 | -1.7922 | -52.1655 | 2024-11-14 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 049544a8-b55a-3a10-81e3-a511bd9e8895 | -1.7921 | -52.186 | 2024-11-14 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| b45a8359-c510-3c9f-b578-3ea08d781cdc | -1.8105 | -52.1857 | 2024-11-14 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 6a7d1721-a5a5-3d7d-aa2f-a4ca9536a2f6 | -1.3894 | -51.1197 | 2024-11-14 03:00:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 35c18f55-43f6-3bf1-8128-7218ffef9c0f | -17.2543 | -57.4698 | 2024-11-14 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 8ed06159-0d6a-3d90-ad08-289bf19e36df | -17.5879 | -57.4917 | 2024-11-14 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| ef330a60-c1c9-3f60-b373-53f73e0842b1 | -1.8106 | -52.1652 | 2024-11-14 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |


[Clique aqui para ver as próximas entradas](README17.md)
