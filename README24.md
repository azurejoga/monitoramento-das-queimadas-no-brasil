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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7018dbf2-43aa-3026-8207-bc29b19f731b | -19.27489 | -44.97386 | 2026-08-17 04:23:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2481acd9-1b92-3568-90ef-d3f7a73e7f24 | -18.44474 | -49.73183 | 2026-08-17 04:23:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d62d370e-4a69-304c-a83b-c77d00e9f8b4 | -15.9437 | -47.84043 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 969bd043-bead-3304-b448-6f7e3418d216 | -14.4993 | -59.32007 | 2026-08-17 04:23:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cc120b4-8ebd-3d55-9660-1cb4e21af7fc | -16.41088 | -49.63408 | 2026-08-17 04:23:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1bf1d4e-ed7d-349b-bbbe-a465b49e614c | -16.22334 | -49.71021 | 2026-08-17 04:23:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd4bb1f7-2c31-390c-8994-2f977d9c2e04 | -16.81545 | -49.06691 | 2026-08-17 04:23:00 | NOAA-21 | CALDAZINHA | GOIÁS | Brasil | 5204557 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 106b04aa-73aa-34e4-ac4a-0711ea522307 | -18.18324 | -42.3377 | 2026-08-17 04:23:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| febf71d0-b924-3e82-b9bf-419b86a48d7e | -18.18278 | -42.34129 | 2026-08-17 04:23:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| f2ce0938-0341-3c92-9b4b-2d07b55fcec7 | -17.35495 | -45.61969 | 2026-08-17 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de83bc55-91ea-3b18-9414-2e7255ba7e1e | -15.84861 | -50.10387 | 2026-08-17 04:23:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afc02e9f-a26a-3231-8f5b-4318823befe7 | -15.83 | -54.21387 | 2026-08-17 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bf3dbd2-82bd-30fd-96e6-44b20dfd9d7b | -15.78496 | -55.57189 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36920fd0-87ff-3b80-9a57-45e7e7b8fc2d | -15.94862 | -47.85244 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63d396a6-e671-3b6d-ae01-488dfb0093aa | -16.75341 | -49.37415 | 2026-08-17 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1271bbcc-24ff-3dfd-b017-bd3ed19809cf | -18.80712 | -46.73857 | 2026-08-17 04:23:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7f09bd5-81e6-33bb-af6d-8abbf23281b3 | -21.16723 | -47.7235 | 2026-08-17 04:23:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1619e424-2d32-3b6d-935f-f4082f2e8aa9 | -18.46323 | -49.72717 | 2026-08-17 04:23:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 09333b60-043f-3636-84ac-55752f79cff9 | -16.7171 | -49.12914 | 2026-08-17 04:23:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0e469d6-b2ab-3f08-b1f7-05ac55291bc5 | -20.2754 | -47.2007 | 2026-08-17 04:23:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a72d23e4-6cf3-3de9-8698-b5e1bd66740d | -20.30033 | -47.21663 | 2026-08-17 04:23:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e5d93c3-ddb8-32c2-be20-082deab45cf8 | -15.78421 | -55.57565 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7e31b81-2824-3400-bcec-8a333d36be53 | -16.20662 | -57.63699 | 2026-08-17 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1132d972-3e43-3796-8f91-d59f78c6ea43 | -16.22684 | -49.7109 | 2026-08-17 04:23:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a582883e-11c2-3a33-8f20-ca57fb2d4b30 | -16.21623 | -57.64756 | 2026-08-17 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ff6b875a-9a3c-3279-b480-c6e9400236ab | -15.90004 | -55.54008 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 30ccf5fd-4a4d-3b50-b56d-f5e698041feb | -23.49336 | -46.76108 | 2026-08-17 04:25:00 | NOAA-21 | OSASCO | SÃO PAULO | Brasil | 3534401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a48460c2-5069-341f-8884-a1a8fa4b4b06 | -23.46601 | -46.48726 | 2026-08-17 04:25:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c3331e07-5e8c-3c64-9b94-0b7abdf2d8e0 | -22.49845 | -47.40108 | 2026-08-17 04:25:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 87ffa6e7-bb78-3327-8599-ee1053e6cf06 | -23.88917 | -49.23495 | 2026-08-17 04:25:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7081cfc2-bc95-392f-966e-76eeadaa204b | -22.89856 | -43.65575 | 2026-08-17 04:25:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 37abccc8-28d7-305e-b0ff-38c11db7482c | -22.28197 | -48.64492 | 2026-08-17 04:25:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0953a334-2cc3-3214-ae3e-a7eea53e32e7 | -22.38579 | -47.25325 | 2026-08-17 04:25:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 04f3f439-e60c-3e5c-be3c-7511e7ba4d28 | -22.27866 | -48.64433 | 2026-08-17 04:25:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 865a1ac6-6f22-3cff-bf88-181c7ab1b77c | -28.6527 | -49.46191 | 2026-08-17 04:25:00 | NOAA-21 | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 75a4f379-ca6c-3ba0-b3ef-2d9417e9e6f9 | -22.38186 | -47.2565 | 2026-08-17 04:25:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0874bc36-83fb-33e3-812d-b11bd0940d85 | -22.38522 | -47.25708 | 2026-08-17 04:25:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d6409e8e-f2de-387c-8180-2d51303b4c2e | -22.49636 | -47.40105 | 2026-08-17 04:25:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5114b142-047c-342c-80e4-b59d7332fcaf | -22.6152 | -46.29976 | 2026-08-17 04:25:00 | NOAA-21 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ef0e323-126d-3379-a1e1-da2d184cb04a | -22.89573 | -43.65423 | 2026-08-17 04:25:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 715e877c-943a-3e33-8023-2dc11aee6984 | -6.6384 | -58.9636 | 2026-08-17 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 8bc76ff5-d745-396f-8af1-493371b5a16d | -15.9189 | -55.531 | 2026-08-17 04:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 245aa661-8404-31ce-a4c2-0df3209b39a0 | -6.6199 | -58.9643 | 2026-08-17 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 71ed477c-bebe-3efe-b282-bcea65553ff9 | -6.6568 | -58.9628 | 2026-08-17 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 37f0b313-2e58-34b5-a047-35a63c1c2484 | -6.7123 | -58.9412 | 2026-08-17 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 63e84cb7-37ba-3ddd-98e7-e47f98cdc94a | -15.8994 | -55.5334 | 2026-08-17 04:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| fd7a3871-8daa-3dd4-b6cf-0e98146a9cee | -6.1106 | -57.7425 | 2026-08-17 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3c5348c8-157c-33fc-8453-add2177baa02 | -6.6199 | -58.9643 | 2026-08-17 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 24aa69e6-3767-3b2b-af5f-603938dcba68 | -15.8994 | -55.5334 | 2026-08-17 04:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| d9984569-fb43-3ae2-9942-57fe79eda64d | -15.9189 | -55.531 | 2026-08-17 04:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 559455fc-2bb6-349c-b286-f60c0fa15f16 | -6.6384 | -58.9636 | 2026-08-17 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| c69a2ea6-964c-3c97-8a90-267efee0f009 | -6.1106 | -57.7425 | 2026-08-17 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 6d9896a7-a5be-30da-958c-fa39b92480dc | -6.6568 | -58.9628 | 2026-08-17 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0df252e2-214e-33aa-8f08-2e5c512be43a | -6.6199 | -58.9643 | 2026-08-17 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9a77ce2c-3cb9-3c21-9463-b1c16af81d2a | -15.8994 | -55.5334 | 2026-08-17 04:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 3815f5ff-5efe-3a32-8ae9-ca2cec3b183a | -14.1031 | -58.4423 | 2026-08-17 04:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| ae78364a-b88e-3013-96f9-3859e25dcbd7 | -6.6384 | -58.9636 | 2026-08-17 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| eeb37c1e-1290-3518-8eb1-e34534dcd5b7 | -6.6568 | -58.9628 | 2026-08-17 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| dc77ef06-ad04-39ef-9bec-22a43a8ace86 | -15.8997 | -55.5127 | 2026-08-17 04:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 84eecc2f-56f5-3bb9-bfa5-d75ea715baa5 | -15.9189 | -55.531 | 2026-08-17 04:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 019b0af5-8b01-3ee9-9495-239505cd4d27 | 2.12542 | -50.96162 | 2026-08-17 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47c485df-8f0c-3c20-8fec-06256f5b3712 | 2.126 | -50.96527 | 2026-08-17 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 476d5c7c-4350-3349-9ae9-1b854209055e | -7.1805 | -43.72722 | 2026-08-17 04:55:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 988cb2ac-f069-3a31-8d3b-966164917c62 | -7.59414 | -45.02783 | 2026-08-17 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0908973-9652-3360-891e-cf57deefdf41 | -6.13484 | -57.73337 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6dba8225-9190-3e8e-a762-9a242d82a305 | -6.5313 | -43.11671 | 2026-08-17 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fe20ee7b-cee0-346e-b0d6-4d0633c93660 | -7.17567 | -43.72651 | 2026-08-17 04:55:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a1ae376-4bcd-3e54-8a1c-7404791ba838 | -6.77936 | -51.06035 | 2026-08-17 04:55:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faf33216-ca1d-38ef-8e40-7a0c8711a651 | -6.38364 | -51.7406 | 2026-08-17 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0306fdd7-f28a-309e-a5f9-7ef1612f432e | -6.93701 | -45.44419 | 2026-08-17 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02fde751-db93-3923-997d-9e2773405e59 | -2.80492 | -48.59269 | 2026-08-17 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17843465-d42b-3722-b956-c022c0480ae3 | -6.02764 | -57.81005 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 050b62eb-ea21-3f17-bd13-9baa9036d510 | -6.52672 | -43.11551 | 2026-08-17 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe78a78a-0d35-37f9-941a-f5d903ac4420 | -1.84063 | -54.48675 | 2026-08-17 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60cc822b-08fb-3526-aaaa-106c6795e730 | -6.21777 | -47.72419 | 2026-08-17 04:55:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4474490d-302e-3307-884f-02b572bf9a96 | -3.26198 | -49.52378 | 2026-08-17 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f87cd040-a1f2-3517-9b5d-a1f257ad749f | -6.10264 | -57.73223 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 37b02106-77b8-3c94-a4f0-8a215061b2da | -4.35618 | -46.1637 | 2026-08-17 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1a028cc-a063-3d7c-abb9-8d364d9d9bf1 | -3.8028 | -59.33403 | 2026-08-17 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a008348e-de4e-30f6-a8e5-3ba9e4d1abcb | -6.11621 | -57.7071 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2455a8b-51a0-31c2-8e4b-00518fd7d39b | -6.73132 | -44.67477 | 2026-08-17 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12c1cd0e-b1e8-38cb-8dda-54c5fb4c6978 | -7.57745 | -48.43771 | 2026-08-17 04:55:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcc9a3ee-571f-364d-85b7-425ad209619f | -3.06775 | -49.36074 | 2026-08-17 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ca6f5d2-1919-3c6c-82e8-dec1bcb24f17 | -7.23977 | -49.88276 | 2026-08-17 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a59099a1-89b6-3d02-9aed-70c71c23ee1a | -7.82441 | -44.09991 | 2026-08-17 04:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cd642d9-0378-3a4c-b72a-26caa6afc804 | -4.96718 | -50.89698 | 2026-08-17 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d75884b1-fcff-3469-afee-8a5c21a23d19 | -6.10188 | -57.73665 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| eeb41d39-9494-370b-8f2c-269eabda6633 | -6.11009 | -57.74277 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11e2486b-c1c9-37b2-8229-7af36871f6b6 | -6.12212 | -57.72656 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3e5d4f2-bb39-377b-a24f-b806f09ac515 | -2.6653 | -48.52692 | 2026-08-17 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0890f229-cdb3-30a5-abed-2be906c59c5e | -7.36367 | -46.84952 | 2026-08-17 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c77b434e-47d2-314d-b8eb-e97de117d2c3 | -2.77016 | -48.56895 | 2026-08-17 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b75a594-a514-3d47-b3ca-2c4b8ca773e2 | -3.2572 | -52.92031 | 2026-08-17 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aa3fbf5-379e-31b2-91ac-4221d8100e09 | -2.80833 | -48.59322 | 2026-08-17 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8a79d718-d0d3-35b6-bbff-779268c6d41d | -2.63284 | -50.86788 | 2026-08-17 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6e6ef12-da99-3a85-a3ac-54e4d3ab0e30 | -3.24395 | -51.55928 | 2026-08-17 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebc5e464-821a-39a8-a7b9-9a152a1f2743 | -3.79758 | -59.33316 | 2026-08-17 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d4e6f98-e88f-30b4-b190-5b824ce4f307 | -3.4627 | -56.80519 | 2026-08-17 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b03fe5f1-322e-3ca5-b0b8-733dd5812459 | -7.59923 | -45.02391 | 2026-08-17 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 79ba11f1-82d8-309b-88d7-126ebc46f50b | -4.1236 | -56.33371 | 2026-08-17 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
