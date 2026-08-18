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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc3d4e80-8a16-35f4-812d-0cf292cd0276 | -9.43448 | -48.2622 | 2026-08-18 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb507889-1239-3d8a-aab7-f4863d524010 | -8.49465 | -48.83092 | 2026-08-18 04:57:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 29a7cbf8-2ede-3caa-96eb-c17d6c7a0688 | -6.30732 | -55.70997 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 268d6443-2294-33ca-8d50-56838460f432 | -7.63371 | -55.62165 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 356d5a2a-39a5-3bc9-a6aa-dd964905f6f9 | -12.00418 | -55.522 | 2026-08-18 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a35e1e9e-9cf5-36d4-9bad-02fbb3f4d2a7 | -7.36453 | -55.49154 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0162e27b-d40f-3a23-908e-d60b8e2b44b8 | -8.04232 | -50.10612 | 2026-08-18 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 61988965-6bb6-345b-a9bf-b6c8243c0859 | -11.52721 | -46.64114 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 455cf53f-0b20-358e-a0e5-47f2533aba65 | -9.16256 | -59.67639 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6ad2416-629f-3096-a37a-523f9cc747df | -11.10114 | -49.91503 | 2026-08-18 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6c38e690-7251-3e49-b39f-a759d71c42ff | -8.56361 | -54.69056 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 532d59ee-739f-3322-bbf2-5265f7e18f15 | -9.4289 | -60.42638 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5617e522-641f-323f-8a32-5a70267fb878 | -7.17541 | -43.12062 | 2026-08-18 04:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aaf509b5-0d91-31bd-a8ac-8c689897138a | -11.33829 | -45.92122 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4009a14c-752f-30e8-9015-a163f8d46da6 | -11.21003 | -54.01457 | 2026-08-18 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a40ffeef-a46f-32cd-999c-14dfde0910eb | -12.46172 | -54.19725 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6df64ce7-2be0-32a8-a8c4-ba9e16317b4d | -11.71766 | -54.62428 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ecf2ef1-2589-3aa3-a043-a1491ee87348 | -8.10034 | -61.34481 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8788d61d-402c-32cb-b3f6-e41e9cddd750 | -6.74377 | -59.16063 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9a07d500-dad0-3c81-b17b-babcbf334ad0 | -11.32606 | -55.2643 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34e5fe4f-4921-3a75-bade-faf54a8e07f7 | -8.60687 | -50.34425 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e8a7b740-0964-3971-83b6-0a30f909ad69 | -8.57417 | -54.71081 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d47d5c5b-bb70-3e32-843a-475a54b8ebc4 | -12.71919 | -48.49183 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 991f9a59-8413-38cd-81bd-681ae5d4804f | -9.06446 | -50.82876 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8c41fca1-f275-3da6-b88a-7b35193c2758 | -11.10772 | -46.49499 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7460d166-ad98-34de-a76a-002a5a5e51d9 | -9.12511 | -61.60735 | 2026-08-18 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8350727c-ef67-3869-9974-883debef7928 | -8.56697 | -54.69111 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d44cbd9-e29a-35ab-853d-128c229068b1 | -7.37764 | -55.48516 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d2e005e-c134-3394-a455-31c202d9b489 | -7.88319 | -63.7704 | 2026-08-18 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bea4eeb5-26e0-3162-9276-2e3f316f9bbd | -7.28278 | -44.07167 | 2026-08-18 04:57:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee9b3d31-5dab-31c7-a64a-2c744844efc8 | -8.89901 | -60.57391 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2a13e96-0baa-35a2-86e9-3d42ecafa4cd | -8.09042 | -61.34315 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8da02203-19c0-3e5a-8cae-035478604781 | -7.56194 | -55.5707 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52872b01-61f1-307d-b317-832f66b059a2 | -8.59196 | -50.34617 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| f8309339-6a79-34a6-84ce-bed0d85c9414 | -6.8714 | -56.40614 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14bc58c4-a110-3407-a0b8-dd138b3df87b | -7.38398 | -46.80912 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25d9b88e-d0a8-377c-bcae-afec92dfcd89 | -7.91386 | -61.73161 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98753d69-d419-3715-ba9c-299fb7e5517e | -8.95268 | -60.58627 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91cfe406-aef8-3a7c-b8cd-09e9cbc8775a | -9.99006 | -53.95246 | 2026-08-18 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2bfde92-a6d0-37b5-a97c-38ea127c0c8b | -7.53842 | -55.58284 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 821fc470-133f-37e3-b434-79a3815ecdbc | -11.29954 | -54.87601 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbc2edac-f25c-3e79-9b1d-88e2fd1f3729 | -8.57475 | -54.70721 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ff2851fd-3125-3071-aaf2-4a86b3dbee33 | -11.52977 | -46.64067 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7424afdb-a33e-3794-9abc-b083496bd7f1 | -8.95928 | -60.52229 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2de3fd39-3402-39ce-9391-e0148321839d | -9.82859 | -55.16034 | 2026-08-18 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1c584d6-c696-3df9-b3d2-aa12d2b83f05 | -8.72797 | -62.89923 | 2026-08-18 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a3550c0-1b6e-38f6-92d7-7eb865a890fb | -9.17231 | -59.70243 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c72e14ab-e365-3cf0-a950-d4042396ab2f | -11.36869 | -55.41676 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89462037-c8b3-3438-baa1-a8978f896ca6 | -7.78006 | -61.11989 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3335ec5-75a3-3dfe-863b-c824429dfc87 | -6.95558 | -59.03154 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b80cb441-1cf1-3e25-a12e-29ef3d54d6be | -8.57811 | -54.70777 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 44401c32-b8cc-3bea-bcaf-413b1d86b6cb | -9.4293 | -60.45071 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34a78fd1-0dab-334c-a4d7-4657f1f1a187 | -9.21629 | -50.09832 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7eaa7fd-23a5-3c71-9d25-25037a2a92eb | -8.56348 | -54.71276 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 524a376a-3fad-3bea-b278-963129fa9e9d | -11.47265 | -46.56702 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc112338-0963-3992-b492-b66ca63d36c4 | -7.45848 | -59.99945 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10b01da2-e65f-3767-98fb-3e9ef6d9bd49 | -9.98179 | -53.94037 | 2026-08-18 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbd68a93-ceb8-337b-9b24-de904eccb55c | -9.07088 | -50.85728 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a322ceda-71c1-3181-8d89-90c5d3175dbb | -8.89598 | -60.55598 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77414350-7084-3f1c-a92a-8e98eba50e0f | -6.74091 | -59.17764 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1149d99f-d795-3832-9dc5-8d71c7a4e618 | -9.97679 | -53.97181 | 2026-08-18 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 494a2740-5a46-3a4d-b90a-8c3fef0f75aa | -8.21227 | -55.01974 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54dffe5d-2d25-3e93-b151-a8de58ad0bd6 | -13.44223 | -43.84571 | 2026-08-18 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d99bcaa3-a76a-377e-b872-42f58fcae0ce | -8.5991 | -50.34724 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2a4b449a-193e-3096-ab92-f43324f11aa8 | -8.63202 | -54.70554 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 893ec116-bc6e-3b35-a780-90da39ac5b4c | -14.82407 | -46.63394 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ffd62ad3-fe5f-358c-a9ab-3c3e061a327b | -19.6878 | -49.0293 | 2026-08-18 04:59:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf1f7a0e-d974-3e5f-b302-2096c2551dd7 | -17.3315 | -54.9493 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74dbaafb-a211-3365-98c2-3a8e4e96b060 | -14.74759 | -56.34367 | 2026-08-18 04:59:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93599d4b-85bf-36a0-bc20-86a06908ec23 | -14.36163 | -51.8833 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba70d38a-0400-3e85-bfff-da86e6498e53 | -15.64113 | -54.8156 | 2026-08-18 04:59:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6ed714a-2e87-340d-81cc-085883c806e9 | -15.28037 | -56.49657 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a5882ef-3648-3a3f-b5ff-7434f3787b2c | -13.79006 | -53.8465 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4ace55c-6a41-35a7-beb3-05c32a16eeb5 | -17.32049 | -54.93262 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3de0adac-fa71-32c6-bea8-19c8aac703ab | -17.08991 | -46.60202 | 2026-08-18 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20ce3e4c-b252-37d0-b9a2-e5ff8d522bee | -13.02118 | -56.59125 | 2026-08-18 04:59:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adcac6c3-0881-3468-8ce3-4ea82de6a6ac | -15.64225 | -54.80845 | 2026-08-18 04:59:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 847768cf-e667-3f00-882b-73404b803737 | -16.17674 | -55.94941 | 2026-08-18 04:59:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8332a3bf-099b-3222-8b1e-0b3f3445cce3 | -15.46079 | -53.03928 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23322bb0-db96-3058-b6de-b7774f545261 | -14.16315 | -52.89821 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1674fed-503b-36e9-bedb-2d85dfad6b02 | -14.49425 | -45.67664 | 2026-08-18 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e9d10d1-32d4-308d-b8c5-eb185d18f16f | -14.36222 | -51.87922 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2643dcf0-9509-32b0-8c72-a6599764491e | -14.48736 | -52.99734 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d68435b1-5dcd-3a56-ae41-a286529f0579 | -12.94316 | -56.6425 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db2b10b0-2b25-3e4f-a562-76be5cd06b9c | -15.29525 | -56.44901 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7611ab08-df00-3e60-8fe1-29fee7ac5d54 | -13.42057 | -57.04295 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fbead1a-c8de-373e-95ec-c6770a98d364 | -14.17324 | -53.05976 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 146b06d4-0ef7-3ef7-9a9c-10d42909e87e | -13.40871 | -57.04915 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8dc861b-97c3-3f97-b5bd-fb677d4670e3 | -14.2821 | -51.93462 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8413eb7c-b65c-300d-a210-a243557518d7 | -13.58601 | -51.78144 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d834587e-22d4-3bea-816e-355f31854ff7 | -13.57836 | -51.78442 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f98e05c-1523-3abb-ac15-d1adc687bc73 | -15.30263 | -56.44648 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e5c8217-6800-326c-904f-4a2f077727ba | -14.12503 | -53.65422 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72bf33c6-4bc9-3fc2-8590-b053c5ad8986 | -15.22892 | -57.65706 | 2026-08-18 04:59:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa2dbb55-67ad-3bfc-87da-86726d7e7692 | -15.21472 | -52.8368 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4df4fbd-d7d7-3806-bae9-9fba44a8a311 | -13.58256 | -51.75614 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 410dcc3b-da98-312b-807b-29d82b25d20f | -14.3581 | -51.88277 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0f83d3fa-0ecd-31cb-96eb-c4966c69070f | -20.29454 | -46.47337 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 337b32ed-44e5-326e-9294-f9726ba62a18 | -14.17503 | -52.93442 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fa135ed9-b34e-328d-9033-885b5b1778f8 | -18.81344 | -46.7511 | 2026-08-18 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README46.md)
