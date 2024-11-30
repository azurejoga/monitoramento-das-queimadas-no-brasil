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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd31a183-3992-307f-bb67-ebbb44beb37f | -3.22741 | -41.07906 | 2024-11-30 12:14:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 19.4 |
| dbef1e79-d74a-39fe-9de3-ab8f4ad37a50 | -7.58869 | -37.83118 | 2024-11-30 12:14:00 | TERRA_M-T | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 11.9 |
| dfde647a-9e75-3331-b084-c419452d5301 | -4.88314 | -41.30577 | 2024-11-30 12:14:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 33981094-7a6b-3b71-92e7-c33b114c503c | -3.62835 | -42.00099 | 2024-11-30 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 37.1 |
| b4f04f3a-0e19-309c-81c8-8b6c3c3bf180 | -7.04806 | -41.52648 | 2024-11-30 12:14:00 | TERRA_M-T | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7aa52397-deaa-33f9-9235-5bfe29bfaec4 | -3.35559 | -42.08814 | 2024-11-30 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 74fe347b-898f-3d15-b383-43e161526a78 | -3.74704 | -42.25883 | 2024-11-30 12:14:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 0ce8cb6b-d1de-3d5f-9758-51bc583cd420 | -3.91293 | -42.38609 | 2024-11-30 12:14:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| fe69f5ba-a765-3dc1-8d55-b0cc6c47b343 | -3.01074 | -43.99199 | 2024-11-30 12:14:00 | TERRA_M-T | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 861ac29b-1eff-3786-bf37-a9f884ca7f3c | -7.59862 | -37.83261 | 2024-11-30 12:14:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 310aef2d-e751-3c0e-88e5-73f0d2f80a54 | -3.61841 | -42.73732 | 2024-11-30 12:14:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d7922eb2-b3cd-3331-b1f6-2964b0323d26 | -3.5253 | -42.12483 | 2024-11-30 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 2c9e47f9-1b79-3267-b4af-41f1fa4ade26 | -3.56094 | -45.16431 | 2024-11-30 12:14:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 0ad60993-c70f-3f2f-b09c-5e83ed739e8b | -5.20428 | -37.97678 | 2024-11-30 12:14:00 | TERRA_M-T | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| ade40398-ffb5-38f3-98d4-290b21021417 | -5.20438 | -39.01099 | 2024-11-30 12:14:00 | TERRA_M-T | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 19.6 |
| cdfc9f10-2d5a-3e40-ab38-704e9704bafe | -3.7852 | -42.43266 | 2024-11-30 12:14:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b8a3085c-5be5-3ef8-8052-c76bbbdd7132 | -6.14117 | -43.95567 | 2024-11-30 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a4f4a576-c411-3bf4-b06c-3db240513f1d | -6.12961 | -44.92305 | 2024-11-30 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| d02e6259-5814-3831-ae7c-89cfab0a1576 | -7.60016 | -37.82144 | 2024-11-30 12:14:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 86.7 |
| b2ca824a-aa9f-317c-a91a-df39ff7481b3 | -2.93769 | -42.54755 | 2024-11-30 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7a8d1c2e-f3e1-3ed9-851c-25f17f2c9ce6 | -6.47417 | -38.56803 | 2024-11-30 12:14:00 | TERRA_M-T | BERNARDINO BATISTA | PARAÍBA | Brasil | 2502052 | 25 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 62373c8b-a634-352b-8930-f80cac672fb9 | -7.73489 | -37.27493 | 2024-11-30 12:14:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 959352a5-75a7-3b39-b866-6b1f9165ba68 | -6.17657 | -42.61664 | 2024-11-30 12:14:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 97db801a-b57e-3243-b3e2-6b4b56cedebf | -6.30063 | -43.84551 | 2024-11-30 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 60c0ebfb-3735-3cf8-bd07-a094d6a16894 | -4.38924 | -43.11458 | 2024-11-30 12:14:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1c7f0ce9-d659-3981-abcd-6c56f3f9df3d | -3.55861 | -45.1797 | 2024-11-30 12:14:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 22.4 |
| d019fe32-4f85-3ed6-9a9c-b7876858b8a3 | -4.42466 | -42.47647 | 2024-11-30 12:14:00 | TERRA_M-T | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 80697fb3-0516-3d10-af80-5ffe5cd59a23 | -4.8215 | -41.28189 | 2024-11-30 12:14:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 819229e5-cdfd-3082-9239-61cc934c459f | -4.87685 | -41.28657 | 2024-11-30 12:14:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 66d7b06e-f676-38a2-a1f0-b2d520bd5d4e | -4.88184 | -41.31468 | 2024-11-30 12:14:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| b1a0bf50-c9fd-3313-b459-fd595719bb74 | -5.45285 | -42.14342 | 2024-11-30 12:14:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 76e368eb-3117-3429-8fae-1e5376d63947 | -3.68261 | -42.56717 | 2024-11-30 12:14:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| ef070a3e-7861-34c6-ab0c-f28dd2739270 | -6.81329 | -38.97955 | 2024-11-30 12:14:00 | TERRA_M-T | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 41cae9e2-e093-3805-98c8-867ca26a3e13 | -2.92452 | -42.07546 | 2024-11-30 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10c34560-264b-38a9-b4b9-f5e1a49616d8 | -3.54289 | -41.63436 | 2024-11-30 12:14:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e8c2796a-5407-3868-b8db-c2a7d439e1a8 | -3.69015 | -42.32167 | 2024-11-30 12:14:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5988bf61-dd97-3b80-9293-4a986abc848b | -3.41327 | -42.01701 | 2024-11-30 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 72f7f9c8-b82e-3acb-a7e2-615bc65bea43 | -3.35993 | -42.05884 | 2024-11-30 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 166.8 |
| 5bcf7055-9b0a-3531-8bc7-e14242889d22 | -3.90144 | -41.64379 | 2024-11-30 12:14:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b92db233-7cd0-3982-908a-c1301576a936 | -3.80692 | -42.41533 | 2024-11-30 12:14:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a947dc83-21f0-3e58-83c6-93ac4b3fbca1 | -4.69508 | -42.39287 | 2024-11-30 12:14:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ae056cb8-629b-3563-aaa2-3654711e6ff0 | -3.40763 | -42.05572 | 2024-11-30 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 46.2 |
| 786fcec2-2ef9-344d-a43c-b11664a684e9 | -3.42915 | -45.34681 | 2024-11-30 12:14:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ea95f7ac-8e12-3214-985b-3d247fa0b524 | -6.95519 | -42.77655 | 2024-11-30 12:14:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 1bf039cf-7494-3719-af43-9ec3ba9f9341 | -6.95664 | -42.76683 | 2024-11-30 12:14:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 57f70211-dd80-3613-a1e7-770f9950dc3f | -4.28335 | -38.03909 | 2024-11-30 12:14:00 | TERRA_M-T | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 992c63aa-bd3b-3e93-b63d-a68a0b86a111 | -3.5415 | -40.50037 | 2024-11-30 12:14:00 | TERRA_M-T | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 5780ae1d-ef91-3b85-b63b-bce378ecc554 | -3.53884 | -44.85044 | 2024-11-30 12:14:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| dab3fb22-ecc0-3beb-b998-cafc9ab28c40 | -6.25097 | -38.39428 | 2024-11-30 12:14:00 | TERRA_M-T | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 10ff3514-f8fb-307c-8ef0-b4c136d0322e | -5.27355 | -43.52372 | 2024-11-30 12:14:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6fab224e-7ace-3850-a3e6-ea379d084926 | -3.06182 | -44.73445 | 2024-11-30 12:14:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 73a14ee3-2c14-3a09-b7a8-414cbd14491c | -4.94372 | -38.31207 | 2024-11-30 12:14:00 | TERRA_M-T | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 44.0 |
| b4e5ef2b-506b-396c-8f8e-8b03f72c3591 | -4.5597 | -43.56505 | 2024-11-30 12:14:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 7b6be056-f0d7-3d75-97ba-9ca7e9e079d2 | -3.43595 | -42.1056 | 2024-11-30 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 5bf2a72a-6c62-3096-917f-482ddbab0efc | -3.61914 | -41.99971 | 2024-11-30 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 681e04a2-7ce3-3ddc-a493-c022ff422779 | -6.17669 | -37.10324 | 2024-11-30 12:14:00 | TERRA_M-T | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 48069956-fcc4-3dbe-aa4c-7c2d17a3577c | -3.85526 | -42.28024 | 2024-11-30 12:14:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8ddae472-d4de-34d1-a243-b089e908d203 | -3.91792 | -42.41732 | 2024-11-30 12:14:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| e6703a2d-702f-3a00-9de9-95369dfa9492 | -8.00942 | -37.89482 | 2024-11-30 12:16:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 16.4 |
| b638ed56-0de7-3471-9377-d6d547fa9cd8 | -7.94169 | -37.71441 | 2024-11-30 12:16:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 48ea2463-c747-36e1-9dda-1affe75c6000 | -9.20113 | -36.50011 | 2024-11-30 12:16:00 | TERRA_M-T | LAGOA DO OURO | PERNAMBUCO | Brasil | 2608602 | 26 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 334fe789-c23d-3dc9-adb2-779211374760 | -14.05391 | -41.81504 | 2024-11-30 12:16:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 912838e9-3e90-34dd-a904-f0dab1db36b1 | -8.29395 | -48.33395 | 2024-11-30 12:16:00 | TERRA_M-T | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 127fe116-4b1e-3837-967c-ce95c79c577c | -8.44071 | -38.6835 | 2024-11-30 12:16:00 | TERRA_M-T | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 12.9 |
| de9bb5cd-4e1d-33e8-a031-a1843f3ef87e | -8.45414 | -45.11762 | 2024-11-30 12:16:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c362ea1c-f461-37d2-8524-81bca33fbe6c | -6.92188 | -43.54534 | 2024-11-30 12:16:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 41b4b2b2-fcc0-3e94-9e35-ed3adca2f7be | -14.16098 | -42.61767 | 2024-11-30 12:16:00 | TERRA_M-T | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| bcd19317-005b-36f0-8fac-9edad24b7944 | -8.02862 | -38.71892 | 2024-11-30 12:16:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 106e5764-d1ef-3a62-a9a9-aa832708ae38 | -8.76622 | -40.36082 | 2024-11-30 12:16:00 | TERRA_M-T | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 95643092-da13-3920-84bb-feceda1d5881 | -10.18468 | -42.47564 | 2024-11-30 12:16:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a6e37561-442f-35f0-a07e-005d67f42c53 | -12.13656 | -43.56878 | 2024-11-30 12:16:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 7b1b57ce-5229-33af-937f-91caae457502 | -7.85433 | -37.75615 | 2024-11-30 12:16:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 837dbd88-da64-3a75-b7fe-8ff27444e54b | -7.80766 | -44.18747 | 2024-11-30 12:16:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 685ab13b-a3d9-3af4-9a2a-f3a0a4150be1 | -7.89307 | -38.36797 | 2024-11-30 12:16:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 11.0 |
| cd60c319-a71a-32a6-946b-889fd24c9713 | -12.13799 | -43.5592 | 2024-11-30 12:16:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 16cb87dd-1e89-36f0-9a64-b68935465e50 | -11.00871 | -38.37892 | 2024-11-30 12:16:00 | TERRA_M-T | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| cd0b179e-d510-3cdb-8342-871a6f4118ba | -8.99425 | -35.23076 | 2024-11-30 12:16:00 | TERRA_M-T | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.8 |
| 1b6edfb0-88f1-3742-9471-495e12edf6b1 | -12.23884 | -42.94229 | 2024-11-30 12:16:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 224dfc11-12c6-324e-9c5b-4371eece941e | -8.76025 | -41.05047 | 2024-11-30 12:16:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b5992dfb-2909-3b7d-9a5f-0ccc731d6867 | -7.83336 | -43.07733 | 2024-11-30 12:16:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 07e1d826-a342-3375-b893-8158db932d51 | -8.31807 | -44.94223 | 2024-11-30 12:16:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 00cd899a-6660-382f-a0e3-e279aa450493 | -8.4458 | -38.67986 | 2024-11-30 12:16:00 | TERRA_M-T | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 7f9cc684-a722-3fe2-8245-466ca6be33ca | -7.7463 | -37.50045 | 2024-11-30 12:16:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 6018f14d-77b6-3be0-acd2-123ba6ade2a8 | -7.2003 | -41.30065 | 2024-11-30 12:16:00 | TERRA_M-T | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7475df39-51b5-3b87-ab89-f52b91afa25f | -8.99213 | -35.22492 | 2024-11-30 12:16:00 | TERRA_M-T | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 47.3 |
| b94ab108-3999-3b61-a227-b860ff0b3998 | -9.42434 | -38.38982 | 2024-11-30 12:16:00 | TERRA_M-T | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e5b4beb4-6a3a-31e3-917a-219805643731 | -8.03809 | -38.72016 | 2024-11-30 12:16:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 22.6 |
| a2b034b4-25a8-3a39-91b9-ce67ff6b690b | -6.90785 | -43.54821 | 2024-11-30 12:16:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9b7ef087-3ab3-3de0-aecc-01962b6361dd | -8.63032 | -41.04657 | 2024-11-30 12:16:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 3781106b-d090-3d8f-8367-9b0548ef163e | -7.93595 | -37.02139 | 2024-11-30 12:16:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 11.4 |
| b07373bf-4034-3911-b997-229a865264f0 | -8.69501 | -37.12336 | 2024-11-30 12:16:00 | TERRA_M-T | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 18.8 |
| d6faae1c-478e-3f24-ae2e-40994136e1cd | -10.27618 | -39.38809 | 2024-11-30 12:16:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| b9080ced-ca4b-3be7-85fb-7e4ac9da4032 | -10.18602 | -42.46653 | 2024-11-30 12:16:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 39.0 |
| 2887d63b-6cec-3741-bf92-7fc1b1f35053 | -11.41244 | -45.09202 | 2024-11-30 12:16:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 5399536b-3882-3f1c-9589-2504de4c21fc | -8.36963 | -44.81131 | 2024-11-30 12:16:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 59c5520d-feac-3c99-9ce8-da68f537d7c0 | -9.229 | -44.286 | 2024-11-30 12:16:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0a780ba4-f41b-3448-81ef-d61c7c280deb | -7.85278 | -37.76768 | 2024-11-30 12:16:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 4a3c7f10-899a-3360-870d-98b8468a1961 | -8.10111 | -38.85999 | 2024-11-30 12:16:00 | TERRA_M-T | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 989ad786-fa28-3788-a88c-5602525cde41 | -7.74465 | -37.51251 | 2024-11-30 12:16:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 761fda5f-08b2-3245-8ab6-73bf33368592 | -8.68701 | -41.04303 | 2024-11-30 12:16:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |


[Clique aqui para ver as próximas entradas](README136.md)
