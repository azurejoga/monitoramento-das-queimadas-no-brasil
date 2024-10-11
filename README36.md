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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04454884-79e5-35d2-b3f9-a1e1fe7cf724 | -9.25196 | -43.53666 | 2024-10-11 04:00:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e2949182-5b53-34f1-bf4a-cb7f8b86479a | -9.24391 | -43.05976 | 2024-10-11 04:00:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 054f73fe-eab5-3bf1-9b23-83f532419802 | -8.93799 | -42.58944 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8cfdbeb4-d19b-379e-a431-1bbf1ae33a11 | -8.93736 | -42.59328 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d7b5c35-e509-3e7d-a08c-f86f04abb10f | -8.93389 | -42.59269 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7e3451f3-45fb-3fb2-8530-9b27f106d7cf | -9.5258 | -42.9902 | 2024-10-11 04:00:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb764c17-7f08-31d3-8caa-92f8bbbb2c5e | -9.52515 | -42.99414 | 2024-10-11 04:00:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 04419e92-3f45-3dde-819c-43c3e779edf2 | -2.97822 | -52.9028 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 183be231-db74-3081-8b85-17d6a969a3d8 | -2.9771 | -52.90952 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ca436b7c-7cfd-3670-8708-aa731e4acbf1 | -2.97591 | -52.91658 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 11f8f326-e2af-3a08-bede-6318eb0e5548 | -2.9741 | -52.89746 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 3d5f2195-9709-3eb9-8db7-57abb87f551d | -2.97293 | -52.90414 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 2ebdcac8-8917-35fd-b9da-3753e004f9fa | -2.97174 | -52.91094 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| c749fc02-cd92-3f8b-b4d3-07557d60ca01 | -2.97107 | -52.90137 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 271911d1-2fb9-3561-a87b-1b5a3a6f8b6e | -2.96993 | -52.90811 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b660ab6a-baee-37fb-a4d1-d6bce4318095 | -2.96877 | -52.91504 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| da7556c1-39ba-33ce-af7f-69ca5400182c | -2.96579 | -52.90261 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cc13b741-c31a-363f-bda5-8a7c9b1b0d23 | -2.96463 | -52.90923 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 14a4c68c-0ef4-38b7-ab5b-735cb92c16dc | -2.96393 | -52.89976 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| faa89598-0555-3a2f-bd58-e1a9a60afdbd | -2.96341 | -52.91618 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 150bad3f-e9bf-3bdd-9697-8e703638a846 | -2.96281 | -52.90642 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| beef29f1-0d06-3fe6-848d-eea1bfb7eada | -2.96167 | -52.91316 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 7691445e-5cc0-3a7d-9c62-421c267d77f2 | -2.95862 | -52.90128 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 02e7aa25-6f7b-320c-b3bc-2fc86da5ba4b | -2.95744 | -52.90797 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1b3ba9bc-8da4-3f54-b85e-1ec571a84e75 | -2.85116 | -52.90917 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 264c99f6-7de3-301e-a534-c2fb00403a51 | -2.8496 | -52.91096 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95f54d65-8e87-3ad2-98ce-ced2d000188f | -2.84629 | -52.93701 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d44c5709-c5a7-3531-95c9-27ae451a6647 | -2.84493 | -52.94481 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a6ed31d-fa6d-3bab-a5fa-c793e58c2008 | -2.84395 | -52.90799 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a43ec717-d575-35ac-a2f7-b57d5a17d7b3 | -2.84241 | -52.90961 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbcb7fbb-e671-33cc-b660-bca64e3884de | -2.78527 | -52.49091 | 2024-10-11 04:00:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e1e90ed9-5360-3c73-8cb5-31c8acc986b7 | -2.7839 | -52.48378 | 2024-10-11 04:00:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7addf9c9-5a01-3c66-89fa-72c4306a526a | -2.78271 | -52.49051 | 2024-10-11 04:00:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8bc239c9-82c6-3d55-b5f2-aa967a87e677 | -2.77939 | -52.48282 | 2024-10-11 04:00:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 233509b0-e125-3c84-84c2-60b395b5cf23 | -2.77825 | -52.48954 | 2024-10-11 04:00:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f7239aec-56f0-3bdd-956d-9bd03f48d579 | -2.77687 | -52.48253 | 2024-10-11 04:00:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3d4ea161-de98-36bc-9a3d-d857d683a840 | -2.77568 | -52.48923 | 2024-10-11 04:00:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| caf267f4-64c9-3a86-9524-eac1dd19e46c | -2.77236 | -52.48161 | 2024-10-11 04:00:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a84d071b-d0da-38e0-b2a6-fb3793c8e20b | -3.32548 | -53.00739 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81a3892c-5185-36d8-b235-fc93fae09f76 | -4.73787 | -43.70306 | 2024-10-11 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07fbd580-54cd-3e12-94c8-ea1a1087a7b7 | -3.78817 | -43.11221 | 2024-10-11 04:00:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0d3a37f-1bac-3fb6-b52f-17fe2bdf82c6 | -4.04178 | -44.26676 | 2024-10-11 04:00:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80e5b92f-f297-36b8-aa86-dbeae1a17cc1 | -4.04121 | -44.27031 | 2024-10-11 04:00:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18f2cde5-e675-3d58-bb0d-08af3569ea11 | -4.03773 | -44.26616 | 2024-10-11 04:00:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f23cd5b-2d73-3380-8cb4-a44038124f68 | -3.80317 | -44.05096 | 2024-10-11 04:00:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8c25b4d8-420d-3029-ad9e-cc127703f9c5 | -3.80245 | -44.05527 | 2024-10-11 04:00:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 44a95ab2-9ab2-34ef-aa6b-aec4a9ae545b | -3.79916 | -44.05031 | 2024-10-11 04:00:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb884796-55e0-3bcd-a248-fe161cca4769 | -3.79845 | -44.05463 | 2024-10-11 04:00:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8c26ccc-868e-3a43-81b5-d22f5f0b160c | -3.79787 | -44.05808 | 2024-10-11 04:00:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f84a926-17a9-30ba-97f1-bc97172d4570 | -3.6659 | -44.40474 | 2024-10-11 04:00:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0961e7f1-7c09-3a30-b28f-f557c8c0011e | -6.45649 | -44.37543 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36c7a3a6-20bd-3e58-a507-41c9e456e261 | -6.45256 | -44.37477 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54d5179c-d013-3331-9b36-2bd449d4ba19 | -6.45172 | -44.37972 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ec9bdc5a-9116-38a7-be68-94fda767d017 | -6.44769 | -44.26101 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 890a3f44-7ac5-3021-a47d-99650ee72d1c | -6.44743 | -44.26428 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ac2904c3-5c84-3d34-b2eb-4f24cc535204 | -6.44686 | -44.26587 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1a3af8f-e678-3893-8dfa-26e19827c2ef | -6.44662 | -44.26922 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 53e04b40-22d8-3695-a315-a240f72d0997 | -6.44602 | -44.27081 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ddaaa651-daa6-3260-a367-db0a81725925 | -6.44579 | -44.27433 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f5beabea-9e85-3b43-ae49-01897c8637a5 | -6.44513 | -44.27602 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 77f17f57-5cb7-32e7-9437-9c913893e655 | -6.44494 | -44.27956 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 286299b2-6415-3fba-8b7f-413c830fef04 | -6.39887 | -44.36414 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99355d2b-94bd-3f56-99ba-3bedca61c534 | -6.39494 | -44.36349 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6690523-bc1e-348a-b79c-a68ef0cdd580 | -6.2687 | -44.18099 | 2024-10-11 04:00:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3261180-fb6e-3ce3-88ea-bb57bfff6ffc | -6.264 | -44.18513 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 980df715-82d4-3cd4-9d05-fc301d95b0d4 | -6.25574 | -44.8015 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e2603d4-2611-3514-89fa-c9131092a34e | -6.25565 | -44.80088 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f43eb75-dffa-3c6f-9df9-a0fdd8d56615 | -6.23474 | -44.19367 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11e7b853-8858-3b9b-b36e-5e752c09193c | -6.19806 | -44.19749 | 2024-10-11 04:00:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18975e0e-daeb-30a9-8ec1-59886aeb97d4 | -6.19416 | -44.19688 | 2024-10-11 04:00:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 770687d8-6080-35e8-9f30-d4a806dde35b | -6.08607 | -44.84678 | 2024-10-11 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6995b989-03ee-3ab0-95a2-0ed5ca0478f6 | -6.07092 | -44.64045 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6b1db7c9-851d-353d-a5cf-2f04ccb43d3f | -6.07031 | -44.64402 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 84cfa2a2-c52c-33eb-9f6e-592e7c8c49c9 | -6.07001 | -44.64021 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cbfdf15c-e967-3a91-b28f-9825b80842c8 | -6.06943 | -44.64378 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3041cd8a-0942-3424-9d3f-54cf5feb3ad8 | -6.06691 | -44.63975 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b8d555d9-1327-35be-8a70-b83216a64261 | -6.0663 | -44.64331 | 2024-10-11 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fc65302d-9eca-35b0-bdf6-45b47b6d255b | -5.96955 | -44.12614 | 2024-10-11 04:00:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2e8e486-420e-3e06-8211-38a9dac0ffa1 | -5.81563 | -44.13661 | 2024-10-11 04:00:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14ca6c1b-b84d-3e52-82f4-3644c6d4a166 | -5.81411 | -44.12125 | 2024-10-11 04:00:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e276bf26-b955-319d-8675-a447e799c699 | -5.8102 | -44.12064 | 2024-10-11 04:00:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9e5e36e-6e7f-3f9b-a4aa-85a9a1836312 | -5.74587 | -44.02255 | 2024-10-11 04:00:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f5d09df-e363-3b23-956b-1e00dfda7eb3 | -5.74276 | -44.33471 | 2024-10-11 04:00:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 449fd752-22d3-302c-a1ce-ce4a9652e4ec | -5.7388 | -44.33406 | 2024-10-11 04:00:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 17f49ab9-18da-3436-b295-ac8ec00dab3d | -5.68495 | -44.38785 | 2024-10-11 04:00:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f6909c99-b5aa-3d59-b010-db74698723e4 | -5.63426 | -44.06908 | 2024-10-11 04:00:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c03c831c-8651-3e28-b1af-46ff2fb7b495 | -5.57994 | -44.10892 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6390a9ea-0e7c-39d6-bedf-5affa656457c | -5.57129 | -44.11261 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68bc50f4-45c9-3924-bb4c-cd5f3b8555f2 | -5.57048 | -44.11752 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5407ebc5-fba4-3114-b3c5-96656e1d4f5f | -5.28479 | -44.20278 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86c3ad5b-1237-3bb3-be2f-5963853d886b | -5.28313 | -44.2045 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c5316c8c-1c37-30d9-848a-cd8c3a491f1e | -5.28227 | -44.20959 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9714f26f-80a5-3682-a4b4-3e9922baa227 | -5.28083 | -44.20214 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b346c01-ca28-34f3-a656-b6f5444f557a | -5.28001 | -44.20723 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d59a92a7-1a5d-3eea-bdb5-16f427739f1a | -5.2792 | -44.21232 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d3c78fe4-0e8a-3181-be15-88901a8d1b46 | -5.27917 | -44.20387 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75ae70c4-ebd2-387e-bb82-96bfcf499071 | -5.27831 | -44.20895 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 551ebbd3-3073-3713-8fe4-5c6af5de565d | -5.27688 | -44.20148 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5cef2123-50e0-3532-97f1-5c525bf204b2 | -5.27606 | -44.20658 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba72537d-0d69-3c4f-8f04-12116d5381fc | -5.27521 | -44.20322 | 2024-10-11 04:00:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README37.md)
