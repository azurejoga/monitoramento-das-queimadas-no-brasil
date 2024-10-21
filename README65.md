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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22848514-dae6-3b5e-b3ab-53d67a68e62b | -3.4281 | -44.7412 | 2024-10-21 14:25:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 44c24dad-f445-3a6d-8c6f-232346a32c78 | -3.4282 | -44.7184 | 2024-10-21 14:25:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 408e610f-b1e1-381d-ba22-dc88b6f18bd0 | -3.5956 | -44.7337 | 2024-10-21 14:25:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 8bba4100-84fa-3ff0-a512-6c8df765a665 | -3.7465 | -44.4077 | 2024-10-21 14:25:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| abe97c43-ff67-3396-b263-5e73fb4f62c7 | -3.857 | -44.6305 | 2024-10-21 14:25:28 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 67a93a69-84a7-376b-a738-556872510b81 | -3.8974 | -44.1026 | 2024-10-21 14:25:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 2ee636f7-f203-345d-ab77-d6f707d8de83 | -4.1017 | -44.2297 | 2024-10-21 14:25:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3631bdd9-d94f-3626-bc97-eb04993e514d | -4.2871 | -44.4029 | 2024-10-21 14:25:30 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2b87e057-b9a9-3f13-93eb-2adddca1b525 | -4.5471 | -44.5709 | 2024-10-21 14:25:32 | GOES-16 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 9c1b624f-ad81-303c-9bcd-0341816a6821 | -5.1583 | -42.8658 | 2024-10-21 14:25:35 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3a2ce19c-2ff1-32cc-a675-33e0bc0e0010 | -12.5168 | -63.0329 | 2024-10-21 14:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6f91e964-054b-34c3-a312-5e92f32b72c4 | -13.0323 | -62.4831 | 2024-10-21 14:26:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 5e17589d-ba5e-3624-b693-63d04e1ebf63 | -16.8655 | -57.2901 | 2024-10-21 14:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.0 |
| b6bc4fcc-f71c-30c5-a087-5800970d4481 | -16.9992 | -57.4995 | 2024-10-21 14:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 0cc0d56e-7c6a-3e8e-a51d-5100afe71f1b | -16.9988 | -57.52 | 2024-10-21 14:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| e9f27b98-3a8f-3e7c-997b-8cab3634b445 | -17.0406 | -57.3515 | 2024-10-21 14:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 7f06e0ca-d122-3596-a685-9c570188c3ff | -17.2373 | -57.3079 | 2024-10-21 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| 34671bb9-13b6-3a4a-aba0-00810f4a1145 | -17.237 | -57.3284 | 2024-10-21 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| c08e3ebe-3295-3c74-9842-f3d1ae1c833d | -17.2376 | -57.2873 | 2024-10-21 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 1aeef24b-d757-34b0-9a03-240c7fa89ec4 | -17.2573 | -57.285 | 2024-10-21 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| b3ffdad4-0f2c-3fe6-9a22-1c72896360a8 | -17.257 | -57.3055 | 2024-10-21 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 784031cf-ea60-3fce-88ea-ee58db6d09df | -18.0025 | -57.4413 | 2024-10-21 14:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 41be9440-0c38-370d-b61e-5316d3dc9fa9 | -17.9428 | -57.4692 | 2024-10-21 14:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.0 |
| fd40573a-0a47-3bf8-a123-1698da0ecc1d | -17.9827 | -57.4437 | 2024-10-21 14:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 0ec85220-911a-37a8-8891-f57d8e0706ff | -17.923 | -57.4716 | 2024-10-21 14:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 67c80f99-fc66-3cb7-89ef-419ddd2e3f38 | -19.5473 | -56.6563 | 2024-10-21 14:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 172.5 |
| 3fb4a971-7753-370a-819c-fb248306190a | -19.548 | -56.6143 | 2024-10-21 14:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 139.4 |
| 817049f4-1137-31ab-9adf-705f7422421e | -3.4281 | -44.7412 | 2024-10-21 14:35:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e4dd24e6-2879-3bea-870b-de1fa5b2586c | -3.4282 | -44.7184 | 2024-10-21 14:35:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 1c4159d5-1c0d-365d-874b-85b48d3e64f8 | -3.8974 | -44.1026 | 2024-10-21 14:35:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6523b3c6-1266-3e34-b009-ddb6956d361f | -4.2871 | -44.4029 | 2024-10-21 14:35:30 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 0e23d499-d4eb-3e38-9891-61059be23c4b | -4.1641 | -43.2559 | 2024-10-21 14:35:30 | GOES-16 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5ae29768-f0cc-3c9f-8dec-80cc2ac2a13d | -5.1583 | -42.8658 | 2024-10-21 14:35:35 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 83a7f0fa-0eb3-386a-864b-aff1d8ec3661 | -12.7502 | -62.2497 | 2024-10-21 14:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4cd539ab-a946-3ebe-8f89-707aca7c0264 | -13.0325 | -62.4638 | 2024-10-21 14:36:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e128fa2e-fc6c-3c30-a432-3c4676d22a38 | -16.8655 | -57.2901 | 2024-10-21 14:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 8510c3ab-f2aa-39ba-97d5-b5e19d67aa0b | -16.8848 | -57.3083 | 2024-10-21 14:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| f9c04812-2ecd-3e2f-94a1-902339cc6f3b | -17.0406 | -57.3515 | 2024-10-21 14:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| aeabbb7b-79d7-3397-8611-81deea7368fa | -17.257 | -57.3055 | 2024-10-21 14:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.0 |
| c6799f61-a952-3246-abf1-5f58bd2f66d3 | -17.2573 | -57.285 | 2024-10-21 14:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| f0ff4451-eb6f-3e24-978a-86b5cecee566 | -17.2376 | -57.2873 | 2024-10-21 14:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 15eb5db5-bc3f-337a-8456-f370cb89c300 | -17.237 | -57.3284 | 2024-10-21 14:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 83b6926b-e523-3efc-a136-3f7cf68b8789 | -17.2373 | -57.3079 | 2024-10-21 14:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.7 |
| 9db38897-4c5a-395d-ba98-ab70f62534b6 | -17.7848 | -57.4885 | 2024-10-21 14:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| ca0a6a26-a434-3ca2-b6d7-d4336103d41b | -17.764 | -57.5526 | 2024-10-21 14:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 43b8607a-993d-3569-ae0c-f909cb2477e9 | -17.8045 | -57.4861 | 2024-10-21 14:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.9 |
| b0743039-a930-3168-88a2-44847df28f77 | -17.7637 | -57.5732 | 2024-10-21 14:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 6acaa671-4dba-3ec8-b297-584e8df9e86b | -17.9234 | -57.451 | 2024-10-21 14:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| ddcbad81-1939-3be3-a4f2-2c2c45d00d2d | -17.923 | -57.4716 | 2024-10-21 14:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| ef0972e9-b263-3ec3-b6f4-2b166d10671c | -17.9428 | -57.4692 | 2024-10-21 14:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 6be6d94c-73d2-3845-be40-219f6c7597c3 | -17.8243 | -57.4837 | 2024-10-21 14:36:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 71012447-61a7-3ff8-85c2-dd4e939c8cd3 | -17.9432 | -57.4486 | 2024-10-21 14:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| df06afbf-1c74-31b2-bc48-097302219d59 | -19.5819 | -56.9443 | 2024-10-21 14:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 5c70e6b6-b39e-3ea4-88c4-82701d265fd5 | -3.2251 | -44.3853 | 2024-10-21 14:45:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4c101d50-366f-3ad4-921a-1a6f8f34f341 | -3.2439 | -44.3617 | 2024-10-21 14:45:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 7197fb36-2d60-3188-bdbc-d16fd416a3d1 | -3.4281 | -44.7412 | 2024-10-21 14:45:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| bed73627-2d01-3823-86e3-de7ddf75c093 | -3.4109 | -44.4687 | 2024-10-21 14:45:26 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 967a4654-f007-39ef-b50a-d19e557067bc | -3.7279 | -44.4086 | 2024-10-21 14:45:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 89be049a-2cdd-38fa-acc1-57a69474c8fc | -3.7448 | -44.7041 | 2024-10-21 14:45:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 51573495-8d2a-3ed2-abde-5c4325f5c3e5 | -3.765 | -44.4297 | 2024-10-21 14:45:28 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 12e03e71-7e93-3cf5-8ee7-48576e8680b2 | -4.1016 | -44.2526 | 2024-10-21 14:45:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6a14d9ca-a8ad-30a9-a742-f6a89cebe214 | -4.1017 | -44.2297 | 2024-10-21 14:45:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6f6c4508-49d6-3c80-8fd8-356bbaac9ab2 | -4.2871 | -44.4029 | 2024-10-21 14:45:30 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e1ef0c92-8971-3d73-a408-1683271177ec | -5.6221 | -43.3934 | 2024-10-21 14:45:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 1f27d947-7e98-346a-b2d4-da130ab7c230 | -6.4031 | -42.2227 | 2024-10-21 14:45:42 | GOES-16 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 8e229e46-4b47-38a2-bd84-7841e6c94d4d | -12.7502 | -62.2497 | 2024-10-21 14:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| bef03bf0-edb2-35f5-a3b7-cbadbff3b8af | -12.7313 | -62.2509 | 2024-10-21 14:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| f2b6d136-9c4e-3750-9da3-0a5e52a45581 | -13.0325 | -62.4638 | 2024-10-21 14:46:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7c852e75-8abe-3ea0-bf7e-b7c5d7877592 | -16.8851 | -57.2878 | 2024-10-21 14:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| af3cd65b-c309-3d91-9402-315366f29bd2 | -16.8655 | -57.2901 | 2024-10-21 14:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| a3fd9d93-8eb6-3719-9ec2-aebaa377e48c | -16.8848 | -57.3083 | 2024-10-21 14:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| ae999032-fe7f-3982-9393-724669c7f64c | -16.9992 | -57.4995 | 2024-10-21 14:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 21ae2b87-5e7f-3484-8b2e-c99dc73f2aa2 | -16.9988 | -57.52 | 2024-10-21 14:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 28f6b83b-af56-3257-9aa3-6d68ccd95185 | -17.0188 | -57.4973 | 2024-10-21 14:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 63fd7d0d-8f60-351b-aaa4-9dbdad8db689 | -17.0406 | -57.3515 | 2024-10-21 14:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 55fd0a5a-19e1-393c-ac63-26ed2211fdff | -16.9995 | -57.4791 | 2024-10-21 14:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 7d2186e7-60a6-3faa-8c38-084fa0ef22c2 | -16.9998 | -57.4586 | 2024-10-21 14:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| af9e9607-f175-3363-8b1f-56d69205c1b3 | -17.2177 | -57.3102 | 2024-10-21 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 00bbbc69-f660-3ca3-a105-9ff1170cecac | -17.257 | -57.3055 | 2024-10-21 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| ef5326ae-e13e-3cf0-9b3a-22b74d7b7458 | -17.2573 | -57.285 | 2024-10-21 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 9a086a19-f889-3fc0-a158-60569f8b82b2 | -17.2376 | -57.2873 | 2024-10-21 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| 7a5be5eb-1446-32dd-bba1-89c0f4c1239a | -17.237 | -57.3284 | 2024-10-21 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 304ce7a8-2b6d-347b-972f-6db5d542cd13 | -17.2373 | -57.3079 | 2024-10-21 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.2 |
| 8f4231ff-53a5-3a5f-aeb9-9786f01f6756 | -17.764 | -57.5526 | 2024-10-21 14:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| f53b36ea-eb19-3245-a68d-5774d8f9d3b3 | -17.7848 | -57.4885 | 2024-10-21 14:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 44878c19-b443-3060-ad4c-80dfc00c7fa0 | -17.7456 | -57.4727 | 2024-10-21 14:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| c211934a-4f36-3d85-9aa2-60ea71f3e2d4 | -17.7834 | -57.5708 | 2024-10-21 14:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 8f3bf99a-58fb-3ad7-8e59-44e8e2b7c3c8 | -17.8045 | -57.4861 | 2024-10-21 14:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 56d33a41-6bea-3edc-9732-4b971467cf3b | -17.7637 | -57.5732 | 2024-10-21 14:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 4fafb141-9fc6-3d7a-af05-c6ac8f111a1c | -17.765 | -57.4909 | 2024-10-21 14:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 097e0d40-95eb-3dfe-bbd5-3f26985d1c16 | -17.9234 | -57.451 | 2024-10-21 14:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 535b3d2e-be8e-39aa-9eda-51fe7c42ee37 | -17.923 | -57.4716 | 2024-10-21 14:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| b95f7743-cedb-3325-b055-e0704f9bc43e | -17.9428 | -57.4692 | 2024-10-21 14:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| ca4dc4d3-0dbd-30f8-b0dc-a1bb2a5edd25 | -17.8243 | -57.4837 | 2024-10-21 14:46:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.9 |
| dedcaacd-102c-3101-a7f0-4425ecbbe99e | -17.9432 | -57.4486 | 2024-10-21 14:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 11a13853-c44b-3980-b9ce-a7eb46824ec6 | -19.5819 | -56.9443 | 2024-10-21 14:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| c4433113-18ee-37ad-b4a9-96754ba9cbf3 | -19.6407 | -57.0197 | 2024-10-21 14:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 99b22cf0-1ba1-3afd-b2af-8cafdc02eff2 | -19.641 | -56.9988 | 2024-10-21 14:46:56 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |


