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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aec5c25-92ad-3a50-bde3-84fd7b5b1666 | -9.0719 | -50.4394 | 2025-09-05 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 367a0f7e-8b55-38e6-a17d-13974646ce35 | -8.4787 | -45.0932 | 2025-09-05 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4e508d90-5b16-3fc8-b141-01e77e17fb84 | -15.7565 | -53.6324 | 2025-09-05 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 938622c1-919b-3828-b82e-25b4aec19de4 | -13.8849 | -47.9481 | 2025-09-05 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 402ce669-2aef-3a39-b9ec-b4ad96fad569 | -14.0499 | -53.9914 | 2025-09-05 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| d19a3ae6-675c-3807-ac04-554229f3eb22 | -8.9034 | -45.7973 | 2025-09-05 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 4bd56ab3-9694-3e1d-946e-e6286d43d4dd | -7.7128 | -61.5276 | 2025-09-05 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 87616ab2-ea16-3382-8f0a-c5adddf36ea4 | -10.1491 | -46.0162 | 2025-09-05 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| e2890358-3fe2-3fbd-bcd6-da9f8e7eea09 | -15.7756 | -53.6509 | 2025-09-05 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 24c99388-ba06-32ab-bf52-76fba4beaac4 | -8.5374 | -51.3278 | 2025-09-05 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 200.8 |
| effc4eec-19c2-3fda-bc4d-1a17ae480f79 | -7.5797 | -44.6808 | 2025-09-05 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c67c8d6f-d4d9-3f55-9512-fa6d76ee8b93 | -15.7558 | -53.6746 | 2025-09-05 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 130.1 |
| b946ac8d-92dd-36f5-81eb-0eddba0c2a7a | -6.2609 | -43.2727 | 2025-09-05 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| a12a6466-99a0-36b4-9c46-aaf71e910a5c | -6.8654 | -52.7916 | 2025-09-05 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 77bba5ef-f4df-30e4-bd91-505751b82acb | -15.8588 | -52.2817 | 2025-09-05 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 7a598632-ecac-325e-b250-43541ff0c8f8 | -13.8651 | -47.9734 | 2025-09-05 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| db2f7b20-a359-367d-8c44-9f6d8216a684 | -7.53 | -47.4662 | 2025-09-05 14:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| fa88e479-ec60-33a0-929a-28efca34ffac | -8.479 | -45.0704 | 2025-09-05 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 2b21daf8-a61b-3faf-a799-17226587c282 | -13.8836 | -48.0152 | 2025-09-05 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 1b2a1d36-1578-338d-9fc0-47e8d265ea4c | -10.7688 | -45.2769 | 2025-09-05 14:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 04402871-9fc3-3979-b6d6-a15893851adf | -15.7561 | -53.6535 | 2025-09-05 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 186.1 |
| e95e4317-475d-3de3-97ea-7b669140d6df | -8.6883 | -62.4002 | 2025-09-05 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8cf79008-883b-321c-9143-0f621b2ef6fe | -11.864 | -50.7075 | 2025-09-05 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 432dde8d-269a-3f39-a4e3-a889e5e16519 | -6.3868 | -43.8206 | 2025-09-05 14:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| da92262e-20f9-36e8-af7a-9e33faf88b11 | -15.0445 | -50.0899 | 2025-09-05 14:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 33e3024f-63c2-3d79-8c91-ff2ab99b331f | -9.6916 | -48.9872 | 2025-09-05 14:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b5fede7a-a0b5-39a9-81e4-a4811086aac9 | -14.7465 | -47.4955 | 2025-09-05 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 2ee196da-3b32-381c-b83b-c0e11ff8716d | -7.6083 | -43.8477 | 2025-09-05 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| ae4ad79a-6621-37ce-9c4d-cb2521f49422 | -8.2001 | -49.5988 | 2025-09-05 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| be8b852c-23ba-3830-8f03-abc94d0f8cbd | -7.0314 | -43.2742 | 2025-09-05 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| b5bb5ca9-dc3c-363d-bf7f-8d53428d03ed | -15.3435 | -53.9382 | 2025-09-05 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 240.2 |
| 0172e75d-0985-3db4-b9f4-dffbca6ca2b5 | -13.2592 | -51.8186 | 2025-09-05 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e2447646-9108-3a47-866d-e6c028e1e595 | -5.9443 | -43.0178 | 2025-09-05 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| bc3244fd-b033-3ee9-a58d-bfa017eaa61c | -5.9963 | -47.6478 | 2025-09-05 14:20:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 5e9ad48b-bf4a-333b-8887-4e810805fe62 | -11.0051 | -45.9755 | 2025-09-05 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 923f5ac6-faa0-3fc9-b14d-f62abf0f55fa | -15.2877 | -52.6809 | 2025-09-05 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 694b6c21-2326-3413-b220-408894452e0e | -14.4882 | -53.0601 | 2025-09-05 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| ceb63808-ef94-3e16-b588-da7c5b8265df | -5.1585 | -45.1698 | 2025-09-05 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ce2a51ae-e7c2-3edd-a67d-15602cf636e0 | -15.7111 | -46.2281 | 2025-09-05 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 7ee774e0-0347-3db1-8ea2-45f6ca75507a | -9.7031 | -51.0802 | 2025-09-05 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 4090d40b-fc38-3b4f-ada5-d5d75ce9c076 | -6.1491 | -43.1885 | 2025-09-05 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 638de89e-fe7a-3f41-a960-e47fb237e74e | -14.0691 | -53.9892 | 2025-09-05 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 28cda01b-9d9e-33e9-86e1-4e7d03a7c281 | -5.9844 | -44.7489 | 2025-09-05 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 3be7be13-2ba7-3710-9419-4df4ec1f2677 | -11.0055 | -45.9527 | 2025-09-05 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 64941b8d-f937-329e-8145-1c7f179109de | -7.9252 | -63.2608 | 2025-09-05 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 2fd98593-8563-3a1d-8795-60e5d97114b4 | -8.4297 | -47.5397 | 2025-09-05 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b1ac84cb-dab5-33df-9536-ee8dd192def2 | -15.2873 | -52.7022 | 2025-09-05 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 83d1d173-8560-30cf-9d17-c8b5f50a692b | -11.864 | -50.7075 | 2025-09-05 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 8bb4a069-2b7c-34b6-ba86-a6af517f5a59 | -11.8343 | -51.4339 | 2025-09-05 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 066ad15e-d698-3ca1-aa45-5c8bf0ac8696 | -22.297 | -47.6343 | 2025-09-05 14:30:00 | GOES-19 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 127.4 |
| f9605770-29b0-313a-960f-7d070771c764 | -14.5597 | -48.0879 | 2025-09-05 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 1dbef2c3-22c0-3cd0-8644-7a11d281ab73 | -10.9852 | -49.7778 | 2025-09-05 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ceeddfe5-906f-3839-8d5b-c721784e6733 | -8.7068 | -62.3995 | 2025-09-05 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a5a134af-2ba8-3740-88c7-af6382fc2576 | -6.2609 | -43.2727 | 2025-09-05 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 14250919-3c48-330f-96ee-c2ce392c9f00 | -7.7128 | -61.5276 | 2025-09-05 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| aeabf0b5-9d80-380f-818c-1951f223013d | -15.3435 | -53.9382 | 2025-09-05 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 177.9 |
| f3b1dcbb-0e84-3e3a-b8fc-d4e842f7a4f9 | -5.9844 | -44.7489 | 2025-09-05 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 1f7c5b6a-a0a6-3651-9eac-cb08b6aeb7e5 | -8.885 | -47.2304 | 2025-09-05 14:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 65ff05d3-e555-38ed-b0b4-6ea3a3b42e8b | -14.7465 | -47.4955 | 2025-09-05 14:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 154.6 |
| f999836f-694b-35a8-ba12-5ece0ef7874f | -10.2373 | -50.5417 | 2025-09-05 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| c3f0136f-d163-338e-b265-6117e46adc16 | -6.2606 | -43.2961 | 2025-09-05 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5b360e32-ab73-32e3-aa3a-8035fd3b53bd | -11.8153 | -51.436 | 2025-09-05 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 624a456f-84bc-339a-a08e-edd80dcce68a | -7.8923 | -45.2893 | 2025-09-05 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 05128085-f709-3f4c-a1d3-b661ad1b760f | -6.0045 | -46.6797 | 2025-09-05 14:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2e28261c-d8c6-30c4-9435-a5141064e025 | -15.2156 | -52.372 | 2025-09-05 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| da1721cd-1847-3028-906f-02ba5c182da3 | -5.7736 | -45.3091 | 2025-09-05 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| db7ac495-89ac-3a3a-8ad5-f81472ba4ef6 | -15.0445 | -50.0899 | 2025-09-05 14:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c0032877-60bf-36b8-a76b-163f21bcf393 | -6.1491 | -43.1885 | 2025-09-05 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 14bee061-1154-3fed-bfc1-fa49a7854622 | -14.1254 | -51.7088 | 2025-09-05 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b1bcc5a0-bbc2-3eac-a041-84d337a9e8b8 | -9.0762 | -47.0113 | 2025-09-05 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 9af009ea-4b98-38ae-b0df-e68b89389a6f | -15.2877 | -52.6809 | 2025-09-05 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 86cf9781-02d8-3fc5-9ead-332546ba76fd | -12.7251 | -45.0828 | 2025-09-05 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d1af078b-d410-3173-988f-e568b981d359 | -5.8986 | -45.9748 | 2025-09-05 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b5e3de54-067f-3587-ac74-8d8609a4aded | -9.7105 | -48.9853 | 2025-09-05 14:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 2d03d511-c3be-348c-9784-14294f42f4f9 | -15.0639 | -50.087 | 2025-09-05 14:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 8f27e3fc-f3a8-331e-be19-a6328a7146d2 | -7.8011 | -52.1331 | 2025-09-05 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| bb8f1ef3-5342-38b5-9dc1-0423cb1ba8c3 | -8.3364 | -47.4824 | 2025-09-05 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| afbe73c8-8bec-3f47-a1f3-68d9d17dea88 | -12.1313 | -50.655 | 2025-09-05 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 8c893716-2caf-3ed8-a002-f7e143c0c657 | -11.338 | -50.2968 | 2025-09-05 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| f83cbb01-dac8-3505-b48b-8b0c7ed71604 | -8.1814 | -49.6003 | 2025-09-05 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f6005f82-b9a4-32d5-8ca1-5967c5a979fe | -7.6186 | -47.9406 | 2025-09-05 14:30:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| dea38ed7-caca-32f1-b3da-1ec06f6c583f | -7.0314 | -43.2742 | 2025-09-05 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| d6ecae7f-3774-3327-8d34-61726e90de11 | -8.479 | -45.0704 | 2025-09-05 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| f899b0fa-5eec-3e68-b14f-80fdbc51e973 | -14.0496 | -54.0122 | 2025-09-05 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| e894bb39-8f2f-3299-b89d-92835ce9b5ab | -14.1447 | -51.7062 | 2025-09-05 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| cd2d9c5b-d22c-3c38-9cc8-77eef5b861cf | -6.023 | -46.7005 | 2025-09-05 14:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| ed31ab9c-fd32-37f0-a1db-e2c190b182b9 | -14.1443 | -51.7276 | 2025-09-05 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 010d899d-6bcc-3276-89c1-e64f7ea31d45 | -8.9034 | -45.7973 | 2025-09-05 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.7 |
| bc3ad1fc-8d72-30d4-9001-168cac7307be | -5.7923 | -45.3078 | 2025-09-05 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 0ff3bb84-1ec0-3ece-a353-92e31a45b863 | -6.9568 | -44.9434 | 2025-09-05 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 7af3b5f4-fdb8-36fd-b8ff-523112c5f2c5 | -11.5961 | -52.176 | 2025-09-05 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 77e902e8-8329-3928-bd74-63823a475b04 | -8.9037 | -45.7747 | 2025-09-05 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 1f2607e1-ebb4-3cb3-ba25-9d03af3f3ee9 | -11.0871 | -51.9977 | 2025-09-05 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7c195d3a-c566-359b-9957-2ddc544c6bdc | -8.6883 | -62.4002 | 2025-09-05 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e48e69e9-e695-3635-ae32-c47e042043fa | -13.8845 | -47.9705 | 2025-09-05 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 584d052d-9f7e-3715-8283-79958e8fdb0a | -6.0232 | -46.6784 | 2025-09-05 14:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 21ef09fb-05a7-3b29-92ff-187f687b60d5 | -6.2418 | -43.2976 | 2025-09-05 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 10121ada-3bd2-3301-ab3f-2979c9b9de76 | -15.235 | -52.3693 | 2025-09-05 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 24d40250-4b3d-3324-884b-a0a63045bcfd | -10.3147 | -46.3571 | 2025-09-05 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f2bf47e0-e1f8-325f-bcdf-b10800c8e788 | -8.3458 | -48.2916 | 2025-09-05 14:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |


[Clique aqui para ver as próximas entradas](README70.md)
