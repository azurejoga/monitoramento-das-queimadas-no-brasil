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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 032f333d-11eb-3e74-b27c-062c9712a626 | 2.0817 | -50.88961 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27f8845d-dfde-3d8d-a43c-537bf0cd2a19 | 2.10206 | -50.74261 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 121174f5-8a40-3e26-94ef-51f0471fba3b | 1.71887 | -55.65161 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9342cfc6-6ea6-3027-8d00-75bf3f87d98b | 1.60595 | -55.79195 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4512210f-5620-3d48-aee9-e24bafa71ebb | -0.40026 | -52.03501 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b458cce5-b96c-3aee-97da-3d114672cdf8 | -1.09945 | -54.14563 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d57fc325-5ec4-3d23-bc38-75c2b79cd3b0 | 1.87673 | -55.77241 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 366391ae-7bda-3ae9-b49c-121e4f033c19 | -1.3326 | -54.22691 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f51a5b48-49c1-344d-afe2-ec5735844be0 | 1.98468 | -60.61234 | 2026-10-05 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63ac2114-1318-3372-965d-cb29e82bb8f6 | 3.10013 | -60.62341 | 2026-10-05 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 678f0e53-9430-3f9e-bda2-68e66109d035 | 1.75296 | -55.61148 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd9557d5-a5fb-30a1-84e8-fd0e0be29653 | 2.08511 | -50.88685 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad254a73-aa90-31de-bb77-106c74bd0479 | 1.89797 | -55.77999 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bc96f30-f56f-3a72-ae67-7f8eb09d7624 | 1.73278 | -55.6437 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7220bfe1-3857-34bc-a2c1-5dd6f91b9ac8 | 2.01239 | -50.92641 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3243ba35-7fb8-384d-a985-789a2c6fb2e7 | 2.0841 | -50.88094 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3edcddc6-10c9-300e-8c8d-2a2a024dab80 | 1.80076 | -55.55291 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48763c3c-8a89-3edb-a1f1-2c74bebc7d7d | -0.3906 | -52.01158 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72ac926d-fe01-341d-885c-b75c53aaf161 | 1.74802 | -55.61236 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24975056-9954-3e27-bada-164299543401 | 1.87185 | -55.77317 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9d1e0f9-1d9f-31ee-922c-8cf7da0ce747 | -0.39588 | -52.01751 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e07a9f7-0ef7-3dde-8da3-8e4c5c6dd71f | 2.00866 | -50.92628 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f13a70e-1df6-32eb-8130-ab6d7e794dfe | 1.60337 | -55.79074 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 864103ec-c883-30a9-b17c-710f479a853c | 2.07845 | -50.88805 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dceb7a73-2714-353d-b308-bbaea20de2ca | 1.98111 | -60.61292 | 2026-10-05 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 427c12c1-b2ba-36fe-9656-e0a514826725 | 1.87497 | -55.76146 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41fb0320-23e1-35aa-b5b0-674719304b0a | 3.36137 | -59.83156 | 2026-10-05 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0893cfc-c60b-3b69-96f5-3882689d8a86 | -1.10517 | -54.14645 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50471414-5a81-32cb-82d7-c791c8a8dc5c | 1.82557 | -55.54889 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a91a7a2-1007-31c6-acd5-f2e449080b98 | -0.38496 | -52.0051 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8fdc215-67c7-3310-9e6b-66d710d1dab6 | -1.0872 | -54.11124 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 012131b2-3d3d-379a-95b2-91a59b014f8b | -2.82795 | -54.12094 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 510ceed8-a3d9-3870-9287-b28ef110bcee | -3.04659 | -54.21156 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9b21bbc-27e0-36bb-b4b9-927791b4bf0a | -2.94388 | -54.14188 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0f16e24-8dcb-3a73-a56e-bf368fa31498 | -2.82413 | -54.11449 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 715ea6ab-354a-3f7b-bd8a-008e0fa4e2e3 | -1.5582 | -54.79739 | 2026-10-05 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb3a7f84-3cdc-3c7d-a214-d2b025827912 | -3.86937 | -55.81021 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c12e79a5-ef0b-3884-ac8d-93c804308872 | -3.11844 | -53.74017 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 247f4524-cb0a-3cee-99f2-a3ef879b4ef5 | -3.07086 | -54.16775 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 556cba18-c0dd-3c2f-a24c-2cad0c0645bc | -2.95118 | -54.14004 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 83a7415d-26d1-3fb8-8fab-1705227e2f9f | -2.7908 | -54.09631 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c999e816-e930-36cf-9688-8d986903e8d7 | -3.84796 | -55.84463 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92976808-a683-39ff-8f2f-ffb5bb5451c2 | -3.11784 | -53.70295 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d92042fd-9b95-30cf-9e24-859ffb925fe8 | -3.10902 | -53.76181 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| a63746ac-c983-39a5-bbd8-7d83f71ff7bc | -2.94713 | -54.20269 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0c7ec84-246b-3662-9072-25ed4063d911 | -3.13998 | -53.73086 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b83daee-c8bc-3ccd-989c-5735c886bb44 | -3.8752 | -55.80765 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e93c7dd-beb1-3e76-baba-b22db2c28329 | -3.185 | -54.07642 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c6ec5f-5bf2-3d89-9cd8-e93c440fd0fe | -2.95707 | -54.1408 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b9a88023-6780-31ff-bd7e-be512a4794a2 | -3.04538 | -54.21999 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9da6efb7-8a54-30af-bc7a-b08084f09bab | -3.50973 | -54.62012 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a13b800f-72d2-3f16-817d-17b909aacaa2 | -3.28379 | -54.17315 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd4e56a1-9ca3-35b2-9304-afae7a407d7e | -3.08783 | -54.1749 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 29f0a0df-9161-38e5-ad33-f20238228952 | -2.85202 | -51.3032 | 2026-10-05 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f80ab0e5-da6f-3c78-b0e1-8f4c29c6d024 | -3.28315 | -54.1776 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc4d1c61-e917-3717-80b3-49580129caee | -3.05358 | -54.21095 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66c10b31-13ea-3fe0-8eb4-d7eb2ecf8c4c | -3.87953 | -55.81515 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8d396d7-1cac-3a66-a854-c6269d8a655e | -2.16661 | -53.67033 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c51784eb-266e-3cff-a682-da06b135fcac | -3.09565 | -53.7274 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| eeb400ed-5e42-30b5-98b8-168c97ad642c | -3.11105 | -53.74827 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 142d1c8f-48c1-3f2e-b897-5e39b9897c04 | -2.81553 | -54.09162 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78cc1efc-8a1d-3624-81ff-02621e704f32 | -1.55783 | -54.79753 | 2026-10-05 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54adbbc2-24fa-31cb-bbe2-47613f076e8a | -3.1158 | -53.71661 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bd7582b4-81a1-399b-811e-7b391a1b036a | -2.95281 | -54.12145 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d80a8422-a986-358e-83a3-e8c2747df596 | -3.88104 | -55.80499 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d42ffc8-ee90-3ffc-93d3-bc275f52b27c | -3.1117 | -53.71255 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ebd9f71a-9778-39db-bb3a-d79dcf9a7146 | -2.91718 | -54.12646 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 941adb43-3f73-37d0-922b-4dce86cef2fd | -4.45979 | -54.96581 | 2026-10-05 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87ed386f-e420-3ab3-adb2-eb01489ba831 | -3.11925 | -53.7462 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15f0c494-5adf-36b8-abc3-4eccf3a74e43 | -2.95406 | -59.15798 | 2026-10-05 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24ffef69-7f99-31a3-8ca3-5818dd771ea4 | -2.80989 | -54.12952 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b30283fb-5c10-3735-b5e8-791ddcf417bd | -2.98523 | -54.10518 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2c36063e-126a-379b-a0c2-60af3b2a78c9 | -4.45921 | -54.96996 | 2026-10-05 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac0cb798-8c7c-3c71-8c4f-54e9ef09aa2e | -3.12107 | -53.7637 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 347bad2b-b2be-3c01-92be-6a8ece9084cf | -4.46547 | -54.96676 | 2026-10-05 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 443bd43b-56a6-32d6-be4e-e76b1457a38b | -3.11776 | -53.74468 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b362bd0e-abb9-32a0-89d4-083f0103c524 | -3.31242 | -53.84496 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71760f2f-8887-3e06-bf44-7810af49c7a3 | -1.88667 | -56.28203 | 2026-10-05 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0ab35f99-d933-38cd-b461-21a41526581f | -3.97192 | -59.33429 | 2026-10-05 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 803ae659-a6e0-32d5-b1e5-854ef952337f | -3.30513 | -53.853 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4de76897-e9fa-3dba-9ba9-abf54a342882 | -1.24998 | -55.8838 | 2026-10-05 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85d96e13-f3f5-3051-8d8e-c369a1c57824 | -3.05123 | -54.22092 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e1c4a33-8d18-3057-90b0-1bfc7ea15c8a | -2.85298 | -51.30463 | 2026-10-05 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5da4b54c-5dfb-3950-891f-2aa0c29163d6 | -3.12379 | -53.71445 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00913aad-d16b-3191-9af6-84974c6147c0 | -2.81428 | -54.10005 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c44b3d25-4def-3ad4-85ec-84cb92726716 | -3.05294 | -54.21515 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb3cb3c4-bc7a-3130-afce-e8278db79949 | -2.85689 | -53.91782 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f831002e-468d-3e26-a013-3bb88f09be4e | -2.94132 | -54.12571 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e600fb42-dbed-3b8b-98af-7219d62d8224 | -2.95578 | -54.14928 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| d53cde71-6a4c-39f4-b34a-ee05527dbcc0 | -1.76611 | -55.03137 | 2026-10-05 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa45bf9c-bc07-3baa-912b-cf46bc56245b | -2.85909 | -53.92152 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1f72011-9ee0-308f-8e35-31c073cefdd7 | -4.46489 | -54.97084 | 2026-10-05 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b975fad-978b-346a-9b3d-6ab7a24d62a9 | -3.14063 | -53.72635 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 447f6da5-eaff-3273-8de2-f3951873611b | -7.32029 | -55.03698 | 2026-10-05 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 229d576e-cc36-3a34-b56d-56417d527c26 | -3.11646 | -53.72257 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78d9f789-8122-3da3-8701-e891df7c05ea | -6.20921 | -52.82821 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4816a33d-e543-3140-b157-2f7f6ed5c367 | -3.04478 | -54.22421 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 782b1276-5fbc-361d-910c-5bcb830de46c | -3.10309 | -53.72974 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4247aaab-a98e-3d48-a861-e851b4ec1d30 | -3.50556 | -54.61887 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ab5e57b-2298-3a84-87b7-c59794c9b77c | -3.05408 | -54.16786 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README50.md)
