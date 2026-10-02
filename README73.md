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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b5aac60-fd8e-3866-9e39-4c94e3c58a7e | -4.06503 | -51.11667 | 2026-10-02 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1daf0aa3-0c5b-3acb-b78a-59b45beb044e | -3.28813 | -53.85147 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 789e29ae-3f6f-3b68-8b2f-26da44fe03c8 | -2.89048 | -54.1361 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 751372cd-0645-3163-b45e-da8c2abcf6a1 | -2.0487 | -56.86876 | 2026-10-02 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 74713f51-658d-3a31-bb59-256e7eba2078 | -3.00046 | -54.22963 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 838f75e3-af75-3c16-9037-7c6184885ff6 | -3.29456 | -53.85189 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff589631-dfa8-350e-84bb-353955333db0 | -4.29096 | -50.7681 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 328dd058-9934-3c0f-9b09-1fdebe2b5de4 | -3.28285 | -53.84176 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 310381ff-275e-3b9a-9f5f-22989e57b062 | -2.87843 | -54.87819 | 2026-10-02 05:33:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa939ab1-bc89-31ad-b7db-5ac048386879 | -1.45338 | -48.91549 | 2026-10-02 05:33:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8438e8a-a2bc-375d-8ad2-6a5b00654ddf | -5.86567 | -50.1607 | 2026-10-02 05:33:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 236d9e3f-0716-3ece-9ae3-56e08dca84ea | -2.90189 | -54.14565 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 923571bb-078b-31ae-a4f3-14d5a1a14ce6 | -5.85426 | -53.48377 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1c2ec60-b767-39fe-b57f-4e9cb5b09cca | -3.14378 | -53.7476 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe71dac8-00e3-3a84-a5ef-09c0d2f7ca9e | -5.86587 | -50.15888 | 2026-10-02 05:33:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 36f31eca-def9-30ad-9ab2-1bfc117f5e39 | -4.2885 | -50.78521 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e81964ec-dc97-3fb9-ae92-47ddce798b7e | -4.25978 | -50.74651 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88119e7a-94e3-3f8b-9ce1-b8f9f2ed5784 | -5.65686 | -51.36795 | 2026-10-02 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a128b1a3-878b-3883-98c6-5c7da8adc833 | -3.01956 | -53.8829 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a457b14-8007-38dc-bbc6-bf4c766f08bb | 0.31303 | -51.04595 | 2026-10-02 05:33:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d24b3548-4188-3848-bd58-07e32e1dda8f | -3.275 | -50.08689 | 2026-10-02 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1bb99ba-3406-3cd5-8974-5951ac988caa | -4.26749 | -50.76895 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 441b1669-2927-3649-927f-3b62dbc8cef2 | -4.36491 | -47.77562 | 2026-10-02 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54196318-df02-3476-ae7b-fcc7a95df38b | -4.01931 | -48.94617 | 2026-10-02 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df658693-c464-361c-8f70-dc9269e74e81 | -3.29307 | -53.84811 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 751cff0b-fcf1-33ed-8ad1-395fc6842d7e | -3.00795 | -53.87289 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eb94145-17dc-37f5-bbf0-da143e184483 | -3.01895 | -53.88689 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2bbd278-2a34-37ab-9955-a0e903edfd29 | -5.8594 | -53.48072 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d63c80f-d20a-328d-bd9c-7ae07bc77469 | -4.28219 | -50.78144 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 075d5fb9-ce13-3d2e-aac5-18e6eaf9f007 | -4.27621 | -50.75525 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1843690d-3d7f-3619-a0e0-08732f233a33 | -3.15777 | -54.07472 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1e1211a-c68a-37ce-ac9e-a32ded3ef908 | -3.2937 | -53.84407 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 28c45ee9-d56f-397f-84c2-e9ff73b15bff | -4.24846 | -50.74817 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b810572a-f488-3897-9cfb-7418a3b61caa | -3.02381 | -53.96861 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d33d2f0b-2d7c-3abf-9324-bbb68f1756ed | -5.30087 | -55.87513 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd66a7f9-6e7c-3a2c-9f43-7f8cd63395a7 | -5.87198 | -50.15771 | 2026-10-02 05:33:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 58e1dd52-22bf-35fb-9524-0c4b47aa8673 | -3.07327 | -54.37362 | 2026-10-02 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68e32d8b-f42d-3823-9996-17e7e158c720 | -3.29086 | -53.84716 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d0dd929e-836e-3624-a7a7-3bd1c74271de | -4.28899 | -50.78183 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6a86905-40f0-3524-8a3a-91cbca90bd41 | -3.01589 | -53.87824 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81593e3b-b6dd-3364-ada3-9d70dd460330 | -3.01895 | -53.97189 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2823ccf2-5475-3ab0-82fe-1c2563519d57 | -4.30078 | -50.77666 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef41c3b2-edc0-3ea9-ab20-3eb689332092 | -4.27091 | -50.78301 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b35665a-7879-3bd4-a6da-d1336ab58eee | -3.35793 | -58.07643 | 2026-10-02 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| faf37c60-572e-3bc6-8f68-0719dc4250b5 | -4.27278 | -50.77937 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 888796a8-1fe9-3520-854f-88a5c8690323 | -6.15161 | -47.46826 | 2026-10-02 05:33:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2178aafd-2c85-3928-bdd0-c287793869d2 | -1.69088 | -55.66796 | 2026-10-02 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdef6301-3054-30fc-ae53-b5798a2fdb20 | -3.58572 | -52.21833 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4ca5f62-57ef-33f6-b314-657b84f9cc9e | -4.25774 | -50.76017 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70607eec-b8a5-3aab-b2b0-e824525ebb51 | -4.27728 | -50.77733 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7becd140-94cd-3f80-860b-b5822ec5bfb6 | -5.8716 | -50.15997 | 2026-10-02 05:33:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 809a6c6d-86ea-3b73-b898-68e381b02878 | -1.61163 | -54.75426 | 2026-10-02 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ebba315-e74f-3ac9-aeaf-bb9bc90e1d95 | 0.63202 | -54.40467 | 2026-10-02 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fa49238-1181-3f5b-915c-7529ed0fcff1 | -3.14132 | -53.73466 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d80abc22-660a-34ce-9ff5-726396316270 | -4.28709 | -50.78557 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed8817bb-c47a-3a3d-a647-33df2850decf | -4.25487 | -50.74229 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7fe69b4-1c30-3e3c-b200-5c19edf3ccfd | -4.01999 | -48.94165 | 2026-10-02 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45b522ba-0ae8-3438-92a6-ac5c5d8fbd8b | -0.3802 | -51.75159 | 2026-10-02 05:33:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e46b1ad-e687-3d30-9063-1ecc5e6b7021 | -5.87503 | -53.50219 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55277291-fbd7-3722-8add-cdbb64d1a0a5 | -3.26942 | -50.08611 | 2026-10-02 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79375dd8-da1b-3e4e-ae04-3bf15d0b593b | -3.84881 | -55.80436 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3734414-5a11-3cdb-b7c7-733b9f86d2c2 | -3.02746 | -53.97318 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65bba50d-d9be-3446-8e20-357df74e239b | -4.25435 | -50.74582 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb96e783-7bc3-34c8-bdd1-4076c9fa4558 | -4.26906 | -50.75843 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e32a5605-3ec1-36e7-8eae-d32d984cab98 | -4.03776 | -54.23357 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c9538ca-369f-3b3f-a794-0552c534c18f | -3.13945 | -53.74695 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 207f3d3f-192a-384a-96c7-c2d82d462c75 | -2.90907 | -54.12724 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8ffe7a4-cdc0-3d87-86f2-89a9008c8932 | -3.28655 | -53.84649 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 3f0139d2-be51-38e3-80a0-d9a635d1445c | -3.581 | -53.46206 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 067ca35c-906d-39fa-a055-378ebb2aafea | -5.86625 | -50.1567 | 2026-10-02 05:33:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91863e7d-0aa2-3fbb-97e9-5ef0549a76aa | -1.64102 | -55.1278 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 543debfe-6af4-3b2a-a17e-fd5bf60e3df2 | -3.01405 | -53.89025 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3ee9f17-3a84-38b2-9207-5b35224a2bbe | -4.25725 | -50.76351 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 999bfc61-086c-370f-bf85-262bd538a29a | -3.1345 | -53.75038 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e04065e6-c919-3289-aaf7-233bb9594a6b | -4.19658 | -54.57798 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2166b88a-250e-33e3-a878-880d2882cef0 | -1.64027 | -55.1326 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b62213ab-4990-3d05-9d2f-808785d7d7d6 | -2.89167 | -54.12846 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 409d7a3f-4e54-301f-a52e-e6fcb8489a54 | -5.87104 | -50.16406 | 2026-10-02 05:33:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6782c653-d6b6-3944-afd5-91bf4aedf583 | -4.26415 | -50.75428 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97ef47a8-9fa2-3478-96de-5c8c5c24c58f | -4.29045 | -50.77162 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6e18c35-8f64-3ccf-89e7-f667b9545eda | -4.45382 | -54.90371 | 2026-10-02 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e182af1b-2363-3afc-8e7a-20c9926615eb | -4.28062 | -50.76312 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e78b7ce-7e53-3b32-8f7e-acc6e2efedb5 | -4.27324 | -50.77612 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6863b35-73a8-3ecf-a2f1-f31842c6d477 | -3.28345 | -53.83773 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 52ca1b4c-dd03-3b63-a22d-4efa26fc52cf | -2.89651 | -54.15264 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| afb9b1a9-cebf-3841-8a32-e776a95cfd12 | -3.17412 | -54.08125 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 84677ed2-8cf1-3d8b-8865-ace5a8ac06fb | -4.26959 | -50.75492 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee013669-aff2-3398-b56c-5d8a7d2c9dfc | -3.28446 | -53.84675 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 50a518c6-f5e5-3c27-9440-ddd810f0f01e | -4.26602 | -50.77878 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f524d66c-30c7-34f8-8d2c-80bbfc9e26d4 | -3.28383 | -53.8508 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 394684ec-e535-3c26-ac62-9f6bc9edb294 | -4.27521 | -50.76233 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 528c52ec-58df-317e-aea4-ff64a5cff38a | -5.85487 | -53.47955 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94e40d8d-28b6-39c0-acbe-940042db1542 | -1.60161 | -55.12653 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ff0c47c-a4dc-39cd-ae9b-6cfe07d2973e | -4.28162 | -50.75609 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eae9a085-bfe8-3ba4-8eab-542acaea9170 | -4.42807 | -54.8519 | 2026-10-02 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 11b48a02-ceae-3568-b59f-ec664edf87f9 | -3.01157 | -53.23584 | 2026-10-02 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29bc2729-9166-333f-8703-546f41524859 | -2.93647 | -54.20041 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c851e10-fdbe-3472-986e-9389b799aedf | -3.17115 | -54.10087 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ef89212-6977-346a-bd7b-881754a5f1fc | -4.86473 | -56.03605 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f74d61c-e37b-3179-84dd-373490fe9961 | -4.04145 | -54.23787 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README74.md)
