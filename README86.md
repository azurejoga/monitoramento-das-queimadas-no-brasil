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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3902f203-4449-3d32-9c84-abe6896bab6d | -3.36049 | -50.47122 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31868ba4-884f-36dd-baca-aaa1e08b2828 | -3.59301 | -54.56546 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 928b2c4c-5644-379b-9893-dc4d95044834 | -3.05283 | -54.2104 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 781432ee-3875-3ace-8222-e8ad515de2f1 | -3.27161 | -54.02823 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9e76ce0-c043-3332-8e47-af12d69593f5 | -3.27945 | -54.04392 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 27e35d53-3971-3764-af12-293efade5ae6 | -3.65052 | -54.06091 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4f24c96-75c5-3b0f-a146-2a3491417c1b | -1.40576 | -54.60522 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82271ee5-ecc2-3af8-a0e7-527bfc2919a6 | -2.98517 | -54.05256 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c59c0490-e230-3d38-8d63-982d76eb878c | -3.94499 | -55.7134 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fff97de4-25ea-3694-b2a5-a4658bc2876b | -3.27066 | -50.40155 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d856993-fa0c-3ff9-93fa-e1b30a414ac8 | -3.08539 | -54.2405 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e6459f1-8c77-3856-8496-8cfc88548acd | -3.19028 | -50.55913 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5ad906a2-8937-30f5-b155-a4cee9e3cd4f | -2.95902 | -54.11356 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cbcc3d3-ec2a-3e92-b6de-fbab30e170fa | -3.29893 | -54.02878 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1619476b-28b2-3cab-9c7c-15d5c56fc93d | -3.10225 | -53.76149 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2460d023-379a-36c3-86bc-e57e187b9e9f | -3.06048 | -54.24734 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19f0254a-75aa-35ba-9c73-0efdc6ef0997 | -3.77903 | -58.52518 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6bccc9ab-c398-3f85-b7f7-cae4b2d4d553 | -3.08671 | -54.29794 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bb9bc12-9d09-3de6-b489-b2c42ac13233 | -3.73235 | -55.98299 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b81eba7-f817-32f5-a521-67350616f9d9 | -3.10271 | -54.28254 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 34f44f0d-94bc-3b32-8cd0-07bf71dd9928 | -3.23807 | -50.17483 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b978bd0e-dc97-3797-9dae-683100388b0a | -2.83124 | -54.12576 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82193b04-0a32-3e21-81d1-02b2bb1a8dc3 | -2.79249 | -57.67427 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24bbb3b5-47a1-39b9-adfa-c21f39263bf3 | -3.84217 | -50.31612 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5483b2cf-20e9-3e53-a2c1-b23bb18b4e9d | -3.41415 | -58.90952 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 97d8d764-6a69-3c4d-bd0d-703e978d9981 | -3.17517 | -57.54399 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4529954-7a82-3d5a-a604-57d54ef093d8 | -2.56553 | -50.67998 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c39c4f6-d134-3511-8a1c-4e4bea06b19b | -3.30773 | -42.28168 | 2026-10-07 05:04:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 040f350f-460f-34cd-8347-a3d7ee4d38ce | -2.93846 | -54.11402 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cc67273-8c1a-3e77-83c7-f5c85f1089ee | -3.3515 | -54.17024 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d645454b-d63c-3613-8726-c75a311ae652 | -3.10163 | -54.28952 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| eb2c2b21-506d-3f28-b548-7d94fdb95ee0 | -3.28126 | -59.56531 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed5babf3-7b71-3c7d-908d-c3d7c931d292 | -3.50249 | -54.66523 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d16d1978-fb1c-37c1-897d-9840ee7ce31b | -3.05338 | -54.20689 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69099d3f-1717-3069-82e0-874ac6b38e84 | -3.08392 | -54.29393 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c5a5d3b7-74d0-3b63-8584-b4c02e6a27bf | -3.09003 | -54.29845 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1aba4c27-cf78-3273-9ca1-b347b3ffcd4a | -2.99894 | -51.11739 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a75a929e-6810-330e-b7e5-378d4bbd0e24 | -4.11769 | -50.82866 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 262e1df2-a15a-34da-8593-772f0671f6f1 | -3.09997 | -53.73179 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 924436d8-559d-3911-a262-64f6d12fe1e6 | -1.10587 | -54.15023 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4782ecc-0167-34bf-b338-84126ce69d66 | -3.43942 | -56.93671 | 2026-10-07 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c27c1ec-8a98-3088-9d09-d80b52313106 | -2.49562 | -56.123 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93a100f6-c307-3e06-ba3d-a3bdd9c911b9 | -2.93792 | -54.11753 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95480d0b-ea8c-33c5-b7c0-8b2b5fa05314 | -3.0826 | -54.23649 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e654e51c-50bd-3401-8f9e-4f210cc0f664 | -3.40851 | -50.76497 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eadf8cf5-dfd4-3424-98d1-b369db744df9 | -3.60491 | -54.35677 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 544c36e4-fff6-36f2-ac10-6de8c8e57d66 | -3.58916 | -54.30413 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d1f611ce-a2cc-3a51-babd-50f34b39a0ea | -3.47861 | -54.62255 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 007c2eeb-e4eb-34ec-ba92-0e934a74858d | -3.07719 | -54.27143 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44e3c515-c95f-3af8-a0a7-3f2edab719dc | -3.11403 | -53.7743 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c300953e-7de8-3e33-886a-fa4cb0122cda | -2.68446 | -49.03318 | 2026-10-07 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92045b20-633f-3265-b8e7-957a775ac12c | -3.0023 | -54.18466 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77dbc60b-6882-32b4-b86c-9e7558f811a2 | -2.99487 | -54.12249 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf5b17e4-bee3-35d4-bf42-464a48db5304 | -7.29677 | -47.26344 | 2026-10-07 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a2723af-4887-378b-9b86-13228970fba1 | -4.3667 | -43.90725 | 2026-10-07 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af320de0-78b8-3c98-9984-82fd25b4a6c1 | -3.54888 | -59.4902 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6f70b9c-2572-3ad4-8e85-b5057d05a8ea | -3.99054 | -56.24726 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a901beae-4043-3dc1-bfd8-88a6db2840c8 | -2.878 | -54.12987 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9425299b-7f85-3db9-a041-9de7b2084788 | -4.44713 | -54.97901 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23aa9472-f946-36d5-9f50-ee1b2f6bb9ae | -5.24096 | -50.91412 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2598a625-d97e-3a76-95f2-6b15567af41d | -2.99037 | -54.10741 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9a7c5ff-0606-3ef9-8b7a-4630cef46689 | -3.84345 | -50.99441 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c868cf34-45dc-3156-856a-4e91e87081f2 | -3.7728 | -59.40344 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2d6bea62-5d3c-3bad-a89a-c62cd31b4bea | -3.07711 | -54.24997 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71ebbd1d-5423-3967-b5b6-bc9324487f5a | -3.29176 | -54.07473 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 567d8038-ffc6-3398-9a75-83efe1b508ee | -3.17995 | -50.5472 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7bea113b-a419-338f-8f82-be4117fffed4 | -4.46517 | -54.97481 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b98c5666-a10d-3b3b-ab3d-d10896d663ea | -3.21873 | -53.8819 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3c69ec7-b5be-387e-8cd4-46f538e3d80e | -3.48909 | -50.08702 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1185155f-8629-30e3-980f-cfdf717c257b | -2.46726 | -56.06495 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c1be287-bff3-3909-8f3f-66d9af1779a7 | -3.08376 | -54.251 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 002a9054-7dbe-3279-906e-1c07824044c2 | -2.97937 | -54.13445 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c50886d-b45f-3070-8cfa-6e7fc2016619 | -3.5168 | -54.66038 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2b306e6b-fd9e-3bf2-b499-ce301cd401d8 | -3.47224 | -50.08804 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 322b3579-5c7b-3185-b13a-bf1062c6dd4a | -3.28693 | -53.86318 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4be0341-9277-30eb-8af6-72065220b3d1 | -2.89419 | -54.15747 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff898362-1fab-3126-9b01-ef1399cb06e2 | -3.01045 | -54.13209 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc6da3c6-e00b-3e04-bce6-5d49d6027233 | -2.92537 | -54.19809 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b35f66e-20fc-344b-96dc-7f1721dbccba | -2.8828 | -54.07669 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca159227-b7c2-3533-9b0b-1cea20042e9d | -3.78666 | -52.22276 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d2da1a4-3ead-33cc-8417-1dd3515cf323 | -4.37352 | -55.27789 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f08da60-2e22-350b-9f5b-254f93e47055 | -3.21308 | -53.88081 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77b40a49-e15b-3e03-b69d-c31fce4323d2 | -3.58791 | -54.53267 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6bab856-d204-3ee5-9e10-28b3663d586c | -2.77508 | -54.09199 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea9739d9-e071-33b2-b327-c51ec6a96f01 | -3.29496 | -54.07146 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 08d05b50-7925-330d-8438-4bd4c0e284fe | -2.88323 | -51.03492 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05c61648-efe4-322e-a4f3-9ab848875a43 | -3.53106 | -54.6342 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42916d77-9727-3f22-92c5-b37a19aee66b | -2.94642 | -54.19418 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61407939-c646-33b1-91a4-efb8383e1a54 | -3.04602 | -54.14475 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a3c336d-13e7-39d4-a395-7d1ed5c1947c | -3.10134 | -50.19733 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecce99b6-f9e5-30e0-a9c9-bde8391ff9da | -2.30972 | -57.08427 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c19b8d0-d684-3840-8ea5-37e0b9d16a89 | -6.31522 | -54.79992 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1daf04d3-33a4-3514-9d52-d5e3156140f0 | -4.13857 | -54.90596 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 925e79ec-2f6d-3fbe-b6c1-cfcf13040327 | -4.23651 | -49.98285 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5b40fe8-9571-3ce3-a29e-4fef2784a212 | -5.96043 | -55.35679 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efddcf67-5e47-392f-a3eb-003cd2814438 | -3.29286 | -54.06768 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 26f585eb-587f-3323-bfd0-190dd91f22ec | -2.94299 | -55.7883 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecaa0d16-6893-3821-81da-a847c53b2d8b | -3.51403 | -54.6564 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5f36292-bd61-3442-bc90-1adc7f3deb59 | -3.61467 | -54.60083 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec7dec42-cbdc-3bd3-85c3-ac2be492c25a | -3.53373 | -54.64158 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README87.md)
