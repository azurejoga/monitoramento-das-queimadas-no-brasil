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
| 2a9eb617-4566-3261-a1e4-f09ce4bd51cb | -4.8399 | -50.9345 | 2025-10-25 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 7cf5bb86-0cdc-3859-b668-325ad318d2a8 | -5.3835 | -40.7191 | 2025-10-25 00:00:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 6d110344-6f9e-3412-902b-b427fcb687db | -4.8214 | -50.9353 | 2025-10-25 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 597296ec-c05c-3a99-8d44-940f766707d9 | -19.7791 | -48.278 | 2025-10-25 00:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 91a12afd-78d5-3355-8f2a-f21fe538344f | -4.7018 | -46.4508 | 2025-10-25 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| fe264128-e572-3b9a-a4ec-16157bd9ba95 | -19.3343 | -49.0812 | 2025-10-25 00:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 5f45e943-a84e-3338-974b-f478cf2d5bd8 | -14.3744 | -51.8038 | 2025-10-25 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 631443fb-2c7c-3cee-ae9a-2e990fe57d2d | -5.3837 | -40.6947 | 2025-10-25 00:00:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 0e8d6488-7c99-33be-a126-9683b7c407d5 | -19.7784 | -48.3011 | 2025-10-25 00:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 040e0d71-13a0-3061-bd04-e7ef1d2ebe92 | -19.7587 | -48.2824 | 2025-10-25 00:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 303.0 |
| 9fb94d80-7426-335a-a719-8a1a083939b5 | -3.8268 | -50.2019 | 2025-10-25 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3bfba9d6-189c-32cb-93a2-cb1501d66802 | -18.1714 | -51.7466 | 2025-10-25 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| ebbebc96-7f18-34df-846a-e53e55e17fe2 | -19.7581 | -48.3056 | 2025-10-25 00:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 5d746cb1-b49e-38f8-a2aa-148a48446452 | -5.3647 | -40.7206 | 2025-10-25 00:00:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 71.1 |
| dc874c26-0eda-3417-92ca-307536589dd3 | -4.702 | -46.4286 | 2025-10-25 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| bbca3bac-a31e-3408-85d5-31d387599fee | -2.7964 | -49.136 | 2025-10-25 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e94e8b86-7d8c-3fda-9121-7fd80480e0dc | -18.1709 | -51.7685 | 2025-10-25 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 535210e8-6968-32bf-ad3a-2ba4aab3f52e | -4.8769 | -42.9319 | 2025-10-25 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| cc00b3de-2aea-3095-8d36-81a999a76974 | -18.5634 | -50.2666 | 2025-10-25 00:00:00 | GOES-19 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 55.9 |
| bab2c4aa-a2b6-30b4-adf2-00cb07d86f63 | -4.8933 | -43.2349 | 2025-10-25 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c02a9fd5-0c42-3ef3-9ea2-6762d0fe108f | -4.7206 | -46.4276 | 2025-10-25 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b26a0bb5-1b1f-37c0-b91f-3450fb37549a | -2.8149 | -49.1354 | 2025-10-25 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 28fd2af3-8fee-3264-9db7-bebcfa29f43c | -3.8268 | -50.2019 | 2025-10-25 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 3f8c94c6-9022-3b15-a18b-a8ed9daab9f5 | -18.1709 | -51.7685 | 2025-10-25 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| dd7eef4f-f372-32e0-b52c-eb82676f86cf | -4.8933 | -43.2349 | 2025-10-25 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a15b2f09-e96b-3be2-8822-00573680392a | -6.8153 | -42.3987 | 2025-10-25 00:10:00 | GOES-19 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 98910da2-8c40-381a-94c2-2d9214301a37 | -4.8399 | -50.9345 | 2025-10-25 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a0c6d2b6-3aef-3950-ba29-5262f2c0b321 | -5.3835 | -40.7191 | 2025-10-25 00:10:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 0ac0beb5-c93b-390b-b1ef-34504b867d31 | -19.3343 | -49.0812 | 2025-10-25 00:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 488413d6-623c-3458-b13e-766db16cd69f | -10.5057 | -50.2371 | 2025-10-25 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 080e1d59-8251-306c-a249-95de022a3eeb | -5.4527 | -35.5565 | 2025-10-25 00:10:00 | GOES-19 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 76.9 |
| d5f142d9-ff5e-3bf2-b3de-d96223482b23 | -2.7964 | -49.136 | 2025-10-25 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 70031272-84ee-3a27-9014-7eef2cbe6b44 | -2.9072 | -49.1753 | 2025-10-25 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 37183a2c-e369-3339-83e1-4caedb3493b3 | -18.1714 | -51.7466 | 2025-10-25 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 632e9897-c7fc-344b-b3b1-95c4300a318e | -4.702 | -46.4286 | 2025-10-25 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 30004dc1-e895-38e3-8055-ff77238437d5 | -5.3837 | -40.6947 | 2025-10-25 00:10:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 0d6cc569-b910-3345-82ea-afefad383f12 | -19.7784 | -48.3011 | 2025-10-25 00:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 4f8b01ea-b8ec-3742-a8ab-651390e54bf1 | -2.8148 | -49.1567 | 2025-10-25 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5e3aa4b3-658a-3113-bf04-12a47d2c1478 | -4.7018 | -46.4508 | 2025-10-25 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| bcf93eea-8c78-367f-918f-2a6a28c13ee1 | -19.7587 | -48.2824 | 2025-10-25 00:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 309.6 |
| 65153604-8e10-3ccd-9d6b-cb8ef57bec05 | -2.8149 | -49.1354 | 2025-10-25 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 7e1017dc-7464-36fa-ae47-d02337613866 | -19.7581 | -48.3056 | 2025-10-25 00:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 210.3 |
| fecc61cb-d1b8-303c-ae46-077efbc58141 | -4.8214 | -50.9353 | 2025-10-25 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d5489822-d355-36fd-829b-e977c6243ef0 | -5.4524 | -35.5836 | 2025-10-25 00:10:00 | GOES-19 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 147.4 |
| c6de01dd-c04a-3577-b076-bff8e8570a07 | -4.8746 | -43.2361 | 2025-10-25 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 1c7c0eca-26b8-3322-9ce7-543537bdc86b | -19.7791 | -48.278 | 2025-10-25 00:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 164.6 |
| fcc2c4a4-cfde-311f-907b-a4172f98c19e | -2.8149 | -49.1354 | 2025-10-25 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| e165bbc0-7495-31a6-9ab2-00f159af0794 | -19.7587 | -48.2824 | 2025-10-25 00:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 170.3 |
| c6e51ce4-d967-3df9-bf0c-75b4da96998f | -15.2436 | -47.9302 | 2025-10-25 00:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| d9165a4b-2cf6-32cb-bf14-2c3092d56ea0 | -2.7964 | -49.136 | 2025-10-25 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 28803dbe-c428-31fd-9b2e-6e6ba6a1e19b | -19.7784 | -48.3011 | 2025-10-25 00:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 9922dc1b-8c37-3b4a-ba76-6e2247f93e4a | -19.7791 | -48.278 | 2025-10-25 00:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 47729020-8a72-38e6-b87d-5ad31f9fc397 | -18.1514 | -51.75 | 2025-10-25 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| d328a683-054e-3868-a0f3-e28dd548d58f | -4.8399 | -50.9345 | 2025-10-25 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| d7e6fc23-592c-3fe6-aa6b-3cb20841d602 | -4.702 | -46.4286 | 2025-10-25 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d145ae39-bec6-3c74-aa7e-12c5835dffcc | -3.8268 | -50.2019 | 2025-10-25 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 4067af06-582f-3c3c-aaba-cf72a5f14adf | -18.1714 | -51.7466 | 2025-10-25 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 167.7 |
| f589b2f9-3f00-30ad-bd87-cb2517067e76 | -21.5008 | -44.6681 | 2025-10-25 00:20:00 | GOES-19 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| 9ed828a8-59aa-3b38-a4b7-224bdd709cea | -2.8148 | -49.1567 | 2025-10-25 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 82ab855a-c2ba-3cd4-8827-11686380ca14 | -4.8933 | -43.2349 | 2025-10-25 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 1c53f36e-76cc-3b7d-ad17-5fee1239d37a | -18.1709 | -51.7685 | 2025-10-25 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| ca7f2d02-7c53-30aa-a092-7f87a7390a70 | -7.1723 | -45.8525 | 2025-10-25 00:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 0ab72a6f-4632-36d0-8614-fdd1740fd8ae | -19.7581 | -48.3056 | 2025-10-25 00:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 54d6a2cb-2854-3ace-83a0-7e5251678ef9 | -4.7018 | -46.4508 | 2025-10-25 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 7cab9849-87c1-3c4a-920a-f2a15ba71756 | -23.20352 | -50.03882 | 2025-10-25 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| 4186d69f-6327-34ee-a934-4554fa544938 | -23.12082 | -50.20499 | 2025-10-25 00:28:00 | TERRA_M-M | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 668b61a0-551d-3727-ba8a-8d69b037ab59 | -23.20505 | -50.05193 | 2025-10-25 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 55.8 |
| f942adcc-04ad-3055-808c-8f3b8496cc18 | -23.39485 | -49.68065 | 2025-10-25 00:28:00 | TERRA_M-M | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 659d20a3-9182-3067-b6ce-fea834310970 | -23.89769 | -51.23765 | 2025-10-25 00:28:00 | TERRA_M-M | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 6ed8d426-a7da-3e03-888b-cb29f5c572ba | -23.89804 | -51.24876 | 2025-10-25 00:28:00 | TERRA_M-M | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 5e52e9f4-5a15-37da-b306-f4d130a682cb | -23.40491 | -49.67913 | 2025-10-25 00:28:00 | TERRA_M-M | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| 98ddb92d-4187-3f5c-82be-0ca9d71ade30 | -23.76635 | -50.74945 | 2025-10-25 00:28:00 | TERRA_M-M | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 791de1b0-1570-39ec-937d-a1e46152e03a | -23.24728 | -50.41765 | 2025-10-25 00:28:00 | TERRA_M-M | SANTA AMÉLIA | PARANÁ | Brasil | 4123105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| a57e74f1-cafe-39e2-b058-3f6ece00fd0d | -23.41498 | -49.67759 | 2025-10-25 00:28:00 | TERRA_M-M | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 40.6 |
| e309d90a-fef8-3491-9842-4aa756d4c5a9 | -23.40639 | -49.69185 | 2025-10-25 00:28:00 | TERRA_M-M | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 7c3ee5a2-bcf8-3f1a-bc85-a567b0836fd9 | -22.2848 | -46.83065 | 2025-10-25 00:28:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd95e13e-457e-3310-97da-114be1fdb5ff | -23.39542 | -51.12581 | 2025-10-25 00:28:00 | TERRA_M-M | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 3d60bc2a-6fee-3544-a139-80c9d696ea74 | -23.36983 | -47.31577 | 2025-10-25 00:28:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| c3fc1c2e-b023-3eee-a1e9-1c6ab2b03e52 | -21.8898 | -45.27267 | 2025-10-25 00:28:00 | TERRA_M-M | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| cbe39d69-66e0-370a-bf73-faa9b9a209c0 | -23.76246 | -50.74097 | 2025-10-25 00:28:00 | TERRA_M-M | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 0d6466c7-7ac7-32b4-8da9-6edc4de90adf | -22.60936 | -47.19354 | 2025-10-25 00:28:00 | TERRA_M-M | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4b07f495-82c0-3321-b7fb-ad952530f30b | -22.58059 | -44.27567 | 2025-10-25 00:28:00 | TERRA_M-M | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 8e4e81f4-6c30-32b0-8aa7-bcf241084967 | -23.34145 | -47.16897 | 2025-10-25 00:28:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 70c22515-5240-3a50-860d-057be4fea764 | -2.8149 | -49.1354 | 2025-10-25 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 76681aed-d08b-31f1-baf4-19efe6b3072f | -19.7587 | -48.2824 | 2025-10-25 00:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 6e5cf53b-d497-3f21-85d0-6e875e805a30 | -18.1709 | -51.7685 | 2025-10-25 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| c77759e7-822f-3513-ab79-3aa39256dc9e | -4.702 | -46.4286 | 2025-10-25 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8282f100-f440-359c-ad1a-62d4a0a7cf92 | -18.1714 | -51.7466 | 2025-10-25 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 140.1 |
| e2e8aa31-be7d-3dc7-80c0-d1f11a6f0bff | -19.7581 | -48.3056 | 2025-10-25 00:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 3735ba5e-890b-3c3b-a985-f3b8e21b8276 | -15.2436 | -47.9302 | 2025-10-25 00:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e3bc0736-78ba-3fde-ae13-c4a91f71a93d | -2.7964 | -49.136 | 2025-10-25 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 9d447808-d63b-3ddc-ae9a-adfa8bec67a4 | -19.7791 | -48.278 | 2025-10-25 00:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 214.4 |
| a732eaff-5ee2-3e85-ba68-1f723d5e560e | -4.8399 | -50.9345 | 2025-10-25 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 7ad0ba52-b75a-3fbb-a607-bb7ed7916e91 | -3.8268 | -50.2019 | 2025-10-25 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6a253711-539a-3d85-b077-b9a089b70bdc | -2.7964 | -49.1572 | 2025-10-25 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c9c4f06a-0ac6-359d-83c7-973b86b74d57 | -4.8933 | -43.2349 | 2025-10-25 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| cba332aa-502f-30fa-8eac-5a46814f9860 | -2.8148 | -49.1567 | 2025-10-25 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 649f6d30-f2f5-397b-8c4a-ff3cb574f4a5 | -4.7018 | -46.4508 | 2025-10-25 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d182bb27-31ee-3432-b112-efadbefce7c6 | -19.7784 | -48.3011 | 2025-10-25 00:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 13ad6033-05d1-3938-8dc9-c62fc7ba0ff7 | -19.62725 | -46.1366 | 2025-10-25 00:30:00 | TERRA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |


[Clique aqui para ver as próximas entradas](README2.md)
