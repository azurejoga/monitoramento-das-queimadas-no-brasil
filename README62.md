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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2c502f5-7d09-3930-a5f5-8db9b8d377c6 | -2.7148 | -57.6274 | 2026-09-12 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| ce82f23b-f525-3e3f-9140-708e5f43be66 | -7.9645 | -43.9971 | 2026-09-12 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 6e35b4ed-e17d-3472-ae45-065726c3ea1c | -10.2743 | -45.2726 | 2026-09-12 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| f0ca31cc-2670-3893-9c1a-e463f4865a59 | -5.1254 | -55.9748 | 2026-09-12 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8ff6fea3-5510-36bb-b5b1-27cf25a270a9 | -6.7648 | -59.4408 | 2026-09-12 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| d41cbd4f-fb5c-3019-aef3-a767880f4752 | -6.5004 | -47.5909 | 2026-09-12 14:40:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 7aa60dbb-5259-3bba-a3f9-411fbc25f584 | -9.6758 | -45.9821 | 2026-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 39191e2f-d4ed-3f3b-a569-149770446ac4 | -10.2182 | -45.2111 | 2026-09-12 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8312998c-ad7d-3857-88a4-4e6f3d884709 | -11.0839 | -50.8368 | 2026-09-12 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0e277b4d-b24c-3892-8d5f-50f94fe1b297 | -10.2735 | -45.3185 | 2026-09-12 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ec1a6a12-f2fc-36c3-906c-45298aa1b89f | -10.2171 | -45.2799 | 2026-09-12 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ecc021c2-f78b-328e-8ef7-f310b60572a5 | -6.7692 | -58.6679 | 2026-09-12 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| f1e58dac-473b-3fc0-93c3-3e68a9428ace | -5.7836 | -53.807 | 2026-09-12 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 95eea83b-112f-3630-a612-37edbdfaca91 | -10.2929 | -45.2932 | 2026-09-12 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 276.8 |
| 98a6bf18-ba59-35bf-85b3-7c6237444440 | -6.5191 | -47.5895 | 2026-09-12 14:40:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f2d9da99-f783-3393-8cb5-1f68e65a1f55 | -2.7331 | -57.6271 | 2026-09-12 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7c9e03ca-de2d-3c0a-98f1-717cf622d980 | -7.1718 | -45.8975 | 2026-09-12 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 0f5fc4b4-74b8-30bf-9ec8-92a22ed4105a | -2.7331 | -57.6465 | 2026-09-12 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 3534f2af-d310-32c5-9847-e62657a95b89 | -10.7018 | -54.1458 | 2026-09-12 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a63c9e06-a121-3232-a34e-f6f3cf5b96a3 | -10.6829 | -54.1475 | 2026-09-12 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| cfbc40e6-3406-3f1a-bf65-234be35535b0 | -12.0468 | -49.956 | 2026-09-12 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 43d98cbe-778f-376d-89f1-99bafa759219 | -11.4213 | -43.9556 | 2026-09-12 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 0934ce73-1f56-31a1-a3e5-39ebf56f3ad5 | -7.0166 | -44.6184 | 2026-09-12 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 277.3 |
| 96836e20-a206-3c19-ad07-0233236d0f93 | -7.2147 | -43.7001 | 2026-09-12 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 6db68701-3a52-36ef-95dc-04b2e4315c66 | -11.2833 | -44.1868 | 2026-09-12 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 241.9 |
| 6882c3aa-a3c7-3172-bb52-5727be37779f | -10.2926 | -45.3161 | 2026-09-12 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| dee79d06-e6c9-3191-9e3b-1f55b4dfe336 | -10.2206 | -50.373 | 2026-09-12 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 632a0457-915f-37ac-93cd-1aefa7dc2423 | -9.943 | -48.5264 | 2026-09-12 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 443c6147-b861-3616-8c39-1a89fdb63e83 | -8.8132 | -46.9495 | 2026-09-12 14:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 3212982e-637b-3e34-ad86-8d9554ed19ae | -7.5736 | -45.2062 | 2026-09-12 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ab0c15cc-8304-37d4-9b1e-e9e10c990734 | -11.4021 | -43.9585 | 2026-09-12 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 217.2 |
| edf25093-b69d-3e4b-98bf-d857ed7531ab | -9.9241 | -48.5284 | 2026-09-12 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| e5274338-5d0f-3c36-a22f-6dfb122f94b2 | -2.7148 | -57.6274 | 2026-09-12 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 18f3ff5c-f32f-395f-a75a-caf09c64f49c | -7.9645 | -43.9971 | 2026-09-12 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 94d16807-cffe-3da6-90e9-ae5ccdc625d1 | -8.8134 | -46.9272 | 2026-09-12 14:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| b093704d-8db4-3c4a-8964-89990799dbcf | -8.7943 | -46.9514 | 2026-09-12 14:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 9f6f6bb0-28a7-30d8-8f04-4737f1bcba6d | -7.1721 | -45.875 | 2026-09-12 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 0cc22855-dccc-3add-a555-f546fecb185c | -11.3834 | -43.9378 | 2026-09-12 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 420adfdb-59f8-3caa-90c1-124dca89ee54 | -10.2933 | -45.2702 | 2026-09-12 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 421.9 |
| 476eea60-aba9-3431-ad95-3b3ecef569e7 | -9.6755 | -46.0047 | 2026-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 14ccf0db-99b3-3ea2-84a4-8fa6c9ab45e4 | -8.0427 | -43.7798 | 2026-09-12 14:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 644ee70a-361b-350a-b717-b83aba12463e | -10.6827 | -54.1679 | 2026-09-12 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 225.3 |
| 3951420c-aecc-3829-86c4-c416f40e7e9d | -11.4026 | -43.935 | 2026-09-12 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 443.8 |
| 6e1e74db-0c42-3cc0-abca-8ba8529a9ce1 | -10.5473 | -51.379 | 2026-09-12 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 0abdc4b9-1322-3894-812f-b07e28c2f78a | -11.3825 | -43.9849 | 2026-09-12 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| a1c328b7-a251-3334-ba40-ebdd15f558c5 | -10.2376 | -45.1857 | 2026-09-12 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| fa6743b6-8bc3-383e-b417-bd1507c1afa3 | -11.383 | -43.9614 | 2026-09-12 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| b96fce36-31d8-359f-b9c9-22974cef4901 | -3.3504 | -59.4274 | 2026-09-12 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 368c398b-cdac-3dd3-bfe6-261409ce3a69 | -7.5924 | -45.2044 | 2026-09-12 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 153.8 |
| b2227daf-96df-3dfc-9b81-4c90b01c0d84 | -5.3646 | -56.0249 | 2026-09-12 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f2c4e752-5e48-3246-8e63-18dd09a9f243 | -12.1388 | -48.9672 | 2026-09-12 14:40:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 0ba9393c-eea6-3f79-976b-8d0197d96322 | -10.9491 | -48.3474 | 2026-09-12 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 88087a0c-45d9-3f22-979d-ba8822454048 | -5.1438 | -55.9741 | 2026-09-12 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 35d987ab-abae-3b6b-914f-1c336e079b9a | -7.6008 | -46.1288 | 2026-09-12 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 5b1a1ea8-5f85-3f6a-90aa-56de1d5c2296 | -7.4595 | -42.1199 | 2026-09-12 14:40:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 10fa8b8e-7b66-35a0-a306-a2f4c59d97f9 | -8.5801 | -54.5747 | 2026-09-12 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 65600bc7-4b77-3223-80b9-3d98df43db8f | -8.0934 | -54.8488 | 2026-09-12 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 4e633c4f-e016-3d69-973d-06c30fcbc3bd | -10.2186 | -45.1881 | 2026-09-12 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e4494ea5-51dc-3012-a4f8-236014a13be9 | -12.1388 | -48.9672 | 2026-09-12 14:50:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 454b5183-4268-3894-8139-3fb7a65c7eb6 | -13.3761 | -51.698 | 2026-09-12 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e491fb53-9e6f-36af-97d7-c9a14aa1e12d | -10.2206 | -50.373 | 2026-09-12 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| d816be9e-3430-3df5-9ae2-cdddd374f77f | -10.4909 | -51.3634 | 2026-09-12 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| c8ee3fa3-8e3f-3a87-a327-dbfa806a72f5 | -6.5002 | -47.6128 | 2026-09-12 14:50:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 7e6f4daa-58b3-3069-b30c-850e82e8b83c | -7.2147 | -43.7001 | 2026-09-12 14:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| df2d2274-7ae7-388a-a3ed-a10a0c315266 | -10.6827 | -54.1679 | 2026-09-12 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.4 |
| e011eed2-603e-303f-abb1-c41d8bb34e59 | -2.7148 | -57.6274 | 2026-09-12 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| f69554c4-e2fd-31ce-876f-e8d2289cff9c | -8.043 | -43.7565 | 2026-09-12 14:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 144.1 |
| c1331a8f-c151-319d-a22b-66e656cd90d0 | -11.4357 | -51.4351 | 2026-09-12 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| a4437496-eaee-312a-a0b0-c51ccfd26a19 | -10.2735 | -45.3185 | 2026-09-12 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 3c3faac3-402b-32fe-93d3-bf89cc777129 | -8.7943 | -46.9514 | 2026-09-12 14:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9388d38c-00a3-377d-b546-720947eaff0f | -10.2362 | -45.2775 | 2026-09-12 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 0616ac10-7bc9-3eb4-8434-c282d8e859d0 | -11.4021 | -43.9585 | 2026-09-12 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 98f90707-dc08-36d5-bed3-ce982ee2a8dd | -13.3189 | -51.6839 | 2026-09-12 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 19d9202a-6297-3490-8179-3ba938316cc8 | -11.436 | -51.4139 | 2026-09-12 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| f846cdf9-b6db-34aa-ac5e-e784a3631522 | -6.7832 | -59.4401 | 2026-09-12 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6d02f7e5-8d71-3be3-a798-0b790f9218dc | -6.2429 | -51.6939 | 2026-09-12 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 4996e6f8-8975-3e35-a2f6-b56e407e54bd | -9.7927 | -47.0895 | 2026-09-12 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b57908e2-ec15-32bc-8a11-fb3a368fe4ac | -2.7331 | -57.6271 | 2026-09-12 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 8775ed2d-4d30-3bb7-8df3-8353c3ceb4e6 | -2.7149 | -57.608 | 2026-09-12 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 0fd02d4e-cae2-33af-ba42-a141ab48d2d2 | -5.8676 | -49.7651 | 2026-09-12 14:50:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| af56bd4e-5a5a-362d-94c2-aab25c1608c2 | -11.0839 | -50.8368 | 2026-09-12 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 833a3040-a882-327f-b16b-9bb0a1219789 | -7.6008 | -46.1288 | 2026-09-12 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 6d1bdc5d-479d-30f1-b784-536c47b042b1 | -10.2929 | -45.2932 | 2026-09-12 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 41a210d0-c0b2-33f8-a4ec-6a3e3fb1cd2f | -5.8491 | -49.7662 | 2026-09-12 14:50:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 5aa7bd78-e2f0-348b-b0c3-3599e8d79b2a | -6.1046 | -55.6367 | 2026-09-12 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 55593e57-51a3-354d-a123-95e13a74f238 | -8.0748 | -54.8499 | 2026-09-12 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 7d843cdd-b8dd-334c-bb87-d550a38f42ab | -6.7648 | -59.4408 | 2026-09-12 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| a0480a8d-38c5-324d-a849-858f4eedd07e | -11.2833 | -44.1868 | 2026-09-12 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 5088b3d5-f0d1-39c8-92a5-40f9b6408f7e | -10.275 | -45.2268 | 2026-09-12 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 4f9c3f53-0d2c-38ab-ae2e-3934fc4ac052 | -11.3825 | -43.9849 | 2026-09-12 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 23f70c6a-ff27-38e1-945c-6a42306e3562 | -6.7692 | -58.6679 | 2026-09-12 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| aaec79c7-da28-3e8c-b931-e367f737e269 | -10.2926 | -45.3161 | 2026-09-12 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 63c1b151-ccda-33d1-a9e2-f68b1c26f76e | -10.2171 | -45.2799 | 2026-09-12 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 199.2 |
| 2c734535-f098-39cc-9361-15e80d874e94 | -10.2175 | -45.257 | 2026-09-12 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 72be4120-7e96-3aee-98e2-0d8726139e4b | -3.3504 | -59.4274 | 2026-09-12 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 59487abd-d108-3a13-b7c3-0866e210d16e | -14.5912 | -52.6673 | 2026-09-12 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 4712333c-509c-3ad7-b6f4-bae96cbaf1fd | -11.383 | -43.9614 | 2026-09-12 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 390a95c3-13b7-3a6d-b41e-a4085054c380 | -3.3687 | -59.427 | 2026-09-12 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 156e36e5-0ad8-322e-946d-7bfa95d68fa2 | -10.9491 | -48.3474 | 2026-09-12 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 010cdc6f-0be4-3d17-a107-35c17373a38e | -6.5004 | -47.5909 | 2026-09-12 14:50:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |


[Clique aqui para ver as próximas entradas](README63.md)
