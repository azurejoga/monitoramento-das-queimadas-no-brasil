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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad26a93f-1f86-376f-a16c-65d5a88da151 | -3.04775 | -48.01256 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51ff8249-45ca-39b8-a8f1-2f358624c4af | -2.1718 | -48.54815 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 993105cd-6e4d-3e3e-8fa4-64f117a1d5eb | -1.21329 | -51.7471 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dfa57e3-9399-39e6-a9af-78fc16899fec | -5.35843 | -44.37003 | 2024-11-14 04:40:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cec6f435-b92a-31db-9196-981fcce88e9b | -3.57824 | -43.82005 | 2024-11-14 04:40:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31e22a2f-2235-32d0-90d7-f86b085cac35 | -2.14543 | -48.80389 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86d40882-6f88-3a20-b57f-a2513b9bc7d3 | -1.55935 | -51.1617 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c00e8579-6623-3473-a16f-52787b2806e8 | -2.27039 | -50.81152 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0f772e3-7100-3b18-8f6f-b873dd83fe3b | -4.55721 | -48.01467 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e097c4f8-7316-3784-86eb-23c158c6e796 | -1.98996 | -51.09895 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 523b66a1-2961-3ce2-be87-e3094beee6bc | -3.41787 | -50.28059 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b49ec547-aa91-3746-a9b4-69963b57c8ff | -2.21757 | -48.3196 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c4ef8db-ef79-3e84-9b60-71ff31c85e21 | -4.13178 | -51.07425 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 761c5859-9462-312b-b280-d9f582c3b407 | -2.37828 | -46.49347 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 863a6718-8b36-31d0-ae1f-ac8bb2092761 | -4.07497 | -46.86478 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d9c6bcb-7fbb-3b3c-8294-2ea5d2c0f5b4 | -1.26506 | -52.13126 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a41f0567-ff52-3754-8c8b-b02de69b162c | -3.04144 | -50.33513 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29f9a10c-2d9e-39da-ad0c-a4905f85d3a9 | -2.64142 | -46.17338 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ca97e4c-a0d7-330c-b1dc-b639021c283f | -2.11304 | -50.69594 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f59de277-d787-3218-b314-b4b4e9dc4a7a | -2.67096 | -46.7335 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbfc48d7-d86c-35ff-b5b6-68c94862c84c | -3.01704 | -51.44025 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d45e5494-55bc-3b22-8374-63b2de9b22b2 | -2.71645 | -51.7108 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 472037be-6f32-3b67-b96a-031c04dd0d7b | -1.68912 | -46.57134 | 2024-11-14 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc01a5be-0594-3c84-99fc-2dc957e1ca9e | -4.58598 | -46.63008 | 2024-11-14 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63a43aa9-18e7-3179-aefc-9122da58a1f8 | -2.9272 | -48.06548 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b420ef4f-12c8-377a-96e6-13ac04447252 | -2.57855 | -49.21286 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1562c591-5948-39cd-a9f1-3ea7c0a8f5fe | -4.16199 | -46.24913 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e9b3129-3ae7-3c85-97a5-c8e5b50f9b99 | -4.00378 | -45.56387 | 2024-11-14 04:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c892b4a9-c8a2-37a2-afd0-052f199fc72b | -3.40613 | -50.31152 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b3970f0-9289-39ae-a6c9-fdcb27c7d6f5 | -1.55506 | -51.86096 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ca8f5249-3935-3f3d-9de5-f3d1436a6211 | -2.67427 | -46.82563 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cfe5282b-490a-35b2-a1b7-4140bff48bb9 | -2.90403 | -46.86011 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 153468a5-f5e2-3482-adad-0291f87869d0 | -2.668 | -46.82084 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06b033ab-6a2b-3e47-a9b9-dbba6cee7e19 | -2.37641 | -48.52364 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 994f7454-bcb7-3c55-a67a-441eceb6d1af | -2.1894 | -46.40003 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd4c5bac-d43f-32a2-ad79-da9de86ac5a6 | -4.02768 | -46.96595 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01a24094-7b18-3fea-9061-f954f83b0577 | -2.75246 | -51.62206 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b412f705-5df1-3e45-98e4-5e950f6cb00c | -3.03213 | -47.98158 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41f00367-9518-3cbf-893e-c477f9a8f615 | -2.47695 | -45.85216 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac4b34b8-8b0f-38f6-9605-9c35c21249fc | -2.08737 | -46.62746 | 2024-11-14 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b25d75d-031c-3fcf-a26f-78fb1f0bccd1 | -1.84735 | -53.69372 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e82fd7cd-b98e-36e0-bc2b-c387f6444332 | -1.46723 | -51.99085 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33677c7d-2ba7-359c-aafe-f78236eea062 | -2.08794 | -46.62374 | 2024-11-14 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b28f04fe-2c9a-399c-a730-ab1bd51861b2 | -2.66628 | -46.83195 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d5813f3-4afb-3d57-85cf-61a2b3d06b15 | -2.66035 | -51.72364 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a2a6c8f-b05b-36f8-837e-e850cc7395ab | -1.73976 | -48.63455 | 2024-11-14 04:40:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d99d04e5-c174-3982-acc2-c77e2fb5f87a | -2.32963 | -51.98679 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52623913-bfee-37f2-8b45-bc681740960c | -2.93844 | -48.32248 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f763fb1f-e247-3fe5-87f5-2f1d085b3b82 | -2.0271 | -46.94635 | 2024-11-14 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d3cdb9d-d894-3719-956a-27c32d976cd8 | -3.14635 | -45.97678 | 2024-11-14 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| caa9e7cb-ade3-30ff-8461-b5bfb161a3d7 | -0.89764 | -51.72756 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efdbbca8-acd7-34f3-b168-b67f61bd3147 | -2.83818 | -51.97527 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51187628-a19c-34cf-813b-e3d9de06a704 | -1.22251 | -51.78291 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5f3632c-3284-3845-97f8-332ebee51874 | -2.93513 | -48.32197 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a65b01d-bd0f-3564-a996-cd64659bbaea | -3.27295 | -51.26567 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96b11f37-107b-3d43-ba2b-657d15825b32 | -2.52541 | -46.51983 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fceb7329-1ded-368c-8223-569ee50f5c28 | -3.17263 | -45.44233 | 2024-11-14 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 867ced16-8348-38f9-9f75-d120fca7d287 | -3.9474 | -46.70884 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9d7bd88e-3b01-3ab7-a654-1390850e63d0 | -4.94483 | -44.95774 | 2024-11-14 04:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 87047ef0-cdd4-3526-b9d3-b30d350ad983 | -2.20228 | -46.8154 | 2024-11-14 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c39b7f7-ef11-3d98-a0cd-304d1686a84a | -1.63398 | -46.10577 | 2024-11-14 04:40:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6decb71b-6346-3362-9f70-b853791e7dd4 | -4.26521 | -48.18663 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2033a7cf-0d03-3bdb-ac97-2c925135dd80 | -5.19675 | -44.36151 | 2024-11-14 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd07e58a-930b-3960-9906-0da17c354dae | -6.57135 | -46.56435 | 2024-11-14 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15e58bf5-a4bc-320a-8853-53885b877512 | -1.87623 | -47.06063 | 2024-11-14 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df92029d-260e-3444-9be2-37e918d45908 | -3.223 | -50.58482 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55618941-9cd7-347c-96f8-a79eae56b6c9 | -2.17328 | -48.38669 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ee73947-5c34-3725-a47b-a0522bdc9b73 | -3.46933 | -50.3031 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af63884e-834b-3256-8b61-9dead7585524 | -2.65197 | -46.17498 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50b84bfe-37e3-3d8d-8192-a2fe1966c963 | -0.89632 | -51.73597 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67c39a83-0691-3b90-9cb1-192bacdbcd31 | -3.08962 | -50.4898 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36e29a7d-1163-3039-9fd3-6034653eed84 | -2.07275 | -46.56411 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb7112c3-3115-3ff9-a7a1-897b4a3cba68 | -3.43801 | -50.30554 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9d81e89-033a-34c6-8835-9503ca449c9d | -1.63108 | -46.10137 | 2024-11-14 04:40:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 114c0df8-bf8f-3b9e-a6c9-10bacc2eef1b | -4.98795 | -50.0313 | 2024-11-14 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdeb0e0c-78f9-3d2d-9cd9-91452d88b783 | -5.07199 | -45.50973 | 2024-11-14 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b5751fc-cd6b-39f0-bf8a-a603d0d2d686 | -2.64688 | -46.82142 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77cc4bb9-1f53-34e3-9445-388b89f928b6 | -3.43074 | -50.30805 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b3d15a2-6061-331d-ae1a-d08494be8cf6 | -3.77649 | -47.76076 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fb0914a-b883-3183-a635-628438cbe472 | -2.36682 | -48.84528 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ffcf7341-a08f-30ce-a859-f22d203eafd3 | -3.63869 | -50.59022 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ef25bd4-dca3-3704-8acd-50e62e818f1c | -1.66777 | -52.55282 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51265564-a62b-31a7-8505-fbbba497062e | -4.05829 | -51.02848 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 461b41ee-5898-3db9-8c86-7d2aab5cde99 | -4.26383 | -47.07373 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58ab0188-356d-3a7d-bfa1-334314ee0a7c | -3.05154 | -50.3367 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da5ed308-98a5-3105-a7c4-99c92d3080fe | -3.77259 | -47.76378 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 203d61db-a384-3f14-bdc0-e2459efac5d6 | -0.41771 | -51.58243 | 2024-11-14 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a669d228-c0f9-3ac7-8fee-c405fae0429e | -4.59141 | -47.041 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 616f202e-9104-3bfe-a580-a04a70e5a2f6 | -2.71176 | -47.98552 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4129ccab-1d9e-3057-b51a-dd125878980f | -4.7972 | -43.66406 | 2024-11-14 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10bdd191-b944-36bd-b6b4-4baa1873fcaf | -4.07439 | -46.86855 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f7996a2-f6dd-3002-8e8a-b1717ab708b8 | -3.40948 | -50.31204 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 71cb6840-5611-3b14-b42b-a246df7967a2 | -4.62986 | -50.90001 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 557e2c50-9f2c-3d6c-8619-ea7355ace708 | -1.36441 | -52.3352 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41b946bd-bad4-320c-94d7-ea5709eab6bb | -3.92033 | -52.2654 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c30c12d7-770c-33d2-8574-eb9654d94b29 | -3.77527 | -41.60685 | 2024-11-14 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0462cf4e-2c70-3ae0-bd50-51c8887b36e4 | -3.28455 | -45.36954 | 2024-11-14 04:40:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edbd29e1-0e48-3180-a725-231dc06f02bf | -4.05887 | -51.02477 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec691475-7637-3529-b7a9-f34e96b4d752 | -3.02686 | -48.05929 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 611a55d0-889e-3b43-b69c-46b10d7280b7 | -3.24755 | -46.51999 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README25.md)
