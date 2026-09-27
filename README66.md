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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcda4db6-49c6-3c7d-aae4-05b32d086a5d | -12.1112 | -50.7215 | 2026-09-27 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 6a5b7503-8d79-3777-98ee-50b97d548572 | -12.1109 | -50.7429 | 2026-09-27 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| c53ef86b-514a-3c43-88fb-cc03592b318d | -12.1106 | -50.7643 | 2026-09-27 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 6e29e740-40f5-32ca-bea9-c29311256f4e | -11.3043 | -51.3434 | 2026-09-27 17:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.3 |
| ba715fae-5590-3c17-95b9-7ed68b40225a | -12.1754 | -50.2635 | 2026-09-27 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| eb018453-bfb2-3c46-bed4-f810de898970 | -12.3706 | -62.4459 | 2026-09-27 17:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 0dfd0498-61a6-32cf-983e-f57379e3870f | -11.0393 | -51.329 | 2026-09-27 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 8a052ae3-24d0-3986-b477-51cd56359f42 | -11.2281 | -51.3727 | 2026-09-27 17:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 125.4 |
| c7ee701c-1339-3f55-a5b0-f6c8702290b8 | -10.11 | -50.1708 | 2026-09-27 17:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| c7aedfdb-ab7a-3d85-937a-b9e70a4f3c7e | -12.156 | -50.2874 | 2026-09-27 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| e6c5f165-1399-39d7-a5be-1b0a9c0582a5 | -12.1553 | -50.3305 | 2026-09-27 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 8c81f72f-44b0-3980-96c0-2c36a44a43b4 | -10.0162 | -50.1374 | 2026-09-27 17:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 191.9 |
| d9bffd82-b48c-3328-862d-10144b6764bb | -12.2639 | -50.7034 | 2026-09-27 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 72c36c60-ba34-3956-9a79-e22a7ba2e888 | -12.1751 | -50.2851 | 2026-09-27 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 0f4a9e36-df84-3407-8d1a-596f9a3680cb | -12.13 | -50.7407 | 2026-09-27 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 433950a8-8618-3734-8bda-c110716774b4 | -12.1744 | -50.3282 | 2026-09-27 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2fe0ba2c-2fc4-3948-b1ec-1eb2d9413083 | -11.2853 | -51.3454 | 2026-09-27 17:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 5f6d65d1-f10b-3cbd-9d64-8caec70733ca | -6.8 | -45.01 | 2026-09-27 17:15:00 | MSG-03 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57daf0d1-800a-3a1f-b296-21913466f530 | -14.17 | -44.37 | 2026-09-27 17:15:00 | MSG-03 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 948abbb1-9ade-3cda-83f3-90e898a9d759 | -8.36 | -44.2 | 2026-09-27 17:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c79217c0-8edf-3c3b-a98e-b9045a8b4919 | -13.46 | -46.3 | 2026-09-27 17:15:00 | MSG-03 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e699293a-cf63-3547-9a43-bd3814019dd4 | -8.16 | -44.44 | 2026-09-27 17:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ad09a181-98ee-3b62-ad1d-65f634586303 | -6.8 | -45.05 | 2026-09-27 17:15:00 | MSG-03 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e869ea7e-a9d0-3625-950c-823a46e3a8bc | -12.65 | -47.25 | 2026-09-27 17:15:00 | MSG-03 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14a6e925-9bdb-3b2b-9248-afa6ace2890f | -11.04 | -54.01 | 2026-09-27 17:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce3076b-6674-309a-9b6b-69c39704cd4f | -1.04 | -47.5 | 2026-09-27 17:15:00 | MSG-03 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8df68bc9-e2b5-3abc-ae87-1aaefcd8f54d | -14.47 | -45.27 | 2026-09-27 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23cfb8d0-e248-371c-b41f-cadefa03c424 | -1.04 | -47.55 | 2026-09-27 17:15:00 | MSG-03 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e001476-8e43-3149-a2ca-f2633cd993df | -14.47 | -45.22 | 2026-09-27 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24c8d1c9-cc37-306d-a744-6117b5fbd591 | -11.01 | -54.0 | 2026-09-27 17:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24115aff-0de4-34f4-b47c-0d61e47b15e7 | -5.51 | -45.48 | 2026-09-27 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffdb6926-cfdd-3a49-a89c-4fa9d37adcee | -12.65 | -47.3 | 2026-09-27 17:15:00 | MSG-03 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bd4141c-92c0-3fcd-a997-6dbce9c3cca6 | -10.0909 | -50.194 | 2026-09-27 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 6cb1bd97-df8f-3820-944a-44d1dcb1f325 | -11.304 | -51.3646 | 2026-09-27 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 918b83c1-0fb1-3025-81c0-6f1232f0140d | -12.1932 | -50.3474 | 2026-09-27 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| d2766227-bead-3df3-aefb-857c5bb10c5a | -11.0988 | -51.1324 | 2026-09-27 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 4e36e782-13d4-3ed4-88d3-3434d581d020 | -10.749 | -60.729 | 2026-09-27 17:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f4db5e70-0c7b-3ddf-9131-03c8e1ffa22b | -11.2856 | -51.3243 | 2026-09-27 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 6de0f53e-5f4b-3f3a-813f-89443f05d58e | -12.1303 | -50.7192 | 2026-09-27 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 4abe3da6-8301-33d3-927b-b01aefe49594 | -11.3043 | -51.3434 | 2026-09-27 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 3bf631b5-df99-3dec-a799-caf6f793b5aa | -12.1747 | -50.3066 | 2026-09-27 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| ecd865a7-35a7-38d4-918a-7f4a74616112 | -11.79 | -50.5664 | 2026-09-27 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| b7dca5be-8826-31a3-9a4e-d5df6413f33c | -11.1524 | -50.0172 | 2026-09-27 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 21d8ffa1-1985-3048-a178-471f45c0ee94 | -10.0162 | -50.1374 | 2026-09-27 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 209.1 |
| ff0cb1c7-838c-3729-94b1-229a2f684907 | -10.11 | -50.1708 | 2026-09-27 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 361f9354-3b66-3157-a58e-2fb0759b6f3b | 1.5649 | -56.042 | 2026-09-27 17:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 1118bad1-1230-3afe-a612-6c552b103f9e | 1.5834 | -55.8645 | 2026-09-27 17:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 09fdc54a-4b41-3367-95ac-9e35d1162514 | -10.072 | -50.1959 | 2026-09-27 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 01670371-867f-31d7-ad8e-703026147b8b | -12.6071 | -51.9595 | 2026-09-27 17:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 179.4 |
| ff1f32bd-4d51-3f00-8a02-d5c106f4b6a7 | -11.4162 | -45.3486 | 2026-09-27 17:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 0db63dbb-af71-32a2-a4ce-63baf2ce743e | -10.1098 | -50.1921 | 2026-09-27 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 0f13eedc-48d3-3181-b72f-badfd618d78f | -9.977 | -50.248 | 2026-09-27 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 838ad201-95dc-3040-a41b-9ee8063317b3 | -11.924 | -50.5081 | 2026-09-27 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| cec8c804-80b6-3458-b14f-8593ffcc8bc3 | -11.2281 | -51.3727 | 2026-09-27 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 131.1 |
| b79c6814-7ac9-3552-9a69-041fe1c0ed35 | -11.0991 | -51.1111 | 2026-09-27 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 1ca9e06a-7d5e-339d-9cf5-ed3bfbb42aca | -12.1112 | -50.7215 | 2026-09-27 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| ea32aa5c-2a68-3db3-8eae-7fb6848e8407 | -11.8672 | -50.4933 | 2026-09-27 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| d47e6544-d3e0-3aa6-9870-3a8ce6e613fd | -12.1109 | -50.7429 | 2026-09-27 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 1bbdb6c5-56f4-346b-af96-6d4e5eceaa6c | -13.4325 | -57.061 | 2026-09-27 17:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ffa4ea04-477d-34bf-902f-cad083106698 | -10.0159 | -50.1588 | 2026-09-27 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 196.4 |
| e35bab7e-2706-3ed8-b0b9-1be4c1521987 | -12.0915 | -50.7665 | 2026-09-27 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 411c8769-e100-3554-85e3-712c837f407b | -10.0531 | -50.1978 | 2026-09-27 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 72744e0e-6632-3095-97df-339611b9785d | -11.2859 | -51.3031 | 2026-09-27 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 36304be8-7292-3beb-98c6-a47f0327f900 | -11.2844 | -51.409 | 2026-09-27 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 1aa62093-2b52-3b76-b97f-cc37635b4964 | -11.2853 | -51.3454 | 2026-09-27 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 09e29fd2-593f-3af3-8af2-099ad4350021 | -10.6889 | -50.6658 | 2026-09-27 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 47a76643-07c6-3a4c-aa67-4dfa5b5656c3 | -11.0424 | -54.0336 | 2026-09-27 17:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 487.7 |
| 0ce618cb-cdfb-339c-ab7c-5dbeea0a6fc4 | -11.9803 | -50.5657 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| c66655f6-a862-3721-a9ed-831c073b87ab | -15.9869 | -54.9419 | 2026-09-27 17:30:00 | GOES-19 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 72a48c0e-da1d-3273-b2df-20bab1028fd8 | -12.0997 | -50.2297 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| b5ce637e-2cd6-3ce4-b444-58664d7ce5dd | -11.924 | -50.5081 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| a4efd7be-c448-37b7-89ce-f8206713cfad | -11.9612 | -50.568 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 187e47be-f446-39d7-a7e7-bee2c6721e17 | -2.0379 | -49.5582 | 2026-09-27 17:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 322ab528-b362-3c84-8a83-6899db1d6b9b | -11.0991 | -51.1111 | 2026-09-27 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 46a7251c-c8a3-3d8a-9095-53b8469c8c4d | -10.6889 | -50.6658 | 2026-09-27 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.1 |
| b820217f-3d7a-3363-bccb-6f5e5eb16a35 | -11.3043 | -51.3434 | 2026-09-27 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| abb5c19d-0272-3a76-aed8-4fd62f4fad41 | -10.9861 | -49.7131 | 2026-09-27 17:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 5b45b7a3-39b0-3048-8811-b36cd4d068fb | -11.9053 | -50.4888 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 7133d164-fca5-3f7b-ba63-b7e47638ece0 | -11.2853 | -51.3454 | 2026-09-27 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| b54d8d9a-f7cf-328d-86cb-e2b686c9da65 | -10.8944 | -50.8569 | 2026-09-27 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 041448de-2024-3747-956d-d97e7a43a8e2 | -9.9582 | -50.2499 | 2026-09-27 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 148.0 |
| eac79755-7c97-38a1-a951-088b93e53796 | -11.304 | -51.3646 | 2026-09-27 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 59d6d9b3-e8e6-391a-8b25-3771bba33c6f | -11.6009 | -50.5025 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 342ba9f4-60be-3bdf-a9d9-4f6a8e9f7d19 | -11.3046 | -51.3222 | 2026-09-27 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| f1e68684-1dc1-355d-86e5-78ac4bfd0a51 | -12.1372 | -50.2682 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 48b910c5-58e7-3001-9574-4551c2526557 | -11.8669 | -50.5147 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| ba045100-2f68-3174-a567-8654de1b2840 | -11.8094 | -50.5428 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 64247539-bb82-3aa1-9e49-ef7a8ef5874a | -13.4325 | -57.061 | 2026-09-27 17:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d137b39a-bd2d-3ed7-91d9-b50db81a7ac8 | -11.9428 | -50.5273 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| b3845dce-f904-346f-ba52-7ea290159862 | -11.2856 | -51.3243 | 2026-09-27 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 78bd8e48-b9ce-3b0c-8738-3dd11975b88d | -11.6199 | -50.5004 | 2026-09-27 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| f88b9e25-7b76-38bd-bbfb-4950895bbcaa | -12.3706 | -62.4459 | 2026-09-27 17:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| bc799dee-1d08-3b4c-8078-4590f228306c | -11.3046 | -51.3222 | 2026-09-27 17:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 09cae4b5-8306-3fe0-8ee8-f636fe94a7dc | -11.5818 | -50.5047 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 6200de20-6554-3e32-a8c4-f52d65d294e4 | -10.0159 | -50.1588 | 2026-09-27 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| ad61444b-ed56-32fe-99d8-226d51df3f85 | -10.0162 | -50.1374 | 2026-09-27 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 184.5 |
| e89c984b-24b8-37fd-8149-2aca1fd3df09 | -11.0991 | -51.1111 | 2026-09-27 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| ddac88f8-3442-3df1-8d26-80cb27e203e8 | -11.5815 | -50.5261 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 269.7 |
| e42c2a20-0479-33b7-80dd-e7c30935900b | -11.6954 | -50.5345 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 03e305f2-6ee9-3cd7-b861-048e96cfb980 | -9.9318 | -49.3733 | 2026-09-27 17:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |


[Clique aqui para ver as próximas entradas](README67.md)
