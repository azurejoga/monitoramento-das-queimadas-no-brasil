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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8878bb5-7d86-370b-9a6f-5949b0bc5571 | -10.4975 | -43.4108 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06dd8d47-97c9-3063-91a8-923d4fed5be7 | -10.60266 | -47.39732 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f96034e9-8025-30f5-955b-13d3ff7c3e63 | -6.31435 | -40.94376 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 26e1b370-eba6-3558-b3f6-581f02ad282a | -3.47255 | -51.66658 | 2025-10-17 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c804f9b-b92d-3ddd-8595-07c0ba2ff6e9 | -4.74088 | -44.94204 | 2025-10-17 04:19:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7766bfe7-bed6-3cb6-9d84-9356b451b399 | -6.37373 | -41.47417 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9753d392-c34a-3276-a7e8-a044ad5cbe9e | -4.83592 | -41.47021 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a7bcb317-da24-31e3-912a-7dbd4b284de1 | -10.27911 | -44.04285 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a85545fe-580e-3a8a-a7bc-52a436d44329 | -10.51072 | -43.41649 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24afdc7e-5433-371a-b0ba-f29ec7a4688b | -6.29125 | -42.97864 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85e26581-49a6-3124-be68-6cbc1d778bb1 | -6.16424 | -40.89217 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c1a0808b-989d-3307-8704-c10a36c7f79d | -8.26265 | -44.08992 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 853b9614-f5c1-3d2f-9483-6be3f0e7a1e5 | -5.99056 | -44.15545 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31f59a50-25b7-3228-92fd-bcefddaf4dc9 | -5.46111 | -43.46767 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fca67c89-ddbf-3759-82d8-d7ccd1af2ed5 | -3.84485 | -47.06502 | 2025-10-17 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3bb7020-a83a-38da-a582-2fa6db469fde | -10.57743 | -47.42374 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4507e6b7-5d16-341e-ab05-a0a739b70897 | -8.25486 | -43.3349 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 43b62a73-4226-3c55-91fa-f7bd4f69854d | -7.08889 | -44.26779 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4b6f769-783a-3585-bcdf-f190c62d9788 | -10.50494 | -43.40812 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c332dee7-574f-3521-98b6-75e66e430980 | -10.11946 | -44.55367 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 801a2279-c0eb-3a9e-95c6-13f7a090a52a | -10.81125 | -43.93634 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98e5e5a0-3eb0-3896-ba5a-e05933e06f18 | -9.03223 | -47.71593 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06b064e8-0763-3400-b041-42c73054efd7 | -9.14733 | -46.65079 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 30cd3d25-8cb5-3d70-bb54-fc7e658ce044 | -7.19468 | -44.00265 | 2025-10-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbbc598c-f065-395f-9331-9d8a6bd40833 | -8.38953 | -46.31948 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 66f7ea0f-7da3-30bd-a39d-d99551b4b62a | -10.2976 | -44.03457 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d75ec01a-f97d-3d02-8e46-ba339a20610d | -6.30636 | -44.72761 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c01a008-29d3-33b9-9ed1-4c9df890e7b1 | -7.33017 | -44.15989 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cad461cd-fa69-3a86-bcc6-7e6ebf64c88e | -8.45604 | -41.26335 | 2025-10-17 04:19:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4764d7e0-d6ad-301a-90c5-ec37b1ccb842 | -4.72108 | -46.44955 | 2025-10-17 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2462e5d5-0367-38cf-b45b-2d048098f653 | -10.50616 | -43.42343 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1bc28146-43bd-318d-a655-779bbfbd8582 | -10.08847 | -45.34492 | 2025-10-17 04:19:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1f48459-bc45-32a7-b72a-f2ec3c71fdb1 | -5.27575 | -43.25876 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d846747e-3dc3-3909-997d-7ae2a5c913ab | -7.03175 | -41.82307 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3e1858e2-22f9-349f-88f1-6ffe28bfaa45 | -7.35688 | -43.85549 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6001cb3e-c147-307f-9335-5fa2d1c1104d | -9.29404 | -46.90187 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f2fce8e-56c1-37d7-bad4-f83261018606 | -11.40882 | -44.20744 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 85ea2d48-c6b2-35da-9b97-beb4526e65c3 | -9.97716 | -47.00888 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 84d7554c-f2de-31c0-92ce-10c69ab69049 | -7.90338 | -44.98169 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e93ad56-7149-3359-a1e5-26f7f74dfd6b | -4.14133 | -47.65702 | 2025-10-17 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8fef6af-082a-342b-9a38-8de1c2bffb38 | -10.50271 | -43.42291 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2241ffdf-2a15-3570-aa22-40a88ef0161d | -8.50862 | -44.5696 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b43caed8-0980-3802-9308-e8e08901b4e5 | -7.74479 | -42.50345 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c890504-47d5-32d1-b2df-29ceb52821fd | -10.59707 | -47.38881 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65a33a9c-363a-348f-a90d-bed8934385af | -4.4418 | -49.69252 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5511584-8773-3170-8188-99751d410cec | -11.52904 | -43.49395 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 063f73e1-6bbf-3774-aa9c-b06b9d107432 | -9.92299 | -45.33999 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a26646ed-dcc8-351b-8daa-3f26c6ab39a7 | -9.0997 | -46.66894 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d35d0131-0ace-3fbc-b849-814f9b808408 | -11.47873 | -44.28156 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e1bd308-2ecd-3c6c-ba5f-c8d49e11cb65 | -9.83853 | -49.30967 | 2025-10-17 04:19:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72648b64-43c1-3417-be65-2d7e1b1f97bf | -5.78398 | -42.46465 | 2025-10-17 04:19:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 70eabbaa-1bc8-3b96-9b1d-ddfd15172368 | -6.33235 | -46.32683 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e325bb43-0d88-3a6a-ac5f-102237186b0b | -8.20654 | -43.96922 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eb4fcce-71b0-36d8-9b0a-0b48e039e206 | -9.24832 | -44.35905 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8c97275-e047-3cdb-8d06-d0c7bde8a4ac | -5.4607 | -43.51421 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f6c96b4-554a-3925-8038-9c0334c22d1f | -10.11135 | -44.6282 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1f470e8-d8ba-34f6-beea-dffcbe61503a | -6.78665 | -44.52817 | 2025-10-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68a4c26a-de45-378c-a556-a7588f6b04e7 | -5.84055 | -45.5419 | 2025-10-17 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0807e80a-740a-3519-a52e-4176b1ae7aac | -10.12348 | -52.3413 | 2025-10-17 04:19:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e4a279b-c94d-3a5b-b193-937436797b85 | -5.72239 | -43.82267 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6878f8c-5851-3b69-b93d-03be21c0c5ab | -3.51172 | -52.48796 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 15daf8e9-6071-3ae1-9f6a-eacff89d9a0b | -5.32966 | -42.93196 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0375570a-5164-3bb1-8a48-a4f10e7b1262 | -2.87003 | -50.72371 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbb5d369-fc56-37f3-b445-d2ae2e7c3aee | -10.57283 | -47.43058 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e539ae5-6ba9-3f10-b5e6-308fcd8209c3 | -6.1256 | -41.75624 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 498e1391-8316-3efd-bc4a-213974724c4e | -10.27684 | -44.03513 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29195714-3609-3602-9f1d-b78fc790fa37 | -10.15963 | -44.53436 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e343cbb-96c6-32ad-8d50-1af1d35dd9aa | -6.91823 | -41.6601 | 2025-10-17 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 773fe94a-94fd-3ce3-b87e-b529a0f17d41 | -5.46009 | -42.9478 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b64bc463-38ba-30e5-bc26-a4393a8fb494 | -8.61231 | -40.19674 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7ceeac0c-fac9-3011-80fa-a51f605c5252 | -5.09319 | -45.42631 | 2025-10-17 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1133b735-46e3-3d40-a943-67a8657e3b78 | -11.48587 | -44.17804 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 271495d9-e9ff-374f-832f-3f9eaaac0721 | -5.13695 | -45.06129 | 2025-10-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e63b2340-ed1d-3a7c-aaf6-da950ea20352 | -7.90125 | -44.8396 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a483a86-8cdd-374a-9fd9-42ff90a60d33 | -5.84986 | -43.87786 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a57dcffa-54e8-3104-a734-a752d50ae6bc | -6.74473 | -46.99831 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f6f7d50-09d6-30b2-98f4-b82287108059 | -6.6041 | -44.7995 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f1a3580-e732-3b6f-b834-0154f9330102 | -11.40599 | -44.20325 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d860f63a-883c-3b1b-9c1e-bce0b33773da | -11.46683 | -44.25776 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7f2abff-b1ee-3932-8085-3c871d291619 | -6.37661 | -44.71035 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a178c5ff-b3d1-34a6-9453-ad7f68de35e8 | -2.87838 | -50.7298 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d936ae6-af0a-3bb2-b1c7-e0951a002910 | -10.12169 | -44.56123 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7dafd47-cfe2-314b-9150-eced78bc46c5 | -8.40373 | -46.23043 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a27d7d17-93c0-3e17-92a1-774dd4b2efa8 | -4.81364 | -45.73152 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c657122e-9653-38ca-b997-f33e751fb6af | -7.50082 | -46.64341 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cc9484d-35a7-3640-8339-2d9da3e412e9 | -5.80977 | -43.07877 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0ded51ad-e777-358b-9769-1f05275203a6 | -11.39194 | -44.20482 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cbe82c9-7c88-378c-b7f8-879133e20a29 | -6.74799 | -44.38073 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41e28208-fd7f-3f58-a2ad-a3cd9706259d | -8.72725 | -43.8745 | 2025-10-17 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 191736f1-1705-326f-b894-228930d24380 | -9.24445 | -44.36207 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbeeec2f-c53e-326f-952b-75eb35fabf40 | -3.53002 | -50.30727 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7dcc3e6-b9c1-33b7-b44f-42cb245d0027 | -10.01528 | -45.63968 | 2025-10-17 04:19:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86a02e7e-2a5c-3770-889a-dceaeae2cc9d | -10.42896 | -45.01667 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65f172f0-7226-3b75-aa49-7134e6501fea | -4.64321 | -50.49376 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a1ee5cf-523d-3182-9428-d8ce6b4203fa | -5.21261 | -46.19085 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 828c6313-3182-3cf0-96c2-18ccb48b4307 | -10.2416 | -49.88771 | 2025-10-17 04:19:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eeafaf0c-e65f-3d81-accc-48d0b966e972 | -5.14018 | -46.28951 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46857114-0cde-359a-88ff-4842a7ef7e48 | -5.84932 | -43.88132 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecf23e97-77da-3691-845a-25a946e03d3b | -11.46481 | -44.04233 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 160dd1e0-aada-3197-9800-f88feb2d3508 | -10.26791 | -44.04854 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README56.md)
