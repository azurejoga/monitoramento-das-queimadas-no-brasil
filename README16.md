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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7d273df-a4bf-34d0-a2dc-bd3019a59be3 | -6.67018 | -44.36927 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59e52de1-f118-3c62-bb0c-1c5e5d416b42 | -6.32642 | -45.65639 | 2025-08-04 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed6e7c43-9bb8-310c-bc72-b2391bdb482e | -8.04471 | -43.10801 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0fbc11d7-93cb-3205-87ee-0a97d1bba754 | -8.04014 | -43.11098 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 97669c70-30fa-3fde-b99b-aadb976ed03c | -8.00714 | -43.19594 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b5478c1-092d-34dc-a71e-218857c8e039 | -8.01474 | -43.17199 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d49b6bac-753e-3f04-b991-a95e27ad3196 | -6.14627 | -43.7816 | 2025-08-04 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 649b19cf-9114-3c9d-b13a-6254a7025e6f | -4.74803 | -44.43938 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5fbb8e3-8725-3a49-8c15-db13b6df8d26 | -6.2647 | -44.06985 | 2025-08-04 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53ccd3c7-a83a-3d45-8b1d-e584fa3fa600 | -8.55279 | -47.46272 | 2025-08-04 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08e8729e-3fa0-3603-9ff6-25e22c302245 | -6.65225 | -59.11112 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f73ceac5-ab2d-3a46-9735-f6bf9a4d47ca | -6.95442 | -44.50871 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dba54b30-38c1-385f-af86-aea945092a1f | -6.32296 | -45.65585 | 2025-08-04 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7040c3d3-3057-3f31-9d84-0bd9b7d83d0f | -8.73847 | -46.39496 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e2b4916-28e2-3674-838b-fed3c5f2eeea | -8.73274 | -46.40941 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4990c36-e5c4-3125-840b-5eba2e1edafc | -7.95128 | -43.90968 | 2025-08-04 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b143ce05-4781-3fae-9f3d-2aac8bb686b4 | -6.61415 | -59.96188 | 2025-08-04 04:34:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91e7e7bc-f49b-321b-8a73-1d65edfa9477 | -7.77459 | -45.22184 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b16f319-93bc-3ba8-851b-8365f2c6aeaa | -6.62603 | -59.96965 | 2025-08-04 04:34:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 49c7ea18-8c85-3e77-ae76-12720b66c885 | -3.66377 | -41.1276 | 2025-08-04 04:34:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5055dd5-9917-3219-ba33-df87101d5d09 | -4.74213 | -44.4301 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f150320-e7a2-3bf0-8955-30798bcd4bb4 | -5.28047 | -44.88364 | 2025-08-04 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3e2de08-28e9-36fd-b086-3e5fb5a7504e | -7.77756 | -45.22641 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b9392a8-474e-385a-a896-772723ec8b71 | -8.26154 | -47.33751 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c50930c2-853c-3fec-ae4a-0c855ac177f0 | -6.17522 | -44.78169 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad4c7b71-f921-32af-b521-1563b93badf8 | -4.42304 | -47.2813 | 2025-08-04 04:34:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae31875e-6a56-3374-964c-8f1c42dbee1b | -3.68915 | -41.13546 | 2025-08-04 04:34:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5ad9cac0-fd9f-3965-aab8-e84117859078 | -8.00269 | -43.14153 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| d166f613-a966-3cd7-bea0-2163070740f0 | -7.03312 | -59.85741 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf21e119-8e99-3160-a405-6c18683727e1 | -6.5636 | -43.38139 | 2025-08-04 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7127e9f6-8e7c-3d98-b4e3-17b564b5cb38 | -7.77817 | -45.22235 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b324c09c-5b99-3fc0-b67b-af830b4a37d1 | -8.01321 | -43.18252 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c8c315db-c1e7-3770-95a6-698f3a5ae6a3 | -6.06487 | -44.67805 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b54b0996-4804-3596-a3ee-69f96397f3a9 | -9.39237 | -45.50293 | 2025-08-04 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5d7d69a-3b97-33c2-b9d7-d5c1f741e533 | -8.05333 | -43.10565 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f2c24157-aae7-30cd-8c72-f9dc2e2ec51b | -7.64766 | -49.84024 | 2025-08-04 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 245214b9-2700-35de-a37d-7d2b9f027aa5 | -4.13555 | -46.46194 | 2025-08-04 04:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 615417ac-962a-377c-a8ae-f0809c809a25 | -4.12752 | -47.65631 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb971534-9133-39f5-9647-ca33fd86e096 | -6.69049 | -44.35955 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91e51426-73f9-3939-8a5d-2564e1b850ce | -7.02549 | -59.83454 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de8a3969-53fe-35c7-ab11-505b9d8fec33 | -7.64459 | -45.30309 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 50f14bf4-7356-375a-a81d-5af6f953850b | -8.73389 | -46.40193 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5de390fe-93fb-37c5-a9ea-e81e018bdf84 | -6.83763 | -44.85766 | 2025-08-04 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddc64bbe-afb4-348d-a024-ebad7015f37b | -6.14313 | -57.91967 | 2025-08-04 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e4ae3f6-9fb7-363c-8167-8b98369c66a7 | -6.63379 | -43.6643 | 2025-08-04 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f083e68-5b57-3b0c-ad8c-0c7ac81dd148 | -6.62858 | -43.67302 | 2025-08-04 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 302af83d-31e7-3ac6-bd13-18d0ea0dcf0e | -6.19573 | -43.7612 | 2025-08-04 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a731d39-177e-35b5-9013-f191a2105120 | -7.99563 | -43.16193 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| deb235ea-c070-35dc-a35f-6e83e4d5b23f | -4.73854 | -44.42956 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 828613c0-ce9d-3c93-b310-057c92722267 | -7.01066 | -59.83641 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08e908b4-0356-303b-ac6f-e0736b7430b2 | -7.5524 | -44.88834 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fc0c953-ae3d-3572-94ba-435e2ec5d65f | -7.99659 | -43.2121 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9d3cb61c-d231-3470-8e10-47934ccf4727 | -8.73446 | -46.39818 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df1f1778-1a38-382c-a55e-e56d0a13743b | -8.00723 | -43.13859 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| e3f9e609-cde8-38d3-a8ac-bcc554f3b867 | -8.73845 | -46.41795 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f4ec5f4-28e0-36ae-8b3e-e03be54662ac | -8.2705 | -47.36785 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c17b749b-9991-3283-9aeb-dca0ebd7160f | -5.28461 | -44.88026 | 2025-08-04 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 52b47570-f0eb-343d-bd11-e5f98da7f205 | -8.35718 | -46.944 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fc675ff-81d6-3705-a3f9-edef5f70d079 | -6.52329 | -44.52884 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1299e282-6e3d-3149-b8b9-e490d9ea81b8 | -8.02088 | -43.12983 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c01dde6b-043b-38ef-a016-747c5a904bce | -7.01256 | -59.82602 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5193a5da-0e45-3577-99a2-a3d3a86a3b5f | -9.40015 | -45.49986 | 2025-08-04 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f505dcb0-e2c6-3ac6-a6ea-cf3ffec951df | -7.5549 | -44.87176 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cae7b33-7b72-3f2f-b98a-38f370609dc3 | -8.31337 | -47.52227 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 113397d6-568b-3526-afd0-fd5664270895 | -4.74579 | -44.44183 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2781da5c-46d4-36d6-984e-95b1a3b43fc4 | -7.01891 | -59.8272 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9b7cb15-ebf1-38b0-b4de-2e679ff58133 | -7.64463 | -45.29789 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d77319c7-e6d3-3456-95b4-91714eba5c83 | -7.96292 | -45.10259 | 2025-08-04 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cedd1b5-6888-372d-a7d8-beec150a83a4 | -9.39954 | -45.50397 | 2025-08-04 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5683f1b7-a9e3-31c4-95cc-29bd5c44208e | -6.64953 | -45.89254 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc6c4d66-b5b6-3c9f-88e7-146cedd8621f | -4.74086 | -44.43827 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 406ce86b-87c3-3ec4-9cfa-8971838ff1f3 | -6.52265 | -44.5331 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90eaba44-2a1e-3a84-9f74-1906fd6c02a1 | -7.76808 | -45.10881 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d85c4932-bdfc-3dbb-ab63-7ebd944e42f3 | -8.74017 | -46.40677 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f11c069a-4d08-365c-bf86-b4b2f7f39a69 | -6.62162 | -59.95748 | 2025-08-04 04:34:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c6f03b-4a74-330c-b9fe-7a6fe45c3f3f | -8.38621 | -46.94085 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f2e8f289-a549-3f30-8ef2-18a5947b0c01 | -8.03102 | -43.11686 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 651491ed-b864-3b5e-83d2-76c0553c2b79 | -3.88408 | -54.21525 | 2025-08-04 04:34:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af404da3-2310-3204-897e-58213f81b381 | -8.74247 | -46.39178 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e6194bc-b48d-34cc-96a1-b6d2a78ac824 | -7.3053 | -44.67447 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ef4cc7e-a9c1-34b7-a163-1ed5ab8ff9df | -7.53555 | -44.87727 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1ec0db1-b729-3546-ae44-ab80921b00bc | -9.39656 | -45.49936 | 2025-08-04 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54f1952d-8c53-36ce-9cf9-4a741b109520 | -8.00166 | -43.14862 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 4a9558e6-dd37-3e8c-88d3-1b647174965b | -7.99412 | -43.17236 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f774c433-098b-3180-95a6-9c96687dda27 | -6.65194 | -59.11363 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bbb2e5f-9ee4-3d16-8520-0af1220f1d33 | -7.37199 | -44.18783 | 2025-08-04 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50711a15-e85b-33c2-91a5-3139e2bb89ba | -8.01075 | -43.14277 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d7aa959-deaa-3717-971f-2a40fa83edae | -7.76806 | -45.21664 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b64bf4c1-7dfb-3ecb-94de-22841fa09e2b | -8.37438 | -46.54119 | 2025-08-04 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 020ddff2-3954-3a66-9986-6327012fd99e | -8.35716 | -46.92192 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f00b4fb-10da-328b-bb73-e2213ae939eb | -6.95935 | -44.50088 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa1240a7-6a32-3002-95af-1f4013efab5b | -7.56198 | -44.89843 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b3be23f-7090-3953-9b8c-94aaafdc96d7 | -8.05737 | -43.10625 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f5efea84-bfea-3c95-8fbf-fe947ac1d35e | -7.54341 | -44.87423 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fa37dd8-50b9-3594-9218-960d947f0c4d | -8.01979 | -43.16559 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b93f36a7-56fa-30eb-ab47-31653c842e60 | -7.01161 | -59.83122 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b913a9f2-3143-3309-a5cf-f753a7655ed8 | -7.53917 | -44.87784 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6838a350-9c4a-3949-8233-f94d88eed946 | -6.60886 | -44.03796 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74a23ff7-5e9e-3239-a481-087d9f282185 | -8.51434 | -44.74842 | 2025-08-04 04:34:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7ac9b3f-0793-339f-b656-1a507df87620 | -8.01684 | -43.12921 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README17.md)
