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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da27ac53-9f14-3f5a-8a46-da97d8fe432c | -18.9185 | -48.53858 | 2025-11-02 04:23:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9693c9b-bee2-3b22-8b4e-ba3181348685 | -13.83696 | -47.04906 | 2025-11-02 04:23:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d28ece6-be6a-3686-ac9b-86f41209f099 | -12.25464 | -51.33242 | 2025-11-02 04:23:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 499f1801-ce91-3387-be6c-092533bbf21b | -15.65052 | -53.48302 | 2025-11-02 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3947308-aa6a-3f0f-8cff-09323be70a36 | -12.87899 | -50.86637 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1853180-bfd3-3520-bdad-c61a84ca17ec | -13.87889 | -47.36206 | 2025-11-02 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5523fed8-2612-309e-8fde-31aecbb7c2a3 | -14.65861 | -46.60972 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1678a810-6ca0-3aa9-99e3-6bdca92da89c | -12.42253 | -54.48942 | 2025-11-02 04:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07a6172f-ddc7-3e62-9b17-0fbc145f8465 | -15.08882 | -42.12528 | 2025-11-02 04:23:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1333440b-78e1-31fc-a8de-b428e847ef00 | -13.84028 | -47.04961 | 2025-11-02 04:23:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de78b473-f758-323f-8849-e42e67eb9d0b | -13.7717 | -48.86961 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d354ed2f-9103-3990-9d99-c7deb849cde0 | -14.10399 | -44.20883 | 2025-11-02 04:23:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b3a6bdb-58d7-3299-b70d-4897e63023f3 | -14.59222 | -56.00134 | 2025-11-02 04:23:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6ec768c-0b3a-3640-b1ea-b2c7dc01c602 | -15.24399 | -51.75632 | 2025-11-02 04:23:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e11e551-1ba5-3bf9-b340-d6650fbd68d9 | -12.86925 | -50.8753 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c40a99a-5ec5-3a34-ab96-f959bfe5526c | -15.24464 | -51.75271 | 2025-11-02 04:23:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18951590-b044-3894-97d6-fa1b910edb36 | -12.42194 | -54.49247 | 2025-11-02 04:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ef3b7e5-fa79-31f5-8eb8-29ea5cbda795 | -14.20494 | -47.80685 | 2025-11-02 04:23:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d1af1b4-737a-30d7-9da2-0d9d316ddad4 | -15.47617 | -43.21997 | 2025-11-02 04:23:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| db7181b2-9bbc-3528-91f0-4542780fa545 | -12.86968 | -50.87862 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fca70bf1-7d36-34c3-af2d-df0c8db8ffa5 | -13.52125 | -48.6481 | 2025-11-02 04:23:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac9ed959-ca7a-3510-8922-17f9f48e4458 | -14.01817 | -43.48296 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1eece98e-d9df-3187-8b84-35b2ef316ea5 | -12.87924 | -50.88779 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f630e790-fa2a-39e1-96a8-a0658ef3addb | -17.14933 | -41.94527 | 2025-11-02 04:23:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d394bead-af9a-3bd5-813d-151601e4e9b4 | -14.61445 | -46.65342 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 702c8eb7-b57b-3e21-929d-c746a8b6e399 | -14.45004 | -51.52725 | 2025-11-02 04:23:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8421674a-e744-31e1-af2c-00a03de7c68d | -18.11395 | -44.42996 | 2025-11-02 04:23:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8cdae2d4-debf-3953-b802-d684f82c3815 | -15.24063 | -51.75195 | 2025-11-02 04:23:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae9144c2-4112-33ef-9534-4d9b839fd79c | -13.87063 | -47.3495 | 2025-11-02 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad5fc290-0c14-35bb-8641-c1891975a119 | -15.12765 | -47.23671 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c0b382f-f341-3677-bac2-4124ed4254de | -14.02936 | -43.48051 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e00fb708-cb4a-3650-bbb2-11b3d897f1b8 | -15.35854 | -41.85243 | 2025-11-02 04:23:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3fae52b4-6a5c-3d9d-9fa8-260a223c4f40 | -15.3004 | -42.95853 | 2025-11-02 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 37b24557-0865-386c-9290-eb1bc0a0c20d | -13.76295 | -46.89446 | 2025-11-02 04:23:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30049dcc-3336-365e-9b5f-2be0874a35c7 | -18.47679 | -48.3842 | 2025-11-02 04:23:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0442f22b-30c8-37f8-83ef-bb6abf954231 | -15.32961 | -43.88872 | 2025-11-02 04:23:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8de18771-751e-3fc2-a4df-8b1d80e49413 | -14.59682 | -46.65777 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a406b6f9-85b4-3464-9619-755548b8276a | -12.87134 | -50.88637 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b94ce77-9b68-31bb-a542-8fcb238a5bf4 | -15.13713 | -47.21999 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6692b4ff-4fea-3bb9-be06-c7304e196fa3 | -13.80815 | -43.2854 | 2025-11-02 04:23:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1188fd55-959f-3235-8c4b-b28492c8b90a | -14.43156 | -51.56104 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fafec76b-950c-335a-848b-3c055e3c24d4 | -13.49623 | -44.10309 | 2025-11-02 04:23:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a19c1fc4-36d6-37d1-9836-6a3989708b0f | -13.57536 | -44.06453 | 2025-11-02 04:23:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1b204c8-9ec4-3235-ad90-e84933b274db | -15.63324 | -41.36187 | 2025-11-02 04:23:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 82e7c8c2-7435-3da4-a392-1ef5a3144ba6 | -16.74355 | -44.15869 | 2025-11-02 04:23:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9416a27e-5c38-3f69-9636-e19a80e30164 | -14.66135 | -46.61382 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eee823c-0e59-34bf-a51b-c0df47a1b7d8 | -14.4534 | -51.53158 | 2025-11-02 04:23:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1756c990-e6bf-3d66-a647-db2af3081f6e | -12.23407 | -54.39361 | 2025-11-02 04:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbd16efe-50f6-3987-912a-31a94468b7cb | -15.4798 | -43.22052 | 2025-11-02 04:23:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 540937f2-3f2a-34ec-9156-10fa4aa54196 | -13.68071 | -47.21826 | 2025-11-02 04:23:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bffd308-4f29-3f94-ab13-a8b6c5e91bf4 | -13.84361 | -47.05016 | 2025-11-02 04:23:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9582f96-74d9-3f42-aef8-9fba05b1ee8d | -18.52235 | -53.49349 | 2025-11-02 04:23:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c4e4255-b122-356a-bfad-9c470a680fec | -14.2233 | -44.30155 | 2025-11-02 04:23:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a9e345a-8583-3784-9b24-dc103b35e64c | -12.4656 | -54.32013 | 2025-11-02 04:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 900aaa6f-23c1-3b54-800c-7fdd7b374607 | -14.3033 | -43.83188 | 2025-11-02 04:23:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1551c54-30a2-3694-bf45-2588182805da | -18.50181 | -46.95852 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9bfbcdb-1dc3-3048-8932-8fb05ec21c53 | -17.85274 | -51.73164 | 2025-11-02 04:23:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 272d6ac5-04ca-3405-9f5d-0edc74457b70 | -14.59738 | -46.65422 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6488f61c-4666-35b2-adf1-1533266bd30a | -18.45292 | -51.62906 | 2025-11-02 04:23:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea87e25e-ff48-3f0f-9ed3-fa3595749cd4 | -13.78504 | -48.87598 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5253915-94d0-3f17-9979-a90814258598 | -12.87227 | -50.88118 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b775b357-54ba-3e08-9cf0-03f333fc5134 | -15.00995 | -39.74671 | 2025-11-02 04:23:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 643519e1-0e09-37df-a8b2-f031ef121176 | -12.87146 | -50.86825 | 2025-11-02 04:23:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d2bae4d-d77b-38e4-8d9f-7b1febf220d7 | -15.11265 | -47.24527 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed5027e3-4fb1-3937-9d43-e3a6cced9277 | -13.77802 | -48.87485 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3585786-ef37-3f9c-a523-cf901e624dd4 | -14.74527 | -42.46042 | 2025-11-02 04:23:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c18ba9e-954c-395c-ad39-1d4580019b46 | -14.02289 | -43.47535 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 228ce23c-7d23-3b63-bd02-48c821747347 | -15.32516 | -44.19076 | 2025-11-02 04:23:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c93ae7c1-d34d-3b4b-9c90-d56948a6d8e1 | -12.42359 | -54.4899 | 2025-11-02 04:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e64b938c-963c-3da0-8fe4-87e83091f985 | -12.46504 | -54.32304 | 2025-11-02 04:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cd99187-509f-3219-b749-e675cba37f08 | -12.87621 | -50.88189 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e1bfbf15-8601-38d3-a7e6-c4b77c95ea48 | -14.19202 | -44.37083 | 2025-11-02 04:23:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c8af5b8-fe30-3300-9bae-b2a0e8c67ad4 | -18.6334 | -46.87632 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc9acabe-bc98-3082-bfba-a40b6e995a06 | -14.66465 | -46.61438 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 827d969a-e939-354f-9838-d92f86b119fa | -13.1477 | -48.44392 | 2025-11-02 04:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b145aecd-ce37-3481-be7d-2f0f2bf7c8ca | -19.33154 | -54.32034 | 2025-11-02 04:25:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75cc7346-a90d-38a4-87ef-47027bdd73d2 | -21.41168 | -49.24816 | 2025-11-02 04:25:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7260bc01-c36b-347f-b4b7-3465224b03bc | -20.29312 | -54.0835 | 2025-11-02 04:25:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df949b7c-b8b5-3eae-a3e4-f6e17f761519 | -20.29816 | -54.08025 | 2025-11-02 04:25:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bb97e09-270b-3d01-ae55-4a896e20ed45 | -20.67501 | -53.80389 | 2025-11-02 04:25:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac2ebd19-d468-37f9-8c46-f7182e193d15 | -20.48016 | -55.83801 | 2025-11-02 04:25:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 914641ee-b6ec-304e-b305-79a324c8095c | -20.29736 | -54.08441 | 2025-11-02 04:25:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90c13d50-699c-3e95-ac63-2084ddafe661 | -14.0356 | -43.4666 | 2025-11-02 04:30:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7bb9452f-d215-3c38-9b3f-153f5b076f32 | -13.3177 | -43.4552 | 2025-11-02 04:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| a99f0fe3-4aa7-3d3d-a499-4405e0dc84c8 | -4.1361 | -51.152 | 2025-11-02 04:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 15f420eb-e77a-30fc-a90b-d619d1e97d1e | -3.7214 | -45.541 | 2025-11-02 04:40:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 79eabd5e-3f5c-3b1c-b4ff-89ef43ecc9e3 | -14.0356 | -43.4666 | 2025-11-02 04:40:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e25f6e63-8c2f-342f-a930-bbbdd8f877e0 | -12.8722 | -50.8862 | 2025-11-02 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2ee5e111-05cf-3d87-b497-b04c8ae5ab61 | 1.69795 | -50.88865 | 2025-11-02 04:46:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 402d7083-7c8f-30b9-a3d7-5b4ab78f8497 | 0.15464 | -51.41998 | 2025-11-02 04:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 986f2aec-09a4-3355-810f-52944b66c0f3 | 1.02382 | -51.19662 | 2025-11-02 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6457e77c-2f74-3106-9bb2-92c1ec06a12f | 0.14836 | -51.42475 | 2025-11-02 04:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d052b2d-2067-35e1-be07-400a33b4df2f | 0.95877 | -51.2938 | 2025-11-02 04:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe706637-50aa-34ec-84f3-b55b72c4be02 | 0.15121 | -51.42051 | 2025-11-02 04:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb91b736-0231-37a0-9505-5722d6091094 | 1.0039 | -51.2261 | 2025-11-02 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5255d8f-d502-3c3e-89c0-f68e5a3e53ef | 1.0204 | -51.19716 | 2025-11-02 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52912b7e-cd12-3f09-bc00-c83499eaa9aa | -4.683 | -44.62373 | 2025-11-02 04:48:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 620db351-6faf-336b-bd47-df276bc18ac7 | -3.5063 | -50.47309 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79bf01f4-827d-3553-bb58-07659890c137 | -3.73452 | -49.6887 | 2025-11-02 04:48:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff7aa105-830f-373e-a229-a0fccbcf19f5 | -5.03581 | -43.61513 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README15.md)
