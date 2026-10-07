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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99c2e4c5-5d6c-3c2b-95a3-414860a7fb36 | -6.604 | -41.5863 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5ebe84f0-fcf5-3e13-bc27-acafc001c5cc | -4.84759 | -40.41143 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| b71e2350-a545-357c-baf7-732c6f7928cf | -9.14601 | -45.82764 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8f1f0f61-566a-348a-a913-63d531929e5d | -9.82254 | -52.12395 | 2026-10-07 16:37:00 | NPP-375 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c6d4a6a9-91bf-3c3e-af24-5ebe21cdd442 | -7.2189 | -44.32615 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0ccaa693-8aa5-3f4c-a564-bf555e3b37c2 | -4.82977 | -40.72936 | 2026-10-07 16:37:00 | NPP-375 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8792dad6-f8f4-310e-bdf0-c401a4583c51 | -8.94043 | -47.38782 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 338048a4-fbed-3025-8034-a92fb0403abf | -3.56025 | -39.13295 | 2026-10-07 16:37:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 2ce04677-07e1-30d1-83e1-0ea8d828a319 | -11.09199 | -45.65892 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 04b31dcf-7362-3231-96ea-ef42bd6abfbc | -8.5343 | -47.53098 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fc79314-52a5-3e66-a383-4176f2b91bcc | -6.37881 | -45.04646 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 006760e2-f487-3b8d-900b-7511a431ad70 | -6.65356 | -47.91227 | 2026-10-07 16:37:00 | NPP-375 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 7865b290-5bc4-3795-a9f4-1c253666a1e6 | -16.72589 | -42.04325 | 2026-10-07 16:37:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 63cdaab9-d33f-3a8b-9e12-2a38f95f6e45 | -8.01673 | -47.17685 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0dfca406-7685-3e7b-8b22-eb2f939a1920 | -3.57393 | -43.09915 | 2026-10-07 16:37:00 | NPP-375 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| dc56fa52-55a0-3192-9759-3a49ed79118d | -6.98413 | -40.03095 | 2026-10-07 16:37:00 | NPP-375 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 0ffd79c5-71d7-350d-be36-cde28a66056f | -5.96435 | -41.34753 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 04da8b0d-19e4-3fe5-af7a-0949e1e3a537 | -6.86369 | -39.10232 | 2026-10-07 16:37:00 | NPP-375 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 0753779a-7f33-3020-8ba7-44ecf5e0f330 | -6.23176 | -52.65509 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 15bfde4c-7fc1-38e4-a68d-86e95cdb9330 | -4.57269 | -40.71951 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 8c2cb74c-b451-3142-bde7-7560d4a41ee2 | -4.28711 | -44.65136 | 2026-10-07 16:37:00 | NPP-375 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f32b0648-a5bf-3124-b6ca-471ae0e25c81 | -3.25208 | -43.85928 | 2026-10-07 16:37:00 | NPP-375 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f99b2c38-8903-33e5-8aa1-30d918a148dc | -9.71503 | -35.92423 | 2026-10-07 16:37:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 387e4cfe-a1f5-3115-b6c8-0f12958209a6 | -4.66426 | -40.56317 | 2026-10-07 16:37:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| ca1a427c-f7a7-3a8a-9cb0-cb713f3bca01 | -3.70537 | -44.8921 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f8428f09-1eeb-307b-b203-a502b3bdbeaf | -7.07849 | -52.67909 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1ba88908-c754-3918-b6b9-881db004006e | -9.88863 | -44.831 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 1832d893-cb06-3d55-833b-52c8d415c52b | -3.9531 | -41.54711 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 122.8 |
| 138651c0-eddb-3c57-a04e-8e52bad4f068 | -5.96712 | -53.59897 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06180f0d-19a0-3499-959c-e6870cf2df02 | -10.63248 | -53.84679 | 2026-10-07 16:37:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bef1463f-d18f-3388-a9cd-0197290494c8 | -7.01752 | -39.97395 | 2026-10-07 16:37:00 | NPP-375 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| f8b10bff-473d-3381-81db-5daccd3765b6 | -11.09197 | -47.61927 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5be9770c-b820-3b72-a3f4-11b0e8e1bd97 | -3.8759 | -44.12897 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 434f3022-6aab-3ef9-91dc-3523bb929e8c | -6.59005 | -44.19077 | 2026-10-07 16:37:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 172eb4f8-f0c4-3b6a-98b7-587bb913a721 | -15.544 | -43.9705 | 2026-10-07 16:37:00 | NPP-375 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 38a2e3ca-c102-361a-b5c4-95977e18ee5f | -6.38269 | -45.04951 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4bd0f82-e767-3643-a2b2-ada4bf6c4a41 | -5.96331 | -40.9355 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 657233aa-ef98-39a0-9a0f-c78917224675 | -5.70825 | -37.71019 | 2026-10-07 16:37:00 | NPP-375 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 68e50a3f-63ab-3a0a-be25-fe6058770e9b | -3.91743 | -44.1333 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8fc3f603-0a87-3e0e-8e85-1358c8109013 | -3.74775 | -41.7163 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| c5e66cd9-aace-37e2-afe6-f8b1efde38a9 | -7.55443 | -40.25468 | 2026-10-07 16:37:00 | NPP-375 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| cc47ad5c-d351-3ab0-9821-4d6d40a4ee76 | -8.99738 | -45.94546 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 7dfc96b3-c16f-32b5-8036-b8c04737a02e | -9.96693 | -43.57076 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| c74ab46d-623e-3576-a9b8-5b4e8d18fa56 | -14.83178 | -40.83968 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a5da012f-7058-3533-8bf6-051e62bf4260 | -6.86711 | -39.09814 | 2026-10-07 16:37:00 | NPP-375 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 34843e96-304e-395e-ac1f-4ef8eaddb0c2 | -7.75987 | -43.81305 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| da6d84af-ba89-3188-8365-672b39a2a063 | -7.17052 | -43.7645 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5d87265c-2ab7-3ebc-8601-d2d9e85aa301 | -3.35677 | -43.38884 | 2026-10-07 16:37:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a31caaba-27ae-3afa-9f73-18e2976ea37b | -6.33313 | -43.74898 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| f7ef3341-0f37-30d7-9a8d-f0ae0b443c88 | -5.76753 | -38.55718 | 2026-10-07 16:37:00 | NPP-375 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 27.6 |
| a1cb69dd-9cee-3704-8887-3e03f3b6264c | -5.62312 | -43.05247 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d27c31d0-d318-3b08-a626-10a3954c33a5 | -6.81093 | -55.29538 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| dd0f3ad4-6ff8-3df9-a76f-fbce0257475b | -11.13924 | -46.17233 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e1e5554f-a75c-3a66-b532-16c9407482c4 | -6.18206 | -38.4777 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 04c7b049-1469-3584-9a57-1c34c91d182c | -10.34007 | -46.25227 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e83a4420-4177-32dd-abc7-9b7f02fe0d13 | -4.91656 | -43.22641 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ef5d1e74-c807-3ea9-9dfc-188e26dbdc35 | -9.917 | -44.81173 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ae401511-4427-3f98-8b10-d39dff79fa74 | -3.22288 | -42.65636 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0512fafd-bcfc-31f5-beeb-0eb089b5b968 | -3.73388 | -39.52981 | 2026-10-07 16:37:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8d8ae4fa-0040-31fd-9b59-3c832fe46f62 | -5.53079 | -44.95653 | 2026-10-07 16:37:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1981f40f-8cc8-3175-815b-4e64e90592e9 | -9.51819 | -46.84792 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 70c8c62f-c1a4-3265-887c-5f7bcd621b45 | -16.19675 | -42.3452 | 2026-10-07 16:37:00 | NPP-375 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0f4488ab-2309-3ad3-b28b-26f8889f590c | -9.14658 | -45.83159 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 07b9a145-92cd-34cc-a578-bfa5e8f64a96 | -7.20975 | -44.28832 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30f3c6a9-cd48-357f-b90f-c1d57ee1c0a7 | -9.82433 | -47.48284 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 373c66ea-4d54-3ae0-b981-18e27c53d0c2 | -7.47508 | -42.82235 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 5672e577-b1be-30b2-b2f2-0e051166330c | -6.61479 | -52.99445 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c56af2b2-1a62-3626-9473-5e28b928a771 | -5.86113 | -45.1995 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4083c4d-8b1f-3eb5-8759-dca348c808f3 | -5.74214 | -41.72405 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fa9e51bf-bcee-307f-a0a5-7d22165cde6f | -16.45568 | -41.0596 | 2026-10-07 16:37:00 | NPP-375 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| d72065ee-b5ad-32c0-a3f1-2de73ee88601 | -6.47118 | -55.44855 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 309354e5-2839-3ea9-a47e-453a92d411c1 | -5.87508 | -53.62032 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 795b662b-6782-3180-9365-3bd50c9a7b7d | -5.99187 | -44.12594 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 94e752f4-9fa2-3db3-a282-f96feec53896 | -4.91546 | -43.2193 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1cc8cdb3-9dcc-3434-82b6-3b8385b23943 | -3.88322 | -44.11009 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 556b635b-4914-31ce-8d20-e12604fb5f7d | -4.76943 | -43.74092 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 78154ae4-8850-3440-bd89-4c6684b3c760 | -11.20538 | -49.42779 | 2026-10-07 16:37:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c0474ef-3522-3a33-868b-238cc5351e3e | -3.11404 | -41.83617 | 2026-10-07 16:37:00 | NPP-375 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2707f11d-0ef1-3dfb-93dc-96f857ce71bd | -9.91505 | -46.80781 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7a0d7ab6-1b71-3bb5-9306-be22f394df49 | -7.21677 | -55.11542 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 9828f693-ba50-3e9d-90b5-a8c662d357d0 | -3.81141 | -42.22045 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 40.2 |
| b7a74efb-5b5a-3620-a9c3-0736786a5abb | -6.05033 | -53.47911 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1b563053-9770-38f6-b616-878b3b14634f | -5.79846 | -52.36472 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1939eca9-96ba-3232-9893-b0ce59ecddbb | -7.26784 | -44.29008 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c6ec2c24-f120-387d-a1c0-e35d6cc55d0b | -3.90027 | -38.4998 | 2026-10-07 16:37:00 | NPP-375 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e790ec8a-dc38-31c1-98dd-de50b7e8ceda | -7.02318 | -40.86696 | 2026-10-07 16:37:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 3d043d08-714c-3762-ae9e-3c9528a08912 | -9.5879 | -48.91772 | 2026-10-07 16:37:00 | NPP-375 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dd1cb901-7c64-3765-9db2-a979a2a6b365 | -5.31017 | -46.6854 | 2026-10-07 16:37:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8df34ea2-3fc5-3366-a049-53645508e800 | -7.26912 | -38.10303 | 2026-10-07 16:37:00 | NPP-375 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 5.5 |
| cf9d197c-505e-34b0-aa09-3dd7daf7b92a | -3.89148 | -44.1195 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 33ef693d-64a0-3b39-915a-88dd762e27fc | -6.48321 | -52.81079 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e497b666-4ee2-3c20-a941-03c832b5c38d | -8.94033 | -47.38561 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d0b642f3-269a-3c44-be15-1d1b8c35f3d7 | -10.17212 | -46.71557 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| af55e616-a501-33b2-ba90-6f064015332a | -9.87753 | -44.80282 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 77ce96fb-7c4e-3c38-9f32-031fc1a0ab5f | -3.75752 | -40.03822 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 979a1341-8e58-3363-8c99-c45a9382d4ee | -10.78397 | -47.18161 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1afe7992-174a-375c-94f3-ebc91edcc1ab | -5.48942 | -42.84587 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| a131dcb4-70fe-3158-8b96-939ecebfe2ec | -4.42349 | -43.73469 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| fb7c7d47-c7cd-33d6-9ae1-03f534f8d4d3 | -9.97144 | -43.55572 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20c093a7-5f5f-3ec0-9937-ce1aaeabb58e | -4.2722 | -43.01197 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |


[Clique aqui para ver as próximas entradas](README187.md)
