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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45fba173-54f7-3c7a-a649-12c9ff162084 | -10.3708 | -61.232 | 2024-10-12 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2dd196f7-93a6-3f67-af84-7e75fddf2379 | -10.3892 | -61.2695 | 2024-10-12 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 53398dcf-6e84-3c7e-b1c9-89f280345738 | -10.3895 | -61.231 | 2024-10-12 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| f4391330-0a70-36d9-ab1b-4eb180cdaabb | -10.3897 | -61.2118 | 2024-10-12 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 99c04530-fcd1-3608-8b95-841f1ced2e89 | -10.4079 | -61.2685 | 2024-10-12 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 7eb4ae16-9d72-35df-8f35-a7ec562fb4c4 | -10.5325 | -51.0636 | 2024-10-12 01:36:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 227e6646-4420-36d8-bf42-2b73c89e7a66 | -10.5328 | -51.0425 | 2024-10-12 01:36:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| dff55c3f-27b3-324d-a938-ce05e4911f27 | -10.9506 | -44.653 | 2024-10-12 01:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 66ed7a6f-01d3-37be-b5a7-6fb7df20c836 | -10.951 | -44.6298 | 2024-10-12 01:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4b76e4db-5420-31c7-830a-4d71d5962311 | -11.2761 | -60.5038 | 2024-10-12 01:36:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 16ffe27f-ea53-3815-8e5e-483f43888aba | -11.8377 | -58.8445 | 2024-10-12 01:36:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| acf8706b-423d-3386-86b3-a7acb2be6b24 | -12.7866 | -44.8873 | 2024-10-12 01:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| da9e5fd2-8ff8-380b-802b-222e5e293edd | -12.7871 | -44.8639 | 2024-10-12 01:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 306.8 |
| 436ecf77-2e97-37c6-90c2-a7bcacf2ca29 | -12.7875 | -44.8406 | 2024-10-12 01:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 201984a9-395a-310b-bb1d-ffa3e8ba59c8 | -12.806 | -44.8841 | 2024-10-12 01:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| aa65a0c2-f455-3134-b97e-11f6c513da62 | -12.8064 | -44.8608 | 2024-10-12 01:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 2feef84c-3e79-3b60-b0de-4284fdc22e36 | -12.9464 | -53.5339 | 2024-10-12 01:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| bfbaf6b4-2928-3658-874e-e4dcfadabceb | -12.9655 | -53.5319 | 2024-10-12 01:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 41ae7cb5-4bd0-30b5-ae6c-391e98b7095d | -17.0426 | -56.0333 | 2024-10-12 01:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 418932d2-0800-3250-a224-0b58f3b6c763 | -16.9805 | -57.4404 | 2024-10-12 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 6645838d-3f91-345c-a0be-78bb576db436 | -16.9998 | -57.4586 | 2024-10-12 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 760faa2f-d267-337f-97ad-82e068f64044 | -17.1761 | -57.4585 | 2024-10-12 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| ecfa252e-578c-3c9a-960b-cf22a4ae6174 | -17.627 | -56.3318 | 2024-10-12 01:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.3 |
| 83802ae9-dd22-3252-9415-a43f63e40acf | -17.6273 | -56.311 | 2024-10-12 01:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.1 |
| de6452b2-83cd-30e1-87b8-aaf4f8ef1bd6 | -17.6467 | -56.3292 | 2024-10-12 01:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 176.9 |
| ad84a6fb-f60f-3ca3-998a-ea27455bba36 | -17.6471 | -56.3084 | 2024-10-12 01:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| b2747642-0bf1-3a49-89e0-7c4593d3f64e | -17.964 | -57.3843 | 2024-10-12 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.8 |
| dc453724-2e42-3a6b-b98b-174ba3d4c803 | -17.9643 | -57.3637 | 2024-10-12 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 9b8727be-5c04-342d-b7b1-4a42fcd2215b | -17.9837 | -57.3819 | 2024-10-12 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| a7447f31-1302-3ea6-aeb7-0f4e581a455c | -17.9841 | -57.3612 | 2024-10-12 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| b76264c0-c8c6-3304-8d0a-c5c3d1e31b5e | -18.196 | -56.5275 | 2024-10-12 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 228.9 |
| 88a6e67c-53a9-3581-8dfa-e341ff6ac4f5 | -18.1964 | -56.5066 | 2024-10-12 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.2 |
| 90ead444-26d3-3ba0-9759-e5f5a1c061ec | -18.2158 | -56.5249 | 2024-10-12 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 54cc78a0-234a-339e-948c-ad2aded2afe9 | -18.2162 | -56.504 | 2024-10-12 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.9 |
| efd2ed91-a26a-3402-9bcc-d0b69b659509 | -18.1762 | -56.5301 | 2024-10-12 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.4 |
| b9d2a6d2-d2ef-3adc-be32-ed36bb165f72 | -18.1956 | -56.5483 | 2024-10-12 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.7 |
| bba2c12b-26c2-338f-ac4f-fedd572d9060 | -3.46324 | -51.54863 | 2024-10-12 01:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 2f4da752-0785-3af2-a989-e3c79317ee82 | -3.28193 | -50.94407 | 2024-10-12 01:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0eb5ceb1-9105-35c7-8a1f-233a061dfcb3 | -3.03692 | -51.13309 | 2024-10-12 01:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a8cbf8b5-03ae-3c16-9f14-65f06bdcb86b | -3.03649 | -51.13886 | 2024-10-12 01:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 0f0b32b7-53ff-3e14-bb4c-6c0a694247a8 | -3.02984 | -50.58427 | 2024-10-12 01:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 1fe7eb0a-65cc-3283-956d-8d432fbb4da8 | -2.8748 | -51.67467 | 2024-10-12 01:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 3c05d42d-e7e7-3685-83e4-84ed2210ba21 | -2.87049 | -51.68184 | 2024-10-12 01:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| c6613f0e-e550-3277-9513-794246fd9d71 | -2.86693 | -51.65717 | 2024-10-12 01:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6deef884-5052-38c2-bfa0-30d1055c837b | -2.8607 | -51.67675 | 2024-10-12 01:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 75c010f3-d3f5-36d6-97c8-7afca1d7e979 | -2.82484 | -51.34568 | 2024-10-12 01:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 57c3c12c-6805-349d-a8be-b31df71db500 | -2.82293 | -51.3525 | 2024-10-12 01:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| aa26b3ee-f5f7-37bb-ae04-0c19dabed41d | -2.78334 | -51.38504 | 2024-10-12 01:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 91034592-c357-388a-9a95-68883b4ddfb3 | -2.77949 | -51.35908 | 2024-10-12 01:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| a8aee3f1-8b37-31d1-ad14-12c96248c327 | -4.02422 | -50.99817 | 2024-10-12 01:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 31a2bb36-f292-3cbc-99ce-1f7e1d800da4 | -4.02307 | -51.00523 | 2024-10-12 01:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 78fd97d3-2cc5-34f3-8e0c-a2aab9781370 | -3.78166 | -51.32341 | 2024-10-12 01:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7c9ad243-6d00-370e-989c-c1f69cd4176e | -3.48102 | -52.82642 | 2024-10-12 01:37:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| b57d4695-a3c7-393f-9821-8ea85d106608 | -3.48101 | -52.82082 | 2024-10-12 01:37:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e6cc98a1-e780-3816-a417-22cecef3b4b7 | -2.98231 | -52.91119 | 2024-10-12 01:37:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 0cc1e892-6440-3750-9638-ced55d5fe5c9 | -2.9696 | -52.91319 | 2024-10-12 01:37:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f73c3a6f-2eb3-3c70-85de-85189dc0cb35 | -2.66697 | -53.34723 | 2024-10-12 01:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 29281959-a7bd-364b-b331-7033d451c0bb | -2.6643 | -53.35335 | 2024-10-12 01:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| db648470-54ff-3033-8dcd-b181924ebdc6 | -2.65463 | -53.34905 | 2024-10-12 01:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 1888f569-9b9d-3cfa-a705-7534ee67cf44 | -3.2529 | -54.19585 | 2024-10-12 01:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| b4c8f51c-ebaf-331d-85f5-72f2be5387d7 | -3.25061 | -54.18041 | 2024-10-12 01:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 533fe955-57ea-3800-80a1-817e00f6980a | -2.79119 | -54.02423 | 2024-10-12 01:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 9ae0a585-273f-3602-9c87-019913e4fe24 | -2.78885 | -54.0082 | 2024-10-12 01:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 09eaddb6-7bd2-3501-a87a-1976b8c54de9 | -2.77953 | -54.0259 | 2024-10-12 01:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 824c3298-5ba2-3597-a023-708bb323efb5 | -4.47056 | -55.07662 | 2024-10-12 01:37:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b7adf0c0-02b5-34d2-863b-eeed5356ccf2 | -4.45181 | -54.90349 | 2024-10-12 01:37:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 199cad57-0e87-3a87-87a0-1b1da661104d | -4.44701 | -54.91063 | 2024-10-12 01:37:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a0daf586-1f75-33f3-8333-9b4f8435c774 | -4.42402 | -54.90076 | 2024-10-12 01:37:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c81cc758-f652-30f4-bc01-b5bab240c44b | -3.95735 | -55.35207 | 2024-10-12 01:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 770961e1-008b-3d70-ad71-43c61af42be1 | -3.95395 | -55.34618 | 2024-10-12 01:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ea55be51-b268-36e4-916e-b3334a89950d | -7.86228 | -54.69563 | 2024-10-12 01:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 1e64aaa9-375f-33bd-bce2-ff9391c5868e | -9.57513 | -55.81048 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 38a124d3-939f-3aee-8502-835064712911 | -9.57368 | -55.80059 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| f65355fc-49e6-3fab-b995-50ec7c53608b | -3.60215 | -55.46014 | 2024-10-12 01:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ea24225e-4427-301b-a513-24dc8622dd0d | -3.5882 | -55.5673 | 2024-10-12 01:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 67aaf5db-fbc9-33e3-8148-076dd985ec9e | -4.89683 | -55.90923 | 2024-10-12 01:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 71fde49c-c47a-3866-a9d6-921e5d51c313 | -4.89523 | -55.89817 | 2024-10-12 01:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1312e003-0e21-3b04-b7b1-2c8f0e65e4f0 | -4.85439 | -56.1843 | 2024-10-12 01:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f0d40cd1-311b-324f-bc97-f226c3cda562 | -4.81135 | -56.15873 | 2024-10-12 01:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| b7c0bc0d-6799-3476-b547-64e3b8c85bb8 | -4.80979 | -56.14807 | 2024-10-12 01:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4ca2a82b-128e-3dc0-a127-b1b7e8fe3d62 | -4.80866 | -56.16558 | 2024-10-12 01:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 19e6dd85-e438-3be5-b1d1-ad5097588c4d | -4.80716 | -56.1549 | 2024-10-12 01:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 9f3f0848-69a5-30bb-858a-30ca78bb89fb | -4.64626 | -56.01929 | 2024-10-12 01:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fda07185-cfd9-3270-a906-9d8b2a143734 | -3.9988 | -56.27789 | 2024-10-12 01:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 757f6b03-2b2f-3816-bf80-cd32a6cd41ca | -5.1201 | -56.24537 | 2024-10-12 01:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7f367c78-7aa4-3399-b8fd-c52ff985e358 | -5.09334 | -56.19586 | 2024-10-12 01:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bf838431-ae5a-3ce5-8f65-ce2d5381073f | -9.94755 | -58.10939 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 25fc415c-4311-36cb-a36a-1485f7b8228b | -9.94631 | -58.10045 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9baac885-6b88-3b17-bdd4-cdf11f6fd1bd | -9.9387 | -58.11067 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2714c3fc-d162-3dd2-90a7-1dbad2e83103 | -9.88073 | -57.50008 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 96a4155a-fbef-3e33-a0d4-f9d01414b387 | -9.8437 | -57.7512 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f089044a-bc19-3305-9d86-c517dc947d7e | -9.6776 | -57.22544 | 2024-10-12 01:37:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5806287a-5bc2-3bae-b843-80f37190b4fe | -9.67633 | -57.21645 | 2024-10-12 01:37:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 64514246-a159-3991-889b-2531aa1256e2 | -9.47171 | -57.93578 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ff3ed648-9049-3495-861b-ecf83c28159d | -10.54538 | -57.7706 | 2024-10-12 01:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3caa91be-39eb-33e2-ae50-5cef2fcb9282 | -10.53793 | -57.717 | 2024-10-12 01:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b68802f0-1c8e-3ea5-a4c4-b96bc9315d46 | -10.51128 | -57.78468 | 2024-10-12 01:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 21214eab-b36b-387d-b56c-71d4f4e82d3a | -10.42492 | -57.23167 | 2024-10-12 01:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 900c72a0-6c0b-339e-8ddb-662d1720d039 | -10.29092 | -57.71956 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b0395710-0a31-3a41-bf81-211cc2c8dc86 | -10.28968 | -57.71064 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README24.md)
