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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d4c52a1-0f4b-3bec-b245-587751e3900f | -4.69245 | -45.62286 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e1fd655-a099-3471-9ea3-b521599194b8 | -4.59529 | -45.60713 | 2024-10-28 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f51bb13c-b267-3669-8456-ac01b8546d4c | -4.59411 | -45.6099 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6544e903-0721-347b-828a-977671fdd8fd | -4.59139 | -45.60656 | 2024-10-28 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b974fc91-9d0b-3395-a1b9-3a19e002f2c7 | -4.56694 | -45.80536 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d22dbe56-6e36-3852-b8e4-5d529313fdbf | -4.56596 | -45.80702 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a28f0770-98f5-3803-a9c6-bcbe76cff97b | -4.56303 | -45.80456 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 26dd1493-91c7-3400-9b28-3449eddb48ba | -4.56288 | -45.80127 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 92f48d8f-4b25-3f0d-aa7a-43a9fba6a12b | -4.56205 | -45.80623 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95132f30-be26-379b-9651-6f9745d8322b | -4.5599 | -45.79886 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5cb725e-1da5-335c-ab01-2765bfcdcff4 | -4.55911 | -45.80381 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c24801f3-bdc8-3166-a3a8-5ae44107697f | -4.55896 | -45.80052 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 090c4226-0b0f-3875-8e4b-ca3af1bfe29c | -4.55598 | -45.79808 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b322ee21-0438-3116-a843-3dac682cf5eb | -4.55518 | -45.80305 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 736fb901-3d8a-32e4-85e9-196dc57fb9b5 | -4.55504 | -45.79976 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 71a76dd5-026b-31bb-b1e3-9ca43e1d436b | -4.55205 | -45.79738 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2774f31a-7d03-3d35-bae4-44b789369165 | -4.54732 | -45.80166 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 024d491b-b84f-3445-8f85-1115ff63e8b5 | -4.47917 | -45.67509 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f28f74a1-7135-355e-b8fa-258329ec1c36 | -4.47901 | -45.67755 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 833bc97e-3a9f-3d98-89ed-c1300b11f013 | -4.47838 | -45.68009 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51a3acf8-4b02-34bf-bd30-74d33ab0036d | -4.47527 | -45.67442 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bd38e0b-8c97-33ac-98b2-ebb73ab49f72 | -4.4751 | -45.6769 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2071115-0526-3872-8a16-5397d649c7ea | -4.47446 | -45.67945 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af28a241-2b69-3317-9dcc-567f9c9c48be | -4.44067 | -46.05542 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7afdf1de-4788-3a67-b10f-18c5ede2e60f | -4.42492 | -45.96419 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4c71912-8927-3bc1-a86e-958507320040 | -4.42437 | -45.96761 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5fd8006-76b5-3b6e-8bbe-b0a0b497432b | -4.41905 | -45.64987 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ad1180f0-fae0-38c3-bb5c-8e6dd11b2b06 | -4.41514 | -45.64928 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b1df8f17-e844-315a-a0a5-30facc14cf7d | -4.41431 | -45.6543 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ffb47d0-70f8-3c9a-8ead-76452899110e | -4.39928 | -46.12431 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 544361f2-1562-3c77-85fa-4329cad3ff57 | -4.38871 | -45.34006 | 2024-10-28 04:06:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 16250169-df6e-39be-add1-5c5597afb21a | -4.38795 | -45.34477 | 2024-10-28 04:06:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e16a018a-b59a-3a29-a52a-816d07a62530 | -4.38487 | -45.33946 | 2024-10-28 04:06:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0a04298e-f814-3ff2-a644-39e51e630ef8 | -4.38411 | -45.3442 | 2024-10-28 04:06:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65b8c65a-1bf2-3e59-bab2-3a66f84e2281 | -4.364 | -45.83741 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 875f9e13-1c5c-3901-85a7-5efe1ee19991 | -4.36316 | -45.84249 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cd41023-06ed-38ab-b835-3ee12aeee4c5 | -4.36007 | -45.83658 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2af59fd2-ef23-328a-9090-3e5a613de54d | -4.32538 | -45.78255 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8c7dc536-e546-3744-82ca-7600f05580fd | -4.32455 | -45.78769 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1bbc7ce6-7170-38e6-afe9-1580607f4da6 | -4.32143 | -45.78195 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9e1cd5aa-8ec8-34b1-a822-99d391add880 | -4.32061 | -45.78703 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c81ae709-b72c-3bd4-93f6-0eb7c68ed779 | -4.31545 | -45.86943 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8c1695b0-a663-3b17-939f-1607e63d58c3 | -4.28531 | -45.53595 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 083962cf-b645-30d9-9ed2-cfb39384b480 | -4.28484 | -45.53338 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08c502a5-29a1-307e-9c5e-7c12b0d16e3d | -4.2845 | -45.54081 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b781214a-6772-3507-8e33-164aae727434 | -4.28407 | -45.53823 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc84998b-8321-3c14-8e06-faef245516f1 | -4.28142 | -45.53534 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27749cb0-23e5-330a-833b-202d80a1d1a8 | -4.28095 | -45.53275 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5c29eda-8e67-3afc-885c-938a59ebe92a | -4.28061 | -45.5402 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1984b55d-d007-3780-ba1c-897552395a16 | -4.28017 | -45.53762 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95f8ba72-6cc6-3ddd-843f-414a211e8f3f | -4.2794 | -45.54249 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 894f140e-6aca-3a11-ba88-5fd813635ffa | -4.27753 | -45.53472 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93114890-ba49-32ee-b23b-513baee0c966 | -4.27706 | -45.53213 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3c5b08d-de28-3c25-b430-292d2193f3b8 | -4.27672 | -45.5396 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67c50a46-ba79-39ad-ac5c-bb6b99fbe370 | -4.27628 | -45.53701 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 959e66c8-93bf-3094-803e-5d6d0842d6dd | -4.2755 | -45.54188 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40d6d635-45fc-3e02-9bec-ee26306d0c6f | -4.27364 | -45.5341 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1bcecff-e64b-3fc6-9043-0794b5ddc906 | -4.27317 | -45.53151 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccc3dfaf-de2a-3fd8-9a1b-32f1077c3e26 | -4.27283 | -45.53898 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cfaaf1c-f2fb-3c70-83df-744d206ddb6f | -4.27239 | -45.5364 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dad1a1f1-c82b-3511-a52b-19acd53af931 | -4.17813 | -46.0741 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6479c33c-6087-3d45-b293-d411647531e1 | -6.17519 | -45.44334 | 2024-10-28 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8ed1f6c-7c87-375a-a3a1-8e4252014978 | -5.97803 | -45.36797 | 2024-10-28 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6288a91-3c52-3143-83d9-9609daab287d | -5.97728 | -45.37253 | 2024-10-28 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23ab66ae-2b47-354c-b71f-f34805ea0c13 | -5.97427 | -45.3674 | 2024-10-28 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 20fe08c2-5854-335e-b351-762f20bfb2ac | -5.44816 | -45.89643 | 2024-10-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 372a5178-5b75-3bfb-8d4d-a5aaa2391523 | -5.4451 | -45.8907 | 2024-10-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb1cb720-3aa8-3676-a40d-9c1b55a8c765 | -5.44427 | -45.89568 | 2024-10-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f914ed15-1d99-3609-95cd-a4f7c136bc13 | -5.44119 | -45.89009 | 2024-10-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1f958c8-e9a7-36fd-8dd8-05cbf7ccf8d9 | -5.28954 | -45.14048 | 2024-10-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eee9496d-82de-3eb5-880e-dcd56b505258 | -5.28882 | -45.14497 | 2024-10-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f3c36fc-ffb9-3682-92ce-43758cc3915d | -5.2858 | -45.13985 | 2024-10-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fde5526-66cf-3641-8fd4-cb1979de30e8 | -5.28361 | -45.72286 | 2024-10-28 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cba0c150-2de5-3adb-8aba-46b46af44f3c | -5.24262 | -45.40593 | 2024-10-28 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a23a6eb-cd56-3d66-8442-40aaad146316 | -5.24187 | -45.41053 | 2024-10-28 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cea632a8-040c-3cd9-93ea-617a7b5ac5fd | -5.23881 | -45.40533 | 2024-10-28 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a532a01f-020a-30a1-baac-dc1b32183a9b | -5.23806 | -45.40991 | 2024-10-28 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76c015cc-97d2-3cbd-b5b6-c8bf718fe4fb | -5.235 | -45.40474 | 2024-10-28 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abb293cc-a425-359c-a8db-d6df4f309532 | -5.22649 | -46.1453 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f4784ea-6135-30bd-ae6c-0af9dd10001c | -5.22303 | -46.14146 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcaa2498-9616-3014-96b5-e90b213d4300 | -5.22248 | -46.1448 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12df67b2-0dbd-33e5-a197-8002a72c3f40 | -5.21532 | -45.7976 | 2024-10-28 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6717b86b-c06f-3324-9ec6-775558bbd164 | -5.21512 | -45.79645 | 2024-10-28 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc9a0af1-74a4-3143-b905-c94bf5d7ff62 | -5.21451 | -45.80243 | 2024-10-28 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4888f94-c23c-31e4-86b3-84f9939062e9 | -5.21434 | -45.80128 | 2024-10-28 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b792fecc-e26d-3e0f-a8bf-7c901e2ae9a4 | -5.2075 | -45.79644 | 2024-10-28 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 977c2117-a52d-3c73-afdc-cfade7b0bbfa | -5.11624 | -46.03221 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6afd12d4-2d31-3a19-9bbc-e270a0285a05 | -5.11172 | -46.08441 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 792c2546-cc08-31f0-940c-61d3afee7843 | -5.11102 | -46.08867 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b983a1b4-b24f-32ab-aaff-82aa40bec547 | -5.0565 | -45.80827 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80c82361-6e14-30cd-9e25-dacea1bd28d7 | -5.85055 | -46.23562 | 2024-10-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57d0f042-0e64-3c0e-9c90-fa09f53fdafc | -5.5789 | -46.34121 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34e6a153-646e-3c20-b94d-67dd91aec5cb | -5.57829 | -46.34485 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cf0668d-5dfa-3736-be81-fbe2089bc920 | -5.40949 | -46.35262 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23f54539-4a73-393b-80fa-658e7a0da25d | -5.40607 | -46.34826 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa3b5f24-49b2-3141-a14d-b25bfd01071a | -5.40548 | -46.35188 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a72f2898-7be2-33cf-b086-558285e4ecaa | -5.29711 | -46.32644 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a19e3093-aa39-3b76-bb19-8025df45af02 | -5.29653 | -46.32997 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e8b3705-3521-338a-8996-23c32773db52 | -5.2925 | -46.32933 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0278bafa-835f-3119-8e04-79d4669e09e7 | -5.28904 | -46.32522 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README41.md)
