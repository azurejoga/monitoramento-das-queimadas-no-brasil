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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d468538-f859-34da-aaab-4e344cc22224 | -4.22608 | -47.21371 | 2025-08-14 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a5cb65d-a78f-3ea6-9459-24e368bb8851 | -2.90734 | -48.30191 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eda65534-1fc7-3558-97b3-444f0aa21bc9 | -2.9059 | -48.25291 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7bf9510-b600-36d3-89c1-1b6284804743 | -4.1438 | -46.45837 | 2025-08-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a62cbc0f-248d-3ba7-b119-1ab8a4ebf560 | -2.90545 | -48.25584 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51196ad0-7107-3cd5-85e8-5a5cb4860233 | -4.22555 | -47.21748 | 2025-08-14 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ae039f1-c16f-3b3d-b851-dfae5d4c5900 | -4.2279 | -47.21083 | 2025-08-14 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd288186-9dec-3e1b-9ec3-cb48d20fb9ba | -4.14446 | -46.454 | 2025-08-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5db3f22f-da8e-3ab4-ae93-b5b2963f002e | -2.9097 | -48.25045 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cd0ffc4-f3dd-32fb-a03e-edc25393940d | -2.90082 | -48.25209 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7b134cb-2f97-37d4-910f-2e24f8fd5501 | -2.91285 | -48.29971 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de08c426-7994-330e-b1b6-d5e54e10714d | -2.48915 | -47.57211 | 2025-08-14 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa6d8822-b76e-3d0e-9aef-c74447862539 | -2.90549 | -48.24369 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed2eb5af-ea9f-3ef8-adea-db6bd397bbc5 | -2.90375 | -48.25556 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba7db754-34d6-354a-9399-c34ede8a485b | -2.90682 | -48.24699 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043c94ad-76fa-342b-acba-0c1af661a274 | -2.90778 | -48.29892 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4811220b-e818-3ecf-b27e-6deb1b3df845 | -2.48866 | -47.57545 | 2025-08-14 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a5d54d5-4266-3686-af6e-d78999e996b5 | -2.90636 | -48.24995 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c49e58d-dda4-300b-9187-094449e7a599 | -3.9124 | -46.45301 | 2025-08-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1736dfd-1334-3e64-98a1-02eb09bb6810 | -2.48965 | -47.56878 | 2025-08-14 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b5c584d-fd46-3ebd-aa61-6db032440a59 | -4.22661 | -47.20995 | 2025-08-14 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aad44a20-085a-31fd-acd8-9d31d1855790 | -2.91014 | -48.24748 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 025d1b49-f4d0-360f-8dce-4426b98889f9 | -4.22502 | -47.22122 | 2025-08-14 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2438fd44-84c9-32a4-a316-bd21214601f8 | -2.90418 | -48.25262 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d26eb8d6-b315-3537-b9a7-d1d344519297 | -6.8771 | -59.147 | 2025-08-14 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b3499bb9-1560-368e-93c2-dc588fb852f1 | -6.8956 | -59.1462 | 2025-08-14 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| a9800858-d7ec-3aee-8980-5e37e0a9fdbe | -6.0991 | -59.9459 | 2025-08-14 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c9bb645a-ef1d-3c05-9885-48f7a6dfb59e | -6.914 | -59.1455 | 2025-08-14 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 8353e960-e63d-3709-8a06-02d338a57ec0 | -6.877 | -59.1663 | 2025-08-14 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 9ebc85db-91a7-3bf0-8cc2-fd88399a64e5 | -6.8955 | -59.1655 | 2025-08-14 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f5c8cb6e-fa58-3021-8a6a-d5e987a87727 | -6.9139 | -59.1648 | 2025-08-14 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 8909805b-648e-350f-a8de-76241aa9dd96 | -7.61945 | -63.51527 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c4c949e7-0f6d-33cc-86ef-e4cf9dbed70c | -6.1044 | -59.92129 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c97810dd-6eb3-34e1-b930-09ae37327877 | -5.75982 | -59.89692 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28b472b5-b6eb-3c7f-9f64-fdb45705f980 | -6.1114 | -59.92239 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3715d143-46ee-3c03-9761-0c49a0517e73 | -6.87756 | -59.13858 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e52e643-3444-3b42-982d-3bd887cc9928 | -6.77475 | -59.46837 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3ac56aa-ac34-3fad-acfa-b46d6954e0c1 | -6.88374 | -59.14331 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34a9ea78-deec-3fd7-b011-4499f88cfd9c | -7.25559 | -59.99017 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7a753c4-dd14-32ae-9c7b-ecadeaeac76a | -7.09498 | -60.02361 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1e9493e-3778-3b73-ae6a-292ef0fc26fb | -8.25941 | -45.06334 | 2025-08-14 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bddb1df1-5067-3a2c-9a15-30c7bf43eb1c | -9.19308 | -59.65842 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 323d6c8a-5885-3e9f-a7a8-c0ae421737c5 | -6.90754 | -59.12479 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11f97965-911e-3477-89af-48d31afe208b | -9.82686 | -60.76064 | 2025-08-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34517f93-15e5-3cb1-bc88-4152aa5a0cbc | -4.77787 | -45.33451 | 2025-08-14 05:10:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8259e1b6-2e14-3f75-b4e3-9b7c41a76a1a | -9.1534 | -59.66006 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ac0bf6c-04ea-3bbd-a479-c3da08803b86 | -6.87639 | -59.14583 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c6f6ab5-168b-3dd1-9da8-3e430c31fc05 | -6.94486 | -44.56384 | 2025-08-14 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ca09f4c1-fedf-3f25-88ef-73028ae9ed38 | -9.15119 | -59.65219 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bb212cd-309f-3edb-b200-827779f0f63e | -6.87418 | -59.13803 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1251a883-8f0c-3bc5-afbf-9153efad7d22 | -7.60124 | -63.5202 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30315397-2e87-3980-81e7-04faf6b79b2b | -7.59904 | -63.50769 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a93b7795-14db-3929-9def-c268122f275c | -9.1484 | -59.64799 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8829cc5-74d3-39cb-a7c2-98e00c25ded8 | -7.58377 | -61.40952 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb092515-d4a5-34cb-b68d-b4b98cd49178 | -6.8758 | -59.14946 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 845f5c47-43d9-3ec1-bec8-6e84b026b53a | -6.87242 | -59.14891 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| caf1c22d-3303-3c9f-92ca-4bd85f569d65 | -9.14546 | -59.66626 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4046cc1e-47b6-36c6-a664-01a002f3d5c6 | -6.1012 | -59.94083 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5cb6b54-66c9-3426-8eef-97d7f08505c5 | -7.14065 | -59.65622 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e493dd3-bdcb-304d-98d6-8e0f60400b23 | -6.10055 | -59.94473 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a92ae8d4-91dc-3fc3-a2af-9bc25250cc9a | -7.1433 | -60.12328 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0de1238a-3508-32be-a851-0ce358b42108 | -8.106 | -61.19428 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3759d283-3b1f-3f74-8eb1-d93ad781c851 | -7.23574 | -60.00275 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 480ab2bb-f74d-351b-91a5-5ab25418d02b | -7.09372 | -60.03133 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3953b876-c514-32c2-80be-aa3e05fc76c5 | -6.08717 | -59.93864 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| deba534e-4146-332d-b31b-f99e831a1c99 | -6.08556 | -59.94288 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 928333cf-68ba-3918-ad00-eae95c129783 | -6.77697 | -59.47636 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4570c0e1-2cdc-39cf-ae6d-e457a222e3dd | -5.73588 | -59.88911 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3437e8e-7893-31d1-8a3c-ca0656671229 | -9.20499 | -59.64918 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c71ca8f-99c0-3ae2-84ab-916c0a7b93fb | -8.57556 | -54.71926 | 2025-08-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 432398c5-d582-36bf-b89a-06a6c5dda446 | -9.06216 | -60.65061 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 009f2ee7-b6ba-3428-b45d-b4bcfd401633 | -6.91137 | -59.14405 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0f7d21ef-e1f8-322e-8633-abc8d23657c7 | -8.11116 | -61.20826 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11a9ff07-f294-36d8-b0ca-af78087ee34f | -6.07093 | -59.94441 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50edce71-ea2a-3fb3-99c3-b0bd1d9d008c | -6.56682 | -60.06145 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddec0aa5-f5e7-34f5-9f40-b3d55eb9db9f | -9.50519 | -60.53723 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95e84f18-bd32-3fbd-a0a6-cbf382983828 | -6.88139 | -59.15782 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a50f3ae8-dfc6-3c53-845f-7828a5c72909 | -6.90299 | -59.13152 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69806a54-6d44-34c9-8b86-200b7da5c255 | -7.3227 | -60.62555 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8608cfa-70d6-328c-bfbf-6ddfbe9e85f7 | -7.87718 | -61.82206 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1ca5e5a2-9e61-3a4f-8059-099b5456f10c | -7.45543 | -57.64841 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89651b22-6f2d-39af-97d0-8afff3e4b495 | -7.14408 | -59.65678 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45939de9-1ca7-3534-91ce-db0885a2265c | -6.89682 | -59.12679 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dcacd38-6ec5-30ad-8d29-fd6afa08adca | -5.74227 | -59.89411 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d696d5e-7c73-3538-b075-1821485f20aa | -7.23512 | -60.00657 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9c533df-bf1a-373b-a041-370a25494d92 | -6.5365 | -56.20742 | 2025-08-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f30ad10-0763-33a5-aecd-2dbedcc2b786 | -9.82971 | -60.76517 | 2025-08-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 174492cc-4b03-31b6-b947-435f89c02f6b | -6.89154 | -59.15946 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a631b9f0-c1a3-3214-baf9-eab015274911 | -9.18672 | -59.67613 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 563f7343-e583-3ec2-842b-482ecd4074a6 | -6.9277 | -59.1504 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ce75274-925e-304f-87c9-e531a9297eb4 | -7.14041 | -60.1263 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcdfea4f-4ed0-3612-bc78-6d33718910ea | -6.88888 | -59.13297 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba79db8c-41ee-3ae8-b252-5dce70ca70cb | -7.13282 | -60.12155 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e69d862f-424c-3e8e-879c-d206d83bd3dc | -9.50866 | -60.53781 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e8aed94-2d9a-3f23-8e78-1d2d5f09c8cd | -7.87872 | -61.81289 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6cce386e-172e-3c02-94db-1b869565548a | -5.74829 | -59.87901 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0345dec4-7131-3793-b914-0b8e7ac54c0b | -7.13981 | -60.12268 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 034fb139-eab8-3b33-aae7-12950a2c432c | -7.8764 | -61.82669 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 67221cbc-8de3-35ef-bed8-a3da1954a07f | -6.8955 | -59.15638 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 08e2dace-064f-3287-a7b1-449683397a2c | -7.25845 | -59.99455 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README27.md)
