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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b73ef6a-ea86-33eb-9db8-9b0d6d7d1a89 | -11.40747 | -43.40849 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2f788eb-0e0a-3087-9417-f58f033e7c23 | -8.59171 | -49.83763 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8de64eb1-e08e-3e87-9ea5-3b080612b48f | -6.36307 | -55.14555 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a219ca0b-3c7c-3c5e-8177-50e5f2904b44 | -9.30763 | -57.71237 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 50adc89f-003c-30e9-8ba1-99ba62ebcdd4 | -12.77386 | -54.01859 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc030f49-ec0e-3593-a143-d8e3fc6df641 | -11.75023 | -50.40189 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2571cbeb-2b9b-382a-934f-a82703c6fe12 | -10.85139 | -48.68542 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 937cdec4-e918-32d3-8685-af1a6de06d1a | -13.06378 | -51.19512 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60de2477-18fd-379f-ac5c-b0eba1f68a5e | -8.38629 | -46.28913 | 2026-10-01 04:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e9c17dc-cab3-3b93-9f44-3ba5d400081c | -8.30323 | -54.71795 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b05a0afb-35ed-310d-926a-94b7e9e714b0 | -11.18838 | -45.11573 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e901c40d-f0da-3979-8d72-78ad55c9aee9 | -13.86599 | -44.44229 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d32fa4f-d664-3336-a271-3a880db4d9ab | -6.44296 | -51.71041 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 446ae435-6f51-3679-97b7-d873f64747c1 | -11.84018 | -50.95248 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce0df47f-b72c-3a77-90a6-acb058790afe | -13.54395 | -49.16592 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 413db63d-fd3f-3377-be04-b465e3deeb7d | -7.46611 | -45.78844 | 2026-10-01 04:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c6a8795-ae04-39b9-ad77-a97ff5baf606 | -7.48889 | -45.79569 | 2026-10-01 04:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 595f3cf8-f877-3aac-b009-19a51c5e98b8 | -7.82098 | -45.82225 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33273e12-9aa1-3461-8fdd-8d079667134b | -8.21394 | -45.47815 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16a4e58c-21ec-3212-a2fa-0c4f7f757680 | -10.77934 | -50.52655 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 89874146-3445-382e-b137-de13798dea09 | -7.18787 | -46.50143 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6486fed-c08a-3488-9c8c-dfd264b3b6fd | -7.67249 | -49.07658 | 2026-10-01 04:34:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c26e42d-75bd-3971-bc40-587944e9be20 | -8.84708 | -44.39114 | 2026-10-01 04:34:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 452df641-de2e-3ec7-b381-cdfa6ef4a3bc | -11.11414 | -44.59199 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d9bf827-3937-3575-aee6-16c610761fe0 | -11.41145 | -47.45761 | 2026-10-01 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca07301b-048a-3b33-9c5a-370b1d135302 | -9.14467 | -46.75681 | 2026-10-01 04:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54e0d489-9764-3a73-aba5-396688043d65 | -13.902 | -43.75008 | 2026-10-01 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3defba46-4985-3fb9-96be-e28592d4d757 | -9.08525 | -45.00649 | 2026-10-01 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| ed5f0290-205e-3760-aec4-cb5f0c1094e6 | -6.0305 | -53.3654 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c86b1fa-e1ec-30df-9dc5-779fc7d0065b | -10.90874 | -43.84695 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09b740da-6892-3d43-9788-31cece193d2f | -10.54567 | -50.01371 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d919e88c-5844-3557-b62f-7100a596e620 | -9.06574 | -44.99591 | 2026-10-01 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e71e0fa9-6ebe-3407-b123-cb6d79c28e68 | -6.36415 | -55.13946 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e447824-d546-3c00-a29d-120f0775b660 | -11.17675 | -45.12193 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0961b91b-f771-36d1-9ab9-d5c3d4d60e43 | -12.24934 | -50.30055 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b93318c-e85a-355f-8764-eb0bb6f27471 | -7.60264 | -55.70235 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dda4d5fa-8eed-3427-9952-6e88b6ca12bc | -8.21338 | -45.48177 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 776ffbec-3ed6-3724-b738-3f37f8931fd2 | -9.54517 | -56.16191 | 2026-10-01 04:34:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac538f29-c7e2-357f-8626-e2a29f8b53c0 | -11.41129 | -43.40905 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4894b226-c344-32de-907b-06bcfe0d2e5f | -7.57291 | -46.62297 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96d14638-2444-3e2b-984b-abf799ec5124 | -8.8465 | -49.70032 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1eeb0987-0a8b-3cfd-902e-bc71ec17609e | -11.83763 | -50.50778 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0e4a28b-2169-3755-aba7-dba8f79342ce | -8.84936 | -49.7049 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63c77cb7-3dc3-37da-8240-dc088d7705d6 | -13.86163 | -44.44627 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4acbb81b-8fc2-3b40-a17f-eac0929fa830 | -11.79049 | -50.50879 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 28592507-a3e0-3222-8eda-9e7959126887 | -12.64657 | -47.63656 | 2026-10-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16cf76fc-f1d5-3e8a-a4ff-5629eb0d45fc | -9.15224 | -45.5964 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e135b1b3-63f2-3fdf-9aab-5efe395ce178 | -10.5359 | -57.77843 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b17ce9c1-7c4a-3e73-97e5-0b3cd9c49d3c | -12.18647 | -48.43649 | 2026-10-01 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 867dd153-b456-3464-bc83-7b3eb509f778 | -6.4331 | -55.80789 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab710a85-c38e-32cc-bc16-4560a0abb4e1 | -10.85474 | -48.68604 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 915b8c44-e08f-3fb0-bb89-4047e25d7368 | -13.38137 | -46.81269 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0694d2fc-94ba-399d-b2b5-3f9826691e78 | -6.75077 | -55.08411 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 568f5d8d-9380-34a0-8dd1-f372f9298949 | -10.7565 | -51.66817 | 2026-10-01 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86a2fbee-7372-38e7-a4f6-9dc23922ef6a | -13.06953 | -51.18305 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bfaf331-897d-3bfa-9754-2b733de25c94 | -11.82004 | -50.52561 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 26df75de-72b2-3170-b0d6-a399985e2da3 | -10.83846 | -48.70147 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbb945ce-1042-3b20-9258-df58526481e5 | -9.34539 | -57.16811 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dc81943-1d51-3a70-bf46-d72065b1cbd6 | -7.5443 | -55.04426 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa364cd0-4f87-3fc1-8292-891a19ede0df | -11.74251 | -50.40469 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05d5ab04-9e40-3b02-ab90-a5ec712792e0 | -11.4568 | -43.4449 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 27794666-ecb9-3af9-92b7-f049aa8225a5 | -11.4436 | -43.42844 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8bcbec12-39b3-39da-b661-d0b4515d12f9 | -9.30839 | -57.71006 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70472ddc-d1c9-3e05-9da7-87d6049aaaa2 | -7.38653 | -46.42675 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3669fc09-7bf1-35ac-9c7e-11677fc3768b | -8.12914 | -43.53295 | 2026-10-01 04:34:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5bc57d38-717a-36af-b8db-94fa31020959 | -10.53003 | -45.37682 | 2026-10-01 04:34:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ed06e03-19e2-34f3-b96e-52ee67bc44d5 | -15.60357 | -38.98384 | 2026-10-01 04:34:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 143fd2aa-7025-37c7-9cdc-4ac2aac10691 | -7.83775 | -47.92358 | 2026-10-01 04:34:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93d5c8ba-b3e0-3456-afc5-e331cce6e7bc | -10.77646 | -50.52177 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1467936b-3ec3-3daf-9626-f80cd27420a5 | -14.14298 | -46.23726 | 2026-10-01 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61922e62-ae7d-3104-b925-2c87811fe870 | -10.52862 | -57.78551 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4a2efc2-53f6-355e-a706-51793d9065ac | -8.20669 | -45.50268 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 746d86e9-58cf-3c7a-abe9-889111f16cd6 | -9.58502 | -54.6291 | 2026-10-01 04:34:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82c8d015-f844-3df6-8ace-bc87f8aae8a8 | -7.54453 | -55.0455 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 834ad3d8-7924-330a-b712-164fd455a1a1 | -12.18922 | -48.44059 | 2026-10-01 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5fd253f4-2e4a-3d72-bd3f-ab7b8acf5e88 | -7.71931 | -49.54747 | 2026-10-01 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c631c27-e981-3dbb-9fba-e504566cbfc9 | -11.37922 | -43.44324 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ad28f67-7d3d-3e51-8e90-4fb1b1604b50 | -11.21217 | -45.14731 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4196cd91-585f-3013-aba2-2dd68957c796 | -11.41571 | -43.4873 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fe36e03-b78c-37b5-a08d-b644d664d339 | -7.06045 | -50.70918 | 2026-10-01 04:34:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6165069-8f4e-39b0-a1e1-05d4d4b85ad2 | -13.38417 | -46.81693 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e3cd5ceb-1eee-3c3f-a80b-c9564a4bbf7e | -9.08385 | -49.88609 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 190b8417-0908-3708-a65f-e466de19c157 | -12.64602 | -47.64009 | 2026-10-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc4712ae-69b1-32ad-9f42-e057a0a6b19e | -13.18046 | -48.50965 | 2026-10-01 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37c7fb96-3cae-3d45-9fe9-24394fd03f50 | -7.38876 | -47.01344 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cb3490d-83dd-381b-a5bc-906a74829389 | -11.19055 | -45.19613 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e0a823e6-7af7-3860-a148-b698e74eb6e4 | -6.50879 | -55.88227 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6692b363-739b-31d2-8116-7443c6bb8eec | -10.56214 | -50.04516 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c05b5234-8e89-3fb2-9221-2e4991ee4790 | -11.60567 | -43.5346 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81758349-060d-3b3f-b0aa-0dabc5348082 | -9.87363 | -44.94719 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0746b314-7968-3bb7-9059-ab24206c6538 | -7.34575 | -55.59968 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b235917-cdaa-3ee6-9048-8e407379344d | -12.37789 | -51.14805 | 2026-10-01 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20c1157a-faa9-3ef5-a936-e3e451d52bc4 | -9.17815 | -45.60772 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4db7f501-ce90-3c8f-af75-fd7e3f41cd60 | -12.86042 | -44.33575 | 2026-10-01 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e3159815-5760-3e82-868e-22daf2361efc | -13.14538 | -48.55856 | 2026-10-01 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4ee43a3-8ad5-3e26-8537-12b652b863a9 | -7.54803 | -55.02367 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b00f9ba0-ac8f-3fb1-ba76-3d5a8ddb1f74 | -13.66917 | -44.30563 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80cd2648-873b-3da1-8aa6-a652fa95bb50 | -6.43371 | -55.80451 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b85da32-ac66-3a82-a900-eaec11bcd477 | -10.53175 | -57.76936 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee485b88-daf0-3887-87c2-79876492ae57 | -8.01231 | -42.88219 | 2026-10-01 04:34:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README61.md)
