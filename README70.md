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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c30021f-5e49-34c6-93f5-7e4a85feb7de | -10.951 | -57.1497 | 2026-08-17 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 4d09c65b-525b-35dd-9e0a-4d9e51a7c282 | -6.2563 | -47.7611 | 2026-08-17 13:50:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| a9049fa5-4c22-3549-9ff7-60538fe306ca | -9.1998 | -60.793 | 2026-08-17 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| aaced962-77fc-35b1-b5da-5f772a46c912 | -11.2314 | -54.0164 | 2026-08-17 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 0d91e0e8-8e59-3cf6-b924-03a9b5ec16d4 | -7.3824 | -55.4924 | 2026-08-17 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 66459005-a9c2-3797-8dbb-f92285950db2 | -9.3382 | -62.3344 | 2026-08-17 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 188.2 |
| 0c6ea35b-2da3-3849-942d-b919521ff402 | -14.2947 | -53.1052 | 2026-08-17 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 86b8b74f-7cca-37af-a33f-b41c39e7bed0 | -14.3902 | -53.1564 | 2026-08-17 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 3917dadb-46db-370a-b7b9-d563e99ad657 | -13.5124 | -46.2449 | 2026-08-17 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 177.6 |
| da598abc-b80e-38af-8472-1719dad13a90 | -6.2376 | -47.7624 | 2026-08-17 13:50:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 4830dfe0-7703-3ca7-a88f-a678450bb592 | -6.7647 | -59.4601 | 2026-08-17 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 0ca7f053-4762-38d1-b0ab-f8a4f704399f | -11.8294 | -51.7725 | 2026-08-17 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 6453e7d6-ecf9-37f7-917b-e21702ad284d | -7.7881 | -47.8607 | 2026-08-17 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| eb0a4821-51af-3a42-941c-44a4b70f53e9 | -6.9884 | -59.0457 | 2026-08-17 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 47fc9c00-bf7b-3cce-a952-4b275173d73a | -14.4871 | -51.9806 | 2026-08-17 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 8bb91aa1-baa2-33f9-91da-9dd1883deff7 | -6.2378 | -47.7406 | 2026-08-17 13:50:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 77bacf07-47a5-3122-8a14-f2dc13a5e186 | -6.6014 | -58.9844 | 2026-08-17 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6074fb2e-3049-3f7b-97de-11423db693c3 | -12.5588 | -47.875 | 2026-08-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 93299b3f-9db2-3d87-ba03-b4a7a77e4af8 | -14.4678 | -51.9832 | 2026-08-17 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2d455080-f279-3f4d-add7-41e2baec12b8 | -7.6053 | -45.7238 | 2026-08-17 13:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 838a2ab7-c8cd-38bd-84cf-2bb7d3a660e9 | -6.2565 | -47.7393 | 2026-08-17 13:50:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 0d12d29a-0460-3bce-b6bb-6f7ac9659439 | -10.5085 | -50.0228 | 2026-08-17 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 7ee72ada-1177-3efc-9563-102e2ae3001e | -13.2805 | -51.6886 | 2026-08-17 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f4386af3-51ae-3fa7-a8f4-40c0d9309e9d | -14.5065 | -51.9781 | 2026-08-17 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 45ac0efc-b41b-3001-a0ea-9880752ed575 | -7.1551 | -47.5191 | 2026-08-17 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5031022c-a392-378a-97ff-29834bea1f3c | -9.7905 | -47.2452 | 2026-08-17 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 76195c28-f5ee-30e3-9944-827eda93cd75 | -6.6199 | -58.9643 | 2026-08-17 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| cb9c33f7-936f-3696-b5b9-ba7c85286f8e | -11.1296 | -46.5244 | 2026-08-17 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 78fde2b6-c656-3970-a5a9-f78c86c8ba75 | -14.5061 | -51.9994 | 2026-08-17 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 1a5a80da-03dd-320f-8374-d816bcff9550 | -6.7831 | -59.4594 | 2026-08-17 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |
| a5af5752-cb1a-37b4-b7e5-45835f77b56c | -14.4868 | -52.002 | 2026-08-17 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 81442ea0-d783-333b-bc1d-1e0d574ea3f6 | -14.412 | -51.8628 | 2026-08-17 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3566935e-5374-313f-84aa-517d856e91da | -9.3381 | -62.3535 | 2026-08-17 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 34e8e522-9c25-3f37-b612-ada675f99468 | -13.493 | -46.248 | 2026-08-17 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| c7afa7d9-0347-310a-8aa9-3bd7bbd09078 | -14.8619 | -46.6351 | 2026-08-17 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 8b77052c-bc28-3b29-bcc8-665aeaca846f | -10.5275 | -50.0208 | 2026-08-17 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 49b01d93-f84f-3756-8045-af7a73a1c84f | -12.5396 | -47.8777 | 2026-08-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 16d6d93b-9e4c-35b9-8b33-5266b8e2c3de | -7.8071 | -47.8372 | 2026-08-17 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 979124b9-bec0-3909-90f6-42e26c3aa85c | -6.6568 | -58.9628 | 2026-08-17 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| bf7de7f9-c892-3c16-b259-0e954a95284c | -12.7009 | -48.5195 | 2026-08-17 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 65bb08cb-b4ce-3ee2-affc-95bd68485399 | -6.7123 | -58.9412 | 2026-08-17 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2fda47cf-a0b0-3b51-8171-6320dded1ae2 | -9.1998 | -60.793 | 2026-08-17 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 887aea6d-25c1-32a0-9951-88f08b4a7a1a | -13.2805 | -51.6886 | 2026-08-17 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 0790dce2-1ce3-345a-a759-7ed3418fb86a | -6.2376 | -47.7624 | 2026-08-17 14:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 289ca931-3e7b-347e-acff-5597d383be0f | -10.951 | -57.1497 | 2026-08-17 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 3bc4ec96-8cfc-39d0-b301-5b24eb324923 | -7.8068 | -47.8591 | 2026-08-17 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 023d69ed-63bc-3d5b-82ec-eee714de1b3a | -13.5128 | -46.2219 | 2026-08-17 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c9a0a354-15fe-3a09-9a27-bcc2185f247b | -14.8619 | -46.6351 | 2026-08-17 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 5f609f3e-8eba-3215-ba10-78c3fce38664 | -7.8071 | -47.8372 | 2026-08-17 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| af5e0237-49cc-32d5-910d-ad075875d4e1 | -22.0767 | -55.9708 | 2026-08-17 14:00:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 112.1 |
| c31ed524-614f-324a-aae5-a89bdade3794 | -14.3726 | -51.9106 | 2026-08-17 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 553f2351-4316-3f4f-85e2-2acb30659e4b | -6.7647 | -59.4601 | 2026-08-17 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 211.5 |
| 5cbbc7c2-c1f0-3acc-b074-02f48a5ee3c8 | -11.3235 | -46.3182 | 2026-08-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 454.5 |
| 2fcda2fa-f039-34ce-93e7-bc8802e7cc96 | -14.2947 | -53.1052 | 2026-08-17 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 3519d2e9-486a-3629-9bcc-7fbf0cb4c889 | -12.7009 | -48.5195 | 2026-08-17 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 08917b07-b86d-34ce-bbf3-a50c1e3b9962 | -14.3926 | -51.8654 | 2026-08-17 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e157cd2a-ba08-3383-94cc-de8c0f74aa0c | -6.7831 | -59.4594 | 2026-08-17 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 9d4bcc6b-d8e5-372d-954e-a2d7d5ec2d3b | -14.3733 | -51.8679 | 2026-08-17 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3748a92b-4ad0-3c0c-92b3-f104aa5c7334 | -9.127 | -46.0214 | 2026-08-17 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2b7f82d4-fe1c-3a2a-a7cc-ff238242919a | -6.6198 | -58.9836 | 2026-08-17 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 7dd58ffa-ceba-3e2f-b33c-458352a27927 | -14.3718 | -51.9533 | 2026-08-17 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 47e8929c-7a93-39cd-985b-a562d157966c | -5.5072 | -43.6808 | 2026-08-17 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 7a1693f6-a506-319a-82ea-1d504721748f | -9.7719 | -47.2251 | 2026-08-17 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| eaf1e742-507f-3814-946e-8e281d37014e | -7.7881 | -47.8607 | 2026-08-17 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e1d8911e-8953-328e-bbf0-c6907b24d556 | -11.3239 | -46.2955 | 2026-08-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b1aa6782-13b9-3fed-9223-17db8a031c44 | -12.5392 | -47.9 | 2026-08-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e987a589-5f5a-31ce-b8cf-bcc390ad95b3 | -13.493 | -46.248 | 2026-08-17 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 54611585-621c-3948-a3b6-cc5e5f498ea6 | -2.1729 | -54.4265 | 2026-08-17 14:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 526128d4-d71c-3ee7-a33d-5230180c8ad4 | -9.7905 | -47.2452 | 2026-08-17 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 11a69add-b217-33ce-91d3-0784b310f59d | -13.5124 | -46.2449 | 2026-08-17 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 69924ad6-22fd-3c97-b224-5381153d3a60 | -14.3729 | -51.8893 | 2026-08-17 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 89f7c724-f4ba-366c-9ad2-b9e4ca146d48 | -6.6014 | -58.9844 | 2026-08-17 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| f287f143-aafd-31fb-b458-78d5260ac888 | -9.3196 | -62.3353 | 2026-08-17 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 5d35b195-87c3-3b73-bc2a-3eb0a7e73fe6 | -6.6199 | -58.9643 | 2026-08-17 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 1da661a7-2876-300c-82ac-d14a742dda92 | -14.8614 | -46.6581 | 2026-08-17 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d03acca6-09ba-3fb5-a62f-932733fdee69 | -8.5212 | -54.9016 | 2026-08-17 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| e93e044c-033e-344d-85a8-6b7b478cfc47 | -11.4904 | -46.6118 | 2026-08-17 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 95e61655-1540-31df-99b9-54de40ddf37a | -7.3824 | -55.4924 | 2026-08-17 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| a1e63c42-c2bc-3c66-88c6-c6b8a2de6824 | -14.4868 | -52.002 | 2026-08-17 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 67074186-9c15-3542-887b-ae2905a97eb7 | -6.2378 | -47.7406 | 2026-08-17 14:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 6d936b20-2dd5-3cf5-9545-4c30e44ad817 | -14.8814 | -46.6317 | 2026-08-17 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d2d73d2e-a450-3cab-82f2-011c91e7e52e | -11.4907 | -46.5892 | 2026-08-17 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 76bfd9f0-ad40-3638-96ec-e77f7ff79b65 | -8.6348 | -54.7124 | 2026-08-17 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 66488fcb-d535-33af-ba5f-c8edfad887c7 | -11.5099 | -46.5866 | 2026-08-17 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b85888ec-46d4-3436-a8db-39a007df2da2 | -9.3382 | -62.3344 | 2026-08-17 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 67bc3f22-57a1-3515-87eb-23c693cc0506 | -14.3722 | -51.932 | 2026-08-17 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 3f2d2cf8-52db-3154-9b79-11a3c917058d | -6.7123 | -58.9412 | 2026-08-17 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| edbf21ca-810b-33db-9d08-c0b7c6f413d2 | -11.472 | -46.5692 | 2026-08-17 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 309e94bb-8c4d-3466-83b7-d825c918ed37 | -11.5095 | -46.6092 | 2026-08-17 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 357.5 |
| 0f529599-a7d5-3179-80ca-e8fa200992c4 | -6.6568 | -58.9628 | 2026-08-17 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c1c15831-41cb-33dd-a937-755327c7870b | -9.7908 | -47.223 | 2026-08-17 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| b456ea4a-596f-398e-8865-26ebe40a1e61 | -14.2568 | -53.0679 | 2026-08-17 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 81694b91-b18b-35a8-aa92-7227c38c3d0e | -12.5588 | -47.875 | 2026-08-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 552dcdf7-32f9-3a9d-9498-9dceb22f6c6c | -14.4871 | -51.9806 | 2026-08-17 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| b31f42be-1e12-3261-8e96-135246c9c18c | -6.2563 | -47.7611 | 2026-08-17 14:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| b565ef5d-679a-35c3-b8f3-737b8fc81033 | -6.6384 | -58.9636 | 2026-08-17 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 58fd77c3-82df-3079-a78e-5bba013ae43b | -10.9322 | -57.1511 | 2026-08-17 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a35546a8-a97f-35e2-9f20-dbed2511a3d4 | -5.5074 | -43.6576 | 2026-08-17 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 27a6d2b8-8f65-334e-8040-26fc95391cea | -11.2314 | -54.0164 | 2026-08-17 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 417b9c95-091f-384e-804b-ea76916dbf06 | -6.2565 | -47.7393 | 2026-08-17 14:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |


[Clique aqui para ver as próximas entradas](README71.md)
