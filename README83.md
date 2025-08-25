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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c52f65fd-5f8b-3e90-8e69-3b61b4459ed3 | -9.20601 | -59.44043 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 266ca466-196c-343e-a806-413a8fece5d2 | -9.18633 | -60.79314 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f34f3698-361f-322f-a2d0-77a0f6de25e2 | -8.89752 | -62.41163 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 757555d4-4232-3117-ac3f-98376163fd3b | -9.01188 | -65.70742 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16b64e95-498e-3e0e-bfee-b824df524614 | -9.20503 | -60.91816 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d336f5a1-6819-36e0-9c31-49e7ebca0345 | -8.89714 | -62.44901 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 116b4179-4e92-3d29-a359-25cad66c1ee0 | -9.96156 | -60.18025 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0791fdd7-ba3a-3eb5-a450-04fcb44c2deb | -9.02963 | -65.71446 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aae386f4-ea17-3454-ab82-6d495989e5c3 | -8.88484 | -62.42669 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f961537-9498-31b4-aeb5-599beb8a1d57 | -9.00791 | -65.38204 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86acedac-7ca4-35b1-801a-15498c3b7e40 | -8.69512 | -62.88011 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15d85275-d2b0-30fd-8e1e-3d97fc70f1ec | -10.41726 | -64.39501 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30002951-9d47-3385-8f66-48e8e6ca3319 | -8.91893 | -62.42415 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10e16526-e9f2-38a4-b807-5ae73088d077 | -7.55834 | -63.85772 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33091969-a566-3989-87fd-cbcefe3da983 | -11.70268 | -60.17678 | 2025-08-25 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a93079de-e1b2-3e85-9eea-cec7bcf2bb5c | -7.90937 | -63.0633 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 7d393438-60d4-37aa-86ba-22fa6886f2b2 | -9.17703 | -59.62192 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 528120f6-f2db-313d-822a-aae4a3e1f7a6 | -8.61317 | -62.59911 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a4804f1-1c4d-34ca-ae67-b8a7c01cecc9 | -7.35642 | -57.63182 | 2025-08-25 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| feaca52c-aff4-3f80-80bc-6a6a5abf1907 | -9.22132 | -60.91135 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b49f02fc-802b-39a0-b188-c16bd2da7a7d | -9.20389 | -60.92704 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52f8167a-493f-301d-9aab-31fc82dc2caf | -9.14799 | -60.76936 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4749f8c2-a4b2-3c87-a792-9346a08ca930 | -9.2024 | -60.78924 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8f14e5d-1a2a-3871-a7a1-e553cd3925c3 | -7.97976 | -70.02641 | 2025-08-25 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ae74ce3-2df8-3f3f-be96-b455fb170e38 | -8.6381 | -62.64779 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76db1b0e-a290-3d32-97cf-4578df4990ea | -9.0424 | -65.72977 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f66d183f-5baf-36b6-b6c4-1112d8567a39 | -9.01165 | -65.3826 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e001bcc-0096-392c-b87a-4734e43211b0 | -8.65603 | -63.43451 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63e3d95d-558b-34ea-8de8-a5e7dac04345 | -8.89969 | -62.45225 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4839fb42-d6c0-3d0b-9f5b-506c00505650 | -8.99203 | -65.41201 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2b4c5815-7625-3345-8c78-d89c377496bf | -8.89389 | -62.42802 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70fd17d0-779b-3d08-b6ef-f1dfbdee8c62 | -12.06821 | -63.15371 | 2025-08-25 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f0e2182-5cf0-3e4e-86ad-4965be4efeaa | -9.15335 | -59.5033 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cffa39bc-0c58-3f0e-a88d-77f46bab3ec6 | -9.8125 | -64.26124 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45aa56b8-5d97-3f85-ae9b-7a60c933aa94 | -6.79083 | -58.62852 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42e07034-d531-3647-865a-cabfb27b75f4 | -8.57645 | -63.92027 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cab91b97-1794-35a1-a63d-e1f07fd51a0b | -6.8191 | -58.95537 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4a073c2-bbb0-33c2-9e19-8020f234f6b8 | -8.88749 | -62.45229 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cbf55d20-a4d0-3bbb-a473-b529cc5e0731 | -8.90988 | -62.42279 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95bd6d13-8f50-3078-a524-3327eb852a06 | -9.04368 | -65.72105 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0950c61-e201-3097-9300-7b9441ed5f7e | -9.08813 | -65.72118 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a0ed62a-c52b-31dd-8b84-ff89a6dde55e | -9.17336 | -60.81279 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bf76a58-1e81-3e27-b888-5030507c84db | -6.6926 | -58.85786 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 431ef41f-e8e3-36da-bfbc-6274ee72fdbe | -9.1951 | -59.61564 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91087ae9-2aaf-35d1-b5c2-7d5fc62667ba | -9.13433 | -60.73079 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37a69ef5-8d88-3c1f-90b0-d52e806599b9 | -9.23851 | -60.47969 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b7ea988-28fb-37d8-a4bf-9d7443f7df1b | -9.63714 | -63.33729 | 2025-08-25 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bc5e669-9c8e-337e-8ca3-4582b936793c | -6.80219 | -58.63019 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7f83115-1aff-35fd-99e9-408cd5cb14c1 | -9.24847 | -60.48441 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60e044e5-32a9-3642-b54d-5632dd372dbf | -8.23127 | -61.431 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30dfb35e-15ed-3823-9bd5-1b37a574fda5 | -10.47677 | -57.94033 | 2025-08-25 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40b7d8b7-920e-3540-a418-9dcb0f1f065f | -10.41725 | -60.3012 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7742108-99aa-377f-b1d0-53c59b5bffee | -9.01746 | -65.69488 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f823bb89-c4a8-37d8-a47b-baa36c7362d0 | -9.2083 | -60.78392 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 177341c0-0ca5-34c8-9bee-d89d3d89294e | -9.1625 | -59.51959 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a6c4cbd-e531-3e3f-8e5f-7550af24029b | -9.16124 | -60.82626 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57342496-dcf7-3fbc-a022-bd20c95693a5 | -8.0233 | -69.92119 | 2025-08-25 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e14b8e00-a10a-3de2-b493-429d385b9aad | -10.25317 | -59.10544 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| aa1b8006-683e-3fc0-bd2a-41663edb06da | -9.21648 | -59.71013 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3570be08-800a-348e-bb23-77e8098d3dd6 | -9.0202 | -65.38593 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da89453-e6b4-3ee6-b37e-58a86b8b2770 | -9.19063 | -59.47266 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3edfd039-082d-34a5-82ee-bb1c6420325f | -8.90433 | -62.4641 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 55294253-54b0-381e-92a4-ce28557d7969 | -7.57654 | -63.43496 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbfd9d93-7f7c-3a3f-9322-0be1f3990372 | -8.60995 | -62.58961 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 126bdfb1-4276-3d06-8627-9daee81ecde2 | -8.10817 | -62.87199 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3c1b7d1a-21f6-353e-8827-bc9d6dbbfd5d | -6.91633 | -62.99789 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4b55509-fbbd-34c5-bf20-c4ff0308fc40 | -9.0205 | -65.69981 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b78d208-e057-3541-b7ae-feb1adf3f1c4 | -6.92 | -63.00245 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca596986-3f20-387e-9dfa-edcd00b5bfab | -8.89452 | -62.45618 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78659143-3433-39b0-bffd-60e953904966 | -6.82971 | -58.96085 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2c2ed4da-f253-3dae-8aa0-bb018930bfff | -6.79545 | -58.63714 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58573997-b19b-323f-8492-7acfe692a864 | -8.92736 | -62.43011 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bf582b1-f38b-3d45-9f00-b5e71ddbb0d7 | -8.88098 | -62.45422 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 82c44a46-5950-3434-b73b-7d05c38a4c9e | -8.99309 | -63.64684 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a256ac48-5801-36ec-b26e-bb89e5cb1ec0 | -9.01338 | -65.39677 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d6893ec-7ddc-3612-b6c7-a85df2f1c266 | -9.16789 | -60.81505 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4cb78b3-1fae-302c-bc89-60af5d6ec5c8 | -9.51806 | -60.51551 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3439b4da-f4d9-381d-8a67-3c4f642bcfc3 | -8.13913 | -62.87231 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f71f39cf-65a0-336e-b7bf-aeb45e362468 | -7.53164 | -63.81381 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aef18952-086f-3e80-83b4-cb7f6d592b1b | -9.1476 | -60.77234 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31d2f323-e63a-3f15-96fe-65e970c9cf47 | -6.83577 | -58.95798 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1b1bbdb6-7c0e-30a0-a021-51e5ebea16f1 | -9.80508 | -61.20841 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09a42272-901a-3d0d-b393-fadd07ad7db9 | -8.60549 | -62.58896 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e577f74b-6ae2-3552-b532-2377b9c20ca1 | -8.90424 | -62.42014 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2235f5ae-907e-3d50-b621-b5573b8bb8ba | -8.57238 | -63.91967 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b1fb0b6-8318-3ee0-a220-307b88df35a0 | -6.79598 | -58.63329 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0debfb13-aa3b-329c-91fc-fceb9f13dc74 | -8.22332 | -61.38132 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 16a1dcd3-9584-3575-b9aa-d5ef2495e8f1 | -8.57434 | -67.7557 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2c4750c-dd9c-3933-b402-6cafae2b9c2d | -9.81199 | -64.26485 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f0a52b1-be8f-3cb1-8868-6e1e387fff53 | -9.16213 | -62.35456 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0bfd8d80-4f92-3037-a996-1bd31638cc6b | -8.87775 | -62.44441 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0b59bc8-3af0-30ff-904c-eca33521f7ab | -8.00088 | -63.45886 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bcb3c6f-c73b-36b7-aa29-8e2b1ddd2db8 | -9.20961 | -60.92665 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8491ede-fa54-360e-9845-25b4a0b36a84 | -9.2274 | -59.71181 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 273c6e48-ce29-3948-a228-450850c0b055 | -9.20541 | -60.91515 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45deec76-c3c9-3688-86be-039f41c7df1f | -9.17428 | -60.76666 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9644eb92-327f-35a7-8d07-338500cf27d5 | -8.87582 | -62.45814 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 98e8ec2b-aa28-3f8c-94ae-831875bc4bbe | -8.21298 | -61.3852 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7a234ddc-877b-3a14-b451-9d6bce967895 | -12.0637 | -63.15307 | 2025-08-25 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb87e42c-76fe-313b-931a-51402f123de0 | -8.59048 | -62.63189 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README84.md)
