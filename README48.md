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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 169ceda6-5ec3-35ed-9258-74473348e30a | -8.34713 | -52.51863 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b186839-748a-3ee6-9614-a4f78c07af29 | -8.87879 | -47.92501 | 2025-09-05 04:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d1d11d1-0064-3c60-ba88-4de57a6a36f2 | -12.60337 | -56.99859 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4de3abe-f7a9-309e-838c-c2b4c12e4824 | -9.34408 | -57.43047 | 2025-09-05 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa638aff-33a1-3b28-96fd-39736495daec | -14.28855 | -45.22054 | 2025-09-05 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4cf0a13f-1055-3466-a733-48d9e908fac1 | -12.98485 | -54.79752 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f69f01fc-fc89-3c37-b86e-ab7a9d023f68 | -11.61723 | -47.79172 | 2025-09-05 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49349be0-b2b0-3278-8aa2-5ad28a346f6d | -9.08216 | -47.00028 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2d8d57a8-9b10-305a-bdcf-057e12e4ff0b | -9.97013 | -51.65098 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c938a4c6-f665-39e2-a2d4-fe791d3863f8 | -12.96018 | -54.78649 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7373ed9c-dde8-397d-9339-701e171a02ad | -9.70109 | -51.07231 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ce0fa35-b252-3c82-9da0-cea9ae4bbf94 | -10.86365 | -56.36604 | 2025-09-05 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1385f5e-ded7-3ea4-a236-0fbda58d06c9 | -6.87033 | -52.78717 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b623eca-00ec-3728-a672-add4d0c82953 | -6.83258 | -52.80725 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 091a1fad-1424-3506-933b-04c0b2b5e169 | -8.64831 | -54.85279 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98b97d30-61bd-37c2-a9cc-994099a077f5 | -10.07876 | -48.06931 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba696893-fe7a-3ddf-a9de-5a6f67a35ce1 | -8.09331 | -45.33734 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5221ce94-ebcb-3b6b-a7e0-deddd97c5fe9 | -9.50509 | -57.81696 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b38427b7-cc5e-3d80-810c-fcdbe627f82f | -12.24391 | -50.13649 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 119a3228-bbed-362d-9945-56c2d8e30b48 | -12.88875 | -56.952 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b5b4ac3-5c9f-3e39-bec9-484f4dd0d3f0 | -13.74479 | -46.92932 | 2025-09-05 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 067d48df-8b55-375f-9062-9bd265a5853b | -10.97218 | -46.82308 | 2025-09-05 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad56cc97-8623-3955-8fa0-4897edb38eb3 | -10.51864 | -57.78115 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba6d6695-6689-3b59-b845-b39976813ef5 | -13.27109 | -51.86093 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e354b63d-8b93-30e4-a6f8-48445e6d53bb | -9.80637 | -48.31062 | 2025-09-05 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afe0a43f-2e46-3fc0-973b-942c43f69a22 | -13.10447 | -57.11173 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb87885a-393a-3f9f-be10-25eab3f08e29 | -13.00405 | -45.22624 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d225cbd-20f0-3bff-bf03-28efe02459fe | -13.46801 | -46.83514 | 2025-09-05 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68d6a4ff-8c3e-35e7-9322-e87fe62bb96a | -10.51227 | -57.77599 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fd7fa8d-4867-3ab2-928e-c6245f598f0f | -6.33374 | -58.17319 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c43d54b-1491-34b9-92ba-bf332b8b1d22 | -5.85279 | -57.76603 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56375441-9500-368f-8bbe-c9da423935af | -11.32016 | -55.22464 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd2992e0-72bc-37c8-a044-7394dc5bbed9 | -11.63119 | -52.21267 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6f02ec5-3cad-332c-a02a-a97e7f36726a | -7.60897 | -43.85366 | 2025-09-05 04:57:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 989627fc-1892-369e-8d2e-7abc2c2812af | -6.86751 | -52.78302 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7393bfdc-6a89-3a81-8b7b-3d6d7d5fefe9 | -7.89351 | -45.23412 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66020060-8232-38b6-a2a3-52af68295c2a | -6.43723 | -51.87589 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e452548-0530-35e8-9345-e31b2f19dd89 | -11.6151 | -52.19014 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf15ff70-1ee8-34b0-97cc-3996ee32c3c2 | -13.2957 | -46.84749 | 2025-09-05 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e851ff1-f9de-355a-a218-dd1c2203e912 | -10.9711 | -45.97852 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14aa3bb1-4d6c-3489-b0cb-2e45065ab8f9 | -11.86609 | -51.45753 | 2025-09-05 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b97cd86-e57c-38d4-a96d-546c6192c497 | -12.97931 | -54.81134 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ab3b75d-15b5-3e47-bc54-024f50b54349 | -12.97803 | -48.0782 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8a68acb-0224-3ea9-8826-830b93ba2ca4 | -11.0351 | -52.04979 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01917c82-11f9-329b-b164-f56ce000193a | -9.3386 | -55.23468 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c2fc56b-ed05-344b-9d93-336f0e92caac | -10.24875 | -61.78355 | 2025-09-05 04:57:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4c50480-e443-3251-b1bd-1c2ba4ace81a | -8.91985 | -45.12018 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 743cb746-f7d4-375e-8a69-a43019d554f1 | -9.71478 | -51.08363 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02198e8c-02dc-3ebf-9d23-4907320ce1a4 | -12.99379 | -54.82837 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52e91773-dd36-37b4-93b4-dc7e2147e2a2 | -7.19641 | -46.19907 | 2025-09-05 04:57:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad7d04e5-9343-3771-8247-40a546653799 | -9.33255 | -55.20866 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 354ffe38-4dc9-38e0-b283-dfe87045664f | -10.45225 | -53.61508 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38e1c340-8ea8-3071-b87c-59287c066429 | -7.77277 | -50.31845 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d0d66b1-e71f-34d0-b9f7-6f558d1acaf4 | -12.48479 | -48.08667 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d32d20dd-e4e6-32ce-8ee5-3a3739b6b614 | -10.76184 | -45.27052 | 2025-09-05 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5956e203-da60-3cb0-95ed-ead52cc72e48 | -13.35144 | -46.83057 | 2025-09-05 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40530d92-aae3-326c-add5-daac6de2f8f9 | -8.89452 | -45.77969 | 2025-09-05 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d1f2355-33e7-3182-b8b3-cb00ec0fb234 | -8.09081 | -45.47767 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91d9b273-0e3e-35b1-9b42-21a311a39baf | -13.05888 | -56.91372 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3dad7e2e-7951-3935-868a-248e02811b6e | -8.08285 | -45.33353 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9655155-3362-34b1-8d3d-ae52e02070eb | -12.96692 | -48.05033 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90ba5a6e-1d1f-3861-b7bd-829438cec9e4 | -12.99324 | -54.83194 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5558d40e-5eb5-3bf3-be8f-5a78c700b24c | -9.33586 | -55.2092 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97e89d12-beb7-3bc4-b84b-6c1ed5ae2430 | -12.9515 | -48.05693 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5860ae93-efce-3bd7-9b4d-03826fba14e0 | -7.68675 | -50.30011 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 413bf882-0885-3a9d-9edb-76d33d4dd318 | -9.62491 | -55.35622 | 2025-09-05 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bfafefc-7996-3f08-a691-ac8619a50266 | -10.96615 | -45.97443 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbc90c4f-1735-3471-a9ea-39da5129f09d | -8.00902 | -45.45396 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0036592e-a14b-3a87-a5ce-93c78540ff08 | -9.07056 | -50.42796 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b2237bdb-941a-322a-96b5-342d23080b8b | -8.02602 | -45.40948 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5516114-8081-3497-a67d-8912d61f4800 | -14.28265 | -45.21988 | 2025-09-05 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d7723509-e627-36f2-adfd-d67debd09436 | -11.00527 | -45.92386 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b26472a0-6aef-372d-80f7-99650a50a511 | -10.06892 | -48.07287 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e199373-02e1-3472-be3f-68f00f434ac6 | -12.9821 | -54.81547 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| be482868-0bd3-3207-b21e-0d5f5ef2d37f | -9.48633 | -54.42542 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59c371b6-6f4c-39c2-a39b-d85694d19864 | -10.96163 | -45.96687 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f12244ec-568b-309b-ac1d-a8817583a4cb | -13.73948 | -46.92933 | 2025-09-05 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebe817aa-3894-3478-8df9-5879d90142b5 | -10.97798 | -46.01095 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d003b0c5-e5ff-30b1-97c5-08b0c9945ffb | -12.96853 | -54.77676 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce892dca-2b47-3ae3-88f5-5fe801765ca6 | -7.77671 | -51.08214 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76fa8234-2b8c-371e-be9c-d9b2d1d2ad04 | -7.89976 | -44.93559 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0ee8e80-6076-3c21-9a0b-0acc78ad07b9 | -8.06862 | -52.34994 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6263bb3b-6ac1-3286-bf82-553a1d464c92 | -9.07226 | -47.00005 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f599a402-134c-31b9-bc3c-992fbd14028d | -10.51643 | -57.77263 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca0b830b-48e2-3304-8486-db66dd9ff2c0 | -6.32894 | -58.17949 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66a09949-80c1-3c47-a3df-cffcb27a47e0 | -9.98502 | -51.62469 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71292a34-ae44-33ec-a9a4-acd28104c2bf | -9.32924 | -55.20813 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36485b7f-427f-3bdc-9628-ff45eb933fff | -9.41993 | -46.80724 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdf39ad1-f78a-38e2-bb25-6760d0fd7512 | -7.22875 | -44.82977 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8af49c60-6933-3be8-a384-9c8520ce6c8f | -12.52137 | -48.06634 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce8abdd6-6ac0-38dc-a025-6ddd54228879 | -9.70469 | -48.99063 | 2025-09-05 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3802bec7-f65f-3fe5-bf62-2a0b1cd76482 | -11.5844 | -47.89111 | 2025-09-05 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58a4d869-fd5a-3142-b52d-b60b530bcc3b | -7.98201 | -44.52683 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac1cb078-7c2d-39fe-9115-bd2f06d78fb9 | -10.14443 | -55.16415 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d941ce75-e82e-3db7-a160-b6b96261896b | -8.18872 | -49.59258 | 2025-09-05 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1a1477c-d417-3a1d-b37c-708fd072d844 | -9.07152 | -47.00546 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb6376c4-eb35-3c91-88be-a6cea4ff5acb | -9.75895 | -46.90961 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e04c7b05-0dc3-382c-abf7-84dc357c9dd2 | -9.38074 | -50.38921 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9af88428-f130-33b8-a998-eeb7c663670f | -12.26249 | -50.15447 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f9485a4-bccc-3ea2-860d-3c4ad2f51620 | -8.52137 | -51.32345 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README49.md)
