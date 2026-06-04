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
| 5f805b6e-b97a-375d-8dc7-ccf692034a51 | -14.0603 | -53.4005 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a61c88ff-0337-3f88-9f17-85a1da39d102 | -11.60354 | -55.33594 | 2026-06-04 04:10:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fe91289-d3dd-3ec9-91c3-9352e773e647 | -10.61345 | -46.6908 | 2026-06-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1fb4869-d661-3ad6-8254-28e2dc783c75 | -11.79244 | -52.5141 | 2026-06-04 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eebda91-fafd-3b97-a467-9ecc0528d823 | -10.38283 | -49.45111 | 2026-06-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 84db59a3-1761-35db-90bb-12f2d2508057 | -10.44134 | -47.95383 | 2026-06-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f21d5382-fc5c-3cef-9f1f-deb99e736437 | -15.33389 | -42.33281 | 2026-06-04 04:10:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7cddbc57-eabc-33ae-91ea-92e12dbfa94e | -11.61007 | -55.3373 | 2026-06-04 04:10:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 991f871f-0318-3571-8c05-bc922bc80a8d | -10.38743 | -49.45191 | 2026-06-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bbec1dd7-40ea-3808-a60f-eca0ce984c1c | -12.02225 | -45.86991 | 2026-06-04 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dec4869b-4e5a-361a-b888-c5635134a972 | -14.77093 | -52.67587 | 2026-06-04 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cfee09c-5842-3d00-a72d-f441910d9c3f | -11.79793 | -52.51516 | 2026-06-04 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8556ea4b-9c85-3a2e-9244-81e2799b83a7 | -11.78146 | -52.51196 | 2026-06-04 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba959e67-d804-37ce-aa17-8b1d31f08e53 | -10.39289 | -49.44787 | 2026-06-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3cbbc79b-f89f-3622-aab3-837067fe0acd | -14.36892 | -45.55073 | 2026-06-04 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dcfae88-6558-38ec-9aaa-a910ad8bd2e0 | -12.73678 | -54.20287 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 217e8b43-2b7e-309c-986a-f1044815e66e | -10.53625 | -46.61951 | 2026-06-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f389161b-a5cb-3e2a-bc1d-33d5e77b57da | -14.78675 | -50.63638 | 2026-06-04 04:10:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 493baffe-f648-3309-95db-4106dbae9f03 | -16.58267 | -45.88501 | 2026-06-04 04:10:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 780a47c8-1762-3d00-a077-96a1331fb35f | -14.06108 | -53.39661 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e4bbcca-c619-39b6-aa2f-c32fa010df77 | -11.55607 | -52.7891 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bb096e39-776e-37f5-b8ab-e256bb4c4e23 | -14.04824 | -46.34755 | 2026-06-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cb3c307-8a85-3884-853a-2f41d3062eaa | -15.33055 | -42.33226 | 2026-06-04 04:10:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 67ebea0c-6939-3a4c-ab09-6dbed34e8a7b | -10.95064 | -44.18536 | 2026-06-04 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef096d7d-200e-3ea4-8398-f28f7e5e92ce | -11.5527 | -52.78875 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6ced5e77-d1b8-39ac-8ced-3345661ad082 | -14.08089 | -53.38464 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d3efecc9-dcb0-3272-be12-04985405c8d3 | -10.60031 | -46.69849 | 2026-06-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 531a443d-66b8-3e26-9d74-278a172fe7fd | -11.62812 | -55.18391 | 2026-06-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 81248a54-7f00-357e-b079-8a0f827b8c44 | -14.78583 | -50.64135 | 2026-06-04 04:10:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d4ebe4b-d5a7-3474-957e-9eddb4e56e73 | -11.62054 | -55.18814 | 2026-06-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c190457-c021-3bd8-a7a7-12f3fdef698f | -16.58053 | -45.87664 | 2026-06-04 04:10:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98158a48-4e3a-3383-8d6b-c4d583d6b449 | -10.5651 | -46.63473 | 2026-06-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8d15b216-31df-3aa2-b890-d1ed652886ef | -15.4363 | -46.33231 | 2026-06-04 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a62285a8-51b4-3395-b2da-c8b7c7f47578 | -16.57989 | -45.88052 | 2026-06-04 04:10:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94b67608-1472-3f07-9b8c-d90f7f927d7e | -14.37001 | -45.55096 | 2026-06-04 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f5c2718-49bf-3a1c-b8ed-6e0d54e53995 | -11.55684 | -52.78522 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 622d3d8f-1351-3670-b3bd-887f9baa1557 | -10.3837 | -49.44626 | 2026-06-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 056fe846-3253-3f82-b33c-95f1a66dde9d | -14.7768 | -52.67378 | 2026-06-04 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fe5fb1b-f978-31aa-857b-20123161cabe | -10.25627 | -48.34346 | 2026-06-04 04:10:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d7ff96a-f58b-3ac8-b27a-a6048b0fbcca | -15.3328 | -42.34005 | 2026-06-04 04:10:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 635d85df-d9d8-3df2-9900-7f5f095e3c07 | -11.54071 | -52.79061 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 126ea2af-54e1-36f7-bcf7-16301f9bd1bd | -11.55196 | -52.79264 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 97868d85-65c2-3a7d-89dd-5b97fe378490 | -14.08011 | -53.38848 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dc93e682-909c-338d-a7d0-679dcafc7cd8 | -15.32946 | -42.3395 | 2026-06-04 04:10:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4c9762ce-dcf3-3933-9411-06e5578d31b1 | -11.7573 | -47.07836 | 2026-06-04 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d716f23-90d5-39f3-9fa7-d663a8abea7e | -15.33 | -42.33588 | 2026-06-04 04:10:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3c684be2-e13d-3bb6-8d74-6a34cc7486a5 | -11.38877 | -47.82439 | 2026-06-04 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9019e27-3ec7-3168-a673-99b986ac6cf9 | -11.75814 | -47.07347 | 2026-06-04 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27d14f2a-f02d-3480-8c8a-0dbce02a9fd9 | -13.95949 | -46.1856 | 2026-06-04 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c35e0b13-fcfb-31b0-acd8-4451ce1edb2b | -9.89132 | -52.44128 | 2026-06-04 04:10:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ece3da7-961c-35bf-aa47-ca8f597d6f71 | -11.76116 | -47.07898 | 2026-06-04 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46e4b4a4-0148-3222-8ad1-441c649593ec | -10.98025 | -45.09762 | 2026-06-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f0fe1dc-9d7a-3847-a3ff-8c8f4c839c01 | -11.5718 | -48.14143 | 2026-06-04 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f018748-77c9-3f83-9467-d80e53c4205d | -11.01423 | -47.47556 | 2026-06-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 630ab061-dcc2-339c-afec-80bea3139e90 | -12.73585 | -54.2075 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 906a5c62-05c0-3038-b6b2-7b1a9f8cc152 | -13.19682 | -43.35689 | 2026-06-04 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eafba2b4-dd67-3509-ae31-08eafa8ecfad | -16.58331 | -45.88112 | 2026-06-04 04:10:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35c2ffbe-b1b5-3dc8-a35c-08f61bae40f0 | -17.96733 | -44.35365 | 2026-06-04 04:10:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8aeab683-97bc-3aef-82b3-924c8b555211 | -13.51149 | -54.31504 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5cde49d4-714c-3ff1-b8d5-1b3a6b55d71b | -18.46383 | -54.70859 | 2026-06-04 04:12:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bceabca1-52ea-3c3a-a7a0-174a6f3d75e8 | -17.46191 | -55.19931 | 2026-06-04 04:12:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 0c30e0a6-0438-353c-8968-41759fac6d8b | -21.49786 | -48.77889 | 2026-06-04 04:12:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2be6bc33-cbac-3e06-93ad-96d44ae5ee0e | -19.74036 | -53.54892 | 2026-06-04 04:12:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84c56caa-92ea-3271-9ed2-925bc0cd1b4e | -19.7397 | -53.55209 | 2026-06-04 04:12:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5b370c5-86ad-31aa-b7e4-922fbece65e0 | -23.51118 | -50.04442 | 2026-06-04 04:12:00 | NOAA-21 | GUAPIRAMA | PARANÁ | Brasil | 4109005 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 70183d62-b769-3615-97c6-a30d0f981f16 | -16.59115 | -58.24052 | 2026-06-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e83a3e90-b939-3e02-890a-308538f8ba2d | -22.29993 | -46.38256 | 2026-06-04 04:12:00 | NOAA-21 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 450fab1e-8143-38ed-ba95-fa1fc44a4ead | -20.02403 | -48.19233 | 2026-06-04 04:12:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c023ffd-bc7a-3fb3-904f-08de05a9d80e | -19.98797 | -45.4933 | 2026-06-04 04:12:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b58796b-3fe9-3ffc-bf79-e16f08c7b2dd | -19.12325 | -49.7612 | 2026-06-04 04:12:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b73e6e67-364c-3df9-9738-7596141b9e12 | -22.76418 | -43.27613 | 2026-06-04 04:12:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9bc83687-096e-38b2-8615-08eb980fda37 | -20.55557 | -46.36191 | 2026-06-04 04:12:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ae7ea81-d54a-3e68-94ef-525da1f42d36 | -22.97171 | -52.69229 | 2026-06-04 04:12:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 27230f5f-b19e-3704-8d78-5cf1987e6032 | -19.12727 | -49.76204 | 2026-06-04 04:12:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 855c244a-221a-326f-9d6e-e9a7b9a4403f | -21.55319 | -49.86772 | 2026-06-04 04:12:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 072901f2-3324-3788-b6c3-bf4d885b3805 | -18.46465 | -54.70478 | 2026-06-04 04:12:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c42b11f-ccf7-3d36-a0e7-49edb939658f | -19.88654 | -44.76255 | 2026-06-04 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50088e25-3f33-3f4b-8d14-394643a5daf4 | -19.96426 | -47.20579 | 2026-06-04 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef762f77-e39c-3399-b9c3-1a8844678fd4 | -18.23689 | -54.5947 | 2026-06-04 04:12:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a3e409e-372d-3327-8149-d3e18e012a59 | -17.46289 | -55.19484 | 2026-06-04 04:12:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ef101ef1-9e4a-3e25-b1c1-45626ec4f6c8 | -20.02485 | -48.18777 | 2026-06-04 04:12:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da89aa1f-7b1b-3527-b35e-8f336a05ca15 | -19.59015 | -45.21445 | 2026-06-04 04:12:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 63b4f32c-f1b5-335c-9214-1f03bf4c3d94 | -19.72711 | -54.65154 | 2026-06-04 04:12:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfe9efac-e35c-3482-bcff-d253e30c1598 | -16.44051 | -57.27069 | 2026-06-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9197d8b5-190e-35a5-898c-f9fa041b0f9d | -20.0245 | -48.18961 | 2026-06-04 04:12:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e0d1c457-daa9-3181-9978-f9a25471c742 | -16.60351 | -58.25117 | 2026-06-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8f194fb9-f946-3c1f-a77a-30fa773e22eb | -23.04107 | -47.88058 | 2026-06-04 04:12:00 | NOAA-21 | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 477fbdd7-08ff-352e-acbb-b2bd6557c5b7 | -21.65158 | -44.38797 | 2026-06-04 04:12:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 20307385-18a7-31c9-8f64-61b53e6713aa | -23.54546 | -47.63418 | 2026-06-04 04:12:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c91f1b7c-ddd3-3bb7-994d-a2160cf148c2 | -17.46268 | -55.20165 | 2026-06-04 04:12:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 6341ae85-aa51-3e02-abb3-07bfc2187bc4 | -20.02735 | -48.19489 | 2026-06-04 04:12:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e5b8d60-f4de-3dd5-b1d6-1bb0c92606dd | -19.79056 | -50.96379 | 2026-06-04 04:12:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7ec89b34-4d46-3ffb-92a2-8d4499e13899 | -18.39799 | -51.45669 | 2026-06-04 04:12:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2efc75a-b93d-3390-b112-39bee16399a5 | -21.5527 | -48.59923 | 2026-06-04 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 54962842-a983-3387-91bb-adeb1a010e08 | -17.46362 | -55.1972 | 2026-06-04 04:12:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 8f67d903-26b5-394a-ba6c-3ecfac7f2b93 | -19.17042 | -55.18687 | 2026-06-04 04:12:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4bb14408-13ef-3771-ba95-1406859847e7 | -21.55351 | -48.59468 | 2026-06-04 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7096cad3-40c2-31ce-badd-6664dd63f826 | -25.27153 | -50.65397 | 2026-06-04 04:14:00 | NOAA-21 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f0ddb775-4ec7-3f1b-b41e-9738a34d9dda | -25.2692 | -50.65543 | 2026-06-04 04:14:00 | NOAA-21 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e7757b07-796a-323e-9e2d-dc6d6b928ca8 | -12.2138 | -57.2688 | 2026-06-04 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |


[Clique aqui para ver as próximas entradas](README7.md)
