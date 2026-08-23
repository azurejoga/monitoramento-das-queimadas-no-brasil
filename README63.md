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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9855c3af-80ff-3c24-9928-5956844152e8 | -8.70091 | -62.89919 | 2026-08-23 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d3f149b-2f95-3050-9f48-d5598dd22a29 | -9.11542 | -60.33803 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21b40fec-28b0-39e9-ba3c-26b85b053dc5 | -6.7634 | -58.65672 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57b41355-9b37-34f5-8803-f334c19a8044 | -6.76762 | -58.66348 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 574256ae-f230-3e2b-a19a-13bcaba7141d | -6.78543 | -59.43092 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10743aef-2d7d-36eb-a2ea-a9c4ed7d3907 | -6.78339 | -59.65445 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 683cebd2-08e1-3111-a9bc-a9c9d5f6a0d3 | -9.21698 | -60.77218 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7678441-ec34-344d-9ec1-dc939e946bcc | -6.7806 | -59.42664 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2568a3b9-da74-3984-af85-e4c123fc13c0 | -8.93271 | -60.72586 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3398d2fe-607a-329c-a9d7-1773597a8735 | -9.12239 | -61.59094 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e68dfec5-2aea-35ca-b63a-7c3117ee4e7a | -10.07023 | -60.50304 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 672e5bed-7c78-3b5d-9b30-3b40e09729a8 | -10.06461 | -67.55408 | 2026-08-23 05:50:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8bf0f02-f0a0-3298-bcf8-b9e232f76d1a | -7.68087 | -63.34962 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 274faede-052f-3954-8c96-9318c95c0b83 | -6.81424 | -58.65203 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| db9967b7-f34d-3b64-b0ef-23d39ee0d710 | -6.97223 | -59.06539 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9e6dbfa6-da79-3234-8c0b-919488f5763d | -6.76127 | -58.67179 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d4e57e8-355a-3437-a1a4-74cf206fff9f | -7.57205 | -61.2002 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9193e5e0-fd67-3873-aa70-e35f73076c92 | -6.8815 | -59.40918 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09479961-e7d1-33a3-a69d-8e9d4f0b3d25 | -6.80529 | -58.64164 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95fe9fbc-0839-3d3a-9dee-675edc356b58 | -9.12182 | -61.59501 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b0d813e-b862-36fc-a55c-66a809f72da7 | -6.70037 | -58.73823 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98375de5-edf6-31f5-a496-fc066784811f | -8.52907 | -54.81785 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5420034a-47e5-3d3a-bdbc-80271f2b234c | -6.6145 | -58.39045 | 2026-08-23 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ae119a8-5197-31d8-9fe9-c04a164646de | -9.0404 | -60.45185 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9da785d0-1d85-3fd3-8046-4e96a1b462c8 | -7.78424 | -61.43414 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87925e4b-ff1d-3417-bc62-e2da8e5248b9 | -6.76869 | -59.44479 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68c08dbe-eec1-3876-bd95-105e9d890a13 | -6.94025 | -59.07769 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 082b6e9a-dd8e-3d0d-8238-4d3d0ac4d794 | -6.80259 | -58.6233 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8396db0e-60be-38f3-af69-ac97db3b94ea | -7.61723 | -61.60876 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26d84a3f-87bf-3e04-9548-73068c2084b3 | -9.59395 | -60.50965 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66460306-953f-3fd7-8c28-3a8f1849a22b | -6.69494 | -58.74025 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c83c1621-e177-3a69-a876-3970a3c46301 | -7.88505 | -63.76239 | 2026-08-23 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b8ec3c4-bb23-3b52-af01-6da84d7c591e | -6.81589 | -59.66428 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b1a04d1-888d-3f01-9139-1c1550cc6949 | -8.90618 | -60.54435 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b12f552-e413-3e73-a1f1-c4e75ea0da4b | -7.78649 | -61.42304 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b137259a-163b-3063-8688-cbff9a66f1da | -6.80423 | -59.6783 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44e9d543-12f5-338f-8cc9-4702979cdf7a | -6.8294 | -59.67133 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2998ef6f-23e9-39ae-afb5-055310eafb14 | -6.80122 | -62.91299 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f21e6340-168b-3fb4-b00a-65d1b58f7cb2 | -6.80875 | -58.65426 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 02500f07-5499-30db-9eda-57c07ea974a8 | -6.8251 | -59.95667 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f0156ea-ff96-3bd3-8a60-db37ceebe191 | -8.90221 | -60.53896 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 637bf3ed-2b73-35f2-8ec4-076ca6db8a4a | -6.86064 | -59.41718 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c9fffeb2-49e1-3228-99de-41d469c9a8bd | -6.55268 | -58.51746 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 735f062c-2213-3338-9e76-f41ddf7b1885 | -6.79146 | -59.66596 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88bca647-165b-38d1-b16a-8b050cf30636 | -6.88074 | -59.41448 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 57a7c8ff-f28a-3079-8fc6-bae66cdf2b7e | -6.551 | -58.52946 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b0ffb27-9736-3a35-ae32-82d655c12ace | -9.13391 | -65.95591 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 177cef58-3366-32cf-bd90-cc7a6d7e717b | -8.53417 | -54.85499 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9138523b-6696-3b72-932d-9d2a7bad2310 | -6.8097 | -59.67382 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be94420a-9f7e-3669-8e42-d3f7f89bf098 | -8.90094 | -60.54845 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a918f19-5f5d-3688-8feb-05aa485aed40 | -6.7777 | -59.44793 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac10a9f7-5792-3d00-a27e-61fc5058e8d9 | -6.80204 | -59.41374 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cd978bf-e908-3086-a9a9-3c11085b0c9d | -9.14963 | -59.40279 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 179fdfaa-5f5b-3a1f-a03f-c121a8cbba7f | -8.92489 | -60.71532 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 384d1622-2da1-3784-89c5-5efa4267d479 | -7.6262 | -61.60604 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1746b896-c33a-3645-a7e0-e0c9301c8776 | -6.76085 | -58.67477 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d5da6ec-9bee-31fa-a04f-1db17c8f55a6 | -9.1132 | -60.33664 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a80ae088-a6ba-3372-9ea8-ee0c093ba69e | -6.78597 | -58.6694 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d55716f4-ed3d-3402-8865-2b510bd39856 | -6.81506 | -58.64603 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89aa291b-1f10-38f9-84cb-bf7c0e6dfc03 | -6.86028 | -59.02553 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e6ef53e-f663-3256-829f-5b7667211931 | -6.75453 | -58.68287 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02cf8d1d-418f-3965-a360-2fdd949ad16b | -6.86866 | -59.03814 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbba6c78-5b72-3ed6-a451-959851160327 | -9.13446 | -65.95223 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d8929806-8e27-3c59-9fc2-005edb0d26d4 | -7.61749 | -60.97598 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1476ea64-1fe3-3c2d-9809-716662469799 | -6.80488 | -58.64459 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d15f2f27-68fd-3684-8a4e-414e9edfa61b | -7.23291 | -59.62059 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68fabac8-88f2-346c-9dd6-aac463f9a01b | -9.10036 | -61.59169 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e36ec109-d2af-3bbd-aedd-afe248f706a0 | -6.81371 | -59.67968 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5370767-6067-3d83-b0b7-cb4908b3a808 | -9.21357 | -60.89888 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0eb4655-6f64-3c1b-8340-140165b07474 | -6.81991 | -59.67006 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1b470f52-8dd9-33f5-85f4-2d784522f02b | -9.15964 | -59.48188 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bef94b1-c1a3-367e-9e14-716a173c173b | -6.79288 | -59.65577 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8f59138-0786-3e32-9614-10ba52e44c91 | -6.83022 | -59.42344 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b99459d8-da15-32a8-87b7-bd8afe8d5bc8 | -6.80448 | -58.64757 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4db611d-582e-3eea-b79a-245958826b5e | -7.61249 | -60.97964 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 537fe40f-ed50-37df-a134-4e695744e04f | -6.76973 | -58.68512 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34f4fda0-ac0b-3a9f-afb4-d6446ae847ef | -7.56343 | -61.19883 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45714dbb-ff96-3726-aecf-9dd4c0870218 | -6.68606 | -58.72993 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28f627c2-c0cf-344b-ac9b-4ec933a53092 | -6.75918 | -58.68658 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5300db13-ba6b-3b7d-9d61-92d82f76f82f | -6.95737 | -59.06318 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ad6fabf-1dd2-35b2-9132-36b2ba732144 | -6.88707 | -59.40467 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37a563a5-67e7-3a06-8f95-58f85ced4de0 | -9.22091 | -60.77744 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 689aa0dd-4231-3a6a-acdf-223d833e829c | -7.62732 | -61.59824 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e504aab-bbb1-311a-acff-792eeade68ca | -8.53638 | -54.83746 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1be93fb3-10d9-37e2-b6c6-2a742fb93b97 | -7.01556 | -59.60185 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37c5f787-1174-3eb9-bd41-fef611e615f0 | -9.06697 | -60.4306 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46075c63-49fa-3e95-a2ee-a0d3828c0eef | -6.76914 | -58.67907 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34a6fcd9-4ed5-3013-ad20-f62e56aa37d8 | -6.80569 | -58.63868 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d273ce86-cc95-3966-8dea-0c585f3f844d | -6.96651 | -59.07019 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| f2094087-fb3f-3823-9db8-2e78aaa15736 | -6.68646 | -58.72699 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8bba09f1-17a1-36bd-a3b4-36b81ac67cd2 | -6.86937 | -60.01263 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6be16f9e-e35c-3628-b5e3-db99af140daf | -7.68154 | -63.34505 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7be5f3d-7d89-359e-9242-7429e88247d9 | -9.14748 | -65.95799 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f92b1b7-d489-3304-b53f-a3f49ebe588f | -7.66714 | -63.33822 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 444d3bdd-6651-36f2-a7ca-58144dbd1b60 | -6.80792 | -58.66032 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 66d3fa1c-2ef1-3d2a-9e94-0eea37556896 | -6.7735 | -59.44547 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4d97ab0-2b2f-3812-8f4c-cf77642d3000 | -10.06554 | -60.50234 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8580219-b147-3e8c-a2c9-57498259af8b | -9.09749 | -60.92579 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3784f199-a1e9-377d-b214-37c5a89a3224 | -7.62676 | -61.60215 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42e13f75-aa80-3303-956a-5ae478fa2349 | -9.53664 | -63.56691 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README64.md)
