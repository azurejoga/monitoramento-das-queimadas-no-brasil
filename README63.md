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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b4712be-a45a-3030-b762-0410d6a8fb95 | -13.27319 | -51.2847 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 875095a7-1973-3c94-b1c6-34e3e907cf2a | -14.15916 | -47.39572 | 2026-09-15 05:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 54bc4a12-3e84-3761-91d5-b23a3ea11e16 | -13.30266 | -51.28933 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a1c8e09-e88a-3c4b-a3ce-f91378686ffe | -14.67397 | -48.00948 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c416720d-17c8-30ed-b3e8-9f13770375a5 | -14.20523 | -47.42659 | 2026-09-15 05:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2c7a0a7e-1893-34a4-84b6-7cd5d28a16b2 | -15.04893 | -48.55785 | 2026-09-15 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b3ae9fe-4a1a-3a1d-8906-82a878835ac1 | -13.26539 | -51.28088 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba4c9175-9afa-3a9f-8ce3-b652ab34a0bb | -13.26001 | -51.28017 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e816d6af-e8b0-3ded-a657-9161ea417b07 | -18.16693 | -51.76671 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd5928e0-913c-367f-943d-9e4bdc2b13a9 | -16.76791 | -52.84162 | 2026-09-15 05:21:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11ee3bfb-33d3-33a4-a6c0-9c9beabfd273 | -13.39318 | -57.02596 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad7316ba-cdf5-3cf4-a364-90a1b789ddad | -14.21255 | -47.42123 | 2026-09-15 05:21:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14f84089-9358-311f-aabc-4b3b58793b23 | -14.20545 | -47.4224 | 2026-09-15 05:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5e1c23e9-96ce-3fbd-bc3c-07b074fd0144 | -15.57596 | -48.81741 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b601fcf-a343-36f9-b387-db7a03274a36 | -12.1345 | -57.18594 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94355490-c02a-3154-acd0-d817d617aff8 | -13.76533 | -48.80551 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ce6177a-a50c-3e5e-9258-ae5ef0f6322d | -14.66056 | -48.00769 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 638c7ba4-2a72-37d8-914d-3bd932481730 | -12.13027 | -57.18964 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d4e5fa0-7a5f-3c74-9ef5-0a65096ef7f4 | -15.58141 | -48.82855 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0714728f-4690-3e4a-bcc2-26f63d8a725b | -14.69371 | -48.01592 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8a7d0ae-490d-3da6-8ef3-d8e6d8cccc94 | -12.12182 | -57.19701 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b41a8e38-fc4d-3ef3-a75b-2948e5fa0945 | -12.12304 | -57.18855 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05746de0-2ba6-3430-b2af-0504a32e5b84 | -18.16808 | -51.75549 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7c8229a7-e764-3c76-ba27-2f72cd08adaf | -13.29688 | -51.2921 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a3aa212-7c9e-3c37-8853-e71ff2653de3 | -14.68749 | -48.01007 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b263327-f932-3213-b0cb-a8a2ffd63775 | -12.12665 | -57.18909 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2abbb9f-d5f0-3f38-b5e5-62fedd2e18ee | -15.55515 | -48.8204 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87ee2871-3c7c-321a-acb4-e42bd7828bb4 | -13.30722 | -51.29703 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e3adcf5-7308-3279-a607-3025b9cc28d1 | -15.05233 | -48.58536 | 2026-09-15 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5a795e5-d4d4-3f61-9ef4-1fd553bb255b | -15.04838 | -48.56315 | 2026-09-15 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d113ca15-2b12-3f5d-8f02-3824cd22e57c | -13.70463 | -51.81741 | 2026-09-15 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7670d191-3893-332f-8f25-c399736511e9 | -10.84374 | -60.81421 | 2026-09-15 05:21:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e10f2c0-e81a-34f5-b0d1-7c0aa9fd1d00 | -15.8682 | -50.18116 | 2026-09-15 05:21:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b40e7f24-96e0-38fb-a212-2cbdbd59a56d | -15.58243 | -48.81818 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ccd04d3-9011-3a99-9c45-70a42f140e6a | -13.57162 | -51.44814 | 2026-09-15 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 54961e23-a9e0-337e-bb21-afe36486b197 | -13.56885 | -47.9048 | 2026-09-15 05:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5955f06b-8080-3523-9b2a-1f0040edbd68 | -13.39193 | -57.03501 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 282aca0d-56d8-3f15-936c-b01dd19b6ad5 | -14.67115 | -48.00753 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d742f605-3fe7-3728-8776-c01211ef91f7 | -13.27535 | -51.2893 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a575e168-ce32-3b7a-b187-85e5c625bede | -15.04539 | -48.58895 | 2026-09-15 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e01bd24e-1a6b-386c-a4d0-9252a37438b4 | -13.39131 | -57.03952 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bdf767e-230c-3d32-8a1b-d99da21fb001 | -15.57873 | -48.78222 | 2026-09-15 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4470f263-deb8-372a-9ec8-ae4510ccc152 | -13.57697 | -51.44883 | 2026-09-15 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bc6200e5-4fa6-3316-96d3-2000e4883345 | -16.8654 | -50.15546 | 2026-09-15 05:21:00 | NOAA-21 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2567b934-546f-3857-8030-5d9f0986268e | -14.67451 | -48.00381 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3a29efb-1e7f-3637-accf-14a9e4981bde | -12.13089 | -57.18539 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c393a284-c24d-3f34-8122-0aa51869f0f6 | -13.265 | -51.28437 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 720024b4-81c3-377e-8d32-3d76dc01aa17 | -13.29769 | -51.28511 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b44d001-59e4-3152-8870-243c108cec3a | -13.59601 | -47.90364 | 2026-09-15 05:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c89d73b2-1f76-3e0d-9157-8835fc9207be | -13.30185 | -51.29631 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f82e580-514c-361f-8e9c-d02d1bfa1d6d | -13.34907 | -51.71208 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef17a651-a877-3559-bce8-96541f45feb9 | -18.16331 | -51.74725 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c1ad4c2-2b35-369d-9f06-6e1e3baa5092 | -14.67846 | -48.00245 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6744f5a9-33b4-3f07-ac93-99001d81fa8d | -13.57327 | -51.4482 | 2026-09-15 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 070dd6b4-fcdf-380d-9d72-6cca372e3d13 | -13.30225 | -51.29282 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeaf9a39-1230-3c41-a110-7c4be6c6cb73 | -15.55459 | -48.82583 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2150f57d-c489-32d4-899d-8a901bc74642 | -13.7712 | -48.81075 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7e22a96-fa35-3b79-9fbe-a2d4f4ab028f | -13.26781 | -51.284 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4830c082-fd75-365b-ab6e-baa5c0fe3ace | -14.07098 | -52.15168 | 2026-09-15 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 604e514f-a6fb-3dfc-a64c-ec811a516bd7 | -13.40429 | -57.02761 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15151cb6-a3d4-35f7-9257-45d4e3f943b2 | -18.17405 | -51.75211 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4f1c3bba-e5f8-335c-b099-e5686b18bc2d | -13.72861 | -48.97471 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 144212c9-3af5-3d0d-8f3c-310e6d812c34 | -15.60237 | -53.78237 | 2026-09-15 05:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 032583cb-56c0-32a4-a580-db59a9b25619 | -15.05263 | -48.58579 | 2026-09-15 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d230752-3823-3543-b5a4-ec89efbc60c5 | -13.29729 | -51.28859 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c06e5af-9ebc-3ffb-be1c-aed8802069ef | -13.78361 | -48.8148 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31085663-65d9-3d66-84b5-ad595fe27b67 | -18.16731 | -51.76292 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2b103750-c181-3ccb-bec8-11a28f662353 | -13.27038 | -51.28509 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c27a691-d88b-303a-87da-b7d3bc9f9207 | -13.76582 | -48.80082 | 2026-09-15 05:21:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15a08146-b0d1-3cfb-a3c7-1bf9262c2a5e | -15.58784 | -48.82959 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 85a82b07-1950-3725-8a77-124f421f45f7 | -13.40492 | -57.02308 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 054ff131-cb5c-3807-814f-e7b786250717 | -13.57123 | -51.45156 | 2026-09-15 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c510e897-d717-32ff-b05e-9b3a3c47435c | -12.12365 | -57.18428 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 350b09d6-7923-30d5-9604-f7cd1d3f959e | -13.39501 | -57.04007 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0605f713-18ce-36a9-a053-e531ec1c54c5 | -12.11881 | -57.19224 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 706cda73-6568-382c-b512-26efb94e4540 | -9.4102 | -62.7113 | 2026-09-15 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ac5f1c18-6ab9-36c5-b84d-5321779ac90c | -9.4102 | -62.7113 | 2026-09-15 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 3bf96bb7-9269-3556-91e0-c7553f50aea1 | -18.1709 | -51.7685 | 2026-09-15 05:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5d9ba465-fdcf-3856-8bc7-4b94056725f4 | -18.1714 | -51.7466 | 2026-09-15 05:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 445b7ee2-f345-34eb-a35e-e65e3bf6d7d0 | -9.4102 | -62.7113 | 2026-09-15 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 45f6206a-5a4c-3376-a548-d228005b61f3 | -6.01903 | -59.93644 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 313c9870-b14a-34ab-8975-6ca32cba31da | -9.57796 | -55.14162 | 2026-09-15 05:53:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 619818bf-23ee-32c7-9bb9-9146ac516d0b | -6.79319 | -58.79395 | 2026-09-15 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d988056-2a59-3886-a717-361617502755 | -6.84798 | -55.53793 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbfe8479-60c6-3172-ab6e-fbfa3860e3f7 | -2.82036 | -51.33654 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69959bd9-3a3b-370e-8221-9ca1c5dc0b53 | -8.08437 | -61.80297 | 2026-09-15 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64132376-62ae-3e18-9acc-ef747adb0012 | -1.68538 | -55.90261 | 2026-09-15 05:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ddc911b-a73f-3875-be18-8e4ea417828f | -6.87988 | -59.63535 | 2026-09-15 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5042bdf8-7f63-3f86-b738-9727ed1bc2d9 | -3.48367 | -54.67009 | 2026-09-15 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b55d6a46-2a3b-392c-88f7-28d27b5374c4 | -6.13843 | -59.88166 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 97a514f2-704a-3e74-bced-c88777f8f96f | -6.74094 | -59.43179 | 2026-09-15 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 891cb62f-6efc-3250-a1e8-7ae571a2b653 | -3.54392 | -53.98953 | 2026-09-15 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b65e5c16-f459-3463-8940-c7a5beed9742 | -5.58939 | -60.18641 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68c30eca-4e2e-3510-be2b-96290537eecc | -6.87928 | -59.63935 | 2026-09-15 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c04a8f9-467a-34e2-a1ee-5a5f1a3a50f3 | -6.11107 | -59.88605 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3af08d73-43a3-3bab-876d-8c806c1895ce | -6.68721 | -58.69241 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10c54fe0-ef5a-35e8-a435-7672c4a13083 | -6.32907 | -59.99192 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98082a53-1173-3cd7-8fb2-1fedfbbe3897 | -7.87708 | -54.72166 | 2026-09-15 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfae19a2-1185-3bea-8500-cec777ef6cc4 | 2.58337 | -60.30162 | 2026-09-15 05:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b0c6a45-af40-3ad9-8c4b-62d9978cbd46 | -3.25725 | -54.51887 | 2026-09-15 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README64.md)
