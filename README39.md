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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fda3994-e4d3-3c9b-a19b-eda6ddc3dabb | -7.92357 | -45.89478 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c73ae6b4-76e5-3151-aca1-a169f37aa589 | -7.29161 | -44.52526 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e52517ba-3a0b-351d-b209-77ad16ece430 | -5.79907 | -59.22146 | 2025-08-25 04:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56898c6a-87da-38fc-a106-24e5066d9db5 | -7.90926 | -45.88797 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 267da4f8-bea0-3d33-9701-cb4147570880 | -7.67696 | -45.40219 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c63a23ad-38dc-321f-a894-5e826f22d39e | -6.89148 | -47.92967 | 2025-08-25 04:40:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 531e2e73-408e-3e61-8d6d-ee817b62623d | -6.12997 | -44.37458 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 659f27be-0dfd-31c0-930b-ce71a68a0762 | -7.53981 | -45.22039 | 2025-08-25 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c80c6417-6484-3e19-97e7-c3878655103a | -6.75319 | -44.81772 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a014c915-0630-3dd9-a21b-8008b9837dd9 | -3.60007 | -47.5253 | 2025-08-25 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d066138-4eb4-3fb7-89a7-af057aa7c670 | -7.9174 | -45.88467 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b19f0cd6-77b5-359f-abf9-9dc3a6ae607b | -6.80355 | -44.99147 | 2025-08-25 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee9afd98-c508-3329-b3b2-ebc05d12ab8e | -5.55648 | -45.56625 | 2025-08-25 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14b93d39-eaef-3087-a7c3-83a3f9676224 | -7.58439 | -45.24353 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2872c72-5080-3ac7-a73d-94ff19dbc160 | -5.55278 | -45.56569 | 2025-08-25 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f6b5d2b-45d6-3c48-a39d-5e155f6d9b6f | -6.1846 | -44.12029 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| feb6b172-0f82-3b15-bf65-29d446ffc717 | -7.28782 | -44.46669 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec65fdf3-5193-3e0a-800b-840720284754 | -6.7932 | -44.31453 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8e78d68-1689-308c-9901-71a91a503fd9 | -7.25864 | -43.66093 | 2025-08-25 04:40:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f357f8de-2059-30f2-8fff-5ca27f1c4365 | -7.53343 | -50.53252 | 2025-08-25 04:40:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f17ace3-3518-35a4-9c57-5cd230d9a558 | -3.79647 | -51.18604 | 2025-08-25 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c9eb333-1dc5-3d46-b176-966ae044ffd1 | -6.5282 | -44.42757 | 2025-08-25 04:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f323ebd2-c133-39d2-8ca8-0577e8297b1b | -8.16955 | -45.06326 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c00b8ff-7f27-3862-80bd-fb9d56439834 | -5.53147 | -41.2892 | 2025-08-25 04:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4241bcdf-afcf-3801-a85a-5de9820a857c | -7.14322 | -44.15752 | 2025-08-25 04:40:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a292644-8f8c-30a2-90f6-36d6e2072ca9 | -5.41443 | -60.17192 | 2025-08-25 04:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d701d9cd-34e6-36c3-bf74-99ba91364ab3 | -7.53457 | -50.52543 | 2025-08-25 04:40:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef5aa448-2009-3c48-8c26-76c9e587c29a | -3.93501 | -55.75408 | 2025-08-25 04:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c11f93c-e331-3113-b05a-e3c990f3800d | -7.93764 | -45.9289 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6104589c-12dd-3b19-a09e-08943264abd4 | -7.5967 | -46.2458 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 685b37be-bdd8-301a-ad30-c74bcc4f0403 | -5.52023 | -52.00126 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0f710b2-c250-355e-9342-9ce2c95af4cf | -3.93421 | -55.75876 | 2025-08-25 04:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a3ac0e6-f34d-37e9-8848-bd79a117faa6 | -6.03267 | -43.99368 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ad32ce1-0053-32f0-9d66-dec6958e929d | -7.09128 | -44.62844 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49f493cf-fb35-37a4-8341-911eb4339403 | -6.05241 | -44.44362 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4def639-02fe-3733-b448-2654bc95baeb | -7.30193 | -43.66359 | 2025-08-25 04:40:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 62e0f11a-8f95-3c43-ace1-254f3606cadc | -6.45152 | -44.61768 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cb6a2678-5d04-3790-9197-ee97facc937b | -4.28852 | -48.26458 | 2025-08-25 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65e9c34d-cf06-373f-a376-5b14726a66b7 | -2.2632 | -47.85207 | 2025-08-25 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e4f5b2f-2967-31ee-bbe3-d8a12a21aa66 | -3.69727 | -49.54604 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f350ab1d-f234-3c51-b37c-6c0b029eb2d9 | -4.1031 | -47.72605 | 2025-08-25 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8af5f961-b798-3077-a87c-38e92dcfcb9d | -6.91557 | -43.77533 | 2025-08-25 04:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d3a0713-52d8-3858-b5cc-55ff0d71e001 | -7.90616 | -45.88297 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01e27c5c-c37f-346c-b560-d5d6f15f99bf | -7.57805 | -45.23269 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c6e4bc7-188f-336e-8fb2-5a810f7faa07 | -6.14773 | -51.75398 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19759256-9146-3bb5-ae70-cb3d9da9e73f | -4.77217 | -45.3299 | 2025-08-25 04:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 253ee746-797c-36d6-9597-44da8a0282f8 | -5.48763 | -48.08786 | 2025-08-25 04:40:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 312da3cb-64f8-3977-9eae-1cbfacb0a1bf | -6.0541 | -44.4456 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28c7cbdf-afee-3b9b-b3b1-a90555e2d99f | -5.54975 | -45.56075 | 2025-08-25 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58d59c60-41e2-308b-a235-8e59f6363b23 | -2.94787 | -48.05871 | 2025-08-25 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83f16774-400b-396b-86fe-caf7ef44d61e | -3.43788 | -49.0486 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b075be0d-665b-34c8-b5ca-ad28f2f2e24d | -7.53678 | -50.53306 | 2025-08-25 04:40:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7a41233-20bf-3e61-891b-3d19a9da7159 | -7.29514 | -44.52929 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7af883d-38b4-3cff-a718-c65765d3af9d | -4.96506 | -55.81833 | 2025-08-25 04:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22128dd2-2367-3b2f-aee7-51a95252f4e9 | -3.45169 | -43.34105 | 2025-08-25 04:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcfa658c-059e-3c9f-a1c5-4c446ba8c085 | -5.71327 | -49.10239 | 2025-08-25 04:40:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d50b5073-266f-3be1-85cf-ceec94b71cc1 | -5.79646 | -59.21632 | 2025-08-25 04:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99ac9e4f-4e59-31b9-acb6-e0087cdd85c9 | -7.92423 | -45.89034 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 131ad7f9-c4b4-33dc-91a8-9f0d9dffbcd2 | -7.53771 | -46.02149 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1714ed98-96a9-3f20-bbf4-f01368964a28 | -7.47033 | -45.01707 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e1b44d8-d9d7-34c5-9133-2c913106e587 | -7.33088 | -44.53863 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ee77c6af-953c-397c-b9c0-5f3a27461a3c | -3.73129 | -48.92853 | 2025-08-25 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a6aeafc-0a75-3ba7-b086-0c6c3f788c6f | -7.76069 | -47.36173 | 2025-08-25 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbf107dd-9bd1-3e3c-a73b-c03228770e31 | -7.09393 | -44.62723 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27ea280d-5939-38dc-9296-ef50350fb281 | -7.17635 | -45.16912 | 2025-08-25 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d7355ed-e0ba-370f-ab16-f16f2e572391 | -5.55468 | -45.56385 | 2025-08-25 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c026c18-94a0-3e7c-bc06-5a6051701cdb | -6.87344 | -45.65374 | 2025-08-25 04:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5983893-5c79-30b4-9b42-f3927bb934c9 | -7.67385 | -45.39662 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ff4e680-4c3e-3671-b871-a25a67bd6d8c | -5.42131 | -60.16846 | 2025-08-25 04:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1b77d3e8-d17c-33d6-b973-f1e900d1f44f | -7.81888 | -46.88882 | 2025-08-25 04:40:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b63277d7-6217-318f-83ab-6fec4385b0bf | -7.46966 | -45.0196 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d8cbd00-1af1-3165-bf38-3581603b8128 | -5.74304 | -57.5837 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b04f416-30e0-3853-8c87-dec04cd317ca | -5.7094 | -46.02443 | 2025-08-25 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33def601-3d22-32bb-aa5f-ba9b0af45be2 | -2.77933 | -41.87728 | 2025-08-25 04:40:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c31ae08-f9ec-3b60-8ced-da09c690b3ff | -7.08993 | -44.62667 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02574aab-0c73-3caa-969f-9bfc46c47fef | -5.85931 | -51.75349 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be847c38-8889-3918-ab46-e4dba3930734 | -6.43391 | -44.55587 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52f8a507-ef72-309b-84dd-898b4a83315c | -6.55781 | -44.44941 | 2025-08-25 04:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1280819-c1c2-3e5b-bf11-70d109e3e589 | -8.17747 | -45.0643 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1fd8a1c6-aa1b-3ca5-a13b-f4949044a7e6 | -3.254 | -46.9052 | 2025-08-25 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 568e5d05-f870-3166-8eb2-82d32dea6994 | -6.90279 | -44.4108 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ef5503d-b373-3f68-ad65-ca9484cb6ce8 | -7.50419 | -45.83988 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 41ee5757-33a2-3b98-b1de-743bc4edbfe1 | -3.73075 | -48.93198 | 2025-08-25 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6105ff7-9eb2-35d9-b7b6-4035d56d95c8 | -8.24074 | -45.09063 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3f67a24-e898-35a4-8c18-a3b3e48f24bb | -6.21829 | -44.1106 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a209369f-a8d4-3740-93e6-672b5b71888d | -7.32738 | -44.53448 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 824d185a-7aca-3b3e-93c2-3ef829bea9f6 | -5.41356 | -60.17115 | 2025-08-25 04:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0689cf0f-21c3-3d1c-ae64-067ac94035ad | -7.28705 | -44.5282 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a96e8fe-13a7-31aa-a75c-d503add8d954 | -6.90634 | -44.41467 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e097086c-de9e-305e-ab13-6df54afa71f8 | -6.90166 | -47.93124 | 2025-08-25 04:40:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f761993d-89ab-360f-9fba-80df552e9325 | -5.75423 | -57.57951 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 770cc68c-deb5-376b-bb36-372935aaa79b | -6.12598 | -44.3739 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a7c13c7-9b2f-3604-88ea-c6e3010f6abc | -6.1664 | -43.00671 | 2025-08-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e5ac370-e3f2-33da-aca1-e464ad66af27 | -6.88399 | -45.66006 | 2025-08-25 04:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ccabe60-650b-33c1-8b9d-0191c28f2a3c | -7.53943 | -46.0243 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c4a5d5b5-c2f2-3d6b-b9b1-58db7d81b200 | -6.70088 | -44.01012 | 2025-08-25 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c83f73d1-b715-39f8-9956-4a7372efaf5b | -2.26653 | -47.85259 | 2025-08-25 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da91966b-faf3-3e07-a2e2-6dee04041772 | -8.17991 | -45.07515 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2ae83ca-5a8c-32b1-85cd-01bbbcc7439b | -5.74861 | -51.70049 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97dc9158-1d02-3a55-bb2b-bc8a725150e9 | -6.52767 | -44.43116 | 2025-08-25 04:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README40.md)
