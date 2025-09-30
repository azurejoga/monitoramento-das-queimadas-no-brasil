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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27e4bb3e-b7f5-30fc-8c51-13c63c78440a | -12.74681 | -46.85591 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35c01e4e-6ddd-32af-8a62-fbb86dd71a81 | -7.5465 | -45.29812 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d63c05c9-649c-342c-93a2-f834971cce6f | -10.10671 | -47.78065 | 2025-09-30 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6400f7e6-3fee-3494-b060-af5218cffe57 | -13.37974 | -48.08137 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f3bdaff-25ea-366c-b3fc-c04e379beeb1 | -11.00147 | -57.04642 | 2025-09-30 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a06a024-fc83-32c3-845b-6fdded2b7d90 | -13.70013 | -47.54509 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 183ac1e7-edf9-3308-9007-c79cc196c77b | -11.20374 | -47.74929 | 2025-09-30 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1ca27b71-e1dc-3b93-98eb-00fa8222c3e0 | -7.72408 | -44.9559 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 113948d9-9b41-3062-b590-fbf33aa4123d | -13.23318 | -43.37326 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a3879827-efaf-3a02-af71-f59c0320db54 | -11.81481 | -48.24444 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8a9e4ae-aadf-3183-be53-78c8fe8c087a | -11.36211 | -44.94138 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31a21862-39b8-3ace-a0d7-4e397f0e061c | -10.83268 | -47.96288 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25b35f7a-76c3-3d2b-b8a6-d360b55e21ea | -12.86094 | -46.97968 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40b93448-a8e6-3fde-a6b9-2ff8dd65d622 | -7.62808 | -45.45715 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95d8056b-1e1f-3c1b-ad42-3e940d9f2757 | -13.39881 | -48.07573 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24c49cd8-c7bb-3898-a7da-12815027c57c | -13.35637 | -46.38409 | 2025-09-30 04:40:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c27df92-2509-3969-860a-1e14e0bf9b58 | -8.86217 | -46.59029 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75ec5130-767d-35ea-a217-4eed6c2e8f66 | -12.79125 | -46.89664 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4210898d-2837-3b88-894d-d947ebc0aca2 | -10.89214 | -53.73976 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7afd7821-47f7-3243-8895-b50c80427b56 | -13.73755 | -48.67595 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51930df0-d1e3-3329-bbe7-fa9190323bd6 | -12.79632 | -46.88816 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6eabdc0f-0532-3010-a16c-fcab1c50fd96 | -12.66684 | -46.87481 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d772199-42e7-3ed2-b210-bb5dc7b06675 | -12.03904 | -47.89882 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9947215a-532b-3bc6-982b-2ff4df7293ed | -7.91329 | -44.62176 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f21707c-c6f9-37f1-a118-0fe190b30a01 | -13.2352 | -48.44974 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cbc55303-9ff0-3f98-9b04-3b7002c84c38 | -11.45503 | -45.05312 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9a8c926a-0ec3-3123-a823-eeda547826e0 | -13.72766 | -48.64615 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7b1a36e-e6b5-30bb-b883-7346a80e2049 | -12.76027 | -47.76453 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84e55492-0e74-3f34-9ff3-618902dc7381 | -8.84435 | -46.65971 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10cb3607-dc1e-3b2b-9b32-190e6260251c | -12.86814 | -46.90114 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2af198a9-8879-30b4-9dbf-cf71462edc9d | -13.6427 | -47.33643 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 777e9295-a5ac-36c4-92bd-75374f514efe | -11.45913 | -45.01161 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f9a331cd-7fac-3ea2-91fe-7970a5ca039a | -7.51924 | -45.43298 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c0766af-cfc2-36ca-8d0b-e5519e29215e | -8.87964 | -46.65004 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7ac8dc70-d753-3da5-9a2e-2e1032d1e8ce | -7.37332 | -47.04719 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eefc13f5-ab18-33d3-9c27-02874fec6eb7 | -7.76167 | -45.76395 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| faf157c1-88b9-36f4-b98d-f71c57e9884a | -11.36071 | -44.94282 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 200b0dcd-d079-3b18-b8c8-61b565c96b9d | -12.83887 | -47.00032 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 911d4d6d-3702-3ef1-a7c5-6e3d470e2b6c | -8.88019 | -50.90419 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4a8eced-ecee-3268-98a6-64cc419c1b2d | -11.1521 | -54.12265 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d47ae960-4139-3099-9747-9d979477269b | -12.70315 | -49.27269 | 2025-09-30 04:40:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbac240b-6377-3c19-a1bb-1502a3c55e27 | -9.96607 | -48.79563 | 2025-09-30 04:40:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e076d0f8-5056-3f1f-ab62-27fe22db9944 | -8.73414 | -47.31862 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a744ab4d-493a-3099-8fc3-b73eeb7af5c9 | -10.20228 | -44.89637 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15b2cb54-8347-391a-9a61-aa490b2703ba | -10.61156 | -49.09121 | 2025-09-30 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca5e6385-1c18-32a8-b365-5b20a5e848a4 | -13.80715 | -48.02408 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 432614e3-ff4a-3fbf-9b2f-42cca699ca1e | -14.00876 | -49.63221 | 2025-09-30 04:40:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62cd3aca-540c-322e-a010-0bcdddf5a463 | -12.2227 | -43.75352 | 2025-09-30 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b9b507e-8db9-3971-bb08-5bf28bef016c | -13.21618 | -47.3173 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b45475b8-ae84-35fb-98c0-3538dfc0ebf8 | -10.17138 | -51.62302 | 2025-09-30 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2feb0fc9-37b2-3295-9604-416c3b84119a | -7.91791 | -44.6186 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 279f087e-5299-324d-a910-c2dc53b3d096 | -9.96215 | -48.79878 | 2025-09-30 04:40:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6910b3d6-2ee3-309a-8657-2b1d7173d090 | -9.29228 | -54.50276 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9bc22a4a-7272-3646-9c84-2fe44340793b | -10.75961 | -45.37127 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5022aea7-2887-36b4-b593-def4de9687a9 | -10.06635 | -50.22364 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a43342df-a045-36c0-a05e-46fec9ebeef9 | -11.10893 | -49.77242 | 2025-09-30 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e66eca26-2ec5-3687-ad75-6786b260a9d5 | -13.21107 | -50.93636 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7e50da88-3619-3c55-80f3-9c8f971b7440 | -7.04961 | -45.20908 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a435743-a3d7-38dc-8276-2bda953bf657 | -11.1291 | -48.35541 | 2025-09-30 04:40:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1beb22ef-7265-3e64-9ecc-b3d1ae3117a3 | -12.96255 | -48.4135 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d624c93c-17c1-3773-a182-4ddfdc454bf1 | -13.40062 | -47.54724 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a93924a3-bdef-340e-8998-519570b3108a | -10.41017 | -48.1711 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59603abb-f867-35de-abe1-85606b485f6e | -12.96131 | -46.40262 | 2025-09-30 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d7363b3-0100-37bb-8cae-6eb074bd4295 | -10.19349 | -44.89906 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 0019289f-5878-3364-9da7-194f40f72820 | -13.78425 | -47.95253 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ae96447-5638-3ada-beaa-a340658dfcec | -14.72353 | -45.21172 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bc6d90e7-c760-3713-915e-526a17b2ff9b | -11.20053 | -47.225 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 27fee922-a09f-344d-93c4-657f3638f520 | -13.56577 | -47.30222 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56497f1f-820e-32f5-b827-9d1c3d899a4d | -9.88589 | -45.9546 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fdc9ff8-00c2-3b5a-87ff-4a83a70dcd6c | -8.02025 | -47.05738 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98ef1f8b-7522-31e0-b56d-e35fdcbedefe | -13.82603 | -47.49424 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27368d0b-b424-3928-a46e-ee8c2dd0dbc9 | -8.25436 | -45.52533 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2bbe2819-fd06-3527-8576-e67dba97c1c2 | -9.57609 | -40.35298 | 2025-09-30 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.4 |
| f881e90d-06ce-3ce4-a969-538eddcb8724 | -7.76178 | -46.64849 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9694db25-6786-362f-90e8-e812d5f38171 | -13.49964 | -43.81525 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c94d0e30-2e0e-399a-bb16-4f39dd85131c | -13.40783 | -47.54935 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82b45054-9a77-3eba-a42e-18a7979b8215 | -7.04349 | -46.41809 | 2025-09-30 04:40:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7733ba42-4013-328e-a80b-44d49d2b919a | -9.7548 | -47.75495 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75174efc-7a56-335d-9b6d-310ca84da37b | -13.07583 | -47.07312 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 081978b7-48e2-3563-a8e6-6dbb32990dcf | -10.10728 | -47.77674 | 2025-09-30 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3ececb8-5db1-3d85-a72a-eb3d975a7313 | -8.64995 | -46.60998 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db057291-6ecf-33e9-8365-80e36915679e | -11.30697 | -47.0834 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d58bfab-646b-3cd1-8a70-ffd458eb6526 | -13.69907 | -47.54713 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0314709e-f84e-3f8a-bae4-e37954a0f8d4 | -14.44575 | -46.37561 | 2025-09-30 04:40:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 148347f7-18a2-3d56-9b02-9e3c01926daf | -12.83712 | -46.98529 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 177d82cb-55ba-3733-a553-5d34325b4311 | -9.84639 | -51.3796 | 2025-09-30 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 143be915-1909-35ec-be89-edf1a3e47a52 | -10.6063 | -49.63567 | 2025-09-30 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a87baa99-fa15-3447-b53b-bafab1bf31a7 | -11.23051 | -48.2112 | 2025-09-30 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdccb376-7b85-39b5-868b-a7ae1a303ba6 | -10.91094 | -44.79408 | 2025-09-30 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7bd75f9-1fc2-38f3-9e1f-f9451e7b22c9 | -12.00616 | -46.5957 | 2025-09-30 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1e14ee5-0087-3a6f-a83c-f34043baf090 | -13.85511 | -47.95612 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93ead26f-d06a-3c94-99af-5d40d65ddcea | -14.00932 | -49.62851 | 2025-09-30 04:40:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ce77e33-0ba3-3e38-8e59-10548504cecd | -7.84509 | -47.25954 | 2025-09-30 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 23c16432-94d0-3bbf-af4c-8c4060eac947 | -14.39926 | -47.14342 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a885d884-22bf-397a-92c3-95c25cce7eae | -7.21591 | -45.47319 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 735c6ac0-d975-3bc5-896b-5f5026771b98 | -13.60281 | -43.45919 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 01fb0ed3-4215-3800-a47c-257ada9a75a3 | -10.63084 | -48.52535 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 887e5e80-4ecd-320b-9251-6f728e2716ad | -8.29161 | -50.79459 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 243a7f82-d387-308c-abfd-e1c6f00e5796 | -12.87502 | -46.90705 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 0c424220-8dee-3eb4-ae80-0b3fcb1ceceb | -10.39637 | -48.16887 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README67.md)
