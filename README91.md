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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b866eea-e901-394a-9556-45679abc89f0 | -3.44661 | -54.63851 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9ae660ae-7c24-37e8-8872-808eae8dcd4f | -3.07036 | -54.78427 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6bc0383-f29e-39d4-8c71-537bbb30d231 | -3.06705 | -54.78376 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef38b39f-cc23-37d1-a02f-3ce6e207527a | -3.06651 | -54.78719 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ed01ecd-3776-3464-bddf-47920faa73ce | -3.04912 | -54.85488 | 2024-10-25 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 496f9d46-970a-35de-b948-fb66c1849413 | -3.28071 | -54.15808 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2604430-2334-340e-8413-0e1ac12ca768 | -3.26136 | -53.718 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38b73575-facd-3e8d-9597-f2b90cd0b70c | -3.14845 | -54.3512 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d909a1ad-e96a-3d63-bcf1-b78ec5f1e9c0 | -3.13832 | -54.28569 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d5d5325-623d-3630-8e11-585f2c2f98eb | -3.135 | -54.28518 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abc61bb2-e2e1-398c-86ec-0170cb8505c7 | -3.13331 | -54.27424 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| acd67e9d-7be1-33bd-93b6-0de16ddc3e11 | -3.12944 | -54.27721 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93114443-4790-3963-8571-47f0924b2fdb | -3.12612 | -54.2767 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c4f95ad-7268-3cc8-9a46-ca6b10462669 | -3.12504 | -54.28365 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45cc3aa7-aecf-3b12-8f3f-88db04d4d8df | -3.11836 | -53.71804 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87727f12-637c-30f8-954c-11c066f5e25d | -3.11334 | -53.72818 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90f63c34-65fe-3c76-92cc-cb096383f4dc | -3.10972 | -54.1636 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84686c2d-a219-3a42-8d83-aa1f55847b69 | -3.10943 | -53.73123 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cee1dcc-a594-3ab4-a238-c4d744391a1b | -3.10918 | -54.1671 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bfbd36f-b044-3967-85dc-1db96d5a5dcd | -3.10857 | -54.14907 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 475af48b-fa33-38f9-89ac-34d00f743183 | -3.10663 | -53.72715 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bd3755f2-d8ad-3a5b-a8c5-2c01a924873b | -3.10552 | -53.73426 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d6406373-2d75-32d9-ae90-ce5e168fdc40 | -3.10477 | -54.17358 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 159417b3-43cc-358b-8936-687b7653cb39 | -3.1047 | -54.15205 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 960fe563-d51e-3b34-8851-a18efcc91127 | -3.10416 | -54.15555 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a1b2948-300a-3b96-a7a9-5375f0630de4 | -3.10383 | -53.72308 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6401b8d2-3c12-3017-b408-6957d38560a4 | -3.10361 | -54.15906 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 138eb874-5042-3d25-8162-d8787e7f6b69 | -3.10253 | -54.16607 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44a488ac-c3bc-322c-923e-c9dce8e64915 | -3.10198 | -54.16957 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed29a357-7f0d-3909-ac6a-090234652d89 | -3.10176 | -54.15167 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f0000e9-38b8-3ab9-bd13-f2bea8fb6f6a | -3.1009 | -54.17656 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a2b7d1b-1a7e-3ec8-8c1b-f9c8bd22cadb | -3.10066 | -54.15867 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6896c473-0da8-3b55-b8f7-6796b9a52b3d | -3.10011 | -54.16217 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c805346-cab4-3512-9c09-8ce779785b38 | -3.09711 | -53.72204 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 998c9cf9-8a6a-3647-8a65-d1122c688192 | -3.09656 | -53.7256 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f34eaf25-e2b1-3fb1-a83b-bcf5d205191d | -3.09456 | -54.15414 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49a894a7-e3c3-3786-a18a-52259160c99f | -3.09291 | -54.16464 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a42da72b-65ef-3784-839d-faa712039625 | -3.07851 | -54.16957 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 244e73db-f8d0-3b6f-ac77-0a278e196acb | -3.07792 | -53.88948 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf2fccb3-ac2a-32cc-bef4-9ffecbadacef | -3.07781 | -53.82416 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e6e7245-cf56-3d92-81a3-54283901bec4 | -3.07501 | -53.82013 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00660be3-5e34-39ab-85cf-9a00f9b496e9 | -3.07391 | -53.82716 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ecc033c-c3d1-387e-8962-62d68fd2c24d | -3.07111 | -53.82313 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21e40a4e-2b61-3c7d-a0c1-af01716db8e4 | -3.07057 | -53.82664 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a73cec04-d770-389b-9ca1-e674e79f9b98 | -3.06831 | -53.81909 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d53034fe-4a9e-3408-8e7b-e2e8b8844eae | -3.04636 | -54.85094 | 2024-10-25 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0873c2f-055d-33f9-84ac-6aae29ab18ec | -3.04254 | -54.18185 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdab8650-055a-3699-9f6a-2b3ff19a671b | -3.00862 | -54.13735 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b530812-f9d9-373a-bee0-f7eb9d3febd5 | -3.00583 | -54.13335 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28a444b5-6f57-335b-ac5a-1c543e484315 | -3.00529 | -54.13684 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 140822ab-91c3-3f8a-a9e0-c09e521bf016 | -2.99607 | -54.11009 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4603611-d8e3-3fc6-8ded-149fd9891716 | -2.99552 | -54.11359 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 523d1764-c893-30fb-8922-b7432f3b1f7a | -2.95515 | -54.15375 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf52dd29-c09a-3a2f-bc11-e369af1c29c3 | -2.95183 | -54.15324 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6040278d-2627-3258-8e15-c95bd92cbb31 | -2.94461 | -53.70276 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea5a60f7-df20-3d07-933e-90c7f21ac206 | -2.94125 | -53.70224 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8e5a624-f5b5-3b27-abbf-a26dd2fefeed | -2.9368 | -53.92154 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47db986e-e4fa-395f-a4e5-286972a31831 | -2.93564 | -53.90696 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c82e57a7-025e-351d-9c65-a157e3ccf9a6 | -2.90996 | -54.22517 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4a80a20-9ffa-3df1-abf7-1323c78865c2 | -2.90123 | -54.25928 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a16d7069-2f0f-3a62-8f0f-c030da9dd5f6 | -2.89252 | -53.99092 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a67b1a0-bb78-3424-a515-fafe91b78726 | -2.84198 | -53.98669 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93107a23-d293-3c82-b59b-2e8cd9cbc830 | -2.79962 | -54.10538 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 405d3609-efae-3ab8-9ff6-fefffc0de119 | -2.79908 | -54.10887 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6b93005-63d5-325f-bc25-7c2a7e33d773 | -2.74983 | -54.03305 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 682ffa87-0d8a-3f97-884f-f625f2141bb2 | -3.65142 | -54.21904 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c554fde2-c0ba-3420-97fc-9ae2f6747062 | -3.64863 | -54.21505 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01f5dd3f-001c-31c4-b987-b2af97b5f8fe | -3.63307 | -53.96758 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c50707cc-d073-367c-b7d0-d8d343b189d5 | -3.63252 | -53.97108 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab744f9f-75d6-3756-b827-a29a5bab9744 | -3.62972 | -53.96704 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba6b7e37-7e3c-3443-8fb2-df24fea62340 | -3.60297 | -53.96281 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a81c616-966b-3041-a855-6bfba84b47aa | -3.55105 | -53.99466 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46cdc2b2-ca2e-3f14-84f7-b26be4b86bff | -3.49515 | -54.437 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35905171-9b97-3b27-a264-e25de30e4512 | -3.49299 | -54.45083 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b2306a3-60de-3446-b2ad-4e45ce0c48fd | -3.49192 | -54.43647 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22c3db71-7435-3c25-a129-94dc1ed68136 | -3.49191 | -54.45778 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0aec2f6-b7ff-38b7-89b1-34135e7926cb | -3.49137 | -54.43992 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79582e50-609b-3a5d-96c5-eb5b0ac54343 | -3.48806 | -54.43942 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51c06ba8-a4e6-324a-94b2-75b5746c2b8f | -3.48751 | -54.44287 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6157de5f-bc66-3e2a-ae95-5fe04cacca8d | -3.48697 | -54.44633 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65acabfd-514b-3848-8536-4523fc2d88f1 | -3.4842 | -54.44236 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1d9c7b7-80b1-333a-b8ea-a84d7b58ed5d | -3.48419 | -53.98433 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa5a16c1-5e5f-3094-8560-e84fe82b94cb | -3.48366 | -54.44582 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6bc12ab-e4df-3e68-b802-5ccedbe5aa14 | -3.48364 | -53.98784 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c588bdc-5f2b-31a7-a60f-f43f6bae6bb2 | -3.48085 | -53.9838 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af3e2778-1fb9-3655-93f5-723f8655e753 | -3.4803 | -53.98732 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14921421-5fc4-3b23-8328-c899ff346bff | -3.4179 | -54.2792 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8664a66-b061-36a5-bd6a-bdf0ecf6b12b | -3.41125 | -54.27818 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbe62180-96a3-3bf2-9dea-b3d6ea2eeb3e | -3.13886 | -54.28222 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9277a776-627c-3cf4-b81b-173dbd148b5a | -3.13609 | -54.27823 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec307f3f-e86c-3952-a302-a65d4c6b0da0 | -3.13554 | -54.2817 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1ff0c80-b123-31a3-9d02-f9afc2f5941e | -3.13446 | -54.28865 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72c5bcce-28ce-3dfc-895f-c791c0bfda27 | -3.13276 | -54.27772 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb74e670-deb4-3266-b7e6-9ad80edda740 | -3.13168 | -54.28467 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a6ff504-6ad4-3b06-aac4-5c5262d87275 | -3.10863 | -54.1706 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4789301-5397-3d8f-8480-96d497e3089e | -3.10803 | -54.15257 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50a156ff-8936-3e79-a107-4d438ed65be9 | -3.10748 | -54.15607 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa030e74-bbf6-3772-98db-a51de0bc2a83 | -3.10694 | -54.15958 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ebb7f9-d1c4-3d69-b662-20d1e318ec1c | -3.1064 | -54.16308 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41e8ecd5-a19a-3a27-97dc-6fad938de482 | -3.10585 | -54.16658 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README92.md)
