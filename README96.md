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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00da64f3-2382-378f-89c5-2e74d975de1f | -3.55867 | -53.75289 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e368af39-e2a5-3af9-97b4-982024095b96 | -1.66267 | -53.6858 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9179afd2-d0ef-3f6d-b2b9-b6a069ce6775 | -1.54754 | -53.70131 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c60fc691-de9f-30d6-91d8-5f9a43b41be7 | -1.5433 | -53.70073 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c8c9934-ac67-3244-8c2d-3db6ebd76466 | -1.49598 | -54.18505 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dfdb981d-d77a-3432-8157-da87962cebbb | -1.49243 | -54.18082 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be83ffed-561d-308a-bb98-5f3c40409fe8 | -1.49189 | -54.18442 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6eae19a1-966a-3a0d-bac2-408e3c3f41b4 | -1.49135 | -54.18801 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eb4cc6ac-92c2-3df4-ba81-981edfc3e25d | -1.16641 | -53.50605 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94e28778-6b17-3ae1-9ced-2cc053c71709 | -1.1629 | -53.50593 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f45c7ca-6d71-3766-81b7-ef9ead9590d0 | -1.16217 | -53.5052 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0f8562cc-3596-33a3-a359-761d3007888e | -1.16034 | -53.65989 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a96c15f-2d2b-3a68-b55a-468a26b70be3 | -1.12127 | -54.15997 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 376550c5-202f-31ba-aae4-7e596f79fef1 | -1.12071 | -54.16358 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc1c4e19-d978-3a62-9bc6-5a676dcc84b7 | -1.09883 | -54.116 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c47ca40-ee7b-30f5-b365-7333980ee3e1 | -1.09699 | -54.18208 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1f64d77-4408-3d94-abb6-d53f9f6d94c1 | -1.09475 | -54.11534 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b1ab135-9176-31a9-a3d7-64b2fe2800f3 | -1.08303 | -54.10993 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2a3c8b9-0c4b-379b-baca-722c5b18b1c1 | -1.08247 | -54.11357 | 2024-10-24 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 450c43a6-4c0a-34e6-91cf-e25aded18774 | -1.07623 | -53.67098 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fb0be19-6f16-3663-8e8b-1df5fa038e24 | -1.07563 | -53.67487 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8e9c9dd-e88b-3319-b18b-1d720b71e612 | -1.0744 | -53.65495 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bae93d9d-b06b-3f98-a704-7d3552592698 | -1.07316 | -53.66296 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2703762-2fa5-3a9f-856c-4abd6bd22738 | -1.07258 | -53.66671 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e85ee9b6-1569-314c-a94f-13b1859e3bb8 | -1.072 | -53.67046 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b21ef70b-7135-3952-9f60-17be8c294600 | -1.06837 | -53.66608 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a569ec7-61d8-3e82-9896-23b40d69a62e | -1.06536 | -53.65759 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 239eaadf-b9e9-38b2-9f82-e325724dda23 | -1.06114 | -53.65701 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef02d6a4-31f5-36ca-abc1-3c5c5c9245f6 | -1.90513 | -54.58516 | 2024-10-24 05:21:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 437e0ab6-687b-3681-a217-84c49374f0dd | -1.90459 | -54.58867 | 2024-10-24 05:21:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 734850fa-ba0d-34c1-adb4-1db767ec2ff6 | -3.26094 | -53.78266 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4bfee85-7e44-3968-a022-4b32581292f6 | -3.11077 | -54.17212 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65344149-6998-3e27-8f58-b5477b66bb05 | -3.11063 | -54.16903 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f64fe593-7ab0-35c6-bafb-e29cad57cc6f | -3.11003 | -54.1729 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f821c3d9-01ff-3213-abe5-86b2a1c498ec | -3.10948 | -54.15171 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d5fdb230-a155-3228-90a0-afa420a1af5b | -3.1089 | -54.15565 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e37819c-609e-370f-a6dc-1a8d3ec725b9 | -3.10889 | -54.15256 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8a118944-eacb-3b90-ab93-69537c2f214f | -3.10831 | -54.15963 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d28b6a64-f2e4-32d7-9574-c9f7636a51d7 | -3.10828 | -54.1565 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bfa6dc60-675c-3d37-a03d-4ae6d37a6ebe | -3.10773 | -54.1636 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23227ba8-2536-39d5-a111-e3b21a335a53 | -3.10766 | -54.16046 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc3cfe56-dfe0-31fd-b7af-21981047fc8f | -3.10714 | -54.16757 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6cd434f5-fc23-3aed-9d46-5f1ccce86dd8 | -3.10705 | -54.16443 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 072521d8-00fe-3fa9-ad8d-5f12902cdd29 | -3.10656 | -54.17151 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 181585f1-9c7c-3af7-9fa9-522c8b9a92dc | -3.10643 | -54.16838 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c106f87-f7dd-3a05-8df3-364499c6809a | -3.10582 | -54.1723 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 585e7592-0d1f-3a8d-bff0-5d31e9bbccc4 | -3.1053 | -54.14797 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c66a1e60-b44a-3373-a5ae-7763807e88b8 | -3.10522 | -54.17616 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60cf9026-78d2-37b0-a5ad-8fd80484e10d | -3.10469 | -54.15188 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3946f314-0535-3e08-8ba7-ca04ad6715aa | -3.10408 | -54.15582 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 29696d2c-df19-3b61-ada3-5ee81016cd9c | -3.10346 | -54.15981 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d7732fd-4bc4-3f03-b2d6-ab717e3f97b4 | -3.10285 | -54.16379 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3810999f-6f93-3f3f-a715-d34ed655619e | -3.10223 | -54.16775 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f624a2af-2f56-3081-8862-75623a245a0d | -3.10162 | -54.17168 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c7abc0e-9bcb-394f-9824-02c6684b475e | -3.10102 | -54.17556 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b62fb0a6-2cbe-3cdb-982c-3792708ccac4 | -3.10049 | -54.15126 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e3169bf-6561-3f25-8490-d61e4d046419 | -3.10043 | -54.17941 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b417462-80f8-3194-b06e-c085a8e7a260 | -3.10015 | -53.72308 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 220596ac-868d-37d5-8a36-5fcea4e8ce49 | -3.09988 | -54.15518 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46e76958-714b-31a9-aed2-598ea42fba93 | -3.09953 | -53.72722 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 51562283-ddb3-3d9b-a50b-4e7538f8affd | -3.09926 | -54.15917 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ff2360e-1c39-3be5-b3fa-d0b510586fe2 | -3.09865 | -54.16315 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52678e57-36da-3469-a445-967d1da4f050 | -3.09804 | -54.16711 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85b290f6-8d6d-3abd-8a20-d80c506b4b2a | -3.09743 | -54.17105 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be7413e3-5ed6-34d8-a437-c58157eb8c73 | -3.09683 | -54.17494 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ee86380-e41e-391c-96b4-173897b1e6ce | -3.09628 | -54.15063 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ec438d2-8496-36bb-acb9-0a7271253b81 | -3.09582 | -53.72244 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c64e9804-5d2b-33ea-8642-a7dfb70aaf83 | -3.09568 | -54.15454 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87f4b5c8-acfb-3bbc-99c4-d5dad1f66b09 | -3.09506 | -54.15853 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cca7ccb-b0ed-314d-9f86-f1823b66cb93 | -3.09445 | -54.1625 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdaf9280-90e2-3046-9249-878c1699af46 | -3.09384 | -54.16645 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb54ca0c-9d2b-3a3c-ae36-1a116761142c | -3.09323 | -54.17039 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e25b904-aa9f-33af-90f8-4bc352b30edb | -3.09026 | -54.16183 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1960e333-f822-304f-a342-68b33e1dec53 | -3.08965 | -54.16577 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f03f8946-558a-3c2b-9095-1f4933598776 | -3.08071 | -53.82365 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c33a2c7-d9f3-3bc9-84ac-6a7f72ae30e6 | -3.08011 | -53.82765 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71e82b72-2dca-3c01-b98a-cb53a664ef1a | -3.08006 | -54.17232 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d08fb772-d8dc-33e6-9237-0b8f8201d301 | -3.07946 | -54.17623 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e2332cc-ebb8-3242-b8a8-421d5007cbec | -3.07641 | -53.82299 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d72cca9-9b3f-34bf-abae-bdf1edd73051 | -3.07582 | -53.82695 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d393810f-3996-37e5-924d-683be4565c8f | -3.07523 | -53.83091 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8236fa0-00c5-3d73-93bf-c093eecc455b | -3.07212 | -53.82233 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0e4c7d5-c682-3c4d-bbfc-48a0583e56c2 | -3.07153 | -53.82627 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8593be85-8b30-3f4a-8696-0f90e15a3825 | -3.06841 | -53.81772 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0719f6a1-196f-307d-8147-07371e7d70d7 | -3.06782 | -53.82165 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f40d37a-3e3d-39d0-a284-5e52c803f25b | -3.06723 | -53.82561 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b20c5022-9d17-3cd8-8f52-73c128f2fe51 | -2.9951 | -54.10458 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32bf73fc-1caf-3003-ba24-fc1ea373683c | -2.95889 | -54.05937 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fafe39e-89e1-3490-9e45-daf833e13351 | -2.9442 | -53.706 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fe5a33a-165b-34ad-b67d-bfadf033cef7 | -2.94356 | -53.71011 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb9642c6-04f2-3ba0-9b04-122c3a6c3ee4 | -2.94203 | -54.1989 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95ca279c-d52d-3aa4-887d-855f2d09ad74 | -2.94145 | -54.20272 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 199b9898-5b64-37b7-8b7f-733e1711edf6 | -2.93924 | -53.70946 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 765aa542-d88c-346d-a1eb-a83175e8605d | -2.93799 | -53.91602 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95b2509c-c7a8-30b5-b204-5bdbbcfbf9c3 | -2.93737 | -53.91997 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6847a38-f80e-3895-a965-16471ae63a0d | -2.93716 | -53.9148 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 154a6c03-c1ca-31a1-a44f-d2357e149bc7 | -2.93675 | -53.92394 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0246342e-7aca-392e-8914-93dbc0760f8d | -2.93658 | -53.91875 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c43774ee-34f1-38f8-afd9-a9c4713babc1 | -2.93599 | -53.92273 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2200855-aea2-30d4-aaac-9aa35bca6614 | -2.93481 | -53.9307 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README97.md)
