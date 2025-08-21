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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e62c6676-bccd-35b0-860a-edf7387b0e00 | -10.72569 | -48.23695 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ffd9fcc-761c-36ea-8ad8-623708cad1e6 | -12.59876 | -47.08328 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a858864e-1544-3122-819b-521aea6130a4 | -6.06973 | -44.14226 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 272294d5-0f43-3528-810a-eb8fa0158b6b | -12.09064 | -44.72686 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a16ae744-1ad2-31d6-8e7e-889fd75c8676 | -7.02757 | -44.61946 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 6821b8ce-997a-3684-8a74-66a88ec04efe | -5.67219 | -43.50996 | 2025-08-21 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d07c5320-70d7-3b4c-8c7d-65fa5e16e33a | -7.20904 | -46.24931 | 2025-08-21 04:17:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f20a586-57fd-32c3-b244-13036935036f | -6.02075 | -42.82825 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f7274a0a-d5cb-3024-aeb9-dd7f72187473 | -6.93985 | -44.3833 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad2345ca-65a9-307f-bfcb-109f63630533 | -12.98185 | -45.20591 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4587081f-bd71-3183-a8c8-2f01e3fc3cbe | -7.09617 | -43.51449 | 2025-08-21 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fcf5e8b-fb5d-3093-bb75-8d36b6292202 | -7.39177 | -44.26813 | 2025-08-21 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e63d758a-5986-3ab0-a8e5-40b550ef0882 | -6.50123 | -43.44848 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15f94759-b7f7-3aaa-9d5d-114ce0e900ef | -7.01857 | -44.61051 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 652e5f13-7c7d-3e29-82c6-18334359a5b4 | -7.64621 | -46.26982 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b719a61-9e17-3601-b903-587339c77535 | -6.56628 | -44.48677 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d090dfc1-5d06-369c-80e9-9f623573c318 | -6.54259 | -45.51283 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 738f753a-3dbd-3693-9477-8c3c12c99b9d | -5.68467 | -43.86221 | 2025-08-21 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5684aef-6db7-3234-8f3e-31fb1394e8f5 | -6.27351 | -43.70612 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a3790d0-b41c-3f9c-9e81-6d6ed8c735b3 | -7.70517 | -44.0283 | 2025-08-21 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f85fe425-f96f-313d-b171-0b0780303b2f | -11.17376 | -46.13493 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13a4373d-0742-30af-a3d0-5c48eb3e92c7 | -8.4311 | -49.57659 | 2025-08-21 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b179423f-99e8-3074-82b3-58c4d235adbb | -6.61782 | -43.88333 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ff6cc9c-d31e-3385-af9a-25e2eed3b1fe | -7.99859 | -44.79308 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e686f65-7607-3b0e-8bcc-ea8648614167 | -8.28635 | -47.28125 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d0b5152-1112-382d-8a43-a3e050d6e2d5 | -6.00696 | -42.85093 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 64952054-4891-3117-a0ac-34820066ea77 | -7.27297 | -43.6788 | 2025-08-21 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4400833-f4e0-3f6d-9a7f-31c9495c5410 | -6.53498 | -45.4714 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 453f2e4a-6cf4-32ed-b0fe-9a942139f9ed | -6.53907 | -45.51229 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eb23cec-22e1-33f6-8178-887394c5dd42 | -6.15639 | -42.71806 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e796527a-893f-38a0-9979-caa392dfb5b7 | -6.21173 | -43.33459 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7c52070-2900-31d5-a23b-2fe2dc51ec58 | -9.48551 | -47.32711 | 2025-08-21 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f80a43a9-0f44-3e13-892e-b365ba8baeeb | -6.50178 | -43.44501 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01f49ba3-23a8-3ada-b58c-d464588a6ffe | -6.49755 | -43.10612 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea29695e-b7e6-3c9c-91ca-6089fc19174e | -8.16643 | -47.35384 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ae5fb55f-0e4e-3b98-8ee9-08440d78edd7 | -6.76976 | -44.33058 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bbc1fb9-7a4e-30f7-a8fb-22771ae72303 | -11.91111 | -44.88007 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78ba7ee0-c882-332e-a22a-e830ef483c03 | -6.5721 | -43.00058 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ab199b5-cbaa-3e79-88c0-1e8445a0784d | -6.34199 | -43.42693 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ddde470-97eb-3d4c-b3ca-1f16abac31d8 | -6.95399 | -44.18063 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a40ca4ea-cbc3-3719-bf29-0870ed0e643b | -6.39963 | -44.26093 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f47dd5e1-d1af-381b-b283-bd47cfd86cd1 | -9.2624 | -44.53632 | 2025-08-21 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 942ef2d4-cc7e-3dc7-8f34-c54c0c87eb1b | -10.97873 | -45.65861 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 245f360b-2e42-3170-849f-2a06b9914778 | -7.02698 | -44.62307 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 741c8a3c-c9eb-306c-a59b-0a145bab2600 | -11.91502 | -44.87707 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc7a21da-5c7b-36ef-82de-385224632831 | -5.87348 | -42.41029 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c41ac403-bbd5-3c5a-9e15-3e9a6f2095b2 | -6.31744 | -43.75274 | 2025-08-21 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64d14312-bebd-3b99-b006-463131347092 | -6.01466 | -42.82374 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a5c89921-6969-317c-99d9-55264f1398ff | -7.89121 | -46.7286 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d6bb8e2b-4576-31ce-a6db-ed6788024f39 | -7.01681 | -44.62139 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| eaf95496-21bb-37a8-a7e5-5a30c73b7a41 | -6.86879 | -43.60368 | 2025-08-21 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e15ce5b-2daf-3463-aba6-fa2c4cdd54a1 | -5.44053 | -45.09971 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4e4547d4-dd59-3df4-a5a0-bbc6a0a4760c | -13.01764 | -45.17518 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 4f5188d0-c364-3d0f-a3a8-2befff1cf208 | -6.41794 | -44.67329 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| be555530-c71e-3674-8992-58ad4adf2230 | -7.57335 | -44.39994 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef47aa96-2a0e-31e3-b6ac-fbdb7e0167d4 | -6.42194 | -44.6702 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 670846e7-77cd-3b92-b7c3-a33166f15652 | -6.63967 | -44.40252 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5106e25-e4f2-3298-8b7a-fe917b626c8f | -13.01879 | -45.16804 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| e7804bb3-4de2-3b28-90e0-fbb40cb3ff4c | -8.37204 | -55.00029 | 2025-08-21 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8fb1e44-8a03-3216-80ab-f677f1aabb16 | -7.59641 | -44.38533 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b86e4dbd-0d9f-3ad9-8b0c-61e5a8b8745c | -7.30294 | -43.68359 | 2025-08-21 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9fee305-f7eb-3bd0-a5a1-0b5319da3c11 | -6.54482 | -45.52126 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60f4d87c-3642-3987-bc61-487961667f79 | -6.49368 | -43.10906 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b41be45-6623-3015-ad84-b533201f937f | -9.33333 | -48.51933 | 2025-08-21 04:17:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b39c2867-ac0c-31fa-b3fc-07559a0aec12 | -7.63446 | -45.25547 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6663550b-be46-3530-9898-103df707d840 | -6.27572 | -43.71371 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8461405a-7ec9-3ec0-9006-3c188bd03ef9 | -12.19018 | -47.21903 | 2025-08-21 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cd985b4-7d77-3793-adea-dd331d796751 | -6.02729 | -44.3646 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4dced9c-eb0b-3fb4-b388-5d5eea30931b | -5.9616 | -44.13991 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a5ee13f-a5ca-3f1c-a7eb-4508578cb31a | -6.70814 | -44.32106 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 786b59b6-a395-341b-9037-bfd06c3d4830 | -7.63974 | -45.24461 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43ae31c6-9554-3d96-81f3-20f95346849b | -6.45317 | -53.37611 | 2025-08-21 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ff0ffe8-775d-3a3c-8779-912f08606e89 | -6.95277 | -43.86489 | 2025-08-21 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c76bba69-02c4-3f03-ad47-bfe0465f12fb | -11.30404 | -44.92609 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64eb0330-aa91-360c-9163-ba84e5c614d4 | -13.02213 | -45.16859 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 657cd02e-09d6-3ed3-a00b-7ecf7e868653 | -11.30796 | -44.92306 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efea05c1-c4bf-3e39-9c11-f2bf28cec705 | -11.43332 | -47.32418 | 2025-08-21 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 713f1273-026f-308b-9821-532f12bd4dd2 | -7.95352 | -42.65099 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2d4da119-018d-3ca2-b95d-693550c157ef | -5.08874 | -47.71851 | 2025-08-21 04:17:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22021a0b-c6c3-31bb-8635-f21892cec88a | -21.9782 | -42.878 | 2025-08-21 04:19:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6764a5d4-431e-3649-aff2-2a1ff31f1135 | -22.2479 | -45.92102 | 2025-08-21 04:19:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9fdaebda-2f79-3020-86bc-4b30f9863bc3 | -22.30509 | -43.17754 | 2025-08-21 04:19:00 | NPP-375D | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f1c4992-4f60-3dd6-b0f6-0a1ab013a3b3 | -19.96 | -44.85528 | 2025-08-21 04:19:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 160344ab-c44b-3b72-a4d4-8c3ad7eab2a7 | -19.3003 | -46.02738 | 2025-08-21 04:19:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d8889d2-bf72-3b7c-ac46-d251ac302f1a | -23.31084 | -46.90498 | 2025-08-21 04:19:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f93d5787-0393-3791-a057-0b269de1352a | -23.34965 | -46.59921 | 2025-08-21 04:19:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2d7f1bbc-4554-3f63-bd79-2883b2641fd9 | -20.49448 | -43.87574 | 2025-08-21 04:19:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6bc1ce9f-0ff6-3941-bb35-8acce24182e9 | -19.42258 | -47.24152 | 2025-08-21 04:19:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b5e2b70-369b-374f-a3af-fc851bc6ee08 | -23.23149 | -47.53047 | 2025-08-21 04:19:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 49f0f77d-7039-3dca-953d-be57793ba6d4 | -20.23838 | -42.34078 | 2025-08-21 04:19:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ece0ddb0-a223-3f16-98d9-2fe7d334a9a4 | -23.67606 | -51.68149 | 2025-08-21 04:19:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b4d7c4d5-3a1d-3212-b68e-659d55e5cb8f | -20.32003 | -46.60855 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f29a6018-dd73-324e-b9d2-b337db54b128 | -22.71073 | -42.64578 | 2025-08-21 04:19:00 | NPP-375D | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dd1364b1-27ea-3725-be49-3114eef3fa15 | -19.29483 | -48.43489 | 2025-08-21 04:19:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 848c0dec-ec25-3f0c-8d96-1a90cbb319b8 | -22.24456 | -45.92043 | 2025-08-21 04:19:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6f3431ee-af79-344d-8a9f-e8049884e35d | -20.50468 | -43.95242 | 2025-08-21 04:19:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 575f7f2e-30e9-3418-b081-a6807ef7b7ed | -20.32335 | -46.60917 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4190e4a-5d5c-36ed-8303-2a10b03dd89a | -22.69547 | -43.73131 | 2025-08-21 04:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c88e3442-2ac9-3483-adcf-c490a62f5e7a | -22.94501 | -43.70587 | 2025-08-21 04:19:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 285374a4-f84a-3737-9520-857e305df6e8 | -23.23544 | -47.52732 | 2025-08-21 04:19:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README33.md)
