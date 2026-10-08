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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 946950f9-3504-355d-b944-72e55d5fc9d9 | -3.18588 | -50.56757 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7df2224d-b26d-3b60-a5ca-3be2dc231eda | 4.31599 | -60.36012 | 2026-10-08 04:44:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8284f307-153a-3efe-9f34-988fbf5c87c2 | 2.11573 | -50.82778 | 2026-10-08 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09ea2bc6-6117-305e-ad6f-77645ddc3513 | 4.27041 | -60.03942 | 2026-10-08 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ec7e2707-681a-3fff-97c5-1e7d52836b26 | -3.28843 | -49.51291 | 2026-10-08 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12da88b7-d3a8-33fa-ba39-28dc9571f42b | -1.74078 | -50.14467 | 2026-10-08 04:44:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b63795-35cd-3c6a-9b06-447e4d28a708 | -3.16977 | -50.44916 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d0e8dcd4-bfff-3c9e-bcd1-920373d09244 | 1.98717 | -59.93206 | 2026-10-08 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed26dfb4-3faf-3d76-8382-610461dd998e | 1.7696 | -55.54755 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c5c8772-1bcc-3d45-9c37-8e420e81c2d8 | 3.12763 | -60.64571 | 2026-10-08 04:44:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ed38a8c-02a0-3bc4-aa5a-8ba849f4e756 | -1.29447 | -54.56102 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9c6d2bf-4b96-3673-91df-74a16e240ade | -2.69061 | -49.04531 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b736af9f-cfb1-34da-8d71-5b93e90ec782 | -2.01806 | -52.11042 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 625ac8d4-2455-388e-b4a0-4e6e9341f45c | -2.04968 | -56.38345 | 2026-10-08 04:44:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2d9e93d7-2993-3eb9-aa4c-f5632753931f | -1.45623 | -54.78441 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba96d586-847e-3cb6-b9c5-236310ad1938 | -0.42015 | -51.73056 | 2026-10-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ada7567e-3de6-3b03-953b-87aee37eedb1 | -2.36176 | -48.8819 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3afcbc9b-e892-35df-b3ac-498f42c253ac | -1.75684 | -55.1219 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7f1ddff-0ce3-3bf0-a083-6ea101ae0a6b | 1.64983 | -50.97657 | 2026-10-08 04:44:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42176137-d6f9-381b-8de9-9046918131af | -1.47447 | -53.61151 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a391bd22-f115-3b27-900c-27093ab8502e | -1.47541 | -54.63939 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3b26da6f-903a-3ffd-b319-0a73afc49874 | -2.41365 | -51.30149 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a680779d-031c-3ec3-9e86-e0967009b686 | -1.75159 | -56.18858 | 2026-10-08 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f5ea250-65bf-3e08-bf18-0f3d8e6e5b83 | -3.17914 | -49.44916 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e25bfc37-32a3-3654-9098-96f5f1e7a593 | -1.71496 | -55.43898 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b03a8b0-2b1c-3d87-b2a2-e03ce4f419b0 | -3.16425 | -50.44129 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c815172-bea8-3998-a960-18460015c6fc | -3.3033 | -49.12816 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e761184-f89e-39ab-84f3-d61623025cf5 | -3.43799 | -44.33469 | 2026-10-08 04:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68956343-5e45-31ad-b07e-f4f0f57c833a | -3.17636 | -50.45018 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 14d509aa-08f5-35a5-972e-3641d8b68de6 | -3.17146 | -50.45995 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d77310c0-6255-3c08-85e4-413e36c83b80 | -2.98153 | -51.24084 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 881478e7-c98b-307a-ac2c-5a4839da25d9 | -7.21267 | -55.09543 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0cbce6c2-d062-3260-b30e-b7349840ac18 | -3.65388 | -54.05947 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40564c82-2934-3ccf-830d-1a6e643616de | -3.00045 | -54.13459 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7589564e-ac40-36b3-b92f-621733f91b18 | -3.10695 | -54.17213 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f7dccb3-d847-3314-a4e2-abf02b1a9bd1 | -3.10596 | -53.75837 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c461bde-4d39-39b0-9b1f-d04cc4fc643d | -11.7211 | -43.65963 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f600373b-d3db-3a54-a2fb-1650467d6e99 | -7.50286 | -54.99534 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7555a0bd-4510-33a0-89f9-f1281a9c55b7 | -3.54829 | -54.66822 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0323ae74-a226-3600-aae1-775dba2be969 | -4.14194 | -54.03135 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 08087a12-c930-3b78-ae78-11287ca1c9e8 | -11.3205 | -46.68688 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 403f9948-3343-3648-89c3-df7206b96527 | -6.6281 | -55.29613 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d161397f-2e51-305b-88e2-04d7ca6fb411 | -4.2362 | -49.98115 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13779240-3c7a-3929-8676-0f7a30daecfa | -5.6787 | -46.35477 | 2026-10-08 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22132131-6d8a-371a-befc-7232139346bd | -2.58797 | -56.17112 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9dd9df0-3d36-38ff-b0c7-0a5b24f88ac6 | -10.77487 | -46.57349 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1d8b374-72bc-3127-a727-eb8e9d71b35e | -3.03958 | -54.52213 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2787054-c788-3a90-a44b-1272057111a6 | -3.50014 | -51.68663 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4c6bc4e-37bc-3db9-8830-c957f358bb74 | -8.41346 | -45.79071 | 2026-10-08 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 009da74b-a66d-33d6-bbb2-49f51b6e884a | -3.26489 | -54.05273 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5ad53ca5-397d-3098-9b5d-087f723a1be2 | -3.66071 | -60.63028 | 2026-10-08 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1d3c0e5-25ec-3d93-b9a9-4bf7d8e9a5c3 | -3.24538 | -56.80698 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab5a03dc-ef2b-338e-ab95-5b6666d22f81 | -3.58809 | -54.30364 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 625b5b1b-e05d-318e-b641-53576a224c3a | -3.26722 | -54.06185 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a4008dab-8df4-392e-88fe-f55fb599615a | -3.17595 | -58.64083 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50b8c10d-4c33-37b8-bcf6-12348917af01 | -2.98676 | -54.77806 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 170c4a80-4dbf-393a-9fdc-9f2e87788b3f | -6.32379 | -43.34965 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 82447f76-6097-35d3-b6cb-c0b6c4f71953 | -2.93778 | -54.16999 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d5be117-e140-3274-9006-88b251323a5c | -6.14648 | -47.93478 | 2026-10-08 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4fe240da-4cf4-38fb-86e8-c85dc07ecf99 | -3.73537 | -59.45015 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12e4a1e9-c2bc-38df-bb00-3f4c8594085f | -3.0667 | -54.37667 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d337abd-2667-3478-b276-9eafe71050dc | -5.74328 | -45.14729 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c310bb2-118d-35ee-9b4b-8a46e8567703 | -5.98823 | -55.36124 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6edb40c5-002d-303f-abee-3a68e4921b2a | -6.62634 | -43.73001 | 2026-10-08 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e5921f62-6d9d-3ffe-ac81-59c9295e1010 | -3.58165 | -54.67826 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 7de6bb01-9720-3eef-b746-8dfc4b3cdf75 | -6.30991 | -43.34222 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7922496d-9872-3093-802c-45c78dcba303 | -5.11587 | -47.12511 | 2026-10-08 04:46:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2267075c-e8d6-3597-86f9-42ef95ccb15f | -3.08954 | -53.71413 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66aa6a10-a3ea-301a-8bd3-b9e89032a0a5 | -4.45381 | -47.92026 | 2026-10-08 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4199f1fd-723a-39ce-b96e-ed4a0389b1c9 | -3.25964 | -54.67648 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 96511a39-cdb2-3a96-9cd2-50de53574742 | -3.11614 | -53.76424 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fed4b66-c487-380e-bb58-5694a763f952 | -3.02627 | -53.92523 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 177f762a-7328-3c63-b987-e6676ba1ddee | -4.54018 | -59.9255 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b3b4491-f7ac-3eba-a661-a8227c1d2c29 | -4.1584 | -55.1498 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c093f566-2d12-36f2-89b2-2ec8a61acf56 | -3.57849 | -54.31587 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5fd933a8-f055-3e4e-9cd5-d649fe413f24 | -3.20749 | -53.87281 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92e4ab3b-9b20-3dec-b142-07333ef1172c | -3.67545 | -55.9442 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 774ef183-6ee4-389e-806b-38f7d393646b | -6.13689 | -47.92472 | 2026-10-08 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 866e59c0-e0c4-3d63-9b82-87c9b9a6a25f | -5.22084 | -60.04662 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db193586-da73-38ee-afb3-4ec433c80a46 | -3.79003 | -59.37835 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26733155-536e-3346-8bf0-97f426ee3e35 | -4.31205 | -50.78302 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01b9c715-0f11-3ad2-bd11-9e364d8ebe27 | -4.45405 | -47.92094 | 2026-10-08 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1005b416-89c7-323c-a16b-8f8000f87538 | -3.68951 | -55.49102 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4282911-87d2-3034-8628-b952d1c5cce4 | -9.58817 | -54.63955 | 2026-10-08 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de322c87-412e-32a8-bafe-bbfc28883aea | -3.34183 | -52.51375 | 2026-10-08 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7278e11f-69cb-33da-8d79-3a963f50aea2 | -4.51615 | -44.0399 | 2026-10-08 04:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 562b66ca-182f-3f62-a604-cfaab2545b3a | -3.02334 | -54.13367 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f964a9f8-ebe2-3255-b74e-09c020172927 | -3.95959 | -56.12243 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 773f5ad6-0562-32d0-a1ee-3a766af34133 | -3.01642 | -54.10563 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 28a6b05d-cdd6-3396-a8bd-2e7034dbf59d | -3.23457 | -53.88997 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c31c2a74-3543-30cb-acdc-2ec9cf428834 | -3.29082 | -54.0067 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 52e4feaf-5cdb-3bfe-aedb-c4fd39d6398a | -3.06348 | -59.26986 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2f59661-b598-39da-ae90-f0fc22a28251 | -3.1356 | -54.36257 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e87655c5-c20e-3e04-976a-ed6402302a7b | -4.99206 | -56.14542 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6335e6d2-975e-32bc-be2d-ae7dfc7f0d7f | -4.80798 | -42.74821 | 2026-10-08 04:46:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b230f005-8d1a-3434-b785-ffdfce8c963a | -2.76115 | -54.10454 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ff43664-d2c8-38bc-a69c-e5263ef58132 | -3.0685 | -54.17515 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd520f53-72d8-3ad6-9329-d83986e427d7 | -6.35256 | -43.34351 | 2026-10-08 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19347795-3d4e-3953-9cfd-ee0629141cd5 | -3.54654 | -51.54304 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09f254e6-5dd9-3cc1-806e-784a93bb7caf | -3.05394 | -54.21814 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README81.md)
