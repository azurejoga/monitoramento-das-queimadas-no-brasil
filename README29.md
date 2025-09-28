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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cec1eb5c-5f71-3032-9f8d-1b69e6a2f1b0 | -5.77487 | -42.88394 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7f747d72-1cc2-3413-8ca6-a4cef330180a | -3.33557 | -50.25114 | 2025-09-28 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3841d7d3-6c23-3bd9-b4ff-418f7d978dde | -5.82336 | -44.44299 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7d30df7a-e5a1-37a3-9b1c-212ef349c0cb | -5.829 | -44.44206 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 412d27e8-42c7-3391-a95a-d04d6aff5849 | -5.73696 | -42.65552 | 2025-09-28 04:04:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 94a4c42e-2b20-3406-8264-657d4dbe244b | -6.64751 | -39.50124 | 2025-09-28 04:04:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dfdca247-549f-3efc-b484-d9a0d289d4c5 | -3.87271 | -48.04334 | 2025-09-28 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c266a9e-9cb3-33af-b248-e1dd6d054c0b | -7.2801 | -45.81245 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b68eb51-ab6d-3c0d-ad25-ede33273e5f3 | -8.63878 | -44.00306 | 2025-09-28 04:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13753d27-576c-3b5d-88ac-6963f43a6efe | -6.76032 | -44.59112 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b75640c2-476b-3818-8a8c-0f8cc57b0ba8 | -8.71336 | -50.05064 | 2025-09-28 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e36cf2d6-4ffc-3029-bcfe-a6686ea91bfc | -5.82587 | -44.43643 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad11a076-3550-3991-b2bf-285fcd238ff6 | -7.25146 | -43.00863 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fddc858e-4969-38f3-9467-0f5465a82709 | -2.47781 | -47.65733 | 2025-09-28 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9b177ae-d254-37d0-9f53-87836b2d26fe | -7.54437 | -47.1454 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b883b1c8-d5b2-3377-8de6-009e66b3c9c2 | -6.76997 | -41.75531 | 2025-09-28 04:04:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 813c2a7e-68a7-35e6-9a1b-1c660f1f2ed3 | -3.33513 | -50.24971 | 2025-09-28 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e0201c1-0f8a-3711-bae4-a7190f40442f | -5.85423 | -42.57916 | 2025-09-28 04:04:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0c25a1a8-ec7d-3682-9039-5bedfc59433c | -5.04744 | -42.90372 | 2025-09-28 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ea26e4e-2c46-36c4-acaf-1f76ced7b8f5 | -5.77127 | -42.88333 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 63098045-672c-3601-b8e8-df23a34eaa2b | -5.86923 | -45.74986 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c3d0dd4-7a50-3bfc-b5fe-d4795ba51a6f | -7.16698 | -41.71708 | 2025-09-28 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 36a2aa60-d249-3b66-b0c6-4fee88388110 | -6.05545 | -43.77876 | 2025-09-28 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0cda20d9-c4dc-3db5-8ee6-d4f926520088 | -5.74499 | -42.83326 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9af570d2-d00a-3002-b5e1-15749e5f0d39 | -7.92815 | -42.67123 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c4c0729-ae57-3bc6-9718-11707eb72987 | -6.4363 | -43.50946 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df08d759-2672-3de1-b818-b7165067f0df | -6.31376 | -43.45989 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2d91864c-27f5-3294-98cc-b24275843fc9 | -5.72858 | -42.8433 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7b52b6af-79a8-3783-a764-e768fbeaf844 | -5.41494 | -42.28389 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 410cf35d-2a6b-3b77-8839-bf9a9462959f | -6.14508 | -45.72319 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aed8b648-8a3a-3aac-a4b6-0ab98ec7efb8 | -5.25376 | -46.17502 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bd27384-9526-38a8-bb6a-9843919338b2 | -7.17897 | -41.70771 | 2025-09-28 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c5de56d-5061-3d08-955a-dc6b9a6ff149 | -3.80652 | -41.56934 | 2025-09-28 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| df032dc1-1bb0-39d4-99ab-25f6ff797844 | -9.28555 | -45.70538 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 648f6be8-0b43-311d-aa29-dda2c42033f6 | -6.14226 | -45.72301 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8891885-d334-3719-b602-30d09c67b8ae | -6.0562 | -43.77426 | 2025-09-28 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 726760c6-e575-3ced-9d48-5707846e8529 | -9.07311 | -45.53524 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ebc655e-cb39-3ab3-b924-86413164ee1f | -5.75938 | -42.83576 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| ab6db16e-8652-30a5-b1d8-d8801d944df3 | -7.23215 | -44.76397 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6dacedcd-e86a-3343-bbd4-f66bd0190fcc | -9.78158 | -47.76169 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a6304b3-bb8f-3158-a915-ebc4e4ca0e90 | -6.40134 | -43.52824 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da20d970-11d0-3176-ba06-20e60bc48f82 | -7.44767 | -43.17632 | 2025-09-28 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 45566a68-4cb0-3a9c-bb21-786f1e16de3e | -8.26877 | -45.47025 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a89610a-e1ab-3758-812f-64e68bbbf7c7 | -5.75579 | -42.83512 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c7e5ac48-122a-354c-b9bc-0baa7602f61a | -6.28943 | -39.82327 | 2025-09-28 04:04:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9d0154c9-5f1e-3c7b-9ba0-1564c7a987c3 | -6.42372 | -43.51651 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ae132d32-6eb5-34e7-a1c6-fa834ea1426f | -5.99664 | -43.92699 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0e01a7f-1dc9-301c-a0ec-2c4e06bd6d2d | -5.73084 | -42.85219 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| dc634b47-7740-3b36-9b74-4bafb3d43f35 | -6.31891 | -43.45181 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5fff9480-7f2e-3aa5-8395-91cdfe1188ed | -5.60069 | -43.37329 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| fdac87ca-a479-373e-8d46-967c75b1323c | -5.90195 | -43.28748 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 04eadf32-2df2-3c32-9a5d-b22ef4135ed5 | -7.30501 | -42.95071 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd34b253-8e9e-3ed4-bc80-e0d11793acd1 | -9.29113 | -45.6947 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae2bba1d-5c0b-3104-8a85-64e05987fc3a | -5.68847 | -42.6604 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bf610913-215f-3b5e-9180-ffa50a192257 | -6.15759 | -42.79902 | 2025-09-28 04:04:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d9d1fffa-9ad0-3b38-83f4-222443670f95 | -8.48531 | -47.81052 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6bac933-99b7-38bb-a18b-ba3a23be128e | -8.29107 | -45.43747 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71c29eaa-441c-3b36-9157-5644e2b0bc75 | -5.97982 | -44.12729 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 384e255c-22ad-32df-ba58-4802b5624314 | -3.80517 | -47.58964 | 2025-09-28 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2eccdc21-283a-39db-8329-4e85611f855a | -9.65655 | -43.85598 | 2025-09-28 04:04:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e4a6cb1b-8f59-33d0-8a7a-ff286a3dffb0 | -7.23132 | -44.76895 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd7d8b02-9f90-3bda-b23d-ad7f59c05d76 | -5.45077 | -46.61878 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 010556d7-9799-379c-baa3-afe7005d218a | -5.48804 | -45.1094 | 2025-09-28 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15a524b6-3be7-3284-8f8f-7de2a5a5f593 | -6.5791 | -43.74094 | 2025-09-28 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1e4777ce-a59a-3759-9209-2a31ff68be7d | -2.58161 | -48.40926 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a3815cd0-6435-319b-b43c-c0f6ea23cd86 | -7.18636 | -41.70517 | 2025-09-28 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c7197904-d89a-3950-a3f0-24b17d861d8f | -5.73451 | -46.17939 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76887ca4-6b61-39df-a9e9-763128b9ebc8 | -9.28456 | -45.70837 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f348e5b-00d7-3680-a8a5-82bb089d7cbd | -7.79564 | -46.99797 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9b20d068-e126-3414-b87b-fe852473fa27 | -6.78117 | -44.08215 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ce3a9e48-0206-3a33-9766-1eef889a090e | -4.29093 | -48.26572 | 2025-09-28 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8e7ff04d-1096-32bb-9f6d-24788759220d | -5.78368 | -42.89803 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 606f2d62-3c6f-3a2f-bd3c-c96a55efdf55 | -6.07017 | -42.44908 | 2025-09-28 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f1b67a5e-55aa-301a-872c-0df48b42a322 | -8.68361 | -47.0703 | 2025-09-28 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e98dab68-6fd9-39c5-920c-800ba5b9286d | -5.6878 | -42.66443 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d784bf22-b0f1-39d2-ad6e-b486a535013f | -5.73872 | -42.84925 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 44d672da-207c-3517-85d1-2e885f643972 | -7.75016 | -46.98827 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c19fe4f6-1708-3ffc-bd92-fb6620d62c90 | -8.19993 | -44.4018 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dc1dff3-0b4a-367a-b850-7a617cecf34d | -6.27241 | -42.4923 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07cb0d82-841a-3d51-8238-66aa79b26d64 | -6.48633 | -44.23787 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd65c003-4fca-3741-ab8f-52c42dda2d28 | -7.34264 | -45.49256 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0277879e-fc4d-3fc0-889d-1015985a2dfa | -8.43849 | -46.87017 | 2025-09-28 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4687219-45f3-3a60-a541-b3ca115b579e | -5.78306 | -42.83429 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 11bd0891-8c47-3f7c-b6fa-91dc75070eb7 | -7.2535 | -42.99639 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c256422a-484d-3336-9a96-ddbdbcc47dd6 | -7.85673 | -43.79571 | 2025-09-28 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 59443cc6-1b8c-3993-84a2-960402d19f1f | -5.74232 | -42.84989 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| d83d1be0-e960-3808-a759-8a4a682ee324 | -7.80761 | -47.00948 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cfa8feb2-0fd9-3648-8dd4-26fd0b7efb18 | -8.28681 | -45.46235 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f11a65f-6034-3af5-b4c1-5bcdb3605648 | -6.79718 | -46.19162 | 2025-09-28 04:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aee36a9-d321-34b5-9115-e3ebe347aa7b | -5.75419 | -42.82207 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3a7646d6-0a4f-381f-b360-3974cf74e4b1 | -5.37229 | -42.30217 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 999b17c2-9db7-318c-b823-56e1af466018 | -3.79039 | -48.86536 | 2025-09-28 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18afcd36-ba9f-3073-a81f-147166c8b0ee | -5.7391 | -43.37646 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cd9c4bad-114d-3d24-ae89-437632caea52 | -3.80205 | -41.56541 | 2025-09-28 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 458b755f-7327-3f4c-8ea6-18a974c8bf64 | -6.1269 | -43.44178 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d01865b-2bd6-3836-91de-f9e4adb21564 | -8.82939 | -46.00443 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed49eb9f-171d-3a67-a420-fe97193988e0 | -8.91715 | -46.09821 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2d16139-6ab9-3604-bdd0-00563d8183cc | -7.03441 | -44.7736 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2adb9567-92b9-3cbd-ba2c-8a9787f1fef0 | -8.8283 | -46.2097 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cbc335c-1112-3844-93f0-d2cd6c12318a | -6.07081 | -42.44516 | 2025-09-28 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README30.md)
