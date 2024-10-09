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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74c692b1-ce16-31b8-8074-b718cd16c25b | -12.854 | -62.7897 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 116292ed-afc1-379f-b6af-77700481196d | -12.8557 | -62.797699 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 475323f8-07a8-3152-9766-1110252f11fc | -12.8426 | -62.784 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 19819d65-3834-38fa-9ecf-28a90a9b532b | -12.8443 | -62.791901 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c75e0ff1-5fce-33db-9045-e655c3f14ad4 | -12.846 | -62.7999 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dbd405aa-aaf6-3b53-9928-6bbd886475de | -11.8782 | -59.009602 | 2024-10-09 01:26:24 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9babfa3-2a5f-3dc1-8e1b-d7cc1f636e45 | -11.8799 | -59.0168 | 2024-10-09 01:26:24 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cb2bc616-1828-3987-b83a-43854e55e110 | -14.1192 | -44.9872 | 2024-10-09 01:26:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 288.7 |
| ff399301-2233-3680-a853-6be2e2d454fe | -14.1197 | -44.9637 | 2024-10-09 01:26:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 408.6 |
| 8a8726c4-ed06-3539-81fc-902c11ac735e | -14.1387 | -44.9837 | 2024-10-09 01:26:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| f78070bc-efaa-38c4-b6ee-90613a789851 | -14.1392 | -44.9603 | 2024-10-09 01:26:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 82b31d2d-5409-300c-aa42-9e53c0f3c18e | -14.1397 | -44.9368 | 2024-10-09 01:26:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 634e8916-76cc-3fb7-bc97-0484274e7d4c | -12.7016 | -62.940601 | 2024-10-09 01:26:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d11e9ee8-895f-3a31-a116-2a1a9b18423b | -12.7033 | -62.948601 | 2024-10-09 01:26:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63e9b6cf-dc6e-38f5-940e-0d74951189ed | -12.6866 | -62.918598 | 2024-10-09 01:26:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b4272c1-65b2-3a2f-9b93-366a68e093d2 | -12.6883 | -62.926601 | 2024-10-09 01:26:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a76d8586-a15d-345d-8771-de025ae8e587 | -12.69 | -62.9347 | 2024-10-09 01:26:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 079f12ba-bd31-3b69-8646-6029875bd71a | -12.6918 | -62.942799 | 2024-10-09 01:26:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d94dc3ab-d957-3ad4-b45a-feb5ae2bcc35 | -12.6935 | -62.950802 | 2024-10-09 01:26:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b055578-ff6c-3399-86b0-36b0bcbaface | -12.6952 | -62.9589 | 2024-10-09 01:26:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae63f5f-e7ee-3710-b745-795c450f653c | -12.6945 | -63.052399 | 2024-10-09 01:26:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| afba1baf-0e03-3012-a9ea-d64a4e1183db | -12.6847 | -63.0546 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 25b43c23-ea4b-3de3-9db7-d7468d5d014e | -12.5917 | -62.665001 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 607d8c98-72b0-3f67-b11b-72f0c3e95cec | -12.6766 | -63.064899 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 43d0a2c0-71a3-3e68-946f-da6ef3437567 | -12.6783 | -63.073002 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9997eed6-d2ed-3962-a40c-e21d0d3ca9ae | -12.6668 | -63.067001 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bcfbf219-3142-324c-aca3-f1cf7a1d1d7e | -12.6685 | -63.0751 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 75a2f828-4028-37c1-bf96-64e0da884259 | -12.6703 | -63.083302 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 00a15684-be96-3d6c-979c-1203a6cb882a | -12.657 | -63.069199 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| db85bf6c-52b5-3bb9-aa91-971dfcdec7ec | -12.6587 | -63.077301 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e1e3f9a8-dc13-3d56-912d-a013df62e4ea | -12.6605 | -63.085499 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ebdc4e0-8bb5-310a-a236-e3c0e510a090 | -12.6472 | -63.071301 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc49552-1797-3ee7-8667-eeef91911cbe | -12.6489 | -63.079399 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2af68fae-c64c-3d64-af60-2f05bf369345 | -12.6391 | -63.081501 | 2024-10-09 01:26:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2aa17047-fd54-3bcd-a9df-90086bf76b51 | -12.6299 | -63.134899 | 2024-10-09 01:26:27 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9f2b6a4-948e-3904-89bc-69238f45befd | -12.0562 | -61.046799 | 2024-10-09 01:26:29 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c23f05b-c5ac-38bd-8c96-fc48affdb946 | -11.5727 | -58.9361 | 2024-10-09 01:26:29 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c0fee53-864f-3056-934e-a81596089f49 | -11.5744 | -58.943401 | 2024-10-09 01:26:29 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5cf6e82-92c0-34e4-bb9f-3d37adf60d5d | -11.576 | -58.9506 | 2024-10-09 01:26:29 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9991025-18c8-333b-b8d3-ab7702e90ed8 | -11.5646 | -58.945702 | 2024-10-09 01:26:29 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f64333e8-e6b7-3887-b122-b3805e9b8040 | -12.4548 | -62.985901 | 2024-10-09 01:26:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 72aeae35-f2f8-31e8-a5ff-55f5897d24db | -12.4566 | -62.993999 | 2024-10-09 01:26:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8052f472-3a97-35f0-9f2c-ca0ad847282d | -12.4583 | -63.001999 | 2024-10-09 01:26:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1ec153d9-746d-3883-8f40-c0af95664dad | -12.445 | -62.987999 | 2024-10-09 01:26:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7cae50-d2b5-3666-99ce-6e1ed9329056 | -12.4468 | -62.996101 | 2024-10-09 01:26:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c888971-4220-3b23-85fc-468b6631889a | -12.4485 | -63.004101 | 2024-10-09 01:26:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 496c92f0-893e-3a52-91bd-f1f6b44d7abb | -12.4174 | -63.002499 | 2024-10-09 01:26:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b89a554-c23e-3240-9af6-b61e67ba996c | -12.4191 | -63.010502 | 2024-10-09 01:26:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7e5d0be-5408-3f73-8066-0028153d9d3b | -12.4762 | -64.0121 | 2024-10-09 01:26:32 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 171bc6dc-4800-3260-aa08-3f684f272cfd | -11.3671 | -58.9842 | 2024-10-09 01:26:32 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20fecfde-7ed4-3484-8ef8-2fc8b4a7971a | -11.3688 | -58.991501 | 2024-10-09 01:26:32 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04fd07fa-1b7b-38dc-abc6-06fc9e5bdbad | -10.628 | -55.872398 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6cb1e3e4-f816-3b0d-876d-77debc3fb8d0 | -10.6305 | -55.882599 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2208895d-d277-34c0-820e-006ce1acaacd | -10.6329 | -55.8927 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce1acb1b-cfab-3bd0-8de8-b8b05fd1d121 | -10.6183 | -55.874802 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fceb54c8-f240-3819-97f9-b49a16d3ce73 | -10.6208 | -55.884998 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5ae0fe7-8a4c-36fd-a3b8-a883e926dd6e | -10.6232 | -55.8951 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5fa765f-2640-3bef-b53a-49b3752e4eee | -10.6257 | -55.905201 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8853f3af-5a2c-3623-b9b2-344278223b8d | -10.6281 | -55.915401 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7699892d-1512-3700-872f-c3cd2cf38b72 | -11.3442 | -58.974201 | 2024-10-09 01:26:33 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c6cacb2-7409-3c0c-8add-4c0980edb3bc | -11.3458 | -58.9814 | 2024-10-09 01:26:33 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7a70422-f1c4-34a9-8d51-c3514991d0cd | -10.6134 | -55.897499 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc9361a5-e407-35ff-a3f0-fe7459e44264 | -10.6183 | -55.917801 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a47b0f99-20d3-3be9-b22b-e36cf6fcd5ed | -10.6062 | -55.91 | 2024-10-09 01:26:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3fee62dc-1dbb-3a35-aa8e-0154b8cccc63 | -15.5996 | -57.3699 | 2024-10-09 01:26:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 873514a6-c216-37e3-904d-d1a55115c811 | -15.5999 | -57.3496 | 2024-10-09 01:26:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 481c6626-7e47-3ba4-a1c0-8fd445067ce2 | -12.1414 | -63.344299 | 2024-10-09 01:26:35 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7a1fcf4-61e4-3331-8a97-626be05b4d4e | -12.1316 | -63.346401 | 2024-10-09 01:26:36 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 95254339-18fb-3149-b8db-1aaf458399be | -11.4541 | -60.420101 | 2024-10-09 01:26:36 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 58cdfccf-7f8f-3c6d-8d4f-6f690958a7da | -11.4556 | -60.426998 | 2024-10-09 01:26:36 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b0811478-78cc-30bd-9139-028779e56966 | -11.4443 | -60.422298 | 2024-10-09 01:26:36 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8f2ddabd-1aae-345e-b3b8-fe13d3b05b55 | -11.1306 | -59.077499 | 2024-10-09 01:26:37 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 142401a8-b69c-3ce1-a195-cbfacb9959f5 | -11.1322 | -59.084801 | 2024-10-09 01:26:37 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a6a49e8-551f-360d-82be-9e71139dde4a | -11.4262 | -60.433701 | 2024-10-09 01:26:37 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b4b1d916-9ebc-3c96-8a17-782e5b62660b | -11.4278 | -60.440701 | 2024-10-09 01:26:37 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e9147931-0b4f-33e8-b46a-47250b3ea2a5 | -11.4293 | -60.447601 | 2024-10-09 01:26:37 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 090510bb-d8ac-3017-8e4b-5a9951a0b077 | -10.3524 | -55.8423 | 2024-10-09 01:26:37 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d92257a7-5a1b-37e4-b439-6326137182d8 | -10.3549 | -55.8526 | 2024-10-09 01:26:37 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87815c6b-527a-32b2-8847-c534bb9961c1 | -11.4164 | -60.435902 | 2024-10-09 01:26:37 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 19632987-549e-33a4-95b7-37e69c04041e | -11.3973 | -60.3964 | 2024-10-09 01:26:37 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d39353e-310b-3b96-a29c-ceffba244c26 | -11.3989 | -60.403301 | 2024-10-09 01:26:37 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1dfde049-0b3a-397d-9df4-d7e8c79f2f83 | -11.3875 | -60.398701 | 2024-10-09 01:26:37 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d1b7e056-3537-3ab8-89d8-d9b84dfffafc | -12.1206 | -63.828701 | 2024-10-09 01:26:37 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d1f80afd-8dc9-3392-9055-f6180cd73a17 | -8.4723 | -48.585999 | 2024-10-09 01:26:38 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d6b89337-e2cc-3a2b-a4a4-f5ce7fb60fba | -8.4811 | -48.619598 | 2024-10-09 01:26:38 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| eb435eff-e86e-3fe3-a86a-eaf80193839b | -8.4899 | -48.653 | 2024-10-09 01:26:38 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2fdaa3e1-20cb-39c5-b53e-f668478c9a47 | -8.4628 | -48.588501 | 2024-10-09 01:26:38 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| da88766a-74fc-397c-bdcf-5c5d0a3a9f3e | -8.4716 | -48.622101 | 2024-10-09 01:26:38 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 60be3476-a974-3646-a044-f254fdf0717a | -12.0552 | -63.760899 | 2024-10-09 01:26:38 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c61222f-dbff-36f9-9d08-935365f0da15 | -11.3469 | -60.539501 | 2024-10-09 01:26:38 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cab1cea6-5650-3298-84dd-40ea8df3ad41 | -11.3484 | -60.546398 | 2024-10-09 01:26:38 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1decf1-7175-3ef9-8672-2456ad2be722 | -11.35 | -60.553398 | 2024-10-09 01:26:38 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 41cf801b-7fe3-3186-aadd-3544581418e5 | -11.3515 | -60.560299 | 2024-10-09 01:26:38 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 56a53172-f7ea-37cd-84c1-97d5dd991f9f | -11.3531 | -60.567299 | 2024-10-09 01:26:38 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b364b4e-a84f-3b36-bb96-fb31724ac5b2 | -16.4184 | -55.9455 | 2024-10-09 01:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 8b2a0b01-6b8d-36c5-9a05-f9b2e6ec7ecc | -16.4187 | -55.9248 | 2024-10-09 01:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| d319fe0d-5d07-30e2-ae5a-5372c331d624 | -16.4379 | -55.9431 | 2024-10-09 01:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| c9184590-8d8e-3c33-9f40-eb4383cac645 | -11.2874 | -60.319099 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 086cf28b-0b3e-3d23-ba3d-55cd0fc1d4b8 | -11.334 | -60.527802 | 2024-10-09 01:26:39 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 30a36c1d-bcc8-30a0-addc-1f220f7c9051 | -11.3355 | -60.534698 | 2024-10-09 01:26:39 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README42.md)
