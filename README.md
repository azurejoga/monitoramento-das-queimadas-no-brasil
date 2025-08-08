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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d48e59c9-8c9c-32fd-a63c-2f94fc7f87e8 | -18.9117 | -47.5439 | 2025-08-08 00:00:00 | GOES-19 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 736fff22-bedf-33a1-914e-e35e2b29b46f | -10.6247 | -44.767 | 2025-08-08 00:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a2399c29-29f2-384e-8db8-6bf5196c9d2e | -8.9213 | -60.7489 | 2025-08-08 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 157.9 |
| 0421a864-3703-3caa-9778-4805d409f71e | -11.8062 | -44.9234 | 2025-08-08 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| a4eabe16-32b0-3e45-be15-1992a9c801f2 | -13.035 | -56.8562 | 2025-08-08 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 54e3c824-a90b-3889-9208-f171dca9733b | -5.9901 | -44.1297 | 2025-08-08 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| c9f1a6d1-4068-355b-be3d-95e55b02f732 | -5.9711 | -44.1542 | 2025-08-08 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 264.9 |
| 3bbb1143-f6a4-38d7-a973-d672eadc4f79 | -5.9713 | -44.1312 | 2025-08-08 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 44ac4bc4-4834-356a-8803-9f4b40a48840 | -5.9899 | -44.1528 | 2025-08-08 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 301.2 |
| 6d62f232-58df-3f36-b118-fcd25dabd3e3 | -8.9399 | -60.7481 | 2025-08-08 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| d846ca0b-14c2-3cdc-a0c8-9e3f808b6eed | -8.54 | -43.3041 | 2025-08-08 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c2ffd5dc-6dbd-3172-8cc3-593f3af69b40 | -8.9401 | -60.7288 | 2025-08-08 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 34a6c530-062e-3e76-8184-41601d7a6fd6 | -11.0201 | -45.059 | 2025-08-08 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| f90e4f76-b472-339d-9b03-647d764cedb5 | -8.9215 | -60.7297 | 2025-08-08 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 3ff9bbd9-c4d6-32e8-88f0-4a7df6b8b880 | -13.054 | -56.8545 | 2025-08-08 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 248341f3-0101-339f-b9de-dd6f1b37640c | -5.8083 | -59.2262 | 2025-08-08 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d8138739-5130-35ec-928f-bf09c1a8b385 | -8.9042 | -60.5385 | 2025-08-08 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1486fe5f-34de-3636-a8ec-d2b6575851d2 | -8.5211 | -43.3063 | 2025-08-08 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 15f91e00-59da-3aec-a423-e30faded9d54 | -8.9041 | -60.5577 | 2025-08-08 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| bc35a4ef-2f0a-39d1-94f2-f3d5cd636d41 | -21.00799 | -43.27621 | 2025-08-08 00:05:00 | TERRA_M-M | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| c383f449-4ae3-36e4-88ad-1e67b09750d5 | -19.23633 | -46.58509 | 2025-08-08 00:05:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 66658c75-9472-3107-81d2-9f7a160f3384 | -19.18966 | -45.06271 | 2025-08-08 00:05:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| e33f7124-19d6-3bcb-8bbb-fc1a60c1413c | -19.19473 | -45.05625 | 2025-08-08 00:05:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 286b816a-e9b3-3b18-9fbd-70ac568f584d | -20.77185 | -43.51603 | 2025-08-08 00:05:00 | TERRA_M-M | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 9c0d54c5-64bd-3162-b02d-6460a943666d | -21.00491 | -43.28223 | 2025-08-08 00:05:00 | TERRA_M-M | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| cc67da8e-9550-333b-83bf-084ddba47fd9 | -12.07441 | -43.98981 | 2025-08-08 00:07:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 41e690cb-db5b-32a4-8351-8f2aec4b3bcb | -18.91363 | -47.56677 | 2025-08-08 00:07:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 87.9 |
| bf716fc6-8583-3e93-a46a-713d5ddcab92 | -12.06877 | -40.25543 | 2025-08-08 00:07:00 | TERRA_M-M | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| cf63d4e0-e823-3041-a8d9-3be1b85400ef | -14.4867 | -43.24612 | 2025-08-08 00:07:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 17e02ee7-167e-3eeb-a2ea-0fa39fca7afa | -11.79598 | -44.9404 | 2025-08-08 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b457f169-30bb-3592-b693-87775a3fb6bc | -13.36112 | -43.76823 | 2025-08-08 00:07:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9d0e07ee-610c-3d69-b821-a3d69412a140 | -18.91191 | -47.57254 | 2025-08-08 00:07:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 355fda27-0821-3977-971d-f08d4d268cfa | -16.21156 | -41.34097 | 2025-08-08 00:07:00 | TERRA_M-M | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 3fa09f71-219b-3489-98a3-0d61fa3147cd | -18.86382 | -45.13919 | 2025-08-08 00:07:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 9783b2fe-8291-30ea-bc39-8d0c5cfc970e | -15.89554 | -40.02815 | 2025-08-08 00:07:00 | TERRA_M-M | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 46096b63-67a3-344b-bad4-134bea2c211c | -11.56434 | -44.85816 | 2025-08-08 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 1108eb1c-25b4-366e-9811-0eac882f8d8a | -11.8066 | -44.93901 | 2025-08-08 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 9744cca2-020c-3e62-bcf5-1c642162af47 | -15.83828 | -41.85513 | 2025-08-08 00:07:00 | TERRA_M-M | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 93313460-fa5a-3948-a32d-a9c2b22b9f24 | -13.03546 | -44.08925 | 2025-08-08 00:07:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 1f52d1d9-e60b-303c-89f8-1293080a552f | -16.88454 | -42.06042 | 2025-08-08 00:07:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 18a5d984-3d15-3fcd-bbd7-b069679f8ad3 | -18.9091 | -47.54476 | 2025-08-08 00:07:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 40.9 |
| cf6abf85-7bf7-3864-87dc-ed08fd8bbbd5 | -11.79435 | -44.92719 | 2025-08-08 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 472949d4-6e4b-3dec-aed1-d35ac46b327d | -15.6855 | -43.20935 | 2025-08-08 00:07:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 96026054-07e3-3de7-bcc2-0c7047bd007a | -12.89338 | -43.77881 | 2025-08-08 00:07:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ec64dd27-ba81-3d09-a836-f03b6f67909d | -11.46714 | -47.32015 | 2025-08-08 00:07:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c815a99f-e6b7-3911-981c-b2046b1fd22b | -17.22861 | -39.28384 | 2025-08-08 00:07:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 47734924-9430-3004-98a7-9671e1959b2e | -12.09731 | -44.72383 | 2025-08-08 00:07:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9f57f5bb-40f6-39a7-a2b1-caf748452892 | -11.75002 | -47.51206 | 2025-08-08 00:07:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 8e35ad4d-08a0-38b1-b5c1-c13c1830a17a | -12.49123 | -47.50431 | 2025-08-08 00:07:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| b9b383e9-6fdf-322d-b82d-bbd1c9a77d24 | -16.88589 | -42.07092 | 2025-08-08 00:07:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 46c66212-f163-3070-a6f0-d5caea40daf6 | -14.78596 | -48.00161 | 2025-08-08 00:07:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| f661ab4a-1441-33d6-ad7a-cee2684ebf61 | -11.57486 | -44.85679 | 2025-08-08 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ede5ccfc-6da8-3031-aa06-c5fbe23f6ec8 | -15.68561 | -43.21498 | 2025-08-08 00:07:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 03efd5e0-0a7d-3e4a-9a61-76233c5ce49a | -12.08848 | -44.73827 | 2025-08-08 00:07:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ee7c034b-ac40-3b2f-813c-8f07f14ca582 | -16.21283 | -41.35066 | 2025-08-08 00:07:00 | TERRA_M-M | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 17b17aa0-10ae-3ba9-a7fd-ab614b55377d | -12.09896 | -44.73671 | 2025-08-08 00:07:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| eda27376-19ec-3d03-8fd3-ccadc45dcca2 | -14.47689 | -43.24744 | 2025-08-08 00:07:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c6774e1b-075e-3559-9cb4-719a10e5ae26 | -11.80496 | -44.92579 | 2025-08-08 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| a24367e0-ec64-3f49-882a-e93f58fe049c | -6.63927 | -41.8723 | 2025-08-08 00:09:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d993305b-49a4-3a19-9126-1baf6540efd2 | -7.91427 | -45.55014 | 2025-08-08 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f2da837a-9e37-3886-b1e7-1db0be56f8a7 | -6.97108 | -42.8775 | 2025-08-08 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 5a21ef48-a5cd-306c-bb08-ad2e9fd438ba | -5.97856 | -44.16383 | 2025-08-08 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dbf60420-8cf3-3f13-94dd-ee1ac585f9ba | -6.96212 | -42.87874 | 2025-08-08 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5bf3a262-5ec4-3378-8e23-c5d93c852db7 | -9.64881 | -43.84727 | 2025-08-08 00:09:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 45da6ebb-b1b4-3c36-aa85-c9acba7d77e0 | -7.11442 | -44.21642 | 2025-08-08 00:09:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dfd49dc6-e387-3154-8f97-c86b5ee5e58a | -6.37668 | -43.37823 | 2025-08-08 00:09:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b086885d-217a-3ed6-9f38-89dbf25064a1 | -3.95023 | -41.48657 | 2025-08-08 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 672de16b-9b78-3e1f-8546-9e35b651e3e9 | -7.41787 | -44.67018 | 2025-08-08 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9b46c0f2-2423-3434-b605-6281bba9976e | -5.9772 | -44.15389 | 2025-08-08 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 499.6 |
| 65efe984-6608-3123-9da4-ee2efb5dfe14 | -8.98936 | -45.67992 | 2025-08-08 00:09:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 139aad5e-3bb1-3d45-8466-6bedbe213127 | -7.24274 | -44.66184 | 2025-08-08 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 0a51c186-0c22-3219-9cce-241914f5da46 | -8.86252 | -47.2687 | 2025-08-08 00:09:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 8dd4ccf5-8314-3572-8390-a657a24434ee | -6.96983 | -42.86841 | 2025-08-08 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| f847b12e-fad7-39b3-848d-56ac812199aa | -7.74388 | -47.39621 | 2025-08-08 00:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| af7a7a6c-6c28-3fbb-abad-961c2427ea13 | -7.38414 | -44.64123 | 2025-08-08 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ff465be9-c1e1-3292-84b2-3ac9a80b3189 | -6.5504 | -43.91122 | 2025-08-08 00:09:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bf61ad5f-18a4-384a-b68b-5f2f9e2a5b96 | -8.8648 | -47.28646 | 2025-08-08 00:09:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 850d565c-5201-3d08-be16-328972e69c73 | -7.91997 | -45.54365 | 2025-08-08 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3015a16b-f1ea-374e-87ed-b202b4ef765b | -9.07114 | -45.05621 | 2025-08-08 00:09:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5db3776c-021e-3efe-8d69-6e359d2156a9 | -8.86647 | -47.26266 | 2025-08-08 00:09:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b595db15-4a70-3eda-acdc-c0d4204cd765 | -7.23154 | -44.65246 | 2025-08-08 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8676ff25-5b8f-359f-891f-f5ef969febd5 | -8.06286 | -49.70521 | 2025-08-08 00:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d24d211c-f771-3819-baa3-00574e71ca9c | -6.79993 | -43.2417 | 2025-08-08 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| adfd9c49-403e-319e-ae2e-731e0bf5be2c | -6.69188 | -43.32549 | 2025-08-08 00:09:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 13.9 |
| d3a43be7-1a6d-3ccc-8d79-810b11a9e895 | -5.36651 | -37.32689 | 2025-08-08 00:09:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 091c93d8-f8d5-3e5b-8c2c-e9bf9382ca6e | -8.52221 | -43.31661 | 2025-08-08 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 702dc5a7-59c1-3c50-975d-5058429154a5 | -7.37439 | -44.64256 | 2025-08-08 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dc5ac042-0c88-3e4b-8cd3-964438e0d511 | -7.37584 | -44.65354 | 2025-08-08 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| db12d947-b996-32c0-ad76-beed92dc9741 | -6.96088 | -42.86966 | 2025-08-08 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| f5b177e7-07e0-3c20-8f87-b7b5d0243896 | -3.26367 | -42.64433 | 2025-08-08 00:09:00 | TERRA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 22dae5bb-19a6-3630-a274-e30d1119ca13 | -8.24741 | -45.07356 | 2025-08-08 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c3bf3226-893b-3572-b8b5-59c804e881b0 | -8.06625 | -49.73236 | 2025-08-08 00:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| fe3900a1-f043-3b9a-b048-67035a83718e | -6.26182 | -45.26002 | 2025-08-08 00:09:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 205fa29a-a5cc-301e-ae23-a3792bcc4016 | -8.20562 | -45.06071 | 2025-08-08 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c075dac3-1f1c-3372-8967-5bf09bc91c8a | -7.89423 | -45.34244 | 2025-08-08 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9fa05f5b-4446-3aee-9c4c-e9c883b527c1 | -10.75673 | -44.44731 | 2025-08-08 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0f3e562f-80c4-387c-a9e9-7a843a4a829a | -10.62558 | -44.77244 | 2025-08-08 00:09:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| a108941c-9922-30a0-8099-082dbb97e83f | -10.43028 | -44.36614 | 2025-08-08 00:09:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1d31f48b-33ad-33c4-a3c8-a3b5bec75e1a | -3.66471 | -41.7477 | 2025-08-08 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f77092f5-5a06-3915-8469-d5c2d261a6cd | -9.06242 | -45.06975 | 2025-08-08 00:09:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |


[Clique aqui para ver as próximas entradas](README2.md)
