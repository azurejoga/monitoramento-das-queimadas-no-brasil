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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 802ddcd9-4be0-3415-9931-6b5f0118fccd | -7.08523 | -49.60255 | 2025-06-27 04:46:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ed14830-3852-32fc-927e-6d67ade41ef7 | -6.27376 | -43.6751 | 2025-06-27 04:46:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4eabad96-7b1a-325f-83df-b38cb261cc54 | -7.54018 | -45.82755 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 461eb0aa-eeba-38a9-82bb-913d00a14767 | -6.27299 | -43.68058 | 2025-06-27 04:46:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| cb830a9d-9af6-3e1b-b798-9cd50861b10c | -7.20632 | -43.07965 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8cf19eb8-f174-3574-9768-efb4f2daffcb | -5.03133 | -49.59171 | 2025-06-27 04:46:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a065990f-86f7-397d-9543-b84e515b96fe | -6.95264 | -42.89012 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 076a1651-eaa5-3bfa-a7ae-0732e9ba6543 | -7.54795 | -45.83264 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02038057-4eca-33ba-bf27-f09b5187f0b7 | -5.85462 | -43.64523 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc96e6b8-fff1-3179-ba84-1f6cfa73e99b | -7.21552 | -43.08685 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a9ab14d5-0c22-30b7-88c1-1216da93420c | -5.92344 | -43.4692 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a455452-6ec8-3e94-8b47-fbe4d40fbdd6 | -6.96194 | -42.89741 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 3ccb9166-d3ab-349b-b8d8-2584fafa01dc | -6.97248 | -42.89585 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 6ece8a7b-713f-39b3-9b3d-5b837af05688 | -5.92198 | -43.47937 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a0da1848-8c50-3571-8ce8-fec6085c46fe | -6.97165 | -42.90178 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 6e98c761-425d-3369-8954-64bc21b15130 | -2.43937 | -47.46532 | 2025-06-27 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42945cc5-3e63-39a6-81c8-4f4dcc710c51 | -6.1721 | -48.08709 | 2025-06-27 04:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6941d5f5-348d-3417-8022-f2d2c86dc75c | -4.81708 | -47.3213 | 2025-06-27 04:46:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30943d94-d188-3c7f-a9d4-1a0688bc16f2 | -7.01755 | -49.18302 | 2025-06-27 04:46:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be747dc7-857a-3cbe-b738-210386764d3c | -5.85532 | -43.64029 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6321b3ec-824f-3f6c-ba46-5571979f9518 | -5.92271 | -43.4743 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 115ba7e7-ce33-3b8c-b143-707b5498ac87 | -2.91958 | -48.06602 | 2025-06-27 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c666e4d4-5334-32ca-8dda-662438344cb7 | -5.17664 | -46.10541 | 2025-06-27 04:46:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48fb5cc7-c441-3cda-8fc1-be22999b5a4a | -6.72289 | -47.21003 | 2025-06-27 04:46:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 584f67a1-bba7-389b-863c-e37da14a7f91 | -7.21491 | -43.08928 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 167a0266-c812-3c40-b4bf-bfff1f501f1e | -6.95811 | -42.88788 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 23c85bf5-e2de-3513-88fd-64d742572692 | -7.21992 | -43.09005 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c05e7526-dced-30a1-b2e5-6dc4d68adcba | -6.1655 | -47.27413 | 2025-06-27 04:46:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83b0b71d-a985-33ec-abbc-e51613fde8fa | -6.22062 | -43.35811 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d565751d-4134-309a-91af-d2ee0d4d7f25 | -6.97207 | -42.89882 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 66ba29e0-7161-365c-a8ba-fb330303819b | -3.03294 | -49.43079 | 2025-06-27 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba315e34-b6e6-3622-8f25-d0b98decf6a8 | -7.70772 | -47.84116 | 2025-06-27 04:46:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61136d34-45f9-34cc-a14d-b17380eb75ab | -6.96659 | -42.90107 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 891eca09-8a39-31aa-bd02-0b6ee2d9896d | -6.57278 | -54.99729 | 2025-06-27 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4711ee09-5395-3904-a47f-d7dba6d2b1ea | -6.69023 | -43.05858 | 2025-06-27 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7f4cee8-d820-31cf-9c21-438b9d2814b0 | -7.21051 | -43.08612 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9dfa1e10-ffef-3937-aac9-c4f787d4e260 | -5.85362 | -43.64311 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 35e0eb14-b59e-3186-9ff9-91a7f9c704d0 | -6.21986 | -43.36353 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f7bd90f-a636-316d-a0c5-3706457d8101 | -7.55211 | -45.8333 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a890cc8d-9389-3d84-8734-7f61e1d032dc | -7.01468 | -49.17873 | 2025-06-27 04:46:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c1d0d6f-a7d8-3880-bb36-49faaf8a1151 | -7.54851 | -45.82885 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2fd36af0-af6d-3e00-8ffe-fc77ce47bbfe | -7.70927 | -47.84347 | 2025-06-27 04:46:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dee6ce5d-f085-325b-a4d1-79c4f4668263 | -3.00025 | -48.02782 | 2025-06-27 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31c3b794-49be-34d3-87d1-8b06624adc91 | -6.21579 | -43.35727 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c98b634e-0874-3be4-b92e-3aa065789d7f | -6.96153 | -42.90034 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 1a387075-8500-3231-817a-be4ab8829625 | -6.57569 | -55.00001 | 2025-06-27 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bef224a8-4fe8-3460-bfb1-e32ee4d1387c | -7.22052 | -43.0876 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1246f21b-8ebd-31ad-ab4e-c3cbb355554a | -7.21148 | -43.07692 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0bb24024-ddc2-33c2-9165-8e881b2abf51 | -6.65802 | -47.58381 | 2025-06-27 04:46:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d249e57f-a784-3a59-ab20-f84132abb5c2 | -7.20646 | -43.07623 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| dd1e51f6-0d2a-3c77-bbc2-b7550886155e | -3.03184 | -49.43779 | 2025-06-27 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 623a63df-e1e0-3e93-89f2-178040fb124c | -6.21743 | -43.36044 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 387d86b0-011d-3e55-bacd-2d2fa1b74993 | -4.3433 | -55.77757 | 2025-06-27 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 550e3c3d-b8f0-39d1-ade1-ee2da1f67476 | -8.0442 | -45.66851 | 2025-06-27 04:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90ac9e1a-bc87-3bbb-806b-2e2a81464955 | -3.16868 | -52.449 | 2025-06-27 04:46:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf3efadc-e7a7-36f1-98be-4ad005708540 | -6.9577 | -42.89082 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| e154a132-0e8b-30e7-8afc-718f7d7d6439 | -11.18711 | -55.9142 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b75238f0-8fdf-322f-b604-3fc10a3f7dfe | -11.99885 | -47.16553 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b5efce0-3552-3105-873f-96c17b2b05a5 | -9.34611 | -58.85291 | 2025-06-27 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f24219c8-4f15-3cd3-b6ea-59b08c65dfd4 | -8.49066 | -48.26033 | 2025-06-27 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d45d6a0-1cdd-324a-a3fa-70f76a9c5ccb | -14.29521 | -41.60266 | 2025-06-27 04:49:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| cec9aac8-f8c0-362f-9740-e11f957509db | -11.99601 | -47.15843 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c176c10-0dd5-33b8-9f2e-02873d001607 | -11.18017 | -55.92929 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0fb188b-f325-3d7f-a14d-d48b96512227 | -11.0634 | -55.37492 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 316015b7-9aa5-3d84-b7ee-680a1919edc5 | -12.02602 | -57.08878 | 2025-06-27 04:49:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08ab6154-74a9-3aae-a625-83ad387f8ab3 | -9.24702 | -48.75215 | 2025-06-27 04:49:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e8b7902-a8fc-3d05-9d68-86ae99548e2b | -8.06226 | -46.9629 | 2025-06-27 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30f7bbf1-3ee9-3ac7-8598-fac4b4cddaff | -9.50121 | -56.09476 | 2025-06-27 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbac58e1-89f6-3cb6-92ed-c2b2272b6626 | -10.80878 | -57.75947 | 2025-06-27 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2438e97-c9a6-3a10-9fa3-a4e9744942b0 | -8.3746 | -51.07021 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a9f25c6-6f74-3ddf-8842-5071c346ea73 | -10.83314 | -53.74816 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1303b843-8fb2-3745-b465-348819b014ec | -11.57726 | -52.10908 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 64ddcbe7-4382-3385-95f5-2fa5f85dd089 | -8.61803 | -51.56675 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4ba88f2-0a8d-3b04-ae1e-8f3925907383 | -12.42652 | -43.72193 | 2025-06-27 04:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27f9c370-f860-37b9-bb79-a0b0fa67a708 | -11.05906 | -55.37856 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8a8d5d8b-18c5-3709-981b-82a23b09bd52 | -10.82694 | -53.7433 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44fe8b69-5a7c-3667-bc65-9517f4791c1a | -11.77591 | -55.03196 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea1afe74-2bfa-3d70-9cd9-85846f32c2d9 | -11.0761 | -55.07512 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a0ab9e8-8b85-301a-8f11-2a0ca748952c | -8.73484 | -50.2591 | 2025-06-27 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 576d0bba-5b6c-3dc3-88da-ff5dd4432619 | -11.74956 | -54.23364 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35336755-f5f0-3975-abd6-f185a85c455a | -10.83594 | -53.75243 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cd62fed-cf21-3bc5-92d4-37d601d8e5ab | -11.75767 | -54.22725 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b19f6d5-3365-3744-955a-856fcae52560 | -8.8427 | -49.85614 | 2025-06-27 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e97f975-75f3-39dc-b70c-49424be8273d | -10.64851 | -44.4907 | 2025-06-27 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 10726ba0-5409-38b3-bf76-a71cb3801da0 | -11.82272 | -47.53515 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9933c2d8-ed6b-359d-8188-47c9dda74d90 | -12.28327 | -57.26373 | 2025-06-27 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27c5318a-2ce3-34bd-8e78-6159a1f7c182 | -11.44469 | -54.46614 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 29006167-abbe-32e6-a8e7-93eb3f128bac | -11.77099 | -55.03946 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8063673f-d834-3456-9643-7ccaf93e54e6 | -10.86203 | -54.03753 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24d10c65-94f1-3b29-8e49-2aa462135770 | -11.36107 | -48.71312 | 2025-06-27 04:49:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 87a62115-54b6-3624-b8e5-85063497fc82 | -12.4313 | -43.7257 | 2025-06-27 04:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49c486e5-b92c-39fd-93b0-c9e58572ce28 | -10.65313 | -44.49259 | 2025-06-27 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4714f0cf-2844-31c2-b628-c29575751f57 | -13.10332 | -52.29398 | 2025-06-27 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 969d5ed8-7af1-3cd7-9cb7-108380259d56 | -9.23823 | -50.02914 | 2025-06-27 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ebe3877-27b7-35ac-8369-56d617ae0376 | -9.06783 | -49.43473 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3b1508ac-6ba1-356a-a367-36a955121ed7 | -11.18615 | -55.91647 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a19e4ad8-7374-3883-9293-f68827829719 | -14.20537 | -45.5083 | 2025-06-27 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2068f966-7e60-37f6-af78-7093c1d095bd | -9.0719 | -49.43141 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bc02c266-de7a-3ccb-a1e5-145e31bb1df2 | -11.80439 | -57.3558 | 2025-06-27 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 860208d8-8497-3ff3-8cef-ec7821efc39e | -11.44405 | -54.46999 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README19.md)
