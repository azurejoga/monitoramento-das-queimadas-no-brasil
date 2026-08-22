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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aec4f8fb-7027-3102-a201-9b5db899d19e | -7.3625 | -55.673 | 2026-08-22 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| d7acdb23-ece4-33d1-961a-8e9e62778034 | -6.0181 | -57.8047 | 2026-08-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 07ed6c08-24a0-3cfa-88e4-01e4e5a92c0c | -12.2627 | -43.1127 | 2026-08-22 14:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 98.2 |
| e64621b2-8bc7-3e55-9a6c-0041792659d5 | -11.3472 | -46.0431 | 2026-08-22 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| bf0e25dd-41aa-391b-9dd6-267329a8ef4d | -6.8042 | -58.9954 | 2026-08-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| b0615e86-690d-3b1f-9f40-db1a5c2f47ed | -17.5891 | -44.6164 | 2026-08-22 14:00:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 137.6 |
| a70df10f-357d-3e30-9552-cef67ff940a1 | -6.5302 | -58.5227 | 2026-08-22 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4499467d-5a7f-306b-97fe-2b553e0a1437 | -11.3667 | -46.0177 | 2026-08-22 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 274.5 |
| bcd2f8d7-f80d-360b-8056-9e740cc7d6b3 | -9.1201 | -61.582 | 2026-08-22 14:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f3a3cd49-a630-36e0-b8a3-fb64195ffdc1 | -5.9997 | -57.8054 | 2026-08-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| a414ec4c-205d-37d9-8ad2-c6987c0fa2b2 | -6.099 | -59.965 | 2026-08-22 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6a8d50a1-123d-318a-94d5-86754ffb6e87 | -8.5408 | -54.7995 | 2026-08-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 69c227cf-8f7c-32cf-9e21-98841b3a6238 | -13.8387 | -53.995 | 2026-08-22 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 7590d200-3d64-3993-85da-aae2a8196b23 | -6.8571 | -59.4179 | 2026-08-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9f2b0b6f-3cb9-3cfb-aacf-ea462a66f37d | -8.5406 | -54.8197 | 2026-08-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 260.0 |
| c4f1a690-d687-3187-89fb-64521f88d728 | -15.1873 | -48.7671 | 2026-08-22 14:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1c61fe19-8cfc-3964-a6d8-c3d174845f76 | -14.0688 | -54.01 | 2026-08-22 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 302.5 |
| c670f286-38d5-3852-a115-6a06c826ef44 | -9.4744 | -48.2917 | 2026-08-22 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 0312b90b-40da-3b7e-8638-bc300e554528 | -8.3904 | -62.6774 | 2026-08-22 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 4e256d8e-e388-357e-969c-943001728968 | -6.9315 | -59.3184 | 2026-08-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 971dc0e9-3681-30cb-a9f0-9e983783b6aa | -6.8569 | -59.4564 | 2026-08-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| a2444d62-8885-31bc-b652-3171bf97415c | -5.9996 | -57.8249 | 2026-08-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 3da2c6fd-58f3-3ba2-8537-f09a0ad710e4 | -7.0191 | -48.0323 | 2026-08-22 14:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| f3c2b436-a036-3a6c-9902-e9c12d431018 | -7.344 | -55.6741 | 2026-08-22 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 92e3ff31-952e-3069-880c-df8285b49eee | -7.3624 | -55.693 | 2026-08-22 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 49cbba93-aae5-3cf4-a038-978e3b03fba4 | -6.857 | -59.4371 | 2026-08-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 11d0a088-9cd3-3128-ad86-46d035b6037b | -8.5218 | -54.8411 | 2026-08-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 28bd5906-9d69-30a9-adc3-c27d690ca57d | -12.281 | -43.1574 | 2026-08-22 14:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 170.3 |
| 064c1215-4b48-315e-92af-23bd111b1d81 | -6.9699 | -59.0658 | 2026-08-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0cf41987-7674-340c-96c8-325fe745992a | -8.5221 | -54.8007 | 2026-08-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| a9773e41-a3ff-36ce-a1d3-1be85a7c5535 | -6.0992 | -59.9267 | 2026-08-22 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 8e9bde66-e133-32e2-8432-95e041f85082 | -9.0348 | -60.4551 | 2026-08-22 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 170.8 |
| ae3784b5-729a-3f2b-8ce9-5d1b699387cc | -11.3663 | -46.0405 | 2026-08-22 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 329.5 |
| 71cbc433-2c6c-3400-93d1-f6d6244b2800 | -8.522 | -54.8209 | 2026-08-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 90d132f0-6fbf-314b-82ee-f0533d3f7b34 | -6.1285 | -57.8393 | 2026-08-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 2ad11665-d032-3f32-b26b-6a693b9a7cbe | -9.106 | -60.9127 | 2026-08-22 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 561417a4-68cd-35ca-bae7-db0264004dc0 | -9.6951 | -45.9572 | 2026-08-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 54574470-2dfd-3011-a9e2-63334599be48 | -15.2069 | -52.8613 | 2026-08-22 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 64e0b1b2-ce24-3fd9-89b5-d30d9aa883ca | -8.4088 | -62.6956 | 2026-08-22 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 0e53d7b0-c8df-3fc1-b322-22772f758f28 | -6.254 | -55.391 | 2026-08-22 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 5f957d56-8782-3e2a-9517-ea355a17cde9 | -8.5216 | -54.8612 | 2026-08-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9cf1eb4d-cd1a-3fcb-965b-e28f2567c22e | -9.1909 | -59.4619 | 2026-08-22 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9e61297f-4692-396f-a704-f9eab9be726d | -8.1667 | -54.985 | 2026-08-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| d528b860-4d0e-3b6c-96a2-4c50fe77c55b | -10.9624 | -51.4214 | 2026-08-22 14:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 41139c6f-8a59-30af-9a4e-7ecd54221338 | -9.1724 | -59.4436 | 2026-08-22 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 0b6b1514-30a2-3496-a674-e5c853bb2ed4 | -9.0536 | -60.435 | 2026-08-22 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 5745acf1-bb8c-32ec-92bb-0caa20d14bc1 | -13.8195 | -53.9972 | 2026-08-22 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| bb7e05e5-4a2b-3829-b0ee-87c6b93e2262 | -10.7847 | -50.5706 | 2026-08-22 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| c2ae4e8c-7970-316f-b814-82cec284f1ac | -6.0991 | -59.9459 | 2026-08-22 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 8ea4298d-a7de-3236-a6c9-aa3ddfd2ce60 | -6.8755 | -59.4364 | 2026-08-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 71919155-5d24-338e-85be-a46811b6074c | -9.035 | -60.4359 | 2026-08-22 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| dd9b0d8d-a6b9-364a-85c0-d6c7457748b5 | -8.9042 | -60.5385 | 2026-08-22 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b2746765-6388-3189-92bd-a887c4e2b7c0 | -6.8991 | -55.7176 | 2026-08-22 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 6ac2184a-d4fd-38d2-8053-d71b8c4b621d | -8.1853 | -54.9838 | 2026-08-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 66bb4dbc-c0d3-30c9-8290-b2de61e9a271 | -6.8568 | -59.4757 | 2026-08-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 8a0298e1-65eb-3b37-9e60-c2fff580c83e | -6.1176 | -59.9261 | 2026-08-22 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 5bc7b4e5-3755-3e0c-8aa1-ae86673fe979 | -16.1279 | -43.6194 | 2026-08-22 14:00:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 426.6 |
| 93a4f5b4-0c7d-352c-9bb1-ef05e0273102 | -9.0121 | -50.7411 | 2026-08-22 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 9fa8c911-3da5-3376-9a06-12331685ca2a | -7.6911 | -44.8074 | 2026-08-22 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| f48ab3b1-6b7c-3838-86e3-2cf1cdae0877 | -9.0534 | -60.4542 | 2026-08-22 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 22d9a95c-4a75-382c-a5bd-4e3f810f2318 | -11.3854 | -46.0378 | 2026-08-22 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.6 |
| a18ff50c-3a6f-39ca-99ab-f052370e804b | -8.3903 | -62.6963 | 2026-08-22 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 19eacd8a-5eb6-39bc-9252-2ee660da0b55 | -15.361 | -52.9253 | 2026-08-22 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 475de4d6-9842-3922-b942-f9ebbb91aa99 | -16.1273 | -43.6437 | 2026-08-22 14:00:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 372.1 |
| 5b13a413-9306-36dc-8cb1-24462dcd573c | -17.5897 | -44.5924 | 2026-08-22 14:00:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 23b32aa4-b51a-3ee4-a5ae-1c5d6ca6f2b4 | -9.1201 | -61.582 | 2026-08-22 14:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 098ed1e0-4df1-3692-b863-fc2a9c66374e | -6.8569 | -59.4564 | 2026-08-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 48abace8-e7e7-3d11-a6b8-b9428971c9d3 | -6.5487 | -58.522 | 2026-08-22 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| cc8da52b-d2c8-3372-ba75-356f6f392653 | -8.3903 | -62.6963 | 2026-08-22 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 72def611-8ac1-3700-8f85-922a45e052f1 | -6.857 | -59.4371 | 2026-08-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 046bc446-709f-3a34-82a6-37588b9e8c01 | -6.97 | -59.0465 | 2026-08-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 83cc864e-4f91-3530-9841-8f9ebf970b1c | -6.254 | -55.391 | 2026-08-22 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 207.6 |
| a796a116-7a78-3a82-ab5b-1945deaa51d3 | -11.3667 | -46.0177 | 2026-08-22 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 8485a8c4-c25d-384e-950e-8e4b4e8a8bf1 | -8.4739 | -46.9831 | 2026-08-22 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5d0754d9-9b3a-34a7-b5ee-631ed7665197 | -9.0346 | -45.8735 | 2026-08-22 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| f6242bc9-c8eb-32f6-b50d-7a31f2579b81 | -6.9315 | -59.3184 | 2026-08-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 8045f649-f523-3100-b7e4-03c8ab2896a7 | -12.7605 | -48.401 | 2026-08-22 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| f8bd9ab5-be78-3c81-8462-5b4c3dfdcda1 | -9.191 | -59.4425 | 2026-08-22 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0482d08c-d623-3ddf-9845-bb0824d9128a | -8.9042 | -60.5385 | 2026-08-22 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 6a838da8-7ac7-3636-90e6-57c5368f1558 | -8.3904 | -62.6774 | 2026-08-22 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 55018c92-2f80-3f46-bdbf-cae8897dbcdc | -16.1273 | -43.6437 | 2026-08-22 14:10:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 332.5 |
| 6f7c42f9-2027-3535-ada6-456e2cb958a3 | -9.12 | -61.6011 | 2026-08-22 14:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ee8f6ca4-e862-3a5a-96b3-803a5d23ad0c | -15.361 | -52.9253 | 2026-08-22 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| ea9b0e4a-abf5-3d65-ae28-e6416caf6745 | -9.0536 | -60.435 | 2026-08-22 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 90f490ed-748f-30d6-b59e-f93922dfbc43 | -6.099 | -59.965 | 2026-08-22 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| f6570ed9-8e59-357b-a90f-aaad6153b73d | -6.0181 | -57.8047 | 2026-08-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 4ba5dd58-d53c-33c4-a528-eb9cc6192401 | -9.1722 | -59.4629 | 2026-08-22 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 0475cdb0-c9df-3de9-abbe-ac93e01e2a3a | -9.0348 | -60.4551 | 2026-08-22 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 160.8 |
| c2766967-ade2-3bef-8261-e383af6e8ddf | -9.0534 | -60.4542 | 2026-08-22 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 532aee60-4b6c-3d79-b8b9-29ca52a08df0 | -6.9699 | -59.0658 | 2026-08-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8ee5922f-d196-3806-ab7f-a414fc3a215d | -9.1724 | -59.4436 | 2026-08-22 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| e231fc61-67f7-3f93-8450-8e1cf073a4f0 | -10.7847 | -50.5706 | 2026-08-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| b764263b-05ce-39f5-a641-03adb238554d | -17.5891 | -44.6164 | 2026-08-22 14:10:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 25d9b619-feed-3e25-9e38-c16561cddcf5 | -13.0881 | -43.329 | 2026-08-22 14:10:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 211a52c4-ba41-3698-95fa-1eb75e015a1d | -16.1279 | -43.6194 | 2026-08-22 14:10:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 547.2 |
| 9090dd54-d91b-31a0-9bd1-02dbcddb9719 | -11.1527 | -49.9957 | 2026-08-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 60b8c189-fd8f-3b9c-bd4c-fec2363c0efe | -7.344 | -55.6741 | 2026-08-22 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 630c6c52-bc5d-3dc8-9388-64bb0cad5be0 | -8.3481 | -46.5058 | 2026-08-22 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 5e68dc84-9812-39e6-b628-e4f154aba3de | -6.3654 | -58.3354 | 2026-08-22 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e806d819-3b47-39a6-a51a-fea9aa60bf0b | -8.4088 | -62.6956 | 2026-08-22 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |


[Clique aqui para ver as próximas entradas](README90.md)
