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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2fabbc8-2b9b-3e6d-a7b1-658dd0504cab | -6.59828 | -58.97945 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15ea2e76-cf4a-331c-94e6-2570c217ce21 | -9.06382 | -60.40343 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e587f341-6276-3c8a-aa9b-98e3dc06e42c | -10.51542 | -50.79008 | 2026-08-17 04:57:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ca20297-5501-3427-9702-7dfd87cbd507 | -7.77982 | -48.27512 | 2026-08-17 04:57:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08e25ce7-c85d-32fa-8db4-b6a23cf88157 | -11.47012 | -46.58508 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7f5fc55-a0e8-31e0-b47d-3f5cb3046f65 | -9.34646 | -63.56533 | 2026-08-17 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bdedde0-ccc9-326a-92d3-91410d74f6b8 | -8.90581 | -60.5558 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c96e7c4b-b659-3689-9390-63e1a3097191 | -10.92618 | -57.12845 | 2026-08-17 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dec1f66e-5ba4-30e0-a7e1-6c64d279f203 | -8.50987 | -54.89951 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28b0cb7c-8b05-3180-ba74-3d1c579e5fa8 | -9.36987 | -57.36414 | 2026-08-17 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c18dc548-9714-397d-b26f-54ec1e6faae2 | -14.71787 | -47.9725 | 2026-08-17 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfe9815a-55f9-38b6-ba6b-5272045b3e59 | -14.50021 | -51.99 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e30350c7-723b-3d13-8080-810629b1207e | -8.97858 | -60.51073 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c62a627d-44fe-3346-9427-c8fadb1bd59e | -8.73451 | -62.91263 | 2026-08-17 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea8cf3d0-ffb5-30aa-8b7f-e90a9aff4b3c | -12.24847 | -47.01019 | 2026-08-17 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88c82eeb-2c02-3e4d-8118-b4a09435777d | -6.62342 | -58.96412 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 41e691c9-73b9-3108-9298-29610a2c0cbb | -11.22721 | -54.01994 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 178ae7f4-fe78-3590-af9f-788bd1e9a479 | -6.99055 | -59.02882 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6de4074-6f36-332e-b779-12911b91c53c | -14.48382 | -45.67919 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bdab3c02-343d-3555-a3ca-bbe29cfa3c2d | -9.54479 | -56.80214 | 2026-08-17 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7a6eee3-c030-32ad-91de-f8fd1d40b31a | -12.7551 | -48.43134 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8ba0597-6d42-350b-ae38-c48b9d8ed879 | -8.98033 | -60.5305 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ca77f29-cae8-32ff-8308-c941fc5c79fd | -9.47767 | -51.60778 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1bf4d3b-4ab6-3095-a022-e86222c09cf9 | -9.47137 | -60.50356 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 927dfd91-0c96-3fd6-bfa4-2114df175a18 | -11.83342 | -51.77118 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 49cbb6ac-84c2-31a0-b0ea-4a4578d7ae6f | -10.94328 | -57.14817 | 2026-08-17 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d45f7b4f-67b0-3c5d-bda1-83f744531432 | -13.44304 | -43.84365 | 2026-08-17 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8f971c59-d47e-35e9-949e-5579bcea809d | -13.50509 | -46.23852 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a21fa5f5-8e47-3e8b-bb42-72d3b60d4f8c | -8.52585 | -54.89328 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 644c9c30-b29d-3816-8a86-3c3b52202afd | -8.89845 | -60.59683 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd08c5d2-0a61-3174-a688-04a832b5fa7e | -11.49958 | -46.59007 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1e7af87-c2c2-31bc-b672-6d621f7f8055 | -9.70198 | -47.66274 | 2026-08-17 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da0e6862-717e-371a-905e-dd4c1587e5da | -6.61761 | -58.96864 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1396b730-05b0-301e-9cba-e13aec98bca9 | -8.04297 | -54.0177 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f33394bd-ff86-3dd3-b446-63ad2c416d12 | -11.58113 | -54.68774 | 2026-08-17 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c837ce5e-9441-315b-8700-78924e5332ae | -12.04784 | -46.48077 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cce30c23-3937-3816-8c10-08461cf7c3cd | -14.32406 | -53.09639 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b50c8040-2c32-3a4b-9ad4-9a32e81962c5 | -12.36266 | -50.89006 | 2026-08-17 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9373091a-da1f-3a4b-8dcd-78e9920df00b | -8.52228 | -54.91456 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2942736f-e332-344b-abd6-3a1cc80929ee | -12.66703 | -48.51163 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2977fab7-a6ac-3915-b478-bd9d03e45951 | -6.873 | -56.41159 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7604c463-a3c7-305a-9314-db68b01a76d3 | -15.16203 | -48.61798 | 2026-08-17 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9056d614-08d7-3f17-923b-7c3f7382a264 | -9.48489 | -51.66984 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78172afb-aa64-3e75-896c-f2b1d6bfbee1 | -11.32521 | -46.21152 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0856ff2-ceaf-3e28-8069-08511a669fe2 | -11.23746 | -54.83794 | 2026-08-17 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 001d70cd-4718-3787-aab9-a50a4956a52f | -7.42956 | -60.02801 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce029c46-1435-3b4d-bde4-82e6ea7342cc | -10.4751 | -50.37096 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5459d5e-bd75-358b-a48d-a6a73ec6449d | -7.59161 | -61.2291 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8f11799-a0e2-38cb-85d9-88df4206bd03 | -8.90638 | -60.55265 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 29d931b2-1c36-39af-8605-f7c37d281c93 | -9.13112 | -46.01936 | 2026-08-17 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63c2772c-c502-3468-b3f3-65b7bf999139 | -11.91828 | -55.45368 | 2026-08-17 04:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bda9f4ca-68a9-37d6-9f66-5433b10fdefc | -7.43639 | -60.01951 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf556bc8-2bea-3835-82a3-d835358636e0 | -9.4915 | -51.60641 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 13ba03bc-fd34-31e7-b096-22f636590b2d | -14.05891 | -53.69699 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2462f8cc-6df4-3366-b7d7-1b01cd70c715 | -9.49482 | -51.60694 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afe3fdb0-b7cf-31cd-b4fb-e09e50af4003 | -12.04941 | -46.45056 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fab11dac-5bfd-3061-bb43-cc124e574ab9 | -11.32746 | -47.01457 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1a5c4de-83cb-3793-878c-e7bed3ba0e6e | -12.33159 | -47.24751 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9cab60ba-3426-3592-be50-94c49c675689 | -14.48917 | -45.67476 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a83edf1-940d-3787-8f77-3f8bfc455a8a | -7.80806 | -47.83789 | 2026-08-17 04:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9f594856-84fc-3e7e-b4c6-9d27591238e5 | -6.8212 | -56.45158 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 955324cc-10ac-3475-a2e7-76c56f23f572 | -13.52111 | -46.25467 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| feb3a02c-3943-39c4-aa31-eb2a9b2212f7 | -7.38929 | -55.48789 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 448948ab-eba7-3d99-ab9b-6ab0b7bbf172 | -9.37579 | -62.36298 | 2026-08-17 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91a30067-3e74-337b-9e43-2245c1dcf929 | -12.70067 | -48.52096 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15b4669b-14c7-3442-8b04-71686574bfeb | -8.90185 | -60.57791 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4011fbb-5fda-3d99-9b66-8302198f334a | -12.66324 | -48.51095 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8aa2428-1196-3aa6-9fa9-939c62209f11 | -8.0318 | -55.14003 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 212be9fb-a47f-3770-9c0c-f94749134349 | -7.36104 | -55.49288 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68538c3c-e8b7-3978-b5db-301e2b78b4a9 | -8.95789 | -60.53609 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61980afb-a58b-311d-8b02-6948290a850d | -9.30228 | -56.80976 | 2026-08-17 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06d113d4-c03e-3823-880d-27b859e402d1 | -14.49014 | -51.98836 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e8be145-4c61-36a2-bc8e-8d25877a731f | -12.66012 | -48.50559 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be0b3904-ceab-3e37-ae50-e7b19bb74723 | -11.51386 | -54.63303 | 2026-08-17 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7656d57c-f358-3ada-a854-602d2fbad39e | -11.71045 | -54.62562 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb0cee55-77f0-3039-b29f-f5b0f809b461 | -13.52158 | -46.28547 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff101506-fb43-31dc-8231-e831f39a3f5a | -10.37263 | -48.30641 | 2026-08-17 04:57:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ea243ea-2a33-3193-b240-2556a9dccd68 | -9.45917 | -50.31086 | 2026-08-17 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 688c8a2c-2662-3b70-894c-bd08dfcc9d74 | -10.48591 | -50.36885 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d4e0222-8bdd-31c1-acd6-69dc62283166 | -6.97415 | -59.03701 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88e26ccd-ce01-33d4-9784-1557c0f5a31e | -6.76809 | -59.47867 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6bb03271-bfd6-32fb-8cef-590dbc0193af | -6.62564 | -59.06517 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7983c91d-fc0d-37c1-a1e1-201d096d828a | -14.3064 | -47.18577 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8f9701f-d919-3c5c-bfa4-f3e5115a2480 | -10.9222 | -57.1277 | 2026-08-17 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b7cf984-6260-3a46-bb67-96e9e1562f71 | -11.61687 | -47.79698 | 2026-08-17 04:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e2a4c264-2954-3361-b668-1f8e94f6afea | -9.27275 | -45.64706 | 2026-08-17 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3874d8dd-3e49-35fc-abec-9e6db1334741 | -8.60476 | -54.7092 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29d24767-5236-348a-b176-9e77a4f73c21 | -11.39212 | -46.40829 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8d14236-a9a1-3e0c-9ac3-6ae6cc398d07 | -6.6534 | -58.96412 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1c041dc4-ac75-395f-bd8f-22dd3ba5a2d8 | -9.3001 | -56.91883 | 2026-08-17 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49f8884d-b54a-3dc3-b56c-02de2e90ca55 | -11.196 | -54.82801 | 2026-08-17 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27b3890b-84ea-3db4-b8fa-c3fd5756e521 | -6.96913 | -59.30172 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cf214d1-f620-31b6-a27e-0705e13030f2 | -6.70164 | -58.94487 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 705212d2-0837-3d70-ac12-30e7bf05fed9 | -8.9734 | -60.50982 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8b831c8-f598-3d0e-b913-4b355d03f3ec | -11.54805 | -46.22717 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66347dba-0cff-3591-8fe0-516a1f3abe3f | -8.06498 | -48.53206 | 2026-08-17 04:57:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 88cdc169-6433-39f8-bf32-4db734ce2b0f | -8.9763 | -60.52322 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e576bb7a-05e4-3f73-886d-7ac2c3249675 | -10.46605 | -46.29996 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7764e7cc-2b5e-3b0c-a024-c8fd984383bd | -8.67451 | -54.76189 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53aa6f1d-af3e-3660-9fec-c7d6cfb1f9b9 | -11.46592 | -46.58426 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README36.md)
