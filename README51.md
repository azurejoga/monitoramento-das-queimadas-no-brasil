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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efbeda9f-2674-34cd-9e17-82f1bbf96489 | -18.4264 | -42.26166 | 2024-10-19 12:12:00 | TERRA_M-T | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 00b53d34-f4d1-3db2-8c3d-84846d4ce144 | -20.24722 | -40.79954 | 2024-10-19 12:12:00 | TERRA_M-T | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 64a0c281-e98b-3b1d-ba3c-60941968e9f1 | -1.1163 | -49.0423 | 2024-10-19 13:05:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 36f7ecd6-547f-3361-a7e1-a7b8ffcafed8 | -1.1348 | -49.0421 | 2024-10-19 13:05:13 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 7763bfb9-8e5e-3547-a3b8-1f9b36d5f824 | -1.1163 | -49.0423 | 2024-10-19 13:15:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 53c59491-785b-3936-8789-3433db2f6f12 | -1.1163 | -49.0423 | 2024-10-19 13:25:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 93e8bc22-84c4-30d9-ab37-df577daa5f48 | -3.0388 | -44.4156 | 2024-10-19 13:25:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 26cf32a7-fb1f-37df-b943-a1f6590ec51c | -3.0389 | -44.3927 | 2024-10-19 13:25:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 267baf8e-0583-36ca-b6c1-c4704eae13dd | -3.0949 | -44.3677 | 2024-10-19 13:25:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 3e69394b-d0e9-392a-b048-5b60565c4af7 | -1.1163 | -49.0423 | 2024-10-19 13:35:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| de2caf00-08f8-3113-909d-91757a702799 | -3.0949 | -44.3677 | 2024-10-19 13:35:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 182bea99-c26d-3ea0-91e1-efcd0bd0e70d | -1.3778 | -47.3799 | 2024-10-19 13:45:14 | GOES-16 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6bb4648a-9a3d-3fc3-af1d-b3dee74d6053 | -3.0949 | -44.3677 | 2024-10-19 13:45:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| bf6785c3-d21a-318c-9057-2c96c59cea1a | -2.3381 | -54.3835 | 2024-10-19 13:55:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a584390c-4755-357c-a2d1-57f3428495ee | -0.84 | -48.6394 | 2024-10-19 14:05:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5596bd81-171c-3615-ac17-27a67197583f | -2.3198 | -54.3838 | 2024-10-19 14:05:19 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| bee10ece-3511-3566-8242-ba299f7758f9 | -7.3271 | -72.7538 | 2024-10-19 14:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f349fdc2-a58a-3dc6-8094-bd5cbbd64b6a | -0.84 | -48.6394 | 2024-10-19 14:15:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 44284e95-b13d-397e-a621-47cd20e5637e | -2.3198 | -54.3838 | 2024-10-19 14:15:19 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 810886d9-028f-341d-ac07-c33945999a02 | -3.5295 | -43.2187 | 2024-10-19 14:15:26 | GOES-16 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| fe22b6f5-9c32-33a5-876f-ed24ce8fc340 | -7.3271 | -72.7538 | 2024-10-19 14:15:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a6d9df81-eec0-391a-83c8-9e428ce19790 | -0.766 | -48.7042 | 2024-10-19 14:25:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 11d034c7-3988-330e-aa51-40171f39155a | -1.0792 | -49.1917 | 2024-10-19 14:25:12 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 94dafd6a-70db-360d-9b01-ab51e1386d2e | -2.3198 | -54.3838 | 2024-10-19 14:25:19 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8e120cf5-60cc-3388-bb18-62540cf22dcb | -2.3381 | -54.3835 | 2024-10-19 14:25:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1eda6331-6685-383b-879b-68064a419ccf | -7.3271 | -72.7538 | 2024-10-19 14:25:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 2562b951-00e4-368e-acd4-c64985836143 | -0.803 | -48.6397 | 2024-10-19 14:35:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 702d4c79-f076-35de-a330-f9b8f79e80b8 | -2.3198 | -54.3838 | 2024-10-19 14:35:19 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 00c7b04f-8c4f-30fa-b0e6-6e9089734cae | -2.3381 | -54.3835 | 2024-10-19 14:35:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c2b75343-aa1c-3377-a09b-6d859539c2c8 | -2.8556 | -53.3256 | 2024-10-19 14:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3ab0315b-1960-336d-9771-e7f7a6c44a30 | -3.4023 | -54.6792 | 2024-10-19 14:35:26 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| a712425b-f2f9-30d9-bae7-68a657a9fc66 | -7.3088 | -72.7539 | 2024-10-19 14:35:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 315a4605-7a37-3e3c-ab48-0e1a98bebe95 | -7.3271 | -72.772 | 2024-10-19 14:35:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b21f7bbd-d230-3452-ae23-7e81cbbbb070 | -7.3271 | -72.7538 | 2024-10-19 14:35:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| e099ef88-ee9a-3b9f-b567-33b1cbbd053c | -7.7127 | -73.0429 | 2024-10-19 14:35:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 449c3251-9a43-30f2-ab81-516df47aeb70 | -2.3198 | -54.3838 | 2024-10-19 14:45:19 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 367ed778-3864-312a-a820-d53cb10c2195 | -2.3381 | -54.3835 | 2024-10-19 14:45:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| eca5a80a-e854-36a2-8b60-04a5eda867ca | -2.8556 | -53.3256 | 2024-10-19 14:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 19096d9b-6591-3054-981b-6c2f0339333a | -3.6384 | -55.4291 | 2024-10-19 14:45:27 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3b3afe0c-e5d7-3a2c-bd23-f0de096a8a2f | -7.3088 | -72.7539 | 2024-10-19 14:45:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| cc9719a3-b1bd-3b7e-adca-c54938dd97d7 | -7.3271 | -72.7538 | 2024-10-19 14:45:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 65b03475-337d-3fef-9ad0-0f7718dd0826 | -7.3271 | -72.772 | 2024-10-19 14:45:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3d520c36-71c8-3f06-a558-d3b321f99501 | -7.86 | -72.8963 | 2024-10-19 14:45:52 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a0d254c9-585e-36d8-a547-b1d66c33d22b | -7.86 | -72.9145 | 2024-10-19 14:45:52 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 48.1 |


