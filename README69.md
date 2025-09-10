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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e579b3a4-fe28-3320-b3ee-17aa9082be8c | -11.664 | -46.90792 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d73b3530-8c2c-3824-af0d-f1b12fcdcb66 | -8.67528 | -45.7495 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f3ef3ba-0e0d-33b2-8e2e-ce46a6295963 | -7.13663 | -44.50538 | 2025-09-10 04:42:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87b404d2-1153-3e7b-b2fa-23ae67f43a3a | -8.41971 | -47.37931 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26c71e16-30db-375f-a728-5a8d42e816d6 | -6.68276 | -44.55086 | 2025-09-10 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c47a277-f4da-3450-a48a-5210e6a3646d | -9.694 | -46.82658 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71695d3c-1fa1-3c0a-b583-526f8470c802 | -9.31395 | -46.73244 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9a4535d3-cb83-3d4c-b87a-8395a0e35a0e | -8.04689 | -48.66822 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b92143dd-03da-3710-ae83-b0c331c21572 | -11.44021 | -49.2651 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffac0fb3-9f7e-37ae-8c78-ff24f9163f17 | -9.35418 | -46.5007 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7edb04b-8a58-3520-9597-f5a2db14828a | -10.19422 | -46.80825 | 2025-09-10 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb187478-e479-3754-a729-60b496f3b131 | -9.5566 | -48.28899 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 562b1fe6-ecd7-3ef0-a876-a27c9b827c87 | -10.01255 | -51.6918 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b29b5152-a1fa-31cc-a944-9afaf028778d | -6.21459 | -45.62377 | 2025-09-10 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49e617e8-e3f6-3657-a21e-905e19eefc75 | -6.7903 | -43.42052 | 2025-09-10 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8d889192-d911-3363-9176-abc264f1412c | -8.52137 | -45.71943 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 183ca562-4b5d-3b76-854b-1735eb904f7c | -11.43715 | -43.63449 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1beaa3e-3b5f-3843-8088-268dfbeec564 | -7.89158 | -46.26202 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c0f158af-235f-36c5-8ce3-7371308666ac | -6.79093 | -43.44598 | 2025-09-10 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d8f3f2e3-eb6d-316f-87a6-e8be92cec4bb | -7.189 | -44.93343 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 6b3e851f-ef06-36a8-ba7a-f854d1163a5b | -7.24559 | -44.46976 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ed1ae55-0d46-376a-bf10-83d0313e105b | -9.80832 | -47.76781 | 2025-09-10 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 241a608c-412e-3429-8767-ec1f80de9cc2 | -6.85622 | -47.93558 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 95245748-e316-37f2-b892-adcc9fff2b9b | -8.75439 | -47.09241 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfee4e97-3b28-334f-976a-b7f041182ac8 | -11.10933 | -48.45498 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e32d3b2-b3b2-363d-be31-8e1320ddb5e6 | -8.06468 | -48.63026 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6145e630-a4b8-3abd-949f-b5f84563e021 | -9.52853 | -48.26568 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54ed7951-9ea4-3ae3-bf67-1db27f4f9803 | -8.74961 | -47.10002 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a4b5cab-7d7d-3785-b653-2a59cfab95fa | -8.05307 | -48.68322 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 07a75dbd-fa76-3178-8192-973823b3e0f2 | -6.84714 | -47.92675 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdf90e53-692f-399a-8f56-d723fa045460 | -9.7578 | -45.40539 | 2025-09-10 04:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| de6db27a-2a79-37b7-8f3b-3fae30c82159 | -9.08289 | -50.46162 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af90d785-2d40-3600-99ca-fafd5eda51ad | -9.69253 | -46.76069 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6771d2bb-bfe8-3116-a171-4314a36d5758 | -9.06631 | -49.83851 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dad525d-50bc-3066-80cc-b7e2bdd8023f | -9.31589 | -46.71959 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 204dd1a8-fd93-30b6-bf7b-3cec274d517c | -8.02833 | -48.63253 | 2025-09-10 04:42:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 504a28dd-662f-3b11-9135-2d6c19c450fb | -7.54774 | -44.66336 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19532aa7-0d06-37e7-afe4-2f204d245ccf | -8.2618 | -49.92492 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 042db738-3264-3d99-8feb-235ce2e964b8 | -8.52532 | -51.38438 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ed60046-05e3-30c4-a3c0-6667480b9545 | -5.79886 | -51.67704 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0707d6a7-dae1-32c4-a677-1332baeef4bc | -9.05375 | -50.47847 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 938a922f-b700-33a2-a2cd-7cb81effe7c6 | -11.45347 | -43.61757 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0fcbe312-9523-343d-a26d-465efaddde98 | -6.79146 | -43.44827 | 2025-09-10 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5c766623-f5d5-319b-9bf7-4a7ab97e19c6 | -11.10663 | -48.45848 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 399e7769-18a5-3530-8844-e7fc5e885287 | -11.34423 | -46.54123 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1db5e828-27f2-318b-b8ab-b1b11d70a457 | -9.51735 | -54.64446 | 2025-09-10 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d482d2e-da32-3dfe-a024-c0368b30b3f0 | -11.44174 | -43.63514 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fea28bca-2c27-3655-bd53-3951cc16d71a | -10.58018 | -52.04561 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c65af25-e792-3de8-931b-a0686bd7991e | -12.41442 | -44.7221 | 2025-09-10 04:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4795c9ff-f83a-3319-a1cf-ae5db177105f | -11.43766 | -43.59607 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a497635e-afc8-37ac-a083-720db6559235 | -8.42758 | -47.27977 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28d44cb6-7693-3bb6-8942-b8e063e3de89 | -6.66268 | -44.54768 | 2025-09-10 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63a265a3-24dd-3ad6-9bb0-3b3c86e0d807 | -8.49282 | -45.65977 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8242068-bbdf-3c2e-a6d8-f925e43d3c75 | -10.88369 | -55.70074 | 2025-09-10 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5caa0f7-9709-3315-be6b-d5702095797e | -5.70358 | -51.64275 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daee43ba-79d6-3535-908c-e1ac8d085e6b | -6.85111 | -47.92361 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16089c2a-bedb-3d8c-b908-95b54c403f89 | -10.19072 | -49.5879 | 2025-09-10 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 151aaf1b-962d-321b-8e6f-7de057056acf | -7.81441 | -47.50489 | 2025-09-10 04:42:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e75e550-1609-305a-a25c-0b2634df5347 | -8.67147 | -45.74881 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1abf827-0b65-3f4e-83c9-e7a5c208ab18 | -8.42063 | -49.12536 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13899554-30b6-338a-9f2b-da1321096603 | -11.45937 | -49.27557 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3505dde1-41e2-3e1f-9ec6-9694fbf2728f | -7.70736 | -44.84648 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e2fbf663-bb23-3a19-8f30-a13e3287e524 | -11.6671 | -46.91274 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e0cf25b-598e-3ba4-a605-3e17ed31f30f | -10.65471 | -48.60707 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a08e3e99-b6a2-3014-aaad-d89d544c7e6c | -11.43434 | -43.58593 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9969a722-ceae-39ef-9fb0-6b4710d699cc | -8.07142 | -48.63126 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87e341ce-dcc2-3452-8b36-6af77eb4995e | -10.56923 | -52.00564 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f931f98b-0050-37cd-bcf7-4dfb106cfbe4 | -10.56092 | -51.498 | 2025-09-10 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 989e64f7-6e48-3aad-94c5-49c89a603ca7 | -9.06805 | -46.97899 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 68aaa898-8737-3d63-9342-2427312bf696 | -8.70409 | -47.87402 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1bf03f1-a234-37b8-a802-611a24c5f89a | -9.66375 | -46.62297 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c90ba403-a603-3252-b111-0b9ed5eaf132 | -7.09912 | -50.76315 | 2025-09-10 04:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 592613ff-66eb-345a-91f1-994fe0241557 | -10.01549 | -51.67368 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72333ba8-f034-3dc2-ad9f-2890f9dcb6ad | -9.09988 | -46.96861 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a793c00d-fade-3b90-8748-aac0e3376231 | -10.54571 | -51.50653 | 2025-09-10 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7807e577-fc69-3337-8118-6fe0ab9157b3 | -8.01094 | -45.52495 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15e5632d-b3ea-3420-bca7-4b24e7bd95ed | -9.44642 | -46.71313 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba50baeb-cb67-38e7-8a2b-40fea3eae09d | -6.41933 | -44.48405 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4b22df5-0c38-3b9f-9400-47890809b9ce | -9.22158 | -50.52693 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dad18da-fef3-3997-9d4d-acb2cfa28233 | -7.08941 | -44.15648 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 503fb81a-e89c-370c-a47f-204cfb883ac8 | -6.67927 | -44.54671 | 2025-09-10 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36c57ccb-dee3-34ed-bb72-a330efd170a6 | -9.80104 | -47.79119 | 2025-09-10 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 704d17e3-d37a-3533-9e27-f0c0f6033058 | -10.76429 | -47.72664 | 2025-09-10 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7328d2a5-fd55-3548-bd7e-44f7d9bb46e7 | -10.5485 | -51.51067 | 2025-09-10 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db19fe84-7f65-3db5-9390-ecb2bea631fd | -9.09182 | -47.04767 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d938d44d-0d4b-36a8-b725-ab9a837a4c8b | -12.08205 | -45.47606 | 2025-09-10 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e4c16988-e199-3662-94ab-cb4ef1657fb6 | -10.7649 | -47.72264 | 2025-09-10 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e8bb63b-081e-3aff-bfd5-935a753a4775 | -7.4649 | -44.94862 | 2025-09-10 04:42:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6116952c-5367-358a-8faa-da5e829c81d1 | -7.70811 | -44.84132 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0dc32bdf-dc7b-32a3-a5ee-07f95f2a0044 | -11.12518 | -52.02427 | 2025-09-10 04:42:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c04d3da3-0931-317e-87b0-fb22670c80ac | -9.52026 | -43.05927 | 2025-09-10 04:42:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 765c2530-7738-3628-8518-b20959a920bc | -9.75852 | -45.40028 | 2025-09-10 04:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 97c2c64e-f2c8-3427-aedd-a46097e6d982 | -10.26786 | -48.81332 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd9da748-b2ec-3f14-a9cc-ba4ba4e8e3dd | -6.40855 | -44.44641 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af471d9a-a273-306a-86ba-7c450586b846 | -10.14555 | -46.18597 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5116cd99-28b8-373e-a91f-697ac5c17df5 | -11.80113 | -46.76128 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0677939-e266-3bd6-a587-2537685e5c27 | -10.00516 | -51.6944 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41c4aaf7-063b-38d6-9214-a54e3960a979 | -11.19508 | -48.37893 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 985b9382-c9f8-3773-b4e0-c587137129c3 | -11.46202 | -43.62349 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e975da9e-fb1a-3a38-8bc5-32a678d779a6 | -8.52204 | -45.71481 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README70.md)
