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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bc72f30-4946-3996-bfa4-ce35226874bd | -9.09377 | -46.93851 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 558d634b-3634-3fa9-a70a-44313128d735 | -12.49377 | -49.13929 | 2025-09-16 04:51:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a902763a-b2e8-31ca-9bfc-73a8d30efa11 | -8.58229 | -46.35904 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3928f64a-1a51-3dce-8718-7980f84c2c5f | -10.05649 | -47.17946 | 2025-09-16 04:51:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e697c966-0b9e-3263-aac8-ce9eec72b205 | -12.84039 | -47.20081 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0cfc8681-28fa-3517-8ab5-407f2892a826 | -8.08861 | -50.15699 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db96d922-d4a2-351e-bcda-0ee4c56b445f | -11.10745 | -45.33744 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a7f82f1-9fca-316b-b657-6127f2219250 | -10.71664 | -44.75601 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 577d9244-d370-32fd-9af8-cee9893cb0af | -12.86227 | -47.14524 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a11dfabd-8e6a-3bbc-a11b-f9447f637c6f | -15.62172 | -47.37119 | 2025-09-16 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8e1ef51-4e94-333c-a38c-f203c4dc6cdf | -13.00507 | -47.94453 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f1807fd-5254-3df5-ab3a-daf74d42dce1 | -11.07106 | -49.73782 | 2025-09-16 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dc7910d-4b2e-3d3b-a600-6f3682324b3a | -12.77942 | -47.92507 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c0198bc-5027-3e5b-b375-58878463aa6a | -12.69826 | -47.99136 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 74f0b53d-1f69-3dd6-948b-7dd5f4551212 | -12.7004 | -47.74331 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c492d70c-1c32-33a2-a488-9c802985c114 | -10.73366 | -44.75597 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed3a9a9f-24cb-3f7a-bb52-13a498017d44 | -8.97441 | -44.19165 | 2025-09-16 04:51:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0c37081-6216-3b66-bdc8-1ebe5453f856 | -14.66181 | -46.84294 | 2025-09-16 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b1e0e2c-9c50-3f36-8f8b-a52bba4e8465 | -14.90494 | -51.67102 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fbe682c-20da-3eb6-bed2-e2aa84d6e7a3 | -10.71417 | -44.74255 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aba26e89-86ac-35d1-9995-e20a82d28193 | -14.80781 | -51.67016 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| bac4ef21-48ad-3b19-96fe-5f6ee6888212 | -14.65014 | -52.10045 | 2025-09-16 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ca02c41-b7d2-3697-912b-7d538ca76a44 | -12.96136 | -47.96154 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bbf4704a-eab2-31ed-bb2f-828078567efe | -9.74313 | -55.37816 | 2025-09-16 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3f574fa-b47e-37b0-8e48-8f9491de3ae9 | -14.82638 | -48.12199 | 2025-09-16 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc7776cc-44af-36a1-8d95-e4e63242dc5e | -8.59383 | -46.34218 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 13c3611a-0d2d-341c-a122-c954d78fac46 | -13.78099 | -54.95699 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49c08299-a665-32e0-9b9e-f7687f91b04b | -12.75547 | -47.97382 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 504eff63-451d-3855-bc61-a17f8f42879a | -10.72246 | -46.48994 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 1c150a35-9ac6-3e43-8df5-20f141429113 | -12.80589 | -47.25214 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 64725c2a-f7ac-3dc1-8db7-aa84f86284a7 | -11.1341 | -45.32937 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7307f755-c56a-34d1-a87c-a1dc99a30add | -10.63357 | -48.74623 | 2025-09-16 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d9d4d02-0c8b-3cc0-957d-bc5c85f54d4d | -12.28755 | -46.40931 | 2025-09-16 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08e1afdf-607c-3398-8f3c-c0704e8734be | -9.05747 | -44.84592 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8786cde-d67b-3fb2-aa3d-ec9e269a0525 | -10.71013 | -46.51201 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 95d26c64-da7b-381f-bed5-382085d6ff04 | -9.73724 | -48.12577 | 2025-09-16 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57d4cafa-c560-3f17-a363-5f274f5613d5 | -10.8862 | -55.66073 | 2025-09-16 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80b6d627-01be-3281-957f-0467b2b7a1eb | -9.06919 | -44.83543 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24f850fc-a9f0-3e16-9d45-d9a0208be5ca | -12.96078 | -47.98056 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e652c8c7-b6fc-3c2c-81ec-d36a34168c85 | -13.73957 | -48.7672 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53c1a70b-b614-3b47-a9a5-cd3090b4f98b | -9.08784 | -44.8496 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ba057c8-cdd7-3447-a57e-a505ea10e86f | -9.09433 | -46.93453 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85618d63-c451-3ae2-9a74-d940f9130df4 | -14.35934 | -52.92015 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23776307-8c5c-3e15-a572-0bde37d93b5d | -10.72926 | -44.74893 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67d2e80d-6af0-32a2-a305-88d926083be2 | -8.98119 | -45.75935 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3629607-14be-3541-bdbf-1aafc704c232 | -10.71742 | -44.7588 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e832a12f-5491-3b61-bbe3-23fe78aca8af | -9.68507 | -62.0027 | 2025-09-16 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed3b8d42-1f43-35ce-86ab-99d1b9812b2a | -9.53484 | -62.3801 | 2025-09-16 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4992d2d6-7885-3ea0-84d9-cee20ee012ab | -11.42489 | -46.92922 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3ec2ffa-c0f4-30d6-8e85-df658de2f1cc | -12.6586 | -47.71684 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff98b5b6-300b-33df-829b-c59b704b671f | -12.85839 | -47.13927 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a80cbf23-9460-3dd3-b935-ef3e341066c4 | -9.98358 | -64.99434 | 2025-09-16 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c94bfa09-3c0c-347c-9688-076b4f257893 | -9.09418 | -44.84101 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b078a47-8e24-37cb-a0a8-95b2c339a6cd | -12.81281 | -47.23469 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60f7a2a8-f556-30e6-b0ea-1e1f7e0ebc93 | -8.66585 | -46.36457 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3534e44-c9fe-3c21-b6f1-8bc1e4fc0a30 | -8.97555 | -45.03717 | 2025-09-16 04:51:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51f8ac5d-7655-3dce-8127-097cf892e7fb | -10.43724 | -50.65498 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f024312-887d-330c-bbb4-c3bf17076b76 | -11.44205 | -47.30564 | 2025-09-16 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83491c8c-96b9-3d37-a0bd-cf628480e241 | -10.43066 | -50.65607 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73304daf-f230-394b-8bcd-2c07f63251b2 | -9.09683 | -44.85091 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 459ec120-2cef-3427-b126-7d166ff9d46a | -13.28273 | -54.24503 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85097c0b-b1d9-33db-8629-d7657dea2254 | -9.08699 | -44.84755 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1825e6f3-0877-3c76-b8e6-3d4bb3f72273 | -12.63258 | -48.00345 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1be50b56-fa40-3010-a58c-7be812acaf09 | -13.20743 | -47.28895 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72b729ff-6dec-32ce-8790-b3ce5d505aa4 | -12.79166 | -47.25543 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3627eca1-9a8f-39cc-9304-038491190381 | -13.00882 | -47.94946 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13b590be-57e1-3915-879a-04237d1d947a | -10.07007 | -48.17915 | 2025-09-16 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 096d346b-8fd2-3ffe-9992-914ce42a10d2 | -8.9266 | -54.44323 | 2025-09-16 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0494b084-fb4f-3370-873d-43dc6942c6c0 | -9.09981 | -46.92739 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ba44836-1154-3846-8824-d13e8ee6bc73 | -12.79564 | -47.26011 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3eb38953-c9b9-3ba8-a918-8a3aff93f9b9 | -12.84476 | -47.13354 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d1cf40dc-0dbd-357d-bf62-11e2ae2a463a | -8.84166 | -47.94663 | 2025-09-16 04:51:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbf28ab0-f53b-3495-92a2-a5d22f75ca17 | -8.62462 | -45.7203 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 784f3750-aa03-3e72-a8b7-4147953160c0 | -9.86856 | -46.45173 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96f64b3a-49a5-3a6c-a2b6-960c0a242079 | -10.88495 | -55.66831 | 2025-09-16 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ffa7ff3-4c64-3372-9501-88e86e0a742a | -8.91358 | -46.15571 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aec9df7d-cb0c-39e0-a0e4-de6e6fbe1053 | -9.09757 | -44.84527 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbc9e186-09ff-3461-8783-1fbddc6f1cae | -10.8885 | -53.75075 | 2025-09-16 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee85bf4c-b1f5-3243-a712-128b39f1f6f5 | -12.68163 | -47.98487 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a2cdd33-9fcd-3ae7-826b-d1800340d37a | -12.97211 | -47.96096 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05b11926-2a36-3a1c-b221-07f822343049 | -12.82252 | -47.231 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c16fc5b4-5a85-3097-8f57-c726f64cb750 | -12.00768 | -47.75602 | 2025-09-16 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2af47bb2-73ee-3008-9ccc-f9e8adcfe358 | -8.60361 | -45.73283 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c15e8357-268b-3933-b5cc-d05c2a00a609 | -11.4625 | -46.92414 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da67371a-eaa1-384d-8972-9b68e983d916 | -8.03631 | -49.83476 | 2025-09-16 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 07fb915b-6bf2-3039-b2b5-2dc42583a3d9 | -12.86172 | -47.14955 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00b8a9d9-629d-36e3-adf2-fe76324a668f | -12.2984 | -46.40044 | 2025-09-16 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9ec1aac-ffd3-3677-aa0c-a25102ab86fe | -11.02545 | -45.06235 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d405d490-a4a5-3c34-bbf0-fd14de0eacef | -11.43333 | -46.93515 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eafb4049-04c5-3770-b8a5-e26a7531214c | -11.13108 | -45.35239 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a9bb752-0cbf-34da-a358-99464330788e | -12.44257 | -49.70076 | 2025-09-16 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6287b8a-5d94-3c3d-9d2f-fd7b4f2f29b6 | -10.7226 | -44.75966 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 169fa948-e0bc-3a8f-88f1-5dc51a7bd147 | -12.74232 | -47.20958 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a60bbf03-540d-3fb9-9e8b-81bec42e0da2 | -9.4539 | -48.60476 | 2025-09-16 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1cb3672-03f1-3970-a1f1-cb8739a158ee | -14.82201 | -48.12125 | 2025-09-16 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7650965a-91bc-3e7e-a89e-bd14a45033e2 | -9.09569 | -44.86718 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 034b8088-5bc9-3cc5-866e-8bdb003dc60f | -8.0993 | -50.15839 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 051501f7-fee4-3213-a521-963474be3ba9 | -12.61135 | -47.96691 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f6d74a9-bc07-3449-9d84-ab570274ce89 | -9.04697 | -44.84748 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f3e835d-9c90-3169-9cb1-0153e8161ab2 | -13.70834 | -49.85684 | 2025-09-16 04:51:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README76.md)
