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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11838152-d122-38d3-8ea1-b26fbc927ea3 | -8.04062 | -43.09512 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 4e82b72a-1de7-3d80-8038-8a764ddd506b | -12.21024 | -38.98161 | 2025-12-12 03:59:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7090c52c-c38d-333a-b215-d97b8357fa2a | -12.12706 | -39.40475 | 2025-12-12 03:59:00 | NPP-375D | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c027057b-c36a-3027-ad1b-37fc7c104e81 | -6.95388 | -38.61297 | 2025-12-12 03:59:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4da71363-8fee-3ef7-8bf2-9f5a25a4cfed | -8.04285 | -43.10533 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8fdbccad-6449-3583-b6e6-7a8c15ae5d46 | -8.11948 | -48.01676 | 2025-12-12 03:59:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dac9f850-f372-3586-a525-a60418e4954c | -8.04446 | -43.09584 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c579f321-6c0e-3ed6-a06c-eaebc64d51c6 | -5.96737 | -44.0678 | 2025-12-12 03:59:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| babcb7e5-9535-3c08-97d6-f41fbb76dae6 | -8.03047 | -43.10817 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| f86afed7-07d5-3965-abb6-6ff97709e60a | -9.40841 | -35.65103 | 2025-12-12 03:59:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2beb8eb2-ff4c-3f0d-a121-b7994618fa65 | -6.95942 | -38.62096 | 2025-12-12 03:59:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 45a84452-0c24-3abc-a5d0-0222d1924c00 | -6.54208 | -41.74231 | 2025-12-12 03:59:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0aefabe0-8732-369b-9e51-ca75b2599547 | -11.89062 | -43.70719 | 2025-12-12 03:59:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92c9984f-a93c-38ac-8f7f-cbd977002c46 | -6.121 | -41.27934 | 2025-12-12 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 512db7f2-75a2-30f2-bf54-eee342322291 | -10.14282 | -36.40861 | 2025-12-12 03:59:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 940d8284-7ac8-3bed-b78a-7b18710c0a73 | -8.9191 | -37.94685 | 2025-12-12 03:59:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 20dac989-bc9c-3a2e-89d4-6b71ee3c94c5 | -8.159 | -43.17707 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24b2a964-4956-3fba-846d-c9623ae27689 | -10.23477 | -52.22248 | 2025-12-12 03:59:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ccb622e-a37f-355c-9966-701cc709e23d | -6.46618 | -39.39708 | 2025-12-12 03:59:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 501f28d3-edb9-3ea6-a737-8860ba35c0e7 | -6.11676 | -41.28284 | 2025-12-12 03:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ca6e5dc-89b3-3f7d-83e3-dffdea885752 | -7.503 | -38.82124 | 2025-12-12 03:59:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 72ef60be-fb10-3b97-8f8c-0fbba7711931 | -8.83187 | -36.55007 | 2025-12-12 03:59:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0528c6f3-e29c-3a7f-85ba-c76106ddd960 | -9.40128 | -36.01852 | 2025-12-12 03:59:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eea0ead4-fcf6-34d3-a6eb-a2cbbbbd1d34 | -6.95665 | -38.61696 | 2025-12-12 03:59:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8e6243a4-31ca-38d5-b7f6-d2dfc258c367 | -8.03678 | -43.0944 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| ee591cc7-3067-3c2b-8e5f-899d7d6fc671 | -11.78664 | -40.85963 | 2025-12-12 03:59:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7446edef-445f-3a44-8326-5adde7d2bd54 | -8.17268 | -34.98104 | 2025-12-12 03:59:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fd067430-79c6-3e0c-b320-9fcb9ac45c0e | -8.91575 | -37.94632 | 2025-12-12 03:59:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d56229a-71fe-3313-9562-f611968fc16e | -6.1161 | -41.28694 | 2025-12-12 03:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8c68301-fa54-361e-879b-49dac72c6888 | -10.23674 | -52.22479 | 2025-12-12 03:59:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3484cd3-8d7b-3966-8410-7d006a86f10b | -11.10794 | -40.28086 | 2025-12-12 03:59:00 | NPP-375D | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d5f504e4-4741-35e0-a1e9-41358906c647 | -12.25754 | -38.24659 | 2025-12-12 03:59:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f9f7bb8e-bdc1-3481-a745-6a1398e0e7e2 | -11.88684 | -43.70651 | 2025-12-12 03:59:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1da2214f-4055-327b-b307-fbb2920c7b43 | -8.03211 | -43.09854 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 79ceff01-28d2-3bc9-a5e5-e63bd86837fd | -8.03129 | -43.10335 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 2cebd1e7-34ac-30b5-abe1-35d3797b8e4c | -8.03596 | -43.0992 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| e002c4e0-05e6-3cea-9874-75dac71373c2 | -9.15532 | -37.1891 | 2025-12-12 03:59:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b9aa84d9-072c-3701-9c70-597ee3afdbbd | -6.9395 | -38.6178 | 2025-12-12 03:59:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6ab34826-791e-3dc3-a107-768d6dacb955 | -6.32886 | -41.88247 | 2025-12-12 03:59:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c324eea8-30da-38b9-9f97-4c3fc0b9d56c | -12.28036 | -38.41583 | 2025-12-12 03:59:00 | NPP-375D | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c9e4689f-5821-3dee-970c-2753465f31e6 | -8.03515 | -43.104 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 90d0d6d5-f7b1-3caf-bcd4-8d8513bfe90d | -7.46807 | -39.9464 | 2025-12-12 03:59:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67208ad0-26d5-3237-8832-ff1d251fcece | -9.40474 | -35.65045 | 2025-12-12 03:59:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6faa2dbc-9c60-3fc7-b6a6-edc01f7b4212 | -8.09046 | -35.01299 | 2025-12-12 03:59:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 96840762-90d3-323a-a630-f3a0dba34431 | -7.33223 | -34.98188 | 2025-12-12 03:59:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3f151ef7-55f5-3ce7-9d13-ac45894cb096 | -8.02744 | -43.1027 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 8c5f53f3-0473-3612-bc46-5a49a1512ae2 | -8.02826 | -43.09788 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c0dd6769-0d50-30fa-8317-8ca478a59f42 | -8.039 | -43.10466 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| dab0fe35-6da9-3538-a54c-fc3f04cd45e5 | -6.12325 | -41.28812 | 2025-12-12 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7719a88d-e996-3db1-b7b7-c314395c1bda | -9.93018 | -36.14217 | 2025-12-12 03:59:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ef42801d-2205-3692-b606-2348276c6a90 | -9.92657 | -36.14163 | 2025-12-12 03:59:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 036d2ea2-7c37-377d-a193-8e4eab90d4e3 | -8.93417 | -36.51643 | 2025-12-12 03:59:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b6580110-1abc-370d-bb6f-07f384a35bb7 | -7.47169 | -35.3117 | 2025-12-12 03:59:00 | NPP-375D | CAMUTANGA | PERNAMBUCO | Brasil | 2603603 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3094476c-a178-31ab-8387-92253468a88f | -9.40066 | -36.02268 | 2025-12-12 03:59:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46db3e2f-fe53-3138-acc8-7023dd5d48d9 | -7.16413 | -35.17748 | 2025-12-12 03:59:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a391bfb6-f10c-3baf-8862-d8b53af65790 | -8.79981 | -36.95522 | 2025-12-12 03:59:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a85b7e5-440f-3b84-b237-a60e00bd947e | -6.11742 | -41.27874 | 2025-12-12 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 49e83589-5992-3387-b577-77c1f91766d4 | -8.82454 | -39.82969 | 2025-12-12 03:59:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7d191bc9-4e9c-34b1-b7f0-b9f8be4fea7f | -8.08671 | -35.01242 | 2025-12-12 03:59:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ad618c02-9e75-3a2b-bc39-3e9a6de0bede | -9.39767 | -36.01798 | 2025-12-12 03:59:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5e46d559-0ac0-316d-a8e4-848a579cd7b7 | -14.9134 | -58.1263 | 2025-12-12 04:00:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4327b08e-b873-3603-8e45-fa7f1ae99a72 | -8.0324 | -43.1022 | 2025-12-12 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 2f35cd31-6f12-300b-aeb5-b304fd725da4 | -2.4183 | -51.9278 | 2025-12-12 04:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 05135fd2-3efa-3ce0-9567-20d679a29c9a | -14.8941 | -58.1282 | 2025-12-12 04:00:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f504e4cf-5ac1-31d9-a015-5d9d9ac9f475 | -2.3565 | -54.3831 | 2025-12-12 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| efc8aa69-22a6-3cf3-a937-d714fa88b1d6 | -8.0513 | -43.1001 | 2025-12-12 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| dad0db30-b3eb-334a-b89d-b48de0d9e30e | -2.4367 | -51.9274 | 2025-12-12 04:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 79002662-f3e7-3657-b3d4-caffb460d5bf | -18.9751 | -40.98057 | 2025-12-12 04:01:00 | NPP-375D | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f76d5fc-0157-3e8a-9ee7-aaab9f93b59c | -18.69149 | -42.96678 | 2025-12-12 04:01:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a1284c12-b14b-392d-9a04-51896bb26962 | -12.22234 | -43.4442 | 2025-12-12 04:01:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f321ac61-1276-3eb4-b695-fec1501f9513 | -14.99865 | -38.99965 | 2025-12-12 04:01:00 | NPP-375D | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b407066f-4436-3d1c-83ef-050f41551a54 | -19.58516 | -43.96611 | 2025-12-12 04:01:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9e64dd4-e2c0-3936-8e62-a432d7b137f3 | -18.45201 | -44.49084 | 2025-12-12 04:01:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65fc5a2c-9339-3d9a-838e-470ce48e29b0 | -11.32262 | -49.19753 | 2025-12-12 04:01:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cbd5c4d-6a0f-3e50-b67c-41a0c4442763 | -12.86035 | -39.5626 | 2025-12-12 04:01:00 | NPP-375D | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 551be7f5-353f-3d7d-a7f8-f666c7a191c9 | -11.31721 | -49.19627 | 2025-12-12 04:01:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a410b4d9-a009-32cf-a91a-eef40af5839f | -12.20284 | -49.54764 | 2025-12-12 04:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83462ce8-f681-390d-8e7e-acbd1b228ed5 | -17.10188 | -39.19514 | 2025-12-12 04:01:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a9676ac0-42b7-38f7-a48d-388a0b5cdf70 | -19.46713 | -44.76527 | 2025-12-12 04:01:00 | NPP-375D | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51aa89e5-42b3-3598-8d8a-30b39fb227bf | -12.2083 | -49.54881 | 2025-12-12 04:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ab776fa-8e47-3095-8f74-ad77b046c779 | -17.10131 | -39.19896 | 2025-12-12 04:01:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 155899b7-ed5a-3150-98ae-4325863774b5 | -12.20355 | -49.54397 | 2025-12-12 04:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c779908-97a5-3348-b29f-8ee8e742f2cc | -19.5361 | -41.97139 | 2025-12-12 04:01:00 | NPP-375D | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e093b128-47a3-32bb-95e2-7193e2c762b9 | -15.31797 | -42.05246 | 2025-12-12 04:01:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 20defb02-d1af-384f-b535-d404ab0f3709 | -22.12353 | -43.25836 | 2025-12-12 04:04:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9729a556-d345-3211-bec1-db8e45d311f0 | -19.86742 | -46.56371 | 2025-12-12 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e687fe7f-cef1-3df9-be8a-bbcc19c625bc | -20.47867 | -42.25862 | 2025-12-12 04:04:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5753badd-e3a9-3eb3-9e5e-790eed30b98f | -22.72951 | -43.46512 | 2025-12-12 04:04:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b7e1670a-d5cf-3b18-8265-d8d4c8efc535 | -22.89561 | -43.58326 | 2025-12-12 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b0fe5a72-9a5d-3439-9c2e-c4b5f1e0d390 | -20.95797 | -48.7707 | 2025-12-12 04:04:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9fc16407-46df-3057-95a7-e591cfb367b5 | -23.40737 | -46.41998 | 2025-12-12 04:04:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e91af18a-2a47-3fbf-a029-eb4bf76796ec | -19.86839 | -46.55855 | 2025-12-12 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2efe3235-ccb8-3689-8277-a074c634f671 | -20.38497 | -41.3335 | 2025-12-12 04:04:00 | NPP-375D | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3d79bce4-6b65-3b63-8ed6-983c920e2a4c | -20.39104 | -41.3384 | 2025-12-12 04:04:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 323ce937-b036-3945-a10c-64422a81a217 | -23.49929 | -45.93781 | 2025-12-12 04:04:00 | NPP-375D | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4f88d87d-a972-3ddb-8337-b9b066c08255 | -21.33656 | -44.95037 | 2025-12-12 04:04:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7251815c-9204-3e82-a3dc-4a807658ad4c | -22.95429 | -48.70664 | 2025-12-12 04:04:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1152940c-3fd9-3d85-8627-8b0aea3de9d5 | -20.43273 | -40.84668 | 2025-12-12 04:04:00 | NPP-375D | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d1c70f59-c9e5-3da7-8a5c-37ebc0293f0f | -23.30485 | -45.64514 | 2025-12-12 04:04:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3b30aeb1-f235-3eb5-8cd2-5dc11939be4e | -23.30408 | -45.64941 | 2025-12-12 04:04:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |


[Clique aqui para ver as próximas entradas](README14.md)
