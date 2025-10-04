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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4e089a6-7b4b-3114-919f-c80c0b2374da | -14.19878 | -46.07276 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ba18b02b-295a-3baf-ba92-8fd15e4c7ce3 | -13.18107 | -50.9281 | 2025-10-04 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e909aa88-de5c-38ef-b77a-9042e5b47dbe | -13.32808 | -47.79255 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fbe65e3-475c-3fb3-8f32-825c97ee4552 | -11.91238 | -46.36624 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1854a454-4f65-371c-b917-de66fd29faa0 | -13.32136 | -48.12347 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39a35d1f-fa68-3889-9b48-f37e22ea087a | -15.61645 | -46.94194 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8e8f862-52cb-32a1-8d2d-d6cf30f62fef | -13.33957 | -47.61879 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b0ceed8-8d97-336b-9e2b-f6ca4a6d7764 | -12.10697 | -43.44583 | 2025-10-04 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84f73ec6-60d1-3854-a5ba-ef4facc12d08 | -12.23067 | -43.7691 | 2025-10-04 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 034133e5-f6e8-305c-baa9-085d48ed1ec4 | -11.54605 | -47.68449 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2353a64-5c70-38f0-82db-68c139fbf597 | -13.3358 | -47.19555 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a233cb74-2f02-34e2-bbd7-aa4bab909b1a | -11.56372 | -47.68117 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c1c2e9f-dae5-31f5-b87a-36e153e97713 | -11.82299 | -48.07199 | 2025-10-04 03:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 269b6c71-13a1-37ce-85c2-416e0e12ef37 | -16.69658 | -48.89396 | 2025-10-04 03:53:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f133e05-2eba-360e-a8ac-7e28b5d1afa5 | -13.12634 | -47.81976 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0ca9232c-d0b7-34ec-922e-7b04c414709f | -13.30494 | -47.57183 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11e02769-06ca-3c24-9c82-46f970de044b | -13.70485 | -47.34986 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6282c20c-8e45-36bd-96c9-e99150d15b60 | -11.90743 | -46.3651 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8e31b78-aa51-39c6-bf5f-06371dd908f5 | -13.701 | -47.34217 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| befd47da-fc4c-3990-9222-430d47bd246a | -13.73205 | -47.92044 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 573a9078-6db3-3c42-b71c-bf202cc8b91a | -17.07584 | -43.36487 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe7608bc-433e-3243-904b-1a5a4fd6b833 | -13.31113 | -47.26612 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36d1ae9d-4343-36c5-835b-e374c29487df | -15.29912 | -46.28945 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 751e749d-2fda-36c0-8bb4-d5056f2783fd | -13.15801 | -44.64038 | 2025-10-04 03:53:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a59e672-38f2-3083-b5d0-afe718729605 | -13.38993 | -47.55156 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ca0f14b-484b-30f1-ba74-881de6bef4c6 | -17.62358 | -46.69938 | 2025-10-04 03:53:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d3ef82b-bb6e-3802-bb53-42476e217d05 | -13.13494 | -47.83259 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01d99eb6-d569-34b4-9490-4e8181735788 | -11.49294 | -46.75662 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fbb4c95-2b65-3f44-8555-c9e38a5c05e2 | -13.57725 | -48.17871 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed9c05f7-ac14-393e-875c-4c2f4e56175c | -12.39871 | -46.51147 | 2025-10-04 03:53:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e744abcf-f3a8-390b-a61d-a17c9cf96fb1 | -15.68824 | -46.27021 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 28c39c5c-1d5e-387a-8e63-d9f938448cc0 | -14.19579 | -46.06802 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 77150fd1-4925-3a10-a22f-12c461e8707a | -16.02529 | -50.94392 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8ff86b9-a9e6-3d59-9c52-c09b3a44e7f1 | -14.92543 | -46.8946 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec582f0c-467d-32d0-9d60-2998e8e6de6e | -15.79549 | -46.26108 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16159915-c6d1-330e-bd20-9743688d2812 | -14.65612 | -48.24099 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23dc6f5c-2a81-3292-b468-5188195e187c | -16.39052 | -52.16232 | 2025-10-04 03:53:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ab561cb-2539-3384-af73-83bbad7d87c1 | -13.11081 | -47.89793 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d82afc3-5052-3fe0-bf03-76404e01c28c | -12.30899 | -45.37876 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2b01cea-b5b4-38da-83de-003b0e297454 | -17.15582 | -47.02814 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 195fd2ec-32d8-37e7-8ef4-9ee6f4ae2939 | -13.72838 | -47.925 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b5e7b93-8024-3130-8a61-d029fde7d8b3 | -14.38626 | -45.96898 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 688f2478-fd95-323f-82c9-6856ff0f97c2 | -17.0071 | -49.15354 | 2025-10-04 03:53:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8500629-a76c-310e-aed7-c7554bfab966 | -16.06348 | -50.90627 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 652f66a9-f615-33e9-a107-cfa6760af667 | -14.23378 | -46.09829 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80fe4f7a-8a05-318f-9f5d-50c1906984de | -13.58343 | -48.17611 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70c89355-b3e0-33a7-aeb4-bd2414450654 | -12.92953 | -45.07392 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57b552ed-6100-3959-a7b7-41fb71a841c0 | -13.08312 | -48.12271 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e22d36d6-7c33-3908-9ff0-157196b369af | -14.92279 | -46.88221 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6257dd98-e4d0-3549-b81e-a234bec6355a | -15.37915 | -47.95673 | 2025-10-04 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b749d58c-fa4c-3658-b8ab-7bd2cc452cae | -15.96147 | -43.33443 | 2025-10-04 03:53:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b86a27c8-0038-335c-ad10-23cb2ff01313 | -13.11083 | -47.92608 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b484fb80-2353-3b97-b0b7-a11e92b3ed01 | -14.94384 | -49.97588 | 2025-10-04 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e17dda87-bddf-35a3-ab0c-fb0de7de385e | -13.26225 | -47.21157 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eec40147-86a4-3aa4-af4c-70b5b4007953 | -11.86648 | -44.97292 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99345b4a-07c6-31ef-ad94-721b3c97141e | -17.0818 | -46.2314 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4decce1b-19f1-3877-89f1-9705ffad844b | -13.99094 | -48.18221 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a567e6e3-b4a7-360b-b461-2a7bb065fa7d | -14.60094 | -46.72927 | 2025-10-04 03:53:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3abec538-7bd1-3439-b6be-7900f71a5a28 | -13.34501 | -47.2029 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bdad1d2-d9e2-39f0-8fe0-73072199114a | -17.96091 | -44.25976 | 2025-10-04 03:53:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89788c11-df1f-38ed-9eb2-69e904b3177d | -11.82967 | -44.9178 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c056380-be59-3d17-b36f-5fe96dfa2b9c | -14.87588 | -48.36071 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08bf4319-1dac-3e98-a100-f179f1152a9a | -15.52492 | -46.83123 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dab30c84-54b0-3bd5-a31f-6df35e09e85b | -16.01916 | -50.94244 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 150cc0c4-5f1b-3e8f-9718-3cac9d1c9f1f | -15.03314 | -46.97602 | 2025-10-04 03:53:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8a261223-4918-3c9b-997d-5d2b0b4276a6 | -14.68272 | -48.27507 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e9acc53-264b-3a11-b415-1ea73e0b0cf0 | -13.1363 | -47.93923 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24f0917e-4628-3726-af0c-a2809c6e2538 | -14.66786 | -48.29334 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.4 |
| d89c6c6b-ceeb-3ad3-b80a-897fd3f1172b | -12.09301 | -45.14974 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 248af7fd-7ab7-3d09-bc01-e24c8ccbe0aa | -11.84497 | -45.0391 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df1e4d01-a113-34b9-bb63-3573de8e37af | -13.65618 | -47.29836 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c9a6b95-e03f-3643-9edd-cf34be9d09c4 | -13.65671 | -47.29567 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b738ddd1-8be4-340c-9e55-48ecf331d33f | -13.57698 | -48.17982 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e62fc3db-3466-33d7-89c8-11a0b7c67428 | -14.84489 | -48.28395 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec94abf8-2766-3a43-8821-da3e7a7daa2b | -12.20251 | -47.77928 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 956dcbec-5459-368b-9d63-72b9d029cb1c | -14.97104 | -47.26488 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 05616bca-97de-3832-9d8d-15c3504d511e | -13.46781 | -47.26526 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ee2c2909-dc0f-32a9-81da-30665ce42e51 | -14.57589 | -52.48524 | 2025-10-04 03:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cf5e60b-3f57-3059-8e93-b7ce1a919cd0 | -14.64936 | -48.23847 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ce94c67-d3fb-3306-a39c-8571cc1d4c1d | -14.21793 | -46.07935 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a6f0eeba-c9f2-3a22-bc7c-84b3c281a2ea | -12.94715 | -50.98804 | 2025-10-04 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca116ef2-b2dc-3b82-95fa-0104a697b7c0 | -13.74778 | -48.06479 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7664d2b0-c76d-3681-82a5-656be628ce9b | -15.53004 | -46.80488 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76714d7e-8065-3a2e-bd9a-74681455d1be | -14.32198 | -45.86135 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f2b0347-4b5c-3c01-8116-ac36032f6495 | -13.25566 | -47.24541 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47662d81-ff3a-3188-857e-e7a97f8b7b81 | -11.79047 | -46.83897 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f997b4a-b50e-3b42-81a3-c1e333e16485 | -11.78997 | -46.83466 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd24569e-a30b-3c55-bad9-71f6bbc93e49 | -11.92732 | -46.36919 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 15e59398-0a3c-3691-bf76-36d46ecc1c72 | -13.09995 | -47.88795 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a74e7f35-86a6-32c4-8d69-e74f4f38a2e6 | -14.28124 | -45.87425 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 307d2320-57b3-304b-9095-d784d6cec8d3 | -11.24614 | -47.80381 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 08eb47d5-e925-304c-b939-f1d70625a677 | -11.82718 | -44.93124 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87e760ef-f6ec-38b4-9df3-7baf4b26bae4 | -13.34279 | -48.07206 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76468ab5-2801-3372-956d-f39acbe335f5 | -13.10554 | -47.89626 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8864755a-98f0-32da-9773-ba6e73a7831c | -15.03017 | -49.45357 | 2025-10-04 03:53:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8584743c-bfd0-34dc-a2a8-72e7f26a13ef | -13.33417 | -47.19807 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9de1aa2b-e2a6-3049-b3f9-0abffdc4787e | -14.28719 | -47.41568 | 2025-10-04 03:53:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5480adb0-13d3-3176-98d4-9d3e7f55ed56 | -17.14998 | -47.03269 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f37d130-1483-3b71-9d2c-64e41f9dcb30 | -14.90807 | -48.28402 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 693302b3-47b0-3108-b24a-cb442b2234a2 | -12.91787 | -46.92282 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README45.md)
