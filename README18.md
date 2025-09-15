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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abd512d9-6039-313b-a79e-f861f86f8f79 | -7.31079 | -43.95014 | 2025-09-15 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48e5e9c9-aae2-3abd-8449-bed117d4cb38 | -5.08408 | -41.16222 | 2025-09-15 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f610a845-4739-3c61-bcb9-5b7b6848b99d | -7.86058 | -43.58407 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfdd6910-c996-3eb6-bd4d-bce584c202a5 | -6.34337 | -43.16428 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7814eeae-74da-3f8c-b3dc-3f758b9f84d2 | -5.85843 | -43.73241 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccda0d0d-ca46-3c94-aa88-e819fcc2c4d6 | -7.14272 | -46.09099 | 2025-09-15 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d00a4658-3f7d-39ac-9428-649d190df506 | -6.7717 | -44.72885 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18c68a93-c072-38f6-b2ce-fe590271be43 | -3.65279 | -54.05731 | 2025-09-15 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 480bcdc9-8f40-342c-a754-fd2d1f8f28d8 | -3.64844 | -54.0569 | 2025-09-15 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ed5389bd-fce5-308f-9d50-d44b81b6c249 | -6.32404 | -43.31323 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 253e8e2a-c914-34d1-af9e-7eed12c67d55 | -6.91734 | -46.16076 | 2025-09-15 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ae2e193-b457-3e62-ac4a-67b2583432bd | -6.55347 | -43.98759 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9543859-a66e-349b-8bb4-56f0f3db42f4 | -9.04919 | -45.71936 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c25eaa62-e306-3941-9121-17712763a365 | -9.23174 | -45.6636 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44d0b19e-eacf-387d-ab20-5ff73bf54729 | -6.10992 | -47.84194 | 2025-09-15 04:19:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 119807b5-a888-3900-be45-33374c83d9b3 | -9.01281 | -47.04001 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65541bf4-d4ea-3e5a-85c2-92a2b5a077bc | -8.98158 | -45.82631 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d2d879ed-b7d5-3707-9aea-7eaeb69551a2 | -5.08067 | -44.09863 | 2025-09-15 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73c4f976-dede-372f-a4d3-2f51c2035c0e | -6.5207 | -43.24644 | 2025-09-15 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f10771a1-fd02-3ac1-a978-48453a150dc6 | -5.63928 | -43.89478 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f35d2d04-c463-35ef-b702-242e3a41d470 | -7.96624 | -45.63826 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b35562a-df66-3dc8-9298-1e31e8d872f5 | -8.98432 | -45.8089 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ee566a6-f953-30e1-8241-063d303df03b | -6.44378 | -43.3314 | 2025-09-15 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c72b9804-309c-3b43-8401-dd34c7b0b8b9 | -8.61669 | -45.74279 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 3b925359-404c-3c41-9d23-fb9923c314c7 | -6.20399 | -55.63017 | 2025-09-15 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00a3cd10-ff5c-369e-b36d-a71bf72c259f | -7.87835 | -43.56849 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 9e8a1d4a-382c-3656-beaf-5bcc1b33c1ca | -3.89848 | -42.51518 | 2025-09-15 04:19:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4494c4a3-c6e7-3fe0-bf6e-6818f5d82f84 | -9.10306 | -44.8095 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd0a8b77-16a9-34b3-be7b-504576f251e8 | -7.21789 | -44.39832 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 481d4201-4abb-3308-a606-94c4e84c8cc3 | -8.91723 | -45.47805 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c30233d6-03af-3017-a03d-c24ddb08e93e | -7.6873 | -45.1396 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a59e692-de93-3c5b-920f-bdbd5c8cee68 | -5.68142 | -43.49221 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c0dcee8-f0a3-3564-ad4a-ede55cf0177e | -5.47793 | -44.68988 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 564f5ceb-f92e-3363-9d19-5296da5ecf54 | -6.16271 | -41.17811 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4b29310e-de59-32fc-94ec-4715afdf46e2 | -8.96664 | -46.22172 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e135efd6-a7e6-3ddf-9c3b-f6b44b70085a | -7.49284 | -44.68694 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a17a732d-8cae-372d-a472-f7ebf42c86eb | -8.78473 | -46.016 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd756570-32ba-3267-85b4-c8e3e80e446c | -6.40959 | -42.61271 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 49e5a689-b378-3526-b2b9-0b0c2020b5ca | -3.89509 | -42.51466 | 2025-09-15 04:19:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b631c41-dc8f-3bd4-b376-c4824a6ad3e5 | -5.81757 | -43.48792 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b834e67-649f-3fe1-aa5a-d7ac047dba7b | -6.978 | -44.54169 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 02a289ae-e606-3e12-9ef5-5304abe6a67f | -8.12216 | -43.66801 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14e33860-044e-3060-83c7-cb9c7ab3240b | -8.99477 | -45.7856 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72c81cf0-3e79-364a-9789-19eae60175c4 | -6.4433 | -44.08434 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39b4fe66-04e2-3239-87d8-c92f55e1f862 | -7.88958 | -43.56278 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 125ff143-d798-3d5c-a961-ce4816702402 | -6.34731 | -43.16118 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7bd3a35-1d25-3dd2-84c2-2432aa4303d5 | -7.89303 | -43.58562 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| d25980f3-1433-3253-b9a5-43870b3082b4 | -2.91907 | -49.56238 | 2025-09-15 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dcf6cdc-40c8-3965-8c55-e18854f2433c | -8.98485 | -45.7626 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55755474-c49a-34e2-8e0f-a3805837f1e3 | -8.42461 | -47.22229 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5748a9c0-cb4e-3055-a53b-a7796b829bf1 | -5.85897 | -43.7289 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60ccd6d7-d012-3095-8def-98954034982d | -5.86006 | -43.7219 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60584d04-6ceb-3bf2-8081-ed355b36a70b | -6.98077 | -44.54565 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 524e399c-90a6-314e-b495-6aadff7c4e68 | -3.55475 | -49.04633 | 2025-09-15 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77bc3c55-f6d6-306a-8d3f-85da7b579665 | -6.17489 | -41.19769 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f13be778-2a63-3341-87bb-6a93ac771377 | -6.41707 | -42.60993 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f5da0021-cce4-31aa-b289-5dce7e54a769 | -8.96285 | -45.79476 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d24d736e-988a-3684-8c86-82e8df18d29f | -3.38738 | -50.14927 | 2025-09-15 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3302d78-0db4-3b23-b884-9055616683a1 | -7.87497 | -43.56797 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c3891c4-3b31-3ee5-b420-a0a773fb7f3c | -2.26188 | -47.84467 | 2025-09-15 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7aee40c1-a04c-3b60-9f0a-9d5d9f777b30 | -8.2798 | -45.89568 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51c16eae-8407-3793-9039-d354ff40dbe2 | -8.94303 | -45.79161 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5273189e-81db-32f9-9935-70f7f9bb0231 | -9.00645 | -47.05795 | 2025-09-15 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 784a4319-a09a-3bc8-9c8f-6f69de6b6603 | -7.22246 | -43.83871 | 2025-09-15 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a06e84be-eda5-3d66-810e-9658964b3121 | -6.98871 | -44.77692 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4224721b-787d-3301-b328-89ed5b5ca1a2 | -8.63062 | -46.36644 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bc0daaf-dd4e-3b8d-aaf8-feb1eab58dad | -7.51123 | -44.36961 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0384925-9044-3a6d-a8a3-a163e17b77cb | -3.35028 | -39.27908 | 2025-09-15 04:19:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| efe31d75-2029-350f-bd10-9a20f429673f | -9.07569 | -44.83039 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95841d11-9cb9-32c8-a2e9-4532a1ec46be | -8.97439 | -45.76451 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24c89503-29ae-32a6-ad0d-ab4d92b25eac | -6.43492 | -42.60857 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 12b5e453-fe45-3700-99e5-255e322372d8 | -8.98322 | -45.81586 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fe9fa3a-fa8f-38df-aedd-1e0a2fac548a | -6.87945 | -45.62443 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33ae143f-15cd-3b6b-9bc2-b45deed6c386 | -8.07331 | -44.51865 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e393458-8327-38db-9ca1-c55644fb0496 | -5.37703 | -43.56757 | 2025-09-15 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffd22a7a-3cdd-323b-951a-3426ec9a3849 | -6.41304 | -42.61322 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 506cb490-a7f6-3d25-9e6a-fa9f5c847bd4 | -6.99514 | -44.56202 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 614e4bb9-cd29-3319-975a-c16e4a7af619 | -8.75989 | -46.08725 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac32c38b-a180-3194-9c8f-59b00e958be5 | -6.43944 | -44.08735 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 808842a6-d429-37c4-ac2b-7a34e2fe3102 | -3.47582 | -39.53896 | 2025-09-15 04:19:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 22197b62-c5f3-3f11-95cf-b40790db2475 | -8.9512 | -46.16879 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08667145-cacc-3e87-8307-a5f5de270e45 | -7.69815 | -44.67646 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 99f44043-f369-3dd9-86a1-06576a4aef3a | -8.95458 | -46.04012 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36ca3098-fab4-364c-842b-929476cc61f1 | -7.69942 | -48.86762 | 2025-09-15 04:19:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e83c5a5-3c52-368a-ba03-47b1d3d632bb | -5.857 | -48.15744 | 2025-09-15 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25743931-f227-3305-bb60-95246eb06c84 | -8.20826 | -45.54863 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 38f9d3b3-8409-3182-b444-638de571960c | -8.98267 | -45.81935 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91685ed1-6353-32c9-943e-7bc70115d6dc | -8.07662 | -44.51919 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69a6be19-0ffd-32c2-8798-f99a8a1b52e8 | -8.62871 | -45.73405 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6c9be27-07d4-357f-abd6-e90a552c12b6 | -7.35951 | -44.29547 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7b3ca8c5-0fa7-37af-b8db-24c15bcabf89 | -3.64904 | -54.05329 | 2025-09-15 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b0a0964-4abd-3eb8-b2b7-03e92fcbc613 | -5.6381 | -45.94312 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a467de7c-6b02-3e71-ae34-54e80f60dd79 | -7.59663 | -37.08989 | 2025-09-15 04:19:00 | NOAA-21 | OURO VELHO | PARAÍBA | Brasil | 2510600 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| abcb0772-68b9-32e3-8f46-8db70c81d3c9 | -7.69485 | -44.67593 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b1b77d0f-f8b5-3d59-bb19-3bbcaa341e9e | -2.29565 | -48.57283 | 2025-09-15 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fa0c9d1-fca6-390e-807f-9241547ade5c | -5.87058 | -43.71996 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e81c9548-1918-3268-b1b0-14433c0b7e87 | -5.98136 | -43.77291 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50ff400a-7bf4-3829-a8a8-4dbb2504fcf7 | -7.69275 | -48.86193 | 2025-09-15 04:19:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bb01865-fb00-3855-896d-00878b59a23c | -5.87391 | -43.72046 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba596c66-6ec5-3c05-8a6d-fad386fc44c0 | -8.41717 | -47.22493 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README19.md)
