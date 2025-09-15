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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a0138bb-d6a0-3bdb-b8e7-57eefea813cc | -11.85293 | -50.53236 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3f04a49-6819-3e96-9b06-0b4f66f4fb0a | -14.80094 | -51.61593 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2a897d18-774d-3605-836e-73d789c708eb | -12.16908 | -47.58545 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20f65f6e-b6b7-3cc0-91fd-77b0f18cee13 | -10.6553 | -46.23976 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3f4168f-5925-3019-bbbe-8a6308aa8db9 | -10.89551 | -45.55262 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d21da5e6-2e4e-3628-8968-7532e2eb979d | -9.73321 | -46.04379 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f76f1a06-2479-35d7-bd0c-b4775432eb1e | -10.73105 | -44.76913 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9976b948-4711-33e7-999f-af7634afb85f | -10.72996 | -44.77624 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 408b0c36-0a23-3ebc-9a2a-e27e2d82c031 | -10.93226 | -45.49042 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ad76868-28f7-3a1e-b340-a9f9e33a44c1 | -11.08081 | -49.73929 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e917fd1a-a111-3a0d-acb3-183e7be1e91e | -10.66577 | -46.23784 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1bf7aa0d-4de6-34ee-b01b-e867e000a797 | -11.62752 | -46.5894 | 2025-09-15 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b783384-a525-3f1f-b5d1-1c65da60fae5 | -11.86751 | -50.5271 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 480fda97-27ac-3a8a-94bd-d4012c0686cf | -10.17396 | -45.3153 | 2025-09-15 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b455ca36-e127-37f0-b52a-436f5ffdc8d3 | -12.00687 | -46.66608 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d8778332-6e2a-3334-bcec-ad302226648a | -16.23053 | -47.90698 | 2025-09-15 04:21:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb6aa24c-3a72-3495-a196-59840f7eeed4 | -16.04339 | -45.16872 | 2025-09-15 04:21:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c382519-48e1-3112-84dc-4f2ad49df28c | -12.60141 | -45.71471 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b15d7d09-e69f-31fb-8c47-20875511f52b | -11.30984 | -50.85253 | 2025-09-15 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a681eb0-9a82-3bcd-8477-d465c466059b | -11.87136 | -50.52777 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ed21728a-400b-3f79-9b99-c49d9b90e9d8 | -14.5103 | -47.33959 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeee200d-f271-3b98-a9db-0b4e55fdaccf | -13.88056 | -48.30035 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 221da46d-f730-3001-8d77-52946022f6a3 | -10.63182 | -44.21104 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e638181-0ac3-3b60-82ed-893f0b20f5e2 | -10.55573 | -58.04229 | 2025-09-15 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38358b7a-59ac-3382-ac8e-7a3060fd4d7d | -14.49866 | -47.34862 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4b2ab91-d51f-39c2-b750-b7a5833d2b4c | -12.76255 | -47.99821 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7e873a8-be79-3bb4-ba96-467d15ec65d6 | -10.16944 | -46.14698 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cec5a3f7-951c-3fe5-8f1b-6cb0e5d1d92f | -15.78015 | -52.21587 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9f776b2-d913-3f34-aa01-27e4ff473cce | -12.64822 | -47.94532 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba5ee916-8989-3b6d-b30c-d28a72e6624c | -11.0427 | -41.90222 | 2025-09-15 04:21:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f945b81b-df30-3f6e-b83a-acded93ab559 | -13.87529 | -48.13457 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ba3ef87-c17b-32b7-a69a-880020f51059 | -14.50805 | -47.35374 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7495eae3-2058-3f3b-8eb1-8d396b6128f0 | -16.9928 | -45.85851 | 2025-09-15 04:21:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b536242-2801-3843-92a3-3c6881c007de | -9.1325 | -46.95123 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d48f52a1-7125-31c7-8f2a-766d6cb6bf9c | -11.31938 | -51.13158 | 2025-09-15 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf772a9f-d23d-3015-a323-a447c8c6ff02 | -10.13086 | -46.15521 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b492f70-945a-34ad-8093-2a41c314e107 | -11.07567 | -49.72441 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5300178-53f8-31b0-8dff-ac567d0323dd | -14.43454 | -43.2234 | 2025-09-15 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2660232e-07c9-350c-81a2-49915149d8f0 | -9.01026 | -49.7708 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fb69716c-2425-3c7f-a235-2e410bb11069 | -14.51137 | -47.35426 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 962b8e18-ce3d-382a-bf87-216900e405fb | -10.18211 | -46.15259 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e95f6df-6e5a-3c5f-9e78-ca667081335e | -14.59371 | -46.59594 | 2025-09-15 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0fbc3cd6-4acf-3070-8733-3551df948e70 | -16.03998 | -45.16818 | 2025-09-15 04:21:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b24ae29-6219-3a46-9672-7cd79346be6b | -10.78833 | -45.97888 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42a48fcf-57d8-3742-9150-5a3563572383 | -13.88325 | -48.12823 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b598ccd-f538-3e8b-8cc4-b29efa33ca32 | -14.93147 | -46.56779 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2e8f49c-862d-3db8-8497-4c6305ceae4e | -12.69536 | -43.47178 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7051e66f-130d-32d2-a0fc-f9d0213ccd24 | -16.65098 | -44.94101 | 2025-09-15 04:21:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49703b6e-6fa2-3ac3-8cb6-0306a37c102e | -10.66634 | -48.67788 | 2025-09-15 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 623ba5ca-2bba-34f4-8d13-460b07434efa | -13.9119 | -44.82437 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 951a328d-3d77-3838-8284-d2c0c7fb462b | -15.79293 | -52.21407 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 440fc991-bd31-31cc-8fea-8e5e32f01e19 | -11.74644 | -50.49519 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9097611-409e-3809-be8d-5ea3e4771e1d | -11.4367 | -43.54028 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91a287b6-42d6-316b-b87f-6e11778b73d8 | -15.42172 | -52.86887 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc6c4c41-51a3-39dc-94e1-a439651dc459 | -12.11787 | -44.83446 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e68e4036-dc16-3362-b728-0126d4fe3d78 | -14.22857 | -46.18756 | 2025-09-15 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e10dd420-12db-3fe5-a758-3cf817037b36 | -11.30923 | -50.85599 | 2025-09-15 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd029d9e-497c-3f6f-b660-7032a4951d8a | -12.55826 | -45.64267 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ab139d04-af58-3452-9b43-441dc8bd2a4e | -13.87866 | -48.13514 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 983a6991-d6e3-33b4-b7df-22f8f18a5a82 | -15.76405 | -52.21299 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6dd9962a-b726-3d62-90d0-14a774518b8c | -13.95266 | -44.89944 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d29ae7d-5e67-3ad8-832a-c8dad99aae90 | -11.49853 | -43.71191 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 327da40a-b514-3382-ac19-469ddf2efbec | -11.08607 | -49.73086 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 782570c1-43cd-3c65-b435-ac7542aaf9bf | -14.49646 | -47.34102 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40e24c5a-23fd-34db-8f10-85507e279a61 | -9.5527 | -45.97926 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d595ce3-f88b-3c9f-a9e6-b150e47e8514 | -10.91039 | -45.56575 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e0b1f46-62c9-3ec8-95b2-33ec1786662b | -14.50698 | -47.33905 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9854a4e8-e043-3cc9-b734-909f16572cb1 | -14.40729 | -46.39497 | 2025-09-15 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcbec479-317c-37ce-80e3-880797c62548 | -11.87304 | -50.53085 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| dafed208-5d97-3dd0-b0f8-9dedcbf5f5a7 | -12.4371 | -46.87141 | 2025-09-15 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 713955cf-3d23-3e55-b068-de526ba19fe6 | -10.75079 | -50.63567 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6902e940-9409-3fc3-b6af-da6a38fc5967 | -9.13528 | -46.95544 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b31e088-5170-3ef5-8695-79659740377f | -11.86919 | -50.53017 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8a85a655-7344-31c1-b291-fc993166b255 | -14.33907 | -46.08874 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0558066c-255a-335e-b517-0d6c8e66ddb9 | -10.80042 | -45.98798 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9069e828-84b9-37b4-b214-539616ad893d | -14.4959 | -47.34457 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00117696-8d24-375d-bb1d-2f0917473703 | -12.97509 | -47.96787 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 9660ac0b-257f-3875-840d-a6010ed212a1 | -9.17803 | -47.0443 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b8ca49ba-8196-30f0-958c-0c7784e8985a | -10.75846 | -50.63379 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0e78634a-7cab-30ba-ba9a-69d90a83e499 | -13.19202 | -47.28081 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4df2187-fcb8-3b6c-8fc1-c9c436815411 | -10.75828 | -50.66354 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dde77689-02bc-39f2-83b9-b9962a87be3b | -14.63117 | -46.37676 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f962c946-f3d2-33da-bef4-9bb6418bfbb3 | -10.92783 | -45.47538 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99111863-391d-348b-b049-2a5a70224452 | -14.51355 | -44.82797 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ade594af-1e3a-3a3f-b9bd-685a6a60c1b4 | -12.04241 | -46.52729 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70ccbeed-d478-3ec8-ab1b-086535cdf83f | -15.67145 | -52.23666 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ed46698-45fa-31d3-8093-3bbc482f3183 | -10.7624 | -50.63447 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1fe51e69-19a3-3b09-aa82-42665c528a40 | -13.90851 | -44.82385 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1e88346-b174-3bb7-8e18-35c11b4f8ee8 | -16.42308 | -45.67772 | 2025-09-15 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4982e73-b21c-3f1a-93d3-edfe49aee30a | -11.69685 | -50.55242 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa499897-b3f8-3581-8d58-ccedfb4870a0 | -9.85624 | -43.14349 | 2025-09-15 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 58c5a149-b569-39b5-a387-2ed337852756 | -13.8991 | -48.31481 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ba245eaa-08a4-325e-a2cf-3bb49e48c0e3 | -13.28991 | -43.78648 | 2025-09-15 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1abcf361-8b7f-3a77-ad27-cf2a9c88d5e4 | -12.1307 | -44.84024 | 2025-09-15 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 736a940d-16c3-3211-8ddf-ef7954367890 | -10.16283 | -46.14593 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7144e1e-1f2e-34ab-b62f-4d579a827546 | -9.3632 | -45.38918 | 2025-09-15 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8aec191e-22a2-3e5e-adfd-b726af7d1884 | -9.73266 | -46.04728 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fccce3e5-414c-3626-9e98-e8555d2ffc63 | -11.14464 | -47.65469 | 2025-09-15 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b20bbcf8-14f5-3fc4-9191-435efff82a5d | -10.14133 | -46.15331 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e41a6f6e-e8d2-3a4b-a9b8-371d72b5cf7b | -12.43501 | -48.0014 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README32.md)
