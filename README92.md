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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 099f34d9-1b99-3911-84d8-72a6a78bcb06 | -8.9887 | -65.42351 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 238d5b15-4b48-3301-bbeb-805a676d0f83 | -8.58014 | -62.63179 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f55a859-b4b1-3d7f-8747-a827916f6235 | -8.34853 | -62.9288 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 952ce4bb-028b-3171-91ed-95d1f7742f89 | -8.55496 | -62.63374 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9dc64a9-7656-3d45-b34e-1e0febc507db | -10.42497 | -64.3911 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59ef309e-7cd2-3aa2-8e37-37c0d85b4516 | -8.61525 | -62.64886 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fc86345-c672-325b-b152-1bc2463e3dcf | -9.0737 | -65.72532 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3899184c-dd9a-38c8-be82-6a3c68a00ee7 | -9.16776 | -60.77059 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45c7c09b-9a57-3b39-bc26-e0608e998f1f | -10.38845 | -57.69731 | 2025-08-26 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3721a47d-e1e5-3274-8286-e588c26dc562 | -7.38271 | -64.35643 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fa527345-927b-3f5a-9b9e-251be97f6fe2 | -9.04429 | -65.73151 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1774b92a-0aca-3e5d-9f6d-ef48be9825e1 | -14.29243 | -60.35438 | 2025-08-26 06:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06cc3e13-dd4b-34ab-93db-41f22ee0c0a8 | -9.07844 | -65.72074 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ce89a0e2-026c-350c-8d06-c43ea10c9065 | -7.35338 | -59.66848 | 2025-08-26 06:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0330e2a-e0f4-35d7-bfb5-4d02ecd61117 | -8.88766 | -62.47494 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c658e0f-d2e1-36d3-8bf6-0c987370a015 | -9.16405 | -59.54085 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8eb988d-32c5-3971-91c8-d07919d6386f | -10.24806 | -59.11112 | 2025-08-26 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f36d4fa3-ae04-3fc6-bb2b-5b368eeb13ff | -7.79185 | -66.95787 | 2025-08-26 06:03:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08d8a8dc-eae0-3876-a557-0799dffdb172 | -9.24986 | -65.62498 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 579d3cc3-de98-37a7-9b21-a0c05f6a127f | -10.65353 | -65.31773 | 2025-08-26 06:03:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 97d3d2c2-0fc2-32a3-945f-b99db0a3476f | -9.80066 | -64.2562 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 247ab994-2df6-35e0-871d-d6c2d10ed947 | -8.85022 | -62.45247 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| c73f7b25-15a1-350c-98f2-297044bbd0cc | -9.1685 | -59.45771 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b41c15d-878b-3177-b1a0-06f501bfa4d4 | -7.3972 | -64.34638 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35a5eb1b-98f5-3b39-9837-0c8247c18266 | -8.97549 | -65.42888 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28c6baaa-c2dd-35a1-b5d4-4001550581e5 | -8.84031 | -62.44479 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 32.3 |
| c762934b-7c40-383b-b44e-6b4dbd5a4961 | -9.23588 | -60.92496 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 190a34b5-fdde-3cab-9279-608633b23128 | -9.18735 | -59.45566 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab6a0a24-42df-3192-9a0d-533eb120643f | -9.02418 | -65.68903 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dce22565-6f1d-3652-b28c-a7cfdbfa231f | -7.56087 | -63.85159 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ab66592-8cae-3c59-a0f5-cdd31c987547 | -9.18415 | -60.802 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77916d25-144c-3a6e-a8a1-045b8241b7e0 | -9.07992 | -66.06712 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15cc25d9-8a83-3e1a-b69e-a5ad68de10d7 | -9.17908 | -59.51985 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec196169-4fbd-3a18-8f7f-d5659a08e7e0 | -9.07918 | -65.71562 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2a0eb9be-44b9-3f0d-8f42-f3d28067285a | -9.63778 | -59.63746 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d256ec22-71df-303d-82e6-0fbb3d17c5fc | -9.18574 | -59.51604 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9eb43254-8691-3333-84ce-351425e90e2b | -10.24867 | -59.10611 | 2025-08-26 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68b6f045-c3de-34b3-a4e5-1718fc7dec40 | -8.98682 | -60.49462 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff05aafa-559c-36a0-9a47-00deadb6b76d | -9.1617 | -59.55922 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 08be4be9-373b-3284-9cfb-7f16f04bd0b4 | -9.23034 | -60.92418 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 040f2d94-f434-3fdc-aab4-b476b0500efe | -8.86168 | -62.44257 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 54232833-342a-3fc4-83b7-d4b492e30f6b | -9.2077 | -60.92484 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fdd0745-4a99-3811-80d4-7ed30dbbee14 | -9.00095 | -65.39595 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b184b373-8168-351c-8592-1c3fce9a4ab1 | -8.53807 | -62.64789 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66cf5664-778f-30cd-b3bf-d5d51fccf9d9 | -7.50135 | -63.50555 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2897c22d-23c8-3d5b-9fc8-1b685fbdc140 | -9.00806 | -65.40435 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bd9d56e-259d-3c27-a325-de04dec2fa90 | -9.10548 | -62.67377 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fed7c79a-49a4-3de5-8bc3-5a742b570d32 | -8.55421 | -62.63915 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 217bf9a9-a32d-3612-ae67-2e2492071f05 | -8.11919 | -61.46092 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d102d26-be9b-32a2-b366-77a63292a80d | -8.87239 | -62.43828 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6baf7350-c097-30bf-9807-2b45f11fe781 | -9.81419 | -64.28941 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43229522-9863-3e2b-bbda-5c4c54787678 | -7.38064 | -64.35252 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9d81ae35-488b-350e-b7c3-94982aeabb5e | -8.12215 | -62.87977 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f657e10a-7ff3-3a6f-a2e1-77d28ceefd32 | -9.27737 | -59.78648 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 357a21ae-e124-3d8b-a8c4-d5d7ca1bc804 | -10.24907 | -59.66737 | 2025-08-26 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5edb987-2f1b-3efe-adf9-3106cbf64aa6 | -9.20312 | -60.91678 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e702ad1-4060-38ae-b88f-a5c716c11913 | -8.9816 | -65.41512 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17ec6146-5297-3a7d-841c-697fe9dbe89a | -10.40925 | -64.40669 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f61997b8-dc6f-3f03-94e1-59b2e825aed5 | -9.67418 | -67.50771 | 2025-08-26 06:03:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c976a686-6e44-3bdf-9a2a-40699dc10062 | -8.57468 | -63.92142 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c93ebaa-0056-3058-871b-37988e71d742 | -8.34722 | -62.94051 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 377a4ad4-e2b2-35eb-b769-58d639bd4116 | -8.90113 | -62.41354 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6502cf44-aacb-37a4-8557-89103994ee17 | -9.00987 | -65.70294 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccf352f1-5505-37d1-ad13-729614558f3f | -8.55082 | -62.62764 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd0f517c-860b-3735-92fe-df84a2130ab8 | -9.18913 | -59.44181 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e89eccf9-d8c3-3c27-87e1-0a96dd87bb4d | -8.97702 | -65.41811 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fcf69bb-966b-3073-8208-8c5471b41d32 | -7.35923 | -59.66935 | 2025-08-26 06:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb78b88a-917e-3c76-97b6-29c5913a3c79 | -9.00803 | -65.69976 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccfe8a8e-27ba-3687-bf99-99cd2800086c | -8.84103 | -62.44545 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a61a10a7-99b4-3975-a3d3-c53f4047318c | -8.99636 | -65.39895 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 646594e0-2bca-34bb-8cf3-20ef8bfdf939 | -8.99585 | -65.40254 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 695ef952-e95c-377b-a0ff-8090c92a9ecd | -9.01421 | -65.3905 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23c4c577-af1e-3eae-91ac-dd99c847d56e | -9.19275 | -59.6194 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c2d74b6-59d1-3a0e-a9bc-46e5ca79dbac | -9.01618 | -65.68786 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8121a57-c72a-36e1-9c48-5825e6e280af | -12.22414 | -64.23228 | 2025-08-26 06:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4063aa29-fec7-39a6-915a-17cbb4b91218 | -9.07284 | -66.06106 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00aabd29-8967-3ddf-ac94-49625f36f5b6 | -9.1647 | -60.77637 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da9c1f60-64d6-3837-8eed-fda6f6374f96 | -10.38922 | -57.69099 | 2025-08-26 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3326f2f6-f9db-330e-8a7c-4aec38600ab6 | -8.63014 | -67.24939 | 2025-08-26 06:03:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f28f2eb-e9ee-3c72-82d6-1acb9cef8f7d | -9.20263 | -60.9205 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8bc1efc-cb3c-3660-a626-c178b4fce8a1 | -7.29413 | -59.66518 | 2025-08-26 06:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b6f5c4f-7d66-3d7b-a8d2-935fcf3220dd | -10.39507 | -57.69682 | 2025-08-26 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a23520a-3e4c-352c-bc15-36d41bce8ece | -9.33155 | -63.20354 | 2025-08-26 06:03:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fd3b8be3-2fcd-38a4-8820-ff3dc60e4d71 | -7.35394 | -59.66437 | 2025-08-26 06:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c655ebb5-b146-3f47-9661-0bab8f63bca5 | -8.08727 | -70.1897 | 2025-08-26 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79868bf9-967f-3425-a0fb-d2b422e94ac4 | -9.23805 | -60.82402 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7556292-8962-3b98-a54a-be3fde7dd4bf | -8.12694 | -62.87894 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70a98754-6e7b-32a1-ba2f-76e323b2d3f6 | -8.54444 | -62.63776 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5ea653a-493f-37fe-a5f8-5e6314e5c9e8 | -8.81466 | -69.29285 | 2025-08-26 06:03:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94d8d01f-4455-3763-8859-b2661a68ba80 | -14.29724 | -60.36749 | 2025-08-26 06:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7f7e8c0-6cc9-3c90-bef1-4d187280827b | -8.63553 | -62.64619 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff6c7364-dc23-31f7-9fe3-a00b7a9cee65 | -8.91132 | -60.71611 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a2cc431-9ec0-3844-b70c-8fe87078e07b | -9.1736 | -59.51444 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df9b8f46-919a-3a5e-872c-a332f7c35509 | -9.0897 | -65.72744 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ab1845e-e584-31a6-80e0-a538edf7d4ac | -9.20805 | -59.43937 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a6bdd36-f3d2-3fd3-81a6-693b3b07fcfb | -9.17614 | -59.5426 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a282f7f4-3595-339b-93ae-803621d31b79 | -8.34779 | -62.93391 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0a9837d-1f0c-3d05-8fde-a23ddfccf378 | -7.89503 | -63.52165 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8ae422d-658a-3772-aed4-88e42fef1405 | -9.01386 | -65.70354 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75a16f7c-8c80-304b-aa9d-e25905ce0480 | -8.98259 | -65.43726 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README93.md)
