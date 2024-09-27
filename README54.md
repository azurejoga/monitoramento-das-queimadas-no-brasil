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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 444b9f1e-e748-39c2-a77e-ee3f5d4bf919 | -5.3989 | -43.43342 | 2024-09-27 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 24cf4b01-32dd-39c6-8c49-714eac5ebd4c | -6.05998 | -44.02744 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bc7d7a4f-9c30-3dd4-9f74-ae30953147d6 | -6.05518 | -44.02694 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a353d638-adf5-32b0-80d9-9666e141a69d | -6.05428 | -44.03217 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1c4ee9e-e1a3-30c5-9af2-407df4aab4b0 | -5.78889 | -44.14565 | 2024-09-27 03:47:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 283f6529-a602-36ab-90c8-b596b4ffdd90 | -5.76388 | -44.00596 | 2024-09-27 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac9554fa-413f-3095-8de5-f0e5da089452 | -6.58796 | -43.60822 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 523dc190-64f4-30b2-b973-a3d83e5d3890 | -5.98865 | -43.98396 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f656780-8468-3051-a446-0315b4fa724e | -5.40353 | -43.43412 | 2024-09-27 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 1276bdd8-251c-3e97-9f0e-c386ef56e55e | -5.40271 | -43.43896 | 2024-09-27 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| c00d7272-1fd7-3bdb-80b8-fa7173922335 | -5.39808 | -43.43827 | 2024-09-27 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 426f52b3-fe52-3c5e-8e8f-a9ad94336f2f | -5.57632 | -44.4169 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d9c581b-babb-33c5-a8c9-948e8549c50c | -6.38717 | -44.78828 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e4426eb-c049-39e3-a786-9d3844e8de44 | -6.3862 | -44.79398 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cdb654ed-e477-3640-92de-f0ec626a8c7b | -6.09911 | -44.70119 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8f1e5d8a-94be-3218-84ab-3e4e8a1c40c9 | -6.0989 | -44.70013 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0955162-10e1-3a1c-bf1c-5c494b3dcb8e | -6.09791 | -44.70601 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bacf72dc-08d5-39b7-b6d3-40d6bc6b894c | -6.09414 | -44.70029 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 91811ac6-443d-3128-80ec-4447122e868e | -6.09393 | -44.69923 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6050d66a-a1f0-3f2d-bc38-98e867ce9afb | -6.09294 | -44.7051 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51d66782-e4ae-3109-bf81-17d9b9c6e598 | -6.09002 | -44.72354 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23f363ca-bd9b-30b7-9e22-2ef8f1d86aa9 | -6.08916 | -44.69948 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ea3756e4-b0e4-3984-a463-0ef1a425e632 | -6.08895 | -44.69843 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9ea6a5d1-546d-3ac4-8cd3-6ec2ba796a25 | -6.08813 | -44.7053 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3fa62f6c-bdb6-3efe-85ee-27edd6869d00 | -6.08797 | -44.70424 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2228e63-dd38-36fc-8046-a7ffdb792250 | -6.08298 | -44.70343 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33cb1ecd-7303-3ecf-b2c8-f1ef5334818f | -6.08199 | -44.70926 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e35c662-bac8-3e85-8149-bd161abd50ce | -6.07701 | -44.70845 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 313938e3-f29b-3793-b2f7-b06ffb6a3013 | -6.07601 | -44.71429 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed333fba-03ea-3d26-8765-614b941394d4 | -6.07101 | -44.71355 | 2024-09-27 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 591805cd-fbe6-32b9-bb8d-96785199571d | -5.71361 | -44.81831 | 2024-09-27 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dd41398a-cbbb-38cb-87bb-99144d1d2332 | -7.35762 | -44.08814 | 2024-09-27 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac1d9d9a-8a26-3a7c-9637-51296c773331 | -7.0678 | -44.12053 | 2024-09-27 03:47:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 652458f9-8fd3-31a3-bba0-11a992ac8ec3 | -7.06391 | -43.93614 | 2024-09-27 03:47:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb12ff70-8fc1-3196-a4c2-027fef63d929 | -7.05841 | -43.9403 | 2024-09-27 03:47:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86d2c39a-288e-32da-bb2e-d06c561c4a0e | -6.87458 | -44.29383 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 488435fd-78f3-399c-8e25-084c2b911fed | -6.87369 | -44.29896 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8150a158-7a12-3ce8-b8fd-007d1d057aee | -6.57943 | -44.18099 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1dac2c25-5dcb-3a4b-bc61-5c474925d8ef | -7.80617 | -44.9111 | 2024-09-27 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bee5ec62-3a50-3758-b198-83780bf2286f | -7.80521 | -44.91672 | 2024-09-27 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40c02489-b15e-3a1b-977a-a7f3f4a33d53 | -7.80296 | -44.91183 | 2024-09-27 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28dd41dd-914d-317f-90af-9e1133e284f9 | -7.78071 | -44.9123 | 2024-09-27 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16dbc593-d48b-380d-95b0-8834c7feae55 | -7.74268 | -44.65011 | 2024-09-27 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1d2abe1-eb55-374f-97a6-29f72f74d8f8 | -7.74229 | -44.64685 | 2024-09-27 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4f5f14f-4d39-3e20-8d60-59a7eca8c13d | -7.68286 | -44.65123 | 2024-09-27 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7f3edd0-0f23-3da2-9604-45a8f43dc2a6 | -7.53658 | -45.01469 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2bb24005-0f16-3144-8036-f19cee51102d | -7.25301 | -44.96134 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8c662042-1d0f-3dad-922e-0c7124e29a80 | -7.25256 | -44.95947 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4e8d9624-438a-30e2-97a2-474c94284a13 | -7.25191 | -44.96749 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 78311f33-0b16-3414-ab05-6a157dd7d652 | -7.25156 | -44.96533 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1a560f27-d6f9-37fb-9c9f-5e26ebb6cadc | -7.25049 | -44.97162 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 76d0b90c-7b2c-3fae-b50f-ee8a3f355db4 | -7.24802 | -44.96065 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 15fee490-1738-35f4-ad37-d1230d39940c | -7.24757 | -44.95878 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e13ace20-33ee-3026-aeed-443895f5a045 | -7.24695 | -44.9666 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e35964f1-9176-3c30-9219-d6d7b81fe337 | -7.24659 | -44.96449 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ac90eeb4-5bb8-3b7d-8aeb-f1bdbc0225d4 | -7.22535 | -44.79328 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 680acb0c-f031-3068-bf74-df34ab061588 | -7.22044 | -44.79242 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fb2a9ff-c1ea-3016-9ef9-35e00f8d5485 | -7.21552 | -44.79161 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d769d51-27ae-3d55-8034-b9d06c93f0cb | -7.42252 | -45.16751 | 2024-09-27 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4111b037-abcd-3378-b7b9-27996452de9d | -7.42203 | -45.17036 | 2024-09-27 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab277687-c26c-34ef-ad0d-d0ccbade2a20 | -7.42203 | -45.16767 | 2024-09-27 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d78bd38-380f-3dc0-bf0a-f5b8fc7aca49 | -7.42152 | -45.17052 | 2024-09-27 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95f6b1b7-5690-33f1-a611-9f70d5a0b237 | -7.35297 | -44.08726 | 2024-09-27 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6575b546-c0bc-38b8-b29b-da8a72f53e4f | -7.35211 | -44.09221 | 2024-09-27 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90fcd810-f94f-31ad-917e-64d0f246e478 | -7.08356 | -44.19647 | 2024-09-27 03:47:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 393faa45-382d-3cf2-804a-7dbbc27cb98e | -7.07254 | -44.12113 | 2024-09-27 03:47:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22708d19-bc15-32ad-a6a9-b1a6cc77f906 | -7.07158 | -44.12656 | 2024-09-27 03:47:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3acf7e78-4499-3b83-8f71-1f2da9b07a45 | -7.07104 | -44.12045 | 2024-09-27 03:47:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13c020de-df2a-3558-8cc9-60cec3b0ceed | -7.05757 | -43.9452 | 2024-09-27 03:47:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf3b7ee0-e4b1-3f94-9fb9-c97aca3b5429 | -6.6186 | -43.92455 | 2024-09-27 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c17bca2a-f24c-3bbd-9e7d-536e27b9f73d | -6.87848 | -44.29972 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52e7415f-e291-3905-ad1a-7b28fb632831 | -6.86892 | -44.29814 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 40b78d91-08d1-33cf-ad92-1baf3053283a | -6.86803 | -44.30326 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc4dc446-f486-3e5b-aa89-c251e05608de | -6.86715 | -44.3083 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 577f7107-17b3-375b-ba53-b2ca2c3bdc5a | -6.86326 | -44.30239 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2177c733-38bc-3c37-ad80-bd3bb28a5e90 | -6.57471 | -44.17995 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 36ce2492-6a57-3cae-8641-41fefe4dd0db | -6.57086 | -44.17383 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 02667abc-3734-35a3-a897-1a1cf2103d07 | -6.56998 | -44.17897 | 2024-09-27 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1dab7bca-4d08-3dca-bbea-ada985d0f69a | -8.37153 | -45.38766 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c846a946-06e3-3f45-b8d9-7ba2cd9892e5 | -8.37096 | -45.39076 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0902287-15e9-3264-9522-54e3a0ab703a | -8.36548 | -45.39244 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46e4f397-d7b7-3746-a2d3-5008b58e2288 | -4.92539 | -45.67624 | 2024-09-27 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cc03683-d436-3c92-b4bb-b4fc69705a94 | -4.92482 | -45.6796 | 2024-09-27 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77e1c91a-4296-3513-a385-9c9b7ef1f941 | -4.61585 | -45.76687 | 2024-09-27 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7889670b-2bb3-39b9-97f5-77a75db60b37 | -4.61521 | -45.77053 | 2024-09-27 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51ad9a84-0b2c-3326-bcd5-2194acd7eda9 | -4.61503 | -45.76908 | 2024-09-27 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e790c60-ecce-3455-bb01-6d699a5663f4 | -4.61023 | -45.76413 | 2024-09-27 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b930ff15-3aac-348e-b6c8-1fc7fd2f534c | -4.60955 | -45.76815 | 2024-09-27 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6a0e240-6507-3188-90d5-5f7d24d5ee11 | -4.60892 | -45.77189 | 2024-09-27 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19809a19-37db-3291-b48b-680104a359d6 | -4.58309 | -45.69222 | 2024-09-27 03:47:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb5f4bee-5727-3858-86f2-0e6731fe4f85 | -5.19747 | -44.94187 | 2024-09-27 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2790fdf3-3e64-3af0-bd6e-104923ea69ce | -5.196 | -44.93798 | 2024-09-27 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcab6be7-0df8-3965-821c-fb9fbc8f240e | -5.1955 | -44.94096 | 2024-09-27 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f72d218c-5d9c-37a3-8ddc-c356b2e71c82 | -5.19285 | -44.93813 | 2024-09-27 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a05dab6-2740-35e8-a907-05e8d78ba5d8 | -5.19233 | -44.94107 | 2024-09-27 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93c260ad-e5f3-3e49-9cfb-9d2a257bdd58 | -5.70387 | -46.45623 | 2024-09-27 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ba8d460-5626-3836-a8a7-a224f2df5eea | -5.69828 | -46.45503 | 2024-09-27 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d304aa90-cf03-310a-9bf7-cb2eea4c994a | -5.50602 | -46.37656 | 2024-09-27 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1011872a-0ff7-3585-917b-1e884056d6e4 | -5.50265 | -46.37578 | 2024-09-27 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 924019f5-f6c5-3bfd-b783-25e1eb6977d2 | -5.50199 | -46.37966 | 2024-09-27 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README55.md)
