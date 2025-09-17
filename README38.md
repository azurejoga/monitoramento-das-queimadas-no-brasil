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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a33be3bf-b7af-3e24-98f3-2a33b3812079 | -6.87495 | -45.18667 | 2025-09-17 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82677fcb-c599-311c-b8ff-db7d851cefd1 | -6.09925 | -45.94234 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cc10f15-432d-3c40-8eb9-eab47645fad3 | -7.40371 | -50.00481 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e0e7791-4464-3fca-8b2b-86fcd22d8c87 | -7.52337 | -44.74202 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12b3d738-1cb2-3282-bc72-4b92f941aeec | -8.1685 | -46.76746 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcfcc7b5-c175-3d63-85a8-e0e4d5e677b3 | -8.4375 | -47.68504 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcf6f602-e13e-3bbb-a820-ad64b3d35d30 | -7.25253 | -46.61684 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c93e56db-462f-338b-939a-159f861b1c0f | -8.92243 | -46.27478 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e0102bb-b2f1-3813-8bfa-fc062b44afc3 | -7.48556 | -46.12606 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ea0355c-5951-35c4-9015-a9208dfa8b95 | -10.07439 | -48.18092 | 2025-09-17 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c74b7ca-6741-36b6-8a7a-230726d91afc | -8.96893 | -46.01444 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7349bd5c-74d7-3a21-9734-9ba3570d5bce | -7.68035 | -44.66771 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 780c2724-e4ad-3b85-ac64-a93d07120f5d | -8.95744 | -46.32273 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76a4c68f-2737-3639-9b74-9efb8e030161 | -9.16804 | -46.93469 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d94a3f1-c2f9-32cf-9243-a869bf5f2f69 | -11.376 | -43.68129 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61b468df-109c-3bec-8a99-13ff120786d6 | -8.12857 | -43.65417 | 2025-09-17 04:32:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eca1adde-afbc-3ec2-9c5b-20e891db9709 | -7.31021 | -43.96521 | 2025-09-17 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b10b06e-2cb2-324f-9f80-a7af6cb0cead | -9.10851 | -44.85242 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 16fceb4a-ef76-341b-be87-ada07f73c1c2 | -5.9871 | -45.85356 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d737d4f5-3838-3fcf-ab03-c82ac0ddfc1a | -6.39849 | -46.23057 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16138c5a-d7d7-3cd8-9463-857723fc051d | -5.80181 | -45.92009 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37fed103-fca8-3c75-85e9-7984ab18df75 | -6.3099 | -44.56017 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22138ff0-e68d-3f3e-bc4f-1dde0615e6fa | -8.65772 | -46.4045 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47720150-52e6-3aaf-bb59-4bbb6de3cc1c | -8.43473 | -47.68102 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5d8e04c-6062-3e9d-a0b3-674dc3786835 | -6.87957 | -43.97622 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7f40f75-eeca-3f1e-93a2-ec2aa608ea0c | -8.62746 | -46.44208 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d905d4f-f509-3114-9794-50014c0d1eb0 | -5.75998 | -43.70602 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a534bd3e-d6f3-3324-91b9-f87f459a31ee | -6.67672 | -46.30672 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dbb55b6a-bfae-302e-8958-af1f56bea76b | -9.08689 | -46.93712 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e0422af-0200-32c2-9f60-2255996caef7 | -11.33231 | -43.48047 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc8bef27-bc90-3d9c-9e05-476b8b57952e | -6.88472 | -43.96754 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c585f44-b068-332f-b98b-ae2ebfc23b4a | -7.07137 | -44.34594 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b87347f6-5cee-3de5-99e1-63c7518f5faf | -7.314 | -43.96585 | 2025-09-17 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b13fd9c7-8799-3b8c-95d2-5fea8423a52a | -6.17698 | -44.50263 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9378df13-3fdf-37da-8910-539977a921b3 | -7.72221 | -45.29395 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1db31e60-9066-316c-b81c-a7275a1060fe | -9.86216 | -46.44445 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c698d8e-9558-32b2-a427-3f5645875551 | -6.96579 | -44.54962 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e5862fb-0253-36fd-9fc2-aa94a8612f47 | -6.59263 | -44.32169 | 2025-09-17 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aa5b4c71-9c2c-3ae4-882d-29e44484a6e4 | -9.09027 | -46.93763 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daee0210-1c04-3909-ab92-142bcf3028b6 | -9.05519 | -44.83767 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9aec413-479b-30cb-ba02-f3b9c7320b16 | -7.57952 | -44.59236 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f14a545e-8bb0-3c16-954e-2797529cf43a | -8.22395 | -49.48433 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0a76564-e540-35ba-82ce-d2ec28686fb2 | -6.96047 | -44.53549 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7fc3122e-cefb-3f84-9021-3bbc5d86fa2d | -7.76771 | -44.73164 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21e69f34-cf5e-330f-bc41-7645b192cd99 | -8.0826 | -50.16545 | 2025-09-17 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3020eb6-ed3b-3640-887c-2cfd2135b59e | -7.39686 | -50.00372 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d13995c9-b880-32d5-9b92-c6ca3d3ef519 | -6.30233 | -42.39804 | 2025-09-17 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| be9fa323-b906-3df1-aa9e-f026aa7e0eaf | -10.88398 | -49.54716 | 2025-09-17 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6382c084-27c4-347b-95a9-03f6197de2b5 | -6.18842 | -45.11325 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50cf49b8-1428-3b3e-bba7-dc699bf69f62 | -10.39224 | -50.63047 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4605f937-e41c-3488-a8fd-772cf01b0713 | -5.56809 | -45.03149 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8779bd88-38c1-36db-99df-f8dcd7d514b3 | -5.52322 | -42.18163 | 2025-09-17 04:32:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b967beb9-53db-3836-b6c9-ffb18af7a30d | -6.41184 | -43.34734 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 27d77a82-da05-3688-b159-6d3aabd4ceb7 | -8.68052 | -46.36983 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4dce3f9e-d303-3580-b29b-4371507f6eac | -8.06852 | -49.96955 | 2025-09-17 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9454ae80-3930-3668-98ca-ca2ac9101b3d | -9.86619 | -46.44115 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99b69ca8-0820-3dc2-b900-f115bfe60ffa | -8.96112 | -44.19626 | 2025-09-17 04:32:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b56002a6-1076-3a2f-a3ac-bd66585bce9e | -9.60793 | -45.65891 | 2025-09-17 04:32:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8424bd7-e017-34b9-bf3e-83d468a4b2b0 | -9.09394 | -44.92651 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e2c4db6-6ae8-3bb4-b5ff-3efb4deb594e | -8.86892 | -50.13971 | 2025-09-17 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e7e1b586-5390-3c0b-ad7b-10e0af50aa17 | -8.51984 | -42.86943 | 2025-09-17 04:32:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db88bc0d-cda0-3fae-b851-e72bf4e29dd4 | -9.5451 | -46.29612 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6f4a3b8-13f0-3c9a-824a-028ef9ef24da | -4.92405 | -47.86845 | 2025-09-17 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d334004-a9aa-3928-9399-845581a3ac33 | -4.65011 | -50.91703 | 2025-09-17 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 613bcbed-e10d-36b1-8042-14371b2c6959 | -8.16567 | -46.76332 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ce6cc6f-61c9-36b3-949a-ed4d51715103 | -10.40128 | -50.63958 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e35a5b9c-4b43-3205-8109-f7d317709372 | -8.92131 | -46.23555 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0bb7b98-31d9-38be-bc12-518014d790c2 | -5.63155 | -44.82899 | 2025-09-17 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bd9715df-13d0-334b-a44a-9062c0f16dd5 | -9.09867 | -44.84221 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed9ee5fd-a494-3380-a52d-8c0b0ceeeb8b | -6.19426 | -45.12228 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fbac175-e619-36de-aa05-73ebce2bc917 | -7.5895 | -44.57608 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 420788df-d04c-3608-ad99-06e21dc7c308 | -5.63094 | -44.833 | 2025-09-17 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7918ed5-f8e4-3d2f-bef2-2a09da0f609d | -7.25702 | -46.61016 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58f22aa7-ef75-37b0-b954-ec056f8c792d | -5.77899 | -43.94313 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3bde252c-2d6c-33ee-9e16-4a38014871c7 | -5.88629 | -45.64414 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73398aac-6f4f-3da5-b2a2-1daf847d97d0 | -7.82374 | -46.15836 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f4a6364b-9f02-360b-989d-84c769084187 | -5.44786 | -46.67316 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d048218-31ed-356a-a2e0-e1061d965d54 | -7.32292 | -44.06215 | 2025-09-17 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 928a4e03-e584-38a3-8275-b5e817493a77 | -6.9863 | -44.61262 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2e747a5-3b64-3b9a-9459-c6af87fc97a9 | -10.77528 | -50.7121 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab633e73-e723-3629-8dc3-8a14aec424bb | -5.34723 | -44.82166 | 2025-09-17 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ac590bb-8552-356c-a75e-74cb6b56a37a | -8.99144 | -47.04112 | 2025-09-17 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59df08fc-4bc4-386c-87eb-08c95ce99e3f | -5.81673 | -46.36025 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d5b856c-ebba-350f-9bf6-397ccbd7754b | -10.29522 | -45.36234 | 2025-09-17 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3a22326-a12a-31f4-be8f-cb3ab2e1c4c5 | -5.7823 | -43.92087 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 16d8d0f0-602e-3db9-9ade-52d20fad0b9f | -6.39946 | -43.35031 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3aa4daa2-edbb-3673-8051-3fc8236f8df3 | -7.57372 | -44.5559 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c2494607-25a9-3ab2-abf6-556bf1454ba6 | -11.50352 | -43.63135 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 643ace8e-68be-3a51-add6-cf7866bdae3a | -8.67484 | -46.40722 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39da1510-24f0-31a6-b18e-f75f39eb5142 | -7.57781 | -44.57874 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f02f349-e30f-345d-af7f-96817bd1b74f | -8.98807 | -46.23817 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57c98882-5ec0-3bb7-a1ce-23bdc1bf9854 | -10.80634 | -50.65185 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3a63bcb-dc20-3a18-af06-7f2ca2a6c50e | -7.39626 | -50.00746 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c57b6df7-2ffb-3ec5-bf1d-a103695f9b6c | -11.12469 | -45.3559 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 865dbf6e-e058-3d8b-b265-7e5ab2329841 | -8.96254 | -46.00949 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c271b339-45b2-3dd2-bb66-155fd123b10b | -6.25402 | -44.68359 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bee40f3c-b0f3-34c4-a130-78a05c61ab28 | -5.95291 | -47.00644 | 2025-09-17 04:32:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce87ef14-d308-3b0d-9120-2d1c7fcd3d42 | -8.63947 | -46.40936 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a8fb713-560b-3dce-a546-b10f7dc08012 | -8.65716 | -46.40825 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ff32614-8b90-3969-89b5-29dcaff99412 | -7.83009 | -43.85349 | 2025-09-17 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README39.md)
