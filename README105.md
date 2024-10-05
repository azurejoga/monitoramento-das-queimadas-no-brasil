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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e4d8f11-8012-387f-a4a8-b5d86a31e07e | -12.80972 | -50.56064 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e8f68a7-5bbd-3c84-b200-31640a91090d | -12.80806 | -50.54952 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 82bbc071-9e0a-38d7-8224-97095d4ed7b7 | -12.80751 | -50.55305 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 051b88c4-9340-35c8-b120-72e590a67830 | -12.80696 | -50.55658 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3c2d0846-e4c4-36f1-95ad-435df273f056 | -12.80641 | -50.56011 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1c83fae-0727-33db-8b56-8b3447bedfb5 | -12.8042 | -50.55251 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f30f7215-2109-38d5-bf8d-2263e8f9cca4 | -12.80365 | -50.55604 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 66c1f629-81ee-320a-a784-82fb53a949eb | -12.8031 | -50.55957 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 615ce0ec-a895-364d-abf4-6f62d6db6bf1 | -12.80089 | -50.55198 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eafda273-d095-3728-931a-6b264b1bea03 | -12.80034 | -50.55551 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9b42cb53-1fe0-3ea1-a18c-a759ca35855e | -12.79979 | -50.55903 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 768711f8-3a5d-3cb3-9f38-64b8064b06fa | -12.79647 | -50.5585 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 17c179f3-9868-3dd3-9041-3f78e0269f5d | -6.44992 | -49.92121 | 2024-10-05 04:38:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf664eec-6e2f-3462-9d8b-75a3086debc6 | -6.44937 | -49.92468 | 2024-10-05 04:38:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da6d42fb-158a-3880-ad4a-52fda12bb173 | -6.42446 | -50.14567 | 2024-10-05 04:38:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 885d12c7-32f2-345e-b719-a9cb95dce069 | -6.17736 | -50.90105 | 2024-10-05 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f6b6bbc3-b7ff-37cf-9a72-8fd6ad409073 | -5.99717 | -49.66796 | 2024-10-05 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 36a5927d-285b-369e-a3a4-5c827a64dbdd | -5.99662 | -49.67141 | 2024-10-05 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62efbfba-e068-328e-bfbb-07743b5373d4 | -5.6565 | -49.71755 | 2024-10-05 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d41ae62-cb22-3622-9781-1e564ccdc1bc | -5.65318 | -49.71703 | 2024-10-05 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78c5fb72-7616-369a-8f1d-aa4400d7a3de | -5.65264 | -49.72049 | 2024-10-05 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 855e9b0a-8683-3334-ba70-d3b14f80de5a | -5.64987 | -49.7165 | 2024-10-05 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50223d13-f3d2-3f70-8703-f3695619fc07 | -5.64325 | -49.71546 | 2024-10-05 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59fd26c5-a022-3760-835a-b80ce0c74976 | -5.63993 | -49.71494 | 2024-10-05 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72fb5214-61c6-3b98-84cf-45cefbc38e0b | -5.50867 | -51.04382 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a39a582-f16f-322c-a1b2-8c9a365c7e61 | -7.81354 | -50.23487 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27ccc727-246f-32f0-b9bf-c0fd174a38bb | -7.81352 | -51.19424 | 2024-10-05 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb661ab0-8fad-34b0-9532-d8ac1de03d7e | -7.81298 | -50.23835 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28245240-5891-3466-9a5e-0f69a5418a45 | -7.80635 | -50.23729 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b799b4f6-2da1-35e3-a3df-2d40185bbf33 | -7.78381 | -50.23011 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d874ec00-ffd0-33c0-9998-7636774638a0 | -7.78326 | -50.23359 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9c3bb8c-2e13-37e9-90ad-9b614dbf5457 | -7.77995 | -50.23306 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75eeefe4-a0e5-3b1e-a166-1b46927adce8 | -7.03837 | -50.73102 | 2024-10-05 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33f6adda-d540-3834-8a9c-d7a3fbed90c4 | -7.03503 | -50.73048 | 2024-10-05 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a1717657-640f-3bd0-be8c-4a5f783f801f | -9.37331 | -50.74711 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 353dac23-2574-3360-874e-45c63537f4f1 | -9.37276 | -50.75062 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fd50fb0-bb4b-31d2-a180-b045fab4ab3f | -9.37 | -50.74657 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 99507124-04e6-3239-89b4-9d3d04a070ef | -9.36944 | -50.75008 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f86ab595-5150-31da-bcf5-47c9fdd45c95 | -9.36463 | -51.1009 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1911de0-fb91-3b63-b8bb-7243b92d930e | -9.36406 | -51.10445 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f05f035-98e8-3abe-9ca1-96744454e4fa | -9.36243 | -51.09326 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd166657-2a10-3308-8bdd-73e87ff0af23 | -9.36186 | -51.09681 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6ae3873-63ba-30e6-8d19-7ba70e461281 | -9.36129 | -51.10035 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea3354a4-9f6b-3630-bb9f-aeddbf2f956c | -9.36072 | -51.1039 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d241aa9-de5e-3381-8df8-fbfe64887716 | -9.35909 | -51.09272 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41f49951-619a-3714-bf8d-8435b9f8f0fe | -9.35852 | -51.09626 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d280d7b4-d9ed-30e9-b71c-fcf0c4b679ff | -9.35795 | -51.09981 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8316a43c-00b8-3872-9d9d-7f7ab03826e4 | -9.35518 | -51.09572 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02192e1f-76d0-38fd-af15-0b60fb1ab3cf | -9.35461 | -51.09927 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5e87c53-50b4-35fc-811e-491645cb657b | -9.35404 | -51.10282 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6ec206a-5ca0-3fcc-8e1a-12c1e7bb9bf5 | -9.35071 | -51.10227 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8d86cee-f755-3bc0-8c29-9268caaaeef5 | -9.3485 | -51.09463 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dfe9888-470a-3599-a6e5-64d3531434e1 | -9.34793 | -51.09818 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f61f7bfa-b136-317a-9b0e-e0bc05387c38 | -9.34736 | -51.10173 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 6557059d-e292-3770-865c-fe4db243c3eb | -9.3468 | -51.10528 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83f177b8-80be-3c93-8449-302d5e26154f | -9.34459 | -51.09764 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 3a494cb1-1cf6-3f70-b1ee-c5440b0bc59a | -9.34403 | -51.10119 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 3790ecd4-5c33-30dd-b6ae-d1d2a1089bbb | -9.34346 | -51.10474 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a046392-19b9-353f-a478-1b75c07cc6a5 | -9.34289 | -51.1083 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe610e04-b9f2-312f-83e9-be1f0fc31b33 | -9.34232 | -51.11184 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3d87cd5-7340-3da4-a94c-e196b24b9329 | -9.34068 | -51.10065 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 109c529a-1a38-3b22-baa4-7efe38ac3abd | -9.34012 | -51.1042 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 564c5332-a640-33d9-9ea8-086905fd96db | -9.33506 | -51.11433 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bd8a6fb-b84e-3417-b848-331b24db27f1 | -9.33449 | -51.11789 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d64bf33-1279-371f-8658-27a52eff9ff6 | -9.33172 | -51.11378 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60eb5307-41c3-3bd0-8c6c-a96a266c6ae0 | -9.33115 | -51.11735 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7461ac20-036c-3d4e-bb17-c49974ab517b | -9.32781 | -51.11681 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 72bfdcc9-db7e-3fbf-8eff-9d8b7d5f4b79 | -9.32504 | -51.1127 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28efced8-07b7-3deb-a563-e81cdc67db70 | -9.32447 | -51.11627 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90ad9541-5767-31cd-a7da-1fbac07b92b1 | -9.04725 | -51.52938 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f66220a-a636-34bf-9683-85f6a5b70143 | -8.38228 | -51.64887 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d1b4394-bb04-316e-9104-a063caf0e42a | -8.37889 | -51.64823 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a760246-8706-367b-bfd3-e7efcbf116d0 | -8.37548 | -51.64764 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45754243-b9d2-3407-97a8-b8c9d3b385e1 | -8.37325 | -51.63984 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| beb336bb-fab6-394f-916d-3cf019aa0a51 | -8.37208 | -51.64706 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58f774f3-d7c5-3118-898b-407e4ca39a01 | -7.95944 | -51.22093 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 332f1cd2-2d9c-3aa4-a01b-d3c3f1da993d | -9.04387 | -51.52883 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6caf4e88-20da-332d-ba63-7c538739261a | -9.04327 | -51.53251 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 731e759d-9753-3409-b812-caf52362eff1 | -9.04048 | -51.52829 | 2024-10-05 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd22c640-f9af-3ea8-a971-0344d54ffc33 | -9.75181 | -50.65311 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51ddbd85-81ad-3227-9b29-1a7f4e0ed3db | -9.75125 | -50.65661 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 111b92ae-160d-31e1-b2a3-fe2879e1b885 | -9.74794 | -50.65608 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eafa275-df17-383f-80ac-23c0c0afc4fd | -9.74518 | -50.65204 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d74ab3e2-813a-30b6-8236-eabaa03cbc9c | -9.74186 | -50.6515 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c36d6460-58fd-3921-9c6e-e811098a35c6 | -9.73799 | -50.65447 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24d23c06-0965-3e56-a54c-839d4474bc65 | -9.73744 | -50.65797 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f34d5d7-208b-39a9-89dc-ec60a8643b24 | -9.73412 | -50.65743 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d789604-088e-39d1-98d6-0bcca7cb418f | -9.73357 | -50.66094 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5bbc68a-cf8a-3b9b-a52e-469a569244e4 | -9.73081 | -50.6569 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9a0e268e-ff43-37e2-9dbd-de4963222495 | -9.73078 | -50.67847 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d4a1758-1c95-378e-b84c-1382f9e65eb5 | -9.73025 | -50.6604 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 203b19f7-9f8e-38d0-ba21-94b1f4fba4ae | -9.72638 | -50.66338 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e3cb6c0-d25a-3e95-aaf7-7b67e7a135eb | -9.72582 | -50.66689 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69d400a0-3096-3c9f-9fbb-421330e260db | -9.72526 | -50.67039 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 960aa208-5b15-3576-9553-0669f99f42ab | -9.6014 | -51.44361 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5df64b72-844e-3cbb-aa3d-a920259dfabc | -9.59861 | -51.43949 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14e52c3c-042a-3532-b7c5-5af33f45f92b | -9.59804 | -51.44304 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ef8f40b-1ea8-3b26-9c80-311533a11657 | -9.59525 | -51.43894 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abb226d8-06d1-3606-ac8a-3b60d152c6a0 | -9.59468 | -51.44249 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee87ff2c-7b4e-31f6-9642-25267fbdd01f | -10.84829 | -51.06534 | 2024-10-05 04:38:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README106.md)
