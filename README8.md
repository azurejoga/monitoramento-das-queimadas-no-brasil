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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9ad3152-1488-3179-b567-b77fedc70ab6 | -4.58593 | -45.38256 | 2025-10-19 03:42:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 597741dd-6428-3ab2-88e6-8f04cfe74c72 | -9.21702 | -46.05704 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe1f08e7-92bf-3581-9807-a7dd0b2c819c | -4.30174 | -48.07035 | 2025-10-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66bc0159-fda6-3208-842a-62381323f468 | -6.79179 | -46.47572 | 2025-10-19 03:42:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e69f6665-dd6c-3979-9bc8-6c38a075e3db | -4.53532 | -44.01285 | 2025-10-19 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 328352cd-cebd-36c8-b2fb-780423834fdf | -6.44146 | -43.9211 | 2025-10-19 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 022c0dab-0345-35eb-9949-ccf537d42b62 | -4.2327 | -44.6863 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b1a3809-e0e3-3803-a9a3-31719209b832 | -5.93074 | -45.44918 | 2025-10-19 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5504ab7-d399-37e5-84e6-0ffcaf83ce40 | -4.85488 | -44.59357 | 2025-10-19 03:42:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5449a4e9-a681-3cb4-8b2f-40a04266b3b4 | -8.42721 | -44.1406 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f3ccc8f-6658-3373-8945-238771289c96 | -5.54441 | -46.52242 | 2025-10-19 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1d5e9b4-ae98-397f-8696-48ed0792953b | -9.21132 | -46.05609 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 853d46cd-b1cb-3275-8f0c-ae16a3041a5f | -7.18165 | -39.66887 | 2025-10-19 03:42:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 44a75c26-07e5-3745-a437-f397287687f8 | -4.83008 | -43.01381 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c96e067-d6bc-365c-8299-347ea3b3e2de | -5.40207 | -44.05922 | 2025-10-19 03:42:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62238ad3-5812-397e-915b-d8807349faf8 | -4.91889 | -45.98348 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73d18947-9e4f-31ff-a407-6280c72a80fd | -7.04438 | -43.94188 | 2025-10-19 03:42:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 783f39d9-e85b-3e7e-a208-b5808a3914ae | -5.90864 | -44.25071 | 2025-10-19 03:42:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d00f31b-d634-3983-8616-2d7a37f5dc99 | -5.70739 | -46.45566 | 2025-10-19 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ede340fe-8acc-3ae3-b05c-773d17ec7ab1 | -6.25159 | -42.32753 | 2025-10-19 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20ea6dc9-26b6-36b3-85ac-8da84550eed3 | -7.19893 | -42.19088 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 19f7aa78-12de-3884-8c10-2c22b74493de | -10.16338 | -42.2148 | 2025-10-19 03:42:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c09d9134-0031-30b3-90c9-11c58dbe7a84 | -7.19659 | -42.18458 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 9b6993e9-d1a0-34ff-b449-2e774df2f30f | -7.3164 | -42.47102 | 2025-10-19 03:42:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b92791ec-5091-3110-ab9c-18b38c8de743 | -7.1596 | -42.36858 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 71388437-388b-37be-a39b-8e9f1d0ff740 | -5.63467 | -44.81039 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1335fe8-69d7-30d0-9dd7-250cbc2b28bb | -5.29651 | -45.07987 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 250f7327-ebaa-3393-a268-bcfc322d08f8 | -5.30845 | -45.01274 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a0db35a-9e4f-38b1-9e58-0e6a7c0976d8 | -7.09235 | -42.20803 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3ce4b4bb-4fa7-3376-84d0-03110186338b | -8.57985 | -44.58537 | 2025-10-19 03:42:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4eb724a0-fc9a-3ead-af85-3f1a5344fccb | -4.9312 | -43.41173 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f7e8a56-ae63-3ebb-9371-61d9162445a6 | -5.58134 | -41.32005 | 2025-10-19 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8e9e7f48-61b7-39a7-b1bb-29b20c13c14a | -4.41427 | -43.96078 | 2025-10-19 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3202db22-1762-3755-8215-e47c63839fbd | -9.32884 | -46.11163 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b62aad9b-390c-35a8-a621-939a83ae205c | -8.25515 | -44.00771 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20fb8273-70c8-39c3-acd6-cdad2667278f | -8.43122 | -44.14744 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1464256d-4cc5-3bd0-85cb-51a9c270d4d3 | -8.61367 | -40.19764 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 43.3 |
| abfe383c-1d64-3f01-9923-0c6fad82b9a9 | -6.35726 | -44.25054 | 2025-10-19 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f79b712-4215-341f-9337-05cf547aa3de | -8.22118 | -43.96506 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19097919-c69d-3ec6-95ba-05676489c2ec | -8.24613 | -43.99991 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c85a5dba-0a70-30ce-9412-65746f4fc622 | -9.23435 | -46.06995 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8377cc92-dcf4-33ee-a502-cfc01190b7dc | -8.25168 | -43.99794 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43f8752c-a1d5-3179-9ae4-fb782dfe91bf | -6.09458 | -44.0221 | 2025-10-19 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8dadac5-6651-331c-a703-2b25e5c47969 | -8.20662 | -43.95945 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eb1b8ab-04a8-32ec-b5d7-d8d8594d9e2a | -7.15792 | -42.37693 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 52c0f3ec-9698-320c-a650-9c5f2f6efcb1 | -5.52964 | -46.9878 | 2025-10-19 03:42:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44be83a3-5ad0-3933-a3cb-992450de76a0 | -4.83959 | -43.0184 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a55bc558-c68a-3b52-92f6-586e34dd6ebe | -4.2479 | -40.34988 | 2025-10-19 03:42:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 656fbe85-f95f-3257-a28d-ae8237493495 | -5.46128 | -44.88974 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 350bae1e-5983-3b1c-8253-3fff68261de6 | -9.21389 | -46.05396 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92078cf0-99fd-3bc7-a02d-ef1a16a3a424 | -4.30281 | -48.06426 | 2025-10-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 80359313-97c2-3170-9dd5-5f40356614b9 | -7.12457 | -46.15778 | 2025-10-19 03:42:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb01d31b-b46c-3205-81f4-6beee0db6877 | -4.2377 | -44.69108 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb02f2c9-aae7-37ce-bd13-18d26818c58b | -8.25064 | -44.00381 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c3a0aff-bf60-3d79-bbc0-39dd15068200 | -5.33806 | -44.71706 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97abf103-06eb-3301-9cd3-be2ce8c70ebf | -7.15795 | -42.3783 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c1a42822-95a6-3cd9-b394-24eade4bf557 | -6.42079 | -43.91735 | 2025-10-19 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1e413e3-b7ac-31d8-b94f-61e8ac7ec3c4 | -6.0089 | -40.22457 | 2025-10-19 03:42:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aa42d62b-7194-31b4-b3dd-36f843c5d05a | -6.00114 | -44.18394 | 2025-10-19 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9e70f7f-d87d-3d17-bf92-d865754a2c9a | -4.59064 | -45.38237 | 2025-10-19 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a53ec6d-f28f-378c-a492-01edc68a76b2 | -7.36846 | -41.95514 | 2025-10-19 03:42:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 91ddf665-b88b-3cc9-8f4e-304d58344aa4 | -3.55163 | -46.4379 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8392b602-8f73-34d5-8558-a2c848a139df | -5.30225 | -45.08059 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8b9d3be4-20be-3ac6-94bc-ccde286d9fb4 | -7.18834 | -42.17834 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0d249aa8-5d74-34c9-a8bc-ae3371ff7881 | -7.18689 | -42.17914 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 52eb7ce0-3b47-37d1-9ee4-0fd80cef3ce7 | -5.06909 | -40.4761 | 2025-10-19 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4994107a-8280-3b22-aa61-8a7d545e8849 | -6.06074 | -44.51962 | 2025-10-19 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9aaa7b0e-e09e-3ca7-a4d0-fd355c2fa89d | -5.93145 | -45.44513 | 2025-10-19 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b29a6d5d-c358-3c1b-a5c0-d2664df8422d | -7.04897 | -43.94582 | 2025-10-19 03:42:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9af4edd5-8460-3bde-b4c0-2ea31ba9eb12 | -3.97017 | -47.57889 | 2025-10-19 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 654753b1-28d1-309f-ae07-dd913ab6348f | -8.44887 | -44.16603 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac9f73ee-f45f-3367-8037-02c67904830a | -4.44364 | -43.22613 | 2025-10-19 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84787e64-3c23-37e4-8c53-fd811b241fb2 | -6.55936 | -45.9475 | 2025-10-19 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69ceb9ec-839a-382c-80f9-4a0a980fd7c7 | -4.23205 | -44.69013 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8401c6a3-9196-36ab-991e-21c35e08d973 | -7.22926 | -41.17675 | 2025-10-19 03:42:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ab45c40a-4c9f-3a7c-96d6-7639502de63d | -8.44328 | -44.16799 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b947ba7c-7750-3351-8347-77f563569895 | -4.75734 | -45.42464 | 2025-10-19 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a63ebf02-9cc7-329e-b5af-01a520179804 | -5.13324 | -48.39196 | 2025-10-19 03:42:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7013d611-6b39-3750-857c-95e115e6b64f | -8.36312 | -46.20348 | 2025-10-19 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32719783-aa34-31bc-8624-51d773f671e0 | -7.1855 | -39.66947 | 2025-10-19 03:42:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 111fc716-84cb-3e1a-a44f-c176809ae111 | -6.75906 | -36.23655 | 2025-10-19 03:42:00 | NOAA-21 | SOSSÊGO | PARAÍBA | Brasil | 2516151 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f344d829-245a-3ea5-ae52-e050dc8a8801 | -8.61884 | -40.1965 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 25012086-3d53-3084-b646-e7eafe9681f6 | -4.95975 | -45.08961 | 2025-10-19 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b146606b-1529-32ed-975a-95989938bcf2 | -5.3086 | -45.07783 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9138a75e-04b5-3915-8c38-f730d4127282 | -4.58474 | -45.38151 | 2025-10-19 03:42:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbd667d8-48cd-345c-80e3-c9078e6c935f | -9.22447 | -46.06009 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f315cde3-bb93-3323-9bb3-c01b18a18075 | -8.55953 | -44.5787 | 2025-10-19 03:42:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c32b547-7265-3e5d-acda-b4f99b6553f3 | -4.58558 | -46.30314 | 2025-10-19 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fafb0d9-d06d-334d-8ca9-8075839a3fdb | -7.19867 | -42.19931 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ae311607-9395-306c-ad89-e17626e15955 | -5.17466 | -46.11219 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fee0b598-6fbc-399f-93ba-d2ae73f80de6 | -9.2227 | -46.05808 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23b7f3d9-d58e-3ed4-a8c8-fd09bf3afc35 | -8.24162 | -43.99601 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d80b3680-8ac0-37e6-a3f2-6405726ff97a | -4.85553 | -44.58989 | 2025-10-19 03:42:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65edd14f-5075-3ef2-bffb-51778ff971f8 | -4.30215 | -48.06431 | 2025-10-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3430fbfa-f22d-391a-bcaf-951f3de63106 | -8.4307 | -44.15035 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e47cb07b-8fb3-3302-8035-feaeeec9a607 | -7.41639 | -40.08042 | 2025-10-19 03:42:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cb050b79-61d8-32f9-9450-f3e927198e87 | -7.09335 | -42.20618 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6510a537-cfb1-306f-9c58-479d474597b8 | -7.58747 | -43.06911 | 2025-10-19 03:42:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ae499e7f-0f83-3a2b-b9af-24f2e3906b8b | -5.3396 | -44.71382 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b78bba65-02bd-3f9e-a705-800e3f8c0d0a | -5.54358 | -46.52714 | 2025-10-19 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README9.md)
