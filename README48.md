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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d289ca1a-a0ee-383d-afe2-bae57e56a0a5 | -3.69736 | -50.15512 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4655bd46-faff-303e-a1c0-b0005d4be73a | -3.69191 | -50.59342 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce0ddeaf-f196-3c05-9bad-6dbb563abf3d | -3.69126 | -50.59134 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9382374c-41eb-308f-8297-1900083dc631 | -3.69096 | -50.59907 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b9dc6f2-50d6-3693-8637-1d55c7e12121 | -3.69034 | -50.59706 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc33893a-c8c6-3182-8d68-b6d6418835b5 | -3.66242 | -50.12771 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0b48224-9b4e-32b3-864c-36949bec4b70 | -3.6242 | -50.18497 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f4dfafe-d213-34b5-8323-7363503ee12c | -3.62278 | -50.18628 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07aa8e91-8378-3d7f-b14d-cd40cb672478 | -3.61938 | -50.18412 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aad2acaf-a07b-3ae7-ab07-6b638707987c | -4.93583 | -49.86005 | 2024-11-02 04:12:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4935fabb-99d2-355d-9dce-5b3f420d3452 | -4.80487 | -49.48744 | 2024-11-02 04:12:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd4d35cf-f127-37a6-b66c-63a5536ef117 | -4.80037 | -49.48661 | 2024-11-02 04:12:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bba62571-cd13-3026-9cdc-29e05c009e18 | -4.75324 | -49.79985 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c42abe7-53bf-30d8-8441-956176448319 | -4.70999 | -49.60843 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f7064504-36ef-370d-8838-e6aaf58ed823 | -4.70967 | -49.60671 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a3afdca5-81bb-3169-b01a-af776f2998ae | -4.70893 | -49.61131 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 95ec9de7-608a-3527-8232-b1fccf907398 | -4.70544 | -49.60765 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ae6c6b0a-7c0d-33a7-a397-382a7c1a63ba | -4.70512 | -49.60593 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68c6dc3c-1c3b-3194-86ab-4a465a9e54c9 | -4.67565 | -49.52952 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7f61631-9832-39c5-95d9-440528d60975 | -4.49018 | -50.34672 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32054cdc-4b6d-37f0-9bd4-8e64b6f4ffb1 | -4.48305 | -50.12614 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14a03c6c-acee-30a5-b669-922fa2df8114 | -4.38381 | -49.4163 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 533035a2-178a-3499-a640-93730f70326b | -4.37923 | -49.67433 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82e2a398-5313-3966-9ba2-c5359ef1a960 | -4.37845 | -49.67916 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f32fb250-87cf-3aa1-9952-759eafa59108 | -4.0614 | -49.2618 | 2024-11-02 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a58b4d0c-e552-3176-aa9d-5efe51cdabc8 | -3.8933 | -50.24639 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a41e7c0f-15ca-31cd-af12-b5a137e1b701 | -3.69823 | -50.14988 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4d7c5995-ff78-3066-9302-c70c60cde4ef | -3.69341 | -50.14913 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c5cee78-d122-3f9d-93dd-cbfb1748cd51 | -3.69255 | -50.15432 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 74b15f4c-4a34-3950-b2dc-73d0144907ab | -3.62759 | -50.18715 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e369949-4da6-3bc8-bbf1-85bcfceaae75 | -3.62334 | -50.19028 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d6a4d6d2-e5a5-3a7f-a831-46211c17350c | -3.62188 | -50.19155 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5732381e-5ca8-3558-9290-22d0e8f0bb44 | -3.61852 | -50.1894 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d43feee-030e-3653-9504-7598c72ca599 | -4.38307 | -49.4208 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 135a838b-1419-3a48-b259-fdf4ab700c3d | -4.37818 | -49.67625 | 2024-11-02 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3fa1070a-3303-3d35-b6f4-fe270a06413d | -4.14839 | -50.75069 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 045ae766-d3d0-3b98-8375-df94735471b0 | -4.14341 | -50.74985 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1f9208d-e844-3773-bd20-ec7764a96758 | -4.09671 | -50.75365 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e825ce60-4022-34b8-8b33-857781d9a95a | -4.09575 | -50.75929 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e0c62560-08a6-3791-8cab-b1293dada9d1 | -4.0956 | -50.75745 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b50dd8f-5b71-339a-9ba9-dae68f02bd8a | -4.09173 | -50.75278 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71656958-ef84-31b8-a7f0-b0486a69b24a | -4.09062 | -50.7566 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3330449b-79bb-3d89-b90a-51bd232fb198 | -3.66366 | -50.76027 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49378ffe-109e-3ffe-af60-480d96a1546a | -3.63302 | -50.79206 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f0fba92-4844-33e2-990e-2abfb0074a77 | -3.628 | -50.79117 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ea86671-9b60-30c8-aa2d-29ff4e598309 | -3.59257 | -50.75542 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f71ceb43-a3f6-316c-8863-ca1dc5956670 | -3.5921 | -50.75828 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9120310b-6118-3e1e-85bf-5cc67dbb9cad | -3.59162 | -50.76115 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8479c8d8-c2ea-3318-b86d-6a3b589ebafc | -3.06959 | -50.98884 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a76ae163-6f8a-3930-b0e3-257bfd6f3af9 | -3.06784 | -50.98793 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe5eef22-3d51-3912-9a4d-34ec3862eaa3 | -3.06735 | -50.991 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef539db2-c769-3e7b-b58e-9a398464005b | -2.95849 | -51.06363 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75ff4d5e-0f93-3d95-a03d-22b881e07c03 | -2.95543 | -51.05816 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 560f297c-3bdd-3204-848b-3bfc130b8341 | -2.95491 | -51.06122 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b7c09172-ca82-35ab-ab8d-5c42dfa31c41 | -2.95439 | -51.06433 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38a739c7-a585-3992-bce8-5fe1fa41a0b8 | -2.9543 | -51.05659 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8e8036c5-2800-3dd4-8a95-bb2e73e8d117 | -2.95381 | -51.05966 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 348aebb2-c6fc-3e4f-94dc-c3eca7ae0ede | -2.95331 | -51.06274 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3bc8798d-a158-37f6-bc52-6d2a740c2017 | -2.95078 | -51.0542 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf5c16ba-82b0-3260-8d82-7a9583e51504 | -2.95025 | -51.0573 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f8756c9-4d29-361f-8cf4-9ad748c07fd2 | -2.94973 | -51.06038 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eafe84c1-6fcd-39db-b5ca-0f4a81049b19 | -2.94913 | -51.05568 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 056a9611-5809-3c6e-9c5e-fa5a7573d30b | -2.94863 | -51.05878 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb9b3b10-d1cd-3717-9158-317a0c2e6cef | -2.94812 | -51.06189 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5efb08d6-762f-3c2e-929d-f55551e7a5d6 | -2.85784 | -51.28567 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ebcb94d-3880-3323-95ca-01742fad64e4 | -2.85731 | -51.28892 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 280cc6e9-b38c-3d2f-99d4-88f03d991563 | -2.85203 | -51.28807 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 458d92d0-58ec-37f4-9e9d-55b6ff7d712c | -3.17747 | -50.59477 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9fb78ff-fc10-3085-a326-e70b09e2b4e3 | -3.17199 | -50.59682 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b08e045e-274e-3779-b2dd-8357b44b54b3 | -3.49958 | -51.18517 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 50f6b302-f6f1-388c-b119-00e313bcf9b3 | -3.29773 | -51.19887 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f7d1bc1-7422-3d2a-964e-e03a27fefd94 | -3.29721 | -51.20197 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7130f4c8-e365-3b96-8c55-2ce8d98b6214 | -3.29669 | -51.2051 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33620bc3-8801-38a1-a2d6-3d911d647d63 | -3.292 | -51.20113 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d787b954-cffe-36a4-b161-33ff71cfe916 | -3.29148 | -51.20424 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef371cd1-a41d-37c9-aa82-330878f5ae3c | -3.28806 | -50.89351 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e9ae74d-66ac-3379-9221-b82d3d5c7160 | -3.28758 | -50.89648 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd20316e-125b-38bf-8b81-14fbd68a76ae | -3.28513 | -50.91145 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fee99eb9-840a-35ab-9404-87a6f1b3f861 | -3.28464 | -50.91446 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c4486a1-87eb-3c2b-aa59-ede93b49051f | -3.28415 | -50.91747 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0349afcc-250c-3663-a627-75e7cfec4ab1 | -3.27953 | -50.91365 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3313578c-f00f-3613-87bb-e5f1d1e92361 | -3.26516 | -50.77901 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cebc0969-6059-39a4-b76f-4d4e4ee010ea | -3.20554 | -51.17019 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 859f295a-4a1a-35be-9818-cdef6b56a934 | -3.20036 | -51.16921 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18c692eb-5f41-33ae-b7d0-a873d6cb57c8 | -3.19983 | -51.17239 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4bc58ed-8dda-33d3-90ed-4aa0eb58adc4 | -3.17772 | -51.08175 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f10adef-fd79-3ea4-a2ce-cb9d8fbd0e68 | -3.17719 | -51.08488 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c01368e-b82c-3230-af89-f6527f764d27 | -3.17412 | -51.07157 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 262b65df-afab-3cbb-a5cc-23511b6b3a19 | -3.17359 | -51.0747 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ca96f06e-bb7a-3428-81bb-3ae58eacd96e | -3.17306 | -51.07783 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a71ad102-1dab-347e-8c64-da82f06904cd | -3.17254 | -51.08095 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 84f15f1d-7fa6-3a80-914b-b8c1867d824b | -3.17224 | -51.07302 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d74964d-1b14-31cf-9f7c-12ac05783460 | -3.17201 | -51.08406 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 822f8cb0-05cd-3cb5-a95e-0a19423a0988 | -3.17148 | -51.08717 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0afdf350-228e-3265-849f-c13055e5fc40 | -3.17122 | -51.07929 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 17c51e55-52f6-3405-8c95-129ed5d3b9eb | -3.17072 | -51.0824 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b15151d-c216-3bca-a2c3-539f66c21996 | -3.17022 | -51.08551 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f5570ca5-99d9-370a-889a-6382262d2ce7 | -3.16842 | -51.07387 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 65878798-0918-3453-8478-301caedc1e94 | -3.1679 | -51.07697 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7939bcd4-5624-3da2-82ee-a44b1572df7d | -3.16737 | -51.08006 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README49.md)
