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
| 2a6dc483-74ae-3405-8d8b-84ca515b24a5 | -3.59599 | -50.38597 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 323a64c3-85ce-38f6-adc1-0552737ac86e | -3.22989 | -53.92646 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e54c167a-5f9f-34fe-8d3c-da3d9d776c90 | -6.63995 | -47.34375 | 2024-11-26 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf74acd0-ab2e-3ba5-924b-e3d75fb39f62 | -3.96948 | -48.07049 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4ac57791-77b6-30b7-947b-facd94d8c80f | -3.97888 | -48.05405 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 593bc01a-e455-33b0-9fff-2e4103da99c1 | -3.55774 | -49.8825 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8558862c-7c7d-392d-954b-08f401ce1b65 | -3.68096 | -50.22451 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a140f550-5c11-3a34-9ad3-73bec1e2702a | -3.98506 | -48.08006 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 312d886a-8748-3a43-a9d7-05773c02a81c | -3.38648 | -50.09787 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55783975-af8e-31b3-8302-30bf0af6ef13 | -3.97063 | -48.08497 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3ec7700-a299-3369-8895-09e3a73f3f1b | -2.33194 | -51.24581 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5fff6716-6220-3452-8d00-1da84a0ab059 | -2.40644 | -53.67942 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dde6b27-74af-3206-abf4-ea0c6b8d9ad8 | -3.50257 | -53.81221 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 887b0cbd-8fbb-36d7-8781-742d834835bf | -2.71118 | -48.67133 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bedecce-e447-3569-b855-e29b4cba1497 | -4.42791 | -48.70678 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 495598f1-650b-35a8-88dc-38da4bed7227 | -4.1195 | -48.51733 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| babda84a-ef68-326b-9dc2-274e1fc67895 | -2.73669 | -54.11085 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6672ccc2-e2dc-33bc-9a40-abece1336c23 | -2.57713 | -48.21207 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 431d7426-9f70-3beb-b549-d46811488b0a | -2.72988 | -48.63892 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2541a936-a397-3261-af0d-277b15e7fded | -3.96506 | -48.07694 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b48c98e2-a6b5-3860-8285-2a5214909053 | -2.58959 | -51.71622 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37a4a4f1-7474-33d0-9dc7-7012b0837585 | -3.24744 | -53.28946 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d2ee30c-4211-3805-94a9-9f2afcd286f5 | -4.2711 | -48.60804 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86c35d60-6019-3b1a-a60e-cc4c69ad7c01 | -2.45913 | -46.55785 | 2024-11-26 04:38:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afae968b-1cc7-32f2-82be-6f5a6e0de923 | -3.38953 | -44.75345 | 2024-11-26 04:38:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c72b4d0-cb70-3e05-ad77-15a1f24c2e79 | -2.5935 | -51.82848 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f163429-79e5-3566-ab59-4a97f2f984e4 | -3.38928 | -50.32436 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5b529c5-3983-3e53-b676-baa5a9fd007a | -2.38597 | -53.7103 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 193d3d78-1d17-3fbb-8710-7a8313edbc16 | -4.1172 | -48.48862 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7af26f5b-558d-3276-9520-511c569166b0 | -3.18882 | -48.43181 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2dcdd7ce-a1da-38e0-8de4-98a4b0474a42 | -3.27718 | -50.01787 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73596381-4c9e-3d04-92f7-303ef79c03be | -3.38756 | -44.17981 | 2024-11-26 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50d7134d-85fa-38ec-8b44-9e8c694f2ec6 | -5.76826 | -47.81498 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c3d9378-a21b-3756-b614-42ba17f638ee | -3.45477 | -50.00176 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37b70f6d-7e33-3329-96b2-6bcd1a0fcc82 | -4.29884 | -48.236 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eac1fddd-6191-3fd6-9607-6ea24a1559fd | -3.68717 | -50.22921 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72feebf7-1bf3-39b3-9e56-b73c56340389 | -3.18387 | -48.44165 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| aa7de187-dc43-3d96-b4e3-c97ce42d748e | -5.50172 | -47.16347 | 2024-11-26 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84bcf8e1-b7be-34a0-a164-8445a2100d1d | -4.31809 | -47.5097 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a2c0e620-d5ca-31b3-924f-afc7b4e3f4f9 | -2.85963 | -51.66085 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 639e9a6f-2d76-3322-b67a-de17e34c72a4 | -5.76542 | -46.30385 | 2024-11-26 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f381e67-1a92-3b45-bc51-3930cdd616bc | -3.93381 | -48.15061 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2ad5631-e01c-34a4-9219-3c4733031475 | -4.32819 | -48.58865 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dc61ae7-03b7-32b3-b2e5-9f8088532948 | -3.97506 | -48.07853 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 3db6d2ec-5b0d-34ec-8e6d-987923067735 | -2.73299 | -54.13397 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f592ce13-a874-3ffc-8455-14a92732cd2d | -3.97833 | -48.05755 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2abd13d2-883a-3245-adb9-200fce62aa93 | -1.99048 | -53.29902 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ecb4a00-0e78-3f94-8ec0-b679b6a9fe8b | -4.23264 | -48.70117 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44415e04-49a3-381d-8f0b-d188894422a7 | -4.54318 | -43.56968 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac9ef030-8c39-3b67-ac89-f252b2d60ee9 | -4.05414 | -48.32924 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2531181-9f74-3698-b048-21cfbd0f1eac | -3.42655 | -49.99746 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da9a8cd8-c260-311a-bbee-7060efe37d01 | -3.50662 | -53.813 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fbb7606f-a7c0-3635-87ac-e2a9f38bf538 | -3.94139 | -48.14107 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2255dbb7-c7ed-350f-a5d4-c5fd42b599fd | -3.26855 | -53.82008 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 633775b0-9845-3100-997d-7f9ceb5e5a8a | -3.27265 | -53.82071 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ffbdb8d-46f8-3e9a-bc58-1c802691f3c4 | -3.26797 | -53.82362 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4488e238-3bf3-34ee-8354-e8246ba94046 | -1.98645 | -53.29837 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 612aa88b-ee1e-3912-96d3-9573f408ed7c | -3.58545 | -50.64886 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71618358-8cd0-3fe1-887f-b928fa4ade74 | -3.94514 | -47.99162 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 099e1a07-819a-3b04-aebd-1959b76dce8b | -3.76243 | -43.25833 | 2024-11-26 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40d693c9-bebf-3182-8369-3b00a8f7aeb9 | -4.75987 | -45.59227 | 2024-11-26 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2171917b-32f4-36dc-9a73-735fdf5b1272 | -3.59998 | -50.38286 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9865e296-e9ce-3b70-9f3f-1abde0470662 | -3.3349 | -53.72077 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd9e3ebc-87c6-3afe-88bf-77d0d6f83c1f | -2.92462 | -51.76828 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e3db966-89ca-3c17-bb9e-ff46409a9e26 | -3.07288 | -50.98924 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a88e5b-ea24-3937-b6c1-73438a28f1ff | -3.96281 | -48.06943 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddf2848e-999c-3b8b-a309-c81ce3cba478 | -4.29605 | -48.23201 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 401e7bfe-c4fd-36db-81c5-77ada9d548e9 | -6.63937 | -47.34752 | 2024-11-26 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 546d2f71-bd7c-3554-aadb-02b01ffe4ec2 | -5.47978 | -51.16781 | 2024-11-26 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5fc4fc2-517d-3985-b92a-2b2ac19c9470 | -3.39221 | -44.1755 | 2024-11-26 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| fbef0327-52d3-3ca6-9e99-d938e8fe3162 | -6.12673 | -46.91357 | 2024-11-26 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b43b4e7-94a4-3957-aadc-86dbf489f039 | -2.86281 | -51.57261 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48998de2-7bd5-3994-83bd-bac3ea45fe42 | -3.22685 | -48.87951 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83f37cf5-c7da-30bf-80c6-af3c116cd02a | -4.36997 | -48.49589 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5934983-d921-3122-9c9a-de1e58958d00 | -3.84478 | -49.96 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 396d022f-997b-39a3-8054-b68c6beec850 | -1.63161 | -53.87203 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2db97cdd-4a33-311e-8260-12b9f01dab8c | -4.1256 | -48.52181 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 608c26cd-6dab-36f6-9ad5-b6e35cd94649 | -3.50603 | -53.81665 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c5e95813-0308-3f99-89cf-6d3715fdad00 | -3.98222 | -48.05456 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c52e2574-9a10-3a00-9a9b-0150a5cda88b | -3.32449 | -49.89348 | 2024-11-26 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ace142a-8ce9-326e-a02a-4a1e8b3f8305 | -5.9485 | -39.66895 | 2024-11-26 04:38:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1431732c-0018-380d-8d71-de1603c053e8 | -3.45815 | -50.00228 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 499897c8-6e72-392a-aa98-3c189e014cea | -3.28581 | -50.75672 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7f7bbed-99fb-356d-a2e1-a2a51d8b44fd | -6.06912 | -48.03342 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8743e02-dd6c-380b-bb71-f7056563b065 | -3.233 | -50.31872 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 969c509a-6596-355c-9e2a-2080524994cc | -4.37938 | -48.1305 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee0d6182-764c-33a0-82fd-0111bb36753f | -3.04604 | -48.50099 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d7c1cb1-d4e2-3363-ba92-fba1dec25dc3 | -3.08959 | -49.21272 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93d6a63c-38f0-36ad-a415-8d773591db20 | -5.06744 | -46.7715 | 2024-11-26 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| ab342679-3dfc-3488-9000-7803a3eb8272 | -4.31303 | -47.51995 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 201f9c4a-ca76-30d2-9694-5cf6e7b780c7 | -4.31697 | -47.51689 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 120aea97-1818-3957-9f5b-c068a86593ee | -3.98118 | -48.08304 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 4ef635ba-4aa7-399f-bd43-4128a5f42e01 | -4.31606 | -48.60092 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 432995be-1841-3292-a83f-76c8e5e14b80 | -3.68774 | -50.22561 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70afbde0-d0b7-36fa-969b-c79c4ba60e58 | -3.07398 | -49.49996 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad3cdaa-19ed-353b-98d3-f49ef74e94d8 | -2.91978 | -48.72143 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84fa97d6-2bcb-3b7f-9e40-b550a65e6107 | -5.94768 | -39.66766 | 2024-11-26 04:38:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 041053ad-67e5-3b75-b43f-7cebbd79d760 | -3.34896 | -50.50984 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31f457e9-069d-303c-bc0d-3ed6852756e3 | -3.41518 | -50.38088 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcb72c9b-6b5a-3b3a-8503-3b3cf042c6ae | -2.45766 | -48.15474 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
