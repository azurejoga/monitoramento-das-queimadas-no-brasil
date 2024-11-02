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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c5169a2-a8b3-39e2-86e5-e5c02a358fdb | -2.80184 | -49.33216 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c348623a-22c3-3714-8cfb-c2661ca7a8db | -2.80068 | -49.33981 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfd3ce56-dc82-3660-9da7-78f451e55060 | -2.79823 | -49.32769 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8ddc1b6-db87-3d6f-b428-431246395965 | -2.79765 | -49.33154 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39a8c76c-0f29-330e-bb38-01edae1860d2 | -2.79707 | -49.33534 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f02944d5-60e6-308f-9849-e3e2569ee7b4 | -2.79345 | -49.33088 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e984c6a-84b2-3c8a-a1f6-2adb2b4043c1 | -2.79288 | -49.33471 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ab6193a-4f39-323a-9437-749d8d10bf0d | -2.7923 | -49.33853 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e72fc8d9-36c4-36df-bd3c-7f76fc66dded | -2.73761 | -49.30246 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02d67615-ec5c-3933-bc84-0e357d6c5223 | -2.73704 | -49.30631 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48d4914c-5da8-3f92-9ae8-e3106bfc6d0f | -2.73645 | -49.30366 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 212c6b7a-4d9c-3931-ba26-b735c1997b4c | -2.71422 | -49.28057 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79cb7665-d822-3593-b61a-e355f633d860 | -2.71362 | -49.28445 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20711e5d-ffaa-36b4-b046-66704f81ce3c | -2.71303 | -49.28833 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe39892b-0306-3dd2-af8e-819033b8d10c | -2.71244 | -49.29218 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fa1c3e5-b608-3f95-9191-cbb5baab2933 | -2.70884 | -49.28766 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cccbd50f-cd2a-354c-b844-b70449517d21 | -2.70825 | -49.29152 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3b6f22d-6781-3ebd-bcff-aaa2cc9240e0 | -2.70523 | -49.28312 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb516bfc-bf22-3cd3-a9e2-49a87bc3175e | -2.70405 | -49.29086 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f7158ac-61f4-35ac-a452-be77c2f75008 | -3.22984 | -50.18816 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17190901-21ce-300b-ad63-735abdef9e5a | -3.22948 | -50.58803 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c735d037-8ee9-35d2-807d-25af2a011021 | -3.22932 | -50.19159 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec2de3ea-c16d-3cc5-8270-9ba9dfac6973 | -3.21219 | -50.30356 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4643414-107b-3238-aebd-1fa583113096 | -3.18529 | -50.59122 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db9ada87-fbac-30e7-8241-6bc8b567456f | -3.18426 | -50.58965 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6302078f-908e-3ff6-9477-2a28bb36fd3f | -3.18284 | -50.58084 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f596ff2b-d9b2-3d02-b6de-bd49b37acc98 | -3.18212 | -50.58573 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd549f91-585b-350f-8155-3b0cded295f9 | -3.18188 | -50.5793 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 195afcdd-06b4-334b-874f-b6d87230171d | -3.1814 | -50.59062 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4ca78c7-ec01-3967-b8d1-96fe8b254608 | -3.18113 | -50.58418 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e56eaf29-626e-372d-aaeb-370232859101 | -3.18038 | -50.58905 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e64b959-7bc7-3f9f-80ff-1c9f77d18d22 | -3.17725 | -50.5836 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ec6c05e-15c1-3dc5-97b1-3313a4eeb0a1 | -3.1765 | -50.58846 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d199c87-9276-3116-907c-4207ce6e549a | -3.17336 | -50.583 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e56ce49-a931-35ae-b06b-46f11a020626 | -3.17261 | -50.58787 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fe0e248-5ac7-3fa4-b70c-de7180f825df | -3.16873 | -50.58728 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fd1e765-5d86-3da2-8855-070d35ada5c1 | -3.14455 | -50.35016 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f56c14d-c03e-3b05-9916-9bc444d3e69d | -3.14379 | -50.35524 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9faf4d7-4f78-30cf-be91-317f82afad92 | -3.14061 | -50.34954 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89e93c5c-692b-3687-b794-7821960fe037 | -3.13985 | -50.35462 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7e4b376-2d89-3ff2-9f78-a8eb97ecf85f | -3.12549 | -50.42416 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f3090b0-384f-3c3f-8369-d403218bcdae | -3.09782 | -50.47583 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edc9f1b1-6f04-3984-b046-c727d6ea4162 | -3.09704 | -50.47816 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f12b60dd-f3ab-39e4-916f-d0b57d557af7 | -3.09465 | -50.46774 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8713666-1aa8-3614-b685-e61f630c22d9 | -3.07726 | -50.23847 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23bb4bc3-4408-34fd-b688-f6c22b7f473c | -3.07406 | -50.23282 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0434ec47-a9a2-34b4-b020-202f6b999cab | -3.07372 | -50.49986 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab38326e-4e48-3d09-9eac-146255d29cc4 | -3.0733 | -50.23787 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c14a40e-3f23-3f99-b44d-6db80ea87aab | -3.07009 | -50.23222 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 18705c92-54b0-34f8-823f-e04ab46873f6 | -3.06933 | -50.23727 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc28c917-f78e-36de-a333-2a1efa7bf328 | -3.06517 | -50.50359 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c371767-9607-3a73-bdef-e4a460c13496 | -3.05812 | -50.49751 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7cee7df1-ab09-35d9-b01e-369703b83f01 | -3.05737 | -50.50241 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ed90e799-e41e-3049-b17b-f5ea48f2f3ca | -3.05662 | -50.50732 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 387f8f33-010e-3d4c-91b3-6b4c9261dd5d | -2.98016 | -50.48537 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92fd49f8-757c-3d43-a56a-6cac1ade9dfa | -2.97961 | -50.4836 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f216e92a-e525-3b0e-a749-0351b9a219db | -2.95994 | -50.29712 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 980c6476-9c42-3322-878b-c5b2982ba270 | -3.07318 | -49.57307 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcaa4585-5edf-3032-9a2b-26df41ed32fd | -3.06904 | -49.57242 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20df7ad6-ff2e-3896-a404-a5768f8a2389 | -3.06847 | -49.57618 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c45840e-714e-3322-8a69-86d5416ebd15 | -3.00097 | -49.55905 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65a98949-96b1-3163-afe7-9e54da1ae5f1 | -2.98895 | -49.52655 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fe1d969-9a88-386e-92e8-fc6e8def9b2c | -2.98539 | -49.52208 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 530d10bf-411f-3241-81ed-775545d88062 | -2.98237 | -49.51389 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72f7d97a-e352-36ff-b85b-0c0c0f1af284 | -2.97164 | -49.75076 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bfaa259-47d9-31db-b55d-8640328bcbf1 | -2.93537 | -49.42914 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 10a3140c-d19d-31ab-bc2f-524627b1bdd3 | -2.93481 | -49.43294 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38428b41-b77e-3d0d-b12c-cb3a88dd95c1 | -2.93433 | -49.42561 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ee3bc9c-39d5-3bab-996c-eac081acc89f | -2.93374 | -49.42945 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48e93246-9321-35f6-9d53-f31cf762d3e7 | -2.93177 | -49.42461 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 523a6c11-b8c9-3b38-b03a-4d59c29f41ca | -2.93016 | -49.42494 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 460434e4-2893-3602-9015-d4ae81d3e56b | -2.90429 | -49.51014 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c695c0ea-1b6a-3869-8c0c-9156b8b52e1c | -2.90129 | -49.502 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c7d786f-cf17-309f-a311-c2ae0941d1f5 | -2.90071 | -49.50575 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 922d931f-bf94-364f-8ded-762ae9a3b6df | -2.89713 | -49.50137 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c84e4d09-22f4-3679-829c-29b881f8490c | -2.89676 | -49.41986 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e22f5f2-531c-30a9-a71c-03b19068a832 | -2.89656 | -49.50512 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc5f4d4f-249f-390a-a7d6-f4a0b6e1cfb6 | -2.89298 | -49.50072 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49987eb2-1771-38a1-8cdb-47ed5d3cfe34 | -2.89259 | -49.41922 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b76b46ec-7ac8-38d6-92d1-8df8a732babc | -2.89241 | -49.50449 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4ec9a28-50f8-3f69-a875-1637f0bd3d6f | -2.89202 | -49.42299 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3cd8f142-940a-3930-b22b-643149d1f3f8 | -2.88785 | -49.42231 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 89f28205-c6c9-3d10-88fb-f1192bd64e6f | -2.88368 | -49.42165 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8298372-7b73-3dae-a417-d8d67c68144a | -2.85184 | -49.46346 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9a34d73-15d1-3984-aa57-baf11c0d5325 | -2.84577 | -49.86436 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0107d73-cc2a-39ce-a14b-c15fd294dd98 | -2.84522 | -49.86793 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a8c7156-c175-3b6c-9cb4-619d5fabef00 | -2.84374 | -49.48924 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b25a8c9-6d30-3aaa-baf5-f33eb583e573 | -2.83903 | -49.49237 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3aafac2-ab7c-3618-8a6c-d73d7ea4a8a9 | -2.83306 | -49.61746 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 619e4499-36e9-3067-b394-79357e10615a | -2.8223 | -49.77274 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 504689f0-e0f7-3773-9fcd-425469b02b33 | -2.81933 | -49.76477 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 229c6a4e-06f3-328b-984f-e6c6e3d9198b | -2.81878 | -49.76845 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed4cfd2c-47d0-328c-ad1f-0ff1b7828bda | -2.81642 | -49.40481 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b3ebd41-607f-3ff9-b368-dec4646dfddf | -2.81583 | -49.40864 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d74317e1-6df5-3b22-a569-1f444eb27e58 | -2.81471 | -49.76783 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88402789-fe35-3674-9c4f-9c0b69ff16f5 | -2.7803 | -49.55724 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d19aa0ab-bc09-37fc-a2f4-b1f7b4f206d6 | -2.77773 | -49.51866 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 663b3651-98f8-372c-86b7-cb02359812db | -2.77661 | -49.82809 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2207ccc7-b18d-3554-8ecb-06199497f623 | -2.77608 | -49.83168 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3037a94-7c29-3a43-b8bc-14310feedff7 | -2.76832 | -49.52486 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README66.md)
