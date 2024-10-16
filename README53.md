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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4bd5569-9171-350a-947c-8a8d95dee49d | -18.28742 | -41.73668 | 2024-10-16 04:34:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cb1b4ad4-2d03-3dc8-b9b8-6fb4136c6ccd | -18.28708 | -41.7397 | 2024-10-16 04:34:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4372d21b-6a8f-350a-8f0f-6dd498fd88e1 | -21.67707 | -45.89975 | 2024-10-16 04:34:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6dac2561-6495-35cd-8760-a711d1cfe0f0 | -21.67301 | -45.89902 | 2024-10-16 04:34:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d5679ebe-30ce-3936-b3c8-e5921e495e77 | -20.76421 | -46.77155 | 2024-10-16 04:34:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8c14ae72-c057-34a1-abb4-35d5f1fdef22 | -20.71739 | -49.45488 | 2024-10-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cecacb8-3257-3d7c-b1e9-5a9992f04c68 | -21.25815 | -49.02934 | 2024-10-16 04:34:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9e0eacbb-0782-356a-8cd7-a3829127f431 | -17.04107 | -49.28896 | 2024-10-16 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11669eeb-3d83-34b3-aca2-99525eab771e | -20.85523 | -49.87306 | 2024-10-16 04:34:00 | NOAA-20 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f4335f73-fece-3e1d-b88d-c8d5797570ad | -20.85466 | -49.87685 | 2024-10-16 04:34:00 | NOAA-20 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1d932cad-3127-3821-82ca-625f4621a4aa | -20.85187 | -49.8725 | 2024-10-16 04:34:00 | NOAA-20 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 791bde14-cd45-32bd-8bc5-d07ec1038851 | -20.8513 | -49.87629 | 2024-10-16 04:34:00 | NOAA-20 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7aa065ef-b606-3607-90f1-75869c60be1a | -20.51452 | -51.04076 | 2024-10-16 04:34:00 | NOAA-20 | SUZANÁPOLIS | SÃO PAULO | Brasil | 3552551 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86550d7b-146f-37e3-9744-5bd1fb8de182 | -20.418 | -50.74506 | 2024-10-16 04:34:00 | NOAA-20 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ebf32b0e-a1cf-3713-ad86-475929d51b37 | -18.26055 | -56.5748 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1975b338-876d-3ce1-a4e1-ab6079c5de75 | -18.48644 | -51.57296 | 2024-10-16 04:34:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84e0b3c7-0d7b-36bd-a492-820e5c9d41b3 | -18.27375 | -51.74791 | 2024-10-16 04:34:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2aca7e71-3b93-3a44-8c45-ce9df6734457 | -20.9962 | -51.79481 | 2024-10-16 04:34:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d8b1ce8-1183-30a0-8811-112272b99774 | -20.99561 | -51.7985 | 2024-10-16 04:34:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a855a9f3-bb52-3284-ae75-9c3784cc8b5a | -20.47569 | -53.67471 | 2024-10-16 04:34:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3cd2b7d-c86d-3a15-ba13-7df6928e5642 | -18.25904 | -56.58291 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 57ff2b63-1f28-37f7-b515-f3bfd15ff967 | -16.81746 | -53.93988 | 2024-10-16 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bf23204-ed5f-31bb-bf39-ba363decf72f | -16.8138 | -53.93911 | 2024-10-16 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce832e1e-52d7-329a-92dd-7bf7286262f3 | -18.2598 | -56.57886 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d840f2a7-f1a2-3642-931b-b744401bd486 | -15.91822 | -56.31144 | 2024-10-16 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d9426e7-a98d-3410-a123-def5e8ed2026 | -15.91745 | -56.31565 | 2024-10-16 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ef3d790-fa6e-3fe7-83bf-dbad5c85a31a | -15.91668 | -56.31985 | 2024-10-16 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90de23fe-e5d6-38de-902d-69797c411556 | -15.91472 | -56.3063 | 2024-10-16 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9eceed0f-a93d-345d-9fd7-009c8d89aace | -15.91394 | -56.31054 | 2024-10-16 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44e82063-005f-3fc6-aae3-735e961249c5 | -15.91316 | -56.31475 | 2024-10-16 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38968f81-5b20-39cb-af0d-034834d09171 | -15.91239 | -56.31894 | 2024-10-16 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57bd3f70-c386-376c-8e63-b70994011f53 | -15.90966 | -56.30962 | 2024-10-16 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d2fb269-cdf3-3a1b-abc1-ac30e1b33691 | -15.36323 | -56.32312 | 2024-10-16 04:34:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e718418a-619c-3d92-9d8f-7de54bf22cec | -18.27356 | -56.57685 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4a5e5133-2db9-3cfc-856c-c6245970aeec | -18.27311 | -56.57745 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 0e74b4cf-d8c0-3fa9-b6ff-27c76376458d | -18.27278 | -56.58089 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5d0d91a0-c746-3d6c-adfa-477365208b9b | -18.27122 | -56.589 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e8009b6f-e2e1-3605-b049-b8b910bf7fbe | -18.27085 | -56.58963 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 5adaca28-7930-351d-ba4c-f1132914900f | -18.27043 | -56.59306 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.6 |
| 5bfa8339-d580-320e-a52a-d99dcc495587 | -18.2701 | -56.5937 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 3e62e14b-dad0-3fde-b5b8-2558575c87ac | -18.26965 | -56.59711 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.6 |
| 97968563-7a96-36e7-af8c-7d661ad9d97d | -18.26934 | -56.59777 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| f9b4d9db-db40-35d0-ae8c-283e1008b577 | -18.26892 | -56.57656 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 44d6db2f-796f-3863-b537-3b08e60743aa | -18.26887 | -56.60117 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d28cdf52-f86a-37ac-952a-6eb6b5af633e | -18.26859 | -56.60184 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bbab4368-e152-3439-944d-0c6b7404992c | -18.26817 | -56.58062 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| ba797ab4-c96c-3262-b703-0cdcd8356ea7 | -18.26742 | -56.58468 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 02b008ce-7f25-3691-804b-7bdd08e3faa0 | -18.26666 | -56.58875 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| c46a1b5e-eb11-36b6-a888-172f052cadfb | -18.26591 | -56.59281 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| cf535309-36a7-37f7-a3d0-af249d166760 | -18.26515 | -56.59688 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 28fbfabc-8c6a-3166-b466-0086d570b6e7 | -18.26474 | -56.57568 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6ff00379-ccf9-3ecd-9b6d-b923004aa359 | -18.26439 | -56.60096 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aa4b25a0-d722-336e-bfb6-2d8c054da1ac | -18.26398 | -56.57973 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7f6be35f-ccde-37f8-904c-3913bcb3ff41 | -18.26323 | -56.58379 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 1c471057-af13-3b4f-aedd-426668069766 | -18.26247 | -56.58786 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| fd81e617-b7d7-329f-8e27-de923e612064 | -18.26172 | -56.59193 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7e3f180c-c213-3616-be79-9261349381e2 | -18.26096 | -56.59599 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b8757ed5-b826-3805-8282-2a01a245b67c | -18.25829 | -56.58698 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7c8a90c0-29b1-3a31-b4f0-3a7d1a8bd6df | -18.25753 | -56.59104 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f1b42977-aad4-39c6-bebe-b13e58bffab2 | -18.25677 | -56.59511 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4c330596-0619-380f-9914-911430dec7d0 | -18.25637 | -56.57392 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 83bcc232-fd79-3d87-94d2-59e2f7fd5aa8 | -18.25561 | -56.57798 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d689970f-efb4-3ec6-9f2f-86312f09bc4f | -18.25485 | -56.58203 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 436af023-bed2-3052-94e8-9fb114af0359 | -18.25158 | -56.4146 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9cd373fa-c8a6-366b-affd-8c10fbbb509f | -18.25009 | -56.42253 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c3001166-8ec5-350a-98e2-78bb3a4024d6 | -18.24934 | -56.42651 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f26e40df-ba18-35a7-9bce-c7abc6b72463 | -18.24777 | -56.38913 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 64b290ff-4ba9-3d64-9b0e-5fedaad8f53a | -18.24702 | -56.39309 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| c06e29da-6762-3a13-ae4b-ff64c211aacb | -18.24363 | -56.38827 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 6e183fff-494e-36a6-83f4-0184aa4e49ca | -18.2361 | -56.3826 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 54cc54b6-3abb-352c-b8e8-43ab1332aaff | -18.23536 | -56.38654 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 988a6340-66f5-3990-91d7-c81a02e775a1 | -18.23196 | -56.38173 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e2d6dea5-a1d8-3d12-b28b-60cd81fdd6df | -18.22783 | -56.38087 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 745e292d-feb7-3250-80f0-8fa30954ebbd | -18.16239 | -56.81593 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 4e96d860-01e4-3ece-83a1-d0a75f17ee40 | -18.16158 | -56.82014 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b9a8f403-c6bd-35b5-b0ad-5829bba47078 | -18.14563 | -56.39874 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 818e9141-0f46-3fa6-93c6-b8d6c066e860 | -18.14074 | -56.40184 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cf98a155-de72-3ee0-8778-60cdff2d1a7c | -18.10582 | -56.28038 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 066ed153-56bc-3373-a34a-04246b1933f7 | -18.1051 | -56.28429 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9dd28ea7-e57a-30b1-a9f1-e0c98bd3b765 | -18.10438 | -56.28821 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b8c3dff8-ff9b-31f3-a7e3-4e7b57eb8cd8 | -18.07887 | -56.35653 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1ec2a1a4-7770-3a72-b862-251417e63120 | -18.06893 | -56.31755 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 63f52992-ddce-31d6-925a-c04d10822134 | -18.0682 | -56.32148 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 66b5d814-283d-35fe-a454-e0f63ada8285 | -18.06588 | -56.40331 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f3d1ea33-e0b3-3217-acc1-a4412916950a | -18.05565 | -56.38876 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 97e8e7af-4e2a-349d-b80b-0a2d8663d6c1 | -19.58572 | -56.99445 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| 8d7eac98-5a70-3787-8dea-81a22011f921 | -19.58542 | -56.97304 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| fce73044-a698-35ea-a38d-094cd97010d7 | -19.58464 | -56.97713 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 061d14b1-aac8-3499-808a-ae8d0641f2f8 | -19.58439 | -56.53483 | 2024-10-16 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a6c387b8-d4ae-307d-b2c4-88d389d997d2 | -19.58386 | -56.98123 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 74f737e2-e883-3bc6-af62-667b51900a8b | -19.58308 | -56.98533 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 0f8a40d4-1f22-388f-9f60-4050326b9f27 | -19.58278 | -56.96394 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 6d474f72-b182-3578-bd7f-06eec34a7ac4 | -19.5823 | -56.98944 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 86abcef3-43f7-3add-8af0-cb7c2b907dc1 | -19.58201 | -56.96803 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 68f0a5be-01d4-3361-9dc0-e7af1fc66d5d | -19.58152 | -56.99354 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| a7af9744-108d-3b76-81c7-45b8356dc9f5 | -19.58031 | -56.53397 | 2024-10-16 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e8f5522c-4c41-30c9-86f5-7d8941ba08d5 | -19.57967 | -56.98032 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f2a254c7-bb61-3c75-a608-593f625cbb23 | -19.57889 | -56.98442 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| e971d7f7-06e0-367b-bb9e-1ba5e759a62e | -19.5786 | -56.96303 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 2dd1d003-7afd-3c1b-a285-0f51d68e265e | -19.57811 | -56.98853 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |


[Clique aqui para ver as próximas entradas](README54.md)
