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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e17f4b2a-e3b0-3b90-9d22-cd181abac191 | -4.75176 | -48.59529 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec8d0e2c-9443-3ce1-8714-4d225df94ac3 | -3.67341 | -54.04298 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 91266342-e35a-381e-9c7b-d91629c5150e | -6.14937 | -41.14812 | 2024-11-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 60aa5b38-5bd7-3f66-87f2-55e4b195fb0b | -1.73464 | -47.82455 | 2024-11-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 43ddb309-0257-39ca-a6fe-6392236d1952 | -0.0448 | -50.78623 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9f156c8-b540-3ebd-b5ca-56529b87d4e6 | -1.34517 | -54.62383 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 24f72840-cc13-3877-9532-c429a3b4db1c | -3.13076 | -50.44753 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9a3b3786-64ed-3e18-87c4-86336abaeb5e | -3.52082 | -46.36586 | 2024-11-10 04:14:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5489dfb9-5703-3f15-be32-d100b52dd5c8 | -4.54373 | -44.63156 | 2024-11-10 04:14:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26343406-4cca-3945-be16-318490ccfad8 | -4.38715 | -47.27031 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec5e7c27-97c0-3a79-b3e7-89492900c5b3 | -3.66551 | -50.26311 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1708ac9c-94bf-31fd-8649-3b1b3d8954f4 | -4.24339 | -45.37739 | 2024-11-10 04:14:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7e93886-fd09-3666-8d3f-cdcce7287e24 | -5.36403 | -48.90879 | 2024-11-10 04:14:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73ef25b5-403e-31ac-b143-f62a1546b282 | -4.36072 | -47.22919 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d24555cc-8513-3257-8442-fc8b4b32773a | -2.91388 | -49.35713 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e48cf04-83c7-3ca6-b33d-4acd9c8d008a | -2.97572 | -47.92462 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69ff64be-c5a7-361d-a518-e910ca4c786d | -2.08417 | -48.82 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7e31a4bf-9803-3be7-937a-2e4f3076725d | -2.69715 | -51.69437 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5e7df9b-6045-3f2b-8110-61b7c1340033 | -3.25369 | -49.58508 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 628517c3-d35a-31f8-95e5-f41af634d857 | -2.39279 | -54.09926 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb995f30-24c2-3c9d-b14f-165c85854f57 | -2.62661 | -46.16042 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb353c0f-3713-3b17-91c5-88b45a4eeeeb | -3.3534 | -51.68122 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a55562fc-aa3f-323c-a495-c31493099ea2 | -4.08593 | -42.93535 | 2024-11-10 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9cde7aa-6846-35a9-88a9-588565af9b02 | -3.18713 | -43.87616 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54a9cfbb-5ff7-3e62-a23d-4a7e84544553 | -1.53882 | -52.21769 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7cce2687-6c22-3368-9cc6-dc7ce558b13b | -2.1153 | -52.1229 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35286506-3644-3b32-a427-761e1e3cb1e6 | -1.03659 | -47.79421 | 2024-11-10 04:14:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 67a94527-86c8-3596-8288-30f2cffb615a | -2.24387 | -46.55746 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4a5b796-01aa-3996-a767-37bcab3482e1 | -1.28592 | -53.71675 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 46d4012e-bafd-3b62-8bb1-ce51ed759313 | -2.23153 | -53.77776 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6d607f4-9c72-333a-a523-04a9d9ea82c4 | -4.62913 | -49.08379 | 2024-11-10 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e6da2cd-02df-3a31-9892-9367f83c7808 | -4.38948 | -47.27337 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0db48211-ab70-3829-8cab-9627dea64c12 | -1.68418 | -48.47438 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fec47dee-aff7-3410-bad7-71a2daa90eed | -3.21763 | -50.39028 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1b158c76-2db7-3973-a416-a7badab29dca | -3.84069 | -44.12819 | 2024-11-10 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4250363b-e164-36c1-9d67-9c87e0d485e7 | -2.63769 | -46.76207 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 839491e9-a7bd-3ea6-91cd-aa5c05b699ef | -3.03486 | -51.09586 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1d1b1be-cc32-306c-b3b9-3d2aad435de7 | -1.72509 | -52.46099 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa6ce2c0-532d-3d37-ada2-abad81f3307d | -2.67787 | -51.94184 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cde1091-cf03-3524-b756-bdbfba5e68dd | -1.15403 | -53.79189 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c0d924e-88ae-35c5-88af-2218895b1c23 | -2.22929 | -46.55045 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c3b98ef-ad95-3e0b-a12d-b40e4713744d | -2.69355 | -49.83704 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 00c7f3e7-3a4d-3ba9-a845-6fe190c2d5a6 | -3.40989 | -47.58461 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e47e506-175f-3f1a-961d-501cf6463116 | -2.9085 | -49.24721 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e79e8b24-e1dd-3cc1-a6f4-99a52eb613ac | -3.96141 | -48.17229 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 873805e0-9224-3948-b668-391a66753c82 | -3.47322 | -50.38287 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fc79bca0-821e-3f5d-ba50-73ac1af68206 | -3.98685 | -49.98815 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48307396-2eee-3f97-9773-a07c43ad142d | -2.55018 | -47.32472 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0e3ad2b-0772-3d50-ab34-bdde49b02b7e | -3.52716 | -50.00192 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57ab1299-d11d-36ff-a0f4-11d96bd2534b | -3.12673 | -50.44122 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 73f42e58-7b5d-3b69-9571-dcc4523b73ba | -2.34757 | -48.92699 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dbf599b-a0b3-3ffa-adc5-352912cbd873 | -3.46615 | -50.18995 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67594da8-7438-325f-95ea-fd9a4ffa07e4 | -3.66721 | -54.04218 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83acb9ca-fed9-30aa-beb0-5c549eeb8836 | -2.30056 | -46.74774 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7843b1a-681d-3f11-9d87-1344e9982a7e | -2.25566 | -46.83088 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 911d5fb4-3d3b-3244-acd6-631cde0bf2c1 | -2.39536 | -50.32043 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5e7d8016-f6dc-3a87-88d6-8a16e457343a | -2.23315 | -46.6239 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c901575b-9ffd-34b0-b4cd-acd746d0696b | -4.05723 | -49.28897 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ad4cfe07-ad9d-3783-8b7a-849af6c44442 | -2.08925 | -48.82683 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a5c06bbf-bd73-3a67-a5cb-cb9e0d46f480 | -5.94221 | -44.76012 | 2024-11-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d55614f0-5cc9-3852-b952-6fe05ebfbc02 | -2.92416 | -51.67299 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 462bd86f-9347-34ff-8f15-ec4ffdfbb879 | -4.27721 | -50.67301 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5fc9c012-2d83-3f8e-a198-d0a2c8740f8a | -4.28046 | -50.66974 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 43c8ec7b-3db8-36e1-95e7-5d11a19076ba | -2.09626 | -46.5393 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fac2e7ff-8b5d-3572-bc9e-727e08040b17 | -2.71589 | -49.30042 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b88ac057-0c3f-3af4-9e72-420a5d2cb60b | -2.46605 | -46.87417 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08fe10a1-8dae-3291-a1d0-dab1f1e63782 | -2.87005 | -50.41252 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 58d436b1-f72c-3758-88d4-1bb63307a3ca | -3.53813 | -51.25154 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 074791a5-c0a9-3691-a42f-bbc4de326afa | -1.05559 | -47.89323 | 2024-11-10 04:14:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd392989-ad35-369b-b013-2381174b9d74 | -3.44721 | -50.75206 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f83bc205-6b3a-3a11-ab16-5bae3ebba1c7 | -1.24588 | -51.76355 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 428137b5-1202-3d9d-ac08-7908206bc81f | -0.04584 | -50.77972 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ca4352e-b208-3d20-9d04-a5b416711481 | -2.42478 | -45.54762 | 2024-11-10 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f5928afd-42df-37f6-9c24-8cb1c37a57f2 | -3.95897 | -48.18718 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8a227ad2-3df6-3420-8d54-9ddf4ac08def | -3.11453 | -50.20724 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 412eb1f9-0ced-31b5-bf51-9f9bf84f6773 | -5.01629 | -45.03944 | 2024-11-10 04:14:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1be46221-1a3e-368b-b89a-e821140a912f | -3.52405 | -40.90601 | 2024-11-10 04:14:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eabfe4bc-b181-3d98-80da-4778dcb6e959 | -4.10292 | -49.12578 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 00e47d91-126e-3be8-83b3-11b7734788b0 | -3.04256 | -49.54729 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| aab1142a-35e8-36d7-bea0-10221e1e7362 | -2.20372 | -47.73882 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4ff92401-1c01-3763-9a58-010664cb354a | -5.31173 | -46.23365 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8ff7dcc-49ea-3c64-a77c-ec9fe308c927 | -1.71134 | -50.20005 | 2024-11-10 04:14:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48726c03-b21b-384a-aabf-df7326e76313 | -3.03664 | -50.32873 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8c55295-c810-356b-a809-5364f8a4e048 | -2.56993 | -48.1882 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5fa2259-95a2-3e1e-8f63-0dee80d396ac | -2.88565 | -48.30154 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ad3a34a-d835-3811-ad36-dd9942ec687b | -2.17008 | -46.41372 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a573f7be-b9e3-35cc-a34c-fccafc8651f4 | -6.48211 | -47.50573 | 2024-11-10 04:16:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ec32cc13-bfff-3a17-b39d-10100bba760e | -11.03047 | -48.79502 | 2024-11-10 04:16:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a1b4234-1ff7-3899-8fee-8508dfe1c89f | -8.39443 | -44.14268 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b74ba7a8-0899-3fbb-9a84-0dbcdc14716e | -8.41316 | -44.13137 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec6d9597-6285-34e1-8a55-e9a157658e21 | -6.48737 | -46.8547 | 2024-11-10 04:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5905c091-a1c7-3e4d-902c-ea61dbc526e9 | -7.94597 | -43.17944 | 2024-11-10 04:16:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 75eb352e-6829-3538-9d9f-f5c05e8c751c | -7.48149 | -43.60573 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04bc9296-5381-3826-ab2b-e2787d79e4ec | -8.4016 | -44.14025 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffa5bb7a-650f-3009-86e8-d77ad565232a | -8.38836 | -44.13816 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ca9b536-3482-36a9-bb7b-6efbd9527648 | -8.40491 | -44.14077 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a94e6ff5-4278-3232-bba3-e7227f2cc90c | -8.3748 | -44.13546 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8163596-43b3-30c8-b2dc-cc3349cd07a4 | -8.69205 | -47.9578 | 2024-11-10 04:16:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e75eb047-ad81-3126-bef1-d2685bd4559e | -8.38615 | -44.13069 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f52c576-c45e-3271-b2d1-e6fc9d95b322 | -8.38396 | -44.1446 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README51.md)
