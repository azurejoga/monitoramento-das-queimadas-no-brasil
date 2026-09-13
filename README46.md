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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14ca8987-349b-357a-8a8a-017bed1fee00 | -4.58743 | -55.94487 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63b4642f-ab2b-37d7-bd92-b5d2286cadf9 | -3.91407 | -55.73544 | 2026-09-13 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c969c79-5295-3afa-8228-2e6c346a9b4e | -6.59516 | -58.84207 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a00f13c1-9d87-3a95-8d49-229b16eb7221 | -5.76063 | -45.09502 | 2026-09-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90412676-cb89-391c-bc66-32418274d1fc | -6.5662 | -58.97466 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a59d2948-4d4e-3097-82bd-8911aece07ad | -1.26127 | -60.31787 | 2026-09-13 05:10:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 651cf9ef-6a9d-3eb9-adef-06c6d4ba63a6 | -5.49176 | -57.23365 | 2026-09-13 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f121dc3-6217-3569-928c-12b76293fd98 | -2.67413 | -57.50485 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45143fe7-6e3e-33c3-a505-801a56608d50 | -6.3008 | -59.95223 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3a5bb90-a377-33ca-b9b3-44bf094b76b1 | -3.79079 | -48.94044 | 2026-09-13 05:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a642b1cf-10c2-384c-8acd-84174226fc98 | -7.87462 | -54.70729 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cdab650-00b4-306d-81e4-bf8829279ea6 | -6.85 | -47.4316 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cba379be-9f46-395d-8785-ccaa82f8ee3f | -6.2249 | -51.69656 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7684f8d6-5807-3cb8-a598-226e4221cdd3 | -1.46225 | -52.96206 | 2026-09-13 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 46f157fa-a1ce-3a2a-a3f4-3f293b64a249 | -6.08045 | -51.7548 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6373c62e-21ff-38df-a1f7-4054db8cfaa4 | -2.68315 | -57.53781 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 448121e2-58ac-3dd8-b939-ff17755bc009 | -1.18418 | -55.65904 | 2026-09-13 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1fb9e237-c753-3b70-896a-0263443c3fe1 | -5.78496 | -53.81803 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1203befd-46cb-3634-b4e4-bb160f95abec | -3.98506 | -51.08648 | 2026-09-13 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c50e131-80fa-3285-9f3b-0d25fddc48c3 | -6.13304 | -57.71181 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 757654a7-b116-3edb-877c-c1f9fb28faed | -6.67463 | -58.71122 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85f10510-05be-3310-b619-a0ca08ceae49 | -4.13501 | -56.3316 | 2026-09-13 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57a19495-fea3-3c2c-a698-1120cacbbb61 | -6.51269 | -47.59883 | 2026-09-13 05:10:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a3f07d4-b35f-3b0c-9ddb-d4dde3ab7b0b | -2.7806 | -51.36961 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80dc46a7-fa83-30d3-8040-81f298c7cace | -5.96115 | -47.20819 | 2026-09-13 05:10:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa4c3c8d-bd06-3fb8-9d1e-bf3287894926 | -6.28423 | -59.93528 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b93fad02-9096-3db5-89b9-7238331152f4 | -2.95859 | -50.38252 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebf0f287-85f9-3c63-a348-af66d78644a2 | -2.95841 | -50.40963 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79b605ed-1841-35f1-b065-4b1165260246 | -6.85764 | -47.42772 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 15c5f6f7-a094-30b7-8200-d2abb5b53506 | -3.0947 | -59.1377 | 2026-09-13 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a5aa80f-ff7f-3546-9373-e4b1b1864ea6 | -2.93615 | -50.39579 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b66a0626-f4f6-3eca-a268-68e79a59bf43 | -8.11735 | -54.78872 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a697c94-85f0-3c2f-b76c-caa30fdcd026 | -7.52781 | -47.33774 | 2026-09-13 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0bdb3901-1b41-36e0-89e6-df71e457f672 | -3.87214 | -51.19363 | 2026-09-13 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72d79647-7087-339d-8678-76dc528ae912 | -6.69858 | -59.13322 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb0e1060-8eb8-36af-ab83-10cc3eebb2fa | -6.02347 | -59.93951 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7f0388bd-d035-3ee6-99aa-eeaa7f6f7509 | -2.96608 | -50.40264 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 873711c4-c159-31da-a97e-ba26eb2950a1 | -2.96399 | -50.40002 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7aec8d76-7601-3149-bcde-00c368b57689 | -6.06633 | -57.86427 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab6ca0d0-8db6-33ca-ab28-b20157d7b0c0 | -4.45307 | -50.16248 | 2026-09-13 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec6176d6-9771-38b7-9201-3ac760f9804a | -6.4377 | -58.14607 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9ad6c52-f700-3589-ae80-08d7a2bacf44 | -6.8165 | -58.99725 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbbdf26d-627f-3fe3-a9ac-9356d63c77ab | -2.71182 | -57.61318 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2683f6e9-cfc6-3248-8468-a2a84119ac07 | -8.0304 | -54.85066 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 405cac79-32a9-36c1-89a4-0a1c70739d25 | -6.96317 | -59.75008 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 779f478c-417d-340a-a54b-a25bc2574ddc | -6.06632 | -57.73503 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8a51dd4-2e95-3707-ab27-f4fa41beb86d | -3.87286 | -51.18892 | 2026-09-13 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51608abb-9908-32f2-a820-725b977140ba | -6.59832 | -58.86744 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a9b1ebf-9282-3bb6-b6dc-51d74ba40c30 | -3.2153 | -56.83815 | 2026-09-13 05:10:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15ed51d9-8b82-341c-a1cd-50f09fdc485f | -3.04734 | -51.27245 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d877815-6764-3450-9c36-675414887967 | -8.53532 | -54.71371 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4756b44a-bd3a-3bd4-bacc-9dbbcb1c4ae2 | -8.04633 | -54.84476 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 127cd3a9-d696-3141-8926-404e35f3ca17 | -4.57163 | -54.90556 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 50ddf65e-fa1f-330a-98c6-0915efc94c77 | -8.3834 | -47.53551 | 2026-09-13 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3dfb0b2b-2b30-3dd3-aebf-07fa3d50f5d2 | -7.37019 | -45.37502 | 2026-09-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ede0714c-f389-3a49-b723-eb6840a86d6d | -6.87363 | -47.42644 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 019ab31d-8ea3-35b0-bc06-060fb9238608 | -3.87464 | -52.27562 | 2026-09-13 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a5a4301-d188-3955-86cf-82849d65a33c | -8.20997 | -47.86948 | 2026-09-13 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67a28f9e-d421-3bdd-aedb-61c1ea8f9651 | -8.58205 | -54.56884 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8528c01b-c50e-3496-99dd-0843c2621ca1 | -3.75253 | -61.20168 | 2026-09-13 05:10:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8846c26e-5fd0-3a8f-9fd1-908c578d449e | -4.01994 | -52.08198 | 2026-09-13 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2334b03f-5d76-32ec-92a9-55127bd89397 | -6.62093 | -58.86289 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f571491-1aed-31ad-8f60-cfc2c1914c23 | -6.22818 | -51.68993 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c4beecd-16e1-3f6e-9626-3c89657678ee | -8.11678 | -54.79238 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13ae6baf-4655-35c1-bc28-17998d78f7b3 | -6.10743 | -57.63253 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 14dead10-5c39-3884-b1dd-10877ded8b5c | -7.87293 | -54.71826 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dea27743-22cf-3755-96a7-e1098152b4bf | -7.01845 | -44.63291 | 2026-09-13 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 719cc031-7ea2-3e99-9ed9-f9c9365706bf | -5.48838 | -57.23312 | 2026-09-13 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ef540a1-8ca2-3fc8-b13f-c2be221412b0 | -6.22563 | -51.6918 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9a76599-236b-32a1-a6da-999037471163 | -3.33441 | -42.30189 | 2026-09-13 05:10:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 59afd14b-18f6-3b7d-a185-f9783bbbe569 | -7.38443 | -45.35939 | 2026-09-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d581ad3-5442-3f5b-b232-997d6dc3298c | -7.46911 | -46.1437 | 2026-09-13 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf6f8fea-79ff-3b3a-975c-dbb575716100 | -2.96723 | -50.39495 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5278f810-5835-35b2-9911-3bcc7e8e44da | -2.95921 | -50.40451 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 742c11b8-26a1-37d2-aee6-1d9f570b6639 | -6.79904 | -58.79153 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca8367f-8459-36a0-8c69-035423c6ca71 | -6.67111 | -58.71064 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 732fade5-344c-3cff-ba8b-6e507e87bd9f | -4.13557 | -56.32811 | 2026-09-13 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c5eb826-21d7-3c6c-8a0f-b27793f6daf7 | -2.96717 | -50.40573 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07b9e2fd-5215-3140-8858-213c6d54bec6 | -6.72019 | -50.95814 | 2026-09-13 05:10:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39bba649-7fd5-39fc-9495-ff086a939420 | -6.07974 | -51.75951 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 345fae78-ef83-3ab4-a3b0-ebd9755cc888 | -8.03507 | -54.85044 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc3c66c-c17f-3a2a-9855-b51d78ec28c4 | -6.36426 | -57.86629 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d44188b2-299c-3ef6-b900-2b212752d091 | -8.04239 | -54.84787 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d43cd2cd-3524-335a-860a-c9fe05daed87 | -2.96602 | -50.38716 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c20eabad-7721-39d4-a4de-d95470cefca3 | -6.10892 | -57.66646 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 096091a6-4a35-350b-ab47-5ee4e20833a2 | -5.27946 | -56.03661 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cdbb8d2e-3f20-39fb-b9e1-514c433eb66b | -8.03846 | -54.85096 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63619c6e-37fa-3aaa-8a2f-4e7b442a62d7 | -2.61424 | -54.7614 | 2026-09-13 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fb71d95-c7b4-3bd5-8bdd-049521918b22 | -6.43708 | -58.14985 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6964b726-100d-3529-ad6e-76c1817f2ac4 | -3.59832 | -59.0713 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2cf748d7-ccc2-32fc-b595-dc30a5ed080b | -7.13896 | -43.75589 | 2026-09-13 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b22d0c53-c72c-34f9-adfc-2581cf05b163 | -8.04128 | -54.85511 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84f9b437-a4f2-3b85-9168-76c51a1f61b9 | -7.86953 | -54.69522 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f420089-8b6f-350f-bd69-5080708275c3 | -6.81294 | -58.99666 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9525bc18-a1af-35eb-9c17-0108ce6a807d | -6.10329 | -57.65809 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ebe6d49-e6e4-3175-8e6f-af21e25092de | -4.52936 | -54.95947 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53119060-8dac-3e18-8928-a2b2243855b6 | -6.30683 | -59.96274 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48efecd4-6781-3624-9ee2-08e62d596713 | -6.25465 | -57.78449 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 230f8637-87dd-311d-9297-23b4d12b7314 | -2.70981 | -54.52153 | 2026-09-13 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fe363bb-0478-3d2b-87da-151e754cfcc2 | -6.98686 | -59.76767 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README47.md)
