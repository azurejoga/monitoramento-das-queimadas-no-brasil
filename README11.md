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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8259911-39d6-3cee-94b8-1152a1da1125 | -17.7091 | -46.8962 | 2025-09-02 02:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 0994df83-ab32-321b-b4fd-c61a14cf39f3 | -5.6079 | -45.0265 | 2025-09-02 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| dc81a0af-9e89-3359-8aec-3fb4f885d508 | -9.5913 | -40.3448 | 2025-09-02 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 6f152c92-0eb8-380f-98fc-75c842035a43 | -7.6783 | -61.0908 | 2025-09-02 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6839a964-5f3c-30ab-ad21-ec6a807fbe02 | -15.5666 | -48.3469 | 2025-09-02 02:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c05caf79-2427-3c5c-a79f-34c1b424a9d8 | -6.4029 | -58.2173 | 2025-09-02 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 00ef3c3a-4a0a-3e03-bc5c-c0170c8b0cae | -11.1037 | -44.6315 | 2025-09-02 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 72b27a8c-5abb-35df-938d-c83ccb643e9d | -5.6081 | -45.0038 | 2025-09-02 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 8b137268-8206-3706-84bb-f94529f0d588 | -17.9016 | -47.1569 | 2025-09-02 02:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 69707f5e-84c8-389f-bfb1-08c59f72eaa0 | -9.1207 | -61.4864 | 2025-09-02 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| c810dc0c-976a-3636-bd07-cab7accf3b00 | -6.8281 | -52.8143 | 2025-09-02 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| da67d526-4030-3bbd-a21e-922ef692b043 | -7.5476 | -61.3437 | 2025-09-02 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 0e8e9510-cd41-3662-86c3-e2c12baf3012 | -10.0617 | -48.1417 | 2025-09-02 02:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 67fe2d75-a45f-3d9d-bc05-08cac5f83134 | -6.8279 | -52.8348 | 2025-09-02 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 98b920d7-0cd3-367c-9571-cb055e949236 | -7.5477 | -61.3247 | 2025-09-02 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| ef34cbb2-55bb-3c03-99a4-5e30d3d362a0 | -8.6673 | -62.8369 | 2025-09-02 02:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 9c3b8ee6-8903-327b-8c01-03c35f26e60f | -6.403 | -58.1979 | 2025-09-02 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| faff009c-9e10-3fae-9aad-b98fcbccea76 | -11.1037 | -44.6315 | 2025-09-02 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 80ece3f2-ba92-3eb3-ade8-de3fa7622bbc | -11.6644 | -57.3733 | 2025-09-02 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 9e2509d0-a323-3b36-a4be-ccf1a4701fcc | -9.1207 | -61.4864 | 2025-09-02 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 6d645068-ace2-3817-a8f6-3cb38b38cea3 | -15.5661 | -48.3694 | 2025-09-02 02:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 6c0fa183-a3dd-3110-91be-71445329a2f7 | -15.5671 | -48.3244 | 2025-09-02 02:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a2e1781c-6087-3017-a994-13b605b175c0 | -6.8279 | -52.8348 | 2025-09-02 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2bccc6e0-2be8-371f-b237-0ed825ceb3e9 | -8.6673 | -62.8369 | 2025-09-02 02:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 41.7 |
| b1df1a05-d738-3cc1-bdf9-e81778535267 | -6.8095 | -52.8154 | 2025-09-02 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| dc4047fd-23e8-36a1-9c23-2e6899c5c135 | -17.9016 | -47.1569 | 2025-09-02 02:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8cd824e9-698e-3281-8e19-f2a84af60cf7 | -7.6783 | -61.0908 | 2025-09-02 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a2e34a3e-a33b-3036-b020-123e832c2a17 | -15.5857 | -48.366 | 2025-09-02 02:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 043b4578-298a-35ec-91f4-d15c238da722 | -5.6079 | -45.0265 | 2025-09-02 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 3baac766-beb3-3310-816d-24417b72561e | -5.6081 | -45.0038 | 2025-09-02 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| c334beeb-f8c2-37db-a7b5-13d2a38ac06e | -6.8281 | -52.8143 | 2025-09-02 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f71dbd4b-c5c1-3d57-80c1-37462573e00d | -6.7909 | -52.8165 | 2025-09-02 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 65614848-5f9a-3241-9723-bdb54df23435 | -7.5476 | -61.3437 | 2025-09-02 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| c35dc91d-50f2-385e-ad2e-a2cc1c35cd14 | -6.403 | -58.1979 | 2025-09-02 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 569553e3-baf8-3315-a908-4d6cd00c3f87 | -17.7091 | -46.8962 | 2025-09-02 02:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 7c27549b-1f23-332f-9b48-11143abc170b | -7.5292 | -61.3254 | 2025-09-02 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 478fef20-8d3f-355d-8c01-1ed38e8432c5 | -7.5477 | -61.3247 | 2025-09-02 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 86f42906-de43-3aa5-b1d8-0b93fc8ed43b | -6.4029 | -58.2173 | 2025-09-02 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8ad9f462-28d6-38d7-998c-4d3f92bf30f4 | -11.6647 | -57.3533 | 2025-09-02 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 9fa3f281-22bf-3e39-ab30-ed0f972bb72d | -3.2305 | -47.135 | 2025-09-02 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| b90ccdac-58ae-34ec-a3bb-57f72b6969f9 | -6.7909 | -52.8165 | 2025-09-02 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| a66b12f3-c6a9-39a3-9df7-d183b24277d7 | -5.6081 | -45.0038 | 2025-09-02 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a06a0278-04e2-367d-b936-5c02ca36a692 | -3.2305 | -47.135 | 2025-09-02 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 3f32b01d-d168-3f07-9f54-c0036625698c | -6.8095 | -52.8154 | 2025-09-02 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a2fa20e7-f757-349f-8dc3-2d6add667d16 | -10.062 | -48.1197 | 2025-09-02 02:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 3d471ef1-30e5-3064-a207-57025fb7f830 | -6.8279 | -52.8348 | 2025-09-02 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2c531922-8694-3639-be58-6689a22619f5 | -10.0617 | -48.1417 | 2025-09-02 02:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 42eca8f9-80d9-3de4-920f-376997145b5c | -17.9016 | -47.1569 | 2025-09-02 02:30:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 9b278ead-8aff-371b-a1f8-170abc73a4e2 | -6.8281 | -52.8143 | 2025-09-02 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d8555b87-5e20-3883-af07-66c90dd4c12e | -6.403 | -58.1979 | 2025-09-02 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| cfea0367-eb56-34eb-ae51-81bd3631f955 | -17.7091 | -46.8962 | 2025-09-02 02:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 59.6 |
| eec35398-8f4a-3aee-8ac8-87de2c3829c6 | -8.9664 | -65.9796 | 2025-09-02 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| dae378eb-cb20-3595-b141-e34afb860d71 | -6.4029 | -58.2173 | 2025-09-02 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 73e4828a-663a-33b3-927d-6db150f35469 | -5.6079 | -45.0265 | 2025-09-02 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| dbfd57a5-c702-3d64-a3a6-59b255cbbdd8 | -7.5476 | -61.3437 | 2025-09-02 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| af927d32-f99b-35ff-a2b7-ef867ac7b52c | -15.5857 | -48.366 | 2025-09-02 02:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 4b7c12fd-50b0-359b-b6f1-145dbe785ec0 | -7.5477 | -61.3247 | 2025-09-02 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| ca6afe70-f707-3706-8b84-2c042589d0fd | -15.5852 | -48.3885 | 2025-09-02 02:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a3b4af10-f60c-3421-9a0e-3be05bcc74d4 | -15.5661 | -48.3694 | 2025-09-02 02:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e73811e6-b32f-3892-995d-31cb86bccf0b | -11.1037 | -44.6315 | 2025-09-02 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a1c17b48-bc74-3687-abde-ab349137913a | -9.1207 | -61.4864 | 2025-09-02 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 674c0705-c46d-3228-97be-1700d92dfa50 | -14.2034 | -51.6558 | 2025-09-02 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 34cbecb9-36aa-3233-a2aa-7a3011d4c0ad | -3.2305 | -47.135 | 2025-09-02 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7e33cbdc-b2ca-34b3-b609-2ebe565e72e1 | -7.5477 | -61.3247 | 2025-09-02 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 7021c0e2-2282-32a4-a28b-078d880f00de | -8.6673 | -62.8369 | 2025-09-02 02:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 3e19433b-727b-3d58-aa2c-fd02ef4af35d | -6.7909 | -52.8165 | 2025-09-02 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 00f699f6-64c0-39c9-b4f3-31694aeaebd1 | -11.1037 | -44.6315 | 2025-09-02 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 46a1a7f7-ac71-31a3-9788-a85928469991 | -15.5857 | -48.366 | 2025-09-02 02:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 8e4dc7c6-67a5-3829-bd71-0b68edfc3ee6 | -11.6644 | -57.3733 | 2025-09-02 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f0e6ee21-7e77-3fec-8176-f272cfd67350 | -6.8095 | -52.8154 | 2025-09-02 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 61b407a8-24be-31c6-937b-d993629853ac | -17.7096 | -46.873 | 2025-09-02 02:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 1199eed3-8f1c-3525-85ea-823c4b5c6057 | -11.6458 | -57.3548 | 2025-09-02 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 89527f5a-e251-3393-b0a8-9f1f0b6eb8ed | -6.403 | -58.1979 | 2025-09-02 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| afb3ee77-09d4-3bb3-9e46-4bfc3d923032 | -11.6647 | -57.3533 | 2025-09-02 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e5a3b8a2-ee6f-388d-a452-ebf26fc38fee | -10.0617 | -48.1417 | 2025-09-02 02:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 7a577a9a-16af-3200-bf90-8f81ba4e5d35 | -7.5476 | -61.3437 | 2025-09-02 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 9a910391-c535-3bfd-aef3-af97b66a6f08 | -10.062 | -48.1197 | 2025-09-02 02:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 85c2f43b-efb6-3bed-a500-b559db9027d1 | -15.5656 | -48.3918 | 2025-09-02 02:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b256791e-39ba-31fd-9093-3412383641bc | -17.7091 | -46.8962 | 2025-09-02 02:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 638784f6-6682-3e09-b5a9-9faaa3c95b83 | -6.4029 | -58.2173 | 2025-09-02 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 9b0c28c5-4b1d-369d-975b-3fefd0beed0e | -15.5661 | -48.3694 | 2025-09-02 02:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 853d7887-9d61-392f-941a-2c5a3089c90a | -9.1207 | -61.4864 | 2025-09-02 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 773e7348-80cb-3169-a5b3-8ecbf658283d | -17.7096 | -46.873 | 2025-09-02 02:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 26cd78cb-1f6a-3f04-bc04-fb38a9880856 | -15.5661 | -48.3694 | 2025-09-02 02:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 9fb7757d-1111-3d8f-9423-4a3f0b94967c | -7.9915 | -46.4507 | 2025-09-02 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f2ed213e-22f5-33b3-a1d9-f4c8f294b10f | -22.6205 | -47.9297 | 2025-09-02 02:50:00 | GOES-19 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 409cdd43-634a-38a3-822b-469c63f9ed38 | -6.8095 | -52.8154 | 2025-09-02 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| aec15447-96ca-3513-83e0-0a63da68fcdf | -7.5477 | -61.3247 | 2025-09-02 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 44ea71db-3566-3086-917b-c4a51ab31653 | -11.1037 | -44.6315 | 2025-09-02 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| aaead384-618a-3aed-ac26-45e93f713252 | -15.5656 | -48.3918 | 2025-09-02 02:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 37cb769f-f63f-32f2-b2ed-fe48d151bf1a | -11.1041 | -44.6083 | 2025-09-02 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| e305688e-f447-3ac9-8494-945881a3763c | -7.5476 | -61.3437 | 2025-09-02 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 1b1b98db-0307-35ff-9911-a0231fbfacc9 | -6.7909 | -52.8165 | 2025-09-02 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d83be080-97e9-3ff2-95da-8cd5d0d74c71 | -3.2305 | -47.135 | 2025-09-02 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c4d0a87d-c81d-31af-81c2-eeb760f01599 | -14.2034 | -51.6558 | 2025-09-02 02:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 4c467f19-9cf2-35b3-9ce6-6f293dfebdf1 | -9.1207 | -61.4864 | 2025-09-02 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0d1b03f4-8125-3cd7-8270-689095b352d7 | -17.7091 | -46.8962 | 2025-09-02 02:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 81820ae2-1816-3baf-8fda-1f3f106486b6 | -11.1033 | -44.6548 | 2025-09-02 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 08f43329-cb1f-3287-8bf9-2e911362ca59 | -7.6783 | -61.0908 | 2025-09-02 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 09ea9c97-5e21-395f-b4a7-c3cf5097c12f | -7.5477 | -61.3247 | 2025-09-02 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |


[Clique aqui para ver as próximas entradas](README12.md)
