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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec52bcbd-2924-3385-87fa-50932541e0d0 | -11.47164 | -50.73961 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8ae4ba8-22ef-36bd-bec1-be54a5880543 | -11.14852 | -48.09008 | 2025-09-14 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a421ad66-a367-3d7c-95f4-7eb3c386be03 | -8.93659 | -48.65359 | 2025-09-14 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04b0db60-2f97-3a03-8dac-a2519f0f3a74 | -7.61839 | -46.71309 | 2025-09-14 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d38878dc-e274-3315-b323-845ffb89ea4f | -12.13112 | -44.8416 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9913407b-23cc-3e37-8417-0c7f573f1e62 | -11.48763 | -50.7888 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 822ea285-dba1-32d3-8a46-b6fec1978e5a | -11.24637 | -47.62645 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40a3c5aa-4640-3a10-b018-10e7163351c8 | -11.24479 | -47.62943 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f267233d-3428-3d3e-a0f9-c08c2f7d1dfa | -11.47056 | -50.76813 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5341893d-fe95-30b3-be29-7d8b84dade68 | -9.62408 | -40.61428 | 2025-09-14 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 4f24898e-0011-3e97-b4ee-2b651ca121e1 | -10.75891 | -44.77809 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6018fa5b-9548-3536-a54f-9fe7e658ac27 | -12.75052 | -48.01837 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1eed929a-30c2-39eb-9cf2-6cf1b9d38dd0 | -11.87009 | -50.49509 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2fc8ec2-ba69-3b0e-954d-a5b82c83335d | -7.38182 | -44.35776 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 808f9420-6506-3209-aa22-738eae341a92 | -12.96108 | -47.98577 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5299905-2225-3bbb-b7c2-cb13413688af | -10.96933 | -49.5668 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9e832f19-7116-3f9b-9528-fb6404372d72 | -10.40996 | -50.61053 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a633b69-e7b9-37be-85e3-bac205b547d1 | -10.88518 | -48.18489 | 2025-09-14 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7422d565-6c93-3c36-b4cb-a018d3ff26c8 | -11.46009 | -50.74852 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 263f2917-96b7-3a45-94e2-ba4dbd002b5f | -10.76166 | -46.47401 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b7a6585-2511-372b-b3a9-fe64fe34ec9d | -11.34572 | -50.82645 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a489b99-9111-3f46-b3cd-5356101f9aad | -8.91263 | -46.15024 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b90dc3d6-3285-3834-bdd6-08d4cec31bd5 | -11.48048 | -50.79123 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4558c3d4-f362-3aac-92ee-dc7feb4c4a9b | -8.0825 | -44.51484 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 467d0d28-fd3c-3685-991d-03dea273f36b | -10.76416 | -44.77132 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94615813-bf7a-3838-bf77-82de4f03a76e | -10.13722 | -47.19035 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa290e18-11d4-3cdf-9015-7088c6a64751 | -12.25145 | -46.79356 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bbe4045-a8b1-396d-8bc6-a8096f67bd95 | -13.0154 | -46.7429 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a8e6676-e39b-30f3-b021-eff0f0ea44ce | -6.56254 | -50.8798 | 2025-09-14 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55f01a71-c310-3d22-bbe9-a13f3788c5cb | -8.64251 | -44.03595 | 2025-09-14 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa950fbd-a7c2-3c54-9098-4f63a2613d37 | -10.71364 | -48.70101 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38095ef7-1130-3669-886a-f762ccabf89d | -11.35789 | -47.33053 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17b30389-2bf9-3206-a432-7e0e1e61919e | -7.87833 | -49.50173 | 2025-09-14 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b519a4d-1b05-362f-81a7-513807ae805d | -11.78865 | -46.64905 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0c49a76-aa08-3a21-a7e9-6e4717f0e811 | -11.45624 | -50.75148 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f40c187-1991-3927-ba64-62ddf21ec9a1 | -10.40893 | -48.60525 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c9a372d-b880-32d0-86a5-9948563c015f | -10.92733 | -47.35886 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebe63b26-6255-3ff3-8ed1-c64281f485dc | -12.13872 | -47.59546 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf45e5d2-b5e7-3c20-9ae8-502830a22ae3 | -8.90404 | -48.44723 | 2025-09-14 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f25ff0f7-fc5b-318e-985f-ea3af513ebe2 | -6.83558 | -47.88772 | 2025-09-14 04:40:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7612d003-1bce-3ef7-96f2-3c9d54ac28ea | -12.73506 | -48.02445 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 8411a541-0297-3313-a4f1-d23335265e8b | -13.01088 | -46.74735 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca4a15e0-b300-3c52-b01b-38c9e4734f67 | -10.35744 | -50.48796 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 47da3ccb-af28-3e89-b28c-97a734d23221 | -12.04751 | -46.54397 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8fd56987-a288-35d7-a572-4382b21afef5 | -11.46727 | -50.78911 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d925ebc-5ff0-30ee-9b54-d24c2cd59d01 | -10.35689 | -50.49145 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa97c6b3-9a16-3a73-af9c-04da3ed70e6f | -12.04523 | -46.55104 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 158531da-1170-32e3-a173-438f1b124322 | -11.24758 | -44.77133 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5fda0c11-2628-332e-92db-df00a0aa1b97 | -8.90459 | -48.44355 | 2025-09-14 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0907d6ab-7478-3b02-a684-ce80ff71e175 | -11.49477 | -50.76484 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de78fc53-a5d1-3907-bbb7-9866185c3c9d | -12.78143 | -48.03163 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b20c5a4-028c-317b-a1a3-65fcfb65131f | -8.62654 | -40.1977 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 659ebfc3-3952-3751-815f-c885033ab201 | -11.47109 | -50.74311 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24fb7550-7c43-3ffb-8e82-f14710152172 | -11.89708 | -50.54246 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1485f896-3083-3c4f-a58d-ecfa9e5aab16 | -11.44931 | -43.56482 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0f8be8c-b83b-3c4d-90c1-7ee1920af60f | -12.1028 | -44.85771 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c88e5133-028c-3514-bd17-acb3b75ca87b | -8.18206 | -46.77045 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5624f69a-e69c-3169-abc4-ffd3a563908d | -12.565 | -45.65051 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9b86456-706c-3409-ad0f-dc6b966f4095 | -11.47554 | -50.80119 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9078ff15-0bd6-38b2-ae53-35fac33f35f0 | -12.14725 | -44.81922 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db06081f-d171-3bf5-b6ff-13571b8df000 | -13.01353 | -47.9775 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a49c1b60-7d46-3614-88cd-4f26ed84eb4f | -11.82894 | -46.36579 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6162f513-2048-3523-8066-0da33eab7cce | -10.60013 | -44.33516 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 84b3ff20-4ca6-3c14-ae0c-d85a20654b56 | -7.52043 | -44.36973 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8da7034d-4592-34d7-941a-583f4e20a44a | -7.21795 | -43.97156 | 2025-09-14 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86083b03-721d-3dbd-9cc5-2c961640e730 | -12.78205 | -48.00231 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 839cda13-9646-322a-a782-3f3225fb9f8e | -10.3984 | -50.59796 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1718a9f-ebf3-3495-a3dc-7b72250c07b0 | -12.93082 | -47.9406 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ec2b0f0-407a-33af-91b5-e1b009ddb38e | -10.43563 | -48.61322 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e8af066-de17-343c-af19-a86cdd884fcf | -6.68613 | -45.51924 | 2025-09-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e7a6118-c3f1-3ab5-b59d-0f840b43f0ec | -6.98352 | -44.54738 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07f05301-086d-36c6-945c-d5df61add9e5 | -8.08716 | -44.51178 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c2a2485-486d-3327-8a47-eb073e10030b | -11.49533 | -50.78286 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08cb1b19-b206-3bc8-9228-369c57c0815f | -8.17846 | -46.76986 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b291cc5d-b2eb-33f8-8677-c2aaa8aa65a3 | -10.75521 | -44.77378 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7324e37-a672-3377-9e7d-bb16d89bf423 | -8.14112 | -43.66513 | 2025-09-14 04:40:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 270f3d48-4011-3d79-800e-9c3633f3ca62 | -13.29003 | -43.78756 | 2025-09-14 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 261cd8c1-80ab-3d59-b64d-97328f16279f | -8.50094 | -44.72915 | 2025-09-14 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ca38756-b417-3eb9-baf9-521c4cfd869b | -11.48929 | -50.79982 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d4e50fa-d2b8-308f-9d23-aab51321dc27 | -11.43402 | -43.53775 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 608afd58-bf5f-3baf-913f-c1d08b3dc7a3 | -6.98709 | -44.55136 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97c8be1e-9589-330d-ba60-bb346cc4ce16 | -12.78318 | -48.04458 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68d95991-b339-3b29-a54f-63c7ade972c4 | -11.91499 | -46.52272 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c760125-3c96-3dba-a2c3-ffbc781b051f | -13.9425 | -44.85451 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 309.2 |
| 8f1d05d7-24a0-388d-b0a6-294fd9b02237 | -11.4546 | -50.76198 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae94d380-e634-3122-8f5d-d680612466fd | -7.39446 | -49.98501 | 2025-09-14 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86e2debd-faaa-336a-b8ea-e4a43df82272 | -6.04996 | -49.88088 | 2025-09-14 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5235c911-b560-33f9-a9b8-073cb9dc67c8 | -11.43959 | -45.13596 | 2025-09-14 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 683639b5-b685-3529-8545-b803ec4810f6 | -7.73401 | -45.31518 | 2025-09-14 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9189b8c-5dee-3257-966f-53ab1be6b5f4 | -13.92987 | -44.84837 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1adb6c4-04de-34d4-b097-9355470b9d49 | -6.99271 | -44.54123 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e0e66df-2da3-3bf0-9952-aedf153259b9 | -12.95571 | -47.97217 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c044c2a9-42cf-397d-8b51-302192073497 | -11.49865 | -50.80491 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 73655780-e664-3f51-8453-0aaf1b5e816f | -9.23884 | -45.66637 | 2025-09-14 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99b409ce-890b-3d52-a009-8411a6dc42b4 | -8.9164 | -46.15081 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcc52f3a-158f-3c67-bc06-c55e7c28d1a9 | -11.39078 | -47.33808 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 377a3d84-57e8-3124-a1d1-5fb80d8df993 | -11.7735 | -46.64653 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b586b6d6-8ff8-303a-8810-a2d26283d8b7 | -11.13638 | -45.31494 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c501a97-fca9-3eda-8d99-38d007455b73 | -7.71139 | -44.86474 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8f72fb0-7af8-3599-a2a5-e9c3dfcf0fc8 | -12.12368 | -44.83204 | 2025-09-14 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README32.md)
