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
| 12fce3e9-d900-3282-b95f-aabc86899cad | -13.84618 | -46.89347 | 2025-07-13 03:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0eca6a52-57f7-3665-bb4d-73fca7ef5614 | -13.84502 | -46.89885 | 2025-07-13 03:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 456c3417-3e26-35d2-b11d-5994136f0310 | -13.88214 | -44.45926 | 2025-07-13 03:32:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1bd3eae7-e3c4-3b4f-8443-932629d87612 | -13.91691 | -47.42448 | 2025-07-13 03:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ddec794-a8ea-32f2-a71c-a98c164484fd | -13.11331 | -47.29716 | 2025-07-13 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d6c0074-02c3-33de-a771-170ea62fe463 | -13.87727 | -44.45404 | 2025-07-13 03:32:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51a43d3a-f576-3d36-a2c7-5fb5c01325de | -13.11551 | -47.28693 | 2025-07-13 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1bf683b-9dff-3f0b-8a35-5a28303bd52b | -13.1044 | -47.30534 | 2025-07-13 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0272d67f-7605-36c8-a9a1-21149de0ac30 | -13.83554 | -45.89885 | 2025-07-13 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5a0ba10-513e-35bd-9eff-64d0677159b6 | -13.91279 | -47.41635 | 2025-07-13 03:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 971f12ed-fefd-3c8e-8106-436e3c19a8d0 | -22.73914 | -42.9584 | 2025-07-13 03:34:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e1a23e6c-b3ac-3c72-bdfc-7b41bdae183c | -22.66181 | -43.29337 | 2025-07-13 03:34:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7af3a5ca-c250-3b82-9f7b-4551644c12e7 | -22.90037 | -43.7507 | 2025-07-13 03:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 64ba7843-3b0a-3c97-b760-2c257ba98e4f | -22.74769 | -43.27034 | 2025-07-13 03:34:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 57482b9d-2f09-3404-9d8a-fe258fed0f6d | -22.69771 | -43.34818 | 2025-07-13 03:34:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ba4dcdf-dc87-3567-b918-033ff10b3b15 | -22.85212 | -43.36323 | 2025-07-13 03:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fc4fd096-4f83-3499-b4ca-606ecd70fce6 | -22.66282 | -43.28848 | 2025-07-13 03:34:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 91389a7c-2aed-3c5d-b101-be7e4cc6d095 | -5.739 | -44.9945 | 2025-07-13 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 6cfad023-c2b8-39f1-bccc-3af846bbba12 | -13.8474 | -46.8964 | 2025-07-13 03:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f20aca35-c30c-38fb-bfaf-5060558ffe95 | -5.7392 | -44.9718 | 2025-07-13 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 5a32860b-b87c-364a-9b5b-fc4fdd48bc37 | -5.739 | -44.9945 | 2025-07-13 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| da140acf-b481-3f12-9ad7-d97fa9ef4167 | -13.8474 | -46.8964 | 2025-07-13 04:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| bed22a15-fe53-3722-826f-de64b0130fca | -5.739 | -44.9945 | 2025-07-13 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 215c6f46-6bd0-33b1-a95b-a6d6ae684a07 | -13.8474 | -46.8964 | 2025-07-13 04:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 9e943b9e-493c-3d54-b1f0-bd1d03e30f82 | -8.32686 | -44.93578 | 2025-07-13 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6c9c7fa-5a2f-36d5-8e2e-0f6cc8db80e7 | -5.21033 | -44.35503 | 2025-07-13 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c5f1eb4-c402-321d-8d3a-6479c1379a30 | -6.16221 | -45.91391 | 2025-07-13 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fee5c82-838b-37fb-81b3-b1f2c97edee1 | -8.35332 | -45.6362 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac3dabc0-32c6-387c-b8d3-303532f52948 | -6.44346 | -43.81477 | 2025-07-13 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e85212f-a052-3b35-b08d-9c7b8904645f | -5.26581 | -44.86872 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d7ec20ab-9832-3550-82c2-ba7d46065f4e | -4.28882 | -48.06067 | 2025-07-13 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 998ce2a4-fa25-38ac-b6dc-3476994bca3a | -7.15122 | -42.28928 | 2025-07-13 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c26f83cd-7479-3bc4-9e75-e061bc395205 | -6.78027 | -43.96761 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89684257-df06-33e4-91bd-97c1506c4fcf | -6.10784 | -45.87278 | 2025-07-13 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0140256-6bef-3715-be46-30956c87b477 | -5.73722 | -44.9853 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 5aca43cc-1612-3969-a0b9-b23530d83c6c | -6.14854 | -44.09482 | 2025-07-13 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 323526cc-60d6-388c-bc7f-44b2b5649e01 | -5.62864 | -44.26524 | 2025-07-13 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 499284bb-ba32-3707-b720-a6a4cc85f644 | -6.33762 | -46.1791 | 2025-07-13 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 847af578-92dd-3784-88f7-750ad6681d4b | -4.53584 | -48.02063 | 2025-07-13 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a7360ea-8762-39cb-a32f-ae0afea32588 | -6.51662 | -43.36225 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34499d12-33c3-3d77-a2d7-d76069bc52eb | -5.73998 | -44.98928 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f0a897c-bfbb-38d1-bfcd-3846be622119 | -7.29104 | -45.31753 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdbb92a9-77df-3259-9d49-37682c87145b | -7.99037 | -43.38296 | 2025-07-13 04:19:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 866d130b-1c38-3c13-ad48-e42953067b34 | -6.62262 | -43.01517 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dffc9a44-3ef7-3e8b-bd33-5aa471bdc92d | -6.8665 | -42.76827 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cc1fe45f-8510-3094-8193-dfde95a46baf | -4.27952 | -48.18694 | 2025-07-13 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f4ff5bf-9d60-3aaf-976a-99535fb42ea7 | -7.29091 | -43.04641 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb70688a-e2aa-32b3-bbe1-75dcdaa8203c | -7.09947 | -44.07833 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a926eb8-749a-3b54-9eb5-e1e45a9cfac8 | -6.65959 | -43.02461 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0de3246e-3a8b-3d72-8376-32938944d264 | -7.11029 | -43.61106 | 2025-07-13 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 555f1e96-3417-3ee7-886f-a3fad2859c05 | -7.82327 | -44.78467 | 2025-07-13 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee3fdd4a-0b60-3fe0-a9a4-4ac1b7a779d1 | -6.7448 | -44.69957 | 2025-07-13 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee86861f-cab2-38d1-8423-3982d66857db | -7.30923 | -45.33103 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 596fd13c-e151-3d92-b728-020aeeee98d3 | -6.81953 | -43.35614 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e921614e-0aff-3884-86ae-c96f30dff531 | -7.28167 | -45.31251 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1008333f-16ea-394e-9f18-8dc26781a6bf | -6.78748 | -43.96513 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17dfd57f-61a2-3ae8-b648-4163b6f106ce | -6.44294 | -45.38796 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a6c8a8e-f5e1-3341-bcee-34f3437cc9c3 | -6.27069 | -43.41278 | 2025-07-13 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16a10049-1312-3473-af92-385cf91e19e5 | -7.31308 | -45.32809 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0be28e3a-be04-3ea7-b0f8-93c858877e70 | -8.3307 | -44.93282 | 2025-07-13 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8317e8f2-5113-3c54-941b-fac340966288 | -6.44076 | -45.40186 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7cebf49e-b282-3176-92c3-8212584a76eb | -7.11319 | -40.38705 | 2025-07-13 04:19:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b46daf19-3247-3020-9d60-cb431d991fcf | -6.65488 | -47.57983 | 2025-07-13 04:19:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46c06f15-d3c1-33f2-bb81-07ddb75d5a54 | -6.64026 | -39.32602 | 2025-07-13 04:19:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4a5b1cf8-5d58-3521-9fbc-c95180f8e4ca | -8.34782 | -45.64959 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50bfac0a-7b2a-3fcd-ad89-6a7646df9dc8 | -7.17724 | -43.01038 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a7847a1e-e5ef-3f64-be38-65537ea86b7f | -3.22237 | -42.13161 | 2025-07-13 04:19:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 543bb6f5-20a9-39f8-bddf-b1d44801a655 | -7.2265 | -44.00419 | 2025-07-13 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0d6646e-4464-3202-9e9b-f9204ed0aa2e | -6.95338 | -42.731 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 00d50c38-b0ee-3c28-9b21-79f3cc0a7908 | -7.1778 | -43.00667 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e0f1d95b-6126-3074-b3c8-4ed1aa4a59c3 | -4.86114 | -43.22652 | 2025-07-13 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dca2e6a4-0de7-3db1-a7ab-c9c14da2fb03 | -7.29597 | -45.30766 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 998d9a17-d48a-3745-a132-e23ec7b8d44a | -8.34558 | -45.62074 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98b25f32-bfd9-3aaf-8cc6-4c017b40ad3d | -6.6563 | -43.11471 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2eee69c-5d18-302c-8b25-7882989291c6 | -6.25723 | -44.83835 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2924a715-fd95-357c-8613-21b53fb1a517 | -6.12945 | -42.95991 | 2025-07-13 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 0577a221-9ade-39f0-a1a0-df91b079a4f0 | -3.62264 | -47.5447 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3e67a2af-2ebd-3ded-9d87-c888f2969957 | -8.35168 | -45.64661 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 52a3e632-ec8b-382a-88ae-4c45d74d1297 | -6.84072 | -42.87248 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b470e606-2ae3-3139-a73a-7ff0485453a7 | -6.83016 | -44.01838 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd433e5e-7e82-3d4b-81a1-35b2173947dd | -3.42117 | -43.37039 | 2025-07-13 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4a4f2cd-5ae9-37fd-9c7f-c269c9a544b8 | -6.52055 | -43.35918 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c992b13-455f-3b1a-91f9-4cfe18766d88 | -6.52502 | -43.35258 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3de30f87-6344-3aaf-85d9-b01ae444e2f4 | -6.94934 | -42.73431 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 197616eb-c7ed-3598-a5ff-ac9b551b4294 | -7.17601 | -42.97196 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ad964877-5fcf-35b4-861d-084b5c410f23 | -6.44181 | -45.37358 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19411043-a8ca-30b2-bf20-d561d6c660c9 | -9.16983 | -43.34465 | 2025-07-13 04:19:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a0c1359-5517-3c49-806a-c927da7d61bf | -6.96333 | -42.66582 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a9f4854e-9046-3f3d-a0f5-b5b88f86d573 | -5.78846 | -42.96513 | 2025-07-13 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9940807e-f349-3f54-b0f2-f662db174675 | -7.78402 | -44.02552 | 2025-07-13 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28040973-efac-3b73-8539-2a38826b5235 | -7.33917 | -44.00031 | 2025-07-13 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 577145fb-15fc-3cdc-8219-c9504b2c6c13 | -6.25709 | -43.3666 | 2025-07-13 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac8df77c-e39e-3e40-ae8f-e9b6e323a245 | -7.7879 | -44.02249 | 2025-07-13 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9276d42d-9529-334e-801b-d98cb9f117ab | -6.48705 | -45.26066 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fc383ca-3da6-31cb-85d1-b0fc731cb0b9 | -3.61901 | -47.54411 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 07335523-9787-306e-9833-8e24b5573b04 | -6.14522 | -44.09429 | 2025-07-13 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fc38a1a-3c9d-3c87-aaa0-bd52a885dd4e | -6.65743 | -43.1073 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b77313a4-ed16-3100-a437-4498a173a260 | -3.7522 | -47.10509 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2c66943-5a1a-376a-aaee-9b409b74c3de | -7.11235 | -40.39058 | 2025-07-13 04:19:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 41bed520-1efb-3c67-a097-b699152d1883 | -7.09649 | -44.07788 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README5.md)
