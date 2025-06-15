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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a198ebb-7c47-3acb-a478-3a35e825e6f3 | -11.5779 | -44.8413 | 2025-06-15 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 8c368349-5114-31e6-bc84-6da7275aae5d | -13.9059 | -54.6291 | 2025-06-15 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 1c1865b1-b113-3d53-873e-a280bb476b51 | -11.5779 | -44.8413 | 2025-06-15 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| bbed60db-2aaa-3ca5-8c5f-cd76e7886e65 | -13.9062 | -54.6084 | 2025-06-15 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e79457bc-5fca-3f44-8384-f23fd3482da0 | -11.5779 | -44.8413 | 2025-06-15 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 74bb7342-5d52-3400-9082-23b04ff139e0 | -7.2283 | -44.1622 | 2025-06-15 12:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 119.6 |
| a80f776f-f6fc-3e3d-9c1d-b45f231969ef | -11.5779 | -44.8413 | 2025-06-15 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d20313f8-d5ac-3d9f-8e09-b9e9b469ac11 | -11.0113 | -55.0764 | 2025-06-15 12:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 150.6 |
| c1036c99-d9d4-3a18-938b-91a976b230f6 | -11.5779 | -44.8413 | 2025-06-15 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 042db6a4-9007-3cf2-ac3b-31a4c8947517 | -13.9059 | -54.6291 | 2025-06-15 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 95f619be-3d00-36a7-be2f-cab9168791bc | -13.9062 | -54.6084 | 2025-06-15 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 136.8 |
| c939061b-b373-388b-8de9-639c1c7e6595 | -13.9251 | -54.627 | 2025-06-15 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 212.2 |
| e34f4579-b568-3e55-bd71-06f4a02695c2 | -11.0113 | -55.0764 | 2025-06-15 13:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 232.7 |
| 8623f1b5-6005-3704-8436-81cac268bf97 | -13.9254 | -54.6063 | 2025-06-15 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 08ba69ac-6dcc-3fc8-aef2-0c59bbed5205 | -10.9924 | -55.078 | 2025-06-15 13:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 02f9ed26-7436-32f1-9c89-02c0757a43c8 | -8.78738 | -46.58167 | 2025-06-15 13:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| ea3d9e7c-b486-345c-9450-fb7fa21feef9 | -8.78322 | -46.62971 | 2025-06-15 13:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7dc02a0b-a627-3a0b-96e3-22b4a7cb1a3a | -7.38291 | -53.95524 | 2025-06-15 13:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea0668f5-71f2-3064-8627-10c9c1464e0a | -8.78252 | -46.62284 | 2025-06-15 13:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 09acca69-2db4-348a-93d4-044a312fc089 | -7.63836 | -48.31771 | 2025-06-15 13:04:00 | TERRA_M-T | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| b2ae8a12-e2ff-3a66-98e7-19ab8ef91213 | -8.7878 | -46.58858 | 2025-06-15 13:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| e6336c4e-f256-3ad5-979a-b0cf5fe1ac33 | -13.9251 | -54.627 | 2025-06-15 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 250.6 |
| c6eea860-bba6-3490-9a11-f5f689ace30a | -11.0115 | -55.0561 | 2025-06-15 13:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| b54d00d0-db6a-3998-88b0-a7335aac071a | -11.0113 | -55.0764 | 2025-06-15 13:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 316.1 |
| b553d9f6-0bbd-3c6f-b71c-144464a08b58 | -13.9059 | -54.6291 | 2025-06-15 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 5b8a1f4e-0eae-3ca5-b081-d0b6f20fe61b | -10.9924 | -55.078 | 2025-06-15 13:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| c4f219c8-b09a-3b64-b4c4-3df8afd1dec5 | -13.9254 | -54.6063 | 2025-06-15 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 5e0abcd1-3b0b-3d75-8bf8-9530bc9006db | -11.5779 | -44.8413 | 2025-06-15 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 006a89e5-e598-330b-a99f-165608b9acd7 | -13.9059 | -54.6291 | 2025-06-15 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 275.1 |
| 0fc0c0ff-8314-3ee7-a303-2c67e3bf4bdb | -12.2228 | -44.1838 | 2025-06-15 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 656744ae-fdeb-3edc-bf6d-e7497a19deaa | -11.0113 | -55.0764 | 2025-06-15 13:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 428.3 |
| 525b2243-adbc-3e39-bea6-8bf5922058a7 | -10.9924 | -55.078 | 2025-06-15 13:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 143.5 |
| e4873e50-b29d-371a-9b5b-bedd4ba98a4c | -13.9062 | -54.6084 | 2025-06-15 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 1d8b7e2d-0cd0-3f60-90ec-d2d08142e66b | -11.0115 | -55.0561 | 2025-06-15 13:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 155.3 |
| db3ff2cf-f4f6-3d1a-bc26-7ea887bcfc0e | -13.9251 | -54.627 | 2025-06-15 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 246.7 |
| 7773b19b-f195-3c20-b3eb-2961c9af6567 | -13.9254 | -54.6063 | 2025-06-15 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 61e07bda-fc7c-3dce-8176-76198914a9d2 | -13.9062 | -54.6084 | 2025-06-15 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 194.9 |
| c47e39fd-9394-3a35-9485-fced973257f1 | -10.9924 | -55.078 | 2025-06-15 13:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 90acfc08-ef62-3c65-8584-1a0b964760c0 | -13.9251 | -54.627 | 2025-06-15 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 247.3 |
| 3869fa30-19df-3600-bc20-d06d6bd52594 | -12.2228 | -44.1838 | 2025-06-15 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| ff883dc1-d7ff-3ee3-84df-7d456c5bec21 | -10.9926 | -55.0577 | 2025-06-15 13:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 95210262-b442-3472-8f2a-de2ea343714b | -11.011 | -55.0967 | 2025-06-15 13:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 4e9bf85f-3915-3a05-87f8-269337823f3c | -11.0113 | -55.0764 | 2025-06-15 13:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 483.0 |
| 7f676b5e-b6fe-35c9-931d-f3bb91629e64 | -13.9059 | -54.6291 | 2025-06-15 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 270.5 |
| 96486830-dade-34a2-8b65-716ef76f3786 | -13.9254 | -54.6063 | 2025-06-15 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 1129cb95-ff80-38a8-a038-39a45c3e9bd9 | -11.0115 | -55.0561 | 2025-06-15 13:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 241.3 |
| 9c4fc8eb-c92e-3a2e-a855-13a33eb28358 | -11.0113 | -55.0764 | 2025-06-15 13:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 580.6 |
| f50906d5-9cb5-3352-a261-49700f24bb47 | -11.0115 | -55.0561 | 2025-06-15 13:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 224.8 |
| 87c833aa-f7bf-36c9-b195-9c48b6246335 | -12.2421 | -44.1807 | 2025-06-15 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| ac643230-f18b-3251-862a-48cf37a4dc22 | -13.9248 | -54.6477 | 2025-06-15 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1f286c5c-262b-3052-a688-b3d7ca612348 | -13.9251 | -54.627 | 2025-06-15 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 308.3 |
| 4b08b21e-7141-32bd-8b2a-b9ac6354ad20 | -13.9062 | -54.6084 | 2025-06-15 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 168.6 |
| d97dfade-6715-3456-9a52-2aa13f6d5e9f | -10.9926 | -55.0577 | 2025-06-15 13:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 02a4a044-106c-3a7e-ba4c-7d0851d36999 | -13.9059 | -54.6291 | 2025-06-15 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 246.0 |
| be0fafe5-6072-353c-b272-6a5304f1be99 | -13.9254 | -54.6063 | 2025-06-15 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 162.6 |
| efa82f75-2765-3756-aaf5-bc5b89919afb | -10.9924 | -55.078 | 2025-06-15 13:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 91e0fbd2-645f-3012-b5be-f73ec244739f | -12.2228 | -44.1838 | 2025-06-15 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 38a02546-dfb9-314f-a5ac-0bb4fa426277 | -7.2283 | -44.1622 | 2025-06-15 13:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 94b3ad93-72f4-3ea1-8f1d-55e5dc5f5afa | -7.2471 | -44.1604 | 2025-06-15 13:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 743eddcf-7ca4-3065-bf8b-14518fa6910a | -11.0113 | -55.0764 | 2025-06-15 13:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 538.1 |
| a2613aea-2b8f-3559-8800-361b4e372b5d | -10.2383 | -46.3889 | 2025-06-15 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 1676b8fc-a282-365b-8865-2c4169f83a6d | -13.9248 | -54.6477 | 2025-06-15 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| acc01402-447f-3073-9956-f2f6785bb881 | -13.9062 | -54.6084 | 2025-06-15 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 190.4 |
| f81a7728-06ae-34ed-bbc0-b946cf6480e0 | -13.9251 | -54.627 | 2025-06-15 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 324.6 |
| 6fa68c9e-c809-3cbb-8be3-40267924085f | -13.9059 | -54.6291 | 2025-06-15 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 233.4 |
| 1ec1307e-de3a-32d7-8a54-6ce39c924b20 | -9.4161 | -48.4286 | 2025-06-15 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 747e3f2d-e576-35b0-8af4-b0bd9b9c1add | -12.2421 | -44.1807 | 2025-06-15 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 781baeef-1eed-362f-8497-ebebb494e463 | -10.9924 | -55.078 | 2025-06-15 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 168.0 |
| bfd9f927-4097-3ef6-9eb4-e09f45b5331a | -11.0115 | -55.0561 | 2025-06-15 13:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 335.0 |
| 1aff8af8-8757-3c5d-99da-c25e2bc6d3de | -10.9926 | -55.0577 | 2025-06-15 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 5afa36d1-0abd-35d1-8c66-9cd95b98e838 | -10.0458 | -46.5915 | 2025-06-15 13:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| deef50fa-9a25-3882-aed9-0bb3c66083ec | -13.9254 | -54.6063 | 2025-06-15 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 191.7 |
| b9126325-c0a8-34a0-84af-3c0583d935e5 | -11.011 | -55.0967 | 2025-06-15 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 6bf91343-f032-3b99-896c-af01e6db310d | -11.0113 | -55.0764 | 2025-06-15 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 445.6 |
| 58c0efc2-96ec-346b-ba51-6cb7e635a8f5 | -9.4161 | -48.4286 | 2025-06-15 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 338a5fcc-f0b6-3ce1-9762-731c6877493c | -12.2228 | -44.1838 | 2025-06-15 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e696271b-56bb-35fc-9d87-4c547c011e9f | -10.9926 | -55.0577 | 2025-06-15 14:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 220b12a7-3cdb-38ed-bd92-1347d5215579 | -10.9924 | -55.078 | 2025-06-15 14:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 234.6 |
| 7d2f42e3-5fa7-3035-a98b-976f703630d5 | -13.9248 | -54.6477 | 2025-06-15 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 6396ddf2-9eac-3b12-bd7d-55124e9ad1f6 | -13.9254 | -54.6063 | 2025-06-15 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 254.6 |
| 68ff5d24-ab7b-3997-b394-e9d6fa3f9210 | -13.9062 | -54.6084 | 2025-06-15 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 157.6 |
| ce21dba4-412d-32e2-a505-5be897eccd8f | -13.9059 | -54.6291 | 2025-06-15 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 193.5 |
| fb9e2793-a4d3-309b-8bc2-587b1920079e | -11.0115 | -55.0561 | 2025-06-15 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 298.0 |
| e1929b51-9ead-3dac-a478-59a8118e9272 | -13.9251 | -54.627 | 2025-06-15 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 383.1 |
| 927208e2-cb89-3bbd-beac-6e469f443731 | -13.9251 | -54.627 | 2025-06-15 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 311.7 |
| ffd26c99-ab9c-3731-8cd9-6c09f9ea78df | -13.9254 | -54.6063 | 2025-06-15 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 822156a6-8d75-357e-b595-fab29ddc06d1 | -10.2383 | -46.3889 | 2025-06-15 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 7adf2c30-f8d1-34da-b380-ed75740639a1 | -13.9062 | -54.6084 | 2025-06-15 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 219.5 |
| 884a4076-acfa-3894-8a3b-847d63b82dab | -7.2158 | -43.6069 | 2025-06-15 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 48c3ddb9-c593-32ea-9328-a5be7c6abb5e | -11.0113 | -55.0764 | 2025-06-15 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 552.3 |
| 0a46b9fc-daef-3861-93b1-1c12a11c9961 | -13.9248 | -54.6477 | 2025-06-15 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| aa9cac0b-176d-314c-9b09-c71f58c8608b | -9.4161 | -48.4286 | 2025-06-15 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b0591620-5304-3aad-ac93-d7663e51ed14 | -10.9926 | -55.0577 | 2025-06-15 14:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 76f24ded-5a2e-376d-a04a-efd07ac8228e | -13.9059 | -54.6291 | 2025-06-15 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 350.2 |
| 5ce642e2-2a68-3364-ac63-de9d3bd45797 | -11.0115 | -55.0561 | 2025-06-15 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 259.1 |
| 7770779e-81cb-3b31-a848-757d9521c4b7 | -13.9056 | -54.6498 | 2025-06-15 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 3e68f873-de30-3349-ac9f-af863c86cc0a | -10.9924 | -55.078 | 2025-06-15 14:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 170.4 |
| 51c716af-c9b2-3d5c-9ebd-c34ef9a520a0 | -9.4161 | -48.4286 | 2025-06-15 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 15d324a1-7df2-368d-8f23-b86fd0da742e | -13.9059 | -54.6291 | 2025-06-15 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 347.7 |
| 1846a880-1de0-382c-8b5f-7c1dbeb25561 | -13.9248 | -54.6477 | 2025-06-15 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |


[Clique aqui para ver as próximas entradas](README18.md)
