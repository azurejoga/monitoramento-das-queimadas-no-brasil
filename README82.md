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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab1ebc6c-d9f2-338b-949a-5bea512d0d43 | -1.72901 | -55.65753 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b942c9d3-d402-3b59-a62f-46224c02767c | -1.71666 | -54.95166 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33add01c-e342-3c63-8a60-29bf0b853e49 | -1.71275 | -54.95471 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cc667e3-f134-339b-af21-a5a5f5c02b3e | -1.65047 | -55.18425 | 2024-10-30 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 528adda7-33cc-3795-bbae-70a0b7b44346 | -1.63713 | -55.20381 | 2024-10-30 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3006ed23-6db8-3cdc-8241-e0689f7c6f9f | -1.63658 | -55.20733 | 2024-10-30 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5ba74d3-736f-3d87-b3a5-847dc0d44e2d | -1.63379 | -55.20331 | 2024-10-30 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84af8fc4-05fa-391f-b00b-b8d3c8a04169 | -1.63324 | -55.20682 | 2024-10-30 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de53cd3a-58ba-3e68-ad97-7539810b4603 | -1.59785 | -55.88797 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bde4ca1b-7eef-3ab3-a5e2-33549b49fbd3 | -1.59454 | -55.88745 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49b81aac-d513-36d2-85d3-29df2da08770 | -1.59124 | -55.88694 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1c4bdda-5dc9-3fb8-9310-ae3096af902f | -1.5907 | -55.89038 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee4f9124-0ecc-3df6-b44e-bbac1ae3e73e | -1.56979 | -55.89418 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2d7fa0e-98f6-32c9-8f6e-9427a1a9329e | -1.54901 | -55.70002 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 483e46ce-7f3e-37c6-8680-f75a0405484f | -1.52144 | -55.70283 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c006b067-95ab-3670-a681-e723eeb575ed | -1.51813 | -55.70232 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3effbad3-8ba7-37f3-97b5-11c4966cc0b3 | -1.45344 | -55.50854 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a143013d-c2d4-3373-9cf5-b51a6dd9a919 | -1.41031 | -55.17648 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7fc9800-d9d6-3ad6-a980-ba7cd892c33a | -1.40085 | -55.99471 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14fb0533-4a55-3d92-bbf7-86530b3fc305 | -1.39759 | -55.21399 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bad9930-0032-3842-a5d4-44153ec5e1e0 | -1.32226 | -55.45596 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9797e8e5-9db9-3668-a2a8-cb26f141cab9 | -1.31787 | -55.83018 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9137a18a-a493-32d1-9f2a-ddc1f1eb21ca | -1.30102 | -55.72178 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc030c7-63a0-3142-bd83-0283891feb7d | -1.30048 | -55.72523 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47bcb97f-3dc3-3d3e-8585-78af00e4ead7 | -1.29771 | -55.72127 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc3586af-ecb3-31aa-a8d1-48e5c0a03799 | -1.29663 | -55.72816 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f206f4a8-92cb-3680-b905-447b9f1d845c | -1.29609 | -55.73161 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c31932c9-ca31-3457-88a8-d62f424df3c7 | -1.2944 | -55.72076 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64b61340-5e19-36aa-b4d9-4142af043ae2 | -1.29278 | -55.7311 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bce94ff2-9ca9-386b-86ab-fe28208a6825 | -1.29224 | -55.73455 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b658523a-2170-3094-8421-97805dc69896 | -1.29008 | -55.74833 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16057d11-90f8-3ebf-ba94-7cd9e5083f1b | -1.29001 | -55.72714 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6be3d9b0-c42f-37a7-b52c-d61184af0091 | -1.28954 | -55.75177 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8adc9a8b-cc79-3041-aa3a-07575343a2da | -1.28893 | -55.73404 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87e2f9c2-e380-3046-8a47-7b804efef07c | -1.28616 | -55.73008 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 878f1d03-de5b-3cc3-90ba-5d7d08162831 | -1.23501 | -55.64447 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e945a84-78af-35ea-8ca3-736d49d387d1 | -3.68983 | -55.56294 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa4ad7ee-2e8b-3c8f-b7e7-40933f95ae34 | -3.68648 | -55.56242 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ede8deee-151a-3ce5-adf9-88d358604c32 | -2.36319 | -56.51091 | 2024-10-30 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2d77c96-df53-3070-b864-353121b23294 | -2.27771 | -56.42693 | 2024-10-30 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74e5c8a2-48fa-3ab1-b78f-a56c821b81ae | -2.27717 | -56.43036 | 2024-10-30 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 607edefc-832a-3ad7-997f-5b7eec2e24d3 | -4.52095 | -55.64008 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5be3a8f6-25b8-33bc-9486-bb851518d985 | -4.51878 | -55.71978 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 005ddde4-ea32-3623-a074-c6e21d7fbb4f | -4.40373 | -55.75981 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99db3e5c-303e-3dca-bc53-3e0c123aad33 | -4.30645 | -55.57785 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a77fc31-97ab-3fdf-9d8d-82ef81cadb21 | -4.30589 | -55.58139 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4d32d73-61e0-34eb-abbd-c6485e5ac8c7 | -4.14623 | -55.44358 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f117b2d1-cb23-345f-8e2d-9ba9946339eb | -4.14396 | -55.43592 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6cffcad-1df8-3eda-9c7a-9302f88bf93b | -4.14341 | -55.4395 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bc0e8dc-e501-3051-b88d-7d211f9df1b6 | -3.99018 | -55.72896 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6cbc289-3c32-37cf-98d6-2870cca519da | -3.98684 | -55.72845 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bfddbdc-8555-3b47-975d-9e36189d7458 | -3.98181 | -56.08955 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4e290d9-482b-3753-a235-a078061c64e1 | -3.95682 | -56.05364 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae7cc4ec-e494-3613-977a-a38b15e6162b | -3.95628 | -56.05711 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 702ccf12-cddb-3c6d-8fab-590274b8d69d | -3.95458 | -56.04618 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b28596e2-f939-3353-83a3-0a3e93a54d24 | -3.95404 | -56.04965 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e04a0d7-4ed0-352a-b799-730cd8fe9445 | -3.9535 | -56.05312 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7e3726b-5386-31d4-8e8d-2f773e94853f | -3.93425 | -55.78495 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22526683-c8d3-3f21-9baa-22990d2edcb3 | -3.93315 | -55.79198 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f66f3f7-e159-3b4a-98b9-2e7e2aa500cf | -3.93037 | -55.78794 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ebc4d83f-c879-31ed-a8c5-a94842e3f07d | -3.92982 | -55.79146 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dfcab1a9-68e5-3972-8b76-ab1299d37da1 | -3.88151 | -55.99172 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03721fa4-14d5-321a-83a2-b8ed2d6a08a7 | -3.84411 | -55.64483 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ce1450e-7024-3db2-b8a5-1e469d8c2c82 | -3.72497 | -55.55747 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0dcb18f2-ecae-3bb2-b156-177eed7f34e0 | -3.72107 | -55.56049 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efac6e67-18d5-3178-b756-63fd19bc0061 | -3.70322 | -55.56502 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c26168c-37d9-3380-a4b8-9182bb28b653 | -3.70042 | -55.56096 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a975341-e892-3011-ad21-8f016eee6ee3 | -3.69707 | -55.56044 | 2024-10-30 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbecd16c-a619-385a-b0a3-4566c6a02435 | -5.19799 | -56.08807 | 2024-10-30 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3d939f0-3efd-3683-ad11-db7a9b6de891 | -2.07041 | -56.55573 | 2024-10-30 05:08:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e52bcc5-40c4-3ccc-9ac0-bb5628dbdd35 | -1.98929 | -56.59573 | 2024-10-30 05:08:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0568e8a0-3dff-39ae-aed8-9061c4585ae5 | -1.98599 | -56.59522 | 2024-10-30 05:08:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4666f825-bfde-370a-b7e4-7349c540783a | -1.98215 | -56.59813 | 2024-10-30 05:08:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2ecc747-7bee-3e7a-a1c6-ddbf121c6465 | -3.68796 | -57.01041 | 2024-10-30 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98aeffd1-5392-392a-bc55-0e49469fd4ab | -3.50863 | -56.9186 | 2024-10-30 05:08:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1218368a-cd3b-3164-ad9f-31b40e670ef9 | -3.49902 | -57.77639 | 2024-10-30 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a1befb0-b91c-39fe-928d-15d8920dbd3d | -3.499 | -57.02273 | 2024-10-30 05:08:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f12c612-c634-359c-a222-ba501c24eeb3 | -3.37176 | -57.69865 | 2024-10-30 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d34150af-e624-3098-aa5e-14d25c4fe904 | -3.1231 | -57.08049 | 2024-10-30 05:08:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 498d8768-109c-3a01-8e45-0546ce3fb096 | -2.90186 | -57.68643 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7309e667-4fd9-355e-b257-06428b467fea | -2.89907 | -57.68239 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1569dce2-538a-3d48-8417-79d182975beb | -2.83008 | -57.68599 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d04a710-9255-3232-983f-29b3926f5ba3 | -2.72999 | -57.48035 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 666e42b8-0ee0-3957-a6c7-bd20a1157d5d | -2.72943 | -57.48383 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f95e360-971c-353a-bb5f-e7bce8a5bab6 | -2.72709 | -57.47993 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 437a3c6d-3bc4-32f2-a2e2-8b34f33568a8 | -2.72376 | -57.47942 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 491b35a0-af35-3b3b-9068-fe1376ea3474 | -2.72044 | -57.4789 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41b32a23-ff05-3e7b-9116-f64028664cdb | -2.71989 | -57.48239 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fd7758b-4485-33d6-a39b-15278dd73e54 | -2.63153 | -58.16291 | 2024-10-30 05:08:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edcc3c27-b50c-35bc-b1f0-60cac9270329 | -2.59374 | -57.44089 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b9b5b8d-28ec-31a1-9995-a908d234ff41 | -2.59171 | -57.58398 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d88ee65-9de9-3509-be27-09e75a01eab3 | -2.56479 | -57.32219 | 2024-10-30 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68887161-5af4-3073-bded-51a0c07107d4 | -2.54046 | -57.34689 | 2024-10-30 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f53ef65-a3af-3fb4-a0a0-ef54e44d7da6 | -2.53991 | -57.35036 | 2024-10-30 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9e4be8e-6fd7-3ace-ac4e-ff9e424b60de | -2.47167 | -57.9096 | 2024-10-30 05:08:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89fb8925-b6dc-3d6f-bf0d-b09ca60ca111 | -2.4711 | -57.91317 | 2024-10-30 05:08:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 864109f5-9f98-3778-9a6c-f7af30636be8 | -2.46117 | -57.52771 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06c25d63-4115-3bd5-8f04-69b9bd67f25c | -2.45784 | -57.52718 | 2024-10-30 05:08:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cbdfbe0-008d-36ce-a5f7-7cd2ef8b13fd | -2.4575 | -57.97705 | 2024-10-30 05:08:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83ee7772-2e51-3c10-aba3-2e8d35775171 | -2.42076 | -56.85691 | 2024-10-30 05:08:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README83.md)
