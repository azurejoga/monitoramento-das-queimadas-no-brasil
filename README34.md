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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a335cdb-b34c-3115-96b9-738b6555a53e | -18.01045 | -44.31806 | 2024-09-29 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2048306a-633a-3897-a6a8-22be1d8a9e57 | -20.01198 | -44.21798 | 2024-09-29 04:04:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a8e48539-01ae-3d96-beac-ecabfc45209e | -20.64902 | -46.28341 | 2024-09-29 04:06:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaa51b7c-25b2-3c51-bbc7-a1bc069d1761 | -20.64244 | -46.26137 | 2024-09-29 04:06:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9258d3a1-badd-3f45-ba35-798bc3a6d057 | -20.6345 | -46.28623 | 2024-09-29 04:06:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8832e25b-da75-39c2-9953-eedafd010482 | -20.63416 | -46.28457 | 2024-09-29 04:06:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2864bc0a-b714-370f-9b52-9ca6fd09768e | -20.63097 | -46.28543 | 2024-09-29 04:06:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1f966e5-f912-36de-b747-9f4753fdaf27 | -20.51822 | -45.90794 | 2024-09-29 04:06:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aefca8b9-7c26-3ce5-99bb-7d8816c34484 | -20.51747 | -45.91222 | 2024-09-29 04:06:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba46cebd-649c-3a2b-8848-ac65e628cf59 | -20.40903 | -45.25166 | 2024-09-29 04:06:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c0be7f9f-e291-33ff-996a-63067003a4c1 | -20.40561 | -45.25102 | 2024-09-29 04:06:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a1b57c36-0599-3780-8b0e-6856a8a1f893 | -22.29379 | -46.82741 | 2024-09-29 04:06:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 861253fb-4b32-33e8-86c9-5d8b7ad0fe2c | -22.01971 | -46.04612 | 2024-09-29 04:06:00 | NOAA-21 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 44d25461-94ea-3849-bb67-d424e47f5e48 | -22.01626 | -46.04544 | 2024-09-29 04:06:00 | NOAA-21 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ca4273db-bb89-3cd0-a434-e543e07c89ab | -21.92134 | -45.59331 | 2024-09-29 04:06:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0f38dd07-619b-3ac4-ae05-8d487529c16b | -21.91793 | -45.59264 | 2024-09-29 04:06:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ad4e0db3-0d53-3523-923a-33e2abb5dd59 | -21.7134 | -46.36238 | 2024-09-29 04:06:00 | NOAA-21 | BANDEIRA DO SUL | MINAS GERAIS | Brasil | 3105301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 953fb10e-31b4-3a09-ba5a-e63ae50ee863 | -21.71291 | -46.36301 | 2024-09-29 04:06:00 | NOAA-21 | BANDEIRA DO SUL | MINAS GERAIS | Brasil | 3105301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d744b8ef-6ab0-3f43-b4cc-ddaa9c52ca98 | -21.70942 | -46.36222 | 2024-09-29 04:06:00 | NOAA-21 | BANDEIRA DO SUL | MINAS GERAIS | Brasil | 3105301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 95c73487-c781-3dd7-9d6d-d21f2a922d7d | -21.47199 | -46.8224 | 2024-09-29 04:06:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ee6e6cf3-5a8e-3df8-a07f-729e731f19a9 | -21.46765 | -46.82595 | 2024-09-29 04:06:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2c87f4f6-5677-364f-9026-40d79e50d099 | -20.9966 | -46.46228 | 2024-09-29 04:06:00 | NOAA-21 | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a7ae3971-03e1-353d-8ef8-20b0121b9c82 | -22.99055 | -46.8041 | 2024-09-29 04:06:00 | NOAA-21 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8497fb90-35e7-3ea7-97de-e9068d6906f8 | -22.78385 | -46.79893 | 2024-09-29 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 64c554b4-54c9-38f5-b628-2de2b64df50f | -22.78308 | -46.80327 | 2024-09-29 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b5df49af-1840-3ddf-a180-f1a720986483 | -22.78232 | -46.80761 | 2024-09-29 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c744e3e0-b728-37fd-b8b0-3d8bee5fcd57 | -22.7803 | -46.79833 | 2024-09-29 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8608ff28-d10b-37c1-b4d4-4d5cd5e89635 | -22.77596 | -46.80216 | 2024-09-29 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 04a3a946-6170-37ad-8feb-242df593b6e5 | -21.93898 | -48.4581 | 2024-09-29 04:06:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 889e35ad-da3c-3034-93ac-e6f595b603c6 | -21.93508 | -48.45732 | 2024-09-29 04:06:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87458a1e-a9ab-36b7-970d-bf44e433fc76 | -21.84728 | -48.21424 | 2024-09-29 04:06:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4a01d14-bbdc-305a-81d0-5143c59cdf82 | -21.84631 | -48.21943 | 2024-09-29 04:06:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2074721c-d515-3748-9040-d7b22de1f959 | -21.62116 | -47.74892 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e22bb4a-75ac-3692-84e1-217c7cf6b7a0 | -21.61742 | -47.74807 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a102ee1-a79f-3459-ac7c-9d8bdb07c04d | -21.61369 | -47.74721 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63f7dc3e-ddfc-34c7-9a0a-1a927c8847c3 | -21.61279 | -47.75207 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc4ab5ba-e152-3a94-ba3f-fb78dc3b273c | -21.61202 | -47.77743 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e15034e-b31d-365b-8cd1-960f70ed1ad3 | -21.61111 | -47.78236 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eaca70a4-3840-3fb5-9fde-92257fa7b9d5 | -21.60994 | -47.74641 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60462968-55f8-3b0f-a104-3f65828543ce | -21.60904 | -47.7513 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fd287ae-b07c-35f3-af9f-116ea6dd0142 | -21.60736 | -47.78155 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79313efa-8228-3c99-b92b-030466f4f873 | -21.60528 | -47.75054 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 200e8e73-2d9f-3726-b77e-95d3dc5117a7 | -21.6036 | -47.78076 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bdf4496-0e42-38c1-aee5-49f76abcb8dd | -21.60243 | -47.74485 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6edc30c0-fc69-3f15-83b0-99b35d6c6149 | -21.60152 | -47.74977 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22672d52-93e0-3e5f-8cde-185f8755f2db | -21.60061 | -47.75468 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdf84144-d9e8-305b-a995-0f53ecfedc73 | -21.59984 | -47.77999 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0f2d84e-84bb-36c6-8b23-1ae82d63637c | -21.59892 | -47.78496 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efdb8e5a-6621-3f96-b97d-83349845fc63 | -21.59869 | -47.74404 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5e6fe15-0806-3dda-9cc7-42a22209f03b | -21.59777 | -47.74898 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2283eb51-10de-3450-a73e-78cede4909e3 | -21.59686 | -47.75392 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c12ef3fa-cd6d-3e6d-9a9d-562d1a682944 | -21.59607 | -47.77924 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a1ba37e-6837-3307-b90b-fdd4c679570d | -21.59515 | -47.78419 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8aecafb5-226f-3a13-af37-75cfe66997d6 | -21.59423 | -47.78915 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fc567cd-eb0f-33df-8dfd-57ffda0f010e | -21.59231 | -47.77848 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16eebbbd-9bc9-3119-9b0d-f79d041b090c | -21.59139 | -47.78342 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fd4dc6b-52fd-3d88-9a37-615f287eaeb9 | -21.59047 | -47.78837 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ed49f033-8a46-3ca7-83f8-3b8cf91b499d | -21.58762 | -47.78266 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4149b654-6d58-399d-802d-e4bf27169ef8 | -21.58478 | -47.77697 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d04557eb-5bd9-3657-b2e5-573fcea68da6 | -21.58386 | -47.7819 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8c0dd9c-e708-31b6-a51c-1b512ffacd60 | -21.58376 | -47.76144 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 098b5607-a62a-3df6-be81-9e248187318f | -21.58284 | -47.76635 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b27428b1-f10c-3f89-bccb-30b4b8e25114 | -21.58101 | -47.7762 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b9fff79-3cb8-3e8b-8474-44bebda87ada | -21.5804 | -47.75825 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 24ede737-6571-393b-8010-a7020d95067a | -21.58009 | -47.78114 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93f5548a-5cae-370e-acec-8a4313ac0938 | -21.58 | -47.76065 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 03437a76-59e6-3e42-b048-1128b9e714f3 | -21.57951 | -47.76321 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f6bf3493-1293-3d13-a8c5-a8986423d4ac | -21.57918 | -47.78607 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa4ccd43-16d3-334b-bad6-d30472ea2a65 | -21.57817 | -47.7705 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afad1bc0-1e56-3b97-8ab3-acfa1ba1c6c8 | -21.57773 | -47.77307 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f1fb3bd-8d40-3a64-a12e-f8a8caf29662 | -21.57725 | -47.77543 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 12336c4f-917a-3253-bb33-d521dbe781f1 | -21.57684 | -47.77801 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 810ce4d6-0b9f-377e-b77b-d04dc9d8cac8 | -21.57664 | -47.75747 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e2e821a8-2bf3-35b3-af68-c577fcdfb587 | -21.57633 | -47.78036 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c20bcf10-d66b-3ca8-8fc6-311acee5a36f | -21.57624 | -47.75988 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4b9a74b5-f281-3ab5-a749-011ea6f0297b | -21.57596 | -47.78294 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0b38c8b5-89fd-3744-b30b-9bc20130f627 | -21.57575 | -47.76244 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bd367e84-0e1d-35a9-bdd8-222ac731dad4 | -21.57532 | -47.76482 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8d5fb2a-43b5-3901-aa94-090a1ea483e0 | -21.57486 | -47.76736 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebd4f030-d3eb-3124-92cd-14dd3e42b144 | -21.57441 | -47.76973 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40e87952-dfdc-35e2-ab93-b79ce2eacbb8 | -21.57397 | -47.77229 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33954730-2cf3-3b1c-8219-77a600fbd44d | -21.57308 | -47.77723 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dafa271f-a94f-37ed-bc24-d897113e8b5b | -21.57257 | -47.77957 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fa0cba77-760e-30e3-a38f-7b9126cd0cc9 | -21.5722 | -47.78212 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f479d8c-e577-3799-92ca-9c1441ffcfc1 | -21.57199 | -47.76165 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08023c47-517f-3550-b539-566a9d6d1690 | -21.57156 | -47.76404 | 2024-09-29 04:06:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d28c264e-f1bf-322b-bb84-de47fe7d1877 | -21.13647 | -47.03463 | 2024-09-29 04:06:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 368fa6cf-77bd-36e3-a35a-a88a5b030236 | -21.13566 | -47.03922 | 2024-09-29 04:06:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ba870130-4beb-31e5-95db-7f7a60cd3aa2 | -21.13366 | -47.0292 | 2024-09-29 04:06:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c44f53f-6e38-3ce3-841a-11e3767a1777 | -21.13285 | -47.03381 | 2024-09-29 04:06:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ca2ad18-3a0e-347b-acaf-5e88795ba2b3 | -21.13202 | -47.03846 | 2024-09-29 04:06:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3388ba9e-56aa-3a7a-8a9e-06baa23412d7 | -21.1312 | -47.04307 | 2024-09-29 04:06:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 709477d4-dc0f-3c09-b1a6-e0d3a30bb998 | -21.13004 | -47.02832 | 2024-09-29 04:06:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d698249b-426b-3b19-8fc3-5cab87817567 | -21.12922 | -47.03296 | 2024-09-29 04:06:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ea3172f-22b7-3ee3-9e37-37d50fff0ab4 | -20.86878 | -49.57113 | 2024-09-29 04:06:00 | NOAA-21 | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 514cf319-7596-3716-bdfb-f2475224c396 | -22.37965 | -48.74541 | 2024-09-29 04:06:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ce559869-c8e6-377f-a649-8e8386ae00e5 | -22.29303 | -49.64975 | 2024-09-29 04:06:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 49565656-e44f-3e9b-9144-530c3cf336ed | -22.29102 | -48.65597 | 2024-09-29 04:06:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 04984738-d715-30d8-b34e-8399663e7c00 | -22.28713 | -48.65505 | 2024-09-29 04:06:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a9e4e9ad-d9b6-3eb1-a124-51092a132233 | -22.27836 | -48.65855 | 2024-09-29 04:06:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |


[Clique aqui para ver as próximas entradas](README35.md)
