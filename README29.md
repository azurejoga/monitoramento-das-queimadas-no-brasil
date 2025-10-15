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
| b4c0846e-2802-37ba-a21c-5874ee4d228d | -5.86916 | -43.85035 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5c415a41-fb7a-37a6-92e5-c5b5e6d0edfe | -6.42294 | -44.03298 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6559b27-d71f-3354-8c60-ac86a15d6832 | -5.11949 | -46.06964 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6c8c838-1c5c-3f66-8744-ffc3527b812a | -6.30554 | -46.9338 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4309380a-483d-36e5-a455-9f08e41a9bb9 | -3.42376 | -50.26293 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0144abde-caf2-3b9f-b204-724272431206 | -5.38799 | -43.22139 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6605f5e7-2bab-308d-b8cc-39cfca0fea5a | -4.85195 | -40.07727 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 54d0d456-4e10-3d82-9a08-845a36b45967 | -8.27412 | -43.42541 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b3be1cd5-1f60-399f-9918-b403811327e8 | -9.34029 | -35.50561 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b3b46806-c69f-3451-82c3-cddc68d8b7e9 | -4.09973 | -44.4564 | 2025-10-15 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e7831cf-95a2-3729-80fc-9d49eb70d96a | -5.54123 | -43.46327 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f2aab91-7688-30c8-b1b2-301af79c32c8 | -6.48615 | -44.11255 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7862d79f-229b-33b5-a711-860b2e842dbf | -6.42685 | -41.83224 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d2528153-2bdd-342f-84ee-5e422ea63737 | -4.94331 | -41.71773 | 2025-10-15 04:06:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e460e8e4-d205-3a33-931d-d54963b0af4c | -5.87267 | -43.85101 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7491ded1-399f-34c1-ade1-dde406189872 | -8.2739 | -43.38406 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9f38dcc9-391e-3bf0-8110-06b28c446a6e | -7.29059 | -41.95618 | 2025-10-15 04:06:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84767997-4c87-3d9d-8967-7eebf6229a59 | -4.89925 | -45.51289 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 893235e9-3725-3bf0-ab17-a53d96b02215 | -5.42764 | -44.42474 | 2025-10-15 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 197b26d7-4e6a-341c-bd10-c02cbd30a68f | -5.33837 | -42.56762 | 2025-10-15 04:06:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 64f2f4ed-4102-328e-9164-cd782d532286 | -4.80176 | -45.71465 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7101c32b-9dde-3ac2-ac2a-0163671bc878 | -7.48765 | -42.14793 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 98b8921e-b69a-3372-8179-cba8a91f12a1 | -5.01157 | -44.49585 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9c32079-ffd1-31af-92fb-67a0212e30f1 | -4.15121 | -43.13165 | 2025-10-15 04:06:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a4835ba-c303-353a-b778-61b8714ff602 | -5.76548 | -46.0059 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6c39225-8e51-3a03-a974-d5aa915da227 | -7.98485 | -38.75538 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 33227f54-816d-3af3-b7e4-685f337fc703 | -8.21722 | -44.0759 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22ff7574-2817-3e2b-b74c-33ee5da368bc | -4.8653 | -45.54778 | 2025-10-15 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d086bf2-3e13-301f-85fb-361c9cf97f3b | -5.88673 | -42.89205 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9d542645-5ba1-39e6-a305-2174a5fea2b2 | -4.14319 | -41.66291 | 2025-10-15 04:06:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 351c8778-52f8-3d2a-a1e0-1c5facdd10f0 | -5.95674 | -43.17606 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9faa6d01-8551-3000-8eeb-06669e5be4dd | -5.1844 | -46.17955 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6620a42-2780-3f7c-aab6-165e77702c8d | -7.79213 | -42.39085 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2dcd47b4-fba1-353c-a3eb-efba701d3db2 | -5.72042 | -44.28006 | 2025-10-15 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb5ae6de-09ec-3e54-be26-b8d3b1f25873 | -6.40955 | -45.36858 | 2025-10-15 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe8c6d24-1204-3f22-8eb0-ffcb9dcbee18 | -2.86264 | -49.1683 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5c99aee-6229-36ec-b741-ba1f672bb045 | -7.08626 | -41.95891 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d29c82f8-edd2-32be-a31b-dd44152c3706 | -8.46391 | -44.19026 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 60e87adc-dd77-3b05-a5e5-89ba0568d281 | -5.42976 | -40.98359 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f9f1b74-b792-3b2b-b251-87b4b58f3a02 | -5.39614 | -44.04196 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ee751a2e-740e-328e-b983-39ed5ecbeeb8 | -6.28828 | -43.90272 | 2025-10-15 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67c61098-1e2d-3c70-95e1-e9f41b566613 | -7.56223 | -43.89442 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10865063-afc7-342b-9735-d7b2f169dc38 | -6.45531 | -44.58182 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b5c28131-b379-39b7-a56d-03f42b2a88b9 | -5.86181 | -43.87348 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6bb0eb8-be34-3513-b1d5-902c2b2119e8 | -6.19921 | -43.28306 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72a6b5ec-f5b4-3562-b77b-beddf58f8190 | -6.84044 | -42.77964 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 538ea0ee-5ca0-3b7a-82f4-e92a0e8626c9 | -6.14734 | -41.77377 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4cab2aa1-0f9a-305a-8a01-4626b2f37893 | -5.2474 | -44.4737 | 2025-10-15 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0b5574d-4f0a-3a9e-9cdd-06683ebfd96f | -2.83178 | -48.83687 | 2025-10-15 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16562bed-8e8e-31c2-8b5f-6c7a367e80b2 | -6.99324 | -38.44872 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3f85a407-5a21-3e63-ab25-cd82176f3346 | -6.15561 | -41.74313 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 426ef6be-b888-36b1-8cc7-f16d020a9238 | -5.86948 | -43.87079 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4976ad85-d1dd-3cac-8b3c-14126181a50d | -5.97226 | -42.92853 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7abf1a1e-0b67-3e1e-86d5-4225e9e16311 | -8.46324 | -44.19428 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 80eda545-5255-38d8-b1ca-29f8acc4d4a3 | -5.90573 | -42.83887 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 929b9e5b-4476-344c-b8a5-47dbf7973333 | -7.50431 | -43.06343 | 2025-10-15 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ee782109-9661-3b0c-aa25-0599ebfe4c22 | -5.97937 | -42.88453 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 663e24e7-d2eb-33d0-8a0e-81be37a7528e | -7.29611 | -41.96419 | 2025-10-15 04:06:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ef321bf-8978-3085-8f57-57dc9651adfd | -6.30973 | -46.93447 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1128bdbf-4298-37a8-ad9c-193a2a7db720 | -6.42205 | -43.07465 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7508cc6e-124b-3dd6-ae70-c4cffbe530fa | -5.31363 | -42.92289 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e1374f4-cab3-3977-a886-3fa197e4d468 | -5.42591 | -40.98651 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f287c456-ebcf-390a-b04f-e47c855d0665 | -5.92839 | -47.31802 | 2025-10-15 04:06:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56d77b72-2cd7-3cca-b4bc-b4c38a3fff27 | -9.13918 | -46.87389 | 2025-10-15 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c1df7e8-d197-3942-b1d7-f94d41758ab2 | -5.90528 | -42.82002 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8f4cffc5-536f-3180-bebd-7ebb1a300f5d | -5.90469 | -43.96539 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e6234c4-7a00-33c6-8dfc-5357fc10d452 | -6.83034 | -42.77801 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa146906-3c88-31ef-9e25-c7852abcfcb6 | -6.3882 | -41.94736 | 2025-10-15 04:06:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 38cceb15-7fc9-3ee0-9b71-545bc5831e00 | -7.79602 | -42.38789 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d27f3bb3-b777-3847-8b52-d0aabacce9c0 | -5.88451 | -42.88421 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 41357e55-45ff-3135-bed6-2d8cb9c3ec59 | -6.76902 | -42.81588 | 2025-10-15 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65908311-928b-3b35-9334-c21fbe04b79f | -5.02802 | -44.73562 | 2025-10-15 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90a11f52-3878-3178-81cb-6921fd78abe3 | -7.36447 | -43.64402 | 2025-10-15 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6088b26c-803e-3e43-9c94-0337e90c4727 | -5.27992 | -43.2397 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38ac98a3-5642-3a9a-8291-4956b0cf170b | -8.24218 | -43.40199 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0cec181a-30a9-30d0-b096-ee8356a30e29 | -6.48144 | -42.06576 | 2025-10-15 04:06:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 434ba1cc-aed8-3ed6-81bb-70baaaa33fa7 | -5.39983 | -41.15182 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d2b35a5c-7775-306b-ae7b-c05c5c5436bb | -6.17383 | -41.77805 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 940ee743-069e-3dac-948e-b8371deb1cb6 | -5.48675 | -44.63585 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d1f0337-5455-31c6-8e97-a8719da8b7ef | -5.86436 | -43.85767 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a124f1c-0ecf-3bab-829d-7f2ed2303375 | -5.41137 | -40.88535 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8650449b-1358-3067-b4ab-63acfe2524f0 | -6.23654 | -41.55367 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dbd9aea9-0fc6-39a5-9af9-4ad7a80f7c0a | -7.08433 | -45.20241 | 2025-10-15 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86a70872-6031-3bcf-975c-3f1bb66c941d | -5.41955 | -44.22512 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 780e6810-9c36-31cd-b61f-c97959e64e2b | -4.79362 | -45.32708 | 2025-10-15 04:06:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9170dfa1-a2f0-3bff-b269-543fa74d1813 | -7.55234 | -42.06186 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 372791d9-894a-3325-88da-0ee82e9f9d3c | -6.14071 | -41.75139 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49db44a9-bffe-3b95-a5ed-38b7232ec051 | -5.83054 | -42.33021 | 2025-10-15 04:06:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16226767-7c88-3284-ae55-f0914d619a8d | -5.79437 | -43.88721 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46f0f0f8-2782-3abe-85e3-9a1e6463fee0 | -3.43115 | -50.25254 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0426161a-b3e1-34c9-8c23-9457fa10f0d2 | -7.0835 | -41.9549 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5fe1d96f-e845-3406-a469-308cf47efdbf | -7.75192 | -42.45249 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0b77dea8-7b67-3d99-8fdc-9fd3ad33d6e6 | -3.78171 | -49.43122 | 2025-10-15 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3d1a404-3e58-32eb-b164-58ddb40c38c4 | -6.45551 | -41.88667 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9ab36f10-15ae-37be-98c2-74f9c0da8f83 | -7.04861 | -43.97286 | 2025-10-15 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b5da28b-31b3-3601-96da-729943a6aedc | -4.90636 | -43.46496 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 3187f04e-9c0a-379b-93e5-d4161c95d3e0 | -6.55292 | -43.92616 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f065d388-163d-3168-9044-773224b53eda | -4.78221 | -46.01142 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d974a17-edd3-3f32-865e-d4ff47d0db50 | -5.877 | -42.823 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8c1431a1-7fdf-3504-9c21-aa394edec57a | -7.27701 | -42.95268 | 2025-10-15 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README30.md)
