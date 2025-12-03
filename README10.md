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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6db0695a-03e5-30bc-ac68-861c6b6ff286 | -3.24367 | -45.55337 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa117807-ac3b-3162-9649-2d5be041a170 | -1.98252 | -46.48081 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2426c5b-1da9-3011-97af-4fb6d7b202c7 | -2.49375 | -48.01844 | 2025-12-03 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dd88f39-4d15-363f-b67e-3af40a19816d | -2.40087 | -45.89135 | 2025-12-03 04:38:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2432a15f-3ada-3ef2-a47c-2ff719c36d0c | -2.40277 | -48.96916 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d3d719b-3163-3767-af83-0a623bc58b6d | -6.60875 | -37.30664 | 2025-12-03 04:38:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e6d0138e-9855-3ded-8b2f-4ab61cdebfa0 | -3.23218 | -45.55589 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8fbf3ba8-d196-3fc8-a380-267ed0c6a0a9 | -2.62262 | -45.13895 | 2025-12-03 04:38:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 40fa4e28-c4e7-37dd-83ec-bec7db5a79ce | -2.83612 | -50.46687 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 32d5129c-be9d-3cf8-a48c-409b6dc30882 | 2.00015 | -55.70614 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7cb4558-2367-3ff9-a254-e78587de032e | -2.24121 | -48.52518 | 2025-12-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 890fe60b-d184-3685-bd32-727517d3a5fe | -3.763 | -46.94498 | 2025-12-03 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 276c50ac-23ee-32dd-85f2-32685c99483f | -4.51039 | -44.65586 | 2025-12-03 04:38:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88ef327b-d963-3d9f-9c0e-0ac3ad930cf7 | -0.17623 | -49.92619 | 2025-12-03 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9400bfd2-fea6-35b5-84f4-4fed5ad90a33 | -3.57929 | -50.2924 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4b5cf67-c244-3518-912d-55ca7edc8341 | -2.45085 | -49.00836 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bea9dee0-508b-353d-9c6b-bb41203a01cd | -3.81695 | -49.94743 | 2025-12-03 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e46ce08f-63ac-3128-bc78-9007673ba8a3 | -1.60522 | -48.69585 | 2025-12-03 04:38:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de54487d-6457-397b-88b6-0846351a4f98 | -2.60643 | -49.25261 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff5424c1-fb47-3708-8d35-4157680c5411 | -3.05291 | -48.42385 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cf2e9fb3-79e8-3810-949a-ce837ee910a2 | -2.63748 | -48.03367 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f2c3466-dd39-3b01-ae4f-c829f2d44e7c | -3.24614 | -50.1594 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0dfd195-9baa-3aac-87b9-ebbfc7b4c969 | -2.82858 | -48.44472 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 91590492-dc7f-30a0-bb0b-098ea8c7872c | -3.6731 | -48.93679 | 2025-12-03 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de12f8cf-c449-3f8d-9d66-305b322bb5d5 | -2.90648 | -48.72834 | 2025-12-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| def4d6aa-9e3a-3144-9f90-70added5c615 | -2.17416 | -48.36656 | 2025-12-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e76d5e30-01d7-3cb5-854d-cd8c2a65b2e8 | -2.15077 | -53.53737 | 2025-12-03 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68430f93-a05b-35d3-8971-214f39919464 | -3.40136 | -50.37937 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7a2b680-cbdf-342c-9bf7-6489b535b620 | -3.38906 | -47.2723 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 911d6349-1d06-318b-a7d9-f3904267f93b | -4.08058 | -47.04572 | 2025-12-03 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85f65632-e545-30ff-86b0-e6309249f218 | -3.3885 | -47.27589 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5708e3a4-433c-3b45-81cc-be0492105697 | -2.79569 | -42.57834 | 2025-12-03 04:38:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c395f6b-25c2-3604-b6fb-9cdee1aeaf06 | -3.12896 | -50.27761 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07ab562e-705f-3f15-b8f5-e8d5da240520 | -4.49508 | -46.0019 | 2025-12-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e064587-7551-3d68-9640-827dbd17cf1f | -5.38726 | -43.11482 | 2025-12-03 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3edf7bc6-8174-3f26-94cd-c07c42eec90c | -2.89714 | -53.29642 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43019b85-2c37-3a11-bea3-0621fa02c9f9 | -2.60697 | -49.24915 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1faf9c76-5da5-3e06-a296-5cb144008c48 | -3.97875 | -47.29935 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b35c770a-c896-35cb-b90e-dad277278c2f | -2.93734 | -53.27205 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20cd8131-5cd7-35e2-a4ca-7a24af3b8683 | -2.929 | -45.46517 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e701d59-8363-3a11-9722-ac2ceaebb827 | -2.89365 | -53.29372 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f9d47bd-9864-3f9f-8905-68c007105224 | 1.98195 | -55.72076 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66d4d640-88cd-38f1-a84e-87e52d3a3019 | -2.60311 | -49.2521 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1d87c21-5cdd-32b5-ae03-510f9fa835ff | -1.9831 | -46.47709 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d59d328-a40d-336a-94e1-7d900a1b8280 | -1.14763 | -47.25023 | 2025-12-03 04:38:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76640b0e-de30-3db0-9a5b-dd6e32a4b26b | -2.19357 | -51.97728 | 2025-12-03 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be2290d2-c324-39c4-b4af-eb61d4ea895b | -3.23501 | -45.57152 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1fbfa045-b764-30f3-b5d6-d696714db25d | -2.8141 | -49.40283 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99108675-41cd-3f84-849e-98c3bb714034 | -3.14792 | -50.56023 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 860cf399-6618-3049-b5fa-2201be1a961f | 1.9737 | -55.73378 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9aaaebd-42c0-3167-a8e0-4c3092239fd8 | -2.54673 | -49.06974 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce22868c-a9eb-32ad-83ba-3efd68f904d0 | -2.8407 | -50.46005 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65e5aa87-deb6-3ed0-9537-779978c0997d | -3.2647 | -48.56992 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5166b20f-6625-3b59-afcd-bbae36aa10f0 | -3.22239 | -45.57137 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7d486fe-7edc-3cf7-9453-8ff100f979fb | -2.22755 | -48.37129 | 2025-12-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc24702c-7487-3e0e-bb80-401a76735a87 | -1.68802 | -45.79473 | 2025-12-03 04:38:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cae22c6b-0ba5-351a-b5f0-ffc519a9537d | -3.0463 | -48.42282 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f7c27f92-672b-387f-80d1-4ee2cd3cee06 | -3.22687 | -46.87229 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd76af41-6506-3feb-b48c-76a9d7700271 | -2.59472 | -46.87421 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9a5394d-e84b-3072-88e5-a599baba944d | -1.60029 | -53.38025 | 2025-12-03 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38ed371c-0050-3ef2-a7d0-582926f05e65 | -2.51373 | -49.10707 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be0b9e8f-8f9b-3fad-88ee-94a87fba723f | -3.2247 | -45.58023 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8156279e-4fba-3326-a766-24a5cf893ef9 | -3.83413 | -49.25512 | 2025-12-03 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6238b476-0b45-3e17-a137-94082a28cd32 | -4.12231 | -50.08219 | 2025-12-03 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a114e363-ec57-3bb9-8b8f-2641f6631095 | -4.90403 | -44.05547 | 2025-12-03 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35388528-075b-3f3a-9ccd-3fbb79d380ea | -1.483 | -45.78446 | 2025-12-03 04:38:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bbf9400-a262-39b3-8a9e-a2d03673057d | -3.24709 | -45.5649 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dc7cbf35-98d3-3a20-9537-040445deeb8b | -3.23987 | -45.56376 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 6c8ceb4f-5f8e-3fbf-9623-aa26a67cc4d1 | -4.11896 | -50.08168 | 2025-12-03 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c004d2c-ecf5-324c-8b12-626adf6bff71 | -3.22062 | -46.86755 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a64a77ce-480a-3ea6-bdc3-994c8bbe466e | 0.7637 | -50.8035 | 2025-12-03 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0194831e-6d2a-3c9c-a23b-3c4ab44e0fa3 | -2.70289 | -49.31016 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 72c6fa2f-c53d-37f1-9709-b3b5c6e03f27 | -2.88382 | -50.47433 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d67f2958-3356-3c59-a20b-89094f71e802 | -2.74054 | -49.3302 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99d44a9f-307b-3018-878f-cb30520b4168 | -3.1301 | -50.27039 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9881c8ea-aafe-32d0-9fb5-cbb8b938237c | -3.23154 | -45.56004 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5326912b-8252-3a77-9071-a7beddbee094 | -2.99657 | -41.78455 | 2025-12-03 04:38:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f028f8de-2c5c-32b1-a57d-820b59cb04ae | -4.38565 | -43.13433 | 2025-12-03 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a76ffe1d-dc8e-3079-9951-cd617321334f | -3.9655 | -46.58369 | 2025-12-03 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbc8be55-9dd1-3594-bf78-234076351dc4 | -3.23564 | -45.56736 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d89cf935-f6d6-30b3-b32d-78841850004c | -3.24237 | -45.5617 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d82b146b-2eff-34ee-a07d-1603109a308e | -3.96839 | -46.58805 | 2025-12-03 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2be0f615-2cc7-3665-8905-f6f77749d384 | -4.39843 | -43.13628 | 2025-12-03 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a65a3666-c5d9-35df-b264-e267c0bf828d | -2.24321 | -45.62445 | 2025-12-03 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bfc48ed-ab5d-37cd-8607-74821951c8a0 | -1.51075 | -45.60358 | 2025-12-03 04:38:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f7428e1-7062-38df-ad5d-158636114b48 | -2.79262 | -47.43271 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8560f34-de21-3e5f-b137-7c5114064aa3 | -3.23751 | -45.55488 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 863ec539-fdd2-358a-8b16-09397e0d5d0d | -3.59313 | -47.27052 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d46f410e-91af-3153-ae1c-17901a6e1ab3 | -4.3996 | -43.12832 | 2025-12-03 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 802b5c13-cb6b-305e-bd84-75512e148c9a | -2.92363 | -48.22687 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3569c29-c512-3862-a0b8-2a1b85e970c5 | -2.64049 | -48.0382 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f6f5488-3623-3fd8-bca0-93d75b25d446 | -3.24897 | -45.55239 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8810ffd-36dd-344f-971f-c8080b798c19 | 0.48912 | -51.1594 | 2025-12-03 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b3fccbc-8bd2-3112-874c-3840cbd42a1b | -2.17271 | -48.41905 | 2025-12-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49857403-eeee-3a72-a4fb-395f1434f0b6 | -3.2167 | -45.53655 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7656e848-6dc6-3064-b18c-abe91e3ea2a9 | -3.06691 | -49.39589 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9305bad9-2635-3f3c-9168-479821ad49fe | -3.15133 | -50.56076 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3bae0ed-5b34-3b19-b413-4c27276c8f12 | -3.25682 | -45.54936 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78e7dd5a-5842-3d36-a44b-496b5712109c | -3.243 | -45.54294 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e08a9433-04d7-3d02-9501-6480d76f7c96 | -3.4649 | -48.85447 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README11.md)
