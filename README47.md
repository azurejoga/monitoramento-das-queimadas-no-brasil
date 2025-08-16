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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 197e9a85-4614-3c02-98c2-70dd2eda0df7 | -13.47047 | -43.7543 | 2025-08-16 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48c32bd4-f4dd-32b9-8fdf-2219a369c961 | -16.9383 | -49.3677 | 2025-08-16 04:34:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00fa9e87-d65f-36e5-956a-2e204255c5f6 | -11.35029 | -55.42726 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adb8e548-cf7b-37bb-adfd-db717bc74068 | -9.50956 | -60.53771 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5dcc50b7-98a6-3f46-8455-e28f81fc3f68 | -14.61582 | -47.92334 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 132ae1d4-4b33-334e-8e40-17cb7eb95924 | -10.95601 | -45.18386 | 2025-08-16 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3fc432b-08f8-3f06-b349-ee929006ec56 | -9.21171 | -59.66088 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 729e011a-1f73-33e5-9dff-7ef9d8ab9eb0 | -15.46326 | -48.54474 | 2025-08-16 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f53522bf-21fb-3702-a5ec-fa5c4e3d58ad | -14.87494 | -60.08544 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 327e931e-b15a-350f-968b-896d21a01eaf | -11.31194 | -55.2077 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d046e49e-59ec-3156-a542-ee827e53a70d | -12.46615 | -46.98509 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e30fd05d-63c4-3d1d-b961-c66045e3a762 | -9.16308 | -59.64281 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6780581a-5fa7-3312-958a-459efdcb35f3 | -16.2444 | -51.12565 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bcfd6c8-0f1d-369f-b2c8-fa841a1e7a1c | -9.19982 | -59.64475 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 502ac5d0-b364-37f0-bf05-70f863b617e2 | -12.49295 | -47.47842 | 2025-08-16 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b3c3053-c548-363d-ba33-bcfbe97be73a | -12.61489 | -45.22338 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a957a40-a152-3f1e-8f64-176be1a4a30d | -11.41709 | -44.68381 | 2025-08-16 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0edb3211-46b6-3f15-9050-ebf95fc927be | -10.05235 | -59.12069 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8934fe1-d847-3e26-b390-5e131a9c17cd | -9.21011 | -59.63726 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aea850fa-c298-3f45-ad04-5e86492589d8 | -17.87014 | -46.13865 | 2025-08-16 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fbaab99-a3c4-308b-bb01-0f3cbae68353 | -8.97696 | -60.54663 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ca326d8e-c63b-35a9-9e44-8ee384bacf3d | -14.86299 | -60.08727 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a71119e2-2593-3695-bdd3-e918051a69c1 | -14.73361 | -43.966 | 2025-08-16 04:34:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1d4af48a-0207-3bbc-976f-ffc629834996 | -14.95615 | -56.2416 | 2025-08-16 04:34:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b29128f-1c6a-3e12-8f64-a95f154157be | -15.8961 | -48.31968 | 2025-08-16 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bd68d20-269e-37e7-aed3-cfc915baf614 | -9.50245 | -60.5224 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c1ece26f-3c77-376d-a50d-54fa9c3a5a9a | -12.60398 | -46.91698 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a5b13d1-d12c-3025-a316-55056113ea7a | -15.65748 | -56.20656 | 2025-08-16 04:34:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06b38f34-171a-3744-871f-b8e3e97baa3c | -16.68134 | -41.34949 | 2025-08-16 04:34:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9563512d-8356-3cb3-9455-8156ad7aced3 | -14.59019 | -47.90847 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b076b333-7261-37ca-aa0c-735a4d804c1a | -14.87035 | -60.08763 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 46928691-0a95-3550-ae8a-5003bac9b4b5 | -8.99896 | -60.5346 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 767d3bbd-3d7a-3b67-a608-cf10f3830ca4 | -12.61274 | -46.95436 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffa6d04f-4583-3b6d-a4a7-d90c50250eea | -17.5077 | -44.88523 | 2025-08-16 04:34:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 295a4a1d-e07e-31e7-b502-4c16277b7c72 | -14.95345 | -56.23929 | 2025-08-16 04:34:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24250e6a-0246-39f2-88ba-f6ff3d78b800 | -13.64749 | -44.20389 | 2025-08-16 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcd206fd-4cc4-3490-a7ac-da37fdb5c29e | -12.53579 | -46.95941 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| abda8fa1-fc7e-30bc-b315-b8e45b2f41f1 | -12.5988 | -46.95223 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7d274e5-3e87-3f6f-b95b-bcda05bd5df0 | -13.12378 | -57.16624 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f69e033b-d9c9-3496-a4d5-a96abf9a8a25 | -9.50149 | -60.52746 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8de4410-3041-395c-a099-b67eccad5157 | -10.0459 | -59.12359 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e545dac-1f0a-38c0-b74b-cdf0fb581867 | -13.64824 | -46.93384 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a090636b-bc46-3dfe-bd9f-a7b2193fe3ca | -13.8749 | -45.5591 | 2025-08-16 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14f94e17-11a8-3bc4-b269-38d2c9a6ef3f | -13.57724 | -46.97652 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec3a6682-b459-3776-9829-acd890c2ce96 | -16.22714 | -51.12646 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31329795-523a-367c-9473-8932a1f22ab2 | -12.82295 | -46.02029 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dda46bf0-c380-3185-bd07-6a623942bc10 | -12.80143 | -45.96342 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc50105e-4ee0-36fc-8736-f6e8d1a68b2a | -8.89825 | -60.74284 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91ad4bde-3d24-3649-9b5c-b93c238a7782 | -9.20734 | -59.63762 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f3aeb59-bcdb-3c62-b829-ae8550ddecfb | -12.9999 | -56.87191 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1953144f-33ef-39f6-a76e-5d595c92aad6 | -13.99392 | -49.6431 | 2025-08-16 04:34:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6a1db9e-a598-334b-a0db-e9ccfe6e88e4 | -14.6124 | -47.92278 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2825b42-2265-38fc-85f8-4f8bb031bd29 | -12.53869 | -46.96386 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 06395d18-3fec-3931-9e78-0737dbe00c14 | -12.59238 | -46.92305 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a75bca9-4be7-370f-8c54-3278f3d4f917 | -12.30229 | -50.00777 | 2025-08-16 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d90ffc47-8495-3472-8f75-a499e9d307eb | -13.57377 | -46.97569 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d42c59d7-acb1-33f0-84a0-00ed1e9ff8c2 | -12.05039 | -45.76567 | 2025-08-16 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9300fb34-5715-321a-9292-b23c88cb0cee | -14.86479 | -60.08656 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1f313377-bd21-38aa-ac82-656671960353 | -14.95111 | -54.75625 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5439bc5e-6238-3300-96f4-93a7f9baa1b1 | -16.23833 | -51.12085 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2284dffe-fc6a-3318-a495-d222ff8b725e | -14.94998 | -54.73986 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0ed637e0-bf51-38e1-a3ee-6305e4edb1ed | -14.58906 | -47.91599 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 715e41d9-efdf-350a-a644-7a534bd6cb03 | -9.39133 | -60.54309 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1746553-37f6-38dc-808f-3626d97cc0dd | -9.16474 | -59.63411 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8d606041-6707-30e3-87da-7e0be959f45f | -13.61191 | -46.91146 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00fd5727-e18a-3421-a53b-fcc86f7a7f68 | -12.61447 | -46.94265 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1a2bc3f0-b89a-3943-bd18-2918c677076b | -12.54507 | -46.94493 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44a4e8ce-c443-36a0-9b0d-a0d3caae09c8 | -14.86221 | -60.09106 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 53eb50d6-7d58-38c4-a46a-ffa702d7e09c | -9.50531 | -60.52617 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d59c4181-b676-3f81-8c6c-7c32bf0e0bad | -11.91125 | -52.53276 | 2025-08-16 04:34:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78be72b0-833c-3293-bf8c-a251fbfbc055 | -12.53521 | -46.96332 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1b89a443-d0b1-3c97-aee4-f13dc927e28c | -12.49179 | -47.50901 | 2025-08-16 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b2fb70f-71cd-3125-904b-cce612d26fe3 | -14.86856 | -60.08835 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a9cb7473-73ee-3adc-ba91-6a01dfdfcf82 | -12.82952 | -46.00197 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad0e8dee-f0f3-3602-bbb7-8af6857d8536 | -11.3089 | -42.13118 | 2025-08-16 04:34:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 535e45cb-6460-346e-a1dd-1dc7cad1472c | -11.34593 | -55.42646 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16c33f6e-f07a-3381-943d-cea12349a457 | -14.9687 | -54.72589 | 2025-08-16 04:34:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40c990b2-5bd0-3183-9639-c1cfc430b897 | -12.53289 | -46.95494 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 656a9783-38c1-3a75-b99d-8bde94ccfb46 | -13.65175 | -46.93446 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05493c32-fce2-3009-9bbb-4cbf095e7e72 | -10.04097 | -59.11844 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4a77e41-d412-3e58-962f-18eeb576e69e | -14.58224 | -47.91484 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5da8f497-8d30-3c3c-af45-35565fe4b4e9 | -13.45613 | -47.06366 | 2025-08-16 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93931e0b-3748-3e3d-96f7-b872b61d9012 | -12.99907 | -56.86376 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65124500-4567-3a4c-98ca-0251951a7948 | -13.62187 | -46.91724 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8015323-0551-31ea-bf22-7d0475268486 | -13.12121 | -57.12733 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a82a270e-9a5e-374b-bea8-93bf877ecbab | -8.96299 | -61.67952 | 2025-08-16 04:34:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 33751226-5c06-3314-93f0-2354396f8fd5 | -12.54158 | -46.96832 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be4d837b-f779-3293-a1af-9597269981e1 | -11.89853 | -43.43864 | 2025-08-16 04:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19a29ae5-c1b3-3cd3-8f93-b47ad0c86d27 | -9.50758 | -60.54783 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9699b247-fef9-3e5d-adc2-4034f7afcc9e | -13.58601 | -46.9656 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d60690f-fd76-332e-b721-a90af54906f0 | -12.57 | -46.94503 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d2073892-28b3-32e7-a022-e0d076f7645d | -17.61601 | -46.7011 | 2025-08-16 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c4c69c1-359c-346f-a1d2-23542484236a | -12.40751 | -47.78883 | 2025-08-16 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c95fa75-0602-3d4d-9e5a-48c45ac5c206 | -14.93839 | -54.75919 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f6d82991-4eac-3cf6-a3a7-2ff1e7e7362c | -12.53927 | -46.95997 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 62eecb9f-137b-3d38-aba6-6912384d9013 | -12.55491 | -46.97439 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ab6a9a8b-8c74-3d57-b13a-f6c4633cde3a | -12.59121 | -46.93106 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f04388b4-8691-3280-b87d-635d507c9574 | -16.23774 | -51.12452 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5521f816-98c2-3806-af52-88f681935c0e | -16.23557 | -51.1167 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fcefaccd-5bf8-31cc-8914-af0333a39821 | -13.47955 | -61.00185 | 2025-08-16 04:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README48.md)
