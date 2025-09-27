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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99d643e3-1ef2-3fa0-953c-3adfe357ed23 | -4.30831 | -48.09137 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9decfa8a-e088-351d-8d9b-e3c1fb851e96 | -7.00536 | -46.99893 | 2025-09-27 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90192a7e-405c-358a-a2c0-9f490865f5c3 | -5.74965 | -42.91101 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bcb7ed29-3705-3eff-901c-01733b60f7db | -6.69815 | -42.74314 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 972a22bb-2912-3361-ad78-8ec624e4c49b | -6.0655 | -44.0728 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbf264f7-1385-3078-beda-d5f3d2db8f56 | -3.80111 | -41.57338 | 2025-09-27 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 74a7a557-a76a-3cfb-b0ba-d5ed021a6b6b | -7.18402 | -41.71129 | 2025-09-27 04:44:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 48df2047-d33d-3386-ae53-4f25ae7a18bc | -7.81299 | -46.89664 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| abeba7fb-66d4-3caf-9d44-a9795d7a383a | -6.704 | -42.73818 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57ef1ba1-65bc-3ef9-a3ae-316f97a2a52a | -4.5788 | -44.07486 | 2025-09-27 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7b73055-ced0-3e0e-a6c3-5b34abd6dfe7 | -3.83813 | -49.25449 | 2025-09-27 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cd9d622c-5a40-363e-a7b1-3799d4596291 | -5.80636 | -42.79576 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 34dc2757-2e8d-3044-9a3c-ea1cbc50686d | -8.32629 | -48.00931 | 2025-09-27 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 914688bd-fd0d-310f-ad8e-c1692b1ada71 | -2.95936 | -48.59727 | 2025-09-27 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58112486-3f21-3772-915f-2f1d9e4cdf3c | -3.59916 | -49.45864 | 2025-09-27 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e0ce01e-1409-3c54-9978-66e57aa86987 | -8.35536 | -49.09911 | 2025-09-27 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03a9a943-94d4-3b31-83be-8758531e60bd | -8.73886 | -48.86017 | 2025-09-27 04:44:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abe5c6df-c21e-342b-9512-1dd772a3ba3f | -4.57812 | -44.07928 | 2025-09-27 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4129d9c1-01de-38bf-8fc7-b48c40a81792 | -4.0006 | -46.96396 | 2025-09-27 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e3cb527f-4f83-31ac-a7e6-1e0065fd5736 | -4.3838 | -41.91938 | 2025-09-27 04:44:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7bed767b-7b05-3f7e-93df-307ee339f91b | -7.14035 | -45.5103 | 2025-09-27 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 741e677d-2bf2-3082-9164-59e50adf2cf3 | -2.95992 | -48.59367 | 2025-09-27 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e7b6b42-f57b-3953-945f-fe0b92f73aa8 | -3.4515 | -44.12415 | 2025-09-27 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4d06068-bb3d-3935-8a6b-64f1a5d553d9 | -4.78866 | -45.34328 | 2025-09-27 04:44:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7606954c-edcc-32cc-a0f0-3fac80a5c132 | -7.80912 | -46.89608 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 683aaad4-5f4f-3ffd-bc2e-96699fcde8c7 | -6.89537 | -44.1618 | 2025-09-27 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12df8da4-0d91-3de4-8c37-df0fc6d077f5 | -4.34789 | -43.01399 | 2025-09-27 04:44:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c09581c-32fc-3df9-9a29-0625aaa63de9 | -3.40046 | -46.90313 | 2025-09-27 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26a2de4f-3748-3d99-affc-fc81126e933a | -5.79746 | -42.82245 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 762ae628-fa93-3f8c-b071-af3f219d7fbe | -6.69919 | -44.58894 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 318d3383-e41d-3352-8713-106a9f18ed8d | -9.01447 | -46.59032 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f48d2362-94b0-3cf2-a8a5-a9f48d9147f0 | -6.98495 | -42.39616 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bcbbe856-cc96-329a-9558-f74aede7cc09 | -6.61546 | -42.93084 | 2025-09-27 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d0fb547-6b4d-3f02-bb3a-90ecfaf3eb9d | -4.00363 | -46.96865 | 2025-09-27 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 180145ed-aca3-31e8-b7fb-13f8a311453e | -4.5756 | -48.01952 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ab38808-abf9-3d48-9351-c793f078a0f1 | -7.83113 | -45.14808 | 2025-09-27 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de558c44-b749-36aa-91ef-fba5840baab7 | -6.20768 | -42.85067 | 2025-09-27 04:44:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 300c5922-36a4-3b8d-ad37-f6d11f96cc4b | -2.5507 | -48.40905 | 2025-09-27 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 486c7757-19a2-3539-a3b3-92815a8cc6c9 | -6.2307 | -44.19516 | 2025-09-27 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33a7224f-be8b-32e6-806e-87251c9b8f40 | -8.82388 | -46.26766 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b50a7c2-8975-38e3-9ab4-b16a7278c5c8 | -4.64547 | -50.96779 | 2025-09-27 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b09ecee-b575-35f5-a545-77dc663491f5 | -7.87815 | -44.02433 | 2025-09-27 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a14eaeed-5e98-3f23-9f0f-f08b0a1393f2 | -7.12153 | -42.17646 | 2025-09-27 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2076bd57-01c1-36cf-87f2-b64194b9ec40 | -3.99629 | -46.96762 | 2025-09-27 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47e33797-a7d0-32c2-b180-ede93640d1c1 | -6.42598 | -43.0723 | 2025-09-27 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 108eea9e-0f0d-320f-9cfe-1eec8c7f5c26 | -4.53405 | -48.65237 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 91e5817b-c390-3ce2-98ae-4c8f080a3926 | -7.18995 | -41.70842 | 2025-09-27 04:44:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44cb357c-a39f-3e33-add2-2c62f444cecf | -6.99614 | -42.39156 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7774871a-4516-3c32-b189-b273a2f6ae53 | -2.49089 | -49.27172 | 2025-09-27 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6dc4339-40ae-392e-97a9-66f173c75c41 | -3.23663 | -46.80067 | 2025-09-27 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c4452d8-5f8e-3d1a-8230-762e89dbd6f3 | -3.82268 | -40.34906 | 2025-09-27 04:44:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7d24f1d2-6e18-38ae-94f8-16a4ee3c0971 | -7.04644 | -43.02632 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 74cc5f1e-bcf2-3756-9fe1-ece05cfd21db | -5.73038 | -42.64972 | 2025-09-27 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ea99b51-5db7-361d-980f-6aae31ea5e30 | -9.03872 | -45.53345 | 2025-09-27 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3c382ed-6ba2-3429-a651-db69e450cb10 | -5.52522 | -43.86247 | 2025-09-27 04:44:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f5f5d7f-d4bc-3ec6-bd5d-e851e4611ba9 | -7.78267 | -46.94167 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df7143cb-92c3-35e3-84c3-af04b0aa6222 | -7.6429 | -46.77245 | 2025-09-27 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 001f3f40-f4ff-3bc5-9a03-c01490a95ac9 | -2.96274 | -48.5978 | 2025-09-27 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40a0b6d8-cacb-3cdd-94a1-970b6af1a276 | -7.23409 | -48.34395 | 2025-09-27 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 045c2e33-bfcc-31c0-9092-ab52b83a7999 | -6.20689 | -42.85627 | 2025-09-27 04:44:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 51735d75-22f8-34a3-b332-df8d92677a2e | -4.61318 | -43.10658 | 2025-09-27 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4f4bdc39-227b-3d9c-84d9-c709a303dc54 | -9.87398 | -45.91064 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1354133-e085-3a4b-8c93-dcfcbc7274bc | -7.61562 | -43.83762 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18bc575c-3865-3e44-84dd-c2fce5ed164f | -5.0347 | -38.00995 | 2025-09-27 04:44:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 72d94572-85b1-39ea-880b-b96a246ae4c1 | -5.47337 | -43.07459 | 2025-09-27 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b39c1a29-7c67-3f05-a9e5-4164f316a687 | -6.3177 | -43.45145 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b7bdcb9-48a4-3565-ad52-0ee99a0947c5 | -8.65871 | -43.99195 | 2025-09-27 04:44:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f09e237a-a0b2-3000-8f4d-0fce23bc194a | -6.42109 | -43.07148 | 2025-09-27 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a5de07d-7b12-35b4-86c5-8bd4e2d44042 | -5.03892 | -38.00681 | 2025-09-27 04:44:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4f52bf1a-0f35-32ae-b00e-5ee1580324a4 | -8.82849 | -46.26452 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99a5a7b2-efa5-3bb6-98a2-f12d24041133 | -7.28307 | -42.97733 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a1a6551-2b2f-3548-afc8-cc7c0d7bdaa3 | -5.73571 | -42.64815 | 2025-09-27 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cbf82543-2fe0-3c74-8808-9613d1e397fd | -5.81051 | -42.80198 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4057bbd3-1074-3607-8a5e-4e53d865f9ba | -6.54337 | -43.93798 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 180b9af7-3e06-3a81-8455-d5e877880949 | -3.1918 | -48.80978 | 2025-09-27 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0604332-9234-3f7d-a885-f0a97c9c0ab8 | -7.1356 | -45.51359 | 2025-09-27 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37aa1ad4-40c2-324e-b50b-a7969dc6b7e9 | -6.45649 | -43.13712 | 2025-09-27 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfcba444-f82d-3a9d-b6b9-4fd97368dede | -4.48067 | -47.67055 | 2025-09-27 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46d2ebd4-ba27-3e02-b58f-bb8410ea652b | -4.61218 | -43.10982 | 2025-09-27 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d354399-164f-3f53-81b2-325f4ff97d4c | -8.69584 | -47.02676 | 2025-09-27 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 054a5bb4-db13-36c8-a9a0-9ef7c9c62a3b | -6.74912 | -44.7107 | 2025-09-27 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc248275-fc25-3996-b27c-308488ed8926 | -6.2209 | -47.32898 | 2025-09-27 04:44:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8ef564df-aac6-3f75-9702-9e0bb4fd6e1f | -4.33319 | -48.39024 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ec715190-83eb-3aa1-a818-6a1270d2a36a | -9.99449 | -44.17888 | 2025-09-27 04:44:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5934029-8e08-36d8-b8d8-6c4f6974413b | -6.7065 | -42.75651 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fd9916dd-79f7-3e91-b025-1dff3d3f0b39 | -6.99912 | -46.98856 | 2025-09-27 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb40029d-4f0f-3e95-b38c-7d2a3afa7419 | -3.35391 | -49.48455 | 2025-09-27 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0197cab6-c5fa-3d14-9a31-218b2bd7cabe | -2.2655 | -47.19361 | 2025-09-27 04:44:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d615d304-cc58-3c8c-98c4-f64a41483f0b | -8.83578 | -46.21299 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed3e8e38-89e8-3e27-aa8d-6d578f4d1fbb | -3.80679 | -41.57099 | 2025-09-27 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26b36b04-3257-3938-a24a-0cec3b65dd46 | -6.53093 | -43.83429 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdef4df9-a41a-3c05-a1bf-d63fef531921 | -10.23933 | -43.95045 | 2025-09-27 04:44:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6606db4-315a-3376-b1b2-52070d30e730 | -7.27309 | -42.97582 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45118328-9674-37cf-b10a-fff552484a44 | -8.81674 | -46.25921 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef9041b5-59e9-398e-9ae0-139093d02393 | -6.70947 | -42.73589 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8f834f11-821e-322e-966f-f7f3ceaa2d4d | -3.29784 | -42.18077 | 2025-09-27 04:44:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4f2e94b-e980-3f4c-8f84-3463f60f8132 | -3.33272 | -50.20311 | 2025-09-27 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e2e2cc2-507e-320b-994d-82f98f90f6ba | -5.48468 | -45.11055 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab6a1c51-3923-3338-88cd-f87411d64163 | -2.95647 | -49.09325 | 2025-09-27 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e5cd47f-2bf0-3647-8a43-ec16f6b9a192 | -1.58268 | -53.97095 | 2025-09-27 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README45.md)
