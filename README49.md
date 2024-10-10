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
| 928eb82a-fe2a-33d2-abff-9e2979ffb76c | -6.92856 | -47.7116 | 2024-10-10 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acd080b1-9d35-37df-adea-0449ba1e9a37 | -6.928 | -47.71474 | 2024-10-10 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec955896-e237-33f3-8ae7-22162ca519ab | -6.92744 | -47.7179 | 2024-10-10 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5affb0e5-c514-304d-ba26-9dd2ab563305 | -6.92688 | -47.72112 | 2024-10-10 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2d3490d4-51ac-3b41-b658-1f129a0062ad | -6.92628 | -47.72451 | 2024-10-10 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b8e7d19e-9496-3617-b816-b94ec6087ea4 | -6.58176 | -47.71449 | 2024-10-10 03:55:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9fd9cd5c-7caf-3a2a-95f0-c963c11d2b10 | -6.58118 | -47.71775 | 2024-10-10 03:55:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8c4e19a-55a7-3813-b61e-c52320ebd64b | -7.02701 | -47.37036 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a8df6f0-363f-3d8b-b0c4-4b5b971eb9a7 | -7.02641 | -47.36923 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cddb2ad-e6e5-3db5-958d-57f2cea2e761 | -7.02585 | -47.37249 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25683bad-b053-3094-b454-e197b4f1377a | -7.02581 | -47.37698 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 892712ca-8a28-346d-819b-23e952b7ef01 | -7.02228 | -47.36681 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1474b717-1a1b-3a0e-8201-0d132d105729 | -7.02169 | -47.37008 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff438cb2-5b08-3552-af8a-6832aedb2cb5 | -7.01379 | -47.19702 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99e83833-8bbd-3bfa-90b3-e964cf6355a1 | -7.01274 | -47.20299 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dede7d7e-3e46-3093-89be-b55628722bb9 | -7.01059 | -47.21526 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41eabe82-a16c-3d13-a32b-ce9c60613388 | -7.01002 | -47.21848 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b65be73-17f9-3f5f-9c36-3453e3510a4b | -7.00864 | -47.1962 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 463bf584-bdbe-3856-8010-80987be59ffd | -7.0081 | -47.19922 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a3c8dfe-7750-30a6-a8c0-92467e01a0b4 | -7.00757 | -47.20225 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3fbe18b-c489-352f-9ab0-053d50ecc4a0 | -7.00314 | -47.22741 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d93f9744-2976-3535-b898-928f270c421d | -7.00258 | -47.23054 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62fd9f0c-8aa3-3cfd-926d-e7e237508e2f | -7.0024 | -47.20148 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bf06560-660c-3ed8-ac0a-a28da2428069 | -6.98171 | -47.37936 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8c0e53d-e35e-31bd-8eb5-6310e1bc54db | -6.98115 | -47.38254 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e4ea0e3-2775-3916-9182-b534c1dfdc67 | -6.98058 | -47.38576 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e8b5684-f76f-393a-af6c-ab2d115fb75b | -6.98001 | -47.38897 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf7dd2f0-03c4-34b4-b4ce-4381d6747bbb | -6.97645 | -47.37873 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b68dc42-ddad-3c4f-b629-b9a65234cf2a | -6.97589 | -47.38188 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d6b7d222-16f0-39bb-94d7-cfd5d5ad989c | -6.97534 | -47.38501 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cda09278-60d9-38b9-bf71-7bb3dbec04c4 | -6.84504 | -46.9251 | 2024-10-10 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ededff8-e405-3d99-bf92-044e0d92e019 | -6.84452 | -46.9281 | 2024-10-10 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29f0cdac-60bd-33b0-a02f-4a758c61dcaf | -6.67245 | -47.11117 | 2024-10-10 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 622d8c16-ee7b-3b9b-9bd8-ddde28faf86d | -6.66783 | -47.10733 | 2024-10-10 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6580cd84-bda5-32ad-bff5-b0ef18d7655f | -6.66728 | -47.11041 | 2024-10-10 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf115b97-6c13-33a1-b36e-bf00169ec656 | -6.66672 | -47.11353 | 2024-10-10 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e44104dc-5149-32bd-8e73-5251d510d4a3 | -9.22225 | -47.56213 | 2024-10-10 03:55:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab7c1370-2903-371f-8db0-d52fb5deabcb | -9.10803 | -47.65317 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae3495d1-40d1-313b-a9ad-c6878932aede | -9.04591 | -47.81932 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2dd48c8c-7534-397d-b91f-dbb32f25484e | -8.99015 | -47.7353 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d353308d-5750-3e9d-89e5-68d83e828158 | -8.9896 | -47.73836 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f409b3c3-e406-3496-b341-90d7b424d0f9 | -8.55193 | -47.82465 | 2024-10-10 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0666e59-f621-35b6-bc60-a0fc121d3a0e | -8.49739 | -48.63426 | 2024-10-10 03:55:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e088ad2f-95a4-3835-ba4f-aec1539712f8 | -8.49673 | -48.63787 | 2024-10-10 03:55:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 172d2d7b-8f74-39f9-bda2-61633c86be07 | -8.37271 | -48.19062 | 2024-10-10 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02b3c374-5104-32f5-b83a-72eb178ef259 | -8.27035 | -47.85534 | 2024-10-10 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d210853-6766-3eae-b87c-cdac8ae5e407 | -9.86895 | -48.26277 | 2024-10-10 03:55:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d210d1f-122d-340f-ba9e-16cec45182c6 | -9.86834 | -48.2661 | 2024-10-10 03:55:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5711d95e-f588-3047-a756-1a8135d05dd1 | -9.8636 | -48.26233 | 2024-10-10 03:55:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c78317d-977b-36e2-9c7a-02ebd57fea25 | -9.863 | -48.26559 | 2024-10-10 03:55:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06a23120-44da-3d6a-af86-4de76adc561a | -9.37061 | -48.80427 | 2024-10-10 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5fbd6541-9a7d-3447-ad6e-38ce5e9994b9 | -9.36531 | -48.8032 | 2024-10-10 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fcb78491-4995-386b-a8aa-9332b5087aa5 | -9.36512 | -48.80325 | 2024-10-10 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 11e9f616-17d9-3b53-8a8e-7360793147ac | -9.36461 | -48.80687 | 2024-10-10 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6f5bd44d-a74a-3a0e-af96-b03d1b4b5dac | -9.36445 | -48.80692 | 2024-10-10 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8984ac7f-307f-3cf6-a823-d4c88be1566d | -10.58129 | -47.8953 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4765a8c6-c112-36cf-9f22-91653ec6bf68 | -10.57813 | -48.02732 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 34ce989a-9ab8-3b0a-a4aa-0c39f5e040f4 | -10.57757 | -48.03032 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a2dcb55-ea51-3497-821f-3b845333e493 | -10.57699 | -48.03352 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1b32393c-6687-3eac-a7ab-6a881d7e3044 | -10.57624 | -47.89429 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 077b9be1-bd7d-3e1d-b411-2dad39abcdf9 | -10.57357 | -48.02332 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7a89586-6916-374d-8ec1-da536f63ed07 | -10.57303 | -48.02627 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 07a477fe-f8d6-3b1d-9842-7f9b0e9573ea | -10.57248 | -48.02928 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c4dbbd57-8f44-35f6-8402-0333d3c74e53 | -10.57189 | -48.03248 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c279b231-d420-3d5e-8fde-304b8fd3fd49 | -10.57129 | -48.03576 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 826a6d3b-1750-3226-af50-b183b38700dd | -10.5679 | -48.02545 | 2024-10-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fad5a3ca-135f-3a4c-8dde-8ef8d0760eaa | -10.05319 | -48.75051 | 2024-10-10 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0857d2e4-c778-3c68-b162-5b19c34b809b | -10.0477 | -48.7499 | 2024-10-10 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78350fab-5c81-3df5-a1ac-09c0e330785a | -10.04703 | -48.75344 | 2024-10-10 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8150beba-aea5-352a-ad33-7611bfc755cd | -10.0347 | -48.72996 | 2024-10-10 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e11c597f-9011-3035-9346-c2376ff08ce7 | -10.03402 | -48.73352 | 2024-10-10 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73026b38-5dd3-3855-b4a4-b71bca8ae10f | -10.01204 | -48.84869 | 2024-10-10 03:55:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 52a1f446-267b-3a04-9772-e98353482906 | -10.01109 | -48.84855 | 2024-10-10 03:55:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cee05a6f-75e0-36e0-a5da-17ffa78659b9 | -10.00657 | -48.84782 | 2024-10-10 03:55:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6f1df05e-c7b7-33cd-a744-48f94bdc9af0 | -10.00589 | -48.85135 | 2024-10-10 03:55:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e3e19f0e-c7c4-38a9-b788-9715a6b30591 | -10.00562 | -48.84766 | 2024-10-10 03:55:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f4af1450-7419-3de6-97d0-0d06065cc037 | -10.00496 | -48.85121 | 2024-10-10 03:55:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7b221ff4-45eb-372c-9992-639f2468f641 | -10.73046 | -48.72377 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 359d086d-6833-3fef-945d-32a2a166758a | -10.72514 | -48.72268 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1c04562-25ab-391b-8b11-a3d4b92bce2c | -10.68123 | -48.73377 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cad1035-83db-313c-a7b3-eafa695ebfe6 | -10.67948 | -48.73005 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45aa2d23-5675-348c-aca1-8b338cbba9cc | -10.67724 | -48.7254 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f53664be-e7d3-3e59-8409-818041488287 | -10.67481 | -48.72556 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95bf820b-1d56-3df8-9b7e-1b0be4a9f8a0 | -10.67247 | -48.72131 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c67832dd-d1c4-3b89-9c8d-170a288d47fc | -10.67181 | -48.72485 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79ab1b88-7721-3802-bb18-899c96f3e7d5 | -10.66939 | -48.72495 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8caaa3aa-1b1f-3147-917e-838be9c687d7 | -10.61557 | -48.29642 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 847af81f-5028-3da9-b4e5-adcdca7591bf | -10.61035 | -48.29554 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 294e7d99-a474-3950-9d44-498b6ce85e9a | -10.60976 | -48.29871 | 2024-10-10 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21c1aa01-1528-38e2-bbe8-dcc1544e5a7a | -10.60571 | -47.70602 | 2024-10-10 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c0e73636-b11c-3b43-9e0a-fe527d69c635 | -10.60517 | -47.70896 | 2024-10-10 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5b1fd2f6-11dc-3fa1-83a8-4ea69ea2a316 | -10.60125 | -47.70218 | 2024-10-10 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cfc378f-3ccf-37c5-826b-c14312c6db32 | -10.60071 | -47.70509 | 2024-10-10 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 511f5090-0c49-3c71-aafd-30523f070614 | -10.60016 | -47.70806 | 2024-10-10 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e445988-a2bc-3cd3-b898-b7dbf6135c82 | -4.60288 | -48.06056 | 2024-10-10 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 984c79ea-ca5b-3d7a-832f-e6a0b29eb86d | -4.60222 | -48.06438 | 2024-10-10 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d957bd4d-9582-333c-aa44-bbc6551f6e6a | -4.48123 | -48.10811 | 2024-10-10 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 175aeb1b-fcd4-3b32-81b6-7026051a6029 | -4.48056 | -48.11198 | 2024-10-10 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f7ed47e0-5e11-304a-ba0a-7f433428f07c | -4.20761 | -48.13937 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b16f7d8f-be57-3a14-8d36-781512283df5 | -4.20667 | -48.13626 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README50.md)
