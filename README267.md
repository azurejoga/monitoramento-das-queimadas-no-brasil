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

## Dados Diários - Página 267

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b36a26e-714e-35a9-8515-0cfdff606c0b | -14.82733 | -42.31498 | 2026-10-09 15:58:00 | NPP-375 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 64bad7b0-18b5-3547-97b3-85b50bc40fc3 | -16.50607 | -41.6278 | 2026-10-09 15:58:00 | NPP-375 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8c0709e4-aa7b-3727-892a-424a176598f9 | -12.22963 | -40.20729 | 2026-10-09 15:58:00 | NPP-375 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 3b21bff3-005f-3fe1-b953-09c84a0acb0b | -11.46773 | -43.3867 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 40db2232-fe66-3bff-8c71-cfedddb9ca34 | -17.54898 | -42.12087 | 2026-10-09 15:58:00 | NPP-375 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8ee03aef-9703-3ee5-90b8-a40b2ec8ab88 | -12.34701 | -39.55354 | 2026-10-09 15:58:00 | NPP-375 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 8e2a539c-406d-38a0-9940-4f6911373c12 | -15.25252 | -42.37321 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| e6bdd4e6-e405-3cdb-84ce-be660efc4653 | -14.4365 | -43.94172 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 6374dc59-5a8a-35c5-ba35-c2244d04bc51 | -12.34685 | -47.32161 | 2026-10-09 15:58:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6215a1f8-595e-3ad7-9da6-5712b653a4be | -12.90201 | -45.11601 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 63c38ee2-d3ce-33d8-b080-4b97227e6886 | -11.98348 | -43.48161 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2b03dd0a-8359-39c4-897f-c89d99c3157b | -13.24154 | -39.76508 | 2026-10-09 15:58:00 | NPP-375 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 91eb7932-579e-3d8a-8b2a-80741f6e4134 | -11.59848 | -43.69962 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| d37f5e24-6cad-380b-a0ca-ffc6ed0b93c5 | -11.5927 | -43.70027 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 8e38444d-9222-3929-952c-f64577d62155 | -11.97728 | -43.47831 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9b4e788c-da5b-3375-a14a-c94c42898e65 | -12.62804 | -40.30685 | 2026-10-09 15:58:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| eedadabd-599c-382e-b64e-4fa3af328800 | -12.12805 | -43.30721 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 3038a8ac-6de2-3833-9bfa-cfc6d796c0e3 | -15.13653 | -44.05892 | 2026-10-09 15:58:00 | NPP-375 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6aa5f39-135e-390f-919b-ec618bbd776c | -12.24333 | -44.72671 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2016535a-79e5-3c9f-924a-29496c2f1b06 | -2.8434 | -57.4696 | 2026-10-09 16:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 76a28aa3-dcf7-3f2b-8d20-fb253df893bd | -2.4623 | -56.0682 | 2026-10-09 16:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 07c58277-7d5f-3a68-98bf-55dd8add405f | -3.7718 | -59.246 | 2026-10-09 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| b5cb8778-90bd-3ad0-938a-8eeccb8b9437 | -3.1697 | -58.6244 | 2026-10-09 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 136.4 |
| d72093d7-88e3-3e23-b42c-24ca4d2fff35 | -3.188 | -58.6241 | 2026-10-09 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 5f556f05-e74a-3157-856e-4a547360c949 | -1.4118 | -48.9318 | 2026-10-09 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a74cec7b-5724-32ef-9021-f9202585642d | -13.1636 | -54.3591 | 2026-10-09 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 438.2 |
| 32bd5a2a-7340-3dc3-9e71-8e826896a054 | -2.572 | -56.1842 | 2026-10-09 16:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 893b2431-df69-38e9-9f1f-787e71aabe39 | -12.2316 | -44.7427 | 2026-10-09 16:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 8daa1e01-c045-3418-a1f9-6191b5bb1ed3 | -1.2907 | -55.7098 | 2026-10-09 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9bfb4fc1-d834-3cc9-a076-078365c7f2b7 | -2.9704 | -57.8942 | 2026-10-09 16:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 521b6bbd-aaa7-34e0-8048-f46b39add803 | -12.1948 | -44.6554 | 2026-10-09 16:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 976e864e-50ff-31e5-b411-0d4b16378394 | -8.9113 | -45.2062 | 2026-10-09 16:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 13879d9e-5a1d-30c6-909e-ec2674644d5a | -3.6435 | -59.3064 | 2026-10-09 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f668df4b-e9ab-3f7a-90f8-528c28d7de33 | -3.774 | -58.5728 | 2026-10-09 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 2b4d82ba-7d86-3461-a3fd-85d7e6ea2fce | -3.571 | -59.0777 | 2026-10-09 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| eb53b808-ea73-3b23-a051-d9e22bfda7ee | 1.6754 | -55.6266 | 2026-10-09 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d3cc3a79-12b4-3968-8550-0bf548dc65d6 | -6.0423 | -42.5859 | 2026-10-09 16:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 143.1 |
| d08f56a9-d25d-33f6-85df-8b42d527ab69 | -8.911 | -45.229 | 2026-10-09 16:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 56e79d9e-a830-30cd-9ca3-89cda6106f03 | -10.98902 | -45.39597 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 987307eb-98c4-3c27-8012-ae1b475d7632 | -7.49002 | -42.82555 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4f197d52-4dcf-3363-a980-dfbaf636ff2f | -7.41237 | -44.76117 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 17eeddc4-5e07-3e8b-89b1-ac0e6093cf65 | -10.88789 | -44.79445 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 558d1cd4-f2e8-32c7-a847-db969f4bdf83 | -5.75627 | -42.09615 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 2f07c2ae-1859-3506-b394-5a96332bb7fa | -11.05533 | -44.02312 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 9acb4f1b-bb99-321d-8fc7-d9d1fa26a241 | -9.72074 | -45.6925 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 28b6e78f-815c-3f1a-82a6-3a236fd2d7e8 | -7.74318 | -42.964 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 13ff3fb1-c1a2-39e8-a9ac-1ad27b319da1 | -10.47031 | -47.33021 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a656506b-82ac-357b-8121-8b2b96d8c382 | -10.85176 | -45.56479 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f5eac049-bf42-3b77-86d8-5d404e193b6c | -11.26421 | -46.26252 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c386f3bf-2f91-3103-9a83-de96a1c457b5 | -9.72216 | -45.69446 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 41439dec-357d-3d03-b76d-6060a7b14683 | -11.41604 | -46.68873 | 2026-10-09 16:01:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| b2982a1c-9e8d-3704-b51c-66b2ac5e76c0 | -6.49123 | -38.95851 | 2026-10-09 16:01:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 3fdc562a-7d0c-312f-8d32-0fc8bbee5ea8 | -10.31628 | -46.25881 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7539fc7c-7186-3db1-a4cd-d509f26c2425 | -10.48204 | -47.24394 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fa74580f-9e42-3737-bb0a-7a71aa2090e3 | -7.68476 | -48.32621 | 2026-10-09 16:01:00 | NPP-375 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2810f5fd-22c5-344a-bff0-490a6c0d2625 | -5.84353 | -42.68397 | 2026-10-09 16:01:00 | NPP-375 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4152dd79-9ec9-3132-b697-d4070a1e31ae | -9.94308 | -43.55415 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 53fafae3-7aea-3224-b925-494c4802495b | -6.49266 | -41.82685 | 2026-10-09 16:01:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| cd049352-e8e7-3d4f-8a31-5dce6116f500 | -11.07784 | -44.11021 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 428.6 |
| a19e0b4d-fac2-31f5-ad94-353763ad9cdd | -7.48095 | -42.83588 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 8075dd71-5530-34ae-b7ce-64e44a9d4d8f | -5.48207 | -41.21186 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0d9d30ee-0524-36d4-8e18-369f3a086940 | -7.23233 | -44.16019 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24fabd70-44f4-35b4-a1f5-033117485b59 | -9.72185 | -45.54762 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c81747e7-2c86-3b33-a3ad-d8d5a1bcd2d7 | -4.99471 | -43.16285 | 2026-10-09 16:01:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3019e38d-02a7-3776-9117-377a1557aea2 | -6.43485 | -43.68536 | 2026-10-09 16:01:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e72e7868-af75-3ad3-bec3-10bebaa89685 | -8.90918 | -45.17294 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8139b001-282c-3776-9276-341e155d711b | -6.05592 | -42.60052 | 2026-10-09 16:01:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 973ba68f-89b9-36ea-a727-36961017bcdb | -5.36196 | -42.88305 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fab3a9f0-402d-38dd-bd7e-c1713780add5 | -9.86029 | -44.8774 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ef63d7f0-b63e-3198-9fef-9f8f4b7ca14f | -9.02141 | -44.36378 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3e73cab3-adb7-36de-b25f-1f9011493ac9 | -10.49084 | -47.32093 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ce2db8a2-22cb-325c-a91c-df19c92083c9 | -9.77638 | -45.92721 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 631b4c47-ede9-3a2e-8dab-8d85e89e012f | -5.81412 | -42.62767 | 2026-10-09 16:01:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 99c9cefe-58da-31c4-8762-1a1891ef6010 | -11.07835 | -44.11445 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 400.7 |
| 5e0c6ebf-b4e9-3050-8be2-55c18fc53b8a | -7.23282 | -44.16389 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| df06ed92-9029-3c94-ae49-a06c5a6bb117 | -9.17905 | -43.39137 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| a5ba6785-4408-3750-8ebd-9ed801db815f | -6.21335 | -38.52315 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| be0a9cba-c2c5-3a0c-9991-6766023acc99 | -8.97755 | -45.96451 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 353eb2ea-6119-3d58-b275-e88e3ae738cc | -5.0772 | -36.93816 | 2026-10-09 16:01:00 | NPP-375 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 282.5 |
| e8b57dce-d150-3477-a2bc-9cf0f91cd3cb | -6.01471 | -40.96712 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| f446770e-8e4b-3f2a-a7a4-9a69cf12d537 | -6.70668 | -44.11674 | 2026-10-09 16:01:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4a61d0f1-0a08-3cf4-9e72-619b4eb6c9ff | -10.1665 | -45.35028 | 2026-10-09 16:01:00 | NPP-375 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b39184ef-e0f6-3275-a99a-071069bc974d | -7.08347 | -43.09061 | 2026-10-09 16:01:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 666ea059-8ec1-3b61-a741-f41587d0ee41 | -7.00395 | -47.69292 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| f7949fd4-afb8-36ef-962f-c92dc7341284 | -5.07777 | -36.94191 | 2026-10-09 16:01:00 | NPP-375 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 282.5 |
| 3778ecc7-d8de-369c-9b06-92ae8c1a60d1 | -10.5153 | -47.34572 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ea667852-0ddc-3839-a8d2-077df2e6fd85 | -8.97585 | -45.89885 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ba3492b9-53bf-31bf-9f0e-905af20f81cf | -6.57128 | -43.05003 | 2026-10-09 16:01:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e3041f59-3fc1-30ed-ad7e-8664b39cfcd7 | -5.95675 | -40.93986 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| fdec9958-9269-3dfc-bae8-9f00268013f5 | -9.43955 | -44.59884 | 2026-10-09 16:01:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 82d718a3-2884-3157-bad0-e2a3fb72e404 | -6.00993 | -40.96851 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 1a573834-dd43-3ebb-a60a-2c81aaeecbbb | -9.12543 | -45.82534 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 67e696fe-3e81-350a-92a6-ab5e407a3d4d | -5.72288 | -41.61758 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 08d445c4-f796-3d1c-a48f-b0d6d59fb040 | -10.50338 | -47.24261 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| ef7cbec1-f631-3d2c-a0e7-e9e626950835 | -9.61297 | -45.99349 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 23eeaab6-796b-3250-9f83-296de68491ad | -6.95687 | -45.28349 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d2477d15-5750-3355-b251-2ced346fff91 | -5.70985 | -41.65825 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 375c847b-c1d2-3d01-9fa3-de2b6b8860ac | -11.11972 | -44.01554 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 56553d33-76fa-3909-9069-ef8184a0f617 | -11.04819 | -44.06234 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| abdba411-cf55-3623-96a2-34563ce7e4e1 | -10.85654 | -45.56173 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |


[Clique aqui para ver as próximas entradas](README268.md)
