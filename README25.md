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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b28aeea2-2a56-3a09-8ad2-3881d6218873 | -1.99349 | -46.44793 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3872ec79-d89d-3726-8fd2-c6ba8a65863e | -3.48562 | -46.08418 | 2024-12-02 04:01:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6dba851-9cbb-36a3-ac19-f24078d4f078 | -4.2693 | -50.84922 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 89a09b76-ba33-3d24-b3f2-eb5d68ee2c8e | -2.5063 | -46.10889 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8734e822-0338-388e-85e4-6aeef6361213 | -5.12502 | -43.20718 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 951b71c3-85a0-3321-8329-95f3b801d823 | -3.64856 | -51.12384 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fdf15e0-152e-35d0-9814-806cc2318e30 | -4.91576 | -41.339 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| aae8ef0e-2ba8-396b-98a2-cb57006968ca | -5.00516 | -44.17211 | 2024-12-02 04:01:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2acb6ed6-b024-3ff8-8411-5072d7a5d082 | -3.02978 | -51.53599 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 953b40a8-3c94-3b72-ab60-11d04afec3ff | -0.31488 | -51.78116 | 2024-12-02 04:01:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f228eee8-7f1f-3d51-a622-e4dfda78adfb | -3.09988 | -53.23808 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f1b83edf-7043-3160-a8f8-85fc23c2f0e7 | -2.60849 | -45.25361 | 2024-12-02 04:01:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9190af9a-4c52-3c33-af1d-7b73013c2042 | -3.26061 | -46.44606 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d87db770-792c-3b39-840c-ab67a5887211 | -2.7981 | -48.68372 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c2dbd91-4f21-39c0-8209-360c8c23dc94 | -1.99655 | -46.45856 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d7a17aa-90ed-3c7e-b65c-661fc9d77bd7 | -3.36689 | -53.21792 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4d93d0ce-6c5a-3dda-9d89-c44ec81b64c9 | -5.58587 | -45.20915 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 559bd3b6-0b92-3066-8c40-58705d695387 | -2.98942 | -52.51552 | 2024-12-02 04:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97bbd1af-1412-3267-abc4-fbcc9cea1bf0 | -4.43927 | -45.35714 | 2024-12-02 04:01:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee3cdacc-7714-3342-bee1-9b80dfda6814 | -4.64074 | -46.90173 | 2024-12-02 04:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8ec1bf3-367f-3687-997f-06095a9253f2 | -4.11434 | -50.49814 | 2024-12-02 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99e34ed8-0649-313a-8c93-2c0b2340d4ba | -2.85946 | -48.56351 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccd887f9-e005-3d45-8bb6-a34fc8f9c050 | -1.961 | -46.45595 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab0484c8-6ce3-329f-8fb6-5ba3f63674ba | -3.28951 | -46.04237 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4cd226ac-7abf-3614-9b62-d657f1b3cbce | -3.989 | -46.65493 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f411a462-49ee-3211-84a9-8a16bc06be03 | -3.26479 | -45.37396 | 2024-12-02 04:01:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cbfb252b-5a05-3e87-8af0-1584926bf0f3 | -5.58179 | -45.20848 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c8259ff-9125-35fe-9446-60fcbe86f5cd | -0.31705 | -51.77896 | 2024-12-02 04:01:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f90eeb5-0a82-3b71-88ea-54b15180fc0e | -5.17016 | -43.04948 | 2024-12-02 04:01:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d2fe8e3-5d08-3449-8ece-537d54bcfcf1 | -3.7463 | -52.2731 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 067ecbe0-9519-313b-bff7-1d5ba620b0e6 | -4.26246 | -50.85277 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0948827c-cb45-3cef-a005-5720d64ca512 | -5.00594 | -44.16736 | 2024-12-02 04:01:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e8ef876-ad9d-38d1-8eb5-0646a7e5c699 | -1.8277 | -46.22763 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f603393-b58f-3acd-a614-8b81dbdcb4a8 | -2.24188 | -47.05577 | 2024-12-02 04:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ad4fc67-b4b3-37f0-8f00-f6b8a42b3d4e | -4.06948 | -47.09 | 2024-12-02 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f71ef4d-e3ec-31d6-a8b6-50b6d99e1968 | -6.00206 | -45.41981 | 2024-12-02 04:01:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a45e882-1cdb-3a2a-8125-5396960ee64f | -2.65132 | -46.7782 | 2024-12-02 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d3bd9f5-fa69-36b9-a956-a179dc9427f0 | -3.32583 | -50.19067 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2aaa275f-5cab-3508-acf7-6c4b12b47e0e | -3.93096 | -46.71888 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f09509c-d189-3942-ab18-380b3aeb7898 | -3.70642 | -51.83591 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0378e6b3-151d-303e-8efb-cc99f8b1de43 | -1.91309 | -46.41065 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 303ecc91-8af0-33e0-bf8a-58bfae07bce6 | -2.24341 | -47.05951 | 2024-12-02 04:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b81c37c-7f08-3f38-991c-11e49bd431d3 | -3.95627 | -46.30585 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a51e3aa-4366-3b9c-9d24-06920dcd669d | -4.64449 | -46.89979 | 2024-12-02 04:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 976bf702-ef9c-325f-a578-245072ef726c | -1.73396 | -52.78067 | 2024-12-02 04:01:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c363e97-da00-36fa-9a19-04857f18c450 | -3.35763 | -49.5057 | 2024-12-02 04:01:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2227fb4b-fb17-39c3-9dce-9abd02f0ed74 | -2.48157 | -46.58082 | 2024-12-02 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33be3146-659a-3b58-a65d-1591f014b154 | -5.58334 | -45.14963 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| c1b19f52-1744-36ef-84e5-4ce7b39e9ad4 | -4.6401 | -45.93312 | 2024-12-02 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5add5749-8050-398e-8ff9-2ac97a11e5d4 | -3.9623 | -46.0169 | 2024-12-02 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05b3dce8-4fcd-3e02-bee5-fbb89d15df4f | -3.25622 | -50.57377 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6801836-3fbf-3f0a-a0d5-2d949add09c4 | -4.32977 | -45.92399 | 2024-12-02 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00c42f6d-305f-331e-99e2-4ad842bedc5e | -1.52439 | -45.92089 | 2024-12-02 04:01:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f454522-21f1-3c59-a00a-1be67f214d0d | -3.39151 | -51.14823 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ec053a6-1e84-331d-a17e-17d39ca5206c | -7.8851 | -35.1359 | 2024-12-02 04:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9a014e5f-6e35-351b-bc97-8d82600ffc37 | -3.21799 | -45.76419 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 725ec3d3-dfb5-37a1-bfcf-fdfaef660b69 | -2.79432 | -51.90252 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 07678b67-a7f4-3f61-9397-b3b5762f8e42 | -4.81761 | -44.35569 | 2024-12-02 04:01:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 887e9af1-0d16-32ef-bd2e-dbac550143ac | -3.74727 | -52.26736 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9729ada5-91b3-3986-b673-ee6d3793bcbf | -4.10837 | -50.4973 | 2024-12-02 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7928d4e9-63a7-31bf-b3a2-2b4851f41253 | -5.11639 | -43.21455 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b87165d8-6d31-35c9-bac5-3633a85c9163 | -4.64152 | -46.8969 | 2024-12-02 04:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f84cad6f-c3e0-394a-86af-15ebd8f30c08 | -5.58394 | -45.14605 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1fc0ebe2-96f3-36a4-9f3e-e5af8469394f | -3.47534 | -47.68305 | 2024-12-02 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a116a4e3-07d8-374e-829a-b3e11e8c7c4e | -3.85205 | -43.93406 | 2024-12-02 04:01:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3d0a28e-05bb-3bbe-8b1e-77b5e9edf9d8 | -0.31028 | -51.77767 | 2024-12-02 04:01:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 844fbd62-6cce-3beb-b3cc-36a0e0cce27f | -3.1406 | -45.23357 | 2024-12-02 04:01:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ffa32cf-64d6-3690-bb30-18c39c3ee7b6 | -5.79864 | -46.14296 | 2024-12-02 04:01:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47bf598a-991f-3998-80ec-938a9f28729f | -4.91295 | -41.33493 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7474c6fe-b281-39fc-bb43-64d1ad0d0896 | -1.6312 | -45.41373 | 2024-12-02 04:01:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3fa8ece-496c-3aba-be7a-607515a3ae34 | -3.15748 | -51.11371 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 847c43aa-7027-3561-9f71-fd34df310643 | -4.07519 | -49.05551 | 2024-12-02 04:01:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fd0d484-1798-3661-839f-9a4947eae38a | -4.90735 | -41.32671 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e714471f-d031-3d44-a711-3eb35dd3e3a4 | -7.88044 | -35.13905 | 2024-12-02 04:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3f0fe23a-db64-39c0-a391-8ac0cde81754 | -2.77819 | -49.21603 | 2024-12-02 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8688101b-c192-3560-9eb4-b07d9ba073da | -5.36863 | -44.90308 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae0a89bd-f3a4-3115-ade4-940907a42181 | -3.6999 | -51.83494 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fb9ad5ad-89fa-3264-9acf-0b0482d534b8 | -5.12138 | -43.20664 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| be10529b-4d65-3dce-8f6c-a1ed476b6c1f | -4.06937 | -46.68001 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 929e688f-c976-3f05-befd-881075748749 | -3.16376 | -51.11466 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bee4dad3-dc22-3d83-89fb-cefad2e18de5 | -3.21869 | -45.75996 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77831a1d-a43f-33ba-bbd3-434425fe5db2 | -3.87865 | -46.58103 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70948c33-8362-370d-b576-41f795bd36ec | -3.5524 | -51.45489 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b1aff940-afed-36f1-b70f-d7bc43fd61da | -2.75179 | -51.75447 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25842695-7340-3064-9516-14832f13d178 | -2.86593 | -48.55769 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6458c5c-f4bd-3c33-9a8a-b71d3c201719 | -5.17297 | -44.67043 | 2024-12-02 04:01:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6ea5d99-7a7f-3f0e-a4e5-2c171b564655 | -5.19835 | -43.86958 | 2024-12-02 04:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95072f29-98b7-3b2c-987d-636f0080d4a6 | -5.58679 | -45.15388 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 779e935f-8323-3009-b7d5-a63640e79219 | -6.36847 | -47.35181 | 2024-12-02 04:01:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd3b04c0-eeed-3642-912a-2a2be6f20019 | -3.28578 | -50.62788 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e87394a-9994-3a4c-a784-b94a5f55533f | -5.57904 | -45.14875 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fbbd8c41-f3c6-3fd1-8049-f670d098d755 | -5.55021 | -50.27168 | 2024-12-02 04:01:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ac681bd-6204-327e-beeb-c0acb65ff206 | -1.53599 | -45.84721 | 2024-12-02 04:01:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cd931e9-3b03-35f7-97b4-ad642d0d8bb8 | -4.26324 | -50.84817 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| be4a6732-da7e-3bf6-8a5c-22fded3ba6a1 | -4.57982 | -43.3544 | 2024-12-02 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 554f6fd8-69a3-378d-9e7a-ca6d34baee0e | -3.93061 | -45.79485 | 2024-12-02 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 690c584d-3ea3-3b18-bbf2-4153db6039ee | -4.09042 | -44.85391 | 2024-12-02 04:01:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bbdf53e-ad53-3943-aa66-488bb0b143ea | -3.87403 | -46.58047 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 360a7126-6413-3260-83ff-eed0e1489b5e | -4.17659 | -48.20049 | 2024-12-02 04:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daef87ed-82bb-32e4-b5b0-36161984df41 | -5.12888 | -43.21062 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README26.md)
