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
| 3c6aae58-e5bf-365d-936b-f5f9c4ee686a | -11.20828 | -44.87163 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70ac93f1-2ce3-319b-a41c-e7aaab816039 | -10.47772 | -47.23996 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b700ad9-50b0-3751-a8e4-da2fd443f5e2 | -9.95791 | -55.33886 | 2026-10-09 04:27:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6d38fb1-316b-3af2-99a7-21bd8c001bdb | -8.97521 | -47.5365 | 2026-10-09 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f92177aa-d6da-3dec-8f0b-97394a91572d | -9.01519 | -44.38071 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9550694-635e-3a5c-aaa6-45ceedba0954 | -8.96543 | -45.17344 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a669b79e-aa41-33e7-98c1-053cae16ff67 | -8.97391 | -45.14044 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7875c9f1-c20a-3209-8e57-b2b8b2fdedab | -8.32638 | -45.01693 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9f69e4b-c431-3175-92ad-520cb5d21599 | -10.45987 | -47.855 | 2026-10-09 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2c71433-129b-303a-b059-0a976193c7be | -12.21803 | -57.10786 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d9dc164c-f934-327b-b6cd-1f20cd69f6be | -11.05543 | -44.0546 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86d38f25-45fb-33c1-b56e-761411ae6996 | -9.8864 | -50.48574 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 148b343a-1ea5-3fa5-91ab-a1444047abf8 | -12.53306 | -48.71096 | 2026-10-09 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a39e921b-d858-3807-9040-41246c9aa6a6 | -6.50866 | -55.31797 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 26b7a24e-e487-3016-90cc-b1a12b9a3748 | -11.96956 | -57.61564 | 2026-10-09 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7c44fe1-1013-3460-ac7c-e7d5b00b4f62 | -14.05211 | -43.83196 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35a4ffe4-1886-3849-8ee5-813964a3b29a | -7.08496 | -52.67751 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed459b11-ab60-3f40-890b-27df11b76cf5 | -8.13742 | -49.43679 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9da06c3c-a009-3ca2-9073-d4ed25dc1961 | -11.78317 | -45.5729 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7930d48-0ac5-3641-9e64-81ea0aef0242 | -8.73695 | -45.13124 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0bd7612a-8f79-3012-85c5-6e4bb7497f34 | -12.10173 | -57.15578 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 475660ee-0372-3a3b-acc2-3c6ff775165d | -12.23187 | -57.09309 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 073bbf9d-ac67-3161-9e51-fdb26f07d137 | -6.76368 | -48.17392 | 2026-10-09 04:27:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cb9f257-c86f-3831-9563-ebf944421041 | -8.98294 | -45.90757 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32bd0537-54e7-3222-bfb3-09b37507c076 | -7.5834 | -45.65504 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abdaaf03-3122-3549-aa21-b192d2e4531c | -9.30299 | -47.41817 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 298ce0a2-fd23-3147-8620-504ba444f485 | -11.18174 | -45.30433 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93eac6c7-124a-3f7c-8691-a0015f968d66 | -6.48831 | -55.30506 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d898c220-874b-3fe7-b0a6-536423436772 | -9.93739 | -43.56304 | 2026-10-09 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fae2d853-1f40-376f-90fc-a0cba93ad038 | -10.8839 | -49.14778 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b87d6635-0b12-373b-a53a-280ba0f9d3fc | -7.40171 | -44.75346 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4c6e361-de29-38aa-8df6-c03197b130b1 | -6.49018 | -55.30172 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 863c1b11-e3db-37af-b32a-6b88f4a10744 | -9.02465 | -44.36575 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3a07430-94b9-3db7-ae23-e4ad617adaf2 | -11.60771 | -43.67569 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7163a42a-be1f-318a-9189-29490549a60e | -10.86302 | -45.54063 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e1d147bb-560e-3f5a-94b1-54b2248c5c60 | -7.56243 | -46.68926 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe7f9999-96db-3a59-aab7-7bbb0f3ea9ab | -12.21476 | -57.1246 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7a09158d-cd95-38de-aed2-3e9a38b5f131 | -11.77827 | -45.56121 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 259983a7-4162-3b70-8dd4-0f9a4eb26fee | -7.02858 | -55.68098 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09c34761-0453-379b-84c7-23e26dddf10b | -8.96823 | -45.15492 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d832234-d1d5-3d85-a45f-99526b5176b5 | -12.22333 | -57.10879 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 18354401-920d-3fbc-baed-e33eddfe6d4c | -7.41481 | -44.75925 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b37631a3-3cee-33bc-ba9b-1d8aa92476fd | -6.50403 | -55.31392 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e8264c9-a119-3f16-83f1-ee60fc41056b | -8.73471 | -45.1461 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cfb4aff3-4e4e-3c65-8b1e-f0d1f3b4b49b | -10.86358 | -45.53692 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f9056185-7216-37b4-ab88-2681fa016c98 | -6.11731 | -55.69749 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b83aa0d-ba9f-3748-9b6f-b46c63900474 | -11.32301 | -46.65451 | 2026-10-09 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| beef0679-02b7-3ef9-99ef-0f2e288fc4c1 | -8.73924 | -45.13918 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 61ac975d-9a72-331e-9abe-94b576a94a50 | -9.30245 | -47.42165 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a7d48aba-9acc-3a27-b790-1cc6a41d7c5c | -9.09149 | -45.10425 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 841e9bc6-6998-393c-8377-734c712c335b | -11.05846 | -44.05949 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdbf4449-e872-3f12-b5a9-fc9294b17e81 | -8.2432 | -54.72969 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d7833d1-0692-3348-9346-6f77011daa9d | -11.0663 | -44.08286 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3c7b6a6a-9488-3410-89e4-cb96defd6d9d | -9.03921 | -46.86403 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad29c638-7d03-3311-8120-448fa7d08392 | -14.78503 | -42.89884 | 2026-10-09 04:27:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3c327c05-126a-3733-a7e9-8c545634fb5e | -9.02139 | -44.36808 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04405f3c-266e-3257-883c-ae05368d8f41 | -11.06577 | -44.06059 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d223811-ccb5-31cf-836e-7ca4a6b90e00 | -7.50567 | -45.76245 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1069a8ca-7c35-3e41-901a-0e6ad698b771 | -11.86675 | -43.56753 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 040ac5ed-581f-3b8a-8bd8-ace3aa391635 | -12.02605 | -43.45243 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed6d172d-b1b5-3fbf-b848-4a933f817b4f | -7.06748 | -47.39496 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b517ca8a-4b74-3568-aab3-69a997207e5b | -11.84706 | -43.59795 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3043169f-3665-38c8-950d-6f1a087113f3 | -8.73304 | -45.1572 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84f504df-1980-3e37-bb11-7544560b479e | -9.87423 | -50.49223 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5f46390-c9bd-380c-809e-0c1dfba684db | -13.20063 | -54.3713 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0a6ec709-ea07-3c5b-a7c0-3cce66aed3e1 | -12.22772 | -57.09152 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| b55fd258-321b-3e0f-a2b9-512ad6f64237 | -8.93128 | -45.14553 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| baede0bc-43e5-39c3-b9b0-1172436ec3a5 | -11.78467 | -46.56913 | 2026-10-09 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb260419-c8d4-3f1c-a26a-1a81709e26ac | -11.11576 | -47.79653 | 2026-10-09 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f94005d3-cb15-37e7-889f-d7b886c4262a | -10.87855 | -44.80083 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e39f45fb-dc95-3c16-add7-94a4a133d39e | -10.57954 | -46.29384 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85fa02b7-12cb-30e7-9512-d498090befd6 | -6.12145 | -55.70526 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 015bb62b-df36-3636-8075-bc4812d766e6 | -8.96993 | -45.1437 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8504533-a23a-35c6-bce8-17d0865bd1d3 | -8.72963 | -45.15669 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1622cca-858d-336e-af61-7fd9ae64cc01 | -12.22341 | -57.13653 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6ec3070-a3fc-36a7-94d4-1b34f3d11966 | -13.14456 | -46.33877 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f649a8ee-feaa-3471-bd9e-1c825a97eb9a | -8.90329 | -44.93411 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 07ed9a50-b23f-3e4a-b268-ca80bf2818f7 | -10.95922 | -45.38847 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdc863cb-3fac-30bc-b9b9-1e86bf13d316 | -8.72908 | -45.16039 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dcc3a555-52fe-351e-a53a-01d1d160970b | -6.14772 | -51.94352 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cac234b-9ab3-3ac0-a376-4ef4d990f2ff | -11.38426 | -55.09752 | 2026-10-09 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c0e72c3-8db5-3833-8737-bc7f7f1d1978 | -11.11355 | -47.78901 | 2026-10-09 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 317d1736-e071-36d6-b832-1aace398aae4 | -11.26152 | -46.27504 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88c193f4-08d1-35c2-a56a-e0cd856a47db | -11.97575 | -57.61303 | 2026-10-09 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c831796-ceec-3390-af51-4ba6589eee6a | -12.22647 | -57.09817 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 271.4 |
| f95bb639-858f-3656-9779-2c6fab8bc49b | -7.51268 | -47.33461 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 595dff84-512a-34ac-b773-42a33338611a | -11.99319 | -43.49226 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3e07d95-fd88-396d-b20d-df72d9c6172a | -12.21939 | -57.12896 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e515566-ff63-3e35-942a-f8ca99b8e3b8 | -9.02081 | -44.37206 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d45669c-47c3-371c-bf45-07b07494d1c9 | -7.25147 | -48.06234 | 2026-10-09 04:27:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b09f3cf-7209-3e82-93ab-31002abd29e0 | -5.97345 | -55.34817 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 250f6d0a-6494-3203-ab57-0a6542b37cbe | -12.22788 | -57.08546 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6036e06-f172-3825-aff4-d7724ec6ff71 | -10.29314 | -46.60839 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 765a6bd3-1041-353e-8701-0cfed395be42 | -6.41157 | -55.19545 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 850cdfdf-7287-3e43-b539-1f44d3b921b2 | -5.95082 | -55.35403 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 266889ce-9ef3-352d-a636-166d57eb7eea | -9.30306 | -47.46093 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f639d5ca-6b40-3c18-ae42-a3baed05909b | -11.20077 | -45.3189 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8a54e76-12ce-355f-8a15-d76ddb1c5070 | -11.09452 | -44.04265 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da50ef9a-b5d1-31b3-9307-61d3f137e9a9 | -7.79402 | -44.57319 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5efe4d35-a4b1-356a-bbba-d9f2f286f097 | -12.54168 | -46.52732 | 2026-10-09 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README109.md)
