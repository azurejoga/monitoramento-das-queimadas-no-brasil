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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 276d815b-01c9-3ed0-b432-d583f39acc0d | -9.20877 | -46.89741 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df7dbd61-33ac-342d-a51f-1f057305208b | -7.80147 | -44.21385 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70e04a6d-6c57-3c62-9679-cb18fc9a9d2a | -7.35152 | -43.87051 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d862464-607f-300c-b9b9-44a421fc8dba | -10.9205 | -51.01939 | 2025-10-08 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20686d79-6a76-3e32-89cb-eefcc3f70426 | -8.39846 | -49.72319 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96d24b3a-715a-3e6f-93ac-9068b6ecc258 | -8.91981 | -46.57972 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89154832-3174-3583-bcab-0d17d20d1568 | -9.18541 | -47.81973 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af1bbbb8-d622-3bd2-9c5a-eb230e2a76f2 | -5.50037 | -39.70348 | 2025-10-08 04:38:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 428c04ef-15e2-33a7-8575-d2306c4c9863 | -9.7873 | -47.74384 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f8edd09-4c51-32c8-a344-12e4476ec218 | -5.96707 | -44.83062 | 2025-10-08 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce5100df-3f24-359a-931a-91ddb6dccbf2 | -4.0203 | -48.96518 | 2025-10-08 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbd69c0d-8f7a-354f-91a3-c79bc0f18846 | -7.79845 | -44.20575 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69da3e02-52c2-3b45-b56e-209f2decc33a | -4.1354 | -47.65203 | 2025-10-08 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f386aa81-93d6-3c91-ae3d-862af8cd3b74 | -6.08957 | -46.23588 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5dcd6b27-a4d8-3e83-999d-4d59d0cbe78c | -10.68252 | -47.55075 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45f060a7-35c4-3c12-9e09-53c460a2ae4e | -8.47532 | -46.27991 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b99fa943-b5af-3af0-bf36-9b1d8d9bb118 | -9.78012 | -48.28089 | 2025-10-08 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6edf7c89-0751-302d-b8a1-163348f4f80f | -7.80645 | -44.18005 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b7eeaf9-3eda-3672-9201-f2361f794226 | -6.30634 | -49.13879 | 2025-10-08 04:38:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d53067c-7aaf-33b2-b8b9-66ae69de6470 | -5.17509 | -45.13038 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cde02d13-bdd4-39e4-b651-103ef2f63af1 | -8.41201 | -46.8105 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffe6fcc2-2dc5-3623-a544-2a6798a3afc7 | -6.28701 | -45.32478 | 2025-10-08 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 054b3035-13f2-3921-adee-d46065bce3fe | -4.40322 | -49.765 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c6db7166-95b2-353d-b415-6425464eba78 | -10.58 | -51.5757 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 792f044d-5719-37d3-8d11-5239fd2d4482 | -7.24554 | -48.47679 | 2025-10-08 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 73e6f9f3-9f51-3a3c-a74c-d2d2a90f39f3 | -11.00057 | -50.90223 | 2025-10-08 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b56e01a7-9b34-3f31-b2bf-ab4d6aca1d3e | -8.41776 | -49.72982 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17af8239-258a-3dfe-bff9-2324018806d4 | -11.85309 | -44.91852 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fbe8f92-99b5-32a6-976b-2622420f22fa | -9.68309 | -45.66239 | 2025-10-08 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52c90cf8-ec63-33e7-80cb-4d88f65c61f1 | -5.0502 | -45.18731 | 2025-10-08 04:38:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89afd81f-f4df-3574-8a35-04f054798327 | -4.95079 | -45.59157 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e97f706c-6822-3a75-92cf-59c8c8153b5c | -9.89516 | -52.22892 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81487560-f314-3ed5-bce0-33f317a1307c | -7.47824 | -43.07129 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d808e532-c6e7-3f3a-be83-42693f727bad | -7.77491 | -44.19375 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15f5f17b-7c35-354c-9586-b0e6848f305a | -11.78961 | -45.1376 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 330c65b8-f21b-3c0d-b68e-75ee8c169089 | -8.11865 | -44.77225 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6434060-aaf3-3599-bf29-f8cf3fd06ab1 | -7.44633 | -43.13758 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0f3426cc-eb39-367e-a945-cd16c60ce739 | -8.46134 | -47.20969 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fdae3dd-85c9-37bb-98ed-bb635cd9ec61 | -3.77598 | -50.76794 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9e0850a-e0fc-3752-8041-68bd5450e606 | -10.50242 | -49.14224 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c918755-c4e5-3304-994d-59e55939fa05 | -7.52777 | -42.71986 | 2025-10-08 04:38:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8e6d2394-c344-3d6e-91e1-94982bd35923 | -11.78548 | -45.14458 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1efa8c72-ae03-31bb-b680-7e382673f7d8 | -5.26555 | -49.51201 | 2025-10-08 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06aaf81f-fb84-3427-b6bb-d431d1eeacff | -5.1684 | -46.22848 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f611d06-421e-344b-a2c4-02718d656e87 | -8.77996 | -48.00101 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75c04ec6-34b1-3479-82eb-b2f3b83cbe75 | -6.75803 | -43.76409 | 2025-10-08 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb89e584-9b59-35cf-84c1-c03375506687 | -9.03909 | -50.63072 | 2025-10-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbdee0d7-b306-380b-9a13-1d00650cf1bd | -9.67997 | -49.93186 | 2025-10-08 04:38:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31ea566d-a5d8-399f-acde-cfd4666b140d | -9.13688 | -50.05912 | 2025-10-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 100b1e08-6b12-3770-9bdb-eb32a3136909 | -10.48341 | -50.30761 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62197d3b-6d5f-3b6e-81e7-c39f98ed5061 | -10.64852 | -47.79881 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf647d9a-3d66-3329-8113-c2a4b13335a2 | -5.69596 | -53.64008 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afaf6232-596d-377e-90d1-1839812beddf | -3.46039 | -50.09219 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2871adb9-2f2f-3156-9fb2-4fd002401904 | -7.13729 | -45.93233 | 2025-10-08 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c402c4f8-fc09-3776-8ea8-aefc14d8f6ef | -10.85588 | -47.11918 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53f585ea-cd91-3b6a-8620-1aa8773d63e9 | -9.68032 | -45.68185 | 2025-10-08 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c694d76-e8af-3d6f-98b9-42a9e5778c9d | -9.19747 | -47.81 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e617be2-4bdd-382e-a4b9-5c983aa8c232 | -10.85656 | -51.01589 | 2025-10-08 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c943f87f-dd25-3047-9823-8885aa78f3a6 | -4.91606 | -48.54131 | 2025-10-08 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da65041a-4ee6-3965-b00f-7826c5ea99d4 | -8.11762 | -47.25278 | 2025-10-08 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b64cf47d-2e08-3ad0-89e6-b0c2026c9db1 | -9.79134 | -47.74057 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c26aa71-f69b-3b40-9687-5892b8a8a81e | -7.67901 | -42.40847 | 2025-10-08 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5b534e1a-a6bf-30ea-9dbb-7cd32e11fc12 | -5.13901 | -44.96084 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 25b8804a-24db-3b05-90ba-47816f8f5da3 | -8.47744 | -46.31552 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3f3b8836-bb62-3604-a26f-3955705d92b0 | -8.02923 | -55.12844 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79ca0130-4543-34cf-94f5-3391a0529469 | -11.78521 | -45.05744 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbd63633-d036-3c9e-b2e2-c22d0ee58db6 | -8.89172 | -46.03591 | 2025-10-08 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80bfaf3f-0dbf-34f8-bf48-61ee6d18790d | -8.37511 | -47.05994 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e025f32-c74f-324a-b9fb-a026deaa259d | -7.77195 | -49.23637 | 2025-10-08 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc98b1a4-2fc6-3625-b6d9-f305912c45d3 | -9.39343 | -45.93404 | 2025-10-08 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c12769ae-9399-385c-8f28-fb06cd9eaa8b | -10.73177 | -47.6562 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f0fa56e8-29d8-30a7-b41f-a742a218e11e | -8.25133 | -50.09495 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3192e739-5bd9-3073-a8fc-4493a837decc | -3.79073 | -49.42851 | 2025-10-08 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bce16217-d630-3f9f-b730-bf772cd35035 | -7.78802 | -44.21943 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab19d8cd-bb2f-3f10-904d-e0c8cd5fb514 | -5.48629 | -44.6208 | 2025-10-08 04:38:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce117bae-f380-338d-b92d-a75c8f6b13d3 | -4.49844 | -46.35334 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44078e62-de44-3df2-a5a7-6c1f8115d020 | -8.22966 | -44.18137 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4a91a6d-ea51-3c60-a922-220d06eebad5 | -5.86856 | -42.77711 | 2025-10-08 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0edb60f9-7f2a-3896-b04a-81a371af00a3 | -10.10362 | -54.23486 | 2025-10-08 04:38:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fb9d958-1e8a-34ea-9a2b-772e21587814 | -8.64415 | -47.16813 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d721ca05-b67a-3157-a832-f1d8407a25d0 | -7.35734 | -43.85977 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7f1c3bb-0428-3308-9098-7b1270004f37 | -6.69044 | -58.81673 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36a69eb8-f88c-37d4-8767-19670675ba56 | -8.59913 | -44.90366 | 2025-10-08 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9932f093-05c3-3539-b57f-9ca88b41ab30 | -6.42026 | -47.2445 | 2025-10-08 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06425414-71a6-36fd-a4fb-ff0fbd11662a | -10.93103 | -51.01749 | 2025-10-08 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bea84339-a1af-3e2b-b9f0-54be7153b1d9 | -10.81602 | -48.80702 | 2025-10-08 04:38:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37daf943-b168-368d-bb1f-1fca71cbf790 | -8.6049 | -48.24893 | 2025-10-08 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 243f5413-1b8f-3b42-9481-c91aa9333aef | -8.67455 | -43.90922 | 2025-10-08 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04a375ac-0f14-359c-94a9-5cb51a9da8e4 | -8.3757 | -47.05598 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73707a2d-f10e-3d84-bc8f-43968c33bcca | -11.85613 | -44.92743 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 245c9d57-f6b4-3bc9-be21-5529494cfe11 | -8.54201 | -46.23081 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d456057b-b486-3672-a46a-dbb89f236a51 | -5.72093 | -43.61856 | 2025-10-08 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 49059973-97ad-3c31-8ec6-79ba6bc9bf31 | -10.37296 | -48.13625 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42140124-1066-38ef-aefe-f8bc7659ed9d | -3.79017 | -49.43199 | 2025-10-08 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6f449a07-dec6-3df3-ad72-f9fcfeae2170 | -7.80587 | -44.24108 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca43f8e3-e4b2-3bc9-9555-ce7cd3244e07 | -9.18599 | -47.79272 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b482442-1d40-3b5c-af59-ad27535c9375 | -5.88728 | -45.5562 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 421352ea-06a5-3f01-8c29-5b334328d127 | -4.8545 | -45.75575 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8c5434f-8dc6-37f2-b91d-f3ebbe2036c3 | -4.25352 | -48.56422 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a705b584-b64e-31f5-aaa3-f095e0b7a2e7 | -11.32949 | -49.03072 | 2025-10-08 04:38:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README70.md)
