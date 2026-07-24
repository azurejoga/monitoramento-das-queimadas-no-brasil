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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c440eba-6855-36c7-9af7-ae836a584519 | -7.81146 | -42.58012 | 2026-07-24 03:30:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4abbffc2-6ce5-3384-94b8-758508fd4807 | -3.99791 | -43.28392 | 2026-07-24 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 800fa9af-04f6-33db-ae47-73b3ed216d0a | -7.01555 | -45.43594 | 2026-07-24 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 737742cd-b144-3c2d-bdf8-6103be3b96ed | -7.01433 | -45.44245 | 2026-07-24 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fd7c617b-f866-31fb-8814-97947f35c6f0 | -7.02036 | -42.7802 | 2026-07-24 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2aaecfc9-a0ef-3314-b711-9ea6760c7521 | -3.99704 | -43.28902 | 2026-07-24 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9d9f11ee-b852-3325-8e4c-3d12715c260d | -4.01309 | -43.28903 | 2026-07-24 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4bffe73-72f4-3ac6-b547-891357bbfdb8 | -4.01492 | -43.27871 | 2026-07-24 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c1d3351-1947-30a2-b994-e69b225e96bc | -4.77655 | -41.79602 | 2026-07-24 03:30:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 19e8920d-a7ac-3013-823a-3d66cbf5ed1d | -16.14518 | -43.62132 | 2026-07-24 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fdb4459-9c60-320b-ab34-8234e6dabc61 | -15.30297 | -41.31736 | 2026-07-24 03:32:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da0166d1-0119-32a1-b84c-f9bebd2f799b | -10.61153 | -40.53343 | 2026-07-24 03:32:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2ea2cd7-afce-3425-a283-2d4cc9ab0373 | -15.30302 | -41.3199 | 2026-07-24 03:32:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59955592-cf8b-32d8-8dc1-04f7e20cb787 | -16.1458 | -43.62066 | 2026-07-24 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c57706e-e51d-3c87-b888-9f9f4ce6d899 | -16.15113 | -43.61895 | 2026-07-24 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aad77623-aa1d-3dd8-81d7-019a25e1f48f | -10.61248 | -40.52818 | 2026-07-24 03:32:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 60fc4a27-d703-35c9-a071-dbf9eb4f7365 | -16.14587 | -43.61795 | 2026-07-24 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a8cf6c5-1ecc-3245-8d29-185438ace44e | -21.23896 | -41.86676 | 2026-07-24 03:34:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6cbf81dd-9bb5-37b7-bb02-91cb52c59475 | -17.61566 | -46.65329 | 2026-07-24 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8a7547a-8344-39a3-a28b-e8c8f8e50492 | -17.8699 | -45.52169 | 2026-07-24 03:34:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e62e02b-3994-3b9f-9baf-bd6fe2b93a72 | -18.19932 | -44.73483 | 2026-07-24 03:34:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca127ea6-702c-30de-bdb2-c910609ee129 | -21.23982 | -41.86237 | 2026-07-24 03:34:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a2a5568c-70a0-344e-9f29-5af966eda086 | -21.56353 | -48.55449 | 2026-07-24 03:34:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 25ab74da-ec97-3f80-8535-df2b9bee6d58 | -18.20011 | -44.73117 | 2026-07-24 03:34:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b12347a9-16bb-3067-a8e7-098c33d885c7 | -18.25272 | -42.52867 | 2026-07-24 03:34:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2744af43-a678-3883-a5c2-304991c88326 | -21.56217 | -48.56014 | 2026-07-24 03:34:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 72320d2f-c801-3671-96e4-7476c1196219 | -18.19808 | -44.73297 | 2026-07-24 03:34:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17e196cd-2f92-3ccc-938a-d773b630d1cc | -18.25378 | -42.52336 | 2026-07-24 03:34:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ff404512-3653-3799-a6d6-653188396f73 | -18.19733 | -44.73661 | 2026-07-24 03:34:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b6de53f-7ff0-3915-a971-3318859ad3a2 | -20.32829 | -42.3079 | 2026-07-24 03:34:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 17863d98-1a57-3106-984b-aad9e6ab4a6e | -17.61677 | -46.64833 | 2026-07-24 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c25a4e9-c055-36ab-9bd3-a099eee3f0d9 | -19.13918 | -39.96848 | 2026-07-24 03:34:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f31ff5ce-6330-3cd8-b047-fc04d9f8ee18 | -17.91675 | -44.40773 | 2026-07-24 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2c92f6d-51dd-3ba7-ba88-fc7a54a7f874 | -19.72461 | -46.17046 | 2026-07-24 03:34:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ad4c329-f5cb-3ff1-bdf8-28b6129af5e0 | -17.91752 | -44.40401 | 2026-07-24 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32f4a44f-3859-3f34-9169-b81998f7596a | -20.32923 | -42.30305 | 2026-07-24 03:34:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 238a1b19-8bab-39dd-8998-b9209e471dde | -3.62399 | -39.23597 | 2026-07-24 04:04:00 | NPP-375D | SÃO LUÍS DO CURU | CEARÁ | Brasil | 2312601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf8502b6-5976-3683-a8be-c69889b47ecf | -3.52858 | -42.7005 | 2026-07-24 04:04:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c99cdb2a-af9b-316f-8a62-21794c8fe639 | -4.01521 | -43.27786 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 463645af-67b6-3521-ba01-881a93c31fb6 | -3.99692 | -43.28611 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b2fa98db-21e0-37f4-a104-b2df5c1eab93 | -4.01049 | -43.28082 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 042f1eff-e8b1-30e2-849c-391fae26815b | -2.90709 | -40.39759 | 2026-07-24 04:04:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9c65fe93-705f-37b8-815c-5536ad3772c8 | -4.01398 | -43.28523 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b5be6bc-56a2-34e7-821b-211e992aa969 | -4.00987 | -43.28453 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5353a65f-c9f0-3eca-89b2-9a6a0ce16331 | -2.90355 | -40.39703 | 2026-07-24 04:04:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7d56852c-b951-3430-8ee3-78d9bd05738b | -4.04716 | -43.23804 | 2026-07-24 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4d92215-b103-3ee6-8002-3d532235bcff | -3.63329 | -42.05199 | 2026-07-24 04:04:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3998ec0c-3fae-3571-91b0-976dbb9ef3fb | -3.99475 | -43.28635 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d4abc91-3b33-3ec1-a1cf-f8608dbd0ae6 | -4.01111 | -43.27715 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45ba5f40-1d43-3f55-8aa9-921abcf3b373 | -4.0376 | -43.2702 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87570ce5-8a06-3604-8659-e6cf13a5866f | -2.90772 | -40.39363 | 2026-07-24 04:04:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 73e4ccc8-8536-3995-a139-fdc1678edcb3 | -3.99416 | -43.29003 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82abf314-3042-31ed-8918-7a3eed01a70c | -3.99535 | -43.28267 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34c772f9-ab83-3021-827a-de14fe4bb968 | -4.04656 | -43.24165 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01f8faab-12a0-3592-8076-c6a372b5ca75 | -3.9963 | -43.28978 | 2026-07-24 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eca94438-c70d-32ec-8fb2-2485f2282798 | -2.90419 | -40.39308 | 2026-07-24 04:04:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ca49c256-efc9-3e16-8ba7-8c9efd61a917 | -3.52459 | -42.69985 | 2026-07-24 04:04:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61762b0b-1aa3-3864-bef2-ed0c29e6017e | -7.01322 | -45.43947 | 2026-07-24 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 076c4621-1f16-390e-8c2b-b160b6f38dcb | -9.23051 | -48.55848 | 2026-07-24 04:06:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 917c3672-0e9a-3d79-b49e-2b23e0cbbbd5 | -5.62049 | -45.97272 | 2026-07-24 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dca9ea1-89b0-3860-85f1-8a6bf0a67716 | -9.22794 | -48.56137 | 2026-07-24 04:06:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81d4871f-590a-35be-89e7-9dc5837301b0 | -5.80493 | -43.64207 | 2026-07-24 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dd1a539-f49e-3b42-b12e-23e24266bbd7 | -6.14138 | -44.94069 | 2026-07-24 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c9dc9ed-7dda-31b9-918e-3d85ed8778c0 | -5.31988 | -43.56211 | 2026-07-24 04:06:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bf14b3e-1d5c-3ccb-9890-25d3188ea424 | -5.49017 | -45.12449 | 2026-07-24 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f66df09b-2416-341f-8ee8-59de3d6fe0b9 | -7.30375 | -47.01915 | 2026-07-24 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2aba769a-802c-34a2-98bd-514ee92b5389 | -7.14878 | -48.68097 | 2026-07-24 04:06:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3baf06c-0f40-3d3a-a339-ac832ef465ee | -4.36781 | -47.76735 | 2026-07-24 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d553a788-e3ba-34b5-b5f6-4a260d88fb39 | -7.0158 | -45.84714 | 2026-07-24 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a03e2e2-4b13-3540-b68e-bf30856db811 | -4.91574 | -43.4694 | 2026-07-24 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1e26b06-610a-3b8f-af42-2d3f12a26316 | -8.83297 | -47.07698 | 2026-07-24 04:06:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7486deeb-6147-3e42-ae7a-0680d41556ab | -5.61959 | -45.97787 | 2026-07-24 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 670a48e7-881c-333a-b1ce-5ea1df593d76 | -4.77538 | -41.79575 | 2026-07-24 04:06:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4ea95a2c-6f1a-3f66-b3ba-423cb1a84a8a | -5.35666 | -43.14172 | 2026-07-24 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb2f3d13-7d22-394c-a27b-8b36989be767 | -7.00951 | -45.43399 | 2026-07-24 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c43f78ef-94cf-3a5d-aa0d-73f5be8ea3e7 | -5.74755 | -43.2671 | 2026-07-24 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ab9689d-1261-3f13-a0d6-77ccabd60216 | -6.13695 | -44.93982 | 2026-07-24 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02fa5c32-34bd-3bc7-814d-2ccd918fc22e | -6.1362 | -44.94419 | 2026-07-24 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1871be4-44bb-34e2-a6df-f5230573f062 | -7.81314 | -42.58093 | 2026-07-24 04:06:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cbd9f5ec-a84f-36ce-b5db-c8a66f8752cb | -7.01032 | -45.42939 | 2026-07-24 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6644d543-e677-34aa-8229-a8d5aaa1ca48 | -7.14314 | -48.68003 | 2026-07-24 04:06:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f5be8bc-b8eb-3a18-8145-66d1df1fd528 | -5.66736 | -44.12149 | 2026-07-24 04:06:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77cae2e9-27d3-3c03-bb36-d8e17dd56006 | -6.48804 | -43.78904 | 2026-07-24 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d32bc5f-8f18-3c11-84a0-5f3b2c382e34 | -5.09755 | -41.71795 | 2026-07-24 04:06:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 52fd932b-94c6-3787-85ec-74339a05e82b | -5.75154 | -43.26786 | 2026-07-24 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75f8107e-b677-389b-a7b6-358d0ffc1be1 | -5.74696 | -43.27058 | 2026-07-24 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 90700b20-297b-3b18-8e9f-4e408fefc868 | -7.01403 | -45.43485 | 2026-07-24 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0f090c8e-8e21-3bc6-8936-b5786020bffb | -5.31926 | -43.56583 | 2026-07-24 04:06:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b6a7b09-67d0-366f-99da-0bd64258c3b2 | -5.74297 | -43.26986 | 2026-07-24 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5dba8618-9db8-368d-ab07-c45a502a0af9 | -4.37273 | -47.77197 | 2026-07-24 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee544445-c983-3877-9754-4013fe6e4e17 | -5.82773 | -43.48289 | 2026-07-24 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1347cba-6b16-32de-8cdd-d987cd808cf2 | -5.32049 | -43.55845 | 2026-07-24 04:06:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eba5c994-0f7c-380d-aada-0daa74db849a | -7.30324 | -47.02205 | 2026-07-24 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 899491af-2140-364f-b954-b5a89535a802 | -5.74237 | -43.27336 | 2026-07-24 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e11b8709-b59f-3242-8f84-467348d37ec1 | -7.00499 | -45.43312 | 2026-07-24 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e098b768-6935-3e54-94fc-45d3c1f1549c | -4.37337 | -47.76825 | 2026-07-24 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccdb3171-b4ea-3f73-be37-9c140c3c259b | -5.80554 | -43.63845 | 2026-07-24 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fb72b8e-a065-34b3-be0c-a48a2ccf247a | -7.02109 | -42.78197 | 2026-07-24 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 379aaae0-441c-3365-9bb1-e67faea15c6f | -7.0087 | -45.43861 | 2026-07-24 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 13f13b51-0b35-36c3-9ee7-79ea78bcf866 | -9.2299 | -48.5617 | 2026-07-24 04:06:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README3.md)
