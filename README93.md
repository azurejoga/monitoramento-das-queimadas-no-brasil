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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 899afb96-12a4-3207-9695-bbacf9056584 | -17.89174 | -57.31761 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 7fb5419b-c5ef-3f55-92c2-5d89923058e4 | -17.889 | -57.31342 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| a15046e3-1239-3d06-8660-14e23eeed467 | -17.88843 | -57.31704 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| bf73d74b-28f3-36d6-a1c1-4cfe3227f0d4 | -17.88569 | -57.31285 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 702e4e37-0ea6-35cb-aeb6-e576f93ae5fb | -17.88512 | -57.31647 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 2f6c4566-305e-34f0-a2df-41c94f9cff52 | -17.88296 | -57.30865 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 9b7048e0-5075-3dc1-8eaa-792ae20adc3f | -17.88238 | -57.31227 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f9a03217-38bd-35d7-b379-02a12ac9b261 | -17.87908 | -57.3117 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| e55c913b-fe15-3cda-94aa-7ffa839985e6 | -17.8785 | -57.31532 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 670a531a-8b06-3a84-a5ad-5a21f35396da | -17.87792 | -57.31894 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 0519e4d5-f95d-3c93-8177-a5fae64e63d8 | -17.87577 | -57.31113 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1ebc9610-816a-3b98-b8ed-5fd314b5d886 | -17.87519 | -57.31475 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| d3ee7a87-87bc-36c0-a2ed-b42fc46ef095 | -17.87188 | -57.31417 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 55d6016a-e841-35e0-8148-2c6bd5700112 | -17.8713 | -57.31779 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.9 |
| b70b8139-291b-3212-9e4c-453a4b7ea366 | -17.87015 | -57.32503 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b88996ba-b3e1-34e5-a0c5-3c21e5513bf6 | -17.86958 | -57.32865 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c904aafc-d6e6-3330-89e6-eb4f2417f184 | -17.869 | -57.33227 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| be1d340f-d489-3768-b293-c0ee527e9c2e | -17.86799 | -57.31722 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 5d87f0be-2cbf-3a4f-9b0a-ebeb1336e73c | -17.86684 | -57.32445 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9f33921a-5828-3fc0-9d2d-cdf879663700 | -17.86627 | -57.32807 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a31a8262-52ad-36d6-a1f9-a7bd92f74920 | -17.86469 | -57.31664 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 749480f5-b100-34f8-84a1-40185d263018 | -17.86411 | -57.32026 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 4506dcc3-8657-354c-87ef-68fede3515ca | -17.86296 | -57.3275 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2442c6e9-0620-3b73-941a-743b48c1edfd | -17.86138 | -57.31608 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0e71ec62-6562-3fed-92c0-22391207ccc7 | -17.8608 | -57.31969 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 49305a0f-d510-3f44-82c9-9aaa73acb332 | -17.86022 | -57.32331 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| c7102b4d-6b13-3384-b9e7-d260b6f59bbd | -17.85965 | -57.32692 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2121e8d9-efea-3624-8631-a4c5e87e4548 | -17.85907 | -57.33054 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 35c9e526-b896-3ae4-935d-654c3eec9d9a | -17.85749 | -57.31912 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.3 |
| 22cf4776-4367-3cbb-bd98-ab36e5312626 | -17.85691 | -57.32274 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.3 |
| 025e54ff-97ec-39c5-a589-e057fd04d88d | -17.85634 | -57.32636 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 6d0f0b1b-ac40-3fde-ba39-84d835e7070a | -17.85576 | -57.32998 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 441a9e15-7873-3a1c-be95-317646be49ff | -17.8536 | -57.32216 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.3 |
| f6c26ed9-d762-3b2d-8a69-a05d1fded7ea | -17.85303 | -57.32578 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 4bef1716-7954-3ef1-aaad-891abf134f45 | -17.85245 | -57.3294 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 6151df4b-af6a-3295-bf37-259decbf1009 | -17.85187 | -57.33302 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7fea8488-2a28-3620-af08-84298f30c197 | -17.85029 | -57.32159 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 10bd4838-42fe-35c7-ab1b-9e69c3c06153 | -17.84914 | -57.32883 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 0aeca7ef-58fa-3704-a13f-dc61e98052fa | -17.84856 | -57.33245 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0e96541b-a7c6-36ed-a1b6-d30e4296f299 | -17.84698 | -57.32102 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8e9b0c94-78e5-37be-848c-c461989e0495 | -17.84583 | -57.32826 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 53f0e832-d8b1-357c-bcc4-ac9617125a98 | -17.84525 | -57.33188 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9da65845-73a6-3678-b195-23f5562183aa | -17.84252 | -57.32768 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.6 |
| ac00ea72-d712-38eb-8502-7c9c186df363 | -17.83475 | -57.33377 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 2df64b66-1678-3f38-a2a7-1e04602bfa2f | -17.73299 | -57.09682 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| aebd3fe2-5485-345c-b10c-0994e803f3e3 | -17.89548 | -57.33686 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 01b07a03-b139-3220-91b7-dfd07b8b8260 | -17.8949 | -57.34048 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| a0dd2dcc-1a40-3d0b-a6f3-0b9766c4c65f | -17.89159 | -57.3399 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| daf52cb5-0f92-32de-b326-8d21345fd25b | -17.89102 | -57.34353 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 3cf22f0e-5e65-3f5b-b8c3-a457ee550cfc | -17.88828 | -57.33933 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 6b8272f3-6d72-315d-8791-365730a18271 | -17.88771 | -57.34296 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 0fc33310-d83b-3b54-9565-0f36d29a5b80 | -17.8844 | -57.34238 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 77bea926-ef74-3529-b411-f58c9cf80f44 | -17.88382 | -57.346 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 46158fde-d8f5-320a-9305-da4c52f63319 | -17.88109 | -57.34181 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 86e0dbf5-1f50-3808-9425-c35d9286bd63 | -17.88051 | -57.34543 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2d8e7215-5def-38fe-9d52-c2a28088289c | -17.87835 | -57.33761 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8b76cb85-7b09-3c5c-a9be-2a58c08b02cc | -17.87778 | -57.34124 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 94bd9344-8a2d-3780-8f8a-e7e3ae6c7308 | -17.8772 | -57.34486 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7b753555-9d42-3de7-8abc-02c35a83b703 | -17.87662 | -57.34847 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2f73e895-7397-3048-834a-9634e7aea7f1 | -17.87331 | -57.3479 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1b4dd3fd-2b5a-387a-8603-0e5fb6e3a63a | -17.87274 | -57.35152 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c1027920-6ed1-3bc3-b1af-c8fc604c22cc | -17.87173 | -57.33646 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 90b8b1be-ae72-334c-9478-c04c659e23e5 | -17.87116 | -57.34009 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4c16012a-e1f0-317b-bcc6-4af17f2f2e03 | -17.87058 | -57.34371 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 63a8abcc-4bb5-3e27-bcec-f40368e0e652 | -17.86943 | -57.35095 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b0edcfa7-cb00-324f-98ea-800454d84e60 | -17.86842 | -57.33589 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 44c384c9-fa23-3d78-965a-9bc0fbbc72c2 | -17.86727 | -57.34313 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 51c37a90-ba93-39cd-9972-043e91a5c07a | -17.86669 | -57.34675 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ff3e9313-bd7a-3e6f-89ba-7c39a5d0c6ee | -17.86612 | -57.35037 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 6018f868-be76-3c7d-abb3-bda36b8ad9e9 | -17.86554 | -57.35399 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 023bbee0-f98b-3853-9dcd-2f3128608ac7 | -17.86338 | -57.34618 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b05eae0e-e434-3b97-854e-c01b84eeef16 | -17.86281 | -57.3498 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 5c85fb7d-d8e4-311f-aaec-6e60b0aff319 | -17.86223 | -57.35342 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 1f2bafea-c788-3a39-a615-0d0b8a946a05 | -17.86123 | -57.33837 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 90c0ca00-9ca7-3c58-a797-be2bccb0227c | -17.86065 | -57.34199 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 31365d37-209c-335c-8ef6-d836d92ac028 | -17.85892 | -57.35284 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| beb855e9-b83c-3e6b-bae6-ee9c31b7955e | -17.85834 | -57.35646 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| fa544445-04a9-3117-b354-1c1c0b6ae6d9 | -17.85734 | -57.34141 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3ea6d878-4937-395c-81b6-28313a9a1ead | -17.85561 | -57.35226 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| dadedad3-65bc-3bcf-86e1-b33658e98d68 | -17.85545 | -57.37458 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 73fc8469-8513-3156-b371-219a7b3e7a53 | -17.85503 | -57.35589 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| f3a404ba-1ca7-3bc2-aff0-e69c3a0e7edc | -17.85487 | -57.3782 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 486e8df5-a047-3c9b-aa66-228e8713a9ad | -17.8523 | -57.3517 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4e70c50a-f288-301e-aaa3-38ab5db548c5 | -17.85214 | -57.374 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| a292d503-8eca-3cec-a045-d57f52b6c26b | -17.85172 | -57.35532 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| cf24c636-5a8d-3bdb-95b1-21ace9ea1ae6 | -17.85156 | -57.37763 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b15654e6-eecd-3d3c-9bce-43bafd82c97f | -17.85114 | -57.35894 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| d1b38d98-d462-371c-a853-b485bd9718a7 | -17.85098 | -57.38125 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 40082f15-30d6-31c0-bd9c-dfe82e176509 | -17.84956 | -57.3475 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4406c521-d69a-3c33-82c7-d8ccdaafa7cc | -17.84899 | -57.35112 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3a969cc9-9597-3e7d-83d1-20dd3ddecd78 | -17.84883 | -57.37343 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| ebed8376-2ee1-364f-8cda-c72d440251e4 | -17.84841 | -57.35474 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 81d76f70-1446-3978-b5e7-30be96ebff7b | -17.84825 | -57.37705 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| dcda7dfd-d3c5-36ed-8497-13e6afb64d39 | -17.84799 | -57.33607 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 15f4be22-a192-3c98-8f4e-4923df3f2339 | -17.84783 | -57.35836 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 9d249b8e-25d7-3185-b8e6-18f50d291a43 | -17.84767 | -57.38068 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a9bd8ca1-1373-33a7-86de-dfdc4c3b3acb | -17.84625 | -57.34693 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| dd28a2c0-ff0e-37cb-a659-54a91c4b5a85 | -17.84568 | -57.35055 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8d0e250c-3ed2-3d65-ac04-8e52f492d3d1 | -17.8451 | -57.35417 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 1b113f89-6fe0-3059-9226-18080956c4e9 | -17.84494 | -57.37648 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |


[Clique aqui para ver as próximas entradas](README94.md)
