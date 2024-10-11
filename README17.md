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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b03c1b4-3894-38df-942b-70e716627b34 | -2.96575 | -48.00446 | 2024-10-11 00:56:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6831d697-b1a5-3fc8-aec6-a48f44defe1a | -2.96448 | -47.99532 | 2024-10-11 00:56:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49c5842b-7155-3512-8c75-3b2834e67dbb | -2.47699 | -48.06754 | 2024-10-11 00:56:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 74638355-8e67-324b-9a3c-1028bacaeb79 | -2.46015 | -47.81624 | 2024-10-11 00:56:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b07e8ad7-4303-3a93-b883-2073617149f3 | -2.4216 | -48.45879 | 2024-10-11 00:56:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8d91d5b5-8675-32b4-ae65-6b8aeea3a2fe | -2.42034 | -48.44986 | 2024-10-11 00:56:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b2d7b97b-8b6a-3e25-bd5a-f3602c06c54b | -4.38034 | -48.62186 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 93332c40-d0f6-3c13-b8e7-0148129962f4 | -4.31731 | -48.63668 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 6b14fad4-11cc-3cbf-9546-b25b8d833475 | -4.31608 | -48.62787 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2c0f1065-e3ee-3c6f-a0c8-c62c924f4b39 | -4.29082 | -48.64044 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fab1645e-3076-3e95-8aab-cd3187c056ec | -4.28959 | -48.63163 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| eba183bd-4d98-3318-a676-f98d4609e68f | -4.28836 | -48.62283 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b10c2814-407e-33ce-883d-d9a7e3f1f920 | -4.25423 | -48.65195 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 719cf7ed-aee2-3a96-8604-1b58aeff2288 | -4.253 | -48.64315 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5112fa4a-0f62-3081-99bd-fcc989fd7191 | -3.95572 | -48.94568 | 2024-10-11 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 0c17c447-2720-307b-9627-1f784c8a0406 | -3.9469 | -48.94693 | 2024-10-11 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 3e3b4a15-1af3-3728-833e-221282d467ff | -3.81191 | -48.97824 | 2024-10-11 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 492ee5f4-b852-33a5-ae73-32aec4b6382a | -4.48471 | -48.11615 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 222d6fd8-ef9f-3098-b855-2d689c7eb2b5 | -4.27815 | -48.22733 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 277fe98f-c71a-3441-9b31-f16977d82416 | -4.26927 | -48.22857 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 93b474d0-b524-3f03-a0d6-f0fcb9e7998b | -4.20222 | -48.13816 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f70df40e-f7bb-3f5f-b528-a4d8b2880fff | -4.20096 | -48.12922 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2db06e92-5e2b-30ca-9b2e-30670056362d | -4.11682 | -48.26254 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 479ac70e-0a5e-39bb-aa98-618b036a4729 | -4.11558 | -48.25366 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 620db32d-b451-3b9d-b2a8-9a14324bf6f6 | -4.11434 | -48.24476 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 655098e7-8ec0-34f5-b1ac-e9af7772bb09 | -4.10919 | -48.27266 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 9a8267af-f5ae-38aa-aefc-e989c86afbaf | -4.10795 | -48.26379 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 652b78df-e174-321b-aca4-5243c144df0e | -4.10671 | -48.25492 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 016bb363-c900-3531-9864-68bff9f9ba69 | -4.10546 | -48.24602 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 36c032d0-04a1-364d-b711-2878a3e65832 | -4.10032 | -48.27394 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 06dadb90-931e-3e82-91c1-09f329ceecc8 | -4.09907 | -48.26506 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 76f81e21-0639-3ee9-9add-882f613f036b | -4.09783 | -48.25618 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 55b061c0-71f7-3daa-a459-d39e212766d1 | -4.09659 | -48.24726 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 5e1f85e2-4047-3277-9de1-662aba8d0153 | -4.07884 | -48.24981 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dabe9f7e-ccd0-3f25-8ca1-8aa7496d4cd9 | -3.95417 | -47.95365 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ab1a568b-b830-310d-a14e-bb22e492aa7b | -3.91858 | -48.35728 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1f02de1d-5b7f-30a0-9e9b-80ebb9635d50 | -3.91733 | -48.3484 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 22463e54-3622-315a-a285-92aeafc6747d | -3.91609 | -48.33954 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0550a885-dea6-3910-acd7-c04bd8684caa | -3.90723 | -48.34081 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e3fd2de0-08ba-34dc-8183-d9e1e89df2a0 | -3.89198 | -48.36106 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 3d375d7d-154f-3d83-8eee-34c97f619cb9 | -3.80326 | -47.79592 | 2024-10-11 00:56:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5359de30-de82-3b48-9207-6cd00b870e59 | -5.06863 | -48.07767 | 2024-10-11 00:56:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3edb3933-2bbf-3378-957b-d08929223425 | -4.48345 | -48.10722 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 01b02c8b-ba87-3d17-8e5b-e9eb14f83458 | -3.95544 | -47.96269 | 2024-10-11 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7f000b40-bcfe-38e2-9772-cb078ab571d4 | -3.81225 | -47.79462 | 2024-10-11 00:56:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1e88f303-3273-3ae6-95c2-f56ffdbc8da8 | -3.80197 | -47.78677 | 2024-10-11 00:56:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2d6261dc-3fe8-3786-b0ea-8d65c9ae4217 | -5.06988 | -48.08656 | 2024-10-11 00:56:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6b713d0-8ff6-3df8-b58d-b5453892b49b | -5.06407 | -48.44564 | 2024-10-11 00:56:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| b26b9e49-8ebf-371b-826a-c171b9960916 | -4.97438 | -47.93318 | 2024-10-11 00:56:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2ba58fcd-8151-33bd-a69d-673784a08027 | -4.97313 | -47.92425 | 2024-10-11 00:56:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eca06c99-5442-3369-b469-1ee0e8ae9650 | -4.96604 | -49.065 | 2024-10-11 00:56:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| facf3747-7cae-389a-a2ac-6d507822778f | -4.83791 | -48.93652 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d8791bf8-c95a-36e9-a9c0-d42f7e48936d | -4.8214 | -48.22188 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 06b6e8ed-5520-33a9-a2c6-f96afbffb537 | -4.78764 | -48.89873 | 2024-10-11 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 07bef32a-a807-358f-9c36-5ba31312a52c | -5.78407 | -49.04817 | 2024-10-11 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 95ac4daa-0ab2-39ed-a1d6-87febd6f0a04 | -5.74909 | -49.25293 | 2024-10-11 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5022ac0d-7d8f-316a-8681-9d31b09bd57c | -5.53465 | -48.96905 | 2024-10-11 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7520b3cc-90e6-36ae-8871-d507daa2c82f | -5.53184 | -48.35128 | 2024-10-11 00:56:00 | TERRA_M-M | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a78f3bce-1573-36f7-ae0a-d74019625587 | -5.2417 | -48.4621 | 2024-10-11 00:56:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 0385cada-32d8-3306-b391-72f8adf67c3a | -5.24047 | -48.45328 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 8ee7a07f-371f-3562-a109-146c0960d917 | -5.17282 | -48.29176 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2773a915-bad7-3eb9-8597-3cad6b81ddd4 | -5.17158 | -48.28291 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 4ac316f4-0fd2-3492-adf4-45e432dd2ee5 | -5.17034 | -48.27406 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f1d6e7c6-f4a7-3e16-ad93-f71dfb58e829 | -7.73595 | -49.03093 | 2024-10-11 00:56:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bebf9345-1bab-3a45-aa8b-dab407b9bb93 | -7.6886 | -49.83555 | 2024-10-11 00:56:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 6e9d4d1b-e146-3d81-8e34-9d25c42af24b | -7.67943 | -49.83683 | 2024-10-11 00:56:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dbd2d92c-6a7e-36aa-9254-eab16ab89154 | -7.60288 | -49.40687 | 2024-10-11 00:56:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b012e690-2c58-3379-bee2-9e24cfbf4bf8 | -7.60163 | -49.39766 | 2024-10-11 00:56:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 062e2091-4f35-3262-9df6-eb2e8677815d | -7.58909 | -49.57572 | 2024-10-11 00:56:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5a672739-546e-3d77-a785-f087e8f878f1 | -7.4048 | -49.64222 | 2024-10-11 00:56:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5996c203-76e9-3b24-92cd-2136bb3afd6e | -7.33425 | -48.59158 | 2024-10-11 00:56:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 130b67bf-4487-3a74-8c56-e32379203cf8 | -7.23621 | -49.35139 | 2024-10-11 00:56:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 620783ff-740b-3191-b4a5-dcfab6a9b6b6 | -7.11692 | -49.15155 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ec5f67f2-e4b2-386a-8941-ff86f3c0f185 | -7.0345 | -48.55289 | 2024-10-11 00:56:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4c125cdc-9a2c-3926-95d4-513a7b4dadb7 | -7.03327 | -48.54402 | 2024-10-11 00:56:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 78d9a605-06f7-3a17-a45c-cd17893e4c31 | -7.00434 | -48.54543 | 2024-10-11 00:56:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 65eb3595-80ba-37ac-a848-f6b2c544e832 | -6.77831 | -49.10427 | 2024-10-11 00:56:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8216d176-20ac-321e-9ed2-be3114399f00 | -8.8342 | -50.0735 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b953bfec-d492-3045-b787-d7a35bf72ca2 | -8.78768 | -49.79696 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8b68bf23-dd50-307d-962f-8c28164eb493 | -8.78637 | -49.78716 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 058168e1-3e54-3892-ab94-d57eb74336fd | -8.78058 | -48.86222 | 2024-10-11 00:56:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b564fd00-237c-3b32-b75a-5933cb0752f5 | -8.77164 | -48.86348 | 2024-10-11 00:56:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d0804e23-11af-39f7-8d0a-dad1729545c0 | -8.77039 | -48.85437 | 2024-10-11 00:56:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ecba82f-4792-3726-a9cf-9959799918dd | -8.70461 | -50.00547 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a1572be2-af68-31d2-b67a-74b724768ed8 | -8.70329 | -49.99552 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 95603204-986f-3e48-a7e0-2708c8eabbfc | -8.70197 | -49.98557 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 17faba1d-bd84-3432-bcee-57c0ba04cfe5 | -8.69396 | -49.99679 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4804d3ba-c5bb-39d0-9d07-3ed103ebf6ff | -8.62704 | -50.04277 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0f208fd7-f0a5-30e8-86b7-28a50c411bae | -8.58863 | -48.93866 | 2024-10-11 00:56:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 184e75c1-d124-3de0-b209-9f61d3d45901 | -8.58739 | -48.92954 | 2024-10-11 00:56:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3c310167-8d8b-37ba-b279-ce8987050454 | -8.44032 | -48.66147 | 2024-10-11 00:56:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8cb25a47-8be7-371a-bec6-27b4cfefc810 | -8.38262 | -48.64795 | 2024-10-11 00:56:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b3702187-dd53-3094-b106-8b74f93142f2 | -10.32802 | -50.56411 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b90b5dcc-c585-3df1-b861-28451811e55d | -9.77014 | -50.12344 | 2024-10-11 00:56:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 877aead7-30a4-3b1c-9659-5ed039b6f076 | -9.67245 | -48.91843 | 2024-10-11 00:56:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9ba3197b-dd88-31d3-b6a9-f2037fab9224 | -9.62778 | -48.99731 | 2024-10-11 00:56:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f2928cdf-06d3-38b1-a40e-baf33c3ae92d | -9.62651 | -48.98801 | 2024-10-11 00:56:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 156186a5-f9e8-38cb-adbd-7f7b28508989 | -10.47808 | -49.98823 | 2024-10-11 00:56:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 58557b69-fa67-3fbd-8588-89e13e3c5b7d | -10.47671 | -49.97781 | 2024-10-11 00:56:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 51362a1e-c9a2-3dc4-a428-441487677a6f | -10.46721 | -49.97912 | 2024-10-11 00:56:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |


[Clique aqui para ver as próximas entradas](README18.md)
