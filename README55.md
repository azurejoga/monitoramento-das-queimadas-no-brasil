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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6976b420-46e6-3162-a860-e5fe14683639 | -6.64271 | -41.99565 | 2024-10-05 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c99ecb89-c03e-3efd-bd47-aedd05a93f2d | -6.64216 | -41.9992 | 2024-10-05 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ce68a984-7a89-38aa-bdce-4f2ea1220163 | -6.6399 | -41.99158 | 2024-10-05 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 21fc4ee3-cca1-3ced-a01b-af2c060a0426 | -6.63936 | -41.99512 | 2024-10-05 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ba2896ff-1cdf-3e33-a5c6-46e8fd9892c1 | -6.63881 | -41.99868 | 2024-10-05 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2d0fc762-02a7-3c9d-8b5c-95e301a07270 | -6.636 | -41.9946 | 2024-10-05 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6bdf9b33-7e0a-391e-a1db-d2043232a630 | -6.63545 | -41.99815 | 2024-10-05 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 57708c9f-626b-35fb-bc5e-655cb8759e76 | -5.20375 | -37.6279 | 2024-10-05 04:12:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 87da113c-ae18-3824-8574-f3840a2fd0e1 | -5.17738 | -41.29558 | 2024-10-05 04:12:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 81e71342-9618-37d8-b7dd-642ee75e8d0e | -5.17399 | -41.29504 | 2024-10-05 04:12:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a9f1adea-7720-3574-a351-6f58df41c9f3 | -5.11848 | -37.5645 | 2024-10-05 04:12:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fd12e41e-ef6a-3ec6-8292-43f36d56249f | -5.11794 | -37.5681 | 2024-10-05 04:12:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a2210068-53cb-3fc9-9fa8-6349346ab07d | -5.11385 | -37.56749 | 2024-10-05 04:12:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 865b7b95-93ca-3903-803b-946d491c8af4 | -4.86515 | -38.43724 | 2024-10-05 04:12:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb2c7dec-ac9c-3103-a315-a37b70f3b005 | -4.8613 | -38.43667 | 2024-10-05 04:12:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20279a54-14ab-37fa-81bc-9653e97b0cd5 | -4.03021 | -40.39399 | 2024-10-05 04:12:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0679eede-f1c5-3ee0-b012-fb8a775e7662 | -3.79918 | -41.5858 | 2024-10-05 04:12:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 99a707cc-f35c-3656-bce1-733f41db63ea | -3.79863 | -41.58931 | 2024-10-05 04:12:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 323a8faa-a155-35b2-9c40-92eed98ff825 | -3.79808 | -41.59281 | 2024-10-05 04:12:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 72bd7b57-a74b-380a-9d11-08f96a4be37b | -3.79753 | -41.59631 | 2024-10-05 04:12:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b6ec9773-741c-3055-8278-61f1acb42a26 | -3.7792 | -38.66132 | 2024-10-05 04:12:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 14e5888a-51e5-396d-9812-41eb90785a5b | -3.77869 | -38.65883 | 2024-10-05 04:12:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2526a517-8c1c-3073-8541-0cd22602726a | -3.778 | -38.66328 | 2024-10-05 04:12:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4304c0d4-25e0-3800-81fb-cef868b5eb49 | -3.77511 | -40.4168 | 2024-10-05 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd776418-b406-3633-b547-e39d9717113e | -3.76362 | -40.42268 | 2024-10-05 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 009c2602-96cd-3e1d-a762-3637538a96b5 | -3.76304 | -40.42641 | 2024-10-05 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fabe1f8d-9118-3004-9b45-302448e7e296 | -3.76247 | -40.43015 | 2024-10-05 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f0430f0-91f3-3bdd-ad9c-b1684a6741d1 | -5.74875 | -43.15251 | 2024-10-05 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad8a0bb5-e29c-3f1c-b25e-79c341a1e045 | -5.69004 | -43.15748 | 2024-10-05 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 41e405db-6fb6-33a9-9673-326da2a2c62b | -5.68672 | -43.15695 | 2024-10-05 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4092c066-3082-300d-af70-50a59dd74aad | -5.68617 | -43.16042 | 2024-10-05 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 679012b6-9fd9-3171-a1e1-3021daed7c69 | -6.27853 | -42.77023 | 2024-10-05 04:12:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 80e2401e-9d1f-3ea0-9a1d-e70f86815f4a | -7.22578 | -43.33252 | 2024-10-05 04:12:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b3ae08d1-b56a-3fff-87e6-9b2562a95596 | -6.8476 | -42.8314 | 2024-10-05 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e4b1b8e8-fabb-3479-9f91-57f668f7babd | -6.40709 | -43.0967 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8aab01a-8432-3312-8106-42126688e8fb | -6.40376 | -43.09618 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd320acb-2fb0-3472-a4f3-e6abbbdb44d7 | -6.28349 | -43.25798 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0185a20b-dde6-3eb0-a2a1-9fb1dcfceacb | -6.2797 | -43.02274 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6ecbe23-d365-3522-92d4-353d572a7f3a | -6.20262 | -43.27372 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d097a8e5-d122-3def-b9b2-9886728f0619 | -6.20207 | -43.27719 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e54cffa4-520d-38da-a386-cb993b131b14 | -6.06632 | -43.08904 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7219d1d4-ef11-31d4-8979-b4ef4b0209ab | -5.64978 | -43.24365 | 2024-10-05 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24c3d24f-d0c0-3e77-b0c7-b23d6fe245f8 | -5.64645 | -43.24313 | 2024-10-05 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0744b704-9b79-3dea-8fcb-5dd86f2a4194 | -5.10826 | -43.32598 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d0d2ca7-b8a6-3a4a-ac45-3c50e16a0437 | -4.89248 | -43.19888 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66f56f1a-430c-330d-a230-ea2f2c264056 | -4.69391 | -43.19274 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fe5858d-17be-35d8-8141-db9fcb930730 | -4.33464 | -43.06475 | 2024-10-05 04:12:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d2760c4-03f6-3158-b19a-4d67b160c20e | -4.01196 | -43.24694 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b652135-f622-35d0-85f4-14568897d8dc | -4.00862 | -43.24641 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a751b259-18c8-3286-899a-360bf157bfea | -4.00807 | -43.24992 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcf03253-cdcd-3fb2-a254-b2f843a8c23f | -6.68463 | -43.99222 | 2024-10-05 04:12:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2c769ae-d5a9-3e96-a018-270f93f437a5 | -6.46759 | -43.41928 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bda6acf-a59a-3de6-84ff-632fead12a75 | -6.41437 | -43.43227 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be317564-7722-3744-aa54-c0eaca6cf24f | -6.29468 | -43.85096 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaa733c2-2159-34ab-bb16-0daa165b4cb1 | -6.29071 | -43.44501 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05148397-b932-399f-85e3-3d510a6b2666 | -4.73534 | -43.59396 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db6352aa-c493-34d1-a283-d921dfbda242 | -4.51807 | -43.86928 | 2024-10-05 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9481f597-5894-3c85-a02a-f662a7298af2 | -3.47667 | -43.36035 | 2024-10-05 04:12:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0f33dff-8629-32e6-868d-2886584afe1e | -3.46996 | -43.3593 | 2024-10-05 04:12:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 819343d0-fd5c-3be1-833b-c4ebe2096ec1 | -4.94884 | -43.77655 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 04e96052-6acf-3afe-be64-40f3ff3bdb3a | -4.94827 | -43.7801 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a9b2eb86-7483-324f-8083-cf68cee2f287 | -4.94548 | -43.77603 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c4a9340a-bb15-3391-bddf-efc31e467c9e | -4.94491 | -43.77958 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b22945ce-4f84-3fbb-9f1f-d25967c875ec | -4.94098 | -43.78259 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 012dd0d7-52c8-3e1c-bb60-d83da2629cd5 | -4.93204 | -43.77386 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2a79539-d488-3b7e-a433-08a718daac97 | -4.89581 | -43.19939 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dad5b1ad-6034-39bc-8659-f27c774f5762 | -4.81788 | -42.76786 | 2024-10-05 04:12:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70a8c91e-4dba-3334-8c80-0ca6aabd05e2 | -4.81069 | -42.77029 | 2024-10-05 04:12:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5080853d-0747-3501-8286-1b8e1af402c5 | -4.79812 | -43.79614 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acf715fb-0944-3b09-9f55-dcd898d39afa | -4.73478 | -43.59749 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e61b13f-6441-3a4e-89de-4a0c148669e1 | -4.69446 | -43.18925 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cafe389-d0ea-300f-a9f4-5faf84c159ad | -4.69113 | -43.18874 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ba84c09-b194-367a-96c0-260dd0be9b14 | -4.66087 | -43.75992 | 2024-10-05 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2dd67abf-8131-31a1-800e-9fa8c2bb8890 | -4.0203 | -43.2375 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0316e9df-bcab-3244-bc44-684e77a6bab3 | -4.01864 | -43.24799 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87c4d7cb-d172-35fe-aecc-782ada99021c | -4.01809 | -43.2515 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a93921f0-dfe4-3ebe-a774-eb3b8e15754b | -4.0153 | -43.24747 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fd0ad2b-68be-357c-8365-f358cd2f3343 | -6.28635 | -43.02378 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07718fd5-5e7f-3f02-8329-11babffcf526 | -6.28466 | -43.01286 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e348398d-dc5c-3972-81a3-be1798d8ba47 | -6.28412 | -43.01633 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bd25a3c-baa4-3dc8-8656-35e057e5ebbb | -6.28404 | -43.2545 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c14596de-b288-37eb-820b-c65a386b879b | -6.28303 | -43.02326 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d5379a2-2c19-30cb-a4c4-21de76d4258f | -6.46973 | -43.36253 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a057e43-c5c9-3362-a62e-0f260a9b3dfe | -6.4664 | -43.36201 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4206836-2b53-3243-b409-8c98208181fb | -6.44219 | -43.12695 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a5af4fd-1ee9-35f1-b137-04d9767da331 | -6.44164 | -43.13041 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34977066-de73-3a20-a74c-9ef27ad33a4e | -6.41715 | -43.43626 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4afa02e3-12b8-3988-a40b-fe9ab5c1afdb | -5.05366 | -42.66713 | 2024-10-05 04:12:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25c0eead-4508-34d0-b2c2-c56fa1a3d875 | -5.05312 | -42.67059 | 2024-10-05 04:12:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c91f267-e853-3386-a7e6-60dc1f84cd40 | -4.81401 | -42.77081 | 2024-10-05 04:12:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2c3ae76-da03-3f93-94bc-770a1699fc71 | -1.95625 | -47.87599 | 2024-10-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e95c0422-db18-3212-8400-dd252179754a | -1.26561 | -47.66539 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84b090b4-9fd7-3340-9d43-a74a609dd4b8 | -1.26499 | -47.66936 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fea1810-a7fe-3f0d-83bf-5987dfea5e83 | -1.26134 | -47.6647 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e414c4f3-92b2-3c47-bedc-626f2e96f8cd | -1.26072 | -47.66867 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 339a29fb-bc84-376c-bb7c-d243a09c14fa | -1.1987 | -46.58471 | 2024-10-05 04:12:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a42da24-2d9e-3e49-8bc2-0e024d60319f | -1.1979 | -46.58983 | 2024-10-05 04:12:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 569464fb-49b4-34a5-ad6c-c2efa4be9a4e | -1.19391 | -46.58921 | 2024-10-05 04:12:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 888e9f10-bfa6-3bc1-a641-d701e42ec870 | -1.18912 | -46.59369 | 2024-10-05 04:12:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 930b4cfe-3858-3851-99cd-37d21cd4d2de | -1.16602 | -53.78559 | 2024-10-05 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README56.md)
