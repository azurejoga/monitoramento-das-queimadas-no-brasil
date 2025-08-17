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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b45214d9-3b02-3e56-87d7-6ff6e14d2837 | -7.53331 | -50.526 | 2025-08-17 05:04:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5584734-09a7-38a7-affb-8168cb87a95b | -5.44818 | -60.12867 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6d5f73a-3eb9-3708-9b6c-3684090ac0de | -6.48153 | -55.88277 | 2025-08-17 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0c967c1-afd5-3cf7-9e23-b548ee3095c7 | -6.06571 | -59.9584 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6210dfa0-84c0-3442-99d2-768256317c27 | -6.1416 | -57.93095 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8819742-7d31-3318-ac5e-a857197b16fc | -6.42107 | -53.37091 | 2025-08-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff76dfbf-8423-3b51-b24f-4e89faf55a0a | -5.79982 | -59.22775 | 2025-08-17 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2de7d627-1896-3a39-b21d-2414360ea8fd | -5.57295 | -52.0499 | 2025-08-17 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50b96f14-ddd3-31f5-84da-cefa56f8ebfa | -6.49445 | -53.38971 | 2025-08-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f03ed6a-1d3a-34ac-84a7-ebe73e3fd16b | -5.93269 | -53.65134 | 2025-08-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cf2a8ac-fc8d-3d19-94a9-85c92a3c2e66 | -4.92749 | -43.25054 | 2025-08-17 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7b02879e-0992-3c53-a76b-e54635168e00 | -7.70835 | -56.41057 | 2025-08-17 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 312fd17b-46e2-3f7a-8525-edcac98fc774 | -6.63876 | -60.01776 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e5b7793-00d0-33de-86ac-1787b7aed22e | -7.14644 | -44.62612 | 2025-08-17 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82f6e3bf-b9ec-3774-b6f3-f1ae012ee846 | -8.50751 | -44.72967 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2e5f3968-1c53-327b-b934-37bed069a253 | -6.61895 | -43.87704 | 2025-08-17 05:04:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d45eafa5-6c5c-3fc3-b08f-a10461cd7191 | -2.58744 | -51.91903 | 2025-08-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af65c0e1-cbe2-3975-a911-504a05429b58 | -6.42047 | -53.37482 | 2025-08-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dba45479-0b8f-3b58-aa5c-b119ba206e4e | -7.14577 | -44.63105 | 2025-08-17 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97089afb-5799-3968-9c4d-4301b7bd2a4d | -2.47043 | -54.71209 | 2025-08-17 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd2a0942-fb4b-3331-85de-fb4ff256d0e3 | -5.97496 | -53.55141 | 2025-08-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 387dbb7c-31a7-302b-b6e6-a7b20c8dcbe3 | -2.95888 | -49.06519 | 2025-08-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fced6705-47d0-3b27-9354-7b376a7ed018 | -5.45977 | -60.13055 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 796438ef-730c-3a19-beee-daee8fa67e9b | -7.37346 | -57.62516 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94a08209-f88e-3d12-84f6-83ffbccade00 | -6.55239 | -56.19093 | 2025-08-17 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d97d5c82-a441-3f16-bb18-05780ff6b3a8 | -8.08141 | -47.69822 | 2025-08-17 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8ba88de-ec9d-359d-8cae-713e9327ce55 | -4.91355 | -43.25445 | 2025-08-17 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9fb1094b-09f6-3287-8153-47ffd4c67703 | -3.4515 | -48.96875 | 2025-08-17 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5366786e-68d7-321a-afec-81e0bdae0053 | -7.15358 | -44.38475 | 2025-08-17 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c01ffb0-95c7-3f52-91a7-5a2e3f616582 | -6.0809 | -59.93714 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdfc7ab5-427a-3ef3-acf2-4f59ad920da4 | -6.55269 | -43.02611 | 2025-08-17 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7c52d5cd-b1fa-36cf-858b-560457c3b1d3 | -5.44584 | -60.14316 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5276a555-823a-3d21-bad9-69f197ea03a7 | -6.54592 | -43.02499 | 2025-08-17 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c58010b5-1d9c-34cc-8024-df18a7c3d057 | -3.97611 | -42.52582 | 2025-08-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e3eca509-6bf7-3545-a103-73ea6c039daa | -7.60508 | -44.9356 | 2025-08-17 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26c23177-2ddb-3b03-a5d1-d82b168b874f | -6.54508 | -43.03136 | 2025-08-17 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 362783c4-f962-3f97-b5ba-ccefe6d80889 | -6.07636 | -59.94111 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04a312c9-ae2f-3687-8b71-3a3e5f44c451 | -7.00944 | -59.84051 | 2025-08-17 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c138f9a9-246e-368f-9f38-6087f15839bf | -6.48207 | -55.87932 | 2025-08-17 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a25b7376-ce95-3ec9-a9a7-81fb4ab464d2 | -5.45205 | -60.1293 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38c07252-319c-3511-95d0-d858d0e7df0f | -6.18704 | -45.43745 | 2025-08-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9126cacc-abef-30b1-b92c-a8a2c5f6cf8d | -2.89537 | -51.47682 | 2025-08-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8590e503-506a-330e-b066-d2a3055e08bd | -4.45158 | -55.48431 | 2025-08-17 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f6036a0-9e0f-3b2c-8307-a1e23c905b44 | -8.50059 | -44.7337 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4c21b55-e7e2-34d4-b078-ac737609de0c | -6.08543 | -59.93321 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad9addb6-2716-3011-b26d-1667db56d4d0 | -6.07567 | -44.62817 | 2025-08-17 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0dba3eb-893d-3be3-bf55-4b333a2964fd | -5.45127 | -60.13412 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f0a75fd-d854-3b42-8bfe-7742f3095473 | -4.60132 | -43.3082 | 2025-08-17 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08d54fda-84d5-33c1-b92c-8157fb8432c0 | -3.45654 | -48.96511 | 2025-08-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96ff1128-8197-3166-af82-89bae50bbffb | -7.01016 | -59.83605 | 2025-08-17 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 262033e6-4e60-3238-b15f-65bab24a3d74 | -5.81285 | -59.2166 | 2025-08-17 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59aa3d1d-013a-3d68-a1b3-432ddc9de191 | -4.6055 | -43.32579 | 2025-08-17 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7654e1d-62b9-38bb-a6f7-26821bbfbee5 | -5.80989 | -59.21172 | 2025-08-17 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c3c2c18-26df-3a3e-ae6f-b00952c69c89 | -7.37289 | -57.62876 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 903c3795-ebd5-32c2-ad8f-b0b5a3fbba68 | -8.04308 | -47.67096 | 2025-08-17 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34f11c11-a644-3e07-8616-2fa0b1290ee9 | -3.15246 | -45.65548 | 2025-08-17 05:04:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22099e9d-fd3b-3ea0-99e0-9e812323537f | -7.14385 | -44.63644 | 2025-08-17 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1e281f-ab2f-301a-8a2d-b5c601ba97c9 | -2.8616 | -48.66907 | 2025-08-17 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea8bdccd-0b5e-3b04-9d61-93323140aadd | -3.45214 | -48.96446 | 2025-08-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbd7c8b0-bd54-32ee-8edf-dcbdb6172b48 | -6.63423 | -60.02177 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58a9ac3e-b3ed-397e-afa1-b4263cf83291 | -6.55293 | -56.18748 | 2025-08-17 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35d3bcee-ecd8-3a4d-9fcf-60a191e6e6e1 | -6.55187 | -43.03236 | 2025-08-17 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6a1197e2-e1b8-3c96-a4f3-ea697dc04bf0 | -6.1865 | -45.44154 | 2025-08-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6705b1c3-c2e6-31ea-8934-4b3e7735eee1 | -4.60209 | -43.30268 | 2025-08-17 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7aa78e2e-020d-3b0b-aa34-19012c5d2c8a | -7.62634 | -44.96372 | 2025-08-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3a738705-1d93-3556-962b-e3dd864c46de | -6.66404 | -58.81619 | 2025-08-17 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ac7c491-fa61-3dae-b005-24c6f0957343 | -4.45434 | -55.48826 | 2025-08-17 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 059afcf2-8b1b-3d2f-b55e-101ded68c802 | -6.66411 | -58.81703 | 2025-08-17 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61f96674-959f-30ff-a760-241a58542c11 | -6.93265 | -59.64454 | 2025-08-17 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b07df4d-1bcb-3ca8-aef4-e2ec0034f1fa | -5.95555 | -46.15414 | 2025-08-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76e07c41-0cd2-3e2b-b731-dae062a794e8 | -6.07783 | -59.95573 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 061011f0-35b8-32ba-abf7-0f572da86212 | -5.45899 | -60.13537 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bf7f282-686f-3a1d-9b83-e6406afd0406 | -8.03834 | -47.66713 | 2025-08-17 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33e2e6c3-1662-30d2-bddf-6c2efdf35152 | -5.56924 | -52.04931 | 2025-08-17 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61cc6dc8-80a7-3419-9f94-c4aa5dd7ad21 | -8.50983 | -44.74026 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b5dd167f-b7c2-3ce4-bc0e-de6486cb2565 | -5.9167 | -61.30469 | 2025-08-17 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf1cf6eb-6a9f-395d-afcf-89224a19a192 | -5.8092 | -59.216 | 2025-08-17 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9bd3ef4-3492-3cad-80c9-eb62f5fcee7b | -6.46578 | -55.8943 | 2025-08-17 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afcd1d52-05cb-3ca1-9f46-8cf07d4b7dc1 | -7.62667 | -44.96218 | 2025-08-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3c61a8b0-ca02-3b54-8f1f-2f5ee1a6483d | -7.1445 | -44.6314 | 2025-08-17 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d32a42c-6991-3673-9ee3-6c7047e31b79 | -4.92012 | -43.2554 | 2025-08-17 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ddc4dad9-0c02-3fc0-9a2d-6a83a0dd9f9c | -4.9267 | -43.25624 | 2025-08-17 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c2b85cf2-c423-391b-ba8d-612001bd66b0 | -6.0695 | -59.95903 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19894228-96d8-386c-b628-3803badf8103 | -6.19235 | -45.44213 | 2025-08-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 104043f6-33df-30c0-9b20-02bd54dd6d37 | -8.99977 | -60.52172 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f144d784-a43a-35f5-8ffd-68b3ebd9ad51 | -9.16357 | -59.61752 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87770afa-8203-3f72-b72d-85e0ab448c6f | -10.82672 | -45.32948 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca98833b-282f-3e07-9c18-c22320d73923 | -13.58877 | -47.78467 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5ead61f5-82d1-36dd-b10f-af0af835b94d | -8.6692 | -51.45938 | 2025-08-17 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fa930ca-ff96-32b5-9b4e-f925d44e61ba | -9.9298 | -60.46898 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3ad4afc-40c7-3a7e-8e28-47605ec342c3 | -8.99832 | -60.52729 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebae6927-d970-3936-9d93-ab541d71b830 | -11.37347 | -55.42525 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 279700b1-0ee6-37b4-9bd3-861b20afcb53 | -8.30932 | -55.09952 | 2025-08-17 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b0b969bd-f639-3e7e-b895-695ba44d9134 | -8.80002 | -52.0687 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 55eac4ab-707d-366a-a76c-632ee2c3b0a6 | -9.55621 | -68.57555 | 2025-08-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd96bbfe-32aa-36dd-9e38-80352172f62d | -10.83818 | -45.32621 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e99aed5-8f0c-398d-b1d2-aea124b531bf | -8.98854 | -60.51626 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac19eeac-fad5-3679-8d0e-755b58c5d46f | -8.99066 | -60.52974 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a7bea16-1716-3b5c-bfd8-f8cb07fb9e0d | -8.98778 | -60.52084 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 021e2cd5-e6dc-33fc-b867-41b852921e91 | -13.43751 | -45.90243 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README26.md)
