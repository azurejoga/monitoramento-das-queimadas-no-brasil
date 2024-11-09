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
| 6ca6af91-ff33-388a-bb73-876c07ef0a73 | -4.8692 | -45.67682 | 2024-11-09 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8120516-4232-346a-a2b9-bc884e2bfcfd | -2.22083 | -46.54976 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 09bb4b89-7279-30f6-942c-82b5490fcc29 | -3.54595 | -43.56559 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 17d35ed9-6613-371d-b765-7aa3bb78d724 | -5.10762 | -47.14148 | 2024-11-09 03:40:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cafb6b3-8a99-309c-924f-35f93de618b3 | -7.11222 | -35.01629 | 2024-11-09 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3753ef53-d27e-3d29-a6bf-455e61a93481 | -2.31118 | -46.48875 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cd21758-fbd0-3aa4-95c0-f3c6d39e1c84 | -2.44517 | -46.32312 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 946f06bb-2c50-3f2e-945b-ca3ef40f2368 | -3.58857 | -47.35685 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| cbf2bf8c-044d-3be0-ab21-5dc059b127d3 | -4.05429 | -46.94518 | 2024-11-09 03:40:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2b90aa8e-5d61-387b-9aca-4da9ab017d01 | -6.59151 | -39.60835 | 2024-11-09 03:40:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4c2efc92-c4ac-34c0-8e6d-c359763e29ba | -4.23573 | -47.5657 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dcd29931-2eb3-30d6-80f7-99deeaef56ec | -2.42299 | -46.30411 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5ce27785-1c03-3486-960f-a0778f66bd12 | -4.73025 | -43.25188 | 2024-11-09 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c42722a9-49ca-33c4-b23d-154c982c8248 | -3.58752 | -47.36292 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8b6762eb-bca3-3df3-bfe1-605a97b4b782 | -2.23296 | -46.55749 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6dc862f4-0aa0-3df7-8a2b-1b73bda9ba38 | -5.44169 | -43.2691 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0fbc5560-6a10-3aba-9dd9-9eb1c7cd1ce1 | -6.22645 | -47.2813 | 2024-11-09 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0edd44ee-e486-310f-bbda-b7681dde935e | -4.82214 | -47.3246 | 2024-11-09 03:40:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 647d95ff-53e1-3503-8ac9-38adfa7e23d7 | -5.93016 | -43.65401 | 2024-11-09 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce241dd9-152b-325d-adc3-0988040a62f1 | -6.49568 | -39.55615 | 2024-11-09 03:40:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f946ecfd-69ef-3b4b-8f68-e4ced91587fe | -5.44689 | -44.82391 | 2024-11-09 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4e95f4e7-77e5-3333-8251-ca24ef8f5d7a | -6.18595 | -45.45078 | 2024-11-09 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cfa84e9-7f95-32a4-a48b-54154fad1990 | -2.08477 | -46.53059 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5abe23a4-ebd2-3fbb-bf5a-382e26fb3b31 | -3.55436 | -43.5807 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e6e37fc-4d6d-3daf-81fe-91cfe0994bb9 | -3.26671 | -46.31938 | 2024-11-09 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e75b780-bba6-339e-b0a2-3d8673cd2824 | -6.23092 | -47.29296 | 2024-11-09 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f93e0813-64d7-3d5e-8c42-4a795e2c7d62 | -7.23979 | -38.92579 | 2024-11-09 03:40:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 71a620e2-c5f1-3cd2-90cb-0db7e66f9713 | -5.59182 | -37.86598 | 2024-11-09 03:40:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f781d560-65b2-3d5a-ad0a-7d0627f74c82 | -3.55545 | -43.57401 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1cc670f5-b182-3347-9db1-68e750be817a | -5.84962 | -44.08173 | 2024-11-09 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e531e91f-e777-3dd4-a5bb-bd5984f09ded | -4.60742 | -45.98619 | 2024-11-09 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d0baa0d-e61e-3b2b-872f-e32f01ed2825 | -3.96812 | -48.18667 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| eebbc418-2896-36a2-b8f7-018ad52b35b3 | -2.97253 | -47.92521 | 2024-11-09 03:40:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dda0796f-13b6-3571-93ef-9d13ff8e1d43 | -5.11543 | -37.56474 | 2024-11-09 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9b986035-cce0-3b56-b61a-d26c29e5bd94 | -3.24729 | -46.48053 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8b07cb8-b1c0-3f23-b3e4-9d2a21477cd4 | -4.98676 | -44.17653 | 2024-11-09 03:40:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17b8f359-615f-3067-9c07-eadd058f6d1c | -5.43917 | -43.25631 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cea6b780-5ef8-3c9b-afb0-fa2b182328a4 | -3.59519 | -47.35859 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 8c0cf387-9ce5-3417-8618-a784c17ba605 | -5.99277 | -38.98797 | 2024-11-09 03:40:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f3def28-e7af-38ca-968e-3df24f5dab15 | -1.8194 | -46.11689 | 2024-11-09 03:40:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7152bba-02b5-390b-818a-82d4fe5c7282 | -2.36358 | -46.8618 | 2024-11-09 03:40:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ac8876a5-aa03-3dc3-8e9a-d159918977d6 | -5.14219 | -46.20879 | 2024-11-09 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49206bd2-600a-3822-b6cb-5f4e113f452e | -2.09127 | -46.53194 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcae9d97-1a2d-3400-b0ed-6d8e533c8514 | -3.55017 | -43.57303 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e57ca6fd-d223-3684-a532-444c75149301 | -8.33758 | -35.15266 | 2024-11-09 03:40:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d8726537-1eb2-36c3-91c4-a1f280018924 | -2.45245 | -46.31902 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83d1b642-2453-3fa3-a953-6c7c52debc51 | -6.23191 | -47.2876 | 2024-11-09 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77ceaaef-7a6e-3689-8e8a-30e75080be8a | -2.99993 | -40.23084 | 2024-11-09 03:40:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 532a6669-a612-31ca-b614-26249221af1b | -4.0337 | -47.14598 | 2024-11-09 03:40:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56b06bb6-f28d-32e9-8d05-93db02f6c685 | -4.12294 | -43.59069 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0766c0c8-7696-3b7d-b6bf-bacec2eb768e | -2.23113 | -46.5684 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 489d9558-e307-366e-8985-6da3e3edd04e | -6.20383 | -42.07873 | 2024-11-09 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f82326e5-3dd8-3fc3-be31-e1c4c2ecccd2 | -3.54908 | -43.57971 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b66e83ad-ec96-3711-a6e8-d61a69f37f61 | -5.44271 | -43.26326 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 233b91ea-0e98-3867-b7fb-b350b9747dec | -3.58294 | -47.34947 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f18fcf4c-0cff-390d-851d-15bb42d9b019 | -5.58302 | -41.69216 | 2024-11-09 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 30ed348a-13c0-3c27-b25d-e3426a7c3884 | -6.23234 | -47.27953 | 2024-11-09 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43f9cb74-0a71-3223-9fa0-0bc1af308898 | -5.19136 | -44.92321 | 2024-11-09 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1038f34-3e27-3656-956a-d854b867abe5 | -3.9611 | -48.18553 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| de1862b1-c71d-39ea-af77-c8e011a7abce | -1.50422 | -47.1818 | 2024-11-09 03:40:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d66d5cd6-6557-3545-837b-ec727220c0c7 | -5.65353 | -42.72998 | 2024-11-09 03:40:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b22939df-ff07-3ff8-b7b7-3f4a4cf277eb | -3.55008 | -43.56644 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 67259dca-811f-3ab3-94d9-5f4d1b8d8c04 | -4.01867 | -46.18476 | 2024-11-09 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0839b5f-6ce5-34af-849d-309991a655d2 | -5.62627 | -44.83249 | 2024-11-09 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c051445-7ead-32b0-8aed-34f8614b8e81 | -5.44623 | -43.27275 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 76b75fd1-fdbf-364a-adba-5dede2ae75c4 | -3.91302 | -46.45661 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5162e12-7e66-3b4f-aff5-2a25b1b4b962 | -6.12533 | -43.42281 | 2024-11-09 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ce45822-177c-3d21-9720-14d65029ca47 | -7.01045 | -45.62094 | 2024-11-09 03:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93358e7d-c29f-3199-8abe-09ee63d520eb | -6.29951 | -35.06491 | 2024-11-09 03:40:00 | NOAA-20 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| fccd3abd-251e-32b3-92b7-ce0301737636 | -5.03673 | -45.87604 | 2024-11-09 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bca79038-b234-3dbe-ba64-b0f9f2350eac | -8.64998 | -40.28842 | 2024-11-09 03:40:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a32d3a95-1f44-3067-a2fb-55e4879ae116 | -6.54254 | -39.44137 | 2024-11-09 03:40:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| c0cb6b29-adc0-373f-b63e-5cb6a36cc052 | -2.31211 | -46.4833 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9178fb6e-3a35-37f7-b27e-59a58a7f2453 | -5.44674 | -43.26985 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f4ee8152-45f7-3e89-9e66-29b11291ecb7 | -4.24393 | -47.58335 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| fb7c2a1f-86cb-3d59-907b-4ac3d8874d77 | -4.14937 | -44.40121 | 2024-11-09 03:40:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 981ca06a-7989-3550-8d5a-bdb526481c72 | -3.9739 | -48.19482 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| e678dbb4-b305-3ebf-9478-16806b303e00 | -4.20688 | -45.86034 | 2024-11-09 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b44348f6-56e3-32ad-9e95-f66b2de7510c | -6.23387 | -47.27707 | 2024-11-09 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66ec531e-2c47-3566-8df7-5d4b0143ef33 | -4.24601 | -47.58577 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| fc11436c-7fe9-33a3-bbb6-24d8f8021f4d | -3.54489 | -43.57209 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bbc1e50-c153-3d0c-b253-deb2bd232202 | -4.19776 | -46.69867 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e950c447-e5c8-3d4f-81d7-d33a442ed50c | -3.90666 | -46.45571 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 510d0bb4-ba96-3117-9ff4-0acd0bb4fb85 | -4.39633 | -47.652 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc2c6efc-19b1-3d43-9bdb-1b3509d63c1f | -5.69128 | -39.98498 | 2024-11-09 03:40:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 763480af-ca8a-3952-8569-4596aa14f8f7 | -4.82013 | -47.32525 | 2024-11-09 03:40:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08b7b61d-3c57-3ec8-9592-23ca477e529b | -7.11167 | -35.01975 | 2024-11-09 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 93484924-2d05-31fb-b7c4-784a7a33b747 | -5.7323 | -42.00101 | 2024-11-09 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7c5f296f-0781-31d3-a2d3-b97e6cc87c2d | -6.17459 | -42.03056 | 2024-11-09 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d07c05f7-9497-3f99-981e-9819e798df8e | -6.12985 | -42.56351 | 2024-11-09 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| f5002a24-8040-3324-a543-2f6cd3391d4d | -3.58191 | -47.35537 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1b4f757e-bc06-3c02-b271-6b2a920ca0c9 | -5.92962 | -43.65707 | 2024-11-09 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49cf7223-1d67-3b1a-949f-0205f9c1be96 | -4.88511 | -44.5975 | 2024-11-09 03:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e845c34-16b5-37f0-b8fe-f22bc75f4fbb | -5.17401 | -44.00231 | 2024-11-09 03:40:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f85c9dda-1906-3f63-ba69-73ca646ada09 | -5.46569 | -43.65776 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35a4c9a3-ae25-36bd-b661-899d28ae1ae0 | -4.23016 | -47.55814 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d4ece14-3819-33bc-af4a-6afbd6c83b2a | -5.46523 | -43.6508 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 72b619d4-12e0-328f-835e-106568ee59c6 | -2.09394 | -46.35241 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f49953b5-805c-380b-8296-54bf2a3dc437 | -5.43868 | -43.2593 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b42aadf-8ff6-3243-95eb-000c851aa6f3 | -2.36631 | -46.86896 | 2024-11-09 03:40:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |


[Clique aqui para ver as próximas entradas](README21.md)
