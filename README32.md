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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aefb8195-a414-3309-96ed-44f3884f14ed | -6.67191 | -43.76373 | 2025-08-16 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed9cbbf5-c425-355b-9c34-99a1ccb6e883 | -6.56725 | -43.03607 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa7d4f10-ffd4-3706-8394-7d5fc94681d1 | -11.25625 | -50.47615 | 2025-08-16 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e488817d-4fe4-3063-864f-1fd0706ed358 | -13.6072 | -46.92139 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61c2c66d-b260-3cf5-b1a9-eab805c6feb6 | -10.35389 | -49.92644 | 2025-08-16 04:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a33901c-26d0-38d5-8e8e-0124f602ea65 | -13.58703 | -46.97123 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b1bc3b8-7855-38e6-8172-063d5deb6d3b | -11.18317 | -43.66074 | 2025-08-16 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62d9f3f6-28ec-3936-8bfa-e062d210c85f | -12.60538 | -46.91671 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| af086b4c-64ed-3ff5-ad2d-529426279d26 | -12.57051 | -46.95968 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fb213f40-e34a-3261-ab73-843921de1764 | -12.56587 | -46.96377 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1d0183c9-a547-31cb-aefe-d25ac46e5fb5 | -12.58911 | -46.94287 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5ff042a-996a-3042-b8d2-01a1f6382f4d | -12.5988 | -46.95496 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc93dd06-5e15-3ee1-9fa9-a71dc4f991c2 | -9.70368 | -46.26375 | 2025-08-16 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 317b15f3-c083-360f-8163-24d13dab496a | -6.9228 | -44.16733 | 2025-08-16 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7db87a77-5f58-356d-a74f-befcfe9e0c3d | -8.19326 | -45.01751 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ea38324-d605-3f2a-99fc-793175e3efcf | -7.09462 | -44.43717 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf508c75-cdc2-37d9-90cb-bcec11b9d274 | -12.80021 | -45.96851 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f6b4d53-f1d5-3237-ae27-f0d978d5a353 | -7.14684 | -44.3875 | 2025-08-16 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ab66db6-b933-3d36-8a61-1ef32901eb96 | -6.55727 | -43.03104 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 39f201cc-d928-332b-bc4d-d04a7c8a6afa | -9.80797 | -49.22101 | 2025-08-16 04:10:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18874fbb-0d65-368a-b900-3f5d570e7346 | -11.9175 | -43.43491 | 2025-08-16 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5baeabf9-b967-38b6-a7aa-44fbb378b668 | -9.85256 | -47.81274 | 2025-08-16 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff4b3709-1f28-3568-bb59-71d4467cd9e7 | -12.82885 | -46.00229 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1886e4dc-ad1a-3aa5-b92e-80fe024ffc44 | -11.41635 | -44.69074 | 2025-08-16 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0bae6556-c885-3af3-b9dd-20abd7717f95 | -12.59375 | -46.93875 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ccc2a2b3-893d-3178-9a13-1aaad595eb18 | -12.36031 | -44.43784 | 2025-08-16 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 924170f0-15b0-372d-96de-a50b89de2389 | -11.36144 | -55.42149 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 696825e9-d801-3f9a-854c-030d5170eb41 | -12.84259 | -46.05258 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc21a505-987e-3737-856d-c68402389525 | -10.24088 | -48.30729 | 2025-08-16 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dbf51668-f457-3c6c-935a-12c84eeeff26 | -12.61648 | -46.94336 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e8a64701-314e-3419-8ddb-7c815d5e5df0 | -12.59207 | -46.94848 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe0b2f8c-e0f9-3699-950b-84c1cd241bf5 | -12.59691 | -46.92041 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5d1feb3a-a032-367e-886b-7d712e6339c1 | -8.74472 | -44.04351 | 2025-08-16 04:10:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9530f62-ab1e-30d5-896c-f04a026767dd | -12.83681 | -46.04281 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 689be765-c992-378c-92a6-8fa8a9c81339 | -12.58993 | -46.93811 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5044562c-b930-3d23-9900-935e2a163514 | -7.55149 | -45.42231 | 2025-08-16 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a98ba1d8-9b1c-38d2-866c-66c36ac0f5a0 | -12.44964 | -47.01006 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa1808bc-3ccc-37de-84c7-e81bbf13f778 | -9.70211 | -46.27314 | 2025-08-16 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37100b7f-d666-3850-a86f-0b21cd548b56 | -13.61676 | -46.9104 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4964a908-640b-3b69-aa8c-354aed191ede | -8.19475 | -45.03081 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5bedf8b-7a49-399a-b805-fa3c443d395a | -12.5929 | -46.94368 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f7efb57-a3e6-355a-bef7-b8bd4aae4c9d | -9.70593 | -46.27378 | 2025-08-16 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b9a70c2-e163-31aa-8abe-cfba51a23fa2 | -11.89966 | -43.43927 | 2025-08-16 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dffa1649-3fe1-3c25-89aa-5537cff4bf4e | -8.11273 | -42.35408 | 2025-08-16 04:10:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f5a037f-a254-3f7b-be9c-3ffcb1917cca | -8.1739 | -45.02014 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dd222da-735e-3a12-9303-bb7ee69cb100 | -8.19689 | -45.0181 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3143782-9ac3-3d81-a493-0c70bea457c3 | -12.83969 | -46.04771 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7f0d77b-0abe-35d7-826b-e5c11bf26b44 | -6.55445 | -43.02684 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acc04934-9030-39f3-9341-5103ae395da9 | -12.79952 | -45.97265 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c2f9711-b89d-3cea-93cd-0a6b0bed9b11 | -11.34417 | -55.42432 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17b87488-fe57-3637-8b94-9a208bbf2c96 | -13.33255 | -45.22113 | 2025-08-16 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc4cf7ec-8483-3bab-aa22-3b2535b5a088 | -12.80867 | -45.98999 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c5a4da0-3e63-38dc-8824-f6c13d43bdd6 | -12.56503 | -46.96858 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ef26d3b1-c39b-3656-aaf0-082235b38585 | -7.42222 | -44.91462 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcf436ef-deb9-3d01-ad66-8666d2b76b50 | -9.17597 | -45.32663 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82a0d6f1-a087-37db-b1e1-07980f41f278 | -6.54706 | -43.0294 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dfb68d7-0775-3f76-b746-4237fa877fb4 | -12.58531 | -46.94219 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19d7af72-bb1f-3fb1-8e88-8d85b9512f6d | -12.64457 | -44.4958 | 2025-08-16 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cba6d02-b1d8-3b24-adbd-6852dde93062 | -12.83898 | -46.05192 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a7eb6de1-92d0-312d-a7fe-117352356273 | -12.56293 | -46.95807 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8adaeeb1-7a46-3042-a593-df22d6b3e409 | -12.54215 | -46.96458 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| e6ca450d-e80d-3197-a8c9-8d917e8f6ad2 | -6.5527 | -43.03779 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30292854-f601-35f3-916d-c60efc79dc88 | -12.82382 | -46.00999 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ace0aab8-cc42-3c5c-a716-a42cec157a42 | -12.82093 | -46.02688 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bb717e2-61c7-30f0-ae82-e4aaa37ac885 | -16.23129 | -51.12662 | 2025-08-16 04:12:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3feef58c-3160-3d2c-b9de-108c8fe522e1 | -14.93999 | -54.70547 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fc6357f0-2aba-38da-a181-16c938d28764 | -16.47593 | -51.97845 | 2025-08-16 04:12:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e577c33-a237-370c-bbe2-ae05a87eb799 | -17.60821 | -46.67895 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3a880384-1c93-337b-9f75-01494e584f5d | -18.12045 | -44.99482 | 2025-08-16 04:12:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5898f4d-b40a-38ae-97cb-ad66499bf671 | -14.95293 | -54.73285 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fda6c9c6-4a00-33ee-8623-fc6cc4073a4d | -19.95376 | -44.14342 | 2025-08-16 04:12:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 27709fec-c13e-37e8-950c-756da18038d2 | -15.9008 | -48.31854 | 2025-08-16 04:12:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79c16456-7edd-39fb-9b78-70704317d248 | -14.04682 | -46.29368 | 2025-08-16 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecf1082a-84f9-3124-9bb5-c958e9cb9a30 | -14.97445 | -54.7199 | 2025-08-16 04:12:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35383325-24db-3cc8-a350-55bcddcf7874 | -18.22799 | -42.70184 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d4185a02-376b-3f3e-8f70-0c5932e3acd1 | -13.9952 | -49.64338 | 2025-08-16 04:12:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9d9c806-3219-3a63-a8cc-aae8383c5100 | -14.58015 | -47.9076 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76caba67-0687-3e8f-b700-cefe894f7ca8 | -13.43664 | -56.67961 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f774fd25-e2ad-39b9-80be-5fa798f2ba9a | -14.95914 | -54.7331 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 41668143-c96a-3d8b-b8b2-2b1002b1446f | -16.22663 | -51.12571 | 2025-08-16 04:12:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7b2f113-df74-3f89-badd-e449608b28e9 | -13.45076 | -56.67477 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39634a60-70db-363f-9ad1-ae91dbff9ab3 | -14.94753 | -54.75447 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c32cf17-f8c9-3a4e-9545-90f8150a8d24 | -14.93501 | -54.69949 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 78b1ad4a-9e0b-3d05-97b8-522eeb4ce53a | -19.64512 | -46.09755 | 2025-08-16 04:12:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f5c279e-e30a-3d33-b2ff-61f26ac556a6 | -14.94631 | -54.72994 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 82f06247-0b53-3c83-baaa-56cd31df86b9 | -17.37938 | -48.1604 | 2025-08-16 04:12:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c993c3e1-ebe4-3d2c-a16d-f690ee859ed6 | -20.05041 | -44.63269 | 2025-08-16 04:12:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b64b7d6-c506-370b-8e3f-851e21247452 | -13.43409 | -56.68501 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2095ee41-c4c1-3c02-b9b6-0dc8ebed2578 | -18.51697 | -50.74883 | 2025-08-16 04:12:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f15511dd-6dc3-3002-95f2-ea57bb2e6344 | -17.80751 | -50.85955 | 2025-08-16 04:12:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b756131d-0953-3ebf-a329-815432d6b5b0 | -14.93986 | -54.73537 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6b2f8b92-5d27-36fa-8b9a-c907ad7903aa | -14.93291 | -54.70929 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d2a53117-9820-3084-bfd2-a0a0d9e752b9 | -15.62681 | -49.26801 | 2025-08-16 04:12:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f6ef96a-db76-3da1-afd4-d44474c1b73f | -14.48076 | -47.72236 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b867744f-4324-3b33-b578-22996f1adab8 | -14.95237 | -54.73091 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ebdf1ccc-8a17-3807-84ec-e64a7e062daa | -19.29686 | -46.21442 | 2025-08-16 04:12:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aadbdb53-ffc6-3bc4-a3de-8ab6bbad77b0 | -14.97261 | -54.7286 | 2025-08-16 04:12:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b9a79b33-0e0b-332b-af10-109a77e1fc81 | -14.58523 | -47.92445 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3788d6a-6e51-3d7b-af03-8aad067e7192 | -14.58916 | -47.92507 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 197e840b-88c6-3ec4-86ee-5e1c7c768c12 | -14.58313 | -47.91354 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README33.md)
