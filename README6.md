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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40e8f22d-59a1-39a1-883a-2a8ec07482cf | -7.49429 | -47.03273 | 2025-10-25 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8f54db8e-91f5-3a50-b158-e2568bb11c5f | -5.38311 | -40.72726 | 2025-10-25 00:35:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 90870ddd-fedd-3dbe-9e22-931dab9a64c9 | -3.76549 | -48.93108 | 2025-10-25 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 27c9d34d-0f12-3214-9407-42383d3c2034 | -3.8301 | -50.19361 | 2025-10-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| cc1bb75a-4262-3b6d-8d5f-e1289f25190e | -9.45784 | -47.73227 | 2025-10-25 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ae1c334a-3862-352f-986f-cf5820957a86 | -3.83132 | -50.2024 | 2025-10-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| c52a43e4-9f98-331d-8695-2a718dc1e578 | -7.98791 | -47.38959 | 2025-10-25 00:35:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 15269d91-530e-3195-92a2-e662000c01e2 | -6.416 | -46.17974 | 2025-10-25 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3ae23197-c58d-3e4b-8b6a-61efdb1cb424 | -7.05282 | -46.75481 | 2025-10-25 00:35:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dfbeafd1-cb34-3621-bee3-2a33fd7a4254 | -3.90432 | -47.77095 | 2025-10-25 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 109a4657-727d-3f1b-9af9-ef80c9696de9 | -4.69674 | -46.44366 | 2025-10-25 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d5f572bf-ec68-3dc4-ba84-7438d4f1e262 | -5.62691 | -51.79924 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| dcfc3f41-fb34-3f63-8f59-68ad1c723547 | -7.37461 | -47.04611 | 2025-10-25 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dbdca799-a96f-3b67-b6d4-c4df50ca695b | -7.16629 | -45.84047 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 6e144767-a574-3074-a0ce-22a1e357208f | -6.79744 | -46.47043 | 2025-10-25 00:35:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| c02093d6-1147-3523-9747-3aebcfb5db67 | -9.74876 | -47.83365 | 2025-10-25 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0a48e621-7c5d-30f6-ba90-a7a6a5267b2c | -2.87097 | -50.71758 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2e61af41-5473-3a35-bb95-acfdaa999962 | -3.29574 | -50.19785 | 2025-10-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a9b07326-abe1-3274-a994-1819fab4247d | -1.49382 | -47.81719 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 71fd9e13-b57c-3d2d-ba81-917065de10c6 | -3.12321 | -51.2095 | 2025-10-25 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 216f5333-80be-3467-89a9-794fa990c4db | -1.50896 | -55.85683 | 2025-10-25 00:35:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 7cc038f1-828a-33a6-88e5-407e1eb2c4fc | -1.07777 | -49.21991 | 2025-10-25 00:35:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b1a62128-215f-3297-9c83-adaba3e3ca54 | -3.22557 | -49.35475 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| da4e4c24-f981-3bb2-a258-67243ca7f61c | -2.81844 | -49.14571 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 10656026-b86a-3708-9f04-c42cacb3a6d6 | -2.89503 | -49.16693 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| a87bef9d-0b12-3f1a-bf68-de46b16d120d | -3.58916 | -51.78375 | 2025-10-25 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 183c2ded-3dff-3b62-9b47-ae6053c6cca2 | -2.74232 | -48.67167 | 2025-10-25 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 39c131a5-a585-35bc-adc4-ed42e62bb7ec | -1.59553 | -48.03177 | 2025-10-25 00:35:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6630d51e-0212-3b87-91ad-6502dcfa8e7e | -2.69041 | -54.76485 | 2025-10-25 00:35:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 94884b36-bb6c-3035-a34d-cf6d4d51b7ae | -3.43411 | -50.25587 | 2025-10-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| add7ff2f-10ae-32b3-aa97-36b42572dbe2 | -3.7253 | -52.44751 | 2025-10-25 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4509ce82-fe2d-36d2-a59d-370fd87abdfd | -3.08479 | -49.47039 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 80149431-bfeb-3807-a03a-395fc2124851 | -2.26756 | -47.85396 | 2025-10-25 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| b31c42f8-10c3-3aa4-8feb-a10c39937cd3 | -3.77955 | -52.03088 | 2025-10-25 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5806aab2-3718-34e5-b632-265c15abf292 | -3.26194 | -50.14874 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 25c3c91c-0b18-3a50-adff-8b0f094da7bb | -1.92531 | -52.14382 | 2025-10-25 00:35:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0ab526c2-5b84-30b9-babc-58743f746162 | -3.80955 | -51.91156 | 2025-10-25 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c29888ef-b71a-3564-9688-a60742a278f3 | -2.90409 | -49.16565 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d8f055d3-7d95-354e-94b4-747b7ecc3758 | -2.86215 | -50.71882 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1a6034be-de88-335e-b9e3-db0d3cab6d5f | -2.26601 | -47.84305 | 2025-10-25 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b272536c-36f6-319e-ab56-c08408d6dc09 | -3.22684 | -49.36387 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b50e3f74-8cd3-35b4-9894-ff9cd86cb73b | -3.22429 | -49.34561 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5fc3d414-e1c4-3129-9e53-3509152cda42 | -2.78914 | -49.59531 | 2025-10-25 00:35:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3793be50-9615-302a-93d8-9471ceb21519 | -1.49435 | -47.81079 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| d849fac7-fec0-3257-acb9-26a3ebc98cdc | -2.8003 | -49.14826 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| deef133e-fadd-3aff-bb49-8b56235f2ba8 | -2.66525 | -49.49862 | 2025-10-25 00:35:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1fc922f9-2bd7-37d8-a9ee-118a993cfdea | -3.1678 | -48.60644 | 2025-10-25 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| dada067d-3a00-391b-ab7f-f00d2f790878 | -3.15422 | -49.17464 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 40bc2158-7376-3076-91e5-64ad519f7468 | -3.43533 | -50.26466 | 2025-10-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b27d389d-17f5-3e80-9010-fd95214ba5a4 | -2.79899 | -49.13897 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| dcfcfe3f-5fc7-309c-b4f9-8200ed89c74d | -3.25453 | -52.90677 | 2025-10-25 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fcfb7d8b-b841-3c22-827f-8a0ec88617f2 | -3.87054 | -51.88768 | 2025-10-25 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d8ddbfc6-02ea-3b43-9ebc-8ddc2d9ba0fa | -2.72755 | -49.15542 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ab2217e4-5b5d-393c-a764-11efc0623916 | -3.28817 | -52.54782 | 2025-10-25 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d076ad9e-c963-391c-8622-c50a022c6d85 | -1.18618 | -53.40583 | 2025-10-25 00:35:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 71a3a1c0-d1c7-3bcb-89ce-478bb1e6f309 | -3.85178 | -52.28426 | 2025-10-25 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2fa664b8-d22a-3dfb-88f4-fba8559cddb1 | -2.81068 | -49.15629 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 14b97673-efc6-36db-8f71-d9914ddda953 | -3.72397 | -52.43762 | 2025-10-25 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 4ff712b4-1ab8-3a2d-84e1-dc86b127c15c | -3.11434 | -51.21075 | 2025-10-25 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f87ef612-a5f0-390a-af9d-022e85dcb785 | -1.59547 | -54.30821 | 2025-10-25 00:35:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 50fc5166-e8fe-3486-a41e-b871b06499e8 | -3.48405 | -50.08099 | 2025-10-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9918c5cb-01d3-3094-b733-c81d98855d12 | -1.49229 | -47.80601 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 783160e6-07fd-34c4-8c8f-ac360f7804c6 | -3.14241 | -50.61662 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 688475bf-218a-3dc5-a689-4bfb623a5b04 | -3.87182 | -51.89702 | 2025-10-25 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 83279472-043b-302a-90da-6a861c38e38b | -3.14468 | -50.16214 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 1fa89399-29fb-3bea-9600-4c6695f1c7da | -2.93769 | -49.00846 | 2025-10-25 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5b2890b8-84b2-3602-99b3-d877b2dcf42d | -3.09627 | -51.27676 | 2025-10-25 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2776124b-f572-36e0-a61c-569d5963b3ee | -3.23404 | -48.75829 | 2025-10-25 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7291e196-852f-3b3b-875c-a48dc6c56119 | -3.09233 | -49.25864 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4ca9c708-3928-39b1-9d84-7258b60b446f | -1.78778 | -53.99772 | 2025-10-25 00:35:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ab9aca2e-7990-3fea-8374-0c6331f87ae6 | -2.80806 | -49.13768 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 947379a9-55dc-3b86-a9f4-735b4035adb9 | -2.80675 | -49.12834 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 65e59e6b-9183-3d80-ab6a-6dd5342cb471 | -3.10291 | -50.20131 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 86dede39-6f61-3154-8183-8f32020f2fc5 | -3.16376 | -49.17634 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 515703fa-031b-3f82-b71e-7834e58f8c9f | -2.58058 | -51.34911 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 187c2f03-193a-316d-9251-9f50fda756dc | -3.47714 | -49.90178 | 2025-10-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6fa767be-7e5c-3ee2-85b8-f23bdc0d1f1b | -2.80264 | -51.36034 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e4f962ac-7e21-3151-8190-5c9261a5c5f0 | -3.14346 | -50.15334 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c222c813-6096-38b0-a17c-67755e8f6af7 | -3.10412 | -50.21011 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 27019f94-7026-3193-a6c6-0202bf26e58e | -3.29453 | -50.18904 | 2025-10-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3ae33d20-c078-3928-a6ed-4def5d5cacf7 | -3.05139 | -50.42952 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| edca6aec-d6c0-38e6-ad01-9b0af2b60290 | -2.94657 | -51.52894 | 2025-10-25 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f4000590-8613-3e0f-95e2-e751c7d3fd96 | -2.72886 | -49.16476 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| eaf52793-9290-3a8f-97b1-3c77a8cf963f | -2.89634 | -49.17621 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a6c23632-f529-3ac9-a202-c1f1515c631f | -2.80937 | -49.14697 | 2025-10-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 6587a63a-9618-32b4-8bb9-cfc9f72b3a0b | -3.14441 | -50.22503 | 2025-10-25 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4b5f3bc6-de52-32f8-88da-626b349919e0 | -1.30667 | -49.3395 | 2025-10-25 00:35:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 80a072ef-2800-38ef-aeac-fc8084c07f1d | 0.36163 | -50.9282 | 2025-10-25 00:37:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5c008cc5-2945-3a45-8c35-0f11893bbcda | 0.17639 | -51.40528 | 2025-10-25 00:37:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a9f724d-6bfb-374a-9811-36f25c4619aa | 1.64969 | -55.7199 | 2025-10-25 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 44758500-fc9c-3079-a750-f6879d4b2573 | 0.36285 | -50.91941 | 2025-10-25 00:37:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f6b9d0ee-904d-395c-8fda-da05084d9fb9 | 2.58342 | -51.32881 | 2025-10-25 00:37:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ca2634e-7c46-3cfd-bb00-e7806fd2fe3f | 1.63508 | -55.74507 | 2025-10-25 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 999fae83-2677-3fba-ab95-3c4ba807aa20 | 0.37139 | -50.85785 | 2025-10-25 00:37:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 565d6b7a-b625-3580-b170-a1667db5f5c4 | 1.62407 | -55.79206 | 2025-10-25 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| def19ee4-02b8-36fd-88b2-0b8f41d314c9 | 1.64411 | -55.72642 | 2025-10-25 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 77d3cbc5-7142-3b82-af09-538760e76e30 | 1.46207 | -50.90382 | 2025-10-25 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8bf8dc07-6974-36ea-add0-6ecdb2b0ce3b | 0.44784 | -51.03569 | 2025-10-25 00:37:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f764e2b9-6aed-3fa8-b98b-e72b42d66f6c | 1.64226 | -55.73983 | 2025-10-25 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 95fcb37d-8857-3164-b3b1-a864921062a3 | 0.37017 | -50.86665 | 2025-10-25 00:37:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.5 |


[Clique aqui para ver as próximas entradas](README7.md)
