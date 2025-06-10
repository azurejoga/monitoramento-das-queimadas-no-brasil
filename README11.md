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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd91590c-28d0-37d7-8594-face73973cd8 | -5.2108 | -43.3067 | 2025-06-10 05:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| bd67e698-f399-343c-ae83-f75d53e603af | -5.20418 | -43.30779 | 2025-06-10 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df1e88f7-b405-39e9-ae56-eab9cf9077da | -5.21722 | -43.31019 | 2025-06-10 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c0a65a1-53dd-376a-8310-66bbc3ee71d7 | -5.20991 | -43.31448 | 2025-06-10 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e2608f1-fe8f-3556-bb5b-84756348bd7b | -5.21507 | -43.31221 | 2025-06-10 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ea34fae2-f146-3c0f-9bfd-09d8293fe9f1 | -4.24787 | -47.58267 | 2025-06-10 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 777fac79-4adf-3295-9d5f-b1f80724012d | -5.2107 | -43.30898 | 2025-06-10 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e2fa005-50de-359f-a624-d82f4f31616f | -5.64381 | -43.60047 | 2025-06-10 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1347b2bf-4b87-35f2-a1c6-2f47a8b444c3 | -5.21643 | -43.31569 | 2025-06-10 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa0bf2f1-717f-3559-baf7-50c40dd53d96 | -5.64955 | -43.60672 | 2025-06-10 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 683f0e4d-ae97-38d5-8cf6-debcb42f57b4 | -4.81663 | -47.32134 | 2025-06-10 05:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a96d815-5538-350c-ba51-b19f4057b209 | -4.24524 | -47.58348 | 2025-06-10 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a2102a71-e957-313c-ae11-6bb7ec09f5e2 | -5.65029 | -43.60139 | 2025-06-10 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 944af32a-05dc-3832-801f-e006ea013f45 | -4.8212 | -44.35447 | 2025-06-10 05:04:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72be4054-6f58-35d7-acfb-cb0508703c9a | -5.20855 | -43.31097 | 2025-06-10 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac4c2c11-7e4a-3418-9e0e-1e05be9af72c | -5.20338 | -43.31333 | 2025-06-10 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 19e71fd5-da97-31f9-9c35-24b9919dca6f | -9.4121 | -48.43605 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c2f68ca-d23d-3e8f-a65b-48dbb2651fce | -5.81708 | -46.48625 | 2025-06-10 05:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f52b4d01-b11e-3cfe-b81f-4a8449449f41 | -8.96237 | -47.9699 | 2025-06-10 05:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1607f3ae-03e8-341f-b0ad-b2d105a50f96 | -10.2145 | -46.92932 | 2025-06-10 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04d6d430-0524-3e8d-91a2-11376bc659f0 | -5.77287 | -43.62523 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1113bc53-eab7-3315-aa37-9fa41e0e436e | -5.91625 | -45.5216 | 2025-06-10 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56f85991-5699-31b1-9e8e-4911a727c7a9 | -10.21219 | -46.93121 | 2025-06-10 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46d37fd8-5ab6-3e4e-b085-782e544fec59 | -9.39219 | -48.43312 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60f4dd85-51dc-36bc-88b9-9e2141a1dce6 | -10.651 | -44.4858 | 2025-06-10 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca730a2a-8764-3616-be9d-b8b4e33873f9 | -8.60677 | -46.5648 | 2025-06-10 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e354701-0882-3537-83ae-63437a8283e7 | -10.21401 | -46.93305 | 2025-06-10 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 070d6570-25b2-3e2c-a41f-2f33d10e0e61 | -6.20159 | -43.33462 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a5923c7e-74b2-3eec-9dcb-cf8a80db8def | -8.07974 | -47.12253 | 2025-06-10 05:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6259c2c1-aad9-33a1-b892-3fc002f56325 | -9.00745 | -49.57338 | 2025-06-10 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b993a7c-3d46-3ff9-a525-cc9d83cccf90 | -7.01434 | -44.62174 | 2025-06-10 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8609186a-72d6-37ea-a8bd-2cb3c0353a36 | -10.20848 | -46.93195 | 2025-06-10 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b27cb35-3503-34d8-8db4-263719391496 | -10.04739 | -48.66282 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81f484a5-49a8-3fed-ba42-ee38fc641f9d | -9.37949 | -48.4139 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff0f452e-901b-3cbf-8852-3d5d6387cd00 | -9.20985 | -48.86351 | 2025-06-10 05:06:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96cedefd-2f70-331c-b2f1-c0b33bb48854 | -10.05729 | -48.66422 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 912bc0bc-052c-38a7-851e-0310bdb26e44 | -7.02032 | -44.57832 | 2025-06-10 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6995e41-579d-376e-96a7-7a3df803df28 | -6.49162 | -42.84961 | 2025-06-10 05:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 03d7652a-98ab-35eb-852c-8bb741ce36b3 | -6.19497 | -43.33356 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df65d2dd-8cb4-372c-a632-3608a6ccb444 | -6.19575 | -43.32784 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6bbe116c-b78b-3952-914c-2d5d43188f58 | -9.01101 | -49.57692 | 2025-06-10 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c79dc5ae-a37b-381d-85b8-c35441806aba | -10.52516 | -47.82359 | 2025-06-10 05:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 688d3e8e-c585-3b62-8d66-178940193aef | -6.86367 | -47.85536 | 2025-06-10 05:06:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfef0812-e906-3f62-9ff8-929880042fc9 | -9.01496 | -49.58224 | 2025-06-10 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0930c1ec-e6d1-38c5-9204-9fddad4b8c09 | -9.00643 | -49.57627 | 2025-06-10 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 96e509e6-eb3d-3b77-aa3f-c3a9ae29e81b | -7.01966 | -44.5831 | 2025-06-10 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffc4c580-d293-3db6-bf6c-d8f91d4e5f1e | -10.05234 | -48.66353 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4bd8a00e-223d-34bd-a662-59ed064b548f | -9.39243 | -48.43248 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5e20fd9-2880-3a36-b94f-d693c11d6672 | -5.78084 | -43.61564 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 283bba72-8dfe-3c2d-9764-e44467892beb | -9.01594 | -49.57931 | 2025-06-10 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4d9076c-2f40-3a02-a3fb-dd14bab85aa7 | -10.22378 | -46.92922 | 2025-06-10 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaa8609d-ca91-336a-b933-e232fab14f4a | -10.2402 | -52.21888 | 2025-06-10 05:06:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36c87193-feb9-3f20-9983-85ee177ab204 | -8.33777 | -48.45052 | 2025-06-10 05:06:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 847810d4-e10f-3dcf-8b4a-3f8dd6f6c308 | -9.70778 | -57.8754 | 2025-06-10 05:06:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 071e0293-3bee-3f44-b03e-53d599396db2 | -5.78002 | -43.61582 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5a06872-9752-3929-a61d-08e3cf2506e8 | -10.27209 | -47.60653 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f3497c0-c206-3d4e-84ef-cd54b4980fb9 | -7.73648 | -44.17442 | 2025-06-10 05:06:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20e0616e-a7e1-37f0-a04b-9b5b9e9e639d | -10.21822 | -46.92835 | 2025-06-10 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76c837ba-43df-39e0-8413-f563b558b864 | -6.21637 | -43.3255 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1877cd36-13de-3318-b415-f129c93efcab | -7.46824 | -45.50605 | 2025-06-10 05:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82d22f61-9dcf-395d-a6c6-bd708f11d643 | -9.65939 | -56.10503 | 2025-06-10 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2a10b84-fe34-3ec2-afec-e52427ffbaca | -7.4747 | -45.50264 | 2025-06-10 05:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce489b08-7feb-30a7-83cc-5c45fef6d0a7 | -5.78076 | -43.6103 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 822643d0-4c1d-3020-bf1b-07b5b676de92 | -10.21775 | -46.93212 | 2025-06-10 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fa9630b-8041-3a23-aa61-c5a3d5c6a485 | -9.21363 | -48.86519 | 2025-06-10 05:06:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06cfec40-3eee-37f0-9728-8f02f8a08496 | -10.21174 | -46.93487 | 2025-06-10 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc984add-61d6-3b70-8b6d-1bc5a525ed3b | -9.00376 | -49.19522 | 2025-06-10 05:06:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9e21376-fa63-3d90-93f5-4eee89880065 | -5.81872 | -46.48584 | 2025-06-10 05:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 905a0e18-aeb5-3f4b-8fa7-4f46416e74e3 | -9.70719 | -57.87902 | 2025-06-10 05:06:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b298ca3-9616-33f7-8e70-42d34932518c | -7.01297 | -44.62292 | 2025-06-10 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a400e75-a405-3e95-b74e-75132bb55de9 | -5.81827 | -46.48912 | 2025-06-10 05:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3705daed-09d6-312e-a9b8-01c13cf7f9c5 | -5.91568 | -45.52561 | 2025-06-10 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fb9a8f6-e3a8-3d62-a733-0968619a96dd | -8.0802 | -47.11906 | 2025-06-10 05:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 621c618a-61d9-3cf4-9be2-0a2c8aafee23 | -10.52032 | -47.81936 | 2025-06-10 05:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 498a6e25-a654-337e-a4f6-a2acd99eb911 | -9.20882 | -48.86441 | 2025-06-10 05:06:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d0fcf22-dc3e-3973-9155-a24301ad730c | -5.77861 | -43.62633 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70c799af-38af-317d-b235-e7ad504725e7 | -5.7858 | -43.62207 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fae1d69e-27ec-3718-9f18-d7015f0eef06 | -10.13186 | -51.65982 | 2025-06-10 05:06:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d684e76-3036-34b1-97ff-93ec4c762a97 | -10.23964 | -52.22206 | 2025-06-10 05:06:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61499338-a43f-32f8-8bdd-9e855c79432b | -10.0516 | -48.66903 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 87f0de75-6498-32d7-a22e-80e156916f6d | -5.77936 | -43.62613 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fdf8b37-da78-39ed-ab9a-7e5082aad254 | -6.21559 | -43.3312 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37f6c184-418f-3da3-b577-1263fb88b5b6 | -8.60938 | -46.58802 | 2025-06-10 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7d78875-ce22-3288-8ea9-e150ca4beb05 | -7.00823 | -44.62029 | 2025-06-10 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37631592-53d2-386c-9fac-574644aee8d2 | -7.47413 | -45.5069 | 2025-06-10 05:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10528e6b-f58a-3910-a253-48151f48240f | -9.86289 | -47.88829 | 2025-06-10 05:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de0ca6d5-ba40-35f8-9cf5-2b1b23642ddb | -10.05657 | -48.66956 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 93c320dc-608f-3182-99c5-fbfa4c0a7a44 | -9.02705 | -51.14025 | 2025-06-10 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b30977e-1991-312f-9211-9b21f05c1b28 | -8.60988 | -46.58423 | 2025-06-10 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 660327a5-952c-30d7-a838-d9d5a7965cad | -6.20762 | -44.5099 | 2025-06-10 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8299a4b6-8000-309e-b3ba-fab57f8b4155 | -8.60627 | -46.56855 | 2025-06-10 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ec1716d-9fce-3193-ba40-7666e3d432a9 | -6.20823 | -44.50538 | 2025-06-10 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19727984-743d-3a46-8eea-63f652e2c0d8 | -5.77213 | -43.62541 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e606f41b-e072-3580-bf48-022971be3d38 | -9.86331 | -47.88517 | 2025-06-10 05:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc83580f-7234-3554-93ee-2f1e5ddaf9a1 | -10.21353 | -46.93671 | 2025-06-10 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddc5da8c-9d17-31a8-946c-b79801d990fe | -10.22006 | -46.93019 | 2025-06-10 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b51e0014-6d79-3e24-9725-4cf188817288 | -6.20234 | -43.32911 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 53dfbb43-aa65-30c3-9e85-12d86e92d889 | -9.21466 | -48.86426 | 2025-06-10 05:06:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e2468fd-3399-30d5-b9b7-5f85cc9fc93b | -10.27744 | -47.60716 | 2025-06-10 05:06:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caf195af-13e3-32d7-bc22-f7ffc13a8f1a | -7.0136 | -44.6181 | 2025-06-10 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README12.md)
