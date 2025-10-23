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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 208930b9-df9b-3440-a876-07172e839b47 | -14.87397 | -57.26664 | 2025-10-23 04:38:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63c04970-72e0-3b91-bd5f-faf285864b8a | -16.07865 | -51.41241 | 2025-10-23 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42ca2919-af9d-3e1e-b4a9-842dd7637774 | -10.63428 | -42.30072 | 2025-10-23 04:38:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a884025-2390-33c7-bc75-cc908d78be6e | -13.48476 | -48.78523 | 2025-10-23 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5776c5fd-3a5a-3e56-83c5-41d2bf5b18af | -13.62438 | -49.45162 | 2025-10-23 04:38:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 428a1ad1-fa61-3006-aa35-3074f9fcc2ce | -12.12712 | -62.96561 | 2025-10-23 04:38:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c934b147-666e-354b-a8d9-9f5308dfa0f0 | -12.70235 | -48.83621 | 2025-10-23 04:38:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69f94357-b85c-3aab-82bf-69ce0b839ca1 | -13.37376 | -46.64007 | 2025-10-23 04:38:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 591c65c9-abfe-3fef-9810-a843cf30eb64 | -10.25052 | -47.99567 | 2025-10-23 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc039259-f419-304d-9abb-d2e3cbfcc092 | -12.41604 | -54.36567 | 2025-10-23 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e89013a-4eb9-3550-95e5-a8b478593fde | -16.08376 | -51.40905 | 2025-10-23 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa073214-97f5-3494-8685-43ed94adcab2 | -11.69371 | -43.93454 | 2025-10-23 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93b6a1be-7581-3ddd-a8ce-8428b51661fa | -11.99779 | -46.77744 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd5a1bb3-745f-3780-ad02-bfbf80f692ad | -12.28881 | -47.45701 | 2025-10-23 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb8e5aca-1f35-3303-8b74-79088942e50f | -13.37006 | -47.91302 | 2025-10-23 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caad60f0-be2c-3532-ae93-756945665115 | -9.68084 | -47.64037 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40ac2bdc-3e67-3014-8a2c-b5d61d8c626b | -12.01305 | -46.74738 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eef279dd-ae65-3fad-b674-179879f2de29 | -13.94056 | -49.63424 | 2025-10-23 04:38:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bdfd7b2-e89c-3460-bc89-fc2fd98cfff0 | -13.80148 | -54.82231 | 2025-10-23 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69927692-b93b-3108-8040-9a56700a74e3 | -9.99602 | -49.14392 | 2025-10-23 04:38:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0aeccec0-ef77-3501-b037-2c77b782ce1e | -12.67871 | -48.62398 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3c0ec66-26db-3f9b-b0d2-4cb69753c11c | -12.69321 | -48.6409 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7206561-80bf-39b4-80c1-f97b66307587 | -11.25001 | -49.86705 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82be0187-78fa-3f7e-b0dd-08a2498b7f07 | -13.89628 | -48.37223 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa51ce65-493c-3857-8cc6-160178c7bb53 | -15.13391 | -47.92886 | 2025-10-23 04:38:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 48d6ef65-88e1-336f-a0fa-9705b11696c6 | -12.66869 | -48.62234 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15ab90fb-e83e-34ff-a533-7338993a2cd0 | -11.35809 | -44.88773 | 2025-10-23 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c559b434-c31b-36f8-9563-cd6a10fdc206 | -11.35951 | -49.79715 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2c5f81d1-8c42-3b6c-9a7c-af572f55d943 | -16.15322 | -50.82389 | 2025-10-23 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cb46cad-b633-3e4f-8351-706f1f0f96b6 | -13.90754 | -48.36636 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 702a5d71-c5b7-3b05-9787-f3a1103012cc | -12.67595 | -48.64178 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a94a5d03-9872-347f-a950-a4c652835a6b | -16.07979 | -51.4121 | 2025-10-23 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 875ddf92-6e4c-38fd-901c-57a03dc4ce19 | -14.84401 | -54.22626 | 2025-10-23 04:38:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b285ac94-fcd7-3310-b979-0f131694da5e | -13.59737 | -43.47738 | 2025-10-23 04:38:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ce5a08b-50eb-3285-bfb4-cf3d35a8552b | -11.27269 | -49.79034 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e3e75e8-3033-35eb-9a1b-0dbbedf1bbf4 | -13.89685 | -48.3685 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fca41754-515d-37d7-be1f-ae96fa581cb4 | -11.36065 | -49.79004 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 376b9d47-944a-3e95-9de8-0a9ec6b43996 | -13.58729 | -48.58817 | 2025-10-23 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a161a012-2d6f-34f2-b2ad-6046bbfe4d79 | -13.58786 | -48.58451 | 2025-10-23 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 36f860a0-8d94-3ff9-834f-a702f7278356 | -15.36218 | -50.56063 | 2025-10-23 04:38:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adce8422-d702-3b81-b47d-66f14c9f8b98 | -10.6121 | -45.18414 | 2025-10-23 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97f565f8-2949-321a-8775-195fb3345cc3 | -12.00011 | -46.78582 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0f85c630-3787-39eb-86e3-4b22fa8a0a37 | -13.1252 | -48.24336 | 2025-10-23 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1202c9fe-50ec-3ea0-85aa-e17eab7e9aa2 | -11.80068 | -49.41157 | 2025-10-23 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a053292-1c0a-350b-9dcc-74085e509e34 | -12.67984 | -48.63876 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2b3ed57-c649-3643-9058-989f8e2669a4 | -12.78395 | -48.57509 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 208c2132-7056-3158-ac3b-a18569479ba2 | -15.67381 | -53.35002 | 2025-10-23 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ec911e0-21ab-3fdf-a7d0-cc170245588d | -12.53646 | -49.82974 | 2025-10-23 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbb8bd2e-ece0-35df-8b39-90cd1c165f3e | -13.79558 | -52.77209 | 2025-10-23 04:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 622effa1-4c0f-323b-b0b3-1c11a5d8fdd2 | -14.84488 | -54.22144 | 2025-10-23 04:38:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54070a66-b0b4-3122-9674-19b7c3b62040 | -13.37019 | -46.63953 | 2025-10-23 04:38:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15a872e4-d0e2-3738-b392-8af847f23c54 | -11.3546 | -49.79291 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5ce19f6b-3fb4-3833-9326-d1d9329ac23e | -12.31529 | -47.83691 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a707cd4-34a7-3d38-abec-d3fb34a3d817 | -13.89572 | -48.37591 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62f6edff-6aa3-3b75-ba2b-abb6eb6f4d2a | -11.85854 | -49.85711 | 2025-10-23 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bd1b574-defd-3d3e-b1d3-7c51f02c6a96 | -15.51791 | -45.96483 | 2025-10-23 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae93e83-3c76-3de3-a69c-3a933c13b1c1 | -12.13405 | -62.96716 | 2025-10-23 04:38:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9630d7f-cbb7-3665-afb0-658a08e99ed7 | -11.00217 | -47.79878 | 2025-10-23 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1be4ada4-a62a-33f1-9675-a19cd9ac89bf | -10.61276 | -45.17963 | 2025-10-23 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4b5a737-3a57-36d1-97ea-6c6f20de9f10 | -9.92807 | -47.46139 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 292a20e4-94e9-37d0-ac47-473b5f44ab6b | -13.37567 | -47.26606 | 2025-10-23 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 4532c224-389a-31a5-a87d-928c9e6a4c57 | -12.78785 | -48.57205 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d2cc20db-33e9-3643-ad34-4a637472e1b8 | -12.37531 | -63.87684 | 2025-10-23 04:38:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8ca0620-5f2c-35f3-87c9-480c4c7ef4b2 | -14.87457 | -59.6351 | 2025-10-23 04:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab47f730-ae9c-3039-8656-2c5e286cd6c2 | -13.01189 | -48.45605 | 2025-10-23 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34c1d8da-437a-31de-872f-a0d6710f728c | -12.09585 | -63.62297 | 2025-10-23 04:38:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a99cd438-9514-388a-b0dc-6e17228d87e9 | -11.80479 | -45.18279 | 2025-10-23 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 898c46e1-e040-3960-8cd8-626a514f1e25 | -16.47635 | -46.475 | 2025-10-23 04:38:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 090b2b57-9611-3957-bbd2-0832a13ae34a | -12.69989 | -48.83918 | 2025-10-23 04:38:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf40867a-61f4-3974-95cb-f709d2fc6290 | -14.84104 | -54.22071 | 2025-10-23 04:38:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0e2b862-3017-3656-98fe-d2f637f5758e | -11.99487 | -46.77296 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebc2d3e8-6fb3-39bd-a6c1-b4a5c9e8cc22 | -12.15915 | -48.05596 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efecde5f-cfd6-3106-9157-18a347ebea37 | -11.33099 | -55.06147 | 2025-10-23 04:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a78846e9-13a8-3246-babf-5e4ed976e373 | -11.33173 | -55.05742 | 2025-10-23 04:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95402339-2241-346e-bdb7-a0dd04deaeba | -14.83544 | -48.3148 | 2025-10-23 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c34bb364-0046-3973-876e-1af3cb5cc317 | -10.02777 | -47.06162 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b708091-fbbe-3573-a4b8-4dbdb2182e9d | -12.69265 | -48.64447 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a59363d-262c-3363-9819-0fdfab0ef2fd | -11.35403 | -49.79647 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0210122b-d01a-387e-b71b-86879b21f705 | -12.78729 | -48.57564 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9ac0c55-1efe-37a9-8a59-80fb062a0709 | -12.91187 | -47.73918 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ebeefda-bd77-36a3-8145-6dc9de2e2d45 | -12.69655 | -48.64144 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be3829c0-0aa1-3234-8598-aa3e54a9f9ee | -12.24136 | -46.785 | 2025-10-23 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a912032-a72f-321c-b6ce-78d99c062691 | -15.88852 | -48.16982 | 2025-10-23 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0a70b24-4c81-318d-a3bb-306c2e6f4800 | -14.20967 | -44.51965 | 2025-10-23 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a482c2f4-635f-3a85-98aa-6cda50295b88 | -14.30249 | -49.95333 | 2025-10-23 04:38:00 | NPP-375D | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 364996d4-909a-3f3a-97ee-b5422c06af5f | -12.02125 | -46.74051 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3670363c-7bf8-3e69-8a33-d4f51c9fb30f | -10.63428 | -42.30071 | 2025-10-23 04:38:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f697ce7c-00c6-35d0-909a-cd8c9a47dbe2 | -9.18148 | -49.71023 | 2025-10-23 04:38:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c642d60-0b82-3c0f-b0b6-73752cb54d73 | -13.2983 | -46.56675 | 2025-10-23 04:38:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6c21f8d-f59d-392a-a058-fe0ddd0bb7a2 | -16.49654 | -49.74203 | 2025-10-23 04:38:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18d9d1be-11dc-3096-8558-e60e6587c2cc | -10.53631 | -47.98999 | 2025-10-23 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06550584-4386-36d2-a215-3f4f7673c7b7 | -13.03808 | -47.22976 | 2025-10-23 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 656584e6-b65f-3add-bfc2-0696ff6ee450 | -13.0433 | -47.21871 | 2025-10-23 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75e08575-9a88-32da-b874-b245522f5864 | -13.46085 | -48.82914 | 2025-10-23 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b642861-542e-3c9f-bcdb-2ddc087f8530 | -14.70416 | -48.33209 | 2025-10-23 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9acb6856-9b1d-3ab4-aeff-0eecccea0130 | -13.8963 | -48.3494 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 084bf56c-0227-3dd9-b807-d9a4df422850 | -12.24622 | -49.58973 | 2025-10-23 04:38:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| feb599cd-f3d3-34ef-bac0-3686c4c42f23 | -13.37511 | -47.26982 | 2025-10-23 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 0c54c2a5-0ba4-3b54-a192-37c658c32217 | -10.61276 | -45.17964 | 2025-10-23 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e208f4d-524f-3179-8368-457706eece3d | -9.97378 | -47.07219 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README25.md)
