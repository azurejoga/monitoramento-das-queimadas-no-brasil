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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bca1ef2b-a33e-3377-967a-2adaf441912a | -12.2692 | -49.1689 | 2026-09-19 14:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 7a23fbe6-9b17-3c88-a678-ffb7d0114d27 | -8.4737 | -47.0053 | 2026-09-19 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4d69d1ed-df4d-31f3-a758-ec53e28ba977 | -6.941 | -55.0366 | 2026-09-19 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 76d0db81-825a-3420-9d16-8ff771e89c88 | -6.0194 | -51.81 | 2026-09-19 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 099b7475-f4c9-3bda-abb4-60acf2e041b1 | -12.1531 | -46.9707 | 2026-09-19 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 184.1 |
| bf5d7c95-68e4-3306-b99f-9590281d0c21 | -12.1527 | -46.9933 | 2026-09-19 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| e3254483-2f8b-3398-b08f-6cf6b58905dc | -2.8974 | -57.8181 | 2026-09-19 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 18af77a0-83fc-30d9-94d6-8a5bfe2a08b6 | -9.0096 | -44.9209 | 2026-09-19 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| dee3c29d-a787-3711-a2e5-685ac2520d69 | -3.7129 | -60.6022 | 2026-09-19 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 17aef89f-bc98-3256-9904-83042e0eb50b | -10.7133 | -50.258 | 2026-09-19 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 84a3ede4-b5cf-3dc1-a85b-55103b6bc1bf | -7.026 | -42.0924 | 2026-09-19 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 162.3 |
| 88b8c1c4-9ee5-3772-a93a-fb93ff8c1971 | -9.7501 | -46.0863 | 2026-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 1a3bffc5-44e4-3a50-a1f7-6d1effcaad5a | -7.7118 | -44.6451 | 2026-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| dfbfac94-f166-34e9-8c63-e0fcdb82ffb8 | -9.0355 | -48.7487 | 2026-09-19 14:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 0bed279e-d82b-36ad-9a53-de31803631a1 | -12.0241 | -51.4551 | 2026-09-19 14:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 8af32652-e20f-382c-885d-e026f3438e46 | -5.9344 | -42.0966 | 2026-09-19 14:00:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 134.4 |
| 2adc785d-a799-3a7d-80b2-a23f20b9bc5c | -11.8934 | -47.6322 | 2026-09-19 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 14514957-b0cc-3a8b-9afd-f41301d2578a | -10.7715 | -46.3001 | 2026-09-19 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 5043c15d-a99e-3396-9801-e0262b5b50e8 | -8.6628 | -45.4379 | 2026-09-19 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 4e52d117-4363-3649-8276-3862c3c7fd43 | -10.1369 | -45.5638 | 2026-09-19 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| c6c00570-dab8-311b-9de5-2a3b555bfb50 | -9.2567 | -46.2098 | 2026-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 7439a870-9a58-373f-ac9b-b2218d6953bb | -9.0167 | -48.7505 | 2026-09-19 14:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8a2709d7-7fb7-3680-82ed-c100c5ec4d0b | -6.2585 | -41.6617 | 2026-09-19 14:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 186.2 |
| dce18a21-7592-36b2-856d-4709dbdd01e8 | -2.8974 | -57.7987 | 2026-09-19 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 292.6 |
| 87bb6685-f865-3f03-a130-efe09f90186e | -7.5704 | -57.6766 | 2026-09-19 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 8bd3ae86-3127-3b23-800c-be7ed3684a53 | -12.7085 | -45.96 | 2026-09-19 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 272.8 |
| 523510a4-054e-3cc2-b81a-97ae14931c47 | -9.0358 | -48.727 | 2026-09-19 14:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 105.5 |
| cd52c093-35c0-333d-9490-2562841cbcf0 | -12.2883 | -49.1664 | 2026-09-19 14:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| b39a8737-a1cf-377a-ac0a-309cb14d7036 | -12.5761 | -49.1071 | 2026-09-19 14:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 4f58909d-270a-3f51-b083-e5635f5731bf | -10.5368 | -46.7343 | 2026-09-19 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| df82a772-10d6-3f8b-a8aa-2b57ccda965c | -12.6896 | -45.94 | 2026-09-19 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 2995c54a-c01e-3eb7-ad00-86001f0fc700 | -11.1035 | -49.4623 | 2026-09-19 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 61a568f1-dff4-320b-9f28-c06d0b44c1a0 | -11.0827 | -48.3095 | 2026-09-19 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 2df86238-ea85-30fe-8a6c-1b18a1bb982b | -8.4296 | -54.7262 | 2026-09-19 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 65cf6be9-e7db-32e6-8ba0-619e012d10da | -11.8546 | -50.0653 | 2026-09-19 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6c233097-a8a4-357d-b3bc-d01370ea953d | -11.8742 | -47.6348 | 2026-09-19 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| e3f2c963-e8c1-316d-8671-bd7acc68796c | -6.2582 | -41.6858 | 2026-09-19 14:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 150.7 |
| d146db3d-cfd1-3426-91fc-b682f7dd21ec | -8.8639 | -45.937 | 2026-09-19 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 0cbbe486-737b-3aae-b488-3412a03414cc | -5.6408 | -43.392 | 2026-09-19 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| fc45926f-ec74-369b-b23d-c02ec1eea8e6 | -5.1538 | -45.778 | 2026-09-19 14:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 961958f8-6b42-3915-8b18-796537b37bde | -8.4314 | -45.8467 | 2026-09-19 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| c01407f1-9948-3259-8f69-ac3636eec4ca | -11.1228 | -49.4384 | 2026-09-19 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 537c2dfa-96b2-3c3c-9a78-b48a32eeb50c | -11.155 | -42.7885 | 2026-09-19 14:00:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 148.6 |
| 4dab90a7-fd87-3ceb-b112-20dc04b40369 | -12.2688 | -49.1907 | 2026-09-19 14:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 1cd3007d-586a-3b90-8ccd-fc62e8ba4a45 | -12.5952 | -49.1046 | 2026-09-19 14:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| d37a5b0a-0bd3-31a0-b6ce-58941a211eec | -9.7504 | -46.0637 | 2026-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 153d3d0f-35a9-34a6-8e52-c0a58abf3256 | -6.001 | -51.7903 | 2026-09-19 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 050ba217-f4bd-3514-ab30-f4edd052f815 | -11.1369 | -54.0251 | 2026-09-19 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 333.8 |
| 55f5d82d-3a98-3077-9695-4b8af3ab6261 | -3.4455 | -58.1941 | 2026-09-19 14:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| bb17f772-8696-3340-ab6c-438353895806 | -2.8975 | -57.7793 | 2026-09-19 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 42a66ba7-5902-35a9-bf15-2df809cd7316 | -7.8598 | -44.8595 | 2026-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| b81a2897-ad5c-32e4-9120-1786a924962f | -12.1535 | -46.9482 | 2026-09-19 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 170.4 |
| a375ad22-409e-3006-b6c8-1c6806521692 | -7.7626 | -46.7612 | 2026-09-19 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| a5245b66-fe80-35fe-9ebd-ce6f1743297b | -12.4841 | -50.0532 | 2026-09-19 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 0da11c27-1b74-3b4e-9b49-804ce843f922 | -10.567 | -51.3137 | 2026-09-19 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 39946fb0-00c9-3f8d-9a06-723ea953209c | -7.0448 | -42.0906 | 2026-09-19 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 484.6 |
| a7fb0eba-a350-37f6-be4b-8d3b756d18b7 | -11.083 | -48.2875 | 2026-09-19 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| bd184eed-591e-381b-8522-eb25301f6102 | -11.8746 | -47.6125 | 2026-09-19 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 48fc758a-66c4-3865-83bf-005c5fdbac4f | -6.8438 | -48.8033 | 2026-09-19 14:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 0efb490c-3d7b-3bd0-8607-d12d73b33b0d | -9.2606 | -45.9164 | 2026-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 83366f67-68bf-3c41-9f29-c1da1ff3abe1 | -11.0611 | -49.7693 | 2026-09-19 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| faed047e-7305-37c4-b3c8-0163dfe73fa0 | -8.45 | -45.8674 | 2026-09-19 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| ddae0237-ea3d-3bcc-9d7b-5fc8da609711 | -11.3604 | -44.1521 | 2026-09-19 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 2c3b8de4-1cba-3717-98bb-15bf86967d19 | -10.5667 | -51.3349 | 2026-09-19 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 425cab88-e78a-3081-a49b-9933e8b81a53 | -2.8791 | -57.799 | 2026-09-19 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| d1b0998a-57f6-3791-bb70-8ce3f73edefc | -11.1038 | -49.4406 | 2026-09-19 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| a4d7e444-06c3-31fb-b2d0-86ea23fce378 | -12.4844 | -50.0315 | 2026-09-19 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 5b88b2dd-99c0-3f40-aab5-6ae1035a4e6f | -8.6173 | -54.5924 | 2026-09-19 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2bb6c322-b06a-3407-891a-80b7f54bdb3b | -3.9902 | -41.2759 | 2026-09-19 14:00:00 | GOES-19 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 5249228c-aaf4-36ae-9332-bf97e5ef851c | -11.0062 | -48.3407 | 2026-09-19 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 5adfeda2-5d8d-340c-8eda-8f8043ebafb6 | -11.0065 | -48.3187 | 2026-09-19 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ca4a1a0b-52d1-3f87-9810-b40bc380a056 | -11.234 | -48.3571 | 2026-09-19 14:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5fb98c6b-01ff-3d6e-8af8-95ed3d4fcea1 | -11.0801 | -49.7672 | 2026-09-19 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| d8279958-dfb5-3676-b613-81992c952d7a | -11.1545 | -42.8124 | 2026-09-19 14:00:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 119.7 |
| 465043e2-d20c-3462-a9c9-25719b8dfa42 | -11.7823 | -49.8152 | 2026-09-19 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9fa37b85-2869-3622-8c5c-41c26b592976 | -7.7629 | -46.7389 | 2026-09-19 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 6539519b-9cbd-3b16-8b4d-aa969cd4abcf | -2.9157 | -57.7983 | 2026-09-19 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 259f443c-426a-35aa-aa17-ee9520d5a9aa | -8.4503 | -45.8448 | 2026-09-19 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5db55bb7-cb25-3199-b7a7-f6e4da23e4b7 | -5.6596 | -43.3906 | 2026-09-19 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 45bdd09d-8364-305e-85d8-db9f7edb82d4 | -6.0196 | -51.7893 | 2026-09-19 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| f56a68e7-9af3-328a-be78-4162201b2c2f | -12.1339 | -46.9734 | 2026-09-19 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 85bbeb80-7367-32d3-8797-455c522050cc | -3.3311 | -59.8101 | 2026-09-19 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| c06c8964-0f06-3fae-b411-828413fed0b8 | -12.2879 | -49.1883 | 2026-09-19 14:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 15ee6b9a-0191-384b-a94c-94d925bca8f8 | -5.1351 | -45.7791 | 2026-09-19 14:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 7edbd036-9404-3b61-b200-f637f975e2c3 | -12.5032 | -50.0508 | 2026-09-19 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 5ee2e6da-84ae-3980-8ac0-1e047f5201e6 | -10.9133 | -50.8549 | 2026-09-19 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 6d393bd7-0fbf-3222-bb65-e77419c34249 | -3.6946 | -60.6025 | 2026-09-19 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| f7ebbdc1-f1d3-3994-936d-69f18e773db1 | -8.9412 | -44.3995 | 2026-09-19 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 147.2 |
| e5fdf66e-0f1f-3555-bf67-b16723f2605b | -7.8595 | -44.8824 | 2026-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| c7113b2c-b24b-3dab-b6e4-9f0f2c42160e | -9.784 | -45.059 | 2026-09-19 14:00:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 45c2d0c2-5add-3209-bb9f-0f280cc19e4f | -11.874 | -50.0415 | 2026-09-19 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e32d7fc3-05f1-3a02-818a-b6ea527f4ef0 | -11.3355 | -43.403 | 2026-09-19 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 523bcc20-256b-3a3c-922c-e95e4ff537c6 | -10.0956 | -48.4226 | 2026-09-19 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 3f6567e7-432b-3b72-b51f-160fde268356 | -11.8549 | -50.0437 | 2026-09-19 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 7d0f1715-bb03-3961-8d8f-2214f1dac744 | -12.0241 | -51.4551 | 2026-09-19 14:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 04f12cba-4fa3-3554-bc95-fea6d0d25173 | -7.8598 | -44.8595 | 2026-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 566fcd23-9d27-3c38-bf6f-42213e14b3f7 | -6.0009 | -51.8111 | 2026-09-19 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0e4595ce-d272-31b0-b1ab-358b885ca13c | -11.8549 | -50.0437 | 2026-09-19 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| d18d6edb-35d4-3eaa-930e-9767b18c687f | -12.2688 | -49.1907 | 2026-09-19 14:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 1c395dde-d53d-3708-aed4-a4e411f43d4a | -11.1035 | -49.4623 | 2026-09-19 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |


[Clique aqui para ver as próximas entradas](README113.md)
