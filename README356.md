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

## Dados Diários - Página 356

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4795b92-18e0-3c56-a080-632f06f45604 | -6.04152 | -46.6413 | 2026-10-08 16:39:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| cc76e88e-d06e-3a81-9460-cbb30e6dd163 | -5.78038 | -50.0988 | 2026-10-08 16:39:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 00ab8cb2-78db-3e88-b8d1-862fb649976a | -3.01254 | -51.0158 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| d2c85de5-fcc4-3c2e-bde2-4e599d990059 | -1.11227 | -52.257 | 2026-10-08 16:39:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b02ddf2e-9f2f-33e5-8abd-31a2ac8dc2b4 | -3.09946 | -59.18927 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a74a5890-d9a1-3268-a645-7b7b898b4d76 | -5.16534 | -45.17457 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0de48241-3f1e-3574-b3b0-33de1614fc07 | -5.36243 | -43.20295 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 958ddf01-5689-3082-9d8a-58a9174804ba | -3.98695 | -59.35085 | 2026-10-08 16:39:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 8a89bdb3-2af8-306d-9297-a21348dcb099 | -2.4979 | -56.3438 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29072560-d99e-324b-adfb-15c91baa9d0a | -6.74042 | -55.12624 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b99af510-8970-3309-b75e-ddc45b5a19d7 | -5.45643 | -45.58639 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a9130e17-f0e7-331d-b5c0-36bdab247c89 | -3.25446 | -44.46883 | 2026-10-08 16:39:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 0908688c-581a-3068-a027-bf61fc4fc10a | -1.54723 | -60.03032 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 91626ad3-54e7-3aee-beea-f60c2bac2d0e | -2.80304 | -54.7251 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4aa14d43-afff-341d-bde8-a04ff910fc79 | -4.85477 | -42.9945 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 798b3583-1fce-33a0-aa5b-63eecd073d66 | -2.61508 | -56.48466 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a93c3b83-9e46-3ffe-a9cd-875f3cdece6a | -6.14212 | -51.9207 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 752e38d4-6080-3f7b-90de-fa5e7d4c3b4a | -1.60405 | -55.15656 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 135aa956-6cdd-3218-9a13-db33009dafc2 | -3.18699 | -58.63733 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| adbdb703-3f9d-3924-9733-c464faf96d98 | -1.52745 | -54.81277 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a9938968-e0e9-3341-9c14-d4382707c6d9 | -6.26015 | -52.85907 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ba83adfa-71ac-319b-a256-568f6b9e0a79 | -2.988 | -54.07457 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0e110bba-936e-3dd2-b13b-cf2449afe6ca | -3.85519 | -44.11876 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 1d05452b-3b43-3e32-8c8c-86d964c957da | -3.02514 | -54.05627 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| de046b8b-8d0d-3e41-9261-4073763ad725 | -3.04127 | -54.26923 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3455c965-f866-35b3-9c9e-3ed4d7ca817c | -5.47105 | -41.22292 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 7c765ab4-22d3-3e34-95e7-b7ac2737d6a0 | -2.55001 | -57.38694 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2fe96c4d-08c1-3725-b748-2eb37e533622 | -5.68537 | -53.4858 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8f5298a6-a91c-3f9e-8814-d010f62990b1 | -3.79441 | -41.66028 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 635a6ce7-665f-3913-8f2e-37fbf10a4ba4 | -3.51869 | -59.09238 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5f990ffb-56a5-3b6c-9ec9-7d4446d11df3 | -3.2537 | -50.39691 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ad3e070d-806a-333c-8a66-3099e6afac1e | -2.61309 | -56.4745 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1dd1d3cd-a344-3066-bef2-56948f17c93b | -2.8784 | -45.75235 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ec41270e-660e-3723-b6f7-8de65a1fa446 | -3.16697 | -58.63482 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| fed72f36-d7a2-3c1b-9464-5af08d683acb | -4.09525 | -44.1057 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6273125e-cd9e-3634-8579-cc22af20171d | -6.14838 | -52.89639 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b34753ef-4b26-374c-8190-4b114b035898 | -3.94296 | -55.32735 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4c9067bf-25af-3acf-aa8b-f91efebff902 | -6.73182 | -55.10316 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 88428256-c9b5-3668-9bca-c9529acf8db1 | -3.19641 | -43.37384 | 2026-10-08 16:39:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 155a2e03-a358-3b8a-9eca-dab3beedc487 | -5.70217 | -53.46825 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 54939af2-2645-31d7-9b09-79bb2d105c8e | -3.14566 | -53.72048 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 9d9c91ae-bcd3-3fba-833c-601503e1973e | -4.75271 | -40.50336 | 2026-10-08 16:39:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 9aef4910-629a-396c-8495-06c0f318cf67 | -2.04273 | -56.19486 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e7acc69-a434-3308-ac17-b357e96c1c9e | -5.72528 | -53.45249 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f126a3aa-2d49-30ef-9245-5437453f176a | -5.37823 | -44.20412 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 158b8bf4-0df4-3203-9ced-6df551657330 | -3.50573 | -59.3323 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 0c41599e-4a4c-3cc2-a37a-73c3f8a25294 | -2.98281 | -56.83076 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ff506ce6-039a-39bd-90e8-c7075c236464 | -4.58211 | -40.65179 | 2026-10-08 16:39:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ce53d2ee-2432-342c-8002-23bafe746052 | -4.80237 | -55.96313 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8115e84-f3b5-315c-89e9-8ede7e4957f5 | -5.47887 | -44.60571 | 2026-10-08 16:39:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8a487065-1478-3de4-b4c1-6275be947df9 | -1.96174 | -56.30935 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b1eaa6d7-9ad1-3316-a239-54aba8c7b1ec | -1.53033 | -54.53669 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0b644b71-2224-30bc-a584-d2f200170658 | -5.69913 | -45.28773 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6867e4af-2a1e-3e29-99f4-7dd9517f9037 | -5.47575 | -45.68993 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 17230560-b16c-3e7f-8335-7c6a25054d5c | -1.93139 | -56.97633 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 90579bb9-9fb0-3eff-8193-9b3ccd059712 | -1.50211 | -47.94055 | 2026-10-08 16:39:00 | NOAA-20 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d746272-22af-3774-8149-dc0beecea79d | -3.16519 | -50.45381 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6acafcae-8b69-3fd2-aff5-48c6797ec7bf | -3.06467 | -57.75014 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f96ab84a-df64-3de1-aafe-a49fc8aeb520 | -2.09896 | -46.5797 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f7f6175c-a048-336b-a890-5c9d9d7da7f6 | -1.52398 | -54.52705 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 21f237ef-08e7-3800-937f-f6e847fcad37 | -3.02673 | -57.87923 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ea62ffe5-bbe6-322b-a94b-f624c07434b9 | -3.77942 | -45.27764 | 2026-10-08 16:39:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b2908e04-9c06-3749-99d2-209dc92e8caf | -3.51672 | -59.56604 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b6012b14-8031-34d8-afd4-1dc9623e54cf | -3.82366 | -59.33667 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| e78bd7f0-140d-3f51-8646-80dfedca1f86 | -1.2892 | -55.41445 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 61cb01b8-f86a-3006-afac-84a4ff67ecb8 | -5.07505 | -46.2211 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67e70a0c-2930-3281-a310-d49a516de6bb | -4.45106 | -55.862 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 28d3b2e4-27da-396b-8983-912b51963a6c | -6.64742 | -52.9537 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a415d1a3-6aa3-3859-be27-8eb1a5c12ed9 | -3.00083 | -57.74717 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b33bdfdf-edbc-39ea-93de-95b88c2a9121 | -1.20997 | -55.68906 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 57e112fb-a52a-3b4b-abf6-e1d70f13245d | -4.35415 | -43.79107 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0e92c445-1f88-3f42-bf3e-23a012cca1a2 | -3.78752 | -41.66839 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| a4fb4617-5f3d-3e86-a001-25abc2c4d004 | -3.00236 | -54.04162 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| d42e8338-b71f-3b21-aa22-3a8214a5e029 | -5.39903 | -42.95614 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 9344ac67-7a72-36f6-b556-dffa271882c4 | -3.199 | -42.96339 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| acfdb901-7ebc-3daf-8d45-0de4c8425863 | -2.88273 | -56.66312 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31d38e18-b3a7-37b1-a9d8-97122a6e5c41 | -4.58861 | -56.08508 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d625d5d5-64f6-3ef1-b6ad-d4842dcbf95c | -3.42747 | -45.04315 | 2026-10-08 16:39:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e6af666d-5b90-3f57-bb22-1070bf88dbcb | -1.82941 | -54.98892 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1ce24649-8b77-3556-a113-129c22dc869a | -6.13974 | -53.0673 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 58667c27-79c7-3b1a-a79b-04fa5a5175b7 | -5.40584 | -45.69846 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f959a730-d203-3785-8cbc-716a3c4bf6c5 | -3.31253 | -54.7035 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 2fe1396d-d40b-3ae5-bf1c-58e44f128eb3 | -5.43153 | -46.64558 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7d310062-a27d-306a-88b6-a768838eda8a | -3.49533 | -39.50527 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| bc7e55ac-b88d-3e72-abbb-7586307d41ce | -2.41323 | -56.52919 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 605c005e-06da-3a0f-ae99-45c99063b481 | -1.56549 | -48.22183 | 2026-10-08 16:39:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 550b7d79-83bf-3c3e-bdf7-29359517c540 | -3.25788 | -54.04387 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| f074ed36-d384-30fb-b5a8-583e4c93446a | -6.12997 | -47.93539 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 44179d50-ea65-30a2-adb4-379edcb93993 | -2.48531 | -56.14012 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1bd8d87c-1045-395a-bc80-3261d9700101 | -2.73642 | -57.60981 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7b159436-7681-3fb6-908a-ad8aafd860cf | -1.80294 | -57.12046 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f89d54c2-cc31-37aa-9702-0c4993642e36 | -5.88532 | -53.62052 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9869e01c-2f0f-3ac5-9c22-41ca688e6c82 | -4.38146 | -43.36401 | 2026-10-08 16:39:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 168d5bc7-c99a-3157-a3e4-d77673fcb463 | -1.30024 | -45.92856 | 2026-10-08 16:39:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fde81244-1a1b-39c5-bf80-8baedebedf54 | -3.25727 | -57.87024 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| df59af43-4654-34ab-afbb-fd82c942f62b | -5.09641 | -49.70031 | 2026-10-08 16:39:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f8c1b54d-73de-3774-899d-611dd552b10f | -3.1798 | -58.63295 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| cad11c6a-be2b-3f55-84f9-d7cdd4a851fc | -3.07572 | -57.99675 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 30601519-d505-380b-8023-d71b30a9667e | -1.77413 | -55.02575 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 816f9a12-534e-3675-9586-fdf8a32a532c | -6.0466 | -53.48566 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README357.md)
