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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c33f6c11-deea-3c79-8dd4-d369d982b451 | -3.21474 | -47.12648 | 2025-09-16 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cf12db51-f4c4-3b1f-94c4-8510eee81b5a | -6.1589 | -45.11234 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4fde7b3-fc6b-3254-9eb6-1edec161324c | -6.40726 | -43.33279 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a859c14b-f37b-37c7-9a2b-e22534d2de63 | -5.78778 | -43.89514 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6f2bcad-e2e7-3726-8850-51ac3b492bd9 | -4.60028 | -43.32317 | 2025-09-16 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 327fc931-a3a9-31ef-9e88-b7a47f53198f | -6.41273 | -43.333 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98028696-1244-355a-b09b-c39167f72435 | -5.90446 | -45.72705 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f00131d8-0420-37e3-874c-db563ccb254f | -2.29892 | -48.145 | 2025-09-16 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e33e1b1b-7d99-3ec4-abf1-ac01a5099f6d | -6.15771 | -43.66467 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc39d03e-5dfc-37d1-bff2-27a939b2b8c2 | -6.18836 | -41.19443 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8bbd29b8-b46e-35f0-b5c8-d7e10fdc978c | -3.42136 | -43.16738 | 2025-09-16 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26e4cad6-66d9-3698-9858-1afb909d4c26 | -6.28605 | -44.08997 | 2025-09-16 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6381dad-2b22-3c49-ba9a-4b75df9a383e | -3.83108 | -44.10518 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b0797a8-dcf4-3753-a061-328605242d65 | -7.06327 | -44.1726 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acd408b0-85f7-34de-90b1-a6883ab0c515 | -6.52869 | -44.13747 | 2025-09-16 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ea92c9a-7827-3a8f-a124-36cbffb65bcf | -5.80355 | -45.70055 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1047145-6757-3d76-9260-7866459ef7bb | -6.82719 | -47.85746 | 2025-09-16 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4594e44c-f6fb-35de-a345-767ddd27c34c | -4.17809 | -48.56986 | 2025-09-16 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0771a659-efd2-3c89-a3d7-86d4e56165c5 | -5.79295 | -45.93728 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9b564e2-5e86-398a-9ba8-10993ac085c8 | -7.26389 | -46.60744 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8256ab51-f898-398c-897a-6e85927b639c | -7.42451 | -44.86576 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 625a293c-33eb-3cf8-8d13-8a05edd86538 | -5.77965 | -45.93878 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d526d699-7222-3c03-9dee-0eafa3cb7785 | -5.88841 | -45.74232 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0708f8b2-fc1d-3a84-ad22-bff8213e6604 | -6.1834 | -41.20139 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4068357b-65c3-367c-9d5c-5fbd69c009d1 | -3.82824 | -44.10102 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaf1598a-b3d7-3b85-8c4b-2c5fafa41f4e | -6.44241 | -46.11056 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c42b196d-9570-3dce-9fac-fa242812c000 | -5.13975 | -46.39231 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ae955a6-0cfc-3372-8981-e5957abca476 | -3.84241 | -44.09951 | 2025-09-16 04:27:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78f9ec05-e577-3fc0-b6de-79b6750ebe51 | -5.1952 | -45.5876 | 2025-09-16 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6ea426b-d6dc-307b-bcb8-25a167ac997d | -3.07431 | -48.81629 | 2025-09-16 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de9abba3-ef97-3467-bdd4-990aa9927ab2 | -6.40966 | -42.65216 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7982a5a5-25a6-3489-9804-fd4ac2537765 | -6.6339 | -47.88611 | 2025-09-16 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6f57216-b3b3-3727-bdfd-529ebf725e95 | -3.21719 | -49.17323 | 2025-09-16 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b300cc9b-9ec5-37d6-957a-a17d22f54062 | -5.77316 | -45.52443 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bd3907d-15f4-39b0-819f-289acb033345 | -7.09035 | -39.67061 | 2025-09-16 04:27:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 094aa30c-b553-3672-98ed-a4b55e2c5206 | -6.18482 | -41.19032 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d15735f8-8d7f-3840-a3b8-cf4ffa962bd3 | -6.17746 | -45.14793 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c8f0586-f8fd-34ae-a193-bb80315ad0d1 | -6.39795 | -41.75606 | 2025-09-16 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 827d62b2-0353-3d13-8327-feb2ea7714e9 | -5.66583 | -43.32224 | 2025-09-16 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 803e80a9-9cbd-34ad-bbdd-d416b508d6b9 | -6.40766 | -41.79775 | 2025-09-16 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 457b1b67-5b7a-3104-a409-87d77a84a0ff | -5.77792 | -43.91312 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b4d5a7c-38d1-33d4-92b4-95f2dea9d6f9 | -7.26722 | -46.60797 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe0e9862-70a2-3957-8d78-9d6471444993 | -5.98955 | -43.70475 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec62a129-e8e6-3f5f-b1b8-8efc8f05c185 | -2.92871 | -49.14162 | 2025-09-16 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02aeca4d-3194-3303-8c8c-7fcde0997cd1 | -3.83901 | -44.09898 | 2025-09-16 04:27:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 37668487-76e1-3533-8815-84ee24498367 | -6.97595 | -44.53767 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b80f746d-19db-3094-8905-7e7cff4ebaff | -7.51484 | -44.66358 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df323026-aee4-32c4-a37e-60d8669de488 | -6.62277 | -44.72962 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0687bfe-eb43-3da4-b681-387727615be1 | -7.67986 | -44.47352 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adb7a6c1-f295-3030-a805-1e376c3ccde9 | -7.0598 | -44.17203 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af2ae0a7-feb2-3a86-80d8-fb2a85e23dba | -7.31571 | -43.95611 | 2025-09-16 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97a0fca5-e60f-3a02-a91f-4dbf39919af2 | -5.80169 | -45.88181 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 368ae314-f906-35ca-bee2-42c21883e5db | -5.53571 | -42.6611 | 2025-09-16 04:27:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 6efde624-39bb-373f-bdb3-a681bbb9462b | -7.04995 | -44.16651 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eebc7f2-1639-3c5c-a66c-2e707a8e557a | -5.77377 | -43.93287 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 300539e2-cf94-3a54-9c94-e6caa513f06c | -6.18859 | -45.1207 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41be8035-0bbf-37fe-b076-0d6e8492c5e3 | -3.21815 | -47.12701 | 2025-09-16 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 540d70a6-cd6f-3212-8eeb-fc79108e4190 | -6.45047 | -45.99434 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22c8b817-90b7-37c5-94d7-b85f80353e4a | -3.88957 | -47.60406 | 2025-09-16 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5423939-ef32-3cf8-968d-ac35479cbc61 | -5.54211 | -46.41334 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aad8db6d-f87f-3ba0-9660-7f0142af5ed4 | -6.09986 | -52.25232 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45a1229d-e0b1-3369-a194-9833cecb6d9a | -5.59624 | -45.36034 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0e20ee1-1e52-363b-82b7-8e45e103a04b | -7.59696 | -42.2527 | 2025-09-16 04:27:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1b4a4130-4707-3677-b5a3-1aca78525abc | -2.03362 | -47.04512 | 2025-09-16 04:27:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78daa429-9cf2-3dff-b88c-39d9366d7874 | -6.68266 | -46.30542 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3d391b3-ed6d-3007-a91e-f7786229b8f8 | -5.55699 | -44.96453 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb9f3684-a71f-3ab3-a9fc-0c4189b78a4e | -5.76682 | -43.93179 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bf8246a-c2ae-30ec-8ebd-e45185a5f07f | -4.8565 | -46.79111 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63be13b5-ebfd-379d-9085-1891a1562c40 | -7.02004 | -44.52518 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51bc217b-7191-3e16-8d87-0fcd345dab84 | -6.14246 | -41.19865 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6cb6c620-4126-3b4a-8f49-b6f32f5f5e70 | -6.37117 | -44.41317 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f6fc481-3354-3fe5-bf85-ff9dd5ca2593 | -3.84185 | -44.10313 | 2025-09-16 04:27:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10567af3-e468-3b05-a7c5-eb521b191659 | -6.12474 | -42.9456 | 2025-09-16 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f97994ff-7644-31b0-945f-01288eb27169 | -7.56075 | -43.95478 | 2025-09-16 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0941d4fa-d03a-3803-9700-237bd15991a3 | -7.26609 | -46.59352 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1f80b4b3-b4b1-3b02-b09d-a5b4b3b46ac0 | -3.81189 | -41.56439 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| eef42c07-a165-3af0-8baf-72220a3f6e20 | -5.77523 | -45.9452 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f8ba996-c2d2-32cf-930c-e2c306e41b34 | -7.66833 | -44.47946 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f909dab-67b0-39ec-a6f4-215e06e237ab | -6.45172 | -43.31794 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa8e6ebf-2e60-326e-86c8-ab11bbc2338e | -6.42897 | -44.38025 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cb5d576-79ff-362e-840b-fe42c138643a | -5.79459 | -45.92692 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bae1e412-b514-3466-8d65-77445a91fddf | -5.6346 | -45.33403 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d68c7569-511f-326d-b2e8-1926a33cdb1b | -3.81787 | -41.55088 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2bd3b332-4a02-3d6a-8742-a3244301cb0a | -4.15579 | -46.78945 | 2025-09-16 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13425034-5c34-33e2-a1c9-97212346a369 | -6.91745 | -44.5369 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7d4bb36-d396-3fed-9cb1-3b8d34b0ab0e | -7.27052 | -46.58709 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2487cc4c-c8f2-39d8-90e8-d83e1dceb950 | -5.1132 | -46.06834 | 2025-09-16 04:27:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d93611fb-4ae6-3d53-b997-1d02c5775d98 | -6.52289 | -51.19733 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae41489e-1766-37de-af90-0caca3268760 | -6.18243 | -45.11608 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 340dfddc-26e8-3f44-8746-d4e14cd89ada | -4.17743 | -48.57388 | 2025-09-16 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80eb1097-8add-32f6-95eb-965a51d0622e | -7.53831 | -43.98375 | 2025-09-16 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa2843d6-d460-3538-92c0-69875e1c4289 | -7.21529 | -47.00012 | 2025-09-16 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 466b0d57-9a74-3917-bb1b-23d62dd55de4 | -6.16562 | -45.11342 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc6eec7e-ef8c-3dc0-a918-3a1fc15385ff | -5.74947 | -43.92907 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceeb7775-e3d1-3210-b875-1f28282ff33f | -5.97573 | -45.83058 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d9a7ca7-b03e-320f-b23d-b747bc647c27 | -5.79529 | -43.93921 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c260a36d-cbdd-3bb9-9e48-2c76fcd9e8f2 | -6.16285 | -45.99555 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba56b82b-f6bc-345a-9556-b2339b6eac1e | -5.19575 | -45.58414 | 2025-09-16 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 490a2aa3-c8bd-35ae-954e-860ce730765e | -6.17605 | -46.81354 | 2025-09-16 04:27:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f413c7e8-c5e7-3621-bc9c-8a5e707f63bf | -6.40663 | -43.33684 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README38.md)
