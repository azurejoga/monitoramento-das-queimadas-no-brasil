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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b251153-a1b3-3ce0-9fc2-1396fbb59fc8 | -5.88825 | -43.2021 | 2025-09-25 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4073fe53-f195-3745-823f-13d5eb7023d7 | -2.52445 | -47.25216 | 2025-09-25 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c2bc5ad-65ec-3dbe-b0ca-71d83966929f | -6.57684 | -43.65646 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7533ad8-ce2b-3a62-8ee0-3b99b6de58b6 | -5.51725 | -42.51117 | 2025-09-25 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a1bcde69-9bb2-38fa-b602-7adb434809e3 | -5.51224 | -43.86783 | 2025-09-25 04:32:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7c28af0-9b96-366b-a570-5fd29e786382 | -1.08767 | -54.10789 | 2025-09-25 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 612b0dde-5e8b-36d2-94da-2cbddc65c78d | -3.83126 | -50.96849 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b393c044-65d6-34c9-88ff-63f22d7e58da | -4.67618 | -48.1592 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe7a8269-5a44-3282-8902-0c7af017c446 | -3.12951 | -46.6269 | 2025-09-25 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42c1f663-12b1-3c8e-bbe4-2dd1d125b97e | -7.26194 | -43.02236 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e768ef47-530a-3c79-af89-858824ba076e | -1.60912 | -54.31992 | 2025-09-25 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83b24fea-c0d1-3870-9bd4-15494c9f624d | -3.61248 | -38.76517 | 2025-09-25 04:32:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee4f8c8f-a04d-3c36-b83a-7323405bfa22 | -2.69011 | -48.47122 | 2025-09-25 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 347c5103-7c22-3ce6-858d-62b65011a764 | -6.12011 | -44.00255 | 2025-09-25 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7433c8b8-9e01-332b-8d6f-9500221b9813 | -6.42424 | -43.07937 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 516a477f-97a6-317b-8436-0d11fb1363db | -7.10217 | -44.09196 | 2025-09-25 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 425c7624-7197-3865-9abd-03a2a1ba1db0 | -7.1522 | -43.53108 | 2025-09-25 04:32:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e72ce1ea-c68e-387a-afe9-38119a67a1bc | -7.25373 | -46.05782 | 2025-09-25 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65072bff-93e2-3d41-a5f9-24dd0ca5207e | -3.61449 | -51.8005 | 2025-09-25 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c29508f-c4b3-34d5-9527-fee7cfe3ff8b | -8.67463 | -44.03655 | 2025-09-25 04:34:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b2a6ce8-748c-386d-8f94-137cb0db8eb3 | -12.06815 | -44.84951 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 940cce38-4135-3546-be6e-a07b008e8714 | -12.85066 | -44.69237 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa1acd75-d1b3-3d3a-b4b1-72a1ff4ac9d6 | -11.43286 | -44.94415 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7b89fc2-4b0e-37bd-9631-17259b580cf6 | -12.86456 | -44.67871 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd8fa3e6-8ebb-3975-8a6f-f632df955878 | -11.6463 | -44.42587 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb415e96-deb0-3833-b21d-a83cdb88f7ce | -11.65591 | -44.44285 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a99c5953-ad59-3997-80ce-2bfea5b6057a | -8.84096 | -42.99672 | 2025-09-25 04:34:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 79d9bccd-3926-3d13-8e01-3aa8616862b2 | -9.58477 | -45.45095 | 2025-09-25 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d18ba67-35bd-3e66-b7e4-74f5f1e11ca4 | -13.84337 | -45.61717 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 243815ba-7bfd-375a-bcd9-11829c239446 | -11.68997 | -44.39811 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 716bff0c-442b-379a-82a6-1f8b6039dfd2 | -11.11258 | -44.88514 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abb64ca0-76a8-3588-a630-c0b66f8ee685 | -12.89523 | -48.88862 | 2025-09-25 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b678c1ac-f857-3a49-b762-945c48588b28 | -11.48011 | -43.52664 | 2025-09-25 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 203a5b93-7405-3a0e-97bd-492ebbf9f18c | -8.67643 | -43.99734 | 2025-09-25 04:34:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45f03f98-7d38-3fa6-a3e0-7ade7d4734c4 | -10.83136 | -44.82296 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0254e0e5-e26e-323e-af45-6d08c0eace49 | -7.76984 | -46.19216 | 2025-09-25 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0502a9c2-59ef-33bf-8736-2ecb5fad6365 | -11.9835 | -46.63307 | 2025-09-25 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8dfcd962-26e4-3efc-9920-d4968c865fc1 | -12.07453 | -44.86019 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b5ffac48-814d-363e-95d7-3cd24e20947b | -8.27158 | -44.81136 | 2025-09-25 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c8fbe75-6437-347c-9e23-477d308a23e6 | -12.05933 | -44.82795 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8dce14a-6a3f-310d-a365-e92e81ae450c | -12.85295 | -45.29184 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ebe89ebe-e643-36c3-859d-9ffdf63c5d3b | -11.40287 | -44.9645 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 30a96420-699c-397c-91ba-0c863605f12a | -10.09452 | -46.32097 | 2025-09-25 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0854940d-e453-3a9b-83d7-bb2cacdb237f | -7.77726 | -46.18953 | 2025-09-25 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79a1aa6a-56ab-3f83-9855-0d7c0c544487 | -9.68347 | -42.64629 | 2025-09-25 04:34:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bc777cba-9cd3-3d69-a19b-219b33accf2b | -10.84175 | -44.83107 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1041ba6c-fdfd-30a0-ad3b-84a7292369d8 | -10.40044 | -46.18017 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8845aaf4-47a8-34ba-92ed-89dfb840fa5f | -11.64496 | -45.34882 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8935027-4dae-3620-aef1-d7760e19c274 | -13.84648 | -45.62243 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83d7bb37-cde7-39db-a3cd-95042978436f | -10.84204 | -44.82946 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6af270b-f8a0-3ce8-bdad-f996bc2ba8e7 | -13.83829 | -45.62604 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e0bc922-807f-31b3-8a0e-00f659cb7ff8 | -11.64058 | -45.35278 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8d23df2-15c0-3a97-926b-05ea8ee1f699 | -12.30912 | -44.21021 | 2025-09-25 04:34:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f280977e-4226-3f6d-a47a-a9aab47bd0c7 | -11.67675 | -44.40663 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1da2a632-7508-389d-9c13-4410ac229969 | -12.02769 | -46.58269 | 2025-09-25 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfb1b93a-0a8b-3ac8-8ac1-9220e01b1202 | -11.68673 | -44.3924 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0f0243f-e4d7-3601-98fc-7c812ba62422 | -10.3987 | -46.16768 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87e491e0-7fb0-3bfd-9cb0-98cc8e76ad9f | -11.01719 | -44.34106 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afb2a291-b327-34a4-81b4-d4447d2cc013 | -10.55628 | -46.2791 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f0fa962-af0c-3f19-af05-ca09bfca48c5 | -11.4297 | -44.93906 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0426bd0a-ceb7-3d9c-acb5-7e5766185556 | -11.63863 | -45.35448 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc593270-56d7-3f8b-9ef9-60e3be188fa4 | -13.83208 | -45.61554 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6e502ad-93c1-3e7a-bd61-eefc13c7ae78 | -12.10428 | -45.78777 | 2025-09-25 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdc02efb-0263-33c1-9ba1-2bcab7ee89a9 | -11.67605 | -44.41175 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2190524a-35a3-3e74-a5a3-c20275424343 | -10.10977 | -45.30981 | 2025-09-25 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46c15f85-4295-3b20-a97b-9481e81c70ad | -11.69391 | -44.39869 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c36e644-20dc-31f2-a794-cb9e89f528e1 | -11.91309 | -44.77694 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd622e43-596d-323a-9c5c-e0cf59478701 | -12.05616 | -44.82245 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f8d2c1d-e305-339f-b56c-719d67befd2c | -8.4866 | -45.00351 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 248c2b99-cacd-3986-bdd1-403f6acf5c27 | -9.44234 | -45.58483 | 2025-09-25 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4681f87d-8206-3d41-9742-f1a7a6bc1419 | -11.11637 | -44.88573 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a196421d-361e-39fd-a552-43b2508d7510 | -11.69123 | -44.32998 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44010098-2f3b-34eb-a01d-abc29f96841e | -11.61987 | -44.44276 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c986dafb-9fa3-3d21-afef-c4f273108edb | -12.54281 | -45.80623 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb72df8a-9a56-3afa-b26a-528c0f4c52d7 | -11.67427 | -44.39868 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f22be6e-8aca-3de5-91bd-136210bb8aff | -11.92795 | -38.32963 | 2025-09-25 04:34:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cdc3cb6f-dba4-3fba-a8fe-fedeb0e9c2ca | -11.79331 | -45.58583 | 2025-09-25 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43eecf6f-bd8b-32e4-a42d-c0949ca740c5 | -11.40737 | -44.96004 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5e5551f-7dc1-39b8-99ef-01de89719140 | -11.90854 | -44.78127 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c744476f-8a40-3406-b30e-b19ade4a629d | -12.10063 | -45.78725 | 2025-09-25 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63b5e097-de28-3ee7-9c91-5b83dce971f8 | -12.41496 | -44.7454 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cca3e39-ca69-308e-8f66-2c7f624da298 | -11.64847 | -44.41056 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cd74f7b-d037-3b07-94b4-276335719040 | -10.76639 | -45.39767 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3547208e-855f-3e14-9d02-2250f5891c7f | -12.05549 | -44.82732 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad31ee5a-d9eb-3b00-8503-e5f3dfb26ef9 | -11.61447 | -44.33746 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8fab8c6c-fa63-38cf-853a-de7673e03e8f | -8.49819 | -45.00076 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b07c429e-d270-3599-a419-a2d7718065fb | -8.84847 | -42.4739 | 2025-09-25 04:34:00 | NOAA-21 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 05a3722b-0cdb-374c-9425-71ebfa526255 | -9.43817 | -45.58832 | 2025-09-25 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1edbfe61-e8c8-33f1-8a88-1f036a07044a | -10.39578 | -46.16313 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33305890-511c-3845-9866-872050d2b261 | -10.59104 | -44.06733 | 2025-09-25 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 78d0aa3e-7daa-36ea-af92-08247488eeab | -8.12924 | -44.13845 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f0ac7f0-5a9c-35c1-ad51-8e5a9f4b911d | -11.78483 | -45.56644 | 2025-09-25 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79a43ead-ce47-3cd1-8924-99e88de05065 | -7.99462 | -45.73072 | 2025-09-25 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1471ad05-4c3a-3633-8ea9-7de75cbc93c4 | -11.60346 | -44.4455 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d48c45f9-a842-38a4-9ce2-e968075483e3 | -11.62129 | -44.31739 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01105bbb-15bb-3a12-b40f-b59fdb208220 | -10.17224 | -44.85785 | 2025-09-25 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4c14393-dcea-3a83-8023-f187a5610ece | -11.67281 | -44.40605 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 560f8611-c7a0-3f7c-aa2f-6d06ba497f59 | -8.48294 | -45.00302 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 30f85c64-5f31-3dfc-80f7-3f0300b5a977 | -8.49695 | -45.00916 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8792801e-1989-3f77-bdb1-e6fdaf0f98c7 | -12.54473 | -45.79303 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README21.md)
