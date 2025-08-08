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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6ad83aa-4b7e-3c7d-8de3-16149aa1cd10 | -9.9285 | -60.4663 | 2025-08-08 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ed7de196-8e40-31eb-8324-dbdc96819507 | -8.4861 | -45.9989 | 2025-08-08 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| bb026f96-e50e-305d-9e76-4fe9b14593bb | -7.3731 | -44.6546 | 2025-08-08 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b3e527e3-a2b9-326d-90a0-27c078a6ab9a | -3.2196 | -41.8431 | 2025-08-08 14:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 6445690e-bf5e-3b6b-ad7c-22b6fc8c905d | -6.5966 | -45.337 | 2025-08-08 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 861d1d18-e36a-3ba7-8043-dea3ca2ada26 | -12.0972 | -44.7403 | 2025-08-08 14:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 6b23741f-34c7-3727-a57d-71044598ea7b | -12.0976 | -44.717 | 2025-08-08 14:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 6ed0680d-1cb2-3501-a38b-fdeaab45136e | -12.5333 | -47.1414 | 2025-08-08 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 162.3 |
| f351bdbf-3136-37d5-8289-97407296955f | -7.4074 | -60.0108 | 2025-08-08 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 706f629f-e700-3c99-a77b-6292aac776ef | -11.7866 | -44.9494 | 2025-08-08 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 59f3f334-cdc7-3682-8dba-02213d5bbb42 | -11.7862 | -44.9726 | 2025-08-08 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 5903acc4-8c8f-3c70-b455-08465121f3e6 | -6.6149 | -45.3807 | 2025-08-08 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4f3e0b9e-864e-3fd9-b248-b35e5bde99ba | -12.0289 | -47.525 | 2025-08-08 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 7b089cb6-798c-3fdf-ad10-88275104c9cc | -8.49 | -45.6826 | 2025-08-08 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0040154e-b8c8-3b8a-a491-7db0889330f9 | -6.6735 | -43.3304 | 2025-08-08 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 75.9 |
| cb2b48a4-9bea-32c1-92dc-a10010aa428e | -7.9297 | -45.3084 | 2025-08-08 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| f90b776e-52e3-305f-8a73-eb55f712e9bc | -6.6154 | -45.3354 | 2025-08-08 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5e19ee30-1253-328f-8d50-f54d1eea4a27 | -6.6923 | -43.3287 | 2025-08-08 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 85.0 |
| f8a1b626-12a6-3ef2-a854-d3cd0d89ee9e | -7.2603 | -44.665 | 2025-08-08 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| dc2ca518-1bdc-3ed8-9447-047252bd17a9 | -11.7866 | -44.9494 | 2025-08-08 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e4deeacb-fba6-36eb-9169-a6a535dd503d | -12.5333 | -47.1414 | 2025-08-08 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| b7aae1ad-8b8a-35c8-96e0-f54b0800d0f6 | -9.9285 | -60.4663 | 2025-08-08 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| a49533eb-dbb7-38e2-8587-7cd737862a4d | -12.0976 | -44.717 | 2025-08-08 14:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| be45748b-e1d5-3df6-99f3-358d5d928927 | -12.0289 | -47.525 | 2025-08-08 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 899b4a41-c4ee-397c-8656-21a62e8106cc | -7.2229 | -44.6455 | 2025-08-08 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 911a66ca-45b4-3534-96f3-25b7a0dcd7e8 | -11.7862 | -44.9726 | 2025-08-08 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 30cc779d-64d3-374b-a974-cb16f6120309 | -8.4897 | -45.7053 | 2025-08-08 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 626b82e4-386d-323d-b2d2-19783383e2ab | -7.4076 | -59.9916 | 2025-08-08 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| fbf67e34-1835-33a8-aacd-4218f3ac8188 | -6.6151 | -45.3581 | 2025-08-08 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 4cb441ca-50a1-3197-ae7f-19ce5fb6e921 | -6.6547 | -43.3321 | 2025-08-08 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 101.6 |
| c43c3aa4-bd99-36c7-bd82-e455bc693b8f | -7.2417 | -44.6438 | 2025-08-08 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 11988980-20d6-30de-81bc-ff46289ecdd7 | -6.6735 | -43.3304 | 2025-08-08 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 137.4 |
| 49b6de62-a569-3c91-bcab-c7f2cea5bc5a | -5.849 | -45.2359 | 2025-08-08 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 154bced7-70ad-332e-8093-59838d9570ca | -7.2227 | -44.6685 | 2025-08-08 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ea00548a-1c1b-384a-b043-36dcc1b205e5 | -6.5966 | -45.337 | 2025-08-08 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 4bd56f69-30c3-351b-af87-87f418230f37 | -12.6682 | -48.1926 | 2025-08-08 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 1674f8c4-31a9-3008-a0ed-afb79cc84456 | -6.6154 | -45.3354 | 2025-08-08 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 9032eb96-399f-3345-a8d1-1ee3b16b0339 | -12.0972 | -44.7403 | 2025-08-08 14:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 7643268d-d5da-347a-b502-58e370aae1fe | -7.7062 | -45.1254 | 2025-08-08 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1037cea9-4cf8-3501-93f2-fdef9a7c571b | -7.2415 | -44.6667 | 2025-08-08 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |


