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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 880317c1-b9a6-3dbd-a33e-225390d5d73f | -12.185 | -63.655499 | 2024-10-08 01:46:35 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c61e9922-198c-3db9-8c27-412ca38fcac7 | -11.8851 | -62.7616 | 2024-10-08 01:46:37 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 74e422f8-3353-35f1-8784-1069cb8b86fa | -11.2524 | -60.365398 | 2024-10-08 01:46:38 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d2346d11-3be8-3f61-ac3e-770db74b8dab | -11.2551 | -60.376499 | 2024-10-08 01:46:38 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54cd4c4c-4b11-377d-9b80-7bd55d80edc5 | -11.2578 | -60.387501 | 2024-10-08 01:46:38 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 833ad8d0-0328-3e00-9af5-d5c4ff9d0b08 | -11.2454 | -60.378899 | 2024-10-08 01:46:38 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e0a94f91-2647-3c7d-a9da-a84eede18e35 | -11.2472 | -60.471699 | 2024-10-08 01:46:38 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a96f8d3b-a978-38b2-b26f-6fbc02294dae | -11.2499 | -60.482601 | 2024-10-08 01:46:38 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b704048-49c2-3d7d-b4a0-447145dd6d05 | -11.2709 | -60.569302 | 2024-10-08 01:46:38 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a0c04b20-3221-3f1b-b5e9-51e8b8a7f201 | -16.5462 | -57.7344 | 2024-10-08 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 1a3fd88f-b46e-3a0e-9745-c754df7579a9 | -11.767 | -62.875 | 2024-10-08 01:46:39 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 194bd272-0e33-3b04-a6f4-920f616a4caa | -16.9211 | -57.4881 | 2024-10-08 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.5 |
| fe1ebf03-f8a5-3bd6-a56d-16613c773bfd | -11.2298 | -61.170399 | 2024-10-08 01:46:41 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e872ad65-eee2-343e-bca0-666413da777d | -11.2322 | -61.180401 | 2024-10-08 01:46:41 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| faa91776-4750-30fe-8407-0f6313510a3d | -16.9924 | -56.7003 | 2024-10-08 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.6 |
| 194d18b8-14b6-3bdc-a178-fe04c0d17f75 | -17.0123 | -56.6773 | 2024-10-08 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 43c7e4c4-dbce-3240-bee0-82a7a8ecaf9b | -11.9058 | -64.921097 | 2024-10-08 01:46:44 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ddecb11-98a1-3e2e-80d1-151d3d71a7cd | -11.9073 | -64.9282 | 2024-10-08 01:46:44 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f5545e00-b1c9-37ee-a32e-bdec466d6960 | -11.6861 | -63.999298 | 2024-10-08 01:46:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a19204a-0c52-3042-8f9d-b9dcc8effee1 | -11.6895 | -64.014 | 2024-10-08 01:46:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a6848c34-e278-3972-9677-1c7cf134772c | -11.6912 | -64.021301 | 2024-10-08 01:46:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68afa396-404b-3161-ac05-9714142f5680 | -11.6746 | -63.994301 | 2024-10-08 01:46:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b8091a6c-01e1-3638-8572-330bbdb826c6 | -11.6763 | -64.001602 | 2024-10-08 01:46:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f9753739-5f57-3708-b094-e4dfb706d72b | -11.678 | -64.008904 | 2024-10-08 01:46:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 52c35208-7ae7-3fb6-9aec-e16ed8802aeb | -11.6797 | -64.016296 | 2024-10-08 01:46:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| feba99b1-0d4f-33e0-8ea4-3dfacc71a634 | -11.6814 | -64.023598 | 2024-10-08 01:46:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9dc7513b-4493-3552-8bdc-1da1db976772 | -11.6985 | -64.961601 | 2024-10-08 01:46:48 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 62eac9b5-c85c-3edf-a450-379fbb2693e3 | -11.6871 | -64.956902 | 2024-10-08 01:46:48 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d692506b-04de-3302-bd94-113b6b15574f | -11.6887 | -64.963898 | 2024-10-08 01:46:48 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7d06918a-af14-38f1-a3ce-f5ab2653c085 | -11.69 | -65.015297 | 2024-10-08 01:46:48 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 820592f0-db41-3719-8a0b-075e9e0d8568 | -11.6916 | -65.022301 | 2024-10-08 01:46:48 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2cfd2ef6-8c71-302a-9d04-f6fc24ef5182 | -18.6192 | -57.2603 | 2024-10-08 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 019b2317-6cec-3fcc-8e7b-07b0f5e03c24 | -18.6195 | -57.2396 | 2024-10-08 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 48fb949a-f2f7-34ac-b196-0f4ea83106cd | -18.6394 | -57.237 | 2024-10-08 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.0 |
| 9c0d755a-99fc-3778-92df-26f2ba4ae846 | -19.2723 | -46.1305 | 2024-10-08 01:46:53 | GOES-16 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 61c1cab8-c7e0-37d7-be32-5222dcd9b7c0 | -19.2729 | -46.1067 | 2024-10-08 01:46:53 | GOES-16 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 770ce9ae-bd92-32de-99f6-c11152130440 | -20.3732 | -43.9468 | 2024-10-08 01:46:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 138.5 |
| 26ec1d18-d089-3930-ba34-8b7819ec320d | -20.374 | -43.922 | 2024-10-08 01:46:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| 8172ab3b-ec77-3bdc-b92d-679cbc7e6ef8 | -20.393 | -43.966 | 2024-10-08 01:46:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| cc3bd0bc-858d-33c1-ae90-cb3c747cbe66 | -20.3938 | -43.9412 | 2024-10-08 01:46:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 239.2 |
| 36ccc374-baef-3cfc-88f9-18fb5a2baa27 | -20.3946 | -43.9163 | 2024-10-08 01:46:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| a72fdb34-4b42-3e33-8f48-260ee131f5ab | -20.4144 | -43.9356 | 2024-10-08 01:46:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| 0557ab36-42d9-37ba-8c33-8c4384d0411e | -20.6602 | -45.9105 | 2024-10-08 01:47:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 137.0 |
| d3b8b0e4-a2d3-3507-a8fa-4368bf9feeb4 | -11.6382 | -64.968102 | 2024-10-08 01:47:34 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4154a4ef-8947-344b-b669-e2bdd56b3b7a | -11.6691 | -65.196899 | 2024-10-08 01:47:34 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da48a316-393b-34f3-9e41-a4d4352663aa | -11.6707 | -65.203903 | 2024-10-08 01:47:34 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a74b393-90cb-381f-9ce9-6995258e0b3a | -11.5416 | -65.042198 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 48375961-a92b-38c2-abf8-4a999d6b23c9 | -11.5302 | -65.0373 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93012473-a90c-3c0d-af9f-e2081e290f1b | -11.5318 | -65.044403 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e831d85-1754-329b-a11e-b6a99a1911ba | -11.5393 | -65.123802 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 67b8e12c-7371-34d1-81e5-62d80f30398b | -11.5409 | -65.130798 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e12670d6-93c7-3ff2-9d85-c4f2a253f9bc | -11.5185 | -65.076897 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0efbfaee-bcbf-353e-a5a4-88530d9e9fec | -11.5295 | -65.125999 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 753621aa-0c7a-3e1e-9836-48eed51f8a2a | -11.5311 | -65.133003 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 98b38a68-604d-3cad-8f4d-98d3c38a83e1 | -11.5087 | -65.079201 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7071c863-605c-31e9-8fb9-360816ebaad9 | -11.5103 | -65.086197 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e58b2aa8-1678-3844-9c48-995307c16975 | -11.5119 | -65.093201 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3849a15f-11b8-3e3d-ae7c-fbd7e460a9f6 | -11.5182 | -65.1213 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5891916-4c19-3238-b207-68cd61a35846 | -11.5197 | -65.128304 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9b8b385-b9e5-323a-a869-5c99312d7046 | -11.5213 | -65.1353 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 13178953-4d48-3f70-ac5c-5a9c8c5a8c6b | -11.5229 | -65.142303 | 2024-10-08 01:47:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6505c9d7-8442-36c9-8497-12f9c255573d | -11.5092 | -65.219002 | 2024-10-08 01:47:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b71d9c1-94cb-34bd-a0c1-8eeda98076a0 | -11.5108 | -65.225998 | 2024-10-08 01:47:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f20b793c-2028-3dc9-8f2a-5a184312f9a4 | -10.9923 | -63.897202 | 2024-10-08 01:47:40 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 40412108-de9c-342b-9232-3b95fea5ccfa | -10.994 | -63.904701 | 2024-10-08 01:47:40 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1d10a100-7878-390d-8fea-dae3bf807351 | -10.9876 | -63.921902 | 2024-10-08 01:47:40 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cfb4738b-4871-3793-b6bf-6e96cca451c9 | -10.9796 | -63.931599 | 2024-10-08 01:47:41 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a701e3c9-4643-3dfe-a271-180269f349f0 | -10.9813 | -63.938999 | 2024-10-08 01:47:41 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8872b1-1515-382d-89d7-c7707958498a | -10.9783 | -63.971001 | 2024-10-08 01:47:41 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a36ab19-4565-3ee1-b536-3e476649a3c9 | -10.9198 | -63.851299 | 2024-10-08 01:47:41 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0362074f-08fa-3bfd-9412-0f6ea0cf8c0a | -10.9215 | -63.8587 | 2024-10-08 01:47:41 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 114652ef-0d36-3d6a-8447-d7e827f7b353 | -10.9101 | -63.8536 | 2024-10-08 01:47:41 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f9abf59-1014-3ae2-a2a5-6aecb1aab826 | -10.9118 | -63.861 | 2024-10-08 01:47:41 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 10e38493-ac3b-377d-b05a-f0bec34e4b15 | -10.8991 | -63.8955 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fbaefbb9-7675-3756-b459-e143db011666 | -10.9008 | -63.902901 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bb8727f9-c3a7-3307-8370-b58bbe8aed74 | -10.8893 | -63.8978 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1212d2c9-ecb9-3182-87a0-41feb31c11cf | -10.891 | -63.905201 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 787beab5-51f5-3521-86c4-e2390cc0c412 | -10.876 | -63.885101 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3361d63-b0f5-320e-8847-a9d85228cae8 | -10.8778 | -63.892601 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 864a64d3-3bf1-31e9-88fe-bfbdf63f8952 | -10.8795 | -63.900101 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 825bea03-a717-3aeb-a674-21418eb35e88 | -10.8812 | -63.907501 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fbbd270a-c532-3473-a9ed-c60bb4c6452d | -10.8628 | -63.872501 | 2024-10-08 01:47:42 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18e24166-f28b-33a0-bde9-bf71240e19b7 | -10.8646 | -63.880001 | 2024-10-08 01:47:42 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2f8feb92-0773-3b0c-9753-fc285c287cdf | -10.8663 | -63.887402 | 2024-10-08 01:47:42 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1bf33eb-767d-303c-b2e5-8fd19a4db5e8 | -10.868 | -63.894901 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dbba9cd5-72ac-39ee-8c7e-23a063b5b965 | -10.8697 | -63.902401 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d451fd3-c799-35fc-8124-83b70206a26d | -10.8714 | -63.909801 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e09546c5-62e8-3dd8-ace9-615163611e8f | -10.8732 | -63.917301 | 2024-10-08 01:47:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d5d6e284-9a5b-3f45-b401-25472dc87487 | -10.8582 | -63.897202 | 2024-10-08 01:47:42 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ec4504d-1bea-3e6a-847b-42153401d833 | -10.8599 | -63.904701 | 2024-10-08 01:47:42 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2a50a46-7d31-3dd6-830f-a93fdec4cd4e | -10.8616 | -63.912102 | 2024-10-08 01:47:42 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d380e2b-9ff0-3cba-9179-3b2804cbb430 | -10.8882 | -64.163002 | 2024-10-08 01:47:43 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 11017cfb-d7a1-3118-8966-6e4527adf31a | -10.8376 | -64.167099 | 2024-10-08 01:47:44 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba3cb78-15ce-34bc-896d-9db8ca5acc73 | -10.8184 | -65.1717 | 2024-10-08 01:47:48 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| df7f73c1-a3ae-363b-ac5d-e7f288b3fc1e | -10.6212 | -64.348198 | 2024-10-08 01:47:48 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bd5126e8-d3e3-35b8-9aeb-c8be7c26f03e | -10.6115 | -64.3964 | 2024-10-08 01:47:48 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1159f075-67e7-3672-a3bd-1ac35afb7c87 | -10.6165 | -64.418098 | 2024-10-08 01:47:48 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8dd07eac-1dc0-3db5-b90b-40ae15f4ce19 | -10.6396 | -64.519096 | 2024-10-08 01:47:48 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f79c932f-e4b3-33df-82f1-7087ee46a025 | -10.6412 | -64.526299 | 2024-10-08 01:47:48 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2bd1ab3-7468-335e-96d7-ec45d8f4f849 | -10.5971 | -64.513802 | 2024-10-08 01:47:49 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README24.md)
