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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| badb4e1d-5f05-38a6-8ef7-61c2d0134e7a | -11.4852 | -43.55954 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff572457-81b0-323c-a908-134cb970ab07 | -14.97197 | -44.43739 | 2025-09-21 03:17:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d518c150-8ff3-34d6-a6e4-1acc981e89b7 | -12.32946 | -44.10629 | 2025-09-21 03:17:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc691bef-2702-3e54-96c0-91c9fd364e8d | -13.24859 | -44.12005 | 2025-09-21 03:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e8a3f16-9bdf-3c01-b7a0-42dd3e474852 | -13.53739 | -43.01668 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 607a738a-a845-3f6e-9bda-6b328e370590 | -13.53183 | -43.01196 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 1e7c73ae-2140-31f5-9e18-03f74204935e | -11.2809 | -41.8559 | 2025-09-21 03:17:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4190ac1a-3ad4-39df-9e63-b90c33d5bd7e | -13.53425 | -43.00068 | 2025-09-21 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| d385dcf9-a025-3a66-816d-e95912b0f660 | -13.68059 | -43.81693 | 2025-09-21 03:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60b07a4a-30c6-342c-b092-a10d576687ec | -11.49976 | -43.59519 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c07b4fe-2334-30c5-a4b4-0059f5f62378 | -11.45289 | -43.54361 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fb09ed7-7365-3f2e-a7d8-6f9e14e8d21b | -13.35591 | -44.28191 | 2025-09-21 03:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fea4edd9-c67a-3f39-9ca3-83b1dd1c9bad | -11.20996 | -42.19698 | 2025-09-21 03:17:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 68622c11-2252-398e-9b6d-b34e40dc92b4 | -11.27466 | -41.85453 | 2025-09-21 03:17:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f4c944a9-b77c-3e15-aa8c-f4d7ae7b4aab | -14.97368 | -44.43317 | 2025-09-21 03:17:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbe0d8ca-e3f8-3485-acb4-cb5c95f131f3 | -14.96976 | -44.41879 | 2025-09-21 03:17:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8cd38c35-0a4c-3760-a480-c56b11213174 | -15.53088 | -42.1777 | 2025-09-21 03:17:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7e2259f-e76b-320a-86bc-a8e2ab5264ae | -11.27802 | -41.85369 | 2025-09-21 03:17:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 03156bb0-e431-3c62-a58d-df7c30083170 | -12.33573 | -44.09968 | 2025-09-21 03:17:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d62a2b7f-1cf3-3db2-a2f5-71109666db8e | -11.49346 | -43.58853 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7eac2ba0-4c4b-3eb6-b509-27560f4ff959 | -13.35739 | -44.28262 | 2025-09-21 03:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cc7b97e-84ef-39b4-947a-eee4e901b091 | -13.36133 | -44.29031 | 2025-09-21 03:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 306d3069-1e7c-34a6-8802-7aa7fadfff44 | -11.48386 | -43.5659 | 2025-09-21 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 591e9361-e30f-38ff-865f-61fbd3420e37 | -15.48486 | -41.92231 | 2025-09-21 03:17:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dcdb6daa-7112-325b-8e0f-dbba0faa783f | -12.33092 | -44.0993 | 2025-09-21 03:17:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91472d7a-9ee4-3b8a-b358-6859b2f7505d | -20.13545 | -42.48557 | 2025-09-21 03:19:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f676afe5-8e19-3744-80b7-97a127240d0d | -20.75989 | -41.91041 | 2025-09-21 03:19:00 | NOAA-20 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1b2e1011-443d-3fc9-8dce-27ab253e03ab | -20.13386 | -42.49291 | 2025-09-21 03:19:00 | NOAA-20 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c16e10e0-c180-3517-8f6d-2e7719233280 | -20.1347 | -42.48902 | 2025-09-21 03:19:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1f76897d-3998-3fae-bd90-9e164258409d | -17.43669 | -44.80243 | 2025-09-21 03:19:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c446557-bdfc-3efb-bf9c-e965d3fc1e6e | -20.53695 | -42.27585 | 2025-09-21 03:19:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6a9c4a4b-c87e-3476-92e5-18b179d0e07e | -18.90297 | -44.28487 | 2025-09-21 03:19:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 946bbb19-e216-3470-882d-da73d6c01a06 | -21.69298 | -44.26989 | 2025-09-21 03:19:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3f28c84a-d65e-3a94-ab84-43251d8c7983 | -21.69039 | -44.27074 | 2025-09-21 03:19:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74872779-694e-3cb1-a203-a2d9c188aae6 | -20.53784 | -42.27181 | 2025-09-21 03:19:00 | NOAA-20 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6ff5283c-a2eb-36a6-8382-6e36a78267c0 | -20.13262 | -42.49281 | 2025-09-21 03:19:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 95c0f575-991f-3829-a00e-64b88f69ce90 | -18.83215 | -42.17781 | 2025-09-21 03:19:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8ac8ae60-505c-3ab1-ba01-bf31429dfe5e | -18.89666 | -44.28352 | 2025-09-21 03:19:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f407647-9dcc-3a21-898c-df79f48da5b1 | -21.29148 | -43.89392 | 2025-09-21 03:19:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d5a1473a-66d9-37ac-a25e-1665c5587fbf | -19.51094 | -44.17356 | 2025-09-21 03:19:00 | NOAA-20 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6dc899b3-838b-3e03-a60a-5bd82af2da57 | -20.94262 | -41.5438 | 2025-09-21 03:19:00 | NOAA-20 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 06fcb9dd-bb04-3512-93d6-0086bccb9e41 | -21.28558 | -43.89265 | 2025-09-21 03:19:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af854c74-d5f2-3c87-9cb2-e29d53c661cb | -20.13429 | -42.48538 | 2025-09-21 03:19:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 59960449-bd4c-34f6-9676-dc74aa2cc643 | -18.89547 | -44.28867 | 2025-09-21 03:19:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d00e584-98f0-319a-a995-ae4752f74c8a | -20.54263 | -42.27585 | 2025-09-21 03:19:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4a8e3044-165f-31e1-86b0-25c38131ba26 | -20.54343 | -42.27226 | 2025-09-21 03:19:00 | NOAA-20 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3eb8c9bc-6767-396f-b959-d53b0bb8f2f4 | -18.36452 | -43.70559 | 2025-09-21 03:19:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cda2eca0-4499-3ab2-b876-be5f622db983 | -18.3652 | -43.70758 | 2025-09-21 03:19:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76e4f7b3-7711-3320-9320-12aac19e2c35 | -20.14012 | -42.4908 | 2025-09-21 03:19:00 | NOAA-20 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 64918ff8-0d6e-3307-8bde-2c0d1fc12ec6 | -17.43807 | -44.79636 | 2025-09-21 03:19:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4231f112-1bfa-3eec-8e33-bb7ed26c3605 | -18.36337 | -43.71066 | 2025-09-21 03:19:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2619827b-cde7-36ba-a7ca-8de3e8be2e09 | -20.94204 | -41.54652 | 2025-09-21 03:19:00 | NOAA-20 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bc430332-37f2-3bb4-9d47-5133b58bde82 | -19.90849 | -44.71874 | 2025-09-21 03:19:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ea081d8-0347-32e7-a20a-55102f84e60a | -16.86762 | -43.90585 | 2025-09-21 03:19:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83642501-4515-37af-9abc-d78f033d777e | -22.17153 | -46.74713 | 2025-09-21 03:19:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 067fcca8-2799-348a-8da3-9283cbf0086a | -20.75462 | -41.90924 | 2025-09-21 03:19:00 | NOAA-20 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 68d753c6-3891-3e94-8007-581ed7063ae0 | -20.13895 | -42.49049 | 2025-09-21 03:19:00 | NOAA-20 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0dff7c66-6c1c-3837-ac3d-064ef09c1c52 | -21.29257 | -43.88918 | 2025-09-21 03:19:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1fcd48c6-6f68-3cf7-a750-7bf116863bf5 | -18.83796 | -42.17792 | 2025-09-21 03:19:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 485f8d11-069b-3395-b06d-a8fde1e9d04f | -15.978 | -59.4269 | 2025-09-21 03:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a1b3ea09-6195-3c8e-9bf3-49d75355635d | -7.9256 | -44.0937 | 2025-09-21 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b11dace8-6f28-3127-a172-e3f07e1966a4 | -15.9783 | -59.4069 | 2025-09-21 03:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 8da9455e-0926-3b28-a9a4-94f30cb97436 | -11.6183 | -50.6075 | 2025-09-21 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d0484015-39bd-33d5-8f6f-09d251c96c3b | -11.4857 | -43.5692 | 2025-09-21 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c7dbecb4-0834-3dca-b4d3-83cc27c179a8 | -13.541 | -42.9835 | 2025-09-21 03:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 085eaced-a2c7-3bb3-af87-f8d597b464d7 | -10.3681 | -47.8875 | 2025-09-21 03:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 725637f2-cdd4-3783-b581-986e51c7d3e8 | -13.5405 | -43.0077 | 2025-09-21 03:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 131.5 |
| 60f31932-cebb-345a-b590-c8df1e4eba9e | -10.3677 | -47.9096 | 2025-09-21 03:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 27b0daae-5448-3506-a234-06884f6b187b | -11.505 | -43.5663 | 2025-09-21 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| b9f54699-8c38-3f83-affb-56454d414b22 | -7.9445 | -44.0918 | 2025-09-21 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 739a9e5e-b480-3fa3-b550-d07eda46ca29 | -7.7328 | -44.4593 | 2025-09-21 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d50ce575-5472-362b-9960-7db938596ee0 | -15.9586 | -59.4288 | 2025-09-21 03:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 5de8305f-3d05-323b-92bd-fd737a442991 | -5.5243 | -43.8647 | 2025-09-21 03:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 795958b2-3e8c-3f02-be54-ff2d15abe6e1 | -11.6377 | -50.5839 | 2025-09-21 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ee320722-97da-359f-b617-29046143c653 | -11.6186 | -50.5861 | 2025-09-21 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 79159d1d-f0f9-34ac-a455-76bc2d832c0e | -23.37316 | -45.42801 | 2025-09-21 03:21:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 36da20fd-6490-3459-a1ad-525032014f6d | -23.22024 | -47.03148 | 2025-09-21 03:21:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0a31a3d6-e54f-3d2a-8ea5-73273c358e62 | -23.14487 | -47.6266 | 2025-09-21 03:21:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 54016312-3888-3ab2-836d-54fee295c21e | -23.2171 | -47.03561 | 2025-09-21 03:21:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d9cea724-f4e3-31ec-a6b2-9daf1139f07b | -23.21353 | -47.02979 | 2025-09-21 03:21:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ed6ad77b-413d-337b-840f-b0e57a4540d5 | -28.2811 | -50.3563 | 2025-09-21 03:21:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 266d7518-ddfd-37de-9a18-f5fbe7e3b292 | -23.40933 | -45.72153 | 2025-09-21 03:21:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9cb09881-fdef-337b-8eba-154c4a6ffcbd | -23.1378 | -47.63258 | 2025-09-21 03:21:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 841e4120-3ceb-3f94-95ea-0fcff2a85673 | -23.41555 | -45.72315 | 2025-09-21 03:21:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c5343681-03f1-37c7-99c8-a34edbefca09 | -28.28335 | -50.37529 | 2025-09-21 03:21:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c6b9763c-d054-3238-9a1e-a9fd76e8b49f | -23.4189 | -45.72301 | 2025-09-21 03:21:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eaebeac3-6f19-3e3e-918e-43780b66c818 | -23.41706 | -45.71709 | 2025-09-21 03:21:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 07e81b1b-b9f0-3fae-8b39-69f04d5936f4 | -23.14309 | -47.6333 | 2025-09-21 03:21:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| cc16d779-5681-3c91-acb2-c568af495c17 | -23.14471 | -47.6344 | 2025-09-21 03:21:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 716a683d-f06d-367b-a80f-d859e7fd24e8 | -23.37829 | -46.36117 | 2025-09-21 03:21:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a3b11bea-9cb9-3e75-8a58-1d2b1a41b53b | -23.14644 | -47.62771 | 2025-09-21 03:21:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9eef620a-66ad-3903-9ad1-8d556fa2b511 | -23.41421 | -45.71513 | 2025-09-21 03:21:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1442df10-b031-3022-89fc-d540a747af03 | -28.27873 | -50.36453 | 2025-09-21 03:21:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 483b33c6-0915-3c6b-af24-63197844a1f1 | -28.28343 | -50.3482 | 2025-09-21 03:21:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9e41aff5-9f8d-3d94-8fe7-4c99be6907e3 | -23.41281 | -45.72087 | 2025-09-21 03:21:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ab1361d5-6a0e-33eb-9748-69e37837adab | -28.28816 | -50.35855 | 2025-09-21 03:21:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0ab1d821-29f7-3a9b-bb9a-22d574dbe070 | -28.28573 | -50.36699 | 2025-09-21 03:21:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8fb17bda-f9fc-318c-bfc4-bc13696acd7f | -23.21873 | -47.02912 | 2025-09-21 03:21:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2e2f3d9c-3ca0-3700-ad84-51baeaec6e75 | -23.41078 | -45.71574 | 2025-09-21 03:21:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bdcafde4-bc78-38c7-bbc6-0d1cc5615c15 | -23.13954 | -47.62582 | 2025-09-21 03:21:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
