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

## Dados Diários - Página 357

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79df7ba9-3aba-3d7c-a171-f82299434d6a | -2.99461 | -53.89594 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| bc1eb897-dcbd-3657-a323-dc7115ffff52 | -2.48704 | -57.78243 | 2026-10-08 16:39:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9fdd0c8a-e56d-3492-92ab-fb4a7e9a805d | -3.64165 | -58.94237 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6aad202d-938e-3788-8bc5-2b3381fa34d6 | -3.43272 | -56.93894 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7ce21d30-8ffa-3f44-9586-42cc1d9f0fcd | -5.9256 | -51.82763 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| df248c1c-52cb-3c51-9da0-891e19776a89 | -4.19122 | -40.4801 | 2026-10-08 16:39:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 0afc21e0-b087-349b-9e67-0bd51169e114 | -5.68861 | -53.47469 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| aa5675a3-bd6a-342b-9e23-eff22479f2c9 | -6.18749 | -52.87622 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 39c48afa-2b9b-3fac-9e45-bbd1c3b9683d | -4.09245 | -44.13362 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d3b4a62c-7f0e-3c46-86ac-2500bebdaf7a | -6.39035 | -52.7178 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 464f3f91-184c-3548-859d-3dbe5063a233 | -1.80863 | -57.11946 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 47ac8d86-ac89-32d2-a396-02bdf180a8ec | -2.08015 | -46.58958 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 48bc4adb-e7e7-3a33-b7dc-d440f8c32e56 | -5.69687 | -53.4986 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 63b79852-ebc6-3221-bed3-e3755d1137a1 | -4.52563 | -44.0116 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 532166e9-2ab7-3022-bfca-f1f7dd60af56 | -4.74916 | -42.59412 | 2026-10-08 16:39:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| af12215b-1ed6-319e-9fe8-4e936bd2ed77 | -5.92617 | -51.83152 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 224cbf44-335a-37da-abae-901611d95771 | -3.86319 | -38.50705 | 2026-10-08 16:39:00 | NOAA-20 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a886465f-c5af-3cdd-b9c8-089b368b18af | -3.02355 | -54.05396 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 508c5090-6d91-3d57-9f57-abca76ad7391 | -2.84711 | -57.4714 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 42c20fbd-cae6-3a3a-807c-0067e4aba083 | -5.66463 | -43.62519 | 2026-10-08 16:39:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 11d0806f-b459-3d50-9d2b-3e4a12d84f20 | -5.74158 | -53.46568 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6c029a6c-a441-3f1c-afc3-add3c4c73bfc | -5.0917 | -46.2178 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 5e677e8d-a07a-376d-a27a-6c4228247f7e | -5.49735 | -47.73067 | 2026-10-08 16:39:00 | NOAA-20 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfee20be-2d08-39ba-bca9-d57be4baa8c1 | -6.02759 | -51.72679 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cee632d2-f6f9-31b3-bcb2-4da9161acfd9 | -3.9115 | -44.39064 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| cecc7dc0-0e80-3da6-a9fc-691a72d2fd26 | -2.73322 | -54.90251 | 2026-10-08 16:39:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 179c6d10-bedb-3cae-a08a-c65b8824dede | -3.9956 | -39.30818 | 2026-10-08 16:39:00 | NOAA-20 | APUIARÉS | CEARÁ | Brasil | 2300903 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e537afd9-7e09-3eb1-b2f0-17a761ff4c95 | -5.45469 | -42.90425 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| e94880be-41f7-3165-9b75-60f5af64c168 | 0.52959 | -50.81097 | 2026-10-08 16:39:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 26a477d4-62ab-3a68-b77e-5cc7d5bb8596 | -3.26861 | -50.39471 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| b2e0b629-fb17-353c-a2f3-63bc3369bcaa | -3.89123 | -52.81353 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| afeafb3f-8793-3c25-b9a5-d2ab1936d5db | -5.69146 | -53.49459 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| eeca082d-3dbd-3983-ad2b-3e652fb6f974 | -3.43015 | -60.22978 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c3790b28-b6ff-3e97-b01f-cff3861932fc | -1.21648 | -55.64648 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d646e17d-220e-3582-8e33-930d82da02de | -5.73365 | -45.16016 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3b412398-5727-357a-95ac-e84a4fffbdf8 | -1.48473 | -54.55837 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1ba7cf43-8249-36f7-91a0-77b351b3afc0 | -4.74914 | -40.50807 | 2026-10-08 16:39:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 25e913e3-7e57-33ac-8206-19592fa97b5d | -7.20925 | -55.18794 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 40d973d7-0f45-3952-9758-d189ebb1cee1 | 0.38716 | -51.15175 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e5937e9f-80ac-31c1-8a20-eb9fa715c16c | -3.577 | -54.48369 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7d73154e-85df-3090-9b4d-c37cba9dd5a2 | -3.01968 | -54.05193 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| de3259fb-e4be-325f-b8ca-2eb9c8538467 | -1.53668 | -54.54631 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 98c58d5f-18b6-3537-8a26-eecd90077eba | -1.59501 | -50.44573 | 2026-10-08 16:39:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 27441a46-165d-32c0-873a-3f2287e35a5b | -2.48316 | -56.08788 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2a4f584c-f72f-3d5f-8bcb-9cb91d92a385 | -3.50307 | -45.19734 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2af6ab84-680a-38a9-b0e3-ba5a2f29b79f | -3.07184 | -59.16808 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1255850-957d-391d-ba03-0078ac264f71 | -3.05861 | -53.92393 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 2170c7dc-d2fb-3c83-99cb-4e5ad1caf1df | -3.4418 | -45.24694 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0ba7ecb-9105-3d5c-b380-d6ee834d099b | -3.79332 | -41.65343 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 68f2695e-57e6-3c2b-8dc2-adf592ca848a | -3.44206 | -45.09266 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7a2c6d7a-8e7f-3d95-8008-bc7a546f86d8 | -3.0086 | -58.96073 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| df42fd16-4689-3d8c-a4fb-4fe0d5187d17 | -4.65779 | -56.21291 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5714397a-94e5-369b-a5ea-e0ac7b778f09 | -6.84484 | -59.29683 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1199a1a1-29f6-3f23-8ad5-6cac51c6c6c4 | -3.48172 | -45.3938 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 283b14b2-e443-35c3-8617-47da50819270 | -4.38253 | -43.95047 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6064809a-b3d0-37e1-b37a-4172a7718b4f | -3.2773 | -53.81758 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 580a4850-6245-321f-a795-3b7b0b40fea8 | -0.37836 | -49.94401 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 28f53d7d-64ae-3a6d-b7c5-693ab3f0c45e | -6.17407 | -51.94105 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2896baa4-6fb3-3403-927d-71d484895137 | -3.08766 | -57.65438 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 65a1f4b1-5478-30b7-a0c6-b79d74ad777a | -1.75316 | -56.18667 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0026fbcb-a0de-326f-ac79-5e83824993ca | -5.48281 | -44.60881 | 2026-10-08 16:39:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a90b8c25-3e95-3357-af70-639843f9fe1b | 0.5309 | -50.80254 | 2026-10-08 16:39:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 781ffcad-b075-3b2c-96e1-2936a24d0860 | -6.20069 | -52.86751 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 603c1db7-e62b-352d-b2b4-3c7d649eb94d | -6.86022 | -52.83591 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c566c123-590a-3676-a117-82daae227086 | -4.26525 | -46.38442 | 2026-10-08 16:39:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c2d385f5-5f5e-3307-9740-f2f414e3b914 | -5.50541 | -42.84901 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 5e68e1d9-079d-32ca-889b-141963e35d97 | -3.48882 | -60.2848 | 2026-10-08 16:39:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1118690e-a9c7-3fcf-8705-9097c4fa7da2 | -3.28444 | -53.70725 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e97d4a77-5f66-360e-9857-fe1f81c1a3c9 | -6.15106 | -47.936 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 660b87ef-1eb0-32ab-ac1d-41a4c04bb4b9 | -5.4719 | -45.68695 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 996efbc3-a426-3113-bbc1-69f93f354940 | -2.2487 | -55.05119 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0af2cc80-7ee5-3ff3-bee3-c999b3194f5b | -2.38193 | -56.85579 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e25a986-9f24-3b5d-9969-cf824eaf8abd | -4.09178 | -44.10626 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| c6d9fcb3-28fa-3b0a-88c1-e704ee12d713 | -4.72227 | -40.92493 | 2026-10-08 16:39:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 755b60e4-b1cf-3466-a75b-ceda8aeedb4f | -3.28722 | -57.90242 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 01bad178-b223-3202-a64a-a84f5b87c1c1 | -3.05608 | -57.48248 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3bf62ee2-e136-307d-8091-a50bdf7ed336 | -3.78234 | -41.78873 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| aa2bc800-b917-31b8-891b-3c247f0fc11d | -2.31566 | -57.98868 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0c896c6b-3cdd-33d9-a154-a9f4c4147bcf | -5.82823 | -52.04851 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce409c00-5489-32b9-bfc5-5e060c642d09 | -2.50695 | -56.13689 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6f5000f7-777a-3d64-9365-2f71452eb7b1 | -4.91674 | -55.85413 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2524260e-59ab-3c58-b23a-86d5eba0ed50 | -3.41288 | -58.03768 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 815b70e3-cc35-3c09-80dd-989ec24cfe64 | -1.50903 | -54.81124 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2c4a4f91-1bea-3b59-8096-8b230dabbc54 | -3.67875 | -39.10376 | 2026-10-08 16:39:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 547b500e-116d-38d4-8be7-6c30bff2ac0b | -5.40664 | -45.92477 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d6320ebd-dd83-3969-b463-038c98a35019 | -3.00921 | -54.08688 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 4c7f3100-a067-3932-8d22-fe1e35ce475b | -2.56986 | -57.4077 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1933355d-eaca-3c96-a860-8a2757835e4c | -2.09008 | -46.58809 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9fcf376-3700-3e48-b836-54313f3ff539 | -5.48924 | -45.22731 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| ac1c4511-cd51-3f1e-91af-f1b712e97818 | -5.8768 | -45.95961 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 8df25499-dcc8-3d4b-b233-68c28810878e | -6.64214 | -52.94967 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7078c817-878d-33fb-aecb-bd9e9c080e32 | -2.10595 | -56.62776 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6f87c7c4-c164-33dd-b181-a2eb59ff1267 | -6.25798 | -52.67284 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 086e4eb5-9ce6-313b-a7a2-183bcb271585 | -3.38394 | -59.43058 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f1562d40-c5d4-3a4d-be64-71f2342f36df | -2.08677 | -46.58858 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d1aecb4c-e901-3336-ba79-4a6cf5eba1c2 | -3.48151 | -59.50211 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 770fbf09-6507-3e6e-a9fc-046109162272 | -6.51234 | -55.39892 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 2d6a04ab-79ca-3348-a635-5d74dcfb9b62 | -3.92517 | -55.85826 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 16ac3904-4e70-32f5-bb63-7dbc9e7fb527 | -3.85638 | -52.03137 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 98665a09-94e5-3df5-832c-a91494670bb4 | -2.81864 | -51.95857 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README358.md)
