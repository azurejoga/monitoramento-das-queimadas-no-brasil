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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66125f87-244e-3b22-a569-d124ef2f9300 | -8.90488 | -62.46011 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b988cbd-35dd-30ef-8a66-d836e2388359 | -8.97753 | -65.41453 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65bde47d-f928-3d3c-acb3-e8c37a5b72a5 | -9.18924 | -60.80651 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c19cbbe-a026-3149-8326-8e32d29be579 | -9.18692 | -59.50691 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 713ea470-f3a0-334b-b74a-9a1c7a6f2c6e | -8.35338 | -62.93095 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9c17867-a413-3963-87a9-32eb748c3220 | -8.97447 | -65.43605 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c633534-7640-3709-b6cc-5c38b0382a02 | -7.38867 | -64.34509 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf281b2e-0bf3-315d-8e9b-0c6bd04a6720 | -9.1856 | -60.79076 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe2b217d-2f0b-3caf-a6db-842324a08830 | -9.04902 | -65.72693 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe92a1f3-11c8-3763-a303-308ae00c84b9 | -9.07045 | -65.71959 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ddc58ad-7eef-3866-8f1e-17c9decc0ffb | -9.00665 | -65.69714 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b01bec7-a76c-3155-8283-1af48f6f0514 | -8.98717 | -65.43429 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c080c51-06c9-388e-aa00-91be44aca976 | -8.98464 | -65.4229 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cb7ba4b-ad3f-3818-b8dd-325a4183da2d | -8.23674 | -67.36874 | 2025-08-26 06:03:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0c11651-1b7a-3851-b37d-6d06d81665ff | -9.25791 | -65.62619 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27533c14-d48e-3f40-a97c-7dedd6514168 | -8.55345 | -62.64458 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5acacb83-7fc3-3ce7-af9e-349a576d8db8 | -10.25555 | -59.10218 | 2025-08-26 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20123f0e-51fe-32b0-8f0f-a99924d50f59 | -8.34791 | -62.93541 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c14b96a1-12a0-3ca8-ac26-04460e753ce9 | -9.16697 | -59.51805 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 840ec159-a6cb-3f19-8528-07417515da07 | -10.01547 | -62.39134 | 2025-08-26 06:03:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 730f35b8-e0a9-3eb2-8d4a-95e7bf7eec1f | -9.01786 | -65.70412 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d346e7f-bc00-3472-afdc-5dcbda54d8bd | -9.193 | -59.50768 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 088292c6-93df-377f-8be4-c398a5abf439 | -8.9041 | -62.46576 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0d102c49-7e19-34d4-8f65-d9073fa4654d | -9.20865 | -59.43471 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a374b009-930f-305e-9e15-41597d2f7a9c | -8.11263 | -62.87689 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d343e14e-cd67-308a-a257-96c63f9dd828 | -7.37901 | -64.35183 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 39de95b7-63b3-38ed-8d76-2511790f43bf | -9.16347 | -59.54541 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8762784e-d0ff-3c59-9e82-1ac15b59afad | -9.27686 | -59.79063 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed5adeb9-a3d0-3d32-a9e7-e5c7b186305a | -9.01675 | -65.69574 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c07d81e-3891-32ff-91cc-8f4d482338f9 | -9.23853 | -60.8204 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b63b591-a9a1-3133-9c21-0d0181080777 | -9.09519 | -65.71774 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c93b48da-d672-3b34-98e4-d91f8997346b | -8.86244 | -62.4369 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| adafc1b3-c5cb-3c9a-b965-bb48feb2fd2f | -10.14472 | -67.67068 | 2025-08-26 06:03:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4221a26-e067-3a8f-a092-a47303d2372a | -9.16814 | -59.50896 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8dbac822-0bb2-3623-80a0-703ea5b7557b | -14.29207 | -60.36494 | 2025-08-26 06:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e21908f-d837-3f6e-9797-4cb772044e55 | -9.15816 | -60.78312 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1ad17d3-9261-3c78-bc14-2a6fb0591d2f | -9.18633 | -59.51149 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 659d7129-af2c-3a69-afa4-8c5c846c09d7 | -7.88829 | -63.01586 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b039bec4-4f99-3bc7-9ed8-8336ee287ee4 | -8.89229 | -62.44107 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9235d95e-9664-3afb-9a07-645bef95fae5 | -8.98819 | -65.42709 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6da5c882-f6ee-37ae-88c5-52e5df014def | -8.98665 | -65.43787 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09b4e390-846a-3fbc-b85d-da2c0175ca61 | -8.1199 | -61.45777 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a364c5c-f5b0-3c59-b218-680209439c56 | -7.37579 | -64.35589 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e425771-cd6b-3b20-bcc5-e0cc36cac2b5 | -8.10236 | -62.88065 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85e5f884-fc81-32a2-a7b4-81a7f75332a5 | -10.42556 | -64.38671 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82e1522d-bffe-324c-b69d-9c617741ea89 | -8.98362 | -65.43008 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27e1e12f-c390-36fb-bb53-8273a45dcf26 | -9.17478 | -59.50525 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6dfffbde-752f-3f8d-9f89-8bed256b7eee | -9.08002 | -66.0638 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dd71a143-5ab5-36f7-9170-0fd683aa57bf | -9.00348 | -65.40733 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 674ec614-a9f8-33ab-bd46-2ed390bea063 | -8.885 | -62.45734 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85294f0e-f571-341c-976a-ebf5435a4dff | -8.34861 | -62.9303 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b3b54ab-4d13-3eaa-9657-b4d27e289731 | -9.15626 | -59.55359 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9cb97768-f10d-37c7-8a0e-8035151b9d70 | -8.84178 | -62.43979 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3a76b5f9-2778-37a5-9b63-7112a8e7e541 | -7.28766 | -59.669 | 2025-08-26 06:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 134155bb-32ae-38f3-acdf-3cc03f71205e | -9.26801 | -56.90647 | 2025-08-26 06:03:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96bd970b-88ac-3ccf-ab97-0ab19915a0a5 | -8.56211 | -62.61816 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 965ebd86-6ebb-3ac6-95a6-77be1b072a10 | -10.24969 | -59.6622 | 2025-08-26 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba057664-de37-3b89-8b15-6ca8387c56ed | -8.97651 | -65.42171 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82a02320-14cf-3a1b-9954-01bf2e88712f | -9.24221 | -60.91533 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d31e2db9-8672-3c63-b502-4c3ea8849cb8 | -7.889 | -63.01088 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b9a681c4-c741-340c-983f-0dd109b012d5 | -8.10309 | -62.87553 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b35763a6-82d5-39c5-baac-3a57dbfeb9f1 | -9.19907 | -59.50843 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c72f47a-d73a-3ce5-97e9-d20555a56e0e | -8.12692 | -62.88043 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2febbaae-87f4-3564-b87a-d4a2ccbaa86f | -10.42052 | -64.39048 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c5bdd6c-af08-3da1-a02c-31ba4d702640 | -8.84528 | -62.44545 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 310b8ffd-a3aa-3913-b2d4-78304b635009 | -9.16116 | -60.77735 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9abdf233-6e43-3a69-8a80-85e4219a7572 | -9.18885 | -59.53961 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c838720-579f-3275-9b3b-8d772f819e9b | -8.54858 | -62.64387 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae958c6a-7ac6-3b9d-b177-69094bb32124 | -9.1822 | -59.5434 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a1956bde-e650-37f9-b0d5-575ed3287f9a | -7.38754 | -64.35307 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a420525f-9c8b-3bb6-a190-bfe61c5c0ecd | -9.00658 | -65.3857 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e21c0a2-2868-3057-8f39-e2373ce3749a | -8.98617 | -65.41212 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11c05a69-1f76-3a74-9168-9a4f0837feb2 | -9.01529 | -65.70614 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a3f2c75-f860-309b-bbd5-4419e5efea86 | -9.67055 | -67.50715 | 2025-08-26 06:03:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eee283c3-be6b-3061-a9bb-afe408dfcca5 | -7.38549 | -64.34917 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50c793ac-bb6b-3796-93b7-f173edbfc1ff | -7.37946 | -64.36047 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1508a415-7095-3252-a50a-0888634cc595 | -8.11961 | -61.45773 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fe8bec6-a384-3f31-9e2f-eee9fe1fa1c1 | -8.55993 | -70.62592 | 2025-08-26 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a8bcc2b1-f84b-3c29-a61e-75f8b314144f | -9.19359 | -59.50309 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 316f6012-b91a-3167-85c4-ef46aab826f6 | -9.27086 | -59.79009 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8861e3d1-9efc-30ee-9d9c-e8046fb4e129 | -8.34245 | -62.93987 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a8420716-1d7d-3317-a9e1-eceb7ca2408c | -9.19182 | -59.51677 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cccf79fe-126a-38d5-b44a-adf565ceb2af | -8.85098 | -62.44683 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 6f4145f6-e358-3b9e-ba86-1eda95b17e9d | -7.61892 | -61.0377 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b8430c7-8adc-31df-925d-8b5993eeb3ef | -7.38698 | -64.35706 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97df3cd3-95ef-3b0e-b8ec-37bc8ea6bed6 | -8.60687 | -69.59304 | 2025-08-26 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d7777bd9-6983-3abf-ade2-c219eec0476e | -8.61036 | -62.64817 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 94d8a3e4-2e52-3f3f-8766-d546b8e81ce1 | -9.0194 | -65.69371 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14136014-458a-386f-91c7-9a0d5a272387 | -9.80956 | -64.25746 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17201000-33aa-3aa9-b049-47a5ea2b5361 | -8.98593 | -63.64491 | 2025-08-26 06:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce3a13f0-49df-3f9f-acb2-be4555cad5b9 | -8.9637 | -68.79763 | 2025-08-26 06:03:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e3ab281-5d36-357e-9509-1bd811262efb | -8.85519 | -62.45317 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1f9d13e5-e96e-3fce-85aa-554e96ff01f3 | -9.09843 | -65.72352 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f3c7ac9-07df-3290-9849-0ecfe3d5c0ab | -8.63077 | -67.24518 | 2025-08-26 06:03:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b40bcb44-f86f-3b50-b962-afb7032c444c | -9.16909 | -59.45312 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7c06bf5-7c9b-3c3a-b83b-6d12fc5c3517 | -8.99482 | -65.40974 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9be88ea0-924c-3b60-96b3-241c5c46c654 | -7.88565 | -63.01209 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0187aef0-2a98-3f76-b198-e3aaf7c8bc4f | -8.35269 | -62.93605 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5a1fe36-5a0d-3cd4-885f-c48f574dd6d1 | -9.07972 | -62.66925 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfc624c2-88c2-3b1a-a346-579f87a21493 | -8.54933 | -62.63845 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README96.md)
