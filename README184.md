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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 043fbb50-30a0-3df4-8c17-38de61a19e21 | -11.62422 | -43.66777 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 323d4dd4-accc-36e9-9453-c8f983a9506f | -10.84273 | -40.83722 | 2026-10-07 16:35:00 | NPP-375 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9fc9721c-af0a-37dd-a741-642a5f24b7af | -12.16976 | -44.75601 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 7e75dd0d-ffcf-3145-99fe-bdc414c0e283 | -12.99047 | -47.06786 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 3c9e73c8-28b1-3de9-ac71-92b2be3305ec | -17.50019 | -39.87757 | 2026-10-07 16:35:00 | NPP-375 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 1d1908ee-6263-3c60-aabd-f786bec3b8b9 | -12.20738 | -44.65349 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2d3d4613-7384-31e6-baf7-21ac29bb98e6 | -11.76099 | -44.93834 | 2026-10-07 16:35:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| e28c7904-4cbb-3b6c-b340-0cae6bb186db | -12.18641 | -44.74961 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 4a7c8d36-ebe1-3f25-8e6b-244d867160ce | -14.25406 | -41.62159 | 2026-10-07 16:35:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 709bd85c-b208-3b65-8400-bebcfe0fb252 | -14.77159 | -47.14973 | 2026-10-07 16:35:00 | NPP-375 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8c3496b8-3dd5-323e-b0f9-52aac27fd96f | -11.84942 | -43.55503 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 5c238448-788e-3243-857d-d822d2623667 | -11.63745 | -43.68751 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 8f8aa912-f239-3678-bb48-61735afe25ad | -11.82311 | -43.55259 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c5b842e8-e6fe-3a0c-9338-a79dfb9f3f8b | -11.85448 | -43.54324 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 12c86715-cc16-331a-a53e-115ea34457d0 | -12.28786 | -38.74725 | 2026-10-07 16:35:00 | NPP-375 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ab516932-dd1b-3af0-b3f8-b5ddeacf15e4 | -10.96555 | -40.18618 | 2026-10-07 16:35:00 | NPP-375 | PONTO NOVO | BAHIA | Brasil | 2925253 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 483d3f3a-32f2-3cc4-b354-9c1cb66aaacd | -11.0657 | -43.17441 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5947d00c-a280-3c00-86b8-a610055594f0 | -14.51098 | -41.44276 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 80b161c2-cbf3-3e7b-ae1a-a396d23937e0 | -12.56949 | -45.08464 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f7b94615-8a4f-3648-854c-438e6a11b356 | -14.39515 | -41.37347 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f0d80c63-09d2-3b25-a2b1-d5fd480128f6 | -12.26293 | -44.41861 | 2026-10-07 16:35:00 | NPP-375 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 36a39fe6-31d2-3868-b6ee-0dcd452543b4 | -13.6888 | -49.09475 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| c9f7c8be-9285-3c2e-9aca-af580dc7e6ad | -11.85594 | -47.32877 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 202fad74-1c00-39a1-aac2-baafc4b0c847 | -13.03141 | -43.12157 | 2026-10-07 16:35:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| db1edb35-22c2-38f5-a143-f132423daa84 | -18.13228 | -42.78575 | 2026-10-07 16:35:00 | NPP-375 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4206e2ae-5534-37cf-ba57-5386ee289628 | -11.64153 | -43.6788 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 5e1160fa-e78a-346a-9013-d04f48e13736 | -12.23163 | -44.73106 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c68701c8-01fa-358a-a713-58db9716cc6d | -11.26232 | -45.19655 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| ca045253-5285-3f51-a800-79c85993664f | -12.27278 | -47.1736 | 2026-10-07 16:35:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c1428bb2-8daa-3567-a340-18bb067f9631 | -12.1772 | -44.75878 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 03bc19e1-c511-381c-acab-04bb66f7705c | -11.641 | -43.67525 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 8047038c-95c9-3947-b506-16655007dd76 | -14.16401 | -41.36739 | 2026-10-07 16:35:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 81759a64-abec-342a-b081-672a466d428c | -18.99754 | -39.80304 | 2026-10-07 16:35:00 | NPP-375 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 46de99db-957d-37a0-a0bd-6e17c0aa8ec9 | -10.87832 | -39.3129 | 2026-10-07 16:35:00 | NPP-375 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2dc96750-b35f-3949-8b2f-48fcfb572494 | -12.18287 | -44.77349 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 5080a2e6-d36c-3b80-8c1b-a36ab0d2874f | -17.54837 | -42.11878 | 2026-10-07 16:35:00 | NPP-375 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 92c5a0c1-8642-3a7e-a06a-6b6291ac79e9 | -11.81731 | -39.14582 | 2026-10-07 16:35:00 | NPP-375 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6156891c-8b81-333e-9412-ea07a3dfa974 | -14.18795 | -48.42219 | 2026-10-07 16:35:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18151149-be47-3ffc-bd19-4766409fb99d | -12.61292 | -38.91163 | 2026-10-07 16:35:00 | NPP-375 | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0eaab1e2-e3a9-3332-969e-f3fd8466945d | -11.85009 | -43.53669 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9765bcea-d604-379b-8d51-625353a5bd19 | -19.8144 | -44.2701 | 2026-10-07 16:35:00 | NPP-375 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a34bb925-00a8-3995-af11-dc6a912b7319 | -11.67108 | -43.67072 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0837f7d8-f2e4-3795-9cfa-3e874a49bc86 | -19.57214 | -40.459 | 2026-10-07 16:35:00 | NPP-375 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e6ee4177-6fce-320c-83e2-43afef78cb95 | -11.62528 | -43.67482 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1582a013-e897-32c6-b3f4-b5aad376c03a | -14.39181 | -41.37403 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| acd0f7c6-5a50-3e1b-a69b-a92231563174 | -12.0493 | -43.44653 | 2026-10-07 16:35:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f00c88b8-8281-3dc9-a263-1b7f40f1bed8 | -18.16681 | -43.26899 | 2026-10-07 16:35:00 | NPP-375 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| e96e74fa-07c2-3074-8eb7-f1b1e2bdb274 | -19.7681 | -40.27196 | 2026-10-07 16:35:00 | NPP-375 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| eb52927d-82d4-3ad1-85cb-2f5648eaa679 | -14.90955 | -48.762 | 2026-10-07 16:35:00 | NPP-375 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1d743b96-fa4f-3cc5-abcc-424b353326d2 | -18.05371 | -44.5789 | 2026-10-07 16:35:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 198d5a6e-0153-3637-944f-e7580ba5e77d | -11.51589 | -42.67244 | 2026-10-07 16:35:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 17fdb530-0ee9-307d-9f81-72f3407d53ff | -11.91742 | -39.38296 | 2026-10-07 16:35:00 | NPP-375 | RIACHÃO DO JACUÍPE | BAHIA | Brasil | 2926301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 043e4474-ad5b-3208-8f16-63e38656404e | -11.22527 | -44.87111 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ebb68a07-f718-3a65-9cd4-82835255d404 | -11.06238 | -43.17493 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5cac132e-ae06-3ecc-91b9-d2a900946b6b | -11.724 | -43.65892 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c7e2fa58-1dac-3db3-9072-3787d1dedce2 | -12.61023 | -38.9131 | 2026-10-07 16:35:00 | NPP-375 | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| fe25245a-42d9-3c7c-adfb-046f3f74199b | -12.34333 | -45.73184 | 2026-10-07 16:35:00 | NPP-375 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1cec41f0-af1d-382d-9978-ab121fa2b481 | -12.04409 | -43.38918 | 2026-10-07 16:35:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 6544458e-7729-3f33-8f17-a9b974d51bbf | -14.86209 | -46.84055 | 2026-10-07 16:35:00 | NPP-375 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47471ed5-4111-3adb-8025-c53ae45cb405 | -11.84723 | -47.38268 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 23ecbbf3-93fb-3a0e-98b9-6301f9878064 | -11.70783 | -43.66506 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| b9d653d7-7a45-30cd-ac78-a9bf1ed56e00 | -11.22495 | -45.25735 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aeb37e20-232d-368f-ad1e-305a2aac3f50 | -6.20812 | -52.78691 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 208ec677-4166-355a-8090-08ebcbf5ba82 | -3.91388 | -44.66457 | 2026-10-07 16:37:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a47d872e-c0a2-30a8-8590-e353622fac7e | -5.27161 | -45.16882 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9e7ea4fd-01d5-3155-a969-be845a99a742 | -5.73654 | -45.1571 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 80f550f3-62b6-34eb-bbb2-9f1beb2b993c | -4.80068 | -42.16258 | 2026-10-07 16:37:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 42938ec9-b3b2-3d0c-82ca-271639afbfd0 | -14.78694 | -42.62438 | 2026-10-07 16:37:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 5abfad5e-1f98-3265-a74e-c59336fa2365 | -7.6832 | -47.34226 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e9ca47d-b15f-31e0-87ba-28d05a3f1f75 | -6.82727 | -39.53921 | 2026-10-07 16:37:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 37.5 |
| aa7216ed-eae7-3b29-812a-832b147464e9 | -7.28147 | -46.16787 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 74fb5120-b67b-3e4e-b4f7-5acd176575a5 | -11.37695 | -46.66849 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5fa5c081-94c8-373f-8300-1c3eb1d5b6aa | -7.74925 | -43.83248 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 397fb5b8-19c9-3ac9-ac48-504ce33491ef | -8.10612 | -47.12938 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e17c9e57-666e-3d87-8713-ab02b7d13e1e | -7.023 | -47.51075 | 2026-10-07 16:37:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8a427f39-bb41-3bac-991c-e9d5faafe067 | -16.62314 | -43.27847 | 2026-10-07 16:37:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6e93eb62-72ea-3f2c-828e-2c711887f191 | -7.47568 | -42.80406 | 2026-10-07 16:37:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 25a9f7da-2eb4-3838-8aea-223d866665be | -9.93782 | -45.73279 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 6d2ca138-172e-3d9c-b620-469d0f5e5a99 | -3.20687 | -42.96105 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 4454a90a-e74e-3120-9372-14042409c9c1 | -8.55885 | -51.23565 | 2026-10-07 16:37:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 33e96786-3cb9-3a3d-8c75-4665d2ab119d | -4.70415 | -41.9117 | 2026-10-07 16:37:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 2da3cc3b-5ada-37e7-bad8-95ece6811c01 | -3.3607 | -43.39191 | 2026-10-07 16:37:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8e4acb68-dbcd-3de8-a828-f5a94ca87ccb | -5.24808 | -50.91228 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| be7c0b82-e979-34dd-818e-155fafa1411b | -15.11058 | -43.6264 | 2026-10-07 16:37:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 626fa4bb-b4fb-37f7-a6ff-944ee4242ea0 | -6.3681 | -55.46529 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5e741beb-b46e-301c-85fb-b833583e27b2 | -17.24537 | -47.48634 | 2026-10-07 16:37:00 | NPP-375 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 465334b0-40af-3c43-b1e3-b19f143751aa | -4.68207 | -40.82408 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4de7cc86-58f3-3a09-9f98-30d2a4acd648 | -9.40404 | -46.4382 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 793f91c0-c380-3aba-aa28-3504ba6e0508 | -15.9482 | -40.264 | 2026-10-07 16:37:00 | NPP-375 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 7a227d88-931d-3c77-94a2-b80c69cb2eba | -11.13864 | -46.1681 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e42461f7-54b4-320a-a827-e46796406b14 | -5.93538 | -53.48775 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e93d3d28-1584-3fad-8796-3f5f980b1a90 | -5.74502 | -41.65129 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8b8b3381-9c49-3fc0-ab21-92e37522c8c5 | -5.21804 | -37.37396 | 2026-10-07 16:37:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 22e57059-9bd3-3f31-bfd6-330ed22f6583 | -6.09921 | -55.73167 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 12a11f9f-5d0d-362d-bfa5-b803733c5331 | -3.342 | -42.93232 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40f34f66-00f1-3028-b303-1865e6a6bdc1 | -8.77938 | -47.58133 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| ef878d40-fde2-329b-9012-14d4dc9304c1 | -10.99948 | -45.4656 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c19493db-0da0-3d09-a835-e699c0318fee | -7.4399 | -44.46964 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be74284c-c41b-3254-8089-94b730a2e4a9 | -10.62813 | -53.86026 | 2026-10-07 16:37:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4e547dc4-4d0a-36f7-b021-9cfaf8b17f84 | -6.31336 | -53.3092 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README185.md)
