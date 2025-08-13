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
| f1f5e751-27b5-3143-b856-e91d753640ce | -10.0833 | -50.3293 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ab816a2-b765-3f9b-9901-c9180d1806a8 | -10.8944 | -50.5285 | 2025-08-13 00:12:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0ea6b57-f52a-3da9-9924-b9ce0257750f | -11.4573 | -47.2953 | 2025-08-13 00:12:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fdc2b502-81fd-36f3-aa72-efea1f1ddb84 | -15.1018 | -51.3228 | 2025-08-13 00:12:00 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b4a7d250-adb1-362f-860f-9b88cc27b536 | -12.318 | -46.0308 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53fbcee0-e49b-3ecc-81af-01cecf1cd40a | -6.3087 | -51.375301 | 2025-08-13 00:12:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58cf8fab-a688-35cc-a911-2fd183050fd7 | -5.4369 | -43.5532 | 2025-08-13 00:12:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e2bd940-dcda-3ede-9b2b-7aa0b4af03ed | -18.537001 | -46.039501 | 2025-08-13 00:12:00 | METOP-B | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ec30302e-ff00-397f-8ef2-6cf023bfe338 | -4.2174 | -47.2099 | 2025-08-13 00:12:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f5e912c-1458-33d0-b85e-03a09a85ee86 | -12.3082 | -46.0331 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f89a71b0-b3d3-3cbe-9a2b-770079f3fda6 | -12.5461 | -46.960098 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 320871bc-1459-3462-b6e2-49e3912d1398 | -6.8689 | -59.039501 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f48ad3f3-2bbe-3dce-aa4c-3ecc1ac480f1 | -8.3837 | -49.356701 | 2025-08-13 00:12:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc62b98c-5a9b-3e81-80b8-ddb0a7377633 | -11.7648 | -48.179401 | 2025-08-13 00:12:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b20d5919-4d90-3c50-a9f4-25dd20aadb09 | -22.137699 | -49.640301 | 2025-08-13 00:12:00 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6c66531e-e148-32f8-88fe-d742590c7ea8 | -12.3098 | -46.040199 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8acfdf50-ccd4-36a0-b1e2-ddc2df154166 | -11.9917 | -45.138199 | 2025-08-13 00:12:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1467f091-4046-3c6a-9fd6-628943c6336d | -19.258699 | -46.293201 | 2025-08-13 00:12:00 | METOP-B | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eac19517-3c86-3f7b-9c91-7d81d0c94ac0 | -15.0941 | -51.335602 | 2025-08-13 00:12:00 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f9518a0a-6ef2-322f-baf8-7ac87ec91750 | -10.2441 | -50.2183 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 933bb427-4e57-3b86-97fa-5bfc76570c69 | -7.0849 | -59.9547 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87885dfd-0fb3-35fe-8e54-5726a03918a3 | -14.2661 | -54.506199 | 2025-08-13 00:12:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0711317d-9d36-3182-8598-5080bc3a2bb8 | -6.8841 | -59.064301 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b5e6d3a-2db0-3289-bc3b-a1dc48903481 | -10.7445 | -48.1684 | 2025-08-13 00:12:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75bca62e-3549-3841-a844-d346dc76ad1e | -15.5455 | -43.143902 | 2025-08-13 00:12:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 18fc068c-90fd-38e4-b80c-305c0571d899 | -12.5265 | -46.9646 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f92dcc21-43aa-3a69-bcb3-446f3629346d | -4.7623 | -45.309101 | 2025-08-13 00:12:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0702f1a-828f-3f04-a07f-24b35a7455b1 | -11.9853 | -45.1553 | 2025-08-13 00:12:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf5d4fa3-221d-35d1-b762-2d247cab93ad | -15.0962 | -51.346401 | 2025-08-13 00:12:00 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d6ae6e84-b015-3abc-8edb-afa9d885dfcb | -5.8944 | -57.696301 | 2025-08-13 00:12:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c28cf1ac-04ed-3103-b4e4-7284f6656c59 | -15.5435 | -43.135601 | 2025-08-13 00:12:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 9f82aac3-323f-3317-8164-f0e938f4879b | -9.1823 | -59.578999 | 2025-08-13 00:12:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7cbe02b4-895f-378f-8e82-a986603191ff | -22.3874 | -45.4524 | 2025-08-13 00:12:00 | METOP-B | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8468cd2-5bff-392b-a279-da14be234104 | -10.2326 | -50.212299 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e41ac326-7eb2-3033-8b38-dfa899fc67f1 | -7.876 | -47.2593 | 2025-08-13 00:12:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbcd6384-f8f7-36a1-b774-a5ced215db32 | -9.192 | -59.577202 | 2025-08-13 00:12:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd1c6c6d-a84b-34ca-a5bc-1b249ea12c4e | -12.5394 | -46.976299 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01348ec3-5a04-3edc-bfd9-2d22663523d8 | -14.1134 | -44.313702 | 2025-08-13 00:12:00 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1390399-7f52-33ec-88fb-c984980d10de | -11.9836 | -45.1479 | 2025-08-13 00:12:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d2b19d5-55c0-37b0-a694-872894ce331c | -11.9181 | -52.509102 | 2025-08-13 00:12:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9725d6-0b07-371e-9e33-a2cf59b8e1d7 | -16.3155 | -52.880699 | 2025-08-13 00:12:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25dd263a-6292-3974-b47d-ef4ab970faa9 | -10.3472 | -50.797901 | 2025-08-13 00:12:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a03a443b-4d36-3889-abf2-c6c93871a9db | -10.9658 | -49.565701 | 2025-08-13 00:12:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f48b42e5-9bf0-3ddd-870a-8400ad05eab7 | -12.5518 | -47.032299 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5e994a1-6aa1-3e2a-86bd-f7cd883e62b7 | -18.0604 | -51.2775 | 2025-08-13 00:12:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0c79c914-5006-31f3-baf1-eb0517872941 | -18.527201 | -46.041801 | 2025-08-13 00:12:00 | METOP-B | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c2b7d562-1d27-3627-89e0-8e240285ad22 | -10.1812 | -49.497002 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57072c04-3bd6-3924-ba96-2c21485319ae | -5.8641 | -42.393501 | 2025-08-13 00:12:00 | METOP-B | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2fa61312-4776-362a-9292-7eb27e5f54e7 | -4.2256 | -47.2005 | 2025-08-13 00:12:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5e828d0-bb74-3350-acd7-bcc0ca63fd5b | -6.8799 | -59.093102 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb5fca27-17dc-3171-9822-6697fe36847a | -5.8847 | -57.698299 | 2025-08-13 00:12:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83c29c46-14e1-355b-a802-7496eda932cc | -10.1894 | -49.487202 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 512db1b5-8d4f-3651-b692-696d60608d72 | -7.1296 | -60.076599 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76071515-7e14-330e-b391-5bb776478003 | -6.8951 | -59.118099 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2fd23da-5e7e-3265-8e6b-32659527c977 | -18.0513 | -47.925499 | 2025-08-13 00:12:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bdcf4d56-7168-353c-b8b8-cf23a0f8ca89 | -4.9535 | -47.594002 | 2025-08-13 00:12:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 29f1474e-504c-316e-b3c3-ae18433066ae | -10.7141 | -48.828499 | 2025-08-13 00:12:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19d0462f-3ff8-329c-bc19-20a05568e34d | -6.8702 | -59.0951 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6982f829-c185-3fab-98b8-9a28e7f508a0 | -9.359 | -40.6982 | 2025-08-13 00:12:00 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| fefe1698-a442-3acb-812f-5ce235aa352a | -9.9458 | -48.3242 | 2025-08-13 00:12:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94e3748e-edff-33e8-b514-10c7003b408a | -11.4506 | -47.311501 | 2025-08-13 00:12:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e4bb306-8b23-3f0a-9fe1-3dc9516c8910 | -10.7619 | -48.764599 | 2025-08-13 00:12:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0285fff0-45f3-393e-8f2c-1a7ccfd70548 | -11.7664 | -48.1866 | 2025-08-13 00:12:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e85e107a-5709-349a-852e-0641f29f9170 | -13.5337 | -47.618099 | 2025-08-13 00:12:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a2daa481-eefc-3fb7-a711-fe09e467a58e | -12.1495 | -48.011101 | 2025-08-13 00:12:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39a40518-dd6e-3f77-a438-225e55e04156 | -6.8786 | -59.037601 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ecceb998-728c-352e-b777-b8569b01c955 | -20.982 | -43.250099 | 2025-08-13 00:12:00 | METOP-B | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d09a3c79-e728-396d-9f1e-c5767b0ebdf2 | -11.4604 | -47.309299 | 2025-08-13 00:12:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7165b7c-3e62-3cba-9a27-2bdff020c162 | -18.062599 | -51.289299 | 2025-08-13 00:12:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7faf24b3-e718-3b87-98ba-efeba595341a | -12.3244 | -46.0592 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9447392a-ff8f-3f95-84ea-5dd4ba2f6c99 | -10.9723 | -49.548199 | 2025-08-13 00:12:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73d423be-4003-30a0-9132-8bfcdb703e76 | -8.3805 | -49.342201 | 2025-08-13 00:12:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac36c3a8-e723-3e40-963e-9d31e0e0fe61 | -15.1039 | -51.3335 | 2025-08-13 00:12:00 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b893804-d466-38fe-b599-fd1bb9694045 | -21.5667 | -44.211102 | 2025-08-13 00:12:00 | METOP-B | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 846e9277-e595-3f3b-ba42-a0bb74ff7240 | -6.8937 | -59.062401 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f605bf04-2f49-386e-8b01-c678b2110a02 | -12.5378 | -46.969299 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfffea0a-7294-3a50-beb6-d4657330e916 | -16.601801 | -47.0289 | 2025-08-13 00:12:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2171d4b2-cf5f-3516-a135-d893d0721f20 | -6.8551 | -59.070099 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5bc0807-b825-3100-8378-b3c45452cd87 | -6.8606 | -59.097 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a24d487c-97e7-3506-a871-f6acffc1d0fc | -10.7635 | -48.771801 | 2025-08-13 00:12:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e53a3d78-c8e4-3815-901b-f4ebd6d94906 | -12.6781 | -46.952 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6faa0924-a32a-38c2-ab0a-bbe91c4f2559 | -10.2539 | -50.216099 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd89947c-4c19-370c-8d98-8fd8b1d8dd8b | -6.913 | -59.058498 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0387f08-9063-35ff-8f66-102ac0592f82 | -6.8882 | -59.035702 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6003b5af-b00a-3303-8cff-15b789c14a74 | -11.9951 | -45.153 | 2025-08-13 00:12:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be2d189c-b502-3469-98fb-4e49476f431d | -12.3212 | -46.044998 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9424223c-f0f5-3b7d-9bd9-711f6f0d57fe | -7.0786 | -59.923698 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f90d54bb-8559-381e-b2f2-556777be8d93 | -20.923901 | -45.234901 | 2025-08-13 00:12:00 | METOP-B | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 125cf406-3521-39b5-b117-9f7ae368b701 | -6.8854 | -59.119999 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97c9a95b-1750-3211-9a48-4d1f662470d3 | -7.7122 | -42.1548 | 2025-08-13 00:12:00 | METOP-B | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87b1f179-eeee-3ec9-9db1-7a9878983347 | -12.5832 | -46.9883 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01904308-a152-3871-bd9b-3456cca155c9 | -6.8896 | -59.091202 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4668cca3-cba4-3947-8fa1-8b5697284561 | -12.5817 | -46.9813 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4067ce8b-8be9-3866-ab73-d86b96f0d581 | -5.3162 | -45.209202 | 2025-08-13 00:12:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6105ad2c-ee47-3391-b03c-074da55ed687 | -12.691 | -46.963799 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 278a44ca-c826-345e-a6c0-f2508fd8207f | -20.3783 | -46.5439 | 2025-08-13 00:12:00 | METOP-B | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 087cd067-8132-3c50-9832-cabfe0dde6bc | -6.8744 | -59.0662 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 822c70bf-2820-3b60-9424-32718bdab11f | -20.980301 | -43.2425 | 2025-08-13 00:12:00 | METOP-B | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e3ab6b93-3caf-3bd3-8db8-ed95af0df5ff | -7.8053 | -48.369099 | 2025-08-13 00:12:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 356f7c58-e8f1-36f1-95f6-61aac11850c0 | -6.9089 | -59.087399 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
