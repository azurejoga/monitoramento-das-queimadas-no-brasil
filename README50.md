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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a464a589-1c1a-3555-b056-bec64b45aabf | -19.49851 | -56.62691 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c51219ac-8481-3237-8952-2e4918471ce5 | -19.49759 | -56.70468 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| fbfd6330-c72b-3242-a013-d0bf3215fcdb | -19.49715 | -56.70949 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| f14bb4a3-67b1-3f32-b30a-53707f383599 | -19.49671 | -56.71428 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| c6024250-4baa-3a1d-9390-c44de17a3830 | -19.53991 | -56.72436 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.0 |
| 555cd99e-b6b0-3579-a406-1068f38569df | -19.53949 | -56.72915 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.0 |
| 1775df3c-50b1-3d1b-80ec-4e21a6fe59af | -19.53871 | -56.72376 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 24459825-5bdc-37db-a1c8-50ddc8b0665c | -19.53826 | -56.72853 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.6 |
| 21583ee8-5678-358d-90d0-1869a9c69061 | -19.53384 | -56.72366 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| b0d6d70c-b8b9-3129-ab25-70d051e739e8 | -19.53343 | -56.72844 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 18b09769-85c8-3af9-9c7e-2d93c49abad8 | -19.53265 | -56.72306 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 6642eb6d-1d8f-3120-8246-edf493c8571a | -19.52778 | -56.72295 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| bf530bb8-2933-3e14-8b26-cc0959536339 | -19.52659 | -56.72239 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| f190e69c-0606-306b-927b-ed256cd5f8bd | -19.48978 | -56.7231 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 421e5c41-8e2a-352a-9951-d84600658bd6 | -19.60442 | -56.75581 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 283.2 |
| b145b0ad-0c0d-3952-8f7b-c66a49e2a015 | -19.60398 | -56.76058 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 5a1c92ff-7ec1-3502-9b94-c32253ac94b5 | -19.60355 | -56.76534 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 27bab0df-9518-3642-b119-aef2879c0e55 | -19.60141 | -56.72169 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 7cc90196-b85a-3fe7-bee3-e55dddb5d978 | -19.60098 | -56.72647 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 7838970d-64ac-3c35-ace6-d65854b1b3cd | -19.60054 | -56.73127 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 42.3 |
| 6a2323ce-7565-328f-9eb8-165c1d07bc4f | -19.6001 | -56.73605 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 42.3 |
| 34db5d50-830a-377f-b6c6-64d01b8e92d4 | -19.59967 | -56.74082 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 202.7 |
| b33046a2-9f46-3e78-adab-ef08880f08cc | -19.59923 | -56.74559 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 202.7 |
| c059e33a-77a8-3394-9c8e-d65c459072ab | -19.5988 | -56.75037 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 283.2 |
| bb7c3fc1-311a-34c6-9c32-b710fd5ee602 | -19.59836 | -56.75513 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 283.2 |
| 5115523d-354f-3fb0-a841-4625cfe8c592 | -19.59793 | -56.75991 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| a6ae5f85-68b1-325b-a751-0faff05f9682 | -19.59749 | -56.76468 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 9b32d11a-1312-38ee-a56a-1b57dfe13f86 | -19.59534 | -56.721 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 5b6be892-0e5e-31db-abdb-51320945aaab | -19.59491 | -56.72579 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 2ad71eb8-10a5-3833-b819-965f822f5bab | -19.59447 | -56.73058 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 4cd30a13-ea79-3c6f-9b28-521f70ec3212 | -19.59404 | -56.73536 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| d85e363c-c1fe-3f1c-9c55-a75dca36a28d | -19.59361 | -56.74014 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 126e2915-49e3-34bd-a4a5-5570065537d6 | -19.59317 | -56.74492 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.1 |
| cc4d3496-d0b2-367f-b6b5-f740baeb4045 | -19.59274 | -56.74969 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| f5d464b1-c9c3-3679-a4bc-d4944dfb8eb6 | -19.59231 | -56.75445 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 6f512b56-cc6c-3e3b-9652-6c2b93743ebe | -19.59188 | -56.75921 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.0 |
| bd1bbc3e-1b56-33f5-a471-ed37e17c5ba5 | -19.58928 | -56.72031 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 3eea5f1c-3d14-302c-84b9-5e74053f7880 | -19.58884 | -56.72511 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| cbf8f7a4-1bb3-383a-b646-0c114c173655 | -19.58841 | -56.72989 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 1d15e36d-5aff-3454-b472-617b57e3b5a5 | -19.58798 | -56.73468 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 18b98d16-d951-31e3-a0db-9183a6da51f3 | -19.58755 | -56.73945 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 5eca5d6a-5cc5-3b67-bdfb-14e97565c70d | -19.58712 | -56.74421 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.1 |
| c81e1e4c-b019-375d-b9fd-a03c8029f933 | -19.58669 | -56.74898 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 66d72bc3-4407-3a19-8a49-e4baaebe597a | -19.58625 | -56.75377 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 454d7d99-86fc-3404-af16-edd214f09f7d | -19.58278 | -56.72442 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 92efe8e6-57e4-3926-9f41-c68dff690b46 | -19.58235 | -56.72921 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 76e03df9-b355-38cd-9f66-6c8ff2dc27e0 | -19.58192 | -56.73399 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7b6aee69-903b-3739-b0dd-d5ec3009167b | -19.58149 | -56.73877 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 78679435-8544-334a-8903-fce9a9d627b6 | -19.57671 | -56.72375 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bc5fef74-c833-3274-8b0a-8b091d4227d0 | -15.6462 | -57.66817 | 2024-10-31 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 005c13ac-bba5-3fb8-8654-c93d406542ee | -16.83163 | -56.69795 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b0afd1f-50e8-316f-ab90-ff3144393794 | -16.82618 | -56.69284 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a2bb1cbb-80d1-3f90-9b1a-5e896da2c134 | -16.82574 | -56.69722 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e897f3d6-29dc-3617-92af-9b8f2567149c | -18.05571 | -57.22483 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c250c9f8-d58f-3557-9142-b5366a31da1d | -18.04993 | -57.22413 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 37121ad6-ded7-32ad-b6ac-5516a0a8a65f | -17.81637 | -57.38484 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 89e24d63-1f29-3c46-82f7-9588c70476b8 | -17.81597 | -57.38892 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 909d1e34-7717-3267-817b-08da204558d0 | -17.81188 | -57.37189 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 121a08f5-d4f0-3106-9b25-d9ac66668b33 | -17.81107 | -57.38005 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c77bce66-df9c-39f8-a369-df2c57e738e6 | -17.80658 | -57.3671 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 01efdac7-8f7d-3d83-aee1-8b59e3fe596d | -17.73444 | -57.5443 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 25d78284-4c4d-39ab-aba2-19bc77cabcc2 | -17.72921 | -57.53965 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f2372ce1-f720-3dc3-8bf6-99fd29fc0fcc | -17.72798 | -57.55152 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 854fedcc-040d-3fc1-867d-967d46c371af | -17.72758 | -57.55547 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 231cdcfa-70b1-3cf1-9d2b-fbb226fcd93b | -17.72234 | -57.55086 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 3e71f226-2acc-3bb4-9321-52256c7530bd | -17.72194 | -57.55481 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 969470cd-3f9e-341d-8731-6c63b4c87cdc | -17.67918 | -57.49441 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a939e5e8-fe5a-3c5f-b6a5-8c1f34bc54fd | -17.67674 | -57.49292 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 943d5f6a-2f84-3843-8473-d92e8ffbd4c5 | -17.67634 | -57.49691 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3b05cab1-558f-36de-9226-cceda0c02c9f | -17.67352 | -57.49374 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 84c257dc-8c30-327b-af6d-c5f5dc17b720 | -17.6731 | -57.49773 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6593e95b-e24f-309d-8f28-0164c2af1f87 | -17.65977 | -57.49086 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 76e36c26-befe-3133-816d-313aeabdd13e | -17.65937 | -57.49485 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ea911255-93a7-3bbc-aad7-800586b624e6 | -17.65823 | -57.47575 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 44e0f210-9980-3996-8281-37301a46a8f3 | -17.65656 | -57.49172 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0d0bc532-8ac9-3ef4-aa43-0ffa035dae91 | -17.65257 | -57.47507 | 2024-10-31 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| ac54e6ad-ab12-327d-b248-5c8dd4ea2ff7 | -17.28033 | -57.49961 | 2024-10-31 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f69dcda7-c5fe-3ecb-9850-e50073a95b8c | -17.27992 | -57.50352 | 2024-10-31 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9c563c68-c923-39c7-897c-132f05400407 | -17.2747 | -57.49892 | 2024-10-31 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| fb1fd8e6-ef68-3db1-971f-2f2e59b50297 | -17.2743 | -57.50284 | 2024-10-31 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| fca7eb6e-112e-3bf9-a5ec-7bd89c15c32f | -17.26867 | -57.50214 | 2024-10-31 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| b783ae0b-a910-3634-b5cb-393751b033bb | -16.92327 | -57.65892 | 2024-10-31 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1cfe110c-6338-393a-b586-ee54eddbe2bc | -16.92287 | -57.65685 | 2024-10-31 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9cc629e6-ded5-3923-a79b-5643cb0f7d80 | -16.92248 | -57.66065 | 2024-10-31 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0db2153f-d22d-39d9-9a53-5639dbf2e7f7 | -16.21313 | -59.33422 | 2024-10-31 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ccef922c-5ac0-3b99-964c-ee436b59b52f | -15.66308 | -59.15018 | 2024-10-31 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85c0b134-5fb8-3367-8982-76386180a5dd | -15.28976 | -60.39988 | 2024-10-31 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14cb47f8-94b4-38b9-8a5a-87ef5beda95c | -2.7383 | -45.0848 | 2024-10-31 05:55:22 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 2069041c-f2e8-39c8-a3ce-5562afbb4b71 | -2.7384 | -45.0622 | 2024-10-31 05:55:22 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 2cffdc35-4b72-3052-8a54-5aa588abc6d4 | -3.2535 | -50.3479 | 2024-10-31 05:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0bacda4d-48b2-3823-b0cb-da1ae80692e2 | -3.2535 | -50.3269 | 2024-10-31 05:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 05d75f19-6ff9-382a-8c93-b53df7fc323a | -4.8584 | -42.9097 | 2024-10-31 05:55:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 4674e991-3705-3a03-a2fb-788f201b53da | 4.96733 | -60.30202 | 2024-10-31 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ccb61cb-9a3b-3898-9948-e96daca03f24 | -0.76707 | -62.89748 | 2024-10-31 06:03:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f76d2be-dd67-36b3-aef9-0f73ee53e044 | -0.76667 | -62.89878 | 2024-10-31 06:03:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db236177-77ca-3011-b490-8119d4ebbcfb | -0.75756 | -62.896 | 2024-10-31 06:03:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f448d5c0-5c58-3150-bf7a-c0bb23f9d58e | -0.6745 | -62.92955 | 2024-10-31 06:03:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f59ccd5-75fd-3c6f-afb0-edea6bcbf6e3 | -0.67386 | -62.92784 | 2024-10-31 06:03:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 93bd593d-1afe-3227-805d-ad381024b505 | -0.66976 | -62.92882 | 2024-10-31 06:03:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b42d2d2-3a80-3a53-9d48-259ed57e2d72 | -0.66912 | -62.9271 | 2024-10-31 06:03:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README51.md)
