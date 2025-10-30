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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f533798a-6c05-3def-9a8e-aa1740876690 | -2.57261 | -45.8013 | 2025-10-30 05:14:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5e97f38d-b5aa-35de-af6b-8acaa20c6db9 | 2.06509 | -50.90513 | 2025-10-30 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5bc6dec-d2df-322e-a068-f9d11e4fcd42 | 2.15575 | -55.78591 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed33c4ab-1739-32f3-94f4-29a54eadf636 | 3.22117 | -61.19473 | 2025-10-30 05:14:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfd3e98c-9169-39b4-8f95-587780ae4a87 | 1.01316 | -59.52555 | 2025-10-30 05:14:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91c32ad7-0094-340c-bcb5-2dc3c5d742f2 | 1.89664 | -50.82021 | 2025-10-30 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63133fd0-f7ca-376c-adbd-7018a0c75f77 | 0.83029 | -59.3172 | 2025-10-30 05:14:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ac3234b-2337-3794-8ec5-c6149e12e47b | 1.61266 | -55.69019 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 158dc480-8798-3027-9445-2ea5da910b70 | 0.29138 | -51.20223 | 2025-10-30 05:14:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92e36d8c-cf93-348e-8a81-e0b651e25412 | -2.6638 | -47.87285 | 2025-10-30 05:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85bf707e-7b2e-3b31-a15e-931c0d0e4c02 | 4.48586 | -60.7631 | 2025-10-30 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e04271d0-49a9-341f-88c5-fc81b890410a | 2.07998 | -50.86079 | 2025-10-30 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3fb5336-21c9-3102-b7f9-4c15d6d699eb | -1.81012 | -55.56841 | 2025-10-30 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1eb01a2-1f8a-31eb-8adb-0df2022197ce | 3.14293 | -60.69911 | 2025-10-30 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3ca1317f-153e-3ae4-9aea-8f5e1781ebce | 3.1422 | -60.6945 | 2025-10-30 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6e25ec10-13e1-3677-8338-cf69e6a5c9f0 | 0.29203 | -51.20635 | 2025-10-30 05:14:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f013cdf7-0185-3c54-a582-03bffd03f253 | -0.19517 | -60.73832 | 2025-10-30 05:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 515c624e-4792-32cf-831e-52867e7391a9 | 1.01663 | -59.52502 | 2025-10-30 05:14:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0654288e-8381-3ce0-88f4-0e1a18f437a6 | -3.22952 | -46.87436 | 2025-10-30 05:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| adabf9c5-5c2a-31f0-91b5-035f4df282ca | -2.77038 | -45.39323 | 2025-10-30 05:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e99754e1-e2e4-33d2-aa8d-40c7720328eb | 0.44297 | -60.47979 | 2025-10-30 05:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19edaa0f-483b-3b02-b251-7a09dedb8f5b | -3.76341 | -50.37083 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b225ea43-801d-3456-ae0d-935e2a951dcd | -8.32732 | -47.93101 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fc983b62-87dd-35ef-932a-6bb2e0d17169 | -7.29974 | -46.64162 | 2025-10-30 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6cc86407-3eb5-38ec-86d6-65e068068d67 | -3.25134 | -54.5938 | 2025-10-30 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6b81214-cf16-3166-863f-df23ad636d94 | -3.69049 | -51.07988 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 511e0a69-7ad4-3495-bad4-aafbd000ba13 | -5.60755 | -47.12475 | 2025-10-30 05:16:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54cbbe50-55aa-30c6-a04c-7603e66d78eb | -3.42619 | -59.6501 | 2025-10-30 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8020583b-651d-3ffa-ad02-2a196683f1c3 | -5.6138 | -47.12542 | 2025-10-30 05:16:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5c1a4a5c-a4e5-3a35-aae3-cf2a9a38ba65 | -2.05355 | -56.87724 | 2025-10-30 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d02d6c8e-f886-3c0a-9af5-e9d224a2ffe7 | -4.84351 | -45.85156 | 2025-10-30 05:16:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1b0a904-f1d6-3e22-8d57-642540644531 | -3.68584 | -51.0792 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1642b020-77f8-398b-b888-cbef33921524 | -2.93875 | -54.16399 | 2025-10-30 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43bccf03-b093-307b-bf47-b3170d31680f | -8.32791 | -47.92633 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6375e095-afef-3ce2-9a96-2d28dfba4405 | -9.89115 | -47.44803 | 2025-10-30 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d67511f-8df3-30ad-8616-ab525fe920ef | -2.05409 | -56.87376 | 2025-10-30 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96c6a069-6a76-301f-8e7a-c090f2731a92 | -3.69047 | -60.55793 | 2025-10-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77ffc2fa-f918-3f77-ad8a-6266b8809b88 | -4.53906 | -54.96688 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb36b9fd-dd54-32ff-8837-087e1bacbe31 | -6.52049 | -46.9082 | 2025-10-30 05:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d0238085-3008-35d0-a7f7-23a9d1667716 | -5.84689 | -45.54181 | 2025-10-30 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bd1af18-d192-384e-ac38-f93117df86b7 | -7.34791 | -47.62717 | 2025-10-30 05:16:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9563cae9-2f04-34d8-ba92-a89a1b662f8b | -4.14436 | -50.68493 | 2025-10-30 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b20151a3-a886-3513-a865-9036f9dc5bc0 | -3.08501 | -49.50135 | 2025-10-30 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fcbbe94-8181-3933-9156-e142dc32a697 | -2.72778 | -58.03138 | 2025-10-30 05:16:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d11748ed-fff6-31b0-b2c0-7185d352a26f | -5.60256 | -51.13571 | 2025-10-30 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b1f365e-f196-3150-b6f5-f5432f98045a | -9.88469 | -47.44727 | 2025-10-30 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20c4f5ea-0e75-36a6-93c7-b43c82ee54a3 | -7.29534 | -45.6634 | 2025-10-30 05:16:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| b324e856-7d5a-3f0d-9ee7-4e476f66ab38 | -8.32672 | -47.93567 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f7193d7e-5508-3e4e-b18f-0fa3a85d834a | -3.47906 | -49.92247 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5e26be1-5a57-3fe5-9539-38de0aec0d71 | -6.52301 | -46.90569 | 2025-10-30 05:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a22c4125-b57f-338a-994a-3b9e788afebf | -2.94427 | -51.26974 | 2025-10-30 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d149dad-ee2c-33b5-bac8-c62a2c6bb2d0 | -9.82848 | -47.6985 | 2025-10-30 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 72b8b8ae-741c-38b2-9c7c-5ad4064c7ce1 | -5.75813 | -49.5038 | 2025-10-30 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b5b9d4e-ee56-3c27-864e-0400bed67c9e | -9.82213 | -47.69775 | 2025-10-30 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e69a1b86-4a07-3110-ada1-c7c18023f7af | -8.3285 | -47.92167 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc8c3365-9803-343e-8e18-756533ddf3a5 | -4.43659 | -50.10327 | 2025-10-30 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 195a83de-1a95-3491-8ceb-7d2ea7ff1b09 | -7.30232 | -45.6641 | 2025-10-30 05:16:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 27db8f86-4b97-3f27-83bc-567905d6d93c | -8.436 | -48.69805 | 2025-10-30 05:16:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acdc1788-2fa8-3170-9221-750787b5adc1 | -3.25259 | -51.37488 | 2025-10-30 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d36c3dc-b05c-3dde-ba62-a694ca1d5ca7 | -4.53176 | -54.96568 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31d5d881-d4d1-344c-a744-9f698ca9406c | -5.84113 | -45.53854 | 2025-10-30 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 111e54cb-a091-3106-a228-a69d22cd6048 | -3.49761 | -53.55534 | 2025-10-30 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73cd2793-354f-3a27-9551-7cc7dc6d274c | -4.02359 | -54.32089 | 2025-10-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 078aa237-fbd9-3bbc-a5af-1fe4e764a618 | -4.24416 | -55.87688 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2228ce3-5813-351c-ba8c-c1421cd5358b | -9.94318 | -47.17287 | 2025-10-30 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9ff2e09e-c99a-37d7-8dd3-12d702960911 | -2.65682 | -54.5372 | 2025-10-30 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8132d485-0297-3e88-8d30-bf2aaad225ae | -2.30464 | -57.01279 | 2025-10-30 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e54f3b6e-94b5-3c03-94c4-d94fea12e621 | -4.64523 | -49.48551 | 2025-10-30 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e2763f1-d4c6-3cef-84f5-d38bba58775a | -3.47404 | -49.92174 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b815e12a-fc75-3dfe-8359-6ed894e32b1e | -2.93691 | -58.34538 | 2025-10-30 05:16:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07e3f946-10b1-308d-811b-99de28a87274 | -3.687 | -60.55738 | 2025-10-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f06ee8e2-2b5c-3ca0-8f2c-cf277255ccca | -2.45009 | -57.99805 | 2025-10-30 05:16:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62e4bf8e-4137-3be1-9499-a99c68f07536 | -5.40079 | -49.4218 | 2025-10-30 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3dcee0d6-4e87-3fff-9c25-365f4c533c5e | -4.07169 | -48.26066 | 2025-10-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4cd0ce2-119f-358b-ac62-f081dbae4ee6 | -2.91152 | -54.29219 | 2025-10-30 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 884985aa-f385-32f6-8d28-49232158f3fc | -3.32661 | -54.08781 | 2025-10-30 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4037d32b-6b05-3ab4-a508-24d3aa681a7c | -3.0897 | -49.50517 | 2025-10-30 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c150e1e9-0a5e-31b8-8e15-a944fe293430 | -4.84833 | -45.42335 | 2025-10-30 05:16:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 954a537b-f784-3650-94a5-652be6845549 | -5.43127 | -45.33618 | 2025-10-30 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6e1c0d54-035f-37be-a54e-caff35afea61 | -7.29896 | -46.64743 | 2025-10-30 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25e22b85-5211-320a-a46f-a0d6de9cdd2d | -7.34713 | -47.62719 | 2025-10-30 05:16:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 42e2e320-8d21-39e4-915d-94863b792856 | -4.24582 | -55.87688 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08034ec4-7976-3f9b-91b9-a5fe360da9e1 | -3.73667 | -53.80872 | 2025-10-30 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e3ab474-14e4-39f3-b31a-2f6602130550 | -8.33287 | -47.93644 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5521179b-b9d2-3b5e-b4d8-a8384c8bd73f | -7.34596 | -47.63643 | 2025-10-30 05:16:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52e9fd50-7483-317d-9b77-c3647b39e49c | -6.52118 | -46.90318 | 2025-10-30 05:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 961d25dc-3b9f-3358-a338-70f3cf272b20 | -8.32177 | -47.92548 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27c59b90-2f33-3c96-a296-37fb81f9caaa | -3.52989 | -47.55172 | 2025-10-30 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d14bd5e4-93f2-3e89-bcfb-f576974911b7 | -3.53115 | -47.55276 | 2025-10-30 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea2d1bc8-058d-3d03-bc92-a2be77121498 | -9.89182 | -47.44254 | 2025-10-30 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cffd1685-6c19-33f3-8843-70051a955fc3 | -3.46046 | -52.87152 | 2025-10-30 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 563ef82e-1700-3591-b716-3ad9dc611521 | -3.42956 | -59.65062 | 2025-10-30 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 905c28a6-aef9-3706-b1d2-b884d2939d5c | -3.94531 | -54.75814 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9322b9a2-88d9-3d67-8bf1-ce3947effe9f | -3.32593 | -52.62301 | 2025-10-30 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60f505d7-825a-3e4e-91c8-7a8e6e78d8ce | -4.36553 | -55.77212 | 2025-10-30 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43b1d86e-3546-3463-80a7-51769ae9c783 | -5.848 | -45.53955 | 2025-10-30 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c0ad08b-7828-3e44-9b02-165678778d58 | -3.08456 | -49.5044 | 2025-10-30 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dde79c4-13af-3bb9-a92d-d3a60a02dd9b | -4.64519 | -49.48648 | 2025-10-30 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cbc7d3f-8b72-3ccd-8330-f63b613e4376 | -9.82277 | -47.69233 | 2025-10-30 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36460e15-c0bb-38f4-b82b-7e743c00ea2c | -2.95434 | -51.52746 | 2025-10-30 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README63.md)
