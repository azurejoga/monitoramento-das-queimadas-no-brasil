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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31765c0c-569c-3628-bdfb-3323dc5c26b8 | -7.09206 | -41.79314 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| f81fc0df-8fe3-38ae-a7f5-9857fcca5024 | -7.55689 | -45.20089 | 2026-09-14 15:48:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4383d9c-71e7-35d3-8c42-d3fdd7536ffb | -7.0898 | -41.81556 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c6334988-03d0-3b5d-830e-f2f4e60fd16c | -7.10549 | -41.7756 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 3a4fdfea-82c3-328b-895c-5ee18e4c11d3 | -6.24759 | -41.95944 | 2026-09-14 15:48:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 9cdc0850-e9cb-379c-a548-c9908f9d19b3 | -6.05569 | -36.38358 | 2026-09-14 15:48:00 | NOAA-20 | CERRO CORÁ | RIO GRANDE DO NORTE | Brasil | 2402709 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f334e642-9d11-36c1-a29d-624d85955b1a | -6.25886 | -42.67067 | 2026-09-14 15:48:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c6d01745-eb0a-3f6f-a295-e2cf9809fd3b | -7.97311 | -44.02727 | 2026-09-14 15:48:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7fe10c2e-e6a7-3aec-9ef3-498547b9e1a8 | -7.10506 | -41.77247 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 39.5 |
| 3e693b33-8352-3573-b7e3-2479424cb089 | -8.57057 | -44.49456 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b8a08368-a90a-3e25-b16d-b95b81b53471 | -6.43712 | -44.95961 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1c1e7dfa-9992-3b93-bd13-249d5c33d1d4 | -7.97854 | -44.02166 | 2026-09-14 15:48:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3555f657-99ce-3808-821b-6562bd58162b | -9.85398 | -45.9913 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 00e5a2b0-a404-3be7-a27e-2c275161121f | -9.93956 | -45.77495 | 2026-09-14 15:48:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a05c5216-704b-3abf-a40c-a603d396daab | -6.53833 | -44.08699 | 2026-09-14 15:48:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f307593e-f564-3b92-b6ae-067567bbc7b2 | -7.13313 | -42.09938 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 054d8727-a496-347e-a1a7-bf62da08c25c | -7.47206 | -45.97625 | 2026-09-14 15:48:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf94bfd4-c0e1-38ae-83b2-04fd633da76f | -7.02216 | -44.6363 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8f6b6751-343e-328c-9d78-a1bae41f9f19 | -4.9796 | -37.39006 | 2026-09-14 15:48:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 796b72ba-5ad9-30be-a640-2183670f0946 | -8.41234 | -44.74617 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 656dde49-6dbc-37dd-a5f3-c604c1148673 | -5.41583 | -42.22868 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 229112ea-1fd6-31f0-8d0e-f3a18d2f00af | -3.51437 | -39.4228 | 2026-09-14 15:48:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 89ccb532-d850-3f02-b5bb-4cb5214285a3 | -5.63701 | -40.85136 | 2026-09-14 15:48:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b5ccd68b-8a5d-393c-946c-0dd5a961a4f1 | -6.26471 | -42.67311 | 2026-09-14 15:48:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| ef2df0c3-5838-3f9e-a1a5-401ba1a221cb | -8.42052 | -44.7599 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2c815142-2394-3e52-ac96-50276f1ab0a2 | -7.14636 | -42.1177 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 595107d5-01ac-3769-867e-7fb958d665bd | -7.01618 | -44.6286 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 279f3b3b-1277-36ee-84b5-e31a386d8c8d | -3.97859 | -42.47969 | 2026-09-14 15:48:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0859ecfe-63fc-380a-99bd-0e565f0421da | -5.6418 | -40.85103 | 2026-09-14 15:48:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4dd4ba0d-8a43-3e9e-9a66-dfda499892f2 | -7.11156 | -42.09582 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| cbb71cfd-57d5-3184-a48e-8192c7813fdb | -8.63275 | -44.45327 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| adb27b0a-d309-313d-bcee-2f037ddacb37 | -6.95126 | -44.47318 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f06ec860-fe25-3472-93ac-ea99a994e445 | -3.65406 | -41.07306 | 2026-09-14 15:48:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 967ad6e4-b721-367d-b728-e1d640aef176 | -7.28979 | -39.30939 | 2026-09-14 15:48:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 56a502c2-5406-3eaf-a8d6-383557b69b44 | -7.24714 | -37.11835 | 2026-09-14 15:48:00 | NOAA-20 | DESTERRO | PARAÍBA | Brasil | 2505402 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a6b53cfe-20c6-3b96-b629-699423a5b3ef | -5.55402 | -44.11327 | 2026-09-14 15:48:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4469d7ab-985b-36d8-977b-a6ec2cb42f9b | -6.2393 | -45.97934 | 2026-09-14 15:48:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 74175d88-5476-31d4-aac9-c07f00090ca6 | -6.25109 | -43.44121 | 2026-09-14 15:48:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0f237e1b-0fc9-3531-99ac-fa6cc1e6e803 | -5.55994 | -44.11262 | 2026-09-14 15:48:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 85a70436-9b77-3c84-86e8-9696711f8019 | -7.19717 | -46.13799 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b14d809f-5484-38af-936b-dc6958b40552 | -5.40844 | -45.86297 | 2026-09-14 15:48:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 16186467-738d-3aa3-bc5b-05c42d0d5c9b | -7.32916 | -41.42752 | 2026-09-14 15:48:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| b79530a9-d5f7-37a7-a6f5-d1041afa3466 | -3.24602 | -39.77571 | 2026-09-14 15:48:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2f61352f-c38f-39bd-ba47-dbb677864b17 | -6.19801 | -42.44999 | 2026-09-14 15:48:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2b5ed2ec-2038-38dc-bc5b-bbbfdcbeddd9 | -4.95645 | -42.69224 | 2026-09-14 15:48:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6190c3a0-f51c-39d6-ad42-3fc5f298ff0f | -8.41841 | -44.75746 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4e9c7ba7-2bc6-32ae-a786-720e01ab1563 | -6.81872 | -42.98724 | 2026-09-14 15:48:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8e9560ce-9800-36f9-9409-28a03c7886c6 | -7.08879 | -42.12563 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| e89a1ebd-28d3-34a7-a5cd-06a80bd119d0 | -7.48466 | -44.8899 | 2026-09-14 15:48:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3f987c87-6196-3cd4-900b-cedc248cd8c8 | -6.85529 | -43.75459 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19d82a4c-8649-3a64-8277-cfcffeddb28e | -7.11641 | -42.09499 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3acb8b6a-4137-3c30-828e-f4f2a67dd67d | -6.36936 | -39.3143 | 2026-09-14 15:48:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 658b39a1-4cb6-324c-a523-c40c1b8d51e0 | -7.09182 | -42.10858 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1b48de79-7a93-3e23-9d55-00db3a0f3470 | -6.28288 | -42.6846 | 2026-09-14 15:48:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1d100a2d-bfba-3171-b9bf-847ee6045b83 | -10.05293 | -45.48937 | 2026-09-14 15:48:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d495db9e-cd38-31dc-9513-ba3997a054cf | -7.06081 | -37.96535 | 2026-09-14 15:48:00 | NOAA-20 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 1e93e51c-ecd6-3587-bfa7-e187b1be8099 | -6.42116 | -38.38049 | 2026-09-14 15:48:00 | NOAA-20 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7ec28607-1f66-3baa-adc3-c629cc2222ae | -6.52928 | -44.08864 | 2026-09-14 15:48:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 58783c55-f0ff-3657-9cec-7e10f88e9bc2 | -6.56725 | -43.15893 | 2026-09-14 15:48:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c62c9c4f-bd7f-3d17-a53c-1ed612856fda | -9.85197 | -45.98732 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cc07b1f2-93ab-3654-b3ed-8a52c0962c63 | -6.23611 | -45.9812 | 2026-09-14 15:48:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b46ba4c3-625a-369b-920e-9b57d90b7846 | -6.65891 | -43.65807 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| b17fc3aa-ea8b-3496-8dd9-f92f5b537fc0 | -7.47148 | -42.11097 | 2026-09-14 15:48:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 46984035-74c8-350a-9ba2-943a36c52730 | -6.67 | -43.65257 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2d2678d8-a221-3583-a771-c7e776d8aa40 | -3.74089 | -40.39156 | 2026-09-14 15:48:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0f250a29-0e7f-3c99-9b1f-ba2a0d8fac14 | -8.03159 | -38.99803 | 2026-09-14 15:48:00 | NOAA-20 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 18.0 |
| f7163850-96d9-3547-ace7-ede9fa599b49 | -7.71626 | -37.02259 | 2026-09-14 15:48:00 | NOAA-20 | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d38cf8cf-ee40-3bb2-8cfc-c463c9887fc1 | -6.79061 | -43.76267 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2e3978b-cc8a-30c6-9f06-ca2ef8e05ba4 | -7.19637 | -46.1319 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| dd5dbed4-5c75-349a-aa44-99bce211a644 | -7.26815 | -44.12233 | 2026-09-14 15:48:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d40ad56-7bf1-37b9-b5e8-d3ff69b4d510 | -7.09598 | -41.78314 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 3e045f6f-2fac-3458-b68b-eb6121498e0b | -9.86371 | -45.96631 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 289f7a73-6017-3dba-9c5c-3e0688520d90 | -8.57326 | -44.48907 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3e913d3e-ab0a-3235-94c1-a314f8779a5b | -5.9859 | -44.86108 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 05c6b03a-dc61-3d94-96f0-5f20434d58f5 | -8.57892 | -44.48303 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c170e975-3286-35a0-a377-52a22be954d0 | -6.16284 | -45.1837 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 921380e7-d96b-3e5b-a9e1-19c224eb9e28 | -8.70464 | -39.60493 | 2026-09-14 15:48:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 7c1ff128-6ee0-3067-9e5e-ff5f2818e8f4 | -7.10031 | -41.77624 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| c640a194-627d-3a79-86ee-833b3464711e | -5.81926 | -42.74422 | 2026-09-14 15:48:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b000a46c-3406-3515-b099-37446ce1a763 | -8.07887 | -44.02257 | 2026-09-14 15:48:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 77431be8-2531-392b-bae6-02f0eca8e8c8 | -6.41769 | -41.55931 | 2026-09-14 15:48:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f47e5102-bfd3-3d28-8b8f-8ab820fe96ac | -3.78427 | -40.77442 | 2026-09-14 15:48:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 8925d6ef-6666-3f7b-ab89-e0ab7e91a8e8 | -6.16449 | -35.14432 | 2026-09-14 15:48:00 | NOAA-20 | SENADOR GEORGINO AVELINO | RIO GRANDE DO NORTE | Brasil | 2413201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 8da6179c-eec5-3c82-8a91-f06c6d10282a | -6.04512 | -46.05641 | 2026-09-14 15:48:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 9b8e7cb9-8aee-3be2-87fc-fe21c3a4ab29 | -7.19474 | -46.11944 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 89e47ede-94ed-3692-9bc5-0e30f6fa0eb2 | -8.32251 | -36.75071 | 2026-09-14 15:48:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da602508-116c-3705-8bd8-2a4eece9a955 | -7.15165 | -42.117 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| a05ab03c-486c-3246-a6df-0dcadbeb1c64 | -5.99089 | -44.04622 | 2026-09-14 15:48:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff78d9d6-c3e6-36de-8ff9-fec2d6b12e59 | -7.3332 | -41.42855 | 2026-09-14 15:48:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 67b7ff77-37ca-37a7-83b5-276a770f9a97 | -6.57322 | -45.32025 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b9eaf9ca-8d81-3f7b-a8d0-ad212dff7ede | -9.84629 | -45.98644 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d8b936cd-00ca-3aa8-998e-71d0b749e6c5 | -4.45822 | -39.35548 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| b26b360a-a8e0-3509-a0a1-ceceb642b432 | -8.62455 | -44.43881 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 6405313a-58ff-39c7-b35d-17b8a473f756 | -7.26704 | -44.12519 | 2026-09-14 15:48:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c5b00221-4885-3b65-a349-3ed10fc252bf | -6.12481 | -43.51264 | 2026-09-14 15:48:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3bbf5b6-8a94-3925-a550-27666590b941 | -5.9843 | -44.85991 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1d95df4c-e19a-3e9b-9c58-b3f29687dff6 | -5.40765 | -45.85708 | 2026-09-14 15:48:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ec6ab37f-a93f-3301-a64f-5dafeb0b3b18 | -6.27697 | -42.68185 | 2026-09-14 15:48:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 185b1a4c-d73e-33ab-8b4b-d576c82484a7 | -5.28822 | -44.4391 | 2026-09-14 15:48:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b037d27-36d3-3d0b-9162-7f90bc50ed26 | -6.44052 | -44.95787 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README91.md)
