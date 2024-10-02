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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40eb8004-1c29-31f0-9816-db7605315ac9 | -16.48908 | -57.30781 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 973eb81a-f674-3eb8-94ea-10a873097d3e | -16.48665 | -57.32176 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 04899543-47a8-3235-a766-47eb05d015c1 | -16.48536 | -57.30711 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| db89d4e9-d428-349b-85f9-1691e29f77c8 | -16.48454 | -57.31176 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 22e3e747-be61-3840-803e-8118cc25fc57 | -16.48373 | -57.31641 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d718fb61-d41e-3134-a386-4eda4f312de4 | -16.48326 | -57.29712 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 56f5390e-d941-3891-8a83-5c8e2e85b72b | -16.48245 | -57.30176 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 761d1d40-396a-34a5-bc82-55d03d6cf230 | -16.47709 | -57.31035 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 989baa21-317f-3200-989a-90c5b9a2eb9c | -16.47546 | -57.31966 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b04d2cd6-b2dc-39c4-aef2-be501b85b2c8 | -16.47418 | -57.30501 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 261db13e-d233-3549-89b0-63591d495c0d | -16.47337 | -57.30965 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 03ff0439-9bc8-3e25-8948-d7c3de8b7b6e | -16.47265 | -57.3577 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 993df188-7c20-3382-bd55-6e812f7cc386 | -16.47046 | -57.3043 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 78d7db5a-9be2-35a8-8ae0-494161b2da8c | -16.46891 | -57.35701 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3e652e0c-8584-3017-955f-4d1ad55a156d | -16.46801 | -57.31824 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 74fff380-281c-3608-a89d-3eacf0ce6e17 | -16.46719 | -57.3229 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0de1b0d8-f56e-33e7-831b-3d1770de0a41 | -16.4669 | -57.3905 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6373a79d-c40b-35e0-9f36-341223d6aed1 | -16.46487 | -57.42411 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| fe93ca7e-cd4f-3d5d-bebd-fc34b30239d8 | -16.46436 | -57.36098 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ac6f74d7-cb88-3062-977e-59bdc9bc9d26 | -16.46428 | -57.31754 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b3935672-b820-3e58-bff0-592f6f0decc2 | -16.46347 | -57.32219 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 58190318-ed71-3a1d-be8e-4d2c860539a3 | -16.46265 | -57.32685 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 790c3ddb-7402-3924-874e-57b8415203ac | -16.46226 | -57.35093 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 08eda721-821e-3c6e-92d7-d2b354853650 | -16.46195 | -57.4187 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5b822bfc-266a-3a58-8888-696541785d3f | -16.46144 | -57.35561 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 82907c1f-fbc6-3a1e-845e-d9ec7222d19d | -16.45815 | -57.37431 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b4130997-b43b-35b7-a79d-965dd99a7963 | -16.45776 | -57.39846 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| eed8dbd5-8a0a-39f6-85ad-0ba223ac57b8 | -16.45572 | -57.43209 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 205eefd3-64e5-37b0-8403-0d7117db10a2 | -16.45562 | -57.34483 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 005526af-1862-3815-bd18-962244456ab6 | -16.45518 | -57.32546 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 90451ed4-5ee1-3ecd-9c0c-94a724515302 | -16.44823 | -57.43066 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2f554bf4-9c0a-3a98-b55e-d20b8076d4dc | -16.4457 | -57.40104 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4c5af866-6a9f-3de4-9d4c-f7baa7ecf2ca | -16.44448 | -57.42995 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dc4b3178-0351-3700-be4e-856e79b9add7 | -16.44364 | -57.43467 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 9fa627c6-3ba5-3042-a3ec-5b3a10d02bcb | -16.43989 | -57.43398 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 17e25249-e61e-31b8-8146-d1b5db521b34 | -15.80986 | -57.33802 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e61cc06-700a-3b95-b5c2-a64c8c4b845e | -15.80157 | -57.34091 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cb34f2b-d7ae-361d-a6cb-3feb05dc4fdd | -15.80083 | -57.34515 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b30eda0-cee8-37a9-a15f-133cd0fc224e | -15.79844 | -57.3587 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ec11555-8253-3cc1-a430-6b708392901d | -15.7957 | -57.37423 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 047de4d4-7ca9-362e-bb78-f1862187ff38 | -16.09521 | -57.53212 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cd2d67a3-a5ec-373b-b9c3-1058d68080c0 | -16.09144 | -57.53133 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1503b6e1-e102-3418-8b89-4dc088705b35 | -15.92367 | -57.44489 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73a874e0-d855-344f-a3a5-673ed1ad3008 | -15.92281 | -57.4498 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3385f92-a8f7-3e89-888f-f84ad839c68d | -15.91901 | -57.44915 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98cebcaf-9b14-347d-bfbc-fc3e1cc72095 | -15.91521 | -57.44854 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b904d3c-0f1f-3242-86fb-ee526588459a | -15.90928 | -57.17433 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 60a53f7c-ad54-3aaa-b4b9-eae6a7a66315 | -15.90712 | -57.1648 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1bdc2879-31e5-3705-a9c0-2bd8933342b3 | -15.90634 | -57.16918 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69a7d155-9259-36af-9381-d5f56c4ba67d | -15.90559 | -57.17345 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8281243f-dadc-387a-81e0-2701e957dac9 | -15.90265 | -57.16832 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 81a8d1cb-68d1-3d36-ae3e-eb4b2c3a8009 | -15.90189 | -57.17263 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a93756ab-42bc-3539-bb95-3284860f7dd1 | -15.90112 | -57.17697 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aefdeb38-2949-3c74-8c28-ea4f7a699592 | -15.90032 | -57.18144 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6dd7e659-3f83-3df6-a1ee-02890d90fde5 | -15.8974 | -57.17623 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 379fc24b-460e-3fb7-aba2-1138ef7132cc | -15.89661 | -57.18071 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5489f103-5daf-33bf-9ec4-729e3dbb0603 | -15.89287 | -57.18003 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| da79af0b-fa49-3288-8145-f4dcd12f5931 | -15.89155 | -57.16584 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bb18b5fc-e031-3c01-a331-ddd44f94754a | -15.89075 | -57.17033 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7f8b8fb6-18d2-38ee-bcec-bfbf729028b3 | -15.89057 | -57.16312 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5c44fc04-cda6-3fb8-bda5-96c5111559f6 | -15.88995 | -57.17483 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a217f34-73c7-3df4-a78a-bbdff00eaba6 | -15.88979 | -57.16761 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0be55f4a-cbfd-362c-be8f-6b6667ccb7b2 | -15.88914 | -57.17937 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a674ef4-579f-3fe4-aa02-b7d63c963c9b | -15.88902 | -57.17214 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1784f828-0826-3bb8-bfe3-dd73de874882 | -15.88864 | -57.16059 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 32bb1f90-5516-3ac7-a712-fd1dba50dcf5 | -15.8883 | -57.18406 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 979a4320-79dc-36d6-b58c-a04f6150c9b4 | -15.88823 | -57.17667 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf998630-eb85-3468-8b5f-ba4959f2d415 | -15.88784 | -57.16504 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b9a7f152-1722-384b-a69f-897dc8bf16fe | -15.88744 | -57.1813 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f78f08e-47ba-3c55-b374-4f19edd29260 | -15.88686 | -57.16231 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f9b2481c-734a-3e0e-8baf-84d9142c9806 | -15.88622 | -57.17414 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85036968-9aa4-3521-bef3-e2acb48fa3da | -15.8854 | -57.17872 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31381fd2-095c-3228-8baa-736df6accd26 | -15.88494 | -57.15977 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c63c17c-87aa-3cc0-84b9-d7253b13523d | -15.8845 | -57.17601 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14ddb737-a817-38ae-9b96-024d6c73133d | -15.8837 | -57.18066 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da4641ec-aef1-3ea6-a401-7cc45c98a9cf | -15.88315 | -57.16154 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cfbf684a-8b2a-3498-ad45-17c7b4b47aa4 | -15.88124 | -57.15892 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d8da84f7-27fa-3da2-b9fc-814c907d6989 | -15.87944 | -57.16074 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2498a6f-f29c-3ca6-8203-11044a0dd26f | -15.80532 | -57.34171 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 861b8fa9-4d94-3f3c-90a6-0bfbb0743b5e | -15.80007 | -57.34947 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 615cfe30-21dd-36b2-a3b9-784cd2c31682 | -15.79928 | -57.35392 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8d0cf0f-3f3d-3857-825d-736ae1f6240a | -15.79631 | -57.34871 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6fedfda-2fed-399f-bc11-9e958c34c355 | -15.7948 | -57.79177 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b50f3aac-dcee-3d76-be99-f2be43e451dd | -15.7882 | -57.80614 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2f7ccb53-ef8d-3142-8576-555b6aaea478 | -15.76773 | -57.78669 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90037cfc-72d1-3967-b9ce-29061d2e5f05 | -15.79389 | -57.79679 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd4676e9-168e-3ea6-a1ef-fa1fc314464f | -15.79003 | -57.79607 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05e5f1e0-0f82-3d68-b9c5-6960228e6352 | -16.48827 | -57.31246 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9aa25d4d-5236-3a41-8954-dc1e720a73a4 | -16.48746 | -57.31711 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1ea8d265-9744-34fd-9c45-5615f941d035 | -16.48698 | -57.29781 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 3a4cd494-9d78-3e5f-8ee4-0bf1603f89a3 | -16.48617 | -57.30246 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 0b044cd7-2333-3267-9bde-d2d9774c22dc | -16.48163 | -57.30641 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 92580d1f-4b39-32c3-aa93-a729608937cb | -16.48082 | -57.31105 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 6de901f2-efc4-33b9-89b2-03474068020c | -16.47954 | -57.29642 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| bf29e10b-d5d4-3ea6-8be9-884c9587f0c2 | -16.47919 | -57.32036 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0278dd75-7e05-3e06-8546-eb3202291c39 | -16.47872 | -57.30107 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 61f469aa-0508-3c05-881a-9dd52d979f3f | -16.47791 | -57.30571 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 0366cf76-02fe-3792-ab9a-0944a93f02c8 | -16.47721 | -57.35371 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fe6ad0c9-a33e-3e67-bec5-f2a6834ed8c5 | -16.47628 | -57.315 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bbdd3146-35fb-3490-8b45-a3def003ef43 | -16.47347 | -57.35302 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |


[Clique aqui para ver as próximas entradas](README111.md)
