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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 712ab2d7-7f5c-327d-b7c6-8527f646263a | -10.9857 | -46.44856 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 12f84f47-50b0-31f5-8a3d-3898964d05e8 | -10.98237 | -46.43803 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dcc8c73-7dec-35fb-9c93-ace3201cfaa8 | -10.98177 | -46.44121 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15854c90-5b84-3007-bb91-742df2caa4c7 | -10.98084 | -50.16222 | 2024-10-01 03:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef6a1b51-d9cf-34e7-a70e-1a6b03796e2f | -10.92849 | -50.09028 | 2024-10-01 03:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0054c44f-1c2d-3340-ab9e-7771c7dee300 | -10.92206 | -50.0889 | 2024-10-01 03:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 12d962ec-e557-37b1-ae7c-3db058c37d07 | -10.92096 | -50.09435 | 2024-10-01 03:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 74ae995d-0b31-3e2a-811d-2c358a3722b6 | -10.91562 | -50.08756 | 2024-10-01 03:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 71316dae-7440-32ff-9c27-7d82dee4c314 | -10.91452 | -50.09299 | 2024-10-01 03:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a5ecd8a9-8e13-3e5d-aa68-6454963fafb5 | -10.90833 | -46.34352 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2541a0fd-6e02-3b56-9d12-ed7430ec5c3b | -10.90776 | -46.34658 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de32a5cd-e12e-307d-aabe-c5c1a04750ca | -10.9072 | -46.3496 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c51b5b1-bdaf-3193-86ce-56a9e54dfa59 | -10.90377 | -46.33965 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc49ebe6-a336-3c84-9ec5-6fc51582ce92 | -10.9032 | -46.34272 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 523c4fc1-26c6-3d11-ba85-b43e8b399bee | -10.77779 | -48.75143 | 2024-10-01 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7294ed67-ea97-38d4-9ef2-0c38293c48f8 | -10.77692 | -48.75587 | 2024-10-01 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c8f695a6-5c10-3b0c-81e7-77a916afc3e3 | -10.52718 | -46.04427 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 08f5c6bf-0c29-397f-afa7-4db3ba7efc4d | -10.52215 | -46.04328 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f05757a-40a4-3ba8-bda0-410c6a9fa5a8 | -10.5171 | -46.04242 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19e428e9-49b2-3073-adc0-4bdaafc30239 | -10.51205 | -46.04158 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 960c549d-aacb-3781-b45c-25de0dac6c26 | -10.50644 | -46.0437 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a51a8f6-3958-3d49-88ea-dda9b0390bda | -10.50588 | -46.04673 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7145babd-7df8-3755-9be7-4adc3816afa2 | -10.50346 | -46.3151 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88e009b4-9e5a-376b-b0a0-7cd26bb1c909 | -10.50026 | -46.04889 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9ad027b-4802-31b2-877a-32f2afe2c839 | -10.49949 | -46.30786 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3620ee3-a3e9-3b83-90b9-975b89883ba0 | -10.49889 | -46.31105 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 346ec6b4-a858-3e1b-8e29-8ab5f582b173 | -10.49437 | -46.30685 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 395cd09a-30ce-3e20-bec5-f3cd2b808d99 | -10.48986 | -46.30254 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2533a379-6836-338d-b024-95d5f9db7661 | -10.45487 | -48.22962 | 2024-10-01 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2708f8c4-1192-3d94-80b9-52e1b030b5b6 | -10.45394 | -48.2345 | 2024-10-01 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a60000d4-f06f-306b-b28c-699b290c502a | -10.38509 | -46.17088 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da49da5d-7d65-35b4-9288-5aa462342243 | -10.38454 | -46.17382 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f001e9a-acc4-357c-be37-69460d8136b3 | -10.38114 | -46.16381 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26834011-6265-326f-8a0d-f79b98978703 | -10.38058 | -46.16679 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cea1245e-2296-3831-bf5e-cae783e051e4 | -10.37608 | -46.16271 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01c5a0c3-b2ae-360b-a807-fe6dc327d0b7 | -10.37552 | -46.16567 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 309f7db9-902d-3fee-9363-12e1e8acde66 | -10.35022 | -46.16019 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6d6201d-8c32-31c6-b4e4-4f28fdbcb9cb | -10.23003 | -47.81277 | 2024-10-01 03:49:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57425f34-3ff1-331f-af5c-71a3ffeb3f11 | -10.22928 | -47.81673 | 2024-10-01 03:49:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ce20662-79ed-3527-9375-d758fdc5742e | -10.0453 | -50.29429 | 2024-10-01 03:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2a73435-1c6d-38a4-a89a-87ff04f941b9 | -10.04414 | -50.30011 | 2024-10-01 03:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17327cb0-abcd-3549-bedc-c4d940cbbb8a | -10.03868 | -50.29292 | 2024-10-01 03:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| addc01b1-d226-3fee-aacb-4c59b923ea48 | -14.48967 | -45.23299 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41240835-fb56-3cfd-adea-d7306855fbfc | -14.48884 | -45.23753 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df6ca7ea-51a8-3f92-8b7d-78c34e947cc1 | -14.49966 | -45.25381 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35eb1d95-b030-3d5d-b963-7cf7aea71e99 | -14.49881 | -45.25842 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a3951bf-7ba1-3d76-b7ab-ab5ee89a054a | -14.49688 | -45.24383 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd16fe90-7682-3c87-b141-cf7911627313 | -14.49329 | -45.23835 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0135bde2-7956-3ff4-ba47-8d2a8a56faa2 | -6.25928 | -42.71739 | 2024-10-01 03:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dd61e4fd-f4b8-3584-843f-67c54e24fb37 | -14.59535 | -41.18852 | 2024-10-01 03:49:00 | NPP-375D | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1e46a0ca-ae6b-3a65-9ef3-c17f83b5435b | -11.56259 | -42.18096 | 2024-10-01 03:49:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 11724339-614f-3d92-bacb-7eae695aaa54 | -7.23777 | -39.39086 | 2024-10-01 03:49:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 63e1a0cc-caed-306c-8084-523678850d01 | -7.07604 | -39.14211 | 2024-10-01 03:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b36b89bd-4ba2-3e7b-82ca-1530389e1139 | -7.07542 | -39.14598 | 2024-10-01 03:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d7e26850-4bbb-3777-995d-c4bdadc6db0c | -7.07193 | -39.14544 | 2024-10-01 03:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e403b71-021c-3b99-b178-07840c3a0526 | -6.93433 | -38.13602 | 2024-10-01 03:49:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54f48211-aff9-3930-b2cf-724150836474 | -6.79984 | -35.23507 | 2024-10-01 03:49:00 | NPP-375D | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad958dd2-8469-3ffb-8319-9568998e8e02 | -5.99415 | -37.83232 | 2024-10-01 03:49:00 | NPP-375D | UMARIZAL | RIO GRANDE DO NORTE | Brasil | 2414506 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8aad47af-f905-31c5-8140-0d5396dbb47a | -5.88129 | -35.49286 | 2024-10-01 03:49:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9e7fab80-34f8-3a96-9b18-e1481a409cff | -13.43218 | -40.69189 | 2024-10-01 03:49:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5e701fde-9258-35ed-a49e-a4704da19250 | -13.31608 | -40.9758 | 2024-10-01 03:49:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7c272ebf-95e7-3069-b599-695df226510d | -11.55874 | -42.18029 | 2024-10-01 03:49:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 056c922c-bf31-3baa-beb6-4e5fda18da9e | -15.44886 | -43.61979 | 2024-10-01 03:49:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c5fd0f2e-03f1-3da8-8482-b67018e4d162 | -15.44794 | -43.625 | 2024-10-01 03:49:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 085b8c88-22b3-3d39-8fb0-9681badb432c | -15.41013 | -44.30182 | 2024-10-01 03:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 62931454-9780-3fa2-bca5-450d8a84755d | -15.40601 | -44.30101 | 2024-10-01 03:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a6d48064-0f04-309a-b147-493dec66a65b | -6.78976 | -40.14276 | 2024-10-01 03:49:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d1ca4ea0-f8b8-3344-911b-52b07fcb4e2d | -6.64049 | -42.10363 | 2024-10-01 03:49:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd211d07-2191-3a28-82b0-d6983b07fabf | -6.63895 | -42.09968 | 2024-10-01 03:49:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 77e4ff67-c7e4-3545-8f7b-d809f071008e | -6.63832 | -42.10349 | 2024-10-01 03:49:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4db2ef14-2dab-3830-9ef7-10ff66aed5ce | -6.6364 | -42.10275 | 2024-10-01 03:49:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ee8d785c-9135-32b4-a295-40744046a051 | -6.25999 | -42.7132 | 2024-10-01 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6434fdc6-ad4d-3ae2-9f7c-ee391d77d6b2 | -6.18571 | -42.96432 | 2024-10-01 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c32d4d0e-56d5-3ed8-9ce1-09cb5edb3472 | -6.18497 | -42.96861 | 2024-10-01 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fc2bd5f4-cf1b-36c0-9b2e-118f59adf0dc | -6.18128 | -42.96371 | 2024-10-01 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c34f583b-e556-34d2-a471-67818e3de722 | -5.9587 | -43.27185 | 2024-10-01 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0cde1559-7a0e-35cd-b5ef-ff523c5cd19e | -5.95495 | -43.26654 | 2024-10-01 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9ac0693-6655-3e30-ac5d-92fcf9434cd3 | -5.95419 | -43.27101 | 2024-10-01 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d1f1506-7428-35ba-bb22-8c0eb886b427 | -6.70217 | -43.05098 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4b3e1b4b-bf85-36c9-a6f8-4a56bdd8c4f6 | -6.70211 | -43.04929 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d2d9133d-7d39-34f8-926a-b875dc84e5f6 | -6.69849 | -43.04591 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 656da433-9202-3cf2-a2d5-c1046e91074f | -6.69846 | -43.04425 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 635f7a22-4946-33bd-a3dd-e0c37092bcb7 | -6.69778 | -43.05019 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f1b6fa11-7ef9-34ed-a2ce-b2242a07b25d | -6.69772 | -43.04852 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 79e0db63-3c24-3a2a-a6b4-1867b14b5698 | -6.69698 | -43.0528 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d654d20-9f63-39e5-9f7d-a152b14cc482 | -6.6941 | -43.04515 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b24e8aa-460d-3a2f-9bf5-818a8b6f2daa | -6.69339 | -43.04942 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a11e5ace-cf0b-3e40-ab96-21ca3826d3cb | -6.69333 | -43.04776 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c47680d2-424f-3900-ae9d-4904bc75a435 | -6.54262 | -43.03685 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 604c4597-3a51-37c2-bc48-9be29a7022f8 | -6.54191 | -43.0411 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 4f4ad485-f9e1-3a52-8b71-8c9e87618eeb | -6.53822 | -43.03615 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c701764a-781f-3397-af3a-6c87dc7d26df | -6.5375 | -43.04041 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c7ed65d9-dd4b-31d9-9196-c0a233f6ee96 | -6.5036 | -43.15931 | 2024-10-01 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8063fe91-cabc-3ceb-ab65-6b5212119699 | -4.84286 | -42.77222 | 2024-10-01 03:49:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2daac77-07f5-39b6-ab98-b3cfde4c4175 | -4.83843 | -42.77142 | 2024-10-01 03:49:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da82c803-886a-3037-86b6-6befe4636242 | -13.4495 | -43.77891 | 2024-10-01 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 233fa7fc-98bc-3034-aa15-63d98e69ddc9 | -13.1743 | -45.45355 | 2024-10-01 03:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e228a95-60c0-3de6-88e8-221cb5e7b1f0 | -12.4335 | -43.74498 | 2024-10-01 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfb87edb-dfb8-3758-ac8b-89547a7bc51e | -12.07129 | -44.95526 | 2024-10-01 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce101426-b72d-309b-b35b-ebb32207d30d | -12.07045 | -44.95994 | 2024-10-01 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README45.md)
