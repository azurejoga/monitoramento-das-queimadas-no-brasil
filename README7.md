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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58be47b3-eb3b-39b5-88ff-9a59eaf0edda | -7.4419 | -67.734703 | 2025-08-09 01:35:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6a53cb-9d7a-3ddd-a4ed-96f4f3c6610b | -9.5426 | -62.7271 | 2025-08-09 01:35:00 | METOP-B | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a02f4f2-e41e-3e7e-9acd-1bfafbd09e9d | -9.9297 | -60.479401 | 2025-08-09 01:35:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de9de52c-8d12-361f-967b-12d08e4ee611 | -8.9218 | -60.734402 | 2025-08-09 01:35:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8adea432-0d22-3bb2-a58d-d7b0d2907df7 | -13.524 | -55.2197 | 2025-08-09 01:35:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 914e2afe-97f8-34bf-96cb-97218c20b982 | -7.4403 | -67.727699 | 2025-08-09 01:35:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2d67c80-aa42-30d3-9b28-02482e472398 | -7.3933 | -60.0009 | 2025-08-09 01:35:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2a89f53-58fb-3dfd-a127-c588b31c2465 | -9.6994 | -61.296799 | 2025-08-09 01:35:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e6be11c-bda0-3842-8a4f-668c8b3af5c6 | -9.5398 | -62.7155 | 2025-08-09 01:35:00 | METOP-B | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4313849e-7336-31f5-960b-1e7107816e7d | -7.0632 | -59.167198 | 2025-08-09 01:35:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3cf2c91b-7127-3693-873a-b69e6cc139c2 | -8.9258 | -60.7505 | 2025-08-09 01:35:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c98ec09d-a9ba-38cc-b4d7-31853c424e02 | -8.9178 | -60.7183 | 2025-08-09 01:35:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2edf83cb-f55c-3892-932f-28dc354fa975 | -8.5879 | -62.6591 | 2025-08-09 01:35:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 377be799-1b5c-38cb-88fb-0145e8c59a40 | -8.9161 | -60.752899 | 2025-08-09 01:35:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 343de326-0373-3b7d-9f88-bcfd13f4fda2 | -13.5327 | -55.251202 | 2025-08-09 01:35:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e3ac988-c0ae-30d0-b5c4-9c89ab7b1312 | -13.5423 | -55.248402 | 2025-08-09 01:35:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36b1b3d5-1db8-36e9-a39a-0526858daf23 | -8.9401 | -60.7288 | 2025-08-09 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| adb8571c-70e3-3d35-a29c-c1c967fc4d1f | -19.8124 | -47.0634 | 2025-08-09 01:40:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 128.3 |
| efc5f9b7-9ea5-3fd4-b6d1-0c425ace1eb1 | -13.0386 | -43.8604 | 2025-08-09 01:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b1d348f4-1f1c-3d30-b4b8-f0038f6ea955 | -8.9215 | -60.7297 | 2025-08-09 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3443152c-73d6-3929-ab9d-045421b798f1 | -13.5521 | -55.2633 | 2025-08-09 01:40:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| f88eb999-9f96-314f-8a98-b7388c860247 | -8.9213 | -60.7489 | 2025-08-09 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| f662d063-74a5-3aa2-88a3-3b6b04883b05 | -6.5856 | -44.564 | 2025-08-09 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 856a2f8c-2b10-38cd-8ef4-ba295946bbe5 | -13.0778 | -43.83 | 2025-08-09 01:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| ffd4d41a-9041-33cb-b12a-13217d050ec5 | -13.5523 | -55.2428 | 2025-08-09 01:40:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d401a367-7d5e-3521-a5b1-751903cce4c8 | -13.0584 | -43.8333 | 2025-08-09 01:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 400942ee-658d-3305-8fec-3710da99a311 | -13.039 | -43.8367 | 2025-08-09 01:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 01950fd6-1166-30f6-9615-bce36396e9ab | -13.058 | -43.8571 | 2025-08-09 01:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 082a6c90-4c08-3e9f-ba8b-c93b54acaf39 | -8.9399 | -60.7481 | 2025-08-09 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 4fd84832-f6a8-37dd-81d5-d5905d62d73d | -19.8328 | -47.0586 | 2025-08-09 01:40:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3efa1bf3-a571-3132-925d-e76db5d5211e | -13.039 | -43.8367 | 2025-08-09 01:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 578ab7ff-b9ec-39ad-87bd-59eb01ae279c | -13.0778 | -43.83 | 2025-08-09 01:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 9641eb45-abaa-3603-9854-c7180ceef800 | -13.0584 | -43.8333 | 2025-08-09 01:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ce82d2d4-e332-391d-8db5-c02bc733d27f | -8.9399 | -60.7481 | 2025-08-09 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| efca9a98-6856-3816-90b4-72297f571cd0 | -8.9213 | -60.7489 | 2025-08-09 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 2e0d7d39-995e-3c52-9f32-37403f9b997e | -13.058 | -43.8571 | 2025-08-09 01:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| c3d8f8c2-b176-335f-be03-f9c80d88db4e | -8.9215 | -60.7297 | 2025-08-09 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d847662c-9410-397b-82cb-d2f56bb4f504 | -7.4285 | -67.7404 | 2025-08-09 01:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 99dc5145-7125-3d04-8289-1c06a12a06b0 | -19.8124 | -47.0634 | 2025-08-09 01:50:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b65a5eb5-9719-348b-82a6-ca45b7f145dc | -13.0386 | -43.8604 | 2025-08-09 01:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 8d7ce6c8-cb61-3314-a185-48de126bb127 | -19.8328 | -47.0586 | 2025-08-09 01:50:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 19f1e08f-dcaa-3c55-9ae9-5e965fe5053c | -6.0686 | -43.7539 | 2025-08-09 01:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 3c71b888-972e-38b8-bda6-da256f71da4a | -8.9401 | -60.7288 | 2025-08-09 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 09f5ebaf-a885-3171-bc7c-a7d0907c6ce9 | -6.5856 | -44.564 | 2025-08-09 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 26f6b403-9e3a-3561-a8b0-5caaa51c9590 | -7.4469 | -67.7401 | 2025-08-09 01:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f391efea-6059-3c53-b6ce-cf6d0169d6d0 | -6.0498 | -43.7554 | 2025-08-09 02:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| b9d9a1cc-2ce9-36f1-9691-d016de526fe1 | -8.9399 | -60.7481 | 2025-08-09 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 0d2af26b-5190-3f5c-91bf-69608d0f8d67 | -19.8328 | -47.0586 | 2025-08-09 02:00:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| e91a41f2-687e-3cb6-acf6-6daf92e07f15 | -13.058 | -43.8571 | 2025-08-09 02:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a6ae91a3-66b7-38df-bdef-a4887d0cba20 | -15.5492 | -50.1435 | 2025-08-09 02:00:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |
| c6e056e9-a5f0-3f09-8c29-ba2b8ead7a3e | -6.5856 | -44.564 | 2025-08-09 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 52c14f5f-4ae9-35bf-9da5-89499bb9f2c0 | -8.9213 | -60.7489 | 2025-08-09 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 398b3ce2-21c8-3ded-807d-796de69a4db1 | -9.0746 | -40.4672 | 2025-08-09 02:00:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 98a7c46b-01ce-32b7-b632-f52b2e4eea5d | -8.9401 | -60.7288 | 2025-08-09 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| ce9cab72-0325-3a82-93b2-f9cf960f7bcf | -13.0584 | -43.8333 | 2025-08-09 02:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 6b733250-8d2b-3abd-b6c5-9ab0a7945563 | -13.039 | -43.8367 | 2025-08-09 02:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 20194cd8-2ce5-3a26-bc4e-fc297e02bfd5 | -13.0386 | -43.8604 | 2025-08-09 02:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 56b18ba7-0085-38b2-9f6b-b73f5ad139d0 | -19.8124 | -47.0634 | 2025-08-09 02:00:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 10d4cf0d-fd37-360b-b288-edf825746ccd | -8.9215 | -60.7297 | 2025-08-09 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a2b29f2e-2199-322d-8f85-64b459aaed9b | -13.039 | -43.8367 | 2025-08-09 02:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 0576e70f-2c7b-3fbf-9d1f-3801085b2a38 | -19.8328 | -47.0586 | 2025-08-09 02:10:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 655a291d-a69a-3701-94de-5feb09bfb3de | -7.0801 | -59.1578 | 2025-08-09 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 307.9 |
| f917212f-5e8f-3b22-bafd-58dd344b72b7 | -7.0615 | -59.1779 | 2025-08-09 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 50c633b0-b4b9-3850-9337-ef2b18dc6a2f | -7.0984 | -59.1763 | 2025-08-09 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 68a9e653-3f3f-35f4-a16b-2c6b0cc48a98 | -13.0584 | -43.8333 | 2025-08-09 02:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 114e35ff-a3e0-3869-b641-bb3eb23537f4 | -8.9213 | -60.7489 | 2025-08-09 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 4f2ff3aa-bed3-3d8d-b8a7-fb7e743980e4 | -7.08 | -59.1771 | 2025-08-09 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 534.4 |
| e49e42dc-6f58-3803-96c3-4436ca08bf38 | -7.0616 | -59.1586 | 2025-08-09 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 54a6b729-47ac-345c-bbf3-51047e04ff6b | -6.5856 | -44.564 | 2025-08-09 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d0a185c7-97d0-3dd9-8e8d-4c03050314e3 | -19.8124 | -47.0634 | 2025-08-09 02:10:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| f0e24acf-11b1-3e59-955e-abecec2af244 | -7.0986 | -59.157 | 2025-08-09 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bbdf54f3-5bd1-3bc9-b05f-064e665f387d | -8.9399 | -60.7481 | 2025-08-09 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 5f58e52e-fdb9-3b3a-b341-0905b41517bf | -13.0584 | -43.8333 | 2025-08-09 02:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 0119a803-907b-3b91-88d1-6ac3b32bd233 | -19.8124 | -47.0634 | 2025-08-09 02:20:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 44799ed3-82ca-3dc1-9273-5a29c350cf30 | -6.8397 | -59.245 | 2025-08-09 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f5bdc21b-1665-36af-9049-301efac4bcee | -6.5856 | -44.564 | 2025-08-09 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 0f9c1381-877f-3070-b336-47a053f3b50e | -19.8328 | -47.0586 | 2025-08-09 02:20:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 1450b599-4180-3036-aa61-909bb1cb1872 | -13.058 | -43.8571 | 2025-08-09 02:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 8acb08a4-649a-3d57-a7a5-0e8aed291233 | -13.0584 | -43.8333 | 2025-08-09 02:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 117a9ecf-8fb4-35b0-9865-2328caeb3043 | -6.5856 | -44.564 | 2025-08-09 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5e10f64b-e0a1-31c3-ae7f-9ee17581c8c4 | -19.8328 | -47.0586 | 2025-08-09 02:30:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 81.2 |
| e75949a0-93ac-3aed-ab43-160778895aaf | -8.9399 | -60.7481 | 2025-08-09 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 9a46e527-36d6-3405-b966-b64f1756ada9 | -8.9401 | -60.7288 | 2025-08-09 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 6438abe0-b671-35d3-8868-a9776a19cf06 | -19.8124 | -47.0634 | 2025-08-09 02:30:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 112.0 |
| f5a0b4b9-ca19-3afd-8a4f-ebb930c988bc | -8.9215 | -60.7297 | 2025-08-09 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 31f4a51b-99e6-33ba-8ecd-c5b0331bcce1 | -8.9213 | -60.7489 | 2025-08-09 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 87123a3d-a767-3380-af4f-b5d71ac78519 | -19.8328 | -47.0586 | 2025-08-09 02:40:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 66.2 |
| ae43f0e5-c171-3ebb-b1d3-3b7851edab49 | -8.9215 | -60.7297 | 2025-08-09 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6e9165df-557e-31be-8f53-40c6003364bd | -8.9213 | -60.7489 | 2025-08-09 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 97080f16-6615-3837-8d4e-5022e8307ff8 | -8.9401 | -60.7288 | 2025-08-09 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c6de2800-4579-3e86-a593-d35abb2dcbe5 | -19.8124 | -47.0634 | 2025-08-09 02:40:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 5bec0348-0973-31e2-8d48-09e461827a37 | -6.5856 | -44.564 | 2025-08-09 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 8e0d3311-d38b-308a-b9cb-45650e824f81 | -8.9399 | -60.7481 | 2025-08-09 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 717e63b2-ed6f-3b86-a6d6-18a9441ca0f0 | -13.0584 | -43.8333 | 2025-08-09 02:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 52bfbe0e-b47b-3258-8312-81330d10d3f9 | -8.9213 | -60.7489 | 2025-08-09 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 916d9de5-4667-31db-aa9b-1623a286c632 | -13.5521 | -55.2633 | 2025-08-09 02:50:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 07750472-06a5-3302-9f13-659b0e7ba470 | -8.9215 | -60.7297 | 2025-08-09 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| cf6e3735-dece-3936-8046-16922f27e42e | -8.9399 | -60.7481 | 2025-08-09 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| af1f4176-da9b-32e9-abe9-39c4f6d93a95 | -19.8328 | -47.0586 | 2025-08-09 02:50:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 25ca67ad-64f1-3fbe-a250-f87ead0de078 | -13.0584 | -43.8333 | 2025-08-09 02:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |


[Clique aqui para ver as próximas entradas](README8.md)
