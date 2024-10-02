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

## Dados Diários - Página 202

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c88c7dc-29be-39a3-ac1f-792f3915e89f | -13.2173 | -48.624 | 2024-10-02 10:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 57f894f6-895c-3f94-b16f-2f857c8b5355 | -12.8803 | -62.531 | 2024-10-02 10:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 368c7b43-c4f6-3105-b4ea-c29b3d5a24dc | -13.198 | -48.6267 | 2024-10-02 10:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 113.7 |
| ef7647a4-8252-3053-b2de-0451c8c52e53 | -13.2169 | -48.6461 | 2024-10-02 10:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ac33bcd7-adb2-34bb-b337-13eb46df5b09 | -13.5376 | -51.2085 | 2024-10-02 10:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| a4a99bbf-c706-36cb-891c-015aa3f94ee6 | -16.7265 | -57.4287 | 2024-10-02 10:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 46b787de-1027-3fa7-a762-86f071693fc7 | -16.5976 | -58.2162 | 2024-10-02 10:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 240.7 |
| ac99093a-8002-30a7-b922-750d041a0772 | -16.5973 | -58.2365 | 2024-10-02 10:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 322.1 |
| 5ae854f7-9793-3d38-9840-8517bd8af4e5 | -16.5778 | -58.2386 | 2024-10-02 10:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 5a455032-a8ab-3957-8fd3-5a12234c095f | -16.8983 | -57.6949 | 2024-10-02 10:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.6 |
| 9f44ad4c-9181-3a5c-8dc1-7af9579d2ba3 | -16.898 | -57.7153 | 2024-10-02 10:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 64448c70-3e55-34b8-8dac-97bcb0751446 | -22.5502 | -48.1834 | 2024-10-02 10:27:10 | GOES-16 | SANTA MARIA DA SERRA | SÃO PAULO | Brasil | 3547007 | 35 | 33 | nan | nan | nan | Cerrado | 155.6 |
| d19e2de7-ba8a-3e23-9427-af3960e83079 | -22.5293 | -48.1887 | 2024-10-02 10:27:10 | GOES-16 | SANTA MARIA DA SERRA | SÃO PAULO | Brasil | 3547007 | 35 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 08a39344-0815-31ef-9da8-5242205a4544 | -12.8803 | -62.531 | 2024-10-02 10:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 7772afcb-fc07-367c-9c30-b3d90cef2788 | -13.2173 | -48.624 | 2024-10-02 10:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 142.9 |
| b98a5199-f426-3a86-8a85-db24ac2bd0b4 | -13.5376 | -51.2085 | 2024-10-02 10:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 697808bf-eb46-35d9-b554-4a36646bc1e0 | -16.5976 | -58.2162 | 2024-10-02 10:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 207.5 |
| cdfdeb24-9c24-32b3-aad3-114db466ccb5 | -16.5778 | -58.2386 | 2024-10-02 10:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| feb5dadd-f32b-3f50-b1ad-36486a15aa9a | -16.5973 | -58.2365 | 2024-10-02 10:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 329.5 |
| 9cc1f896-0e3e-38bc-a0a8-0c62336cfb16 | -16.898 | -57.7153 | 2024-10-02 10:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 1bc907b5-1862-3a1d-9726-f9387ef988b1 | -16.8983 | -57.6949 | 2024-10-02 10:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.4 |
| e499b391-11ec-3bc2-a1ec-c94f81886c69 | -20.4309 | -46.0639 | 2024-10-02 10:36:59 | GOES-16 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 0b210b07-4003-36dd-a499-7130c2d8d37b | -10.5929 | -48.0597 | 2024-10-02 10:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 943b352a-4035-3c59-aacb-484c90853a18 | -12.1597 | -50.0501 | 2024-10-02 10:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ecfe8323-6727-3103-a54a-23bc71cda8ef | -13.094 | -51.3712 | 2024-10-02 10:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 183.4 |
| a5ddf7aa-ff84-3e45-877a-ecb50fd43be6 | -12.8805 | -62.5117 | 2024-10-02 10:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 145e4be4-80dd-396f-a429-aac2646d9a06 | -13.0563 | -51.3333 | 2024-10-02 10:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 278.9 |
| a0b5db2b-073f-3eef-b62d-954554c3ac86 | -13.056 | -51.3546 | 2024-10-02 10:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 3e6e1646-1352-3c56-88f6-5cc111734f92 | -13.0375 | -51.3143 | 2024-10-02 10:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 120c3f34-708a-3259-bfc6-0d00c8a590ab | -13.1125 | -51.4115 | 2024-10-02 10:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 0706ee2b-b6e3-3a9a-839a-7ebee6b02a55 | -13.0937 | -51.3926 | 2024-10-02 10:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 88d66ae0-3403-3796-bfe3-4f6b2328182b | -12.8803 | -62.531 | 2024-10-02 10:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 93.6 |
| cb9c61eb-d911-3d2b-8bfc-53604dd99dc3 | -13.2173 | -48.624 | 2024-10-02 10:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 226.8 |
| b0727062-b887-3432-ac15-16912a3c5cac | -13.2169 | -48.6461 | 2024-10-02 10:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| e7601829-4884-325c-b432-50748a1788c0 | -13.198 | -48.6267 | 2024-10-02 10:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2d3b9a83-38ab-335c-bfd7-9d720b1a57be | -13.0567 | -51.3119 | 2024-10-02 10:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3a966e0f-eede-3e3e-88ea-c390ad67db84 | -13.0372 | -51.3356 | 2024-10-02 10:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 224.0 |
| 1cc768bd-1e85-3322-8875-f45bfd4d9973 | -13.5376 | -51.2085 | 2024-10-02 10:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| aeff9c0b-b1da-30a4-b62e-cab6c28cf1a2 | -13.5184 | -51.211 | 2024-10-02 10:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c66c3f6c-ac36-3b34-9638-22f01214ae23 | -15.9003 | -50.1537 | 2024-10-02 10:46:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| d785b61f-e437-3982-9315-71ef86761834 | -16.5973 | -58.2365 | 2024-10-02 10:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 349.2 |
| 40f2ac1d-82c3-3be3-b383-42b8ed8bbbf0 | -16.5778 | -58.2386 | 2024-10-02 10:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 3b2f44da-e991-3f96-a099-d19c6a8c28ab | -16.5976 | -58.2162 | 2024-10-02 10:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 215.4 |
| 7a67f939-845d-371a-b5fd-680830e97447 | -16.8983 | -57.6949 | 2024-10-02 10:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.6 |
| 6e053c7e-6c18-3758-978b-c5b0671915fb | -16.898 | -57.7153 | 2024-10-02 10:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| e02f542e-2cf9-327c-9970-24d3f2657710 | -20.4309 | -46.0639 | 2024-10-02 10:46:59 | GOES-16 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 3b8371ea-d0cd-3524-bfa2-a682a6d501bf | -20.4316 | -46.0399 | 2024-10-02 10:46:59 | GOES-16 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 200b85d6-51c6-3ce4-b981-9589cdf7e9d5 | -10.5929 | -48.0597 | 2024-10-02 10:56:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 58f82e11-1ef6-3d23-ab06-b45170038045 | -10.5933 | -48.0377 | 2024-10-02 10:56:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 15aa06ae-97ab-3ff1-acf6-10158eda0ecb | -10.7165 | -46.1716 | 2024-10-02 10:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| b8c9c329-1a77-394c-9b08-5169ce07baa5 | -11.2952 | -46.8849 | 2024-10-02 10:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| bb375d87-11cf-371c-8010-9beaa6a82340 | -12.1597 | -50.0501 | 2024-10-02 10:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| fce854a6-64fd-34b3-94bb-89c9db81e7d2 | -13.0019 | -51.148 | 2024-10-02 10:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c417a661-5cbb-3874-8c5a-df97e3838068 | -13.0372 | -51.3356 | 2024-10-02 10:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 9cdf8d50-0615-34fc-8393-c5140e3be214 | -12.8805 | -62.5117 | 2024-10-02 10:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 176.1 |
| e7b1d87f-06b4-30b8-8512-2bf627c12262 | -12.8803 | -62.531 | 2024-10-02 10:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 163.8 |
| e9bd3719-f857-3edd-8602-0f2380ab90ec | -13.2173 | -48.624 | 2024-10-02 10:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 309.2 |
| 1b3cdc76-8bcc-3272-a664-77c94d142ac2 | -13.094 | -51.3712 | 2024-10-02 10:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 6d0875a6-a501-3def-b087-abc951e96f48 | -13.0937 | -51.3926 | 2024-10-02 10:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 5627e670-4af6-3ca7-9451-53ae9552c789 | -13.0567 | -51.3119 | 2024-10-02 10:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 3ff914db-aaf6-39a7-9516-68deb85bfdbd | -13.0563 | -51.3333 | 2024-10-02 10:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 356.1 |
| 25dcc830-2f27-3886-baa5-c02328fbc2d7 | -13.056 | -51.3546 | 2024-10-02 10:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 8b5fd70e-2cad-3b71-8b61-275e6d304561 | -13.0375 | -51.3143 | 2024-10-02 10:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 641bfbb6-a91e-39a6-9a64-6bfd077772d8 | -13.0211 | -51.1456 | 2024-10-02 10:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 2e52e188-e454-31ec-86ec-7dcc37173ae6 | -13.2169 | -48.6461 | 2024-10-02 10:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 1d22803b-1765-3921-981f-3e51a5e6f393 | -13.198 | -48.6267 | 2024-10-02 10:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 8b8f8281-3387-3bd3-94b7-1cff2242c59b | -13.5184 | -51.211 | 2024-10-02 10:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| cb30d9f3-c67e-31d4-858d-ab29560760f2 | -13.538 | -51.1871 | 2024-10-02 10:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 01bcdd9a-3c19-3358-b3bd-747dd5e445fe | -13.5376 | -51.2085 | 2024-10-02 10:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 2e3b711c-9e85-31d0-8490-8cc53f9957ee | -15.9003 | -50.1537 | 2024-10-02 10:56:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 084a7630-8f28-3220-9067-7c536202bb86 | -16.6168 | -58.2343 | 2024-10-02 10:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 4388b734-261a-37cb-847a-0698f7964b17 | -16.5976 | -58.2162 | 2024-10-02 10:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 183.2 |
| dd90ac31-f3cc-3b8b-82c3-19af9df777f0 | -16.5973 | -58.2365 | 2024-10-02 10:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 280.4 |
| 04b744a4-03e7-3030-8e61-a44739add0cb | -16.5778 | -58.2386 | 2024-10-02 10:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| eec08ba0-9884-304c-a287-5bf2f3f018d7 | -16.8983 | -57.6949 | 2024-10-02 10:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.8 |
| 57e617b5-0ad1-3582-979b-a7435d12c050 | -16.898 | -57.7153 | 2024-10-02 10:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 8473aa79-3f4d-300c-9ea2-786ed5bee37d | -20.3834 | -46.29 | 2024-10-02 10:56:58 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a8694d99-c170-3fc5-8767-5739e78d137e | -20.4316 | -46.0399 | 2024-10-02 10:56:59 | GOES-16 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 0adfc6b9-5e32-3d5d-a0e0-aa3e390720f1 | -20.4309 | -46.0639 | 2024-10-02 10:56:59 | GOES-16 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 256.9 |
| 0d5be474-2588-32bc-9eaf-377e33bedefe | -21.3661 | -55.6807 | 2024-10-02 10:57:05 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e606f51a-cd4a-3cc2-9678-c4f098281ae6 | -13.52 | -51.18 | 2024-10-02 12:04:07 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5820799e-2ac9-3857-a156-02a86c28cffb | -13.55 | -51.19 | 2024-10-02 12:04:07 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 671b8bef-4b84-3687-98af-1b3f20dad4e5 | -6.33098 | -43.46854 | 2024-10-02 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1acb02b6-231b-3200-a073-653af1965d1d | -10.99042 | -41.82909 | 2024-10-02 12:14:00 | TERRA_M-T | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 90668c87-06c7-392a-8d98-f60308a3e575 | -10.99186 | -41.81956 | 2024-10-02 12:14:00 | TERRA_M-T | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 86cf739b-3627-3ec1-ae11-7508687532df | -11.58458 | -42.73632 | 2024-10-02 12:14:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 3280a439-f631-37bc-8857-18deeec8b20e | -11.59048 | -42.73329 | 2024-10-02 12:14:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| e614ce47-aa77-33b1-9c5a-09bcf64c44f0 | -11.66298 | -41.7135 | 2024-10-02 12:14:00 | TERRA_M-T | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e202a24c-ee64-3676-8bbd-be73ba92e7fd | -11.82345 | -42.66815 | 2024-10-02 12:14:00 | TERRA_M-T | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 6f26e4ac-6264-3230-9311-24ffe52093aa | -11.825 | -42.658 | 2024-10-02 12:14:00 | TERRA_M-T | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 3c415476-dcf6-3f6b-b088-027896059e51 | -10.6718 | -42.16719 | 2024-10-02 12:14:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| c0e35ef8-d430-3b37-ab47-1b66bb60194b | -10.67329 | -42.15736 | 2024-10-02 12:14:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 284fb7f6-fc8d-344e-8c1c-8d53fcf7832e | -9.74233 | -41.97878 | 2024-10-02 12:14:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 4cd16f31-dbca-388d-a245-f2d6d88f501b | -9.8164 | -41.47998 | 2024-10-02 12:14:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 75087b9d-46e9-3074-b969-d9601da741bd | -9.82549 | -41.48131 | 2024-10-02 12:14:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 8ee19882-045d-3cbc-a784-1ebc38ee8f4c | -9.98139 | -42.10367 | 2024-10-02 12:14:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| fa8d3e1a-20c6-3ab7-bbd5-9d1999a2202a | -8.06236 | -41.30513 | 2024-10-02 12:14:00 | TERRA_M-T | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f4545e7e-dfc4-34c4-a76f-76dd9e478aed | -8.52239 | -41.37499 | 2024-10-02 12:14:00 | TERRA_M-T | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5920d2cc-1398-39d0-8c89-c9971049c5a1 | -8.52379 | -41.36551 | 2024-10-02 12:14:00 | TERRA_M-T | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 99580054-7499-38b7-a443-de0feff7beea | -6.8379 | -41.83435 | 2024-10-02 12:14:00 | TERRA_M-T | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |


[Clique aqui para ver as próximas entradas](README203.md)
