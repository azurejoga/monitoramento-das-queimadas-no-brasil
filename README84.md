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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59fd808c-9dcc-33b7-b15d-edb9b864ad56 | -11.44982 | -43.39025 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 85d08e0c-e430-3eba-938c-0f8b070972b5 | -11.8043 | -43.55492 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6612d630-786f-3090-979a-8aa0eeb85d35 | -11.7297 | -43.4233 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 141460f6-013f-3c42-a494-bf6cfcb2c684 | -13.34929 | -43.86123 | 2026-10-02 11:45:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 01545e10-bcb3-3131-b193-13c31105379e | -11.72782 | -43.43769 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a5cd962e-0ca4-3972-83c8-c71be22ca32f | -9.8257 | -44.8011 | 2026-10-02 11:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 9abe77c7-1da6-317a-bc56-0758d6ac703b | -11.2629 | -44.2598 | 2026-10-02 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 65752f05-a4e1-3926-9bfa-6bd7674ce6c9 | -11.1611 | -44.6234 | 2026-10-02 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 96768483-09f4-356b-8d84-d43b7ab592f6 | -11.1427 | -44.5796 | 2026-10-02 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 12dc9c7a-c130-3524-b0f4-eb7731f4cc24 | -9.8254 | -44.8242 | 2026-10-02 11:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 203e8cc7-d0e7-37ca-9494-1706b70fda86 | -13.8037 | -45.2287 | 2026-10-02 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 67b359da-bc22-35b5-a9ba-dc4ddf8c090d | -11.7169 | -43.5098 | 2026-10-02 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 28300d36-9598-30b9-9a93-ea8239798058 | -12.4737 | -44.1435 | 2026-10-02 11:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 196.0 |
| b4c18e9f-65ea-34f4-a921-71a8a20f0bfc | -9.8444 | -44.8218 | 2026-10-02 11:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b18c6bf9-befd-3ce0-8560-8603bfc30d04 | -11.1424 | -44.6029 | 2026-10-02 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| d8beba44-9672-332a-9dc9-10e222ff444d | -13.8032 | -45.2521 | 2026-10-02 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 274.1 |
| 2bb5220b-b9d8-387d-8d13-cf23ac44f5c3 | -11.7362 | -43.5068 | 2026-10-02 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| bd0f68b3-0d79-3d8b-8bc9-4543dc8130be | -12.4544 | -44.1466 | 2026-10-02 11:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e7619ce5-654c-3aab-8a8c-3ea1e29c43ec | -11.1615 | -44.6002 | 2026-10-02 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| cdd6c009-46af-30a8-bb65-9eb60acf2746 | -12.4544 | -44.1466 | 2026-10-02 12:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| edc188eb-33d5-37f5-b547-5c9adc52592a | -11.7375 | -43.4356 | 2026-10-02 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 16d5d3a6-318c-3314-b00e-90c9762e6993 | -9.8254 | -44.8242 | 2026-10-02 12:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 4d2cb942-c23e-3ad3-b55d-ffa8a4d557c7 | -12.4737 | -44.1435 | 2026-10-02 12:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 442.7 |
| 59622397-08df-34eb-874c-cecf3aa0da68 | -11.1615 | -44.6002 | 2026-10-02 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| e60c8397-bcbc-368f-a166-9f7c13abe2f0 | -11.2629 | -44.2598 | 2026-10-02 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 70d12fc8-f5dc-3d6c-9c5a-a3a3943cc1cf | -13.8032 | -45.2521 | 2026-10-02 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 338.9 |
| 3a74933f-3f4d-36fc-a039-6a21b0eda721 | -11.1611 | -44.6234 | 2026-10-02 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 07cb5d09-6ebd-3341-8d8f-313b95ab0858 | -11.7169 | -43.5098 | 2026-10-02 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 89438d83-b334-3055-9a98-07852f6f9f3d | -9.0844 | -44.9811 | 2026-10-02 12:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 2bd33840-63a3-3be9-910f-42b491eb24d4 | -11.1424 | -44.6029 | 2026-10-02 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 8e6fd1a3-9490-3c30-866c-14617f1968f5 | -11.1236 | -44.5823 | 2026-10-02 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| c328395f-227f-38f2-8309-de91c009b2fb | -11.1427 | -44.5796 | 2026-10-02 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 106802a3-a8ce-33e9-930f-c693d1cea09e | -9.7877 | -44.8058 | 2026-10-02 12:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c310f199-c825-359a-96a4-1ea31c0ea8a3 | -13.8037 | -45.2287 | 2026-10-02 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 9bf24c4d-ac24-3a9e-b3bf-b0fbf4f44c53 | -9.8257 | -44.8011 | 2026-10-02 12:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| fa95f6f2-62c3-338f-b722-e91eabea1758 | -9.844 | -44.8449 | 2026-10-02 12:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 5cfd4f7e-8b09-3583-bca4-67933fc00dcb | -9.8444 | -44.8218 | 2026-10-02 12:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 38ef2a92-7134-3104-9eff-dfd4d2b2bd87 | -12.4732 | -44.167 | 2026-10-02 12:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 5be16092-528a-3e32-942e-aa60dc8bbd60 | -11.6977 | -43.5128 | 2026-10-02 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| acf27096-e2f9-349a-845b-0bb7c92902fc | -9.7877 | -44.8058 | 2026-10-02 12:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 12ad64ec-7c3a-3311-9d5f-3230b6e09dc1 | -12.4732 | -44.167 | 2026-10-02 12:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| dac0c673-e37f-35bf-ba52-169f71976077 | -13.8763 | -43.6396 | 2026-10-02 12:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| cfce5076-62a8-3a0f-be39-0d5fc9ba90d7 | -12.4737 | -44.1435 | 2026-10-02 12:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 507.1 |
| 45301ebb-253a-336b-99cf-5260bee182f0 | -11.1611 | -44.6234 | 2026-10-02 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 9f39232d-9f7c-3194-81ca-4baa17c0b2ce | -11.1615 | -44.6002 | 2026-10-02 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| cef02a58-40e3-3135-b363-50c571eb3b12 | -9.8257 | -44.8011 | 2026-10-02 12:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 168.5 |
| c579438c-6bd7-3933-9e0e-d65d042a07af | -11.1427 | -44.5796 | 2026-10-02 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 34118568-6cf5-3bb8-807c-a45c3e73bb87 | -11.6977 | -43.5128 | 2026-10-02 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 8c14c132-92fa-371e-8aa2-75a7fcac93bf | -11.247 | -45.1886 | 2026-10-02 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 32c98f24-5c49-3382-ab15-861e00716710 | -11.2466 | -45.2116 | 2026-10-02 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 3a212725-02ad-32d1-92ed-fae2446894ad | -9.844 | -44.8449 | 2026-10-02 12:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 241.2 |
| ad7e8925-a173-31e3-9e1a-b75724a320d0 | -12.4544 | -44.1466 | 2026-10-02 12:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 88f5e5be-3d38-350b-9616-1665bb3d5bef | -13.8037 | -45.2287 | 2026-10-02 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d148a59d-c371-328a-86d5-867f5022b95f | -13.8032 | -45.2521 | 2026-10-02 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 286.2 |
| e8c19f60-b23e-3ba5-87f2-1909dc42a9d9 | -11.1424 | -44.6029 | 2026-10-02 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 82347406-8200-3a90-8e39-539ce80b3f6c | -13.8568 | -43.6432 | 2026-10-02 12:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 43d65c7e-8396-30ba-a779-c17472708048 | -9.8254 | -44.8242 | 2026-10-02 12:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 1147b627-45b1-3498-b1a0-a70710600bb0 | -11.7169 | -43.5098 | 2026-10-02 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 5eee0874-4f13-33a1-b5d0-d788b8f21905 | -9.8444 | -44.8218 | 2026-10-02 12:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 4a5999d4-ba04-3e2d-be97-ee3fd93df04b | -11.2629 | -44.2598 | 2026-10-02 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 8c7c6e13-1a1b-3270-b3b7-4d7f9afc4b7d | -11.7375 | -43.4356 | 2026-10-02 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| b528ade0-51a0-33d9-820b-9c70b6012b19 | -11.71 | -43.6 | 2026-10-02 12:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ebb3990-7f03-37b6-858b-e01b5232bd03 | -13.81 | -45.25 | 2026-10-02 12:15:00 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 693c216e-c17e-3723-b1fb-2912d4e8d840 | -12.47 | -44.16 | 2026-10-02 12:15:00 | MSG-03 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ddd37e9-9198-3f09-8bc6-580981f2ad95 | -13.8763 | -43.6396 | 2026-10-02 12:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 181.1 |
| d643996e-1f80-3811-b7b6-571222222c5e | -9.8444 | -44.8218 | 2026-10-02 12:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 5a3784a1-8f53-3c87-8737-9d2341ee7590 | -11.2629 | -44.2598 | 2026-10-02 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 7716101f-f616-3d95-859a-f73f28170c9b | -11.1427 | -44.5796 | 2026-10-02 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 8584c501-4869-3245-9cc9-7fb50ef79c0b | -11.2278 | -45.1913 | 2026-10-02 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 6db87937-74d3-3e42-9357-0a35f79f0280 | -11.2434 | -44.286 | 2026-10-02 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 94a5c4f0-8501-3383-87e3-e3aaa4c46c3e | -11.7169 | -43.5098 | 2026-10-02 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 6c1817d0-c0d7-3941-9c11-45de0b2bcbab | -11.7375 | -43.4356 | 2026-10-02 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 2dfc1310-7554-338d-bc1f-83cd40710d02 | -11.2466 | -45.2116 | 2026-10-02 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 9c47c087-d10b-3ffe-af53-f2002eda9628 | -11.7182 | -43.4386 | 2026-10-02 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 48c82425-df11-3ac5-895e-7bfd3529ce17 | -12.4544 | -44.1466 | 2026-10-02 12:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| dcab8475-9e9c-3105-8b50-f872787217df | -12.4737 | -44.1435 | 2026-10-02 12:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 486.0 |
| 3fcbd12a-34d8-32fa-81ac-09b02d2185dd | -9.8254 | -44.8242 | 2026-10-02 12:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| e166c1ed-322b-3278-821d-afee054b9472 | -11.1424 | -44.6029 | 2026-10-02 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 07c68a1c-f858-38ff-9d79-f19e4fca69b8 | -10.9262 | -43.8406 | 2026-10-02 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 381e5a26-14c1-32ae-97c6-a16ae545dff1 | -12.5329 | -43.091 | 2026-10-02 12:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 9f55646c-e473-3106-a499-6fcb1d15aca4 | -9.7877 | -44.8058 | 2026-10-02 12:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 821c33b0-d95f-3286-9f81-9c56f9d127e1 | -9.8257 | -44.8011 | 2026-10-02 12:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 310d304d-e5ae-37a1-a840-9ff447ef4a05 | -11.1615 | -44.6002 | 2026-10-02 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 347fba1f-75ce-37bf-8603-9aceaf2b29eb | -11.7187 | -43.4148 | 2026-10-02 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 546bec75-493b-3025-bbc9-b7459e15097c | -11.247 | -45.1886 | 2026-10-02 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| bfd201ad-d11e-3351-9aa2-b9957eb7d413 | -11.1611 | -44.6234 | 2026-10-02 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 613f1209-3cd2-3c96-8140-d57d7f4b6734 | -11.7567 | -43.4325 | 2026-10-02 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 3306e056-a5a9-3e15-ae76-75a5792af4ef | -9.844 | -44.8449 | 2026-10-02 12:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 27897e64-97db-3efb-854b-30bff4590ec9 | -11.2242 | -44.2888 | 2026-10-02 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| e454083b-bcc7-3b14-a05d-e4eebe5c666c | -12.4732 | -44.167 | 2026-10-02 12:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| b14f2556-6948-34fa-b0bc-f34d306be5c9 | -9.0655 | -44.9832 | 2026-10-02 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 711a3ce6-1e31-3554-8507-920284679182 | -11.2629 | -44.2598 | 2026-10-02 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 293.4 |
| 04ffae2e-0969-32ed-9a8b-0f6c37bb1f26 | -11.2434 | -44.286 | 2026-10-02 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 14e5e8cb-86f2-30e7-9766-eec8fcabe4b1 | -13.8037 | -45.2287 | 2026-10-02 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| b1de3464-f698-374b-9798-ea09c83ae95a | -11.7375 | -43.4356 | 2026-10-02 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 839f7f21-55e9-3d60-baf5-67204de4e2ab | -11.247 | -45.1886 | 2026-10-02 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| c6fd3c10-083b-3508-963a-8efd198a2436 | -11.1232 | -44.6056 | 2026-10-02 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 18511498-75a6-33a9-9776-a9b29473f049 | -13.8032 | -45.2521 | 2026-10-02 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 333.7 |
| fb83485e-4436-37ac-831f-75d5cca81dec | -13.8573 | -43.6193 | 2026-10-02 12:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 179e9310-36d9-3932-ae24-71e3f0231654 | -11.7563 | -43.4563 | 2026-10-02 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |


[Clique aqui para ver as próximas entradas](README85.md)
