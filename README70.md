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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74a918bf-5297-3862-9f9d-24a1ce2768f5 | -11.1771 | -44.8064 | 2026-09-28 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 213.8 |
| 2ab4c256-e5bd-3670-a9fc-bdf4a7fc61b8 | -9.9396 | -50.2304 | 2026-09-28 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 467e7d34-db36-36f0-b9b8-c09ecee45576 | -11.5352 | -47.3678 | 2026-09-28 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 6d894d95-e436-33e8-8639-3221afcc88b2 | -13.161 | -48.5437 | 2026-09-28 12:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 97e4a366-22a1-3e0c-a5bb-fafe19a2224f | -7.3842 | -42.1039 | 2026-09-28 12:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 0f69c5de-849f-3418-80b2-5f88e3df89ba | -8.3611 | -45.4468 | 2026-09-28 12:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 19781d93-c93a-37f6-8630-ae508e6eb8a1 | -11.1966 | -44.7805 | 2026-09-28 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 6101eebd-8219-38bd-bffe-89b6858f00f1 | -11.2154 | -44.801 | 2026-09-28 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 3056f7cf-20a5-3538-ab18-199f7454847e | -12.6832 | -47.3442 | 2026-09-28 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 5353b884-ea02-3bba-b3ba-61cb1aac6968 | -8.3617 | -45.4013 | 2026-09-28 12:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| eb226063-2950-3fb4-968a-611a086ee926 | -11.2158 | -44.7778 | 2026-09-28 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| d3880db4-01a4-3a4c-8395-d5fe969ba478 | -12.7024 | -47.3414 | 2026-09-28 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 34e6ddd6-eb77-3741-9b6c-5f4a1261421a | -11.1962 | -44.8037 | 2026-09-28 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 77da40ec-a060-33a3-ba1d-ffd20f449f0a | -15.1847 | -46.141 | 2026-09-28 12:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 163435cc-8707-31ee-954d-37114f858047 | -11.1775 | -44.7832 | 2026-09-28 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| eecf3463-86d8-3c7a-a917-19e6b07d6bf8 | -12.6263 | -47.3075 | 2026-09-28 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 5f0cb769-dd4e-37cd-a5bc-b4c74fedfbad | -12.6836 | -47.3217 | 2026-09-28 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 416.7 |
| 0db0bc19-eefa-31c7-acef-fd32c0cf20fe | -8.2859 | -45.4317 | 2026-09-28 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 23db36d4-0044-32c7-8841-e42529f1caca | -8.3666 | -46.5263 | 2026-09-28 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 15a82bfb-9154-357e-9a49-5e639386a54c | -11.1327 | -50.0624 | 2026-09-28 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 412cfbc4-d594-39c4-8e45-840265e9c793 | -12.7028 | -47.3189 | 2026-09-28 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| c425c2c6-6a3c-323c-8c36-5286c6292a15 | -11.8641 | -47.1004 | 2026-09-28 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 0ca1a31a-c6ff-39b8-a2a5-d6007c897734 | -8.2862 | -45.409 | 2026-09-28 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| e1b483f7-57bd-33c6-bf79-f8071ae4a7a6 | -9.9784 | -50.1412 | 2026-09-28 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b7776c38-adcb-3745-a349-285c35a11102 | -12.6643 | -47.3245 | 2026-09-28 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 216.3 |
| de6eabbb-ccc1-3b99-bd83-9f1c6bd25bc1 | -12.6832 | -47.3442 | 2026-09-28 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 304.5 |
| 71ec94f1-7a4d-3c47-a284-fe5672233b1d | -13.161 | -48.5437 | 2026-09-28 12:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 00512505-0e16-3d24-874f-41b6ddd9e55f | -11.3962 | -45.3973 | 2026-09-28 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| f33af9bb-5f1d-38d8-8a88-4da8136936a5 | -12.6263 | -47.3075 | 2026-09-28 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| ad001bef-748b-3ac1-a041-64288ea24c46 | -12.7024 | -47.3414 | 2026-09-28 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 7aab09b8-13ad-33f5-a332-9ae463286ddf | -16.6932 | -50.6608 | 2026-09-28 12:10:00 | GOES-19 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 133bf793-cca1-3612-b612-8f7a4a933b28 | -8.3608 | -45.4695 | 2026-09-28 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2f1fdd84-2299-397a-a753-dac97d7281c7 | -11.4616 | -44.9276 | 2026-09-28 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 2452e345-96ca-308d-8de6-9498b4ff5552 | -9.9396 | -50.2304 | 2026-09-28 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 47248359-85ee-36d3-8aca-194a0e3231a2 | 1.68102 | -55.96599 | 2026-09-28 12:19:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 49171bf3-0d24-3fce-9a68-7689f8f3901b | 1.48197 | -55.72157 | 2026-09-28 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 19a4a07f-a7f3-3953-8bea-cbbb15d0ad15 | 1.62675 | -55.9014 | 2026-09-28 12:19:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| eac94c89-a5e6-3978-a14b-458b2d140892 | 0.63326 | -54.38046 | 2026-09-28 12:19:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 5e1bf49c-8183-3264-ba7b-9b85f0c2c67b | -0.44501 | -52.02036 | 2026-09-28 12:19:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| dc7ad12c-80eb-3189-b311-fe1bfd8e9251 | 0.63198 | -54.37141 | 2026-09-28 12:19:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7da30754-38ce-3834-aae3-fa6fa1f6e894 | 2.8665 | -51.14596 | 2026-09-28 12:19:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 34.7 |
| de2e73e5-739d-3867-b503-d80852d6ecc6 | 1.66586 | -55.92301 | 2026-09-28 12:19:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a66ecd70-775d-3e09-965b-fa5ba67c5133 | 1.67975 | -55.95714 | 2026-09-28 12:19:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2309ae5c-120c-36c7-8f75-618a2f64167e | 2.38521 | -51.00778 | 2026-09-28 12:19:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 281642f3-92d1-3b69-9fbe-de2880253232 | -0.44329 | -52.0327 | 2026-09-28 12:19:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 20.0 |
| b20396bb-59e6-3236-b0dc-91fb2a71f7fa | -10.8967 | -50.6866 | 2026-09-28 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 49ee4c6a-9450-3fe9-8cfa-fd9b9cfe61da | -8.2862 | -45.409 | 2026-09-28 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 172.7 |
| cdec1a26-cd5a-34b8-b201-1ef3941d3306 | -12.7028 | -47.3189 | 2026-09-28 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| c7b9d93c-8e0c-3704-81af-3ac656f7194d | -8.2859 | -45.4317 | 2026-09-28 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 42d0944e-4fd1-39a5-addf-25e2ef422fd8 | -7.3842 | -42.1039 | 2026-09-28 12:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 338d1ddb-64d9-3693-a8af-c414f15ed604 | -8.3608 | -45.4695 | 2026-09-28 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 2339df99-7566-3a3e-9b2e-f0bb0a3123dc | -10.9349 | -50.6612 | 2026-09-28 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 82b22ab3-dda8-3008-85bd-46c2889e54c3 | -16.6932 | -50.6608 | 2026-09-28 12:20:00 | GOES-19 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 6657c77d-da40-341e-8347-ba3d74f36fb0 | -9.9784 | -50.1412 | 2026-09-28 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 96a2c6c1-101e-3814-b0f9-c80cee847229 | -9.9781 | -50.1626 | 2026-09-28 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 10c44361-d08f-305c-a33e-0da618623dd1 | -12.6878 | -45.0192 | 2026-09-28 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 3ace0a0c-b090-3e28-85c2-169115436647 | -12.7024 | -47.3414 | 2026-09-28 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 180.5 |
| f1eb2667-5771-39a9-be76-8cc36039ee4d | -11.3962 | -45.3973 | 2026-09-28 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 186.8 |
| b2649240-f234-3ff8-a1c1-6bbcd1af5e94 | -12.6832 | -47.3442 | 2026-09-28 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 234.6 |
| c4120f07-998e-3313-88d3-649d68140134 | -7.0547 | -42.8726 | 2026-09-28 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 1388b881-4a1b-3589-9670-6ede79e62fdf | -11.1327 | -50.0624 | 2026-09-28 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 301cdaba-d3ce-38d3-8b69-3991ccc5945f | -9.9396 | -50.2304 | 2026-09-28 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 504eb088-3da9-3378-b518-7c373e5c9d8a | -11.5352 | -47.3678 | 2026-09-28 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e0463e08-a735-34ac-a9bf-ce3a5e3b1eb1 | -8.2293 | -45.4375 | 2026-09-28 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 4d478486-80cd-35dc-ad49-bc89eee35af8 | -9.9393 | -50.2518 | 2026-09-28 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 2c2f3ff3-0000-32af-87a7-0bde2152a061 | -11.8641 | -47.1004 | 2026-09-28 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 399a861d-91f8-3ffa-9df5-097c87d7954d | -11.4616 | -44.9276 | 2026-09-28 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| b34e45ec-8333-3081-bdb9-8e70278864c3 | -13.161 | -48.5437 | 2026-09-28 12:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7bf3ec73-6089-3c7b-a1a8-ee295819405c | -8.3666 | -46.5263 | 2026-09-28 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 834218bf-5af9-30f9-a782-a82743670cc9 | -11.4425 | -44.9303 | 2026-09-28 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| fef5a3c8-206b-3375-96b9-463e128b637c | -8.3617 | -45.4013 | 2026-09-28 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 8c361b27-e7ab-3b19-a532-767c4dddd420 | -8.6631 | -45.4152 | 2026-09-28 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| ddbc4962-d6e6-3a87-91e4-3a68f2701d79 | -12.6263 | -47.3075 | 2026-09-28 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| e766a85b-3316-3ba9-960a-05baac5e28f1 | -12.6643 | -47.3245 | 2026-09-28 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 754da2e6-65ca-3fe7-9d6b-ed6d013cf16a | -8.2291 | -45.4602 | 2026-09-28 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 8cdd8e0e-375f-3adc-876c-cd390733bbc6 | -12.6836 | -47.3217 | 2026-09-28 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 260.6 |
| ee211a23-2632-3cae-9be2-07bc56d7b9e4 | -2.67811 | -56.46293 | 2026-09-28 12:21:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a45d6b3-9b4f-339d-b054-c1774ac21767 | -7.86813 | -54.70323 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d4ec3817-fd7a-3fda-b8f8-0ec03cc48dc5 | -1.03586 | -53.72845 | 2026-09-28 12:21:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9d44916f-2bb6-3673-9188-072446b8d05f | -7.82742 | -55.13467 | 2026-09-28 12:21:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0b44477e-f759-3f1b-bb64-7abe3507bb96 | -6.66136 | -55.09303 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 64427d20-4a39-306c-a2b0-80c8c825ead4 | -7.71817 | -54.77216 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 54a1a38a-6d2a-33b3-89d9-79a57fa89d4f | -6.16227 | -52.89636 | 2026-09-28 12:21:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| aeec396f-a189-37c4-8aad-288b4ba85062 | -7.77719 | -54.69517 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cb4e43fd-01f8-3e93-b39e-681a1b265f3c | -6.66002 | -55.10275 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2022f2c6-13d1-32ef-87c5-b5dc4b896449 | -1.09607 | -53.70588 | 2026-09-28 12:21:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8f77d3a7-fbf8-3712-8852-7210d1049719 | -7.68808 | -54.85215 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1adc4038-8e82-3b06-8c6a-cdce20203c7f | -7.48162 | -54.97153 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 629a5942-9ba9-37fe-9316-b048d2f90816 | -8.03526 | -54.89669 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ef9d6a6c-8263-38f1-9029-76e74f11d9f7 | -7.67892 | -54.73979 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| bd112f20-01bd-3c06-9d03-e2d3fd709093 | -1.23434 | -54.09386 | 2026-09-28 12:21:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 851a5c07-0d37-39bf-b41f-2f26bec1ed44 | -7.86959 | -54.69264 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0456dfc8-b30d-3a4d-a711-625fc56ddb52 | -1.97535 | -54.26014 | 2026-09-28 12:21:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 940a1ae9-4115-34b9-a631-16ebe5c4f3bb | -7.68213 | -54.85576 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| efeae3d7-f253-3456-8a5f-310bffba75b6 | -3.83567 | -55.90519 | 2026-09-28 12:21:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cff1d4ed-38c5-3b33-9c67-b03186f3ea40 | -1.04895 | -53.56652 | 2026-09-28 12:21:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7bc23a65-9abc-3825-9235-434b6e39d227 | -1.9767 | -54.25053 | 2026-09-28 12:21:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| cf2e7faa-9c99-3d20-8f42-52dd06e42067 | -1.05036 | -53.5564 | 2026-09-28 12:21:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e49470ea-9da2-3b97-a9d7-25d798026125 | -6.00849 | -47.3782 | 2026-09-28 12:21:00 | TERRA_M-T | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 9cc1c5f5-b6f8-3c58-a7d0-5ae4062c5250 | -7.68355 | -54.84557 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README71.md)
