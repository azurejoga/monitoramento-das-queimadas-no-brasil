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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 747b6262-2034-3b2d-9290-bcb1e53e597a | -6.8117 | -59.66226 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e425e93-e2a2-31fc-9df9-6de1111f1762 | -9.12703 | -61.59743 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d4862f6-96cb-366a-b277-9b1ea6e7b3b6 | -6.90018 | -59.00306 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5087295-d276-3c26-945f-dd94d0402238 | -6.36315 | -62.8989 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 808c4ed1-cb08-325d-963d-b8b661569680 | -6.80252 | -59.43127 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f39e956a-cb95-3e12-acd0-d4ff2ff61dd7 | -6.85889 | -59.45036 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0e52a3a-7ca2-33e2-9e58-cb9fbafbb53c | -6.7836 | -59.42233 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 50c91a03-eff0-3c8f-abac-515795e81df6 | -8.394 | -62.68498 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 43351ee1-51ce-3687-9aff-5777db98792c | -6.36795 | -62.90286 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79565457-5cd4-3bf0-8a7a-a0ff6b42d07f | -6.77662 | -58.66331 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 904dd25c-c0c5-365e-81a7-3012f09b0d63 | -6.77086 | -58.70774 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb550298-64bb-3126-83e5-7850003c69c7 | -6.79436 | -59.59301 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99f7099d-ff23-357a-8880-13ae5d1aea13 | -6.08892 | -59.95914 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fea0819-53d4-3d7c-9284-1378d6d3137d | -6.86839 | -59.03547 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98e15229-09df-3460-8a84-7480927f80c0 | -9.17918 | -59.46003 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5a38d2ac-09ec-3a43-bb54-99d15e3c9a28 | -7.60175 | -60.93839 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a51a7b1d-beb3-3e54-8229-045d5230532d | -6.85082 | -59.40884 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c70f945-eb4d-3582-9e64-35d37e7aed2c | -9.17554 | -59.45251 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| eb54f793-75bd-3826-95fd-028c7c0d9d01 | -9.11626 | -61.58706 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 87fa3c62-0568-3cf5-a220-5d3cfb26ff40 | -6.78013 | -58.6902 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| fbceaa3d-6bf8-30db-8f0b-3e3d85332a58 | -6.26984 | -62.52714 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46caca44-1876-341c-a98d-af0fc52233ab | -9.15893 | -59.45719 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1b333d37-b0db-3ffe-a52c-6a957770601d | -9.21178 | -60.76982 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed099e55-aa8e-332b-b109-7c8aeb144409 | -6.75682 | -58.65395 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b7273428-8016-3dd9-96ec-67f20be509ef | -6.13766 | -59.90527 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82b46524-0186-36a8-9bb9-0704f62c9eb4 | -6.80987 | -59.42633 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 25803b32-0962-39d4-a034-8ec5ecfd2c98 | -7.86519 | -63.76865 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51993efd-3690-3614-82a3-5cccffe33727 | -9.04968 | -60.44724 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8cc9cff8-1b51-3105-8a18-53077ae5d157 | -9.18156 | -59.45965 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 11280027-bf84-356d-bb40-270445769e30 | -9.21001 | -59.76732 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4518058a-c7ba-364b-bca5-295debd644b8 | -6.86917 | -59.02959 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2453f046-4376-393d-b7b4-14efce3da432 | -7.87374 | -63.74294 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7470609-f03a-34cf-879d-42c8c138666b | -9.41699 | -60.41311 | 2026-08-22 06:08:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9ee29f5-084f-383a-9b03-ea080455cdd8 | -9.1152 | -61.59567 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a11542c-9e20-352b-b14a-9b8dba3fe72c | -6.81719 | -59.4217 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1dd7747b-cb3a-3599-bc55-9970ad07d56f | -6.8165 | -59.41511 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 622cb545-24ee-35ad-9656-78e3f03ffdd5 | -7.60717 | -60.94389 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b7bdf16-9e18-34db-9f98-6b7dbaa1325d | -6.08962 | -59.95404 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a887318-b1fa-38b2-a88f-8423294980a2 | -6.7706 | -58.65575 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fb3c0eb5-37c3-3860-b6fe-efb937ea79b2 | -6.36746 | -62.90332 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1218aa9d-c7a8-3679-821f-5cbb9cb5e991 | -6.96459 | -59.05462 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 06a8126e-c46e-3101-bba1-b425224718bf | -9.11573 | -61.59137 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 360f57d2-071e-3e6b-b179-6bcf6ed90636 | -5.91735 | -61.29867 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a79ca2e3-e4e4-37df-85d0-aef6425f28fb | -8.89413 | -60.54002 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 809dc33d-d627-3ada-9981-4e7f552c2610 | -9.18904 | -59.45453 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2cbbb3d6-5f45-3dab-9bcb-5d489c7301c0 | -7.67134 | -61.12287 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a3e31e3-1fc1-3215-936e-888b656ca6a7 | -6.78434 | -59.41666 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| e48b1f1b-56da-3e37-9fab-bd4c31d1b774 | -6.80136 | -58.63489 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b104b1ad-d135-36b5-9458-14fea4ad7223 | -5.90634 | -61.29297 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4aff5069-5394-3658-8031-d1d5148ea114 | -9.12164 | -61.59232 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7438eb56-1cc7-3ccb-80d8-01f8566b8664 | -8.40349 | -62.69729 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92deaf6e-744b-32d6-8e3c-4180c83cea26 | -6.81795 | -59.40365 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 247e425d-43d7-37b7-86db-69ec08269684 | -9.16492 | -59.46426 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 856ca932-2b58-3da1-986e-c5ce630eb953 | -6.82298 | -59.67529 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 4b21c63e-d6a3-36ef-8b0e-ad49cebc1f69 | -9.54045 | -63.56247 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d448d506-680d-3b2c-ba00-851df06e6fea | -9.18083 | -59.46579 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 50f761d3-e1b2-30ac-9f41-b4f6d02d99c0 | -7.61084 | -60.97725 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66a399fb-ee14-367e-8ac8-d195971da164 | -6.25913 | -62.52558 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa5ee93f-3c23-3a0e-b76b-6f092b88a618 | -6.79343 | -59.59793 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 432becfe-e2eb-3b3b-91f0-4b437aa4908c | -9.20968 | -60.76997 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cd36c97-bd39-3f4c-8e6e-5e4ac3e42320 | -7.87335 | -63.74589 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3298a4a-feb6-39ef-9547-5b477af85384 | -6.54237 | -58.5162 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 769651ed-3310-3a1c-b31f-8c3bbb4d240f | -7.87023 | -63.76939 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f0f575f-d72a-32d5-8d5f-b88e28221273 | -6.8115 | -59.66257 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18fc4233-9245-3e6e-8b7d-065251e1689d | -6.91707 | -60.06957 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 58f49274-c014-31c8-b57d-ae46f3b64d98 | -8.40443 | -62.6902 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10b09742-31c8-3ba2-b834-6025b57c6fb2 | -6.93842 | -59.30484 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42da5fe8-259e-34a6-863a-7e6ad044bd4f | -6.26542 | -62.51962 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f311e496-4708-3e2e-85a8-a8ee9161eb12 | -6.37269 | -62.90407 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be4caa4a-a043-36b3-a4c0-d843d1140b4d | -6.53302 | -58.5343 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 21d75717-3d91-357c-b6f9-a892e585d0d6 | -6.81208 | -59.39692 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f60bb5c2-c779-38e5-98c0-79e0279d47c1 | -8.3876 | -62.69127 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| b0069cf6-6f5c-3073-be46-7d927680fad9 | -6.82452 | -59.41696 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e5a1f873-a138-394e-82cd-d9c021e6c9b6 | -9.17841 | -59.46616 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| eeaf7c11-9b12-30af-bb15-28d8fe4d6ba2 | -6.79443 | -58.6342 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7ac5791-a779-3d15-b169-72a7225bbfbb | -9.17167 | -59.46514 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cfb03f19-d711-3fca-ba70-5d15d9da9960 | -6.09589 | -59.95518 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6fe2db5-9448-3b50-8086-9601955ba6eb | -6.85743 | -59.46167 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f6afeeae-0b03-389d-8de6-b05f2fe73990 | -6.76891 | -58.66877 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| adef42e0-447b-3af1-bb8f-7f068fa4b291 | -6.86244 | -59.02855 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4274b02-9319-3bb6-9a0f-4e060cd5826d | -7.60282 | -60.94376 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99e17a50-a29a-3299-b548-dc9dad81af86 | -6.9517 | -59.30665 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be8ed63f-6d85-345b-ae11-6b2de2c4dd6f | -6.78755 | -58.63319 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68484db2-0500-365a-87fb-70e7b4ad4fe7 | -6.94104 | -60.08335 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a19366a-c43d-3000-98ff-bad639a7be22 | -6.75515 | -58.66689 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e24d82eb-5068-3a7e-94f6-0ea5b72846da | -6.13066 | -59.90943 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4a589c9-290a-3561-9348-7dd1ee1fcf14 | -8.89353 | -60.54508 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c310d135-82af-367c-9e62-52fc1d24bc2d | -6.54073 | -58.52909 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 207d7554-2674-39d2-b2b3-1ca7a16789f4 | -9.28691 | -60.90555 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c299dac-38a2-3e57-b99a-5fc4eabda65f | -9.11641 | -61.60326 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 945a13cc-3cb9-3cde-984f-bb30047677d7 | -6.93644 | -59.30305 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66aad439-5776-368b-aa21-c325e2fc2454 | -9.11696 | -61.59906 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b2b3e87-9b5f-3216-b974-ebbb31e7ca71 | -9.0474 | -60.44674 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 574afc80-abeb-36c1-a604-95f710b676e9 | -9.21901 | -59.76744 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01ace94b-ac5a-333e-9987-e7e64f97caf3 | -6.8182 | -59.66305 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 93b96d27-3558-362f-aa67-331f0f01fa51 | -6.94829 | -59.31621 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c0580f6-5051-33e7-8393-9924b1942699 | -7.01829 | -59.55282 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 247d984e-c415-313c-94a6-63ef66edfd23 | -9.17481 | -59.45865 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f84ef6d3-714a-3b8b-b8a3-f6ba7b92954f | -6.81064 | -59.40847 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be4dafc9-3672-333a-aa6f-15b698e5c2f3 | -6.94164 | -59.31541 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README79.md)
