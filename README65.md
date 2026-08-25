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
| 94eacca5-1d36-3586-b0d1-d96b7710b378 | -6.8163 | -59.45658 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 830fa7c8-fff1-390b-9460-4b09a176a543 | -6.72241 | -59.44569 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b366c968-ebfe-3752-a845-5f7a59d2cfc4 | -6.80752 | -58.66535 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ada653a3-f99b-3bec-b97a-c19ee0438bf0 | -7.20684 | -60.6144 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 68ceab74-429d-3e06-81cd-f71b39ccd132 | -6.77169 | -59.59864 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07c64f39-9604-3317-87d4-043d056fc660 | -6.83033 | -52.50128 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d2013c7-c90c-3506-92c2-5ccbff58b8b6 | -6.17324 | -53.47623 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48de15d4-5b00-3788-be95-f5606791e1bb | -6.18339 | -53.53104 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27c330bd-54f3-35e7-8ea7-f7866eef1b2d | -7.2973 | -60.67883 | 2026-08-25 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50078f55-93a3-3bef-ba56-2370a4ad5624 | -10.7988 | -50.9305 | 2026-08-25 05:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 691605d5-2cb7-3470-b213-f04599d8ce7f | -7.0058 | -59.2382 | 2026-08-25 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3138d441-3eb4-3929-a51c-e35f7d24b08b | -11.1447 | -44.4632 | 2026-08-25 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| ea90f971-a484-35dc-8c79-e0f04e4ca4a8 | -6.641 | -58.4987 | 2026-08-25 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a5c8d462-fe2c-3dcf-bd9b-a500b6f6db65 | -7.0057 | -59.2575 | 2026-08-25 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 5f6b367a-2c78-3bf1-9118-04e388e2d9b7 | -10.7801 | -50.9113 | 2026-08-25 05:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| b6d4c8e6-1ae5-389a-be80-5bb64f1513d6 | -3.5407 | -48.1673 | 2026-08-25 05:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2b773e13-c12f-3619-9f0e-d3c2bd24dc56 | -10.4269 | -61.229 | 2026-08-25 05:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 20d36f9e-8cf5-3976-81f8-8f1fd571fb4b | -11.9991 | -45.9287 | 2026-08-25 05:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| a8e2057b-a830-3972-b15a-949e041ff659 | -6.9873 | -59.2389 | 2026-08-25 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 46d5c63a-d906-3ca6-bb73-795b36dfcdc0 | -11.1443 | -44.4865 | 2026-08-25 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 4cdb16c9-9708-38fc-b66e-4f222a90c740 | -7.2901 | -45.3683 | 2026-08-25 05:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| beb293dd-6df6-3dab-93bc-333786456e98 | -6.9872 | -59.2582 | 2026-08-25 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 96180a35-42de-3eaf-b083-adcfdee4835a | -3.5406 | -48.1889 | 2026-08-25 05:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| c2654da1-fa23-3a66-bc9d-8f3d67157998 | -10.7799 | -50.9325 | 2026-08-25 05:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 881b5ea4-9296-30da-aa5b-deca872c95a7 | -13.872 | -55.26206 | 2026-08-25 05:50:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23a62ab5-40ff-3ae5-99e9-f19b329cc59c | -13.8756 | -55.26664 | 2026-08-25 05:50:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bb38e78-6f8d-34d2-aa3e-1a6d899f2910 | -13.20657 | -51.48211 | 2026-08-25 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2a9cc4cd-b964-3a1e-9292-29f3ecb7225d | -14.37904 | -51.96531 | 2026-08-25 05:50:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f674c8c7-32fd-3a98-a940-f58f5cf55d89 | -14.38494 | -51.76259 | 2026-08-25 05:50:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff206919-62ee-38a8-9f5e-d83ec0518be7 | -16.50152 | -54.66843 | 2026-08-25 05:50:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e2c2472-5a03-3a50-956e-5b538670247b | -13.19411 | -51.39403 | 2026-08-25 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 60d3c24a-077d-30a2-adb3-7a911ff2cdfb | -16.50105 | -54.67305 | 2026-08-25 05:50:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0594cc97-b24b-322b-9902-ceef1b14aae0 | -14.91568 | -52.64424 | 2026-08-25 05:50:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4e81667d-83ef-328f-af7e-11a25c0a11fa | -14.91633 | -52.63805 | 2026-08-25 05:50:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a83111ab-d9e0-325e-b81e-b111d99b2be4 | -15.24255 | -52.79779 | 2026-08-25 05:50:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bd59bb3-7837-36c5-9d0f-3ed133e4ebe9 | -14.91661 | -52.64317 | 2026-08-25 05:50:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc87bd96-7e9c-3fc8-a214-130cbcff9a88 | -13.19793 | -51.49544 | 2026-08-25 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba59f5db-f697-3892-9760-66eee8748e1f | -13.87813 | -54.03099 | 2026-08-25 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2f12ad3-7e1b-342f-b44d-1dbd4c4b632a | -14.9089 | -52.64324 | 2026-08-25 05:50:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 624d029c-c260-3257-9131-d1206fd95197 | -13.19486 | -51.38684 | 2026-08-25 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3878e667-9fc5-3fff-b670-dfd7770c8fec | -13.21447 | -51.47581 | 2026-08-25 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6464d9cf-7447-3e57-94e7-fe774d62e6eb | -13.20128 | -51.39484 | 2026-08-25 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7804bf76-daa9-3e33-bc1d-6b58a42b497b | -14.91723 | -52.63697 | 2026-08-25 05:50:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 728591ba-7286-3542-9d7a-c0dc42567cda | -14.38539 | -51.97287 | 2026-08-25 05:50:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2b1f0a0-d77d-311a-a4ad-85186f558133 | -13.86872 | -54.00311 | 2026-08-25 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45d61dd8-92e6-3770-a5ea-ed55ee574f9f | -14.39205 | -51.7634 | 2026-08-25 05:50:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30999894-c585-347f-863c-e144ed54ef7c | -13.20732 | -51.475 | 2026-08-25 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7d1a2c6-15bf-367c-9052-3d7ef41ac370 | -13.87195 | -54.03025 | 2026-08-25 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d16f9de-0cc2-3c5c-a1de-45ed0920e131 | -14.53257 | -53.20873 | 2026-08-25 05:50:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29522701-917e-3758-b393-a3fe2229fed6 | -14.53198 | -53.21446 | 2026-08-25 05:50:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d4f2263-cf77-3080-8d82-57911ffa109c | -13.20582 | -51.48917 | 2026-08-25 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23b14815-8153-35ed-b432-f637d6dd7685 | -13.8761 | -55.26253 | 2026-08-25 05:50:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c8d1ae6-c63a-3552-ba0f-146b6c33fc19 | -13.21371 | -51.48289 | 2026-08-25 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dec7d86-a2fd-3eb1-abd2-fd3c00bd9cb3 | -14.90984 | -52.64206 | 2026-08-25 05:50:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68d52134-d771-30c7-bd4b-46fd3d871a43 | -15.24311 | -52.79224 | 2026-08-25 05:50:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db920e31-d94c-3fff-b906-79666ff6160c | -14.38608 | -51.96608 | 2026-08-25 05:50:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fb6b654-03d6-3f21-b390-910551d60c43 | -13.86195 | -54.0074 | 2026-08-25 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8526f6b7-9d37-39be-b64d-6e6131b83d15 | -13.86253 | -54.00222 | 2026-08-25 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fa049a1-cd8e-3d76-a9a5-2777c3ee023c | -13.87772 | -55.26275 | 2026-08-25 05:50:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c690de8c-eb73-3162-81e6-ed917d0a837a | -20.71517 | -57.82746 | 2026-08-25 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e7318438-80e6-3152-8ab9-8bde7de5c20d | -20.70954 | -57.83024 | 2026-08-25 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0be811e6-e024-3458-9263-4c8fdc7ac3b4 | -10.7801 | -50.9113 | 2026-08-25 06:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| a201aabd-93ee-3e25-bb05-0b48f0af5f22 | -6.9873 | -59.2389 | 2026-08-25 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| cc057f8b-c6bf-3fda-a038-7c9c6609eafc | -3.5221 | -48.1896 | 2026-08-25 06:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ec0073b2-7b76-30e2-881d-932da7ba1c7e | -3.5406 | -48.1889 | 2026-08-25 06:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| d37153ea-2b2c-39e2-b7a5-12e6e0e8327c | -10.7799 | -50.9325 | 2026-08-25 06:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 6a2f261a-82a2-30aa-b3d5-31367f44cb9a | -11.1443 | -44.4865 | 2026-08-25 06:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 1e0be7f6-35c9-36fa-9d1e-6e022ed13852 | -11.9991 | -45.9287 | 2026-08-25 06:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 95350950-12f3-32d8-b293-57c48ec5b523 | -7.0058 | -59.2382 | 2026-08-25 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| bfaf552a-e443-3f4d-bcfe-5f1159354ccc | -7.2901 | -45.3683 | 2026-08-25 06:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c8d67913-8e52-37f8-8124-add04da2c378 | -6.641 | -58.4987 | 2026-08-25 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 8b375e56-9253-3cf8-8e9e-1e91ba6d705b | -10.7988 | -50.9305 | 2026-08-25 06:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 03d02ddd-9681-3352-8d94-6fb5f1aab4e2 | -6.9872 | -59.2582 | 2026-08-25 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| cb607d24-0d70-3b59-a1f1-68941bd0b4fb | -8.5775 | -54.8575 | 2026-08-25 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d08db12c-cc30-333b-abe2-2d6e3591684b | -7.0057 | -59.2575 | 2026-08-25 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| a42692ad-1f31-3f8a-9068-4fb6001cb822 | -3.5407 | -48.1673 | 2026-08-25 06:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c3a8c5fe-4f65-3994-a905-0dae27dba728 | 2.59375 | -60.69792 | 2026-08-25 06:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d12d5bed-4c93-35f8-b2e1-9544703e0514 | 2.5929 | -60.69271 | 2026-08-25 06:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f622b391-9b8a-3756-9fbf-cde6e2102669 | -6.80993 | -59.60194 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98e5d4bc-7be3-3cdf-89a6-49fd16b3074a | -5.94283 | -57.73821 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b076942-8036-3265-958e-32a17d1230ed | -6.78687 | -59.63841 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df94962b-a716-3d4d-9b78-3eef01b2c0b4 | -6.79841 | -59.81814 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 641e6517-a710-3507-a141-b0ada6ed545b | -3.10382 | -61.22956 | 2026-08-25 06:05:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a697063e-c638-3d23-bf5d-679434a5d801 | -6.60812 | -58.38629 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2491ad72-db0b-31a3-822c-92215825d142 | -6.61022 | -58.38272 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b173a6c4-169d-3d3a-b1e9-ff2e125698dd | -6.81157 | -58.65825 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9194e68-8500-3504-a064-e355e13e0944 | -6.79332 | -59.59047 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb3e1a56-5ce3-3ba9-aae3-459040a28d89 | -3.3904 | -59.56525 | 2026-08-25 06:05:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b0370ce-59e1-3736-a24e-2abb13ed14c8 | -6.86673 | -59.40891 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 210e5eeb-6ef5-34bc-9e93-4ffb981570b8 | -3.13042 | -61.18429 | 2026-08-25 06:05:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d843924a-c014-34bb-bca8-e28d18a90c8f | -6.01145 | -57.66754 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbbb75f0-5ce2-3e97-8594-e46b4fca45a5 | -6.69253 | -58.72599 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f23cd1c-190f-37d2-92c0-bb9973ca8812 | -6.79164 | -59.64779 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 857a0a88-9ea5-3568-ba82-ccc01628aad5 | -6.80518 | -59.59233 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ba4adaa-28fa-37d5-b9b0-49a133a2a507 | -6.6403 | -58.49809 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1126781a-c9a4-39ba-8208-db89c5ba6bc7 | -6.12776 | -57.83525 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97621fb6-efae-3aab-a263-f8fd93306af1 | -6.62694 | -58.48412 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 57e97bc3-bb18-3ff8-99f7-cc30992e14bd | -6.69687 | -58.72474 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 959a15ea-9257-3750-840c-ead82a2fd56a | -6.85408 | -59.41181 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6aee2752-a2ac-343c-9f6f-64162e865a78 | -3.12998 | -61.18724 | 2026-08-25 06:05:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README66.md)
