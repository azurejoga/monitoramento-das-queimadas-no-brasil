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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d7d4381-64c5-3331-a049-f78f928f2003 | -6.92226 | -46.41113 | 2025-06-24 04:25:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ff74e0d7-e41d-366b-9e72-3705ac437c85 | -8.57335 | -51.58206 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8a488a8-cda6-30de-87fb-77244c2c0b66 | -7.31056 | -45.77606 | 2025-06-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a299256-a41d-3e40-8a99-14050575c12a | -8.57422 | -51.57697 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 893ad590-3f0d-3e2d-9982-69175af86058 | -13.07026 | -48.83752 | 2025-06-24 04:25:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94b04429-710a-3298-89dc-c0c8b4cc9cbf | -7.90885 | -49.64503 | 2025-06-24 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed1c98ab-2990-32c4-8ac8-67c1325063e9 | -11.56649 | -47.91515 | 2025-06-24 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7de6368-dc83-3a75-ac84-44ce2890094b | -8.56853 | -51.58648 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4af150ae-61cc-38e5-be51-147bba30a4ee | -13.25725 | -41.32356 | 2025-06-24 04:25:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8efe9761-a815-31da-bd5b-8d6e4ff4367c | -13.42126 | -48.72704 | 2025-06-24 04:25:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d5e9effa-2089-3e65-8557-4261e731b91f | -6.25326 | -44.84053 | 2025-06-24 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 990aa74f-7f19-3fbe-99e8-c01e516e85e1 | -6.24826 | -44.83998 | 2025-06-24 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2df4c2fd-bb96-3e64-9ea0-1f388b8c2036 | -10.59143 | -49.64479 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0d2f53f-6c4b-3f74-b995-1a8131f34ec2 | -10.28259 | -47.61296 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 578a596c-f1ec-365c-9364-cb7e24b1e1b3 | -10.58164 | -49.63914 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4d76748b-d44d-3845-9bf3-0b1cdaea29fe | -7.01033 | -44.60525 | 2025-06-24 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2ced88f-602b-3c49-a006-891d097132c9 | -12.75697 | -44.40915 | 2025-06-24 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a67eb419-952a-30fa-b659-7fbff3f48699 | -8.05979 | -43.11419 | 2025-06-24 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2fba347d-36c8-3966-9706-4b32275880e9 | -10.581 | -49.64303 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 306988ee-df04-3483-a1fb-5af648b0af67 | -8.87255 | -47.2702 | 2025-06-24 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0126e4c-6aa2-3be9-879e-7a99854818b1 | -7.86845 | -47.87453 | 2025-06-24 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fd7d50a-e895-31ac-994e-ac5ba9b81267 | -9.31954 | -47.7914 | 2025-06-24 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff5de142-cd89-36cc-9e42-ee20842f894c | -13.24079 | -49.8357 | 2025-06-24 04:25:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0853fef8-a1e0-381d-aaa9-5e5fa84461fc | -11.66283 | -48.62715 | 2025-06-24 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0fcf560-6395-38f6-b406-2074e0da1f57 | -6.1736 | -47.27657 | 2025-06-24 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b555703-a705-3cee-bfc1-476df00843ba | -8.56191 | -51.5539 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 1a84c344-ce6f-391f-acbb-76711dcb3153 | -8.99183 | -49.87255 | 2025-06-24 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 932c4028-7183-368e-8bb6-9075bcdc95ee | -13.07417 | -48.83449 | 2025-06-24 04:25:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e1c51ae0-16cd-3195-9389-6acb8add64b3 | -7.43408 | -45.42046 | 2025-06-24 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ca85fcf-e661-3de1-b843-7b85c7b4ffdf | -14.0032 | -42.5557 | 2025-06-24 04:25:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab6a815b-1e63-37a3-9e11-7ea95f61b5fd | -6.95936 | -42.93205 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8b88937-6d76-3d5d-a6be-86356b9e3485 | -7.05808 | -43.92122 | 2025-06-24 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8117f558-528f-3d42-8f3b-ff246e0dca9d | -10.08083 | -52.7457 | 2025-06-24 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cb1a54c2-040d-3ea6-9ef7-669cd2e2d79e | -7.34289 | -45.32966 | 2025-06-24 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1a17ab13-d5c1-37ca-a327-fe3e6cd0244c | -6.95642 | -42.80227 | 2025-06-24 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d1b7eedd-f13f-3c97-8344-e96011258003 | -8.24859 | -44.95718 | 2025-06-24 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6693cb3d-b5f5-375a-8b74-81a5aaa8641c | -11.09582 | -46.65185 | 2025-06-24 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0bddd728-12bb-3512-8da0-7e052e5488a2 | -6.70943 | -47.39095 | 2025-06-24 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edd0724c-db92-31f8-b818-65364ef5684e | -8.55709 | -51.55832 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| d75f2554-9654-37b8-8982-64e3a973c92d | -12.79843 | -48.73381 | 2025-06-24 04:25:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6fc7c09-8a20-3ed5-a022-95b696073bde | -12.80234 | -48.73077 | 2025-06-24 04:25:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cec4c76b-d1c4-37ca-bd88-75523115781f | -6.92557 | -46.41165 | 2025-06-24 04:25:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f3983907-6ce2-37d2-ae58-54b81588d2e2 | -7.33955 | -45.32914 | 2025-06-24 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3fe19576-4009-351b-8def-ce6f13a42d13 | -7.44641 | -45.57791 | 2025-06-24 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd74cbfe-a598-3c92-9501-d927c96d3874 | -10.87055 | -49.54259 | 2025-06-24 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daccacfb-0d4d-3e3c-95ed-a88367dbc863 | -7.86788 | -47.8781 | 2025-06-24 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5871980d-ab57-352e-b75a-f36233ba36e6 | -7.85815 | -46.65987 | 2025-06-24 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 283e2175-37bb-32c4-835e-b269ad11c419 | -10.51239 | -47.57805 | 2025-06-24 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebfd2305-b3ff-3bbe-961e-8cf9a0ae5734 | -11.58349 | -44.68502 | 2025-06-24 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b799c1bb-4dd2-32b5-a0ee-172c40584749 | -8.98469 | -49.87135 | 2025-06-24 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d74c7bf6-288a-3925-bd3d-d1d8d63843af | -7.32659 | -43.222 | 2025-06-24 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d166f6b-fb25-36b6-90bc-c5069a8d2b64 | -8.57027 | -51.5763 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b815303-7823-30f8-8f89-dabe9f32c5f9 | -8.58041 | -51.58842 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 241ac0fa-f42d-35d7-b208-b03b2ca519dc | -8.24462 | -44.96036 | 2025-06-24 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15623965-ff66-3261-ada4-7189281fb0e7 | -7.87123 | -47.87864 | 2025-06-24 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65f76188-7c49-39a2-94d0-66a278681ef2 | -6.63963 | -47.85161 | 2025-06-24 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b3cb4f3-2045-3db7-bcf7-994a3a5f0c02 | -11.37167 | -43.7477 | 2025-06-24 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70811e5d-d190-3d51-b20e-46deac145d6b | -6.63905 | -47.85521 | 2025-06-24 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f676327f-e364-3448-a530-b3043a670892 | -10.58448 | -49.64362 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8719d483-6696-30d9-ad9d-a67164bc65cd | -7.21086 | -43.09687 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a7c4f23c-b13d-30c8-ae6d-76d6d2e9e325 | -13.31162 | -47.13834 | 2025-06-24 04:25:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87e8bdae-3a48-3a49-ba10-641eb7c94c7e | -7.09542 | -44.36969 | 2025-06-24 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d65b3cb-9e5e-3861-a5ce-b7dbefbde6fd | -7.4019 | -43.87043 | 2025-06-24 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d091f85-85f5-3ee3-ab77-fddce176d1ae | -8.71461 | -47.85334 | 2025-06-24 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48a4e554-3834-3a35-b6be-8624a296b6f6 | -6.63568 | -47.85466 | 2025-06-24 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1febc54-3794-3809-b913-894693c6f53c | -10.87337 | -49.54701 | 2025-06-24 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06afbfe4-13a1-3012-9ab9-378d42456307 | -10.27984 | -47.60892 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f25d7aa3-7c16-3bd5-a5c4-d15f4f7c3ed5 | -9.41542 | -48.41896 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5178bcd6-0dfd-356b-83bb-c0dfc95dea5f | -9.39841 | -48.4385 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef69d590-c575-32ff-b2b2-3938faeb26dc | -10.60086 | -49.64123 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d5c6f8a-bedc-3c30-89ca-756e3b5c2048 | -12.31847 | -50.06255 | 2025-06-24 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78802a0f-4766-307c-9542-8f5562330e46 | -8.56104 | -51.55899 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 94eecf10-612a-3d22-a39f-43f68f7ed42b | -8.58915 | -51.58485 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 433627ff-c843-3783-9538-9e7b39c525a9 | -10.58922 | -49.63642 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac17f108-2c95-3d20-b109-c9f8210cf8d7 | -8.26747 | -47.69824 | 2025-06-24 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0e348cb-c50f-3367-afc1-108a5967ace8 | -7.32617 | -43.20019 | 2025-06-24 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cd7de995-215d-3b84-abb2-8e3d5dc221f9 | -9.40548 | -40.31588 | 2025-06-24 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1547732a-227d-3ee0-83c0-cbdef04e1d64 | -7.20229 | -43.10427 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1ec3b8e3-0914-348f-ba2e-ca8a772fd5d0 | -11.24452 | -49.48952 | 2025-06-24 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2f87023-a977-3ca7-a00a-a8551ede5410 | -7.20958 | -43.1054 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 71b2eeb5-0d75-38e7-897f-8bba59290060 | -7.45567 | -45.51799 | 2025-06-24 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 761bb53a-e135-3587-bb64-c948da0938b8 | -10.06436 | -49.65897 | 2025-06-24 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2179e48d-5980-3e6c-8bd4-e47a0b3e87d4 | -7.43352 | -45.424 | 2025-06-24 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d3f8d11-0437-3eb4-b545-dbd21a7e9b49 | -7.2427 | -47.06997 | 2025-06-24 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d5ae9da-1c7b-3ce3-879a-0af14d5d313b | -8.06043 | -43.10981 | 2025-06-24 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 05aae83d-0ad2-3a87-a3d8-faa10a58364b | -10.57682 | -49.15176 | 2025-06-24 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42cc6c4d-479e-34c6-af85-a241fdbc46c9 | -8.31169 | -55.10796 | 2025-06-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fff85906-5165-3b8f-88be-507f1e8ba1a8 | -9.64683 | -48.56867 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe4b18ff-59e6-3415-bab3-11e53a8131a6 | -12.79901 | -48.73023 | 2025-06-24 04:25:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9781cf28-a882-3b51-9c49-b617a481734e | -12.75635 | -44.41346 | 2025-06-24 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3abb0b78-e7f9-31f0-a0df-ef79c6fe6014 | -11.24733 | -49.49392 | 2025-06-24 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 639f7247-b129-3e93-b829-511bdda1f7d9 | -9.93735 | -50.63622 | 2025-06-24 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d589746b-1364-3b19-b1f7-46000627675a | -10.58511 | -49.63972 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3af7e8af-286c-3901-b760-59e6952707bd | -10.58795 | -49.6442 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8ac1f15-d9a8-370b-9ce4-e75cdf72d407 | -9.1361 | -47.57811 | 2025-06-24 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 982b07a8-2c4f-3510-a7ee-baac036934bb | -10.49454 | -53.57051 | 2025-06-24 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 151d9974-7108-3e31-a3cd-282235572a39 | -8.55796 | -51.55324 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 7d1cbacd-e521-380e-bc5a-b9402744bad2 | -9.7908 | -48.56564 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb6ea1d6-5594-37c6-8886-0eed3ef8d8a3 | -10.58732 | -49.6481 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f96f49f-4fc6-3cd9-acdd-dbe382818420 | -7.00636 | -44.60833 | 2025-06-24 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README14.md)
