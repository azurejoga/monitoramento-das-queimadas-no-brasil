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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a589d55-7c2e-3872-9a25-938f6aadad56 | -6.23708 | -41.57861 | 2025-10-11 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 62abfadf-7cbf-3bae-a493-a02cd554b73c | -4.05491 | -42.51517 | 2025-10-11 11:57:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 32164954-bb02-3b45-b109-183657c043cd | -5.60397 | -39.53098 | 2025-10-11 11:57:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 021c37f9-19c1-3236-9e51-d928dcda3968 | -6.16334 | -42.54794 | 2025-10-11 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 8907daab-46c1-3b0e-a9c6-d176879478da | -6.21028 | -40.19344 | 2025-10-11 11:57:00 | TERRA_M-M | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 9d3f228d-22fa-3d02-bdab-68a563169fbf | -6.72746 | -42.08266 | 2025-10-11 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| acfbd24f-31f0-3675-a81e-77a6cd441272 | -5.48497 | -43.40412 | 2025-10-11 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ef7f3b40-224b-3ae7-aaae-492630cd65e5 | -6.18728 | -42.56934 | 2025-10-11 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| e4c1711d-5252-3c9d-824a-ed94dbd1d3ab | -4.4142 | -43.47176 | 2025-10-11 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a305e5b0-afd2-36a2-beb1-ddca7e0a2398 | -3.55889 | -44.41886 | 2025-10-11 11:57:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 48aafaa8-ca41-358e-a79e-69d6a591f461 | -5.64206 | -43.90865 | 2025-10-11 11:57:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b7854cee-daf7-3f37-bcb2-2bdcbefeb978 | -6.15451 | -42.54671 | 2025-10-11 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 50.2 |
| d1ac7c16-946e-3b6f-9786-9d1318f9c404 | -6.73556 | -42.8559 | 2025-10-11 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 93cc3e60-93d2-323b-b686-a435c85508fa | -6.25444 | -42.99292 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| e962e23a-7645-35ce-9170-cc93a1e6927c | -6.76065 | -42.82056 | 2025-10-11 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| acddb51f-a196-3d9c-88ba-8f5f59d92459 | -6.20987 | -42.66274 | 2025-10-11 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 9b10ae5c-92f8-3774-b7d1-29a26b5b1334 | -6.22692 | -41.58633 | 2025-10-11 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 071a0177-b04e-34a3-af96-e8dfe7075b9c | -6.26806 | -42.97351 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7ecc7eee-e0b9-36a5-8a54-4c5a6a8d1f72 | -4.97421 | -38.61559 | 2025-10-11 11:57:00 | TERRA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1faf3fb6-d030-32ac-9bad-7286ec42194b | -6.25459 | -42.92917 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b2347164-4d1c-35f9-b81b-6aa9125ae088 | -6.25371 | -42.74775 | 2025-10-11 11:57:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| cad8fb2b-4423-3893-9f65-f04e8fe5fd94 | -5.26368 | -43.78085 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 09af1ce4-6ff4-3f6b-9ff2-5fcd691ff079 | -5.32817 | -43.08983 | 2025-10-11 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0c8681a0-f5de-3dc1-8319-d32a205f69c4 | -6.16206 | -42.55677 | 2025-10-11 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 538b1515-ee7c-3a27-bd02-82034900c5e2 | -6.19739 | -42.56174 | 2025-10-11 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 339.4 |
| 3c557b47-43e0-3499-a81f-760296c32f47 | -6.10999 | -38.01791 | 2025-10-11 11:57:00 | TERRA_M-M | SERRINHA DOS PINTOS | RIO GRANDE DO NORTE | Brasil | 2413557 | 24 | 33 | nan | nan | nan | Caatinga | 18.6 |
| bab61bf4-75da-31d1-b99e-a21690fb2ce5 | -5.87117 | -42.84086 | 2025-10-11 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 91480db0-d23f-3166-bc48-bde7b9988648 | -6.24685 | -42.98279 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 9564038f-0b97-3793-95bc-9e7f1feaff94 | -5.15564 | -39.37417 | 2025-10-11 11:57:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| ce528804-fd67-3fe9-b770-0f087e1f5a0f | -10.5274 | -47.3601 | 2025-10-11 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 23ead44b-d45e-3e99-b0b1-7a7e43ab3e4d | -10.9293 | -47.1553 | 2025-10-11 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3c0f78bc-545c-3f50-bd22-b500b01679dc | -10.2088 | -44.591 | 2025-10-11 12:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6e8952c9-f40e-3b44-a325-e175a959dd1c | -10.5084 | -47.3624 | 2025-10-11 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 87620f1f-92e9-38c4-a2e8-faf7f9607393 | -10.2085 | -44.6141 | 2025-10-11 12:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b0dbcbf3-f20c-3090-9f10-e7267c3ab3a7 | -15.0016 | -45.5958 | 2025-10-11 12:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 104.3 |
| d8a1c83a-c9d5-3ce5-87e3-78b9ad19c787 | -15.0021 | -45.5725 | 2025-10-11 12:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 176.4 |
| d23d0166-15ce-36e2-a89d-a0ef074f4636 | -13.22616 | -42.33943 | 2025-10-11 12:00:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 90d896ef-55ac-3d26-afc7-049de5357065 | -7.5501 | -44.29155 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 26dfdbb1-4d6a-3570-9383-2e87d34cead1 | -6.76063 | -44.95439 | 2025-10-11 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 75e972f2-61be-3839-84ee-035438f33c3f | -8.97742 | -46.90648 | 2025-10-11 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0708c41c-58d7-36d8-b989-dfaee94aab7a | -15.00063 | -45.58053 | 2025-10-11 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 1f0209ae-5c88-3962-8faf-236754b9f26f | -14.9992 | -45.59019 | 2025-10-11 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| fba21948-4426-3837-98b4-d8c264ebf331 | -15.01617 | -47.56315 | 2025-10-11 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c60a038c-9dd8-374e-8992-e10fa1f3731e | -10.52644 | -47.34346 | 2025-10-11 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 20f5eb82-5e74-3553-aa33-018fad696349 | -14.27808 | -45.90252 | 2025-10-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d84b3e68-e879-3f3b-b8de-93e6ab4cc7c7 | -14.56095 | -45.55566 | 2025-10-11 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 41a352d6-930d-3e9b-a472-f154344f137d | -10.19963 | -44.5994 | 2025-10-11 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| edaf8bf5-c0c7-3ce2-9e1a-4f32a69a42e3 | -7.35713 | -44.79499 | 2025-10-11 12:00:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4e456670-994b-37ba-841e-d6a2771260bc | -8.13599 | -44.45391 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9723d214-1b6a-34da-b081-29f1dbda1ea6 | -13.27858 | -47.13058 | 2025-10-11 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 4dfaecbe-d705-3c09-9212-795750ee8f8a | -15.57593 | -45.31086 | 2025-10-11 12:00:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 02afd82c-3d62-3683-accd-5a52ba48cbca | -8.50206 | -44.60186 | 2025-10-11 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 8e5efd71-4c94-3861-a69e-65988ec79d83 | -7.84469 | -44.55168 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9bceef52-37ec-38a6-9f61-e05693668bc0 | -10.51581 | -47.34172 | 2025-10-11 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 12a944b3-249a-3dd2-95db-3d586f74ddbb | -7.52976 | -44.61715 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| b1f23e78-6598-3d5a-b61f-69bdfa12227f | -14.5519 | -47.3179 | 2025-10-11 12:00:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| eb4463a5-1b8d-3c4d-a983-1572bedb7d6a | -9.12377 | -45.06636 | 2025-10-11 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 7737f6af-ad93-3b46-a171-da55d4d105f3 | -15.00969 | -45.58192 | 2025-10-11 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 40de96d8-cc4b-383c-9476-7012b1068259 | -14.83615 | -47.33587 | 2025-10-11 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0c237ee9-fd57-3eb1-b8e0-c2ba6ff41250 | -7.85765 | -44.46381 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d7e3763a-0809-3365-a32e-c6232c617343 | -16.23076 | -44.80568 | 2025-10-11 12:00:00 | TERRA_M-T | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f5f7bb1e-ef50-3e7e-9cd1-0f6bed36d953 | -8.50349 | -44.5921 | 2025-10-11 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 537.5 |
| b7e2bd11-ec73-3d50-931a-988aa9c1b93c | -12.50065 | -43.17122 | 2025-10-11 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 8eac5d0a-c067-39c7-8960-2d02a4c9cc6a | -8.0146 | -44.45971 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4d925fc2-e36b-342b-bff8-48f3e4ad0b39 | -8.166 | -44.0615 | 2025-10-11 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f4b351c6-260d-3e09-b2e1-b2d09e5bedad | -13.31134 | -47.11747 | 2025-10-11 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| b03d1e1d-8f22-3e05-bdaa-972048dd34af | -12.38779 | -42.53804 | 2025-10-11 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 5ced58c1-96ee-3f9c-85b3-60c8b3b566ad | -12.92653 | -42.30787 | 2025-10-11 12:00:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| c6b5eb14-80f9-3a32-a3af-f06bdc86c4eb | -6.91776 | -43.57732 | 2025-10-11 12:00:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| afbdcee8-d110-3160-9c7d-144533438ce6 | -7.84282 | -44.80056 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| af88a2b8-2c40-3a53-97c9-9af74fafa470 | -7.87183 | -44.49543 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 4ba95e84-6fec-3536-86b2-1cef2b3dbbc3 | -8.49589 | -46.1608 | 2025-10-11 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 67dec9eb-3470-3138-9750-4d6facdf6cdc | -7.3219 | -45.32084 | 2025-10-11 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d97f3e4d-748f-3faa-8968-a914d01ae212 | -10.2073 | -44.61024 | 2025-10-11 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 9cb492c5-9064-3818-8212-42e10a1eddc2 | -15.30198 | -43.8335 | 2025-10-11 12:00:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 175e3ce6-3677-368c-9df6-f5adf9e44e7a | -14.99302 | -45.5695 | 2025-10-11 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 208.8 |
| ba5c7fdf-7e59-351c-bcb4-c8d9d21e0ec9 | -15.02506 | -41.67833 | 2025-10-11 12:00:00 | TERRA_M-T | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| cc0aef1f-36d2-333b-aac6-9889795a0760 | -10.42678 | -44.99469 | 2025-10-11 12:00:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1e049ad1-22ac-377e-be41-20748572ee65 | -14.99444 | -45.55992 | 2025-10-11 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| b25b64da-2573-32de-adf7-05bcccef4546 | -16.31262 | -47.14704 | 2025-10-11 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5d109640-2f0c-3709-b480-ea2bc83ff727 | -8.20106 | -43.31612 | 2025-10-11 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 147696f9-def3-31a4-b5c2-f59681b3bd5f | -7.87326 | -44.4857 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| fb5d42e8-3ad4-3cf4-9184-f63bf88c99de | -12.74929 | -48.65733 | 2025-10-11 12:00:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| ca5f0adb-e90a-3d31-909c-56a0e02a0355 | -10.84531 | -47.14533 | 2025-10-11 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 94fd90cc-65cc-3ebc-9310-6ea86b0cde50 | -9.40534 | -45.77564 | 2025-10-11 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0cfc3652-0241-37d0-9c3c-266e155e24f7 | -12.46011 | -43.20221 | 2025-10-11 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6ea6d5ea-f743-3412-a027-59cf81c37eb5 | -8.8326 | -44.42009 | 2025-10-11 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3eb61caa-b949-3d17-b02d-57b16cee466a | -13.3324 | -42.37037 | 2025-10-11 12:00:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3b85b5c9-e16f-3b7e-bb32-776ad65cccd6 | -12.74064 | -48.63914 | 2025-10-11 12:00:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 7f608fde-df03-3ad1-86e0-7ea2a55f7134 | -15.69792 | -46.63082 | 2025-10-11 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 2164677e-63b7-3ac6-9abb-89bb656f6f81 | -13.49209 | -42.01649 | 2025-10-11 12:00:00 | TERRA_M-T | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a029681a-7a75-3384-a9eb-eb993cb874bb | -7.41132 | -42.97443 | 2025-10-11 12:00:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 75d10fd1-c920-3f5d-9669-be2f59146517 | -15.11164 | -41.53801 | 2025-10-11 12:00:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 3cc16ec3-5b45-394a-ab08-70b3c63d5649 | -11.72222 | -44.28989 | 2025-10-11 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7c4b7520-3538-3ca0-8d58-519f70e44455 | -13.30958 | -47.97242 | 2025-10-11 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a0088234-c235-3994-9e7b-5b6594b1d77a | -7.86261 | -44.49409 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.9 |
| cd36d782-d24c-327b-9535-9178cfa74ec1 | -12.50786 | -47.40735 | 2025-10-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 65a4bcd4-118a-37ac-9566-9b2ff025220e | -15.49062 | -47.99459 | 2025-10-11 12:00:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2be3948e-6d3f-3dd6-bd8f-6b3e6dd765b4 | -14.03174 | -48.14259 | 2025-10-11 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 477d7724-d0f3-37f0-96d7-4ac8bba8f5ab | -7.86404 | -44.48437 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README48.md)
