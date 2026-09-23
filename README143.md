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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52e24c8f-2195-31f5-920a-cb5d4f50f405 | -9.043 | -48.1384 | 2026-09-23 14:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 6f097584-c373-37de-a013-ed9a35715e77 | -2.9525 | -57.72 | 2026-09-23 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 3e0e81b2-bde9-339a-bedb-2a9f91a291c2 | -8.7772 | -49.955 | 2026-09-23 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| c38cdaf1-22fc-37b8-8c99-273be29496f1 | -8.9019 | -45.9104 | 2026-09-23 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0f6ee84e-0b1f-3aad-921d-0a4e6efb7eda | -6.2394 | -41.6875 | 2026-09-23 14:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 50f7b535-d6ff-3ebb-a5c2-6c0a5028a70e | -6.0172 | -45.2462 | 2026-09-23 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2acf3013-7e41-3b72-a6f7-c125b7c51d83 | -6.4671 | -59.9711 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 914a97d3-c1e7-3a37-947e-211b439c01f7 | -9.8499 | -48.4272 | 2026-09-23 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| eaedb14f-39bb-3342-b906-a4500603b821 | -8.4985 | -57.6075 | 2026-09-23 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 217.4 |
| 1e135a2e-c2cf-3332-bdf9-2164ac5b8dbd | -11.3547 | -43.4001 | 2026-09-23 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 357b261d-c25b-360f-b85c-0f9c095c7f60 | -6.2205 | -41.6891 | 2026-09-23 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 886691d9-a8bb-361e-bdcc-a055e08308f2 | -8.4613 | -57.6096 | 2026-09-23 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| d0c1e9de-83bc-39b9-84bc-ad2c91f350f3 | -7.0826 | -42.0868 | 2026-09-23 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| ac1bb999-5ed3-31c7-8c0a-2871cebc180a | -2.5687 | -57.5135 | 2026-09-23 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b6fc8016-4c32-3fc4-bcd0-675352887b6b | -9.788 | -46.0819 | 2026-09-23 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 8ce5b913-f33a-3d4d-a437-11d25c2929cc | -6.4485 | -59.9909 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 77f45f12-f685-37f4-ad98-a851d87cf250 | -6.136 | -59.9254 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0f7fcce2-cab1-37a8-b82d-900516bdf67b | -10.0096 | -45.1915 | 2026-09-23 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 230a8036-ecf9-3bd8-b010-26b2cafe0884 | -3.2047 | -53.3977 | 2026-09-23 14:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 165.7 |
| 689fcdef-75ba-30d3-a2b2-b98d3b273de5 | -6.4486 | -59.9717 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| b3f72ccc-6975-3f36-8e2f-0f7f779347e8 | -6.4368 | -48.4436 | 2026-09-23 14:40:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 91.7 |
| e7ef7400-6e5b-358e-b3ae-a65923d41ca7 | -6.5639 | -44.8628 | 2026-09-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 7c4d3cf0-8c45-39bc-8269-5e8167dfa7da | -11.801 | -49.8345 | 2026-09-23 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 8ad5318e-f883-3967-b082-54ce2116e0a9 | -8.7735 | -45.6303 | 2026-09-23 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 0555a185-86bb-367f-824b-163550104b78 | -9.807 | -46.0797 | 2026-09-23 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| ce3d015b-23fa-3eff-b229-630f07d3bfb0 | -11.4209 | -47.3603 | 2026-09-23 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 189.8 |
| d0cf3319-23c4-3914-b8e5-444cbce9e835 | -9.6043 | -48.4529 | 2026-09-23 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 22e4a443-e882-3c88-bfc4-ac539732065c | -11.6812 | -50.2147 | 2026-09-23 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| f628a6c2-7cee-3c79-9380-d1fe128f6d60 | -8.0093 | -61.3824 | 2026-09-23 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5d6f48c5-020b-3e66-916c-45dbd1fdd677 | -10.1104 | -46.0661 | 2026-09-23 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 02100673-8281-3195-bfa2-a1df9a28d87e | -11.3592 | -44.2224 | 2026-09-23 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| fd95d6f8-326f-3af6-a155-c9b5cb7ee3d5 | -8.9016 | -45.933 | 2026-09-23 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e69cfe69-7b84-3daf-b79f-a35e6c0224e7 | -8.3591 | -45.6056 | 2026-09-23 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 745d588d-c7b6-3225-b8a5-64a4411ee173 | -2.9158 | -57.7789 | 2026-09-23 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f90fb3d7-6f2a-3249-a04d-702856ef4e99 | -11.4782 | -47.3529 | 2026-09-23 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| ce9a69c3-1ed3-313c-b14c-53ca4690545b | -5.9983 | -45.2702 | 2026-09-23 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 3aab2003-0f38-31a6-82d1-4409ec19f7b7 | -6.5829 | -58.9851 | 2026-09-23 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| acd4e0e4-05fe-3f28-9e62-cf4a15cfa9ba | -6.5941 | -43.7333 | 2026-09-23 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ad2ea950-9346-3b9a-a1d1-7151f401b779 | -6.467 | -59.9902 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e254b144-7353-31fe-80f7-5966da5de0d3 | -9.3871 | -47.7526 | 2026-09-23 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 0272dbdd-bd59-33d8-9435-9211acfc90d8 | -7.41 | -44.7198 | 2026-09-23 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| dc80019c-f8e8-3f70-87bd-85a7b4e882da | -6.4302 | -59.9724 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 3a98dd6d-e66d-386c-a7f8-d84d1842e450 | -6.5963 | -59.9087 | 2026-09-23 14:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 37ae48b8-db9b-3de8-922c-fb760c535e06 | -6.5056 | -45.0723 | 2026-09-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| bfaf5ed6-3dde-37bc-9dac-1972c9fde951 | -6.3382 | -59.9566 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 3906820e-a867-3cbe-a83e-f32eaab342b9 | -6.9029 | -46.5456 | 2026-09-23 14:40:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| e65aae0a-293e-35f6-ab28-7a06aeb7e432 | -7.4495 | -44.5557 | 2026-09-23 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| ab088173-21d5-3069-ae9d-b12c688378b2 | -9.831 | -48.4292 | 2026-09-23 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 9fe25b86-27a9-3f56-aac2-d4f78d87fffb | -6.1543 | -59.944 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7948cf0e-0210-3c83-8eb0-f943fd97ec8b | -6.9841 | -49.7777 | 2026-09-23 14:40:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 209347d4-c4e0-3059-88b4-4ca8b75f2e39 | -8.4983 | -57.6271 | 2026-09-23 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 176ae6c0-bc1a-3e02-97fd-b956d7aba65e | -3.2955 | -59.4284 | 2026-09-23 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f04f3d9e-0d4e-33ca-9a39-351b8ee5686f | -6.5636 | -44.8856 | 2026-09-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| b7150d56-558b-369b-9dc9-977a277cc6ab | -9.9058 | -48.4867 | 2026-09-23 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| fbd45208-926c-3c55-8d82-3eea8621a24f | -11.1204 | -48.327 | 2026-09-23 14:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| d8762477-7659-32b2-81c6-3bd600a84d6a | -6.1317 | -45.0109 | 2026-09-23 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| c1730847-b123-3999-abb3-d76317bd2909 | -6.9228 | -42.8852 | 2026-09-23 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| fa4f35d5-b6b3-334a-a087-be96ba2eaed7 | -10.1294 | -46.0638 | 2026-09-23 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 203225d1-74ef-3be5-a4ed-9b4b50b365e1 | -11.6789 | -43.4921 | 2026-09-23 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| c7eb1f70-905b-3be2-a00f-76338edd1215 | -6.6148 | -59.908 | 2026-09-23 14:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 180.3 |
| 5135d5d7-3ea1-3308-a5ce-c7bb56aa9c71 | -7.0352 | -44.6396 | 2026-09-23 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 098defed-d080-3b49-8716-b1f7de7ed8e6 | -9.5735 | -46.5337 | 2026-09-23 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 12293068-e08d-359f-9d04-6ae547871b3e | -8.7735 | -45.6303 | 2026-09-23 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| ac7293fb-e933-3e2b-9546-9e6a24309e9b | -11.4209 | -47.3603 | 2026-09-23 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 227.1 |
| d9151ecb-89f8-3c9a-a24d-e1b17272cd39 | -8.3588 | -45.6282 | 2026-09-23 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 74ae7a3d-4446-3296-80f5-ac16540e14da | -6.4671 | -59.9711 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| b4365a17-f480-3d79-bf51-c04f18c2815b | -2.934 | -57.798 | 2026-09-23 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| e7a850c0-2235-3759-b98d-9eaf3e68ace1 | -2.9525 | -57.72 | 2026-09-23 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ef417051-76d6-3acf-9813-d3433bd9d6d4 | -6.6148 | -59.908 | 2026-09-23 14:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 189.8 |
| 3731528e-48f0-3708-9695-a8dd714a090a | -2.9158 | -57.7789 | 2026-09-23 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 9705ef23-dfa7-336a-b626-f6043f8379bd | -3.4272 | -58.2138 | 2026-09-23 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 380cbec3-01ef-3452-b3e7-398be1c96bf4 | -6.9225 | -42.9088 | 2026-09-23 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 7f70342f-b6e3-3020-87d1-180af71043f6 | -6.9029 | -46.5456 | 2026-09-23 14:50:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| e998d834-dee1-3e3e-9436-7c3605d9353b | -2.8609 | -57.78 | 2026-09-23 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3306a9ba-6bf3-3fb9-b3b7-62351f67d1e6 | -6.4302 | -59.9724 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 78f8414b-bcfa-310a-9128-d14b16db57b3 | -11.1541 | -42.8364 | 2026-09-23 14:50:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 172.5 |
| 5df1a17a-8f09-3a1f-9fec-56797b05798f | -11.4162 | -45.3486 | 2026-09-23 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 304.6 |
| 81f02718-cffa-39a9-9a7d-09e9ea5a1592 | -9.5731 | -47.9529 | 2026-09-23 14:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b0abf43a-ae79-37aa-b97d-a9bc9254550e | -6.4368 | -48.4436 | 2026-09-23 14:50:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 89d4dfed-5656-3109-b0fa-bb9e186db71b | -6.5759 | -45.5419 | 2026-09-23 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ae0074b3-2a5f-34ce-8d16-f1e121aab4f8 | -6.4486 | -59.9717 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| b0f5fe15-266c-3b91-bd40-be2b0a2e6487 | -10.0096 | -45.1915 | 2026-09-23 14:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 492200ee-11ae-3a00-ab3e-61906d5f46c9 | -8.4613 | -57.6096 | 2026-09-23 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ff365dcc-6ad4-362a-8669-8a4f4a44cdc3 | -9.8118 | -48.453 | 2026-09-23 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 074cbb79-79ae-33fb-bc48-99970e8e9577 | -8.0093 | -61.3824 | 2026-09-23 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8a959839-2e05-3072-9683-0a9bbe96d386 | -6.6332 | -59.9073 | 2026-09-23 14:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 2531fb81-7996-3842-86c5-73fce628bf72 | -4.2632 | -55.4303 | 2026-09-23 14:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c5ea5627-8b7f-394a-b66e-8554c9fe5249 | -2.7713 | -57.0229 | 2026-09-23 14:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c8a82dba-9eb4-3c24-b20b-986534ccb4ba | -8.4799 | -57.6085 | 2026-09-23 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| d8e87985-640d-37f3-9337-f151fb92d64c | -9.831 | -48.4292 | 2026-09-23 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a878b480-e251-3f1f-b082-65bfd5ac5ad1 | -11.3359 | -43.3793 | 2026-09-23 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 1da102ba-f873-34cb-a16a-8b8889a9b14c | 4.1314 | -61.3134 | 2026-09-23 14:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 541beabc-4386-3f1c-8e7c-512a093f229c | -6.2399 | -41.6394 | 2026-09-23 14:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| fbb03ff7-5594-349c-996d-d11f0069fbfc | -6.3382 | -59.9566 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 6ab7b3c5-90f2-3c68-b70a-b3096424dc42 | -7.5704 | -57.6766 | 2026-09-23 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 63fd3ef3-7afb-34b3-832c-76da641cf32a | -6.7119 | -58.9992 | 2026-09-23 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 42ffb4d5-0c9a-3c43-94dd-ab9115d8c4b1 | -8.1215 | -48.2245 | 2026-09-23 14:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e489e881-f7de-362a-8851-0770f5ea54f1 | -5.7567 | -45.1067 | 2026-09-23 14:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 89b21d0d-e976-30cb-9e71-d974ca66777a | -6.9414 | -42.907 | 2026-09-23 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 88b5c0cd-7402-3f13-ac6a-9f5dbaa4507c | -3.4272 | -58.1945 | 2026-09-23 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |


[Clique aqui para ver as próximas entradas](README144.md)
