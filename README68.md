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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07662dbe-b145-31b3-a23c-e1ac28a9820d | -3.2385 | -54.2431 | 2024-11-22 07:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 170952b0-7980-349a-b6ff-c3552fcc8580 | -3.2201 | -54.2436 | 2024-11-22 07:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| ed06dff5-e6b9-3cc0-be04-28c1347198d5 | -3.2386 | -54.223 | 2024-11-22 07:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| fa9f8a8b-82ae-34fb-9083-46fc4bcf9893 | -3.0536 | -45.2314 | 2024-11-22 07:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 94d43a5c-29cb-3c6d-a910-2e609e00f095 | -3.3451 | -50.5126 | 2024-11-22 07:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| d35a2c3d-383d-3f99-80ba-59d4aa6533cc | -1.2041 | -51.9478 | 2024-11-22 07:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d1fe49f2-94fe-3c6b-bba5-a17dbe5e4242 | -3.3452 | -50.4917 | 2024-11-22 07:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5337e859-6074-398e-9100-149fe041e3c0 | -3.2384 | -54.2632 | 2024-11-22 07:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 56e27f3c-ad16-3c41-8486-5de61934cbdc | -3.2569 | -54.2426 | 2024-11-22 07:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e19b5f89-dfe6-3a1c-8077-a986a1274846 | -3.9104 | -45.0364 | 2024-11-22 07:50:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 57e4c8c1-969f-3b9d-9f2a-ed85fbf394e7 | -3.2201 | -54.2436 | 2024-11-22 08:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 014bc5b4-2a84-3d81-9c13-27aa133cc5a4 | -1.2041 | -51.9683 | 2024-11-22 08:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 47afeab9-be2f-3fab-a18f-6749592961cd | -3.2768 | -53.8199 | 2024-11-22 08:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e69a01a9-7fef-3be3-9151-104b292823a6 | -1.2041 | -51.9478 | 2024-11-22 08:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| db432f21-06e8-3cbc-a474-c90a3a9cf62f | -3.3451 | -50.5126 | 2024-11-22 08:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| fabb47fe-8add-3adc-8651-e34399b608df | -3.3452 | -50.4917 | 2024-11-22 08:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 16fa2f64-eb05-30db-a290-a1541f7097c7 | -3.2201 | -54.2436 | 2024-11-22 08:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 2ff4e93c-f19c-39cf-9c91-8f0fcf59d940 | -3.3451 | -50.5126 | 2024-11-22 08:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d74b5361-65f5-395c-b2bf-c29799f94762 | -1.2041 | -51.9478 | 2024-11-22 08:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2866f3c9-bc63-3607-b05d-888677658ecf | -3.3452 | -50.4917 | 2024-11-22 08:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| aceef567-0faf-3876-b591-437961025ac1 | -3.3451 | -50.5126 | 2024-11-22 08:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8690fed1-b180-3d19-82f6-19e3f8c31f95 | -2.8498 | -45.0809 | 2024-11-22 09:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 101.8 |
| e8da3440-9823-3382-aabd-e0d0ff9771a4 | -2.8312 | -45.0816 | 2024-11-22 09:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 154.5 |
| f3402851-3a30-3703-8d2a-5f10a3b7d117 | -2.8498 | -45.0809 | 2024-11-22 10:00:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 59ada460-1709-30fa-a6d7-7f758d0fb419 | -2.8125 | -45.1048 | 2024-11-22 10:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 66bf5757-3912-316b-b4dd-877df4dff6af | -2.8312 | -45.0816 | 2024-11-22 10:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 54c0a209-86c1-33fb-9675-8a607fef1bf0 | -2.8498 | -45.0809 | 2024-11-22 10:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 35f2ca66-54b5-3c88-a273-10ba33c92a42 | -1.5447 | -47.2244 | 2024-11-22 11:30:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 6715f55e-ce98-3ac8-a653-872ad49ed912 | -3.6277 | -42.393 | 2024-11-22 11:40:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 149.9 |
| 66776554-9a93-3fda-9a12-6024a882daa3 | -3.44131 | -41.46682 | 2024-11-22 11:49:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 235.7 |
| fb4d61d6-ffad-35b7-89d1-f1ebc5529a9f | -3.6342 | -42.40802 | 2024-11-22 11:49:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 9107ddc5-7f74-3b64-9b6a-d66702d11928 | -3.43733 | -42.00632 | 2024-11-22 11:49:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| c65083a7-1070-3280-a086-d27c29edc556 | -3.62176 | -42.3989 | 2024-11-22 11:49:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 144.5 |
| 255ce4ed-a8c0-3a82-adf4-0cf7fe1ef3a4 | -3.44489 | -41.47375 | 2024-11-22 11:49:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 168.1 |
| 8cc95921-b4d5-3871-bbac-d7a8a4725906 | -3.63886 | -42.37892 | 2024-11-22 11:49:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 34.8 |
| e28e8306-a6bf-3c3c-890c-fdcd136132a9 | -3.4486 | -41.4499 | 2024-11-22 11:49:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| adde155e-11d9-309d-b6a0-145ee196583a | -1.5447 | -47.2244 | 2024-11-22 11:50:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 2ce8d646-b7a8-3c4a-82da-5f32505d11b7 | -6.11974 | -42.52575 | 2024-11-22 11:51:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 7f8038fe-aad4-3a58-9355-f9ba7eebd4d7 | -7.47393 | -34.92258 | 2024-11-22 11:51:00 | TERRA_M-M | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| a294ad70-22c3-37e7-9d51-47993e45bb68 | -7.53818 | -34.9769 | 2024-11-22 11:51:00 | TERRA_M-M | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| b7c7e0a6-20d1-3a50-bc3d-027b18430d26 | -10.49988 | -39.37652 | 2024-11-22 11:51:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| d1d81f48-639b-3f6f-8a5b-9ace166e8416 | -6.12494 | -42.5044 | 2024-11-22 11:51:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| b552ec75-4ac1-3c28-ac11-b082c78f75f4 | -6.28538 | -37.79393 | 2024-11-22 11:51:00 | TERRA_M-M | JOÃO DIAS | RIO GRANDE DO NORTE | Brasil | 2405900 | 24 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 6160068f-3f67-3b6c-9282-8b4a5ff423c4 | -6.94293 | -41.18806 | 2024-11-22 11:51:00 | TERRA_M-M | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 7bda61f2-ddbe-3c78-b3f5-76d857596ef5 | -7.87711 | -36.8824 | 2024-11-22 11:51:00 | TERRA_M-M | CAMALAÚ | PARAÍBA | Brasil | 2503902 | 25 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 681e106a-a760-3b21-963f-a9123014b289 | -7.45051 | -37.55258 | 2024-11-22 11:51:00 | TERRA_M-M | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e09f16c5-bcc0-3d27-8b3d-d1e74eadc507 | -8.89855 | -37.87207 | 2024-11-22 11:51:00 | TERRA_M-M | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 14.4 |
| f3867be6-ddc7-347e-86b3-5e35f03ce40e | -9.20413 | -37.74899 | 2024-11-22 11:51:00 | TERRA_M-M | INHAPI | ALAGOAS | Brasil | 2703304 | 27 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 62a6a943-c40e-3b7b-99d1-83cad5ef8530 | -7.46509 | -34.92133 | 2024-11-22 11:51:00 | TERRA_M-M | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| f7e34262-da56-391f-aa39-6fd35369b8b8 | -6.84285 | -35.69974 | 2024-11-22 11:51:00 | TERRA_M-M | SERRARIA | PARAÍBA | Brasil | 2515906 | 25 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 337528a3-3cfa-329c-afb5-9af70c6fb67e | -6.11256 | -37.91824 | 2024-11-22 11:51:00 | TERRA_M-M | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 0fc5222d-62ae-3877-aed9-47f705266e10 | -6.08311 | -36.83118 | 2024-11-22 11:51:00 | TERRA_M-M | FLORÂNIA | RIO GRANDE DO NORTE | Brasil | 2403806 | 24 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 377734a2-3ad9-3032-88e4-ed619c40521d | -9.9391 | -37.96643 | 2024-11-22 11:51:00 | TERRA_M-M | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 70176f06-ca4f-30a8-a9d0-68fa15ccd3d5 | -8.52501 | -37.06224 | 2024-11-22 11:51:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 43acc272-878d-3ab9-9de9-a0a15d787064 | -9.58845 | -37.65003 | 2024-11-22 11:51:00 | TERRA_M-M | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 56ce49f0-ef6b-34fe-a535-d8db871ca18e | -7.59234 | -37.96362 | 2024-11-22 11:51:00 | TERRA_M-M | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 41.7 |
| ed35dc60-49a6-3928-bcdd-ec2f2cebf9bd | -7.7379 | -37.54893 | 2024-11-22 11:51:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 11.8 |
| dad047ce-be42-3561-ab6a-d1551f0eaaca | -8.93194 | -40.98632 | 2024-11-22 11:51:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 8fc3580c-818d-3dde-8105-3350bd60dcba | -5.98671 | -36.62809 | 2024-11-22 11:51:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 11.6 |
| adb333ae-53cc-3ae4-8760-0b14fb6414f8 | -7.6757 | -37.88917 | 2024-11-22 11:51:00 | TERRA_M-M | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 20.3 |
| be4b8535-45d7-3cc8-a3d8-360bccdefe7f | -5.99434 | -38.9797 | 2024-11-22 11:51:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 29.4 |
| 4f0cc861-dc13-3b8a-93b9-af736f6e5ae4 | -7.53946 | -34.96804 | 2024-11-22 11:51:00 | TERRA_M-M | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 75f00015-273d-3eac-bdcc-9b9450cacdd6 | -5.79846 | -35.58499 | 2024-11-22 11:51:00 | TERRA_M-M | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 91395a18-753b-3828-9988-1c24f38b8fcf | -10.24962 | -39.3435 | 2024-11-22 11:51:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 46.1 |
| ea469ce6-0c4a-3eac-b31e-c3db2d1080d3 | -7.32063 | -37.25826 | 2024-11-22 11:51:00 | TERRA_M-M | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e35a6868-7ac1-3937-8849-bfcb39002626 | -6.84313 | -36.51498 | 2024-11-22 11:51:00 | TERRA_M-M | PEDRA LAVRADA | PARAÍBA | Brasil | 2511103 | 25 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f213700e-e34b-3ef0-93ce-ccf96d7a7384 | -7.50719 | -37.63936 | 2024-11-22 11:51:00 | TERRA_M-M | ÁGUA BRANCA | PARAÍBA | Brasil | 2500106 | 25 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 699c36da-bb70-3b7b-971c-e4a17959a4db | -7.50721 | -37.44016 | 2024-11-22 11:51:00 | TERRA_M-M | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 165ccbea-b319-3836-873c-b72e2cba8424 | -10.90775 | -38.27351 | 2024-11-22 11:51:00 | TERRA_M-M | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| c7daf981-4a23-35d9-89c1-195a54d4ebb3 | -13.019 | -44.46147 | 2024-11-22 11:53:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 97650890-c073-3016-be3d-9896e9e4cd2e | -3.4237 | -42.119 | 2024-11-22 12:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 511.9 |
| a4a61803-499d-396f-aa29-3406e38c3e10 | -3.405 | -42.1199 | 2024-11-22 12:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 353.4 |
| 784f1020-61d5-31ef-8e8d-23c06df02cdd | -3.4235 | -42.1427 | 2024-11-22 12:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 161.0 |
| 70a63344-355c-39d0-89d1-e14b2fd0eaa5 | -3.4048 | -42.1436 | 2024-11-22 12:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| af9fdd1f-6102-355b-bf59-df7140c35089 | -3.4237 | -42.119 | 2024-11-22 12:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 192.7 |
| bedcbcb0-6933-3d3a-b0c0-202c6a16751e | -2.9488 | -48.0153 | 2024-11-22 12:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 265.4 |
| fa5e7de9-cef3-3ee9-8a6c-e6fd9876a3a1 | -3.4235 | -42.1427 | 2024-11-22 12:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| d485e74b-43dc-37fe-a737-0f2885ecfca7 | -3.405 | -42.1199 | 2024-11-22 12:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| d4aba32f-c9e0-3662-9a53-aa0e08e4ff42 | -1.7892 | -53.6293 | 2024-11-22 12:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 26dc6e13-ad86-349e-a829-83657dd0ae23 | -3.4237 | -42.119 | 2024-11-22 12:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 566967d7-ca92-3d8b-9b2f-a269b5a06aef | -1.2572 | -53.3534 | 2024-11-22 12:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 04ec0950-794a-32e9-94a4-ec1e21e7aad3 | -1.7892 | -53.6293 | 2024-11-22 12:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 9993a982-9125-31cf-9fd8-6e0a298f6c6e | -0.2667 | -51.5835 | 2024-11-22 12:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 71.3 |
| df92f080-78ae-3e6c-afbe-047c6f3bd6c2 | -1.1287 | -53.3951 | 2024-11-22 12:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 08d3d353-db27-3c08-be20-72fd6e06f1ce | -1.2572 | -53.3534 | 2024-11-22 12:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9e18a52f-cb11-3a54-ac84-86f59b91b570 | -1.1287 | -53.4153 | 2024-11-22 12:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| adebc3f9-110b-317f-a72a-06e8174de9f8 | -0.2667 | -51.5629 | 2024-11-22 13:00:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c6798028-8e48-3abd-9ac0-f165ca3b719b | -6.9118 | -47.5382 | 2024-11-22 13:00:00 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 652775d8-21a6-3863-98b9-6030c0bc781b | -3.3306 | -42.0522 | 2024-11-22 13:00:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 209.5 |
| 272a7f01-df1c-367a-88d1-1d2c49fb192d | -1.7708 | -53.6094 | 2024-11-22 13:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 58f1a617-6aee-3e4f-979d-7c9548ecb1fc | -5.4548 | -43.2426 | 2024-11-22 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 337d7011-2700-325d-a2c4-5df3f997e0f9 | -0.2851 | -51.5629 | 2024-11-22 13:00:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f2d92453-9e59-310d-a329-132e1ce4d307 | -1.1287 | -53.3951 | 2024-11-22 13:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 23930ca3-2fb1-3281-95b5-804320ba02e2 | -1.7708 | -53.6094 | 2024-11-22 13:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d620d31c-6c25-38fc-9bfd-482bcdc209c6 | -1.7892 | -53.6091 | 2024-11-22 13:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 9a20daf0-285e-343c-b93d-757540506200 | 1.3819 | -55.9455 | 2024-11-22 13:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| b99a9072-e642-3ed6-b632-fc9f5a009ad5 | -3.3306 | -42.0522 | 2024-11-22 13:10:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 60387551-f64b-3db2-baf6-71b3fc94ff0c | -6.9118 | -47.5382 | 2024-11-22 13:10:00 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 867d0cfb-a7f9-3f2c-ac7a-c1bda741cff9 | -7.5892 | -37.9589 | 2024-11-22 13:10:00 | GOES-16 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 9cfa1c06-0f16-3f7f-bce9-f427af097104 | -3.1438 | -42.0369 | 2024-11-22 13:10:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |


[Clique aqui para ver as próximas entradas](README69.md)
