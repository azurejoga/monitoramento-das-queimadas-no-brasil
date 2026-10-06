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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b923b49-e069-32d7-a059-1d581040c9d6 | -4.47128 | -54.97631 | 2026-10-06 00:18:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 08535d1b-b566-3b77-8b00-959a19f7eb95 | -2.78892 | -51.67064 | 2026-10-06 00:18:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 537b77ff-8294-3731-b143-bb66b105ddfa | -4.91489 | -55.87165 | 2026-10-06 00:18:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 32d17371-4558-3eea-8895-f740495b971b | -3.04906 | -54.22652 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 62d562d7-ec89-30a9-85e6-ad5d8e55a784 | -3.08052 | -54.24274 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 218.3 |
| 41e43ad2-e461-3311-a038-0c4304b23b7d | -4.29082 | -54.80635 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a4b2a5f7-9645-309d-9377-6e05bcf57b61 | -3.32427 | -59.48481 | 2026-10-06 00:18:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b164090e-f09d-3569-b0df-9fa8c50acb22 | -3.11634 | -53.70624 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 946d3039-ae1f-38b8-aa5a-b666e35a635c | -6.71642 | -45.98841 | 2026-10-06 00:18:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 1b8ac873-e4ef-3184-a79e-bb02b8ad222b | -8.77809 | -62.8774 | 2026-10-06 00:18:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 23d816af-dee3-3c93-9a56-1a09f89ce7a6 | -3.33435 | -59.47773 | 2026-10-06 00:18:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 485f3a35-f87a-3783-ac45-c435f75a4f9e | -5.6745 | -49.21905 | 2026-10-06 00:18:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 7db2724c-253f-379a-977c-e578f2639123 | -2.98698 | -51.04794 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 24f85999-fb4f-3c7e-93d9-2dd17290bbb3 | -3.05824 | -54.14693 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 18531b95-5632-3eb8-af5e-d667a1fa165c | -4.05686 | -56.33301 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| dec40091-6736-3db0-a029-3a886ff8a6a8 | -2.98994 | -51.05384 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a97718d1-7531-345a-988b-c19033de49b2 | -3.27703 | -54.0049 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4f82b007-6c5b-3fe1-8ef2-508fc9f0d08d | -2.88426 | -54.15652 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ca0b9356-c6fb-3c05-a1cd-b7483b012f5b | -3.69244 | -55.95732 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a2b3d319-f5fb-30ce-a402-76e4b62bda55 | -5.98973 | -53.62917 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5a9e01ce-98f6-3807-ba05-75b08402c0c4 | -2.99911 | -54.12551 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2fb67926-f346-3cbf-a865-e185f915886d | -2.93732 | -54.14912 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 9aa4aa67-9282-3787-8677-c1bbf6230f67 | -2.9434 | -54.19329 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ddd42c93-f2d6-3c61-8c71-5de96d2f40d2 | -2.86294 | -54.14771 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 604a6bfa-52f6-3c0a-8cc3-a21eb6fda4bc | -2.99881 | -54.18856 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0cfb308-0ca3-397c-88d3-2a44ed109295 | -3.06314 | -54.18225 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e009b17e-00e3-30af-9715-de491be1cdcb | -3.62905 | -55.29056 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9536eda7-b478-3a5e-83fc-39211b980543 | -5.45462 | -45.52407 | 2026-10-06 00:18:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 8729fa00-2d88-3bff-b21a-d6cde04dddd4 | -2.96985 | -54.17459 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9dab9275-f28b-3b87-af66-39f43baf64cf | -3.60896 | -55.47571 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cbb59dff-c368-307d-88a6-fc29edbebc7c | -3.50634 | -51.67678 | 2026-10-06 00:18:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| aa99948b-d4f1-3090-8360-6ad6d2a7c2d4 | -3.47346 | -55.43362 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ce487c13-b7eb-3e5a-8ea0-86a66c8ef600 | -3.09461 | -53.74591 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| d9b227e8-7192-3080-8c00-de3fe0c0e9d2 | -3.10102 | -53.72672 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5184f3a8-a1ca-3b61-9fc8-502e93117871 | -4.45274 | -47.92239 | 2026-10-06 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 0bf2c47b-79a0-3ce2-808e-071466ec7eb4 | -3.32305 | -50.04573 | 2026-10-06 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e54f2664-4d87-3cac-8454-51d9551a00d8 | -3.08203 | -54.18861 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 20d6816b-e6fe-3b0d-9b7e-9b19f0402de0 | -4.41721 | -49.66513 | 2026-10-06 00:18:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 76a3af43-ad0e-3e96-af54-6e871074d8ce | -3.10352 | -53.74467 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| e311ba1e-58b7-35a6-823a-10778123d995 | -3.10477 | -53.75365 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 3b03a523-9cd3-318c-a304-02444a871b87 | -3.0997 | -54.18612 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| b43670ad-acda-308a-8946-394055aeb5a1 | -3.07291 | -54.25277 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| c85cc098-2223-3393-abb5-43a37716db14 | -4.46122 | -54.96868 | 2026-10-06 00:18:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e0ed02f0-409e-3f4f-adc4-75566928ca20 | -8.70301 | -45.21738 | 2026-10-06 00:18:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 98db1619-de7c-30d2-9a32-632a63190ca3 | -5.6763 | -53.49284 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 16d3c9c9-0802-3f8d-a5af-26dda4938d6a | -4.14667 | -54.02004 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| acc61ec8-34cc-3488-8e0f-65a2fa6dcbd1 | -2.77843 | -57.68443 | 2026-10-06 00:18:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| eb5963ce-c3a6-38d2-805c-112cb07540b8 | -4.46242 | -54.97754 | 2026-10-06 00:18:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 24ee1efe-f9cb-3c41-92f6-b61f45c46dfc | -3.05789 | -54.22528 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| ee5c4dbb-466f-3544-86cb-14992dbc033b | -3.84143 | -55.96859 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a11ed01c-f799-3445-b99a-973488c72f75 | -2.84313 | -54.06924 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f2071f7c-99fb-3829-aadc-3d2639c8a31d | -5.68639 | -53.50052 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9cb67675-170f-3e41-8039-e032ede25900 | -3.01649 | -54.18612 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d920388c-1cf1-3d6f-b90d-a44ab60e1e91 | -3.21527 | -53.95015 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bf7d2f70-1a6c-3b1c-91b0-da2876ce3faf | -2.77597 | -54.10575 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| aa1d0bef-cad1-3169-ba2c-bddf62514297 | -4.57734 | -54.94674 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5ad6038-00a9-306a-bf87-0411860556dd | -3.05668 | -54.21646 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 4864922c-f58d-3c87-ab54-b3540996fef8 | -3.5913 | -53.47949 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e049b565-0127-3a71-ae03-0bb75b4e5a32 | -3.23324 | -53.88424 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| caff80a3-097f-33b9-b6d9-9faec825221d | -3.49423 | -54.6349 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| baa8e1bd-ad46-312e-b067-f25d2fe74e26 | -3.52066 | -54.63121 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 66b5caa9-7d3e-3bdd-a519-3d648c9d0bb0 | -3.08842 | -54.1697 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| cc92af79-c838-351a-bda5-280634af4677 | -2.91231 | -54.09851 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 72a7d9b2-33d1-3d31-92e5-87b274c9a999 | -2.92604 | -54.13268 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 8407cd90-f1de-39c3-9716-3c5a027467e3 | -3.54085 | -55.51893 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48747758-dbed-359e-8270-2d5e8ea9c049 | -4.05882 | -59.83323 | 2026-10-06 00:18:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c3187d00-03c1-3281-a044-18b606b0a9a0 | -2.8931 | -54.15532 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| c359cc57-e421-384e-9f17-721fa0c23f5f | -3.27321 | -50.41024 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| b06cd280-753f-3344-9711-81598003ff33 | -4.35436 | -47.7839 | 2026-10-06 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| e9e35841-6b47-3ee4-b30f-f9d490f9560c | -6.17391 | -55.37796 | 2026-10-06 00:18:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7164092-ecd8-3d25-bf57-cf8bb742c9f1 | -2.96128 | -54.11276 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f40ee5d1-e2b5-3083-a470-527eb681af20 | -3.04145 | -54.23656 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 247ae525-41af-3d71-ad1d-e1cd5e99a8f1 | -4.32828 | -50.40421 | 2026-10-06 00:18:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 80c1877f-fc21-38c9-991e-696b71afecb1 | -2.95637 | -54.07738 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 34977b15-7232-3534-9076-aefc2092094c | -3.33052 | -53.38934 | 2026-10-06 00:18:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1dc1714d-41da-3893-bf28-559f35d061fa | -3.21402 | -53.94121 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bf4b9363-dcb2-3f14-9dc7-3f6489a66d5a | -2.88303 | -54.1477 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| b1a6aa85-0478-31d0-a404-87828aabc349 | -3.08081 | -54.17978 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 9ea95ef3-d258-35d2-99b2-575fb8fdb482 | -3.51306 | -54.64121 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d48196a2-c1f8-3e8b-8039-8066de3afc0e | -3.71155 | -58.94138 | 2026-10-06 00:18:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 69452a9c-5ddd-3536-856e-11187c31345b | -2.89433 | -54.16415 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 09555bfe-0988-39a4-afd3-7ca1b7641a9b | -2.79858 | -54.1387 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 9df8edaa-707e-349b-80b7-4e5d47a3839e | -2.99027 | -54.12675 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 7c6a4ab7-3b21-362d-ae7a-b752660e27f1 | -2.8013 | -54.09318 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 98b201cc-2ee7-3455-9cca-4d700f080c94 | -3.54208 | -55.52794 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5633ef5f-2c8f-339b-92e9-e7a765f09cb3 | -5.8501 | -45.01806 | 2026-10-06 00:18:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 74df9270-0982-3bf6-8431-6c9c60aecb4d | -3.17504 | -58.64151 | 2026-10-06 00:18:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6d2fa03e-2c52-3dac-968e-2a483a6125ac | -3.22313 | -53.87657 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 3e5d71f3-cb63-3282-b746-2acd0f6a5804 | -3.49302 | -54.62613 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| bfa67244-ac68-3aaf-bc2c-120a7d8f982f | -3.04266 | -54.24537 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| aa043cae-5e73-3bd2-b410-479a9918430d | -3.10943 | -59.16482 | 2026-10-06 00:18:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0dda5e57-45c1-3fe2-9a8e-6e09e8acbb6a | -3.43961 | -59.8266 | 2026-10-06 00:18:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| e8375a22-285c-362a-92d5-a288276bce2c | -3.07075 | -54.17218 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| dff1581b-a97b-3d35-bc8a-b411e35633a1 | -3.67308 | -55.95049 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| cedc206d-2420-3c97-83df-8df9959357d8 | -3.47267 | -54.62633 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e4865405-baa9-3dbe-9288-7605f114e900 | -3.49799 | -49.90561 | 2026-10-06 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| efcfae36-785f-30de-b19e-bef5a3bccc2b | -3.07169 | -54.24397 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 2042afee-5ac1-3c65-947a-1223576ab94d | -3.05547 | -54.20764 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 2c153930-b7ca-3282-841c-1e5814b06f2c | -3.74544 | -59.29223 | 2026-10-06 00:18:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7249204f-dec9-373c-bc85-4fa9bf278e55 | -7.24448 | -45.26479 | 2026-10-06 00:18:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |


[Clique aqui para ver as próximas entradas](README6.md)
