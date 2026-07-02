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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a550352e-74f1-3a3e-8e68-7c16e1f1ef18 | -12.5097 | -48.284199 | 2026-07-02 01:17:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41057185-95b8-371c-ab93-f259da104b07 | -11.3681 | -55.4319 | 2026-07-02 01:17:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 721bf4ef-97a8-35ab-8127-0e4c74f95682 | -12.7696 | -44.496498 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7aed2029-7223-302e-939e-b2b61430befe | -12.5336 | -48.296398 | 2026-07-02 01:17:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86754965-8167-3b70-a2fe-f6713b3e63c9 | -12.8587 | -44.335701 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8f9e190-ad15-366d-8dc7-c3dfcf0daa8d | -12.8403 | -44.3069 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 86c8b520-fbd3-3893-a437-31ce8af777df | -12.7523 | -44.434502 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bbba62e0-dc2f-34b2-a751-3bd68977e9dd | -11.6284 | -59.017899 | 2026-07-02 01:17:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 586ab62f-b6da-3128-a659-3d985c2a2543 | -9.1911 | -58.0466 | 2026-07-02 01:17:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b55b1b9-59c7-397e-a0d9-5290420055f7 | -12.7782 | -44.527302 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 203fbc5f-a679-36e7-93df-d2486dd056f5 | -22.6029 | -47.9785 | 2026-07-02 01:17:00 | METOP-C | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3d93bb6c-5f81-3cd1-a898-a49e66651fb3 | -11.4298 | -56.0583 | 2026-07-02 01:17:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6db7afd1-b092-3434-931b-f9cc3e9c222a | -12.8769 | -44.3643 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d770273d-7933-37da-8b0a-04464920fa50 | -12.524 | -48.299 | 2026-07-02 01:17:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61a4942f-59e1-37c0-ba1b-1b8b59ce74bf | -11.0499 | -56.925499 | 2026-07-02 01:17:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75d7d7fc-14df-3c44-8fa8-bcb85df7a932 | -12.8593 | -44.3013 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0ac350e-ad45-30da-83fb-1af0e41aa4ca | -12.8865 | -44.3615 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c6face3-7137-3330-ac38-34747a23aa17 | -10.1302 | -52.091801 | 2026-07-02 01:17:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b58495c6-8d27-35e3-a019-07ac888aac78 | -11.8087 | -57.000599 | 2026-07-02 01:17:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d717189-037c-327d-a694-c81e3e5542f3 | -4.0153 | -48.060902 | 2026-07-02 01:17:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dfa6feb-12f2-303c-84a5-33215bb82fa3 | -8.6648 | -49.713699 | 2026-07-02 01:17:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82d9b807-6af1-3559-87e5-de5ea82589d4 | -21.77 | -56.291901 | 2026-07-02 01:17:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d9f835ad-6217-3fc5-96be-188026270c1a | -12.5291 | -48.278999 | 2026-07-02 01:17:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 450996fe-bf18-35de-9073-10f53cc93f66 | -8.7207 | -48.347599 | 2026-07-02 01:17:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efe1c0f7-9079-3ca5-9b17-b5bfcbe104ad | -11.4216 | -56.0676 | 2026-07-02 01:17:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf031848-4c51-3119-b8c1-11c7ccb08f8b | -11.4282 | -56.0513 | 2026-07-02 01:17:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe0e7407-8fe1-3e91-a15e-aff047f9d175 | -11.8557 | -48.2323 | 2026-07-02 01:17:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29f11fee-200b-3d9e-a4dd-ad62d2930e02 | -11.3566 | -55.426899 | 2026-07-02 01:17:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4ea2c56-6242-330c-b5b0-8dff1c8fde64 | -11.7974 | -56.995998 | 2026-07-02 01:17:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23258fcd-aa5b-3a01-bd68-d12cc84cdcb3 | -3.5221 | -48.047001 | 2026-07-02 01:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3474931-5258-3802-95e4-5a6ca97c6e05 | -21.781401 | -56.297501 | 2026-07-02 01:17:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 81437dc3-8a67-33cb-8dec-ddff00e611a6 | -10.7017 | -49.6105 | 2026-07-02 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62abda88-10a3-3a0c-801d-8867eebd0617 | -21.768299 | -56.2841 | 2026-07-02 01:17:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7c7ea8b2-ba32-3bee-bb86-a17e548f1460 | -9.1926 | -58.0536 | 2026-07-02 01:17:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 113513c2-a6ed-3cc5-b016-6ad6ba3d6122 | -12.8498 | -44.3041 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 429ec882-9907-3c18-9aae-8e4856b5a7fe | -11.1707 | -50.077499 | 2026-07-02 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a5c6319-a4b1-38bf-86ba-5e7a8261a9ff | -10.1328 | -52.102501 | 2026-07-02 01:17:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f38043d6-b186-3d19-9a6f-3e15652cee89 | -12.8491 | -44.338501 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ef9e705-b663-351e-a826-b45442683db0 | -12.7706 | -44.462898 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1de4fbb3-8a65-3120-b596-21d2a71c5ec1 | -12.7428 | -44.437302 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a881e848-8d00-30a0-8389-0d538bcf2962 | -11.4314 | -56.065399 | 2026-07-02 01:17:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3cf9a61-6895-3a01-bdcf-f109269f0b1e | -9.9772 | -54.427601 | 2026-07-02 01:17:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 800a5edf-35fc-3c33-90ec-b41790d4af2f | -12.8682 | -44.332901 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59ae79d8-7ca0-3f33-85c7-56e1b9bd80ef | -11.3664 | -55.424599 | 2026-07-02 01:17:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46886c34-b727-3558-ac9a-905f970598ba | -12.7686 | -44.530102 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e381de0f-88d5-39a3-b99f-126f37e8b758 | -8.7303 | -48.3451 | 2026-07-02 01:17:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6644cc63-008f-3ab7-96b1-d3065ea4a1f2 | -8.7156 | -48.327599 | 2026-07-02 01:17:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb7883b8-1ddf-3083-a5a5-e3139fe4c6a4 | -12.8777 | -44.330101 | 2026-07-02 01:17:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e68b042-6964-39df-9237-963f36cc24b6 | -11.8603 | -48.250198 | 2026-07-02 01:17:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 495ec7d7-93a4-3d5b-a1fe-dc24304959c6 | -8.7252 | -48.3251 | 2026-07-02 01:17:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c08efc68-8289-3a88-a0ea-485ba267395c | -12.5135 | -48.2802 | 2026-07-02 01:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 7bae9bed-1546-315d-85b0-2e8afd8a74ca | -11.4149 | -56.0525 | 2026-07-02 01:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 14c7aa82-04ec-3fbd-8cd4-d1cf19294a22 | -8.7208 | -48.3441 | 2026-07-02 01:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 209abf6b-5dce-36ed-9c33-2cb2c1f3c891 | -10.9593 | -43.0326 | 2026-07-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f16ff420-fae3-32f2-b31e-56c0abf0c31a | -3.5043 | -48.039 | 2026-07-02 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| e183ea94-d8c9-347e-a3d0-f9f1a357e4b0 | -11.8007 | -57.0032 | 2026-07-02 01:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| c53d6e2a-c7df-32a9-af0f-30bd346e63e6 | -10.9588 | -43.0565 | 2026-07-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| ce53de2e-c4ef-31a7-a2a5-66c6a666021e | -21.7827 | -56.2762 | 2026-07-02 01:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 0353d0a7-820e-3c8a-85f8-90aac7d74b46 | -21.7823 | -56.2976 | 2026-07-02 01:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 53624b63-b3da-3d9f-8c68-b77e7fca28ac | -3.5228 | -48.0383 | 2026-07-02 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 29132c6a-cf27-359c-b047-41cc6dd4d44c | -11.4147 | -56.0726 | 2026-07-02 01:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e8672e8d-3310-3594-99ee-e54ad23f6705 | -9.2123 | -45.3092 | 2026-07-02 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| e4052fd0-0554-3042-9ef8-63576e631f53 | -21.7617 | -56.301 | 2026-07-02 01:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fd6e28b1-c438-351b-ab0b-3212f0c1d0c3 | -9.1933 | -45.3114 | 2026-07-02 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 2f8c30fd-d300-3ffe-bed7-fbe60be0261c | -10.9397 | -43.0593 | 2026-07-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 354bcff4-4341-3bf2-a1a6-7320521c5bf3 | -10.9401 | -43.0355 | 2026-07-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 31168d34-c21a-3561-a849-4c2d2bb22603 | -10.9593 | -43.0326 | 2026-07-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 8026d88a-b828-3866-a1d0-bf40938a53b7 | -21.7827 | -56.2762 | 2026-07-02 01:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 108.6 |
| fdc0d75c-2efe-38ba-9eb6-8e2d39f86e9a | -10.9588 | -43.0565 | 2026-07-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 0667a927-e16e-3b8e-8dff-a0010ed10ee8 | -10.9401 | -43.0355 | 2026-07-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| ad497eb9-3cbc-3890-b9f4-87618d65d759 | -3.5043 | -48.039 | 2026-07-02 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 3702065b-d389-3114-a08e-ac2a3db9251f | -12.5135 | -48.2802 | 2026-07-02 01:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 075b903e-0bbc-341e-b678-f7abd72673d7 | -10.9397 | -43.0593 | 2026-07-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 49f42bb0-3cb3-3815-a3b2-293ea789a337 | -11.8007 | -57.0032 | 2026-07-02 01:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| cf558c44-b841-3725-9594-a477da7c545e | -21.7823 | -56.2976 | 2026-07-02 01:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 127.4 |
| eb8be4ad-15f4-3976-827a-66ef1d3496e0 | -11.4147 | -56.0726 | 2026-07-02 01:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 32399590-d65c-36bc-ad50-45e352f4659d | -11.4149 | -56.0525 | 2026-07-02 01:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ae351003-4501-3649-a21e-f5d0485cd175 | -10.9401 | -43.0355 | 2026-07-02 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| b1ee1b58-3ae4-3388-8af5-39b24a33a782 | -11.8007 | -57.0032 | 2026-07-02 01:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 76215087-8e91-3148-b0b9-96170ea8fc6f | -8.7208 | -48.3441 | 2026-07-02 01:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| d84b8c6e-2a09-3f2a-aba9-f3a1bd963227 | -10.9397 | -43.0593 | 2026-07-02 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 7f9ef961-33c7-35a5-8300-9fb9fb8d4682 | -10.9588 | -43.0565 | 2026-07-02 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| af0f8748-fc15-3a65-aa5e-b46820eaa71e | -12.5135 | -48.2802 | 2026-07-02 01:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 014270db-6bb5-32f6-bcc3-43d0148da26a | -11.4149 | -56.0525 | 2026-07-02 01:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e73d1269-f5ef-3263-ac1a-68d0811adb15 | -21.7827 | -56.2762 | 2026-07-02 01:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 43970aed-75a0-35ec-abb1-40bb35c41e5b | -10.9593 | -43.0326 | 2026-07-02 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 73c8f7c1-a999-3221-a7a3-adedf74885cd | -11.4147 | -56.0726 | 2026-07-02 01:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 71720090-940e-35eb-8c67-61823fcd20e6 | -3.5228 | -48.0383 | 2026-07-02 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| e84035df-33ce-35be-bf49-faf499335a6d | -21.7823 | -56.2976 | 2026-07-02 01:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 6339d3ed-abf3-3769-b69c-9ee87d373e5e | -21.7617 | -56.301 | 2026-07-02 01:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4fe8d275-a0d7-3b3d-9332-14fbf373cd13 | -11.4149 | -56.0525 | 2026-07-02 01:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 061ed3f0-257a-3d7c-adfc-99c6947be5be | -11.4147 | -56.0726 | 2026-07-02 01:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5ca0cb24-0b8e-34cc-a949-3d508dd79a2b | -3.5043 | -48.039 | 2026-07-02 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 23ea4d4b-b643-3892-ae8c-ad6f761410d3 | -12.5135 | -48.2802 | 2026-07-02 01:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 26fa91e6-2c17-3d62-a67a-25b344d3ccc8 | -21.7823 | -56.2976 | 2026-07-02 01:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 90b0fc73-3eab-30b9-aca6-2f82b1f222b4 | -10.9397 | -43.0593 | 2026-07-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| aab77ce3-41c6-3ee3-8a98-dcc078f865a4 | -10.9401 | -43.0355 | 2026-07-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| d9219ee9-274d-3a5b-b155-95342a324abb | -11.8007 | -57.0032 | 2026-07-02 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9c779540-ba33-394a-8f68-8e6f73a4456f | -21.7827 | -56.2762 | 2026-07-02 01:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 53f1e3ec-f6b7-3557-a595-d6bc1bd5226a | -11.4147 | -56.0726 | 2026-07-02 02:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |


[Clique aqui para ver as próximas entradas](README6.md)
