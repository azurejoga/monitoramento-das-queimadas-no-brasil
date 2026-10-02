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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9f87d86-8111-378b-9e6c-bfa151742905 | -4.2954 | -49.0807 | 2026-10-02 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| defed130-1f7a-3a29-9c8c-c45ffb8748c4 | -4.286 | -50.7707 | 2026-10-02 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c46a7c59-7549-3fa7-aada-de6937897940 | -3.1838 | -54.104 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 7ecbc59f-aa48-34e9-aa81-dd6b5db789e5 | -10.8005 | -53.7682 | 2026-10-02 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 1a28b72c-16c6-31d1-8efe-55bd59b87057 | -11.793 | -43.5452 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5a6c18b5-c9d2-3361-a2ba-10f6de5bf44b | -13.0762 | -51.2882 | 2026-10-02 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 6a7ec9da-a330-3b80-aee0-a9fbc7bef043 | -2.0576 | -56.8786 | 2026-10-02 01:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| e917f289-6a3f-3a54-a805-91586fbfc2d2 | 1.8037 | -55.5854 | 2026-10-02 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 03a0a5cc-909e-3669-9963-7e7ecf828395 | -2.0393 | -56.8789 | 2026-10-02 01:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a651c66e-1c68-3fcd-8025-3c37784e28d4 | -5.7563 | -45.152 | 2026-10-02 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 4e2e2ebf-2a4b-3bbc-8257-5e5d6ebb93c1 | -7.7219 | -54.8114 | 2026-10-02 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 800812ee-9827-38df-8081-1ca5ce1ceefc | -11.7926 | -43.5689 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 02967e62-e54e-38c9-a454-d7b39bd87d2c | -11.6977 | -43.5128 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 7ab82469-951c-3482-8dd8-7a804089fdaa | -11.4695 | -43.4062 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| e0a47ffa-a1bd-3c18-a504-7031caa94a45 | -7.0478 | -55.6302 | 2026-10-02 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 249ae9db-54a2-352f-8d3d-2d0d7a57249e | -3.0192 | -53.887 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 38b8fd10-5c1f-3e51-8f2b-086aa9b6c188 | -11.7541 | -43.5749 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e5759173-e2d2-3de7-ad3e-e40e483e8f46 | -11.7733 | -43.5719 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 680ec98a-bd17-3d7a-a1e5-2062ef472b29 | -10.8154 | -51.0984 | 2026-10-02 01:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 5b61323d-e430-3768-a2d5-5a3c93715510 | -11.4768 | -47.4422 | 2026-10-02 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c74e26aa-9cc3-3ceb-8f0e-6fa7f439fc6a | -13.057 | -51.2905 | 2026-10-02 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| b24ecdf0-4ad5-379b-8650-981c74485bbf | -3.295 | -53.8597 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| a35627a9-9e80-3740-b801-e076d80da290 | -11.4691 | -43.4299 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.2 |
| c7598799-5eca-377f-8ec5-1f39b323d30f | -4.2953 | -49.1021 | 2026-10-02 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 629071d9-84ec-3e68-a796-76a93350cb5c | -11.1424 | -44.6029 | 2026-10-02 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 27aec52e-63f8-32eb-a798-45973002d5b7 | -3.0189 | -53.9675 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c83fa8e3-4c72-3683-80da-fbe5f6e5540a | -3.2767 | -53.84 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 8a340765-6954-3856-a86d-fc59ac03404f | -11.7375 | -43.4356 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 90c14d31-4823-3fab-afe5-1ba542e18c2e | -6.4137 | -56.415 | 2026-10-02 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 67bc4493-7e0a-3727-82bf-2dff429066c9 | -11.4764 | -47.4645 | 2026-10-02 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 55e95829-0afb-3568-8525-694afe38c34b | -6.3952 | -56.4158 | 2026-10-02 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 6b1b09be-be62-3bb0-96a7-9eac24d06188 | -3.1299 | -53.7431 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| b384d9a4-d733-384a-917b-dd143673e9da | -13.0375 | -51.3143 | 2026-10-02 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 184f6df5-77dc-35cc-b7bd-f09bacb5850d | -3.1655 | -54.1045 | 2026-10-02 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| e6ddf4d9-123c-337a-a101-dfc44fd5add7 | -3.1483 | -53.7426 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| dad3354e-1df1-30e6-aca5-dae32d926d98 | -13.0567 | -51.3119 | 2026-10-02 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 0b05a3f0-5e3e-362e-806f-6fce7d902ad3 | -3.2766 | -53.8602 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 53d8adad-125a-31ab-be01-6456c70a58d1 | -11.4955 | -47.462 | 2026-10-02 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 592df18a-1780-315a-8f9f-2ec0033dbfaa | -3.1839 | -54.0839 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 49ea6689-a5e1-36e2-9841-91d19178a710 | -7.0477 | -55.6501 | 2026-10-02 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e7d6faae-147f-3ab8-99a3-9d2faadb52c8 | -11.6959 | -43.6077 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 20904ce8-5557-3215-8b92-d66cb463ac94 | -13.0382 | -51.2715 | 2026-10-02 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0d06cf7c-61d2-3c0f-98aa-decd2b0312bc | -11.7738 | -43.5482 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| b973ca62-aba2-31c7-a17c-2468161fffb3 | -11.3425 | -51.3182 | 2026-10-02 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a2eacef4-0584-3e24-884a-0e7dc408ec00 | -11.6964 | -43.584 | 2026-10-02 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 3783e7f3-ab34-37ef-aeb9-297ba04b7383 | -3.1483 | -53.7628 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 6b17bd6f-9907-3f3e-9e44-7c8d340bac36 | -2.0577 | -56.8591 | 2026-10-02 01:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5cc066bd-9ab3-3893-8e23-ca1aa00f29ae | 1.8221 | -55.5851 | 2026-10-02 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 15f60c88-93df-32f4-b2e7-dfaefbd874e8 | -11.1615 | -44.6002 | 2026-10-02 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 7ac1c1f8-3049-3829-a589-7dd389dd5d96 | -3.1299 | -53.7633 | 2026-10-02 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 0d4fb2b5-a393-3c4f-81a8-fa76efc4e51e | -7.4031 | -55.2114 | 2026-10-02 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4d678c2c-ee18-360e-887f-14e510c4b4a6 | -4.2676 | -50.7506 | 2026-10-02 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| bc563f92-81a2-3ff6-aa65-586f32de2a9a | -13.0378 | -51.2929 | 2026-10-02 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 0f6e3f32-f364-3cf7-90ac-632ff72d5b50 | 1.8037 | -55.6051 | 2026-10-02 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 9f91a07b-8d54-3327-9976-2f09d8b08773 | -11.4764 | -47.4645 | 2026-10-02 01:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 91bc03b2-a414-3325-a50e-0d434ff70881 | -11.7375 | -43.4356 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f19c6715-0d4d-3cbb-b10d-8ef7895be110 | -5.7563 | -45.152 | 2026-10-02 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 3bd8b197-f686-32d4-8c74-ec3115c5bbae | -11.6964 | -43.584 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| b7a04103-e41c-32b4-b440-0dda3479b776 | -4.2676 | -50.7506 | 2026-10-02 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| e9be3896-402c-38b0-bdf1-303112151d50 | -2.0577 | -56.8591 | 2026-10-02 01:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d03201c4-9338-38a0-9300-98365800edd7 | -10.8007 | -53.7476 | 2026-10-02 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 26306cdc-4b70-38d7-8c35-aeca9839f8f6 | -6.8952 | -43.6833 | 2026-10-02 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 760b4b53-d12b-3268-9976-fb6333074c02 | -9.5146 | -45.3427 | 2026-10-02 01:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| c9f4507e-cd1d-316c-bffc-1afd042528f0 | 1.7853 | -55.6251 | 2026-10-02 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 01159232-3ae2-3091-82fc-c7b5616b9744 | -2.0393 | -56.8789 | 2026-10-02 01:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| ae592751-255e-3d67-9dcc-756d34c9cec5 | -11.7541 | -43.5749 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 29523950-186e-3a81-b184-d4679e6e68ff | -6.3952 | -56.4158 | 2026-10-02 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 2d12bbc1-f95b-3cce-a661-089cd46464e6 | -7.7219 | -54.8114 | 2026-10-02 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 42942b14-b492-36a8-9659-bb8215e3988f | -11.6977 | -43.5128 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 8255c7b8-79f8-3e23-9838-a850505d9619 | 1.8037 | -55.5854 | 2026-10-02 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 72cfebce-04af-34c9-b09b-1b3cc54c3c84 | -10.7816 | -53.7699 | 2026-10-02 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 6ad09527-99d8-3500-a594-374f40c37dff | -3.1483 | -53.7628 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 05313af9-811f-322e-b153-c894559557c4 | -3.2767 | -53.84 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 9bfecb31-247c-3326-84f4-987c3a457130 | -4.2677 | -50.7297 | 2026-10-02 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 83922989-bcdb-3dce-9bf7-e455a478b583 | -3.0008 | -53.8874 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 6e11fad3-0592-3880-8005-a10e92f067b9 | -13.3676 | -43.8504 | 2026-10-02 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| a05c6eec-92b7-31ac-af6e-6b933cb3225b | -11.4695 | -43.4062 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 6a0c9b66-aa74-3cc7-a6ce-17fee525a3a8 | -3.1838 | -54.104 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| ca856c98-0dbd-3ec1-a188-ece4d30df3ce | -4.2954 | -49.0807 | 2026-10-02 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a565dde0-deec-34aa-b60d-119f5df8a43d | -4.286 | -50.7707 | 2026-10-02 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 008bb32a-d92a-3e60-8834-48083923448a | -4.2953 | -49.1021 | 2026-10-02 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| d4bc1e4d-7204-3630-b971-0c8f3901d20b | -11.793 | -43.5452 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 64aca123-be04-352b-9b92-c2a7da5740df | -11.142 | -44.6261 | 2026-10-02 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4e03498e-f3fd-3b74-9a91-f462f04ba35a | -3.1299 | -53.7633 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a9b5cf72-1bb7-3ec1-9301-71527dfa3fc2 | -13.3287 | -43.8573 | 2026-10-02 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 347.5 |
| 3fc6bc6e-0713-3f16-b05b-dcfa2cdbdb5e | -11.1615 | -44.6002 | 2026-10-02 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 3eccf550-6230-3b82-94a1-16f074dcbffd | -9.844 | -44.8449 | 2026-10-02 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| dc55ffb0-56d5-36f0-8bb1-c839a76b3a7b | -9.5149 | -45.3199 | 2026-10-02 01:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b40a7705-9cee-37e6-8579-a1dd46202e21 | -3.1839 | -54.0839 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 56ba1977-cd51-3fbd-ad06-2ffe89c914b6 | -11.4691 | -43.4299 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 009210a5-dca9-3172-b0df-83dea071d657 | -10.8005 | -53.7682 | 2026-10-02 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.6 |
| e63f22c4-c406-392b-9da4-581b8a5523e1 | -6.9143 | -43.6583 | 2026-10-02 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 01e414a8-0582-30f6-ba2f-029044f462c1 | -3.295 | -53.8597 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| c83f31c8-70e2-3524-a73d-ff7a4d796a09 | -11.7733 | -43.5719 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 1d04e78f-9e73-3ba8-ac88-cafe1cf2cd77 | -6.914 | -43.6816 | 2026-10-02 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 935b19ac-4a8c-31a4-9275-7787fa05acac | -13.3481 | -43.8538 | 2026-10-02 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 550.3 |
| 34b41341-d2b8-3603-b7f7-1f2f1cea3b02 | -3.1655 | -54.0844 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 89d89d94-ccfc-3a2c-b3b0-d28075fd61ce | -10.7818 | -53.7493 | 2026-10-02 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 9d20b846-2640-366a-972a-7edcf386165c | -11.7169 | -43.5098 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 59712380-8cb0-30e6-ac0a-ee2e9fd60280 | -6.4137 | -56.415 | 2026-10-02 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |


[Clique aqui para ver as próximas entradas](README10.md)
