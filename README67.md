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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a082b78-0972-3aed-a070-3c16e32fb8a9 | -10.90703 | -46.54762 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8647ac0d-12ab-359d-b5d4-a1b5f6867034 | -10.90499 | -44.30095 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9870992-d11b-3813-a831-7f4ab5531378 | -13.81815 | -47.50463 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7748627b-fc76-395a-9d75-3aa760ccf757 | -13.28657 | -47.23169 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 618d345d-4e36-3106-aff2-1c3da2f9d2e0 | -11.82634 | -44.95 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f10d4737-0a8f-3b01-904c-729bd77ff2d7 | -17.38715 | -47.14661 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2febf08c-fb82-3da4-a1fa-ff2adfc8343c | -15.43073 | -44.99692 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e16a80a4-f6ba-315c-a631-eac8f770856a | -13.32749 | -47.33821 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 652c198f-5232-377d-868b-8c84336a00d8 | -11.0867 | -47.82861 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 09b99042-78c1-3c38-8ee9-c5b19be890b1 | -10.91721 | -44.26554 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46873b93-56e1-3331-a4da-6f4fea3da1f1 | -13.94202 | -48.10666 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c2fcbda-d769-342e-82c8-f8ce0ed6aab6 | -9.58527 | -54.59462 | 2025-10-01 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cd7fdbf-a277-387f-a277-2449926a191c | -13.66456 | -48.07993 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2f1800e8-563c-3c88-890f-41904737eb05 | -14.58004 | -46.36631 | 2025-10-01 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c959063d-675e-36a4-be2f-838a02bd15da | -11.82586 | -44.97545 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1a4fcf29-4b1b-3435-91ab-8cd84aa8a816 | -13.34944 | -48.14185 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68b5b788-76f7-3905-aa98-fe8d9b4049dd | -15.75953 | -43.68674 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7ad8a1d8-96d0-30ad-ae16-98c967400ff9 | -11.99931 | -46.5928 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58cb2dc1-e423-3bc5-9add-a807fc4d71a0 | -10.07278 | -50.28628 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bc6df4d-112d-39a4-847e-15319bf278f0 | -13.17419 | -47.78534 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c2df290-96db-3d65-b642-8601a9cddb5d | -12.4415 | -50.18518 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce1bcaa1-56da-3efe-bd67-bc82abd6e2ba | -12.82835 | -47.0094 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc0f02fe-6081-336b-b7ec-3dacbede8091 | -15.3648 | -47.07131 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dd11bf2-dfb7-306e-aa7c-8a771adf1699 | -11.83863 | -44.98115 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ec97ec2-5b73-3b81-8659-07a7308636e4 | -12.88498 | -45.25195 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74b6d161-1959-30e2-aa33-b525931248d2 | -12.95239 | -46.41767 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe461554-3e08-392e-8242-5561d1a67345 | -11.99157 | -47.13134 | 2025-10-01 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10bc1491-2726-3224-bbb3-0dd0d9757d68 | -11.06711 | -47.84116 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93d53459-23c7-31a1-bcec-5bac94864091 | -14.10319 | -44.30867 | 2025-10-01 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df3dd8ab-e018-3fc3-bfe7-5da681ead72b | -16.24416 | -44.06073 | 2025-10-01 04:21:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f513e008-1ef8-380e-99b6-a9dd09c8faea | -15.68831 | -46.25853 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d2bbe20-81b0-357a-a7f9-db00e951a3fd | -14.98985 | -50.76236 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11f8d842-62fe-32fe-b374-a5f9e3798738 | -10.79467 | -45.20327 | 2025-10-01 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69bf7f1a-b3c4-349b-a3ec-f53f0b9cea99 | -15.46636 | -45.88693 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20306010-3e80-359a-a80b-375b98a260ac | -14.18235 | -46.12363 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 06c6e3b8-565e-3169-aec9-2e41b9524272 | -11.46976 | -44.99236 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6413e090-1b54-3387-b94b-192603a9f1ad | -14.68515 | -48.22868 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b37e5278-1984-3019-8aff-b36f90ecdfb1 | -13.67134 | -48.08093 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d08ee4b7-74c7-3d4d-abff-8dce7105fdc2 | -16.38007 | -47.06215 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 641e5ec1-a9e1-31f4-a727-0f0e46279cd2 | -11.8353 | -44.98061 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a600a751-ca87-374e-ae95-1aa22429aed3 | -12.21551 | -47.80732 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88c17b84-0fb1-3b03-bdb6-ee8357c85774 | -15.291 | -46.40986 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a7ae755-3da4-35f8-811d-f50bdd190da3 | -14.69262 | -48.11943 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d3afa6a-875f-307d-89c1-f9b9f4551d8b | -17.38821 | -47.16153 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6cf163c-cb68-3ece-8ac3-17bfb9174a69 | -10.10569 | -50.23502 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 054fae1d-f4dd-3143-aa95-0cb1031f82c9 | -15.70667 | -48.31058 | 2025-10-01 04:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d6bb7f6-362a-3a4c-a588-127105c7f07d | -12.96073 | -48.43115 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 692d4b02-4fd3-349c-acf9-9270f4dd7364 | -18.06022 | -43.07818 | 2025-10-01 04:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7e5fc21e-2a25-3309-9a22-44924f72bae9 | -13.76805 | -47.96365 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aced23a3-b27e-3493-b5ec-eb056679bc91 | -12.24554 | -47.7937 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b2270cb-9c69-34df-98d3-d5bd78c042b0 | -13.66998 | -48.04639 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a13680e-0da8-31cb-807b-ce4883a3eaa4 | -11.61039 | -45.05071 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cec4b054-19e9-3e69-b36f-b692644419a3 | -13.37194 | -48.11105 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f88ffbb0-0c00-3def-a51f-e50c173d9bbb | -14.6859 | -48.11829 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 66de5e1e-29fa-3a57-803a-37dee1d9c308 | -14.36244 | -47.1447 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 564b184f-7922-371f-aa7f-ebb381c56684 | -15.75796 | -43.68452 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc9bfdec-681f-3c71-8f0a-94e55adc1e36 | -9.72942 | -48.02688 | 2025-10-01 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 803f9be4-8cb5-3f0b-af20-fb303b44f3a9 | -14.51892 | -48.36546 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45511d3b-505f-3813-b9b8-f9b63786dcab | -11.78672 | -48.44497 | 2025-10-01 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b9608b4-0b31-3d16-8af4-dcd10fa7699f | -15.2998 | -46.39673 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e9a7318-2716-3b8c-815e-80ce36b5ba7d | -16.75838 | -51.3418 | 2025-10-01 04:21:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 611adacf-a685-3eda-a62e-13237d24782d | -12.88211 | -46.90849 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cd020ef2-ae80-3373-a32a-33549d9ab53e | -11.94896 | -47.88636 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2595daa3-69d2-3239-8a7e-a2119022848c | -16.06046 | -51.01175 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 42030250-0dd3-3a13-8373-efb3314dbd68 | -15.38349 | -49.19484 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d13045c4-a6b8-3628-9c43-bd6180038201 | -10.84186 | -45.40442 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b7fc4f4-d3af-32ea-8555-c0dee1cc0267 | -10.18592 | -52.55341 | 2025-10-01 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75f62367-6cfd-326e-95bf-0e0ca6b50b0c | -12.16169 | -47.76791 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c56cc209-d8fa-3b73-b0ba-819b435d30ec | -12.8656 | -46.94621 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 566f2f09-d201-3e45-86fa-9fa2889c6126 | -15.93987 | -48.11726 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0557a85-f60d-39aa-9976-597655e88253 | -12.77083 | -50.5544 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 33a33c74-6624-3edc-a9a2-3762abd4c349 | -10.90765 | -46.52237 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 003089e6-9875-361b-8770-afe70fba3165 | -11.79243 | -47.60082 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79a768d2-1717-3856-98e5-0e8081222e50 | -15.40609 | -47.06718 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f632141-0be4-33da-8e8f-5ae77427bb0b | -10.98133 | -46.53069 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68891504-4144-3b21-b90c-1ff23c311dc6 | -12.47318 | -54.42049 | 2025-10-01 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b19343fc-f370-3b15-8da0-d1d2bb394ddf | -10.95271 | -44.32698 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a01e8f9-970a-3803-a19a-af2b318f4a7d | -13.33167 | -47.85988 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9978e192-3f78-3683-930b-50549d1946e0 | -14.7286 | -46.83055 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19bc5eec-7c6d-3ed8-899b-9d6cd4979d33 | -14.85673 | -47.05548 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3320c362-6d35-3da1-8cc9-069aef657591 | -15.24187 | -48.73616 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1204eea1-7f7e-395d-84df-fd12f0aa66d7 | -11.61093 | -45.04721 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9741cc1d-c487-3ed7-9cf1-e6e66ee4a401 | -14.77712 | -41.5998 | 2025-10-01 04:21:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d51c7b1e-6f5d-30b8-8a70-a18d08b1deea | -14.61171 | -48.30832 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dcb93a60-32ba-37ef-8bd5-d1006c64aaf7 | -15.76695 | -43.67275 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02e231a8-30ca-37fd-8963-949b794df630 | -14.0514 | -47.97754 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d033ae0f-3abd-3ea9-b86c-19f3a65b7145 | -13.76468 | -47.96312 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0021e1c1-70a4-3532-bdbc-949731b6e471 | -14.91096 | -47.20739 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e907a007-c92d-3c5f-babc-333ec4af5bd3 | -15.3404 | -56.95705 | 2025-10-01 04:21:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef7c7e4a-5066-39e6-a109-d2fba67e54be | -10.54714 | -43.64508 | 2025-10-01 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcf790bd-f1a8-381f-923f-065452e3d6a6 | -15.46249 | -45.89 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca9f5ea5-b49a-3edd-8a63-09265ad58aa9 | -13.03214 | -48.6741 | 2025-10-01 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7e1a63b-a960-3b09-a54f-b5f97a2ac644 | -15.36641 | -44.15308 | 2025-10-01 04:21:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64d9c36d-9180-36a2-a9a4-f037a8ee275c | -13.30995 | -48.70027 | 2025-10-01 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 349f35e8-f103-3536-8952-8d269bf4c10f | -13.76268 | -47.93285 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c68e4948-8b31-3fcf-92e2-1c85fbf63231 | -14.03638 | -47.96373 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 969ad590-29b0-38a6-ba72-c53c71fbbdd2 | -14.78575 | -45.7598 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b74479c-ab99-3393-8ec9-b6b0d9486d9e | -16.00177 | -50.87788 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95b19bc2-a46d-3638-913e-2b68a3ae20b3 | -14.69969 | -46.97129 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fe6b6d9-e9c9-3cc1-a71d-bdcc8f0f6df9 | -14.01735 | -46.31038 | 2025-10-01 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README68.md)
