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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a028e288-2dc5-3f00-8823-d8b2d4332c00 | -6.6653 | -47.11229 | 2024-10-10 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fe79ab6-91e5-38b5-bc54-e9d096af2f04 | -6.58139 | -47.71525 | 2024-10-10 04:44:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a9dbe3e-4d20-39a9-9cc8-9bc0a73befdb | -7.76335 | -47.03676 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cab522a-b86a-3d9a-907c-5d4d23ee6870 | -7.68875 | -47.25127 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce9d7fb7-daee-3498-8818-2c3576fd1052 | -7.49097 | -47.20319 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 863c8dfe-a2b4-346c-a535-6d7d4cae36f0 | -7.24194 | -47.49826 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 871a3d16-ede7-3d79-ad87-6853d44b3c57 | -7.14124 | -47.7459 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15950bf4-e253-3a8a-8409-47fd2d5270e3 | -7.13758 | -47.74538 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cae1a515-b7b7-3e53-a1c1-e59ca7adbcd7 | -7.13311 | -47.75087 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 557df50d-58f7-38eb-ba86-9c82b4d9cc81 | -7.09734 | -47.86353 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d8910f8-c28d-3d70-a798-0c629fb25502 | -7.08813 | -47.87531 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f304729a-2a5e-3ffc-9f86-87c0a85f38e1 | -7.0845 | -47.8748 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c552d898-03d3-395a-aeff-8b4b7b98beaa | -7.0283 | -47.37659 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2076726a-6c08-337e-9048-56de39b3fb69 | -7.02766 | -47.38094 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13c848de-dc84-37d1-b630-19690e43f12e | -7.02156 | -47.37074 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c625ff70-ba9b-3055-8036-1c4961f18be0 | -7.01052 | -47.21207 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85a89951-80ec-3660-9370-260d17ea9ac6 | -7.00788 | -47.2301 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 147a77c7-da61-3253-9737-e4d846cd9ac5 | -7.00734 | -47.36389 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8c91fc9-f10c-38ca-b46c-23f659c4840c | -7.00611 | -47.21593 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 777d9004-11d0-3fa0-bada-c1892c3e5989 | -7.00105 | -47.2243 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dcfa86a-4389-3356-aaff-270e3e9b8a15 | -6.98479 | -47.38787 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9fe5e13-107d-36ea-8623-e34b0f79dc54 | -6.98283 | -47.40123 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ec0ff24-cb77-301d-bf9b-7bc783289678 | -6.97804 | -47.38205 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e817fdc4-e706-3805-bc89-f9fad25d121f | -6.97675 | -47.3793 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ffffcc2-7d08-34bb-9804-eaa2bfbd3174 | -6.97539 | -47.38826 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c18280a5-b3a6-3363-98d2-c07e07a035a5 | -6.93411 | -48.17504 | 2024-10-10 04:44:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69398b55-a737-32d6-9bb6-cf84e6105ddf | -6.93045 | -47.73191 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fbb26322-adc3-3c8b-ae7e-898cc6be04b6 | -6.92806 | -47.72282 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 45dd725d-991e-371a-a8fb-91770ae25a83 | -6.92743 | -47.72709 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd4146ed-80a9-3d11-9700-e50a8136288c | -6.9268 | -47.73136 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 93f153f7-6c2d-32a2-9d64-0d5302b59a34 | -6.92611 | -47.7108 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4c5867b7-270e-3690-aa85-95b360f7b7e8 | -6.92569 | -47.71352 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 09c1bc72-5761-311a-9ccc-cdda5affc1dd | -6.92544 | -47.71518 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b536ab3b-b7cc-3c14-bbf5-886f7144bc81 | -6.92505 | -47.71791 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc054ff9-1012-3123-ae2c-f0366ca2d010 | -6.92477 | -47.71957 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99535468-7ba7-3207-90c9-24331e5582a9 | -6.92441 | -47.72225 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6fad2653-1f57-33fe-93dc-4ed0342de6da | -6.85824 | -47.34518 | 2024-10-10 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7709e83b-38ba-3081-a1f5-56b9bfdd2452 | -6.8552 | -47.3401 | 2024-10-10 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66652d0e-35fa-340a-b111-f2ef7e4cd911 | -6.85453 | -47.34454 | 2024-10-10 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fb25c1d-a763-317d-a7d8-b640300e64a9 | -6.66906 | -47.1129 | 2024-10-10 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bfcb3004-6e7f-3166-ae27-a1f7051f829d | -7.94493 | -47.71695 | 2024-10-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 052443a8-2b90-369f-93d5-425242bda096 | -7.94428 | -47.72137 | 2024-10-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1a2c243-621e-3d4c-a59c-7a45259ee6a3 | -7.76263 | -47.04156 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6550476c-59bb-31f2-ba4a-1db38d4baa47 | -7.49475 | -47.20374 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aad5ca8c-5f89-3111-8c16-cf29fa890ef4 | -7.43726 | -46.96777 | 2024-10-10 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0efa978-ff83-35c1-a128-27c36bfcbf2c | -7.4338 | -48.36011 | 2024-10-10 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f9b34d5-604f-3780-bf0f-d3d2f8aef73a | -8.99055 | -47.73373 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6026ceec-fe40-355c-8644-6f8347366776 | -8.98681 | -47.73316 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a664b16-af95-3234-991e-4f8801ec7e51 | -7.96942 | -47.80556 | 2024-10-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07013e23-55f4-37fb-9a24-8eac339c7695 | -8.04468 | -47.19784 | 2024-10-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a04d5ca2-3cc1-348c-b160-067b186429f4 | -7.98163 | -47.62283 | 2024-10-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1f47196c-c1a7-3adc-a149-44dec2e50dc0 | -8.62445 | -47.22637 | 2024-10-10 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b087d74b-806f-36d9-adb7-8920d113830f | -8.49442 | -48.63741 | 2024-10-10 04:44:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09bf2d88-9a59-3d87-9247-90397313fe16 | -9.21984 | -47.5629 | 2024-10-10 04:44:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b97bab5f-053f-306f-9196-0d22e7dc1b4d | -9.20746 | -47.94001 | 2024-10-10 04:44:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6719e95-bac8-3766-b80f-c889cbda75d9 | -9.16821 | -48.71893 | 2024-10-10 04:44:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abf06684-a150-3dcf-8b22-768d6a37b623 | -9.10609 | -47.65488 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2a6405d1-bde6-3f77-b456-7c60271e235c | -9.09455 | -48.17495 | 2024-10-10 04:44:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbf520d0-5353-3464-bf45-9e52d0131146 | -9.09003 | -48.02775 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8666950-9c09-3599-918b-c88d6aafcc8e | -9.04346 | -47.81546 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0639b8da-725f-3abd-9b2e-2dc4d6af8c84 | -9.0428 | -47.81995 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37656606-2678-3ee9-b14c-0a83ca2ea7f5 | -8.98989 | -47.73831 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eae5dc0f-31eb-3302-8a77-5ca752d92d16 | -8.55249 | -47.82258 | 2024-10-10 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbfa8b4d-ce81-3151-80e3-5352c5ebccd0 | -8.54878 | -47.82204 | 2024-10-10 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a5804d4-4dcd-3996-b08a-deeaddae06d2 | -8.49796 | -48.63795 | 2024-10-10 04:44:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 648f4e6a-87d8-355b-8c64-98d0ddaa022b | -8.26838 | -47.85297 | 2024-10-10 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b89fd677-cc44-385d-a1ee-b911efc7def5 | -8.26773 | -47.85735 | 2024-10-10 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc6cbff2-e94c-38ea-99f4-bf195c4fdf06 | -9.36861 | -48.80481 | 2024-10-10 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 54b5f885-5075-3d2d-b514-12b9e765aa51 | -9.36447 | -48.80832 | 2024-10-10 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9f103dcd-e2ab-3ff8-b4c1-33d218da8c5b | -9.92377 | -47.71708 | 2024-10-10 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 640c8f2a-7436-34ae-9bed-98082e0c6612 | -9.86977 | -48.26274 | 2024-10-10 04:44:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ad0af03-49df-3945-8758-949745c5eb47 | -9.86942 | -48.26088 | 2024-10-10 04:44:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4412063c-f119-3d07-a28c-969ef29914b5 | -9.86612 | -48.26207 | 2024-10-10 04:44:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a50161b-b8a2-33b9-bcfa-38354d251041 | -9.86547 | -48.26642 | 2024-10-10 04:44:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71887c39-bb76-3636-8ae8-cb72b74205eb | -9.86247 | -48.26139 | 2024-10-10 04:44:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e399dbca-ee2d-36c6-afe0-d730c5fea7fd | -9.86182 | -48.26576 | 2024-10-10 04:44:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a82a390-9e4b-39f0-ad0e-b5483a82c9e6 | -9.85031 | -48.8227 | 2024-10-10 04:44:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3c8f016-d5c9-3bf7-bb5a-f6f44d506291 | -9.80514 | -48.37086 | 2024-10-10 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9a1fab63-e026-329c-98e9-8d03a1510fc9 | -9.8045 | -48.37518 | 2024-10-10 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d95ced05-40d2-30d0-bb04-977cb9c200e5 | -9.65899 | -47.83776 | 2024-10-10 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d40be782-6dcf-38e1-9e7d-803a5784c4d4 | -9.36506 | -48.80427 | 2024-10-10 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b53a30b0-d7a5-34cf-b095-812a6985c05c | -10.0559 | -48.7492 | 2024-10-10 04:44:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fca29f38-c8b5-3b2a-b81a-996337d57f7a | -10.05231 | -48.74865 | 2024-10-10 04:44:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb838542-2675-3928-a98d-634bf89979bf | -10.04813 | -48.75218 | 2024-10-10 04:44:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9925e6d1-415a-3189-a1ec-4b6b2da12a24 | -10.04516 | -48.7474 | 2024-10-10 04:44:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65a95d63-97e2-36da-b2cc-191acd0614c7 | -10.04455 | -48.75156 | 2024-10-10 04:44:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 231ffdaa-3dd1-3906-a140-16e2b4af832d | -10.03623 | -48.73317 | 2024-10-10 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd3c69a1-f4ed-3924-abe4-32595bbbc10a | -10.01215 | -48.84828 | 2024-10-10 04:44:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6588335a-61b2-3bd8-b3f7-5742dc9d06a9 | -10.00858 | -48.84771 | 2024-10-10 04:44:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 031da808-37f4-3e8a-b6cf-005e8e39e72c | -10.00591 | -48.84927 | 2024-10-10 04:44:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd253664-471a-3523-acd1-943eca078fe0 | -10.00502 | -48.84716 | 2024-10-10 04:44:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 804a545c-db17-320a-a4ae-b0576bd33a67 | -10.00442 | -48.85127 | 2024-10-10 04:44:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c8e3e18-f11a-388e-a22e-ce5d77a2876b | -10.00234 | -48.8487 | 2024-10-10 04:44:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 760922eb-3bb5-3d1b-beec-72040dc8a056 | -10.76 | -48.52916 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afc1339f-4b98-3743-be97-0cc18974a1ff | -10.75635 | -48.52853 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 656a82d7-5667-35c0-acf1-2468b91eccd8 | -10.72806 | -48.72211 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ea5251f9-19c0-31f7-aa31-97fd644f3c90 | -10.68226 | -48.73195 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b023058-be17-31e3-9a9a-4c5490322cf3 | -10.68165 | -48.7361 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a86066f-6cac-37e8-b1af-6ae9ee9e8a6b | -10.67864 | -48.73141 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df4ca3f7-7178-3a83-96e8-e95b869309d6 | -10.67741 | -48.71431 | 2024-10-10 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README102.md)
