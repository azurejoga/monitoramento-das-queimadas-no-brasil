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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00473030-d4b0-33c5-a422-1a7224c81e26 | -1.75093 | -56.19264 | 2026-10-08 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1691860e-d33d-3cad-ad81-c71bf9bea46f | -1.71791 | -55.44682 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3dfd49e-993a-3320-8e58-47c161dae7e8 | -2.10681 | -52.06075 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f1d07cf-795b-3ec7-87b6-1344abe0c425 | 1.34047 | -50.82983 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf0244a4-6dd3-3c62-9a21-d6e293a22b44 | -1.52652 | -54.79802 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 179d1d3b-dbc8-3ac0-86fa-9e1aeaf830fe | -1.14746 | -54.21482 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 344ca421-bc31-30e1-8575-283375ad8d27 | -2.36122 | -48.88547 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6de7f048-f6ef-3e7d-9ed2-594164f3af02 | -0.85037 | -51.8531 | 2026-10-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a32a851e-d511-3698-88f5-ef34f212d27e | -1.50649 | -54.8235 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bccf10e2-3384-3cad-bed0-a4329381d323 | -1.44317 | -49.58476 | 2026-10-08 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07a0a61c-cc2f-35b0-97db-022a99376b26 | 3.46928 | -51.75856 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4560464-2bb9-365a-a5af-61963de30b2e | -2.12447 | -54.80738 | 2026-10-08 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a1dc3dd-5c5e-33b9-8523-de494ece307d | 1.7188 | -55.60229 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f5f509c-ec18-3afd-9416-766c1f0fe6e7 | -3.18526 | -50.54994 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f23caec-3647-315e-b950-1886206f966c | 1.98772 | -59.93577 | 2026-10-08 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b057aac-62dd-3943-8e39-b311a0f107a1 | -3.20557 | -50.54956 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3f3724bc-5640-39aa-a74d-2be71ac40dfb | -1.23928 | -46.02973 | 2026-10-08 04:44:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ef03302-b101-3384-96fc-0a5cb79386de | -0.4145 | -51.72218 | 2026-10-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b967be0-d551-3412-96a0-dd274ee30c3e | -1.40347 | -54.60954 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 321ae3ec-9be0-3782-84fc-5c38b0d020cf | 1.62165 | -51.06193 | 2026-10-08 04:44:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b84fc952-21e3-3369-99f2-58287668ca6a | -2.04953 | -56.20414 | 2026-10-08 04:44:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0990f20-dfb4-3b30-bcb0-d4c87b514067 | -1.71905 | -55.43959 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fd07e993-b31e-3d06-bb98-93dd4b4b521b | 2.11518 | -50.8242 | 2026-10-08 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b563ce91-5ce9-3333-8f54-0694d86fc4e4 | -1.52725 | -54.53821 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2b7dfbae-9b40-38a2-89c9-073b4316df37 | -1.62692 | -55.12654 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec2c103c-87d9-36c9-ad46-1286e260b233 | -0.41732 | -51.72638 | 2026-10-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f20f63a6-8ae4-345e-b6c5-2b31f09d5751 | -3.29176 | -49.51341 | 2026-10-08 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cba03cee-0c5b-3d5a-9b7e-59d87798f6ea | 1.32856 | -50.83586 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 146cde1d-55ff-3da3-9923-9866ccb7aaee | -3.17253 | -50.45309 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 78e6f5a3-661d-3449-bce9-6ed71f1e1ea8 | 2.44427 | -50.81803 | 2026-10-08 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0dbd30c-d388-3a17-b74b-f7e4c98d8e46 | 1.32688 | -50.84702 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04194826-9370-3ff6-8d4e-5679f193f54b | -3.16647 | -50.44865 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8ce50dce-5d8d-3e66-b4f0-c6e40de5f9e9 | -3.29041 | -49.12966 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a617b81-2042-3bf3-a989-ba5c93d091bc | -1.79733 | -47.85117 | 2026-10-08 04:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d178fb1a-b449-3657-ad42-147fe7a615bc | 1.08408 | -50.77527 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb9ece23-7003-32c1-9b4b-731ff42720a2 | -3.18249 | -50.546 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3520616-24e1-3bdd-b81b-32fa23992c72 | -3.24206 | -46.95934 | 2026-10-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c03af27f-81c6-3e3f-846d-8265824b3e87 | -2.40331 | -51.30335 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab223ce6-508d-37dd-adec-40269d07f960 | -2.99055 | -51.05041 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4dbd559-36cd-34fd-915c-9f478ae6dff6 | -3.07453 | -51.23397 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7843749d-3ad1-3b3b-85e6-6848d30bbcc9 | -3.8174 | -44.60187 | 2026-10-08 04:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5184fd4-577a-3536-8880-ab43145807d3 | 1.69831 | -55.61389 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0f34550-595c-3bd1-8fbe-a4a052881339 | 1.32517 | -50.90187 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91801d91-682e-3f9c-92b3-5a4918d4a834 | -3.16371 | -50.44471 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a0d405f-2998-3c8d-aa66-567626961d80 | -3.18035 | -50.55971 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc36c2b8-9792-3b44-82b0-ac7cb95fc47d | 2.44819 | -50.82111 | 2026-10-08 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7e25cc0-65ba-3718-a6c7-82dccca54dcc | -3.16761 | -50.59269 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| e169e9aa-da24-3378-bad2-eff795421e76 | -2.30961 | -50.46479 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b21c4a3-64ce-3a9f-8bb8-d3191f555b4f | -1.48111 | -53.61707 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26e65b3f-a4b7-3ed3-bd2f-d7cca37658e4 | -1.18447 | -54.1773 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7fab319-768d-3df7-9b88-d161e523652c | -2.51044 | -48.34604 | 2026-10-08 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efce63be-0db6-3fb1-8aba-edfb5f7ae9da | -3.04186 | -47.46339 | 2026-10-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3a10fa0-3b04-3c56-9559-acbf64fba01c | 1.87087 | -50.88739 | 2026-10-08 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7f8ef45-e1e2-365a-8c48-7ee32802bd99 | -2.25308 | -51.93416 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a9836ea-27cf-30b4-b9d7-15ecd5c2f3f5 | -3.19131 | -50.55438 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d3fbe45-fb08-300f-acad-88c70f62d347 | 2.11237 | -50.82829 | 2026-10-08 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66b33829-be04-3e5e-bbda-2020304918e8 | -1.19831 | -54.21099 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f8d4e96-d9e6-352c-8b9c-e4bfb2247ea0 | -2.99109 | -51.04696 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cd3ac16-7024-3638-b7ce-3c894a46e824 | -3.1963 | -50.56568 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 499ba796-7429-38ed-b1cd-b8963f00a994 | 3.54312 | -51.27567 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 55d478ff-1a40-38a1-93f0-09fb9dc38044 | -2.56535 | -50.68074 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40dda940-0265-3fa1-8a82-cee848f7aa6d | -1.44088 | -52.85268 | 2026-10-08 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a22c2b3-7bc9-3093-963f-1f9a1945a024 | -3.19737 | -50.55882 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b4c6a0d-8f53-34e4-93b7-78064fc24310 | -2.04416 | -56.37932 | 2026-10-08 04:44:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b37a47fc-c7cc-3274-bc7b-a800a6d24d3c | -3.193 | -50.56517 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1009a57f-cdf8-3c3c-8b66-c4b3874c61bf | -3.17414 | -50.44281 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2c21f9de-be15-342e-9a2d-626c6a3078bc | -3.19407 | -50.55832 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90d02584-67c7-3abd-85c1-4e14763a30f3 | -3.17786 | -50.54866 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3164ef3a-1a9d-371f-94f9-28b4d03cc627 | 3.52292 | -51.25932 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9998c1be-7423-38f6-9f7e-10fe0ff6c668 | -3.27585 | -50.03321 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db041a6d-4b49-30e9-a8a6-e30f6fefbdbe | -3.17966 | -50.45068 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0d6808a8-c396-306e-8a0b-3ecd594a4560 | -3.16378 | -50.59561 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6751dae8-4e63-3972-ae92-1423fc984c85 | -1.88461 | -55.52583 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd291ff2-1c23-3de3-a20c-3861d89e18fe | -3.0006 | -51.11966 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bab2cb88-de4f-366c-8662-50bb6d2f082e | -2.78525 | -51.66879 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bad7f52a-dde8-314e-b29d-5f4f5a49923d | -2.22082 | -53.70564 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88405981-ea92-3d2e-b9f7-ce7b0401f007 | -2.26125 | -47.00335 | 2026-10-08 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19068f64-2ac7-362a-a6c7-96d1875db585 | -3.16042 | -50.44421 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7be9af4b-ac06-3899-8f89-a8c477944eb0 | -1.50807 | -54.81338 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2c701871-3427-3484-8c3a-5aa11843511e | -1.53732 | -54.54971 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a649c7b1-345d-38f2-aa69-20dc3356b562 | -3.17122 | -48.61489 | 2026-10-08 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bf049ec-f08f-3229-86ed-ae355d68891a | -2.30854 | -50.47165 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8740552a-b252-3a73-838b-476f8e0b9b86 | -1.5188 | -54.56661 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6bbe4315-cb3e-3a7b-962f-20c17b842e40 | -2.25251 | -51.93777 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b967df12-6008-326a-b25f-252584949719 | 0.98783 | -50.02536 | 2026-10-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46f55768-a51f-3946-a87f-a4b26924e9f3 | -1.47813 | -53.61209 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ab671af-2880-39a0-aa9d-ae472c69b5f8 | -3.19791 | -50.5554 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2af957e8-a5f9-36b1-b585-7ba7faaff92d | 3.12883 | -60.64046 | 2026-10-08 04:44:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c3be2c9-da16-325c-a44d-aeaf4ff09202 | -4.32017 | -41.237 | 2026-10-08 04:44:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 68a51c55-c3cc-3ad5-8dae-f4899937ae9f | -1.62636 | -55.13004 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9976f0b-c4a2-31f2-b4d7-ff2edff99185 | -1.41974 | -55.7178 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6327850b-3780-36ac-9c90-23a1c666b971 | -1.2937 | -54.56589 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29a0b7d0-61d1-3566-ba87-2832d1b391f1 | -2.69341 | -49.04939 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43c4c756-e4eb-3ab9-bacc-d7aaf111d86c | -3.47459 | -44.24054 | 2026-10-08 04:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abcf5274-d2c2-3538-a42f-30bbfee28eda | -2.03966 | -54.48533 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 98a5c15c-44b5-3eaa-8e29-f113b9b6f4d0 | -1.38103 | -56.89496 | 2026-10-08 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e41d2c02-d6b6-34ff-9cb1-c0c36ee721fd | -3.21109 | -50.55743 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0370fe2b-9d74-3c5c-b9ec-664e9a083061 | -0.04825 | -50.82534 | 2026-10-08 04:44:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 778ecdc6-2da7-3fdd-83a3-7ea2ba1e0dd7 | 0.73271 | -50.6608 | 2026-10-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00b6db6d-db73-3804-979d-ff049d0c4075 | 3.53446 | -51.52028 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README79.md)
