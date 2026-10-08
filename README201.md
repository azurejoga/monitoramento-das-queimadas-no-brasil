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

## Dados Diários - Página 201

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91ec4022-abea-351c-81bc-f35837d95733 | -9.20689 | -66.0776 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f04dfb22-5771-3712-afdc-737ba0972a13 | -9.11141 | -65.36346 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee5c7980-db90-3b1f-a7a6-9deae5d2f12c | -9.86268 | -64.97822 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8be0910-5e4e-3be1-853d-6407159ebc07 | -9.06094 | -65.48592 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f513e782-8bbd-398a-a942-6a206f0467ae | -8.59998 | -67.30678 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 926a04b2-89ec-3e1c-8008-0499647e559e | -8.60419 | -63.06841 | 2026-10-08 05:44:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0443080d-38ef-342f-b3b6-e13e284d74a7 | -9.47467 | -64.36167 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b99fcefd-f041-3b42-911b-32033ee6566c | -8.61832 | -67.06165 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7c36187-1621-31f5-ae15-5a3a8ab0979b | -11.02192 | -65.20938 | 2026-10-08 05:44:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a35f9b24-e454-3c7d-a1cc-48e91792ad50 | -9.20393 | -66.09582 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98338efe-b0bf-3303-881c-c9aa71647196 | -9.05569 | -65.93328 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 386fac00-9f1e-35d2-b19e-1833d49bbd62 | -9.07486 | -65.48454 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67e05cd0-52e2-3d40-8eeb-cd627ddb6ad1 | -9.47853 | -64.35871 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68db9290-383e-35e2-b580-a3dccbeec461 | -9.8042 | -65.00452 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60ecb3b7-1e11-3a45-bc53-1c6f9daf9797 | -10.56426 | -65.39397 | 2026-10-08 05:44:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce866abd-3f2e-31ac-8643-0d883af6bca0 | -8.25351 | -61.39161 | 2026-10-08 05:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7746f857-82ba-3a21-857b-6608a9a28854 | -10.53114 | -68.0107 | 2026-10-08 05:44:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f56d289-74ba-365f-b89d-bcb4989ec712 | -7.89919 | -63.71077 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7c64442-c6f4-3130-864c-eff60bd4a013 | -9.6019 | -61.82186 | 2026-10-08 05:44:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19c1bf35-791b-34f7-83ef-1d5b67aa54c1 | -8.75645 | -67.70119 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17800072-4687-3120-8777-ed8920a2d08e | -8.07977 | -55.28925 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76ba5b51-1263-320f-9b61-4251b43f2197 | -10.32662 | -64.51605 | 2026-10-08 05:44:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 05fe9b8d-bd6f-30c3-8cac-ebf6559eb7c6 | -8.75952 | -67.70881 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b27614d-f37c-31d2-8955-08c660297b9f | -9.12264 | -66.01137 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d0147c6-40b5-3baa-9e5f-9926eddca0ad | -8.61429 | -67.02022 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| afb047ec-88f5-311f-bcbb-b904416e09f2 | -9.45921 | -65.45958 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54ba11b7-7ddf-3caa-bf66-bceb15f3c072 | -11.00428 | -68.50008 | 2026-10-08 05:44:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a23aac01-20ce-321d-b2f1-6548b9387ff1 | -9.54197 | -64.81543 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 903461f2-ec66-3aa4-95ec-2137cf3f6d04 | -9.51183 | -54.75143 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b8123e6-41ad-3eab-ba99-09dc5892c943 | -9.04076 | -65.93119 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 496ca5ed-3d94-30eb-b013-bf1616210745 | -8.66076 | -66.49969 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3412b3d2-8008-36e4-bfb4-bdb5546feaef | -9.54252 | -64.81194 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d89b04e-9ee3-3500-9299-d03f807a7bd8 | -9.48902 | -64.35682 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f544240f-b0c6-30a0-8f3d-46a3702c9509 | -8.75868 | -67.71028 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccecfb71-5180-3712-9f4f-52ac89c976dc | -9.16777 | -66.93918 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73dddd6b-16c5-3aa2-bf95-daeda14934c8 | -8.53454 | -66.97492 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b11d91a-6e58-3e3e-8fa1-02813632baf9 | -9.05906 | -65.93385 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8f3f96f6-04ca-3238-ae0d-1a81369c3352 | -8.64583 | -67.17954 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fc72433-aac7-337d-b0f7-9506e6bb471e | -9.48294 | -64.35228 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fec6b5a-a26c-358d-a917-a0515f17045a | -7.90251 | -63.71129 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 099017d3-eaa7-3fb8-a4d4-229d17068b10 | -9.25583 | -60.87862 | 2026-10-08 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ecf0ae2-95a9-393a-a3ee-017b4b915a31 | -13.80703 | -52.79415 | 2026-10-08 05:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af88f94a-34f4-346d-b83a-afa8832cbf8f | -11.749 | -61.06018 | 2026-10-08 05:44:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1545073d-4454-362b-8c39-2c4819638a67 | -10.81205 | -56.50282 | 2026-10-08 05:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 808f6cbb-ac5b-31d6-83a7-1aeaff463309 | -9.69018 | -58.09845 | 2026-10-08 05:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 517fd058-56bf-356e-8a5b-a9910a86b5cb | -9.07152 | -65.48399 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83fc9fcd-21f0-3e73-afe0-5711a55083cd | -9.35488 | -65.7495 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb3d22ae-f40e-346a-b863-56c57e6fc370 | -9.51628 | -54.75216 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40281067-a1c2-39a0-8133-3e6d08bb6708 | -8.61897 | -67.05767 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 853dbc02-03b4-3698-90e0-e8939163d7da | -9.55943 | -66.00031 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fb9ec16-825b-3227-b07d-0ec2aebf7572 | -9.11985 | -66.00719 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae39780e-727f-331c-b2de-d999ffe68a5d | -9.24783 | -64.44296 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84fbd168-5490-35b9-bd92-f4ae1163865c | -10.61935 | -60.48937 | 2026-10-08 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6507ffc-5e48-30f9-bfc0-46de75de60d5 | -8.64869 | -67.18415 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 212f3099-84e8-316a-ba05-7cb9fba9c3b5 | -9.49028 | -63.95924 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8162b697-1a81-3ee7-a1a3-02fde4733c7d | -10.56094 | -65.39342 | 2026-10-08 05:44:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 959be334-73ef-3538-90da-143be4137525 | -9.05628 | -65.92966 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b831c71f-d1c2-3bfb-abe3-92df47b4568c | -9.68985 | -65.01794 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d2850d7-8c7f-312f-9edf-3723a60b2ce9 | -8.62418 | -67.02595 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 469f8827-ad85-3c20-adbf-43b167825de2 | -8.08418 | -55.29634 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d8834df-deea-36ac-89eb-bc8e4151f383 | -10.61549 | -60.48878 | 2026-10-08 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae29186f-de47-3609-afd2-536d6d390947 | -9.04983 | -65.91781 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af7c7ab4-5815-3846-9140-77f78da7db54 | -9.04355 | -65.93536 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1edfd509-c394-33e8-8890-ba7b1d606cd7 | -9.12322 | -66.00774 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5842c14-69cf-3847-98cf-1c71dbb0165d | -9.49456 | -66.78582 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16bf0107-e910-3362-96f4-90fa94089581 | -10.28427 | -60.53638 | 2026-10-08 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0f9879a-dc89-39ae-91b0-d62d70d87461 | -8.07404 | -55.29182 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 775b1de4-0d1a-3091-9281-eedeff4b3d6d | -9.48018 | -64.34827 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a26cd1a5-657d-3980-bc3b-a39254023bd8 | -9.48515 | -64.35977 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52435590-0737-32f4-a537-6d1727cdbd0b | -9.03564 | -65.74899 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64ef51ac-a2c3-3f24-8626-1f6290c4a283 | -7.90382 | -61.6525 | 2026-10-08 05:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d5d19f6-2de2-3fa9-b8b9-816472ac1392 | -8.62314 | -67.0543 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 431a4260-4ea9-3a2a-a272-596e78e7b804 | -8.08329 | -55.30288 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3df60d9-cb3a-3dba-a203-b6d14c40b207 | -8.5252 | -67.00995 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2fd4be05-1b13-3407-a112-519c2900a210 | -11.98003 | -57.58681 | 2026-10-08 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a9b55b5-f5c8-3149-942a-05e38ea29192 | -9.48074 | -64.36622 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e5a66a3-29a8-38f1-b4fd-6f5e25b87fb1 | -10.6162 | -60.48393 | 2026-10-08 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aff5ec2b-25b2-3ab3-b6c2-5bb211d865c0 | -8.07317 | -55.29828 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c4e277a-27f6-3f3c-a7e0-1b55597d7802 | -9.45645 | -65.45551 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c103a59-358e-3fa7-9a3d-0c5845a863d2 | -8.75661 | -67.70396 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30324b1b-c206-33ee-a482-3d9ddb61c91e | -8.53676 | -66.98341 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68d4b546-b9cf-3168-a898-a9fa74461d8e | -9.0769 | -65.38682 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4d73790-752f-39ff-98bd-b8d68ff04a87 | -10.81244 | -56.49984 | 2026-10-08 05:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71569924-c7bd-3c6f-8c24-19358defa3db | -8.52299 | -67.00143 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d22a0d6a-fcb2-362b-bff2-55846a80d83d | -10.28357 | -60.54116 | 2026-10-08 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91309788-b103-3203-898f-1468bfec6b60 | -8.08462 | -55.2931 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 855cd97a-18d1-3198-8cee-8898b326c58e | -9.22722 | -67.52674 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a24a91de-1b3a-3bd3-a98b-4ec07e2e8a69 | -9.48239 | -64.35577 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b6e2485-6933-3025-80f8-0c8e75f0ce2d | -9.49233 | -64.35735 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fd62898-5e2b-3ce2-83e6-85c7a17fec2d | -7.44463 | -63.53548 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2943625a-b8ec-3f94-aba2-a28d0e8eeb0f | -8.61963 | -67.0537 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be3e3a3b-a905-3305-975a-b9e9d6041682 | -7.3119 | -72.71146 | 2026-10-08 05:44:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc1959e8-6734-38b0-9495-3001f32b3dc6 | -8.62067 | -67.02536 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| fc145720-5ae2-3e67-a140-d4e2f337f3bd | -9.22655 | -67.53086 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7067e199-a633-38f3-b9f2-dcbdf22ee3cd | -9.47798 | -64.3622 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc93ebcf-48f8-37f4-9b64-583d26d622e6 | -8.58923 | -66.97538 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8036d9a4-b032-3679-b277-133ca0735a9c | -9.34484 | -65.45596 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b2fa4f8-c545-3453-998d-e17bdb7f929b | -9.86544 | -64.98225 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5631b267-afe3-321c-876c-4397b9deaef0 | -9.05291 | -65.92911 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 997767b9-ceb2-342b-871a-731c5e4e6471 | -8.76005 | -66.9257 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README202.md)
