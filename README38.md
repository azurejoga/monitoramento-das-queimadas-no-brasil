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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d826817-44a0-3ec7-b27c-11eeac95d50d | -8.58311 | -54.71969 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| b64276e4-baad-3d3c-8f34-9183c6788355 | -7.62607 | -55.62437 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cc5f07f-520a-37a4-bb05-3f7caec967c9 | -8.36734 | -46.35917 | 2026-08-18 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 401a8eec-976e-3eba-bab2-e5b6fb88ddbf | -10.40893 | -61.20664 | 2026-08-18 04:57:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3bedd0f-9c16-3650-87da-8f3954deae5a | -10.93042 | -57.17937 | 2026-08-18 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f84afab-a029-3223-b7c1-7ae33a4ddab4 | -9.00921 | -60.50344 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1561fe7c-cf63-3b11-8653-198c8392732c | -6.87 | -56.4147 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0335efc6-3401-392b-8579-e758fb8be722 | -11.32416 | -51.42373 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3739ea8a-5e0b-349c-bbdc-7189e6c11d7f | -9.06798 | -50.82923 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0b98da75-6c0f-34de-b58b-8f47ee067f96 | -12.46615 | -54.19075 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ca3d129-7417-31f1-b639-f2e7408246e6 | -6.99301 | -59.04662 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea64d538-e552-393e-9982-51da885f1a19 | -10.408 | -61.21164 | 2026-08-18 04:57:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1a4f623-90a7-32b0-bebf-2ec700ac9f70 | -7.72412 | -56.19297 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb17254d-992a-3970-a7b5-bc9a765e327f | -6.96129 | -59.02411 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6ad1bec9-039c-3ee7-ba1b-1d8ade004834 | -8.21359 | -55.03475 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a2ae658-e7ec-3f17-b374-ac78fa6bb06c | -6.77489 | -59.75986 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80f976c1-227f-328e-9d85-a5f0e4e87534 | -8.90149 | -60.55191 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 45c9d608-4fc4-3da3-8258-36b5dc37c5ee | -8.21262 | -55.01937 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2493ad25-e4bd-3417-b81d-3a41e7935a21 | -9.82143 | -47.28296 | 2026-08-18 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdadeece-4e9c-3fbf-81b1-072f73498cad | -6.84796 | -59.00129 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a7112ffb-9d76-3429-b506-0744137def71 | -7.39935 | -46.48497 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfc5c544-c177-3350-96e7-e6bc1071fca4 | -12.40049 | -54.96278 | 2026-08-18 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90369329-a51b-39d7-b24e-f79d13d30de9 | -8.6033 | -50.34371 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 70b3ec61-f036-3f6e-b30d-9f4de6eae1c0 | -8.32099 | -46.48215 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9695696a-e000-3611-b21b-f55abdadc230 | -12.77516 | -48.42905 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c81091c-4b6a-300f-a60c-feb02cea8526 | -10.07169 | -60.49747 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d69e389-640c-3bd8-8c4f-d855890e71c0 | -9.49202 | -51.66994 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f415d2bd-d276-38e5-b9ea-1b60ffcb0605 | -7.12525 | -47.54738 | 2026-08-18 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79f35975-0cd5-3e81-bc6b-612ad087105f | -8.18783 | -55.01954 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c638352-5d78-3988-b744-0bfd12d4f218 | -7.63721 | -55.62224 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5ab09d1-a971-31cb-93c5-084583b14a3b | -6.988 | -59.05 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ee8649e-6ce8-34a3-aaa6-b52797aa8534 | -8.56302 | -54.69417 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2557dd4a-e387-35c0-a63d-41ac952f1f83 | -8.49049 | -48.8054 | 2026-08-18 04:57:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6df54bba-4f52-3aec-b45e-b3eb1546186d | -11.12169 | -47.27683 | 2026-08-18 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 77309f3b-f4df-3af6-a060-93cbcaea5b0b | -7.60607 | -60.82303 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40795662-fc06-3888-9b07-92000efb9a25 | -11.92575 | -55.91549 | 2026-08-18 04:57:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93bad582-ac17-3a65-9f0f-692dfa91db07 | -8.58716 | -54.69447 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a8e6ccb-5ee7-3065-9fd4-09ab34d3b399 | -13.46036 | -51.80153 | 2026-08-18 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b7fad22-1ae1-3442-b0f1-dac618b06a6e | -9.18171 | -56.98618 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e7018f06-0be2-30ce-bb32-73f6474a48fa | -6.76922 | -59.46228 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77a7cd04-e2f2-31fa-8eac-ff4c3cfed127 | -12.40106 | -54.95922 | 2026-08-18 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adaa7bd4-d814-3f75-a4d1-f0c838bc7701 | -11.33986 | -51.12314 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd8e5f30-0609-33a5-b05a-b816bdcbd99b | -6.69731 | -56.16473 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2caebd7-9146-3488-9974-184e7ced00d2 | -8.89862 | -60.54868 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6aaee25c-bae5-3d77-8076-b0bb57f4e221 | -8.62528 | -54.70445 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c97ff3d-03b8-3799-a094-1ad702377d2e | -12.75405 | -48.42569 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b813e4c1-63f7-306c-ab4b-28306eecb067 | -7.81341 | -44.60288 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 180dbe39-0c67-34f9-a7aa-580590835ee7 | -8.36086 | -46.3723 | 2026-08-18 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59cf5bf6-76ec-3b8a-8c6c-7c12721ad152 | -7.37215 | -55.48876 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3bdad22-619a-30b2-902d-5d15026af869 | -9.46187 | -51.61591 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acd3f110-291e-3bd6-a0dd-3e62a66ed64f | -6.95266 | -59.02264 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 379cb94e-a992-3b07-ab09-7fccf14ac899 | -8.56113 | -55.31322 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b2c7ee4-01e2-3a7d-807e-c81edcfc8228 | -8.58927 | -54.71338 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9c66079-d595-346b-a0c1-49fa0449483d | -6.74458 | -59.1826 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88427242-86ea-353e-8a46-1e73da52cf67 | -7.38526 | -55.48241 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 063fcd1d-6600-36d1-bc4e-7a4ed1eee3f9 | -8.2232 | -55.04014 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c1aa5344-963e-359b-9187-1d00b2812048 | -8.57649 | -54.69639 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| d67e8f0f-e7db-3bd5-904d-925c0f66175f | -13.26618 | -51.64983 | 2026-08-18 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e58d1c73-eb26-3095-955d-87552143ab5c | -8.56627 | -54.71692 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbc36539-9518-39cc-bbe4-09b6cebf1135 | -8.56581 | -54.69833 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f831f843-01c7-38d1-a7e6-b87af56f34d8 | -8.57823 | -54.68557 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0410403c-8641-325a-a47c-426d610722b7 | -8.58159 | -54.68613 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c67fa206-5e64-39b3-9450-474db2b8cf0d | -8.5838 | -54.69391 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b826f350-db3d-36c0-983c-6b2ca0fa835a | -6.85005 | -58.98903 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b779aa9-2f0f-3e40-8ac7-3273bc34b770 | -6.75761 | -59.15849 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7eff1846-015e-3e36-8699-b77139f1bb40 | -9.45259 | -60.29235 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2a9672c-5ea9-3f38-a9e5-1bc51541dd97 | -9.16378 | -59.67495 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ac4d95b-9c6c-3f85-a37d-230e62fa154b | -7.88147 | -61.79515 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9e10615-74da-3064-a0a0-01118da71cf0 | -9.41972 | -48.24895 | 2026-08-18 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 494c2121-72df-3f74-9dbe-7b2224e3c3fb | -10.92754 | -57.17436 | 2026-08-18 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2dac4a0-1816-3374-8546-fb351a1f84d5 | -8.56976 | -54.69526 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74bc463f-759d-3e91-b68b-f92734cd000c | -8.94949 | -60.55054 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a547f1a2-af9c-3597-b489-d91dba2b87de | -8.94717 | -60.51017 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f78018cd-247d-3279-b22d-ac940fb468bc | -6.76941 | -59.76154 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 820feee2-c4e3-3947-b259-dc268b45dfd2 | -12.46782 | -54.18019 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2584a23-60c3-3fdf-b265-54c91a47980f | -7.56796 | -55.55567 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b97ac3f1-d69b-3713-ac5a-654793fe6088 | -6.75041 | -59.1746 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 385f650a-f8bf-3d24-9934-fb2da7994b8a | -8.33055 | -46.49075 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 526afb56-2ee9-3875-9cbb-5d84bd335b6e | -8.55487 | -55.30837 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41b7cf86-953a-364a-b482-85074a59e26d | -11.10181 | -49.91041 | 2026-08-18 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| afabb10b-f66c-313c-a4aa-8b4d53e85624 | -10.85735 | -44.96722 | 2026-08-18 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9f0cb96-f7a3-3147-a894-31333c46b88c | -6.75186 | -59.16932 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0b771fd0-8cd1-33e9-8870-e25478359de8 | -8.6247 | -54.70807 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6dd8084-62ab-3b97-b0ef-aef61525aa31 | -7.81385 | -44.59979 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a6743ed-1aa7-399c-a357-6fa26259899f | -10.14567 | -54.27623 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3bf805c9-254c-3735-bfa1-8b86093d42d5 | -8.6326 | -54.70193 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86c6a2f3-16fc-38d8-90d4-88f69d8d7031 | -8.52685 | -54.89681 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 202f7684-3d81-3c3f-bdb4-3a0dfbc52249 | -8.57765 | -54.68917 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 6fad5325-578d-3073-acd8-b618b126c5b0 | -8.96851 | -60.52396 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff3cec71-e754-38e4-861f-43894bbfdced | -8.49149 | -48.82549 | 2026-08-18 04:57:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ef38c38f-465d-3968-840c-40b3758f6b18 | -9.1212 | -61.6006 | 2026-08-18 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 76ea50e9-66cb-3f46-9d66-949d329393d1 | -10.56629 | -51.97234 | 2026-08-18 04:57:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffbd76c1-7fec-3a71-9042-4a69b15fd2dd | -6.74886 | -59.15705 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9e53624-e6f9-3c9a-a8e2-cf55e47b963f | -8.55548 | -55.30462 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25f7e2c4-f0cb-3737-a200-513278d8f0ef | -7.63307 | -55.62556 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ae53a24-1836-399a-ab89-3a4f31a41c4c | -11.33071 | -55.26825 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a111eb69-e3ae-3bdf-a399-b1434a541033 | -11.11937 | -47.27425 | 2026-08-18 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e3014512-e92f-3d78-874f-ec7bd288a4e7 | -8.7334 | -62.90027 | 2026-08-18 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0470ea8d-c160-36a3-bc27-01d522547d59 | -9.73464 | -60.74396 | 2026-08-18 04:57:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f027487-474f-3aa0-a63f-ddca86d274e3 | -10.85694 | -44.97036 | 2026-08-18 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README39.md)
