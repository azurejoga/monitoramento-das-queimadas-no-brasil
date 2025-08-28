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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34e5e4c4-2188-3fe2-bd76-73d628d75486 | -7.46231 | -61.40271 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8aa7be38-48dc-3f0a-8a63-6e71885ae689 | -7.62681 | -60.84678 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d0aadf28-5305-34fb-b38d-c5a8591528e7 | -10.46673 | -57.9576 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eba30099-cdc1-33c1-8d4c-b3e6fd0f247a | -9.08785 | -65.72407 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa1217a4-e94a-38ec-b43f-4d5eaba4b381 | -11.22089 | -55.05613 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3a862502-57c0-3859-937f-7011596d7036 | -8.96223 | -65.94988 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73c5fbc9-bf4e-3c38-85c6-b05d6a03ad2c | -9.79742 | -64.27172 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1314cb46-7628-327a-95c7-9c5e4304526d | -11.2311 | -55.06946 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6613ffe-72da-363f-8f6b-be92bd4b6c9e | -8.34949 | -62.93084 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 142f7d0d-12cf-3536-8b69-dfeb5f948663 | -9.16722 | -65.8004 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b4fca26-7b21-333f-9aac-663e12ee2243 | -9.47155 | -57.84034 | 2025-08-28 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e015c15e-134b-3125-b185-a418aa943801 | -8.69214 | -63.83872 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| af06726c-a6aa-3a53-aa02-0a4cdf6ca784 | -7.3773 | -64.36427 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 746d67aa-9aba-37a9-8f90-bc97f16b9073 | -8.92098 | -65.92477 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b046e0ff-2833-3527-bf0b-7348d500f342 | -6.01394 | -57.84885 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6943f1cf-d163-3a29-86fc-c111564c280b | -8.94984 | -65.9629 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1972bb6d-a9dd-3963-9f42-b6e5310bd5c0 | -8.09239 | -71.24712 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c297b981-2184-37bf-8bac-7dad254e52c8 | -9.40851 | -60.57141 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 6d24f000-135a-3da4-aac0-11c3b980d5c2 | -9.4755 | -62.3859 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0955e8f0-3900-39d7-a9a1-db0e98b17d7a | -9.40713 | -60.51211 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0496292f-4cc8-30ce-a30a-d7ae055b659c | -11.22579 | -55.0562 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8321531-f42e-3dbd-8d52-4a7a05fbe2b3 | -9.13555 | -65.29062 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 160b573a-ec84-397a-ba5e-189e431d35ff | -8.65785 | -63.84935 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 038ad24b-9aa3-3db9-ad2e-7bbf578510f6 | -9.1165 | -67.70747 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69643d85-e1d8-360b-9f53-2dfded7505dc | -9.28357 | -68.26042 | 2025-08-28 05:48:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59888dd6-8818-39df-9a96-0d9af109fbb9 | -7.34877 | -57.63033 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5ac82c2-5a83-329e-a191-5adb447a2df5 | -9.41575 | -60.51826 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f57e3450-8a28-399c-ace1-528db0cdbdfb | -8.55917 | -62.64301 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3972eff8-4f93-3a62-8f5f-e849faf98436 | -11.22697 | -55.06324 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9750f79-80bc-3469-a445-a43528431f29 | -9.16049 | -59.566 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 659cb38d-78bc-3d98-843a-435389977ae6 | -9.12598 | -65.77171 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0baf94e-509a-39eb-acf8-3b3ab43a6f57 | -8.57054 | -63.93034 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea44d179-99ed-3275-991c-fec1419edc99 | -9.41046 | -60.52244 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9fe6751-827a-3186-9a4b-c53e465f5f6d | -8.96112 | -65.95718 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a15d0c8c-16e3-3601-8f30-4bedf176858a | -9.49626 | -60.54145 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54520e4c-a416-3422-a0ad-5cc9a9a754a2 | -9.1419 | -65.27187 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45ec5200-2044-3a18-8d77-089575dfa312 | -11.22767 | -55.05694 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c0d13fda-69d7-33e3-87a9-1d80906de4cb | -8.89125 | -60.75966 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 638372fd-07ae-3e5f-96e0-668e2e0d64e1 | -9.13507 | -65.78069 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8b0b0a8-3b20-3bbc-ae77-46797e97f4cc | -9.11632 | -65.78921 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0963d6e6-996d-3234-a481-20a52377ac29 | -9.41243 | -60.50793 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b65f25e-bc3f-34b9-9c52-437fe9449555 | -9.5368 | -62.39487 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15be5015-b732-31f2-b9f7-f1135112c156 | -9.40915 | -60.53208 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e2cfc8e-d030-3bc5-a0bc-87ba5c9ea54b | -9.13279 | -65.77277 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8b3a177-36a3-33ec-892b-e898a2d40e80 | -9.1556 | -59.56501 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7f57550-1ff5-3c9a-bb92-8d3f689b11cb | -7.38085 | -64.36481 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c12a5b7-3dec-35ae-b06f-4d84076ad878 | -9.12541 | -65.77541 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a84d630-baa9-3231-8cb4-b4b2d218bfa5 | -9.40381 | -60.50175 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14894ba8-eae3-38b8-adb3-db8ccd1205f6 | -9.48063 | -62.37915 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88ee115c-a483-3cf7-8b9b-267261620001 | -7.9965 | -70.28771 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc463080-2071-3baa-87d6-dc507fcfbd2e | -8.30602 | -70.87034 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a0b60cd-5702-3fca-af66-05f054f9b78e | -8.34877 | -62.93573 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43e9ffce-7db0-3edb-8ad4-074b2c026b22 | -7.56408 | -63.84483 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f068c219-3cea-3792-93e8-f8f8897f61d4 | -9.12655 | -65.768 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4bd676a-e434-3a2c-819c-94327575dbda | -9.35713 | -67.56001 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5531a72-cb07-37d3-a32f-4938952841a5 | -9.12029 | -65.78603 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6de1242e-afb2-345b-a24f-6e8479665bea | -7.55979 | -63.84855 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb836201-840a-3ed1-ad20-fd7e90ccb75a | -9.2565 | -65.90492 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cf9c7d6-162b-3f35-8f7f-c4227fe084c4 | -8.88349 | -60.74928 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91e33560-c42e-38d1-9a3b-215d9f101988 | -11.21828 | -55.06171 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 841eff50-ff91-3e39-9d08-38a93e146ea2 | -8.91589 | -60.71637 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd74ed7c-0a6c-38b4-a2b8-3cb06f29f9f7 | -9.18878 | -60.80871 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e67c9601-3704-3db8-92ec-0d6f3fe19891 | -8.04135 | -70.09803 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 277ef92f-972c-37b1-ae5c-7b020e19d08f | -9.11374 | -67.70346 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8859f099-08ab-345f-933d-99a6dc0ed0ff | -8.87832 | -60.75317 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6cc6681-8d89-3422-86bd-615c22bc998e | -8.90767 | -67.45981 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd3df1ff-5ca3-3774-be38-c5fef41e115b | -9.48828 | -62.38406 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d051fb5-a06a-3a37-aa6f-21b5223ffef7 | -10.47111 | -57.95345 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b318724-aa3f-3f56-9378-ca6c243aa32d | -8.10894 | -71.24052 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 293c1926-1b62-3647-b9e1-fbc093546b94 | -9.14017 | -65.28345 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2504ff5-e7d3-3ee6-851b-08220839567d | -9.17909 | -60.81204 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 469da387-33d4-3db9-8000-8fd6749ce6c4 | -11.23862 | -55.06396 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2f754d1-576e-393d-8f30-57a11b89e28b | -11.22505 | -55.06252 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca6c3a62-a326-3f3c-ba7d-af4fa90ab14d | -8.30968 | -70.87096 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41478b9e-1934-375d-b495-27b7254e6614 | -9.16129 | -59.56018 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb077821-8739-3971-afeb-991657d05d98 | -8.58212 | -70.11755 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 613cbb70-f7b2-3185-9c1e-bd1dfc428c91 | -10.46013 | -57.96457 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 138aae80-8dd3-38d7-8f62-2fbcf99adb27 | -9.13223 | -65.77646 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1406366b-5fb0-3256-8bae-954a8a3e3a1a | -9.41775 | -60.53826 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca3a2215-2780-3c36-b640-3b10bbf4ad27 | -9.40779 | -60.50727 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9744c6e6-2067-3873-ba99-fb7979e8a445 | -6.2462 | -60.01662 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c80183d-5dc1-3908-8a7f-0f8476242638 | -9.40786 | -60.57621 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 30f2db34-4895-3b1d-bfa8-18b72030fe0d | -8.71503 | -68.68826 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c21c4229-791c-3b8f-a17d-39254e8ee7d9 | -9.01642 | -65.70948 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e545ef9-fd83-382e-928e-0c8e767ec4fb | -8.57422 | -63.9309 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d29af5e1-b15a-3b0e-b33a-b40a11a1abc3 | -8.09537 | -71.25237 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d105d56-9c8a-3205-9154-3b1f2dfe753f | -8.74199 | -70.99969 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eb2a9528-0ac8-37b7-affc-21fe551edb43 | -9.311 | -57.69923 | 2025-08-28 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04d8518e-e940-390f-8706-baa19da05a66 | -10.47814 | -57.94264 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fed2a2cf-1d34-3151-a025-cc15328ad361 | -9.10086 | -60.32354 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e65aa9d4-c403-30c5-8cef-a75affa37a0f | -9.16208 | -59.55448 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e752d866-43a9-3db3-a690-f036b42b1a22 | -9.19066 | -67.75472 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17ec821e-bbe2-3dfe-bfdd-f846ddecb3e4 | -9.52606 | -60.53069 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49f5dc6c-e0d2-3cce-a4da-06648f4b935c | -9.12995 | -65.76852 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2614cfa-2fa0-3eb8-abe8-e86f8657abf0 | -9.12711 | -65.76428 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e058d281-1247-347f-9f8b-307e7f771e70 | -8.35199 | -70.84253 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 864ecc28-ab40-3b7c-9b59-7a3c671f6cb7 | -9.40119 | -60.52113 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5960348b-5d74-3468-b324-1962cf4a76aa | -9.79461 | -64.24027 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b54a701-6c9c-36ba-927e-d516b3676c39 | -10.47435 | -57.94284 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 417fb362-75e9-3f27-b91f-8c22df7633fa | -9.15482 | -59.57071 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README85.md)
