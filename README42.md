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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc9b303d-68e7-36e2-9a56-a3238df77d16 | -11.3159 | -60.5392 | 2024-10-09 01:26:39 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d6975ca2-6e2c-3ccb-8810-4e866b3e469c | -11.2673 | -60.367599 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 095417fb-7a4c-326f-b21d-a34852d306cc | -11.2689 | -60.374599 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1d079e64-821a-3a11-91a8-428b8d7bf094 | -11.2704 | -60.3815 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da2cd2d6-612b-3427-9222-220339dd7f5d | -11.272 | -60.3885 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 527e082a-0a2a-3f0b-8377-906d12b97fc4 | -11.8997 | -63.2677 | 2024-10-09 01:26:39 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e68b92be-dc8a-3f78-b744-ecfb2d9a69d7 | -11.2544 | -60.3559 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b313239d-3e08-3b06-8371-f68ca2bf9296 | -11.256 | -60.3629 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb04903-f922-3de3-8a88-f895729e540c | -11.2575 | -60.369801 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b360e0c9-5e70-3215-98d5-ad7ae9d83dca | -11.2591 | -60.376801 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86d74814-ee22-3b21-b8c0-e66818a083e6 | -11.2606 | -60.383701 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65da53fb-705f-3866-becf-3ab00dd1d026 | -11.2622 | -60.390701 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef782c2-5c1c-3934-8141-a9bf712457bf | -11.2963 | -60.543598 | 2024-10-09 01:26:39 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 22ecc106-f42e-3871-8b6c-aa023d93e28b | -11.2979 | -60.550598 | 2024-10-09 01:26:39 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7443cd8-36d1-3b84-a487-00caded7225d | -11.2994 | -60.557499 | 2024-10-09 01:26:39 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 515a2e61-8e14-3569-8516-9a8354e3b1ab | -11.8881 | -63.2616 | 2024-10-09 01:26:39 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ede967e9-e38d-3f51-9de8-5e96b7f264eb | -11.8899 | -63.269798 | 2024-10-09 01:26:39 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bc0895da-ff86-31ea-b115-6db37d85c2b2 | -10.5959 | -57.523602 | 2024-10-09 01:26:39 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e455ee7-29a2-3bc9-ae95-3dae7d64169e | -10.5979 | -57.531898 | 2024-10-09 01:26:39 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2f2d307-136e-38a6-8fd5-e650d2c689ee | -11.2508 | -60.386002 | 2024-10-09 01:26:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f07eeab8-30d1-3fcf-b5ae-390592cc51a0 | -16.7067 | -57.4514 | 2024-10-09 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 864d16b5-ac8c-3e5c-815b-60ca44c60e27 | -11.2581 | -60.464699 | 2024-10-09 01:26:40 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fe14daba-9bd6-3190-80ac-62725c1545d4 | -11.2596 | -60.4716 | 2024-10-09 01:26:40 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fa61027c-8228-3fb4-b2fc-c36c4f1c7586 | -11.2612 | -60.4786 | 2024-10-09 01:26:40 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 592c392d-652f-3477-9079-84b96b299e36 | -11.2627 | -60.4855 | 2024-10-09 01:26:40 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e953dbd-2423-3f8b-a1f8-80b734509c1f | -11.2814 | -60.569 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9025c9ca-7b5a-37d6-8f80-2461fe8cfd8e | -11.2829 | -60.575901 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 071d780a-5c1d-30a1-bac2-b39a5fe4f585 | -11.7834 | -62.866299 | 2024-10-09 01:26:40 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 82d98506-0b0a-38d5-b582-fddd26e57d15 | -11.785 | -62.874199 | 2024-10-09 01:26:40 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b642a1c7-bf2f-39dc-af12-21e25ff1153d | -11.8703 | -63.273998 | 2024-10-09 01:26:40 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3bccedf-f666-332c-94dc-9de69a809874 | -11.2514 | -60.480801 | 2024-10-09 01:26:40 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ed448571-a29f-39b1-a1c7-2c1b74450a23 | -11.2529 | -60.487701 | 2024-10-09 01:26:40 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 53edc98a-9412-3c9d-a3eb-9bb2e1677836 | -11.2685 | -60.557301 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b18c86d-3157-30cf-a4f5-120809860530 | -11.2762 | -60.591999 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 70f198a0-537c-3bb3-b46a-6283ce4e4f87 | -11.2778 | -60.598999 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0bcf611f-cb78-31d9-a965-7bae297155ed | -11.7736 | -62.8685 | 2024-10-09 01:26:40 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bbf50ad0-897f-3c16-8733-2626a45ec67b | -11.2571 | -60.552601 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c74a3352-8efa-353a-be7b-c5eb566078c4 | -11.2587 | -60.559601 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2b864d93-930a-3f1a-bbdc-374ebc6f9316 | -11.2602 | -60.566502 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8c6aa912-090b-3c4d-a3df-81624a924813 | -11.7621 | -62.862801 | 2024-10-09 01:26:40 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 42dcbf0a-fad2-3a60-8569-1ca8f1955b61 | -11.7638 | -62.870602 | 2024-10-09 01:26:40 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6780c5f1-9b00-3ad7-9b26-ec1362e5e26f | -12.1505 | -64.707703 | 2024-10-09 01:26:40 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2991e194-1bca-372e-a885-bb84e856f0bc | -12.1525 | -64.7174 | 2024-10-09 01:26:40 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b95de6db-e770-37f4-84f2-5132b72e16cc | -11.2318 | -60.485298 | 2024-10-09 01:26:40 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b2b92fe6-a2d3-34b0-be22-009a8d3e11fe | -11.2473 | -60.554798 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 25f033c0-d5e1-3c29-b43c-8e061f56c720 | -11.2489 | -60.561798 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 81d46579-0099-3f7d-a22a-1ec8723ed6ba | -11.2122 | -60.489799 | 2024-10-09 01:26:40 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 66903986-2d40-312b-8a85-125f09b58d50 | -11.2262 | -60.552399 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a5c93040-ef5b-3868-9853-ad8f15338062 | -11.2277 | -60.559299 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b17e12f-7b0c-33af-9359-3fb8dcc81cbc | -11.2293 | -60.566299 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 73104b3e-955c-37e9-8d9a-755c7b0f9f69 | -11.2324 | -60.5802 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 348694fa-c082-3eca-bfed-0478e105768c | -11.2339 | -60.587101 | 2024-10-09 01:26:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 416b077e-b349-314e-8c96-6f2d7cb8d0fd | -16.7846 | -57.4629 | 2024-10-09 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 2c2cf318-f4e0-3948-96fc-19e58679fccf | -16.7575 | -56.7081 | 2024-10-09 01:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 315dd66a-ce96-3c6c-9e88-b9727f8d637c | -16.777 | -56.7057 | 2024-10-09 01:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 2ada2565-9326-3c75-8d8a-dd9fbc98ed89 | -16.8743 | -56.7352 | 2024-10-09 01:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 4f1f879e-1939-38e5-94fc-a6426704e8c8 | -11.19 | -60.436401 | 2024-10-09 01:26:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a265693b-d7ed-35f0-a453-5af51d0d614e | -11.1802 | -60.438599 | 2024-10-09 01:26:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7dfad954-e324-3ef2-bcd0-8b22e74b488b | -11.1817 | -60.445599 | 2024-10-09 01:26:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c4bdf6e1-caf8-35a9-ae59-700ff0ea2344 | -11.1833 | -60.452499 | 2024-10-09 01:26:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b0b5d234-b405-3980-8b2a-62a40105161f | -16.9609 | -57.4426 | 2024-10-09 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.0 |
| 4b78c00b-6958-34b7-aec1-93c943db3b42 | -17.0878 | -56.8534 | 2024-10-09 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 6f802093-8605-318b-b02d-6dba2030b85a | -11.1715 | -60.630501 | 2024-10-09 01:26:42 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7e5aa74f-6c53-3b9a-afe6-284fa89472cd | -11.154 | -60.598 | 2024-10-09 01:26:42 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e88efa7c-cc69-32dc-b924-3c689d362e20 | -11.1555 | -60.6049 | 2024-10-09 01:26:42 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0831d6-a58b-3f32-81a5-3a1e5f831489 | -11.1617 | -60.632702 | 2024-10-09 01:26:42 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 43a82bdf-f17e-32b0-80e7-388b24ba0b39 | -11.139 | -60.623299 | 2024-10-09 01:26:42 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f8c1d16b-4a7e-37c6-8f24-eb14f766ec9e | -11.1406 | -60.630199 | 2024-10-09 01:26:42 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86b0fd3c-b1b7-36ff-bbec-88d4d61a03cc | -11.2385 | -61.1647 | 2024-10-09 01:26:42 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d7158c7a-e241-36e7-b00c-4f9e27ee0d90 | -17.1271 | -56.8486 | 2024-10-09 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 0891bb99-e0f6-3617-97c6-2321819196c0 | -17.1467 | -56.8463 | 2024-10-09 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| be88af0b-ef22-3f7e-b48d-ad837ca16edb | -17.1588 | -56.1222 | 2024-10-09 01:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 0dd96b67-714c-3c0f-a7ac-dd1a170456cc | -17.335 | -55.0366 | 2024-10-09 01:26:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| 85cfc93d-3fa3-39d4-a208-2bbd91d6f8fd | -17.3353 | -55.0156 | 2024-10-09 01:26:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| bf9f3e73-6415-3af9-b609-2812c14c363b | -11.2256 | -61.152901 | 2024-10-09 01:26:43 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 29c32987-1701-3b2b-9f61-10ebcef55dc2 | -11.2272 | -61.159901 | 2024-10-09 01:26:43 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4b6461d2-ace8-3aff-8f4c-f6287697c83d | -11.2287 | -61.166901 | 2024-10-09 01:26:43 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca170a7-72e9-396f-b61f-2fd74a8548bb | -11.2169 | -61.206402 | 2024-10-09 01:26:43 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e827644-096d-3c6b-8bef-ce3ed6c970e7 | -11.754 | -63.7896 | 2024-10-09 01:26:43 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5d4a334c-b16b-3469-ab22-9758c59f6e8f | -11.7559 | -63.798199 | 2024-10-09 01:26:43 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77722a69-ceec-3239-a6d8-680e03a05d24 | -11.7461 | -63.800301 | 2024-10-09 01:26:43 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5af425ac-8b75-33ce-bb17-2e5c83fd3889 | -11.7479 | -63.808899 | 2024-10-09 01:26:43 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cba680ca-121e-3c24-ac3b-15973565e80a | -17.3551 | -55.0129 | 2024-10-09 01:26:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| b478d046-bda9-3f62-a953-f279a4d625a6 | -10.3301 | -57.490002 | 2024-10-09 01:26:44 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 576dfd99-2fce-3abf-95d1-d42e22c025c7 | -11.7486 | -64.055496 | 2024-10-09 01:26:44 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 15acf1d5-5065-3690-af8c-902f07d01435 | -11.7504 | -64.064301 | 2024-10-09 01:26:44 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8415789b-1afd-3f1d-a50b-a1100d144930 | -11.7388 | -64.057602 | 2024-10-09 01:26:44 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 58a50729-ad2e-378d-907e-9cc1c8905b99 | -11.7234 | -64.033096 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6de06a72-8cf9-3888-986b-7c73422cadbe | -11.7253 | -64.041901 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2849215-49eb-3b8d-bc8a-b0e0df90aec0 | -11.7272 | -64.050797 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 996ebcb9-e10a-3369-b807-46547ad84e43 | -11.7118 | -64.026398 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1dc69e52-793e-3850-87f2-4db0b63813d9 | -11.7136 | -64.035202 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65757382-ab25-323f-b6f8-0947760075bb | -11.7323 | -64.1241 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e80e509-cdc6-3c08-9f6c-973cf5e289d2 | -11.6946 | -63.993198 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff1ef77-fe01-3c78-bfd4-93581e2632f8 | -11.6964 | -64.001999 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c398cb8-f31a-3fa0-85ee-1f8984d90579 | -11.6983 | -64.010803 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dba39a5e-586f-3d89-ba6e-bc73dcb9a600 | -11.7001 | -64.0196 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2db4f36-21eb-3a18-b457-1923325a6429 | -11.702 | -64.028503 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 507f6c86-595f-3007-9e96-036dd7807259 | -11.7206 | -64.117302 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1e7567a-1d65-3402-99f9-c2ca8d23c8b6 | -11.7225 | -64.126198 | 2024-10-09 01:26:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README43.md)
