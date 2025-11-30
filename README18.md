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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe381a64-3df2-3870-abbc-0efabeb0d81e | -2.60673 | -47.34062 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc17032d-b57e-32e9-835e-3b32f5d59c50 | -2.89988 | -45.2686 | 2025-11-30 04:44:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ab76755-e48a-399c-8028-2944a9a85db6 | 0.85143 | -50.18577 | 2025-11-30 04:44:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08dd08c3-3216-3a86-8f67-e27e40eeef2e | -2.32007 | -49.16721 | 2025-11-30 04:44:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f945846-ad41-33b3-b043-40ebb4f9fc7f | -1.11845 | -47.73476 | 2025-11-30 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5843b6ba-bc5b-3ef6-b8ad-4957538d9f4f | -3.07828 | -46.64742 | 2025-11-30 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70812fe7-c5c8-3132-8e49-a02cafcbbb9f | -2.57574 | -49.09843 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e620f43-593c-3b95-9cbe-b78ea04f3820 | -2.23615 | -51.56678 | 2025-11-30 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef00c221-c878-3740-9f14-ab39210b616c | -2.6452 | -48.54851 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5b34f508-bb18-37d1-a1f2-c81ac7e00e95 | -2.64802 | -48.55268 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6f223a75-8058-333c-95be-bc5b52f9a4c0 | -1.1567 | -48.09444 | 2025-11-30 04:44:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d3ac2d7-6dcd-3669-8b5f-763900bbc9bc | -3.58611 | -41.66495 | 2025-11-30 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| da189551-2341-3aa0-82ec-1af65015ae13 | -3.58041 | -41.66734 | 2025-11-30 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa6b8fe1-4543-3f60-9e4b-bfe8f91f3d0a | -2.64462 | -48.55216 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 251e2251-4523-364d-81f9-4cfa52b5b7ce | -2.69694 | -49.31882 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0bd0b4fb-0418-3cc3-9ddf-4d578db9cef4 | -3.28076 | -50.65861 | 2025-11-30 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c4f176d9-e6c2-3b0e-b4ea-3e5479a7750d | -4.42457 | -43.30871 | 2025-11-30 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e84247a6-483d-379a-ab0e-e6b4086472a8 | -2.43449 | -45.73924 | 2025-11-30 04:44:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ea2dc04-e33c-38b5-9cf0-1084f631a6f7 | -2.14205 | -48.52016 | 2025-11-30 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e04f314-00c5-3539-bff8-10a9dcca5e6d | -3.58564 | -41.66808 | 2025-11-30 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cb324a41-edbe-3cba-9624-68f938bc6b6f | -2.51333 | -49.1032 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4605e3b-6486-3bde-9abd-22b161483bf5 | -3.22921 | -45.53187 | 2025-11-30 04:44:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f004e50-188f-3ae1-8268-a5f2589b6764 | -0.96148 | -46.8009 | 2025-11-30 04:44:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebb7c4ed-3bba-36f2-bbf6-4e86530e1fe6 | -4.35853 | -43.16398 | 2025-11-30 04:44:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67d57717-ee43-3ebf-bca1-20b46c4cc1ea | -2.20894 | -48.002 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32be17af-3a7d-327b-aa56-c99216139d54 | -2.83565 | -48.82938 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a57bd24-25c8-3010-af00-3b6083fa3555 | -2.70484 | -48.34742 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4f64775-f6b3-31e7-af1f-2e9d07278ed6 | -2.69882 | -47.3989 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3565f323-7ed2-3363-9358-06e992d7b83a | -3.2511 | -50.69626 | 2025-11-30 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 016f6fb6-76c7-3438-8d77-2984174ca0cd | -2.41411 | -49.34644 | 2025-11-30 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 268b6158-18a7-30ae-9d96-b88db9889d0e | -3.28211 | -50.77873 | 2025-11-30 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a54f83bb-cfcb-32e7-a8f3-6f077795c6a6 | -2.30754 | -48.40016 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7492ea58-b88f-33cb-8413-be7fd28456e7 | -4.35776 | -43.16744 | 2025-11-30 04:44:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 77aad379-211a-3938-8473-a127371b2b10 | -2.69526 | -47.39838 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b69b498e-a475-3fc9-be5a-f795726e8856 | -2.38646 | -47.61301 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee0f789e-f769-30df-b1ba-259db4509721 | -3.58678 | -45.6249 | 2025-11-30 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33ca63ea-f141-3456-897d-42f6b635c602 | -1.39944 | -50.73713 | 2025-11-30 04:44:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78030e00-3dca-314a-b1ae-d87292a4bdee | -2.24322 | -46.52444 | 2025-11-30 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51109baa-c81f-3666-bd2b-695a12f58d1d | 0.85474 | -50.18525 | 2025-11-30 04:44:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ee4d953-b353-3cd0-b30c-8618e78e0a29 | -1.99207 | -48.70755 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cb3509c4-ea77-3f78-8938-8b694ee8c9a1 | -2.54607 | -48.35386 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95fc1e77-8e88-36fc-bde3-23434aa6ca5a | -2.60015 | -49.26409 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1f450d8-c8fe-3cd2-8dbd-7d30af22869b | -2.64123 | -48.55164 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| df4fcc46-665a-3676-b0d4-85ee1cccedd1 | -2.63501 | -48.54695 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8de36410-ce94-3636-8bbd-778cd6cdb6d0 | -2.47323 | -46.28256 | 2025-11-30 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 71a783b4-ad2b-3c60-98b1-235bd16586d1 | -2.42074 | -47.23508 | 2025-11-30 04:44:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f645ca3f-59be-327b-9c72-541e1442506f | -2.50906 | -49.21768 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41b84260-d42d-3a7b-ae9a-4adea2bfc34d | -2.00593 | -46.42076 | 2025-11-30 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73f37e9a-817e-3381-82aa-096d31482b5a | -2.64066 | -48.55528 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4cad746-3937-3dd1-abc9-6cb6393222a1 | -2.59627 | -49.26707 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34d99e0a-19c9-3ddc-9857-41de43fb8bbf | -2.68307 | -47.35946 | 2025-11-30 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca64d56-01b6-342f-9cb6-0bdaa2b88423 | -1.90327 | -46.4564 | 2025-11-30 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac2451ef-d0a9-3996-9123-1b3b7a31c537 | -2.70426 | -48.35111 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87644337-e043-3b82-936f-6036acb2dc72 | 0.30134 | -50.87342 | 2025-11-30 04:44:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c29a5e0-2111-384c-bfb8-89b1b8e99b28 | -2.63162 | -48.54642 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6002d851-260c-3738-87d3-b119fcbd147c | -2.24693 | -46.52501 | 2025-11-30 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15491fb2-1acd-3f52-aca2-b86ea8d9b959 | -3.2332 | -45.53246 | 2025-11-30 04:44:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70b235d6-24de-3c6b-96c3-749023e7ecbd | -5.75046 | -40.8192 | 2025-11-30 04:44:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad9988c4-e360-3473-ba5a-0f80f84bb634 | -3.00854 | -50.46754 | 2025-11-30 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1832779-b4f0-32a3-9345-5f96580c799a | -6.30241 | -43.81263 | 2025-11-30 04:46:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f684cc2d-d2bd-35ca-a729-27da94f62918 | -6.30962 | -43.81118 | 2025-11-30 04:46:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01c47b25-4f62-39d3-b6e8-b97bbc5263f2 | -7.46704 | -39.96362 | 2025-11-30 04:46:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7b13c18b-d680-3cae-9d2a-e5b97a25556b | -6.3089 | -43.81635 | 2025-11-30 04:46:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb8821ce-c779-3fd2-a5af-5a4c33b7191e | -12.65571 | -46.75194 | 2025-11-30 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 545a6583-86da-3732-93f7-72a521dcecb2 | -12.00418 | -49.26159 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b93c62b3-7921-3572-a36b-9e5ddeba5685 | -8.04236 | -43.13306 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a0230370-ae7e-33f7-9e3f-88d74da851f7 | -7.74062 | -44.18433 | 2025-11-30 04:46:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ee9a229-d282-3856-8a8e-73c6bd36cf1b | -8.04821 | -43.12787 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c61ec771-e67e-3856-9da7-c1da05c5ddc5 | -12.01498 | -49.2632 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ebf915a-f9fa-3ca2-8dd0-2316dabce41d | -5.9233 | -42.91254 | 2025-11-30 04:46:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d2b8e7e3-e9ac-3de4-9b5a-a47bd6768909 | -6.30023 | -43.80973 | 2025-11-30 04:46:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e8e22bb-1eda-3516-b726-d0d38076901d | -8.04276 | -43.13011 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 45b0bcdb-f37f-317b-8d8e-c1e3b15b2f04 | -8.03225 | -43.13164 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fd68b9f8-c09f-3c77-a1dc-a685ea8ab117 | -12.00233 | -49.26246 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52db1f9e-d6d7-3e2a-b457-ab2085e64fab | -10.71761 | -47.26126 | 2025-11-30 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e6da081-428c-3a77-b50b-38be16318bb0 | -12.0053 | -49.26722 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ce3f8476-78dc-3a85-ab25-acab32219067 | -7.74531 | -44.18493 | 2025-11-30 04:46:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc5be95b-6ad7-3a17-bd81-bb37108bdd93 | -12.00593 | -49.26299 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7504d100-aa7a-30e4-a9bd-a0c07dcab37e | -8.04741 | -43.13375 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a5b4ab46-644d-30b8-8956-147488b61f88 | -6.22344 | -55.63717 | 2025-11-30 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9511dcd4-7860-31ca-a9f6-b4962247ed52 | -7.74858 | -44.19535 | 2025-11-30 04:46:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 829aa2ef-9c5f-3408-90cd-4f1c33697ed3 | -6.71003 | -41.50633 | 2025-11-30 04:46:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6b880c71-b8d6-3764-b37e-3de2c6e1aa5b | -12.01077 | -49.26689 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70491099-0e49-36af-9722-91e39f5b28dc | -7.75162 | -44.19318 | 2025-11-30 04:46:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf7bc021-5696-3378-8baa-83d730a129bb | -7.73594 | -44.18371 | 2025-11-30 04:46:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d668f0a-03fe-3fce-91e6-78394785043e | -12.01437 | -49.26743 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 60bc8809-1627-3f66-9412-e65ecfa31f9d | -12.01858 | -49.26374 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 837ad111-fe6c-3a2b-991e-8fc24b30116e | -12.01016 | -49.27112 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c160b952-8499-3c44-b800-139563239750 | -8.16785 | -43.18818 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 24400817-c669-3106-b07e-d4c7e164c758 | -5.70719 | -45.63224 | 2025-11-30 04:46:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 204170b3-5b30-3883-b3dc-301316744ec1 | -8.04316 | -43.12716 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a3ba1a1a-d42a-30c0-8fd0-b3c61df13e6a | -6.21953 | -55.63652 | 2025-11-30 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d95cf828-f846-3d65-8e37-6a62a7290d05 | -6.71508 | -41.51054 | 2025-11-30 04:46:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3e77d6c0-61fc-3541-9d60-879759ee97e0 | -10.71834 | -47.25611 | 2025-11-30 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fef2669-972a-32e0-8c08-85f6a233d97a | -12.00717 | -49.26635 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4132bc1-5068-3e36-92f1-ea7e54e31c88 | -8.03265 | -43.12868 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 32964671-abe4-390f-835b-b21da8303f85 | -6.3042 | -43.81566 | 2025-11-30 04:46:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d40bcedf-ece7-32bb-97be-3e278aa6de5f | -11.39798 | -49.19108 | 2025-11-30 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e8908343-3b60-3616-89d6-30f8f0939e1e | -12.00778 | -49.26212 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 977a8fff-55df-3ad1-ad5e-e7c4ff5d2e24 | -10.71436 | -47.25558 | 2025-11-30 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README19.md)
