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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cefab94c-8cf8-332c-97ab-b731765a1605 | -9.28987 | -48.58312 | 2026-06-02 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd0bf77e-cd06-3667-91ba-bc36e6dca6ba | -7.50821 | -55.00418 | 2026-06-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75cce1bf-a8c5-3a11-8d83-f69522a19eb0 | -7.50622 | -55.00586 | 2026-06-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3702532e-4583-3a7f-a434-e03ebac755ba | -10.74974 | -46.90358 | 2026-06-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7770220b-7edc-311f-a46b-98b00084e173 | -9.07218 | -46.5303 | 2026-06-02 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2588f54-2d43-39c5-adcd-2442c67e8ea5 | -9.92901 | -48.68865 | 2026-06-02 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cebb95e-359e-3fef-8a8f-7b083ca74936 | -6.61017 | -47.5405 | 2026-06-02 04:46:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 85a4c562-b3b6-37e7-91a9-a3b5c2bb51e5 | -9.13624 | -46.92689 | 2026-06-02 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a8a91d1-daa0-3ddb-b818-c0546456dacc | -6.29884 | -43.64355 | 2026-06-02 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4208305d-4845-34b7-b5f9-5562b7704d69 | -6.30352 | -43.64423 | 2026-06-02 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cecdd65-660f-38e1-9694-6dd2e806865b | -6.39368 | -44.17448 | 2026-06-02 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38420277-f5fb-383a-bdc1-a79fc42d8d4e | -7.60511 | -45.55626 | 2026-06-02 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0b9ca53-eeb9-3936-8140-6e1c9cc38e2d | -8.98108 | -47.97692 | 2026-06-02 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a9986cc-93e0-355b-bada-79058e26b68d | -9.19297 | -58.05318 | 2026-06-02 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16471d01-ccd1-3342-bd09-b62905328199 | -10.0371 | -51.67843 | 2026-06-02 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 774643ab-187f-37fa-83cc-446cc2cf9245 | -11.48288 | -46.76725 | 2026-06-02 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a1eda3c-1e9a-3c32-b0ad-b44e3fd2dde5 | -7.83799 | -55.40253 | 2026-06-02 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5319dca-0ecb-3379-bb9d-7e4304716e62 | -8.98045 | -47.98127 | 2026-06-02 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8f4432aa-aa41-3470-82db-1ea281044d09 | -6.30119 | -43.64266 | 2026-06-02 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8077e764-862d-3a87-8bcd-724ed3137fde | -9.88665 | -52.44115 | 2026-06-02 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c579410c-591f-330c-8e6d-7a56b8826189 | -6.76017 | -45.03108 | 2026-06-02 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8eae612-e214-3c7b-b548-6dffe854b9bf | -9.12903 | -47.65189 | 2026-06-02 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4cb5f43-d39d-3140-9aa5-5bb9b9cb4cb3 | -6.06882 | -42.5127 | 2026-06-02 04:46:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c7399e30-1ff1-3df9-b6da-8fde5d4ef059 | -10.49654 | -52.13449 | 2026-06-02 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1582dd5d-e4f4-3846-b6d8-352690129dd1 | -5.51927 | -37.48423 | 2026-06-02 04:46:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bab8c12a-6095-3063-ada8-0a8674b79309 | -6.39885 | -44.17055 | 2026-06-02 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5eb3b94-dc8f-3d90-a144-e8fcfe4bb870 | -10.97991 | -45.09361 | 2026-06-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dcfeb791-1ecf-3b80-a072-467d64aebf63 | -9.13696 | -46.92182 | 2026-06-02 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32f18dd6-78e5-3428-a57f-bab6e0891a76 | -8.70224 | -49.08407 | 2026-06-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 768376c9-b262-333e-9d4a-3acd37d1de9b | -6.39433 | -44.16991 | 2026-06-02 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ab9873f-a65f-39df-882c-c387c6a7993b | -8.69355 | -49.0709 | 2026-06-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26cda1b5-649f-378b-92b3-f1fc9649e1a1 | -8.6982 | -49.0874 | 2026-06-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15b32ad3-e9d5-3372-8a17-736d690a26b6 | -11.58684 | -47.4501 | 2026-06-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dc927dc-39d0-3b4f-946f-edf97873a849 | -7.50322 | -55.00076 | 2026-06-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9291a37a-7107-392f-b6a0-c54e217ddcf1 | -9.12265 | -47.95627 | 2026-06-02 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e40719a1-3d2a-3a6f-a203-6e101499d2f7 | -11.34688 | -47.18744 | 2026-06-02 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0efed4d2-d56e-3829-ae6e-6380e7700c60 | -11.59612 | -47.44106 | 2026-06-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe119f17-4e33-3e8a-99a8-4f63dbaa15a8 | -6.76878 | -45.02235 | 2026-06-02 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b9c2086-7f0f-3534-b726-2d82a5c80314 | -11.59931 | -47.44667 | 2026-06-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3db05fab-dd06-3789-8196-cad654ea167f | -6.3042 | -43.63926 | 2026-06-02 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b86496d7-b105-3d8d-ae61-ab45b6bf07b6 | -11.79487 | -47.33755 | 2026-06-02 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 056dc5a0-e8ae-36d2-a11a-baa5b46e217b | -5.52617 | -37.48523 | 2026-06-02 04:46:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9e9a0a48-8ea2-38c7-9537-2b79ca1150f4 | -6.99927 | -43.86924 | 2026-06-02 04:46:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 401dd554-0a1e-3056-9b50-45a328d04714 | -9.122 | -47.96066 | 2026-06-02 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5e0df97-3144-3343-97b3-fee865596115 | -8.72658 | -47.97847 | 2026-06-02 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc73b31c-f875-3be3-bed1-9de969b99632 | -8.69126 | -49.08633 | 2026-06-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58308bce-f995-31da-b709-5e4f9a0b8a5f | -6.76503 | -45.02777 | 2026-06-02 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8c8a1a4-bc17-3556-8d0f-0d3f116573e5 | -6.75909 | -45.02917 | 2026-06-02 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c768fbc5-c731-30d8-a14b-3e4682fae170 | -8.68433 | -49.08525 | 2026-06-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54808d1f-f1ff-3fca-8ccb-2101a2abab5b | -6.99997 | -43.86432 | 2026-06-02 04:46:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b1b810c-d4c6-36ea-a8a5-b2127182f12c | -10.49599 | -52.13799 | 2026-06-02 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc7eae20-65ce-30fb-a0d3-46c200623bf9 | -7.50249 | -55.00528 | 2026-06-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2000cefc-dc05-35e4-ab43-ed24f48f25d6 | -9.28928 | -48.58722 | 2026-06-02 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 329f0778-6172-3384-84f7-1c8a9da1021e | -11.59539 | -47.44614 | 2026-06-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4e35ff3-154e-3af4-ab10-637c5a134981 | -8.69009 | -49.07036 | 2026-06-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac82f47a-b218-36df-a0c9-71bcb779e7a9 | -11.59147 | -47.44559 | 2026-06-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6dbcf9d-45ca-31b7-85b5-b1b4aa52cd07 | -11.58365 | -47.44442 | 2026-06-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8faf0e1c-78a7-3516-95b5-39297fede209 | -7.50447 | -55.00361 | 2026-06-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76ea6583-a044-3797-90ef-cf9c989c9fa0 | -10.03986 | -51.68243 | 2026-06-02 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c79e6ec-6338-3370-9e65-c2e32df3d529 | -10.54915 | -46.64114 | 2026-06-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a11ff12c-a4ba-37fb-bc02-ee5d7f666f8e | -8.69184 | -49.08247 | 2026-06-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14b9fc34-0a64-3e23-8fea-3cc38502dc95 | -8.98411 | -47.98185 | 2026-06-02 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0af1e9bf-00a2-31f7-8412-27995db9e489 | -8.5239 | -51.56492 | 2026-06-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 170503f5-011c-3718-89f4-208d49c32687 | -10.55321 | -46.64174 | 2026-06-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 771f190e-953e-33a0-bd4d-0b86648a6029 | -6.76336 | -45.02992 | 2026-06-02 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9900938a-5cd9-3cef-b151-938c5a115527 | -9.88996 | -52.44168 | 2026-06-02 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f554d02-95d3-38d5-b3f5-b27cce7660eb | -6.99048 | -42.8776 | 2026-06-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c75fa3b8-f5a4-380d-8be4-7fe8659aa4f4 | -6.99587 | -42.87536 | 2026-06-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 953940c4-151c-37ab-851c-e41e01d34310 | -6.61036 | -47.53796 | 2026-06-02 04:46:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74dfb160-56ab-3b72-a8f7-ca5cc8d21135 | -9.08514 | -50.59721 | 2026-06-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cf18e65b-0116-3ea6-9b58-6088514dc85a | -10.40401 | -49.44534 | 2026-06-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a4df7c91-c569-39b3-9826-2663598adde3 | -9.37546 | -50.54475 | 2026-06-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13960636-afca-3d53-9f03-3c352cb43cf1 | -10.98444 | -45.09431 | 2026-06-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e639573e-36cc-3fbc-bbf3-48703863ea68 | -6.10923 | -44.74652 | 2026-06-02 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f724cb6f-7b19-3808-afd5-792149bbc2be | -14.08226 | -58.14036 | 2026-06-02 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c79327e-b875-35f0-bd11-7ef348a10823 | -12.30247 | -47.91176 | 2026-06-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2d3a197-eb08-31cb-b29e-eff69e2243a6 | -11.27207 | -53.95783 | 2026-06-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb1e1984-0310-36d0-9377-d0253b4ed037 | -11.62183 | -55.17287 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c906719-a47d-3397-91b2-56d6eb02a28d | -11.56844 | -54.57665 | 2026-06-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a52d7ece-49b9-36dc-845c-139f39cd8709 | -13.70413 | -52.59507 | 2026-06-02 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1cb1138-80b3-3a24-913f-a03e4e3c1fa0 | -12.30145 | -47.90837 | 2026-06-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2412585-7361-3758-b170-6b3cda6b4d69 | -10.70952 | -56.24691 | 2026-06-02 04:49:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f696473-a05e-3c20-851c-15e16d9e762e | -11.32861 | -51.39709 | 2026-06-02 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e5da912-f490-356c-98e1-a0eab79d9922 | -11.27086 | -53.96535 | 2026-06-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf07dd3a-b69d-354d-ad3b-e5cfecccdcb5 | -11.88172 | -57.8402 | 2026-06-02 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35427c71-7903-3367-9430-c4a3cc94f5d3 | -10.89919 | -54.13419 | 2026-06-02 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 179d64bd-2f04-33c2-bd3f-307d22cecc9f | -11.62078 | -55.18622 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bec59a4b-f657-3d91-90f5-521d8be345dc | -13.98714 | -53.85908 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5939c25f-8450-360a-8d27-11c7ea9ac6da | -12.55268 | -57.18687 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8cece16-9cd9-338c-8cde-3911d6c09fc6 | -10.86301 | -53.74872 | 2026-06-02 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53f74778-1e73-3d08-8951-12bfad028ddb | -10.57319 | -57.32581 | 2026-06-02 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f813bfca-4f19-3b3a-a814-b8ac56bc95f1 | -14.23755 | -48.00204 | 2026-06-02 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a077ec68-cd42-3ed2-a10a-0cb8b33ca614 | -11.04032 | -56.9253 | 2026-06-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70823ccc-4ebd-3bb8-b6e1-fe1502334fcf | -12.73402 | -54.19833 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb07122e-ce2e-3eb9-9700-c89a83fd8e18 | -13.64469 | -55.29012 | 2026-06-02 04:49:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 845af2df-127c-3a87-9eb7-122d0c70af87 | -13.97987 | -53.86161 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3abe14f-2734-3cc5-af0c-109344ee4b87 | -12.17035 | -59.75989 | 2026-06-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01ce09b4-0493-31d4-b3b7-e370b79fbce6 | -16.15399 | -58.46781 | 2026-06-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 877d5e33-6a52-37b5-b777-11b022e01df3 | -11.62897 | -55.17408 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0949be94-67dc-3c6b-9889-cf09f649a15b | -10.81446 | -56.59765 | 2026-06-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README5.md)
