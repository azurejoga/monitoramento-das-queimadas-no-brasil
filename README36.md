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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d5c40cc-4cae-3e09-bcc8-fa80e1ccf373 | -2.63591 | -54.75355 | 2026-09-14 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b176374-161b-3c35-ba86-f22d70a429b0 | -2.91713 | -50.44248 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31da4e04-db00-3251-99cc-fe379422aac8 | -2.88071 | -50.41565 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ddb8db4-daf3-34f0-be68-fa6e76c94129 | -2.91206 | -50.38885 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b6aebb9d-54a9-351d-86b0-189de96fe858 | -2.90775 | -50.4375 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c72bee28-4680-3272-af2f-65e9245ec23c | -3.37695 | -50.39154 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c52f5b7b-be92-3e82-8a6d-dbce7aa8a011 | -5.29105 | -45.26806 | 2026-09-14 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1c4265d6-7938-3539-8a13-020b35d5ab09 | -2.90499 | -50.43354 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 620eae3d-d2be-3e32-b288-e95318f3601c | -3.85686 | -52.15865 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36e619a1-1b60-3243-a368-d7120383dc58 | -2.95559 | -50.39215 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f25592f-4031-3d19-810f-e6fd4e76d805 | -2.62348 | -50.83739 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3487184a-c46f-36ac-b52e-f76743f546e3 | -2.9435 | -50.40434 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74f77f4d-3380-3c4d-862d-329ea2c30475 | -2.8813 | -50.43335 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c05810f-bc94-3fbe-9132-35f60ec96c98 | -2.69594 | -57.54372 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9bff522a-f891-3fa3-a9db-196e07703b0d | -2.92089 | -50.39728 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 17251f99-51d4-342a-a091-ef605faed191 | -3.2227 | -50.59309 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19bedfa1-9cc6-3f6e-8f06-cc716fe8e8c0 | -2.92646 | -50.42633 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73eeeb58-0fc6-3f47-9ca6-c178922d1351 | -2.94513 | -50.39403 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4001199-c76a-3fd8-a5f9-072cf9c6f003 | -2.87966 | -50.44366 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e83bef2-6a3c-33ce-86d2-65bdd19607a8 | -3.35282 | -51.29298 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f8267d9-ac88-360a-8ef4-8051dcb361da | -2.91596 | -50.40707 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 23a9eb51-5e23-30e4-a132-4bc08acb240d | -2.92755 | -50.41946 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6485eff-0538-3ed0-bfd5-8a0744247884 | 0.17897 | -51.4764 | 2026-09-14 04:51:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8d782ac-602b-329a-8f6d-8891b815c865 | -3.38988 | -50.76027 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b9dcd4d-c0b9-37dc-a315-2ba9344c8474 | -2.94735 | -50.40142 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f208681e-6875-37ae-824c-d834fe0454e9 | -2.96665 | -50.40797 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14ad3592-ca11-307b-8aa0-af41392b2612 | -2.91156 | -50.41343 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| e47a15ef-c74e-3e15-854e-461096760112 | -2.92583 | -50.38749 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1018b2de-1059-30bd-941b-516e6b43f9b7 | -3.5496 | -48.18192 | 2026-09-14 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e60d71d-d79f-31dc-90f9-6d29c8424f0d | -2.88515 | -50.43043 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abd630b6-38ad-3658-ad88-d4ff60785b99 | -2.91319 | -50.40312 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 48e913ec-0d72-3f8a-beab-158416f2ff21 | -2.92973 | -50.40571 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b2c55d2-b8fc-3eb1-af2e-c24093495e3e | -2.93525 | -50.41362 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0da7d850-828d-36fb-b31d-82f421b9f06c | -2.91265 | -50.40656 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 213cf5fc-0010-3baa-a345-b76120871d06 | -3.38357 | -50.39257 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7479cccd-a9ff-3249-a73d-34c46a55cd08 | -2.91378 | -50.42082 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 83e65691-af6b-3942-9534-5582afc6e3ae | -2.95066 | -50.40194 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c42e7dd2-2a72-3544-bd9c-b6bff9043c98 | -1.22198 | -54.1287 | 2026-09-14 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 569bddf3-200f-3ed1-b4b6-73746bae04fa | -3.78589 | -51.34704 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bcdce3e-e1e2-374b-ac4c-2334ad767ed4 | -2.66933 | -57.54347 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed6c4a90-1aad-3e79-b7e3-b2a936661dd1 | -2.93638 | -50.42788 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaacc958-c5e4-3bcb-8883-273b17a0f076 | -1.46414 | -52.96661 | 2026-09-14 04:51:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 823e73d3-594a-3dbd-adbc-d887175e5d68 | -3.35615 | -51.29351 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 901466bd-343a-3d2a-ba96-19cd02fd90bc | -3.7934 | -44.11008 | 2026-09-14 04:51:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c2a9679-5b03-368b-b70b-6afdfa26e0c7 | -4.55482 | -50.46074 | 2026-09-14 04:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| efd25ab2-b361-3aee-824c-ac3deca0cbef | -3.23493 | -43.03529 | 2026-09-14 04:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c378ec1-0313-3b54-9b4c-810f2c82d0ea | -2.6185 | -54.72947 | 2026-09-14 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09d5e851-b700-3c3d-89c7-adb57020ec5b | -2.95836 | -50.3961 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf119017-2958-3af3-ba25-c4b4560451ab | -1.71612 | -54.95404 | 2026-09-14 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d29c13d-a423-3b92-b573-32d8757788fb | -4.34779 | -48.96512 | 2026-09-14 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f33d5d11-6038-39c6-a0d8-36aad0d32c97 | 0.18237 | -51.47588 | 2026-09-14 04:51:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e67f9e5e-795c-37d3-ac89-1447d500c631 | -3.04746 | -51.27013 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1405997-3965-310d-89ed-095fbca4862a | -2.97125 | -49.56171 | 2026-09-14 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac07a39b-b3ce-33a9-bfc7-0299eef63079 | -2.89285 | -50.42459 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 83f1605e-f629-32c0-881c-f3bfb7ace7dc | -3.38766 | -50.75286 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4147b725-3436-35f8-8699-5e38b2624eec | -2.87385 | -50.4353 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d2df8d9-605d-3649-b670-0a69a3563a53 | -3.19633 | -51.01624 | 2026-09-14 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6056d598-df99-33a3-afa6-f07275f18b08 | -2.94078 | -50.42153 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65487b74-cfff-301a-bbc0-c54e11a56cfa | -3.22378 | -50.58622 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 283d8c46-41cf-3d59-83c8-720098f3fc37 | -2.89511 | -50.45312 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26af3bc9-24c8-3f64-a612-e39e5dd324dd | -2.91495 | -50.45623 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6e955fd-1933-3f71-90d6-726d2675ad4d | -3.22985 | -50.59069 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcc07c80-f4c6-3cfb-aea5-356f43c8ef8d | -2.87799 | -50.43283 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ebab83f-1741-3af7-9254-1ee1a808182b | -3.7896 | -44.10495 | 2026-09-14 04:51:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b29534f9-f43c-3248-b93e-54beae5bb7b8 | -2.78435 | -51.36441 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6db1d2fe-c25e-3738-bd88-d30a1340a992 | -1.86432 | -54.42623 | 2026-09-14 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c5dc278-d780-3394-ba3a-63fe628833d3 | -3.04634 | -51.25566 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab774bc7-ea52-3642-86ba-28bc58f18c1e | -2.91981 | -50.40416 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f4da68e5-735f-3abf-baf4-7c0bd6c86789 | -2.93575 | -50.38904 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82ea8450-a855-3139-9a1a-5f714d038258 | -2.91771 | -50.46019 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3be6ee03-bd1e-338a-b9ea-cd93ad9c0af9 | -2.96497 | -50.39714 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7dbefe7-9f2a-369a-ae8b-ed2e5fe82998 | -3.37831 | -50.76903 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 662721c5-bd68-3025-bbbb-40c6e7f703c1 | -2.92148 | -50.41499 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca4ca4eb-3883-3a6f-b789-648a105dd5f0 | -3.16259 | -48.61264 | 2026-09-14 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b21525af-b5c2-39bf-af61-4962d91d1dbd | -2.9121 | -50.40999 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| cfe96352-698d-30e5-a996-829f8b48aa53 | -3.53741 | -53.98289 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b29e3611-8d6c-3fc6-8b02-753e5c658293 | -2.90717 | -50.41979 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| ec4b9c7a-b0b2-30fd-ae6f-fcaf6e500c11 | -2.88733 | -50.41668 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f32dac1a-63d9-310b-871c-ea86768ce2f3 | -2.7838 | -51.36791 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8edff769-ec9b-3954-ad19-0b1cb127c49d | -2.88456 | -50.41272 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa7d8442-2dad-3087-9dc4-6b47cf9e3f85 | -3.86082 | -51.98287 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c731d867-09ca-3e84-b20e-46aec8d3d1b4 | -0.00334 | -51.07754 | 2026-09-14 04:51:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 150ff943-f69d-3d9c-9eda-0c8e67322168 | -2.61008 | -54.75755 | 2026-09-14 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| c7e94835-4435-31fc-91b1-9ed74faf6e03 | -3.37972 | -50.3955 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 775e5b99-730a-3999-bbc2-b900a24e9d59 | -2.89063 | -50.4172 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5c3a8e16-b2b2-3dab-afae-a22023951a9a | -2.6724 | -57.55401 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8e5e5c4c-3611-3501-abed-eb4e28a92173 | -3.53671 | -53.98718 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b4740ed5-8710-33a7-a41d-657fa6267132 | -3.16277 | -48.61258 | 2026-09-14 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d79b6a63-b05b-36ea-b20c-89bbdc5662a0 | -3.02119 | -53.86402 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b76b95c-5fec-31ea-8f49-f8ec6c94a5dd | -2.93249 | -50.40966 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a900688a-50e7-3c00-a16c-04df5b6b3575 | -3.24743 | -54.31143 | 2026-09-14 04:51:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f7392d-e79e-3ea8-889c-47722eb4472e | -2.93743 | -50.39987 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad6570ef-f560-3e9e-a4b2-6a28fd0685d0 | -3.54038 | -53.98774 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7cb6f8e7-95d2-3e6b-9524-fd4ec9873891 | -3.54107 | -53.98346 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e7bb3989-91a0-3c01-a144-e424d35cb802 | -1.196 | -54.12359 | 2026-09-14 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58969b2f-a989-3a7c-9a3d-f093e73b1249 | -2.91822 | -50.43561 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ede9bb23-c395-3df2-830a-3a864345115f | -2.94626 | -50.4083 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec37da25-7d15-3f50-b1f2-e53a6e9bb8f6 | -2.95672 | -50.40641 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ccdf5e2-2b7b-3322-9ba4-ca11fe842bba | -2.89398 | -50.43886 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6dc49703-f6d4-39b7-b266-2829b52d65f1 | -2.88682 | -50.44126 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README37.md)
