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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 022bdeb2-0a42-3827-a239-4954866d157e | -3.501 | -52.48958 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7112b38e-db3c-3606-b48d-b2d05973f9d0 | -6.31739 | -40.9487 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6fcb5f42-0b50-3861-93fe-1d0364288c8d | -5.8832 | -44.75575 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e3bd152-ebb3-3fd7-887d-9512529d6e4d | -8.23609 | -44.02093 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61b169e0-7a5c-336c-a705-fd911b27c3c8 | -5.23177 | -43.38879 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9e769ca-9da8-3184-b285-29b6bf69923c | -9.33945 | -46.90908 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 363a361a-fa0d-35aa-b5b7-8dc258f027f0 | -5.91833 | -44.74712 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d30a802b-737b-33c9-b919-14eb77b4ca91 | -10.65444 | -45.25001 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7877712b-44ee-3cce-b5a5-9caa22cc9c43 | -10.48195 | -43.79565 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18860abf-c027-3ad8-b11e-a9fd93e1a9c7 | -8.69798 | -48.71896 | 2025-10-17 04:19:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07b5d041-fd5e-33b7-897d-d8d761e54a78 | -4.10924 | -48.023 | 2025-10-17 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87ab1beb-d560-3a74-8cea-7f683bd3099d | -3.82245 | -52.34702 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bc8d3d1-738c-3589-ace4-ba2a0d13141d | -9.047 | -46.08125 | 2025-10-17 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57cdeffd-2842-3347-a0d6-46243b428fd1 | -6.7496 | -42.36779 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8db6f1b9-ec14-319d-a3c2-d89eb571bfab | -7.20747 | -45.48777 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8d89edf-2d92-3275-b5fc-d851b66f461c | -6.33001 | -44.31144 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d2fccde-0549-30dc-b5d3-11d905918d03 | -8.41547 | -44.72956 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7e99270-91aa-3bc8-8a5e-a987ace6d7a9 | -7.4416 | -43.74533 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7514b477-642f-3d54-9ff2-97c29d4fa4cb | -6.29238 | -42.97127 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 612e6af8-bcf2-3921-a794-a53d0d52f665 | -4.72564 | -46.15667 | 2025-10-17 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4eb32d0-5a56-3e41-9488-333fe76330db | -6.13572 | -41.73706 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0f029015-30b9-3125-bdc4-25ed29cfc640 | -11.39029 | -44.21582 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 322775a6-bfcf-3930-97a5-a80725f6e76e | -7.98353 | -44.15851 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e55d2805-9c8f-37ae-b9d1-ed1bcd530961 | -5.49515 | -48.94476 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7998f7c0-0cf5-387f-8210-4936e5058819 | -6.24133 | -44.4035 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1b4356a-b1da-3d05-a8a3-80e3d3fee9f9 | -6.20497 | -41.73496 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11a2f7fd-0efd-3a01-a11a-d5c5b32c3943 | -6.38153 | -41.47126 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e418cbeb-a983-3d6c-a372-9ac60f122adf | -2.87763 | -50.73443 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c743636b-a1bd-3dbf-92c6-67a10c8353ac | -4.55764 | -46.61899 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bb10ed3-f832-3a3d-a909-538883fb1d93 | -10.57804 | -47.42003 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f432178-4ba1-3866-b024-cef97fdcb710 | -8.35728 | -41.41747 | 2025-10-17 04:19:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b99bcfe2-dfe9-38fa-92fb-2a504de5d718 | -8.25636 | -44.04193 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e5c2455-081e-31c4-910c-dcbc30d71de8 | -10.88945 | -47.90394 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 552447e5-fb47-3fa8-b894-3190c637a464 | -7.86184 | -42.86995 | 2025-10-17 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 886c72f3-cd98-3004-afb8-66206b363804 | -6.74684 | -44.36641 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55e01cc8-6ac8-3f70-9a31-24e0583113be | -8.57289 | -45.43969 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0630b279-750b-33a3-9e5e-2e2c952c178c | -6.26439 | -43.90343 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4407780-18e3-3843-9421-457567362a91 | -6.75131 | -42.3798 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7cdf2b4f-241a-3c51-8528-35070c62154b | -7.46896 | -42.14244 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3adb77ac-3a90-3ea6-ad87-0e20e325f2ec | -8.62193 | -54.55999 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4723b1dd-b83f-32a7-9b2e-13656274ebc0 | -10.62105 | -42.30743 | 2025-10-17 04:19:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7e995d30-6803-3ca2-b6d3-ef8b31dc0d1b | -3.60061 | -48.98484 | 2025-10-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a973cad6-4368-3494-a333-0e9cdc91da31 | -10.14965 | -44.53286 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5cb4147f-5f8f-3c06-86a1-b29cbd6ddef6 | -6.78374 | -44.65478 | 2025-10-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bd764a0-ddcd-369c-899a-d3efacb3a2f5 | -4.38236 | -43.38182 | 2025-10-17 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad77c25c-47bd-353d-b0e6-43df7de87b92 | -5.25988 | -44.21254 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00a8809a-b4dd-3d3a-abb1-2f65420ac63f | -9.06533 | -42.45877 | 2025-10-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1166cbcb-7bcd-3ba8-aedd-26dd753922a0 | -10.14154 | -44.58584 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b23fdbe0-006b-3b2f-a57e-a1c3ec5ef64e | -7.1805 | -42.37065 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0ac4c128-d34a-39fb-aa22-14aedbbaa842 | -6.84553 | -44.38883 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c521f65-a8d3-3c3a-a0f8-22ae78c6f424 | -6.42316 | -43.09841 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e31a7560-fed3-3ee5-8184-8bc03a005a28 | -5.88758 | -44.74938 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d2752f2b-0809-3700-98e5-9bc24be8c9a3 | -8.58808 | -48.63504 | 2025-10-17 04:19:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| faf477c1-a417-314a-8fc1-53f4a3039411 | -10.2748 | -44.0247 | 2025-10-17 04:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5eb1dd16-efb1-35f7-9f02-75b844f2f185 | -9.1375 | -46.6485 | 2025-10-17 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 44ac6051-c48b-3e8f-b993-3123eae894d4 | -12.4267 | -51.2814 | 2025-10-17 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| ecdeddfa-1cc1-34ac-9add-524226062794 | -4.4061 | -43.3816 | 2025-10-17 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| d645068b-cab5-3f57-b24f-9899c48521d4 | -11.9516 | -45.3632 | 2025-10-17 04:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7ac30f60-418e-31ab-a9e3-7c103d850877 | -10.9475 | -49.7605 | 2025-10-17 04:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 3a6f3f69-e1ad-3fbb-b579-49aff8ceb510 | -12.4455 | -51.3004 | 2025-10-17 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 1c3506c9-b211-3d9c-be2f-f5c7912efb81 | -10.2939 | -44.0221 | 2025-10-17 04:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| afe86140-b1fa-3910-95bc-79e7f6a2ae05 | -14.3417 | -51.4663 | 2025-10-17 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| d53d9d83-5f0e-35fa-9592-08729abc8e1b | -10.5132 | -43.4289 | 2025-10-17 04:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| def15e81-8110-369b-be65-a104aa9076a4 | -4.4059 | -43.4049 | 2025-10-17 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 2962cbcf-7da0-32ed-b54e-094776277e2e | -5.2836 | -43.5575 | 2025-10-17 04:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7caecac6-c991-3e69-922d-1c71aa6ff7d4 | -12.4264 | -51.3027 | 2025-10-17 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 4670741a-095e-317e-916e-d1ea833e176e | -5.9095 | -44.7545 | 2025-10-17 04:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 38663e7c-fa44-3d90-9443-2c80a19eceb3 | -10.4945 | -43.4079 | 2025-10-17 04:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 6152cdef-e301-3f61-ab5f-18564e4b6697 | -12.7866 | -44.8873 | 2025-10-17 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 205160c1-2a12-3a6c-93f5-0d1c44680bdd | -12.4073 | -51.3049 | 2025-10-17 04:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 15bcbed6-5c6a-3fa6-b19e-743436010b8f | -12.426 | -51.324 | 2025-10-17 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 7fae9b36-9d6f-3a86-a553-b934f4162e76 | -14.342 | -51.4449 | 2025-10-17 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 664cbb14-9fb6-32c6-aedc-2cc62ad27f02 | -14.3227 | -51.4475 | 2025-10-17 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 6a8d8b5f-7dd3-31ba-867f-4c1c32cce6ed | -10.2935 | -44.0455 | 2025-10-17 04:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 9a86f51a-b49d-347c-8f90-276298432b1a | -10.4941 | -43.4315 | 2025-10-17 04:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 4c2deca3-9cc2-3050-92d6-9e475e94fa60 | -5.9097 | -44.7317 | 2025-10-17 04:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 32ca4b65-6495-341e-8b96-9b3ecaa1b05e | -14.3424 | -51.4234 | 2025-10-17 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 2e22b36b-e42e-33d9-94c3-b3ba0b8e5333 | -8.389 | -46.2333 | 2025-10-17 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| ec5b38ef-e431-3b79-a02b-0bc7f05ca2e3 | -14.3614 | -51.4422 | 2025-10-17 04:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 20cc219c-43b2-3f05-bc44-dff23969a52e | -10.5136 | -43.4052 | 2025-10-17 04:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 885afbbb-4f88-3b4d-9592-bbad8526d632 | -10.2745 | -44.0481 | 2025-10-17 04:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 6fb7abed-0e6d-3db8-bbc4-c98320583a02 | -10.534 | -49.5471 | 2025-10-17 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ef8f116c-c6e1-3e18-a5f0-2667438c2dce | -13.43421 | -47.95274 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1be9eae-31fd-315f-9a1c-04ee2d9a3511 | -12.43981 | -51.30326 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d150000a-0dca-3f2f-b8c1-2c4be6fe82db | -12.31748 | -47.83248 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0595e36-0d81-3d8b-a493-f02026c8670f | -14.89309 | -52.42474 | 2025-10-17 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce9b2fa8-de0f-3cab-8a61-ebceea2afde0 | -15.43185 | -41.13943 | 2025-10-17 04:21:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9a22e0fb-0d52-35c0-838c-95f43a6b2189 | -13.41774 | -48.58175 | 2025-10-17 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2c6cf51-7604-3d59-80b1-a3d470495d3a | -13.42249 | -47.93944 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c32a69a9-e8b7-345a-a1e6-f92b8af03a15 | -15.5854 | -49.066 | 2025-10-17 04:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb61c705-ae95-3b55-99aa-b545ab67e7e4 | -11.36528 | -45.27378 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1f945d9-6cc7-3027-a67e-255a951ca1a7 | -12.16596 | -45.06453 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4d3e9110-cd31-3d8e-aa82-8a77f90fb42e | -11.97478 | -46.55126 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c5739ed-f491-324b-a40d-ff846624dac9 | -12.94914 | -47.926 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ea1a042-b1aa-3e6a-924a-53f5739a6790 | -14.72346 | -48.30122 | 2025-10-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a7f7cd3-5bae-3a0c-9039-ba52328a25ea | -15.02319 | -47.30986 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 656df1ea-b3ac-3354-93a8-377cb0d0fd58 | -12.30869 | -47.25433 | 2025-10-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c257e228-3227-3101-b512-12de9a157919 | -13.95043 | -48.69978 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc4e0cab-021a-38f6-bc0e-37d9676085ef | -12.04605 | -51.37489 | 2025-10-17 04:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb37e8e9-62fa-3d91-9cb1-169df6ebe389 | -11.47923 | -45.08675 | 2025-10-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README66.md)
