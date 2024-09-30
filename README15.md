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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5003f494-8fa0-36a2-a2b1-9d1bd72b8d94 | -14.8846 | -58.00551 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f22e68fd-8a89-3193-96d7-a2c6e9996d44 | -14.88322 | -57.99597 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 79f93bfa-bcde-3c9b-9aa7-bf4208d4a9ae | -14.77738 | -58.22469 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 2f3b8639-771f-3579-84ed-ba232ed724d9 | -14.77606 | -58.21542 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a7efbe01-50ed-32a9-9674-07adbc418382 | -14.76846 | -58.22606 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2400a304-9c52-35a4-8973-99b914e3b81e | -14.76714 | -58.2168 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a31db0e1-dd11-3040-9d80-999694b191d9 | -13.51717 | -59.54079 | 2024-09-30 01:45:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0da4bcaf-6f30-3f43-8b1b-86d91291e8b6 | -12.69196 | -54.67367 | 2024-09-30 01:45:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f393f49c-60f0-3dba-bdb6-af36018cc82c | -12.66324 | -54.70953 | 2024-09-30 01:45:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 968bf188-cad8-38f9-b16d-5a90f5a2b4cd | -12.64974 | -54.69641 | 2024-09-30 01:45:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c08986af-ee75-31b0-9194-9eba744228fa | -14.93296 | -57.95928 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 13626bf1-2bef-3f6e-9a95-744af433da43 | -14.93163 | -57.94994 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 76e8c7eb-5569-3c71-80ec-7e3e866a6ad2 | -14.9074 | -57.97289 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4408bc04-8038-38dd-b81b-063a21c1046a | -14.90605 | -57.9635 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 38e6ac2f-5186-3796-8c7c-118965336628 | -14.89356 | -58.00412 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d744a315-bade-338e-a60a-2bed4e0fceff | -14.89219 | -57.99466 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| dfa692cb-1e3b-308c-b0c8-30356590e217 | -12.57525 | -53.50414 | 2024-09-30 01:45:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 9761b077-8aac-33d2-bbf7-4ff2ad9338c7 | -12.25689 | -59.23281 | 2024-09-30 01:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1f63aef-65f6-310b-8e51-4c0ffea40d9a | -12.2228 | -58.91669 | 2024-09-30 01:45:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 96c83c98-b0e4-33fd-a225-94aed6e6f864 | -11.85467 | -58.99366 | 2024-09-30 01:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba246219-7c1e-3382-9669-32480b995de3 | -11.85348 | -59.04958 | 2024-09-30 01:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 893c708a-fe1a-352a-b668-6007d89ed60e | -11.84963 | -59.02232 | 2024-09-30 01:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2b5397a5-e570-3a25-a9ae-d0923fa4325f | -11.84901 | -56.87664 | 2024-09-30 01:45:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ee0176d6-d014-3917-a1b6-80351ad275d0 | -11.7681 | -59.2899 | 2024-09-30 01:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd3a19c2-e943-368c-9caf-273f4df84e67 | -11.76683 | -59.28088 | 2024-09-30 01:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 57e346ea-4943-38ae-9702-aaed11d3e524 | -11.68482 | -58.89457 | 2024-09-30 01:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2a1e5e03-f4e6-3497-b071-49cbe524bf8a | -10.73243 | -57.5549 | 2024-09-30 01:47:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ea760be7-5c26-36cc-90f4-d3f1940e31da | -10.69299 | -58.53697 | 2024-09-30 01:47:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e6c4aee6-0482-38f6-9b38-b179f774555b | -10.69163 | -58.52758 | 2024-09-30 01:47:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 92e2d89f-9097-3e5d-b9c8-a4a155b5fd9a | -10.68246 | -58.52569 | 2024-09-30 01:47:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8bf0c50f-a7c7-39a7-b447-5091f8830cae | -10.51861 | -57.78403 | 2024-09-30 01:47:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 169de101-5a3c-3b33-bec8-5cba0e0cd5cc | -10.51712 | -57.7739 | 2024-09-30 01:47:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70c3d67d-956c-3d47-b33c-01884b37a4b1 | -9.70707 | -62.17953 | 2024-09-30 01:47:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f63ae371-78f1-321c-a8ff-39b28a5a4e80 | -9.69521 | -62.30376 | 2024-09-30 01:47:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6767fe54-cd6d-350a-9767-872dc58e757a | -9.08642 | -61.13943 | 2024-09-30 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d1314329-6d32-3c43-8f84-38a72982f6a3 | -9.05662 | -62.34246 | 2024-09-30 01:47:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6e0e7331-807f-3033-ad3a-61fb86015b6e | -9.05528 | -62.3325 | 2024-09-30 01:47:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9664718c-7195-384f-8a19-3d5d79d8d751 | -8.83928 | -61.82137 | 2024-09-30 01:47:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 87717aa3-e83e-3921-a693-da99ec573b40 | -8.48024 | -62.7015 | 2024-09-30 01:47:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 70af49e9-945a-3bfd-b245-263ff78c34e6 | -8.47079 | -62.70283 | 2024-09-30 01:47:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 12ed9cbc-4610-310a-99c2-590f103a1e99 | -3.12745 | -53.74848 | 2024-09-30 01:47:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| e0d4abdb-1cdc-31a8-8d38-d3415073dda6 | -3.12365 | -53.72297 | 2024-09-30 01:47:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 586ad003-f894-3d7d-96a5-12d0f24c2867 | -3.08847 | -53.08166 | 2024-09-30 01:47:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| f4dbab20-6ab3-3a20-b043-a6960ea34949 | -3.08399 | -53.05225 | 2024-09-30 01:47:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 8edd123a-cf0c-3d42-a356-117ec1048485 | -2.97241 | -54.74026 | 2024-09-30 01:47:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 967d8f88-17bc-32bc-a149-b4992f5d7b24 | -2.13975 | -53.66196 | 2024-09-30 01:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 533befec-ff80-33a0-bdf2-5e082fbb3626 | -2.13912 | -53.66765 | 2024-09-30 01:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 2518ec71-4786-3a28-99dd-4e1645cd8eae | -21.667 | -54.812199 | 2024-09-30 02:04:14 | METOP-C | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6fde19b5-156b-3b65-a4fc-54a378e25001 | -21.6733 | -54.834099 | 2024-09-30 02:04:14 | METOP-C | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e220441a-c60e-399d-845c-3f2bf1842939 | -21.657499 | -54.8153 | 2024-09-30 02:04:14 | METOP-C | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f279ba52-35eb-3348-9ab5-8765028d2c6c | -21.663799 | -54.8372 | 2024-09-30 02:04:14 | METOP-C | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b6229b8e-e0f9-35f9-8255-c553aa96ae24 | -21.6479 | -54.818501 | 2024-09-30 02:04:14 | METOP-C | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9874599c-f6c6-3fb6-9ba8-698e16112bbf | -21.6542 | -54.840401 | 2024-09-30 02:04:14 | METOP-C | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 581b5414-1db9-3853-b23c-a7cf3c327615 | -17.147499 | -56.212601 | 2024-09-30 02:05:33 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d151b615-744a-34a6-8bad-fc7c7f7b5cf2 | -17.1259 | -56.172401 | 2024-09-30 02:05:33 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6bab5682-7c62-30c9-8956-0e627fc172df | -17.131901 | -56.194 | 2024-09-30 02:05:33 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 057cc87d-1756-3708-8f16-724f4a434e1e | -17.137899 | -56.2155 | 2024-09-30 02:05:33 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 09a0aa80-df6c-3a2b-a5d1-b612c321e3ab | -17.1103 | -56.1535 | 2024-09-30 02:05:33 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b96653e1-dc0f-360a-81d9-272d07f6c59f | -17.116301 | -56.175201 | 2024-09-30 02:05:33 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a00363d-d833-33ce-91bc-872aaa0f6b88 | -17.122299 | -56.1968 | 2024-09-30 02:05:33 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b419a080-ad76-3ad0-b1f5-4a15550cc7d0 | -17.1283 | -56.2183 | 2024-09-30 02:05:33 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c46ae905-dc35-3418-99b0-6ac6abeee68f | -17.112801 | -56.199699 | 2024-09-30 02:05:33 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6245d356-1b1f-3569-92ad-1ab7c5faf5b6 | -16.998899 | -56.163601 | 2024-09-30 02:05:35 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5a6dfbc6-cdc0-3ff0-962b-5dea89ad0091 | -17.0569 | -56.7113 | 2024-09-30 02:05:36 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fefe53ed-3ec2-38e6-8a8e-55bccc5101a5 | -17.062401 | -56.7313 | 2024-09-30 02:05:36 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 04c7a9e3-9126-37bb-bbc5-0c062f36821f | -17.0679 | -56.751202 | 2024-09-30 02:05:36 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 677e6f8d-10eb-30fe-b58f-c50eaa677fe6 | -17.0473 | -56.7141 | 2024-09-30 02:05:37 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 63a9ff62-9861-3a89-8295-dfd0e5037867 | -17.052799 | -56.7341 | 2024-09-30 02:05:37 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89379ec2-c8c2-340c-80ac-d0950fab17a1 | -17.0583 | -56.754101 | 2024-09-30 02:05:37 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea1c98ea-a693-3bd3-9f41-f33128f32efe | -17.037701 | -56.716999 | 2024-09-30 02:05:37 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a8d3d9e-c951-39f5-be31-0ae88b06ef12 | -17.0432 | -56.737 | 2024-09-30 02:05:37 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a958008-5746-3c3a-893c-20cfce5f94db | -17.0487 | -56.756901 | 2024-09-30 02:05:37 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f92af7e-bd4c-3ef4-8fc4-4a8a89262a7b | -16.5958 | -55.946201 | 2024-09-30 02:05:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9759d37-3ce2-35e2-a87e-90292efb3f8f | -16.6022 | -55.969002 | 2024-09-30 02:05:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1628c500-ebbe-3104-833d-f6bb64384845 | -16.586201 | -55.9491 | 2024-09-30 02:05:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 197cf4b3-113b-37e1-a75c-b442979cd59a | -16.5926 | -55.971901 | 2024-09-30 02:05:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41dc1a7f-daed-324c-8324-15329a2d304b | -16.993 | -57.9688 | 2024-09-30 02:05:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6ce32b6-91c8-37b5-920d-27c4cd6e98b8 | -16.983299 | -57.9716 | 2024-09-30 02:05:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 80998987-aceb-3fa9-b3eb-89b7277590a7 | -16.9877 | -57.988201 | 2024-09-30 02:05:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b1a068b-75f3-3dce-a5db-a7df223574c8 | -16.9737 | -57.9744 | 2024-09-30 02:05:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b4f277e-83c8-3695-9c8a-9c174b2aba1c | -16.9781 | -57.991001 | 2024-09-30 02:05:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb05f761-b7d0-3c8a-b097-20b659f5bb6c | -16.9825 | -58.007599 | 2024-09-30 02:05:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eab357d7-f7bb-3423-a313-c5dfa4f12b63 | -16.9641 | -57.9772 | 2024-09-30 02:05:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d43e97a-ad46-3fd6-b634-116b821fbb45 | -16.9685 | -57.993801 | 2024-09-30 02:05:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa0c4c76-04bf-36a7-8cc0-b53f4129571f | -16.9729 | -58.010399 | 2024-09-30 02:05:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9c50347-92a5-3d51-a38d-c5f7dd331775 | -16.8575 | -57.6964 | 2024-09-30 02:05:44 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d37c9fa-3dcd-332f-9f7e-fd3f87e0f767 | -16.708599 | -57.452 | 2024-09-30 02:05:45 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00fbe24f-4427-3b89-b18c-705326eb609a | -16.713499 | -57.4702 | 2024-09-30 02:05:45 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11ba572b-b98f-3e9d-adab-acca479f6af3 | -16.708401 | -57.4128 | 2024-09-30 02:05:45 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 656b7313-728c-377f-b60f-751442ea6cf7 | -16.698799 | -57.4156 | 2024-09-30 02:05:45 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 50dcedb1-91fd-3757-8975-3f546b12d138 | -16.703699 | -57.4338 | 2024-09-30 02:05:45 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f74b771-1cbe-31fd-8f9f-e4dfc6060429 | -16.704 | -57.511902 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4159bdd0-0075-3f5c-9337-32b409c296a6 | -16.708799 | -57.5298 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f754c8b8-d78f-367c-afb8-3c016913d0fb | -16.7752 | -57.776199 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 87370397-8534-30d5-ad92-3d2b70093846 | -16.7798 | -57.793499 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4245cec-4f72-37ca-8361-0da096dec9c5 | -16.674801 | -57.4422 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b1d7ebb-eb5c-3820-8ba0-725d53eaffe6 | -16.679701 | -57.4604 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c987f6fa-4d19-3c4e-bd8e-c0840e086644 | -16.7656 | -57.778999 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0eb6b580-4e1e-31a5-a44f-9ee14f367a4f | -16.770201 | -57.796299 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d1b98033-70aa-3603-bd14-27465660cb2d | -16.774799 | -57.8134 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README16.md)
