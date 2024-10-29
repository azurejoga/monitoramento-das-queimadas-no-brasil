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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecae5b9a-1f8b-34e1-bcb9-9c979460fc63 | -9.74116 | -46.27235 | 2024-10-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ca4b25d-4330-3911-af21-d02eb61a1fba | -9.70266 | -46.2478 | 2024-10-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 539b7a13-bd7e-3914-9b67-9eb06010ca29 | -10.08857 | -47.40949 | 2024-10-29 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef5dbe8b-713f-3b17-8ab7-abfc1c81937f | -11.99881 | -47.16566 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| adc1049d-7c77-300d-9c3e-d74912d14ca4 | -11.99869 | -47.16429 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76862f92-5fa9-3aae-80b3-063a2900cf7b | -11.99816 | -47.17006 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd4bbc86-3e00-3863-b728-bbfc5231e677 | -11.99807 | -47.16869 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e870c89-874e-3e5d-b226-6001930c8084 | -11.99515 | -47.1651 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcbe89a0-6f04-3879-b1e3-29a9645b5687 | -11.99441 | -47.16812 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3319eb1c-c9f2-3784-a7b3-2479ad921e21 | -11.79258 | -46.48244 | 2024-10-29 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7b972ae-361f-35a6-ade6-4b270e40b2e7 | -11.78944 | -46.47717 | 2024-10-29 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58c3c5af-1525-324b-b786-834710228425 | -11.77554 | -46.46765 | 2024-10-29 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1df9a65d-52d7-368b-b023-5359d036d1e2 | -11.69206 | -47.11493 | 2024-10-29 04:40:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c598ee2d-75fa-30fb-be2d-b57a5d6bea78 | -11.69097 | -46.40685 | 2024-10-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f50e99be-caf7-3856-8f58-4a88b8aa0153 | -11.5084 | -47.17075 | 2024-10-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d454b0f-8d4f-3e86-8e76-7b2773b45d65 | -11.42198 | -47.14684 | 2024-10-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d0c8dfe-3bb6-3fb5-850a-0c33ca6d167e | -11.40586 | -47.07797 | 2024-10-29 04:40:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50f29076-efb5-3b24-a8e5-31216abd9664 | -11.39304 | -47.0892 | 2024-10-29 04:40:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ea0030-3bb2-3a8f-9f5f-5af03a6e7ae8 | -4.93212 | -47.56316 | 2024-10-29 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 740b7ea2-f29c-3160-bfd7-c120f14399ea | -5.01809 | -46.48193 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f99218a3-b075-350f-baa2-ae21b7771516 | -5.01217 | -46.49703 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4d66f36-0e5b-3e34-9152-2c6cef93a6a3 | -5.01166 | -46.47706 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99bfcb46-5e7c-324c-a467-5c18f440825c | -5.00814 | -46.47655 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daaab24c-e427-3119-9da3-d120b0306436 | -5.00522 | -46.47221 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4afdab39-a5f5-3cbe-8f68-8c3d7da53e5e | -4.98711 | -46.47325 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 881987ce-2db5-34ea-8d84-88512cb990c3 | -4.9836 | -46.47271 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ee5ef4e-c8cf-34e0-98fd-19f9cc8765e1 | -4.96308 | -46.48975 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5feff99d-3408-3ed7-b263-1bb5ba1261ae | -4.96249 | -46.49362 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22663c9a-47aa-36ed-aedc-7163f4c21491 | -4.96191 | -46.49749 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8211865d-7fdd-3a9a-9a21-4ebfa465b070 | -4.95899 | -46.4931 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7f5a29b-c0f7-3970-bd51-840089896bc3 | -4.9584 | -46.49696 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b4a83b4-27c8-373e-bfa2-78c289f6c682 | -4.77802 | -46.60535 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 795f3027-575c-3e8f-a236-1ec52ee2fc4f | -4.77054 | -46.39727 | 2024-10-29 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac5f56a2-92f7-3b8c-b135-8fe213bc5d0e | -4.62948 | -46.53999 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c61dbda-817f-3a73-bb46-d70c3eb588a9 | -4.50775 | -47.05938 | 2024-10-29 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f886e7c4-c837-38d5-b012-6f5284c8c315 | -4.50718 | -47.06304 | 2024-10-29 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1d617c2a-1a42-3582-8363-6619130ee575 | -4.50377 | -47.06251 | 2024-10-29 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 07039bb5-cea3-3f27-944c-d1babff8cccd | -4.626 | -46.53941 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a155b533-cb8e-3701-8444-eb11621e448b | -4.54256 | -46.60669 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f3e6438-dbd2-3b0a-a8ed-660d0bd9e5e5 | -4.50434 | -47.05885 | 2024-10-29 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6d513d55-8a74-39bb-b367-b0bfea9ee9bb | -4.50093 | -47.05834 | 2024-10-29 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a59fa63f-528c-3ad3-9282-d56d17cb0ec2 | -4.50036 | -47.062 | 2024-10-29 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3c7135c5-8f45-322e-adfc-b073ca837d51 | -5.01749 | -46.48582 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fe7cabb-4312-34fe-855f-7c9fa6636e12 | -5.01517 | -46.47755 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b509e7d0-d6c5-3d9e-bcb6-12e6b2d3f788 | -5.00873 | -46.4727 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 972fe1ec-f43f-3a4e-aa57-33e6d08de351 | -5.00171 | -46.47167 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44bf49b5-26a2-33f9-a1b0-3c9ea2cdf878 | -4.9801 | -46.47217 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5015a63b-1935-3a68-adc1-27d7ea9edb24 | -4.97949 | -46.47616 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d24d719e-3af2-39bf-958d-4e0046161889 | -4.96718 | -46.48636 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 290ae8b1-cefd-3d6f-87df-8fd0ca630843 | -4.96541 | -46.49798 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61f84f8a-c871-3f59-be45-45642850598e | -6.51329 | -47.04047 | 2024-10-29 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0b117089-85e2-3f1c-bc8f-7041ce452d06 | -6.51271 | -47.0443 | 2024-10-29 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b5c20dfa-2bf2-3821-ba39-1622f9b5302d | -6.51214 | -47.04813 | 2024-10-29 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3cc6d744-a344-3d9b-aeea-d4e6449088cf | -6.50924 | -47.04376 | 2024-10-29 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 41d8f27f-65ee-3ffb-8fcf-f7d2746785a8 | -6.50577 | -47.04321 | 2024-10-29 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0c258e0-f4af-3a92-b038-aedb5696b0c7 | -6.46381 | -47.16294 | 2024-10-29 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1e5fe47-37e8-3c4c-970f-d0a3ff59e1de | -6.4631 | -47.16192 | 2024-10-29 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0bebf37-b8c5-39cb-a8bd-492826803d2d | -6.42333 | -47.28816 | 2024-10-29 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 266bbbfc-f2d1-397d-ba1b-1ce6aa60b5e9 | -6.50866 | -47.04759 | 2024-10-29 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10d81c10-391a-36a4-9202-1a16a6aab3fd | -6.34788 | -47.14131 | 2024-10-29 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 710e30f0-ae4b-38b8-8dd4-e65eb2f277c5 | -6.27592 | -47.28861 | 2024-10-29 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edf68692-8c5a-31c3-8bfa-1630b6fa0104 | -5.94211 | -47.33813 | 2024-10-29 04:40:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97335920-8063-3a5b-b902-9687198d69b8 | -5.72883 | -47.19621 | 2024-10-29 04:40:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c65f29a9-be8c-37db-8f0d-1d7e8e83b32b | -5.61345 | -46.96725 | 2024-10-29 04:40:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 653afda0-7748-3961-8f7a-120a4ca185e9 | -6.50982 | -47.03993 | 2024-10-29 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9d159245-e194-3054-ae3f-a16510af9530 | -6.42856 | -47.41467 | 2024-10-29 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14379109-336f-370a-9822-a1438632292d | -6.29534 | -47.34525 | 2024-10-29 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d73fe5af-0cab-3fa3-b695-8b82f9535fbb | -6.29249 | -47.34096 | 2024-10-29 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96d43e45-ddbf-3cf1-b5cf-f037fbd5d364 | -6.08907 | -47.20368 | 2024-10-29 04:40:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0a4325-63ef-39ef-835d-09c8aa011fef | -5.91372 | -46.59838 | 2024-10-29 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e4649df-08d9-3d4a-965f-0c56dbddf59b | -5.79769 | -47.32029 | 2024-10-29 04:40:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80f45876-861e-3693-a1d8-c4509771e04d | -5.71589 | -47.44062 | 2024-10-29 04:40:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a08f1bb1-4eec-32f8-a32e-53e1e4ca2757 | -5.71081 | -46.71722 | 2024-10-29 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b780e93-d7c7-375a-86af-aa9d160d6815 | -6.36584 | -47.91885 | 2024-10-29 04:40:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2528c423-e056-3da7-ab0b-af35c1335a30 | -6.28561 | -48.06801 | 2024-10-29 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5a1376f-1eef-3e3b-bdd6-64d98f98cf0e | -5.64937 | -47.82761 | 2024-10-29 04:40:00 | NOAA-21 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c975389e-fac6-36dd-9a3d-115efb0cd8ad | -5.15102 | -47.71057 | 2024-10-29 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1af49d3e-5801-3d8a-a23a-f35e5515eff6 | -5.05977 | -47.75183 | 2024-10-29 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a23c299-3d6a-33c4-b97f-2ccb20465844 | -5.05921 | -47.75539 | 2024-10-29 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b84c3d68-b217-314d-bdee-437fcf4986a8 | -5.05687 | -47.66006 | 2024-10-29 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20a42ac6-f34d-36e9-b533-bc98526fef44 | -5.05641 | -47.75135 | 2024-10-29 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07d954ce-35a2-3c50-a74e-82982ee0e124 | -6.12833 | -47.26668 | 2024-10-29 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2adbe35-1319-3407-8098-6fab6e953521 | -6.09554 | -47.04579 | 2024-10-29 04:40:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 416b737e-3039-3a23-93a0-f7c62d07303f | -5.76151 | -47.0278 | 2024-10-29 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bda9c357-9877-333b-9770-eb3e3beb61e2 | -5.75806 | -47.02728 | 2024-10-29 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e552c667-7a47-3e1c-9ea6-e608491e54c5 | -5.72826 | -47.19994 | 2024-10-29 04:40:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ca7e0b9-7a6e-37ce-aa3c-38e8b5bce9f9 | -5.50882 | -47.16702 | 2024-10-29 04:40:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9945d307-9884-3c54-97ea-e87d0473cb82 | -5.43446 | -47.308 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 181a6b44-f5d9-39c6-bc11-aef3a8462326 | -7.43428 | -46.93427 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2091616-ed58-305d-a7e4-892e87a87452 | -6.98796 | -47.08211 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ce21426-6966-3286-96ac-138f96cdee05 | -6.98389 | -47.08545 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f382a508-dd5e-3549-a013-7f67a9cb0274 | -7.93031 | -47.75388 | 2024-10-29 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f7afeeb-f9eb-358d-acd3-927bc902bae0 | -7.5963 | -47.13398 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6eef312f-dcb8-341e-a82a-1317e0dfc27f | -7.54153 | -47.01434 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f7251d6-0ea7-33fd-a483-a5cc7462f3f5 | -7.47003 | -47.1797 | 2024-10-29 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de421079-0a9c-37c0-af7d-17cf32b6cf08 | -7.46945 | -47.18357 | 2024-10-29 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3148cf41-7a43-3ce4-b028-cca661783f5a | -7.37768 | -47.60625 | 2024-10-29 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84835163-faaf-381f-a020-8b656ec5b950 | -7.33524 | -48.11495 | 2024-10-29 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96eeb3c4-805c-3087-a795-30ae4f3f15f5 | -7.05516 | -48.29923 | 2024-10-29 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcd8f1e1-64c1-3317-9e11-8802c75725f3 | -6.98737 | -47.08599 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README60.md)
