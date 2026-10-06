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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86af704d-8bf7-38f7-a6fd-d721b212c6b3 | -9.47906 | -66.79053 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69162743-81ac-3773-ac2e-6ab0d5ed1fdd | -10.64198 | -68.59884 | 2026-10-06 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0226bd4c-d9be-3789-b638-88bbf87d19b3 | -10.24655 | -68.30129 | 2026-10-06 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05efa17d-0b68-3312-a79d-a0fd18116c9a | -7.6926 | -72.41928 | 2026-10-06 06:01:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3af90496-980d-3f6f-ba2e-c8979dd360b7 | -9.27 | -68.37527 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b035fdd4-90c5-3c66-9117-2893d112bd93 | -7.91002 | -70.91479 | 2026-10-06 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ab6787e-4f6d-3883-956c-ed1081cc6186 | -9.16428 | -61.4043 | 2026-10-06 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7405ecce-1733-3846-ae79-b8b1fb127743 | -9.11705 | -67.71066 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05bcafcc-fca1-3b3f-a444-3da35ec89e71 | -9.16059 | -68.2558 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c8aa7fa-c780-3a9a-9419-21018344bb84 | -7.44574 | -63.55532 | 2026-10-06 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b499618-77b8-387e-be64-6a9843a9102d | -10.15014 | -69.02391 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5fe153e-2415-316c-8830-de860c9d75e7 | -9.49985 | -67.6825 | 2026-10-06 06:01:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c20162dd-4439-3901-9c2f-fa1a58aca8af | -9.11483 | -67.70312 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdcc0cc2-ff3f-3bd5-b648-9d0133fb606b | -9.00715 | -62.10193 | 2026-10-06 06:01:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83121b90-be09-3d6a-95d5-b039a7877519 | -9.29446 | -65.64613 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a77c7af6-9068-378e-acd6-8c71d59a678b | -9.33964 | -64.71451 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d630d949-c22e-3345-868c-9de09f0a5d99 | -9.09068 | -65.38102 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b30a07ff-f744-3b14-b4a1-0700626f3b8f | -8.85195 | -66.79272 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10b10c02-725e-3eb3-b444-afdf0dba9d69 | -8.60277 | -70.20125 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6761d69-ac06-3cd6-814a-4b7c8bb141d9 | -8.35151 | -62.83567 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3db1f9a8-cfbd-3fbf-8d37-fd0beb668034 | -9.11005 | -67.81038 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f9899c8-c0a2-3b4a-bc3c-fcf64237f1e3 | -7.4377 | -63.55854 | 2026-10-06 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce4b064f-40af-3158-8528-bd9d2857a09f | -7.89283 | -72.35158 | 2026-10-06 06:01:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ae0393c3-9374-3c53-aeca-b5e58ac91915 | -8.62669 | -67.001 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bf0464c-484d-3fd4-b506-5702554b2662 | -9.09874 | -67.69693 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee271fce-1d98-34a2-b603-3767cce5d1b7 | -8.59908 | -67.19728 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c260f326-49e1-38ef-abd0-61739f37491b | -9.11794 | -65.91068 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20a9d7dd-a9f4-33a6-8b10-6a9c9bf5049a | -9.54623 | -65.68839 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40add067-e6cc-3d93-92f5-1721c0085600 | -9.09487 | -67.67835 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54921ab4-06ef-3a0c-b3b5-94cbf7415562 | -7.36538 | -72.60847 | 2026-10-06 06:01:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76bb8c80-693f-35d4-af44-d0b4c27052e1 | -7.44509 | -63.55967 | 2026-10-06 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 548889d8-d6da-3758-b069-061b7fc81f04 | -8.60001 | -66.8103 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bfd8d38-6154-3af7-ab99-9dec6dc2f5b4 | -9.05098 | -65.43298 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba4625b6-5e1f-395a-be71-083a5fcd53cd | -10.44285 | -67.8995 | 2026-10-06 06:01:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9d4caa6-c785-3ab2-a6f0-36aec3b8b5fe | -9.33482 | -68.79436 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fad338e3-648a-3cad-a738-1b68811e6431 | -10.56122 | -68.3418 | 2026-10-06 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b4fb889-b516-3780-83cd-1c047776691d | -9.14593 | -65.41291 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7f8e5da-3a9f-3621-b970-b423b76dd39e | -6.96333 | -71.49819 | 2026-10-06 06:01:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f70ec7f7-635b-3119-9e36-68c8c3731d3e | -8.99391 | -65.40102 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ca1d702-0ed2-357b-953f-3eae124f994a | -8.04859 | -72.4351 | 2026-10-06 06:01:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c9989f9-b982-3dad-adc5-7667cd7fbefa | -9.10313 | -67.9389 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15389f8f-c95c-396b-bdc1-43c24a3e7bb0 | -9.16221 | -67.8476 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe42c2c2-eb45-3e33-a1da-c362f5b8d5c3 | -8.61497 | -66.94537 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2a9dcc1-be17-3196-bd6f-d50db7c49ad2 | -9.09615 | -65.7344 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a93d980-f4df-32f1-942b-494b7faa8aee | -9.02267 | -65.71165 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a138a8f9-71d1-328e-8dc5-7468b7085dc4 | -9.67632 | -66.82501 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88c794f3-7dd5-38b3-b970-0d7082f44da7 | -8.74594 | -72.82661 | 2026-10-06 06:01:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42836c69-9c44-341d-87ad-23f05287abf6 | -9.48106 | -68.0358 | 2026-10-06 06:01:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c00b8113-d8a5-3e62-9bfb-bd88986b1631 | -8.59612 | -66.81327 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2ef2c97-07ad-38aa-9876-2b648f5100c9 | -8.80356 | -67.35928 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ce5ba3b-3ea0-34fe-8866-21c648f025a1 | -9.26665 | -68.37473 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78ca37de-14b0-3abc-8c4f-66fe16248ba3 | -9.13291 | -67.75295 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b388c746-0223-379e-8cf9-e5325a4a00a6 | -9.10036 | -67.751 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0101fda-375e-3510-97f5-24286150e619 | -8.58945 | -66.81222 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d76912ca-7fb5-362b-abd2-ca588be6c6ae | -8.97321 | -65.44412 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faa2fada-7296-31f9-8fc1-ce009ab54fe4 | -8.76605 | -63.68565 | 2026-10-06 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa66cc36-3a92-3c2d-8ca1-01647e361e51 | -10.56179 | -68.33826 | 2026-10-06 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d8dd2e5-739c-3063-8558-a71a4a530189 | -9.10428 | -68.31598 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0f7557b-89c0-3fa8-9972-9e08817eb1b9 | -9.34866 | -68.92348 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 238a1b4a-7cd7-3669-91f5-01c71232f52c | -9.23629 | -67.87027 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38f05654-c864-3178-a628-314250c6b17d | -7.36539 | -72.46024 | 2026-10-06 06:01:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e800db62-4ddd-3d95-b03e-539140c1e3eb | -9.6805 | -67.07188 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cd25ff6-b4c5-3f94-ae39-700172db76ac | -9.34321 | -64.71503 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cd4e1b0-08c2-3ec5-9294-c607f4d6c34e | -8.59557 | -66.81678 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40fe83a2-c858-3758-acdc-aa3568f273ad | -9.11769 | -68.31815 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05a9d8bf-00c0-3f3a-a095-dc101d7d6ea5 | -7.67808 | -69.95525 | 2026-10-06 06:01:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca5879a0-f98c-3301-a635-234cf125c7b5 | -9.1314 | -68.2112 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25f64cd4-6651-3272-bf81-1e55cf9a59ae | -8.64264 | -66.8564 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cccfe3a-f609-3655-bdb5-18c23b60b061 | -9.10706 | -68.32008 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f326a508-7660-34d8-a849-f1f39019e57a | -9.49206 | -63.95395 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7954fa1-3ffb-3877-94bb-c3d42f5bc9bc | -9.7221 | -65.08703 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cda9bab2-2c73-32c8-b98f-34037b1acb67 | -9.11372 | -67.71012 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfb53f65-0e70-3bd8-aa8c-d826dab4497b | -9.13197 | -68.20767 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fb1cc6d-2e0d-3801-a02c-08eae210e7b5 | -13.51814 | -61.11716 | 2026-10-06 06:01:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4166abcf-6d76-3c51-b2f9-046da9e546d8 | -8.63161 | -69.50022 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b7cdb59-32bd-32e7-9b2c-f31ff27f0d04 | -8.85529 | -66.79324 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1060aa9d-9cf5-3944-a4f1-e518dbec794e | -8.6234 | -69.50672 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a3dbb25-5b82-3193-8d5a-21d432614cef | 0.44057 | -60.53541 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 938ae0f2-95b1-3c7e-8509-bd788c95f4c1 | 0.44278 | -60.54448 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba91dc90-e146-3e1a-8cd4-bcefb32cacc8 | 0.44128 | -60.53503 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d68aee27-7d51-3a30-8100-796ee4645196 | 3.12368 | -60.56266 | 2026-10-06 06:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe931119-50db-3cd6-b33f-6fc0d124cfae | 3.12443 | -60.56693 | 2026-10-06 06:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfa6b635-72c5-36db-90a7-fc92b08dc18e | 0.32009 | -60.4446 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95f36440-4c55-3915-9b4b-11abf9f60179 | 0.44213 | -60.54483 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9fe264e7-12ef-3c8f-92d7-13192e975437 | 0.31836 | -60.44172 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 270ff41c-6a01-317b-a7d2-fc517703b9c3 | 0.44818 | -60.5387 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5d3c1c87-2d77-31c9-a37a-623aa9984554 | 3.55974 | -61.33846 | 2026-10-06 06:18:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e77f5aa8-4127-31fd-9f7b-2d77e9e7ee9a | 1.98395 | -60.61863 | 2026-10-06 06:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7970281-8850-3139-9535-44ca7f6c2754 | 0.44893 | -60.54345 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ab1c9efe-25d0-3f55-9508-4f62f8ca15b3 | 3.12744 | -60.57451 | 2026-10-06 06:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95af15e0-23d3-3061-86ba-988b4f406c1d | 3.12816 | -60.57878 | 2026-10-06 06:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d6ad6dc-9bbc-3052-8a12-b7fa83277092 | 0.4475 | -60.5391 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2be8d62c-31db-3e90-9fcf-34e45f2ae740 | 3.12673 | -60.57024 | 2026-10-06 06:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59709854-15ed-392e-86e8-b96430d06627 | 3.12665 | -60.57969 | 2026-10-06 06:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9043f736-542b-36de-832a-492ad3e66781 | 0.44743 | -60.53397 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ed35816-eff1-3f7f-8ed5-46c07b2c0e4b | 0.31915 | -60.44653 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f130cd1b-d659-34ea-bec5-af3c0bb1bb5b | 2.00995 | -61.09055 | 2026-10-06 06:18:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42898bcb-6bd7-3de4-a591-aecaaac69166 | 0.31933 | -60.43978 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac6cc2de-c39b-33f6-b674-99ffbcc09a39 | 0.44828 | -60.54382 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 374b8fe0-8d16-3666-889a-f1d5c7a01084 | 0.44672 | -60.53438 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README76.md)
