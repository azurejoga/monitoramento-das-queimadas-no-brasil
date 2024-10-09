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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e27dfbb-bcc4-3a1a-80bd-c0e418fcbf44 | -6.79449 | -59.3449 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 367fbec6-9733-3945-89b9-601757ab46bd | -6.79405 | -59.35144 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1c5d489-0a50-3aa5-92d5-3f7558849705 | -6.79376 | -59.34925 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eb023ab-bf79-32c6-a318-732ad98bcbfb | -6.79195 | -59.36451 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cfdeba7-7f92-3fe1-b3bf-1f3f0171b498 | -6.77643 | -60.05206 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97fcfc7c-d882-38a5-8de3-bd8d75bf2230 | -6.77562 | -60.05685 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 576f118a-4c07-3475-b069-326930b53958 | -6.77441 | -60.04951 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 323fc8ba-d792-39d2-a39f-46881807076f | -6.77363 | -60.05431 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 00974441-f69e-32dc-84e0-1507a97b661e | -6.77285 | -60.05912 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 76bdb0c8-c244-3c85-9c99-ff03d1c1cf8c | -6.77059 | -60.04885 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 3492a8fc-3558-3bb5-a11e-bd01b0820c61 | -6.76981 | -60.05365 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 719396b0-6f9a-30c7-8228-0829a3625a4f | -6.76902 | -60.05848 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 3e1c1141-a9b1-3c6e-b8e4-132f69f006a5 | -6.76676 | -60.04823 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 487c9f58-4249-3f57-a451-ca1e4063aeb1 | -6.76598 | -60.05302 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a37e60c2-aadd-3ec0-bed5-089391be93af | -6.76519 | -60.05785 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3060b046-56b7-3389-b09e-b0708bab9325 | -6.76293 | -60.04763 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aac5174f-6374-3747-9a11-bec032debeeb | -6.76215 | -60.05241 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5b7be33e-b252-30a4-929a-553c9d54eed6 | -6.76137 | -60.05722 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bb50e415-f9ff-3702-adf9-d00164edf74e | -6.7396 | -59.6725 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7583862d-8b0e-36e4-bca8-6bb674cd8401 | -6.73888 | -59.67025 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f66824e-3079-3b2b-b336-38de3846f776 | -6.6828 | -59.84899 | 2024-10-09 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf00673a-22b4-3be7-8983-528416827c28 | -6.68033 | -59.46771 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14ccf51e-d7b1-3089-bf4f-7bf4baec96b8 | -6.67663 | -59.46709 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbaaacc8-2455-35d1-8304-a23671e693a7 | -6.67294 | -59.46643 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51463935-5f77-3967-a2fb-1c4a9ec89b89 | -6.65945 | -59.77856 | 2024-10-09 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20e211e7-237d-3390-9b51-d15eed523f35 | -6.65568 | -59.77794 | 2024-10-09 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9fdd263c-7207-32ab-91bf-cd5fd5e290d0 | -6.65492 | -59.78255 | 2024-10-09 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a75bc818-a954-33a1-9538-e1bebc9532b1 | -6.60709 | -60.0 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c95dbc84-4fa1-3c88-a04a-cbdf9db14190 | -6.60629 | -60.00479 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42c67a22-11d1-328e-9927-d3fdfa34fc7a | -6.55075 | -59.99316 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a46744d1-da43-3b7f-b3c0-c8ed6151cfda | -6.54841 | -60.00745 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bab0f79d-0597-3642-9445-7be9372dfb29 | -6.54692 | -59.99256 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6d3dcb0-f7f1-3770-b573-c9a553b7bdbd | -6.54614 | -59.9973 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a81bed0-7523-3bcd-855c-594cb43ab585 | -6.54537 | -60.00203 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1e0f0588-9ae2-388c-b39a-9b5af2654cc3 | -6.54459 | -60.00681 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc6eedcd-3425-3ea0-a400-09318d2b39b8 | -3.48019 | -60.04294 | 2024-10-09 05:01:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 885f14a2-4f0c-341d-ad7f-c276ef132209 | -3.08062 | -61.06285 | 2024-10-09 05:01:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 980b8496-4361-39c2-a34b-fea79c54aa03 | -3.07995 | -61.06697 | 2024-10-09 05:01:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e9f5ce9-f21a-301b-bbd9-08de0b1cc069 | -3.07631 | -61.06208 | 2024-10-09 05:01:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7349c57c-5921-3d16-a09e-6421d2e4430f | -3.07563 | -61.0662 | 2024-10-09 05:01:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78f9c5d5-b14a-347c-80d6-13a9500ee893 | -4.71708 | -60.81491 | 2024-10-09 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b535b961-a937-3f20-b8ef-c7b7fff86ec3 | -4.11899 | -60.78125 | 2024-10-09 05:01:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04a12960-308c-3193-a831-b843d265a98d | -4.11837 | -60.78505 | 2024-10-09 05:01:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6271b6b9-6115-3bee-8cb3-8d124e7e4d62 | -4.00653 | -60.39779 | 2024-10-09 05:01:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b3f9de2-0488-3312-bf8c-3389e6af07df | -3.88628 | -60.59284 | 2024-10-09 05:01:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1bb273d-cec0-3afe-b632-e98f308dd657 | -21.65 | -47.72 | 2024-10-09 05:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7898be40-9f9c-32c6-a39c-58ebe090e24b | -21.65 | -47.77 | 2024-10-09 05:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9a1fd842-b9fa-3162-8b05-8fb52816ca3c | -21.68 | -47.73 | 2024-10-09 05:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6b955abc-0ddc-3317-8d91-a4ee1d04c69b | -9.16878 | -66.05513 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2618c838-ba65-3d24-9e74-7c55ac6631f6 | -9.1633 | -66.05416 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8f6f37f-b912-35e6-827a-39dda1aac3d9 | -9.16196 | -66.06143 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46a8aaa0-6e49-3208-b004-dfd447425a05 | -9.15783 | -66.05312 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc53e56a-6a89-300e-a25d-dcc112a1d308 | -9.1565 | -66.06037 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec7b2c6b-6a10-31d1-9df3-e6e5e7fc3d5f | -9.15584 | -66.06396 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f738f740-da88-35e7-a31b-9a2dc9893563 | -8.88013 | -66.65121 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c6e06e4-8571-3efb-86ed-86523f3dd6e9 | -8.87934 | -66.64852 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a60e3e2a-2f0b-377d-ad2a-c087c7e6b642 | -8.87863 | -66.65245 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a998902e-e102-31ba-8d62-c7ade5f6eac6 | -8.87444 | -66.65004 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f0a928e-455a-35af-a4cd-24456e1f1ab3 | -8.87366 | -66.64732 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a29b0306-d7d8-3084-99d7-e3c0da52b22c | -8.87294 | -66.65125 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 082510dd-8e6a-326f-be6a-c1466479211c | -8.86874 | -66.64891 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5253b382-3d43-31b1-9e11-e7420bdfd60f | -8.86723 | -66.65016 | 2024-10-09 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78c786d4-fc9b-3f48-8e1f-4de263d82044 | -13.80802 | -43.60866 | 2024-10-09 05:04:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 633828ac-d77a-3855-ab30-5cc4d7ec94c4 | -11.89203 | -43.88689 | 2024-10-09 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c76c32e2-0ef6-304e-bec5-bac216be72d6 | -11.89135 | -43.89318 | 2024-10-09 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 583bfeb1-28c5-3a3f-a2e4-0d2953a143b1 | -11.89061 | -43.88645 | 2024-10-09 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8c39a75-697c-33d4-b46a-7c16cc54956a | -11.88988 | -43.89273 | 2024-10-09 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0fd7302-3b9f-3281-ae43-ac4ac13b9813 | -12.87944 | -44.61958 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31d37868-04ea-3fdc-97dc-a04288e118a0 | -12.87764 | -44.62041 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9a9a48b-0ed7-372b-bfe8-d137792ff10d | -12.87216 | -44.62481 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e1dc9f8-8d56-3522-b53a-34f9aef98b1d | -12.87103 | -44.6198 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ddee372-040c-3f90-b3a8-58abedcfb9e2 | -12.87041 | -44.62552 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 70c2f0fc-4ab9-37d0-a237-fc9a2951314c | -12.86623 | -44.61832 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 85e8f672-bc7f-3007-997b-417b68ff44af | -12.86559 | -44.62396 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff56eaf4-4a3b-3fa4-84a0-40f3ae0229a8 | -12.86444 | -44.61898 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 58c4cb3e-65ba-3fb4-bb5c-9ac8d1117141 | -12.36477 | -44.73743 | 2024-10-09 05:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f83e18af-06c7-3342-b2d6-7a8e58f51202 | -12.35824 | -44.73679 | 2024-10-09 05:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b811a3b-da48-3d89-a1bb-c04e6c6cd6a2 | -14.50964 | -43.85146 | 2024-10-09 05:04:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05403d40-ea3a-3112-bf72-3b0184f208e1 | -14.50898 | -43.85826 | 2024-10-09 05:04:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 452fd6da-571a-3c9c-b695-ed5c4fca98d2 | -14.15213 | -44.94682 | 2024-10-09 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1893b77-cf8f-3441-a2a0-c33dcbd3aaf6 | -14.14554 | -44.94637 | 2024-10-09 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c349b55-2ff1-34f1-9a52-550895cb03bf | -14.08869 | -44.15635 | 2024-10-09 05:04:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77004546-c552-324b-82f0-0ce08b05feac | -14.08796 | -44.15438 | 2024-10-09 05:04:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6dc7078-8098-3770-bd17-1e2d15b09341 | -14.08182 | -44.15559 | 2024-10-09 05:04:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a45b4f5-04b5-3496-bb96-3d022202c8d6 | -14.08109 | -44.15369 | 2024-10-09 05:04:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b2960db-332e-38da-8206-06ba03db8912 | -14.0631 | -44.47416 | 2024-10-09 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3702affc-e64d-3ea0-a8eb-6e08b274b2e9 | -13.94488 | -44.53411 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93f23421-fe01-367e-b7f1-93940db2f740 | -13.94426 | -44.54009 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c85a79f4-f3c0-3890-bb13-97fbe47e1a62 | -13.94185 | -44.53308 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa9fbf0f-07d4-34c2-9380-ba39cb18dacc | -13.94118 | -44.53911 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 203eaa0e-43a6-38d0-b898-b10f6bc4a97b | -13.94052 | -44.54513 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da8328d2-5e4f-372b-a5c0-b291785cd31c | -13.93986 | -44.55113 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca394c0a-6033-3c12-803a-006dd9cfbecb | -13.93878 | -44.5274 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45432db4-fb37-324b-8ef7-21b7610bca08 | -13.93815 | -44.53359 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff673f7d-daf0-3313-9762-6f71a0336e45 | -13.93752 | -44.53966 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f632d88-bd99-3f58-888a-577d993d40a1 | -13.9369 | -44.54569 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76200a55-63f8-368e-99e0-d13c6a6e01cf | -13.93629 | -44.5516 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad4870d4-4911-38c3-a78b-ac9e017878db | -13.93513 | -44.53246 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07845e20-e5e4-3e65-ad85-8ffe2199e3f4 | -13.93316 | -44.55048 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59824d06-25fb-3a25-adb8-928405720d34 | -13.93209 | -44.52655 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README170.md)
