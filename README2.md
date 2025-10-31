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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ab2173d-8a27-343c-b2d3-d66d0de8025f | -2.9985 | -49.4488 | 2025-10-31 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 7ccc61a6-2240-3468-b420-cc0a04bc1895 | -14.079 | -44.1483 | 2025-10-31 00:20:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| afd2c3c4-537c-33de-947a-8f9099b15fb0 | -3.0171 | -49.427 | 2025-10-31 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c8870082-56d9-30f8-af85-cff266bb5561 | -14.4756 | -51.5338 | 2025-10-31 00:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 5a0eb87f-a11c-3679-94dd-5209b96976da | -14.4946 | -51.5526 | 2025-10-31 00:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| b357d149-47d1-37eb-a2bb-833622345076 | -2.6324 | -48.499 | 2025-10-31 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 4ff98876-b3bc-334b-ba55-b445076af01c | -7.6677 | -43.609 | 2025-10-31 00:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| bac74022-11c5-3eb4-baee-9f0d096126c8 | -3.0355 | -49.4476 | 2025-10-31 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 2ff4f5e2-e1f3-395e-a52f-dec0e6f1e4fe | -9.5067 | -47.2763 | 2025-10-31 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f73cad5f-e32d-35c4-98c5-45e3a51abf3b | -10.2466 | -44.6092 | 2025-10-31 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| aa31164f-2493-3fdd-9a86-b178df86c58d | -7.6491 | -43.5876 | 2025-10-31 00:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 8deebc63-1b27-3802-8c57-24796324fe18 | -10.9397 | -44.1663 | 2025-10-31 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| f3efb80c-28e2-3a66-9e43-df789be2a2e7 | -4.5583 | -45.656 | 2025-10-31 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 0315f948-0d40-3dc2-8267-8b7516b3415e | -7.6491 | -43.5876 | 2025-10-31 00:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 314.0 |
| d842bba5-48a1-3cea-a890-2cc93e3c1dcb | -10.9397 | -44.1663 | 2025-10-31 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5f9f6b0d-5f3e-34f0-8720-bf80bf74cb49 | -14.079 | -44.1483 | 2025-10-31 00:30:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 434bf319-4ef5-354b-83d9-8ea2737343d5 | -4.4363 | -44.4174 | 2025-10-31 00:30:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 543f6924-4c65-3ccc-a75f-2e370a73b27c | -10.5455 | -48.7221 | 2025-10-31 00:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c35df281-7f29-3843-864e-893a2f4d0c5d | -2.3178 | -48.5717 | 2025-10-31 00:30:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8c613374-3922-3d81-a499-94b4bef88b39 | -2.9356 | -51.4613 | 2025-10-31 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3b5d9180-489f-36d9-a922-b5422bcf7414 | -7.6682 | -43.5623 | 2025-10-31 00:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| f1197161-eba3-3aad-a779-a091a9835e51 | -4.4663 | -45.4814 | 2025-10-31 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f2149355-b3cc-3696-b1a6-e547094f60ee | -14.1365 | -44.1851 | 2025-10-31 00:30:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 8fc5d12a-f6eb-3c5d-85f4-c66263f6ba3e | 1.2852 | -60.4265 | 2025-10-31 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b61b675a-ae7a-3fb7-a496-f516877151a9 | -10.5458 | -48.7002 | 2025-10-31 00:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 1624f5f8-45ed-3bf0-a3c8-1cc05455981f | -4.8402 | -45.3249 | 2025-10-31 00:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9c21d456-f09d-3bfa-b76e-275064894394 | -14.098 | -44.1685 | 2025-10-31 00:30:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 168be5d9-fdf1-35c4-b0b7-2749522d629d | -4.0634 | -47.4943 | 2025-10-31 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 255e01ed-9805-3356-a0b5-16a3e7c56e0a | -4.5584 | -45.6335 | 2025-10-31 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 46c9bedd-861d-379e-9eda-7974cb42d9f6 | -7.6488 | -43.6109 | 2025-10-31 00:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ce91298c-5f10-3963-a419-ab1515c1a39d | -3.017 | -49.4482 | 2025-10-31 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 8cba3bec-5915-3c51-b6d8-fa240fa65710 | -3.5146 | -45.975 | 2025-10-31 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 8ae98069-b5aa-3fe7-869d-624493c83096 | -7.6677 | -43.609 | 2025-10-31 00:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 00946590-b6de-3136-848d-763306ceb9eb | -3.0355 | -49.4476 | 2025-10-31 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d532fad9-bec4-3358-9003-36114239d9ce | -14.0985 | -44.1447 | 2025-10-31 00:30:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 94df159f-842f-3ec3-a46a-2d18c7696a28 | -4.0447 | -47.5169 | 2025-10-31 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 17823495-7ff3-3839-b515-2e97752c6ec2 | -2.3178 | -48.5932 | 2025-10-31 00:30:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ffb61e7e-d2d6-3b35-9c71-342bc497fea1 | -14.117 | -44.1886 | 2025-10-31 00:30:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| f9cb21c5-544e-3dd0-9231-18e3a403f3ca | -2.9089 | -48.7268 | 2025-10-31 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 1a5c06f8-d4a9-3508-b212-9aa2c5218e10 | -3.0171 | -49.427 | 2025-10-31 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| de543525-8c14-36df-822a-8fadc0df6b8e | -7.3734 | -44.6316 | 2025-10-31 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 5cd1af63-2198-39f3-ace3-5e39637269c8 | -14.253 | -46.0068 | 2025-10-31 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 182e237a-e7b2-35d7-970a-b5fbdd9e32a1 | -7.6494 | -43.5642 | 2025-10-31 00:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| fb00b1b3-470a-3233-8865-4cc8bbb35a33 | 1.2852 | -60.4454 | 2025-10-31 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 1bc2788d-3082-3a4f-8a5c-7523c0dc55f1 | -4.0449 | -47.4951 | 2025-10-31 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| d5635d35-e2dc-32e2-a667-569096796591 | -7.668 | -43.5857 | 2025-10-31 00:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 317.8 |
| 81a92e0d-273d-364a-bc13-4af53e6d643e | -14.2335 | -46.0101 | 2025-10-31 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| d6273ec2-90bf-31a1-b408-666335ba65fa | -14.0785 | -44.1721 | 2025-10-31 00:30:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6940f246-2a21-36b7-98ff-b5df30748442 | -3.5332 | -45.9742 | 2025-10-31 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 044f7f2b-a15b-3af7-bdd6-298563374c67 | -3.1465 | -49.4229 | 2025-10-31 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e2b8def0-3544-3567-8672-7954598aa860 | -14.2525 | -46.0299 | 2025-10-31 00:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| a8d19623-2bfb-307f-94c5-e659a5d28af3 | -2.9089 | -48.7268 | 2025-10-31 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| e1e72e6b-0d4b-3964-be43-23841c175f3b | -14.2535 | -45.9837 | 2025-10-31 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| fdee2f53-ab2b-3710-ab38-71ac32c4d37a | -9.7421 | -48.0228 | 2025-10-31 00:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 784a6be8-8bae-30fa-a734-e726a76cb75c | -4.3649 | -46.778 | 2025-10-31 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 757cf6d0-1349-3978-9a88-ce60bc99a2a4 | -4.8582 | -42.9332 | 2025-10-31 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| f7be2123-9e05-3739-adc4-04c2b69a0ee7 | -4.8402 | -45.3249 | 2025-10-31 00:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 886a118b-9255-3a25-b4c2-bc3aa950b2bb | -14.253 | -46.0068 | 2025-10-31 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 209.3 |
| a5059202-43eb-3f7a-b570-46a8cde962b6 | -3.5252 | -47.5389 | 2025-10-31 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| eaec88a1-cb7b-3358-b8ea-d882d81d762f | -4.4869 | -45.1872 | 2025-10-31 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a2444da3-242a-3913-983a-78365f24b6b2 | -10.5455 | -48.7221 | 2025-10-31 00:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 41b4ecca-27bb-3813-b68a-b9c7a869aa02 | -5.0399 | -43.6205 | 2025-10-31 00:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 0771b382-2f7f-342d-bea4-80cb35101514 | -11.738 | -50.2295 | 2025-10-31 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 30deec3d-8047-3dbb-af96-bb0de6074002 | -11.7192 | -50.2103 | 2025-10-31 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 823a242e-5a13-34c0-84cd-1dc9f18633dc | -9.7232 | -48.0248 | 2025-10-31 00:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 06bb9fa2-1cdc-361b-92c4-ee50e405aa82 | -10.5458 | -48.7002 | 2025-10-31 00:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| aa1f0742-b3eb-3343-bd68-f7f0a0a1718d | -3.5251 | -47.5607 | 2025-10-31 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 398b5aa5-bed4-3ae0-a0b8-95a32150b873 | -11.7383 | -50.208 | 2025-10-31 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7d6732e1-fe3a-3293-bb7e-d72466c206ce | -14.117 | -44.1886 | 2025-10-31 00:40:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8643ca52-9720-3592-b93f-226c12a64ffa | -4.0634 | -47.4943 | 2025-10-31 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 88d76691-b8f4-3028-bfe7-9f52f1bf6e65 | -2.3178 | -48.5717 | 2025-10-31 00:40:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5459461b-cd0a-3750-a8fe-b9bcff59ff48 | -3.1465 | -49.4229 | 2025-10-31 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 2d8c1b91-a11e-3cf2-b9f6-0743a2cb4258 | 1.2852 | -60.4454 | 2025-10-31 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.7 |
| ec32ce08-860d-330c-95d1-b112af424bfe | -9.457 | -40.3889 | 2025-10-31 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 158.0 |
| 65cc655d-fbd4-3ed2-8ee3-9ed1ba814dc6 | -15.2141 | -51.3876 | 2025-10-31 00:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 808dadea-cb95-32f3-b516-25ee82688990 | -4.5584 | -45.6335 | 2025-10-31 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| e580b095-332c-3e1f-83fc-87753c533351 | -3.017 | -49.4482 | 2025-10-31 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1eae8870-b8d2-3d7e-b6fe-799b58a1da2d | -9.4761 | -40.3862 | 2025-10-31 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 191.8 |
| 6cf2f917-8016-3306-98a0-a278fd962282 | -4.5586 | -45.6111 | 2025-10-31 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 9351fe65-51d0-3b38-9f3b-6b1d09af4306 | 1.2852 | -60.4265 | 2025-10-31 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6a6f729d-a3e9-30c2-90df-65dbe32cba46 | -11.6999 | -50.234 | 2025-10-31 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 0b7c2751-8773-31a9-975d-7e3fcbd87a12 | -14.079 | -44.1483 | 2025-10-31 00:40:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 1049df29-2fbd-39e5-b245-2d46de409ad9 | -12.1308 | -47.1534 | 2025-10-31 00:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d1fc5fc7-73eb-3dc4-a13f-9aa956dd1760 | -2.3178 | -48.5932 | 2025-10-31 00:40:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 84639ac1-abed-32b6-ad66-3edb251ae1a5 | -11.7189 | -50.2318 | 2025-10-31 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 04a055f7-9e0d-3c75-b03b-ac0a0d17c81e | -14.0785 | -44.1721 | 2025-10-31 00:40:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2675bcca-c190-38ba-b3f4-0c6b00733f40 | -10.9397 | -44.1663 | 2025-10-31 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 562940e9-53ce-36c2-87a8-77547fca8f64 | -2.9274 | -48.7262 | 2025-10-31 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 8d9fd20a-bd34-3feb-8387-99e7413e8af7 | -5.0401 | -43.5973 | 2025-10-31 00:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 0e8ba7bb-3d77-3658-8a81-b1c1acb52482 | -14.2335 | -46.0101 | 2025-10-31 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 682b8297-51c5-3494-ab4e-d9a173e72784 | -10.5293 | -44.7798 | 2025-10-31 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9692b647-1263-3a0e-8486-994f61366394 | -2.9089 | -48.7268 | 2025-10-31 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d3b54594-e872-3d79-bdef-de6da7ecd874 | -2.3178 | -48.5932 | 2025-10-31 00:50:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e19c9bb7-3cf0-3fac-a9e7-a411cf3c7422 | -3.017 | -49.4482 | 2025-10-31 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| d6f2d5f1-10fa-3369-a95f-e3c44316e611 | -14.117 | -44.1886 | 2025-10-31 00:50:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6bd0ab26-6e35-3f99-899e-f13020d75594 | -2.9356 | -51.4613 | 2025-10-31 00:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 15e34d4a-bf24-3a25-9599-7dbbcd09d871 | -11.7186 | -50.2533 | 2025-10-31 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 794afed2-7bac-3aae-b84e-efd85f7c8c6e | -5.0212 | -43.6218 | 2025-10-31 00:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6e924992-a9ce-3263-8ea8-343ce8a1d850 | -10.5458 | -48.7002 | 2025-10-31 00:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 91753539-4d5e-3ae0-a3f8-6235d2ffc833 | -14.2535 | -45.9837 | 2025-10-31 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |


[Clique aqui para ver as próximas entradas](README3.md)
