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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a0e2072-8501-3e9d-85f6-e396a99540a1 | -7.28589 | -44.61621 | 2025-07-09 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c575cfe4-af22-3c6e-8b2e-f23c7ceffc8f | -7.6445 | -45.35703 | 2025-07-09 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01795daa-b7af-319b-9d8a-f09ade240296 | -12.05657 | -43.51403 | 2025-07-09 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5232b3d2-58bf-386f-aa1c-42adcd790d9f | -8.22088 | -44.93756 | 2025-07-09 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ddd6a2a-ad15-39bf-8510-c31b478edfa6 | -11.67532 | -43.77998 | 2025-07-09 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3f764864-6b5e-37a1-ba1e-1e8a98a55271 | -13.45468 | -40.3166 | 2025-07-09 03:55:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 580b4fed-f5f4-3473-bade-ae0107fc91c3 | -11.43352 | -45.12614 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a8fbc40f-af4f-37c0-ba1f-3b182bb5b0e4 | -5.49966 | -45.49054 | 2025-07-09 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dff3554-b47a-3103-8678-9387061004e0 | -11.44218 | -45.10054 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0c5f80fd-ff62-3555-8312-b505157e593b | -11.44283 | -45.09679 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 11a90bcc-d3c2-3495-bc76-7ea954cfae72 | -6.39187 | -43.03731 | 2025-07-09 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03d5cdaf-0598-3b3d-b1fc-c4dc7fcb2457 | -7.95624 | -49.64793 | 2025-07-09 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d679609-41bc-35ea-9b2e-8a36a93546c6 | -11.4478 | -45.11705 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e173123-3af5-3893-bb47-9305246c6001 | -8.50836 | -43.27898 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| c4237136-e6e3-36b5-ba64-33fad30d30ea | -7.24464 | -43.07253 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ea49e52b-8655-39b9-9dc3-5c3367ba6263 | -8.50859 | -43.28638 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 26882b0a-6886-3b82-9780-bd565fc3dd8b | -11.43137 | -45.1141 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 25dbd962-e742-3fdf-9c77-a86c50949c36 | -7.54444 | -45.66333 | 2025-07-09 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4912807-aeb0-3726-9c8c-c91fe5e09afb | -11.46867 | -47.92484 | 2025-07-09 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e392663a-70c3-3728-adb4-4a41c6b15161 | -7.09235 | -49.16812 | 2025-07-09 03:55:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 800b23ba-4c69-3f34-b64b-3ef4f6e958d7 | -7.83579 | -44.19547 | 2025-07-09 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85fc93aa-074e-3430-8da9-afd4a10f7862 | -8.27512 | -42.28019 | 2025-07-09 03:55:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4b79cb9e-cc37-3f71-98f8-5f8c8f566194 | -6.53756 | -42.27701 | 2025-07-09 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0087fb27-0c83-3dcd-b741-8f30a093c5ec | -12.38836 | -40.30393 | 2025-07-09 03:55:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| b842253f-2f91-3624-8f7d-b1c9a690853b | -6.13079 | -42.9572 | 2025-07-09 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7393ba01-c0ca-39a7-839e-4bdaff8555be | -5.78578 | -43.60856 | 2025-07-09 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de208f62-fb66-3911-98fe-ba723972ecf9 | -5.59062 | -45.33973 | 2025-07-09 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f5f3179-91d1-37d2-b9a6-18383d7b6521 | -7.09312 | -49.16389 | 2025-07-09 03:55:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f2deeb9-5226-33dd-9236-d6561c4ed1e0 | -5.58683 | -45.33424 | 2025-07-09 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9eded8b7-d458-3d25-b10d-313bff2fa4c3 | -9.79118 | -47.74781 | 2025-07-09 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56dfc6cd-5a3c-3533-a785-987b356d312c | -10.57489 | -49.11992 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 28dc3907-c358-3cd1-ad44-995d275b4291 | -7.2485 | -43.07316 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0caf6f76-456d-3927-bc19-fa4038c045a2 | -7.32198 | -43.87317 | 2025-07-09 03:55:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 735daecf-dad8-3833-b71c-2e3c81da465f | -11.42792 | -45.1096 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| fe32cc4c-b1b7-383d-ab7b-861aaea49e06 | -11.10853 | -48.86912 | 2025-07-09 03:55:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 711477d0-2c89-3bd3-aed6-f8cc7d890d71 | -11.43743 | -45.10357 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eb65afed-dfd9-322d-a950-b41a28dbe4eb | -11.43398 | -45.09907 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 633d254a-8027-3035-8ec4-cb6731b34a8b | -11.43332 | -45.10283 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| da63c4bd-ac20-35b5-9af6-a1cd3592426b | -11.46103 | -45.10743 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1ddd6efa-1cb6-3e92-b62d-fb07403e786d | -10.65158 | -44.49103 | 2025-07-09 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0f083c2d-fc00-3fdc-b8c2-b04f01af686d | -11.43463 | -45.09532 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31606062-37a0-388a-b1b4-5fb45dfe60c7 | -11.43873 | -45.09606 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 63b5aeb3-3e63-3fc3-a496-3470a3167a21 | -6.85107 | -42.80077 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f303e845-e4a6-31ae-affa-8a5b658dd518 | -8.2831 | -42.27707 | 2025-07-09 03:55:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 503ce9c8-fb38-3675-9e4f-ae08b7ffb7e5 | -11.51052 | -48.95622 | 2025-07-09 03:55:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a35f5074-527f-3da8-b006-2ec09cd7d893 | -6.68219 | -46.30098 | 2025-07-09 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84322283-ff9f-362e-b9f5-389176a4c7e6 | -10.64879 | -44.48333 | 2025-07-09 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76963cbb-32ea-3d0c-89a7-92604207ad8c | -11.67454 | -43.78466 | 2025-07-09 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9e2841f8-d56b-35f5-a65e-86ba0dc58b38 | -7.03325 | -43.32191 | 2025-07-09 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f54dd419-e649-3a49-8add-9b457b6e5ba4 | -5.78519 | -43.61213 | 2025-07-09 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d92d46a-a764-39e3-9aed-ce31a3582d39 | -5.96371 | -44.18467 | 2025-07-09 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dc1a7bd-9347-3c51-8212-8c63b782e28d | -5.96506 | -44.1768 | 2025-07-09 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe5edb2d-fd75-3c91-831b-02e016ee996a | -5.96475 | -44.17764 | 2025-07-09 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9112b88-66ee-3d37-8b04-995db0a6fb3e | -6.17348 | -48.05094 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 0f7f14ac-ebdc-3215-bf6d-8e0f953bd196 | -8.1777 | -46.51027 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44e34f6c-33b9-30a7-b9d8-2bad3b0fc559 | -6.95967 | -43.25509 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cbe40b56-5c48-318d-b67e-61426afb7197 | -8.51057 | -43.28913 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| da2f1bf4-573a-39ad-ac30-c4e12718437b | -6.67894 | -43.19942 | 2025-07-09 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8d7b953d-a067-38c3-8199-7a1ad13af9f7 | -10.5742 | -49.12359 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 087db7f6-63f3-3aa4-ba65-13b9f645ad32 | -12.98236 | -44.88824 | 2025-07-09 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 294ea21e-7115-3d8e-a7a9-aa629dabff1a | -7.66208 | -44.37499 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd8b8eaa-259e-3a45-8d56-a91249f0cfbb | -6.83431 | -43.35683 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9da9b024-2806-3a37-829d-dab53ef9070c | -9.22673 | -48.59571 | 2025-07-09 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f0583b21-bec2-3cc3-b66e-ee49ac3d3b0e | -8.69203 | -45.39944 | 2025-07-09 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bdfc2ee-f91c-365c-b4a3-75c4b9e7c4bc | -6.72096 | -43.71669 | 2025-07-09 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93d853fb-e2dc-3855-b028-dfa476bc9e7e | -11.67155 | -43.77932 | 2025-07-09 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7cd658d2-89cb-3fec-937e-da46107dc346 | -11.42249 | -45.11642 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d6e6be9-be7a-36cf-a449-b7335c0562eb | -13.38992 | -47.89273 | 2025-07-09 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 669e8d2d-af49-3d74-a323-379eb55b64d0 | -17.90097 | -43.9954 | 2025-07-09 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57c21ba7-6262-325a-8528-237764af8bbc | -16.62984 | -42.21355 | 2025-07-09 03:57:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6c33894d-1fe4-3f38-a09b-50afd1879d3f | -20.21869 | -44.47728 | 2025-07-09 03:57:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c089f572-2d49-336f-9cee-e40254522ab6 | -19.64708 | -49.51168 | 2025-07-09 03:57:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fcc0730c-1251-3783-b81b-93c70a6f9c53 | -18.40125 | -44.19498 | 2025-07-09 03:57:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5669c03e-674a-3994-b435-94184ae5dff5 | -13.38613 | -47.88663 | 2025-07-09 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bebc4a9d-3308-3088-9084-f56c4635ff04 | -15.78936 | -48.25113 | 2025-07-09 03:57:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1981da83-7a9e-382d-aa7b-6c0a7924d5ce | -14.85785 | -45.1263 | 2025-07-09 03:57:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a75131d5-b532-318c-9af8-2da7612f77a5 | -19.73869 | -47.44208 | 2025-07-09 03:57:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b73b4a4-1b50-3432-b277-beed611bac8f | -13.02094 | -46.28796 | 2025-07-09 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f88d86c-5e1d-375e-bc10-207addbce6b6 | -17.69311 | -46.7482 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e608469d-c926-3d87-9508-feb53149db87 | -14.79075 | -40.68669 | 2025-07-09 03:57:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ff41acc1-0c40-3919-ad99-ae2bb8e0b9a6 | -17.69041 | -46.7397 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 873b2860-ff02-3ce2-9813-96d74e351343 | -15.88497 | -42.19921 | 2025-07-09 03:57:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b7fb4091-4287-37a4-9b80-f457fcc32f57 | -13.01334 | -46.75581 | 2025-07-09 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30798306-3a4c-3635-ba41-d30787f5398d | -20.41861 | -45.58262 | 2025-07-09 03:57:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91390a8c-d7f4-3b4d-a23f-f9c08f3af47b | -18.649 | -55.72585 | 2025-07-09 03:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| e365f53f-42f5-393c-a3e0-f06f35a2f01c | -15.78612 | -48.25361 | 2025-07-09 03:57:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c22ef66-df92-3072-843f-a1ba75d50679 | -15.19658 | -44.05929 | 2025-07-09 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d546196-373d-3827-afc1-8a7216235417 | -13.63953 | -44.41642 | 2025-07-09 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ec580b1-7ff2-3104-be2a-3738faf1e07c | -17.75287 | -42.89495 | 2025-07-09 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36362bcc-3ef3-3cee-8ea1-39279fa55c43 | -13.70454 | -45.61623 | 2025-07-09 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36f728b2-d109-3e45-bff7-74e47bb2ee22 | -13.01248 | -46.75084 | 2025-07-09 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75a049fa-e594-35cd-b2d5-e6647f872472 | -18.40904 | -44.19212 | 2025-07-09 03:57:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fce7e13b-c64c-3d0b-9851-8216bb7768fa | -14.94803 | -42.35567 | 2025-07-09 03:57:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7d6f8327-adc9-3a37-8de4-37cf43927887 | -15.92502 | -43.51616 | 2025-07-09 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa333d69-14db-3302-b020-33aed0b45896 | -17.78095 | -42.80973 | 2025-07-09 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bc87871-d426-3713-a73a-b9358ca9e50b | -12.97632 | -47.83163 | 2025-07-09 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf920048-4a5c-3363-87b1-eb17373526b4 | -15.61781 | -46.4627 | 2025-07-09 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9ebe9c0-5ce2-3998-93bd-f560b636086f | -19.36698 | -51.40117 | 2025-07-09 03:57:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 804a4f81-30bd-32b2-b3de-b918d1fe037c | -14.62359 | -40.47295 | 2025-07-09 03:57:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a98c9d78-8891-33f7-89fa-0b3ee8257a2e | -18.64045 | -55.73094 | 2025-07-09 03:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |


[Clique aqui para ver as próximas entradas](README11.md)
