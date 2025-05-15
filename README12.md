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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca23bd11-dce8-3942-b175-a8ccb3ce4eba | -11.00921 | -50.75942 | 2025-05-15 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5aea816-3d5a-36fd-ab3e-62805708ad15 | -12.12049 | -54.66417 | 2025-05-15 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0e01375-ce45-38f1-b06b-e6c1c6f74ffb | -11.42547 | -54.33062 | 2025-05-15 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f914a7a1-8902-32f5-a10e-273f839ca057 | -11.5599 | -47.61343 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 219fa6b6-996b-33d3-8be1-8c745334e735 | -12.35192 | -49.95872 | 2025-05-15 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a32ec84c-27e5-3340-b2bf-2c5f39517d80 | -12.87241 | -55.06692 | 2025-05-15 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cfc4449-5d68-37f9-8b47-4ad4e02dcc97 | -12.2903 | -52.47081 | 2025-05-15 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68288a84-e42e-3ffe-98b9-09a897b605a9 | -11.65164 | -58.26313 | 2025-05-15 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4b6478a6-d387-33d4-aef7-7416dcf7ef97 | -11.78891 | -47.35938 | 2025-05-15 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91f736d9-cc1a-3662-bd6e-42badf947450 | -11.89243 | -56.40804 | 2025-05-15 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21bcb1fd-75ed-384d-b23c-8b73c61f3f94 | -10.66845 | -57.63621 | 2025-05-15 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ff829b8-e4ea-38cc-aec7-d039ed104fcf | -11.56626 | -47.43849 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e353a8a8-a037-3ece-8fa8-28bd995a6d97 | -10.10742 | -57.85584 | 2025-05-15 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f813f311-07cd-38ea-a35c-e27f740daf74 | -8.58704 | -45.88923 | 2025-05-15 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 267c6e8e-b244-34a9-b396-2322ec9ff165 | -11.5541 | -47.61729 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 37eb4b4f-2ed9-36bb-a75c-88432f8b54ef | -13.04174 | -53.71883 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 849d6ae7-d7d0-3018-a639-7b41828d8856 | -11.7896 | -47.35348 | 2025-05-15 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d88370a-059a-3ce4-8eb5-6eb9b25f4a96 | -11.24019 | -49.49026 | 2025-05-15 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4155b2e-28ba-3208-80fc-4dbe9ddf52a9 | -11.24602 | -49.49092 | 2025-05-15 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba63304e-62d0-3037-971c-1d4011b4406f | -13.04683 | -53.7148 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c41dbe49-9eef-3f26-bb7c-9f259846e5cc | -10.68522 | -57.59523 | 2025-05-15 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cf29033-bdf0-34d0-9d19-94ec42a5cfb9 | -11.65406 | -48.11021 | 2025-05-15 05:16:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a6fc559-cc38-31e5-b1e9-1900c97a3575 | -12.49289 | -54.40163 | 2025-05-15 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f5497ef-558e-3d0f-acd4-312ae320c04b | -12.35239 | -49.95477 | 2025-05-15 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cfc5621-9e9a-30e5-806a-6e56fca3ff50 | -10.46937 | -49.14173 | 2025-05-15 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a22e7582-8c2f-3dad-a31c-1e1fc6547f64 | -10.47525 | -49.14259 | 2025-05-15 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47086412-ce68-336b-b173-8002aac93205 | -11.56224 | -47.43703 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 04f436cf-98b5-36d7-9f86-4829b7f6f56f | -11.38453 | -57.8276 | 2025-05-15 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95a3cb3e-cfea-38f8-85b2-4d26e3e41b9c | -12.72456 | -54.97011 | 2025-05-15 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 622242f7-c1de-32ef-a9a0-dc82802a380d | -11.42493 | -54.33451 | 2025-05-15 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1596793-9f44-3e46-8cf3-06d5f70726a5 | -11.78548 | -47.35972 | 2025-05-15 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 03afc426-ace7-3aae-b73f-b165c9677f90 | -11.89434 | -56.41055 | 2025-05-15 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a46d281-0a27-36b7-99ae-182847d64a5d | -11.63353 | -54.94268 | 2025-05-15 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ab75e2e-7f25-35fb-8cbe-dbc71c921a52 | -8.59296 | -45.88255 | 2025-05-15 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9f15a33-f6fa-308c-8e42-053c73c422a3 | -8.72025 | -47.97745 | 2025-05-15 05:16:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44c1ab39-4a55-389e-8ff4-2dfddbd1ffac | -11.65735 | -54.94976 | 2025-05-15 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf8b6b0f-65fc-3788-983f-36bcdb4bb023 | -9.9306 | -59.93841 | 2025-05-15 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3ad3d27-23e2-3291-82fe-61952debc09d | -8.58586 | -45.88229 | 2025-05-15 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f807ae8-f22c-35ba-9dd6-1352ee9bb56e | -12.19681 | -55.21965 | 2025-05-15 05:16:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e011e78a-07d6-3562-b0fe-90e8181eed90 | -8.72089 | -47.97255 | 2025-05-15 05:16:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4e57deb-a41a-3018-a37f-b193448539be | -10.33753 | -47.97742 | 2025-05-15 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71d35fe9-27e8-3b5a-acd1-ab0754a5e242 | -13.04233 | -53.71423 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 14872153-0742-322a-982a-03c783a8d8e2 | -10.68464 | -57.59913 | 2025-05-15 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 348cd6ed-5c2a-38c8-b630-1ca0550fb15c | -11.16303 | -48.67802 | 2025-05-15 05:16:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb71e9ae-7f02-3f47-bb26-e0f60eeeca72 | -12.08576 | -54.57667 | 2025-05-15 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39a7480d-5d57-3dd4-9fa4-d2e2bde2dd98 | -13.67213 | -53.93018 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 194a72e4-82ac-3f48-908a-aee313f06817 | -12.36392 | -60.80633 | 2025-05-15 05:16:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f2ff0e4-7525-345e-b2b1-ab65804a2370 | -12.12102 | -54.66032 | 2025-05-15 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 296c7d60-48c2-30d1-b07b-5a53fd823184 | -11.64767 | -48.10949 | 2025-05-15 05:16:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b0306885-2893-3433-86df-9672772dfdb5 | -12.20082 | -55.22029 | 2025-05-15 05:16:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad7ba7c9-388e-3660-af18-b889d8d7f249 | -11.56886 | -47.43795 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d03f0fe-f409-3260-b44b-b1e5076c9b9e | -10.76859 | -54.78063 | 2025-05-15 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 409fcf09-ef4a-30af-8884-f6432dca2ef3 | -12.14685 | -48.01499 | 2025-05-15 05:16:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a99bd80c-1b95-3a96-a6df-3a036d279116 | -11.59734 | -58.96083 | 2025-05-15 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 866b3acc-22d1-3056-ab5c-c216f6e50fae | -9.79622 | -56.13088 | 2025-05-15 05:16:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60df3e1d-870f-34cd-a5d5-12978b235c8a | -13.05074 | -53.71993 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1e6c0fd-b07b-31b6-ae0a-7ff9913b1629 | -12.8714 | -55.07437 | 2025-05-15 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c56aa9e6-6e4c-34e2-a3b7-a5dd1489056c | -8.5879 | -45.88253 | 2025-05-15 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8126fff6-31db-309e-8d5d-011c8d43b9fb | -10.66498 | -57.63568 | 2025-05-15 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aa6c8f3-081d-31b2-b8c6-edfdf067af20 | -12.1973 | -55.21608 | 2025-05-15 05:16:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4430bab-385a-3081-84bc-43ac7cda4826 | -11.91072 | -54.40667 | 2025-05-15 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 443b0c6a-a573-33be-84f6-3a9c4aade762 | -13.03724 | -53.71825 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5843308-a448-35a4-aca2-e3ac0d6e346e | -12.8719 | -55.07065 | 2025-05-15 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8324f627-8025-3f55-9f24-3a69a4e6a042 | -11.6278 | -48.475 | 2025-05-15 05:16:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af0a27c6-f3c1-39f4-950b-263d5d9b38af | -7.94905 | -49.76542 | 2025-05-15 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 11f4a307-0290-3d84-a4c3-9fb224942354 | -11.38799 | -57.82814 | 2025-05-15 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 965269eb-42b0-3fd0-9f27-dc3494d89914 | -9.78885 | -56.12976 | 2025-05-15 05:16:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c37fd9a-88f9-3f46-a339-c4523a104e32 | -13.62005 | -54.88095 | 2025-05-15 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceac3476-9a6b-3916-9b1e-5d22a21941bc | -11.60069 | -58.96138 | 2025-05-15 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2766fd7-5d02-3876-a518-3a0ff3accc8b | -11.15137 | -48.67168 | 2025-05-15 05:16:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7144b07-c0be-3043-9db0-95729bede5b7 | -8.58873 | -45.87598 | 2025-05-15 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74ca853a-f640-36dd-876b-6a0a4e02c337 | -11.55271 | -47.61812 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0f70df1-1c34-31d5-a553-af72c24a93f1 | -11.56816 | -47.4438 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 907e7cde-b42b-307a-bfc9-1ef86f38c05a | -13.66765 | -53.92972 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4a50474-9881-3e60-8838-987181cf987b | -11.94029 | -61.99302 | 2025-05-15 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7ed2c0b-7b4d-3c94-93af-eed5a788e543 | -11.77619 | -47.3522 | 2025-05-15 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8699478d-cc41-3d81-acb8-a4f255f03ab4 | -11.42072 | -54.33392 | 2025-05-15 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8268dba-b73a-389b-a6cf-d82ceb3559ec | -13.08857 | -54.87204 | 2025-05-15 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d56cbdd7-07c4-316f-8066-b8da3d1eac06 | -11.66089 | -54.95399 | 2025-05-15 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6eb3337f-abe9-3b2c-a072-153e9260276f | -8.71107 | -50.24638 | 2025-05-15 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a05ac0d-affb-322d-afbc-ded1c32341c7 | -11.77943 | -47.35321 | 2025-05-15 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f1b3aff8-3afc-3984-a197-4157fad078ef | -11.55332 | -47.61269 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85de266a-01da-3d9a-841d-8311f09169e8 | -11.62836 | -48.47 | 2025-05-15 05:16:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 443e0558-f62d-3b80-bf2d-3c3e2c5362c2 | -10.47472 | -49.14682 | 2025-05-15 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92ac4918-2aae-32ac-8bac-5697f3b7cd35 | -11.42126 | -54.33004 | 2025-05-15 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 879c37f2-e3ad-3ecc-b892-a0e10b48100a | -12.86882 | -55.06258 | 2025-05-15 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a0f65f1-8c9f-3b88-a1d4-7528b1c5a695 | -11.6614 | -54.95039 | 2025-05-15 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 886e344b-602a-322e-8f78-a8931578d451 | -19.17271 | -57.54018 | 2025-05-15 05:18:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 840bec25-4bca-3237-8637-157cfbfd3016 | -15.26515 | -51.45913 | 2025-05-15 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc919306-06da-3927-a357-fb1b1a4bc441 | -15.26475 | -51.46262 | 2025-05-15 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cf2095d7-4aac-3eab-8851-78505538484f | -15.26395 | -51.46963 | 2025-05-15 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e97a0d1-f46f-358f-ad81-77df06e78072 | -15.26435 | -51.46612 | 2025-05-15 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ae527cd0-e05d-3dd4-9398-8be932962c84 | -19.06707 | -53.45311 | 2025-05-15 05:18:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c3ae73b-8014-3f92-9df9-937eb8e472fc | -19.15334 | -47.81914 | 2025-05-15 05:18:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd841b67-c563-389d-b443-bb7a1e72a670 | -16.6133 | -53.40874 | 2025-05-15 05:18:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3ce8092-644d-30c6-a590-e8887ccdafbb | -14.06731 | -57.11208 | 2025-05-15 05:18:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fa47566-8c82-372c-a57f-e70d1a1072b5 | -19.0621 | -53.45253 | 2025-05-15 05:18:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6c36ad7-171e-367e-8450-209a8d43edc5 | -14.06678 | -57.11042 | 2025-05-15 05:18:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41c2993a-7f0e-3b64-b517-78785a2971f0 | -13.48781 | -60.37791 | 2025-05-15 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4928247c-cea2-3d36-b79b-7a9ab5ae25fe | -19.0555 | -53.4574 | 2025-05-15 05:18:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
