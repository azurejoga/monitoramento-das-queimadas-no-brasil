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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c19736a-8a77-3f53-ae15-bebb5ee37e5c | -10.75254 | -44.74714 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| deda05bb-1bb8-3f23-81f4-4b7b59949652 | -12.2206 | -43.7073 | 2025-10-30 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 764ad1d8-e5ac-3719-a4be-d2c0706a3d12 | -10.17516 | -44.66252 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2473cb1b-d352-3da3-bb30-58972811e4e5 | -7.95564 | -46.72597 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4615e206-7ca2-30c8-be61-8530f1b4c5c2 | -12.69202 | -46.32808 | 2025-10-30 04:06:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 06851f2b-6ebe-3ec6-b48c-8081dbae8347 | -12.30186 | -50.26579 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d1a79522-601f-3df0-926b-2eb8479f5c07 | -10.88441 | -44.35514 | 2025-10-30 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcd77884-d34a-3885-86c1-24e18f680e81 | -13.2621 | -47.72534 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ad8c7c3-39bb-3d39-8c9f-e1644eb32784 | -13.4249 | -47.36746 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7b94cf7-78dc-3f58-878a-509270e0b605 | -13.52974 | -44.34611 | 2025-10-30 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 28f1b153-49cd-3f72-a7bb-82101cd11084 | -10.7625 | -44.73666 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e708455-446a-3d14-b775-849ceea98191 | -13.37381 | -47.38581 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f5f8fba-d262-32dd-93e9-29e698b3e940 | -13.9854 | -44.02075 | 2025-10-30 04:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d04c4c5-6440-309b-b8a0-a4ab522ebd98 | -13.21648 | -47.73099 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9eca00ac-22d0-36a4-9221-7cabb9cf2f0f | -9.8514 | -47.69389 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba966059-97e8-3bfd-8752-086d1a79eaf9 | -9.85221 | -47.68937 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aae1d155-44ed-32e9-9170-c3f5b77fd36d | -9.734 | -47.69478 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d262020f-7324-382d-afd5-7227ea442c37 | -9.2944 | -48.41673 | 2025-10-30 04:06:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00a64b46-d7ea-3a99-b716-4f6b9455526c | -12.49572 | -50.57014 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d1da9833-ed02-3e78-8f02-11b3a9980737 | -10.4271 | -45.04714 | 2025-10-30 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e0425ce-5a8d-3c22-9060-874f2b62dd90 | -12.49812 | -50.56764 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99f658d0-cb5e-3ba0-8cd4-23a8f3cc7143 | -12.25082 | -47.93665 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59cd0e19-f227-39e4-a83d-3516f49e2ae6 | -13.37979 | -47.42509 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96476d56-f3cf-3b6a-8ccc-f140656c7317 | -12.48124 | -50.59872 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5cff66d-a197-3b40-a2d6-b8a8ec8c3838 | -12.19036 | -46.71337 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c21069d0-3055-3a36-8394-2021822133fd | -10.25841 | -44.56305 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a943d8ae-1066-34ed-982a-92a036282061 | -10.27994 | -44.57155 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc40ec90-5572-3882-8b6d-433f3843b551 | -12.16378 | -46.56261 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62332bc3-b6e9-3e7c-b507-c507722e6f5e | -14.57436 | -41.14188 | 2025-10-30 04:06:00 | NPP-375D | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 485358d5-75ba-30b2-96ef-f5524e3fbe02 | -13.32808 | -47.469 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9913b7cb-d82c-3b7a-b0f4-ad69e5652ee5 | -13.78373 | -44.36297 | 2025-10-30 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fec602f6-f543-3dd7-86ee-60a8158992f5 | -11.17978 | -45.21482 | 2025-10-30 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c27edc8d-1239-30dd-bf6b-372f5be18a03 | -8.19569 | -44.44747 | 2025-10-30 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9fdae2d-aa5a-34cd-a491-7f98584d40e6 | -8.52075 | -48.94569 | 2025-10-30 04:06:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33b8edda-c17b-3ef1-b0ec-df02ceb3239d | -8.19687 | -44.44953 | 2025-10-30 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fe72459-368e-3346-98a7-82ed7ce71963 | -11.11798 | -42.26171 | 2025-10-30 04:06:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9dda7fa0-9092-3f7c-9893-0d8f4687ebb7 | -10.74595 | -44.74346 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad8bd842-7df0-3ee5-9e16-b8b84a2592ee | -12.48588 | -50.60314 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43b45844-7fdc-3aa8-ade7-5feccd120513 | -12.49638 | -50.56682 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5c8704a7-37ba-3009-82df-d34baf802881 | -10.2372 | -47.63763 | 2025-10-30 04:06:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23b364e3-1e27-36d5-963e-89cc2ddbd854 | -13.98887 | -44.02137 | 2025-10-30 04:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 593079b6-6c40-36b8-bb73-6d5e2a2c0824 | -10.24906 | -43.95804 | 2025-10-30 04:06:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7fefd79-605a-30ed-b018-f57b74ed8f8c | -8.33037 | -47.93936 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f7646ed9-9c31-341e-88c8-555d13907680 | -10.43 | -40.50378 | 2025-10-30 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c896dbc7-ec12-36ca-8c3d-a1b65b13de07 | -12.70573 | -46.29692 | 2025-10-30 04:06:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8954fa9d-feb7-3e36-8807-537fb2d867af | -13.87291 | -43.55797 | 2025-10-30 04:06:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0695dbba-5e25-3dca-8595-a6ad6ac10ab0 | -7.88558 | -46.74254 | 2025-10-30 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f7047eb-6cd8-304c-8c7d-47c173ef1df8 | -9.90584 | -47.91368 | 2025-10-30 04:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e1c74870-105e-3e0e-a698-ffa9177a89ef | -9.81538 | -47.58131 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88858a3a-8c28-3b99-a788-aebc1b060d94 | -10.94949 | -50.20488 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a4ae1e3-c33a-370c-9460-57fe92b4f8a9 | -12.32418 | -48.06262 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 253c0333-d832-307e-9526-c0216d9027fb | -13.33143 | -47.69247 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e399c16-05d5-34f0-9a7a-9c195817375c | -13.3065 | -47.70729 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 818ea6c7-d404-3f79-9087-9a7685096fb4 | -12.17925 | -47.751 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 407643cf-ffd6-380a-b16a-44e8b298cdb5 | -11.16061 | -41.10372 | 2025-10-30 04:06:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 638b80c8-813f-3952-859b-145bfd49efe6 | -13.38394 | -48.51147 | 2025-10-30 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10dee2b4-bba6-3ee0-b3a3-b4ad8fe693f5 | -12.88562 | -48.63314 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f95dc56-946f-3857-bd14-524048949a44 | -12.85344 | -43.76806 | 2025-10-30 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18783eab-cf00-368e-8a9a-dede5bf6f427 | -12.25729 | -47.94043 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7fde4f4-fd0b-33ce-89f0-2086706db817 | -13.93001 | -44.20148 | 2025-10-30 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c6d4820-bde0-3259-b2c2-0ba9f4e480ac | -9.8974 | -44.88411 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02847195-5336-31e0-98cd-03c1681a0704 | -10.97366 | -50.21317 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2deb4f6f-5a2e-36e4-9811-9cbb27bc61d1 | -13.29112 | -47.3661 | 2025-10-30 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5829ca1-5f25-3343-a554-a6186a31b20f | -14.28725 | -42.3397 | 2025-10-30 04:06:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57b350c4-fdac-3d76-8104-d3771eb97864 | -13.28629 | -47.72032 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8d3684c-3334-3a59-aead-c3e2114d1901 | -7.95855 | -46.7354 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70f51a08-43d1-310d-a2c2-0d83851daf22 | -11.05953 | -47.53767 | 2025-10-30 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee362ef8-55f3-322e-ada5-cd0a1d0e79b6 | -13.17029 | -48.44571 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 792c1850-992e-3f3d-8b3f-b4c0d500a0d5 | -13.16933 | -40.8246 | 2025-10-30 04:06:00 | NPP-375D | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 71657fe8-baf4-3bbc-914e-e4e82127f859 | -13.3226 | -47.47499 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1698ec81-3ecb-3efb-ab54-c49fa5221468 | -10.34952 | -47.27462 | 2025-10-30 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c94edc0-5b21-348d-9f5f-44ddcdfa421e | -8.33129 | -47.93414 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 321daec7-e12f-39ac-9b16-47cbc650ff4b | -11.1382 | -44.93727 | 2025-10-30 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8946518-47a4-3c2e-922b-fca7575273c4 | -12.81635 | -43.4559 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6a3411e-9310-3aef-8c1e-e6f5644306c1 | -12.32513 | -50.17197 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 971d28cd-4cc9-38e1-873e-abe411419598 | -12.71662 | -46.30491 | 2025-10-30 04:06:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbe0e9dc-9773-3c9b-994f-fba1b8be98db | -10.25766 | -44.56741 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afc87190-bdb3-3afb-b0c0-9ae0028e00c2 | -10.64705 | -47.89225 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ec38d0f-40ef-33b8-a6fa-bae8c3fb941e | -10.08594 | -36.24346 | 2025-10-30 04:06:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| d65fe695-4ade-33c6-a33e-39a2c5317ab6 | -10.42167 | -45.0559 | 2025-10-30 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db02af4c-60a3-310a-a056-8b19e0d68ef8 | -13.60657 | -43.56398 | 2025-10-30 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e23dad85-2c28-383d-a9b3-b86902297fd4 | -11.95331 | -49.93944 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a86f8c2f-ef83-3411-adeb-e6677e997a25 | -9.812 | -44.7283 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 945c3ef9-cefd-35f0-a9d2-a5852876e7ee | -10.8583 | -47.86926 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f6d200d9-d4e2-3378-832a-f25c5dd3fdab | -11.06041 | -50.32225 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6ade19b-a9c1-34c7-bed5-f9220e4662bc | -13.88776 | -43.93626 | 2025-10-30 04:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 051f6b07-667f-38e9-b5e1-052a38822b53 | -9.91048 | -47.91446 | 2025-10-30 04:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8c03a578-5158-3558-a935-d5decb515c3f | -13.21718 | -47.72712 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 684feaa2-d5fd-3508-bf9d-f2b0936f6e6e | -13.99209 | -40.44326 | 2025-10-30 04:06:00 | NPP-375D | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b9cc5af6-414a-3b1e-b75c-29fda087ba27 | -10.94357 | -50.20716 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa505c60-23ff-30ca-937e-a22c5c6eae3b | -13.60928 | -47.59682 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10bffd66-f8b4-3331-b038-2e72810b76bb | -8.51566 | -48.94481 | 2025-10-30 04:06:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68412430-0b08-30a6-8140-db89e768246f | -13.40962 | -47.38012 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 604585e4-9c36-37fb-a462-2c708053114f | -10.35833 | -47.27621 | 2025-10-30 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfabd5bc-8214-382d-b4d8-04286c4900be | -10.26694 | -43.91805 | 2025-10-30 04:06:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af6ce659-ad9b-3dda-b502-a8b5924af05e | -13.36343 | -43.08785 | 2025-10-30 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 89210046-b072-3441-9616-62a3a0b55c09 | -12.29607 | -50.26792 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d50a0a8c-c95c-3b6d-9510-5140580217bf | -13.73163 | -44.24288 | 2025-10-30 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa1e4dd5-f1cb-3b1a-bbed-3139593851c2 | -12.48168 | -50.56771 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a11395fb-4760-349f-aeb8-1cc96e0bf8b2 | -13.8884 | -43.93236 | 2025-10-30 04:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README30.md)
