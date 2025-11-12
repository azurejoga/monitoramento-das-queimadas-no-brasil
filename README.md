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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3543f4d4-3090-33c2-834a-6b8bcf59e54f | -2.8802 | -51.4835 | 2025-11-12 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 547d2a25-d0b6-39a5-aeb6-b053ed7738e5 | -4.116 | -48.0352 | 2025-11-12 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| e2d2999d-08f2-39f1-86dc-e78cd9273a3e | -2.6484 | -49.204 | 2025-11-12 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 75bdd734-a074-3f34-9521-617529e87300 | -2.8618 | -51.484 | 2025-11-12 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| f3b2377c-45ca-3a1f-9f7b-bdeb9dfed8ec | -20.8886 | -50.0937 | 2025-11-12 00:00:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 132.9 |
| 970f2173-758b-3574-91b6-e4ee94e8bc51 | -2.6299 | -49.2045 | 2025-11-12 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 422f1465-7499-3de0-9857-3dc5b047c7c3 | -2.308 | -45.9278 | 2025-11-12 00:00:00 | GOES-19 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9d664fec-f9aa-37d6-b45d-bebe12739f5e | -4.9456 | -43.7194 | 2025-11-12 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 627ca66e-be0e-3a0f-b2a6-952facd51185 | -20.9091 | -50.0893 | 2025-11-12 00:00:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| ec84e5d2-c3e0-3a14-8af6-54f7550441ac | -4.0976 | -48.0144 | 2025-11-12 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 251.9 |
| 52968225-8655-3580-b1c3-983d10c3ec4d | -3.974 | -43.7763 | 2025-11-12 00:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4f8fbf67-428b-3168-96f7-64165eb473b0 | -10.9323 | -44.6093 | 2025-11-12 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| edec95ac-95a4-336b-a5a4-1465242192c7 | -4.9454 | -43.7425 | 2025-11-12 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 33faf703-50e0-391d-ae48-a8f65deaf37c | -20.888 | -50.1165 | 2025-11-12 00:00:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| 980fa49f-ba86-325e-9255-84938b4e4277 | -21.4201 | -48.6453 | 2025-11-12 00:00:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 12f8104b-c93e-3f50-a7c7-67c2ba96967a | -4.0974 | -48.0361 | 2025-11-12 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d5a44f70-555f-3d62-a8d4-5ca6de68567f | -4.9641 | -43.7413 | 2025-11-12 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 3ab76f11-958b-3303-82a5-b692bbbfb764 | -4.9643 | -43.7182 | 2025-11-12 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| ed49a320-c286-3805-8ca2-39e50e5d0dd7 | -10.4885 | -44.9465 | 2025-11-12 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 20b386bd-0888-3daf-991f-fa24f7c1d89e | -4.0977 | -47.9927 | 2025-11-12 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 0e11b85f-ada6-34e9-af84-b84521026926 | -15.5925 | -46.2734 | 2025-11-12 00:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 1dcfe038-cca7-3647-8628-915bce14ff20 | -4.1161 | -48.0136 | 2025-11-12 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 707b2abb-caf4-3067-bb66-52f6cd340718 | -6.4212 | -42.2924 | 2025-11-12 00:00:00 | GOES-19 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| e0f6ade0-86b3-37c4-8e14-906e7b30aed2 | -4.1162 | -47.9919 | 2025-11-12 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ffe97bf2-5e1d-386d-b3a4-ae75cc9e9564 | -10.4504 | -44.9516 | 2025-11-12 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 6822aad3-1a90-36af-95f9-ed87cf63c7b4 | -2.6299 | -49.2045 | 2025-11-12 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 69cdd0d3-fb8b-3323-8b15-e5685ed0c7f0 | -2.3891 | -49.4019 | 2025-11-12 00:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 84b2f059-114a-3ad8-8008-93e9924d27af | -21.4201 | -48.6453 | 2025-11-12 00:10:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 08d920da-1821-3631-9482-e14135503d8b | -20.8886 | -50.0937 | 2025-11-12 00:10:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.6 |
| f89c9d3e-6a82-3fc3-8e8e-7e81e307c810 | -10.9323 | -44.6093 | 2025-11-12 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f56dd613-de98-3455-b7ff-be949cb29a48 | -10.45 | -44.9746 | 2025-11-12 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 0483ebe7-a8d8-3020-aed0-67b1e9da9e45 | -2.8618 | -51.484 | 2025-11-12 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6af747c6-4386-3123-904d-67958028cd7b | -2.6484 | -49.204 | 2025-11-12 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 48e57f1f-7584-30dc-9e35-fc9cd2c1e914 | -4.9641 | -43.7413 | 2025-11-12 00:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 26dc48e4-a596-3172-a801-8c5c38f0ed42 | -2.8802 | -51.4835 | 2025-11-12 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 929845f8-f362-37a3-8de6-2226b77ac211 | -4.9456 | -43.7194 | 2025-11-12 00:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 16941eb3-1257-3b43-b849-5cb0acd76d0d | -2.5238 | -47.8115 | 2025-11-12 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| d6b205dc-84b8-35da-8942-839adb5f8cf0 | -10.5476 | -44.8235 | 2025-11-12 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 06007811-26df-3848-9de4-84c028b3aa4c | -4.9643 | -43.7182 | 2025-11-12 00:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| ef0f11d9-a948-3aed-8f65-53c4e1ece0ac | -3.974 | -43.7763 | 2025-11-12 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 2ab873b8-fbaa-3c73-b978-9d1f1d74b146 | -20.9091 | -50.0893 | 2025-11-12 00:10:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.9 |
| e4895e0f-2c7d-38a4-a761-4b90e6a1dae3 | -4.9643 | -43.7182 | 2025-11-12 00:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 38d03bd9-ab95-34f8-8f30-b195f4cd3ac7 | -10.508 | -44.921 | 2025-11-12 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| c97cafba-0a65-3059-aa0e-0772f97af80d | -21.4201 | -48.6453 | 2025-11-12 00:20:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5b65e5c7-8ddc-34f1-aa21-db14a6c42ac9 | -10.9323 | -44.6093 | 2025-11-12 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| da5c37cd-4b3b-3b1a-8ad8-7a14927acc2e | -4.9456 | -43.7194 | 2025-11-12 00:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 47bfa6b1-59a9-3a5e-9b2a-efffd994670d | -2.3891 | -49.4019 | 2025-11-12 00:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 220712e5-1345-31df-b04b-a840265dc21d | -4.9641 | -43.7413 | 2025-11-12 00:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f3ad9bf9-c131-3d81-9a20-5b7dc9e0d249 | -10.45 | -44.9746 | 2025-11-12 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 32d58e50-086b-3a00-b6ab-cb7d9021cc7e | -20.8886 | -50.0937 | 2025-11-12 00:20:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.0 |
| 97acf53c-7278-3d45-8cdb-279d22cf09b8 | -10.5076 | -44.944 | 2025-11-12 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7b1895e3-7936-3acc-8f96-fe5dbceb9c55 | -2.3891 | -49.4019 | 2025-11-12 00:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 2fe9bb3a-db62-3bcc-a5dc-8a6ccac1c2a3 | -20.8886 | -50.0937 | 2025-11-12 00:30:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.9 |
| 72052cb1-12d7-38e9-b1c3-f28df5402dc0 | -4.116 | -48.0352 | 2025-11-12 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 2236ccc4-5edc-3b50-92ca-19da30aa7302 | -4.9454 | -43.7425 | 2025-11-12 00:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4cf19ebd-e47b-32ff-a520-3d796b57bfcd | -10.5476 | -44.8235 | 2025-11-12 00:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| e2e01d12-245c-314d-84de-399cc5bd017d | -4.1162 | -47.9919 | 2025-11-12 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| a120efc9-7c66-382f-bff7-2521ee8c850b | -4.9641 | -43.7413 | 2025-11-12 00:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| d653b97a-0d27-3c2c-94f4-847d42280f22 | -3.3385 | -44.0599 | 2025-11-12 00:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ceaaf3c8-ac3d-3f9b-adb7-e0fdc9bc478b | -4.0977 | -47.9927 | 2025-11-12 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 9143241a-aa9b-305d-bb39-ef0befd4634e | -4.9643 | -43.7182 | 2025-11-12 00:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 1a9d8de5-8c07-35a7-93e5-17023588a89a | -4.1161 | -48.0136 | 2025-11-12 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 340.6 |
| 99725572-8fab-3289-800c-c9579091ec9f | -4.0976 | -48.0144 | 2025-11-12 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 345.2 |
| 43d7c4b0-23f2-396b-bf88-ba33889a9d25 | -4.9456 | -43.7194 | 2025-11-12 00:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 691f6e0e-4dbc-3b2f-8e15-607f364889e0 | -4.0974 | -48.0361 | 2025-11-12 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 157.9 |
| fccb5028-e529-39a5-b424-74be49adfed5 | -19.7974 | -57.949501 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5a4c9a22-64ad-3849-b57f-716453502823 | -3.7995 | -52.216599 | 2025-11-12 00:34:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c0e8b66-0062-3188-a7c4-5a2e753253a0 | -19.8095 | -57.960499 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1ac423d1-9a8b-3047-9530-1ee5947252c1 | -22.7868 | -51.6796 | 2025-11-12 00:34:00 | METOP-B | LUPIONÓPOLIS | PARANÁ | Brasil | 4113809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 00c87b7e-ae65-3b48-8d99-134123c1b1f8 | -2.8674 | -51.4814 | 2025-11-12 00:34:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3fc1e0-fb25-3ed7-b321-6356cfbaf1e9 | -4.0884 | -48.002998 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef075d90-a1da-366a-b7e4-cdc096e5466f | -2.5187 | -47.785 | 2025-11-12 00:34:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f92845f-97c2-377d-8a66-a7c151b8d112 | -21.4121 | -48.6535 | 2025-11-12 00:34:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 24f4e8a6-8c88-3f5e-ae33-87066c05d257 | -17.116501 | -44.640499 | 2025-11-12 00:34:00 | METOP-B | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f606b401-7b34-373c-9744-04c9b694dd96 | -21.168699 | -48.674702 | 2025-11-12 00:34:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c76a2eb-d1ca-3586-b3d5-791dfc73abfb | -19.746 | -58.000198 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 97f5d660-5018-387f-a7df-f433406421fe | -3.0816 | -49.439201 | 2025-11-12 00:34:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89e30edd-4118-3f2d-a7c0-a8b7d06ce6cb | -3.4411 | -52.6287 | 2025-11-12 00:34:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5e412cd-c7a4-30f7-a3e1-3cc350197055 | -16.8911 | -51.6436 | 2025-11-12 00:34:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e2e3c0c2-73b3-3aef-aa02-300a1e8d427d | -4.9439 | -43.693501 | 2025-11-12 00:34:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7519ede-14a8-3689-9a17-672a65230b2b | -19.743601 | -57.987202 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7170c883-a1bf-3394-8c7a-2c9967dec012 | -3.6349 | -50.574699 | 2025-11-12 00:34:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85d21929-a6ee-3c57-900e-425871400f07 | -3.9411 | -43.758598 | 2025-11-12 00:34:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e977306-baa0-39f1-bd15-df93175f7e64 | -2.7969 | -52.964298 | 2025-11-12 00:34:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06bcadee-fb8c-3f40-8f58-0e3297f5d5a8 | -2.8729 | -51.460899 | 2025-11-12 00:34:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09b9ece7-aaf0-343d-9781-ce69060968ec | -3.3162 | -44.0331 | 2025-11-12 00:34:00 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b0e1880c-ccb7-3153-bd44-34a9d7768b10 | -3.9433 | -50.308399 | 2025-11-12 00:34:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f413648-a94a-3e62-bfee-380fc16524d3 | -21.170601 | -48.682899 | 2025-11-12 00:34:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 56c609a2-43ab-3e11-8f62-30ed340f78bb | -4.9343 | -43.6959 | 2025-11-12 00:34:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec70cbea-7e7b-3f67-ac87-4523b8af70b6 | -6.8598 | -42.834202 | 2025-11-12 00:34:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 66e72f79-aa5b-33d8-b691-bed6095f67f4 | -23.6033 | -51.313099 | 2025-11-12 00:34:00 | METOP-B | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5701e76-a0b6-36bb-8cf4-6de50081983f | -19.843599 | -57.980598 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ade3c6b8-f891-3e3a-bf5a-8dceae2bf704 | -21.4083 | -48.637199 | 2025-11-12 00:34:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a7a3162a-9908-34b8-9195-bdca47c61850 | -20.8939 | -50.087399 | 2025-11-12 00:34:00 | METOP-B | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e6a8f3a4-b281-3067-ba1e-60382c6c4c4f | -4.0954 | -48.032398 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9677fcc-3445-33f1-9b7f-87d56379ef97 | -17.620501 | -46.690201 | 2025-11-12 00:34:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3d05ca0f-3899-3fc7-8a4b-08bd4d3cc6b3 | -2.4889 | -50.247898 | 2025-11-12 00:34:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0b63192-932f-351b-9ac0-fa9e5d8819e4 | -3.0844 | -49.451401 | 2025-11-12 00:34:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3703f04-ac0c-3ed3-9aa6-757ed945acf0 | -18.476999 | -53.3936 | 2025-11-12 00:34:00 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fe34e360-8f6e-3978-af77-15167975c76b | -20.2045 | -56.599701 | 2025-11-12 00:34:00 | METOP-B | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README2.md)
