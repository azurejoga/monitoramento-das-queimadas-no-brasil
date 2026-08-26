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
| 6f5e0cd5-9a56-3af4-9116-5a2b8ad43f33 | -7.00415 | -59.3109 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 18ba1d1e-bf55-3ade-ae03-8513cef3d95d | -3.1359 | -61.18718 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b9d08ef2-4ea8-35a9-bb45-915a47ee3c8c | -9.97947 | -48.32746 | 2026-08-26 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68f0da56-e2ab-3d4d-96b4-8aa405a87ec6 | -6.25991 | -55.41988 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fe28bdb-be26-30af-9616-43738812c1c5 | -7.74947 | -44.76075 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a17c702-f16b-36a0-8cd0-920f09d26e6d | -7.52229 | -61.38797 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| cb9e2068-5f78-314c-8071-69847423ec6f | -8.68485 | -54.71854 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00d10681-ae37-32de-a684-58a735cf6ccf | -6.93657 | -62.88116 | 2026-08-26 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8037d70d-9dd7-39f4-9f57-e86bdf236133 | -6.1338 | -59.89299 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a9c2bd0-8925-3089-97c2-cb51e29a5cc2 | -8.00918 | -51.82515 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c35c984-737f-3e11-8985-23824c42a35f | -6.40752 | -60.05397 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae8aca79-8c74-356f-8374-8af3e1f67505 | -8.756 | -49.9454 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 879b4099-d832-390b-b9f6-1d96bf84c68a | -8.20622 | -54.96467 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99e71fa1-0137-3cb7-9457-22ae791d1a28 | -3.59517 | -54.04471 | 2026-08-26 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bde1d9ec-571a-3e7c-874a-4fe73cab0c5e | -6.72759 | -59.44779 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0b6376e-bb04-3cc9-8395-3aaaebe9954d | -3.49779 | -57.02437 | 2026-08-26 04:51:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f741cbf9-7a56-31c2-b8e8-5c517259c006 | -8.11304 | -47.46853 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8851a24-f1b7-3b07-b814-91a94fa54d74 | -7.30649 | -42.96411 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 79543204-ea43-3d2d-b3bc-976814ba459f | -8.15431 | -47.50988 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b01f9e54-fa44-366d-9625-e2699a724b4f | -3.13533 | -61.19055 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e505fae2-6160-35f0-bddb-823591ff4f69 | -6.86214 | -59.71162 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f71b67ef-157a-32f6-b240-14fdc23501be | -8.01848 | -51.82341 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a71c681-8b5f-3fa7-9c39-0db8779dbf89 | -6.11985 | -57.69477 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 528d0549-b759-39f9-9823-fa40eb159b8c | -7.31805 | -42.9889 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5ea8a5a6-875e-3bf5-b4d3-113783287192 | -9.57123 | -49.28111 | 2026-08-26 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc49d06d-eb01-35f1-8248-49a4368219a1 | -2.79577 | -49.58415 | 2026-08-26 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| adb63fd4-4402-3cf6-95c9-ddc2b3808d8c | -5.51818 | -44.11729 | 2026-08-26 04:51:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc3a058c-39c9-3f11-87a3-39d37fff8a49 | -10.38014 | -45.06292 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2e2261a1-2ed9-3e98-8a1d-e4ff191a278e | -7.51826 | -61.38127 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 85932880-25ea-3fcd-bd57-7b67f2c94220 | -8.14123 | -47.51178 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9249488-5e77-38a9-9a9c-09bf31749d59 | -6.98127 | -59.2584 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 473d6334-473e-3810-8290-cb5fee059a8d | -6.63639 | -58.49765 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dafea3a5-232e-3b74-b1d6-a39f1c4fc40d | -6.18946 | -53.48968 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b58b2696-a932-3f7a-9254-2e710c236ec4 | -6.94055 | -52.79843 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bacb960-a147-3460-a73b-916498d746f4 | -8.08335 | -45.89954 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d719cc9b-229b-31ea-9fa8-36059b13cfd8 | -6.1303 | -57.83116 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36136a3e-ca37-37c9-b642-e68332b96a41 | -8.59826 | -54.75271 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 215f728a-2885-3211-8351-d12b80b5994d | -7.3791 | -55.1912 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e6c8f1a-a816-3eef-94c4-00ada3ffe300 | -3.5119 | -48.03939 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 698fa0f0-fe69-351c-ba94-dfc13676ffc1 | -8.57613 | -54.78271 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10bc179f-7800-318e-844a-92239624197a | -8.12147 | -47.46945 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67905fbb-7824-3519-92d6-e0f6d3a00f59 | -6.28107 | -53.36105 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fdcef1d-fe31-37da-adff-874a84a21031 | -5.93765 | -57.73258 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adf7336b-fae5-33aa-b4fc-efb0f6806ff1 | -6.12862 | -57.81621 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b7cdcbb-f0f7-37ce-b36c-f5818a0a83c3 | -9.16615 | -49.97799 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cbef8d8-6cb4-3721-81c3-584fcb133377 | -8.62594 | -54.73108 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 096a41c3-d8ac-3ff3-9bda-005267b91ae8 | -7.76027 | -44.7566 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49fc6b90-fa99-3a2d-b0ab-9afedd6b5bd3 | -8.14649 | -47.50477 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 39351a0b-5132-3eb9-ac56-6d2f868918a5 | -7.38183 | -55.15272 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b133f2bd-86ab-3d63-925d-ff1d469be571 | -8.0173 | -51.80844 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11582fa0-5250-371d-b0c2-9b06f0873b65 | -6.9901 | -59.2597 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e253b60d-0d29-3f29-84db-544771103e80 | -8.61879 | -54.68905 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a8fa8ea-f60a-36e7-b403-edded4b9bdb8 | -6.80946 | -59.68593 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9cb45cd-f5af-3d22-9bb1-ff046623d9f7 | -6.83665 | -59.9404 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d32fe165-42fd-356d-a731-255066a25e88 | -3.73415 | -49.68183 | 2026-08-26 04:51:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9b52721-5037-3a4f-a1e8-52000eb0e5f1 | -7.28791 | -44.08323 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f5d5cc5-4153-3fa9-907d-20088fc231c4 | -8.5535 | -54.79404 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a04b587-b70e-3ace-b6f0-fc2acf794b56 | -10.37285 | -45.06302 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 33815d61-0d2b-3652-a431-ed71252b3d13 | -9.02944 | -50.78987 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca2da356-8d73-3661-970d-5146213bc7c7 | -5.90489 | -43.46145 | 2026-08-26 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a41a5958-8f24-3e1e-bc55-bad87a4740d4 | -7.38723 | -55.1848 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdb9c94c-bc98-3bee-b9f0-407ec072e288 | -6.27166 | -53.35601 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2c78e11-fbf1-350b-848a-33d3f5e6ed08 | -8.64467 | -54.75311 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99c2ab49-261b-3098-8f43-bead692cdb11 | -7.51876 | -61.37835 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| b8a72e0a-4750-3505-bf39-9991bd5b2786 | -6.11274 | -53.84566 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca7acc61-ec2a-3cb2-ae1b-b59e7657594a | -7.50074 | -55.35297 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0599d75-9f8c-37be-8970-6f64069f87a1 | -8.75821 | -44.25455 | 2026-08-26 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26b917af-e4fb-38d0-9824-c294d5ff835a | -6.50756 | -53.26183 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 485f251a-d41d-32ee-b664-dac8aafc9754 | -6.95496 | -59.08981 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 044dc501-6616-3af3-997a-53cd70cd843d | -6.15028 | -57.71053 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fd584d0-5d03-3c21-93a7-1eaa2b392c88 | -3.05807 | -48.74393 | 2026-08-26 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb0e6d0d-21f4-3a7e-bfaa-7c24b7a9309d | -7.21289 | -60.61095 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71a98887-9bfa-3c8a-beae-57d5a222e5fa | -8.21725 | -55.00471 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dd5571e-4471-3003-9c52-1a2c366992b5 | -7.27339 | -45.36109 | 2026-08-26 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f43a2e0e-e3a2-3080-a071-f416dbdca558 | -7.06869 | -59.22295 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 67587f45-eefd-3993-a05a-52f621fd511e | -7.48716 | -55.32686 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e134288-a207-3ece-a0df-85190d4495bb | -6.80492 | -59.68517 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4108fd99-db86-3c31-b1be-aeeb69155bb0 | -8.21664 | -55.0085 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18ed2fc3-1eb9-3800-ad05-8c82360a9676 | -9.03997 | -50.79134 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d532a200-9737-32aa-8d0d-90c51e557b6e | -6.18018 | -55.44091 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e49bc783-e42e-3b3b-aa41-54e637060642 | -6.25232 | -53.37084 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2db77eca-54ad-3cc2-8dcc-d5853ce6ad92 | -7.86185 | -46.11206 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f8cdcbb-c226-3bca-b559-db5d31dcb592 | -7.02448 | -59.24342 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05afb3d8-793d-3401-91ac-a0e7455216d0 | -8.22685 | -55.01029 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efc24951-9f43-3678-82ed-caaec627fa6f | -7.27758 | -44.076 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e366e09-2d04-36d7-8196-25c4d5e00910 | -8.62265 | -54.70825 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b41f7eaf-9d56-3392-ac0e-8bd16e4a5f2e | -6.3582 | -46.12064 | 2026-08-26 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 694149df-7946-3698-9a0d-903f17b18c90 | -6.83717 | -52.50185 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20d798ef-7b38-387d-9893-bae101a3f877 | -7.3928 | -55.15061 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 148dc95b-db8d-334b-8511-a02270ef2331 | -6.2469 | -44.79684 | 2026-08-26 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5aa5b644-b42b-3f1d-80ea-93a4d47dd78d | -8.5697 | -55.27938 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c0650dd1-7022-3c2f-a394-7d41655f3f59 | -3.1294 | -61.19307 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73e7efc1-3c0d-3972-8fc0-a029967fdb80 | -6.26946 | -53.36995 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| acab29d3-f31b-3958-bc5a-a1a1b0e4f3ba | -9.44485 | -51.67851 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f315cd0-0072-3ec6-be0b-7879ece9a1a5 | -7.07308 | -59.22363 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 80b0f332-5bb3-384a-8237-24fd51536fc8 | -5.77403 | -57.55666 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 348f86db-f63f-3ed8-aa77-2aca5b677901 | -7.3743 | -55.18329 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fefd225-dbf3-3c94-98fe-f283bb5b9b71 | -6.12842 | -57.71769 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 296b412f-f638-30d3-ae81-6fee25a99483 | -8.61147 | -50.01641 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 858ed08b-3472-3358-b2e6-c9765a439d79 | -6.83501 | -59.94989 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README35.md)
