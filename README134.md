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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa0d0796-853b-338d-b3c0-8bca1a5b5e4c | -16.90728 | -42.10036 | 2026-09-28 17:07:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 895b7f2e-9b9d-3dea-aab4-227f7938b7d1 | -17.5613 | -42.52991 | 2026-09-28 17:07:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd2c1cf2-da51-3c4a-8487-bfffef1e2a40 | -20.83715 | -57.7 | 2026-09-28 17:07:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d1a4b57c-fbbd-34ae-83fb-9a5db52678fd | -11.3814 | -43.43252 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 88df76ed-a66f-31c2-9b5d-cbed12a6b293 | -11.60255 | -44.13493 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 172827bf-a927-3aed-ae52-5c7511f50b31 | -14.11703 | -43.9254 | 2026-09-28 17:07:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 52bf1cd5-9d2a-32e1-97ce-5874222641a4 | -12.69444 | -47.36305 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| d7600182-4ffb-3c60-b040-91a67add2fb9 | -15.15092 | -43.57966 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 07501c85-f63f-3eba-853b-894ee466732c | -13.40092 | -51.32046 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6dd67af6-8e00-3bb6-85bb-9873740410c5 | -12.95424 | -43.36595 | 2026-09-28 17:07:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 6ca34961-ed62-3e32-be4a-17f95df20209 | -13.8898 | -53.66437 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7c1b5803-254e-31e0-b69c-0d496df81ae5 | -12.09451 | -45.2321 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 49dd7ef7-dc6b-31d4-99ef-bb8429bd41b9 | -15.85486 | -42.43328 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0721376-c19f-3ce7-aecf-c6f4d4e9591c | -15.04112 | -49.58902 | 2026-09-28 17:07:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 9f9a2803-4d2f-327a-a235-e654b861073a | -13.81746 | -44.25744 | 2026-09-28 17:07:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 02adfdfa-c9c0-3d52-aa7d-a009ef883a5c | -13.48528 | -48.59914 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1c46c71-e198-3410-86f5-3b4881466fa3 | -18.10821 | -44.39457 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cc802f93-4a96-3658-9258-95cb1b592a30 | -13.51935 | -46.90424 | 2026-09-28 17:07:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 7c47f13c-ddbb-3da6-b37a-d11c5035b2b4 | -18.39616 | -42.54707 | 2026-09-28 17:07:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 170ba19d-0ea9-390c-b833-2f91c8797de0 | -11.37873 | -43.38749 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 5ed05046-73cf-3bde-a51d-40d89a09322e | -11.64609 | -43.27343 | 2026-09-28 17:07:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ca1580d6-be4c-3b65-a965-c8d28e63721b | -14.67358 | -40.06356 | 2026-09-28 17:07:00 | NOAA-21 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 002a5d12-8e1f-358e-8357-e7dfb467f93e | -11.26416 | -43.54076 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| f7b62650-3cfe-3bdb-b151-8d71a8178e4f | -17.99853 | -41.91995 | 2026-09-28 17:07:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| cd5f124d-3557-34b3-bc79-b9fad4e69456 | -15.19555 | -46.13796 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 78719ce9-35c2-36d5-8b29-816ac453f738 | -15.15262 | -43.60987 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.2 |
| f49f69f5-d58a-3a1b-8736-e99797f48004 | -24.73295 | -49.48872 | 2026-09-28 17:07:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 597a0919-db57-3aba-91e0-dfbff92f244e | -17.253 | -42.77756 | 2026-09-28 17:07:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7632168e-e753-3d3f-bdce-5b308449d91c | -14.52556 | -48.29942 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2f7ba4c8-8c09-34c0-9b6b-c75c45559a69 | -11.71362 | -44.534 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 35c78338-57d4-354f-95b5-aa7591e162ce | -14.32897 | -44.81601 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b6b6ee76-545d-328b-b9c8-f8951ffbdd38 | -14.73969 | -41.0518 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 85c52bc1-96da-3d27-93ba-8dafab4f49d2 | -11.38128 | -43.40058 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 7968143e-cffc-3b9a-81fd-b3fb394e5d57 | -11.36711 | -43.42182 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b61ebafe-0f17-3161-8a65-c83b7ec6c63b | -14.63376 | -52.11575 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d312ac9d-9f06-3741-87fb-55163a45585d | -14.00002 | -43.76421 | 2026-09-28 17:07:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d565e04b-40b8-3aa2-aa6f-689a66eabfca | -18.87729 | -46.6703 | 2026-09-28 17:07:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cc262cc4-6f08-3b86-8080-76f6045045d3 | -12.68477 | -47.36032 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1be1a0c9-f979-362e-a4e2-749d3238c39c | -17.67192 | -42.00823 | 2026-09-28 17:07:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| 810fb09b-caf4-3730-b7d9-232c30a73b65 | -16.90793 | -42.1036 | 2026-09-28 17:07:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 4d591f5a-cbf2-3679-a39c-4bf87e7d96bf | -12.43695 | -44.14486 | 2026-09-28 17:07:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e34ae231-85eb-3d04-ae15-3e82493dcc01 | -11.29588 | -43.54798 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 60b6fac0-81f8-3ffc-8b23-f24d55521a9a | -16.07236 | -41.75747 | 2026-09-28 17:07:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8a99e614-3585-3d5c-8be2-6dd22f6f3828 | -13.3268 | -43.9396 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ceec3ab4-2563-34d4-a5f4-a122875112e8 | -15.40318 | -47.90659 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6ee6895e-ba84-3df5-8084-7449c36feb61 | -13.96564 | -54.00733 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5671a0d6-e8eb-3086-a83c-1a6397c7a0ca | -11.717 | -44.52203 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 82914a3b-b77d-3d5c-8f4f-aa29105abbf6 | -11.90249 | -47.00637 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1c615fb1-e055-3f52-a5de-a949ca0933b2 | -17.21349 | -53.3348 | 2026-09-28 17:07:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90740c8e-ab57-3f6b-bd0a-9b0c9a54fe8d | -14.52118 | -42.18352 | 2026-09-28 17:07:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| f7073986-c538-32e5-87b8-80cd32f671d4 | -18.99398 | -48.17932 | 2026-09-28 17:07:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cded60f2-9f89-3133-a844-fc4244e0714d | -14.58955 | -41.23635 | 2026-09-28 17:07:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7d8ccfd3-4bb2-3f7b-9bb4-9865caa87bff | -16.64173 | -48.47379 | 2026-09-28 17:07:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ee8d3f11-de68-3c25-a962-ee864c471ce0 | -15.1239 | -40.98808 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 706719ba-037d-348a-8f20-cbbc30c13369 | -15.13712 | -43.6241 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.5 |
| d466f711-a253-3d32-bfdd-dbb7df2e6df1 | -15.19913 | -46.18296 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d9ea845d-ca44-3125-877d-e037c471a31f | -10.81464 | -41.33358 | 2026-09-28 17:07:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 92f1dcb3-6690-3e6c-b4fb-59dce1a8ce68 | -14.32775 | -44.80981 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cc11a0ea-c12d-30f7-b43a-3e6964557fc7 | -11.39396 | -43.43444 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 619c47f1-8d4f-3593-9ad9-5fc0582aef52 | -15.03818 | -49.59433 | 2026-09-28 17:07:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 78ff069f-aa6f-369f-a60a-2cd29db047f7 | -17.67294 | -42.0074 | 2026-09-28 17:07:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 38a55b74-edf1-3348-866f-2c3780722eb1 | -16.35198 | -42.56538 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8c7e4234-aa35-37c8-a387-9ba9c21ff200 | -13.17001 | -48.54726 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f3f6ecf9-6dd5-34c9-b20b-b638fc16d0da | -17.17812 | -47.42538 | 2026-09-28 17:07:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 0369cb74-5a4e-3aac-a26d-40386bdd2240 | -15.39566 | -47.91181 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bc437af5-7aed-3bc4-acc3-01fc799b2113 | -13.41742 | -41.57787 | 2026-09-28 17:07:00 | NOAA-21 | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7b5e41bf-10c0-3875-9690-8d74da03c49e | -17.17742 | -47.42149 | 2026-09-28 17:07:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 2c1e9941-e721-3b61-81fe-33c16d2aaf55 | -19.4071 | -48.44234 | 2026-09-28 17:07:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a45468a3-c3d5-366c-be04-adc50315d876 | -12.42988 | -44.16655 | 2026-09-28 17:07:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d398b8a6-a223-3fe2-8d91-dc39afbbac92 | -14.4681 | -45.23918 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 916fb8dc-f1d5-3050-893a-4aa0dbb7ff82 | -21.28656 | -57.90419 | 2026-09-28 17:07:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| a94b2d1d-fc5a-3bd4-87d8-a544a1007db6 | -12.68386 | -45.01906 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| b385d111-7be4-3872-b425-7f9741f4c540 | -13.70863 | -48.82686 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ab048184-4e4e-3ef1-a0e6-f8c6d9c41eac | -12.73063 | -50.6867 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 450a0ecf-7198-31ba-a8e3-3882c7d300ee | -13.47412 | -48.63401 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aa5f1bfa-8489-305d-9b7c-4087e8ed39ce | -17.32401 | -53.96373 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4ee8d9c8-6431-37f5-9613-ee78d41242d9 | -14.22204 | -51.98254 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 016028ed-ea66-3646-a188-c31f96bb7a34 | -15.15952 | -43.61594 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 019e50ce-9312-3453-9cd9-f6b819bf7b86 | -13.45519 | -48.59689 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c9b9eb0c-ce4a-3ba6-9da1-eca425199b54 | -16.29155 | -40.19732 | 2026-09-28 17:07:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 38ccb148-ab3f-3e92-a8d0-085d51ca4366 | -12.70378 | -47.33809 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d11e20bd-ac8d-3656-b7f8-4767990e07f6 | -13.58862 | -51.4513 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 7072dd99-dbd5-3a13-ad6f-33d465326352 | -14.10093 | -40.71737 | 2026-09-28 17:07:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 5dec4f4e-86c5-3488-b0b3-1f096d3c69c2 | -11.63412 | -43.49607 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 402d7da0-e153-3dc7-9c67-b68d5240a181 | -16.0636 | -47.92091 | 2026-09-28 17:07:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e2b52bab-2105-36fc-b877-15ce1d783b8d | -13.71261 | -48.82622 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 386d1105-9128-3f84-9ddf-599d08a7e8e6 | -15.16654 | -39.81991 | 2026-09-28 17:07:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 6790ce95-5938-32a0-8f70-13ae009a2808 | -15.5531 | -50.15244 | 2026-09-28 17:07:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2ee80f9b-87a9-3cc3-83b8-37dbacae68be | -15.47874 | -46.13436 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ab60fb15-eefa-31cb-9874-751be553e898 | -17.21112 | -44.81818 | 2026-09-28 17:07:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e4080836-70ee-3d36-9154-d686838ebe4d | -12.95515 | -43.36507 | 2026-09-28 17:07:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a4bc5f07-e726-39ae-959e-fd1c84d8658a | -13.14835 | -48.54381 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d58137b6-17eb-33c5-81cb-226f9f0aafa9 | -14.10844 | -46.29766 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 49e9afbe-6e23-3d96-96a5-dfe32aa4233f | -14.88186 | -40.31394 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 10772d7c-e404-3504-98b9-2729ede23ed8 | -12.39696 | -39.95746 | 2026-09-28 17:07:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 189b4123-2b81-3866-b9d9-f3ca0c41b105 | -14.31967 | -44.80946 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 18c29169-bd47-36b2-8190-e4e8996ab11c | -14.89477 | -42.57059 | 2026-09-28 17:07:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ef61dd2f-3690-3001-9005-2a455e56a224 | -15.08065 | -41.20098 | 2026-09-28 17:07:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1b66b8cb-6616-3100-b2d0-e781a0379e1c | -17.67729 | -44.74975 | 2026-09-28 17:07:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 47efd442-fd56-3399-af13-1e5b945d622e | -16.98266 | -41.94572 | 2026-09-28 17:07:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |


[Clique aqui para ver as próximas entradas](README135.md)
