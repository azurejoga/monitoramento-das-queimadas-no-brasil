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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42851334-36e6-3187-9f6c-7d25e38796f3 | -10.9606 | -57.2187 | 2024-10-10 01:59:35 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d93a00ad-523d-398c-8b19-d4cd00c56599 | -10.9652 | -57.2365 | 2024-10-10 01:59:35 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ab9306a-e774-34b0-b13d-0abf87b6e3e4 | -10.9463 | -57.2034 | 2024-10-10 01:59:35 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad6af796-45e4-3df9-95ba-92f3a5ab8cf0 | -10.9509 | -57.221298 | 2024-10-10 01:59:35 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9787213b-b559-3cfe-b92e-30380b4ed6e5 | -10.9555 | -57.239101 | 2024-10-10 01:59:35 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad1fc8ed-dc3c-3906-ac50-0510cc1a6f8b | -11.3228 | -60.411999 | 2024-10-10 01:59:42 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac61cee-cef5-3c6d-a2e3-87e7da9ae5a0 | -11.1979 | -60.408501 | 2024-10-10 01:59:44 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f86e7a76-fe1a-3262-b9be-dd011f25d7c8 | -11.1854 | -60.400002 | 2024-10-10 01:59:45 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 047b9dcc-8b7a-3932-b4ed-bbc940100bd1 | -11.1881 | -60.4109 | 2024-10-10 01:59:45 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9da6a958-ffd0-3af4-81da-5b01556486b5 | -11.1874 | -60.4921 | 2024-10-10 01:59:45 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 33563471-7f25-38c0-b21c-e3621e019114 | -11.1901 | -60.502899 | 2024-10-10 01:59:45 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9e3889-b347-3218-a281-bafaa309b107 | -12.3289 | -54.560299 | 2024-10-10 01:59:45 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 065d32ca-a440-311e-bb80-e267b47b639f | -12.3359 | -54.5858 | 2024-10-10 01:59:45 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 449d289f-c94b-3a52-b2b8-5e14bd2d14a8 | -10.3283 | -59.154999 | 2024-10-10 01:59:53 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a402768e-db0b-38b8-9993-a2310ec44642 | -9.8419 | -58.1283 | 2024-10-10 02:00:40 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e5aca42-a198-3af3-8f35-d8ca072236f6 | -9.8323 | -58.130798 | 2024-10-10 02:00:41 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d124330-61a9-34b8-88b0-e1673f2a1c01 | -9.8226 | -58.133301 | 2024-10-10 02:00:41 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07f14cf9-506c-34e4-a0f6-c4d72da90c1e | -10.3489 | -60.992901 | 2024-10-10 02:00:44 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db679556-d326-3a20-b74f-349f7349bdd7 | -10.3514 | -61.003201 | 2024-10-10 02:00:44 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fac2ef5-f09f-3a0a-b75f-b4e498d34cb6 | -10.3539 | -61.013599 | 2024-10-10 02:00:44 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2bbb9cb8-112c-3fec-a5dc-1a664772d515 | -10.3417 | -61.005699 | 2024-10-10 02:00:44 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a33b763e-3025-3a9b-a4b0-b22661e04179 | -10.2866 | -61.246101 | 2024-10-10 02:00:46 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b753f57-e07f-3c9c-a392-e5dac05c81ad | -8.5354 | -54.600498 | 2024-10-10 02:00:47 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be55c288-e360-37a1-95e6-0e7aadc7099f | -9.7906 | -60.316898 | 2024-10-10 02:00:50 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b45aad6-528a-3698-9308-914a16bb88b7 | -9.7935 | -60.328602 | 2024-10-10 02:00:50 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f78d1bb1-053b-3e57-9b51-64342ce57459 | -9.7809 | -60.319302 | 2024-10-10 02:00:50 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa501ca1-f4f9-3134-b2d6-aa19b6b8da61 | -9.7838 | -60.331001 | 2024-10-10 02:00:50 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8488e89b-ad71-3f0c-834e-4b4144e4510e | -9.3113 | -61.059101 | 2024-10-10 02:01:01 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6fd2d8-4255-307a-89cb-cdeeba9cae40 | -9.0423 | -61.269299 | 2024-10-10 02:01:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc1a70c1-02e7-3223-9e9f-0f9d9bcb37f4 | -9.0449 | -61.279701 | 2024-10-10 02:01:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| daa90d25-2dde-352d-afe9-47380dd869dd | -9.0474 | -61.2901 | 2024-10-10 02:01:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f18d01d5-a248-377e-88ed-2110d5baefc2 | -9.0499 | -61.3004 | 2024-10-10 02:01:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b5f6127-9b7f-316d-bf4b-5f4156f5e033 | -9.0326 | -61.271702 | 2024-10-10 02:01:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dbc0b471-8e38-3f8b-8247-71356cfeae58 | -9.0351 | -61.282101 | 2024-10-10 02:01:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 027a6558-b797-3574-9ef7-926beebdb3fb | -9.0376 | -61.2925 | 2024-10-10 02:01:06 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37c91bf1-26ca-3e42-8f87-0e7d7e98b8a5 | -9.0113 | -61.396999 | 2024-10-10 02:01:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f9edd5d-c15c-3d1f-b50e-635f7f380d92 | -9.0138 | -61.4072 | 2024-10-10 02:01:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e182107-43cb-3c8a-a0b1-f4a259e2c793 | -8.999 | -61.389099 | 2024-10-10 02:01:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9753666-5b32-3041-8f16-6fa22fbb2232 | -9.0015 | -61.3993 | 2024-10-10 02:01:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 664e3b5c-90c7-36d8-bdec-debc2521621f | -9.004 | -61.4095 | 2024-10-10 02:01:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec7497e5-738b-3697-bb7c-65118de43461 | -9.0065 | -61.419701 | 2024-10-10 02:01:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eacea75c-0241-3cf0-a39f-24c7f5ed434c | -8.9918 | -61.401699 | 2024-10-10 02:01:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a65095e-7ab8-3558-b5b7-45c11e6fd138 | -8.9943 | -61.4119 | 2024-10-10 02:01:07 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93e35a66-fdd7-3dee-aec5-9eabe362667d | -8.9504 | -61.614498 | 2024-10-10 02:01:09 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 08d8182a-1d10-33d0-bfc1-0e1fccd95b64 | -8.9527 | -61.624401 | 2024-10-10 02:01:09 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e51ad8b-9dec-3ded-ad46-2065498020fe | -8.9406 | -61.616798 | 2024-10-10 02:01:09 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a10058c0-fb4e-3af4-b0a1-78d629946103 | -8.943 | -61.626701 | 2024-10-10 02:01:09 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fdff5262-88e2-3540-ad97-c2ae6bf9e61d | -8.9454 | -61.6366 | 2024-10-10 02:01:09 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7075b2e-1e8b-37a4-9eaf-29286053d103 | -8.9332 | -61.629101 | 2024-10-10 02:01:09 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1dc7c390-3769-32d1-8a72-7756a312c50d | -8.0348 | -58.032101 | 2024-10-10 02:01:09 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2f715fb-03ec-30b7-a239-02c6a905cf76 | -8.0392 | -58.049702 | 2024-10-10 02:01:09 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba56f5eb-7387-3204-a17f-4e88c52178c8 | -8.9211 | -61.621601 | 2024-10-10 02:01:09 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2bf5cdcb-49b9-39b9-83b9-1e28efbfc007 | -8.9234 | -61.6315 | 2024-10-10 02:01:09 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b032cd1-acc6-30e7-82fa-7547bb83f239 | -8.9114 | -61.623901 | 2024-10-10 02:01:09 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 03fcf478-0e15-31b1-95fb-dbab0460581b | -8.9137 | -61.633801 | 2024-10-10 02:01:09 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bbcf2dbd-72d7-3771-8f16-77323973a848 | -8.829 | -62.3554 | 2024-10-10 02:01:14 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 693e858e-62b0-38d7-aa19-10ea08f8ef7e | -8.8312 | -62.364498 | 2024-10-10 02:01:14 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bf8639d7-7bfa-32dd-a7a5-7af9aeec240e | -8.8333 | -62.373501 | 2024-10-10 02:01:14 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd836f1b-0f8a-38d5-b765-e56e8c6e3a43 | -8.8214 | -62.366798 | 2024-10-10 02:01:14 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea95adae-7325-384c-9983-5ebf9fb10226 | -8.1539 | -61.182098 | 2024-10-10 02:01:20 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4658c18-6230-3c09-8f12-6265118a3cae | -8.1566 | -61.192902 | 2024-10-10 02:01:20 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc0e6ce-5452-38f3-80ed-e7c5534ef7ae | -8.6128 | -63.0952 | 2024-10-10 02:01:20 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dac5d24a-402b-3aef-8cc7-e7f64d115078 | -8.6148 | -63.1035 | 2024-10-10 02:01:20 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d54dabce-d3b9-347b-b157-9e4afca4015f | -7.7017 | -61.359699 | 2024-10-10 02:01:28 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 946a490c-90f4-3c35-8bdd-f741b9f9e462 | -7.0646 | -59.385201 | 2024-10-10 02:01:30 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 617fcd3b-1de4-341c-bca2-17c3d9799df4 | -7.0559 | -59.308498 | 2024-10-10 02:01:30 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a92b87f0-1536-3ede-baf9-77a933d1ca60 | -7.0657 | -59.306198 | 2024-10-10 02:01:30 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c9eecda-8515-3b6e-b459-cf783f6f4789 | -7.3973 | -60.616001 | 2024-10-10 02:01:30 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5604434d-91fd-3c54-8639-0e64c8425174 | -7.5648 | -61.220699 | 2024-10-10 02:01:30 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 318af404-fdb0-3535-a3d1-694a1ba0a08b | -7.5622 | -61.209801 | 2024-10-10 02:01:30 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca2c8843-ae61-3669-9f92-b9f1a44841de | -7.0136 | -59.428902 | 2024-10-10 02:01:31 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a313b7c-3229-36b9-b535-05f5c3c895b8 | -7.01 | -59.4142 | 2024-10-10 02:01:31 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e71d9b65-eddb-392f-b5fc-9be562247fce | -7.0064 | -59.399502 | 2024-10-10 02:01:31 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99fe4608-fa2a-3aea-9ac3-0643c00b7f63 | -7.006 | -59.273201 | 2024-10-10 02:01:31 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dac04bed-ef3e-3fd4-9d53-d0317596fc04 | -7.0549 | -59.3876 | 2024-10-10 02:01:31 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9e367fb-43f6-3ef9-a975-f5730a5d760f | -6.9553 | -59.443199 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5914280e-3253-3f78-ac13-3d1dfc4093cd | -6.9517 | -59.428501 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1ef1617-ea81-3c79-8853-b725902ede6c | -6.965 | -59.4408 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d312a9a4-a2fb-3196-9446-399bbb6cc67a | -6.9614 | -59.426102 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 611b5d80-b64d-335c-b882-4f256e76ec14 | -6.9578 | -59.4114 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b380bfb3-7571-35ad-81e6-03dce06071cd | -6.9747 | -59.4384 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a026e153-dd40-3b61-9f00-bfe6e4e5208d | -6.9711 | -59.423698 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2b19436-6a84-33d4-9d00-10940fbe19fa | -6.9675 | -59.409 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d95036a-8f3b-3f97-8503-583c4cbd5511 | -6.9602 | -59.379398 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33870a48-13e5-3f9e-8015-db0d8cf8f734 | -6.9565 | -59.364601 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c3925cd-b278-33d8-b0f7-d5dd97f0aa21 | -6.9844 | -59.4361 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e69b46c-63ea-35aa-abb2-61a73e71cd04 | -6.9808 | -59.421398 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fbfe61cf-af5f-3631-b180-1bf4e65d46d6 | -6.9772 | -59.4067 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47d9c06e-4901-3ec5-af7c-45cb38fe5b49 | -6.9941 | -59.433701 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0da8378b-794e-3504-aed6-29cc8c3ba29e | -6.9905 | -59.418999 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a2b2ee8-f259-35f4-8fa5-de83af85f37b | -6.9869 | -59.404301 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdc81927-4d42-30da-896d-c273144c991d | -7.0039 | -59.431301 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c7e9ce4-1c7e-3e98-a368-31a0d60867de | -7.0002 | -59.416599 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 106beac2-c965-3c20-a3ba-2aea8924a7a8 | -6.9966 | -59.401901 | 2024-10-10 02:01:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73cc77be-17a7-386b-ba57-49d7d1cf5af6 | -6.682 | -59.3367 | 2024-10-10 02:01:36 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71b0a8d8-4135-39ee-ad45-bf6f58e04ca8 | -6.6782 | -59.321602 | 2024-10-10 02:01:36 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2ad8e4c-624f-3924-a354-08643fae0a50 | -6.6917 | -59.334301 | 2024-10-10 02:01:36 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a00a893-3bc9-3d11-9931-98876af7d6ae | -6.688 | -59.319199 | 2024-10-10 02:01:36 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd79a335-e8bb-3ff2-8a2c-78165ba915c6 | -6.7014 | -59.331902 | 2024-10-10 02:01:36 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c68dd480-664b-3eae-9228-18f02f4133d4 | -6.6977 | -59.316799 | 2024-10-10 02:01:36 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README35.md)
