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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d926b17b-eada-3c5e-bf69-f0908a0b491a | -22.24788 | -55.53839 | 2026-07-02 04:42:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7664e885-2d31-3bbc-b234-a6a61644c25c | -21.78158 | -56.28816 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0c2d06f-ef1f-3798-905f-7f231c316f8a | -21.77293 | -56.29159 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 38d1df7c-a549-370b-87bd-187dc258e3d8 | -21.77006 | -56.28554 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 8199e58c-829e-3aa5-9822-299b3ccb69e5 | -23.5647 | -47.50894 | 2026-07-02 04:42:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e39e86c3-72fd-3adb-8b59-9ba23c012844 | -21.36007 | -56.12109 | 2026-07-02 04:42:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17af7842-5fba-3231-91c3-808bc3025463 | -21.78061 | -56.29334 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dffefbe0-885a-3c57-9a10-9a20d65ae5b8 | -22.69952 | -53.96079 | 2026-07-02 04:42:00 | NOAA-20 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 69a7285e-b456-340f-b953-5be61495c223 | -23.56087 | -47.5083 | 2026-07-02 04:42:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 51a21280-5967-3327-a2e8-496d063e114f | -23.56268 | -47.51036 | 2026-07-02 04:42:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e53aa01e-a4c3-32fc-9f46-306aaed0b69d | -21.76525 | -56.28986 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 52c525eb-67f6-3e14-9f5a-87a0c9356340 | -22.44857 | -55.55181 | 2026-07-02 04:42:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 279eb57c-8292-3bc2-b566-e8d481ff92e6 | -21.78444 | -56.29422 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1cc56d64-94b9-3f30-8b6d-404471dfc5fd | -22.70022 | -53.95677 | 2026-07-02 04:42:00 | NOAA-20 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 70d1d1d0-2492-3a07-b8d0-8b9d8101556c | -22.69609 | -53.96012 | 2026-07-02 04:42:00 | NOAA-20 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bc253610-361f-3a36-836e-22de0f7fb267 | -21.76909 | -56.29073 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b335f667-451d-3048-a83a-4ab04ab98811 | -21.7739 | -56.28642 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 2e29f34f-77aa-3618-8692-14f6806117e0 | -23.56402 | -47.51407 | 2026-07-02 04:42:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d718e9a8-c64a-3a87-ba9e-050f3f4e0088 | -21.77774 | -56.28728 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 3c6cd31d-5b3d-36a6-a2bc-4bd874a7f077 | -22.79318 | -49.34571 | 2026-07-02 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf08b5e3-8691-3801-8885-af3d32bd5bad | -22.24421 | -55.53761 | 2026-07-02 04:42:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 893fbac3-7a9f-30c8-9450-0b347ec65061 | -21.80483 | -52.71815 | 2026-07-02 04:42:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b142cfe-239f-3a2d-9415-f3a3623a403f | -22.69667 | -53.96101 | 2026-07-02 04:42:00 | NOAA-20 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2afd885d-ce70-3b35-866b-f5be464200c4 | -22.7926 | -49.34983 | 2026-07-02 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29d3c104-0600-366c-b5c3-2bab55502c97 | -22.77424 | -46.99625 | 2026-07-02 04:42:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 181ae7f6-96be-34f3-aa90-d62e07f5f0ae | -22.53807 | -46.97215 | 2026-07-02 04:42:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c076c519-c082-3413-b92a-9a5af6d3c33c | -22.9602 | -52.70138 | 2026-07-02 04:42:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6dfcfbde-d1aa-377e-b171-e3d76b6fa514 | -21.77963 | -56.29856 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 528f7f80-a7b4-3f21-a257-489b6b1f4a9f | -10.9397 | -43.0593 | 2026-07-02 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 43aa0876-d458-3ee2-b6d8-999a6794d906 | -12.8557 | -44.3154 | 2026-07-02 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 1e676841-f465-3700-bae0-de49a6691fc2 | -21.7823 | -56.2976 | 2026-07-02 04:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 83.3 |
| cb572247-9903-3405-a0d6-e45f363cabb0 | -12.8548 | -44.3625 | 2026-07-02 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 8e732cba-3b1c-3c59-9ee7-1685bfad7fa3 | -12.8741 | -44.3593 | 2026-07-02 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| a1845803-c77f-3ee7-b0f6-e81e0990fc7c | -12.8746 | -44.3357 | 2026-07-02 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 285.7 |
| 7c2dea56-5a75-31f8-9549-a1c0a03b645c | -12.8552 | -44.3389 | 2026-07-02 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 380.7 |
| 90187881-857b-3dbc-91df-8934a5fa72df | -10.9401 | -43.0355 | 2026-07-02 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9eca9741-9290-3147-9f3e-6395baba08ab | -12.8746 | -44.3357 | 2026-07-02 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 276.2 |
| e40212d9-3ccd-316b-b3d6-a26233398219 | -21.7823 | -56.2976 | 2026-07-02 05:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 21f5faa2-0c7e-35be-9ae3-715bfa73f018 | -12.8552 | -44.3389 | 2026-07-02 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 361.1 |
| f9432494-a835-3df0-9f8e-514ce69ad76f | -12.8741 | -44.3593 | 2026-07-02 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 1c60e0b2-52ac-3e71-9306-cb2932a05b8a | -12.8557 | -44.3154 | 2026-07-02 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| dec51af2-430c-3f36-8742-10f4ed30ca70 | -10.9397 | -43.0593 | 2026-07-02 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 4d9a6317-b5f4-3cf8-9057-2a9c142b707b | -12.8548 | -44.3625 | 2026-07-02 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 1e74782a-767c-3e9b-b277-072f0d4680c9 | -12.8741 | -44.3593 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| d70b870c-2446-376b-95ac-27f6ca6c4f7d | -10.9401 | -43.0355 | 2026-07-02 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 8ba4936c-44a3-3182-b8a6-0af77375dd14 | -12.8548 | -44.3625 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 144dc8ce-5414-34cd-889a-d9104ba18905 | -12.7755 | -44.4693 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 2a64d06a-7b5d-34a8-abe9-f2e0b2cd00b0 | -12.8557 | -44.3154 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 475945ba-f250-3f30-8de7-f2e6092ed56f | -12.7557 | -44.4959 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 298.4 |
| f487f614-5f50-3b7b-a77f-fdcbdac28699 | -12.8552 | -44.3389 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 379.6 |
| cd8e3b54-0bba-3478-917e-1fb84824b997 | -10.9397 | -43.0593 | 2026-07-02 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ec9c42ac-fdc1-389b-aff4-e1fba7f9ec3a | -12.7746 | -44.5162 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 96877879-f4e9-3b11-820f-ab91f65e5864 | -12.8746 | -44.3357 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 265.5 |
| 4a9ff3d6-4796-3c95-82c7-0fef26016720 | -12.7562 | -44.4724 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 416.3 |
| 6ed26a51-9f0b-393d-946e-8e74eba9c5bd | -12.7751 | -44.4927 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 0f848d21-3662-3bef-868b-55ff092ad252 | -21.7823 | -56.2976 | 2026-07-02 05:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 79.0 |
| dcc36469-6766-3692-be38-d9d70d48a516 | -12.7369 | -44.4756 | 2026-07-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| abf21c88-b351-3c52-9df0-5bff7571c991 | -10.9397 | -43.0593 | 2026-07-02 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b57eeb4b-0c5e-30e2-b9f6-c1470fa942ea | -12.8741 | -44.3593 | 2026-07-02 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 181.6 |
| d3bef0af-91de-3a82-867d-6fec973c07a2 | -12.8548 | -44.3625 | 2026-07-02 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| d75b484a-1abf-37b0-bd2c-cbb4526d716f | -12.8552 | -44.3389 | 2026-07-02 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 325.0 |
| 75c74aea-fbc0-3fc5-b873-16341ffe850b | -12.8746 | -44.3357 | 2026-07-02 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 268.8 |
| 05200190-1bfe-3e81-bb40-7bd0f03083cb | -12.8557 | -44.3154 | 2026-07-02 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| c287fc9e-e117-3b2a-9e89-308d33ebd1af | -21.7827 | -56.2762 | 2026-07-02 05:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 1ee1f108-8c49-3d41-8d11-06e8bf0eaf34 | -9.18836 | -58.05504 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3d99d85-398c-30a1-8e68-9b8d7d01239c | -12.50819 | -48.2752 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47710d1d-ff19-3a8a-a0aa-8cc211eb5641 | -10.69564 | -49.6139 | 2026-07-02 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2d6efa0-d782-3e81-b369-87a89c8e523c | -11.36342 | -55.428 | 2026-07-02 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 328f46da-614a-3ecd-8049-19809d8a3120 | -4.00732 | -48.06534 | 2026-07-02 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 29b8ed7c-61a6-337b-a827-210020f05260 | -4.00804 | -48.06043 | 2026-07-02 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0f68836b-96f1-3679-898f-fe3f74150ddd | -9.20778 | -61.90817 | 2026-07-02 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 561f4b91-6196-3474-9471-c838a97216b9 | -9.02772 | -59.53353 | 2026-07-02 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f32309bb-0a03-31fc-862f-0e584561c3cf | 0.89303 | -59.69281 | 2026-07-02 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50497f55-7d56-33ab-a1ff-7dc35a9a12f8 | -9.26102 | -57.86199 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86e6d374-7094-36eb-8850-9b46fd2e1291 | 1.98585 | -61.08765 | 2026-07-02 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f65afcd-3a1d-3d8c-8fb3-df1ea22f0d24 | -4.94792 | -48.24842 | 2026-07-02 05:23:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55ed7673-4fed-3cc4-8323-54bc6e228263 | -12.52001 | -48.28841 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77deb9d3-0c08-3e0d-973f-2c878aed1497 | -12.52065 | -48.2904 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| da7e6a7e-b05f-3bc0-b91d-7b4aaf387df0 | -4.35088 | -47.76305 | 2026-07-02 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7da3d83f-0d6b-32e0-85c8-c2989e24f90f | -9.17522 | -58.0699 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03bfe5f8-4643-338f-ab07-f58e84809fad | -9.1794 | -58.06633 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a32402d8-36d6-3555-8028-ea808d460d08 | -11.42436 | -56.06464 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 87224e8d-3076-3558-bcb7-5a83ace41b15 | -11.42125 | -56.05648 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| af28e960-5acc-3029-bdda-f184a26823ad | -9.60722 | -56.9334 | 2026-07-02 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 875cfc75-d18a-38f0-abce-5863022e8279 | -9.03578 | -61.3362 | 2026-07-02 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d195a852-7e98-3490-aed1-5335dc6131c8 | -11.43574 | -56.07395 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e51f8ddd-da4e-3462-9500-6a8da1f06e60 | -11.43212 | -56.0696 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 762fcbcf-d99a-3061-9870-b8e906976084 | -9.02435 | -59.533 | 2026-07-02 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ae8bae-0643-3a04-b420-cf280c422dec | -11.04904 | -56.9257 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 838a843a-cab2-3e77-86fa-da9efcce69ba | -11.35964 | -55.42327 | 2026-07-02 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e37952f9-805c-302b-93f0-4c835d61fc05 | -11.4192 | -56.07155 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 273a32ce-588e-382b-ab62-66121ea5a93d | -10.66712 | -54.52412 | 2026-07-02 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 723fd6b9-c96f-3e61-801d-f02351143c3d | -12.51373 | -48.28094 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9111b514-feb9-35e5-b1e1-4d75ecd09556 | -11.42074 | -56.06026 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 530c7b31-69bd-318d-be82-b04ce4047f51 | -3.51389 | -48.03952 | 2026-07-02 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 33ec0a3e-bfda-3ce5-8383-0a92d68d5102 | -11.41558 | -56.06713 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 246f31cb-f8aa-3b30-8e2b-11e2ecf0e996 | -9.59645 | -56.92699 | 2026-07-02 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 111e84ff-97e2-3f86-8594-2fc36fb7098c | -9.02043 | -59.53611 | 2026-07-02 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ce283fe-9516-3f7e-8d92-e2977d3892c0 | -3.5083 | -48.03345 | 2026-07-02 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5da58a04-5690-33cb-abdb-f173de5d2df3 | -9.08653 | -59.48677 | 2026-07-02 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
