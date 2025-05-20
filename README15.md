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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b39dbdb9-3c2b-3c89-8ad1-519b1e50c3ef | -9.18437 | -45.33342 | 2025-05-20 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8f8d4a65-9773-3c9e-b48d-c53542dd1bb8 | -10.63391 | -48.09502 | 2025-05-20 12:21:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 49672095-3564-30f0-969b-889e9d2aa66b | -9.57909 | -48.23384 | 2025-05-20 12:21:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4223720b-a9d7-3677-92c1-302faaee81db | -10.23851 | -47.59021 | 2025-05-20 12:21:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7654db96-9096-3cb4-bb32-afe68b581c83 | -8.23153 | -49.9572 | 2025-05-20 12:21:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 902410cd-c9fd-3014-ad2a-d789b6e903cb | -10.60665 | -46.97151 | 2025-05-20 12:21:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 04ae4c5d-a05f-3438-abef-f9566b9673a2 | -14.50418 | -43.7695 | 2025-05-20 12:21:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 75db7d8b-9a4f-323a-9372-fe86dd6a4ccb | -11.86936 | -44.38188 | 2025-05-20 12:21:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 43c2077d-add0-3d26-8bc4-3193060ee616 | -11.87994 | -44.37332 | 2025-05-20 12:21:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 56dd218c-9957-3b96-a1f1-891600a1f917 | -9.01579 | -49.16812 | 2025-05-20 12:21:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a6dd70af-9b42-3c61-9127-0a160b127478 | -8.74995 | -49.75216 | 2025-05-20 12:21:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| fbbf6452-74ad-306f-8414-78c10a2f14ae | -13.66232 | -45.26393 | 2025-05-20 12:21:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 60044cee-3dd8-324a-89cb-103323f3e329 | -10.23707 | -47.59985 | 2025-05-20 12:21:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2a80ef68-8fb6-31b2-8bca-8867c26a3cea | -12.69403 | -44.94338 | 2025-05-20 12:21:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ba4ba10b-2139-3a57-9111-7af8bc4e0beb | -11.69255 | -47.80061 | 2025-05-20 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| cdfd7e97-b078-3361-bef7-8d9db47c8140 | -11.68484 | -47.7896 | 2025-05-20 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 25bfd8cc-af24-381e-95dc-1de180147bba | -14.61191 | -48.86773 | 2025-05-20 12:21:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1a97635c-30a6-32d2-b5a7-91a5232632c1 | -8.7464 | -49.74545 | 2025-05-20 12:21:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6a800777-ea63-3375-a4b7-1ea6dfb07b8e | -9.19322 | -45.33467 | 2025-05-20 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 968eb9b3-9403-3336-a3fa-74a8dce68184 | -8.54122 | -45.89435 | 2025-05-20 12:21:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d0c78cf8-0171-3175-a103-90e93da192a4 | -10.65208 | -47.04071 | 2025-05-20 12:21:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a9682be2-8945-37ed-82ec-9b811381172f | -8.12323 | -49.24699 | 2025-05-20 12:21:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fd8d0238-c35a-3ddc-ae72-d0d2d0a46295 | -11.09471 | -42.15646 | 2025-05-20 12:21:00 | TERRA_M-T | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a70a4eda-828f-3c7a-9d32-1fc38f46c006 | -11.84348 | -49.64461 | 2025-05-20 12:21:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0c975c9e-8a14-36d0-b7f9-37b305de2272 | -8.75205 | -49.73883 | 2025-05-20 12:21:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3162049c-ca58-3782-803c-0b8f8e3096ad | -10.63542 | -48.08492 | 2025-05-20 12:21:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| f2e268c7-265d-3cac-8194-3a7eb9784d91 | -10.57355 | -44.76538 | 2025-05-20 12:21:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c1c9865a-6ae2-3ee4-bad8-8c0a14ac889f | -9.25758 | -47.91795 | 2025-05-20 12:21:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| ed076b3c-2273-3fea-adcc-ec9849996b2c | -9.19194 | -45.34358 | 2025-05-20 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| a7787d3e-6a75-39f6-8d6c-78a52dc35b71 | -14.79477 | -42.70186 | 2025-05-20 12:21:00 | TERRA_M-T | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c6c5a503-7ade-3a19-8bf7-9c8098dbd92a | -13.5756 | -47.35621 | 2025-05-20 12:21:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3a9b84c5-be65-3de0-a1ab-49ef04e608db | -11.53767 | -47.78099 | 2025-05-20 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 05607892-56c3-340a-b345-101496bd18e5 | -13.68788 | -45.412 | 2025-05-20 12:21:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 115d4470-2bbd-34fa-819e-a0a251db30f7 | -12.33918 | -49.9471 | 2025-05-20 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8963f223-f9b3-38ac-b134-86a5da845cfa | -10.65071 | -47.04999 | 2025-05-20 12:21:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 70a3d21d-f98b-395a-a273-ed8b4840e5b3 | -10.39636 | -47.02218 | 2025-05-20 12:21:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 05205d47-a76a-3382-bc62-3de6ec130de5 | -11.52936 | -47.78294 | 2025-05-20 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 96e2b13a-a814-3336-99da-af4bf6c1acb2 | -10.24768 | -47.59164 | 2025-05-20 12:21:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| f4581806-3c6a-33ea-a5b2-e30fe547f6f4 | -12.34553 | -49.9734 | 2025-05-20 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 71342b15-8f58-3ad0-8cb6-4f743b7fd7be | -12.10916 | -49.31812 | 2025-05-20 12:21:00 | TERRA_M-T | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 5fe83864-4538-37c9-a183-50801ebda415 | -11.97126 | -49.68306 | 2025-05-20 12:21:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 36788b98-1611-3a6b-a615-51201bbb3a6e | -10.23181 | -48.05984 | 2025-05-20 12:21:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 13774967-e3f0-36af-bd42-9b265d6bd216 | -10.52417 | -47.59289 | 2025-05-20 12:21:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4d3db1e2-c7cb-35ef-ab99-5fc967c3bf82 | -8.34999 | -45.1774 | 2025-05-20 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9a1ba8c4-3991-3257-bb64-549ceac29338 | -11.6954 | -47.78141 | 2025-05-20 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 79ca78ce-b9d9-343e-9268-82593f8ef078 | -10.64034 | -47.05797 | 2025-05-20 12:21:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9cc10616-87da-3180-8a80-efac964918d0 | -12.34943 | -49.94868 | 2025-05-20 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f6f042ee-38b3-369c-b56c-6cf8e9eaeb2c | -10.64933 | -47.05927 | 2025-05-20 12:21:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3561d8ee-f736-36d3-b284-017cc7730cd2 | -11.88706 | -46.921 | 2025-05-20 12:21:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 38f66eaa-1d80-3c1d-af7b-9927844f64a6 | -8.35756 | -45.18754 | 2025-05-20 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2b6075da-0fa1-3dae-a51f-9882686028cd | -12.33723 | -49.95946 | 2025-05-20 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d0ef9d15-debc-30a9-98b2-490003a7647a | -10.60529 | -46.98077 | 2025-05-20 12:21:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4b611828-b2a7-30e6-b6a4-a11c4eb3b345 | -11.7921 | -44.27428 | 2025-05-20 12:21:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f507c2bb-68c7-351b-9271-c2f58868d266 | -13.57426 | -47.36528 | 2025-05-20 12:21:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 755329d2-f5fd-3e24-b87c-3f87681732aa | -11.68341 | -47.79921 | 2025-05-20 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ac8214b2-a36e-3d8f-8d12-dfd1157255eb | -11.52793 | -47.79261 | 2025-05-20 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 08307b35-227e-3d29-b906-f16032feaf42 | -10.52561 | -47.58322 | 2025-05-20 12:21:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a75ed49f-9c28-337b-acb0-8ac1674fb75e | -12.34747 | -49.96106 | 2025-05-20 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 402.7 |
| c948a972-e7ea-38ef-97e3-8cab0d4ddd93 | -11.69398 | -47.79101 | 2025-05-20 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| afac5cb2-8c5a-3400-9f65-5e8666361d8b | -11.8786 | -44.38315 | 2025-05-20 12:21:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| db5a33e0-5b6c-3838-8806-07a418c97424 | -16.1451 | -45.94658 | 2025-05-20 12:23:00 | TERRA_M-T | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 74f1bb66-7706-3f42-be71-8596a18ef36c | -21.39298 | -44.62725 | 2025-05-20 12:23:00 | TERRA_M-T | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 832b123a-1b92-3525-a907-29b0ce10d739 | -17.663 | -46.67944 | 2025-05-20 12:23:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bc99e736-7996-386d-ae4e-d657bc0b8d5b | -16.47294 | -45.01739 | 2025-05-20 12:23:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b351ff78-a8cd-3157-80a6-0b727396bcc7 | -21.4389 | -45.1645 | 2025-05-20 12:23:00 | TERRA_M-T | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 4e353e9b-7ed4-394c-97a1-59f21b9df407 | -21.22079 | -48.6047 | 2025-05-20 12:23:00 | TERRA_M-T | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2aad557a-ec55-37f2-af2f-b8c55535becc | -21.40386 | -44.27007 | 2025-05-20 12:23:00 | TERRA_M-T | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 7c9ad41a-1d79-3418-89a4-ccf8be45ddf6 | -17.50839 | -46.73602 | 2025-05-20 12:23:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9926514c-c10d-3997-b476-34ed3b3c4456 | -11.6999 | -47.7909 | 2025-05-20 12:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| af25203f-dd05-3255-901b-a7db3de9ceb1 | -12.4798 | -57.2063 | 2025-05-20 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 178.9 |
| a24d1e4a-6cf4-3846-b3d9-0c91e65ae8f3 | -12.3522 | -49.94 | 2025-05-20 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 97bc79ff-1b32-3e2e-9cf4-994ec9ca5fbb | -12.461 | -57.1879 | 2025-05-20 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 186.0 |
| 8b6049cd-c34d-3f94-be88-57436e0e8d00 | -12.3327 | -49.9641 | 2025-05-20 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 258.2 |
| 9e53f260-5b5f-3ebb-b378-c1c619425255 | -11.8863 | -46.9179 | 2025-05-20 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 0bea67ce-d09a-3062-a62b-5ba196ae1c60 | -12.48 | -57.1863 | 2025-05-20 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 540.5 |
| ff67888d-7cb8-37d6-81d4-0380bcb29631 | -12.3519 | -49.9617 | 2025-05-20 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 2b5b204a-3636-3d42-84d1-73624e479026 | -11.8859 | -46.9404 | 2025-05-20 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 194.9 |
| a4d721e5-947b-3d42-9e78-725755987522 | -12.4798 | -57.2063 | 2025-05-20 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 48aa8e22-04ed-3858-a1c0-f225a00b32e3 | -12.48 | -57.1863 | 2025-05-20 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 632.6 |
| ef1b5170-eb5e-354e-82ed-c379d91462d0 | -12.461 | -57.1879 | 2025-05-20 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 5f6dfcf5-a162-3702-bc89-f0739ab11116 | -12.3324 | -49.9857 | 2025-05-20 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f4d12094-d7b9-3c56-9eed-e902f1291b0d | -11.8863 | -46.9179 | 2025-05-20 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 233.6 |
| 27d2c71b-664d-39c5-a0b5-95328875da39 | -11.6999 | -47.7909 | 2025-05-20 12:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 4c96a533-9a67-3da3-915a-2c4e0a82886e | -11.8859 | -46.9404 | 2025-05-20 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 192.4 |
| c0844845-c61e-3d19-89de-251f2f5335c9 | -12.3519 | -49.9617 | 2025-05-20 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 229.0 |
| f1312d12-b0f0-39d8-a49f-6301e10f4954 | -12.3327 | -49.9641 | 2025-05-20 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 67b3fd15-b0da-3743-a2b3-d221ec5d2978 | -12.4798 | -57.2063 | 2025-05-20 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 136.8 |
| d8214554-d058-3528-9e0f-6e99d94ef229 | -12.3324 | -49.9857 | 2025-05-20 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 51a38acd-e541-3871-ac30-fc882322396a | -12.461 | -57.1879 | 2025-05-20 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 65da5634-e056-3718-8a05-ac23b63156b9 | -12.3519 | -49.9617 | 2025-05-20 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 33ecac70-3fc9-3a80-9688-bb7e9360218d | -12.3522 | -49.94 | 2025-05-20 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 93e4b351-b757-3dc5-beff-a2cf823f8322 | -12.48 | -57.1863 | 2025-05-20 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 578.0 |
| 8240f421-a475-3691-8f9f-f7287ebac0e4 | -12.3327 | -49.9641 | 2025-05-20 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 311.4 |
| 89ade9c7-1180-3ade-a138-59ad68aa4776 | -11.8863 | -46.9179 | 2025-05-20 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 280.0 |
| 11a85356-2c0b-3567-abeb-80b5b296f223 | -6.204 | -43.3241 | 2025-05-20 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 583ed38c-bd5a-32eb-ae93-4eb51420eafc | -11.8859 | -46.9404 | 2025-05-20 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 248.5 |
| 14537e25-3fbd-38a4-ab67-8e695ca059b2 | -11.6999 | -47.7909 | 2025-05-20 12:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 95baa3b6-f9b7-3a44-a083-16f60c08fdde | -11.8859 | -46.9404 | 2025-05-20 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 66cb7f7e-4196-3621-8723-77f2d7a3a0ce | -12.3519 | -49.9617 | 2025-05-20 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 361.8 |
| 0159ead6-2a91-399f-9f8b-2d75046db998 | -12.4798 | -57.2063 | 2025-05-20 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |


[Clique aqui para ver as próximas entradas](README16.md)
