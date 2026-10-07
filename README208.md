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

## Dados Diários - Página 208

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9508e09b-f4a9-3345-aa82-dedb81140fba | -6.12295 | -51.68797 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5de4bf98-b004-3cc1-9d9f-81e66688071d | -11.23059 | -46.24162 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 448d135f-088e-33ac-8ca9-90d793ea316e | -8.59786 | -45.08095 | 2026-10-07 16:37:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4b1160e7-3ff7-35eb-9aa3-c20d25361702 | -9.94991 | -43.54829 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 404babaf-7909-3d92-bf72-0650409c50c5 | -11.15632 | -46.11024 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1e91243a-8acf-37eb-8a5d-f6f7a8f94058 | -8.75972 | -47.57952 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5f750280-9ffb-3062-9ccc-bc37cf523338 | -6.61719 | -37.88358 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 29673d68-9b6d-30ce-a24e-16ad61d6a3bd | -3.76983 | -41.78787 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| c175e52a-cd93-311b-bfe3-81f17a16128f | -7.43885 | -44.46263 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 83b6c20c-e324-32e7-ad2e-e91c98218d72 | -8.54671 | -54.5825 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cc4428b9-753e-3482-836d-c5d03573ab06 | -5.04357 | -49.76367 | 2026-10-07 16:37:00 | NPP-375 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 692b918e-59f7-3c6c-bd9a-590333480960 | -7.76687 | -54.94076 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a02c5c63-632b-3e70-a481-fc16f3761f68 | -10.62708 | -53.85177 | 2026-10-07 16:37:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 2f78f0f3-b6f9-3fdd-9323-e1f4ff3d286e | -10.99198 | -45.41427 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1878c4dc-dc46-3d1a-a3be-7db88e5cc7b9 | -3.85676 | -42.23311 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f9125a48-46e8-3406-b65e-09e28670b92b | -7.86779 | -44.54326 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 44169a95-bb52-3c5b-9cd1-d348558077d2 | -6.22073 | -52.83946 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 85d27e3e-c35c-36af-86f4-d5e1c58e226a | -5.37402 | -44.17485 | 2026-10-07 16:37:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 46812683-7afd-3f2a-91db-d214e13cb4f1 | -9.86047 | -46.30689 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a59e6544-3b96-354b-ac3a-a2f357551a37 | -6.2863 | -44.90274 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 140438ba-2f04-3782-ac32-58535c3c7e78 | -9.5809 | -54.64027 | 2026-10-07 16:37:00 | NPP-375 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4edf2f39-a011-3ef8-85dc-fbc44280a4af | -7.38762 | -45.61052 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c7b41999-76ed-3ad9-973f-48e19d777ebd | -6.40144 | -52.71832 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6c6a9d6c-46cf-3a1c-8d5b-724291b94ac3 | -11.39989 | -50.88348 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a73a91c0-fdbf-3169-a81c-cf0c7e1ef9c5 | -6.68695 | -44.94026 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7b9834ae-330d-3f89-be45-f3f64e9b04e1 | -7.17642 | -47.80354 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| dd0b440a-81f1-3c7b-910e-102353b771f9 | -6.68321 | -52.8658 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 50c999e4-6919-343f-8cdf-e212e0683753 | -4.80219 | -42.16302 | 2026-10-07 16:37:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| eed3f8ee-2b1e-3b03-8145-d866eaa25898 | -6.14784 | -39.42482 | 2026-10-07 16:37:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 2c282887-ebb6-3009-8d50-b5a8901ca49e | -11.09372 | -45.67101 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 427df203-ae88-31b9-b3b5-3617dcc7b49b | -5.74152 | -41.72013 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 044e5023-601e-316b-9b5a-5038d4fe42f0 | -6.63651 | -50.06377 | 2026-10-07 16:37:00 | NPP-375 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c1909b0-f871-3d1d-9c53-69c2311ea8e2 | -6.09359 | -55.7375 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a660ae34-7557-32d9-a77c-5a3613749794 | -8.52861 | -54.62031 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c9228c8f-b0b0-3bcb-a0a5-dace39bed3af | -8.941 | -47.39018 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8ef54b08-685d-3528-bd16-36887fa8eafb | -11.15144 | -46.1279 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c238238a-5953-33d4-8210-1373ffce5131 | -16.35069 | -44.71729 | 2026-10-07 16:37:00 | NPP-375 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| db547f19-1a94-3484-95b0-001fe6c6bbb7 | -7.04078 | -50.68767 | 2026-10-07 16:37:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9a28b43d-5b95-39cc-8099-dc97dfccf0ed | -4.19553 | -40.39301 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 7df37f45-acc5-392d-9a94-1d73ecbb6ae4 | -7.11014 | -55.72888 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f8234939-0801-3b5c-9d13-6d5e0775b352 | -7.83503 | -45.50486 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 826c3336-570c-3aa1-8763-73584f315809 | -5.68312 | -53.4937 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ebb06b1c-8215-32df-924d-922e3e302efa | -6.22639 | -52.84193 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ccb3cf2a-2495-3fb4-b019-21da91b3a9a7 | -11.05585 | -45.82802 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4c284f72-f837-393e-a3de-16c0d2876377 | -5.98217 | -40.9369 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| de19d4f3-7fdf-3290-9355-a140bcceaf46 | -5.32282 | -42.80898 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 576727ad-b695-340b-ae2d-8dc4989b7032 | -6.37644 | -55.20511 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3ac62acd-c1d6-3242-b4c0-3e45b481757f | -5.5154 | -42.81229 | 2026-10-07 16:37:00 | NPP-375 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 40ac9791-0f93-372a-8d58-97442a3a3b8f | -7.30808 | -43.97729 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 93449d5a-7e41-31e1-bef9-9ec23406c887 | -6.59203 | -41.55613 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 357b1693-f764-3e7a-a427-3eab7646bd09 | -7.50674 | -45.77833 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 14ab5d80-f807-36f6-8956-3ec73aa4f516 | -10.87923 | -47.60816 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 293f224f-e9f9-3871-80af-f1fcfaf669c9 | -7.80608 | -45.4979 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3e475d3e-d9ae-3396-a740-9f31a6f2b7cb | -5.30833 | -55.92099 | 2026-10-07 16:37:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f04ac028-6cd8-3b23-b627-84b258ecbdbb | -5.96078 | -41.34807 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 3e59c8ed-c7cb-358e-bf2b-994bfbc1e798 | -3.44111 | -45.06802 | 2026-10-07 16:37:00 | NPP-375 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95539cbe-42b3-3418-85f0-b73f15be89e4 | -5.97651 | -40.92474 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| da9968e9-7151-325a-ac84-0fd7b23a0a7d | -6.63539 | -43.77904 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 1dc2713b-537c-376d-b26d-e6e4211be8c6 | -3.90479 | -44.11747 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 87ad5afc-1288-3eb1-a32b-581a03e5a7b7 | -5.61658 | -45.81915 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 665fcf95-83d3-3d8a-aff5-86c8edb6f5bc | -6.37494 | -55.46913 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8eac08a4-9bc3-305d-8d3a-ebfcfdfef7da | -6.6129 | -53.01233 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 867ab9ad-71e7-324d-825f-4980ec2c12c6 | -3.22761 | -40.17605 | 2026-10-07 16:37:00 | NPP-375 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0fcaefd2-39c1-3a85-8a8a-28701086fe58 | -6.4062 | -52.71456 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6d2c41a-8405-3f00-9f42-1cb0c643ef01 | -6.98485 | -43.21572 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 001c4fdc-d251-39d4-9096-160e10049728 | -5.97755 | -41.3619 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 89471f3f-4ead-3321-97a4-c61eecdfa3e5 | -11.09267 | -47.6243 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 70ace4ce-9711-304a-b4a0-4b632515b714 | -5.80664 | -52.35547 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 993ad386-6ee4-38ec-b12e-f5c28410a6af | -11.11247 | -45.70094 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 24baa84f-3831-37f9-b4e4-27ea2d660827 | -5.72878 | -45.15108 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| a0ced5d6-ce0f-32a3-a59d-c060cbe1aa6a | -11.10416 | -47.59203 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 55f6330a-e94d-31b6-98ca-9f49a737a132 | -9.88815 | -48.78296 | 2026-10-07 16:37:00 | NPP-375 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 141099fe-520e-3e8c-aba3-1a50ec62f7aa | -5.94386 | -45.38289 | 2026-10-07 16:37:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a4802cc-561d-32b1-838d-aa9e8982258f | -14.56774 | -41.42176 | 2026-10-07 16:37:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f56c921-b36d-3663-997b-3e72fd97c82b | -6.86019 | -52.83597 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9eaf04c8-2f9c-3898-a4a3-7339398ee001 | -7.87534 | -55.01377 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 195f6bb7-20e2-3514-9964-f8eb654c1f83 | -5.48886 | -42.84227 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 92b9fc50-4c70-34c2-935a-e9b661b59036 | -3.32743 | -42.77087 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bfdee92f-dfb3-3ae7-a99a-d7d2cf6aa919 | -4.27351 | -39.55137 | 2026-10-07 16:37:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| cf801ed8-799f-3517-80fe-118b077ed66a | -11.05409 | -45.81589 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b9ed8ece-469e-371d-8bce-9937df5e2b65 | -6.44707 | -45.20282 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48cb0142-a74f-38b2-a4c8-30002db29cfc | -3.77404 | -41.79142 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 36.1 |
| 2f7668f9-ebca-33b0-a51b-287a1fc8d97a | -9.96588 | -45.97552 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 253eb123-5819-3243-afef-8fb5f5268880 | -17.14842 | -43.85315 | 2026-10-07 16:37:00 | NPP-375 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2c57653-0080-3935-a017-d97a5dcdd931 | -8.90851 | -48.73516 | 2026-10-07 16:37:00 | NPP-375 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6274d25-0d0a-34d9-9e9c-c0067faca17a | -3.15363 | -43.49739 | 2026-10-07 16:37:00 | NPP-375 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b82cbc66-04a4-3901-a504-7143e0f7d5c6 | -15.16604 | -41.98645 | 2026-10-07 16:37:00 | NPP-375 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 762610b9-386a-387d-bf64-ab734c0dce38 | -11.1387 | -46.17086 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f3817a73-aa6b-3e2a-89e3-f3977cf16753 | -5.24541 | -50.91047 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| e48c801a-d028-3ae8-bdc3-74c723abb6a2 | -4.63404 | -48.85436 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d2410376-a89f-368b-87d8-7c19dad9c573 | -7.39192 | -38.9771 | 2026-10-07 16:37:00 | NPP-375 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| da957d41-8282-33b2-ae91-90d6aaf0daa9 | -5.94213 | -45.3941 | 2026-10-07 16:37:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 46a1c936-d8e3-371f-b1ed-8b5ad33f860f | -6.60086 | -37.89528 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 89926223-1cf4-3e45-bdf7-4f887032535a | -7.77645 | -48.24017 | 2026-10-07 16:37:00 | NPP-375 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 45bd82bd-096f-3863-af45-ac34ca146828 | -3.49722 | -40.31081 | 2026-10-07 16:37:00 | NPP-375 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 9e2af32d-e9fe-3b35-bf4c-4dde93d5dda9 | -6.94104 | -45.2833 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 774a1dc4-2655-3053-a28c-e9995fc39e61 | -5.72417 | -41.74685 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 22eaf0a0-f691-37e6-b314-dc243af23765 | -15.70131 | -40.59917 | 2026-10-07 16:37:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 31655e65-5b8f-3c46-b1a9-4568c6615bf5 | -7.81582 | -44.58361 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9bfec350-c4c5-3fc5-8328-d6b881fafb78 | -4.61917 | -45.52249 | 2026-10-07 16:37:00 | NPP-375 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README209.md)
