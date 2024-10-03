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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bec1a213-da0e-3a72-afae-edf4a6775455 | -4.64766 | -47.43828 | 2024-10-03 05:14:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4e735e5f-aee7-3d89-80c3-7d490b9a6f1e | -4.64673 | -47.43583 | 2024-10-03 05:14:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3aa4b519-816e-34af-8d4f-97207f581ef7 | -4.64605 | -47.44051 | 2024-10-03 05:14:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14533a76-bf79-3f3e-b1cc-ff7ae52a3550 | -3.70146 | -47.61117 | 2024-10-03 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5aa2dc9d-9a93-37d8-bfb5-d950ae09cc53 | -3.6968 | -47.60167 | 2024-10-03 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be51e90f-996a-3d43-8931-2743dd8927fe | -3.69618 | -47.60598 | 2024-10-03 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7816e91d-9073-3360-87e2-c06c628c976b | -5.35471 | -46.72118 | 2024-10-03 05:14:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 775b84d7-df6d-3cd7-8318-39b6f5126bcb | -5.35401 | -46.72618 | 2024-10-03 05:14:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18a8b3aa-47d2-3c0d-b419-d1ca5487f44f | -5.24075 | -46.77604 | 2024-10-03 05:14:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1727fbfc-3c45-3754-95c3-d8753a9e5f5c | -7.11385 | -47.87738 | 2024-10-03 05:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 120a9fbc-abd9-3bd9-aba8-f052704978c8 | -7.11326 | -47.88176 | 2024-10-03 05:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b434946f-b26c-3f66-a137-2874d1b9eb8c | -7.11267 | -47.88614 | 2024-10-03 05:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1640f1a-c1a4-3850-b3bd-650d8529388b | -7.11206 | -47.89067 | 2024-10-03 05:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d7404f1-7b31-3a77-914e-1897cb35a498 | -7.10665 | -47.88486 | 2024-10-03 05:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 242aaf8d-f0a4-300e-a891-bc5ac169c6f7 | -7.10603 | -47.8894 | 2024-10-03 05:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ddc14c0-759b-3a11-bf60-043971a729c4 | -7.06834 | -48.03243 | 2024-10-03 05:14:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22d2948c-33a8-3a5a-ab45-38670e781c3f | -7.06773 | -48.03703 | 2024-10-03 05:14:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 457f9479-be7d-37ad-8a12-6eff5d985062 | -7.06712 | -48.04162 | 2024-10-03 05:14:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a57094fe-2b23-30a3-92c1-1dbf34fccf29 | -6.9473 | -47.67253 | 2024-10-03 05:14:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a7a1e7a-054b-31ca-b63a-902e5fc1818b | -6.9467 | -47.67715 | 2024-10-03 05:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57f71fcf-6083-33fc-8f3e-a5f8799ef17e | -1.91148 | -47.8854 | 2024-10-03 05:14:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1138455-5a50-3a1c-964d-35be23a65598 | -1.91091 | -47.88921 | 2024-10-03 05:14:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a816e8f-bd75-3b4e-a5f4-0d8546c9ad4a | -3.46365 | -47.66302 | 2024-10-03 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 630b33cd-243f-3776-aa51-e25c998d5104 | -3.46301 | -47.66726 | 2024-10-03 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| defe2f55-ab5e-3a27-b27a-5597a3973830 | -3.46277 | -47.66235 | 2024-10-03 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 323b5a39-6972-316c-90e9-31969a85d49c | -3.46216 | -47.66661 | 2024-10-03 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37bffd92-de30-3dfc-b794-358aa9e8cfc6 | -3.22748 | -48.92812 | 2024-10-03 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4925817c-7c55-3daf-95e0-19d24e92b0a7 | -3.22209 | -48.92739 | 2024-10-03 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 93537df0-f97d-3dfe-b1b4-7222d78c2248 | -2.98995 | -48.55755 | 2024-10-03 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9195261c-501d-3455-9243-191cd7abe761 | -2.98944 | -48.56109 | 2024-10-03 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bf1edc4-0c52-3eb7-9ebd-3939c3f34601 | -2.94896 | -48.6047 | 2024-10-03 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cb42376-5ee6-3a46-8153-99eeb44e1487 | -3.70679 | -47.61605 | 2024-10-03 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b89afd26-35cf-3347-9979-788c97737c29 | -3.70085 | -47.61544 | 2024-10-03 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97a481f0-956b-340e-8f94-0dd3ce7fab95 | -4.80339 | -48.47898 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 552b6c98-cd07-3a90-b319-aba44126efd9 | -4.80282 | -48.48293 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14131427-aee1-3587-b0d0-060a4b52c377 | -4.79775 | -48.47796 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0a5931fd-1fd3-3ceb-b4ae-39e89db38b3d | -4.79716 | -48.48202 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c6081d65-1cd0-3404-b295-27a2ea0d025a | -4.1443 | -48.40257 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2f53451-aabe-3620-bb87-a67abb7ac632 | -4.10361 | -48.48552 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 59011263-e30f-3575-b299-d8bf98597b28 | -4.10308 | -48.48922 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b7d25893-e4f7-320e-9982-fbff607b4a1f | -4.09853 | -48.48099 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2d87d7a2-84d8-3c31-af71-d7199d13f4cb | -4.09801 | -48.48462 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bab2e34d-40c4-368c-b2a2-85b377770685 | -4.09749 | -48.48825 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1b431f2f-db3c-3f27-9867-bcf55feb402c | -4.09631 | -48.47184 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ec946832-5283-3ded-b174-eb7f4af522e0 | -4.09575 | -48.47559 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2e2c3bb4-598c-3bef-b0a0-47fbdf980895 | -4.09519 | -48.47931 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f0c1697d-7089-3128-a712-74e2fb7e9dfa | -4.09464 | -48.48294 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 84ebae06-0c57-3844-b93f-e79c296adbbf | -4.09453 | -48.46883 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fd776b30-dd35-342e-88b4-54b7a52bb2cd | -4.0941 | -48.48656 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bd1022cc-be5e-362a-bc1f-3322a20c23a2 | -4.094 | -48.47257 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f3709d54-34b6-3c76-ace4-3a80e585f07d | -4.09355 | -48.4902 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fae1b00f-b32f-30e2-b90e-24f7d629b4ce | -4.09346 | -48.47631 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 108ccf10-316c-3117-b336-d0f9feeba5de | -4.09293 | -48.48003 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f040d245-4985-3903-89b8-fe0eccefa9ac | -4.09241 | -48.48368 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 893d9c35-08cd-3207-bc50-e18b3acb50e3 | -4.09189 | -48.48735 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bf660457-ff7f-33ab-b289-49c09784b0fe | -4.09128 | -48.46713 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb9d6ab6-48a6-3ac1-92bb-00f8fb7e0a67 | -4.09072 | -48.47084 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 972afaca-b0a5-3ed4-8e74-1211f7e69f67 | -4.09017 | -48.47455 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9589ab6a-01ec-3d54-8ea3-084e56fb7f81 | -4.08961 | -48.47826 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b31b417e-7e07-38a1-b407-32f6d67a5b5b | -4.08906 | -48.48195 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9700f87b-f5bb-3994-b04b-e812ad7c9122 | -4.08893 | -48.46784 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fddde53f-9ebe-39d6-beb8-04a73000c7b3 | -4.08788 | -48.47525 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 93b99e99-0f97-3b0b-9005-7297cd1244d9 | -4.08735 | -48.47897 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 99474d69-d2d6-3dd9-9fcc-3ce753738e40 | -4.08683 | -48.48269 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04390e21-b707-3e5c-a387-85d380777199 | -4.58073 | -48.01143 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c411088-c45c-3bf2-84f8-34a17fc00dcd | -4.57429 | -48.01472 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 37face2a-417b-368a-ae04-53c3e13980fd | -4.57399 | -48.0132 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fddf5d54-f3df-36b0-9739-f4be80424977 | -4.57369 | -48.01881 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8262958d-66b0-3448-a87d-d4658f96c021 | -4.57342 | -48.01731 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9a10f83f-519e-3b2c-a7e2-dea046226828 | -4.57285 | -48.02139 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0820375e-57e2-3d37-84a7-98b7f89ab89a | -4.56787 | -48.01794 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cc0a441-f840-3f61-b003-fa4798f6c287 | -4.56759 | -48.01643 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a329cab9-dfa0-3507-bafa-537b606e202d | -4.56703 | -48.02047 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36363d31-2136-3eaa-9fdf-774da7df2181 | -4.4893 | -48.1107 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dc57ee5-878e-36ec-9373-7f1b7081ddf2 | -4.48873 | -48.11477 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9240d673-67a9-3fc0-959b-6a8f4d1b845d | -4.48353 | -48.10982 | 2024-10-03 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0f7a885-48b8-3a51-9f10-743a57c49e46 | -4.28166 | -48.06997 | 2024-10-03 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7e0c09a-cf8d-3464-949f-10f10ce221fd | -4.27587 | -48.06918 | 2024-10-03 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31d7102c-a028-3e30-b5fd-0068260b1f3e | -3.8046 | -47.80014 | 2024-10-03 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 36cd99ee-f181-3d64-8170-6a43a5971fd3 | -3.804 | -47.80423 | 2024-10-03 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f824dce-8f6c-3719-b82e-7519d76bf57b | -3.80341 | -47.80829 | 2024-10-03 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6860208-c555-3385-8138-de9acad578ea | -5.22078 | -47.95822 | 2024-10-03 05:14:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f23bd3f0-38db-35b4-bee0-0cf389fa354d | -5.21689 | -47.95728 | 2024-10-03 05:14:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0894379e-722f-33c9-a8e9-943a2436aaf2 | -5.21486 | -47.9575 | 2024-10-03 05:14:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bc25b92-8ce9-3cb9-b9ab-0f9b6be85534 | -5.46746 | -49.0254 | 2024-10-03 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d0b7c5a-d9cc-3c78-a97c-b657079ead45 | -6.97421 | -49.4332 | 2024-10-03 05:14:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ea94538-0d81-3db0-b835-f0ca1032b857 | -6.96872 | -49.43239 | 2024-10-03 05:14:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0f7c6b0b-9c80-3a33-b065-f5bd59b2ea19 | -6.96823 | -49.43602 | 2024-10-03 05:14:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 869b0d73-3097-30cf-95cb-fd687f7ab528 | -3.31122 | -50.45433 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54747293-cb0a-32c3-b8c9-bf6b2e447614 | -3.30718 | -50.44817 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e42f595-912b-3b96-afa3-d9f99c18ee2c | -3.30639 | -50.45346 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c898769a-111f-3a7e-b0ee-fe709f003383 | -3.24766 | -50.48252 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23ac1b3a-2528-3004-aba1-8f2e5b3ed184 | -3.14246 | -49.42495 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14dc7f71-b07c-3cb7-9c6d-157de6c6fe4d | -3.14199 | -49.42809 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05970bf3-5718-37d2-8495-64e045ba63c7 | -3.13821 | -49.41782 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31bd8314-2531-341d-b41b-061c606edfc9 | -3.13774 | -49.42102 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abb92b50-8c80-3254-8148-a5dd4d9eaf64 | -3.13727 | -49.42416 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61ad4fcc-ba31-3e96-b362-12266c225ffa | -3.1368 | -49.4273 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47e21e06-fa85-3e75-b74d-1909af73c5e2 | -3.11789 | -49.4116 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9517cc17-d168-3a0e-b610-c02b67a00c32 | -3.11315 | -49.40775 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README150.md)
