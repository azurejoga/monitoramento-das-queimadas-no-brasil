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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1104de24-d061-3101-8bc9-7ef23b6ef83d | -5.75203 | -45.16424 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df1e746b-c076-3fe0-8b7a-8797ec76d89b | -10.7162 | -44.42617 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ba8e7df9-4619-37a2-99a5-ec90cb354ad4 | -15.34934 | -50.15177 | 2026-09-30 04:53:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30daa760-1e93-3e54-b21c-ebce7b9e1de5 | -7.5318 | -44.54513 | 2026-09-30 04:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f77d6e4c-18da-3984-b11c-249388a7f043 | -5.03166 | -43.56766 | 2026-09-30 04:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a1580d2-cac0-3634-b895-56a6d319143b | -7.95298 | -47.70697 | 2026-09-30 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f07434bd-5ad0-3e56-a492-4ddd80edc09d | -9.81864 | -48.2123 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c2f1811-63e7-3520-a2a1-21e0dfa3bcf8 | -5.9758 | -55.37391 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02a57d01-691f-3b01-b7d1-0f3741266c09 | -4.80232 | -45.64077 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4875c73-93a2-3305-a0dc-f17a2d8f6e69 | -11.71156 | -43.4465 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf90e27d-4932-31e1-817a-d0be1ececf5e | -6.11094 | -55.70086 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ae418bf-d378-3142-808c-dc67d67c3ab4 | -10.51588 | -45.37828 | 2026-09-30 04:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cac4f5dd-e8bc-348e-b3fc-da25930cbe8b | -10.71199 | -50.84229 | 2026-09-30 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58ece944-7425-3901-9cd2-8235a24c736c | -7.82155 | -45.82488 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b84272f4-19ef-33c8-b8e6-733ec2c4e740 | -7.50502 | -45.80822 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70ba3221-287c-383a-8c78-e77ec6c719dd | -3.83672 | -52.26251 | 2026-09-30 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43f95565-9437-34e1-bee7-6831560f8999 | -7.82302 | -45.81682 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6ec08ca1-d45e-35e7-9109-116f7c7692b0 | -11.43095 | -43.42947 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe494d2a-7af6-380b-a770-05d9ef4a2cd1 | -8.38735 | -48.06812 | 2026-09-30 04:53:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eba91583-db5a-310e-853f-c0805665fe19 | -10.83595 | -48.70359 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d0d0b93-0867-3318-98f3-0fccae014bdc | -6.31051 | -56.05022 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9298b2c3-6522-33e6-bf12-2f8b75acf666 | -3.24625 | -50.81067 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9a15cdf-df1d-3781-9071-521b55c6257b | -7.01972 | -44.62114 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1e8fa87-2e02-30a2-b768-a4aea271256b | -11.7164 | -43.45046 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42b57e26-0f8b-3773-93e0-c3939cfe8295 | -9.78994 | -48.22604 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cfa389de-9b0e-3e57-bd34-857b6c93be4c | -11.31982 | -47.75042 | 2026-09-30 04:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e545a873-48cb-31ac-80e0-914ce90ec8ce | -9.59796 | -45.73001 | 2026-09-30 04:53:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9094e4c-9b2f-3388-a618-7d0f26682530 | -6.72598 | -45.58349 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 60036364-d745-3859-bb08-bf6ce87ffdc6 | -7.0086 | -45.30628 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b48e1c14-55c6-3903-a1c6-f0cd7d4dd506 | -10.76713 | -50.483 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 875b004e-2594-3b95-b24a-d5f378262e2e | -6.35777 | -55.45269 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa35ca45-f719-3b86-8427-8c43d18500a1 | -3.35878 | -50.46531 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18b160f4-b159-31d2-8d6d-af653cb19477 | -3.18214 | -51.23656 | 2026-09-30 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ea3372f-88b0-37d3-bead-1a0de00f7e7e | -4.81345 | -49.46311 | 2026-09-30 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd81ca8d-375d-3995-a340-f85a5be12400 | -11.365 | -43.35997 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 204dc1cd-6d49-38fc-ae95-04d118498188 | -11.38432 | -43.37577 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 95265221-f2d9-3283-b664-843d0c22f0a5 | -8.26558 | -54.75518 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e392b4a-1096-3d10-8586-207d7a46f0ac | -5.74168 | -45.17492 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a53353cb-c01a-3f35-8138-f89acdcc36be | -7.72575 | -54.80065 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e44bf0ee-e5c4-391c-83ed-f13f871af875 | -11.38377 | -43.46601 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64127185-2465-3919-8e67-a7d8ab05cb1a | -5.03268 | -43.56965 | 2026-09-30 04:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dc8f3a3d-f705-3d85-990c-c17cecdbddf9 | -7.55198 | -55.0375 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e47130fe-5dc2-3997-a2b6-a2e7284a0e16 | -7.8137 | -45.81968 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f3dab3c-6216-352e-a057-3d3fb0774020 | -6.22484 | -47.44801 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcc28158-4309-3303-adb1-b284c97edde6 | -3.05225 | -53.87014 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddd94931-ed7a-3044-9549-2ac7127f4b6a | -11.43536 | -43.43663 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d776627-02dd-3163-a718-bd19cae34308 | -5.74346 | -45.16308 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 481d25a1-a110-39e4-8cb5-7fa2eadbc6f1 | -3.91533 | -49.37283 | 2026-09-30 04:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4704f343-40f4-3e18-a0fe-518342a0b1b8 | -3.14622 | -54.07874 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 937e9f8a-ec2d-3104-b3c1-f1eb40cb5612 | -11.1907 | -45.117 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c5619fb-fad6-3566-b1b4-3174945c8523 | -10.20048 | -49.97605 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7e69c27-4b83-3512-b865-59135056fa51 | -7.38403 | -47.01244 | 2026-09-30 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45f8e692-94b1-325a-b0c1-6a74c8741d5b | -6.73498 | -49.13227 | 2026-09-30 04:53:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc43e7ee-f45d-3f51-9da8-3d2749dd3281 | -16.67087 | -41.85459 | 2026-09-30 04:53:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 49466370-0fa0-3c01-8e3b-cb78325ca619 | -7.82139 | -45.82838 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61f32be4-1130-3dd2-8243-d76dc4335220 | -4.80952 | -49.46617 | 2026-09-30 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2d19fd2-443f-3aa9-8585-c672de269f0a | -3.96601 | -53.43542 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 686610cb-443d-310f-a037-2efc50cbf61a | -3.01015 | -54.22599 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5765c78c-8334-3b5d-a848-53c345a72454 | -8.26289 | -49.50553 | 2026-09-30 04:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 097c6a0e-afae-3eef-82b0-d1867167de91 | -9.04388 | -47.32736 | 2026-09-30 04:53:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05e1eb3d-9785-30a2-8a0a-95e7cfdc79a0 | -4.12684 | -46.86879 | 2026-09-30 04:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9afea336-ae9e-3e4f-8f50-6736249d8e87 | -7.4748 | -47.41686 | 2026-09-30 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32d5e824-6515-3381-a206-6c9eab131fcf | -4.11781 | -48.82138 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 610796fd-5356-3643-8164-4d4f693a9c8b | -8.11425 | -54.85567 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a5a199c-5439-34be-b108-89cfeed5ce59 | -10.77174 | -47.72038 | 2026-09-30 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 90785298-b7e2-3ecc-89bc-a8d2c3786b22 | -11.44018 | -43.44057 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e3acc39-5c1e-30f5-9a4f-0d537ea2df5e | -5.8557 | -51.79315 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8b711aa4-2f5b-3a09-8c03-d117fcd72691 | -3.56809 | -50.25865 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 537c0145-9295-3f61-9308-fe058bcae97d | -11.175 | -44.82571 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ae76a6a5-0450-3a27-9000-2e9cf82ee316 | -7.01845 | -45.29927 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4190749-cc04-3e9c-9160-faaa195c7450 | -7.82746 | -45.81406 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e68a619f-7e84-345f-bf08-369348ae9667 | -7.55126 | -55.04185 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccb37a72-38c5-336f-a891-9e5115c84c3f | -10.58128 | -50.85241 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00463b97-8375-3076-9c39-6c62b220b80b | -11.26359 | -43.52971 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34e86a45-c84a-3f17-8ca6-3d5e284c713a | -6.33463 | -51.15248 | 2026-09-30 04:53:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49103cb6-1a9c-34e6-aaaf-d3458df54c33 | -7.54043 | -47.1237 | 2026-09-30 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17abfd22-84fa-3745-97b8-e7ed5fb927a3 | -5.85238 | -51.79263 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0f83186f-5e3b-3f18-a6fb-cc4734907ee4 | -5.72886 | -45.17306 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ac33fde-5e2e-364d-a51f-8b64a587344e | -4.29799 | -48.60813 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01963d22-fc62-3c43-9776-ab5ceff1fdbe | -15.63494 | -43.2383 | 2026-09-30 04:53:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0cadf711-0d96-3a1e-b79f-11e92eecaecb | -6.22923 | -47.44416 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44eab863-a73f-3453-ad3b-7863ab555a92 | -5.87239 | -50.16119 | 2026-09-30 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b248a69d-a62a-3751-b814-a38dac9c34c1 | -13.54191 | -52.22338 | 2026-09-30 04:53:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9704a96-d3bf-3508-858b-9edfb6c2a6bc | -7.49896 | -55.03772 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a627bbc9-573a-3c02-8e47-78d780079ac5 | -6.38278 | -55.14139 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32855e70-48c3-36ad-9a93-e39ef8b3e53f | -4.54275 | -50.77619 | 2026-09-30 04:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0adc2da6-c137-3f6e-8987-7553b1cc0ea5 | -3.1529 | -54.08438 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f56e49b8-4585-3a10-bf54-c66f0bdfb39a | -6.34327 | -55.3292 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7601afbd-3d70-334d-99f0-eb2d0d69890f | -3.60905 | -48.91668 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cca9edb-9a63-3002-bf62-c58483675297 | -10.57455 | -50.85136 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7cfe715-d989-3864-b794-4bba9f1eb48e | -4.80532 | -45.64851 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04ab9027-4e86-3542-97a2-bc72eef84f0d | -3.38127 | -50.94536 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5553c9ec-10f3-3db8-9a52-6628464365ad | -3.71022 | -54.221 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7eabe45a-e4c1-33e1-907e-05c459bb3a69 | -11.40075 | -43.41557 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 626f2b19-4624-3cfc-af6b-5883c7d739eb | -6.40298 | -55.20559 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44d0f391-7440-3ed1-b736-e501ecc4c77a | -7.0252 | -44.62419 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d34b6711-e358-3c59-88d6-e4f87de6a424 | -5.30001 | -55.98127 | 2026-09-30 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30244fd8-f553-3423-86f7-a349837cf0fd | -9.81934 | -48.2076 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74cb4c54-b51f-30b7-9770-fb3bf286bcff | -6.22551 | -47.44356 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5385b9c-c610-3a76-9d13-b594ae4fcdef | -4.35881 | -47.77016 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README50.md)
