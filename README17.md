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
| a44b1dc0-e1d2-3c2e-b048-4eddbda77295 | -3.8655 | -54.34985 | 2025-12-11 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b254f67b-f3cc-3408-a0a9-17f51a775678 | 1.95971 | -60.56846 | 2025-12-11 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17264db3-f775-3216-b2b0-9b0cff29b102 | -3.69921 | -50.94783 | 2025-12-11 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ac2ddd-1cc1-3f36-9465-07adcc40949f | 1.76621 | -60.52887 | 2025-12-11 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ccd1d57-c7b5-3de2-8a1f-52e21d9f1378 | -3.61599 | -55.46575 | 2025-12-11 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58ec521c-9ca6-350d-93b5-58c28e5e40c1 | -3.49101 | -51.53817 | 2025-12-11 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5eb6dccb-65b7-3a58-aa9a-c90bc99bf66c | -2.59682 | -53.98383 | 2025-12-11 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4039deb6-667b-3bf2-8e03-8944ad9890b5 | -2.65954 | -51.6421 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4207c155-8618-3239-aef8-354b80cfa668 | 0.96472 | -60.60172 | 2025-12-11 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17d77894-764b-3be9-a8a9-905743345720 | -2.69331 | -51.64368 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48f1c20e-898c-361e-9da1-d5dc17f6208c | -3.75389 | -51.83406 | 2025-12-11 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7864212c-ce9e-3c3a-a664-dbeed5ef4b0b | -1.58578 | -53.7587 | 2025-12-11 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a5d4f92-40db-3f16-b6f4-27f79676f0fd | -1.74652 | -54.59636 | 2025-12-11 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fab9b409-dbca-3a72-93ff-427c70fbb9d1 | -2.94143 | -53.0301 | 2025-12-11 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84f74a23-fdfc-354f-b8ec-e753cd345f68 | -0.64467 | -52.3913 | 2025-12-11 05:29:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1d3f3e9-0821-3465-b420-5c23962ba77e | -2.20995 | -51.89351 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f00a5613-77e9-3edd-ab38-4d0c4be46598 | 3.03031 | -60.14645 | 2025-12-11 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef84dd74-0e26-3cf4-8cf1-2e3d0dd227c2 | -2.02135 | -52.04669 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e53257d6-8458-3478-8ebe-6aea7311f969 | -1.48141 | -54.20161 | 2025-12-11 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 86e94cb1-4ed3-37b3-9258-27eb8c3cc300 | -1.11422 | -53.69087 | 2025-12-11 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 05723b8d-ca6a-38ee-9e96-6befdce31205 | -1.01922 | -53.73044 | 2025-12-11 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e5b5123-bfdd-3dfb-b0d7-949edfc44188 | -8.59816 | -63.28313 | 2025-12-11 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f528384-9fb0-315b-9b7f-6e84501a31cc | -2.94187 | -53.02721 | 2025-12-11 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a58f9be-5aeb-3f1c-a4db-8c632c104a77 | -1.1103 | -53.68516 | 2025-12-11 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b3ec895-7873-38f8-9b04-cbe16f1a6555 | -2.47537 | -56.04829 | 2025-12-11 05:29:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 611a4197-79aa-30f5-9829-992adc0b1a5d | -3.32954 | -52.8191 | 2025-12-11 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae153161-da74-31de-af30-a103fbd3ea08 | -3.7403 | -45.4952 | 2025-12-11 05:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 75479ff9-d9b0-3318-88fc-b89c5a0cb063 | -3.7589 | -45.4944 | 2025-12-11 05:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 0a1e68dd-1360-374a-a153-dbf61a9f975e | -6.56069 | -56.1334 | 2025-12-11 05:31:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 755764bb-195a-3645-b8bc-81846a8070b5 | -12.44697 | -63.63809 | 2025-12-11 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d62b3b4-776d-3192-af86-ed6c4d77385b | -12.19754 | -63.49283 | 2025-12-11 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 036191ec-ce14-3f8a-815b-98798fb8ec63 | -11.45864 | -54.30238 | 2025-12-11 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16a5e006-59b9-3427-b45e-03c1e041c8a6 | -16.30896 | -53.82701 | 2025-12-11 05:31:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd3078c0-7145-3a2c-a969-3f97f2e52da4 | -11.75049 | -61.73005 | 2025-12-11 05:31:00 | NOAA-21 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f0282fb-6c60-33cf-88ca-30fb2e28ed86 | -12.44421 | -63.63403 | 2025-12-11 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2ae016d-64d6-3985-96bf-8cb49f97f98d | -12.19368 | -63.49581 | 2025-12-11 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f20463fd-f0c2-3a21-94f6-625b430adebd | -14.07877 | -56.1654 | 2025-12-11 05:31:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc8f860c-86eb-34ab-a367-7efaac2197e1 | -11.45883 | -54.30316 | 2025-12-11 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09aa7501-df55-37ee-bb03-91ebf6ddd870 | -16.30993 | -53.82582 | 2025-12-11 05:31:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4cdff20-a0c1-383b-96ee-98b861f2ca4a | -12.44752 | -63.63457 | 2025-12-11 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eae2c56b-32d2-3567-b506-990c54485b86 | -12.45083 | -63.63511 | 2025-12-11 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bba2fff-7ae9-3ce2-8e92-cb5bd899a27a | -22.02482 | -56.34173 | 2025-12-11 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88983165-5988-3fbc-bc54-f1b2f1a202fa | -22.02515 | -56.33828 | 2025-12-11 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87ec4f95-f96a-3c94-96fd-ba4a5dc9b8f6 | -3.7589 | -45.4944 | 2025-12-11 05:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 5e4311d3-31c2-3e6b-ad52-164b4baad519 | -3.7403 | -45.4952 | 2025-12-11 05:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1e3d97f4-d27c-3e6c-871c-c806e3ab8fb1 | -2.2906 | -45.5933 | 2025-12-11 05:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| e824bfdf-fe93-35a1-815d-be46c737ba20 | -3.7403 | -45.4952 | 2025-12-11 05:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 0faa341c-1da3-3d4d-9b3a-07c86a7ae941 | -3.7589 | -45.4944 | 2025-12-11 05:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 4e12e7cf-feff-37c1-b5a9-ab56c68b468f | 3.03152 | -60.16683 | 2025-12-11 05:57:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 062b42bc-f151-3fbb-892c-c7722c8bafc6 | 3.03082 | -60.16259 | 2025-12-11 05:57:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc4fd2d6-8df0-3eb3-b3cf-b03c2e0a83f9 | 3.03011 | -60.15833 | 2025-12-11 05:57:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 779b634d-3f2f-3555-aa35-a2fd95f38148 | 0.45834 | -60.42701 | 2025-12-11 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cc97d726-8082-3eda-bac3-de4d85e69eac | 1.12613 | -60.52629 | 2025-12-11 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc9affdb-97ca-3972-8c6a-f4815923563b | -11.17529 | -65.04872 | 2025-12-11 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b57ff1d-fcea-3103-a571-effc6aa1b6b8 | -1.11538 | -53.68939 | 2025-12-11 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 16105643-528b-37ad-b054-e3e9a596d0b4 | 0.4607 | -60.42557 | 2025-12-11 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| df99c89d-b19b-3799-8172-c06fe5d55030 | 0.96346 | -60.60184 | 2025-12-11 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 349d5afd-0519-3c23-9cd6-1865837ab90b | -1.80927 | -54.0587 | 2025-12-11 05:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f3fd8c8a-6b3e-33fa-8dd0-6c428f7129cf | -1.48482 | -54.20327 | 2025-12-11 05:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40383958-6820-3001-b077-a7f091dd1efd | 0.23757 | -60.61007 | 2025-12-11 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46407aac-c386-3a16-93b4-b657d2a32e3c | -1.58644 | -53.76141 | 2025-12-11 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36b268d4-a2a6-38b9-9a8b-c7c6522f05fb | -1.80722 | -54.05734 | 2025-12-11 05:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a33f3d5a-d50e-3de4-b9ca-af3fa69bff91 | -1.59366 | -53.762 | 2025-12-11 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fed5e99-5d41-3cf3-9f30-6f77bd43a94a | 0.45621 | -60.42627 | 2025-12-11 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 675673ec-17f0-347b-861e-5272a3ec5734 | -1.11105 | -53.68697 | 2025-12-11 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c90d8c64-98c3-3990-86d6-c0cfad25811e | -1.48262 | -54.20602 | 2025-12-11 05:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77df3485-06cd-3b24-9ce0-3fd13dd10649 | -1.47783 | -54.20242 | 2025-12-11 05:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5361ac9-c001-37a2-983d-053110d0dc9a | -1.11819 | -53.68802 | 2025-12-11 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b8d2b0b-88f7-3587-8eb5-8d7c940299dc | -3.7588 | -45.5168 | 2025-12-11 06:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 091c0bae-218c-3370-9b23-640820383a89 | -3.7589 | -45.4944 | 2025-12-11 06:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 0b96389c-52be-39a8-9198-1eb6e6cf32d7 | -2.2906 | -45.5933 | 2025-12-11 06:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 42.1 |
| e1e0450e-a637-3a1f-8315-d6ceda39a78b | -3.7403 | -45.4952 | 2025-12-11 06:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 197ed67c-5192-370d-b03c-89b8dfbedefa | -12.44979 | -63.63422 | 2025-12-11 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b24412f-4b65-38b6-afd8-edc14fe8afe7 | -12.44541 | -63.6336 | 2025-12-11 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4561baed-7a1a-3e19-9476-476f579cb39d | -12.44482 | -63.63791 | 2025-12-11 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9619c925-22a1-31d1-864d-62db798f0c39 | -3.7403 | -45.4952 | 2025-12-11 06:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 99.2 |
| b7807378-0abe-3cbd-a484-156427f35ed8 | -3.7589 | -45.4944 | 2025-12-11 06:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 559f3e32-9749-3d39-8205-c1b26ae3a618 | -2.2906 | -45.5933 | 2025-12-11 06:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f368d0d1-da2d-3c55-9c53-a3fee9361e4d | 3.03004 | -60.16886 | 2025-12-11 06:18:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a7bcfff1-606d-35d5-9617-587f1836d5b2 | 3.0322 | -60.16354 | 2025-12-11 06:18:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5827795c-21c6-311c-8c56-65fa89ad4363 | 3.03567 | -60.16193 | 2025-12-11 06:18:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43e9f310-e480-3a47-be58-9ee36b657988 | 0.46162 | -60.43237 | 2025-12-11 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 944c8854-e1cd-3ba3-aed4-bd6d1c55767a | 3.03318 | -60.16934 | 2025-12-11 06:18:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f97934d2-da34-3839-b1ac-569ebc371018 | 0.46062 | -60.42626 | 2025-12-11 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cf03ee3-2b03-3ff2-a44d-3466d056af4a | -3.7402 | -45.5177 | 2025-12-11 06:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| cc6bc9d9-753c-37b2-8f1d-d41cd3da4fb6 | -3.759 | -45.4719 | 2025-12-11 06:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| bd1e31fa-2aaf-39c4-83d5-32726e9de270 | -2.2906 | -45.5933 | 2025-12-11 06:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 12530389-6c34-3585-acbc-e4352a45b155 | -3.7589 | -45.4944 | 2025-12-11 06:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 23f56f41-6470-3b1e-8b70-cc1d1ff2b2c3 | -3.7588 | -45.5168 | 2025-12-11 06:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 1f40ec64-8e97-331c-a6e6-c4f224291a97 | -3.7403 | -45.4952 | 2025-12-11 06:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 193.8 |
| 210471d0-e4d3-3c35-a19f-0b794a147ec5 | -3.7404 | -45.4728 | 2025-12-11 06:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 669d00e2-c2cf-3f7a-948d-16bd5a4d7fec | -2.272 | -45.5938 | 2025-12-11 06:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 3ad91775-5d0d-39ee-93cc-5b8264ec26a6 | -3.7402 | -45.5177 | 2025-12-11 06:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 20d9684e-2c1d-3fcc-b8a6-f1a03e2029ed | -2.272 | -45.5938 | 2025-12-11 06:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2408bca0-da95-3c9b-b71b-43fc4f755ec6 | -3.7589 | -45.4944 | 2025-12-11 06:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 359.4 |
| 0ebb8c7f-9221-3cb1-9be1-e14c2c7c95e0 | -3.7588 | -45.5168 | 2025-12-11 06:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 91.5 |
| da5edeb8-a365-3a9c-ae56-ade48e722256 | -3.7403 | -45.4952 | 2025-12-11 06:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 349.4 |
| ee91cec6-4605-363b-a82d-71b56f48b2f4 | -3.7404 | -45.4728 | 2025-12-11 06:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9b6cc3d6-94e3-3f6a-8f21-9fafee456a2a | -2.2906 | -45.5933 | 2025-12-11 06:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b24f2d01-9ca7-3841-907b-f52bdcc2c476 | -3.759 | -45.4719 | 2025-12-11 06:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |


[Clique aqui para ver as próximas entradas](README18.md)
