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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6204ea06-8eab-37c2-9c7b-78ffb990036b | -12.31893 | -47.89727 | 2026-05-31 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 728d7fbf-472f-3f3d-b07f-96014a6a0926 | -10.57025 | -57.32355 | 2026-05-31 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18b0d945-b049-33f5-b926-2766248d26ae | -16.27105 | -48.97731 | 2026-05-31 04:38:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 81f07b6d-bfbe-36c2-a0ce-c21aea3950f6 | -14.22938 | -47.98622 | 2026-05-31 04:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ebee8288-91e1-3936-943a-03bd2008dafc | -10.81625 | -56.5956 | 2026-05-31 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef595390-9d9f-3e32-9a4e-4ee726ed25eb | -12.32229 | -47.89781 | 2026-05-31 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33f9d989-f91d-3c51-9542-bc99addda439 | -13.70302 | -52.97199 | 2026-05-31 04:38:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 706648ad-459f-3692-b800-4dc54c87278c | -11.60319 | -54.18801 | 2026-05-31 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa961e1d-2a99-37bc-8bc6-93d414d6fbef | -10.0723 | -51.6769 | 2026-05-31 04:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0b67307c-0ef7-3f2b-80a6-e96a347dffd3 | -10.0725 | -51.6559 | 2026-05-31 04:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| ab26594b-3187-3fb4-94de-3d94b6f88c00 | -21.80598 | -49.13152 | 2026-05-31 04:40:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9eb266c2-0d4f-3f82-ade1-d3c5b2a3d0a7 | -21.39904 | -45.49107 | 2026-05-31 04:40:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 06d5370e-48fe-3789-a11c-5ea25c01ed83 | -23.15148 | -51.65939 | 2026-05-31 04:40:00 | NOAA-20 | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 56db5cd3-0692-301b-a9b4-2b9faf5395a9 | -19.50765 | -46.81025 | 2026-05-31 04:40:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0790768e-cce9-3530-b16a-01b5b7b020ff | -21.21152 | -48.54398 | 2026-05-31 04:40:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0b80cd4b-9cc7-305b-b404-823862d9f7ae | -21.80656 | -49.12747 | 2026-05-31 04:40:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 26e57179-199f-3011-a18c-fc967c3520ca | -21.21503 | -48.54461 | 2026-05-31 04:40:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edd638fc-adf4-3a54-903e-b39267b6db55 | -21.32466 | -47.77144 | 2026-05-31 04:40:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eea1be94-5dd8-373f-99c2-19e63dbadba8 | -21.80715 | -49.12341 | 2026-05-31 04:40:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4342a926-f98d-3621-88fe-4a2c8f86cd11 | -21.49027 | -48.38097 | 2026-05-31 04:40:00 | NOAA-20 | SANTA ERNESTINA | SÃO PAULO | Brasil | 3546504 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd720e7b-4aad-3eaa-8332-9b59de083960 | -19.17383 | -47.35553 | 2026-05-31 04:40:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6215ec9-9ac4-3b9f-a268-7f38037f13af | -21.5678 | -48.52245 | 2026-05-31 04:40:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 138853c9-d219-34fb-9cb5-3d3617bedb07 | -21.81003 | -49.12803 | 2026-05-31 04:40:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 68dd7bd2-bd5b-3595-b1d5-d2b7d9f9400e | -10.0725 | -51.6559 | 2026-05-31 04:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| c7f08a54-ba9d-3d01-82ce-b3fedf4ccc6c | -10.0723 | -51.6769 | 2026-05-31 04:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 891f5317-45f4-3cbd-8470-1e35e3b54861 | -10.0537 | -51.6576 | 2026-05-31 04:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d816226c-4d4e-3edd-b7ba-dff6f9364930 | -10.0723 | -51.6769 | 2026-05-31 05:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| b46af814-cf39-31df-bce6-8fbbb0d9700f | -10.0725 | -51.6559 | 2026-05-31 05:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 4b2bfa7e-ada7-31d4-a6c6-7f33aa27bdb1 | -10.0537 | -51.6576 | 2026-05-31 05:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d10541ac-fdfc-31c5-9662-faf6ecd142cf | -10.0725 | -51.6559 | 2026-05-31 05:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 694cfb55-3754-3962-950c-b90e4d24c3a4 | -10.0723 | -51.6769 | 2026-05-31 05:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 20c5268c-54d8-3628-b9a5-c1288b952252 | -10.0723 | -51.6769 | 2026-05-31 05:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3562f16b-ddd1-331b-b76c-5e7c9ed26590 | -10.0537 | -51.6576 | 2026-05-31 05:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 43a8875e-3c82-39c1-b0de-c1d9f0b2b80f | -10.0725 | -51.6559 | 2026-05-31 05:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 9030c184-415e-3462-8898-c7390241ddbb | -8.20658 | -49.83757 | 2026-05-31 05:23:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7524584b-e2c9-3fd5-aabe-1cba0632a8a4 | -7.19247 | -59.83681 | 2026-05-31 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bfa8070-57d1-354d-935e-2b5d2743bded | -10.06824 | -51.64722 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f21bb265-e202-3c51-88ca-cd8b1033ba36 | -10.07016 | -51.67657 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 601cb47f-e18f-339d-8937-db0227be4bbd | -10.07832 | -51.6558 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 960ecc3a-f4b2-3b0a-8cf2-786c585c6d54 | -7.50342 | -55.00679 | 2026-05-31 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9337e5f-f5e2-378b-94fe-1644b5b9b130 | -10.62928 | -48.32518 | 2026-05-31 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 918b2ab7-d560-339f-bf97-c5d9eb1b4323 | -10.0669 | -51.65805 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a9497973-b93a-312b-b53d-ab3740bfccc3 | -10.07698 | -51.66653 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15f67246-ae6d-318f-bf0b-bd61abc11c05 | -10.06054 | -51.66436 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 50c0cc87-4091-33c5-9804-b201c3439b20 | -10.07061 | -51.67301 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8ae9aecb-8d0a-3ae0-8528-429560d90d4f | -7.50397 | -55.00293 | 2026-05-31 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 665f7c45-69bf-33f6-85e2-6710036aa01d | -10.74466 | -49.03062 | 2026-05-31 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17f1e288-f26d-34be-90b4-e3e172d63310 | -10.06646 | -51.66161 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 787c21fe-4037-3f0d-9321-720d85592e93 | -7.5076 | -55.00753 | 2026-05-31 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bdd4b4c-d866-3eac-9e04-4e9d7b4ac1d0 | -10.06972 | -51.68014 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5679934d-074a-3167-b35e-317938d45975 | -8.20601 | -49.84199 | 2026-05-31 05:23:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd4d488c-9949-3af7-97d8-9f7566d4b762 | -10.07283 | -51.65519 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ce5465f9-f906-3110-a4a4-5ca7b1607d1b | -10.06469 | -51.67582 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c5e3be9c-141c-334d-8a0b-21561d6a8199 | -10.07788 | -51.65939 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae689a36-c97d-3b0c-b0ff-34f83ae3cb6b | -10.06734 | -51.65449 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b8985587-f738-325c-8583-1b48ded57018 | -10.06513 | -51.67226 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 102174de-1d0e-31ac-9dd1-eeede6639120 | -7.50704 | -55.01142 | 2026-05-31 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91fb0702-b9c6-3277-bc19-818ca8c2f996 | -10.06602 | -51.66515 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 815cf355-52ae-30d3-b489-74a5eeefa5ef | -9.45371 | -51.82848 | 2026-05-31 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6923b29a-f9ad-3f4a-895e-b41d525841d7 | -6.80412 | -59.04474 | 2026-05-31 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0267aab0-f9b3-3bf2-a994-9362bdeb2ae4 | -10.07194 | -51.66234 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9d4dd489-a875-3318-86fe-22d01d7206d1 | -10.05966 | -51.67149 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9d885206-171b-34b4-9b33-2fb9afdbeaf6 | -10.05922 | -51.67508 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 29ba38ff-bb5e-30b2-ad4f-a2adc6ba36de | -7.49977 | -55.0023 | 2026-05-31 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07d75628-95c0-3721-94a4-3668fc935388 | -8.73579 | -48.3271 | 2026-05-31 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| daf87db7-d611-3be4-a443-b7ddd4587ed5 | -10.07328 | -51.65157 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d04213ea-a2e1-3ef2-992d-edf2914aff66 | -10.0601 | -51.66793 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5901f065-aeb1-3b67-be55-db19e60f4370 | -10.07105 | -51.66945 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 42175866-b4c7-3646-bad9-406960a34490 | -10.07373 | -51.64795 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f7d65dea-540d-32b4-9c06-75f7425933c8 | -7.50286 | -55.0107 | 2026-05-31 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 355ef8f7-ac80-39ec-9a59-31df24350575 | -8.72989 | -48.32016 | 2026-05-31 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2d68c9b1-4489-354f-af97-dfa74064202f | -8.73373 | -48.32509 | 2026-05-31 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8237c4a6-a0cd-3a69-923d-3d92dfc25595 | -9.45907 | -51.82929 | 2026-05-31 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b519cb36-76a8-3977-852c-20d89ea15be5 | -10.07149 | -51.6659 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 01f7083f-4274-3054-abcd-22a8b16e5165 | -7.49922 | -55.00619 | 2026-05-31 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 430df383-e14f-3507-bf6e-52fe24a77dd5 | -7.75064 | -55.33928 | 2026-05-31 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc34ea4f-34b4-3881-9df0-6e78c0d3cb5d | -10.06425 | -51.67938 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a426679f-a2eb-3d99-9840-406fdf349674 | -10.07654 | -51.6701 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c288559-dcd3-3e41-b7b4-c8ce66219a80 | -9.49366 | -48.66101 | 2026-05-31 05:23:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c32e79f4-ae32-3434-91f7-323e0d1ae9b1 | -10.05332 | -49.11597 | 2026-05-31 05:23:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff04fab7-5306-3753-96f4-2d068c8c3930 | -10.07238 | -51.65877 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7682dba3-75e9-3927-aa27-ae6a540e08ab | -10.06779 | -51.65086 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 34063c82-8e83-3d31-9593-8f0c4936af99 | -8.72914 | -48.32621 | 2026-05-31 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b4c8db4a-a355-358d-ac55-c33bf45796ca | -10.06557 | -51.66871 | 2026-05-31 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1a78b781-9e06-37c2-abb5-774c31728258 | -10.81379 | -56.59632 | 2026-05-31 05:25:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a68b8bab-6245-3b2b-b299-9aba190c7cdf | -10.70837 | -56.24156 | 2026-05-31 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bcc1976-e789-3dd9-8239-6dbc12d9f234 | -11.62443 | -55.17893 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0ed4d67-6cd0-3b7e-a769-a7147a6fbf78 | -14.76711 | -52.66963 | 2026-05-31 05:25:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 376da800-32f0-321a-9e21-35c40ee6b92e | -11.62557 | -55.1701 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6321df4-b823-338b-a525-e215ceae1c5b | -11.62941 | -55.17516 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfd4a534-4ad2-32bb-9a02-a2bbb716f959 | -11.62998 | -55.17072 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b18a3771-18ad-3b83-8f42-7844ff6a4489 | -11.63021 | -56.85944 | 2026-05-31 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ae10360-19dc-3044-9692-fa834ec20a33 | -12.54394 | -57.17495 | 2026-05-31 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6f22051-7fdf-3d58-a8e9-461ac7692614 | -11.80147 | -57.01288 | 2026-05-31 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a491581e-c189-3c89-bfeb-6fe2ac4810ec | -14.47316 | -56.83392 | 2026-05-31 05:25:00 | NOAA-21 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e810942a-12a7-3db3-8105-df41b565b815 | -9.75152 | -63.33627 | 2026-05-31 05:25:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6da425ec-374e-3572-b2e2-4422f35c919d | -12.54302 | -57.17868 | 2026-05-31 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd60a4f2-f99a-3812-8e71-4bcef65ed31e | -11.62503 | -55.17562 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b348dfa4-e2d2-31d3-86e3-139b2cc64d54 | -6.2786 | -48.53 | 2026-05-31 05:25:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9149c8e-8c4e-3347-8e89-45d68346359e | -10.81451 | -56.59107 | 2026-05-31 05:25:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README9.md)
