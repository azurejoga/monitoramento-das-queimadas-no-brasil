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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b658aa04-ace1-38a0-9721-62829f788f8f | -11.20879 | -47.84882 | 2024-10-16 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c84d732b-c8e2-372f-945e-46f038e28d37 | -11.20824 | -47.85239 | 2024-10-16 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe4c5e76-0d1e-3165-8fe0-2c9d9a0fcafc | -11.20544 | -47.8483 | 2024-10-16 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4344943d-f3aa-3d7d-b62e-eea747ef8c9e | -11.2049 | -47.85187 | 2024-10-16 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bc9c956-351d-3219-af58-d6439bc204a2 | -11.20435 | -47.85544 | 2024-10-16 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 629ed7ff-56da-369b-8170-57ce8941e45f | -11.2021 | -47.84777 | 2024-10-16 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f59c10c-fed0-3e3e-9fe4-029a21d4c96d | -11.20155 | -47.85135 | 2024-10-16 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34406bfe-f5b3-3ed7-8e12-003748760420 | -11.201 | -47.85492 | 2024-10-16 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c71be165-5661-3b57-9dc5-ad52e5ccf9fa | -11.15654 | -48.73442 | 2024-10-16 04:32:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e3cbbde-bd95-3753-84a9-e5b6b3fbb6d5 | -11.15599 | -48.73793 | 2024-10-16 04:32:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd0b362f-bbf2-3b8a-99a8-0376eda3d7ec | -10.93082 | -48.74462 | 2024-10-16 04:32:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2742c38c-8b78-3c63-9627-816f2b2754e7 | -10.92751 | -48.74409 | 2024-10-16 04:32:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0c47d2f9-cdbe-34c8-87a1-0a2930ed0415 | -10.88572 | -49.13879 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0ca818a-cd32-3aae-bf87-e125032b97d7 | -12.52224 | -48.73001 | 2024-10-16 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d081b09-7601-3a4b-9611-a6bf6e6fbc5c | -12.38014 | -48.59462 | 2024-10-16 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11c36b62-4452-3064-8d64-348856f174e5 | -6.41704 | -49.59272 | 2024-10-16 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7db94ecb-f21e-35b9-b173-996d34d9c093 | -6.17348 | -49.07244 | 2024-10-16 04:32:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ff5ad3f3-2652-3798-8806-8f1e30cdc7f7 | -6.17013 | -49.0719 | 2024-10-16 04:32:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d35fcca-e5b7-3f2f-a80f-7b9f24df063b | -6.68348 | -49.197 | 2024-10-16 04:32:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fbd250c-ad72-3081-bed9-5f335440b411 | -6.66333 | -49.4633 | 2024-10-16 04:32:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eace7fc0-2e07-3c55-b41f-9893c4c841bb | -8.83602 | -49.88821 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f24d800-b3d6-3037-867b-e069180b2f43 | -8.75517 | -49.77828 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e5e706c-6eea-3061-a649-c7e0f5258e08 | -8.75181 | -49.77774 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61690299-14fb-3ba7-a147-b15af560e53c | -8.75123 | -49.78135 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 31f7f724-7b01-337c-80b8-015463744e11 | -8.74786 | -49.78082 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3854a3e-90cc-3fd7-8382-918aeebd20ed | -8.39778 | -48.92809 | 2024-10-16 04:32:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 386d1c68-f1d1-3ad3-9dbb-e391e3f63a8e | -8.39723 | -48.93159 | 2024-10-16 04:32:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bb82e97-8f37-3cb9-8149-1ac4c5d7db06 | -10.06856 | -49.55463 | 2024-10-16 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e61d852d-59c7-302a-96a1-765d295c29fd | -10.06799 | -49.55818 | 2024-10-16 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22b2f0ec-0299-331f-be3e-b9d16ddc1993 | -10.83489 | -49.2455 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef230492-bc57-3c9d-940e-bd4c770a030b | -10.83213 | -49.24146 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24d82296-59a4-33d3-80f4-96a9f5c3eee6 | -10.83158 | -49.24496 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 61c4c32e-851a-394a-b3d1-3f5dc7ed5dbd | -10.83102 | -49.24847 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8c285c4c-4f4d-3cf6-81a8-266bcb9c8767 | -10.82882 | -49.24092 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c00501d-0e5c-3d97-ace4-71663e2600c7 | -10.82827 | -49.24442 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a2373305-016e-37b6-9c36-513ab703feba | -10.82771 | -49.24793 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 594bc038-45ff-3265-9ffb-d2f8fb7370ad | -10.82715 | -49.25143 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59e84c95-a258-3cc9-a054-f05046589e30 | -10.82472 | -49.24419 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6e3a62c2-cb04-3df3-8afb-9c816fb52cfb | -10.82416 | -49.24769 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7d8d9b98-9532-3f62-b8f6-bc7754d555e6 | -10.82361 | -49.2512 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05282f95-cdf8-304b-b7a8-54370ea46ddf | -10.82085 | -49.24716 | 2024-10-16 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d987eb0c-ac02-37c4-9a15-5133cb9033c9 | -11.15022 | -49.6979 | 2024-10-16 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 676bb195-c78a-37cf-b4fa-3b227d6e58c0 | -11.14965 | -49.70144 | 2024-10-16 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7c0d0ac-5a87-3eb4-bb7b-bf78baf58a57 | -6.19278 | -50.88419 | 2024-10-16 04:32:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42749998-e73e-3e03-adc7-683be34acbce | -6.18918 | -50.88363 | 2024-10-16 04:32:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 623c2b68-aa69-3017-ba81-eb8e7ed199a8 | -6.18851 | -50.8878 | 2024-10-16 04:32:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bef69f95-3314-3603-83e8-dc0194b6fbd6 | -6.18492 | -50.88724 | 2024-10-16 04:32:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fed9b766-bffa-303d-9693-3561ab40551f | -6.10886 | -50.96826 | 2024-10-16 04:32:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c9e3fb7-a6f1-3b0d-b961-172ff2c9def4 | -6.10595 | -50.96349 | 2024-10-16 04:32:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d30fe443-2e87-3179-8aaf-65a8ee7f9cad | -6.10527 | -50.96761 | 2024-10-16 04:32:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67409ff9-f496-3896-b858-404054241612 | -6.81496 | -50.57663 | 2024-10-16 04:32:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be0f6779-f66b-357f-9117-ddea9e6a39cd | -6.32845 | -51.86884 | 2024-10-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1e8ab41-6e2a-31c9-911c-691171f8ee92 | -6.07324 | -52.34359 | 2024-10-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eb3e41e-771f-3d61-b927-b56f6b202811 | -9.18122 | -46.99862 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f781406f-09f8-3f09-a250-d1872bb12e46 | -17.21356 | -56.69348 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 2f3bc3fd-bd95-3c19-80b7-74d622c4497f | -17.21008 | -56.6883 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 92accfbc-0220-3f8c-8f01-05da624da741 | -17.20926 | -56.69259 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 3aed3ff9-2ab0-3853-8e51-df769581fbdc | -17.1665 | -56.82263 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 467cd7c2-bce4-36fd-9508-5efec2c53e6c | -19.59566 | -56.98806 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 25f45a78-4cdf-3844-b24c-e9e791f0d557 | -19.59488 | -56.99216 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 7e7ac556-bbb0-365d-89d1-c2112258ad17 | -19.59302 | -56.97895 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 2a05a355-f529-3f37-9cd3-f6549f1362be | -19.59224 | -56.98305 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| ceb8ac88-d80e-3483-a822-1978d900fffa | -19.59147 | -56.98715 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 724be150-2143-3629-9fa0-26cb3c513fd6 | -19.59069 | -56.99125 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 7e59710d-d372-39a7-b9c1-183ef7fd5a5b | -19.58991 | -56.99536 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 916e3ea5-532e-31be-85bc-ba809557cebb | -19.58961 | -56.97395 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| d244fb6d-f0e2-3eba-98ba-c6c9a9c19c9d | -19.58883 | -56.97804 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a2e9f70f-d9d6-3a58-8c1e-80abb8bcbacd | -19.58847 | -56.5357 | 2024-10-16 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fe685479-1f67-3aaf-b110-03704b65f07a | -19.58805 | -56.98214 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 873d8e10-fe9d-346f-9cd4-cc52c4fd5f47 | -19.58649 | -56.99034 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 6941d2fc-cf06-3c5a-bb11-0dd24304e29d | -19.58619 | -56.96894 | 2024-10-16 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| c6e2e012-0f2c-3bfb-b809-a115967b8d19 | -17.29907 | -42.65155 | 2024-10-16 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 33c91ff8-cbcc-33b3-9feb-97dc1f2f7c0d | -17.29431 | -42.65091 | 2024-10-16 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b2e4f69c-d9b2-3af5-ad09-7c1cfb8d079a | -17.25447 | -42.66157 | 2024-10-16 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cfb4448a-97a9-3c8c-8d2b-7c312f37bc91 | -17.254 | -42.65992 | 2024-10-16 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 92e00df0-1aba-363f-9a6f-e2e8bc26e960 | -17.24972 | -42.66093 | 2024-10-16 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 975db956-1d72-399f-a31a-ef6dae89bb20 | -17.24926 | -42.65923 | 2024-10-16 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 66c52e50-c276-39bf-aa67-7fcda7a7e316 | -17.24452 | -42.65852 | 2024-10-16 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0850471-a47f-30be-9e03-ffd0811d39cb | -17.0335 | -42.75147 | 2024-10-16 04:34:00 | NOAA-20 | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 564d34bf-3af8-315e-8adf-d370f40befa5 | -17.03039 | -42.75137 | 2024-10-16 04:34:00 | NOAA-20 | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc747630-9be7-3ab4-9046-74fb9f43bb9a | -17.74204 | -43.91144 | 2024-10-16 04:34:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb2e873d-d5d6-3fdd-979a-a5a3e25cf4ab | -20.45035 | -46.54701 | 2024-10-16 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4a73e7d-5496-3731-8da9-e6e963bc3879 | -20.71796 | -49.45103 | 2024-10-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 323f6b4d-4106-3d2d-92b9-35dd24062c3a | -20.58189 | -55.52827 | 2024-10-16 04:34:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c16a6bfd-58af-322e-9655-085652ed6048 | -20.58097 | -55.53324 | 2024-10-16 04:34:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9847e861-3b16-318a-80da-2c5fbf07b4cd | -17.164 | -56.83567 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3ed6fdce-2ab1-3e41-baa1-5dc402e16b26 | -17.16316 | -56.84003 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 045cc4fd-10d9-37cd-b5ef-7fee535da78c | -17.55479 | -52.67247 | 2024-10-16 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad4f21cf-ecbe-3613-827f-e630b8491268 | -17.16233 | -56.84439 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 66b584bf-185d-3bd2-8aa1-ec6daa0da9b7 | -17.15966 | -56.83476 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0dc89935-fc39-3c78-83e8-074fbb0d6bd4 | -17.15799 | -56.84347 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| d6b59627-3ffb-3415-9c2b-a6869dbe9665 | -17.157 | -56.82516 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 06568c65-8aab-38b6-986b-2effef74b06a | -17.15533 | -56.83384 | 2024-10-16 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| f2d2d853-04c1-37b4-88f2-7e2792db58b6 | -22.30604 | -41.8805 | 2024-10-16 04:34:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5013d39f-33fd-3015-85f7-1d4df2f731d5 | -16.06048 | -42.27482 | 2024-10-16 04:34:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6be95993-d435-3b3b-9ffb-a20d8020e54f | -18.32087 | -41.76241 | 2024-10-16 04:34:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e09df8f4-81cb-3368-b74b-56ec63dba0c5 | -18.31845 | -41.76338 | 2024-10-16 04:34:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2f3440b5-d033-3d1e-9504-02a470197974 | -18.31574 | -41.76188 | 2024-10-16 04:34:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b93d417b-774f-36a4-bdae-48406c020fcd | -18.29256 | -41.73716 | 2024-10-16 04:34:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4466cd6b-d74b-3f95-8e03-c2dd865dfb65 | -18.29222 | -41.74021 | 2024-10-16 04:34:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README53.md)
