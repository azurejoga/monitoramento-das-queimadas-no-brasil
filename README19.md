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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00b44e62-1e2a-3aa4-acea-0ec4f21b315b | -19.2323 | -46.8452 | 2024-10-02 01:16:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| aa226ea2-d226-3ee3-b207-46cf84b66ce7 | -19.2519 | -46.8641 | 2024-10-02 01:16:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 61.9 |
| dd9378cf-4b09-30a3-9d51-7abb663013e1 | -21.2854 | -47.6277 | 2024-10-02 01:17:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 62.7 |
| fa05d1a0-d881-3581-8039-09bcd33f2c1d | -21.2861 | -47.604 | 2024-10-02 01:17:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 941ecbf8-505a-358a-8b7c-e6a2e6b526fd | -21.3661 | -55.6807 | 2024-10-02 01:17:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 906f08eb-0976-3143-90c7-3455ee1ce0a5 | -22.9277 | -43.7243 | 2024-10-02 01:17:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 97.5 |
| 91cba0e7-4e85-3029-ae28-ddfc76246b15 | -22.9006 | -45.1029 | 2024-10-02 01:17:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.9 |
| 9fefef8a-a55c-39f9-b905-44aac9c3b5e7 | -22.9014 | -45.0779 | 2024-10-02 01:17:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.1 |
| 8e4ebd96-fe12-339f-80ec-ec2cb08de5af | -27.043501 | -50.682499 | 2024-10-02 01:20:49 | METOP-C | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3f76f16c-356d-37bd-906a-27b0cceb51b6 | -27.045401 | -50.691002 | 2024-10-02 01:20:49 | METOP-C | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d8bc77a-8834-3638-99ec-37e02450abbd | -26.971201 | -52.043499 | 2024-10-02 01:20:55 | METOP-C | LINDÓIA DO SUL | SANTA CATARINA | Brasil | 4209854 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ffe18a0-7e49-3d6f-9866-9ad85e28f871 | -25.029301 | -50.7132 | 2024-10-02 01:21:22 | METOP-C | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbfb8bdb-c364-3084-aba9-8423e3f7a33c | -25.031401 | -50.721802 | 2024-10-02 01:21:22 | METOP-C | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90b8302c-4ca2-3a6d-8b4d-250cfdc9e451 | -22.930901 | -43.7295 | 2024-10-02 01:21:26 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 756fdcad-099f-3826-8cb6-d6534afa1827 | -22.669001 | -43.692902 | 2024-10-02 01:21:30 | METOP-C | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ae9e74f-100b-3e6b-ac81-7f9af17e0d5d | -22.6758 | -43.7159 | 2024-10-02 01:21:30 | METOP-C | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ccb384b4-8744-3986-b9a8-dd85e289fe05 | -22.6595 | -43.696201 | 2024-10-02 01:21:30 | METOP-C | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 217e4fb6-eed3-3947-b80b-8b53bedffacb | -22.6663 | -43.7192 | 2024-10-02 01:21:30 | METOP-C | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c05d054-f2ce-3c84-9cdf-dd825ac68720 | -23.5028 | -47.210098 | 2024-10-02 01:21:32 | METOP-C | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8245a50e-4376-3c3a-b03a-52adc754fe2d | -23.506399 | -47.223701 | 2024-10-02 01:21:32 | METOP-C | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c5ba6a4-fe95-37b1-8ca1-222cb05650ce | -23.496799 | -47.2267 | 2024-10-02 01:21:32 | METOP-C | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a884239e-5f18-378b-92b5-475f7c3bc0f7 | -22.8974 | -45.073101 | 2024-10-02 01:21:32 | METOP-C | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2d46272c-5858-3f2a-83a2-a49ce1a70ede | -22.9027 | -45.091801 | 2024-10-02 01:21:32 | METOP-C | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36c184d5-be65-338a-be22-696a869905b8 | -22.887899 | -45.076199 | 2024-10-02 01:21:33 | METOP-C | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a068fc43-8c5d-34e8-b8a6-32b2dd92151d | -22.8932 | -45.094898 | 2024-10-02 01:21:33 | METOP-C | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2c7ffd19-04f8-32e2-ad0b-14eed7337482 | -22.898399 | -45.113602 | 2024-10-02 01:21:33 | METOP-C | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3bcfc2f3-130f-398f-938c-1b9790c0dc83 | -22.8783 | -45.079399 | 2024-10-02 01:21:33 | METOP-C | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9d650bd9-13a1-360f-b564-d3e386749c14 | -22.8836 | -45.098099 | 2024-10-02 01:21:33 | METOP-C | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db5d7f02-744a-3c38-bbb2-52beec708737 | -23.623699 | -49.8801 | 2024-10-02 01:21:41 | METOP-C | SIQUEIRA CAMPOS | PARANÁ | Brasil | 4126603 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 400f9c31-e529-3ae8-9063-64ce8ea05bf5 | -23.626101 | -49.889702 | 2024-10-02 01:21:41 | METOP-C | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ae72db1-b972-38fe-adb3-9c0f0be9ac4a | -23.1672 | -49.589199 | 2024-10-02 01:21:47 | METOP-C | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eee043cb-fc53-3741-89a0-3cd8c17dc3c5 | -23.169701 | -49.599201 | 2024-10-02 01:21:47 | METOP-C | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b9b9636d-1dff-37de-a93f-94af15d184d1 | -23.5149 | -51.101501 | 2024-10-02 01:21:48 | METOP-C | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8850c701-2403-354c-b453-9fe158ef59a1 | -23.516899 | -51.1101 | 2024-10-02 01:21:48 | METOP-C | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44b97cdc-5589-3c23-b05e-6f170daea307 | -23.503099 | -51.0956 | 2024-10-02 01:21:48 | METOP-C | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d8bf8011-06e8-39fc-932b-34897cb46e54 | -23.505199 | -51.104198 | 2024-10-02 01:21:48 | METOP-C | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67660d90-3d98-3d31-8bc0-7160d83e9e80 | -23.5072 | -51.112801 | 2024-10-02 01:21:48 | METOP-C | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8db1bc6-6322-3c39-af56-c9667d04a0ce | -23.708 | -52.6436 | 2024-10-02 01:21:50 | METOP-C | CIANORTE | PARANÁ | Brasil | 4105508 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f0c6a8e-a168-3ba7-bbcd-b4f4e0e4880b | -23.709801 | -52.651299 | 2024-10-02 01:21:50 | METOP-C | CIANORTE | PARANÁ | Brasil | 4105508 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 912efa5f-3c5a-34c6-8ba7-b455f0b79db5 | -22.5961 | -48.768799 | 2024-10-02 01:21:53 | METOP-C | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b1adf370-76f6-39dc-815b-c7f26c976421 | -22.3955 | -49.289299 | 2024-10-02 01:21:58 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| acc9c039-7a2c-3407-b6e1-287dad357f42 | -22.398199 | -49.299999 | 2024-10-02 01:21:58 | METOP-C | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11d85f64-a346-398c-b588-fb16347c398f | -22.3804 | -49.270699 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8e04d72-82ac-3517-a8b5-94f49969e288 | -22.383101 | -49.281399 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3af1bcda-7482-3705-a1a8-ece939d1bbc2 | -22.385799 | -49.292099 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f15067e2-c07a-3c93-a4f9-1251ffe63921 | -22.3885 | -49.302799 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7c766a9-22ea-34d5-8b56-d908fd63a620 | -22.391199 | -49.313499 | 2024-10-02 01:21:59 | METOP-C | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1082a0b0-516f-3c18-bfc4-70bd725d01e8 | -22.368 | -49.262798 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e3edff2-b15c-3163-b336-a2aad5de7d43 | -22.370701 | -49.273499 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 726cd4e9-84c7-3246-8cd7-c63505df103a | -22.3734 | -49.284302 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6e78c92f-b76b-34c5-8f65-0d4494e5329e | -22.376101 | -49.294998 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d110f5d7-260a-3630-ae1c-3dd2b7bcbac6 | -22.378799 | -49.305599 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9beffc12-bfe0-3d13-8b01-f58efbee08e7 | -22.3815 | -49.316299 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0056758d-67ff-3e16-9cdf-3d96d565d2d3 | -22.358299 | -49.265598 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 024994c5-d953-3268-b755-fb2a6b963639 | -22.361 | -49.276299 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa5f68bd-86b1-3bdc-a52b-08155a1c2f0d | -22.363701 | -49.287102 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e15015cc-153e-376a-becf-91359c2a9b85 | -22.3664 | -49.297798 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07dbf279-42d6-3efd-af9f-0ad70cc3e2eb | -22.369101 | -49.308399 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c044d036-da74-3092-8ef2-56031e8c8e3d | -22.351299 | -49.279099 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 124c3979-5fbf-3a31-9835-32ab58debd73 | -22.354 | -49.289902 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0cc000f-ba6b-34d4-b398-82d1b8d4b98a | -22.356701 | -49.300598 | 2024-10-02 01:21:59 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff33a5e1-1077-39c7-86c7-63e06880e3ec | -22.3594 | -49.311199 | 2024-10-02 01:21:59 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbf47ac2-ace3-38d1-99d6-74be4f830a0f | -22.3524 | -49.324699 | 2024-10-02 01:21:59 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03254b1f-b2d9-3b64-9539-7b75b7d53aaa | -22.355101 | -49.3354 | 2024-10-02 01:21:59 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c66d7cda-c242-30cd-b454-33a7b01781a7 | -22.0819 | -48.468399 | 2024-10-02 01:22:00 | METOP-C | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2dcf7eb6-50ff-3da2-b95b-e225f396c949 | -21.8857 | -48.474499 | 2024-10-02 01:22:03 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e3012cd3-7ce6-3516-b085-e84e3b3c7f05 | -21.283701 | -47.607101 | 2024-10-02 01:22:09 | METOP-C | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 63d55d8b-c283-3f59-9b1f-6e58aa2ee371 | -21.287399 | -47.620998 | 2024-10-02 01:22:09 | METOP-C | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cc1b503e-2f55-3a96-9091-e0ce15c2a2e1 | -21.274 | -47.610001 | 2024-10-02 01:22:09 | METOP-C | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 36785979-9664-3524-b029-47f8690988e4 | -21.2777 | -47.623901 | 2024-10-02 01:22:09 | METOP-C | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5bda191b-d377-3e3c-9533-4eedaa79aa51 | -20.524799 | -46.261398 | 2024-10-02 01:22:16 | METOP-C | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ecda5afb-6a84-3933-90f3-51328559215d | -20.5152 | -46.2644 | 2024-10-02 01:22:16 | METOP-C | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d64f9602-1729-3aa6-b782-6e97d5b3e626 | -20.514999 | -46.301998 | 2024-10-02 01:22:16 | METOP-C | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 158203bd-8468-37b2-8761-aceff7a17bbd | -21.634001 | -50.783401 | 2024-10-02 01:22:17 | METOP-C | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 58fdc72c-590d-36d0-8675-bb4d6f9934e2 | -21.636299 | -50.7925 | 2024-10-02 01:22:17 | METOP-C | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57af7714-42c4-30ee-92b6-e4d6b3eabee3 | -21.624201 | -50.786098 | 2024-10-02 01:22:17 | METOP-C | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1881e9e7-a3a5-3305-b2e1-0d1af2220d9a | -21.626499 | -50.7952 | 2024-10-02 01:22:17 | METOP-C | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 91cb95f4-93fd-35ea-a419-340ab55beb5f | -21.6287 | -50.804401 | 2024-10-02 01:22:17 | METOP-C | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc14a094-c37f-3ff2-ad2c-272a761fb4ef | -21.6145 | -50.788799 | 2024-10-02 01:22:17 | METOP-C | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1061130-80d7-3b0b-b940-7872e632069d | -21.6168 | -50.797901 | 2024-10-02 01:22:17 | METOP-C | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b1212802-c67f-3573-8e3d-d18136551f61 | -21.618999 | -50.807098 | 2024-10-02 01:22:17 | METOP-C | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba8c50bc-adbe-3771-af1c-1a7d71422903 | -21.621201 | -50.8162 | 2024-10-02 01:22:17 | METOP-C | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0cdfb50-826f-3aa0-ab26-fc5236c29dbd | -21.6071 | -50.800499 | 2024-10-02 01:22:17 | METOP-C | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e78b6e4e-64cb-31ef-928c-09d13cbdf65c | -21.5646 | -50.753601 | 2024-10-02 01:22:18 | METOP-C | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 946ce899-f2ea-3336-aa36-2e14b0b1977b | -21.566799 | -50.762798 | 2024-10-02 01:22:18 | METOP-C | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b5718e81-7ff8-3edf-970d-19e60b084ea1 | -21.5525 | -50.747101 | 2024-10-02 01:22:18 | METOP-C | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 626906b0-5c17-34ee-815a-ad5d69aea09c | -21.5548 | -50.756302 | 2024-10-02 01:22:18 | METOP-C | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c731b2bc-ea43-33e2-bede-48fed35348a2 | -21.556999 | -50.765499 | 2024-10-02 01:22:18 | METOP-C | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3acd9996-a1ff-3b40-9ba7-2b16c71be287 | -21.545099 | -50.758999 | 2024-10-02 01:22:18 | METOP-C | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b9549a10-7349-3668-92ca-63dbb02e0699 | -21.3724 | -51.029598 | 2024-10-02 01:22:22 | METOP-C | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ee41dbbd-04a6-3f43-9495-7aac10639584 | -21.3745 | -51.038601 | 2024-10-02 01:22:22 | METOP-C | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bdebaf61-e48e-368c-a272-208e28a94802 | -21.8906 | -56.110901 | 2024-10-02 01:22:32 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 39e4d540-71c9-3b64-897c-f03ae5640371 | -20.667101 | -51.4571 | 2024-10-02 01:22:35 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1e40bcb-0ceb-3b96-bc30-aa593e96a9ff | -20.6693 | -51.4659 | 2024-10-02 01:22:35 | METOP-C | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 374847a2-50e1-34ec-95c8-1f138ae1efd1 | -20.6574 | -51.459702 | 2024-10-02 01:22:35 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fba18555-7bbe-39ba-b7bb-77eca2d85f14 | -20.659599 | -51.468498 | 2024-10-02 01:22:35 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f1bee789-379f-3c04-b9bc-6bc2a7a45995 | -21.3398 | -55.6903 | 2024-10-02 01:22:39 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 164a7ea0-bb25-3e91-a3c5-1d47bc55979c | -21.343 | -55.705299 | 2024-10-02 01:22:39 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 216ad055-02e9-3494-9e6f-d69595767bd4 | -21.3414 | -55.6978 | 2024-10-02 01:22:39 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c9522560-5ae9-3db8-a21a-96dbadef5260 | -21.3479 | -55.6805 | 2024-10-02 01:22:39 | METOP-C | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README20.md)
