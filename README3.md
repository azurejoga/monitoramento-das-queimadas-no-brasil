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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66676e92-15bc-3fe8-9323-8ce55e462f0c | -6.75843 | -59.15105 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| e05c38b4-5230-37d4-88ce-288379267511 | -8.57872 | -54.76802 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 475cf326-8582-37a3-9bd2-eb5a6369dad1 | -8.67405 | -54.63048 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 182a12fc-90d7-320f-9cc7-dd20e6f1aae9 | -10.31296 | -50.44625 | 2026-08-19 00:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8d8afcf7-74f7-37f3-93b1-4c3b2a218c53 | -6.33844 | -54.89777 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0b5bd3db-5b06-3629-989b-fb6911a326d9 | -6.01979 | -50.19764 | 2026-08-19 00:09:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| b786966a-ef26-3f0a-bf73-1746fac318f0 | -10.81018 | -50.30185 | 2026-08-19 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d1e71598-7600-3038-80c7-8744175ff587 | -11.31915 | -45.2146 | 2026-08-19 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7c76ef84-73eb-3ef8-8f41-64df38b34671 | -14.48139 | -45.67238 | 2026-08-19 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| b713970c-3fb7-3908-ac0d-b85290f3c5f7 | -8.57745 | -54.67564 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 08efbc56-c84c-3774-bf83-e05fa1c71a21 | -5.90957 | -43.64362 | 2026-08-19 00:09:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| f4d20e7a-4f46-37f1-a2d7-fcdc91d0facd | -12.78749 | -48.42702 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 186bebe9-6386-32b1-b8ed-469966868af1 | -11.99977 | -53.44468 | 2026-08-19 00:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 6a3cd8f4-edea-3a4f-8896-e8381a559800 | -6.68999 | -59.07838 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| b29c05c2-f82c-38d4-ac31-80934f700513 | -12.47265 | -54.19484 | 2026-08-19 00:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b3f6a8e7-3df6-308b-aef8-fe02adb53114 | -6.86805 | -59.04417 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| cc75c9af-08c7-3e38-87f8-524ef6b0bba6 | -6.33536 | -44.06441 | 2026-08-19 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| af80869e-95b3-3c75-8af0-01bd840777d1 | -7.55972 | -55.57802 | 2026-08-19 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 43297b05-ba75-3b8c-a65b-ff8552db523a | -6.70273 | -58.94198 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 223.5 |
| fc13af65-2504-3c79-be23-598ada60ae54 | -12.47092 | -54.18115 | 2026-08-19 00:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 16556474-d044-32fd-bb49-fdfb0a6e93d9 | -11.19996 | -54.81684 | 2026-08-19 00:09:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c068861d-96dd-322b-8ea6-4f5213691956 | -6.44375 | -52.75139 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 77d7eff1-6874-31a5-a85f-aa239105e80a | -6.35199 | -54.92119 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 437125af-d49e-3b1e-bee9-3f69f9b37873 | -11.31857 | -45.20905 | 2026-08-19 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 671dfa8a-13f0-36e9-be72-8ba55a58025a | -6.84511 | -58.99929 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| fb694b08-d972-377c-8427-f4c3eeb07ae6 | -8.55416 | -54.74454 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 1ded2893-1c50-3332-9248-21f20d14402f | -8.54613 | -48.29708 | 2026-08-19 00:09:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a0392f25-3e58-3acb-8f94-3618877bd901 | -6.35039 | -54.90876 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 33a5da5a-b68f-3656-bf56-45c2e97543f8 | -11.03148 | -51.05167 | 2026-08-19 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9d6f2a91-b1e5-3fac-922c-b1efbca46caf | -6.81196 | -59.4553 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 849c8684-b3ab-3a49-a9c8-de7766f7a5c8 | -9.41515 | -60.41977 | 2026-08-19 00:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 90f9fabd-27f7-3564-a65c-78ab9cbdef39 | -8.92974 | -47.6022 | 2026-08-19 00:09:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f3e081b8-e0f1-34f2-b5a2-93b1e2fe05c8 | -6.88591 | -59.06916 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d786f82e-ea27-36e0-a217-eb821ed3a679 | -9.41967 | -60.4577 | 2026-08-19 00:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| c6ee831c-486e-3969-a676-fd3ba9f2a949 | -13.43981 | -43.84386 | 2026-08-19 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 1f465e11-4f28-3b9e-be84-f35d9f0aac7b | -9.4028 | -60.56977 | 2026-08-19 00:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 201.9 |
| 2c08ed56-6584-36cb-ab43-ebac825b7dcd | -9.73721 | -46.83568 | 2026-08-19 00:09:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a0315387-4c7a-3431-9542-080fdc7458d0 | -8.53136 | -54.73438 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 8f202e4c-c2fa-3886-83e4-33ff5d9675ee | -5.91974 | -43.61688 | 2026-08-19 00:09:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 264.7 |
| f6fdee55-8454-353f-8aca-469e28112c8a | -8.57364 | -54.72882 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 398b5452-148b-3044-ad46-fcf24f66eb2f | -6.61377 | -58.95983 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 31d5c22f-c676-3727-a797-9a896ee28994 | -6.39118 | -51.74824 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 23a9860a-e9e6-316e-ae3d-3eb77518e61c | -11.21852 | -55.06234 | 2026-08-19 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| d7089f01-0226-3608-96f8-e3c228bd18c3 | -10.68379 | -49.00435 | 2026-08-19 00:09:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2c695c03-a47e-31eb-a4f1-d672aa777911 | -6.68593 | -58.95068 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 8df3b8e4-4cc3-3329-901c-884f812e6ec2 | -5.73971 | -51.70145 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 68d1b4a3-fb31-32a3-8869-b43d8a8a1a07 | -9.08001 | -50.79821 | 2026-08-19 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 2ec24c90-c4c3-3774-8b4e-09c0128198f1 | -6.85344 | -59.04588 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 138501be-5c3e-339f-9be9-34ffa9ccc866 | -11.20458 | -54.01903 | 2026-08-19 00:09:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| d2b97f85-ca45-31f8-9345-f5105b54fd02 | -6.69153 | -58.97012 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| a3203ac5-5764-314b-b5c7-32c92f0d7c65 | -10.19622 | -54.24915 | 2026-08-19 00:09:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e047ca64-087c-37f1-9028-f013f7b62787 | -11.06427 | -46.51782 | 2026-08-19 00:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| a256bbe3-6db0-3f0f-8054-2a40b8b18a90 | -5.4389 | -48.41201 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 5617d707-46a8-3010-b42a-8f448eea2dd7 | -6.84704 | -58.99243 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 18983242-9bcc-32dd-adad-9a86630c9373 | -11.73362 | -54.59464 | 2026-08-19 00:09:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a1f066d3-4a4d-31cb-89e7-3bf0ed69f890 | -15.20305 | -48.22592 | 2026-08-19 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| d05ed9aa-b9c1-3793-be0d-f4d719e25e6b | -10.18577 | -54.25054 | 2026-08-19 00:09:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8e864c0d-a557-39a8-8dd1-190744acf27b | -8.10162 | -51.6641 | 2026-08-19 00:09:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| f68833d4-8e98-3754-8535-5a2b77c66095 | -8.56691 | -54.67693 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b71a7863-a0b7-312d-b152-9d827112a6a4 | -11.12709 | -47.28729 | 2026-08-19 00:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0fd5f594-0eda-3fa3-a16b-da1a8cb0497b | -13.5818 | -51.68583 | 2026-08-19 00:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 1df5f574-2999-37bc-8e76-97f5c9ecc288 | -8.49945 | -54.86528 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 407356ae-0ca6-339f-8d30-bb9f2ff6984a | -15.31445 | -56.45224 | 2026-08-19 00:09:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 8814582c-9482-3eb6-8935-8d63ae0b4d58 | -6.75325 | -59.46959 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| b98b4bc9-fe44-3075-8284-40b19cf772e8 | -9.08881 | -50.79696 | 2026-08-19 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e2f1ec6c-84fd-3831-a3f4-52092b93457c | -15.20439 | -48.23527 | 2026-08-19 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 04f69e65-b212-3936-9871-71a59b5abbb5 | -9.11886 | -46.047 | 2026-08-19 00:09:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| fecea8a1-7cf6-3e0d-b0e1-ec3c19025410 | -8.49776 | -54.85221 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 98a9d8d5-1226-3622-953a-7bee8d8d7e64 | -10.8114 | -50.31076 | 2026-08-19 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4615f349-52a9-309f-b0bd-a0dfb16fc9f9 | -8.73164 | -49.61346 | 2026-08-19 00:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| a21359a5-a5b0-31db-bfe6-da4d2d11daac | -14.01877 | -53.70649 | 2026-08-19 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b7d38752-32d6-379a-8ffc-f6542581747e | -12.5198 | -47.84727 | 2026-08-19 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8d51ab2d-9ad4-3c7a-adc0-9d242ed77cdd | -11.6955 | -54.55573 | 2026-08-19 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| c6e7efe7-d1c9-3534-8b8a-50a42dc71f45 | -7.41413 | -49.61898 | 2026-08-19 00:09:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| e5b6347b-57d7-384c-9290-eca79ac6d718 | -7.42813 | -59.79624 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 790ec71b-0307-3895-b9b6-59f3697a3ac0 | -5.91943 | -43.64765 | 2026-08-19 00:09:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 461d8eb9-ef0a-333b-8b80-e72d0aed801e | -7.10815 | -59.76497 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| b1b266ea-e2c3-3b10-a28d-8aa9d1d89a64 | -8.36039 | -45.97981 | 2026-08-19 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| adf62439-c8ef-3b3b-93b8-c26cf9f7aba1 | -7.43298 | -59.80114 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| d3f16d87-90c0-3a22-8216-80c93ca7cb20 | -6.28004 | -55.97081 | 2026-08-19 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 568a37d7-e89e-3001-9877-7d0b38d7403b | -10.12489 | -52.12218 | 2026-08-19 00:09:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 4bbc608f-8dbf-3d20-8c15-f461b571a293 | -9.39482 | -60.53802 | 2026-08-19 00:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 7c0aae0a-2a44-38cd-a522-7bdedbeb97e7 | -6.79692 | -59.45733 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a5dd1b06-e374-3ed4-83b6-d0f4c0f4d992 | -6.75931 | -59.1461 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| fc23e26b-f4cb-3910-94eb-f8c28a24b443 | -6.35912 | -54.89493 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8b8fed42-7fd1-3c5b-8a42-e782ce453a4f | -10.31174 | -50.43736 | 2026-08-19 00:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c5a28775-9ea9-3a90-be9d-32a33561c23a | -7.56897 | -55.56207 | 2026-08-19 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 9184c7d2-7880-3112-9fc5-04a10ddfa896 | -9.39932 | -60.57672 | 2026-08-19 00:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 230.1 |
| ab71e125-ec7d-3905-a464-594bcd7bb735 | -5.79804 | -43.91997 | 2026-08-19 00:09:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 3dd916e5-02f2-3b4c-96eb-eb24fc638be7 | -8.57533 | -54.74184 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| ee5658f7-54df-37b1-83c1-beba488acba0 | -7.05347 | -59.83394 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 814496e3-fe89-3618-9ccf-090de3e1ee82 | -14.45304 | -45.62552 | 2026-08-19 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 1bab45e1-9909-395e-87fa-933d865c41ba | -8.11129 | -51.65654 | 2026-08-19 00:09:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9b4603e5-8cf7-3dc2-97b2-0ca8e3261fce | -10.6825 | -48.9951 | 2026-08-19 00:09:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 35e2440e-a307-389c-869d-e7024e129553 | -9.42391 | -60.45063 | 2026-08-19 00:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 65a5b4e7-d21c-36ec-bdb1-6d1684c53fc0 | -8.53632 | -54.77364 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 87ee8afc-d14c-3e25-ba70-a83fd040b783 | -12.47429 | -54.17434 | 2026-08-19 00:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5c14786f-7770-30e0-83c0-474b56b2e654 | -15.06429 | -45.33539 | 2026-08-19 00:09:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6238acf2-211f-3088-af9d-8fe682faecfe | -8.56812 | -54.76942 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 174.7 |
| c1908fcb-6da2-3a54-8a05-fed70d8cccbb | -6.34877 | -54.89632 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |


[Clique aqui para ver as próximas entradas](README4.md)
