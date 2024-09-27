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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19a6b230-47db-3008-9757-368638d926e6 | -20.49961 | -43.49483 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f4a77aeb-9134-3833-8cd9-b325c9cb1fe9 | -20.49673 | -43.48982 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cda187dd-7c03-3a07-8fb4-26fbc52e7edb | -20.49594 | -43.49429 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c6c5d056-731e-3b55-b07f-f7a726990b26 | -20.20908 | -43.43809 | 2024-09-27 03:49:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 586ab6cb-5f17-316b-bd16-b58d26bcbf21 | -20.15464 | -43.51041 | 2024-09-27 03:49:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 0e1ea565-bf97-3740-8954-d6ba0062c2e6 | -20.12197 | -43.44159 | 2024-09-27 03:49:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 82dbdb59-f326-3cdd-897a-e82b61169259 | -20.11836 | -43.44061 | 2024-09-27 03:49:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b19dac74-4afd-3387-b1fd-8975f0266eda | -20.11761 | -43.44489 | 2024-09-27 03:49:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c5201bcc-0221-3557-a136-3278dd695948 | -21.6245 | -43.46836 | 2024-09-27 03:49:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 04af6db7-89f4-3712-9b7b-78ecf5e82b70 | -21.53786 | -43.62043 | 2024-09-27 03:49:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fb7a1bd1-9a99-3852-97d4-5e1c3a3039c9 | -21.53425 | -43.61971 | 2024-09-27 03:49:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2c24df10-3e30-3873-a362-74c2b6ab66a9 | -21.88969 | -42.67068 | 2024-09-27 03:49:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c4ce7b60-3da8-3994-914e-5c4362ceeac3 | -21.70046 | -43.13798 | 2024-09-27 03:49:00 | NOAA-20 | CHÁCARA | MINAS GERAIS | Brasil | 3115904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3e9a8bcd-38c3-35a1-bf55-a08453202985 | -21.41531 | -42.97946 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0cc142d8-34ef-3b4e-9e51-7e6174a6f17d | -21.41182 | -42.98028 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 9b1ac997-d71d-316b-bc81-970345485c48 | -21.41182 | -42.97862 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| e90505c0-6e27-3310-8ec8-9107441af85f | -21.40984 | -42.97054 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| b3580180-3265-3fc5-8bf6-16d5d64c05cd | -21.40913 | -42.97327 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1fe6a0e4-c8e4-3fb6-b52b-3f8b59e5147b | -21.40908 | -42.97498 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 4ef847f8-b42c-38af-b400-74ac0803ee5a | -21.40833 | -42.97775 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 8efc4266-8d05-33bf-9de4-bc26c4d74c29 | -21.40832 | -42.97944 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 6ae08565-e87e-370f-9276-6d07a2b6fdd6 | -21.40756 | -42.98211 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6a1ca0d-3942-3a97-b9b5-437f21aabcdf | -21.40559 | -42.97406 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1e5507a7-8daf-3dec-a527-6650cefac4de | -21.40482 | -42.97858 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9837b031-9b45-3a4c-911c-d968c49cf1ea | -21.40361 | -42.96441 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0b780bcb-e3a3-359c-996f-a3747ad2a26e | -21.4021 | -42.97321 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 33f5266b-146c-3a04-8f69-c9c42df9fa03 | -21.40132 | -42.97777 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 705e452d-3d38-39af-8215-75967a74c278 | -21.40012 | -42.96349 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1a75d23f-49ad-37b0-b53e-6f64248c7f13 | -21.39859 | -42.97243 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ff7529ba-3e6c-3b6a-9be7-91d8c6f8e93d | -21.39782 | -42.97698 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a6831e52-d765-33a7-b3b5-f3f8b62ecf4a | -21.39508 | -42.97169 | 2024-09-27 03:49:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 433b064f-230a-3d1d-b1ce-22dff6cb2b0d | -21.39314 | -42.96182 | 2024-09-27 03:49:00 | NOAA-20 | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ef086bce-fb20-346a-bb35-e92925580cd9 | -21.39235 | -42.96639 | 2024-09-27 03:49:00 | NOAA-20 | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a5d0aa45-59da-3a46-a02d-47da94d33efc | -21.38963 | -42.96108 | 2024-09-27 03:49:00 | NOAA-20 | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ced2cc73-3fcf-325b-82aa-b13eb61209e2 | -21.38883 | -42.9657 | 2024-09-27 03:49:00 | NOAA-20 | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bfe94022-7dbd-384c-8b35-f9a45b886b3f | -21.27616 | -42.7979 | 2024-09-27 03:49:00 | NOAA-20 | DONA EUSÉBIA | MINAS GERAIS | Brasil | 3122900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b2deef80-57a1-3930-9eb7-138995ae173a | -21.09721 | -42.96978 | 2024-09-27 03:49:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bf9041a2-5bcc-3a0c-a0bf-3fc48f0b385c | -21.02178 | -42.67107 | 2024-09-27 03:49:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| afc21155-64cb-3293-b80e-293ed98f3d94 | -21.02106 | -42.67535 | 2024-09-27 03:49:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b46b3dcc-b048-304e-8451-d1e3839235fb | -21.01481 | -42.66962 | 2024-09-27 03:49:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aa226b43-2697-3dad-9adf-a1c50e0aec7c | -21.01131 | -42.66898 | 2024-09-27 03:49:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 14070382-586b-3699-b9ab-fea83e961253 | -21.00851 | -42.66429 | 2024-09-27 03:49:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 01ef0503-a963-310e-82f7-16fa44c00baa | -21.0078 | -42.66844 | 2024-09-27 03:49:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ef5e745-f77a-3214-9bf6-3d07457763cb | -21.0043 | -42.66787 | 2024-09-27 03:49:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a4cfaf3f-7fd6-3c47-9c4e-324963cc4365 | -22.90155 | -43.75212 | 2024-09-27 03:49:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5dc280fc-2abe-347b-9baa-328b68cbb4db | -22.7843 | -43.75716 | 2024-09-27 03:49:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8a83b30b-4b1c-3ee1-8243-099cbea9bc43 | -22.77582 | -43.80526 | 2024-09-27 03:49:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7044f472-5280-35a5-9b49-45bfc38b2ade | -22.61838 | -43.59711 | 2024-09-27 03:49:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f71657d0-2e35-387f-bfc7-83afe8fd02de | -22.59275 | -43.96837 | 2024-09-27 03:49:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 96edca47-f037-3fa8-830f-47b4ef279fc5 | -22.58911 | -43.96771 | 2024-09-27 03:49:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 79f517fc-2c5f-3ba2-af41-bbb16927e87e | -22.55615 | -43.81411 | 2024-09-27 03:49:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 0a8d56d2-45af-3bcb-9d52-70ee57e48861 | -22.55256 | -43.81335 | 2024-09-27 03:49:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9dbe5326-5be3-37c9-a10f-79c3734d7d35 | -22.40667 | -43.95705 | 2024-09-27 03:49:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0d5c2f31-74b5-3304-9996-20862229df99 | -22.40588 | -43.9615 | 2024-09-27 03:49:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f895de86-e8a6-3012-b68e-4efc959e79ba | -22.40308 | -43.95608 | 2024-09-27 03:49:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b53f70a2-9389-392b-a993-11b15134a2ac | -22.39717 | -43.54086 | 2024-09-27 03:49:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76cb2444-a330-3efd-908b-956267747270 | -22.39359 | -43.54024 | 2024-09-27 03:49:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82d9f8f9-9127-3920-9afa-65db06599b1a | -22.38869 | -43.95229 | 2024-09-27 03:49:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f7d556f5-2704-3099-93ad-24cc247b26ef | -22.38721 | -43.53453 | 2024-09-27 03:49:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 70b2b53c-0fac-35db-b992-339b4e67eddb | -22.387 | -43.96179 | 2024-09-27 03:49:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4e4e72e4-99d6-3af8-95b9-4759a01f9383 | -22.38615 | -43.96649 | 2024-09-27 03:49:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cf1a6c67-fa47-3b75-bace-e8b195428598 | -22.37606 | -43.95979 | 2024-09-27 03:49:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d8c4795e-056a-30ea-8f74-d36cc1cc8793 | -22.35315 | -43.51851 | 2024-09-27 03:49:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a99c13cc-46c4-3096-848a-0b3088845dd0 | -22.35239 | -43.52279 | 2024-09-27 03:49:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 30957392-3a26-387b-8001-a69c2f70a804 | -22.34961 | -43.51762 | 2024-09-27 03:49:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1aebf79d-71e3-35ef-950a-e1ce9918ed42 | -22.34884 | -43.52196 | 2024-09-27 03:49:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1c5fc0f9-50b9-397a-aaa2-2ed538585eb3 | -22.67586 | -42.85689 | 2024-09-27 03:49:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 7a9ab83e-8db4-3b68-85c7-8e1efd8fc045 | -22.67515 | -42.861 | 2024-09-27 03:49:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 510a4ba2-1aa7-3f7d-a086-997f9a573de8 | -22.6724 | -42.85618 | 2024-09-27 03:49:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| e3eee009-314d-3e4e-9111-55dee566d985 | -16.04239 | -43.61288 | 2024-09-27 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d0797722-9bbb-3b5f-938a-6496de417123 | -18.00808 | -43.69292 | 2024-09-27 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6ce3b7a-0936-3be8-8b4a-2e71524825f8 | -18.00621 | -43.69464 | 2024-09-27 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d76c0ccc-d587-33f0-ad40-12e8f554cf23 | -18.00426 | -43.69221 | 2024-09-27 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 777fc826-2c25-3484-8b87-3dae45c1da8f | -17.95255 | -44.24883 | 2024-09-27 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bda7f863-b7d3-383b-b415-04568ae334a9 | -17.94377 | -44.25219 | 2024-09-27 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35c6f092-06bc-346e-9799-0a8414eb45bf | -17.93985 | -44.25134 | 2024-09-27 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d0ca498-6878-33b4-9c06-413298d0ef01 | -17.92669 | -43.5145 | 2024-09-27 03:49:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2f59a76-d806-3bba-940d-67819c690da4 | -17.92581 | -43.51947 | 2024-09-27 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf6bda76-7ca7-3399-bc96-02473e40c756 | -17.82738 | -44.44941 | 2024-09-27 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38e76a3b-b285-3ab6-b16e-51196a9b17ac | -17.82672 | -44.45303 | 2024-09-27 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 341cc7cb-0bea-37b3-8bf8-19b10b1e8121 | -17.82203 | -44.456 | 2024-09-27 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1518f93-f7a0-3153-bfcd-fc9a2bb3b6cc | -17.65969 | -44.40103 | 2024-09-27 03:49:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab756386-b50a-39d1-8cce-43315502d361 | -17.5267 | -43.61652 | 2024-09-27 03:49:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2de6a6d1-6693-3309-97d1-0c5a1f8e598a | -17.52287 | -43.61583 | 2024-09-27 03:49:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9980246-a560-3a0f-bc55-d1f732b13c90 | -17.04252 | -43.23368 | 2024-09-27 03:49:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad6af448-2c2e-3e2e-9f0e-5127536819be | -17.04169 | -43.23833 | 2024-09-27 03:49:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 625729cd-0d62-3f05-bf8f-d7c2a3875cba | -17.03875 | -43.23295 | 2024-09-27 03:49:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa7bbf45-ae7d-351e-949a-2dc295a3682d | -17.03792 | -43.23759 | 2024-09-27 03:49:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4fb3ef70-4cb1-359a-aed4-93e89b85229d | -16.68012 | -43.88255 | 2024-09-27 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d634225-256a-3919-83c4-2174f75f995d | -16.67891 | -43.88305 | 2024-09-27 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 238213b4-aabd-3a75-8a46-cd1a0d5cd1a0 | -19.24156 | -44.37675 | 2024-09-27 03:49:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91f4c034-d2b5-3835-afab-73a5a0f7278a | -19.22985 | -44.35286 | 2024-09-27 03:49:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbd30dc2-f1a5-37e6-bbda-2d8ad2021aca | -19.1041 | -43.45862 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4b5ee13d-bdb3-3e22-ba8b-77e651e449ec | -19.10037 | -43.45805 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a3c0150a-7680-3223-ac23-907ef30bc03e | -18.94977 | -43.51819 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 948c0b3c-727d-32f4-adc0-d34481302001 | -18.8764 | -43.44848 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a2ffb8f0-bc07-3a4a-8114-b7a99d10d22d | -18.87271 | -43.44766 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a19252ca-617d-3f4d-ab30-081180254599 | -18.60878 | -43.46699 | 2024-09-27 03:49:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c8d770a4-ee0e-3134-af59-11894bd1ffb1 | -18.60682 | -43.41393 | 2024-09-27 03:49:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b085fc93-baa8-3744-898c-4bcb41d82e7f | -18.60608 | -43.41092 | 2024-09-27 03:49:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README63.md)
