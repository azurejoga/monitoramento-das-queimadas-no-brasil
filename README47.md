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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0bae54b-b918-3ea5-81f4-10a8c352bfc1 | -6.07997 | -44.06054 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ccab5de-4128-3e8c-864d-18ab0433d445 | -6.38981 | -42.91542 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a4d387f-e56d-3a8d-b338-f80c28c3dcf0 | -6.00537 | -43.79359 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 161614ec-84d8-32f4-bee2-6ff44731234f | -3.45347 | -53.83208 | 2025-09-30 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b2ffb9a-d4d6-38c5-bf18-9f2c46be2a61 | -5.76888 | -43.83448 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bac3b7fa-ebf3-383b-98a9-d72f620b1938 | -6.27167 | -43.65255 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04f0ddff-fdcf-3336-8d2f-595b192ab1e0 | -6.6493 | -45.32868 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 106590e1-c3d4-3f1c-9b23-40ab960db01a | -6.17469 | -43.9314 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7596cf4e-4eac-300d-be22-18961bcf87e2 | -3.09703 | -47.01765 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1f03dcc3-e572-39bf-8885-9921a01b8abc | -6.04988 | -42.46866 | 2025-09-30 04:38:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c2df93d2-7b4f-36f4-bb41-19d241a50698 | -4.29395 | -48.26895 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b8f9c81-e31c-3059-88ae-4355e10a9404 | -0.1009 | -51.27631 | 2025-09-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 990f9a78-cd4c-3955-9c9b-16d8b84b1007 | -5.25856 | -42.90055 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 973f6f16-221b-3d72-92ab-ec2b435301eb | -3.81253 | -47.5755 | 2025-09-30 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 05709c4a-146f-38c9-8903-c2169ce5cd84 | -5.8595 | -45.94537 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cc4ac12-a65c-327b-a975-80f0bccbb01e | -3.10495 | -47.01141 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4dd8bad1-0367-3660-a421-7ecfca4c2cca | -0.39616 | -51.78376 | 2025-09-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d43ff466-1070-33ea-96b3-5792a0544d16 | -3.05135 | -48.70841 | 2025-09-30 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 763162b7-8fa8-3d90-b5c0-cb1021afb6f1 | -6.4738 | -44.21869 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b5ea97d-7f84-3133-a169-d9e61845a314 | -2.07547 | -56.87848 | 2025-09-30 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c16aff3-42a8-3331-905f-8957270a813d | -5.74858 | -42.66468 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 04a8b099-c158-3385-8ade-fe582bb97950 | -5.31268 | -44.78881 | 2025-09-30 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2811e9a7-f566-3675-97d3-bbbf6d2d1ad1 | -3.50109 | -52.4693 | 2025-09-30 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b195ff75-2a08-3a1d-a229-50e1b349cef5 | -3.81199 | -47.57906 | 2025-09-30 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb158e58-b553-3efd-9357-2c3d345410e0 | -4.33301 | -47.88445 | 2025-09-30 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ce0333f-1717-36bd-9d18-26785cf11a59 | -5.91754 | -43.68165 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cfcb657-d267-3bfc-ae0f-cf7384d53ecc | -1.29368 | -54.1815 | 2025-09-30 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef03f0b0-e360-371a-b0bf-786a8c0a9b88 | -6.01079 | -43.80694 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce0e6c89-db21-39dc-b592-93b6f59ee097 | -6.88686 | -44.52871 | 2025-09-30 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc7988c6-650f-35f1-883d-bb2a49f16ace | -5.70627 | -42.63922 | 2025-09-30 04:38:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 843126a8-6058-3cba-942f-d49aaacde7cd | -6.09755 | -42.66258 | 2025-09-30 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 40ae76f1-a37c-3439-85c3-46f6f197580c | -5.94229 | -42.89952 | 2025-09-30 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 64b62aeb-f4ac-3f1b-a66f-6369ca865c50 | -5.23041 | -43.70068 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43f4b84c-e210-3642-802b-3e2925782b3c | -6.08092 | -44.06092 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e5de6b7-0257-32e1-b212-bf5313fcbfc1 | -6.12261 | -43.48887 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d438becf-8831-3867-90ce-196eaea34681 | -6.74842 | -43.36794 | 2025-09-30 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bcd242c2-7d24-37ea-b204-fe824db9acbb | -4.40428 | -44.39566 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 499ce2cf-7d7a-3047-a5df-762c077b8ead | -4.76929 | -45.32983 | 2025-09-30 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e1fe9ac-cc97-377f-b587-5bcd1b5ec788 | -6.24993 | -43.65311 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e6d51cec-4ef2-3736-8ad2-e05cfa9a6195 | -6.51076 | -44.24899 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75704211-bd7e-3ad8-9043-7a19e292aefd | -5.15854 | -46.41491 | 2025-09-30 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e184eb2-b752-3871-9622-431624bd52f7 | -1.59568 | -54.05943 | 2025-09-30 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0002add7-87e8-3240-bed0-b09662cd4ca6 | -5.52887 | -46.38355 | 2025-09-30 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bb2143c-369a-3fb3-bfaa-6d8dfb1b5eea | -6.46322 | -44.00316 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3186b215-a6bd-3273-8710-ec0b993a3191 | -3.83972 | -51.17525 | 2025-09-30 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8523d66f-3afc-3383-9c92-b2d2077da0d3 | -5.5124 | -42.72655 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b53d1697-8f1a-30b6-912f-524d4412b310 | -6.74477 | -45.62418 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 912aeabb-9ac9-3b4c-a001-da6f6478efc2 | -5.50407 | -44.01796 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c919975-bd8e-3120-aa41-a54fd3ac1c01 | -4.39661 | -44.39187 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4ec51cf-27c3-3652-bb41-a82472da068b | -6.80733 | -45.98801 | 2025-09-30 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebea75ec-7192-3071-b373-c27540d5d201 | -6.50035 | -44.11576 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 586f92da-3d1d-3f54-a543-4834ff8677bf | -6.1035 | -43.46984 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85ccbfc8-ad51-3722-980a-01d9713fbe9f | -2.82308 | -51.38394 | 2025-09-30 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d9f1591-7317-3a00-9f6a-83e4ae5899e5 | -5.76944 | -43.83073 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c87b3815-9a43-33c6-a925-f7a5c51a344d | -3.10099 | -47.01453 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2bd56657-066e-309d-abbe-b0aad65ad558 | -3.25651 | -50.11129 | 2025-09-30 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 651b040b-5d71-3864-9dac-2b4025d2d648 | -5.88265 | -48.11582 | 2025-09-30 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c7e46867-efa5-36e0-acbb-4155eb004fd5 | -5.51883 | -42.72563 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 854ca7e7-f33c-34a0-a09f-2872d36e8a8f | -6.79819 | -45.97327 | 2025-09-30 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6943bb3f-fdc2-3628-bdb8-7b4fb405b7b8 | -6.06698 | -44.87877 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8a99921-eafb-32a5-8284-1be358aead67 | -4.2603 | -48.55051 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd9ffafc-5989-35cd-b14d-4ee69895cf68 | -4.78228 | -41.04711 | 2025-09-30 04:38:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 94759eb9-0949-3176-9a1a-60e54a2605a1 | -4.89365 | -43.46394 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b9597b8-372e-3ca4-b299-4078dd36aa4f | -2.71304 | -49.43383 | 2025-09-30 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b469a809-cd45-3af6-98b2-7d7276523e4b | -3.25595 | -50.11484 | 2025-09-30 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ffe853f0-ecb9-3ca4-a3b0-6b297977ba84 | -4.07754 | -47.31075 | 2025-09-30 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec1c74f6-0fd6-3cd8-9c2e-bf6f39b261eb | -5.91001 | -43.70451 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7844230-ffbe-34b7-a61c-5fc2e8c87022 | -6.09821 | -42.65789 | 2025-09-30 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0467944f-2c89-3ef4-aaed-a64334b7a52c | -6.50254 | -44.2481 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a8f0fa5-fed3-341c-a3bc-0b93d2514d99 | -3.22424 | -49.34421 | 2025-09-30 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2f57598-2d4f-36af-8336-1bd11b5c0e13 | -6.30802 | -45.90028 | 2025-09-30 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ad5d255-eef6-3340-9336-55c0b78fc06c | -5.33961 | -43.72357 | 2025-09-30 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fdd0f1f-0040-3785-abac-738f2a2d2c59 | -3.25483 | -50.12194 | 2025-09-30 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faea5828-5721-3419-aca0-dc27e937f5fc | -5.70542 | -42.67673 | 2025-09-30 04:38:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d8c707b-cd63-3556-b2d7-0ce3c1247ab9 | -5.25792 | -42.90485 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 92f596f5-2030-34b3-b7c8-ec1bebb7e2bc | -5.74136 | -42.68236 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b731ae27-dec2-3cdc-8c06-b88ba561e1e9 | -2.52452 | -54.95736 | 2025-09-30 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e19269ee-638b-35b9-a0fa-9cd81c9392be | -2.58475 | -48.40379 | 2025-09-30 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cb54ade-c4f7-3f27-bac0-25361d867921 | -6.04029 | -43.81836 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ea9105e-6919-37dc-a443-3490b385a958 | -6.25049 | -43.64915 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28851d81-5494-329c-b2a4-b01f9a24c9ba | -6.20798 | -44.21321 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ad12563-2637-316c-a46e-8861fb396bf0 | -1.11789 | -48.03298 | 2025-09-30 04:38:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e2b3c66-4c1f-33c4-87c7-b4b358c534f3 | -6.10727 | -42.65926 | 2025-09-30 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 269594b9-d7ed-37bb-9074-989f7786e634 | -6.13663 | -43.48276 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5cd4e2c-e784-30de-a964-de59971c40eb | -6.30145 | -43.80439 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 106e1b26-8176-3d6a-b1fe-e8095d140332 | -5.28293 | -43.16624 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 965b254b-a471-3229-afd5-52b686c6f4f0 | -4.58048 | -50.69254 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e3d33e3-1faf-3134-ad27-33d6ba0cca3e | -6.41296 | -43.75281 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bc50946-c08e-3f68-ac20-b0444e6ce54e | -5.85698 | -50.06897 | 2025-09-30 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ccf5475-664c-3cf4-b9d8-c6342fc3dc64 | -4.86552 | -45.0522 | 2025-09-30 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 98fa73d5-563b-3be5-9711-8bcc5cd3bc12 | -0.09795 | -51.27163 | 2025-09-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b43bbddf-8062-37a1-b299-8cf9a929ac93 | -3.50039 | -52.47364 | 2025-09-30 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83ac9c6f-2b9e-3b27-9552-3c862874bdf6 | -4.39249 | -44.39391 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1acdc48a-d977-3fae-8522-6138d6301f26 | -3.09478 | -47.00983 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80f279f1-7e7b-3abb-9c4d-bbacfab74e0c | -5.85367 | -50.06845 | 2025-09-30 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ae4b7721-1aac-349c-877d-cd7c41b26eeb | -3.33303 | -50.25077 | 2025-09-30 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 113e1b4a-d6f4-3048-97b4-5b487f9e26ac | -7.01069 | -44.47619 | 2025-09-30 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dda2c8e7-b0a0-3091-b14e-962aee9c5521 | -3.4981 | -52.46443 | 2025-09-30 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fafbb196-7979-3391-916e-f2cc5227d27e | -5.2996 | -43.173 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0aa203a-743d-3a16-9fcf-37b9a1512b04 | -0.10025 | -51.28045 | 2025-09-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README48.md)
