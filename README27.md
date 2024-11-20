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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c42ebbd9-cca6-320f-9e17-f79bc65c6642 | -3.2367 | -45.56439 | 2024-11-20 04:25:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c0159b9-93ef-3cc7-b941-74395f3263e9 | -2.87597 | -45.26156 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dd2755b-2c8e-3a6e-b7ef-675de7835624 | -1.90552 | -48.66935 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1034847e-4cf0-3a0b-b026-ff7f3eac7717 | -3.08821 | -45.97402 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3af1af99-2c85-3468-9e64-6277f80c1dd2 | -1.22575 | -46.78352 | 2024-11-20 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d980f026-b958-3d46-9b20-9be9abeaf55e | -2.22204 | -48.5319 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38d445b8-e0a0-3e3c-b489-64041e4932d8 | -3.78273 | -41.60676 | 2024-11-20 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7df30dc0-f4cf-35cc-81be-df82798bd0a0 | -2.6358 | -46.83854 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0acca98e-e7ee-3c5b-a8dc-4a2c290780bb | -1.20468 | -51.77719 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c0fbd5e-0d2e-3655-a67d-e63ea392a54c | -2.69351 | -46.23309 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f10d7444-071c-3054-9f03-de8b057216cb | -2.55535 | -47.07369 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7ee81ef-88a1-3cfd-88e5-6db08dfb3432 | -2.71281 | -47.7263 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b08ef23-c2bf-360a-bdd2-fb875d70dcaf | -1.8186 | -52.69481 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 586f8aef-cebd-39db-b505-12d12ab55bf3 | -2.60751 | -46.26228 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27ef3a61-38c5-30e6-b469-6c35c57b75fd | -2.84916 | -46.67416 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ccb22c7-329c-31d5-ae5c-ba5b4be598cc | -2.82822 | -45.13055 | 2024-11-20 04:25:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cee0767e-cb34-3419-9947-633d2b9de399 | -2.60085 | -46.19401 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1838015-3e51-3b60-9f67-9e81e0cfca84 | -2.26769 | -48.44669 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2d9d09e-cf0f-31c8-8fce-10e61f2aa3d4 | -2.49832 | -46.22066 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2df81284-42b8-3e10-8d51-d9a2eaf430e6 | -1.59378 | -50.44363 | 2024-11-20 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4362b5be-b947-38c2-8bf8-4833a758b54c | -2.72447 | -49.34303 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f8b64dd-b79f-378b-b398-ae97118b9cbe | -2.64491 | -46.21851 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc3677a3-074d-30cb-b1a7-99112fa8c332 | -2.29405 | -46.37286 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bdd2f1b-71f4-341e-99e9-7a7cc0cf5b33 | -1.11293 | -52.34605 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d59108e-44ff-37c6-8286-2ddaf73948aa | -2.83305 | -46.66808 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e33e236-c547-3804-9220-b37099868b29 | -2.5156 | -46.28351 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5e231e9-523b-354f-9f9c-98c98944e18f | -2.3685 | -48.56486 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 496c53e0-64fd-362a-bc70-1c9e3f1fcc44 | -2.28198 | -48.49432 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d8c92be-67c9-303f-a3bb-0b50726559f3 | -2.65627 | -46.14605 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41b2ecd6-a92a-3388-bb8e-80a7568a8338 | -1.41284 | -51.07747 | 2024-11-20 04:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2d3336c-fb60-356f-972d-2fa1433779a4 | -2.28831 | -48.40879 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3f3e963-8160-3f3f-9f8b-8d7769c29f7f | -2.8249 | -45.13004 | 2024-11-20 04:25:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c980e7a6-aac9-3061-b3ca-e892eac3f948 | -2.64416 | -48.83637 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54f157ab-6a78-370a-bdac-aef986473d62 | -0.88335 | -51.72682 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2000b64-2846-33e2-9454-c6f837c8b986 | -1.33674 | -52.24229 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 494ba8fe-6d4a-39e1-b5e9-525de7913761 | -2.36347 | -46.86481 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c1a0b47-8b32-3044-9304-747f1335b7ff | -2.78635 | -47.63873 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcf8dac6-9e3d-3c2e-862b-599d4c1c685e | -1.51903 | -51.55834 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8a3aae2-7b51-30fd-829a-6b594b273084 | -1.85646 | -54.2803 | 2024-11-20 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0747d0f6-f846-3554-b955-3ad75168d288 | -2.52034 | -46.40501 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56681730-100b-3564-8d83-f37234a9b1fe | -2.21909 | -47.22466 | 2024-11-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86a66e05-592a-3f90-9ce0-ae094b45ebab | -2.70899 | -48.66096 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0850035e-ef17-3ef4-8964-77282a3eaf12 | -2.70437 | -47.97997 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf01d098-3751-3516-9d7c-5087ceb1dc7d | -3.00435 | -46.96482 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6c498ec-8816-3565-ad0a-cc6e83bd1d44 | -2.91512 | -46.83897 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe0432b8-7c75-3d02-b8e4-c6348899db48 | -2.68558 | -46.1753 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f58a079-5247-34db-a754-96debcf99846 | -2.89352 | -48.27333 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a31c4e01-9808-38aa-9826-4cf214b797c3 | -1.26928 | -53.41439 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd919466-b6cf-301c-bf21-8fd5dd8c4248 | -2.35842 | -49.00232 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d68d37d0-c14d-393b-a261-815632713a6b | -2.65419 | -46.55041 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f49f3cdd-7784-3287-ad79-549bb530fab0 | -2.68843 | -46.20049 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f69e004e-a5a9-395f-a69a-9afffb7780fc | -0.9127 | -47.38681 | 2024-11-20 04:25:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7636d706-26bd-38cc-882d-af1ae211c552 | -1.87859 | -48.78647 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b393cc63-b14a-37fc-8076-ba6ad2f1837d | -2.84419 | -46.68414 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bafbcc61-ffe1-34c3-95a9-6ab39143ef36 | -2.5195 | -44.99394 | 2024-11-20 04:25:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c1ab554-4ce7-3c3b-8f70-dbbee10a6b2f | -2.17251 | -48.38369 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72a0ea48-683e-3a90-802e-e0cc7f145982 | -2.07892 | -48.51818 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ed429b7-1e11-3ea2-88ab-76922144fea8 | -3.4252 | -43.1646 | 2024-11-20 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b58711a-db4f-369f-80f0-23f319a2fee9 | -1.99993 | -46.6023 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c721dec-b29b-3433-8e30-2596ac35be7b | -2.72609 | -49.35685 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b42f271-386e-33ae-b41a-1ac392299e32 | -1.20132 | -53.67353 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 728f3068-c86f-3c30-9c96-7810d27ac130 | -2.68303 | -46.23501 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f854596e-46b1-3f3b-bc3c-bf537da3ae41 | -1.24938 | -51.75307 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a1c439c-8676-31d2-a606-9644bee4274f | -1.70695 | -52.48755 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4db005e0-1102-3c2f-8d0b-048d1f5197e0 | -1.21468 | -51.74324 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 067d41b3-2882-3c01-9a13-bf466e238344 | -2.66154 | -46.24231 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d8db7fc-4882-3c69-889b-798b4c304e97 | -2.03384 | -45.79816 | 2024-11-20 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 595558d4-045a-3214-bf5c-ed57a4a1d2b2 | -2.8325 | -46.67158 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a887b2a3-b952-31e5-a2ae-3df61fc5fd34 | -1.30494 | -52.26333 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f8bd5a4f-557b-389a-9071-3e21bd4cdc9d | -2.60417 | -46.19452 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ac35ae7-3c78-370a-8414-be00358733e2 | -1.06518 | -51.74992 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7307353-9619-3b88-a47f-8bd2af765ab9 | -1.44764 | -52.67065 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2b63bdcf-be34-3e5b-9d9c-9ea946b66c08 | -2.58208 | -45.59548 | 2024-11-20 04:25:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eae3a58-f725-3e7d-b6b8-dc52a8a0dc13 | -2.85086 | -46.68517 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76212b14-8160-30c2-8e52-d285855bd330 | -1.0972 | -51.74426 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1aa9be59-c1a0-301e-954b-d7ea72bd6810 | -2.88869 | -41.75789 | 2024-11-20 04:25:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba8e29ee-019a-3693-b032-219627e3e8fc | -2.6668 | -46.16534 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75dd6e98-67ac-326c-8dd1-74fcb2f2fe96 | -2.68581 | -46.23898 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aedf1432-aad9-3855-b9dc-3a4e52274679 | -2.70736 | -49.09601 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e1237415-58ff-3483-82f6-04e7f733cf44 | -2.84807 | -46.68116 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe1a42a2-2a5b-3690-8f32-09376f966294 | -1.39223 | -55.62428 | 2024-11-20 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1536a1c-b1d1-3680-b5df-65fd63322770 | -2.63171 | -48.48462 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cc022d1-116e-3dbb-abe2-0886e0517460 | -1.20096 | -53.68133 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e49abb6a-415f-302c-86bc-de4a30266e58 | -2.47594 | -45.86379 | 2024-11-20 04:25:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d63347f-1429-378a-ad81-31b5386ffab2 | -0.94382 | -51.71824 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cbff990-0978-380e-a0a3-82a17bb841a8 | -2.85249 | -46.67467 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57452a3b-e799-363f-a01f-41fdaaef2227 | -3.14573 | -45.90902 | 2024-11-20 04:25:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1895315-ac44-3639-a960-de4f450d2826 | -3.00115 | -45.44002 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 520803c8-c115-3cbc-a80e-46a3be0e5c5a | -2.69189 | -46.24346 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab30996e-d053-34e3-b268-307a9c64a5e3 | -2.1832 | -46.99035 | 2024-11-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b249acbb-48bf-356e-b272-83b5553d330e | -2.68411 | -46.2281 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8da04303-6561-3bbb-8132-dae0b7d58d88 | -1.62049 | -52.25971 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27c352ca-bb67-37a5-aa47-3c7afe042327 | -2.68027 | -46.07924 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd2d225e-b8c4-3224-9802-1088052309f4 | -1.64349 | -47.36096 | 2024-11-20 04:25:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcfdccc5-bcde-3c0c-ac37-f073604fbd39 | -2.23641 | -46.8272 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d887caa2-5d18-3ed5-a8b3-016f3c8d4b48 | -3.58658 | -43.6269 | 2024-11-20 04:25:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfbeb382-2663-372b-b6e6-52b065f90098 | -1.89262 | -52.62099 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6113c936-834d-356d-a42b-5bb9b82fef2a | -2.67972 | -46.23449 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ede5d121-aeba-3ba5-ac84-8a512c3e1b55 | -2.66826 | -47.00326 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42704eb2-b8d0-3d94-8ebd-00923c1b4856 | -1.15015 | -53.5144 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README28.md)
