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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8ecb0a7-467c-3347-b8fe-9286adca8f28 | -14.45156 | -46.34141 | 2025-10-03 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 708ac4b3-efa9-3377-a4ac-e976c06a5be7 | -11.84856 | -44.95338 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34d0a174-328f-3980-8b8a-478bb4d3ce0f | -12.62061 | -46.95779 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 42d07a70-0d90-3966-a0b3-690fc69574d9 | -9.71422 | -45.43948 | 2025-10-03 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98c1cba5-6d83-3ac7-908b-af35d196f8fb | -15.2453 | -49.29156 | 2025-10-03 03:45:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c8b6787-b05a-3f11-bca7-3d1370b4b1d2 | -14.06949 | -45.68184 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b394131-4c23-35bd-88ff-b617ed335fa7 | -14.93494 | -46.89232 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3f52fa89-553e-318b-a839-54f8341eff38 | -12.38208 | -46.51577 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb4513b0-6a6e-3ee7-a5b9-6e382bc6058b | -15.22593 | -47.18539 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca32ffdc-ba1f-3235-b127-8bb664cb0691 | -13.33085 | -47.20326 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 511836a9-fbf2-3593-ba94-39a87d460ea0 | -8.81428 | -46.67056 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d4bc929-d1ca-3828-a143-a5ce98244743 | -14.90181 | -48.30019 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6779162e-5340-3ece-901f-0494cffa6f7a | -8.70903 | -47.98477 | 2025-10-03 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8ef2f191-7e1c-3aa8-89ae-0591719b5046 | -11.13865 | -43.39977 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e451e28a-9028-3fd4-9e4d-dde53cbb7042 | -13.37443 | -47.27995 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2327bcd-83c3-33d0-986d-81edcee7ac2b | -10.68163 | -47.34156 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c929aa87-2af8-3e84-99b2-1d1e506f0d1b | -13.18899 | -47.81863 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb2c15bc-3016-3bfe-9b3a-eaccfe1e55fc | -15.58819 | -46.91417 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ac58ba5-0bd5-37ae-8ba4-ac194cb34405 | -14.89822 | -47.82849 | 2025-10-03 03:45:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe6d10d5-cb37-3d5c-9e74-02bb93a7a1ab | -14.2136 | -46.08656 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7c0e649-0a17-3ff1-b732-de390f9525e8 | -13.32577 | -47.58903 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58fb7b94-b601-3107-832e-f4093a9dc33e | -15.3004 | -45.09631 | 2025-10-03 03:45:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af175b12-4ad3-3005-bf9d-9d14332224fa | -10.83797 | -46.5993 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ec1ea6b6-4c15-33e6-9187-feb38cce2bb7 | -14.28596 | -45.91874 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd3889e2-9b92-3842-a5b0-98e3e4e67eaa | -13.56818 | -43.57405 | 2025-10-03 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 727b35b8-57cb-3f21-a17b-589ff6b6caa1 | -10.86577 | -46.67833 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e985a95-e085-3a9e-a8e1-89f6f4cee7b5 | -9.76785 | -46.2165 | 2025-10-03 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3019704f-6339-3796-bb4e-f1e21d4293df | -15.25409 | -49.31075 | 2025-10-03 03:45:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff67261e-12a5-34ba-9454-8efe6316a115 | -14.23036 | -46.1109 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10d1c63f-26b4-3b99-8126-70d9e0d43fb3 | -11.87845 | -45.01222 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c2abe1a-6706-3534-8e3f-85df33de4ddc | -11.62869 | -47.98145 | 2025-10-03 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be2bee46-2660-349d-9f3a-5ad116266115 | -14.19902 | -46.07882 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cc77669-5342-321c-a895-3125fface002 | -10.83402 | -41.27266 | 2025-10-03 03:45:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d36ffed4-1de2-3744-800e-660fd67b186a | -14.64672 | -44.73665 | 2025-10-03 03:45:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfdef8cb-893e-3cad-a6b9-93d2d593f5e5 | -9.31755 | -45.97005 | 2025-10-03 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93839bee-a722-3ebc-a37b-2a18f474cf70 | -14.2943 | -45.88931 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 125b635d-6905-3dd4-9a64-482cc286dd39 | -9.08419 | -48.02888 | 2025-10-03 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95d83c0f-74ae-3d49-9af1-065bc5140688 | -14.28788 | -45.92288 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdd64a28-f3b8-3df0-8da6-17ae769e33ae | -14.30164 | -46.02762 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9f22bfd-50d4-3d5c-a20e-1c04b1092c57 | -15.52087 | -46.81073 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5f21d70-2f27-35a2-bf98-9afba4419157 | -11.80603 | -45.01444 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2b3d7c7-e506-3a99-aa21-83da818cbc8a | -13.66961 | -47.31133 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b81d90da-43c2-340f-9af2-38788ac46c31 | -12.41332 | -45.16673 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6299ce0-aeb5-34d6-8a43-d3b2f1f0ac88 | -14.37837 | -45.94845 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84d80969-3616-3cce-bfd8-94c3ee1c13fc | -10.87543 | -46.65928 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0fdeeb2f-3e5a-371d-a072-1fccf4f84987 | -8.64789 | -47.71775 | 2025-10-03 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2505e145-47fe-339e-bcbd-6e9ab299f89b | -15.94632 | -46.23194 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36a22adb-8f6b-311e-88e6-989ef63c7977 | -11.08595 | -47.86772 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c59eb85c-c73b-37ea-9768-f0d6741fc837 | -12.62423 | -46.96906 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 958f40f0-b5b0-306a-957a-12e302ac8efd | -15.58759 | -46.91716 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 285d89dd-d39a-3a4f-a547-187629e54966 | -12.94066 | -46.37473 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4ac2f5e-80fb-3c74-8162-e2ff823faf3f | -14.42507 | -46.08931 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8f64862-adb0-3306-882c-603b416d69bd | -14.8996 | -46.84589 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6de853ad-be8f-3ec0-bc2c-e750a19951bb | -13.56215 | -47.29099 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 121178e1-6edd-3c84-85ad-6ea0de49fdd4 | -12.69606 | -48.54642 | 2025-10-03 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42968ea9-a8e2-3095-bb0f-8214220f19dc | -11.88122 | -45.02509 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0e47890-878b-3c29-900b-7b5daa8c035c | -14.90535 | -48.34153 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a7d41627-aff9-3f87-b0f0-cbe9c24def70 | -13.3295 | -47.60022 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50aab81c-58ca-3860-ade6-0cc007e6952c | -13.93502 | -48.08832 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5096b3c9-83f5-30e9-9c28-25f6eca9c7f0 | -12.82416 | -46.90746 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba66d667-e30d-3d83-8ec8-b37a619155e0 | -11.46931 | -45.0168 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d318b8a8-8523-3753-a302-14b76d15577f | -13.75883 | -48.07166 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 91ff2bda-0af4-3235-a573-909e950b192e | -9.93606 | -43.58596 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acea9310-0f25-318d-9e6b-26a9ae823c02 | -13.94089 | -48.08965 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe29dee4-b7bf-39b1-9a23-adfb77f314f4 | -14.01865 | -44.96202 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c9652ab-c1fc-3c75-a217-4e8eb55c5a22 | -12.90324 | -46.90963 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 468b7ceb-640c-3555-b19e-ad7aca8a3662 | -10.86238 | -45.41943 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b74923f-ee23-313a-aa12-8f32d034c1d8 | -12.2929 | -45.36756 | 2025-10-03 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68dd4470-f416-366b-89b7-af34210e7aaa | -12.63207 | -46.95888 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d2ea9e6-393f-3049-b6a1-a755562589e6 | -8.90627 | -45.04558 | 2025-10-03 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5202d65-e2a1-3b9b-8edb-893ab674a054 | -15.35749 | -47.06496 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7035bcb2-6844-3091-8b83-42d4c845497c | -13.12916 | -47.8418 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1613b82a-d353-3478-9013-958bdb37c0ee | -13.6823 | -48.64054 | 2025-10-03 03:45:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3515066-33c9-3ed7-9879-4a54dea6d95c | -13.23183 | -46.43679 | 2025-10-03 03:45:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fda7547-4070-300f-b05b-9d9af74c9fbf | -11.56641 | -47.65995 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cfd4321-594d-3aa1-818e-2c4fa836b962 | -12.11862 | -43.44435 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9082d65b-1e98-38ec-b923-feafd68ec4eb | -15.33649 | -46.29539 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b93ca1f9-90c3-354f-b69d-7759b6cdd813 | -11.90363 | -46.30418 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 913d6b5b-3abb-30d5-81c6-483ce8ee4ac3 | -15.34942 | -47.83383 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3961969b-135c-3794-b815-2704529f04a6 | -9.92484 | -43.7267 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8bd702e1-93ee-3981-afea-4f8142218870 | -13.76855 | -47.57441 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 44b978ae-6df4-3f0f-b8f9-1443dc97d6e6 | -13.15488 | -47.89574 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62836eeb-3d64-3c41-a8ec-f4fc79114712 | -13.27101 | -47.26689 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 47aef418-1572-3b20-adcf-f8da42e89acf | -14.3162 | -45.87305 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a99948c3-4b03-3f55-aa78-27b2b19b5cf0 | -13.13917 | -47.88247 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 07465d02-a3d0-3a1c-9a0b-6a2e5cca4a1d | -15.11463 | -48.49561 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e244d6b-8cdc-3f25-9e8d-b1ba2e2ad5fa | -15.56853 | -46.95702 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daa015a8-f6a2-335f-a016-9ec6b5ad11d9 | -15.25952 | -44.12593 | 2025-10-03 03:45:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bea747f9-cd25-34c5-a837-8698df09a2d1 | -12.6128 | -46.96771 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 00b41b24-a4c8-39b1-8de6-c65f93c2cc68 | -13.30515 | -47.60162 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e1269587-6eb9-3dba-8a22-d60a9ba77df3 | -9.94091 | -43.57949 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6ef9f02-596f-38a5-8ab8-30134be29fc9 | -15.70447 | -43.22494 | 2025-10-03 03:45:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4adaa29d-0f4e-30aa-98d8-4d1f22994312 | -13.71232 | -43.89513 | 2025-10-03 03:45:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bd7bced-a630-3215-a2af-878626a511a2 | -8.79418 | -46.68012 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b854baa-7c33-3cfc-815d-f589ff3c366e | -13.96643 | -48.10487 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3f27bba2-611b-3710-88fb-7d115f2de58d | -13.17711 | -47.87707 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| feef54a5-3b4e-3387-bd1a-4f642517859d | -13.48336 | -47.24616 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4616d13d-bcd1-3c27-b3c4-42c972ef6562 | -13.1363 | -47.8964 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8865cbf3-4da2-31c9-b86b-544153d262db | -13.86345 | -47.93779 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9953d991-9761-36bc-9264-b59e23957804 | -13.7514 | -47.98653 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README26.md)
