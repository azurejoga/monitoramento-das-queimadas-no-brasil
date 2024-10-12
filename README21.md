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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bf23419-7f3f-37a9-8a75-67eeee507a32 | -17.66771 | -56.25639 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.9 |
| 314f412b-b0f3-36d8-ac31-f81b30f5aaf6 | -17.66643 | -56.24714 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| a347dcae-a692-3be8-a80d-9a6f31119ed4 | -17.66515 | -56.23789 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.3 |
| 3780fec0-1454-3f7d-8435-3e2d33b876a1 | -17.66269 | -56.2855 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 825b9ff7-64ce-302f-8fde-e50bccfc4ff7 | -17.66141 | -56.27625 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 85e291eb-6677-3747-994d-a27e5e2b947d | -17.66013 | -56.267 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 54d1cf5a-b740-382e-9f45-8868d15645d1 | -17.65885 | -56.25775 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 9ae00a44-fe9c-38c0-9c43-b49e05987284 | -17.65757 | -56.2485 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 644be33b-b2aa-3ca8-bb93-602c033098db | -17.65629 | -56.23926 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a9c408aa-c766-372c-8389-1a0048c83df4 | -17.65383 | -56.28687 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 1158e848-760a-3fc5-be0c-8444fe10560b | -17.65127 | -56.26837 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.1 |
| 41bfbb96-c82d-365e-968b-f73af57f4de1 | -17.65008 | -56.32525 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9a8f62f4-c845-3373-88e7-bfea73cc6698 | -17.64999 | -56.25912 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 5c8f424e-73ab-3003-a3f6-3aa600cb08c0 | -17.6488 | -56.31599 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 53db9c7d-c4d0-34de-ba84-fcb7647c7165 | -17.64052 | -56.33256 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.4 |
| dc940f55-1dc3-3193-bc0a-37bf4df9a841 | -17.63924 | -56.32331 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.4 |
| de5cd83a-2db6-3223-a0ce-e8067b1aef2b | -17.63796 | -56.31405 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| bb401fd3-7623-397e-9d5c-e246382cc803 | -17.63166 | -56.33392 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| adff3177-3137-3621-9211-b96c61976cb6 | -17.63038 | -56.32467 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| e491f0da-c5a4-34e8-8388-491a73b47c56 | -17.06649 | -56.03728 | 2024-10-12 01:34:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| c6f9dd93-7256-33a1-bab6-bf4c0289c627 | -17.0652 | -56.02807 | 2024-10-12 01:34:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7cd600f0-60d3-34ef-b7c5-2a8afa78c5a0 | -17.06261 | -56.00964 | 2024-10-12 01:34:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| d5cba2a2-935f-3e7e-a804-7bb3260c74b7 | -17.04416 | -56.01842 | 2024-10-12 01:34:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| d2141db8-e24f-3834-b930-a2bb68b2389b | -17.02904 | -56.03959 | 2024-10-12 01:34:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 92fcbdb2-cce2-3552-9803-605284d0d272 | -17.02774 | -56.03038 | 2024-10-12 01:34:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 28.0 |
| fa81b78e-57f9-3486-b5cc-44c04062012e | -18.22938 | -56.5228 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| a9cb60c6-ccb1-3e27-8f67-652fe11927bd | -18.22811 | -56.51344 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 9cf50dc4-0eb0-3b27-9063-1e68d4f403e7 | -18.22011 | -56.53003 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 7698a79e-d88d-355a-9beb-75545526757a | -18.21627 | -56.50198 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 625e031e-ea8a-34b1-b12f-fa837a4d7175 | -18.21122 | -56.53139 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| bb5c643b-563b-31a9-8491-5660c201bcfb | -18.20994 | -56.52204 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.8 |
| 2fb770a7-ed22-382d-abf7-e125fc2f6eda | -18.20232 | -56.53275 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 411e0122-ee4b-32aa-ac7e-6110afc91fca | -18.20104 | -56.5234 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 6c18dfe1-3cde-3923-ae15-797ae6dbbb3c | -18.19343 | -56.53411 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.1 |
| e92238d5-a245-3a0d-b88f-58ed3b20664d | -18.13108 | -56.34369 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| fa7cda93-551f-3a0f-a4ed-14849aebacea | -18.1298 | -56.33439 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 431dc891-d783-38d1-97c8-c32542f79481 | -18.09377 | -56.41281 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 140a28a5-d9b6-386e-8b74-480af8ee9b2a | -18.09249 | -56.4035 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 119fdf46-0de5-30cf-9c25-d382964ac8cd | -18.08617 | -56.42349 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 08d541f1-9443-3f48-b0b7-4bb908dda7a2 | -18.08489 | -56.41417 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 1f3c3c13-a125-345a-b95b-35d6b89eba46 | -18.08361 | -56.40487 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 1e53879f-752c-325d-9270-403847f1c525 | -11.9366 | -56.96835 | 2024-10-12 01:34:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 632311f9-8eb7-3143-bfd3-4063c4b90355 | -11.93533 | -56.95935 | 2024-10-12 01:34:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d2faefd-f71a-31c3-a4e5-541b2967995a | -11.93151 | -56.9323 | 2024-10-12 01:34:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2270b746-b6e4-3bac-a23c-8a066e871c78 | -11.91919 | -56.92195 | 2024-10-12 01:34:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b3b35758-1135-3417-b47f-c1807bdf526d | -11.91792 | -56.91292 | 2024-10-12 01:34:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4331f1e8-8024-3592-9476-778074c52298 | -11.84957 | -56.87708 | 2024-10-12 01:34:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8f147ad6-b290-3ce2-8064-c47b45f3e079 | -14.35447 | -57.60626 | 2024-10-12 01:34:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 14c850d9-37b7-3060-b101-f15df9a2646c | -14.32644 | -57.60073 | 2024-10-12 01:34:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| d350ed61-52a4-3984-ab62-5fb73a63a84a | -14.32519 | -57.59148 | 2024-10-12 01:34:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e7101b74-535c-3c26-9da4-cd4346bc4476 | -14.316 | -57.59875 | 2024-10-12 01:34:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8ded157c-e20e-35fe-8f1b-48f44b91c8bb | -14.31473 | -57.5895 | 2024-10-12 01:34:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9c74edb3-1222-3d9b-87cc-2ed54878c412 | -15.8643 | -57.4777 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 32ff3878-807a-3426-9447-d446802f0abc | -17.98512 | -57.37981 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| b1b96505-ca2e-3c0a-a8af-b3c1eff246ca | -17.98385 | -57.37009 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.8 |
| d7484795-79e3-3682-9290-786db545b4ae | -17.97606 | -57.38115 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.1 |
| 45dadce6-323a-32ae-a870-7e643d00effa | -17.97478 | -57.37143 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| c5824bd2-0d37-3895-a369-8da56dbb6e72 | -17.96833 | -57.38818 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 2d2067c3-9b68-3edc-b900-f7512761f547 | -17.96703 | -57.37846 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.2 |
| 5b7818ad-eef2-342f-9db2-3b537dd51296 | -17.89588 | -57.32962 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 78498b68-0fde-354b-9841-5840e115c648 | -17.89461 | -57.31995 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 1170cfe3-a473-3ee4-b944-74a7563c15ea | -17.89333 | -57.31028 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1691e2a0-ee90-318b-b329-149853ae1003 | -17.88939 | -57.35033 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 24f793ee-48a3-3ce0-ba4e-79077f3f53f3 | -17.88811 | -57.34064 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.9 |
| bd4df85e-70ed-38d7-9058-47c762b0c154 | -17.88684 | -57.33096 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| a4181851-7d8a-3dda-ac81-2ec4f8a9c0a7 | -17.88556 | -57.32129 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.9 |
| bccdc174-9f7d-3cb1-972e-59ff513d80fc | -17.88428 | -57.31162 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 94e50b6f-9b45-3273-81eb-5d8e567b9311 | -17.88033 | -57.35167 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 60d4bbd7-2a14-3de9-af62-0c3d4afe1c6e | -17.87906 | -57.34198 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.7 |
| 29f72773-dca3-320a-87f0-4822b968c407 | -17.87779 | -57.3323 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.3 |
| e1353a9d-0dd0-3829-939d-63a937647b07 | -17.86849 | -57.3301 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.2 |
| c97f9ff6-ae7a-31ca-b564-4ed7de44509e | -17.86719 | -57.32044 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 13d2ba67-2198-3ee9-987d-384c5102d074 | -17.86333 | -57.36047 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| 9a804f8e-56c4-3275-996f-e4087175086c | -17.86203 | -57.35079 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 187.4 |
| eabce9e8-988f-3f09-80b9-052036b1ca79 | -17.86073 | -57.34111 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 34bb57f5-abea-3999-a81c-2fb6a3f16b0b | -17.85944 | -57.33144 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 1eba0b0e-646f-3820-8403-b1d40c6cb9a3 | -17.85814 | -57.32177 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| ce8e9b9b-cdba-3897-99e6-8c6118eaef69 | -17.85686 | -57.38119 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 8d440450-24db-3cac-8fc8-5dc1a95aab25 | -17.85557 | -57.37149 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.6 |
| cecf44a9-df00-3d7c-a794-531af530e819 | -17.85427 | -57.3618 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 90d00a3e-4aed-399c-aa99-a7368243908d | -17.85298 | -57.35212 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 368.0 |
| 3974a414-0def-3da2-8cb0-378c55b7e704 | -17.85169 | -57.34244 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.5 |
| f9a86c14-8f82-3908-b663-ba4697c3b4c7 | -17.85039 | -57.33277 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.6 |
| 1a0af569-0b5e-31db-a0a1-3d749963ab68 | -17.8491 | -57.32311 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 53250acd-41fa-311a-bcbc-9852999303bb | -17.8478 | -57.38253 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.5 |
| 2e3169fc-08ae-38e6-9a94-bd2d85a7201a | -17.84651 | -57.37283 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.6 |
| 22f5219e-8f1b-3fc0-9642-bd42a7bffeea | -17.84522 | -57.36314 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 220.2 |
| 7ac123dc-6656-3817-b458-20d82a62d134 | -17.83745 | -57.37417 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| bb534a72-919d-31da-8c87-0a9b04849888 | -17.83616 | -57.36448 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 91bdf8c4-dbdd-30da-a750-3f2a222bf475 | -17.83488 | -57.35479 | 2024-10-12 01:34:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 74c7e027-b49b-3047-9579-2f6dca75b5df | -17.18467 | -57.44394 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 37e1045b-bf16-3416-8358-122f26873e95 | -17.18339 | -57.43433 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 23f81c52-0ca1-348c-9621-262674cbde28 | -17.17691 | -57.45488 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| ca253d27-9e18-3fdc-99e0-73bf6bd5dfa1 | -17.17564 | -57.44527 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.6 |
| 061514d1-6548-33e3-92c1-c30fc8ac3a3c | -17.16137 | -57.4768 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 08eaf265-015f-3432-bcc6-ca122210741d | -17.1601 | -57.46717 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 94d68885-81b7-3bf0-9e48-bed482d6d7f2 | -17.06449 | -57.37024 | 2024-10-12 01:34:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 319becae-7baf-3f0b-8feb-0fabfe682b04 | -17.0008 | -57.44401 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 97071af0-ab82-3acf-b9d2-7f247510ca20 | -16.9956 | -57.4741 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 67bb80d3-6568-38a5-ae7c-c229c4165ac4 | -16.99178 | -57.44534 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.1 |


[Clique aqui para ver as próximas entradas](README22.md)
