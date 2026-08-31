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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0a9f61a-c6e8-336b-8703-8aea7960f3b8 | -11.69879 | -47.60655 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81ace7a0-1b60-3bb6-a32c-0d55df90836c | -8.81532 | -49.16809 | 2026-08-31 16:50:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 29c3278a-1e4d-3b46-8658-01f7218cb33d | -7.64473 | -46.71365 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ec581f2-810f-3a53-af48-8e07c17e0e89 | -12.95819 | -45.93604 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| acc29491-68a2-3417-9785-47866df061f2 | -8.93665 | -60.71852 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2d4a4039-e0cd-3bb0-9e41-94755909f863 | -9.19693 | -47.9999 | 2026-08-31 16:50:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 8709b4ef-b924-3807-99fe-86c5b7e3ee7c | -8.63257 | -47.46896 | 2026-08-31 16:50:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7556af4c-ebce-3692-9491-9e2d9881bc79 | -9.59606 | -47.61802 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3d975df8-8d96-37ed-9322-e1270e7949db | -5.9011 | -46.13435 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 58b4068e-46cf-3e66-8a7c-2f0a2fd9854a | -12.10595 | -47.27568 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| feab4691-c54c-3379-9e3e-bb70be1dacb1 | -7.55358 | -49.6858 | 2026-08-31 16:50:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 00178f74-aeb7-3552-bb3a-4d045f050dcf | -10.12942 | -50.30664 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c4ba2478-7db7-39fb-b990-a346b40dc199 | -9.42847 | -45.68242 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 3c52f19b-fb0e-3b84-8c2c-14c37b47769a | -11.48672 | -58.51278 | 2026-08-31 16:50:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 4d50e73c-e550-38ef-ae1f-7975820df225 | -11.71527 | -47.62554 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58cceae3-dcf2-383f-82eb-4a5167739a85 | -8.80256 | -62.50737 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a87f60cb-ade9-3910-98c7-30362854ceda | -9.23704 | -60.25815 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| de7a8060-f13b-3f35-a4a5-2412cb279b4c | -8.17758 | -54.93256 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 6b7182e9-efbc-3378-a283-204ce38b06bf | -9.42802 | -56.97841 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 51e2512c-5553-3695-8ef3-4465570c4c32 | -11.22301 | -45.10715 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c8df0d6b-cf73-3a69-84fd-3a60a8c3bbb0 | -12.37802 | -48.16694 | 2026-08-31 16:50:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 83e5549a-829f-3ca7-9fa0-f91cca90d64e | -10.1242 | -50.31901 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 8f266ea1-74cb-3394-b3e3-3086d4268e74 | -8.65474 | -49.54231 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 00d01a5c-0ece-3db2-9171-c1e4b6afca38 | -7.28589 | -52.54168 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 020d35b7-0010-3379-a8ca-a2c78a4bae04 | -9.16087 | -49.95468 | 2026-08-31 16:50:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ef8c91be-8645-39d4-9f33-fbea489f1305 | -10.02547 | -45.56594 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2844da11-3d06-3950-afb0-58087d06deff | -12.09272 | -47.25607 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 546fd00e-fd45-3f12-b92d-0b0ff532d9c0 | -8.76525 | -46.46528 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 55be3ab3-97a3-3736-89fc-b9ad40357a6b | -11.18507 | -55.09993 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5a8e6fac-7fac-3488-99e6-f52403934e07 | -8.49753 | -45.53067 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8913b515-d140-3d22-a7c6-5b8b719a461f | -7.85557 | -45.17793 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1ed6a6aa-a985-32c6-bc9e-60ace48e62be | -8.63592 | -47.46843 | 2026-08-31 16:50:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 75d0a057-d20f-3fd1-8f09-7469c7f7739b | -12.96158 | -45.9355 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 094dd979-1ee5-3eba-be7a-081fd09c314e | -12.17358 | -50.54134 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5378f854-b942-36db-aae9-6981d4d7a4fe | -10.92273 | -50.62337 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d233b5f3-fe99-3059-a638-e7631a3086bb | -10.4063 | -45.08081 | 2026-08-31 16:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ce52830f-6fdb-3224-9ecc-7739874c1329 | -8.95523 | -60.59953 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f59092b7-a524-330d-91df-2cc2d8235699 | -7.1034 | -45.7891 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 14143fdf-c495-3e37-840a-8b79c0106b27 | -11.35549 | -45.23244 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ca1a0fc8-fdbf-3604-afbb-74b7c9aa0918 | -7.08632 | -43.60775 | 2026-08-31 16:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fcd86ac6-730a-3fe8-b40b-f4d736aed892 | -11.67284 | -47.61429 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a6e54e09-8960-3fe4-9c83-dc4f04c5e8cd | -7.41957 | -44.25021 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b43f530a-a3db-38d9-b9ec-2f4ef02fe357 | -11.18812 | -55.09196 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b9bf83ff-8dcf-33a2-9a21-c633d728a123 | -10.82989 | -47.23183 | 2026-08-31 16:50:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bb28c888-5f9e-3ec4-a82b-379faceb2f32 | -7.05955 | -45.41803 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3c0ee518-66d6-30e9-9377-51f61aec3bb9 | -8.76565 | -46.44577 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1de4da7a-8191-3f20-b6e8-182819361622 | -9.96458 | -46.77856 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| fe94d135-4616-3ce7-b7f9-b7220de068e5 | -13.46466 | -51.41387 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ea29e9c2-dfb1-31ab-a3ba-8da079b191a4 | -12.0829 | -47.1487 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68c6cbaa-c8c5-3706-ad82-08bfcb1085d5 | -8.1266 | -45.48912 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5deeda51-d278-38ab-9e78-c1d9a8cf0668 | -7.43909 | -44.9505 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f0361b16-c7a8-31c9-ae67-c011ac6ca5f5 | -5.57945 | -45.73774 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2e3d0224-94d0-3c32-9764-55ab5c1b98d5 | -8.17319 | -54.93288 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 3f0a3fa1-6884-391f-9f70-e7efe58726d9 | -7.30201 | -45.36948 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 786acce5-2885-332c-b198-9ef3e8743fe9 | -13.83554 | -54.09284 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4a6f6d08-eb88-348f-938c-65f6bbc1224d | -7.7964 | -44.07316 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a41ac082-254e-3c50-8113-dc5b602c5256 | -10.15855 | -45.76487 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 44dd90e2-1f6e-36af-9024-e031b95f4b4f | -8.21394 | -54.93856 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e4d46d2b-7043-349b-9079-3d12085deb20 | -9.22706 | -59.58518 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6c86a9f4-4dc9-3cd6-af41-52ce53cf9fd3 | -8.14869 | -45.46453 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1310dd46-7989-33b8-b40c-8de14e36e3a0 | -12.92345 | -45.84977 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dd2edb08-bef1-3bcc-be10-7b6b51452255 | -8.41037 | -44.98021 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 38926458-cd40-3643-8928-8e39bf24c7a7 | -8.94485 | -50.76087 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 2d52ed0f-bc17-3d5e-b79f-96f7e139f959 | -11.03338 | -49.67494 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 176ebafd-ef79-3247-90dc-6d7e1e56b65c | -13.39882 | -51.66376 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6abd4728-6dea-3bce-b05e-d386a471f605 | -11.21177 | -46.08727 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ab9a7043-7f58-3b58-9e7e-ee7efcc402e8 | -9.22102 | -59.58604 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8c957f5e-41e5-35fd-8d1f-50ffd696c685 | -12.45243 | -47.80792 | 2026-08-31 16:50:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8130171a-007d-3751-a7ac-c1ee4fc357e8 | -11.23946 | -51.25386 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a0b52074-f8c4-36cf-8d54-18445f82ead5 | -13.83118 | -54.02412 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 29af6dd7-ea51-37d5-a1ed-c5d4808c84da | -11.37986 | -45.20338 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b9697b2b-9882-3e13-9513-275bde87340f | -8.86496 | -47.09169 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3bc2bbab-d1a7-34c2-aa7e-f29313af3ca3 | -7.3591 | -45.07824 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b1b9741-5c3a-3db8-ab0c-3050c8c112c7 | -11.93848 | -45.0751 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c5c63d75-3175-3d6a-8c43-628b368b5135 | -10.85321 | -45.33081 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| cdf9ca23-5ed8-3e02-8267-4cd5b2d3ed0a | -8.39059 | -44.98745 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0f79a100-7e62-3db2-bdc7-bdc913f0f308 | -8.44958 | -47.55687 | 2026-08-31 16:50:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1f40e79e-9d87-3c55-9452-4b0545fc91c9 | -11.52145 | -46.94215 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 406297b1-906c-3726-97cf-fc85881313bc | -10.1518 | -45.69457 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| acc069d1-c0a1-3db4-abb0-4e4d6b634d83 | -12.96099 | -45.93177 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 05e8b98b-ed4b-3cc2-bdc0-d5d80dc290bc | -11.25542 | -45.11045 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4cb3cb01-7820-3f65-8190-7306b0b6a8b1 | -7.60528 | -44.92519 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 42038c0f-2eaf-31e9-9402-890551922eea | -9.59665 | -47.59987 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 184f8a01-466c-38a5-a3b1-08bc59989f07 | -12.10375 | -44.99765 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 93889470-987f-368f-ba76-26c67561bae1 | -11.64125 | -49.40901 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f076e449-fd6a-3beb-b1e8-934099789825 | -7.93576 | -44.23811 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8183ddc1-5469-3b45-98d5-487891238e71 | -8.85872 | -47.07409 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a5e37d7c-b492-3b6a-9791-d3cdde33bb7b | -7.53098 | -44.44222 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c59ad82d-551b-3de4-9c60-94d1c1d43278 | -6.94309 | -55.63242 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 518ac3b6-d451-3d8d-ac21-0901744380b9 | -7.62884 | -56.76041 | 2026-08-31 16:50:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 1cf34193-e813-3720-ae5f-afaabc8101dc | -10.15505 | -45.69759 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 3fcb2c3b-6b38-337a-b300-a47839a6438d | -9.60225 | -48.25227 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d380d003-a67d-35af-8826-71a9c5540a77 | -12.41826 | -42.88397 | 2026-08-31 16:50:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ee51ffbb-fdf0-3c16-bdac-739374424177 | -9.5961 | -47.59636 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 46406b1c-d857-3a35-beff-3f67cf3732b0 | -5.58626 | -42.32254 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 328599fe-65bb-3940-8f60-34d08f944d30 | -9.161 | -60.93619 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 9814830f-2b6a-3ddb-8b81-e5c7bd974171 | -12.95658 | -45.94775 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 84e46c28-32a7-389d-ae50-e15ca3dcd886 | -7.02824 | -55.6361 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| b0e36075-d084-3da6-87ba-50f73dd44de0 | -8.7555 | -46.47059 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 839c5fc1-6209-385b-a80d-2141a8100226 | -11.3788 | -45.4218 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |


[Clique aqui para ver as próximas entradas](README161.md)
