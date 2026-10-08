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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b4132e4-4b59-3b31-bf8e-900048ce02dd | -9.4936 | -64.3518 | 2026-10-08 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 160650fb-9acf-3d51-98ef-c87a3a68c58f | -3.1697 | -58.6437 | 2026-10-08 03:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| d6a59a6a-e063-3ca5-835d-f4f98c2c3690 | -2.517 | -56.1656 | 2026-10-08 03:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| fcea75a0-411e-3147-87d0-c9972e73a9ce | -7.0065 | -59.1223 | 2026-10-08 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 687a3453-f9a9-3963-824b-18c5357388e8 | -5.6931 | -53.5073 | 2026-10-08 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 3a9c9d04-7990-33ea-ba80-e5359721ed23 | -11.6369 | -43.6876 | 2026-10-08 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f5a7dbf5-0e7f-34d4-a4a9-ad1b7fa9fe39 | -3.1786 | -50.6016 | 2026-10-08 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f61e40be-aa0e-339f-985f-731410514294 | -2.7796 | -54.0937 | 2026-10-08 03:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a670f076-0714-3f63-97c4-1c76acfd3bc4 | -8.3882 | -46.3006 | 2026-10-08 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 456e8789-81c0-3cd0-bf8a-87de29e16d3d | -2.4032 | -57.8848 | 2026-10-08 03:00:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| a6f2274b-3e0c-35f8-b0c8-a66134f9f79f | -3.1101 | -54.1661 | 2026-10-08 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 252cab0a-6f36-3258-8e74-7d477636ea20 | -2.4988 | -56.1462 | 2026-10-08 03:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 9ae25f91-92b1-37f9-82eb-a6ff4395e0d5 | -8.742 | -45.1563 | 2026-10-08 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 0524153d-04f9-32d7-bb09-79995e20ba85 | -2.7797 | -54.0736 | 2026-10-08 03:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e8ca1f24-6f3d-3e33-a0d4-a58731ab9060 | -5.7117 | -53.4862 | 2026-10-08 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 37cc1d51-4563-33fe-891a-210fd683c00b | -3.1114 | -53.7839 | 2026-10-08 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 4d61064e-724e-39a0-9ff1-fb2f57996eb6 | -3.0913 | -54.287 | 2026-10-08 03:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 6061fbb6-aeb8-32d3-9112-420731bec58f | -3.1972 | -50.5592 | 2026-10-08 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 24c14d67-4882-360d-ab51-b05c0204d4fb | -3.0741 | -53.946 | 2026-10-08 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 7e12fe02-1f18-3711-ab75-7e44196bdc07 | -8.7561 | -67.7115 | 2026-10-08 03:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a988aa62-c212-37d8-8730-e71ee928d770 | -2.572 | -56.1646 | 2026-10-08 03:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| bc876acc-be63-3162-bc7b-11d110711f7f | -8.7228 | -45.1812 | 2026-10-08 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 110ec54a-252f-39d4-aa1a-b154d47aac37 | -3.11 | -54.1862 | 2026-10-08 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a82ce3d2-1676-3565-885c-e7a48ec0398c | -2.499 | -56.0675 | 2026-10-08 03:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c53b6b97-abcc-3fc5-a111-69b45d42bb2d | -8.7231 | -45.1583 | 2026-10-08 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 2fb3243b-14f2-3b12-8cbe-ed90dec49be0 | -6.1617 | -47.9201 | 2026-10-08 03:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| cd947548-2660-3f74-ad82-290f70802db7 | -1.5306 | -54.5558 | 2026-10-08 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| bde82155-4076-3c07-a710-f55031c643ea | -6.15991 | -39.43229 | 2026-10-08 03:04:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| a409fdbe-f63d-36b2-8aeb-3e431dd41696 | -6.15867 | -39.43885 | 2026-10-08 03:04:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 68698740-7730-3ebd-b62d-4c1ba9ee6d41 | -5.23409 | -38.55049 | 2026-10-08 03:04:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e0545a14-b01b-37c4-a2b4-ec0cc676e2b9 | -6.15298 | -39.43068 | 2026-10-08 03:04:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 8007b95a-5eb5-3341-b281-a76b6b23c8fe | -6.16126 | -39.43314 | 2026-10-08 03:04:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| caa6bdc8-b4af-3032-827d-755a32c56e18 | -6.15312 | -39.43815 | 2026-10-08 03:04:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9edc8b1a-41eb-3026-a08f-dbcb55ecde0f | -6.1656 | -39.44046 | 2026-10-08 03:04:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2121bcde-515a-303c-adc2-8d7e093f2f8a | -6.16699 | -39.44135 | 2026-10-08 03:04:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 07d24152-edb4-353d-aacd-b2282c43e4b8 | -6.16006 | -39.43974 | 2026-10-08 03:04:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 2bba93ad-14f2-3a20-baf8-a2922bf768c0 | -6.15434 | -39.43148 | 2026-10-08 03:04:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 775d94e5-dfae-31f1-88a0-1893bd577fef | -6.83553 | -39.5547 | 2026-10-08 03:06:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 303db82b-7b23-36de-a571-da9653cbfb48 | -6.82167 | -39.55171 | 2026-10-08 03:06:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 050670d2-e2e6-3409-b36a-8250b67d3aee | -10.24834 | -36.34222 | 2026-10-08 03:06:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 7e740c25-dee3-39d4-961f-986c40721182 | -10.1542 | -36.17619 | 2026-10-08 03:06:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f1435c1f-8824-3021-ba13-f612e903707b | -6.83661 | -39.54893 | 2026-10-08 03:06:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8b496788-1fb7-32c6-b8ae-2ccf7eef74aa | -10.15357 | -36.17956 | 2026-10-08 03:06:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 75ea0f52-fa45-3d2d-aa51-bd75a7f0801d | -6.82869 | -39.55275 | 2026-10-08 03:06:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3f130353-c5b4-3bb5-9e5a-8622ed6ddc32 | -6.84354 | -39.55039 | 2026-10-08 03:06:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e0465b68-a27b-3594-87c5-f3cba258b52b | -6.83457 | -39.55981 | 2026-10-08 03:06:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1b41e40a-e721-32e9-8dba-345b61d2c5b8 | -10.24899 | -36.33871 | 2026-10-08 03:06:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 92d1601b-e887-3b84-b886-1492c93a99bd | -6.82285 | -39.54548 | 2026-10-08 03:06:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a2a4dbe4-bc47-3fe1-98f4-bcc384f16c7e | -6.82763 | -39.55838 | 2026-10-08 03:06:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 042887c2-1288-3fdd-8501-1e9af254c770 | -16.83832 | -41.04531 | 2026-10-08 03:08:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8fc09bcf-1c50-31b4-b27f-c38925f822ee | -16.87601 | -40.61161 | 2026-10-08 03:08:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 84aca6c8-5ce0-3bf4-957b-22bc7c1c163f | -17.764 | -42.42888 | 2026-10-08 03:08:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| a1d8beb2-0d0d-3599-a29e-c34e82067b52 | -16.87715 | -40.60655 | 2026-10-08 03:08:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| b28f42d4-b097-3a7a-a281-cc0de991c0c7 | -16.84463 | -41.04715 | 2026-10-08 03:08:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 50543756-79c3-3738-954e-7e5610244e76 | -16.85857 | -40.584 | 2026-10-08 03:08:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bf531cba-1a57-3b15-8554-03463b51b748 | -17.50126 | -41.91491 | 2026-10-08 03:08:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8db0cf6d-f684-3c3a-b013-3fdb6eb513f1 | -18.26363 | -42.17314 | 2026-10-08 03:08:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 809953e9-6e3f-3386-9d03-7c78fa40f4cb | -16.87274 | -40.60892 | 2026-10-08 03:08:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 53028487-f8e2-3bdc-a76d-4ad28855254d | -16.89972 | -40.88976 | 2026-10-08 03:08:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a318df9e-8f76-3fb1-8e0d-9f05f560939a | -18.37339 | -41.95813 | 2026-10-08 03:08:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 58132714-2e07-36c3-982c-127fd38209ea | -17.54053 | -41.69245 | 2026-10-08 03:08:00 | NOAA-21 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ff3f3b30-eb23-3ea0-bc79-42430484bdeb | -17.50787 | -41.91651 | 2026-10-08 03:08:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| a5b0e560-170a-39e8-afa7-04442ba22002 | -18.38767 | -40.31945 | 2026-10-08 03:08:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 80cfc58b-4b94-3b13-baed-8949b4b0e746 | -16.85393 | -40.57535 | 2026-10-08 03:08:00 | NOAA-21 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 27535a5c-b594-30ba-9c11-0c23a5c08406 | -16.85973 | -40.57872 | 2026-10-08 03:08:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69a2b787-5e71-31d1-a110-dd16485c9082 | -17.43815 | -41.36227 | 2026-10-08 03:08:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 082d8cc3-f2fb-3bb2-9a18-f9bea169b5af | -16.87383 | -40.60394 | 2026-10-08 03:08:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0e13e0f2-689b-357c-a675-cd42a29eaba1 | -17.43171 | -41.36076 | 2026-10-08 03:08:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c7ec0c45-fd30-3e61-8ba3-dea11890132d | -16.89171 | -40.89589 | 2026-10-08 03:08:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 77b0d058-a60d-37c5-9e2b-7808b55c21de | -17.71232 | -42.03064 | 2026-10-08 03:08:00 | NOAA-21 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 556a1028-eeaa-394c-9f0f-7be91fb1821c | -18.25678 | -42.17249 | 2026-10-08 03:08:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a4ab8778-b71d-3c26-a43b-d47a49a2c6be | -17.71364 | -42.02489 | 2026-10-08 03:08:00 | NOAA-21 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 830755f7-b5ad-342d-a696-efe01ac13075 | -18.38574 | -40.31853 | 2026-10-08 03:08:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5f17705c-aaa3-3a99-9303-8e0815f2f6f9 | -16.89332 | -40.8886 | 2026-10-08 03:08:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 573fa804-1e4a-35d0-bd0d-4901227bc464 | -17.76501 | -42.42926 | 2026-10-08 03:08:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2ebb58cc-d5fa-35e7-91ae-ad600bbc3741 | -17.10781 | -41.35363 | 2026-10-08 03:08:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 40968d28-1a31-3ec6-8bac-1aad78e75321 | -17.11712 | -41.34251 | 2026-10-08 03:08:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f5780396-a536-3345-8c3e-89cb075fe38b | -16.83189 | -41.044 | 2026-10-08 03:08:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 12956ad4-6ca9-34b0-a237-0b20a423d349 | -17.9813 | -41.44803 | 2026-10-08 03:08:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f561063d-c74b-3f77-830b-7847868aa653 | -2.7335 | -57.4717 | 2026-10-08 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 1f6a515d-b58a-3d95-b1b4-a8118ad40fe4 | -6.1429 | -47.9432 | 2026-10-08 03:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5256cd72-a00a-3f7c-b1fd-cfabb3dedba0 | -3.1786 | -50.6016 | 2026-10-08 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| da4dd419-3724-3d1a-b324-e923d9a33320 | -2.4988 | -56.1462 | 2026-10-08 03:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 30baa183-2d3c-33c0-8003-98c0e5f0ca72 | -2.4805 | -56.1072 | 2026-10-08 03:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 2b5b5503-41bc-3cc0-b7f5-6b94e6bc3490 | -3.074 | -53.9661 | 2026-10-08 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 26d4ae6f-b313-3995-b3c8-d161411dd639 | -3.073 | -54.2874 | 2026-10-08 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ca2a319a-c82a-39a0-9f7d-726c30d1d010 | -5.7117 | -53.4862 | 2026-10-08 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 32fed279-be73-3abc-b87b-306622aba92e | -3.0374 | -53.9268 | 2026-10-08 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c81d8591-f481-3beb-8e72-efe99b93be7d | -2.4031 | -57.9041 | 2026-10-08 03:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 8c874791-2a16-3dbf-8db4-56223adbd1af | -8.7228 | -45.1812 | 2026-10-08 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 059016e5-4ad1-36e8-9560-7cd2e2fe3e47 | -3.6049 | -54.5736 | 2026-10-08 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 63265728-22f6-331e-8c80-b99da73bc78d | -3.1115 | -53.7637 | 2026-10-08 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| c9e93b78-8e3e-3c92-8263-b5c6537395ad | -6.1431 | -47.9214 | 2026-10-08 03:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| ece3cd18-39d2-35d0-9fe3-c2df94515964 | -3.5865 | -54.5742 | 2026-10-08 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 42601081-483d-31c9-9966-c8f342f2b130 | -3.2157 | -50.5586 | 2026-10-08 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| c2dae3ad-ef47-356a-a137-01192554f833 | -2.4987 | -56.1659 | 2026-10-08 03:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a93ce4b7-88f5-37d3-aa16-052d7d472e27 | -2.4032 | -57.8848 | 2026-10-08 03:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 3e99467d-6659-3060-9f2c-5c4b0d009c4b | -9.4936 | -64.3518 | 2026-10-08 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| bccdf233-4f7b-3065-8791-c5e07b60445b | -8.3882 | -46.3006 | 2026-10-08 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 2a110755-abbd-32ee-8383-1d21f64d60e7 | -8.7231 | -45.1583 | 2026-10-08 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |


[Clique aqui para ver as próximas entradas](README54.md)
