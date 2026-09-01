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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e7699b9-81f3-33d6-aaa4-4bd0edee5e7e | -6.72505 | -50.4642 | 2026-09-01 05:36:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d80abc93-2a28-3ef1-a939-478c0008f395 | -7.30143 | -60.56704 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6fb33e3-585d-3949-8b20-29c17c9daa80 | -9.20729 | -59.40923 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1cad6fc-ef0f-3e75-9e91-87fea72aa9be | -9.06597 | -60.48759 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a6f3954-3ccf-3f18-b22c-635f8d24de17 | -9.03084 | -65.44471 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f705481-ea6b-3f71-8af9-26d669e0b44d | -8.50387 | -55.31641 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9057818e-669f-33d7-9310-cbdc579045fc | -7.58396 | -61.34189 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2591dba8-1608-34f6-89a5-0b5249d89bdd | -7.29627 | -60.5777 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c894816b-3433-304c-9898-cf887ab90194 | -7.58736 | -60.48307 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9430017-1e72-399b-b26c-aae47bc0c47d | -6.80713 | -59.57549 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6e65ad8-1ec6-3383-aef8-c7b68070a639 | -6.09043 | -57.72137 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9519eaa-9f5c-3676-a94e-4acc456006be | -7.35786 | -60.58702 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9da082a2-f3d9-3cd8-b2ca-ec374836ca3c | -9.39234 | -60.57443 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa16e930-f89b-3e07-8094-35d1c3214452 | -7.5292 | -61.38457 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24461594-6506-3aed-84cc-28415a9f9efa | -7.09454 | -63.04657 | 2026-09-01 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5f1e9c5-a00c-3c17-b142-cf356be0d4da | -11.25997 | -50.58309 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 52dd2963-73ed-36d0-9022-b52d20232d1e | -5.95194 | -57.68282 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9a28833-1b40-358d-bfb3-5bc7aaf2b2d6 | -7.02042 | -59.64733 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d78d5ec4-08c9-3fb9-acee-de84d5e5bf22 | -9.89211 | -60.27629 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11717e45-b36e-309b-b7f9-c2a77865526f | -7.02598 | -59.56153 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d0ce670-2884-39b1-8594-adb2dcc30c04 | -8.71163 | -52.36959 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf12ed15-26d7-3873-92d0-d97e486596dc | -7.57703 | -60.48141 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f824045-1f39-3678-9be0-5be7216c743a | -7.29221 | -56.68244 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4eed450-103e-320a-9a2b-1b761a55b930 | -8.13747 | -54.9669 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ddc525a-5c5e-3187-bae9-51f3704bfc19 | -9.85607 | -64.97862 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87d36b83-f6ff-3be7-abdd-531a285c1323 | -8.96866 | -71.25901 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14142a3d-2f33-33d9-af1b-35f77009fd20 | -7.363 | -60.59922 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7e9a2eb-6414-35b8-beb5-b5479f1cfb86 | -9.45537 | -67.45687 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce5373ab-c2c6-34b4-948c-70e7579b3d6a | -7.62335 | -55.29085 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f1e90de-724d-3807-9e44-12bc212b437e | -5.48615 | -57.15512 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbc9243a-e337-3d70-bab0-d6e0ec6b63d3 | -7.03562 | -59.21675 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9da0532d-453f-3f06-836d-82d20eba4681 | -10.94976 | -61.66043 | 2026-09-01 05:36:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| db7d5b8b-c37f-3b5d-81a1-e0b862f32e74 | -8.27953 | -54.92913 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03efad38-dd2b-3105-9a4e-410712f7c618 | -6.80436 | -59.45572 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77a4c9b9-9756-34b2-828f-f2ec0a98f690 | -5.48264 | -57.15107 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad5851f2-1f2c-3257-88c1-cf068eeccf13 | -7.0319 | -59.57074 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32f62959-0216-33ae-97aa-0e2aa629bb18 | -7.52695 | -61.3769 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e0f4d75-81bd-35fc-a362-e420acbf6396 | -7.18902 | -60.68284 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b39037db-d343-38bc-adf0-0d024efcc3e0 | -6.61082 | -58.59696 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5247262c-393b-3566-a2f3-c93a0bf6aff1 | -6.10913 | -57.8665 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f8f837e-2deb-3710-8fb7-40bf4de1a462 | -7.35158 | -60.58221 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 96dbc339-4836-3c7c-9345-d513b7ec6d27 | -8.79206 | -62.4954 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bd1009f-632f-346c-a249-ef71f85b2c4c | -10.21178 | -50.31434 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bfecd19f-5e72-3695-8eed-83a9d9944ae1 | -11.25686 | -50.57871 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2505d4f5-951c-324d-9cd9-54a2b8a27b1a | -6.59826 | -58.6042 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bfb5332-63c0-3db5-82a5-9d9a42686f09 | -11.27169 | -50.56829 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0ed6002-188a-3281-b57a-cd4928a75cdc | -8.93706 | -62.37163 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2092caf2-7527-345f-a409-092e962306f0 | -7.53255 | -61.3851 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61bf1042-2973-385e-9ff6-d34981a8033a | -8.5063 | -55.30336 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d473e607-a029-3db0-8966-48f97649eeae | -9.13881 | -61.09446 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae534a38-f605-3bf0-852a-4ecd4d0d2a92 | -10.41517 | -64.45786 | 2026-09-01 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 39d6ce88-80c6-30b2-873c-2045fdc8cc38 | -9.08161 | -65.48552 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a2339b4-2b91-36ff-b793-6d3acc2e3f70 | -8.71205 | -52.36633 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62f014fa-d1a1-38c0-8d70-172f6dcf86d9 | -5.58384 | -60.23706 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 316abbb2-716f-3706-a62a-9c4f186229be | -7.45833 | -59.93072 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9dbb2e6-73f5-35a6-9ec7-996d87e5db3c | -7.03733 | -59.22988 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce60e55a-33db-3012-9b70-0868099746e0 | -7.02938 | -55.64717 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc890a04-5c62-3454-aab4-f18e63fb6b7f | -9.91395 | -67.01275 | 2026-09-01 05:36:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d240dd6-ffcb-30ec-8e00-65aafab8cba7 | -9.0352 | -65.39719 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 723e8a75-491c-311b-99a2-2b41f2e4b24b | -6.90511 | -59.48273 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16e6d526-6b45-3d5a-b64d-cc1adf14a87a | -10.36128 | -50.01361 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 93ea66b3-b6a8-31ff-93d9-371cb0a02ff7 | -9.4571 | -67.45473 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 35f37869-396f-3b9f-87fa-99650a5ef9d8 | -6.81072 | -59.09849 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6b650d0a-9db4-3202-9064-3cba467bbcba | -7.18366 | -55.48225 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a30b7f2b-e649-3233-b9dd-af86702ee8fc | -7.58851 | -60.47558 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| de3c7cd1-9ae1-33d4-81f4-cefa8a176d97 | -6.94238 | -55.6319 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3fcf96b-58ea-3d8f-935f-b0d831217616 | -10.21104 | -50.32039 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4e51089c-ad5b-384f-96f2-78806e73700e | -7.68988 | -55.34398 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 821607f1-2b26-3f0b-acc1-86eacdd76325 | -7.57893 | -61.35209 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 821a3adf-317d-3180-8644-092b46c93a9e | -7.34413 | -55.19103 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49b7f0dd-a4e6-3a4f-a7e2-0fded1e2f919 | -6.15792 | -57.77888 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22ad7989-0c3c-3a35-94ad-7d9d8cb35058 | -10.74802 | -54.06565 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edcccb49-b05f-38ed-9f67-46603077128b | -6.94761 | -55.62794 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f373b3ac-4ed6-3337-8ec0-c94d5bf96272 | -9.15336 | -59.54338 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd6ee45f-6bd8-3015-8fbe-1e110887ee2c | -6.69429 | -55.40565 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4807385e-73b2-36a0-b56b-5ae61fd3d4b8 | -8.45549 | -70.72254 | 2026-09-01 05:36:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3674d456-2994-39cc-93cc-5bd0de4a47e0 | -11.06709 | -51.52811 | 2026-09-01 05:36:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 109dc83d-caa2-3915-973e-57f56830d7dd | -8.80801 | -71.29141 | 2026-09-01 05:36:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a3d83096-194f-3685-b5b6-dd2eaedf3354 | -8.13358 | -54.96912 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 63e70998-9b95-391d-bfb5-8bfe6e589720 | -8.79039 | -62.48441 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4f16ebb-8500-3b93-9b8d-da11f9cab1bd | -7.55775 | -61.42187 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a94961e2-fac9-341d-92e2-c7e9e2e235cc | -10.3412 | -50.00437 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6990fdbe-2b30-39fc-bdeb-37a7e21eddcc | -7.03498 | -59.22096 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b9a1f33-9e0d-37d9-aba1-4880006039f1 | -9.62008 | -68.60075 | 2026-09-01 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 430b1d51-7257-3283-9840-15f44ea4a339 | -8.95866 | -62.40731 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdfd8a5e-e516-31a4-bf99-5438c0b0d7d4 | -6.91863 | -55.69915 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fd86000-9b76-3d65-b18c-cd26de9aaf45 | -9.32129 | -68.89059 | 2026-09-01 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad3d05b5-95d8-3608-98b3-ec61c9430619 | -7.56669 | -60.47978 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a60e76e0-464a-3ca0-9cc2-c3e20a5bd915 | -9.46805 | -57.02101 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 905fb530-8bc4-3f2d-afd9-64c5c867d578 | -6.81137 | -59.0942 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 307d9463-80f5-3df9-906a-c69f6d58b2ae | -5.96143 | -57.6995 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b001ea1-835f-3ba3-986c-7a92768cc1ae | -8.80036 | -62.50744 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1387f9f8-e13a-3dac-a5cf-4a9beb9e704b | -8.62648 | -54.8562 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 366b905e-b44c-3753-b4ca-cade05bee95e | -9.94112 | -53.99545 | 2026-09-01 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65fb4969-be0f-3731-bc6c-cd8c04cb0338 | -6.16184 | -57.77936 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7458c0b6-8363-3f3a-9cfa-940f4b2d6093 | -9.14733 | -59.53364 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f349bffe-5f84-3054-b369-3f4a2fdc5ada | -8.50461 | -55.31126 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbd59cb2-5709-3e99-b309-056cdf9a4d95 | -7.5778 | -61.33727 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be00f621-7d91-355b-8774-0faffa198663 | -10.06612 | -59.40851 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a76e7637-e346-3a86-83a7-a589c53c53f2 | -10.83408 | -50.71046 | 2026-09-01 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README84.md)
