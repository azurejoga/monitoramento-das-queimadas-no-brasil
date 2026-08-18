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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59a60ad8-c680-32de-845c-ffbf6780c7cc | -13.29088 | -51.65868 | 2026-08-18 11:57:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 643fb5ab-dc17-3113-a519-2c4209b37497 | -14.81034 | -46.62616 | 2026-08-18 11:57:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| b280c0b1-bf43-30cb-a993-0941fc5d186d | -18.95857 | -47.32045 | 2026-08-18 11:57:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 2cbb2182-0b7a-3f51-a04c-0d961ac3f8fc | -12.76982 | -48.44807 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 3952dbc7-858e-3b38-9747-dcb459a47a46 | -19.25947 | -45.31754 | 2026-08-18 11:57:00 | TERRA_M-M | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 281800f4-6105-3ec9-950f-79d70bc86033 | -14.27712 | -51.9133 | 2026-08-18 11:57:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f31f15dd-5ecc-3ab8-9e26-621f7fa61dae | -17.46058 | -47.84905 | 2026-08-18 11:57:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1b52a65e-fd6d-319b-87fe-94f9e65d270f | -14.34805 | -51.93378 | 2026-08-18 11:57:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a7f09d74-ad94-32c7-bbbd-4c28bc0f95cb | -12.74097 | -48.45379 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6d5d6185-6696-3d4d-8171-761aa01b1658 | -12.79089 | -48.43089 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 5a94c741-2ac0-311e-b506-14905e0a49ac | -17.24309 | -48.11819 | 2026-08-18 11:57:00 | TERRA_M-M | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 025e04c7-a3bb-313c-9650-aa4aba947517 | -12.53873 | -47.85888 | 2026-08-18 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 6e4d61f9-cb38-34fa-924b-602b76ea89a5 | -14.17616 | -52.89111 | 2026-08-18 11:57:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 77252c46-7790-390e-b104-6a7771b7898a | -14.28331 | -51.93372 | 2026-08-18 11:57:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d57a6c2a-08d7-35fd-abe4-72ba5924c182 | -12.70514 | -48.52147 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 43a823f3-c1a5-3d2a-8d03-4ca76b79de8b | -14.1776 | -52.9452 | 2026-08-18 11:57:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7bb81242-68f2-34fb-8014-48dfdf1c2582 | -13.56289 | -51.69024 | 2026-08-18 11:57:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5111f91a-8e76-3720-be24-374c824ddb87 | -14.16615 | -45.4125 | 2026-08-18 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 9676826c-c254-3bac-a006-09f1b2f9282e | -13.5615 | -51.69968 | 2026-08-18 11:57:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 08036002-b0c7-3614-9b42-0911b90b9937 | -16.09775 | -45.13975 | 2026-08-18 11:57:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 541605c9-a721-38a9-84b1-df587898fb75 | -14.24678 | -51.93187 | 2026-08-18 11:57:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 39047387-75b7-3bbd-b7bb-c0dc7db6d3fd | -14.19182 | -52.91536 | 2026-08-18 11:57:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 5d11df6e-57c8-381b-8ee1-bc7c6939d2ae | -13.28046 | -51.66678 | 2026-08-18 11:57:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| dbce929e-7471-33b5-8012-0aaf170d56a5 | -14.24819 | -51.92235 | 2026-08-18 11:57:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 8af666e2-4597-3b33-8d76-3f1c55930e8b | -14.03321 | -53.68696 | 2026-08-18 11:57:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 504cdb72-5e9b-3378-a807-cce412819bdb | -19.614 | -46.97488 | 2026-08-18 11:57:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f8fea312-e70a-3d08-abd9-40005585a593 | -14.50132 | -45.66782 | 2026-08-18 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 26d74ab0-12d3-3495-bc1d-255d848cdab8 | -13.58691 | -51.77734 | 2026-08-18 11:57:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| ec0ea4f7-08b8-38e6-9d99-3df6fdb0f12d | -12.54013 | -47.84861 | 2026-08-18 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 3796d103-643f-3ea2-b85e-434be88dce35 | -11.33981 | -51.12407 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 38571de4-d22b-302c-9ec7-396aef5d714e | -15.01785 | -52.69365 | 2026-08-18 11:57:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5d8ca8b0-6b9d-351f-b880-52d94a069096 | -14.1821 | -52.93 | 2026-08-18 12:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8d1d6c3a-d342-39bb-97f1-27b3cbfc4ec6 | -14.1631 | -52.9113 | 2026-08-18 12:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| a4523a6e-73f2-3849-8c5e-d722cc609ee7 | -8.5973 | -54.7352 | 2026-08-18 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8267685f-50f4-3ab6-ac9d-64db5d98527f | -8.5788 | -54.7162 | 2026-08-18 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 191.1 |
| 4fcb2932-a7fb-376f-99f8-0f2924e6838b | -12.7793 | -48.4205 | 2026-08-18 12:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 305f5829-e939-3258-81d8-feaf9108ea52 | -14.1628 | -52.9323 | 2026-08-18 12:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 139.7 |
| a0cb88fb-6b9d-3a9f-aaa9-5dde40b83f88 | -8.579 | -54.696 | 2026-08-18 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b5bd9f3e-280e-370b-b916-4e1042ae0bb1 | -14.1824 | -52.9089 | 2026-08-18 12:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| f022f9d4-8743-3552-8c3e-86baf7ed6eb0 | -8.5602 | -54.7175 | 2026-08-18 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0414af55-d289-34bd-8242-8d805f3c2d53 | -19.58836 | -49.22903 | 2026-08-18 12:00:00 | TERRA_M-T | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 37.4 |
| c50b0ea8-75c0-355e-a7e5-513ca8d2db5c | -21.11106 | -45.61349 | 2026-08-18 12:00:00 | TERRA_M-T | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 49c2f44e-9c87-38de-a0b9-6cddfa8442a8 | -23.55351 | -50.78775 | 2026-08-18 12:00:00 | TERRA_M-T | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 98750d90-4a0f-37bb-967c-0b42da73cb08 | -21.21544 | -45.87375 | 2026-08-18 12:00:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| e9671ba1-1310-3286-9faa-a23908ad69b5 | -19.58977 | -49.21818 | 2026-08-18 12:00:00 | TERRA_M-T | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5cacd164-6066-34f3-83c5-b8e4d4cef48b | -23.11353 | -52.07914 | 2026-08-18 12:00:00 | TERRA_M-T | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 6b6a315e-a1d6-3fa9-83ae-4f2976c33d1c | -23.52148 | -48.07305 | 2026-08-18 12:00:00 | TERRA_M-T | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 767676cf-96ea-3ec1-ab5d-d8d133273bfb | -23.10157 | -49.16793 | 2026-08-18 12:00:00 | TERRA_M-T | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 196b046f-1f46-3fb8-a24f-fdfe355fa313 | -20.28928 | -46.46525 | 2026-08-18 12:00:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| feda0321-df92-31ea-a02e-6ecbab910978 | -21.11317 | -45.59348 | 2026-08-18 12:00:00 | TERRA_M-T | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9276aefc-2784-3473-8350-945f9def807b | -12.7793 | -48.4205 | 2026-08-18 12:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 3259bcd4-19e3-3e30-862e-af204a39641e | -12.7597 | -48.4453 | 2026-08-18 12:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 10eff4dc-8e28-3018-aeca-de4946889155 | -14.1631 | -52.9113 | 2026-08-18 12:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 6a7259ea-438a-331a-8dfa-f5c89ee28f5b | -11.3606 | -46.381 | 2026-08-18 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 850c23bb-dbef-3b31-ba9e-64135bd195df | -8.5975 | -54.715 | 2026-08-18 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| fde47ebe-976f-3c3c-9d5f-f789194d9860 | -14.1628 | -52.9323 | 2026-08-18 12:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 37bd86b3-12a7-3630-aa76-7aa99c0b0943 | -14.1821 | -52.93 | 2026-08-18 12:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 01268ebb-5f51-3a27-8838-926bce4eb5db | -14.1824 | -52.9089 | 2026-08-18 12:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 94ad1e50-04c9-36ee-9c52-d42cf7b5ef71 | -8.5973 | -54.7352 | 2026-08-18 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 0701a07a-6127-33f9-a156-8d876ee9ba8d | -8.5602 | -54.7175 | 2026-08-18 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 56f1be85-3688-35bb-9a96-6055b45f1b5e | -8.5788 | -54.7162 | 2026-08-18 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 199.3 |
| fa1ce70a-e911-3d21-96b2-b04ed8b85e65 | -8.579 | -54.696 | 2026-08-18 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| d1734d78-2214-39d9-a955-69d1b49a29c9 | -14.1631 | -52.9113 | 2026-08-18 12:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| eda1cde7-2a06-34e5-a7a6-01a90d8a3cdd | -9.7709 | -47.2917 | 2026-08-18 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b09302e5-51c9-358f-adcc-62ab58c3e364 | -14.1628 | -52.9323 | 2026-08-18 12:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 145955ff-ad69-383c-9c92-9fe66cf168d1 | -14.1824 | -52.9089 | 2026-08-18 12:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 4a19f15c-5c86-39a2-8a59-18be309b998c | -12.7793 | -48.4205 | 2026-08-18 12:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 46e764e8-f03c-3f63-95f1-9a26926fd97c | -13.2808 | -51.6673 | 2026-08-18 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 9c7d1002-7807-33fb-a591-06c1e17a7f01 | -14.1821 | -52.93 | 2026-08-18 12:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| d0b0394e-8548-38b2-8183-c5a821f60459 | -12.7793 | -48.4205 | 2026-08-18 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 72d16f90-df22-343c-b331-de72999a7692 | -14.1824 | -52.9089 | 2026-08-18 12:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 4cc5fdfc-d6b5-3dcd-836b-e7e20a838090 | -14.1631 | -52.9113 | 2026-08-18 12:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 8a7e3034-68d9-3a64-a207-c038ce2d525d | -14.1628 | -52.9323 | 2026-08-18 12:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 20d6817d-cb50-3ab7-9afa-fa5f2e641b8f | -14.1817 | -52.951 | 2026-08-18 12:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1da53915-3f3d-3c12-a5fb-a1fe1357e732 | -14.1821 | -52.93 | 2026-08-18 12:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 47c782f6-38e6-38bf-99ab-396a0cd84e4f | -14.3521 | -51.9772 | 2026-08-18 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d822cc25-b1f9-3821-9a3e-937b3bbe0831 | -14.3525 | -51.9559 | 2026-08-18 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 3804b11a-109f-3609-8653-f883472c35a5 | -14.2566 | -51.9259 | 2026-08-18 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 4dc306b0-129f-3862-8e16-13c735a7e595 | -14.1631 | -52.9113 | 2026-08-18 12:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 71580ff0-89fc-3748-861e-d9e2b0603ac1 | -12.7793 | -48.4205 | 2026-08-18 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 155.2 |
| f1b20dea-5ec1-33d7-acc9-263e1b0ad3ef | -14.3525 | -51.9559 | 2026-08-18 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 59146d55-9c93-3c60-bf02-81a3098a9c7b | -14.1628 | -52.9323 | 2026-08-18 12:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| f4ac3c5d-2e6c-387a-a57c-88385827031b | -14.1817 | -52.951 | 2026-08-18 12:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 4c84cded-b3da-3539-891e-8bb10f115651 | -14.1824 | -52.9089 | 2026-08-18 12:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| e9359c45-dad1-35ed-aeb2-06f370038be5 | -14.1821 | -52.93 | 2026-08-18 12:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 207afe66-6364-370c-86f8-b40c562bf2d6 | -10.2765 | -50.4313 | 2026-08-18 12:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 7eba7862-1c52-3600-915d-549653b619f0 | -6.7478 | -59.1716 | 2026-08-18 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7a41950b-fc50-318c-aa95-553985bca81a | -14.3521 | -51.9772 | 2026-08-18 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 8299d052-d392-31c8-a68e-617804a539c3 | -14.3521 | -51.9772 | 2026-08-18 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 8c8b0f26-3ef2-31e2-babd-918b4b7cf4a4 | -14.3529 | -51.9345 | 2026-08-18 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 4d3c8549-606c-310c-84ee-6ae7764ea00f | -13.568 | -51.6953 | 2026-08-18 12:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 134.5 |
| eac9fee6-f212-3538-82a2-2171f7211b7d | -12.5399 | -47.8554 | 2026-08-18 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 5c230c20-7a16-3c54-ab02-cd43e7e81474 | -14.2566 | -51.9259 | 2026-08-18 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 02bb21fb-2149-3b2e-8d9d-b75ec6a5eb3d | -10.2765 | -50.4313 | 2026-08-18 12:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 06820c7d-a40a-36d8-ae12-7d8089bd87c8 | -12.7793 | -48.4205 | 2026-08-18 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 4bbe2c89-4400-3072-ae64-97e75536cc39 | -6.7478 | -59.1716 | 2026-08-18 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| fdda2a05-fbc1-3644-ba0e-a9af18526588 | -12.7789 | -48.4426 | 2026-08-18 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 219.4 |
| 8e3fb6dd-066e-3746-88df-fa2c8aeff9f8 | -11.3606 | -46.381 | 2026-08-18 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 5d435139-0b7c-3856-b5a8-fffbf10b624b | -14.3525 | -51.9559 | 2026-08-18 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 03dfd9d0-ff76-3cce-a051-99c4555ecad4 | -8.4899 | -48.821 | 2026-08-18 12:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 76.6 |


[Clique aqui para ver as próximas entradas](README66.md)
