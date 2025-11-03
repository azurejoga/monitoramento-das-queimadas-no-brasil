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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9508cfa8-f1da-3e10-bb4f-c08fc065f94d | -3.69605 | -49.22683 | 2025-11-03 04:29:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 277c400d-1034-3e87-9b97-196ed0cad930 | -7.96193 | -39.62494 | 2025-11-03 04:29:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 594f7788-08a7-3e2e-b759-25adef148075 | -5.31714 | -45.33817 | 2025-11-03 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7df5fe22-89ee-3581-a49f-2e35a5db0436 | -9.86203 | -44.15255 | 2025-11-03 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c3d2a1d-5937-3a47-8ca5-b9a75e36596d | -7.96437 | -39.6226 | 2025-11-03 04:29:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6108a295-05ab-3c4f-87af-3bec7aae9819 | -7.17352 | -47.8779 | 2025-11-03 04:29:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d526194-a6d3-38e3-9110-0245c1bd1ec9 | -3.07947 | -51.25044 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c768d481-7665-387b-bd2b-e9a15860413d | -6.84889 | -46.29143 | 2025-11-03 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efefb0db-5042-388d-9a22-645c7fb62722 | -4.70323 | -46.54906 | 2025-11-03 04:29:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35f79310-195f-3ca0-86cf-2ef36e238a78 | -9.9227 | -44.8279 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12066be3-8f10-386d-b0d5-acc4cd1f3671 | -7.12668 | -45.01304 | 2025-11-03 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03d38c52-39cd-3ba8-a243-0eb9053105ea | -9.94533 | -44.84328 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a2fdd30-2371-38fd-b041-2a328c3fb00d | -4.22873 | -45.80712 | 2025-11-03 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6eb8549f-c22f-3a0c-9549-af937c9d819e | -3.66364 | -51.71718 | 2025-11-03 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0cb26f3-eb0d-39d5-a72c-a4bf6d9ebfaa | -9.93489 | -44.84164 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32c78aad-b502-3b2b-a23b-8e8c856e3624 | -6.61808 | -47.72254 | 2025-11-03 04:29:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff040e48-e0ae-3337-bcac-3396cfaf237c | -3.2879 | -50.19849 | 2025-11-03 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 501d2fea-0d78-3850-808f-265f14bb85f8 | -6.6842 | -46.67085 | 2025-11-03 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 005e0642-ff73-3058-8882-2933c15792e9 | -7.9798 | -45.89697 | 2025-11-03 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ded0b9d-1464-374e-9b00-595c307789d8 | -9.85844 | -44.15202 | 2025-11-03 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed657c52-4fa6-32df-a087-163e447e9f65 | -7.56866 | -56.16019 | 2025-11-03 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 751190a9-8b3d-3d58-b925-ab94c735240a | -5.03516 | -43.62053 | 2025-11-03 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 75caf28f-5141-335f-b31e-ac1b01b6da51 | -3.02038 | -51.37018 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 452bdeac-d313-32c6-a861-2d325d563d48 | -9.94475 | -44.84715 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca5be0ae-9275-36f5-b537-60398f8780a9 | -5.03457 | -43.62439 | 2025-11-03 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| fc861f8a-bc7c-3dfb-93b5-8b058165fd8c | -6.84502 | -46.29436 | 2025-11-03 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b40e9e7-cfd1-3ac4-8002-84bc180f0f2f | -4.51683 | -50.79696 | 2025-11-03 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfb8449c-90eb-303d-a2e5-533258852067 | -3.42451 | -51.22535 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e5c9e35-96d6-3ecf-83d7-ef3d0c4b8d7b | -9.92909 | -44.83283 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54b8badc-8337-32d7-af21-877b67b4e6d8 | -4.84353 | -42.92147 | 2025-11-03 04:29:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64379da6-9ae7-3124-8269-2d6d2115c93d | -9.94876 | -44.91475 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22c63e16-d2b3-3de4-b80f-a6a3783fd929 | -5.14163 | -46.15289 | 2025-11-03 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daafa3cf-8a96-3a86-b94b-11068b217088 | -9.17902 | -43.02236 | 2025-11-03 04:29:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2851927f-4c05-345a-9e02-df355f6673d1 | -3.38901 | -54.27882 | 2025-11-03 04:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 987689a5-acb2-332f-834d-daf5edc08454 | -9.91922 | -44.82737 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ac3921a-17f1-3398-bc5d-97ba296c2081 | -9.09469 | -44.32391 | 2025-11-03 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18376306-9cf0-3c1b-8511-5ff827251e55 | -9.94009 | -44.90163 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26a094b4-df4b-3bd9-9996-0aa2bfc76b29 | -5.40093 | -46.05188 | 2025-11-03 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d12832a-3a87-3fbf-bb8e-e376c61e5159 | -3.98873 | -47.30128 | 2025-11-03 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baf0f057-5079-3e6d-8255-57cf33ccf250 | -8.59774 | -44.16059 | 2025-11-03 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 87f29423-4def-3789-970e-2bb4729abfa2 | -4.65527 | -42.51819 | 2025-11-03 04:29:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 314928bd-fc06-3fb2-b157-dac501939029 | -9.85188 | -44.14688 | 2025-11-03 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc10989f-e6e5-3bf9-b90b-22f54372ec0a | -10.03757 | -42.28099 | 2025-11-03 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e5f2345-738a-3165-86bf-f55c11c392cc | -4.21586 | -44.22898 | 2025-11-03 04:29:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7115a4ee-1228-3de9-a2d7-fc2e52e53f04 | -8.59482 | -44.15606 | 2025-11-03 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba139fce-7478-344d-8c1c-b09218b77500 | -3.01677 | -51.36554 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ee055a3-cdbb-394f-a8b0-4ae68c15989a | -7.23657 | -45.06726 | 2025-11-03 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30100ee0-a91e-3edd-a284-132025d16fd1 | -4.50875 | -50.1945 | 2025-11-03 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5451c984-35f6-3fa4-85cc-cba21282e0d4 | -3.89335 | -52.31186 | 2025-11-03 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec7cc6ef-43b1-3236-ae68-64724de90512 | -4.0782 | -50.35878 | 2025-11-03 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a149a35-efa9-3cd1-84b7-7d92b2afdc64 | -4.70207 | -46.44903 | 2025-11-03 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8320ad1f-484f-376e-9fac-7500641148ac | -4.25874 | -50.67319 | 2025-11-03 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e09fb68e-eaf4-374e-8520-4f796e5d34fb | -4.51676 | -50.7937 | 2025-11-03 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bdc23fb-de38-39fa-b2a3-9bad8348bda0 | -6.70811 | -40.83339 | 2025-11-03 04:29:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ee7f971-6d1c-35a5-9675-ea2ae1bc804b | -5.03866 | -43.62108 | 2025-11-03 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d5a0d31b-3f9e-39ff-bee5-66257bc473b3 | -6.04247 | -46.49088 | 2025-11-03 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32b8b8ab-5ca7-3136-ba95-7d9afbe20c70 | -5.43076 | -46.35808 | 2025-11-03 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f508dd00-4bd4-3da7-9ba3-0498a42161ee | -7.56882 | -56.16003 | 2025-11-03 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f54790e-13d8-366e-a564-4c5cc7e978c0 | -8.43574 | -45.61559 | 2025-11-03 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89e9c811-3b5c-33e9-885d-2406793e2885 | -6.40715 | -44.51892 | 2025-11-03 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 981237f2-f96c-35e8-9364-aafba2ca5bce | -7.05274 | -39.47193 | 2025-11-03 04:29:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 917e778e-8f7c-3394-a8db-a448468734c3 | -3.29103 | -50.20416 | 2025-11-03 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bb8e502-823f-3326-bfef-e8ad7050fbd0 | -6.42243 | -47.33292 | 2025-11-03 04:29:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a459d0a4-2af0-31f2-905d-9a50d7c506f3 | -5.03108 | -43.62383 | 2025-11-03 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1774fc3f-323e-325a-9d61-46b8d03175e3 | -9.86264 | -44.14846 | 2025-11-03 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c01f81c-a58b-36f8-936f-ce8bee4768c6 | -8.59421 | -44.16005 | 2025-11-03 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3af8aa35-bd9f-381e-bd3a-c58b8729d866 | -7.08595 | -44.98468 | 2025-11-03 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab71b37d-336f-3a64-a8f6-7245adf09cbd | -4.70485 | -46.45303 | 2025-11-03 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 18cba457-1d17-3263-9d06-9d7b707efdbc | -5.71778 | -42.18917 | 2025-11-03 04:29:00 | NPP-375D | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e52ee3f0-2e66-35c4-b1b8-40cc3c1680e0 | -3.22152 | -50.58548 | 2025-11-03 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67351db5-8b1b-34a4-b619-de35f05bfcb4 | -5.60395 | -46.43908 | 2025-11-03 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ce00e5e-69e5-35e3-a12e-f427f573891f | -3.24052 | -50.79698 | 2025-11-03 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bef923bd-55d7-36cf-8956-2ea44161d46d | -5.0399 | -43.6205 | 2025-11-03 04:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d633ae28-0e58-3888-a6c8-c8414513687b | -10.42561 | -44.94912 | 2025-11-03 04:31:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2b03b900-4d9a-36e6-bf74-03ed09c7866f | -14.8748 | -43.55703 | 2025-11-03 04:31:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81cbf280-e35a-3b17-b6c5-0d59d3c0238e | -10.406 | -44.3576 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5b3ef6f-f9e8-3798-90f5-4d8ca53654bc | -10.41024 | -44.31393 | 2025-11-03 04:31:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9953d194-e2f9-38e3-b0e1-713e4b148d58 | -13.61826 | -45.30537 | 2025-11-03 04:31:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23422051-329a-3e67-9c04-27d00e746668 | -13.73258 | -44.22757 | 2025-11-03 04:31:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f23ec1ac-92ef-3430-b938-67e40d06e0b7 | -12.77536 | -43.47696 | 2025-11-03 04:31:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 519cc8fe-3bda-349e-93e6-f1224c656ef1 | -12.64246 | -41.0117 | 2025-11-03 04:31:00 | NPP-375D | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e317220f-225d-3938-8bc5-88b669da4fdc | -13.63534 | -45.33693 | 2025-11-03 04:31:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ad45b0e-c4b9-3450-8ceb-719d79554757 | -12.39896 | -46.63319 | 2025-11-03 04:31:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39d1dcb5-ba6e-34cd-9b76-085f9b4ba9f6 | -10.61889 | -44.6726 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1c7bc6c-942c-39dd-b755-6cb79d8d39bf | -10.40411 | -44.35452 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e49b97b-2aac-39fd-bb17-ecaf025e7008 | -11.5158 | -45.00343 | 2025-11-03 04:31:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6f3a37e-fadc-39e8-a9e6-41f7dc916900 | -10.40643 | -44.36326 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f98366f-3ac7-3176-b51c-7e6a237de846 | -10.84459 | -56.9611 | 2025-11-03 04:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acbf4890-e92c-3bab-9208-efa305be28c6 | -13.30638 | -41.91998 | 2025-11-03 04:31:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 1ce38df3-7faf-3048-a1be-95fc1660a2b2 | -13.61454 | -45.31049 | 2025-11-03 04:31:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d8d2461-fb18-35bc-9692-3e1791645d7b | -10.76356 | -46.29678 | 2025-11-03 04:31:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 183bf0ce-5f3f-3e27-a107-da8d05b44a14 | -12.68459 | -41.56658 | 2025-11-03 04:31:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2adbd90e-ad76-3230-96e4-132def353eb6 | -12.77151 | -43.47639 | 2025-11-03 04:31:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b29d6e56-c2ff-34f1-ad97-b411778a0627 | -12.68403 | -41.57078 | 2025-11-03 04:31:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 6af9b3b9-8336-3197-b665-f999e695bb12 | -10.64119 | -44.69235 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 851be1c8-2c81-3fe5-b6e2-946aa507a9dc | -12.05319 | -43.54729 | 2025-11-03 04:31:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c96c4626-acf2-3b44-99fb-bddee0dab600 | -10.62242 | -44.67316 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bef8e55-2d92-3ca9-96a3-aca8629931ec | -11.4168 | -44.67865 | 2025-11-03 04:31:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55874a26-58b0-3a2d-abb4-afc002a29126 | -10.85433 | -44.73491 | 2025-11-03 04:31:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b13affba-60a2-3bbd-873e-d6bce9acf98d | -11.66888 | -41.68816 | 2025-11-03 04:31:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README8.md)
