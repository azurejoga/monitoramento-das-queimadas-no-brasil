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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47ed9188-1c1c-3ed0-b9dc-dd2df1872a3f | -8.80204 | -50.49662 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3d88216-a8d2-3366-8404-21aa31d6d942 | -8.11195 | -51.65797 | 2026-08-28 05:10:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45f73b7a-0dcd-3af7-be26-9850cafc8735 | -11.01425 | -45.07704 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 39582414-2427-3a47-8803-b91a681865ed | -9.00625 | -57.54776 | 2026-08-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80191208-35b2-3e1d-8358-dfcfa393ba05 | -8.59975 | -54.78419 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbf40b0f-c2a8-3972-ae52-1a35527fbbc9 | -7.38178 | -55.14677 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d73c8ac-0a06-3aa8-99dd-505b1dd77674 | -9.976 | -53.9424 | 2026-08-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 057ba0c4-cd29-3da0-bd2e-49fe41a01cfe | -6.26485 | -53.3682 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e3b9b80-bef8-3a54-b8a0-b30c7ac5e3ba | -4.31016 | -59.47672 | 2026-08-28 05:10:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bec3c8ad-8579-3836-82e2-092bef6abdc2 | -10.0628 | -46.94174 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d035071-0c21-3be9-b1cf-0c0e480b9450 | -7.24772 | -45.86934 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3bea5217-829d-333e-aea3-59fa5d3407cf | -6.59922 | -55.44183 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aad97fd5-0c94-3aa9-bb3d-aa80be0f198b | -7.40576 | -55.1687 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4f449b5-8cf6-3f4d-96d4-9d03cff0c03e | -6.52378 | -55.25101 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc5878a2-0809-38b9-8579-9b8898520c0e | -5.28698 | -50.94102 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c57fffb-0cb8-32ca-90c5-a6973f07dcb2 | -6.53376 | -55.25257 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1afa6814-25f5-3ab7-a678-fb0d29521fe0 | -6.1693 | -57.78207 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90de554a-aac8-3d5b-8329-2625f2d43e79 | -6.32026 | -54.73153 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eced1fb2-19c2-3b24-8bc6-114b0db846e9 | -9.97305 | -53.9378 | 2026-08-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 09f40258-7444-3637-ad3c-dd0868250920 | -6.30924 | -53.5774 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d6ed3e1-725b-36e0-b513-05e0d5041928 | -6.15268 | -57.79831 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 091c0173-ec9c-36c7-9d09-0e8ef13d1b90 | -6.22849 | -55.61755 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93bb0d7b-7473-30d2-b961-1fa92c7821ec | -9.17636 | -59.63257 | 2026-08-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9bf60875-b075-31eb-ace7-31f5fcc74721 | -6.27891 | -53.37033 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5921b031-b061-3c56-8a15-4dcdea04cc36 | -6.85943 | -59.02346 | 2026-08-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af5edbaf-a156-3ec6-8118-2cecd19b3a68 | -4.30323 | -55.24649 | 2026-08-28 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 392378f6-0ea6-36b0-876c-2976103272ac | -6.24089 | -55.47399 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b61c8c9-6909-3058-91ae-2e48ef4d0b5c | -6.2645 | -55.4101 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 295b0183-502e-39ab-acce-daf0e748ee4f | -6.82377 | -55.61223 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8bf60be-d023-326e-8b3c-2e603aad537f | -8.78594 | -50.07457 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ede3102a-d69e-399a-87ff-3ddd5ce88ae0 | -8.551 | -54.71627 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41b41761-c544-3f8e-b501-7f0dfd080eb2 | -6.23095 | -55.47242 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 152a13ed-c4dc-380f-98fb-4c8a8c4d6b7e | -9.22622 | -51.55035 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8613f83-8b6f-3f1f-90ba-de91a78c3660 | -6.76374 | -55.69168 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e278a62c-7da7-380e-be22-151a6d5b95b1 | -6.31914 | -54.73865 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a878b02-1d4a-3d0e-a6b5-4181513f46ff | -5.91498 | -52.12246 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 870aa480-93c3-3a0d-b91f-8bf5d09520c4 | -7.15607 | -46.54326 | 2026-08-28 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc113d79-9a3e-37d2-ad4c-50ab4757f93e | -6.14068 | -53.5172 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d176106b-a8e5-3b41-8ff9-337db1fbb606 | -7.27209 | -45.35086 | 2026-08-28 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 43eff4d1-5b1c-39ce-9f0d-4f203da4cdb3 | -6.63611 | -53.18504 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 240c4b57-6e20-3454-9987-cb42b1f7c6b4 | -3.94283 | -54.83945 | 2026-08-28 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b7f8710-3a47-39ab-b18f-90a900255b04 | -6.52433 | -55.24752 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17f73c79-32d8-3be9-a174-e76691907b88 | -6.2208 | -53.46939 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdab6482-28f5-3af2-a97c-e1b72d53730d | -3.93746 | -53.59019 | 2026-08-28 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d309ce6d-ca0e-39ac-b508-9cba3b6e054e | -6.229 | -55.93642 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99894d9b-ef62-31f6-9b93-b6f7fae1cd55 | -6.24797 | -55.42887 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed2aea33-5448-39cf-93fb-89ec7fd04a9a | -8.14902 | -64.00679 | 2026-08-28 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 194d279c-78a3-3384-abd7-6b05a62621f8 | -9.65448 | -48.29876 | 2026-08-28 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca92e9b1-1a83-3eb0-9efa-ce50d2a42938 | -9.06207 | -45.78118 | 2026-08-28 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0d7a57a-b55c-3f0f-baa5-7f106fd009bd | -8.77708 | -50.07325 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef44f8fa-4f40-3f06-8a04-c5e9d3e16cd9 | -6.2666 | -53.12099 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 785a9d86-2553-34ca-b2ec-bde0e58a6bb3 | -4.07483 | -56.32243 | 2026-08-28 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 543aba27-f8c3-3ea2-a5f0-b2317106fa1d | -9.61284 | -55.11847 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 66064a41-a48c-3ef3-9e47-1a2e0ed2314e | -6.96621 | -55.63498 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96eb3b41-8549-311a-8203-80192181091b | -6.62543 | -53.18347 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30e7a8d7-8306-339d-9d04-77ba3e92310f | -8.61059 | -54.73674 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 200a20f5-58a6-3ec4-b8c2-c92dfd08ad5c | -7.34557 | -55.66242 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a89307e3-2a9b-3792-b449-c08140da4a6a | -9.3405 | -48.16858 | 2026-08-28 05:10:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9991109a-8cea-397c-b160-e56b0557d910 | -5.99672 | -57.83055 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56bd35b0-adf7-3a5e-982d-d839502a5e3d | -6.75857 | -46.13687 | 2026-08-28 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0f9fd93-8123-3cc1-8554-d1eeff4c5a06 | -8.14994 | -64.00159 | 2026-08-28 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98ea5675-bc0a-3234-aa58-74cc9f1354bc | -7.70696 | -55.37164 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6902f484-2d5d-3151-9b98-250ebad7702b | -10.06643 | -46.94512 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f40c756c-2a5d-3404-ae77-a8f4c362ca0f | -7.24937 | -45.85717 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 596f36dd-1050-39fe-befc-e74317fd0b11 | -7.26094 | -45.85857 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| eafc77c7-2f9d-32f4-80aa-3981e40a3877 | -6.64323 | -53.1861 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0fdd2b9-0634-35b8-abdd-fdef6ddc80e5 | -6.75104 | -55.68613 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02a733f3-e7de-3641-a2bf-86edd031344e | -9.97244 | -53.94188 | 2026-08-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca4cdbd7-7ec1-3ef8-93be-4fe305f39c3b | -7.01989 | -55.70396 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6412c183-a6f3-3bcf-8229-1bbcbcb16336 | -10.00899 | -46.41026 | 2026-08-28 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b814164e-f985-3829-9b41-3661e2b5f990 | -11.37 | -45.14972 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8f8a9fd-bc70-3607-98e8-53cfb1a1e8e6 | -8.78169 | -49.95409 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 158bd10e-2226-328d-bf42-c5183820a380 | -3.45429 | -59.51746 | 2026-08-28 05:10:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1e613f8-b336-3b4c-9435-8c6b8e37157e | -8.60323 | -54.71669 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65074148-204b-3860-a010-1db7152ea5de | -6.77476 | -55.68633 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 675faf9a-4b73-3f16-b086-9ea7f5727277 | -6.16411 | -57.79256 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 98ce5d19-7bee-33ce-aaef-724cc5c0b370 | -6.83628 | -59.9456 | 2026-08-28 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a18ade8-7a7d-3dc7-813f-2a9447a6fbdc | -6.2442 | -55.47451 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5edac69-9b15-3910-9efa-07e42703eba9 | -6.28011 | -53.36252 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 164fd8ac-33c7-3269-a145-6c1e9d11a666 | -6.26232 | -55.42403 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3d175d9-5b86-396c-9c6f-95d6c677b462 | -5.29002 | -50.93846 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a64f0d3a-0fbc-3cf4-b222-126abc8da35c | -6.52324 | -55.2545 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cdb60ec-5f9a-38d1-a80b-38096e6232e1 | -9.22883 | -51.53189 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cc92e70-fa48-3174-ad61-182ef40cbb6b | -9.22931 | -51.55763 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7de711ac-3b7f-3796-943c-e6ec4022d48a | -6.30676 | -53.53819 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 989ad201-4375-3b9b-8e4a-8dc4a70282af | -6.52155 | -55.2435 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40eb42d0-98bf-337b-87dc-ec51dd7e64d2 | -6.15387 | -57.79091 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef6ece8f-06d8-3afc-9cc4-a49272c489f0 | -8.2425 | -54.98745 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 662592b5-63bc-36d6-9ab3-12c8da19c09b | -6.17094 | -57.79368 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b10cc3f-af92-3943-b8b2-da96b7e9dc8c | -9.46154 | -51.70209 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5008ba2f-dfe3-314d-97e7-cc8ebceb2d1e | -4.35983 | -55.36127 | 2026-08-28 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8145751f-fa4b-332c-862f-e6743022bf89 | -9.38846 | -55.9743 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eae5db00-a472-39fc-b382-fffbf451bf6e | -6.1607 | -57.79201 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 60feaade-b93f-33f0-9c80-e3a0a3f7c317 | -6.27779 | -53.35413 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 876002a2-bc82-3410-904f-d900076d165e | -8.80367 | -50.07713 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ae17dfe-d518-34e9-b127-48feaef6ce94 | -6.18894 | -55.41602 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f08db0d-3067-3d96-ab4c-0ea523aa7089 | -7.26863 | -45.35272 | 2026-08-28 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b27f76c3-0515-3798-9c7c-265f1d1c2c26 | -6.75435 | -55.68666 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f275c45-f46e-31eb-9392-22fd864df2b4 | -8.59521 | -54.79105 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f989510d-b7d8-3c1b-8049-b6c8a383807a | -9.21268 | -51.55867 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README49.md)
