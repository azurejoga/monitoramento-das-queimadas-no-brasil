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
| b4090ab5-15c9-375c-9707-581fa5abf3d4 | -6.13345 | -57.7442 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e6c19da-c95c-3139-97c8-6d8ca3e6b997 | -11.32045 | -45.06474 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e050cc3c-615b-356e-b2d0-5216f18e5f99 | -9.73154 | -43.40735 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b954985-a543-386a-972b-f2bb35963a20 | -11.52108 | -49.61451 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a2ba21b-c230-3502-a4e6-48b7e8809e01 | -4.67699 | -55.63023 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20ba460a-bea4-3a9e-8118-f8b24e0d5dc3 | -9.51828 | -41.99369 | 2026-09-07 05:04:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 72b6df60-5dd2-3999-9345-2cb0c0fde392 | -4.50767 | -55.71113 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f63be08-b23f-3d12-8526-594e76776ad1 | -6.86987 | -55.59789 | 2026-09-07 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a7f38f4-eaa6-33e7-88f1-9d932362b76f | -5.48596 | -60.20453 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73e36556-106b-34da-9c5d-c95dd78b5d09 | -3.76607 | -61.75901 | 2026-09-07 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dddcb91-e862-35ea-a3c9-6c50e1600682 | -3.38725 | -61.33003 | 2026-09-07 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c171b9ab-7ada-3eaa-b90b-7e62b57544a2 | -11.32082 | -45.0618 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25f6d32b-6f79-3132-8294-1d80ed90c9e8 | -13.30419 | -45.23068 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 7fce4e37-641d-35ad-81bd-fd0494ade185 | -13.30768 | -45.24094 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5d165978-1b45-3fb4-b147-f80bb75b9d23 | -5.29879 | -60.1427 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c33b7e7b-1635-333d-b6c8-d59fe0c47cdf | -6.05532 | -57.7908 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3a21d0c-8ada-3662-a5ae-a006d91f9ea8 | -9.57529 | -40.35213 | 2026-09-07 05:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a0f3f00c-0fcd-3b29-b282-bfd7a84ea4c2 | -4.47351 | -55.08983 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3b49fd2-23d9-3e6b-88d6-f4f9ada36e08 | -9.732 | -43.40375 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e0dd009-acf3-3898-a2a0-c9e762440487 | -4.6726 | -55.63404 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9f3798b-cf40-34f1-b6b8-0de177ef2c09 | -9.74822 | -43.41228 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b6835fcf-9046-3ba9-a4c3-833de34b0e6e | -4.65781 | -56.02621 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c229dc84-ff48-3773-aff6-767a5469dbcf | -4.2881 | -59.96298 | 2026-09-07 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8f51ab5-2338-3466-8e98-9ee099e4981c | -5.97702 | -57.6879 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 138308e2-dc67-3ed7-96c6-5f423c8b360d | -11.52037 | -49.61935 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f29f73a-c9cb-38c6-ae46-2853eeb7e36f | -8.75864 | -62.43722 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd2d8688-4671-30bc-bdd7-a03e227748dc | -6.44661 | -58.15943 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 380594ce-05b8-369b-b7b2-169551e08699 | -6.44371 | -58.15125 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec2616db-68fa-3422-b131-8b82fca7747e | -8.87038 | -62.35131 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42824e42-0b52-3833-b1c7-b52db91e99dc | -5.98802 | -57.69703 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b27ee5e3-2606-305a-a751-2b9007dcffa5 | -4.46929 | -55.09327 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e71d6d2-81d4-3bba-965f-5f54d7e5f707 | -6.13021 | -57.74393 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b883e9a1-faca-3e57-99ac-462e2db3b4dd | -5.84743 | -52.04694 | 2026-09-07 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0ca4568-5038-31de-a727-c6c8593f19de | -4.51064 | -55.71617 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98af8240-3962-34af-861b-a241e603f6ea | -5.14471 | -55.95975 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e8be416-f670-3061-b5bf-b280c231b4ea | -5.28864 | -60.12871 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca1aca61-379b-3594-8268-7a0ae9b923c6 | -8.75698 | -62.42958 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 250e676e-7c3c-3dbc-b454-39ddc4146979 | -9.74971 | -43.40072 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 86b180e5-f2a5-3c56-9d99-d0f8bb5dbdfa | -11.51024 | -49.60802 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 722cd596-eef4-3976-bedf-661796bffe48 | -5.35158 | -56.01727 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29e1909f-b3f5-30b3-8e41-dd174c1142b9 | -7.91539 | -47.66747 | 2026-09-07 05:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9804108b-bc45-3d4b-a8a7-abdfb1a14bb7 | -6.13427 | -57.74468 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce419152-bc90-3767-9175-76569551bf5f | -9.73487 | -43.42641 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d9f73342-0bb8-3fc8-a4c7-37bf52a41f96 | -4.47708 | -55.09041 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52edaff4-28d3-3116-8765-bfe6e997daa5 | -5.26621 | -60.11385 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01f3da53-eb4a-3514-a1ec-659129779174 | -3.9259 | -59.23441 | 2026-09-07 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4318265e-565f-33fa-b03e-e4f74cc598aa | -11.52806 | -49.6205 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dcd74309-b451-34ce-801b-074db1622168 | -6.63667 | -59.44181 | 2026-09-07 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8871542e-c0c8-34d9-abf9-64cb4c689f25 | -11.5057 | -49.61226 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f25be36a-316c-3a15-9c73-f099aa6910f9 | -5.85021 | -52.05093 | 2026-09-07 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 414fecf2-9160-352f-b5b5-f4d87be2584c | -5.30755 | -60.1497 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dc36d67-285c-3192-8fb8-a6f03b48029a | -13.29792 | -45.23292 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 80d45e62-1e6d-3ce2-945b-c05b2a8ab2a6 | -6.87212 | -55.60652 | 2026-09-07 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44cf2928-55c8-3af1-a07b-c93a9e2beeb3 | -6.50583 | -58.29444 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cae944f-b361-37df-9c45-ef4c659d133b | -5.14325 | -55.9685 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b2a92e8-9f49-34db-9d90-74b688b6bba7 | -9.56771 | -40.35574 | 2026-09-07 05:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3842e58-3391-36fb-bca1-35e3c10a5e9f | -4.41578 | -59.96449 | 2026-09-07 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 645bcc7f-6048-3d66-a5fa-ec89282de8d9 | -5.99148 | -57.70132 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 40b79b52-0ed3-34bd-be8d-9b29cc012547 | -5.36712 | -56.01539 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f7390c9c-2d1f-3acd-9e3c-9bda18871b25 | -11.52876 | -49.61568 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1bfbebe7-9dd4-31be-bffc-fe1c2f14f227 | -4.66531 | -55.6327 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0aabfe6-69bb-350a-bb74-72ee03923a94 | -5.64576 | -60.23639 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5cdcdb7-1abd-3972-a806-e7cdc589f880 | -5.35753 | -56.02726 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0850324-7365-3716-91ba-402b502a9390 | -9.72635 | -43.40282 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bf297f50-ca7c-3fcc-ae83-986efb1808fe | -5.36421 | -56.03288 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a874a1a-2c0d-3bef-afd3-3c65df6202cc | -11.51583 | -49.62357 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b118f13-25d8-391a-8ebf-1dc18a9c910a | -5.96766 | -57.6938 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a49e5b06-96da-3347-bef8-f263b49f1a2a | -4.23126 | -55.56916 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b33a377-de53-30ee-a80c-cc6e510e56ac | -5.27354 | -60.15902 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a42f0c8b-40e7-3d61-86a6-a53fd3de17a1 | -11.52492 | -49.61509 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6458386f-ce96-3198-88ae-b5d5ffbd3a8a | -8.7295 | -62.44576 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 609c0a1d-a401-3c0e-8709-11e8a44923f3 | -11.52531 | -49.62187 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f0b1512-56a3-3593-b357-00dc829a54ce | -5.26868 | -60.15818 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2415ab1-50d7-382f-a57f-d3115505e8aa | -9.73631 | -43.41514 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f953e418-f1f7-3f63-a82f-557db8840d43 | -3.61525 | -60.57286 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2b82149-abb7-35a7-acc9-529dc0c97d57 | -9.51889 | -41.98886 | 2026-09-07 05:04:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a973984b-2bb1-3354-8edf-75ced7ed61bf | -5.36806 | -49.19559 | 2026-09-07 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad4ef493-92d6-3aa8-9102-baf8ee218111 | -5.16324 | -55.96269 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d48557fd-fb95-3888-90bf-1ce92563653f | -7.11407 | -56.50886 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b716a11-d46c-3c9d-acc1-65473f6066aa | -5.14696 | -55.9691 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 046a9f46-e340-32a5-9df2-0656e02e2a23 | -5.3531 | -56.03102 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a56ab2e-aa9e-30ae-a64e-a357ccc677d0 | -8.75514 | -62.4261 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d54d79e-2076-3b21-8ff1-ce62b42643c8 | -5.15583 | -55.96153 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 642e04a8-ec1c-36b6-b159-c7d1fa292311 | -8.76355 | -62.42403 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4229d151-4b60-3308-b6cc-3490d114f499 | -11.51794 | -49.60913 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fc48c8b-e15e-3d30-a04a-7ba931192f59 | -8.76229 | -62.43071 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a6269d1-f257-3187-af88-78ff06ffc940 | -5.36647 | -56.04227 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2354c69-c1a0-32a1-bcbf-63e6d92011b8 | -6.06352 | -57.79198 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d400206-d104-3f7f-a288-da7bcdd83a90 | -5.5953 | -60.25226 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 532646b7-3014-3354-afea-5e4cf73ee6f6 | -3.92669 | -59.2296 | 2026-09-07 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbcdf788-2ead-36e3-bd51-c917e4d94508 | -11.52735 | -49.62529 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a868cc0b-9957-3de9-b8e6-cae36a8c1dda | -10.74358 | -45.07291 | 2026-09-07 05:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1476c986-e98e-3bb2-a1f7-4ccadb18d8ef | -3.61011 | -60.57198 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0916ba8f-7846-3859-859d-a5a6b392e53b | -6.05696 | -57.80592 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f49d92a6-b614-37c1-a03a-ed1bb7ca0a98 | -10.37441 | -45.01406 | 2026-09-07 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46588091-e911-34d4-a1ec-d4c87821c43b | -3.61063 | -60.56896 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e4b50d0-76a3-3457-b11e-54329098de32 | -4.42937 | -55.09084 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e44ab006-1acf-3abe-96fd-518d776e5a12 | -5.26383 | -60.15733 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45da2a48-7a13-3fd5-a716-a90867f495f8 | -5.29971 | -60.13741 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f3c2c34-4b4c-3438-9e43-495fd262de98 | -13.31334 | -45.2384 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |


[Clique aqui para ver as próximas entradas](README24.md)
