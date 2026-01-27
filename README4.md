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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef3d39cf-3fff-3ea4-9745-1e9012d78f16 | -19.69988 | -56.8228 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a985d973-022e-3e4a-9bc7-11cc2b4433b3 | -18.80919 | -57.71381 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e7e71a61-5db8-3846-b4f7-59d0aaf494e1 | -19.34688 | -54.17146 | 2026-01-27 05:01:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3645f00f-b632-3544-98b8-c99e3795e783 | -19.60643 | -57.35626 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 15b7fa33-b2a5-3acc-b7a9-154d87d21887 | -19.34328 | -54.17091 | 2026-01-27 05:01:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c927d34-9151-3578-b2f2-fad9690adb5b | -19.69931 | -56.82648 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 94b1bd75-8c4f-3c05-bc55-f9450aad5be7 | -19.69599 | -56.82591 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a2bc2177-c620-399f-bb9b-f804196b9e44 | -19.72041 | -56.82255 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| b7dd3d98-cfa3-3820-8061-1826859ca8d8 | -19.71375 | -56.8214 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| cdd73854-1acb-349d-b810-222b9eeb2366 | -19.68783 | -56.9227 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 33fff5c6-3b3e-360f-91b2-b6139b5d460d | -19.61018 | -57.3757 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f314a2c8-bfe3-3107-bdfb-7409a3ff375b | -19.68726 | -56.92638 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 21296ed4-17e6-344d-bf6b-5548a70698fd | -19.70653 | -56.82394 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 65e4ff19-cfd4-30a6-b6f4-6b6000758245 | -19.60758 | -57.34895 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7374bde8-6028-324d-b4ee-a37ae9ac81e4 | -19.61292 | -57.37993 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8497019e-a6c5-35a6-b11a-320de8b20939 | -19.69209 | -56.82902 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fcdaac80-23e2-33e3-90e3-9ff0f7a918f0 | -19.60585 | -57.35992 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d2332587-0340-392d-abc2-775fc0c78755 | -19.34267 | -54.17521 | 2026-01-27 05:01:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6643a57-fa91-3bec-acdc-11d8919644d6 | -19.1021 | -57.77182 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a3d3b04b-9e06-3967-8abb-fc64c88fe476 | -16.25153 | -60.03463 | 2026-01-27 05:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f2d3311-08ac-32df-8e11-8da48c439f2d | -19.61133 | -57.36839 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e3ae6f15-52ca-3128-856a-32ca07d09105 | -19.60802 | -57.36781 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 35c1d6c2-7379-3804-97e7-a7ee6e57bedd | -20.16141 | -50.60765 | 2026-01-27 05:01:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 26c912c2-4ce2-34cd-94c1-4e9803f2a3e5 | -19.71708 | -56.82197 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| fa832450-d188-38f7-be78-fccfcd57fba9 | -19.66711 | -56.83606 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a285fd5d-d2b9-35c2-99a4-7cada23816ad | -19.69656 | -56.82222 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| afac9bc7-669f-38b8-b102-d670691dc4ac | -19.61075 | -57.37204 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6042141c-15c7-39e8-954f-a7e2d633bc94 | -18.90972 | -54.83283 | 2026-01-27 05:01:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef1c05df-450f-38be-9a38-867cd6605645 | -19.10542 | -57.77241 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cb19e1ad-e65f-3d1c-b8ae-5dac81352d49 | -18.81192 | -57.71806 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2400d021-bff5-3c07-81b5-ff0b669c1c88 | -19.69266 | -56.82534 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 56e0d9d9-33a1-39b1-a9ba-721375c32ed9 | -19.67043 | -56.83663 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 96255bb1-79b8-3c53-bb84-82f49a3cafd8 | -19.60816 | -57.3453 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 758eef85-3142-3ec7-98dd-c31647ad2f66 | -19.61349 | -57.37628 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d1fb9792-c9ba-34a7-ba67-ff6743407e20 | -19.60859 | -57.36415 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6271fe31-b9a2-3edc-ba89-3ff0258f7971 | -20.92431 | -56.37008 | 2026-01-27 05:03:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5431b9b-8db9-3ae1-bcfd-d9a5671f6363 | -21.74475 | -52.75165 | 2026-01-27 05:03:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b8e6fb3-6d73-32cf-bd40-1e4334fa302b | -23.5956 | -48.34411 | 2026-01-27 05:03:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 282c3c57-22f0-303d-80b7-2215513bf54c | -22.87038 | -54.65848 | 2026-01-27 05:03:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7ffb602d-679a-3db9-a8f8-14d99d2dffaf | -23.59397 | -48.34386 | 2026-01-27 05:03:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a40ceb1-3ab3-34e3-95d0-d88920a84715 | -21.24194 | -49.37029 | 2026-01-27 05:03:00 | NOAA-20 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2379a5a6-50a4-3fd2-add5-f76956370fac | -21.74076 | -52.751 | 2026-01-27 05:03:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c04e350-a371-3ade-a866-e9f74e717134 | -23.60013 | -48.33693 | 2026-01-27 05:03:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e285dacf-15d7-3f92-9e1e-0d206980bee1 | -21.53949 | -57.52037 | 2026-01-27 05:03:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b316ab2-7da1-331a-b5ad-49d8cfcb3e2c | -23.00774 | -52.38843 | 2026-01-27 05:03:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 056b1ccb-d036-32fe-ba69-a58f864460c0 | -19.66594 | -57.30281 | 2026-01-27 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fdb8a153-911f-3c8e-bfb3-bc07c2ce6d96 | -20.61633 | -50.38564 | 2026-01-27 05:03:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 075b9897-08d6-3127-8678-f2fa7e875803 | -20.6206 | -50.38863 | 2026-01-27 05:03:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c8a3ac2e-5287-3cc8-b743-9c45a7f62727 | -23.59939 | -48.34457 | 2026-01-27 05:03:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14aa50ae-75ad-34d8-9ab9-0483a3d8f994 | -22.83772 | -48.65268 | 2026-01-27 05:03:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35df2bde-07f8-3ce9-891a-8ad8f4d322a4 | -22.73033 | -49.34286 | 2026-01-27 05:03:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b441d2ed-bddf-3a08-bdf7-4410f9f86b15 | -20.29999 | -57.82351 | 2026-01-27 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0e56d723-27ae-3698-ac35-516205e489fa | -23.34686 | -52.20495 | 2026-01-27 05:03:00 | NOAA-20 | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3460bfe1-3583-3cca-a11d-5bbe20fe5cc3 | -19.66262 | -57.30223 | 2026-01-27 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a86911ac-a58e-3070-b997-0609b77c8cd1 | -27.6277 | -54.76844 | 2026-01-27 05:03:00 | NOAA-20 | ALECRIM | RIO GRANDE DO SUL | Brasil | 4300307 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3b852d29-60ba-33ff-a32f-527969883f5e | -20.3033 | -57.8241 | 2026-01-27 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ef64f6c1-9d22-3d78-99d0-430b01d0dc0c | -19.65931 | -57.30165 | 2026-01-27 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 03df3764-f39d-32b6-9e50-ab8bb03082cf | -22.83808 | -48.64922 | 2026-01-27 05:03:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 05cd3ff7-ee0c-3be5-8fb7-4a7969dd949f | -19.72649 | -56.82737 | 2026-01-27 05:03:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7b736d0d-d328-3b36-bcda-c60c8ff43f98 | -23.59628 | -48.33643 | 2026-01-27 05:03:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cac832d0-85c6-342a-9879-f94b7e944d36 | -20.61601 | -50.38805 | 2026-01-27 05:03:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| af83e07d-19bc-3b17-ad6c-ce85d0660657 | -20.91758 | -56.36892 | 2026-01-27 05:03:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1449a998-c72c-3d76-a051-8843dc112158 | -22.83843 | -48.64575 | 2026-01-27 05:03:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2ff9b2c-5eee-3d77-bdbd-464e89750c48 | -20.30272 | -57.82778 | 2026-01-27 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7e0ef883-f7ee-316b-b585-c71cca84b9f1 | -19.66925 | -57.30339 | 2026-01-27 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8e771398-cdd1-33d0-8248-2aae6b3ce345 | -20.92038 | -56.37333 | 2026-01-27 05:03:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49e6a492-f7c8-30ca-be77-89dc1d7e3dfa | -20.2994 | -57.82718 | 2026-01-27 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dc8fb3d1-5a4d-38fa-aa57-fbac06e6755c | -22.83702 | -48.65047 | 2026-01-27 05:03:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db5abf10-66af-3ced-a91f-dbbb223c0ea7 | -22.83734 | -48.64704 | 2026-01-27 05:03:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b39dfd9e-9fa0-383c-915a-bb6fc588e71d | -19.66868 | -57.30706 | 2026-01-27 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 352c84ce-7ce0-395a-9941-39d3cdc56142 | -22.83767 | -48.64356 | 2026-01-27 05:03:00 | NOAA-20 | PRATÂNIA | SÃO PAULO | Brasil | 3541059 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13d15c5e-74da-3a2f-b2e1-350dea2872a1 | -20.92095 | -56.36951 | 2026-01-27 05:03:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cad9cdd6-4e1c-3917-8b1a-f4cf0427fbee | -22.7354 | -49.34326 | 2026-01-27 05:03:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91ef8bb4-a6db-33f2-b1e0-fbe994df4412 | -19.7246 | -56.8198 | 2026-01-27 05:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 94bdac7b-712a-3e2e-ac25-766e8320e1cc | -19.7246 | -56.8198 | 2026-01-27 05:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 64acdc6a-56be-3cfe-a07b-89e6dd3db052 | -19.7045 | -56.8226 | 2026-01-27 05:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 49.8 |
| afbf2397-39ab-33cd-8129-70f43f14aaba | -11.98728 | -37.74567 | 2026-01-27 05:35:00 | AQUA_M-M | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5906077c-477c-3d30-94b4-71631682ebef | -6.5631 | -51.1126 | 2026-01-27 05:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9b482f68-2f90-3c25-9a38-5d25332aac7b | -11.96815 | -58.07398 | 2026-01-27 05:52:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7ae5c35-47c7-3916-9a74-dd70628d3662 | -11.96198 | -58.07715 | 2026-01-27 05:52:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b97b3e2-3c92-3c23-b963-58f9ae1161ce | -18.8127 | -57.71634 | 2026-01-27 05:52:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 63c72128-aa09-36f5-a242-21de1fa2b015 | -18.8132 | -57.71106 | 2026-01-27 05:52:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9cdb0f9d-dea2-365e-b0b6-000c3be7d838 | -11.96766 | -58.07796 | 2026-01-27 05:52:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7a8e3d5-2842-3d7f-b81b-9a6a9cf64295 | -11.9615 | -58.08109 | 2026-01-27 05:52:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc7edeae-daea-35df-9298-51d193a615e5 | -19.10423 | -57.77293 | 2026-01-27 05:52:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 747c688a-6095-3127-a4c0-8b913d47c2c1 | -11.96246 | -58.07322 | 2026-01-27 05:52:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1ec0cfa-898b-349f-a864-54023d9c62ad | -19.72414 | -56.81971 | 2026-01-27 05:54:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 981ff2b1-03a6-301c-aab6-4563692369a3 | -19.71023 | -56.8245 | 2026-01-27 05:54:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 5efd7583-9527-3cde-8f9c-1602171d62aa | -19.71743 | -56.81899 | 2026-01-27 05:54:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| a1656714-f01f-3eaa-9251-aea47d6f8f72 | -19.71694 | -56.82523 | 2026-01-27 05:54:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| e7b4c8a5-899c-33c5-8044-8ccf579e4f80 | -19.721 | -56.82065 | 2026-01-27 05:54:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| b9e3d005-7170-368c-8859-ed452ae3d063 | -19.71428 | -56.81995 | 2026-01-27 05:54:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 0272bdcb-5cd5-3009-b9c7-be7a9dea04d9 | -19.71071 | -56.81827 | 2026-01-27 05:54:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| c85f2c1d-4b69-326b-8716-8e6324e7114d | -19.70647 | -56.81633 | 2026-01-27 07:16:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| e457c40d-e8cf-3f6b-a41f-8c82dc90b4de | -19.7045 | -56.8226 | 2026-01-27 13:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 62ee6274-b5f0-3bf5-a881-59430fac935f | -20.3291 | -57.8433 | 2026-01-27 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| d5a13152-b81d-38c9-9645-415588029325 | -20.3287 | -57.8643 | 2026-01-27 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 4446f4f7-5bed-3dee-92e5-099a57182eeb | -20.3489 | -57.8615 | 2026-01-27 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 35734b00-8189-3a21-bc2d-367860e651f9 | -27.77 | -50.38 | 2026-01-27 13:20:00 | GOES-19 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 106.0 |
| ba235e80-bcb9-322b-8feb-417761634799 | -27.7558 | -50.791 | 2026-01-27 13:20:00 | GOES-19 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 141.8 |


[Clique aqui para ver as próximas entradas](README5.md)
