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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94095073-c8fa-3977-a51b-b18ce7daa536 | -14.3348 | -47.6981 | 2025-10-05 14:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 132.3 |
| bb7dbd89-87c4-3e74-be38-5e3753bc113f | -10.158 | -45.4244 | 2025-10-05 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 1e133691-f438-38e6-8c70-3844cd024b7b | -17.9661 | -51.1474 | 2025-10-05 14:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| e1bae726-74f1-307e-91fb-ce95c8428532 | -16.0021 | -50.9238 | 2025-10-05 14:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f8bcda28-5a94-3645-b837-95ab60967ffb | -9.7649 | -47.7345 | 2025-10-05 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 916f41f0-ca79-309b-a06f-2d0e64591cb5 | -10.4054 | -45.3931 | 2025-10-05 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 257.8 |
| f5a7e598-3dc8-3c81-97f8-e46192a4066f | -8.4872 | -45.9087 | 2025-10-05 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 241d2836-556c-33ff-9fe9-0b1008f20d2b | -17.9408 | -57.5928 | 2025-10-05 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| bbd72b2f-afe2-35c5-8934-12da165b6197 | -18.1769 | -53.3669 | 2025-10-05 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 29d85a07-4dc7-38c8-8b42-89393f2a2205 | -8.4353 | -70.13 | 2025-10-05 14:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6472a641-04a8-3672-bc2a-8510176618f1 | -5.9229 | -43.3003 | 2025-10-05 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 932558ac-4b24-3cd7-b8fa-96c1068dc8dc | -5.4777 | -42.7721 | 2025-10-05 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| fa1041c6-bfb0-3fe6-b39e-96624e8724a9 | -13.6398 | -48.6735 | 2025-10-05 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 455753b4-e90c-31c2-88b4-da040b4586c0 | -7.7118 | -46.2754 | 2025-10-05 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 23f3a5c5-c225-31c2-865e-1312eea30860 | -12.2688 | -49.1907 | 2025-10-05 14:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| de7d2f41-4f05-3696-a93b-7341b000646b | -13.6204 | -48.6764 | 2025-10-05 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| c4e94a06-5849-33c8-b73d-f888513bd24d | -7.7933 | -44.1304 | 2025-10-05 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 7fdf287a-6717-383f-b93c-af14f47927e2 | -7.4279 | -46.5016 | 2025-10-05 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 16df89c8-1595-36b5-be3a-52d857082d9c | -6.1538 | -44.6446 | 2025-10-05 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 27b3cf7b-3a47-3de8-a0bb-4b3a380f468d | -6.9871 | -47.4885 | 2025-10-05 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 56d2b85c-bb7f-3b94-9d6c-975599806459 | -7.0372 | -42.7563 | 2025-10-05 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 9d5c1bac-48e1-343e-b349-ccb6667b3b9b | -12.5863 | -54.7679 | 2025-10-05 14:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| b7f84c30-8a95-3a97-b399-9581f6ee9242 | -3.6689 | -41.7495 | 2025-10-05 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| e5df7aab-5ecd-33d2-9d2a-c6b527b85f39 | -18.2569 | -53.3329 | 2025-10-05 14:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 608efe0b-7f39-349d-bd94-6f40044e28cb | -6.2179 | -45.7947 | 2025-10-05 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 57a9a7c8-d649-3e72-94b7-bcf48ba9277c | -7.7306 | -46.2737 | 2025-10-05 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 89798bdf-f922-3030-a50b-4b14a0321343 | -9.931 | -50.911 | 2025-10-05 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 249.7 |
| 5ec387f1-3b19-3208-944f-5f3abc4e7632 | -11.5094 | -54.4619 | 2025-10-05 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 432140bf-355c-3c39-add0-23a58b313f37 | -11.8777 | -56.8769 | 2025-10-05 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 78d02dfc-73ed-388c-9ed3-4d394453a25c | -6.1536 | -44.6675 | 2025-10-05 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 168.0 |
| a92adfac-8a06-335b-a9fb-ceafada86c35 | -10.1943 | -45.5339 | 2025-10-05 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| cf85c6b0-e17c-3b25-944d-6df82f874537 | -15.5824 | -52.4916 | 2025-10-05 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 7e711119-9db7-302e-9ee7-8cc3e0e32e95 | -17.9602 | -57.611 | 2025-10-05 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.1 |
| faec207d-0324-3768-a283-4f6e2fa0b92c | -12.3914 | -51.094 | 2025-10-05 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 609eb5c2-b2fa-35b1-998f-d11fc3d9e511 | -7.4669 | -43.0674 | 2025-10-05 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 95cb70cd-8801-3c09-873f-816891a17cd9 | -7.4672 | -43.0438 | 2025-10-05 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 132.9 |
| be21eb56-a265-3914-ae5f-dd63a0864938 | -9.6287 | -46.6394 | 2025-10-05 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f22d23e1-a366-33f7-a8dc-4a3b553b0591 | -15.2208 | -56.821 | 2025-10-05 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 82718b73-3d78-33a7-b290-fdaeff276299 | -10.386 | -45.4184 | 2025-10-05 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 155.7 |
| a4f29fbc-a490-3ea1-b3cf-6d3647f08a60 | -9.9122 | -50.9127 | 2025-10-05 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 9f7cd441-3df1-34bb-8b72-d9e1b68021c4 | -8.912 | -51.3181 | 2025-10-05 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 98935f35-f7a7-3a45-a2aa-350052ba7699 | -13.728 | -51.3122 | 2025-10-05 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 422.5 |
| e31ed7a0-557a-3adf-92d5-7f8bf7e16a13 | -6.3529 | -41.6292 | 2025-10-05 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 9755b1b9-9ea5-3d9d-b3c2-7ce5bb549073 | -17.9609 | -57.5698 | 2025-10-05 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 8f2f3445-c808-3dff-8986-18462003fb41 | -3.0575 | -44.392 | 2025-10-05 14:30:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 88.1 |
| ed38dc4f-975f-3c53-b613-57ef36cc52ab | -5.9772 | -43.5057 | 2025-10-05 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 066688ab-c6c5-3aee-952c-7854c5f023ce | -11.0911 | -47.7573 | 2025-10-05 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5ea9cca6-479f-3ece-8bfb-db0517f51e3a | -6.2156 | -44.0658 | 2025-10-05 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 3bef23c7-badf-3690-ba4d-5793805e1ce5 | -1.2085 | -49.1051 | 2025-10-05 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 7a21b152-e04d-3edf-b64e-e682b1985299 | -9.9313 | -50.8898 | 2025-10-05 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 1f3bdc15-2f53-3a48-b238-1a6b480901c5 | -8.5596 | -47.6813 | 2025-10-05 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 8ef09bfa-4d72-3db2-9522-d294a6e9b61a | -18.1972 | -53.3423 | 2025-10-05 14:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7a206bbf-ea3a-3883-8ed2-43890b14a4ad | -13.2745 | -47.5933 | 2025-10-05 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 802a7577-d9de-3154-80a1-a6d7d16a5cbb | -7.7938 | -42.5607 | 2025-10-05 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 156.1 |
| 6b2e6293-36b2-372e-bcbf-22d2a827bcab | -7.4279 | -46.5016 | 2025-10-05 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| aa7eab8f-6503-375d-854e-88366de546a7 | -6.9871 | -47.4885 | 2025-10-05 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ed36f5d4-0cc1-3c99-98f2-6ff4052638b3 | -5.4775 | -42.7956 | 2025-10-05 14:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 120.3 |
| 39413b70-c848-33ac-ade3-8d18419743ae | -11.5094 | -54.4619 | 2025-10-05 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 129f97c4-24e4-303f-950e-92c442b583ad | -9.1114 | -44.4029 | 2025-10-05 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8312139c-6d4c-3c24-b1ce-eacc3e79e049 | -10.195 | -45.4882 | 2025-10-05 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d0715dfa-1913-38d4-9283-141f03fff32f | -5.9269 | -42.8783 | 2025-10-05 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| e9de5dbc-b0a2-35f4-a965-eca71ca4fe25 | -10.4557 | -48.3827 | 2025-10-05 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 794c98d5-46a1-3871-a392-69fd21c67144 | -9.5794 | -46.106 | 2025-10-05 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 224.5 |
| afb47494-c938-31bb-8f6e-907284fc9f59 | -12.3157 | -55.1212 | 2025-10-05 14:40:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 15703e7e-5c2b-37ff-bbc2-defed59211c8 | -6.2251 | -45.0264 | 2025-10-05 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1cd1abb2-a426-38ac-83ca-88b440fb13b5 | -5.7917 | -43.2872 | 2025-10-05 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 1c2d040f-482c-3a84-a2dc-a4da3f357de0 | -17.8417 | -57.6254 | 2025-10-05 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 84dfc83e-4391-3f0f-a6c2-c242b435f16f | -12.5297 | -54.7326 | 2025-10-05 14:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| ae9e2193-ff5a-3505-b91e-5f52a2573b68 | -6.2596 | -45.341 | 2025-10-05 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 36dd501b-dd14-3071-ba23-243de8efe430 | -9.0966 | -49.9263 | 2025-10-05 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7509ee44-433a-3f8c-9dc6-270c909afb49 | -6.4076 | -43.6099 | 2025-10-05 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| df2bfa90-9f7c-393e-a930-e20c023b4464 | -8.5598 | -47.6593 | 2025-10-05 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 442732b0-b582-3afb-a68a-14f83c9c31ce | -6.3427 | -46.4556 | 2025-10-05 14:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 92ced877-bff6-3ce7-bebf-2d3656d34697 | -16.0212 | -50.9425 | 2025-10-05 14:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 47754a40-10ff-3d83-a069-39aa71fd054c | -14.5755 | -52.4576 | 2025-10-05 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 68a19770-ab5a-3a24-8bd9-0932c5bda36f | -6.3889 | -43.6115 | 2025-10-05 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 3d44c895-7f16-320f-88c6-59e6dc249d24 | -8.5407 | -47.6831 | 2025-10-05 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 907b8251-6b3c-3251-85e6-5c4301beff46 | -5.9226 | -43.3236 | 2025-10-05 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| b21e7997-c912-3309-b592-04633b29e65c | -17.9602 | -57.611 | 2025-10-05 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 9514525f-6583-3a7a-88d4-451a5083a87b | -6.2594 | -45.3636 | 2025-10-05 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 312aee3c-bc00-32ea-9555-495ed00c0ce9 | -6.2153 | -44.0889 | 2025-10-05 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ff79d37a-530d-3152-90b2-5831173e6756 | -17.9408 | -57.5928 | 2025-10-05 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.2 |
| c657ed85-2d36-3664-908b-fa48bf1fb587 | -5.4742 | -43.1711 | 2025-10-05 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b3c68007-87f6-387c-8d68-686f343ebe32 | -6.2179 | -45.7947 | 2025-10-05 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| a4283530-585e-3e30-81aa-b3e4eef5f617 | -5.9266 | -42.9018 | 2025-10-05 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 841d3084-ce10-3b27-8a91-12792ae5b98e | -5.4554 | -43.1725 | 2025-10-05 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 178e12e6-ab8d-39b3-bb93-5ed536c939ba | -8.5764 | -46.3041 | 2025-10-05 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| bb6bc33c-f7f9-35f1-9632-486328917080 | -7.7182 | -42.5688 | 2025-10-05 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 854c20b8-70b4-3c77-b61b-a86b47d6f210 | -15.9084 | -48.8254 | 2025-10-05 14:40:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 9ee6a356-a044-37a7-a3aa-95a970faca0e | -6.9858 | -42.3109 | 2025-10-05 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 200e42c5-0800-3371-a484-6e16f8cc0b6f | -13.7476 | -51.2883 | 2025-10-05 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 146.5 |
| ccc4161d-f928-3078-bb0f-457f1dc1c019 | -15.582 | -52.5129 | 2025-10-05 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 294.5 |
| efcce85c-e710-394a-adb1-317d1ea1bdbb | -15.5824 | -52.4916 | 2025-10-05 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 9c82b93a-cfab-3f5d-8804-39b1b9f21be9 | -7.6463 | -45.4262 | 2025-10-05 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 088b07d3-45b5-3d2a-8f84-cd9b36dd7d24 | -11.6849 | -45.2872 | 2025-10-05 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 9f777e89-30c2-344f-a101-f6a2992713ef | -7.7931 | -47.3996 | 2025-10-05 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 90e98a80-f972-39f5-9d36-754d481291a9 | -18.1963 | -53.3853 | 2025-10-05 14:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 3a5b7438-5074-3fd4-9fce-5f3ac49c7a8f | -11.8635 | -44.938 | 2025-10-05 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| c82a47d9-9ccd-343a-a76c-5e36433802ea | -8.4148 | -45.6678 | 2025-10-05 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 4b8166da-a427-3a61-9f53-700f25787ea0 | -7.7933 | -47.3776 | 2025-10-05 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |


[Clique aqui para ver as próximas entradas](README169.md)
