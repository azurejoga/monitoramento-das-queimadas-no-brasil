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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c27575e0-a34d-395f-810a-4a782a11bf49 | -8.65012 | -53.18483 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f6dc3bf-0b67-3d89-afe4-3ed0255a7aa4 | -8.64971 | -53.18796 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0bf5ee3-6c68-3337-9e99-6936a5fe2643 | -8.64931 | -53.19102 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c88e5359-717d-3025-ae55-960c91874e76 | -8.46397 | -53.22581 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4409ef75-5a09-35b7-9d10-4f1c012f08c6 | -8.46353 | -53.22918 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5196c0c0-f0dc-3c84-bf08-b40e3319afc7 | -8.37291 | -52.47477 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bc70f2b-9533-3b05-a301-5f40605cac7b | -8.36733 | -52.47365 | 2024-09-27 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| add41d6f-9c98-341b-bb99-f67c8e0c12a1 | -9.55772 | -53.40384 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee70d2c9-bc65-3284-ade8-ffd54d389813 | -9.55726 | -53.40725 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71df7b3d-de53-31cf-8774-fb414388d955 | -10.04395 | -53.47581 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 09ff6e5e-9931-3099-b461-94471b32dcd8 | -10.0435 | -53.47928 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2d10724e-d7fe-3d32-9af1-9c773ca00603 | -10.04305 | -53.48273 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c00d21ee-7288-3130-8f3e-b9a7858f20ea | -10.04261 | -53.48619 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 252d8fa3-cae2-343d-a313-0a163b6e0259 | -10.04258 | -53.44387 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 048a9afc-aebf-3787-b5ca-19cf44c47407 | -10.04216 | -53.48965 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a02f8ea0-c6d0-36bd-8ea6-16b1689513fb | -10.04213 | -53.44733 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 507ed5dc-30c8-3850-ab08-4e990ee83ea5 | -10.04171 | -53.49313 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 921f635c-c00b-3538-94d9-ba89b17e2075 | -10.04169 | -53.45079 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0e0e60c-2114-3402-ba32-32e25e822b3c | -10.04124 | -53.45425 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d855b989-97c0-3fed-a868-a5cef64998b9 | -10.03856 | -53.47503 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 34d2a5a5-95d1-35c5-96c2-674dc84f33cf | -10.03812 | -53.4785 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 44de25b1-a5a8-3a68-9dd1-e17552c6d920 | -10.03808 | -53.43611 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 211592db-7135-3634-b5ed-28c6da0ca619 | -10.03767 | -53.48199 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 399eee40-8ad6-35ae-831c-81a4939fc435 | -10.03763 | -53.43961 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 86800a08-f7e0-330d-8eb6-f384f5afe9b5 | -10.03722 | -53.48549 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b85fe64-4290-3916-8378-746ad6a5c119 | -10.03718 | -53.44314 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 364ce98d-6e6d-3e06-976f-05aa70f36f95 | -10.03673 | -53.44665 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 26625746-cb3b-3a7f-9661-e3d0ef7ba365 | -10.03631 | -53.49249 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcd1b512-2126-3949-a35e-c28c112410a1 | -10.03628 | -53.45014 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f3534cf-682d-3c41-bc17-8ca7c54f208d | -10.03583 | -53.45363 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 148585f0-908b-33a7-ac63-e4dc886fe87e | -10.03539 | -53.45709 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| efd82ae1-1486-3de4-a771-d7470332939f | -10.0336 | -53.47096 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 585d4823-3b75-3313-9fe3-a31c31cdf2c3 | -10.03316 | -53.47442 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eaac8a7d-4ee1-39b9-b88d-f393cd6e0f71 | -10.03272 | -53.47787 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cbc710de-6adc-351c-93da-3cf831fdaecf | -10.03268 | -53.43533 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5012403b-a305-3e80-bf19-bd572a4b3c67 | -10.03227 | -53.48135 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92f517d5-ea35-3800-b9c4-a0dd976fc273 | -10.03223 | -53.43883 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92b01ed3-62b9-3ff3-a80e-dbc85bb42c7b | -10.03182 | -53.48483 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3777c786-1dc6-37f4-bebc-acd0f6af07cd | -10.03178 | -53.44235 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 66816fa8-7aae-37b0-a0e5-a10b715fd95c | -10.03137 | -53.48832 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c0c467b-3758-373b-895b-86607722caab | -10.03133 | -53.44587 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 8db211b0-f5ad-335e-a19b-797f4036a749 | -10.03088 | -53.44938 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| e298b25a-cc61-32e1-9eb4-8a582af2b863 | -10.03043 | -53.45289 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 421b61d3-f637-328c-bc22-582b458de9cf | -10.02998 | -53.45641 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| efb540b1-541c-3cd2-9a1b-d8845b281b2f | -10.02864 | -53.46693 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 81f4e1ca-6e9a-344e-a606-10aba4c3c584 | -10.02819 | -53.47041 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 3620f00a-2831-3c9e-b8dd-4c0098000270 | -10.02775 | -53.47387 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 4cdae8fc-a5d3-3cad-8a35-b4051e4fad08 | -10.02731 | -53.4773 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 721343da-1cc1-36dd-a41f-23773d33a044 | -10.02642 | -53.4842 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d95510-f7b4-361e-a295-eeb3b3699d48 | -10.02593 | -53.44516 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| ee11c5e8-8080-3d69-be8e-99cdd593e391 | -10.02548 | -53.4487 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 33b2cc6d-06ab-316c-8ef3-d74932dd081b | -10.02503 | -53.45225 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 55645144-de49-36e5-9e1e-fc890978f159 | -10.02457 | -53.4558 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51b6fe92-cc85-3066-ad82-895d254c4de6 | -10.02052 | -53.44448 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5b978bb4-a402-3c3b-99d8-c2ff2f11741b | -10.02007 | -53.44803 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 42de0419-70a6-3c46-9930-5254f774cb9a | -10.01962 | -53.45159 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 15ffc0c3-b0aa-347f-b85d-c7e6f6ce16c7 | -10.01917 | -53.45514 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dd6fe560-4a3d-313a-a419-e71641edf99d | -10.01423 | -53.45082 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0514ec3a-fde7-39f1-8aee-933b3e65eb04 | -10.43419 | -53.67607 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8423037-10cd-3d19-96af-33cde3f6579a | -10.82012 | -53.74078 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3990a2f5-9079-3ba2-80c8-b3e5f766bd4a | -10.8173 | -53.73598 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3330d399-56b6-387e-ada7-6cf962f2d67b | -10.81684 | -53.73948 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2b3d195-9dab-30a4-acd0-cc80c3ddfaa0 | -10.8152 | -53.73656 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e56443e-10b2-3140-81dc-e9683b496d13 | -10.81477 | -53.74004 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 499bf46a-7f12-32aa-8850-9fa8cb4b1222 | -10.77678 | -53.54053 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 358a3cb9-13d7-3d7f-9445-0185085e2cb5 | -10.77137 | -53.53973 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1ea40d3-5a1a-3708-babc-18d209907026 | -12.58398 | -53.16367 | 2024-09-27 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8640afce-4748-3bdc-aaa2-ebe0d3520e55 | -12.53796 | -53.16193 | 2024-09-27 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb062a43-baa3-378f-b245-a0d0455a7f6b | -12.53559 | -53.18166 | 2024-09-27 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc68de74-2785-3866-8048-ef2211394ef7 | -12.53512 | -53.18559 | 2024-09-27 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9a49e2b-5df1-38c3-800b-edbe1b10778b | -12.5318 | -53.16517 | 2024-09-27 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44b8c3ef-829d-3d6e-b70f-b3452ba5feb6 | -12.52991 | -53.18095 | 2024-09-27 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b16148ab-f488-325c-87fa-50b1fdcda685 | -12.52423 | -53.18021 | 2024-09-27 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f91b8f9-317a-3665-9b57-9700aa5b7ea6 | -8.00726 | -53.20102 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b9729bf-5e0e-3add-9597-f7c55f137d15 | -8.00684 | -53.20415 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1c27c7a-e5fa-3940-82d6-5c2f7709b46c | -9.17385 | -54.67311 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8bfb88ef-fc51-35e9-88ae-5c2e3c79367e | -9.17316 | -54.67841 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8746e9c-592b-39ca-9bd5-611599b75c8b | -9.17179 | -54.67086 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff1ee0a2-14ae-3479-aa39-d0415261aa65 | -9.17105 | -54.67618 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14b7550b-e617-3807-af34-c60cbe2938e7 | -9.10165 | -54.67221 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6536a8a-fc84-3881-a7fe-910ce9669102 | -9.09676 | -54.67145 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9cb2428-3440-3dda-83f7-fe2da93a90f6 | -8.54037 | -54.58205 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 201f95ec-e563-3399-bf07-277e190f3f6a | -8.5396 | -54.58752 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5794b16-b46e-3f37-bf3b-495f675c8d33 | -8.53471 | -54.58683 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d70cbea8-60cc-3215-a9fe-c827918ff3ca | -8.53059 | -54.58063 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 039bc4b5-55f6-39ac-8431-8cc6407e4a48 | -8.52983 | -54.58612 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f89d7fc7-0d57-3373-9430-373ed7c5f681 | -8.52757 | -54.60242 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48bff250-4f5f-3777-8f90-0c650808052a | -8.42978 | -54.67709 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f468472-7392-310b-ae35-20611d57fa6f | -8.42902 | -54.68249 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86dc8ec3-c9f3-3967-aee6-0fe4987c922f | -8.42826 | -54.6879 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78085d01-a4fe-3e1d-8e9a-d1cd7d381799 | -8.42741 | -54.68242 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d90995c-cbfc-3be1-a85e-deed5e755a5b | -8.42189 | -54.69803 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63d76021-760d-3884-b831-6c64555ea1d3 | -8.42184 | -54.68709 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fd4c263-7b92-3e6e-83d1-f94bac5ac84e | -8.42042 | -54.70852 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b655d78a-6707-35a3-ad5a-b471c88eb4d1 | -8.4204 | -54.69799 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 398349d1-6a51-3156-b325-edf5410bf1f0 | -8.41969 | -54.71373 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03ebae48-60c9-3d0e-b3b1-1c6b1484dbaf | -8.41901 | -54.70849 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb2c0a6f-aa16-35ea-813b-5f16ce26fc44 | -8.41631 | -54.70262 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c7cfbba-9d66-38ce-b059-2a4ce2cb5278 | -8.92697 | -54.74606 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17f93d09-8de6-38d3-8092-23631b0a700f | -8.92625 | -54.75134 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README115.md)
