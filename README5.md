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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec448831-6029-36d6-a37d-8abe575568d0 | -10.65131 | -49.44193 | 2025-06-05 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f8b5fc05-b0ea-36c6-9993-5b55ae93862d | -10.84813 | -46.85888 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77ff0ab1-0d3d-30e3-b3c7-c8e9a8574ef4 | -9.2169 | -48.86245 | 2025-06-05 03:42:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1027852-d8d3-3d14-81ed-d091bd9b20a8 | -10.70199 | -48.78354 | 2025-06-05 03:42:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22bace39-807c-36a7-875d-1d2302423e3a | -11.6258 | -41.83334 | 2025-06-05 03:42:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0bdef8fa-2827-38fc-b906-edb825062813 | -10.84972 | -46.85056 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d6f48a-a493-3fd3-b845-65fedba99368 | -13.57262 | -44.265 | 2025-06-05 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c7989b2-757f-3cc6-908c-5347312e6ea1 | -10.8721 | -46.85949 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c790f16-4294-35ac-9bea-fe3f93236db1 | -10.84891 | -46.85478 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca74f3b2-f34c-3b34-a716-e5400868cb4c | -12.03006 | -43.72337 | 2025-06-05 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d6b2c72-31ba-3393-b60b-bc451de650b4 | -10.8739 | -46.88178 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7630a272-40b1-3b42-a211-26078535b967 | -10.66795 | -44.37887 | 2025-06-05 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 269ab5cc-fba2-3b64-9f69-44b369040c60 | -14.15662 | -45.48329 | 2025-06-05 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7c08317-7855-3073-a509-8ebf21cdb474 | -10.66298 | -44.37799 | 2025-06-05 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b18551e-1e63-3a8f-94b9-ba298275a9ef | -14.15719 | -45.48031 | 2025-06-05 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dbf6780-80e3-323a-bd4f-0788045589ec | -9.38179 | -48.40554 | 2025-06-05 03:42:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11da1705-0bfd-387b-8de1-ff49c5a611cb | -10.84632 | -46.83687 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18223eeb-bb32-394f-8c56-f3c3dcfda7fe | -10.87389 | -46.87875 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe832923-affe-3783-8d73-ccb8b398b64a | -11.43833 | -45.11186 | 2025-06-05 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79676bcd-e082-3713-b12f-cf1d303f919b | -9.3513 | -47.69628 | 2025-06-05 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5e72040-d871-350a-af08-e8f120c48aab | -10.84817 | -46.85636 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99fed50e-63ed-332a-8d93-c357a8305795 | -10.6729 | -44.37986 | 2025-06-05 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8323989d-fe4e-358f-8f32-1bcf14f27c28 | -14.16106 | -45.48732 | 2025-06-05 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afd311de-1ed1-37e7-bf1a-733f155da2f3 | -10.66934 | -44.37516 | 2025-06-05 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c45bc552-36d8-36e6-bb3b-6b002e332b70 | -10.65264 | -49.43558 | 2025-06-05 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d61d1d59-5148-39e1-b467-963e20cbe1a5 | -10.65286 | -49.42912 | 2025-06-05 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1768ead5-7db4-3455-a2c1-5f954c80bf34 | -10.70144 | -48.77996 | 2025-06-05 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66419e61-5d5b-361b-8c83-219f11f9d030 | -10.8457 | -46.86875 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8326b25e-6724-32f6-8623-a21874284d0c | -10.85564 | -46.84906 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8bc67fb-1bcf-38e7-a789-1d460b349803 | -12.28923 | -43.54817 | 2025-06-05 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e00edae-4775-3695-b6bf-9718abe0bdea | -10.87136 | -46.86098 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32810666-f101-372b-b457-12cb7ffcd3a6 | -10.84713 | -46.83268 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7835da3d-6a7c-3d66-8122-54d9fa7a62f6 | -10.87054 | -46.86769 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f20f3a51-9bc8-3b46-a4af-3251053abaef | -11.44346 | -45.11288 | 2025-06-05 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 396c887b-9c46-3478-94fa-1d218364fbc9 | -14.15605 | -45.48627 | 2025-06-05 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1928894-2992-3eab-bfd1-1fd1049ba2bc | -8.96293 | -47.97052 | 2025-06-05 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5a2fc1cf-4b54-39ae-aaa4-d43ca1837924 | -10.86975 | -46.86916 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8992a34-f28f-3be4-bf9b-e30d2755afa7 | -14.11904 | -41.67739 | 2025-06-05 03:42:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f64d703-75bc-36a3-94d7-e2931f6fb580 | -10.64451 | -49.44062 | 2025-06-05 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f48b387b-c135-30e6-bd53-8c65176f911e | -10.86814 | -46.88037 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b65c661-18ab-3141-ae1a-3f14cbf4e8fc | -10.84899 | -46.85221 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2fbe5fe-006a-3fc3-a3ee-519766783655 | -10.87471 | -46.87458 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75ab360f-ea35-35e2-abfb-de85c405ec89 | -10.70798 | -48.78127 | 2025-06-05 03:42:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bac4d95-2df5-3df7-aff9-df9b4e91446c | -8.45816 | -46.48181 | 2025-06-05 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a802b665-5d89-3d35-a6cd-d608f1164f05 | -8.46405 | -46.48299 | 2025-06-05 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 870017b0-0615-31f4-be83-c9570bc0e063 | -8.45226 | -46.48064 | 2025-06-05 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff19dcde-c19b-3b24-8a64-b3eb77ef629c | -10.87476 | -46.87726 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30483411-822f-3225-aece-04b0041c371e | -8.73166 | -47.98728 | 2025-06-05 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86da9fb0-9296-3db3-8e41-36ef77e51410 | -7.90178 | -46.29802 | 2025-06-05 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 748f2c63-503b-34fa-aa74-05b1519462c4 | -11.81497 | -46.14141 | 2025-06-05 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0851aef9-72cd-3d26-b748-7520bc275c1c | -14.15162 | -45.48224 | 2025-06-05 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9f164b9-00a4-363a-a88b-40f3a3d189b9 | -8.46025 | -46.48445 | 2025-06-05 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aff645b2-7dcf-3bd7-b62a-2488ceeb29bd | -10.84735 | -46.86297 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb9435af-9371-39a0-b0c0-504959a3d627 | -10.86976 | -46.87181 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86635c2b-2d49-3db9-b030-662a16b7511d | -10.87056 | -46.86507 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff3e7fa6-4c2c-3f39-8fdd-d11ff653c089 | -10.87297 | -46.88344 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a402b25-0822-354d-986f-c3ff3e1f9c4e | -10.87132 | -46.8636 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5695230d-4511-3e38-963e-622018cbc078 | -21.17732 | -43.98043 | 2025-06-05 03:45:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 951df24e-b976-3214-af2b-6cefe1e71685 | -16.56116 | -43.92249 | 2025-06-05 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac0e5a12-48a5-3c5c-84f5-883bd1f9833d | -19.49394 | -45.33905 | 2025-06-05 03:45:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3133e3c-0ae5-34a6-a787-dc99ee1bfa58 | -14.15628 | -45.48191 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f373d7b6-37f6-366c-b134-75d7e6cdfd4c | -16.58889 | -45.87863 | 2025-06-05 03:45:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d02887f2-9643-3fbe-af59-756b5eaa5d43 | -14.15569 | -45.48487 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 316d13a8-d2db-3852-b513-f67e3fd5040a | -16.58773 | -45.88438 | 2025-06-05 03:45:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f6d4430-9e2b-321c-b4fd-6027f0a26d63 | -16.30149 | -42.75824 | 2025-06-05 03:45:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebf2a896-4858-36e2-9b5d-aae60dbaebcd | -14.73665 | -45.10211 | 2025-06-05 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6160ffd7-6676-361e-8824-4285e19a5a8f | -16.07091 | -43.65962 | 2025-06-05 03:45:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6e748e80-50bd-38dd-80f9-ca915e8f9130 | -20.41567 | -43.55243 | 2025-06-05 03:45:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4e9e5f32-c1a7-33fe-9c7a-f5f5ed1021e8 | -14.72331 | -45.09321 | 2025-06-05 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a666aebc-eeba-3222-a78a-663328e8e194 | -14.23416 | -45.48256 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fac6455-50fb-35a8-9f0d-536bf6bd6802 | -14.22917 | -45.48151 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce86d70c-b797-317e-be99-2fe7a2af6030 | -16.56547 | -43.92342 | 2025-06-05 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bf0ebc8-ae90-307c-b5d3-311a47ca8b91 | -20.76238 | -46.77049 | 2025-06-05 03:45:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4a11a158-0ea0-357d-834a-9ad358d392eb | -14.22417 | -45.48049 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42bb22c4-bddc-3ec4-abe8-003049daf2b3 | -18.62875 | -47.64319 | 2025-06-05 03:45:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3338ddc5-2aba-3084-8679-4d29b8cbd99c | -17.75185 | -42.89363 | 2025-06-05 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15f598ee-d204-32fa-85aa-c0fc297a9098 | -16.68184 | -43.88482 | 2025-06-05 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 945a503d-6b48-3d43-bdc0-610db7d16721 | -18.62802 | -47.6466 | 2025-06-05 03:45:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d719e763-861c-357b-9d8e-8cd91212d99b | -14.72703 | -45.09992 | 2025-06-05 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba659e44-c3d1-345c-b8e3-b0066b10422b | -14.7185 | -45.09209 | 2025-06-05 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d216698-a885-39c1-bbea-34104673cf61 | -14.72223 | -45.09881 | 2025-06-05 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b0edbc7-2bdd-3199-885e-4889fe20c9f7 | -14.22475 | -45.47751 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0538291e-f3ee-39e5-8d05-c9bfb2787b37 | -16.58677 | -45.88313 | 2025-06-05 03:45:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee8b7df8-deca-3581-8903-dbccdb1f52a6 | -14.23032 | -45.47558 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6246b721-fb51-3157-9f12-64bd035a7e41 | -19.65709 | -40.18512 | 2025-06-05 03:45:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 475d97f1-056e-3e3c-a279-1409aa96056f | -19.48946 | -45.338 | 2025-06-05 03:45:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89a454b0-f939-33e7-b668-e68b9af9ca36 | -14.73184 | -45.10102 | 2025-06-05 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 924e3141-9cbb-343b-bce6-6b2e477b8f38 | -16.06742 | -43.65454 | 2025-06-05 03:45:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c7e0abe-7885-3eea-93d3-2a3d4c0fa50e | -14.23474 | -45.47959 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92b1fdfe-50a4-37d6-b35c-f8494ebdcdeb | -16.5879 | -45.87737 | 2025-06-05 03:45:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0879437-1157-3153-9f74-b5a035cf846d | -14.22859 | -45.48448 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80766ae8-18d2-3cc7-a53b-1e74daf4e637 | -20.34722 | -40.36274 | 2025-06-05 03:45:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f4c6dfbf-2d35-326c-a486-745b817a16e4 | -17.5951 | -43.19704 | 2025-06-05 03:45:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e3a870f-063b-300a-ac78-25e4fdc6e352 | -14.22802 | -45.48746 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 427b2d76-a486-3108-9c08-c2ff0ed6ee71 | -14.73292 | -45.09541 | 2025-06-05 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1c4cf85-af2e-38d6-8da8-c0107826a51f | -14.22359 | -45.48347 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e3f76cc-20bf-3007-8eea-593db9b526c7 | -14.22974 | -45.47855 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bc5f1e4-7de4-3c7a-a848-6f1603882421 | -14.72812 | -45.0943 | 2025-06-05 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfe36eb3-8bc6-3f15-b4ee-c84473f470a5 | -14.1601 | -45.48888 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60cc8848-b923-322d-9fda-6509f432418b | -21.22322 | -44.02863 | 2025-06-05 03:45:00 | NOAA-20 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README6.md)
