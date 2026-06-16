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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a81bc95a-1c64-3ea1-a14a-22942b13ff17 | -9.32045 | -45.47775 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73d54c05-3623-3351-9a15-393b1ef5d76b | -12.13252 | -39.41135 | 2026-06-16 03:45:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d7156c80-88f7-3722-ada8-e4ce64f597b4 | -8.97971 | -47.97945 | 2026-06-16 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b34729e4-6684-33f7-bc26-b26a05931801 | -9.34854 | -45.47925 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e89bfd44-af63-3026-8196-e0582451b7f1 | -9.22992 | -48.594 | 2026-06-16 03:45:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9a6385f-e9df-3996-9a84-a5a41efe321d | -10.54995 | -47.03259 | 2026-06-16 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbec7d9d-cbc5-35ff-8933-2a2735f62b53 | -8.93437 | -46.96162 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f07272c4-d51d-3120-af9a-a7b1fbb9bf22 | -9.22446 | -48.58662 | 2026-06-16 03:45:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de7f0933-9723-3045-8f6a-691d2f372a9c | -13.56321 | -47.85515 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55e35fc4-5353-35d5-a1b2-06809ef50e8b | -12.85149 | -44.37302 | 2026-06-16 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| a1b3fa98-16db-3343-bd49-d502ef27634a | -9.26462 | -48.57804 | 2026-06-16 03:45:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 635d1aa0-2d5d-3283-896a-6b74cac95011 | -6.83285 | -47.90691 | 2026-06-16 03:45:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e32f176b-d915-3143-83ea-640a957eca9e | -8.93679 | -46.95449 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9df92291-2333-3cbc-9cd0-e18d25c6371d | -12.73782 | -46.30349 | 2026-06-16 03:45:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd234e2e-3041-31ad-b516-5357570e5268 | -14.72084 | -42.94292 | 2026-06-16 03:45:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b9ceb1c2-672a-32cc-96d8-bfbe3d3ce90e | -9.33758 | -45.47722 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 73054ec8-b8c4-353c-99db-f63208b03983 | -13.81427 | -43.64616 | 2026-06-16 03:45:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d99ebf9-9333-3207-ab37-3c684b9fac18 | -8.93524 | -46.95694 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aad2989-c962-33c6-b434-cdcade99d65c | -14.1558 | -41.95943 | 2026-06-16 03:45:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 447ede0b-af20-3829-ad2c-a23212c54935 | -18.96622 | -40.37476 | 2026-06-16 03:47:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b16b8bd1-7c61-3d5e-b378-7387c4b6131e | -18.85472 | -40.24849 | 2026-06-16 03:47:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2443ae1e-5a0d-3a1a-a006-9142511fd545 | -17.71617 | -39.75475 | 2026-06-16 03:47:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5807d168-c32a-346b-83fa-aa07f3f6e3c0 | -17.80498 | -46.69999 | 2026-06-16 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5de198ff-4cbb-358d-9af7-2ad81fe47553 | -20.82091 | -45.17704 | 2026-06-16 03:47:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5bea931b-493b-304b-9d5b-b268b14bbcbb | -17.80434 | -46.7031 | 2026-06-16 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2777a678-de00-3c87-b237-2e3aef2be26f | -12.8548 | -44.3625 | 2026-06-16 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 6fa3b771-711e-346f-95ff-49d31557cd0c | -12.8548 | -44.3625 | 2026-06-16 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0e30bbfe-e6f2-3daf-9f52-f926c542123d | -12.8548 | -44.3625 | 2026-06-16 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| fffb1713-6328-3e31-8891-ae4bbb9fc12a | -5.84104 | -43.49082 | 2026-06-16 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 03f30791-3fbb-3185-9793-d3e7b7cb6943 | -9.35067 | -45.47739 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f11472d3-7702-3e8c-886b-c4447950be90 | -9.33477 | -45.47991 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0875256-137f-358a-aaf2-86de62983359 | -8.94313 | -46.96291 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb72dccb-8fab-33f0-b033-56e01e5b3086 | -8.97597 | -47.98145 | 2026-06-16 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9678cfa6-582c-3941-bb15-944ae71e8b0f | -3.95958 | -43.11685 | 2026-06-16 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 412157bb-3a58-37d4-8847-6680180df00c | -5.58966 | -43.50902 | 2026-06-16 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9be4c50f-e26c-3957-a28e-f06b9d7f092c | -5.58339 | -43.50414 | 2026-06-16 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59e488c3-8ab2-308e-83ee-5ca5402a59b9 | -9.36351 | -46.49315 | 2026-06-16 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1f32cf1-5f73-3a7f-ab3b-17ebfa6de264 | -9.6265 | -49.01838 | 2026-06-16 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a80c0220-737c-3d11-b364-517830daa6c2 | -11.45489 | -48.08441 | 2026-06-16 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ae198c5-8cf4-3d1f-bde5-0253962d21e0 | -4.35241 | -47.76303 | 2026-06-16 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a71a05d8-07ff-3f53-a7f8-49163a970d6f | -9.34636 | -45.48092 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f49289c5-c7dd-3336-be4e-235db8c01e0a | -5.52014 | -37.48638 | 2026-06-16 04:17:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0ec7efe7-665f-368f-b181-1241f0901628 | -11.11984 | -45.13892 | 2026-06-16 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0463a3-1397-34e9-bea4-67352b5a26ca | -9.21202 | -47.3387 | 2026-06-16 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 513c4c7e-0a73-3812-b585-afb7f61173fd | -8.94226 | -46.968 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00d5f32d-25a0-38d4-8e12-3dff768509ea | -9.32395 | -45.47805 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf759ecb-be7b-3612-b42b-11d376d7cba9 | -9.38821 | -40.75707 | 2026-06-16 04:17:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 82f1da82-b6d6-33ca-b84a-c3d14f8a847f | -5.51931 | -37.48378 | 2026-06-16 04:17:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a699a0f-2a03-35d2-82f2-180cb0c2ca14 | -10.50853 | -44.86146 | 2026-06-16 04:17:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0977b03d-6936-3ba6-a25d-22951813a1ba | -8.95187 | -46.95919 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6bc611be-6248-3191-851f-37b494c3d193 | -5.52742 | -44.4193 | 2026-06-16 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 602f8ce5-5e90-3b4d-8507-11d1e49c0c54 | -9.69514 | -48.61032 | 2026-06-16 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8b943bb-f5a0-37ea-935b-50e80f263d50 | -7.76642 | -47.57155 | 2026-06-16 04:17:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6329cc5f-dc2a-326f-9903-49e2ccd8876c | -5.80342 | -43.78984 | 2026-06-16 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0146b57-e802-3e6d-9635-35c67755c61e | -9.26392 | -48.57749 | 2026-06-16 04:17:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36c53db8-8666-365c-aeae-93a18625f09f | -8.95101 | -46.96423 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57731ce7-d734-3823-92ef-b486cb249fbe | -4.35688 | -47.76374 | 2026-06-16 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8fb040a-8e7c-3f3d-b29b-52219369c25b | -9.34198 | -45.48113 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 549a9715-8d31-328e-acba-f5623d83f286 | -9.34276 | -45.48031 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce3200be-daf0-35b9-af55-db2e74d67a96 | -8.95666 | -46.95481 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2b24408-b24e-386f-b344-f660dbdd59fd | -9.22023 | -48.56998 | 2026-06-16 04:17:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5b9050d-3207-36a4-aea8-dd4d7f4d4c81 | -9.36049 | -46.48782 | 2026-06-16 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57a649da-e0c0-3d2d-ba0c-8298e03264ff | -5.32935 | -44.69074 | 2026-06-16 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d1af143-d064-31c9-8092-f8bcfad5ca9a | -5.446 | -43.57519 | 2026-06-16 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e89d1737-c149-333d-ba1e-d64e7247f192 | -5.49394 | -37.24572 | 2026-06-16 04:17:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 97fe2a81-bdb7-39a4-8fbb-1261ae353ab5 | -3.51036 | -48.03951 | 2026-06-16 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54d0a5c8-8140-3e8a-b18e-f9b3a8153bc4 | -9.21142 | -47.34222 | 2026-06-16 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4d10b3f-f7bf-394f-93a4-9114b23b83a5 | -8.98085 | -47.97825 | 2026-06-16 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47aea4d9-d12c-3db6-9e84-6cc5dd53be45 | -9.4629 | -48.39175 | 2026-06-16 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee163a69-1432-3123-9e70-099993291d89 | -12.1323 | -39.41356 | 2026-06-16 04:17:00 | NPP-375D | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c34c79e0-0a00-35dc-b9c1-57238b22419a | -3.50923 | -48.03612 | 2026-06-16 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ae10ed1-19f1-3fed-9278-8112272934d8 | -5.52313 | -37.48436 | 2026-06-16 04:17:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 367e7a9b-e9f3-395a-ad5f-23a669fc8701 | -5.83537 | -43.48225 | 2026-06-16 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3d4f96f-1b0c-34b1-946a-c054c8ba6be9 | -3.95898 | -43.12057 | 2026-06-16 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 531cf5f7-a1fd-3d62-a2ff-64a872ec855c | -11.16655 | -49.25166 | 2026-06-16 04:17:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffb8c6dd-e5dc-32cb-81c0-5dad411bbccb | -5.32866 | -44.69494 | 2026-06-16 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42ea56f0-3e95-3ced-87e5-2c8e48398bcd | -10.2929 | -44.08364 | 2026-06-16 04:17:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 221bf67a-c2f6-32b5-a26b-5e0134d5853a | -3.5046 | -48.03545 | 2026-06-16 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 625e6c6f-2ecc-30b7-b558-d9bb376a3011 | -7.36022 | -49.86752 | 2026-06-16 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51f7d622-f8c9-3ccd-87b9-240a942e8e88 | -9.45862 | -48.39098 | 2026-06-16 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5880ce99-c502-385e-84d7-19676fd09965 | -9.37141 | -48.42238 | 2026-06-16 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ecd128e-35b2-32a8-a074-068404fb8503 | -3.50377 | -48.04031 | 2026-06-16 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6da35148-b492-3542-b7d1-31398ef857a5 | -9.2296 | -48.59354 | 2026-06-16 04:17:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81f7a942-a867-3b2c-a29e-5deec22182d7 | -3.51115 | -48.03467 | 2026-06-16 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de121d1e-fd8f-388e-84af-264952d49270 | -4.35614 | -47.76813 | 2026-06-16 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f19b3466-82ee-33aa-bf50-522b071ba582 | -10.54707 | -47.03337 | 2026-06-16 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 631573e0-662e-3a14-90ae-b4d74c70d19d | -9.33545 | -45.47575 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c4544c9-460c-3e5a-a6f0-7393c198dc31 | -9.32687 | -45.48283 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6651fc65-4416-38bd-8436-15c7628a222f | -8.44897 | -45.55544 | 2026-06-16 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04a16696-2f67-3053-b4ff-ccf4e8fa36c4 | -9.21603 | -47.33944 | 2026-06-16 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ace905c9-4a97-35f5-b939-3d17e5a353cc | -5.58683 | -43.50472 | 2026-06-16 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95b8ba57-4e43-378b-bfdb-10418cb5ae93 | -9.09247 | -46.81663 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ef8964c-25d4-3d6e-84b9-502d52e8d205 | -10.88001 | -49.54288 | 2026-06-16 04:17:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 805593cf-ee03-31ab-93af-0c5c47c4f2a4 | -8.93832 | -46.96735 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 198f0404-60db-34df-9775-7f81396996fe | -4.27981 | -48.36404 | 2026-06-16 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12826743-fb8f-38a0-9593-9515d8967566 | -8.94793 | -46.95852 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acc11456-6ad0-391d-b462-4278880d42dd | -9.26827 | -48.57828 | 2026-06-16 04:17:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b5c5efc-85f9-3f68-ae3a-a9939e2243c6 | -9.36429 | -46.48849 | 2026-06-16 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d94de5d-ac47-3890-a159-8d89036fe23e | -9.22525 | -48.59273 | 2026-06-16 04:17:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3e40408-a0dc-323a-acad-d6c19d92dc46 | -9.78947 | -48.08047 | 2026-06-16 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
