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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ac30457-5c70-3f98-9cc1-51ace482795a | -10.859 | -47.65548 | 2024-11-19 04:48:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5d90174-a6fe-325a-bcd0-374f9318e99b | -10.41992 | -44.48323 | 2024-11-19 04:48:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03081f8e-71cb-3d0d-878e-5841003992c2 | -10.19382 | -59.55851 | 2024-11-19 04:48:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d9a663d-e348-3c81-b0dd-27a6dac5e0cc | -9.30956 | -46.18805 | 2024-11-19 04:48:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 73c0f4d7-a442-3f46-8315-f8e370ecac8d | -9.3059 | -46.18356 | 2024-11-19 04:48:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ac36f4d-022e-349f-a788-db94c74092af | -10.00826 | -47.55745 | 2024-11-19 04:48:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c82f184a-16a1-35fd-a632-3cbffa9ed878 | -9.29766 | -43.27511 | 2024-11-19 04:48:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9a9bac70-5dbd-3c5d-9c61-3b7abdf5247d | -11.9073 | -44.37158 | 2024-11-19 04:48:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3a458bb-63d0-3b4d-8943-b7aa676c7be2 | -13.17495 | -53.28843 | 2024-11-19 04:48:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca5710d6-6e46-3495-bf30-97647db4db42 | -10.4053 | -44.48482 | 2024-11-19 04:48:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d24ec73b-375c-39df-9da4-2422b0b94e69 | -10.76005 | -44.35202 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09eb53c0-6fc2-3774-bf1b-0d0ca80da097 | -8.81707 | -49.70052 | 2024-11-19 04:48:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 378ce53e-5546-34b3-8126-fd65e7c003d1 | -10.46247 | -45.06367 | 2024-11-19 04:48:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cea4740d-c3df-3480-9f4e-60228f047b50 | -11.24734 | -44.65054 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9446bb6-6d2a-37f4-b62d-7a9a084e0bff | -9.25079 | -44.99805 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5e570aae-4440-3186-8c7e-53c1d06af682 | -10.0076 | -47.55513 | 2024-11-19 04:48:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a4f6612-6a90-3013-a746-e6e859c75ee7 | -10.46122 | -45.07335 | 2024-11-19 04:48:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0244f606-aeaf-3efe-bf84-6924aff7c5c8 | -10.01149 | -47.55571 | 2024-11-19 04:48:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 292a6d37-e752-3f31-a440-7fe4009d3d10 | -10.72596 | -44.49696 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35e54df8-6e50-36c6-9866-54a31844705e | -11.16156 | -43.58363 | 2024-11-19 04:48:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79f8893c-9f1e-3d6f-99b5-3dc8073312cc | -11.88184 | -43.81093 | 2024-11-19 04:48:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7201b571-7ee2-3894-8597-3ac874f235c0 | -9.72383 | -48.1273 | 2024-11-19 04:48:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8cd6b94-fc67-39d4-be2d-12c509f52e6f | -10.36881 | -51.39431 | 2024-11-19 04:48:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e837778-e1d5-3e6e-acb6-1478db5dcf23 | -10.7585 | -44.34815 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e77dfcab-0c14-3c82-91f4-3daa933213cd | -13.25341 | -43.6513 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28a1b69e-5775-3b37-9068-4187edbcb92e | -10.97731 | -44.44473 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82143fef-201a-3259-9b1e-79a6f6525ac8 | -10.46221 | -45.07213 | 2024-11-19 04:48:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2858931a-c44c-3d3e-9f5d-bb7fa6b8072b | -10.70537 | -48.81459 | 2024-11-19 04:48:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5c73d3ea-2e63-332e-b14a-5415b283a907 | -9.84734 | -48.18085 | 2024-11-19 04:48:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f7ad269-6840-3a9e-8d72-7b78f189abea | -9.93453 | -49.59883 | 2024-11-19 04:48:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ccb7c78-d01f-3084-9471-52d1155cb398 | -10.79006 | -51.59459 | 2024-11-19 04:48:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00559729-ae7c-351e-b4a5-b4beb1a61104 | -8.89623 | -48.53349 | 2024-11-19 04:48:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce2f613e-4492-34d4-8e6b-a5005addc04b | -10.96982 | -44.53726 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| db777d23-360b-309f-9a49-2df0a70bfb89 | -8.89527 | -48.5344 | 2024-11-19 04:48:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed8a168e-8e48-37ec-bbdc-94da617d1f2a | -13.16891 | -53.28323 | 2024-11-19 04:48:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 891b5b66-0e13-34ab-b4ba-2d476a440acc | -9.08382 | -40.54383 | 2024-11-19 04:48:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0427182d-5382-3de5-83d0-72a4d7bd0f4c | -9.26382 | -45.00469 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af8408e3-5b07-31bf-855b-73da029705ab | -8.68043 | -47.98442 | 2024-11-19 04:48:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e7afa72-9078-3a38-8c02-973a079cbc5d | -10.75781 | -44.35369 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a44dba89-b09e-35b4-bb22-11d9b9b8dd12 | -10.975 | -44.52783 | 2024-11-19 04:48:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9c134164-6ba8-3527-bf20-6983b1f4588e | -9.26317 | -45.00938 | 2024-11-19 04:48:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5b2a4c00-bdbf-36cb-b294-1b443baa02a5 | -10.8551 | -47.6548 | 2024-11-19 04:48:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c878770-8405-30eb-8ae0-142c451c7d02 | -4.5429 | -48.0151 | 2024-11-19 04:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ae50515d-6417-3c04-a79e-8000c8a04d11 | -4.5614 | -48.0141 | 2024-11-19 04:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| bef39c74-ba81-3b98-adff-0ff1a6d014c6 | -5.9788 | -45.3621 | 2024-11-19 04:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6187a24d-94fd-3591-be67-bfc3d58582e7 | -4.5616 | -47.9925 | 2024-11-19 04:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| bd9a2445-d685-3bed-8f34-17301ab165d3 | -4.58 | -48.0132 | 2024-11-19 04:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ef01b58f-58ec-3262-91fe-1309924e3ced | -13.2626 | -56.81968 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf2b6912-fe1e-3de3-b236-2b3abbe92e28 | -13.25592 | -56.81364 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53dffa6e-e12c-3550-8448-1a69b6b6e2ba | -20.10511 | -47.46862 | 2024-11-19 04:50:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0846c4c-14e8-3102-88bf-22614d68b5d2 | -13.26048 | -56.80967 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24f87b37-ee28-31ac-96cc-3a7e3e70e974 | -13.24844 | -56.81225 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aff5890c-2189-3e0f-9bbd-42a5e03f5d6b | -17.59406 | -43.28986 | 2024-11-19 04:50:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb7f2638-6561-3837-a83e-5e4b1759303e | -20.10963 | -47.46905 | 2024-11-19 04:50:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 253e4c70-cb76-3ea9-80da-789ebc58001c | -17.59451 | -43.28551 | 2024-11-19 04:50:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2a8d36b-64b0-3058-8f9d-7eaaea91cb8b | -20.45297 | -50.00981 | 2024-11-19 04:50:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fd0c31d-471c-315a-8e3a-13cdf478ecd6 | -13.25886 | -56.81898 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d36acf9-ca44-3c2f-90d6-32d563c63f33 | -21.19979 | -48.56137 | 2024-11-19 04:50:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e2f3c82e-7058-32b4-be22-5496220ddec6 | -16.44911 | -55.98116 | 2024-11-19 04:50:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4e2c36ee-8138-31c6-bfdb-4ad674a57cb1 | -13.26341 | -56.81503 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 653d6204-ea51-395e-ba07-fca4d327b4e5 | -15.28494 | -53.14839 | 2024-11-19 04:50:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14ab8f77-aec9-3588-bf3b-d76efa4920c2 | -13.25218 | -56.81294 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e71caa2-896a-37b3-95c2-372ae0a46177 | -13.25299 | -56.8083 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e297e09-e75b-3177-9298-ad5e6e22250a | -17.59612 | -43.28659 | 2024-11-19 04:50:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 498c6925-1a95-3666-b759-e11ec9c96350 | -13.25137 | -56.81757 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2990817c-3e0d-3891-ada5-1f282ba70f76 | -13.26422 | -56.81039 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 15912794-5bd1-31e8-b660-68c0b083ae50 | -13.25967 | -56.81433 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 125ea8ca-f3e9-3ff9-8a06-6faadaf8b7c7 | -20.76413 | -46.76791 | 2024-11-19 04:50:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6c10f58b-85b0-3fd8-9845-c4961a15e0e3 | -13.25512 | -56.81828 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5961fd7-5c4a-35be-b8aa-41842c4c82d4 | -13.25674 | -56.80899 | 2024-11-19 04:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ea87ec2-a3cb-3859-aae2-d50db11db766 | -19.27091 | -52.41288 | 2024-11-19 04:50:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 343b6bf9-133a-339f-af2c-d28e4fd91a84 | -23.97064 | -54.14328 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4faaafa1-f76c-3bd7-8f13-20bce81bd4bc | -23.91696 | -54.11003 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8409fcb6-b993-3976-b99e-0177bb37b7c1 | -23.969 | -54.13107 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| fcd90903-57ca-3928-be80-60230c653322 | -23.97007 | -54.14716 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 196b109b-98c0-3a9c-8c52-573423ffaefa | -24.01214 | -54.22494 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 40797a30-a4d6-3de5-9bb9-d7bb06e17181 | -23.94384 | -54.11473 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 83f12612-b959-352e-a126-4d7e6f04ac61 | -21.36168 | -55.90124 | 2024-11-19 04:53:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6415d7b-3f2d-392c-87b3-ae7c06f4f1c9 | -23.92145 | -54.10286 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fbed570c-926b-34ae-baad-0369aeea28cf | -23.9472 | -54.11532 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bc43a34d-1dca-383a-8de3-4f5910227e25 | -23.91309 | -54.10165 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 310f624b-9b29-324b-b8d0-915749ea0188 | -23.97286 | -54.15162 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 3d65ce1e-9915-3dc1-aa6c-0b3b4e2e82ae | -23.92817 | -54.10404 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4b7f16bb-3b85-3939-960c-ac8b5cf834e1 | -23.95113 | -54.11204 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| dc22a08e-12f9-34fd-8d3e-91a3c29143a4 | -23.95785 | -54.11321 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| cc40d3b1-69ad-319f-9512-cf4d8e1b6bcf | -23.96285 | -54.12602 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 376b16a9-57b3-36af-b637-5345c6e8b955 | -23.069 | -50.25396 | 2024-11-19 04:53:00 | NOAA-21 | ANDIRÁ | PARANÁ | Brasil | 4101101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 33043c50-f13c-33fc-913c-09a23114406a | -23.9444 | -54.11086 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2b442336-dfc1-32ce-871f-3187b5024914 | -23.95506 | -54.10875 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3311c205-8769-33c6-aff9-33d0372f5ecc | -23.94777 | -54.11145 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2ca9aee7-c469-3046-909f-015e7c7092c9 | -23.97515 | -54.13612 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f33ae9ca-2b23-36fc-9b69-cd875907f185 | -23.9695 | -54.15103 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| f0695001-2d55-3763-a659-9a422a679bae | -23.95056 | -54.11591 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| a93ddc88-035f-3003-a144-bc12af4b3a52 | -23.96621 | -54.12661 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| dc57f704-d728-3010-ac85-5c264924e7ab | -22.30484 | -49.76153 | 2024-11-19 04:53:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2ee2c8a4-83d3-3bbe-ba85-dfc782620aa0 | -23.97179 | -54.13554 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 2ab9c16b-88e8-369e-be8f-073de2f0ff8f | -23.9153 | -54.10999 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7e9ea0e6-cf2c-3c6d-a4ce-d9f1bd3ad6f6 | -22.30839 | -49.76577 | 2024-11-19 04:53:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b040afc1-adac-32af-85fc-5c86f436c719 | -23.96671 | -54.14657 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| d9caf590-1993-3f24-bfa9-57479fd805cf | -23.91866 | -54.09839 | 2024-11-19 04:53:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README37.md)
