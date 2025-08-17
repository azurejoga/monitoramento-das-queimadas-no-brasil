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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e22b7890-0437-3821-ac0e-3b97be95c79e | -22.7684 | -49.110901 | 2025-08-17 00:26:00 | METOP-B | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 773d1440-4a24-34a5-bacc-1881118c7ea6 | -9.1786 | -59.626499 | 2025-08-17 00:26:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da47477d-a276-39f5-b6b4-d4494a6e6dd4 | -14.6302 | -54.8792 | 2025-08-17 00:26:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff96babf-36f1-3027-9d31-65d7bd8c1ab2 | -13.4343 | -45.882599 | 2025-08-17 00:26:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a64e66a4-df2a-36f3-ad5a-4e2fad730bfd | -9.5017 | -60.524601 | 2025-08-17 00:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8f1d6c7-3168-335c-bd7b-79679baa6fdf | -12.5402 | -46.931301 | 2025-08-17 00:26:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1a85f33-60ed-3559-8d1c-d9afe0eb0d43 | -7.1129 | -46.109402 | 2025-08-17 00:26:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4891f58e-668c-3cfd-a736-4b34888af2f9 | -13.4369 | -45.893398 | 2025-08-17 00:26:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b15c2cf6-99ef-329b-960f-94aee957e23f | -7.1098 | -46.0965 | 2025-08-17 00:26:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a23529f-a4f8-3e3e-ab1f-37042540e62d | -12.55 | -46.928902 | 2025-08-17 00:26:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c39c56c5-4d62-32de-8a22-2bcf365a6427 | -9.5114 | -60.522598 | 2025-08-17 00:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81dc3491-7242-39e2-a9de-48496daa1ff1 | -10.4477 | -55.416801 | 2025-08-17 00:26:00 | METOP-B | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a7953d1-60e0-38d3-a2fc-c1d5176ce7f7 | -15.1815 | -48.770802 | 2025-08-17 00:26:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 288305d3-99a4-364a-85e6-b0494622e925 | -8.7488 | -44.037201 | 2025-08-17 00:26:00 | METOP-B | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f1baf93-53ec-34ee-9ba6-d58065b4c4d3 | -4.776 | -45.320499 | 2025-08-17 00:26:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15999bb9-e012-32e5-b15c-4b8e6815f0e9 | -14.084 | -54.061798 | 2025-08-17 00:26:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be8eddb8-66bf-3b3f-92cd-b35361c6aecd | -11.3631 | -55.389801 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d41665e5-04bb-3cca-a2e3-b42741bb47c6 | -14.9712 | -54.748501 | 2025-08-17 00:26:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c6db39b-5d2c-3cea-8c36-54a1556e6850 | -10.1155 | -57.743999 | 2025-08-17 00:26:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ceaa0613-6d66-3b85-a89b-382e9824606f | -10.8275 | -45.318199 | 2025-08-17 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9dd72c1-5924-34b4-af58-cf1119d464e1 | -13.5739 | -46.976398 | 2025-08-17 00:26:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 05009c6b-d690-39ac-9d12-77b64f7f522f | -6.1904 | -45.4375 | 2025-08-17 00:26:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edf599f5-c745-35d5-908c-08d75e7ac65f | -14.5973 | -47.9417 | 2025-08-17 00:26:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f093a090-a369-36ed-ab9a-61a46d5b47ef | -11.4286 | -52.206001 | 2025-08-17 00:26:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2885fbd-e76f-355c-a6c7-dbe2f494d6a5 | -14.0875 | -54.078701 | 2025-08-17 00:26:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a81a447-2742-3366-a703-1dacba192e80 | -6.54 | -43.0396 | 2025-08-17 00:26:00 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9d771e0-18af-3cd6-a5b2-377119ea149a | -9.7665 | -48.739101 | 2025-08-17 00:26:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10fbe82c-ce95-3b37-ac65-fbcc201b3825 | -9.6944 | -46.259102 | 2025-08-17 00:26:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd1ac331-557d-32a6-b22f-d9641fbb229d | -4.0701 | -48.041698 | 2025-08-17 00:26:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac9ccdf5-5fe7-32c3-ac24-6c52412e50b1 | -12.1402 | -47.900799 | 2025-08-17 00:26:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 178bfb0e-b3e3-3446-b927-0ee374e87c3b | -23.3083 | -50.072201 | 2025-08-17 00:26:00 | METOP-B | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 78a464d3-0644-373c-aaed-abb54b08c88c | -14.5521 | -48.5919 | 2025-08-17 00:26:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 141fff49-3cde-3992-bab3-e315f662c495 | -11.092 | -44.7999 | 2025-08-17 00:26:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce6f2b5a-f356-3f8f-8954-23b57fe0e8bb | -14.9248 | -54.6712 | 2025-08-17 00:26:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f4e1534-4084-38d1-81e5-8d43abac722d | -15.1798 | -48.763199 | 2025-08-17 00:26:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10ab2da0-1d89-3738-8378-00f1d343a0c4 | -19.482401 | -44.751202 | 2025-08-17 00:26:00 | METOP-B | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 99add7aa-d0b3-3956-abd6-1e8ccddb0500 | -9.5175 | -60.502602 | 2025-08-17 00:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efd30648-7c66-33b9-af21-f0af00705dd7 | -25.183701 | -50.076 | 2025-08-17 00:26:00 | METOP-B | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3321c67-be4c-3b98-86d0-5f3806e9a36b | -13.5642 | -46.978901 | 2025-08-17 00:26:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c6bf1533-2941-3cc3-b5ba-a9738a9ac2eb | -10.8403 | -45.328701 | 2025-08-17 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28e1d012-b5f2-3c25-a3dd-4739d7f2a658 | -16.493799 | -45.111 | 2025-08-17 00:26:00 | METOP-B | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4b15540e-737d-3352-98ab-629d564b56f1 | -14.3625 | -47.033401 | 2025-08-17 00:26:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3bc246ae-1f35-3b87-98ae-42aaf75f0e69 | -6.0768 | -44.625801 | 2025-08-17 00:26:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb5293e7-034b-3e8a-b68a-e08a31ee605a | -8.8055 | -52.073101 | 2025-08-17 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12ac03f6-8325-309f-9b88-ac408994983e | -6.1413 | -57.922798 | 2025-08-17 00:26:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7168b33-e134-332f-a9ea-819054ef6546 | -13.0126 | -42.316101 | 2025-08-17 00:26:00 | METOP-B | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 82e97f30-af70-3829-9278-6b65bcaec49f | -8.0382 | -47.659698 | 2025-08-17 00:26:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01ba0fd9-5c27-3fcc-bdb0-83863ecbc5db | -11.3649 | -55.3988 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7e33b26-6c05-3a84-be1f-7c117c536978 | -10.3202 | -54.1474 | 2025-08-17 00:26:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92b4cd6e-26d2-3541-8586-1cf4b5beb472 | -9.7685 | -48.747398 | 2025-08-17 00:26:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed84c4a7-57e1-3497-bf89-755cbf96ab16 | -9.5041 | -60.486301 | 2025-08-17 00:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| beb80861-670b-3e5a-8174-8d7e74daa691 | -9.7704 | -48.755798 | 2025-08-17 00:26:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1117a42d-f51e-306e-a210-d1676c9b18a4 | -10.3219 | -54.155102 | 2025-08-17 00:26:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25c0beac-f3c7-3540-8874-4a5b13034c15 | -8.819 | -52.0411 | 2025-08-17 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b33767cd-7e22-3d23-9795-1fd506a867cd | -15.1895 | -48.760799 | 2025-08-17 00:26:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 97f0b953-dfe1-301d-a052-7718ac168543 | -14.9693 | -54.739201 | 2025-08-17 00:26:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60977dd6-1ee1-344c-8f39-19725fe498a2 | -8.4976 | -44.73 | 2025-08-17 00:26:00 | METOP-B | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0fc9c47a-d219-3db8-9f3a-948a9c205ada | -12.5546 | -46.948299 | 2025-08-17 00:26:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9f4d60c-02fb-3e8c-9ec0-5d1b969022a2 | -20.8241 | -44.514301 | 2025-08-17 00:26:00 | METOP-B | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 21536941-9584-3ded-bbb9-7e4546324822 | -11.3785 | -55.414799 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 861408bd-c465-3765-9d34-5a0cdc24b448 | -11.3593 | -55.3717 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92ebc22a-5c72-3b32-9751-d3c305f646f4 | -14.0857 | -54.070202 | 2025-08-17 00:26:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cdd1f6d5-35b8-31ac-94fc-9cc088950f3c | -13.0174 | -42.334801 | 2025-08-17 00:26:00 | METOP-B | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 64205c00-2941-39e9-8c88-cc82bc92e0e8 | -20.483801 | -49.344101 | 2025-08-17 00:26:00 | METOP-B | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38cf1578-c90a-317c-9feb-cc56c831636c | -6.1389 | -57.911999 | 2025-08-17 00:26:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 807a72f3-9d6f-32ba-845a-26989957beda | -13.5951 | -47.763802 | 2025-08-17 00:26:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 57530ca1-5268-3354-8730-35f7832a906d | -14.9614 | -54.750599 | 2025-08-17 00:26:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 95cd30e0-cb40-3c78-b41c-9c2fef8f907e | -11.3687 | -55.416901 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78c374b8-6d01-39b3-8425-31014cfa1268 | -8.0406 | -47.6698 | 2025-08-17 00:26:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96e4c5c3-16cc-3640-94d0-31a6285f369f | -8.9864 | -60.478298 | 2025-08-17 00:26:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19f89d88-2b6e-39b0-b1b8-288fd982aaa6 | -6.1807 | -45.439899 | 2025-08-17 00:26:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec7f7294-c215-3a97-b8ca-78f60fcc49e9 | -11.3551 | -55.400799 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e578c6c-7de3-35ca-8c6a-ccabe3233b6b | -2.9008 | -51.472801 | 2025-08-17 00:26:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e069e8a-efa6-3c82-87ca-9812576c24a7 | -9.5078 | -60.504501 | 2025-08-17 00:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26f4466f-f01e-3d29-b313-8c4dba5d817e | -20.292299 | -46.044899 | 2025-08-17 00:26:00 | METOP-B | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c62890ee-6784-31b2-9d25-15e1acfdc2b0 | -11.3491 | -55.421001 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12969ad2-a82f-3440-98a1-c051bb839de0 | -8.9767 | -60.480202 | 2025-08-17 00:26:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1afc420d-ab62-3bcc-b523-4f9ed9aaf86f | -14.9354 | -47.0522 | 2025-08-17 00:26:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bf050931-886a-3167-9e94-163f1d95dd32 | -6.5496 | -43.037201 | 2025-08-17 00:26:00 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d36a843-a803-3c57-a552-b0d009126482 | -4.9139 | -43.255299 | 2025-08-17 00:26:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acc00049-45ff-3db5-8002-b543d6bcef42 | -13.1644 | -55.701599 | 2025-08-17 00:26:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f64422ff-2bee-32e3-b0b9-c7215b416f92 | -11.8583 | -48.1954 | 2025-08-17 00:26:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebcd149a-dc68-3583-ac6d-2886f2a71fd1 | -12.616 | -46.902302 | 2025-08-17 00:26:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bceca189-1be7-337f-9c36-21646b1207ea | -14.9791 | -54.737099 | 2025-08-17 00:26:00 | METOP-B | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f742159d-498b-3538-8721-83a5fd9261a9 | -13.5853 | -47.766201 | 2025-08-17 00:26:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 59709f13-2ec9-3f8e-857f-7f5b26bebedb | -4.9183 | -43.230801 | 2025-08-17 00:26:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5f7edab-14ad-360a-b54e-da725398c8be | -11.3533 | -55.3918 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc9df147-9ded-3ff9-8a5f-7c654e9dfa97 | -8.0359 | -47.6497 | 2025-08-17 00:26:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc59f86c-e917-3bba-bbae-7be5f4c7687d | -11.3668 | -55.407799 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8901fa-6523-3efd-bb5a-731e0963f997 | -10.834 | -45.303001 | 2025-08-17 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0bcb2b84-7ef9-35c1-9d62-c558f5a970f0 | -6.175 | -47.273899 | 2025-08-17 00:26:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09fbd4bd-3145-36b6-842a-3227a1bea85f | -14.1836 | -45.310902 | 2025-08-17 00:26:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c5141d68-d9db-3dcf-b979-d49090ce26b3 | -14.3647 | -47.0424 | 2025-08-17 00:26:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8d56bd48-8740-3e5d-8fdc-b5ee9427db23 | -13.6288 | -46.903198 | 2025-08-17 00:26:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa0adaec-8480-308e-8ce4-206c66b32e21 | -8.0285 | -47.661999 | 2025-08-17 00:26:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8de35deb-b5a4-3ce8-b39d-fd8716d17b87 | -4.9193 | -43.277302 | 2025-08-17 00:26:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fd71e8f-7c88-341e-bfe9-f413c70c47ae | -14.9772 | -54.727798 | 2025-08-17 00:26:00 | METOP-B | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e910ac7-bea1-3aec-b645-f413921fed81 | -20.482201 | -49.3368 | 2025-08-17 00:26:00 | METOP-B | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9fb763eb-bcb9-37b9-a319-5bd2b6f40e3c | -13.5931 | -47.755299 | 2025-08-17 00:26:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1fdcbed-6615-357e-8c4e-19c7afea6d78 | -6.5347 | -43.018101 | 2025-08-17 00:26:00 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
