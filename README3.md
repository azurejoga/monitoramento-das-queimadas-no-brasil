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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec4bcf1c-5a5a-3c1c-95be-49b4c6997b85 | -7.80066 | -34.95678 | 2024-12-31 03:42:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1ce9eff9-f7d6-3e69-9b90-6a11304c882a | -2.71642 | -45.57065 | 2024-12-31 03:42:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc5b3bc7-f3bb-373d-8ee5-279cdfa8e3d1 | -7.79677 | -34.95977 | 2024-12-31 03:42:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| e8529993-b86a-3899-b6ba-ade58cad4846 | -6.0919 | -42.67455 | 2024-12-31 03:42:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ea675f90-bc1a-33ab-8139-cf4c1e73aa55 | -1.57637 | -46.04181 | 2024-12-31 03:42:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b5ed37b-889b-3d6b-8e39-eed310861af2 | -8.08807 | -35.23171 | 2024-12-31 03:42:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5dac161b-47ac-3536-9fb8-3d7ddeba8a5d | -2.71551 | -45.57297 | 2024-12-31 03:42:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f32ed8da-e7af-3dc8-8cb0-63b226c64eea | -6.94965 | -43.01001 | 2024-12-31 03:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5bc23a84-98d3-3dbb-bc1c-0fd7f765a095 | -1.57121 | -46.04314 | 2024-12-31 03:42:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2e9840c-f2e4-3705-992b-e500f694623e | -8.08752 | -35.23521 | 2024-12-31 03:42:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cb602c91-094b-36ad-88dc-34fa0ac92e59 | -6.27539 | -43.81747 | 2024-12-31 03:42:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe80f96a-441f-355c-b302-79eb38d105d1 | -6.87938 | -40.62101 | 2024-12-31 03:42:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8896c7b5-3c61-30a9-9e03-94b147f1316e | -5.52638 | -37.76307 | 2024-12-31 03:42:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24685d9a-b7ee-3f4b-a834-86a9ba0f5886 | -1.65312 | -45.86452 | 2024-12-31 03:42:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df860464-598d-3116-a5d6-80f59c12ecdf | -7.53739 | -35.31331 | 2024-12-31 03:42:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7d681c57-76d8-32be-bfd2-b9d1a38cb672 | -7.81439 | -35.23151 | 2024-12-31 03:42:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 9cff774a-ef11-34fa-b788-3d0e97ece3bf | -4.91712 | -40.75938 | 2024-12-31 03:42:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d1807fc3-7cc0-36cd-b085-226e39ef9bb8 | -4.8782 | -39.04887 | 2024-12-31 03:42:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f6cb2ab9-9da1-3674-b789-a9ae151f98c4 | -3.76577 | -43.95315 | 2024-12-31 03:42:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9569062d-7b12-35bf-a847-8d27a866b978 | -4.9006 | -39.92112 | 2024-12-31 03:42:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 638b358f-a267-3a0e-86c2-4063e9d465ba | -7.05927 | -40.56181 | 2024-12-31 03:42:00 | NPP-375D | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6878ee01-9764-39da-ab4c-a92a60d05f3d | -5.94865 | -39.68362 | 2024-12-31 03:42:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46d66354-e0b0-3376-b48b-0c84ef0129ef | -7.53406 | -35.31278 | 2024-12-31 03:42:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 983ee072-6aff-3e36-9bc2-c7aea69f35e2 | -2.71563 | -45.57523 | 2024-12-31 03:42:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88c1a4be-ff9e-31ff-ac5c-a5b69a299fb4 | -3.78268 | -41.61191 | 2024-12-31 03:42:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b0f9b0d-8fc6-37d4-b12b-91332dc6c9a1 | -6.59682 | -39.42157 | 2024-12-31 03:42:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a73f2fe4-063a-344e-bb09-015b97ef4781 | -7.80011 | -34.9603 | 2024-12-31 03:42:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f62bb12d-26f4-348e-82a2-92978f264e0d | -2.80215 | -41.77886 | 2024-12-31 03:42:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84f7dfdb-e8d2-3c22-89b0-8da41f4904fc | -1.56916 | -46.04591 | 2024-12-31 03:42:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a72519e7-d3ea-311b-899e-2ebd50853835 | -2.83979 | -40.29584 | 2024-12-31 03:42:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 083d88b9-bc55-3288-bab3-5b18c3d0de79 | -6.88347 | -40.62173 | 2024-12-31 03:42:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 86f11b08-3eb6-379f-942f-6dfec7bdc06d | -2.80295 | -41.77386 | 2024-12-31 03:42:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb62a686-f4c2-361a-a6af-1598fb65b4e4 | -3.5535 | -43.56495 | 2024-12-31 03:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f52c543e-792a-3fac-8342-23cb93ed674a | -7.80344 | -34.96082 | 2024-12-31 03:42:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 24affe5f-813b-39bb-a834-675056ea430f | -2.49186 | -45.45052 | 2024-12-31 03:42:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96ec89f9-8791-39bc-9da4-ad8cf43370f3 | -6.13386 | -39.79861 | 2024-12-31 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a0a3e5ca-3c9c-3ffa-b19c-f0f936f1047c | -8.08497 | -35.23484 | 2024-12-31 03:42:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 89e713f5-e316-3eee-9d94-2702cea54b8d | -6.28 | -43.82132 | 2024-12-31 03:42:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d27e1525-fbf6-3eba-8325-442ed5a8eae3 | -7.81494 | -35.22802 | 2024-12-31 03:42:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6da598b0-3f56-39d1-b6ba-978a054a219b | -6.95536 | -43.00561 | 2024-12-31 03:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| ac5adeb1-847b-3e58-92c4-6e8721f16311 | -7.65522 | -35.17095 | 2024-12-31 03:42:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d5898ccf-b06d-34c0-bf16-a413deab1b0b | -4.87439 | -39.04821 | 2024-12-31 03:42:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0aece710-b0c8-3b3a-8156-5bbb8710cc9b | -2.79872 | -41.77456 | 2024-12-31 03:42:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1306a53c-538f-3c06-8a25-6c8cc254f051 | -3.76519 | -43.95655 | 2024-12-31 03:42:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5660a604-67c9-38a0-87d7-ccf12ad9595e | -1.57 | -46.0407 | 2024-12-31 03:42:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0022944b-d551-3d46-8b90-3bd06d2f7fd3 | -6.70361 | -34.96443 | 2024-12-31 03:42:00 | NPP-375D | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c4afe334-6ef1-3224-bbfa-b542c4b6281d | -7.82648 | -35.17612 | 2024-12-31 03:42:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7fac866e-3882-3c8d-8394-e1cee9e81342 | -7.91291 | -35.20748 | 2024-12-31 03:42:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7f15bf29-1300-327a-8907-3344925cd3dd | -4.99627 | -37.09546 | 2024-12-31 03:42:00 | NPP-375D | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4da75536-a36d-3129-97dc-4a887dc5ee6d | -6.28051 | -43.81841 | 2024-12-31 03:42:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a52b4e2-7422-37e0-a549-2d63bcb36302 | -7.36649 | -40.0445 | 2024-12-31 03:42:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bca05303-5c63-31c4-9355-cb2e9af2c7e9 | -6.75514 | -39.14047 | 2024-12-31 03:42:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dbfa6f61-da69-387a-b138-5bb0966d6dfb | -2.81288 | -41.7769 | 2024-12-31 03:42:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a88dabc3-5df3-3037-b97b-2e4352a6963d | -5.21941 | -37.61163 | 2024-12-31 03:42:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a67d8b3a-061d-3f95-8d48-373d97ac3e46 | -4.52341 | -44.23925 | 2024-12-31 03:42:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53bbd3ab-3182-3d07-9ffa-05874172adf4 | -4.62505 | -38.48613 | 2024-12-31 03:42:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d26ec6c-4dd9-38ab-b562-8607e52a534e | -8.05758 | -35.14801 | 2024-12-31 03:42:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9c1a7e6c-3c01-33ff-ae56-a4383ca816e3 | -3.76107 | -41.0293 | 2024-12-31 03:42:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0560ab50-75d4-3634-ad2b-f7f7d6605c28 | -6.27488 | -43.82036 | 2024-12-31 03:42:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8274c1a6-f69f-3546-b9ad-d21a27554d6e | -5.60559 | -37.81255 | 2024-12-31 03:42:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 85644f97-3daf-3c54-98fb-d2715da1e13d | -6.09234 | -42.67321 | 2024-12-31 03:42:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3f08f23-1cb0-3ce9-a040-2d6ec5812d64 | -5.85271 | -39.0827 | 2024-12-31 03:42:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b7ac9bec-9442-3bd3-b83c-3193f1273dd0 | -5.69714 | -35.46772 | 2024-12-31 03:42:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9bbaccd2-d1d8-39a4-920f-887229e957f1 | -2.81159 | -41.78043 | 2024-12-31 03:42:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d7fcbab-aba8-3d74-b6f1-96cfa0596c6a | -7.79732 | -34.95626 | 2024-12-31 03:42:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| ca511923-98cb-3a43-b44e-158e317a49ae | -4.5348 | -44.23794 | 2024-12-31 03:42:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee8f7a00-ec57-3352-b362-42734dc4449c | -2.80344 | -41.77534 | 2024-12-31 03:42:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2eb679c-48a3-3450-9894-2e898ec38fc6 | -8.0914 | -35.23223 | 2024-12-31 03:42:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe184fcf-8664-3da9-a5c5-a828097c8dc7 | -6.38843 | -39.39723 | 2024-12-31 03:42:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e0e7c439-ef49-3a8b-be80-40bc691f5771 | -2.49261 | -45.44595 | 2024-12-31 03:42:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87b90c6d-0a08-35ff-963d-8ba95db75ab1 | -2.84144 | -40.29659 | 2024-12-31 03:42:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e04b11a2-1fa9-3325-9672-3f8564998d6c | -7.91624 | -35.208 | 2024-12-31 03:42:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b8979a72-6d16-39a8-bc17-0b77a66dd1be | -4.51858 | -44.2348 | 2024-12-31 03:42:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7a5fbdc-493a-3f17-9648-e67bee0a1908 | -4.5294 | -44.23683 | 2024-12-31 03:42:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dcc65d5-b0b1-3ed2-ba91-83056a879309 | -6.19846 | -36.57106 | 2024-12-31 03:42:00 | NPP-375D | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d8cad50e-e1ac-31d8-a8f4-bbacb5e7b25f | -12.05993 | -40.01483 | 2024-12-31 03:44:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 456640bf-f280-348e-bc6c-411c960914e9 | -9.86647 | -37.19875 | 2024-12-31 03:44:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f1a87e07-7c9f-30ba-bcad-e811a24bd969 | -9.13759 | -38.4348 | 2024-12-31 03:44:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f9c788b6-2991-3668-8883-6d93bae40242 | -10.1595 | -36.36412 | 2024-12-31 03:44:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5faa9b2e-3b20-316e-bd5a-5a81d1e62429 | -9.88083 | -37.23818 | 2024-12-31 03:44:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8a43d5cc-82cb-39a4-a3d9-05fdd69f50d8 | -10.6378 | -40.21585 | 2024-12-31 03:44:00 | NPP-375D | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 703f80fc-2551-3dcc-979e-2a67974f60b8 | -12.83978 | -38.33787 | 2024-12-31 03:44:00 | NPP-375D | LAURO DE FREITAS | BAHIA | Brasil | 2919207 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4b362229-ab39-3e53-b2aa-fddc1bf5c2b5 | -12.58496 | -38.96515 | 2024-12-31 03:44:00 | NPP-375D | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 00633d81-0b20-357f-9be5-2aab71d7875b | -10.63871 | -40.21386 | 2024-12-31 03:44:00 | NPP-375D | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 77c6a547-8b23-3b92-b6ef-574f05e9b3d3 | -12.35722 | -38.27675 | 2024-12-31 03:44:00 | NPP-375D | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2df3eb90-d19a-33b4-85ad-2726a7097c55 | -9.19194 | -35.50589 | 2024-12-31 03:44:00 | NPP-375D | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c6b2d350-a3b7-31c6-abe5-d596b56e20d4 | -9.12841 | -40.64315 | 2024-12-31 03:44:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4a78ae9c-ab8d-358c-9a9c-4bf83869e266 | -11.1285 | -37.23906 | 2024-12-31 03:44:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c04d1f5a-245e-3481-9c7e-94a94dde51ed | -9.14111 | -38.43537 | 2024-12-31 03:44:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0314d927-b61e-354b-9e9f-3fd19772bfba | -22.78603 | -43.75725 | 2024-12-31 03:46:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 67d12fa5-8e81-3d12-945e-09f9ad5eb486 | -19.83952 | -40.08264 | 2024-12-31 03:46:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fcf2b719-b5a7-3ece-90f2-43634412c433 | -19.71677 | -40.35199 | 2024-12-31 03:46:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cb165432-311b-3081-9ef3-959682247ce7 | -23.043 | -49.89589 | 2024-12-31 03:49:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c0171f07-fe4d-3f87-9ec4-069bfcd4d38e | -23.04842 | -49.89766 | 2024-12-31 03:49:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7a14edcc-5df4-332d-b353-19519392cb93 | -22.53906 | -48.81509 | 2024-12-31 03:49:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dd445bf-8beb-3d55-ae6a-858ef39471f4 | -23.9859 | -48.91814 | 2024-12-31 03:49:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da5c0e7b-6d1f-3918-b364-9dd50b6fe74c | -23.9808 | -48.91686 | 2024-12-31 03:49:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a3aa187b-32fb-390b-931a-8650464978a9 | -22.5398 | -48.81165 | 2024-12-31 03:49:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b138f375-44d8-37dd-83d1-61c7f09dac25 | -22.11849 | -51.47228 | 2024-12-31 03:49:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| de560d8e-0d56-33d2-90bb-b80cf2e3b6dd | -22.12097 | -51.4618 | 2024-12-31 03:49:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |


[Clique aqui para ver as próximas entradas](README4.md)
