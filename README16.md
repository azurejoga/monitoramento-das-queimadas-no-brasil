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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8918fe6-aa7b-3148-9f9c-d6c9a314904c | -2.8897 | -54.1313 | 2026-10-02 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5a51509a-caae-3663-ac9d-fdd8c29aa4c1 | -10.7818 | -53.7493 | 2026-10-02 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| ca8e3e35-8197-3a97-9698-c435ef5e2ac7 | -7.7219 | -54.8114 | 2026-10-02 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7dd4128a-9a15-3c30-b38a-b5f0332c32d3 | -10.7818 | -53.7493 | 2026-10-02 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 4bc74bd8-f9da-34cf-9215-68e70f26e618 | -11.6579 | -43.5899 | 2026-10-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 72a69e4e-c2d7-33fb-85fd-16fb2c0d318c | -11.6767 | -43.6106 | 2026-10-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 3aed2c39-68db-3ebc-9e4c-1a9e2331d553 | -1.2556 | -54.5589 | 2026-10-02 01:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8eacb7af-d4a5-31be-8aac-0ea4b55e3431 | -11.1615 | -44.6002 | 2026-10-02 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c5478d2c-b462-32c6-b74d-983fbf40f5b1 | -5.7355 | -43.2916 | 2026-10-02 01:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 72081e61-0ad0-38ea-9243-aaf5ef1985d2 | -13.0378 | -51.2929 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 676f8db8-ba33-33c4-8020-6406cd0e006c | -3.1483 | -53.7426 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ac4185bb-0c7b-3d60-af6a-bc424e279825 | -3.1839 | -54.0839 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2632f226-bc22-3981-9765-942df010f3a7 | -4.2676 | -50.7506 | 2026-10-02 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| ccdbd30b-c714-31a8-a262-7c1586f33563 | 1.7853 | -55.6251 | 2026-10-02 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| de4978ff-249e-396c-979f-c2b9e38761b5 | 1.8037 | -55.6051 | 2026-10-02 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d2e45239-581b-31c3-acde-c57d906fb166 | -11.7733 | -43.5719 | 2026-10-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 270.3 |
| 3f30713b-f21c-3339-987c-8443ad81dfff | -12.8066 | -51.4063 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f4c3050d-683f-34f4-b96a-3af9d52b70b3 | -10.8005 | -53.7682 | 2026-10-02 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 8f5fdf3c-c6e3-3dc1-b5ee-eb3c4b9244f7 | -3.1838 | -54.104 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cd1c480f-1d9f-33ff-a51f-409deb752b16 | -11.1424 | -44.6029 | 2026-10-02 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| e37ba7b7-e81c-3f7e-80ae-a78122b96d87 | -3.1299 | -53.7633 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 1110d753-97e7-3a3a-bc8c-a3bec1003113 | -12.8244 | -51.4892 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 59e9dd06-8856-35c5-a17d-2bd4e1f86731 | -13.3481 | -43.8538 | 2026-10-02 01:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 298.8 |
| 261941ea-413b-3b63-99b6-4b10d5b3a59a | -13.0759 | -51.3095 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1eeb85f8-4454-35ab-85a2-2160f31eb153 | -6.914 | -43.6816 | 2026-10-02 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| d2196cc2-4416-3484-b479-5689cd1e29af | -3.2766 | -53.8602 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5919b0ba-2d07-3ff1-b202-35baafe5698e | -6.3952 | -56.4158 | 2026-10-02 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ca89efa1-d04e-3b01-887a-93cf89ee4950 | -4.2677 | -50.7297 | 2026-10-02 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 11bddc1f-92d8-355b-8934-229d5cb0dc8a | -12.8247 | -51.4679 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| be2fb0ed-63a9-37f9-a51d-d925b0694ccd | -13.3476 | -43.8776 | 2026-10-02 01:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| e74f1303-074d-3179-8e8f-45d72707cd24 | -3.0008 | -53.8874 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 74a36636-cd92-3fa9-8371-9630073878a0 | -12.9992 | -51.319 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c8aa1764-e9f4-3710-a4a4-5c8d42697c86 | -3.1655 | -54.0844 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 93c42bfd-4f2b-3f21-9a95-5a143b537dbf | -7.8682 | -44.169 | 2026-10-02 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 8408e9d5-292b-3885-8f3f-ced182ed340b | -12.8435 | -51.4869 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 10030fa1-041a-33e1-adc9-3a9c670711c6 | -3.1655 | -54.1045 | 2026-10-02 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| f1bfb243-3d2f-3bb6-a4ff-360d63de9cbf | -11.6959 | -43.6077 | 2026-10-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 0e2c91fe-b128-3291-9d91-5ea439588a07 | -13.057 | -51.2905 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 6dbc5ba3-76bb-3fae-8adb-5529c81d7cde | -2.0393 | -56.8789 | 2026-10-02 01:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| cd00e853-c3b0-3fae-803c-351a944a0fd5 | -7.0478 | -55.6302 | 2026-10-02 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 056b5d12-519d-32ac-8d8e-46ac9f3fda8e | -13.0762 | -51.2882 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 23c29337-029c-3e7e-b3f2-70ae5e2727ac | -6.8952 | -43.6833 | 2026-10-02 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 3fcd59cc-41c1-3a0a-87e4-9b551074d72c | -2.0394 | -56.8593 | 2026-10-02 01:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| af457867-7330-3e14-b46b-0b229587a259 | -4.2954 | -49.0807 | 2026-10-02 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 445a25bb-b12a-33ea-8b19-70900d29a45c | -4.2953 | -49.1021 | 2026-10-02 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 2db9880d-a9db-3544-93b6-02770f7e9aba | -3.0192 | -53.887 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| f3668de3-dd16-3303-91bf-6092f223836e | -11.6771 | -43.587 | 2026-10-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 2e3ac4ad-c271-3160-9432-eb12472824a9 | -11.7541 | -43.5749 | 2026-10-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| aa30afa5-70d9-34ef-89db-776ad49f5dda | -3.295 | -53.8597 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 6cd0a19b-e8eb-3cb8-bcba-fe4144b73502 | -11.7926 | -43.5689 | 2026-10-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 2a6a4e50-de91-369a-b2d2-1411440ad131 | -5.7563 | -45.152 | 2026-10-02 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| c7d1adf9-cf6a-3101-8704-4ceb6fd6810c | -10.7816 | -53.7699 | 2026-10-02 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 210.0 |
| 4f96148e-3743-35a4-89f5-9aadbacf6a5d | -13.0567 | -51.3119 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 51334fd0-9209-314e-a1b9-d2b61eb9aee3 | -10.7627 | -53.7715 | 2026-10-02 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 417fdc39-07a3-391b-99cb-8b140ff40a21 | -12.8062 | -51.4276 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 6f3db746-af97-3d21-a01f-425749a656c5 | -12.8254 | -51.4253 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| ec94b84a-d0db-3648-8a53-bc83c6bfb378 | -3.2767 | -53.84 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 773269a2-c874-399d-9355-fc8744ca3feb | -10.8007 | -53.7476 | 2026-10-02 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 9e1ed514-9018-3f7d-a237-ef5b533be42f | -13.0375 | -51.3143 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 78b2bb24-bb9a-3c96-ab70-a41d924ea5d6 | -11.7738 | -43.5482 | 2026-10-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7d9d1b14-ba8c-3318-9569-30b6f4e04992 | -3.1299 | -53.7431 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 6154ab27-17da-3f66-b748-cde194f10fbf | -12.9995 | -51.2976 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| c8022adf-74b5-3c36-81a2-71d2dd2b1359 | -9.844 | -44.8449 | 2026-10-02 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 475e678f-b4ed-3030-97d7-0b802dda550a | -12.8439 | -51.4656 | 2026-10-02 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d130e7f8-4476-3990-a8e8-8d83e3a6802d | -5.7542 | -43.2901 | 2026-10-02 01:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 1c86c9ad-abcf-32bd-a5c6-41f9bd509003 | -11.4691 | -43.4299 | 2026-10-02 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| a902026a-a505-3846-bbbf-96f5039c1cfa | -13.3287 | -43.8573 | 2026-10-02 01:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| fe25b08d-8c0b-3725-81c2-4b5012d91f14 | -5.7544 | -43.2668 | 2026-10-02 01:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 11c20058-ff3d-383c-9450-0610f182c827 | -5.7357 | -43.2682 | 2026-10-02 01:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| dd2df0c7-9aa0-385d-b124-081ca9d8438c | -7.4031 | -55.2114 | 2026-10-02 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 25ed87f5-c460-388b-8bf3-fd890da1adb8 | -2.0577 | -56.8591 | 2026-10-02 01:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 11cc12c2-f61e-3cbe-8f40-7e15d2151b1a | -7.8679 | -44.1922 | 2026-10-02 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| e831f94e-62b7-3fcd-b64a-175abd3db39a | 1.8037 | -55.5854 | 2026-10-02 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 48a93596-86a0-3b35-9a86-7f4f5073b41c | -3.2951 | -53.8395 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| a6e6c947-d2ee-3388-a666-83c7b0f3cbb6 | -2.0576 | -56.8786 | 2026-10-02 01:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 15fef263-b110-3749-bc39-dc07e6decf05 | -3.1483 | -53.7628 | 2026-10-02 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| e017c35f-29d0-3941-9ae5-510e849cace1 | -13.3476 | -43.8776 | 2026-10-02 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 401e85cd-bf49-32bf-a5b9-ef57ccb7c3e4 | -13.3287 | -43.8573 | 2026-10-02 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| a87905f1-2046-3da9-b98d-74f3c35f96a2 | -13.3486 | -43.8301 | 2026-10-02 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 89948435-42ac-378f-b7ea-77f7ce3e7d53 | -10.8005 | -53.7682 | 2026-10-02 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 3d5317a1-ac30-3085-9dff-e62814ad5905 | -3.1299 | -53.7633 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 49d71ce1-f71f-3f2d-817b-3ad95e8a14dc | -12.9992 | -51.319 | 2026-10-02 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 1526779b-3f52-39b7-86dc-e353561f8c8c | -11.6959 | -43.6077 | 2026-10-02 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 2e72abdd-ce14-340d-90d7-b3811181fe78 | -3.1655 | -54.0844 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 777a6427-0cd8-3795-81b9-9ddd48eef687 | -11.6579 | -43.5899 | 2026-10-02 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 5823eb2b-1c52-3d25-b553-70d293f8f205 | -2.0576 | -56.8786 | 2026-10-02 01:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| c80ec0e3-6140-3db6-8e49-6a048908c246 | -11.6771 | -43.587 | 2026-10-02 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 92aafc2f-cb0d-30b9-ad57-2a763f2a8866 | -11.6767 | -43.6106 | 2026-10-02 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| f48927e7-b573-37b0-8f80-4cd76a0b82ee | -3.1838 | -54.104 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| c68f6143-2ca6-3635-a894-b71664c90ea6 | -3.2766 | -53.8602 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c1fdc261-87d9-39c7-8ca7-542e190652bc | -3.1483 | -53.7628 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 79f8dbba-41b2-3689-acc7-8e045595c72c | -1.2556 | -54.5589 | 2026-10-02 01:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| d5c9f57a-23e7-36b5-87d9-c5c072cdfa93 | -10.5275 | -50.0208 | 2026-10-02 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 716bcdf0-29e1-3de7-a3c4-2edcbb108ada | -12.9995 | -51.2976 | 2026-10-02 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 5fd5c659-ceb6-39cc-8858-a48c27fdc469 | -10.8007 | -53.7476 | 2026-10-02 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| aad058f1-2ab5-3b25-b35f-7745170c3fce | -6.914 | -43.6816 | 2026-10-02 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 8420f6ba-c99f-387a-8409-fe50434e6073 | -4.2491 | -50.7514 | 2026-10-02 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 5bdb8cde-44ac-34d6-8158-b4e18ba4c9cd | -2.0577 | -56.8591 | 2026-10-02 01:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b60a6696-ee3a-385a-ab1e-ac2b3f77c8f3 | -7.0478 | -55.6302 | 2026-10-02 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| d618b028-a318-3297-9bf9-72abf414ab26 | -13.3676 | -43.8504 | 2026-10-02 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |


[Clique aqui para ver as próximas entradas](README17.md)
