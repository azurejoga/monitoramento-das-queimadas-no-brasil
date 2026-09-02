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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a418fa58-af37-3512-9c72-9d6ad5eca43a | -6.84432 | -41.68251 | 2026-09-02 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8687d672-6016-356f-9249-de6e5e8f17b6 | -6.047 | -53.83876 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9cc0107-f2c2-3cd9-b111-7149fb9a3364 | -3.18674 | -48.02289 | 2026-09-02 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d5259de-a00b-38b6-9b21-0320cbd8bab5 | -6.93445 | -45.71527 | 2026-09-02 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41d7f6cb-a2fc-32d4-bfec-c1da315ceb8b | -3.85436 | -44.05682 | 2026-09-02 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 215f2bb7-6efa-37ed-8d84-d3b00b341743 | -4.49663 | -45.904 | 2026-09-02 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 482a557d-2da5-3c3c-8466-8bb96f98637a | -3.44893 | -47.27294 | 2026-09-02 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2afee724-9cc3-3e8e-b81e-c3c7229a39cf | -6.98395 | -35.13085 | 2026-09-02 04:19:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 93544836-e73d-3057-a70e-02ebbf48f6c4 | -7.37506 | -45.05222 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b29e4bfa-4508-3730-90b7-b66572cc6616 | -6.77417 | -41.17657 | 2026-09-02 04:19:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9316a60-8089-3737-956a-444370129076 | -7.6046 | -47.28949 | 2026-09-02 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12679013-e1f4-3f6e-8ec9-4a010c787fd0 | -4.12804 | -43.25681 | 2026-09-02 04:19:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97097d91-6646-36db-8e95-8571abd88f33 | -7.65008 | -45.88004 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e48cfe03-5e98-3449-8df6-5d14edc472e4 | -4.11977 | -51.0326 | 2026-09-02 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0a212e6e-11da-384e-af79-4f67a4a792af | -5.75577 | -53.40028 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05fae173-cf2f-308c-a9d5-7057153b817d | -4.37245 | -47.77764 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f93a387-1983-3b18-b043-8c18cbc3a3aa | -5.97855 | -53.57983 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be5b93fb-f0b7-3e6c-9f3c-fcbba52fdce1 | -6.61511 | -47.6381 | 2026-09-02 04:19:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c868c7ed-d350-34b1-95e8-8d376087f9ab | -5.63339 | -49.95286 | 2026-09-02 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f5d9e98-6847-34c8-b9eb-3d9d68279d4b | -3.23872 | -47.24973 | 2026-09-02 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 6df33071-b832-3d4d-91ef-b8cfcbacb122 | -5.9328 | -50.21132 | 2026-09-02 04:19:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47016c55-3ca1-36e9-9634-5938fdce0d3c | -4.96452 | -55.8546 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e971f244-d23c-3523-8e17-4e751eb90d4c | -6.10032 | -44.13169 | 2026-09-02 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d065d20d-83e2-3a41-8e54-6f701cd08e46 | -4.36148 | -47.77593 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4295837c-08e7-3621-ac8f-5631147757d2 | -5.4576 | -42.66176 | 2026-09-02 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| adb18c2a-2b84-3a5a-9a1c-70a5f5140a5b | -5.80228 | -52.05145 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a24567c-c497-356e-b8ce-7fa5d814a21b | -5.97117 | -53.59177 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3962bd78-cd46-3e62-a7ec-1e75a8519e38 | -6.42888 | -46.27045 | 2026-09-02 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bac7bc50-398f-3553-9540-401a76a8b3e7 | -6.09807 | -47.38014 | 2026-09-02 04:19:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40a0837f-e9d3-3395-afb9-7b24219df8d1 | -4.36948 | -47.77281 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 661c53b3-bec2-3e76-846b-df88dad9e995 | -7.17398 | -44.06952 | 2026-09-02 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 044e7694-6800-3cbb-bce6-31900eea3697 | -5.86327 | -51.71189 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b09c7f5-f077-3a04-abff-8ec793774327 | -6.12112 | -53.54082 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb939f70-69d6-3fdc-b8d9-f46c59bda817 | -4.2644 | -55.15759 | 2026-09-02 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 622c8c3d-9433-3ea9-b6d8-3309c1bb992a | -5.97801 | -53.583 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 52a8c144-a1a8-39f0-83ff-2a719ecbda10 | -3.23939 | -47.24558 | 2026-09-02 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 9ca30351-ef37-35de-8a65-2ca79f8cba4b | -6.20052 | -53.48147 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 311de5dd-08e3-3486-83d1-2b2fd55de715 | -5.24642 | -55.90367 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8038065d-aef6-3d15-b011-02a6396d2e15 | -5.73542 | -43.278 | 2026-09-02 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1b67056-3e29-3b12-8429-d39b2842f530 | -6.31518 | -54.75393 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e5fdfc7-4f27-369e-ae3c-7de350d66d17 | -7.90603 | -44.2158 | 2026-09-02 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43258733-65bf-358c-a869-6b823cae2a15 | -7.66558 | -45.86815 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdafff53-499e-3277-bd83-2eefbbe43244 | -6.23436 | -43.83743 | 2026-09-02 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 177db96c-24d0-3cf5-b205-862f50c45fab | -2.1627 | -47.48212 | 2026-09-02 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d9c24d4-46e2-394e-b183-0e978edf1d74 | -7.17731 | -44.07003 | 2026-09-02 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc22effc-5ccf-3a72-af72-5747aef8e4f3 | -6.20328 | -53.47665 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 27b5c630-2202-3af1-ba04-5dfabe24f702 | -3.85176 | -52.03769 | 2026-09-02 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfa9bf94-ef07-3354-a28d-c8804bbb4fa9 | -3.24299 | -47.24614 | 2026-09-02 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| b220faab-5f76-310b-89e7-fd9256f3e5ca | -6.07738 | -53.66737 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71eed651-44be-398f-a8d1-372d33ba9c87 | -7.66171 | -45.87112 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c7646ba-e12a-32aa-9026-2967345028d3 | -7.15567 | -46.84945 | 2026-09-02 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d37a4fa9-a6c7-3ccd-9c2b-23299f94e533 | -7.65893 | -45.8671 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73b97a5f-e2c7-33b5-8f0e-2de9d935968b | -6.04855 | -53.835 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfab8998-8aed-3b3b-b892-49bfd1b50a7f | -6.44059 | -41.52912 | 2026-09-02 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9bfd4c18-86ad-37b4-a630-9cd52a7dcd46 | -6.12059 | -53.54384 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d85184c9-d957-343e-a673-e08db52e0ae7 | -6.34739 | -44.09552 | 2026-09-02 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb8595cc-c4b7-343d-ab4d-cd7bf6f0ca4a | -7.22196 | -42.74401 | 2026-09-02 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 351cc677-7bfd-3171-a769-7033e96b2519 | -1.5042 | -54.96138 | 2026-09-02 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d6a34b2-d41b-35de-a466-25594a598b29 | -6.16558 | -52.63586 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab2f00c5-4613-3538-943f-858a96a4fd48 | -6.07796 | -53.66407 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 228397c7-2e97-325f-81c7-8f1f13cc14e9 | -8.4671 | -54.7035 | 2026-09-02 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 190.5 |
| 44de5375-2cf8-335d-abc5-167dfaeb9343 | -4.3588 | -47.7636 | 2026-09-02 04:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fd64bd09-fd30-3793-ace1-51c22345e927 | -8.4856 | -54.7225 | 2026-09-02 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 8c53d9f0-14d6-3ecf-9898-1ec234d96100 | -8.4858 | -54.7023 | 2026-09-02 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 667708e1-e94f-3b15-ad41-330fe73ba6b1 | -8.4485 | -54.7048 | 2026-09-02 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| f2102472-0d76-32cd-a4ff-9c0ae84b229f | -8.4483 | -54.725 | 2026-09-02 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 34db4491-dd72-38de-9972-d9e5f59ee124 | -8.4669 | -54.7237 | 2026-09-02 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 16481936-e8d3-3ef7-8d4c-22c99cbe1d96 | -11.65483 | -50.19978 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8759879-344e-31a7-8bc1-14825637085a | -8.47505 | -54.69909 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a9334fa3-e4db-3bac-8dca-30630f8c1bec | -7.54913 | -54.99624 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a57246fe-19df-3db5-ba94-bd13d413b494 | -11.67161 | -50.19296 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 725c7673-1d27-33cf-b849-271fb12bdd0e | -12.80221 | -46.44592 | 2026-09-02 04:21:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6b3b572-791f-367c-b389-2af7bfd26be6 | -10.44015 | -46.73507 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cf0b2c7-1fba-3689-8478-18cc4859c50d | -6.94183 | -56.45281 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eee5ae01-6768-3537-bcd6-9edbf6dce42f | -11.83579 | -46.75153 | 2026-09-02 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7011689d-7efa-3b0e-b59d-1491310b8c52 | -10.86442 | -45.37473 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 839f6f26-cd08-316d-bea1-9c4360f7fcc4 | -15.37086 | -47.69001 | 2026-09-02 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ccfe9d1b-9cd6-3be1-9a97-98142e47814e | -11.72518 | -47.63554 | 2026-09-02 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95f4294e-c860-398a-b9d1-49ea805d4116 | -15.1751 | -46.22546 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d2983bb-609e-3130-9dfd-e1454659037a | -12.13418 | -47.10003 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d106a8bb-c00a-3162-a22e-2fdbfd0ad6b0 | -12.12711 | -47.05852 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f31ea159-484c-35eb-908f-a3b960c01b52 | -11.01358 | -48.37655 | 2026-09-02 04:21:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bfb066f-93c5-3fe0-9017-c88817d50999 | -11.83207 | -46.03975 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7547fb6-b38c-3003-a428-933468e6a396 | -10.39394 | -49.99539 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8baf8d18-af20-3572-ad27-959e9a9692c7 | -11.30965 | -45.15296 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6325ce2b-ba34-348e-b5dd-9cb7b755c3d9 | -14.05638 | -48.40481 | 2026-09-02 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc7e4c8a-91be-37da-a659-d0eec258be7c | -8.46334 | -54.71846 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 255636e1-4a68-3e9e-bc78-e58aaa211a95 | -10.9002 | -45.34084 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 54cfb920-9b01-321b-8546-c4dcb579d63c | -6.76093 | -56.33366 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58811bc5-9161-31cf-a527-440e884b0aab | -11.30138 | -45.16253 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff79e82e-bc81-3f00-9a9e-265d70bc837f | -13.1149 | -45.16824 | 2026-09-02 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b62fce97-049a-3001-97d0-d65f500d229a | -9.55256 | -48.38552 | 2026-09-02 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2941d577-d84f-3aa5-bb61-1d4a7c10cf08 | -12.13654 | -47.06371 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60d724f9-f84e-3768-81e9-1eb81c97bd1c | -10.67654 | -54.04868 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 53216592-90f2-3f12-8838-401b25c93894 | -15.66262 | -45.89976 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69566607-9b9a-3d89-9baf-30af9864dc7f | -9.23165 | -47.97477 | 2026-09-02 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f3c7462-8952-3541-b962-0ee9a7b0d942 | -11.33524 | -50.59001 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 51947d69-5bb2-3982-8f2a-2c65cae502bf | -12.05885 | -45.01038 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bc9ee09-050e-3461-89d3-ac8aac9867f3 | -11.83264 | -46.05782 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4ab45c1d-f0a2-3a6b-9d7e-69f312325e9c | -11.66022 | -50.19098 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README21.md)
