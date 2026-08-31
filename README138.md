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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47cf4d1f-46f0-3064-abf5-71ea7d8a0850 | -19.08343 | -57.41012 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 564ba2ee-5693-3bad-ba38-605d3560d30e | -13.51472 | -43.5154 | 2026-08-31 16:48:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3bf0f8d0-031e-3130-8db6-dd53ee209586 | -17.29831 | -46.95269 | 2026-08-31 16:48:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 09d07dbe-51dc-34fb-b4c9-16a4e6cd4613 | -16.55464 | -52.51332 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 33aaf903-c2b3-314e-89db-26c098325feb | -17.89794 | -52.08823 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 116.0 |
| d0cfc4a7-ff0c-355d-ba8a-a59cc89e1c30 | -19.22987 | -57.33755 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.7 |
| e77424e4-4345-362c-a0ac-bd805fa59eb9 | -19.55535 | -48.273 | 2026-08-31 16:48:00 | NOAA-20 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f96bbaf6-089c-3fe7-b8b5-6b31e308c3da | -14.82489 | -55.73721 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d4cc6503-6f82-3427-aa0c-5315aa4fe44d | -16.01396 | -54.40436 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d7f0d5ff-aaf2-3443-be35-2604c1e0ecb2 | -16.46285 | -41.81755 | 2026-08-31 16:48:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| fe65460b-de7f-3369-9528-0c66ddae1507 | -19.12462 | -57.36656 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.9 |
| a2c61dfa-537d-3f3b-b43b-077e483dd123 | -14.22826 | -51.94206 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 0a975eff-d397-34a7-a106-9f1090f380c4 | -15.5358 | -45.91529 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 57a858df-ac4a-3b24-b30a-b99f1b80658a | -19.11314 | -57.37233 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 962340fb-cd1d-34b7-b735-9aa656ac9bd7 | -15.63901 | -56.37971 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b90a6183-0ac8-3942-9ad6-fff7733b7f72 | -15.46176 | -53.96028 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 215f3a94-09a5-303e-9ab9-b39eb50f7fa4 | -15.34918 | -53.80288 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 70d7d07b-3581-3e8d-84a1-9fd29889410d | -14.99363 | -48.13656 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 17dccc9f-e36e-3cdc-8c84-cd37b58435b3 | -17.89579 | -52.10438 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b5dc6a9e-7936-3e6e-9a8d-c8d47e66c009 | -19.14031 | -57.37687 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.2 |
| 98b1fb1a-299e-3f9f-a34e-39e88ff98d2e | -14.79296 | -48.75121 | 2026-08-31 16:48:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f6b90adb-6656-3f18-b507-0d0d7345b509 | -19.22393 | -57.33815 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.7 |
| a9a6bb45-e503-32be-ab1a-47b6d20f101e | -19.15815 | -57.40434 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 1654c2ca-604d-3e00-a404-e8feadda8dac | -18.2679 | -52.71159 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 63d6b86f-3df7-3845-b5d5-aa2f9a3206ea | -15.09923 | -41.37572 | 2026-08-31 16:48:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 8dd61bf3-2573-34dc-9d19-e12413722c9d | -17.86197 | -50.49781 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 269.3 |
| 9995b65e-0337-30de-86c2-02685f664b15 | -16.5649 | -52.51687 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4a095a48-966c-3298-aee5-ac1598666ed8 | -15.23406 | -56.38877 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9046c2e8-d32c-3131-9489-c58fd04d301c | -18.68905 | -48.22464 | 2026-08-31 16:48:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 870f003d-74be-3126-88f1-081b9c648929 | -19.17176 | -57.35715 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.1 |
| d3f14dc0-9ae0-3222-833e-8e3c9ea03856 | -16.07965 | -41.44912 | 2026-08-31 16:48:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b3d58884-fceb-3fa5-9890-124fc453c9a5 | -14.56927 | -53.60252 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a5c40c7e-1766-306d-8aa2-6aa4a8b525ec | -19.13902 | -57.39256 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 56a8cbb6-e264-3b5a-9f79-769a9a470ecb | -18.29939 | -45.09051 | 2026-08-31 16:48:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 06ceef1e-67c8-3d83-962d-522c99b784e1 | -16.02879 | -54.40837 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 050fc821-b3ac-32b4-8f3b-71d24da1b99b | -15.97796 | -55.95158 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 25.0 |
| 58333c85-8810-3b0b-be56-12071582a5de | -16.86672 | -48.27727 | 2026-08-31 16:48:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| acdef3a2-5870-359a-9ab4-e7b5cad4f2f9 | -16.35826 | -51.00967 | 2026-08-31 16:48:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 044a705e-082d-3165-9a8b-032dc3367500 | -14.58343 | -54.10321 | 2026-08-31 16:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5b9127e0-8eb9-34ac-b035-f27a1db42f2f | -18.55334 | -46.32878 | 2026-08-31 16:48:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 261b8a00-0aee-385d-991a-8bcef7da6daa | -14.418 | -53.15165 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 064e3759-b4f5-3180-ac6e-c81b3c5e5b9f | -19.17007 | -57.40311 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 30264031-f0d4-33f6-afb3-590b3a2c189e | -19.10418 | -57.3759 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| 4d930253-b952-3c6e-bbb0-1909b002e54a | -19.19088 | -57.36889 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.4 |
| b4c03236-9ba9-3410-b9c2-e65c0c320bf9 | -15.99781 | -43.55484 | 2026-08-31 16:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cb6dbe90-3f73-3ebf-a620-0ba62fba3c84 | -16.56349 | -52.51603 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 37b20ae4-75fc-38c8-8816-24d0c9945505 | -16.55831 | -52.50884 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cebf7fa6-c60b-3aec-aef2-448ad8d281db | -16.85064 | -43.2939 | 2026-08-31 16:48:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0947cf9a-c5d6-3aab-a37e-bddc15d0a73c | -19.11396 | -57.3814 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 8fd0db07-2f08-3359-9d1f-c81ae6e5b5e2 | -18.80545 | -44.98526 | 2026-08-31 16:48:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f55ae440-a754-3f3f-b5d6-6d2272b2e216 | -15.64261 | -56.38248 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8317fda4-7e21-380c-8453-cc80bef35b73 | -17.86065 | -52.09301 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 689d349e-fe20-3447-85fb-2ebabefd29df | -18.27061 | -40.55387 | 2026-08-31 16:48:00 | NOAA-20 | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| d02d3882-860b-3eee-bffe-27354ecd57c6 | -19.18752 | -57.39674 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| dd4504fe-394a-3d2e-ab14-5e93018446fd | -16.75265 | -39.97288 | 2026-08-31 16:48:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f02d187e-c462-355c-91f6-d424af8afc2c | -15.82696 | -42.6117 | 2026-08-31 16:48:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 603a926e-b9f2-3e93-9fee-6551fc00a8d4 | -14.69666 | -53.58622 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 13c72eda-ffb4-3be1-9dab-92adbebacce6 | -19.18493 | -57.3695 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| e7da4ff6-b899-3033-bdf1-e5048f6321b0 | -16.99662 | -51.83899 | 2026-08-31 16:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 33.0 |
| b24133fc-e856-3f3a-ae90-bd1814d32d33 | -17.95027 | -44.57474 | 2026-08-31 16:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 594464d2-f166-30eb-8bab-359e81e66bf0 | -13.41451 | -40.96213 | 2026-08-31 16:48:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 3daa8d40-0440-32db-8b8f-b99d09350767 | -17.17559 | -44.42829 | 2026-08-31 16:48:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0db2fe1c-4953-3471-b4af-96bff671644d | -17.59391 | -46.48852 | 2026-08-31 16:48:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 60b6ea54-098b-3ec7-8a2c-46ef5d88854f | -15.81026 | -48.36722 | 2026-08-31 16:48:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2f22f2a-4f20-3a34-b4d2-470ab0f06280 | -19.09447 | -57.39983 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a0eec508-1c57-32f6-9d3c-f39ffcb459d0 | -19.18199 | -57.4019 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| 9f32ff63-1321-34e7-9e67-74d9b078607f | -15.49539 | -56.01172 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 957d1c23-a8d4-3544-bda5-12f808bb1415 | -19.47467 | -57.55946 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 84f98953-f8fe-3246-aa05-3bcac8535507 | -17.86029 | -52.70914 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54ef08ec-4458-3e0c-89a9-541d84766a83 | -15.73959 | -56.1021 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f2e46e3b-70a8-3a9b-a56c-4242d8de6b02 | -15.66926 | -45.94132 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a5600895-9b1d-3347-8adc-ad8a9c53f76f | -17.85445 | -50.49892 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 296.1 |
| 39809e28-9ab0-3433-b811-01ea59662130 | -14.85533 | -42.07003 | 2026-08-31 16:48:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| faef5583-2ef4-320b-acc1-76080bb547a3 | -16.6974 | -49.8968 | 2026-08-31 16:48:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 2210779f-c29d-34a0-8a05-6810095cd815 | -16.58508 | -42.48459 | 2026-08-31 16:48:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0f21942b-465f-3f83-b67f-3eab7b6ff647 | -19.22235 | -57.34586 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.8 |
| a2b331b6-2bd1-3136-a6e9-62b1f423305d | -15.05853 | -48.3916 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 03f55db5-1dc4-3ef9-b110-20a88fe2f23b | -14.70541 | -53.58516 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 5d4cbbc5-1aa7-3b6d-bbcf-c4b0db1c1fc7 | -17.82497 | -44.45154 | 2026-08-31 16:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 84fbe0ed-e914-3b95-af6f-092aeb570c5d | -17.7963 | -44.44857 | 2026-08-31 16:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15821405-6497-3af0-a53d-44fbb6d1e119 | -15.65215 | -56.37067 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 327f2f22-2170-35ba-badf-38fe9e30d598 | -19.18242 | -57.40645 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 5906dedd-9d14-3320-9524-5e43de2c5cff | -16.51654 | -47.73132 | 2026-08-31 16:48:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6bab5d9d-dd80-32c3-b75f-9327ab211e12 | -19.20451 | -45.4702 | 2026-08-31 16:48:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ebb7bea0-4fd8-30cf-9c19-48a8e0b56cd6 | -14.52473 | -52.28155 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 026373e4-ed09-3c95-8553-625c0ee1730b | -15.97325 | -48.0465 | 2026-08-31 16:48:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0a2bb3b6-e473-3d31-804c-88e417ce9c1f | -16.99211 | -51.83587 | 2026-08-31 16:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 33.0 |
| a5c6923f-b34a-3a9a-ac25-f13e6dee7d19 | -18.83473 | -46.77708 | 2026-08-31 16:48:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ee9cd55-e324-3b3c-bef5-23500d59c414 | -18.10742 | -42.87457 | 2026-08-31 16:48:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 51ac751d-aece-3ac0-bb96-805ac2e468f1 | -15.61391 | -56.39701 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b15d7f64-d599-325a-8e15-f5bb9a3dd78c | -17.88869 | -52.08174 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1fa3996a-fc65-3f40-a044-1e9bc2d5d994 | -14.44919 | -53.1599 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 80e25853-f84e-3085-bfa7-768abbfb9ada | -18.26567 | -52.72941 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4c61e043-8943-34a6-8ff1-9497152a6501 | -15.98877 | -55.95355 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| e5d251db-a0ee-3d24-b1f7-9b1b781ba68c | -17.89332 | -52.08499 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| e8eff5a1-4071-369b-b326-5aff0ee4ff5a | -19.07747 | -57.41072 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| f1ec2c80-9a4d-31eb-9f7f-7f8868e0e3c4 | -15.60516 | -56.41542 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b79e0de4-6082-3cf5-8908-467264c58f80 | -15.02067 | -40.94746 | 2026-08-31 16:48:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 8261c292-afc5-3e91-bb0e-da71d8f7c782 | -19.1238 | -57.39223 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 13f054a0-fd3b-3359-a703-25f8c8baa4f0 | -15.68043 | -45.94693 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 78.5 |


[Clique aqui para ver as próximas entradas](README139.md)
