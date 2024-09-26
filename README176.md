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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fc8c7ee-fd41-398e-8eb1-16a881bd3b43 | -12.8852 | -51.269 | 2024-09-26 11:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e5d259c1-3a37-30dc-b192-24748b439dab | -13.1963 | -45.6308 | 2024-09-26 11:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7e240085-0353-3b54-beec-c4f801480865 | -13.2152 | -45.6507 | 2024-09-26 11:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 5b39c1f3-767d-3e12-9976-3f9d4b86374f | -13.1958 | -45.6539 | 2024-09-26 11:36:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 9350cba5-d767-3571-8d70-04a8b650c863 | -14.1582 | -47.816 | 2024-09-26 11:36:26 | GOES-16 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 78288380-cd92-384b-9437-415ad62686b1 | -18.9102 | -49.1674 | 2024-09-26 11:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 168.7 |
| edf8c727-b83d-3b11-8cfa-cc2e0b96b663 | -18.9096 | -49.1902 | 2024-09-26 11:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 283.5 |
| 9ec65d06-d9ae-3014-903c-bb31a9f389a5 | -10.032 | -53.5065 | 2024-09-26 11:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 180.3 |
| b0254f5b-6887-3765-a45d-1612cc3ef463 | -11.7179 | -47.8551 | 2024-09-26 11:46:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 960c709f-b0f2-3f51-bf21-2fbded55917e | -12.2367 | -45.5045 | 2024-09-26 11:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 7ab44b06-3d46-327c-ac0b-83099559ce3e | -12.2179 | -45.4844 | 2024-09-26 11:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| ce940f95-1464-386b-94f3-5d473807619a | -12.4612 | -47.9774 | 2024-09-26 11:46:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 3cbdc211-6968-38d5-84d4-182e906b2abb | -12.8657 | -51.2927 | 2024-09-26 11:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 46954215-84fe-36e8-84b0-75f2553845ed | -12.8852 | -51.269 | 2024-09-26 11:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 3342d1f4-c0ce-3baf-9884-6c1f23ea81aa | -12.866 | -51.2714 | 2024-09-26 11:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 81ef27e6-583f-3e0c-8eeb-6990536192db | -12.9525 | -45.2778 | 2024-09-26 11:46:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2b6bb075-8780-3f66-99c5-d767ad0f9066 | -12.9714 | -45.2979 | 2024-09-26 11:46:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 73132ed5-36cf-369a-86fd-a992cc617548 | -12.9718 | -45.2747 | 2024-09-26 11:46:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| dacc6d17-4f8a-39a1-ae67-3cf343749a0a | -12.952 | -45.301 | 2024-09-26 11:46:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| c7f4247e-d382-3d92-8a21-cb811ae55b52 | -13.1958 | -45.6539 | 2024-09-26 11:46:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 015c2901-012a-3179-abc7-05a67696536b | -13.2152 | -45.6507 | 2024-09-26 11:46:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 43488ee6-f828-3aa7-999f-df7aa679f168 | -14.1582 | -47.816 | 2024-09-26 11:46:26 | GOES-16 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 245a2dca-7ad4-3594-a151-57568e291ba9 | -18.9102 | -49.1674 | 2024-09-26 11:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 317.3 |
| c1222c19-c5de-36f3-b370-d4764beb34bd | -18.8901 | -49.1715 | 2024-09-26 11:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.2 |
| b13b7d99-d341-30d8-8ca7-739949c26673 | -8.8293 | -63.699 | 2024-09-26 11:55:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 5f86733f-1e4f-3007-8c36-9be28d11eec1 | -10.032 | -53.5065 | 2024-09-26 11:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 79339553-90a7-319c-a278-d028de81dbd0 | -10.8161 | -45.8868 | 2024-09-26 11:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 4ad29ec8-5ac6-3e17-a730-58adf8052f63 | -10.8348 | -45.907 | 2024-09-26 11:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| ca4f3dae-2805-318b-a8c2-695cff750b29 | -10.797 | -45.8893 | 2024-09-26 11:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| bf32fd9b-4f74-3c97-9d6d-6a08e8e11000 | -10.8352 | -45.8843 | 2024-09-26 11:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 1de2eec9-e350-3bec-8fb3-fe0cdfda6317 | -11.2224 | -45.5131 | 2024-09-26 11:56:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| f8b7160f-742b-3761-b007-b4322ea934e4 | -11.7179 | -47.8551 | 2024-09-26 11:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| bab2a0f6-6284-3bc7-b570-a6fe96cfdf56 | -11.6988 | -47.8576 | 2024-09-26 11:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| d6e1a1e7-4806-361f-b14b-571f0e1268a8 | -12.2367 | -45.5045 | 2024-09-26 11:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 8ef4bf56-01ad-337f-a456-7d83504ba831 | -12.2179 | -45.4844 | 2024-09-26 11:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 1afc3ab0-eb3c-3c63-854a-19446a8b8abe | -12.5026 | -48.9198 | 2024-09-26 11:56:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3a9b3cc3-28b0-3007-a7d4-a00999b6db1c | -12.4835 | -48.9224 | 2024-09-26 11:56:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e2a7c24e-169b-3379-87f5-2b2e62d106ba | -12.4612 | -47.9774 | 2024-09-26 11:56:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| f69911b9-a8a8-34ea-a481-ecb37f1ce24c | -12.5464 | -53.5147 | 2024-09-26 11:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 42734eee-a52a-3c6d-a57f-a99bc141bdd3 | -12.952 | -45.301 | 2024-09-26 11:56:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 596fc392-0f5f-3f37-9762-4a59107a5562 | -12.9718 | -45.2747 | 2024-09-26 11:56:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| dffeca3d-178d-3764-9326-e117de5a36e9 | -12.9714 | -45.2979 | 2024-09-26 11:56:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| d95c50a6-67b5-30a8-b6c6-257791f47d32 | -13.1958 | -45.6539 | 2024-09-26 11:56:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 26a6485c-1c77-3d51-b3de-accc24d46387 | -13.2152 | -45.6507 | 2024-09-26 11:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 201.2 |
| a7cf6448-597f-3bc0-94c6-f745f98ff73e | -17.8851 | -47.0217 | 2024-09-26 11:56:46 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 85d0963b-03bd-393c-8e29-8dd7bce7d6a1 | -18.9102 | -49.1674 | 2024-09-26 11:56:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 214.6 |
| f1705680-d5a3-3172-b4f7-2c6297fddb24 | -18.91 | -49.19 | 2024-09-26 12:03:36 | MSG-03 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8360b77-2698-3572-bd61-ca0d2ee2ba9c | -13.23 | -45.7 | 2024-09-26 12:04:07 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 967246e6-6555-3bbe-96a4-b722c405c16f | -10.65 | -45.91 | 2024-09-26 12:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e011ff6-37a2-3003-921a-db72dea507e1 | -10.83 | -45.95 | 2024-09-26 12:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4570c25-4484-3813-8c76-7782677c43f7 | -10.83 | -45.9 | 2024-09-26 12:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c5d95e3-e2a2-340a-af74-3a758eb35c22 | -10.04 | -53.48 | 2024-09-26 12:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53e46f33-47a1-344e-97ec-d9de1c2bc4b2 | -8.81 | -44.98 | 2024-09-26 12:04:34 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 44b47731-6f92-3254-813d-c29dcea88ac0 | -8.84 | -44.99 | 2024-09-26 12:04:34 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 96b2e3b9-e1f6-3679-aaf9-0808bc933ef1 | -10.032 | -53.5065 | 2024-09-26 12:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 224.7 |
| 20d22cd0-fc71-33f0-9e8c-1cdbe49bfd5d | -10.7981 | -45.8209 | 2024-09-26 12:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| af401ca1-54c2-3049-8dcc-d121578a30e1 | -11.2224 | -45.5131 | 2024-09-26 12:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| df1f9dca-913f-34a4-8fab-76ae6196a002 | -11.222 | -45.536 | 2024-09-26 12:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| bf3a78ae-88a6-3659-9d3e-048cd473c464 | -11.7179 | -47.8551 | 2024-09-26 12:06:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 27c42d5c-1f1e-375e-9106-e60efe90785c | -11.6988 | -47.8576 | 2024-09-26 12:06:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| bd8d0308-7fae-31b4-8c8d-9d526fe5674d | -11.6985 | -47.8798 | 2024-09-26 12:06:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ac3a609d-f38a-37d6-8615-a37ca2f0a3f1 | -12.2367 | -45.5045 | 2024-09-26 12:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 7eda752b-9e34-3e52-967d-363c007b7833 | -12.2179 | -45.4844 | 2024-09-26 12:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 300.7 |
| bacab8cd-5c6c-3e95-b78a-c2289cc0e01b | -12.4612 | -47.9774 | 2024-09-26 12:06:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| a10313bf-add9-3ac8-8b27-5402c362ac1f | -12.5026 | -48.9198 | 2024-09-26 12:06:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 6482a171-1851-3d5b-b5e9-df8c46b88edc | -12.4835 | -48.9224 | 2024-09-26 12:06:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| c4f857af-eb45-3c58-ad64-9ef124bd4da8 | -12.8102 | -51.1716 | 2024-09-26 12:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a1fa835c-3512-3e97-85c3-ec0d6f318994 | -12.7911 | -51.1739 | 2024-09-26 12:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 691936a5-df85-3349-ad87-f63adfb4f5a4 | -12.7914 | -51.1525 | 2024-09-26 12:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 66886d51-7148-3def-a206-4de94617a88b | -12.9714 | -45.2979 | 2024-09-26 12:06:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 89ba2032-c057-39f8-b1ad-8244fa1494cf | -12.8106 | -51.1502 | 2024-09-26 12:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9309598e-3afa-335f-a934-82ca1ece4ec1 | -13.1963 | -45.6308 | 2024-09-26 12:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 80529365-e911-3880-9b3f-ac670a47e36c | -17.8851 | -47.0217 | 2024-09-26 12:06:46 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 30481202-1583-3bbf-b60e-ba04eddf90b7 | -18.9102 | -49.1674 | 2024-09-26 12:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 236.4 |
| 6428013d-b67e-3da9-b4cc-337518303e70 | -18.8901 | -49.1715 | 2024-09-26 12:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| deba9610-9aa9-3c74-9410-4305493ba1ca | -20.7971 | -48.9496 | 2024-09-26 12:07:01 | GOES-16 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 158.6 |
| fe453d2a-678e-3c28-858a-7ad9aa85fa3d | -21.2733 | -51.0061 | 2024-09-26 12:07:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 196.1 |
| 129f2caa-2c92-3ee4-b159-edf8c1ec4155 | -7.2906 | -61.0869 | 2024-09-26 12:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| a94b58ee-9252-3b18-9a5d-7d129c48d03c | -8.6722 | -38.149 | 2024-09-26 12:15:55 | GOES-16 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 244d8be3-7496-3acd-a367-23221fff3c52 | -8.839 | -44.9628 | 2024-09-26 12:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 193.2 |
| d308a787-fd82-3df7-8cd8-fcec4d9135d6 | -9.4165 | -51.4846 | 2024-09-26 12:16:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 49edba86-2581-37a2-8135-ca22c61f6ea0 | -9.398 | -51.4652 | 2024-09-26 12:16:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| ec755a6f-a876-39e0-b333-556a024b77a1 | -10.0134 | -53.4875 | 2024-09-26 12:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 782630fa-599b-3a77-86ae-99bf12e01c11 | -10.032 | -53.5065 | 2024-09-26 12:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 169.0 |
| 7d5a07e4-ccdc-3fd1-9a14-6b715f8b4d1b | -10.0136 | -53.467 | 2024-09-26 12:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4c399abf-9613-3819-b42d-c618ba65df68 | -11.1354 | -46.1623 | 2024-09-26 12:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 32c69da8-4b4a-3545-bf42-fcdc991c3623 | -11.1351 | -46.185 | 2024-09-26 12:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| d4b82d5e-ec80-3a86-96fb-a76f0d374c4f | -11.7179 | -47.8551 | 2024-09-26 12:16:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 0cde25aa-8ed7-3212-b0d1-ba43a4eada98 | -11.9369 | -47.3143 | 2024-09-26 12:16:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8afe22e4-bd58-361b-a680-64716c291a6b | -11.9365 | -47.3367 | 2024-09-26 12:16:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| ba2ddf4a-d5db-35a4-b9ca-89242cba2ac5 | -12.2367 | -45.5045 | 2024-09-26 12:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 330.4 |
| d8babf1e-9227-3550-99cd-d1980b5153e2 | -12.2179 | -45.4844 | 2024-09-26 12:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 292.0 |
| 27d33074-33ea-3cff-9735-c06c3ff3310f | -12.4612 | -47.9774 | 2024-09-26 12:16:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 64cdf550-5622-3a80-9f74-c56ffe95b753 | -12.4835 | -48.9224 | 2024-09-26 12:16:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 7c72eb17-2373-3e17-9574-a9929ee41b1b | -12.5026 | -48.9198 | 2024-09-26 12:16:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 189.8 |
| eda0ff3c-bc0f-3251-b71f-6a82f4d93849 | -12.5464 | -53.5147 | 2024-09-26 12:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 159.1 |
| f4d0f836-9653-30aa-8868-3f6c39cfb157 | -12.9714 | -45.2979 | 2024-09-26 12:16:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d9f9c4ff-a10c-3c49-80ab-2430db39e9f5 | -13.1963 | -45.6308 | 2024-09-26 12:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 4384a3cd-1c5e-3c05-b08a-ce426d3d0040 | -14.8828 | -51.4777 | 2024-09-26 12:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| f3b95f6e-e5a2-3d8f-a976-c63282ee5668 | -17.8851 | -47.0217 | 2024-09-26 12:16:46 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |


[Clique aqui para ver as próximas entradas](README177.md)
