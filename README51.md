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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5b38e9b-720e-3fa7-a182-875e2d4c72fe | -12.86022 | -53.50725 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e645380f-11b6-31bb-9b9e-75041420e0b6 | -12.85984 | -53.51411 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 032e9999-6f82-3367-b9fa-db1e087669f8 | -12.85941 | -53.51138 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64034168-0438-3840-a177-38656de3b6d4 | -12.859 | -53.51825 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9905f25c-43cc-38fc-9c31-32e05761953a | -12.85861 | -53.51552 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eab9ec5-bc43-37c7-9cbd-7bd43d57b5ed | -12.85816 | -53.52239 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 740df332-708d-3329-923d-ac34fa78e38f | -12.8578 | -53.51966 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c672fe4-ffd1-3b1e-a528-fc6726924c13 | -12.85732 | -53.52654 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ef5893e-61dc-30e5-befd-655accbc51f2 | -12.85699 | -53.52382 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a58cc817-f5dd-3fc3-b9d2-ad8b94aa6a0b | -12.85648 | -53.53069 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd68c11c-ac46-3f77-bb35-3a686ca1b758 | -12.85617 | -53.52798 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35f19697-9c75-3efc-a36d-609970458046 | -12.85536 | -53.53215 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a69c2fb-2a31-33d4-9d1c-db267776dd32 | -12.85499 | -53.50872 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd23bbea-19f4-3f3d-83bd-a3d6f6baf3b2 | -12.85415 | -53.51281 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48b882b7-ed8a-3fd0-acaf-79bee55b5768 | -12.85372 | -53.51008 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0474ff1-a152-33e9-b0ba-1f67ae2076e2 | -12.85332 | -53.51694 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3565e9f5-236e-3cb7-aad3-2e168afe79e5 | -12.85292 | -53.51421 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d43589b6-390c-3070-94fa-b8b90359d94c | -12.85247 | -53.52108 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97f95e7e-d201-3e51-9aee-8fc34129459d | -12.8521 | -53.51836 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fa59cd7-419a-3e28-9103-7896125cdcdc | -12.85163 | -53.52526 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d498ca8c-be39-30b9-9363-506388d59c87 | -12.85129 | -53.52252 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a02eec-14d3-3c2a-910f-e419f0eeaa7e | -12.85078 | -53.52945 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec273682-2a06-3b7c-ae6a-03eda12cd3d4 | -12.85047 | -53.52672 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fac37d4-73ba-3f9d-83fa-1bdbca053c2c | -12.84965 | -53.53092 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d3c0b22-798e-32f6-b046-d38ac07ac1b8 | -13.01254 | -53.47057 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ce7ed27e-389a-3b41-8b6a-d216f15caee0 | -13.01175 | -53.47451 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5045679e-9aa5-39b9-823b-048b8e98de6e | -12.98829 | -53.5028 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4c5f7b4-b6da-313e-8d32-9e4382a39977 | -12.98748 | -53.50682 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57562a7b-8362-3e0a-847b-34d7110b0316 | -12.98667 | -53.51085 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8aa5656a-397b-3123-a2ed-c90e0cab55d0 | -12.98585 | -53.5149 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caf3178f-4634-35e2-aacb-0c68a3d90351 | -12.98097 | -53.50965 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f00727b-ca89-3a66-8d18-492ddf66847f | -12.97197 | -53.52481 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f04024fe-3be7-35fb-a928-f9c5a6eef793 | -12.97113 | -53.52894 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7815f588-a088-393a-b219-1f64eb674471 | -12.97063 | -53.52489 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02c6b2cb-feb9-3be5-85bc-effb718d06ea | -12.96983 | -53.52903 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b932319-fcdd-3128-bb1f-5790de378d8f | -12.96902 | -53.53318 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25755cdd-bd67-30b8-8fff-d3c02baf22f5 | -12.96862 | -53.54134 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4da2911-639a-3552-a1a5-77e08974b8e3 | -12.96821 | -53.53733 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51836fe1-8b78-33c8-ae41-8cf1998d438d | -12.96794 | -53.51537 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99dab9d4-d0c2-3ffa-8481-a00f3c8650d1 | -12.9674 | -53.54146 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c263b4ed-1e54-3c20-8616-c1eb5a1f4100 | -12.96711 | -53.51945 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c452998-c657-3df9-8fb0-ae152bbed292 | -12.96655 | -53.51541 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b8c1b76-4f11-3e65-a5dc-3a7ac54f5026 | -12.96628 | -53.52355 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2875713c-52db-3610-afbe-bebf292928d7 | -12.96575 | -53.5195 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3090e26-fcb2-3dae-af6a-26f5c8561226 | -12.96544 | -53.52766 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 663757bd-0bf4-3fd2-aeaf-a40de09f4a64 | -12.96495 | -53.52361 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76e69292-af2d-3eff-853a-ee2ccfcf48b2 | -12.96461 | -53.53179 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8adec249-420c-3569-a90c-2e1e0d1212d1 | -12.96414 | -53.52772 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1d6801ad-540c-39f7-a4cc-48389b9f7348 | -12.96376 | -53.53594 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 34b4b86f-e94c-3794-a3fa-85112ec87933 | -12.96333 | -53.53187 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b4f1980f-1e30-355d-bbfe-3666d04133e7 | -12.96292 | -53.5401 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 26594af9-60aa-3c1e-b92d-c275fd0b294a | -12.96252 | -53.53603 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 06133c8c-d6ec-3797-a742-00a96379adff | -12.96207 | -53.54428 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b40536d7-01d0-33e2-a3d9-fb375f9ab364 | -12.9617 | -53.54021 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| baf65d03-d9f8-34a4-a817-2beecdd348cc | -12.96142 | -53.51822 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d33bdf3b-8817-387b-b7ab-9e521b91bb22 | -12.96088 | -53.5444 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cbf81371-4c7f-34b3-9cfb-1c6f3e00f955 | -12.96059 | -53.5223 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3c08d0d3-248b-338b-9122-a47ec0a0d920 | -12.96006 | -53.51826 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 634f5a1f-30ff-3e3f-9551-48d81b4558c8 | -12.95975 | -53.52641 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7c6b1b1f-47a9-301b-8a35-65fae255fea9 | -12.95925 | -53.52236 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 33c304ac-da25-305f-b80a-909224421eb5 | -12.95902 | -53.50083 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6633597b-87a8-37a3-bae9-8597b0da1fb5 | -12.95891 | -53.53054 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ba11fc1c-10cd-37b5-b2d3-a0fbdf613889 | -12.95845 | -53.52648 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a2ed329b-f07e-3c25-9ada-d92e8a9d3e55 | -12.9582 | -53.50486 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86a3069d-359f-36a2-8b43-e02b0cd81f1d | -12.95807 | -53.53469 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5574dbf9-2a52-390f-8ff6-1a3c0d29df8d | -12.95764 | -53.53061 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 29bda10b-416b-3fa1-8d9b-fc1749a9ee8b | -12.95755 | -53.50081 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2ca9f7c-9363-3154-ae11-8c6e127a8f97 | -12.95722 | -53.53885 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a5c24a2a-aa27-3a8a-b7a5-b9ffc340b415 | -12.95682 | -53.53477 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 872ddc67-14c1-35c2-aa00-c974dcb14375 | -12.95675 | -53.50485 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2137dd3-9d7c-3cd4-bd50-693cfce698a1 | -12.95655 | -53.51294 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5e4e9ce-2a80-3f6d-b51a-30ab5aca56a6 | -12.95637 | -53.54304 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ddd5f3c1-3bef-3811-aae8-2172c5a39f0a | -12.95601 | -53.53894 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f167e59e-7eb2-3d6b-b3ec-bda5c14c1cd3 | -12.95596 | -53.5089 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a3d9978-3c01-3ef0-867a-5cd283798dc3 | -12.95572 | -53.51702 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a979334-86c2-37b2-a07d-09bc1a541253 | -12.95553 | -53.5472 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ad5e237d-bd37-354b-90e4-ee02bc0a3f18 | -12.95518 | -53.54315 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 266f1700-029b-3cd6-bb26-0fa22933d964 | -12.95516 | -53.51295 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 002d73fa-dd47-3c8b-a1a7-b749587a1e58 | -12.95489 | -53.5211 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e5820867-f71a-33eb-b5c0-c56be2867f7e | -12.95437 | -53.54731 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cb16ac72-6006-3b77-8c3b-b07a1214028f | -12.95436 | -53.51704 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 138b773f-1be9-3f3b-9e5e-57f54b0d7817 | -12.95405 | -53.52521 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 46c62efa-68a1-3c3a-85cc-51142d013e61 | -12.95355 | -53.52114 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e03d4aec-9359-30e0-ba44-00871b240829 | -12.95332 | -53.49965 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf744dd0-48a4-3a00-a81c-77b1a2c84df9 | -12.95321 | -53.52934 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 3e1e0e51-ec43-3ce7-86d0-bf692de122f2 | -12.95274 | -53.52527 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 245f0d47-4f24-37c0-95fa-3bdcb6b94986 | -12.9525 | -53.50368 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd1efc32-9b32-37e3-adbf-953364c3c76f | -12.95237 | -53.53349 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 3de45cd4-74c4-3fa7-89ab-088a64cf593b | -12.95193 | -53.52942 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a35678e0-78fa-33b1-87b6-000bdbd5caaa | -12.95168 | -53.50771 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 127426b6-be4e-3810-b4e3-60def9781f15 | -12.95152 | -53.53764 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b4ce43dc-b45c-3b45-aa1d-e657533d3d3f | -12.95112 | -53.53357 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 241bf4a4-1759-3bf7-96dc-9a18e8a3a64e | -12.95105 | -53.50366 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 011a2c5d-fccc-33ae-8958-14bb7959a275 | -12.95085 | -53.51175 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d36f06e-3e95-3714-88ec-2b5b0311dc15 | -12.95067 | -53.54183 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3728c57c-687f-356e-ae53-73211709aaf2 | -12.9503 | -53.53773 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 23e3e542-1ac8-30e0-a3b9-bf461af80616 | -12.95026 | -53.5077 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 641a4832-2364-3e44-9be1-4f995b5bbcd2 | -12.95002 | -53.51583 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60c07622-073e-3ca2-b087-ab8856d21a15 | -12.94982 | -53.54599 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c5c1fadb-6dc1-3c83-a6ea-e7c1669bd83a | -12.94947 | -53.54193 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |


[Clique aqui para ver as próximas entradas](README52.md)
