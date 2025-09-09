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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba09fa22-3600-36d6-bae6-59f9fddbc281 | -9.55661 | -48.66352 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52b5c6e2-7632-358d-aff5-3a9291c2f9a4 | -7.77527 | -50.76976 | 2025-09-09 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43dd5cf6-c8e9-3176-bc43-995184c91e0f | -11.22943 | -59.12764 | 2025-09-09 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7d77638-bb34-35f2-aaee-20fbf6d83eea | -11.82624 | -46.77716 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c82b853d-a688-35c3-89bb-3ff27c2a85d6 | -8.06155 | -48.65493 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1b3ad8a-2e15-3140-86a3-6869bdda9b2d | -13.48427 | -48.21252 | 2025-09-09 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f57bcee7-5634-3526-b4f6-cf5db5e9cc17 | -7.80823 | -45.41502 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f78b52d-f3be-3523-bdb9-4ba4d788c624 | -13.84394 | -46.23227 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3238f581-0a4a-39e0-96a3-6a927cb80525 | -14.43787 | -48.46688 | 2025-09-09 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6989d941-221b-37df-a119-52dd98318259 | -8.08862 | -54.74812 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbfd788b-abcc-35c6-992c-f88882d26a15 | -8.87656 | -47.89848 | 2025-09-09 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d86d6b43-f8f0-34bf-b7c6-ee539e7a7dcf | -11.31096 | -50.41537 | 2025-09-09 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 326e6f03-e69d-3129-8cbe-dfb3f34ae8c1 | -11.42248 | -43.58919 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9386563-bddc-3f41-830b-e3fb0651607c | -11.41935 | -43.58102 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5210bb38-1687-31a2-a9bf-ab818a68a772 | -6.39813 | -58.20467 | 2025-09-09 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2300236-00ec-3e1d-b2bc-5fb992d1b74f | -8.02082 | -43.81292 | 2025-09-09 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 86c5b24e-8f7d-377b-8101-e76b90ecb004 | -11.18718 | -55.05853 | 2025-09-09 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 335c23b5-5c8e-3cef-aafe-cec382060dc4 | -9.55715 | -48.66004 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 486ad3be-a4d6-3eae-8fe4-c33913bca5c5 | -7.6816 | -50.28273 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12a0c9d4-e263-38dc-b2e6-d517b9a9cc7b | -10.3401 | -47.73318 | 2025-09-09 04:34:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9550232c-4ecb-3d33-a2ac-5a5199e7352c | -9.13961 | -60.52302 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50de16ab-f9c7-3c89-8619-9e0d0ce28e97 | -9.07752 | -46.98105 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df807352-95d3-3f31-bd81-d791cb1f5f46 | -13.79774 | -46.26708 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ca97efd6-0535-353d-b6ff-0f7001cc56d5 | -10.97456 | -46.80846 | 2025-09-09 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 506926c7-30e7-37f8-a167-5433a1dd2f2d | -11.55779 | -49.0494 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e7ad1fc3-4d55-3c5c-b1d8-e4025e4cee4b | -10.33731 | -47.72908 | 2025-09-09 04:34:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 271bab75-e9c2-36c3-ade5-75bb430330bb | -8.03941 | -48.64081 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63fe5276-5713-3c6a-867d-7ba476e58ca4 | -12.96426 | -54.76447 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e2f66df-9364-3211-b408-4b733355ccbc | -13.94584 | -48.23984 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dbd77041-cf50-3ad4-b14a-2f6d2717268a | -12.81581 | -47.02934 | 2025-09-09 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 855cad63-b3d6-3287-ab95-58c04d1d834f | -8.03014 | -44.51063 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5d1e63f-9018-3933-bb55-6e00180db370 | -13.80567 | -46.28954 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 49b8896b-125e-387f-a964-ff06fbdad2c5 | -5.89598 | -53.84066 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8126db54-eeee-36a0-a9c0-fafce9835f51 | -12.19179 | -53.87968 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82ad7fd7-7b75-3297-ba81-29049e3621b4 | -7.71589 | -44.74673 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78fb430f-eff9-3e7e-9f2e-2ae6ac12640a | -10.77271 | -47.72641 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04398b1a-a59f-3a05-af05-db06e5b59904 | -7.86914 | -46.25308 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88c3a1f4-e7ac-3f74-9824-186c06aeed8a | -13.13339 | -54.9209 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e4d2750-8314-3a0c-a820-89dd8466e23f | -6.2742 | -53.42065 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67d2d471-a760-3694-9b24-2a4c8ed9d40b | -11.3451 | -46.57669 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f46aae31-fa09-31f5-bd5c-c94f2baadb33 | -7.43324 | -45.2131 | 2025-09-09 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 91e5cd2f-ca62-3cde-9cc3-b30169bf56f7 | -12.19343 | -53.91568 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ed8a4a9-05ce-3ab0-90cb-3327340798dd | -11.19707 | -55.00225 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6da043ad-d81f-3769-9393-7998b6563791 | -9.71044 | -46.82635 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d040ff51-823f-3d12-929d-d8e8f418beaa | -12.89084 | -47.9832 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3daabb2-c7aa-3776-b4bc-aa2347141a5a | -13.80262 | -46.25892 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb15c4e2-0668-3731-8d8c-f130a6c48cd0 | -9.78124 | -46.23778 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8f353b8-71fb-35c0-84bc-a2ce53a87828 | -13.94302 | -48.23564 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ccd4155e-150b-3b6d-a1bd-995e8667d0c9 | -13.29196 | -43.73424 | 2025-09-09 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fedab9a-6391-32c9-8acc-5df423f3cf02 | -9.04308 | -49.80639 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ed93b28-41dd-335e-b81f-071d8cc1ea08 | -8.4502 | -47.29061 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a09b9b0f-24dc-3ce0-b8e5-b360123f304f | -12.94772 | -54.81056 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d9a378a-e077-3c77-8547-1722910df552 | -9.85109 | -47.7952 | 2025-09-09 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0f4970e9-0f5f-369a-af21-613215d94f75 | -8.23572 | -43.03438 | 2025-09-09 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1fd8d355-99c2-3466-bec0-40c9153e1eab | -8.00905 | -46.34711 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37b1baac-9e98-30d0-bc85-4f85e079b767 | -11.4287 | -43.60576 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b57043bc-e71a-31c0-af87-bbd776a356ad | -11.67109 | -46.88668 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fd45b91-78a7-345d-86c7-89e3b80885b8 | -9.21778 | -60.82675 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 55ee092e-5860-35f7-a775-34c98ccfc05d | -9.81489 | -47.76417 | 2025-09-09 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a85ad9d4-363d-3eb6-8bf0-12d78a047da8 | -9.17363 | -59.3747 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6cc98674-0e14-3c44-8724-b1caf62dcd75 | -9.96274 | -51.18596 | 2025-09-09 04:34:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d43751c-c439-361a-8570-991d69e22d75 | -12.02304 | -51.0782 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b68a95f1-1908-3678-98e7-7552c56d55c5 | -12.57437 | -43.78328 | 2025-09-09 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c09c6458-63b3-32ab-a1c4-486e9248dd21 | -12.64237 | -56.97487 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d167e9ef-e62c-3062-a874-36746d05cb08 | -7.79129 | -52.12414 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3c5304a-4752-30bc-b4f7-d5cd5103ce37 | -7.71351 | -44.73739 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 864eb8bc-f2c5-3ade-9252-e6e20a6910c6 | -8.47692 | -47.31282 | 2025-09-09 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61629517-34ff-3d30-8c1a-b7c7fbb37817 | -14.33365 | -47.30725 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b40d8b6f-eb42-3127-b99a-6bf249f1570d | -11.84131 | -46.77159 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 443d5c1e-b072-30f2-8ae5-1fcb67504946 | -9.78473 | -46.23836 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94b83c34-f436-35cc-a32d-35e297c83a40 | -11.20977 | -55.00438 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e8f5f097-cd31-3933-997d-b3728ff5f615 | -7.82242 | -45.41748 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3e2ccdd-6bec-3920-8302-d0101975aeec | -7.80253 | -46.6188 | 2025-09-09 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acf60fc4-4105-3a74-8d96-a15fab541349 | -11.95456 | -50.97943 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3350c0e9-3442-345f-98fc-e99b0b0bb612 | -8.67865 | -47.19748 | 2025-09-09 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea7f036a-a661-3ecf-83cf-afb7320f9740 | -12.63299 | -56.97301 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c830d2c-e5be-3926-84ac-f33a8cded870 | -12.93479 | -54.7892 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 401cc796-ef0b-333f-b8e7-e9e8e5fca7ed | -8.02983 | -47.28331 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e0cb269-2be6-3e93-9159-dbfd8d5601b2 | -13.48818 | -48.20936 | 2025-09-09 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54338b82-1f83-39a6-b640-f7314b57d59e | -11.55118 | -49.04834 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfd2ef16-cb06-30f5-8cc8-2095de8fc3db | -13.75383 | -46.89832 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ff773aa-bb1c-3db2-a393-79c538959906 | -9.102 | -49.5209 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 020c82ee-917f-3ff2-97b1-e309d741c90d | -11.44011 | -43.64611 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75f664f2-50e1-390d-adb5-586c08c9e146 | -12.82036 | -48.17667 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3254cb96-ce6c-38f2-b443-15754cd241ce | -10.30794 | -51.7127 | 2025-09-09 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccd78268-8284-37a5-8cd8-73d2d0bec66c | -9.44846 | -60.5153 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f46e601-db4e-38bc-97bd-0d1b7bae9b26 | -13.01336 | -54.81863 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e1b1620-3dfa-3651-b1e4-5307b0085cc0 | -11.36895 | -43.53172 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2d4c10f-a764-37c2-9992-208fd73ce6b4 | -7.14423 | -46.06078 | 2025-09-09 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 809cb327-2154-3407-97b6-38df542c4f2c | -11.95177 | -50.97515 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e7e29b5d-d623-3abc-88e9-eb88c89225ac | -9.4437 | -60.51751 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81e4b2ae-1ffd-36ab-9e22-eb3f21be4820 | -9.16199 | -60.79803 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 529ed987-eccb-3f9b-9ff5-0366fb920ad7 | -11.84423 | -46.77594 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4abb8cb9-98ae-3f0c-9ac1-ccbd932177af | -11.98302 | -51.01848 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1975f916-a36e-331c-9b96-bdaa46d03828 | -12.4853 | -53.88107 | 2025-09-09 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91eaa7e4-0ba9-34c3-b0f8-4ff4c55d058f | -11.81215 | -46.76452 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65adf5d5-354c-34eb-8004-955f52b5ccd0 | -10.56838 | -52.00159 | 2025-09-09 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78d911ca-cc57-375b-8930-faf33466ad0a | -7.70628 | -45.15872 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cec06339-9633-3d6e-b02e-6d63413c632c | -12.82716 | -52.93458 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f41496e3-b59f-3cce-b859-0ddd07b03e33 | -12.92801 | -54.78038 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README43.md)
