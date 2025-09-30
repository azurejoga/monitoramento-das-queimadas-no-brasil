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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9be511d3-50e5-39c7-8a3f-ad99476ee10c | -11.88553 | -49.90726 | 2025-09-30 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4661ede5-ca6b-37e2-9fee-7c0b2fa46f69 | -11.03477 | -49.81683 | 2025-09-30 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60d107ed-a156-351a-9cfd-8e7b74813fe8 | -13.21119 | -50.92782 | 2025-09-30 05:08:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61068f83-78bf-3df8-a158-d44432e5c6b9 | -8.87839 | -46.65365 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 2ca60dac-6b82-3ef0-812a-88853d12c9d2 | -6.84202 | -44.83448 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 791a1965-6d35-3bfa-a56c-0a016e3a7829 | -10.60343 | -49.63492 | 2025-09-30 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd561707-b45c-39c3-9d0a-7a98b85fa9ad | -11.20088 | -47.22612 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d20fbb36-7e66-38a3-80b6-d54fada5621b | -8.87819 | -46.61265 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af8b28a8-2dfa-36f8-a86c-586ac4dbd31a | -10.64807 | -48.58804 | 2025-09-30 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 31db4ff9-ee28-3184-b372-33e576526235 | -12.85132 | -47.00034 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8fd02900-447c-33ec-9bdd-4fb5974ca0ae | -8.94738 | -51.68824 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d897a74-cb89-39d1-a988-6e92976460a0 | -10.01754 | -56.19821 | 2025-09-30 05:08:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fe63152-fb8a-3365-8abd-13f36f387dca | -9.29826 | -54.50204 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87245ded-ee8a-38f6-8196-45e8e4f9b24c | -10.89094 | -53.73756 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad1d0950-64f1-3bf8-9ee3-7ccf18d2d637 | -8.72139 | -50.04496 | 2025-09-30 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bbc5bf6-add0-3cad-b53a-c603d9a294f7 | -11.42941 | -43.50415 | 2025-09-30 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5d44148-7f3e-3d9b-9a78-ff1314be4b0f | -7.83125 | -46.99531 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4b495a6b-5fcf-34b0-a122-617a9dfc772a | -10.40241 | -49.04757 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8625ed8-5f78-3320-bdbf-747ec05fbd0b | -6.83583 | -44.83429 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e58f0ea3-6ad4-393a-82ec-456a1661a686 | -12.79482 | -46.8864 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aac0b76e-d1b5-321b-82ba-2d88d64cef10 | -9.40847 | -54.71818 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0fcb9bc-11fe-3fd0-9f42-d74483b324ef | -12.415 | -50.19711 | 2025-09-30 05:08:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b2d19a9-7760-3d88-bcc1-c5087768a117 | -10.0913 | -46.07567 | 2025-09-30 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f458497d-98ed-3611-9372-3192f6dfe8f6 | -12.4104 | -50.19645 | 2025-09-30 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ddd0df7-0f1b-325d-9d33-33a3022cd1a7 | -6.7545 | -50.92306 | 2025-09-30 05:08:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c343c31f-dc1b-3de0-98b8-b2dad2438deb | -9.41473 | -54.70011 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3062a807-a2f2-36f9-9c21-aaa112b683eb | -11.8777 | -48.05764 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26cf46ee-e157-3d55-94d0-20cd5e87c440 | -10.96191 | -46.48978 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fdd332f6-5197-3e93-8691-7edfa9eaf2b7 | -12.82188 | -47.00279 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc7b0c68-cc0c-3212-b84c-da5c84222ca8 | -11.74753 | -46.84115 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 025f660a-1e38-3db4-8c3c-6bfd323fc0ef | -11.2615 | -47.2255 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c90ee572-e8c8-36c8-b59c-8f2e2c5eee14 | -11.88993 | -48.04609 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da8d679a-bcac-37cd-afc5-3782f04d1d43 | -8.1448 | -46.36882 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5b71b380-77f9-3c9a-845c-40989a64792b | -12.87357 | -46.91246 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3543c028-6489-3572-8bd3-27145017da0a | -7.23497 | -46.76278 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20c0ae8b-c33b-32b8-8955-87094f78a320 | -12.84991 | -47.01204 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cc8dd9b5-c248-3dbf-b532-c8a8c1e839a4 | -13.57766 | -48.05289 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a72b901b-197a-3f49-b7f3-2676e3894e36 | -8.82952 | -46.1836 | 2025-09-30 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 291f7768-29ab-3b8a-ab90-46e253142dad | -11.88464 | -48.04535 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77797273-526d-3c31-a313-d4996b050177 | -13.01337 | -44.11956 | 2025-09-30 05:08:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e313f894-cf9b-303f-b263-89102508d5b1 | -7.79999 | -55.31194 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13624968-3ee4-34c0-850e-cd88baf3837b | -9.95907 | -48.80156 | 2025-09-30 05:08:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a345f4d7-1a7f-30b9-9734-fbf4d5f1d10b | -12.45208 | -54.30478 | 2025-09-30 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd24174f-4880-32df-8d64-ccbd4f89a693 | -7.82587 | -46.99466 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78f344fe-3e44-3aa2-974f-10a26511a0f3 | -11.29847 | -54.88755 | 2025-09-30 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64b26545-e1e4-3d19-9b7d-4a3aa62e75ac | -10.18722 | -44.88787 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 23cff27e-5225-365b-96ce-3aa94ecdc27e | -9.4153 | -54.69639 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 894ab5d1-4680-398d-8787-1e961519eca1 | -10.40021 | -48.16558 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d69d662e-c930-36f4-9b7f-8114cd436d56 | -11.19356 | -47.23975 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b42dec95-3d42-363e-aa9b-431313d6a5d0 | -10.66437 | -53.71101 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfdb4417-5d5f-328e-9a86-8e12f17c1a42 | -10.81867 | -45.36985 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b066d52b-25e9-3e65-b111-4fb649c581af | -12.87404 | -46.90854 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be9b9844-5cb8-3a43-b4b8-dd30dba5bee6 | -10.18985 | -44.89773 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b52417ce-0462-3d64-929a-884ddfdd944a | -10.03941 | -50.19396 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8b8e17d-7587-33d3-a7e2-c729601844e2 | -9.4233 | -54.71289 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0df1d537-9079-377a-9925-87c8dc618d58 | -9.413 | -54.6884 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80ca95a2-8369-36c0-b126-25b474c00b57 | -11.25815 | -47.2187 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e29f8d3e-d728-3aa7-be5e-586659eb351e | -11.20546 | -53.2996 | 2025-09-30 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2016dd9c-bc1e-354a-ade0-1c033b5c8726 | -8.53477 | -44.66788 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 700b3e50-fba1-3a85-949d-3fbbeb89c752 | -9.40731 | -54.70277 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16673f16-fe87-3602-8d98-c1d8b28ebbe1 | -10.63306 | -53.69781 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d6ee0f6c-fe38-3046-bd28-271f4d0ed75c | -12.87956 | -45.17487 | 2025-09-30 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1085bd64-86af-36b0-abf9-3d69958a3fbe | -7.91603 | -44.62594 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 497f7011-3f05-33ff-a2b0-2be71f6f86a4 | -7.87082 | -47.25866 | 2025-09-30 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 868fd18b-07c8-3124-a03f-7dacde94cd29 | -11.15818 | -54.11676 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c7627b4a-a9a8-30a1-8472-616e2bfbcf2b | -9.41702 | -54.70809 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b89840e-389f-3ef0-988a-e275202bb2bc | -11.74569 | -46.85568 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79929754-711e-313b-9b59-04e106d00ed2 | -7.70765 | -55.45286 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08748c7b-ee2e-38df-8ee1-3fa3d6d34bc5 | -13.59924 | -47.2822 | 2025-09-30 05:08:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf8be9fd-8e48-329f-8cc1-15954c2811d6 | -11.88755 | -48.02259 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b13ca4f-ae68-3135-aa09-40e63d24ea40 | -13.00584 | -44.11898 | 2025-09-30 05:08:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f855aef6-0d60-37c1-adc6-b8ae4a44906b | -8.44443 | -46.93397 | 2025-09-30 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9d270d9-71f4-3b3c-bd53-4b913adf39b1 | -11.03176 | -54.26282 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca4bd394-4a10-38c6-a80c-0ce9569b3c77 | -11.8902 | -49.90791 | 2025-09-30 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 741217c3-2780-36ec-820e-e20c3ccf7e90 | -9.41988 | -54.71235 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4ab4e11-af64-385e-a9d4-66c7dda56b95 | -9.69828 | -48.24358 | 2025-09-30 05:08:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5783699d-c96c-3675-b934-66940808c697 | -7.01532 | -44.46751 | 2025-09-30 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55a5d6b4-41a3-3e1f-9146-728ca5ae04d3 | -11.9083 | -48.06352 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a3eeab3-6320-3604-acef-0dffab9bcbf6 | -9.4216 | -54.72403 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc629556-2626-302f-a7b8-64b257a3eba2 | -9.55433 | -54.63302 | 2025-09-30 05:08:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6240aabe-847f-3ac1-85b9-0ac91360b3fe | -11.88381 | -48.05189 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42b5816a-7031-3746-980f-ccb3040581d9 | -11.64774 | -47.49313 | 2025-09-30 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f3bc28f-91f7-3107-b25d-83892179d73c | -10.40736 | -48.16725 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90b3bb34-9b3d-389e-8e9b-22134f12b2ef | -8.14843 | -46.38446 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a5c51784-298a-3ca8-9466-98017c885327 | -9.44987 | -50.9004 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 653f538f-bd66-3866-9681-b7ffb2048c36 | -11.22029 | -47.20599 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 118d60f7-90fb-36cf-9e71-73f52cf30a4a | -7.92329 | -48.18025 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e58c425f-fce9-319e-bea0-290b42816daa | -13.39806 | -48.07405 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5303a982-063d-315c-a06d-5e0de37cf099 | -11.24561 | -47.22868 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88c512e9-8f52-318f-b48e-1724420680aa | -13.0127 | -44.11986 | 2025-09-30 05:08:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b04a39ab-c93f-316c-b964-2a9cf80eb3cf | -11.43715 | -55.03747 | 2025-09-30 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45ed7364-18cd-3f23-8e36-1856753b3f2b | -8.0064 | -47.04974 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bafd0fb-c279-384d-b944-5796b15e93d5 | -11.30376 | -53.96088 | 2025-09-30 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f8d7819-4177-3a94-baba-714089a4f9eb | -7.91827 | -44.60942 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bbb6d3cd-da6a-3613-9ff0-e5cf7f7ab9ff | -6.87062 | -45.62611 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41ddcca4-91cb-3360-be64-33cf7ed0dfad | -11.65322 | -47.49369 | 2025-09-30 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6417dad7-1bf0-3911-aca1-1669b1853395 | -9.40448 | -54.72137 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3db14020-8d50-3819-b29a-ac84f71ca61f | -11.74074 | -46.84888 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c73f4bbf-f9b8-3ad5-9417-35c4cc370751 | -7.88713 | -55.44834 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85859697-9f83-37c0-a791-59b1f204721f | -11.17775 | -47.23468 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README86.md)
