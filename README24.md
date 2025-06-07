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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e4364cb-a58c-3b78-b3e7-6596c9630944 | -7.72306 | -44.17525 | 2025-06-07 05:38:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 7ee8fa7e-ed08-3ca4-b624-7beabe721738 | -6.95983 | -42.89957 | 2025-06-07 05:38:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| a5a39645-56a5-3f73-8ecc-2dc5b5c42dd7 | -9.40028 | -48.42744 | 2025-06-07 05:38:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2be867dc-cb29-3605-9274-65f91a768745 | -7.73191 | -44.17655 | 2025-06-07 05:38:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 15ca1a6a-0149-3e63-8aa0-9e7770571336 | -9.07417 | -47.13656 | 2025-06-07 05:38:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| dd45576f-cf0d-3af5-b03b-dfe08cfd7f2e | -5.64026 | -43.70977 | 2025-06-07 05:38:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e79b42d5-5f36-3468-8c55-40d77c8bfd55 | -5.7755 | -43.60776 | 2025-06-07 05:38:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2f017da5-f221-3c6b-a12d-4dab2251fffd | -7.73458 | -44.15861 | 2025-06-07 05:38:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e8032112-4cb3-3794-98b0-a4bf2970429c | -6.21378 | -44.50404 | 2025-06-07 05:38:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e22a33b-7dc8-32f0-a207-9a20cfa185ee | -5.64911 | -43.71107 | 2025-06-07 05:38:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1c693e8-2612-38be-82dd-2b97362ef259 | -6.94926 | -42.90784 | 2025-06-07 05:38:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 554b201c-e6ba-380a-aa13-acaac8046094 | -7.02294 | -44.5899 | 2025-06-07 05:38:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6e42a529-6c8d-357f-9702-22e960067410 | -7.71554 | -44.16501 | 2025-06-07 05:38:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e857400f-7a48-3bcf-b06c-a0ae8842d8ad | -9.39847 | -48.43889 | 2025-06-07 05:38:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 73991d63-6971-30b1-a8a3-c23a0052c9a3 | -9.07263 | -47.14634 | 2025-06-07 05:38:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ef7ae82f-e8b7-3dd1-a3e6-64d66d8fd36c | -11.38711 | -56.55471 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a083e4d1-573f-35f2-a453-e379e596e94f | -11.89534 | -56.41065 | 2025-06-07 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b3a3a53-c762-3003-870a-d16d1022db1d | -13.3651 | -54.26041 | 2025-06-07 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cba1ea99-f96a-3db5-b938-d573145938b7 | -12.10289 | -64.05688 | 2025-06-07 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9feb4ba-9a28-349f-a4e6-9aafb5cb21e9 | -14.02973 | -55.13336 | 2025-06-07 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48808991-5968-3b1a-beab-a237dc49c8a8 | -11.37087 | -56.56295 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c77a33d1-1455-3876-b450-62e2eb097e21 | -13.36822 | -54.263 | 2025-06-07 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 19c35c83-c046-314c-90a1-a28afd392b75 | -10.88234 | -54.30514 | 2025-06-07 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ec9038b-c78c-3811-a935-8bcec65c5c5d | -13.09396 | -52.28211 | 2025-06-07 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1e63b025-0aa4-3155-8c21-1965713e0e81 | -9.92863 | -59.93369 | 2025-06-07 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 526db697-3a43-3e35-8e81-96ceecce175b | -13.29543 | -57.94071 | 2025-06-07 05:38:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d97e88b-7ef5-3228-af18-46395d1034e1 | -13.52002 | -56.56205 | 2025-06-07 05:38:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 739d2c53-fef9-3072-b41c-6966694f59a4 | -12.67083 | -58.21984 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e76734a5-14fb-3f59-a360-1b745af85d74 | -14.0412 | -55.13465 | 2025-06-07 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7a73965-4fdb-3838-b647-30fac0231aa8 | -12.70548 | -58.24486 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c6ad257-3d06-3595-b7c0-57b8493da2fb | -13.72073 | -58.67768 | 2025-06-07 05:38:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29268dbc-3a22-3f01-83f9-4c9a0bf3d050 | -9.8213 | -67.41547 | 2025-06-07 05:38:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82e518ab-eaf9-35f4-8c82-e1d5470abf0b | -13.51964 | -56.56528 | 2025-06-07 05:38:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4094a9bf-8aac-34e7-877d-b101678d701f | -12.87829 | -52.20207 | 2025-06-07 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 642d2841-0564-3389-bb9c-5ad9fef85cc1 | -11.38674 | -56.55769 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd03d679-0ae4-3113-993b-9d20033c90b5 | -13.46575 | -56.85897 | 2025-06-07 05:38:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebdf795f-76ec-3ae5-9f53-dd81164b06d2 | -11.91496 | -54.82453 | 2025-06-07 05:38:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10351afb-cb70-3f72-ad09-e2cfa19d82e6 | -12.52232 | -58.35423 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5c9c5a6b-183b-38ca-aa0a-32fe6db95115 | -11.25209 | -60.78971 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb2cc8cd-7fa6-35f6-890d-a04d5c4044f4 | -11.13901 | -53.94661 | 2025-06-07 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0b46a93-b469-38b3-aad4-e32598fe03e0 | -12.32939 | -52.47401 | 2025-06-07 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d9b8d12-3cc8-3ee8-9c73-8536a6f63a5a | -12.53257 | -58.34638 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c50fdc6d-e14a-3c88-960e-12873c8035df | -11.37742 | -56.55202 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 268e27cb-f014-3197-9506-8f81db564238 | -11.25703 | -60.80964 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 352bd4d0-8859-3e45-9457-9649ffb945a9 | -12.336 | -52.47488 | 2025-06-07 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cd8cdc3-901f-3bb7-aeb0-766a2f473e32 | -10.05602 | -59.36134 | 2025-06-07 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0faf7a51-3ad5-319a-aba7-511cb732b0f8 | -9.81223 | -63.36352 | 2025-06-07 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93e8baba-4079-33f3-b802-a1193a944c6d | -13.28603 | -57.9394 | 2025-06-07 05:38:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e13a8f58-757e-3149-a3e6-0e0fccea123a | -12.52744 | -58.35033 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a2575e31-293a-3a10-899e-afbb9aa48f83 | -10.69339 | -57.65042 | 2025-06-07 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e300f7b2-165b-3d04-a365-a3a073d5d014 | -12.71066 | -58.24072 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69c9935b-02f0-3d0a-ba02-d60d490482bb | -11.26278 | -60.79621 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 65b31990-3a01-39f8-a2b8-26698711ad21 | -12.71005 | -58.02464 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6502cef2-9681-324d-acba-8167bd65b982 | -11.25521 | -60.79501 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 329e0bfb-431a-359c-a0e4-c6aa8771e9b3 | -11.26147 | -60.80555 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06625a61-7d15-319d-92ff-0a20e82c73ec | -13.36874 | -54.25852 | 2025-06-07 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 385e2027-c7dd-34fd-9021-4af39d187e0d | -12.52682 | -58.35498 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6b7ba5b7-6e0c-3411-babe-5bc2d9505b55 | -12.88505 | -52.20297 | 2025-06-07 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 883b7e64-814d-3538-b526-9264c2c80b48 | -10.88183 | -54.30929 | 2025-06-07 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac280187-5524-3de9-a762-fdc29631e0db | -11.83689 | -60.91965 | 2025-06-07 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a81e27d2-a4b8-3dad-bbab-e2664eb75100 | -13.46613 | -56.85594 | 2025-06-07 05:38:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a7b86f1-b474-3b29-b506-ab7175acaac8 | -9.4191 | -63.33517 | 2025-06-07 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04fc1953-dff9-3de5-ab2e-7e9b6797a65e | -11.38244 | -56.55106 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bea66b40-bb92-3227-b88c-30dbd75b2748 | -12.66625 | -58.21926 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea279ae0-4966-3411-b23d-32b0763c2b2f | -11.91957 | -63.34003 | 2025-06-07 05:38:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13185b8d-7fc4-33bc-81cc-71a1137534fe | -13.30546 | -57.93703 | 2025-06-07 05:38:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a92f2d2-a7f9-384d-822b-6b673033fb2d | -10.33538 | -57.49055 | 2025-06-07 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c16fba8-6486-3897-905e-57d4c4e300ae | -11.36622 | -56.55939 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5b6d204e-8667-3246-a998-6bf6c9b2a260 | -10.88131 | -54.31345 | 2025-06-07 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c454676e-f62a-35bb-80f8-0a59e1273897 | -11.84001 | -60.92492 | 2025-06-07 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68e13c08-8566-3be7-ad2c-f0d508df0bf8 | -11.89023 | -56.40991 | 2025-06-07 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c216c5cd-602d-3444-b1f8-52c6002b43dc | -11.53672 | -56.45995 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34cb8f39-87e5-3a21-9d7e-5a91c71ba18b | -9.81612 | -63.36047 | 2025-06-07 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 986431a1-af8d-3a2b-8744-f85516059ac8 | -10.29882 | -57.13828 | 2025-06-07 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7eceadd-0a16-3ef7-8bc6-60b3e181a2b3 | -12.66216 | -58.21997 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d4bbf6d-c9f1-3f38-b161-4d85b843473d | -11.37239 | -56.55135 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dbbf7d60-004b-3f53-b34b-799a45f35dad | -12.35455 | -63.96716 | 2025-06-07 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| add2fa6c-7b17-393b-ad37-c0e693d51ac1 | -11.36584 | -56.56228 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3eb238cb-9343-37c1-a22a-75e3a763888b | -12.53331 | -58.35283 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a979ebe2-59ab-33e7-bbf7-5aec0488eb6c | -11.259 | -60.79562 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7bbbf367-8e0b-3519-ab78-c724f84073ac | -11.38283 | -56.54981 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e9287b5-89c2-3194-83ab-d9c12680a678 | -13.51778 | -56.56581 | 2025-06-07 05:38:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 705077da-26d4-384e-86c2-3681d2a5a22e | -11.54367 | -56.44572 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f5d7cbf-8c52-3a5f-9e11-04e596ec82c8 | -9.42243 | -63.3357 | 2025-06-07 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 172c33cd-325f-3d26-8def-921849622cd6 | -11.37201 | -56.55428 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79fe948e-1f42-3ad6-b9be-6f0785a6eedf | -11.37166 | -56.55551 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2b028da-1531-3ccf-84db-ead3b8d25c5d | -10.8202 | -56.95769 | 2025-06-07 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e7e1015-dbbf-31f9-894a-c751338550ca | -10.29952 | -57.13306 | 2025-06-07 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31e6c4f3-a20c-3b3e-b08b-da98e9998230 | -11.53709 | -56.45699 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb0a7dca-1d1c-38e4-aa03-d947928b8b87 | -10.54117 | -56.38644 | 2025-06-07 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 15ba1cdf-9b9a-3c35-b03e-f70ef24cd9ce | -11.71207 | -56.45256 | 2025-06-07 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10e89fd8-5fca-33d0-b542-5cbc38d78a55 | -10.53575 | -56.38875 | 2025-06-07 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a9466a4-af33-323d-a192-e062b0310436 | -13.30076 | -57.93636 | 2025-06-07 05:38:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67d5a4f1-2cfc-3128-a928-824be4a1ef23 | -12.53194 | -58.35106 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4a1a1300-0f2c-3def-9041-d92afb2c5193 | -12.70543 | -58.02391 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b8c0c84-29c7-3257-b5d9-8ec22a72ba56 | -13.28133 | -57.93877 | 2025-06-07 05:38:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26b1b67c-604e-39aa-a6cb-9acc3d17d39d | -10.69773 | -57.64741 | 2025-06-07 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf592a36-9b57-3c36-bdcb-f988d6d90cde | -11.1422 | -53.92036 | 2025-06-07 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82280480-4cca-32cc-8a96-10ddb6643c7c | -11.37665 | -56.55786 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ab65d1d-77f0-3423-a14f-ee956ec0c811 | -11.14166 | -53.92482 | 2025-06-07 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README25.md)
