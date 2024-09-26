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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adc43e64-b7c9-375b-9e07-4a321e5c5570 | -9.11553 | -61.31943 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba9a6891-dbbe-312d-b814-571419b8e184 | -9.11524 | -61.35276 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9b47f56-8771-377c-bc28-b7e32f4fa37a | -9.11495 | -61.32355 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38ff3f76-df08-3fa0-afe2-2ca22280866c | -8.47274 | -61.53464 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16c3fc5b-940d-3592-88b5-d69ea05c0c45 | -8.23321 | -61.52121 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba997909-4cce-372b-b190-4b9b9a827e2a | -8.22901 | -61.52068 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c4cda8e-7f2c-37b1-b90e-97f429701cfe | -8.22813 | -61.49685 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d66d9f-5889-3b7d-b108-572b91b1e234 | -8.22758 | -61.50072 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af214605-7fdd-3637-a047-0cce81640aca | -8.22703 | -61.50459 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76e31852-d43c-314c-b308-11a604d9c76a | -8.22394 | -61.4962 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a83191e4-b3fe-3a87-9425-55b7fdc93b23 | -8.22339 | -61.50007 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d73120a-8d30-39bc-97b7-a86ac8701d4a | -8.22284 | -61.50394 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 933b8523-fb36-33e2-a202-3a427559b71b | -8.21975 | -61.49558 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40a57751-c49d-3552-9611-003c6d4f0e67 | -8.2192 | -61.49945 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08ddb8e3-bfad-3374-a9d7-28a698235d5f | -8.21865 | -61.50333 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0df6f040-421f-3bae-852d-0b36a4aac532 | -8.2181 | -61.5072 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 890100b8-1575-3725-9633-88ad640ecbe6 | -8.21021 | -61.411 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adc20cb2-62c9-385f-acb5-e5084d58762c | -8.19865 | -61.4012 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07713bbb-40da-3358-8cec-c390ee608b2d | -8.17319 | -61.39857 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 988f07a6-8a34-3d79-a1fe-7f5a56d9310b | -8.17262 | -61.40251 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| adeec977-56f5-350b-a192-e89aa027ae75 | -8.16954 | -61.39403 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b05afc20-fee9-3e77-9df5-a6a92d812595 | -8.16897 | -61.39796 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30bfb148-4436-302d-ac05-19f7d1132e7c | -8.1684 | -61.40191 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 910b1c3b-331b-3fe9-82ea-f9833875c264 | -8.16662 | -61.53898 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d4ca847-ea10-331e-8530-b0c72101c03c | -8.1655 | -61.5396 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a9c6226-50e3-3537-8577-165f41d7225e | -8.16532 | -61.39339 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f63e143-d8c8-3081-94eb-3ce1bc01c3d3 | -8.16475 | -61.39734 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 083436c8-b21c-394b-8d8d-87da00c09398 | -8.16418 | -61.4013 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 311d2c8d-3468-3162-8b15-0da8d7820059 | -8.16242 | -61.53144 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3b30e75-fe00-3331-af3e-874bfcfa4cf6 | -8.16187 | -61.53523 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d76a8ee9-5e3c-3da8-85f3-da878602fcaf | -8.16111 | -61.39277 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d358493-f823-3e14-bf8d-fdb143eb667e | -8.16054 | -61.39671 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1a33e45-7e0f-334f-8a80-658318c4dc87 | -8.1588 | -61.52697 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52a2e012-1ba9-3807-b966-998501d57bc5 | -8.15825 | -61.5308 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7894d5d0-7f57-3070-a353-754f4931c796 | -8.15463 | -61.52632 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ff8d1c8-8dd7-3d59-97ce-65fa4dafeacb | -8.14924 | -61.2945 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 687e606c-5f71-3a60-a02c-a7e55116e5c3 | -8.14867 | -61.29848 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 443f8b20-487f-3d51-a9c0-2caa20149909 | -8.14811 | -61.30246 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1332b30-a94c-31c8-87b1-b2ba951d5612 | -8.14669 | -61.2819 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36dde468-3392-3b27-8ba2-bc432636f8a3 | -8.14613 | -61.28589 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0d001a2-e29c-3afb-9c2c-0dd56be21cb6 | -8.14556 | -61.2899 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef83cbdc-0993-3f04-bce5-9b2681e962ed | -8.14244 | -61.28126 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a6679f1-ea3c-3097-b694-b7eb86f7bf0c | -8.14188 | -61.28525 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca9bf33a-e04b-3ee9-ab5b-e124153843cf | -8.14131 | -61.28926 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b32c96a0-a813-372f-a6a1-35f1239b055b | -8.1382 | -61.28059 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3c74b38-836e-37b8-916e-c2e0f31ad361 | -8.13763 | -61.28461 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41e02a3f-99fb-306c-b974-fcfd36e75d43 | -8.13338 | -61.28397 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bdcba33-7ebc-376e-99a1-c655411d8781 | -8.13146 | -61.53891 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e12a0b0d-bc31-38b6-b273-817a65117ded | -8.08635 | -61.28275 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fa6a0b2-457b-3595-ad95-bc6d137c306c | -8.97768 | -62.40756 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8326a89-51a3-3a4f-a4b9-4f0bc80ca9e1 | -8.88814 | -62.30886 | 2024-09-26 05:46:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a30f064-8216-33fd-a815-0cd645f2e4f1 | -8.87002 | -62.37767 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8b80b04-01c7-34b1-bcc1-4708c1cc3bc3 | -8.86952 | -62.35273 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d31102a3-d4b4-384d-8d1e-b1e7f986f28f | -8.86652 | -62.34519 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d50a944-0991-3f94-9bb2-82639b404806 | -8.86651 | -62.40194 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e832252-55ef-32ef-b5c6-b58dc9d6a153 | -8.86602 | -62.34869 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7920066f-5c2e-3269-9234-9e7d1e16f3e9 | -8.86551 | -62.35218 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c5a2dc5-4d38-3f99-82a1-f939258ba9d0 | -8.86252 | -62.40139 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9eb1d34-c46c-300f-9761-04a7fa30f34a | -8.86201 | -62.34814 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 746f4796-9dad-39b0-947a-4332fc5fe529 | -8.86151 | -62.35163 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 884184dd-ea05-356b-824a-926e804efe5d | -8.858 | -62.34755 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aadb7b85-dbc8-3330-9e5d-769b6f9373e0 | -8.85751 | -62.35104 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94546683-e0c9-3bbf-82cb-fff0cc264fb6 | -8.85104 | -62.39619 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 530aa046-198a-3356-9e0e-8fc25b20bcdb | -8.84704 | -62.39564 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17de3854-2be4-3b6b-b219-2d1cfc0cf1f0 | -9.11437 | -61.32769 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1a0d8f2-97f3-3205-afa3-a9b591c175f6 | -9.1138 | -61.33179 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb933a14-b6c4-3adf-8eaa-3bd043e43c47 | -9.11323 | -61.33587 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c37e780-2469-3e69-a9cc-50cbc6460f45 | -9.11266 | -61.33991 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cffa5dc-9777-3fc2-9506-7f607456662a | -9.1121 | -61.34393 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9783c14c-b966-3a57-bf1f-959cad646254 | -9.1118 | -61.3147 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f40475a-8c99-34ac-b9ce-f7cb11d1aa5d | -9.11153 | -61.34801 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bbb0626-e211-31a8-aed9-2488bf8516e7 | -9.11123 | -61.31879 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f82fa54-1df1-31b7-b4e0-02fd51ff7c86 | -9.11095 | -61.35213 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b430ec56-d364-3c21-9752-1a35a8fa5ba4 | -9.11065 | -61.32291 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24e0135a-5dc0-3018-8830-a25fd4da5672 | -9.11007 | -61.32705 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f468882f-1a1e-3efe-919f-da261d7d1584 | -9.1095 | -61.33117 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27e5e3d7-71be-3f95-8cb3-d9413b752696 | -9.10893 | -61.33525 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0fba1c45-333e-372a-a1e4-0bfe650b53f4 | -9.1089 | -61.27241 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f0cfea2-90b9-3d9a-bb5d-6a4c46362c4b | -9.10836 | -61.33931 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a94ecb6e-3113-3d1b-a6e6-c65484860d5f | -9.1078 | -61.34333 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a3a9617-b7ff-3a8f-a330-a8b73a803a85 | -9.10723 | -61.34739 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ade1e16-5416-3255-ae5d-70afc5d6c259 | -9.10693 | -61.31817 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 592e0105-a28f-3f47-be03-bb2283ea1495 | -9.10666 | -61.35151 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7304a68-de0b-3780-ba6e-0c63e16e849e | -9.10635 | -61.32227 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67312fe4-4aab-3508-9424-82f0a958cc87 | -9.10578 | -61.32638 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fcba482-ccc5-310d-94db-20a0d970910a | -9.10521 | -61.33049 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05a3ed05-19c6-3e21-80c1-0f12c381002b | -9.10515 | -61.26767 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b5f91d80-256e-37d4-ac34-9d2bd7b42201 | -9.10463 | -61.33461 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a54cba6-da8f-3b89-bf55-5de9a22e6ca8 | -9.10458 | -61.2718 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1b700df9-9cf0-3642-84e0-1946d5b71eb2 | -9.10406 | -61.33869 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1d4c382-0e14-3f8f-b8b2-988d623ea8c5 | -9.10401 | -61.2759 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ab4e1d42-6d09-30ee-9442-b0c4a086c0aa | -9.1035 | -61.34272 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 419eaa99-e65b-3afe-9fda-0a6f9de8436a | -9.10319 | -61.31347 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f05c8987-d000-393c-b6df-2036a130a140 | -9.10294 | -61.34678 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b616d13-ca8a-347e-9341-bc58f8938320 | -9.10262 | -61.31756 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68bfbf1a-bc95-39f6-9b2e-7554657dd25d | -9.10205 | -61.32165 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ec33570-f65e-31c0-b80a-9893fc9c14c6 | -9.10148 | -61.32575 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0527c7ef-730f-36e6-abd2-cbef7ad652c7 | -9.10091 | -61.32985 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12919662-4c02-3a3c-a772-82a518fa7346 | -9.10084 | -61.26704 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d6f7dc82-70b2-343e-975e-6cc199046fc6 | -9.10026 | -61.27118 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README162.md)
