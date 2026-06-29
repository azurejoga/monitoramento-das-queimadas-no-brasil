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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 077c9c74-b824-3498-8209-f5a437dfded9 | -11.66166 | -57.25726 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bf5228c-0352-3240-8f68-07f7656a8ae6 | -11.88463 | -57.12713 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e28ae1cf-5f06-38b4-835b-80b31af7eeee | -11.49832 | -54.50002 | 2026-06-29 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca768e9c-906c-3110-81b8-a46bd37a66c7 | -9.08605 | -59.39964 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3d69e91-bd4b-380c-a4d2-2e92b95a2568 | -11.51908 | -54.79239 | 2026-06-29 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88f42728-83bb-32c2-b6ad-42023191603b | -9.08436 | -59.38607 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30d1a96d-d18e-3727-a866-185b2a783f9a | -9.08344 | -59.41689 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd7ef84a-9c20-3900-8d8d-02070c1257c7 | -11.21846 | -54.30314 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff8809cb-9404-3a08-814a-d58bfc185de5 | -11.91847 | -57.4058 | 2026-06-29 05:33:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d997a1e5-f349-353f-a2c3-4826f855f847 | -11.88841 | -57.13209 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8f5e251-0a14-3a1d-b7d5-deb8ec5eb515 | -9.32411 | -58.01378 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62df8c97-647b-3976-9216-1456176ce2a6 | -12.23328 | -56.56014 | 2026-06-29 05:33:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b890f565-35db-3a44-8ef8-f094ecf087e5 | -11.89598 | -57.14442 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bdc05f7-7632-3388-b4dc-8886346a0560 | -11.49792 | -54.50323 | 2026-06-29 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76805529-f6d1-3c90-9550-e0c249dd3016 | -11.21804 | -54.30645 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ef8aa49-2b51-3a08-b313-2bff86762152 | -9.60725 | -56.9215 | 2026-06-29 05:33:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8434a34-98c0-3886-adcd-868929d283b0 | -9.326 | -58.02909 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 817e8d41-4d89-398c-bb83-8c8feac04775 | -11.88403 | -57.13146 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2fd4ac5c-c455-3879-8a31-91a4412c6f36 | -11.49759 | -54.49875 | 2026-06-29 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 636b78f3-8d8c-3a36-937b-3a57b3a6c973 | -11.50394 | -54.49747 | 2026-06-29 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cecd7062-a635-333c-a376-b051c8edb901 | -9.09277 | -59.43016 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 659bb73f-4935-3d77-87c5-7f762044fa32 | -9.0807 | -59.38552 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f34cc1c6-b58b-3d4d-91d2-7796eb5b3925 | -9.18521 | -58.0685 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 025ed913-c94a-3a8c-8b36-ae1383567f8c | -11.89216 | -57.13953 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60372a90-d5f1-329f-ac96-6dcd1373c753 | -9.0824 | -59.39907 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b2317d5-10e8-3ca4-901d-d46ba3c67b9a | -9.09214 | -59.43447 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a90eb50-c38c-3441-8e9a-7788ad2bfa98 | -11.22026 | -53.83378 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9741d2f-e269-3722-8f84-8ce051da4d85 | -9.09114 | -59.44003 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f1b5331-2c4f-3502-98b3-df3c08cb3897 | -11.49912 | -54.49356 | 2026-06-29 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47f57ca2-50a6-3875-ac6a-a649daf706e3 | -11.91791 | -57.4099 | 2026-06-29 05:33:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57a4c825-953a-3406-9fc2-549e20b2b1a2 | -9.32748 | -58.01869 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7446dd51-5e58-3558-a850-7e77e2d9b16f | -11.88961 | -57.12337 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5d75af4-273a-36c4-ae6b-0e1a2c4974ad | -9.08109 | -59.40772 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3288a1d9-c094-3ddc-8d1a-e1bf5220b39b | -10.30291 | -57.12235 | 2026-06-29 05:33:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 47896525-ef0d-359f-8a26-5841ee6c84c4 | -9.0871 | -59.41745 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2522190c-b507-315b-9ca6-251e8a195d16 | -11.89329 | -57.13095 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9292a356-4282-3a0b-84d2-7ee3e75848b9 | -9.3281 | -58.01435 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22c1e788-ddb5-3ff1-b5d2-9dffda95a3dd | -9.3235 | -58.01811 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 652fdb8a-9daf-3186-b320-adb56c5e8182 | -11.50281 | -54.49941 | 2026-06-29 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af4b0c22-d000-3aad-8d1f-06f15cb3f45a | -11.52932 | -54.79365 | 2026-06-29 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 502359e6-2c10-3600-b67c-fdbe18d75e8c | -9.60237 | -56.92501 | 2026-06-29 05:33:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40e79d47-fb5d-3483-9153-caa9c23a85f1 | -11.51948 | -54.78926 | 2026-06-29 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6612b487-ac79-3733-85db-7c9895cb7c1a | -9.57647 | -57.01677 | 2026-06-29 05:33:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c13e20a-c804-31b5-a484-7f3de1e817c3 | -9.60667 | -56.92561 | 2026-06-29 05:33:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00e0ed40-987a-3552-bda0-7ba4406a1c3a | -11.88782 | -57.13636 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| febd4b39-49f1-35e2-9e29-c98e5693f864 | -10.32144 | -50.1843 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e859b2c6-53f2-3936-9e75-adbbb20d4ce2 | -9.08974 | -59.4253 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 824c78dc-83f8-3e25-a7ec-f2b5e1c9505e | -11.2112 | -53.81811 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b855bcb2-3f99-3d3c-8fa9-e37f2cc49ab6 | -9.08945 | -59.4266 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a03540b-9e27-3a8e-9146-294322984a2d | -9.08371 | -59.39041 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9ae02bb-de6d-3dee-890b-1e3bb6b7ae8b | -12.22997 | -56.54983 | 2026-06-29 05:33:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6375ba81-7f02-369b-9d27-eca652b23965 | -11.21074 | -53.82172 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bea8ec6-b4ca-3658-bbbb-9f3c4b81132c | -9.31804 | -58.02792 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| edb5af47-2e51-34ef-aabb-e1db78ebfb5b | -9.08305 | -59.39474 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f596c95e-ad1f-35d5-9a80-62119404f17e | -9.09037 | -59.421 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d41b65fb-83a4-36b5-8eb1-81ec00010ac2 | -12.23455 | -56.55051 | 2026-06-29 05:33:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e0339d0-4f1a-3fbc-9a54-ac5847fb60bf | -11.89654 | -57.14017 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7361826-c23c-3994-ab2a-276a7a70e587 | -9.08802 | -59.38662 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbbc84e0-1bbf-323b-81c7-00bdc3732ffb | -11.88085 | -57.12213 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32b05fdd-bac8-3ee5-8d23-e1aacef922f6 | -10.29862 | -57.12177 | 2026-06-29 05:33:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d8217676-1586-349e-ac2d-2e792caf126a | -10.97742 | -49.55784 | 2026-06-29 05:33:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7107e2c6-62df-3772-b4c4-02df5ceb72b5 | -9.5759 | -57.02082 | 2026-06-29 05:33:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2d5acd3-e73a-3a22-ab0a-e8f227c2829e | -11.49801 | -54.49554 | 2026-06-29 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f20bf82c-71e0-3cd9-a11b-68b0000fc593 | -11.51867 | -54.79551 | 2026-06-29 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ffc2c57-0200-3727-a693-bbf06c662deb | -9.0934 | -59.42587 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8089dde-884a-3a21-966e-509c508255c9 | -11.89598 | -57.14188 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72c45c7c-3fbd-37b2-9fb6-e9f3097ce2f2 | -12.54513 | -57.1824 | 2026-06-29 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e8cd090-fab7-3d40-80e7-20ae7f6191ae | -15.38269 | -59.48343 | 2026-06-29 05:36:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a605a4d-4ac7-3160-9aeb-6a7471b20ecc | -12.549 | -57.18427 | 2026-06-29 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76c41cda-f8f1-357e-ae7c-b0401a2f8206 | -15.07138 | -55.80988 | 2026-06-29 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d3c38a3-6564-3a32-943f-5e09310eb9bd | -15.07596 | -55.81149 | 2026-06-29 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b937716-99ae-3eec-b90e-ea8730e386e7 | -12.28593 | -57.54845 | 2026-06-29 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6c41a33-8320-326a-bcc6-a5f60757c98d | -15.07637 | -55.81067 | 2026-06-29 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 451adf6e-132a-3a1a-a00e-9ae684c05b28 | -11.90158 | -63.81304 | 2026-06-29 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe8b2c52-3222-3d0e-9201-f933f0e27f58 | -12.54459 | -57.18371 | 2026-06-29 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb1334ea-224b-3eaf-9e69-7a6cafa6c0f9 | -14.41227 | -60.20513 | 2026-06-29 05:36:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c89421fb-1e91-35c9-b74f-b17f3e7c4704 | -18.78453 | -57.36435 | 2026-06-29 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 0503b3e4-9817-32a1-95f8-ebe3046094ae | -18.78866 | -57.37028 | 2026-06-29 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cbbed357-12d4-3563-a28c-d1d46243fbe4 | -18.77915 | -57.36906 | 2026-06-29 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ac2a9e59-ff4e-3982-8a26-32ecc24698e2 | -18.77977 | -57.36374 | 2026-06-29 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 455db202-e723-3883-add8-45aa1382ae1c | -10.3176 | -50.171 | 2026-06-29 05:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| f3612947-13c0-3ef3-bf78-a44c0dfc70ef | -12.51995 | -48.29375 | 2026-06-29 06:14:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 76e32e19-5238-3962-a120-338dba4afaa0 | -10.32036 | -50.16562 | 2026-06-29 06:14:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 475878ae-911e-304a-9bd9-ea37b4805a92 | -11.48906 | -47.41281 | 2026-06-29 06:14:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| da5c6e94-deeb-336e-bd72-4c9cc0680dfa | -10.31249 | -50.1817 | 2026-06-29 06:14:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 27a594a1-dcf6-3211-a6bd-502c7c2ff30a | -10.31606 | -50.18993 | 2026-06-29 06:14:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 9f92fbdd-3720-3625-8d35-fda130f55d4d | -9.49686 | -42.98841 | 2026-06-29 06:14:00 | AQUA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 657ee05b-6a23-3261-8e67-2f56ae458f2c | -10.3176 | -50.171 | 2026-06-29 06:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| f64adf46-63fa-3a73-836e-d2d3879c6f90 | -9.08181 | -59.39994 | 2026-06-29 07:52:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 13ab4b5e-e1a4-3481-b303-88608bd744d6 | -9.07869 | -59.42433 | 2026-06-29 07:52:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b46d2751-9b83-313f-9776-528906685df3 | -8.2907 | -48.1876 | 2026-06-29 09:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 8670fe3e-d097-37e6-ba48-5b6b1dae55a4 | -8.2907 | -48.1876 | 2026-06-29 09:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 162.9 |
| d58d868c-03c2-352f-a13c-4d15b5acbf99 | -8.2719 | -48.1893 | 2026-06-29 09:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| b764d2e4-4817-3f98-9e2e-4dd7365ea2fb | -8.2905 | -48.2094 | 2026-06-29 10:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 123aaa4f-43e0-3f6b-ade3-193cc9cabf2d | -8.2907 | -48.1876 | 2026-06-29 10:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 209.2 |
| a6440222-1669-3f25-90c7-475c93914222 | -8.2719 | -48.1893 | 2026-06-29 10:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 8a5a86ea-6d89-3936-b58a-3225d5d5f35d | -8.2907 | -48.1876 | 2026-06-29 10:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 409de0b1-1115-388a-af34-9a23c21391cb | -8.2719 | -48.1893 | 2026-06-29 10:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 0a9e8a9e-e1f0-3721-aed4-2a515d45c255 | -8.2907 | -48.1876 | 2026-06-29 10:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 265124d5-4097-3c8e-abf5-dde75929839a | -8.2719 | -48.1893 | 2026-06-29 10:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 160.5 |


[Clique aqui para ver as próximas entradas](README10.md)
