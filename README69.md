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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50efc1d5-512c-347b-8f07-1bc5f8111752 | -3.16366 | -50.44222 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fd1408dc-ad68-37b2-9801-2ece2ffe7410 | -3.16325 | -50.34985 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5fcc8180-29c6-30bd-bc42-266d78321abd | -3.16262 | -50.35395 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f6a0bb37-c3dd-3cca-b17a-89585eaccbab | -3.16198 | -50.35807 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69a7ec2e-95cf-3493-978e-6d8b3d712fff | -3.16135 | -50.36219 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1180e44f-b743-3f70-951c-654c8cd0dc86 | -3.16072 | -50.43753 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bba88a30-087b-33ab-a3f9-0766d45b1026 | -3.16029 | -50.34521 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c9ce8d8-db5f-3a89-8298-f51db2d139a2 | -3.16008 | -50.44168 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af146d3d-148f-3ad5-9899-4fed46d1191b | -3.15965 | -50.34932 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ea712baf-e47c-3aaf-bf0c-69cd9b16b864 | -3.15902 | -50.35344 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3fde4ef5-7169-379a-b24b-1b3bce845719 | -3.15839 | -50.35753 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e452b1a2-93d7-34a3-9f03-02035cbab698 | -3.15776 | -50.36163 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c33c1c3f-a28c-3360-b460-e6ba5df8b598 | -3.15714 | -50.437 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9358b187-b789-378e-8555-a85dae07d261 | -3.15712 | -50.36577 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04fd658a-3b65-3407-af09-deba49cdd0dd | -3.1565 | -50.44115 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 188a59c2-f14b-3412-a096-aa601cdef930 | -3.15648 | -50.36992 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ce7a78cd-6254-3b77-bb3e-c6916b698e0b | -3.15606 | -50.34879 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 40cbb31e-90f2-3371-8ca0-ae46bbac1679 | -3.15585 | -50.37404 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3c5f8c65-6ec8-30bb-a9bb-1248b6ff3913 | -3.15542 | -50.35291 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 655facf4-0b2e-3324-8ee3-fc38ee395dfb | -3.15479 | -50.357 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8573bb71-d250-3647-a921-9e4249f3b77e | -3.15417 | -50.36108 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 652528bd-bb7e-3337-ab8b-d104f318f263 | -3.15356 | -50.43645 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e90f886f-5458-3ec2-a578-f40f5dba01ab | -3.15353 | -50.36522 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 139aa0ae-99bb-3661-b9e1-6e7a2ce5a8e9 | -3.15292 | -50.44061 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 896da95a-d42a-3ed8-8f89-705514200699 | -3.1529 | -50.36935 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 64bf8ef7-a258-39da-ad00-fd903844f856 | -3.15229 | -50.44473 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8a898d2-4d5e-3b1c-a114-a8468813ec8f | -3.15226 | -50.37347 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f3ae0ecc-2f87-334f-9650-b7ee6c1e0cab | -3.15183 | -50.35236 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6e378a1-6ea4-3a64-aa30-e5f563ff11c4 | -3.15163 | -50.37758 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4cbfe2d0-6526-3687-9e34-24f2483be9bb | -3.1512 | -50.35646 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8e388100-6802-3346-a155-8a12540d4801 | -3.15057 | -50.36056 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 41697a32-046d-3b51-b862-48b050d8ac0b | -3.14994 | -50.36466 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c34fa76-e7ba-3ee3-8427-8f5827be099d | -3.14935 | -50.44007 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acb74454-0723-3c33-84cc-6e4b53a6804b | -3.14931 | -50.36877 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8a11ba7-c2bb-33f9-bfd2-313b14fbb78f | -3.14868 | -50.37288 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36b44c00-ffb5-34af-a8b1-e99305045662 | -3.14805 | -50.37701 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 935cb43f-12d6-3b02-8ff8-a59eedb37a94 | -3.14635 | -50.36412 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58e1c70a-9bc5-31ee-8ac8-95a6351463ed | -3.14572 | -50.36822 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 910c90c7-e504-3065-8bbf-f047e266ab8e | -3.14514 | -50.44361 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f1953ff-1a09-3e83-9011-9ca41c8da1e7 | -3.1451 | -50.37231 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e359438-a0d4-3e0a-965b-633f70fd5048 | -3.14446 | -50.37643 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0e77bda-676e-3c6a-947e-7d3df6440c31 | -3.13693 | -50.42556 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b405b882-0857-3d4c-8b2a-8324fa04eeae | -3.06548 | -50.49113 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fad0a195-7faa-3a21-9f60-1c2465d18d64 | -2.59515 | -49.80516 | 2024-10-12 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8dbd3f2f-85a9-3a92-bc19-ca5b88c3bc63 | -2.57907 | -48.94661 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55b93971-1b66-313f-85c8-8a6146b8656e | -2.57488 | -49.07807 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e2ca165-2228-3ff8-bfcb-c5e57bd33f93 | -2.47545 | -50.24747 | 2024-10-12 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d01b6ef-8638-3b02-b2e4-9e7696d4c465 | -2.47249 | -50.24281 | 2024-10-12 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdf9b106-91a8-3dee-a354-ae452f970d59 | -2.42888 | -48.94851 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| baf66ec4-c23b-3eaa-999c-8c677ff82aba | -2.27792 | -49.94037 | 2024-10-12 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 548582bd-4e39-337d-8f02-009b14fdb1b2 | -4.28027 | -50.2737 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72514a54-2aed-3686-b6be-3839084e1f0d | -4.26369 | -50.60973 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6702b206-792f-3c01-972b-6234c526db9f | -4.22463 | -50.65918 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16b37f38-3c9f-309a-8d2d-b5cad46c8d07 | -4.2133 | -49.7505 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c718a48c-7bd6-365b-90eb-e6f0c778ee44 | -4.20954 | -49.74994 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| da7d5222-852c-3bfa-b8b8-2cb8f342cbd2 | -4.18355 | -50.64029 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1d926dd-5d6a-3f5f-b65b-acad562db15c | -4.18292 | -50.6444 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 805252bb-2d76-3c85-9a08-577fbba51200 | -4.16787 | -49.77152 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d7b41bb6-ea12-3cf9-87fe-67a5bb88ce21 | -4.16663 | -49.77375 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| a94dc742-e5d1-3762-a438-ef1f87961787 | -4.03363 | -50.46407 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c55fbc1-30fb-380a-9939-1056f81e3e85 | -4.02028 | -49.5655 | 2024-10-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79f85cb3-8399-363b-a524-16058b324407 | -3.94412 | -49.84282 | 2024-10-12 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e305debe-b37b-3285-862a-9d27eb9833d9 | -3.94411 | -49.40332 | 2024-10-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8553e52-1270-3eb1-ba94-52928f375cf3 | -3.94214 | -49.84487 | 2024-10-12 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e1913bb-4658-34cf-9fa3-ca0c486756cd | -3.93667 | -50.618 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb6d8990-3dfc-31cc-8297-59e7fd044eb3 | -3.70801 | -50.12061 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d3428d9d-9649-3f25-943e-5ea59c959b49 | -3.70566 | -50.11139 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24e20a47-ad23-3830-98e9-c4dbd91918d8 | -3.705 | -50.1157 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 355db45b-4b6c-3dcd-815d-340d86ebe41b | -3.70435 | -50.12001 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96ab26cf-7975-32f4-b9f0-4a4d1fa33b90 | -3.70371 | -50.12429 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1b1f8b8-fc76-3512-9b54-01451c40e25e | -3.70135 | -50.11512 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 36c2b988-0fba-34c1-946c-0c62cc5274fc | -3.7007 | -50.11944 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fd134281-9589-3ea8-adb6-6797a51110d1 | -3.70005 | -50.12374 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea31b00e-4953-3659-af9f-614cdb63bb47 | -3.69769 | -50.11454 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0de9839c-f30f-3ac6-b7e4-f2a1cf804751 | -3.69704 | -50.11887 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ef981ab7-c9f0-35ec-99b6-8938c55f4d00 | -3.69639 | -50.12319 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72baf5bd-cd02-39d7-97e6-cfa0dda26a68 | -3.69403 | -50.11396 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f074dfa8-b5d5-33d5-b3d0-d6cbfe696a81 | -3.69338 | -50.11831 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ceee6a1-6eae-3b74-a941-e5aef64be263 | -3.69273 | -50.12263 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 49442d42-1790-323f-b07a-05ae686a8a6b | -3.68971 | -50.11774 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83dbf8da-8bce-3b1a-acce-7ed5d15417ea | -3.68606 | -50.11716 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e04cc737-0bfe-3837-b058-554d42018e58 | -3.68541 | -50.12147 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1875f34-4b2d-3ffb-8b4e-64d7518116d4 | -3.57913 | -50.56767 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 086767b7-70cf-302c-9ceb-1ed79b379f45 | -3.57556 | -50.56715 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 55f06cb3-93d0-37c5-8810-41e03966b747 | -3.57493 | -50.57122 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e962ea5c-c413-3663-add8-7e79233ef554 | -5.00713 | -49.75544 | 2024-10-12 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3698a68b-d87d-3dc3-a145-7b2977d2a1eb | -5.00333 | -49.75486 | 2024-10-12 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b2fbfde-f9d5-3631-aab2-8962d5bddda7 | -4.99954 | -49.75425 | 2024-10-12 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fd0ddb4-a8a7-34da-a399-77f450895572 | -4.90901 | -49.86803 | 2024-10-12 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8282858-fd94-38ac-8da5-3881c8a8e93b | -4.86335 | -50.77048 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e086ca4e-d367-34bf-bd41-60851dbaa2ef | -4.85444 | -50.6846 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02da0600-054f-3f8f-ac98-af3d01435a83 | -4.83682 | -50.80004 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae03206b-666d-3820-a0c9-cbc84ca5be68 | -4.83386 | -50.79543 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db99f5a0-eb33-3c00-b019-4a6166bf7cc8 | -4.83323 | -50.79951 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7c7de28-2d1f-33dc-b4e4-d64f92337076 | -4.83027 | -50.79491 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0f162e7-56b0-3be6-83ce-ee676b81f097 | -4.82965 | -50.799 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9af79b49-b2e9-3424-9f39-384f98599e3a | -4.82607 | -50.79843 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e11ab55-719e-3dd3-b966-690d77e0d7ac | -4.75159 | -50.7422 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 766d270b-e758-35fd-820c-77594e5b6afa | -4.60463 | -49.52173 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ccf650d-4b26-3d2f-a669-4138442f7c34 | -4.58565 | -50.80621 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README70.md)
