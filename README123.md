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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26197d2e-72ac-3345-9acc-745f43ecc597 | -9.90262 | -51.86726 | 2025-09-12 12:36:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| eeedbaa8-0609-372a-b128-8124203fe37d | -15.10964 | -48.02185 | 2025-09-12 12:36:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 7e2248d2-4066-3a3e-95ac-2d909ba2a964 | -11.96114 | -51.12326 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 812b4049-c0da-3c8b-8955-cf5c032dd1c7 | -9.90134 | -51.87618 | 2025-09-12 12:36:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| ba5fecfc-9f9e-3ddf-b431-929dd4f5165a | -9.91144 | -45.98773 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 26fd840a-ddea-3d29-b150-4cd9b1a73c87 | -8.86441 | -47.26386 | 2025-09-12 12:36:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| bd0c7349-dba6-3a6e-a3d1-592201500036 | -11.31696 | -50.78807 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ae805d0a-35a5-3149-b840-bfab8635f631 | -12.10642 | -44.86423 | 2025-09-12 12:36:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| eaee3b95-a0a0-3d73-9a29-321ea5e0972c | -11.7829 | -51.41301 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a6e04972-5cd8-368e-ba65-0bb0111d965d | -11.44725 | -48.57144 | 2025-09-12 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 295.0 |
| 77759627-7b78-32fc-8bb1-8dd58bffd8a6 | -10.41559 | -50.58531 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 75a9173c-a76c-3cfb-8e68-2ac485b7f499 | -14.33139 | -54.12377 | 2025-09-12 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 13bb6c47-849b-3288-87ad-81d22e337f58 | -11.71812 | -46.59533 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7f363cf3-512f-3034-92a9-ddb9bc4db409 | -10.88929 | -45.58525 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| fcee6303-6046-3641-9ec2-78e306d289c8 | -14.43374 | -52.92625 | 2025-09-12 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 27a18e8d-2909-3a35-8558-c41ae7e884ba | -11.11595 | -50.71283 | 2025-09-12 12:36:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c13347b2-5902-3d1a-9652-c5cf08c671a0 | -9.71873 | -48.30964 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ecace87e-6f2b-33fa-aa0e-4ee831fe600b | -13.1781 | -50.08356 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8433ed34-f317-34dd-bd0f-7f30d7582681 | -11.54701 | -50.58853 | 2025-09-12 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 397e5b75-927a-3217-beac-0ff168279746 | -11.43695 | -48.57009 | 2025-09-12 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 174.4 |
| eb111e60-a4b2-3f5c-a8ca-dbe5c036fc5f | -10.37028 | -50.51136 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 1f71d254-b5ee-3b6c-8ecc-9aad454659cb | -7.66636 | -50.28462 | 2025-09-12 12:36:00 | TERRA_M-T | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bc9b48c8-fab8-320b-8ecd-da321d036a18 | -9.75917 | -45.74907 | 2025-09-12 12:36:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ee0a7d75-066d-3b41-8e17-906134e25467 | -15.0772 | -48.01122 | 2025-09-12 12:36:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1522137f-2f9d-390b-b006-b3a58085141c | -11.11941 | -51.34411 | 2025-09-12 12:36:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 1b350014-d137-3f37-8383-63cd0c288aba | -7.66765 | -50.2755 | 2025-09-12 12:36:00 | TERRA_M-T | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3f751ff9-c176-3a74-bae3-7df6b4002e81 | -11.72598 | -46.6308 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 30639989-b828-3de2-b86a-f75b4fbcac9e | -9.83257 | -54.54021 | 2025-09-12 12:36:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 19da9129-344c-3811-92b4-ddc90ed5dad6 | -10.8764 | -45.58345 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.3 |
| ec4d4d43-6df4-326f-8aa2-d7209baf0226 | -9.61714 | -47.90744 | 2025-09-12 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 052f237d-9199-31c4-b42b-3ebd2e2f02ae | -9.95437 | -50.32553 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| fac614d0-99b7-3548-9099-db46ac031562 | -12.99102 | -46.74684 | 2025-09-12 12:36:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 29.9 |
| e9c93aec-834e-341c-b0ee-881701a00467 | -13.46331 | -51.77299 | 2025-09-12 12:36:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2aeba7e6-0346-3e5c-b8d4-7c2ec115718c | -8.90299 | -49.94022 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 308977f6-6d15-3d0e-9291-c6c9cdcdf8de | -11.69831 | -46.55647 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 1f3955b4-1a11-3181-92a9-74f0e56dca4b | -11.97395 | -51.16319 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 41.7 |
| b21026cf-f0f9-31ab-9de4-4383af158736 | -10.71651 | -48.62502 | 2025-09-12 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7baf27c1-e9e7-3b42-b335-aef600ed71a3 | -8.95658 | -46.72594 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| abff2a34-417d-3427-a70b-3b2df3ab6402 | -12.0004 | -51.17286 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 41.1 |
| b5000523-5252-389d-8c27-08242a702ce6 | -9.99731 | -51.72348 | 2025-09-12 12:36:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3a2ff23c-0aae-37f7-a8ec-748066a4b686 | -8.48256 | -47.26812 | 2025-09-12 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| b3cbd8c2-a688-300c-aabc-c013e5ea28b4 | -9.76629 | -46.01844 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ca7e1b10-2d31-34f9-bc64-ad479a4e6af2 | -12.66794 | -45.32542 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 97c9a5f9-705d-32de-b25b-a74452767ffb | -11.49007 | -49.25513 | 2025-09-12 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 92c34df1-a111-3697-a9f7-2acca51ae114 | -11.19 | -48.43163 | 2025-09-12 12:36:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3db535bf-81fa-35cd-8445-97ec351c92ad | -10.22125 | -46.23404 | 2025-09-12 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 10e5f9f2-0a67-3786-9f7c-8f59b3a2bf5b | -11.42979 | -48.5633 | 2025-09-12 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| ef985ff2-39bf-35d1-936e-1487612fcd9e | -9.06455 | -47.03668 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 2a29d70b-c52d-3ada-b999-03d089a427e4 | -14.45139 | -47.31298 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1179b86c-c390-3c4d-9738-bc0081ca01d0 | -9.34719 | -45.39842 | 2025-09-12 12:36:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| d09ed089-1bba-3bd9-89c6-f54c8148f1bc | -8.18858 | -46.10277 | 2025-09-12 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| d87dbf13-2f43-3b58-ab4b-4101aa7c655e | -8.89378 | -49.93896 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 35385237-9e4e-3fba-be36-ea79a710b661 | -9.07654 | -46.94755 | 2025-09-12 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| af893328-5697-3070-b3e3-91265f2380ea | -12.92762 | -54.74984 | 2025-09-12 12:36:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 16a672cb-55e8-397c-9432-b2f4deb431ff | -11.97526 | -51.15385 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f5fc9add-a565-3030-a61e-6ea9e8c75687 | -11.95212 | -51.122 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 58d3a155-017e-3068-9663-ae78e5dd8546 | -8.50161 | -47.31849 | 2025-09-12 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 519f1469-9185-3dcd-8470-43369507f629 | -8.73205 | -46.69457 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 440cdad0-d6c5-3ca5-8f1c-fb6f5979b679 | -10.54896 | -51.53127 | 2025-09-12 12:36:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c3f623da-4340-3153-9943-0357908fe5bd | -8.37469 | -44.82955 | 2025-09-12 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 62cd9b23-93ed-3a45-859f-b3d4a9b188c7 | -12.00169 | -51.16352 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 359dd1f6-8d2d-3f98-b2fe-ed967626a049 | -11.42627 | -43.54829 | 2025-09-12 12:36:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 75c6b5f6-eccc-32cf-a6fc-0456187cc14e | -10.68294 | -48.65195 | 2025-09-12 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 82d80bee-496e-3da6-b758-1f94c8bac184 | -10.13982 | -47.91375 | 2025-09-12 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bb53e3e7-c910-3d72-9254-3a50831a215b | -14.39495 | -52.93249 | 2025-09-12 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 02c8dfbb-71a7-38b2-8966-fefef533a2b0 | -9.34778 | -45.39197 | 2025-09-12 12:36:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 89f89193-f0df-3f6a-8b40-b35b2a65c453 | -10.54768 | -51.54022 | 2025-09-12 12:36:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 312aeb2b-b8a9-34d6-a951-069d1dac3644 | -9.47766 | -46.41934 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 7532db65-d4ee-3afd-a26e-90a9844be6e8 | -8.08715 | -50.17551 | 2025-09-12 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 79b2ae00-e376-301a-881e-a62e6c487184 | -7.32587 | -49.63224 | 2025-09-12 12:36:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1ae957d7-5c85-3d34-b397-31b637b33181 | -8.41745 | -47.25959 | 2025-09-12 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| a9e6be97-bbb3-3088-bff9-937432ab5668 | -11.20695 | -48.38218 | 2025-09-12 12:36:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fbf63e23-983d-3c37-914d-23c068053bf2 | -10.71806 | -48.6132 | 2025-09-12 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| dc303a4d-be2c-3fae-835c-38512b601957 | -10.07989 | -47.16336 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 02e46756-b96b-32ae-a18a-587e971acb3b | -8.7303 | -46.70021 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 914e002e-2ed2-3329-85ce-f5ef26dfff14 | -8.87735 | -51.11013 | 2025-09-12 12:36:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c336ff8e-82f9-3bdd-b411-f292f141b5b6 | -10.20915 | -46.23232 | 2025-09-12 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 1d9badd1-29ce-3489-bebb-f1ba66f42c3d | -12.91825 | -54.74838 | 2025-09-12 12:36:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 7b38661d-cd9e-3154-b49d-53b0135d1ea8 | -9.77609 | -47.84825 | 2025-09-12 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 02d10a5a-70c8-31b8-a5c9-fbbe753f7b54 | -9.06666 | -47.02793 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| bb009831-a73e-397a-ae63-75ac6a4628ea | -9.06481 | -47.04249 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| c9b4d8aa-8630-3f78-9004-7db3299c568d | -8.1825 | -46.09521 | 2025-09-12 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 23af3e91-9d08-3c39-bf3e-12912b2fa2c0 | -11.92843 | -50.69567 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 59d9c882-8f4f-3f51-9368-0c9118a248d0 | -8.03979 | -52.37 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0e9e9257-c037-3f02-aaf0-e682bf7ddf3c | -8.41565 | -47.27335 | 2025-09-12 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| a5f2fb0c-db9b-32e5-8188-72b344ef2076 | -14.40511 | -52.92472 | 2025-09-12 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 0f1403c1-9ef2-36da-8b38-1c74c1faf5c3 | -9.78039 | -47.85558 | 2025-09-12 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 92147e53-c8fc-3ad9-ad6c-103adfaefc79 | -14.60532 | -52.03661 | 2025-09-12 12:36:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f0bc8c20-751a-3c9a-a7f4-9dbc2f887b46 | -13.46462 | -51.76369 | 2025-09-12 12:36:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 28f7e5e9-a8ad-3e64-a0a7-a837d18b7ce0 | -10.87762 | -45.5682 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 229.4 |
| 44386a1d-fa29-371f-882b-317caf8de427 | -11.7104 | -46.55806 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 156.0 |
| b05bcf56-26b7-3eec-b211-2405fecadbed | -8.89513 | -49.92926 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a484a894-e957-3a78-b457-d5cf52ca96fe | -9.00945 | -46.12356 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 5f51b6f9-4c3d-3be9-9315-a424df41bdcf | -10.68131 | -48.66395 | 2025-09-12 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 40a122b4-4d3c-3c56-979e-9e75bc102459 | -9.73873 | -48.08494 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 43380cf5-9bf8-34fb-bcd6-21a2d921dd6b | -9.03288 | -47.1044 | 2025-09-12 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 59c8fa59-779e-3cac-b065-1bc95cced6a9 | -8.94516 | -46.7245 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| aeab8d81-a564-399e-b314-6b3879d52f8b | -15.12003 | -48.59805 | 2025-09-12 12:36:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c906e69c-d5fa-374e-b9db-619e4317e70a | -10.58868 | -47.2139 | 2025-09-12 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 368bb117-66b7-30ce-ad59-697197939724 | -14.25207 | -53.40709 | 2025-09-12 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |


[Clique aqui para ver as próximas entradas](README124.md)
