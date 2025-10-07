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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83613107-5094-32bb-8666-8c3828e864cd | -7.51936 | -49.91027 | 2025-10-07 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df3660e2-6406-3c33-9cd5-9d0c62f600d2 | -6.71022 | -42.85453 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 41c52e53-1eda-3fc2-bfb4-1d5535d59403 | -5.22235 | -47.37429 | 2025-10-07 04:55:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 612192a7-9f56-3d57-a116-a15eaf35cb6a | -8.20502 | -44.18908 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5ac71fe-25b3-31ea-a641-ffbb48a9c635 | -3.08622 | -50.577 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 010eb2f2-fae0-3aa0-9fba-096583a14f5d | -3.1008 | -47.0127 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae3da1ac-3963-325d-b266-38dc077ad65c | -3.67869 | -55.57631 | 2025-10-07 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47d5ea1e-29ac-38ee-bd90-269727875665 | -4.87018 | -50.90226 | 2025-10-07 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b1850af-0a40-3c90-bacd-ab2996fe63b1 | -4.22112 | -56.08338 | 2025-10-07 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2aedffc-9481-34a7-b508-6d90288019a1 | -6.71718 | -42.84772 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9acbb513-468c-3eaf-b82d-44d238590426 | -7.03035 | -42.75422 | 2025-10-07 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c44d66c3-3bf8-3467-aa4c-18c35567d3e1 | -5.71463 | -44.83383 | 2025-10-07 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb5ec08f-6020-35e4-8cbe-89bfe87df574 | -7.75665 | -49.85622 | 2025-10-07 04:55:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fd26b43-1b31-35ef-b1d5-ee2ecc1c44a1 | -5.49953 | -43.06801 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 08d62b5d-0e31-3030-abfb-c1d29d2c7986 | -5.73667 | -49.13231 | 2025-10-07 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 86e5170a-e83d-3b18-9928-f6f9ba601478 | -7.2708 | -49.40643 | 2025-10-07 04:55:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d0cc5e7-7983-302a-96f0-91ddc69f4640 | -7.52124 | -49.90735 | 2025-10-07 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd46b45d-175e-3508-9eca-0d3a474ecf69 | -4.44747 | -43.22646 | 2025-10-07 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 5a319df7-e9c6-3cbe-847b-7b772117b7fc | -3.37322 | -52.18022 | 2025-10-07 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a73f7bb-d14d-3bd6-af45-229f4cab4f68 | -1.38808 | -49.04094 | 2025-10-07 04:55:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a3fbf75-a10d-3cf3-9705-643dfc54ca16 | -7.67116 | -50.20986 | 2025-10-07 04:55:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd0736f8-fb93-3c90-9f89-3a039920fffe | -6.71672 | -42.80426 | 2025-10-07 04:55:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02629712-5ac4-35ae-8978-5fcc1ca873e2 | -3.20178 | -51.01862 | 2025-10-07 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8367a29d-a75e-3df4-93d5-699e6f1329a0 | -2.14477 | -47.50773 | 2025-10-07 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0941861-a4d3-3d1b-89aa-af6633ace9fb | -5.7626 | -45.75256 | 2025-10-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2308f72-dea6-3f22-b572-a0fca684a2f2 | -2.8006 | -54.85791 | 2025-10-07 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e172be63-a40e-3ef9-8d01-32ea6eea9352 | -4.69059 | -45.8472 | 2025-10-07 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 462c64ba-52a4-38a4-aba7-c22354f997c3 | -5.03365 | -45.55985 | 2025-10-07 04:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c765dc35-d619-3610-b1da-e7517a65cdf4 | -5.8047 | -46.55637 | 2025-10-07 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19321682-324b-3ef9-a28b-b90fe0ea4cb6 | -6.71595 | -42.85691 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5f66d21c-dd27-38ed-9b57-db1daac3496d | -6.33322 | -44.02528 | 2025-10-07 04:55:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6875a69b-1a51-352a-966e-e73ac0d2e44d | -2.51936 | -51.92854 | 2025-10-07 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b0cc57f0-ecd4-3816-b817-ca92ce14b4dd | -6.85121 | -51.0645 | 2025-10-07 04:55:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f5ae69e-792e-35e7-b80f-3d47a1d0b2f1 | -3.09552 | -47.01788 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 46972fd0-73ef-3ab7-bf7f-bef4309740e8 | -6.72287 | -42.80518 | 2025-10-07 04:55:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 436dff22-4b94-3761-b98b-98364351f4bc | -3.50145 | -50.81783 | 2025-10-07 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 609c3d53-8e08-3a92-a209-c655ed0b3c04 | -8.1978 | -44.20752 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dd5b4d4-a216-3b6d-9e93-ec2898e16185 | -7.68786 | -42.41168 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 569a9dfc-b9fa-392b-89be-e2104704124a | -3.40929 | -52.72659 | 2025-10-07 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c50ec55-aba7-3694-ab7c-b66232ef0239 | -6.7178 | -42.84306 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c1f3435-b184-3d02-a3fd-026cfaf05136 | -8.19522 | -44.22765 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6b63886-2cc5-3fea-8080-4d25a525c4de | -3.46761 | -53.45599 | 2025-10-07 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72f2ad12-3071-3321-a49c-2c610ff4dd20 | -8.1757 | -43.34196 | 2025-10-07 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d6a4bcf0-5b7a-37e8-b3b2-6fa30cac128d | -3.09047 | -47.02145 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| f6cc1219-0750-31a9-8e4c-597d2388b4b3 | -3.14315 | -44.4239 | 2025-10-07 04:55:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c021f34b-2708-3ff1-878a-8c460d51207c | -3.23741 | -50.04755 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c50d2988-a783-3bdc-b86f-526a089d5d91 | -7.52397 | -49.90596 | 2025-10-07 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f2b67825-5dcf-3941-9597-c1f57bb6dba5 | -3.08931 | -50.5809 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f2b04c4-4a1b-3783-a6d4-1b2530e973d4 | -3.0918 | -47.01289 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83b46728-aee9-329c-9b84-1666e5d78b2f | -4.18514 | -55.69677 | 2025-10-07 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cda22bd7-37d8-37ca-b8b4-ae483391f264 | -6.73857 | -63.06251 | 2025-10-07 04:57:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df0bddf9-b315-331e-b5c5-83360ba25ef9 | -8.61984 | -54.96925 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87a11d8b-4d5c-3543-8183-add914cad26c | -9.34277 | -54.5216 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50382d6c-3979-34f1-933f-4ad1e4dae2d8 | -10.41275 | -45.39258 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64038dca-755d-3469-baea-9b8c6eaa8da0 | -14.92531 | -46.80444 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a077dd9e-add6-375b-af54-d5dbf1be816a | -10.74912 | -50.47361 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c4fa54d5-406a-3a68-961e-ee88b577ef76 | -9.76763 | -62.31992 | 2025-10-07 04:57:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be4c0573-c791-3711-9916-79fe21d021d9 | -14.9318 | -46.79467 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c328f1c-f7d3-3e0d-a596-f82bb3cd3be2 | -14.92619 | -46.79671 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| df29baf8-7659-3d5b-93ef-77c1d84a5cdf | -15.27299 | -46.34617 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c545536-05e0-30aa-9408-33d82aa10b5d | -10.4336 | -50.32959 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 20007ea2-70c2-34b6-91e7-7af7e62c3f0b | -9.02851 | -50.69937 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 222cd0c7-3cfb-3b0b-b4e4-423b68a11b91 | -12.89458 | -54.75592 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d338e9d-d6b1-3d2c-b9b1-0b9d26cdf258 | -11.65247 | -46.40758 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 168223db-269c-3c64-bfb3-150266dc0ea2 | -10.99251 | -51.21815 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 734409ac-df10-33a2-97fa-d91bedc41a5c | -9.62571 | -54.3195 | 2025-10-07 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d88753aa-ac18-33ef-8382-d5e0368bba52 | -6.70122 | -62.84262 | 2025-10-07 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c7ed913-f5e4-39ac-badd-fdad6cff548d | -13.27412 | -47.16698 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89193de6-97d7-39f0-8277-318c56b963a1 | -14.50175 | -46.92126 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 376c7ac8-62f7-3de6-aaf4-22db0101f3d5 | -12.89956 | -54.74577 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c6f3828-827f-3867-9fcf-71a2d305eace | -11.50612 | -51.4833 | 2025-10-07 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02c8119a-8155-327e-aebf-1b3618cc1954 | -11.25832 | -50.27459 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 770e583d-8eb3-36a6-b98f-62bb610dcde7 | -12.76515 | -50.48948 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55bd1eb8-2952-3f1f-9b7c-4c5daffa152e | -14.7713 | -46.04298 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81006ffd-ae9f-3520-abcc-22b3776c2b5a | -9.0254 | -50.69441 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49f1e984-221e-3c90-ab4c-7f47863f56c7 | -12.16717 | -50.91228 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 820c4c7c-61a5-3975-8d44-12a6c739bf7f | -10.40366 | -45.37709 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6693a30c-4561-3f06-9b3c-62dff3373cae | -14.91953 | -46.81672 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0740fed-8146-3a01-b0bc-1dd339458665 | -13.37101 | -47.24055 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfcfed2a-fef0-37a4-b956-ed49689cc4af | -13.10148 | -48.01132 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f688bb2-385b-3309-b303-619aa321f636 | -10.4247 | -50.30768 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 12b77e54-0c95-31c1-97e4-4cbd058e5833 | -12.93561 | -54.73325 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cd8c611-f123-3c6c-a80a-a5c78d15e350 | -13.67375 | -47.95299 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0768eb7e-1786-3b5d-9037-9ec1e1b2c8b4 | -13.09195 | -48.01007 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36e08bf2-9d66-37b0-b916-ac91c371554c | -11.1184 | -47.22083 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83f483e3-99a0-3269-a3c9-13a232f904c3 | -13.24795 | -47.17085 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ee9b05b-2283-3e6b-b872-d896538e3cb3 | -14.37161 | -52.74312 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 938e8385-2ceb-3b77-bdbf-37cfae03225e | -13.36469 | -47.25594 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f0c72da-2fe8-3f99-bdc6-bf19b56c7425 | -14.91797 | -46.86857 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d72b5342-1422-324f-92ae-d521c9581c61 | -10.42863 | -50.30825 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 88865e45-0bab-3543-89c7-854469bda1c5 | -12.9391 | -46.78841 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3883e4ff-9b25-3398-b707-9fa28a4f85ba | -15.21288 | -49.29588 | 2025-10-07 04:57:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aba9114a-6b7e-3f8c-81a6-a92f6b122a13 | -11.04905 | -50.91224 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8afff169-3f9f-32ac-abf2-2762c1a0d04b | -14.73973 | -46.02354 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6465ea42-78d3-3a29-9cf3-c2db74ddf77a | -10.43288 | -50.33463 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64262045-b43f-32c1-a32b-5b55a1bd7027 | -14.96744 | -49.95584 | 2025-10-07 04:57:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 329c4e71-cef7-3fb8-b5c7-336439cc0bce | -15.3713 | -47.31428 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9ca13cb-9854-3d9e-aa67-3b67722a439c | -11.78915 | -45.10387 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcc92bd2-36e9-3a2f-9b50-ccc6a9629e5e | -13.85722 | -43.99564 | 2025-10-07 04:57:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5135568d-3e85-3dc4-9e19-a005ac3bb337 | -9.75055 | -62.27313 | 2025-10-07 04:57:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README86.md)
