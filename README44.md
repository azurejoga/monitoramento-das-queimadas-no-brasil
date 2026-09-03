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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22e00f1c-56d4-3eca-8622-e52fa8d77df8 | -3.14919 | -60.64319 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e426ddaf-9125-3cb3-ba07-e5401e33c195 | -5.58465 | -60.19575 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d250f7fd-5e06-366d-a2a7-490f3e316b42 | -3.38843 | -59.42415 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| faaaea02-d2ce-3cf4-8492-8e737d749ec0 | -6.64654 | -59.44782 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 79c4552b-d9fb-3d06-969d-e22901f90d86 | -5.60275 | -60.24181 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3642f38d-a577-3fdc-a64a-5676486aa15f | -5.59225 | -61.47371 | 2026-09-03 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcd8a07d-7fe2-30f4-b5de-0505b8209c28 | -3.39326 | -59.36417 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f2bd251-4b4a-3635-bbd9-060e06bebca9 | -4.97489 | -55.85579 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 537b7999-3345-3844-a864-137468c1d8bb | -6.64165 | -59.4512 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ae954b38-0a91-3fc8-ac83-dc29e2611d3f | -6.3181 | -56.05006 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce37e361-0b3b-3eb1-a159-d5edbaf46cf5 | -3.7544 | -61.74865 | 2026-09-03 05:42:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71697891-6f85-36f4-ae13-db6d7bf33b05 | -7.07957 | -56.51806 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43c4795f-9722-324a-9d32-0f3931a0a52d | -6.64222 | -59.44724 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1fd6001c-40a4-353b-9442-c7bade8e738d | -5.46335 | -60.05484 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7928e2a-2a9e-37e3-a449-55a8d5d7be3a | -3.22792 | -61.21993 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 778a12d0-0243-3fe6-a7f5-1cd12ce7d596 | -3.39382 | -59.36042 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90cde15f-94e9-3c01-a0c1-c81c7f7c3763 | -3.61727 | -60.56956 | 2026-09-03 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 38909dcc-e223-3520-bd1a-f985bb9fe64a | -6.31856 | -56.04662 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6491bde7-78ec-3727-8bb2-2c5768b865ab | -5.45821 | -60.06142 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cefac2d-ce16-3f89-9c0d-cab7b8c2fd82 | -7.08444 | -56.51426 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4c21f1b9-6f26-3965-ab8a-3cdab4c425b6 | -3.97974 | -60.02917 | 2026-09-03 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cabeb5c8-cac5-3145-a5e9-367acc5d736f | -5.16132 | -60.27327 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50fb328d-3bd0-3a1b-ac93-b4fdfa02ceff | -5.58729 | -60.2004 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dda0a1f8-9978-3426-8376-8ec9f85741f5 | -6.64337 | -59.43931 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a0ba3f4-c53d-3527-baa0-05e81a9a2f0d | -5.2169 | -60.03317 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb045fcd-01cf-3b1a-b33e-7b00b72a57f1 | -3.55033 | -58.68398 | 2026-09-03 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53dfba38-17c9-3b10-bbcb-f29bd4d15084 | -6.77171 | -59.43425 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbffda6c-30ec-3fbd-b921-60f8e2d1cdb9 | -5.25189 | -60.18713 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 113852ce-270e-363a-88fc-a916507f3ec0 | -4.15621 | -60.7736 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0a142e4-224f-3853-a54e-e04698115cb4 | -5.32962 | -60.14394 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c288297f-620c-30a7-baf0-25d7530a95e0 | -3.37891 | -64.90323 | 2026-09-03 05:42:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82e8478f-af71-34ed-b087-fab86eba3266 | -6.68221 | -58.75421 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1506ea72-0ba9-3ad4-8d0d-d5c86a907972 | -5.46742 | -60.05544 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b9977f7-8901-3a52-9502-c1d8affd3e56 | -1.51123 | -54.95984 | 2026-09-03 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0af81176-9b6c-34a2-827c-35b26d54eec5 | -6.75504 | -59.4451 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bf6546d-3fcc-34ad-a2fe-6a0e13243801 | -3.77896 | -61.75662 | 2026-09-03 05:42:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7080cdc-d5f1-3460-a3bd-0bb59b72a0c5 | -6.6428 | -59.44327 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ea9c5086-19fc-32c7-a5d4-a0e4a23747b8 | -6.6532 | -59.43237 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9891d8a7-e89e-3ff2-8e7f-d62c013036ba | -6.12763 | -59.89426 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd5c7991-75e1-3634-ba58-44f3c605149d | -1.27829 | -60.33318 | 2026-09-03 05:42:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30d81fe7-8f33-3ceb-af65-8ba62111f6a2 | -6.77296 | -56.41285 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b227182a-0c07-3da5-be40-ed962c047c61 | -5.17629 | -60.28257 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 854dcfa5-0473-3023-995b-d843506da30e | -3.1246 | -60.70351 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 234ebc9d-b50a-3b98-9e03-b110ba4cb4aa | -5.20878 | -60.03191 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77cdf1a6-d107-3058-9118-55363435f909 | -1.62101 | -55.16506 | 2026-09-03 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ba5df12-b606-38c0-af19-7f34d4eccf3d | -3.02722 | -61.48211 | 2026-09-03 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37cad7b5-c6cb-3187-91f0-156bb0599c7f | -6.74699 | -59.43975 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8733cb81-7187-3038-b073-3c59472b36f2 | -3.12848 | -61.23326 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73237cab-a293-3263-a6a1-3d3c681b02ca | -6.75131 | -59.44035 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ab47c3d-a0e1-3196-ae07-44f4dff093f2 | -6.37357 | -58.2867 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f40e479-9fb3-3930-b1a0-c2916cdf1649 | -5.5957 | -60.2336 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ede6ab3-8335-358e-bbad-838db682d1ea | -6.88224 | -56.50654 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f595af82-4918-3f68-9da5-65d568938ced | -5.51111 | -60.18535 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d9727ac5-2451-329a-8a84-f150b7aab38c | -5.46281 | -60.05843 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90ac4501-17e6-3c9e-b4df-995567d3ee9c | -3.12481 | -61.23272 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40b5c96d-794f-3fe9-95f4-cd148bcafd4d | -6.76979 | -59.43476 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fcbaa06-3de1-34ec-aab8-5f87ffc5dde8 | -5.26197 | -60.18424 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47a0e633-7e1a-3473-ae28-19aed0bfbf99 | -6.68156 | -58.75886 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6151f629-e9d1-3c36-92c6-114c26289a96 | -3.12246 | -61.22355 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a57ded1-3abf-36fc-856d-adde1526f612 | -6.65577 | -59.44496 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b274615-fa95-32d4-9fde-86a7327d0447 | -3.03021 | -61.48683 | 2026-09-03 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52a74d8d-933b-3b75-96f7-b22c0dbffb03 | -5.58852 | -61.47316 | 2026-09-03 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5109f2f-49ca-3f58-af90-69ff50d8edd7 | -5.26147 | -60.18776 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5d0c5b4-4d89-3b76-8ce9-3086f38f3a0c | -6.6764 | -58.76281 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcdd40ec-fab5-3d57-9f11-33f15ad8d26f | -3.094 | -61.18831 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a510cb6-74fe-3a4a-a32a-fe4141e621d8 | -4.19647 | -59.94816 | 2026-09-03 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 771860bf-214a-3b1d-a566-38a1a6e24158 | -6.64887 | -59.43182 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8913c01c-1c2e-3c62-a7f1-0255bb11c491 | -3.14471 | -60.64721 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c21810fc-7fd6-35d1-bcc6-a720b925b864 | -1.3565 | -54.63266 | 2026-09-03 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceba6e09-a936-305d-8f42-4806e98389b4 | -7.08531 | -56.51575 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b01a0fd-bf39-3aff-a192-def81b5b7be6 | -3.64892 | -58.77832 | 2026-09-03 05:42:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 832468e0-f4e7-34f2-9cbc-a18c6e828250 | -6.67751 | -59.94776 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 9a34415f-6d75-323f-88f6-3a4655e2275e | -5.45875 | -60.05783 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c617adf8-5dc5-39ae-844c-947c42ec4df0 | -5.56571 | -60.17904 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 241f4ff6-f633-3362-a6d3-3a02a1166c10 | -6.68168 | -59.94834 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 80ba1b05-8dd9-3ee3-8d66-3ea078150c60 | -7.34416 | -55.20792 | 2026-09-03 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 511421b3-6bea-3712-82f5-ddef2a36e159 | -3.07043 | -61.21999 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a932e8a-2e36-34ba-9465-aabb8a5e13ed | -7.08577 | -56.51252 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf358387-35a9-3ffc-8a1b-08541a4e4a38 | -3.06978 | -61.22429 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a3526d7-838a-3e0e-9acd-e3232537f071 | -4.09988 | -60.66182 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6085b54c-3106-310d-a9b0-ab124140061e | -6.5998 | -59.1181 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0dd3956b-f8cc-39d9-a1ce-8a328c54b186 | -6.68113 | -59.95209 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d62f0bb7-f215-3987-b879-3352a771701f | -4.15239 | -60.77302 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7e1b6c8-ac9e-3bac-953f-5d97a8d78db9 | -6.65379 | -59.42834 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 325c4109-b18d-315c-a7d7-dff4da7a022e | -6.75071 | -59.4445 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be738c3c-d375-37c2-804f-bbdf235974fe | -5.25592 | -60.18774 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d4677e9-b6a1-3bcd-b09a-46da856f9842 | -3.39647 | -61.31727 | 2026-09-03 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b87197d4-ee44-3627-8b25-5a8e640927ad | -5.58818 | -60.19993 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2638f52b-b135-3e94-bfa8-8292b922c79c | -4.6929 | -56.06473 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b94eb4ae-7106-3eff-b38d-96e96224aa75 | -4.14841 | -60.69523 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d393c6e7-47f0-33fd-882a-41f904a5f1f6 | -3.12613 | -61.2241 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ce416b7-f49f-37e4-a7f7-77eff0bb01fe | -4.96998 | -55.85165 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ff5ad39-9a00-3a1b-b5b4-c155d5273f85 | -6.6853 | -59.9527 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a7375dcf-49d5-3c90-9449-8de9f47b324e | -6.77594 | -56.41911 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9038121a-2b36-3260-8bde-b0a0929cd334 | -6.37893 | -58.28244 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d96b209-c37a-37db-b331-eb8aeca208e9 | -3.95037 | -62.97481 | 2026-09-03 05:42:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8e41074-a0bb-33f4-be21-e304f3d7d8c6 | -3.14148 | -60.64466 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9538aa03-4592-377f-b9d3-1dadef1572b5 | -6.75994 | -59.4417 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e32d5111-6951-3067-97f0-df8b85c11e24 | -6.67768 | -58.75357 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d0b5a0e-44f4-3697-a3d9-6597a7579429 | -6.77684 | -56.41237 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README45.md)
