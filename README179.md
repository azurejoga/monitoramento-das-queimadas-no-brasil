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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfc61d16-b383-3337-8c13-f5805e8454d2 | -11.0223 | -54.1379 | 2026-09-28 19:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| e5aeaa0d-61b8-3508-9c30-c7823fa40e6c | -9.7051 | -58.1247 | 2026-09-28 19:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 0ec4cac3-e721-3bda-8125-eddc612ccbb3 | -11.5193 | -47.1689 | 2026-09-28 19:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| cbb24c69-a79d-3348-97d6-35d06a6e6d99 | -11.1771 | -44.8064 | 2026-09-28 19:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 8277a148-d289-3fef-bf3e-db6fc035873c | -9.1335 | -49.987 | 2026-09-28 19:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 074e5120-fa8b-3045-a1a2-b1c94fcfdf0e | -11.3247 | -54.1103 | 2026-09-28 19:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 28b7c90a-0ec4-31d3-9aea-3d901fcc4a3d | -11.1716 | -45.1301 | 2026-09-28 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 94c82140-38e0-375a-b7e5-935da36efa99 | -9.9595 | -50.1431 | 2026-09-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| d2e2d5da-e583-3d2b-92cb-405fc2f06cfb | -12.1202 | -57.1767 | 2026-09-28 19:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 27a62cd9-b31d-3980-8a01-09cbf8a92bd1 | -12.588 | -51.9617 | 2026-09-28 19:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 8c11fcf4-1ac6-391d-bd1a-7016fc561e4f | -11.5384 | -47.1664 | 2026-09-28 19:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 071c845f-cbea-305f-a995-5416bcf45d22 | -9.1682 | -45.7684 | 2026-09-28 19:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 055dd718-da84-392a-ae21-e69c9cef0eee | -11.6213 | -46.7742 | 2026-09-28 19:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 6f3cbd97-284c-3932-b0c2-d1e4f8f7b2cb | -11.1775 | -44.7832 | 2026-09-28 19:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 178.3 |
| cdc5dd53-26bc-32dc-a560-2bd8204d5be4 | -9.9784 | -50.1412 | 2026-09-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 43208c7f-f7be-3e00-a040-4256c8fef7ff | -8.2482 | -45.4356 | 2026-09-28 19:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| bc90552a-034f-315c-be6f-bee5cfd235b7 | -9.9453 | -60.7161 | 2026-09-28 19:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| deb8bef2-59cf-3955-a420-a2eac7b495c4 | -10.2065 | -50.0113 | 2026-09-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 6da0fd99-9c11-39f7-8d5c-64a867efb0e1 | -10.9254 | -43.8876 | 2026-09-28 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 25aa1520-6056-354f-81a5-e80a0ffeed06 | -10.8001 | -57.2007 | 2026-09-28 19:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 0dc9ce05-f773-300f-8952-ba2471661cee | -7.2181 | -45.0797 | 2026-09-28 19:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 09feb647-18d1-33f1-910c-c5f91c027630 | -10.8191 | -57.1795 | 2026-09-28 19:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 1a9dd9a4-0b21-3765-b1f1-23aedc62c25d | -6.1251 | -43.7262 | 2026-09-28 19:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 198b1206-2070-3391-9005-adae5bb4904d | -10.9445 | -43.8849 | 2026-09-28 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 72e63d00-b6e7-3a01-8a8c-9adcd65c07e1 | -10.5201 | -45.3554 | 2026-09-28 19:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 701a1619-7e21-3b3b-9c3b-3d66819274f2 | -9.8625 | -43.6348 | 2026-09-28 19:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| a3eeb7ef-0558-379a-9a06-088ab08c7ccf | -7.0674 | -55.4896 | 2026-09-28 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 159.8 |
| c7075ba5-e139-3ebd-b810-1ddd1d6d6fc1 | -11.1324 | -50.0839 | 2026-09-28 19:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 17992f4e-aa08-3cf7-8430-7671a13576d6 | -8.2291 | -45.4602 | 2026-09-28 19:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 4b92c181-9dcd-3fa5-873c-e1a9758e4c17 | -18.6834 | -48.6234 | 2026-09-28 19:10:00 | GOES-19 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 44d2d777-8ddf-31b4-a6c7-722e40e7ba5d | -10.2254 | -50.0093 | 2026-09-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 172.4 |
| d50a2a3c-d5d7-397b-8958-82e1c6394535 | -14.4151 | -52.8165 | 2026-09-28 19:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 33a4509a-df04-31e9-865a-c9767f2f8c46 | -12.5234 | -49.9834 | 2026-09-28 19:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| ec792f7d-dfe6-3063-bd8e-f18e51bdc630 | -10.7916 | -48.7377 | 2026-09-28 19:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 728efdd0-15b0-3cc9-8375-8beb7e3b8c92 | -5.76 | -45.19 | 2026-09-28 19:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de2ee21e-9424-3940-bb45-42f7a93d36be | -11.3 | -43.54 | 2026-09-28 19:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d09ae0ec-5102-3f6f-bb4e-4ea5ef568bcc | -11.62 | -43.53 | 2026-09-28 19:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d4296049-b996-33a0-9de7-d0b854824c1e | -5.73 | -45.18 | 2026-09-28 19:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6353c267-1bb0-30b5-a9b7-606a5c492930 | -11.07 | -46.11 | 2026-09-28 19:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7b412a-5a91-3f9b-be5b-df67726253d5 | -10.05 | -50.26 | 2026-09-28 19:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6eea2c70-a92f-3b91-b4be-2b8a552fa1a7 | -11.39 | -43.47 | 2026-09-28 19:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3e2091f-5aac-338c-9985-5df0e3801113 | -11.1 | -46.12 | 2026-09-28 19:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6138d4e0-f5bc-32d6-bcc6-15062c25a20f | -10.9154 | -50.7059 | 2026-09-28 19:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 4b588ae3-ad9e-3fdc-9eef-d287d2a66102 | -11.5384 | -47.1664 | 2026-09-28 19:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 953b9d9b-f79e-3c7f-9aa0-88145ba4ae59 | -8.664 | -45.3469 | 2026-09-28 19:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| b0239e51-5443-34d9-ba7a-c444b142917c | -11.4977 | -47.3281 | 2026-09-28 19:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 61e3edca-fe37-3fb0-987c-0c68a31601b7 | -12.9646 | -51.0886 | 2026-09-28 19:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 7b8368e6-ccdd-3c60-9fc3-4d5ce3eb1dc3 | -10.8238 | -60.744 | 2026-09-28 19:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 299.5 |
| a5b9c9c7-9335-3795-99d0-3b8a16416ab9 | -11.1775 | -44.7832 | 2026-09-28 19:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 72ba52da-e7c2-32cb-b4d9-e5b7f3d8f09c | -7.6852 | -54.7532 | 2026-09-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| b77fe64c-4090-31f5-a0f8-de1a49729ea9 | -10.9254 | -43.8876 | 2026-09-28 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| b24c83e3-3873-3aee-b747-65373b5948b3 | -10.2062 | -50.0327 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 0a82ac9b-89c5-3cf4-811d-2cebc3e591f8 | -11.6096 | -44.1382 | 2026-09-28 19:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 235.2 |
| 2b5495a3-8cc2-39e6-843d-35f5a8f01e48 | -12.9457 | -51.0695 | 2026-09-28 19:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ed17616f-53d8-3661-85d2-8ec0105ffecd | -7.4974 | -55.0256 | 2026-09-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 197.7 |
| 49882e1f-aaa4-3182-88a5-30aba233864c | -7.7038 | -54.7521 | 2026-09-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| b8f3af57-f7c5-3813-b700-04397f689e5c | -5.4762 | -45.1262 | 2026-09-28 19:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 2e75b6e2-3464-3f8f-9537-e5dc35dd5de8 | -9.7051 | -58.1247 | 2026-09-28 19:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 130e8137-de7c-3ed6-a8bc-811c3d2f13f0 | -9.1337 | -49.9656 | 2026-09-28 19:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 7b5873fd-6752-3b2b-a189-f0af18be5914 | -8.2807 | -54.7158 | 2026-09-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 4e1c7244-902f-33c7-802b-a4d3f5fdae10 | -10.9637 | -43.8821 | 2026-09-28 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 43aeb613-afdd-39b8-82c1-5f9cec688201 | -10.8001 | -57.2007 | 2026-09-28 19:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 152.7 |
| a359a3d6-45c4-39b9-8c98-8712bd7319af | -12.7868 | -54.0275 | 2026-09-28 19:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 8116a7f9-164f-373f-bd25-072d3a195b31 | -10.7916 | -48.7377 | 2026-09-28 19:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 36f8926d-2773-3729-ab94-8818b2fb5fec | -20.0991 | -57.2067 | 2026-09-28 19:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 9029de07-7eec-3833-906f-07460bf5fc13 | -9.0971 | -49.8836 | 2026-09-28 19:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 46987059-860c-30e8-9d3a-4a25a5a4e398 | -0.4889 | -49.1327 | 2026-09-28 19:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| a4fe5dbc-c9a1-36cb-ac7b-a2e9bf90d171 | -9.9595 | -50.1431 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 5c465143-65ab-3778-83f3-dc71d3856434 | -7.6851 | -54.7734 | 2026-09-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| a8ecbd18-5a39-32ec-87ba-00a8d9032dbb | -14.7295 | -45.5527 | 2026-09-28 19:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 696.5 |
| 777fa540-f3bf-36df-a011-934a9a976d13 | -15.2694 | -47.6327 | 2026-09-28 19:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ef3b36c1-8d42-3eb6-93da-1c8326b43c3d | -9.6864 | -58.1258 | 2026-09-28 19:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 138.6 |
| f5263729-a89a-3e5b-84ae-5372dd36ff87 | -7.0675 | -55.4697 | 2026-09-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| e2bc26ad-1887-3e46-8af4-f333c0797eb9 | -11.7178 | -43.4623 | 2026-09-28 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 0331c615-4415-3b27-a7e2-b23c627f5dbd | -12.1204 | -57.1567 | 2026-09-28 19:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| b0c1e151-437b-3915-ae0e-e6a8e74affad | -13.3267 | -43.9523 | 2026-09-28 19:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| a5c6de9f-e506-373f-b69a-566807d39215 | -8.6451 | -45.3489 | 2026-09-28 19:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| a5b0e9e7-32fe-374f-a5bf-70014ed91516 | -7.7037 | -54.7722 | 2026-09-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 4fadcc9a-b3f8-36e0-b44f-63edee88d888 | -11.3444 | -54.047 | 2026-09-28 19:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 330.9 |
| f95c3070-a4e8-36dd-8b08-9522296aa6db | -9.9784 | -50.1412 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| cdb587dd-daec-375a-bcda-6da7e9c529a8 | -11.0101 | -50.6958 | 2026-09-28 19:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 5059c7d3-3516-36cf-910f-cd8a05255679 | -5.7386 | -45.0399 | 2026-09-28 19:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 21d31984-7f4e-39f3-b5b3-f48821dd9c12 | -11.1517 | -50.0603 | 2026-09-28 19:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| c808d217-95cb-3391-ad81-3b64aa762d61 | -5.7388 | -45.0172 | 2026-09-28 19:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 96cd948f-4897-31eb-af99-b7696f4c5020 | -13.9015 | -53.6548 | 2026-09-28 19:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 162.0 |
| f2fc27c1-e973-32a7-bdf6-9df168a06014 | -10.7056 | -50.8341 | 2026-09-28 19:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 35789274-f472-31a5-8322-1cd0fff7ae46 | -11.1966 | -44.7805 | 2026-09-28 19:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 8dc78848-4177-34da-b973-688b4c6f2600 | -11.0796 | -46.079 | 2026-09-28 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 8bf35eb7-faa3-3f30-9d26-70b377e2d774 | -12.0694 | -48.5377 | 2026-09-28 19:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3d99c2e7-e8d5-3d78-b0cc-022e68310b05 | -10.8964 | -50.7079 | 2026-09-28 19:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 44d6989d-47c1-30ae-a2da-a76de7c2bff7 | -9.9396 | -50.2304 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 63efe036-5e2c-33f4-bf8c-461f9db79e91 | -10.8191 | -57.1795 | 2026-09-28 19:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 6b243672-9b98-38ef-95a5-3d3993b3f3fd | -12.9456 | -46.652 | 2026-09-28 19:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 234.4 |
| db613442-4df7-37d2-b487-14f5cff88fa6 | -8.2291 | -45.4602 | 2026-09-28 19:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 4fee9fb3-8205-37c4-8301-40616325ef8b | -11.2945 | -43.551 | 2026-09-28 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 571.7 |
| af3ec8b7-5038-3669-9e51-cecb12acc622 | -18.6834 | -48.6234 | 2026-09-28 19:20:00 | GOES-19 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 174.3 |
| d40cf9e8-6927-38df-a563-2f50e969f367 | -5.7384 | -45.0626 | 2026-09-28 19:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| a81dac77-5a4e-32dc-827b-80194749853e | -15.0807 | -54.6172 | 2026-09-28 19:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 18efee57-f44d-379d-a7a6-3b58eb4a8bc7 | -14.5171 | -52.4864 | 2026-09-28 19:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 8ede4cf3-f89b-3ab7-99dd-f60154a60b4f | -12.1391 | -57.1751 | 2026-09-28 19:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |


[Clique aqui para ver as próximas entradas](README180.md)
