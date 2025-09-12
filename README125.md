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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 593b10f0-f5ff-3548-8738-73e232c81341 | -10.89542 | -47.23172 | 2025-09-12 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| da9fd46c-2e45-3ae9-b4ee-87d21aafb558 | -10.6712 | -48.66256 | 2025-09-12 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| ebcb2683-0f2b-3c23-a9c0-dcd261244ff4 | -11.10371 | -51.97443 | 2025-09-12 12:36:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 462cce22-637b-3cef-8f14-cdef3b515186 | -11.95592 | -51.16066 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 09891546-a5ac-3e45-830d-0d525fe7ecc4 | -11.72393 | -46.64733 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 05755d77-7f08-36eb-9a6a-708bcb797011 | -9.03479 | -47.08999 | 2025-09-12 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| b8d66b0f-77b8-36d6-819e-8f90730aeb94 | -9.52305 | -54.62777 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 545a7f27-5c30-3340-b3c3-9c4e0014cd8e | -8.36147 | -44.82805 | 2025-09-12 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 029cefb4-59ab-3a90-9f7e-0d16154eabac | -14.39626 | -52.92341 | 2025-09-12 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 058f7795-40d8-3021-86bb-482943175ae5 | -7.97709 | -46.32627 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 931b4cda-fe42-3db1-a3df-fad4129518c8 | -9.72832 | -48.08361 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7f230700-e93a-339f-bf3a-339a3fb8639e | -11.77204 | -50.56282 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 85181b50-990d-377c-9b1b-402a8c52fdaa | -10.90483 | -47.24819 | 2025-09-12 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| e911591f-8bd7-378e-9ab2-afa2877e24c5 | -12.09601 | -47.60688 | 2025-09-12 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 7a698421-6de8-3f6c-9860-6a2b6fbffc89 | -9.72634 | -46.87936 | 2025-09-12 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a6574092-c635-32b3-a211-24dc4ce8244b | -7.8583 | -45.40133 | 2025-09-12 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5f2a5d8e-a54a-35bc-85cb-614b63c59a40 | -9.87942 | -44.68626 | 2025-09-12 12:36:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 072f1376-6dc8-3b37-8715-1ab717a74901 | -10.89055 | -45.56995 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 0ce712e2-27a1-3ada-95f7-8397aa81edd5 | -8.05683 | -52.32359 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fe733f37-da06-33f9-9b07-2a9a0ddf6082 | -9.67368 | -46.75621 | 2025-09-12 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 60d131f8-1f50-3474-a029-f233a1700569 | -11.43649 | -49.28188 | 2025-09-12 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b61ddd3c-db88-3b90-a1be-4e43f77c36dd | -9.72314 | -48.34096 | 2025-09-12 12:36:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6cbdf265-1d17-35e9-b5fd-9d92dee63c19 | -8.47171 | -47.26669 | 2025-09-12 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| c6af911f-2a59-3e9a-9309-68d2b3a2835b | -9.81299 | -47.81324 | 2025-09-12 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| d05c2905-4443-3b70-9a93-e6bea5abc0ab | -8.05098 | -44.50087 | 2025-09-12 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 9facb35a-dd41-3278-be05-c2f2dc96ebc3 | -9.8813 | -46.46645 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 15e0b403-5204-37dd-8575-d2124cdf7bd1 | -8.46986 | -47.28042 | 2025-09-12 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| fb1de1cd-f2df-38e0-9a3e-f982a17ee716 | -9.56788 | -48.28279 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e05c75eb-5894-3014-9b0b-08f0355fb966 | -10.70803 | -49.1578 | 2025-09-12 12:36:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9cc41d98-0e23-3e8f-8bb8-2aabdc9ace16 | -10.68134 | -48.65755 | 2025-09-12 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5e111c3c-05b0-3519-8c2f-94dacf747b90 | -10.41425 | -50.59486 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1cfb4a41-e4be-31de-b0d6-6d9097952d3f | -10.09285 | -50.38618 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 86eb5b2b-3cc8-32c4-8ac9-b3f60ebd6aae | -9.72643 | -46.88851 | 2025-09-12 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 6025d6df-c5bf-3fc4-94ac-fb98f0a70876 | -11.58048 | -47.60954 | 2025-09-12 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 8b6474c6-6b7a-30c0-ab15-fb9e5db2034b | -8.50342 | -47.30466 | 2025-09-12 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0c81d348-032e-3cf3-a629-bf3d039a98d2 | -11.53422 | -48.52607 | 2025-09-12 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 364b3420-9749-3409-9d7d-a3e5f6ec46bb | -8.95077 | -46.05677 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| ecfe377e-356f-3979-8196-640401da20f5 | -10.58783 | -47.22017 | 2025-09-12 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| fff90e9a-4583-3a14-86ec-50fe4b8d46c8 | -9.61548 | -47.92018 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 255.7 |
| 62aa10f6-d8db-3312-87be-26db51f618d4 | -8.87608 | -51.11911 | 2025-09-12 12:36:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c09245b1-1562-3f0f-a858-e7f6201d03aa | -11.6962 | -46.57404 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 0a66b288-2fbf-33d5-a978-6f187a821c95 | -14.46747 | -56.40043 | 2025-09-12 12:38:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c0f67259-efda-32bf-a2a9-22c5aec4d30a | -20.01021 | -47.65256 | 2025-09-12 12:38:00 | TERRA_M-T | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 35.1 |
| a9cce1f1-0854-37cf-ace9-17df14c0fad5 | -16.49018 | -51.98589 | 2025-09-12 12:38:00 | TERRA_M-T | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 77cb41d1-d2c8-3102-a329-79a273c653af | -15.01953 | -50.12341 | 2025-09-12 12:38:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| c2ace7be-3205-34ed-b9c4-0c1661a61d09 | -21.72594 | -49.7346 | 2025-09-12 12:38:00 | TERRA_M-T | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 2c9898b4-d835-3d02-9b44-483b531abadc | -17.833 | -52.05805 | 2025-09-12 12:38:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| e2f45575-1078-3c5d-894d-27e79c6321b1 | -17.38683 | -52.95605 | 2025-09-12 12:38:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 34f93830-d4c5-3480-9dd5-5bba647a80d5 | -14.83184 | -53.22395 | 2025-09-12 12:38:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 054e8492-edb0-319d-88db-8a58395189a0 | -14.74438 | -55.60939 | 2025-09-12 12:38:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 45fe2cff-8162-3104-b777-2a0d325b2ecf | -15.07366 | -50.16459 | 2025-09-12 12:38:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| cbd7bf21-4217-3864-a8f2-cbd55e202c8d | -15.79341 | -52.23199 | 2025-09-12 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2102865c-52c7-33d6-a9bf-f6eed6b00e26 | -18.65621 | -47.6614 | 2025-09-12 12:38:00 | TERRA_M-T | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 26d2ff85-b0c6-38da-a38f-05699211ba6d | -16.65961 | -47.63036 | 2025-09-12 12:38:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1661d3e9-bddb-38db-8dff-3dd7332440b8 | -18.56535 | -47.54697 | 2025-09-12 12:38:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2537e056-eeea-33ba-ad57-13838e61f11d | -17.37556 | -52.90695 | 2025-09-12 12:38:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| df6d1ca2-9f3b-3fc0-83cd-898f718799d3 | -16.28443 | -50.03671 | 2025-09-12 12:38:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2f79213d-04a3-3172-a249-fe2a2c6ae88f | -16.92864 | -51.87633 | 2025-09-12 12:38:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 7e7010f2-72ad-31be-bcdb-e76e8193afd5 | -17.13268 | -48.49357 | 2025-09-12 12:38:00 | TERRA_M-T | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9cf16fda-d698-3947-a01e-1ada27f259e8 | -15.87914 | -48.18397 | 2025-09-12 12:38:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 25303195-b996-3799-bb9b-5e4620f10dbe | -16.63193 | -49.78848 | 2025-09-12 12:38:00 | TERRA_M-T | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| d0114a18-432a-3eb0-b123-e804e9c1a746 | -14.8243 | -53.21353 | 2025-09-12 12:38:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f17d4a7a-fe28-3394-8323-3e467423c5cf | -18.2518 | -47.2141 | 2025-09-12 12:38:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 846121b1-eb9a-31ac-b550-bc04c959e288 | -16.35213 | -51.519 | 2025-09-12 12:38:00 | TERRA_M-T | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 9679d97e-5439-314a-872d-a804cb94d5b2 | -15.67797 | -47.07128 | 2025-09-12 12:38:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5ff97045-f2b6-371b-94fb-664ccdf942cc | -18.69364 | -48.13338 | 2025-09-12 12:38:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| b95a4445-168d-3e9c-afb2-ade634883534 | -18.02968 | -46.85381 | 2025-09-12 12:38:00 | TERRA_M-T | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 9a2de826-53e8-3792-8d4b-d71abd8ed94a | -15.22855 | -49.68932 | 2025-09-12 12:38:00 | TERRA_M-T | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 293b55fb-ac95-3c44-8e0e-3088c310ea84 | -16.30802 | -50.09332 | 2025-09-12 12:38:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 42.9 |
| f33cc11c-916f-317c-920c-0bae6d01e9a7 | -15.08498 | -52.42612 | 2025-09-12 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 7a5cb67b-762e-3f05-b9b6-7dfacc4e146b | -17.59179 | -52.47404 | 2025-09-12 12:38:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 01a85da9-61ac-35f5-9a33-e974651bc5f4 | -15.7921 | -52.24133 | 2025-09-12 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fd948428-7776-3c9d-acdb-2e1a45de3976 | -14.51152 | -53.90469 | 2025-09-12 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 121efd24-abdc-3f33-b94a-5b578fc2c126 | -16.64529 | -49.76477 | 2025-09-12 12:38:00 | TERRA_M-T | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4fd553e1-38b8-32a4-bdc8-0eaa5ec65199 | -16.35347 | -51.50917 | 2025-09-12 12:38:00 | TERRA_M-T | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 552c2506-25ec-303f-b2d1-3aab3c1e7a67 | -15.78445 | -52.2307 | 2025-09-12 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| aae31b30-082f-3c9e-8147-201aac23ded9 | -18.46028 | -49.42211 | 2025-09-12 12:38:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0c4660b7-7ed4-34c1-8095-68719d3d78c0 | -15.68608 | -53.82426 | 2025-09-12 12:38:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 99a65b55-83ca-3810-9d70-f1f4a35d34d9 | -14.51289 | -53.8954 | 2025-09-12 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 284cf404-5644-36bc-967c-2deb8b807c17 | -16.9273 | -51.88616 | 2025-09-12 12:38:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1c369866-fdd1-3a2f-9cf1-ea039f36ed81 | -15.81362 | -52.22253 | 2025-09-12 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cb686a28-bbdb-3425-b215-173e41914fbf | -21.32594 | -45.0044 | 2025-09-12 12:38:00 | TERRA_M-T | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| a1513059-e290-31f2-abaa-ae6f2de08530 | -18.66107 | -47.64893 | 2025-09-12 12:38:00 | TERRA_M-T | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 60aa6997-2e63-3064-9117-f50631dbb3da | -16.07867 | -49.97305 | 2025-09-12 12:38:00 | TERRA_M-T | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 637d588b-a2a9-33cc-a528-30aeb1ca5f0f | -15.08369 | -52.43531 | 2025-09-12 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 80c001c8-c3e0-3600-8c0e-512b3dfbdb41 | -16.30654 | -50.10499 | 2025-09-12 12:38:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 1c96ad97-0dc6-3e0e-8342-01206f2fc8f8 | -16.66613 | -47.62559 | 2025-09-12 12:38:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 75c61b79-1abf-3bb0-a015-319ea34a43f1 | -15.22872 | -49.68396 | 2025-09-12 12:38:00 | TERRA_M-T | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e6d6eff8-9b3b-38b1-a1f0-2264cd198676 | -16.29809 | -50.09186 | 2025-09-12 12:38:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| cd94a679-93bc-333f-82e3-91e07288548b | -19.34472 | -50.73388 | 2025-09-12 12:38:00 | TERRA_M-T | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 139.3 |
| c832bbf7-39ad-3e64-a8be-e531616223c7 | -21.35589 | -51.17964 | 2025-09-12 12:38:00 | TERRA_M-T | LAVÍNIA | SÃO PAULO | Brasil | 3526506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 165.5 |
| 0c562bba-e291-375a-91fd-4d83d07d2e9f | -15.68398 | -50.5867 | 2025-09-12 12:38:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 59b3da74-fa4b-382b-9fb7-f5f859711079 | -18.44919 | -47.18845 | 2025-09-12 12:38:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 137700ea-0587-3caa-ada5-fdd024ae10f1 | -16.64365 | -49.77771 | 2025-09-12 12:38:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 22d8bec9-cdd0-3672-9416-3981706ef4b7 | -16.44005 | -49.03063 | 2025-09-12 12:38:00 | TERRA_M-T | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 31cd42f3-f4ac-3eb8-a44b-14fe6e42d0ef | -16.06871 | -49.97145 | 2025-09-12 12:38:00 | TERRA_M-T | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bdcfd19f-b661-36e3-9a99-d6676c457640 | -15.81491 | -52.21318 | 2025-09-12 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e606f03b-cd90-3d9e-b3b5-4fae47d8fc15 | -15.73732 | -53.7849 | 2025-09-12 12:38:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c1454411-e8b0-36f5-9577-8f36d12e29a9 | -14.4998 | -53.92197 | 2025-09-12 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| c56d6e75-6e55-3273-8d32-92824a10f06f | -14.50118 | -53.91264 | 2025-09-12 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |


[Clique aqui para ver as próximas entradas](README126.md)
