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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0b6792e-b93b-372f-8ac2-df7b51cdd03d | -7.11134 | -50.76377 | 2025-09-11 04:21:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 100c0768-47be-39af-bf3c-325c93e70d44 | -7.5013 | -48.24243 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f554c2f3-7c2b-393a-9b42-9bf13bab18ec | -6.41828 | -44.4898 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 535dd16e-d154-3433-bc5c-e3ced5d756de | -6.6638 | -44.54256 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b315bcde-0bac-39ec-87b7-1bbd95f69e13 | -7.38132 | -50.88985 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c7b7d85-3e7d-3c02-9395-6ca33afb231a | -6.67454 | -44.12669 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 916b0860-cff3-3715-b5e3-f43b698c7150 | -7.20439 | -44.96787 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67e12a3a-a217-3b16-9477-73b6465dfbba | -5.89424 | -45.80658 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a240b1d2-9866-316b-b46c-f42bd8e2df78 | -6.81864 | -44.88507 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 670a9a27-f6dc-39a4-b645-9c5d40550bf0 | -8.65447 | -45.72551 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 726ddeda-4b3f-3e17-9864-ab1ae7c1691a | -8.04222 | -49.04528 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c06ab565-c00a-31ad-85bc-42507e8ae9b9 | -7.84919 | -45.4062 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b481c1d-bb4b-341a-9b49-153d6018af99 | -7.16358 | -48.8941 | 2025-09-11 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38548105-a480-3e7b-b3d7-efa9c519c9e9 | -7.8812 | -46.04691 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89674113-bc56-3199-936a-468d1a72b42e | -5.23073 | -43.69064 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 070cfd64-4b4e-3ec1-b904-f713433fd4be | -6.37043 | -45.15885 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6f5e7254-88d1-310c-ad32-4dbc740a0a87 | -7.73285 | -43.90616 | 2025-09-11 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 142a28d7-f5a6-31be-9e39-1ffbd0f724d9 | -7.38799 | -47.36356 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa92f567-fe74-3ca7-a8dc-1cfb5f80fcb9 | -6.20202 | -43.52347 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c8115a8-af5c-31f7-bff6-17eeb38a417c | -6.24922 | -43.42808 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 81a6df3c-b766-3541-9298-b8634fdd4387 | -6.40181 | -43.49899 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c63171fc-19ae-30db-956a-74fec4ca58b6 | -7.35354 | -44.30245 | 2025-09-11 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1400ccaa-10c5-3453-b739-c4ed2cb45fd5 | -8.04043 | -48.66255 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e4bc17c2-ead9-3aa8-895f-bb6be22decf2 | -5.7578 | -45.43234 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa735548-7d09-34f5-95de-f9c5c0a90f6c | -7.8785 | -46.0209 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28fa90e1-5976-3f2c-ad1e-bf2256f5ccb8 | -6.44958 | -43.57533 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 494e0d87-ba34-375e-b916-4540a703d12c | -7.80942 | -46.07566 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 061bf0dd-98f7-35bb-bd6b-af22a3f22cfe | -6.76721 | -43.46356 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc4384ec-a4b4-36b2-9284-9c5c71ae6e0e | -5.69406 | -45.32468 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70dde706-abaa-3d90-9830-3b9530c1f211 | -6.55653 | -43.97942 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5229f5f2-109d-3795-8e0e-2f2a59275748 | -7.16511 | -48.88479 | 2025-09-11 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af39d76b-fead-32f7-83be-224a6f377ee5 | -7.54661 | -42.52744 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 59c1412a-f2c1-3e08-99d9-d16ec79a991a | -8.02165 | -49.05142 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ba2a892e-a728-3706-b04c-f11034a6bd37 | -5.74136 | -45.6004 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebb76a89-2eaa-34e0-b241-6102d2881718 | -5.45515 | -44.34933 | 2025-09-11 04:21:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 714c8b97-99a7-348f-8082-f8345179ff8a | -6.66047 | -44.54204 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b92b496-2792-39d9-8586-bb11d1a924f9 | -5.76722 | -45.52443 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68bcdc83-86fc-3294-a73b-7cf243159c19 | -8.48487 | -45.6797 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31d61bd1-047b-3629-8a4e-031ef549d723 | -7.37355 | -47.42993 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8379227c-77f2-3d1a-8c7c-dca1c6b42f72 | -6.30985 | -43.41551 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4d5fd20-54d5-32f5-8366-a5a32416006e | -6.6129 | -43.95924 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61f92ad7-ee56-396c-91f4-0ca3fec3f028 | -4.73179 | -43.5304 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 509210a9-a0d2-31d0-995e-53bccf19fe89 | -7.05072 | -41.4176 | 2025-09-11 04:21:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c38c2af2-e13f-3ae8-a1b3-2bb498e048d9 | -6.4541 | -43.59058 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 555de45a-038d-366d-88cf-1c9d15c010ab | -7.03861 | -42.13214 | 2025-09-11 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ccae466c-407b-3d91-a71f-f619a132e0ab | -5.94671 | -42.78585 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 43248da0-371a-3030-9254-1aff1a86402f | -8.20239 | -50.10325 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f475fedc-4cab-316f-885f-b9dfce16c259 | -5.36066 | -45.2256 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18e7e03f-1672-3043-a99b-d255a03df48c | -5.93839 | -45.68176 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 060c18ea-8836-3c26-82e4-42851c95b617 | -7.35593 | -47.42702 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a11eab4-df6a-3ede-8cae-7d92968cb849 | -8.04992 | -49.02291 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0999181-3e3c-3fc9-b6af-797d6cc24c2d | -6.23616 | -46.15665 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72a35f90-c5f7-349e-9c28-e45046a84b1b | -7.87236 | -46.01628 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4274dbde-4458-3403-be09-8b7eb41b4ec5 | -8.51208 | -45.70208 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78e77f6f-e5a5-3d89-8761-53fb0b8d9925 | -3.07977 | -48.81672 | 2025-09-11 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29982bb3-001e-3de6-a2a4-61e0c275ecd4 | -4.9325 | -55.78379 | 2025-09-11 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 816aeb77-a6cd-314c-9e3f-38a9939660ac | -6.55987 | -43.97995 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 52c2f955-692d-3055-b478-247a74e54d6c | -8.66058 | -45.7301 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 681944d9-cb24-3fb9-b30c-4850e72ad07d | -6.81096 | -52.80473 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0352bc8f-178c-3559-ad63-807178f4a7de | -5.96407 | -45.83212 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e621f00f-3f90-3697-9ab6-3b75077ac65c | -7.83587 | -45.40411 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d507cf54-12c3-361d-809b-a8cc4b99ac35 | -7.62201 | -46.54659 | 2025-09-11 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c383e5b-49ad-3a70-bb80-07b206e29fe0 | -5.20107 | -45.72365 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dcc0b8b-2791-3fe2-81cb-13ec77910e38 | -8.02004 | -49.04304 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 250c9ec7-957f-3adb-bc49-3f20b4e9a460 | -8.0155 | -49.02319 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a47d247-e6ac-37c6-bbae-6d3f8359b44e | -7.0132 | -42.13229 | 2025-09-11 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 23a5f0dd-8e8c-3c96-a1ce-b2a31fbd3aa3 | -6.34739 | -43.78091 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 134e0025-e5a0-3616-97e1-131d5bc4bcb6 | -7.23592 | -44.46957 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4de7ef96-2660-31cc-a3c0-91eb0c1e4bc5 | -4.45864 | -55.04734 | 2025-09-11 04:21:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c01b473-35ff-3ef8-ac28-cbb2fd93935b | -5.73577 | -45.59225 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6653d23d-f5e7-3278-ad1b-fb9c7d64c0ac | -5.36535 | -45.96469 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b3a2185-6ff6-3605-97ab-ce60e1a77f55 | -6.28759 | -42.40626 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 518aa61d-ad2a-3261-87eb-cea918c0e741 | -5.93948 | -45.69653 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6057876c-de77-35df-8979-6c7816959adb | -7.78461 | -50.77262 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| de0a0db5-7cd9-32a0-8cb5-6af154e6e085 | -7.46609 | -45.27694 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70ef2593-384e-37c9-ab68-2ab07adcde3a | -7.74552 | -44.75047 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8cdd481-c8f3-3dce-8691-f9acb65264cb | -8.93062 | -46.15008 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2313aeb-afae-3f03-8334-ea62ae735111 | -5.6587 | -43.89698 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96a250c7-0d37-3f6f-a139-f3ea5f19cb01 | -3.79365 | -51.15711 | 2025-09-11 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 763a3452-adb8-3551-be3b-5d686d0056b7 | -7.16837 | -48.04481 | 2025-09-11 04:21:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12401403-1483-315a-9898-10be9cb8e769 | -8.3239 | -44.88474 | 2025-09-11 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 376c8e02-8914-3dcb-9d6d-d5ae64707032 | -8.1664 | -46.07094 | 2025-09-11 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf1b8848-e0f0-346d-bbbd-e0c4b92573d0 | -6.8371 | -45.60053 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef398d3f-4f39-36b7-969e-de21a9c97234 | -6.31941 | -43.44263 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c26a263b-024a-384a-8021-8e1455ca8fb0 | -6.67065 | -44.12969 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92146c76-4d2b-327a-952b-477fc543eccf | -6.63802 | -38.73721 | 2025-09-11 04:21:00 | NPP-375D | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3100337e-9a57-3670-a602-d48c13ace030 | -7.71781 | -44.80279 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 685b504d-d10a-3b9a-99af-4e91d81eadf7 | -5.52347 | -42.68047 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d594ca97-324f-3380-893c-7e0889ffb95e | -6.57905 | -47.34587 | 2025-09-11 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0406192-29d3-360f-8eeb-2d1e69f034e6 | -8.04443 | -49.05529 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 012e4aba-0a0b-3150-892c-9baf5c388499 | -5.39231 | -42.62667 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9a28d9c1-473e-35c4-82df-699820870623 | -5.22684 | -43.69363 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18363f0b-958d-3a57-b2ad-7ca5834308ee | -2.21793 | -48.22697 | 2025-09-11 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddb81142-c56f-3737-a444-dcfd523677b7 | -6.4882 | -44.4935 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bcfa813-1741-3546-aee3-734e513a06a9 | -5.77521 | -43.12868 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e8d7b6b-8273-3142-833d-bf96a78ae95f | -9.09914 | -45.6961 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 401ed8c5-7373-3bd7-8a7a-aeff45dfe787 | -3.14201 | -49.8996 | 2025-09-11 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 911a52c7-1ea7-3cb6-ac47-53c6bfe3a151 | -8.73129 | -47.0958 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0cd2c6ad-9375-301d-9620-6cbaabd9c6d5 | -5.67674 | -43.33033 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f07a219-3e37-39c1-a983-4bd367f0b92d | -5.11181 | -46.24091 | 2025-09-11 04:21:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README50.md)
