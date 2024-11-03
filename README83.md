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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54117a80-b30f-388e-955e-f04146a49752 | -1.26288 | -55.69668 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2dfb9519-1c55-3bd9-a72a-f554581c6f1e | -1.26218 | -55.70119 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| faca65f5-19d8-375c-bfaf-edae0b3b9db9 | -1.26146 | -55.70576 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f4ff18f-bbe3-3657-8064-39956015d496 | -1.26073 | -55.71045 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d49e39b-829f-331a-9633-9e115930ed0f | -1.25904 | -55.69131 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4587ee05-16eb-3740-8702-2a4cafbdb449 | -1.25833 | -55.69588 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a329ddea-33e9-3055-9693-5bfb09822ce6 | -1.2576 | -55.70051 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec586769-b251-3c70-bb65-920609536b0a | -1.25688 | -55.70516 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ddaac527-283d-3d5b-bf59-c9f4b95440cb | -1.23239 | -51.95166 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bcb4eaf-a7d3-3bf2-a0ea-0fb8af6209f3 | -1.22386 | -55.82749 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05c94655-18bc-3c5f-97e2-d6ee6ac80a59 | -1.22166 | -54.14881 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8773a9db-b76d-30b6-ae29-e957e6874576 | -1.21934 | -55.82674 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9beb2a5c-0771-3ad5-b25e-dff6e552cb88 | -1.21906 | -54.16594 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c14448d-ec58-3cec-b968-6dd28e404fad | -1.21863 | -55.8313 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 314539fe-aef0-3e9d-b5e3-e948d37c1b66 | -1.21792 | -55.83588 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f1b9bcf-a761-30f9-868c-96f1fa39daff | -1.21405 | -54.16464 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d133918-1421-31ea-bec9-db115ff68d04 | -1.20818 | -53.91155 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8072730-3d4f-35fb-8504-64e4c7795431 | -1.20248 | -53.9142 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebed607b-c756-3276-af9b-0f9a8362f262 | -1.1992 | -53.65797 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d209a4b4-770f-322d-8c67-0ffebcee4eef | -1.19502 | -53.65006 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ed96d0d-2371-3e1c-8f27-aaae215e74b4 | -1.19447 | -53.65371 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9925878e-99ff-3f4c-9a9b-994a90ea8c5e | -1.18944 | -53.68682 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0beb19bb-1604-30ed-8691-7c2a04f141a4 | -1.18892 | -53.69021 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b93d64a-cbf3-3acb-87fe-f50eb336e068 | -1.18518 | -53.67947 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c3ed30f-f4f8-343d-9295-92e866d23269 | -1.18468 | -53.68275 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0dff699-63f4-3aaa-9ac7-f4223344fc59 | -1.18418 | -53.68609 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28b5f75a-1997-3778-a37b-86e24203b34e | -1.18366 | -53.68953 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7021e72b-3880-3540-be60-110dd0babb4d | -1.17949 | -53.68157 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5db4159a-9f39-3386-9b6e-95c708b59cc6 | -1.16675 | -54.17742 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0807e84f-c894-3b13-9707-3da073dd5abe | -1.16629 | -54.18035 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e565a3aa-8d3a-31b9-8cb7-48422866663e | -1.16126 | -54.07844 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce106372-880f-3f03-8a82-cc0c21b456a7 | -1.16079 | -54.08146 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0098364d-7a71-34ff-afb7-f4d01effba15 | -1.16032 | -54.08449 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c83c57bd-fb91-3118-94dc-eaafefe675e4 | -1.15985 | -54.08752 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 660e837c-0606-3df0-9fb5-d453001abe17 | -1.15938 | -54.09057 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fcb1735-84f3-39e3-8ac2-bc4484d1f488 | -1.13664 | -54.10267 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1490a9dc-dd51-36ff-aadb-ab768268c9da | -1.13153 | -54.10194 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a17f96b-90ba-3fea-a5c6-b505730b88f6 | -1.09306 | -53.65069 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04c03cbe-598b-3c6a-8653-c0a81024b926 | -1.09257 | -53.65393 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65790d55-2a08-3296-8b5e-326daf4305e4 | -1.08827 | -53.64684 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 573f9e4a-304f-3727-a099-e33a7c63e3cc | -1.08776 | -53.65017 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8d3a3094-075d-3125-a0d0-9c3c0b214391 | -1.07309 | -62.65009 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29f9f3f1-7853-37f7-a53d-e0bf272764e6 | -1.07201 | -62.65694 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c6235c2-39c0-3837-bef3-f3c65a44b0ba | -1.06871 | -62.65643 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e701adc1-7f91-3644-aa70-155d34f39185 | -1.03202 | -53.73068 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cffe4733-23d6-33e1-ae46-e925e139fa86 | -1.02624 | -53.73345 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b7f1ef1-f05e-31fc-9d82-edb5babf8498 | -0.77706 | -62.89182 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1c0e413f-6504-38f1-a6af-60df64bfa905 | -0.77652 | -62.89526 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 275af7d3-ebc5-3f59-94de-ebeee02f3e58 | -0.77321 | -62.89474 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf6a3f51-91af-3d4d-a7fc-e4014e87f15a | -0.76936 | -62.89767 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37ed95cc-6f20-31be-83fe-c8e0bd70c999 | -0.76498 | -62.90403 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bf5eeda-4594-3190-b3d2-6fc7f85b28fb | -0.76167 | -62.90351 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90e1bac8-6bf0-33ee-b4f9-3f75bc07168d | -0.76113 | -62.90695 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65359d2e-a3b1-3cca-af7b-d6a3ee8438f4 | -0.75837 | -62.903 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc3d0d46-f336-3bcf-be65-7c4f33d635ae | -0.75783 | -62.90644 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3df3b206-fe79-36ea-b368-f8f5406097df | -0.75675 | -51.96021 | 2024-11-03 05:31:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5c9c8ef-3d88-3b6a-b2f7-cb3a8f13d9dc | -0.75452 | -62.90593 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a02538ec-e528-3cd3-9304-0a1b13744d7b | -0.75284 | -62.8951 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a038bb3-1c8d-3a82-9310-e924d170f19d | -0.7523 | -62.89854 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72db2cfa-705f-35d4-84ca-34f85ce6f5f4 | -0.75176 | -62.90198 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57aa324e-cd98-320c-a2c9-d48df9505bd0 | -0.74953 | -62.89459 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 089175a5-3c96-3119-ad37-06f24a287a5c | -0.74899 | -62.89803 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d79fe72e-a1ae-36ae-ab07-2fe32f9eef70 | -0.69953 | -63.21207 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49d4bb3a-91c2-3c7f-b449-2ad235553338 | -0.69621 | -63.21156 | 2024-11-03 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eef93de-b1cd-3a47-bcf6-ce54db634e8a | -0.68159 | -51.67886 | 2024-11-03 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04fb0419-9466-3396-9b8e-0299ba596960 | -0.67563 | -51.67801 | 2024-11-03 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4742faeb-e09d-3213-8de7-c664b6c489f8 | -0.67495 | -51.68236 | 2024-11-03 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 914893a8-1970-3621-9ae3-b90fb9460464 | -0.67359 | -51.69105 | 2024-11-03 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b210993-8580-3650-8f38-2a8fabea6a78 | -0.11623 | -51.56508 | 2024-11-03 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63961981-0815-34ad-85b6-e1bd5ea6ee62 | -0.11556 | -51.56944 | 2024-11-03 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bf811bf-45e2-3369-ad9b-2caefe743833 | -0.11221 | -51.56765 | 2024-11-03 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6641fb97-7b9e-3269-a882-8feb792144e7 | 4.24469 | -61.02195 | 2024-11-03 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3db03274-9aed-3217-947f-75fd6cfd7285 | 3.51614 | -51.27523 | 2024-11-03 05:31:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c667105c-92b3-30a7-bbee-4196ab50a1c7 | 3.51546 | -51.27125 | 2024-11-03 05:31:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2635c9b5-3213-3cef-ba72-7a36ce291afe | 3.51042 | -51.27621 | 2024-11-03 05:31:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3a7504f-14b8-38ac-8f6f-104441583e0a | 3.36356 | -60.82438 | 2024-11-03 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e3b5dc2-e0ce-34f4-88de-23f5aadb3d5d | 2.81908 | -60.82112 | 2024-11-03 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 489e58d4-d778-33fc-ac24-288198095d72 | 2.55704 | -51.10643 | 2024-11-03 05:31:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c99c3084-4f5e-3938-961d-6c7ccacaa564 | 2.55633 | -51.1022 | 2024-11-03 05:31:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffa64e79-d66d-3b69-9617-213e6ed6416b | 2.55306 | -61.00872 | 2024-11-03 05:31:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08c8f5be-a040-31c9-83a9-8688069e8523 | 2.55046 | -51.10318 | 2024-11-03 05:31:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a22c97e-0c1b-38c2-b5d0-775edbef0a27 | 2.54387 | -51.09988 | 2024-11-03 05:31:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbfcbb62-0549-347f-8f4b-d59c9a59dfcb | 2.53729 | -51.09663 | 2024-11-03 05:31:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0835a9a7-84ab-33cf-a2ff-edc72809ec3f | 1.84874 | -50.52005 | 2024-11-03 05:31:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8f8cb99-08f9-306f-81e0-f82ef56f78f3 | 1.84391 | -50.52643 | 2024-11-03 05:31:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e86ba167-2c93-396b-8d9d-3a16328d2e97 | 1.84338 | -50.52576 | 2024-11-03 05:31:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4e70355-6df4-36e9-b139-faaea0a96187 | 1.84313 | -50.52164 | 2024-11-03 05:31:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c16a0b34-fa5b-3f8f-af3f-635e90379f05 | 1.84257 | -50.52097 | 2024-11-03 05:31:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97fc1cc8-24e5-34e5-b937-d067715ca96c | 1.84235 | -50.51682 | 2024-11-03 05:31:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fcbe141-ad85-3513-b434-e0e2f74b0db8 | 1.78486 | -50.4375 | 2024-11-03 05:31:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b3caf07-3d44-3591-b80d-df7d6989c51a | 1.72669 | -55.90981 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f9642f9-94d4-34fc-b0a6-59017824a4a7 | 1.7211 | -55.90237 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d0f3de9-a2c5-3bfa-938c-f084189cec81 | 1.72045 | -55.89831 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 881b3157-14df-3552-aa6d-4c7cb401647b | 1.13296 | -59.44559 | 2024-11-03 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 371e5e08-abf3-3343-bbd5-cb767e4d5683 | 1.12946 | -59.44614 | 2024-11-03 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e9ba152-b93e-34f6-8a9f-bf5224315136 | 1.12885 | -59.44226 | 2024-11-03 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3fda03c-0618-3493-9b03-432763d1937c | 1.12534 | -59.44279 | 2024-11-03 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfb03fd5-3d05-357f-a29b-86c3e531c9f8 | 1.12473 | -59.43891 | 2024-11-03 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d064bf9-ed36-3d31-b332-99869d151304 | 1.0388 | -59.60652 | 2024-11-03 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166360e6-dd6f-3881-80c9-3827d536b087 | 0.68059 | -59.80984 | 2024-11-03 05:31:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README84.md)
