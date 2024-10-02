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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14eac7d3-4265-3a09-945a-a447f7e2c324 | -13.1499 | -51.23978 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3120981f-1a50-3291-a3b2-0ebc75ee3cfb | -13.14913 | -51.24685 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a791c461-ef0e-3275-887d-ff391d1af082 | -13.14355 | -51.23198 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| dcb6ca0c-fe9e-39f5-9472-6a33b1779f86 | -13.14081 | -51.22407 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 826b1e73-701f-3650-a0c4-22a04b0008af | -13.14009 | -51.23114 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0b22912c-7b02-31e7-a202-6b593a4b6493 | -13.13719 | -51.22416 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 487fd936-3540-3612-8db7-8912f418f34b | -13.13643 | -51.23122 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d1022d7f-419c-391c-847b-ea0125b2ade5 | -13.13368 | -51.22328 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d25b72f9-909a-3086-8c6f-9d82b5ae9a2b | -13.13296 | -51.23037 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e60614eb-fb65-3477-95ac-045301424588 | -13.13007 | -51.2234 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8fed859b-b74f-3e66-94f3-93ba778961b5 | -13.12931 | -51.23048 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 96550864-e309-39b0-97ea-44b92ed36ee6 | -13.12656 | -51.22248 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 34d8fb3b-07d7-3ed0-8626-e19784ac4ff4 | -13.12584 | -51.22957 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8a4db155-65ef-3412-b8fe-c89c34d85a63 | -13.12219 | -51.22971 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1825a4da-1bc6-3382-b6ae-5b8ebff180e8 | -13.11872 | -51.22877 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e164412d-86f1-3d91-a35e-3dc5cc131112 | -13.10458 | -51.19196 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 547937df-963d-3f5a-857a-f74c6d9d204c | -13.10089 | -51.19086 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b864679-b5ef-3a8e-bc2f-dd66f8ac559c | -13.09745 | -51.1912 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12864451-696a-3c4e-a055-353c3d1f8421 | -13.0592 | -51.35006 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39915a01-9853-3b41-b894-d89d8fd2177d | -13.05503 | -51.32154 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85819a07-c308-3060-87e5-141d4d31541d | -13.05431 | -51.32846 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65d7cc6d-06bc-38cc-9f56-7da6b4bf9a88 | -13.05358 | -51.33542 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 815cf10e-32f0-3509-a0fb-cb90eac187e9 | -13.05286 | -51.34234 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efa3f30b-f90b-3875-8076-dc017ff4e30c | -12.89945 | -51.32766 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 82d171f1-7ea9-366d-b944-308a42344e99 | -12.89494 | -51.32796 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 474de5cf-f49c-3cc0-9bd3-5fc2c4cf1df9 | -12.89239 | -51.32685 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d6e0828a-69f9-3a1e-89da-32f9ac49958a | -12.88788 | -51.32718 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fd48ffe7-a965-3e1a-a574-0c1c9d00261b | -12.88533 | -51.32604 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22395412-5a96-332b-acd6-16bd8072e63b | -13.12647 | -51.43389 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| ee25b92a-61d9-3784-9dec-3465d7431d0c | -13.12234 | -51.42672 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 2fd76eb5-c6a4-32d5-91f4-bb05e46883a5 | -13.1216 | -51.43355 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 55760d08-2ebb-387b-89c2-e8e9d8de247f | -13.12014 | -51.42622 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 42287e91-9edd-3d01-bb2d-5da26bbaa171 | -13.11944 | -51.43307 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| da2a92d3-dc4c-3401-9704-43d8be509120 | -13.11605 | -51.41908 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a6047121-3570-367b-8a10-0f24c7e0eb3f | -13.11531 | -51.42593 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 1e61c0f7-76ce-31d3-a073-ded3ab34abc7 | -13.11456 | -51.43278 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| db654c17-c972-39a6-bd5f-65459b70154b | -13.1138 | -51.41854 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 2750eb59-78b9-3423-83bd-7f8a3c44aea8 | -13.1131 | -51.42542 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 80804168-1da8-3ab3-9b37-3553aa12fc01 | -13.1124 | -51.43227 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ed2b81e3-1df2-3312-b5b4-67c554345ed9 | -13.10901 | -51.41831 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 55ad6f33-8fdb-3dbd-b2f2-14ab95fee2bf | -13.10827 | -51.42515 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c04e3352-8885-349c-99ff-0ae654a06297 | -13.10753 | -51.43201 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 18d1fc3b-c681-3ee6-878c-0fa6297a5128 | -13.10676 | -51.41775 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 68313fe2-fa29-3e75-acfa-902318c1fd58 | -13.10606 | -51.42461 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 35eb8cd8-d70c-34d5-9895-65f57135647b | -13.10537 | -51.43147 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f0710e97-441a-3977-a293-6e4908c4ca13 | -13.10494 | -51.39006 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9862fc14-c7c7-30bb-a5aa-74276196958a | -13.10251 | -51.38941 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3320b194-40e2-3db6-9b3d-b97eb0295f4d | -13.10123 | -51.42439 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6307a40f-f72b-3884-ae07-3f4c68dfb2c6 | -13.09862 | -51.3824 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 582210aa-9d06-360a-a4cb-cfec741d5827 | -13.09615 | -51.38172 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f964b2ba-d7c7-320b-a267-1b7cdead10f4 | -13.09083 | -51.38851 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3142a3b9-8d30-3a39-8558-141ff229cd6c | -13.0901 | -51.39539 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f22b84d9-8613-3135-84ba-2723f63b954e | -13.08936 | -51.40226 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 97532242-4fae-3049-9cf0-1b997f0275a6 | -13.08862 | -51.40912 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e6968e9b-5c7f-3ed9-8055-f07551653cb0 | -13.0884 | -51.38781 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2134e717-f1f5-3c1e-9145-c4a38c2e9e0a | -13.08771 | -51.3947 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 00336685-d7c1-32a6-9a00-c4070e319eed | -13.08702 | -51.40159 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 63b09216-54ef-3383-aabd-8d6b15e48447 | -13.08633 | -51.40846 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5401093a-3d56-377b-bdea-93ef8b3b292a | -13.08305 | -51.39461 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 128703ee-91f1-3c58-a980-0b4523cbd927 | -13.08231 | -51.40148 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7cb19b13-0275-3991-9b10-871be3adff68 | -13.08158 | -51.40835 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 49028b44-7e26-340e-b07f-9677fdf0d019 | -13.07998 | -51.40076 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a6a1f510-e765-3602-ad1d-efcf838737f1 | -13.07527 | -51.40069 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 18ff4fd1-3f4d-3c87-a180-363b2a607824 | -13.06481 | -51.36467 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 80ee752c-c1ff-3ba5-b9e1-c0c63359839c | -13.06408 | -51.37157 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 9abbb013-20b2-3e7d-979a-01b13cda7648 | -13.06335 | -51.37847 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 7d4d8dc8-403a-3cb3-b3f6-567a1939db41 | -13.05702 | -51.37078 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd7533af-e1fd-3b42-b26c-ab74721d9eea | -13.0563 | -51.37767 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d7b4191-8591-3878-967c-c775eba97a5b | -13.05413 | -51.39831 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 17d2c6ab-7dfe-301b-812b-f03c037e6be7 | -13.05341 | -51.40518 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 20e5ec3d-9112-3380-8672-6328d2660131 | -13.04709 | -51.39752 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4a2ab2b4-82b2-3d05-99b8-e7f25805d1de | -13.04637 | -51.4044 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 754517a6-3af5-3245-9131-e3fef8049dfc | -13.04565 | -51.41127 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| efc57c43-7699-3d98-95bc-418a1bb68093 | -12.93393 | -51.40804 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d221487b-4d01-32a0-b0a0-d97cdff3c5d1 | -12.92896 | -51.40801 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12040cc8-cef8-3e0a-8ddb-8e7d83fb646c | -12.9282 | -51.41484 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 580b3691-b370-30df-8c35-3ec9260d65d2 | -12.92689 | -51.40724 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d931e40f-ae2c-3b87-a5ee-c55c0e77cfd1 | -13.00864 | -51.5056 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 176cd873-f036-3fda-9d20-40dd114249e0 | -13.0079 | -51.51233 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 12509b78-77a1-3048-a8f2-b33f2eaf039a | -13.00765 | -51.50339 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5579ad2a-dbc2-3bf1-a6fe-c680d28d240d | -13.00695 | -51.51013 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c0aee813-515a-39b0-9fa9-b3de71c5b92c | -12.96519 | -51.51452 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4117c8a6-1481-3cc8-aeeb-fdee9675bb7e | -12.96447 | -51.52125 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f17cfe37-37c8-3a2e-a9e4-c7439ddd020f | -12.96428 | -51.51217 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1ca4fc5-8c9c-351e-afc1-61be98d9e335 | -12.96374 | -51.52801 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5fe230de-d963-3e6c-abe9-918944b526d1 | -12.9636 | -51.5189 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7dcf8ab9-6276-384a-8608-bbd32bf9f47f | -12.96301 | -51.53481 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1dac1db5-488c-3af2-896c-cb338f95d889 | -12.96292 | -51.52566 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10ff47d9-25c8-376e-b591-5bb44e6e1b3b | -12.96223 | -51.53245 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c2aa489-5a60-35a3-89ad-06b0a0edb7e3 | -12.95819 | -51.51379 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4cdefa49-43c6-379d-a045-bb5f9907f528 | -12.95747 | -51.52051 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 646cf05c-43c9-3ab0-b0b0-64d00d9da7a8 | -12.95675 | -51.52726 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0505667-f95b-35f0-8e12-10a0a322b36b | -12.95264 | -51.49957 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac01d7e3-7807-3653-8e8b-b7851ab1fa8b | -12.95048 | -51.51979 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9dba2ca-8310-313b-9757-37bbfb02000e | -12.94564 | -51.4988 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e0ea9f7-257e-3c3c-80d3-14b9c185f411 | -12.94492 | -51.50557 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| edb0393e-c840-3686-9f2d-890e7b9af8d0 | -15.67289 | -52.50976 | 2024-10-02 05:36:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15cc3c7b-f2d5-3a9d-a39c-4a68900362a7 | -12.54785 | -53.14297 | 2024-10-02 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d3893a9e-20a1-3e00-8691-bc23d57d8e71 | -12.54274 | -53.1316 | 2024-10-02 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 35b89193-8472-3a52-b7e8-87fa66173835 | -12.54213 | -53.13693 | 2024-10-02 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README175.md)
