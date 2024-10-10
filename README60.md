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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21ae3232-bd54-353e-8898-e585e58a01d4 | -4.99267 | -45.37725 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b8daa00-6d17-3fab-ab95-3d72cbb83c1e | -4.94813 | -45.50545 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc519ae5-e136-38c4-a250-df0a6df28626 | -4.93254 | -45.42984 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 594f5598-08c9-3494-8c96-b3a874f2a9f6 | -4.92917 | -45.42932 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 795da66a-370a-39e6-86fb-5cd2cf2002a3 | -4.92873 | -45.8023 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87520ba3-1cb7-3a54-8ee5-e19a52866b42 | -4.90382 | -45.93711 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20186cf0-cfc3-332d-b3fa-2209760a14e0 | -4.88944 | -45.69917 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 193feb20-793f-3166-93ce-5d6009db9f09 | -4.88605 | -45.69864 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f32fd3e-5622-3501-bb89-44f32316148a | -4.88547 | -45.70225 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8cb6d36-a3d1-3ee6-b785-ab11c6b1baaa | -4.88118 | -45.33383 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6cf2d49c-3ee8-3c84-8913-bd3f67362110 | -4.8692 | -45.80368 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f4c3062-f908-3b45-ade2-d47942c1d5da | -4.86861 | -45.80735 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83b60ed1-f200-335e-ba33-bff34ff337f9 | -4.86827 | -45.34997 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e413544-bb6c-323f-96d1-2d984867baa8 | -4.8658 | -45.80311 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2a9bdcc-a104-3bb7-9143-b123596a266d | -4.85078 | -45.41658 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d108783-6abf-31de-ac16-7cb280b667af | -4.84684 | -45.41964 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e57c443a-7259-30d1-8076-7e466272cdf7 | -4.8401 | -45.41859 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aea99b97-3e38-3153-bffa-a92983d4f6c3 | -5.5811 | -46.31194 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| af04a111-ae26-315c-8e84-f30c327b8ae7 | -4.83673 | -45.41806 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f71b1fa2-8b19-3582-a486-9793c2df756e | -4.83293 | -45.35533 | 2024-10-10 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fab34e6-ade9-3438-874f-2d1cf8795325 | -4.73493 | -45.68193 | 2024-10-10 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e143207-c01d-3e01-98ee-0cb8a2717691 | -4.72532 | -45.67667 | 2024-10-10 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ab42c55-d254-3b4a-a5a7-c877e6e5bef7 | -4.72193 | -45.67612 | 2024-10-10 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a277e08d-270f-3a0c-8422-c2567b0095af | -4.72136 | -45.67972 | 2024-10-10 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4066ef40-b5c4-32f6-a34b-7aee00d7d06c | -4.69039 | -45.63404 | 2024-10-10 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10b24eb4-17bf-38c4-bd54-8cd8bc99996f | -4.68914 | -45.81651 | 2024-10-10 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa5edd12-83b7-36ac-845e-4fc967bbf7a4 | -4.68856 | -45.82017 | 2024-10-10 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 211a8edf-64d6-3a67-95d4-d06ab6eb887a | -4.68515 | -45.81964 | 2024-10-10 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53b098ec-8f6e-3bec-8115-3125941cd4fb | -4.68376 | -45.87226 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39079453-c859-3cbd-9784-cfd17ea62103 | -4.6727 | -46.05217 | 2024-10-10 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fba6e54-aca2-37d2-8d73-9cfeaa15f86f | -4.60428 | -46.08322 | 2024-10-10 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c4f2d86-c0d6-3bb1-bff2-21875962b577 | -4.49631 | -45.71188 | 2024-10-10 04:17:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f94b1970-aca6-3a63-a421-2d32b446b13c | -4.4929 | -45.71136 | 2024-10-10 04:17:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d981ca83-edb4-341a-837d-a53fa607478b | -4.46374 | -45.89463 | 2024-10-10 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d20946b2-9656-3f7f-aed8-bf7c70235f9d | -4.46315 | -45.89833 | 2024-10-10 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a597356c-17ca-312a-81b2-a8e6b2e3eac8 | -4.46031 | -45.89415 | 2024-10-10 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0c1310d-ba7d-3bc6-a818-4cf98af4b6d2 | -4.28359 | -45.47071 | 2024-10-10 04:17:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1deeacb-7c5b-3b93-bac1-ad677ac3c4d4 | -4.28301 | -45.47431 | 2024-10-10 04:17:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eff92781-7d64-3454-ad7f-8c46f0a937ae | -4.28244 | -45.47792 | 2024-10-10 04:17:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b664d99-dcb9-30fe-a453-c260b2abe793 | -4.2802 | -45.47018 | 2024-10-10 04:17:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51ac0755-0304-3b35-b79b-902da051c545 | -4.27739 | -45.46605 | 2024-10-10 04:17:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b03081de-af2c-3ef7-95a2-060bb7f301c6 | -4.27682 | -45.46965 | 2024-10-10 04:17:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49343136-4e6e-359d-bfd6-961e7890ff4f | -3.90825 | -44.86977 | 2024-10-10 04:17:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7683d13-02e0-3b4b-871d-cc0537aeec4f | -3.83201 | -45.56382 | 2024-10-10 04:17:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52f9e707-9765-39bd-949a-8f90e8a24de2 | -3.81131 | -45.49723 | 2024-10-10 04:17:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0c4949d5-6198-3966-ab9d-7b9e9ec13015 | -3.81072 | -45.50085 | 2024-10-10 04:17:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 67202baa-8b3a-3028-993d-fb0c63ac0381 | -3.80791 | -45.49669 | 2024-10-10 04:17:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0e4675cb-4d59-310c-b048-3879bac08d2e | -3.80777 | -45.4971 | 2024-10-10 04:17:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9d0a3e39-46fa-3092-96c3-f28bd6979d39 | -3.80733 | -45.50032 | 2024-10-10 04:17:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bf363cfc-9746-34c0-8791-5733941a4dab | -3.8072 | -45.50073 | 2024-10-10 04:17:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 57da00c5-4f49-3f12-9163-4689821be4bf | -3.80437 | -45.49656 | 2024-10-10 04:17:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7eff3219-64b8-3cd7-b9bb-991b2df33ddc | -3.72199 | -44.67926 | 2024-10-10 04:17:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31ad8ac9-5cab-3eaf-a2cd-345462682be7 | -3.72144 | -44.96338 | 2024-10-10 04:17:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56684caa-dcc4-39d3-a729-34f04c82e210 | -3.72088 | -44.9669 | 2024-10-10 04:17:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c12e7572-a8bc-3d3f-abf8-1d37ec4eb6b9 | -3.71808 | -44.96284 | 2024-10-10 04:17:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4d89be5-ca2b-3e46-b195-0c27642ac5b1 | -3.71752 | -44.96638 | 2024-10-10 04:17:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73ee209e-6d40-3652-9c42-63440dfe9130 | -5.0864 | -45.16709 | 2024-10-10 04:17:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80cb3b34-0be6-3402-8dd4-027bab23afbd | -5.08584 | -45.1706 | 2024-10-10 04:17:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58d6c055-73cb-3cab-b946-ea3dab7da4b0 | -4.96498 | -45.03278 | 2024-10-10 04:17:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2bc8448-b8a7-3feb-be4e-c23e63e93681 | -4.70817 | -45.21227 | 2024-10-10 04:17:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47d9ce17-1dd2-3c56-95c8-3b684b47c1c0 | -5.84735 | -46.43357 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81fc0949-4667-3a5b-949c-65eef97703a1 | -5.84714 | -46.45672 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c01acf9a-b662-3c51-aa07-c5d48180090e | -5.84431 | -46.45238 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0124cd3-68d0-3a97-b42a-6dcbd444423c | -5.77626 | -46.11826 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 364eb844-a864-3802-aeb6-5d74e76b293b | -5.76997 | -45.98191 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f67918a4-5977-35f9-a59a-8589b8b34d53 | -5.76017 | -46.50185 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe9f4cdf-c8f7-32c3-b95f-5f5f94d7c1d4 | -5.70371 | -46.4425 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 307be853-3c33-35e9-b5af-adaf5aafd7cc | -5.70311 | -46.44627 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae7b07c3-3a37-36f6-8bee-4e4faaa3c341 | -5.68784 | -46.32057 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f69e81e-4bed-3497-9250-bdc346e0816e | -5.68439 | -46.32003 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f046d233-9c36-3ab4-8c2b-c16c21106d78 | -5.66754 | -45.30536 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b583ca33-b3e9-33d6-85ff-038387177011 | -5.66419 | -45.30483 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db63ff2b-d0e8-3d7d-a6b6-1fad7f31fe0b | -5.5389 | -46.20208 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ae3608e-ea12-359e-89bc-deb3d815dae3 | -5.53651 | -46.19842 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8037f6b3-ea91-3eda-b5fe-b1880e210116 | -5.53607 | -46.19782 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10dfd127-0de4-3053-9540-3b3f0ce49f25 | -5.53592 | -46.20213 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ff31acb-a0fe-3179-87db-d920e6785706 | -5.42822 | -45.10211 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3490448-3f14-3aaf-a682-728b4a953e86 | -5.4161 | -45.94563 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95cc2ea1-5935-337b-b2cd-7b1fb278ad33 | -5.4095 | -45.89966 | 2024-10-10 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fc0a3a2-24ff-3227-96f9-5b42b92837a9 | -5.40892 | -45.90328 | 2024-10-10 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21b992a3-928e-3851-a8d2-6082414d990b | -5.4061 | -45.89912 | 2024-10-10 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63934735-ef9f-3a36-a2dd-f8e03d97f3e8 | -5.3986 | -46.14275 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4eff7ce-3867-372b-9d74-7855c389a456 | -5.39824 | -45.99166 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bfcd10f-79be-3334-ac46-7e24b4380d76 | -5.39483 | -45.99112 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10358298-2a1b-3cc1-ac18-5506d1c807a5 | -5.39201 | -45.9869 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b6c40c3-b47e-3c73-b706-7778d562c047 | -5.39142 | -45.99057 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2733aa9d-46a4-3a97-b5bd-401fe7e52332 | -5.3867 | -45.40625 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc6dda90-d4c8-36d0-a1a2-90493f9bda9d | -5.37244 | -45.19407 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1073e012-d35f-3874-b297-514d45ea685e | -5.37081 | -45.19353 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 730755b4-b9b0-342f-ad81-cb57599ce5f3 | -5.37026 | -45.19705 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77c267eb-bbaf-35e4-890e-54134a73e30a | -5.3563 | -45.70552 | 2024-10-10 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d9c89a6-6283-3ded-afd4-44974a8fa47a | -5.31544 | -45.47844 | 2024-10-10 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff15b00e-797e-38c3-a126-7af92edaa000 | -5.31488 | -45.48199 | 2024-10-10 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45e33735-3700-36af-83a5-3e6284460049 | -5.31432 | -45.48555 | 2024-10-10 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 343bf06a-ef2e-31dc-916e-e95888bd557e | -5.31152 | -45.48145 | 2024-10-10 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e4d93b0-23d0-361f-952d-31968c63ca5f | -6.10481 | -45.98611 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 133fc466-4b19-3716-9755-c7e6c155fc2b | -6.08446 | -45.98278 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52f40fd4-9b97-3aa7-968c-ad50ad966502 | -5.98799 | -46.34444 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bf118f7-1992-386e-8979-2e6c13b8993e | -5.98739 | -46.34815 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 095fd97d-bede-3a66-950a-676ced1ca669 | -5.85019 | -46.43791 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README61.md)
