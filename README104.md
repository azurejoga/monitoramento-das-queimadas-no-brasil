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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98fa5aa1-eedb-35e0-83b1-5f3a2f522302 | -4.88407 | -48.6679 | 2024-10-29 05:27:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0852528f-9241-3dcf-a872-0728bbecfea1 | -8.84141 | -49.86183 | 2024-10-29 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1f0be51d-e7de-36ab-985d-8aa065d48463 | -8.7476 | -49.78889 | 2024-10-29 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a78b2f0d-9879-303e-8d84-84cd9864e6f3 | -10.23224 | -49.69054 | 2024-10-29 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f27d281-f399-3674-ac77-69d2565ffb63 | -10.22456 | -49.6964 | 2024-10-29 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1362e56d-f681-31e4-a9ea-ac829b2146fa | -4.64955 | -50.46402 | 2024-10-29 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7e7c21c-f9bd-368b-8f6a-36f6daad7881 | -4.6489 | -50.46873 | 2024-10-29 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 327dc992-6a02-3a0b-a916-ffa040d46833 | -4.60398 | -50.56494 | 2024-10-29 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 699159b1-99f9-3169-aabd-150262144667 | -4.62533 | -50.63694 | 2024-10-29 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9ec1fa1-023e-3523-aa3f-7f671d8fb784 | -4.62469 | -50.64152 | 2024-10-29 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ad2fd9d-59c9-3815-a1df-c8e6193253dd | -4.60465 | -50.56029 | 2024-10-29 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ecd3c6a7-a0ea-3176-9022-5862eff9fc08 | -4.60461 | -50.5624 | 2024-10-29 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 593bca23-3049-3942-b08c-6322d597905d | -4.60396 | -50.56707 | 2024-10-29 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 056509e1-0ecc-3540-8f12-7da67efe10ec | -4.47846 | -50.65155 | 2024-10-29 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17dfdeb7-e552-3cf3-bbee-731d4d7c1510 | -4.47238 | -50.65078 | 2024-10-29 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48aa8c45-eca6-3614-bea0-2d14d55a7c56 | -5.60061 | -50.05872 | 2024-10-29 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0768c870-c1ea-3c87-964e-608c22afc510 | -5.59988 | -50.06401 | 2024-10-29 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee6df1a5-12e5-3916-ab85-911b041469b0 | -4.67093 | -50.98552 | 2024-10-29 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b229afe6-c842-324f-a354-0655a293b091 | -4.668 | -50.98162 | 2024-10-29 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40394fb8-d4d1-3e5a-9b1e-3b5ffb48affc | -4.66737 | -50.98592 | 2024-10-29 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bcf0a58-832f-306c-986b-72e695663bfa | -4.66558 | -50.98037 | 2024-10-29 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0970b548-8ab7-38c0-8ef7-33d0e43201c9 | -4.66498 | -50.98466 | 2024-10-29 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1160a7d-9169-33de-bc8f-915b10f99fce | -4.48001 | -51.0002 | 2024-10-29 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e1ffd89-4caf-365b-8650-baac76cf457f | -4.47408 | -50.99933 | 2024-10-29 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fb088a3-8b38-3002-b379-3ff4749e82e6 | -6.26504 | -51.7019 | 2024-10-29 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b757bde-9b8d-358e-b0ec-342b1ee1b5ea | -6.26498 | -51.7034 | 2024-10-29 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61d5cdc3-f6dd-3fdf-8aa1-3e26a3ee36ab | -6.26447 | -51.70595 | 2024-10-29 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bde54627-a223-3405-b624-675e026364bd | -6.26444 | -51.70746 | 2024-10-29 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87384a4d-0633-3de0-8eb6-474469c9b9d2 | -4.20226 | -53.46315 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b0adf1a-e351-34f1-9fe6-34af04d83f7f | -4.20214 | -53.4649 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8bfc228-d7fe-3f66-b34d-b0a2d960ac3b | -4.20185 | -53.466 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c217bd69-32c7-369a-ab71-39e33e14d9bb | -4.19724 | -53.46246 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9fadd2bd-0667-3bd3-9fd2-1f01b0ad6a82 | -4.19712 | -53.46423 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08f91875-7d81-3a95-ad1c-60102874a2a5 | -4.19683 | -53.46534 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 654da132-d232-3d31-ab9d-3d3a7736bfe9 | -4.19669 | -53.4671 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eacb6f0e-ebaf-367e-b4f7-84d87e2acb96 | -4.19642 | -53.4682 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21dc3c17-bdb4-35c6-8e01-e41f0fbd4cf6 | -4.05127 | -53.41146 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6aa1bae8-2c1e-3a2a-9265-fb1e91179c23 | -4.05084 | -53.41436 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bd71c19-2dc6-35bb-af23-57e58de12ade | -4.04668 | -53.40781 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4652fb3b-fd31-3be0-a34e-7cd75151420c | -4.04626 | -53.41071 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4d58e8e-b36d-3679-a5ca-9e6cde6de5fd | -4.04583 | -53.41362 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a92e6c8b-da54-39c2-9890-384b113b52cc | -6.16817 | -53.5838 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00749c07-5a75-3e07-800a-29a095761f01 | -6.16775 | -53.58677 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30eebae4-bc19-3afb-930b-77f18433d479 | -9.47789 | -54.53021 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d2a3cc2-a336-33db-b36d-17c9dba623a7 | -9.47328 | -54.52638 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f33b850-b048-3489-aeb8-948d7416be90 | -9.47288 | -54.52936 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1105607-3f2d-3e27-bafe-c7ccb7d7cd5a | -10.34227 | -55.01702 | 2024-10-29 05:27:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5ad071e-b104-3005-bc52-6ac06195cb20 | -10.03423 | -54.33437 | 2024-10-29 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1cc89fe-9410-3a23-93b8-6f9b3f568283 | -10.02948 | -54.33072 | 2024-10-29 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ada5263d-d3df-3217-a401-4d29a16a4b8b | -10.02907 | -54.33379 | 2024-10-29 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97e2a6c0-9fe1-3a0a-b3bb-fe7e9a190a3b | -11.32513 | -55.21767 | 2024-10-29 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa8485ea-4d7c-31b4-872c-9f39f6366956 | -11.32094 | -55.21137 | 2024-10-29 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ed999d1-98d4-312d-8446-4d9517a17bc2 | -12.09488 | -56.83178 | 2024-10-29 05:29:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e6e12db-42d0-338a-93a0-cba96b5db428 | -11.86949 | -56.87388 | 2024-10-29 05:29:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 255d9a8b-0992-317a-b635-65b73a4bed60 | -11.86769 | -56.88712 | 2024-10-29 05:29:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20d07055-1fcb-3a90-a16d-d270823be71f | -12.20747 | -57.22688 | 2024-10-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45db9758-d0a4-356a-9581-be0939be93f4 | -12.20312 | -57.22621 | 2024-10-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b20a57e-0efd-3e2b-808e-da49c1190246 | -11.31086 | -58.4159 | 2024-10-29 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0814f377-e0b1-3274-ab96-4a2f694a65e1 | -11.48372 | -59.09758 | 2024-10-29 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63180386-231c-3365-82f4-2c727b1b158b | -11.12899 | -59.01775 | 2024-10-29 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff20e6d4-68ef-3e84-98df-16e1a47c50d6 | -12.5377 | -63.24966 | 2024-10-29 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb86ea44-4e08-3074-8079-7f17b6b09ea6 | -12.53439 | -63.24912 | 2024-10-29 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51c9ecb0-e6ab-394f-ba63-86f94f526b54 | -9.75692 | -67.24397 | 2024-10-29 05:29:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e85afe9-5c3c-32b7-9fbe-467a9bee61e2 | -9.75558 | -67.24142 | 2024-10-29 05:29:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 794ba335-a53b-3fcc-8019-0f104e9743fd | -9.62574 | -67.21378 | 2024-10-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed2fe03c-138f-3f48-8c02-730abef1cb57 | -9.62493 | -67.21859 | 2024-10-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d2b6d32-7943-309d-88be-5fe1f31dd596 | -9.60516 | -67.19537 | 2024-10-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 276bf6b5-2dde-385f-8e5f-575a4ab43cfb | -9.60435 | -67.20019 | 2024-10-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbbca6d8-c046-3070-913a-cd9f2d21e789 | -9.60051 | -67.19952 | 2024-10-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38d5a244-935a-30ef-9855-1c23f421bfa1 | -9.76341 | -68.42168 | 2024-10-29 05:29:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c7bc81a-cdec-3d89-9c9b-fb27bce17d50 | -9.63737 | -68.67725 | 2024-10-29 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcc95eca-c179-37c4-bf13-d8da2c8637bc | -10.13808 | -68.06205 | 2024-10-29 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd128328-3c1a-334d-add1-4898908d8e1f | -10.03478 | -68.44241 | 2024-10-29 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e483416f-ed7d-3866-93ed-2f1028c01e09 | -12.34766 | -49.92627 | 2024-10-29 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fe2fd5f4-9151-32d4-994f-34b197e09d88 | -12.34692 | -49.93312 | 2024-10-29 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5c19fb3b-5357-399b-b5ab-2c4ea56decb1 | -12.34618 | -49.93994 | 2024-10-29 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 01ac95e1-d717-3ff3-bd2a-276d7e76b733 | -12.34068 | -49.92528 | 2024-10-29 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c3275cfb-cafa-3eaa-a3ff-9927d2033a5c | -12.33995 | -49.93211 | 2024-10-29 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b79b141a-fe24-3ec6-8dfc-c77d7ef7329a | -12.33921 | -49.93895 | 2024-10-29 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3c4f8c43-6576-38dd-af60-457910ff4ecd | -12.09529 | -52.48506 | 2024-10-29 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 784a8f80-f7e4-3ff4-a5c9-f09942e3a0eb | -12.09475 | -52.48955 | 2024-10-29 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4232d71b-7dff-3823-9970-24cbcaa98cc2 | -13.25304 | -53.92717 | 2024-10-29 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3c836d8-c8d4-39ee-8f21-0ff01f561fa2 | -11.33007 | -55.21827 | 2024-10-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fdcb4c6-fad9-3100-b62a-b86836c95767 | -17.79696 | -57.36804 | 2024-10-29 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9aad5aa5-33b3-3f8a-8117-3e2ab97ef62d | -17.79635 | -57.3731 | 2024-10-29 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 9e627720-b966-3747-ae79-409a7804c1b3 | -17.79574 | -57.37817 | 2024-10-29 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 1c1cdd7d-ef29-35d5-9e2b-9fb413f63e5b | -17.79229 | -57.36744 | 2024-10-29 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 475b84fb-424d-30c7-a4f5-47d9a9444118 | -17.79169 | -57.3725 | 2024-10-29 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 8ed53462-3435-38a7-99da-e217e28613ae | -17.79108 | -57.37756 | 2024-10-29 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 875eb128-7fd7-31dc-8d6e-929f80339a78 | -17.7177 | -57.56059 | 2024-10-29 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 87ff00dc-64fd-335c-9101-01012f631ca5 | -17.71713 | -57.5655 | 2024-10-29 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6cf0278c-ec7f-34ec-b5d1-8c820810aa9b | -17.68447 | -57.48975 | 2024-10-29 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7096da70-0984-3e03-942b-25eedd2660d8 | -17.65736 | -57.48118 | 2024-10-29 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d25de748-ee49-31b4-ad6a-fae64c058b42 | -23.99312 | -54.11961 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 63ce5112-695e-3cd8-ae23-081d44bd0e11 | -24.00536 | -54.12844 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 711ef707-0094-386c-bf31-64674583c22f | -24.00509 | -54.12587 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0d20e841-d067-34b2-bd94-08ab5a23ee5e | -24.0047 | -54.13101 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3f72657f-6d98-3620-af3e-d858dd7166fb | -23.99961 | -54.12278 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| cbfa7e6b-945d-33b1-8f58-e9ac6e73aee2 | -23.9993 | -54.12017 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f3ad1050-93ef-353a-9df6-c76f71d04d66 | -23.99919 | -54.1279 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |


[Clique aqui para ver as próximas entradas](README105.md)
