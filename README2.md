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
| 7da40fb6-c14d-3b66-bff9-d2e2ca53d0be | -15.67699 | -48.24222 | 2025-09-02 00:09:00 | TERRA_M-M | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| aa8d3d26-9ae4-3379-83da-133b2d87bcfb | -10.46168 | -49.06231 | 2025-09-02 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| be522593-ad11-3747-a750-9a6f481b289a | -11.05926 | -45.40005 | 2025-09-02 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| da5d1f3e-6196-3269-b93f-67549bb71afa | -11.10001 | -44.62854 | 2025-09-02 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| bca80cd6-38cb-3933-9682-e9fea380c86f | -11.05778 | -45.38849 | 2025-09-02 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 8976d2d5-cc03-3440-a659-a1e21c1ef75a | -11.80656 | -46.41637 | 2025-09-02 00:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bcbbb70e-7e9b-3e6b-9986-e233cfe04a63 | -12.7599 | -44.41445 | 2025-09-02 00:09:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| e528b208-c91d-3984-bf1e-4a966ff20a38 | -14.26021 | -45.24062 | 2025-09-02 00:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| df05f5c5-a369-3938-a49a-e39cec1cdd3e | -11.0468 | -45.14709 | 2025-09-02 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 4fd41105-3f67-3b5b-80b7-e8c1e26be6d0 | -13.31988 | -46.83388 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| f5719c04-e2fc-32b3-83ee-bd8df0ffb5b9 | -16.07505 | -43.61619 | 2025-09-02 00:09:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e4369822-af0b-3052-b8df-934d6bbb115f | -12.57227 | -44.79216 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8d9e5166-9253-3319-a58f-200e884ebc81 | -14.78798 | -48.18598 | 2025-09-02 00:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ba4301d3-1fa4-3c5d-9757-ff090ac01003 | -13.70378 | -46.89086 | 2025-09-02 00:09:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| ecc1e55a-8266-36c9-a049-fb116506e71c | -14.49384 | -45.95099 | 2025-09-02 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| c1cf6aa3-7b2d-35b2-b288-5599051e2452 | -11.86516 | -46.71461 | 2025-09-02 00:09:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9b481163-87b8-3590-93c0-aa4365851cdd | -12.75032 | -44.41577 | 2025-09-02 00:09:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| b296851d-a903-31ae-ad0b-b93e111e0160 | -11.65832 | -52.14357 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| e3a04361-c85a-3874-ad86-489bc8311a63 | -11.54844 | -44.84121 | 2025-09-02 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 10406c97-0723-37e5-bd23-87222a2e732b | -17.88942 | -47.17321 | 2025-09-02 00:09:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| f89738de-5d84-3beb-af0f-dd31147ea9dd | -11.35736 | -43.66892 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 34287aba-4a9c-3cef-8f3a-53d9174cd03c | -15.02742 | -42.14277 | 2025-09-02 00:09:00 | TERRA_M-M | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9a97fd52-5679-3447-9baf-4f4f2cf8eecc | -11.66598 | -52.1748 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1185.2 |
| 2072652f-045c-381e-8ab6-eedacf47ac9d | -13.31104 | -46.84125 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 0ad153fb-af4a-3d61-820c-713bcac79fbd | -17.72111 | -46.81054 | 2025-09-02 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1f8a17c9-4fc6-3db8-b5b9-1054e3b2f746 | -11.54985 | -44.85211 | 2025-09-02 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4bae53ba-8ceb-3755-a48d-90d5dcb9eef4 | -17.70454 | -46.88923 | 2025-09-02 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| facbedd9-c6d9-39cd-85e4-d8fbc47361c1 | -15.02867 | -42.15204 | 2025-09-02 00:09:00 | TERRA_M-M | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 3f23cb27-7da0-3b9a-bf94-58147f0cc1e1 | -11.65305 | -52.21633 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 202.6 |
| 5ef416bb-b130-3d17-a501-ca515f0f7ac4 | -13.49382 | -46.93524 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c6206edf-50ec-3cff-ae2b-fde4302217e8 | -17.61183 | -46.64332 | 2025-09-02 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 46.3 |
| caf200f3-5210-3f2c-bc00-b72b44012e48 | -13.50235 | -47.00513 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a43fefc9-74c4-3a60-8f23-4dcb3463e507 | -13.28069 | -46.87976 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8f241ef2-37b3-344b-a5e9-2f8912d8edce | -13.5021 | -46.93023 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9555d5b7-e2b7-373b-846f-d716423db838 | -12.4396 | -48.71409 | 2025-09-02 00:09:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| de319ccb-9906-38cc-8cf5-85e82610d577 | -11.54747 | -45.06611 | 2025-09-02 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fba61b2a-f0b0-39e2-8078-22a1d0972a89 | -11.30679 | -43.7018 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 90c9394f-9015-3863-ba38-389cc36f06d7 | -10.27102 | -47.51532 | 2025-09-02 00:09:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 32b0af46-1b89-3247-a2db-044b72c19da2 | -19.44262 | -43.82129 | 2025-09-02 00:09:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5f4f0068-3ba9-3c39-8b4f-9b1918d5b22b | -11.79403 | -46.40397 | 2025-09-02 00:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 5c764d35-8d0f-32d1-8a13-95b46b24d52a | -15.88598 | -47.64862 | 2025-09-02 00:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 316db6b8-338d-337b-986a-cfad18359e67 | -12.98306 | -48.1126 | 2025-09-02 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0214afff-82a6-3371-9e3a-3a075bf99136 | -11.39189 | -46.87208 | 2025-09-02 00:09:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c8592e0a-d8e4-3169-82e2-d411043e4447 | -15.78848 | -42.12526 | 2025-09-02 00:09:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b9b0420d-ba35-3c55-ab85-ad7ce3be7543 | -13.76162 | -43.77937 | 2025-09-02 00:09:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6ceb5297-79c0-3516-96ee-9058cafb652d | -11.65716 | -52.25604 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 15a12862-40df-3ae7-8b0a-4b08818bf1b3 | -11.09468 | -44.66135 | 2025-09-02 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c958cfad-04d7-386f-88a2-40a4e61db5a7 | -17.61381 | -46.66147 | 2025-09-02 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0a26415e-9937-3234-b7d7-e6922ed9e85b | -13.28263 | -46.8959 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 3fe78835-33b0-370a-bf78-cac83c80d784 | -14.60393 | -48.04983 | 2025-09-02 00:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8e5c92d5-3a6b-37e7-a302-58293ccb84c7 | -11.28096 | -43.64704 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cdba7bc6-9ea6-37c9-90be-16b117b81fd3 | -12.7648 | -47.66881 | 2025-09-02 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e5be7f83-12bd-3f39-a8d2-dc4a4ea14959 | -12.77302 | -47.67408 | 2025-09-02 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 2bff9f25-99cd-3db0-93c2-f272a0086d3c | -13.30842 | -46.83554 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 47c7003b-80ca-3a42-91d2-e14ec399d807 | -11.90117 | -44.88092 | 2025-09-02 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 52161b38-3f9a-30d8-80e1-ce7c9263a115 | -11.37578 | -43.59829 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 06f04889-ad53-359c-8e9d-6f3080352db1 | -14.79014 | -48.20559 | 2025-09-02 00:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c69ca2c0-8f6f-3d51-ab22-9588ed75a0af | -11.37073 | -43.56044 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a8507752-ec42-3cc5-9378-d9c69769b116 | -11.31093 | -43.59427 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| fb35dea7-4c5a-3e3c-b911-d28cb558a979 | -11.66265 | -52.18231 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1874.3 |
| 16efa3af-4468-3cc4-8e68-77c4048ef394 | -15.80398 | -43.57434 | 2025-09-02 00:09:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b414091f-8395-3ad0-bb5c-09cf855cdc06 | -11.68419 | -52.22014 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 48a191b6-e3cb-370c-b8cc-131e61b47160 | -14.73946 | -46.74837 | 2025-09-02 00:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ad306e21-e608-36cf-a72e-f9d81d802957 | -12.46466 | -43.20809 | 2025-09-02 00:09:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d7d4b590-d64f-3dfb-85f5-4083dde1fd26 | -13.50025 | -46.98788 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b1641d54-953b-322d-a6f5-884883ce27f3 | -13.75504 | -43.7762 | 2025-09-02 00:09:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 24764049-4995-3f0d-9501-545e6a3e0add | -11.80219 | -46.40851 | 2025-09-02 00:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 968a9cbb-2e23-3335-975f-1e48bf19e72b | -11.14055 | -46.34184 | 2025-09-02 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1f4a7f78-3472-35ab-a368-8ccdd4b61eb7 | -11.64898 | -52.17711 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 409.6 |
| 4cbaf2cc-5f1e-3fc3-aba2-3fbb0f40a569 | -15.57561 | -48.3587 | 2025-09-02 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ca3a5c8a-58e2-3e52-81b0-9f117cdb1662 | -11.28898 | -43.56844 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6c4e7388-db6c-3f56-9204-ab175abb11cf | -17.88723 | -47.15308 | 2025-09-02 00:09:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| d251ac56-1962-31c3-bb45-2190ff20b0de | -15.44184 | -43.32141 | 2025-09-02 00:09:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 4e8dc579-b496-374f-8f8b-e811dd453a74 | -15.55972 | -48.33805 | 2025-09-02 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 13a76db5-ebf1-3ae6-950d-7b31e57b8e65 | -12.77216 | -48.08918 | 2025-09-02 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| cab71e22-62a8-3ac9-ad92-e6e72f41a8ce | -15.13199 | -48.12484 | 2025-09-02 00:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 4fe7d8f1-12cb-3009-8d84-d8fd43b503b5 | -15.57289 | -48.37506 | 2025-09-02 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 15699b9d-fcfa-3352-98ea-ec4c6f4ebb14 | -15.56219 | -48.36048 | 2025-09-02 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| de5010c1-266d-3c4d-b2bd-a35fef36b1b4 | -11.38213 | -43.64596 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 64bd4fd3-b5a6-39f4-b0d6-4a3a287fd3d2 | -15.43118 | -43.31252 | 2025-09-02 00:09:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 855d8c9b-a8f5-38f6-ac35-2c0343313ac1 | -11.79137 | -46.41006 | 2025-09-02 00:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2d81c087-8dcd-371e-be37-0a3009f53966 | -11.80485 | -46.40232 | 2025-09-02 00:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 66fc9694-684b-3ac3-962e-8eb914368763 | -11.97555 | -45.86617 | 2025-09-02 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 39.3 |
| c2411c87-fc8b-3474-b81e-3418344eec2a | -11.0933 | -44.65091 | 2025-09-02 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 67e8109e-11d2-3479-910f-d1604ce4f0d9 | -11.35789 | -43.53334 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| db5523ce-5afb-314e-b908-0bed293ba3cb | -14.27367 | -45.26453 | 2025-09-02 00:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| a3efeda3-5c2d-37ed-84a6-116cbc6d4913 | -11.11092 | -44.63773 | 2025-09-02 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2599ce99-ea1e-3fc1-9fe1-ada911444f0f | -14.27209 | -45.25183 | 2025-09-02 00:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 2a8fbfdc-b241-3f04-a561-fb24a36d520a | -16.07641 | -43.62688 | 2025-09-02 00:09:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f6fa3cf8-0924-3564-ba1c-45378c25b9fa | -11.3834 | -43.65556 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 83ce66a8-96a6-3f0f-8dc2-6151de3efbde | -15.44049 | -43.31122 | 2025-09-02 00:09:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 20.3 |
| dfefc3cb-fb51-302c-baba-158a93cc7705 | -11.10952 | -44.62725 | 2025-09-02 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 54a6c037-4b4c-3298-bb9a-7760105bd4f8 | -12.74896 | -44.40508 | 2025-09-02 00:09:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d1ac3feb-46ba-3c4e-96c2-0e94af18834a | -13.32248 | -46.83936 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5f599e0f-3af1-3403-b2c8-05f260484678 | -12.77698 | -47.66724 | 2025-09-02 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 3d215e5f-8e51-32ec-951b-ad7f1931e8f6 | -15.57815 | -48.38147 | 2025-09-02 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 7d4be455-ac86-3022-b343-4a2f054dced4 | -11.38868 | -43.62559 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9d7cbae8-c326-33b7-9bad-9686afb63592 | -15.66537 | -48.22632 | 2025-09-02 00:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 737302ed-0219-301e-a32b-3df15ecee143 | -14.21462 | -48.06182 | 2025-09-02 00:09:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 50273dd1-cdbc-3158-8547-029d8a1b3187 | -11.39185 | -46.86567 | 2025-09-02 00:09:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README3.md)
