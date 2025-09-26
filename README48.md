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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0a21773-420c-37e2-90c3-fecc8eff2ecb | -15.53333 | -44.33021 | 2025-09-26 05:23:00 | AQUA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 253d9ba6-90e3-3b98-9579-e021dd25d00a | -15.2618 | -46.42853 | 2025-09-26 05:23:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| acded781-cf87-3c88-8cfe-432259327c7b | -20.42319 | -43.36208 | 2025-09-26 05:25:00 | AQUA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.7 |
| b99e28c0-db6f-3102-b98b-c3cd3904a300 | -20.42513 | -43.35058 | 2025-09-26 05:25:00 | AQUA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 4d104836-8578-3359-998a-0a144ca2a8b0 | 1.0053 | -59.51088 | 2025-09-26 05:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 540aa796-2a11-3637-b3de-242b24d3705a | 1.00677 | -59.5098 | 2025-09-26 05:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 73fd3b49-085f-3150-b4e6-77368db4ad82 | 3.91084 | -60.23744 | 2025-09-26 05:53:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 180c591c-9966-36bb-b451-9b0517720465 | 4.26916 | -60.98442 | 2025-09-26 05:53:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92e3090c-0fed-3c16-ba05-81460216ad70 | 4.49803 | -60.11474 | 2025-09-26 05:53:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4be5de7-100d-3f5e-bb1d-2d86d787aec2 | 3.91018 | -60.23333 | 2025-09-26 05:53:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5655cc0b-b741-3319-aade-2450822e54ac | -2.69261 | -54.94838 | 2025-09-26 05:55:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df4135f8-6f93-3db1-af9c-5a7b88087345 | -2.69933 | -54.94944 | 2025-09-26 05:55:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbb39127-697e-38d4-bc78-8e3cf1b16bc9 | -15.72514 | -59.49157 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc0351c3-b497-37ef-84f6-4d7d1ed95cf5 | -15.90681 | -57.48778 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af30bf0a-4234-3cb5-b15d-779461b19d03 | -15.98913 | -59.48336 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e72228ef-c4c7-303c-94f6-9e96887a4642 | -15.73282 | -59.50192 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da7c403a-f979-3564-8f77-c02391a2e6d3 | -16.00894 | -59.48784 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdde22ad-63fd-3c9c-9808-64f7285e22d1 | -15.97639 | -59.48856 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9bb6fe8c-1404-3a72-b80f-ec05f41613ab | -15.92177 | -57.49817 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49a3796d-d49d-3db3-988e-9bd45aa4098d | -15.92222 | -57.4934 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c9a7188-c0f5-3daa-a6e6-690d33eefc31 | -15.88025 | -59.33407 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a48cdf8a-3358-3dcc-8589-6eb4fdd1da68 | -15.74742 | -59.47825 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a4053ff-e5b8-3f5b-a821-d66dd90eef99 | -15.91263 | -57.49829 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 896c2aa1-a321-3e6d-8d3d-67d94e7995c3 | -15.72772 | -59.4924 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 469fca2e-ae89-3896-82fb-41b7a30f0ba2 | -15.90828 | -57.4958 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78a9d6b4-4ee5-3413-990a-7f3e4848084e | -18.29419 | -57.10108 | 2025-09-26 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4b5a67cd-d2d8-3de9-9b6e-7664a0c08b17 | -15.73327 | -59.49756 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| faeaf134-52b2-3548-a2f5-f66082b0caac | -15.93939 | -59.49282 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95075d84-8d53-3847-bb17-764aa5a212d1 | -16.00061 | -59.49018 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61613833-f501-3c07-b3eb-db0295cc01bc | -15.91501 | -57.49711 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cdb2cef3-e76b-342d-9323-c2a0504a5ba9 | -15.74704 | -59.48189 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b491537-94c6-3fe0-8e0b-eaff695dda91 | -15.99427 | -59.49251 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a5e1eb2f-5e0b-36b4-b5fc-905d0af5d204 | -15.90869 | -57.49135 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8f6e9c2-e558-322c-9fbd-e7d3db6fd02a | -15.93896 | -59.49709 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81266682-2634-38e6-aed2-d9223e7284d3 | -15.92903 | -57.4938 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0f6d96a-2d5b-3564-b144-9219d54c5c7c | -15.91309 | -57.49373 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 510f9045-9a95-37f7-a471-310daf90b1d7 | -15.90914 | -57.48656 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 29659516-6a13-3b77-b3dc-9632239acfd7 | -16.00028 | -59.49336 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c0da1a2-faf4-3bdb-9750-0ff92eeb1a9e | -15.99389 | -59.49609 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa9253e2-4804-3260-9981-3f4fb48226e3 | -15.91937 | -57.49943 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6dfaa2a2-8cfa-33b7-ae1a-8f53c1ba2c66 | -15.92665 | -57.49525 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 988d1380-394c-3d97-823b-e026ea83822b | -15.89235 | -59.33596 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f4d0a70-a377-34fd-807c-004e57f9bf15 | -15.72727 | -59.49683 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f3ac220-857a-3ec1-aef4-d1a37b24ed9f | -15.92613 | -57.50043 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a8ecd9c9-1943-3b56-97ad-2bb00bed881b | -15.98878 | -59.48671 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3769cdee-9a97-39e3-bcc4-f882352da7d6 | -18.3007 | -57.10901 | 2025-09-26 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 7574810b-513d-3e2a-9460-f30714c3fc11 | -15.88625 | -59.33552 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ea46c1f-15b1-3533-8ee3-b41c13191342 | -15.89843 | -59.33654 | 2025-09-26 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 355dd92d-49e5-33e0-afe8-cfdcbd3de1ca | -18.30128 | -57.10186 | 2025-09-26 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 476fb19f-a593-34eb-aa6c-b4e8519c2cd2 | -15.91985 | -57.49469 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5ac57f1-82fe-3bc9-9b15-4fd3524b7984 | -15.92855 | -57.499 | 2025-09-26 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c887609-dd46-352f-b73b-98895c62dbb0 | -2.69538 | -54.94852 | 2025-09-26 06:57:00 | AQUA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 91d79d13-e968-3a28-8a6f-aabc6680fce5 | -15.92514 | -57.49643 | 2025-09-26 06:59:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| cde7c804-d248-3b3e-b9e5-71414a21c3b5 | -17.17067 | -56.36378 | 2025-09-26 06:59:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| 5e070592-d938-3d72-a4b2-2f9cd4838611 | -15.92467 | -57.48974 | 2025-09-26 06:59:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f4d80ee5-625a-3df0-a12d-1e2aea88ae79 | -15.91209 | -57.48801 | 2025-09-26 06:59:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 10dedfeb-abb8-3e88-9713-20479d7b4c1c | -15.72772 | -59.49742 | 2025-09-26 06:59:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| dba2411e-2fe7-3c96-ae7c-3d1213344c76 | -15.93343 | -59.49509 | 2025-09-26 06:59:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 28df2c8b-5584-3389-9f8c-4f128452ae30 | -17.18073 | -56.3574 | 2025-09-26 06:59:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.0 |
| 00223d38-cebb-36fd-9147-cba60067fc06 | -17.17341 | -56.33838 | 2025-09-26 06:59:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 0b869d5f-ed39-3eec-8382-961c992aec41 | -15.608 | -46.4549 | 2025-09-26 09:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f9f8adc3-7c6c-348e-a8ca-442517dd46cc | -15.5883 | -46.4585 | 2025-09-26 09:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 77caf32e-0767-390a-9ac1-b0cb87d1b836 | -15.5883 | -46.4585 | 2025-09-26 10:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 102.5 |
| bc7ae3db-2146-3627-a03d-dc34000ddf2d | -12.5568 | -45.8459 | 2025-09-26 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 695a43fe-166a-31aa-a7ad-41e2b8044e2f | -12.5568 | -45.8459 | 2025-09-26 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| bd10ddb8-78cd-39bc-a1c5-aedde3606c3a | -12.5568 | -45.8459 | 2025-09-26 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 80324a34-4e47-3397-b033-508ae5dd07a5 | -12.5568 | -45.8459 | 2025-09-26 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| d44d7ff6-5c3e-3b31-80b6-40a32800a1a6 | -12.5761 | -45.843 | 2025-09-26 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 37fe6bf5-c108-322e-b396-a414c6ebdea7 | -12.5761 | -45.843 | 2025-09-26 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| a5c81371-5887-3a85-b5ee-44b03211df3d | -12.5568 | -45.8459 | 2025-09-26 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| e1b14475-4c89-3588-8dad-e69c9aff4110 | -11.4225 | -44.9794 | 2025-09-26 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 433f3014-1370-3c62-aa9f-f6b41a87afe0 | -11.4221 | -45.0025 | 2025-09-26 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 65143ed5-76b2-37bd-9b82-be5987efa576 | -9.9873 | -46.7103 | 2025-09-26 11:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 89a941e4-d474-3a74-949c-a3d85d63dd83 | -11.4221 | -45.0025 | 2025-09-26 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| ff313047-803d-30d3-a56d-eaebfa8b8964 | -12.5568 | -45.8459 | 2025-09-26 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 051a530e-e922-3ab0-8f63-8fc2a1f7e20e | -11.6233 | -44.4398 | 2025-09-26 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 9289bb7a-83a2-31e2-a487-41aa2adeb48d | -11.4225 | -44.9794 | 2025-09-26 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 96156772-bb6c-309f-a8d8-c679e9e63636 | -7.64631 | -40.34003 | 2025-09-26 11:57:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 10.1 |
| a376297a-a982-3ec2-a3cc-1bd556dfd08e | -5.46626 | -43.07092 | 2025-09-26 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 726659ff-fe28-391f-a85a-860c5dbe982f | -7.05915 | -43.02893 | 2025-09-26 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 15ae806a-8ce3-3720-be0d-2ccfbe6a291a | -2.95256 | -40.87511 | 2025-09-26 11:57:00 | TERRA_M-M | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 983b8c8d-2a8a-347c-b8b1-fe9afe3d2bc5 | -6.25262 | -42.48324 | 2025-09-26 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0e736b5f-a858-3bcc-96d1-0820c63d03f5 | -7.88007 | -45.28643 | 2025-09-26 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 61b7bd1a-6fd5-3fe5-8706-3e2cbd3efb1f | -8.13079 | -42.37534 | 2025-09-26 11:57:00 | TERRA_M-M | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a78434fe-5c18-367c-b745-a2f44c34cb15 | -8.39889 | -39.77094 | 2025-09-26 11:57:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 42750d09-7b7c-3782-b191-bf27c3bb9c61 | -5.98957 | -44.1555 | 2025-09-26 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| acefb309-f0f5-3b76-beda-7f64c141d4f3 | -7.6836 | -45.98552 | 2025-09-26 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1823dd72-3691-3563-8a8a-4616052b87cb | -5.30861 | -43.14094 | 2025-09-26 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ce0da3f4-e536-37c8-bc5b-3604a77fa096 | -4.40154 | -41.57683 | 2025-09-26 11:57:00 | TERRA_M-M | LAGOA DE SÃO FRANCISCO | PIAUÍ | Brasil | 2205573 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0cd132b5-169a-30d2-8f2d-67a123264ee3 | -7.76958 | -44.72142 | 2025-09-26 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 36c00278-0053-3989-ad9f-b5f3551b022d | -6.79978 | -45.52341 | 2025-09-26 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f2310ca7-d68b-3c06-b277-b19d8112881d | -5.74454 | -44.97862 | 2025-09-26 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 7dc538aa-a3ae-3fa6-8ad9-fdf3cac34ffc | -5.73629 | -44.96555 | 2025-09-26 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| e0e944ef-66b2-34c2-9d69-b5c58489882a | -6.57517 | -45.1092 | 2025-09-26 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 182.6 |
| f52b9a91-da93-3e6c-932f-bb20e12dd4de | -4.16085 | -40.99821 | 2025-09-26 11:57:00 | TERRA_M-M | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 7c44c454-7b1b-3b4b-97e6-a57e770a0b11 | -3.35689 | -44.79039 | 2025-09-26 11:57:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| b25a617d-93a3-34f9-867a-492fba1d5d0d | -5.76858 | -42.89703 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 276b8ea3-dba0-3d4d-8947-7290af6c2140 | -3.45577 | -44.11914 | 2025-09-26 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 42cd0f68-f2bd-3715-8eee-d4731a48c1f7 | -4.35722 | -43.02039 | 2025-09-26 11:57:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| def70999-dec3-3f02-8998-fb575ec1b41d | -8.77181 | -43.04493 | 2025-09-26 11:57:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |


[Clique aqui para ver as próximas entradas](README49.md)
