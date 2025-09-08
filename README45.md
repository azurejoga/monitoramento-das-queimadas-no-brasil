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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee7972f7-8818-3e69-9298-6cc91e0d0fb1 | -11.32642 | -46.56299 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1da1e95-d747-30f0-908f-12998658666b | -15.16805 | -47.9881 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e66a87a-3a3b-30bc-b48b-67ec9d373398 | -9.95781 | -51.19686 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 970b4ee6-d6b6-328e-a066-5417c715324b | -10.32945 | -46.35723 | 2025-09-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cfafdce-9e53-3f8e-8a36-e0bbb794c757 | -13.35698 | -44.42879 | 2025-09-08 04:02:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbaab7f7-9830-38d1-aa3c-70d26704c0b7 | -9.1482 | -46.07215 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45eba097-988c-3be0-b623-4f3f59288be2 | -15.54411 | -48.38026 | 2025-09-08 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6336a75-f84c-3a9e-9c39-33f95593b95c | -9.20429 | -46.05464 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06d9f695-7bd5-3809-af92-ec18cc3800b9 | -11.15185 | -45.24543 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7c816d2-a2d5-3358-add6-1fd25b7d3e6b | -15.18735 | -47.97841 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4142903-c9bd-3d63-b2ad-87c47334a223 | -9.14953 | -46.07558 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2c1c627-7cff-3ea5-8c2b-f92f4652fb1a | -13.72287 | -46.88899 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10f1aefc-be53-3d26-9593-cac1781a2fba | -10.80844 | -47.25476 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f19d603-5dba-35f7-93c5-5c7579160f19 | -9.88105 | -46.53495 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 46760f4c-614e-3528-a154-27acf50a76c4 | -9.20694 | -46.03931 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77951581-8b2d-3a83-897e-40c9e7ce77d6 | -14.7907 | -48.14387 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cbdb50c5-45d5-3d99-a3c5-60c7455da33c | -14.50809 | -48.81522 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dacc2470-4b46-36ba-8a8c-7b69a617cbde | -11.28319 | -46.47106 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 14d585b3-15c6-37be-9b17-ca481ca4bab5 | -12.86337 | -47.97943 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecedcd6f-1edb-3dc8-862a-f4c646abcae8 | -12.92506 | -54.78218 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a40418ab-a0b2-3347-ae8d-749fcc169afd | -8.13928 | -48.47747 | 2025-09-08 04:02:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cfa7ae3-5f8b-3355-a857-0365b35105f8 | -12.84924 | -47.98193 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33ec9687-30d5-31f5-bec0-69fa21128358 | -14.99658 | -48.01787 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 680c98a8-4ae9-3e0a-8a27-f926ba31bff3 | -11.21116 | -55.00769 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37dec1a0-134a-30d4-a635-bfc63b61889a | -14.68605 | -48.19318 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 182d41a9-dc52-31e4-93ea-9161f7faab2e | -12.83042 | -52.90036 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da98fac0-5344-3fd3-9ad9-32c96db0cf39 | -13.67052 | -44.22666 | 2025-09-08 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 54b2571e-ed40-3ec1-ac84-dce69f773206 | -9.03535 | -49.7992 | 2025-09-08 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c4580e3-f24b-38ae-acb2-55d1bd702240 | -10.78241 | -46.01052 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d70d5d35-d176-3c6c-86ed-6d30d87822e1 | -12.81006 | -48.00082 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aa94bc1e-788e-3574-9f51-0858fd4c79f0 | -14.29783 | -44.87163 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41fe1efd-09a9-3abc-aa18-ad3fbefdb225 | -11.38105 | -50.41541 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dbd9d9b-e32f-3420-9deb-a5c886393e0d | -8.82672 | -45.89718 | 2025-09-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e629dc71-3b0a-3f10-9d15-70a6b1ed8d0a | -14.52499 | -53.97639 | 2025-09-08 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 526ed670-7a3d-39f1-88e1-9c2c71cec6ff | -11.86044 | -51.06831 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cdfdf96f-0e76-351d-9af8-54e2ebdab680 | -10.28494 | -48.80691 | 2025-09-08 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f6e51a0-99ce-3ad1-aee1-cda79a3c731d | -14.51669 | -48.79923 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fdddeaba-dd35-3a8e-8332-dd5707e0f364 | -13.64923 | -47.91749 | 2025-09-08 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52093836-1898-318a-ac4d-dd4d247c852c | -15.29618 | -43.37543 | 2025-09-08 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d1d33537-0917-34e9-ac2d-6325084d52d4 | -15.29557 | -43.37913 | 2025-09-08 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6dff0585-a0ac-3497-a0ec-9b2411fbaf1f | -11.27977 | -46.46646 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a324ba4f-efc3-39cf-9308-d9a4cdca71fe | -8.18145 | -50.14338 | 2025-09-08 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c10e1cc6-87c5-3d93-b893-f77b006d8336 | -11.28385 | -46.46734 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 54f11ae6-3151-3852-ac5c-51a9345254d8 | -11.20269 | -55.01324 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4ec8086a-9858-3f4f-a0fc-0e70b199c337 | -13.71942 | -46.8849 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bc24ba8-a620-3cdf-b2fa-66e0108668e2 | -10.15356 | -46.21762 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b34ef438-6239-3b80-921a-7b287a7a4a5e | -12.00457 | -47.77228 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bceff016-b57e-36c1-b757-4946c2406216 | -12.9492 | -54.76799 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a99ec8ec-8ac3-30f6-b5ac-ddc5059ec0c3 | -14.42365 | -48.45896 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ad4980f-9c7d-34bb-85ac-bdf9a067cc77 | -9.03067 | -49.79481 | 2025-09-08 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0412721e-3d4b-3ae9-bbb0-0d92f7a2696d | -10.18036 | -46.23409 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b12a73a0-3d70-3c22-b0e8-5809ec500875 | -10.79878 | -47.7279 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8264680a-2c20-3ebb-8c4a-d6fe8f85cce3 | -11.41323 | -43.5891 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1428a9ad-42c8-39ca-ad7b-f729391219b9 | -11.60516 | -47.15219 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56533809-2821-3b12-bf20-f2236d344e51 | -11.402 | -50.39165 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a6e4b9b5-0c39-3657-bd66-3bbc637e0084 | -14.21845 | -53.34885 | 2025-09-08 04:02:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 685eba24-1838-3430-bf09-2a7ec998affe | -9.40018 | -40.30804 | 2025-09-08 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e0f3446b-a94a-375a-bf70-b11ac9706be9 | -9.59694 | -39.67625 | 2025-09-08 04:02:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 891f157d-6ea0-378b-91f0-59fc8ec43420 | -9.1769 | -46.06535 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f068f28d-9f0b-3ad4-9d8d-779409c25c7f | -13.03759 | -47.14206 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 726a01c3-54e8-336a-a0ed-4299f6247885 | -12.19521 | -53.90815 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f4536d2-b037-390b-9f77-aafa724f2d89 | -9.33011 | -46.53072 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72a3b6b7-2804-3ebc-8ce1-a4cff46c36b6 | -13.04107 | -47.14664 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d56f574f-6a4a-3b2d-99f8-95c8416e1011 | -15.18184 | -47.96074 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 400c6c6a-a2a9-3f17-b107-a7f23e21841d | -11.76066 | -50.6374 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9dbc2629-84de-33a7-a045-39e9df93169e | -15.24253 | -52.38805 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d078331-593e-3567-a9b1-aa3687113abb | -17.63097 | -44.18123 | 2025-09-08 04:04:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec3436f8-15c6-3bcb-9055-06c3f13d4f3e | -20.92843 | -45.26859 | 2025-09-08 04:04:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d5928147-b920-3c83-a757-8812a3230604 | -16.90934 | -45.83746 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7f48ca04-003e-3840-b1cf-63db2a51ee53 | -17.59278 | -44.53347 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 410c220a-e629-3e06-917e-e02dbb902da9 | -17.16197 | -44.44279 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8277b27b-4a45-3e53-81ee-39949f378c62 | -20.53582 | -46.47836 | 2025-09-08 04:04:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a5c4b12-1a1a-366a-a703-2ee50cf2e40d | -16.52104 | -45.11199 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3fec836-ea16-39d2-83b1-31e662936fd8 | -17.164 | -49.02908 | 2025-09-08 04:04:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb164661-7e2b-3250-ae0a-b86664785072 | -15.21837 | -52.34799 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8410798-a387-3cb3-bd59-48ab74d44f8f | -15.73305 | -53.58538 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e95d286e-440f-3660-94af-bc30d9bc8c72 | -16.95343 | -45.75817 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 525becb6-a35e-3518-875d-1483798ebd7a | -16.30744 | -45.693 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2838beb-7403-34fe-a02a-76110080a43c | -17.71022 | -44.48209 | 2025-09-08 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d996cbc-7226-3e84-a17d-c9a47a27a95c | -22.68892 | -46.92683 | 2025-09-08 04:04:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| ee2dba51-5986-3fd1-abf6-415f50400c3a | -18.24206 | -46.63086 | 2025-09-08 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ca7d02a-54eb-3397-9e9e-8dee2ce37c80 | -16.90768 | -45.82639 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 128f48be-d70f-366a-914b-17df5972a278 | -16.9113 | -45.82713 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b6514002-9a91-310d-b4fd-2f8233b08559 | -15.24164 | -52.36423 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4343144-ef1a-3c13-9a68-f53e23030f12 | -16.27941 | -45.68094 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b9d42c17-fab9-378e-bbc0-d5ff38013294 | -17.14979 | -48.68099 | 2025-09-08 04:04:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6944db31-e73e-31ca-9344-a5c964f40c09 | -17.16472 | -44.44738 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc91853c-49aa-3d60-9d9a-883e36f5e0bd | -18.04465 | -47.10207 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f050a17a-96e2-3970-995d-5fdf18d17e3a | -18.0472 | -44.33748 | 2025-09-08 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98aeb29f-140d-320d-ad46-f70ed635faa0 | -19.62366 | -43.95617 | 2025-09-08 04:04:00 | NOAA-20 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9d01544-ef93-3ad5-aab9-3d7632c3cfe0 | -17.15855 | -44.44212 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d4c6a937-1e4f-3eb7-8bec-8017f1fa8292 | -16.37813 | -46.87666 | 2025-09-08 04:04:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a4763f9-8bde-3278-8904-294f1f2d7155 | -18.58567 | -43.98724 | 2025-09-08 04:04:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47293d8c-8fe0-367a-b9ae-1df754d756ac | -17.57369 | -44.5421 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e98de963-f7bc-3d1a-b17a-f2a6b16f9e7e | -16.54646 | -45.11243 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b040dc45-2448-3ec4-8e5a-60bc2d6606bb | -18.04382 | -44.3368 | 2025-09-08 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd7e118b-6331-3c77-9fc2-1fbbd9012034 | -15.74329 | -53.5365 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8980c419-fbf6-3a68-9696-2c86de35c21d | -17.26129 | -46.69804 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62b79a75-5ae8-3a15-b262-a67e408aec11 | -22.69046 | -46.91803 | 2025-09-08 04:04:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 81bcb9a1-c31a-3186-8912-532fd95bbeda | -15.74485 | -53.53888 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README46.md)
