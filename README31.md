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
| 70b80279-4b90-3785-b708-18f4fd31a046 | -3.02839 | -53.89281 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 5d31f702-cbf4-3b1d-aa06-862e8464a535 | -5.94853 | -41.37129 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 78a4ba1a-ccb2-3de1-b651-acc1d9e0d41d | -4.19522 | -44.26492 | 2026-10-06 04:19:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62529f65-a8b9-3503-817b-960416999b53 | -2.77212 | -54.09816 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a648d8-ea3c-35a8-bc78-0d23cb3986d5 | -7.90466 | -44.19096 | 2026-10-06 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f865c55-cacf-312f-a5fa-578121cad26f | -11.63838 | -43.65784 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38703dd1-6eb2-31cd-b3b1-bff0c53274ef | -5.83944 | -45.01366 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 8c25008e-d6fb-3359-82a0-22ce3c2399e6 | -3.0273 | -53.89919 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| c50d3b1c-0ab2-376c-ae14-6c3da501d098 | -8.82218 | -37.34386 | 2026-10-06 04:19:00 | NPP-375D | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5fb054cc-2268-3724-80bf-5de23e5a5868 | -11.26933 | -45.50081 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 63fce919-38b2-3cce-8dd2-5082290a8965 | -8.52197 | -48.90555 | 2026-10-06 04:19:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea47bddf-1164-36b1-b111-e3c93714cb08 | -3.64847 | -54.06277 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 907e494b-db1b-31bd-b107-f57bd4c08135 | -10.36121 | -45.03328 | 2026-10-06 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 737949c4-1619-37c1-8043-1f243d9e6868 | -8.90847 | -43.88174 | 2026-10-06 04:19:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4668828a-a1b2-3bc4-87d4-e73468ea731f | -5.60168 | -45.37306 | 2026-10-06 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00e1c900-6a57-3c35-9dec-53e3b03f510e | -6.76497 | -48.68218 | 2026-10-06 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1372318c-65bb-3d56-956f-8f4c57b7b006 | -6.34668 | -42.5511 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3ae1b360-f99b-37d2-a314-224b001e3292 | -6.36567 | -42.54658 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0de6a30f-5234-34c5-b4ed-2b1d819dac10 | -8.60274 | -45.66046 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 890ed0d9-9591-38c6-a5f3-b19a82dd555a | -3.06835 | -54.17595 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63ac22e6-ac8f-3c48-844d-732a869d6bd6 | -5.68648 | -53.48867 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb307fee-0da0-3a99-92fa-8f612f7a3a71 | -6.45189 | -43.82703 | 2026-10-06 04:19:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 782934b0-7751-32fb-84e5-8e08f4b1e2a2 | -5.6789 | -53.49337 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e14a280d-fa72-35d8-ad1f-fb9386af0cc6 | -11.26575 | -45.50019 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6c6e9f7b-e44b-37f7-990a-6579c189e200 | -7.37734 | -46.22309 | 2026-10-06 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 233be952-056e-3eb5-b708-4b9c38cfa2d5 | -9.81956 | -44.79428 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91dafd45-fd44-3032-954a-bf4623a60d30 | -9.60305 | -40.61266 | 2026-10-06 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| ebd6d2ba-5a8c-3a23-a735-9c993e1ffb84 | -6.33818 | -46.95118 | 2026-10-06 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da9bdc47-1f5c-34da-a84f-ab81f36ae7a4 | -9.76473 | -44.79847 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bc3a42d-8cd8-34fa-bd27-a8f818ec828e | -5.67924 | -53.49495 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10483315-d29d-3ab7-ba04-54475295fb10 | -4.3351 | -50.40615 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41a4a59f-b8ca-3d17-866e-e31eef252dc2 | 2.45909 | -50.82829 | 2026-10-06 04:19:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5cb7fe28-c738-3448-9c85-f67db18912cc | -6.8978 | -43.68076 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfe79bd1-1fe4-317b-a8e1-59cf14644d06 | -5.84318 | -45.01425 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 007441a1-7699-347f-a7d4-5ec3cf932ec3 | -2.87402 | -54.13659 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b9169be-e1b1-3095-815a-dd8f7da03f17 | -4.19226 | -44.26003 | 2026-10-06 04:19:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbf20eca-b4ac-3051-8542-abb349c8b139 | -9.82309 | -44.79484 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a67ba0d-f2de-3428-ab77-f5477952049c | -5.66995 | -42.59008 | 2026-10-06 04:19:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c4a01f1-dbe9-3c7a-8254-9f6ab7b3ba32 | -11.27595 | -45.52749 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5ce18a90-8fcc-3424-8701-26b52b7e9b69 | -3.09763 | -54.17415 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a2e133b2-19f4-3a2c-8d20-f7d0db48bfc7 | -6.80338 | -41.24698 | 2026-10-06 04:19:00 | NPP-375D | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 422b0eba-871d-3787-ab6a-ee1bb99260e8 | -7.24354 | -45.25917 | 2026-10-06 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d58bb7bc-d5e9-3009-839d-1bcb281ef338 | -9.95597 | -43.47483 | 2026-10-06 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7245c3b5-32e0-32ad-a37a-4231f235b48e | -3.11291 | -53.77153 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2c9b0f84-7d06-38ce-ae50-bd63626cad42 | -11.28239 | -45.51854 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5e2b1e88-dccd-347c-beb0-32d0ee62f57c | -11.27717 | -45.49793 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 395f3602-7bc7-3e22-9499-83fe33119ebf | -3.84295 | -50.31363 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1a38143-61fa-3b04-a7b9-120c51ad1169 | -4.77844 | -50.80883 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a379cb2a-e2d9-355a-af3c-6356d7cd74c7 | -5.97453 | -41.31494 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 85c10063-ab6f-3585-9154-20560e9de89c | -7.531 | -45.87934 | 2026-10-06 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d9f0c74-8666-3d02-892a-80c052ac1326 | -7.46906 | -42.99877 | 2026-10-06 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 87933ebd-7c8b-3999-a7cd-baf62b909ae4 | -3.80399 | -51.03755 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 699a24b6-c3c8-3181-8ae6-edacf52d0e5f | -9.92068 | -48.13963 | 2026-10-06 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b20f0d7-1605-3353-acba-5e6b6b8e41ff | -5.95518 | -41.37235 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ebf1f9ee-3ab2-3ed5-9be3-59f6ac8e4b85 | -3.02756 | -53.89359 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 05c10a18-b824-3b0c-ace4-85a9c386ecad | -3.31706 | -53.8554 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b62062d7-84c8-345d-81bc-5f0f3fe2b78f | -4.4653 | -54.97111 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75177c7b-fe3f-310d-8c5b-b4ad6d26dd0f | -11.27593 | -45.51317 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 3aab2e2b-b3bf-302b-bf98-82919a6d7237 | -9.60362 | -40.60899 | 2026-10-06 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 32d86708-6373-342a-954f-ece178c10495 | -3.07844 | -54.26233 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c0f622f9-9d20-3f56-afc7-51437aceef6a | -3.07537 | -54.17715 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 587298be-13c8-3d48-8a03-ffdab48e4ec9 | -6.34725 | -42.54752 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 35423322-7c0e-38f8-b964-659ba3dfb7d4 | -3.96533 | -48.12555 | 2026-10-06 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da3917de-622a-3ad1-98ec-a115e274ae73 | -5.84139 | -42.41967 | 2026-10-06 04:19:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c845a92d-dbc0-3adc-9ca0-5dc5518ff094 | -6.82068 | -39.30399 | 2026-10-06 04:19:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93ca27cc-f4ef-3279-b667-4d267d2c09b9 | -9.2562 | -45.66042 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5bca1b8-dc43-377e-882b-ece66befc345 | -5.97398 | -41.31841 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bb7ecff-e740-3e92-86a7-510847db1376 | -11.2852 | -45.50212 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 139d6f50-5dcd-324c-b1a0-98c107646cde | -7.29038 | -39.31744 | 2026-10-06 04:19:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 410f706e-a4ab-39aa-9539-34a2302a4821 | -7.7677 | -44.58087 | 2026-10-06 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8466945-a129-3eb4-adee-b6a082a1afce | -4.50852 | -43.68839 | 2026-10-06 04:19:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53084138-7632-324b-9e5a-eb1267a3c8a2 | -8.70203 | -45.22451 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8b758d0-085c-3d46-82f7-3f509ea7bf2a | -3.06539 | -54.27364 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d245d25-efef-3043-bfdb-b5c7674fb005 | -4.99771 | -42.42862 | 2026-10-06 04:19:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 12b7770a-5186-3bb7-a0b4-a5fda2d7899b | -5.3161 | -40.89775 | 2026-10-06 04:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6922c229-7627-3d6b-8c29-2df4e00654af | -7.46848 | -43.00239 | 2026-10-06 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e58a99e6-0944-39a0-a64f-f23d04906e07 | -5.83494 | -45.01757 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f0d47826-9a5a-3307-bab4-b7860e4dc4c5 | -11.2449 | -45.2532 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 017bf4ef-99ae-330b-9567-3486dcfec665 | -5.12243 | -43.99599 | 2026-10-06 04:19:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b28559b-675f-3b8e-a746-989b5b044536 | -9.8125 | -44.79313 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07495865-79d1-38ba-9c20-c06aac9a9ed6 | -6.877 | -43.67742 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 816806f7-57ff-3688-a9e4-059b97e4baaa | -6.89434 | -43.6802 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe4b1584-55ee-3c24-86fb-ee713c32eacc | -5.89015 | -43.53799 | 2026-10-06 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a23fbea1-9fda-327f-bd1e-df68b6279971 | -4.33269 | -43.81347 | 2026-10-06 04:19:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33b15743-0d74-357f-84fe-f1d983e476b0 | -5.82772 | -45.00925 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0ff0fb3a-aa81-3ef0-9425-6a5442e8b7eb | -8.58626 | -45.66712 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 193aad14-0e8d-36e9-89a6-f1f392f2d244 | -7.4754 | -42.80828 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 223c8ad3-8435-389d-8a09-9139c875d51f | -5.6158 | -44.8415 | 2026-10-06 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3051340c-48fe-3e9c-8821-766d7a6ea053 | -3.0787 | -54.23981 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 049f7da3-e131-303f-a239-059f8269b40c | -6.32438 | -43.81495 | 2026-10-06 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07854fd8-a9e6-3faf-b3fe-d8a2680a0e03 | -3.22081 | -53.88055 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72e5d89d-62ae-336a-8ffb-1562f362aa25 | -11.28808 | -45.50684 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 777909a9-dd3b-3600-a394-af2367e29e2d | -7.48155 | -42.81297 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bd305faf-3ff7-3d95-89a0-90c9ff5551e1 | -3.16786 | -50.44166 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 21c669d4-562f-3b6b-a7ce-b350062dc96e | -6.00836 | -53.51122 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00af690a-1309-3f1a-b71e-a9769334d93c | -3.09532 | -53.7106 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9e995d6b-b081-310c-96a3-3b9844e7c1c1 | -11.66317 | -43.63255 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b276d2b-e37f-3f5a-b6ad-210fe8c75609 | -3.80362 | -49.1154 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb3e4bc9-8889-3290-a362-55c3447e5c83 | -3.23356 | -53.8863 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c835ce8f-dbf0-3878-bc09-6227087f1bba | -3.16906 | -50.43454 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
