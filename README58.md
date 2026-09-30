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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a761f418-90ee-3e4c-872e-ae5bfa23cf57 | -3.18269 | -51.24503 | 2026-09-30 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f17ab597-6976-33a5-abc8-46a40d81f524 | -6.13982 | -53.05819 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ec5ca3b-d55f-3bc0-a96c-f6aa28636ea5 | -7.55343 | -55.03758 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4864b248-e08d-39ca-85f1-29072fe3dd19 | -6.10874 | -55.70984 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26e9cafe-4163-3aea-b476-f785484c5146 | -3.01946 | -53.87781 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 004fc716-38d2-3af7-b3f1-cbd3448e3726 | -7.51003 | -55.03765 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1762ded-f344-342f-aff9-526125e16b86 | -3.3804 | -50.85015 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 90d357c9-1db6-363b-8c25-f2d65d7d154e | -7.50563 | -55.03005 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9db4c3be-3f4c-3162-bf5b-a4111c94f554 | -6.07301 | -57.60926 | 2026-09-30 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c69201df-c048-3175-92e4-6b187fd9a4bc | -4.02375 | -54.20093 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f02d53b-4275-30e4-b27d-a3fbadde7e5c | -8.11605 | -54.85397 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4006b61b-d53a-3899-88cb-b3909821c56c | -5.17214 | -56.00612 | 2026-09-30 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00847486-ec18-385c-b9ea-167f7f4bffbc | -3.01408 | -53.87693 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a47b5e34-5079-382e-87b5-e5b4ccac3cf0 | -5.72359 | -53.46605 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf099c58-4439-3a11-b21a-abc1bda09414 | -7.43163 | -55.18002 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cf4fb86-d7b1-3aa0-96fc-df93412530f7 | -5.98416 | -53.55168 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1acc1c43-a83f-340b-9713-3d0b834a2043 | -7.17636 | -55.40953 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c99a0be7-c706-3a9e-9b16-1b85846b80e5 | -7.71927 | -54.78698 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cb1a0d7-7fc5-3d70-954c-267a0879ce59 | -3.41643 | -59.57343 | 2026-09-30 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e404ba94-adf3-3b0f-adeb-76b7ba90737f | -3.65683 | -58.55175 | 2026-09-30 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 16c35879-203c-3792-a596-e4dffb27dd69 | -3.83076 | -55.80031 | 2026-09-30 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4aef21bd-e492-3779-8ec9-a933ac24fe21 | -7.50032 | -55.02925 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c49ef6b8-1071-38ea-93e5-502ca3f222d0 | -8.31847 | -54.76084 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d3e65ba-b2b9-38ed-af68-fa8babc855d3 | -3.7432 | -59.41616 | 2026-09-30 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88b9f9dc-252f-3eec-8606-8e8be9305b15 | -3.10723 | -50.28143 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c70a6e9f-47de-3f10-a27e-15f1801043c0 | -2.90198 | -54.0971 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| f73b4b20-f98c-3be2-b4db-fa19a9f1a380 | -6.74794 | -55.08382 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7e533be-09e6-3da0-9aff-f6de52334b6e | -8.29777 | -54.70622 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52cdb645-801e-38a0-9a84-999d729d3fd9 | -6.11032 | -55.69852 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9963f15b-73f8-3af0-b81e-e27a3191feaa | -3.18544 | -51.23743 | 2026-09-30 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e89ac62-16ac-39ba-b531-4a591012ee94 | -2.89426 | -54.1128 | 2026-09-30 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96040d6e-a816-3699-9711-512903b7a074 | -8.26823 | -54.76088 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58783346-c5e6-3a90-9d3c-c1cfc9162000 | -6.10614 | -55.69202 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d1b6c28-f3da-31cb-bf69-697bdb3b7905 | -8.29729 | -54.70989 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecc7b1b4-2a0b-3ff1-b9fd-27aeefccff4c | -7.50427 | -55.04014 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dc519fa-523a-3754-b6ac-727e2b680a99 | -6.78905 | -55.81982 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2ce056f-b260-3e08-893e-15ed7578d0e9 | -2.98045 | -51.04557 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 032e20ea-76ad-3c3b-bd61-f0bbaa823fdc | -3.15168 | -54.08148 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ec004e7-5ce5-3961-b6b5-51a8880d088c | -2.90295 | -54.09051 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| fa384328-f9c8-3db0-a0c5-1d35d857adb5 | -2.89764 | -54.08974 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a6905e53-5f68-3121-82c7-73ba6f95a884 | -2.90343 | -54.08723 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7089dbec-5d88-3fb7-97fb-d1b3649c3d97 | -3.37979 | -50.94714 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| caba5cf6-1957-3fce-ad5c-84e8b8d7c445 | -3.72049 | -54.22517 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba2d3690-7bc3-3028-b0f2-d2a70c12bfdc | -2.97968 | -51.05096 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0298bfb2-a5d0-3f41-92c4-620a34000f44 | -5.85811 | -51.78933 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 52d191db-31f2-3c6e-92ae-98e36a2f6e0b | -3.63855 | -55.47014 | 2026-09-30 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9e86099-6dda-3e27-a497-7870d1e398b0 | -4.02423 | -54.19756 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77a8dde1-0fb3-3d38-843c-304528d88b9a | -5.17303 | -55.99802 | 2026-09-30 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 853b28e2-ddbd-390f-9b9e-31c1ac473d9b | -8.26368 | -54.75294 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47ce0133-a436-33f5-94c6-f642db31dc7e | -6.11488 | -55.70225 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 135b837c-ba6c-3964-95aa-dd5c822682b8 | -3.82037 | -55.40844 | 2026-09-30 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81e05556-c169-32cd-a8c6-7f671a48d0c9 | -4.0317 | -54.19855 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b780bb1-5255-3ccd-aa67-a89a177bf96a | -8.32396 | -54.76152 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad57aa48-d3af-3220-9c8c-c44a35729b02 | -6.49223 | -58.53157 | 2026-09-30 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf610702-a269-3d73-ac96-d3c9e4f7cdd1 | -4.03068 | -54.20538 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2ed53f7-01b9-3c6c-999e-c8bb3c0fd84e | -2.89716 | -54.09302 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 919487eb-15d8-3914-8057-925226638dcc | -3.15701 | -54.08225 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf4b861e-bee5-3836-a40f-2fc5885f64f7 | -7.54649 | -55.03735 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f95b3c13-d7c2-3614-857c-8ba44fdd0d3f | -6.10733 | -53.09214 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f795fe6d-acef-3e52-8eef-4c914a087895 | -5.86798 | -50.16788 | 2026-09-30 05:36:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 147f6f8f-684c-3b32-adc7-66e634ee7be0 | -3.10352 | -50.27339 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 016fe523-19e2-3a3b-ae60-c58c61f65677 | -7.55297 | -55.04095 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0898be1b-2f6e-3003-9e8f-d26374f1ba81 | -3.10137 | -50.27425 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 01c24902-6da3-366b-81f5-7c4d2507c395 | -3.01996 | -53.87436 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 024b3aed-9da2-31bf-8853-4d7df54f92b0 | -6.23413 | -55.65394 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4db73632-8853-38ea-b43a-3a7d5c71e46d | -5.8567 | -51.78899 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2e09eef4-3cbb-3903-9e69-f250ac3875e9 | -2.97983 | -51.04573 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ce9c114-cb2c-33b1-b2cc-b0fe8e30f3bb | -3.01458 | -53.87344 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5cafa7a-c60d-316c-98fb-fdf8e5749252 | -2.89861 | -54.08315 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51fca833-d604-3ad3-9e73-d6e89f8dc59b | -6.06864 | -57.6087 | 2026-09-30 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79e1504c-94fb-3e02-80f9-6cf0eefd470f | -6.48811 | -58.53093 | 2026-09-30 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89f40f6b-c3b3-3fd1-a1b0-e184dd8aa68f | -5.1307 | -56.02095 | 2026-09-30 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58dfe696-5101-3f41-87c7-f83d356a6e9f | -3.38553 | -50.95359 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a00da231-a078-3837-95c1-ae3ee73c143f | -6.09902 | -53.0919 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d699777f-b98e-33be-9b8a-caca636d5ec6 | -2.89813 | -54.08644 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6f340af-4ca6-39e7-a181-0b671ce7a16a | -6.10912 | -55.70707 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65b8d5b4-62ef-30b0-a2c7-5694ce7062b1 | -3.18477 | -57.83795 | 2026-09-30 05:36:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e410c2a-7694-397a-b600-5cb1f4610867 | -7.72515 | -54.78429 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5e0dd35-0ba5-3230-a5a1-fe896468dfab | -3.37822 | -50.95802 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fbdd9c4d-8e3f-39df-b0d1-4ef907ff1cb4 | -4.02902 | -54.20237 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55dc8a21-965f-3fd9-b8e9-92c7eb0f363c | -7.5061 | -55.02657 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b401994a-bae3-333a-a12e-281a04faa84a | -4.02951 | -54.19884 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37b60b10-1950-38db-b5a5-36531ab311ce | -8.12194 | -54.85123 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dca6fc5a-75b3-3e27-a415-beb56106221a | -6.79426 | -55.82235 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccd159bd-d1c4-37e8-ab17-93f9d2e24a09 | -5.16611 | -56.01234 | 2026-09-30 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89a7ccf6-e74d-3cd2-8ae3-c09544cfcf0c | -6.43806 | -55.80506 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a736dfc9-0998-3d30-afbb-9778212d702b | -4.0281 | -54.20886 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1db02ac1-0c7e-351f-b682-fc812969775a | -3.72094 | -54.22202 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf176598-3680-308e-a43d-c5b632bc2381 | -3.37404 | -50.9408 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 860b0554-9ba5-31ca-aa5d-fb6c31d6e1b5 | -6.78864 | -55.82266 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02055686-a7c6-3cb6-9920-a9c05bf2d88b | -6.10051 | -57.63445 | 2026-09-30 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aae93d71-def6-3564-a2a7-f042da4bd46c | -6.10951 | -55.70428 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06f968b4-e883-3953-b83e-8d12753709be | -2.90728 | -54.0979 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 1418940a-ef29-3e4b-9262-27d9c180e558 | -3.37324 | -50.94628 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1c37c0f8-3434-34d5-9a05-3844b80192dc | -3.15651 | -54.08561 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03d6e421-b800-31b1-bc43-05ace42225d7 | -2.90873 | -54.08802 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1acda774-4ec3-3708-9c5b-3f69d700ba7d | -7.17485 | -55.40514 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8606d0e9-1b96-32cb-883d-b8655c040355 | -7.49986 | -55.03267 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cad62e00-1467-3b10-bb01-259d05f9235b | -3.25029 | -50.12565 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c7a0b71f-ab1a-346b-be5d-25428f90028e | -6.79464 | -55.81949 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README59.md)
