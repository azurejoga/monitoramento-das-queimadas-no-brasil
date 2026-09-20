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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6f580d0-bad4-3c3e-925c-c44f5b5f947b | -12.152 | -47.0383 | 2026-09-20 10:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 157eef58-64e2-376f-939c-d1ce319660fb | -10.336 | -50.2119 | 2026-09-20 10:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 985bcbc5-fada-329f-a91a-ebfcd14d640f | -10.3546 | -50.2313 | 2026-09-20 10:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| d6025c22-cffb-398b-832f-9fba35914368 | -10.3357 | -50.2333 | 2026-09-20 10:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 380.3 |
| 7dca67e5-d1ec-3405-b28f-345b71e45d6c | -10.3354 | -50.2547 | 2026-09-20 10:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 38e1534c-4aee-3e85-9424-5eeab93846da | -12.7428 | -46.183 | 2026-09-20 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| a87ca074-2bf1-3d28-87da-66dfb5d03ace | -12.7621 | -46.18 | 2026-09-20 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 64ea770e-7c53-37e7-964c-937f6d6de982 | -7.5334 | -45.4367 | 2026-09-20 11:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 30f468e9-fbf4-32be-a179-40c821f45ca7 | -10.3168 | -50.2352 | 2026-09-20 11:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 991fe05a-8e2e-3620-bfb4-d52eee48be72 | -10.3168 | -50.2352 | 2026-09-20 11:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 1b38332e-502c-3d52-a4b6-2370d7f5c2ca | -12.7428 | -46.183 | 2026-09-20 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 249.7 |
| 17200022-ba7f-334d-a413-96657a0db921 | -12.7621 | -46.18 | 2026-09-20 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 448.7 |
| e1956f12-4180-3b1c-9e15-b4f38edff080 | -7.5334 | -45.4367 | 2026-09-20 11:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 84632a17-4072-3ce3-8a47-8509b0ec5944 | -12.152 | -47.0383 | 2026-09-20 11:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 93edc643-6da2-3b0c-8f92-158e2f6c9609 | -12.7625 | -46.1572 | 2026-09-20 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 9ffdf78c-bea4-3910-b910-95de8df82e53 | -10.8659 | -50.1775 | 2026-09-20 11:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 79024173-7d70-3531-8483-d5b05bfd2120 | -12.7423 | -46.2058 | 2026-09-20 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| af619c85-c66a-3b14-9287-78f5649086a6 | -10.35 | -50.23 | 2026-09-20 11:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1946c344-40cf-31d9-95e6-7beadfbb9b8c | -12.7621 | -46.18 | 2026-09-20 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 275.1 |
| 753b5875-34c6-352a-b6c3-05cc537c68bf | -7.7631 | -46.7167 | 2026-09-20 11:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 6ea7893a-dd13-3935-87c0-7ffbb68c0b62 | -11.0991 | -54.0285 | 2026-09-20 11:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 1fe4a4ea-8144-3e9b-a730-f5e59d10b997 | -7.5334 | -45.4367 | 2026-09-20 11:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ca40305c-a840-3561-9e2a-6bdf61c364f1 | -7.5522 | -45.435 | 2026-09-20 11:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ae81b381-f716-3fab-acbd-533d950940a1 | -12.152 | -47.0383 | 2026-09-20 11:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5f404f60-2bb6-3944-9087-a1b5ddaa46fc | -14.6661 | -46.6919 | 2026-09-20 11:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 8efbee39-2727-3fec-b004-903325d2267d | -12.7616 | -46.2029 | 2026-09-20 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 258.9 |
| 723e18b6-6eeb-3274-acca-ec01ff06a918 | -11.118 | -54.0268 | 2026-09-20 11:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 562fc6c2-94c6-3bf0-9f4a-9d0273442b44 | -12.6423 | -50.9144 | 2026-09-20 11:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 659ac024-e40e-34c3-ab7c-6504cb5c61cb | -14.6665 | -46.669 | 2026-09-20 11:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 3670240f-4049-3c8e-90e8-c195c752b0c4 | -10.8656 | -50.1989 | 2026-09-20 11:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 44a0accc-308d-3141-adae-f67f757747aa | -11.379 | -51.42 | 2026-09-20 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 5aacce02-353b-37dc-9859-0fa2d9766167 | -7.7631 | -46.7167 | 2026-09-20 11:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 3a7834f8-4a32-3013-be57-59bf91d5d65b | -7.5337 | -45.4141 | 2026-09-20 11:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| ea678525-94a1-3aad-83b8-c2e6851124c9 | -14.6861 | -46.6657 | 2026-09-20 11:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 5f518954-b9fc-3597-afc6-851d132906be | -12.7621 | -46.18 | 2026-09-20 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 26124763-f0a3-3d64-bc2d-afae7b6de2d5 | -9.8313 | -48.4073 | 2026-09-20 11:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b7bca3bd-22c8-36fb-8da8-ee9c848cf3fb | -14.6661 | -46.6919 | 2026-09-20 11:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 291.6 |
| a1ee5a72-2465-3b6e-8ce9-fab74d388456 | -7.5334 | -45.4367 | 2026-09-20 11:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| c6c8717c-a0ca-361d-8a3c-2b672d2ff894 | -11.0991 | -54.0285 | 2026-09-20 11:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 6053fbf2-6d32-3881-8133-a1fbb5b5544a | -7.5522 | -45.435 | 2026-09-20 11:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 92fd8d4f-1c2b-3a64-aecb-811a0d3f15d6 | -12.7616 | -46.2029 | 2026-09-20 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 4cc8d5e0-885f-3ac9-9303-5b32d1b5127a | -7.7444 | -46.7184 | 2026-09-20 11:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 69146140-4c07-3025-8b97-df57bac9dc70 | -10.8659 | -50.1775 | 2026-09-20 11:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 2922cc77-20bb-304f-942f-dd0eef2486e4 | -11.118 | -54.0268 | 2026-09-20 11:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 140.1 |
| e49c0f89-0bf8-3c27-9839-647082858a94 | -9.7154 | -47.2091 | 2026-09-20 11:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 99ef0cc5-07a3-35b5-adfb-1915858935af | -8.4376 | -46.8757 | 2026-09-20 11:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| d44289ed-7c02-3b7c-abb5-1c1b0f086e93 | -12.6423 | -50.9144 | 2026-09-20 11:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 421702db-b486-3e26-9b4e-3ec035d98e51 | -11.0991 | -54.0285 | 2026-09-20 11:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| c5bfd0b8-f5ed-3cbe-a579-b00a7b6a0f98 | -9.7151 | -47.2314 | 2026-09-20 11:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b49b5aeb-27cc-3dba-bd31-365c7ba8f403 | -12.152 | -47.0383 | 2026-09-20 11:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 6c840cdb-1d84-3f6c-8e1f-a66973c6f74a | -14.6665 | -46.669 | 2026-09-20 11:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 134.2 |
| eb4ec4f2-63ae-3344-a6a4-eeb5890fa61e | -12.642 | -50.9359 | 2026-09-20 11:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 4e4bdb54-1009-36ab-a201-35db832d8276 | -7.5334 | -45.4367 | 2026-09-20 11:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b5c0abda-bbc5-352a-b7f9-e2867c65c84d | -10.8656 | -50.1989 | 2026-09-20 11:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 1cc9680f-f5ad-3782-91df-da416595425b | -10.8659 | -50.1775 | 2026-09-20 11:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 173.0 |
| c72d3e28-b0d9-3582-be04-96de345cd0f0 | -9.8313 | -48.4073 | 2026-09-20 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5a78b317-4012-30cd-94d3-dc801ceacb83 | -9.8502 | -48.4053 | 2026-09-20 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| fb28feec-68eb-3a11-8f4a-6a6d47050860 | -12.7621 | -46.18 | 2026-09-20 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| eb0a63f6-1c49-30be-8b50-2f2cb49d9329 | -14.6861 | -46.6657 | 2026-09-20 11:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 5444ce56-9ccb-3d50-9bbf-7994f6b26f84 | -11.118 | -54.0268 | 2026-09-20 11:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 174.9 |
| 15fbee03-71e4-397b-a1c9-4d39e42f9d28 | -12.7616 | -46.2029 | 2026-09-20 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| a4908498-68a6-33a9-bd61-c1dd335284a0 | -14.6661 | -46.6919 | 2026-09-20 11:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 442.9 |
| 95fc0b4a-e9fa-3654-bb53-41c53e538bee | -11.379 | -51.42 | 2026-09-20 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| ceecceb4-3318-37fd-9691-374adad6c083 | -12.6423 | -50.9144 | 2026-09-20 11:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 3975fc17-503e-384b-9921-c6b645d09259 | -12.7625 | -46.1572 | 2026-09-20 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 8254adc3-82a7-39ab-9e13-61399bc44ee5 | -10.473 | -51.2808 | 2026-09-20 11:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 85fad34d-2920-3e70-8b95-78e3d119713f | -11.118 | -54.0268 | 2026-09-20 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 71fc267c-952d-34ff-a0ca-4ac4f49f3419 | -9.8313 | -48.4073 | 2026-09-20 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| f239c997-b320-35eb-aaf2-dfb9c869db32 | -10.8656 | -50.1989 | 2026-09-20 11:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 83713f2f-8724-3a58-a9d0-a269ed4cb572 | -12.7428 | -46.183 | 2026-09-20 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| ed48133a-ff70-3386-90d5-b1738be59df4 | -7.5334 | -45.4367 | 2026-09-20 11:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 88462514-478b-3096-9fa1-f5916843033a | -12.152 | -47.0383 | 2026-09-20 11:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 57e1d02b-4e69-3629-b6d7-0b273a362fa2 | -12.642 | -50.9359 | 2026-09-20 11:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 6faffee5-cb32-340e-815a-5f6ae7daf1d1 | -12.1328 | -47.041 | 2026-09-20 11:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 1b5b13d9-8b44-3104-87d9-f97c57126ed6 | -10.8659 | -50.1775 | 2026-09-20 11:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 199.2 |
| 5d57197b-611c-37a5-b211-75a6334403f9 | -11.0991 | -54.0285 | 2026-09-20 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 01f8abc4-e1df-3b28-a88e-e683ba30752b | -10.3168 | -50.2352 | 2026-09-20 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 098cd4e3-fe5f-3bd8-92b8-ca5631e73d54 | -10.2787 | -50.2605 | 2026-09-20 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 67a74df7-127a-33a3-9b23-027f3b67e4ad | -8.4376 | -46.8757 | 2026-09-20 11:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| db2fe023-e517-386f-92b3-120c940d76ef | -11.379 | -51.42 | 2026-09-20 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 33affee6-0ef1-3f45-8869-9ea413a22b41 | -10.7899 | -46.3429 | 2026-09-20 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 84a812ee-ec99-3ca3-9432-b86c797c8e77 | -7.5522 | -45.435 | 2026-09-20 11:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 86a98c7e-3123-3d4b-a103-39e05384a3e9 | -12.7616 | -46.2029 | 2026-09-20 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 508.0 |
| 6a541939-616b-3ee4-a216-8c0fe343fb99 | -14.6665 | -46.669 | 2026-09-20 11:50:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| de5ec042-247f-3cb8-b6fb-24540008d687 | -11.0991 | -54.0285 | 2026-09-20 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 44c10384-568b-3b2c-b0e7-4dc34d9f71be | -10.8659 | -50.1775 | 2026-09-20 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 813c667c-0893-3247-b968-e38c456347f8 | -10.473 | -51.2808 | 2026-09-20 12:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| f9feefde-eb40-3e0d-9136-79be50228c54 | -7.5337 | -45.4141 | 2026-09-20 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 283.7 |
| cbcc9d91-2e19-3aab-a458-701b71b20233 | -14.6665 | -46.669 | 2026-09-20 12:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 1779853d-6d5a-388f-ac0d-01b39291e2aa | -12.152 | -47.0383 | 2026-09-20 12:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 46790d41-2bb9-3b6e-9bf1-3119f26d0d3f | -10.8656 | -50.1989 | 2026-09-20 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 2b705c0d-1a16-347f-bf0c-af4db3570cf4 | -12.1328 | -47.041 | 2026-09-20 12:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| dc9e5d72-1ec6-3488-be86-6106f35c4061 | -12.7612 | -46.2257 | 2026-09-20 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 7a9b0360-8f87-3ef7-931c-0dc0905eb8ea | -9.8313 | -48.4073 | 2026-09-20 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 2f80dfb6-cd11-3030-a43e-9dbd6c17f2e2 | -7.5522 | -45.435 | 2026-09-20 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 3236c5cb-8995-39bf-8e8d-a9c9f29386f5 | -10.2787 | -50.2605 | 2026-09-20 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d0f34432-8bcb-37e0-b871-4c6761a0303d | -10.8469 | -50.1795 | 2026-09-20 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b690aefe-4142-3769-bc79-b0e62bad5c32 | -11.3787 | -51.4412 | 2026-09-20 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3020df6e-0c99-392f-9fda-2963a04793f9 | -12.6423 | -50.9144 | 2026-09-20 12:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 5d9f0336-100d-32ea-89b1-0e64d82c8df1 | -12.7621 | -46.18 | 2026-09-20 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 231.5 |


[Clique aqui para ver as próximas entradas](README109.md)
