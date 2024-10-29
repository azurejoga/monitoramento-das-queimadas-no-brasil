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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 169e9d93-f9e3-3f50-9c2f-0023eeb97cd6 | -2.27519 | -53.77757 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee637a07-43fb-3bc4-8447-8267124e0c8c | -2.27339 | -53.78862 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa11ee57-9e9a-3686-8ea3-23c4a5e0e5b9 | -2.27278 | -53.7923 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ed60cf1-39c9-363e-817d-b1ef2a0e4c2e | -2.27169 | -53.77326 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aee67ff1-6785-3537-9115-aeca0e7d31d7 | -2.27049 | -53.78062 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9742925-1b9c-3783-b87c-2b85d3dcf566 | -2.26927 | -53.78803 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7859f1c6-a388-3ecb-9d69-e4137ec4eea4 | -2.26867 | -53.79173 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 621bc4ca-533c-3e63-bb24-2ad12b763a1e | -2.25192 | -53.71783 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a780ca7a-4432-3553-8de9-c65cec015f57 | -2.25134 | -53.72146 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94a30727-9f30-3294-a56f-44f2441e6ed4 | -2.24726 | -53.72081 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bdfff57-9238-30a0-beb0-fcbe6f864113 | -2.24668 | -53.72445 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 239481d7-8321-38ef-8a3e-a5ca9b6324fe | -3.20724 | -53.85202 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6b91edb-c10b-37d6-b2b7-ea6ee39f74e4 | -3.20667 | -53.85559 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b91951b-3190-3308-8945-a4b3b720d872 | -3.2031 | -53.82589 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33a0f89c-bcc4-34ba-b588-b96f67aaa095 | -3.16764 | -53.91648 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12864e77-5500-3f31-9365-a5424080e4d5 | -3.16414 | -53.91224 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13cdf2d0-069a-3746-96f7-3bdfce4712b4 | -3.16355 | -53.91587 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5442b8c4-dc47-3789-8b7e-145363ec4032 | -3.16005 | -53.91163 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b6ab954-daf6-3faf-ba7c-75725aef6e1f | -3.15597 | -53.911 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4f8ebfb-0429-37da-8f90-6f12f333efd7 | -3.15537 | -53.91468 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b10507b-6e36-3327-bb95-8fbf0bb5f298 | -3.15477 | -53.91838 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 104dd520-d911-3c18-ac9d-2eedbc00a524 | -3.15128 | -53.91409 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f36232f-a8cc-392b-9531-ea3c4fd71854 | -3.14718 | -53.91353 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f25810d8-63c0-36f5-8d36-d4deb805f405 | -3.11681 | -53.7129 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db16ee2f-697d-395d-a721-2416ac7691d8 | -3.11625 | -53.71644 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2fcf54d-edd1-39c2-a409-c63d5ecfcf20 | -3.11568 | -53.71998 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5cf998a-6697-33c3-bbc7-34d5627ac674 | -3.10358 | -53.71808 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2078e416-9307-38d6-8fa0-8322d018832e | -3.09954 | -53.71744 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7f78df25-def8-3e7a-894c-e939798afaa1 | -3.09897 | -53.72098 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aef13710-dc79-3503-b09a-60e145c6e45d | -3.09551 | -53.71679 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7579b091-66ae-3748-9bd5-9888406bfdfe | -3.09494 | -53.72034 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 502d844b-a7ba-3d77-8afd-a8da03037b8c | -3.09323 | -53.80836 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 742718eb-aa75-3a3e-b557-fcdf94acaf12 | -3.09264 | -53.81205 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 988d6470-2263-30a8-a3b4-4c3d2f0382ce | -3.09205 | -53.81571 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 969b361f-efac-31db-b789-27359201377e | -3.09147 | -53.81937 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db0098db-8b71-3b25-8066-5c18d4cd4f5d | -3.08858 | -53.81141 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32da58a2-faf5-33de-b8db-ec9fb4043ac5 | -3.08799 | -53.81507 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91a91882-4804-35b3-87d8-33282937a010 | -3.0874 | -53.81873 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d613719-fd09-3d90-8790-1530d6463471 | -3.08682 | -53.82239 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a68fa9d-30f1-3f18-b3d9-c9379c6c0ce3 | -3.08099 | -53.8327 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8f17e6f-94d9-377b-affd-0a3862c8bf79 | -3.04161 | -53.79307 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79be3bcd-c86f-32c7-b011-73ec86fabf0f | -3.03754 | -53.79249 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95a74a31-91a1-3075-9102-80823e328d5b | -3.27325 | -54.14444 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf39bb25-2195-35cf-a95f-f0068124ec66 | -3.27317 | -54.1716 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31ee6f08-10fc-35b1-8fb5-63338bd1a294 | -3.26903 | -54.17087 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 917cd65d-6027-3733-9033-b29cff4739b5 | -3.26784 | -54.1783 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25f28225-2343-3036-80cf-97e77991ae75 | -3.2637 | -54.17762 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad960758-5f3e-30d7-89f3-e2cdf3caf683 | -3.25896 | -54.18061 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4e8e7ea-b491-3339-8798-b4b01d166dcd | -3.25542 | -54.17621 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fe3e989-5335-3863-adc2-99b40d1bc0f3 | -3.13667 | -54.26663 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 510cdd8e-eaa0-38a4-bec6-6beb74fc595b | -3.13607 | -54.27037 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ca9ac0f-1f2f-35c8-b3e5-045d1e3e2ecf | -3.13249 | -54.26591 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35481ac0-d348-3b37-937a-c1272837b300 | -3.1319 | -54.26965 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34e4d327-65a2-3ef6-b6e6-5853916c56ee | -3.13129 | -54.27341 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| adcca75f-3d46-36f6-ae4a-1c1097eef84b | -3.12832 | -54.2652 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0ce5b24-617d-3523-96e8-47205c917a0c | -3.12772 | -54.26894 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 64cd79be-8de9-3e98-8b8f-effe1dda1b77 | -3.12711 | -54.27271 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fcb9afb7-b108-3d7e-8544-330fc04cc48e | -3.1265 | -54.27651 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e767ebd5-114a-3613-9652-9ca859e77311 | -3.12589 | -54.28033 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3f560369-3fd5-3e4e-b5cc-1f5bcfb935f0 | -3.12415 | -54.26446 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0ce98d4-81f6-3e7d-aac6-77842c32693b | -3.12354 | -54.26823 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2b226d56-a54e-3419-b156-851d22f26124 | -3.12294 | -54.27201 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7b049006-04f2-3a6b-a1cf-592d4092aeec | -3.12232 | -54.27583 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 812a79ff-dbe7-397c-a2de-2a2c601b383b | -3.1217 | -54.27965 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 28515237-a153-37df-a66f-0b58d338dcb7 | -3.1169 | -54.28283 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1de5c7bc-1444-31a9-a48d-22443d5d7382 | -3.11628 | -54.28666 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e62c3af-c5cd-36da-a4f4-299fd337ba26 | -3.11469 | -54.24347 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 044a1ef7-c44c-3fb3-8675-72bc4e7424ff | -3.11333 | -54.27832 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40e7f80d-1d7c-326c-b006-78efbd7c2f00 | -3.11271 | -54.28216 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0365271e-a0ed-3cd7-a10d-06f77597d6cb | -3.11209 | -54.28601 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4ea25d6-1f1d-3d0f-ba47-d0b42df94081 | -3.10852 | -54.2815 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 59aa85b5-7cb9-32e7-a9a6-15c07b448997 | -3.1079 | -54.28535 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0a2375f6-a65d-3ba0-9f4d-b0daae5d2931 | -3.10559 | -54.27316 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5c3cfd37-e13d-3fc8-bc4e-8e825308ccce | -3.10496 | -54.27699 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4f014adf-2633-3b32-b361-45c7595ffdf4 | -3.10434 | -54.28084 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 4948603c-8d93-3d94-a3c2-cdea2f55867c | -3.10371 | -54.28468 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a8a8c740-0e8e-3e3e-9928-e336415e4c01 | -3.10015 | -54.28019 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f5067f26-2f59-3c6f-8e26-b1bcdb5b1c2d | -3.09952 | -54.28402 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 471d3929-78dd-34a3-8651-1a5e9430f167 | -3.0989 | -54.28786 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 714c969f-ecc5-3e22-a382-cc559db32f10 | -3.08005 | -54.16787 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03c5df01-5930-3d41-ae0d-ff403fc44b1a | -3.07589 | -54.1672 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5f308653-a9bb-328f-a3a3-7c20e6788ffe | -3.07528 | -54.17091 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a43a5371-4a65-3217-96e2-48996dd6a60b | -3.07174 | -54.16652 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bd76144e-6e40-3407-9dc0-2e88674e358c | -3.07112 | -54.17024 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1e6b8ec0-8be2-3a0c-a261-f73db37c9ce2 | -3.06984 | -54.16653 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| afdb7fca-d52c-359a-968b-1deec1af5c79 | -3.06925 | -54.17027 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 124544a9-e503-3b19-992e-792c039d945e | -3.0147 | -54.13837 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd6c1e19-0691-3a42-ba48-b0250fb8549c | -3.01055 | -54.1377 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 451a8ab2-f8d9-3a2f-a697-e2ac9d62be7c | -2.99343 | -54.53856 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a32780f4-c6f8-31d9-acf7-7338e5e1a753 | -2.9796 | -54.51566 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e38e0872-a5bc-37ce-9a1b-127aa9400ea8 | -2.97533 | -54.51506 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c11244f8-6a2d-34ad-9401-0eba77c3ebf5 | -2.97468 | -54.51907 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e62b1305-5c7f-365c-bfe2-16384bc5d87f | -2.97104 | -54.5145 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1798e327-38d1-3621-80a5-767b9b125700 | -2.9704 | -54.51848 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c6fe822-ed64-302b-9d23-874257496de4 | -2.95781 | -53.87069 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8fbad774-8db6-3fff-995b-5b4be5b60d6b | -2.95098 | -54.1239 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b02df67d-a121-3da3-8916-8195c80163ea | -2.94349 | -53.7028 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66d19442-74bf-3782-9a65-fba836d29a54 | -2.94291 | -53.70635 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc88442b-827a-3931-bfba-501719dc5999 | -2.93829 | -53.70925 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a30cb129-c59f-3390-9ba0-24b39f1a224a | -2.93777 | -54.18002 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README54.md)
