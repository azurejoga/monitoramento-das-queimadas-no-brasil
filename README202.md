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

## Dados Diários - Página 202

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a272c8bf-4c4e-30df-a41f-e4cabc5b0c1c | -9.39699 | -68.30499 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5b06384-48d9-37cb-b6b7-f72cd07e2759 | -9.39726 | -68.25576 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73dcac60-45c8-396f-ba32-fffb7829d38b | -9.41856 | -67.23447 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4098e9f4-f310-3b09-8d8c-eceb2bf6b465 | -9.41858 | -67.6219 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cad5f08c-3228-39ba-81bb-e7cd98abae77 | -9.41916 | -67.6173 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4150b32f-35b3-3749-b6c6-403599715e32 | -9.42302 | -67.236 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1806267e-bd14-36cf-a8fe-5dfe4ff5e8e7 | -9.4236 | -67.23127 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a372514-c0c7-3f43-a107-f938c0de8246 | -9.42414 | -67.23994 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| acdc148d-8b3e-3d1f-8a20-c8fcaa3fffb5 | -9.42475 | -67.23521 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 49eba37a-e4a8-35a0-85e6-8b422e80504d | -9.4252 | -67.61805 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38988955-079c-3313-9024-8f9529e3ea64 | -9.42823 | -64.54404 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c08741c5-e380-3d66-a38b-d455d92d7a7f | -9.42921 | -67.23681 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db97188c-cc42-3196-af00-609d82f80b1a | -9.43404 | -64.54288 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81081799-4b8c-3cd7-b54d-ebeaeff85b82 | -9.43545 | -64.54531 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bb31b190-8187-3929-871b-75ef0c03ef31 | -9.43832 | -68.94994 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e55e9a6d-2825-39d4-ba9d-823cc684b97e | -9.43879 | -68.94626 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89d7d87f-bed1-31f4-8dcb-3a7923d5f8f9 | -9.4404 | -64.55116 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ba0ee331-4d2e-350e-8665-2d3d499a1cb9 | -9.44132 | -64.54368 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e90d7b81-9169-3cf2-9091-a8e0b72cb8f8 | -9.44274 | -64.54602 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0e42bf9d-c647-398c-933c-6930a74997a8 | -9.45781 | -68.52347 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 305bea3e-9738-38b3-b530-e758d5391b04 | -9.46107 | -68.54378 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de9d7fa4-6a10-3030-8589-c5ed24633fb3 | -9.46214 | -68.52424 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 423ae66e-0667-3b7b-82b4-5770bb284c9f | -9.46265 | -68.52035 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37e51cc9-a30c-3a81-aca5-4763584b04e9 | -9.46316 | -68.51648 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f13f5a4-8ce4-30a4-83cd-f80e2be2bf10 | -9.46368 | -68.51257 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb118017-6bef-3c34-b63c-baec41006e62 | -9.4635 | -68.5243 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af1b2b23-7a60-3c57-8a7d-0018c8dce28d | -9.46447 | -68.5165 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38cab3e7-2be2-3922-ac43-b58b5ad9dc30 | -9.46496 | -68.51258 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47c17ff6-5740-3d00-86e3-c6f37c7e3856 | -9.46677 | -68.54445 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a843ff59-c3b3-3967-a6c9-4f0d18a52374 | -9.46888 | -66.58582 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e96f592-4276-3cf8-a884-2a0aa038e0f3 | -9.46955 | -66.58048 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4da40732-6325-34b2-b7d6-5e5958711216 | -9.48858 | -68.55504 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7851573-86da-31cc-ad4e-dcb8abdcbcdd | -9.48906 | -68.55121 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9980e82c-2756-3e55-8bee-47d213422811 | -9.48979 | -68.4996 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d33ac115-650e-371a-b627-bf6d7b506509 | -9.49028 | -68.49569 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 218c13ee-981c-3382-becf-e21a37f122c4 | -9.49346 | -68.05808 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb00531a-6cae-3bc0-859d-4c0fb52fea68 | -9.49477 | -68.55185 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa120b7e-a295-38db-bddb-39151340eb8a | -9.49551 | -68.50029 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85d7bb57-cb06-3d91-ae6a-2c15b152c978 | -9.496 | -68.49635 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31ba050a-ffdd-3969-be09-918e923dac6e | -9.4965 | -68.49245 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0574ef7e-4931-39ab-bb48-e606153682be | -9.49933 | -68.05886 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 435889ab-a89e-3713-8535-c6089f273f92 | -9.49988 | -68.05462 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea16d7d4-99dc-326d-b2c4-4ccc8adf8eab | -9.50172 | -68.49706 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cd7f818-a095-30b1-b566-607c9f18fbdc | -9.50769 | -68.44997 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b73471c7-d4e2-38da-9d47-95fc4004a24a | -9.5082 | -68.44597 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8253143d-b03c-33c5-ba0b-0c0802bf0fe8 | -9.57916 | -68.58905 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9db4a16d-b128-3aee-b718-f2d28e34ecc2 | -9.58163 | -68.59519 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71025a31-1312-3c47-94f1-5b59a7904de5 | -9.58216 | -68.59122 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d596cb9-f389-3b78-bd0c-f5e69930f30a | -9.58384 | -68.59779 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a0836e6-f1ee-36b6-9bd6-756dde341607 | -9.58433 | -68.59383 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd15a359-4e82-3a57-892a-5f885a9496d0 | -9.58483 | -68.58987 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eba64d19-9498-314a-8d1e-231c93cde5f7 | -9.62386 | -67.47236 | 2024-10-03 06:31:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60901619-5dfe-37ef-a600-58226b629468 | -9.62398 | -67.47374 | 2024-10-03 06:31:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a953e951-fdb8-3199-9373-e29a9ed9f74f | -9.62995 | -67.47328 | 2024-10-03 06:31:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86a52582-a043-34c0-bd40-8eba662f4916 | -9.63052 | -67.46867 | 2024-10-03 06:31:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 002636d6-9a34-337b-89a8-1c1772ef3684 | -9.6351 | -68.64787 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e752e42-3a78-347a-b3e6-b9130f69ce3b | -9.6356 | -68.64401 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 905ac813-2193-3626-a10f-4e89f8a5df0a | -9.63659 | -68.63641 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 563b8f09-0c65-306c-9f8a-d70ec846f914 | -9.66481 | -69.05872 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 161c737f-00eb-3a77-9844-69813b6cad2a | -9.66986 | -69.06307 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82076104-d4c9-3f05-9c3e-65db4264c452 | -9.67033 | -69.05939 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34547ba5-5c5b-3f20-8581-bf7a0c496952 | -9.67426 | -64.72687 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9510700-7ed0-3fe3-b52b-3d16fc09b1bd | -9.68146 | -64.72778 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68d2e78d-b606-3c7c-a445-fb77978b254c | -9.68228 | -64.72092 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4221a7d0-722d-334a-8168-5fdaa7d2cc6f | -9.70842 | -69.06843 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f90af4ab-6af7-3ff5-83ea-b13bfd02de0a | -9.70843 | -69.06759 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57872a7c-e26c-3bd7-830d-a44821e934c5 | -9.70888 | -69.06402 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed254fa7-dfbb-330c-a14d-a86cc9f0d985 | -9.7089 | -69.06487 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e4fe55e-d6fb-3787-8754-7608fcd0ae0a | -9.72822 | -68.38177 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab49431f-3ba3-3782-a101-20a014e42025 | -9.73316 | -68.43542 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13121c3b-c84f-3046-a167-717768c087ad | -9.73891 | -68.43621 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c27ba8b9-b9e8-382a-aefc-7b5627ff41cc | -9.73992 | -68.42819 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03ed3976-6dc2-38e6-b671-6c7fbcc04ec8 | -9.74044 | -68.42415 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5f6fc03-f605-3ac9-8194-4507ac1b313c | -9.7462 | -68.4249 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f79df608-7ed5-3d04-83fc-bd36bb313fe3 | -9.74671 | -68.42084 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae2e78a7-ff25-350c-b0e4-eb4881ce900f | -9.80901 | -64.95616 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcabd34d-59f4-3227-ad44-0984b589cf09 | -9.81299 | -64.9549 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a64acc2-4595-30a4-9e6b-720247cd3bce | -9.81612 | -64.9572 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05408f8d-24ee-35c5-a6a0-108ee5b08eb9 | -9.82009 | -64.95603 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca6ccca2-d008-3b6c-badf-9bdbaaa23a60 | -9.85208 | -64.86789 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ff77d45-d73d-362e-a4e8-39a2ed50f7cd | -10.45315 | -69.18334 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91680c3d-fd46-3a1b-9ac4-d6623dc4512c | -10.45398 | -69.18468 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a621cb36-d45c-35b1-9f9e-625a5ef1cc5c | -10.45446 | -69.18105 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c344c218-693b-3e67-811a-1d8bfda48cbb | -10.49681 | -69.45403 | 2024-10-03 06:33:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81d624b8-7893-3a9c-aea2-96974e2a435e | -10.50225 | -69.45467 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8efe75ec-7f5a-3a69-9845-17e137260274 | -10.50315 | -68.67464 | 2024-10-03 06:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 593fc0fd-b9f8-386f-8d41-805b4b6d1baf | -10.50365 | -68.67074 | 2024-10-03 06:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6241c2cc-3e26-393a-9b41-e3a2eb51416b | -10.50382 | -68.67672 | 2024-10-03 06:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 49f1709c-11a3-3280-acca-28a879f9243a | -10.50429 | -68.6728 | 2024-10-03 06:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 082ca615-1c2f-3ef1-9ffb-e5eb71c60b62 | -10.50888 | -68.67527 | 2024-10-03 06:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5ceb53e-4fc6-36eb-9000-d5b9a7533cea | -10.51947 | -69.23598 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0f3cf518-b092-3ec6-b84f-191797dac776 | -10.53601 | -69.32876 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f589f53-01cf-3be4-b82c-c1921078142e | -10.54029 | -69.33374 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98c83d00-cd44-3bf8-85cd-b9776c58a2e6 | -10.54075 | -69.3302 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d2502b8-f158-30b5-a095-c4fcdf828c7a | -10.54106 | -69.33291 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81d6c586-2e45-339b-a01b-db094e3154fd | -10.54123 | -69.32658 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 049041db-c4cd-31d6-a848-02d3ef81e0ac | -10.54151 | -69.32934 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b31fd1-f839-3e6b-96a9-7fa2644ebb7b | -10.54295 | -69.09754 | 2024-10-03 06:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ff0519d-807f-38eb-ab3d-ba9fe706a07a | -10.54762 | -69.23469 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d4f409e-69cf-342c-94b4-c1fd226458f6 | -10.54806 | -69.23112 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README203.md)
