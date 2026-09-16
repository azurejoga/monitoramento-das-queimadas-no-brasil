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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b16d83da-6141-3d2e-8820-04f74430ec7c | -3.4461 | -58.0005 | 2026-09-16 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| f4294942-3a85-362f-bc9c-afcc9dcb4a98 | -13.4468 | -54.5968 | 2026-09-16 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 4973c9db-ed4a-349a-9d98-3c8e4f25925e | -10.3953 | -58.3159 | 2026-09-16 14:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 207.0 |
| fedbb58a-8f78-3855-bc56-b1fefdce4371 | -1.6022 | -55.5682 | 2026-09-16 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a43f0b31-524c-3523-a1ca-f70abe6df58f | -8.6188 | -44.4819 | 2026-09-16 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 2b486fcb-fa90-3587-b0c7-372726262002 | -1.8426 | -54.4317 | 2026-09-16 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4c9e4570-fe85-36d5-a746-800c67b5f52c | -9.031 | -61.0122 | 2026-09-16 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e07f2c65-bc4e-36dd-b18f-630a3d294f76 | -8.8459 | -45.8713 | 2026-09-16 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 1ca272ed-fd37-30f2-a9fc-5aee9461278d | -6.1177 | -59.9069 | 2026-09-16 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| da327e5c-15de-3895-8357-7e2dd08031a9 | -10.3766 | -58.3171 | 2026-09-16 14:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e0b5d8ea-13e4-3abb-a911-27a7d35e5d34 | -9.7793 | -60.4744 | 2026-09-16 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 79295709-f17d-3c21-a2df-5e9a1c1aeabc | -6.3196 | -59.9956 | 2026-09-16 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1d16af66-7e92-33af-be0d-4d45b6bcb5bf | -10.6829 | -54.1475 | 2026-09-16 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0790cb28-9152-3d6f-8ff3-da93840a79bc | -10.876 | -50.8163 | 2026-09-16 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b1c0c66c-e482-3f3c-beff-0fe84e4c7d98 | -5.1256 | -55.9352 | 2026-09-16 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5580d0cb-16cd-334d-b3a6-3e11ef6f95e8 | -3.1174 | -57.6779 | 2026-09-16 14:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 83af2aed-9369-3914-b086-72c9e67594a5 | -11.6315 | -47.3105 | 2026-09-16 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 95d79d6c-f94f-3f77-9c82-1fb8746d6e6d | -11.417 | -51.416 | 2026-09-16 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 2e80bc2c-38b7-3335-9f1f-c5c48d0d15f5 | -10.3955 | -58.2962 | 2026-09-16 14:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 5fc75a3e-9365-3ac4-b7e2-46cd85490c0d | -9.8099 | -45.8759 | 2026-09-16 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| f4192af4-25d4-320a-8460-3aa2d2e3a121 | -6.1292 | -57.7223 | 2026-09-16 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2b2b6d50-1d06-3f3e-9e1c-1ab2e59c214e | -11.2382 | -43.4887 | 2026-09-16 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 279.2 |
| 87159225-a297-3d0a-8b45-711830d01cfb | -12.6636 | -54.6782 | 2026-09-16 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ffe20e86-0f0e-32ed-84e2-0c632135d1d8 | -11.417 | -51.416 | 2026-09-16 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c1c621d1-a49c-3dbd-a347-091914d56cdf | -9.0059 | -65.4186 | 2026-09-16 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 053bb90f-55d5-3a11-bda2-8ee943fe1ef6 | -1.6206 | -55.5679 | 2026-09-16 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 967ab00f-6803-3ebf-a74e-a566a4d8e0cb | -7.0428 | -59.2173 | 2026-09-16 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 34448c97-6027-3d9f-b45e-5deb0d7c9427 | -9.7913 | -45.8555 | 2026-09-16 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 13cfd765-99a8-3950-8f28-b9f40c8b1dd9 | -11.2488 | -54.1378 | 2026-09-16 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| ba8b79fd-e285-3e15-a9f1-30a867718783 | -11.4167 | -51.4371 | 2026-09-16 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 15e4cb23-fbc6-3c28-9dd2-91d6af260499 | -3.4645 | -58.0001 | 2026-09-16 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d12c0ed6-d760-3e1e-acc7-3b4d7a618b17 | -9.0866 | -61.0287 | 2026-09-16 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 3e6c09c7-42ec-3da9-812e-72caffc2e7ce | -6.7839 | -62.9782 | 2026-09-16 15:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 54f30f99-a827-320b-aa01-7826e410157d | -11.9543 | -49.7728 | 2026-09-16 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 0d4abca1-6163-3fea-97f7-5651218dbe47 | -9.0124 | -61.0131 | 2026-09-16 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| eae3a58e-14d5-3f58-b521-b28435bda6ea | -14.1633 | -51.7464 | 2026-09-16 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 18185af1-1ebe-3209-93ac-c445a63f8ac6 | -6.6021 | -58.849 | 2026-09-16 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 8ed0749a-a072-3d2c-b053-353595c918b8 | -13.5719 | -51.4605 | 2026-09-16 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 490bc9be-d715-3036-b293-1d254e75e76a | -8.8456 | -45.8939 | 2026-09-16 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 4012cf2b-1f20-34ed-8d73-81196d8a3249 | -15.5588 | -53.8266 | 2026-09-16 15:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 6d64ac3a-5c40-38cb-8cb7-331b9add4278 | -13.3761 | -51.698 | 2026-09-16 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 924e5ab8-4ecd-311b-9518-40af86e3aaed | -11.7962 | -46.5926 | 2026-09-16 15:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 0d1d6e0b-9f3f-3429-96ce-c3d69a080481 | -10.9595 | -50.2529 | 2026-09-16 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 52c2fe6f-071a-35ca-9111-07d9bb05b6fd | -9.0309 | -61.0314 | 2026-09-16 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4da3d184-852d-3b04-bbee-345159cbff8e | -10.876 | -50.8163 | 2026-09-16 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| b7fe3de1-a5d4-3038-b58f-087627d1ad5e | -6.8216 | -59.1686 | 2026-09-16 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 214.0 |
| ed98a3c5-32da-3d13-b677-36363116e22c | -10.6829 | -54.1475 | 2026-09-16 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 547ac403-d3e7-3ca6-a1ce-f1b2a4541d88 | -6.7832 | -59.4401 | 2026-09-16 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| c10a320b-24c8-36d3-9114-6862b359d12c | -12.1072 | -44.2021 | 2026-09-16 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 1b945633-fbb6-3d03-a6f3-f0620387207d | -6.7869 | -58.8027 | 2026-09-16 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e3b75eb8-4f82-3fa3-84ae-003f6e549e62 | -9.1337 | -65.844 | 2026-09-16 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 0276e395-42ee-3ddd-b251-a143fc890aad | -9.7322 | -64.9067 | 2026-09-16 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 1f7aa938-386d-3d8c-a0d5-1808f1012a13 | -9.7909 | -45.8782 | 2026-09-16 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| b0078302-fcd9-39e5-aca2-8d39d30e3c6e | -15.6557 | -52.7366 | 2026-09-16 15:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| c128cfc9-db5f-33d7-be94-d452bc6f5fab | -5.1255 | -55.955 | 2026-09-16 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4cc41053-e376-3e2a-a516-e26d93cc70f2 | -8.6184 | -44.5049 | 2026-09-16 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 77010bf9-9e6a-3af9-bad3-f1064f8c7f02 | -11.2113 | -54.1208 | 2026-09-16 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2a2456e0-e1db-3285-bada-7ea363362473 | -9.1624 | -60.814 | 2026-09-16 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| cf68132b-160f-37ab-896a-1b7fcf9ec55e | -12.6628 | -50.8264 | 2026-09-16 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 24739d26-c6f0-32f2-b26f-426e15f03f40 | -8.2052 | -54.8416 | 2026-09-16 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 9c7abcfc-7c4f-3cb9-b0fa-f8974b1edf85 | -5.3646 | -56.0249 | 2026-09-16 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8c633271-58b3-339d-89e5-589257986392 | -13.3185 | -51.7051 | 2026-09-16 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| dea1998a-c8dd-3bdf-a18d-aea897dcb659 | -5.4546 | -60.2155 | 2026-09-16 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 99d356f7-fc3a-3d17-9c63-985fc09fbd11 | -9.8099 | -45.8759 | 2026-09-16 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 300.9 |
| 7f9c5cf9-7cb7-3ba8-a0a2-4c3a9bb9e755 | -8.6188 | -44.4819 | 2026-09-16 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 197.7 |
| c2bee64f-f8be-38a8-9582-29a61123d2fc | -11.2386 | -43.465 | 2026-09-16 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 280.1 |
| 68a4fdfe-68cd-3c24-a2fe-88241b97b5a7 | -6.7684 | -58.8035 | 2026-09-16 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| e7100ace-0620-334b-b4fb-0904c20f3b8d | -11.2115 | -54.1003 | 2026-09-16 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 5f3983dd-a288-3f32-af04-08000fbaeefa | -6.2731 | -55.2904 | 2026-09-16 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7ba8fbd0-f89c-3812-acab-054764df0382 | -3.4462 | -57.9812 | 2026-09-16 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| f9ccfbaf-e350-3d2f-839d-b78c9a1d5807 | -13.3199 | -51.62 | 2026-09-16 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| e553a2fc-f7e8-3d6c-b5c7-3e0a4e0652e4 | -5.1624 | -55.9338 | 2026-09-16 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 09dff666-f19c-3c9e-9248-781966f7de43 | -10.4772 | -50.9634 | 2026-09-16 15:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d8c9cc37-d45c-3d74-9e63-be60c17a3f78 | -13.6337 | -45.9732 | 2026-09-16 15:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| d409e84f-c42b-3af0-b5c3-7b4a90b1b7c4 | -8.3737 | -54.7299 | 2026-09-16 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 2647c6da-5107-3cec-a0d8-72c3cfaf6a2e | -12.6818 | -54.7379 | 2026-09-16 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7f0be3a5-20a8-3dbb-bf42-9e493ec6626b | -7.0242 | -59.2374 | 2026-09-16 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 81ef748b-2438-39fe-bc36-cc982c75d1ca | -7.8654 | -55.4446 | 2026-09-16 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3c7d70ab-ac21-3dcb-9e2a-ad3dcd803598 | -3.1697 | -58.6437 | 2026-09-16 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 883414d1-7f90-3006-abab-9da8f53cca41 | -6.67 | -43.657 | 2026-09-16 15:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 06271716-cd64-347d-9c30-aac9bbbddcdf | -9.031 | -61.0122 | 2026-09-16 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d68d4588-6ecc-3d3e-8900-5c09f99b2d0c | -12.6636 | -54.6782 | 2026-09-16 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5e0f295b-90af-3a5f-ae55-5c197cd76750 | -6.5836 | -58.8691 | 2026-09-16 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f7269a93-43ca-3ecc-b7e7-60ced45bcdb8 | -1.6022 | -55.5682 | 2026-09-16 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| ec6db8a9-c515-3d31-8e94-cf620003e33c | -5.144 | -55.9345 | 2026-09-16 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| a317728d-f518-396a-9303-ce6e3b85d8a7 | -12.1265 | -44.199 | 2026-09-16 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 338.0 |
| bec4142a-87d0-351d-8e5d-b4f7d28e3fb8 | -11.9356 | -49.7535 | 2026-09-16 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| acb97819-6e10-39c5-ae9c-f2782c96ecc5 | -3.1604 | -42.4386 | 2026-09-16 15:00:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| f705013e-73bd-3a96-9920-46ac3a2236e6 | -13.4468 | -54.5968 | 2026-09-16 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 7a159948-eac6-3fbc-80bb-7992611b7f3a | -6.1292 | -57.7223 | 2026-09-16 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a961561b-07f6-399a-af3f-806ab7abff2e | -10.3766 | -58.3171 | 2026-09-16 15:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 908ac7da-2eb8-3e77-9022-b377f473bac0 | -13.2996 | -51.6862 | 2026-09-16 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| faef2f9d-e840-3f44-b3e1-de3c9cd54ab2 | -12.1453 | -44.2195 | 2026-09-16 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 3df6effa-ae20-3dd2-afef-3d6a6a70bbeb | -10.3955 | -58.2962 | 2026-09-16 15:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 183f0956-7095-364a-8c8a-e5b4582f264d | -3.1174 | -57.6779 | 2026-09-16 15:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| e636636c-5605-38ba-892d-15b81749fcd9 | -13.3566 | -51.7217 | 2026-09-16 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 0f5fa043-a225-3261-b99c-a95b042f1d6c | -13.3946 | -51.7382 | 2026-09-16 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 70dfe0b0-c13f-3312-b341-653c082e688b | -8.5431 | -44.4902 | 2026-09-16 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 220.5 |
| a91eb49e-8189-3569-8355-23b83b738235 | -10.8571 | -50.8183 | 2026-09-16 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ddf1b118-78c4-3136-b142-8a435d58e442 | -9.3892 | -60.3215 | 2026-09-16 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |


[Clique aqui para ver as próximas entradas](README80.md)
