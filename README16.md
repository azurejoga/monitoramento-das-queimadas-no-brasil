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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e9b3a0d-a7ab-366f-84fa-4bf35657eb13 | -9.79318 | -46.93567 | 2025-09-29 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d86303ff-dd41-319a-b500-bfd59b550e7c | -7.45954 | -46.30153 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8f133dc-1921-31f0-bdae-c8ee20ee250f | -15.29443 | -46.42437 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef848152-86a7-38c8-ae92-238f647e5a63 | -6.46288 | -44.22686 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a4326dc-72fe-33e3-9972-76df17c57437 | -11.80271 | -44.91142 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0a2fec0-0415-3da5-bdc8-ea11fe92d0f6 | -16.47019 | -43.49735 | 2025-09-29 03:47:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18a77aac-dec9-3290-837d-9ff8c5b3b000 | -6.12583 | -41.81472 | 2025-09-29 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c4d4e5d8-bd18-3fde-90e3-49d46d01f065 | -11.36674 | -45.07533 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cd7ba492-e990-3c1e-95d0-322a0a67ce50 | -10.75977 | -45.37962 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fd233b62-910f-3b87-ad02-9e5534dcc8f6 | -6.21889 | -44.20619 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6ffe423-b667-3ce0-ad40-d188fe331f17 | -6.28108 | -42.48836 | 2025-09-29 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bf45c090-cdc8-3ade-a665-14e362b8982a | -9.63329 | -48.12662 | 2025-09-29 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7edfe727-23b7-3f7a-a706-ec7c10f3dfb9 | -18.90717 | -41.1362 | 2025-09-29 03:47:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 800ae984-32ae-326f-b014-a11a9795e378 | -11.45689 | -45.0021 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c755a37d-cb92-3f54-a0e9-f22597cd06d7 | -6.81927 | -44.92308 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c9127c0-8fc0-3c2f-9b46-548c4fe8c13f | -8.30095 | -45.48053 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 18f2a54f-4cf6-3ef6-8ad2-22ebbe3cca55 | -15.26691 | -48.76207 | 2025-09-29 03:47:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 806f4198-7523-338b-af9f-313af30175fd | -17.09364 | -48.57701 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 51b9b342-9f6b-36b0-a8f6-b41c7b60a299 | -12.17728 | -43.56739 | 2025-09-29 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89f70e4b-ac39-3cf2-9910-9e2366479174 | -6.82533 | -44.82836 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 823359ac-7796-3c14-942c-3db4ee24205a | -6.46341 | -44.00964 | 2025-09-29 03:47:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f7fbd145-09a1-3720-a4df-dbc3da57d182 | -11.66907 | -45.33029 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83545939-5088-3b86-ba36-383ce16162e8 | -6.81992 | -44.9195 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 726b8695-8528-3270-b860-dbbd60bea2d4 | -7.22384 | -44.78053 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3b32dccd-bf13-3ba5-a6e6-aa47289ed4a7 | -7.49197 | -44.30141 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 101944b4-b0f4-3533-8c5f-9e831c808a8c | -11.44301 | -47.28528 | 2025-09-29 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8e4353d-6d4a-3453-9e64-69cf08e558dc | -10.40992 | -48.11604 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1acffb7-054c-3fc8-9f7c-4b3d050d434b | -11.7935 | -44.90493 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47def787-ceeb-34b9-b8b9-c023a5c5c667 | -11.5184 | -43.54604 | 2025-09-29 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e1be56d-5b4c-3423-aec3-de0266229894 | -11.68999 | -44.47361 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35ca34d1-fca7-36bb-8fd3-20b2dc9a39b8 | -10.79686 | -46.6867 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d322b94-f919-31e7-a35d-0c8dbd8d328b | -11.34627 | -45.07098 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98e135ee-2583-3c32-8e21-15f804612c2f | -7.58633 | -44.80276 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 427a804d-f109-3016-9ce7-59a1fd8dcbf6 | -17.71949 | -46.7185 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c543fd6-7c5a-34ec-999d-1374c4202a8b | -12.58699 | -41.2894 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 19526e97-e80e-3382-be8c-b75bd7e2ff89 | -6.05614 | -42.45781 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 00224e28-9317-38ea-85ba-51da27261bf4 | -10.42152 | -46.14975 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff6d1e46-3c5a-30cf-b4ff-eadeb37212a9 | -17.72574 | -46.68818 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d7e97a5-bb79-3baf-9887-157e0469da7d | -12.01753 | -47.79227 | 2025-09-29 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 878c1885-d2f8-35d5-aaf7-0e3fea18f3a1 | -6.83587 | -44.08963 | 2025-09-29 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39880cbc-e1bf-30ca-b731-71bab10601d5 | -11.50918 | -43.54414 | 2025-09-29 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bdd56aa-6546-3b6f-9d5c-ce6a5d904cff | -9.7742 | -46.19388 | 2025-09-29 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbb1296b-b839-3b5d-8e93-aee1342f915e | -6.46924 | -44.22165 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51c736e5-f7a7-31ca-946d-caa103ab0dec | -9.07866 | -47.60403 | 2025-09-29 03:47:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58399d53-ec90-31b8-aec0-6c104872b4ac | -11.35079 | -45.07524 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48eff17f-f33d-33c4-af07-772e8ab1f5f6 | -12.28877 | -44.10664 | 2025-09-29 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e157692-95cc-3d80-8280-e97266aac7a9 | -10.79191 | -46.68132 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43e8c25a-b884-3bb8-a5c4-debe229d6c15 | -15.60908 | -46.25935 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8397b8d-ab01-3d77-b24c-ba53f951b4ce | -6.49593 | -44.25632 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6e6f582-f8e0-3905-ada8-8630736da6bc | -8.26593 | -45.48325 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21afde66-eff8-3732-9c43-8cb2c11d80a7 | -11.36317 | -45.06602 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbf09b5c-13fe-3f61-b954-5c3efcf54a6b | -7.2178 | -44.78305 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| da3fd09e-4702-31df-bb7d-4ef12162912f | -5.98539 | -42.35525 | 2025-09-29 03:47:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3f2155ca-3c88-30c0-9614-d1538935066f | -8.14984 | -46.40785 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7ff46a5f-98ba-3b6c-beb0-b82e9381b868 | -6.05827 | -42.47339 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 55b59b2b-905b-342b-aa29-1049cf307b06 | -9.08067 | -45.88031 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3bc935e-dcf7-37ae-9cc7-7f79a873cc2a | -11.76533 | -47.56494 | 2025-09-29 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 822d56a3-3a37-3ce0-947e-5a7110e1d59c | -6.90569 | -36.22533 | 2025-09-29 03:47:00 | NPP-375D | OLIVEDOS | PARAÍBA | Brasil | 2510501 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7357fdfe-3cdc-372c-be7d-adb88f0d9589 | -15.46939 | -47.9394 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98e3f4e1-c906-30f9-b1cc-d5f8ee269edb | -12.88671 | -45.21852 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f41c874d-35ab-375c-a72b-1f827d93e949 | -10.76625 | -45.37436 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72091576-ce99-30f0-a621-d42904d40255 | -17.08977 | -48.56667 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 4703568c-391a-3493-8f95-21b7e6b3fdde | -18.11407 | -42.1928 | 2025-09-29 03:47:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 67b5ee94-cd04-3ac0-ae1e-fd2a08ffeb08 | -11.92597 | -48.02966 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0f8f62ce-c810-378f-968b-d5934969b059 | -7.86985 | -44.59028 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e328bf8-3d8d-3e05-bd0f-61eaf32cdb3b | -15.8556 | -46.24274 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcd3c77a-57a1-323c-b84a-a72668dc9838 | -8.32653 | -46.21737 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d926313-9822-3334-b537-939abe541877 | -16.4067 | -43.72647 | 2025-09-29 03:47:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 285b082c-5e54-3874-8ee0-e9d7da367c7c | -15.27795 | -49.50288 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74d52a35-866e-36e3-b8d0-fa01fa106b16 | -11.36157 | -45.07449 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b5c22d2-916b-301e-aab4-5552c25b4ee6 | -18.91228 | -41.12803 | 2025-09-29 03:47:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1b68c7d2-acaa-30cb-b19a-22953df719cc | -12.68756 | -46.86519 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0d1ef12-7e63-3d33-9628-da6b5ad1c20c | -12.58396 | -41.28359 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a756c4df-825a-3856-809f-53aa2ecba97d | -8.16497 | -46.39199 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86088068-6489-3baa-b5cd-f06613089eaa | -6.26924 | -43.63892 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d09216e6-76a9-3cca-b2bc-d7db26fdcdd4 | -7.49717 | -44.30246 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2ede476-fb07-3af4-8f27-14c71cbff911 | -11.38122 | -44.97011 | 2025-09-29 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f476b1e6-ced1-39c6-9eea-f43aa8215424 | -11.51127 | -44.85348 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a35c3b38-e871-363d-8e32-c78ce193cd3c | -7.80826 | -46.8969 | 2025-09-29 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b697ea26-9cf5-37c5-98a2-229880aee18e | -11.91785 | -48.03851 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06f9fdf3-8700-3905-817c-3b2da19beafb | -11.65748 | -45.33467 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0bd50b87-4d88-324e-a428-c915c846058d | -12.03208 | -47.20895 | 2025-09-29 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbd4da9d-462e-32e2-912d-a1d60561f1b6 | -15.70758 | -47.80129 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 003b8f5c-4fba-3234-9e74-5a709a6b3d06 | -17.12256 | -46.98662 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c32c6fef-91ce-3118-8f87-617784d7b14f | -16.50271 | -46.03173 | 2025-09-29 03:47:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0c57795-6d21-3921-8360-99c7048c2195 | -15.26785 | -48.75762 | 2025-09-29 03:47:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9946b0bd-bdec-3954-ab12-7c217f1d35e3 | -9.104 | -45.84851 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddc19376-3eac-33a1-89ab-bfe9060ddef5 | -6.11338 | -43.46793 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c54ab191-887d-37b9-ac26-317c4a66be87 | -16.33818 | -49.94934 | 2025-09-29 03:47:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15001c02-342d-3aa3-8a29-745bfb7f3a8a | -11.27208 | -47.18701 | 2025-09-29 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71e1b12f-ccc2-3963-8e42-deab0067fc8e | -17.71241 | -46.72711 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d403d2a5-9685-346b-91ff-117a3860211f | -12.65885 | -46.92004 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 978b71a7-e5cc-3679-8cc9-f3cb7a3b6bcc | -7.58852 | -44.80152 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1bff3df-b122-3659-b9c2-45c6de6035e5 | -6.25636 | -43.65264 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee20ca72-5f07-3401-b4d5-e57c77868440 | -7.7005 | -41.28849 | 2025-09-29 03:47:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 91e6983e-e44d-3de5-bc1d-b9e4ab4ff924 | -9.99987 | -45.40975 | 2025-09-29 03:47:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9343b372-ae02-323f-be08-a2e9ceb80225 | -12.00409 | -46.62756 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d66eefce-5dbb-3a29-9862-ff6a769e97ab | -12.28307 | -44.11087 | 2025-09-29 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 229fc722-bd94-30e9-a3f0-13f7962c229e | -7.21484 | -44.76839 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c455b9c-b5bf-3c85-a59a-01b2a735d2fc | -6.11289 | -43.47072 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README17.md)
