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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99de0827-cbb5-379f-889b-d4530128ff10 | -4.88509 | -41.50174 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf389bce-eaee-3afb-828d-fe6ef28fccce | -7.02656 | -42.12518 | 2025-10-14 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 74636bcf-62a5-3f51-bde8-28f2c39d040f | -7.95237 | -44.12008 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84d50082-295f-3e8e-a08e-af16fb7e8e2b | -3.93516 | -42.80636 | 2025-10-14 04:04:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5fcd9112-b53e-36f5-8f55-ce5b1b812ac9 | -7.90014 | -44.99905 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a5a1c0f-fac7-3cc0-9475-5c64e242766e | -4.86136 | -49.47754 | 2025-10-14 04:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a19dde9e-6c60-3885-b87e-798425012dc3 | -6.83692 | -42.7815 | 2025-10-14 04:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7742d1d8-db8e-3c04-9db2-2f80eed96b76 | -7.9501 | -44.13354 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| fc1dc099-228b-3729-956c-8cf9af36d78a | -6.33058 | -44.02151 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83ec7100-5bb2-3a9d-bdf8-94600a15ca9f | -7.25168 | -40.59447 | 2025-10-14 04:04:00 | NPP-375D | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 934e4484-7ac3-3968-aa9d-0cb6be0e0206 | -2.83681 | -48.83585 | 2025-10-14 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59d3b83a-2b2c-37a8-8d20-121a38bbd002 | -5.54622 | -41.3191 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a77f6c1a-d800-37cf-8078-fdb857fca59b | -6.90443 | -45.66369 | 2025-10-14 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9fdb129-34f1-35ab-a000-84fde4b67f4d | -6.57798 | -39.24555 | 2025-10-14 04:04:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 117ac06d-8c3e-32fb-88d3-8e58f16b0643 | -5.39985 | -40.87973 | 2025-10-14 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cb6d28ec-77bd-3ef6-a74d-01b16481c981 | -5.20951 | -41.6513 | 2025-10-14 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d6d3fae6-b2f1-3ca4-910a-85060a3e159d | -4.91224 | -41.54756 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d9bf1097-0348-3dc5-9f0e-fdac3821e7ab | -6.15533 | -41.76514 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 105b0d64-58ea-3c63-834b-9ad37876d420 | -5.8594 | -43.85213 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed38117a-776e-33e2-b5dc-2c709c92b95c | -5.73864 | -47.47546 | 2025-10-14 04:04:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6175fa3f-a49d-3b14-b7ed-66896f96047f | -5.10115 | -43.20142 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c29cff6d-ebac-3f78-b1fa-37fe1e74b165 | -3.15765 | -42.88952 | 2025-10-14 04:04:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 154527f4-f62d-38ae-8436-10b484dc0e39 | -2.87411 | -50.73717 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9039c6ab-3c96-303c-871c-44af4199efa4 | -7.75592 | -44.73158 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9a40a7da-6525-305c-89c8-2878ab09ea30 | -5.85338 | -42.6174 | 2025-10-14 04:04:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7e4222a8-c0c4-37a5-85e6-44ae4eda8316 | -8.2485 | -43.35225 | 2025-10-14 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5ff04216-84ac-3226-b249-36e744a012d1 | -6.33441 | -44.02202 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b32b547c-d93b-3293-a27b-936490445952 | -5.19121 | -45.39782 | 2025-10-14 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e0ced2b-aa6e-39d2-b08f-45b7301dc2dd | -6.14736 | -41.75283 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4d6b002a-72fd-3fa4-bc94-9a8316058352 | -4.55705 | -49.64433 | 2025-10-14 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 862ba09b-bfff-3323-a04c-67760ac757b7 | -5.2814 | -48.27492 | 2025-10-14 04:04:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 914d683a-1508-3673-85e2-3ba5d8789e95 | -7.89931 | -45.00402 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ef4e9c5-f523-3264-9247-64a6d998f176 | -5.63113 | -50.0328 | 2025-10-14 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45d84720-0c8b-36da-a646-85d32e193ffe | -2.53323 | -47.80308 | 2025-10-14 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 898367c0-9d0b-3702-a5df-b4bf07988122 | -3.62803 | -41.63127 | 2025-10-14 04:04:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4b327634-951c-3b4c-8a43-3d35ed7d8a9a | -3.13957 | -50.21212 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82a255e2-76ba-313a-bde8-c1463f026504 | -6.68237 | -43.5692 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4b54ba79-1ec0-3878-98b4-21657ff899d4 | -7.20763 | -45.48324 | 2025-10-14 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5b0e790-e584-3af3-bc47-6a41cd384885 | -6.43911 | -41.82873 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da4cba78-3c70-3a5a-adeb-7cd9310730aa | -3.15392 | -42.88894 | 2025-10-14 04:04:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7d1de12-67c2-37af-bd85-65a03c2e78e7 | -6.98781 | -47.09156 | 2025-10-14 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40804f39-e736-3d3e-8994-b7ca9cdd162c | -5.763 | -47.90683 | 2025-10-14 04:04:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e31ab7c-82fc-3ce1-88a8-6c06b8d17ebc | -2.44068 | -49.37401 | 2025-10-14 04:04:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82b8165f-6830-336d-b823-070e04f69e5c | -4.66439 | -43.13279 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| efc93e0d-9e5d-3bb0-a684-48216e75e85c | -6.54162 | -43.56084 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a798a5a6-1a90-3899-90cf-6adc805d02f9 | -4.00298 | -44.67044 | 2025-10-14 04:04:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7fc06076-1b3c-38c0-be23-aa498c486999 | -8.45637 | -40.55043 | 2025-10-14 04:04:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0362a637-602d-3d7f-ac16-985374a3204a | -6.84924 | -47.64491 | 2025-10-14 04:04:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f27bfb71-28b8-35bb-9348-5af909a053de | -7.62416 | -47.84034 | 2025-10-14 04:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fb31e48-e17f-3b60-a2d0-b480c9d202e7 | -5.59271 | -41.09303 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f91de864-5202-3614-ab34-b1d9d1805fea | -4.64078 | -42.52499 | 2025-10-14 04:04:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f30abdef-b72b-3940-a83d-3a746a0b22c6 | -7.30778 | -45.75858 | 2025-10-14 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf0fafe5-0de6-322b-9638-75d405691275 | -7.90489 | -44.99482 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21290bf2-4295-3e1c-a582-ba3b5e4df5d6 | -4.62459 | -45.77777 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a64f195-99db-3e09-8aef-0c7bf75576b4 | -5.847 | -42.32438 | 2025-10-14 04:04:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 89551140-4d59-324a-8fad-7202c9791ede | -7.75799 | -45.72766 | 2025-10-14 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 963fd9a9-b5d9-39a0-a23e-c56c834795ed | -6.33134 | -44.01683 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34a8613e-4733-3e54-b4bb-25409298462e | -4.67036 | -43.14277 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 72b8c18e-cf88-33d3-a7be-3b22a54c5183 | -3.4332 | -50.2507 | 2025-10-14 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0fd469fb-6fed-35ad-8b18-751c7372fa0f | -7.92445 | -44.12204 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4c52af15-278c-3e07-ac29-8bb5548094a8 | -5.38384 | -43.22467 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c323b97-d41b-34a6-9b39-56f038b9e493 | -4.66582 | -43.12407 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| bf366dfa-62e2-3621-9fc2-df2eaa75eae3 | -4.68872 | -43.12338 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fbcc94b-63c9-3f2f-a71d-82c83bce2a8f | -4.82503 | -43.20627 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0749fae8-d790-3303-8446-912448435e91 | -6.53803 | -41.62465 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 163169eb-a147-3db5-928a-4b9fa236b8f0 | -5.88335 | -42.91409 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a0cee397-512a-3901-b0a2-4e33ca353f0d | -5.25205 | -45.23835 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6913b03-c526-3495-8fec-c9fd2e4641e5 | -4.85007 | -43.20412 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 084d6881-dbde-3e4a-94cc-014676d630f7 | -6.44031 | -41.82126 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8a7f2b50-6777-3468-b0dd-aa6a849d1ba8 | -5.91757 | -42.81827 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c6aa51a9-3c6a-339b-b351-e6c0fa0088c4 | -7.94414 | -44.12325 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 420e4ee3-6576-3247-a29e-f07af044beb3 | -7.14401 | -41.72151 | 2025-10-14 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a8a9dfa-1ece-3fc5-b10d-5a974cb94825 | -7.91695 | -44.12078 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b5e32004-a22c-3955-8b76-3cbd0f758af6 | -5.40168 | -46.02119 | 2025-10-14 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ee06a83-9e3d-3acf-9bc8-03ca4a80a5b3 | -7.94115 | -44.11813 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f07f987e-9ae8-39aa-a892-03d734bdb120 | -3.09738 | -51.29994 | 2025-10-14 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 239490ce-d452-36ed-88d9-dee59d635715 | -4.66213 | -43.12346 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9032cf6a-e178-30ee-a5ed-3c1fd27b7775 | -5.59315 | -42.57888 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15349fb1-ae72-389f-abcd-0d2abf507926 | -6.57012 | -43.92099 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 313edb01-0a59-3302-a5c0-cabd8579ab28 | -5.73887 | -40.77013 | 2025-10-14 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f0c1c032-99c2-38d9-bef7-13b30db81c6c | -7.59823 | -37.80713 | 2025-10-14 04:04:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5679930b-fa7f-3435-8e37-cf302f602180 | -6.85013 | -47.63979 | 2025-10-14 04:04:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 126c5512-d3b0-3196-b0c0-8c4dc58d5382 | -7.94268 | -44.10917 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99865ab8-209b-3e81-bb61-e1395737327b | -8.25322 | -43.39095 | 2025-10-14 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c5c90a33-4495-36e8-9d09-a962c0f4a620 | -3.16137 | -42.8901 | 2025-10-14 04:04:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c83a911a-863e-35e4-9b1c-043b3d1c3974 | -4.62483 | -45.77513 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d55c67dc-bd00-3e8d-81c4-80a2588a53a6 | -7.29369 | -41.96416 | 2025-10-14 04:04:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c0fc87b6-4df6-3e86-a707-c7f77ba7467d | -7.23148 | -45.31841 | 2025-10-14 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9744ae70-90c2-35d7-b8d0-04b9af8b40a7 | -7.93194 | -44.1233 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50273cf2-0eca-3d7a-9a0f-b7e1682b3db0 | -6.45014 | -41.80387 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 875ef0d3-6cad-3776-a3cf-b8a8faea4a00 | -6.44999 | -43.99313 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73ec3422-8e77-3054-99fb-82f54c1a2768 | -5.58425 | -41.10271 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3cc63cc3-b41c-338a-b98e-3cb3a79ed24c | -8.23261 | -43.3369 | 2025-10-14 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6873432b-100a-30f1-95f2-6114a15c39b7 | -7.68196 | -42.37575 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 10960014-dbc7-35e0-835e-f5b2ad775829 | -7.24123 | -46.25835 | 2025-10-14 04:04:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39cd816a-a125-38d2-af1d-0b1842e635b7 | -6.57743 | -39.24906 | 2025-10-14 04:04:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 46ca7a00-4d77-3b6b-b1ec-790b5183bc82 | -5.87012 | -42.8822 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| abd5d4b8-25cc-34dd-a656-6b56558a811e | -7.08583 | -41.95443 | 2025-10-14 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a1b9d015-0092-3fac-bda1-aa0a95eb600e | -6.43495 | -36.88882 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DO SERIDÓ | RIO GRANDE DO NORTE | Brasil | 2412401 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 64a17af8-f359-33c1-a668-db28427773a4 | -7.80965 | -42.44193 | 2025-10-14 04:04:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
