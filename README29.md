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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bce5153-42b1-35fb-b691-8e0f820094b6 | -17.41105 | -48.10409 | 2025-08-24 03:45:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc626118-ff2b-35d4-b526-e3e18e5c9141 | -12.71957 | -48.13813 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 846bc20c-3081-317c-a847-eee1fee7bced | -13.03619 | -45.21767 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2de2945-5fea-3b85-b6d5-68307afcf767 | -14.39932 | -49.76633 | 2025-08-24 03:45:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0be1983-4b9e-3f3c-936c-5005611b2c05 | -14.87767 | -47.60754 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60349060-b9fd-3fee-9a87-159c1e33ffeb | -12.99618 | -45.23705 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3838c157-6d24-3932-ad45-77b2e2506eb6 | -13.09852 | -44.10169 | 2025-08-24 03:45:00 | NOAA-20 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b2a5bf1-7e53-3141-be91-5cb45abd9720 | -12.72757 | -48.12552 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1d13fc1-e6bf-30ee-8feb-cd64b9e4c89d | -12.93755 | -46.29522 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51bf8135-5f1b-39a8-8a62-3a24a4117464 | -15.10809 | -48.66085 | 2025-08-24 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 438ddc03-d5d6-359b-b360-752f9de3807d | -14.8104 | -47.94072 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 064e037c-1417-3ebb-bb42-b5bcee116908 | -18.7519 | -45.10044 | 2025-08-24 03:45:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0c1cfce-79e4-3224-89d5-e9fa0004e4d2 | -12.72356 | -48.11877 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fcf43da-d115-3b40-9041-dbb820d47e1a | -12.04216 | -50.36617 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 056894fc-1559-3622-99ef-b11ae1fedfef | -14.37819 | -49.17149 | 2025-08-24 03:45:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5bad58e8-5806-3d94-937a-aa94520e895b | -13.47165 | -47.02208 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e970152c-9935-3459-ad20-db14468d0136 | -12.54731 | -45.62143 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5485f05-7bba-3550-aaad-8060320f0d4d | -18.39712 | -46.84105 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29b91e23-54af-34ae-8c0f-cc6817dfe1cc | -15.22897 | -48.2153 | 2025-08-24 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76af6d63-1d72-3aa5-9e2a-c0ff1b9b9802 | -12.72579 | -48.13851 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80d2d0cc-0377-3c25-bf22-8d0366754179 | -14.8025 | -47.92056 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| fed8bae1-fac4-3cc9-9f97-a25bf83b4524 | -14.84715 | -48.32211 | 2025-08-24 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b44fdfb-f0bc-3c1f-8b11-ce323006ddc3 | -18.40214 | -46.84215 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04bdd1d7-dc09-3e34-bc07-39d2c70ffb22 | -13.48282 | -47.02413 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5ec8664-cea6-3481-b269-19bab900b107 | -15.22222 | -48.21855 | 2025-08-24 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b63c3ff-3272-3b39-8171-75cad046c79b | -14.84996 | -48.3265 | 2025-08-24 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3355f586-52c9-3950-8029-ed45ecda4bad | -13.10312 | -44.10277 | 2025-08-24 03:45:00 | NOAA-20 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf37fa93-87f8-3cb7-bb55-1d19edb76946 | -13.47685 | -47.02499 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4b18e76-43b4-361f-a904-f315d053d6c4 | -13.05447 | -45.23063 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ea24daa-4420-3c67-aa36-c999a7099fb8 | -17.39302 | -42.62612 | 2025-08-24 03:45:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 902baaa7-ee76-3f3d-9cf6-4036d432b5e8 | -13.04949 | -45.22957 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9eea375-db99-3df6-a1cf-73ab84fbcc80 | -18.40583 | -46.84362 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dabc1991-8266-3877-8ebd-a54054d96441 | -11.31066 | -47.85463 | 2025-08-24 03:45:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6451b70e-8157-3975-9027-e0eaa58784f0 | -11.60506 | -46.23694 | 2025-08-24 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1c0a354-7420-3f01-923c-066edbfd77c8 | -11.27678 | -44.97282 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46d71323-9eeb-3163-b2df-2537a4520424 | -13.64849 | -46.88242 | 2025-08-24 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ae7267f-ab3d-38f5-b45d-e50f55d1be81 | -11.59956 | -46.23603 | 2025-08-24 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3471461-e839-3df6-ae7d-9a59791030bf | -18.74906 | -43.83571 | 2025-08-24 03:45:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 984ad446-e5c3-35fb-84b1-e1d4408c0a2c | -13.45551 | -47.02431 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 403198aa-f594-32d6-a00b-d32c79fd568f | -14.80334 | -47.91644 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c8068d36-ff15-3197-9257-66a90cd3a718 | -14.80087 | -47.9286 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d16114ef-050d-3a77-ab36-358f8b6802c0 | -12.73395 | -48.125 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5e283fb-2648-3940-99f2-f2d6eb5b2f0b | -13.0445 | -45.22853 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d4d5427-9789-3552-a48d-4ea56c49072d | -15.04856 | -48.52863 | 2025-08-24 03:45:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e07663d-985c-3e9f-b037-fd2c8ab99906 | -14.87474 | -47.60717 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fb66a78-0dc6-3309-8478-fe93884269c5 | -17.60869 | -44.30373 | 2025-08-24 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d28138fa-6f9c-3f31-8133-db45551572b0 | -13.04561 | -45.22264 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c445e8a-8255-3419-b053-9b23ef77a2c5 | -15.06336 | -46.48147 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed95ce6b-498d-38e7-a983-0e07364c42d3 | -20.35402 | -46.73351 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cb371f5-98b5-340d-b609-cfe8d1f0ea7b | -22.72422 | -46.98093 | 2025-08-24 03:47:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1e6a7404-51b2-3fea-becc-dc17c164c1f7 | -22.72812 | -46.97198 | 2025-08-24 03:47:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4070c2fc-382f-35a0-b362-c95ca7871ffb | -20.77672 | -43.4417 | 2025-08-24 03:47:00 | NOAA-20 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 44df6c10-7f36-3d0b-825f-576230302636 | -19.72894 | -47.98048 | 2025-08-24 03:47:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f40d979f-8f2a-3f1b-81fd-c81d65119d51 | -22.73113 | -46.97095 | 2025-08-24 03:47:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ec85b810-62fe-30ff-863f-98326af12c07 | -23.64988 | -46.50076 | 2025-08-24 03:47:00 | NOAA-20 | SANTO ANDRÉ | SÃO PAULO | Brasil | 3547809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6454a231-d087-34f9-b2af-1f35a6bd129f | -20.97566 | -42.86586 | 2025-08-24 03:47:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 78baf393-08c0-39fc-a30c-c62ff510d3dc | -21.27645 | -43.75321 | 2025-08-24 03:47:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a7bc226f-46b9-311c-93c6-736ccc657fa1 | -22.13911 | -43.65713 | 2025-08-24 03:47:00 | NOAA-20 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| a2125846-989d-37c5-b90d-afbe570b8689 | -20.37048 | -46.74441 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13d51cfb-c85c-34c8-8336-cf683cabeeb0 | -22.45044 | -42.30452 | 2025-08-24 03:47:00 | NOAA-20 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 23440915-4bb0-38ef-a2b4-f3c484ecdf8a | -19.68977 | -48.98633 | 2025-08-24 03:47:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05562fa5-cd32-387c-90ee-08a368ebcee7 | -23.4932 | -47.07747 | 2025-08-24 03:47:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e843d0f1-fa06-3d99-8c5c-4ddf4ceb72d4 | -23.32465 | -47.84228 | 2025-08-24 03:47:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 85e29958-b23a-3572-92ef-14db7cbb17f0 | -20.35165 | -46.74512 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96f5e0c2-ea23-331d-9158-08d5b6fe1cbf | -22.72859 | -46.95964 | 2025-08-24 03:47:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3ea28929-9749-3301-9442-a1aba6e2eab9 | -20.8045 | -40.91141 | 2025-08-24 03:47:00 | NOAA-20 | RIO NOVO DO SUL | ESPÍRITO SANTO | Brasil | 3204401 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 03724dd7-ac50-3195-879b-92ef9e0c81ed | -20.96063 | -42.86275 | 2025-08-24 03:47:00 | NOAA-20 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1fd6f904-19e5-3739-bf8c-8949ff4a980a | -20.36668 | -46.76241 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e01933e-7ba3-3cb8-90cb-3857b3bd690d | -23.72391 | -47.43015 | 2025-08-24 03:47:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c6317162-4e7c-3904-84cd-a2b45939b1c9 | -19.63221 | -43.18612 | 2025-08-24 03:47:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| fe55154b-0f96-3dd6-8540-75be44e8d538 | -23.12109 | -46.84949 | 2025-08-24 03:47:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c0a8da63-899c-3ffc-839b-c79d8a45b1b7 | -22.21872 | -45.69414 | 2025-08-24 03:47:00 | NOAA-20 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| d5c2c5c5-46ae-396d-b605-3bebab1e0aa2 | -21.38468 | -43.8812 | 2025-08-24 03:47:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 04f7148e-eb8b-334e-9ac7-dc36865f3d64 | -23.27945 | -46.56887 | 2025-08-24 03:47:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 92a33e37-e2ca-36bc-b69d-958f6a5e4cf3 | -20.51058 | -42.3808 | 2025-08-24 03:47:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9f22f06c-e9df-30b3-ae93-59a71fe32a64 | -20.3504 | -51.69677 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a43e89f4-d751-3bcb-aae5-938bf7928864 | -20.34133 | -51.70627 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b2f42314-bd19-324f-8ca4-ecaaab717d31 | -19.62928 | -43.18003 | 2025-08-24 03:47:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c7f7528e-220f-3a50-a498-0ea69134f672 | -21.29402 | -43.849 | 2025-08-24 03:47:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 03f69e76-ec33-3719-98a4-d3f96dd3f712 | -23.10703 | -49.9739 | 2025-08-24 03:47:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5ede06e1-f5c2-3d40-91ce-e4341e4e1f40 | -22.72287 | -46.9638 | 2025-08-24 03:47:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0d06475f-e174-3917-a66c-618e501b70ec | -23.26319 | -46.78374 | 2025-08-24 03:47:00 | NOAA-20 | FRANCISCO MORATO | SÃO PAULO | Brasil | 3516309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4f7d4106-2d96-3615-bbd4-7deca4ab3070 | -19.83321 | -47.54106 | 2025-08-24 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c45bb1b5-38bd-3e1e-8449-dc08ae3751fd | -20.4009 | -41.40157 | 2025-08-24 03:47:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d52d4fca-5763-3bd3-b5de-41f9b650a33b | -20.3595 | -51.68554 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8e5bee1d-e11e-302c-85e5-cf383a6dfafb | -21.38267 | -43.87923 | 2025-08-24 03:47:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ce02585b-7d96-34c9-9e48-5576959bf204 | -20.97191 | -42.86501 | 2025-08-24 03:47:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 582d96f0-dfcc-3d2e-9efb-9950b6805c5d | -20.93781 | -46.83492 | 2025-08-24 03:47:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c078abce-87e2-39b0-b21b-bd63ba2818f5 | -23.35322 | -45.80765 | 2025-08-24 03:47:00 | NOAA-20 | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d3a1274d-d02d-3e34-8ab8-5c4f9cbb6969 | -23.32577 | -47.84894 | 2025-08-24 03:47:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 5d03e430-a77f-342d-af07-b9a12a281b53 | -23.6234 | -46.02722 | 2025-08-24 03:47:00 | NOAA-20 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 65cdddd7-9438-398c-b75d-fbfb5acb4d90 | -23.26215 | -47.24196 | 2025-08-24 03:47:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 50b001f8-ea1e-3b25-a2a0-88646c635e6c | -23.36509 | -46.8662 | 2025-08-24 03:47:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 635b691f-1b0c-32d8-bac0-398343eb3b45 | -20.9326 | -41.68221 | 2025-08-24 03:47:00 | NOAA-20 | SÃO JOSÉ DO CALÇADO | ESPÍRITO SANTO | Brasil | 3204807 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 65a4924a-2758-30c5-a60e-f03c489b0cee | -22.11614 | -42.0015 | 2025-08-24 03:47:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 22183e8d-ce7b-34bd-9283-51ee5e0c6b20 | -21.54663 | -44.17029 | 2025-08-24 03:47:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 05b18f3d-360f-3739-8d73-e96ba17ff96a | -19.83278 | -43.58149 | 2025-08-24 03:47:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea0cd754-77a3-3d5e-8834-b2cd2ccab884 | -21.78523 | -42.08557 | 2025-08-24 03:47:00 | NOAA-20 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b26b4119-9cf3-3451-9a9a-51d6a1f47178 | -20.35317 | -51.68353 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5e5f3a8e-2f21-3d93-a2f5-0dce237d5b8e | -23.32704 | -47.84312 | 2025-08-24 03:47:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |


[Clique aqui para ver as próximas entradas](README30.md)
