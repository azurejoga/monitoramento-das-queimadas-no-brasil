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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 067b3a68-5aa8-3525-ada5-6f53d21aa441 | -18.33192 | -44.03624 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4962cb64-08a1-3044-9ee7-6754c4c34d6f | -18.33142 | -44.01765 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0b73de2-8fdc-309e-b4ef-42e79bb9ddbd | -18.32993 | -44.26597 | 2024-10-04 04:10:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b4c6e62-017b-3744-b012-9c2ceea2328a | -18.56939 | -43.84243 | 2024-10-04 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 571b08f7-5ef1-32ab-a294-6dd66acf7e42 | -18.40421 | -44.46457 | 2024-10-04 04:10:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64ec53be-553c-3df7-a493-eeb38d898428 | -18.36882 | -44.03883 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3075864d-1e77-36d9-a550-79428264ff3a | -18.36826 | -44.04243 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9808963c-d85b-32b2-95b8-59e01d3cfd86 | -18.3108 | -43.91034 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 972832b5-00b5-3e56-bb1c-ec7f388e9113 | -18.26509 | -43.4329 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59193466-8198-31c4-85fa-fd0e92a96819 | -18.26896 | -43.42986 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e1335c4-1907-334f-bf1a-440d64d56b20 | -18.26454 | -43.43647 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99de4ae5-4aac-38cb-9885-487e893d9269 | -18.22317 | -43.2842 | 2024-10-04 04:10:00 | NOAA-21 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddf7cf25-5db6-319f-bee0-45fbb8bab813 | -18.21817 | -43.29473 | 2024-10-04 04:10:00 | NOAA-21 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7269f26d-db76-3de8-9ab3-229b916a53bb | -18.21484 | -43.29419 | 2024-10-04 04:10:00 | NOAA-21 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79f56bf3-7963-31fc-8f21-c07f6123c51a | -18.21428 | -43.29789 | 2024-10-04 04:10:00 | NOAA-21 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df7c3331-8c6a-37f6-b775-18cf4a5344ea | -18.31227 | -43.23367 | 2024-10-04 04:10:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8c8a8e75-eda1-31fd-87e0-b11ff2e4853a | -18.48104 | -43.41998 | 2024-10-04 04:10:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dfc15d42-530b-3474-b986-361894a0b9df | -13.89262 | -43.96378 | 2024-10-04 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db0bec7a-0284-3167-a58d-e3d517c601cc | -13.66144 | -43.72786 | 2024-10-04 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 771467ec-59df-3907-b7bd-9da21076df90 | -13.66087 | -43.73141 | 2024-10-04 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 27464bd1-12f1-3e70-a6ba-f7563daca175 | -13.54038 | -43.63151 | 2024-10-04 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 727c2c79-99ce-3180-b6a1-7ec165fa0178 | -13.48361 | -43.77491 | 2024-10-04 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 448ad95b-7f2d-3978-bc20-314ad82ff8cc | -13.4803 | -43.77437 | 2024-10-04 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61959e7c-7c88-326d-8913-c77e8aff8b57 | -9.5974 | -51.46074 | 2024-10-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 067e9d5d-3e33-366d-99e0-9cbc5b80ef53 | -9.59671 | -51.46441 | 2024-10-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f189d697-2d61-3f8e-ad18-53abd4ba728b | -10.55013 | -50.98114 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e505979-6425-3c1f-aed2-797d011adc23 | -10.54674 | -51.08287 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00005933-63c8-3fec-9df7-f775d0e39f64 | -10.54564 | -50.97727 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cebde04b-a1b7-3d3d-a188-f9e5eb509496 | -10.54508 | -50.98024 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f27d76b3-91b3-36ff-a3e7-27f074350b06 | -10.54224 | -51.07886 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed360e4d-54ca-3fb4-a4ae-875d65b97a98 | -10.54168 | -50.97652 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 35e7967f-b7ba-3145-aee5-a42c01e5ae96 | -10.54115 | -50.97949 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1cbc9be0-32f2-33cf-ba80-6ab554bab001 | -10.5406 | -50.97633 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 34f63233-730d-35df-86e5-1559177c8fa4 | -10.54004 | -50.97929 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 66fb4139-c9d4-3e0b-841a-10d12e2e394e | -10.53881 | -50.9636 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56c87dec-4e63-3ea6-aaa1-03428267b278 | -10.53827 | -50.96661 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a6877d0-f55b-3938-b002-5113768bd5a3 | -10.53782 | -50.96345 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0c7eef1-a693-34ed-94b3-c2a4fcc870ce | -10.53772 | -50.96961 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9818ded9-1531-32b1-bc6a-d1cdd9f182e8 | -10.53725 | -50.96645 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a2dce6e-bf0f-3206-b5ea-86676c66e682 | -10.53611 | -50.97853 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 83b64d12-270c-3b12-8f26-efc96879f575 | -10.535 | -50.97833 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 141596e8-3d5a-3845-93c2-dc86516e9c5f | -10.48891 | -51.12238 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d809c53-f84e-375d-b271-ee72de2bca1b | -10.48779 | -51.12852 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79eb4328-18b8-31d2-a6d1-5499b4fcf659 | -10.48325 | -51.1245 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13c177fb-8514-37ed-8130-144753632db5 | -10.67026 | -50.695 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25935ada-92a1-33b0-a6cf-e1b2853366fa | -10.46136 | -50.73529 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7419d5b3-11e7-3e0c-81ff-0bf35bde2c82 | -10.45692 | -50.73141 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce4f4da6-384e-3dd2-bf34-af857474e9a6 | -10.45641 | -50.73421 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a59f530e-85d1-32c7-b6b5-e1c3cb01ec48 | -10.4559 | -50.73702 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d6eeae8-5beb-3863-b974-c415af9514db | -10.45539 | -50.73985 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e065b48f-2fe8-37f9-aa75-ccec8ff167e6 | -10.45195 | -50.73053 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b4b00fd-6350-3fc7-8e31-dd1f5092f514 | -10.45143 | -50.73335 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c7afd84-e155-3010-8f02-3555f8261191 | -10.45092 | -50.73618 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 789907b5-ff88-3b09-8fe7-53e750afd22c | -10.4504 | -50.73904 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dbab9d3-0e08-363f-9b0d-38f7ef9e0e60 | -10.44727 | -50.75626 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9134651f-3b75-3bcd-a790-232c0de21a76 | -10.44695 | -50.72974 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0613e66-4e54-3381-9a62-aaf42e2bb8da | -10.44674 | -50.75914 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 139b694c-8149-3ebb-b35d-710f86022309 | -10.44643 | -50.7326 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc458102-e999-3314-9b2f-1c723ca53339 | -10.44591 | -50.73546 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 13512107-a5b8-3c7b-9649-1d99dc416466 | -10.44539 | -50.73833 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e4dac25b-3a89-3b16-80f5-0bf16a2bb693 | -10.44487 | -50.74119 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81f6aac3-c34d-35c7-a2fd-da3e7f4ef101 | -10.44435 | -50.74405 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4323eb2-a15b-3a8e-ae8d-f0e9c15d7d41 | -10.44383 | -50.74689 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65d0fb56-4cb0-3cfb-b7d9-bf9c9a1895ea | -10.44145 | -50.73176 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a0c2cd4-19a3-3a0f-974f-2cdf6e1d4479 | -10.44093 | -50.73462 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c04f70e0-eafc-315f-a7f9-3c8dc0619ebc | -10.4404 | -50.73748 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a206620e-0b14-3409-af5d-ba8c0373ac2b | -10.43988 | -50.74035 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3093383-6b87-3565-a0f1-4a90929d6bf4 | -10.43584 | -50.79069 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d62d78a1-9a36-39c0-8240-aa3a0712c959 | -10.43085 | -50.78975 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e350864-1a35-3777-bd47-d635ec516c9f | -10.43033 | -50.7926 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87f87cae-23bf-3a0a-b7cd-0e8ce76955f4 | -10.42982 | -50.79544 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09558bcc-faf1-3ffd-bca6-2fa88078ca3d | -10.42932 | -50.79817 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7479527e-6a02-38a8-a527-401159d2a603 | -10.42883 | -50.80085 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9fc5337-1c9c-3db4-9bf6-7c33bb16f10b | -10.42832 | -50.80361 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b5ff955-e4df-3f13-8386-fe68932e06ea | -10.4272 | -50.80976 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6dd886e-bc60-38b6-9d2f-d2361fefb530 | -10.42663 | -50.81287 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66bd0967-9b70-3e36-a2ef-8b2a3404ee0a | -10.42431 | -50.7973 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c83632d-0c5b-3ae2-aad7-677ed24c73e0 | -10.42381 | -50.80002 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6a9441d-5904-345c-a556-6b888893f43d | -10.42331 | -50.80276 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18c4cf3f-ecde-36a6-bb3f-1385e4b07944 | -10.42278 | -50.80569 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 93974121-869b-3b94-bd8b-cd94f745f042 | -10.4222 | -50.80884 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33ea9830-0c24-314d-ae9f-9d5e6ed8a551 | -10.42163 | -50.81196 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ad8617d-8c9b-3695-84ef-37860dc7e684 | -13.27622 | -51.25608 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a62edc46-6df6-38a1-b2ea-7c234d36c34e | -13.27133 | -51.25515 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33fa7440-179e-31c1-83f5-f8af148b2b12 | -13.16039 | -51.21288 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1871145b-e467-3953-8fbf-04291ae073b7 | -13.81452 | -52.44341 | 2024-10-04 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62c09563-0654-3121-9894-9a43b658cdf9 | -9.84166 | -52.06839 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29bc6188-065f-32db-86e7-d721d84b930f | -9.841 | -52.0719 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cb7881c-03f7-3674-82e1-806614cc0a63 | -10.92013 | -52.42086 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb3be413-8c37-3ef5-a68b-03fbaaf142b9 | -10.92002 | -52.42247 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e771dc72-a814-3e23-83f5-90fef17e5945 | -10.91941 | -52.42453 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ab473f7-6d88-3759-9dae-d267abd2fd56 | -10.91655 | -52.441 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 832ae6a9-e32f-392a-a00d-433639e56a17 | -10.91652 | -52.43935 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4c57976-446c-3c12-bd11-6e0cf9373c95 | -10.91521 | -52.41771 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20d48b5d-0175-3381-aa0f-f8b2ac64d0e4 | -10.91464 | -52.41974 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8500b2b-fda6-308a-b2db-9930778f0106 | -10.91453 | -52.42133 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5adf3aa-cb9f-3018-a455-c8493cff3fb9 | -10.91392 | -52.4234 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6725f09e-d944-3627-ad8e-d61e938d99cc | -10.91383 | -52.42503 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8e522e4-55e2-3ee3-9f36-a7c9621d7106 | -10.9132 | -52.42711 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5136741-efbf-34f7-b310-7596cf2bf2c2 | -10.91243 | -52.43253 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README79.md)
