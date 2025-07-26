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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59e85894-b302-3715-8d06-ab4a3caa4fa2 | -6.92989 | -42.80624 | 2025-07-26 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c25f72f9-e2ac-3c45-aca4-95871837953b | -7.56454 | -44.48908 | 2025-07-26 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc152391-9bb1-3677-a2e7-552d1d954ab7 | -6.86789 | -43.68511 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dc056641-c857-3fbe-b587-83299cd75672 | -7.53605 | -42.42451 | 2025-07-26 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 342f4491-9886-3ec0-b488-3184e820713f | -6.86313 | -43.68417 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90ad9588-08da-3800-86a1-0bdd4342653d | -4.61672 | -43.32682 | 2025-07-26 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5a221f1-f984-3eef-af26-5376e72b46f4 | -6.86936 | -43.68127 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f4682fe-a390-3c4e-b83e-6bc670fc8a6f | -8.17381 | -43.22884 | 2025-07-26 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 22d31747-68d5-35d6-a4ad-5c47c36008d0 | -4.77641 | -45.33861 | 2025-07-26 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c7da2e7-9bc8-31fe-90ea-471d6cb995bf | -6.88653 | -43.11059 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae54aa48-7a2e-30a2-9dbd-1b0569c0d15a | -4.0783 | -46.90551 | 2025-07-26 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9737f6cb-7eee-3635-ba0d-d7608aa3340f | -4.07125 | -46.9043 | 2025-07-26 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac1f31d3-abaf-345a-b9b1-016dd215f6e0 | -6.92998 | -42.80837 | 2025-07-26 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1704df90-ca6d-344a-940c-c2292cd28818 | -5.76936 | -43.64437 | 2025-07-26 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50ec55d5-c23d-36c9-a9ac-4c098dac72ea | -6.7772 | -44.10565 | 2025-07-26 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75ffb53c-b08f-34c1-b673-f8ef757257aa | -6.8805 | -43.68286 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 168a3d70-821c-3714-a5ab-400419ea671c | -6.87278 | -43.68962 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7f2beac5-c229-393d-9157-33f18aa087e7 | -4.77449 | -45.33647 | 2025-07-26 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b770f412-394f-3c6c-b88f-0d459f14781f | -6.86857 | -43.68142 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab31236c-3ad4-305e-93d9-aedc95096206 | -6.15134 | -42.59451 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| f6556ee4-68ac-3ea3-88ad-85f480892ac3 | -6.78359 | -44.10276 | 2025-07-26 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fcb9348-20be-308c-9c12-5e6b1467d42b | -6.33007 | -44.09771 | 2025-07-26 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c2d1f09-23cd-35c9-93e8-dd73c2f9339b | -7.25074 | -43.07076 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 44bfdd7e-1ad9-32e0-ab8f-536d7d41a23f | -6.87481 | -43.67851 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f5f84c9-628c-3529-a333-715665aab883 | -7.57031 | -44.49012 | 2025-07-26 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3362d61c-e497-3437-a3ad-bf23118ab9e6 | -7.24016 | -43.06895 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 4ee463bf-7f03-39fd-bfd4-ea33ab70f7ba | -7.24958 | -43.0773 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 67b55163-2354-3520-a848-e990db93043f | -7.19443 | -44.02003 | 2025-07-26 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4f8cb9a-e6d0-3e6b-ba23-1c5ff43e2b1f | -6.88038 | -43.67932 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b52002c7-1299-33f8-9215-db003084c372 | -6.87549 | -43.6748 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa96e60b-083f-3642-b230-8a6764a9afee | -7.17571 | -43.49094 | 2025-07-26 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe69d02f-4134-3143-86ce-8725e28df4ed | -5.74332 | -43.96861 | 2025-07-26 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c409941-9a08-39cb-8034-031a796a0afd | -6.87347 | -43.68586 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e7f99520-afc5-3f90-b3a1-60ee51d614dc | -6.87414 | -43.68218 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5e96271c-7f47-3ed8-810e-4d33bd838afe | -7.23838 | -43.07887 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c1e67b59-1910-3a32-9d51-bfc641b05312 | -6.22951 | -44.5264 | 2025-07-26 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4b9947cf-a781-34d9-a2cf-1e3aa8dfdc87 | -7.02884 | -37.24448 | 2025-07-26 03:36:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c01e3134-23d5-3491-9eec-32f2c83268d3 | -6.70586 | -43.06621 | 2025-07-26 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 93407ec9-2e31-330d-acca-7050472efc2d | -6.16068 | -42.60265 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6ee39553-bb0a-33ea-adb3-16b9a03b42d9 | -7.79283 | -37.59729 | 2025-07-26 03:36:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 49bf7cde-6173-34a8-85fe-8d68c64b5006 | -4.07601 | -46.90456 | 2025-07-26 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fbea20b3-7f86-3aa6-b82f-5dbb45b548f5 | -6.87001 | -43.67756 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 52fa5950-c1a5-3cd2-b134-4d17abe95829 | -6.86299 | -43.68062 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f96418f5-0725-3ec8-99f4-9f69a4a488a4 | -7.78845 | -37.60104 | 2025-07-26 03:36:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 80387ce6-5de1-3c13-9724-5bbbae30068b | -5.48684 | -42.15482 | 2025-07-26 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a9c29fcf-8c65-3053-900a-3a9db8113eef | -6.93055 | -42.80521 | 2025-07-26 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ec4160d9-6184-34c3-b613-058be63283c4 | -6.98929 | -47.08423 | 2025-07-26 03:36:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8eef4461-6f15-3095-8653-9795d3e1db14 | -6.23026 | -44.52221 | 2025-07-26 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1dffc834-4a79-35e1-a11c-ee5ee40d5eb9 | -6.88949 | -43.12477 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d893e53f-33d1-3119-9d71-d8306a2d73db | -7.24428 | -43.07643 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 09c803eb-002d-3e51-9c12-d38f000ae4b4 | -6.56713 | -41.50094 | 2025-07-26 03:36:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 22b47a33-cf6e-3d51-b459-52fa7185f548 | -7.23898 | -43.07553 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 671c989a-c812-3db9-a89d-70d16b08ba80 | -7.23486 | -43.06805 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| d2704e38-e302-3cbf-84dc-2010823e1930 | -6.14611 | -42.59369 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33dc3237-f27f-3c33-b30a-4d28929dc931 | -8.17623 | -43.21553 | 2025-07-26 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8c5e6f45-844e-3372-86fd-2b54cee2786e | -6.87363 | -43.68949 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 83bbc6d1-2bda-3452-81f0-a632fa3a91e7 | -4.61802 | -43.31925 | 2025-07-26 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| daae06b3-2c74-387a-b882-c11dc5ca7cab | -7.24545 | -43.06985 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 049729f4-8593-3629-9360-d5a73ba6eb51 | -6.87429 | -43.68574 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a292ca3d-3ce4-3edc-981b-0a071c936796 | -6.86924 | -43.67771 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32540883-9d4e-30b6-a86b-11dafa4f0d90 | -6.78466 | -44.10685 | 2025-07-26 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 151cc9c5-6f89-3e02-902a-eeaae2e690c9 | -8.17098 | -43.21458 | 2025-07-26 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b49470b7-4025-375e-a34b-8a9102f0e792 | -6.88593 | -43.11393 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48ead36d-a78d-3b14-874e-7932272e0276 | -6.15659 | -42.59528 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a7624094-db82-3f28-8da8-8cebfe433c59 | -4.6111 | -43.32583 | 2025-07-26 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37485c46-b7b7-3421-b3be-5441fb12a482 | -6.87972 | -43.68295 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4a4975f3-59e4-300d-9a08-84a7c2528dda | -5.48225 | -42.15083 | 2025-07-26 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 90ce1b7b-d69e-3e9a-84b6-74869f396932 | -7.78915 | -37.59671 | 2025-07-26 03:36:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a4109afb-6d12-3602-8114-1fd40be21656 | -4.61737 | -43.32302 | 2025-07-26 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd3f165a-62db-3165-a78f-101d3bead889 | -6.15079 | -42.59771 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 06cb00ee-206d-3576-a61c-edf62c9b4b0c | -6.86806 | -43.6887 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef87e8e7-d147-364f-89b5-2fa19dcb8416 | -6.9139 | -38.56285 | 2025-07-26 03:36:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 548f9fd2-6398-3412-8292-dbce3e49bf61 | -7.23544 | -43.06481 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0355b0b5-fd9b-3fb9-859e-ee565782eec1 | -8.17564 | -43.21881 | 2025-07-26 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bc7210e5-b137-3a04-b83c-1319197f897c | -6.22354 | -44.5257 | 2025-07-26 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f995b54b-95ad-38f8-8052-c872f8dfcd85 | -6.90475 | -44.29911 | 2025-07-26 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7614adef-3399-31cd-968b-8d649a57d821 | -5.48736 | -42.15178 | 2025-07-26 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9711a51b-d799-33e9-8054-b2139967096e | -7.50379 | -37.36776 | 2025-07-26 03:36:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b1dea638-f088-3258-aca8-5cedb39c554e | -6.88534 | -43.11721 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d748b7c-fe75-35e2-8353-5bb5905f4084 | -7.79212 | -37.60163 | 2025-07-26 03:36:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ded5cd23-354c-3605-95ac-cfbf79f85bb9 | -7.23428 | -43.07133 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| aa4f3393-5140-3070-a64a-3fa2a06d4b0e | -7.1937 | -44.02407 | 2025-07-26 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a7abf95-4389-30bc-96b4-4af2ebb69726 | -7.24368 | -43.07975 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 827c6aa9-633a-35cc-8a02-fa8e946ec882 | -6.56231 | -41.50017 | 2025-07-26 03:36:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 73c79bca-2d86-3178-8394-190be9d6371d | -6.93569 | -42.80658 | 2025-07-26 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c5253cbb-a90f-334e-b3c8-2ebe5affc0ff | -6.89009 | -43.12141 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d5e033c-5380-39e4-9566-e3c8cf4e1ddc | -5.73683 | -43.9664 | 2025-07-26 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da3eb954-b849-31a1-946c-0a7b5f621262 | -7.82697 | -35.24562 | 2025-07-26 03:36:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 04f7ffd6-7919-36eb-b328-9f062aa604b3 | -6.16125 | -42.59935 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bc314126-1d7a-3209-b5ee-c28d00b3b454 | -5.73833 | -43.96344 | 2025-07-26 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5710ca54-0971-3c1a-b3f0-645e3137d08b | -6.87558 | -43.67837 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61f86a12-a887-34fe-88d5-be050e024140 | -6.16182 | -42.59606 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| fb24d5c4-a51b-3534-9e44-9cf36534ae57 | -5.74259 | -43.96732 | 2025-07-26 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07f80b71-b3a6-3582-bdcc-6ca4574a6d9d | -6.70645 | -43.06289 | 2025-07-26 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b6a56b13-c6c3-3501-bec1-7b3a01cc3bbd | -5.73757 | -43.96214 | 2025-07-26 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5316870-d123-35af-bcee-219d8823d52d | -5.74409 | -43.96438 | 2025-07-26 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cd273db-4243-36cc-b6e0-19b20440d9e4 | -6.06792 | -43.6529 | 2025-07-26 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2837bc6d-5b98-3cca-8d9c-cf3c30cb7ae1 | -3.82489 | -41.57699 | 2025-07-26 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 18fd4e45-ee8f-39d6-bb38-2c25f51ee056 | -3.81285 | -42.55158 | 2025-07-26 03:36:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac2d790e-eff6-3234-bd30-cc400eef832d | -4.76074 | -38.48462 | 2025-07-26 03:36:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README5.md)
