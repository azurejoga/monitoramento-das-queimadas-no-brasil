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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e47bd1e1-4c1c-300b-a100-1475b45a11e9 | -15.1939 | -49.4083 | 2024-10-09 02:46:31 | GOES-16 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 589ee837-4d9b-374f-8560-dcd7ba663493 | -15.1943 | -49.3862 | 2024-10-09 02:46:31 | GOES-16 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 25fbafdd-e62c-336f-bf36-50fba698894b | -15.6791 | -52.5206 | 2024-10-09 02:46:34 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 00b744c6-b56f-32e1-b733-92d5a6dc27c9 | -16.4184 | -55.9455 | 2024-10-09 02:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| ae2084b2-ba96-372f-85f7-f84d70da20cc | -16.4187 | -55.9248 | 2024-10-09 02:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 19e5ac16-9791-36ac-a9ac-c0d2a21ab5e8 | -16.8898 | -55.8039 | 2024-10-09 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 175.9 |
| 8236131c-8e4a-3047-8b8a-a76d10e4727c | -16.8901 | -55.7831 | 2024-10-09 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 137.5 |
| a762ca64-7b5d-3a90-8cce-ae7da3e2087b | -16.9091 | -55.8222 | 2024-10-09 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 948c7af5-d72a-3327-ba0e-c47c1ac5443c | -16.9094 | -55.8014 | 2024-10-09 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 463.5 |
| e6b49da4-37b7-3e4c-afe3-7ed13757f33c | -16.9098 | -55.7806 | 2024-10-09 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 270.6 |
| 536b0a32-d587-319a-8274-6272c3b83992 | -16.929 | -55.7989 | 2024-10-09 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 9689ff38-a5ea-31fa-806d-dad45495da34 | -16.941 | -57.4654 | 2024-10-09 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.4 |
| 1d0448a9-38d9-3c5e-aedc-761086fb2b70 | -16.9606 | -57.4631 | 2024-10-09 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 10f31b1a-42cd-3a8c-a03b-ad820a7b41b6 | -16.9609 | -57.4426 | 2024-10-09 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.0 |
| ccf5077e-0684-3e28-956b-553e2c9c568b | -16.9802 | -57.4609 | 2024-10-09 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 45a8963a-cb5b-3a90-b03f-28f917d39ea7 | -17.0623 | -56.0308 | 2024-10-09 02:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 3c8e4ff1-1c68-3d10-9f59-51435d152d46 | -17.0795 | -57.3674 | 2024-10-09 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| cd8041dc-15a5-3492-8d06-3faa8e13d587 | -17.0799 | -57.3469 | 2024-10-09 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 102cee73-7e84-3117-8ce1-ede7db844c97 | -17.0992 | -57.3651 | 2024-10-09 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 60bfc153-faa7-3aa8-9f8e-6a4ac3251f24 | -17.0995 | -57.3446 | 2024-10-09 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.5 |
| 348dc4a6-6db3-30d7-9edf-522b087ee8bf | -17.1188 | -57.3628 | 2024-10-09 02:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 33230b42-adf7-3b32-a7e2-78a9dd768263 | -17.1588 | -56.1222 | 2024-10-09 02:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| ac521f46-74de-3817-b3ec-6818750eb5a7 | -17.7526 | -53.7948 | 2024-10-09 02:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 5e018ba1-00a6-3255-b1c5-1e2eddf7b669 | -18.1193 | -56.3921 | 2024-10-09 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| a16abd22-6ae4-3e4e-b055-9b80197305df | -18.6597 | -57.2137 | 2024-10-09 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 9c901920-d858-3ce4-a82b-57d38cf26929 | -19.7927 | -45.6252 | 2024-10-09 02:46:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 7d60839c-ed24-3f62-918a-a45c971f56dd | -19.8131 | -45.6202 | 2024-10-09 02:46:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 4646af31-9e5f-3605-8281-722f99e9def1 | -20.3346 | -48.7307 | 2024-10-09 02:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 248.6 |
| bce5f4f2-7e5b-323c-b515-14611cbef0d5 | -20.3352 | -48.7076 | 2024-10-09 02:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 3b76c45a-34b0-3f88-a142-a83b47d7fbec | -20.3513 | -48.8648 | 2024-10-09 02:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 106.9 |
| e643c897-3ba1-32d4-8bce-909822cdb505 | -20.3551 | -48.7262 | 2024-10-09 02:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 7f5828ce-3add-313b-9857-a6a2620d8bb3 | -20.3557 | -48.7031 | 2024-10-09 02:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 99.2 |
| d3d7ddd9-dc8b-30e7-99db-9d54870cdd6f | -21.0719 | -47.2094 | 2024-10-09 02:47:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 6e6ef757-2231-3dd9-a2a7-a3c16a98699f | -21.0926 | -47.2043 | 2024-10-09 02:47:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b53b14d1-09fb-3c78-a047-233dd047703c | -21.1126 | -47.2229 | 2024-10-09 02:47:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 77.6 |
| aec722d9-595a-3815-85db-76fdf228b586 | -21.572 | -46.9898 | 2024-10-09 02:47:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 6fbf9714-7b4a-395e-afe7-bed82d01bfe4 | -21.5727 | -46.9659 | 2024-10-09 02:47:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 82.4 |
| d8ecb133-c042-3558-9cac-cd9524a3ce79 | -21.5864 | -47.8827 | 2024-10-09 02:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 401585e5-88cd-3492-acab-eca0a69a0f40 | -21.838 | -49.1493 | 2024-10-09 02:47:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| 79c71452-7828-3cba-8417-8127fb2d1c26 | -1.11 | -53.6173 | 2024-10-09 02:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 6eb075cd-6b1a-3b82-81f6-8c8f46da7caf | -3.9021 | -46.4689 | 2024-10-09 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e76f460e-7db8-312a-803f-a06ad9b15549 | -3.9023 | -46.4467 | 2024-10-09 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 3c9ef996-f787-3789-a203-9386362d470c | -3.9208 | -46.4459 | 2024-10-09 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| de68ddd4-5219-355a-af63-e4f130f656a3 | -3.9393 | -46.4672 | 2024-10-09 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e6589733-5635-30fc-9dd8-0953399e44ba | -3.9394 | -46.445 | 2024-10-09 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.6 |
| c58bba62-0efb-347d-b136-377757398a3b | -5.5905 | -44.8687 | 2024-10-09 02:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 4a11ef6b-a527-36fb-b144-bc7c20928951 | -6.7614 | -60.0559 | 2024-10-09 02:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 8991ea81-4b3c-356b-b9de-5810bff1182d | -6.7615 | -60.0367 | 2024-10-09 02:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 579c9d4a-f67c-373e-bf57-34876d1fb078 | -6.7798 | -60.0552 | 2024-10-09 02:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 08d22ea1-7b40-3d41-bb88-719c0c55576c | -6.7799 | -60.036 | 2024-10-09 02:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6e4a8222-4953-3e1b-af4e-651845369dbf | -8.4919 | -48.6476 | 2024-10-09 02:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 86.6 |
| d626ff14-0881-3b29-99e9-dee766daf123 | -10.3655 | -64.8451 | 2024-10-09 02:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 30.8 |
| f903d5cd-d50c-300f-b0df-1f65e0f95061 | -10.3656 | -64.8262 | 2024-10-09 02:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 33.5 |
| c5f91f84-26c5-31f6-ac22-2bc14cbb52f5 | -10.3894 | -61.2502 | 2024-10-09 02:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7a4875f3-7f6b-35fe-904b-154e297e88ca | -10.3895 | -61.231 | 2024-10-09 02:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| ae6e15d0-8f49-3c23-8995-c78b4340e0d7 | -10.3842 | -64.8443 | 2024-10-09 02:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 7c5fabcb-87bf-3a77-8773-0db31d6063ec | -10.3843 | -64.8255 | 2024-10-09 02:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 85dfc877-68c6-32b0-8edc-d38530d7c215 | -10.6068 | -55.9169 | 2024-10-09 02:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| e8737f74-9a8b-3b8a-b7c6-c7c3c65dcf99 | -10.6253 | -55.9355 | 2024-10-09 02:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| af3dd43b-b374-3643-ba3c-101fe50145bc | -10.6256 | -55.9154 | 2024-10-09 02:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| e38687b0-db36-3e1a-84fc-a2f71fc31292 | -10.6258 | -55.8953 | 2024-10-09 02:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| de5d3f92-b600-32e0-8340-627270d1f7a8 | -10.8567 | -63.9177 | 2024-10-09 02:56:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1e588579-bc0c-3864-ada6-382fa6273fe0 | -10.8754 | -63.9169 | 2024-10-09 02:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.4 |
| c65f7029-10d9-34da-bd0f-84c5f6bba15b | -10.8755 | -63.8979 | 2024-10-09 02:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8c617291-5cb8-3f26-98e0-35e824c0e5ae | -10.8941 | -63.916 | 2024-10-09 02:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d0bc442d-ef58-3b0e-aeaa-d915d6102c21 | -11.5233 | -65.137 | 2024-10-09 02:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| fcfa5e0a-94e3-3fda-87b5-62579f67cbc6 | -11.6806 | -64.0312 | 2024-10-09 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5467e37f-7479-3e3f-97e1-c89d2fa360e2 | -11.693 | -65.0163 | 2024-10-09 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 89980658-7aa8-3d64-ab66-0cacab7a8310 | -11.6931 | -64.9974 | 2024-10-09 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 025a57cb-f15c-3cb8-b915-c818e598d4c4 | -11.7117 | -65.0155 | 2024-10-09 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 832543cb-c609-3532-af44-db4d7d5a2a47 | -11.7119 | -64.9966 | 2024-10-09 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.4 |
| b16954b0-86fd-304c-a072-ffc1719b4c73 | -12.011 | -51.0531 | 2024-10-09 02:56:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 6ca8590e-af1b-30e1-9a50-08d567d78616 | -12.6676 | -63.0819 | 2024-10-09 02:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d20e9559-a899-3c4e-a438-0dfa8301ed01 | -12.7501 | -62.269 | 2024-10-09 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7641f1a1-4739-3c38-8ef3-251b8885ea40 | -12.878 | -62.8007 | 2024-10-09 02:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 0283a603-4a02-3c4e-b52b-3355564c95a4 | -12.9756 | -62.4673 | 2024-10-09 02:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 481654ad-e4ee-3890-89fa-b4a8770ff8b4 | -13.817 | -44.5961 | 2024-10-09 02:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 62f3c2b7-45c6-3c2e-b227-ebb3e90f2a3e | -13.8364 | -44.5927 | 2024-10-09 02:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| aabb65dc-ccc6-3fd5-9924-69e31488b59d | -13.8369 | -44.5691 | 2024-10-09 02:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b177f778-8a4d-3621-bac3-e2c05d034d9e | -16.4184 | -55.9455 | 2024-10-09 02:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| fba0d206-dc21-34dd-9d25-a1e433982962 | -16.4187 | -55.9248 | 2024-10-09 02:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 060a049b-a4d2-31ce-a809-2aa1570b18e9 | -16.9603 | -57.4836 | 2024-10-09 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 6ecfc556-67bd-3d84-9f17-2393c62e8327 | -16.9799 | -57.4813 | 2024-10-09 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.9 |
| d48adbda-042d-3e62-8bd0-2dfb10ad7ff7 | -16.9802 | -57.4609 | 2024-10-09 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.3 |
| ba573171-05ca-3367-9622-32eeb5df8dc4 | -17.0623 | -56.0308 | 2024-10-09 02:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 4e2b7830-51ad-3acd-9013-a6594bf6a6af | -17.1588 | -56.1222 | 2024-10-09 02:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| e4c46183-988a-3146-a5ad-fa62ec984c08 | -18.1391 | -56.3895 | 2024-10-09 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.6 |
| 1016247f-9f67-3e77-a60f-1834d45906cb | -18.1193 | -56.3921 | 2024-10-09 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 7dce7f22-5bf3-37b0-b301-71e947242fe5 | -18.5993 | -57.2629 | 2024-10-09 02:56:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| a74c011a-94d6-33a1-b9d4-57bbcd142cce | -18.5996 | -57.2422 | 2024-10-09 02:56:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 16baf5d5-35d5-3e14-9915-ffbd2d971175 | -19.8131 | -45.6202 | 2024-10-09 02:56:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 8e886e1f-2f22-3467-896f-a0f8d6ccd494 | -20.3346 | -48.7307 | 2024-10-09 02:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 218.9 |
| 6a978896-deae-3e77-b1e3-b397b10a99dd | -20.3352 | -48.7076 | 2024-10-09 02:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 22149302-46ed-33a3-992c-a140b98d0596 | -20.3551 | -48.7262 | 2024-10-09 02:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 180.9 |
| ec5cfad4-ab0f-3b71-b346-78d9bb26347b | -20.3557 | -48.7031 | 2024-10-09 02:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 3ce81177-d43b-34bc-8183-dd3b41dd64cb | -20.6396 | -45.9158 | 2024-10-09 02:57:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 83.9 |
| e6676259-12fa-37ca-bb7b-65952819375f | -21.0926 | -47.2043 | 2024-10-09 02:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c2fec8df-c5e6-39e8-966a-683f32512ac1 | -21.572 | -46.9898 | 2024-10-09 02:57:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 6e46bfed-ce6f-39cb-bdb6-c920149a0942 | -21.5727 | -46.9659 | 2024-10-09 02:57:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 96aaaa6f-6d3e-3688-9fae-ff5cf2f64479 | -22.1369 | -48.1224 | 2024-10-09 02:57:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 85.7 |


[Clique aqui para ver as próximas entradas](README56.md)
