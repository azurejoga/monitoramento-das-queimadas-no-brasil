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

## Dados Diários - Página 193

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33640c93-da7f-361a-80aa-9b93b75581f7 | -10.84587 | -64.18182 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a76773c3-11d6-3d6f-b3c4-d851b83d482d | -10.85128 | -64.17988 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98dbc75a-0715-3d41-9c5e-941d6bf187d3 | -10.85172 | -64.17657 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b2a6e0c-da3d-30c9-a524-fa690f92a1d7 | -10.86887 | -63.8858 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 915c4384-dd1a-3b28-b71c-001596ba5682 | -10.87316 | -63.89325 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d9ea328-8cf1-36ef-b64e-90572b6289c2 | -10.87358 | -63.89003 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d992cb75-4d41-3d87-857e-6448c3624ef4 | -10.87829 | -63.89428 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f2158164-adad-3cfc-845a-70d644b9ad3f | -10.87868 | -63.89128 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf1871a5-af58-3e8e-9f94-24c194111b04 | -10.88799 | -63.90049 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17bc792d-47fd-381d-b392-fbbd1e0e4f01 | -10.88975 | -63.90335 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60201ee9-77e3-3cdc-a52a-6ef323181f89 | -10.89018 | -63.89988 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57221958-bffb-360b-92f6-07da5036d43a | -10.89272 | -63.90454 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f759a20a-55d0-37cb-b73d-1b03bdb7d2ad | -10.89315 | -63.90126 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a8aa4bc-4cb9-3c9d-bb5a-26056f7fd748 | -10.89362 | -63.89768 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d33f562-34ae-3751-9c1c-31035f14f43a | -10.89493 | -63.90399 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d09b135a-f9e1-388b-85ed-d629060005ea | -10.89535 | -63.90053 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a04e5b34-b07d-3537-9bb7-82f3870fc3b8 | -10.89579 | -63.89696 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c38d43db-6c68-347b-88e4-fcc8d17909bd | -10.89619 | -63.89372 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5f0a318-c9d7-34c4-acf9-51cc4cab97e7 | -10.89657 | -63.89069 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f37f0bd4-b3d1-3d2a-b29f-bda50ea08371 | -10.89837 | -63.90154 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58b00130-d6b1-3ebc-b7d3-5252e6101c06 | -10.89883 | -63.89799 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a01e9ab-846b-390f-a04e-ba28960a7777 | -10.89927 | -63.89464 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d31fa0f8-883a-3e2a-a916-9df8c8ddbe10 | -10.90009 | -63.88845 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43037ffa-6100-3143-a156-d565e7b80710 | -10.90047 | -63.88554 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2287510f-329e-3d18-81de-9bddce0f9344 | -10.9022 | -63.88765 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1eed0be7-7876-3eb8-8fae-099431136dea | -10.90494 | -63.89154 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d437f1be-c304-37c0-aafe-851bb25c9600 | -10.90669 | -63.89378 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3248f97-64fe-34ce-9560-199420369cb3 | -10.90706 | -63.89081 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb7f2d92-9502-3ecb-bd09-cb2fc8d58e73 | -10.90777 | -63.88512 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5329714-d2f9-3ab0-9523-bf2456f78836 | -10.98146 | -63.96594 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94faa0ec-68d7-3092-8673-b548b5742fee | -10.98185 | -63.96297 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2553c55-4711-3a50-b335-acea8cd1c9f0 | -10.98226 | -63.95976 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92cb3aee-504f-327d-b536-5dd3b23b494a | -10.98309 | -63.95341 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e446ef5-9de1-3432-a902-efd8e7839ca0 | -10.9835 | -63.95026 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5097d782-a8a0-3b0e-87f7-f193641d8eea | -10.98391 | -63.94713 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f135353b-a6c0-33df-9bea-0aded9d2227f | -10.98433 | -63.94394 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00c94621-aa2e-3c30-ba87-066bf065aa24 | -11.45183 | -63.33658 | 2024-10-03 06:10:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc777fe5-b495-3f45-97b6-6a6da65a46a9 | -11.45679 | -63.34087 | 2024-10-03 06:10:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfcfe7ec-2c57-3ba9-9337-20cf6ea595f4 | -11.45722 | -63.3375 | 2024-10-03 06:10:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc8103e1-3be3-37f1-8c4e-0c42bb0a7a28 | -11.45764 | -63.33407 | 2024-10-03 06:10:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 548cc9bb-8272-30e7-b150-a3e4d49cd2e7 | -11.52298 | -63.70796 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42f10503-f407-3e4b-b03c-9e72539bdfb9 | -11.55129 | -63.73851 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf14e788-47e4-3db7-979e-d337cdd2343e | -11.55147 | -63.73565 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98b90a71-36dd-30bb-b2b8-4f9cf39cb521 | -11.55171 | -63.73522 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95ffdf6a-8d00-3e19-8236-a46c12ed3d0f | -11.55671 | -63.73663 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1bdce08-36c7-3200-960a-5f3a8bc713a1 | -11.55694 | -63.73623 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29e6d831-54ae-3d7b-9c1e-b089df568258 | -11.55721 | -63.77572 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 950122f1-8970-3063-9639-39489e9396ee | -11.55726 | -63.77624 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a29cd2c6-7551-3d41-b1ce-27138064b5a9 | -11.55763 | -63.77248 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d769d18-329c-3dc1-b485-09c48cfdee55 | -11.55765 | -63.77299 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a45b814-dc89-334f-9f1a-fbb19587defd | -11.55805 | -63.76925 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a78a6b31-1390-38d7-b653-b8b36f215ad7 | -11.55805 | -63.76975 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cffc5f1-4f2c-3dbc-8885-7a4518c4b8ed | -11.55844 | -63.7665 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1355c081-abbf-3376-a09a-64bf7556f45e | -11.5637 | -63.76727 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e18ef4a-1a6d-3106-a860-b1a9c3ab5a8b | -11.56372 | -63.76676 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c4498bf9-e74f-39e1-b491-b58467f8a81d | -11.58009 | -63.76453 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9d67ef5c-7885-3d0d-8c07-09e349f9fbfc | -11.58043 | -63.7618 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9d2d8c53-0fa4-389b-a59b-42b37eda3c88 | -11.61163 | -63.72621 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8dfa1bbf-20c5-3344-b065-533df371cc37 | -11.61205 | -63.72284 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6bea5e3-9bf7-3905-8b41-64861524ab9f | -11.61246 | -63.84753 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 137abeb0-2da1-39e3-b7ec-119cb9c952f3 | -11.61285 | -64.09277 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b16b7637-7094-3326-8506-7f6603e599bb | -11.61326 | -64.08967 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5399f20-e136-34d7-9eef-8ea3596bee07 | -11.61411 | -63.83448 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4d31c98-6ac0-3360-afce-36c8b10aa1fb | -11.6145 | -63.83137 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8202fb74-63a4-32e5-97de-10c5a127706d | -11.61494 | -64.09285 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb8222b4-abc7-3014-80d6-2d06ce197a08 | -11.61532 | -64.08974 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f788aa9-47f3-36b7-8334-996b2f67caea | -11.61752 | -63.97469 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0edd8107-a724-3e08-8b5e-536c50b178a4 | -11.6176 | -64.09656 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78fc435f-cb9d-3d97-b871-c631151342b3 | -11.61764 | -63.67789 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab59be46-01a9-316b-8883-f55410b92317 | -11.61766 | -63.84852 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59600fd7-0912-30c9-8863-e89f253c4c5e | -11.61808 | -63.67429 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a29c8e3-cc11-31f9-89c7-6b066f3814e0 | -11.61845 | -63.84226 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8908ccf2-622d-3bef-b418-76b1453571fd | -11.61857 | -64.10598 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ee56fda-eb10-3f96-b941-8f893c36045f | -11.61933 | -64.09975 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c794d52-8197-3a71-b967-ff83c0b99c19 | -11.61967 | -63.8326 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2f53cde-392f-398d-b841-6cf6c679f867 | -11.61971 | -64.09664 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cb4e674-aedc-344b-a9c4-a50a50f6635c | -11.6227 | -63.97543 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 641840b3-78cd-354a-aaa2-e679bcbaf602 | -11.62311 | -63.97229 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5573906d-1bb5-3f18-84aa-1cb808367f26 | -11.62571 | -64.03391 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6988c7e-4224-3b8d-8167-a2cf5b451730 | -11.62611 | -64.03079 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4d5694c-6d93-3674-b236-319e5e521bd2 | -11.62698 | -64.037 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d1904cf-4187-3397-a473-ccd8e0cb86d4 | -11.62736 | -64.0339 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02990695-a5a1-3c30-80d8-2d447b65f49d | -11.62774 | -64.03078 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85292c10-d6d5-3a4d-9b4c-99a37e631df9 | -11.63047 | -64.0378 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4e66292d-5ac7-3307-963b-e48f11d4f3a3 | -11.63087 | -64.03471 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7f045f4-e6b7-3705-9fa4-f7879a6b173d | -11.63127 | -64.03161 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e50f29c6-6ab4-3d20-9e19-238d150d3cf0 | -11.63214 | -64.0378 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 46200eea-ba32-3e45-b385-2513e7e12799 | -11.63252 | -64.03471 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7dc7c40e-bf5b-3480-b2ed-25d885e84f05 | -11.63563 | -64.03857 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1a72cf8e-60ed-3b67-9389-f125c21d2eab | -11.63603 | -64.03548 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 744b1260-f303-38cb-b4a4-32dec613c44e | -11.63643 | -64.03242 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62965e9d-4a0c-3686-8609-0b875efe1e2c | -11.63683 | -64.0293 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 719b169a-3eb4-3fea-b34f-db79e0d6a000 | -11.63768 | -64.03552 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11773f9c-a36a-368c-b55b-0f5b69310a5a | -11.63805 | -64.03246 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dee2c27c-7cc3-3680-a4f5-ed9befd29ba7 | -11.63843 | -64.0294 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7e756d93-4da1-3645-83a8-c9e9ecf0a666 | -11.65026 | -64.01881 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d587f5cc-80b0-36a5-b42c-0e2172bfb99c | -11.65492 | -64.02376 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a27ec5b-5d68-35ec-9d03-3821afd5efb3 | -11.66723 | -64.00945 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5908d11-3c8e-3943-8042-24c0834a8eb1 | -11.67319 | -64.00396 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f739b6b4-2c5b-313c-8b9c-ad0b0d687ab9 | -11.67329 | -64.0453 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README194.md)
