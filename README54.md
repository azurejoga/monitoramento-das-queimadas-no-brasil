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
| 285ad64b-70cb-328c-aee7-48849963c3b5 | -2.78031 | -54.08797 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ae74d326-5d98-3620-a9d5-85d93fe1f0a5 | -4.77377 | -50.81253 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c2fed7a-82f8-35e2-a0e2-6283ed771485 | 3.06652 | -60.58913 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f771b5a6-7f62-35c6-99b6-165236024643 | -3.15108 | -50.44446 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c43424b-f30e-3be7-b1eb-3e724081408a | -3.23072 | -54.34533 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ddc0b32-bcdf-32f5-9902-b326d94a67fa | -3.72782 | -55.48098 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c4710d4-7620-3329-8abb-217f44a780a1 | -3.08552 | -54.15924 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bd5f446-4245-3a69-8147-e054b0ada51d | -8.76647 | -62.62284 | 2026-10-06 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14596c73-04b9-307e-b937-146bed54c04d | -2.77286 | -57.68032 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe8177da-aa1d-3fdd-9569-1d6d3a260ac6 | -3.054 | -54.16684 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31f2a9ac-5a0f-356a-888b-4a62f32315fa | -3.12158 | -53.70219 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a4a187b-ec22-350d-8993-b9d91c5043f8 | 1.03284 | -59.44832 | 2026-10-06 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95807ff9-3387-33a1-a977-caf575607303 | -3.51054 | -51.67669 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 314e9d13-972b-3b3c-a16b-92f6221a0138 | 0.30217 | -60.43983 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 793feda2-2c14-3595-8407-4e5f23f7f0b5 | -3.01193 | -50.4701 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d40b0f2-c692-379d-bf4b-5c001fe93988 | -2.37034 | -55.26956 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6380d5c-5078-35b0-bae2-02d40da27495 | -3.54178 | -59.48654 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd4dc525-9398-3f61-824f-6f1ff21e1a0f | -3.08529 | -54.24836 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8359ba21-3b61-3fb1-a90c-58a00f354933 | -3.09139 | -53.72147 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f5e2de2e-7bb0-3560-9020-1fbb1be95934 | -3.84015 | -50.31687 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ff6e1a7-050a-39aa-b618-71c15be1333e | 1.73488 | -55.61519 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d17fe2d-9b4d-3c2f-b6d9-cf45c8835473 | -3.3535 | -59.4959 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 45af6c19-4426-3f61-b549-a5990cb56449 | -7.36244 | -72.60693 | 2026-10-06 05:23:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d464fb6c-8445-39b8-b667-cc58aa453f29 | 1.15451 | -50.74538 | 2026-10-06 05:23:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cef25cbe-0ab3-3c42-8c4a-d833b08b76f1 | 3.56427 | -61.33591 | 2026-10-06 05:23:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bbcbf83-e4d8-380d-af89-93de4f9941fd | -3.07685 | -54.24703 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f6fcbf96-b6fb-32c8-96aa-8eee4b939730 | -3.09765 | -54.16535 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 94d0ca59-48cb-362b-91b6-ddf15d49fd37 | -6.48645 | -62.86161 | 2026-10-06 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86db3e1c-5d3f-33dd-b034-a732b45848d8 | -2.99975 | -54.18399 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1ed111d-b5f8-33fe-819c-6ef7d2bfb63d | -3.37471 | -58.1938 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57f80cb2-52ba-3509-a935-a6f1a063cb36 | -3.07099 | -54.16943 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3b1c43a-f186-3da1-b66a-b312c0fb4e14 | -2.87727 | -54.16284 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b884acc-2193-3fac-9782-de77e20a44e3 | -3.08185 | -54.15466 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43d21866-5ff9-35f5-a690-f750b13a5678 | 0.44717 | -60.54025 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ac1bb5a2-1a0e-38e7-86ce-00445f39ccea | -1.61779 | -55.11933 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecd3190e-13a2-3e7d-b2cc-411b770d712e | -3.50979 | -54.61851 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a447374-8ebb-3600-b7f4-d04ab753f558 | -8.77091 | -62.87595 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0811b27-e63f-369e-9848-e88805cd1aa1 | -2.13449 | -56.695 | 2026-10-06 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0234f06b-727f-3cf6-969a-90376df13ef3 | 0.44436 | -60.54431 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb0204f1-23ce-39d4-8e8a-da57ddd8f374 | -3.05669 | -54.20776 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6b535753-5363-35b5-a836-a3b33f267112 | -3.14164 | -53.71836 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c0c6a33-c9ed-3939-a4cb-7234fe2f9bc3 | -2.87535 | -54.14664 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6d72b474-683d-3791-9c1a-62d82d284270 | -3.04991 | -54.22425 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a1ab861-4d95-3def-a512-1f2b4d405da9 | -3.72839 | -55.47864 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c32d8ef4-1756-34b6-88f5-d9c00f2d2066 | -3.06 | -54.24411 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 18d93885-42d9-3e3d-b1d1-517ae7d6f071 | -3.07759 | -54.15408 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fc1c171-17f2-37ab-9b4a-7630f9aee8da | -7.44954 | -63.55941 | 2026-10-06 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f9bfaa0-e3cb-3914-8cc7-6e0395f10ef7 | -2.77913 | -54.09587 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40fc453c-c97f-3558-9e36-d926387a0525 | -3.67762 | -55.95493 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b75da8fe-8b5a-3365-bb50-c7f0349bdd42 | -8.77429 | -62.8765 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0c0d618-5aa0-31c1-8de7-028ac8ddc27b | -3.06424 | -54.15621 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14863e08-0a1b-3928-8b3c-577e5f8d3db1 | -3.12973 | -53.70782 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d272c0e6-ecf5-3d50-a01e-ee64fdbde5b2 | -8.8256 | -64.22874 | 2026-10-06 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dea9717-2ad0-3812-81be-a9795fe195e2 | -3.25315 | -60.72707 | 2026-10-06 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 577d8b8a-aafa-362d-ad77-4b9dc756f714 | -3.07405 | -54.1781 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 439744f3-b9bf-3cb1-9208-c7901a15dd9e | -2.87667 | -54.16689 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ede4ceb-ca7f-3130-99b8-36a47c0fd465 | -3.07991 | -54.25552 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 84debaa8-69b2-3fce-aae3-41a7024986c4 | -2.43985 | -58.01944 | 2026-10-06 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddbf092b-1ac0-3c02-8a27-fc231a7739e9 | 0.86442 | -59.70024 | 2026-10-06 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29733d14-0f5b-32a9-950a-ce4f93a6b243 | -2.77371 | -54.10312 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 047b2dd2-5685-3bb2-9350-6edc50f2a7d5 | -2.0692 | -56.8559 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d3bffa02-db21-3588-86e3-307bf0ae5501 | -4.77925 | -50.81345 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 929fa546-03d2-3877-9872-aa3dec2debb9 | -8.76727 | -63.69073 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dcafa25-35bc-347e-962b-ffa95d6b8f68 | -2.77606 | -54.08734 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8d691753-d518-3e87-9de2-2fc967ec746b | -3.00683 | -54.13678 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e917bacb-6db2-38a2-b6ee-3252245034ec | -1.61751 | -55.11749 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b352a226-b96a-3970-901e-1a8934357795 | -3.00396 | -54.18478 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39a9a536-f670-31ef-bf75-e0bd7a1e7510 | -3.38738 | -59.4304 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70f88a07-b77c-3e49-80b7-1cf979e0a2d8 | -2.99517 | -54.09826 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49fd5d02-3cd7-32d7-8df9-6ecf11eec2f7 | -3.1687 | -50.44173 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11b5e139-32bf-31b0-99a5-b0b6204e7a3b | -3.49302 | -59.16623 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9092d0d3-8a0e-30d7-b597-7f1b625d316c | -3.13977 | -53.73109 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36e6aeae-fcac-3a75-beac-d0fb7ecc2b81 | -2.93467 | -54.12751 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d4a1348-baab-35be-bfbb-dd5ecf8ca5eb | -2.99457 | -54.10226 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 178f1e3d-184c-3747-8020-2c327ea55eea | -3.37811 | -58.19433 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16187135-3a21-37ee-85ed-8eb95409e2bf | -3.10632 | -53.7411 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80cf9562-c2df-3c66-afc7-6c8e7adf8ba8 | -3.10003 | -53.75308 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8019d397-2710-3b3d-99d8-f9adc30fc6b0 | -3.27737 | -54.1777 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6151748-1b15-3755-8cbc-122a01ae6e3c | -8.82205 | -64.22814 | 2026-10-06 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c19e1a40-c105-391e-bc0b-7dd6b0e37eb1 | -8.7663 | -63.68664 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36ed5d94-4e36-3dfd-be14-1cf5a014e257 | -3.02593 | -53.89118 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| f67a93e2-f705-398b-a1d7-d440e4d90164 | -3.06422 | -54.24479 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| faf6f31c-3f15-37b6-9164-9bcf2b515058 | -3.91222 | -55.8885 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 122b41e5-938e-3ccf-8926-681715d31fdc | -2.83504 | -59.24204 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 513410c3-7667-3b69-be6b-33035637b3f7 | -2.99279 | -54.11424 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cddd59f5-716a-3f2e-bd5d-b33205bd60a3 | 3.12687 | -60.57241 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fde6706d-2e72-3596-aa38-d9dc0a2926a7 | 2.73695 | -60.25453 | 2026-10-06 05:23:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab7b828b-2f92-3ed3-acce-63ff62829f55 | -3.51336 | -54.62289 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2eff0833-2885-3572-80dd-d0e96fa380f7 | -3.68074 | -55.96016 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c182c02-f8c2-3ace-9d0f-684eee9689a1 | -8.34321 | -62.82622 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f264a356-3423-3f99-ad83-c7b8ebc85b75 | -3.05999 | -54.15558 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7edc9a74-96ad-3612-9dd4-de6bdb4fc225 | -3.12911 | -53.71207 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46412e2c-f455-324b-b501-8c99de32ecd0 | 2.01323 | -61.08723 | 2026-10-06 05:23:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b0fe0a93-6c7c-3739-a65e-d4822836b498 | -2.15347 | -59.22446 | 2026-10-06 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e56da81-2420-39e0-918d-e67c333ffbd5 | -2.77972 | -54.09192 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f24c5f54-45cd-3556-aa15-d1f8a40e8703 | -3.10647 | -53.71073 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bc67a47-52b6-3403-a494-4085d9bff43d | 1.72239 | -55.63701 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82a97c2a-8f61-3725-9956-6ca5e748a0bc | -3.38095 | -58.19852 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 577c05a0-4a19-318c-80cb-52d64c75c570 | -3.09401 | -54.16059 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 50a0a9d8-e0f8-34c8-84b6-0c87e4c695f8 | -3.66924 | -54.54453 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README55.md)
