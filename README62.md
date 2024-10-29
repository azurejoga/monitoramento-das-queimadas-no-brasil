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
| 4f5497f0-feae-346d-9840-6a1346df361d | -5.05006 | -49.94024 | 2024-10-29 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73cc8680-2e7c-3708-892f-b6ce5e762f4a | -4.94169 | -49.57058 | 2024-10-29 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e3cc3a3-ee2e-3587-85c0-380f5edc8553 | -4.86964 | -49.98295 | 2024-10-29 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17073be0-4925-3c72-8ea8-b83c4fbe3583 | -4.86908 | -49.98646 | 2024-10-29 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5e1d9bb-ca42-3336-a5e7-05366405ad31 | -4.80488 | -49.79044 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0c749d0-4f98-3b93-b484-f9559cc6b6d7 | -4.73494 | -49.39308 | 2024-10-29 04:40:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 220ee7e7-9f78-3942-a25c-4736535f05eb | -4.73164 | -49.39256 | 2024-10-29 04:40:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf173e62-8a8b-3ba8-8422-c292e35fc387 | -4.60018 | -49.36426 | 2024-10-29 04:40:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7a77ba7-3fdf-3bee-9045-6fac43b7f9c1 | -4.46561 | -49.7189 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 399d2c2a-d2e9-38f8-a254-63c0049e76cc | -4.46229 | -49.71838 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f01bf583-a435-3b1a-8bea-a807ac1eed9f | -4.40694 | -49.72395 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4df5649e-ecb1-3aae-a998-c44a80a8f26c | -4.40362 | -49.72343 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1669915-8042-312b-ba5e-e5c620f83988 | -4.39205 | -49.75369 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fab08962-411d-3090-8836-827a311cb940 | -4.38818 | -49.75665 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fae1e724-4804-3691-93fb-a8589d6fdb87 | -4.13971 | -50.22546 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a64d652-166f-3dc9-8ff9-f9d36aa589ca | -4.11274 | -49.25909 | 2024-10-29 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eb58ca2-0aab-3873-9db1-4a6e7656cdf3 | -4.09586 | -49.98993 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bad875ea-ce50-3df8-bea8-9e233fd14216 | -4.0953 | -49.99345 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a584db8c-0ba1-3171-a6ff-7a52b9b76c1a | -4.07411 | -50.01905 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32eddabc-a4be-3243-ac1e-4e17530924e9 | -4.07077 | -50.01854 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 969b89f4-4830-3c47-81e9-feef6100cead | -4.06908 | -50.02912 | 2024-10-29 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5219b7b-cc43-35bd-9944-657ab2f8bddd | -4.06852 | -50.03264 | 2024-10-29 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2809df0-897c-351e-8778-3a2532959389 | -4.06574 | -50.02858 | 2024-10-29 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7efb6e3d-68e7-3c48-820e-94214d3317d8 | -4.06518 | -50.0321 | 2024-10-29 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15b0bd88-02de-3786-ad57-e55a5e4ecff6 | -3.99059 | -49.98804 | 2024-10-29 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b76abc13-d583-342a-8f42-68a063c4bc23 | -4.59968 | -49.38889 | 2024-10-29 04:40:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a69abaf8-10b5-379a-922d-c14f27ac95a2 | -4.51196 | -49.66211 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5ce7c82-f00d-35fc-bf65-7bfc4501c3bc | -4.46284 | -49.7149 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6da2cdc1-c735-3550-9d73-425fea8e50a3 | -4.41421 | -49.78572 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61539460-4965-3f7c-878e-b198cdc912eb | -4.39259 | -49.75022 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1481f8e1-b90c-3aa9-9819-9f06826a7955 | -4.1155 | -49.26305 | 2024-10-29 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d7ed95b-6f5b-35e1-acd2-69d9190d5cd6 | -4.10264 | -50.52145 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 225cb608-1414-3efd-9f6f-68928c0dbcf0 | -4.10206 | -50.52506 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 52d3d29e-6820-3a92-a26c-bfd3eeb1feba | -4.10148 | -50.52868 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ff022872-ac8c-3b65-bf38-1ad1f545c5cc | -4.1009 | -50.53231 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 83327e42-22b2-398a-856d-1b624cc6cbd0 | -4.09868 | -50.52454 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3e0cd66-4475-38fa-a4fa-cff0ce560a8a | -4.0981 | -50.52816 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba967134-a024-318b-8494-c8feeb998e48 | -4.09751 | -50.5318 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9352eeb-8fc1-3bab-8530-29fa8befe1ac | -4.04367 | -50.5569 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4bce9f9-9bdb-3e40-88f0-70f993c61597 | -4.0431 | -50.56052 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bea80ff-853b-3b86-8039-c90e87fb1e6f | -4.04144 | -50.54909 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd61e097-7d7a-332a-adf6-d340ff573320 | -4.04029 | -50.55636 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a77810f2-0807-3a4e-bc64-435c1b31bac3 | -4.83134 | -50.92824 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdb0481f-d978-312f-a8ac-7b030623e84f | -4.74544 | -50.82773 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06c575fb-743b-389d-89af-a86db718e7d7 | -4.74486 | -50.83139 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ff2932d-45d4-3ba7-b0d9-8c84471e1417 | -4.73198 | -50.69463 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2d2487c-fb5d-3102-a450-2c4b099c54f8 | -4.73033 | -50.79156 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eec5d862-3cc6-39e6-a0e3-8f9f238e447a | -4.65377 | -50.4604 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00d3f6aa-a431-38fa-b05e-ae757274512e | -4.6532 | -50.46398 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7c616d4-d244-3cf2-9f95-2140ffc8009d | -4.64983 | -50.46346 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1174438b-6d7b-30fe-b84d-b5126e93edee | -4.64926 | -50.46705 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b91df8ee-d2f4-3475-9408-afd33c5f425d | -4.62541 | -50.63703 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b86d57a-0032-32bb-9312-95e32816f7c3 | -4.62483 | -50.64066 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05a5799f-55db-37fd-a8f8-5acab7d7128d | -4.6083 | -50.56045 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e47669-5970-39d5-9c6b-67ddeff64585 | -4.60773 | -50.56405 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad6dbdea-99dd-3e7d-81bb-7eed9a2b90f4 | -4.60493 | -50.55991 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc45dba0-bede-3fd6-9934-2d13eddf26a7 | -4.60436 | -50.56352 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bd495f1-670c-3eae-8028-109015ad76ba | -4.58944 | -50.65775 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3652a466-60ca-31cd-8a85-e16c6102fcce | -4.51246 | -50.50038 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6329c230-3d45-368b-87e9-3602bdece636 | -4.51189 | -50.504 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1365998c-c0ce-3e1b-a8f5-f1800a7429c3 | -4.50813 | -50.75334 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83df8279-9e9d-33c1-ae8c-67f9197d44bd | -4.47883 | -50.64729 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eaabb5d8-03f1-3eb0-b1ab-ffdd15f3d58d | -4.47825 | -50.65091 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff70bdd5-f93e-35c9-b878-f5157dec8b24 | -4.47544 | -50.64676 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b82cbfc-0108-3ff4-abd4-82964713c4cf | -4.43156 | -50.72587 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 792e02db-2026-3d46-bd3e-71787ea6a95f | -4.42707 | -50.47234 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1434d95a-07b4-3cfb-8c93-f003db09c0f0 | -4.42428 | -50.4682 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82da5592-58e8-3fa7-a14e-766b9c793085 | -4.4237 | -50.4718 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7266159-703f-300c-909d-dfeeb68f10e2 | -4.39084 | -50.8059 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f17ff91-f5dc-3886-9583-7f9922d95de9 | -4.37694 | -50.44997 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30ebe715-3e91-31f4-9729-d43dde352424 | -4.33712 | -50.56956 | 2024-10-29 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00d70059-bd38-349b-9ea4-98910a59b811 | -5.51754 | -49.80415 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4b171a0-8b21-3903-8774-ee60e934ecc9 | -5.90757 | -50.1128 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a124de1e-7373-3ba9-a9f2-ecc916b30177 | -5.85015 | -49.98164 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b90c706-840f-3703-8ed4-74d95f6402cc | -5.82032 | -49.9342 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31b32390-9c7a-3bfd-9769-2f313444eebe | -5.81037 | -49.97542 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b752a4e0-2bac-37d8-bb15-9475222e53a6 | -5.67736 | -50.14757 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bce599f-e5f8-3aa7-a091-472f999d1e2a | -5.66312 | -50.00198 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1004f884-756c-35fe-bf40-bf8336ae2378 | -5.6244 | -50.01026 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c806d28-45bb-3b7c-93c3-95c0ef586cbb | -5.60338 | -50.05696 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cdaf769-361e-3c56-92ef-71ab78c6cad0 | -5.60282 | -50.06044 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1be8ef2e-df32-38d6-b96d-eb61d9641512 | -5.60227 | -50.06393 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e5360c1-e197-369f-8578-5ea7ab9b0831 | -5.5995 | -50.05991 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb57ab2d-b134-39a3-8d43-62f6be964c79 | -5.52085 | -49.80467 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6138e317-e231-33b0-a9af-d678b4481d78 | -5.51809 | -49.80068 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8e5ab5c-ac7a-3785-9368-4e923830a1e6 | -5.20894 | -49.94722 | 2024-10-29 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9115697-9623-3e40-92ad-6b96bbde5e8e | -5.13088 | -50.05322 | 2024-10-29 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fcf9f3e-cd63-3298-99fd-605082cd03d5 | -6.40266 | -50.78894 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 700b86b8-04b8-3aab-83b3-04d9ca054379 | -6.40209 | -50.79254 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e72d5b36-2daf-3367-b5c7-efad773971bb | -6.30937 | -51.19833 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ac570a8-4c19-34c2-8456-0929f438abf9 | -6.21907 | -50.86694 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 243f3dd7-1409-3312-ae2b-880e7c50039c | -6.2157 | -50.86643 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a65b52fd-1a1c-3442-b2ad-e17359cfc651 | -6.21465 | -50.8515 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df6b4691-4225-39ca-85ff-dd402ee5c662 | -6.21407 | -50.85509 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26f36768-e943-32fc-8679-ef758f30f64c | -6.21349 | -50.8587 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5bcdde5-2afa-3041-911e-54315256df98 | -6.2129 | -50.85129 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea07def1-d45a-32a0-88a6-87ebc53dcdc3 | -6.21233 | -50.85489 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0da0947b-18b9-3c8a-8a3b-2d6b4c8c3fc0 | -6.20616 | -50.85024 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be6cb354-37eb-3be5-8f85-3c34f7b73080 | -6.20337 | -50.8461 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da37521a-95ab-3f82-ac07-5dd89c89fc9a | -6.20279 | -50.84971 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README63.md)
