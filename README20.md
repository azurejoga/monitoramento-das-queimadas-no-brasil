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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 333d0453-0e0f-386e-89e7-e8a5bb67071e | -2.84268 | -46.66974 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b517cf7-61e8-34b0-a9e9-0ee4855e7993 | -0.89008 | -52.72509 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b69e24da-a099-36fe-b284-e93da173743f | -2.24211 | -45.74897 | 2024-11-18 04:10:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bdf09c7-53e3-3097-aea3-c62093b6347f | -3.22506 | -45.55196 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 394d4e8e-19d3-3d0d-9465-60a6437bc8c5 | -1.62279 | -55.15176 | 2024-11-18 04:10:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e4139aa-095b-3485-9fb8-64914f152fd2 | -1.70191 | -46.165 | 2024-11-18 04:10:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81668a7a-a99e-367f-909d-1a4c914a6a1a | -2.67903 | -46.81688 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23a925d-2bdc-3737-8385-33bc730245c5 | -2.8681 | -51.7904 | 2024-11-18 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e7b7b8d-8af6-3c17-9ca2-9f9e3c68b272 | -2.9483 | -48.32133 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa8ad488-e258-38d8-a26a-3957064fe607 | -2.93765 | -48.06989 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| eb94ee2c-2b61-321e-8256-f30e882545fa | -3.14043 | -45.9899 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34a635f3-70a7-3de5-aa21-fbc1f57f6b54 | -3.14484 | -45.35014 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92401cb6-fa1e-3fdd-8a62-a95fa998132d | -2.11252 | -46.48727 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9581af87-9891-3530-84ed-1d6c86781b88 | -2.36223 | -53.68273 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 901eee9f-cc02-3802-9429-57cce1139f09 | -3.17106 | -46.60138 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe1a81f2-eee3-3e0c-8ac7-15ad4b885a22 | -2.85618 | -46.66878 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82110ac9-1198-322b-8421-20e47f34b868 | -2.19431 | -53.67641 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8f508aff-0fc8-351f-ba16-1acaaba396b3 | -2.65586 | -51.73972 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27a00883-f2a2-372c-a887-75a3af738f5b | -1.28927 | -51.73897 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2a28409-76c9-3649-b88c-73ad365a1c7c | -2.90949 | -46.83241 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bb25a4f-a3ed-39bc-8d06-97c9356819ff | -1.72112 | -46.19207 | 2024-11-18 04:10:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97d1438f-ab7e-3c40-8b77-001003bba4aa | -3.3305 | -46.01701 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d996b9b0-4842-308e-9f50-f9968720a427 | 0.1667 | -51.26776 | 2024-11-18 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c968f58b-0945-3556-99f6-e2fc479dc42f | -2.67688 | -46.22281 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f64d6f0a-6050-3b73-9b22-de22a3df8c1f | -3.1905 | -45.44451 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9ad1c41-9468-31b3-9b6c-612b6423950d | -3.15223 | -45.98731 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd1e3a10-417c-3d5e-bd59-1c01aaa70a4a | -1.85142 | -50.79995 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b66da8fa-7b75-3118-954d-149d850539fb | -2.85429 | -46.67163 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa9c4f2f-242d-3e90-8451-00ebdb3ffea7 | -1.31734 | -51.87423 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 366ff32f-1098-332c-884a-a980c65f07a2 | -3.21062 | -46.4701 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c961bb9-0f29-3195-985b-841e91a4bea6 | -2.49875 | -47.24015 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0aae2f54-7467-39da-8999-cce4b8bc2a3e | -2.86752 | -51.79394 | 2024-11-18 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84a7a1f6-f1df-3146-a604-12387313aadc | -2.63587 | -46.83536 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5412e6b-f128-3897-8981-9f3006d5f7e8 | -2.97816 | -49.1129 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2a07b3d-cdd5-3721-97de-d3a2bf0cb956 | -3.16414 | -46.59542 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5833c7dd-c32d-31a4-92f4-fba425d07fdc | -3.16339 | -46.60017 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efbaa445-15b2-33a9-907d-e390cde7c2f0 | -2.50738 | -47.23791 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47251eb0-bc99-32ba-aa5e-44ae2b71aacf | -3.354 | -46.42469 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1464265-8dba-351a-ab6f-f59c116737b8 | -2.94763 | -48.32542 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe83ab27-e33e-3dde-aad5-3c769ed53d79 | -3.14232 | -45.506 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1c43b15-a1b3-3358-915b-b9b19e52483d | -1.29708 | -51.75082 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 30e1b1ab-ce39-30d6-93e1-497a027d6125 | -2.63977 | -46.83612 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eacf98f5-109a-338c-91b4-df80fa01d282 | -2.86004 | -46.66943 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b37b57e6-d145-3216-b3c2-6703bece214c | -2.36363 | -53.68489 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bac00d8-c2ca-3b97-a65f-5251c6fefc4b | -1.76748 | -50.74583 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3239de8b-5eda-3e09-8f57-c1a593f1eec6 | -2.93337 | -48.3315 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ed43479-3909-3914-8223-01baf6fb5218 | 0.17223 | -51.26688 | 2024-11-18 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39a2678b-2a6c-32a8-9be2-d0b0e7502a56 | -2.36441 | -53.68008 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba8c87a6-ec58-3f62-b82d-07fd641e6bc9 | -2.91626 | -40.3893 | 2024-11-18 04:10:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c3d4b11f-9ae5-35e8-bac9-b2be5a46d70c | -2.76313 | -52.61749 | 2024-11-18 04:10:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ce349ebf-5d17-3482-a7ea-b96ec68d69bd | -3.20645 | -46.47676 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bb3e9d3-64b0-3915-beba-7a4056475208 | -2.84458 | -46.66691 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe7fa173-983a-3a5d-b763-6fbb94f0025c | -3.14164 | -45.46345 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eb4d78c-376d-321d-935f-074071e81e2c | -2.65581 | -46.23354 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe49f4f-b59a-3a67-a334-6641362fcf8e | -3.27155 | -43.21672 | 2024-11-18 04:10:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad0ae0af-544f-371d-b552-75084f4ed7b1 | -2.63894 | -46.84119 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1268281a-ce34-3581-aae1-d7debc7d9b64 | -1.76334 | -50.74651 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab63469c-a49b-3010-89fb-50e6a17b2953 | -3.33799 | -44.06403 | 2024-11-18 04:10:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16686af5-0213-36e7-9305-2bee7872b1c4 | -3.30684 | -45.74513 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 339a784b-34a4-301a-85a1-bb60966e054b | -3.57581 | -45.21245 | 2024-11-18 04:10:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f544d129-fc7a-36ad-9655-022728ad2074 | -2.97286 | -49.11684 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 609fbbf2-db8a-35f1-92be-f64308f3afcb | -2.67201 | -46.81057 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11fe5645-f719-3bdd-9254-347fcfaac71c | -3.09002 | -45.97285 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4f6b13d-1567-3648-a329-a13316accd99 | -3.02497 | -48.01095 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8cddf6c-8f11-3519-97f8-99f9c178d143 | -3.38187 | -46.39638 | 2024-11-18 04:10:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8720d9d3-566e-3372-a02c-8cba88a8579f | -3.17182 | -46.59663 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dfcc75f4-890d-314d-8852-4a15ff5a9f1c | -2.78289 | -51.75785 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57aed747-f0be-351a-8120-bb0c64ae145e | -3.23294 | -45.54897 | 2024-11-18 04:10:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fac0a26a-8396-3ed2-abf7-7deef34b3ac0 | -3.0882 | -45.17917 | 2024-11-18 04:10:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c9f041d-7078-346f-bcd5-73427336276c | -1.15829 | -49.11777 | 2024-11-18 04:10:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba1a46a9-a3ff-3791-a383-3acacc8530a9 | -2.65728 | -46.22431 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1959c96b-905a-320b-a9cf-90e6189a8945 | 0.79604 | -50.23035 | 2024-11-18 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a12c200f-cf1a-3f83-93ec-4638d515868d | -2.21826 | -46.4035 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e2bed36-1784-308d-aef0-aa4586c2f225 | -1.75789 | -45.69045 | 2024-11-18 04:10:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a531cb9-735c-37f7-bfa3-9b6814db3ccc | -2.3308 | -45.64323 | 2024-11-18 04:10:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92c9d8ec-5035-3877-9299-6c0ebf68236a | -2.18521 | -50.33899 | 2024-11-18 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0787f1e6-bcb2-36f7-ae42-d54de27c1f46 | -2.61353 | -46.82444 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f1bdb4b-1ba8-3a51-ae75-fa7152e64ae5 | -3.35853 | -46.42073 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b736370d-46c2-3efe-bf02-1e562bdef544 | -3.22973 | -45.38345 | 2024-11-18 04:10:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0156b8c9-11e9-3c69-a68e-13f940f96f48 | -2.64669 | -46.21789 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0769ce82-8079-3376-b45c-d26700cf42e2 | -1.89777 | -46.44873 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2c422331-395e-39c6-a77c-f1ebf1813124 | -2.62805 | -46.83393 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1859683d-c98f-390b-827c-5dc9108d6ed0 | -0.89275 | -52.72316 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c33e91e-eb5b-3cea-9426-4110a5be005d | -2.7976 | -45.9547 | 2024-11-18 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 001c9ae1-5bab-3903-8405-d24b2687206e | -2.56008 | -49.11249 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e31cfec-68cd-3fe9-a624-2d9e529c85cb | -2.85539 | -46.67361 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b71a3a8b-4ec9-3629-9cd3-50b8d41de67f | -1.28869 | -51.74266 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 620377d3-082f-3835-8e29-e728fa5ab833 | -2.64677 | -46.84257 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8205d346-4a97-3327-9676-d54b03ff85a7 | -3.57645 | -45.20845 | 2024-11-18 04:10:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a02fa289-71e1-35dd-91b5-96708ccce3e6 | -1.43069 | -53.38534 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 35af481a-3569-3657-9507-74297065eccc | -2.85118 | -46.66616 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57de3711-6211-3154-86d5-69db3e5edca0 | -2.20795 | -46.29543 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6419a3ab-093a-3254-b3f5-f133cff5be19 | -4.21246 | -44.0342 | 2024-11-18 04:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1fc9130-f354-390f-962f-137d6fafb503 | -2.65655 | -46.22892 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf952800-351e-3887-a857-d8d7d2058c85 | -3.22867 | -45.55255 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f490fd3b-9007-3852-895e-4f342e7dd47b | -2.85925 | -46.67425 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e09ccb3e-64d8-363d-9bfb-4dd125b109c9 | -2.50681 | -47.24149 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ceaf87cd-db9b-37cc-b5a7-9adb00d5280a | -2.93404 | -48.32739 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6834ad6e-0f47-35a1-8398-3f4378be9a98 | -2.92974 | -48.32669 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dca853a-2921-39ea-9377-9deb9bf98c06 | -3.35325 | -46.42928 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
