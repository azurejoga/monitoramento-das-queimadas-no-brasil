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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0977a072-dea9-3046-bb2b-f401e05049d7 | -6.16804 | -48.04984 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| cb8fa9e9-965b-336f-a9ed-08e2ff710a0f | -11.43958 | -45.11558 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 354638cf-9b23-3e1a-9951-78a98cc3eae3 | -5.78112 | -43.61143 | 2025-07-09 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8339340b-ee74-3f5c-a480-d476a0c073d0 | -8.51092 | -43.27214 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 5b69d19a-299a-3dd2-be61-64b84c9f1cee | -11.90568 | -44.91276 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d0becf9-696d-3e13-9ebc-26f0f6e8ef77 | -9.28185 | -40.51868 | 2025-07-09 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d6593462-0043-3796-bb22-8948c2bcbad4 | -11.45255 | -45.11403 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88776823-cc58-35bb-ab1f-4246500f5f83 | -11.44369 | -45.11632 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1499c0c4-00c4-337a-99c0-de7a58dae417 | -8.50937 | -43.28162 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 2f002c13-f6fd-3c00-b9e5-b9bcefd93a1f | -11.46036 | -45.11118 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b2b44376-921b-3bd9-a0f3-810421b5f6c4 | -12.47588 | -46.91 | 2025-07-09 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 827bf8d4-2162-33ef-8c5b-32d9ab0f33ce | -11.47858 | -47.92663 | 2025-07-09 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bcfd18dc-eb3e-3d80-925c-66fe63b2e58c | -8.50553 | -43.28096 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 5851879d-55d2-3833-bb79-26448e7b4739 | -8.50372 | -43.28307 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| ee9d01ac-d84b-38d4-a992-62cd6f2a3d7c | -10.85992 | -44.61757 | 2025-07-09 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0a2747c-6f86-3d3e-b691-61835cf57a04 | -6.83909 | -44.03696 | 2025-07-09 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d96c06d5-86ef-36a3-9409-c545f50c4b10 | -5.58773 | -52.07697 | 2025-07-09 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0338415-108a-333a-a22c-074c807766bb | -8.22779 | -44.9313 | 2025-07-09 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9fc22b5-a66c-3314-be4c-e72f9dedff50 | -6.63949 | -43.19476 | 2025-07-09 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 07ef5b7b-e3d9-3097-b619-c83e4aff30aa | -11.50906 | -48.95661 | 2025-07-09 03:55:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce190800-8091-33cc-a79d-de5688f5fb74 | -8.51743 | -43.2952 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7616eb9d-65ee-3b7d-b299-013c3e06af7f | -11.42661 | -45.11714 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6f31f80-12ef-3219-84c8-e46081b9bc8b | -8.51219 | -43.27963 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| f7d645e9-d17e-3eaf-9dcb-5184fdb77585 | -8.50534 | -43.27359 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 384ccc5d-1445-36eb-a415-24bf1a7fae77 | -11.44089 | -45.10806 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 53627b17-f110-3a75-962d-e4d899de8642 | -6.68104 | -46.30278 | 2025-07-09 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ed74c872-ff59-36c0-b021-6c0a6f0ac368 | -6.38797 | -43.03667 | 2025-07-09 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8689591-180c-3901-9d8b-568eacc1fa7e | -6.95885 | -43.26009 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e85eb78-2389-3b7d-8f4f-6a65a6e51094 | -12.9811 | -44.8721 | 2025-07-09 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9b4d348-25b9-34d3-a76d-effd7dccc415 | -6.17344 | -48.05605 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 9e69b135-8710-3c9d-a1bf-ce23aedddc2b | -5.78171 | -43.60789 | 2025-07-09 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 609c0348-d302-3b4e-8038-481467934a33 | -11.43808 | -45.09981 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0bae8633-793f-3f6d-a76e-172048ebd37e | -10.63512 | -49.46527 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c311c06b-bf0d-3394-99b6-c3dee700b761 | -7.23996 | -43.07674 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3c512e7b-e3a5-3daf-8c99-55fb2b0c7095 | -7.83639 | -44.19197 | 2025-07-09 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 932953e8-9e28-3087-9915-caa0a20ae67d | -8.76182 | -47.67833 | 2025-07-09 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 664fd591-c705-3597-a3de-2a24d1e00a55 | -6.95629 | -42.70754 | 2025-07-09 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 14fd5bbb-2243-312a-8f34-aa03ae8dd99b | -9.23211 | -48.59669 | 2025-07-09 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fc5c9a4a-ee7d-34b0-a4cf-4cbc067bc32f | -8.76237 | -47.67529 | 2025-07-09 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eed29d54-2bb2-32d7-a6c3-17ef745db594 | -12.98506 | -44.87276 | 2025-07-09 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 466f3706-d672-3320-85d0-62c366a4c75a | -7.57226 | -47.06259 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b4e097e-5381-30fe-a5ae-f3378689d8dd | -6.17405 | -48.0476 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| e04e3f75-661f-3697-811b-ab733b9d1c6b | -7.67722 | -44.36177 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4002c21a-fac6-376e-b49d-3ade4a6303bc | -6.73264 | -44.34003 | 2025-07-09 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9cc6fa8-7440-32de-8f36-b2c15fb5f2f2 | -12.9784 | -44.88758 | 2025-07-09 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5998c15-dbf1-35f1-b392-dfeb31d5900f | -10.4627 | -47.946 | 2025-07-09 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6857728-7057-343e-8a89-39be538244eb | -6.61085 | -42.22434 | 2025-07-09 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af6dfd65-461c-3ab0-a6ae-61602e22c9a1 | -11.43418 | -45.12237 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 48c617ee-fa2f-3785-96be-b81706c0aea7 | -10.17923 | -51.15394 | 2025-07-09 03:55:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 268a0db8-c52e-34a7-99f5-c74d56659337 | -7.24078 | -43.0719 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ef8831d0-fc2e-382a-b4c2-39e30b062262 | -11.44693 | -45.09753 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50a3a265-6008-3653-95b6-e14fc5b9dfc4 | -10.56126 | -49.13244 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3cf72185-c2e7-387b-aa17-50d73f6fedc0 | -11.43007 | -45.12164 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 300bf5cf-1a89-3982-bd96-22f63d43a3e1 | -7.07327 | -43.5136 | 2025-07-09 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8bd4376-5457-3e69-9e0a-66ec86ac6e6e | -6.72842 | -44.33934 | 2025-07-09 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 497fa1d2-276a-3331-ae67-dc0dbf96fd7b | -10.17828 | -51.15882 | 2025-07-09 03:55:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8e3d9cb-4e58-387c-ab85-352044f973f3 | -11.6789 | -43.78312 | 2025-07-09 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f029c6ef-c0a7-3b02-bb85-44782e25a0b1 | -12.04924 | -48.54759 | 2025-07-09 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3c24bad-8d24-3156-a126-23d742a6ec15 | -5.77522 | -43.62173 | 2025-07-09 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98569843-983a-3f8a-bf3e-8f9ff9a49c0a | -8.22711 | -44.93535 | 2025-07-09 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae3a7e9d-6051-3fef-9c09-95a129f9208e | -6.74196 | -43.159 | 2025-07-09 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b65cd5e4-7e26-36dc-8a0e-af04bc8e8f8d | -9.28663 | -44.83783 | 2025-07-09 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8f7754d-c233-3387-8557-1e91e803ce85 | -6.6813 | -46.30628 | 2025-07-09 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c238499-75d9-3f86-bd22-246bfb804a07 | -11.47388 | -47.92928 | 2025-07-09 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 83ad3579-d432-36b8-98a8-9fa05bb434b2 | -8.22215 | -44.93869 | 2025-07-09 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2af8ea71-5a76-39e3-8b7c-188d982dd09c | -11.43829 | -45.1231 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8ad39c18-a3ff-3d0c-a944-a07d52539309 | -6.9815 | -47.08397 | 2025-07-09 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c12c0ce-3242-3796-85f9-3af59bbe7b6d | -7.0902 | -44.15454 | 2025-07-09 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16febd5d-2f42-3587-8017-91087f2b845a | -13.57344 | -40.6409 | 2025-07-09 03:55:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e7c310eb-7312-32da-9819-3c6b466656c3 | -9.40608 | -48.45028 | 2025-07-09 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fe3cf9b-3257-3c5a-a4d9-708199c60dbe | -6.96019 | -42.70623 | 2025-07-09 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 25dc6740-28bd-386c-85cf-58471ea8d2b5 | -11.44629 | -45.10128 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f40ebe6c-dfc8-3443-929a-2e317c5cce52 | -10.57281 | -49.13098 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b6a1282d-c958-3843-9d28-ef4ea1f49461 | -7.66274 | -44.37118 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eca0af2e-b416-3715-9364-07218453f033 | -5.50432 | -45.49129 | 2025-07-09 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9825b46a-da1d-3491-b294-ea02503cbc1f | -8.51522 | -43.28503 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 62c0c4c2-497b-3292-8f43-f955c3e218e5 | -11.43894 | -45.11934 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1d377eee-0545-3b3d-ae3c-9e030be7963e | -10.64758 | -44.49034 | 2025-07-09 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a6b5b946-0ecf-3b78-ba67-84e119b15145 | -9.20891 | -47.63136 | 2025-07-09 03:55:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3c6b777-352f-3ca8-a999-c2c8a17a9cc0 | -8.50755 | -43.28373 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 305960f8-b867-3899-b8e0-a7d9a7f52f81 | -11.42726 | -45.11337 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| a7ba082f-df4c-3bdf-b1b3-7f5e756130d7 | -6.57103 | -48.24685 | 2025-07-09 03:55:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1030dd7a-c8dd-3b80-aa22-0c089bfe92b7 | -6.53306 | -43.54102 | 2025-07-09 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df39f576-1b40-3097-92a4-c1aee4e1580c | -11.4197 | -45.10814 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 611788e2-262e-32fd-a637-61aa553783cc | -8.513 | -43.27491 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 01d64ef3-4175-3416-908d-bef6ae1e0385 | -10.56197 | -49.12872 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 00227af2-8809-3761-8b60-9b2b3df9a2c9 | -5.58602 | -45.33898 | 2025-07-09 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1e266e6-45dd-3395-8fbb-41ea500cc6ef | -12.05493 | -48.54548 | 2025-07-09 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d6bc510-f8c7-3196-99c0-7332de0eea3d | -9.28127 | -40.52229 | 2025-07-09 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d46248d-15ef-39c4-ab71-c547c9d3c000 | -6.17404 | -48.05273 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| ad199cfb-2341-3c43-948d-541cf49d9f6e | -7.08654 | -49.16718 | 2025-07-09 03:55:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| efce6005-a2a0-3f83-b763-d6741f8bc789 | -8.50623 | -43.30075 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c9fe60f6-b876-3aed-9fcb-e2da7f0d0a7c | -5.95988 | -44.18087 | 2025-07-09 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a0dbc88-c967-3b40-a9fc-908d7db7d92d | -12.98416 | -44.8779 | 2025-07-09 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d494b4a7-6b60-3a5c-976c-e330765f80d9 | -11.43613 | -45.11108 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7a3cb86-6611-3bea-8080-b50e5cad06a1 | -6.16859 | -48.05165 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e81023bd-5a68-3606-862d-63fc6dfc8652 | -6.16919 | -48.0483 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 87d43ed2-2d18-3d5f-9519-ca6c3d2a233a | -7.5461 | -45.65398 | 2025-07-09 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05661ec1-f29c-3bad-bd10-747e6f15bba6 | -8.50631 | -43.27621 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| f2be1e26-048d-32c0-b527-db7f053f0dec | -10.5783 | -49.13179 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README9.md)
