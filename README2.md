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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d35c4e1d-f917-3bee-bcd1-8f8131522277 | -3.2147 | -50.7884 | 2024-10-21 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 707ec56d-4603-37d5-bfa3-3c461dd6f4f5 | -3.2585 | -53.78 | 2024-10-21 00:15:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 933aa00e-22cd-3f54-b3b9-4fab562b2cc7 | -4.0899 | -46.1493 | 2024-10-21 00:15:29 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 33129075-327b-3826-bc92-aaabc2508619 | -4.4414 | -46.4425 | 2024-10-21 00:15:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 103.7 |
| a818f1ed-11df-3551-8be2-3bd024978971 | -4.8291 | -46.8857 | 2024-10-21 00:15:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 0b2abbbc-e6b9-3c32-8b3e-5bbceaad6537 | -4.8477 | -46.8847 | 2024-10-21 00:15:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 137.4 |
| f4c3f208-d427-3335-8066-6650dee34640 | -4.8924 | -45.8386 | 2024-10-21 00:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 026eebab-1dde-3761-a622-8122b03cb63b | -4.911 | -45.8374 | 2024-10-21 00:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d22f2b3c-488e-3dd3-a52a-9994b9dfeb1e | -5.4904 | -50.5882 | 2024-10-21 00:15:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 141d0bc4-36e1-3cd1-a3a0-b4e4a65ec647 | -5.6894 | -46.435 | 2024-10-21 00:15:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 175.5 |
| ff4e41f8-2340-37ce-a7fc-2fef9271fd17 | -5.6896 | -46.4128 | 2024-10-21 00:15:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 52761b11-e5b2-30e7-b8ed-ee8c4fb72a23 | -9.7704 | -64.7174 | 2024-10-21 00:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 1e8332ba-cf1a-3249-8468-34f9db50d777 | -12.5147 | -63.3014 | 2024-10-21 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2aa62271-e4b6-340e-a627-ee9cbb18d351 | -12.5168 | -63.0329 | 2024-10-21 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d1f51cf2-d111-3319-aa4d-a0210bb619f0 | -17.7065 | -57.4569 | 2024-10-21 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 0d47ce44-6bd8-3635-8014-5ed01ebb8af3 | -17.7259 | -57.4751 | 2024-10-21 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| b438a5ba-0e72-3b78-9a25-f6554782c771 | -18.263 | -56.1021 | 2024-10-21 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 2a0e6aa9-daee-3fbd-9ace-8a6323686efd | -18.2828 | -56.0994 | 2024-10-21 00:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.6 |
| 6e0c2c17-c2ad-3d1d-be8f-28f81d9f385c | -18.2832 | -56.0785 | 2024-10-21 00:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| c9b9dfb8-9d12-356e-8b6e-91d6c8e4c77f | -19.5477 | -56.6353 | 2024-10-21 00:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 1c148b6e-95f5-311a-b9ae-772938b687a1 | 1.0212 | -51.1654 | 2024-10-21 00:25:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 80.8 |
| d9ed24e1-467b-3989-bbaf-507a7fe49124 | -1.1834 | -53.6368 | 2024-10-21 00:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 3250763a-4696-3a40-b8e7-cbbd69d34ae1 | -1.1835 | -53.6166 | 2024-10-21 00:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 09283168-8a48-3750-81d4-f03264fccb62 | -1.2018 | -53.6366 | 2024-10-21 00:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 151915a5-823c-3136-89b1-e67461bcdd03 | -1.2018 | -53.6164 | 2024-10-21 00:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 24b38afc-0765-3c32-be11-4c2b835d523d | -1.9395 | -52.1016 | 2024-10-21 00:25:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| cbfe1a87-58e0-3a52-9353-41f010b71f6d | -2.2199 | -50.4594 | 2024-10-21 00:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 4c926deb-b300-3ae7-9dfa-d91d49766bc4 | -2.2671 | -47.0775 | 2024-10-21 00:25:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 42bfc8ae-7c35-368c-9dbb-2c597ba3f050 | -2.464 | -49.1024 | 2024-10-21 00:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f388503a-99eb-3a5d-93de-7483e602fb34 | -2.4824 | -49.1233 | 2024-10-21 00:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e94d1dae-904f-3d72-a12f-0abf348b20b4 | -2.4824 | -49.102 | 2024-10-21 00:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| a4764a13-c030-3975-a127-bed24d34482b | -2.7885 | -51.3618 | 2024-10-21 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ad8c989c-6db2-3947-9dd9-a76ba80e777d | -2.8097 | -45.7786 | 2024-10-21 00:25:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 1e9ac8d1-6e97-3ecc-9f2e-4d9a2885e73c | -2.8069 | -51.3613 | 2024-10-21 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| c703aad5-cce6-33aa-9e56-d842b54da338 | -2.8482 | -45.4637 | 2024-10-21 00:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a81fac0f-39dc-3574-8c38-ca814753cf8b | -2.8372 | -53.3261 | 2024-10-21 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 17bd2c89-e799-3940-9e2c-c43f7b46f49c | -2.8667 | -45.4855 | 2024-10-21 00:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 614489f9-a888-3fd1-8d64-65abc06d13de | -2.8668 | -45.4631 | 2024-10-21 00:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 8daf42ac-e97f-3085-9901-d6a9f403c92f | -2.8864 | -45.215 | 2024-10-21 00:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 6e0487ca-300c-3b29-b9c4-3ffaad139add | -2.8865 | -45.1924 | 2024-10-21 00:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 3a0c20d3-cdf7-3119-9b74-7d69867c6890 | -2.905 | -45.2143 | 2024-10-21 00:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 221ce5fc-32d7-358a-b1f8-b8708dca6315 | -2.9051 | -45.1918 | 2024-10-21 00:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 0097bb23-5304-3396-860c-b2c9eb4e0d8c | -2.9674 | -47.9931 | 2024-10-21 00:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a2d12ad3-0e18-3666-9e13-2f69d76c8d13 | -2.9852 | -53.0587 | 2024-10-21 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 57c2afa7-4e8f-3279-a85d-05f6f421f9a1 | -2.9853 | -53.0384 | 2024-10-21 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ae48c57d-bb08-3f7c-ad6e-ddaf212f9c76 | -3.0036 | -53.0583 | 2024-10-21 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 0e616a5b-2caa-325f-8990-4e976f4f0bc0 | -3.0037 | -53.038 | 2024-10-21 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 49fe23fa-bd8e-33d7-8ca0-3a5b3c437148 | -3.0176 | -54.3489 | 2024-10-21 00:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 69b45bd2-d59b-35a0-85dc-f57d6fd31969 | -3.0581 | -53.2395 | 2024-10-21 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6c96c63b-e020-3b5f-95ee-aa30e896de5c | -3.1962 | -50.8099 | 2024-10-21 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 27a0a93d-8943-3705-8f21-3db81fa2caca | -3.1138 | -53.1163 | 2024-10-21 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| bbd56f9d-3213-32f3-a542-e4946a92d7c8 | -3.1963 | -50.789 | 2024-10-21 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 27c11457-7e60-312d-b1d5-68997e925f3a | -3.2146 | -50.8093 | 2024-10-21 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| cbc3b671-98fb-3231-aead-c585fea846b4 | -3.2147 | -50.7884 | 2024-10-21 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 7e115d75-201a-3e71-b7f3-23e19d371776 | -3.2585 | -53.78 | 2024-10-21 00:25:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a0181ca2-1fb3-3413-9e13-9187966a46d1 | -3.7984 | -52.3204 | 2024-10-21 00:25:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 1f115865-3b26-3f03-8123-8efa0f464203 | -4.1085 | -46.1484 | 2024-10-21 00:25:29 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 97a950a9-37aa-3da6-9c88-4e131b0a6e69 | -4.4414 | -46.4425 | 2024-10-21 00:25:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d3f71943-9c1e-368c-b183-0d26f7619542 | -4.46 | -46.4416 | 2024-10-21 00:25:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 0ba6250e-644f-30ee-bb06-15d23230de09 | -4.8291 | -46.8857 | 2024-10-21 00:25:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1fc177aa-be07-3294-901e-785ebe52280f | -4.8474 | -44.3472 | 2024-10-21 00:25:33 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 56500fe3-143f-31d9-9165-0c04f3ff08b7 | -4.8477 | -46.8847 | 2024-10-21 00:25:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0cc5bc62-46c2-3981-bbca-0eb224fd4121 | -5.509 | -50.5872 | 2024-10-21 00:25:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c071a909-1f43-345c-b64c-770f54843c60 | -5.6707 | -46.4363 | 2024-10-21 00:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1d76227b-dfdb-3218-9358-258489c6d8f1 | -5.6709 | -46.414 | 2024-10-21 00:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 5c2ae197-64ae-30a6-88be-33803522f128 | -5.6894 | -46.435 | 2024-10-21 00:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| bcf98ca5-8f70-3d78-80dc-ae0f11e98737 | -5.6896 | -46.4128 | 2024-10-21 00:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| ea6f5b3a-a287-3884-93c1-4dedf67d032c | -5.7081 | -46.4338 | 2024-10-21 00:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| bd7b3339-8233-3391-953f-16ff34595cd0 | -5.7083 | -46.4115 | 2024-10-21 00:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| cf20a309-86d1-32a5-9645-580a3b4d93fc | -9.7704 | -64.7174 | 2024-10-21 00:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 34ce332e-266e-3e48-88e0-594a11d1a1bd | -12.4778 | -63.1885 | 2024-10-21 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6234ee53-df52-3ee0-94e9-573859cf7694 | -12.5147 | -63.3014 | 2024-10-21 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1e2649db-2f8d-3a2a-af5c-4c3451d632ea | -17.765 | -57.4909 | 2024-10-21 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| c0723833-2b81-3e4a-9fe8-dfc481ca96c2 | -17.7654 | -57.4703 | 2024-10-21 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| ace0e3bd-02aa-3611-b38b-fa6d2a770e08 | -17.7848 | -57.4885 | 2024-10-21 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.0 |
| 18fba032-b035-3e98-9201-c41fe14c1357 | -17.7851 | -57.4679 | 2024-10-21 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.8 |
| 23ea4199-3c39-3f48-9981-677aeb07b801 | -17.8045 | -57.4861 | 2024-10-21 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 249.1 |
| 6048755b-83e0-3e39-9d5b-ff394ce2f35b | -17.8049 | -57.4655 | 2024-10-21 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 175.9 |
| 22a8d4a9-24a7-39b5-8ecd-d2dc05ad9029 | -18.263 | -56.1021 | 2024-10-21 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| ea3f85a8-e3cc-3c74-8664-d9c94f003b1c | -18.2828 | -56.0994 | 2024-10-21 00:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.7 |
| 145d3640-1eeb-343f-9ad2-81127a3f7caf | -18.2832 | -56.0785 | 2024-10-21 00:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| ff959f54-4865-3931-9a2c-3d918c77dc73 | 1.0028 | -51.1656 | 2024-10-21 00:35:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 65.0 |
| efd69f83-31d2-371d-ad0e-2ca0bfd92c9c | -1.1834 | -53.6368 | 2024-10-21 00:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| f1193e5e-c214-3b78-8a97-4a554e3627e7 | -1.2018 | -53.6366 | 2024-10-21 00:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| c7d06725-0503-3c7a-91e4-c99bf4a1d894 | -18.250999 | -56.063099 | 2024-10-21 00:35:14 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 18f2448d-edd3-305d-bbc9-aa582cd42302 | -18.261801 | -56.125999 | 2024-10-21 00:35:14 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dc582eef-7f9b-39eb-af1e-ac04dab01a9b | -18.237801 | -56.043999 | 2024-10-21 00:35:14 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 31b5b5bd-63eb-3254-89a7-099bc5500138 | -18.241301 | -56.0648 | 2024-10-21 00:35:14 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d84a6cac-9d14-39ec-9e90-f6b00eff1b2a | -18.2316 | -56.066601 | 2024-10-21 00:35:14 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 661111a8-853b-3ef2-a3b3-4f0b7f50f856 | -18.2449 | -56.085701 | 2024-10-21 00:35:14 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1ab71ea5-ed4c-33e2-b502-6581bebb16cb | -18.2521 | -56.127701 | 2024-10-21 00:35:14 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eecc4557-66b8-348f-9e96-dc07b353785c | -18.2281 | -56.045799 | 2024-10-21 00:35:14 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| abea6801-d0a4-37a4-88c2-4e0a84bfeb2e | -1.9395 | -52.1016 | 2024-10-21 00:35:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| abdbe907-af16-3b25-ad85-368ef67dbac1 | -2.2199 | -50.4594 | 2024-10-21 00:35:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| dc502291-00a2-392c-ad12-a5ebbbcf088f | -2.2671 | -47.0775 | 2024-10-21 00:35:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 996d18a6-f173-3e19-a422-07f35099ebfa | -2.464 | -49.1024 | 2024-10-21 00:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 687d0f62-85a9-3933-a3a9-77027f5f4786 | -2.4824 | -49.1233 | 2024-10-21 00:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 311a9260-2511-3608-83d8-731d6664382e | -2.4824 | -49.102 | 2024-10-21 00:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 1278823c-5987-356f-ab0b-597eb5635ca5 | -2.8864 | -45.215 | 2024-10-21 00:35:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 55ea69f6-60cc-3c85-833e-c70480fb80bd | -2.7885 | -51.3618 | 2024-10-21 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |


[Clique aqui para ver as próximas entradas](README3.md)
