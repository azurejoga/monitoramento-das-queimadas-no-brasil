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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9301ae56-b5ec-3277-8a65-46410c344cc2 | -8.33598 | -70.91847 | 2025-09-22 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c8bc3ac-54da-32e8-8b4a-9c84f8e00168 | -7.59012 | -69.89192 | 2025-09-22 06:20:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 980c9e2c-ef4d-3480-8e37-67eef471e4c0 | -9.47017 | -67.10343 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1748a5eb-336e-31dc-ae8e-489925372346 | -7.56718 | -69.9069 | 2025-09-22 06:20:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa2dc18b-a098-3c4a-b949-b8ec32c8dde1 | -9.4694 | -67.89339 | 2025-09-22 06:20:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e4a7960-ead3-3547-92f2-b4b467eeb364 | -10.17244 | -68.79315 | 2025-09-22 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed5b157d-d44a-3dfa-9af6-1abcdc3e7a4a | -8.98313 | -65.45583 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 83c96ee0-1b68-3eb0-a595-d32eda162b9d | -10.19487 | -69.35206 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d53c2acb-e536-38d2-b261-4f30149f0b3f | -9.59408 | -68.57929 | 2025-09-22 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f05d9dcd-b242-36e8-a49a-b48a2e0bf87d | -7.24642 | -72.50576 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22e85503-8da0-3e25-a83c-28c6eb820418 | -9.81783 | -68.89557 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0258397-361b-3dd3-8ef6-85ed4b11661d | -8.63125 | -69.26618 | 2025-09-22 06:20:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14898dcd-e063-3d97-82e8-acf53bf0de49 | -10.01935 | -68.40699 | 2025-09-22 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3bc5dea-4fca-3256-9b1e-6d7b7dca6acd | -10.92017 | -68.58868 | 2025-09-22 06:20:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 433d8b18-1295-31af-985b-e6d2ced05de3 | -10.19051 | -69.35142 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20fed8ac-e21a-3aad-86fb-b14c0e64c539 | -9.74026 | -68.43764 | 2025-09-22 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fef5f563-b24a-3cc9-8af8-978ac673f6f8 | -9.6805 | -69.01398 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63c17b20-b281-3c51-8120-eda583da6231 | -6.59358 | -62.92551 | 2025-09-22 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99315210-fdd6-3444-bfa7-bb041f392b21 | -8.74023 | -69.10291 | 2025-09-22 06:20:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 145a9490-889d-3b69-842d-66c27bed7fbd | -10.91822 | -68.591 | 2025-09-22 06:20:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44848e50-6990-33f2-943f-a4ce7179ee87 | -10.16226 | -68.69633 | 2025-09-22 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 452b32ed-df96-3b52-ab88-e74e9fcdee2a | -11.88005 | -64.93439 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5b65acac-9fd0-3152-94ad-978f8875a278 | -9.11582 | -65.50415 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bd8583c-af6d-3d47-a3af-da6d8bda2ac1 | -8.57115 | -67.86288 | 2025-09-22 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 725112e9-e981-35fa-a228-acc9bfbe2ebf | -8.63985 | -69.26736 | 2025-09-22 06:20:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d400f94-7fbd-350f-a00f-8362eeab4704 | -9.79919 | -68.88062 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b27f55dd-9076-3d03-9d85-99a220274468 | -8.04628 | -71.23615 | 2025-09-22 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f18bb1a-80ed-3373-be18-a2b481c6388f | -11.87403 | -64.93364 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1c9aa96-2f9a-35b2-a325-fee5b3eae6e3 | -11.79283 | -64.92936 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 467fe32e-3b1b-3769-83af-7e0ef405e46d | -8.0485 | -71.01422 | 2025-09-22 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2396540d-b8f5-3c3e-ba20-4bbb9b8c4d8b | -8.0643 | -70.338 | 2025-09-22 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9df24e5-df43-3d60-ad7e-f1b17ae96bf5 | -11.87951 | -64.93891 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 963513bd-1a6a-37c4-a7b5-ddb818ad9830 | -8.10802 | -70.50188 | 2025-09-22 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6369740b-391b-34a8-8d02-fc73ecca0689 | -8.63555 | -69.26677 | 2025-09-22 06:20:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9784c604-0c33-374b-bf03-557bfb801744 | -7.85652 | -70.11489 | 2025-09-22 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92c9c244-aae6-3da3-94dc-f051db8d4901 | -7.5626 | -69.90992 | 2025-09-22 06:20:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7df84758-e656-3330-813a-fcce61e6fcc2 | -8.29244 | -71.0648 | 2025-09-22 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7b06384-046d-3668-a3b0-7a709c76100b | -8.5559 | -71.02819 | 2025-09-22 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abc030c1-7ff2-3e52-affd-131edf6ec559 | -9.67606 | -69.01333 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 754f6882-474f-3068-8a1a-c1ef1fe87666 | -9.11533 | -65.50787 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b7417c3-0285-358e-8b5f-1651f64aebd7 | -9.3619 | -68.32932 | 2025-09-22 06:20:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 202fc4b2-4491-392d-8e3b-c075df8009eb | -8.49067 | -71.44884 | 2025-09-22 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1d71648-0738-3f4c-b0b7-0a0659aa077b | -8.0244 | -70.83143 | 2025-09-22 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2f06659-f278-3f51-b128-517244f9e817 | -9.4486 | -68.58562 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73d3ddfc-b8c5-3ec8-aa56-b53d5dfff6ae | -9.91921 | -65.04987 | 2025-09-22 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bf2fc5e-cc7b-3f70-8dd1-d01cf2188c9c | -11.78918 | -64.92765 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5587ea1f-ef14-3a1c-9cc2-5d17df736ee0 | -9.47057 | -67.10053 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79923a35-3438-33e4-9ac8-6363de6e7dff | -7.56665 | -69.91051 | 2025-09-22 06:20:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fd3484a-95c3-3f50-9c05-1ef16b5de723 | -10.27295 | -68.77679 | 2025-09-22 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a937d690-633f-34b1-b9ac-82b0df2fa9e9 | -9.91973 | -65.04575 | 2025-09-22 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e21982d2-64ab-380c-b545-3f39c1d08230 | -7.31125 | -72.74771 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e49366f5-068f-3c5b-8e3d-0fbafa7cd956 | -10.8576 | -68.56003 | 2025-09-22 06:20:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ae094e3-e6d9-314b-9140-c350a9103e18 | -11.88608 | -64.93513 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e3cf4605-4c09-3b2f-848d-9f40529d4325 | -8.29118 | -71.06691 | 2025-09-22 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 064dcdd2-7e82-3abe-82a1-d97b2d337915 | -9.72084 | -69.08237 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2246975-5e62-3e57-9350-0818e137ff00 | -9.24816 | -67.3917 | 2025-09-22 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5d671a6-ed0d-38f3-b785-dfda7af81886 | -8.52708 | -71.48641 | 2025-09-22 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8d2b72a-9e98-3608-8040-11572d3865a6 | -11.78867 | -64.93208 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 981b73ce-d19b-3895-a9e9-82d31653828d | -10.91949 | -68.59357 | 2025-09-22 06:20:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3e32855-b6f7-3c52-b8dc-dde51a2a354b | -8.72742 | -70.78349 | 2025-09-22 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 970e4823-c7ce-3b5c-9764-eb646730fe05 | -9.46512 | -67.10271 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccd7f415-d01d-3f54-b1b7-61b63e6d87bb | -10.16163 | -68.70107 | 2025-09-22 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb9a5813-d25a-35b7-82e0-7a2e925743b1 | -9.11485 | -65.5116 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d79c8aa-8199-37f2-a1e2-88ab116f7b3f | -11.86801 | -64.9329 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f36f9cdd-e8c2-3848-b7bb-ed6c24c31fd2 | -9.47096 | -67.09763 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d418f08-5f6e-3d45-bc33-e16b5519c47b | -11.8806 | -64.92986 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2f32a301-fc19-33bd-9b02-5cd7172dc672 | -10.27451 | -69.49092 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afa6b977-8156-3ab4-887a-dabba4be7256 | -10.16289 | -68.69161 | 2025-09-22 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d04519cc-1dd6-3405-80bf-4398a75a2094 | -9.46552 | -67.09979 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23b86a08-04bd-38dc-b954-01fc38833d17 | -7.60197 | -69.8961 | 2025-09-22 06:20:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 095b36a1-ad35-3389-9ba7-7d7e0e14da4c | -11.86746 | -64.93742 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 958d9dc9-3551-38e0-8344-06109e92fbee | -11.8609 | -64.9412 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4d099f0-d564-3fc4-b123-4c419c196c72 | -10.90779 | -68.43546 | 2025-09-22 06:20:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9a20729-38c9-39b3-8404-aeefc3405d24 | -10.19964 | -69.09308 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dff7178-a62b-33e3-b0f0-d7139481d06c | -9.02744 | -68.52148 | 2025-09-22 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e6cce25-1850-39c9-8c6a-f2d50c20f5cd | -10.27547 | -68.75805 | 2025-09-22 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8b72bb0-9e57-30b7-abf5-9b81b3588a8b | -10.92288 | -68.59164 | 2025-09-22 06:20:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2809c62b-303b-39b7-85ac-58bb1a10c068 | -11.87349 | -64.93816 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca025ed6-de4c-3423-98fc-0fa03e3f5254 | -6.63188 | -62.93063 | 2025-09-22 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8cffe5df-58f6-31de-81be-a11f7a7ded8d | -9.71642 | -69.08172 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 006dfd9b-e7e9-39b5-ae9b-220c3d009ed1 | -9.60923 | -67.54694 | 2025-09-22 06:20:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45869f4f-8d20-34a6-9c8c-a95f4d112fa3 | -11.87294 | -64.94269 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e56a939-959e-39db-ae8c-8da57cb7ef96 | -10.85359 | -68.55451 | 2025-09-22 06:20:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e8c13ff-60e0-3963-89a6-99229e4cb52f | -6.63116 | -62.93581 | 2025-09-22 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27d1ed09-25cf-3b2f-9e3b-241547d531d4 | -7.65863 | -61.12843 | 2025-09-22 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 729e4c7b-236d-3a0a-b802-c698901ef3b1 | -7.66581 | -61.12946 | 2025-09-22 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a79a8b33-b8e4-3018-935a-9af854b8b3d3 | -9.10175 | -64.0076 | 2025-09-22 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1017a28b-8c61-3751-93f6-c42beda37b50 | -7.59418 | -69.89252 | 2025-09-22 06:20:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c27feb49-6bec-3966-a5f2-4d99dfe6d5fc | -11.87896 | -64.94344 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 89748bca-50f3-3b52-b4ac-e25320444509 | -8.98262 | -65.45959 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cbc848b8-4b93-3a76-bb58-c47566350eb1 | -10.63542 | -69.03839 | 2025-09-22 06:20:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01d7a80a-ffd5-3024-a24c-fd0d6111a674 | -7.24233 | -72.50913 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1f162a6-db40-3581-9b60-9f91c5be89a9 | -11.86692 | -64.94194 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e181334-f77e-3bb1-ab7c-e48ffaf9dcc2 | -10.85293 | -68.55943 | 2025-09-22 06:20:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81575bb4-d27b-38f8-928c-02e203e9037a | -6.62708 | -62.93129 | 2025-09-22 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fbc163d6-7024-355b-ba58-59292c788453 | -10.62469 | -69.18784 | 2025-09-22 06:20:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cf1dbdc-9016-3eb5-ac8a-a55acbdd5a99 | -9.46473 | -67.10566 | 2025-09-22 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0655a1c4-d6a0-3e2a-bc58-c3d655ad722e | -9.19157 | -71.83583 | 2025-09-22 06:20:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46b77cbf-9c48-3215-92e4-7d4dfe69ead9 | -7.60177 | -69.8973 | 2025-09-22 06:20:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dfb1563-6e8c-38cf-a3c8-85aad532a52d | -6.59288 | -62.93069 | 2025-09-22 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README43.md)
