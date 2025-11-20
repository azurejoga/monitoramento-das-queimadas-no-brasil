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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57855c23-b662-3d65-8396-103ed371cad4 | -14.45033 | -59.97589 | 2025-11-20 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6d65596-8192-30ea-9500-e9b40962b96b | -10.36999 | -48.89909 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| caa4b0f2-84d6-33c2-b000-e35306ccd726 | -17.61823 | -54.18261 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6e32fac-88a5-388b-bf53-1842b1618485 | -21.05697 | -55.81215 | 2025-11-20 05:25:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c85b4ec3-38e3-357f-9712-196a0744a872 | -9.05642 | -48.8358 | 2025-11-20 05:25:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9785ca82-377e-3819-b233-f90bb2470754 | -10.36279 | -48.90368 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| cd369d4e-1cf9-3958-857c-e1c83460fe93 | -17.53697 | -53.70453 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9876543-4fc4-3e4f-ae97-c89e69d960ba | -9.01825 | -48.66636 | 2025-11-20 05:25:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 93c459e0-2fb7-3d8f-affc-00ee4c2cc67a | -14.68772 | -59.6642 | 2025-11-20 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d7d021e-3708-3aea-bbdb-2e3c879cfc9d | -10.48779 | -49.367 | 2025-11-20 05:25:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3897d36-b5a9-336b-80c6-59b7d1f83f6e | -20.88414 | -52.34726 | 2025-11-20 05:25:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1becd85-085e-3bff-bcfe-f6d163e82e97 | -20.73787 | -55.70049 | 2025-11-20 05:25:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8718bd0e-4a4c-3016-81c2-e8b9670310d6 | -20.28909 | -50.97404 | 2025-11-20 05:25:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| a352d233-3bca-3a28-b9cd-bb309bdcd7a2 | -10.3569 | -48.90623 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 88d0b539-cca5-3faa-9280-2b8156818e74 | -9.35139 | -50.7399 | 2025-11-20 05:25:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3a9cba1-b218-30f7-bc56-01a209174cf1 | -17.53623 | -53.70438 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96658ebe-3991-30a0-b5f0-621001e46a49 | -20.29648 | -50.96369 | 2025-11-20 05:25:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 056bdcaa-28fe-3fd6-b6f5-d969e0dd1e91 | -17.53658 | -53.70103 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68e3f917-3afb-321d-b956-c5d84355fff3 | -10.36865 | -48.91057 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5397708d-2e25-3822-93f9-e6533737130c | -20.29555 | -50.97485 | 2025-11-20 05:25:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 35a55d11-c179-338d-8251-035680e9e3e3 | -17.53133 | -53.707 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb84d06e-1e5a-365a-8bf7-912611674fd3 | -15.54546 | -50.66278 | 2025-11-20 05:25:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0cd8882e-eb0d-3be6-b5b0-50b345caac79 | -17.53623 | -53.71117 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 276ed66c-0f57-3a56-8cea-a27d254e1e23 | -9.46078 | -56.64 | 2025-11-20 05:25:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a0917669-7363-3f2a-9e84-7623dc1560f1 | -10.48602 | -49.36697 | 2025-11-20 05:25:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b53b452f-1b2e-3b4c-bee9-a93c8758d1d4 | -9.01783 | -48.66515 | 2025-11-20 05:25:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47f7c523-4576-3065-9451-e6c5e22b0bea | -10.36345 | -48.89794 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 12013090-8134-3cbf-a2ee-86ae1e57afd0 | -17.62266 | -54.18976 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43aa37c3-882d-3a00-94fa-825ac45d92b4 | -18.02898 | -53.68123 | 2025-11-20 05:25:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3531a419-80e2-3720-86de-3ca2f2507ee6 | -14.85795 | -52.85492 | 2025-11-20 05:25:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a425ff1b-05b6-33d2-a342-c2b2ac0b801f | -10.36485 | -48.89575 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f6f99784-fc1a-3286-bbce-779314675e00 | -15.14952 | -58.99242 | 2025-11-20 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb7e8590-2387-3eaa-880b-489b269b4822 | -19.47952 | -53.94532 | 2025-11-20 05:25:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34b657c0-8356-3910-a155-36db2da9cb44 | -10.36415 | -48.90147 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 35825052-5a4d-318e-8a35-8611cfce5b44 | -17.62233 | -54.19283 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bfb4070-57f8-337c-847c-f959a5696708 | -20.30295 | -50.96452 | 2025-11-20 05:25:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| d85684b6-6e3b-35b1-acf2-f91d85f0bdf1 | -16.01213 | -59.90153 | 2025-11-20 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83bf3d7d-1ae3-3d7f-9609-90eacff5cb1a | -9.39602 | -54.60602 | 2025-11-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1989fca-64eb-3cf9-9186-99db71c3b9ed | -17.61857 | -54.17947 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d808a350-df2b-3c2d-8fa5-ead90c354cf7 | -9.39453 | -54.60776 | 2025-11-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b4890e4-2ebf-3eaa-b3e1-c9c4bcf68339 | -17.61789 | -54.18574 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f3dee85-4aa4-3954-9153-6b1f44216ea7 | -16.30067 | -52.93706 | 2025-11-20 05:25:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ad1ef94-4846-3f5f-80ff-74246aa6caa7 | -21.05598 | -55.8125 | 2025-11-20 05:25:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b60d3ef2-685e-37f8-a923-733a8310824b | -17.53735 | -53.7012 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd377a7c-7350-38e7-ae50-cfe318ca6573 | -10.36344 | -48.9072 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 35f76c25-89e6-3216-a7b9-274666e175ae | -17.623 | -54.18665 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1934b17-b4a5-3fdb-abb4-c72f18345984 | -17.62334 | -54.18352 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b223c81c-39e3-3cbf-ad9a-fe530cc3e828 | -15.59554 | -59.29975 | 2025-11-20 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f20bb35-af97-38cb-998f-5a412d501429 | -20.73894 | -55.70063 | 2025-11-20 05:25:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 856e17a4-f979-3175-ac3c-e791423a8756 | -14.31373 | -57.58593 | 2025-11-20 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55d08124-3087-397d-ad34-48320e330b94 | -9.39513 | -54.6032 | 2025-11-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04c26ad7-7179-36fb-8251-5911840d6b83 | -10.36932 | -48.90486 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bdf1784a-749c-3bef-8700-aa73d1ee8f94 | -19.47885 | -53.95182 | 2025-11-20 05:25:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 513dce40-ef73-33c0-8592-972cf8c1ce4d | -20.89016 | -52.34769 | 2025-11-20 05:25:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5cee85e-f397-37d7-a62b-bcc946bcbbab | -19.47918 | -53.94858 | 2025-11-20 05:25:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1a0b33a-2e0d-3cff-8b27-fc92c1c0e6d0 | -16.01196 | -59.90301 | 2025-11-20 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f418ad09-80d6-3584-a14a-a60fb3224fbd | -17.61755 | -54.18884 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cefca674-a982-3683-b9bf-3299e7b770a5 | -20.30248 | -50.97013 | 2025-11-20 05:25:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| ad4f7d2f-0d92-3864-9c13-910536fe5616 | -17.53554 | -53.71103 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43d3cc18-2f7b-3064-9a24-fd4d6e8e89fc | -10.36212 | -48.90945 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2018476e-1d83-357b-8827-2cbd2cbe21a3 | -10.3576 | -48.90047 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8bcafe5a-8d73-354c-91cb-6339bea20fbb | -17.5366 | -53.70786 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4566dd59-44f2-3dcb-b9a3-6e24f943cd3d | -20.29601 | -50.96939 | 2025-11-20 05:25:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 5f8a33d9-b87d-3aa5-98e6-1f91c0dbb01f | -10.3728 | -48.8936 | 2025-11-20 05:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 55421f13-b1e9-3b36-9a3c-ea91c8d6a1a6 | -10.3538 | -48.8957 | 2025-11-20 05:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b9680eee-4190-3bef-bd7c-251bbf7abca1 | 4.38927 | -60.18773 | 2025-11-20 05:50:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25e0b1ce-27d7-3412-831e-64ceffed03d0 | -9.16034 | -62.43185 | 2025-11-20 05:52:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2374118e-ee91-3c32-9db0-2eb102c9adf7 | -9.04072 | -64.04107 | 2025-11-20 05:52:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5fd492a-1bd8-3d3d-bfc3-e8094b2c8676 | -9.04576 | -61.95969 | 2025-11-20 05:52:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88d44644-9180-351b-b878-2998026faa74 | -9.04684 | -61.95206 | 2025-11-20 05:52:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48f09595-03a1-3da3-8123-18f3bb52232e | -9.03704 | -64.04054 | 2025-11-20 05:52:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22eecdec-f39a-3b0f-a39f-17e38452d645 | -9.0463 | -61.95588 | 2025-11-20 05:52:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bb189f1-2443-3d17-9241-32689ebed298 | -9.04213 | -61.95525 | 2025-11-20 05:52:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da2998ac-eb08-3b75-8abc-8e2832dd5c43 | -3.0478 | -59.18768 | 2025-11-20 05:52:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1be3b2d-6c7e-3582-92ac-21786c502ffe | -12.42397 | -64.14077 | 2025-11-20 05:54:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b738a45b-05f2-39a9-9aba-e42732d25f67 | -9.85307 | -63.98288 | 2025-11-20 05:54:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7897520c-9f3b-3cec-9362-5656e628748a | -9.73317 | -63.64655 | 2025-11-20 05:54:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f32a6906-12c4-3ec4-ab40-91ad8e43df91 | -12.42778 | -64.14131 | 2025-11-20 05:54:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc9a23e1-6b76-3a09-89a8-ac7515ccbb8e | -10.62125 | -65.27364 | 2025-11-20 05:54:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac9eed9f-9c90-363c-9a33-8c875f794d93 | -9.63525 | -67.48429 | 2025-11-20 05:54:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5d359f7-8551-3082-ac89-eeb90854f966 | -9.6347 | -67.48779 | 2025-11-20 05:54:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10a1b4a6-e6c2-34f4-8177-19c621f24409 | -14.49238 | -59.75199 | 2025-11-20 05:54:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95d70d5a-3ebf-3e62-a76c-ffa466a76e71 | -9.93418 | -65.19889 | 2025-11-20 05:54:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4f83e2c-1253-34dd-bedb-a13c664df43f | -9.63187 | -62.40347 | 2025-11-20 05:54:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6495f66-9dd2-3c33-a62f-d7edde733a8b | -12.42546 | -64.18426 | 2025-11-20 05:54:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e76d46ae-0e7a-3e46-b8d1-1a10b8cdff02 | -9.4956 | -63.5095 | 2025-11-20 05:54:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e6dc0a0-7731-32b4-8ef5-45973925666a | -9.63208 | -67.48757 | 2025-11-20 06:14:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3676c54-4914-355f-aba1-94dc95ec28d5 | -3.56038 | -43.47658 | 2025-11-20 06:14:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 7bd30e77-9a90-3134-89cf-36e5ed4811b8 | -4.10309 | -50.06359 | 2025-11-20 06:14:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d5fafbb6-fa22-35a0-87e1-c7c635c8f836 | -9.63653 | -67.48821 | 2025-11-20 06:14:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4dbbf2c-07bb-3e9e-9346-72d38a67c3c8 | -10.83269 | -56.96159 | 2025-11-20 06:16:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a16a58db-285e-3b85-ae08-2e0b4bde2da2 | -10.35748 | -48.89933 | 2025-11-20 06:16:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 1ec14d2c-a5f0-34bf-8c19-f7e437a15ba8 | -9.34531 | -50.737 | 2025-11-20 06:16:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f55b0b5f-67ac-3bf6-b8ba-6f8ea48e77b5 | -10.36661 | -48.9007 | 2025-11-20 06:16:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f442b6ac-44d0-3c1f-8359-b3dd358c0b07 | -10.35607 | -48.909 | 2025-11-20 06:16:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f22a09ff-f6fb-33e1-9de9-e274841bf34f | -12.87808 | -50.15192 | 2025-11-20 06:16:00 | AQUA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 76fa4821-dd17-3b46-bba8-0cf5902e25e7 | -10.35888 | -48.88968 | 2025-11-20 06:16:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d5c35a85-ad15-3703-8116-571de93b494c | -17.53431 | -53.70454 | 2025-11-20 06:18:00 | AQUA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 376f3ba6-7be9-307a-90ce-77732accc512 | -20.28665 | -50.96938 | 2025-11-20 06:20:00 | AQUA_M-M | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| 9ec74719-685b-3701-a73c-e3b5079fbfa0 | -20.29727 | -50.96059 | 2025-11-20 06:20:00 | AQUA_M-M | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |


[Clique aqui para ver as próximas entradas](README16.md)
