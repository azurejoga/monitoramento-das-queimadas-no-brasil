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
| 1efdaee0-6a6c-3a59-9270-f5aaaeca8915 | -11.63488 | -48.02601 | 2026-05-19 05:01:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98aa6e3a-cca0-3038-8894-91f36a879827 | -9.30235 | -45.48666 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd6ba326-79ef-388b-8476-12c67213d38b | -14.17629 | -52.88794 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0138f49-59ba-341d-9802-1a4733a34239 | -11.18208 | -55.91776 | 2026-05-19 05:01:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ffedea1-1923-3d47-93eb-8acd97b82e41 | -11.18541 | -55.91831 | 2026-05-19 05:01:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42fdb959-1df6-31b8-8b45-25de379c95f6 | -11.7467 | -54.79753 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a410256-cde2-3fc0-b5f4-20a86220bf2f | -11.07947 | -48.25916 | 2026-05-19 05:01:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6d9d540-491e-39cd-abb5-e77f18855ee4 | -10.45112 | -47.93762 | 2026-05-19 05:01:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2ba63be8-6862-3515-805f-d3d9150ef3ea | -11.45577 | -52.91842 | 2026-05-19 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e969b3d-0fe0-388d-a560-57c2ed42713d | -9.30484 | -45.4894 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7635bfcc-36dc-3b9d-9365-eb627f1256c5 | -11.45044 | -55.10734 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 589de6b8-a2d7-385b-ac77-059ea5514c72 | -11.46273 | -52.91949 | 2026-05-19 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2f3bb85-57f8-32ab-9b60-2bc46e6e95fb | -10.66601 | -49.70235 | 2026-05-19 05:01:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f88b5d82-d37c-357a-aaaa-1f678a0ee052 | -11.07879 | -48.26406 | 2026-05-19 05:01:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0061c40-2f60-36f6-8bc8-68d532634d51 | -14.1626 | -52.88151 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cca46d4d-afa0-30f3-a728-5bef26528455 | -9.29539 | -45.47773 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2998cfbb-1a51-3d64-878c-bf0300d8262f | -9.29789 | -45.47912 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cd74b4f-1539-3476-a5bd-d42ce1f54c13 | -11.45264 | -55.11489 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 946ecd74-349a-3b34-b968-d8084ee7ba7e | -10.5731 | -46.66416 | 2026-05-19 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd58d282-9ba1-3a7c-a6a0-858d82a6b249 | -11.44861 | -54.09337 | 2026-05-19 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2cce41c-28e8-3a2c-a50f-d9bd5c44f5e3 | -12.05079 | -45.27626 | 2026-05-19 05:01:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90da807b-8778-3d31-b8b1-95478e63be8a | -14.16617 | -52.88206 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e0ac698d-31e0-3352-bb09-4d9ddbfc2afb | -10.65288 | -42.31944 | 2026-05-19 05:01:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1385ad0d-a225-3993-b9ba-939bea9354d3 | -14.1584 | -52.88521 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6ddc5461-81da-3ea5-bde0-a08c133b3d8d | -12.06115 | -45.28556 | 2026-05-19 05:01:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 597830ab-0020-353e-84a7-0e62a20ce78a | -9.29495 | -45.48119 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1f93d6d-f32a-3081-8a4d-f88bd49ce726 | -14.97268 | -45.45532 | 2026-05-19 05:01:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d88cce02-9b91-3a3c-ad7c-8ccd8e20f33c | -9.89262 | -49.33728 | 2026-05-19 05:01:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e75e2004-9609-3b78-91a4-9fc0cb22f3f6 | -11.44414 | -54.10004 | 2026-05-19 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1da67bfd-799b-332f-a3e6-244f55515041 | -14.16443 | -52.869 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d92eee7-6df7-373b-b4d7-8e65d627f070 | -10.65011 | -42.31551 | 2026-05-19 05:01:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c5b59bf5-ce2b-3902-bb7b-91027b214ca2 | -9.30727 | -45.49074 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e741bd31-503c-3417-a377-ec7c33a5b260 | -9.31024 | -45.49004 | 2026-05-19 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e4b5a6d-e2ab-34f6-a626-84c252df1b87 | -11.45651 | -55.11192 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79f02968-1930-3694-a29c-1d0e3d9c12ae | -14.17987 | -52.88847 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f0844e1-212c-3221-8add-d51a36f3923e | -11.44933 | -55.11436 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfa59de2-f6bc-3c9b-95e7-ea9800998618 | -10.39933 | -49.44499 | 2026-05-19 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59778055-4370-3a78-a0ec-6e863793160b | -12.23259 | -49.3924 | 2026-05-19 05:01:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7978d788-eabe-3489-9bee-442b2b016d36 | -11.4532 | -55.11139 | 2026-05-19 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8c44e01-de21-3fa6-a1e9-12d4eef9387a | -11.61209 | -47.09778 | 2026-05-19 05:01:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8bb0f25-2d07-3ea8-957b-c2ebec0e78a7 | -10.13287 | -52.20214 | 2026-05-19 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bedcd288-43ba-32ee-925d-2fec1bf561d3 | -14.14942 | -52.89663 | 2026-05-19 05:01:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55df4d01-d459-3be7-8089-f5456c5fb5b1 | -14.70578 | -48.31966 | 2026-05-19 05:01:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f70d5594-1dbf-3e5b-8f74-f0bcc265acfc | -15.96141 | -52.21013 | 2026-05-19 05:04:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3aacd15-1f8b-3399-9d15-bd45ed77ec49 | -11.45229 | -54.09303 | 2026-05-19 05:50:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d67caf3a-993a-3120-8453-a30f42b3fd0b | -11.44872 | -54.09795 | 2026-05-19 05:50:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cf3e0a64-3588-38ff-8061-93cd825f90cc | -11.44946 | -54.09101 | 2026-05-19 05:50:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5f995522-f902-385a-8b64-12d2cc3b878d | -11.43808 | -54.09141 | 2026-05-19 05:50:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4496d153-2bd3-305e-a9be-cf17355be279 | -8.54878 | -45.98566 | 2026-05-19 06:25:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7ba24334-3510-38a0-8a0d-a916ac499c9a | -8.28513 | -49.39433 | 2026-05-19 06:25:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4e0aded1-d8cd-3caf-9965-9a5fc44be8b3 | -8.71745 | -48.32718 | 2026-05-19 06:25:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| a57e680a-8397-3fa4-a1e7-d5fc8943c309 | -12.05057 | -45.27678 | 2026-05-19 06:27:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 972499ff-836f-332b-a1aa-54cb89106fee | -12.05727 | -45.27422 | 2026-05-19 06:27:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 22c9fa95-31ad-3390-99f1-85b535115228 | -10.45052 | -47.9415 | 2026-05-19 06:27:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d795d430-0a53-331f-9471-8420d9962ba7 | -10.5719 | -46.667 | 2026-05-19 06:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 614922d6-cb7b-3ee8-b710-4a4c0f45754a | -11.60734 | -47.09821 | 2026-05-19 06:27:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 27d8d0bd-f25d-3270-9b85-37f48e3bb902 | -10.4519 | -47.93251 | 2026-05-19 06:27:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4cf573b9-c7e6-33ab-ba2e-358b92d1da51 | -10.44913 | -47.95055 | 2026-05-19 06:27:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8806e0c9-4327-3ff7-a55a-0b2d0ab0abfc | -12.05203 | -45.26675 | 2026-05-19 06:27:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5df243be-4fdc-36c0-91ed-b379e21067a5 | -11.61611 | -47.09954 | 2026-05-19 06:27:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f07f54cc-2acb-3f89-ac2a-347152b5c2c3 | -6.2978 | -43.63435 | 2026-05-19 11:36:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b2576ebd-51f7-372a-8a84-d2fdab187ccb | -6.39632 | -44.16282 | 2026-05-19 11:36:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 31103694-3171-382c-b57a-a236adc1ae32 | -5.25765 | -37.91102 | 2026-05-19 11:36:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 61d0828f-6d28-3c8e-975f-4ab6ecb34dc1 | -6.39488 | -44.17268 | 2026-05-19 11:36:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3a85b011-0282-3db3-a1f7-044f8833b1a0 | -6.81583 | -43.8142 | 2026-05-19 11:36:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 935118f7-1878-3c65-bf69-731b29d8f044 | -12.22395 | -44.24575 | 2026-05-19 11:38:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| aebf67f6-91c1-300a-bdef-023adf8f6308 | -12.60803 | -44.51637 | 2026-05-19 11:38:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1ea70e9b-6740-3654-9966-832c788bd685 | -12.61699 | -44.51771 | 2026-05-19 11:38:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 88343452-2f5d-3cfe-9c85-36fd33109cf2 | -12.06927 | -45.28029 | 2026-05-19 11:38:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 61f2c726-8319-3ad1-94fb-72e2a4d28e94 | -12.60667 | -44.52564 | 2026-05-19 11:38:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| f6d9b253-081e-39e5-9175-f25f8557c79a | -11.92876 | -43.41444 | 2026-05-19 11:38:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ed5954fc-0295-3a40-a293-02a16e2e6ac8 | -12.2226 | -44.25493 | 2026-05-19 11:38:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4db43bc1-aac7-35d0-9706-578537eae57a | -13.97684 | -42.68259 | 2026-05-19 11:38:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| dcfbbeaf-4260-32ee-96a7-5891da54f4a3 | -15.02751 | -45.12808 | 2026-05-19 11:38:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4e15512-0c59-3b7e-b949-0f603f66fd9a | -14.11899 | -42.11865 | 2026-05-19 11:38:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b4a93aca-c913-3dae-aabe-3c302d3c2a1c | -14.08117 | -42.12321 | 2026-05-19 11:38:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| f2dd046a-2693-307d-a68e-9242098efaea | -17.45298 | -43.64563 | 2026-05-19 11:38:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 6e2d4cb6-369a-3a58-8795-8398617d456e | -14.08247 | -42.11352 | 2026-05-19 11:38:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 789e89d2-a07a-3520-b676-2c925bd28e22 | -12.06777 | -45.2902 | 2026-05-19 11:38:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| e473556b-4b7f-3f9d-9a56-e513c639a4d6 | -15.54699 | -43.31225 | 2026-05-19 11:38:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 04df1f8c-673f-3e1c-a6ed-2955843739a3 | -12.61563 | -44.52698 | 2026-05-19 11:38:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 845d505c-2123-3489-be06-c66b96eb0712 | -11.93004 | -43.40548 | 2026-05-19 11:38:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| bcdfaf1c-eeb3-3026-ab97-e870f38952cc | -15.37771 | -42.87618 | 2026-05-19 11:38:00 | TERRA_M-M | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 667582ec-66a1-3676-bbab-e4ebe268024a | -11.9301 | -43.405 | 2026-05-19 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 0aa02cd3-7b77-3f0b-8737-98f621cc6b94 | -12.2215 | -44.2543 | 2026-05-19 12:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e1a4885d-2799-3e97-9c4f-60abfef196cf | -12.6011 | -44.521 | 2026-05-19 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| f29e1a75-8577-33fd-a3c0-720330f7f56b | -12.6011 | -44.521 | 2026-05-19 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 9b9f6301-e603-3741-9ad7-20dabfad24f3 | -12.6205 | -44.5179 | 2026-05-19 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e97d9ad2-a8d9-3aec-9460-0a2381673dc2 | -11.9301 | -43.405 | 2026-05-19 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 179f7573-ead2-36e4-98d8-5bf7ff208d22 | -12.2215 | -44.2543 | 2026-05-19 13:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| dd380427-70b4-361d-90aa-464cf4bed29f | -7.9148 | -48.2642 | 2026-05-19 13:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 4158f670-9bdc-31d0-bb7f-2fd63a2ea697 | -12.0682 | -45.2768 | 2026-05-19 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 4396f7d2-f711-33f7-8afd-38d9cb0ca416 | -12.6205 | -44.5179 | 2026-05-19 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 03b6ef6d-e41c-38ac-89a5-403cae0c834e | -12.6011 | -44.521 | 2026-05-19 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 8f3f426b-a670-382b-9b70-3e30bb2b28dc | -12.6011 | -44.521 | 2026-05-19 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| baccab2f-d6e3-3a34-aaf6-19b9c7c35e27 | -12.6205 | -44.5179 | 2026-05-19 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| a50e4f42-1854-3323-908f-650efa38c973 | -12.6205 | -44.5179 | 2026-05-19 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 2ada478d-9dc4-3f4a-aa93-db7202d36641 | -12.2215 | -44.2543 | 2026-05-19 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 27a62e9e-f2a2-34c5-9abb-3937e1418ccc | -12.6011 | -44.521 | 2026-05-19 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| b7dcd307-1b25-30de-adce-7104004e5838 | -12.6205 | -44.5179 | 2026-05-19 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |


[Clique aqui para ver as próximas entradas](README8.md)
