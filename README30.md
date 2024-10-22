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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d935ed68-2fb8-3fa2-beb1-0fa63ce940e6 | -17.03842 | -57.4504 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 784323c8-411c-36ce-8cab-142d49240b11 | -17.03495 | -57.44986 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6ad3e0de-fd41-3fc9-81ff-fe7c82983420 | -17.03091 | -57.45329 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2da5512e-ce56-3aba-bd16-abcee631fffd | -17.02742 | -57.47709 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| aac1597c-db3c-3cc2-9845-49ee419dff42 | -17.02453 | -57.47258 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5aa6f421-6a63-3548-ae86-f088be67148d | -17.02395 | -57.47654 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 832d2461-51b5-39e3-8736-8ec6cf11ad53 | -17.02223 | -57.4641 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 61b0bbe8-a277-3976-9723-40ad0f162426 | -17.02165 | -57.46807 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| de5c3674-05e6-3827-84d4-d954599fc3a7 | -17.02107 | -57.47204 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 50e07f45-3a51-3625-9806-19594971bfe8 | -17.01876 | -57.46355 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ac08bbc7-5578-369f-99b4-2e5d69651aac | -17.01818 | -57.46753 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1b6bfc13-ddf2-366a-abc9-da8a383a062d | -17.0176 | -57.47149 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2da28014-0a8b-3859-a46a-64d875d0152e | -17.01759 | -57.4958 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| bdee8bca-6c2a-3955-9cfc-a529dd7cc9d6 | -17.01701 | -57.49976 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 23431e13-a5aa-377c-879f-892c86a4f86f | -17.01585 | -57.50767 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 2616dd12-f0be-3556-892a-b7064ad70d49 | -17.01527 | -57.51163 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 06de569e-bae3-3382-bf86-23a530ccb04f | -17.01411 | -57.51953 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| e5ea80d8-b955-3c1d-b4fc-de20330c5fe0 | -17.01353 | -57.52347 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| b684ff6c-2c9a-334e-b36b-4505ce636ca2 | -17.01239 | -57.50712 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 11733fa3-9dbd-334b-b694-09831b29ce3c | -17.01181 | -57.51108 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 202e7b48-55de-36f1-9b11-c66a3fe6a4ba | -17.01065 | -57.51898 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 5310d333-8445-3a13-b815-9506cfce28b0 | -17.01008 | -57.52292 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 1d3463d6-6959-36db-bd7b-8742e9481dd9 | -17.0095 | -57.52687 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a74d9c32-f2c4-3196-bfc8-1bd3d268a667 | -17.00893 | -57.50658 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 74b22195-fb57-3d3a-a783-4290a902b553 | -17.00778 | -57.4902 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b3875301-e318-31ad-9c09-5cf4f59e88a6 | -17.0072 | -57.51844 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 0499cd3f-68de-3c3f-a3fa-94df133ed2eb | -17.00662 | -57.52238 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 8673e809-002f-394c-a416-22768cfa6b2a | -17.00604 | -57.52633 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 547166f9-79f1-3b62-b7d7-619e6e727590 | -17.0049 | -57.48569 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 67f66b9d-beea-3618-a49f-2c0ff1cbf06c | -17.00489 | -57.50998 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f91e61ff-5f9e-3410-9cb4-bca5498ce615 | -17.00432 | -57.51393 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 120c4580-a627-3d27-a3d9-d995bc5fc538 | -17.00432 | -57.48965 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4745b269-5fd6-3001-a2a5-f96c025d4187 | -17.00374 | -57.51789 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 61795ca9-53ff-3df7-a5c6-a740e2083ca9 | -17.00374 | -57.49361 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e6d9c3dd-1c0a-3918-a04a-20d10a25e40c | -17.00316 | -57.52184 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 27a8d5f4-1540-37b9-b06d-41d5a2316540 | -16.9974 | -57.51284 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f7722227-401b-32a7-8586-53546dce57df | -16.99682 | -57.51679 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 91a32e02-0e81-338f-9341-8d3350a584b8 | -16.99394 | -57.51229 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 851e377a-4063-39db-a52a-16a3fe5193ef | -16.99336 | -57.51624 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 818786b4-8b64-30db-bde0-90610d0bd442 | -16.17503 | -59.09928 | 2024-10-22 05:14:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 044b458d-788f-3894-adbb-c30f3304894e | -15.83733 | -59.01819 | 2024-10-22 05:14:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04e74e3f-b479-3ae0-81f1-fcf1a6b63e06 | -15.48956 | -59.37436 | 2024-10-22 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e30346bb-3b1c-3228-a800-c43f60e27e29 | -15.489 | -59.37792 | 2024-10-22 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a446b89b-ab27-3045-b117-9af401f09fc5 | -15.48239 | -59.37682 | 2024-10-22 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2d34f3f-2eda-3e64-b2d1-fd08c23db48a | -15.1223 | -59.02483 | 2024-10-22 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09b11a78-a9c3-3c4b-a62e-3ec7f73af460 | -15.87186 | -58.4379 | 2024-10-22 05:14:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 52e83fd7-cc38-35c7-b2dc-27eb3007bd1d | -15.53588 | -58.01235 | 2024-10-22 05:14:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 14b0c1c2-7ed7-3dfa-ac06-ce94665ed9a8 | -15.23269 | -59.60155 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60d393ef-786f-330c-a87b-46ff18c25732 | -15.22939 | -59.60099 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1447451-00f4-37ed-a362-6b919d9a1543 | -15.16402 | -59.92675 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d580ab1-e0d9-30c3-b0f4-73c38e3374cd | -15.1639 | -59.94878 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ddf9a4e-d486-319e-80c8-d39407afc5e7 | -15.16298 | -59.71804 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f0308c6-8b41-383d-81c7-85295eed552b | -14.91918 | -59.88182 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89537eff-313a-3a57-a234-e8c30ef756fa | -14.30465 | -59.3156 | 2024-10-22 05:14:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f01b053d-ef49-3c40-9ac3-49b5fc8d4174 | -14.27737 | -60.12677 | 2024-10-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89e9add3-4510-3931-822c-636983182851 | -14.27678 | -60.13038 | 2024-10-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 683ab885-6b6b-3cd3-ba04-5901f4f5522f | -14.27129 | -60.12205 | 2024-10-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 046a5230-0b59-3766-aca4-d161338ace08 | -15.67103 | -59.7554 | 2024-10-22 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdec92e9-d872-34de-84e6-1aa7caddf700 | -15.66829 | -59.75128 | 2024-10-22 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17ecb024-2d44-31fa-8dbc-2f25101345fa | -15.66772 | -59.75484 | 2024-10-22 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1f03531-2671-3040-8a78-438b9fbc6004 | -15.63736 | -60.01024 | 2024-10-22 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bae80e57-dc06-3ce9-9c32-19334ea92721 | -15.23143 | -60.03734 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05d71754-f857-3aae-a571-2ab821c5122a | -16.09222 | -60.12465 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3a739fd-f9d5-31e3-b431-2c4e7474a06d | -16.08947 | -60.12049 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b3ebb6c-8b5e-38e6-b6a7-54c4987885fb | -16.0889 | -60.12408 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50f3af10-a381-3439-a367-988043dd0d6b | -16.08833 | -60.12767 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7986e622-3078-38b3-b32a-36120e659b84 | -16.08616 | -60.11993 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 623ca1af-09a9-3e5d-ba41-c9587ffd8ebb | -16.08559 | -60.12352 | 2024-10-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c59829c-8786-3b42-b704-c0ea9b698ec8 | -15.96343 | -59.75705 | 2024-10-22 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5bed0fc-adc7-3c1c-ba64-a9a1c11d0d4d | -12.25932 | -60.6642 | 2024-10-22 05:14:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9e1d5ca-31c0-3d39-83ab-1d0644d7fe62 | -12.2492 | -60.38578 | 2024-10-22 05:14:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae92e52b-8442-3806-86be-8797a3b4c0fa | -11.49664 | -60.57695 | 2024-10-22 05:14:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76f515e7-c404-3c9e-87d9-69c8a1ca3179 | -11.49602 | -60.58069 | 2024-10-22 05:14:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ef09493-efb5-3fa8-8e33-57339231c594 | -11.4932 | -60.57641 | 2024-10-22 05:14:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 543d50e7-b508-32b5-91a2-6a4f57cdfccb | -12.81666 | -60.78081 | 2024-10-22 05:14:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f1140cb-ed27-31ad-b98b-0523c75c61bc | -2.7588 | -49.3285 | 2024-10-22 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 5fbd205f-b42f-3b1d-b458-1fcef0c84c0c | -2.7589 | -49.3072 | 2024-10-22 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 175.3 |
| 6c67ef3d-1d1e-3648-a5dd-165a446830ac | -2.7589 | -49.286 | 2024-10-22 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 9fec492c-73c5-3590-90be-a579f295f3ee | -2.7773 | -49.3279 | 2024-10-22 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 0a36be04-699d-3ea0-b249-00dae5f75785 | -2.7773 | -49.3067 | 2024-10-22 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| f9681635-919c-312c-974b-2bac40ea981d | -5.5718 | -44.87 | 2024-10-22 05:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 4ea732e0-3b64-36e7-9bd1-a254ee1d8510 | -5.5905 | -44.8687 | 2024-10-22 05:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 7ab9d00b-131f-3763-8d17-5ef525f66997 | -6.2524 | -44.132 | 2024-10-22 05:15:42 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| a03e7d03-e868-3053-8b07-a7b3ea568a4b | -21.37708 | -55.71228 | 2024-10-22 05:16:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0ba8c96-1fda-39ae-a465-9c8b05e74066 | -22.18427 | -56.9124 | 2024-10-22 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35ad8414-0848-3057-b239-3979db637ebb | -2.7588 | -49.3285 | 2024-10-22 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 907feb51-6a89-3d7d-b3bb-8d08ec3d72b1 | -2.7589 | -49.3072 | 2024-10-22 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 36963922-1162-33f1-b54f-86b66dbd08fc | -2.7773 | -49.3279 | 2024-10-22 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| be865d08-b035-3222-a0a9-0ed0ab0124d6 | -2.7773 | -49.3067 | 2024-10-22 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 192e91ee-f718-33de-9284-4c5234493ad4 | 1.84016 | -50.49952 | 2024-10-22 05:31:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fabc9102-67b2-3e2a-b04d-36070499d1c5 | 1.83938 | -50.49485 | 2024-10-22 05:31:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe043966-7458-3a0d-9708-e52044147f98 | 0.9906 | -51.16236 | 2024-10-22 05:31:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b28d80db-bdb6-3a12-a701-9fa2c0942232 | 0.98462 | -51.16333 | 2024-10-22 05:31:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e02239c-7a4c-3ad3-9268-3cc496deebdb | 0.97767 | -51.1754 | 2024-10-22 05:31:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb31190f-cb6d-3e14-998a-fa6d4582e0cb | 1.01015 | -52.21972 | 2024-10-22 05:31:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec2cf523-b419-3c23-95fe-b060cdfb02be | 3.02883 | -60.25914 | 2024-10-22 05:31:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af4bd0ba-e660-3ae7-949d-c7d726c3d6a4 | -2.77826 | -49.29893 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65e4d4bf-9e46-3482-9826-976d048aad0c | -2.77726 | -49.30563 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89824ab9-1966-3f20-b9e8-acdb1d4089ba | -2.77626 | -49.31239 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0208ffee-bf22-370a-b138-5e6330ca03b5 | -2.77221 | -49.29101 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README31.md)
