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
| 9f6c17e2-f7a3-37ec-be31-810795dd4b9e | -12.06213 | -50.54683 | 2026-08-24 07:20:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| d521ef63-c0db-31fa-8234-db0d272fe8c0 | -13.89196 | -54.03768 | 2026-08-24 07:20:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.4 |
| d19c7d24-ad21-3f5d-bf75-5e1b18336af8 | -14.29915 | -51.76849 | 2026-08-24 07:20:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| cd8b316a-66dd-3f6d-a2f7-774e671ce228 | -13.15801 | -51.38464 | 2026-08-24 07:20:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| bba5a01f-09b4-308a-8b9a-c8bf294fe93d | -14.30157 | -51.74903 | 2026-08-24 07:20:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 086cc0d9-076c-3d58-9cf8-833efd39d01a | -15.40389 | -55.7824 | 2026-08-24 07:22:00 | AQUA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 7d818c30-459d-3391-b390-bb04fb7e2c7a | -15.40538 | -55.77163 | 2026-08-24 07:22:00 | AQUA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 376a044a-cf4b-3538-9d0a-780c1a37d112 | -15.32421 | -53.95843 | 2026-08-24 07:22:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9a213892-4782-3a1d-b8a9-ab3119752c3a | -16.05412 | -50.44529 | 2026-08-24 07:22:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f8a59969-1a31-3017-8915-de05d2bfc5e6 | -16.06485 | -50.44184 | 2026-08-24 07:22:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| f0df2c9e-a13b-3819-9516-d9f8b5189fa1 | -7.6665 | -63.3261 | 2026-08-24 07:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 57a57a13-824e-3eda-8e10-4e7bbb3734c8 | -7.6851 | -63.3067 | 2026-08-24 07:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 06725fa0-3edf-3754-b3bd-417e66dd9596 | -7.6849 | -63.3443 | 2026-08-24 07:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 8a021c9e-7e2a-343c-88ab-1c1a04561c94 | -7.685 | -63.3255 | 2026-08-24 07:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 2ec13192-561f-3fd5-a49d-b607859053a3 | -7.685 | -63.3255 | 2026-08-24 07:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 9a0ccd8e-ec79-306c-935a-a37a2506e1d5 | -7.6849 | -63.3443 | 2026-08-24 07:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e2463d69-d9ab-35f6-ae79-ede2ad760b6d | -13.8768 | -54.0114 | 2026-08-24 07:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f3338553-e721-3d22-a0ae-05fa953158df | -7.685 | -63.3255 | 2026-08-24 07:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 62b511b7-9fa2-3988-ada4-e84b9153d606 | -7.6665 | -63.3261 | 2026-08-24 07:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 16aa67f8-243d-372e-845d-1877fd890cc1 | -7.6849 | -63.3443 | 2026-08-24 07:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c59f037d-8e69-3eaf-a4db-132275e05bae | -12.0566 | -50.5567 | 2026-08-24 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9764a8df-f4e3-32da-ab2e-4ee7740b3823 | -12.0563 | -50.5782 | 2026-08-24 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 05a507ba-e88b-3004-9933-7b012403c795 | -13.1704 | -51.3831 | 2026-08-24 08:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| affcf6a3-637d-322a-ad84-765b829b4208 | -13.8768 | -54.0114 | 2026-08-24 08:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 63d9cb8b-7033-382c-8437-c35b23ec5c18 | -7.685 | -63.3255 | 2026-08-24 08:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| b5347533-b007-3190-b687-d2228fc06fc2 | -12.0566 | -50.5567 | 2026-08-24 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e6541ede-862e-30b2-a8a7-4d5f1f02780b | -13.8771 | -53.9906 | 2026-08-24 08:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| bca9bfde-4aa1-378d-9baa-9a22842ce69c | -12.0563 | -50.5782 | 2026-08-24 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 5e9e78e4-b51d-3958-abdc-a64624c68295 | -12.0566 | -50.5567 | 2026-08-24 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 57e36503-a088-3013-9ccb-8e55cda8c3ec | -13.8768 | -54.0114 | 2026-08-24 08:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 70a0c1ca-c5ab-3a28-9f8e-82b420baabf7 | -12.0563 | -50.5782 | 2026-08-24 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| fdd59640-966c-3944-afc0-ac80e9f7cebb | -13.1704 | -51.3831 | 2026-08-24 08:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 3a5680e3-1b51-3730-ae2d-705019ad55f2 | -12.0566 | -50.5567 | 2026-08-24 08:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 0fbf226d-637f-3b21-9ef3-741eb2d1df4d | -13.8768 | -54.0114 | 2026-08-24 08:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 73ea6817-0ccb-36ed-9a73-85895d9b3d96 | -12.0563 | -50.5782 | 2026-08-24 08:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 504c5f51-9bd8-3d33-9ee7-3175510c5acc | -13.1704 | -51.3831 | 2026-08-24 08:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 571fc5d6-bc9e-3c30-86cb-9ae07d6b5537 | -12.0563 | -50.5782 | 2026-08-24 08:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 68daed85-721f-30f5-a13d-f34767010b28 | -13.1896 | -51.3807 | 2026-08-24 08:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| dd984264-f544-30d5-a88e-2861f47674c7 | -7.685 | -63.3255 | 2026-08-24 08:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 075a5b3f-9a17-3311-b410-a334fa0b5092 | -12.0566 | -50.5567 | 2026-08-24 08:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 1aa02745-b44c-3ac5-8fcd-d30ea9e89b78 | -13.1704 | -51.3831 | 2026-08-24 08:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 861dfd9e-41e5-38ed-94ab-fd7a25c65d9f | -13.1704 | -51.3831 | 2026-08-24 08:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 050b4193-e109-3bb9-95be-22bed880c7f3 | -12.0563 | -50.5782 | 2026-08-24 08:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5d2fa83b-aae4-377e-9077-05c619766f5f | -7.685 | -63.3255 | 2026-08-24 08:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c5443bee-21f0-3a98-a5b7-d21c0156b509 | -12.0566 | -50.5567 | 2026-08-24 08:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b3d8e3b3-368c-37f6-b389-7c47b248bf5e | -13.8768 | -54.0114 | 2026-08-24 08:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 6c7b2ad6-0219-34c9-9831-9dec62e7b420 | -7.6849 | -63.3443 | 2026-08-24 08:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c7e6682d-c7a3-3075-81c1-15ba1a60e040 | -14.9392 | -52.664 | 2026-08-24 08:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 2dbefb98-79e3-37ee-ab5c-c19237bd897a | -7.685 | -63.3255 | 2026-08-24 08:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 92830a2e-6f3e-31cb-8c7f-014083d576cc | -12.0566 | -50.5567 | 2026-08-24 08:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 63ca72de-9f48-33a9-980d-7548219a15f0 | -12.0563 | -50.5782 | 2026-08-24 08:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b9a2d317-7753-38b0-9bda-a10fc832b131 | -7.6849 | -63.3443 | 2026-08-24 08:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| bccfe9e4-7714-3498-a1b0-563d28c74f59 | -7.685 | -63.3255 | 2026-08-24 09:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| b266664d-315b-3c7c-8635-b8583ab551a5 | -7.6665 | -63.3261 | 2026-08-24 09:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a4618370-5110-3c54-aab6-333d8fc7f49d | -7.6849 | -63.3443 | 2026-08-24 09:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ce514f10-01b2-3a1b-8607-3841c54f4736 | -7.7034 | -63.3249 | 2026-08-24 09:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 17e14265-d034-37e5-9efa-501d631481ad | -7.685 | -63.3255 | 2026-08-24 09:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 4b97f7c6-f45f-3085-994c-d1786c33f16c | -7.6849 | -63.3443 | 2026-08-24 09:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5dfd5262-1ee2-3c5a-990e-6e43e6a5370d | -13.1704 | -51.3831 | 2026-08-24 10:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| e4bf428b-ba37-3751-8548-a59dfac621de | -14.2982 | -51.75 | 2026-08-24 10:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 0ea713c8-c1d8-30cb-ad9e-8da60d0444ac | -14.2788 | -51.7525 | 2026-08-24 10:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 286.3 |
| caaec6bf-4cb8-3504-8ffb-e769c949707a | -14.2785 | -51.7739 | 2026-08-24 10:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| f4190880-6d88-3c49-9df6-6dabf3dbb6bb | -13.1704 | -51.3831 | 2026-08-24 10:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 48ce2a61-5e2f-3fc9-93ee-9673effba7ea | -14.3175 | -51.7474 | 2026-08-24 10:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 27663c5d-8ac7-331c-8f0f-d2077c5fa55f | -14.2982 | -51.75 | 2026-08-24 10:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 319.5 |
| cf70cb26-ca07-3f3e-923c-f0bd35617d8c | -14.2978 | -51.7713 | 2026-08-24 10:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 37b084f4-0d9d-3ceb-aa47-cec2e052386b | -14.3368 | -51.7448 | 2026-08-24 10:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 33f272df-e9c7-3940-bddb-2b1d82cb3819 | -14.3175 | -51.7474 | 2026-08-24 10:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| fdf05966-b359-3924-9939-b45ba942bb29 | -13.1708 | -51.3617 | 2026-08-24 10:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.9 |
| ef07ebd7-845f-3c92-9367-ab3eb82fe2f4 | -14.2788 | -51.7525 | 2026-08-24 10:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| bb3809f1-4e01-301f-b475-ad288b2a8f38 | -13.1704 | -51.3831 | 2026-08-24 10:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 83ae3e92-c92b-37db-ab6a-0d91335ff8d1 | -14.2982 | -51.75 | 2026-08-24 10:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| bbdba9fd-55e4-339b-b234-208f02f6501d | -14.2788 | -51.7525 | 2026-08-24 10:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 14415a4a-6b64-3d7d-a140-e639d2c0bed5 | -14.2982 | -51.75 | 2026-08-24 10:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 324.2 |
| ba8c15e2-f49a-3ec1-bc72-301e64565aee | -13.1704 | -51.3831 | 2026-08-24 10:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 5d1c11fa-e84e-308f-aca4-c3c5fe95e97e | -13.1516 | -51.3641 | 2026-08-24 10:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| e1aeeefa-8ec6-34c2-a280-a0e6aab53818 | -13.1708 | -51.3617 | 2026-08-24 10:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 8805f419-e146-3414-94f8-e942207320dd | -14.3175 | -51.7474 | 2026-08-24 10:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 153.8 |
| e191f049-1461-3f38-8294-a29165b8f004 | -14.2978 | -51.7713 | 2026-08-24 10:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| df682229-e5af-34d0-8989-7a5beeaf4451 | -14.2788 | -51.7525 | 2026-08-24 10:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 238.1 |
| 2fe39714-92ed-3e49-bcd2-e3763b271f2e | -13.1708 | -51.3617 | 2026-08-24 10:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 99c4fa88-0d20-33fe-895b-9e6e5f9a7d44 | -14.2982 | -51.75 | 2026-08-24 10:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 166.6 |
| a79c73e0-ffff-320d-ae54-5121470e35bc | -13.1516 | -51.3641 | 2026-08-24 10:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 3b8b5c3e-1400-3693-a554-43e35321a254 | -13.1512 | -51.3854 | 2026-08-24 10:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| eb5ba745-b5d1-3eaf-bec2-71c2b57db96a | -11.0778 | -46.1925 | 2026-08-24 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d95d12fe-4f1f-350a-b5f2-90d0e45ba6bc | -14.2792 | -51.7311 | 2026-08-24 10:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| a1ae987b-7e91-3613-8689-c7079a34311d | -13.1708 | -51.3617 | 2026-08-24 10:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 460c3323-638c-300a-91b2-7669a800e280 | -11.0969 | -46.19 | 2026-08-24 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 37a2df55-a93c-3261-8b69-958a47882f58 | -14.2985 | -51.7286 | 2026-08-24 10:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 8f62c6e8-7d85-3146-9699-d6361a6e4fce | -14.2982 | -51.75 | 2026-08-24 10:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 344.4 |
| 64bee3d8-9594-34a3-84c6-0d3c88d849de | -13.1516 | -51.3641 | 2026-08-24 10:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 232.1 |
| e8492836-4f39-3330-914d-cfa67c706632 | -13.1512 | -51.3854 | 2026-08-24 10:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 1e4652e3-4a9b-301b-8146-8e97140566b5 | -14.2788 | -51.7525 | 2026-08-24 10:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 253c0cd3-e12c-3232-b1f5-ea9f253b1449 | -14.3175 | -51.7474 | 2026-08-24 10:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| cdc193a6-4d35-337d-baac-c61c6bfdb1fc | -13.36345 | -41.66483 | 2026-08-24 10:58:00 | TERRA_M-M | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| beaef7d0-2051-31c2-a399-3544a7a34d7a | -14.2982 | -51.75 | 2026-08-24 11:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 241.9 |
| 07b364f4-e9a2-31d1-be24-7b0dcb610892 | -13.1512 | -51.3854 | 2026-08-24 11:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 29ef5e17-2962-34b5-8eec-e3ae52e6241f | -14.3175 | -51.7474 | 2026-08-24 11:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d501a8af-e2f8-358e-8eaf-505e35aedfa0 | -11.0969 | -46.19 | 2026-08-24 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| ab55781b-bb31-377f-8735-38580768641e | -13.1512 | -51.3854 | 2026-08-24 11:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |


[Clique aqui para ver as próximas entradas](README50.md)
