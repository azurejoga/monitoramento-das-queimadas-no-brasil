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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e9a6850-865e-368a-97bd-e453f505a3b4 | -4.5134 | -46.444401 | 2024-10-30 00:51:30 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0086e159-ef9e-3bd4-a154-604d3ecdfd60 | -4.5167 | -46.458 | 2024-10-30 00:51:30 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28e629eb-6f67-376f-976a-34485ec50d6c | -4.5004 | -46.432999 | 2024-10-30 00:51:30 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71ab994e-e976-3bfa-abc1-a22022f2427b | -4.5036 | -46.446701 | 2024-10-30 00:51:30 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0423c0a7-372c-3da9-8d59-474c2e12d0b7 | -4.5069 | -46.4603 | 2024-10-30 00:51:30 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 475b351e-2472-3159-bed8-2e934031f6f2 | -4.7732 | -48.029999 | 2024-10-30 00:51:31 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbec8013-ce35-3adb-98bb-c62617e0225f | -4.7757 | -48.0406 | 2024-10-30 00:51:31 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 726ae7cf-6019-3660-b09e-31c049be6a5c | -5.3084 | -50.5616 | 2024-10-30 00:51:32 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20d33afc-7793-3bca-b651-0a9e61dcfb8a | -4.1019 | -45.921101 | 2024-10-30 00:51:34 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8fb523d-402c-3921-81a2-2510abd355c3 | -4.1054 | -45.9361 | 2024-10-30 00:51:34 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e1d13425-96e7-3c80-bf9d-3a8afb01a0e5 | -4.9729 | -49.6422 | 2024-10-30 00:51:34 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8004c12d-43c6-3c75-a7a7-ab38d6c83ffb | -4.2042 | -46.701599 | 2024-10-30 00:51:36 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c0dab77-3e1d-3b08-b93b-b843a0517e91 | -4.2073 | -46.714802 | 2024-10-30 00:51:36 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f042a8e-3d2e-338e-ab32-14451d3932eb | -4.0775 | -46.2519 | 2024-10-30 00:51:36 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3f53592-ae8a-3953-a2d4-96a51fc8498e | -4.0809 | -46.266201 | 2024-10-30 00:51:36 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43e9aa79-6936-37c5-86b7-5db579b23ad8 | -4.0842 | -46.280399 | 2024-10-30 00:51:36 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 171398d9-c3ca-3384-9f6f-e4376cc69998 | -4.0712 | -46.268501 | 2024-10-30 00:51:36 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22bcecc3-4be8-321e-8ddf-70849fd425f7 | -4.5023 | -48.104099 | 2024-10-30 00:51:36 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c60d5836-3b55-3dc7-9ac4-1182b522dc31 | -4.1608 | -46.822701 | 2024-10-30 00:51:37 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa53fbaf-aa1d-31fb-968a-1cd7163940a4 | -4.1638 | -46.835701 | 2024-10-30 00:51:37 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8375b1bc-4ef5-34b0-ac01-1ca18b532251 | -6.8671 | -59.002998 | 2024-10-30 00:51:37 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a9b74f2-2e02-3c06-bf19-d60df2d75e59 | -6.8699 | -59.0159 | 2024-10-30 00:51:37 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8e92424-9652-31ad-bbc1-db1311449384 | -6.8726 | -59.028702 | 2024-10-30 00:51:37 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8313db77-4317-3482-92ee-2f02fa59bd72 | -6.8602 | -59.017899 | 2024-10-30 00:51:37 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42a75768-aa8d-39e7-a2b0-18895f55a37a | -3.6726 | -45.062901 | 2024-10-30 00:51:38 | METOP-B | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7afe8580-180b-3343-b6be-927ad6594401 | -3.6768 | -45.080399 | 2024-10-30 00:51:38 | METOP-B | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45fe61f4-f5c9-32ae-b197-7c5be620863b | -4.3706 | -48.201401 | 2024-10-30 00:51:39 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 059a21ab-c287-33a4-b216-9c34e2219fee | -4.373 | -48.211899 | 2024-10-30 00:51:39 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40be3dc5-e18b-35d6-a2e1-79487f02c057 | -3.3687 | -44.0452 | 2024-10-30 00:51:39 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3df77588-3af4-3224-a058-ec30473a9c0e | -4.1456 | -48.119099 | 2024-10-30 00:51:42 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61cd76a2-965c-3818-8711-8c8f3f3dbe71 | -4.5802 | -50.398499 | 2024-10-30 00:51:43 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad5d077b-5cf0-3c61-9263-6a9c7f555ba3 | -4.5726 | -50.499901 | 2024-10-30 00:51:44 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a764677a-94ff-3edd-9383-f5b5bd47e60b | -3.9572 | -48.1059 | 2024-10-30 00:51:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17350876-6d6c-3463-863f-892da24e9ef9 | -3.9597 | -48.116699 | 2024-10-30 00:51:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef98b041-b687-3a05-92e5-e22cc43502ad | -3.9622 | -48.127499 | 2024-10-30 00:51:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58b275cf-8871-34e4-8c54-eb4bc005a5f4 | -4.4156 | -50.309799 | 2024-10-30 00:51:46 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fff0a42-94c9-336a-a4cb-6390bdcb7dc2 | -3.9506 | -48.342602 | 2024-10-30 00:51:46 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88829255-ac6c-332c-937d-9a8e555d5f67 | -3.5868 | -47.355801 | 2024-10-30 00:51:48 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cce1d6d8-c892-33b1-aa91-85d1e1d71812 | -3.5897 | -47.368 | 2024-10-30 00:51:48 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0950b55-3c3d-382f-a2d7-67473d86b9de | -3.5925 | -47.380199 | 2024-10-30 00:51:48 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be8bb722-170e-37bf-9d9f-b8ffc2501a3c | -3.577 | -47.358101 | 2024-10-30 00:51:48 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c5b7e08-3910-3ef1-9ed5-8a02e52ac535 | -3.5799 | -47.3703 | 2024-10-30 00:51:48 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ffc7aee-0df9-36d6-870e-a8699065ec99 | -3.5827 | -47.3825 | 2024-10-30 00:51:48 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa06a00c-ea7f-3a9a-b9b5-37a38ee5f112 | -3.5673 | -47.360298 | 2024-10-30 00:51:48 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7700e5d-cea4-3ea4-af3e-961bf350e912 | -3.5702 | -47.372501 | 2024-10-30 00:51:48 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc8e120-51ae-3aa9-a1ba-f74c00fc3f7f | -3.9117 | -49.062901 | 2024-10-30 00:51:49 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81dbda81-2b0d-3668-b721-97d60cbf5e16 | -3.9139 | -49.072399 | 2024-10-30 00:51:49 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a67a27e2-ed13-35cb-a402-3e527af56be2 | -4.277 | -50.6493 | 2024-10-30 00:51:49 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de114166-2109-3d5a-ba4e-024fd51f126d | -4.2788 | -50.657001 | 2024-10-30 00:51:49 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d5a1796-0c96-344e-9b6a-416829dfeac4 | -4.2806 | -50.664799 | 2024-10-30 00:51:49 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee2ceca-5288-327e-b43d-12831945745c | -4.0858 | -49.9963 | 2024-10-30 00:51:50 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbc570d5-81b0-3447-888d-273ad0c16e3d | -4.0878 | -50.0047 | 2024-10-30 00:51:50 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f136e34-c4de-357e-a359-44b0a6367f33 | -4.078 | -50.006901 | 2024-10-30 00:51:50 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 829dc745-b67e-3af6-9f8c-61375870a9e6 | -3.3131 | -47.02 | 2024-10-30 00:51:51 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 616efc75-2850-3131-898a-a11376970fbf | -4.0566 | -50.542301 | 2024-10-30 00:51:52 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ec3ffaf-e781-3f81-87f6-b0e9af73cc28 | -3.5335 | -49.2089 | 2024-10-30 00:51:56 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6058b9a-e0c3-32b5-a196-7eca3c49f059 | -3.5357 | -49.218201 | 2024-10-30 00:51:56 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fdac4d7-ad05-3293-a9cb-1183ea615022 | -3.5378 | -49.2276 | 2024-10-30 00:51:56 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 764dd7bc-8a90-36a2-91e5-bdb555f511f3 | -3.6665 | -50.144299 | 2024-10-30 00:51:57 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6992e6d7-981a-301b-93bc-7e61754259dd | -3.6684 | -50.152599 | 2024-10-30 00:51:57 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d0b7760-27c1-362e-b2f6-e9927a51df35 | -3.6703 | -50.1609 | 2024-10-30 00:51:57 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65e5dec5-87c9-3117-8b10-53c159e6f695 | -3.639 | -50.159302 | 2024-10-30 00:51:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c50ccf6-9034-31ea-9b62-9f6bc94a0a98 | -3.5866 | -50.021 | 2024-10-30 00:51:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4f853ee-45c1-35d6-9a47-f14a90be2cd3 | -3.5886 | -50.029499 | 2024-10-30 00:51:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8027433a-e41e-35de-9019-d9a2a43d92ef | -3.5768 | -50.0233 | 2024-10-30 00:51:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b183d397-45a9-3bce-b755-2423db6a1dd4 | -3.5788 | -50.031799 | 2024-10-30 00:51:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d7fcf54-891b-3a99-9628-bb8fb525d76e | -3.8236 | -51.145802 | 2024-10-30 00:51:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 748cac35-8d33-32ab-a169-4e66d78bafdf | -3.8254 | -51.153301 | 2024-10-30 00:51:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f32c9289-89f5-3cbf-a474-b6a8c268d566 | -3.8271 | -51.160801 | 2024-10-30 00:51:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d670eeab-8247-3f08-9b00-36db4168e3b5 | -3.8138 | -51.147999 | 2024-10-30 00:51:59 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11388bf0-0e61-315d-8a73-340df33c2b41 | -3.8156 | -51.155499 | 2024-10-30 00:51:59 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0715d733-6530-32c6-977b-8e8dfcb786f5 | -3.8173 | -51.162998 | 2024-10-30 00:51:59 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8c69f7c-c0a3-3b21-bfb4-3fdfc232db6c | -3.9032 | -51.902599 | 2024-10-30 00:52:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4860601d-f8be-3570-84c3-f9958e29d287 | -3.9048 | -51.909698 | 2024-10-30 00:52:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72e7775c-8736-336f-ae93-c3bcbb9fd53d | -3.9065 | -51.916801 | 2024-10-30 00:52:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 931466fa-dd9f-3a2e-b2f7-b5e16835e017 | -4.2688 | -53.610901 | 2024-10-30 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 085ffa27-fd17-3b5b-83b8-259be1cf12d3 | -4.2704 | -53.617802 | 2024-10-30 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42f22f9e-ed6d-3b2d-b950-1f002d0b68c0 | -3.7336 | -51.338699 | 2024-10-30 00:52:01 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c7c4642-2cd6-3821-ae40-cdcc0ff03c12 | -3.5228 | -50.461399 | 2024-10-30 00:52:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 971147e3-beca-3899-a47a-db7fa6634bd7 | -3.5247 | -50.469501 | 2024-10-30 00:52:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e82303-a295-30f9-b1f5-bbf94ee1831d | -3.8116 | -51.952999 | 2024-10-30 00:52:02 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0e71c2d-e2b7-3056-93d1-42b5c22115e3 | -3.8958 | -52.3694 | 2024-10-30 00:52:02 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1c1a34e-ee1e-3dd0-8fe7-a864efc6af2a | -3.3788 | -50.1479 | 2024-10-30 00:52:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ae07071-0a33-366f-8bd0-64835ba2ad21 | -3.3398 | -50.112598 | 2024-10-30 00:52:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1af85e31-091c-314a-837d-0c16dc4416f1 | -3.3724 | -50.254601 | 2024-10-30 00:52:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d820b4d-d448-3f76-bbc2-81f67d1e3eb9 | -4.5232 | -55.439602 | 2024-10-30 00:52:03 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d25992f0-dead-3a91-8eaf-3cc607ddc7d1 | -4.5249 | -55.447201 | 2024-10-30 00:52:03 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2321b18a-b242-3c0b-9518-ccc34204eaf9 | -3.5984 | -51.4235 | 2024-10-30 00:52:03 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c77d15c-11a7-35dc-8ede-9005725fae05 | -4.4259 | -55.0947 | 2024-10-30 00:52:03 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcfbc70f-ce8b-348b-9250-396649a239cf | -3.3022 | -50.218102 | 2024-10-30 00:52:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4985e00-3e2a-3a26-83ed-3fc6bbab1ad1 | -3.3041 | -50.226398 | 2024-10-30 00:52:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0840bc1-0f02-3a4d-94c6-9a8a47bcee46 | -3.7961 | -52.384399 | 2024-10-30 00:52:03 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a207ae6-591b-39d7-a4f7-255d7c3ffa00 | -4.1244 | -53.930801 | 2024-10-30 00:52:04 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abd57232-36b0-3d0f-b56f-7277133393d1 | -4.1259 | -53.937698 | 2024-10-30 00:52:04 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d639130-2892-3e4f-ad2e-1f4eb0584307 | -3.663 | -51.934101 | 2024-10-30 00:52:04 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 310c6ed2-034e-3ab3-a325-1fa5e43e8ef7 | -3.2398 | -50.170601 | 2024-10-30 00:52:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd7a45e9-8758-306d-bbe0-06795585c67e | -3.2417 | -50.179001 | 2024-10-30 00:52:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ea77fff-1bd0-3a83-a784-ffe4be4f49cc | -3.2436 | -50.187401 | 2024-10-30 00:52:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c114817-f894-3193-b159-310664acae59 | -3.276 | -50.328602 | 2024-10-30 00:52:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8678db87-874c-31ef-8843-3adf2882ba82 | -3.2779 | -50.3368 | 2024-10-30 00:52:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
