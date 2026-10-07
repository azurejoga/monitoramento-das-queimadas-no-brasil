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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4274bdd-9d8b-35f2-b5be-2d6bad721468 | -11.38699 | -46.70306 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fa9bc8f4-c571-3cb1-8315-231091226705 | -9.95043 | -43.54704 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 1b1e1870-9c6c-3ba3-a1c8-b638465abead | -11.23275 | -44.86638 | 2026-10-07 16:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| fba8f490-3c2f-35da-b9b3-0ff5d6e88a50 | -7.67104 | -39.83935 | 2026-10-07 16:01:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| da7b6632-418d-3f94-be9e-b625a5b224da | -10.97568 | -45.40384 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0b0ec8c0-9a7e-32b2-bfa3-f9a1e083faae | -7.79258 | -39.54781 | 2026-10-07 16:01:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 27.5 |
| a4d66bd6-44f0-3626-9598-dbf8322b1f79 | -9.92313 | -44.81513 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| abfbf1f8-fc40-3ada-bd3e-010f3cc54f4b | -8.82328 | -47.55323 | 2026-10-07 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 85766722-33ba-3fa0-afab-9861a32edcf3 | -12.21837 | -44.71428 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 81bc858c-4dd7-391d-af85-3cebb2bdfb5e | -11.73704 | -43.42342 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 77213c16-0bc9-3983-9549-b65e42a586a4 | -11.39425 | -50.88842 | 2026-10-07 16:01:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3d72f8c9-4b80-380c-9325-3e0a709a86da | -11.64229 | -43.67983 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 82a1a514-067c-3763-9d17-6bdaca90c755 | -12.99399 | -47.06316 | 2026-10-07 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 2cb311b7-4ffd-3366-a9bf-2e98affda185 | -11.87492 | -44.77859 | 2026-10-07 16:01:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5a1b3c66-ad64-31e2-8c02-da623881ad90 | -10.87903 | -46.67712 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| ebf959fe-9a6e-372a-a041-5b31a49cd7ca | -10.45979 | -46.83213 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| c8f67368-df06-3711-8db6-ecbe83f38006 | -11.64296 | -43.6848 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 8dad367e-c072-36c6-9fc9-e0a2fa30fc8b | -13.65172 | -44.78801 | 2026-10-07 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 26dfb99e-8f3a-36c2-94f2-3111b24c5d43 | -10.99706 | -45.48985 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 72b68df6-247e-3ea5-bbfb-213e19f33396 | -11.00498 | -45.43195 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 954fe99c-2f76-3508-a061-f23f57c2b105 | -12.29375 | -45.29749 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c44d6fe-99c3-32b2-8201-4cb9d87a9b48 | -8.96104 | -45.10688 | 2026-10-07 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ad79ef99-bf54-3f14-a264-4b54c60d578e | -10.99939 | -45.46802 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9da04063-5afc-377c-8957-267979ff2fc9 | -12.36648 | -38.00425 | 2026-10-07 16:01:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8ae38a90-8cfd-32aa-a94f-b5ffd4c54472 | -12.32298 | -47.94523 | 2026-10-07 16:01:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4c53fa0c-7da7-3f2c-b3e2-9b42ebc08405 | -12.56752 | -45.0875 | 2026-10-07 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ba9bdbcc-e28e-3e61-a0ef-7cc4e48cb155 | -10.04074 | -36.05331 | 2026-10-07 16:01:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c29e23ce-c808-3949-aef8-c2132de605f4 | -9.97521 | -43.56546 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 62d39d51-615b-31ab-a503-ab37ae67e5af | -12.21518 | -44.70784 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8f2b2344-3acd-3de9-944e-b542fe60ddf6 | -11.22822 | -46.24962 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2d01533c-351f-3df4-bb91-659dfe0cc887 | -11.83804 | -47.37594 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1832e917-cce5-3593-8b59-d81bc460d873 | -8.77206 | -45.76881 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 374f0344-ac6c-3609-8bfe-af16faa77027 | -10.99122 | -45.48454 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4235a35-31fb-385a-934d-b167add06951 | -12.21734 | -44.68493 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 263584a1-43c1-37ee-9047-7772dbb3c676 | -9.96597 | -43.49751 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1c95fdbc-461d-3194-b077-d3f37b7014cc | -11.46933 | -43.3964 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 7bf1a645-7e6c-32b5-9dec-5badb9a41692 | -11.43542 | -45.56781 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 7652a35f-1c59-3dcf-ab19-d950662226b6 | -10.07628 | -45.985 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| cb3c038a-2c68-35b6-be0b-51b0daf14ae8 | -11.85635 | -47.33184 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d6e03fcd-beb2-38e5-91c7-138e9df9151f | -12.22772 | -44.72889 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| da39d6d1-73a9-3f10-b95b-0f0bad94d3ce | -10.64546 | -46.70255 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 220fc154-bf8e-39ca-897e-70b57247daea | -10.12548 | -46.84959 | 2026-10-07 16:01:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 12e9147a-6df9-31da-8735-0fe9f063516f | -9.40678 | -45.89849 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc113a0b-493d-35e0-8ee9-63e9326b8f16 | -13.56996 | -47.24345 | 2026-10-07 16:01:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| cb01c37e-9044-3bda-a358-86c56fc03bd3 | -12.04072 | -43.43996 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 93240857-2358-3421-9c4e-1d90f39a7794 | -11.75268 | -38.44626 | 2026-10-07 16:01:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 56d9831e-ca38-3610-8a0b-4d0656e6aa36 | -10.47857 | -39.4288 | 2026-10-07 16:01:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 0425be5c-5a3b-3e4e-bd2c-71655ca6447c | -12.20908 | -44.65801 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 4c16edd5-e022-3f8c-b3af-4739c971db22 | -8.94082 | -47.38761 | 2026-10-07 16:01:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2afd525e-de2c-3d16-813a-b7400793f368 | -11.00056 | -45.47704 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1010f2a3-365a-3418-b392-9ea9cc3c96c0 | -11.20457 | -46.27776 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a68a1ef6-d791-3e15-a71f-fe0121296c37 | -11.08585 | -45.6738 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6bc43da5-559c-3e61-a0ed-f3b4ab402c15 | -9.93381 | -46.80044 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4593ef3a-a687-38f3-9c43-b69ae23300b8 | -11.38411 | -46.67808 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d9feb6e1-627a-3185-ae77-ca6351060062 | -11.05639 | -45.82794 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9508c6cb-661c-348a-a9d5-6feb757e02ee | -7.54386 | -35.26934 | 2026-10-07 16:01:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| d71235a8-0812-39df-a3a0-b6f16e556b1e | -13.93593 | -46.48848 | 2026-10-07 16:01:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3b24bb32-c9d0-365a-ac86-436bd4febff6 | -7.09062 | -36.08875 | 2026-10-07 16:01:00 | NOAA-21 | POCINHOS | PARAÍBA | Brasil | 2512002 | 25 | 33 | nan | nan | nan | Caatinga | 9.0 |
| a1a561a7-51d7-3729-ac1e-a9e6ae6ae631 | -9.03342 | -46.88739 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e96a65aa-e075-39f3-a287-dc830d25706d | -7.91406 | -35.20728 | 2026-10-07 16:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| ca908f58-073f-3fd9-847a-ea74b6a06e74 | -8.25177 | -37.03467 | 2026-10-07 16:01:00 | NOAA-21 | SÃO SEBASTIÃO DO UMBUZEIRO | PARAÍBA | Brasil | 2515203 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0ada7b70-d901-3b26-b579-802b2999331a | -11.38018 | -46.69144 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b79221f6-7708-307a-a2dd-f3239f2337cc | -11.85176 | -49.09538 | 2026-10-07 16:01:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 31672d22-4366-3a22-90dd-1c44196b9984 | -12.13937 | -43.31211 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| c6e7ddca-08e2-3e79-a119-ad8fb8fbce96 | -11.85494 | -43.55795 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| e9ff2d31-cc41-3a13-b407-5ae0fb8323bb | -10.87855 | -47.60021 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 109fd02f-c9b1-3a1b-b335-b90a9b89b1db | -9.95481 | -43.54648 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 76615414-95a5-3186-b27b-9c3d217ac374 | -13.33288 | -38.98845 | 2026-10-07 16:01:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ed685b99-8c04-3f98-9b07-2973976520f2 | -12.20067 | -44.65452 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 8d0351c3-2ea9-3dbc-a0cd-c7cbb0dfc5fd | -11.43581 | -45.57091 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 12f2c505-36df-36a5-9a36-fc3c85e6cf91 | -9.86025 | -46.30201 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 199ce898-456b-3e01-8626-81ba8a4813df | -11.22484 | -46.23785 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 919d39c8-f878-39ff-a1e9-d248a3be5dc3 | -9.53013 | -46.85431 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6d73823c-3a3c-3bbf-98a4-08aa218bae2e | -9.0348 | -46.89788 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7abf7610-dc06-3dd4-83fa-4ec534973829 | -14.18891 | -46.2149 | 2026-10-07 16:01:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d541296-f1a7-3d41-be18-0beb05e8f10b | -13.17576 | -47.88097 | 2026-10-07 16:01:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dafdd38c-fb61-3ad0-9147-88f80bee82c8 | -10.41647 | -47.54176 | 2026-10-07 16:01:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| aed23d0b-25d3-3446-a030-a41ea51be56c | -8.76746 | -45.77253 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b039a274-4031-377f-8a42-b04c5bfcf542 | -11.61829 | -43.63772 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 47694cb3-80c3-34e1-bc21-c3a191435ee1 | -10.45305 | -36.4743 | 2026-10-07 16:01:00 | NOAA-21 | BREJO GRANDE | SERGIPE | Brasil | 2800704 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| f02f3832-9ca6-3eb7-82d2-b3cdf211ade4 | -10.88363 | -46.6692 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 7679db55-d42d-3c9f-bece-37c7feacb31c | -12.36311 | -38.00476 | 2026-10-07 16:01:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 7b651d72-f7fb-3b10-8444-b78b45c227c9 | -9.86248 | -46.06896 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e7ab177d-23a3-30fa-a004-740ee6533e16 | -9.97233 | -37.33006 | 2026-10-07 16:01:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2648599e-a444-33b1-9a6e-ccea1ff6d153 | -11.06592 | -45.80971 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0b02540d-b3e8-3fa4-8852-9e575e57ec41 | -12.22007 | -44.70717 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 7d96d8a9-4255-3224-a684-686a1ecd3489 | -11.84025 | -43.53359 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d48f7df6-db19-3c58-83b3-267ce4ae17ba | -11.08895 | -45.65691 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 9cd6d140-a8c0-3db7-9165-8b57d50ae4cc | -9.98984 | -46.02097 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2a9ccc9c-97c4-3eed-9ac5-55e4a2d7115e | -8.80172 | -47.22124 | 2026-10-07 16:01:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c22b759c-7322-308b-886c-a999f228f518 | -11.84337 | -47.37117 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 846f02af-aeac-305a-a925-d87735657363 | -11.00579 | -45.43809 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f3db3f5b-8488-3122-8ee7-edae8da98e47 | -7.54756 | -35.40509 | 2026-10-07 16:01:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 95b7fed2-1d1c-3aa3-987d-615f32f4c7da | -11.85288 | -47.30294 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 69983c54-02ec-3135-9244-0d5dd7f87b44 | -11.15514 | -46.18678 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0889708a-6b5e-3ca3-8ef4-e28bfb37eeb5 | -9.97025 | -43.56177 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 6d83e4de-4af8-3d0a-8b87-df163f7c4b84 | -10.49 | -47.26522 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e3db99df-a7af-3f4c-b647-5c96299ae024 | -8.95221 | -45.11394 | 2026-10-07 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 505934f1-25ba-3a8e-a1c8-383cc461171c | -8.76707 | -45.76967 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 894ff21a-2390-3826-9a8b-bd50c1a108bd | -9.92197 | -46.79453 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README151.md)
