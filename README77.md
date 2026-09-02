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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad620607-8ac2-37af-912e-28542ef4c20d | -12.1312 | -47.1309 | 2026-09-02 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 4efcfb00-c91f-3ac1-a5f7-b4db88495880 | -6.6765 | -58.7492 | 2026-09-02 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 16884bae-2de3-316c-ae41-03d130e78639 | -6.1474 | -57.7605 | 2026-09-02 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| aefd34c6-bd31-3095-bcf2-9a5c0b1c53bb | -11.7148 | -50.5109 | 2026-09-02 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| d4a0be96-62e4-374a-8dba-de3d7590000d | -10.8046 | -50.5046 | 2026-09-02 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 090a3a3d-7c00-3f7b-b543-8f94e2c89c2b | -11.277 | -50.5815 | 2026-09-02 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 3ff247f8-d5e1-3233-a98f-efa979138219 | -10.3007 | -50.023 | 2026-09-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 6f7ba72c-ddeb-396a-a987-22de07bcbd94 | -7.219 | -60.689 | 2026-09-02 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| c2badefa-cd33-3b12-b691-61a3e311277b | -11.6624 | -50.1954 | 2026-09-02 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 8893e397-1f27-3ddd-a28d-418008b606fd | -10.301 | -50.0016 | 2026-09-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c7224b37-335e-38c2-88f1-992abf052f16 | -12.0741 | -47.1164 | 2026-09-02 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 305.6 |
| 870d8e3e-4663-397c-a651-1c0356997385 | -7.2006 | -60.6706 | 2026-09-02 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 9dc19774-6c8b-31a6-b5c9-297bf0a3f644 | -11.3771 | -45.4 | 2026-09-02 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 805b7ef9-eb9d-3160-b1c4-11fd979bd3db | -7.3487 | -60.5883 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 85aad017-7481-3878-bca3-18e1e727b04d | -10.5788 | -47.7306 | 2026-09-02 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 485.0 |
| 07909c1c-34c6-3a03-a28e-aaf2d3c849dd | -11.3575 | -45.4257 | 2026-09-02 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 2e953ba1-938c-3eed-b217-9534116461ff | -7.2191 | -60.6699 | 2026-09-02 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| e217211e-6a2f-3ce3-a911-733799c61e49 | -10.3193 | -50.0425 | 2026-09-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 027f067c-aa94-320b-999f-19c5626249e8 | -7.6505 | -46.7268 | 2026-09-02 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 184cfcf9-5413-3cb8-8e25-bfecc32806b0 | -11.1821 | -50.592 | 2026-09-02 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 0f4b78a1-3153-30e9-b8e8-76b0f898a640 | -5.5832 | -60.2116 | 2026-09-02 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 681f4da5-3847-3af0-91cf-d4e68373e6e2 | -11.3052 | -45.1344 | 2026-09-02 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 7ffb8203-0977-3dd9-b133-2eaaf36195e6 | -10.2209 | -50.3517 | 2026-09-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| cd8c0f09-ddf7-3fa7-a236-ade650a77030 | -10.4145 | -49.9898 | 2026-09-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 46df85c3-6739-3fd1-bcd4-fd311dd6b0b4 | -8.4298 | -54.706 | 2026-09-02 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 7957902b-77a6-3d80-8f70-53e10542e377 | -12.3622 | -48.1681 | 2026-09-02 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e5bd56a3-fa9e-3e36-a12e-df9eda2a7303 | -12.1504 | -47.1283 | 2026-09-02 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| cc2429da-2176-33bb-8546-90d6fb48d93a | -7.6149 | -44.8833 | 2026-09-02 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 81b121d5-f2e4-3fc6-abc7-533b6a548a0f | -13.9855 | -58.672 | 2026-09-02 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 234.1 |
| 60531c09-1e67-3d10-9bb6-52ab476b19d7 | -10.358 | -49.9742 | 2026-09-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 530148cc-a670-36c5-92b4-fbcfd366e1d3 | -10.8235 | -50.5026 | 2026-09-02 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| c16582fd-811d-3bbd-9a25-3eec9b273c5c | -3.3688 | -59.3887 | 2026-09-02 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 123032f2-2264-3cea-b58b-e8ea516d1ac3 | -11.0247 | -49.6656 | 2026-09-02 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 9da1b703-e9ac-32bb-a87d-172358e9f146 | -10.3004 | -50.0445 | 2026-09-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 0480e9a5-2913-3d14-9f3c-d2f19584fab5 | -10.0818 | -46.7217 | 2026-09-02 14:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 7207123b-86ee-3d7b-a7eb-b8524470047a | -11.67 | -50.52 | 2026-09-02 14:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9adfe30-2948-3d0e-be72-ff65e290c9a7 | -13.5531 | -59.7574 | 2026-09-02 14:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b838df6e-1314-3e49-b70d-9d91df01eeae | -6.6765 | -58.7492 | 2026-09-02 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| e84e3a14-fd1d-3ed8-9b9f-99a9164aa45f | -10.3394 | -49.9547 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c6114a98-6821-3ab1-b37b-db487744b074 | -10.442 | -46.7235 | 2026-09-02 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f3eec19c-c9cf-31d9-b17f-0fbe078d7450 | -9.4349 | -45.625 | 2026-09-02 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 2b629538-92c8-38f9-80f3-74e60920f762 | -10.4334 | -49.9878 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| a8d4df70-398a-32ab-a07b-048d72f80954 | -9.139 | -51.1307 | 2026-09-02 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| addf8a14-25e0-33dc-92fa-e9f083c6e132 | -11.6434 | -50.1976 | 2026-09-02 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| c15a24eb-a12f-3921-af3d-c29b451c3c38 | -11.1631 | -50.594 | 2026-09-02 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 9dcd010d-6c23-334f-8890-76557f342c63 | -8.7817 | -46.4623 | 2026-09-02 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 84932503-052d-3cbe-84d4-42d35be8d316 | -3.6216 | -60.547 | 2026-09-02 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3db28c97-4cb0-3f14-bef4-6ba1f32d4358 | -12.1312 | -47.1309 | 2026-09-02 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 5c693d9e-98e8-39f9-89a6-343ce2377dd2 | -11.6624 | -50.1954 | 2026-09-02 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| f7c3ad12-6089-3648-b3f9-ac2462b6b44c | -7.8071 | -47.8372 | 2026-09-02 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| e127e8b8-64cb-3e03-b4c8-7b736eef13e8 | -14.5758 | -53.5948 | 2026-09-02 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 99a6695d-0d59-3629-b19d-c2f4c37d8bba | -11.1821 | -50.592 | 2026-09-02 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 30e4d39a-04c6-32dd-a139-4985835b6096 | -7.2191 | -60.6699 | 2026-09-02 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 06ca7539-7a9b-3f92-824d-fb7233d0fd48 | -3.3688 | -59.3887 | 2026-09-02 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 66052ced-73ff-3343-85a0-68152450d248 | -6.7648 | -59.4408 | 2026-09-02 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| afd757d8-a661-36b8-b2a2-01678e0c3dea | -9.6633 | -48.2721 | 2026-09-02 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| e19b23cc-0b41-3beb-82fb-b778aea21296 | -7.6505 | -46.7268 | 2026-09-02 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 3712dd9c-83b4-30fe-af7a-f744295439de | -7.5326 | -60.7147 | 2026-09-02 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 012e280d-7b6e-3ee9-a056-cc0d126c5fba | -11.1304 | -51.5939 | 2026-09-02 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 7a304e64-c397-3fd3-bfb7-dfef4f921233 | -13.5533 | -59.7377 | 2026-09-02 14:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c2cfdb0f-bd97-3255-8984-f0b90b66417b | -12.3622 | -48.1681 | 2026-09-02 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 131b35af-0a64-39c0-b36b-d73d6baabed7 | -3.2455 | -47.9187 | 2026-09-02 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 7d4cf361-8fff-3c22-ba90-9c0eec8dca26 | -10.3193 | -50.0425 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 82b8a1c1-1788-3296-8945-a4e19decc186 | -10.0638 | -46.6566 | 2026-09-02 14:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 33fdddc9-9a30-34aa-bdd1-ba17e9a090ab | -9.8806 | -64.9764 | 2026-09-02 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c4c46de3-6482-3ca9-ab1c-20f6eb66f95b | -10.3391 | -49.9762 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 1de569a5-4f52-389b-a787-4e8cbaa2ab0d | -5.6016 | -60.211 | 2026-09-02 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c12bffda-534c-3063-8eed-9a2f4fdb24ae | -9.1533 | -59.5027 | 2026-09-02 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| c01e4690-51f0-3e19-92f9-d1ea956e8c8f | -12.0936 | -47.0913 | 2026-09-02 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 21d73554-f783-3608-b2b3-f60def70d102 | -13.5724 | -59.7362 | 2026-09-02 14:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 1a743438-a752-3df4-bb12-1075969118d1 | -11.1307 | -51.5728 | 2026-09-02 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 5b7c8019-f1e3-308d-bffc-da328c1fbbab | -6.6542 | -59.426 | 2026-09-02 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| c2c8312b-0d3b-3bfc-9c72-ce5cfa97bf81 | -7.2005 | -60.6897 | 2026-09-02 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 400ed507-a442-342f-9545-be1a0575a5de | -10.4142 | -50.0112 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8eb36b68-d979-3a7b-88fb-ead04cdb5973 | -10.8235 | -50.5026 | 2026-09-02 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| abfabcd0-453b-32a9-a6b8-7a5947dd98ea | -14.1083 | -45.5008 | 2026-09-02 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 239.3 |
| 4365968b-52bf-38c1-85f1-66a4423839b9 | -10.5788 | -47.7306 | 2026-09-02 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 223.7 |
| 880a646f-bd41-3ccc-a62b-6f6d2faa309a | -5.5833 | -60.1924 | 2026-09-02 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 0efbf490-5b16-3432-b845-62072f5387a4 | -7.0057 | -59.2575 | 2026-09-02 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a294a682-1472-3596-86d5-6e3e2b11f6f6 | -11.6621 | -50.2169 | 2026-09-02 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 604ab65b-f58d-3b1c-a37b-02f10e2a952b | -10.358 | -49.9742 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ae8c7d0e-f83e-3bfd-8ae5-bed4edaabd0d | -10.3959 | -49.9703 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 8c9f864c-14fa-308a-b24d-6e190d187614 | -10.301 | -50.0016 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ecf938e1-aa19-3510-ad0c-9c66880208f8 | -7.3487 | -60.5883 | 2026-09-02 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 07413492-7584-38b1-8705-f6458883a106 | -2.9447 | -60.9002 | 2026-09-02 14:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3b8bb3d9-dd9f-3119-8204-68c569b44df4 | -3.8604 | -44.0585 | 2026-09-02 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2968ed12-e7f6-38e9-9d78-3c5510908426 | -9.4159 | -45.6271 | 2026-09-02 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 916ff7a1-67ff-3ced-8b8a-d549a1dc0b1a | -6.6764 | -58.7686 | 2026-09-02 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| eb0f091b-54a8-3020-aa02-cb27c34f0201 | -6.8422 | -41.6791 | 2026-09-02 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 1ba90de5-fb92-3231-8901-249ddd190925 | -10.7431 | -50.8514 | 2026-09-02 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 2af4fc5f-a6e5-3013-a879-864dc6f785e1 | -11.1634 | -50.5727 | 2026-09-02 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 3af72135-4b6a-34b6-8ea0-9a2f7c185fd6 | -8.4298 | -54.706 | 2026-09-02 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 32f244b1-38cd-36d8-8c44-c11b37ab1c20 | -13.9662 | -58.6936 | 2026-09-02 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 290.4 |
| 51c0a528-3b2d-37db-985f-eae17fa85cda | -11.3579 | -45.4027 | 2026-09-02 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 509.7 |
| d0dc8da6-8f99-3270-85b0-34a761a0e726 | -10.3004 | -50.0445 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 04745294-9741-3fbc-adc6-eb2cc05f65b3 | -10.3583 | -49.9528 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| fadf97d0-e5b6-392e-a467-428edfddb9c1 | -10.7618 | -50.8707 | 2026-09-02 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 986b0499-82b0-3f0c-bc41-73a202b55d4a | -8.7615 | -62.5679 | 2026-09-02 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7981a4d6-59fb-3183-8aa0-44682ca94e2e | -5.2167 | -60.0507 | 2026-09-02 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 31f9ab95-5643-3757-9927-5f3055c03a6a | -11.0247 | -49.6656 | 2026-09-02 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |


[Clique aqui para ver as próximas entradas](README78.md)
