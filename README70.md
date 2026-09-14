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
| 566727c5-39f7-364b-b95e-b355c3d7cea9 | -11.2391 | -43.4413 | 2026-09-14 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 1b1aa7ea-e689-3e22-a250-fd2b1165474e | -4.1333 | -60.6882 | 2026-09-14 13:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 42c510d5-1840-372c-9227-156d375e68b0 | -9.4513 | -50.1282 | 2026-09-14 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| c7d00fe7-32c7-3d25-88db-85404f0ee77f | -6.1294 | -57.6833 | 2026-09-14 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| f9404ccb-4af1-35b2-b07d-945f792de3c4 | -6.1111 | -57.6645 | 2026-09-14 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 05e43d7b-ad02-3511-a85d-894eb904298d | -3.7855 | -44.1081 | 2026-09-14 13:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 56fd2fcb-0a81-3ce4-bfe9-9e2a538582a9 | -9.4936 | -45.4818 | 2026-09-14 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 755dea4e-8421-3627-8a64-4f4f1af74ac1 | -3.1697 | -58.6437 | 2026-09-14 13:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0fcdf23c-a11b-332b-a476-ac6d22506a8a | -4.1334 | -60.6692 | 2026-09-14 13:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a06f06ec-ba03-38ca-8acb-e96467cdc3f5 | -10.6638 | -54.1696 | 2026-09-14 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| de080f03-96c6-3d0c-b340-58388d006ae9 | -8.7634 | -46.4194 | 2026-09-14 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 3fcc4369-622b-3ab8-b608-296b232dae19 | -10.5484 | -51.2945 | 2026-09-14 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 90e5156b-f1b7-3659-9c55-be5131f3fba0 | -9.3763 | -50.1139 | 2026-09-14 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d96dfb0f-a554-3ca3-8a9b-94da17c13543 | -6.5837 | -58.8498 | 2026-09-14 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 87f3ae5b-bde8-3593-b08c-82eef54cbffa | -10.6643 | -54.1286 | 2026-09-14 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 21ab0219-e1af-33ed-ae8e-0c8108dd2e9f | -3.4089 | -58.2142 | 2026-09-14 13:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 0f4ef5b2-b381-31b0-9f95-b3682866e565 | -3.4089 | -58.1949 | 2026-09-14 13:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 05ae94b2-7fd6-3f72-ae91-b4d88f192c85 | -6.6767 | -58.7105 | 2026-09-14 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 168.1 |
| c1bcc2c2-4f38-36da-9962-afe1c0712aba | -9.3753 | -50.1992 | 2026-09-14 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b5b474c2-4c26-3cdd-a773-f5c5e58255e8 | -13.4264 | -43.8163 | 2026-09-14 13:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| d47887a5-bb66-3b72-b698-7523029ee0f7 | -9.4328 | -50.1086 | 2026-09-14 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| ebe05530-83c8-3f9c-ae0f-d8ae1f83b5cf | -13.2867 | -51.3046 | 2026-09-14 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 2f479c5b-424f-3cfb-918d-cb6d6e6a0a3d | -9.3755 | -50.1779 | 2026-09-14 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 281f41e9-30b2-3ca9-bda8-44693a0fddef | -7.0166 | -44.6184 | 2026-09-14 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 6f020bc6-10f0-3e62-b2b9-85bd27fc80af | -13.4453 | -43.8366 | 2026-09-14 13:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 7b5866fd-2759-3b26-aa88-a3d871a487bd | -5.1255 | -55.955 | 2026-09-14 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| a68250b1-0f4b-3d43-ab37-5bd8fc8e2e25 | -10.6829 | -54.1475 | 2026-09-14 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 17238cde-5f35-343a-98b8-9674b18133c3 | -10.6832 | -54.127 | 2026-09-14 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 75ec2294-0dd1-334f-abf3-6f01445aebd3 | -8.8081 | -45.8753 | 2026-09-14 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 346.1 |
| cb40eaaf-d076-39d8-a3b6-a5dbea849087 | -8.6194 | -44.4357 | 2026-09-14 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 6ae6747f-ae5f-365a-955e-8c43c4426263 | -4.115 | -60.6886 | 2026-09-14 13:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1c663dcd-db4e-3264-ad15-fa19849b69c4 | -6.1109 | -57.684 | 2026-09-14 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 192.5 |
| c69bb548-5cf2-36d2-87e4-da2664268e73 | -13.4458 | -43.8128 | 2026-09-14 13:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 01818563-2be9-3937-8a70-f0896c146032 | -9.9956 | -50.2675 | 2026-09-14 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 3678fe73-9f14-322f-86f4-2bd1f1887208 | -3.4272 | -58.2138 | 2026-09-14 13:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 748651fc-1142-3cbb-9a1e-f88df82db6dd | -9.5126 | -45.4796 | 2026-09-14 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 88b037eb-837b-37f8-980b-9eb6693c3375 | -9.494 | -45.459 | 2026-09-14 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 2d217d95-c205-3d15-8525-3b963de9a3fb | -7.1048 | -41.7971 | 2026-09-14 13:30:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 128.8 |
| 3174d5c7-1de5-31a0-8ab8-f53c399b7e23 | -14.205 | -47.4039 | 2026-09-14 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5b21b274-8a2d-3f37-8f76-69f5a0f6d42e | -9.4325 | -50.1299 | 2026-09-14 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 03ba748f-aed8-34cf-99d8-d913fcf42bd6 | -10.6827 | -54.1679 | 2026-09-14 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 135.0 |
| cdd01786-7d36-394a-ac3b-520c9102654e | -15.5768 | -48.792 | 2026-09-14 13:30:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f242cd54-92df-3920-a07e-6077ceee32b8 | -10.5295 | -51.2964 | 2026-09-14 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| c5dd985f-ac8f-3fde-9761-2b7037c949f1 | -13.2863 | -51.326 | 2026-09-14 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c63399d5-93ef-349f-b132-f14ee4e88a7b | -7.0859 | -41.799 | 2026-09-14 13:30:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| 70782b57-0e15-3814-8711-95c148afe2ef | -12.2249 | -39.2952 | 2026-09-14 13:30:00 | GOES-19 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 129.9 |
| afd89a2a-b09f-3274-ac13-f2c7d520e549 | -14.205 | -47.4039 | 2026-09-14 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 289a92d5-b561-3bdd-839b-fb2ae80b5bb1 | -10.6643 | -54.1286 | 2026-09-14 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| c6ed47c9-e2d0-3fb1-be83-19c087b8f8df | -3.4089 | -58.2142 | 2026-09-14 13:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 4d926903-6ad3-3859-81bd-d4a42d45e7fd | -13.3059 | -51.3022 | 2026-09-14 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 87db397d-75e5-3a10-8871-3a4b097f8e26 | -10.6832 | -54.127 | 2026-09-14 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 45cb7160-8965-329b-a974-a4a25d661c43 | -5.1255 | -55.955 | 2026-09-14 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| c8c35e8b-850c-332b-beba-af80b0ed7122 | -9.4328 | -50.1086 | 2026-09-14 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| e76e37a8-6b97-33c4-a8a7-f8edba00bd4e | -3.3505 | -59.3891 | 2026-09-14 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d978e411-8310-3bf4-a265-bdb97bb94b15 | -7.1051 | -41.7731 | 2026-09-14 13:40:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 155.6 |
| 10fa31c1-50df-32ce-b95d-d14ee899ae2a | -3.6076 | -59.0769 | 2026-09-14 13:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 81120725-9fbc-36b1-b155-2d962632fc4e | -15.5763 | -48.8144 | 2026-09-14 13:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 6cd1219a-7bfa-3a7b-9ec5-d61ecc68610a | -6.6767 | -58.7105 | 2026-09-14 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 143.9 |
| f128d667-bbcf-3e56-b23f-b739f8ab5f73 | -13.4453 | -43.8366 | 2026-09-14 13:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| cf5325f9-05f0-3d61-92bf-6f067f740a50 | -10.5667 | -51.3349 | 2026-09-14 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 26ff53f4-b690-3263-9a29-453e9a6c6815 | -13.47 | -48.4772 | 2026-09-14 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 191155cd-08e8-364a-a598-f7c9129e8900 | -10.7145 | -47.5374 | 2026-09-14 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 00dde5de-8126-3517-8503-df74db19ba0f | -10.312 | -45.2907 | 2026-09-14 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| df0cc74f-cd48-3904-bd4e-2a4721fc02b9 | -9.3753 | -50.1992 | 2026-09-14 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 018a0ac4-8b2e-3b31-950e-5d0cab84173d | -15.5572 | -48.7953 | 2026-09-14 13:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 95b0a9e8-5f00-3240-af0a-0ad617f9db44 | -10.6829 | -54.1475 | 2026-09-14 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 179.7 |
| 2e1e61db-f2ed-364d-8281-4905498166c2 | -7.4713 | -45.961 | 2026-09-14 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 1230d909-2f3d-3ed2-800d-5e0a8033b38b | -8.7634 | -46.4194 | 2026-09-14 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 234.8 |
| a8771c43-78dd-3c31-8cf8-a1be03abccf1 | -7.1048 | -41.7971 | 2026-09-14 13:40:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 185.0 |
| f0f26ed8-4ac8-3b77-af39-556fea5fe509 | -11.2391 | -43.4413 | 2026-09-14 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 8b8ee054-7342-3c0d-af19-44fe812b05a4 | -8.8081 | -45.8753 | 2026-09-14 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 55b27272-7110-3b81-b494-8d8c8847ce33 | -13.2867 | -51.3046 | 2026-09-14 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 1f7fdc0f-ddb4-32e5-a01d-8e31779b501d | -3.4089 | -58.1949 | 2026-09-14 13:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5585a763-0ae7-36b7-9389-6b810eab2319 | -10.6958 | -47.5175 | 2026-09-14 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7332ee28-9f1a-35a0-bf5f-1393f2d7ead4 | -7.0164 | -44.6413 | 2026-09-14 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 0b01ae33-92d1-374f-bd9e-72f4db71b67e | -3.7855 | -44.1081 | 2026-09-14 13:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 3ce3ecbd-7840-37dc-9e3b-cc7eb0e4580d | -9.3755 | -50.1779 | 2026-09-14 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 419c8407-4d31-3f60-a168-698c8b37c40d | -9.4137 | -50.1317 | 2026-09-14 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 79f45bc3-bb67-3286-9539-822135f00399 | -9.3763 | -50.1139 | 2026-09-14 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 134b0214-62e8-3918-ba7b-65b18491071a | -13.4704 | -48.455 | 2026-09-14 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 36331bef-6681-3f0e-8bdb-b0ac4794573a | -9.3758 | -50.1565 | 2026-09-14 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| ce9000cc-5974-38a1-a127-5af235ca399f | -3.1697 | -58.6437 | 2026-09-14 13:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a440809f-735a-386d-b906-9a6ef3e8d249 | -3.4272 | -58.2138 | 2026-09-14 13:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 2f423ca7-4d7e-354e-8513-7a27b8c1d6f6 | -7.0166 | -44.6184 | 2026-09-14 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 5acaf958-e7ed-3333-90a6-b4ccbaffd03e | -7.1012 | -42.1088 | 2026-09-14 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 145.1 |
| 2b4dba6d-005c-33fb-9257-b7637eccb6d6 | -9.376 | -50.1352 | 2026-09-14 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| aad94d44-2506-3ae6-8524-bfdd0d82161e | -6.1111 | -57.6645 | 2026-09-14 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 9f783052-fac5-3708-8473-d3e6d62840bf | -6.6021 | -58.849 | 2026-09-14 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3c00609a-b041-37ca-bb11-bcbea120565c | -15.2859 | -53.9037 | 2026-09-14 13:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 9edfc004-a556-30f1-a5a1-a2ec85d7696f | -6.1109 | -57.684 | 2026-09-14 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 2be8adf6-9292-3756-bd83-5a6cbabb83be | -10.5484 | -51.2945 | 2026-09-14 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| e3b71d55-9dc2-3679-801a-da32d4cd56dd | -9.4129 | -50.1957 | 2026-09-14 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 11fc324b-9ec8-3ed6-895d-cec3e7652898 | -8.6194 | -44.4357 | 2026-09-14 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 323.1 |
| 95cbe424-7bbd-3586-b347-1747a08eea88 | -4.1333 | -60.6882 | 2026-09-14 13:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| db16e8df-e20a-3bc3-bbef-0392636f0375 | -9.4936 | -45.4818 | 2026-09-14 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ee94b6e2-9f8b-313d-9904-b8c8b0660197 | -9.4513 | -50.1282 | 2026-09-14 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 82073427-32bc-3e7b-9751-e4996e782e86 | -7.0859 | -41.799 | 2026-09-14 13:40:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 155.5 |
| 825e0b13-17fe-39a2-9d9a-573377bd1c4d | -3.3493 | -59.8288 | 2026-09-14 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 610898d1-295b-3bb5-aa95-c20b78262f8e | -4.115 | -60.6886 | 2026-09-14 13:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 00998f65-c18d-311a-849f-b47529d3db5a | -9.4325 | -50.1299 | 2026-09-14 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |


[Clique aqui para ver as próximas entradas](README71.md)
