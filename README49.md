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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b09b747-94c7-37ad-be92-8729452039cc | -11.8039 | -58.17846 | 2026-09-18 04:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ef8a519-d113-3bc6-a8b2-1df0e87b2039 | -10.15973 | -45.3606 | 2026-09-18 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6716fb07-f0a3-35ea-bbb9-0ce7e40ea1cd | -11.16836 | -42.84679 | 2026-09-18 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dab70960-ec71-3941-b523-dedb1c16afb0 | -12.29156 | -50.74526 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 531bd341-35d7-3b05-880a-5a6fdb3b085d | -9.75166 | -46.57094 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8990c012-9fb8-3f4a-8ab8-d41a927df938 | -10.61099 | -46.56135 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5711026e-4d9f-3ab8-bdfe-114a20910bac | -9.84668 | -48.39022 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d7fbdd83-6a98-3893-b5b8-4b10b66a5919 | -9.70523 | -54.82202 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a565b645-b06a-3207-bee7-542bb923c08e | -8.88357 | -45.88744 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e87f74a-f30c-3488-994b-7ad0c3360e96 | -9.39786 | -46.8468 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09906de8-c325-336b-a203-30fac25e4927 | -10.85888 | -43.84242 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95829089-7c0d-37be-a37b-b0024fee45a7 | -10.52092 | -46.72098 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9c2655f-0758-3ec6-af1f-8205fee77b53 | -9.33101 | -48.16881 | 2026-09-18 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 824c4646-11fa-33da-9aa6-9599e0956b92 | -10.65759 | -50.4674 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf842d90-ce46-3441-9e02-1ca54f883f29 | -9.6326 | -47.80664 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ed6b909-9e4d-3e0d-92a6-fcff848a1b03 | -10.10619 | -45.63721 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 445f56fa-8d8d-30b6-a144-ee5265fb0fd7 | -8.86768 | -45.85645 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb7016d4-4605-3a5d-9a01-4ec51a78f45c | -10.10786 | -45.64819 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af865acd-66aa-3840-ad64-76ca140c7be6 | -14.962 | -47.53157 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3384ad8f-2e9c-3d6f-9f81-1e1f9943731f | -14.93758 | -49.92385 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99660dab-0bfc-39c8-9176-3971d92d2899 | -10.53743 | -44.85019 | 2026-09-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48df20ef-7c53-3ce6-94e2-e6394d2e62b8 | -8.77975 | -46.90602 | 2026-09-18 04:21:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b8d4cea-d56b-3c30-bf95-ac7f5ce0c252 | -8.47154 | -44.53522 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4143579c-14ce-3fa4-888a-e327c5b415bf | -11.31089 | -47.25027 | 2026-09-18 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3f11b449-af68-35eb-83c8-40c58b95b600 | -9.95265 | -45.68442 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9008231-e950-3857-9f0c-f6c2e29acb0d | -8.76955 | -45.89814 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73ed5055-747e-399a-a716-1635267dee70 | -14.96144 | -47.53513 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 938af4e7-ba15-3223-ab99-91f472f4a7e0 | -11.8955 | -47.57025 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f7fdb14-1507-351e-acdd-35f54546f8ce | -9.74295 | -46.11178 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3ab8df2-46d8-399d-a54c-226255718cd6 | -12.33148 | -47.73978 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb2d3342-4759-328e-b129-4dd63c4a5c14 | -10.6615 | -50.46808 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e79eb758-1f27-3a25-b55c-ef7bb543fac3 | -12.05604 | -47.50673 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7aa9485e-e3d1-3d92-9833-4f27f88a6919 | -9.91134 | -46.55274 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3f741bc-4338-3388-89b2-ca9a49748c85 | -12.17588 | -46.99179 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 59756fb9-e23d-3647-90b2-5c58d79174d0 | -8.65797 | -47.46716 | 2026-09-18 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dac72d1e-103f-374c-928e-1e856cce64c8 | -12.05663 | -47.5031 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c3d0dc8-226a-3693-8224-856dfbb20bbf | -12.33683 | -50.7666 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dba5202e-6623-3f7e-84d1-daf390c2a145 | -11.34065 | -43.97159 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4c8135e-9f41-3a29-bfc9-0b9d4f36cdf8 | -11.82195 | -46.7992 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c1a213b-5a3a-36e0-987d-ab9d8ea6f90d | -12.51714 | -47.0919 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d4eaa0bc-f3c7-312a-97c8-431f57a68e82 | -9.92472 | -46.5114 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| debc6c76-2aea-343c-b296-228d920a30a6 | -8.99484 | -50.16882 | 2026-09-18 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faae7cdc-a306-33a3-8d0f-610966e5c954 | -10.11097 | -45.65292 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e003f835-9e58-3bbf-9a5e-2e4417ee37c8 | -8.67795 | -45.30986 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93524d26-557d-3b16-a5ea-7759885dedcc | -8.11827 | -45.62548 | 2026-09-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 822a378b-a668-375d-99bf-032e22480944 | -13.24973 | -46.91391 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b2ba946c-906c-3644-bfad-e65faebc24d6 | -11.6705 | -54.43796 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c851ed69-db80-3a36-ab3d-72f7a1caadb6 | -13.60171 | -48.28978 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14630439-f296-3c8c-a984-f7f737533382 | -12.62459 | -50.89418 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75949e82-2a54-31db-9451-43ba46fbb65e | -11.32452 | -46.76072 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96cf604e-feac-3212-ba30-ef502dabeb0d | -11.47407 | -45.72036 | 2026-09-18 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c0dcbc2-fcd3-3f70-aa57-1926fd897264 | -13.94819 | -49.64707 | 2026-09-18 04:21:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6c82211-31e7-3ab4-ae4d-c164d0f6a86b | -8.68105 | -45.44185 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88047017-d2ae-3a5f-877e-4df7292a0c05 | -8.48129 | -46.88074 | 2026-09-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 805bdecd-97fc-3093-8ec7-052bc25f7fe1 | -13.60801 | -48.29817 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 90e754b2-2954-3752-82b3-f412f661e67e | -11.28413 | -43.36184 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcc654a5-9818-3691-a0da-a58d6585cb00 | -10.0972 | -48.85342 | 2026-09-18 04:21:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 248b7f9e-68ab-3c98-bdb7-f165e69c43e0 | -10.80046 | -46.65414 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54a96fd3-e895-3e9e-a6cf-ff251fad2a23 | -9.39948 | -46.85814 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cef68ab5-db22-3687-ac77-69a7df941e0b | -10.48724 | -46.31083 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02e9b7ef-2161-3426-b6d3-0c548e604057 | -9.94296 | -45.33316 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc6943fe-2ed5-3e0b-ab4f-10c74e5b6afe | -12.53043 | -47.09407 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7cf5546b-46db-37db-8cb6-4c4039fad7fd | -8.85778 | -46.92579 | 2026-09-18 04:21:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5560a932-95d2-3a5e-9e26-643de48f665f | -9.09253 | -45.72448 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06e46f96-310c-3db9-824e-cf50361c4818 | -9.84315 | -48.38966 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c217e85f-d2b4-3852-8a35-4ef6e91ae6b1 | -10.61718 | -46.06968 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db1a282a-5ce5-34a7-b883-b37f8c83b4b4 | -10.95008 | -54.09078 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90cab8e1-c947-315f-894a-592f56ea3777 | -14.22711 | -48.50978 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d55fdb97-82ea-34e4-a1b4-714f9d2207a1 | -11.55457 | -46.89677 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 733fbd4c-37e2-33d6-ab43-b685730a43f0 | -13.3597 | -46.29856 | 2026-09-18 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0c67867-51ca-3af6-a2fa-39fd16cb19bd | -11.10719 | -47.09846 | 2026-09-18 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cf85bef-820f-3c27-9071-2e0262d772d3 | -8.55799 | -44.89928 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bceaa8a4-a436-35ab-a1aa-a0b849c9da22 | -11.32705 | -47.25671 | 2026-09-18 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34227194-7787-3a58-960e-d3ed368c3db4 | -11.16372 | -42.80336 | 2026-09-18 04:21:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 09393cc6-3227-37a2-9e27-a83fa2d2433c | -8.88412 | -45.88396 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa6ac923-e780-3868-a13d-984125d200ff | -10.51809 | -46.73873 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef00c095-1b50-3d2b-b4cd-7624f3224b54 | -11.13573 | -47.72426 | 2026-09-18 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c2cde56-9e28-3a97-a4f8-1b0ac316e035 | -9.71889 | -47.13999 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3eba2a67-c9df-3ab6-87d2-801d7933d88d | -12.2666 | -50.75107 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6d707d0-dab0-3dfd-85c0-363491f73f2a | -9.08647 | -45.71996 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a43588d6-7d00-39bc-9fd4-bcca38b6cc0e | -9.60484 | -45.36153 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6da32308-7196-3cbe-bf29-54e5af301dee | -12.26532 | -50.7816 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1850bbab-fcab-3773-a133-9c81b690a50d | -12.43111 | -50.68168 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84db2236-1b50-3bf4-8521-06bde840a899 | -8.90412 | -45.01511 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6ce36e23-0765-35aa-b46d-257f2fd99f79 | -11.67603 | -54.43601 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d428b289-0f5a-39c4-84f7-e6398ebc8f7b | -12.17037 | -46.9836 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| af52ce03-0952-3c1f-8854-28177fb2ebaf | -12.40282 | -48.48536 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38006fdb-b5a8-3ac1-b7c2-2b61b16e8d51 | -8.8808 | -45.862 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c72d6f42-0b2d-3505-ac6e-202f89790e0a | -10.62879 | -50.25644 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea460862-ec0c-3d44-99ff-af446a785e25 | -11.63888 | -51.58319 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bbae97d-4799-352f-b9c5-cad40cbd4a27 | -11.80493 | -58.17347 | 2026-09-18 04:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bcf0ed80-7350-3517-b8cf-56fdef15c630 | -10.32207 | -45.32166 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb220be3-be89-3e3f-85ad-9d0e4f4d4b21 | -10.83848 | -44.94829 | 2026-09-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a0bcb42-c4e8-3080-97de-35e18742e8a7 | -10.63149 | -46.06482 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0a4a633-551a-34ec-a25f-db4bbeb1a06b | -10.54409 | -44.85123 | 2026-09-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cf22508-9635-3c47-b173-96529faea904 | -12.57205 | -47.08973 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7920cab6-ad25-3900-8609-471fabd9c474 | -10.62819 | -46.06429 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a799ba5f-9ce3-36b6-8988-f822b6016bf0 | -9.92969 | -46.52306 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b1da6fc-ccd4-315e-be77-0874a1059196 | -10.59828 | -46.55563 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 232580d4-a5a2-3178-a2d7-cde243836eea | -15.04057 | -49.4388 | 2026-09-18 04:21:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README50.md)
