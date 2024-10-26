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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee6b8cb3-305c-3dec-ab97-ab30b48e52ef | -17.0504 | -53.445099 | 2024-10-26 00:31:54 | METOP-B | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a417be5-d774-3860-bfe8-16c7672c1231 | -17.7444 | -57.458199 | 2024-10-26 00:31:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 517faeb9-f2b0-3ff1-bdca-cf242792474c | -17.734699 | -57.4599 | 2024-10-26 00:31:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 585c82f1-57bd-394f-a40c-afc810ba31d3 | -17.676901 | -57.41 | 2024-10-26 00:31:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41b63cd6-518e-3414-971e-d723e46a04b0 | -17.6817 | -57.438999 | 2024-10-26 00:31:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 55470235-2170-3610-b5c7-04608fb08480 | -14.5407 | -42.965801 | 2024-10-26 00:31:59 | METOP-B | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93cf4082-8c33-3d01-85dc-4a4c243eca42 | -14.5428 | -42.974602 | 2024-10-26 00:31:59 | METOP-B | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4ee3f1d-84bb-3ca4-8b00-ca100d9eb2c8 | -14.0506 | -43.0788 | 2024-10-26 00:32:07 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 27ba4de1-8d3b-3325-9142-f15fe51c81fd | -14.2464 | -44.131901 | 2024-10-26 00:32:08 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7a410593-1232-387b-bf89-dd8ffe3a3d3c | -14.2482 | -44.139801 | 2024-10-26 00:32:08 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7742424-a345-3788-95db-59bf3f928d7a | -13.9918 | -43.2234 | 2024-10-26 00:32:09 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| de4c3d7a-edc3-3a54-9658-534423145db8 | -13.8555 | -44.450001 | 2024-10-26 00:32:15 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9be1c041-0d35-37d1-8eda-d1f6f2a9314a | -16.4107 | -58.280998 | 2024-10-26 00:32:19 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce574773-8832-39ec-8b6c-f9e747bd0006 | -16.416 | -58.312801 | 2024-10-26 00:32:19 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 04873e10-f7f7-30c1-97d0-e15eaddc0b5a | -16.4063 | -58.314499 | 2024-10-26 00:32:19 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 803708f2-d979-38a9-a6e9-63473f41e561 | -13.2847 | -43.950199 | 2024-10-26 00:32:23 | METOP-B | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8843458-6bc4-3feb-9df6-6e1b3d90b6a0 | -12.9145 | -42.434799 | 2024-10-26 00:32:23 | METOP-B | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4f3f7925-986d-301c-a5e5-2c2f8424acb8 | -12.8596 | -44.608101 | 2024-10-26 00:32:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b85c4f0-8a3f-3bdd-94b9-caceba51c2ec | -12.8614 | -44.615898 | 2024-10-26 00:32:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 140c905b-f766-3147-9bf7-3515af3a7284 | -12.5834 | -43.8228 | 2024-10-26 00:32:34 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e8821b2-c2b9-3fb8-a7fd-12a64ce6391e | -12.5854 | -43.831299 | 2024-10-26 00:32:34 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf5e1158-bbdb-3e46-ae35-df8dce98511b | -12.5874 | -43.839699 | 2024-10-26 00:32:34 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 16fb972a-e535-393a-9297-f1b5d28f16bd | -12.46 | -43.781502 | 2024-10-26 00:32:35 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1bce9a05-064e-3459-8b92-2030fe6cf78a | -12.462 | -43.789902 | 2024-10-26 00:32:35 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2141c065-4050-3f5c-9954-d5972f78f281 | -13.2334 | -47.2178 | 2024-10-26 00:32:36 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a2389cc-6581-383b-b46a-f1f750d680d9 | -11.1972 | -39.905602 | 2024-10-26 00:32:41 | METOP-B | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8cadf6be-b0b9-3310-abf4-0732cfa90b4c | -12.4779 | -45.235802 | 2024-10-26 00:32:41 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5825a8bd-302d-37cf-a14b-efdde5ffde82 | -12.4796 | -45.243198 | 2024-10-26 00:32:41 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90d05826-cfb6-366b-b1f7-0b29dd05495a | -12.2705 | -44.383701 | 2024-10-26 00:32:41 | METOP-B | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 566bf2c2-0028-3782-9b98-c32f47895e55 | -12.4698 | -45.245499 | 2024-10-26 00:32:41 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 964fe14e-72a1-39fe-9300-6522bd7772eb | -12.2608 | -44.386101 | 2024-10-26 00:32:41 | METOP-B | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74de3283-40fc-3c1b-8fca-84513ea2db59 | -12.2535 | -45.652699 | 2024-10-26 00:32:46 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9bb86722-a0f6-37aa-91eb-7b01803ef8d6 | -11.9371 | -44.547798 | 2024-10-26 00:32:47 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e1fc6c7-751c-3def-819c-7edfd368b072 | -11.9389 | -44.555801 | 2024-10-26 00:32:47 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ff786b6-6be7-3115-ab61-a9fe2c212495 | -11.9407 | -44.563702 | 2024-10-26 00:32:47 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f0b19994-43e9-3d5e-8e87-87e4962fb1e7 | -12.0985 | -45.6968 | 2024-10-26 00:32:48 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4643b3d1-59e0-34a7-bcf0-0ab3c8a7ce6d | -12.1002 | -45.703999 | 2024-10-26 00:32:48 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 150af91d-5df4-3c4f-b392-04fb38de7cac | -12.1018 | -45.7113 | 2024-10-26 00:32:48 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4157e00a-38a3-37a4-b047-0df28973cb06 | -11.8276 | -44.6987 | 2024-10-26 00:32:49 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa893d2f-1fce-39e5-bc42-15afafe6859d | -11.6684 | -43.9286 | 2024-10-26 00:32:49 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 020e7a76-9727-39fc-9015-4950b60c3aa0 | -11.6704 | -43.937099 | 2024-10-26 00:32:49 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 549fc518-d572-3459-9119-e1649915f81b | -11.8258 | -44.690899 | 2024-10-26 00:32:49 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac591dc6-211d-3120-b3f2-aaf9bcfec134 | -11.8295 | -44.7066 | 2024-10-26 00:32:49 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 234ccbd3-f3d4-38bd-947e-650e193f4ee6 | -12.5915 | -48.752899 | 2024-10-26 00:32:51 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32802a07-02bc-3348-adb2-a549c7373148 | -12.5931 | -48.7603 | 2024-10-26 00:32:51 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea6c146d-2039-3b5c-b9c2-b8f87f6844de | -12.5947 | -48.7677 | 2024-10-26 00:32:51 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37906cad-5da2-3ed0-b3ad-f00a6e8d6574 | -12.3804 | -48.584099 | 2024-10-26 00:32:54 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1356fafb-a791-3869-8fce-a7e28273584b | -11.5191 | -45.824799 | 2024-10-26 00:32:58 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 852fff9d-ded6-3264-ac33-81c36d97ef84 | -11.5208 | -45.8321 | 2024-10-26 00:32:58 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 837c8d7b-4242-3dba-b749-ed5478c10a24 | -11.5224 | -45.839298 | 2024-10-26 00:32:58 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9821aad0-b9a3-3d9a-9c71-033c96dd0537 | -11.506 | -45.812599 | 2024-10-26 00:32:58 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dba4ca2c-7363-398e-a928-5a5670340c1a | -11.5077 | -45.819901 | 2024-10-26 00:32:58 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0b5dff0-0bb6-3432-821c-e0bec1997f59 | -11.5093 | -45.827099 | 2024-10-26 00:32:58 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe6e1474-6f78-3d12-9569-79d9d9f7a9ac | -11.4979 | -45.822102 | 2024-10-26 00:32:59 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cbff8941-ebb2-3b32-a755-4d452449088b | -11.4995 | -45.8293 | 2024-10-26 00:32:59 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5cceea10-74a3-3541-b4b4-ebab23a56a85 | -10.8623 | -44.7202 | 2024-10-26 00:33:05 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8249acb9-7b8f-3e81-8d7a-28af2e43c16f | -10.1902 | -42.447399 | 2024-10-26 00:33:07 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8e9c0003-2847-3fca-b5fa-d22a9522d93b | -10.5992 | -44.256901 | 2024-10-26 00:33:07 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 53ee9ded-98cb-3ec4-9f79-91c4a74f4d58 | -10.6012 | -44.265301 | 2024-10-26 00:33:07 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b84f0af6-21dd-335b-83da-61f621ce0283 | -10.5719 | -44.272301 | 2024-10-26 00:33:08 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ad22249-85f5-325d-96bb-a01f5e8da070 | -10.5739 | -44.280701 | 2024-10-26 00:33:08 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a8ffdb0a-29eb-3c49-8c8b-0557914fe6b9 | -10.5601 | -44.266201 | 2024-10-26 00:33:08 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ac9d670e-42f8-3a19-9412-ec2e36c920e5 | -10.5621 | -44.274601 | 2024-10-26 00:33:08 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0bccd2ae-9466-33a1-a55a-5f63df0086b8 | -10.5641 | -44.283001 | 2024-10-26 00:33:08 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57782bf5-ace7-30f9-bd57-de33f888ddb7 | -9.4589 | -40.380901 | 2024-10-26 00:33:11 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 79c991b7-17f5-3110-851b-d47874f0e3b7 | -10.5016 | -44.855999 | 2024-10-26 00:33:11 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c968c40d-c528-3d02-b099-1a7e1702144b | -10.5034 | -44.863899 | 2024-10-26 00:33:11 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f7f7fc64-2387-348c-9325-05541eda4cca | -10.5667 | -45.137001 | 2024-10-26 00:33:11 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 914d8cbf-92bb-3f93-b42e-40d5298912fa | -10.5685 | -45.144699 | 2024-10-26 00:33:11 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d175b4a2-6292-3278-85d2-14f772caccf0 | -11.0153 | -48.265499 | 2024-10-26 00:33:15 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd93b37a-5886-3163-961d-1ec7be640be8 | -11.0168 | -48.272499 | 2024-10-26 00:33:15 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c57ca66-67f3-3630-9ca9-51a092ff9dc9 | -10.8821 | -47.803101 | 2024-10-26 00:33:16 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1864fccd-1d21-33fa-af37-5d797a5f97e8 | -10.8837 | -47.810001 | 2024-10-26 00:33:16 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81b792e4-3a4e-360d-8716-22237c93db96 | -10.5437 | -47.762699 | 2024-10-26 00:33:21 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec5cc4ba-915d-3e75-8a18-8fa297e20800 | -10.5453 | -47.769699 | 2024-10-26 00:33:21 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9419c029-c07d-304f-bfb8-f94cb522d10a | -10.312 | -47.7859 | 2024-10-26 00:33:25 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 704481fa-bdd0-39af-a9a9-28a426871a91 | -10.3007 | -47.7812 | 2024-10-26 00:33:25 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac61982c-7215-3d34-94a4-ca535beca961 | -10.3022 | -47.788101 | 2024-10-26 00:33:25 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a14da5e8-b089-3d9a-8398-724fac1ec3c1 | -10.3038 | -47.794998 | 2024-10-26 00:33:25 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca249ba9-a992-3be4-9029-a38eec16f230 | -9.1717 | -43.2384 | 2024-10-26 00:33:26 | METOP-B | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 999d5e73-d23e-3790-a35b-88ffb5c6b1cf | -9.1504 | -43.148899 | 2024-10-26 00:33:26 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d136110f-002b-36a5-a4e9-3237307ed37b | -10.1919 | -47.6166 | 2024-10-26 00:33:26 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0dce5e9-5932-3e07-87cf-969be4d031ee | -10.1935 | -47.623501 | 2024-10-26 00:33:26 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0653940-773f-355d-a852-f8bc43dede9b | -9.1876 | -43.348598 | 2024-10-26 00:33:27 | METOP-B | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6dd8ce74-9482-3c08-9b18-9be5c417ab00 | -10.0376 | -47.4333 | 2024-10-26 00:33:28 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc334609-8ca9-33c7-afda-8b03b64084ed | -10.0391 | -47.440201 | 2024-10-26 00:33:28 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba6f3ca8-0114-3960-baa7-a5c482248c30 | -9.699 | -46.2551 | 2024-10-26 00:33:29 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef2eb277-fa07-354b-80bc-f75d42d035e7 | -10.0513 | -48.048698 | 2024-10-26 00:33:30 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7a382a7-9c88-373b-be54-7170de11eec2 | -10.0529 | -48.055599 | 2024-10-26 00:33:30 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1348a9ef-11bd-3903-b3d2-4c5c18cd1209 | -9.8126 | -47.5788 | 2024-10-26 00:33:32 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4707439f-1b80-3e17-bffe-2ebad439ebc6 | -9.8142 | -47.585701 | 2024-10-26 00:33:32 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5faf4e8-200f-3ceb-aa85-2ca72e5bb921 | -9.2103 | -45.2509 | 2024-10-26 00:33:33 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 286713a7-85db-39b1-9c3d-5a8acb99bffb | -9.2183 | -45.2407 | 2024-10-26 00:33:33 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74e22679-0bb3-3227-a690-796971f4d97c | -9.2201 | -45.2486 | 2024-10-26 00:33:33 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f67fa5bc-f2ea-3e2a-8c49-87e9fd178802 | -9.0001 | -44.3041 | 2024-10-26 00:33:33 | METOP-B | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c0688555-642f-301d-ba3d-1e780a92d19e | -9.0022 | -44.312698 | 2024-10-26 00:33:33 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95b1ac96-0469-37d8-b1c1-1563ae9324b9 | -9.6413 | -47.595798 | 2024-10-26 00:33:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 781a73f1-a3da-39b1-8573-2b9eefb75633 | -9.6284 | -47.584202 | 2024-10-26 00:33:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9fd2e44-faea-35b5-9372-2b2fefae300a | -9.6299 | -47.591099 | 2024-10-26 00:33:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6321c821-6455-3cb1-bcff-918f28edd727 | -9.6315 | -47.598 | 2024-10-26 00:33:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
