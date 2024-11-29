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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4857d0ab-00fc-3843-9269-e9dbf8eca19b | -2.38494 | -56.09173 | 2024-11-29 05:46:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25731cb9-340b-3c7a-b1a7-e7cdb9cd80b5 | -3.33441 | -53.21451 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c444ea5-dcd2-3bcd-ad61-889b3f7f000d | -2.96809 | -53.29132 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7f4f376d-f435-3bac-babe-973dff3c6ea9 | -2.90799 | -54.1824 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e05b7ea-a0be-3285-a875-83254212856c | -8.65325 | -63.42534 | 2024-11-29 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16810599-68d9-3293-8fa9-0e56b883ba97 | -3.38943 | -54.28687 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a3303631-b705-3d9c-91d4-d440ec09c817 | -8.47163 | -63.94036 | 2024-11-29 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac2bb028-269b-3011-b360-8960fcc6e3ba | -8.64033 | -63.46059 | 2024-11-29 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcde8a80-c219-31c6-a9cb-5ba4460dbffe | -3.10026 | -53.81279 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1379e92f-3633-34db-97f2-31aab745a01f | -3.10606 | -53.82366 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8ddf786-cf54-3304-80aa-6d7279a8462f | -3.21834 | -54.18253 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c42abe69-01cf-3cce-ba06-263fd4f8081f | -3.417 | -54.90762 | 2024-11-29 05:46:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b76dbef-9ed9-3ea6-8ecf-14afca1b0042 | -3.67765 | -54.45089 | 2024-11-29 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccd9b507-aa5e-3539-980a-197865533860 | -2.83721 | -54.11628 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f803c8a-36ad-33e9-a782-33c57e751171 | -3.09948 | -53.81815 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9711f152-eb8c-3102-8669-5c659d8b0452 | -2.97571 | -53.28645 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b6894b5f-b074-3e0f-8bf7-85c22a626a03 | -2.7347 | -54.13655 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 16f5207e-189b-366b-b579-14af72a38f2c | -2.97668 | -53.28016 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4306aef9-202f-3ba2-8898-93789b6c94de | -4.07275 | -54.56921 | 2024-11-29 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14fb82f8-a541-3b84-8b8e-d1b6d4ad0dc5 | -3.49379 | -53.80328 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1758d3e-b837-3e22-a2b1-a62cd6799ebc | -3.10677 | -53.8139 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24f2ca7a-f745-3613-8569-5632b2829788 | -3.02293 | -54.02321 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 362625b0-d2ac-364a-9e5c-cddb9f0890f2 | -3.24566 | -53.63551 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2121cc81-6f63-3998-88c5-fb9199c14e89 | -2.90163 | -54.18142 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 014004ed-6529-3ffd-a0e0-3b469030d333 | -8.82944 | -64.27184 | 2024-11-29 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 890052af-3b6e-3c4d-8269-81e0eb43e3c9 | -2.73205 | -54.13861 | 2024-11-29 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 917c525d-6e03-35f5-a9d9-83f6ee12684f | -3.10039 | -53.81707 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eeafac6-3b83-380b-b934-e5820602f3fb | -3.11034 | -54.47665 | 2024-11-29 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99484984-24cc-31a5-8ae8-ae0b038f21fe | -3.22473 | -54.18348 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 339e8c18-cf63-3896-ae77-a963b21f4823 | -2.36973 | -56.11668 | 2024-11-29 05:46:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5c5cdc3-c85d-3e94-a626-d536e8d46727 | -2.89974 | -54.17833 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dc8c070-1a94-3d8b-b343-93e5d99243ef | -2.73125 | -54.14379 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 17dd1521-0e1d-3315-9f92-bb7d0bf7ca38 | -2.83503 | -54.11965 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dbfd03d1-15f1-3412-a5e5-4ad0e7f49fd8 | -3.47109 | -54.54123 | 2024-11-29 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 579fc38e-424e-3466-93ec-d38ad44da999 | -3.11195 | -54.48135 | 2024-11-29 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3757d241-c10c-38b5-8972-449970ac1177 | -3.09958 | -53.82238 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9408340c-d384-371b-b666-d71d5e42ea1a | -3.50834 | -62.85213 | 2024-11-29 05:46:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d4b74b7-f730-36da-a0db-db9c50edfd94 | -2.96803 | -53.7232 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d17cf5b-c504-32ad-8f1b-1aba37dc8c7c | -3.0714 | -54.40976 | 2024-11-29 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b634e87-4338-3cc0-9abe-dca09902f5e5 | -2.83646 | -54.12147 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79be4414-48ac-3097-bfbb-402c47a407ce | -3.07062 | -54.41499 | 2024-11-29 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9d5f8c6-a052-3ced-9624-ee42f22ca41e | -3.22785 | -54.07456 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a38877f7-b115-3f13-b810-feabf7251282 | -3.41089 | -54.90661 | 2024-11-29 05:46:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 374942aa-dbfd-3fc7-b801-a7f84ca68d7e | -4.5147 | -59.80819 | 2024-11-29 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b2474db-1489-39aa-875a-64640c6089b7 | -3.10772 | -53.81276 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 958f84f6-9f02-3875-afc7-40ddc0fbe735 | -3.09251 | -54.13659 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16174f92-e320-3535-b3ed-6d942f9ee83f | -15.09253 | -59.6431 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77c0f882-9615-3c31-9454-357bb69f8709 | -15.09293 | -59.6398 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec6d5e66-cdb8-3342-8d26-b15b9e38a2a6 | -9.01993 | -63.7694 | 2024-11-29 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccd35fb4-f557-31c6-97b5-0f9c16e16df6 | -15.08088 | -59.6451 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7163c5d-054d-3998-8c1e-3823bbd13001 | -14.48313 | -59.92099 | 2024-11-29 05:48:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 189d4705-ec5a-312f-9c17-8c031534d478 | -11.36425 | -56.21015 | 2024-11-29 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50e2b125-227f-3fbd-bcca-866b64fa164a | -9.83714 | -63.36408 | 2024-11-29 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0fa4900-00d8-3c3c-85d3-409b031ee1bc | -11.36368 | -56.21508 | 2024-11-29 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f6797a4-a284-3614-9989-b0f3d17d46a5 | -9.61852 | -62.54971 | 2024-11-29 05:48:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5061538-198e-3c8d-bfa6-3b1e2479dc16 | -12.41191 | -63.71698 | 2024-11-29 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a1a3da9-c492-37e7-a8fe-cba8532c4030 | -12.41262 | -63.71204 | 2024-11-29 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29a1bafd-50a4-3385-aa79-5a10c7b09278 | -12.40946 | -63.71355 | 2024-11-29 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 672e4d10-5c26-3ac3-a1df-550a7b026245 | -15.08157 | -59.64519 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d50c17c9-e946-35f0-b6d5-6d628097581e | -12.28046 | -63.74163 | 2024-11-29 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3987a5e-35c9-3dd9-9e03-4b182fab2a01 | -12.40558 | -63.71299 | 2024-11-29 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f3834e6-2a09-33db-b323-3975f9db9abe | -15.07182 | -59.63714 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 68d339a6-dd6d-310f-91e5-0f8c0198d012 | -15.08725 | -59.64249 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81b7b279-61b5-3187-8273-008c50bec509 | -15.08685 | -59.64579 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63cecfff-d466-3b35-9ff1-4808f0d6b1d6 | -9.81436 | -64.22902 | 2024-11-29 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb564e87-bee9-3564-9e10-2ef60fddbafd | -9.18636 | -62.37927 | 2024-11-29 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dba15de-9fe8-3a2f-a8eb-abe1a104f2ff | -9.51522 | -64.46314 | 2024-11-29 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20bf5599-f9ee-3507-ba03-f2ac7e552f98 | -9.92417 | -65.11336 | 2024-11-29 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c0a165a-c3c8-33f1-a08c-f5aac3bd6277 | -9.8224 | -63.24916 | 2024-11-29 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f0df7e5a-7fb3-3e7c-be21-ef5a94f979e0 | -15.09182 | -59.64304 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa7a4b1a-cb19-3eff-87d3-8d9f7cb33857 | -15.07709 | -59.63787 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d76f4f94-d44a-3ed5-9155-0f5cce8f6125 | -9.54121 | -66.1533 | 2024-11-29 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d0f2157-fd42-3cde-88ea-fc689bca3c48 | -14.48351 | -59.91789 | 2024-11-29 05:48:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 477c004f-4aec-3cc3-aa79-677f8c816c82 | -9.02058 | -63.76505 | 2024-11-29 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 625c2c49-473d-393f-b7fd-3fb0a5b068ef | -15.0922 | -59.63973 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c90bfe0-8143-39ee-8831-1e13bd434ffd | -15.09748 | -59.64034 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3da1bb2-3086-340f-b97d-46b1e6cffed4 | -9.94486 | -63.71359 | 2024-11-29 05:48:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 424ed43f-3b0a-353c-9aa5-f7bd64d41c11 | -15.09333 | -59.63649 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fb32b78-09f9-3e21-ac12-d4d7da660907 | -15.09787 | -59.63701 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 554a5002-d4d0-3e99-9c1c-5c8746339b41 | -9.54457 | -66.15383 | 2024-11-29 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f04d2bbc-0d80-3b6b-a2c0-e6df538aadbf | -15.08654 | -59.64242 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67a9ffb9-2fe9-36ec-b429-649762774cfd | -12.44003 | -63.69276 | 2024-11-29 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2c8e571-c3d8-31cf-9707-0bf8816b69b4 | -9.58976 | -62.05448 | 2024-11-29 05:48:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aed5fd72-78d7-3c0c-8a4c-d9cad8aba8c2 | -9.20704 | -62.37867 | 2024-11-29 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 354bff68-351e-353d-9a4e-e0f01efd3678 | -15.09258 | -59.63643 | 2024-11-29 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93a916c0-809c-3b1b-9e21-6071bd5f4b72 | -12.41334 | -63.71412 | 2024-11-29 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c90e88b0-52e4-36f8-9b64-f8ac9d797f24 | -9.92186 | -65.10496 | 2024-11-29 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c70a05a-3007-3256-b3a7-4806ccbd36ef | -9.65007 | -65.74296 | 2024-11-29 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2f6acb2-3430-3520-8371-fa5973f9a600 | -9.53154 | -64.60011 | 2024-11-29 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8e1e02e-08b1-333f-a633-9553a35eadfc | -2.9844 | -53.3022 | 2024-11-29 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| c9c623c2-f56f-3fa6-bfc4-86aa5c902678 | -2.6683 | -48.7981 | 2024-11-29 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 82d34a9d-02d9-376b-80d9-f51c99078685 | -2.6498 | -48.7986 | 2024-11-29 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 89e9b25f-5fc2-333a-9cdb-b28655656df3 | -2.6499 | -48.7772 | 2024-11-29 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 7c382ce5-f7f9-3f3f-a4f2-a6052b4a9e2a | -2.966 | -53.2824 | 2024-11-29 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 855ee27b-a6c9-3e8d-9fc4-73b73bea68d5 | -2.9844 | -53.2819 | 2024-11-29 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 6d24075f-0003-3f16-80ba-526be3bbcd77 | -2.6684 | -48.7767 | 2024-11-29 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 12263c2f-6818-3f1d-ba86-2a50b0905d76 | -1.6997 | -52.4535 | 2024-11-29 05:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 34d5dd00-73b0-3690-a75e-18282c17d976 | -17.65072 | -57.57149 | 2024-11-29 05:50:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f74198d8-e4cf-3ee6-8d98-1234b5ded02a | -17.57228 | -57.60352 | 2024-11-29 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5ad4d695-9456-366c-a317-16107aeb211d | -17.64326 | -57.56728 | 2024-11-29 05:50:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |


[Clique aqui para ver as próximas entradas](README107.md)
