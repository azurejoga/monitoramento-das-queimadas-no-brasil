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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6afea239-2ab1-35af-b0f8-333cd62024ec | -7.43734 | -41.87886 | 2025-10-27 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9f98096a-1c46-3c08-bc12-27b2eef1b510 | -9.25152 | -45.56818 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1461de36-9115-3971-b043-8ae5fd76998d | -5.30689 | -44.87613 | 2025-10-27 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc88463f-5830-36e4-8e35-48a58910f823 | -8.05831 | -54.9247 | 2025-10-27 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a47a2b39-5b09-3acb-a419-41a2dfe122bb | -3.12139 | -49.11109 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56f70c34-e702-3a26-9036-585d0b4a563f | -5.01619 | -41.03823 | 2025-10-27 04:32:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 972d0617-ae14-3769-aac8-312f39c568e5 | -9.55474 | -46.93425 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfb67afd-b3cd-34d8-a053-99cff745359a | -3.29468 | -50.19368 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37393a69-4b42-3862-9ad7-b500819e191e | -7.03923 | -41.64215 | 2025-10-27 04:32:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce088cac-4fb2-317f-9131-462badda1597 | -6.53853 | -41.61498 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6ba7e2b7-6a76-3199-8747-85cbb6cc72a5 | -3.9832 | -48.99098 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 234beb96-e6a9-33f0-94c8-44317ba39b14 | -5.77731 | -51.55927 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e92fed8f-261a-3706-b062-f3d1d0721601 | -6.25946 | -41.83472 | 2025-10-27 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a1618f4-9c6b-3d1b-b769-f422a8ee7296 | -6.59544 | -42.66758 | 2025-10-27 04:32:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 75c16880-96c4-3cab-b2cb-e50db5a8c1b8 | -6.13011 | -41.71066 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e3804b3a-6610-343b-95b2-d3b7ed682953 | -3.12431 | -50.15176 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 60883932-1634-3cdf-9a05-a4e37a0ff451 | -6.57791 | -48.76672 | 2025-10-27 04:32:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac1b4be0-b3be-3f35-b0f4-a75050d2c712 | -8.53027 | -47.20562 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5db39e8-05ae-3b68-9a08-e048720db24c | -7.16502 | -45.65203 | 2025-10-27 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26448788-5b9d-36a5-b134-58a2dea01222 | -3.70524 | -44.33393 | 2025-10-27 04:32:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee20e50d-b767-3670-8eeb-be2e451920a7 | -5.69894 | -40.80799 | 2025-10-27 04:32:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 101ae858-057e-3316-a143-d2de72d2e484 | -3.11028 | -51.21243 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c448f2da-518a-31ac-b51e-b73e655eed7b | -2.08331 | -48.36809 | 2025-10-27 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9ae5b48-c035-3b44-a2d7-ad079230c8e2 | -7.03825 | -43.93313 | 2025-10-27 04:32:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0663435-ad5f-3b93-b35b-27710d02f0c5 | -3.0452 | -53.01556 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c35c8738-b91b-383c-aad9-cc99643bb6dd | -7.3774 | -46.54229 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bcb57567-0b8f-3894-954c-d0d8f8d7e141 | -4.15531 | -46.79338 | 2025-10-27 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 890e0f67-7d82-3237-920b-7575486e438e | -4.83573 | -45.35793 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ecff2fc-076e-3388-b675-661c24249f92 | -7.82443 | -46.44067 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 22ec00d7-af4b-3407-9a4e-4ff5ad47887b | -5.07188 | -44.73288 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fcc69f8-2678-3ad4-a721-ff2b895cb675 | -4.45922 | -45.4535 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| cd364231-8b50-3f21-a21c-3f49a3ae7fb0 | -6.09936 | -47.00231 | 2025-10-27 04:32:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed3095c2-b55a-332c-8a5b-b6ceb602f395 | -3.31517 | -50.11246 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59d3d104-2cf9-36f9-bf00-508beafdcd0e | -9.60387 | -45.48439 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 965e58d3-6356-373c-96a7-374ab2a0d056 | -6.6713 | -41.5116 | 2025-10-27 04:32:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 59a055fe-2877-34ae-a758-f3cbf81f8d96 | -9.55922 | -46.92752 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a790b867-d0cb-31b5-aad0-19c494897b29 | -2.94307 | -51.75838 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e30521e1-0ed8-3f56-a3e5-68cf4c4b93fa | -6.88446 | -45.15189 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cdd2dc92-b8cd-318e-acd6-d9ea62d3a2bb | -4.42477 | -45.97683 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7081267-7fd8-3255-afc9-778d18db6a4d | -8.22989 | -46.92648 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a20e556-7cc2-3c9c-bc55-88d13fa560e5 | -3.21933 | -44.43301 | 2025-10-27 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 372baca0-b0f6-3a03-906a-b28931357cd7 | -3.04949 | -53.01624 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4097ae81-afb2-38f9-b7c0-46c43f8c667b | -4.95481 | -44.88074 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce61b839-5600-3d3c-ae54-33de5c683224 | -7.5988 | -45.6809 | 2025-10-27 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82ed9787-2ade-3b45-b6ba-98c670a4bcf1 | -6.18866 | -47.80471 | 2025-10-27 04:32:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0833277c-dcd9-318b-8176-a20c31a5c62e | -7.82388 | -46.44429 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e44d3eaf-110a-384d-b947-6438f4a511ae | -3.58473 | -43.601 | 2025-10-27 04:32:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f66670fd-a0a0-37fe-98c5-0cb4a1e21df5 | -3.72042 | -47.65728 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f46a6640-a1f6-3683-ab50-5a246627d405 | -7.96313 | -45.4711 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9be9fb20-b980-3405-865d-0ed2c47426d8 | -6.14605 | -43.12806 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 06158d7e-b156-355a-b1ae-d3107a705a74 | -3.7836 | -51.9367 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbb6a2ae-af4c-3512-9c36-b4382d002570 | -6.10674 | -41.75217 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 53c51cce-5d29-3361-8027-4e1b92539879 | -7.96769 | -38.28018 | 2025-10-27 04:32:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6573368a-f2f6-3fe2-a821-20cc545f4a02 | -4.83629 | -45.35424 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 804ce47a-a7b2-3fab-b418-2fd5322b09f7 | -7.53624 | -46.25848 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d7311d0-5f52-350d-b1f9-822adbc4adf9 | -8.01013 | -47.38015 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9f185d0-0e22-390a-8c6f-239e8ba5b1d6 | -4.45691 | -45.46827 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a05336ee-d66c-3b52-8f47-812fb332cb40 | -3.24016 | -50.64633 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 90171a28-d8dd-31d4-b4cf-fd15707acdeb | -6.69043 | -42.05263 | 2025-10-27 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b00ff956-603d-3631-b10f-f4ec3deb2729 | -4.27021 | -50.51741 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 581fc490-f06b-39fe-ba13-8b935cf634a0 | -4.88992 | -48.65758 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b35538e-8797-391e-8a40-17e5a4ff5c1c | -7.77458 | -45.39949 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92425b4b-642c-30d7-8fd8-ac93645fd83a | -8.0129 | -47.38417 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8e19825-cf38-3dac-89ed-0d10ac4c58be | -3.75827 | -47.61021 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3154c1d8-d6ae-3b2d-88a8-02d9e4c3d88b | -10.21406 | -45.17315 | 2025-10-27 04:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7172d135-7e2c-3010-976a-a4bb4584306c | -4.44503 | -45.45506 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee5ccfe3-de59-3157-b5d8-2f69ede4c551 | -2.87023 | -54.20829 | 2025-10-27 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5450ac6f-1b61-3c4d-a18c-a876b63ad19d | -7.77633 | -45.38778 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7972cb86-3890-3809-a2ad-f7d425cd8bb2 | -6.37567 | -44.26109 | 2025-10-27 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8554d59-3f74-3ddd-aa5e-cb15ab2814a4 | -7.23766 | -46.94358 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba5e65ad-4903-3218-9f61-303026e22d06 | -6.18026 | -43.73829 | 2025-10-27 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f6a1323-45ba-355c-b457-17a0e9814f4e | -6.88606 | -43.57574 | 2025-10-27 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bf5fdf10-f3b0-3fb5-82b8-69d4c90de54a | -3.13503 | -53.005 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca76c176-b388-3065-aa3f-643c678a8867 | -4.32945 | -48.09043 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d9e4bb4-056d-34be-806b-c29e1c934840 | -3.13568 | -53.00095 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea317b94-b0ab-341a-b7d6-0f1c4328ffdc | -4.21903 | -48.35939 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 227c7d87-3edd-38eb-b4e2-1ae16bdd1f12 | -3.62022 | -42.77702 | 2025-10-27 04:32:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7896dbdf-0c1a-3e33-88b9-1d205bea0300 | -3.11049 | -51.20594 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9399d79d-6139-3eb8-a54b-a61add7fc695 | -7.77808 | -45.40009 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f80904a1-138f-32e4-a7ca-6bd88a42e8e0 | -3.47313 | -49.96566 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9ff16498-7d4a-33b6-b464-9c1c1c0e6e8f | -5.71136 | -49.30716 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3533e8f7-d99b-3a8b-bc56-dae28e5d5f77 | -7.8374 | -46.44637 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25c7ec73-c34e-3528-bddc-46e37fa187ed | -9.56926 | -46.91748 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6786577-9213-3feb-8243-49af355dd072 | -4.9635 | -46.67149 | 2025-10-27 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b04b3b51-f73c-3124-8e3b-be88e27cda73 | -9.86421 | -44.88257 | 2025-10-27 04:32:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e658ed23-0755-3763-ace1-03e9d7bbd022 | -3.48063 | -50.07884 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 789417eb-542b-363f-8b27-30f37200ee95 | -7.0266 | -48.21035 | 2025-10-27 04:32:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b8894ed-8915-3ef0-8c8f-6eccebee0307 | -3.72797 | -49.68891 | 2025-10-27 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7c79b4c-4cf3-39ac-a8f4-c5605507db57 | -6.98557 | -44.00428 | 2025-10-27 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f2937b1-116a-37e5-bfb0-dc6a6d559204 | -7.85492 | -46.46753 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59d228a2-a1d6-3a0a-bce9-94d2b752be8c | -4.44153 | -45.97939 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 41737919-46f7-3888-bb64-81d64ffe108d | -8.21396 | -43.80648 | 2025-10-27 04:32:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c52d270c-f259-39b2-8eb6-97468db88483 | -5.88782 | -41.32579 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3113c149-39f6-3023-a19f-bd5272d2b70e | -8.112 | -49.11728 | 2025-10-27 04:32:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ae187e3-4788-3232-acf6-597865cf679b | -5.65401 | -41.10443 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b7c9b64d-c89f-351a-96db-6556a0c8c397 | -7.85321 | -46.4561 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 750d0d19-df1c-3d55-a84d-ae00d8dccbd8 | -8.3119 | -46.18521 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be7e1f61-f835-34e0-9201-0226c4fe0fbc | -2.69471 | -48.45941 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8217557e-649a-349c-a995-fabc3a242c85 | -9.13004 | -51.2985 | 2025-10-27 04:32:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f86a68-7be0-3e99-9c8b-02cc14753395 | -9.28036 | -45.59342 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README39.md)
