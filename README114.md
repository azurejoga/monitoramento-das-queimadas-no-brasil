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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c70007d-5af8-3622-9090-31a9decb78a1 | -16.57838 | -58.24126 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ed5443b7-84b6-3489-8382-c4f68d402788 | -16.57792 | -58.22311 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d27ebdf3-07ef-335e-bdc5-e2c89b002733 | -16.57742 | -58.24648 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0316e57a-be55-391f-9126-0ff5a3cbf335 | -16.57732 | -58.22492 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c6cfb49c-fd19-35d3-b47d-0b653a7d9323 | -16.577 | -58.22832 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2accb747-bafe-327c-acdf-e7903b40df73 | -16.57637 | -58.23011 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| feaec7a8-d610-3f21-966a-eb0e11d8967a | -16.57607 | -58.23353 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 48350240-dfe1-3cd9-869f-7686240a2975 | -16.57541 | -58.23531 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c0d8887b-c86c-353a-94cf-c6ea642a52ad | -16.57515 | -58.23874 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cefca057-fc79-31fc-abfa-6965731f62e7 | -16.57446 | -58.24051 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 90edf15e-2dd2-3c84-8208-4360496827ab | -16.57423 | -58.24396 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3f59e85c-7c1a-3a83-a6fa-6f8ac0473c0e | -16.5735 | -58.24572 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a2c0039e-d013-318c-a063-2544e9cbb465 | -16.57331 | -58.24918 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7e6bd955-faf2-35a3-9821-015cb90d4c7e | -16.57307 | -58.22757 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 23d7d33f-eca9-3020-abbc-ff7144726b5b | -16.57245 | -58.22938 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b95da513-4648-3092-9ca5-a9c0926f344e | -16.57215 | -58.23278 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b0868ef3-f709-3b3e-b902-4abf969f8254 | -16.57149 | -58.23456 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6148de68-68e7-35eb-b847-45f201701282 | -16.57123 | -58.23799 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 784c4078-249b-373f-8202-e7a40c3a615d | -16.57053 | -58.23977 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| fe994d22-2aac-3f94-b8bf-7501de374144 | -16.5703 | -58.24321 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e1db16f5-f0f1-3401-829d-a61f65bdb557 | -16.56957 | -58.24498 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8febd06e-5504-3695-9149-6172c1ea0cba | -16.56938 | -58.24842 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a55864b8-4858-3dd6-ac41-6b662e28830c | -16.56862 | -58.25018 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 33436238-034c-3a2e-9b20-286c88f2991a | -16.56469 | -58.24944 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dec96f58-8e7d-3d74-8d90-4c5958aa21fd | -16.19334 | -58.43173 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f1f2bbdc-1eff-3ceb-bb18-d24d97f13771 | -16.18934 | -58.43096 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 639cb13b-0a3b-3c61-836a-12496e9de89e | -16.1873 | -58.41931 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9af822fc-d0c1-30e4-be17-32e2b307381b | -16.18535 | -58.43019 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 54c040f8-55c8-36bd-a840-bfaed23bfc7d | -15.38236 | -58.15722 | 2024-10-02 04:49:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23cb3685-66d3-3bae-b40a-f0691c7b3cc8 | -15.38038 | -58.15675 | 2024-10-02 04:49:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abb3fdc0-faa5-3749-a2ef-0cd8f81e183e | -15.37844 | -58.15612 | 2024-10-02 04:49:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4ecf2be-b5dd-3992-8111-2df56ba65075 | -15.37391 | -58.15848 | 2024-10-02 04:49:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4917d85e-7e23-330e-b17d-81afd2a3377d | -15.35952 | -58.17 | 2024-10-02 04:49:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b9d14da-0f28-3db1-b649-c5859f78fd67 | -15.35884 | -58.17378 | 2024-10-02 04:49:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8166cb3d-cb64-3d91-8369-655f364217b2 | -15.28111 | -58.19323 | 2024-10-02 04:49:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ccfa48fa-b827-3d5f-8256-8117673b7e0b | -15.27433 | -58.18509 | 2024-10-02 04:49:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8327d6f7-054b-368c-8c11-93bafbdc6225 | -15.27368 | -58.18864 | 2024-10-02 04:49:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8bd88fe-a532-3c7c-9150-09ca4bad6d36 | -15.2703 | -58.18458 | 2024-10-02 04:49:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9db240d6-d095-3528-8b55-1f09d0a95c9c | -10.72066 | -58.51596 | 2024-10-02 04:49:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a9bbe24-8269-33c6-8f99-cd45fee7cc47 | -10.71989 | -58.52033 | 2024-10-02 04:49:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| baf0439f-e9ed-3a55-b7b4-2d3329204697 | -10.71912 | -58.52473 | 2024-10-02 04:49:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d6024e3-2b75-3035-8a61-e9767aaaa80d | -10.71548 | -58.51957 | 2024-10-02 04:49:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2bc0a1a-2f93-3371-a02b-e4215f663f82 | -10.71393 | -58.52839 | 2024-10-02 04:49:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8696c9f5-1740-3c68-b52d-d5b1fb6df479 | -12.23632 | -59.24192 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 245ad59b-3f7b-368b-80c6-cd3223a5e8d9 | -12.23371 | -59.24065 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 471c69c3-38fe-3b8f-8ef8-4752da30da1f | -12.23098 | -59.24575 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07691a8c-6c31-3366-9a52-6261173a6f4f | -10.98069 | -58.96811 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f593df8-052a-35a0-9ba8-ed7fa4f62165 | -12.15145 | -59.88319 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 789bdacd-cb84-305f-8790-6a4808f788f6 | -12.14578 | -59.88743 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70563989-5dde-334e-a1ff-a7d6c36fefd1 | -12.1448 | -59.89263 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b019f7a-aa5a-36da-8e52-9b62ddd071a1 | -12.14105 | -59.88665 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab41300e-1bcd-3c77-bbaa-3bc933b9c37d | -12.14008 | -59.8918 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62748368-0b57-35f4-aad4-9c9ec2f9cf8f | -12.12489 | -59.77957 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ee40d52-3256-3441-b201-1601065f2942 | -12.12394 | -59.78477 | 2024-10-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e497b2f-037a-3c0e-82b0-2e7d5ac9e02e | -12.34554 | -59.2137 | 2024-10-02 04:49:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f432da9a-8ce9-3bd0-96e5-134938ec579c | -12.34471 | -59.21832 | 2024-10-02 04:49:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7449dd9c-5de0-3fe0-bdcc-3b1aab993127 | -12.34106 | -59.21286 | 2024-10-02 04:49:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d738c2d6-7183-376a-8fa3-230c450c3c90 | -12.13965 | -60.76678 | 2024-10-02 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55a510ec-279c-3ba7-8bf4-8379bbbd1433 | -12.13911 | -60.76965 | 2024-10-02 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4536ae99-2102-3a67-b78c-e26d108b199d | -12.00321 | -61.08434 | 2024-10-02 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f4b1c6e-0cc8-3fef-9272-052d5859f4f3 | -11.9981 | -61.08339 | 2024-10-02 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d7e2f22-056e-3643-b313-bfe02e58cefc | -11.33036 | -60.55999 | 2024-10-02 04:49:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d5de11f-26f3-3adb-a9b9-7bf402b80eab | -11.25608 | -60.59706 | 2024-10-02 04:49:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d4c4d1b-48c7-3d53-a679-bbf0be85795e | -11.25099 | -60.59651 | 2024-10-02 04:49:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 27e19c99-362c-3414-95dc-80ecba878eba | -11.25034 | -60.59991 | 2024-10-02 04:49:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6c1b51d-94d6-3281-8b59-3600c4ad6e5b | -11.24767 | -60.47782 | 2024-10-02 04:49:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 780af7ca-fea1-3fc9-80a2-81487baf94e7 | -11.24709 | -60.47924 | 2024-10-02 04:49:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 596324c2-7f01-38b5-ba22-0c226b431732 | -11.24522 | -60.59954 | 2024-10-02 04:49:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a259586e-4c17-3444-b2d3-426bd21e3e35 | -13.28975 | -60.81738 | 2024-10-02 04:49:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24dacfab-2fba-3837-9424-66d241ddd017 | -10.63641 | -62.81406 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c28ab565-a9a3-3e59-9169-49bb21329692 | -10.63558 | -62.81836 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11d05534-2f2e-390e-9a80-07522d24d0dd | -11.31075 | -62.06902 | 2024-10-02 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ff3d851-8a52-3fe9-8f67-79c016157909 | -11.31003 | -62.07274 | 2024-10-02 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92a38350-6485-3cad-825f-9506af78b5bb | -10.92354 | -62.4495 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5aa05b2f-baaa-35bd-b77c-4ccd7ab61e4d | -12.75749 | -62.91551 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c38f31dc-4b7d-3db1-8992-71c2df7f23ae | -12.75666 | -62.87867 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0f615a6-6f19-322b-84f8-e8731ada1807 | -12.75589 | -62.88264 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 163d0226-f263-3154-85c1-5437e54908e8 | -12.75342 | -62.90641 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c601b61-881e-3810-b872-f724ea4fc50d | -12.75338 | -62.87745 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad8b3f4f-05ac-38d3-b00c-889795ac20be | -12.75262 | -62.91039 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8a9fa931-5a3c-3bef-90b8-93178f92511f | -12.75257 | -62.88141 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87bd0e56-e70f-3f42-b457-49be9932e410 | -12.75182 | -62.91438 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b13bcfc8-9ff6-31ae-9bf0-eac86a5a5619 | -12.75124 | -62.90657 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 84912e22-871a-314d-a222-155701b635ca | -12.75046 | -62.91056 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfe17def-d77e-3906-9e40-fe9aa09d3671 | -12.74969 | -62.91455 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8741b0de-e196-36f5-bd5c-bdecd888b52f | -12.74776 | -62.90526 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a8b639a-3f12-3b34-87bc-fc53010c4a01 | -12.65762 | -63.11113 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c6ba93c-cd05-347d-8525-f3f258fb7de8 | -12.6568 | -63.11527 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b096508c-45df-334b-9edd-1bda63675b81 | -12.65597 | -63.11944 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3aeda73d-bd27-3725-9cf7-5c4ce55138ee | -12.65269 | -63.10583 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4e4a1d89-9283-3af9-88c1-10a1b0881b4e | -12.65188 | -63.10994 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 1b6bea09-0815-32c8-864d-f7aef48da57a | -12.65105 | -63.11407 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 07874808-2a77-3dc1-9787-f96545fa0384 | -12.65023 | -63.11824 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ec88893e-06d2-3220-8e83-550c474e6c10 | -12.6494 | -63.12238 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 36b92e35-2204-3b46-b1b7-b8ee0da16be2 | -12.64692 | -63.13483 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3af891eb-6ff3-3511-aa1f-7cd66b122786 | -12.64531 | -63.1129 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3e8dc964-85f8-3723-ab98-6eeb2cbb9907 | -12.64448 | -63.11703 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6637dae2-eeff-3511-ac74-da47160586f0 | -12.64365 | -63.12117 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 67ae5d65-4678-30d3-b656-b190b7141d51 | -12.64282 | -63.12534 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fbf10909-a1eb-3967-b120-f6ae409de678 | -12.64199 | -63.12949 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README115.md)
