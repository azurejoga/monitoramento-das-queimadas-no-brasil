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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e31eae73-c68c-3d0c-9b47-dd11aedadd59 | -18.21452 | -56.55538 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0b9e3dd5-0193-3792-8892-29ee0c1f0396 | -18.19477 | -56.85106 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f7d66d6a-b048-3ed8-a83d-0dba19883816 | -18.19059 | -56.84491 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f68cbff4-aa96-302f-bbd5-7897453a13cd | -18.18994 | -56.85045 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e4a66bf7-f615-352c-a301-bc75c9d76143 | -18.18974 | -56.84041 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 43e962bc-26ea-3849-9e3a-fe9b8fefd9a7 | -18.18928 | -56.85597 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bd9c0eb3-42c7-3310-8c07-0356e3457916 | -18.18851 | -56.85151 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a6de1222-dd1a-3441-8a03-950184675b89 | -17.98399 | -57.36044 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0e848bb9-be7c-3395-8e00-9ecf4c1685f6 | -17.97932 | -57.35984 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 8452bf7a-fce6-3df5-a642-9698e99f5cf3 | -17.97466 | -57.35923 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 35664cc9-8376-33e3-9bf8-c225c390958d | -17.97406 | -57.36431 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 851c768b-374c-35bf-9206-dc8fa958b00f | -17.95771 | -57.38276 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| b78e95fe-f47b-354a-af92-a0d8da7b91fb | -17.95712 | -57.38781 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 48795608-2bba-35e4-8bc6-f88623456ccd | -17.90933 | -57.32845 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c1cd236d-9364-3d36-90c6-ffd92846d57f | -17.90872 | -57.33353 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2a42b75b-cf3e-3425-b177-bb9c2c1533b6 | -17.90749 | -57.34369 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 9bb92cb1-99dc-3bc7-a42a-21240910ff14 | -17.90688 | -57.34876 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| fb956aaf-b027-3598-ac09-1b6a2911724b | -17.90627 | -57.35382 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| d3470713-e581-31cc-be1c-332764686863 | -17.90589 | -57.31767 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| d981f4a5-8974-31a5-a5ec-d731eae17155 | -17.90566 | -57.35888 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 7b2c9923-f68a-3f4c-9712-2c59eb9c005e | -17.90527 | -57.32276 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d1eb338f-0285-322b-9435-a726ec3e8959 | -17.90504 | -57.364 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 7cd1de35-eec8-3ccb-892f-2b8661819298 | -17.90466 | -57.32785 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| b2fd9ee9-57ab-3fca-86f1-81875932043f | -17.90405 | -57.33293 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f509d28c-05e9-3d6e-84e2-c903ee7b5bd1 | -17.90283 | -57.34309 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| e1797694-6650-35a6-8841-eaf18d08ea82 | -17.90161 | -57.35321 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a8812551-5bef-3b13-8c57-ef6098afe176 | -17.90121 | -57.31707 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 3bedaf04-82c2-32b6-a0eb-791e6486c1f9 | -17.901 | -57.35828 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b600413a-bfa9-36b9-b468-1cf6cbf18e00 | -17.90039 | -57.36336 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 6be07b5e-6980-31f7-8709-0b528431c194 | -17.89715 | -57.31138 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5b06a8c3-4cf0-3da0-8f7b-90d6405e2e2d | -17.89695 | -57.35262 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 717add6d-0581-3ea4-8992-3dc7fb5be534 | -17.89655 | -57.31647 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c11972d4-6c79-3f94-9d25-3a09eabc8dfc | -17.88763 | -57.35141 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 6108fafd-d112-3f90-bd4c-e668ad3b4ef3 | -17.88297 | -57.3508 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| bb632004-6222-3b89-8f8c-a5b457b908d6 | -17.8744 | -57.30325 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ea158537-ea78-3810-9dae-7f3437780487 | -17.86972 | -57.30265 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 55155ee3-c73e-3198-aaab-81da02084113 | -17.86913 | -57.30775 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a38c8b50-8cc7-30b4-82a7-125cb7492941 | -1.44442 | -52.86086 | 2024-10-13 05:33:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8fbdbbe7-7cb6-380d-a340-2963d3fcd1d4 | -5.14678 | -45.4002 | 2024-10-13 05:33:00 | AQUA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f7a938f2-1bd8-3f6a-bde4-f6508fb2125d | -5.09327 | -45.84347 | 2024-10-13 05:33:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e70203b8-ce1c-3480-a307-6d4ced18c664 | -4.54015 | -46.55549 | 2024-10-13 05:33:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 31.7 |
| b87241a8-2c8b-3dbe-8df0-9eb126564e9a | -4.53994 | -46.54862 | 2024-10-13 05:33:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5d58eb28-df12-3930-a9e3-cd671044aa9c | -4.5383 | -46.55971 | 2024-10-13 05:33:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 777e336b-ccdc-3eaf-a48a-a5d906dc6941 | -4.40646 | -44.47682 | 2024-10-13 05:33:00 | AQUA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 7567712f-e206-372c-a086-2d2758fc119c | -4.39499 | -44.47515 | 2024-10-13 05:33:00 | AQUA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1a7194b5-887a-3417-9bfb-4ab361d666eb | -4.36721 | -50.79422 | 2024-10-13 05:33:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 890bbc2c-6dd7-37e4-97f8-f80172611d89 | -4.36583 | -50.80344 | 2024-10-13 05:33:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 399d9b99-557e-3c5f-90f8-acf613553bf2 | -4.29726 | -47.30066 | 2024-10-13 05:33:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 33962c1f-cfcc-3a1f-b522-fb4d282abd32 | -4.29489 | -48.62858 | 2024-10-13 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4202bbfe-5207-33b8-8953-7262d52eeb44 | -4.28969 | -48.23193 | 2024-10-13 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| acef9ddb-3e74-372b-a540-21aa1eca4a82 | -4.28934 | -47.28929 | 2024-10-13 05:33:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 96cb006b-99ee-3dff-95c1-d0a57de7745b | -4.28787 | -47.29933 | 2024-10-13 05:33:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d4f5e1ed-e043-337c-808a-e5fd4757e1d9 | -4.28597 | -48.62729 | 2024-10-13 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 725210f8-b581-333f-b8b7-de7f54990342 | -4.28067 | -48.23064 | 2024-10-13 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c5cd6df1-abba-33c0-b057-b328f60b9c5b | -4.12707 | -48.26811 | 2024-10-13 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 605cf941-1190-38d9-9c0d-626b934044ac | -4.12597 | -51.10941 | 2024-10-13 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 26212c6b-2189-38b0-b373-791f3de12792 | -4.12572 | -48.27726 | 2024-10-13 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 0961c8a3-ec03-39fa-99b4-ac8b0cd65c7e | -4.1221 | -48.23938 | 2024-10-13 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| f57b925b-7912-35f0-9921-6dc8ebeaee9d | -4.12075 | -48.24859 | 2024-10-13 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 542f2570-4a21-33a3-a677-aa540cf6a350 | -4.11673 | -48.27592 | 2024-10-13 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 286fe767-f14c-389d-9f1d-5be54e93afc2 | -4.0824 | -45.54189 | 2024-10-13 05:33:00 | AQUA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ded60652-4824-3fc6-9fd0-363647ec101e | -4.08058 | -45.55461 | 2024-10-13 05:33:00 | AQUA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| c50b192d-6d4b-396c-993b-f64e210ab0aa | -3.94451 | -46.42743 | 2024-10-13 05:33:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9a9cd8e8-9f1c-355e-b23e-6db3b7c157b7 | -3.94291 | -46.43851 | 2024-10-13 05:33:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 32a394b8-74e8-36e4-9054-08a04f52b56c | -3.93467 | -46.42599 | 2024-10-13 05:33:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 60eb4098-6c5b-3976-8bdd-c0422de91746 | -3.93308 | -46.4371 | 2024-10-13 05:33:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cc419113-e166-3221-be42-f201ac01b4c7 | -3.93074 | -48.3483 | 2024-10-13 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0098e05b-da77-372d-8f47-6ac1d40f5930 | -3.92941 | -48.35733 | 2024-10-13 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b7a42e04-bc08-3e4e-8ae7-55319c0509ca | -3.92419 | -51.22384 | 2024-10-13 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9fe408c3-fc3a-36e1-bc1e-169446de18b1 | -3.92274 | -51.23347 | 2024-10-13 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dc1e02f7-ee7b-3f54-b3f3-79663c784c37 | -3.92177 | -48.34697 | 2024-10-13 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 40e98714-383b-3257-ba05-4ff7f769053a | -3.92044 | -48.35603 | 2024-10-13 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 4dd71944-a9ac-31bf-a15f-2c7ab6c7e95e | -3.91147 | -48.35473 | 2024-10-13 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 05a8bc4d-7b5f-3de7-82e5-3d6f2cab7bb3 | -3.78146 | -52.38726 | 2024-10-13 05:33:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 02b29d4a-20f9-33fc-b685-e6e0c7efb8ed | -3.71874 | -51.78667 | 2024-10-13 05:33:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ea6b2fde-78ae-310e-8299-8c307fc9b973 | -3.71717 | -51.79696 | 2024-10-13 05:33:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8eefef26-8798-3203-b5cb-fcbd2159e91d | -3.68782 | -51.06857 | 2024-10-13 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| db3a1d0c-77b8-351a-8b67-08f6f1a2436e | -3.68635 | -51.07812 | 2024-10-13 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6ecff55e-0854-3f1f-a017-f692f8130f11 | -3.51704 | -45.77715 | 2024-10-13 05:33:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 164.6 |
| a906ed5b-9469-339c-8902-0c5717ab0b84 | -3.51529 | -45.78909 | 2024-10-13 05:33:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 6b6933c4-4389-3c43-9982-ad950fac2704 | -3.47189 | -50.60934 | 2024-10-13 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 214295c5-1824-31f0-9441-3048a01e16be | -3.44709 | -50.16221 | 2024-10-13 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d3a5e452-c0de-3e4f-a998-8d347525c4e4 | -3.35388 | -47.31532 | 2024-10-13 05:33:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 374f2c6a-f177-3b41-965b-e156d9470a7b | -3.35245 | -47.32508 | 2024-10-13 05:33:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 02ae45d8-0c59-382a-ba0b-0e6181e6bc7b | -3.34175 | -49.14925 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 52f27a3b-6101-3d83-9c6a-819910a87f49 | -3.34044 | -49.15804 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 96874c72-234a-3be9-8c2d-d844250c978b | -3.30113 | -49.10153 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f0871688-0926-38cd-a30c-6972c5250351 | -3.29361 | -49.09145 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea28b636-05d1-314d-928e-a08a9c6abb26 | -3.22713 | -48.92234 | 2024-10-13 05:33:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3c8cb3f6-1ff7-38a2-82af-79b3e3784ee0 | -3.19101 | -50.45514 | 2024-10-13 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 824879fd-aec8-3d4a-b911-3c8e7a852bd8 | -3.18964 | -50.46424 | 2024-10-13 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 2aeca853-e72a-3dc2-801f-061d91526194 | -3.182 | -50.45379 | 2024-10-13 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 3ef4dc46-acfb-3da7-b852-2435d3567c61 | -3.18062 | -50.46291 | 2024-10-13 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| c1d5eaa1-86bf-390c-9d61-ea05d3b05ad9 | -3.17161 | -50.46159 | 2024-10-13 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 2e7d4d09-4425-349e-93b0-be9bb4692512 | -3.16199 | -48.36522 | 2024-10-13 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a361b8d7-fbd5-36eb-8a45-00824496d7c0 | -3.11035 | -53.02599 | 2024-10-13 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fbb287c2-54ba-3f7a-a2b5-e7ab34d79007 | -3.1085 | -53.03837 | 2024-10-13 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| bb43ca6e-ec96-3add-beb8-20eb3ceb2922 | -3.10663 | -53.05085 | 2024-10-13 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 463f705e-39e3-345e-879a-01c02c1d38f2 | -3.10661 | -53.03108 | 2024-10-13 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| bd0f4fe3-e7ca-3c82-a076-8c4daec2d856 | -3.10467 | -53.04345 | 2024-10-13 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |


[Clique aqui para ver as próximas entradas](README112.md)
