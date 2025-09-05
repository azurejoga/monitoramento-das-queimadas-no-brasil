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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cea5f64b-09bc-3a4d-964c-b01e2bb8ca8a | -6.25245 | -43.29029 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f12b294-38be-35c2-9c72-ea0df403f894 | -7.90297 | -44.93294 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ad34d85e-7974-3f28-a2a6-0f3cf85a9c72 | -5.86194 | -45.65007 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc907c0d-c391-30f0-84a7-8d4a1f91300c | -7.88615 | -45.28551 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9d5a419-00a6-3fa0-acc5-11a2b656f94c | -6.16371 | -43.18402 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 618310df-29f6-3644-8895-73548ef19a59 | -7.64221 | -44.75716 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0611035-4b9c-3377-af94-6af67f2d9aa4 | -6.89945 | -45.18801 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5795527b-2c90-3599-8302-34c9844a96c7 | -6.86776 | -44.83417 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eaef209b-b10b-3c9e-b839-5bfb39a59534 | -6.22504 | -45.64183 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cb097db-8b16-3d34-94e0-2c9850c044aa | -5.43716 | -42.8657 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e1eba5f9-75aa-3e4a-a1f9-e5bab472ba2d | -7.04983 | -50.85648 | 2025-09-05 04:34:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a663084b-e3ac-3737-a430-faaecd9c69d8 | -6.55003 | -43.90993 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d81b8677-575f-33c5-a258-5efc3a81dfc6 | -6.0046 | -46.68732 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4abe3370-1e52-38c7-a9dc-cb88a0803d74 | -6.01824 | -43.70516 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acb4bb34-7ce9-3f37-bd2d-1d34e8400ab4 | -6.91072 | -45.18563 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4657b61-d056-3806-9bce-5bc10fba00c5 | -6.69966 | -44.81844 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6e51a57-a256-3445-870b-c0078357b55c | -5.38066 | -43.24471 | 2025-09-05 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55993ac4-3907-3e90-a6ab-608d0159cdc1 | -6.87523 | -45.57826 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a70078b-e545-3b7c-8c48-cbfaf754770d | -6.27173 | -52.81895 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 41d28ec8-037c-3f58-a023-5ea3ccff9f32 | -5.75943 | -45.1734 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03ff2f01-17a3-38b8-8274-3a6ca6e359ee | -6.74636 | -45.93099 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4971195-fc4e-321f-9d1e-27594f9cd125 | -5.76747 | -44.86374 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 369f0d07-d28c-3f84-8ba3-2128b67a3486 | -7.57858 | -44.68228 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76f03a74-43b9-3b8b-aa19-29f459c29b66 | -5.7633 | -45.28924 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63f4e02c-6a7c-3942-ab45-49c887d9bf2e | -6.59451 | -44.5532 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| aba1d833-861d-3144-a8dc-e700c53ce18b | -5.8731 | -46.03079 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b2a04f4-7fac-3e7c-9bb6-9088d9cd2122 | -6.87639 | -45.57057 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 892960a9-e5c8-3081-ac63-d7fbafdfbfd9 | -6.30906 | -47.76841 | 2025-09-05 04:34:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0cb8d1b-c2ad-3a56-a455-1d27221bde10 | -6.07075 | -43.43398 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 254df5c8-3c63-30ef-a596-e63ac45c9865 | -7.07385 | -46.19827 | 2025-09-05 04:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c511017-0577-360b-9b70-a543a1db80d0 | -6.26955 | -43.49693 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3275bad3-7cb7-3b3c-adfb-2c6940135fd8 | -6.20364 | -45.04792 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ab1b3b3-f4e6-3ced-9635-ee5957d333cc | -6.33635 | -43.55798 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 138942d2-df72-368a-b281-2b09bef26fa7 | -6.2299 | -45.16137 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a9b8907-cd70-38b0-81a9-3d4942457c8b | -6.21725 | -43.55748 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1694d18-56cd-323b-a9dc-3bd90568c656 | -4.74711 | -43.52997 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebb68690-d820-390a-8689-79c2a41688c2 | -6.39353 | -44.69641 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b225712-6a5c-346e-9319-ffe0f736e05f | -6.26883 | -43.50174 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 673697ec-dd88-3276-b13c-e626c2f190ff | -5.95645 | -46.16631 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5919995-0204-33b9-87c0-0a3634c491cd | -6.64996 | -44.0928 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4933d89-8756-3fb9-95fc-fe000e9bf273 | -6.34213 | -43.38398 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b937405-f822-3805-9d76-30e37262d7b5 | -6.90007 | -45.18398 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a577920d-7508-330c-ad3d-a1987d5ea9d0 | -7.54684 | -45.35464 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98c81d77-bc50-38ba-885d-f853ada585bf | -5.70104 | -45.17723 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 256fed4b-d0ff-3486-bd3a-a4de547fb3a7 | -5.79468 | -45.62795 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7aa30d09-a555-368e-a544-2911af79134f | -6.61743 | -43.97729 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65a6b608-e2d8-3371-8c5f-1cd38e375da1 | -6.25399 | -46.11755 | 2025-09-05 04:34:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b93f8dd-fc64-325c-b9c7-47da8e468b2c | -6.20361 | -43.34616 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38ce2426-9980-390a-a30a-67b7a608fc8c | -4.4858 | -47.67917 | 2025-09-05 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f24bde-1734-377d-b431-9603f4c857f1 | -6.36833 | -43.02555 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5cfbd3c-fee4-303d-94f0-82a8ad6d76cd | -5.751 | -42.74958 | 2025-09-05 04:34:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 27f617d3-938c-31bd-9120-676befd0eb8b | -5.89619 | -44.16361 | 2025-09-05 04:34:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d046352b-20e9-3e35-9b01-3c34fdbb3223 | -5.60191 | -45.0268 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 366fc806-2af7-3fc3-9f4d-144d2f025dbd | -6.26864 | -53.4476 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d289ce1-7cc9-3c69-b65d-4f917efaa59a | -6.30034 | -43.57995 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f38174fb-e12d-367c-b2b2-5020723cc334 | -6.61809 | -43.9729 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d3c2e53-8e85-3ecc-92a5-d9805b69d8d5 | -2.378 | -47.63304 | 2025-09-05 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e595ada8-cc5f-3f8a-a611-46fda12799bf | -6.00847 | -46.66256 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d15a2699-1ccb-3b2c-a6ab-40b288e29eeb | -6.67007 | -48.40092 | 2025-09-05 04:34:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 420cad31-aa22-3e4d-b4ca-cbe512ef652b | -5.98282 | -43.81233 | 2025-09-05 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 509e77b9-d567-3232-9557-645134c01cba | -5.69342 | -45.18005 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c59bb40a-0aa3-3605-a733-e3ea87bb3a42 | -5.86078 | -45.65754 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac86807d-7620-311c-8bac-a0c88e2f0611 | -6.01573 | -46.66008 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca5e5d0e-6523-34d0-9fc1-ee4a728230e3 | -6.54554 | -43.91409 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db83a93c-b35f-383d-bf1e-a8c4dfe4f731 | -5.98947 | -49.23489 | 2025-09-05 04:34:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc3f1af6-440b-3247-a4ce-632589afc496 | -5.34692 | -49.02996 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37059e0b-4201-3f60-9b72-dcef85edd143 | -7.97646 | -44.52008 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fa6b74c9-140f-31e5-8c9e-99e34206e9bf | -7.98018 | -44.52063 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8c0467e0-d3d1-3906-8c87-e7e2f30fc29b | -7.53443 | -42.53264 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3754acf2-d32c-3918-98b5-b71e6fb1027a | -6.20435 | -43.34125 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f345fefa-a574-33c5-a0a3-35ffe0d7aa0a | -6.90674 | -43.79824 | 2025-09-05 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d24c001-4e54-340a-a842-5ad050af0d7d | -5.85997 | -45.95733 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f068978b-ba85-3759-8983-72d7a860b1d0 | -6.68083 | -49.76746 | 2025-09-05 04:34:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4555f11d-5a8b-3fc8-9193-45da0899e982 | -3.0568 | -40.84967 | 2025-09-05 04:34:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d7aa5eb-4d30-3828-afba-669856cbca0d | -6.1352 | -44.58456 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 851f8a79-5e67-3bb5-8389-5e0bb751d083 | -4.00972 | -48.94346 | 2025-09-05 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa63f7ac-e6ea-37eb-88dc-9763aeaf67fd | -5.5455 | -43.77748 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fad7857-d48d-3126-bad3-e5a36a27e8f2 | -5.54393 | -43.08898 | 2025-09-05 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54569674-278a-3cf1-8469-e5ce51f3bd3a | -7.05277 | -50.86096 | 2025-09-05 04:34:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b075bc14-ddd6-3e20-9fb1-7a467b23d5aa | -7.62478 | -42.64557 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd49f3bb-69f7-3b5c-a9ee-fbbc37c360b0 | -6.14198 | -47.88068 | 2025-09-05 04:34:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7fc50f0-7708-31c2-b36f-b910df8beb50 | -6.73391 | -42.24716 | 2025-09-05 04:34:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e8bcd0fb-3ec1-3740-a3d6-231149313455 | -4.88993 | -41.74396 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 554d8218-d33c-3613-9a74-9d44f3044404 | -5.89989 | -44.16414 | 2025-09-05 04:34:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 605a746f-028c-3ea6-a2d0-47aebc9c19bb | -5.88058 | -45.5757 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 442d6cde-e604-3b41-a39f-2123b73a17b8 | -5.9321 | -44.15114 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d324f363-f01f-310c-9254-4729eced80ec | -5.87999 | -45.57944 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38f3bcd2-cef0-32dd-a7f8-49f1b4445e89 | -6.07239 | -43.2903 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6f31b9ed-ab86-3513-b8a8-3cd10b58200c | -5.20733 | -43.69752 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 674f2502-f4c1-333f-851f-6dfa02af2ba8 | -6.54652 | -42.9453 | 2025-09-05 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e83577b-6b65-32d8-877e-8dfec7047b2a | -4.89475 | -41.74068 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 04f379cc-9c93-3de7-9273-d8123255ae70 | -6.04612 | -45.99331 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eb156aa-4d6b-381e-8fc8-8be63a3e0e42 | -7.24159 | -43.8595 | 2025-09-05 04:34:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a8fabc9-801c-30aa-952e-60046298a0ed | -6.01802 | -46.68945 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e90ff767-2bf3-37c5-bba1-4a07ebbc7521 | -4.12821 | -40.57542 | 2025-09-05 04:34:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 41e94998-0d48-3014-8790-8f7c6d5c6fc8 | -6.2155 | -43.54264 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0ad6a5d-5773-387f-8ee2-d43be427ce0f | -7.05342 | -50.857 | 2025-09-05 04:34:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bd7805d-4d07-3694-8952-0a104ebf90a9 | -6.24112 | -42.43446 | 2025-09-05 04:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f39f7214-a7bb-3857-926e-9b30bab92191 | -6.25058 | -46.11705 | 2025-09-05 04:34:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00e6db22-0283-337e-9a3a-4d461f56ce0a | -7.19772 | -46.5713 | 2025-09-05 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README21.md)
