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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6339a5e7-5a7f-384e-a12b-d496a5919542 | -1.7124 | -54.52935 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a6cbbc12-358f-31b6-ab1f-68f3d2dc1988 | -1.70934 | -54.52783 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a65cea9-558e-34e7-a1d7-d7c8ee75d348 | -1.61041 | -54.77532 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94058956-5717-34a5-bb21-81c7a5106384 | -1.56369 | -54.44636 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 240cf328-eaec-3599-84f8-c88661ea62c6 | -1.56303 | -54.45047 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a002e2b6-e55f-34d2-b598-af37e62f5823 | -1.28825 | -54.67273 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81d708be-ebf6-32bc-bb4d-a56654ec6e68 | -1.25814 | -54.69043 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b613a087-5d4b-3174-a486-a39dd79c8835 | -1.24256 | -54.53502 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30802419-acb1-30da-af1e-2c4784ac952d | -1.21228 | -54.19812 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 055935f2-9ade-3849-8e05-b1d191b87236 | -1.2095 | -54.16898 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fedb4860-8760-3162-b84c-8f96ec3c7a8a | -1.20882 | -54.17333 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ba829f7-3a0d-3abd-a0e5-fe157a3c2bbc | -1.20815 | -54.5253 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05924ef6-9ae6-3cc7-a8ea-0f7a77d51468 | -1.18118 | -54.18167 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b734eda-9966-37dd-b244-eb69f02f8a27 | -1.17687 | -54.18113 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28be9216-f5b8-36f9-acd2-e3d52987f2c9 | -1.1702 | -54.08558 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 401090b7-339b-3bb1-a408-84b0112e3e5e | -1.16959 | -54.08943 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a96ffbca-c1ae-3057-bb29-aec09a6349bd | -1.16698 | -54.1881 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2eecb68-6498-3815-9bcf-3c32d5276b54 | -1.16269 | -54.18744 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7601a571-02e9-3619-9867-827b0b49a206 | -1.12078 | -54.14776 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27ca76fd-73ae-3502-944c-aca4bdd6ee4b | -1.1202 | -54.13188 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84cff5f0-f1a9-363f-830c-fb8d2683d837 | -1.11957 | -54.13592 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37c0887f-5e12-317a-bb7b-48cc9d4e944c | -1.11769 | -54.14808 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb0c7b64-f233-3edc-b746-c48f3b1727f9 | -1.11651 | -54.14703 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9aabd8d6-c416-3293-8a5e-b110a9616fed | -1.08913 | -54.21846 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75b35797-89bc-3d50-b576-5da95c5ce142 | -1.08456 | -54.16351 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91fddffc-e428-3388-8918-5ee4049b1315 | -1.76687 | -53.74742 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a82b720a-13c9-3646-b4c9-edb490713bef | -1.65542 | -53.3988 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ce9fd68-4801-3b4c-9959-8f32eea97fba | -1.19775 | -53.52446 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 948087d8-163f-360c-beab-65a52586f040 | -1.18782 | -53.5075 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea766b3d-c399-304e-9601-e9d6616d7fc6 | -1.18725 | -53.51113 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7216f6ac-22cc-3916-b8d7-7ef1ab152d11 | -1.18373 | -53.5068 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81522168-7e43-310e-b51e-2a5ea00fef94 | -1.17965 | -53.50608 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b3dab58-6bf2-3e40-8738-60710d6033a8 | -1.17903 | -53.50997 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae331182-ba17-3708-b978-4bd7cd9c040a | -1.17613 | -53.5018 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96fe490a-6ff2-30d6-853a-a1ee69e5c544 | -1.17556 | -53.50543 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bf071d9-a97b-37ad-9fd0-070b88bd3c14 | -1.17203 | -53.5012 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd427c4c-9a61-335b-a718-a4b3c3dadab9 | -1.17146 | -53.50482 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58318b44-8e35-32bd-8902-faa6a2fcfcb0 | -1.17119 | -53.66704 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d893647-3ae2-303d-acc1-ca22e5489b78 | -1.07293 | -53.65584 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b1250b9-d166-3ff6-8330-a3f7b4046f57 | -1.06877 | -53.65527 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7694f5e-683e-3973-a38d-24a29f141711 | -1.06821 | -53.65886 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 907ce72c-87a3-3982-bb92-604ec5a6bc11 | -1.06764 | -53.66249 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4b112a9-a1ad-36d0-8d3d-451a7672e901 | -1.06407 | -53.65819 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99a756a4-4422-3dcf-8240-fc3b4a5bca6b | -1.06349 | -53.6619 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 124a806f-a1a6-371e-9c1f-55e518f1fd3e | -0.98875 | -53.7038 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c582cc2e-ced8-3519-81c0-9ec3f19edf5f | -0.98816 | -53.70747 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f4d36796-7b81-3701-a5e9-f498cf1cb2ca | -0.98459 | -53.70315 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e47905a-1a8a-39e2-9318-a7e78dfdc5c6 | -0.98399 | -53.70686 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bac2eccb-8b11-3c2e-a563-7b9afe18e8bd | -0.98341 | -53.71047 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 807d142e-2036-3933-aca6-dac55317d93e | -0.97983 | -53.70623 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ac790c40-c8a9-3854-8425-1b0190035077 | -0.97924 | -53.70983 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2df09039-61d2-330d-8990-1635c978e563 | -0.97867 | -53.71341 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 32a96c75-07c3-3816-b350-28b75dc50b0d | -0.87865 | -53.68725 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 668bf386-43ee-32d3-9907-d526d693f2ae | -1.4871 | -54.27511 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef1be275-c747-3fb8-a461-70ad50fed6ad | -1.44983 | -54.07283 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dff41f13-d98d-3d9d-93bf-eb9a377de296 | -1.44979 | -54.0735 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94084e36-e476-3671-9c3b-449b5a97c29f | -1.44921 | -54.07664 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f73be185-c3a2-3169-8c5f-4ef13d7bd644 | -1.4374 | -54.22898 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bdae925f-2abf-360a-81a1-871f4bfd0e75 | -1.43672 | -54.23316 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 456cd149-e2aa-3d13-9226-bbb7c7a49453 | -1.43484 | -54.22542 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 63efba44-6866-3ea3-94c5-28313fba90f0 | -1.43423 | -54.22936 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c17bb49-bded-38dd-b6db-7c5786f64615 | -1.43377 | -54.22436 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0ca7417-70c7-36f6-a610-ef6547501c29 | -1.43313 | -54.22826 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0f6ffd3-d20e-3af7-9183-c852f65d3bd8 | -1.43057 | -54.22469 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14f496f5-5f55-3384-a825-ad908bb5897d | -1.4295 | -54.22363 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1046299e-bf89-3b92-a44f-95fce80d6c44 | -1.42632 | -54.22383 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bef23a62-ada5-3081-bf74-eaaa3f1aad39 | -1.42525 | -54.22275 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d47dac31-ef23-3b4c-a8c1-e8ae843cd623 | -1.42207 | -54.22292 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82225c7d-1d73-3766-b24d-a28a1595d5b6 | -1.42073 | -54.55116 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eac2500-ea77-3e8f-afa9-72898c97b9a5 | -1.41569 | -54.55461 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60ea9af9-ea6a-3639-b617-f3f155833245 | -1.39426 | -54.04059 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0833a45-032e-3732-8321-b6c2a4d56bac | -1.39004 | -54.03985 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1156a80-8644-3a8f-9297-5c39081e5b07 | -1.38941 | -54.04374 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ac2e522-7bac-3977-8403-11950e1af306 | -1.38518 | -54.04309 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fe7fa48-5b4e-38a6-a3fd-4bd2fbd9a687 | -1.348 | -54.60993 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 835bdc36-1a58-39d3-90f3-f5a561a0ea57 | -1.34734 | -54.6141 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ded9e85-c4e8-3798-a585-223d0c64b9fa | -1.34361 | -54.60917 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6b44609-6512-3783-be00-1b28ac9ac449 | -1.34295 | -54.61333 | 2024-10-29 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68df1e5e-ce46-382c-bd2a-29c239759588 | -1.34122 | -54.65297 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b0f3aae2-c55d-39d4-a6f0-d69442c60969 | -2.26185 | -53.55037 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4234f0c7-3569-340f-b1d4-d9b4255dae4a | -2.26129 | -53.55391 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b764255-29ac-38ba-9856-5dc1110de261 | -2.21746 | -53.67162 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1975bc49-fd3e-37b5-86ca-bcbe45bc74be | -2.21688 | -53.67526 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a442036-c8df-32f6-8500-fb06a2f68aba | -2.21629 | -53.67889 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 055a9002-bf59-3502-8a0a-89a3fc80e7b4 | -2.21338 | -53.67099 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 309411c0-6015-3be9-9fa4-6b739f176f6d | -2.20229 | -53.68786 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59c54cf5-d8d4-3f13-b08c-cb99f17c1045 | -2.19763 | -53.69083 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59c71871-5a9d-3bc0-96e1-3c9435fdd7c4 | -2.07696 | -53.55716 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddbeb953-eca1-33dd-b82a-1bd6f61aaffa | -1.87322 | -53.76026 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b7b631b-df76-3369-abf0-199e204d81e9 | -1.86909 | -53.75961 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48b7207d-e846-3291-873e-90af2e4a3adb | -2.39191 | -54.66063 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 957d8535-7ba6-3ae5-b0a7-5c3745615a4e | -2.38689 | -54.66412 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4ad7d99-d4b3-30ce-b2a0-5589bc991beb | -2.16513 | -54.63901 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc42d7aa-8489-36dc-b003-d79a29d2f5a4 | -2.15711 | -54.63346 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9ff0a76-dd82-3766-a8df-09787699c1b1 | -2.12438 | -54.8066 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ab9c032-fd54-3fa1-b9bc-591b8e6b4096 | -2.12068 | -54.80161 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ed73b1c-d354-3730-abed-d88dd58245fb | -2.32675 | -53.74445 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b49c4c5b-4100-3888-b0e7-503e93a4679d | -2.28049 | -53.7709 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2d0566a5-f4e0-36a1-ad85-0b76f4e16002 | -2.27989 | -53.77455 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9f896e6-ad6d-3ca8-aa97-d418cfdb0f8c | -2.27579 | -53.7739 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README53.md)
