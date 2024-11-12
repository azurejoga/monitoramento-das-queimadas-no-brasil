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
| 000fc503-86c9-3a99-9b6e-d69231d0ee0a | -21.55868 | -54.19677 | 2024-11-12 04:27:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe85fda5-8aaa-396e-98bf-48d4415ee09e | -20.32443 | -48.82882 | 2024-11-12 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 312e4a68-ad84-3ca6-98d9-6b1ee410f8da | -20.25371 | -55.07855 | 2024-11-12 04:27:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e513eb11-2b1b-3e17-8ed1-be9ad1e358fc | -21.31655 | -53.92292 | 2024-11-12 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e8b458f3-0526-3afe-b50e-dddad4533d48 | -19.16913 | -40.13392 | 2024-11-12 04:27:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1b8b1da1-e015-37d7-b4fe-e8ad8d25bd78 | -16.57355 | -44.07446 | 2024-11-12 04:27:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15b25c24-6f4b-37a9-8331-2ffea622df11 | -19.61938 | -54.15341 | 2024-11-12 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50a12047-2aac-3bf8-a997-ba9d365e235f | -16.00404 | -59.37602 | 2024-11-12 04:27:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9d31302-2aa4-32a7-bc64-860585a317d4 | -21.31562 | -53.92508 | 2024-11-12 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 75211d64-ce02-36a3-99e2-d147d2408187 | -20.9323 | -47.43854 | 2024-11-12 04:27:00 | NOAA-20 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aea6b6a3-ff28-3293-b5a4-22f787c8a239 | -20.10622 | -49.1891 | 2024-11-12 04:27:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 427f3c01-502a-3549-aaf9-952da1180c1d | -16.57099 | -44.06395 | 2024-11-12 04:27:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29ba393f-366f-3b5d-a9be-af32745cbc89 | -20.32054 | -48.83194 | 2024-11-12 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72be3f27-bd08-3a85-b592-8b606dde2d84 | -15.2978 | -56.50793 | 2024-11-12 04:27:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bea93be-2e63-308f-9a0b-3d9df3d9fcc4 | -18.03859 | -44.52664 | 2024-11-12 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d750b1f7-01b5-3af7-aefd-0e399bdde44a | -15.99677 | -59.38101 | 2024-11-12 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af67e1c5-9aca-3614-9b7d-f245ad5bcba0 | -18.90376 | -49.76941 | 2024-11-12 04:27:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76092cdc-18b5-343c-b0ae-feabbfe8dcf4 | -18.03474 | -44.52607 | 2024-11-12 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87186b62-baf9-372a-a094-4789b739441f | -20.10896 | -49.19335 | 2024-11-12 04:27:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8da8147-edb6-331c-92cd-07c1ee8ea390 | -15.30646 | -56.51546 | 2024-11-12 04:27:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0367fdfb-d7b5-3033-8eaf-61852de09837 | -20.04938 | -48.98748 | 2024-11-12 04:27:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fd7fea5-bd81-3a3b-a5d1-7a6b671ca38d | -19.34533 | -50.82312 | 2024-11-12 04:27:00 | NOAA-20 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1d0fc653-2d6e-3bf5-8d9a-fe91843f155d | -15.31621 | -56.51744 | 2024-11-12 04:27:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9df8e876-c1c9-3b79-b70a-90a1e63921f4 | -20.31998 | -48.83565 | 2024-11-12 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4fdd4f9-19b8-3218-b913-88a9a79ccb30 | -18.34774 | -40.0168 | 2024-11-12 04:27:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7559d44e-2705-3386-84f4-2ed4fa30922d | -19.62328 | -54.15417 | 2024-11-12 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4a10bf44-5b0e-3a17-bdf0-1344b75c2c6c | -20.10953 | -49.18968 | 2024-11-12 04:27:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e745b127-e82c-3569-9dc5-6ecd6e1d173e | -17.27404 | -57.4821 | 2024-11-12 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| cf39ef01-faa4-3575-9922-8e523f71f2cd | -16.34806 | -43.69842 | 2024-11-12 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f30f845c-8b84-37a6-b42d-2d745063c333 | -21.31282 | -53.92211 | 2024-11-12 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b92e4cb-ca7f-35f6-bea7-e57d67f1fd70 | -21.31648 | -53.92029 | 2024-11-12 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 16027225-610d-38b8-8b10-c52a3ce26f01 | -18.4481 | -47.55316 | 2024-11-12 04:27:00 | NOAA-20 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db8a6e31-610b-33c1-90ce-2693aa7493d1 | -20.63933 | -48.83667 | 2024-11-12 04:27:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7f315c9-fb41-38f1-a9e3-9f8513515125 | -20.325 | -48.82512 | 2024-11-12 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e91b6b7b-a521-3ace-ae94-94c6c7a639e5 | -16.0032 | -59.38009 | 2024-11-12 04:27:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5579290d-f119-388c-ac43-dda5e21ee7ba | -20.25776 | -55.07946 | 2024-11-12 04:27:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f03058c2-6b3f-36b9-ae39-50252ec19f81 | -21.19637 | -44.9398 | 2024-11-12 04:27:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 333df57c-1254-3f6c-8c91-cc508ffeec2e | -20.96281 | -48.6492 | 2024-11-12 04:27:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b3655bc9-28d2-373d-b022-131981a637eb | -18.29316 | -50.43416 | 2024-11-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef031085-b87f-38f3-b3b6-3e7f755b500d | -20.32224 | -48.82085 | 2024-11-12 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69be0d3f-2edc-37cf-8866-0caaf74b5dad | -18.34594 | -40.01887 | 2024-11-12 04:27:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b88b5108-0cc8-3b41-8d68-6d5d0f6f9026 | -21.31936 | -53.92588 | 2024-11-12 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 26eb6163-b971-3ee2-a1bd-a6271f8aaf33 | -18.44675 | -47.55325 | 2024-11-12 04:27:00 | NOAA-20 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0571d48-5e70-35f0-bd43-1ae2d08d64d3 | -21.32028 | -53.92373 | 2024-11-12 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9250b977-cf66-3cc2-8523-2edacdab31e0 | -15.99747 | -59.37866 | 2024-11-12 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06386084-7e0f-3537-944b-3ea64511aaf7 | -19.45868 | -39.75789 | 2024-11-12 04:27:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a4e349e5-2a80-3b95-8c05-f81eb35d366e | -20.39617 | -47.08113 | 2024-11-12 04:27:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83e8409b-4af5-3469-939f-b4789a2cb03b | -15.99091 | -59.3802 | 2024-11-12 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9baac3ff-3797-3652-ac0a-0addd5f1a238 | -21.2005 | -48.55754 | 2024-11-12 04:27:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1cb5b952-f495-3eba-8d40-d4250676e851 | -16.56942 | -44.06652 | 2024-11-12 04:27:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4332cc2-d185-3080-8dda-4cdfaac4fe10 | -18.39583 | -45.97705 | 2024-11-12 04:27:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37d53fa9-2cb0-3af0-a14e-fa0c9d453d00 | -20.996 | -51.79289 | 2024-11-12 04:27:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1f3fed62-69a7-30bc-825f-69ad677832d5 | -16.17343 | -42.19341 | 2024-11-12 04:27:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e338224e-d0b8-3e1f-8093-09c21d91095d | -21.63382 | -49.84305 | 2024-11-12 04:27:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1fde1c56-798a-38cb-80a1-cb9ac6953be0 | -20.22945 | -47.51314 | 2024-11-12 04:27:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bc1978b-8071-3004-81a6-7d7e2fa1ca9c | -17.59383 | -43.19893 | 2024-11-12 04:27:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c23862f-6ad2-39b2-aed6-ca01bdd12d25 | -16.57421 | -44.06947 | 2024-11-12 04:27:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b98d2ec-19ca-3e5f-a57c-53c85493159c | -18.03924 | -44.52169 | 2024-11-12 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb48376e-267f-3f40-9201-4000bf9355ed | -21.03295 | -48.65285 | 2024-11-12 04:27:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 13b0dc05-f019-3af2-a8c3-6bf7d365dc97 | -19.27359 | -49.1294 | 2024-11-12 04:27:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59473a5b-2c8a-3a0e-9266-ea6dd228225a | -19.19678 | -50.41232 | 2024-11-12 04:27:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ed1028c-71de-3666-b2e6-51115d1884d2 | -20.32167 | -48.82455 | 2024-11-12 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c04ec9c2-b7c4-3eec-8ebe-6ef95ff20f39 | -18.35148 | -40.01628 | 2024-11-12 04:27:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3c80dd74-5927-3597-a610-abb9697c5014 | -21.32021 | -53.92111 | 2024-11-12 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 683cf850-abf6-3744-ab02-07449d45a856 | -20.31734 | -51.64839 | 2024-11-12 04:27:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb380e90-ba79-3b66-a7f3-f209d9e2bbcf | -19.17432 | -40.13457 | 2024-11-12 04:27:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3c409f10-79aa-3b0c-b2ad-801adf5181df | -16.57012 | -44.06152 | 2024-11-12 04:27:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd8ebf87-2ea8-392d-ad16-706b05471b0c | -20.32111 | -48.82824 | 2024-11-12 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cc9dfb8-8298-34fb-bb42-ca16d14d9c1c | -20.39269 | -47.08057 | 2024-11-12 04:27:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 086de639-dfe3-3c2a-a244-1d46de19ca0a | -16.00427 | -59.3741 | 2024-11-12 04:27:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18634853-ebe0-32a8-b4f7-2d66236782bd | -20.11284 | -49.19026 | 2024-11-12 04:27:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7da8f794-398f-3c34-9882-e28ba8379427 | -18.34809 | -40.01355 | 2024-11-12 04:27:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d971cb7-5683-3823-b90f-871409745ce0 | -19.17544 | -40.13561 | 2024-11-12 04:27:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7f0ee117-2e3f-314f-8ead-fe170d168df5 | -19.17032 | -47.08072 | 2024-11-12 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc8155f5-7d8f-39ef-b0fb-79884f16672e | -16.57033 | -44.06894 | 2024-11-12 04:27:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb1aec86-b002-3f7d-8ee3-41376296854e | -20.76466 | -46.7694 | 2024-11-12 04:27:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 232e389c-1e36-338e-bd60-e4524399a478 | -21.31743 | -53.91816 | 2024-11-12 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1b49e9a-b74e-317e-bcbb-140727cf6ea4 | -20.52168 | -47.33154 | 2024-11-12 04:27:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d9ead3d-550f-361d-93f0-5a03a4ca2059 | -17.70708 | -44.73074 | 2024-11-12 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 429bf2f0-f620-3351-b922-804be2630310 | -20.11227 | -49.19392 | 2024-11-12 04:27:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9b2660d-eb4d-3df0-a74b-cb38ad61b26a | -16.00339 | -59.37823 | 2024-11-12 04:27:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ea332b0-ab7c-3803-b54a-7fdbbd282167 | -23.40415 | -46.55568 | 2024-11-12 04:29:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb74adc8-cc17-3b58-8af5-3ee513c73874 | -25.20217 | -49.40311 | 2024-11-12 04:29:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9288089d-0e77-3905-8717-e7a5b03b9051 | -25.18908 | -49.32836 | 2024-11-12 04:29:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 104a8837-7e4b-3e3f-81ee-c543dbde5ab2 | -23.94998 | -54.04163 | 2024-11-12 04:29:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5a8666fc-4b85-3322-bb0b-e03c897cf5cf | -25.20552 | -49.40374 | 2024-11-12 04:29:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a07e4ea4-4aae-3e9b-ac84-1c8fc355ffae | -23.59372 | -47.43964 | 2024-11-12 04:29:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 29f9e603-5435-3446-8074-ce2dd722e003 | -22.36779 | -54.41739 | 2024-11-12 04:29:00 | NOAA-20 | VICENTINA | MATO GROSSO DO SUL | Brasil | 5008404 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 02c1d6ae-0020-365d-abe3-db77ad3884d0 | -23.70373 | -46.47901 | 2024-11-12 04:29:00 | NOAA-20 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2d0a380c-80af-3bb7-bb00-b0f5c4825c1d | -25.2061 | -49.39985 | 2024-11-12 04:29:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8858879a-a9dc-3714-a374-2e880c19d8c8 | -23.98351 | -48.91824 | 2024-11-12 04:29:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5051d503-1413-3a94-80d4-065f6d82909f | -23.9536 | -54.04242 | 2024-11-12 04:29:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8b261d2c-747b-37ee-b0e2-c742ba33585e | -25.19546 | -49.40186 | 2024-11-12 04:29:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 946fb7a2-d540-33b7-a6bc-c0fc6e4dcce6 | -24.7157 | -49.47964 | 2024-11-12 04:29:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 18c8a5c2-853f-3430-861d-1b539eeae592 | -25.19244 | -49.32899 | 2024-11-12 04:29:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ff50bbc0-d984-31a0-8e86-ace490531e99 | -23.33819 | -46.77152 | 2024-11-12 04:29:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8b66adb8-d4e7-3bb1-b0d4-67832f2d3a24 | -3.0504 | -50.3332 | 2024-11-12 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 0ab8452a-f862-3b2f-93d6-034823e5fe09 | -3.0689 | -50.3326 | 2024-11-12 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 9a154cc7-4d54-3c93-8b6b-391248c90529 | -29.95072 | -51.616 | 2024-11-12 04:31:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 81246b57-4d8a-3cb3-80c0-eb0ac648a9fc | -2.1087 | -50.6916 | 2024-11-12 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |


[Clique aqui para ver as próximas entradas](README18.md)
