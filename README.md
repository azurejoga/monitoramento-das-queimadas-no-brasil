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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be6cb229-9107-385b-945c-03db8314acfc | -10.4889 | -44.9235 | 2025-12-27 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d2db4a65-3a11-3008-bddc-8d177b819142 | -3.0029 | -40.3307 | 2025-12-27 00:00:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 3048c106-2b8c-3ade-b007-6d822cacedc2 | -12.4719 | -43.523499 | 2025-12-27 00:08:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41b2697a-7556-3812-8709-053d639ce261 | -20.4921 | -43.649101 | 2025-12-27 00:08:00 | METOP-B | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77609836-0ea6-319d-a938-1b595052aad8 | -10.4894 | -44.934601 | 2025-12-27 00:08:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4256b121-81e8-3064-919e-d9caf7621a86 | -18.8302 | -43.4646 | 2025-12-27 00:08:00 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 007ec6b1-98e1-3135-8ca8-d5ce918fc35f | 1.8245 | -60.876202 | 2025-12-27 00:08:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f5b8ad09-625f-3c5c-a049-65cd9bb707ad | -3.0056 | -40.375099 | 2025-12-27 00:08:00 | METOP-B | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1f6f3b6e-fa1a-3a4c-8b07-33cb520daef8 | -17.982599 | -47.887299 | 2025-12-27 00:08:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 62c12743-2907-3ae2-bce4-328bbcf8fde0 | -3.0752 | -50.352299 | 2025-12-27 00:08:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e4b1b74-dd4d-3a27-981a-93b7f5d56764 | -6.5536 | -43.108898 | 2025-12-27 00:08:00 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ddd216f-79b5-3ced-a834-dc04b959d7e8 | -12.6711 | -46.777401 | 2025-12-27 00:08:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e763f0ef-aa05-3e2f-9d19-7ef168098529 | -3.759 | -49.7313 | 2025-12-27 00:08:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c307b3f7-242e-3500-9b54-5efb374fce60 | -12.6727 | -46.7845 | 2025-12-27 00:08:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a463a5d-2e5c-379e-91cf-09a68c1db0e1 | -15.7438 | -41.899502 | 2025-12-27 00:08:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa7a1f86-c652-366e-b956-9b607f3c9d6a | -18.832001 | -43.472198 | 2025-12-27 00:08:00 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c92f6bda-db22-3ba0-bc4b-da6f8a8378f3 | -12.304 | -44.349701 | 2025-12-27 00:08:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba0e6394-0810-3b71-9d2e-46f7b87ebce6 | -12.7276 | -47.731499 | 2025-12-27 00:08:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4cdb786-84ea-3685-9825-c09dcfdff58d | -3.6546 | -43.523399 | 2025-12-27 00:08:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da75de29-bd93-310a-9953-f7e08f2e9368 | -21.0867 | -42.0951 | 2025-12-27 00:08:00 | METOP-B | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04f652d7-4725-3340-9ec1-c3d45a0eb243 | -12.6614 | -46.779701 | 2025-12-27 00:08:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53c91f8e-9d88-398f-a4ad-2243705ad625 | -10.9479 | -49.4175 | 2025-12-27 00:08:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71897e39-d75e-3927-9d51-9d566b05742f | -13.5211 | -43.681301 | 2025-12-27 00:08:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2214dc77-01dd-3ef2-a3d5-ed312c044a6b | -0.0943 | -51.287201 | 2025-12-27 00:08:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 33b0df8e-190f-3b04-a810-5d426b65fc97 | -3.2045 | -45.5345 | 2025-12-27 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18b6407b-4f75-30f6-9c91-12f00fd32988 | -2.8985 | -52.590302 | 2025-12-27 00:08:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fdd8d0d-8b47-3ef4-9bf6-1ff1c82b3869 | -15.6616 | -43.118301 | 2025-12-27 00:08:00 | METOP-B | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e407be3a-7ec9-3e82-823a-f4c590d83cb4 | -10.4975 | -44.924702 | 2025-12-27 00:08:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8873d5c7-2f75-3838-b874-aab8d64d7c90 | -11.8507 | -43.735699 | 2025-12-27 00:08:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 67c2134a-bf93-341d-b438-581569916800 | -10.4992 | -44.932301 | 2025-12-27 00:08:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ba1ed0a-d991-3bc9-bf13-13788796020d | -10.2457 | -36.3904 | 2025-12-27 00:08:00 | METOP-B | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3e70286d-cd88-37a4-b040-2480837d06bf | -20.969999 | -48.6278 | 2025-12-27 00:08:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba72000f-d93e-3ea7-9637-09332d7c4c6f | -3.6039 | -49.3638 | 2025-12-27 00:08:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47c98d8d-7ec8-3583-a6d8-8d47577d3013 | -19.203501 | -48.156101 | 2025-12-27 00:08:00 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4331969b-f3c6-3359-b577-12220134e01b | -15.8993 | -43.339199 | 2025-12-27 00:08:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 747351bb-63c7-3cd9-8272-8172165269d1 | -10.5483 | -48.7141 | 2025-12-27 00:08:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb9d0c77-314a-36e3-98cf-f3757ed446f1 | -15.7416 | -41.890301 | 2025-12-27 00:08:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| daaad126-8618-3e59-b298-b814d9cd0478 | -11.6365 | -49.423199 | 2025-12-27 00:08:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 773ee06e-0ffd-31da-92f6-36059dd751f3 | -6.5438 | -43.111198 | 2025-12-27 00:08:00 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a18a1f3-dcc2-37c9-8c74-5139894a43d8 | -2.9916 | -40.359699 | 2025-12-27 00:08:00 | METOP-B | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2dd07361-500c-38c6-9228-425db3a210d2 | -3.7574 | -49.724201 | 2025-12-27 00:08:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3113989b-3322-3025-aa03-ddd4ce63b4d9 | -10.9496 | -49.425301 | 2025-12-27 00:08:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd8d7ff3-e995-3fa6-b8ba-c4f4c5dcca85 | -3.3218 | -45.9995 | 2025-12-27 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b63ccdf7-3450-355f-a139-3c5b2cd4a649 | -10.7671 | -45.02 | 2025-12-27 00:08:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 72865fef-6872-3002-b6d8-4cd2e9b7c4b3 | -10.7769 | -45.0177 | 2025-12-27 00:08:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 753e03df-93a6-35aa-8bf0-efdc07dd165e | -2.453 | -47.7878 | 2025-12-27 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5367e74-1d07-36aa-a914-eb00730f69a9 | -10.3666 | -45.161598 | 2025-12-27 00:08:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8d8d6ea9-9212-3e49-9945-4c3f250e920a | -9.8325 | -49.151699 | 2025-12-27 00:08:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e28534f6-a924-3222-bcac-3ed1c18823e1 | -10.4877 | -44.926998 | 2025-12-27 00:08:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d0d15d00-fcf8-37d9-88be-33c274f1061e | -2.3762 | -51.911098 | 2025-12-27 00:08:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ebf5437-a75e-31b3-bd9c-8bc1ae518177 | -15.8731 | -40.9422 | 2025-12-27 00:08:00 | METOP-B | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 037d7ed4-9b41-3a30-b068-213c11fe90bb | -14.4444 | -44.861401 | 2025-12-27 00:08:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 061d8515-8d35-39be-b6a2-6b07e4525c12 | -3.2064 | -45.542801 | 2025-12-27 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa2d7068-2f7e-3c05-8e11-40c2a968efab | -17.8036 | -40.1203 | 2025-12-27 00:08:00 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 980dec8b-21b0-38b8-9e57-5a4ffdaa1175 | -3.2083 | -45.550999 | 2025-12-27 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7b8f9fe-4cec-3ea2-8961-ab8ebdfc0b92 | -12.5127 | -43.6964 | 2025-12-27 00:08:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ff3fce3-45e9-3ecc-8e1b-86f0a78c1262 | -2.4514 | -47.7808 | 2025-12-27 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4afb48d5-8225-377a-afa4-34938b20d8f9 | -22.182699 | -43.139198 | 2025-12-27 00:08:00 | METOP-B | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1b3d6f8-9b5e-3d84-a142-8b71978cbf2d | -12.5107 | -43.688202 | 2025-12-27 00:08:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ecaa47ad-fe58-3b7a-85d3-567e49809216 | -0.0927 | -51.2799 | 2025-12-27 00:08:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| baa84475-54e1-3ed2-a6af-1b0e0c9359cf | -3.1894 | -50.402699 | 2025-12-27 00:08:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a01db14f-342e-3016-932b-d86e3fb8c7df | -20.4937 | -43.656601 | 2025-12-27 00:08:00 | METOP-B | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 799570aa-7351-3d83-a0db-c789abb8f1a6 | -20.971901 | -48.637402 | 2025-12-27 00:08:00 | METOP-B | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b4bdcf4-5f33-3973-b085-7553ca83eccb | -3.6521 | -43.512798 | 2025-12-27 00:08:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03b28f85-5045-307f-ab80-d925a7f38ff4 | -5.4828 | -46.838402 | 2025-12-27 00:08:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a66af04a-90d1-3b59-990e-7fa818dc1bbe | -15.2733 | -43.180801 | 2025-12-27 00:08:00 | METOP-B | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 8990f0b5-6e19-3ad7-84b6-dd08b8ec9b71 | -10.3683 | -45.168999 | 2025-12-27 00:08:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a6dc4af-d655-389c-af66-18380f3fd703 | -4.8923 | -40.4631 | 2025-12-27 00:08:00 | METOP-B | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e4830992-2ece-37b7-abbb-fa261723e4a6 | -2.4628 | -47.785599 | 2025-12-27 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f16dd9c0-d6bc-3b83-9ee6-dc9f07a6a13e | -22.315901 | -43.088799 | 2025-12-27 00:08:00 | METOP-B | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 630d1e1e-246f-33b7-bb71-ba0cb90dbb08 | -2.6973 | -51.646198 | 2025-12-27 00:08:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83624f63-794d-3ece-9ca8-31f187c25a97 | -11.8527 | -43.7439 | 2025-12-27 00:08:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ae93219-c3d8-315e-9a91-81777d0dd7f8 | -21.722 | -47.113499 | 2025-12-27 00:08:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ba264bff-be7a-3c7b-af88-0570bbcfac05 | -15.9091 | -43.3368 | 2025-12-27 00:08:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5ace06e5-c1be-3fd4-a6df-e039031f2330 | -13.5193 | -43.673302 | 2025-12-27 00:08:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb529d95-2c42-3b4c-9ebc-7e73aaf05352 | -20.9949 | -49.393799 | 2025-12-27 00:08:00 | METOP-B | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fbf0e762-9d61-3a76-93dd-561fd3f9726b | -6.5365 | -43.123798 | 2025-12-27 00:08:00 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a2de9ba-c823-3ae1-a341-0206096a0516 | -12.5204 | -48.383801 | 2025-12-27 00:08:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 234287ca-1551-338f-a890-fc475cc19d72 | -5.4573 | -46.187599 | 2025-12-27 00:08:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5b3499ef-e477-3cf8-8227-c0060da4cf05 | -2.9005 | -52.599201 | 2025-12-27 00:08:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae7ea3e0-53c7-3236-bdb4-2a526ca30819 | -3.2102 | -45.559299 | 2025-12-27 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96aa6584-bf50-3f03-820a-43e30339f3d2 | -4.1704 | -48.588902 | 2025-12-27 00:08:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc271b2-ff7b-33f2-bb44-7527f06e3c23 | -11.0181 | -45.258099 | 2025-12-27 00:08:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3de6423d-3fc4-3c25-80f6-52f100e4da4e | -3.1073 | -49.445099 | 2025-12-27 00:08:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9178b2fc-92ea-3035-a959-05559354d908 | -15.5282 | -49.975899 | 2025-12-27 00:08:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25d21d8a-4e75-35f5-9114-0a8e9c516509 | -15.6597 | -43.110199 | 2025-12-27 00:08:00 | METOP-B | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e0742c0f-282e-31e7-90b5-db455998382a | -10.2391 | -36.365101 | 2025-12-27 00:08:00 | METOP-B | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03002fcf-55e4-32c6-83fc-9adafb1b184d | -5.4555 | -46.180199 | 2025-12-27 00:08:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 05754917-f863-34d4-9fd4-e2a4821cdbd3 | -11.8446 | -43.797901 | 2025-12-27 00:08:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2d94450-e92c-3530-95ab-666cadb31e88 | -12.4739 | -43.531799 | 2025-12-27 00:08:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d16df4c-70f7-3bdb-9e8a-b70a13506fe6 | -19.2052 | -48.1647 | 2025-12-27 00:08:00 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a900a344-f64c-3cb3-8c83-9c6d84f394e6 | -11.3987 | -48.000401 | 2025-12-27 00:08:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 230979e6-2f45-3016-95da-e9b6b976ab95 | -3.6015 | -49.444199 | 2025-12-27 00:08:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c38e949f-5ab8-3b4c-9636-d851ff38943c | -12.5188 | -48.3764 | 2025-12-27 00:08:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| adc4b593-b170-34ad-aba3-1796f6ba97c1 | -10.8842 | -48.982101 | 2025-12-27 00:08:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe237063-1c13-33ad-a4dd-46a997c45e03 | -10.2295 | -36.367699 | 2025-12-27 00:08:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0b2515d-a90b-3415-ad0d-f619d43a407d | -20.9737 | -48.6469 | 2025-12-27 00:08:00 | METOP-B | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 384e4031-0dc4-3ffa-8a93-b21d41f69f79 | -4.6325 | -47.946098 | 2025-12-27 00:08:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf9472ce-ae44-30b2-997c-d33cf4d7312c | -1.4848 | -54.205601 | 2025-12-27 00:08:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c2a0bde-886f-3fc9-9dd1-0417f6683b05 | -15.8706 | -40.9319 | 2025-12-27 00:08:00 | METOP-B | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
