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
| e61fee62-9c2c-3fa4-96ce-6b1a3588e8a0 | -11.96473 | -56.81164 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b810fe60-accf-3011-a6eb-40f93a9fdcfc | -12.44858 | -54.45311 | 2026-05-26 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18194544-0633-301a-9e80-e90a0897f2f8 | -14.16359 | -45.44511 | 2026-05-26 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efc3eb62-cdab-32f2-9819-f0fa4e140095 | -20.19541 | -49.56646 | 2026-05-26 04:32:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a7027d87-ab02-3e23-989a-d0b7b6f0e57d | -14.16768 | -45.44163 | 2026-05-26 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4644941a-15a3-312e-8e47-bc2a655690eb | -13.64277 | -55.45434 | 2026-05-26 04:32:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2eba8e3-9e08-3dd7-89f2-62222c3ede49 | -12.05338 | -57.42282 | 2026-05-26 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a8e5c15-6f14-3868-92a7-5fea9ce53cff | -11.79159 | -57.00841 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22bda37d-9a09-3559-800c-3501eb2cf163 | -11.9637 | -56.80891 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49d7dd50-7e29-3738-85c4-4a9bcd950e1a | -17.24432 | -48.29871 | 2026-05-26 04:32:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 839451dd-e5f9-3e63-87c4-9e592d576e9c | -17.95344 | -54.46403 | 2026-05-26 04:32:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 471b3284-f7e2-38c9-9365-1cdeca460817 | -13.27787 | -48.86287 | 2026-05-26 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6d790c9-cc1e-361f-8eb0-b3ab6be803f7 | -12.44941 | -54.44864 | 2026-05-26 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35cde722-e640-3416-adc9-07a832cd38a8 | -11.96303 | -56.81235 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c59ea2c5-d322-3947-905f-4212e995393e | -12.1688 | -56.45174 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c841e0a-f41c-3982-bfa3-9c5ea1854249 | -11.73621 | -54.80646 | 2026-05-26 04:32:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88183b73-1a06-393f-a5a9-6a3a84e234ce | -13.58537 | -47.53534 | 2026-05-26 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53ce578c-e576-3997-8124-8b4181d10351 | -11.73528 | -54.8115 | 2026-05-26 04:32:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af4b3863-7f1f-3ae3-a2f2-654152a8df58 | -20.19211 | -49.56594 | 2026-05-26 04:32:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b090dc28-a98d-35a2-8337-872a6339c515 | -14.25134 | -45.82396 | 2026-05-26 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6e3f901-c1b3-3b62-962f-093d5e80a43a | -12.46205 | -54.45569 | 2026-05-26 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 747f3277-7daa-3154-862b-06ae8f4f8ef2 | -12.45839 | -54.45033 | 2026-05-26 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ec636fd-7a6a-33bb-85ec-cad5f567dd43 | -14.24731 | -45.82727 | 2026-05-26 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b61b034-f19e-336f-abc9-4a412628ae5b | -18.7699 | -48.04006 | 2026-05-26 04:32:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c46c6fd6-6ea2-3f2d-abb3-19abf49fe3c2 | -11.97132 | -56.80584 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 031082c8-71f2-35f7-9880-bda6dd2e1431 | -14.24673 | -45.83116 | 2026-05-26 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 995642ea-0b8d-3828-8bc2-48457c90e613 | -17.24101 | -48.29815 | 2026-05-26 04:32:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e00f62b-7a3a-3fc0-bab6-79f56146f489 | -11.55032 | -56.93442 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aacba080-2a97-3cdd-b883-13de8f2cb09e | -18.08401 | -46.87409 | 2026-05-26 04:32:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fe1a529-496b-3727-8ff4-543c59f7e81d | -13.65687 | -55.29959 | 2026-05-26 04:32:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14165510-6891-3579-9181-70eba52b27c8 | -14.15131 | -45.3569 | 2026-05-26 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b215327-6ea8-369d-86aa-b7619fbd98e7 | -11.91111 | -57.03606 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba3ab50c-8dac-3771-97ff-70a8458fd2df | -12.05304 | -57.42319 | 2026-05-26 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e76334c-b5ff-38d7-be0a-44bae9ef71ae | -13.65315 | -55.29367 | 2026-05-26 04:32:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e89e970-1f06-3a86-8e0e-43ef5a05a157 | -11.91716 | -57.03358 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dd67906-e69e-38bf-977c-56a474829136 | -12.05408 | -57.41917 | 2026-05-26 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ae11c4e-9f9d-3a14-b663-93301c03ce09 | -14.15834 | -45.43199 | 2026-05-26 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8f77bc3-6949-3795-8b04-edbab7f59f22 | -11.74086 | -54.80741 | 2026-05-26 04:32:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da807f9c-2406-3978-8bac-8c5ca57c7cb9 | -11.91381 | -57.03375 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8b63f4a-6dc9-3c5f-8ebb-28b68eef1563 | -12.17456 | -56.44957 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c10d038-6bed-3cca-96d3-c31031211fb6 | -13.65916 | -55.3006 | 2026-05-26 04:32:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebdd5b38-27d2-3df9-b25a-f6ecd6320515 | -11.96966 | -56.80655 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8138cee6-0d77-3b7c-9d5c-5f027e3ba1ec | -17.95273 | -54.4679 | 2026-05-26 04:32:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65d90c01-2394-38ef-8c00-b32aa943d9da | -14.04018 | -46.34486 | 2026-05-26 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05982d34-4c26-3b9e-b004-014020d00028 | -11.91313 | -57.03721 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66e091a4-d08c-33d5-94ee-842eb37f0db1 | -16.43435 | -57.27144 | 2026-05-26 04:32:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c17d649d-4a0c-3969-84cb-83afab061f56 | -18.08343 | -46.87801 | 2026-05-26 04:32:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 783acf36-d058-3faf-8bdd-e6e630b6bbf3 | -11.54965 | -56.93792 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a229d13d-7587-3316-b8d3-34b6719439f9 | -13.65453 | -55.29963 | 2026-05-26 04:32:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bbf1362-1710-3397-a151-cddea2f6d23e | -12.45757 | -54.45482 | 2026-05-26 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89f0ee59-ebee-3ce0-9b3f-55a2d6064cc4 | -13.28122 | -48.86344 | 2026-05-26 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9ae68ed-7ed3-3f90-9cfd-026693a9f6fb | -11.96602 | -56.80477 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abab68db-5ec0-3f75-85c7-8d8d5d624c97 | -14.03962 | -46.34861 | 2026-05-26 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 593c0540-bec3-3695-bd6d-0557fdc347ae | -12.46122 | -54.4602 | 2026-05-26 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 281610d6-ec9c-3d78-8bcb-982a5d746cfc | -20.196 | -49.56286 | 2026-05-26 04:32:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6a613700-a5f8-3104-8f01-f255c1357c60 | -14.24789 | -45.82339 | 2026-05-26 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 940f20ea-365c-3f99-8e36-bf7fb78fa322 | -11.9165 | -57.03704 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04c8da6f-18c2-3cd4-b1d7-922546859ef4 | -11.96438 | -56.80548 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3137a55-426b-3dc0-b334-cedbea9b0570 | -11.97067 | -56.80927 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9363a50-ffd3-3950-a32a-0d5fff0081e1 | -17.59115 | -46.56551 | 2026-05-26 04:32:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7c96d85-1e8b-38cb-b255-b66f65d01538 | -18.77381 | -48.03692 | 2026-05-26 04:32:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c53cc2ea-6bdc-3e88-b953-37bfbbb2ae9c | -12.44775 | -54.45761 | 2026-05-26 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72b6f690-92c8-3f29-93d2-3002e20fb7af | -14.03679 | -46.34432 | 2026-05-26 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3915044-4862-3051-8823-0ad823e4d2f5 | -11.96538 | -56.8082 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79fa491a-5837-3e4e-bb3c-2c30a84f8510 | -11.57214 | -56.34039 | 2026-05-26 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aed64543-7df6-3269-93bb-745bd05357a5 | -14.04244 | -46.35287 | 2026-05-26 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7fbfab7-4ccc-3af1-ad2a-caf3c358cec3 | -11.969 | -56.80996 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 924e4b8c-2814-37a8-a6f3-e9a144306f0a | -13.65223 | -55.29863 | 2026-05-26 04:32:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 347ff1d8-f7b3-34fa-b542-4418d1913cf8 | -11.91583 | -57.04055 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 498cf1c8-5dbb-37c1-8b04-9e4535ff2e47 | -11.91243 | -57.04071 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4f90339-0031-3b10-bc44-4934748d2aa5 | -17.84543 | -50.78695 | 2026-05-26 04:32:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f308b13-e94a-32a5-9295-a876480fc20c | -12.05377 | -57.41958 | 2026-05-26 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b790f3a-7134-3766-a071-1b71e3eb3098 | -15.66205 | -43.28862 | 2026-05-26 04:32:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7cad9ff2-6024-3aab-92a0-293290164371 | -14.03905 | -46.35234 | 2026-05-26 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd1a3f8b-856e-385a-aa8f-34df93002736 | -21.14993 | -42.99629 | 2026-05-26 04:32:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1011e79a-35c3-3dcc-ac72-c7e9ea2ad78f | -11.97002 | -56.81269 | 2026-05-26 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee3dbe4a-0bce-35b8-b6f3-c6ef3e9250fe | -16.43323 | -57.27121 | 2026-05-26 04:32:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a1042a8d-4bb3-325d-a01d-93e3227a8f99 | -11.91177 | -57.03259 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9140e10f-e342-3553-a729-c31f7768fcfa | -21.5511 | -47.04966 | 2026-05-26 04:34:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30c0f3fe-0674-33fd-852d-6e91679251ef | -21.30086 | -48.58672 | 2026-05-26 04:34:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a5f5a1a6-4506-3c46-8627-ef0cfe683342 | -21.32081 | -47.07173 | 2026-05-26 04:34:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0345f677-56ae-3aec-ab93-9fbd1fd39bf6 | -20.27913 | -50.72491 | 2026-05-26 04:34:00 | NOAA-20 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 71dc5b96-f712-33a0-a299-dc811087c9bc | -21.30421 | -48.58731 | 2026-05-26 04:34:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 022f9252-cd28-33b9-81fb-ab6c81d9cb4b | -21.95092 | -57.59449 | 2026-05-26 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4256b8f-5440-30db-b5ce-4c8494aed66f | -21.26606 | -49.47303 | 2026-05-26 04:34:00 | NOAA-20 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2728e117-1a43-3d6e-99bd-131a37a7bc79 | -21.55462 | -47.0502 | 2026-05-26 04:34:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bec4240e-9026-35a0-82b3-4867d2d18376 | -21.52855 | -47.15731 | 2026-05-26 04:34:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94767107-5332-3777-8e55-41189c64354f | -19.76277 | -54.08174 | 2026-05-26 04:34:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 075b0589-efc4-3820-9259-056e28eb8835 | -19.75891 | -54.08087 | 2026-05-26 04:34:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9ad5fd8-704f-3d8f-856b-06ef27102bb9 | -20.27578 | -50.72429 | 2026-05-26 04:34:00 | NOAA-20 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 36b6a707-1ec1-33e2-8708-d6ed5acef6a8 | -21.49436 | -48.04005 | 2026-05-26 04:34:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e87075a-5e0c-37aa-8336-b824c7661b8d | -21.3214 | -47.06757 | 2026-05-26 04:34:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0861bf44-7b4f-3b8d-a97d-94c13fe015e2 | -21.5505 | -47.05385 | 2026-05-26 04:34:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1407765b-6118-3a78-bd2a-e67bc9709c9f | -21.55402 | -47.05442 | 2026-05-26 04:34:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6d298a4-bcc6-3d65-9012-a5eb379de033 | -21.26548 | -49.47672 | 2026-05-26 04:34:00 | NOAA-20 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9db4776b-bbff-37c6-ac48-552878b7fd71 | -21.55754 | -47.05497 | 2026-05-26 04:34:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cd5e20e-376b-35d6-80a8-41441f2a825c | -23.3373 | -52.29858 | 2026-05-26 04:34:00 | NOAA-20 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 80a1fd82-a71a-323e-8a01-d23ad0800fbf | -20.91775 | -46.78724 | 2026-05-26 04:34:00 | NOAA-20 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 45815ed9-bacb-32a4-8b84-40ed210a8a35 | -21.33821 | -48.61251 | 2026-05-26 04:34:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5bbfcb4a-d420-3b53-8b76-e05cacdf0453 | -19.76372 | -54.07653 | 2026-05-26 04:34:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README11.md)
