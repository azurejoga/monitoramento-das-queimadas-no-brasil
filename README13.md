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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 282a5186-ab2e-3d60-b46b-b42ac9aa44c7 | -8.07429 | -44.5233 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41731328-f796-3cc9-bc9d-4e5b5e99d446 | -7.67326 | -44.48561 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 100b04b3-41c8-3936-978c-3998aa10ca07 | -10.78603 | -41.70226 | 2025-09-15 03:30:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a64fa830-379e-363c-8d5c-c0e194049b52 | -7.8949 | -43.56084 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| de8ac05f-d88c-37c7-98ea-6ec644631f60 | -11.77456 | -46.66499 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10120e16-0ebe-3426-b6e7-49d785dbf4ec | -7.86631 | -43.57941 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 20ead203-19d7-3ed4-88e4-40a512225899 | -11.33269 | -43.4971 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26080bc1-29a1-3bfa-a699-63422aa22aa5 | -12.55412 | -45.64623 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9b443f85-cfff-3f28-ac02-28a5c78440ea | -7.86291 | -43.56429 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1143d40e-3ba9-39f2-96a0-a706c13dcc36 | -8.96521 | -46.22352 | 2025-09-15 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0c1f4ae-3b47-36d5-94aa-de4aa480d385 | -7.88187 | -43.59672 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7f4f2b0-4324-3a67-bb60-0ead9b1ec6e4 | -7.86025 | -43.57828 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f68f6296-a9fc-38ce-bc1c-e5b3eb0d272a | -7.99662 | -44.82644 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6b5618c-0c7f-3e60-b94f-c9ff769b0a42 | -10.16494 | -45.32617 | 2025-09-15 03:30:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c622e546-469a-3361-97b1-fe76e1fc0996 | -10.93787 | -45.5227 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17ae7a8f-90f1-3e4f-9592-3924c3ce0633 | -9.18774 | -45.24738 | 2025-09-15 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 403ebb40-aa94-3f58-b993-f0f9f295c880 | -10.65501 | -46.23985 | 2025-09-15 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb36bb80-544a-3cc6-89f2-961b9fa89e12 | -7.85507 | -43.57249 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b454d01f-031e-36e4-89a0-ea0acdd4adf0 | -7.87645 | -43.58894 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3767fcc2-8817-3de6-a6bb-8bb90f36415d | -10.93533 | -45.50367 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 68782496-7812-38b8-b701-68a3cfcba198 | -8.78591 | -46.0542 | 2025-09-15 03:30:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 176bfd19-ed06-398d-8e44-30d1779d895a | -12.00129 | -46.67443 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6775b9c9-7599-3218-8377-73c0e9605153 | -10.91696 | -45.56243 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bf83d52-1a25-3922-ae6d-3d32f10dd80b | -7.8759 | -43.56191 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5b26e117-9cb4-3bab-b754-361e899b0955 | -7.6969 | -44.67652 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 44d1a3f7-d59a-3002-a500-73f0e822744d | -12.6049 | -45.72821 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d7d8268a-224c-3132-92f2-e4b689fae8ff | -10.90961 | -45.56181 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07ba7e44-b970-3fdb-ab1f-47c550d57813 | -7.88366 | -43.554 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 443d9fa4-a66e-3752-b1f3-0dc6cd7863a6 | -10.93108 | -45.4912 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 602bc8c9-27c6-3f92-b098-385d90d7009f | -7.85475 | -43.57038 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4cb2a95-aded-3d2f-9389-24a031af331c | -8.64594 | -46.36117 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 99b4c877-ae4c-3363-8872-e25778e993b3 | -8.8207 | -40.6682 | 2025-09-15 03:30:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ed834dce-4afc-3aab-91f2-8a07ac233ff3 | -8.12061 | -43.67089 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5b5424a-0ac1-3702-b7c4-8941a3ae6fea | -11.7614 | -46.66283 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c488184d-5d15-3481-88b2-5b479401b2ea | -7.85846 | -43.58767 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 6297d208-0942-34e8-a46f-f7a085c7f1ba | -7.86431 | -43.58672 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 632387e0-1305-3da8-8c6b-2eb3f998770b | -8.9823 | -45.81568 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| f6d401a5-5cdc-3f90-9ec0-9cc60143618c | -11.12901 | -45.30892 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9807fbe3-ccc1-3a27-9b5f-440998a3f3e9 | -11.47093 | -43.58479 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33c4865a-839d-3283-a0c6-daca6eca42f3 | -8.61235 | -45.74175 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a2f59b79-40fa-39bb-a26d-95ed69ab22a5 | -7.85304 | -43.57975 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76fed05d-c108-3d90-b6f6-b5958541ad7d | -7.84526 | -43.85812 | 2025-09-15 03:30:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2adce6e-54c0-37ad-aacc-f5537fdc9d74 | -10.90848 | -45.56728 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a69820e3-bcfa-32ef-83fb-f31afe679760 | -7.68901 | -44.68262 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bea096ba-2ad6-3fef-a395-ab4ea80defb3 | -10.94069 | -45.51062 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36dd6889-a885-3166-bde4-90c69e43dd6e | -8.59675 | -46.36708 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb842c09-1e64-3901-8661-bce60a3a3e47 | -7.87844 | -43.58164 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 874.2 |
| d28281f0-ab02-348a-8b3d-8c11b32444fc | -8.08363 | -44.50891 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91457aa5-3954-3f8f-a262-deda003f0977 | -8.64047 | -46.36814 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| dada4960-6a85-30f2-8754-590d28bb7a95 | -12.78715 | -47.93525 | 2025-09-15 03:30:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0f29bf51-297d-38fd-8314-6e0db5d0c47e | -7.88538 | -43.57812 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 243.3 |
| cccca474-f170-3ab2-8c1c-901afe3f7bbc | -12.16666 | -44.10129 | 2025-09-15 03:30:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 950c0e2b-eef9-3819-b743-27f930a1f286 | -11.76406 | -46.65032 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 983e7f5c-3ebb-316d-a6be-c9c3a72ef0c2 | -12.6148 | -44.20321 | 2025-09-15 03:30:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 845a642e-0c48-3065-8fff-f743f9722736 | -12.79478 | -47.94321 | 2025-09-15 03:30:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6db7f335-aea4-3dfe-9d73-33734759d926 | -11.47994 | -43.59939 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 280e0cef-c8f4-3ae5-bbe1-c1abba54d953 | -9.3534 | -45.39069 | 2025-09-15 03:30:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2859522e-69a9-3e0e-be92-72902c7bd865 | -11.77324 | -46.67144 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f4f45de-b4d5-35e6-aea5-e1f2eee1b93a | -10.7306 | -44.77139 | 2025-09-15 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d67bb25b-7539-30e8-9dc7-6e2369f24fcf | -12.79426 | -47.93711 | 2025-09-15 03:30:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e5aec3d2-dc4f-379d-a470-f8ffe0e64bda | -7.88363 | -43.58741 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| c4565c1d-077d-3d4c-9778-53b347152e56 | -12.56041 | -45.64776 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 116e9d6e-3fde-339c-b83b-10a85e34635e | -8.61906 | -45.74358 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8d743e48-1aac-393c-862f-01963d7e2dda | -7.89317 | -43.57008 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 520.8 |
| d42a996f-fdd0-3e0c-a13a-538a514c0138 | -8.96816 | -46.2157 | 2025-09-15 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8742746-996b-3de6-95e5-e1009de9e4e8 | -11.47838 | -43.60737 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4eddc501-8290-379d-8889-091343ac5df3 | -12.79628 | -47.9364 | 2025-09-15 03:30:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c7f29e7b-9ee0-3437-9bd5-e640971454f4 | -8.91554 | -45.47054 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60261b74-b23f-31b0-86ea-401f4c11ce6a | -7.85824 | -43.58559 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5cb16f3c-b8c1-3703-9532-261f1dcf9049 | -8.89989 | -46.1666 | 2025-09-15 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f656804d-a1df-3c96-8d0a-1888330e0966 | -7.879 | -43.57495 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 629.7 |
| 3b828a7a-4ea1-3fc3-87ec-7fef201bdfaf | -8.59811 | -46.36007 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d1bf590-8f37-3f58-8b9b-e00a15d60c52 | -7.86974 | -43.59445 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dae52a6d-0ef3-37d8-8006-8c657a6b104b | -10.66186 | -46.24082 | 2025-09-15 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b14b41a2-d05b-3574-9f69-09400b76f7e9 | -8.81992 | -40.66692 | 2025-09-15 03:30:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6b5fde47-4f12-32b5-9af3-d7332823ead0 | -10.92589 | -45.5813 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d809cd5-e668-3ba9-ae92-118d8c97742f | -11.33758 | -43.5022 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45387b96-a50a-3236-af59-35b346bec6ba | -10.93598 | -45.49905 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 87bc1cb4-3567-3a0d-9411-be9c9bf2c822 | -8.91341 | -45.50056 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 90377474-c995-34de-b8fd-95469d3cf23c | -11.47016 | -43.58872 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a3f36b1-d17a-3f18-b2ea-ff2b43017428 | -10.9161 | -45.56311 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6da859f-a903-3be0-9972-e5b88a5765fe | -11.43996 | -46.9337 | 2025-09-15 03:30:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8d043355-27a5-3deb-9958-0bf4be320f9d | -12.44077 | -44.74329 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 046e82b0-c30c-363e-865c-1994f507dfc6 | -11.33836 | -43.49827 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 401245e7-bd7b-3ae1-a35d-92e7272a74bf | -10.92782 | -45.57578 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 296ce243-c4d6-3f31-a45e-46ab15f49885 | -20.22883 | -46.18298 | 2025-09-15 03:32:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 793e498d-88f2-3579-b6bb-c25306b82ad4 | -19.62331 | -43.73181 | 2025-09-15 03:32:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dbecd23-3da6-36ba-9599-e09a9c5fde7e | -14.94434 | -46.55122 | 2025-09-15 03:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3fa1c497-fe4a-3fd9-894e-2d8a02e8fa83 | -14.50298 | -47.35309 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6447a220-6fc3-3e87-8c24-a78b1cb0972c | -14.50996 | -47.35355 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4caf77dd-2089-321b-9725-bf72239e68d3 | -14.94161 | -46.56377 | 2025-09-15 03:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6c522ccf-4646-3bf8-8388-7651d2dc2c51 | -19.62217 | -43.7372 | 2025-09-15 03:32:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e28526fc-c657-3d30-afb2-30bb1dd4e9da | -19.74418 | -45.12878 | 2025-09-15 03:32:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfb29111-b015-33d2-96ee-06d731421a01 | -15.7454 | -45.09138 | 2025-09-15 03:32:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd0692e0-c9bb-3fa3-927c-bd97c346e4e4 | -17.33488 | -42.65731 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fface62-d256-38b8-ad14-a0ac3e57c18d | -17.76142 | -44.51762 | 2025-09-15 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 707bbb01-ad56-3149-b1a5-0d0ce8702e5a | -20.52136 | -47.47868 | 2025-09-15 03:32:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 609a6096-d3a3-3d7c-8f1b-7d9c38113a54 | -19.71574 | -45.44791 | 2025-09-15 03:32:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a57a5e6f-3fed-3608-b8d6-4e72500194f4 | -20.85719 | -46.21899 | 2025-09-15 03:32:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f92ea407-4cce-37a4-bf7b-24e1ca5f9cbb | -19.71523 | -45.44802 | 2025-09-15 03:32:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
