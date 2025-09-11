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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a06f27c-eaed-32bd-bcfa-c305dc0c0406 | -7.38733 | -50.89003 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f600f48-b119-37c7-9bb7-16f807e02bfc | -3.85924 | -55.99435 | 2025-09-11 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e25a84d5-1259-359f-ae69-de4b6d9336e9 | -8.05337 | -52.32701 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c624881-9980-3596-a3c7-023d52aab4c8 | -8.64527 | -45.72315 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b698f660-413d-37ac-adea-0ddb885231e2 | -6.25357 | -51.83055 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d9414e8-5ad0-3d78-a90d-d15622ecb1c7 | -2.94633 | -49.34745 | 2025-09-11 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d261390-853e-3cbc-a1e8-e18226fa1429 | -6.1698 | -41.07957 | 2025-09-11 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f848aea4-0376-3696-bbdb-58c441ea149a | -5.86356 | -44.22539 | 2025-09-11 04:44:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ac8bd111-5739-3c3b-acf3-b9842487d2c2 | -8.76004 | -47.11447 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c1a0194-ab32-3bfd-adde-f261230f310a | -8.96888 | -44.93436 | 2025-09-11 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66f6b781-e6f3-37f3-aeeb-3fc10ac4e9c2 | -6.39534 | -43.51204 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7adbbb39-e93e-30f2-ba90-56bb0ac6f3d1 | -6.17173 | -41.07992 | 2025-09-11 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 25cd90cb-4232-339d-9073-55fefa25906f | -5.59048 | -51.94154 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86c10eb9-1371-3c36-845a-8a51ec8d67b7 | -6.69948 | -44.94046 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3752494a-b22a-32a9-889f-651330d94bc1 | -7.54049 | -44.6731 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac2beba2-30e9-3dd0-a2c7-d6f78e4818d6 | -9.05269 | -46.97747 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c640c168-b309-359b-85a6-0368b773b885 | -9.08055 | -47.08944 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9875835b-1236-3e83-8f5b-c276645f8770 | -7.20143 | -44.94295 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a93833ba-591c-3af8-970d-ac67f4f060cb | -6.83739 | -45.60925 | 2025-09-11 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44d5cae7-2417-329a-a50f-d2a970b16ddb | -6.19998 | -45.656 | 2025-09-11 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 088b6a05-335e-3448-89c1-d48510b7fc7e | -5.72945 | -45.41335 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5ffc199-5e60-327b-a614-37f0d5d309da | -7.38512 | -50.88251 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4fd666b6-0d94-3b70-8f66-797a0ae9fbb7 | -5.10891 | -46.24044 | 2025-09-11 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25d05ff3-59d8-34bd-8713-30cb937f440c | -8.04989 | -52.39188 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e84e387f-1885-381a-b152-ca09131e3a1f | -7.11432 | -50.76814 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11d03987-bd31-3c4b-881e-5a356d518e5b | -6.66397 | -44.12655 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 716cad3e-fb83-3d88-9644-b618523fca55 | -6.81896 | -44.88763 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| acc5d699-e0ae-36e2-b1c4-48c834b25f0c | -8.23622 | -47.86203 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffaae099-6d2a-3c4e-ab21-57c59acfca0c | -5.97394 | -45.80951 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85da8994-5e93-3504-8e5a-be989671d749 | -6.31696 | -43.44593 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f51719dc-a6aa-339d-b6d7-607275bb7699 | -6.58041 | -47.3465 | 2025-09-11 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2819a9f-1bb3-345b-96b8-dfd6043e0533 | -7.19347 | -44.96709 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfb9c7ca-ef5c-3a76-9e1b-6452f9339327 | -6.24616 | -43.42826 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e0d80455-c75b-3485-98d7-c5f9b4ba710a | -6.81872 | -44.88596 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a5839e7-770d-35e2-9d53-32053941ab87 | -5.59962 | -45.36071 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac156768-61b6-3293-93c4-802b3cf4bdbd | -6.74927 | -51.96 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7232f9ce-6581-3c41-82ad-76eccc2a24e9 | -8.1086 | -44.84939 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80e92fe2-c117-3eb5-9fd1-1265b779b6f0 | -7.20222 | -44.96831 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88f6dd68-f9d9-382e-8c19-4901749c2da9 | -6.53201 | -44.60689 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 995f9c62-a8cf-32a5-9c1f-042fa2696d2d | -7.67671 | -50.27489 | 2025-09-11 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce3f7eb4-cadd-3e6f-8b58-5d7f18feba94 | -9.05881 | -46.96297 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 22b42435-ffc4-3b54-89d9-a5faff700562 | -6.83745 | -47.90275 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c28d516e-cbe0-39f4-a8b6-fe2cb314b6b0 | -8.07802 | -52.38153 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b7fd968-cc4c-3e14-b6a1-d72f89d0f8f5 | -7.99262 | -45.79706 | 2025-09-11 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1e7a52e-b769-3743-a604-fd9279044be1 | -9.08213 | -47.07745 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18a55347-7f9f-3a5d-b96a-52a7cdc96cbd | -5.66332 | -43.89558 | 2025-09-11 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9408835e-485a-3148-b15d-d32c3fb11ffa | -6.25218 | -43.48982 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f2222c6-6e39-3a6b-b7d7-860b328d895e | -6.82469 | -52.80012 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcd64f14-caab-3cd3-91fc-01336f53608c | -5.74903 | -51.69305 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dfeb13d-2447-3484-9d04-3419a552a2aa | -9.06599 | -45.7014 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b30b1755-cf8e-328b-bb1f-5b50ff585e55 | -8.0376 | -49.04516 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc1470a8-4e15-362b-9fa8-9a13610bf8d0 | -9.08266 | -47.07442 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd152d14-49bc-32ce-a80a-16f4af0f84b0 | -6.25655 | -43.4242 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2fd30151-25af-32e8-9328-48aebd64b295 | -2.21745 | -48.22827 | 2025-09-11 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1ec7f1ed-184b-3a64-9f78-67ce4933ec3a | -5.59168 | -42.89559 | 2025-09-11 04:44:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f45b8303-2452-3f22-bf99-c66141c37db2 | -7.26359 | -44.60791 | 2025-09-11 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6006671-468b-3d6f-a3d0-c5f4368c10c4 | -5.67921 | -45.46687 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a5e4e57-1a19-30b3-b3f6-de1cb2a10b7a | -7.21655 | -45.30995 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f35d04c7-e215-367d-8b37-3591b09f3278 | -8.05726 | -52.32406 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1a30f79-3931-3bcc-b055-a767d9a6a99f | -8.03818 | -49.05267 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eaa5475d-a0b8-3d6e-bbfd-0908fe447d67 | -8.02368 | -49.04301 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61eddb78-e583-3701-86f4-dc3c2f053bc4 | -7.79177 | -47.94023 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5410f00-7aab-328e-8c19-91690a05fbec | -7.16544 | -48.88665 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eafdecdd-dc01-39ff-bdbe-fba8ecb980c2 | -6.38149 | -44.43266 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f200b9c1-6415-3f9b-960b-27a457ffbc7b | -6.40084 | -47.32818 | 2025-09-11 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76e0ddb8-a3e7-34ca-8c49-d7559be3f776 | -4.58565 | -45.61245 | 2025-09-11 04:44:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fde52d8-2342-3a85-96fb-6e6913b8f0ad | -7.83277 | -53.26697 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b317a9ac-c5c7-3160-a301-9add571b71d5 | -6.10059 | -45.93393 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c8bf17f-afe9-3115-b357-b4348ac4f778 | -7.38788 | -50.88655 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1f25217-e8c2-3927-9974-e35a4b67cec8 | -7.53534 | -44.67718 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d2f45586-8fc7-3be8-8817-01ea242a38b8 | -5.65145 | -42.6258 | 2025-09-11 04:44:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c54fb975-3383-38d2-8609-cbcaca1df3fc | -5.47301 | -43.43509 | 2025-09-11 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cfdad2f-a6cf-33b6-8406-e90c4820b23e | -6.25806 | -43.41382 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 56e323f1-e34b-36a9-9433-c89538628eaf | -8.73288 | -47.1103 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2657305-3094-392c-9286-5809e7580638 | -7.92116 | -44.86515 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dfc06aa-b23c-3648-8185-532c59eac6eb | -7.83711 | -45.40126 | 2025-09-11 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c53dcb80-c327-39fa-9a10-5fd75a1f6344 | -2.74163 | -48.68444 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9586b1d8-a49a-3eb3-8807-a8431d32d9c1 | -8.81128 | -48.09082 | 2025-09-11 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f240e88f-7968-39b5-80af-e4ad77f8d91e | -7.23375 | -55.05111 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47e1a9e2-313f-38c7-b9d7-68be36852d3f | -6.35037 | -43.41807 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72488c9e-45f1-3a0c-a39b-937dcd2c90f0 | -8.80329 | -48.09404 | 2025-09-11 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3644550f-5e09-352b-be64-39b0221375d0 | -5.93743 | -45.71957 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48ca2f56-d7df-37d6-984d-66938feeb534 | -6.21523 | -43.37048 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b4d32836-7995-36c8-ad8c-2bed5e414c06 | -4.41569 | -47.95511 | 2025-09-11 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30c4c461-a88b-3e46-baf2-c9a3e83cc449 | -5.36483 | -45.9695 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02616548-9362-325c-abf4-e0d875b9acc2 | -6.54507 | -42.44099 | 2025-09-11 04:44:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b52b53bb-8de4-3d6b-bbd7-280a9af064da | -3.73703 | -53.73631 | 2025-09-11 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15cda8ae-2079-3179-a815-0d6e8a921f23 | -7.87801 | -46.02385 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b778e86c-e0d0-35aa-b902-bfe949d2b637 | -7.56032 | -48.21459 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fc3f04b-c642-383b-89ff-70f4fcbc9832 | -7.5032 | -48.27768 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2c0d051-0557-3ad0-aded-0e9887ea8586 | -6.40087 | -43.50743 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cf6913e-4228-3fa5-b824-62aff6bbe769 | -8.44198 | -47.2706 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 39781b9e-4887-358a-8db4-aa9311fb3348 | -9.05736 | -46.97299 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddd47abb-4b31-3cb6-bde5-366ae869470f | -6.80981 | -51.87985 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f0ff387-e6ab-31b7-ba82-d9bb7a8686df | -5.86493 | -44.21589 | 2025-09-11 04:44:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5d5e137-9c7c-34c5-9cff-13b6ad2cc102 | -4.93108 | -55.7872 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5bb99ca4-beac-3990-9338-05e2f08d989b | -5.91859 | -42.75941 | 2025-09-11 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dc4b5726-08f1-3b7b-8a80-c98d1188af5c | -7.91922 | -44.87909 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db655b22-3d5c-3df7-a89b-118a60cf7894 | -3.73751 | -49.04232 | 2025-09-11 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01091e0d-6342-3c93-9590-a10cceb319dd | -6.27561 | -43.39451 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README93.md)
