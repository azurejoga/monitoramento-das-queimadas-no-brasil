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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd133de5-18f6-3e06-a687-cecbff3773d0 | -9.0995 | -61.43614 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1047c663-2ba9-3006-b212-fe0e70d08b31 | -6.74041 | -55.30925 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4804b588-0fad-3e1d-8bef-aeca7da013be | -4.25926 | -60.00616 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3505ddbc-3a24-3939-a83c-f6e3ca654979 | -5.77377 | -47.15613 | 2026-09-23 05:04:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 90c6df79-080f-3ad2-8556-474ca04eddf5 | -7.98492 | -47.4702 | 2026-09-23 05:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab678c29-8d6a-3a86-8f20-eb7368fb539b | -3.72056 | -60.57413 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c141b9c-afd3-35f4-b0c4-0568aec869fc | -11.30368 | -51.36497 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db885e32-d0dc-3d47-bed0-a80a4bf53e2d | -8.17326 | -54.78207 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bb4230c-8d3b-359c-8fae-e8bcd35894c7 | -6.10399 | -57.67316 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d2da445c-cb9f-31c8-8e1a-cd475fdb9790 | -5.89254 | -52.2782 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf8ac81d-752e-3ea0-9150-d65074bbb055 | -6.13222 | -57.75601 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17bed826-1f4b-3d00-bcd1-d237a8c493e1 | -6.46628 | -59.98743 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e378859-13e9-37ab-9c94-234be94407ff | -9.1728 | -51.474 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff5adc79-730b-365a-a5ca-5eee7c38e8c5 | -11.88782 | -45.76419 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6f3c4e8-0493-3693-aecb-fe1e2da9a065 | -8.92598 | -61.4903 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f677426-f935-386e-ba7b-8b5851d20dea | -3.81954 | -58.88223 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f819bac-1233-313b-810f-3a07e4fe4d5c | -8.45404 | -48.69849 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89b04c7f-4350-3244-a997-edabbed9ce18 | -8.80384 | -44.26651 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3025b3d7-8b83-381b-b264-6a43d0e36a5a | -6.45148 | -54.99869 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db134e43-1538-32cd-9ca6-b8a6a781a4ba | -8.6536 | -62.49995 | 2026-09-23 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab6d24f8-f11f-3365-906b-14b5d84009be | -3.0782 | -58.40627 | 2026-09-23 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19776701-135e-39fe-b93b-4cfb03230421 | -11.77901 | -50.99548 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76f9d7ee-1d7c-3f9f-b544-bb3b6daedf88 | -5.87668 | -52.07635 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e63b8828-1710-39ee-a224-bf90a35c93ee | -9.9427 | -48.46825 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a99c6504-04ff-3a47-8d6a-0ebbcc9ef79a | -6.6739 | -55.0727 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 430fbcb3-34a9-3020-9d09-5733b4f566d2 | -11.29959 | -51.36835 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e70a5c0f-e86a-39aa-b8bb-14a83c21f0e5 | -5.87845 | -52.13005 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0a9f52b-8165-31fe-bc3b-04be734d143d | -4.1553 | -60.79507 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 127cca49-1237-3be0-aa8c-d8fc41a28bc4 | -11.74848 | -51.01752 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe0d359a-e4dc-3673-bed2-75d5bd1bfe2b | -10.4591 | -44.94518 | 2026-09-23 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87711b76-cf7a-3a43-ada1-857079253801 | -10.87245 | -50.15609 | 2026-09-23 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59570de8-afbb-35a8-a5af-c9c59b628d87 | -3.11778 | -60.68198 | 2026-09-23 05:04:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0885a01-b8cf-379d-9e4e-53fbe650e7aa | -8.25127 | -50.86686 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5f5b2a3-161c-3b95-90ba-8f57faa67fc9 | -6.28188 | -59.91997 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d70fc582-7b37-3d7d-9bee-ce2e9fa1d660 | -6.64494 | -50.92989 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35aee679-0d72-31b8-a79f-4d9bca5fd287 | -6.465 | -59.96662 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 781eca26-fb32-3f10-8fb2-9e20d2fe9df6 | -7.09964 | -52.75114 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a248eb14-40d4-3be9-9372-85d2c37a8118 | -6.34809 | -57.77385 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5c834d0c-8ab2-3368-922d-33c2715315cc | -6.04013 | -57.82696 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fde26aa6-52e2-30de-aa6a-f2de418f2ae0 | -6.03872 | -53.27157 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35874bdc-dced-3787-8cae-d8332f2d74cb | -6.09992 | -57.67246 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37655a7c-a0c6-3169-bc90-0fa3f8e9fbfd | -6.60978 | -59.92152 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 871251fe-5511-3e17-99fa-a2f91dbd372e | -5.73721 | -53.46909 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ca74280-8728-3d4f-ac78-fed40ebc16d8 | -11.13073 | -42.78204 | 2026-09-23 05:04:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 46bd7b85-f039-3288-9565-2289b82edcfa | -4.06615 | -56.22112 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a994716-e891-3095-95e1-19e77613a231 | -6.0415 | -53.27561 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ade1328-0934-3ec1-bc2c-b3bb38c60fdb | -5.73778 | -53.46555 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 502cdb8f-3c93-337d-b480-5a5919bd7e53 | -6.67001 | -50.9488 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e733707-b41c-32ee-89ba-537b7ea077de | -4.00505 | -52.08648 | 2026-09-23 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 527fc17a-304d-3d8c-96b2-4c020a98a4b8 | -6.61293 | -43.72813 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0dcd8f5-f040-30f5-bfd5-519add809b3c | -6.72463 | -44.15456 | 2026-09-23 05:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4b2f705b-d129-3a45-978d-88680e6a7ba2 | -4.08844 | -62.09323 | 2026-09-23 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb8a42de-cc18-3d89-9be9-384cd7aa2fe5 | -8.36062 | -45.61432 | 2026-09-23 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5081cc37-64bd-300e-a209-0c5e5b3a82fc | -5.28188 | -60.20358 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e14169c-d138-3738-b56f-cf760b9eb657 | -8.21027 | -56.09072 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fd79c4d-21ca-3e0d-8a06-683115dcd13c | -5.88111 | -51.57508 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db8cc4c-09a5-3445-8730-4997269bac12 | -6.63783 | -59.93315 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1c35e414-83ed-39a2-9bcc-b1992df4afda | -9.59773 | -63.91981 | 2026-09-23 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c866496-71a4-340c-8399-a5701afbbbad | -7.43103 | -49.83871 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2c65126a-b430-30c2-93f8-5fab6425e896 | -7.78614 | -50.22784 | 2026-09-23 05:04:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b5b7bab-1f77-3321-86b5-1a104a902ccb | -6.73687 | -55.08701 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ce25a2b-a6bc-3752-a69e-4691d5c534a4 | -11.78499 | -50.97961 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22a47c1c-7eec-39b2-9367-db4e10e27598 | -8.91528 | -50.92541 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e27e8690-f6af-36ed-b01f-3eb016f902e2 | -3.15487 | -57.6935 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6258ace5-f022-3163-9c89-724edd41a532 | -8.46335 | -51.4833 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74a37119-480b-3ff0-b1b7-b94eb9dd1ad3 | -9.57904 | -46.53304 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 16635bf5-1332-3144-bced-422096ed4928 | -6.47825 | -48.45995 | 2026-09-23 05:04:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b78e875a-ca91-376d-b0d0-3a5e88486ab5 | -6.93282 | -46.56701 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c83a1eb-2649-32f6-a7ea-71233d0e9cb6 | -7.3975 | -55.21834 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d22c9a2-9356-35b2-87c9-012f91eff7ea | -6.37882 | -42.78848 | 2026-09-23 05:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e7ad7a7e-dbbf-3aef-a9aa-0d1e7e19e6c8 | -10.89824 | -53.96419 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b3aeb86-f432-3979-903e-4ec0725ef7a7 | -6.66951 | -50.88456 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ba11393-3a80-31cb-93f6-6c3364c41589 | -6.67328 | -58.57173 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fb184515-d48a-391d-a86c-c174d9b5bb39 | -7.31434 | -55.21781 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d042d05c-2f4a-3bbe-8c12-138ef2d6ef0a | -6.67537 | -58.55958 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4177182-3094-3cbf-9206-fceb93788816 | -5.85725 | -52.03059 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cb8796d-23b4-3efd-8da7-403e090b9d2a | -5.87112 | -52.06833 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 924b5340-51fe-328d-a28a-6dad2dffd9db | -12.01886 | -47.80599 | 2026-09-23 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 44421729-56f0-3d21-827c-8f59e3c23f33 | -3.24656 | -60.80701 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d124315-e143-38a9-8363-f0691342f0a1 | -5.34798 | -45.17018 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 688be191-e202-3667-a3a2-64247bed8e88 | -6.67178 | -58.55486 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a57eed3-99ae-3ac5-a67f-84183a03f3d8 | -8.4618 | -48.6997 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc73251a-2bca-36a6-9184-678144a723da | -3.74276 | -58.86763 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4da9046-9e8f-3adc-8f6f-07afffad4a7b | -5.34329 | -45.16944 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f69cf100-1774-33b2-9a32-759593314a8c | -6.31141 | -57.74975 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 338ac3c5-366b-38c2-bfb7-0125d86b289f | -6.30819 | -59.94182 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32979266-d81a-3535-99bf-4e76bb230bc9 | -6.34872 | -57.77017 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e73a9ff0-3edb-3781-8231-6389a0da82c0 | -6.44054 | -48.44961 | 2026-09-23 05:04:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acfdcbc4-138e-3a39-9f8f-a80ab95d23cc | -8.25751 | -54.78017 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f0c03c5-52fb-332c-ab51-094b3ee56f32 | -6.61755 | -59.96552 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 071dac3c-ce81-39cc-964e-24742949d159 | -7.43345 | -49.8471 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d4a98bad-389b-3c4b-a3e0-93731f9c3360 | -6.64809 | -59.9299 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6fca6747-fefe-3c29-9be0-f798da9633c9 | -9.54815 | -45.77535 | 2026-09-23 05:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b69a129-31d5-368c-b7fe-c796a20204c8 | -3.69016 | -60.56562 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4cfa092-4b53-36d6-a617-122d7c9f9867 | -11.40778 | -44.03585 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f798441a-5917-35a7-aed6-35071a9207ef | -3.7257 | -60.57508 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58ad619e-280d-3957-8020-e7b0479829f5 | -9.94168 | -48.47527 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 655dbed8-2d46-34bd-aadb-f40f9090e122 | -7.4618 | -45.50183 | 2026-09-23 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a28d3d91-238f-3128-b2a5-df794b38c1b9 | -10.91606 | -53.93819 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17f2d1ad-8eda-3b0f-a7a9-92fa0dc10377 | -8.83145 | -45.9297 | 2026-09-23 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README95.md)
