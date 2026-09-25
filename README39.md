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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23fbed47-0dd5-3c41-af99-1500a640aa36 | -7.80867 | -71.94691 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc609fa4-1933-35ad-a1ee-e8052db9187e | -9.22525 | -71.8628 | 2026-09-25 06:29:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6091d720-d54e-36ec-a1b3-1b467c513a8c | -8.00479 | -71.3092 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| affc645f-9ded-396b-992b-8f4da9431b85 | -7.51969 | -70.39404 | 2026-09-25 06:29:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a7b2753-6ce7-393e-b5c3-84079b076cc2 | -8.07231 | -72.40324 | 2026-09-25 06:29:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fd0e969-634a-3dc1-b0bc-8857e13fadfb | -7.86798 | -72.86759 | 2026-09-25 06:29:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00cd5260-09d7-3a14-9bfc-c7a890d45e25 | -9.46973 | -67.0761 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa415b32-9cc4-3c79-91bf-588a96c1ca0f | -8.51021 | -71.39108 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98c1a9fd-26ae-3d2c-b091-0561ab8d8c9b | -9.06706 | -65.70256 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc2f89fc-5776-360e-8e95-edc50201ae39 | -8.57821 | -69.93311 | 2026-09-25 06:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecc80fb4-427d-35b3-a659-ca8d53c51262 | -8.59049 | -69.99712 | 2026-09-25 06:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9a39bf4-3f99-35f2-aa6b-5b4fe79a12d9 | -7.86448 | -72.86707 | 2026-09-25 06:29:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc393cf0-6e6a-3b7a-ab59-213e508373a3 | -7.88041 | -72.99648 | 2026-09-25 06:29:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee37604a-f9e5-3b56-9e1b-b976383a317f | -8.27639 | -70.90767 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4751c1fb-8bde-3c2e-8a71-a990e0b9f23e | -9.55203 | -65.98793 | 2026-09-25 06:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba8896da-74fe-379e-81dd-201ed2c93805 | -7.9512 | -72.3898 | 2026-09-25 06:29:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b9a9427-a09d-334f-bbd5-80c4f8620cda | -9.38101 | -66.50671 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 781704e0-5db7-39ce-a067-f3f46bc9af22 | -8.90402 | -71.34546 | 2026-09-25 06:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96033035-f865-33dd-bd64-3223b925ed2c | -7.60656 | -69.89407 | 2026-09-25 06:29:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c304eff3-6a82-38a7-b82d-e800d7a6b845 | -8.02819 | -71.36006 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d0551d6-bb01-3f14-9a53-acd06a15545b | -8.95833 | -72.85069 | 2026-09-25 06:29:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffbd2617-2866-3d99-822a-6e80fe6d052c | -8.90019 | -71.34488 | 2026-09-25 06:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13fd51cd-84fd-31ae-bb26-1ccc3f841f02 | -7.35888 | -72.45892 | 2026-09-25 06:29:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3144e27-aee3-3e7e-b7ba-8d5957c3b7f8 | -8.03527 | -71.26111 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f229fd02-ccd0-3799-ac27-2afc22087d44 | -8.7851 | -66.59914 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17c71afe-d325-3aaf-ba1e-d6a7503d45d8 | -8.31372 | -70.54034 | 2026-09-25 06:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9483369-2fdc-335b-a0af-baadf0c530a0 | -8.26742 | -70.8045 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 675828ab-2dec-3ab5-9a0b-8299c34db93f | -7.94628 | -71.33825 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b6cf37d-c031-3058-9ed9-c6a1a249cf5d | -8.66332 | -70.91676 | 2026-09-25 06:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4aba36b-5c1c-35ba-9d81-52f8e9d6d4db | -9.1636 | -67.67999 | 2026-09-25 06:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca7d7123-fdb0-3d7e-abdc-d3f9e2a2a4dd | -11.03308 | -68.7517 | 2026-09-25 06:29:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0ae67f6-fff6-3ec6-a37b-09347e2c9e00 | -8.64283 | -66.85995 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60dd6bb0-4d64-39c7-93f0-1e53e6fe04cb | -8.22843 | -71.04591 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e353056-cd43-33d7-a40d-f18cb090407e | -9.06758 | -65.69853 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e1578c6-9a83-337f-98f2-9334c93731ce | -9.06369 | -65.7007 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f150618-5654-39a7-b9db-8a30e8b5c007 | -8.77983 | -66.59843 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e16b47d-8b8d-3eea-8fdd-0f58224c3f38 | -10.47422 | -68.40495 | 2026-09-25 06:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b06ec4dd-7923-3c25-ba71-5cf02826743e | -8.29265 | -72.83237 | 2026-09-25 06:29:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7bb312a-a339-3447-a981-799738885615 | -8.27062 | -70.81011 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4db1a53d-b06c-3efb-b220-00a2de7c21f0 | -7.80245 | -71.96347 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e9e5556-b4f9-3cab-90aa-59b40e93c467 | -8.84996 | -71.0883 | 2026-09-25 06:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 751efb7e-a59c-3dd3-b5ac-05ce1935940b | -8.27142 | -72.66307 | 2026-09-25 06:29:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1df27b7e-2c92-389b-8ff9-e328859b0d06 | -8.63766 | -66.85929 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e1aee8f-192f-3a11-afaf-ad5f10ba826e | -8.96187 | -72.85123 | 2026-09-25 06:29:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95a6a548-e0fc-34fd-be51-cba6b38deda3 | -9.55222 | -65.98952 | 2026-09-25 06:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13529878-1841-3361-9485-e57c5f275f5c | -12.25 | -50.83 | 2026-09-25 07:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2822ac75-90d4-33d9-a341-2594b1e8c933 | -12.19 | -50.81 | 2026-09-25 07:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6a2e3a36-ec82-3a20-9eb2-8055f2cf05de | -12.22 | -50.82 | 2026-09-25 07:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57444b50-0cca-3172-9282-ea34e39aa10f | -12.24 | -50.77 | 2026-09-25 07:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7fc0ec7f-5543-38fb-a335-46c507e88e42 | -12.21 | -50.76 | 2026-09-25 07:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5f2d8fe-26a8-35c6-9b9f-26a6999d2ef4 | -11.9974 | -50.6921 | 2026-09-25 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 14217f2c-df21-35de-b054-f1dfa227c017 | -11.9971 | -50.7135 | 2026-09-25 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 98f0aa2f-3ee4-328d-9892-e032b27d1930 | -12.0162 | -50.7113 | 2026-09-25 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 30313bb5-7cd7-365b-8816-398d99b3fdaa | -6.633 | -59.9457 | 2026-09-25 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f7051c9c-45bb-33eb-a6de-584fca4d48d7 | -11.9783 | -50.6943 | 2026-09-25 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c2d05dae-4f45-381a-b62e-ec5bd44a5ddc | -11.978 | -50.7157 | 2026-09-25 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3bfefd1e-918d-3147-8106-37353aacab5a | -12.2244 | -50.7936 | 2026-09-25 07:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| fb935bea-3499-3a93-810c-4ba6f890a6df | -12.2435 | -50.7914 | 2026-09-25 07:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| a83356c3-0c0e-387a-977b-f8d7e9134c48 | -12.2623 | -50.8105 | 2026-09-25 07:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 4d1c65ab-a44e-3783-80f6-a4cc4b3eba27 | -12.2626 | -50.7891 | 2026-09-25 07:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 160.5 |
| ac717e5e-a2a9-3cc0-9832-d2f44a938786 | -11.9971 | -50.7135 | 2026-09-25 07:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 518d03c3-6275-3004-84f7-e78dcaa4c4ba | -12.2432 | -50.8128 | 2026-09-25 07:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 154.6 |
| ad45a2f4-625b-381f-abea-33b6bde3ff3a | 3.07903 | -59.97059 | 2026-09-25 07:52:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0740f116-d6c7-3425-9f87-a80f6acc1a6d | -3.72274 | -61.74948 | 2026-09-25 07:54:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c2e23375-592f-372f-9f35-d0cbc8d85703 | -6.43326 | -59.9544 | 2026-09-25 07:54:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 15e7db2e-ba3a-3ed8-bc81-c037f8afcbb6 | -8.63529 | -66.85382 | 2026-09-25 07:56:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b4a9c9b3-8926-3d7d-88ca-c3563d42b885 | -9.38372 | -66.50262 | 2026-09-25 07:56:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cae88def-9fe0-3787-bb12-2f37d0b6f89e | -9.30014 | -62.30267 | 2026-09-25 07:56:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea3110e4-525b-3569-a39b-97d15b4ddaa1 | -9.02115 | -60.52115 | 2026-09-25 07:56:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 81080f61-ff94-396d-af69-e9b05377849f | -12.2432 | -50.8128 | 2026-09-25 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| dde4e63a-4105-3e69-8fd5-aed844d79854 | -12.2241 | -50.815 | 2026-09-25 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 626068a8-a53f-385a-a65b-7d2366a63fa5 | -11.9593 | -50.6965 | 2026-09-25 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 62979088-ca27-3b76-9167-7869f862b7ec | -12.2623 | -50.8105 | 2026-09-25 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| d487c409-1638-3bae-9b30-50c41b091277 | -11.9783 | -50.6943 | 2026-09-25 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| da5c15a4-783c-301e-9ebc-c6dce057e07a | -12.2626 | -50.7891 | 2026-09-25 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4cd8b7bd-b68a-3e11-ad3a-d2008f5e8411 | -11.9974 | -50.6921 | 2026-09-25 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 674b64c8-0841-38bd-97b6-78cd6a3dd603 | -11.9971 | -50.7135 | 2026-09-25 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| a1f00923-4544-310f-998a-d0d486698d8f | -12.2432 | -50.8128 | 2026-09-25 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 174.9 |
| b17a8d0c-aa74-3bf3-af97-3359f4d4574b | -11.9593 | -50.6965 | 2026-09-25 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1689762f-12af-3832-9d44-b6267403aba2 | -12.2626 | -50.7891 | 2026-09-25 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 85594f9c-cf60-37ce-857e-685a3968d83c | -11.9974 | -50.6921 | 2026-09-25 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 1c73cdef-5bbd-3156-9ec9-91025d0b2277 | -12.2623 | -50.8105 | 2026-09-25 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 4c3049b1-26bf-333d-992d-cf145796e836 | -11.9596 | -50.6751 | 2026-09-25 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e721c96f-27ab-3868-afd9-40405287cdfc | -11.9783 | -50.6943 | 2026-09-25 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 67dd6205-7926-3f39-875e-8f36ef164ff2 | -12.2435 | -50.7914 | 2026-09-25 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 412a2fd5-ebdb-3362-8c5a-929a68c4d32b | -11.9787 | -50.6729 | 2026-09-25 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 134fcb04-3748-3a43-bc91-aa0479a21454 | -12.2241 | -50.815 | 2026-09-25 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| bfb76228-f35b-338c-b6a1-d1d9d54078fc | -12.2435 | -50.7914 | 2026-09-25 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 458526a8-3ad3-3c66-a962-8012839f53f9 | -12.2432 | -50.8128 | 2026-09-25 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 3ea8634d-2c4f-312d-be05-ab25ec702345 | -11.9596 | -50.6751 | 2026-09-25 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a80af49f-b37d-3928-8d1a-0f07aa092704 | -12.2626 | -50.7891 | 2026-09-25 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 50df2d11-601d-33ca-b0d9-fcc88dad4d0c | -11.9783 | -50.6943 | 2026-09-25 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 63101e92-dc9c-39b7-9849-9eb4024daa00 | -12.2623 | -50.8105 | 2026-09-25 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 881d78a4-ac69-370c-9f8f-d2941c49e3a7 | -11.9787 | -50.6729 | 2026-09-25 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| bb16ef28-b905-3f4b-a3c5-e6a9ee05c308 | -11.9593 | -50.6965 | 2026-09-25 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 00f43db0-d44f-3db9-b840-ecf36bfa43db | -6.633 | -59.9457 | 2026-09-25 09:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| b2f7fd27-7b90-3f2a-9c90-e6236f41ceff | -11.9968 | -50.7349 | 2026-09-25 10:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 3cab5007-0dad-325a-b9c7-e84e2e1ba591 | -12.0158 | -50.7327 | 2026-09-25 10:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 649.5 |
| fe492cdb-b087-3943-a8a4-4270e38b0492 | -12.2241 | -50.815 | 2026-09-25 11:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 6ffea614-954b-39e9-b946-a6c011b6694b | 2.3494 | -50.76928 | 2026-09-25 12:02:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README40.md)
