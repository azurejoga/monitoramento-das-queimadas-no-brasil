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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2847f04-f4aa-3b21-aeb4-4c939da1ad1b | -10.8002 | -50.8243 | 2026-09-21 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 4838ec9f-59b2-371f-9d2c-d3c8fc13b9df | -3.3823 | -50.4486 | 2026-09-21 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9473637a-94ae-37ba-aef5-97088805ea91 | -11.9507 | -46.5033 | 2026-09-21 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b7ddc759-f637-3350-9753-aa45788a1f6a | -9.8307 | -48.451 | 2026-09-21 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| cb09ffdf-8a32-3bb5-a3b4-a3e6a07f302e | -3.3454 | -42.7597 | 2026-09-21 13:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a4bb5395-6922-3166-80f6-42078c9f263c | -10.3924 | -50.2275 | 2026-09-21 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 723327e7-fe61-3f7d-9637-fef31342f97d | -6.8263 | -55.5421 | 2026-09-21 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ddc5fcee-6133-3c93-bc67-16fc5f263d2e | -8.7726 | -44.28 | 2026-09-21 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 27a834da-7bab-3f0a-91ab-4844743367b8 | -9.0227 | -49.8262 | 2026-09-21 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a0419b50-a878-3965-8ae0-ff0e20ad2fe2 | -9.257 | -46.1873 | 2026-09-21 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4c812e2a-c749-35b3-bec1-36839e63da05 | -9.9768 | -50.2694 | 2026-09-21 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 1673e0b6-31b5-370e-8e66-20a120b21507 | -13.2787 | -51.795 | 2026-09-21 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 73d7beb7-fc22-322e-8fbe-9eecca1dfef5 | -10.4919 | -51.279 | 2026-09-21 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 8f94ee30-83be-3f08-9456-d35aa3dfbb03 | -10.8014 | -50.7391 | 2026-09-21 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 34b3790b-e36f-33e3-bb47-f5f4d43c448c | -13.3443 | -51.2973 | 2026-09-21 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 263.3 |
| a12be577-5a85-3152-9c71-129b853ecca2 | -10.336 | -50.2119 | 2026-09-21 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 93518223-b451-3bc9-8e2b-5ed65fa5a4d7 | -9.2759 | -46.1852 | 2026-09-21 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4171bf8b-36ba-3f4c-8b8f-c138aa6b9fd6 | -6.4486 | -59.9717 | 2026-09-21 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 968de10b-e7ad-3f57-be04-f2a05c4f6eed | -14.1819 | -51.7866 | 2026-09-21 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 12eb89c8-c988-375e-b93a-e18c5a742da0 | -5.841 | -53.5205 | 2026-09-21 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 80ec6d6f-6b4c-3dcc-b791-0e37e4f3ddbf | -8.7537 | -44.2821 | 2026-09-21 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| ab86b7c7-0125-3167-a5c1-3e5ac5675e4a | -10.6889 | -50.6658 | 2026-09-21 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d6f783b0-e310-3bed-8383-9b2dffa3d4d4 | -5.9334 | -59.9707 | 2026-09-21 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 238.6 |
| 461eba9d-8b86-3e28-8eb6-98dbad3c7d42 | -6.5571 | -45.5434 | 2026-09-21 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| fbc15346-98ea-3182-8266-e33ab9986467 | -6.4671 | -59.9711 | 2026-09-21 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c8acf325-3cda-33f5-b55c-37971225f32f | -9.8121 | -48.4312 | 2026-09-21 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9a3b9e64-b06d-3a9c-8e2d-d241c874e9bf | -10.4297 | -50.2663 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| fed5d2ae-3203-364f-9a93-d99a5718dde3 | -10.0898 | -50.2795 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 2a4a8c21-30a7-3430-a7c5-52898db60bd4 | -11.0509 | -54.9106 | 2026-09-21 13:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| bb56a30b-b1a9-365b-a3e0-8a8c15a86bd7 | -11.8715 | -48.9792 | 2026-09-21 13:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 82e2d70d-17c6-3ed5-908b-30c174a9ae5a | -5.9334 | -59.9707 | 2026-09-21 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 503ec88f-b385-31ab-a8f4-d58de30add17 | -3.3453 | -42.7832 | 2026-09-21 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 23ab0b76-115d-3753-b41f-19bc7509ded5 | -13.2596 | -51.7973 | 2026-09-21 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 0eaa69d5-1863-37d0-8232-c57555ca8062 | -3.3454 | -42.7597 | 2026-09-21 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 9eccd254-05c3-35ff-9abf-ee22e054cebe | -3.1698 | -58.5859 | 2026-09-21 13:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3bb3e6d1-11ed-3abc-a429-66ce79ace4e8 | -10.7999 | -50.8455 | 2026-09-21 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| ef3c086d-5069-3333-8555-ee4bc59f717c | -9.831 | -48.4292 | 2026-09-21 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 23cd1082-2212-36dc-8662-b560732e2e15 | -5.9151 | -59.9522 | 2026-09-21 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d1e76489-03f9-36c7-a283-92ab8645f6e0 | -6.4485 | -59.9909 | 2026-09-21 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a2294c3b-becc-3f1c-b3a9-2e8021aefda7 | -10.8921 | -53.9857 | 2026-09-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4ba6300a-e619-3f3d-a917-94f1e6b3efff | -7.3289 | -55.2155 | 2026-09-21 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 0095db46-8103-3de2-96c5-fb8c560018d2 | -11.1183 | -54.0062 | 2026-09-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 7f2f9bf7-065c-3825-8c66-a1e590317260 | -8.7726 | -44.28 | 2026-09-21 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 193.4 |
| fd1a2b01-2547-3a5c-a487-5491c77b7b8d | -5.841 | -53.5205 | 2026-09-21 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 73659bc3-a5ae-3e9e-b7bd-8a196c908a10 | -11.9507 | -46.5033 | 2026-09-21 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| df46ed85-ee54-3141-8352-1cc05f674a9f | -7.3291 | -55.1955 | 2026-09-21 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 7e33820d-c276-3b50-a915-a3b97602ca03 | -3.5653 | -43.4959 | 2026-09-21 13:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 5458f195-a469-37b3-a216-a2bb51766131 | -14.5406 | -53.3896 | 2026-09-21 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 507731dd-9eab-3d6b-b88a-9f1a5e818af5 | -10.279 | -50.2391 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 0713b064-b45e-3f60-8989-b925f2c0f703 | -8.3963 | -47.1899 | 2026-09-21 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 551c017f-20d8-340f-ad8d-600472b6b08f | -4.0142 | -53.4946 | 2026-09-21 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| bfbb6d19-0f32-3551-9061-cd3302dce26e | -6.1663 | -43.3506 | 2026-09-21 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 79e35c6f-237f-3627-b3bc-9c415e5b3a55 | -6.9225 | -42.9088 | 2026-09-21 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| affcb72f-d975-353a-b545-6a5aae5b1bfc | -10.3725 | -48.9153 | 2026-09-21 13:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 567ec1ad-0218-3d38-b448-cf2ecf9953e8 | -7.5704 | -57.6766 | 2026-09-21 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| d49c9fe2-c94b-3cef-9db2-94ee082ef299 | -10.43 | -50.2449 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 74a790a9-5e64-3553-9f4c-2d14ec4ce773 | -10.8472 | -50.1581 | 2026-09-21 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 401cd5f0-6754-3a7c-a3c5-f585670e33b0 | -5.7615 | -57.5807 | 2026-09-21 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ffe3aab0-2258-3eb5-b72a-66df531bd0f7 | -8.1874 | -54.742 | 2026-09-21 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 871517cd-12ec-37df-b9ef-3694da35e220 | -3.7129 | -60.5832 | 2026-09-21 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ba5be374-d44f-3a48-ab80-77025278fed9 | -3.6946 | -60.5835 | 2026-09-21 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ec7e572c-3472-3c93-b857-04e5f31840be | -10.8093 | -50.1621 | 2026-09-21 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| c7782b57-7cd0-3c4c-b36a-a271872961d5 | -8.7914 | -48.7285 | 2026-09-21 13:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d622b99d-a977-3236-ad13-2b303ae45c39 | -11.0412 | -54.1362 | 2026-09-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5e78ec1f-cb99-3f95-920b-3f1107755f6b | -8.7912 | -44.301 | 2026-09-21 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 4bee095d-18b4-3c7c-8564-393fef86cc78 | -7.428 | -44.7867 | 2026-09-21 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| a3ca9415-da48-3775-b157-d64d12a680ce | -10.336 | -50.2119 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 5fedf6f4-1305-3348-ae6d-a877916c36fd | -10.4917 | -51.3001 | 2026-09-21 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 584953a5-6225-3f11-9e00-b20e7424de0b | -9.9768 | -50.2694 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| fcf41bf1-fb21-35f8-b7d5-a8c7dfaf5252 | -12.9091 | -50.9672 | 2026-09-21 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 450c76be-7ffe-3200-9669-9045f5bfb330 | -9.247 | -57.1488 | 2026-09-21 13:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 3aa93e6a-1e21-3aca-9d31-3524580a72af | -11.6802 | -43.4209 | 2026-09-21 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 5208b2fa-66ef-3c2a-a9e2-09b54e9b2a60 | -13.2787 | -51.795 | 2026-09-21 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ebff0de9-71cd-3697-9bc3-0520b24a599d | -6.392 | -45.1948 | 2026-09-21 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 040d20b7-47bf-3b9d-b681-b93f7c26c78b | -3.753 | -59.419 | 2026-09-21 13:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| a514b6f0-3681-3c8c-8149-25b4e264f4c6 | -3.2817 | -57.8685 | 2026-09-21 13:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4254e9de-b656-3d8d-9a4c-aba56c89cc81 | -9.2759 | -46.1852 | 2026-09-21 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 0759dc7e-7238-3beb-af1e-9831a9a6d69b | -11.6798 | -43.4446 | 2026-09-21 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| d8c21443-a399-309b-b77b-1459542ca949 | -10.8735 | -53.9668 | 2026-09-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d7ae6346-a9fa-3f27-b647-f5ea5330554a | -10.4919 | -51.279 | 2026-09-21 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 54f38e60-ecce-3c48-9382-2fbd8460a2f2 | -10.3549 | -50.2099 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4f42615e-6905-3cef-83de-838fd8cc0252 | -7.4283 | -44.7639 | 2026-09-21 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| df5ed720-af97-36e3-8ec9-378fbda7f4f6 | -5.9335 | -59.9515 | 2026-09-21 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 1b2b8be7-cc9b-395d-817f-598cf04bdb60 | -12.0649 | -50.0185 | 2026-09-21 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 8121f4fe-202e-3ebc-8bd5-b5bc4afa940d | -11.7823 | -49.8152 | 2026-09-21 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| cebbe86b-684b-3a14-b8b6-aae66f39d244 | -10.7076 | -50.6851 | 2026-09-21 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 30a77158-738d-34a0-a5f4-c64118614868 | -3.3823 | -50.4486 | 2026-09-21 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 527b2383-9565-38e5-b9a5-a9ce54e32356 | -10.8282 | -50.1601 | 2026-09-21 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 428f0998-892c-3975-8dab-eaa6767d9b2b | -6.0033 | -44.7247 | 2026-09-21 13:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ad3e873d-c8df-340f-809e-50a1f3978def | -10.8002 | -50.8243 | 2026-09-21 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 7a0bbbc4-1eb4-3adf-89d2-d2d4696aa3d8 | -3.3 | -57.8681 | 2026-09-21 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| b397d7fc-f97d-3e59-99ae-dbbc430576a9 | -6.5759 | -45.5419 | 2026-09-21 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 1f8a6633-2e45-3ec5-88f9-c033e49d4624 | -8.7911 | -48.7502 | 2026-09-21 13:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 4ce85a01-71d0-3676-8076-eb2991a9ec6d | -12.4204 | -47.0228 | 2026-09-21 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 301.1 |
| 1f062fb6-daea-3c3b-b75a-d34d4de0f7da | -8.7537 | -44.2821 | 2026-09-21 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 7c14553a-9e5b-3f8e-a0e5-15c416d23d54 | -13.2794 | -51.7524 | 2026-09-21 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| cd842e6c-8256-3966-8205-625fd1d30f57 | -8.7729 | -44.2568 | 2026-09-21 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9a685022-3f77-3a32-9e98-e2a0d9e9c004 | -6.8571 | -45.5189 | 2026-09-21 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 0a892421-04dd-35e0-aba6-0ba9c3567193 | -10.3914 | -48.9133 | 2026-09-21 13:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ba848ccd-c05f-322f-9fe8-c802a6b74730 | -10.9544 | -50.6165 | 2026-09-21 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |


[Clique aqui para ver as próximas entradas](README121.md)
