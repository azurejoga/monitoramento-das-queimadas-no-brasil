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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d42bd190-b342-3296-aec5-4f0bab140fde | -13.7346 | -42.75732 | 2025-06-16 04:27:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2dd21746-6efe-3fc3-acfc-bd6ad11db9ab | -14.03135 | -55.12749 | 2025-06-16 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 186c5755-b7ca-37a5-bb46-54f85299b400 | -12.72765 | -46.27353 | 2025-06-16 04:27:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bfbd0ad-1873-3a75-a97b-f68523bb17d6 | -14.64734 | -48.0608 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d922664-4fb0-333e-a907-a65c4ca52c24 | -15.05592 | -49.4763 | 2025-06-16 04:27:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2656a807-9951-371b-9b9d-aa7ee37716af | -11.13984 | -53.91569 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41e1ae1d-97e1-3b29-ae51-ae717d9ac2af | -10.82846 | -46.95935 | 2025-06-16 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21b7f2f2-cec1-386c-a6d2-4d9ac82f9bfa | -10.03531 | -48.78503 | 2025-06-16 04:27:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 244d0a73-866f-3abd-a770-a512972272f6 | -12.08837 | -49.49325 | 2025-06-16 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 164d149b-f931-320c-84e6-b965975be98b | -13.91948 | -54.62407 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 280d8c44-90cb-3a2e-9c1e-fa498cac31ba | -11.0064 | -55.07571 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bded00d7-e322-3f58-ac86-fb3c36d677b8 | -13.92269 | -54.62964 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ec6aac0-eb96-3b4c-b449-3841bdfe9282 | -12.20831 | -49.64416 | 2025-06-16 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7eb3306-76b1-3e53-b446-f633fd504516 | -12.17469 | -54.2372 | 2025-06-16 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9916dd85-ebd8-3378-8b22-dbff1eaa1bfa | -11.40433 | -47.62854 | 2025-06-16 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b4c9f1a-276e-3453-a3ef-f8de857a83ac | -14.83129 | -48.45049 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1444cdba-ffb3-3836-bbcf-3a543aee9e74 | -12.52373 | -57.22736 | 2025-06-16 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7df92f4-8599-3e22-b221-4fd4a4b46430 | -11.01207 | -55.07145 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8202af56-78da-34c5-bd03-7be89350a0b9 | -11.00918 | -55.06021 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 98e22ed3-61de-3d97-97a3-63a7d0e1b69e | -12.98013 | -48.64222 | 2025-06-16 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ef2b8da-5aca-3f3d-acbc-406e2820e2de | -14.82637 | -48.43876 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ade5093-3ad3-35b1-91d1-f239e49fbef7 | -13.49021 | -47.86757 | 2025-06-16 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9e4e72d-b421-3919-8d5d-edf2af529c2f | -13.29134 | -57.07537 | 2025-06-16 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4e93b10-dd93-3a99-a9ad-0e5c953d9c86 | -14.82585 | -48.4205 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c9ca7a92-cae4-37ce-90cd-71b8dca8ac39 | -10.85454 | -53.78719 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6ba8b2e-fe72-37fd-9a28-20a9e1804e68 | -11.02734 | -44.64609 | 2025-06-16 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db89dad8-f616-3985-a087-c8f20bbdb77e | -14.02683 | -55.12664 | 2025-06-16 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51c6c0e9-87bb-3904-aca4-91a657c4cdb9 | -10.85531 | -53.78284 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7267d585-fc93-3440-b3b6-07ad97a8f670 | -9.40973 | -48.42698 | 2025-06-16 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f35f38cd-6253-3547-9aed-613bda436671 | -14.82529 | -48.42405 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc02dd89-e457-3d6b-9f4e-9078048713a5 | -11.00491 | -55.06159 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a81f1e68-d106-39ec-86ef-966441996a16 | -12.02386 | -57.09266 | 2025-06-16 04:27:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9ddf177-eec7-3eac-b620-dfcd9392299b | -10.09799 | -52.74005 | 2025-06-16 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1db19151-39c8-3714-bfd0-f77db6a66bf9 | -13.91751 | -54.63327 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63f55767-6e40-350c-820a-0b69acdb468d | -11.00444 | -55.05936 | 2025-06-16 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 75d973d5-40b4-3067-ad8c-5f7b85aee334 | -10.99967 | -55.05858 | 2025-06-16 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e034483-e2bd-3fbc-932b-689b3dd97c70 | -11.00395 | -55.06674 | 2025-06-16 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5a7b8baa-fe56-38e2-bbd6-3cac59f837f6 | -11.00351 | -55.0645 | 2025-06-16 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| db1c1051-34dd-33de-9846-73a35cd60420 | -13.91391 | -54.62813 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad8b9faa-bfaf-32df-8e5b-ffc82ad8c8be | -14.83788 | -48.45161 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5307bff-8650-32fc-81fd-1d0131ab452e | -13.3621 | -47.86124 | 2025-06-16 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4861a78-30b8-3338-98ff-186e65aa9d8c | -10.07605 | -52.74401 | 2025-06-16 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fc308234-5ead-3f55-ab22-235ab3ec396c | -9.40187 | -48.43311 | 2025-06-16 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b2cbe43-d2f4-3e29-a4ec-45134fd81ccb | -13.9147 | -54.62373 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9665717-67e9-3b22-8e4a-4a0d99855770 | -10.08975 | -52.73855 | 2025-06-16 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 12dc20fc-0c2c-308a-8173-34badd8e8e7c | -10.82462 | -46.96232 | 2025-06-16 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80ceeb1e-2c85-3e26-9f27-c37a3807eb9c | -10.09387 | -52.7393 | 2025-06-16 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| f9d93b6d-14d9-3a92-92e2-3276d473f15a | -9.41472 | -48.43887 | 2025-06-16 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 645ed084-da09-328a-8a84-55342f9d678b | -10.8257 | -46.95533 | 2025-06-16 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0418b20f-7fb7-313b-829c-50ed5449f2c8 | -12.76744 | -44.40379 | 2025-06-16 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2baf82e7-f327-39d4-8fb9-14716db3b248 | -10.82516 | -46.95882 | 2025-06-16 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fb672214-ad22-3681-94f4-53b79fe322bd | -15.05317 | -49.4721 | 2025-06-16 04:27:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87a9ba8f-082c-3681-b655-3ff72858e012 | -14.39096 | -47.07341 | 2025-06-16 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2577c03d-587a-3958-bc91-2f3ddd0f3416 | -12.75928 | -44.40477 | 2025-06-16 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef7e5e25-5dd0-38a0-9625-75fb48c502b6 | -15.39333 | -47.85378 | 2025-06-16 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62b3b607-c85c-3e38-8dfa-dfead6b24ad1 | -15.39278 | -47.85735 | 2025-06-16 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 617a831e-82f1-393c-bd04-644d65639751 | -14.65504 | -48.05486 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57eb8025-852c-3e87-b009-9d446030a990 | -11.01061 | -55.05734 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| eca0c854-2ea5-337d-99bc-98c48f8d4454 | -10.85017 | -53.7864 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a497ef4-5bb2-3971-8f51-c2a3b0fba394 | -10.84815 | -53.77252 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f23aa34f-bf05-360e-94bf-b59ae4bae63b | -14.02769 | -55.12202 | 2025-06-16 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a425746d-fc96-30e7-b3f9-e13e19a04873 | -13.91865 | -54.62849 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71d07bd0-f918-31f9-83d0-13dc257a278d | -13.03576 | -50.39883 | 2025-06-16 04:27:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7589dbb8-b0a1-3207-b896-cd3643cfd392 | -9.17105 | -45.32659 | 2025-06-16 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5732c3eb-0703-3484-bbe2-83f00d6d8d2b | -13.9183 | -54.62885 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80eeaba0-c1a4-3095-aa3f-eb7c7dbb5fe4 | -13.9191 | -54.62441 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ca081e3-74da-3485-879f-a679f262d661 | -14.66164 | -48.07766 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c23ccf8-a647-3898-aa78-f1763daeeebb | -11.14468 | -53.93905 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ce34f491-211e-324e-a623-0e500cffd932 | -11.00059 | -55.05347 | 2025-06-16 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76db17a3-eab6-3726-a9f2-91a5489210ee | -12.02921 | -57.09359 | 2025-06-16 04:27:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 885f8d73-15a1-3ee7-8f1b-49fb10a38e3f | -8.74327 | -47.17418 | 2025-06-16 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 618cbc6d-faa2-3324-ae36-54a441d2b95c | -11.00587 | -55.05647 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| bbae5577-2e12-3f0b-b050-ee913fb756fd | -9.40858 | -48.43419 | 2025-06-16 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98621b39-20c5-38a6-9a51-2c848a16dd4e | -14.74063 | -48.2904 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fa4e4c0-bc34-33a9-90d4-8fba861fce5b | -14.29895 | -44.28692 | 2025-06-16 04:27:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7215506-1221-3552-abef-e1f0a84cc9e7 | -11.00773 | -55.07277 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7151b9f3-0c48-3f1c-bf7e-7c72affc4172 | -11.00733 | -55.07055 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c5a0f0d0-b90d-3004-980f-304888c2b06a | -14.82855 | -48.4464 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8f14209-423d-3c98-aba9-5987c27ac021 | -11.88487 | -54.68176 | 2025-06-16 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aab71f9a-04d4-3376-b0b0-51c8aca4a42d | -16.68129 | -43.88322 | 2025-06-16 04:27:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7341678e-b49a-3f9a-900e-6b39981ce6a2 | -11.01343 | -55.0685 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da5e3c52-a88f-3e4e-aa1e-0484a3cc36da | -12.76229 | -44.40965 | 2025-06-16 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d1bf279-f16c-3050-bb69-01523ff6f206 | -14.08998 | -45.091 | 2025-06-16 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6f6b997-cb57-3c5b-afb3-f7843c127b4e | -10.73775 | -44.49876 | 2025-06-16 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65768cc5-1add-3efb-ac30-e049e8ba8d1c | -11.02793 | -44.64205 | 2025-06-16 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54424579-8f65-3dc3-aa10-1e7773f3ee9a | -15.40771 | -47.84923 | 2025-06-16 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa5a97a9-0386-36f3-aa62-024c42b6aace | -12.72712 | -46.27702 | 2025-06-16 04:27:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 820995e7-1485-3f9c-ad17-d3979a681568 | -8.74657 | -47.1747 | 2025-06-16 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0afbd4f-dbe4-3cbc-a403-255dbcaf63cb | -9.41587 | -48.43167 | 2025-06-16 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5cfd114-a7c3-38f4-8569-99713430940e | -15.56966 | -47.85698 | 2025-06-16 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5adbeaa8-ae3f-3b88-aeac-8bad6ed3f182 | -14.82799 | -48.44994 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 218de017-6284-3bde-8689-317cebdd9a83 | -11.011 | -55.05006 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2d028e71-0d6d-3f37-ba0a-2a79a8e05162 | -11.0115 | -55.07884 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9228656b-1b7c-34e3-bda3-8fcef3ee4ee0 | -12.05837 | -48.08045 | 2025-06-16 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be0c1c1d-d952-3e10-b368-dc7a9c7d73fc | -9.16428 | -45.32553 | 2025-06-16 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29aa9c1f-6ff7-3194-959e-598cc44d1d4f | -9.4058 | -48.43004 | 2025-06-16 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4968e522-19cc-343a-82e6-298287a0f4cb | -14.83733 | -48.45515 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 074ddfd9-4e47-38ff-9d93-3537452d9c94 | -11.00259 | -55.06966 | 2025-06-16 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f3029669-9caa-3a7a-9067-1448a65a3bf3 | -8.90048 | -48.84332 | 2025-06-16 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3d9f931-de07-3899-9540-71b997e9beb5 | -11.40884 | -47.62607 | 2025-06-16 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README7.md)
