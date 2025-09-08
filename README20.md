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
| f3542023-245b-37f4-8e17-ab18740cc6ba | -6.47958 | -41.77381 | 2025-09-08 03:38:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 71f15532-5ec0-32a4-ae1e-0ca68ea3db33 | -7.09699 | -42.93735 | 2025-09-08 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7bd7fcbf-aca9-32e6-a1eb-e3ca908dab33 | -6.19176 | -43.58406 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dca047b-fe70-3f50-863e-a928d5f733f8 | -6.19283 | -42.64514 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f63f69fc-e36c-35c3-9836-5f935583bf2c | -6.19906 | -43.609 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b068088d-71fe-3114-8ee3-7df8bb638014 | -6.61026 | -44.00618 | 2025-09-08 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42bb3c16-135b-31f3-9cd2-2e3185f83368 | -6.49524 | -43.98178 | 2025-09-08 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0fb7524-4437-3e0a-af9f-4be43b252f17 | -5.80745 | -45.64757 | 2025-09-08 03:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5916dc39-dc75-3e2d-8882-59d5716d33f1 | -6.4594 | -43.95284 | 2025-09-08 03:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70087e5a-2eae-3dd0-afb3-823b5761ad14 | -8.16185 | -44.85099 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62afeff1-b8c2-3478-823a-87227a0faacc | -7.09375 | -43.90144 | 2025-09-08 03:38:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b135a33-8872-324e-bc44-c6838c6affc0 | -7.83075 | -45.43188 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b33f519-32ac-3581-ab64-c2172a41600e | -5.88071 | -43.95969 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57609ba9-e3c5-3c09-9f63-db1d9a8d6173 | -5.87832 | -43.973 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ff0d5b1-b268-3f41-97e7-caea360c918d | -6.2218 | -42.59191 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| edc0ce0a-7a42-392a-a29a-b3fc05b4f48a | -6.2673 | -43.69649 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4b4669c-0a2c-333d-8edd-aae4329d4f67 | -6.46005 | -43.94917 | 2025-09-08 03:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a151f0c-bcf9-31fa-b4c1-5d669fd6a3ff | -8.299 | -45.38848 | 2025-09-08 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 067180c4-6a3a-3e3b-bf47-a9d3cdbcce15 | -6.19905 | -41.0017 | 2025-09-08 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d089abac-2dc5-39e1-b714-d89f60e29ec8 | -7.11048 | -44.13922 | 2025-09-08 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1b998d6-55c8-3256-9f37-6d8563f5755a | -7.29935 | -44.14677 | 2025-09-08 03:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c30f3224-fbd1-3467-a484-371c0a4a7019 | -5.35287 | -42.64468 | 2025-09-08 03:38:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 25b97306-876d-366c-a54f-f5f976a83afe | -7.76249 | -34.90962 | 2025-09-08 03:38:00 | NPP-375D | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 9ca073be-c8d4-3f83-a196-ab540e1d3f47 | -7.08372 | -43.89171 | 2025-09-08 03:38:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10b9b020-287e-3f9f-ae40-d5b2ef577ddb | -9.59512 | -39.6773 | 2025-09-08 03:38:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4df55598-caf3-336b-87c0-44a68070a665 | -7.73481 | -44.73071 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 647742f3-1204-3d0c-816c-77c4ce97f51b | -6.30425 | -43.8215 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0ab2d35-a7df-3313-9476-94e426a2f336 | -6.30397 | -43.82362 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7de4565-e6b4-3393-92ac-3a7643e09fee | -6.30325 | -43.82769 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 158cfd1e-3039-3ed1-99ec-ea879a31fb37 | -7.81985 | -45.43274 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc516718-86c9-360c-b919-ad828c7f9793 | -6.2114 | -43.37589 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a606ddf-4199-3ea9-93b1-d0387ca3c740 | -6.21533 | -42.59741 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d3581b58-4439-3719-8bbe-0139956ec4fb | -5.64557 | -45.11467 | 2025-09-08 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 242edb35-7b73-3ada-94af-52a45fc19ef1 | -6.20693 | -42.64442 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b6633893-a156-38dd-9e1b-0d109f069a63 | -6.38661 | -42.60651 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab917594-d44e-3012-9829-c651636e15ae | -6.83938 | -44.88144 | 2025-09-08 03:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7fdcb128-2fb8-3a08-a294-9fa440ba339d | -8.61849 | -40.19962 | 2025-09-08 03:38:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 14e07704-3854-3cf2-b33c-e60714b7ef4b | -7.87386 | -46.25412 | 2025-09-08 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cfd265c7-6bf9-3ca3-9cbc-af39de10fd76 | -6.61684 | -44.00294 | 2025-09-08 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f998692c-faad-386d-8460-d0fe66cb1037 | -6.48562 | -41.76888 | 2025-09-08 03:38:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 686ca311-906a-355f-848a-4bf8b9c47734 | -6.19224 | -42.64857 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 244622ad-56da-3dca-acb0-71178c4ee945 | -5.41691 | -42.85738 | 2025-09-08 03:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 14dc357a-4f34-3ae2-adc0-98519f7e1af8 | -6.13363 | -44.23626 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 242a9673-42a7-3d7c-a530-4df1ad872e84 | -6.23452 | -43.50743 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0fd3e8a-fac0-3f27-b138-b9c7a61e6ae0 | -6.19043 | -43.59153 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05ea68fe-1253-3de5-8c54-f86ebde8b1bc | -7.08944 | -43.89269 | 2025-09-08 03:38:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccb20f41-5904-372c-bf6d-cb7b631a21e3 | -7.82651 | -45.42039 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87632f48-0804-38a3-b2eb-63d4c2e25026 | -6.22122 | -42.59516 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 45ac7aaa-25d9-33c0-820a-b52e35d2599e | -8.0412 | -44.06227 | 2025-09-08 03:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e52d2dc4-83b4-36dd-aa99-3c2e7032425d | -3.9628 | -38.87566 | 2025-09-08 03:38:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 879cd9a3-a683-342c-be52-57f81798f4bb | -7.84462 | -44.85989 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1d49110a-3656-3077-85f4-09653585795e | -7.08301 | -43.89562 | 2025-09-08 03:38:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcf2c1e2-a57d-3bba-964f-928396444f45 | -6.30276 | -43.82964 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff72ac41-0b19-39fb-80c5-610123acec30 | -5.45061 | -43.43712 | 2025-09-08 03:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 613e6dd0-1e17-3e21-8051-c52556b1575e | -6.5055 | -42.17621 | 2025-09-08 03:38:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 407a50e5-6942-3623-bef0-3b3c6bc76242 | -5.88142 | -43.9558 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 988f7583-f9a4-34aa-aa54-3961af8ee18c | -7.98908 | -45.46453 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b33b8c5e-b42a-3e3d-8cb6-087547add791 | -5.85406 | -43.84756 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 117e1bcf-b891-3a73-ae14-3a603e5d702b | -7.35301 | -43.94662 | 2025-09-08 03:38:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fea04275-0d7b-34dd-b68a-aec82be2a27f | -6.28666 | -44.38827 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32fd0398-9846-3cbf-8a05-2e017479d256 | -5.6519 | -45.1157 | 2025-09-08 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80c87c86-db6d-347e-976e-6bb3151373fe | -5.86067 | -43.84401 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fcf7a4f3-4b92-3cd4-a73f-9d3fdacf4174 | -7.00096 | -44.92518 | 2025-09-08 03:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf79e815-00f9-378b-80b0-5993097055cb | -6.19025 | -42.64524 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 313a67ff-58a6-3b15-a099-db8a3d14b396 | -7.1406 | -44.56836 | 2025-09-08 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47caf623-8fa8-3367-83c2-65756918839d | -4.63071 | -38.56903 | 2025-09-08 03:38:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cebf6122-cc9f-372d-ac85-e3dc8863818f | -6.53233 | -42.41885 | 2025-09-08 03:38:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b0428972-84b4-3d72-a742-97b49d34ba64 | -7.57178 | -44.66837 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b6b2a83e-807b-376f-af1e-846a0d2f562c | -6.22942 | -42.57993 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 568d1aed-65e0-36e1-be36-a54008ad293d | -7.6577 | -44.81375 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b46b22a5-5f71-39ca-a07e-557423bb400c | -5.78502 | -45.6302 | 2025-09-08 03:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3d4abcf-81c6-3289-ad9e-897eb2600cd7 | -6.46594 | -43.94967 | 2025-09-08 03:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 628de7a3-51f4-3444-9f83-96e74a9e7ffd | -6.08088 | -43.3604 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4887b24-5adf-38e2-a953-9c67747ef0b9 | -8.0426 | -44.05463 | 2025-09-08 03:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b5a9d26-1f2d-36c9-b721-c4ef4c26fc4d | -5.8755 | -43.95516 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86f1721d-dcc3-3a16-8fb2-fffd5f018957 | -8.0356 | -44.06079 | 2025-09-08 03:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bf9d0f0-6ac8-32f2-bc2b-39123412db78 | -5.64354 | -45.11422 | 2025-09-08 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 365ca107-fb4d-3c6a-9fd8-3397e62a87a0 | -4.82807 | -42.73566 | 2025-09-08 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e25ee6c0-9593-3b40-a559-442a2d16a526 | -6.17738 | -42.63898 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3ffe51c8-0312-3862-9643-44fa4bb2d1de | -5.87124 | -44.18228 | 2025-09-08 03:38:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1af9ba4f-d50f-33de-aa8b-e97b12ffddf3 | -7.08345 | -45.19736 | 2025-09-08 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ba7d935-3387-34c8-8ecc-ebb6981816bb | -6.25187 | -44.83136 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cf2057a-e557-3703-8717-9b6b24a270a0 | -6.30996 | -43.8228 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02dfaa14-98cc-3788-9d93-463d511ee1e2 | -7.54559 | -42.52549 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 529bd7b1-26cd-3546-9d30-f588f99a757e | -5.41627 | -42.86102 | 2025-09-08 03:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d22a5ffb-700c-30ce-9f92-a7e13e59b251 | -6.88149 | -44.25772 | 2025-09-08 03:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b61a8eb-7855-3999-b0dc-0aab385f88bd | -8.2193 | -44.77451 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49aab918-89fa-32b2-b082-96468d0e07b8 | -4.55916 | -40.34147 | 2025-09-08 03:38:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d4231142-19e6-32af-92fd-50156130bb7b | -7.13686 | -44.56999 | 2025-09-08 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cd47ce8-3f4b-32f0-9812-dcf5cf7179d4 | -5.87913 | -43.96848 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe1ddc51-403d-31de-a1a9-c02fad29776f | -6.19978 | -43.60495 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 768a79fe-77eb-3cce-978a-79eda2a28eb7 | -4.89629 | -42.21507 | 2025-09-08 03:38:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aefbb867-5bd8-3495-a6bd-4e036227d582 | -6.6688 | -43.84785 | 2025-09-08 03:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbd22eb7-192a-301c-8728-b5aaddb9d192 | -4.80515 | -43.54752 | 2025-09-08 03:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 491f3dc3-40bf-39cb-a602-22779eb54f8d | -6.18472 | -43.59065 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9139fc9c-7488-346f-8a7d-efb3fa65597b | -6.60967 | -44.01141 | 2025-09-08 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e83614dd-27e2-368e-9ac5-b7fd5d196436 | -4.82869 | -42.73209 | 2025-09-08 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82c4a437-7751-3115-a8ba-028a06543048 | -6.26803 | -43.69238 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c39cae6d-273d-36c6-a0e5-ae9d294973cb | -7.56258 | -37.18886 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5c80b259-d5bb-3765-b009-03c7e34b2477 | -6.19996 | -40.99649 | 2025-09-08 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README21.md)
