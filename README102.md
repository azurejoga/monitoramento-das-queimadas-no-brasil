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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 934c91c1-a4d5-3823-b11c-eb9b6b47ddbf | -5.87395 | -48.09681 | 2024-09-28 12:49:00 | TERRA_M-T | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| dee3e175-f25e-31b2-a984-d15041a41626 | -5.22611 | -49.12945 | 2024-09-28 12:49:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 92d1e25f-c8c9-3533-a771-216602b60df3 | -5.21899 | -49.24019 | 2024-09-28 12:49:00 | TERRA_M-T | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3fdae325-116a-34a3-a606-54cf6bc79bb1 | -5.21791 | -48.35809 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4e9bcfe0-4d8f-3f98-8408-47e612e7624a | -5.21032 | -48.34798 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 31d24943-9549-3363-acc2-23cb6243d365 | -5.20904 | -48.35683 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8e9066d6-30c6-3467-96ad-94d97faa257e | -5.20807 | -48.17625 | 2024-09-28 12:49:00 | TERRA_M-T | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 224b6472-2506-384a-931d-21fba90982bd | -5.94592 | -49.18949 | 2024-09-28 12:49:00 | TERRA_M-T | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| fa76dd86-5e5f-37dc-b63a-58570de7236f | -7.71804 | -49.99202 | 2024-09-28 12:49:00 | TERRA_M-T | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0ed48a2c-2130-3e16-91a3-f6fb4be622f2 | -8.26828 | -49.44831 | 2024-09-28 12:49:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 83689bc7-befc-3cf5-9d6e-6590cb1b1334 | -8.24052 | -49.38914 | 2024-09-28 12:49:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 126158a3-0c3c-3390-876b-dd83f8b3f22c | -8.10041 | -49.52237 | 2024-09-28 12:49:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f3afce88-7162-3008-ad6d-1ab6ec331c1f | -8.24185 | -49.38013 | 2024-09-28 12:49:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 812118eb-c185-359f-8857-83482ab9be32 | -8.23294 | -49.3788 | 2024-09-28 12:49:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bae016a5-2ef8-3813-8da1-e5c3eb81ee0c | -8.23161 | -49.38785 | 2024-09-28 12:49:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 599a2c8a-43aa-3191-b433-eb55e2f595e1 | -1.32838 | -49.29301 | 2024-09-28 12:49:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| a3828082-2eb9-31d7-8b99-36b3de8d9ce0 | -1.31906 | -49.2917 | 2024-09-28 12:49:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3533972c-5947-35f3-a05f-a579a53bb435 | -1.2726 | -49.11015 | 2024-09-28 12:49:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b0fa98b6-7a7d-3ecb-b13f-3633ff89cc85 | -1.27119 | -49.11979 | 2024-09-28 12:49:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3440ab67-47d5-3a0e-b3fb-955ce73c9398 | -3.19714 | -50.43686 | 2024-09-28 12:49:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| a4b8b325-a7df-3e86-9e0b-43a219a204be | -3.13807 | -50.28091 | 2024-09-28 12:49:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9aed8f22-2c97-3162-a3bc-4ec5cb6df168 | -2.88364 | -50.39986 | 2024-09-28 12:49:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2036aea6-776d-31b6-9e42-89e25547a067 | -2.75775 | -49.23438 | 2024-09-28 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 201f1be9-8fd7-391e-af6a-9f964cd177e9 | -2.48295 | -49.15769 | 2024-09-28 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f77492b4-c548-3850-8b96-f20562a9bcbc | -2.47379 | -49.15638 | 2024-09-28 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 54b2cde5-42e5-39da-961f-ecab22029211 | -3.57742 | -50.56025 | 2024-09-28 12:49:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 7cc5ed85-1e03-3156-bc10-74d401f90733 | -3.57584 | -50.57099 | 2024-09-28 12:49:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 07596c92-7154-3066-ab83-405dd6d397ca | -3.56559 | -50.37339 | 2024-09-28 12:49:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9f7aa4c3-dd34-3a3a-a090-ec1cbd70409f | -8.0725 | -51.1311 | 2024-09-28 12:49:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3da1c7a8-8f93-3e33-9819-149824abd1ae | -3.01429 | -51.04502 | 2024-09-28 12:49:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 00429bb9-15c1-3d8b-a6cd-20b972fbef4d | -3.01253 | -51.05677 | 2024-09-28 12:49:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 4aecd81c-9cc6-3c84-9064-43d2fd9c5a09 | -5.94053 | -53.44157 | 2024-09-28 12:49:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6669a3e8-a99e-3629-aaf3-71317fa4ce77 | -10.69247 | -58.52555 | 2024-09-28 12:51:00 | TERRA_M-T | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 790cba7c-3d6d-3ad7-9a82-639d260d1322 | -10.69973 | -58.51958 | 2024-09-28 12:51:00 | TERRA_M-T | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| a76da659-8269-31a7-88d5-9cf65cdd5ee9 | -14.90141 | -57.9734 | 2024-09-28 12:51:00 | TERRA_M-T | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 0c1774ed-882f-37ff-a5b2-2e8fa1d34507 | -14.32815 | -41.8019 | 2024-09-28 12:51:00 | TERRA_M-T | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 185.7 |
| 6bf55b55-772a-367e-a3e6-27cd307d650a | -14.32778 | -41.7965 | 2024-09-28 12:51:00 | TERRA_M-T | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 160.5 |
| 4c6c525c-3480-307a-91d8-12c7aefe9637 | -14.3247 | -41.824 | 2024-09-28 12:51:00 | TERRA_M-T | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 0b01f20c-e65a-3afc-b585-e41e12d5e734 | -14.27964 | -42.09376 | 2024-09-28 12:51:00 | TERRA_M-T | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| c2071a88-74c5-3f17-8d7f-5b54737a3171 | -14.24447 | -41.31377 | 2024-09-28 12:51:00 | TERRA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 9b04933a-5dd5-37c3-9aaa-2493b3de603e | -15.1509 | -42.00264 | 2024-09-28 12:51:00 | TERRA_M-T | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 36.3 |
| 490e9bc4-15a6-320f-84f7-76db9565d3c7 | -15.13706 | -42.00657 | 2024-09-28 12:51:00 | TERRA_M-T | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| 3062c593-c693-3dc8-8e56-388750da7ff3 | -11.61788 | -42.73256 | 2024-09-28 12:51:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 124.0 |
| a9829b09-09db-349f-83a4-b459db53f812 | -13.76931 | -42.46415 | 2024-09-28 12:51:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 34deb8cc-4740-3c30-9a1c-cfb41e6842ef | -13.16036 | -42.34816 | 2024-09-28 12:51:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 88fd10a3-cb78-37be-99e2-b5030f37dbb0 | -13.08282 | -42.35606 | 2024-09-28 12:51:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 49.6 |
| c81ea2a0-7416-37ca-b165-0376aa1fe316 | -13.74433 | -43.46225 | 2024-09-28 12:51:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 6964d2f6-b01a-397d-af1d-ce23779c2d15 | -10.26165 | -43.57414 | 2024-09-28 12:51:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| c5d96a3f-54ad-332c-82ed-d948e503eb1e | -13.42313 | -43.96488 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 77132141-d2a5-3a8e-a8c3-9ea7b0657fab | -12.99409 | -44.7447 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| e31ddbf2-e05b-3a6e-9958-9f9945e85c24 | -14.52404 | -44.95589 | 2024-09-28 12:51:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 9996d9d3-1768-32ae-8b0e-ac03616d9e75 | -14.52141 | -44.96111 | 2024-09-28 12:51:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 082b53db-5c88-3918-8860-b6942d629f05 | -15.79017 | -44.67147 | 2024-09-28 12:51:00 | TERRA_M-T | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| dcdd887a-0fdd-30cc-b8fb-e6169e913db5 | -15.78811 | -44.68895 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| a4b2f883-fd27-34c2-984e-e0fb846f961f | -16.88892 | -45.31456 | 2024-09-28 12:51:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6a47f7b6-1af1-316a-a659-2bad47662f84 | -16.87731 | -45.31308 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| acb52053-5245-3f4c-b9dc-2690ef926316 | -16.8754 | -45.32941 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f4cfaada-8b16-3569-ad06-bb489dc362f1 | -10.71634 | -45.8682 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 5541525d-159c-30d3-bba0-83bb167a1bc3 | -10.71476 | -45.87987 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 390.6 |
| 5fc69063-f8e9-31ff-aa65-4fbcacd8bfc9 | -10.71319 | -45.89148 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| d6fd878a-92a1-3eb0-8e93-09a33a187eae | -10.70621 | -45.86672 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| d137e272-c7a4-3184-be4b-8fa9e3340ec3 | -10.70466 | -45.8783 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 164cf89b-e27a-3e94-a41b-df5b6418683a | -10.69765 | -45.85352 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 3e80aa9a-20c4-3f46-b959-d2e17176b7d5 | -10.69611 | -45.86511 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| f2b92d18-4fa9-3dd6-8298-740714b2c449 | -10.68751 | -45.85213 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 0f87cc10-c80c-3c3e-8341-79f674789461 | -10.68498 | -45.94829 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 4ab0fc3c-45f0-3f79-9d18-9de159929d48 | -10.68342 | -45.95992 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1a126214-fe87-3c21-a63c-2db992be3855 | -10.68276 | -45.88784 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 358.7 |
| c5c1b7d4-c2e9-3cc1-9a26-a6fe99fc1c60 | -10.67582 | -45.86241 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 23df1a99-aba4-3eac-a05f-2e91e7de0b4a | -10.67489 | -45.94699 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5ac24684-0793-3c52-acd5-d605fbc0cb74 | -10.67421 | -45.87459 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 272.3 |
| e5d146ef-225e-3bf2-9fa7-ebf88b82e158 | -10.67334 | -45.95861 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 0b98b69e-1c39-3fe2-a530-10b8d0ab3d5a | -10.67262 | -45.8866 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 5bdab999-d942-32f1-aee0-97629dc6e5c4 | -10.66568 | -45.86105 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 5ed5c1e9-56ce-347b-b36e-546dda2733ba | -10.66407 | -45.87328 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 251.4 |
| c1a56d9f-38d7-3773-87a6-a8c8eb4390f9 | -10.65551 | -45.85987 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| da688d03-ea1e-36ef-8c2d-4dd5cc83d4e8 | -10.19873 | -45.7734 | 2024-09-28 12:51:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 01397262-2331-3ca7-852b-d72a71b0d876 | -11.25374 | -45.4057 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 8ac358a6-dbba-32be-9dc5-ddbb1c685046 | -11.24895 | -45.39878 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 9fc8cbbf-b6ea-3e7c-b119-b8ec90f42f94 | -11.14423 | -45.57457 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 3c01b62b-d18d-3c46-8161-42f37da51268 | -11.14242 | -45.58789 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 22cf2cea-2f82-3cfb-ab41-32ea5c23c59e | -11.1424 | -45.50924 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 572f46a6-429b-3721-a6db-dc5d0cbc601d | -11.14151 | -45.56704 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 35fc6a99-706a-3142-882c-198ad6120151 | -11.14069 | -45.52198 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ad704edf-23ab-3ac4-a35c-cf633cedb988 | -11.13981 | -45.58036 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.5 |
| e4dcf915-2aaa-3ace-b40e-78564ea3831b | -11.13372 | -45.57383 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 02bd8313-acbe-3785-aaec-10d936f580c9 | -11.1303 | -45.59924 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 5686309d-4abb-3627-a4d1-c9785ea04173 | -11.12164 | -45.58489 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 8dbf65d0-a761-3725-ac46-a8828c719097 | -11.11994 | -45.59759 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 262.3 |
| 23538bbf-2cfa-3ed0-ba9a-6370682405a4 | -11.11826 | -45.61017 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| f92e5377-44b9-3f02-a776-354e0706b9b9 | -11.10957 | -45.596 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8345c253-f59b-33be-92a6-830f71d2442a | -10.8607 | -45.55656 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| caf7f0b8-fe49-3a3d-9614-96db13df2702 | -10.8503 | -45.55525 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 09fd3bb8-aee9-3340-b5de-dbc06c2b68dc | -10.84862 | -45.5678 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| a402ede0-3719-30b9-b5a7-d3847720d541 | -11.30139 | -46.14537 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 242a2416-2bfd-3ad1-893c-d0807bbc26e6 | -11.29138 | -46.14389 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 9a222e67-a04e-3798-bacf-576f03a80701 | -11.06752 | -45.75478 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3fd08e04-c3c9-35ef-a083-6e6cf7ad94f3 | -11.06591 | -45.767 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 1fa77ec3-d1f9-3e54-9492-b858f9a31ed5 | -11.05883 | -45.74133 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e336c9ae-bfd2-3405-aefb-3a40c8b80e6c | -11.05721 | -45.75372 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 247.2 |


[Clique aqui para ver as próximas entradas](README103.md)
