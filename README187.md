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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dff3d58-c1f2-3ebb-963e-8e5d75f83a7e | -11.67104 | -64.02682 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7323d2e6-314d-3571-a5a7-d7a93de3505b | -11.67017 | -64.03159 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 692623ed-8f35-33e7-95bd-2542dfa0b482 | -11.66836 | -64.04145 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 042490bc-6bce-3a1e-b2a0-ef0127b2e59b | -11.64714 | -64.02813 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 100d7a7d-3f47-380e-ba2a-664fa446c0bf | -11.62 | -63.8393 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f722f7f7-0429-3d1d-92d3-0fa939c4bc19 | -7.35619 | -64.66643 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9de0ef68-ffd0-3d85-9d2e-0a68dc054c91 | -7.35564 | -64.66953 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 962c9cc9-28bf-3cdd-8275-034f4878b58e | -7.3551 | -64.67262 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b773ad6b-f35a-3374-ac0b-44dca324dfe3 | -7.35455 | -64.67572 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9166faf-55c4-3345-b378-23e869f5a6a0 | -7.354 | -64.67883 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 787fde11-eaa1-3d2e-b0c7-3cbd2593464c | -7.35049 | -64.66859 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87381939-0056-3e2d-b190-2906061518c1 | -7.34995 | -64.67168 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25b5a9ed-9895-3631-9d19-a3f795f7afa7 | -7.3494 | -64.6748 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 373b6d88-59f7-33dc-aeaa-63b51eee81c0 | -7.3025 | -64.66946 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77d4013c-b4db-37d3-be62-61e44ea81595 | -7.30105 | -64.6688 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ec7c185-001f-389c-875f-3d41a77bbcdb | -7.29734 | -64.66853 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abb682fe-083a-31db-95aa-1d2f2c108be7 | -7.2959 | -64.66787 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 668923f6-878c-36ee-94b6-88dc065287e5 | -6.8228 | -64.33076 | 2024-10-09 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97915dcb-9cc3-3e28-8ef4-ce0e48492421 | -6.81981 | -64.32852 | 2024-10-09 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49ec5780-ff19-345d-a70b-03d7eabda505 | -6.81929 | -64.33153 | 2024-10-09 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2da57ee0-fa5d-3cb8-99e6-8bb347b76361 | -6.81773 | -64.32983 | 2024-10-09 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f7daaf0-0dff-3055-9791-3d1b08102f9b | -9.29412 | -65.42815 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a42bb8c5-642c-32f1-882f-b4c244a39486 | -9.29352 | -65.43149 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f5a85c9-3182-32bb-b1a2-ab6000364abc | -9.29292 | -65.43478 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 556cccab-f631-3451-9678-84e4e8d34dae | -9.28886 | -65.42731 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a748f1eb-b2d2-3a9c-81ee-b47aa470693e | -10.62552 | -65.21452 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4d7ee96-502c-3f02-9622-599c1ec7e1cc | -10.62498 | -65.21751 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58efc3ad-74fa-3638-988d-bf17df3fc285 | -10.61994 | -65.21649 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40fe440e-12c5-3292-8ab9-03a7fd92395b | -10.37533 | -64.83265 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| aed3a514-bfa4-397f-bb32-c6170d4bfaf7 | -10.37428 | -64.83843 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 670d08a8-2735-392f-ac54-f7518aec5086 | -10.37039 | -64.83169 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 510b89a8-f4f8-32bd-97bc-7318d1cb85e4 | -10.36934 | -64.83749 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 7f8a2906-f0c2-3e90-9f04-15c0eb2d86ce | -10.09558 | -64.84162 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13a1cff0-a8f2-3179-accb-07afd7da81ad | -10.0945 | -64.84746 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d41bc1d-ce7d-33cf-95d9-ece83b2b34c8 | -10.09061 | -64.84073 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 844be472-639b-3f28-94f0-cf4b94d6b66b | -10.09024 | -64.84113 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b2401e10-01fa-3f7b-97eb-fa70964841b9 | -9.58251 | -65.24383 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6175cc78-7628-31df-9700-5d51a4c2a7ec | -9.58193 | -65.24696 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1574ecf9-47e3-3efd-97b3-2d398823788e | -9.58135 | -65.25007 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b5f3e48-9fbb-387f-a73f-95b02ff8d38c | -9.58077 | -65.2532 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc7702bd-87f8-33d5-85cd-207ef207e57f | -9.57678 | -65.24598 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13c9cc2c-035d-3635-ac81-4e83b4f8b383 | -9.5762 | -65.2491 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b776f58c-b65c-31f8-ae94-f7a83d42adcd | -9.57562 | -65.25222 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1db78c55-39e8-32d9-9a40-a6c499872b50 | -9.57504 | -65.25534 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b66e283-8701-3188-9603-4039c4c7c4db | -9.57423 | -65.25153 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d092caf-6ee5-3cc9-8a6d-2adb8fc5259f | -9.57367 | -65.25465 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e70bbe48-e281-3ea0-9cd3-b22d92044c6b | -9.4919 | -64.67353 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| baf5f886-c6e8-3a08-9382-759b225c8fda | -9.36434 | -65.51623 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f089b9d8-6d9b-33bc-b22e-bfa59837c88c | -9.36374 | -65.5195 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 221f7161-2082-3232-8096-3b7cbcaf6623 | -9.36314 | -65.52277 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5eef2d8-16b0-3709-83e8-0f53268e2368 | -9.36254 | -65.52603 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2f45628-df0a-3ef6-ad59-2a3c84014789 | -9.35787 | -65.52182 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9024eafe-5537-343a-8ea2-0b76aac5f5d2 | -9.35727 | -65.52509 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59f11f17-15aa-3882-aa98-6e27a86dfdb1 | -9.35667 | -65.52836 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 158e737c-ff48-3c75-bb00-b663bd8623b5 | -9.99305 | -64.77874 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8caee1e-e4ea-331c-8173-cc4215216900 | -9.98957 | -64.77408 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 13a65a42-3021-3bee-9d22-5f45a04ab5bf | -9.98852 | -64.77973 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58c5dc70-65ee-3500-8663-5a04d9551004 | -9.9881 | -64.77779 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f389151-f7f1-36b1-b2c1-611fe622ab66 | -9.98746 | -64.78545 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3813e716-7171-3d29-8544-e42a5391985f | -9.98708 | -64.78352 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 73fdf9fa-ffb6-342b-9bda-2c5ad2aefc0d | -9.98356 | -64.77884 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68bd239f-913d-3851-a19a-ad14bdf426a4 | -9.98313 | -64.77691 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7fbc364-8ee5-3a11-a583-5c9f0e31ffc7 | -9.9825 | -64.78452 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4db9082-93c8-301b-a696-d62ea05470a3 | -9.98212 | -64.78259 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0d816f3-105d-3532-a213-27bca871366a | -9.96585 | -64.76388 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ffaf5ff-8449-3279-900e-573f6c01a767 | -9.96479 | -64.76955 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 939ef090-5080-36dc-a857-32b539641922 | -9.96432 | -64.76755 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afa45ca8-a8d6-397a-8e2b-1968c2188ec2 | -9.96127 | -64.78456 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb6bfe2a-7fec-3fc0-99c8-38c081939490 | -9.92552 | -64.78371 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60d558e6-e928-3e02-a1ca-37ce60b75d7f | -9.91912 | -65.04796 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99c827ed-cef2-3772-9933-15dbc393ea34 | -9.91858 | -65.05096 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c0d0ed5-465b-33df-bdf1-448406c65bfc | -9.91664 | -64.77617 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 466e446e-061e-3eb8-ad0f-8660bede844f | -9.91558 | -64.78194 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5deecfef-fab1-3818-a228-3e6f266b6bc1 | -9.91166 | -64.77532 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e217fa4-3844-30c2-bb28-f591ea3472d5 | -9.88927 | -64.92577 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3794109d-1735-381c-bd8f-4e8db7545bb6 | -9.88425 | -64.92484 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e4ef94d-5df5-3a21-9ce6-8874112b7c53 | -9.79368 | -65.05738 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a12d49d2-57f7-320a-93df-524b9a195ebf | -9.74119 | -65.87779 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6baeb1d-ca52-393d-8ff1-053264462ac7 | -9.74056 | -65.8812 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccb10953-3dc4-345a-b65a-d35cf2e24eb6 | -9.73994 | -65.88461 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2d22132-3cbe-35ce-8c41-66c384c27288 | -9.72959 | -64.89874 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb0e7c56-d45b-35fc-9e2b-cac1a0ce06af | -9.72906 | -64.9017 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a452839-190f-3027-a254-6df90364ac7d | -9.80155 | -64.46732 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccec3b05-64b4-3f24-9989-aaf49ad7e88e | -9.80059 | -64.47272 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6f64490-7fe6-33e3-bca5-6b6a3581d297 | -9.79669 | -64.46639 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bed60d5-585c-3a99-a33e-2c106c928e38 | -11.71211 | -65.00471 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ece005ad-a635-37aa-828b-944a8ad71d64 | -11.71108 | -65.01019 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 9956e662-cc6f-3bbb-8166-0199e00df437 | -11.70723 | -65.00376 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.4 |
| d4de15e5-73f2-37c9-b5bd-85120d9ad85a | -11.7062 | -65.00925 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.4 |
| e3d487a5-66ae-3812-b98e-1bad1e2d1250 | -11.70517 | -65.01476 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3c7406a3-c9a2-3324-9dba-4febb525587e | -11.70235 | -65.00282 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c9830f7f-a1d0-3848-ae65-ee329a5f4c81 | -11.70132 | -65.00832 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 480eec3c-4352-3d03-8930-38204fd70648 | -1.11 | -53.6173 | 2024-10-09 05:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 4c8cd528-a737-302d-b3ee-98a7d9a77d14 | -18.68373 | -57.2278 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 26d71dc0-6810-38ea-bcde-4286c82f8efe | -18.68036 | -57.22725 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| dee3e168-c76e-3d4e-bd6c-f364a5f72b3e | -18.67756 | -57.22293 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 24c04be0-829b-3d49-ab55-8a7737b4041d | -18.67531 | -57.21487 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f44831e6-fdb6-3a0b-98a9-7cdbf9599111 | -18.65903 | -57.20834 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 824bcd38-82ec-3a71-abb2-8cf38608d5fa | -18.63653 | -57.30087 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| e4e2c0db-589e-3a17-9174-7ac06440b2c5 | -18.63374 | -57.29658 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |


[Clique aqui para ver as próximas entradas](README188.md)
