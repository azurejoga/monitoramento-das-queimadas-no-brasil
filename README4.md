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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23c5bd41-e0e5-385b-bec8-6d8a554ff483 | -22.8594 | -53.50518 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| f899b2cd-235b-3ce5-acad-f5a97e9d9cf8 | -22.83963 | -53.47362 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 18057a61-7764-3433-97ad-68610c04dbec | -22.85376 | -53.49617 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 31e513f8-654f-3885-8ad6-05716ff770ca | -21.88677 | -56.10923 | 2025-01-18 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 327234ae-6c44-3e95-b45e-83baf5d5588c | -22.83905 | -53.47755 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| dc59ecd6-e06b-39a3-a97a-7ffafd0e1e1a | -22.85765 | -53.51694 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 32903afd-0b13-3754-93f8-a9eb8b228edf | -22.85658 | -53.50068 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0d9008d0-95d1-3120-9a1b-4d527dd09066 | -22.856 | -53.50459 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 465faf39-b72b-3c43-9da7-66a50e0c4b99 | -21.88613 | -56.11306 | 2025-01-18 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d73c72e-0112-3968-a45a-be1265c2fd65 | -22.85882 | -53.5091 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 24b16cc0-7330-387b-b750-65cb80c90921 | -22.8628 | -53.50576 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| f51a0da4-1775-3d0c-a2f5-60c8da0b4fc9 | -22.85035 | -53.49559 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8e08cc06-0bff-304f-88cc-136c01a56153 | -22.86164 | -53.51361 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| bbe3db93-68aa-386f-a86f-e75faed43994 | -22.85542 | -53.50851 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 014f5aac-b838-34b5-b48a-2462525e844c | -20.76382 | -46.76971 | 2025-01-18 04:50:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3152943-2151-34c6-af03-cc728fcd4e94 | -22.86222 | -53.50968 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 461c0ca0-4879-3d34-a1c4-3ea622a82280 | -21.88277 | -56.11239 | 2025-01-18 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9802d13-d0a1-307e-ac32-8c4aa4b02e0d | -22.86106 | -53.51752 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 1714f3cc-8309-32fe-9fde-5184b57ad977 | -27.08055 | -50.50832 | 2025-01-18 04:53:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0a931a4a-7ede-3a2e-ac00-e39590abc092 | -29.10692 | -55.93958 | 2025-01-18 04:53:00 | NPP-375D | MAÇAMBARÁ | RIO GRANDE DO SUL | Brasil | 4311718 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 564fc3fe-a7ec-3bdb-b3a5-0ca549451c83 | -29.31955 | -56.00767 | 2025-01-18 04:53:00 | NPP-375D | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| adc61ef8-f4c4-39d7-9989-e6c9471a16f7 | -29.31498 | -56.01503 | 2025-01-18 04:53:00 | NPP-375D | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| d65ccb91-693b-376f-8274-338e300a21b8 | -26.46208 | -52.22988 | 2025-01-18 04:53:00 | NPP-375D | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02cf8b5e-6438-3a8e-9ff1-fd166a39b53d | -29.31103 | -56.01838 | 2025-01-18 04:53:00 | NPP-375D | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| fbacdb60-e174-36e4-9c2b-587215765073 | -29.10752 | -55.93557 | 2025-01-18 04:53:00 | NPP-375D | MAÇAMBARÁ | RIO GRANDE DO SUL | Brasil | 4311718 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 01744f2a-61fe-34b2-bea3-a8bd9f90874c | -27.08466 | -50.50875 | 2025-01-18 04:53:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7cc20fc1-35a5-3e65-b348-3e04e5581d03 | -25.20166 | -52.78273 | 2025-01-18 04:53:00 | NPP-375D | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dcafa10d-a7a8-3180-a468-aabb2a89a8d3 | -22.8585 | -53.4947 | 2025-01-18 05:00:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 70.6 |
| 56de8831-ec03-3c41-819b-7ad84db08d8a | -22.8579 | -53.5169 | 2025-01-18 05:00:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 0d448cf8-7e63-360b-84af-d26fafb39b2e | 3.61895 | -60.11448 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d924790-52c6-31bf-b075-ab87d9dd814b | 2.9429 | -60.16461 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bb98e0f-b36c-3968-a24a-1a5f7795648d | 4.36282 | -60.81875 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ccfeca8e-f770-357b-9dba-7c68e4554289 | 4.91343 | -60.28422 | 2025-01-18 05:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c150d3a-10d5-32d6-b2ad-2caf68eb9064 | 4.91529 | -60.29645 | 2025-01-18 05:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acce6641-bfff-30b2-b1aa-a9a52ce79b8f | 3.28743 | -59.95882 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f69787af-49a1-3805-a550-61e5a8865f59 | 3.67279 | -60.61889 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a6408d7-797c-30f2-b438-e42d80151c3b | 3.11039 | -60.76682 | 2025-01-18 05:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a716a99e-2a93-3897-a4af-022328e0d77e | 4.12839 | -60.0145 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 688429ff-6699-3fa1-b628-ddc3f19e7f26 | 3.29139 | -59.95821 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5c58673-2c35-3c6f-9da8-b3ba278c3f9b | 3.61494 | -60.11512 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6462a7e1-4161-3295-893e-4853e4cff2b3 | 3.10681 | -60.77125 | 2025-01-18 05:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6eaf45b-2324-3349-aafe-88e0b1a5a816 | 3.30413 | -59.93555 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82f83b45-3a75-3322-bd06-88ee0209ab2e | 4.81083 | -60.63396 | 2025-01-18 05:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52184c4e-d3ce-310e-9e0f-28a883958723 | 4.11632 | -60.84229 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12dbcb81-57e7-311e-a285-f3014eadf4d7 | 2.37656 | -61.25797 | 2025-01-18 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9b0c81b7-fadc-3d8a-84d2-aafcd2738d8e | 2.6274 | -61.46189 | 2025-01-18 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 681c06b4-98d6-3c1f-8b61-8ec83dba4ecc | 3.61739 | -60.104 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdb55025-8ee9-37c4-8e32-ed688c4a5303 | 4.36706 | -60.81797 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f4fa95c7-4d4b-30f2-acee-65d90630f5a2 | 1.87851 | -60.36323 | 2025-01-18 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baf850a3-4b17-314d-a831-20623bb10c79 | 4.53408 | -60.68956 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ab6d32d-30b7-3c58-933f-5f05d613b551 | 3.67103 | -60.61843 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f7160ff-dc64-3b57-b903-d820bba2f7a8 | 4.72114 | -60.46963 | 2025-01-18 05:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32c6a28a-09b5-364e-a0a7-4520fe68b6c5 | 1.88897 | -60.4828 | 2025-01-18 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f19147e-2dc8-399a-9efb-fa526f13dc3b | 3.28028 | -59.96511 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bebfc4f-1460-3309-96c7-a02f8337cf65 | 3.27312 | -59.9714 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 63c27300-5aeb-3313-86d3-9681b59dbdab | 2.94689 | -60.16401 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55adefc4-cd1a-312d-9aed-7d4ff90121da | 4.37069 | -60.81304 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba673cc4-c730-37a1-ba7b-3f4b69879a28 | 4.53299 | -60.68234 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9d20800-daea-33b6-9b95-e815758c2023 | 3.61546 | -60.11862 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00a739fe-d3fb-332b-b0f7-2bf0e5f0402c | 2.67858 | -60.41632 | 2025-01-18 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70fbf7ff-fe49-39fd-b343-f96ec842207f | 4.11046 | -60.01383 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60a0ed3a-2c78-3268-a39a-b668f1bc23fa | 2.0517 | -60.00801 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fdba5cb-2593-37d7-983a-6dad04c416e0 | 4.81503 | -60.63312 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a69c5ca4-c860-37ee-8468-f91b4027b8e2 | 4.36341 | -60.82278 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2a7b0027-ef3d-3821-ae32-f05c8e2a507c | 3.28347 | -59.95942 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f880710e-0b9b-3422-b5b4-1c890e1764e1 | 1.88952 | -60.48628 | 2025-01-18 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccf44c22-3268-3e7a-b6bf-ca39a20cab96 | 3.28424 | -59.9645 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96b42396-918b-3445-a864-2a53d23812ff | 4.13293 | -60.01745 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12cd6f45-62ba-338e-8530-d86f620391e7 | 1.65867 | -60.1384 | 2025-01-18 05:05:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a3b17de-d43f-338b-97ea-466bad4dc1e0 | 4.36765 | -60.82204 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 592660d7-7c44-3191-bbb8-0f4e5436feda | 3.10207 | -60.7681 | 2025-01-18 05:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07ea77ff-d1c1-3e1d-8e4b-9b37e4ffcdd5 | 4.29348 | -60.1205 | 2025-01-18 05:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5701f68-67ae-32b3-8474-541c25bb07fd | 2.37229 | -61.25859 | 2025-01-18 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15a52655-0c73-34cb-b24c-0165bc4379cf | 4.11393 | -60.00962 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61f99b40-486f-3dbc-bc4c-4fb3ec156ac9 | 3.10982 | -60.76303 | 2025-01-18 05:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 239b6cdc-d7a2-3e18-b42b-59de15264a89 | 2.68262 | -60.41569 | 2025-01-18 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46a992a0-33c1-3c37-ba63-182c4a55cbc6 | 3.29535 | -59.95761 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30052b23-d4e1-3069-9200-887f14165600 | 4.10994 | -60.0104 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a262fb80-da92-32ee-b52b-f1a90c77a5c8 | 4.29752 | -60.1198 | 2025-01-18 05:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64fe51dc-8e78-3a87-a582-938a80bebf4c | 3.26992 | -59.97708 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8bafe462-3d51-3d06-a9a6-6cea731f61bb | 3.61791 | -60.10749 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a6b93af-5659-305e-b7f1-acc7090703fd | 4.37128 | -60.81712 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d80f3fc3-f46a-38a4-b7fe-3a6222e23708 | 1.65921 | -60.14143 | 2025-01-18 05:05:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 751fb491-bf9f-3827-8a61-04853144df5d | 2.61401 | -61.31353 | 2025-01-18 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8afa1e04-9e83-3737-843a-cf8d37c2318e | 4.53353 | -60.6859 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13c5ca2f-30e6-3fe4-861c-274d55de08de | 3.61843 | -60.11098 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8140c65c-e824-3034-b68a-0b247242b550 | 3.27708 | -59.97079 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 400054d5-ba99-3ada-a4fb-4bd3b7de143f | 4.37187 | -60.82113 | 2025-01-18 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 580c6944-51d4-3714-8468-3a37047ca810 | 3.79994 | -59.71663 | 2025-01-18 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1393898-57c7-3d46-9928-34acde0a45c0 | 4.91746 | -60.29661 | 2025-01-18 05:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e33f2904-501d-3554-961c-9d90f0882e52 | 3.27632 | -59.96572 | 2025-01-18 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 267f6254-54f5-36e6-9c40-1d56d7102656 | 4.91934 | -60.29525 | 2025-01-18 05:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e30e5d6-c66f-31bc-8dbd-a9b1882f1186 | 2.60972 | -61.31419 | 2025-01-18 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c825a99a-e949-3844-aa40-515fc3cc0052 | -0.3543 | -62.7527 | 2025-01-18 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c95ef3c-1329-3ce4-8b38-c122804b22ff | 1.11478 | -59.46201 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35956354-f32e-32dd-a5a6-1c089e5d3ade | 0.63545 | -60.04029 | 2025-01-18 05:08:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5ef8391-c84c-33e7-95b3-22442ff4c585 | 1.09965 | -59.54468 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ed5ce69-fbdd-3d6b-afb3-d8a3575b499b | 1.12628 | -59.4374 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc23b65b-0b1f-30b1-a13e-df150733e225 | 0.46622 | -60.44277 | 2025-01-18 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aca7f97-62a9-3b7b-bfd5-d8ce5690821b | 0.76678 | -60.10957 | 2025-01-18 05:08:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
