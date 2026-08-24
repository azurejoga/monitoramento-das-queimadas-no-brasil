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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8574f962-a576-3ece-af40-899d1f8079d1 | -12.1435 | -43.39259 | 2026-08-24 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38e576ca-8947-341a-b779-d78f7980b258 | -7.17399 | -42.74235 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 565ac6ae-9a18-38c3-87e9-7428c7792f2c | -7.89943 | -46.32617 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d4ca0e6-1c89-3385-8586-41efa0e8be7c | -7.29376 | -43.00856 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| bb90be46-4f1a-3764-8c77-7ce3ca8d1aef | -7.1782 | -42.74301 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59a2d4a1-f82b-36e5-9804-9656fea7c3c3 | -10.55332 | -46.31432 | 2026-08-24 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7b834c8-c329-3fa1-aeaa-903a7490ea6c | -12.74177 | -46.46184 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4cc24ac7-4377-3151-abc8-520e436c0742 | -7.35639 | -45.82362 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| efe570fd-35e2-3572-bbd3-5c0de3068fbd | -12.21481 | -43.17385 | 2026-08-24 03:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 23203057-8661-354d-92b6-9d87e0116c97 | -8.79533 | -48.31476 | 2026-08-24 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90957af5-6527-3eb4-9c5b-5ae001aec7d5 | -13.51252 | -42.77188 | 2026-08-24 03:49:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 45f6e675-c629-311b-9a1f-e883239eb1d8 | -7.15644 | -42.79537 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0a96537a-7638-35e1-bc2b-502c2cc475a1 | -10.46191 | -46.22128 | 2026-08-24 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a18e3abc-45cd-30ef-ae59-8d8b3337f95f | -7.36668 | -45.82553 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 39de9abe-446e-3a9a-98b9-2fbf9cc41f36 | -7.24626 | -49.86442 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 65babf64-dcc0-338e-8313-7dae2f9bf68f | -10.03966 | -46.43386 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f40ead82-d58f-3016-94b7-59f0bb644e95 | -9.30258 | -40.22328 | 2026-08-24 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 48553b17-b832-3247-b5b1-d37590a3ac00 | -7.89839 | -46.32775 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38fe41d0-ceb3-3355-9542-271a34dcdce4 | -6.78902 | -44.66158 | 2026-08-24 03:49:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf680fcc-48dd-3dea-bcda-593de34527a5 | -7.35345 | -45.81039 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a045e809-cca6-35b4-8071-e14fa2ea6472 | -7.36024 | -45.80209 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dcad58bc-ae94-33fd-bc3b-3bb129f8f197 | -12.02604 | -41.93153 | 2026-08-24 03:49:00 | NOAA-21 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ffbf8f67-c028-3dc6-8f25-272c9f3079f7 | -8.07484 | -47.25561 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c7bcff7-d569-3bcf-af6e-32dc7cb92050 | -7.24097 | -49.87679 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| fd2c6e1c-9f11-3490-89eb-a243a572c624 | -8.59359 | -49.99629 | 2026-08-24 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5840d08c-3b20-3bdd-96d3-dfaf048a122a | -11.61974 | -51.09082 | 2026-08-24 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4581fa8a-bf3e-3ae2-8da9-0b713baeefed | -8.09278 | -50.04984 | 2026-08-24 03:49:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 88a22330-debf-3cb4-80e8-4ffef2dca669 | -11.11593 | -49.88827 | 2026-08-24 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84daca54-f709-39b1-9949-7483a3a06edd | -6.94721 | -42.69676 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 534ebcae-8ce6-3f94-bc7b-4d9d3bad5e39 | -7.24474 | -49.87265 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| eaebef6b-8b9e-3ffa-bfdb-c77f6ce82a53 | -8.80123 | -48.31592 | 2026-08-24 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 170e8851-aaa3-39d2-9eb1-2d9f4c16a8db | -7.36485 | -45.80603 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bed07181-413a-3c01-a15c-28d594d410a6 | -12.40217 | -42.90557 | 2026-08-24 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c2187df4-d0bd-3c0c-a392-8acae76e9b62 | -11.57839 | -46.95663 | 2026-08-24 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69b8b64c-5b50-35d0-8a63-de9728a0c6fc | -10.7372 | -47.97773 | 2026-08-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41753d1d-f4b9-3de6-ac3a-da014c0c8a91 | -7.89468 | -46.32221 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6733c17a-0504-3c66-95bb-f2e7e5f04591 | -11.10319 | -38.5988 | 2026-08-24 03:49:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 349b9fac-d41c-3e97-832d-139aee97f55a | -13.09772 | -43.35427 | 2026-08-24 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 52cf6593-9766-321f-871f-b6e997effc99 | -7.24163 | -39.3768 | 2026-08-24 03:49:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 116bcc78-9785-3347-9bc6-f480d2ef2a8e | -8.09822 | -47.47847 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bcf5536b-5e28-37d2-a8e6-300d68da070e | -12.4037 | -42.89865 | 2026-08-24 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e0d212e4-4179-3bbc-ac5f-66de2b6dc318 | -7.97065 | -45.26344 | 2026-08-24 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b26099a0-bc16-3dfa-8e31-64fae1a3b7fa | -5.06451 | -49.38245 | 2026-08-24 03:49:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae34f34f-070e-3278-9aab-ab919948e944 | -7.15942 | -42.752 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6df09a56-41a3-3d30-aaf1-83e1c1620942 | -8.31075 | -46.89655 | 2026-08-24 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f219bb53-ab94-3a94-ad05-cc9a932bdfea | -9.4446 | -40.52697 | 2026-08-24 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd7579d9-0c46-395b-8b1a-7de024dd4e10 | -7.97332 | -43.92578 | 2026-08-24 03:49:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8a5e617-5876-32a8-9828-446bf718e19b | -12.75236 | -46.44404 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19d095b0-dc7f-3727-b18d-8c4c5844b7b0 | -7.28285 | -45.36882 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f50348e8-ab19-3971-9907-df9778059652 | -13.09573 | -43.35186 | 2026-08-24 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dcce5303-2365-3893-ad0a-4eb45eeb3e56 | -8.10745 | -47.49235 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d6fd8f9-f6f2-3f9c-bbc6-fdffa3fd160a | -10.79895 | -50.94926 | 2026-08-24 03:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f72b072-669d-3e39-96fd-7b3bf3e2134a | -11.10968 | -49.88702 | 2026-08-24 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75fb6ea4-5323-3dc2-8e9f-83303ad99efc | -7.35454 | -45.80427 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3b20f77-a79d-3cad-b0e1-8bd570647a8d | -7.25217 | -49.8697 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 3d80e395-9934-3898-be3d-ea60889188af | -8.10321 | -47.48329 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e14e20a0-99f2-337b-8027-9c7e576a2160 | -5.627 | -48.42254 | 2026-08-24 03:49:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be52febf-8e64-3dfa-b0da-dc8bdba2d827 | -8.10067 | -47.47811 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8971c787-5d7a-3f97-b8c9-e37aa785cf92 | -12.25667 | -43.13527 | 2026-08-24 03:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 98060adc-70b9-3cb6-a204-ba038fa43f73 | -10.04202 | -46.43655 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb29df57-0fb8-38b8-94d6-ecd324f2ce61 | -12.13412 | -43.39847 | 2026-08-24 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d886e438-4441-3182-8623-aebcbb2719cf | -10.73085 | -47.98056 | 2026-08-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 062542f8-dbf2-3ce2-8add-eebf5905a30f | -7.48869 | -45.13753 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f59411e2-05f6-3841-ba9a-4484921e0648 | -11.61854 | -51.09676 | 2026-08-24 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8026623b-14a3-3d3d-b979-8c28444f7bc4 | -7.36098 | -45.82768 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 7487f7db-42ed-31c5-ab73-92b07c4f0301 | -10.55276 | -46.31738 | 2026-08-24 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8810ee0b-5a5e-3271-9369-8ee7224476fe | -10.47468 | -40.55631 | 2026-08-24 03:49:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9b065ba4-48a4-3257-8ad5-33fd4171cd49 | -7.26785 | -45.36608 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54f2b779-807f-38ad-8052-6fd6b6b3361b | -11.14608 | -46.17785 | 2026-08-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 43486018-13f3-3d6d-ad77-3d538a4af010 | -8.81457 | -46.61151 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a58c157-0293-3a2c-86bc-87da61d5c349 | -10.86424 | -50.98534 | 2026-08-24 03:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c205ef2-6f8f-30c5-9d47-13750b0a2a03 | -9.05872 | -50.77462 | 2026-08-24 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2a93a48-200a-3e73-9116-1122fcdece35 | -7.24285 | -49.86694 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 6780ed81-cff4-30ab-bb88-e1d39d8d5244 | -12.41405 | -42.9066 | 2026-08-24 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 848c619d-c09f-32c1-be37-f196147b6496 | -13.09375 | -43.35355 | 2026-08-24 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a511843-67be-3c72-8378-951786e40309 | -13.10262 | -43.34974 | 2026-08-24 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c07b8bc2-05d5-3714-aa63-2b36c72563f0 | -7.14536 | -42.80961 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0ec7d9da-2941-304f-84ac-70eebc1a7232 | -7.28235 | -45.37172 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ae0d760-c68e-3a17-925b-c5e39fb5b1cc | -11.6018 | -46.76349 | 2026-08-24 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c25f091-1d53-3431-a51e-2b40c785109c | -8.08045 | -47.25653 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 599ec43b-aae3-3dd4-9f1f-fa761a97f165 | -7.97224 | -45.2654 | 2026-08-24 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7e80d1cb-3f45-3d39-ab04-289bc79f6f12 | -12.2812 | -44.82454 | 2026-08-24 03:49:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19a37d02-78ee-35eb-917c-dd6438cd461f | -13.51759 | -42.77061 | 2026-08-24 03:49:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4f24395d-7ed1-3e43-929c-e5d4e2113de1 | -7.28835 | -45.36682 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ebbac4e-927c-3743-b3bd-09e8ae03005e | -7.28335 | -45.36591 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56d9ce8d-b16e-3113-a898-6c60f00a5d1a | -11.58414 | -46.95452 | 2026-08-24 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7958f7c3-6156-340a-8a76-9bde6529b684 | -9.7266 | -46.00784 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bce1a5e9-ab08-312f-8f55-6ee5559a4af2 | -11.55456 | -46.96209 | 2026-08-24 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5153e5f-98d6-3a86-9269-dc5962cafe34 | -8.98068 | -46.0254 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d4519d8-4731-3f1d-922b-337c494ea099 | -7.26704 | -49.9211 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ab7d51e7-3a7f-3296-b6fd-a06c895b0bf1 | -10.29065 | -48.20338 | 2026-08-24 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a6bffae-057e-39be-ab11-7eda32366e4a | -7.24201 | -49.87136 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| cc354459-dacb-3870-96bf-63ca22e8a4db | -6.9764 | -43.74868 | 2026-08-24 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60440e02-0126-3e06-a429-b2bb11a1af1c | -11.14709 | -46.17231 | 2026-08-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e21039b0-35bf-3d38-a7f6-f362cadcbda4 | -11.10375 | -38.59528 | 2026-08-24 03:49:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 03885d1f-4a7b-3c40-8553-26d3ff34402d | -7.24884 | -49.87168 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 6f554aa1-0d66-376c-9ff8-d7a9bd3a5ef5 | -10.73364 | -47.97746 | 2026-08-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c91f6bd0-2249-3d81-ac9f-88b99f56235c | -7.31986 | -46.14872 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 074ff09a-00b0-31dd-84d2-dd3747c117c2 | -5.07333 | -49.372 | 2026-08-24 03:49:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d838ff0c-bf7a-3460-bf23-aa89ca299f0b | -7.37239 | -45.82332 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README11.md)
