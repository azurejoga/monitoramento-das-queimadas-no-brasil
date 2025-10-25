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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b16c95f0-1c64-3ab7-9a97-f8d358e2f08f | -9.86802 | -44.88974 | 2025-10-25 04:19:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 772ccda3-6420-3abd-8289-7a8e968f4b9a | -10.68923 | -48.089 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8571dbf8-b8dd-3101-9404-a6319c8350f7 | -8.59675 | -44.83065 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be655adc-1969-3b25-957d-9254ce49063f | -12.28087 | -47.02607 | 2025-10-25 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0388845-5a0f-3ca6-8da6-df96c6313cb2 | -12.90824 | -47.74314 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5435c8f7-9f4f-3970-8d6e-10a49e2793eb | -7.98293 | -47.39133 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a7977f6-6b5e-377b-9d80-3a5f4170ffa5 | -9.17959 | -48.849 | 2025-10-25 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07d341dd-c5e2-3153-8eda-4b3d5c8dc75c | -10.45069 | -44.96464 | 2025-10-25 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2e3a626-290a-3871-85cb-8f9343e6cbc7 | -13.34024 | -47.97559 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b6b12eb-d046-3f58-b10a-c59ad8b8c174 | -12.38514 | -49.95058 | 2025-10-25 04:19:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78caadda-b68f-3dd2-8f89-dd13785bedc8 | -7.81531 | -45.11096 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33085820-6d83-3f52-8713-e1ecf2d27384 | -11.2576 | -47.55729 | 2025-10-25 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa0455a6-95f2-3774-adb7-dd312856e4a8 | -13.05258 | -47.21011 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98aae3dd-c0d5-3698-8454-a12662ce10a7 | -9.64905 | -47.7564 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12bc14b8-0db3-3047-b421-ad2b282a5421 | -12.10525 | -46.40484 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69c84bf6-efb8-3740-9e03-0c36d2d6b775 | -9.19853 | -46.3444 | 2025-10-25 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa26d448-fa96-3ff8-9a50-6fb869326610 | -9.32126 | -45.19192 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4144c03-0201-3078-a72c-8d4fc4d79fa3 | -13.21779 | -47.78296 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58d860cd-cea6-35cd-97a0-3bc31035bc02 | -7.84914 | -40.89946 | 2025-10-25 04:19:00 | NOAA-20 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a80790ba-94a0-39d0-bf69-901f4c6a731b | -8.5564 | -49.86335 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4f6b18a-9c48-3e37-86a2-d4a40301b92e | -12.22771 | -43.31197 | 2025-10-25 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4106628-f4c5-3c5c-b030-155e9fecae33 | -6.41304 | -53.6633 | 2025-10-25 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0368baef-cf5a-3310-acdf-9127fb0860ad | -12.83613 | -48.63855 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31512f4b-358f-3cb9-8b9e-9c6e4b0c6a6c | -7.69542 | -46.91388 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a7eb973-3f7c-3364-94f2-b453720ff721 | -7.77637 | -42.91484 | 2025-10-25 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b25ade8e-1e45-3e8e-912c-e1267af6a299 | -11.36351 | -54.32911 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e80049fd-94f0-3ff0-9b93-0a06eba66901 | -13.33219 | -47.9394 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 662ff3bd-ec11-38ef-a61e-5c673605bc52 | -11.93863 | -44.54317 | 2025-10-25 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d102f25-8f81-30ce-96a9-65594ebf74ae | -6.8846 | -43.61618 | 2025-10-25 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2795f423-7f90-37dd-a32a-ed0a96d66b4a | -12.28953 | -43.77996 | 2025-10-25 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e592ef79-cd49-3a90-840b-b866a02c37cb | -8.66362 | -44.77391 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 544f03d3-c96b-3398-801c-7c2eb2615597 | -11.57081 | -51.46753 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f574328-9c67-3caa-8e53-1e60cbdd0340 | -6.79635 | -46.4649 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa488078-cd07-36d9-99d2-8feeb1a3c261 | -12.80743 | -48.67682 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb7a8737-2115-3916-a994-0060307a69f9 | -9.59095 | -46.8863 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82cef62f-e352-304c-a49c-90a020059ad6 | -7.58657 | -43.57946 | 2025-10-25 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 168a3ad2-beda-3fab-8087-06982a6dca5d | -10.40672 | -44.74502 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a69a82d-8986-348d-a92c-c1700f29ee40 | -10.66261 | -48.07604 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e25b7e72-fa42-3ffe-8930-b048f54576b0 | -7.37554 | -47.02606 | 2025-10-25 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 236364fc-c84d-3fd9-a4ba-9a7cd66f98c5 | -10.63582 | -47.92714 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96457f59-b6fe-3351-ac55-ed3eab94049e | -12.28608 | -43.7795 | 2025-10-25 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5218ec0d-e206-3617-a7dd-6bf8a03b789b | -11.14394 | -44.93792 | 2025-10-25 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c7907a44-4995-31eb-b015-de6eef5ed263 | -12.08917 | -46.42027 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d75ca143-0dcc-3df6-9a37-b1a635c46cf3 | -10.59612 | -45.20712 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48023a12-819f-3279-b4da-b552f168d920 | -8.27699 | -46.87585 | 2025-10-25 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cad8767-eac5-37e5-b268-fd970e27321c | -7.36323 | -46.99268 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c15c10f-cc71-3a74-b1c3-8961cba733b4 | -9.12002 | -45.86053 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f20eb22d-73cf-3624-9aed-ed7459b8f50b | -12.83718 | -43.81262 | 2025-10-25 04:19:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b91e7f1-ad58-3d61-b1f8-479b73724235 | -6.92732 | -45.16121 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba8a9d38-681e-3e62-984d-57de47600e58 | -11.75516 | -44.65119 | 2025-10-25 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e5b5f7e-de16-34d2-add0-d7f38a3782bb | -14.01894 | -44.21714 | 2025-10-25 04:19:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd03f284-ebf8-3b05-82a8-abd5c7720bc1 | -13.31942 | -42.41772 | 2025-10-25 04:19:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8cc5ed14-f5a2-39b4-8a18-46e1151309fb | -13.31571 | -42.41721 | 2025-10-25 04:19:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 61b9e9a3-d4bb-3ec6-af14-16e4345824a5 | -9.32235 | -45.18497 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e65720f8-0369-3bb2-9d11-328eeb2126ed | -8.11638 | -47.06551 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10f1f236-91ed-3aae-95d6-eb7dbe0d4de5 | -8.1977 | -46.50092 | 2025-10-25 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9674201c-649c-39c0-b5e8-108fe1acaa77 | -12.06608 | -46.39442 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c6035275-46f9-307b-885b-ee9ade1369f7 | -13.47421 | -46.49267 | 2025-10-25 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfa19776-9421-30cf-ad34-475b58c34967 | -10.46867 | -50.21096 | 2025-10-25 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15ee6033-f696-325d-9eea-a601c6896dc6 | -12.87485 | -48.60104 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfd7c039-3c7e-3dc8-a77a-25af1d372eb1 | -13.64925 | -44.23172 | 2025-10-25 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fabf895-a4ce-31da-b346-71a4754bb92f | -13.33654 | -47.91287 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebed1a7f-f41d-3265-b820-0f25f9f69659 | -13.28926 | -47.47334 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 961337f2-2f95-37bc-95b1-87c7a1f96c54 | -7.46857 | -44.01011 | 2025-10-25 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 490ecd80-0b99-369c-b8eb-475c735e64e8 | -10.63857 | -45.23903 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 727de905-3602-3b76-9efb-d115f02eb10d | -12.15804 | -43.95781 | 2025-10-25 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea276827-1a65-3169-bce7-f036c9547146 | -6.96401 | -43.50158 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ddc2943-c761-393f-800d-4c27cf1dd494 | -12.68023 | -47.91289 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4883ddbc-f8c7-3ed8-a8a5-603597bbf763 | -9.12058 | -45.85703 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57faaeaa-8ad5-375d-93b2-bfa8529c6265 | -12.04727 | -46.40572 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87d85fd9-58c1-32f1-8594-152fe4181127 | -10.97929 | -44.73024 | 2025-10-25 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c090c7db-1299-337e-9147-38b082757071 | -12.24869 | -47.28876 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97f1fdd0-3e80-3ecd-bd85-488475c528c9 | -12.29641 | -47.45064 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ace926b-683b-370b-a68f-0b43dfc4d344 | -11.10078 | -54.38998 | 2025-10-25 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 558f9321-26dc-3e0e-acb4-1c99bf4336c4 | -10.51118 | -47.67679 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acc48e3b-7386-3d5e-9119-f2f73485e930 | -10.87035 | -48.04937 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51988be5-d57a-3f88-97ff-82d4af7505a2 | -6.81275 | -45.43216 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3ced89a-a97d-3b92-b35e-a2ec5150d5aa | -13.20642 | -44.10735 | 2025-10-25 04:19:00 | NOAA-20 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00b336de-d3d9-3a91-9bc8-1a6439e1858c | -9.53598 | -50.80262 | 2025-10-25 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09d7d94c-9313-3594-863c-c02ddbe18e3f | -7.49384 | -47.03334 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5e9d89f-b453-33b6-a03d-87dde4ba0730 | 0.37734 | -51.00818 | 2025-10-25 04:19:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6ccf024-ad93-3aee-8830-e3f8cf5bc94c | -8.82919 | -49.72396 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f662da5-4b63-342b-b01f-511a8e0d02cd | -13.65023 | -46.81701 | 2025-10-25 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fc9aa26-c1ed-397a-9d95-8ac9e6655417 | -13.29262 | -47.47383 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23c5c756-0816-34e9-bcd3-8e2e10541aa6 | -11.43205 | -44.67783 | 2025-10-25 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b565113-a4e5-3e90-81c0-3656915c962e | -6.97972 | -45.28009 | 2025-10-25 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 099e3c39-f37a-3a3a-b59d-c410c4b473cc | -7.9842 | -47.38346 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d57beb42-e9ad-3e4e-9144-bd7f2210f941 | -12.2406 | -47.44548 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b243957-4147-334b-bdd8-bd6df156c6b3 | -9.60946 | -46.90074 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0d75aa2-0485-3c9e-ad44-6ca5f49fa2fe | -10.56047 | -44.9353 | 2025-10-25 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5749afb-87e4-3d99-ba32-3764c44ed6b2 | -8.46095 | -45.56031 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b73bdd6-6763-3173-b651-26fe09b4c980 | -8.16187 | -47.7613 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 592713bc-b0a1-3da8-b14c-279df9a6df37 | -6.96736 | -43.5021 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee66e8e8-864f-3db1-b7d0-6bded3e3988c | -10.35355 | -49.00275 | 2025-10-25 04:19:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21a3654b-74f3-380d-be66-1d1f580f005a | -13.41643 | -47.96188 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8a18f09-061c-3175-9b91-a0001aba895a | -13.2144 | -47.78239 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 172a8f2c-5eba-346d-88d1-cdd04d4acd48 | -12.21031 | -46.51225 | 2025-10-25 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1989c43e-b426-3bac-abfc-1e4286a31177 | -10.34712 | -45.10613 | 2025-10-25 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8821f352-f8a5-3e1d-8177-62f83a59912d | -2.7964 | -49.136 | 2025-10-25 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9d6d3d32-3a88-39d0-85b5-5c283e80dec3 | -15.2436 | -47.9302 | 2025-10-25 04:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 48.0 |


[Clique aqui para ver as próximas entradas](README43.md)
