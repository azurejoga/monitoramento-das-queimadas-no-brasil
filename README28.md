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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 691a5c12-c369-3670-b883-81ecb0a4a0a8 | -10.28341 | -47.61103 | 2025-06-19 12:27:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 11710345-fe62-3dc8-a595-2b8debb66c0e | -11.27833 | -52.45971 | 2025-06-19 12:27:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5a7c891d-829b-3ab3-8d30-38dd4825fd4d | -12.22569 | -44.23294 | 2025-06-19 12:27:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 3cdb2ad1-ccfe-37a8-a674-023d66cddafd | -9.22441 | -48.8614 | 2025-06-19 12:27:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 87caf307-2671-3127-90ed-13a712f0e65d | -10.84917 | -53.76639 | 2025-06-19 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8956715f-5828-30f1-896b-9359fde7b979 | -7.8668 | -50.6873 | 2025-06-19 12:27:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| bc310963-e81e-3cb6-8807-2241839069f8 | -12.22403 | -44.24585 | 2025-06-19 12:27:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 810852c4-e393-3518-91a1-4e2d14f8c680 | -11.18041 | -47.3933 | 2025-06-19 12:27:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 57a0a34e-8aee-3719-a7b6-826547b45fd9 | -9.87396 | -49.3363 | 2025-06-19 12:27:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 70844c94-cc44-3dee-bdfe-07120a3be595 | -13.97317 | -48.75827 | 2025-06-19 12:27:00 | TERRA_M-T | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 57e3ce20-30a2-3172-bc4d-e9211b0604eb | -8.64732 | -47.17854 | 2025-06-19 12:27:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| e82ea53e-c608-3083-a476-c10597d33f8e | -8.59572 | -51.54781 | 2025-06-19 12:27:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f92efc45-f823-3eb0-9a46-7cd96de19e4b | -8.62629 | -45.03888 | 2025-06-19 12:27:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e6f0bc2d-3b27-39c6-bd4a-88df14e83d24 | -9.00072 | -46.90797 | 2025-06-19 12:27:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b62739fe-8189-3a19-b615-d0393e7b2129 | -12.2395 | -44.20859 | 2025-06-19 12:27:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 45540ee1-8b0e-337b-b8fd-42271bdefeef | -13.96433 | -48.75697 | 2025-06-19 12:27:00 | TERRA_M-T | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 51d11b1b-2033-3a80-8036-38091af4dd87 | -10.52909 | -46.65683 | 2025-06-19 12:27:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6bf031c6-291b-36d0-95c1-71c6b8ec2225 | -8.95737 | -47.2745 | 2025-06-19 12:27:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 46a7d7e8-f1ee-3062-980a-b3c9e405b754 | -7.91141 | -47.5549 | 2025-06-19 12:27:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| adca51b0-641e-38ba-b60a-1a1b3cb4a23f | -11.47341 | -47.27799 | 2025-06-19 12:27:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| b238a093-caab-3b47-aa0c-6e004b8af759 | -10.0793 | -52.74314 | 2025-06-19 12:27:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5aac1301-5a1d-3ea1-83dc-9d0c68c9ba0c | -12.87057 | -44.29414 | 2025-06-19 12:27:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| c0179935-deb5-3ace-a59c-651cf596107d | -12.1732 | -43.20149 | 2025-06-19 12:27:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ad3d8b7a-7341-3542-b30b-87e2a99630d2 | -11.56655 | -47.33469 | 2025-06-19 12:27:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 363f870c-135d-3fc0-9405-0ec7d68dd5da | -7.86497 | -50.69914 | 2025-06-19 12:27:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3a656bef-baec-3ddf-92f9-77ba571fec4d | -11.46323 | -47.28581 | 2025-06-19 12:27:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 4de64aad-1c1a-36a6-9179-417d952b06da | -12.30621 | -50.03706 | 2025-06-19 12:27:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ab09af40-52b2-3685-96d4-abb41bc0eeec | -7.88941 | -47.13003 | 2025-06-19 12:27:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3f54ab38-c0df-3913-9e8b-7ae2162b3786 | -10.24325 | -50.56549 | 2025-06-19 12:27:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ca9cfbd5-f382-3b08-b395-60eddf907709 | -12.26972 | -44.60149 | 2025-06-19 12:27:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9d9fcb3c-ebff-374a-a9d3-520ed1f5d6c2 | -10.83696 | -54.01612 | 2025-06-19 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| b460c0bb-5efd-3c93-8c7b-d78c3a00533d | -9.82398 | -48.1118 | 2025-06-19 12:27:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 74bcde74-b833-3a84-b74f-1fb9c32a3849 | -11.92701 | -47.84954 | 2025-06-19 12:27:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 438e7c9a-cb40-3b04-9bfe-492c6a65b3cb | -7.88814 | -47.13888 | 2025-06-19 12:27:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 544a3054-210a-3146-ba5d-7c779a06a85e | -9.37545 | -47.63683 | 2025-06-19 12:27:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 51e0d778-3d6f-3b89-afca-dc2a9b627fb8 | -7.87114 | -47.89481 | 2025-06-19 12:27:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 8b9997ba-6945-3731-9bcb-6731f40c94b6 | -11.46658 | -47.90775 | 2025-06-19 12:27:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 80626622-a8d0-3cca-b588-db4cd8fb737e | -8.12869 | -49.58031 | 2025-06-19 12:27:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eeb3c6de-1673-3ad9-80fb-8e57d0100d28 | -10.65109 | -44.49532 | 2025-06-19 12:27:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b0b1c1a8-35f0-3184-af56-18c2c06d80db | -11.27602 | -52.47392 | 2025-06-19 12:27:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e55065c7-d844-3e54-9f86-d059da26c114 | -8.21647 | -47.60812 | 2025-06-19 12:27:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 66586c90-b5c1-3bc2-98cb-b8575428b917 | -11.80312 | -43.78142 | 2025-06-19 12:27:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d335d94a-e402-385e-a655-fafd6f90807e | -11.2745 | -52.46684 | 2025-06-19 12:27:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| e984ed61-8c9e-36c2-b29f-78292d8d67c5 | -11.57224 | -47.4338 | 2025-06-19 12:27:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 144baea8-cc73-3fbd-a54a-f648d4ca3628 | -11.17026 | -47.40105 | 2025-06-19 12:27:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 10f8f0d2-a2f2-39bd-8451-5bbfa05aa981 | -12.88108 | -44.2956 | 2025-06-19 12:27:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 053616f2-d3dd-3776-941f-f92c1215e00d | -8.12112 | -46.08808 | 2025-06-19 12:27:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d8eb36bb-fd43-3ce6-9b4f-c26a04e6cee1 | -9.32948 | -47.83001 | 2025-06-19 12:27:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6d33704b-4a2d-3ea6-8554-83efc818fd9c | -11.14026 | -53.93338 | 2025-06-19 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 3c912fb6-0a2d-33cd-b8fc-52f18857a59e | -10.65267 | -44.48354 | 2025-06-19 12:27:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d468a54d-1e17-3c64-9f3d-4858787a9836 | -10.86133 | -53.76854 | 2025-06-19 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 8d2dadf6-827c-3330-a9a5-2dca6fdfdf01 | -9.12454 | -47.58253 | 2025-06-19 12:27:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5746ebdd-8ef5-3a17-bd7d-e7072d0a0d77 | -9.79239 | -47.17589 | 2025-06-19 12:27:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 697894d7-e2be-31ba-9359-1cc38c2f7419 | -9.50021 | -45.44693 | 2025-06-19 12:27:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a6e3ff42-8757-3eb9-be39-48e0da064b5b | -10.15707 | -48.98203 | 2025-06-19 12:27:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c36f453b-f4af-3a90-9c42-3bca3bbf5588 | -10.48137 | -48.66261 | 2025-06-19 12:27:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 84ea4f7a-973b-3e60-8190-d514210b576e | -8.01349 | -46.78238 | 2025-06-19 12:27:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 1dc61be3-20d4-3a1c-8b54-b708d1dd1a51 | -8.72578 | -47.98838 | 2025-06-19 12:27:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b03a2bfe-c7c0-3335-8b41-4e9ed0acc6e2 | -8.36638 | -47.66013 | 2025-06-19 12:27:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7550eab7-9d83-307d-a118-32a797a98d3f | -7.61357 | -49.93243 | 2025-06-19 12:27:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bda8bcb3-abf1-33bc-a125-91a351eaacdf | -9.63464 | -46.07284 | 2025-06-19 12:27:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a96de794-1ec3-3f7c-8a9f-4ceeeb820dac | -11.46452 | -47.27673 | 2025-06-19 12:27:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1e6b40bb-6f1b-3ff2-ac64-43cb9085bc4b | -8.82361 | -45.47342 | 2025-06-19 12:27:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8053382b-4c96-3f4a-bde8-85835697338a | -15.73781 | -42.29654 | 2025-06-19 12:27:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| eb5958bc-48ae-31e3-b237-371abf50fa6b | -8.67777 | -51.29403 | 2025-06-19 12:27:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ed756db2-bb02-39a0-8100-6877c252cc89 | -8.53155 | -47.66899 | 2025-06-19 12:27:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c584f350-ef8f-3ef3-a3fe-9eb41404867a | -11.17155 | -47.39203 | 2025-06-19 12:27:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 66ac38f1-fd6b-3708-be39-543c372b45c3 | -7.75493 | -47.61076 | 2025-06-19 12:27:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 84d11c5d-99d2-3c88-9151-b47224c8229e | -11.1614 | -47.39977 | 2025-06-19 12:27:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 034678c8-bcb6-3819-8736-c2da09c5eaac | -11.47212 | -47.28707 | 2025-06-19 12:27:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 2e2285ab-b4df-3b9a-a189-d23dd2a82ce8 | -9.71981 | -51.95692 | 2025-06-19 12:27:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 35bbff20-4f9d-34a0-a0b6-47aec2775437 | -8.94854 | -47.27325 | 2025-06-19 12:27:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0b543fd0-4ac1-3d53-a77d-9ae2b8c3fc19 | -17.05404 | -47.40871 | 2025-06-19 12:29:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 83fcd359-2f90-3763-82a1-ba4e218364d8 | -16.32184 | -53.80202 | 2025-06-19 12:29:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 266.1 |
| e7a3dfdd-e232-3a3a-91e8-5a465205d4ad | -17.71008 | -46.30925 | 2025-06-19 12:29:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b30d72d6-bd50-368d-aeb6-eeba9a87297e | -18.99865 | -52.08444 | 2025-06-19 12:29:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ab8593a2-3eb5-3122-ae3a-11facf54430a | -17.71152 | -46.29774 | 2025-06-19 12:29:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 389022bb-5ab3-3f95-8c02-ba520a33f677 | -16.60177 | -49.07261 | 2025-06-19 12:29:00 | TERRA_M-T | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 47d5270e-a9bf-339f-b344-37120162fd13 | -19.12289 | -52.70932 | 2025-06-19 12:29:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| de2bf4c3-767d-3f79-8cc4-253a8bf8f321 | -18.99451 | -52.07767 | 2025-06-19 12:29:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 11db7ada-371a-3cdd-b422-c4fb51629ff8 | -13.98605 | -58.10694 | 2025-06-19 12:29:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 5aa87861-34b1-3a25-8da3-df8382096510 | -15.96952 | -52.84496 | 2025-06-19 12:29:00 | TERRA_M-T | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 311d42cb-7c70-3298-b501-377aed025d66 | -19.13449 | -52.69946 | 2025-06-19 12:29:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1e67046e-9826-314a-a898-fe233781bcff | -19.87222 | -44.96084 | 2025-06-19 12:29:00 | TERRA_M-T | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5647c09d-4de9-3247-96d4-565f1d0a7200 | -17.04483 | -47.40747 | 2025-06-19 12:29:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| db3a8ee9-534c-3cf5-8888-4bffc11b2d91 | -16.25317 | -51.82951 | 2025-06-19 12:29:00 | TERRA_M-T | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 87047d67-b32f-3438-acf5-01474b6c69bb | -19.12475 | -52.69774 | 2025-06-19 12:29:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e785cc8a-f0f0-3497-9f25-a2778dd0fc8e | -15.11592 | -54.65447 | 2025-06-19 12:29:00 | TERRA_M-T | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f4e422f1-8e2f-316a-a198-8321233e61cd | -18.7837 | -51.99612 | 2025-06-19 12:29:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cbd728c4-d334-394b-8b80-df2a858df4b8 | -17.57483 | -47.49981 | 2025-06-19 12:29:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d4376f09-9313-3e79-a4cb-3211e7afb4f3 | -17.58404 | -47.5011 | 2025-06-19 12:29:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ea926713-20f3-3b04-bc46-a33d24bb4b8c | -17.57618 | -47.48972 | 2025-06-19 12:29:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fdfc0953-6ed2-3517-9bbf-51c3da356a06 | -16.25488 | -51.81843 | 2025-06-19 12:29:00 | TERRA_M-T | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 5916b1a2-acd1-3eb8-a0cc-a0d50f5a7220 | -16.29211 | -52.93807 | 2025-06-19 12:29:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| df82270f-56f9-3aa2-aed8-4ce192a73b77 | -16.31935 | -53.81668 | 2025-06-19 12:29:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 36f21426-67d0-3252-a00e-2bcb460a13fd | -18.99284 | -52.08844 | 2025-06-19 12:29:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3e6b7a57-2a25-3298-b894-a1d590917377 | -16.32095 | -53.79586 | 2025-06-19 12:29:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 9d157c79-96c5-3654-bb24-3ac1a631020d | -19.8611 | -44.9594 | 2025-06-19 12:29:00 | TERRA_M-T | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5b246fa1-4aa2-364a-8dbb-8cbbe9d3c190 | -16.31078 | -53.80034 | 2025-06-19 12:29:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 8188d445-1d3b-3c16-801d-03f64df6ccaf | -21.09514 | -48.67706 | 2025-06-19 12:29:00 | TERRA_M-T | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |


[Clique aqui para ver as próximas entradas](README29.md)
