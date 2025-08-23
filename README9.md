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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1acec1b2-b7c5-3d2a-9094-a5ea9b1add0d | -9.93449 | -65.00848 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b410981d-0af4-3e77-b244-a9f2a115fe96 | -9.83475 | -64.26383 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1846889b-67e2-3600-94e5-cfdcf330af59 | -6.68736 | -58.86722 | 2025-08-23 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 4b3f27bf-9a7c-3410-98ef-0c96dbaeab9e | -7.57195 | -63.4376 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 72a9b99f-2a6b-353a-aa89-25fe8cadb568 | -8.59596 | -62.63161 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.7 |
| bd9820e4-4755-359f-8068-f07fc0fb3e8b | -9.82683 | -64.2756 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d95ef4e4-0b5c-36c5-98e0-52cabfaefd81 | -6.57415 | -59.86981 | 2025-08-23 01:49:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| df7180bc-b83a-33c4-bc43-4edcd6cdf4dd | -9.82119 | -64.27177 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 9f69cdf1-e0a7-3fce-824d-62dc3ed9899d | -9.94593 | -60.16629 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 5568c8ed-d470-39c8-9858-5f8b98fbd94d | -7.72589 | -67.06227 | 2025-08-23 01:49:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de48d385-bb15-344a-bf91-87de618ec350 | -9.94979 | -60.1918 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 545.9 |
| 682ab22e-d6c2-361f-8221-5b768d47710d | -8.89859 | -62.43991 | 2025-08-23 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| bb74843d-a28f-3931-9ddf-78584e791d78 | -7.78846 | -61.57237 | 2025-08-23 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f2bbbb83-1081-32ef-9060-903eb6b3dd37 | -7.82537 | -63.56662 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| d144cb81-25ba-3990-b563-b65ec27f1ade | -7.73723 | -67.06339 | 2025-08-23 01:49:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1d27bf1e-8a4b-39c2-88de-4319af80d347 | -7.43064 | -60.62685 | 2025-08-23 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| e9d0903b-826d-301f-b6e1-9edd5ad8dce2 | -9.94919 | -60.18627 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 538.2 |
| c6b5cc64-1ac4-330d-bf9a-c12fe3ec931f | -9.5075 | -60.55341 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 187d3210-a5d4-32d9-9917-aa8d47fb701a | -8.62912 | -63.67082 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 443fd890-d975-3e8a-9254-489cce860643 | -9.94669 | -60.17179 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 364fd57f-795c-3cee-b43b-285892ee13ce | -9.53399 | -60.54252 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 154416b2-caf7-38bd-b293-fdc37f04bfc1 | -9.23352 | -60.47385 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 2713dc65-65a8-3808-b6cf-6180dcc92be0 | -7.72712 | -67.07112 | 2025-08-23 01:49:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 81332a3b-4332-322c-88d2-e143c51febc1 | -9.21536 | -60.7969 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| b349a6a9-5382-3053-accf-34228efd464b | -9.19856 | -59.61797 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| e25eb89d-8ee9-3244-a782-9131d15cca1c | -7.82358 | -63.55457 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 9219774c-f828-35a7-b314-1c4548ff3e68 | -9.20319 | -59.476 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| bd09fe5c-5229-3cf1-8aa3-cfeb5c4feb5e | -7.81341 | -63.55618 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 52d277d9-fc73-32f5-9517-0021cebb5c95 | -9.95287 | -60.21169 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 42339cfd-2fc2-3eb1-8ba2-a2e189c57f51 | -9.95242 | -60.20613 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 226.4 |
| 9f6da0e0-2250-3c37-aba6-ac98f0e95838 | -7.55064 | -63.85556 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| a0db0951-8986-36a8-92ac-a4734728ff02 | -7.80504 | -63.56974 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 246c0b9b-0a99-3141-b812-012800055450 | -9.22557 | -59.75726 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 1205becc-6058-39ce-a05e-15431ba7a072 | -9.18501 | -59.62001 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 61342804-9be0-360c-8c5b-c2368ab049ce | -9.24572 | -60.47755 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 3e4ab9e4-6297-36dd-b65d-9e1e30fa6058 | -9.96511 | -60.20389 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 47e2e86d-98d6-3523-8d3a-e78fcd2683e0 | -9.52953 | -60.53049 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| c3bd7613-d212-314e-a02b-7fb34e8097e0 | -9.83628 | -64.27415 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 8b303ebd-ee80-3338-aeeb-072d233c218f | -9.52661 | -60.5116 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 8798302b-262d-308b-9d70-1b049d8d08b2 | -8.90084 | -62.43304 | 2025-08-23 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 8416558a-2e6c-39aa-84a6-9f157b03d75d | -9.19307 | -59.46051 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 75294a6e-4be7-3e1e-8c6c-1d5a8eb843e5 | -9.81173 | -64.27322 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5cdbc009-ce5c-3d2e-abcd-4bdc97edf798 | -9.52289 | -60.5702 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3afa9ad1-89b5-34a1-978e-af5a099e68e2 | -9.51997 | -60.55135 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 848f7223-67f4-3317-b06d-4137d949e6c9 | -9.10307 | -61.4291 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 8f51cbf7-b586-3047-a7dd-202cb0d632ad | -9.51044 | -60.5722 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 103ba28b-61e1-30be-b3ff-34397e567f32 | -9.5016 | -60.51577 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| f8b8493a-218c-3498-bf11-b14063c05369 | -9.51409 | -60.51362 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| e2eeac6e-c846-3f2b-a66e-0b71ea26464c | -7.5063 | -63.83257 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5d9d9c84-eebd-336c-b09d-d7f810034115 | -6.68917 | -58.87354 | 2025-08-23 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 9a9b23cc-01f8-3b3d-83a2-692abd733456 | -8.88566 | -62.42775 | 2025-08-23 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8ac2d9fb-c208-39e4-b743-2dddbeab5d6f | -8.61542 | -62.6147 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a6943b56-bfcc-3701-9151-169a9e0c76be | -6.92949 | -62.89449 | 2025-08-23 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b583e4f7-9d3b-357f-81b8-e93dd10d5256 | -9.52458 | -60.56335 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 7830c58e-1aff-3d26-b250-93a231062191 | -9.95868 | -60.16415 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 76799634-8091-3fd8-932b-53f257e3e8dc | -6.56912 | -59.87643 | 2025-08-23 01:49:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 771f7c0b-2511-313a-a3da-81be7030b49d | -7.54975 | -63.8497 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e2a949ef-2332-366f-9d5d-127bbd6f3bee | -9.51536 | -60.50687 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 2d5b834b-0ef3-3eea-ba06-bd934bf9c190 | -8.61915 | -63.67234 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| da65e5d8-3cc2-3544-8cc0-e300e92868ce | -9.53094 | -60.52371 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 82ceef3a-bcbe-3509-9d71-07ffd388c466 | -9.51843 | -60.52568 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 7bcd7c9b-3f2c-331b-96ad-a603e20a1ba8 | -9.17394 | -59.60512 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 018657f5-777e-38a0-8c34-53e79931b144 | -9.21814 | -60.78983 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 36f9ea43-4444-3e79-a3ed-3c0daa66f277 | -9.51703 | -60.53249 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e3486a48-688a-3716-8467-33b942f6d77e | -7.55141 | -63.86127 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8c0d3888-300d-388e-947d-d45772e8c2a1 | -7.80324 | -63.55775 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| f0ecc77c-2b2f-3fcc-bcf0-6845aa08b18b | -7.8152 | -63.56818 | 2025-08-23 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 256b6675-004c-3395-b148-00425bc7847c | -8.8748 | -62.42947 | 2025-08-23 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| dd8c885a-cad2-387d-8150-0206e918d13c | -9.9619 | -60.18403 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 410.8 |
| f753829f-4f57-3a4c-9e57-f23756f0a30e | -9.1911 | -59.62577 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| c956023a-c841-3215-831d-d9a2f07744d9 | -8.59389 | -62.61803 | 2025-08-23 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b6cfebdc-81f2-3530-8936-8ffe5c255433 | -8.90945 | -62.43822 | 2025-08-23 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a5ef6ac4-6bdf-3912-bf42-dc243ffc3d88 | -6.578 | -59.89377 | 2025-08-23 01:49:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 060bcba5-dd1c-39a6-b9e7-550175d2f13e | -7.73846 | -67.07224 | 2025-08-23 01:49:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a4024232-34fa-3a00-a95b-25c3c8dd70e1 | -8.70405 | -62.88 | 2025-08-23 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 61421618-607e-31d7-a42b-049fb2214eaf | -8.69153 | -62.86868 | 2025-08-23 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 28.2 |
| a28a2995-bc6d-3f6b-bafb-2967f68fa74a | -8.89653 | -62.42604 | 2025-08-23 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f1c1088b-205b-3434-b96d-1f96c182d74d | -9.19941 | -59.45285 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 86f0b7a9-029d-3a65-a727-3f87dbae1471 | -9.18882 | -59.64289 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 70d3cce8-6f29-3e9e-b8a6-d1f01b91c4ec | -9.95563 | -60.22586 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 13bb0041-3efe-3068-b639-bfe73de4d5ce | -6.87167 | -59.82843 | 2025-08-23 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| fe3ddbc2-8f66-3a7e-94dd-0b19a1d23f87 | -9.9493 | -60.1947 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 467.9 |
| 7684cff8-ffd8-327a-b739-6684ad4b94a5 | -7.0352 | -44.6396 | 2025-08-23 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b4be57ec-6921-3fc1-8d01-2e21246b1847 | -6.6231 | -44.5608 | 2025-08-23 01:50:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 2dd328fd-6382-35bf-8484-1b3dbf26b023 | -13.0114 | -45.222 | 2025-08-23 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 55219283-fe84-3943-826c-cb8776905f8a | -17.5985 | -46.5481 | 2025-08-23 01:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 9537f15f-e92f-39fd-92a9-6edbe0aad409 | -17.5979 | -46.5715 | 2025-08-23 01:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| d0239f87-95db-3e13-b1c9-96835b020d81 | -12.9921 | -45.2252 | 2025-08-23 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 2e6c4491-a8a0-3033-b707-22ce222b4cb7 | -9.5366 | -60.5258 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 4e4db752-1ae3-3d0d-84f7-0e9448864801 | -6.4138 | -41.2132 | 2025-08-23 01:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 41c02bcb-f87b-3689-995c-d4aa12492ba9 | -5.7615 | -57.5807 | 2025-08-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 414f9255-b48a-3c23-937b-4a5dba8ed2b5 | -8.9106 | -62.4289 | 2025-08-23 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| db46c4e9-6830-3434-95e2-1e36dbba25b7 | -6.4327 | -41.2114 | 2025-08-23 01:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| a2317d8a-0aeb-3a00-910d-5f3958d35a15 | -9.1895 | -59.6364 | 2025-08-23 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7d5f3757-fd2b-3e34-8998-f4b197d64d13 | -9.4449 | -47.6585 | 2025-08-23 01:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 604120e9-ceae-3a34-a1ca-5f16f20ba8d9 | -14.6706 | -54.9142 | 2025-08-23 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5de1566a-c84e-3345-ae98-33d8ebd43669 | -6.6044 | -44.5624 | 2025-08-23 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 6f748bc0-5ded-3f56-8155-56a904eb8eba | -7.8314 | -63.565 | 2025-08-23 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5c144d65-ed66-324f-962d-772a2f2bdc6d | -5.7614 | -57.6002 | 2025-08-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| be9fca52-9193-3cd1-9605-84f5e82df321 | -8.8921 | -62.4297 | 2025-08-23 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |


[Clique aqui para ver as próximas entradas](README10.md)
