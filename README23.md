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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de0f542d-988f-3a4a-800d-7229da9f8825 | -10.86523 | -45.36439 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51f06c21-b32f-361c-b200-84dff6e3648a | -11.24833 | -45.15142 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29dffd67-29bf-3cf6-b618-2a86aefb3a7d | -11.18885 | -45.03783 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 905ac042-da9b-39e3-bd60-b3aa4be5b444 | -12.89225 | -45.82952 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22d29c8e-2cd4-3d07-89e4-9d084cdd1e3c | -10.03636 | -44.70296 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0ac3c9a-8421-3d3e-9369-0793c78f243f | -10.05235 | -36.2149 | 2026-09-01 03:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 7afcfd2c-75fb-313a-84ae-6ed127c917b8 | -11.27259 | -50.57503 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 75852b45-8721-32d6-94e3-292940e5f29f | -12.07047 | -44.99659 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8bdeb2e-2525-3524-84af-0c5a9a4e18c5 | -12.88017 | -45.84231 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4abf501-72a2-3d37-adb6-61788aec0f11 | -9.45479 | -45.62617 | 2026-09-01 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6442e3e5-4cb2-3431-b4e9-c44bbb837530 | -10.73071 | -47.95983 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4a50231-8ad0-3e9e-96b9-84150d994f79 | -10.02518 | -44.68674 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4fa8ca75-4143-3172-9833-4dfa6bde40e2 | -11.1038 | -51.54477 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 074bed24-2a9c-354c-a9da-a9a5a83aff9b | -10.02436 | -44.69136 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 351f3b7c-cf91-3534-8fd9-eb704a115ebd | -10.82349 | -42.36701 | 2026-09-01 03:55:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 9e07bbcb-2137-3ce4-bcb1-662dc7406e1f | -8.91184 | -45.04868 | 2026-09-01 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e108bed-3c50-316e-959d-8fc7e826d4db | -9.9972 | -46.44317 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2164ba9a-dd0c-37ce-9496-43740af51bac | -11.48436 | -45.09999 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e88f3d0-a8dd-3419-b2af-1ecf2154171d | -13.5449 | -48.24395 | 2026-09-01 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59dd07d9-36d2-3f7b-88da-1f52eb561aef | -11.66568 | -47.61588 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0efcc770-a3f8-3252-9c21-f7484886f973 | -11.2124 | -46.08555 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0c201ce-866e-3eec-be29-2f98d0b24a90 | -15.18996 | -46.22731 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e1f2760-2bdc-3dd9-8d21-dda9ec5044ad | -10.74893 | -47.98558 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21b3ff55-c3ab-391f-b851-7dd2843fcbe1 | -11.11064 | -51.54615 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5677d5e6-2d0e-32b9-8f56-622794f9451a | -10.32396 | -50.04292 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5d567c9-1472-37d3-8967-2a5613a4d6c4 | -10.19634 | -50.31736 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da273eab-4d9b-3d22-b031-81e8288c41ff | -10.32499 | -50.03764 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 336e74b5-e661-35e1-b1ec-876505ee0cea | -11.37102 | -45.23003 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e34f2da-acf5-3b6b-9b5f-6b49f07c9366 | -10.35754 | -50.00621 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| de2c404e-e740-3e5c-a18f-a2aaa0d909d6 | -11.29174 | -50.61383 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16933ca5-34ac-392d-95ce-bf37dff1d276 | -7.88434 | -47.07654 | 2026-09-01 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c0ea190-cd7d-3428-a7e1-0d1366c5ad6c | -10.8559 | -45.36254 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5106ad8d-e946-36d8-9cab-826bb3ea0444 | -7.41923 | -49.74131 | 2026-09-01 03:55:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 748d7b32-0741-3e4a-826b-426f3e8b1bc2 | -11.66427 | -47.59399 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 509862d0-bb30-338e-9211-d9dbb25f061c | -11.66671 | -47.59587 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef182484-f71b-3d3b-ad36-9b0a34962bc0 | -11.47779 | -45.08197 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7c503b1-7be3-3ca9-950f-f55ff5ddb14c | -8.41517 | -44.99251 | 2026-09-01 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e16a1153-e7ff-3af4-8c4c-dc41f978a506 | -12.10116 | -44.9804 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| adb232a0-b718-3d4e-ab74-87d044574cd5 | -13.19818 | -44.07291 | 2026-09-01 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49e9e679-018a-35bf-ae16-4125c9778a4a | -11.65099 | -47.60555 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b1bddd6-6b62-3b17-89a8-99aa7b263d80 | -11.51934 | -46.93109 | 2026-09-01 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8cee50a-fcf4-3a24-88a7-8630ef41726e | -11.52539 | -45.49849 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64f51f96-12fa-388f-b6c1-b459e871be91 | -11.9102 | -45.0653 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60282529-aa12-3075-b91c-f9b9c3f1fe0e | -13.19122 | -44.07605 | 2026-09-01 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dd930cd-4842-3219-8fca-a0f8e6b5b8ff | -10.75372 | -47.98133 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d7f44219-8192-335b-8459-e25edd501795 | -8.41997 | -44.99314 | 2026-09-01 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 868f2e7d-9d58-31dc-ae97-0bcf1014f4c7 | -10.35796 | -50.01296 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 55c06039-5238-3aa6-9529-70e94800f65f | -15.17267 | -46.24694 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 686f8340-487a-3f8a-ac91-7f8471753f9c | -11.2508 | -45.13766 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55fe170e-52cc-34cf-bae8-d096fce8c6a1 | -11.27371 | -50.56952 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1bc04041-d270-3bb7-b91d-31dd2c8c3a3a | -12.91182 | -45.82799 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f6ee4be-d6c3-3fc1-af30-b79e592d30b2 | -10.82502 | -50.72131 | 2026-09-01 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9551f5ed-9402-37d8-ad52-b1be6f87c563 | -11.3094 | -45.20334 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25779550-c832-373f-a969-c7862720a83d | -10.20308 | -50.31565 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8d50c526-8211-3871-a5be-a827066ac080 | -8.87944 | -46.02023 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b1c251a-2dd1-32ae-904a-11f87c4ea5cf | -9.42841 | -45.63281 | 2026-09-01 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3d08244-d022-35f0-ad84-086bb3af4855 | -9.99574 | -46.3942 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f27134a4-397c-308a-984a-1e2fdfca1f95 | -15.18525 | -46.23069 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 668f82a2-c0e2-33bf-b57c-11314280eed3 | -11.37017 | -45.23484 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 078dc8be-3c2c-3f1f-8b95-dbf628887fd0 | -11.11195 | -51.53975 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ac5e7e3-13b0-3918-8500-3c1617ff8a4b | -11.93487 | -45.06585 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21898823-70d1-3d8c-abcd-450482ffdc65 | -11.31188 | -45.1898 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c042d522-03d6-3312-81bd-01c06f8100de | -10.82719 | -50.721 | 2026-09-01 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b805a44a-ac66-3ca8-9a14-4b2c7e176408 | -10.05685 | -36.20809 | 2026-09-01 03:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 2ef0e7b3-26f5-3081-b1ac-0b48afc0af7f | -11.27742 | -50.58298 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| c994c3ac-a17e-3b9e-a7ae-00269df95c0d | -11.93749 | -45.06868 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 57ee19a5-de76-32b4-a789-ef8f2133a85c | -15.18987 | -46.23137 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c30772eb-e088-3b97-996b-bce7b01f44e6 | -10.82265 | -42.37187 | 2026-09-01 03:55:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 24c2e7c5-085d-361b-b141-b3c1b9a7b7ed | -11.37481 | -45.18227 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd14f081-462f-3029-bd2f-227acee31de6 | -10.03264 | -44.69751 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f54e8a2-de9b-388c-8c2e-0dfa49e29bb4 | -8.77343 | -46.45267 | 2026-09-01 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa3894e4-345d-306e-a777-241f763c694e | -15.19085 | -46.22272 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0a0202b-6f56-3ef6-a2d1-8f6a13736bbb | -13.3263 | -51.73035 | 2026-09-01 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 667e52c7-ccf7-3133-bde0-9c055bc2de35 | -9.40565 | -51.68133 | 2026-09-01 03:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc83d454-c8a5-3576-a48c-b2f2cf288f89 | -11.90683 | -45.08396 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22f48437-71f8-3fcc-abff-69a74d2df358 | -11.29334 | -50.60365 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 930ffce4-4302-3a6c-9230-4df46c1058d5 | -10.35652 | -50.01146 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b5a19605-f2e6-3b85-871c-61453006af3c | -11.20858 | -45.10989 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67083152-78c2-35a4-be1d-045707544451 | -10.05629 | -36.21176 | 2026-09-01 03:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| a166d06e-3c00-31cd-bcdb-04d196fc22f3 | -10.78143 | -50.51077 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef9c2847-f7db-3e20-8ea0-18d0e6afed28 | -11.67076 | -47.60349 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c54c5112-0575-3fcc-aed9-340d2f51911e | -15.18444 | -46.23119 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f085543c-3297-3073-9aac-b6c76edc4174 | -10.85872 | -45.37363 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5e19ab3-6f2f-37e2-abcc-09692f178ae9 | -11.66966 | -47.59476 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb70c9fd-8969-3993-b75b-78d4e25955ee | -10.05402 | -36.2039 | 2026-09-01 03:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 5a182362-2a92-3bd0-8a77-203562a8c12b | -10.75232 | -47.98851 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c2c56bd-8126-3c1d-a9cf-8cd17b093c90 | -12.07286 | -44.98372 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8053e8e-ef19-3e62-a34e-5550db4b0e67 | -11.48233 | -45.08281 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 88e270c1-3e7f-32e3-88d3-d50a2d190b6f | -11.31315 | -45.20882 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4931ea5d-ff18-30a8-8181-275c6d3e1e6e | -15.18085 | -46.24956 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 971b2abe-e0da-3938-b0d3-b3767f84a1b5 | -11.48526 | -45.09521 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b355899a-f3d6-397a-ac8b-17898af3cc0c | -11.29617 | -50.59169 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d5a42871-5242-3207-865b-f3985cd27dd6 | -7.87869 | -47.07991 | 2026-09-01 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df18a7f7-749a-3481-826d-9197aebde5df | -11.24915 | -45.14685 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cae74feb-237d-3008-80f5-fa00cb6225d8 | -11.27148 | -50.58055 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2f9c0e30-9bec-3c86-9dea-455d3ef731e0 | -15.21464 | -46.22268 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54fccc6b-4d3c-39ee-8349-bab7e69266c2 | -11.48063 | -45.09225 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e567265-760b-30e3-a063-545ae99feaf2 | -13.3498 | -43.67532 | 2026-09-01 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b832e41-ee8e-3263-b542-f247a5de9075 | -13.19532 | -44.07695 | 2026-09-01 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31c5a1a3-f4d5-358a-a3c2-cd07233f3839 | -10.01983 | -44.69053 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README24.md)
