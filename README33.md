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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 190210d3-b331-3520-914f-b92e6789514f | -3.08494 | -52.92245 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| df99b8ca-a16e-3f6f-b66d-9384fe8fe5a9 | -6.12906 | -52.63985 | 2025-11-09 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87584010-b72a-39a2-95e2-51b7ffe336ab | -1.72491 | -54.67597 | 2025-11-09 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 259a5cd7-63d1-3924-8dbd-e5c6f7e90374 | -3.32293 | -50.15415 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20762ed0-70b9-3e52-8507-373bd06c9e10 | -3.45622 | -49.97013 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7048cdf4-4098-3a78-8a48-2929f7b570d5 | -3.86426 | -51.21781 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d2d0005-3e8e-3cf2-810a-b6db337f1b5a | -3.08539 | -52.9226 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 04cb8818-5652-327d-9c38-31d525cc4229 | -2.71617 | -60.01025 | 2025-11-09 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19d9db97-e0ab-3826-84ab-beb80dbbbcbb | -3.41383 | -50.26271 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89853e0b-42ab-3415-ae34-c47124197d14 | -3.09759 | -50.31906 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4a9ac0e5-d101-331e-a305-ed1bc0cb9281 | -3.03837 | -50.30502 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd2777f5-15be-302a-8b7c-44b00a3c94b8 | -4.28163 | -49.90506 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85bbddbe-c867-3905-acf2-0a4addc3fd85 | -3.05724 | -50.21613 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba41187e-066d-374e-b0fb-a54285355009 | -3.835 | -51.1262 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 70c83543-d025-31c0-a26c-a26c6742b8b8 | -3.86662 | -49.38348 | 2025-11-09 05:29:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a74a1fdc-84e4-30c4-9163-022214063d20 | -2.92161 | -52.51532 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60b3f511-b60d-3ee2-b595-4104c88f42ae | -3.79535 | -48.90184 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aba59c89-2c67-3df7-8ab5-30144510c9ad | -3.34736 | -53.2256 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8952296-d58d-32e2-8877-10f6b304a6f0 | -3.31411 | -50.12927 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45786536-f050-3495-94ee-10c3f072357c | -3.75521 | -52.10645 | 2025-11-09 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6ad758e-d3de-3c9c-883a-1722b35ac8ad | -3.5626 | -51.12517 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e0c505f-7f85-32f6-9105-6a700c6fbd24 | -3.50181 | -50.04472 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c7925a6-d13b-3fb7-85cc-8d7bf8ab9f93 | -2.87633 | -53.1553 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb31ee8e-3b48-39c1-86dc-6b472a8837fb | -3.04815 | -58.73235 | 2025-11-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9267bbb1-df5d-3184-9117-6c6d7c52c486 | -5.09843 | -56.15845 | 2025-11-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3524082-83db-3e1b-a657-678c288701d3 | -2.98061 | -48.70845 | 2025-11-09 05:29:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64aabc3f-f330-3f21-8989-080b486e1406 | -3.79681 | -48.90529 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26c72adf-e9c0-33cf-ab37-d1ae74770e6a | -3.12343 | -50.14325 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abd4d69e-3638-30a9-ac10-479cdce68ef0 | -2.98689 | -52.82067 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5d85457-86ef-333b-8aff-e06637d32f08 | -3.83436 | -51.13062 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 83496c31-b964-3f7f-a5f2-aafccec2ccd0 | -4.28002 | -60.01799 | 2025-11-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27dba44e-8ae2-3cd5-88ad-00dbff063efa | -2.94504 | -49.35759 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b4f6e9dc-1b30-3bf1-b95f-a80a17777503 | -3.95621 | -49.02937 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46403b70-dd38-3368-a761-b166291e3c34 | -3.09834 | -49.26394 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e05687a-0026-3309-8ab7-f4e494590efd | -3.45702 | -48.81742 | 2025-11-09 05:29:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9061ea3-3833-366d-8f2f-e998a4cf18ba | -9.62378 | -68.59824 | 2025-11-09 05:29:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d7ede33-6a1d-30c7-a534-6488f7328433 | -3.65613 | -50.27668 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b0b9ebf-bcee-3f6c-afcc-ba340372a62f | -3.32353 | -50.10713 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02e71b8e-eb63-3f31-bf45-c664dfc7fb04 | -3.58106 | -53.52164 | 2025-11-09 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbc92938-ca63-3222-aa9d-1ef97b39c285 | -4.40373 | -49.66348 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83e1a839-fa7a-3701-894d-cb07256d39af | -3.36024 | -51.28693 | 2025-11-09 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4be69fc3-e67d-385c-a395-9c940c06e5fb | -4.61736 | -49.65799 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db208b64-4bb9-3bd2-be7c-6df1654b489a | -3.44114 | -52.63857 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64bc036e-dcbf-37c9-8a82-12373ac1de14 | -3.10359 | -50.31986 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f87f30b9-1341-33f4-886a-b2d05b12a6d7 | -3.09754 | -49.26923 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 399cbb3a-77d6-33be-9f88-bcb7af91b829 | -3.31745 | -50.10614 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f0e2defc-568b-3128-9d4a-7f2b4e5f790a | -3.40449 | -50.453 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46108902-be1c-370b-a28d-7257dc9eed0d | -3.33403 | -52.56422 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3efd2bf6-2b08-36c3-8c52-f1f6d180e7d5 | -4.37651 | -55.88832 | 2025-11-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9aae4c6-47db-33b1-bc1a-bde0e1c5410e | -2.60755 | -49.21679 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 848abf76-08b7-3274-be19-9fd6a598831b | -2.60601 | -49.22721 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cac5aa02-21b6-3950-8cb6-cc0310145abe | -3.84297 | -50.74856 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71a52f1d-7383-3246-8d07-76a9bf490056 | -6.80486 | -59.42741 | 2025-11-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0c52dab-fda1-3c9f-baac-4fb5e7e18ac5 | -3.68967 | -51.38882 | 2025-11-09 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ef5f82a-6957-3ad6-b72f-592f2b2f8245 | -5.09789 | -56.16222 | 2025-11-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2f5518f-79d0-3863-8081-080d187dca95 | -6.04839 | -58.05135 | 2025-11-09 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a2153ee-b035-3b55-89b4-4dff82526631 | -4.37038 | -55.89185 | 2025-11-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 936503bf-07ea-374b-8ae3-3b021304571e | -3.09629 | -50.32785 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d0a70ca4-c635-3887-8e4a-0bf1cf63c10f | -3.46834 | -48.82063 | 2025-11-09 05:29:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4cc35752-ebc4-3889-af07-a11822cbb527 | -3.95075 | -49.02948 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32a56151-41d5-37cf-b68d-67ac3492f352 | -3.47021 | -48.81956 | 2025-11-09 05:29:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9084549-f6ba-35f2-88d2-11c1c6d5e202 | -3.05661 | -50.22054 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0ff0bbb-70c8-3d2b-ad69-9446e4932c10 | -3.10293 | -50.32434 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8204254-5f96-3fdb-a034-8cd898b65e1f | -2.66714 | -54.76581 | 2025-11-09 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 885e7e07-77bb-353d-8c93-ae6200dbeb9b | -2.98259 | -52.82286 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ae33a56-2eb0-365c-95b7-170988d13f8f | -3.32917 | -53.24555 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a877791-13fe-3f95-9346-507d87a1962b | -3.09946 | -49.26703 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8b89751-2af1-3c1f-b5dd-d649fd4cfc92 | -3.35232 | -53.22632 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aaaff160-0f9c-3c95-9c30-96bc95179e9f | -1.85994 | -54.35726 | 2025-11-09 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e4a8b5f-cd24-3faa-a505-1cd7a08583fb | -4.39811 | -49.6574 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8508fe20-6258-372d-987d-fd6ff87987bb | -3.0916 | -50.31814 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 526cdc43-262b-3511-adcd-005584e0e764 | -3.3315 | -49.1281 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efdf6c7a-369d-32bb-bd5b-2cf139fea980 | -3.31543 | -50.12012 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf2beea4-e7ca-3cd4-9bc6-c65d162924ed | -6.05214 | -58.05185 | 2025-11-09 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c79d078a-485a-3509-903d-e84a9a2d8053 | -2.9478 | -49.35734 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a2e27c9f-f373-386e-86c0-fc3db7e1600d | -2.50731 | -49.46114 | 2025-11-09 05:29:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f243dd5a-ee75-3757-bd6e-d48bb4716db7 | -3.08583 | -52.91971 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9b957af0-3e37-3320-a0ef-cdc8df051f3c | -4.40448 | -49.6583 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| feaa679d-51c3-3467-bcc7-09aa7840aaa5 | -3.10334 | -50.19592 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 57347508-959b-3daf-9f1b-3a8050e1aa42 | -3.50111 | -50.0494 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 657c7750-4ccc-33be-b149-6676be38a132 | -3.86736 | -49.3783 | 2025-11-09 05:29:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0beb9fa5-69e3-3ed1-a185-8ee49c005300 | -4.22567 | -50.63912 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 465b0ac6-32c9-3942-a4ff-026376e6cead | -4.37177 | -55.8915 | 2025-11-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d13632f8-5301-3f45-87f7-830ef818f92f | -3.84768 | -50.74778 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a34221b1-cdf5-3ffa-b5d6-c73d8c306536 | -3.06075 | -50.22025 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e308e344-7771-3eb6-a1ca-c447811dbd8a | -3.57326 | -52.25792 | 2025-11-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e2e9816-6deb-3219-b9c5-9d7430408b7e | -2.60042 | -49.22091 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3daf9c63-36ae-34ac-b8bf-0e800019f6ac | -3.26351 | -50.04289 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acc1db5c-42eb-3311-b80e-b736c08484c5 | -3.9504 | -49.02288 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4b7f62f-6cbf-34c8-8bdd-60522052e2b0 | -2.98809 | -52.82079 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fab5bcc8-3875-35a5-89b4-7693a27a1985 | -3.50586 | -50.05959 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2129fed-51c6-35ec-992f-9ac4052cf96c | -4.40298 | -49.66868 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5489893a-def6-3ca5-bb86-c1809c974808 | -4.58914 | -49.39302 | 2025-11-09 05:29:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e80b56c2-aa11-324e-acb5-634151585ef5 | -4.15015 | -59.34205 | 2025-11-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e112658-cece-3fdf-8f87-355355a64159 | -6.62115 | -55.0164 | 2025-11-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca4d29f0-1fde-3b56-8ebb-2aacd2961ddb | -4.39794 | -49.77188 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae2f0c70-d9de-39ae-ac1f-a0f0e54e1c32 | -3.14553 | -50.28542 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3c93d38-a22f-3a80-a918-4f3711ae088c | -1.65728 | -53.71043 | 2025-11-09 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 02c8c5f7-ea0f-313a-8e64-8dbaa2227d71 | -3.92302 | -51.01034 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23f80cd5-8c9d-3aea-913b-129f12ea9dec | -3.86921 | -52.13693 | 2025-11-09 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README34.md)
