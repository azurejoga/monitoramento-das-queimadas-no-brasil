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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7984bf3-7503-3f5f-b7e4-32e153a0d962 | -7.65727 | -45.38183 | 2024-10-24 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d6d8f8c-3a2a-3d28-93d1-aae0a3ea7f75 | -7.65659 | -45.38566 | 2024-10-24 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2322af95-f0b6-3898-a4a4-74fc7635e1ed | -7.65589 | -45.38966 | 2024-10-24 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e24ff9f6-0ef3-39c3-937a-e299fb200bbf | -7.65584 | -45.3807 | 2024-10-24 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7826c4c-5c41-36ac-89ab-aaeeb4e86734 | -7.65514 | -45.38452 | 2024-10-24 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e672e16-d8ff-367d-b8c4-e0a3b8d3369c | -7.56683 | -43.46068 | 2024-10-24 03:40:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c22574a-f2b5-36a7-9cfb-d99489a355b2 | -7.56434 | -43.46492 | 2024-10-24 03:40:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 62d43269-cf19-39ce-9fc7-96d6ed391135 | -7.56193 | -43.4598 | 2024-10-24 03:40:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51bdc15b-d385-3045-b47f-cedfe14caeb1 | -7.56091 | -43.46548 | 2024-10-24 03:40:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8adea8e-0efe-3c72-9d2e-03aa83b45c58 | -7.55326 | -38.74535 | 2024-10-24 03:40:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 799623fc-2b1b-3e92-82e9-47ed77efe6db | -7.55255 | -38.74963 | 2024-10-24 03:40:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9f6acf32-d2d2-3159-986a-da13842398ff | -7.54646 | -43.19178 | 2024-10-24 03:40:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5b6ef0b2-f4ee-33cb-9f29-0f282f6c9745 | -7.43095 | -44.73446 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85a6117f-740c-3688-963a-751b350c6cff | -7.42886 | -44.73158 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf65721f-df8b-3101-b812-708215404f29 | -7.42824 | -44.73497 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f39eb871-cb19-319d-a804-08696d05382a | -7.42617 | -44.73017 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9a22c8f-1307-334b-a793-119149172b98 | -7.42557 | -44.7336 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6982358-aedc-3bf0-a51c-e7743b08fc33 | -7.42496 | -44.73706 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6331c387-227f-3be6-afa5-1676630c854e | -7.42124 | -40.34662 | 2024-10-24 03:40:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8f69d722-7c0e-3569-8b17-a6c3cf7e3f11 | -7.41483 | -44.73178 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 201dda21-de7f-3076-a49b-74353423d1fb | -7.40944 | -44.73098 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 984409c6-100f-3fab-9b0d-51dd46f82019 | -7.4034 | -44.73387 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fb5f9e5-0ff9-3bf5-ae17-e4c10ff2464b | -7.33671 | -39.33067 | 2024-10-24 03:40:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 53317253-7d64-3309-9936-e420fd3bde80 | -7.33295 | -39.33009 | 2024-10-24 03:40:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99829c99-cafb-3f1d-95b9-3ea338c807bf | -7.32088 | -39.333 | 2024-10-24 03:40:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4c4164e6-7e1d-3c81-9091-20ef14360e72 | -7.30507 | -39.14165 | 2024-10-24 03:40:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 3d816e1b-e7bc-36d8-b3c3-d4ac7f6bfa5a | -7.3021 | -39.13644 | 2024-10-24 03:40:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6df7eede-5c10-3ddf-b071-7f48b5f1d711 | -7.30135 | -39.14107 | 2024-10-24 03:40:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| bd609158-8d57-3663-b6ba-5d565abf9541 | -7.13576 | -39.27806 | 2024-10-24 03:40:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e321881-f061-3e74-83e1-dd252718e0dd | -7.09468 | -41.13638 | 2024-10-24 03:40:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| da58fcf2-99d8-3db9-a927-dd52bc853527 | -7.0862 | -37.19316 | 2024-10-24 03:40:00 | NOAA-20 | CACIMBA DE AREIA | PARAÍBA | Brasil | 2503407 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9ee6a612-3fdf-3b02-a978-8513ac62dedd | -7.06951 | -42.55839 | 2024-10-24 03:40:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 685b8720-bc92-3bcb-9b06-fabb49ca85ee | -7.06865 | -42.56349 | 2024-10-24 03:40:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4652055a-82a3-3ad2-be42-6e4f93e0b8b6 | -7.0671 | -42.56001 | 2024-10-24 03:40:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 4fdcacb1-a71f-3fc2-962a-41cf31df1786 | -7.06485 | -42.55758 | 2024-10-24 03:40:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8ef97b46-f5fa-3b33-8efd-4e5529282fe9 | -7.06399 | -42.56264 | 2024-10-24 03:40:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3a2c0f57-aff7-379a-bc71-1ce41f1a57d2 | -7.01855 | -40.05782 | 2024-10-24 03:40:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9a887e19-0101-3e39-bba3-d00f565d50bb | -7.00052 | -41.3065 | 2024-10-24 03:40:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 269a94b5-a4af-3725-8117-9a80fc56b143 | -6.99625 | -41.30574 | 2024-10-24 03:40:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf19b1c3-9252-3889-a366-5b44573337fe | -6.93996 | -40.84708 | 2024-10-24 03:40:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c6d89533-9d59-378a-b16d-56492e91196f | -6.93646 | -40.84258 | 2024-10-24 03:40:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0487825-a926-30b0-8d5e-b1c8c8cb229c | -6.93582 | -40.84631 | 2024-10-24 03:40:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 41a2df47-7769-322b-ab2d-a016f6fd523b | -6.93517 | -40.85011 | 2024-10-24 03:40:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7d07c78a-e198-3f45-b3d1-1f7d00a4a0a0 | -6.93231 | -40.84185 | 2024-10-24 03:40:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3620c2e-2e61-3455-b1d4-7d6631f68d12 | -6.93168 | -40.84557 | 2024-10-24 03:40:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aea46475-f47a-3c72-91ee-4f2a3f827063 | -6.93103 | -40.84935 | 2024-10-24 03:40:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c8f40271-5112-3074-9bd8-01e526b7d9ec | -6.87811 | -41.91513 | 2024-10-24 03:40:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 044fba0a-db1b-32f9-b650-ec2935bb83b1 | -6.87732 | -41.91969 | 2024-10-24 03:40:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ac26329e-6b1e-30e2-a75e-735de6fa3922 | -6.857 | -35.22636 | 2024-10-24 03:40:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 70473e29-abce-3165-8af3-68f3cb3e3b26 | -6.8537 | -35.22584 | 2024-10-24 03:40:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 04621a73-3087-3a87-8125-5da1838bad49 | -6.83482 | -35.15208 | 2024-10-24 03:40:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0cf4f1ed-d7f3-3b96-9aff-639d3c94a8c4 | -6.83427 | -35.15553 | 2024-10-24 03:40:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 6b38fcac-d49d-3298-9ba2-062661a660d5 | -6.83206 | -35.14811 | 2024-10-24 03:40:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a8705a8c-9bd7-36b3-9ec6-360728ae5e8e | -6.83151 | -35.15156 | 2024-10-24 03:40:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 099d2178-8c2c-37a7-8340-2001240d346a | -6.83097 | -35.15501 | 2024-10-24 03:40:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d1d5bba5-4d12-3fd7-8565-09e02b4df771 | -6.73255 | -40.49776 | 2024-10-24 03:40:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 88bb57b5-c82e-3126-956c-0e5441252444 | -6.73209 | -40.47535 | 2024-10-24 03:40:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc734d86-7374-3db4-ad9a-26e5c81e5af0 | -6.73194 | -40.50139 | 2024-10-24 03:40:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 40c75deb-a70d-37af-9a96-6ba736cad099 | -6.73149 | -40.47894 | 2024-10-24 03:40:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9474baf6-2a4e-3690-a4f0-79002420eb1e | -6.73089 | -40.48255 | 2024-10-24 03:40:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2ba9763f-4a53-3843-9300-e124c5ce8134 | -6.73029 | -40.48617 | 2024-10-24 03:40:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 543d18a4-4575-3535-aabe-8b7646285117 | -6.72743 | -40.47822 | 2024-10-24 03:40:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 79085794-593a-3446-ab1e-0d66d29378c7 | -6.71871 | -37.51146 | 2024-10-24 03:40:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 23240229-20a1-3df5-8e86-a2b4b32c312f | -6.6994 | -43.05676 | 2024-10-24 03:40:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| caa20551-8b1a-336a-8d19-022f1b66a206 | -6.64753 | -39.62661 | 2024-10-24 03:40:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 438b28a9-2fd2-35cb-9028-6552fa81c055 | -6.50657 | -35.25221 | 2024-10-24 03:40:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b572960f-2948-3fcf-b3b5-a129ac48c636 | -6.50602 | -35.25566 | 2024-10-24 03:40:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 053d0801-8e98-3fd6-b870-a4d9357e66e7 | -6.50326 | -35.25169 | 2024-10-24 03:40:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c598e75d-7c05-3530-a03b-f2fd19b3bb4a | -6.50272 | -35.25514 | 2024-10-24 03:40:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 11.7 |
| a4bbc60e-3316-31e6-8fb0-4fb7352f90db | -6.49942 | -35.25462 | 2024-10-24 03:40:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6bd7875f-471f-3cc3-9a27-08cba0a5d4e8 | -6.28871 | -43.3751 | 2024-10-24 03:40:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 058f6fee-dd08-3ae1-8515-1126463cbf5d | -6.28821 | -43.37791 | 2024-10-24 03:40:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c154830f-2757-34c0-b0d0-c0b59cf00135 | -6.19294 | -43.54223 | 2024-10-24 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 077ac1a8-f69e-37e6-96aa-099880287f64 | -6.18935 | -42.27662 | 2024-10-24 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2eaf26e2-1dcb-3c38-a3ac-ee770c01e93a | -6.17702 | -42.60948 | 2024-10-24 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7f1bba09-3f8e-3e0b-be8b-a3fe0a77dedc | -6.17611 | -42.61466 | 2024-10-24 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0cf5c13c-5929-3096-86f0-93b1d046d951 | -6.17577 | -42.61287 | 2024-10-24 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 710ca7c3-88e4-38cd-b3c7-57d2edaab81f | -6.17123 | -39.41236 | 2024-10-24 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a8fe5894-b5e5-3630-b653-0963f67c5dab | -6.09756 | -43.8769 | 2024-10-24 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aafae03-6b67-37b7-86e2-80b4fd5e7a32 | -6.097 | -43.88004 | 2024-10-24 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f57bed4f-6ad4-3067-92e2-92f9397b9a2b | -6.09294 | -43.87281 | 2024-10-24 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caa3d454-6c3c-3b92-bfc1-052d98aea959 | -6.09239 | -43.87595 | 2024-10-24 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54e70583-351d-39b2-82a4-f5d5c5ee94cb | -6.01099 | -42.22073 | 2024-10-24 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cc1560b9-93ea-3e71-b384-4c37c4dd4b7c | -6.00636 | -42.2199 | 2024-10-24 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eecbbd79-9bc9-39e2-b188-8e740cd3fb01 | -6.00173 | -42.21909 | 2024-10-24 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e8d96406-3f58-3955-b923-1a8e1f1c30b1 | -5.96148 | -35.28246 | 2024-10-24 03:40:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 23860385-69ea-3517-8557-cd44d8cbaf34 | -5.90279 | -42.89127 | 2024-10-24 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 16a1ff09-617e-3ceb-9a12-bbe75ba61ccf | -5.87868 | -38.23576 | 2024-10-24 03:40:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 63848179-e4b5-38a4-b5e4-4783365b7848 | -5.87232 | -40.17452 | 2024-10-24 03:40:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aea89312-057e-36a1-bc6e-955f4afcc512 | -5.72472 | -35.6427 | 2024-10-24 03:40:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2d904b80-018c-38ee-8902-e215b52a7b3d | -5.71139 | -43.82994 | 2024-10-24 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e0358219-3ab6-3017-b8e8-4709260b5981 | -5.50743 | -43.69948 | 2024-10-24 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 372c6f18-aa09-311e-b2e0-52f103bdee1c | -5.50689 | -43.70263 | 2024-10-24 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e87d3dc-6b45-375f-86e8-a1c2bf18f571 | -5.50634 | -43.70576 | 2024-10-24 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba64841f-8d0a-351d-8642-dfa722c97b01 | -5.45732 | -43.27304 | 2024-10-24 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09607c8f-6aa6-3278-a22a-3fcd84673d07 | -5.32212 | -42.98075 | 2024-10-24 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2074bc14-84e3-3a8f-bd8e-441a23b08be7 | -5.32114 | -42.98652 | 2024-10-24 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9ebfa125-902c-3a73-925d-4028328e2176 | -5.27441 | -41.2021 | 2024-10-24 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d4528a61-3b83-3265-ac07-1fdd3f779c0e | -5.25655 | -43.99753 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 95d531df-0f5d-332d-8d5c-06aa235310b2 | -5.20638 | -39.00048 | 2024-10-24 03:40:00 | NOAA-20 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README18.md)
