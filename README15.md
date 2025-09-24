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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1758e312-0edf-3b36-bc78-da3ba0b5e6b0 | -5.63595 | -45.72435 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| af2b407d-0d2a-3b80-8c57-6ce888066d73 | -5.76468 | -46.76224 | 2025-09-24 04:51:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c17e2e61-8918-31e8-8a84-77989ee92ae7 | -5.21618 | -43.72482 | 2025-09-24 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4337ce94-19de-31c4-9ee0-abf516f21326 | -11.6391 | -44.34534 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d5c8fcc-8cd8-3f02-a5ae-ff53c1068bb3 | -10.583 | -44.07491 | 2025-09-24 04:51:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 779438b3-23ac-354f-9d83-29fc2735af03 | -11.6373 | -44.3596 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 519fec35-cd9b-3fb8-aa2a-7927b73ee5a0 | -10.57662 | -44.08137 | 2025-09-24 04:51:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59ead036-e63f-3070-a845-9fed75d9166b | -5.30949 | -45.32111 | 2025-09-24 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dfe08341-1993-33eb-940e-d9e1841fefc5 | -10.28986 | -45.23646 | 2025-09-24 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cf4962d7-bcec-3560-9a5d-8f13e76dd525 | -11.5243 | -43.67111 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 790db8a2-40a7-3b69-8956-14de93b14beb | -11.42538 | -44.93517 | 2025-09-24 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74a355e2-8e9c-33e8-9b26-1439ba83c08e | -6.11546 | -41.79474 | 2025-09-24 04:51:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c4640532-1409-3be1-a687-3f9c37e4538f | -5.88624 | -49.64512 | 2025-09-24 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 075fd4fc-16e2-3008-83cb-886ab6843e86 | -10.60513 | -49.63963 | 2025-09-24 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c041e06-77ab-3594-92ea-9536145caf58 | -7.37187 | -47.03859 | 2025-09-24 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 697df011-e03b-3e4a-a409-722e5c47e834 | -3.7972 | -51.41431 | 2025-09-24 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33c20b36-77a1-3f0f-bd8b-7bcc70fb6791 | -5.91642 | -43.85269 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2de8e838-1896-3180-953b-6a671affadb6 | -10.58438 | -44.06406 | 2025-09-24 04:51:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b08a41dd-a9df-393f-a475-afc865d6a33f | -3.79666 | -51.41777 | 2025-09-24 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a7a88c1-79d2-33b7-b2b7-7a13dcdab0dd | -5.1718 | -45.43415 | 2025-09-24 04:51:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2624598d-f8a9-32a9-a9c4-9c95f6969db5 | -8.66481 | -50.69915 | 2025-09-24 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bd62ac3-6a3e-362f-9e2a-42403bc756e6 | -4.67877 | -48.15482 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7af418f0-9443-3000-91da-69af58f4d8c1 | -6.06018 | -46.6071 | 2025-09-24 04:51:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6853179d-ca8a-323d-9c84-a00ffd5f01b5 | -4.316 | -48.09588 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 30d7797b-6077-344d-b360-2baf10addb83 | -5.97445 | -44.12558 | 2025-09-24 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35525b21-3bb5-3b88-ba5a-38af62b01f21 | -8.69202 | -44.02197 | 2025-09-24 04:51:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 765a2162-74dc-3432-8aba-b8d1a9dd03d8 | -5.64564 | -43.91249 | 2025-09-24 04:51:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 80c5b584-a4b4-3166-bc3c-f6abbfd28112 | -9.03522 | -44.95127 | 2025-09-24 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c18b5dd2-7a28-3947-a505-883de6b5e157 | -12.01561 | -47.79207 | 2025-09-24 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06547afb-6e49-30b6-b52d-500b2f3643ba | -11.01047 | -45.89193 | 2025-09-24 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3ae7f56-f37f-3993-86ba-d2bd7d74515d | -3.80867 | -53.38177 | 2025-09-24 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 825e185c-18b9-3549-9c7c-b9dbc4051ddf | -5.63854 | -45.95639 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3cb30bf-f077-3e7e-a9dc-c4dc9284f2aa | -7.48995 | -47.54635 | 2025-09-24 04:51:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c30ea164-7506-3e1c-a032-a0d32feaef0f | -8.13957 | -44.46562 | 2025-09-24 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ce422f2-67d8-3af6-82b6-7c48b629b685 | -9.13875 | -65.305 | 2025-09-24 04:51:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d4e950f-d565-3ade-bf87-04a583655799 | -8.17319 | -46.24529 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c93f727-9e7c-3777-b36e-964ed818f467 | -6.32303 | -43.63161 | 2025-09-24 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e7e1c65-5b06-3f6f-9a04-3f4e3f346ff6 | -11.41655 | -44.96316 | 2025-09-24 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8eefb43-8dd2-354b-b706-00d851113554 | -5.96938 | -44.12459 | 2025-09-24 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7441754-cb9c-375b-a9cd-97c29cc4adbb | -11.81631 | -45.312 | 2025-09-24 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37434c99-944d-3130-a504-26690a19a844 | -5.94143 | -42.92266 | 2025-09-24 04:51:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc2e0e3a-663e-39f1-967f-e62cc33cd35d | -11.425 | -44.93815 | 2025-09-24 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45056fce-5dfe-35cd-ad98-ca230fb7f5a9 | -9.43937 | -48.8871 | 2025-09-24 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 368126c4-fec9-3616-8ec8-5e8532c4ae9e | -5.62551 | -45.73232 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13a268e5-ef04-3799-b1e4-2622ed8f90ec | -7.54331 | -47.38046 | 2025-09-24 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efd0317e-a073-3548-8acc-65e9150f96bf | -8.13916 | -44.46875 | 2025-09-24 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60bbf5d4-bd41-3b4d-b214-39982ce30a98 | -6.42023 | -43.08586 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 35ecc06d-08ce-393a-938b-ace510f3652b | -5.59811 | -45.36366 | 2025-09-24 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67d52867-acb3-3cfc-81e9-ea4a4b0e7be1 | -10.28451 | -45.23823 | 2025-09-24 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0b402a6b-7730-34c5-a2eb-53148b0c9f54 | -5.76795 | -42.59714 | 2025-09-24 04:51:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3bfab2f6-e957-361a-bbd4-0bcfcdc3dea8 | -6.56312 | -43.83419 | 2025-09-24 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f669a09e-7d32-3fd7-81af-399cb67b64dd | -5.52341 | -43.86932 | 2025-09-24 04:51:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a56eddbe-6fab-3efa-b432-6cb708771727 | -5.91032 | -43.85827 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ae54337e-7193-3bda-b13a-d2d3f061d9f4 | -11.7054 | -44.3597 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd87bb51-f9cc-3e61-83af-3f01c910e3bd | -5.64047 | -43.91188 | 2025-09-24 04:51:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ed6759bb-109a-3437-9cd8-cf6327ec8640 | -11.01369 | -45.89414 | 2025-09-24 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 843e2225-b8c1-3dd5-871e-d4997adb0167 | -10.29063 | -45.23051 | 2025-09-24 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9855b99b-8fec-360e-bfcf-22dbb332aa44 | -10.17541 | -55.39097 | 2025-09-24 04:51:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2c46eac4-1d85-31e7-8beb-50641e009702 | -9.1177 | -49.62762 | 2025-09-24 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 944c44cd-6de7-3bca-a147-11b97d60b84f | -5.22135 | -43.72569 | 2025-09-24 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 666bbd45-daec-383d-8695-8298c718835b | -7.19863 | -46.67709 | 2025-09-24 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 142f4ff2-1bac-394d-90e6-557f63eeafff | -6.42573 | -43.08674 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 37b31688-e3f1-35c4-8c25-161655b304c3 | -7.28751 | -41.86529 | 2025-09-24 04:51:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 410e568a-99e0-3412-aa8c-a277eaf0fe64 | -3.83037 | -52.1424 | 2025-09-24 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 229b2ab1-3e70-39ff-91db-907c0770607e | -11.63596 | -44.37024 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb2990c0-a057-3e15-802e-90308a29f874 | -5.03444 | -43.60398 | 2025-09-24 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bffac62-92e3-36fc-abef-506253e9d54b | -5.76928 | -44.52484 | 2025-09-24 04:51:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17784e32-c11e-3312-815d-02ac10439430 | -5.78419 | -42.56379 | 2025-09-24 04:51:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2fc453b2-9ac1-3fe8-bcd5-3c0722bc6eb4 | -11.69777 | -44.37678 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2d1a220-37da-322b-974a-7dd975e04228 | -8.69032 | -44.02203 | 2025-09-24 04:51:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb6facf1-666b-31be-9923-e662fd0788da | -8.78921 | -43.03708 | 2025-09-24 04:51:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ecb8349-c5df-30e7-94e6-d39b69ca2e13 | -11.51905 | -43.66665 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a0281da-78ef-3d40-94fc-77d5b36bd570 | -6.04208 | -51.63501 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7224d6f-a7da-3336-bae5-012fc758dde7 | -5.91581 | -43.9306 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4cec437-15ae-3bbd-9ed1-69eadca9e0c8 | -9.59413 | -46.43869 | 2025-09-24 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13f76966-fb8f-38a1-b6d9-10e7375e10da | -9.58432 | -47.5869 | 2025-09-24 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9be5ac3c-7485-30e0-9321-ccadfbdc6704 | -3.73943 | -52.11358 | 2025-09-24 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53e12e7b-322e-339e-9596-526a4dace548 | -11.03115 | -45.92214 | 2025-09-24 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70bd7694-acc2-390e-832d-e871de695c68 | -5.59989 | -45.36267 | 2025-09-24 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94d60457-f394-38e2-8f22-780a203a5020 | -10.28413 | -45.24123 | 2025-09-24 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af5e5005-e032-3300-8c3f-5e13d449a1b3 | -6.25318 | -46.12104 | 2025-09-24 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd024967-446c-3423-9edd-9260feb66457 | -6.07002 | -43.79514 | 2025-09-24 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0f32069-b687-32ed-a30d-ee6cbbf3c591 | -7.50696 | -43.6721 | 2025-09-24 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16eec0cb-5a98-3a34-be9a-70414010a809 | -10.30159 | -45.22501 | 2025-09-24 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff304d70-ab98-37d4-8288-61128ea9bf55 | -8.53011 | -45.01981 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30c995e7-cb07-3233-941f-9f6071bf4aac | -10.58209 | -44.08208 | 2025-09-24 04:51:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66ecc87c-2035-3de9-9546-71ded68fd8b1 | -6.41425 | -43.08855 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 66250f3f-2da7-3470-8222-f92fd243d8e9 | -5.76228 | -42.59661 | 2025-09-24 04:51:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a7a6d654-8a89-378f-8732-a509154cd156 | -9.24978 | -44.49474 | 2025-09-24 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40a62961-49ef-3684-bd5e-20a19b6356d4 | -8.18097 | -46.36659 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6427943-616b-3651-b8a9-d68e30d539e7 | -5.6039 | -45.81757 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c537447-e8f9-38fa-8f6b-2e0d8b648482 | -5.24295 | -43.72268 | 2025-09-24 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fde5cad0-0590-3b64-8188-222d95a5bfc2 | -5.18097 | -46.12485 | 2025-09-24 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd6a3fe3-d2e7-33a4-b9c0-2c9d1dfcf36e | -4.18756 | -49.40729 | 2025-09-24 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e17cf14-454e-3d3e-828b-22548c50c848 | -4.30839 | -48.09473 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49e67f65-09a5-31db-a1d2-2325beb694cd | -10.87541 | -51.97016 | 2025-09-24 04:51:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25c5e1f8-8b22-3f37-abf1-93780399d89b | -7.23204 | -44.7899 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| aac27ec5-86cf-3b5d-b8c4-5a3b5f5d02a5 | -11.52845 | -43.66231 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6ada92b-a9b4-38bc-9aff-c355b44db76d | -11.69733 | -44.38034 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6e6c62c-b6c2-3359-b91b-a25230422fbf | -3.71861 | -53.30602 | 2025-09-24 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README16.md)
