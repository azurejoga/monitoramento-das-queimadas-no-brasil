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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c5f4beb-285c-3df0-8dc3-9edcef6bafdc | 1.11276 | -60.51972 | 2025-05-02 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 018a8c69-ea5f-331d-b66e-4ba7884715f3 | 1.10879 | -60.51665 | 2025-05-02 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9200d901-bd09-325f-ad23-fe9f4c4d321b | 1.11449 | -60.53055 | 2025-05-02 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed7c10ca-4c7d-38cb-9d77-c9ca19609ec6 | 1.11219 | -60.51611 | 2025-05-02 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c573d2d5-5c23-3444-8c66-f1fffd889453 | 2.61301 | -60.35744 | 2025-05-02 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dbd1ad8-3256-31fa-b3cb-b5190d0e4e2a | 1.10937 | -60.52026 | 2025-05-02 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10130e03-9857-354d-a477-a130ac0fb6ff | -11.8845 | -58.06247 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1be0e6b-ae95-3cce-bd63-be7ea5a6b02c | -13.04963 | -53.72737 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e246ab0a-b1e7-3cf1-ab7f-f82e702fe66b | -11.39542 | -52.94851 | 2025-05-02 05:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78f20579-6268-38d4-a4c7-56ac8ee0e9e0 | -11.40182 | -52.94921 | 2025-05-02 05:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7a89586-dc22-3daf-9a6b-666e0884f9c1 | -13.05072 | -53.71752 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e97f5464-27ec-311f-98fd-3def6417757f | -12.55588 | -57.70841 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 913ac472-7de9-3253-bbc4-e1d31e81db94 | -13.04286 | -53.73169 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4c463be-4da8-391b-8ca5-5b879b9a5521 | -13.045 | -53.73098 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64964963-d9b7-3c3e-a831-16968e1f2a77 | -12.55115 | -57.70772 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 966c559f-91f2-3ff0-8076-bbe340d569b7 | -12.55121 | -57.70903 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed5f2fdc-8c12-347a-9aed-4c82a54749f0 | -11.4006 | -52.95947 | 2025-05-02 05:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75d659e8-0d7d-312a-a4ab-d5e2467fe025 | -12.5553 | -57.71489 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19dff6fd-bcc9-3837-bd3d-5f5e5ec3535f | -12.55595 | -57.70975 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41464136-b847-3d75-bb49-7b7890417336 | -12.55519 | -57.71357 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4c17ccb-ff10-3537-8744-35bf8632af74 | -13.05356 | -53.71186 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3536c88-2475-33e4-b0e5-a5627a32533a | -13.04732 | -53.71127 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 173e0141-7e5a-3b65-8deb-08e58dec2bfc | -13.05298 | -53.71679 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a17e3f8-fa09-3c0f-8a42-4c0cd43d0833 | -13.05127 | -53.71259 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60541ba1-31e9-3071-be59-71aa2d331c2d | -13.05182 | -53.7266 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5db280b5-206d-3b63-b811-065ce384c5fd | -13.04504 | -53.71196 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fed7788-7862-3dee-866b-03a4f3ecaebe | -12.68017 | -58.09557 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d58fbd7-5ae0-360c-80bf-af5c1a572dc1 | -12.55452 | -57.71864 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee974722-83c2-3e66-a51b-b500d378e1ae | -12.55056 | -57.71417 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3c054fd-ef76-38a2-857d-11c305022289 | -12.55046 | -57.71286 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3445a286-f151-3e37-bf4f-070da378510e | -12.55466 | -57.71997 | 2025-05-02 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdb02366-7094-37c0-a2a5-1850d273b1c9 | -13.04674 | -53.71624 | 2025-05-02 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46b0b028-9840-3354-aeba-0e327b2fc00b | -21.46876 | -57.1576 | 2025-05-02 05:40:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c08c1952-9afa-3b2c-8172-f4b02fde5f87 | 1.11091 | -60.51595 | 2025-05-02 05:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe2ec117-9b8d-36a5-8abf-6cfb67caab70 | 1.11178 | -60.52133 | 2025-05-02 05:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09f5bca3-d221-34c6-b5d7-b1900ec6c478 | -12.55309 | -57.71424 | 2025-05-02 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0172ff3-f9f1-3445-8954-af15ac971eb9 | -12.55383 | -57.70735 | 2025-05-02 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c2067b9-e912-338f-bd69-d7af99b4a0da | 1.1188 | -60.51095 | 2025-05-02 06:46:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3d375446-6440-3015-adae-230d5da3a708 | -6.9615 | -42.7872 | 2025-05-02 11:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 60e20bdd-6e10-3d1b-9843-35ca3cee588a | -6.9615 | -42.7872 | 2025-05-02 11:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 74e456fa-9948-39ed-a631-26e65efbc871 | -9.23508 | -35.9424 | 2025-05-02 11:57:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 4c222dd6-47f9-345f-8335-1c6fddc2b9c6 | -8.82408 | -36.56611 | 2025-05-02 11:57:00 | TERRA_M-M | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d60c1af3-edcd-3d4a-aba2-020257a75c72 | -5.47308 | -35.58462 | 2025-05-02 11:57:00 | TERRA_M-M | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 1666bcd3-8564-345c-9554-7f42d89a50e8 | -9.54226 | -35.93924 | 2025-05-02 11:57:00 | TERRA_M-M | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| a30e3809-80b9-34f4-8525-e0cbce76f4bc | -9.71858 | -37.06821 | 2025-05-02 11:57:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 8575a49e-f5d7-370e-8028-afb15a629813 | -8.82559 | -36.55513 | 2025-05-02 11:57:00 | TERRA_M-M | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 6ba23740-f444-3eb2-941d-c178ace407e4 | -6.62014 | -41.70911 | 2025-05-02 11:57:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 421ecdb1-4c34-33d3-a841-1e60726d30fd | -6.06892 | -39.93034 | 2025-05-02 11:57:00 | TERRA_M-M | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 867b63cd-c878-3454-9dbe-569bd2588294 | -8.325 | -35.65822 | 2025-05-02 11:57:00 | TERRA_M-M | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 0a2668a8-3a1d-3b51-a27b-e3d30d6dd157 | -8.68678 | -37.14523 | 2025-05-02 11:57:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 42727872-54e5-3efa-93d6-c044b893be45 | -11.16619 | -37.53267 | 2025-05-02 12:00:00 | TERRA_M-T | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| ac54e736-d439-3d53-b43b-a07f158be1b8 | -10.72679 | -39.75481 | 2025-05-02 12:00:00 | TERRA_M-T | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 9ae85631-208f-3401-bd6d-e54b94141544 | -10.72551 | -39.76374 | 2025-05-02 12:00:00 | TERRA_M-T | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 39095b5f-8a25-38c1-97d7-c09f1bd4746e | -10.44588 | -37.81284 | 2025-05-02 12:00:00 | TERRA_M-T | CARIRA | SERGIPE | Brasil | 2801405 | 28 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7b07a598-2ed0-3be8-8bb7-ba8ed0dd5a55 | -22.96414 | -45.46948 | 2025-05-02 12:02:00 | TERRA_M-T | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 992336d1-4a66-316c-aa19-f07f4669e339 | -12.6172 | -46.7463 | 2025-05-02 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 7d20b9c8-fc5e-3a7e-ba51-576188097632 | -12.6172 | -46.7463 | 2025-05-02 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| d09f41da-8973-3435-bae1-1693a9bc6b2a | -6.9615 | -42.7872 | 2025-05-02 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 8b0ad80e-242a-35eb-87e3-422133c80196 | -6.9615 | -42.7872 | 2025-05-02 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| dfcf213b-2362-3a8c-a36a-6dda90446509 | -6.9613 | -42.8108 | 2025-05-02 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 09ea35a3-6afe-350d-bb2b-07d5061a22b6 | -6.9615 | -42.7872 | 2025-05-02 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 148.7 |
| 6f2d46e3-cdbd-3edd-8fe0-b51d3da0bd8f | -6.9615 | -42.7872 | 2025-05-02 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| cefa6782-dac9-30f9-8596-8150678075f1 | -6.9427 | -42.789 | 2025-05-02 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 407ef5ee-383e-3490-99e2-80fd55d8ca76 | -6.9615 | -42.7872 | 2025-05-02 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 197.6 |
| d34cc101-454d-370d-be08-0607e92a9ce9 | -6.9427 | -42.789 | 2025-05-02 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 135a1d5c-d79d-38d6-9d3b-76b820dd90f1 | -16.3181 | -53.8305 | 2025-05-02 14:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 7f3c6eeb-ce1f-30be-9db2-73ecb2c0c3d2 | -6.9427 | -42.789 | 2025-05-02 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 40609dfb-1046-3dbf-b98e-29e1e0b5a478 | -6.9613 | -42.8108 | 2025-05-02 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 2116ebe1-5f7c-3e02-8da7-ab1423cb26e0 | -6.9615 | -42.7872 | 2025-05-02 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 166.1 |
| 5b26bf25-12e3-3a13-b3aa-63cf34843a5d | -6.9613 | -42.8108 | 2025-05-02 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 4e3f1b12-8d85-3f53-a415-ebedbcd77b03 | -6.9615 | -42.7872 | 2025-05-02 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| 52f06f05-d48d-3d2c-8ae6-f6044ad84223 | -6.9427 | -42.789 | 2025-05-02 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| a883be9e-4087-3521-9aa1-1631a1b77928 | -16.3181 | -53.8305 | 2025-05-02 14:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| a8f97288-99d2-3987-a9ce-05b96b955855 | -6.9615 | -42.7872 | 2025-05-02 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 160.5 |
| aaccca44-a3a2-3a1b-b772-3dee4a3edf12 | -6.9427 | -42.789 | 2025-05-02 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| ff9ef194-3040-3093-9d9f-490ff6a13b7b | -6.9613 | -42.8108 | 2025-05-02 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 9b4a0665-dc6e-360a-ad5f-f0cea29c6341 | -6.9427 | -42.789 | 2025-05-02 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 7ddf4ad0-2ca7-3006-aa10-298d6006ea62 | -16.2985 | -53.8332 | 2025-05-02 14:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 78a69a48-5ceb-3de2-ae48-dfc9079418c1 | -6.9615 | -42.7872 | 2025-05-02 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |


