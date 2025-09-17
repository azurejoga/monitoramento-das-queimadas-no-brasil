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
| 6d3cd2d6-bcdc-33fb-ba1b-372bb0986b40 | -23.48387 | -46.40342 | 2025-09-17 03:49:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b95efc36-4bf9-3cdc-9cad-8201cf0eb448 | -23.72222 | -47.10317 | 2025-09-17 03:49:00 | NOAA-21 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0d605a64-8baf-3824-8cce-dd182d28dacf | -23.13624 | -47.01322 | 2025-09-17 03:49:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6031dfc0-7dd6-3955-8b3a-18c51bbac5c7 | -23.80546 | -50.98029 | 2025-09-17 03:49:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b3d7056b-26e6-38e9-a7b9-6bdaff8ff8fe | -23.21417 | -47.0497 | 2025-09-17 03:49:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7847dc9b-cf3b-3220-a6a3-fbd551abf4bc | -23.67982 | -51.65448 | 2025-09-17 03:49:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 813eca0a-77a1-3a26-b056-cc9f55118b1b | -23.80546 | -50.97985 | 2025-09-17 03:49:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ba2d762d-ad28-3e66-a419-b81b492e0823 | -23.50891 | -47.05146 | 2025-09-17 03:49:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d3bbe4f8-de24-388b-ad94-b603a933f5db | -23.80647 | -50.9755 | 2025-09-17 03:49:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c5131a30-cd78-3295-9d96-af4ac9aa31f5 | -22.33412 | -50.16309 | 2025-09-17 03:49:00 | NOAA-21 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3985176a-aa0b-33b6-b051-fd8ecc27d454 | -15.0179 | -49.4579 | 2025-09-17 04:00:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 9495cbff-1781-35ef-980d-730a562d40ae | -13.2807 | -54.1814 | 2025-09-17 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f0d461be-0af9-3ab9-9e9b-f680172e02f2 | -13.2804 | -54.2021 | 2025-09-17 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0b9462ec-bcd4-3f68-893e-35a7934f1295 | -2.92054 | -40.42042 | 2025-09-17 04:08:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0388100-be7c-3295-ae16-e219fe57034f | -3.03099 | -41.81541 | 2025-09-17 04:08:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 89c145bc-f0e9-3917-bcdb-3a3149dadefa | -3.60326 | -38.94851 | 2025-09-17 04:08:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| e937059f-b67f-3854-9d16-e93a65902a82 | -3.59982 | -38.94798 | 2025-09-17 04:08:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 58fbfb1e-8d31-3497-96ed-b5a650e0cf7a | -2.26219 | -47.19563 | 2025-09-17 04:08:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 679883b0-f3c3-3636-8d37-c176db4b4245 | -2.91834 | -40.41953 | 2025-09-17 04:08:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 31fb42fb-6bad-3fac-9de7-27a78bff175a | -3.59924 | -38.95169 | 2025-09-17 04:08:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd1c9506-7df8-31e7-8605-d67a2a06436d | -3.0092 | -41.83383 | 2025-09-17 04:08:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74287e81-ab63-3699-be17-5e7caf6f120a | -3.60268 | -38.95223 | 2025-09-17 04:08:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 58cd47bd-c3ec-31df-84e3-67401c76bea3 | -0.75609 | -47.75762 | 2025-09-17 04:08:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea6b0586-7c87-3b73-be6f-b5aaec73265c | -2.26186 | -47.19268 | 2025-09-17 04:08:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 764eb4ba-d4a2-3bce-9913-5dda48e0bac9 | -1.6918 | -47.07327 | 2025-09-17 04:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46bcb1e1-354f-370d-bf0e-609616140086 | -21.564 | -50.1063 | 2025-09-17 04:10:00 | GOES-19 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.4 |
| 69a6e8ec-0ff2-37bd-9de3-4fac48b562e4 | -13.2807 | -54.1814 | 2025-09-17 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 01dc9160-f33e-3290-935f-cdf86c073485 | -21.5634 | -50.1292 | 2025-09-17 04:10:00 | GOES-19 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 185.1 |
| d7f19d6e-0949-3d9d-a484-65ba1aca9ceb | -5.09223 | -41.15087 | 2025-09-17 04:10:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc8b5031-dde9-3e87-89a5-b8cbcdc5dcb6 | -8.56659 | -46.34599 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f96c644e-6d09-3fa0-b693-837089c29f98 | -5.59919 | -45.37988 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc43900b-096e-3a32-85e8-7a4b2c5c25d3 | -5.64182 | -37.48643 | 2025-09-17 04:10:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 833b17c7-b1bd-39d0-9fe1-45fa7cfde903 | -6.45725 | -43.31575 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a8f7d50-a83d-3c53-ba82-92837a697c1d | -8.92995 | -46.28193 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 363dfa40-becb-3544-b18b-5c5bd75be345 | -8.67891 | -46.36753 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a961970-afe8-3013-8a9d-a98b0ec70b61 | -8.56742 | -46.34118 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1a6cc674-0262-3645-a527-15cd1c3d581c | -7.31721 | -43.98483 | 2025-09-17 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d1fb534-6070-3adf-9a9b-4356af953651 | -2.26409 | -47.88377 | 2025-09-17 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 751cf338-8312-3d2f-86ed-72b2824ba87f | -8.67668 | -46.35732 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad37d971-73de-383e-ae53-00dba45148c5 | -2.83589 | -48.6618 | 2025-09-17 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 713a639a-98c9-3d46-93e4-10a133308d08 | -6.47948 | -46.00826 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 382c870f-2973-3736-801f-cc87c7aeece2 | -5.13345 | -45.11589 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 27fdd543-f88d-3601-9a90-02b29b7d3e67 | -3.8747 | -41.62039 | 2025-09-17 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2d54248b-6a07-3144-9b0f-35c5b265370a | -9.23894 | -45.64783 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efdcaecc-23b5-3db2-8bf6-725a86ebe659 | -8.4381 | -47.68243 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0738debf-5dd5-3e6b-95da-e66a0aa00511 | -6.17397 | -44.50503 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6271cafa-b58e-3d18-aed0-b693417469fe | -7.58081 | -44.5788 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8bfdd9cd-bb90-38f5-ab31-c18e4450cebd | -6.37945 | -42.84368 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0eea3402-6468-309c-b93a-3a5f3e305652 | -6.87692 | -43.96354 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 491d951e-a196-3570-be4d-3b986b4d7e55 | -7.97333 | -45.62902 | 2025-09-17 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 93ee0df1-2a2f-36c3-8724-a2522034fd9f | -3.06872 | -49.46055 | 2025-09-17 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd67d911-f59f-3fdb-a7bf-481ff74d009e | -8.54051 | -48.97432 | 2025-09-17 04:10:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8b29d683-1e2f-3cac-a8cc-b067a4a51452 | -5.99767 | -43.69174 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f27a4843-6a9f-35ca-8af4-d63a1aa2a021 | -8.90508 | -46.28027 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79009c84-8096-3c3d-a4de-4547af10edd0 | -8.16274 | -46.75477 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a086386-ae35-3170-818d-c965351bd49a | -5.61176 | -42.90401 | 2025-09-17 04:10:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5e296362-02e4-3e7e-9f43-7372cca428b5 | -9.14649 | -46.93788 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6682e18c-2c62-3fd9-b8db-78248c4f2f31 | -6.45665 | -43.31948 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a4420bf-b89b-3e74-85cd-dc3b1254a714 | -6.25264 | -43.45549 | 2025-09-17 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 394ea437-ed18-3dbc-8d04-ef6d203686a9 | -3.06836 | -49.46013 | 2025-09-17 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b268546c-49cb-3e25-abcf-1b192be0ca01 | -5.80478 | -45.70519 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52880b42-d181-3816-ac92-2cee4ae1864f | -6.00116 | -43.6923 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e37f681-9563-3794-8755-0284c467f74c | -7.58148 | -44.57476 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 839ef51c-3a8c-334d-85af-4abce8867646 | -6.15829 | -44.52962 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7202329e-f52b-3e16-ab3b-74dc65de45b9 | -6.42235 | -44.00823 | 2025-09-17 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18f53130-cc34-3dab-976a-1057de619b2d | -7.8295 | -43.85478 | 2025-09-17 04:10:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f21628d-9b81-3cde-9a00-5211459cdfac | -6.16218 | -43.67375 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46f3a0c7-7951-34b1-ba6b-ad9367ab04e9 | -6.76286 | -37.89253 | 2025-09-17 04:10:00 | NPP-375D | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c4d709fa-6090-39bc-975d-5547c6ac333f | -6.18468 | -41.2168 | 2025-09-17 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 356307d6-d16f-3e77-b267-49c5b14b0f4b | -7.68577 | -44.47245 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1d05ca3-db6d-3598-8ee6-4615ea794f44 | -9.05129 | -44.83294 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e99ca6e-aa15-3d9a-bffb-382a4145b3e1 | -8.98778 | -45.75529 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 85334c38-9671-3fb2-8d3c-8c8979ec6b37 | -7.64613 | -44.47014 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03561b41-2458-3d4c-ab89-0712cd593959 | -6.6739 | -46.3073 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d9c15d97-56ed-370c-bac4-9aa3c5cf84b9 | -6.39765 | -43.33657 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc48b804-0f23-3472-b847-1092a0db5e23 | -5.81654 | -46.36204 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63f8177b-e049-31d7-bfa3-c608c8eb334e | -6.18081 | -41.21975 | 2025-09-17 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 833e4480-508d-39bd-8210-70a002a7442b | -7.41198 | -49.98701 | 2025-09-17 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee3ed733-9f63-3f52-b888-90720bd2a5f1 | -7.3238 | -43.96609 | 2025-09-17 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7840d910-6d6e-3251-bd1e-1ec8f7e25df3 | -8.68888 | -46.37902 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07a09703-ef86-33f5-bc8f-9029f3ae6d21 | -8.63564 | -46.43281 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 832c24a5-3176-3fb9-ba17-aa2c29a88e70 | -7.40857 | -42.07987 | 2025-09-17 04:10:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ceb50124-1357-3608-aeda-49ea03a47335 | -7.26878 | -46.57844 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| db75a14f-08f0-35f5-bb39-06c24cada0ca | -6.0384 | -43.14039 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 219d6ec1-4a0e-3bd9-976c-b0e1903f915c | -3.41906 | -46.96816 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc085389-9ddb-3925-b952-c5545383f4e7 | -5.81191 | -46.36492 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eceacf57-450a-3924-8987-c3b66af35d89 | -8.63582 | -46.40781 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b664b03-730a-38bc-8b95-dae644f28d80 | -7.64968 | -44.47071 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d299ce6e-8a67-3643-9630-7bf3a3255014 | -6.28544 | -42.37906 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9080fb28-613f-38ee-933c-61841cf9035c | -10.15429 | -45.29462 | 2025-09-17 04:10:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 595d75c1-0881-319e-ae67-3923d84578b3 | -5.9882 | -45.85483 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bb7ea91-fb9b-3e20-9ea4-15f2428c4adc | -8.96187 | -46.32666 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e645b77-db9e-33bc-a0de-23ea537a715b | -3.4183 | -43.14896 | 2025-09-17 04:10:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17e92660-a91b-37ef-ba02-42ec3422fe2f | -7.38372 | -50.00008 | 2025-09-17 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 616fd00e-028d-3def-84ad-7077d874ac3f | -3.42179 | -43.14952 | 2025-09-17 04:10:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60f25b23-650d-3112-b697-a3cc02aa3b19 | -4.32727 | -48.39045 | 2025-09-17 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6548800-e9ad-3d36-9e9b-0157bcaf1fc3 | -6.67253 | -45.31626 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29cc8f1e-6f96-372c-a68e-77ec549c4c73 | -6.16329 | -44.52474 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dac956e2-7b12-3204-a201-a838fe692173 | -8.63176 | -46.4321 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e9b2122-d0fb-3a00-b201-b496c2f67497 | -8.15786 | -46.75258 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README18.md)
