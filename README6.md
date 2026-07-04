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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79b9223a-2f5f-3b21-98fd-127732fd6296 | -5.32228 | -43.56739 | 2026-07-04 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6f599d5c-ba4d-3e05-84fc-58367a4857c2 | -9.43623 | -40.32232 | 2026-07-04 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5177e76-cafe-3ae3-9afb-8070e10acdb6 | -6.90216 | -43.72181 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91074714-1a49-3654-bf04-3f3784dfefed | -6.89599 | -43.72073 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83af5947-1f31-30f4-9f21-d6a1a72cea14 | -7.00753 | -42.77789 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b8cc84a-3189-3449-bfcc-d79da639514f | -7.00287 | -42.77463 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c60ac8bc-21c9-327c-826d-20ce883ddeb5 | -10.2397 | -37.43527 | 2026-07-04 03:40:00 | NPP-375D | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f06d8d71-60ca-3bdc-8d86-be37a94f8c65 | -6.86087 | -38.35151 | 2026-07-04 03:40:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 329ae70b-89b5-3aba-b576-16a231a30195 | -9.43713 | -40.3173 | 2026-07-04 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b41a856d-b5af-3584-8c98-e79d2a82e2b1 | -7.00719 | -42.78398 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a2b0dd9-a238-3ae4-87df-97d5205e1068 | -9.44387 | -40.3341 | 2026-07-04 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 0fe28f10-aac5-3a44-a912-8a0892bd8f8d | -7.00601 | -42.78616 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec2f01b1-b9b7-3762-b612-e2fb468d9ba4 | -6.90303 | -43.71704 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 75c2ab6b-1148-3a8f-8124-2e4f6d2fe694 | -6.93256 | -43.7248 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4d2d0a3-b554-3632-aa7c-69850a64ede7 | -7.00327 | -42.76859 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5bde21d3-4000-3695-bf40-be210264e406 | -7.00646 | -42.7881 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 44ec43ff-0a28-33ad-82ea-937a910eea98 | -8.033 | -46.243 | 2026-07-04 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9e0f5573-1bdb-3c29-83a7-321967463822 | -5.31513 | -43.5713 | 2026-07-04 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f2d1e3ac-db31-359e-9d9e-ae124ee7508e | -8.08398 | -46.70675 | 2026-07-04 03:40:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c7de6a8-defd-3443-bbb6-33c4f0c4fdd6 | -6.85656 | -38.35075 | 2026-07-04 03:40:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b5a3287-edc5-3a36-b35f-c48a24e5fa25 | -6.93434 | -43.71534 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 130b8546-f7c1-3f46-9026-463f46f73d0e | -6.93375 | -43.72289 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78bb1c6b-e6f2-3322-b93d-80e2b0f9a3b2 | -5.59813 | -39.54234 | 2026-07-04 03:40:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c0952cc9-651d-37ed-953d-051ea235e8e8 | -5.15061 | -37.91034 | 2026-07-04 03:40:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e7e9b3d3-de27-3927-a09d-3cadef78c12b | -5.31696 | -43.56101 | 2026-07-04 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5b5f7321-cfc4-3594-a4be-3169bd6dbac0 | -7.72918 | -44.17559 | 2026-07-04 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb792702-b476-3301-b5db-58046c21e372 | -5.43279 | -44.65653 | 2026-07-04 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4fe266e-d7a2-3b41-bab1-53a353426776 | -5.14855 | -37.91122 | 2026-07-04 03:40:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f2e3d1e4-8a69-325b-b3bf-2b6fedca02f0 | -6.42953 | -43.72463 | 2026-07-04 03:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d2b22ba-5fc0-3fdb-9f22-e21b71c6274f | -5.51987 | -37.62235 | 2026-07-04 03:40:00 | NPP-375D | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9b6fb2d0-89f3-34e0-92df-070c992f1cb3 | -5.31605 | -43.5661 | 2026-07-04 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aced179d-cf02-3c72-8052-0c54555c3c31 | -6.93346 | -43.72004 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc12bb1a-72cf-3bd1-85db-eb2ce382bf34 | -7.82383 | -36.26873 | 2026-07-04 03:40:00 | NPP-375D | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e6b1ea96-3860-3292-a656-30ab8ee967cf | -5.42273 | -45.29708 | 2026-07-04 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f68bfac-dee9-36eb-b8ae-9e78b2a9babd | -5.1456 | -37.91369 | 2026-07-04 03:40:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 72074cb5-632c-3a68-8ce9-af43974909b8 | -9.44005 | -40.32821 | 2026-07-04 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| d5093152-c567-34e3-88cd-ae835b0bed5e | -5.14991 | -37.91441 | 2026-07-04 03:40:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 747e381d-9142-3323-8a13-ccdb0c03460d | -6.92821 | -43.71412 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3aba850-9fe1-3ce9-b254-e540c99f3999 | -9.44477 | -40.32907 | 2026-07-04 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 564ff378-61d9-37b8-b094-1a263f3f3b8e | -7.73011 | -44.17069 | 2026-07-04 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3174f9bc-a207-3517-b15a-3598904f9601 | -9.43915 | -40.33324 | 2026-07-04 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 650f51f9-a205-31bb-a6a3-3665c2414bf5 | -5.79774 | -43.6379 | 2026-07-04 03:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3f19417-fe31-3125-b97d-f6161c51bbe9 | -8.95833 | -40.72072 | 2026-07-04 03:40:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cfa1795e-714c-3c74-8e5b-666a4d752fc4 | -6.92847 | -43.71692 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94e4cf02-7b9b-37f5-9cc1-7436dd23acdb | -6.92933 | -43.7122 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5e623e2-6f48-37b1-a1c9-5f1dce73bb6c | -7.01179 | -42.78724 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d6e5442d-04ed-39b6-adea-c028ec61a66c | -5.43388 | -44.65052 | 2026-07-04 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb38806b-6445-317f-b3bf-2765dce558c9 | -7.73541 | -44.17685 | 2026-07-04 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fcd4e1e-0a45-35b1-bafa-26d2cabc958b | -12.75678 | -44.5619 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e39a117-f94a-33c7-8544-e74feda9a20d | -12.73316 | -44.56767 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 921da6e1-251e-3e33-af92-6f3f9230bfd8 | -10.9268 | -43.0583 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 20203efb-fed0-3a2c-bbb8-2da28ff83cdc | -12.76018 | -44.52402 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5317149-b93b-3395-ae2b-ed933cedd1e4 | -12.3461 | -47.90761 | 2026-07-04 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 484badaf-166a-3bd4-8e9a-80243627a215 | -11.4217 | -46.58075 | 2026-07-04 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 644a45cd-9dd2-3022-bd16-c45e69cdd2fd | -10.98363 | -43.71127 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5373ba9e-8c10-3665-bf7c-c29e2688a3a9 | -12.74424 | -44.54284 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9bef9ab3-7a0a-369a-9841-6aed79f02d64 | -12.75932 | -44.52832 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 705f840f-dca6-3dc6-a946-04c7e890896e | -10.92344 | -43.0462 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 071346cc-bd8a-3f22-a176-febfa811b0be | -12.75847 | -44.53259 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38164b97-2151-33b0-a97e-4f2e5a2d0a7c | -12.73144 | -44.57622 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89776c97-ffa3-337b-8476-e9d708a13906 | -11.92267 | -43.39406 | 2026-07-04 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f84d1f7-6402-36f9-a836-f1aff56fb672 | -12.7525 | -44.5625 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6cad6b36-b0ff-3be4-8195-8b7bbb387fc3 | -11.43989 | -46.56603 | 2026-07-04 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4eb4e3ea-2889-3685-b222-5b84d5ebf7b0 | -10.928 | -43.05519 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a1a43b8a-1d0b-3ad8-aa49-6dfef604a025 | -10.9779 | -43.71007 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46b67e60-fba2-372c-81d1-27b87e79529b | -12.73751 | -44.54598 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e570f20-e492-3ff1-97ac-d6f6f4a3efa8 | -12.97261 | -42.58721 | 2026-07-04 03:42:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f136f3c1-429f-3194-b734-040a60d5d110 | -10.92273 | -43.04986 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| be98c21d-1a6b-318c-860a-b4820b5fb471 | -12.74097 | -44.52874 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba465b07-cccb-3c5a-929e-0f0c668b8cac | -12.73901 | -44.56892 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06a38a0e-019a-3c66-a293-a3e948b2d463 | -12.74011 | -44.53302 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 22d0d598-e2e2-34c7-b897-e3512ef4a2a8 | -10.92894 | -43.04732 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e6885677-9843-3ef9-bee9-83a928c0da69 | -12.75009 | -44.54406 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 64b372ad-ae49-3708-a3b6-b0b3e4c10c4c | -11.9241 | -43.38664 | 2026-07-04 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9986f00c-34e3-3280-9e9f-78df21030d08 | -12.75593 | -44.54531 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 43df4c8f-db19-3b15-ab13-fa47ca98b337 | -12.76292 | -44.5322 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65dca357-074b-3623-b2ee-6e8a93244e0c | -12.73814 | -44.57327 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 915f809f-6e25-3284-8222-4fb971ea2e79 | -11.92208 | -43.39143 | 2026-07-04 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17f9c12b-c20a-3555-9fdf-360c75272644 | -12.74923 | -44.54835 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 36a17aa5-b7b7-3e89-86fa-b80eeec54d4f | -12.75521 | -44.51844 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 328fd0fb-dbd9-30b7-8524-6140301419b9 | -10.92965 | -43.04365 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 54b9a0a5-d456-39a9-a4ab-ae92271f7da2 | -12.75179 | -44.53553 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 55ce9d66-fe3c-31b1-887e-2bc2c63e51d8 | -12.76104 | -44.51971 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b5129b4-bf33-304b-9d5d-f58e2b0d4491 | -12.74766 | -44.52575 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39d4796f-bc1f-3713-8e34-e44d5686c1e5 | -12.75922 | -44.55941 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61b83af4-320b-3b47-8db0-632af93eff10 | -12.75762 | -44.53683 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| fcab4df3-41ff-38a9-a914-a5894e904803 | -10.93301 | -43.05575 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fc59901b-67c5-394d-93d4-32000f893919 | -12.73075 | -44.54925 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e52efee-df62-3e5a-bd1c-f7c93637371e | -12.74837 | -44.55265 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ad17de27-75de-355a-9937-49ab164e5a4a | -10.92201 | -43.05352 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ef534e26-06b1-312e-96d8-00a453ffa90f | -12.73727 | -44.57759 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1b58022-ac17-3d38-bbd4-23edfec16af8 | -12.75422 | -44.55386 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f7c3500b-7a58-3258-bb9c-e273bc532c24 | -12.7323 | -44.57196 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02d030ca-d832-3a77-95ab-39fa4750be65 | -12.76177 | -44.54662 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35d4687e-cd6c-3a70-b54d-0a097cfd8ac8 | -11.91237 | -43.38791 | 2026-07-04 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4613ff68-0444-330d-bf95-ff965931decc | -12.75336 | -44.55817 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a1e1255d-8700-3716-8aa2-7bed7516e71a | -12.73163 | -44.54489 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47f7bc6b-772e-3a55-a3f5-ad9713039b81 | -10.92251 | -43.05405 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e8082139-f56f-3354-82c8-f219254f78ef | -12.76092 | -44.55086 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f59982ca-f0d7-3a3f-8e60-abd872030825 | -12.74268 | -44.52022 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
