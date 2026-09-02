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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be99042d-826a-3dde-a447-8547222db884 | -10.77992 | -44.7532 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e240ddea-0340-390a-8605-423c2e9b1263 | -8.80467 | -49.62879 | 2026-09-02 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 213b35ba-8be1-37c0-b691-81be6e814e06 | -15.68044 | -45.89512 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f69f285c-b72a-3186-b09d-e2320f5955d3 | -15.6487 | -45.90129 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df16707e-5678-37e0-bec7-ef0c5c8d46cf | -12.13378 | -47.0596 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a1660c64-ae65-348e-b5f2-66abb36ed9d6 | -10.39993 | -50.00624 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a8a29466-a327-39d9-b531-b35a013ca7b0 | -10.43958 | -46.73862 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a661bf99-20d3-3b26-a7f1-59a994e43b7b | -9.66926 | -48.27085 | 2026-09-02 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10d05070-7999-3c94-9747-4db8046fc710 | -8.4472 | -54.7155 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ae9a55d-78e0-3bdd-b190-7e415173c92c | -13.40956 | -43.87875 | 2026-09-02 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de7d4ea1-11e4-3887-afe2-30e2c49f7580 | -13.18681 | -44.07586 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f4d561b-0a1f-32b3-adf7-3dcde140075b | -11.34876 | -50.62868 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0ab621b-66b7-3b05-9b23-4ea998af4c40 | -9.94276 | -53.99417 | 2026-09-02 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5e4ff20-c184-307c-9709-2c2fc75ba9d8 | -12.16766 | -47.06151 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fedaf2f4-cc59-3ed1-a158-bb3083da601f | -10.9046 | -45.33433 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4fdb8b36-5e3f-3f29-8686-c5719be87044 | -11.47943 | -45.08867 | 2026-09-02 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 25ae32be-f8ef-3a71-875e-93109c445eeb | -10.6815 | -54.04954 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4a27c362-3881-30a0-a1c5-a189d54fa784 | -9.69201 | -47.17616 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a40d2805-c640-397b-98fc-de814e2f2d27 | -15.03618 | -48.18747 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52a4b0f0-c946-33eb-8df1-9d29248d7c7a | -8.1194 | -54.95766 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b211d1f6-7823-3599-8d63-ef278ef9d280 | -11.82326 | -46.05272 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 378d2ec5-c4c1-3224-ae35-3010c9458c43 | -15.65928 | -45.89922 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46bf7ee4-17c7-3877-8f68-5f8b1dbea4d9 | -9.94777 | -53.99501 | 2026-09-02 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e1dec06-8556-3f5c-9d85-10da37dc9a6b | -8.44434 | -54.70051 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9af6d7a4-f12f-32ed-8a6c-bfb8b1d9e9d5 | -10.99567 | -48.39793 | 2026-09-02 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f2b313e-be10-315d-b20a-895a3685d510 | -10.88256 | -45.34522 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 31e386b3-dfa4-3cd1-9c10-686f7e590e0d | -8.47782 | -54.71406 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 8af54da5-b81d-3256-8781-5008b804d2a5 | -10.79497 | -44.76657 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8147f05-91e4-3784-8358-cc705ddd1e4d | -14.32525 | -47.22794 | 2026-09-02 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a085d8d-cb53-3382-a20d-47fdc2103de7 | -11.47998 | -45.08511 | 2026-09-02 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a02083c9-91bf-3042-97e9-0b4c75134ac5 | -8.44844 | -54.70858 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 952c8ced-2ca4-3578-a19c-82692cc08077 | -10.7688 | -54.04778 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ac5905cf-a0f3-3760-bdb0-e08c929475cf | -8.45425 | -54.73817 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbe85d94-7a08-3a6e-b198-1c7aa620858f | -11.52737 | -46.91594 | 2026-09-02 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b09f6ce-2751-3e31-9907-75b60271a124 | -9.71966 | -48.14392 | 2026-09-02 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40bf562e-a77b-3349-bca7-471fc58d329b | -6.9542 | -56.4548 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e106ab85-20bb-3439-97a7-55a7b4f424dd | -12.15133 | -47.12122 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba5c869a-ba18-3e52-a17f-df79f1cf4822 | -12.15182 | -47.13968 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db5692bb-1a23-35e3-af1a-ff71d2958fad | -12.37278 | -39.58196 | 2026-09-02 04:21:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b6af6812-7276-3f15-9a65-532f60aa6a25 | -12.07957 | -47.12045 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c553aba1-a8ea-34f3-8528-cf932a831f09 | -10.77712 | -44.74911 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed1cff09-2c8f-369a-ab64-4f3c55e1523b | -11.82548 | -46.06027 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 52bd1b00-30ac-34f0-ac0b-a2831232f211 | -12.15239 | -47.1361 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3370249e-18ec-3015-9675-6488b90f9b9f | -10.77681 | -50.48508 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac6c7ffe-92d7-3c51-b525-9fc3076218b1 | -13.40042 | -51.38208 | 2026-09-02 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6fd6c764-7c0a-3ba3-b672-24678c1cb647 | -8.8014 | -46.46983 | 2026-09-02 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09c4c331-0e4e-30f1-863d-0f053608f124 | -11.30416 | -45.16661 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fda655f7-9649-3f42-b7d0-d8ad6fa44319 | -15.37592 | -47.6797 | 2026-09-02 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 545e6f2b-314f-346b-8b3d-14935352a047 | -15.36507 | -47.03934 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ceb58769-4880-3449-af20-b4f67eec4ab9 | -11.30354 | -45.14835 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa2f526f-6e90-3963-8779-fe1463495507 | -10.38477 | -49.98655 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3eb4ed9-0a20-3e9b-b218-b9eee902e5df | -12.14857 | -47.11709 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04feef50-a2a8-385e-9b7e-6e411e13794e | -12.37557 | -48.15248 | 2026-09-02 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b83ab56-5575-341e-ab3c-e724bc09684a | -8.44344 | -54.73635 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 44397790-9660-3a98-9ce2-4c44381ad713 | -12.14629 | -47.13142 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 74c359f6-6b81-3ccd-b39f-c855a7273a0b | -12.05607 | -45.00614 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28319552-33a9-3754-b8bc-d8cfd1509a9c | -6.76138 | -56.33351 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a854a0c8-e27f-3dd0-ba4e-16abe1b9a8d4 | -8.44532 | -54.72591 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af86744a-eaa0-36d9-a5a9-be3dbb2c7cff | -12.14515 | -47.13859 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec9f00f1-12e4-39ec-8785-30ec1b1ee87e | -11.29364 | -45.16861 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0bd7d06e-d64f-3305-97af-35839ebe1690 | -12.10884 | -47.28017 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2899cbc4-20ca-35b1-8192-70a21c43a450 | -8.46319 | -54.73289 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5a09ebe-8b75-3253-9156-e0273ecb5bad | -14.02699 | -47.79171 | 2026-09-02 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebd57e8a-591b-3ed9-b270-533a461f7d4b | -9.2141 | -48.58335 | 2026-09-02 04:21:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3ee3598-252c-3468-b69e-255e6a81e22a | -11.7614 | -50.55146 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eef75664-8856-360f-8756-d23d1fdb6e0a | -10.70486 | -46.20233 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17fc8e4f-aa37-3e40-85bd-50fb2b841edc | -10.39045 | -45.07664 | 2026-09-02 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee7b7134-df23-39d3-aecf-45e35efbf49c | -8.43166 | -54.70918 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3ec7ad0a-310b-3e7f-855b-d9905240a9e2 | -11.03603 | -57.23543 | 2026-09-02 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f3ab342-80c3-3dba-95d5-4388be671e03 | -13.54192 | -43.31084 | 2026-09-02 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 437468c2-d90e-3381-8d91-b283910a4135 | -9.702 | -47.20036 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68eeda4f-ee21-37e9-8425-87d1b2ca8c28 | -8.42976 | -54.7197 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd8bd8f4-9436-3b48-967e-14e3fe7682f2 | -13.40664 | -43.87421 | 2026-09-02 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 702e0f38-9c94-3484-b341-aae771174380 | -11.3322 | -50.58432 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9735356e-869b-3918-a288-723c7c4af80c | -6.1581 | -57.77679 | 2026-09-02 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 85889ded-d938-31d4-a0c1-3ceb259ed395 | -11.91055 | -45.04601 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac93f283-38e2-33f8-8bc9-5143710a0dca | -8.44884 | -54.73728 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eaec84ed-0746-31fa-a4ed-b2092be9fb71 | -8.42913 | -54.72316 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 11079a81-c540-3cf0-afd4-a2506d2a2e21 | -12.14124 | -47.14163 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 698fc162-827c-31db-8a64-f988170e6a36 | -14.96244 | -48.11021 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d32d08c1-646c-3924-903b-8ffddf6f5097 | -11.72829 | -50.53551 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e44d394-0f8a-3e0d-8768-117a1f498796 | -14.11663 | -45.50307 | 2026-09-02 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11d5638f-ff0e-309a-99a6-17c7ddc0cb19 | -8.48136 | -54.71083 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 196e3b6c-dab4-3756-a8bb-ff69be1ab298 | -8.48042 | -54.70003 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 734d938c-704f-3513-a9a0-5954aeca0d51 | -9.00573 | -50.77903 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5350d996-a3f4-323b-8e7e-5532e1d0c4f0 | -12.18828 | -40.40871 | 2026-09-02 04:21:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8d419520-4d67-391c-a5fe-7cf8f0ab8244 | -12.0768 | -47.11634 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43f65ff3-0f2d-31a1-8a58-419fe49fe273 | -12.08463 | -47.11024 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6f89de4-c938-3766-bb7e-710e7e1bc4ee | -14.96795 | -48.11873 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ef0545e-84c7-3a36-a8b8-06f159263400 | -13.07695 | -45.1697 | 2026-09-02 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01566da3-6c87-3032-bd7c-c745eaac1f15 | -9.67916 | -48.27671 | 2026-09-02 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8611b8f0-01b8-35b9-8206-ec78d0844e2a | -14.98835 | -48.03566 | 2026-09-02 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06c8bb5c-3f0f-37f8-9d28-eb2d1e9a11d7 | -8.43515 | -54.72062 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01340586-276a-348f-a297-4f8b5e9e6f70 | -9.63891 | -45.71228 | 2026-09-02 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae19c81e-9b18-3c60-960d-4d947baadf76 | -11.5268 | -46.91951 | 2026-09-02 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cf4038a-bceb-38ef-bd26-1cae6dc70734 | -11.66101 | -50.18624 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6ee4d780-cb62-3173-a3f9-be92945d757b | -11.12562 | -51.5295 | 2026-09-02 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b90e8da-cbae-32a3-89ed-adef24a63317 | -10.75056 | -54.06923 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 64d23f5d-31c4-3f1b-8bf7-78fa5da2327d | -12.37215 | -48.15192 | 2026-09-02 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44551cd4-3f74-37ab-b82c-b82ca8cbf522 | -8.42629 | -54.70815 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README28.md)
