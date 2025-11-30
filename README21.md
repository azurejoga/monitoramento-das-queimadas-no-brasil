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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4331723-971b-3f79-8adf-adbcb6bf0ae2 | -17.49687 | -57.14892 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 10619cd8-4917-3d31-8162-eebed8ede269 | -17.49983 | -57.12258 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e645cac1-fa45-3d24-a8df-50c844271ed9 | -17.51349 | -57.14814 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5a9fb317-7451-3b28-80ea-59bc7c787f1b | -9.73536 | -63.64416 | 2025-11-30 05:37:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d37cc56-ee97-3486-b99c-f7057ee7ff8c | -17.50209 | -57.14958 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c3c099fc-73f5-3797-9f48-0ccaaa8f906e | -17.48974 | -57.11793 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2f25e134-23ac-381c-b668-8ba11943a238 | -16.21924 | -52.18006 | 2025-11-30 05:37:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a0c446b-5423-37e8-bc26-1ac198adf1a9 | -16.21862 | -52.18711 | 2025-11-30 05:37:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d2c386d-5c9b-3578-8c97-461b5ca1d008 | -17.50732 | -57.15023 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cf3bb200-d3f6-3306-a283-46c789f9d1bd | -17.51315 | -57.15144 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 74a1104f-046d-3c73-b8c2-782872707569 | -17.47854 | -57.12323 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5653777e-f9f5-3bdc-b544-20199ba1a072 | -17.51291 | -57.14761 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7974ebce-58fc-3d25-8ac9-0272282e37f4 | -17.49202 | -57.14498 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7cdc30ad-4abb-35bd-8b60-7d417588247c | -17.51385 | -57.14484 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 80d1658e-959c-31a7-9941-ffb5d3e16538 | -17.48451 | -57.11726 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 22a410f5-3ea9-3eb3-84bd-3df35ac66b00 | -16.8008 | -53.77052 | 2025-11-30 05:37:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da4021c0-78f0-33af-bc34-2b4f1448c125 | -16.80241 | -53.7723 | 2025-11-30 05:37:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9fcc9228-47a3-3a26-ac5f-88fd349c9d94 | -17.50506 | -57.12323 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 05ad2adc-f69d-39a1-ac50-bb7ecc2ed23a | -17.49165 | -57.14827 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5db5b5ff-8d92-3f78-bbed-7bab2c95e735 | -15.27996 | -59.91695 | 2025-11-30 05:37:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e4dcf28-1c51-3a8a-97f7-b13c964d6c3a | -17.47891 | -57.11991 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6fb3cddc-3608-3c5e-867e-5f52ec8f8a1c | -17.51254 | -57.15089 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| af4d86e4-da7c-3e04-97fc-ac0b852b7316 | -17.48414 | -57.12056 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8406b0b2-04bb-3460-809e-a697b854b92c | -16.22038 | -52.18261 | 2025-11-30 05:37:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e165ef30-96a0-32ee-99c5-e479d965eeaa | -17.51329 | -57.14431 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c4b8695d-4f7d-3574-88e9-5a75c838b46b | -16.79551 | -53.77689 | 2025-11-30 05:37:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3d97cc5-f7f2-3206-b294-a3243ec40c48 | -19.92978 | -57.44295 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a120a99a-64a3-3740-bf8d-16d23eeb3671 | -19.8571 | -57.78619 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a0c2c9e0-ecff-3429-9556-2c900e136f47 | -19.92415 | -57.4457 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 26e65f15-3871-365b-b46f-6f44ccc0d175 | -19.85676 | -57.78943 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b0f0037f-b2e0-348e-9b87-e64c6e7cfd14 | -19.92944 | -57.44638 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3e1d46a0-8cf1-3b41-9199-6473344e77cc | -19.85159 | -57.78879 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 14f6c652-0364-33c4-beb4-84ed6d623b02 | -19.84366 | -57.76476 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8d58dafc-fec6-3e98-91c2-273c555a4f97 | -19.86261 | -57.78359 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| c7165a24-37e2-3c47-8db8-f102035f322b | -19.07993 | -57.68888 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8ae28673-b780-3ece-9bfb-cbfe85c98fbd | -19.83849 | -57.76411 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 028a780b-0919-3a6f-94db-95b8fc2126e7 | -19.08026 | -57.68578 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1227f115-b6cc-3cef-8053-4f28002071c9 | -19.84229 | -57.77776 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5b5c5992-a20e-3eca-9b1a-c9defba2c6ae | -19.84196 | -57.78099 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 71991689-8408-3ed3-8575-0c641854f075 | -19.844 | -57.7615 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 4563aff4-c8ee-3092-80d0-fff8da4bbb4f | -19.84162 | -57.78423 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 139530fa-d440-3b24-b758-5c365db926fe | -19.84678 | -57.78488 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8b4c363c-3a8d-3c7f-9ca1-8c3fa28d97ed | -19.08537 | -57.68668 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7512c675-f7e2-3020-9322-34f49f185272 | -19.86226 | -57.78683 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3825f8b6-482c-3b73-98fd-a81af37f6206 | -19.93013 | -57.44754 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2f8017ff-8314-31c4-9adc-11ceb2eafd0c | -20.18653 | -52.38509 | 2025-11-30 05:40:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b30a90d-8ee2-3be6-b683-7cb9e9851ad6 | -19.86777 | -57.78425 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| bd661907-5a12-376b-a984-d3c61da7c135 | -19.84712 | -57.78165 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9f725792-e9ce-3eb8-b3f0-08c375db8b95 | -19.86812 | -57.78099 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 9fd00331-7158-38d7-a48a-999a4f2762d4 | -19.84264 | -57.77451 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 776e5b53-2a6a-3282-81ef-22de46971c50 | -19.85194 | -57.78555 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 18cd3fd4-048f-3507-ab24-17afd0b04b1a | -19.86743 | -57.78748 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 0d2669b6-4a65-344d-b5fb-c538a8d4d2ea | -20.17992 | -52.37717 | 2025-11-30 05:40:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16ce2915-5bab-3b8f-8351-c6228229b583 | -19.93049 | -57.44412 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 164fecf4-eeae-3de4-831d-62dc57e2f05a | -19.84434 | -57.75824 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b91838bb-ae63-3af6-8bb7-04950b4d4718 | -19.92485 | -57.44688 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 37e219e9-c178-384b-b5e0-1056ff1fe1ad | -19.84643 | -57.78813 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8ad5774a-f360-34e8-aa4e-f1493d3b0136 | -19.85125 | -57.79203 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 9064d1cc-22f0-3f5f-bfcc-26b06a32ee23 | -19.84298 | -57.77126 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 21c35380-5f5e-3ed0-b70f-2f795e162c3b | -19.08505 | -57.68974 | 2025-11-30 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 72b89bb6-25a2-3505-8407-05a80f107066 | -2.2088 | -47.99654 | 2025-11-30 06:07:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7921aaf1-420b-3743-a940-c98b56f6321a | -2.60551 | -47.33605 | 2025-11-30 06:07:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 833a623d-1e59-34a8-be67-72c9c8930e67 | -3.22916 | -45.52236 | 2025-11-30 06:07:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 70354287-b189-3e63-860d-bf935b5fe811 | -4.29077 | -45.34877 | 2025-11-30 06:07:00 | AQUA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6a03cd7f-d6f7-3ac2-b668-2bebab2f255f | -1.87897 | -47.91922 | 2025-11-30 06:07:00 | AQUA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7b4bea7c-0547-33a4-b0d2-239b317bfd4b | -2.51015 | -49.09652 | 2025-11-30 06:07:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0b9d8b8c-17cc-35c7-9830-2bc0df14e0c2 | -2.44029 | -47.07563 | 2025-11-30 06:07:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 266ffc0c-b19d-31a3-a4dd-7800d5687c38 | -2.50594 | -49.09987 | 2025-11-30 06:07:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 2d5da636-abe3-3ed7-90a7-16be5357a9b1 | -7.73716 | -44.1834 | 2025-11-30 06:07:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5ce95758-4395-337d-9fa8-0e086d0c7439 | -3.11236 | -45.19236 | 2025-11-30 06:07:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 54a2cddd-80e4-3ec6-aae3-23f3acfe94b5 | -2.64413 | -48.53798 | 2025-11-30 06:07:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 86918404-fbee-3f60-ade5-cad0f09b78fa | -2.64265 | -48.54772 | 2025-11-30 06:07:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| d6dd09ab-e24d-3351-bcd5-d221f4017fc2 | -2.63969 | -48.0243 | 2025-11-30 06:07:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 35b92430-ee86-3283-874b-7cfe3a9256ca | -4.36283 | -43.15201 | 2025-11-30 06:07:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7082b244-b0ac-324b-99d4-b7dd5a5a978d | -3.2278 | -45.53138 | 2025-11-30 06:07:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a2034c0f-db39-3bef-858f-136f50194ab5 | -3.62447 | -42.74793 | 2025-11-30 06:07:00 | AQUA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c246a89c-acde-3439-bf63-f1e151bbd07d | -2.6334 | -48.54633 | 2025-11-30 06:07:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 19a09acc-cbb9-322e-95a0-b3d0a2dbee20 | -2.63829 | -48.0336 | 2025-11-30 06:07:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1f4fc29b-75fa-3fa9-8d92-2befe949d4db | -2.70105 | -48.34863 | 2025-11-30 06:07:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 69b4b327-6f8d-3f85-9498-19c783f88070 | -12.00278 | -49.25395 | 2025-11-30 06:09:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 66ac34bb-3f29-394f-94d6-6f2015bc2904 | -12.0014 | -49.26297 | 2025-11-30 06:09:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 61fb830d-ed6e-373c-a769-c3f880fedff7 | -12.01332 | -49.26141 | 2025-11-30 06:09:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 2281981f-2ec1-3025-9d43-6c1d0220de42 | -16.75671 | -51.34639 | 2025-11-30 06:09:00 | AQUA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5d78b769-b274-31f6-b53b-17c081563074 | -16.79276 | -53.76272 | 2025-11-30 06:09:00 | AQUA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bc165f24-6740-3a7a-a72e-5560295c2c70 | -16.79047 | -53.77609 | 2025-11-30 06:09:00 | AQUA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f0656b25-b1c0-3d68-844f-b81efb95ef5b | -19.84878 | -57.79287 | 2025-11-30 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 5bbed001-a20d-3b46-ab18-54e4bfe1237e | -19.83997 | -57.76693 | 2025-11-30 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.6 |
| d5aaf839-172e-321c-a995-6c1b5d4c9e9b | -19.08503 | -48.58551 | 2025-11-30 06:12:00 | AQUA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 11a235d7-627f-3dd4-bb94-28aac1a4abed | -21.28952 | -48.56615 | 2025-11-30 06:12:00 | AQUA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 17c0cd6d-e42d-3d39-8285-4e796ccdbb71 | -17.51013 | -57.13401 | 2025-11-30 06:12:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 13af7fce-3c03-3052-a72a-d220c624cc42 | -3.0531 | -45.344 | 2025-11-30 06:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 91c0461c-b842-362a-a63c-00a59e1b09be | -3.0531 | -45.344 | 2025-11-30 06:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7570a8c1-f187-3fa5-b46f-3b861b3a4809 | -17.5148 | -57.1513 | 2025-11-30 11:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 1606d6b1-16fc-3614-9654-d1f425ba6d28 | -5.33128 | -40.3385 | 2025-11-30 11:57:00 | TERRA_M-M | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 18a03e77-5ba5-32ca-8d98-c7bf31c64d21 | -4.60461 | -45.20461 | 2025-11-30 11:57:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f4357b39-b051-3433-8c71-a9d40c2e8be8 | -8.69385 | -40.73413 | 2025-11-30 11:57:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 19.0 |
| a0bfb824-2e6d-3026-bb50-1b19c2facda4 | -3.50513 | -42.48307 | 2025-11-30 11:57:00 | TERRA_M-M | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 9f449800-ec28-30e7-8f38-9151f44605fe | -8.2388 | -36.55302 | 2025-11-30 11:57:00 | TERRA_M-M | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 123bc034-7384-341b-916e-38a3e0f92a13 | -3.51357 | -41.96756 | 2025-11-30 11:57:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 99229853-a987-3c80-a6b7-e2d4c89d0645 | -8.2412 | -36.53329 | 2025-11-30 11:57:00 | TERRA_M-M | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 36.3 |


[Clique aqui para ver as próximas entradas](README22.md)
