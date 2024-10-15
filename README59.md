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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 749598d7-c663-32b9-9c0e-ef55d29288a5 | -8.45913 | -47.80143 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2fc107a-a77c-3040-a300-1bbe97b1533e | -8.45875 | -47.80147 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 477c12c5-e25e-33e6-9490-16467cb0e079 | -8.45859 | -47.8051 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16295d49-18ca-3119-91f5-c2ef0ae15927 | -8.45824 | -47.80515 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ec4ede7-82d8-3c1b-86b9-ab4958a75e10 | -8.45805 | -47.80879 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54909160-3a74-3ba0-adf4-6a786943e2eb | -8.45772 | -47.80885 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3acece6c-472a-39b5-b904-8491a59e80a3 | -8.45505 | -47.80082 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a422fb4f-23a4-313b-a29f-a265181b39a3 | -8.45467 | -47.80086 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4a4b663-2579-34d1-9b16-45af7d9d567e | -8.45451 | -47.80449 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 333be7e2-a68a-3f52-92ed-faf47c236bad | -8.45415 | -47.80454 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4cd4128-8389-30e0-bd1d-4ef5c90b3a94 | -8.13464 | -47.57579 | 2024-10-15 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65df2a77-49ef-34b0-91c2-1e8e659f780b | -8.13051 | -47.5752 | 2024-10-15 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66f64afa-e646-3edc-a8ef-2ff21010483a | -10.1698 | -48.94231 | 2024-10-15 04:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cda4d2b5-acf0-35a9-b531-e6c541d5aac9 | -10.14245 | -48.82534 | 2024-10-15 04:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b94be338-202c-3fcd-88fb-c1a671d16bc5 | -10.13854 | -48.82478 | 2024-10-15 04:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4064a587-2afa-34c8-86a1-a23a909eb1f7 | -10.13824 | -48.82668 | 2024-10-15 04:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8d578e2-846f-3386-8605-def72a2fa4e6 | -9.60145 | -47.73515 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23b550f8-f81f-37b0-a81a-f06f33a754b1 | -9.59998 | -47.71528 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15c4a5e0-f19d-315a-a761-3bf8726c52f5 | -9.59945 | -47.71911 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5485bfbc-c953-33bb-99e5-d8bdd2c82c40 | -9.59727 | -47.73458 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45e4808c-223d-3db2-bb29-c8522af63837 | -9.59526 | -47.71857 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aede7312-6e21-3cfc-845b-572db46b9dfd | -9.53324 | -47.63515 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2af24a07-72b9-349f-a779-c08fa9412ff8 | -9.53154 | -47.79549 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0233560-c05d-371f-baa5-4c9da3ab150f | -9.52793 | -47.79113 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 478a95dc-2665-3bfb-87f0-372a5193c52e | -9.52739 | -47.79485 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37bb6c59-31e0-3e42-9601-4a4d09f80959 | -9.52429 | -47.78692 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0da6e907-9a8d-3dff-b147-a4210bfeb5b7 | -9.52376 | -47.79064 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 134f0445-0d8c-3bc9-9993-694b2a7748ac | -9.5227 | -47.79802 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79cc87d3-63f6-38a4-acab-0db9995fe79c | -9.51855 | -47.79741 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0f53caf8-7622-3b42-95ba-810ac2b7a396 | -9.51802 | -47.80115 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85cbc21a-942d-3f72-81eb-356a1b148843 | -9.51536 | -47.6405 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0746a741-fcf7-38d2-995b-e0d6ea06eee8 | -9.51388 | -47.8005 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0e43fa4-6ed9-35d0-8860-7b2c423a713a | -9.51334 | -47.80426 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67de9fdf-4e73-363b-9428-c623a271ccd8 | -9.49924 | -47.81405 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18652a75-871c-3695-a030-9efebd28cad9 | -9.49871 | -47.81782 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 619f2f66-7768-31b9-9f24-834cdbdf69db | -9.49817 | -47.82158 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e10f436-c13f-374b-b2c3-52ec6eeff3c0 | -9.99692 | -48.86245 | 2024-10-15 04:49:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b94e71d-9ebd-3263-accf-c28b64315adf | -9.89584 | -48.75915 | 2024-10-15 04:49:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d826a7f-ec4d-3b19-aedb-ce803ad73df7 | -10.90208 | -48.71886 | 2024-10-15 04:49:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 801d0c1b-892d-3a1c-9fcb-170b19a46a11 | -10.90144 | -48.72334 | 2024-10-15 04:49:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36c1b8f7-5a92-399e-a5bb-6efff35b25e5 | -3.46469 | -47.67097 | 2024-10-15 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7012089b-f1a2-36a1-9622-446df9b6f46e | -4.67031 | -48.50341 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ffb26ef-b63a-36b7-ab41-9fb2d3103bc3 | -4.66799 | -48.50476 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89c25387-62ea-3e49-89c6-90d9aa88cbab | -4.63771 | -48.74818 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e912778-b701-304b-b39a-5c1df34553ef | -4.63764 | -48.74952 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 390512fa-ab01-3cf8-9f9b-b0c1e28d6901 | -4.63556 | -48.5181 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a482ef4-aa84-3c8f-8716-4610deb802aa | -4.61959 | -48.67181 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c47082f5-3c98-30f8-96ec-5cf23a48fc82 | -4.61159 | -48.67494 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ec545b8-4fc4-3b7b-aa1b-e410080ea401 | -4.41541 | -48.711 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1efb1847-cf51-3e44-858a-87a76c9b6b85 | -4.41304 | -48.70209 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61fdbb54-e57b-34bd-873d-eb8eba93ad47 | -4.41109 | -48.71466 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82ee8f67-e364-3b41-ba1c-fd651b37ae01 | -4.37426 | -48.61201 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64c771d0-bd11-3d5a-b7d1-57d7c7a93ce2 | -4.32793 | -48.62461 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e409568f-2b6a-3606-814b-b248e4174020 | -4.32726 | -48.6289 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b2e7056-c08f-3eeb-83e4-1ac02b00eeac | -4.32688 | -48.62705 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fe1179d-89ab-3c9f-b67e-5e77d2bb3c7f | -4.32624 | -48.63134 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09f62e75-b819-3c73-b5aa-b5aac73821ea | -4.32359 | -48.62833 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2af059ee-241d-3df4-acaf-06a09432b8b2 | -4.32293 | -48.63261 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e951f82-8dd1-3de3-be07-f33b4ef9e16d | -4.31926 | -48.63205 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 723632a0-80d1-3660-b038-b76ac3a09203 | -4.31559 | -48.63148 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 622856ec-967b-37d3-8cf6-19534c7dc00a | -4.28557 | -48.63133 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 788ec7f8-bba4-3ffc-bc99-1c7cd3599a6a | -4.27811 | -48.22103 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7712fb8-f286-33b0-a230-b7beaa9c7222 | -4.27742 | -48.22553 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de56f460-3193-3ffb-af54-cd5b5299df44 | -4.27561 | -48.64735 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e47dcb2b-5105-3c0d-ad1a-c271be2fae0b | -4.27436 | -48.22046 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47fb6373-6e16-3b86-b3d9-29ccc6a51c80 | -4.27367 | -48.22495 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be2f5b03-80b1-328e-ad0d-a9d91b537e2e | -4.57615 | -48.01852 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0aa60026-3123-3d19-bcd7-bc49d044cc58 | -4.57233 | -48.01795 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c3e8161e-61c2-3e3c-a358-47c3baacb1fd | -4.56852 | -48.01736 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a2d4b031-0601-3dd0-ade2-584bf9490989 | -4.56782 | -48.02202 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7d685c2f-1e91-36e4-9482-c7c175737d1e | -4.3863 | -47.76222 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 4177bd6e-8923-36c9-ad08-0e4d74c315e0 | -4.38243 | -47.76161 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8449dccd-edfc-30f5-b578-f808da46ec3d | -4.27872 | -48.06674 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a2e4590-fcad-392e-91a4-980b94f91dd0 | -4.27493 | -48.06618 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c17f5330-ba3d-3cc6-84e9-a03ff82c066f | -4.22646 | -47.85487 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2eb6370-2283-318e-bc8e-316445c4118c | -4.22574 | -47.85954 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6a82765-86e2-3119-b43e-d5ac45afc5e5 | -4.22449 | -47.85689 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 48d6de94-59f4-3858-a853-4d2d297afbaa | -4.2226 | -47.85442 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f951f2a-70df-37b2-b739-b46e24e4945d | -4.22188 | -47.85909 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e2cc8eb-a13b-3a8a-90ec-97a958330ac1 | -4.21875 | -47.85395 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe05f90c-60e3-35ae-a759-9eb326afc79f | -4.09264 | -47.94288 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1398036-4407-3531-b266-f886514d8a14 | -4.06198 | -47.91396 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d472548-f770-379a-9aee-6843f9cccc31 | -4.06127 | -47.91862 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 834a41cb-9834-396a-9779-db89dac6c419 | -4.05815 | -47.91344 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4df40c62-d72e-3471-9001-f61eefcfa087 | -4.11905 | -48.27702 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 523344f7-fc52-3272-ac31-6421e35fa226 | -4.11836 | -48.28152 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 926e8a31-8e4f-35c4-b2ca-ea4c3f656c07 | -4.11701 | -48.24017 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fd18392-146e-3d81-932f-3d825eb95824 | -4.11464 | -48.28089 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7636731e-ec8d-3019-a959-36470a8aeef3 | -4.11326 | -48.23965 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f1bf9ad-e2f9-3a82-bd15-33fb2e62bdc4 | -4.11091 | -48.28029 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d72fe51-0a35-3264-b35b-7a3f71f17ff6 | -4.11023 | -48.28475 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c9a467c-6998-3a05-a7de-d8a37a76016c | -4.10951 | -48.23907 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4293c32c-e615-32aa-bc85-d3504f6fdee2 | -4.10717 | -48.27974 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1fac65f-567b-38ad-be1c-33b6b5411ab7 | -4.1065 | -48.28415 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad690233-8d9a-3ce0-a358-73e7a9127718 | -4.1044 | -48.24755 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 731d0480-b48e-396e-bcf9-01e3727037a8 | -3.92871 | -48.3523 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7ae93acc-1cbe-3094-b22b-a4d61e3555c2 | -3.92804 | -48.35665 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 006ad696-7c93-32b1-8975-ebb2c47f0ccf | -3.92501 | -48.35172 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| eca6139d-ba70-38d3-9297-05f0d78e54ed | -3.92433 | -48.35609 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c33bdf27-fc66-36b4-9705-1418aa7ee5be | -3.92365 | -48.36045 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |


[Clique aqui para ver as próximas entradas](README60.md)
