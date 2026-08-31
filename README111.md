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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15822ecd-ee1a-3ac5-807c-3d2186d506f3 | -15.58539 | -42.07817 | 2026-08-31 16:28:00 | NPP-375 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 375341aa-c46a-35c4-b79d-88140096e4b9 | -14.2732 | -40.02431 | 2026-08-31 16:28:00 | NPP-375 | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 77b6d5c0-15fe-3404-af67-c27bc50fe0a1 | -16.21602 | -43.02972 | 2026-08-31 16:28:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa4c7a33-d2e4-311e-a0ac-47532a1bbfff | -17.22013 | -39.29355 | 2026-08-31 16:28:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 178bd708-9979-3d87-b0d7-5e977cc3f941 | -14.62598 | -41.46181 | 2026-08-31 16:28:00 | NPP-375 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 0ce63465-394d-33dc-a660-641191b02cdd | -18.11975 | -51.61487 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cc6cd2e2-8af3-3ee1-bf75-d4e8918872ef | -17.72453 | -46.85382 | 2026-08-31 16:28:00 | NPP-375 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16a90b10-6756-39d8-ae79-6687029642a3 | -16.19526 | -49.31625 | 2026-08-31 16:28:00 | NPP-375 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7d4bca87-52d3-33a5-b039-9e46afed3afe | -18.12673 | -51.61678 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 60908a3b-da6c-3f1c-a7da-cfaf7ab3e09d | -17.85907 | -52.09199 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 4e64e6f2-51af-322f-a577-bc51d3362073 | -14.99243 | -48.13091 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e09b0794-047d-3fad-abab-095a4f112cc0 | -17.86296 | -50.51134 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 37.3 |
| f4cd8d6a-6239-30e7-abea-95678119099c | -16.38498 | -45.10977 | 2026-08-31 16:28:00 | NPP-375 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01658046-fbe5-346d-b11b-d3236e02ae88 | -17.8479 | -52.10874 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| aa830cf1-aec9-3899-8af2-debf593c2b05 | -15.64956 | -40.95832 | 2026-08-31 16:28:00 | NPP-375 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 72007235-889b-36fa-9b60-33e63285fd83 | -17.56525 | -44.72174 | 2026-08-31 16:28:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3d05d2b0-1b44-3446-a0d1-bdd013019db2 | -17.88019 | -52.11164 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 8e3758dd-5895-3f00-bab1-1f60e17d4e6b | -18.90665 | -50.88182 | 2026-08-31 16:28:00 | NPP-375 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 40ce4c4a-686a-3027-a3fb-44bad7ade06d | -20.4304 | -41.9843 | 2026-08-31 16:28:00 | NPP-375 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d818dc45-e605-3c55-add6-c432aa035cf1 | -15.65145 | -43.32516 | 2026-08-31 16:28:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 23edc776-f252-3e41-9a0a-9a4fb5d60e57 | -19.36754 | -40.18063 | 2026-08-31 16:28:00 | NPP-375 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 245dd017-eb8d-36d5-b924-1f81df4d7448 | -17.93903 | -42.79891 | 2026-08-31 16:28:00 | NPP-375 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9f3d82e1-b657-3619-9751-ed505d32bf9e | -14.08744 | -41.34663 | 2026-08-31 16:28:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d451432a-2969-36d3-bcda-e1bc136ff218 | -17.856 | -50.49994 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 3b60213b-7e77-3e5a-9ccc-8c8d9c829367 | -17.72907 | -44.28363 | 2026-08-31 16:28:00 | NPP-375 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bbc83639-efbc-3c2f-ae7c-202ca7858b43 | -17.50542 | -44.22533 | 2026-08-31 16:28:00 | NPP-375 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1211cf9c-0649-38af-a085-f56f96b719fb | -14.59215 | -41.28309 | 2026-08-31 16:28:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e3f79b88-5b10-376b-95c4-f5d95dd9a943 | -20.16251 | -42.17621 | 2026-08-31 16:28:00 | NPP-375 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 8dc83e08-207e-309a-a85f-f1db65f150e6 | -15.67094 | -45.92183 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 995b4da1-fcc6-3266-acc8-0f648b9dfbf0 | -17.83881 | -50.50217 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9447407b-c08c-31f3-b065-7e40b814c656 | -16.85862 | -48.27743 | 2026-08-31 16:28:00 | NPP-375 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a719a0c1-714b-3bdd-8307-d3c1fa6df852 | -15.61208 | -41.52149 | 2026-08-31 16:28:00 | NPP-375 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ac376e08-cdc2-3d96-8dc4-8b630f65fbba | -17.71744 | -49.22881 | 2026-08-31 16:28:00 | NPP-375 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b9067f89-ca1f-3ec1-b019-f1376e525cb5 | -16.29162 | -42.57786 | 2026-08-31 16:28:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1fffc03a-f881-32dc-bbe9-1aea568490a5 | -15.36995 | -41.18508 | 2026-08-31 16:28:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| ff813fcb-68c8-3a07-83c7-86da63c12b42 | -20.29749 | -47.8336 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 21fee2d6-4b47-36f6-878c-0ee477893c2d | -17.27862 | -39.78982 | 2026-08-31 16:28:00 | NPP-375 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 17ab5b6c-71da-3bc7-8479-f50163a7ee73 | -19.25472 | -41.61905 | 2026-08-31 16:28:00 | NPP-375 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1c5bc487-544c-36d8-b8cb-338919f7c93f | -14.90723 | -46.90277 | 2026-08-31 16:28:00 | NPP-375 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 81540122-1c4c-3d87-b9fb-9a0004784a4f | -14.61104 | -41.56754 | 2026-08-31 16:28:00 | NPP-375 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8a428ab9-1989-3675-ad48-274097a0208b | -17.86215 | -52.12363 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 68e43215-acce-37e3-995e-f83efb752cf7 | -14.88188 | -40.57095 | 2026-08-31 16:28:00 | NPP-375 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d23d8c6a-0e21-37c5-8da7-051faa43db70 | -13.88992 | -39.84681 | 2026-08-31 16:28:00 | NPP-375 | JITAÚNA | BAHIA | Brasil | 2918308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 94c71559-730f-3ac4-b268-0c054f270d9c | -15.99947 | -43.55035 | 2026-08-31 16:28:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b4572c1c-5912-36d9-94cc-239a8f1c1f30 | -14.99422 | -48.13453 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 2fdbe93f-7522-3ebd-a8fa-eceb9c4eb932 | -16.018 | -54.40719 | 2026-08-31 16:28:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62f0b477-42c3-3290-b383-04b01791c5ab | -19.82507 | -47.94679 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2adb78b7-4079-3069-937a-1d55a45e30d6 | -15.16457 | -44.00278 | 2026-08-31 16:28:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4b3a80a7-ec2d-30e7-a4ee-9fa2ff352393 | -17.7178 | -49.23217 | 2026-08-31 16:28:00 | NPP-375 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ece96a08-3252-34ee-b3f0-ff09582b9f18 | -17.1804 | -48.7458 | 2026-08-31 16:28:00 | NPP-375 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 1c9ea9d6-a5af-3b77-9056-b590a96a1672 | -17.85781 | -52.1266 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 52bdc00b-c19d-3c21-b56a-caaf62b7c9f3 | -17.87176 | -52.09105 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 560072b0-caa6-36ad-b4d9-221312ace26a | -16.8958 | -40.22274 | 2026-08-31 16:28:00 | NPP-375 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f07b9e09-b580-3fcc-b40f-2b3e6cd30564 | -18.26046 | -52.75353 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6e0c29c-883b-33b8-b9ee-b335454b4f0b | -18.27513 | -52.69358 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| bafc4645-1e37-33f8-add3-8d9e90861614 | -16.99489 | -51.84346 | 2026-08-31 16:28:00 | NPP-375 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e33d978d-aae2-37dd-b23a-2b601e5019fc | -16.60526 | -42.37595 | 2026-08-31 16:28:00 | NPP-375 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 31530f8d-8c66-3b58-a5d1-7702875388b9 | -17.8606 | -52.1077 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| ae290e85-ef50-395f-ba98-a428b2769991 | -17.87398 | -52.09338 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 288.4 |
| cb135e66-9044-32b9-a2ba-0e2180b2a0b5 | -19.84371 | -47.93272 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 0e48b0a3-ebb2-3d35-a369-79061d15411c | -19.82877 | -47.93439 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 41bdc004-4efd-32dc-9f5b-60ec89b651f0 | -17.85425 | -52.10825 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| ae4d36e8-99c9-36ea-bf94-f2fd89e780de | -20.34086 | -47.10366 | 2026-08-31 16:28:00 | NPP-375 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f88ba21a-a354-3733-9565-43f9ebe2ff0f | -19.83308 | -47.92772 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 56c54ffa-b165-3c0f-81e6-1851e9517078 | -16.56611 | -52.51959 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 1f367337-d932-3052-86cd-d47019a44bfe | -20.29348 | -47.83817 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 56f307f4-06b4-3bd8-acbb-a1e62eb79501 | -19.83375 | -47.93383 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 78b62da9-67fd-306b-bdf2-eea1f72ca454 | -17.85148 | -50.51273 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 43d58f36-171a-344a-937c-695c42e38c25 | -18.98215 | -46.81982 | 2026-08-31 16:28:00 | NPP-375 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 532bcf8f-aff0-3e3f-a7ef-7ead35fde148 | -20.29289 | -47.83252 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 26.1 |
| f0479651-6bcb-31d2-b7fb-b5ed7703d5d8 | -17.74299 | -47.27325 | 2026-08-31 16:28:00 | NPP-375 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| bed0fae2-be0c-395f-a6a1-b33a38e07bf5 | -18.26992 | -40.55186 | 2026-08-31 16:28:00 | NPP-375 | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 34aba39c-4d63-3741-8537-b73132c370b7 | -17.37214 | -44.88149 | 2026-08-31 16:28:00 | NPP-375 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b9ecffa1-2f43-32b0-9c68-4c61d69ddaae | -14.99094 | -48.15731 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ace1d451-b7d5-3a31-9285-c6b911dbd939 | -16.80108 | -41.65789 | 2026-08-31 16:28:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6413d8c5-1967-3312-a711-2673dd6f2ce9 | -16.57145 | -52.50788 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 4e4dda08-d876-3582-91b1-7e8c61622b47 | -18.41484 | -43.64884 | 2026-08-31 16:28:00 | NPP-375 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1bccae9-eb56-317c-b62b-395ca19af811 | -15.03891 | -41.40197 | 2026-08-31 16:28:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 57618f17-1845-3c41-9edc-af41cdf92da4 | -18.9097 | -50.87853 | 2026-08-31 16:28:00 | NPP-375 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 38.6 |
| d711c184-e459-3904-bf3b-cfddcd3b2f61 | -17.70654 | -49.22686 | 2026-08-31 16:28:00 | NPP-375 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cce10e36-08d7-3aab-b549-8c4d500f2cf9 | -17.37103 | -42.13467 | 2026-08-31 16:28:00 | NPP-375 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 01061ab4-9306-3a81-be1d-f036ecef00ab | -15.67392 | -45.94441 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5bdb79b6-0c99-3603-bb60-797378175fff | -18.26348 | -52.71224 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| a4ec154b-3e42-3b49-9ceb-a53fc1bcc0ef | -17.35006 | -44.92745 | 2026-08-31 16:28:00 | NPP-375 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1d7d543-1a3f-338d-89bb-f4b10ca54523 | -18.739 | -41.50867 | 2026-08-31 16:28:00 | NPP-375 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 1e4509e9-823f-3583-84fa-abdb9cbb09a2 | -15.2134 | -41.74613 | 2026-08-31 16:28:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0a8423d5-5fcf-3c52-80e0-a470d43b0c4a | -15.02172 | -48.16389 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f6f5b405-e6b8-332b-a839-65bc3b52dbe6 | -15.088 | -48.02892 | 2026-08-31 16:28:00 | NPP-375 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 01b42055-e08a-31f8-ba77-18bbd35dc971 | -15.66682 | -45.92237 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b22a7084-07ef-3985-9825-701d92995783 | -18.26247 | -52.75559 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4dd29f77-fd4d-3612-a19a-19ed2b498c93 | -14.79993 | -40.67632 | 2026-08-31 16:28:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e942b919-3096-34e4-8eb2-e077e1bdf8b0 | -19.18559 | -44.51026 | 2026-08-31 16:28:00 | NPP-375 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b0055645-eb46-3c49-8e0c-5a84483a2d1a | -16.56411 | -52.51667 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| fdf1e5e4-c353-3336-ac5d-caad029fdd1e | -17.37083 | -44.87925 | 2026-08-31 16:28:00 | NPP-375 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dc2a48b2-360f-31ad-995f-0a8a25853474 | -17.27816 | -45.99578 | 2026-08-31 16:28:00 | NPP-375 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 712e7092-91eb-3aee-9638-dc9cf1df34fc | -15.96257 | -39.11547 | 2026-08-31 16:28:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b88b0612-02cb-3abe-a449-11779411e83e | -17.87341 | -44.25333 | 2026-08-31 16:28:00 | NPP-375 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be1ba180-3b32-3df7-a1f0-3f60085161ef | -19.82379 | -47.93499 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e4dfc1c8-b4dd-32a5-971a-f4316eb3123f | -17.87125 | -52.08588 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 08321978-f065-3a64-82be-f02a6283bc41 | -15.42937 | -41.21623 | 2026-08-31 16:28:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README112.md)
