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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d6f1666-a4a5-3d17-9930-df5a0434baa3 | -12.49839 | -53.84991 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07bfe3a0-3262-34c6-bd65-7517775b3ac3 | -10.16273 | -46.25057 | 2025-09-05 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5f61e9a-d5fe-3395-a07c-528bf735bfcc | -7.81974 | -46.08612 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| febe2e79-3333-312f-b32e-5e451dcacb49 | -11.3196 | -55.22815 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c60eedd2-6a83-3ea3-b339-6e65af95d856 | -7.61851 | -55.2635 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ac720b72-7030-3b60-b6d0-bb57942c5bfd | -7.72073 | -50.32632 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b81c61fc-2f1a-35e4-8bdc-10b98b820920 | -12.90118 | -56.93914 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68fd9430-3cd7-3f4c-ac98-09a4b5a0a08f | -10.06268 | -58.38802 | 2025-09-05 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d48b863-d20c-3733-9967-19fd1440d5aa | -10.51929 | -57.77716 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d879277c-2786-3240-971c-f6d431991ef8 | -8.08171 | -47.57857 | 2025-09-05 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 754a0ad4-cde8-3d3e-bfc4-042e7eed420c | -11.54986 | -47.31564 | 2025-09-05 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdc7d169-17c3-3f29-9d26-bf090f559524 | -9.50154 | -57.81637 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bc28d14-53f0-38f0-9d0e-fd4258e766b0 | -9.7032 | -48.98811 | 2025-09-05 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7c91680-8225-324d-99ad-6a341b7430ee | -5.53258 | -57.24716 | 2025-09-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 995fd3c0-60e1-31af-8584-57a3b637ab7e | -10.52916 | -57.78298 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3131019c-d9b1-394d-83b5-193511b0336e | -5.91934 | -57.72152 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1200417-7cef-3b70-928c-516e34fb0450 | -7.07401 | -46.19787 | 2025-09-05 04:57:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 122ed6a1-4ad2-32e0-a947-49cac646b6fb | -12.21277 | -54.30305 | 2025-09-05 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9837462d-8549-3cf7-abd6-b46ff12f9e96 | -8.48396 | -45.0621 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fe89468-7d33-34a8-910c-c4182b0a8eb2 | -10.97557 | -45.96473 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6a009dfc-ff72-3f96-b99b-1ae7b8620972 | -6.26496 | -53.44337 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8b6c355-75b7-33e6-8ef0-2d7569142cf5 | -9.07081 | -47.01067 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bc92c008-94ef-34ed-a66b-254bb6ce367b | -12.87856 | -48.01713 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83e1d64d-ae72-3533-b181-f78ad3c470f4 | -5.85741 | -57.77423 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bf43e139-e8e2-3039-8ce9-3770b61b298d | -11.49178 | -55.51469 | 2025-09-05 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 045d3c4d-4c21-3bce-a3c5-ec4c7f72de96 | -8.02011 | -45.41278 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 847db923-79a7-3139-8493-4b7572f5cd0b | -7.05545 | -50.8587 | 2025-09-05 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82202173-a028-35b0-a36c-badc23e48de1 | -9.63727 | -47.10067 | 2025-09-05 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c0753c6-e822-3d7d-aa4e-80319622408e | -12.98488 | -54.81959 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6be4683a-c473-34c0-9596-e3b01def1f8a | -5.89427 | -57.73551 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eac3bea7-3245-3b3b-846b-7471f35b35f9 | -13.09774 | -57.1106 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d0d65cc-aa62-3281-b916-34a7190ef048 | -11.58285 | -52.10709 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eea32b03-8270-3a5d-a9a0-11696b241bd4 | -11.6543 | -54.51796 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 236474ec-877b-307d-8036-91d2956d41de | -11.98906 | -46.75569 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca05fe9c-5538-31ab-af10-16843bff9c5d | -12.50461 | -53.83174 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15c7ca45-ee59-345c-adde-cb28b1082aa2 | -12.64153 | -56.98596 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f101757d-cdba-3658-b70f-3fda80c22227 | -11.10268 | -52.02397 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58e5a9a5-8b38-3a96-9ab5-29aca39debbe | -10.88296 | -55.39124 | 2025-09-05 04:57:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 75a07d78-7fbf-373b-9174-5a0f257e23ca | -6.87158 | -52.7874 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d5dcdcd-e392-370b-be8b-984a469b1eb9 | -11.09514 | -52.01964 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3ffab69-f2a5-31fb-8bba-2cc9af18303e | -11.61794 | -52.20198 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 863f4856-b85b-39a6-a768-2494597822b1 | -10.97287 | -45.96428 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 411c27b1-535f-33ae-97a9-b44dab5a403b | -10.03698 | -48.13736 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3192380-9406-3b35-8a30-f75bb87df3e8 | -9.70486 | -51.07282 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bee6e7a-b015-3f63-a174-6bba8f57eb34 | -11.58476 | -47.89287 | 2025-09-05 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67b19219-7c03-318f-a311-691687e3bbdf | -6.82469 | -52.81345 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d5a157c-8ad4-3b00-80f7-38d34c970291 | -7.22326 | -44.82888 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8a7df33-4090-36b6-a2c8-7f38da65df81 | -10.97691 | -45.95455 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d8e863e0-edaf-3e22-add1-86772707c1b0 | -12.91497 | -48.03777 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50624678-89de-3548-95bd-447805a71da6 | -10.22756 | -50.53915 | 2025-09-05 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bba883f-4bcc-3dbb-9d56-7e75631fdf5a | -11.00397 | -45.93415 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e58c5eb7-88cc-3e6b-86cc-e47d68b135f3 | -12.26661 | -50.15506 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87f31a94-d3ba-3f59-bf4a-d3ae53c7cbf1 | -12.53252 | -49.10413 | 2025-09-05 04:57:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a20ba85-6caf-3667-ac64-bfd0c6a26470 | -8.88924 | -45.73808 | 2025-09-05 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| add7114a-8acd-3d56-84ce-a3fc1fbf54d9 | -11.74436 | -47.75173 | 2025-09-05 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1b16a41-a739-3a2b-9f37-8d91e7a2c928 | -11.20299 | -55.01857 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8207b99-fad7-3706-bf39-b630d10b2ccc | -13.09715 | -57.11425 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 315cec0a-7aab-30dd-9a17-c9833db2696c | -12.98265 | -54.81188 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed976c1a-ae1f-386f-aaa2-b80696910544 | -8.0904 | -45.48063 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05baab6d-04e7-3d27-8a4d-7e40daf98763 | -5.90907 | -57.73782 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4ea4b54-f9b8-3e04-a046-ff54f286d57b | -5.90312 | -57.72789 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1da4725a-1f22-37b6-a361-e75929c1ce8c | -12.90911 | -56.99656 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14dda107-d767-3c0b-a3f8-14da71c6d98e | -9.07796 | -46.99464 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6a1bf1d7-7ec0-3759-b0b1-d2560f10278c | -12.72001 | -45.08613 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3d5ea658-b21e-3bd3-a735-e517599b8a33 | -12.018 | -43.79028 | 2025-09-05 04:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2ea4266-8e20-3a08-9728-5701efe70897 | -11.98946 | -46.7525 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e58f485-2c4d-3759-9fd4-e90a46d928a6 | -10.97067 | -45.98204 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 325be49c-6a91-371f-afc4-7f23a95a8364 | -11.39466 | -43.58868 | 2025-09-05 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb35a399-1da4-3482-8196-4316a477fd8e | -9.41716 | -46.79028 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc5ed3b5-6ac2-38b0-93db-d1e05eb15940 | -12.96741 | -54.78395 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ad878dd-a64f-38fc-9971-01145da40fcf | -7.36367 | -44.32531 | 2025-09-05 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d24879c1-58f2-39d9-b88c-4a3d68701515 | -9.32371 | -55.22155 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16d34452-1114-3bb8-9094-20c9d4141f07 | -10.482 | -46.75669 | 2025-09-05 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44c40c8c-6423-3d0b-8822-02dec20e70fc | -10.32156 | -58.72269 | 2025-09-05 04:57:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6968918d-df7d-3db0-8cfb-600bf2fe42c6 | -12.6437 | -56.99382 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cda6ffe-b8ab-3c1d-a203-40cf03335035 | -9.32646 | -55.22557 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5db10a7b-fe9c-389c-8e07-798d4830510c | -7.97633 | -44.5261 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18a0f348-669f-3319-a418-c98f784768f5 | -10.9733 | -45.96081 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2b9219ac-3437-394d-a22e-8db98534506a | -7.90032 | -44.93259 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90ded409-7491-326d-a06c-44bdd4438bb0 | -7.72545 | -61.52562 | 2025-09-05 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71ef06a4-abda-3451-9e6e-fe529f063968 | -11.97074 | -46.77608 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 414af191-5989-311c-bd62-93472d1ea359 | -11.00853 | -45.94147 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afe07e83-6a2d-3482-a552-19108e7a4107 | -8.86507 | -47.92337 | 2025-09-05 04:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34e82bcd-fa1f-32f9-a498-0e39aa1b45cf | -12.99156 | -54.82066 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3b0b8793-b0ba-38c1-99e3-65f55d1ee5d7 | -12.96351 | -54.78702 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0fdc733f-92cd-34db-b0a0-4d8376b233c5 | -9.8781 | -46.54572 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34493700-93b1-3033-8ab6-822f014593e3 | -7.71621 | -50.33051 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbf2548f-8fb9-30d0-ae4b-187274b1baa6 | -12.51597 | -48.07636 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6134c334-bdd4-36be-8c84-694a47e4c23e | -8.07268 | -52.3466 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09c603c8-dd38-3b99-a741-5b6aa79d50ea | -6.33603 | -58.183 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23c8e625-6814-31e1-8e32-c1fd907e89b8 | -7.68759 | -50.25799 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 04b136d4-ee42-338e-b66b-1f575cd7c430 | -10.9643 | -45.96736 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7880ae1-bdc8-36c8-983a-87d746422ad3 | -12.48887 | -48.09244 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9012d8a2-7fe3-395a-b670-a80c10e73b47 | -12.52194 | -48.06742 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbc7280b-add9-336a-93f0-525f26a8d658 | -9.08067 | -47.01112 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f986138e-b525-3875-93ed-accef5fb6070 | -8.31011 | -55.10159 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c701703a-b230-38b2-a300-53b88c4e11a8 | -7.30353 | -44.067 | 2025-09-05 04:57:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 608fecf9-ecf3-3a30-ad2f-c420a5e15d39 | -8.52199 | -51.31929 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cdabdf6-ec58-3b24-9066-67f2f427c03d | -12.99713 | -54.8289 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 090b619e-dcdb-3ecd-8627-91064b9b3574 | -6.33648 | -58.18074 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README52.md)
