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

## Dados Diários - Página 393

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e3fd859-d6e8-3096-9fcd-49ac8c5d9677 | -7.1886 | -44.3503 | 2026-10-08 18:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| da68829e-bcec-3097-9fa9-ad4929fafe5a | -2.8896 | -54.1715 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 63a04a9f-9cc3-3160-a55e-2450c7dd7a99 | -2.7152 | -57.472 | 2026-10-08 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| b62b21cb-3bef-3f6a-ae6e-8285267808c7 | -8.6136 | -44.873 | 2026-10-08 18:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9590f026-c7c2-3c53-a60a-cc54ef14befe | -11.2849 | -45.2063 | 2026-10-08 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 082d7026-9831-322c-9fdf-914360db9865 | -1.5306 | -54.5558 | 2026-10-08 18:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 05129691-d512-3a00-90e0-14266efa2079 | -3.7239 | -57.1384 | 2026-10-08 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| a55a811d-b78c-3967-a052-17a04ae9216e | -3.8383 | -55.9774 | 2026-10-08 18:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0d68a1d5-cecc-339e-93cf-1d0c4b92a78d | -5.3905 | -44.1968 | 2026-10-08 18:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 36758f2c-9bac-3cec-86f9-457c59454771 | -6.1617 | -52.6471 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 599b8974-9bb2-3eb8-bd37-efe0aba75ec8 | -4.934 | -42.8108 | 2026-10-08 18:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 1bd797d7-0a53-3c82-8790-73de23046e0f | -6.8952 | -43.6833 | 2026-10-08 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| dcf52070-6ec2-3723-80fd-80ff0a278a3b | -14.3608 | -55.032 | 2026-10-08 18:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| b5135c8b-17c5-3821-bb46-01740779fc2c | -8.5554 | -66.9759 | 2026-10-08 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 86288b65-f14c-3281-b328-261f4bdc2a44 | -15.1057 | -43.6168 | 2026-10-08 18:30:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 135.1 |
| 97678b8f-519c-30fb-a371-6be416feb997 | -17.1012 | -41.3472 | 2026-10-08 18:30:00 | GOES-19 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.7 |
| cda08142-634f-3a5c-8384-6bdc9407b69e | -5.9649 | -40.914 | 2026-10-08 18:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 52ceae7b-78f4-3f05-8d6c-5344dd2c3034 | -3.4277 | -58.0397 | 2026-10-08 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| af29bdf6-f5c4-30d1-819e-9991b90c4235 | -9.1362 | -65.3022 | 2026-10-08 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| b29c2d2c-e7f8-3bcf-acde-e1dc88e6e449 | -3.2956 | -49.1415 | 2026-10-08 18:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 77b7ca29-eab5-30b2-98ba-11faef36c5b5 | -2.9633 | -54.1095 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f8390d5a-d27b-37f6-b68c-e06aebe00131 | -1.3264 | -56.398 | 2026-10-08 18:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 1b10d089-2486-33b0-8ab2-5c58465aba09 | -12.2316 | -44.7427 | 2026-10-08 18:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| bd79227d-0e18-3852-8fef-cbc696280a79 | -10.9384 | -45.3916 | 2026-10-08 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| b50d6c63-017a-3e82-a5ab-1b3bc7f05e25 | -11.7545 | -43.5512 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 3e8e114b-baa9-325c-95e4-8e36cb23e33d | -1.5489 | -54.5556 | 2026-10-08 18:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| b83ebdb9-a507-3c6c-a2db-0265d0cd7ec4 | -9.3565 | -65.7623 | 2026-10-08 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 4202f6cd-cad9-3742-b2bb-95a0188f5ded | -14.0873 | -43.7671 | 2026-10-08 18:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 230.0 |
| 132168da-c21b-3412-81a5-6df367498880 | -11.0953 | -44.0037 | 2026-10-08 18:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| c9267c50-83bb-38bd-8c72-e67f7d74bb65 | -11.4695 | -43.4062 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 648986e8-942f-3d79-86be-c62a214ea38b | -7.4697 | -42.8315 | 2026-10-08 18:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 142.5 |
| fcf54b8d-e227-3e47-8c46-ab79ec838c76 | -3.9121 | -55.8964 | 2026-10-08 18:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| f8587763-2c06-3267-9df9-3e864709bee8 | -2.8228 | -58.361 | 2026-10-08 18:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 46e58196-a028-37dd-9b16-1ad55d1c0654 | -2.5903 | -56.1642 | 2026-10-08 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 1fa4aab0-2147-3464-8961-81033129489c | -9.1257 | -67.8322 | 2026-10-08 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 130.7 |
| c19e9963-8a7e-3e78-b027-4995a94f4965 | -6.0386 | -51.7261 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| b95680ea-be50-3053-9475-ab03d80b14c9 | -3.2451 | -57.8693 | 2026-10-08 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 49cab2af-4858-3476-a450-b25d11c177b0 | -6.737 | -55.0674 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 8165967e-b9c1-3806-989f-d67939f23b8c | -3.2533 | -50.3899 | 2026-10-08 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| a818d710-d90c-3b04-afb0-4df4726f9b88 | -7.3941 | -44.469 | 2026-10-08 18:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 9227f4b5-2793-3de6-adcf-a93defc679ec | -12.0448 | -43.434 | 2026-10-08 18:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| e8f86418-f3aa-37e0-958f-0056e746c943 | -9.6627 | -45.5757 | 2026-10-08 18:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 9b60fbce-1da9-30f9-822c-bb3441b6768c | -5.9936 | -55.6815 | 2026-10-08 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 100e9e28-aa29-3011-bf3f-85e6bc8af628 | -10.4724 | -47.2333 | 2026-10-08 18:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 58c5ecb0-e648-3269-b898-26e19ba6620d | -13.395 | -43.4652 | 2026-10-08 18:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0742e61b-ccaa-3d53-9e8d-eaaf8bf38f08 | -3.3141 | -49.1409 | 2026-10-08 18:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 0293d4ad-5120-3bf9-bd0d-2fe84f2628ae | -3.2031 | -53.8621 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bedcd4e3-df07-3489-90b5-2d1b0e2ca8a9 | -1.2728 | -55.4135 | 2026-10-08 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 62d1f719-b8fa-33ef-80ef-cdc13a1671f5 | -11.6387 | -43.5929 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 095d1615-8144-3236-9fc0-2e1979cec2a4 | -6.2485 | -53.4592 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1d3dc003-e679-3447-95e0-bc9c264f6fe7 | -14.4345 | -43.9157 | 2026-10-08 18:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 269.9 |
| db079324-1917-31e6-b4eb-c62da4dd8c8b | -6.3232 | -46.5459 | 2026-10-08 18:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cc9ff5c8-a33a-34b4-ab6b-e2f87c7c8d8f | -1.6213 | -55.1123 | 2026-10-08 18:30:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 30baa808-8659-3425-bc43-a4797b59347a | -3.1951 | -42.9538 | 2026-10-08 18:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 40da3d16-6500-3fd7-9183-9642557a626c | -1.1094 | -54.1601 | 2026-10-08 18:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8ff61218-8874-3acf-b0dc-46faa0406a0c | -14.0472 | -43.8222 | 2026-10-08 18:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 213.8 |
| acb7cad4-26e8-32da-ac61-d0763420e20c | -15.3419 | -42.7704 | 2026-10-08 18:30:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 6835c294-0dc4-3a63-8afc-2dd84c692c21 | -11.2657 | -45.209 | 2026-10-08 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| ea1cad62-7b45-3f27-93a6-56cdcf7c3621 | -5.9647 | -40.9383 | 2026-10-08 18:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| c65f3989-96ff-3a45-a332-e36b2fe274e8 | -3.2945 | -54.0006 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 6acb3293-b7b5-334a-b002-6134143f5508 | -3.724 | -57.1189 | 2026-10-08 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 703899dd-487f-3c8c-b54e-3500198ab622 | -4.0838 | -44.1159 | 2026-10-08 18:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 269.7 |
| da6a8ee8-6bf1-380b-9a95-abdc57a6a519 | -6.0609 | -42.608 | 2026-10-08 18:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 52.7 |
| f059999c-18e4-3ac5-8567-9695d5dd4098 | -8.5183 | -67.0139 | 2026-10-08 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 62fe112e-f5c7-3d31-b697-d871ee9f4f57 | -6.8764 | -43.685 | 2026-10-08 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 89dcd68d-48e7-365c-92f3-25df97d15ef8 | -3.7057 | -57.0998 | 2026-10-08 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| d9a6a104-f8ac-32b3-ba0a-6ecb4ae899b9 | -2.8347 | -54.1125 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 61f1b781-65fe-3daf-9d0f-34a4fe97b3b2 | -8.0766 | -45.6112 | 2026-10-08 18:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 505.5 |
| 001fc8cc-d1b1-3d3c-a4e7-8ea009a0a350 | -7.1825 | -52.6283 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| b3113146-8c78-3a89-b5b0-ca2ac71214ae | -6.1217 | -53.0584 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| ad037285-35d7-374c-a9f4-f85b47885385 | -12.0256 | -43.4371 | 2026-10-08 18:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 821.1 |
| 93165f7d-d0e5-351b-a276-80d0d34cba08 | -5.9586 | -55.3648 | 2026-10-08 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 9f12245b-745b-3991-bf0b-9998f0bad435 | 1.6937 | -55.6263 | 2026-10-08 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a8e83bb6-a709-3f6c-a38b-46af55ff73a5 | -6.1977 | -52.7886 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 887c6cce-7ff0-3661-b886-2610076bde32 | -9.1072 | -67.8141 | 2026-10-08 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 11a73d1e-7dec-3ad4-a193-2b1ef3f4bf11 | -3.2633 | -57.8883 | 2026-10-08 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 133.5 |
| adbce455-1635-3f5c-b7e4-766211b0d58d | -5.6136 | -44.3647 | 2026-10-08 18:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| c1bfe7e4-db74-3cf3-9795-f115744417d6 | -11.6186 | -43.6433 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| cc981115-25af-3065-ac9a-ba39b50a1e5e | -3.7809 | -41.7913 | 2026-10-08 18:30:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 232.9 |
| 4c09d5f7-d486-3713-ae5a-744a6de703dd | -6.7368 | -55.1074 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 962c41fe-9ba0-3316-a7ed-058c3b05bbf7 | -5.4956 | -42.8648 | 2026-10-08 18:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 161.6 |
| 34fc65c4-2827-3ce8-ac96-0cfbd64d9815 | -2.5721 | -56.1449 | 2026-10-08 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b1c34d98-9c08-35f8-8175-eb591a821e6c | 3.5448 | -51.2772 | 2026-10-08 18:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 57.2 |
| eee2a5a8-1288-3a69-9a53-6e22b2cc17d2 | 1.7672 | -55.5463 | 2026-10-08 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 610fee3e-a922-3c51-85f6-4426eecc1dc3 | -5.3718 | -44.1981 | 2026-10-08 18:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 300.8 |
| 78d42ae6-cd26-3f7f-9918-1881d45cdec3 | -6.7185 | -55.0684 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| dccf3303-ed2d-3206-ad15-e3cf3ad2c65b | -11.755 | -43.5275 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 5c5fcf66-3a2b-3a60-9878-a2c4e4d20158 | -13.8855 | -44.1127 | 2026-10-08 18:30:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| c34299e2-6c99-33a3-8a64-710d3c5acf79 | -7.4694 | -42.8551 | 2026-10-08 18:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 119.1 |
| a15abbb4-d05e-3a2b-956a-e3bf619330e4 | -3.3128 | -54.0202 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| af14a0b9-98f7-3b86-ba01-db914396deea | -9.3394 | -65.4638 | 2026-10-08 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 8826cd07-f485-34f5-bc1e-792a7a99094e | -4.6641 | -56.2281 | 2026-10-08 18:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4a340443-97d9-3f86-89e6-f157360807c5 | -6.6027 | -37.8944 | 2026-10-08 18:30:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 120.0 |
| 9b5ab8e9-80b6-3a78-8f64-d9ec595f2aed | -2.8346 | -54.1326 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 216.4 |
| 7365dcd0-f8ea-3757-b232-8556cd46df44 | -8.9082 | -49.986 | 2026-10-08 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| ad029812-2214-36af-a042-c98b1f707253 | -4.576 | -40.657 | 2026-10-08 18:30:00 | GOES-19 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 7e50c602-0f8f-388b-8200-83a29156d304 | -9.1072 | -67.8326 | 2026-10-08 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 220b40c4-77d4-3106-98c0-90440a1a8fa0 | -6.7366 | -55.1274 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 231.2 |
| 874e0405-e79f-3618-80d2-23013345a7a3 | -2.9264 | -54.1505 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 98c75360-5a4a-32c2-b57e-9aa96103415d | -6.1501 | -51.6992 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |


[Clique aqui para ver as próximas entradas](README394.md)
