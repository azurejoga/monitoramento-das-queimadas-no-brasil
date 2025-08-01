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
| 3f70ea83-2eeb-3bcf-9b1f-b83024194686 | -15.1382 | -45.65089 | 2025-08-01 04:17:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04f88da5-d772-3474-bcad-0f65666f8fdb | -18.44413 | -46.92286 | 2025-08-01 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86b78f4e-2945-39a8-8327-d885c0d1ce1f | -20.53034 | -46.10749 | 2025-08-01 04:17:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d82f4852-f9dc-37f3-a4e9-17653158f790 | -19.70514 | -46.7968 | 2025-08-01 04:17:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3747b681-bee9-3c38-8c75-9ad929a5cbc8 | -15.03156 | -49.43941 | 2025-08-01 04:17:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc3ba30b-1d64-345b-8315-1bb225323d46 | -19.01927 | -54.65847 | 2025-08-01 04:17:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a939a82-7b82-3cc2-a9fd-796cad1f4822 | -24.52657 | -50.79628 | 2025-08-01 04:17:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1faaa8e3-0b87-3a64-a71f-0f4b8f0a6a65 | -14.21437 | -43.93238 | 2025-08-01 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11361960-4f61-3c95-9e7b-83641f9d5a75 | -21.13981 | -42.02374 | 2025-08-01 04:17:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e566e9f8-04b9-386b-808a-f5013046a4af | -20.44683 | -46.42525 | 2025-08-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cde79dc5-012d-3992-823c-361b00784f74 | -23.52312 | -49.97577 | 2025-08-01 04:17:00 | NOAA-20 | JOAQUIM TÁVORA | PARANÁ | Brasil | 4112801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 410fd567-2722-3235-b708-eb71bff7859c | -25.79593 | -53.30931 | 2025-08-01 04:17:00 | NOAA-20 | SALTO DO LONTRA | PARANÁ | Brasil | 4123006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e6bc3320-3ef4-30dd-a6fa-262b915b010b | -18.80362 | -43.67843 | 2025-08-01 04:17:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c455d420-3ae0-3d30-98d9-10bf2593b9da | -20.47252 | -46.28252 | 2025-08-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbcb543b-d93d-30ce-bc93-5394a3e61df1 | -14.21772 | -43.93292 | 2025-08-01 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8140361-ec3d-3e0e-b1c8-7a65ffba8d2f | -20.34837 | -45.98995 | 2025-08-01 04:17:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c6bf311-dfd3-30ee-b443-599ccc97d5d6 | -18.54026 | -46.68764 | 2025-08-01 04:17:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67e05cda-c4fc-3c6f-ac01-bfb82a172055 | -20.38542 | -45.50194 | 2025-08-01 04:17:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f1be91d-90fa-3881-9448-ed7afd418e4e | -19.48488 | -43.85336 | 2025-08-01 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 460658b4-48f5-3262-a9df-c9bbbcf46b00 | -25.10131 | -49.51014 | 2025-08-01 04:17:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a69eb0cf-89cb-39ae-a4c0-7fb4a78498f6 | -15.08417 | -55.20926 | 2025-08-01 04:17:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cee0f200-75d7-3b40-a316-1f26f84e896b | -18.44771 | -46.90084 | 2025-08-01 04:17:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60578d40-bef3-35a8-8300-71120678d464 | -15.68991 | -43.21075 | 2025-08-01 04:17:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3a0b8bf2-e135-37a0-8b4f-9eb92570ba1b | -19.48776 | -43.858 | 2025-08-01 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 41e2aff8-f05b-34bd-ac48-72cf35a6f772 | -25.09791 | -49.50946 | 2025-08-01 04:17:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d40f2171-26e2-36f5-8dd9-c43a36df39f8 | -18.72659 | -46.88122 | 2025-08-01 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65ab6480-ff0a-3a1f-b673-b08bf8b527c7 | -15.08373 | -55.2395 | 2025-08-01 04:17:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd94eee5-1545-3533-85f6-a811dbeac612 | -14.32924 | -48.65402 | 2025-08-01 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc1ac58a-2c87-3033-b67e-d2dfbc5bde4d | -20.44741 | -46.42158 | 2025-08-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4805b5f7-6972-3159-88ef-23a70d6ae48b | -22.66517 | -53.37734 | 2025-08-01 04:17:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| edcd89ee-dcd5-32f8-b83b-2a8dc44a6677 | -16.13508 | -46.87874 | 2025-08-01 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d8a6f07-73d5-3d90-86ea-132dd52ce507 | -15.40685 | -55.77841 | 2025-08-01 04:17:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f33b857-af0e-39a1-9a1c-8ac5956b2102 | -17.13455 | -47.36794 | 2025-08-01 04:17:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e781658d-6fb9-34f8-8f73-e6cebd224047 | -15.08456 | -55.23541 | 2025-08-01 04:17:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a44d4d76-ed3f-3740-8f33-926ae446b19d | -15.40604 | -55.78231 | 2025-08-01 04:17:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2eb86f0d-febd-3458-b63d-b550b1f1c2de | -14.37706 | -50.33238 | 2025-08-01 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92042b3f-c1e4-3e4b-a465-2945afca2f8a | -14.23612 | -43.94702 | 2025-08-01 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17d27110-d0e4-32e5-9171-10ca90c79989 | -14.37368 | -50.3279 | 2025-08-01 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71e81f1b-7c44-368f-b523-35a5e3b3e502 | -23.35312 | -51.19759 | 2025-08-01 04:17:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 35c68eb3-06ed-3d9d-8424-23393d6664b5 | -24.58665 | -52.82105 | 2025-08-01 04:17:00 | NOAA-20 | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 464f2431-09cd-3c12-9a17-164ea0ac31bc | -18.21582 | -44.71265 | 2025-08-01 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b759891-064e-3ee7-b130-6c9003c06702 | -20.45071 | -46.42205 | 2025-08-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e890afc-2ef9-30d4-b589-9c4ae06dc940 | -18.44746 | -46.92344 | 2025-08-01 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f16ecca4-a6d4-3806-8fc9-ce78919fefe2 | -16.36123 | -49.48717 | 2025-08-01 04:17:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcca0b5e-27a1-3abe-adc1-44de6d4093b3 | -20.44353 | -46.42467 | 2025-08-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfca22b3-9ef9-3c8e-be48-f71abb885b79 | -18.21399 | -44.71287 | 2025-08-01 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e05fb8be-ad2c-3b0f-ac8d-69cd3354440f | -19.01434 | -54.65752 | 2025-08-01 04:17:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46efe15a-98e4-368f-b772-a3150e9c612d | -19.0038 | -46.25149 | 2025-08-01 04:17:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fe66331-6da8-3933-a287-c1c52c237021 | -17.72506 | -46.21817 | 2025-08-01 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91a5aa3a-a175-3028-bf6b-e884b2d8bca1 | -20.45128 | -46.41838 | 2025-08-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0bf0ecb-743d-361e-8265-c273b10ff0c6 | -18.44686 | -46.92715 | 2025-08-01 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5b45a7a2-1af6-3564-8d9e-37bf0b3ee25f | -20.01142 | -47.38231 | 2025-08-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8da45d48-d8a1-3034-92ac-c8500d01e5e8 | -18.54357 | -46.68822 | 2025-08-01 04:17:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8e3fc36-59ac-388f-b36a-155a8f6df441 | -20.43964 | -46.42775 | 2025-08-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d318313-df10-3266-9749-f7348874c7de | -14.20584 | -42.84335 | 2025-08-01 04:17:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a6591af4-0940-38ef-9b34-5aaf2e5edf3d | -28.18445 | -49.60588 | 2025-08-01 04:19:00 | NOAA-20 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8905178-8b13-358d-b80d-6e44060b6308 | -22.95605 | -49.12239 | 2025-08-01 04:19:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21495f9a-1a79-3d98-9334-8f6ea0e73529 | -23.12694 | -48.77975 | 2025-08-01 04:19:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6055035b-dd39-3acd-aea8-3ae1062def46 | -22.99926 | -48.63635 | 2025-08-01 04:19:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7c4ac2aa-dea8-344f-8bf7-6b93ecc3d6de | -29.80794 | -51.2278 | 2025-08-01 04:19:00 | NOAA-20 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 89d6e79f-fd85-3832-b36b-41c79f162a46 | -23.52488 | -47.83371 | 2025-08-01 04:19:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 3bdb4400-53ca-3f42-afc3-fdd74160d618 | -22.0868 | -46.96651 | 2025-08-01 04:19:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 230eba48-7a67-30dc-a76c-8aaed747e0a6 | -22.70515 | -52.63266 | 2025-08-01 04:19:00 | NOAA-20 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 01a0b5d5-3412-3448-af25-0da3920bd845 | -28.2878 | -49.89871 | 2025-08-01 04:19:00 | NOAA-20 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bb8a2202-5360-3222-817c-cbd98da55eb1 | -22.86316 | -47.14626 | 2025-08-01 04:19:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a08b79d5-ef08-3dba-973e-1cc606b99f8a | -22.59607 | -42.1068 | 2025-08-01 04:19:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b471604e-1c4f-3dc4-8c66-800ae3b2764a | -22.69743 | -43.34775 | 2025-08-01 04:19:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| da00d802-1415-32c8-8564-31e6c681f8ad | -28.252 | -49.71025 | 2025-08-01 04:19:00 | NOAA-20 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 28475e83-17dc-3303-a0b5-a57a5a321647 | -29.28832 | -50.48914 | 2025-08-01 04:19:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3cea03a3-cb0b-3175-b155-d88c7642ff5e | -23.03628 | -50.16031 | 2025-08-01 04:19:00 | NOAA-20 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ff6dbe8e-8730-3b42-a646-299b722968fe | -28.97901 | -50.44646 | 2025-08-01 04:19:00 | NOAA-20 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6439df6b-52aa-3ae3-91b5-b7c403b2dd3c | -27.92075 | -49.3281 | 2025-08-01 04:19:00 | NOAA-20 | BOM RETIRO | SANTA CATARINA | Brasil | 4202602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 609283c7-b471-3b91-acad-91790320e213 | -23.53059 | -47.06921 | 2025-08-01 04:19:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c61c1599-9610-3046-a113-83d79403192d | -31.06372 | -54.26061 | 2025-08-01 04:19:00 | NOAA-20 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 365aaeaa-7dc0-3286-a7e5-8f0aad903b7b | -29.14961 | -50.66217 | 2025-08-01 04:19:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae80316e-fc53-349e-8df3-8483ec809d36 | -22.74514 | -47.14118 | 2025-08-01 04:19:00 | NOAA-20 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9cea944-5273-3644-b464-23cacd90ed4a | -22.59214 | -42.10618 | 2025-08-01 04:19:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6336648e-1c3c-34c5-bc3d-df7d4e175ecd | -29.6781 | -56.02558 | 2025-08-01 04:19:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| c71d86fe-c656-3d37-82d3-e97d9b91ff74 | -22.04999 | -46.81099 | 2025-08-01 04:19:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5dbba0c3-23a3-3824-beb3-fa4a22a645b3 | -22.71153 | -43.76694 | 2025-08-01 04:19:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aee5a439-756c-39f7-8198-0c14ed062f2f | -29.00676 | -50.16005 | 2025-08-01 04:19:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 72d7c449-cbf8-329a-a848-9404dbc2ae3e | -22.5155 | -47.21856 | 2025-08-01 04:19:00 | NOAA-20 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b7a0c43-5966-3275-bea2-5ec763347850 | -23.52095 | -47.83686 | 2025-08-01 04:19:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| eb56995e-a92c-343f-932d-5871df607a52 | -21.47698 | -57.10832 | 2025-08-01 04:19:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 213d425b-a81b-3615-9aad-f46ea8925408 | -28.31627 | -49.55103 | 2025-08-01 04:19:00 | NOAA-20 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b0913407-b902-3aa5-9ad4-41475dde167d | -22.51279 | -47.21423 | 2025-08-01 04:19:00 | NOAA-20 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6b596a21-3957-3a3c-a640-ac55321d1b32 | -29.06874 | -50.92821 | 2025-08-01 04:19:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fe9f21fc-1091-33a7-a286-36eb22c19db5 | -22.69766 | -48.04653 | 2025-08-01 04:19:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5611888-bd26-3b99-be21-5ca21f279f33 | -22.95946 | -49.12306 | 2025-08-01 04:19:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9005a856-e311-3be8-b463-22015162e1bb | -29.28761 | -50.49327 | 2025-08-01 04:19:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d229feb8-0fc3-3243-961a-8f080b65f628 | -19.45893 | -56.885 | 2025-08-01 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 43da6284-67f8-343a-8be9-7ac89695d4e8 | -30.07212 | -52.07034 | 2025-08-01 04:19:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 81fa0f05-c4c4-3bf5-9953-d436f34732e8 | -21.4407 | -57.14062 | 2025-08-01 04:19:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a0c76b7-9a77-3cae-9921-ab860afa7a45 | -21.24739 | -48.56779 | 2025-08-01 04:19:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83f91839-0f2b-365e-98bf-4db24c5a6c5c | -23.52156 | -47.83308 | 2025-08-01 04:19:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 98e1edd5-d8a6-3a95-b471-5113b5fca5c7 | -21.80758 | -47.24846 | 2025-08-01 04:19:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| dad90b50-912c-3149-9f52-4d2cc1dacc13 | -21.47458 | -46.71383 | 2025-08-01 04:19:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e370101b-d7d4-3ef3-a201-58285e8ea836 | -21.47516 | -46.71013 | 2025-08-01 04:19:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cb00ab38-f82c-369f-ade0-863970e035ba | -21.39235 | -48.74882 | 2025-08-01 04:19:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ed31f69b-bc09-33db-a4c7-4d7598448412 | -23.51492 | -47.83184 | 2025-08-01 04:19:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |


[Clique aqui para ver as próximas entradas](README18.md)
