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
| 12e5561e-71f6-39cf-b5fc-f65593dd9e11 | -16.67789 | -41.35612 | 2025-10-29 03:55:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b80a7c08-2e1e-3212-a686-aac955d175ac | -15.15592 | -47.23756 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d06aded-7c9b-32f4-bb32-8e50930233c8 | -14.28013 | -47.30903 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7db440f1-4319-33b5-aa53-e0724676bc4d | -10.96054 | -47.61589 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36b6d8cb-c5e7-3620-bec4-7541902b3bd0 | -11.17687 | -43.43302 | 2025-10-29 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2987298d-59cf-3146-80da-e5bd534f3c27 | -12.08339 | -47.99784 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bfc8005-51a6-36dd-be9a-75ab395ccf07 | -15.33825 | -42.01465 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ba8d2f1b-d86c-3e06-9020-873aa79176cd | -13.78909 | -43.2563 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c0ad0ca2-84e7-301b-b3e5-1b38bd26d4b3 | -15.63813 | -42.98599 | 2025-10-29 03:55:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e967bf4f-05c3-3b95-845b-89fa0ef224ff | -13.5771 | -49.60784 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6c7d63b-e0c7-386b-a262-1b268b77ca9b | -13.88393 | -48.4621 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4ca80fa-6773-3e71-b868-f062c6e9b637 | -9.50906 | -46.95647 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86384d59-94ca-3be5-9f5e-41f9cb2cb57d | -12.28849 | -47.00367 | 2025-10-29 03:55:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 240c22cc-bcc9-3f77-978a-b065fb87fd2a | -13.57232 | -49.6123 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10e6a080-f08f-3d32-a6f5-40f928d63bc3 | -15.11142 | -43.26378 | 2025-10-29 03:55:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b841c432-2ac6-3e87-abe9-9f6f5901cd1d | -10.85726 | -47.89894 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0043bce2-d84e-35e6-a392-f9f27f66c9b0 | -13.68333 | -47.18599 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 496d4d40-c7ba-3fb7-8f79-a041eb3b8580 | -13.89653 | -48.50233 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb93cc35-c04a-34fd-a3a7-e89f92e71290 | -12.06412 | -45.71668 | 2025-10-29 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 13e1ca25-91d1-3f0c-993a-e3446155d988 | -9.93818 | -47.86433 | 2025-10-29 03:55:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0de0411e-7e51-39d2-a7f5-707ed0b74157 | -9.4428 | -46.90424 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 20280c0b-2e5f-30cf-aac7-ab4c350faed6 | -10.77439 | -45.11075 | 2025-10-29 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c999cf5-68bb-376b-9961-1739b9c02d12 | -11.37248 | -47.01669 | 2025-10-29 03:55:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c540a8e2-262c-3767-9934-404620122163 | -12.91822 | -45.04176 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4462794-6c1e-393a-b38d-444f47847814 | -13.2518 | -47.01175 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00765347-6c78-3715-a257-d7c83a5e8e60 | -13.53933 | -43.35291 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 141bb083-55d6-34c3-9f40-eed99a214eb3 | -13.26604 | -47.72464 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a3b3ee8b-a21c-3b6a-96f9-9ceaae868aa8 | -11.28802 | -47.55124 | 2025-10-29 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cda5ca65-476e-350c-8710-43774da240db | -12.10764 | -44.59454 | 2025-10-29 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c28725da-62de-3378-8a0d-70f65a56da16 | -13.91342 | -48.46921 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dac914e5-4a16-32c6-bbb2-267d8120537e | -11.25468 | -45.47258 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 68a7465a-5f13-34c7-9043-f07b32925cf2 | -12.68893 | -48.4358 | 2025-10-29 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 543a2fc7-3342-3205-9f9b-35507a5691f8 | -13.67041 | -47.17845 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18f87054-097f-3bd4-86a7-45fbc1b32154 | -13.64257 | -47.02302 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7e29a207-ba5f-3697-81de-eaaaa12a5755 | -13.89605 | -48.50766 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e6a08f0-025a-3ad0-a336-2c79fff68547 | -9.37196 | -43.68359 | 2025-10-29 03:55:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fbd5d319-b00d-3b99-829a-c8708fcd468e | -14.42054 | -47.84648 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdd8dee2-8acd-331b-9ca6-255b08512f7c | -10.61457 | -47.89619 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| daaa49f0-bd1a-34cc-b2a7-c8a94efe4fd4 | -10.74001 | -44.46747 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79d20834-a620-398e-b5ef-e65368349972 | -10.58385 | -40.50945 | 2025-10-29 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae733156-5bb9-336d-9b3c-9504f2f1631e | -9.92613 | -47.67282 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23251e66-b1d3-3466-a7a3-da4ed32a1a88 | -10.51713 | -47.72271 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4350e61-400b-320b-a838-821f6d5aae17 | -14.79172 | -46.17485 | 2025-10-29 03:55:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a054ef8-caa8-3c16-bf78-540282b59638 | -10.86174 | -50.10068 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e8f4e3e4-766e-30cd-8f3d-c7bea2f944d7 | -10.84866 | -47.88847 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a0abc52-b205-3bbe-8a56-ea9f7d6f655c | -10.76315 | -47.89543 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab71f5da-e754-3ed0-a3be-893e034f9b82 | -9.50801 | -46.51793 | 2025-10-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76c53b45-9d55-38f8-bf47-38639408fe3d | -10.38053 | -47.56524 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9f5afe4-d07b-38b6-938e-ab9e1aaa51ca | -11.57134 | -47.94487 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe8b27b7-2b7b-3a74-a497-4fd05dd48071 | -8.76404 | -46.5122 | 2025-10-29 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dfd11417-8725-380b-ad36-b3e56bf6c671 | -10.9049 | -48.37738 | 2025-10-29 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9828c192-0d59-3a4a-887a-25399b16ac4a | -13.54898 | -47.32373 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa288685-3486-335c-a668-eac0e949d58e | -9.22741 | -46.34903 | 2025-10-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f35c0bba-7458-3204-b4a9-b5f0f788844b | -13.8166 | -41.69107 | 2025-10-29 03:55:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18e9845a-bf5f-3d78-a707-d4974f14b81a | -12.2185 | -46.53545 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5d57263-c688-3625-9916-bee0044ec132 | -9.8828 | -44.88389 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30e73562-bda9-32f1-b753-a4262682a651 | -10.62411 | -47.97296 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 528c67b0-80eb-3501-97cb-cb21fd6f1f7b | -13.58579 | -48.52935 | 2025-10-29 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0953380e-5497-37d4-8ec7-c9346558cf5b | -11.27893 | -45.5111 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6c4c7fd5-4c54-3e24-a9e6-419337680ef6 | -10.7717 | -44.08371 | 2025-10-29 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0d640da-536a-3107-8917-0eef8ea03608 | -14.51951 | -48.00092 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 84db2aa3-0561-31f9-901f-7b9ae0968c96 | -13.56816 | -47.33841 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b597c565-050f-357d-910f-16d33191b794 | -13.30072 | -47.62224 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8b376cd3-fef7-396d-958b-2a39fb7ae728 | -9.73396 | -44.06343 | 2025-10-29 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 524f33ca-9f97-3f3f-955f-9b7f665fab38 | -13.23143 | -47.99676 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7e1bf253-ef53-3e6a-9032-3d86f4dc3e31 | -12.14559 | -45.21376 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 935756ec-36c7-322e-8eaf-11040dd8f363 | -13.53418 | -47.35139 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ccc60012-6f28-3c64-b698-f0e367c5be83 | -13.49061 | -44.08115 | 2025-10-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e782455e-93bc-3086-9ea8-bab1a6cab91c | -13.56163 | -47.1522 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10b19484-974b-3962-acd1-26130f7d8971 | -12.00764 | -46.78267 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 09466bd3-c3ba-30d6-887c-07acc7dec1d4 | -11.99839 | -46.78093 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 81d8d41a-06e5-3e1b-b1cf-8cb248acdb1e | -12.90528 | -46.35533 | 2025-10-29 03:55:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1c29fa9-3a1a-3203-8d03-b71afab4246a | -14.31773 | -46.52364 | 2025-10-29 03:55:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df5dc922-8329-313e-9f96-0322b62c6811 | -13.62443 | -46.46688 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f8a2af04-b367-3890-a483-639e72bc86b1 | -10.77021 | -44.08556 | 2025-10-29 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43dde23a-7327-3422-83a5-e1dd67d0d916 | -13.32465 | -47.43976 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc954a98-a964-3e36-9834-19e1e62c0221 | -12.07837 | -47.99696 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f0f31e4-6f5c-33fc-af83-82352260b3fd | -10.85598 | -50.13076 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4295774c-86cd-38ab-acd7-752894bcaaed | -13.87014 | -48.48 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2027af3-adbb-3bda-bfe9-cc1463e84d1b | -9.50536 | -46.9631 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7eef6197-1d9e-3fcc-9a5c-237b74401c88 | -13.52761 | -47.33474 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d172a25d-bb61-35d8-b3e0-4f787e1ee124 | -13.32692 | -47.48048 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8f2f4b34-9487-3fbd-81c7-f67cfe9cac65 | -12.53082 | -47.53877 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e031fda2-b160-3a43-921c-7b47dacc2556 | -13.27589 | -47.72537 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2b3f69e-f04d-34ab-a968-23d9d74a1b37 | -13.64622 | -43.69644 | 2025-10-29 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc83cf36-59d0-39ec-96e3-6b6cb6a6f3a2 | -13.64409 | -46.50803 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 42e843da-abff-3b7c-9806-f8d24c642c32 | -12.3638 | -44.06758 | 2025-10-29 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08666be9-ed59-3b54-8391-003bda3373ad | -15.07922 | -43.13408 | 2025-10-29 03:55:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8562bf87-c1fa-3feb-b848-a3d02ce30daa | -13.47551 | -47.45684 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b707190d-d232-35ef-8298-705542ddab68 | -10.85545 | -47.89813 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5fb0ab9-502c-36d6-80d3-3f494df5919a | -10.88062 | -45.07563 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62b9c9a1-f31c-32d3-8daa-791c0303251c | -12.05966 | -46.62646 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4324d829-5443-3519-8a15-eb51d8334a91 | -12.41113 | -44.70528 | 2025-10-29 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4afe43bc-c97b-3c53-84ed-6df989077d2c | -11.64607 | -48.53055 | 2025-10-29 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b5d9434-ca5c-39ed-bba8-33691f958db9 | -10.36824 | -44.26865 | 2025-10-29 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55a840eb-028c-3035-9f7c-b5330e2ddfcf | -10.6229 | -47.87953 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc939a55-4153-3404-9463-a1bd985fe544 | -9.57593 | -46.93582 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24bb3137-e36d-3dea-861b-4c384bbc0d7a | -13.54997 | -47.13796 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f65730e-6e1d-3d7e-84ed-abd728d3cd5f | -13.32845 | -47.47794 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25a5a14f-52f9-399e-871e-1a5a61a9a224 | -13.47629 | -47.45269 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README21.md)
