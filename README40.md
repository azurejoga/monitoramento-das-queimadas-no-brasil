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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7139a175-a4a1-318e-bede-c7995a528387 | -4.45241 | -45.45241 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 901febfa-4d37-30b4-9a2e-05bbc2f70a52 | -6.11922 | -41.72577 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a040265a-56c2-3119-ae87-b104927e4a88 | -3.84174 | -55.79251 | 2025-10-27 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5a35ed4-3a90-394b-a9c2-c601ad6003d7 | -7.33968 | -48.49098 | 2025-10-27 04:32:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9080f4e6-ae84-30c3-90cb-e3393208c8da | -3.97888 | -55.74396 | 2025-10-27 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a3a24d7-ab9b-3022-ae3c-fc7338b44e2e | -5.57244 | -46.42938 | 2025-10-27 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29c4ceb3-5268-3adf-b9bb-f59a7ac77341 | -8.1221 | -47.03014 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c24091e-4e0c-3c51-834e-10c3de615f5f | -4.43729 | -43.42642 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd720f51-083b-3845-80b3-1a3121bb803d | -8.54081 | -47.20363 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd0701d3-0e80-341b-bff9-8608cba12c3f | -6.14142 | -41.814 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 941df076-e377-3bae-9f48-d30812997475 | -4.83922 | -48.20294 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4f7eaa5-b898-377b-ab12-73d843a9917e | -5.71194 | -49.30352 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee9481b9-b0bd-3df7-b5e9-c277e9a8349c | -8.05179 | -46.95379 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f7de929-75ec-3bc3-898d-7ee8ac2b46ef | -4.44103 | -43.427 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1ae2e92-8511-3643-981d-24f5a052e083 | -7.86757 | -45.71637 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0c268ad-5871-3b0f-9b33-eb5f298610ce | -7.92068 | -45.68444 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fdd83b71-35bf-38c9-8cff-7ae71cc4f4de | -6.8998 | -52.19593 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d60894a-3d2a-33be-a6bb-bdd0e602b842 | -3.70401 | -44.34193 | 2025-10-27 04:32:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0011ab95-ba2e-3ad4-bc0e-5fb3db16ad26 | -3.41271 | -42.4762 | 2025-10-27 04:32:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08f5e32a-1cc6-3300-92d6-a27c302c9455 | -3.57478 | -49.0214 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c02b29f-31bc-3864-9932-c38927499955 | -7.87345 | -45.19633 | 2025-10-27 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b172e42-b6da-357d-ae28-b44998af3190 | -8.54136 | -47.20009 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ab6ab02-094b-3408-8508-3647eead638b | -10.21343 | -45.17749 | 2025-10-27 04:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daf0cee8-787a-3c70-b831-de9aee16a640 | -5.71885 | -49.28223 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 71489585-e542-369d-a475-8e23aca15bf9 | -5.65339 | -41.11437 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 259c8ff8-4917-325d-acfe-6320fbf25dc3 | -4.44433 | -45.98344 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 05905e05-e25a-3f81-bd01-c6dc425260ea | -4.25958 | -48.59827 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ccc0e40-b082-32e0-992d-2887565b4a83 | -6.59439 | -42.67465 | 2025-10-27 04:32:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 28a25884-20c6-3914-a16b-7c5905671a0d | -7.85159 | -46.48927 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7aa3456c-28b1-34bf-b390-6e1eed3299c6 | -7.43676 | -41.88287 | 2025-10-27 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| be77f305-56f1-3316-9c2b-5114aa098638 | -9.72948 | -45.41808 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da80d102-a1b7-33f3-a0c8-b05e263e0fc9 | -4.45898 | -45.46047 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75f5337f-83e5-33b3-a3ed-cf06e69160d5 | -3.73478 | -44.33029 | 2025-10-27 04:32:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aaedceca-ace5-3d01-ae26-b1cb0ed3333d | -5.65403 | -41.11004 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5bc56cc1-d2b8-3f06-b9b7-2cbd8aa18f92 | -7.87163 | -45.71299 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1ba5754-98f1-3e7a-bced-590d3defb7ee | -4.44762 | -50.1578 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cee9158b-c327-3771-9f75-21312d8003e9 | -9.5844 | -46.90866 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24b28152-99d5-3cbd-9fa5-42c55250acd6 | -6.68065 | -41.50863 | 2025-10-27 04:32:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 49e9aea4-c924-3fc2-8dde-281521a82fd3 | -8.72006 | -49.40361 | 2025-10-27 04:32:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82ae59e2-d88f-3367-bf79-02fa450bde64 | -2.80958 | -49.14828 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f6c9d34-ac92-36fb-b916-f0905d14d138 | -7.87363 | -47.25101 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4362e517-35a6-375e-8eee-0341bf1e5213 | -5.60344 | -47.1051 | 2025-10-27 04:32:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 068ee275-373c-3f4e-aa12-35cadd1f6c7d | -9.72292 | -45.41287 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fed141c5-b43b-345d-826d-09e18dca1b1e | -3.11854 | -49.10678 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6fb4e42-cc61-397c-8eda-1f103212cb2b | -4.83172 | -45.33825 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4383844c-5364-380f-9ccb-b1ee9afd1ab4 | -3.48421 | -50.07937 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b99f1acf-8792-3e7f-9e89-27bffbd45899 | -4.3845 | -44.22781 | 2025-10-27 04:32:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 603196d6-2959-3866-94e1-103b1c58c866 | -5.63088 | -50.31394 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1616e88-35fb-3a05-9c67-f7ea20ed51fc | -6.29675 | -44.70619 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eaf930b-bdf7-34a4-99f5-49b6c99d8f22 | -8.03211 | -46.75307 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52ccd200-3185-369d-95f2-0776156421ca | -9.22908 | -45.84158 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1047d38-6caf-397a-8f97-7839a9a85dde | -4.49856 | -42.62505 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad55caa9-b572-363e-bcb7-a5d95140de6f | -9.06221 | -45.09198 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 715f9956-fcc5-3cf8-af57-245667b6fedb | -6.88325 | -45.15979 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e3157315-866a-37e2-9ac2-33261b3a17ed | -8.11225 | -48.81517 | 2025-10-27 04:32:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca289064-9264-357c-8279-54b2e7cc7068 | -7.84746 | -46.40312 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6eef98ee-5890-354d-984d-913317bd3ae6 | -5.71944 | -49.27858 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08644146-f772-3475-997d-d0de14c0cea2 | -5.71533 | -49.30405 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fda444c1-3df0-3f75-8c25-090cfc1c66df | -3.60967 | -43.56054 | 2025-10-27 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 300a52dc-b665-3b08-ae3d-fc18690690c8 | -4.32614 | -48.08991 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29a4df57-5697-3a7b-b6bb-ef10716ece1b | -6.69523 | -42.04932 | 2025-10-27 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e2858154-4779-3d10-862e-4eb1b86f75d7 | -9.28129 | -47.00705 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f477a5d-326a-3a1a-a4ff-4ce2c5398eee | -7.36499 | -42.44288 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7cd44cdd-8bd0-3739-b22b-00f01a626893 | -2.37875 | -55.96173 | 2025-10-27 04:32:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38ae3a88-f64e-3289-b26c-f2d7a53f3204 | -4.72649 | -49.08827 | 2025-10-27 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89fdd416-a18e-31c7-a751-1b6733a03b88 | -8.32745 | -46.82043 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 961774fa-bbe5-3f4c-a813-4a46ef7813e6 | -7.85048 | -46.49652 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b17587e-095e-3a43-86c1-0d22a4d922d5 | -8.07347 | -46.94626 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1de05510-9625-3c43-93a9-44e5b9d14315 | -7.40174 | -44.60656 | 2025-10-27 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e6bdc717-689d-3a67-b302-bf1aeba3234b | -3.09032 | -49.52407 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc8fc693-37ff-3d0f-9c34-e048f7185c5e | -5.33485 | -44.71845 | 2025-10-27 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 379e036e-f180-3294-b7bb-639bafffbab0 | -7.87417 | -47.24752 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 859609fb-4cdf-3ec3-a573-60b806938c47 | -3.73186 | -44.51877 | 2025-10-27 04:32:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46df3f6f-b988-33d5-950c-876087cea98a | -4.85199 | -48.6589 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da40cbbd-7463-3d08-b622-b749ce235df7 | -9.53692 | -45.79228 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40f65413-27a1-323a-a092-8e0d384beec7 | -10.09276 | -45.33596 | 2025-10-27 04:32:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10d29435-c8c9-3e15-b6ec-851e7c3861ac | -3.57331 | -44.53283 | 2025-10-27 04:32:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1f4396c4-de68-3280-b430-9b1317aba874 | -2.27306 | -47.85579 | 2025-10-27 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 195f0d2f-198c-3f7d-98b1-c110887db8a5 | -10.01407 | -47.17101 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a675499-078f-31cf-9c59-5dc083390005 | -6.1765 | -43.7377 | 2025-10-27 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a445a0d4-a60b-3c83-9d6c-9610a50e3257 | -4.45524 | -45.45662 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| b4451a2f-0cbd-3044-a61f-d453e5943c25 | -8.65477 | -44.76243 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d890af59-0549-3582-8358-5a667709747e | -8.32636 | -46.82756 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9bbf953-e95a-3812-b671-e5eea6704f9c | -4.73696 | -44.81318 | 2025-10-27 04:32:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4edbcc66-0737-3238-9407-9a6e9164f0aa | -5.63606 | -47.63568 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f76f0c8-8a3b-3376-836b-1132f21c0f28 | -6.12523 | -41.71423 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0251ec93-33fd-3c26-9c5c-4ad61b0974fe | -4.87648 | -50.85413 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd9a3d57-1f2e-3551-ac1b-fb1c0c09848f | -3.40083 | -49.98843 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b515575-64d5-348c-a619-46841b3ac121 | -7.24397 | -45.80367 | 2025-10-27 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7878c1c1-4bdb-39b8-92d7-62d8f2ead9e2 | -10.01864 | -45.00036 | 2025-10-27 04:32:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1d3fcdc-9d84-3c3f-a6e4-88f7d06e4807 | -7.8414 | -46.46548 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7230e460-5f0f-3c64-9d2c-53c1885451be | -4.47474 | -43.43222 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13c2b583-d2f3-3a7c-b887-9ffaac4b8142 | -9.26507 | -45.5745 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c74e32a5-6c89-3a69-a737-5dd56c98d813 | -4.86615 | -48.52703 | 2025-10-27 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bc566963-4424-3514-b077-c2f6d60cc77a | -6.73938 | -45.34359 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d5ca614-0416-32c8-975b-17ce8add72b9 | -5.59604 | -41.31941 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 00ebfa16-aebf-3f58-bce2-57d9396bcb17 | -6.4914 | -44.43943 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60c2611a-8a2c-3429-8899-fea5b1261699 | -6.08943 | -47.00077 | 2025-10-27 04:32:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49c1c1d8-5619-3ffe-9fc0-1edb0e2bb08b | -7.0016 | -46.99633 | 2025-10-27 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2dd29b1-7854-39b0-9ded-99b534b43afe | -4.9589 | -44.87738 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
