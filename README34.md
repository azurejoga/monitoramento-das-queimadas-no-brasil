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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72fd8b4e-f906-3b90-a492-f006a4f6a82b | -2.35884 | -50.86701 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edafeede-bb0d-34bb-a9f8-9ba7f0570c31 | -2.24339 | -53.74871 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 82085a5b-303f-32eb-9be0-6cc950c9cc15 | 0.84927 | -50.21013 | 2024-11-13 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a6f6c1ae-7132-3c9a-9e5c-cdf2f751476b | -0.90012 | -51.73192 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83d60c9a-766e-3144-a4b8-24da849adbd1 | -2.24946 | -53.75317 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 061e6e68-9c3f-3b0f-98f1-6ab595a38ebf | -2.39848 | -53.73405 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4439596-4a49-3d9d-a120-b6b8127f37ce | -1.38954 | -51.44701 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94829f68-997f-3ff9-b8c7-9b61097d6536 | -3.73124 | -45.94715 | 2024-11-13 04:57:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5457f252-7362-3bf3-b2b0-1afa8d36e887 | -2.89501 | -48.3095 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37ef2dc2-f540-34b9-be0f-344df11a7338 | -2.98405 | -51.34564 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd09f76b-ffd6-3851-8fc6-9a81a1a531c5 | -1.84783 | -46.28503 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 144cc29e-ea20-34f9-8090-11420634fced | -2.29579 | -53.5214 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6aba4e8-54f5-3bfe-8c5b-e1ce78eb92b9 | -2.58658 | -53.98899 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53a01a88-eba8-3524-9a1f-aebe76655218 | -1.52048 | -52.20807 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5449da4e-b4ba-3469-8fc1-feebf2930aea | -2.11697 | -50.69526 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 957c399f-93ad-39d2-a664-ba73d7917703 | -0.01218 | -51.14132 | 2024-11-13 04:57:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91604299-8519-37f1-a2d9-ea56bb54fac9 | -1.51208 | -55.88065 | 2024-11-13 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bb43ac5-d424-3606-b0a2-ad9c37b12746 | -2.82388 | -54.01942 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3c7b4d5-1397-3391-a8d9-9490892f8e72 | -3.1074 | -54.29375 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7889c5bb-596d-3363-9c0e-c94e6ead4f4c | -2.72728 | -45.29539 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 212d78ff-86da-3667-819a-7f45cdc54a17 | -3.1718 | -50.44887 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c51d99a5-2c53-3feb-b21b-64cc34970100 | 1.05512 | -60.60343 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 19a22052-4ec7-3af3-a7b7-e28d9b9d9953 | -2.4592 | -48.82354 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36dec011-fea9-307b-a364-8f9af14bfc50 | -2.82702 | -51.04704 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3060fe86-6521-3762-8fba-29f06623a043 | -2.26836 | -51.02844 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 481e392f-8fd0-31b9-b6e5-f69aae189939 | -1.42189 | -53.47555 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bb7b8fd1-1c1e-3057-95c9-17b90d539aa5 | -2.35987 | -48.51862 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 402d1b21-a75e-3c59-ba50-0455349e1710 | -3.41289 | -50.31437 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b998fd4a-65a2-310c-a234-d4fbf60d9c33 | -1.49711 | -51.15987 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce7e7206-de2f-3945-89f9-4e5fd4165fc0 | -1.37586 | -51.3998 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7efc7db0-571b-3d47-9ba4-8f7de9b5c580 | -3.06621 | -57.30407 | 2024-11-13 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57893b72-03a4-341d-854d-a5ffa122e523 | -3.88017 | -51.1511 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daa3fc27-c74c-3e85-8f40-d32207785f34 | -4.37054 | -48.08511 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdb99ad9-ed95-3c6d-a3b3-74972dac8b73 | -4.54077 | -49.79324 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba1ecbe6-cf72-3bb1-b9fc-a959bd1962ed | -3.70861 | -53.75318 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4135fa32-c1ba-3afa-9be3-93f9e188bc27 | -3.14652 | -54.47748 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 624f924d-c786-3dc3-8e1f-fbe659c7bc0c | -1.64937 | -52.53874 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f0c173f-9a26-3463-859d-473913deb095 | -2.88019 | -49.35073 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c4601da-b283-335f-bd64-cb7363102af1 | -4.11145 | -51.10752 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 836be467-3827-3df3-b53d-9666eb0d7597 | -2.37667 | -55.759 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8236cea3-d0de-3045-bdee-50ea4a27b66a | -2.93641 | -54.1039 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7280eb8a-0b6b-33b2-8d18-aabf26a286ac | -3.05935 | -50.326 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b9cbe8f-a442-38fb-a7b4-101cca0b6b20 | -3.43869 | -50.36608 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc169d3d-581b-38c4-85f4-8eb94fe62a35 | -1.98296 | -51.10015 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ee6e19e-af3e-3574-bd40-e24c6afe35a7 | -2.39491 | -53.67023 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 059eadf5-317e-3654-a82f-bfef93588e8b | -1.96896 | -46.5718 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7730c5c-d98c-3367-ac7c-80f51955f0ac | -3.17463 | -53.64451 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef65f25a-2cf1-3f77-98f5-922ee119e41b | -2.82246 | -54.09328 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3140f7f-84a0-3748-a2b4-d2b6ac8b1f5b | -2.56682 | -54.00711 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb6e1d08-0572-327f-a1b5-9e21ed7591a8 | -2.73251 | -45.29033 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a2a9fabc-1f08-3058-a078-78a649af4140 | -1.95699 | -53.31748 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db21f633-6d8f-3978-ad9c-6820eb43c3a3 | -2.27888 | -48.44499 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4763995-a32d-3d8f-a333-65c387cec006 | -3.07817 | -50.32462 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2397a66f-8855-3e94-9588-f8dd31d2356b | -2.96029 | -51.05805 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1ca58f1-0195-307c-a419-1b7b30b65a09 | -1.63941 | -52.5372 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fe1347f-0df9-3219-b877-b163924a2c7a | -3.61582 | -51.36413 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d113873e-a1b3-3ca2-9ebc-bf4d1af95b74 | -4.10852 | -51.10303 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72a8fb18-d668-371e-af2c-0ee92130669c | -3.04627 | -49.7106 | 2024-11-13 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c1737ae-17d2-3d16-9e51-69bf7b4f163f | -3.89092 | -53.43703 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b036108-12fd-3734-9f9f-f2bc142859e8 | -1.39783 | -52.07693 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3db802f0-78cf-3396-9bff-7ddf290f5ab4 | -4.36802 | -44.10831 | 2024-11-13 04:57:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0e247c8a-bf2f-3b24-a0ed-b32d98416bce | -2.28695 | -53.773 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc05911d-5a70-3bb8-8859-701c43ed26fa | -1.48234 | -51.09596 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73586da9-cfbf-3454-b556-afca600e8eed | -3.31074 | -54.12374 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ed3bc19-9a5c-318f-b937-b435dee5a13f | -2.39545 | -53.6668 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59ed4213-fc42-3bbb-ab5f-1e86a0ffa266 | -2.41058 | -48.93362 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c173e7df-8d52-3c50-9430-0a742a8386d7 | -2.54427 | -54.02132 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c24823a-13ca-3924-8150-b6dc82473cfd | -4.67916 | -44.5783 | 2024-11-13 04:57:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b48983cb-4147-3996-9431-cf07fc52c2b6 | -1.39449 | -52.07642 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66e11f5b-9d39-3b70-bda8-712c8b5a302d | -4.1162 | -51.10018 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ea8975a-0b7e-3538-8a46-52eeca1ed73f | -3.52989 | -54.48422 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59c85e57-59dd-346e-bc1f-b67898365378 | -2.96762 | -54.68527 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6f7bd7d-259f-3a75-be2d-975dbb5cf3ce | -2.21089 | -53.7402 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7189e4fe-9087-3064-891b-d0a49fd66756 | -2.19782 | -50.82771 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60832dbf-4681-3abb-b14e-320dec123d29 | -3.70237 | -54.62121 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e27b6b3e-9285-324c-aa16-dcc4e449ab32 | -2.45937 | -53.93346 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59618135-713d-33c3-aeb6-f417791ec0a4 | -2.7227 | -45.29163 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bea551b7-63ce-3194-8855-d7bd92158cf0 | -4.78644 | -49.74976 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31802453-ff5d-332a-ba6f-212cea9376d0 | -2.56835 | -53.97561 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89ca1957-b9b3-39d8-82e6-9b47022a99fa | -1.60967 | -52.40078 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52fde210-7fea-3059-b8f3-8140b872ccf5 | -3.23776 | -50.30804 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f6e0da1-1b96-3553-9843-5ff28cf44470 | -2.88262 | -53.96855 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bc92555-f3a3-3754-8774-d3f5a36992c7 | -3.14597 | -54.48096 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79fca29c-1830-3596-91fa-ee7ca2a66cdc | -1.44315 | -51.67085 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5c6c359-e171-3400-8099-97dff0fef619 | -2.62767 | -54.27129 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49e3ac6b-e22e-328d-b61c-77b6d1e5fecb | -3.46126 | -56.30983 | 2024-11-13 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a6d6e03-d89a-31c3-bc1a-1321f27e4cfb | -3.83829 | -52.26424 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 750cf527-8e25-379d-b1ff-5a48758fa01f | -1.65269 | -52.53925 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8796c6df-8a9e-3bd9-9b1b-e2eb3522ed0b | -1.39611 | -52.39605 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97390ca4-e92e-39e6-8687-2fe66c14fab8 | -2.58104 | -53.98109 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaee310a-afa7-38ed-a6c0-64b8dec4d904 | -3.87778 | -53.69565 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4dc0da04-fbb5-3909-bd3c-068d92d1a065 | -1.7606 | -52.67701 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82fcf50e-b2cd-3c62-b3b1-16be44c49fdc | -2.28463 | -53.74451 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19646ad9-c660-3925-9eaa-00c793ddb790 | -0.89676 | -51.7314 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02ce5b5c-37d0-37ae-a1e7-99ac050f485f | -3.15142 | -59.15467 | 2024-11-13 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb583729-a580-3b8d-9b3e-b5eb59462ff4 | -3.09028 | -50.48944 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fb0160b-c50f-392a-af2b-130bb9294c54 | -3.05683 | -50.34293 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 29fe050f-6b57-3a49-9bae-0e458136dbbd | -1.41907 | -51.11705 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 333d1c35-ec61-3f5a-8db8-0a4abbb7248f | -2.93933 | -48.31557 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c73811c-f23e-37d6-b9b1-4b9377f3c736 | -3.24571 | -50.30489 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README35.md)
