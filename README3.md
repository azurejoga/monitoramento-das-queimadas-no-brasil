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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dae1214b-7fc0-3f1b-88ee-d6c378d7bab9 | -7.8701 | -46.422501 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d9866ff-68c1-346b-84dd-1bbc9a96fd42 | -7.8657 | -46.446899 | 2026-09-19 00:19:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee827e1e-cc0d-36fc-9114-babab282ddf2 | -1.3069 | -55.823002 | 2026-09-19 00:19:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69edfb19-9080-31c6-bb7b-aa59b309a704 | -5.296 | -43.433899 | 2026-09-19 00:19:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f6f312c-d859-3908-ac94-3a9414f69a1f | -16.7939 | -46.978298 | 2026-09-19 00:19:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 05049ad4-6b1c-3e44-9807-dd1e29a1b29b | -9.0513 | -48.716 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ce65f572-2e94-3e5c-a0a4-a0386addc0ce | -10.1699 | -48.5112 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9bc58918-1054-38e4-9770-00207d8720be | -4.8077 | -56.074402 | 2026-09-19 00:19:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e107da4a-3677-31b1-a5dc-01ad3c7cddea | -10.8255 | -50.1497 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b72cb7df-ffd2-313d-a264-a655e837abc0 | -5.8623 | -52.037399 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0da5018f-d0dc-3272-97cb-ee7622d10056 | -4.3601 | -47.789501 | 2026-09-19 00:19:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab08c1e2-03b4-30c4-a8b9-93b177d504af | -11.9118 | -50.120899 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 001c2482-e62d-3b4a-9dc1-03776e17eee3 | -5.8607 | -52.030602 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96f20315-5d6b-3e8c-bd34-0bf028dafe9d | -11.1113 | -45.2738 | 2026-09-19 00:19:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56cf7578-02ae-36e1-8613-4d033b820ff4 | -5.9938 | -51.798801 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf771738-d263-3955-890a-d7cbe9b09a7b | -12.1464 | -46.993599 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a95cec1c-a6ba-32ed-be6c-67d893bef5d3 | -4.5414 | -54.918999 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e69df593-5ce1-32a1-b5f0-c0f6e07e4eaf | -9.6563 | -54.305099 | 2026-09-19 00:19:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d5c6991-eea4-345e-8e06-e6e7a2c34e8b | -5.8602 | -51.937099 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43c46e96-31b1-3d4c-b072-1eb5968c2831 | -9.9315 | -45.262798 | 2026-09-19 00:19:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c82a101-21d6-347f-ae81-f27dc5aa4631 | -21.0201 | -47.248798 | 2026-09-19 00:19:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e2899219-fe5e-3b99-851a-9b9680d8fa74 | -8.0131 | -49.043301 | 2026-09-19 00:19:00 | METOP-B | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5f6ef3e7-04c1-354b-9890-786319415730 | -8.3758 | -47.202801 | 2026-09-19 00:19:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb02d383-57f3-3c09-a9b4-4111c13131aa | -6.7123 | -59.440399 | 2026-09-19 00:19:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d59e5d66-d382-304d-b194-4f41504ec101 | -6.6483 | -50.9133 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a68fdc0-e747-3a21-8429-7d5c8a33a1fd | -4.5512 | -54.916901 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10131afe-27c9-33fd-ae33-cb5ab3ebd4ff | -14.3896 | -52.119202 | 2026-09-19 00:19:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77353d7d-7d56-3f33-933d-5764cb4a3006 | -14.7978 | -48.571098 | 2026-09-19 00:19:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 22026786-fba3-3a16-96ac-055a4c3aa1e3 | -7.6462 | -46.090401 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ede2e92a-ec84-3c2d-82dc-90975259d000 | -9.9532 | -46.546799 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74359c37-f18f-3ffb-bf57-f7d4b36ea89a | -8.9843 | -50.169998 | 2026-09-19 00:19:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6a067fa-cf26-3400-8e0c-96027e748dce | -6.9705 | -42.1604 | 2026-09-19 00:19:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50494811-cb31-35b0-8a80-06045f7e3ebf | -12.1177 | -50.853802 | 2026-09-19 00:19:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10847bc9-e4ed-33f7-bcfe-8e13b71228cd | -3.2243 | -46.9347 | 2026-09-19 00:19:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d45bfbc9-00ad-30bb-9cf1-5c47a1105484 | -5.2254 | -49.296501 | 2026-09-19 00:19:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51a7738d-46fa-3bab-ab23-a2e15cb8a2db | -3.4861 | -59.566898 | 2026-09-19 00:19:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee193c6e-8ce8-30ba-ab9a-52847af3b495 | -13.3832 | -48.034302 | 2026-09-19 00:19:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8697c4c4-be60-3976-aba8-d5af3f0aefdb | -10.8692 | -53.9823 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 468f2da7-0d13-3ce7-894f-d7b42621bd66 | -4.3915 | -43.591301 | 2026-09-19 00:19:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f3a5411-a8b2-39c5-b820-fd28ef064644 | -3.2298 | -46.958599 | 2026-09-19 00:19:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 594d1a0d-eb0a-39d9-8de1-2f7e1bce1fe3 | -9.0532 | -48.723999 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 50e2009f-4ced-3251-96a6-f7ee8883c6f5 | -12.9915 | -46.984299 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97119df8-6cf4-3e34-8c4f-ee0d2c1a926f | -5.5131 | -43.778198 | 2026-09-19 00:19:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6653aaf8-b9f0-3b59-a76c-9000dd110111 | -6.9664 | -42.185001 | 2026-09-19 00:19:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7a1b47e8-e0d3-3140-a102-c8dc07c56bc7 | -5.3279 | -48.982498 | 2026-09-19 00:19:00 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 276395bc-c9a5-3dee-a29d-1a0e38dcab5a | -2.8235 | -50.461201 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a6c2401-6d7e-364e-911c-db816b288a88 | -8.7609 | -44.233398 | 2026-09-19 00:19:00 | METOP-B | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e5a882c-91a3-3ebe-9312-5a83ac1d9304 | -6.745 | -59.402199 | 2026-09-19 00:19:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54ae4701-1af8-309c-ab79-a2ea6dcd6286 | -7.6393 | -46.1045 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ef19554-9afe-3ea5-844e-506c33673d20 | -11.938 | -50.099998 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6cf4c1c-a996-3011-adfa-09ea0931741d | -12.5835 | -49.0849 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2b796ab-b417-3780-bab1-d73979d3bf5a | -11.2541 | -54.104198 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ccb379a-4b38-3592-98c6-e0ab82c799b9 | -2.8137 | -50.463402 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2e61fcb-b126-35f1-943f-bd525b3c71a6 | -11.273 | -43.5121 | 2026-09-19 00:19:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05f6fbe9-973f-3f3b-999b-5c55327ddbee | -2.0244 | -48.771301 | 2026-09-19 00:19:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52a0ac10-8511-3712-94b4-db49d0b3e12b | -10.9101 | -53.981899 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0fa057f-affb-38b6-848a-cf2a8dba11b6 | -8.7702 | -46.908798 | 2026-09-19 00:19:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d772023d-f236-3f50-9a44-a5e564cb09d3 | -11.9881 | -52.460602 | 2026-09-19 00:19:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2b3eace-1e25-32b8-8d8b-0514edd48b52 | -9.713 | -54.806999 | 2026-09-19 00:19:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f8a7184-85d3-3a82-a5c8-693fb61f5967 | -6.6543 | -51.4837 | 2026-09-19 00:19:00 | METOP-B | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40071ba0-4cf0-3914-a5a3-ba8e729ff724 | -4.5529 | -54.9245 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c470601-113e-3d86-858e-f296ae5258dd | -11.9799 | -52.4702 | 2026-09-19 00:19:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d6c40c6-7f72-3c26-aab5-7ff087ff0a96 | -3.3773 | -50.449001 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac796c29-3791-3d28-ad4a-ca1458b665ae | -12.5383 | -47.0774 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afe88681-83a8-3ff5-ae21-de978667af61 | -12.4351 | -49.5644 | 2026-09-19 00:19:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b36e0aff-9026-3db2-9dcc-e976a309c88f | -11.0235 | -54.1283 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce1787df-d84d-3aba-89b4-06a13409bbeb | -16.0527 | -49.979 | 2026-09-19 00:19:00 | METOP-B | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c8b35566-d5c5-392f-9062-3f3a3462a3b1 | -10.8449 | -50.1898 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 064d9512-618c-3cd1-8bcc-a0f54458215b | -14.171 | -47.033401 | 2026-09-19 00:19:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ed65d558-d786-36a1-beb1-5567ea820649 | -10.2335 | -50.904598 | 2026-09-19 00:19:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59a7eb89-b690-3a71-8823-3ebdbbebc984 | -10.8905 | -53.986099 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12b98120-5334-3c81-8ce0-aae815db2fe4 | -21.4611 | -48.6819 | 2026-09-19 00:19:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 735f6056-d1cf-3239-9fb8-1892e3960e36 | -13.6218 | -48.305401 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 426eb422-0c0d-3c6a-aef7-484e0f790b1a | -3.7623 | -55.946602 | 2026-09-19 00:19:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c79972cc-4901-3149-85dd-f1e1eb51ae16 | -5.5549 | -48.450802 | 2026-09-19 00:19:00 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f03700e-e22d-337d-b982-46f08daf0584 | -14.9579 | -47.522598 | 2026-09-19 00:19:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d18c201e-ae6e-3c07-9830-c7db7b4c2965 | -2.8316 | -50.451302 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16c49868-bc7f-3129-ba4a-df858d3a432f | -5.8755 | -53.610298 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c1eb497-fda5-32a7-b8cf-66836a5b1550 | -12.9949 | -46.955299 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2fcd7f2-5aee-3bab-b2a8-425d6fa301a9 | -13.6102 | -48.299999 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e92b18e-3f42-3756-bca0-707162ba4bc6 | -12.4013 | -46.892399 | 2026-09-19 00:19:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31c571ce-d312-37a6-9a78-7ec4a5959aff | -12.5754 | -49.094601 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69a6df1e-6a29-3d42-b794-59b6e0db0ebf | -6.0036 | -51.7966 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eff29345-070c-38d3-ba55-ee2bcb9f7647 | -4.2135 | -56.313301 | 2026-09-19 00:19:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b357e33-940c-3bdc-b225-6c572d1e74de | -4.5333 | -54.928799 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c171ced-2296-3ac1-a333-15bb90eed2ee | -13.0047 | -46.9529 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21c7dcd9-f13a-38aa-8020-cf20e16cc887 | -11.0217 | -54.119999 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe5b4900-f666-3480-8876-c8d755a310ee | -10.8088 | -50.897301 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7035e666-e403-34ab-8702-b382f4825495 | -9.6927 | -54.3311 | 2026-09-19 00:19:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c69eae38-f579-3ec8-9e57-7c3787ecbb49 | -12.1486 | -47.002602 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fb32b86-6139-34e0-9ee4-298916feaeac | -5.2401 | -49.404999 | 2026-09-19 00:19:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4945891e-3419-3d33-aaa5-a412c0b74ad1 | -2.8155 | -50.4711 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09f0c668-96ff-3096-808d-30c55ae8e410 | -9.022 | -48.7229 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 18eb4ee0-d6f7-380d-beba-c739125450ae | -13.0068 | -46.9618 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c11da7b1-a82e-3d10-bc70-09b76856ff41 | -1.4951 | -54.9674 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faa7a70b-e1ed-3e2b-bb3b-74983d15de30 | -2.8333 | -50.459 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3697386e-c78a-31f2-8741-cc22b33d7a22 | -10.7058 | -60.695499 | 2026-09-19 00:19:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c87df068-1ab7-3197-ba50-5a384b3f51d4 | -14.1268 | -45.176498 | 2026-09-19 00:19:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9cb6222-e606-30b0-aa49-55140e838866 | -10.2371 | -48.844398 | 2026-09-19 00:19:00 | METOP-B | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54aeaa81-ff85-3dd8-854f-5a4f0a2e6b9b | -14.6715 | -46.6595 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
