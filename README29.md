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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2b4b871-a260-3b40-9af5-ed9cdf6ac38b | -10.8979 | -50.24007 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea1fc1a1-7db3-31a7-bbc8-e835c80a2324 | -7.34132 | -55.70059 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58e342ba-b5c7-39fa-a9ad-3e2d6f1e4d31 | -7.64069 | -42.72664 | 2026-08-22 04:27:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b204db31-b4b0-37fb-a890-99be4866ca84 | -6.60873 | -56.36743 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba9e120a-6827-3e6d-83b9-b8c88b3c4e71 | -6.79649 | -59.60189 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e74f032b-2ace-34af-99c4-20cf57fd15bd | -6.76682 | -58.69926 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19d05f72-fe62-31be-ab53-a1e5495459c1 | -7.4706 | -45.1384 | 2026-08-22 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18e6bf88-a846-308f-864c-5c5291db58e3 | -10.4245 | -45.1447 | 2026-08-22 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 058b677f-32f1-3995-b4d1-cdada44b9ab4 | -6.79103 | -59.44127 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0fe238ee-9e40-31cc-bc6b-e7fd897047c6 | -8.53005 | -55.32662 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b858431a-1c9b-3b19-bdc8-bd2536ac57e0 | -6.22921 | -55.42395 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45d78cec-6663-3f68-8169-7ac12403f4de | -9.00547 | -50.73654 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e99b560-8d25-32eb-a0be-4652395e1b79 | -9.16815 | -59.44279 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 43ea77d8-b8f8-3d9b-abf5-9e3153227365 | -8.68158 | -49.52555 | 2026-08-22 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1be43e48-2f94-38cf-aa1f-3a0a0bd6b3f7 | -9.17458 | -59.44326 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c8affd99-74e9-32ce-a9de-ded72878006c | -13.38639 | -54.36506 | 2026-08-22 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5aaca091-3797-32f4-a30e-7c90990d965e | -12.66375 | -47.80285 | 2026-08-22 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f685ce49-57cf-3a7e-8b0e-8283b7042e34 | -13.38553 | -54.36518 | 2026-08-22 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 77bcb900-ad1a-3782-9602-87332bc1e240 | -6.65934 | -56.34229 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a9496aa-869e-3237-8c71-e6cc285b84ca | -10.30522 | -48.2219 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6cda2529-0951-3b1d-b647-d59d8e8979a9 | -6.20625 | -55.63796 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdff360b-7c4e-3f00-8adb-823172fbece8 | -6.82737 | -59.66976 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d62e718d-8e42-39df-95b1-9735e76ef3ab | -6.25594 | -55.42115 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 248b7089-b813-3521-8825-14b38a1d219c | -11.20791 | -54.0013 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4059d75b-5b1c-3dff-b9f7-6109a48564b1 | -12.77117 | -48.39585 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1211fb4-f776-3c45-8457-311c86526c21 | -6.88011 | -59.42458 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68af7a59-04ae-3025-ba9c-895828c0d2bf | -6.88042 | -56.63726 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1897bf07-a9cb-33ad-829c-c2a7b35246a7 | -10.52734 | -50.77772 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 074a727d-cad2-331d-b1c5-ec9b861512dd | -8.53905 | -55.33443 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4144382-8e6e-3784-821a-28514e043ff4 | -7.01974 | -59.54984 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 07e648a0-2319-3799-ac0a-be4feeee39d2 | -8.37214 | -41.72371 | 2026-08-22 04:27:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4e948384-d70e-3a0a-a053-ce97d0f24694 | -6.43354 | -54.95398 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c68a28c4-b266-3c25-ace4-fcb1b01d698e | -6.82527 | -59.42071 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a96645d4-df8b-3763-b54d-fbe2f64bcb36 | -6.93914 | -59.3131 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 181f7a8b-b5cd-3670-b54c-35b3b1e44889 | -14.80235 | -44.22743 | 2026-08-22 04:27:00 | NOAA-21 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cffda38-dc03-3512-83a8-d02cc48a454b | -12.79529 | -48.45824 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a71fd059-5f81-3d0a-b5d5-58cecbfe1a0c | -6.39164 | -54.953 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f370b1d-018f-35d5-b2a3-ab7a31f62949 | -11.56406 | -46.93704 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7efc9b7d-9906-3308-a32a-e6e646dd083b | -6.17383 | -53.50272 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71d65289-1a2d-324f-b61d-cd3d22c23cba | -9.17891 | -59.45543 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 42742aa9-ba3c-32a5-bafb-acba1272aac6 | -12.78866 | -48.45712 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19a1e15a-de6f-3b48-91dc-4869cef27253 | -10.51996 | -50.82117 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a0e8236-3808-33df-840a-8be3fcd696ff | -12.2656 | -43.13507 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8d34abc9-e8af-3582-b65d-da84fa8cea81 | -6.20595 | -53.08962 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82a8eb7d-b271-3fb8-b920-5afd1c579153 | -6.76048 | -58.65752 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4f19796e-dd67-3e37-9b24-47ff370aba7e | -8.16824 | -54.98946 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 903b7cef-f788-30a3-9c6b-530b6303baf7 | -6.75665 | -58.67888 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7f9b3e1c-90dd-3b75-ad89-5f954b7400db | -12.82404 | -48.47024 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3d65797-ef22-3d07-864e-209b04741d81 | -10.34516 | -48.25034 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2085f37-dd01-3a29-bf4e-5faf081fe9e6 | -9.42761 | -51.6399 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e384532-2026-39b7-b782-8e96a4dfcafe | -8.53135 | -55.32562 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad1c398f-5f94-3dbc-aafb-6e38a23bb93c | -12.86774 | -48.42992 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f891f996-44b1-3205-832f-200aca8cb66a | -8.02782 | -51.79586 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 413bef5a-98bc-3e5b-a5bb-8888d3aa496e | -6.67044 | -56.34454 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba0b002a-8041-327d-b94e-68695da53d2b | -9.17798 | -59.46172 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| a8574430-21f8-3fa7-9f33-64892eac570f | -8.95069 | -50.73349 | 2026-08-22 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7ccc5fc-a724-3a4b-a283-020cd9d18583 | -8.57924 | -54.79322 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7740077c-d5b1-39ba-8f0c-f1772d8141a5 | -8.89994 | -60.53872 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2afdbdab-d968-3f49-8889-900adcffe841 | -12.86161 | -48.44707 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 240afc3a-6697-315d-8f8a-77099ee5cec1 | -10.30246 | -48.21775 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1984ebef-153a-3c0a-ab9e-996cc7a0da97 | -9.51402 | -51.67703 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 428b35c2-169e-3376-bf53-ecd418bf3689 | -9.1876 | -59.44643 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a315017a-2639-3857-b62d-e325138817fa | -11.13111 | -49.04218 | 2026-08-22 04:27:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 88fcc52f-56d6-3d29-87bc-1aed44d65dfd | -10.51628 | -50.77725 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5bc8730f-c495-3767-8920-7e81757fb421 | -9.18757 | -59.44559 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f46d4ff-c31c-3831-8ad1-5e3ac6074c50 | -7.01303 | -48.02728 | 2026-08-22 04:27:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 114de33e-a5bd-35a5-82d9-756e4c5b3828 | -6.79261 | -59.59287 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4535a7a-e115-3679-adb0-23f35f85551d | -11.3701 | -46.33766 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5258c5b-2836-3ef7-abb8-f87b70df32e5 | -8.11072 | -51.65682 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2b5857e-3101-37ab-bee4-9b5f03f4d74d | -6.77974 | -59.42709 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| cfbfcda3-b1da-3b50-8517-0f13f3076f4d | -9.18006 | -59.45078 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f2828fd0-7997-33c1-9db1-5c958611b6a7 | -8.52951 | -55.32958 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdefa884-96eb-38fa-8911-4dcbbed0ecaf | -13.6973 | -51.84729 | 2026-08-22 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59bfae7c-2885-31cf-a948-0f0059026bc8 | -10.51923 | -50.82549 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5b80da5-948f-3a17-b6fe-fa7aa01c96fb | -6.25198 | -55.41805 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a3ea962-04be-34c9-8d92-b9c8d705e5e4 | -6.25532 | -55.39407 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f282a7bd-c037-30c4-99f7-fd24398a0d06 | -9.18221 | -56.99768 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e210464-cbd3-3fe2-8374-906efcbbe48d | -11.20245 | -55.06982 | 2026-08-22 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5c8ea78-f931-3728-b56b-4763db3b7aea | -8.54452 | -55.30984 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09f8c012-ad77-3a01-b8f0-fa952e0ac34f | -12.8683 | -48.42638 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1871270-2a39-3ec3-9da4-602d6a1e33a8 | -11.59476 | -46.58206 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a5777df3-9c8c-3420-9abc-be175d0963a7 | -11.7313 | -45.5865 | 2026-08-22 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 414a08c2-ffad-3c97-8f36-749ecd067fb9 | -6.87678 | -59.44249 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cbbf2aa-ee36-3d39-bcc2-9925b3cadc94 | -8.63364 | -54.70434 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72f30397-42dd-3e42-b90c-6d102800d299 | -12.8224 | -48.45904 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46c6019d-294b-3aae-bd08-a2d933fcacb1 | -10.77169 | -51.00134 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 56ebff09-d3c2-36e5-8110-46bb25a6a8b8 | -11.59415 | -46.56367 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 78b90d51-71ad-3a6f-98c3-68d55450f142 | -6.12008 | -59.91207 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 23c1a86f-ba35-309c-81f5-18f54306c3da | -10.52807 | -50.77342 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aace5da5-e1d7-3c67-8470-4b6ac7aff3ec | -6.97494 | -59.05339 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b0b9c1d6-7476-39b6-840d-c8af37611521 | -12.83081 | -48.40586 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acadbb7a-2e54-31ce-8226-704c8d3d6e1f | -10.27565 | -50.37665 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b79696d8-d982-349c-8ccc-acaa0385f9b6 | -8.53238 | -55.31975 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1cc14b7-5f3e-3391-b4db-af95f6fb4348 | -9.21353 | -59.76581 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68fecc7f-3e00-3395-a228-f267c6973507 | -10.03755 | -59.45872 | 2026-08-22 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 373f5c42-bbfa-3f6d-80cb-4e65783d706a | -6.96732 | -59.05774 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2bbdef7c-e7a8-3323-b858-00e0d8379e03 | -6.79495 | -59.43385 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5d70d8e2-543c-337c-aa4c-d1cabd6c0dff | -6.89057 | -55.71372 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 155b17ff-ee63-3a0c-862b-e901fedd6c3a | -9.04711 | -50.83081 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bfa60ef-7cb4-37d5-81fb-f5205dbf351f | -12.5918 | -47.89249 | 2026-08-22 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README30.md)
