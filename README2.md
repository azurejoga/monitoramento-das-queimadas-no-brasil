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
| ce883c60-66ca-3bf3-a22b-75b675c66aec | -21.70749 | -48.4255 | 2026-04-28 04:06:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6897e1fa-afb8-34ee-a533-2c615124a5b9 | -22.2806 | -42.49873 | 2026-04-28 04:06:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0312dc91-0ab6-3a9d-80fe-64cb8d560cdc | -21.33314 | -42.27435 | 2026-04-28 04:06:00 | NOAA-21 | BARÃO DE MONTE ALTO | MINAS GERAIS | Brasil | 3105509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9ceaa78a-2866-3fb2-bc0d-75d198668a11 | -19.06287 | -46.23235 | 2026-04-28 04:06:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fbd3818-3fe3-3c1b-9874-7749416bd3f1 | -29.85775 | -51.19405 | 2026-04-28 04:08:00 | NOAA-21 | ESTEIO | RIO GRANDE DO SUL | Brasil | 4307708 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 46b0fcb4-9e3c-3317-bfd6-e2835546a2d9 | -31.96271 | -52.19741 | 2026-04-28 04:10:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| e31b2f4f-c9ca-3459-9b98-2ac2c5aea360 | -31.95295 | -52.20344 | 2026-04-28 04:10:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 5d07a397-eda1-306e-9e87-ba0d70aa8264 | -31.95783 | -52.20042 | 2026-04-28 04:10:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| f65a0e45-22a6-3344-a379-d0bb838b7143 | -0.16386 | -50.40638 | 2026-04-28 04:51:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f61fcf38-caed-34fc-b045-ee02fa4c7a0a | -2.26097 | -47.85818 | 2026-04-28 04:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0a3afa9-f1ca-3456-a851-f09e09578011 | -6.25781 | -42.58276 | 2026-04-28 04:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e038812b-a6e0-3f3d-8c03-a3067df21220 | -8.15193 | -46.6563 | 2026-04-28 04:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd348c87-5414-35b0-8539-2bac66e70fd3 | -8.48702 | -41.54377 | 2026-04-28 04:53:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| cfad3469-8603-3769-b0cf-31ed4b8aecfb | -8.48503 | -41.5453 | 2026-04-28 04:53:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 60e1ca49-fdc6-3fcd-b0a8-86604c43628d | -6.24708 | -42.57702 | 2026-04-28 04:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 802a2d1d-e2da-316b-a485-8db0312dac88 | -8.15632 | -46.65699 | 2026-04-28 04:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26a9ff1b-5419-3a73-ba1a-704019f6d7d0 | -6.25219 | -42.58173 | 2026-04-28 04:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5e4aedb7-85a8-35b9-a8ff-08275ad4b828 | -8.48567 | -41.54023 | 2026-04-28 04:53:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 07237e8a-21b4-3c4f-ac75-bf83e4f0fee7 | -6.27164 | -57.91039 | 2026-04-28 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 505d2aad-9194-3882-a0fd-5857d47d75cb | -6.27226 | -57.90673 | 2026-04-28 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88c96778-15d3-3478-8c78-91df4630d41e | -8.48769 | -41.53872 | 2026-04-28 04:53:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d7db87ca-a7c0-3ab9-ba43-6b38b77b21db | -8.94389 | -45.6663 | 2026-04-28 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8c94670-2229-3263-9e8a-7ebf5c4ea56e | -8.1601 | -46.66193 | 2026-04-28 04:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e668adf-ac73-3b8a-812f-2d6d22b1db59 | -6.24656 | -42.58082 | 2026-04-28 04:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fc1a4634-4371-316e-ad39-022548e3d119 | -6.25271 | -42.57793 | 2026-04-28 04:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 415ea096-9c73-3742-a737-42cb6fb2f195 | -11.84079 | -55.01762 | 2026-04-28 04:55:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cba99db-13f3-33c5-8d5c-32e4d633738d | -14.33702 | -53.85003 | 2026-04-28 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e6ea8ea-6c2d-37f2-9668-95cafba9e0a5 | -13.40722 | -45.329 | 2026-04-28 04:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddba9dcb-5edc-3aae-9a2b-7ef035860554 | -14.33813 | -53.84291 | 2026-04-28 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4911b7f7-e1fc-3d6c-95c8-54eaee7f6197 | -13.40763 | -45.32576 | 2026-04-28 04:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b589268f-0e6b-3e59-990c-0e5d842d9448 | -16.17527 | -50.97509 | 2026-04-28 04:55:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 484cb3a9-7240-34f5-ac32-6302d8614af3 | -13.40163 | -45.33158 | 2026-04-28 04:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41b0e76c-d09c-3eb1-bb3a-350e3bbed3ce | -11.85203 | -55.01208 | 2026-04-28 04:55:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5b039ac-957b-3c36-ab1f-d993bbdceddd | -15.95877 | -47.76505 | 2026-04-28 04:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cfd1db2d-019b-336b-8907-c9e86b9cf12f | -13.40683 | -45.33222 | 2026-04-28 04:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf31b0b7-4c73-3bb6-8014-fe93f8611bbb | -14.33426 | -53.84592 | 2026-04-28 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2b3a0a0d-299e-364b-80bf-8e08f25ac7bd | -15.84013 | -50.8898 | 2026-04-28 04:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9594dd0c-bdd9-3796-a628-ab0ea64d6ff3 | -14.33149 | -53.84182 | 2026-04-28 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ac9b8807-bfec-3623-ad43-ed3c50246d36 | -13.39683 | -45.32774 | 2026-04-28 04:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5615dd2c-0052-3876-bd98-b7dd18862701 | -21.70827 | -48.42873 | 2026-04-28 04:57:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc6ebc85-6e99-379c-afda-b7d275831dec | -17.70931 | -53.27998 | 2026-04-28 04:57:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5c7e6d75-8a18-3a69-84c1-e913d8002f85 | -21.70353 | -48.42833 | 2026-04-28 04:57:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fb3007e-3332-3926-baef-2a920610a889 | -29.97841 | -51.20125 | 2026-04-28 04:59:00 | NOAA-20 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 2fa086d1-eda3-366e-83e0-9c0914bea50c | -29.8549 | -51.19254 | 2026-04-28 04:59:00 | NOAA-20 | ESTEIO | RIO GRANDE DO SUL | Brasil | 4307708 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 9af1367a-ae5a-3281-b10d-7434e6e74333 | -31.96158 | -52.1963 | 2026-04-28 05:01:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 49ac2ef5-6888-32d1-a310-7100604361c3 | -31.95258 | -52.1997 | 2026-04-28 05:01:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 5708c125-8352-30b2-944d-bc742aed2df3 | 2.72948 | -61.35957 | 2026-04-28 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f7c5644-f00d-3e90-95a7-9b59e902ef74 | 2.73173 | -61.35172 | 2026-04-28 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65477160-9cf2-34d3-b221-879e3d7c6727 | 1.82355 | -60.87125 | 2026-04-28 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 434def83-4c4c-39eb-b350-559f0398dc9f | 2.72833 | -61.35226 | 2026-04-28 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e02aee3-5d72-3a35-83a0-8bfe61be065f | 2.52633 | -60.31998 | 2026-04-28 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffc8fb78-b3ca-3391-bd40-defa4960f968 | 1.82191 | -60.87115 | 2026-04-28 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a36ec3b9-adc5-3cb0-b68f-974a8060c853 | -6.27665 | -57.90667 | 2026-04-28 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bb6ad0b4-bbe0-3815-b88c-62edc717b61a | -6.27594 | -57.91169 | 2026-04-28 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 087de080-ff39-3e64-b563-729beafd9410 | -8.48622 | -41.53535 | 2026-04-28 06:12:00 | AQUA_M-M | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 66caaeec-217d-3459-b80a-103861dbbc74 | -13.40378 | -45.32755 | 2026-04-28 06:12:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c3b5bf00-a81b-3be6-afb0-5ef511f1fa66 | -6.27749 | -57.91056 | 2026-04-28 12:40:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5ce5d729-ac7a-3148-9431-ed5a02abd78b | -17.7125 | -53.288 | 2026-04-28 12:42:00 | TERRA_M-T | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 86315cf4-16d1-3005-85ef-1ad8f6ac0f28 | -17.71476 | -53.2673 | 2026-04-28 12:42:00 | TERRA_M-T | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| bc2c4420-9958-3ee9-bb0a-6045b96313cc | -18.70642 | -54.98845 | 2026-04-28 12:44:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e072a1b0-bc00-3d0c-a0cc-37ce6886489c | -18.79321 | -51.91415 | 2026-04-28 12:44:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 06efe62e-4ba1-312d-b14b-19fe2cc12ba8 | -31.39429 | -53.70551 | 2026-04-28 12:46:00 | TERRA_M-T | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 60.5 |
| 5c3dc3d5-730a-3dd7-8cf5-9927f57cb6ec | -31.39198 | -53.73677 | 2026-04-28 12:46:00 | TERRA_M-T | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 43.3 |
| 25918c65-5d6e-30d9-a294-40cc49809933 | -31.394 | -53.71259 | 2026-04-28 12:46:00 | TERRA_M-T | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 85.9 |


