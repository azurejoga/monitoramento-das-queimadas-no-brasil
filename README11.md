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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73a3ea43-a351-36b5-99f1-59ea0394eee6 | -8.93512 | -44.40872 | 2026-09-11 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b503560-17e0-3d0b-b294-e0aa83a39344 | -10.77193 | -45.93991 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58321d3f-dd9f-3f7b-965b-9b156d0947b8 | -10.64234 | -46.12608 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8a49de6-0e9e-399b-96b2-a1bc60798bc1 | -8.77503 | -44.17817 | 2026-09-11 04:08:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ad1a8e47-5ff0-3915-b25e-d6f784e68b66 | -8.94474 | -44.41961 | 2026-09-11 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fc2cbbc-2c6d-3a38-801d-20fe70a76152 | -4.23908 | -49.94395 | 2026-09-11 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de78f959-e1dd-39e4-97ab-f9fdff872e4d | -4.29522 | -49.10909 | 2026-09-11 04:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 42e38a58-e115-3875-b439-040da66f7f6f | -9.78045 | -43.44498 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9740c725-a07a-398a-a588-7eb9ef516f54 | -10.7798 | -45.94144 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 8b57523a-8c5d-3a07-88ac-c56b134f19ce | -10.22067 | -45.21192 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 060e3b99-a205-320e-9e7b-dbf3f157eec6 | -8.70293 | -49.62018 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 558693be-d3a9-3a55-969a-c1c26fe1fd5d | -6.23742 | -51.69193 | 2026-09-11 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00b4f70c-20b3-3995-820d-9711983fc54c | -8.6344 | -47.41754 | 2026-09-11 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22211cc0-4f11-37e3-a0af-f0cfd261cb55 | -8.35113 | -42.41646 | 2026-09-11 04:08:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dcf9e686-bf38-39af-be47-6feae0b9da31 | -6.12993 | -43.74652 | 2026-09-11 04:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cc00788-b1b3-32a5-b740-d38aa07998f6 | -8.93959 | -44.40475 | 2026-09-11 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aba33f47-e1da-36b5-8514-07affe6087b5 | -8.50103 | -50.15137 | 2026-09-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb0f08a6-664a-3238-bb77-f08ba7f209c4 | -8.7846 | -44.18877 | 2026-09-11 04:08:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bfd3af7-869a-35a6-be46-13ef63771d8a | -11.11166 | -47.07568 | 2026-09-11 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dabd8a23-e357-3876-85f4-c34f4513cdbe | -10.78069 | -45.93641 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 21664e1c-f34e-3cfa-94f6-fa427c5ba47f | -11.34499 | -45.79502 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| def5990f-6d37-311e-888f-53c2c30253ce | -8.70817 | -49.62105 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6fd79be1-82ca-3480-8d9f-133c72161d8a | -10.77425 | -45.93285 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c168e36-6cfe-3465-b5f7-dac2a7cfad63 | -6.73105 | -45.44754 | 2026-09-11 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4aee512e-7a83-3e8a-a243-97b526efff31 | -11.3453 | -45.79708 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e370014-bf25-3c0c-ae0c-011fa82ae8c9 | -10.13466 | -36.31783 | 2026-09-11 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 5e5c4361-660d-325b-ac71-2d9f327a4cf9 | -10.26599 | -45.26159 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd4532f5-e92c-3bdb-962c-e28c60b54f6c | -8.27636 | -47.7872 | 2026-09-11 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2e39f1d-0cab-3252-b0db-4f8faeb18a8c | -10.73307 | -46.15024 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fc67629-f69e-3eb4-8e06-e34acc4f4501 | -11.39143 | -43.9596 | 2026-09-11 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81c966ef-d932-3d9a-91c2-41d2b065f520 | -10.76977 | -45.92915 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 226f03d4-631f-313d-af0e-6ed37a154ad0 | -10.78127 | -45.93943 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| edce547f-fdf2-30a2-b00d-742290c3bc36 | -10.70654 | -46.06525 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec8b030e-a513-3ac2-a091-d8448a9eaba4 | -9.33483 | -48.1704 | 2026-09-11 04:08:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2ecf6ef-1ea3-35d0-b633-894071264e22 | -8.82145 | -46.91364 | 2026-09-11 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc370e25-8359-39ab-b2d1-2f163b2a0e7b | -5.47857 | -45.12916 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc4a0f8c-27c9-3dbf-a92c-c5e8a7a32633 | -9.53561 | -45.45456 | 2026-09-11 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94aeafdf-bf57-3f1c-86c1-cadc0ec61113 | -6.8671 | -43.06418 | 2026-09-11 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99a7c38c-10e9-3009-9e10-b116d18d7dec | -12.18499 | -47.17506 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dda8586d-737f-3b77-b7de-cf4c97fadbc7 | -12.18916 | -47.17588 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a69d04c-808f-3d5d-9a61-45fbfeaf5c29 | -11.34142 | -45.79635 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ff3d2b4-8404-369b-ad2b-05c7abf38fb8 | -8.28101 | -47.78799 | 2026-09-11 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98cff175-252f-3064-a3a4-cc6751d7f307 | -10.64455 | -46.09036 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7430adc4-6970-3a9f-a996-9045a609c9d1 | -9.69866 | -43.45621 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b2fd4950-ad5a-36dc-abb8-ca0da9b51878 | -6.75645 | -45.47071 | 2026-09-11 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a7c297d-9d65-3b9e-ac74-0e5c4af94c23 | -7.46554 | -42.12299 | 2026-09-11 04:08:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ff873848-17d0-3f78-857c-652b382a86ec | -9.70216 | -43.45681 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 404c2364-0231-39ec-abab-4ae251be57d0 | -7.02649 | -45.11223 | 2026-09-11 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0c846e7-754a-3171-9db1-3392e78df373 | -4.77455 | -46.50182 | 2026-09-11 04:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a3e5ba7-81fd-3b00-917a-8dee7893732d | -11.43765 | -45.1559 | 2026-09-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 410bd04d-e886-3147-89ad-22ddd2813574 | -11.35433 | -45.81397 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a533d17-8109-3dda-b0e6-ea587d748761 | -10.28241 | -45.30345 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 257eeef4-b6b3-37ae-bbce-8c29dd8e0f2e | -10.54538 | -51.35315 | 2026-09-11 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cfd22b6-488c-34c3-b59c-2e5768ada7e7 | -10.78287 | -45.94711 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 35a8263e-188a-39ac-9e01-bdba68ef7a89 | -9.74646 | -41.96833 | 2026-09-11 04:08:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| abbd9442-32cd-3bc4-8161-dbb24e6c7300 | -7.13445 | -44.56974 | 2026-09-11 04:08:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d16b7e5-4a1f-33b4-88cf-3f144495a576 | -5.47917 | -45.12541 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7fb99541-91fb-3310-a5ef-3247e1d33f7c | -7.35178 | -44.19703 | 2026-09-11 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a25aa46f-ffa0-36ac-95cb-4f6a33ae93c0 | -11.11002 | -47.55279 | 2026-09-11 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 519e42b5-713f-3048-824c-84f9468c6694 | -4.29582 | -49.10563 | 2026-09-11 04:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ac706662-3340-3f99-8642-0dfc5858f3c1 | -8.82573 | -46.91481 | 2026-09-11 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bac5d34-3da6-30fa-a3db-319609070eff | -10.85233 | -42.46202 | 2026-09-11 04:08:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2d84a949-a0cc-3d9b-be8f-5b63d994daef | -7.45533 | -42.12136 | 2026-09-11 04:08:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 08b54f99-be72-3469-9f45-dfeaaf2a5629 | -10.27589 | -45.27265 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48ae6842-5851-37b4-b219-26a97560967f | -10.64048 | -46.13658 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50eb7274-9392-392a-a92c-161b0f5fe56c | -8.48985 | -44.74718 | 2026-09-11 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3d7f9de-b41d-3765-b091-b03ac1b275aa | -10.07888 | -45.52575 | 2026-09-11 04:08:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd6c0f32-1287-30f8-9b83-0308f5ea77d4 | -5.47843 | -45.12829 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39b0c4af-5065-3b69-bb85-b1d16dbced9f | -5.32123 | -44.22715 | 2026-09-11 04:08:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a9a757e-a3a8-37e3-b3db-0514568a7070 | -6.02449 | -51.33459 | 2026-09-11 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15f3f2b1-3217-3622-b8f7-099758b3d03e | -4.77003 | -46.50109 | 2026-09-11 04:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ca2676d-f37c-31a4-82e7-911ae2a9897b | -6.23121 | -44.03091 | 2026-09-11 04:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fb8a4f7-966f-3aca-aba1-e2e2742c8e35 | -7.98881 | -45.56426 | 2026-09-11 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd1afc3b-0d19-3266-ace0-ef65e7075f43 | -9.63518 | -49.015 | 2026-09-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7fb203a1-0c94-3428-92ba-8aa0e42b98fa | -7.34429 | -44.19581 | 2026-09-11 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 233b20c9-f081-3dc6-bd52-ade19c58f67a | -8.7787 | -44.17879 | 2026-09-11 04:08:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ede857af-a1c1-3ab1-82ea-27957932174a | -10.98059 | -47.89044 | 2026-09-11 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7268394-cf68-3e83-baca-534e903c1e30 | -10.78591 | -45.95298 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6755eb92-9be4-35c4-b5fb-f5d697e547d1 | -6.73091 | -45.45101 | 2026-09-11 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31777f01-30b0-3f73-ac0a-2b5f22c19339 | -9.63024 | -49.01408 | 2026-09-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6f63e674-45ce-378e-a6f4-40b8f7eae903 | -10.42064 | -45.13092 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24a61d8e-d056-388f-8c8c-df476a0aff12 | -7.62017 | -44.72309 | 2026-09-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7e2c29d-f832-3523-ae50-1db0fb2c4c77 | -6.28699 | -41.71355 | 2026-09-11 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c9747c9d-0894-303c-88ed-7d058ba2d848 | -9.69669 | -43.40339 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c82561c6-4fee-34e9-b6de-f7a97f54f788 | -7.81235 | -42.77619 | 2026-09-11 04:08:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c9ab5cc3-040f-38bc-ad7d-c421bfb69b4e | -5.48313 | -45.12529 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 888442ce-b0d9-342e-b8c3-dbe59db90e55 | -8.3893 | -46.30153 | 2026-09-11 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07c3c03c-1cac-3bb5-a82a-f7538d0bfdf5 | -8.03155 | -43.84607 | 2026-09-11 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1ac6a68c-187c-34a0-874c-ebb2ff2e7d86 | -6.45134 | -48.03008 | 2026-09-11 04:08:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fd68f37-d231-39dd-a815-89a4c02bd626 | -10.97777 | -47.88066 | 2026-09-11 04:08:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f12b9073-40cc-33a0-a5ba-55fe53298d11 | -6.72742 | -45.44676 | 2026-09-11 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cfc6614-d5f3-3f34-8d5a-23835c8ff59c | -9.6848 | -43.47438 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7f3bb98-abae-3b46-b8b4-93e664b47049 | -10.0611 | -46.26981 | 2026-09-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 697ea9f2-c54d-3e50-bd2f-3488cb75560d | -5.38172 | -45.64201 | 2026-09-11 04:08:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad1ebb54-3222-3875-999e-f8a803205850 | -8.62909 | -47.42126 | 2026-09-11 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3a3ebdf-e0b8-393f-8a1e-1ba07624f29f | -9.78024 | -43.44188 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66733e31-01af-3d44-b60b-bff8d1196f7c | -9.7796 | -43.44581 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 437a2383-ce99-3ff0-b2a8-9ae3c23ec275 | -4.55799 | -47.76064 | 2026-09-11 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64f24cf1-57e7-3168-85b0-5c7cabd9b6c3 | -7.45873 | -42.1219 | 2026-09-11 04:08:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a4f1eb8c-4d1b-3f92-b111-2107f01cb2c7 | -6.73044 | -45.45108 | 2026-09-11 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
