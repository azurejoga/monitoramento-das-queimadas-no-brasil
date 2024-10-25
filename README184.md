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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfeb8d0e-17a8-3037-b676-0762daf8d2ed | 3.46024 | -51.26254 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 232d9c28-995e-3740-880c-b4d72ba027c2 | 3.4597 | -51.26612 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aef5ac8-52bd-380e-b362-e1722b7397bf | 3.43209 | -51.27611 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7335aa72-4a72-383f-a0c4-f3ebaed6357e | 3.43154 | -51.27969 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1f8e51a4-a158-3e54-9e04-faad709b9449 | 3.431 | -51.28327 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5e28f396-4834-3e85-af42-37734853b46c | 3.42873 | -51.2756 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 45936f5a-4b72-3a09-bc4e-12609b837112 | 3.42826 | -51.30115 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd50d4a2-60ef-37a9-bfb6-e53e7c3c8b27 | 3.42771 | -51.30473 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d93d24dc-f5df-3da3-8155-b6e5705cfe62 | 3.42717 | -51.30831 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5f1c7a3c-efd2-38e8-a850-c4c893839e92 | 3.4249 | -51.30065 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b8ad001-a3f3-30f7-a6f4-54f3aba7ffc2 | 3.4238 | -51.30779 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 18fdc746-888e-3428-933e-46b11d1959a1 | 3.42208 | -51.29656 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6ff07a71-d4a6-3103-a8f5-07154e537c70 | 3.42044 | -51.30729 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6a7916e6-da20-356b-aba9-a93fc12a6cc5 | 3.41927 | -51.29248 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 02b933c7-e355-3268-a1cf-9822a3beb7ba | 3.41872 | -51.29605 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c06c2295-bb16-365a-acf5-e13d365b6f87 | 3.41763 | -51.3032 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1bf8f807-2c54-3db2-8455-a5b1af120caf | 3.4159 | -51.29197 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 01e3fafd-8259-326d-8ea8-0e0c28c89d0f | 3.41536 | -51.29554 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a0455bf2-abd7-3519-ad2a-dd2908516084 | 3.41481 | -51.29912 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5ea05352-9661-363a-9e88-fa53024533c7 | 3.35103 | -51.60508 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98bdc2e7-a563-3543-b44b-a10062f7e93a | 2.80082 | -50.93257 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7a317ba8-6281-3c2b-9615-a6287180eba0 | 2.79743 | -50.93206 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b82bba12-6fcc-3226-9b80-ede5f5540250 | 2.79405 | -50.93154 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 169f1946-8f7e-3f30-9a1b-a29153afe7af | 2.79066 | -50.93103 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cc37d0d3-7457-37ac-a412-df155115033c | 2.51258 | -51.0803 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 17.3 |
| dcd0baf6-5889-37fb-a56f-2a63e7778df4 | 2.49674 | -50.94498 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2ce7e6b-364a-3f6d-911d-6502e1a2f302 | 1.23789 | -51.28344 | 2024-10-25 16:54:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 077273ce-a4c8-3e71-80cf-edbdeb8cbebd | 1.23616 | -51.27247 | 2024-10-25 16:54:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 20.1 |
| cd51d9e7-1e90-386e-9a26-5fc1dac5e8cc | 1.23283 | -51.27197 | 2024-10-25 16:54:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 20.1 |
| d5172157-14e2-390f-9946-e13529671d4e | 1.10322 | -52.38742 | 2024-10-25 16:54:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 9283cac1-8e00-3255-a01b-73f5241f6839 | 1.03497 | -51.27637 | 2024-10-25 16:54:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89f657e5-745b-3898-88dc-c050de07112f | 0.91034 | -52.11098 | 2024-10-25 16:54:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3838f0b-066a-331d-9add-3afbcd47faae | 0.90704 | -52.11048 | 2024-10-25 16:54:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2dd1b78a-8fc8-32b0-a222-7b6988f7fa21 | 0.81591 | -51.99461 | 2024-10-25 16:54:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca696e52-4003-3fa6-9471-2809cfad3550 | 0.5333 | -51.59872 | 2024-10-25 16:54:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 86a464d3-77f4-3a12-81ef-35c3843831da | -0.6294 | -51.79886 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 57c71145-1d0b-3baa-b5c5-2eb2c28ce2cf | -0.58987 | -51.71717 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6b258670-5acc-3abc-b585-7f9840d0a51c | -0.58657 | -51.71767 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fe5c9cce-7171-3391-b3f5-5879b0fc3bce | -0.58605 | -51.71424 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 17.8 |
| c559fee8-f14c-314a-838b-188881d4a64c | -0.54974 | -51.71975 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 274f4288-9418-368a-9dd8-f8f055954bb9 | -0.54933 | -51.85385 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4106ad54-79d2-3018-8940-6df792a915b8 | -0.52953 | -51.85684 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1605d704-8942-3b5d-ad99-dd0c3a143ba5 | -0.52728 | -51.8642 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ee9263a6-d3c5-31b9-98bb-9c3325a334f6 | -0.52675 | -51.86077 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ee423b73-8324-3e46-8483-88154f5a4d00 | -0.43575 | -51.59742 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 281f94cd-57de-390c-a2db-9dfd20c4598d | -0.40623 | -51.7846 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac141920-ccbb-39e5-a3f6-5556334c4f4f | -0.40451 | -51.79538 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e41b948f-81fd-313f-97f9-e291dea12a40 | -0.40398 | -51.79195 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ac246c61-5ab6-31b4-9c5b-30b1fae74993 | -0.11726 | -51.83029 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 71b5a04e-4188-3c56-9976-71c2577d3368 | -0.58757 | -52.27998 | 2024-10-25 16:54:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 20.6 |
| d8be0e55-584c-3436-a244-166fd497d29a | -0.54558 | -52.58342 | 2024-10-25 16:54:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 5a59b953-5f1b-3499-95b9-1693c4fa9e9b | -1.63191 | -52.63949 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e51a0ea-7cc3-37f3-a32f-bafedc38b3b2 | -1.58097 | -53.31121 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4977b32c-cf16-3957-aafe-0c844e3376d2 | -1.57813 | -53.31537 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5fb0f113-6f09-344f-923e-684ccc8bfa07 | -1.57758 | -53.31172 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f4326bd8-ced6-34bc-9dff-8d6c58bbd025 | -1.57703 | -53.30807 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c20cf210-ae89-305c-a453-e216ff27f70b | -1.54795 | -52.15768 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 7f386b76-0e2e-3773-9277-bd6d3b9f6352 | -1.54516 | -52.16163 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 55e5aaaf-1e9a-332e-b39c-41fc3cecb1fa | -1.54464 | -52.15818 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 30518c5a-59d9-33d1-93ea-65979278eade | -1.52828 | -52.78454 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e935ca8-ad8c-3e08-9327-dfe88faa118b | -1.51369 | -52.59988 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 344e46e3-5aa9-3d53-b1d0-6cfedb3c27d6 | -1.47783 | -52.47676 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0cbfd7e7-9c27-3449-8600-35d8968c915f | -1.46641 | -52.35762 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f556eb0-1a69-34c1-bc46-67529af5b75f | -1.4544 | -52.78933 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8c0c751d-e717-37d1-99d0-45f916cddff5 | -1.45105 | -52.78983 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 87eb4d78-5333-397c-9652-a46bcc9f5025 | -1.44787 | -52.23646 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f2fce707-c336-31ca-95b7-97ef85ee8dbd | -1.44403 | -52.23351 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 70d39dac-ec98-3fad-9d52-d56786806ea5 | -1.4362 | -52.24883 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 509f2306-aa52-3aff-8bc0-2203b6ef8d47 | -1.43464 | -52.72747 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5316d79-8067-3ba6-a19d-39cb2692100b | -1.43422 | -52.45841 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e1e16c2d-ab80-32b8-a2eb-fe098cea2393 | -1.39103 | -52.95807 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cb698d5-90ff-3c0b-a30c-0e4658261c25 | -1.39053 | -52.28498 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 39945ace-7be6-353a-8d4d-0e9e4e524ae1 | -1.38549 | -52.29636 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b0c91143-0f74-380e-8285-bfc8090d713a | -1.36544 | -52.40918 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9efb19c9-3929-3e64-940b-082b53365c6d | -1.36282 | -52.30332 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 83fd769a-830e-33f7-a28b-434c5bb24697 | -1.26162 | -53.04007 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 40dad235-db33-3760-a1dc-045391cc1050 | -1.25826 | -53.04058 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 5b643d13-fdfa-347f-93fb-ebb94ae1b3a8 | -1.16577 | -53.14629 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| c1933e92-2855-3ebd-a2ce-405c7b6a17fb | -1.14851 | -52.10001 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4b499cf0-4b12-3a75-8c18-b658b0dffded | -1.14798 | -52.09657 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cd5a9904-193b-3fce-be24-55100287b691 | -1.14465 | -52.10082 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7791a15-54d7-37d9-915a-0c9b12682d26 | -1.10688 | -52.22985 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7ba122dc-2420-340a-a6c7-5a18f01a0125 | -1.10343 | -52.25156 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f99752d5-6ddd-3938-a1bb-a22b5190a697 | -1.1031 | -52.13878 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b60dbf8-fbe0-3d06-a986-d7fd6527c1c0 | -1.1029 | -52.2481 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b9f8ec51-e92c-31d7-88e5-c9e76d909cd6 | -0.93632 | -52.09084 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 244.6 |
| e63b7d92-1e6c-31a9-bb5e-ccdfd67ec110 | -0.93302 | -52.09134 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 381e5984-19b3-3338-ad18-dac472ca72d4 | -0.90343 | -52.07915 | 2024-10-25 16:54:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b88e4ffb-b1f2-3959-aea7-111ded2a4c50 | -0.89675 | -52.4116 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 176136c3-873b-3f81-95bc-61585a2089bf | -0.89622 | -52.40814 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 11ef3927-72e4-3bb8-93e9-678c0d87efe0 | -0.89343 | -52.41209 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| cc080c7a-6e8d-37a6-9159-1555d578c0f5 | -0.8929 | -52.40864 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fb305af7-c12f-33fe-bb0a-51e395ada4d8 | -0.89012 | -52.41259 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5a7b26b1-24a2-3365-9119-ddbd51dc2c31 | -1.62422 | -51.85655 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7d0de1ca-a522-3ab4-b265-b23739128325 | -1.53247 | -51.92402 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 1c2c3571-0bce-3acd-9f8e-22c92b7a0c6e | -1.53194 | -51.92058 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 782d9a75-7b61-38f6-860f-e3f156f4fa20 | -1.52916 | -51.92451 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a771f54d-a12f-32d5-b5b8-7e3891047eaa | -1.52864 | -51.92108 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 59a40de2-0b69-3e61-a228-45f22ae1b1cb | -1.52293 | -51.95007 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8c403bd-3646-3e66-b0c0-77aa5387a1a5 | -1.48785 | -52.00814 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |


[Clique aqui para ver as próximas entradas](README185.md)
