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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d19079d-461c-3ae3-845b-4db6b2aa1c0c | -13.10323 | -46.87991 | 2025-07-08 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 999cac9b-939e-3eb2-8483-8378f034c6ac | -17.21545 | -44.79786 | 2025-07-08 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b50aa662-fa7c-3090-b96b-62b29aec60c2 | -13.40541 | -47.882 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36ac81c7-90c3-3f09-a2aa-7e4fcbfce288 | -11.41759 | -45.1074 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 531d58b7-7c64-3020-a747-bf78ea0824d3 | -11.84687 | -43.79811 | 2025-07-08 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f65ceec5-8a6d-3850-86b0-2a0596608c46 | -11.90036 | -44.91593 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a25d2d54-0fcd-3a4d-9cb1-7da5b40d40ed | -12.98708 | -44.88444 | 2025-07-08 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7031d370-c2ce-3708-9b49-98b473ec0236 | -23.76123 | -45.72961 | 2025-07-08 04:17:00 | NOAA-21 | SÃO SEBASTIÃO | SÃO PAULO | Brasil | 3550704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d4f4e969-5cee-35dc-b1ee-73bceb5fe67a | -10.57745 | -49.12564 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| b4fc5171-8749-3e3b-92b4-4d88b9574af9 | -10.82469 | -54.01449 | 2025-07-08 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd870357-fb77-392c-8467-f0804cdf09db | -12.98764 | -44.88092 | 2025-07-08 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58ef6de4-fa4a-3b6f-a764-88a9d18ad711 | -16.06826 | -53.75092 | 2025-07-08 04:17:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 320f763d-f071-3c11-a49f-44809e6d0689 | -11.43529 | -45.10303 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 966c57fc-88b5-36fe-983a-680395d674a0 | -13.02772 | -46.29009 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b309f4d-df96-3bc1-b42f-0795000751d8 | -11.88822 | -44.92838 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8d250d1-8ef2-327a-b841-a732fddf331a | -23.59543 | -47.43807 | 2025-07-08 04:17:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c5d951e0-7d2b-3a8d-8663-137043c42260 | -17.0609 | -48.6606 | 2025-07-08 04:17:00 | NOAA-21 | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4843abba-1aa3-3ecf-a197-be49b1c07e3f | -10.82948 | -54.01909 | 2025-07-08 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce108ad8-ac43-3ff2-8413-0b4fff46fb61 | -13.40472 | -47.88602 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb1a3fc3-d796-3652-a693-846b8294d3fa | -18.65438 | -55.73834 | 2025-07-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 319100b2-dba0-32bd-a201-2748cf5474ab | -20.77429 | -49.86162 | 2025-07-08 04:17:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a298b555-fc86-3613-b1d9-7a7c31a6c8ad | -13.41681 | -47.87965 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eab336ff-061b-3b2c-a2cb-ab48590c8ea4 | -14.92663 | -46.9274 | 2025-07-08 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7831b3d2-feb8-3781-b8e0-bbd6403cf470 | -11.89042 | -44.93592 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fd53e21-e846-3d56-becc-baab71e84b90 | -11.43198 | -45.10249 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 39968f12-c714-35ff-936c-b496b0f215ed | -14.37287 | -46.83321 | 2025-07-08 04:17:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2ff6f27-71f4-327b-895f-340ba6d79dc9 | -21.79584 | -52.7653 | 2025-07-08 04:17:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 23827608-9e73-344a-a615-d7476aacee94 | -10.83354 | -54.02755 | 2025-07-08 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f2cf484-a8ad-3265-ad6d-1e8d0722bf9f | -20.77787 | -49.86231 | 2025-07-08 04:17:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 006de139-8699-3b11-a3b7-f919a7a51e8c | -11.89097 | -44.93242 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ba69b6f-150e-3ea3-96c9-a70b860c509c | -12.58091 | -56.98199 | 2025-07-08 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5be5fbf-8c03-3f96-a52e-c71251d24545 | -10.63902 | -49.46659 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48ceef4e-408b-3622-b094-31045b80db70 | -18.65343 | -55.71648 | 2025-07-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7f54bc74-65e7-36f1-a9ee-a8b341e90da9 | -11.81106 | -44.27185 | 2025-07-08 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2637878c-640e-37fe-ae7d-e2cf7d6d51ce | -15.25082 | -51.53233 | 2025-07-08 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78b8a31e-cd1d-3d9d-acc7-7ce0775272cb | -13.03509 | -46.2874 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dc35044-5535-300e-a3ac-fd1ef5c50f44 | -22.54052 | -48.8149 | 2025-07-08 04:17:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90e850d4-eba8-3d1a-81f8-cee433292721 | -15.34995 | -47.59998 | 2025-07-08 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4f7395a-e7df-33c7-8ecb-f50e8569290d | -21.72732 | -46.3765 | 2025-07-08 04:17:00 | NOAA-21 | BANDEIRA DO SUL | MINAS GERAIS | Brasil | 3105301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7b6749e7-c6d6-38f4-9b46-5b2e749677ec | -10.64095 | -49.45563 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd1474b6-01ac-3684-913c-113ef6b4284a | -11.42479 | -45.10494 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 2c527b43-554a-385c-b573-52269b93c289 | -12.07228 | -43.50213 | 2025-07-08 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 948d4fbe-f679-30f3-898e-536702c37c37 | -11.43637 | -45.1177 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f3b4aee1-2845-3ab6-ad1e-cd806daef00c | -12.29311 | -50.11076 | 2025-07-08 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 994038ec-8526-33e6-8eba-450ea012c4c5 | -10.62877 | -49.45362 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 0cdd1449-5eb1-33fd-ac75-861a1ff69ff5 | -10.64244 | -49.47097 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02423b19-ed71-3ace-a1a1-a2a495e8e797 | -11.31095 | -42.13095 | 2025-07-08 04:17:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 89ae4840-9bb8-36ba-9892-6d138a990741 | -10.64778 | -49.46436 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fb174a29-3e7e-3c2a-a9ef-5dd62e689c54 | -21.72789 | -46.3728 | 2025-07-08 04:17:00 | NOAA-21 | BANDEIRA DO SUL | MINAS GERAIS | Brasil | 3105301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2f0f19e8-7b5b-3e64-b933-76ccdab94405 | -12.33486 | -49.3227 | 2025-07-08 04:17:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b3c077f-b1e9-35ac-a1a7-d9d078409fa2 | -17.65595 | -46.82958 | 2025-07-08 04:17:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2a10c6d4-efb4-3fa0-beb6-539dd16e1eac | -13.4139 | -47.87518 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db91163c-fb78-38df-b718-f6c854779a76 | -16.60269 | -44.51577 | 2025-07-08 04:17:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b3176ac-eb5d-3d0d-b00c-8bf75e6498ce | -11.84023 | -43.79705 | 2025-07-08 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d2c99b4-1290-3a6e-9089-101795eeaebf | -13.40757 | -47.89084 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e3232fc-dba6-3e95-8896-ee5dc2a9f694 | -10.41973 | -49.76697 | 2025-07-08 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf7143fe-31b8-3367-8e16-fe8c4a35da76 | -10.34536 | -49.92158 | 2025-07-08 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71d49400-1f4c-365d-b70b-63176bb070a9 | -13.03786 | -46.29168 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5147643-6a07-32f3-a7d6-7983b764f8f2 | -14.18794 | -45.51075 | 2025-07-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f9b7c4c-a76a-3276-95d0-68cfe18d9ad4 | -10.82491 | -49.55293 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3ef92ee-3c96-38c7-87a9-758305f4f02f | -14.0526 | -46.25095 | 2025-07-08 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d523c0b-63bc-3efb-90cb-f8600cb0559f | -10.64372 | -49.46364 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a06c4c39-a88c-35d3-8864-2815c2ae68c7 | -21.09586 | -47.97715 | 2025-07-08 04:17:00 | NOAA-21 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29baff62-d84c-34ba-a580-63699fcd17fa | -12.01678 | -47.77835 | 2025-07-08 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9caae95-7d0b-30e2-8abd-4f6431930874 | -18.64386 | -55.73592 | 2025-07-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5473b344-9d19-3d71-85c8-929b7f52af93 | -11.20039 | -49.00172 | 2025-07-08 04:17:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a2716ce-cc3f-3adf-9466-03e0713b01c7 | -18.14744 | -47.8002 | 2025-07-08 04:19:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 020f90e2-fb31-323e-9a20-5c963d5b1dac | -19.59477 | -47.6162 | 2025-07-08 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47d2ad0c-3889-3a70-8d1b-77fbfcbe6070 | -25.54139 | -48.57266 | 2025-07-08 04:19:00 | NOAA-21 | PARANAGUÁ | PARANÁ | Brasil | 4118204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 46df2633-cba8-37c3-8694-82ac345fb000 | -19.7851 | -47.46944 | 2025-07-08 04:19:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 941eaf02-12af-3fb0-b80c-ccf92237a02f | -19.96977 | -44.21633 | 2025-07-08 04:19:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e3506765-c95b-37e0-9071-3524a775c5a4 | -20.41608 | -43.55388 | 2025-07-08 04:19:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 15104e8f-8530-387a-9195-cfda2afb0708 | -19.76411 | -43.64776 | 2025-07-08 04:19:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07ce8675-2f59-3f6b-9799-10c8fde4d1b7 | -18.51952 | -47.15442 | 2025-07-08 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af4f40ef-710b-3106-a341-604fe0a37d16 | -19.89323 | -44.70047 | 2025-07-08 04:19:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 475f718d-777d-32e4-9e7a-b219108129cf | -24.24217 | -50.74022 | 2025-07-08 04:19:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7ed24f08-f82a-334b-846e-23529a0ef444 | -20.00456 | -42.1941 | 2025-07-08 04:19:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3a3f8f5d-270c-3f23-b2c6-cfc38a86b72c | -19.44825 | -48.37165 | 2025-07-08 04:19:00 | NOAA-21 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a42b8929-3826-364b-b102-497188d2fdcb | -28.58517 | -49.44082 | 2025-07-08 04:19:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 73bb9067-4508-33b5-a881-cd275ec4ff4a | -25.45796 | -49.61023 | 2025-07-08 04:19:00 | NOAA-21 | BALSA NOVA | PARANÁ | Brasil | 4102307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4a815a93-21d0-3496-b923-8d52e75dff0e | -19.51362 | -44.27677 | 2025-07-08 04:19:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 606255bd-9a35-3396-9c86-e52a42e35922 | -19.49905 | -44.80589 | 2025-07-08 04:19:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df4aba34-b877-347b-bd19-f31f0b06eba7 | -19.59812 | -47.6168 | 2025-07-08 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c20c3b5a-999f-38b0-9e2f-e475dbec2f54 | -18.3989 | -44.19166 | 2025-07-08 04:19:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 02265342-333d-3e35-8fca-da8356471e44 | -18.51892 | -47.15813 | 2025-07-08 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b92c682e-32ad-3008-bda5-3f021103411d | -18.22652 | -44.20017 | 2025-07-08 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0a284958-4c99-38c0-983b-4d73e61f61c1 | -27.82987 | -50.30307 | 2025-07-08 04:19:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9440b4e-365c-3535-894d-3aa4a3c2b91d | -18.22708 | -44.19632 | 2025-07-08 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea8181f6-05dd-3893-a02b-c92dd7ef7480 | -16.46966 | -54.54635 | 2025-07-08 04:19:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 951572c9-8af1-3406-b315-44137337207f | -24.24441 | -50.73901 | 2025-07-08 04:19:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3c8b76a3-0d7e-3382-b6f3-3cb3923343cf | -18.22992 | -44.20071 | 2025-07-08 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b5531db1-0dfd-3418-a490-23a858cd4145 | -19.59355 | -47.62368 | 2025-07-08 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f17d47f-7e0a-387f-a48d-5214005bf834 | -19.45506 | -45.30586 | 2025-07-08 04:19:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbf9e290-34aa-3292-bc0d-1c4a004db0e9 | -18.40287 | -44.1884 | 2025-07-08 04:19:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaa4291e-514c-3197-b80a-3988e3e909a3 | -19.05655 | -44.36124 | 2025-07-08 04:19:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14dd4f3e-d559-31e2-aacb-8ee28622b84e | -17.91809 | -45.55757 | 2025-07-08 04:19:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 526301a7-de7a-366d-b0b4-a8a31745d31a | -19.73559 | -47.73845 | 2025-07-08 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ee5ec96-4ba3-3288-b469-eadfa27f4cfb | -19.00457 | -48.05933 | 2025-07-08 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85eed6ab-1454-3966-bc26-55604661aaa1 | -19.73913 | -47.44168 | 2025-07-08 04:19:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 304dc02b-184f-354f-afb0-86c59f579583 | -19.51367 | -44.27567 | 2025-07-08 04:19:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README11.md)
