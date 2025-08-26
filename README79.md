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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a2909e7-aae9-379f-abec-290318e0f398 | -6.77119 | -59.66851 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fd5b8793-4c73-38ee-8978-f206c2fd0622 | -7.38797 | -64.35075 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9998b82-b7a4-3da3-b69b-db0ca562fcd3 | -7.90133 | -63.52231 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b38cdd3-1087-308d-a23d-956724c76aa8 | -7.05174 | -59.1973 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd2f5dc2-f97d-3a19-b5d6-1dd0c8d346ce | -8.12181 | -62.88117 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30cd97ff-3768-3504-83bd-728cf8378ba4 | -6.25509 | -60.01622 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8108093-9d03-3511-a35b-9543063e0472 | -5.30288 | -60.19757 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 71202020-1f00-3350-9349-8ba842313f74 | -4.96593 | -55.82476 | 2025-08-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 58d55dad-5fc4-3f8e-b343-97fde0ade7e2 | -8.22078 | -61.41667 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35210130-74c7-31f8-8a3a-e973b2cd0a6f | -7.65882 | -61.47335 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7aba8bd-0794-31e9-b5f0-461168ccc6dc | -7.48223 | -61.34905 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2856992c-91b8-3427-85ec-cf3948a3e86f | -7.40174 | -64.34937 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb78b319-d899-30cb-a23c-e36c1bced38a | -6.63276 | -58.55294 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66ceb264-6f6f-3bc9-9aa8-655460c08fb6 | -7.44003 | -60.61798 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f8f46cc-cf12-3750-aa60-2868e79b8433 | -7.89869 | -63.5178 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56bff018-326b-3f0c-8ad6-dccb31c25695 | -7.65926 | -63.52704 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4039df48-bbed-3a27-9c48-70a673cc5bea | -6.26039 | -60.01481 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9260e34-bbbd-37f1-8bde-3fad33c7f574 | -9.09735 | -65.71541 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c0615c8-7b91-318f-9d81-6ae4f37ffa23 | -9.02044 | -65.38974 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4285112-9215-3d9d-9efa-786726c7e2ef | -8.56935 | -62.6289 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d41a335-f4d0-3015-997f-ba908f1b33f2 | -10.4174 | -64.37822 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc37a5a0-7985-3af9-a835-d5087bab98df | -10.41962 | -60.30451 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b76d6fc9-55b2-3b96-9a26-c0bfaec1478c | -11.30192 | -55.1082 | 2025-08-26 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5d7d406c-13ce-305c-a759-0daef689e57c | -9.82382 | -64.25864 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9b382b8-c503-38bb-9ec8-68dd6c1ceb23 | -8.99321 | -65.41075 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a2a58354-8517-3571-abb4-c18416f93548 | -8.87944 | -62.45846 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15213001-cfab-3085-bcd7-89accf6e6e71 | -10.03523 | -59.35755 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 781cc6dc-5f2c-3a37-865a-7d34023a6f74 | -9.20291 | -59.50895 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f94227d7-53a8-3f2e-b079-30752cbbfd64 | -9.02022 | -65.71035 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0834ecd1-c064-3a88-a4cb-9b44118d09f4 | -8.77242 | -64.1092 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b44916f7-e472-3682-b493-2d1e8ba70627 | -9.40241 | -60.54464 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 470723ff-fdef-3c8f-b207-d414556a8b74 | -9.19088 | -59.53603 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41e61aee-9267-375c-a6d0-c5b60c5ffe2e | -9.17831 | -59.509 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30c0c060-a02e-3936-8eed-e582310d181a | -11.31256 | -55.1137 | 2025-08-26 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec3bb570-1f28-3559-ab27-fed0c10487c4 | -9.18181 | -60.80383 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 674d7441-cefb-3ee6-9fb5-e96cfe5537a9 | -8.54388 | -62.63626 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 208a6e7b-5367-3666-bc8b-0cd5245c5283 | -14.11931 | -53.97947 | 2025-08-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a4ba726-45e3-32a3-81fd-40e50400b870 | -9.17479 | -59.50482 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1b666c5-0d29-3e46-8985-7ca9e1a953a9 | -8.58611 | -63.95158 | 2025-08-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3381165e-7766-3eeb-98c4-547ce2361e9b | -9.80673 | -64.25953 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43e87349-8c09-3e67-8eae-4bb63ee49ce1 | -9.16351 | -60.77366 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f02e2523-9ecd-3131-bb85-3a444f2a6dcd | -8.35509 | -62.93545 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00c922b5-9116-3067-bb17-31f686abe56d | -8.6372 | -62.64626 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4535433-4850-3502-8f53-aa93c74d912b | -8.59247 | -63.86698 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edede3b1-d074-3c2d-8c9b-cdfb9bbc9688 | -9.19587 | -59.50071 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db9e3078-a072-3b5d-aa9c-2d1fe9e4350e | -9.17877 | -60.79881 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee9d634a-e49c-32c3-a64b-a8aa92085a7f | -9.33049 | -63.20316 | 2025-08-26 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d63ac3aa-4239-3354-bc01-65d03b95fd6a | -8.63664 | -62.64994 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 573d085a-93b8-36d2-a12d-e64a236d6bf5 | -8.86625 | -62.42954 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9d8212f-db8c-3371-b536-b94f6798cdda | -11.69506 | -60.17752 | 2025-08-26 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a912dc49-dcd2-37fb-ac7f-edca2263fd38 | -8.56028 | -62.61993 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa00e71d-1ed6-34fc-90b7-eb8f007cae74 | -11.0583 | -52.00868 | 2025-08-26 05:38:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4dd282f7-2022-3164-9e9f-532a13fb56f5 | -8.88 | -62.45471 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bc81aac-1b06-3941-90cb-2f34e1615761 | -8.86287 | -62.45208 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8ce112e5-330c-307b-bd0a-53ef30b9fe72 | -8.97262 | -65.43285 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95f486f8-8dc6-3ab1-a1ad-2d355e3a235b | -8.60945 | -62.64576 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4780c388-4cde-3c3b-b103-6b04785ed3ec | -8.57941 | -62.63736 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90e75997-51cd-3709-a409-571e07b572ef | -9.23541 | -60.91826 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9d74b938-5c66-3eb3-bfc8-c0b25ab1a290 | -9.16965 | -59.45337 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 490e42dc-642a-3295-8819-85631d04a3f1 | -14.30823 | -60.37995 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93f864c8-268d-307a-a069-2bddf0a4eabf | -9.06599 | -65.72505 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0333314-5a68-307d-a3c6-72e1ab649206 | -8.51582 | -63.87991 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccf4381e-a83b-3fda-a730-309019e001be | -9.18111 | -60.79689 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab3bff78-3708-3059-9791-25100d23978a | -9.19516 | -59.78969 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4459f54-dc61-3991-bf01-d9890b00a5cd | -10.74226 | -60.72009 | 2025-08-26 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b971e1e6-0977-3dda-8346-f6be1a5f6322 | -9.81852 | -65.16176 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 92b95e06-57ea-375e-bbea-867a851286bc | -9.19539 | -59.53308 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f0643a6-9d2e-3875-811a-fadc14d87098 | -9.20141 | -59.51951 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a912454-0507-3377-9d2c-335deb68b7ce | -9.18286 | -59.53483 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 031669f0-fff6-38f4-bced-b428d952e19d | -9.18314 | -60.79491 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb58e270-41eb-3fc4-b11c-6bd77d8c824e | -9.18584 | -59.51369 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c8bfdfe-247f-3d5b-9478-68e0fc68a497 | -9.18208 | -65.54993 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32c888be-46de-3474-b557-02d426fbb7c5 | -8.91322 | -60.71733 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90ee9658-7d16-3852-9916-d79c8f77261d | -10.38647 | -57.69158 | 2025-08-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2c0c12c-b804-361d-afae-7f67f43f968b | -8.86742 | -62.4451 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ddeb15e-76b5-39eb-a9d5-cc90492b5f5d | -14.28955 | -60.36438 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6705cbf-50e0-36c6-857c-25cb56064bab | -14.40514 | -51.93793 | 2025-08-26 05:38:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f9371b6-c8f4-3bb6-9d88-2731ec017fc2 | -9.17232 | -59.52247 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5f8b60b-4a1b-3908-b05f-fc42ff456e29 | -14.75789 | -59.72282 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d3bcb68a-b226-34e1-9650-ee8068585453 | -9.18986 | -59.51427 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 095f8bef-5ce7-313d-a166-95981d8e1bb7 | -10.82595 | -62.4427 | 2025-08-26 05:38:00 | NOAA-21 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 568d499d-4ae2-3103-aa6c-02d0b6ba9e23 | -8.9095 | -60.71677 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e8b47b1-7f67-383c-b363-a05b4b918c1c | -8.9257 | -62.431 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ea6ebe-ee9f-3639-b7ef-12d4c9d6db11 | -9.19289 | -60.79412 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7b89d00-5ea0-334c-8c07-d4140eac6634 | -13.04093 | -56.84597 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66bcfab5-28b8-3316-bffc-88e5614c4987 | -9.18174 | -59.45517 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6be07b42-7fee-3375-9a2a-c202962155b5 | -11.54972 | -52.11537 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b8fab2d1-d1c3-3267-8c3f-c9313572d8bd | -10.52094 | -57.97821 | 2025-08-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8fa5a3c-3794-32cd-a92e-75f448a4c1f7 | -9.17821 | -59.45099 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 75788dce-a0d1-3ed0-8276-3a268856557e | -11.55784 | -52.104 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66cd6b6a-765f-30bc-8965-6a3f2f518cb6 | -14.7531 | -59.72626 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2d8f358a-d87f-3af6-9c17-64bf84579bb7 | -10.65115 | -65.31847 | 2025-08-26 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| da68bd0d-a59c-3826-9713-42150e5e388a | -11.70001 | -60.17113 | 2025-08-26 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f994296-cb64-3d02-823a-fba7683b3bbf | -9.01213 | -65.37756 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43d39d5d-0569-34de-9d9f-ebdfead2f7d6 | -11.5544 | -52.13432 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14027585-96a3-3ef7-9627-9c7eb1f4ea10 | -9.15686 | -59.54527 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 91e4360d-c6dc-3812-9147-2e84ee979b4a | -8.35117 | -62.93853 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 97e90ebb-e0de-3368-b555-7d3e5dab1dde | -11.57599 | -52.12461 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1769f1e0-6db1-39d1-88c8-7efbf2b3f586 | -12.34045 | -64.22907 | 2025-08-26 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58c7ed43-d83d-37f5-a729-0587ab2c79c3 | -11.56389 | -52.11095 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README80.md)
