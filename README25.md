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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14fd10f0-56bd-3747-8243-def733a47ecb | 2.70279 | -60.08718 | 2026-08-07 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6c0f6a4-5108-3b6d-a31c-2112e0ed6346 | -6.53091 | -56.54869 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c7c7981-fd7e-3532-95c9-ba1de18b1570 | -6.64434 | -56.41303 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08a7608d-a5cb-32cd-9469-c2373cb11a1c | -6.55144 | -56.25428 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec30f329-873d-331e-b24f-71212ee637e9 | -6.53145 | -56.54462 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5a7d98c-fc8f-354f-b7e1-52de12e06e39 | -6.53727 | -56.54535 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45156941-ed29-3fca-b149-ca339eff2e3a | -2.09098 | -54.44204 | 2026-08-07 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce770629-8bbe-374d-b5ac-0a3d0cdb2de8 | -6.53692 | -56.54827 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54f256c7-82f4-3a98-a1e8-0156a7fb22f5 | -6.54332 | -56.54485 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4dbbef1f-e18b-33fd-8d01-0af3a4537fc6 | -6.60484 | -56.35106 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 649c73e0-e55a-3fb1-a45a-2fbd77f581b4 | -6.55088 | -56.25862 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc7cd15c-9977-39ba-8fa7-5f6935f65cda | -6.54309 | -56.54611 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aebfcf51-2561-3063-9c39-8f77feba4367 | -2.09025 | -54.44696 | 2026-08-07 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea0d6dc4-668e-30ee-8211-da66093c31a3 | -6.54274 | -56.54905 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe47405a-4d29-3d6c-acb3-866d05cf6463 | -6.54364 | -56.54189 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ff50671-b232-308d-a100-5a771e0ca469 | -6.61123 | -56.3482 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 640ee8f9-4101-390e-8483-b196da492a45 | -6.53673 | -56.54946 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 779d7d40-f42e-30cd-84e0-0c4599ed6f6c | -6.53636 | -56.55231 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6005779d-8fff-31fd-99e7-209d606f9e3a | -6.53111 | -56.54754 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fab1742-cc0f-3b60-9f81-add74a12158d | -4.96939 | -62.32585 | 2026-08-07 05:48:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c843b5f-a43e-3f59-b166-23b867437378 | -6.54253 | -56.55031 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaaac3a1-7e6b-38e5-aa60-c9f34d3e8ffd | -6.64494 | -56.40865 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fa48f75-35e6-3ad5-b827-469fd6289bfd | -6.53751 | -56.5441 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a21fb55-e60b-3519-a229-f6fe5c7737d1 | -6.53056 | -56.55146 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36b32eb9-1454-32a4-93cb-bba131daec05 | -6.54391 | -56.54063 | 2026-08-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a83c611-4bc5-3155-90d4-a845cf88b842 | -11.63579 | -59.01154 | 2026-08-07 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 919f3381-20b4-323a-bb28-dc2bb44d0fb9 | -7.03974 | -56.51033 | 2026-08-07 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 875039cb-ca74-3dda-9141-08c41bee1dca | -6.65084 | -56.40924 | 2026-08-07 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe9c24c0-f9c6-3297-a8c0-41b8bc5b35c6 | -6.95099 | -59.51891 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c356357b-bf0a-39c4-867f-40c155bdf130 | -7.03389 | -56.5094 | 2026-08-07 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3b76432-e452-3d17-a59f-a9a7691442dc | -6.95503 | -59.52485 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88a31c4f-2962-364c-8a8a-d01fb2457bb9 | -11.13481 | -54.8987 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f900bd7-4d61-36ab-b901-6d79ce1fcc7f | -6.70842 | -58.95084 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c6dc900-6159-3c08-a3b1-d094c51b4f50 | -11.13343 | -54.91095 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe5b7c1a-f24a-39b2-8623-ec3634d12907 | -6.7257 | -58.93596 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 481ee222-74cc-3970-92a9-96cdcaedb37f | -6.64391 | -56.40987 | 2026-08-07 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea8cc878-7e03-3626-ac86-eb2c11b6b4d7 | -6.86466 | -58.93504 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8095f79e-71ca-39b8-9047-2e5fe40baa14 | -14.34547 | -54.93075 | 2026-08-07 05:50:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| edc9b4ca-40cf-3fe0-9825-83d8d68b89f5 | -11.16709 | -54.85823 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 334b120d-b605-3eb2-8a1b-0816d700a2f5 | -11.17316 | -54.86574 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0d71e3a-fc46-3271-8cd1-6c33de02132c | -9.54761 | -63.67231 | 2026-08-07 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f27d7d40-afe9-39ad-9e7a-78b3a7b0e247 | -12.51791 | -55.78459 | 2026-08-07 05:50:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cffb611f-803a-3208-89d0-37a22fadcdc3 | -10.93322 | -57.17554 | 2026-08-07 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10b7b7e2-91e3-36ce-920d-c22f240d410f | -6.64982 | -56.41042 | 2026-08-07 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 748ecfeb-d337-31c8-8447-dffc0c67b34a | -14.35396 | -54.91745 | 2026-08-07 05:50:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdd9c1f8-f4cd-329f-af96-bdbc9c092811 | -11.14779 | -54.90612 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20678bda-307c-3389-aac5-abf99efe89af | -6.73407 | -58.58384 | 2026-08-07 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d51955f-0911-3b9e-a503-a32e8f91708a | -6.71259 | -58.95707 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eec59bc6-cff3-3953-af4b-494cedd8404f | -6.60119 | -59.1261 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58c58b10-0625-3c21-893e-31213ec1fc27 | -13.62306 | -54.68092 | 2026-08-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0907440d-d8bc-3311-b1c7-206a2727c1d5 | -9.09464 | -61.38317 | 2026-08-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39a3ad39-9e6b-3c20-9964-2f577deeb9f8 | -11.18311 | -54.84893 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91aad599-d136-36ee-ae64-c1ba67c28c40 | -7.75712 | -73.06067 | 2026-08-07 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04d1e249-960d-3942-bfaa-338287ff91bc | -6.85969 | -58.93428 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ad5c527-b9e4-37b4-9465-23eccdf37c3e | -11.17487 | -54.86106 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c31328e4-e6c6-3097-b3fb-0282c2b338ee | -6.73365 | -58.58689 | 2026-08-07 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52b145f6-f440-3653-9235-ec6ee0f4d7cb | -6.70763 | -58.95648 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54447e71-9da4-3d9e-a5b8-b95ac8b09943 | -11.13276 | -54.91686 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3eb5a89c-2e0a-3704-9f79-3ef2daa6fe4f | -6.65628 | -56.40669 | 2026-08-07 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de48ea59-999b-38ac-9476-257ad8625746 | -13.05773 | -60.65949 | 2026-08-07 05:50:00 | NOAA-21 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 247a92d8-9d86-3d89-b43e-197ba47495d1 | -6.72896 | -58.58329 | 2026-08-07 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7d7b598-89c9-3eeb-9e7a-502e52c206a3 | -11.18241 | -54.85544 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 596f5b15-b145-3216-9cd6-e86679ba3550 | -6.86886 | -58.94139 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 851672cb-e5dd-34c1-ae81-1fa039ccac2f | -11.18171 | -54.86193 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48e33010-c433-39b0-a9f4-e1d24b6ab8d0 | -9.49129 | -57.32121 | 2026-08-07 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 026dc480-1af4-33db-ac32-77378e20ef98 | -6.95026 | -59.52407 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3bd1df8-b149-31cb-a580-bd8582311aef | -13.62377 | -54.67408 | 2026-08-07 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 81ca52a5-3c96-3812-8269-4a973145bdc2 | -13.62775 | -54.67815 | 2026-08-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d64ca5e6-84ff-369b-aa18-c0730fd00df9 | -9.18077 | -58.07105 | 2026-08-07 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d14378f8-60b9-38a7-b8e3-5e5ee105b7fd | -11.13412 | -54.90486 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6380107a-de58-3096-9fb6-06de3475c6f1 | -11.18148 | -54.85368 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff1b12fa-ca2b-3df0-87a2-4a1fccfaf734 | -6.5988 | -59.12663 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0f97275-c279-3b65-90d4-ea58da3fd071 | -6.72252 | -58.93119 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7d9e3f3-d0c2-3a0e-abc0-7bd442855936 | -14.33842 | -54.93006 | 2026-08-07 05:50:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd114d7e-7316-30c2-90cf-83ec655e5481 | -6.65038 | -56.40607 | 2026-08-07 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 737a5656-6098-30f9-8fcb-35ec9b7d08af | -10.93275 | -57.17954 | 2026-08-07 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acd30976-d061-3853-b6de-09fcb229c4d8 | -6.7118 | -58.96273 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13cb2c54-3fab-3d0f-b7ea-83d23b83650a | -11.15955 | -54.86356 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e797bc07-fd1f-3cc1-bc31-111ee4344419 | -11.181 | -54.86843 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c55056a5-f9be-32b7-9920-b356c4e770af | -13.62067 | -54.67715 | 2026-08-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80525b2b-528b-34f0-b3f2-0d98f4f760d7 | -6.65143 | -56.40496 | 2026-08-07 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aee68039-7da7-3d5b-8594-6f89db62c589 | -9.0919 | -61.3817 | 2026-08-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5754730-fac5-3017-88ff-178a59108858 | -10.07403 | -67.78992 | 2026-08-07 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adde0b75-09ef-32a9-8c71-d731f5abb90d | -11.13551 | -54.89246 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c791d9ca-4901-331b-8ffb-b7a9168f68fe | -6.72748 | -58.93188 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6b2da83-d973-3e16-b3be-b09b99e3bb43 | -11.17999 | -54.86665 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fc1c6e00-7759-3f04-ae4e-edbea0b754c2 | -6.72649 | -58.93038 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29964491-859c-3579-96e9-3d92450a86b8 | -11.13959 | -54.91752 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf5be5af-a367-3f70-82e6-6e066629fb1f | -6.72153 | -58.92969 | 2026-08-07 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae22ce89-2f91-311a-84c2-61cb606a5f86 | -11.1273 | -54.90406 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84189f12-8cb0-3646-a506-f406e1b0ca44 | -6.64822 | -56.42268 | 2026-08-07 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11f36ff8-65be-31b9-a8ac-3a3eeda733d6 | -11.14095 | -54.90549 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6535049c-3eb5-39e2-838f-afaf93247834 | -11.14027 | -54.91154 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78f53c4c-a039-3ba3-a4ea-54a6f680f8df | -9.09034 | -59.4833 | 2026-08-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c6c9cbc2-6830-35aa-ac41-4c5b00fc2744 | -6.72854 | -58.58636 | 2026-08-07 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88a519dd-e08a-357e-badc-a2a24b1e0e33 | -14.35467 | -54.91052 | 2026-08-07 05:50:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52c863b9-687f-3e09-a805-59e158c62f69 | -11.18222 | -54.84718 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57f0fee1-431a-3dd5-8b35-65c65270a41f | -9.5367 | -63.55944 | 2026-08-07 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7263f1a-972e-3fae-a872-990984d2f3e1 | -6.64763 | -56.42716 | 2026-08-07 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ae71503-0b47-3941-90ab-a330a4d08e4f | -11.91446 | -63.27066 | 2026-08-07 05:50:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
