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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1738261e-ee8f-3e90-acc8-602e84003414 | -17.5338 | -43.7135 | 2026-09-30 13:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 98.4 |
| e54dd818-b868-3750-8777-cec66053acee | -12.4355 | -44.1262 | 2026-09-30 13:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 3bce05a9-674c-32d7-9d83-d14964c6870d | -6.895 | -43.7066 | 2026-09-30 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 2d86e000-5ed1-31f6-8292-5c5c26bfa97b | -9.9973 | -50.1393 | 2026-09-30 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| bda486cd-87bc-37b8-8e2d-3ac4e742d434 | -8.0355 | -42.866 | 2026-09-30 13:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| b73eadc9-acba-3a63-aa9e-cdd0cd17971d | -8.0169 | -42.8444 | 2026-09-30 13:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 243.8 |
| d09b940c-7d34-360f-80db-930a11f0d5a3 | -17.5137 | -43.7183 | 2026-09-30 13:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 134.9 |
| ae0d6245-5a8d-3719-a91f-e36b9e0ae605 | -6.914 | -43.6816 | 2026-09-30 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e4113aaa-294e-328d-b010-1a28960038df | -9.9215 | -50.1682 | 2026-09-30 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| e0b15cef-8cf4-3ade-bc93-02eb4d9cb778 | -7.0281 | -45.3008 | 2026-09-30 13:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 0773089a-4887-32f9-a188-dccb167f088d | -11.4311 | -43.4121 | 2026-09-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 792259fd-bdec-3acc-bdb4-5e942472765d | -11.6797 | -44.5012 | 2026-09-30 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 2151bb44-2300-3b7f-bb67-b69e12b37362 | -11.2095 | -45.1478 | 2026-09-30 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 262.5 |
| ed4f25f9-9592-37a7-8106-305bc71d7994 | -11.6605 | -44.5041 | 2026-09-30 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 8744eba1-72c6-3874-b178-167aadcdef4b | -12.4346 | -44.1733 | 2026-09-30 13:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| a0afb5b6-a594-3ea8-911a-05494b767a1f | -14.9802 | -46.5685 | 2026-09-30 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| a8ba12af-a842-37a9-bd88-41683f07544e | -12.8847 | -44.8015 | 2026-09-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 1f2ff06d-0b4b-3124-b338-3d273ac906a3 | -12.4351 | -44.1497 | 2026-09-30 13:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 208.7 |
| a7e5fc6d-e537-3fd9-9396-c470784aa905 | -6.9138 | -43.7049 | 2026-09-30 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| f2a269fe-9cab-39ea-b410-b7492f488c53 | -6.8952 | -43.6833 | 2026-09-30 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 325ad6bb-6270-3854-8949-b1ffaec971d5 | -7.0609 | -42.3274 | 2026-09-30 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 30159cf0-e16f-340e-aeaf-90e5af26a3d4 | -8.0166 | -42.8681 | 2026-09-30 13:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 272.8 |
| 15c25697-daff-3aaa-b399-15a2b1db824b | -11.4307 | -43.4358 | 2026-09-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.7 |
| f888685c-a7ff-3ec8-aa06-d157c431d3c7 | -8.0358 | -42.8423 | 2026-09-30 13:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| efbf8842-abec-34db-bc45-1081ff801f1b | -9.9396 | -50.2304 | 2026-09-30 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9a68c94f-77f2-33d4-8202-ad2d550e8903 | -11.4119 | -43.415 | 2026-09-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 196.6 |
| f5a77fee-fdda-3814-adf9-a05479b9547e | -11.1903 | -45.1505 | 2026-09-30 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| fa9e9ed1-26c4-3123-9124-037cc595b145 | -11.4499 | -43.4329 | 2026-09-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 5a1900b0-e7ca-3d6a-b139-d36c60aead1b | -14.7731 | -47.1515 | 2026-09-30 13:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| db550c97-7bb7-3a7b-a084-dba5eb0ed880 | -7.0612 | -42.3035 | 2026-09-30 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 5404fa10-5d64-3bc8-8ca8-dd4d4409ef45 | -9.9973 | -50.1393 | 2026-09-30 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c6c14998-1261-37ec-8584-e638ca0a7e5b | -8.0166 | -42.8681 | 2026-09-30 13:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 176.2 |
| 4916780a-90dc-300d-bcd2-76624aa5624d | -9.9784 | -50.1412 | 2026-09-30 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f7a95c0a-66bc-3626-992f-0b93aa23558f | -7.0612 | -42.3035 | 2026-09-30 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| a7d84643-ee67-3811-8a88-8cf9a3d91537 | -7.8297 | -45.8156 | 2026-09-30 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 8011cd58-ca2c-3887-9f9e-b48f1ed81577 | -11.1903 | -45.1505 | 2026-09-30 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| ce59ecfd-8597-3d3e-886b-db2427876df6 | -13.8784 | -44.4442 | 2026-09-30 13:10:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| d080a6fc-2734-3bf4-b2a1-d6f776e0a037 | -6.2217 | -47.4575 | 2026-09-30 13:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| ed6d2f82-e44b-3c62-861c-1ee99d8daa05 | -6.2219 | -47.4355 | 2026-09-30 13:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| e627f086-7450-3f9a-bc3e-d141b5339894 | -11.152 | -50.0388 | 2026-09-30 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 55be7799-4aa8-3c3a-97a2-798104a02097 | -7.0164 | -44.6413 | 2026-09-30 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 871974b7-c5b5-3047-a92f-e990f4071445 | -8.0169 | -42.8444 | 2026-09-30 13:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 143.7 |
| aca9b05e-10b2-3bf4-83ae-12919dd1f9c6 | -9.9215 | -50.1682 | 2026-09-30 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| b7da9412-20f9-3175-aa2d-fcad18e2c85b | -12.3744 | -46.3745 | 2026-09-30 13:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5e572f59-7f68-370f-99ad-3fe941982b24 | -14.1119 | -46.2604 | 2026-09-30 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 0cc636e9-b5f0-3dba-97a0-5973e2de3fab | -6.8952 | -43.6833 | 2026-09-30 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 0774ffbd-3e48-31da-841c-951c0a5eeeb0 | -8.2479 | -45.4583 | 2026-09-30 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| fe0b7eba-0336-37a8-9f73-489a6098485f | -6.9419 | -42.8598 | 2026-09-30 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 5f82b3a5-c648-3325-beac-190c7df3ddcb | -11.4307 | -43.4358 | 2026-09-30 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 247.7 |
| e91bb737-347e-3c89-a0d1-1160ef0e7b5f | -11.998 | -44.9177 | 2026-09-30 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 54ab428b-f4da-33a3-95ed-29dbfbd26d16 | -11.2095 | -45.1478 | 2026-09-30 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 42397eed-644b-3104-a3b0-06241817bdba | -6.895 | -43.7066 | 2026-09-30 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 138.0 |
| d92a47b3-d540-3895-b927-4eccab41475b | -12.4346 | -44.1733 | 2026-09-30 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 211.7 |
| b4e7d736-7071-3520-9040-672f41b61f6f | -11.4119 | -43.415 | 2026-09-30 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 277.3 |
| a2d5cb04-c1df-3d5e-a83d-3e71368e7215 | -11.4311 | -43.4121 | 2026-09-30 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| d8893f8b-593e-3d8f-b233-82eb963456b8 | -7.0074 | -43.7428 | 2026-09-30 13:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| efddf2d5-21ce-3b25-82d6-912df2132e14 | -12.4355 | -44.1262 | 2026-09-30 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 224.1 |
| f46599be-d3d5-35f4-ad57-98d37bfbfa39 | -12.4539 | -44.1702 | 2026-09-30 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 34531af4-bfd1-3b91-bdef-0684f55bb808 | -12.0662 | -46.4643 | 2026-09-30 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 8af918f5-b1c5-3b0c-bb80-cdf11ccf5cd9 | -6.914 | -43.6816 | 2026-09-30 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 5479f8a3-b7be-3924-9edd-785ffa7fdf8d | -9.8613 | -44.9577 | 2026-09-30 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8d5659ac-2d8f-3473-8349-0654aa56a5dc | -6.9138 | -43.7049 | 2026-09-30 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 5b6b605b-a0a2-38ca-9f6c-30afb129f4bb | -11.4499 | -43.4329 | 2026-09-30 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 235.3 |
| 10fa4ad5-3723-3c77-b1db-f308329968d4 | -7.0609 | -42.3274 | 2026-09-30 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| b9ea67fb-b30e-32b4-a5e8-9f2064726fe9 | -8.0355 | -42.866 | 2026-09-30 13:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 11a13a66-8da4-3d9e-bf0f-b1ea76d45886 | -12.4351 | -44.1497 | 2026-09-30 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 246.4 |
| e6337304-2d37-358b-885e-f7d64ed790ca | -7.61 | -44.58 | 2026-09-30 13:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 09f6ae37-9dac-38f4-8f8a-a4857c358646 | -8.02 | -42.89 | 2026-09-30 13:15:00 | MSG-03 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 66aa1147-0518-3628-9dcb-af5bd3c8d2a7 | -7.61 | -44.53 | 2026-09-30 13:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 293d5f50-23ff-3030-b885-1968e3dd6e21 | -8.01 | -42.84 | 2026-09-30 13:15:00 | MSG-03 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 33082696-cc89-35f0-a235-909cc2b9fd69 | -10.5197 | -45.3784 | 2026-09-30 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 3a3622c3-3920-36c9-9356-92b51e49e12a | -12.4351 | -44.1497 | 2026-09-30 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 262.9 |
| 2da32449-2f40-32df-b062-f08ce4f6cc3a | -9.9215 | -50.1682 | 2026-09-30 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 45ae026b-c9f5-3aad-b9ed-166ad087c7b5 | -17.5338 | -43.7135 | 2026-09-30 13:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 188.8 |
| d66ca91b-aa69-37a4-a1ee-495cd8f642a4 | -11.6605 | -44.5041 | 2026-09-30 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 0f271c53-c694-3da4-a434-9050df13f489 | -10.5166 | -50.8322 | 2026-09-30 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 04f0c8f1-a157-3b05-98c7-1980660a9079 | -11.4311 | -43.4121 | 2026-09-30 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 1c10116c-8a8e-329e-bfa5-c7551dff3074 | -11.1903 | -45.1505 | 2026-09-30 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 3c619369-474a-3ff9-8217-caa47a7d71cd | -14.3153 | -44.9052 | 2026-09-30 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 152d8038-2db6-3bf1-a674-bf5fd35f6e7c | -14.1314 | -46.2571 | 2026-09-30 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 9e6c9a7b-8825-3342-951d-5987bb12525f | -6.9419 | -42.8598 | 2026-09-30 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| d40bb4fa-4020-3564-b73d-893823a41cf3 | -11.4119 | -43.415 | 2026-09-30 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 261.1 |
| 902bf4a5-b3c5-3fda-8009-4e75c2e4e4bb | -6.895 | -43.7066 | 2026-09-30 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| b3905a75-1b9c-39ed-be33-26e2f9d75cfe | -14.9802 | -46.5685 | 2026-09-30 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 28234d73-5168-3f87-9814-b5ce6523114d | -17.5345 | -43.6891 | 2026-09-30 13:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 128.4 |
| e97bf6a8-67d1-35de-bf79-17e94748eb65 | -6.9138 | -43.7049 | 2026-09-30 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 24f47335-5034-3e37-8425-241735b2a0e8 | -11.152 | -50.0388 | 2026-09-30 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 44393a0d-fe3f-3aff-8de1-ebb6b8e48975 | -11.2095 | -45.1478 | 2026-09-30 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| a1e7e87b-1cdc-379f-baba-b668f8390ea5 | -8.0166 | -42.8681 | 2026-09-30 13:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 0024c82b-3e97-334a-ad75-497a4684de71 | -12.4539 | -44.1702 | 2026-09-30 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| bdddcbbd-aa69-3c5d-a605-4b8575f6eed3 | -7.0612 | -42.3035 | 2026-09-30 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 7a6f1ac2-2091-31bb-a3fe-c06a9bd032e3 | -17.5137 | -43.7183 | 2026-09-30 13:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 116.5 |
| d8854d52-ca45-3b52-98b3-2076ff62e9b4 | -12.6082 | -47.2429 | 2026-09-30 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7359719d-9f83-36e8-9fba-a07ea29e83d3 | -7.0074 | -43.7428 | 2026-09-30 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| cd29103a-faee-30b1-802f-9188165b1510 | -12.4355 | -44.1262 | 2026-09-30 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 194.0 |
| bd3e0df7-e659-39c2-b12a-fd9598468b26 | -10.1098 | -50.1921 | 2026-09-30 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 64daba9b-af16-3d09-a65e-8588b2b648cf | -14.1119 | -46.2604 | 2026-09-30 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 270.3 |
| 60a60e75-8b86-3e58-a0a3-df0dcb90fe6c | -9.8613 | -44.9577 | 2026-09-30 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 1d26cb02-8d25-3685-a25d-df095e015138 | -7.8297 | -45.8156 | 2026-09-30 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| d3d96eb4-3783-3a01-95c2-1e0d0bcafad0 | -9.9784 | -50.1412 | 2026-09-30 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |


[Clique aqui para ver as próximas entradas](README67.md)
