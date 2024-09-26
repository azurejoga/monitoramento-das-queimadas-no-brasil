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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23365491-4d6f-36f1-a7ab-39fd257d26db | -7.9289 | -55.76132 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c964b3b-8a2e-329a-a8d8-ac85a2c5fbfb | -1.98875 | -55.97961 | 2024-09-26 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cd14b8c-d0f5-3367-8cfd-3e704525b28b | -2.46093 | -55.61454 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87c9f30f-471e-3321-8b43-05e471cbd9ef | -2.46033 | -55.61834 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e04be325-f5d8-3194-a3c5-b50c0e634beb | -2.45972 | -55.62215 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bef19bf9-cc59-3097-8a96-e550fec4fb6a | -2.45911 | -55.62597 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c16a9274-74e3-3f33-9625-486ddd1e09c9 | -2.45747 | -55.61399 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23db546b-4093-3fd7-8463-ead7b1925774 | -2.45686 | -55.6178 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76180924-8a95-3f05-9807-88f14314c5d1 | -2.45625 | -55.62161 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afff0128-3159-32e9-afcc-de73b9b85a39 | -2.45564 | -55.62543 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eb31f5b-a8a8-3d2b-9a22-a683e245b0d6 | -2.17324 | -56.1422 | 2024-09-26 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 59295e20-20c0-304b-b471-44efd8e88e49 | -4.04954 | -56.22931 | 2024-09-26 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d6b34f7-3213-3ccb-9c04-c9169b443a45 | -6.4796 | -56.01255 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0adbe4d8-0ff4-37d7-a277-ea8b3ae08935 | -6.02319 | -56.57676 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e1c6a56-2f82-3c09-9a34-69c42a17148b | -7.68585 | -56.96037 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 612de325-61de-3e3e-8321-3815afa5dcd7 | -7.68521 | -56.96428 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23787060-eb7d-3bf3-9b76-63269dde8abe | -7.68236 | -56.9598 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 309d921a-a71a-329b-b8ff-a7e905f8d925 | -7.68172 | -56.9637 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45e2970c-b40c-3dc7-bb5e-38704bc1be78 | -7.6367 | -56.35624 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dff91874-2189-3c5b-bdd8-c93a87ed6713 | -7.63388 | -56.35197 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eb1d072-8396-3f38-b77c-6ebb67ffc62a | -7.63328 | -56.3557 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdc02a8c-7cf7-3621-b725-76de27e43cda | -7.13239 | -56.43327 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3aee11be-1070-3a7c-b3bc-b2588aeb328b | -7.05574 | -56.6944 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0735f352-465f-3a4d-bd79-9b3a9fc9cff7 | -7.05512 | -56.69826 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb1aee01-aad0-37a9-aa65-b613de6a6bcf | -7.05433 | -56.69419 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fe4469d-4afa-30a1-8985-1db6e282e7e6 | -7.05369 | -56.69804 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ab1ddf2-9add-3d28-bfaa-ad074473a8b8 | -7.05165 | -56.69768 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2aab5cf6-37c5-31c4-8a84-d70ac5e72924 | -7.04879 | -56.69329 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd30658b-5d72-3faa-a0e1-0712ed4d9fe7 | -7.04818 | -56.69713 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9daa68e1-fca1-373e-be31-240f44669a76 | -7.00284 | -56.45097 | 2024-09-26 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7701e179-c622-3d66-a91c-f73f9bcc370f | -9.23936 | -57.29156 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69979693-2495-30f7-bdb5-1f706474d3bf | -9.22444 | -57.14191 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ae5874d-af61-3a2e-9d4c-2f0c7854b864 | -9.21121 | -57.13582 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90bebc53-0c88-31f0-b474-4af0aded4377 | -9.20838 | -57.13136 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 837ab7a6-177d-3705-ba19-b4ca73b2d069 | -9.20776 | -57.13516 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 737f8ed1-acb4-37e1-9485-fb45e6848121 | -9.20713 | -57.139 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1951c5f5-70fa-334f-a4b1-bc24717d739b | -9.20649 | -57.14291 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d6ad419-91bd-35ba-9108-fa57007ed47e | -9.20584 | -57.14684 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cc9a8e3-38b5-3995-a3d8-49f86dd8340d | -9.20493 | -57.1307 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c19925e2-ae3c-35b2-a89f-ab287f07b964 | -9.20368 | -57.13837 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4806f0b6-117c-3cde-b821-62b35bca3f51 | -9.20238 | -57.14626 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6f8d9d9-487e-3891-b284-8af48c18934b | -9.20209 | -57.12634 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7be25628-26a4-3fa0-9cd5-6976cb33b5ca | -9.20147 | -57.13014 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 463a996c-0be3-32f7-be4c-d862b50a5e14 | -9.198 | -57.12961 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81213ceb-4ec3-3f48-a77e-2771829368cd | -9.19453 | -57.12908 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe18df71-4e6d-3c5a-b556-11c1a2c55a30 | -9.19042 | -57.13242 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f67e4e4-7280-3b6e-a6ef-0cea33278edb | -9.18915 | -57.14013 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8566ee2e-e091-3243-9e79-95f6426e9228 | -9.18607 | -57.11567 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e107a02a-bb73-3db7-923c-4706c0d5fc46 | -9.18541 | -57.11966 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74899caf-cc0d-304d-abd6-2ba462a3646d | -9.18262 | -57.11506 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22a7b844-c9c1-39d6-9019-b1c10acb0ed5 | -9.17982 | -57.11052 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a3252ed-2d79-3828-a98e-a2acbbaa066b | -9.17916 | -57.11443 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8234aac1-ea21-352c-bae0-8302bf69b048 | -9.17906 | -57.15813 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc269c29-6281-3966-970f-88fb6923612f | -9.17635 | -57.10996 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36730b37-bc9d-365f-8264-f10afe7fec7e | -9.17352 | -57.1056 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc2ca2a7-44f2-3ff0-a1d0-be8313697ac5 | -9.17004 | -57.1051 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8567847d-fde3-3b22-b8c6-1e967577d3d4 | -9.16759 | -57.10542 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dce5367-ef14-3d5b-b034-21128dbc7fb5 | -9.16756 | -57.33628 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 381577b0-39a7-3d01-bfde-cdd6b23a4233 | -9.16698 | -57.10925 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 234f497b-7dae-3368-8bc9-d3432143dc7a | -9.16593 | -57.10843 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 798a54e3-bb59-3b53-a2e4-f2d74db0eaae | -9.16406 | -57.33574 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7acba152-76bb-3c94-b8f1-720b7c84a9cd | -9.16289 | -57.11258 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 730978cb-a036-3120-9fe5-daeda1ad0195 | -9.1588 | -57.11586 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d534c025-0746-333c-b884-045a1b6e8c64 | -9.15839 | -57.32664 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03f3d2cb-3faa-33e6-b95a-0887b3c9c875 | -9.15534 | -57.1153 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d827a13-46f4-391c-ac0a-cce9b896866c | -9.15472 | -57.11915 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8770fe8f-df85-3d41-97c2-31c17d74fa42 | -9.15373 | -57.10329 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6df85370-d522-3ac7-89ee-2f24bfd0759d | -9.15346 | -57.1269 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1de1e0cf-7f07-374f-bc4d-b6ebbc8e5d9b | -9.15311 | -57.10712 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 455d53b9-fc23-35bd-8fa1-d1d57537c3d5 | -9.15203 | -57.32168 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f740c71-e502-3c88-be48-8d1859b47299 | -9.15062 | -57.12249 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 442df168-0376-3607-a5a0-74aa819eea71 | -9.1459 | -57.1297 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73a8e466-b3bc-3596-91e7-f8e39647958f | -9.14252 | -57.79788 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d696248-d057-3772-8c7a-8eab9f969c60 | -9.14243 | -57.12917 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a147b4e8-abbd-32a3-a641-9230c829483a | -9.14079 | -57.25979 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a2a9a8e-f6b3-3cc6-863f-0a24cce162b4 | -9.13905 | -57.26029 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcc39e3a-e9a6-38c3-ae3c-07bf12f0f0ed | -9.13554 | -57.81806 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e69dcfe3-4126-320e-bf34-43863ddd64d4 | -9.13268 | -57.81316 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 552e2401-a530-30ce-8e35-6fa5370aca87 | -9.132 | -57.81726 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 945ba4f5-1627-36dc-81dd-8699b4091dac | -9.13133 | -57.82135 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4491b0e-aeee-3751-bf19-6bad961e9ddf | -9.12559 | -56.99268 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d7ea5eb-5316-33e7-9365-98477dad495f | -9.12215 | -56.99212 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79e64656-f36a-3faf-a878-98642844a9a4 | -9.11171 | -57.78458 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 827c871d-c9bd-3dc0-a80f-e0851786febb | -9.11103 | -57.78867 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86a52ffa-b50c-3b27-b173-c9f39034fba8 | -9.11035 | -57.7928 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7503d982-0573-3cb6-9d3d-4ac17f543e3a | -9.10813 | -57.78402 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4f49325-e4f7-3de0-b156-64e5c3000ef2 | -9.10745 | -57.78811 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c2919d6f-9ea3-3f89-b1fa-a6e7453ef1f5 | -9.10677 | -57.79224 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d38c81b3-b47d-3c62-a90d-0aff2690b19f | -9.09453 | -57.55778 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29bfd7d7-2381-3a40-a862-4604f1b23fb6 | -9.09034 | -57.56123 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17e655cc-aed9-37f0-b715-c36aa3cc77cd | -9.08998 | -57.56429 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7a9ea06-7888-391e-974f-67bb6ffe266a | -9.06779 | -57.08538 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21659de1-fe4b-35e6-a21c-1b2b2fc8feb7 | -9.05985 | -57.11182 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ecbb9fa-5aaa-320e-a2f5-d62114ccff8b | -9.05922 | -57.11567 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6144fe8f-aa6b-373a-ab28-874b5936cef4 | -9.05781 | -57.11139 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adc929c3-f5c5-3d83-84b6-ffaa91fc2c40 | -9.05719 | -57.11525 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a60043eb-018b-36ff-8eea-b776e1803f81 | -9.05638 | -57.11127 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eea09ed8-838c-362f-941a-e7a1d266241d | -9.03296 | -57.15495 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebe956e1-e978-35dc-ac5e-2f9a939e58af | -9.03229 | -57.11511 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cf37570-dc3d-32b9-9445-e59a9b257694 | -9.00662 | -56.81715 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README106.md)
