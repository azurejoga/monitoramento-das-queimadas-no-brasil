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
| 3f391d5f-7c54-3441-a64e-ce71ceb79239 | -6.33448 | -42.75604 | 2025-10-26 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35e3eaed-1c8d-30be-bc4a-1d6163a029d7 | -5.53366 | -41.24766 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e9ff38c-5541-35d5-90bd-6fb2f8cfabd4 | -7.78783 | -45.38748 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e5ab2ca-335c-36b7-b548-202eb836dcc7 | -5.22691 | -48.53235 | 2025-10-26 04:00:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73adfadd-543f-342a-b1b7-0e6d11b89781 | -6.38799 | -42.1668 | 2025-10-26 04:00:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ef5a234-bb1a-3906-a593-f9dd8d9ffc06 | -4.26955 | -50.51469 | 2025-10-26 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ac9de3b-9900-3783-948e-fb88d3058f45 | -5.00957 | -37.84172 | 2025-10-26 04:00:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e3282f8-9e03-3f6f-9822-a74872bf11a7 | -7.00837 | -49.52588 | 2025-10-26 04:00:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4df1c74d-9170-3d86-87cf-4f596d86b50b | -8.33745 | -48.17874 | 2025-10-26 04:00:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7dc098da-36ab-3c59-86d7-3562585080ce | -6.62993 | -44.634 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 638af3e2-c52e-3b4f-8189-3c15b8b50b83 | -3.93532 | -41.02242 | 2025-10-26 04:00:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a73ce774-1afc-37d0-9e30-412503e18948 | -5.5477 | -41.26857 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 06064c47-731c-3b30-9dc4-c0dfd8e7f9d1 | -8.53483 | -47.20267 | 2025-10-26 04:00:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc1dbb47-155f-317c-9889-459cb288f764 | -2.321 | -48.58518 | 2025-10-26 04:00:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2883a48f-d2ad-3807-b82f-18b376b100ea | -6.12182 | -41.73675 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 148af2d3-0d58-3706-8128-8e91771f030a | -4.79447 | -42.7751 | 2025-10-26 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eadfdac-92f0-3b51-9f92-f8a7f73e7271 | -8.21315 | -39.34345 | 2025-10-26 04:00:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 53ebbb48-284e-3032-a849-bb463c017bec | -5.11097 | -43.20434 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d072290a-8ef2-35c9-8896-ee004b3bb07b | -6.82825 | -41.55733 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aba47ae0-f987-3a15-ab9f-d45f0e36d29b | -4.90541 | -43.23603 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5bb7421f-21e3-35bb-9e9f-fddfbaf22814 | -8.16157 | -47.0439 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8e1b007-711c-3a0e-bf83-dedf1ad91fad | -5.92456 | -43.85149 | 2025-10-26 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bb4a7f0-5bd6-3820-89fa-3dfa222c00ac | -5.60003 | -47.09659 | 2025-10-26 04:00:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a12a157-37dc-3b17-a346-d746ace70d94 | -7.04969 | -39.74567 | 2025-10-26 04:00:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b8470e06-fffb-36cb-a80c-d76a7c0b284a | -5.52593 | -46.51307 | 2025-10-26 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a315a7b5-153e-3892-a756-f5d254189b94 | -3.73208 | -47.39687 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93d15596-f3b2-3552-a614-d88523fc54bd | -6.43398 | -42.3455 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 27b7117c-0b15-3edc-bc1a-8d871c49893c | -7.45846 | -46.63929 | 2025-10-26 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d019459-7abf-30db-b94a-d7e559344d9b | -7.44555 | -44.74036 | 2025-10-26 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55c4a21e-3211-340f-8368-308624fb9fc8 | -4.738 | -43.25853 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fae8003-dba0-3171-ac49-e14d32611e9a | -6.7273 | -45.37996 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 489320a4-50fa-3aa5-b22e-2985f6a714e6 | -3.83728 | -50.20127 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ba45bfe-46c6-3c0c-9120-fa9f04ee0f09 | -8.86295 | -41.44461 | 2025-10-26 04:00:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7e3a59c8-671a-33aa-a775-0ffefe232f1a | -6.83816 | -44.00764 | 2025-10-26 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf2eae52-a3af-340c-a32b-0036f83c35c5 | -4.32731 | -41.79329 | 2025-10-26 04:00:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2191a844-d663-37b1-b891-f4b9b84d645a | -6.35319 | -44.22058 | 2025-10-26 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4876aa2-c260-3ffa-9f26-8d3d6aea44dc | -3.1191 | -51.21215 | 2025-10-26 04:00:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20ebb111-9c8a-338a-80cd-c99e19c4182f | -5.70789 | -49.30993 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66563b6c-04fa-3004-a06d-80ed9f12addf | -4.67239 | -43.25445 | 2025-10-26 04:00:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92b4d03a-e7d8-3c1a-9ec7-607adbd51dea | -7.78375 | -45.3868 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bfc2c6d-810e-311e-9ddb-acc26ed8aac5 | -7.14229 | -44.84994 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2de65d13-85b5-334d-9c4e-f2d5858b7a1b | -4.89709 | -43.25517 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| eadeb7dd-348f-3132-9d30-5ad7320ebf46 | -6.21495 | -42.53493 | 2025-10-26 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ac4790a7-736f-3b17-bd1d-54254fdcf8b6 | -6.58322 | -48.76704 | 2025-10-26 04:00:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 120438c3-8b13-32f4-980b-1fe34ff8aa77 | -4.7108 | -46.43468 | 2025-10-26 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 90001478-93e1-318f-bbd5-fa0f03603b30 | -7.35769 | -42.44185 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f7e9b804-48eb-3e4f-bbb0-55bc78a21db9 | -3.7271 | -47.39591 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2322dbe0-d403-32e3-bca7-70bca7192d19 | -4.25223 | -47.16972 | 2025-10-26 04:00:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01626c20-223a-366b-8468-bf45ef140758 | -3.38071 | -42.4812 | 2025-10-26 04:00:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a49f518-7e58-36d9-8cb1-7501ef54c0b2 | -6.73213 | -44.15047 | 2025-10-26 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b0b8f09-32c3-3e6a-8e65-75f3255c15d5 | -5.60827 | -45.19086 | 2025-10-26 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 356b27c8-79e8-32f0-a848-36e0c9c9a0cd | -5.71337 | -49.31098 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57bd1548-0821-33e5-83e5-51decc9af4ad | -5.47153 | -40.86945 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8b8e441-48c6-34a4-b933-661c597b5e23 | -3.09799 | -49.46037 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 16a0e947-2cc6-3fd5-be5a-2e2c02c96c07 | -6.22204 | -42.53596 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4de64181-70cb-32ba-8397-1a96ca49cd4a | -7.33734 | -47.12405 | 2025-10-26 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94f2e2a3-9a5b-3513-a451-bae28c053c11 | -7.84452 | -46.44352 | 2025-10-26 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd727d22-8d83-3518-be75-e882ab9e18d0 | -4.26393 | -44.3911 | 2025-10-26 04:00:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50ee9463-e93b-3f72-91bd-30be7c3702e4 | -5.69039 | -46.28853 | 2025-10-26 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51717776-8e88-3c34-93f5-142581d2248c | -5.91918 | -39.22324 | 2025-10-26 04:00:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eda4143c-27a8-3c81-97cd-a002cb9a32f9 | -4.15527 | -47.66343 | 2025-10-26 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f035c2f1-d5a1-304d-8528-e6175654cfc1 | -2.32038 | -48.58889 | 2025-10-26 04:00:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f3186f9-4605-3c38-806b-99a48286ba83 | -4.89253 | -42.4452 | 2025-10-26 04:00:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d15489ca-dddb-3b22-bfe1-631f5c4ae120 | -3.83128 | -50.20026 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 770ba0e3-ed5b-3ae3-b0cf-17ee79d1a11d | -7.15432 | -44.13264 | 2025-10-26 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa21d063-065f-3546-a9e3-ef24b942bd0d | -8.31618 | -46.81907 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fcb7e066-01b7-3624-ad19-7016466f4528 | -6.21012 | -42.54242 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 81d9f768-25e9-39b8-b80f-bd389d448c71 | -9.11334 | -40.08033 | 2025-10-26 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2b5b2fae-0d33-3a20-972d-ad2452416261 | -5.7122 | -49.28498 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4338c9e-a877-37e5-a6be-a28b82662364 | -6.20497 | -41.52631 | 2025-10-26 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 334515fd-4869-326c-8381-ca346837d4ac | -5.46735 | -37.84749 | 2025-10-26 04:00:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1990fcb1-1d1c-34c1-8798-2c69679daa21 | -6.13446 | -41.72368 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 33f70d0d-12bb-3332-a304-50ac95e6a0ba | -5.66517 | -42.59105 | 2025-10-26 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 194a6e81-5b65-3893-802e-7659d59c13aa | -4.26771 | -40.70095 | 2025-10-26 04:00:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 53f6845a-5a78-3b32-844f-d9ea6e401922 | -4.73575 | -50.87449 | 2025-10-26 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b444d23-1598-3e41-8a1b-eb2cf62b571c | -7.05249 | -43.88353 | 2025-10-26 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 00dc0487-0f31-37d0-8d1a-0d6a28b3e0e5 | -6.21862 | -42.53406 | 2025-10-26 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6f5c1abd-871a-3763-8dfa-800ec7a50390 | -3.1031 | -49.4655 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd910119-6be6-3fa3-9004-c75669c0dec0 | -4.24961 | -47.17071 | 2025-10-26 04:00:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b905ae4d-98a2-357a-9118-9dfd1ea75294 | -6.40385 | -38.2694 | 2025-10-26 04:00:00 | NOAA-20 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a6de7f30-b5bd-3015-9d6c-b7944302fc7b | -6.84106 | -44.01089 | 2025-10-26 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 224b30bf-e222-3ee5-9327-c5423c9bbbc9 | -6.10853 | -41.75397 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 75758190-8ebb-3e0d-91a0-0021c3c104c3 | -8.15763 | -47.74988 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cae2566-d8d3-37a1-8961-343656fe5a70 | -7.00444 | -41.07651 | 2025-10-26 04:00:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7e6efcee-b7d6-3c03-b982-b8a1610c5bbd | -5.11996 | -40.74788 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 03accda6-fa1d-387c-8c7a-df63e07fd814 | -6.47457 | -47.56159 | 2025-10-26 04:00:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d411cc48-df1a-3c94-90d0-0103335a517a | -6.71456 | -42.04241 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a54bbc18-0b17-3c38-9f0f-c76bb54ba7c5 | -7.79603 | -45.38861 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab5435c6-0b30-3fcc-ab5e-f042bf7686d6 | -5.61119 | -41.11865 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af442cf5-100c-3fc6-94bb-01d86ef948f8 | -6.20947 | -42.54645 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d2f70588-98dc-3933-a607-3f90372675e1 | -5.01688 | -41.03635 | 2025-10-26 04:00:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a5bd8593-374c-325f-8864-c43fd82a6f2e | -6.7162 | -44.62846 | 2025-10-26 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11aa18b1-d9e5-3c9e-99c8-a934f73ff4f7 | -5.88673 | -41.30384 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 51a490c9-2434-365a-b038-dbdb4f594d11 | -5.69484 | -46.28952 | 2025-10-26 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bf8b46e-55f9-395b-bc77-184d7439e7e0 | -6.47331 | -47.56214 | 2025-10-26 04:00:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 616a1d19-1e88-38ae-9b37-74dd0b953872 | -3.45137 | -49.69665 | 2025-10-26 04:00:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 272bb4a2-6234-32de-995d-02bdb594c3bb | -5.824 | -40.81181 | 2025-10-26 04:00:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 31260647-78e1-3964-886d-4e54d85c99ad | -7.56368 | -46.2658 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f76eeaf-e88a-33f1-8606-d82f792b7c93 | -6.90412 | -46.15395 | 2025-10-26 04:00:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f42ca4bc-6b26-3d36-9304-0d50c23177f7 | -3.84449 | -43.17205 | 2025-10-26 04:00:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README21.md)
