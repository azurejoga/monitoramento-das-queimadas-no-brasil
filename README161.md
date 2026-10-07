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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db6e8787-d675-3933-a0b3-f73144595b5f | -6.92076 | -41.24237 | 2026-10-07 16:03:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 135.7 |
| 240b5a2e-9aae-3356-a5dc-68e892c0f273 | -5.22762 | -50.90188 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| a5f81482-80cd-3a77-9bb1-8ef97a0dc71c | -3.47332 | -44.77636 | 2026-10-07 16:03:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| a175c98a-9ade-3a8c-aec8-713701b2c3db | -7.04402 | -44.32745 | 2026-10-07 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b45eb130-8a51-345f-89e1-fb81af348597 | -3.54307 | -50.09824 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 7aa33fb3-9ba0-3825-9c71-58a5ef9a236b | -6.83972 | -39.55294 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 79374129-fe27-3fd8-9074-74e1007c238b | -5.735 | -45.14888 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0beb3768-6522-39fa-98f7-f3532a38285d | -5.97445 | -40.92737 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 3562c131-1025-3dd1-82da-bc60d9d3fa5d | -1.88767 | -45.4346 | 2026-10-07 16:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 1ce8c8c4-8ed7-32a7-8458-97c59f6d8dc5 | -6.89263 | -45.02421 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 07a73cf4-c62b-3a45-98d7-fdc926cfb071 | -8.01407 | -47.18061 | 2026-10-07 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 038ea22c-0479-3b57-b51d-7be955861890 | -6.6162 | -35.1609 | 2026-10-07 16:03:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| c7178934-b5f6-3a64-8ab3-ff24c1d9ffd9 | -3.51145 | -41.94752 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| e2170103-fd5e-319f-a1a1-1f6ddd201af7 | -7.69713 | -44.74557 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cb796538-0f88-34d3-bd93-f121bfee819d | -7.16906 | -43.71157 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 878e2704-ed07-34b4-b85b-6bfd53f465eb | -7.12394 | -44.06425 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 004ea1d8-9a29-3464-9802-434f30bed3ae | -3.55529 | -43.87897 | 2026-10-07 16:03:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| be4023af-13cb-35c8-b111-d35748537e5d | -7.00587 | -44.05533 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| faf2bd5a-a1c4-3b70-aae7-8eeaa14da5aa | -7.03501 | -45.42721 | 2026-10-07 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1fb2463f-edda-3e02-a086-c6b4335a4cf6 | -3.51331 | -44.9837 | 2026-10-07 16:03:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e298ee06-ebe8-3e5e-989a-8eecffda857b | -3.44686 | -49.25684 | 2026-10-07 16:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| be81ac52-c8f1-3358-b3cd-5b3b40c93481 | -5.96131 | -40.93738 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 8c3f2db0-93cc-381f-ba70-6563585815c7 | -3.19519 | -50.55241 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| a1abc93c-e8f1-3736-9802-090f0ecb87b6 | -6.02099 | -48.83046 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 85b0c4d9-b4ef-38bb-8dc8-8be1ceb9657b | -7.3386 | -50.82328 | 2026-10-07 16:03:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c018e765-f1ae-3d77-9930-08f44a4c8a35 | -6.82794 | -39.54357 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 22.0 |
| aa3c2286-a534-3f41-a151-5dccb3788d34 | -7.39035 | -46.20844 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e5c42ad9-0d70-360a-8855-31622a40419c | -4.241 | -49.9861 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 9fbf8722-596e-3121-aa06-e06f5f3f0831 | -5.25644 | -47.93174 | 2026-10-07 16:03:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 01785e2e-639e-3a7d-ae24-ada8fa281b48 | -3.8072 | -42.22097 | 2026-10-07 16:03:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| f8ad36dd-043d-3838-a790-2c6246b22b6f | -6.75792 | -50.96632 | 2026-10-07 16:03:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5d92bd01-0e19-3f89-97c6-99f4d516d5cc | -3.79597 | -38.59134 | 2026-10-07 16:03:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9b173cff-2671-32a1-900c-eebd1ddf4b7a | -6.98908 | -43.28999 | 2026-10-07 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| cd985091-15b8-3ca0-8b52-56aca55d85a9 | -6.37326 | -42.93112 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.8 |
| fd4aeffd-9066-3f31-abf1-d0bd45e5e38d | -6.26225 | -45.32787 | 2026-10-07 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6d1c087b-ba55-3d67-afcc-b800b81623e1 | -4.82938 | -40.72765 | 2026-10-07 16:03:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 7a433a8c-fe57-35d7-9b93-b082eea82034 | -5.47473 | -45.29602 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dc4c1e10-6af6-3f02-a4b0-675bffff071e | -4.52822 | -42.89082 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 789ccf1c-fb08-3d3d-ae8f-0e7ae468a58b | -3.51221 | -41.94437 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| f00c4770-f6ce-342e-a437-3634d5259ccd | -4.84282 | -40.39756 | 2026-10-07 16:03:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c024fe87-9734-3e8f-9c29-3710f1bc7aef | -5.72731 | -45.16215 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4cb8e2ae-47a0-3f5e-b4d6-2f7f25e7c989 | -5.23093 | -40.57885 | 2026-10-07 16:03:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 8b24f800-9638-3ec7-a9fe-4a18897bcb51 | -5.71945 | -41.67042 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| cb85a40f-b74b-3618-9b4a-68a5f1fd5ffe | -3.86945 | -42.28352 | 2026-10-07 16:03:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b21e619d-4206-3984-9385-fcef09d13472 | -4.83228 | -40.72333 | 2026-10-07 16:03:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 8fe5dfcb-f108-38a1-bd64-b5ac2a48c807 | -3.30265 | -40.08834 | 2026-10-07 16:03:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6ae8ea9a-429d-3915-b6a7-33feb764ce81 | -5.42209 | -48.31616 | 2026-10-07 16:03:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 07e70224-250f-3136-935f-ae9c7d15175e | -7.40241 | -45.64925 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| e739e1f0-6a24-3a50-8fb2-68bc0a8c03d1 | -5.73172 | -45.15891 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 244.3 |
| 5ea40b87-dc88-3cf6-8c8f-17fc17a56c0b | -3.25978 | -50.39492 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7d0421ca-efd4-36b3-b4d6-95d7aac87ca2 | -2.05146 | -45.97115 | 2026-10-07 16:03:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f84135b3-a784-3532-96c5-f2198a8fea9b | -6.07544 | -45.30838 | 2026-10-07 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bb46d98d-bcf3-3f17-b45f-1c9aadae41d4 | -3.76194 | -45.05161 | 2026-10-07 16:03:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c54b92e1-f713-3425-aae9-99abf07a5468 | -1.21829 | -49.04237 | 2026-10-07 16:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 13d3edf8-4bb9-3312-acef-a5ba10c20d84 | -2.81806 | -42.31207 | 2026-10-07 16:03:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0fe40e1f-de4c-384f-9524-bbc3282081ae | -4.28008 | -39.54333 | 2026-10-07 16:03:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 6275d94b-20a5-3d3c-9da9-ffe8092e5c70 | -1.09154 | -48.05226 | 2026-10-07 16:03:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cbea17eb-ec30-3525-8088-6e6172603089 | -4.36464 | -41.8209 | 2026-10-07 16:03:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| c7e1c740-1fc9-3791-8c51-02c99642e456 | -4.45854 | -37.81158 | 2026-10-07 16:03:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c4c258ee-70a4-3a90-9c4f-bd2efe20621b | -7.47178 | -42.82216 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 210ba536-b3de-3216-a556-a3da15c727c8 | -7.21445 | -44.2912 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 609bc1a2-89c3-3a4a-be84-0cd24fb4cd31 | -7.00095 | -44.0518 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 70843c27-d20c-3266-a6a8-7f6106d658b6 | -1.20537 | -49.03279 | 2026-10-07 16:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c9a28e79-92b4-3d29-8f1c-7cd0c2efed17 | -8.2162 | -46.34145 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 30e445bd-b893-37ea-a134-d58194b04b87 | -7.45877 | -42.99604 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 430788f9-7d29-38e8-9bc8-792b0eac1a86 | -2.78305 | -51.67854 | 2026-10-07 16:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ec27623a-3ee8-3cd4-8ef0-c485dc53c6b8 | -3.80683 | -40.45518 | 2026-10-07 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 16.3 |
| c005c11f-0c5a-35e8-a057-f6a7ad072920 | -4.34655 | -47.76474 | 2026-10-07 16:03:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f57c7457-b6f7-30c0-8185-a1b90d36cab3 | -6.84256 | -39.54884 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 772709dc-1387-3125-b8e3-b7e9e0aed6ef | -3.17987 | -50.55561 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 3537b85e-0c7f-3e29-b6e3-4fdbf36e6cd9 | -7.28583 | -47.29383 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 310c2d7c-5dc2-3be3-b734-f7022ef6e549 | -5.94066 | -46.63089 | 2026-10-07 16:03:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| acd647ed-0e3e-33dc-9821-774e7d19681b | -5.95388 | -46.35638 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ff62271-13c8-3f0f-a58a-ccb3b97ebc6e | -5.72972 | -41.73971 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 40b00465-cc24-3851-bb36-5ebad8938046 | -5.97142 | -40.95646 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 41.9 |
| fa045e3b-581e-308a-870b-57dc00a82ea9 | -1.09201 | -48.05545 | 2026-10-07 16:03:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c0fb5d0c-7069-38c8-b227-a6f4dd14d764 | -1.88638 | -45.42596 | 2026-10-07 16:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 190.5 |
| c5db74f5-0c3c-38cd-8604-ef0f020a3417 | -6.86671 | -39.10142 | 2026-10-07 16:03:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 120.1 |
| 5e7ea609-7ffc-3e37-9d86-6742f394cb01 | -6.99483 | -45.12309 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b9466aed-c0f1-307a-a322-b3781fd45fa6 | -0.952 | -47.63143 | 2026-10-07 16:03:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bdc2006f-6157-380b-9e53-9eeb7dd681a8 | -3.56159 | -39.46564 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b6d39c81-03ba-3bf5-9c70-4e5867f9f355 | -5.72321 | -45.16506 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4e23cc8d-72c8-312d-914c-4afa6c90bec1 | -3.35723 | -41.9142 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 61cc5532-1580-378b-9a69-d388124f197d | -3.23504 | -42.62243 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f6c15729-d6d8-3089-adc4-9fa4c216de08 | -3.91842 | -44.13489 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bcdc2420-da3b-3483-918f-411da880e851 | -7.53399 | -45.8786 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 201620de-fb04-3d22-80b5-d37917e6df20 | -5.97266 | -40.93988 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4c8c8f9e-e79b-34b5-99dd-1205e76a3248 | -6.94892 | -45.26094 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 644e4415-bb49-38e5-b837-354436210820 | -7.12459 | -43.91321 | 2026-10-07 16:03:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f4975dc0-a5c6-3f06-a03d-ad943b430d04 | -3.47857 | -50.08221 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 553b11aa-96ce-3dc1-b41f-38240e1e382e | -6.89254 | -43.68075 | 2026-10-07 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| c5b7fe1e-bc02-34d1-96f4-7d92310f39da | -7.20547 | -44.29455 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bae86c03-b8bf-349f-97f7-633f573ba350 | -3.11035 | -42.95232 | 2026-10-07 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 99b42e90-4319-36f8-a582-0a2122190676 | -7.39074 | -46.21138 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 67ec522c-d65d-3a1c-b53f-2f2f3fd6be24 | -7.00037 | -44.04765 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e41be834-0dad-318c-9058-2d3eadbe6ada | -1.21212 | -49.03942 | 2026-10-07 16:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 695724c9-eadb-38f0-b2e5-d5c7a675cb7f | -6.94625 | -45.27642 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 0e8e70b2-176e-3237-bf2e-85b73e227194 | -5.95348 | -46.35359 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70de94b5-268b-3d0a-a918-dbd0e85aa8b8 | -3.11107 | -42.95702 | 2026-10-07 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3fca665c-5b7d-3144-bc2d-434971972194 | -3.17615 | -50.55499 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |


[Clique aqui para ver as próximas entradas](README162.md)
