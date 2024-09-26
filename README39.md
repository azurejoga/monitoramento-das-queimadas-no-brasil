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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cecc286-c4dc-3b37-ae2e-03e45a1d2e0f | -11.2561 | -65.281998 | 2024-09-26 01:49:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 98cd9583-dfe9-33b3-b7ee-6101bcd672b6 | -11.2578 | -65.289597 | 2024-09-26 01:49:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bd09361a-902c-3abd-9861-d8c2d09a6467 | -11.2595 | -65.297203 | 2024-09-26 01:49:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ebc8a7f5-5385-3201-a587-8ff1916384dd | -8.7174 | -54.791401 | 2024-09-26 01:49:48 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 018f5d58-3ac3-3fcd-bb2d-730b36c994e5 | -9.3081 | -57.138302 | 2024-09-26 01:49:48 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59832050-7396-3269-b6bb-d3a2b24c607e | -8.7028 | -54.774899 | 2024-09-26 01:49:48 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f5c2e38-6492-3789-96ab-2c6a9b6d8df0 | -8.7077 | -54.7939 | 2024-09-26 01:49:48 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9db7bd9f-c056-3a9d-b6f6-a092ab6ecbdd | -9.2984 | -57.140701 | 2024-09-26 01:49:48 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60374375-f76b-3bb3-80d3-2fdfdf2f4c3a | -10.0368 | -60.4403 | 2024-09-26 01:49:49 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3bf08d1-b5d7-3398-abe6-c2adb050497b | -9.8672 | -59.858101 | 2024-09-26 01:49:49 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0147e42-f374-30c4-a1f3-a95dcea5c3fb | -8.5275 | -54.571602 | 2024-09-26 01:49:50 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd53ee96-fefd-333b-827a-a5ae53dd19e7 | -8.5172 | -55.177601 | 2024-09-26 01:49:52 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4e2d0a-2014-3879-b473-0eb8cb67d68b | -8.5218 | -55.195599 | 2024-09-26 01:49:52 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71d661d7-334c-3295-a5d8-d33ded670a3b | -8.9357 | -57.134499 | 2024-09-26 01:49:54 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a4a4f9-7ec0-34c0-9928-86633dc57b9b | -8.9389 | -57.147598 | 2024-09-26 01:49:54 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7496a64-ee03-35e8-8b9d-4a352c9def8e | -9.5754 | -59.760899 | 2024-09-26 01:49:54 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 158a700f-3e99-399a-805a-721eef0f359b | -9.5775 | -59.769798 | 2024-09-26 01:49:54 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 084673ba-c140-3212-b281-bd5d2bee1484 | -9.5796 | -59.778599 | 2024-09-26 01:49:54 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3532e7e9-0565-3040-8702-651b7b05a581 | -9.5656 | -59.763199 | 2024-09-26 01:49:54 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3be46b6-42d5-3195-92ad-4cc39e4ba7bf | -9.5677 | -59.772099 | 2024-09-26 01:49:54 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0f67fd-6f8b-3ce5-b196-5471c24b48ad | -9.5698 | -59.780998 | 2024-09-26 01:49:54 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee82e044-00f6-3c1c-b62c-b6c1b78f5534 | -9.558 | -59.774502 | 2024-09-26 01:49:54 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d08bb7da-9cc4-307a-a93d-77140a9e30f9 | -9.5601 | -59.783401 | 2024-09-26 01:49:54 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c503ac7-1fa6-3f01-b138-fa5eacb6165c | -10.2841 | -62.875702 | 2024-09-26 01:49:54 | METOP-C | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 924089d5-5995-3041-8e66-6d5bd3e1433e | -10.2857 | -62.882599 | 2024-09-26 01:49:54 | METOP-C | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5d2163d9-e6f5-3dab-8222-4c45d0524b31 | -8.326 | -54.9921 | 2024-09-26 01:49:55 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c86aa56f-14c0-36c8-bf90-8f3f55a6871b | -8.3115 | -54.9758 | 2024-09-26 01:49:55 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5322c5cb-673e-3bcf-896d-e65bd7b17de6 | -8.3163 | -54.994499 | 2024-09-26 01:49:55 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b772ff8-ee92-3e5f-b8a3-b6b586f3dbd1 | -8.321 | -55.013199 | 2024-09-26 01:49:55 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4df566e-01fb-39f2-bc5d-2d2311566d2a | -9.3902 | -59.634701 | 2024-09-26 01:49:56 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd9fdff3-79c0-3a60-a8cb-93eee1e1c235 | -9.415 | -60.300598 | 2024-09-26 01:49:58 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12a162df-6144-3461-9046-88cb2790dde6 | -9.3914 | -60.288601 | 2024-09-26 01:49:59 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc23abd-4831-31da-be4a-847020c64a6e | -9.3934 | -60.296902 | 2024-09-26 01:49:59 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1f6254-6149-3615-98a9-ea42f01433af | -9.3954 | -60.305302 | 2024-09-26 01:49:59 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f48b7fb-9f91-38b1-8607-0d9ba27ca32a | -9.3836 | -60.299198 | 2024-09-26 01:49:59 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d662074-7451-3c2b-89d6-e01d33eca6df | -9.3856 | -60.307598 | 2024-09-26 01:49:59 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86f3daa7-5f57-3a48-9ffa-ce8a768cc4ff | -8.8192 | -58.2136 | 2024-09-26 01:50:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d67d59d-a232-3c9a-b967-de4bfef0e59e | -8.8067 | -58.2048 | 2024-09-26 01:50:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e446416-f16d-36b2-8641-baec17319a8e | -8.8094 | -58.216 | 2024-09-26 01:50:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e49cd733-da65-3c4f-bfc9-027c297a5be8 | -8.8121 | -58.2272 | 2024-09-26 01:50:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7afbcc1e-371e-365f-93ef-336056c07ebe | -7.8223 | -54.7099 | 2024-09-26 01:50:02 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82c0fb72-3fc1-3f7c-b332-14e5957d7168 | -7.8273 | -54.729698 | 2024-09-26 01:50:02 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cb22d9e-b15c-3748-9e16-64107cb2190b | -7.8126 | -54.712299 | 2024-09-26 01:50:02 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a98cfaf-2f3f-39bc-90c4-1a541d3a1436 | -7.8176 | -54.732101 | 2024-09-26 01:50:02 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 250ff73f-b342-3db9-b39c-cdf91cf03c5a | -7.8227 | -54.751999 | 2024-09-26 01:50:02 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5e67ccb-319b-3d16-afbb-f8d3b22054a5 | -7.803 | -54.714802 | 2024-09-26 01:50:02 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc61c0f6-fc35-3beb-aa15-b0cad61c3e6e | -7.808 | -54.7346 | 2024-09-26 01:50:02 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce1723b2-04ab-3e8c-8f0a-0a7bd5d98717 | -9.2252 | -60.676102 | 2024-09-26 01:50:03 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb265ba7-4077-3fa7-bf11-7ca510acbb6b | -9.0515 | -60.422501 | 2024-09-26 01:50:05 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 037ade6c-7114-3f9c-8568-cf65f3cc565b | -9.0534 | -60.430801 | 2024-09-26 01:50:05 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 301e298a-6a5b-3360-b84e-9e8022aa1bc2 | -9.0554 | -60.439098 | 2024-09-26 01:50:05 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27f7f6c6-9e36-309f-9f1e-2915330911b2 | -9.0417 | -60.424801 | 2024-09-26 01:50:05 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78c8a1c3-00c8-3223-8a3c-01abe311999f | -9.0437 | -60.433201 | 2024-09-26 01:50:05 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b253f514-94fd-3206-980d-fca6177b4eaa | -9.0457 | -60.441502 | 2024-09-26 01:50:05 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84c0fb3d-6287-38ae-973d-51bd5dfe5b2e | -9.2103 | -61.138802 | 2024-09-26 01:50:05 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e212a64-e97c-30b4-a122-8038def1f9c1 | -9.2122 | -61.146599 | 2024-09-26 01:50:05 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fb5af2c-e7c4-35b1-86ea-d987a7d2b14d | -9.9495 | -64.767197 | 2024-09-26 01:50:06 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b86ac3da-132a-3c19-9872-0003eed308fb | -9.01 | -60.7271 | 2024-09-26 01:50:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7634b4-bff8-3cf6-972c-910a2066115e | -9.0119 | -60.7351 | 2024-09-26 01:50:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3864a3a6-99c0-3e0f-a2a8-6ab5439b7b02 | -9.1016 | -61.115299 | 2024-09-26 01:50:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 845fbe25-6bec-3c83-8bea-a7f69aaeb3c5 | -9.1034 | -61.1231 | 2024-09-26 01:50:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8eba5bc1-53a6-338f-86e0-3ea9129ffb10 | -9.1052 | -61.130798 | 2024-09-26 01:50:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d03b7613-1b0f-373a-a80f-8ea77770b2bf | -9.9397 | -64.769402 | 2024-09-26 01:50:06 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca4182b-1a52-3fa8-9317-f84a91f86b05 | -9.0918 | -61.117599 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02965a1d-db94-3210-9bb3-812a9c18e5dc | -9.0936 | -61.125401 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8966647-2529-3def-8101-a5d24b04665d | -9.0955 | -61.133099 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c3e5fc3-fd88-3016-83b2-f8e7159cb4be | -9.082 | -61.1199 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f97f389-7f88-3d80-8219-7d9a7b2cc278 | -9.1165 | -61.266499 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63d8e913-2569-3f9e-9282-445022054a53 | -9.1049 | -61.2612 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d0d413d-0d06-336e-9cc1-c79866d5cce1 | -9.1067 | -61.268799 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae05c599-b8a2-3331-8976-cc00c244637a | -9.1085 | -61.276501 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b18c9cc-fc2f-366b-9870-4619d224b7c6 | -9.1157 | -61.307098 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8a1b9dc-cf1c-3aa2-95ae-08e2a7249bd5 | -9.1175 | -61.3148 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f31cb7a2-db03-3ae2-91d9-2350511009c7 | -9.1193 | -61.322399 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09dc28f0-17a7-3e51-b63f-b35a53dadf82 | -9.1211 | -61.330002 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed8653db-71f3-3a8f-b53a-618214caf3d7 | -9.1229 | -61.337601 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8680fed-65f9-36d1-a062-685f8fb08e21 | -9.1246 | -61.345299 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94b3b4da-f36a-3a32-a5ae-f7ea666bdf31 | -9.1264 | -61.352901 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d07bf99a-b15a-3716-ac70-a5cdcb14726e | -9.1282 | -61.3605 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23255bb4-f2e8-3309-91e3-e8b8dc0c40ab | -9.0951 | -61.2635 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2692b0d3-143c-399e-9f3e-02023fe67577 | -9.1059 | -61.309399 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f66d85e5-88ab-3145-a63a-a55ab72a0c32 | -9.1077 | -61.317101 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ab6a39a-fa1f-3e8a-8dfb-ae7dd1162bf3 | -9.1095 | -61.324699 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcd99071-5bf0-3d24-9ed8-a1d17ca63aef | -9.1113 | -61.332298 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb3d086a-83c9-311f-940d-7aae86930bf3 | -9.1131 | -61.339901 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37bb7ed4-22f6-396f-a17f-7b78c571181b | -9.1148 | -61.347599 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86620e61-896e-3f82-89dd-35bc8424b9a7 | -9.1166 | -61.355202 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9378af94-7690-3a0c-ac0d-f8edb1a55aaf | -9.0997 | -61.327 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea559b81-35f4-3b17-b441-03b11da94010 | -9.1015 | -61.334599 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6872acc0-92c7-36d2-a0c6-513014d90ba8 | -9.1033 | -61.342201 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd50343b-081c-3420-9901-58d8f0ebc90e | -9.105 | -61.349899 | 2024-09-26 01:50:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c84c8baf-0d38-3f64-814e-d32b9f7e954e | -7.5626 | -55.146099 | 2024-09-26 01:50:08 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 883e4c45-fe91-3b20-ae6b-da42fd735b4e | -7.5673 | -55.164799 | 2024-09-26 01:50:08 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 183a0187-6684-3826-8d30-1ed4c24eb9ed | -7.6137 | -55.349098 | 2024-09-26 01:50:08 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11c04513-fa80-367d-87f6-58c165d3d3aa | -9.0775 | -61.3643 | 2024-09-26 01:50:08 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f002718-ac32-36e4-93d0-1748d70d5553 | -9.0793 | -61.371899 | 2024-09-26 01:50:08 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d7bf497-ce28-3503-976b-145700edc35b | -9.0677 | -61.3666 | 2024-09-26 01:50:08 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71772043-be99-3347-9227-774fea8ec51c | -9.0695 | -61.374199 | 2024-09-26 01:50:08 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28a32238-10ae-38fb-8958-8a45d7c0c1c8 | -9.0713 | -61.381802 | 2024-09-26 01:50:08 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc3510e8-3060-342b-8a7a-020a84305f72 | -9.0597 | -61.376499 | 2024-09-26 01:50:08 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README40.md)
