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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 679712e1-8193-3ab1-88d3-efac878f7ae9 | -12.96881 | -62.6723 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a71c3d3-5d24-38e3-9eb4-8b0fad5e89fc | -12.9678 | -62.78938 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de120825-6138-33b3-ba3f-269cd3ab9db9 | -12.96437 | -62.67893 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3fb1027-9110-383c-a2cd-7a78b367f58a | -12.96326 | -62.6861 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e6acdac-acbc-34d3-97d3-664a6693f50e | -12.96106 | -62.70043 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7b7b064-4dfd-3c55-b1a2-3fe2aeacaa98 | -12.95883 | -62.69273 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aadc3449-4e33-3af9-ad06-b9df6311d5e4 | -12.95713 | -62.65941 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7641b363-d1b4-3614-a595-8868463579a7 | -12.8924 | -62.79194 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ede3db9-dafe-357d-b686-702dc139b790 | -12.88798 | -62.79855 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03ea1235-d462-3a64-9e36-c6fb731bef11 | -12.88466 | -62.79802 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46c0be24-d2cb-3668-b917-470ecc704008 | -12.86971 | -62.80658 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7af3eaba-c1d0-35e7-b6ec-018da40e0f0a | -12.82597 | -62.9164 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74e84bad-59a5-38d2-bf9a-f9fb2150676a | -12.82493 | -63.01074 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c7f8129-e493-35fa-b3bf-0cd18ad06536 | -12.82265 | -62.91587 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df6cb874-bf40-3731-84ee-2d3b7c25c488 | -12.82161 | -63.01021 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86bb8aac-4c63-3ec6-a6b8-9769640fe052 | -12.81933 | -62.91534 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba5d0b26-b1df-34a1-8fc2-33e059735173 | -12.81718 | -62.99497 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a472ba66-5af9-3efb-a583-c97f6445f773 | -12.81601 | -62.91481 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 407cf6fa-ca24-32d8-8a16-bac2bd602178 | -12.73537 | -62.86532 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4423c0c3-23d4-37a0-acea-7e1a9984ebbb | -12.6984 | -62.97207 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 983aa669-b24f-3e3d-a740-52221170c1db | -10.64957 | -64.37303 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abf816a6-8072-3679-b721-86307797fc59 | -10.64737 | -64.36524 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6245c732-eefb-3bfe-b61c-2ad07a293b13 | -10.64679 | -64.36887 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7219940c-fbe5-3921-9a29-0beb10115408 | -10.64306 | -64.43524 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 133afe19-e31f-3329-8de8-15c1b146f2e5 | -10.64249 | -64.43879 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fdd62399-1d76-3be6-bccd-5a42017c68cb | -10.6397 | -64.43463 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3306dfff-52c3-36f5-a942-5db47591f45f | -10.63913 | -64.43816 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4acbd661-da30-3262-b8cb-a9bd6613ca10 | -10.63578 | -64.43758 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 708c4ebe-5a6e-35a1-b54b-f56cbf038497 | -10.63242 | -64.437 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bccfb4b-c327-3a0c-9e6e-47e30e9c8c82 | -10.63183 | -64.44066 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 915b68ab-636e-3064-9e64-0cf61940c06f | -10.63124 | -64.44436 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be76a101-09de-35e6-a118-7bc070367637 | -10.63065 | -64.44807 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc1c91d9-0158-3950-8328-397f7b11a49a | -10.62199 | -64.39463 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59949cb6-4907-317b-bf90-e35e885ca8e2 | -10.61863 | -64.39404 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ade4e0a1-2585-333f-b471-0d79af030021 | -10.61192 | -64.39288 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b00ab05-8eee-320a-9750-00389bcf53b6 | -10.60857 | -64.3923 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 713ede5b-ff49-354f-8e22-ed7207f5451f | -10.60521 | -64.39172 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a4398d1-12e9-35be-a526-2a0c715a0635 | -10.60464 | -64.39531 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dfaf4fb-05f7-33b1-a5a0-7f91a50621ac | -10.60258 | -64.53664 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22867490-10ae-3980-a8e5-d9011297886d | -10.59863 | -64.53971 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf1ca885-715a-3d2b-ab3f-e59e8261e70f | -10.59187 | -64.53872 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8155826f-61b4-33be-a759-f289b56df312 | -10.59043 | -64.5048 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16cb9e2f-e80e-3544-9a90-c0a27af2e5c5 | -10.58983 | -64.50849 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa340a7a-fe84-3c0f-a0aa-f3d8f572b802 | -10.58706 | -64.50423 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f0be88a-4691-3529-9943-ef8bbbcfae6a | -10.58329 | -64.48479 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 126f2ee6-f9de-3917-b350-96232ae13d53 | -10.58051 | -64.48059 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 158a4130-5b94-3b49-a511-84f54a5d43b4 | -10.58016 | -64.52554 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f94483fc-bc4b-3761-b570-b8c567623d77 | -10.57992 | -64.48425 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aff031f6-83d6-39fb-a158-e6a42c91b76c | -10.57739 | -64.52123 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a73c0c82-10eb-3ba1-84b5-11a814f0a9d8 | -10.57714 | -64.48008 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2309c641-fc44-3559-ab24-4f94f725c1a6 | -10.6981 | -64.11215 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d54c8b8-8807-3e3e-a19f-125d61f6d030 | -10.69695 | -64.11935 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a916de01-0697-31f7-8142-7f4dbd21addd | -10.69476 | -64.11163 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71636e2c-b1fb-34b9-a6eb-7dcf107fa37e | -10.69419 | -64.11521 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ce16d1f-0312-3ecc-b392-ee1a959f83e9 | -10.69411 | -64.1372 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6929c17e-1ab0-3163-8f9e-46d0eba9e2eb | -10.69362 | -64.11881 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 869290b8-91ab-35c8-a422-55d2dbe60489 | -10.69142 | -64.1111 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd3c16c0-80c4-3239-a5f6-6a687f6e25be | -10.69134 | -64.13309 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c090aa43-e75f-3222-b3c3-9623845b9007 | -10.69085 | -64.11469 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdacefb9-80af-32a6-ab45-5b319cc8b036 | -10.69028 | -64.11828 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 429af264-dfe6-384b-943b-d4fe6c764486 | -10.688 | -64.13254 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43de220e-4e4a-34da-a34c-16ad32a2ce1d | -10.57336 | -64.04031 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 156cdf3a-58a1-343a-861d-bb5d0ec89d3c | -10.57002 | -64.03978 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32679d7b-4914-3bb9-b8e6-d71c1f87c761 | -10.56726 | -64.03568 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b535f8f-8a37-3b26-9575-d3f6b023fc8d | -10.56506 | -64.02802 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d464fb92-fe62-37a1-a293-213d3c78dcb2 | -10.56392 | -64.03517 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7688d63c-6187-38de-bf67-22f5f0ea31c4 | -10.56115 | -64.03105 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb3ca6c0-42a3-3c9a-a509-d6beae3f4d5a | -10.56058 | -64.03464 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c27d6fab-9383-3315-baf4-0d0add32d334 | -10.55838 | -64.02699 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cc4f73c-cdce-3fcf-b9e5-3b56cf2e5e81 | -10.55724 | -64.03411 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5385554-1aba-3f5b-9c71-f6e6ea28d7aa | -11.94788 | -64.37156 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 754ebab8-c7c5-3b06-87b5-6508f5610fe2 | -11.79886 | -64.28062 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f39217e-f3ca-38a7-84b3-b2d603b57c85 | -11.79829 | -64.28418 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6401ed5e-670a-3859-a4f6-8406201c505b | -11.79772 | -64.28774 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15cd3363-2db9-36bc-8c25-06abe951f361 | -11.79128 | -64.24273 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d83ed85-3edb-396c-bac4-0426db89ee95 | -11.7907 | -64.2463 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eac71d8-e972-3164-8a31-51241a94a912 | -11.77542 | -64.2987 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19ca4dc0-f455-3891-bc6b-a6da3d582050 | -11.73221 | -64.29602 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a32954ba-0099-326f-a24d-c251f4846359 | -11.72888 | -64.29546 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cf9850d-aa6f-3d11-9ae7-e511dbf5dc81 | -11.7283 | -64.29904 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6af2e182-7965-3deb-888c-f9e94186ceaf | -11.72497 | -64.29848 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87086c2b-6130-3b85-8a9c-0f5bafde25d8 | -11.7244 | -64.30206 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b69532ad-2381-32aa-949b-9aec1d19513f | -11.72163 | -64.29794 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 752e4011-c7d4-30a0-a262-7a96c882c110 | -11.72106 | -64.30151 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dd1383e-89dc-3546-90d6-10dce3a8aaab | -11.7144 | -64.30038 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8ecc361-e147-332d-9318-6181c7de37e4 | -11.71164 | -64.29626 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d141ded-e665-3fd1-809f-c31d8e92477e | -11.7083 | -64.29571 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7670b4d-57aa-320a-9f8b-afd71b0241b0 | -11.70554 | -64.2916 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10d0869a-cdb3-33fb-af41-ac832ce83854 | -11.66186 | -64.24409 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e16e566c-9a74-39c9-9768-ee878c4b6adf | -11.66071 | -64.25122 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 048aac09-e2e7-36e3-a04a-64553eab0735 | -11.66013 | -64.25478 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43eb93ba-56ce-3ce7-813c-4ad9b60e69af | -11.65853 | -64.24355 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80c70ed3-8d66-3863-af30-5de86f099aa7 | -11.65795 | -64.24711 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a2d2581-2746-384f-842b-74ab741057e1 | -11.6568 | -64.25425 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6219f949-d568-3b33-a55c-a980f03ec468 | -11.65622 | -64.25781 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17c7af6f-7c5f-3c0d-93a5-1ca278dfe6b8 | -11.65078 | -64.25309 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79b55596-79dc-3024-b897-e09debae6bf2 | -11.42002 | -64.20773 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95fb3a08-5e83-378a-ba8e-469707fba1d9 | -11.41945 | -64.2113 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39aa4117-dad0-3edb-b814-2b84ad8487f1 | -11.41888 | -64.21487 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d918e616-198c-3b90-aaa8-6a464d8f45eb | -11.41726 | -64.20361 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README108.md)
