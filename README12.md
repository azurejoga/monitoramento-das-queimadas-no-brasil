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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34ff43a3-aab6-334f-bf32-359d9b528817 | -7.10671 | -41.79449 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 31514074-4d30-31a0-9b24-b967eff3dfb4 | -9.40247 | -50.16892 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| de07ff8d-49ba-330f-a70d-93467c88b8ed | -5.28384 | -45.26418 | 2026-09-14 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e0c0082-6989-336f-9d52-28a62d3807b0 | -4.85833 | -48.36389 | 2026-09-14 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c84e6d03-59f7-3e79-85d9-a06e5f35395f | -11.05177 | -49.57333 | 2026-09-14 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1e366442-bb7d-325d-b31c-91e8ecc0001d | -7.11948 | -41.78387 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aa7dd522-31de-333e-ac23-20dd475d40cc | -7.0764 | -43.55629 | 2026-09-14 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55aa844e-f096-3d27-becf-4a41065e49c7 | -10.63952 | -45.99849 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b791c278-0027-3d63-9ff7-864eec95fb53 | -6.33876 | -43.36734 | 2026-09-14 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 317ebc9d-8089-3e44-aa85-5d6493648ffd | -4.27183 | -48.64164 | 2026-09-14 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e45f0de6-e61d-3643-b098-e8c82d9f308a | -9.49397 | -45.48127 | 2026-09-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e4405bc-3e33-3d66-86e8-8f965b764351 | -8.00023 | -43.78629 | 2026-09-14 03:55:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 348c77d2-94cb-3180-ba74-f214390829fa | -7.96463 | -43.98809 | 2026-09-14 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d478525d-6f04-3185-b908-1f392c8426c0 | -7.4748 | -42.11729 | 2026-09-14 03:55:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 811c7ec4-de45-3ad9-a90b-7f9ec3c13c2e | -10.56108 | -44.61311 | 2026-09-14 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3a57568-fbe3-3c76-9aa9-6d5160198130 | -11.18226 | -42.81108 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 88eab9bd-946f-3476-8923-cba2ecc78dd2 | -5.29301 | -45.2658 | 2026-09-14 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b3179662-bac2-3409-84b4-096f055c13f0 | -9.43362 | -50.1339 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| de494027-8370-3576-a0f9-e47a335bbca0 | -9.43709 | -47.85695 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47688bfc-6f4c-3ad0-a19b-5505a360c4e6 | -10.10932 | -36.29089 | 2026-09-14 03:55:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3d644b5d-77f0-3c9e-a298-f4e95a22c230 | -3.38621 | -50.77044 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61783ee8-3ab0-3dc8-81ad-16ad46531841 | -11.62026 | -38.04911 | 2026-09-14 03:55:00 | NOAA-21 | ACAJUTIBA | BAHIA | Brasil | 2900306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 916957a4-b411-362b-bfc7-8fb1d4c8b5da | -11.37431 | -43.96026 | 2026-09-14 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9860ec7-e6f4-3a02-95e1-596472efea15 | -7.77702 | -46.66124 | 2026-09-14 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd0aaa1f-8123-3f44-874d-e1064f1f5da2 | -6.77747 | -42.74512 | 2026-09-14 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2c92323-f2a0-30d1-b36c-880550f916bb | -7.10968 | -42.10103 | 2026-09-14 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10dc8ada-afe2-3e8a-a358-975f496224d8 | -4.59496 | -47.17551 | 2026-09-14 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8997532-018d-3318-8643-329943970012 | -9.42343 | -50.123 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3feaeb73-0d7d-3aa3-bc28-dc6bb1cc6361 | -7.10963 | -41.79927 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9f702f22-3281-311a-a3dc-d008bda8e518 | -9.4501 | -47.85986 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4f9538e-9a45-30aa-a1bd-5f455a573b77 | -6.66599 | -43.6558 | 2026-09-14 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd061cb1-29b5-34f2-a5fc-712eda0f1508 | -7.0855 | -43.55086 | 2026-09-14 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 89accf92-2a16-33b5-9e4f-e14ead9bea6c | -9.45024 | -40.3925 | 2026-09-14 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 722e4789-9d9a-3068-a0e1-030959ccb31c | -9.41338 | -50.14376 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 783b19d1-4963-3325-8a9d-cd1e8bc5e42e | -7.96147 | -43.98758 | 2026-09-14 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97855711-73da-3b89-a97b-1c36b7f34815 | -11.18516 | -42.81591 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| af6ed841-85e0-38b9-ab20-605179d14bae | -9.98692 | -50.27459 | 2026-09-14 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ecd8138-f85e-39ac-9105-430091d3e668 | -9.32998 | -44.37553 | 2026-09-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d863525-461b-3e62-adcf-8bb9aec258fe | -10.5518 | -51.30584 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0de3bb16-09af-31f4-a116-ea0adcb34666 | -10.58409 | -51.33889 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61bb0b27-230a-31f0-8c78-ecfd0fa2c086 | -10.17614 | -48.06582 | 2026-09-14 03:55:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d4e90e0-b8f9-353d-9af0-3bcef01c5d6b | -7.10536 | -41.80286 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a7849d83-043c-3090-9030-d827d8d00995 | -6.8741 | -52.1013 | 2026-09-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f6a578c0-1f75-3cc9-9bb9-d237af0e9acf | -11.42426 | -45.14003 | 2026-09-14 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0654f21c-9fb8-3bbf-bce3-ea1159f07a12 | -9.43655 | -47.85996 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f401896-000f-36f0-b81b-f653fd5b0065 | -6.1008 | -43.51299 | 2026-09-14 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60f6f498-6bc0-3f2d-82f0-5c72aff6d4a6 | -9.37625 | -50.1776 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6767f5ba-f2b0-3cd6-9bf8-ad21e57ecddf | -7.08381 | -41.79917 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5ac85c1b-9e69-3e77-8511-97bdfd6b6e71 | -5.84416 | -52.09378 | 2026-09-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c0baead5-37ff-377c-b94f-1a22d2352c27 | -10.10442 | -48.85668 | 2026-09-14 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b840a3c-f038-313d-95a8-36126a4b55d1 | -10.58318 | -51.34352 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55ab262f-bcad-3943-bfd2-85db72d0fc58 | -9.33124 | -44.36827 | 2026-09-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44ef2dd8-28f9-3b88-b450-dab3c4000ca0 | -3.38729 | -50.76423 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 459783b4-01e7-3293-bbcc-31eb87f234d6 | -9.9839 | -50.27074 | 2026-09-14 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17ea5027-1fd7-3334-81c2-ec386c14f1fd | -4.76399 | -42.11191 | 2026-09-14 03:55:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 69f5ca2d-a6f1-3486-841d-beb0eb0b3f91 | -11.22942 | -46.42886 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45445e4e-233b-3a4f-852d-2d32c9ffbb62 | -9.45139 | -40.38535 | 2026-09-14 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 79a9cd8b-ad27-37fb-bad1-c2b69c972d37 | -11.21145 | -46.42561 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d56c56f-de9d-3f19-b5bc-f721171fdb54 | -6.33536 | -43.36324 | 2026-09-14 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 64281953-337d-3a8c-abeb-729abf0d03d4 | -9.44116 | -50.12632 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0dfbfb8a-8c75-33bc-9efb-65b2272e18e4 | -10.46842 | -51.2473 | 2026-09-14 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d85be83a-b99d-39d2-bbde-b9325f5acaa3 | -8.53101 | -39.4315 | 2026-09-14 03:55:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f5581317-0c4c-33e5-9916-9d55f6ba8ea0 | -5.89104 | -45.57423 | 2026-09-14 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec24ebb3-53ab-3dc6-ae8b-d284c4bb1aa1 | -7.07873 | -43.54256 | 2026-09-14 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c06811d8-331b-382e-90ed-4145e6a42148 | -3.39093 | -50.38971 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e93e12cc-0f43-3724-b88b-2ffb0ae36190 | -11.60107 | -46.99104 | 2026-09-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b3170ee-9b03-38fd-a106-9ecafaee8b8f | -7.09166 | -41.79627 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f19cf233-fb26-338f-88ca-5926b1054e4b | -7.01976 | -44.62982 | 2026-09-14 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7418e6b5-b770-34c1-861b-b4b22ac1c042 | -11.23321 | -43.44506 | 2026-09-14 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c0f77f2-afb0-3560-a465-72e4ca1de8eb | -9.45692 | -47.85151 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 176edc16-d226-3bcb-bb95-85f81178e45b | -10.55705 | -44.6124 | 2026-09-14 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65010805-fbc0-32ea-9c71-f2fce80fe826 | -4.8526 | -48.3631 | 2026-09-14 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1e72faac-9043-3dc4-8579-9bfdcc42cb7e | -9.89221 | -47.62053 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa1239ff-b485-387c-95d7-935dee25f55e | -8.60554 | -44.45409 | 2026-09-14 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b7786ad-4e0a-35d8-9afc-4cd8805a52bd | -10.31426 | -45.29285 | 2026-09-14 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc83d990-df8c-35bf-94ca-62859f8e7ddc | -11.17597 | -46.39082 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e82fb4a1-f25f-3b12-bc89-bce9edd8aad4 | -7.10603 | -42.10044 | 2026-09-14 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa374318-fb0c-31b4-9b70-c8c4e9a7d784 | -9.44791 | -47.85535 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92bee370-1d95-312a-a2a1-9c336f9c16fd | -5.80407 | -52.11405 | 2026-09-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c9104a5c-dd8a-37f2-8a2b-9e678d779edd | -3.76061 | -51.14954 | 2026-09-14 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 687fddf0-5ac5-3b9c-9e44-9c58a7b325fd | -8.38961 | -42.2178 | 2026-09-14 03:55:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d80688d3-90f1-3ca5-ba8a-137f925a97a2 | -5.29221 | -45.27053 | 2026-09-14 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a6317e8e-cf13-3743-9457-ad475b74f0ff | -5.76445 | -44.0592 | 2026-09-14 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 673c1f52-ad25-3a6b-ab5d-720a16b071fc | -6.49744 | -40.0926 | 2026-09-14 03:55:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a5bf0b03-ff17-34e5-8c84-362763364295 | -9.44736 | -47.85841 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbb16a85-dde5-3863-a350-9084fc84d25e | -9.41172 | -50.15251 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9981cf2-1aa2-3e50-8f4e-469284e1ae40 | -7.0919 | -41.8176 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8b9911db-587f-3703-9309-3183447380c1 | -7.2893 | -40.12199 | 2026-09-14 03:55:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| caa556d4-8fcd-3032-91ce-e547f68d25d8 | -6.34401 | -44.1042 | 2026-09-14 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c7b2b22-8cb6-3367-a8c7-eb797f9315ce | -6.2072 | -45.32698 | 2026-09-14 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7e216aed-1f43-35c1-ae1e-3d5874932da1 | -7.12935 | -42.09539 | 2026-09-14 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a6aee02-9334-3a26-a8b4-816577c49413 | -5.84752 | -52.10277 | 2026-09-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bd0dcc18-7123-34ca-86fd-4240da7da663 | -9.37714 | -50.20507 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c542ae7-b90e-3404-9c85-1aec3820d9c9 | -7.01548 | -44.62916 | 2026-09-14 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8156a564-9634-32a2-9509-b0e2dcf74035 | -7.562 | -41.84282 | 2026-09-14 03:55:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5eb8052c-182c-3ca7-9be9-85fa6252e732 | -11.18075 | -42.79782 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cc0f6a31-d824-39a3-9c12-4e1d3939e5ad | -10.95736 | -39.27021 | 2026-09-14 03:55:00 | NOAA-21 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a6651fc5-a02b-33c8-855d-003669b33b78 | -7.02266 | -44.63863 | 2026-09-14 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2333921-d584-3ac8-b139-4fbf57d54c5c | -10.10852 | -48.86463 | 2026-09-14 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f88aeeb0-3882-3749-b185-0416efe501ad | -11.22359 | -43.43411 | 2026-09-14 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README13.md)
