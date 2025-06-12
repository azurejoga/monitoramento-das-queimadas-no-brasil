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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85e662d3-0c29-374b-a548-93359662e767 | -11.83782 | -43.80242 | 2025-06-12 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13d176e9-de0a-3ec2-881a-a980a5d8ffb6 | -11.56749 | -51.30285 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 900068de-5e1b-3eb3-921e-d28df1619c44 | -10.93593 | -44.15139 | 2025-06-12 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24bdd7d9-d9a1-30c4-ad7f-ed587ec62751 | -8.31059 | -47.91988 | 2025-06-12 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d0424c5-4ddb-3987-9db2-44fb0495ca35 | -11.84546 | -43.79963 | 2025-06-12 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25aa0c26-9c10-3e1c-9650-eeceb3aaf315 | -11.57184 | -47.4338 | 2025-06-12 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 47c513f9-8cfa-3f0c-90f8-a13b54f141a3 | -10.65824 | -49.42493 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e0e63f62-58b5-3b00-938b-7bda0b1a2f69 | -9.76299 | -48.5795 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caed6eb4-a42c-3810-b22d-9783b7712577 | -8.52528 | -36.21058 | 2025-06-12 04:02:00 | NOAA-21 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 431ccb65-85bb-3a99-9041-5f1f47c6caa7 | -10.88081 | -54.7588 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7c29808f-633b-378f-8e43-b1fbc6514fa2 | -9.38596 | -48.42617 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7831bbe6-f8fc-30d6-9bc4-e93a7b41093c | -11.33267 | -45.45441 | 2025-06-12 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6355d93c-61a9-34eb-9608-b96d9953e92c | -11.96445 | -46.94717 | 2025-06-12 04:02:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 441e307b-59cb-3fe8-ac4d-413af1a6e5a5 | -11.1363 | -53.92374 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f267b6d-1fe9-3685-897a-d522b375b90d | -10.69758 | -49.52127 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5b5dcad-6185-3b1d-9536-be833722a0ba | -6.68619 | -43.96874 | 2025-06-12 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dc3c077-dbfe-3a95-8082-ecb8fff63fd2 | -9.85433 | -47.88342 | 2025-06-12 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d875c19e-37da-3185-99c4-c9bfbc020530 | -13.33042 | -40.30978 | 2025-06-12 04:02:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 42ae92c4-87e9-3428-9222-84a73d0ef713 | -10.86818 | -54.32559 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c15d74d-461b-3978-8c6c-057e354b575e | -10.70426 | -49.51318 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9eb21aa4-285f-3280-a72d-ccd3668fda4c | -6.68842 | -43.97094 | 2025-06-12 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf3d1071-ca25-33a7-8956-1ee9ee5f640f | -10.65974 | -49.36157 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0ca7b8c3-b87d-3872-80c8-ebdff43b46ec | -10.65475 | -49.36067 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cc8124b-f5d7-3287-a82f-79334550db4b | -10.87102 | -54.3208 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4a380e4-3fe9-3ad7-ac7c-37f3430fcce6 | -7.24381 | -43.10954 | 2025-06-12 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 13344c5a-cf13-39db-b080-444654513432 | -10.87524 | -54.75071 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b518a4a4-a86c-3a44-979b-fba203787eff | -9.60612 | -48.54416 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 027860fd-1af4-36fa-b797-b9930a5eff16 | -11.34222 | -45.21907 | 2025-06-12 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77890694-b696-3f49-b0a7-db9e714d9f55 | -7.3959 | -43.40194 | 2025-06-12 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42042b7a-abd7-3053-b3d2-f51540b5fa5f | -10.17551 | -49.35316 | 2025-06-12 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69916070-8bd5-3bb6-bcc4-a2e5221cacb7 | -11.62773 | -41.83722 | 2025-06-12 04:02:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9ad52f8b-82c0-3744-bb61-39855cf941bb | -10.88773 | -54.76021 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 46342180-90ec-3631-8724-c712241baee4 | -8.66145 | -47.13414 | 2025-06-12 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63cf25cd-55ed-3ad9-885b-a453025fc569 | -6.74303 | -44.99227 | 2025-06-12 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94058c26-be7b-3950-9d7d-6319a27fcb37 | -7.86423 | -47.88708 | 2025-06-12 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86e865db-0042-3b22-b574-5ea184bd216e | -11.83848 | -43.79847 | 2025-06-12 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7079fb97-9aa5-31f2-9981-54ac39df8291 | -10.89875 | -42.2426 | 2025-06-12 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e5078989-d8c0-3894-9447-665b4e7c7861 | -5.7801 | -43.61582 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfd714ff-95d7-341e-9337-6af337c0639c | -10.86975 | -54.32692 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43669931-24f1-37ca-95c5-cd792862b887 | -9.00556 | -48.73823 | 2025-06-12 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddf2ef7f-d41b-3b8b-84d1-d5af75313cc8 | -7.86288 | -47.88876 | 2025-06-12 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bd0b81d-76fd-3152-be9f-1925ddf7cf10 | -9.40068 | -48.42534 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0258c2b-2cd6-3583-a6a2-c6b78df81644 | -7.05243 | -43.5051 | 2025-06-12 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 763cae6c-1adb-3352-8464-d9b430cb2cf1 | -11.13812 | -53.9487 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6497e801-f8e1-391c-ab8a-fc405b98f129 | -8.88216 | -47.66473 | 2025-06-12 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a36801db-3de5-370d-ba58-2ca5985d54a5 | -8.96849 | -47.97551 | 2025-06-12 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04017d4f-2b58-3ff4-a3e7-ec376dd098cd | -10.69472 | -49.50843 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54a609f5-7355-3034-b449-e9ca11fc8788 | -10.70317 | -49.51918 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99733243-e595-3ac4-af3b-e547e39b2ddf | -13.03714 | -42.00713 | 2025-06-12 04:02:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 52a823e3-81d4-33ad-be2a-f3fb4e9207f2 | -13.60165 | -39.97559 | 2025-06-12 04:02:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3a4e0d85-c775-3171-a4e5-f4477f9bcf21 | -5.64775 | -43.60645 | 2025-06-12 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b97f08bd-afa3-303a-95f6-ae4b03de1568 | -13.03384 | -42.00658 | 2025-06-12 04:02:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 85b1aaa8-e474-3162-8e08-cbf0bc3fff62 | -10.70262 | -49.52218 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e442c339-7b4a-39ae-89e3-be051c19a1fa | -10.18053 | -49.35415 | 2025-06-12 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 863f599a-dbeb-3f85-8cab-ee7cad84d06c | -9.60477 | -49.0256 | 2025-06-12 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36036e39-f271-391c-92b8-2af153a03215 | -10.65431 | -49.41822 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2b61e58d-d7d7-3320-aa15-226fd5b55b4c | -11.84197 | -43.79905 | 2025-06-12 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e6640c4-5e67-3180-b0d6-9021c7a4a1e4 | -8.95135 | -47.28009 | 2025-06-12 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bb8ff17-b49a-3de8-b7be-e636fab39cc5 | -12.76934 | -44.40054 | 2025-06-12 04:02:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f372112-a253-38f7-bb6b-21a99466af36 | -11.57895 | -47.44382 | 2025-06-12 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3528d7c-c053-3c4c-a7af-816966bce424 | -10.23428 | -52.23428 | 2025-06-12 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cc8352b-de7b-3669-b695-70eb198554e4 | -13.0443 | -42.00467 | 2025-06-12 04:02:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d938cb6a-79c0-3e74-b5dc-8d0b9a0cb47a | -13.33097 | -40.30614 | 2025-06-12 04:02:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 30e8869f-25f5-3b0d-813d-551c12bb12c3 | -10.6553 | -49.35774 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ab1c99c-92e8-3979-a3a9-3a4bdd2c7424 | -10.69542 | -37.04752 | 2025-06-12 04:02:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 054a8fd6-edf3-3ecb-a640-a4877d67922c | -11.33847 | -45.21835 | 2025-06-12 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 607d350e-5cec-3070-8200-a4356149ef5d | -6.45809 | -44.45398 | 2025-06-12 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d5c664a-1ef1-353a-adbb-fb30b26f5eb6 | -9.05464 | -40.66881 | 2025-06-12 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 97f2a021-4723-3e8f-b3a4-3328f9682df2 | -12.76797 | -44.40874 | 2025-06-12 04:02:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f20491dc-4889-3825-b2a2-f306e933523d | -9.39076 | -48.42701 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a7b91a3-0ae6-3203-91b6-e08445879150 | -8.96381 | -47.97466 | 2025-06-12 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad23ef0b-03b6-3ef8-ba2d-018a92af3111 | -12.22694 | -44.21114 | 2025-06-12 04:02:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4403938-f8de-3d0f-bb2b-4c72941bc503 | -11.57214 | -51.30142 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b727a8af-1734-397d-8410-021bd7fa27bd | -11.7756 | -47.31573 | 2025-06-12 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4cf9926-f2c6-3c2e-9b76-0190320d054f | -8.59054 | -47.09451 | 2025-06-12 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4116c355-1800-328a-9d59-062f2b3b7734 | -9.40993 | -48.43036 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9314437f-d8bc-3b90-b8d6-a0651d696f2c | -11.96517 | -46.94316 | 2025-06-12 04:02:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 608b1a01-25f3-3786-8d25-cd49c5328685 | -8.07528 | -34.97651 | 2025-06-12 04:02:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 848d3c71-d241-33d8-acad-5f9328e1bca8 | -13.04044 | -42.00766 | 2025-06-12 04:02:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 56efdc8b-6f02-3dbd-8906-41a5f2d64374 | -11.61194 | -46.99297 | 2025-06-12 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6829c57-9428-381e-a1cf-2de6dbdbcde0 | -10.23337 | -52.23891 | 2025-06-12 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0cbd24a-98c2-3b9c-90f4-a8a47f09498f | -13.04156 | -42.0006 | 2025-06-12 04:02:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 1f11342a-bf37-385d-bafd-90945cf755ff | -12.38747 | -45.77067 | 2025-06-12 04:02:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfc1f41e-0626-3d1a-8b6d-87c07c6c078d | -10.86426 | -54.31945 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d498702a-04c5-3792-8470-8d8d172ee279 | -7.22835 | -44.79299 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42b5d890-f567-3819-93fe-9d569e66b755 | -11.5651 | -51.30776 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48b84a98-9f3c-3abd-969b-621bd57575ba | -10.88076 | -54.75558 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 74aa70aa-13bd-36a2-91a1-c6889841476c | -9.27666 | -48.26376 | 2025-06-12 04:02:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31e9c540-f137-3c5c-bc10-92d40e971710 | -8.96472 | -47.96962 | 2025-06-12 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5dede1e7-dfe6-35d3-98a7-8b899b898175 | -10.69788 | -37.04992 | 2025-06-12 04:02:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5a294abe-e591-396b-95e0-ffb4f0c0b51e | -6.74696 | -44.18557 | 2025-06-12 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cee0b7f5-934f-3283-909d-5840ec5f9f63 | -9.86953 | -42.44593 | 2025-06-12 04:02:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1fab0da3-1a66-30fd-b365-f4e56a3c48db | -11.13564 | -53.95013 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39926e8c-514c-3f00-b6ca-808f48d23fca | -10.69812 | -49.51828 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c666b46d-da33-30e6-b96b-b519bb55f6a0 | -12.37895 | -45.77422 | 2025-06-12 04:02:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6cf7909-3b5f-3ae8-bbbb-e2cd0b907e78 | -11.56586 | -51.30397 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9cae1c4-7398-3dfa-9bd8-eda76422c6f4 | -6.68929 | -43.68377 | 2025-06-12 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14fa3734-15de-38fd-8cb0-67f48c7074ea | -10.99301 | -50.75745 | 2025-06-12 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92fef3a0-814e-3b52-b85e-faf749b10156 | -8.11193 | -45.33644 | 2025-06-12 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f75fe14-c841-3040-83dc-21a2fe6b52d8 | -10.6455 | -49.43756 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README8.md)
