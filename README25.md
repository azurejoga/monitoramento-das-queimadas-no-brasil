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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21edc4ad-36db-36ee-b4ed-c5f36cacd9f7 | -22.7271 | -51.3948 | 2025-09-27 04:10:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| cd99e0ce-670d-3998-83ac-9080bfa470bd | 1.88272 | -50.83086 | 2025-09-27 04:19:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84b8e4f0-9acc-3c7d-a069-43b254d34cfb | -22.8617 | -51.795 | 2025-09-27 04:20:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| ace8209c-684d-3e99-93cb-48f172634290 | -22.7271 | -51.3948 | 2025-09-27 04:20:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.9 |
| e9b81344-fbfa-3c30-93af-3be8e36b5ecd | -22.8623 | -51.7723 | 2025-09-27 04:20:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| a28e203f-9efb-3c2b-8afd-bca480a48e5f | -9.9328 | -59.9247 | 2025-09-27 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 7c58b69f-1c3a-3043-b792-537a21daed5a | -22.7277 | -51.372 | 2025-09-27 04:20:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 57.4 |
| 76bc57b4-57d8-3fb2-9526-51278ab44d33 | -5.48275 | -43.07463 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5aa68d04-ab46-3b69-bb18-ac88a7bfd33c | -5.40786 | -42.27476 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 10bad9d5-1377-3bed-83e6-aac1190f670a | -6.54113 | -43.82892 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cdeb197d-2e28-34f6-8432-db20e0848d24 | -5.48331 | -43.07101 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed109e22-e609-39c0-9f58-7f63fc82e6d2 | -6.54139 | -43.93726 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5d8fe85-02ff-324e-a34d-2975cf81f02d | -7.04593 | -43.02577 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 399f2ffe-688e-317c-a6a2-fd14df5aefec | -6.49964 | -43.64503 | 2025-09-27 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be58f904-69bc-3db8-8739-2c287ebfc6e4 | -5.48727 | -43.06791 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05734b92-5d82-31be-ba79-74ec43824876 | -5.91524 | -43.96559 | 2025-09-27 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7dca6d2-27fb-363b-bab7-5879c231f8ae | -5.72258 | -42.65354 | 2025-09-27 04:21:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 319d7186-2050-37aa-ad42-342807e02f28 | -6.22638 | -44.18281 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 800df743-2f0e-395d-b765-98cae16281db | -5.49576 | -43.08031 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0184bccd-1bda-3695-83d6-52ff08df3f70 | -6.26929 | -44.07481 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f1b17bd-08bf-3dea-938d-498ae1e89527 | -4.66927 | -50.97467 | 2025-09-27 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 202cc165-827d-3188-9068-3ad44ccbfd41 | -6.06577 | -44.87645 | 2025-09-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fd95bad-4cd4-3ff0-9c05-dd07b21cfa57 | -6.08661 | -44.07811 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39f3f60a-190d-3a08-9c88-d2b7eca6c7ba | -7.15047 | -45.52057 | 2025-09-27 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 595f265a-3b14-3555-9c44-eda7f465742e | -4.57499 | -44.07996 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e0f64fa-0d90-3851-bbc9-ae72c7ed9306 | -5.95674 | -42.89645 | 2025-09-27 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 59ed5c8c-71a5-34d0-8812-a691322c70d7 | -5.7299 | -42.64633 | 2025-09-27 04:21:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ed8363f-8143-308c-bff4-d3d7b573f4f9 | -5.91469 | -43.96908 | 2025-09-27 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d33e9387-b131-37e8-a3de-0db525d42df7 | -6.27905 | -46.09973 | 2025-09-27 04:21:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8a87ff9-51b8-3417-8378-af29e99c136c | -6.49909 | -43.64857 | 2025-09-27 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11aa6ca9-057a-3710-8d03-7426d1fd2130 | -7.18943 | -41.70403 | 2025-09-27 04:21:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2f1bb339-b081-3900-86c6-38e0b850f9c2 | -3.83979 | -49.25872 | 2025-09-27 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d14cac76-a1c5-396e-a3f7-ebf78aed5e6c | -5.08273 | -44.867 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 335e299c-9793-3ef8-b6ae-934fb46cd1e2 | -7.26534 | -42.98207 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a5ffcad-af57-371a-9f4e-558972d2f6f1 | -5.82192 | -41.2991 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 992728ae-8cd7-3ab8-bdd6-3a09ea61274e | -6.06222 | -43.2033 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c89e4150-8478-3b81-933d-1b3225242948 | -6.99527 | -42.3959 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 65757722-a84a-3ad8-aef9-600ba352fdcd | -4.60942 | -43.10642 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46a1b30b-4d68-3a0c-bfb5-059a40dd7333 | -5.08161 | -44.85255 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fd08d90c-fe8c-3e1e-85d1-fe1846ed475e | -3.45782 | -39.04145 | 2025-09-27 04:21:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 175ceed5-4e91-399a-9015-160a572a58f4 | -6.70349 | -42.75245 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3ba09b3f-b0c1-3089-99a6-a8a05b767fce | -4.6837 | -46.4477 | 2025-09-27 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b980b49-1bf9-3707-a8c4-a266ade881e6 | -6.01196 | -42.5157 | 2025-09-27 04:21:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f00baaa7-3eb5-385c-b213-c7985edadb11 | -5.7893 | -45.36161 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4cbe3d5-39ba-3dfa-ae80-1f40aa1c0116 | -6.27263 | -44.07533 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3173215e-21b1-3c06-bcba-b125d510fad6 | -4.14493 | -39.99972 | 2025-09-27 04:21:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f5ca54b0-934f-3747-b73d-707f0634555b | -2.91528 | -48.1917 | 2025-09-27 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00b6fae9-d269-30cb-a95f-2571e947c301 | -6.55065 | -43.83391 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1bf5ba5-ccdc-3db5-9d1a-4b9a8f76c598 | -4.77042 | -43.28409 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ee61c34-2961-3ca5-b406-2b7a40634539 | -5.79621 | -42.83088 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 85ca15f3-ba5d-39ee-9082-871022784107 | -3.82194 | -40.3412 | 2025-09-27 04:21:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c1793cef-5578-39c5-a9e1-181dc27a215e | -4.7983 | -47.27999 | 2025-09-27 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b40dcea-5223-3abf-8a62-13fa92c1e542 | -6.33527 | -43.35614 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf5ea436-a339-3324-94b9-be2185cb4a07 | -6.63291 | -43.82538 | 2025-09-27 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5cefeca-3e93-3776-b8e5-e966f322ca3c | -4.94018 | -45.58675 | 2025-09-27 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53f2b8fb-0da6-31d3-b12e-8898decf2490 | -3.82379 | -40.99038 | 2025-09-27 04:21:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c761e0ec-d8d1-309a-8b4c-adc5532ec15e | -5.53471 | -42.73888 | 2025-09-27 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7081343b-8f5b-3c9f-bec1-4cd48fb547fe | -5.47322 | -36.66628 | 2025-09-27 04:21:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 244d39a2-f4d8-35d3-bd01-f12c7da9db26 | -4.60997 | -43.10286 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81a7aa57-7a37-38ca-937f-af179b97d9c8 | -5.08106 | -44.85603 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 979436de-54e1-37ba-85c5-6a88bf35030f | -5.80362 | -42.82833 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5a24f97a-db29-3686-9c3c-f7d70aa99e85 | -6.07048 | -44.072 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea753718-46f0-3913-b636-63f318baa69b | -7.60253 | -43.05588 | 2025-09-27 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4abe8d3c-b5d0-337a-9b10-728f8c65613c | -6.70925 | -42.73787 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 09dd6d34-8fd3-35eb-95e3-dab81e371566 | -6.45904 | -44.05775 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a463113-79d0-3c60-8d8e-66306ab22493 | -4.57941 | -44.07355 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6fdffa5-560e-3598-91ca-0516b102e457 | -5.80806 | -42.81763 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a8abbf9-e70b-3972-a210-a6e1caaaeda9 | -5.19656 | -43.72081 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a11c70a2-bdef-320f-b439-fb0f309edd03 | -5.30826 | -44.85258 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7dfab9e9-630c-3784-948e-6898f5edeba0 | -5.19381 | -43.73832 | 2025-09-27 04:21:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17992a9a-3ba4-3aa4-9eae-7e4dc9b50b5f | -4.96757 | -43.19796 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0977e82b-cd86-3aa2-94b4-e56318a7d83d | -5.07996 | -44.86297 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 08fedb8a-e44b-3aeb-a0d0-1372c14870c8 | -4.60605 | -43.1059 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da99baba-4c94-3022-abcd-6ee3b0bf3308 | -6.74505 | -44.70962 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0589a8b-a770-364f-adc5-8a3a7f1696c6 | -6.55009 | -43.83745 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94bc5b30-c1a0-36a7-adcf-17406653bed1 | -4.6139 | -43.09982 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b85735f5-67dc-345d-8456-d90fc8bddef2 | -5.14481 | -37.74274 | 2025-09-27 04:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 53d848ff-efa3-3952-b28c-58ddadef7517 | -6.69835 | -44.59901 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e7391fa-6c42-33a6-a05f-6c42baa84478 | -2.88236 | -40.46312 | 2025-09-27 04:21:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1a1cfeb5-6de7-33f9-b769-cbf8356a85be | -6.31954 | -43.39045 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0e3440f-55eb-3501-b130-cd878d43bc31 | -6.9961 | -46.99422 | 2025-09-27 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2df41232-efca-33ea-97d5-668a8f4397ce | -6.40503 | -43.31145 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56748d79-dd93-3b79-9323-b3b142cd7b20 | -5.73447 | -42.63954 | 2025-09-27 04:21:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc6e503a-12a1-3702-a5d0-be9c757ada0d | -5.52847 | -42.82451 | 2025-09-27 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 32b5abc2-b24a-3c9a-8b8d-4a3622d85a42 | -6.31616 | -43.38993 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d70d6628-3206-3cee-9443-b0ca1268af61 | -6.06504 | -43.20747 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 786e77ee-9c7e-3bc6-b8d0-8ae0e816cb19 | -6.069 | -43.20438 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 640c6c3e-a057-3145-9708-f862f995bea5 | -6.70407 | -42.74868 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c232c305-8693-3ca5-bcc5-0133b2815c30 | -5.36726 | -42.28415 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 950c7c06-ac7a-3e30-98ad-b58a7d649e2a | -6.3196 | -43.45667 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b055300-fe19-38c7-ac86-4c7e112b2ea5 | -6.26984 | -44.07132 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcac9d1f-7490-3d90-a12f-e387c78a0f08 | -6.34087 | -44.37526 | 2025-09-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b83ad47f-d822-341d-ad2b-b4a68a6fd090 | -6.94464 | -43.25163 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e681980-6959-36c6-8c36-4b63f4d5381f | -6.05173 | -44.74977 | 2025-09-27 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01c6f9d1-6b3b-3287-8c40-1ab87d3faffc | -3.29745 | -42.17855 | 2025-09-27 04:21:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12e9628d-577d-354a-9fc4-6363f37612da | -6.70176 | -42.74057 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f39d24b7-c535-314b-91a4-aec44af39b0d | -6.06961 | -44.85217 | 2025-09-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72d188c9-a37b-3bd6-94d0-5788044e5799 | -4.57179 | -48.02239 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b14755e7-29bf-325e-ae8f-bca4e2daaf0d | -7.03004 | -39.63068 | 2025-09-27 04:21:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 49448646-1c4d-322f-8427-490880bdc207 | -5.73739 | -44.98447 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README26.md)
