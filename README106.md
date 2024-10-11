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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad60fcbe-1108-363e-8d53-d1a5bcf766b6 | -4.23048 | -59.85678 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fc469ae-064d-3fcc-9369-f8e313dade92 | -3.60208 | -59.77345 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c9b523c-64f7-35df-bba6-67c73fb57b75 | -3.9103 | -59.10812 | 2024-10-11 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9e9347b-6091-3a94-9ec9-9da862bb44fa | -3.68456 | -58.77893 | 2024-10-11 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e249d36-3a7e-3141-99e1-7bf62917b01a | -3.68398 | -58.78287 | 2024-10-11 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ae07bfb-b6b2-33ee-a06a-f5c026c21796 | -4.54814 | -59.91962 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09b9ca7b-0b85-3097-bd4b-8ff2ec18bb96 | -4.54636 | -59.9158 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13951c0d-4f8c-33e6-9906-7f0140ae6bc8 | -4.52652 | -59.90051 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d626048-8db9-37d7-b0ba-8df2a3c27076 | -4.28973 | -60.01306 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a45de0e9-5ad2-3d44-b301-d66072a64b49 | -4.25637 | -59.99254 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53a3570f-0cef-32e6-b33e-b912f87c12f5 | -4.23368 | -59.86253 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e1aaa79-dc05-3e74-b391-04b59695810a | -4.23151 | -59.85835 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d360ee5-3d6c-3c32-8373-14ddb3b71465 | -4.18777 | -59.94963 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2454b04-8799-3ff1-b56a-303bc0d636c0 | -6.46673 | -59.7746 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75880fb7-01c5-3f4b-84e1-bad568e8aa40 | -6.38622 | -59.98106 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b0c27c2-c1c4-3934-aa48-c2863758430d | -6.38519 | -59.98826 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05d8fe86-e0d0-338a-a5e8-ff317d2e259d | -5.57152 | -60.17034 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9381b8b-9a35-3b0c-93ce-8670afcf872a | -5.33834 | -60.12608 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b5934a9-9dbf-3928-9ac6-8108c0238c77 | -5.33512 | -60.12033 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1369ac43-5d9e-3e64-b47c-6c0f321950b8 | -5.33359 | -60.13062 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 68c92bd6-1262-3c12-9b45-ac4a97a7fe3d | -5.33282 | -60.13575 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa43f73a-fefe-3b92-8bb1-8fca143b3d70 | -5.33264 | -59.80186 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37b17d6f-bab6-3bb1-8302-20cb9666f131 | -5.33211 | -59.80544 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3a561ce-e23a-31fc-8620-68c07ddc2cc7 | -5.32807 | -60.14028 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b0c4499d-3359-38cd-84de-8e1974018013 | -5.32731 | -60.1454 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce868920-6c18-3855-b18f-1e75e42fc40a | -5.32485 | -60.13455 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c33dddd2-abf1-33f9-816b-cb4fcc9b17f5 | -5.32409 | -60.13967 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ba2bcfe-54f8-35c8-b945-841b1e0e1144 | -5.29016 | -60.08564 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5af8e52-00b5-349f-86d8-d31454dd8373 | -5.19826 | -60.07189 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df56a03d-eb69-3e12-8e83-3a1eddc391fe | -5.19427 | -60.07127 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7b73de0-cb61-39b1-99c2-16b1b40d2b76 | -5.19155 | -60.22728 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9225031-bbc3-3337-954f-cf399094064d | -5.57074 | -60.17548 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b04db43-2cce-3486-8cd9-13eda7a28331 | -5.56753 | -60.16973 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0145ed2d-d35e-3233-a6d2-55f7b41de7bc | -5.33911 | -60.12094 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f80b0ac-dc7b-3d7b-bb78-f421ee851153 | -5.33436 | -60.12548 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a85d2f62-948d-364f-a57f-222e608a5117 | -5.33205 | -60.14087 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 23cf7967-5013-3586-9f56-913d1fbdadcd | -5.33113 | -60.11974 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0996cc0-1557-3a27-a484-2114b117e3d8 | -5.33037 | -60.12488 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2a298ac-d912-33cb-bba5-67c50b10dce5 | -5.32883 | -60.13515 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23640274-e060-3cc8-b408-d23bee25e18a | -5.32638 | -60.12428 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dfbabb54-3791-3229-9894-4929352c884c | -6.83375 | -59.09944 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff2a563e-4afe-375c-adcd-d2b90ec029eb | -6.80948 | -59.14304 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a58f51a4-98a5-38e2-a4e9-dd5c98357a15 | -6.80513 | -59.14242 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b49d5126-aa1a-3a13-889f-9d50bc5ce367 | -6.78456 | -59.31177 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1391ce7-a97d-37ef-8a56-0e62a75a1796 | -6.78026 | -59.31117 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89312288-cd07-3194-96bb-5b35ea583be1 | -6.73958 | -59.28884 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f19835c-51b7-3f21-a4f0-98c6c9ed6f8f | -6.739 | -59.29286 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53efa45a-14ee-3909-a35a-1a8b588a6d34 | -6.73842 | -59.29689 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d078fa38-b868-326a-bb21-948af1b01d34 | -6.73469 | -59.29227 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb7a74d1-fea9-3915-9074-9418ec1fabde | -6.73411 | -59.2963 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54e1a3bb-788c-3276-9db5-acaeb53980f5 | -6.72376 | -59.30721 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f60e61ae-b7ec-39ee-850f-84977c064a7f | -6.72062 | -59.29848 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9216f74f-2287-39b5-9cbd-08c5225af93b | -6.72004 | -59.30254 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ad6216e-3fe4-3b80-854c-53ae8e7142ca | -6.79618 | -59.6426 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3a82355-54af-3194-8d33-67eeb73acdde | -6.79562 | -59.64646 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14bc01d4-a1e5-3efb-a1e5-2a12fef622bb | -6.79309 | -59.6343 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a249f4c-1265-3452-b101-830d2f93c137 | -6.79252 | -59.63818 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86c1d20f-e84f-3711-a177-da0bf2a6da89 | -6.79141 | -59.6459 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cffcca1-9758-3cb9-9e10-f4f2a397ef3f | -6.73723 | -59.63123 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43e7c349-f387-36a1-92a8-33fd1ce26742 | -6.72902 | -59.6576 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0d9f4c6-051a-3ec4-b331-1c4c7418493a | -6.67631 | -59.81271 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38581eda-5122-3aaf-a2f1-1a4cb2a6b46b | -6.65937 | -59.78335 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b17057f4-7f78-3843-a4bd-ac7c7ecb2d46 | -6.65522 | -59.78273 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e009683-77ba-37eb-9f1f-1e17f862aab4 | -6.61029 | -60.00597 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 695f8044-4561-3216-98bc-d295954840cb | -6.60671 | -60.0018 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6ab7103-c1b2-38b0-ac63-9f5078a74c9b | -6.55816 | -60.02858 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b53cd0f-df97-35ef-96e4-bde8ce9e5968 | -6.54891 | -60.03464 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9401313d-c057-3938-aeb7-ef5ddd6b6527 | -6.54695 | -60.01966 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da85138f-65b7-3666-8c34-a26d902cb0bf | -6.54598 | -59.76717 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27045f1f-70b6-3c19-8a69-049805708a30 | -6.54588 | -60.02691 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2397ab43-5da6-3667-b581-5a79405e66bd | -6.54237 | -59.76278 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52f45b9c-9efc-343f-b8ff-b4d6b8db48de | -6.5418 | -60.02626 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b919418-aca7-3a6a-b7c3-a79c6950f023 | -6.54127 | -60.02988 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f9315f1-bc28-388a-99b7-1b135d6a05e8 | -6.79674 | -59.63875 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97aba46e-0f41-3d65-9d20-536e45aa5a4b | -6.79197 | -59.64204 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8741b27-3a7d-3fb3-9719-038a2d4348df | -6.78396 | -59.31585 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fcb980d-9659-3e16-a9a8-ccf136a810eb | -6.77966 | -59.31525 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81f51c2b-b604-3c72-98ba-8d56a0bb9033 | -6.77905 | -59.31937 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6033bc6-38d5-3e48-af13-d9dc766abc59 | -6.77899 | -59.43776 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 28a391ec-c5bb-30f3-92a8-56d1f73267b3 | -6.77535 | -59.31466 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bafd2ef2-ff64-3eab-9463-e9e7b2168441 | -6.77477 | -60.04819 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebcc3925-4b43-3ada-9bf7-849760e9e865 | -6.77475 | -59.31875 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb9e9fde-ba62-3a17-a3dd-79a0befc60fd | -6.77471 | -59.43719 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5f3cdf00-3e59-312f-962f-84e80ca4ea8e | -6.77415 | -59.32281 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1451381c-a141-308a-aa4f-61ba3c8044e2 | -6.77105 | -59.31405 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b92f0ec0-2287-3bec-8321-6c9a22b00267 | -6.77045 | -59.31813 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 793a66bc-e3b0-3a25-b04a-777823080ade | -6.76985 | -59.32219 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5987e0ad-d869-3a10-907a-9de3d407af1f | -6.76926 | -59.32621 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82ec5196-4d70-3513-85c2-73431917b2f1 | -6.76615 | -59.31751 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74d7d149-16b7-35cd-9354-3c10d148a2b7 | -6.76556 | -59.32155 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdb73bb2-c796-38a8-bb70-87e43823e7a0 | -6.76497 | -59.32555 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02ff6709-315a-305d-b915-adc3e6d771ed | -6.76313 | -59.78227 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d8355a5-7c02-3496-a9eb-536bdaa627c5 | -6.76185 | -59.31689 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 529ea99b-ed00-39d9-9fbc-9aed1fe8ae4f | -6.76126 | -59.32093 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 343374f0-a19d-35e3-9ab1-96242d0ee54d | -6.76068 | -59.32491 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e9b219d-9f98-362a-b190-c2fe47953be1 | -6.75697 | -59.32032 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fce2a58-3f31-3990-8141-6f1bd309918a | -6.75638 | -59.3243 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1df33a70-a230-3cc8-8ef0-7097506f0bf9 | -6.75635 | -59.61836 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb33869b-367c-3300-82e3-48ab6633b955 | -6.75463 | -59.33633 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e0e7fd91-e735-3d4a-a995-03ea0d6309df | -6.75209 | -59.32368 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README107.md)
