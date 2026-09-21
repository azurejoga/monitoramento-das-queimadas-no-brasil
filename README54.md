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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8e2065b-72e7-39b8-ab13-49cac42c845a | 2.12197 | -50.68445 | 2026-09-21 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9314ebda-1376-3f71-baec-9496db01231b | 1.72183 | -56.12765 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9901716b-031f-38f2-8a4e-6464b1af4274 | 1.54789 | -55.82068 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1379b49-dff0-33bb-a439-48e837625083 | 1.05325 | -51.18804 | 2026-09-21 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14727a60-fa30-3669-a654-6e84f8654c27 | 2.51535 | -50.84946 | 2026-09-21 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cf7c830-e667-3de9-aa41-f0c82a175db9 | 2.12129 | -50.68021 | 2026-09-21 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed9b01a7-9df8-304d-9160-79483680ef00 | 4.70222 | -60.89177 | 2026-09-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cbcd676-42bd-3802-b264-427e2ca634ff | 4.53039 | -60.86194 | 2026-09-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d1562aa9-2793-3ebc-825e-94e348a9fb4d | 4.52301 | -60.86561 | 2026-09-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5bfed08e-c5cc-3996-933e-2a1d8ed70d37 | 1.54898 | -55.80545 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dc2448e-d146-3d24-a703-c6d362f88b0d | 1.21564 | -50.97771 | 2026-09-21 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bca12d53-f08d-3ee4-9c7d-6a432b61b340 | 1.21201 | -50.97828 | 2026-09-21 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 518ea17d-f91c-373c-850b-939281d4eb1f | 1.53942 | -55.81071 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a03da4a-4720-3754-be12-2780b6e9fe83 | 1.54846 | -55.82431 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 660d3208-82a0-3d56-9fea-77355d8014f8 | 1.5428 | -55.81021 | 2026-09-21 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81266d18-9067-36dd-a43a-f6b47442ff03 | 0.26297 | -50.99915 | 2026-09-21 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a020ab7-35b3-3b87-bbde-e18a19688c7d | 1.94145 | -50.96324 | 2026-09-21 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e33812a-0a39-3aec-a134-3f7f7d9637cb | 4.52764 | -60.86427 | 2026-09-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1225c494-cf80-3512-82da-504affe7590d | -6.10507 | -57.68541 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69054bbe-3983-310f-97ee-55bdedd65e96 | -3.47746 | -59.59509 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb7e619c-4854-3301-aa98-f62ab249544d | -2.61725 | -51.73207 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe475d39-fb10-3f13-af1a-b92c3dba6cbb | -1.33062 | -54.66419 | 2026-09-21 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 071b9630-3f5c-3010-82d1-13e9ea315cbe | -3.28927 | -57.86389 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 32605912-9c2e-3bc9-8ec2-64bd26677038 | -3.36595 | -50.44292 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbca4bce-6bdc-302f-8346-40b9f47b1916 | -3.39627 | -58.47318 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b2155d5-b3fd-3f1e-ade8-f142be75d31e | -7.88387 | -44.84194 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b438cb35-647a-3482-9134-17b895c89c52 | -2.97402 | -54.76991 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 463f3946-5852-35f2-a4dc-e40edd6fdb97 | -6.32523 | -59.95039 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eeac19e1-6fc9-3bf9-94f0-a5911f7e84e6 | -5.92938 | -59.94864 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 230364f6-d7c6-368b-b180-0e5db760b0a9 | -6.11778 | -55.68258 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 476846d2-9961-358c-96cd-45651650177a | -6.18312 | -57.74709 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45eaa94b-3954-3ed7-b406-f9a3a4d32e6c | -3.45994 | -60.51768 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fceaa4d5-e426-3955-b084-4f05ab28f4df | -3.07504 | -61.17681 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32c78bd4-8cba-3996-b780-6e152ce83b03 | -5.831 | -53.49224 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be6e914c-b279-35d8-b9ff-87ece377795e | -5.84031 | -53.47793 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 702d0210-6049-31bc-9aaa-c7028e4d727b | -3.07146 | -61.08992 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e447d2f-f159-3e97-a191-4add1952702d | -3.44182 | -50.60952 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e36bba58-7dbe-31b8-a110-1a0b41f9d950 | -5.98344 | -57.76477 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3712a394-361f-3556-a83c-2de3cbfc2261 | -3.33578 | -59.44204 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 675c467b-c653-3bda-a5c0-9f6a69e1af46 | -7.05802 | -49.90409 | 2026-09-21 05:04:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02da73b6-627e-30bc-b780-3199b8dc8b81 | -3.45026 | -50.60949 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2176b20-9f10-3512-b621-8f2d297d76ae | -6.85265 | -55.2646 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc6f2d6c-aea1-3096-a6c9-afe736336913 | -6.12948 | -59.96007 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 771ad18e-eee3-330b-bfe5-ee4f415caebd | -6.56529 | -45.54865 | 2026-09-21 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d5646b3-509d-37a9-bf59-74b76390a070 | -2.19193 | -48.37494 | 2026-09-21 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e68c710f-b3d3-379d-93be-aaaf6dd34d2b | -5.98665 | -57.70096 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4a58d32-ff9b-3eb6-975d-b296ccd5b8c1 | -1.90509 | -45.80962 | 2026-09-21 05:04:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 59cf0b65-5524-3707-82cf-6ef60054fde1 | -2.8176 | -50.46553 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02b09a9e-8b88-3989-8d9b-304211e7698c | -3.44632 | -50.6089 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ff5c5c9-6463-3e57-9500-63d2ad7a2f90 | -4.58971 | -45.16565 | 2026-09-21 05:04:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 020805b4-706e-3fe9-a726-d88f44f81fca | -2.82626 | -50.46174 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a2b1a9d-a6ee-310f-a47c-7642bb1ec653 | -6.7298 | -55.09139 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 676729b1-26d8-3ae9-a04a-dec899f980f5 | -1.90694 | -45.81062 | 2026-09-21 05:04:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2c48c3e6-e762-3622-988b-489cc756535d | -6.30376 | -57.73959 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e439b151-c842-3094-b78c-31838f0083fe | -5.74605 | -57.57659 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bcda5ac-1444-3a64-9dad-08b552a58f95 | -3.05511 | -61.27383 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f709a43-3821-3c54-8f6b-465a9c0acb5d | -4.29889 | -56.2622 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04c477c9-e56c-3622-8cd6-efbf4dce253a | -3.64165 | -58.86437 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e181667f-1c41-365c-a439-736b5de4e714 | -2.82955 | -50.46368 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d78082c3-6189-38b8-9b94-a8536d91ba51 | -8.31133 | -46.00491 | 2026-09-21 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a28c744b-4d45-362a-aca0-e9ac49924fef | -7.05742 | -49.90839 | 2026-09-21 05:04:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89070c00-c7e5-31a7-a474-203aa790af9c | -6.35012 | -57.77706 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22427857-8d03-3897-9ff4-1632cc88cdcf | -5.36972 | -56.05177 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3609fcc7-57cf-3ac7-83bd-f155930bc66f | -5.85466 | -53.53866 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db616b26-f19e-3118-93ea-850f2d2df867 | -6.3609 | -58.28255 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d110ba0-766a-3d4d-8e94-897bfb0b3c4d | -5.88138 | -57.72233 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52872c7c-7540-3c42-a6be-2fad7baec3fd | -6.15997 | -57.71291 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| acd04c4a-41c2-3cb2-a440-e57814dcfe22 | -5.83843 | -53.48114 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96c97140-5d76-334e-951c-6e36b9b23caf | -5.82747 | -53.51523 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a15b898-fd84-33a1-b23e-b24e12a4f5da | -6.28217 | -57.74372 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bd99099e-4322-352f-89fb-8a48253a16fd | -3.45104 | -50.60442 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50a41446-ee00-3b01-a50e-f9c57a0e6e06 | -3.38687 | -50.43906 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 33cfe6a5-ad73-3c77-a8d0-cec34814d0d7 | -6.46969 | -48.44322 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 642a7269-643b-3190-9fdd-3365afb7dc63 | -4.9404 | -55.81828 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d10837c-3750-3faa-834f-f7febd9b5f52 | -6.40016 | -55.2659 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4097852-4b79-3707-8802-ddbeb83676d9 | -5.9793 | -52.19918 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5839ae0e-b711-3a9a-8a87-7a877b4dfd97 | -5.81668 | -47.79295 | 2026-09-21 05:04:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4eca6ad8-5b8c-3f3b-a2a1-bfcf40a3291f | -5.82341 | -53.51854 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddb056c0-1c4b-3101-b765-0c27fd729ac9 | -4.48474 | -55.48907 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02e886f8-01c5-3e1c-9c7d-bb7e3633566c | -7.29649 | -46.76831 | 2026-09-21 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 953fbe16-3202-325a-a535-6c43cc1dca8a | -4.93986 | -55.82172 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40550607-d8f7-3b5b-8cd2-5ad365da3163 | -5.21142 | -56.10469 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9d325cd-c54d-33bb-9b45-b58a888cbccb | -2.94856 | -51.04274 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0673165-1be1-335f-b0ad-2094f0dc845e | -5.83381 | -53.52012 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2120b31e-1245-3560-8bb8-e3dad1b9424b | -3.42196 | -59.19136 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0eb3392b-c34d-3c77-a33f-2bc56d52d84b | -5.63223 | -43.37275 | 2026-09-21 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 548717ab-037f-31af-b1cd-004a79ae5688 | -6.06692 | -55.61818 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23369b6b-8bca-30c5-aa9e-39c69dc839e6 | -5.77294 | -57.58822 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a44330d8-b88a-3ce4-9c92-578f0cae469d | -3.66326 | -54.27226 | 2026-09-21 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41cd3e41-4dd2-3bea-9e5a-868d8d964d3c | -2.91047 | -54.14911 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 385b1037-3a01-3ca4-b6d3-5bf7b96aa348 | -6.16166 | -57.72862 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5b26c5f-baa1-3d5c-af6a-c3ffaf94f9b8 | -0.51467 | -49.15769 | 2026-09-21 05:04:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14db85f2-1da5-3d51-ab42-b1aafec341f8 | -2.97768 | -54.15582 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 457b44f9-acfc-3ee8-845b-a014cd4773ca | -5.83094 | -53.51576 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5e5f8ad-b931-3132-9b98-a09a0ade6573 | -3.38289 | -50.43851 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 76e54c90-50db-3cf2-9fac-7a828a0ba9c4 | -5.82516 | -55.70757 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42f0259a-c89b-3619-a273-a626e6ba5fde | -4.04749 | -44.97025 | 2026-09-21 05:04:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f6de1e3f-6459-3a3e-92ca-460d36c194f4 | -3.00326 | -54.16692 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef64d7d4-446f-311e-a6c2-021af7a1799f | -4.29943 | -56.25873 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0361497a-b2f5-3afe-a86c-053b7d0af803 | -5.42164 | -60.21774 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README55.md)
