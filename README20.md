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
| ba8bcfc9-7b80-36d7-b6ae-b64ad519d6ff | -0.90898 | -52.44219 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ca7c1b6-4be0-351e-b5c7-1e5e950ea59c | -2.79243 | -47.41785 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7175dbca-b273-3629-9e6d-ead45cc0d6d7 | -2.79126 | -47.43568 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d375f51-8c56-312e-9411-d42a1ece1565 | -1.10475 | -52.2483 | 2025-11-29 04:42:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5be45b19-7180-3ef9-928e-d9cf65171e4a | -2.93346 | -53.27692 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5b1794a-c859-3dd6-9bf6-64df82c39ed3 | -3.33429 | -42.50135 | 2025-11-29 04:42:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a32268bb-66cc-3cae-a3b6-ed654d570b56 | -2.8411 | -45.17114 | 2025-11-29 04:42:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac7f769d-5001-3ffa-8e1e-7bb0ff03e6b8 | -2.74681 | -47.13589 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c544b7a-4954-3eab-8f00-5d5d7cf8b583 | -2.64873 | -48.02404 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c15a71e1-4753-3825-ad8c-f3d15150fbda | -3.21183 | -46.82113 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77134078-8bdf-34e8-9d64-9b19f4058511 | -2.64075 | -48.54649 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| acac0dc8-e063-3131-9c10-c50f639a36e6 | -6.69589 | -41.46276 | 2025-11-29 04:42:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e9cfa7ef-174d-3a81-bdda-1c78849f60cb | -5.00538 | -38.54121 | 2025-11-29 04:42:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 343dbf69-ce32-32b1-a0f3-0984e765628c | -4.86627 | -50.82708 | 2025-11-29 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bab47dcc-e079-3570-a919-ddaa32a89463 | -2.74592 | -49.33505 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41d22f11-43c5-3dae-804b-6a2016f45af0 | -2.42612 | -50.2898 | 2025-11-29 04:42:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d4f781b-7cf4-3b45-aa86-4dc93a7f5862 | -4.86286 | -50.82655 | 2025-11-29 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6de11f2-18a6-3b31-abac-a45e9c7c299d | -3.16949 | -45.24222 | 2025-11-29 04:42:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 598c91e4-2233-3af6-9ada-575fd57614dd | -4.04476 | -50.69876 | 2025-11-29 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7b76eae-a625-3940-917a-4e8efa4f180e | -2.42953 | -50.29034 | 2025-11-29 04:42:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4690818a-68fe-3621-b0b5-1f7b6495d312 | -5.94097 | -45.39648 | 2025-11-29 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cf4260a-6909-3f58-90de-d55789c233a7 | -2.35703 | -48.0743 | 2025-11-29 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d91ca73-02b2-3dca-83a5-3a3769b7c0d4 | -2.95978 | -51.04334 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16263464-1122-3b88-8495-52a9a2677c98 | -2.78738 | -47.42797 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2152acc5-cd2e-3f70-93f7-fff37d6f2f56 | -2.91421 | -53.07216 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc3ef564-5b21-30f4-86b5-8c30882590a5 | -2.78457 | -47.42391 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d789cd93-fe79-384e-b2a7-fad7dfd4da9e | -2.74904 | -49.8643 | 2025-11-29 04:42:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8db481d3-8534-3c7e-8e76-b83a18baa61f | -3.10406 | -45.78628 | 2025-11-29 04:42:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e01695d-d991-3291-a685-88067e8ee6be | -2.85678 | -50.28209 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8150114b-5c22-335a-a24a-2738761d62e3 | -3.32211 | -53.32267 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8155d3b6-57c3-33c9-b46b-613ab4f5007b | -3.3336 | -42.50372 | 2025-11-29 04:42:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d6fef81-46aa-348b-be22-b0cedad0cb37 | -3.22262 | -50.79582 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55b416c4-97f3-37ad-bd34-96d12612e23f | -3.2084 | -46.82059 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3c010df-710a-387d-8eb2-a94656445d42 | -2.71232 | -53.18195 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30b5249d-7962-3de7-9df9-56ac1adb6b37 | -0.97148 | -47.56358 | 2025-11-29 04:42:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db91aaca-7d70-3a45-8f1f-71f8a04426d8 | -4.01086 | -49.10847 | 2025-11-29 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d778a735-3edb-31a7-8330-1eff23319901 | -2.63689 | -48.54942 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e93c71ec-7706-3164-ae65-d4f9720238fc | -4.73709 | -45.68259 | 2025-11-29 04:42:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec29c3ca-2944-3700-abf5-320d5f09187d | -3.25148 | -50.69641 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b8abefb-e449-34e7-bbb2-6bc40d55cc5e | -2.24571 | -46.52375 | 2025-11-29 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 850b3e26-b1b0-3fb9-8899-e5c608b4e0f5 | -1.49893 | -47.80587 | 2025-11-29 04:42:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 654d7de0-3520-3da1-8bb7-de4cd9ee5413 | -2.77963 | -53.26112 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95185865-7472-3d15-a5b3-623afde3d7bb | -3.6602 | -50.22259 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53269f1b-97be-3eb5-8d3a-bbee7957d757 | -2.67782 | -48.80639 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58e7c16c-d2a9-35fb-8159-6707afa0f6bd | -4.36005 | -43.1591 | 2025-11-29 04:42:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a80e81b0-0087-3803-b241-809c01a90f91 | -1.40165 | -54.46968 | 2025-11-29 04:42:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83df5208-a864-32db-8f03-57aa1ab0a4f8 | -2.22063 | -45.28151 | 2025-11-29 04:42:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc875f36-c2f1-322d-870d-6214a04b4401 | -2.84034 | -49.52847 | 2025-11-29 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41b33d40-a9b6-31d9-ac3e-29de7af97b09 | -2.3537 | -48.07377 | 2025-11-29 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6681904-4a9b-35bf-8d73-d7108c05ec57 | -2.9374 | -53.27755 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f45767d-201c-38f5-b4c5-dae93d3f6fe0 | -2.85736 | -50.27845 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed08218f-0727-38dc-aaba-c7134ba3a973 | -2.79237 | -47.42858 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 284ed498-02e6-38f2-bebe-4e4884a1834a | -2.53622 | -45.3863 | 2025-11-29 04:42:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15965308-88b1-3997-91f1-a1904fc7cd2c | -1.3547 | -53.09814 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 757f5363-7312-3996-94dc-11ada3c134af | -2.78794 | -47.42443 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32ae5529-d411-309d-8d05-60638d22c515 | -5.30202 | -44.72507 | 2025-11-29 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c90f1480-0d9e-3f22-bea7-ea65d458e121 | -2.59889 | -46.87581 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce3cd207-225d-3c86-b377-a5bf61b9d625 | -2.63026 | -48.54838 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b7ee7fb8-84b7-3eae-aa5b-30fb567f120a | -2.7502 | -47.1364 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe320d70-7f2c-3869-8b1b-55b9c46dbf7c | -5.35573 | -43.03024 | 2025-11-29 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3f743c3-4c05-3bb4-bf07-4c96c89ea559 | -5.36579 | -43.0228 | 2025-11-29 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1ad25eba-c556-3938-832d-17653734f093 | -5.00008 | -38.53614 | 2025-11-29 04:42:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7279bc39-cd60-3a09-9717-65092d9a27d5 | -2.96903 | -49.57383 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c820e3-e07b-3b11-931f-112edc479530 | -3.67762 | -52.5318 | 2025-11-29 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27dce571-b4f9-362d-b182-e12ab4afaef1 | -1.48179 | -45.78489 | 2025-11-29 04:42:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1805b8aa-125a-3063-92c2-bb9636a868c6 | -1.48117 | -45.78881 | 2025-11-29 04:42:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| aca70efc-e4f9-39f1-85ad-a187e8bd9056 | -3.86317 | -54.05924 | 2025-11-29 04:42:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61caafb7-c7eb-32bc-8567-c0adacd8df6b | -2.79347 | -47.42148 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81b9a52b-542d-3a91-8e58-b9d25ac8a5d2 | -1.68596 | -53.65976 | 2025-11-29 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2540ced1-1465-35c8-8c91-a10ef09a633e | -1.75794 | -46.56016 | 2025-11-29 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8a71dda-9e4e-3271-8609-d9f1ad5363bd | -6.69606 | -41.4651 | 2025-11-29 04:42:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5747c58c-cd6c-3e40-999e-177c818e2b7d | -3.24946 | -50.693 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a5064f6-379a-3d53-8354-dca2c21b49f7 | -2.96479 | -50.9892 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bccdf07-f4af-3a8e-aa3c-770ca5983424 | -3.22831 | -50.14767 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 245bbc69-7ca8-3aff-bc3f-7158e840423d | -5.00601 | -38.53695 | 2025-11-29 04:42:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 51322536-9e1f-3b6d-83b4-0e26dc1910ab | -3.61136 | -50.36996 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8a20659-16f1-3109-853f-a4dad5e97551 | -2.79181 | -47.43213 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32360106-50a3-3a8d-b834-cf5cd1a362b3 | -4.4771 | -50.09256 | 2025-11-29 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b6c2653-8ef7-3d4f-a3cb-b90523a2b876 | -5.002 | -50.72123 | 2025-11-29 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5ec2e6d-cb6f-3f50-b299-81f0f0323056 | -3.00699 | -45.42495 | 2025-11-29 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aef337bf-1e3c-3604-b7a2-98dba9d3149f | -2.7055 | -48.35182 | 2025-11-29 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8151280-6f54-31cf-ab6c-926d152b279c | -4.35518 | -43.16243 | 2025-11-29 04:42:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 879a93cf-cc4f-38e3-bcc0-665224e0e538 | -2.78401 | -47.42746 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc23a29c-2717-343e-804f-af51529cda16 | -3.94919 | -44.76283 | 2025-11-29 04:42:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78e1821a-5a31-3b0e-a8f4-0b897bf745d8 | -4.0556 | -48.82559 | 2025-11-29 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52330b0d-dfbf-377a-a75f-ad15d8adb693 | -5.23427 | -41.25317 | 2025-11-29 04:42:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f22cb87-b871-301d-a288-eb3cac6b46f2 | -2.91499 | -53.06738 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad11fbf7-5d6b-3a9f-9ebb-93190e172fa0 | -3.26083 | -52.57732 | 2025-11-29 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25dfa4ad-2ff7-359e-bf11-974fda43fa70 | -3.22936 | -50.31397 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3df1970-8864-3689-a752-9ffbbd0c456c | -2.74347 | -54.59558 | 2025-11-29 04:42:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2916938f-9aac-3d06-b137-c402523e556a | -2.47327 | -50.23379 | 2025-11-29 04:42:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2557948-278e-361a-a257-9fd8ffe52a1a | -4.6327 | -43.9922 | 2025-11-29 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a08f5018-a2fa-3602-88ac-79f14fa1c20b | -2.84061 | -51.81838 | 2025-11-29 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7873eda-d5ac-33b4-9745-cf43036dae5b | -2.42443 | -47.23355 | 2025-11-29 04:42:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02d59a89-5d51-318c-9226-d926bfc57321 | -2.92639 | -53.27069 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b6fbb46-4ca9-3a44-865f-7aeb3c196037 | -2.42106 | -47.23302 | 2025-11-29 04:42:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03f1205a-28d1-352a-8758-6e3e6bce52c0 | -2.59548 | -46.8753 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a43dad7-5867-3167-89ec-4ef583be8ad3 | -2.55017 | -44.60466 | 2025-11-29 04:42:00 | NPP-375D | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56684c49-38e2-33a8-b48a-b14d568970a9 | -4.35578 | -43.15842 | 2025-11-29 04:42:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cdeade3-9e94-3c0a-b64d-3d8da5c4c858 | -2.74647 | -49.33157 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README21.md)
