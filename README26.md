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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52052eaa-f9f7-3b25-bf70-d04f3f2943ea | -6.78009 | -46.45881 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2fd3ab1-714c-3789-8b44-e1a0dcde8fcd | -7.98892 | -46.19993 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b0dfd6ee-2706-3534-a2c8-147f3891f7f5 | -7.45157 | -49.40951 | 2025-10-28 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| e51f6133-3a6f-367d-add9-67af31e53aec | -6.648 | -44.59996 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5568fd3-5c60-3ec4-9951-5e4febce5705 | -9.59339 | -44.94056 | 2025-10-28 04:14:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75c9372b-de12-3d73-afa5-91519f456185 | -11.84963 | -43.92617 | 2025-10-28 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2069342d-115d-3bdd-be1d-6261c92f1739 | -6.14821 | -46.69647 | 2025-10-28 04:14:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4937dd43-1ba3-3482-b755-4fbff86f830b | -7.96448 | -45.45634 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3add28c9-225e-36a3-b7c8-9b71a7f3bc95 | -12.00723 | -46.78633 | 2025-10-28 04:14:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b1ac490-f0ee-3a03-9b1f-5ed6c14928f9 | -9.13723 | -50.70184 | 2025-10-28 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f321dc1-b472-304b-a3db-e32a5285adf4 | -7.95829 | -45.49456 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86fe5a24-b263-38a9-bf00-286df4c54529 | -9.21975 | -46.35627 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c38967f5-6903-3fff-953b-a68b38e088ed | -8.64341 | -44.77176 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8ddab5a-62c3-360d-9311-7ea1596114db | -7.69218 | -42.17923 | 2025-10-28 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c65fe85a-7c51-362e-989c-adfeff1bb214 | -5.61821 | -47.11016 | 2025-10-28 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb7c3e78-1c9c-39fd-8dbc-6387cc6869bb | -10.67572 | -48.0472 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16d0e119-c58f-34af-a6e2-0fdf02c3e258 | -8.13905 | -47.75298 | 2025-10-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9996e1d5-4db1-3563-9e45-c0b4db615db4 | -6.23872 | -42.56002 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1cb10464-3552-3367-b411-9aad6e5e0a19 | -7.81383 | -46.44904 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ba25527a-4dbd-381e-a129-0cf1e1c14bcf | -6.98833 | -44.00542 | 2025-10-28 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07a3fa43-72de-30c8-8dda-306f4cee6148 | -6.6866 | -42.04193 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f020c322-dca5-3615-8976-c2141997c65d | -9.54013 | -46.96286 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dda680f-850f-3f82-9ad8-c16466f08feb | -10.9263 | -47.61452 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd4d75c5-7ed1-3818-b7d3-5a642d9ff4d1 | -12.22103 | -46.49 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8041eb1b-6c16-3592-975f-1903478a0c10 | -5.30751 | -47.87661 | 2025-10-28 04:14:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99c1d4a6-1f8b-3b33-b0a0-38db0e8853b3 | -7.83272 | -46.401 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 65172414-467b-3425-991d-cdba5142e9d5 | -7.51633 | -46.29342 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67222fac-6b26-37b1-bbe2-720a67b62629 | -7.97863 | -46.28615 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66372b81-983e-3b55-aa0d-eacd4bf6b3ff | -11.56925 | -47.92039 | 2025-10-28 04:14:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33a6f482-8717-397f-8e78-5ba7f2bf873e | -5.30226 | -48.69796 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28f68258-6f9f-3389-a335-1a1c2d573ff5 | -10.91137 | -50.25658 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 741b3b28-1850-31dd-aa0b-5cdde0fac556 | -6.63347 | -42.23096 | 2025-10-28 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c703b5d-2d5a-37fa-a28d-c0b0018eae29 | -11.6471 | -48.529 | 2025-10-28 04:14:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88bfe713-6dc5-3c4c-b408-d14ec7f6f8a7 | -8.62993 | -44.79166 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed9bd235-78d9-326f-a435-0db6cfa13dfe | -11.28888 | -45.15131 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ab51861-0d4e-3b27-a4a3-d0aa291b931b | -7.95398 | -45.52119 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b14281d0-4d1b-3382-a6ea-fc6c6a8dfc53 | -6.69326 | -42.04295 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 95fe68e0-6dcf-3a37-81f6-b555e5176f17 | -8.62935 | -44.79526 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1494bb9a-12c8-3658-98fb-3d413dd74453 | -7.04388 | -41.64174 | 2025-10-28 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ae9c68e-c78b-3ecb-8fa1-f34e1853bf17 | -6.23512 | -43.32194 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 186996ce-4008-3947-b525-51ba260dd288 | -6.12922 | -42.69419 | 2025-10-28 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed623a0c-51f1-31f8-b56b-598738eb138c | -7.9896 | -46.19574 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d0c7df80-cd39-3caf-883a-074ad81fff80 | -10.83642 | -44.95691 | 2025-10-28 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c021489-281b-366e-8d1e-5010e249bfb5 | -12.24405 | -46.52173 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0088cf1d-3c37-3568-a0f2-30e107cbeea5 | -9.46158 | -47.7266 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d6be588-831f-3e70-81bb-cbc6271c9619 | -10.56156 | -48.99562 | 2025-10-28 04:14:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb74c93d-e4dc-363c-ad24-a5a96a5c5889 | -7.79156 | -46.44988 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e09029c-c1fa-3ec7-a86d-1b41585a2df5 | -10.63078 | -42.32124 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ae55131c-0325-36a1-b5bb-e40bc0489bf0 | -11.14206 | -44.94142 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| db47d819-c528-3b84-b272-2fcc981f9628 | -10.74338 | -42.69573 | 2025-10-28 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aee65427-174c-36af-9f88-fd4a17b278c7 | -9.59233 | -47.8508 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c64cbe9e-3c95-3d59-8abd-63be4c11044e | -10.55127 | -45.06002 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 174bed80-70f5-3563-8027-8ba29218599b | -8.17868 | -47.30671 | 2025-10-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f43e4b56-2f51-3225-9064-d3e2f7a636a5 | -7.83765 | -46.39329 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c857659f-53dd-30d1-9e13-e456a27db192 | -11.0753 | -44.52538 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 818c2962-d37b-3d81-85dc-1ca113494eac | -8.19488 | -44.4445 | 2025-10-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c56b9e62-fd6c-3cdf-adc1-91109f720260 | -10.07874 | -50.52917 | 2025-10-28 04:14:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f26d796-c221-37e9-8e9d-44b658b04b7d | -11.50751 | -44.00383 | 2025-10-28 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 846cb64a-9fd4-3705-99ba-1469e4d3e410 | -7.94735 | -45.49676 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d65ff67-3fb8-31c2-a125-1fe6954dbdfa | -11.10714 | -44.02161 | 2025-10-28 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de512cce-d333-3358-9245-42a086531f33 | -9.5618 | -46.96651 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| efc3ada2-74fb-3fd9-8fc7-d62a581a2d64 | -13.49072 | -43.93686 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2aaa560-41f9-36a6-821e-e526af8ec458 | -6.17094 | -41.83538 | 2025-10-28 04:14:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc30c229-37e3-3f81-a865-9ee8e29a17d3 | -8.19268 | -44.4369 | 2025-10-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 55d5dbc2-b0a2-317a-a71f-88ec20cf5b35 | -12.69944 | -46.3195 | 2025-10-28 04:14:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f1442b7b-be27-3d97-a6a0-eebd097363e0 | -9.57234 | -47.90211 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b26b0b0c-5cf6-3e77-ae59-1d9133875735 | -6.17014 | -43.12806 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e6f5949f-c0f4-3909-8c9c-53a50b207e87 | -11.05484 | -45.23093 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3204f14-326e-38d4-97e3-3c0e292f320d | -10.30107 | -47.21804 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7249ed01-886a-399c-9c09-893c03c6c09b | -12.85357 | -44.64394 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8c8b120-bd4f-346a-b48d-379c5a4b8b5f | -9.89007 | -44.89351 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b98430f-cfd8-3959-adfa-96a2c6880524 | -9.98485 | -47.15517 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da2936ea-4763-34ad-beb0-0bdb833ea02c | -12.24228 | -46.48974 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 383f99f5-ed30-379a-873f-ec3714f3c34a | -11.10723 | -42.71901 | 2025-10-28 04:14:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d4cd0712-f4d9-3003-81da-000c9efa83de | -6.93996 | -44.85936 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b1b0adf-6ad0-3d79-aeb0-37fdeb3c83a8 | -7.2615 | -45.00095 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1196f01c-b316-3f4b-b7ab-46df07b964d4 | -7.80697 | -46.49101 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6402b883-211d-38f8-8af2-75dedede8909 | -6.23925 | -42.55658 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a5db615-7a17-3270-a133-6d1a919011f4 | -10.63245 | -42.31023 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2b98090c-bd19-36d6-9098-3b6408df0c19 | -11.73528 | -49.33319 | 2025-10-28 04:14:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51c372a5-bfbf-39e2-9fe4-aa4d53aebbd1 | -6.4492 | -42.32307 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ceb1f645-e90d-3973-be17-9683d42cd163 | -12.43672 | -44.17591 | 2025-10-28 04:14:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e7ba7a9-e694-3bff-8572-6455d78d7a91 | -7.83787 | -46.41457 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c6c7ea3-fb21-3ba4-a1f9-72f0ad855b86 | -9.46307 | -46.88237 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5315383b-3a1a-3a1e-85a5-2885153385c9 | -10.29086 | -47.18994 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 971adf4c-5fd6-3195-aaee-ae594c3051a6 | -7.83002 | -46.41756 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 973b844d-df0e-3233-9c2b-a8014d8bc1b4 | -7.85979 | -46.39279 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19159229-57d8-3c17-88ac-0d1bb8a38527 | -7.64808 | -45.24056 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02431141-613f-3baa-8f77-f378e84e41dc | -9.56541 | -46.96711 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 954b50d2-867c-35b1-a97f-c66fd7902d0c | -11.7319 | -49.32888 | 2025-10-28 04:14:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dbb7399-7b3e-3020-94d0-6a2d1980bebf | -7.95028 | -45.54405 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a5078998-1f0e-303d-821f-11f6556624d5 | -7.83988 | -46.40219 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 69278cbd-5e98-3fe6-bccf-3d66233adc6a | -10.99891 | -50.3684 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 500d319d-f211-3c85-9315-aa0ff1075619 | -5.7012 | -49.19586 | 2025-10-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c893e52e-dbc5-3b2c-8dbf-9f47a0fed34c | -10.92206 | -50.2715 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 370764de-a8f7-3ff1-b38b-521a3bbd4309 | -7.07245 | -44.95148 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f17664b5-6f2f-353b-ab64-86e7405bf6e8 | -9.95784 | -47.07175 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a94896a3-81e2-3f8b-a109-f1252962ee5c | -9.64498 | -44.57382 | 2025-10-28 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bce7c2f-063c-3dc3-a007-bb8d0f7e0765 | -12.70251 | -46.3434 | 2025-10-28 04:14:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa95d830-8574-333c-925d-a3e94ce99a8c | -7.81108 | -46.46589 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README27.md)
