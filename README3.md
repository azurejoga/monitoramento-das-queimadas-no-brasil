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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d8f402f-7847-3e65-ab3c-4eec1b5c1312 | -12.4905 | -45.2816 | 2026-08-11 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| c28a4efc-ed8b-371b-bdc9-03d84abe6116 | -8.9038 | -60.5962 | 2026-08-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0779fafd-5e04-30ba-9771-ce6073a55545 | -8.95208 | -60.5259 | 2026-08-11 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 225.7 |
| dfc6f1d0-2543-3235-bcde-a6f6141b307e | -8.95856 | -60.5644 | 2026-08-11 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 817971fc-f6f4-3acf-ad07-550835a23473 | -8.89107 | -60.57598 | 2026-08-11 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 01ad3ca1-08f5-30d1-9068-f70d4a8f7876 | -8.95522 | -60.51818 | 2026-08-11 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 177.9 |
| e1ffe897-9a47-3304-8539-ea645cbd9fa4 | -8.9484 | -60.47929 | 2026-08-11 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e31d9ee5-3e6c-3038-a5f8-801aba00236f | -9.06524 | -65.45016 | 2026-08-11 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 195984e8-4d89-3ed1-b520-b10d4c404193 | -9.06769 | -65.46593 | 2026-08-11 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 76a4190d-12f1-319d-9278-2d879afeafd1 | -8.94553 | -60.48704 | 2026-08-11 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 8c9ddcbb-7874-384e-a304-8ee886b19b07 | -8.96196 | -60.55667 | 2026-08-11 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 525a4d83-6481-380a-b0db-585bb181c2df | -11.0294 | -45.6536 | 2026-08-11 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 5f948c2d-4a81-3ec6-b75b-9c7d11e4cd3b | -8.8855 | -60.5586 | 2026-08-11 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 14933498-abc1-365e-af2c-5ecfba9b99e9 | -12.4703 | -45.3308 | 2026-08-11 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 64cbf959-dfab-3a4f-89cd-be85ac670c3b | -12.49 | -45.3047 | 2026-08-11 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e95b13d8-83fa-3afd-8d39-52563ac12a4f | -6.1855 | -47.3284 | 2026-08-11 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 50dcadc7-a1f4-3712-ae1d-1b20b361cda3 | -10.424 | -46.6584 | 2026-08-11 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3ee9a3d9-1133-392b-b43f-de0df1d5bb42 | -12.4699 | -45.3539 | 2026-08-11 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 5c04dc4f-f9c9-3bf9-aa3a-edadeac44e20 | -8.9041 | -60.5577 | 2026-08-11 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6011cf49-4688-38e3-b00c-7317271c86cc | -13.8611 | -53.7845 | 2026-08-11 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d75e8dfc-3a5d-3840-bfb1-2f07bc512715 | -4.2635 | -48.1799 | 2026-08-11 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 93a81bc6-2e3d-39eb-bd10-b81241fb3f35 | -14.4544 | -45.6716 | 2026-08-11 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8fe1ced1-f798-3007-83bc-bab10f27b911 | -14.4734 | -45.6914 | 2026-08-11 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4e482189-7b9f-3483-a9b6-e57d61d86b35 | -12.4511 | -45.3338 | 2026-08-11 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7bf193ef-af6a-3701-9be1-416ddab12272 | -4.2634 | -48.2016 | 2026-08-11 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| df74592c-a7f4-389e-bcdb-742a6792533c | -12.4708 | -45.3077 | 2026-08-11 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| c5ac6752-8664-3b38-9df7-459db0da7411 | -8.9039 | -60.5769 | 2026-08-11 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 50471860-9bd0-3332-b241-e9e176b6e664 | -8.8854 | -60.5778 | 2026-08-11 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0dc1aeb3-83e8-339d-8e2e-893902be2400 | -12.4896 | -45.3278 | 2026-08-11 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 7f102919-7047-3fa1-ae01-578073f3a4c6 | -13.8608 | -53.8053 | 2026-08-11 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 6f26135a-c773-3153-b741-30158bbf7243 | -14.4539 | -45.6948 | 2026-08-11 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 23c29226-5780-318f-b51e-12a9f3bd68de | -13.88 | -53.8031 | 2026-08-11 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| da1a19aa-e11f-35f8-8a0d-74323fc1a39d | -12.4708 | -45.3077 | 2026-08-11 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c7de5c60-9316-32cc-b5e6-7e76a61d92ec | -8.8854 | -60.5778 | 2026-08-11 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| cd427557-4d7d-37c8-8ce8-cee5978584d3 | -14.4539 | -45.6948 | 2026-08-11 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 46600682-1a19-303b-8c21-0f181f010156 | -14.4734 | -45.6914 | 2026-08-11 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a9562b2a-2396-30ba-8eb2-b46e42498a81 | -12.4699 | -45.3539 | 2026-08-11 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 99b1e5b9-b884-32d9-af0b-145776046424 | -4.2634 | -48.2016 | 2026-08-11 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 8d38b086-733a-3376-990d-8dfff90b8b0d | -12.4703 | -45.3308 | 2026-08-11 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 7d97960a-7f85-3544-974b-2d805ef29aa4 | -8.8855 | -60.5586 | 2026-08-11 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2c45a001-1689-39f6-a209-d0d1d9ce37aa | -14.4544 | -45.6716 | 2026-08-11 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| bb18a951-305b-38ec-a56b-7f9e9d0121e4 | -8.9041 | -60.5577 | 2026-08-11 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 4af29a6f-0dfd-3cd6-8eeb-448d000f72af | -4.2821 | -48.1791 | 2026-08-11 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 31d9775b-5e4c-3f18-83b9-e6b3d8b6356a | -12.49 | -45.3047 | 2026-08-11 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 58e3d021-07b0-303c-b776-a709f0e57a84 | -8.9039 | -60.5769 | 2026-08-11 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 7bf85c73-6fb3-3d66-9356-d03dde17d839 | -4.2635 | -48.1799 | 2026-08-11 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| b2a6680c-8580-3079-a71e-84a5f37c20cd | -10.424 | -46.6584 | 2026-08-11 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 8ecc446c-836c-3987-8aee-5e4cad8ffc19 | -14.4734 | -45.6914 | 2026-08-11 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b2f3e584-bc27-34d9-b359-63c4e698cb7f | -8.9039 | -60.5769 | 2026-08-11 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| c17a26f6-f25c-3508-990a-3f8b0dca47a4 | -4.2635 | -48.1799 | 2026-08-11 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| b584d9ab-629c-328b-8311-a2c8b4138775 | -4.2634 | -48.2016 | 2026-08-11 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 02bfc633-a6ab-3cae-8dcd-4ee0982162f7 | -12.49 | -45.3047 | 2026-08-11 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 5fb8bcb3-0452-3911-ac6d-b12df761055c | -8.8854 | -60.5778 | 2026-08-11 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d3dd74a3-da3c-3636-aa5a-73d39e004b2e | -14.4539 | -45.6948 | 2026-08-11 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1e23e43b-ac42-3531-b974-e5c129d9177c | -13.8608 | -53.8053 | 2026-08-11 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 5053cba1-cdca-3196-af56-84761dfcfe13 | -8.9041 | -60.5577 | 2026-08-11 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 2cca0511-c658-3629-a6dd-bec81e9b2731 | -12.4703 | -45.3308 | 2026-08-11 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 1ac53f90-ca9e-3fbe-8fdf-5f962fb4b1f2 | -14.4544 | -45.6716 | 2026-08-11 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0c633208-6210-32ba-afc9-1e746153aa9c | -8.8855 | -60.5586 | 2026-08-11 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 884e252b-c7da-36f3-853b-0dc2fa38143f | -8.9039 | -60.5769 | 2026-08-11 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| c1775182-efb5-3f3c-ae5d-8da3bcd7c7af | -8.9041 | -60.5577 | 2026-08-11 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f3d564f8-e4ca-3bc2-a840-2380aa38cee1 | -14.4544 | -45.6716 | 2026-08-11 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| c54ce3d6-923f-3879-9303-50b158f5fb77 | -4.2635 | -48.1799 | 2026-08-11 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 59417f63-69d2-3eb0-92e7-3b27dc731fe3 | -14.4734 | -45.6914 | 2026-08-11 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 1d44a0c6-dc0f-3230-bf4e-4cbc0bf4d1d2 | -6.1855 | -47.3284 | 2026-08-11 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 2fa85eb1-d3ec-3529-9e57-62329e81e6c6 | -14.4539 | -45.6948 | 2026-08-11 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 65ffc2b5-9f65-3c75-b250-00d94e72349c | -4.2821 | -48.1791 | 2026-08-11 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| be59fd28-6005-3678-ad15-6096bf234ba1 | -4.2634 | -48.2016 | 2026-08-11 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 9a2dcad0-9668-31d7-aa75-7bcddb02c518 | -13.8608 | -53.8053 | 2026-08-11 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 5f693783-e68f-3e5e-af74-af3f03ca15df | -13.8611 | -53.7845 | 2026-08-11 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 90b58b20-883e-33c6-9116-d6db209d231e | -8.9039 | -60.5769 | 2026-08-11 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8ae3e746-cf71-3c47-a6b5-0de9f725094c | -8.9041 | -60.5577 | 2026-08-11 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 92371051-92a6-37b5-9e49-92ce8f7c0c63 | -4.2635 | -48.1799 | 2026-08-11 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 9157ff2c-7a34-3c14-952c-f365b6738bc3 | -13.88 | -53.8031 | 2026-08-11 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 07204e9e-3b40-35eb-8e75-612fc3470d32 | -4.2634 | -48.2016 | 2026-08-11 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| e2734e13-e382-38fa-b047-32ac4693c6d3 | -14.4539 | -45.6948 | 2026-08-11 02:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d1327741-20d7-3bb3-bdab-73e6a4fe8ef5 | -14.4734 | -45.6914 | 2026-08-11 02:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f16b38aa-098a-3a45-9f83-40ab6eaf56ae | -13.8608 | -53.8053 | 2026-08-11 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| c512c705-8c05-3bb9-96f7-1c71bf6ed693 | -4.2634 | -48.2016 | 2026-08-11 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 199292c7-6d6f-33aa-9ea5-be3ab7569699 | -4.2635 | -48.1799 | 2026-08-11 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 1eaceec8-1bf3-356d-acf5-abbddbfaddb8 | -8.8854 | -60.5778 | 2026-08-11 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ec52b148-e56a-3c4e-b78b-3b2b94aac6bb | -14.4539 | -45.6948 | 2026-08-11 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 16ccca51-b5a4-36c8-996f-18988fbcd877 | -8.9039 | -60.5769 | 2026-08-11 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b7678236-3606-3f72-a48f-ed41d2e3ba6b | -12.4703 | -45.3308 | 2026-08-11 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ee27970c-bd90-3274-b024-a8b7701ed0c6 | -8.9039 | -60.5769 | 2026-08-11 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| d5107ec4-af18-335d-8a55-833d3c788191 | -4.2821 | -48.1791 | 2026-08-11 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5a029d01-fc53-3ea1-ab12-e1046e838788 | -14.4539 | -45.6948 | 2026-08-11 02:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| acdfb5ae-dc79-3037-b23d-f08fbfe731fb | -4.2635 | -48.1799 | 2026-08-11 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| a4373109-4bb3-3337-907c-ddbe8da99bfa | -4.2634 | -48.2016 | 2026-08-11 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4856b5c6-fbc4-38b1-920a-e991708d4bd0 | -12.4703 | -45.3308 | 2026-08-11 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| e681a6fc-a856-3b4c-80e1-a53e6c17eb17 | -4.2634 | -48.2016 | 2026-08-11 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3231c5bc-b0e3-3b3d-a092-a3c280d4526a | -8.9039 | -60.5769 | 2026-08-11 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 613bfd1d-5d72-3ad8-a4f1-0a113932fde0 | -14.4734 | -45.6914 | 2026-08-11 02:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 882b66f5-e059-39a0-bc9f-2199d46f6fb5 | -14.4539 | -45.6948 | 2026-08-11 02:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 444532a0-4bee-3715-adb1-2b290e5af3fc | -4.2635 | -48.1799 | 2026-08-11 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 6291ff1c-da3b-36e1-bc74-12dd7d082326 | -16.6616 | -43.6228 | 2026-08-11 03:00:00 | GOES-19 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 9b896f06-a0ea-33aa-baeb-20f5cbdb65bc | -12.4703 | -45.3308 | 2026-08-11 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c408e440-6cd5-36da-96f1-e205e3365fed | -8.9039 | -60.5769 | 2026-08-11 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 32326017-cb9a-3e0c-a490-c7b80cd9c467 | -13.5894 | -46.2553 | 2026-08-11 03:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| acb2c2a3-8eb7-373e-b0ae-a4ee23689c22 | -14.4539 | -45.6948 | 2026-08-11 03:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |


[Clique aqui para ver as próximas entradas](README4.md)
