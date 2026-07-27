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
| b0d857a2-71b2-3d2a-870d-9d3e80c0a3c9 | -2.74768 | -48.76731 | 2026-07-27 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 742814c3-5906-3a86-b4ff-355d5dfca310 | -2.95246 | -50.33596 | 2026-07-27 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98054605-3f36-3c73-88db-d65a0955eff1 | -10.94501 | -43.06385 | 2026-07-27 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 6878cf9a-128c-3bcf-a0c7-6971530d990c | -7.16983 | -59.3102 | 2026-07-27 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc5b8f54-048a-3cd0-b850-736e081d10b4 | -7.16859 | -59.31721 | 2026-07-27 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2cba5ea-ee2c-3b8b-9f77-026309cad07a | -8.83096 | -47.07278 | 2026-07-27 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edd2cd38-46a8-3f65-8f01-9d09aaccc36f | -8.36595 | -45.38148 | 2026-07-27 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65bce6fb-4277-347a-bcb3-3258cc4ad7ae | -7.16501 | -59.30572 | 2026-07-27 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aac4e20a-18f5-3155-b12f-e8fea7149d82 | -5.48716 | -45.11744 | 2026-07-27 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe0a66ff-91b5-3319-a7de-4fce1ef3e320 | -8.82735 | -47.07222 | 2026-07-27 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 680f2053-b0ea-3476-b7d9-9ebbcf75b1c9 | -2.80989 | -48.67094 | 2026-07-27 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccce0623-ab71-36e4-84cd-22bb81840199 | -3.34605 | -49.22183 | 2026-07-27 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 686f4feb-29a6-31c4-9bd2-e2d4925adfcb | -3.51343 | -48.03477 | 2026-07-27 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c6d7387-8f50-3e25-b6eb-dc8f2d554dff | -2.76829 | -48.57284 | 2026-07-27 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6ec81ee-30e7-3300-824c-d7ebae842cfe | -4.91004 | -43.46856 | 2026-07-27 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0ee2f94-10b5-3cac-bc03-4ad3df8778b3 | -2.76188 | -49.46656 | 2026-07-27 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33ac4d01-fdfc-3406-b680-2ac0ea5b5f1a | -10.93611 | -43.05728 | 2026-07-27 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 128a8741-9818-374b-8260-0082d1a22e03 | -10.93753 | -43.04676 | 2026-07-27 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d8eaae44-b933-3241-8cd0-9475e8cd4053 | -7.16438 | -59.30922 | 2026-07-27 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 992ffed5-d7a7-3d6c-b444-4bd1abaed919 | -7.62688 | -50.03621 | 2026-07-27 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec4fff5e-2ae4-301b-a9d2-f7d7a085ff95 | -10.93201 | -43.05135 | 2026-07-27 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 31cdfa21-922d-3ccc-8fa5-d9fe2d3f61ed | -10.94163 | -43.05267 | 2026-07-27 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b3417a4f-a0d5-3ee7-989c-5a5f178c5dbe | -5.93653 | -43.65197 | 2026-07-27 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d47f91fa-0d8c-3324-95ac-0dba852c2e82 | -4.09804 | -50.42744 | 2026-07-27 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f06e48d-b395-3bee-8958-b2a67e6b55ac | -9.40196 | -48.94192 | 2026-07-27 04:49:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f662a028-cd95-383b-ba4f-61981a57c60e | -5.42387 | -43.42412 | 2026-07-27 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dace5b92-cc29-3ae8-aa29-4bc17942b8c7 | -7.16921 | -59.31372 | 2026-07-27 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab32ff10-aefb-3ae1-a243-2298416e8ade | -3.21599 | -53.13531 | 2026-07-27 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6795c2c6-be21-38dc-a016-fbdb37671113 | -8.07277 | -45.58274 | 2026-07-27 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d900e21-a3af-39c1-aba1-c2530bf0826f | -7.17403 | -59.31823 | 2026-07-27 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c494f0e-3247-3a1b-b4cd-59015ca1e9d3 | -6.92894 | -42.81893 | 2026-07-27 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5ed59d49-aae3-399d-8ef1-dbdf3a9ce5c1 | -10.32591 | -46.73475 | 2026-07-27 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72d8f7a1-aa8a-3369-ba65-07986a052c43 | -4.9143 | -43.46921 | 2026-07-27 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec958779-9dd5-3847-8034-ce45148e9491 | -10.93682 | -43.05201 | 2026-07-27 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| e923c972-d90f-3352-b527-39d22cd70146 | -7.89857 | -48.05079 | 2026-07-27 04:49:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9f05d4e-0c6c-39df-920e-648fbc8a5f8b | -2.95022 | -50.32822 | 2026-07-27 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7853c8c-8f42-3e5f-8efc-585793d5d556 | -9.63417 | -45.5159 | 2026-07-27 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dc64214e-a406-356b-b603-1386ab101b39 | -5.35989 | -43.13565 | 2026-07-27 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0463a65-648b-3fbc-97c1-ad26e8b3daee | -2.9536 | -50.32876 | 2026-07-27 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9d5fd3a-09ae-3970-ba20-f484f4077cef | -8.82909 | -47.08527 | 2026-07-27 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f604fa27-61e1-3ae0-95f7-62790f22808c | -3.91804 | -47.82228 | 2026-07-27 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55a54067-58ac-3f5c-a83a-9fe815705b34 | -8.82549 | -47.08469 | 2026-07-27 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f1b868c-f746-3583-9ad2-ff019d1b4e9c | -10.9397 | -43.0593 | 2026-07-27 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 239.1 |
| 0fe5eb69-bcca-3d1c-985c-88d7c394132b | -10.9401 | -43.0355 | 2026-07-27 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 6ce2452a-7148-3461-8c6f-407c5901360c | -10.9588 | -43.0565 | 2026-07-27 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 5b7bfb1a-db27-36fa-a0c4-b5c53ea3ffd9 | -14.35289 | -54.93469 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 941a30fd-2fbd-3b45-a86e-17e39db8b2fe | -14.35684 | -54.91143 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eacc5dd8-3305-34bf-bb70-20ec2e9bd939 | -16.9619 | -51.88565 | 2026-07-27 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 148b3589-ec03-3f6c-a4ba-6bf47e414fe9 | -14.34484 | -54.93765 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea1b36cd-0098-325a-8d61-f3189001fb89 | -12.31313 | -50.35899 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5078da6-92b3-3667-b5a0-f5801f465be6 | -14.36049 | -54.91212 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 927c2aef-87a5-38b4-a724-8566fc6a40fc | -14.23331 | -54.56345 | 2026-07-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 009926cb-3efb-3eed-a61f-4136a5dee0d0 | -16.96522 | -51.88622 | 2026-07-27 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 67ab0d10-ad39-3033-ac6a-bf79a17c9f5d | -17.16714 | -46.83332 | 2026-07-27 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 579c573a-29f9-3118-abd4-f7e9425efdaa | -11.75091 | -46.45475 | 2026-07-27 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e7c4b22-ee39-3dd8-ae34-790a18913a36 | -12.30092 | -50.37159 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba7db3d1-768e-3c64-bcc9-0ec59e2ec35e | -14.36413 | -54.9128 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 24b22740-3031-305b-ac00-42345dd2180c | -14.35607 | -54.9158 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e9f9d18-d486-3784-b6e4-293373c17843 | -14.24192 | -54.55648 | 2026-07-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43887f63-da36-3fa5-a1ff-6a2815dd9629 | -14.38643 | -58.87571 | 2026-07-27 04:51:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e076bf62-fb3a-3b20-adf2-3f30ea293175 | -14.35663 | -54.91274 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| fc920f5b-dd44-3c74-b055-d4530ede4932 | -14.23761 | -54.55998 | 2026-07-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 788fae40-83b4-3af6-81b4-c9624fc583ae | -13.69287 | -51.91507 | 2026-07-27 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 292bc95b-9031-3165-b7b9-99462d5f9efa | -13.69127 | -51.90378 | 2026-07-27 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cde0d4a-7e0c-397c-9ffc-6bd007a0fee4 | -17.13584 | -47.22137 | 2026-07-27 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcb31984-c64f-350a-a814-eed55eda8668 | -14.35953 | -54.91783 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0eb9eebb-0499-3d12-9d32-77a378de6abe | -13.634 | -44.44214 | 2026-07-27 04:51:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e7f9099-f8cf-366f-b748-926409a0b5e5 | -12.32369 | -50.37891 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c594350-0c57-326a-9fe7-79777c5df74f | -12.31554 | -46.38675 | 2026-07-27 04:51:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6d45db8-2f99-3398-be1d-6d69e3260dbf | -14.23403 | -54.55924 | 2026-07-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e0907a1-7eda-363e-85bb-33057555ece1 | -12.2948 | -50.36696 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 350ed366-19c3-3816-a09c-f318aa8c21a4 | -13.7632 | -47.14114 | 2026-07-27 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28e83f1f-d0ad-392f-8676-c222d0a49281 | -14.49116 | -49.15469 | 2026-07-27 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbdd0086-82f8-3927-acec-d768c4dfa6f4 | -10.54154 | -48.60921 | 2026-07-27 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cb9d8ab7-b30c-3213-89c2-771c59214e7b | -17.16256 | -46.83652 | 2026-07-27 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0783aa21-1ff9-33fc-804a-34528b2add0d | -14.50899 | -48.93785 | 2026-07-27 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d35ca237-e276-324a-9bd1-79c03f4202d3 | -11.26925 | -47.69211 | 2026-07-27 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c065fd3-18f9-33c0-9485-efe382776bf6 | -14.36336 | -54.91719 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| be0df4b9-3d93-38b4-815c-1622982860c7 | -14.34924 | -54.93398 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 919e8a60-a843-3828-b769-e86cb3dd6277 | -14.35971 | -54.9165 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b80fdcda-4d59-3fbb-98e5-cc6d532af41b | -10.90889 | -56.36381 | 2026-07-27 04:51:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88071d4d-3930-34c6-92c7-16c2fd9f3992 | -11.5045 | -50.18586 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6882c68a-ccac-370f-bc0a-dc28b825bf98 | -11.88715 | -43.83096 | 2026-07-27 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c1d038b-f67b-38e0-8a53-e5d71caadfd8 | -13.68795 | -51.90319 | 2026-07-27 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2344abc-53cd-3a9c-acd3-aeafc85802fb | -15.96321 | -52.20886 | 2026-07-27 04:51:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6753dec-98b7-3e00-a055-62f59a318bd6 | -11.46855 | -47.5493 | 2026-07-27 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3ba878a-97b8-35c2-9af3-d454acd73c9a | -11.4643 | -47.55297 | 2026-07-27 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d872f0bf-3004-3d41-bff1-b8ac46e43255 | -13.69012 | -51.91092 | 2026-07-27 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c0548fa-08ce-3230-aa6b-b44fe684a6de | -14.35298 | -54.93333 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cf5a595-261b-3861-ac4b-6e13ec22e034 | -12.31947 | -46.38726 | 2026-07-27 04:51:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08e6b04f-0b5e-3edf-be90-1f977ccf08a8 | -17.16663 | -46.83714 | 2026-07-27 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eb2c219-9ca9-32c9-bc7e-61c80179600d | -11.48303 | -47.55183 | 2026-07-27 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92985e93-481a-3633-8c9f-a4a8fe23062e | -11.48665 | -47.55247 | 2026-07-27 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8435f65-163e-3dad-876d-584f5a5d5d2d | -13.69069 | -51.90735 | 2026-07-27 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d3cb920-98d8-3f2b-b9c9-94945a0b2783 | -14.36102 | -54.90907 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79deb4d7-fa6b-3255-8234-fe1dd5329ab1 | -11.99283 | -45.56445 | 2026-07-27 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28717659-70a5-3d41-ac61-e6a787cdc938 | -13.69344 | -51.9115 | 2026-07-27 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 15e56eb8-70b5-37dc-8822-4fada0d67ec1 | -11.44558 | -47.52855 | 2026-07-27 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afe1caef-dd43-32df-a3a9-937a9abfab12 | -12.32928 | -47.17179 | 2026-07-27 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da75e634-7ddc-3c58-88d6-c482adb6f617 | -12.32424 | -50.37536 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
