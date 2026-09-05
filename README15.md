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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78459594-6ea3-3121-a3c3-cc52fc448ffc | -6.17465 | -47.08737 | 2026-09-05 04:19:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d1361a9-fc64-37d6-add6-e69f56582de5 | -5.9259 | -47.89555 | 2026-09-05 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| a503d007-6fe6-33e7-ab77-e01b2996fc71 | -5.29458 | -56.00484 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf320d2b-c38d-3f9a-badc-a2f079af24d9 | -5.97078 | -43.62602 | 2026-09-05 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 765a71b9-210b-3d1f-8803-ef2af666e5b8 | -5.29117 | -56.02323 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7413f47e-7452-332c-8b18-86b2ede7181f | -7.72179 | -42.86204 | 2026-09-05 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aeb062a5-139d-3eee-90ea-0655b50e5222 | -5.77131 | -45.07276 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 4a79d34b-9bac-3641-b8b7-e795ad304a79 | -4.55925 | -47.76665 | 2026-09-05 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 245ce295-eebf-3186-ad9e-72cdb4ff9a61 | -5.3238 | -56.03567 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01491134-ed99-3888-806c-e2bceb12615a | -5.31367 | -56.01479 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2920bd6-d33e-3b7a-b7e4-2cdf3a19e77e | -3.6673 | -49.19072 | 2026-09-05 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ee9f257-e723-3860-b573-63c45e91e495 | -4.18032 | -42.44751 | 2026-09-05 04:19:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ca71ed86-8d1f-3909-b96e-e427db2e0e1c | -7.67176 | -46.06213 | 2026-09-05 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96705876-86ae-36b9-905b-d13e126fbc69 | -4.12474 | -49.4561 | 2026-09-05 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17e1a1a6-1d44-3216-80fd-9f135a6335c7 | -4.90439 | -43.47405 | 2026-09-05 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92d8b304-609c-3713-80ab-a22f4f5917a8 | -4.15867 | -49.70402 | 2026-09-05 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 68c50b16-93eb-3368-9a55-e37110f4a34b | -5.41107 | -43.25693 | 2026-09-05 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc63237a-04dc-3d0d-85ea-20d139e6954c | -5.41769 | -43.25798 | 2026-09-05 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d43cc423-bdfa-3f09-8505-9e95819250fd | -4.66154 | -55.64389 | 2026-09-05 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fccfd1f5-0626-39af-aef5-e125087f8e56 | -5.17023 | -56.06147 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 694312cb-e573-31e7-b7bb-507c7498a081 | -5.97409 | -43.62655 | 2026-09-05 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a417f2c6-40a6-308b-abac-7c08b2b2e651 | -5.30521 | -56.01095 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30b379a2-3992-37a8-809f-3b34d74bdeea | -5.31144 | -56.02693 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e76a7cb-b077-38c2-b8b1-9e8e4c15c8f1 | -5.33057 | -56.03683 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6bfb5c6a-82b8-316a-9040-12a511acf54b | -6.17091 | -47.08676 | 2026-09-05 04:19:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86c63849-3311-3f84-ac1a-45dde487376e | -3.2422 | -47.2509 | 2026-09-05 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc214907-dd34-3cb0-bb57-62e9545ba631 | -5.7685 | -45.06851 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 659a354e-a74e-35a9-8c18-118e8abd5c7d | -4.1015 | -50.4462 | 2026-09-05 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 382a2595-e9d7-3ab6-a634-8248f73b625d | -5.15259 | -55.95727 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1780faa5-2b6f-3402-b16e-f557a1d455fd | -7.45781 | -46.14894 | 2026-09-05 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c26bbf3e-a9f8-3a24-82a8-d9ad869b28b1 | -4.90107 | -43.47353 | 2026-09-05 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be01b5b5-330d-368a-8a66-20bc1b2e23a8 | -6.3581 | -46.1122 | 2026-09-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d400afcf-a5c2-33b0-b12d-3dee79c66247 | -4.43264 | -47.5414 | 2026-09-05 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fd7fba5-41b3-3411-9684-7cf6f548392c | -5.8505 | -52.04935 | 2026-09-05 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 928fe131-0c19-36d6-bed4-5a5d5c0f8806 | -5.96218 | -47.17742 | 2026-09-05 04:19:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ebe7caf-4e08-32c4-b1e3-c3ed724652c6 | -3.24614 | -47.25154 | 2026-09-05 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fdbdf16-b9fa-3e6d-8b99-c70ea16fbe04 | -5.32492 | -56.02954 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b25ff561-beb9-34ca-9ba8-b9cdcd637cad | -5.17059 | -56.05159 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf7cf661-a687-3b4c-8593-fec7dd5a1e70 | -5.30469 | -56.02565 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a33462a-fdcf-300e-b1c6-7767f6f4e04f | -7.14998 | -39.53648 | 2026-09-05 04:19:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 72b1c47c-c6e3-3fe6-8b03-06823e6be4e7 | -5.85216 | -52.03976 | 2026-09-05 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faafab44-7560-3614-9f65-0c1541027461 | -4.9077 | -43.47457 | 2026-09-05 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 825484cd-1c87-3edd-802f-a2e1b57100b5 | 2.38137 | -50.76141 | 2026-09-05 04:19:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f4bd4d38-f301-3916-a309-820947ffcf88 | -5.4238 | -36.76879 | 2026-09-05 04:19:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9a8b29d-7d21-31ca-af00-c8504fb8e0e1 | -7.48507 | -46.09292 | 2026-09-05 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56ead9fd-8930-351c-af80-069264b20531 | -5.14476 | -55.96205 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5abfe0d5-9e7d-3e07-9045-b44dc2cbda85 | -6.77501 | -46.46498 | 2026-09-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d184e59-0d2c-3af3-be53-f789aae96cc9 | -5.41823 | -43.25453 | 2026-09-05 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fbcae4b-6cb9-317c-bc5d-9f60fc5a2736 | -4.75539 | -49.27056 | 2026-09-05 04:19:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccdefb55-bcbb-3ba9-a63b-c506e9612b14 | -5.16909 | -56.06763 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b72a855d-ae2c-34eb-8654-224da0fc606e | -5.85513 | -52.05364 | 2026-09-05 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8e9d2a9-0420-3054-8dee-a2540f52dd2e | -5.33168 | -56.03072 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 114841b8-9810-3359-ab17-7a7ffb730004 | -6.72944 | -39.27398 | 2026-09-05 04:19:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7016c656-b6b4-3d30-ab06-8e1634f21eae | -5.29233 | -56.01699 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf192da7-5aaa-3e52-99c6-5c402bbf8a45 | -3.17696 | -51.54746 | 2026-09-05 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e1153d51-cbbe-3c2b-9c05-8be3e1b23c55 | -5.85105 | -52.04617 | 2026-09-05 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9391bb06-0cd8-301c-9140-fae8ca72676f | -5.83898 | -42.63388 | 2026-09-05 04:19:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8bcaf235-2854-3fd6-a19f-e03e86c7b39a | -7.70311 | -44.33199 | 2026-09-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85569d12-b1ba-3f4f-afef-3371e3dd8013 | -7.67616 | -46.07889 | 2026-09-05 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dfcf2e7-0a69-3691-9170-3972b69077a7 | -6.55895 | -44.77429 | 2026-09-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bbc472f-29b7-3117-ab5b-825ba99cae4a | -5.77071 | -45.07646 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d6c2624d-d81d-3ca1-afef-833f0b50d643 | -5.41052 | -43.26038 | 2026-09-05 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c493ea8-e017-373b-8596-995cd02887b7 | 2.37099 | -50.76659 | 2026-09-05 04:19:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| db5eddcc-9986-3917-95c8-128f37cffbfa | -5.76789 | -45.07223 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ffd95630-9d06-3494-8ee9-e65f4a50dde3 | -6.12648 | -43.75783 | 2026-09-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82e0ba27-234b-3ddd-91e9-543ac566332f | -7.69535 | -44.33794 | 2026-09-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aa94018-ef27-349b-8a20-2e47b76aaa38 | -5.33279 | -56.02467 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a7674bb2-b334-3838-ab74-d26f10bebaa9 | -4.17533 | -42.43612 | 2026-09-05 04:19:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0b67759e-5b82-3896-8c0d-29e88954277e | -5.30693 | -56.01351 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75f9fc0a-e778-32f0-89fe-0a4534cac804 | -7.45911 | -46.14109 | 2026-09-05 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11964a99-839c-3b47-8488-586b15f9567c | -5.92279 | -47.88985 | 2026-09-05 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 756adc07-a963-3ad7-939e-3342e90ad88e | -4.36551 | -47.77425 | 2026-09-05 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c63b2773-17d9-3f29-ad09-93995a57d097 | -6.12703 | -43.75436 | 2026-09-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a618566-1149-3876-8a8e-996936352e0e | -6.555 | -44.77736 | 2026-09-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0879fd8-a353-322b-8621-a47c085c32de | -5.398 | -45.14883 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e003b808-f4ff-334c-af2f-3aa6c4767874 | -5.31543 | -56.03196 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a17ab07f-aaca-3b00-9b4c-912e085033b5 | -5.34738 | -56.02111 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 757b6a46-a521-3377-9cd8-a5174f062b4b | -9.12338 | -44.28871 | 2026-09-05 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3480398-8b8a-3661-8746-6bcd32c06457 | -5.4901 | -44.3583 | 2026-09-05 04:19:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6be7f6e-96fe-356d-bd8d-1eccc823b9be | -5.49362 | -45.12111 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07203a2a-ab3b-3bb8-ad5e-5affdd6c2c16 | -6.34483 | -46.1073 | 2026-09-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e938a67-33fc-3f4e-b1a5-af14b5527447 | -7.5395 | -44.98661 | 2026-09-05 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5237bbed-f9c6-3eee-aee1-7d3872542fa1 | -3.4364 | -52.81256 | 2026-09-05 04:19:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1d1fc972-cb4b-393d-8634-cc6abb08b376 | -5.30412 | -56.01706 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d6ed637-11f0-3363-97c6-a3c0f9da937d | -5.2974 | -56.01567 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9391eff-39eb-3899-a2ec-e698f401a2da | -4.5407 | -38.45269 | 2026-09-05 04:19:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1db84ec9-038f-35c5-9df8-3ac4804e3b27 | -5.77192 | -45.06906 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| bb716ef6-eba0-391a-9549-3baf5b5ab216 | -5.41492 | -43.25401 | 2026-09-05 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26ea1473-1916-3ca2-8daf-6e2ea40eefcd | -5.17701 | -56.06271 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 141961b5-7f21-332d-bd72-091a1b500bd2 | -5.49019 | -45.12054 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4807bf0-de3a-39fc-a079-8a9e43b7de3d | -5.62488 | -44.95881 | 2026-09-05 04:19:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7e1a9df9-3a77-3f03-88dc-9ef7d22548a6 | -5.97354 | -43.63001 | 2026-09-05 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6329d5a-81ff-3ab9-99d6-787b63e7e0ff | -5.29347 | -56.01083 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e22b26b-0ea7-3931-b9b3-73cbad7a4dcf | -4.89813 | -43.2569 | 2026-09-05 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9aa2597-d306-30a8-af93-acf13632539c | -6.35418 | -46.11707 | 2026-09-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef8dd7c5-a4e5-37be-8704-30bf8f8f442f | -5.67447 | -45.30384 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd76bfc0-6a6b-37f9-9ec9-675fed74d548 | -5.31652 | -56.02582 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95be8c40-b9b5-3aa1-b80d-cbd71a4d6cb9 | -5.31194 | -56.01229 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 520d4b6b-0fbb-326d-8fb7-f6ed6155c616 | -5.29281 | -56.00228 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3bec485-0768-3d65-a0b7-ef0b6cd914ad | -4.18087 | -42.44406 | 2026-09-05 04:19:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README16.md)
