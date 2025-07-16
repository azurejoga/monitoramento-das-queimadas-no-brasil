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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fdad3a5-dcab-313c-a398-9bd2ab70477f | -8.51289 | -43.30263 | 2025-07-16 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 91d8eeaa-c642-3b17-b2e8-22cee4cf4c02 | -3.99892 | -43.24027 | 2025-07-16 03:49:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f199dc85-f37d-3a35-ba22-2272fc139368 | -7.35353 | -45.66935 | 2025-07-16 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5fa0ee9-5b2b-3575-85b3-f140a26dd6c5 | -6.7324 | -44.33117 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| de3e3dc9-2e28-368e-afd8-b64cfe3563cd | -5.53107 | -43.88038 | 2025-07-16 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56d1de6f-b218-3158-ba4a-ec310a2a8930 | -7.10758 | -43.65223 | 2025-07-16 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec6b8a5d-df35-366e-886e-7fbe8bbba069 | -7.21366 | -45.33302 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79450d33-a000-3791-927f-8494a479b467 | -4.96209 | -43.22509 | 2025-07-16 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fa0439b-cf8a-308e-b392-4f2c8aecb845 | -3.38528 | -47.48365 | 2025-07-16 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15926dd3-21bf-3c77-a090-7ed269e56db6 | -7.04922 | -43.47981 | 2025-07-16 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65fd2f47-6950-3c69-a01f-cf353ae9c677 | -7.10227 | -43.65607 | 2025-07-16 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40430ca1-eaf4-30ba-8390-2a34d99acda5 | -8.50714 | -43.28469 | 2025-07-16 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a63b732b-3292-3366-a02e-edfee3c11397 | -13.0146 | -45.0593 | 2025-07-16 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c18b1376-4a96-3256-8ee5-39007c35def7 | -13.0339 | -45.0561 | 2025-07-16 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a27e0c41-a84b-30d8-8059-22f34f4fc594 | -6.5631 | -51.1126 | 2025-07-16 03:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| d245c823-21f9-3346-b932-cd0628f09a7a | -20.0805 | -47.6319 | 2025-07-16 03:50:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 3565550f-ecfa-320c-aa11-36567e63cc0f | -10.5696 | -49.12196 | 2025-07-16 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f54f5685-57a3-34b9-b942-6b1fa02b9ef6 | -13.0516 | -47.80625 | 2025-07-16 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1c90bc9-1713-3958-b9e5-a28baddef4ea | -12.58658 | -44.7986 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56391d1a-4043-34a1-9083-7eed8f81af43 | -8.91075 | -47.34717 | 2025-07-16 03:51:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dda7e31a-16d9-3a9c-bcc0-74c278888fdc | -12.017 | -47.78003 | 2025-07-16 03:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e964a6a7-0338-3ff5-aea0-9722d40ec804 | -12.07423 | -43.48365 | 2025-07-16 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40ecab95-636f-322d-aacd-49f3d8dc827f | -10.22746 | -44.63107 | 2025-07-16 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c95876d9-a8ee-3372-b48c-58a79088b56b | -8.651 | -47.74932 | 2025-07-16 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 309692b5-b9cb-3e10-8027-1065b227c6a7 | -10.64929 | -44.48498 | 2025-07-16 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fa61cec-eaec-398e-a189-c8de87ac6341 | -11.47114 | -47.31488 | 2025-07-16 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc28af3b-ac86-31ab-9984-8376b0c8dca5 | -13.02136 | -45.06681 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9560cd1a-739c-305d-b806-8d1afe2453f4 | -12.49061 | -46.92278 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f2d6e99-314c-3921-9b2a-84cea1abada2 | -12.02863 | -47.77863 | 2025-07-16 03:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 754b901a-d1f2-30ad-b0fd-a9f6043a2a23 | -12.49001 | -46.92587 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a20db64-919f-3372-aaae-071ffcf70aee | -10.28424 | -47.61742 | 2025-07-16 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b73188c4-df5b-3470-ae9a-e555c13ff3c4 | -13.01238 | -45.06505 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 21ec3228-309f-357e-aec0-789f5ca63d59 | -13.16571 | -50.77211 | 2025-07-16 03:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 049d1789-c7dc-3953-abc1-0ed35e80ddf5 | -13.01853 | -45.05675 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a9374142-d307-3b0c-a9ba-878f9d5e9f81 | -11.45818 | -48.16241 | 2025-07-16 03:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2376aeb2-7a8b-38d3-b5a3-316933bccd09 | -12.47279 | -46.93217 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e6a9950-8a79-3f93-8ae8-a6c96e5eefb5 | -12.56977 | -48.88778 | 2025-07-16 03:51:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a3afe6e-35db-31f4-9454-1a603517cc3e | -11.99538 | -43.36616 | 2025-07-16 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5484cf4c-b19e-3ca8-8ebd-209163f9d457 | -8.65021 | -47.75346 | 2025-07-16 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 020cbae2-eb07-3800-8ef4-61ae5e1a4034 | -11.45399 | -45.0998 | 2025-07-16 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c875978e-4ba7-3e70-925d-5fcdb33959cc | -13.1274 | -43.48945 | 2025-07-16 03:51:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82f6f41b-f485-345d-86f7-bdede03a8e1d | -12.99116 | -44.87838 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 724f9913-3416-333a-922a-42ad5cf5a566 | -12.47914 | -46.92696 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d8e51b1-96cb-348a-aeb5-2cba3479c80d | -11.47245 | -47.30805 | 2025-07-16 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9259d64-cbdb-3089-93d9-3b391d71d2ee | -13.0 | -44.88026 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a244b61-3924-3a04-a486-8b0905380b76 | -8.76165 | -46.5936 | 2025-07-16 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b4d6c07-512a-3f9d-81dc-1e9839f4a907 | -8.75816 | -46.59999 | 2025-07-16 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8dc312a1-4d38-3587-99ed-bc3c0a35b06b | -13.20851 | -43.12809 | 2025-07-16 03:51:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fd29a98e-0bb1-3380-bd92-b51f81ccb783 | -9.3141 | -44.84775 | 2025-07-16 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad2e74c0-4f33-30da-8347-1afc8c27f7be | -13.02219 | -45.06223 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4f3b1455-c163-3b98-8d4b-09065b493622 | -12.48307 | -46.93417 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5f4e6c2-7bd8-3f0f-84ef-3d6383a8379b | -11.47049 | -47.31829 | 2025-07-16 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d86a31ce-c238-399d-bffd-5d43377476ec | -8.7594 | -46.59307 | 2025-07-16 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64e5c47d-59e5-36a8-912f-68882b71ebf8 | -12.47733 | -46.93628 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cf78b21-8d29-3832-be50-85dabdd99e1b | -12.8209 | -38.41913 | 2025-07-16 03:51:00 | NPP-375D | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9c42e9ff-b092-3e90-a599-6cb88ae0b36a | -8.75497 | -46.59966 | 2025-07-16 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf77d4ff-db5f-34ea-bb02-2fa00b374b14 | -13.02375 | -45.05975 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bcddb28b-b453-3474-92f2-8bfe1f74b3f2 | -14.1541 | -42.84409 | 2025-07-16 03:51:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2df0111-37d2-30ec-97cd-0e3ae06e865c | -13.36989 | -42.50148 | 2025-07-16 03:51:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 723b7ad3-aae0-394b-bd61-df994a196bb3 | -9.30938 | -44.84688 | 2025-07-16 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c3f3657-1508-32cd-bb82-23d22d2d1720 | -11.186 | -48.62902 | 2025-07-16 03:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5388a59-bdbc-39b5-9ea5-381b51907b51 | -10.38987 | -49.7558 | 2025-07-16 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7b1ad389-54ef-3ed8-9db3-a1b25a715deb | -10.65248 | -49.47565 | 2025-07-16 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb527faf-d0f4-3f94-b8ce-ee91331d86be | -10.22285 | -44.63038 | 2025-07-16 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3256d69a-906b-3bad-ae0d-321c2ef528f3 | -12.42062 | -43.75437 | 2025-07-16 03:51:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 89ffad38-c6c5-387c-b2ad-92c34d0e7716 | -8.65143 | -47.75185 | 2025-07-16 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e01d9c27-8940-309f-a2e3-29a6f890c376 | -10.9669 | -49.25196 | 2025-07-16 03:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ffcbbae-6f09-381a-8b1e-652439af01de | -12.47349 | -46.92288 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfde2fea-c980-37b2-b784-bb16645e84d2 | -11.59019 | -47.31294 | 2025-07-16 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68795ade-3d30-39d4-beaa-589c9ecf6822 | -10.28057 | -47.61723 | 2025-07-16 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 54b3dc4b-de76-34fe-a04b-c6d9fd066ca1 | -10.27865 | -47.61641 | 2025-07-16 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88136778-b349-3764-af06-3401e7f13cc4 | -10.64624 | -49.4745 | 2025-07-16 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94aa6cb9-7d77-3301-95dc-4671e4fb27e9 | -10.65458 | -49.48202 | 2025-07-16 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebd58ca3-3c95-33f2-9907-65b2101fd9a0 | -11.78079 | -45.21634 | 2025-07-16 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33570074-f522-3fa2-9991-24c5ba926b7b | -11.95525 | -46.75134 | 2025-07-16 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 659decdd-4486-36d4-8ffa-5562d3dfea42 | -12.58148 | -44.75133 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9e02c61-bdf1-3d7e-9eef-e1daa499f257 | -11.95226 | -48.41506 | 2025-07-16 03:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6481c78a-2634-3ac8-a8a7-12e2956eb2bc | -11.49012 | -48.07662 | 2025-07-16 03:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bba2667b-991a-32de-a645-73ec22e3164a | -12.99197 | -44.87397 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7776c62d-eff8-3f50-864e-f79809546453 | -9.2952 | -44.84428 | 2025-07-16 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46a15781-20a8-3735-b572-b79bb342f724 | -10.64527 | -49.47945 | 2025-07-16 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2d4ee2a-28da-3830-9efa-5eb9ce5120cf | -13.12401 | -43.48505 | 2025-07-16 03:51:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15371f7a-f03e-3732-a743-4257f943dd4a | -12.48035 | -46.92073 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8584e7e3-92eb-3a89-9804-0364437ad85b | -11.4671 | -47.30695 | 2025-07-16 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3341fbf9-4e1c-3fa2-b8f0-86dfe7131758 | -10.56675 | -49.13641 | 2025-07-16 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6f78722-5aec-3004-b732-98c65c743eac | -13.01603 | -45.07052 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 745785cb-1abb-331a-95eb-847edc94af72 | -11.95126 | -48.41689 | 2025-07-16 03:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cfd80e50-10a5-30ad-933c-0adc3a7baadb | -12.46948 | -46.92183 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01e69c65-80ac-3afd-9830-03156cdc8800 | -8.75562 | -46.59616 | 2025-07-16 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e474261-bce3-3927-bde9-ff2302bdd7dd | -8.53593 | -47.85466 | 2025-07-16 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4d3f497-4347-3078-8321-331e9f2ecd5b | -9.84998 | -47.88097 | 2025-07-16 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adca4fd9-888a-3f0f-a1d2-527d52e28392 | -8.90582 | -47.34239 | 2025-07-16 03:51:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27cbe01f-7962-36c0-8a57-65d6d3f6f2fb | -8.53702 | -47.85638 | 2025-07-16 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 106907e8-a791-3426-a3a7-4905a4c77a96 | -13.04977 | -47.80598 | 2025-07-16 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe3f4245-f33f-33b0-8e03-4972bd3ef663 | -10.89765 | -49.22107 | 2025-07-16 03:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea213e14-6e9e-3007-83d6-3aaa7e307e3e | -13.05461 | -47.80986 | 2025-07-16 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc4d31b6-a62e-3d4c-955e-03218dde487b | -12.02248 | -47.78107 | 2025-07-16 03:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a90fd8bb-c828-3055-9896-641a733364ff | -12.07073 | -43.47941 | 2025-07-16 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f19dc0c-5b7f-37d8-8593-71483f6d59dc | -8.76036 | -46.60052 | 2025-07-16 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82f85f29-7b10-31f7-a9e6-6388ce63da3d | -12.47974 | -46.92384 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README11.md)
