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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa29c4a3-d641-3930-9d13-473166087ebd | -5.48558 | -44.10828 | 2025-10-30 04:04:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 833762a8-939d-3e45-892a-d854ceb0da60 | -4.47175 | -43.44319 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5b77a973-a325-3925-ab24-23de7400994e | -3.10395 | -39.6129 | 2025-10-30 04:04:00 | NPP-375D | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2345e232-8239-3b08-997a-31e4574cd183 | -6.14324 | -41.69331 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2afca90d-d5e9-39ef-ae86-10b737904c0a | -3.91945 | -43.32224 | 2025-10-30 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7065d94f-3632-3390-841d-6bca0655da9a | -7.13358 | -39.44006 | 2025-10-30 04:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4352ba8b-2cc5-32d6-a8fd-9e512200aa70 | -6.11086 | -42.43648 | 2025-10-30 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| de6cc62e-c232-36c9-b733-41f891e06df1 | -6.14338 | -41.67052 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 724aac38-25d5-3468-869d-cdfd9128a241 | -4.46797 | -43.44257 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cc338a83-5b44-385a-883b-ff112288820c | -6.14679 | -41.67111 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11418005-314b-31c4-b411-6541ef1993a0 | -6.1347 | -41.59376 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a98f5a8-78d9-3cbc-a805-3845e08100c4 | -7.61658 | -43.59378 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 15bd61ee-5cd5-337b-a75f-96746c18e152 | -5.46865 | -41.74041 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 858ac2af-b25c-36e5-80ff-b78ba14f8f5d | -8.49745 | -40.95782 | 2025-10-30 04:04:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f8c2cd1-3231-3998-9c9b-857fa65d745f | -6.13582 | -41.6958 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 75cacd72-ca82-3b81-87e0-ef704c171fd5 | -7.35019 | -47.6332 | 2025-10-30 04:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5f4635a-46fb-359c-90cd-87b6c29c31b8 | -6.3667 | -40.97361 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6b5c2669-e8d4-3638-ae3b-996980acf6be | -4.08098 | -46.93714 | 2025-10-30 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00a0c002-a652-3a23-9cf3-9e9df3b07e67 | -4.467 | -43.44462 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3f0f35eb-8864-31b9-92c8-859f822bf7d8 | -4.05151 | -44.25985 | 2025-10-30 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcec92ca-4d6b-38bb-af29-38c0a43f49c8 | -4.69795 | -45.83765 | 2025-10-30 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dd31003-8924-34c3-ab99-d531a64bc831 | -7.78294 | -46.45167 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc03a090-2796-3142-a145-92e4fe3d7099 | -6.13642 | -41.69209 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3bddd977-dbff-3a3d-9e5d-c0377ceb657e | -7.62532 | -43.5864 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7de580a7-d30b-36b7-bf3c-a3cfaac7b9ed | -7.79749 | -46.41943 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2fb29397-c90c-34ae-a497-afdacd2ac9b3 | -6.7101 | -38.21326 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 29b2d23e-5d42-31a2-b3ee-5e002670c6df | -7.21511 | -46.03688 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 162d7571-61e0-38d9-b66b-176c17376cc2 | -7.50909 | -46.26347 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0bdfdbef-6fd4-3b4a-88aa-dbf4590d68a7 | -7.42709 | -41.85585 | 2025-10-30 04:04:00 | NPP-375D | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 16887975-2ab0-37ea-a706-3edb115a3a75 | -3.42378 | -42.34278 | 2025-10-30 04:04:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f5b84d39-d930-340b-820f-7685c39a1a15 | -4.15001 | -43.87989 | 2025-10-30 04:04:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a3570cb-213f-3c31-990f-d270f5753363 | -5.60629 | -42.78665 | 2025-10-30 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bb582d1b-981f-3767-964c-160f6affa9f0 | -5.23758 | -44.29939 | 2025-10-30 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70c4ac98-868f-35a9-ba64-02fe92f7e266 | -6.91307 | -42.27264 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 56989944-18e2-3488-a453-a5aed14fdfc4 | -7.26706 | -45.02488 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 215bbd7e-7bff-3ab9-87fd-af014e49d72f | -5.66018 | -42.79554 | 2025-10-30 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 396996c4-1208-3734-836e-87d2001c4903 | -6.31371 | -42.10412 | 2025-10-30 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fac4ffc5-e98a-3585-b70f-be195a203921 | -7.2232 | -41.40996 | 2025-10-30 04:04:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8c2b4d9c-170c-37cf-860c-3844a5308b44 | -6.46488 | -41.65006 | 2025-10-30 04:04:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bd0ce76a-4c32-3c29-9aaa-d232eff41e9e | -6.13121 | -41.70269 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 85eca72a-5b15-3780-8683-a7a0f32fe0b4 | -7.16409 | -44.99518 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 39ea307e-f1be-39e1-b985-e3ff36e764af | -7.33783 | -39.71282 | 2025-10-30 04:04:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 544d75ae-b44e-3379-a262-be9f4d6e4a79 | -2.57817 | -45.79653 | 2025-10-30 04:04:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 205cf782-e232-3415-9115-28f9953c8e9b | -7.07734 | -44.93955 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 12c1ab2c-e32b-31e9-a43b-1f3263024ec0 | -3.79958 | -43.89147 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 60fc55fd-4981-3add-94db-89907a65c540 | -6.14268 | -41.58758 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 118b664d-0884-3584-be45-fabd2246b1f8 | -7.44728 | -39.26985 | 2025-10-30 04:04:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 64a9861e-4761-3b0f-8b6b-d91262cfc021 | -5.63209 | -41.09441 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c5ce20c3-88b1-3bee-af57-119500ee88cb | -5.57287 | -42.1697 | 2025-10-30 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d6e19523-567e-39e1-b5ba-63bd1eaf2c78 | -3.29015 | -46.05386 | 2025-10-30 04:04:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6f5557c-ae55-3b1b-a8bf-8317b0bf14ea | -6.14622 | -41.56553 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4a41c716-4b25-3982-92f8-bc706d2a4d64 | -6.42905 | -42.32206 | 2025-10-30 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 59fc9e35-c2f3-3a06-b020-f0b495922eed | -3.36354 | -44.78809 | 2025-10-30 04:04:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51858b07-1e31-35b0-95b6-1281f726d6c5 | -6.13478 | -41.68047 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e583cb2-4c31-3c25-a7e5-47b2d7d60f3d | -8.03374 | -42.51133 | 2025-10-30 04:04:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42772c16-136b-358d-9c07-27a59d05c8a0 | -7.54475 | -44.04606 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 116d2172-744a-318d-a794-93a625627f47 | -3.11905 | -45.10227 | 2025-10-30 04:04:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f5bffc54-f42f-3829-a660-04053eb2d4a3 | -4.84265 | -45.4266 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f199a71e-0a75-3e59-9589-90fe777f1389 | -3.99955 | -43.2816 | 2025-10-30 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2e21bd3-a2fa-3adf-82ac-5fe88855a16b | -4.60333 | -48.75039 | 2025-10-30 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 573efbc4-7105-33ef-8721-fa53fc637790 | -2.57364 | -45.79579 | 2025-10-30 04:04:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e116f868-5777-3dd1-b4c7-6c948ee82558 | -6.9151 | -45.21057 | 2025-10-30 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9172502a-2a0f-3f05-869b-7de8f8cdd0eb | -6.17523 | -41.60381 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5efeb020-0d29-3467-b78c-4bb498c8fe2f | -4.48438 | -43.43337 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a5f3e14a-fc6b-30cf-8f1f-e24711f5b266 | -6.31309 | -42.1079 | 2025-10-30 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a80c4cb-c613-3771-b817-95c2e42eb276 | -4.46916 | -45.75391 | 2025-10-30 04:04:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d405af7b-b810-38c1-a6a7-f9318249f9a6 | -6.08727 | -41.77922 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cb957e7c-674b-3045-a258-d6445894d777 | -6.17463 | -41.60749 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8707f1bd-d6bf-39f5-a36b-0672a2008216 | -5.796 | -40.81058 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e643c794-4d3a-370e-8b9d-923b1ba99483 | -5.43556 | -45.34194 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebebe26e-6160-3967-bb09-531dd03f2998 | -2.66416 | -47.87661 | 2025-10-30 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bac573e-027f-3726-8f8d-9a70e0ce21b6 | -5.82223 | -40.79682 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 13819c6d-e0eb-301a-a619-ebebae98d68e | -5.41846 | -44.83773 | 2025-10-30 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 895fc2f3-5836-3362-b16e-e6d69e44bf1b | -4.46775 | -45.76235 | 2025-10-30 04:04:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 780151a5-2cc5-35e2-8d7b-16fdc967c009 | -7.48074 | -42.73407 | 2025-10-30 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 522847ff-8ac8-398a-a191-35eb815aa234 | -7.78493 | -45.9402 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a3914279-2d2a-3191-8479-1a849ca6e204 | -5.02766 | -44.81326 | 2025-10-30 04:04:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 97c0d9a4-e01e-30a0-9e1d-b249865c8b0b | -6.14282 | -41.56496 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2de5d306-4724-36e8-b25c-5cdcff6fa048 | -6.03872 | -40.24709 | 2025-10-30 04:04:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 42c06558-b134-38e4-9533-3fad744675eb | -5.07987 | -46.08025 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15a35b26-5e6a-33c0-9651-0dfa2c9e05f1 | -4.68246 | -42.72896 | 2025-10-30 04:04:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5d3e707f-d41b-3e8d-ab56-55f53fe0d5a8 | -4.53637 | -45.62185 | 2025-10-30 04:04:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c2bfe1f-8a51-3ab6-9927-c574a48ffa35 | -4.4336 | -38.88626 | 2025-10-30 04:04:00 | NPP-375D | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ebc4d074-f3c6-359a-ad90-4476dd88c109 | -7.07597 | -44.47136 | 2025-10-30 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1ccb8f5-e152-37b0-aeab-f9d2fe012d28 | -2.77143 | -45.394 | 2025-10-30 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9276b5df-5fac-30d5-a77b-3946f7876630 | -6.1542 | -41.66861 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4aee0b1d-804d-352a-95ac-4b18c4896cc4 | -7.27838 | -46.06651 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0e72e7dd-91d4-3173-a3e7-4632856acd90 | -3.36415 | -44.78428 | 2025-10-30 04:04:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9ad5a8c-ddb8-3661-b503-3210f33ff22b | -7.62604 | -43.58211 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a1ee121-0c6d-3b9a-ba86-f06abb394514 | -4.74491 | -45.71767 | 2025-10-30 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 657fe88b-d5bb-3f71-acf2-d308969eb00f | -6.0164 | -41.97601 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fd39654b-2409-3d24-80d2-efeb56a6928b | -4.65964 | -41.59803 | 2025-10-30 04:04:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 34da24aa-179b-381a-ac03-e9037fc42899 | -7.10165 | -39.57836 | 2025-10-30 04:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 39fd58ad-2656-385b-9364-82d6b87bd944 | -6.86411 | -43.7896 | 2025-10-30 04:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beae04b7-2c8b-37dd-892b-73974d145cda | -5.60112 | -42.77311 | 2025-10-30 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8170b909-732f-3492-a90b-53793bfb509e | -7.15214 | -44.85831 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d5ad2d67-fefd-3300-850d-5cde7ae1a460 | -4.25358 | -43.71111 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a838a111-292e-3f86-b165-8eab3b728803 | -5.12966 | -45.36217 | 2025-10-30 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92eb760b-2113-3307-b336-21b278b547cf | -6.6437 | -44.61683 | 2025-10-30 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f50b6465-c9b4-34f8-ba96-f567de6283b1 | -6.21008 | -41.82195 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)
