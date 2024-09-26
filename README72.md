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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56ec758f-0609-37ad-b643-6fd51e277b9e | -13.31705 | -46.34076 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53bf36e2-e15c-36b1-8d19-2c632487a6cc | -13.31417 | -46.33572 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81ca358d-c403-37bc-8e15-8e9afe1ef0e5 | -13.31341 | -46.34009 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a84c6f68-0930-379d-b523-28ed1199fb82 | -13.31287 | -46.32153 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 28290237-88c7-3c4f-b682-f65b2cb35eb2 | -13.31053 | -46.33508 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 748f0980-2c20-36bf-9801-5ef8e329a5af | -13.30928 | -46.32064 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ae7b6db8-23d8-3282-95c2-7a4529991bd6 | -13.30847 | -46.32534 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28a8d47d-e3f0-3be3-ab76-25de27b823a8 | -13.30766 | -46.33004 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5a4e86b-f8dd-3186-b9fd-90874f3056e7 | -13.30689 | -46.33447 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 355e1fb0-5821-3e09-ad85-190be2b9ae1a | -13.30402 | -46.32941 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26295cb7-dea9-3914-9bf2-0922a3d7dc3d | -13.30325 | -46.33386 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8029de83-00b8-3607-99a2-1b057ac296be | -13.28835 | -46.30917 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb7b8341-0552-3a7b-a29a-a00a0fc3830e | -13.28238 | -46.41096 | 2024-09-26 04:08:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 497caaf1-6f76-3c51-99f3-429600e27892 | -13.28229 | -46.41241 | 2024-09-26 04:08:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe70fa06-2922-3eb1-8f0a-1bc0b1054179 | -12.68178 | -45.858 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dab589c-d4c3-381b-854d-60d6313e757c | -12.67821 | -45.85732 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dea03b02-bf41-3955-9def-7532e196bf70 | -13.62893 | -45.94048 | 2024-09-26 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1d497f0-5fbf-3498-b59e-2e3aabcee631 | -13.2039 | -45.6643 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5667ed4a-bee2-3582-a7e3-d2994aeca255 | -13.20243 | -45.65155 | 2024-09-26 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ba4325a9-4b18-385d-a1b9-98ee9a613a0b | -13.20175 | -45.65559 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80fd517a-4137-3a19-a177-fd837b5dee0a | -13.20106 | -45.65963 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2044315-4a4e-3de0-9246-975f81f7a2f0 | -13.20038 | -45.66367 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 23bc5539-d7b7-3748-a7cd-81a95d3eca75 | -13.1996 | -45.6469 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 230475f3-d9b7-3720-aa95-b554dcb12108 | -13.19891 | -45.65093 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f180a17a-690d-3949-a634-93213d26fbc1 | -13.19823 | -45.65496 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7f34888-a98b-39b4-8aae-dd12caf5957d | -13.19676 | -45.64224 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c552dedf-6741-33f0-a790-d628a50d06e5 | -13.19647 | -45.64302 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1168a47d-2f50-3f24-ac3c-27624a51222e | -13.19608 | -45.64628 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4b832a0-fe77-3936-ae3e-32e7fbe67184 | -13.1958 | -45.64706 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48043bb6-21fa-3aae-840d-7ab47fbcd3b8 | -13.19462 | -45.63356 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f451e186-0514-3c85-8e32-d5648713e1c4 | -13.19428 | -45.63432 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd19cfa0-7b05-397b-96cc-5b5cd201a293 | -13.19393 | -45.63759 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e01ed582-123f-3ead-bf84-41504358a552 | -13.19361 | -45.63836 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3847c109-a9f6-3c87-9d8d-958af83e1f96 | -13.1921 | -45.62563 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7462c584-8567-355d-b4b4-06e5e2fb6bc5 | -13.19143 | -45.62966 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 84971500-70f4-32c1-b542-a41614cb70b0 | -13.18506 | -45.62438 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8a729c1-2021-3732-a5c4-4af71d9bd680 | -13.18221 | -45.61972 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 522baa16-74f3-336b-9b4a-5c13db43f2d8 | -13.17852 | -45.59832 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eca2debf-dcc5-3dd1-baa4-0087c789c2da | -13.16915 | -45.48124 | 2024-09-26 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 181f77bb-c1ba-338e-9074-b5494b405bb3 | -13.16632 | -45.47666 | 2024-09-26 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39e74066-9295-35ac-8167-ad4883e5f650 | -12.95685 | -45.29913 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 422da6c6-7a40-3fc8-942f-7b1f15eee53b | -12.95619 | -45.30306 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02ae1173-53aa-30f1-a24b-1cdcc2396a66 | -12.95487 | -45.31094 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51051464-212f-3b49-8457-33cf6422a01a | -12.95421 | -45.31488 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c685ac7a-a208-3f70-8213-3f0aa3a9d1ff | -12.95403 | -45.29459 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f692b065-d8e9-34a0-a2ba-e0478b61093c | -12.95187 | -45.28613 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97759e67-b878-39b0-a056-d1c99779b37c | -12.95121 | -45.29005 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e43af48f-7ccb-3c8c-af84-69b7b28f66e4 | -12.94839 | -45.28552 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a1df2f6-1caf-3604-8583-f31eb7f21178 | -12.92732 | -45.34687 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94788fb6-85c5-3e1b-935d-7d0565927289 | -12.92665 | -45.35081 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7efc7fb4-8edd-31f8-b44e-7ad41259b48f | -12.92101 | -45.34169 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d81a8aa-af23-3ab3-a3e5-3d6a989723c8 | -12.92035 | -45.33916 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbd2d1d1-0b95-3ecb-9d91-4720db696b5e | -12.91969 | -45.34314 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90118256-5b77-3de3-8bda-744607fc92f4 | -12.91904 | -45.34711 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d366af45-4aae-3732-9f02-6f69224a5656 | -12.91685 | -45.34505 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e2dcaee-91f3-32da-8297-4567d14563a8 | -14.6933 | -45.47707 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01bd06ab-9823-3637-88e4-a4c61659e0dc | -14.69265 | -45.481 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 850c0800-73c8-394d-a01c-32b1a950d9e1 | -14.68986 | -45.47646 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ff68002-0593-3741-9efa-7db6e5623f84 | -14.68641 | -45.47584 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 907a031a-9626-3a2d-b6f6-901461ae0a34 | -14.68232 | -45.47911 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b8888d2-2ac3-3777-b8fb-bd6b13b17102 | -14.67262 | -45.47346 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6621069-7782-386f-9dc3-d311bec97cdb | -14.60542 | -45.52266 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f41a2d1-46f5-34c5-b812-36e38adc3372 | -14.60197 | -45.52202 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56c73e84-c70c-3322-8f2e-d9d7dc757e08 | -14.5691 | -45.69832 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b223e12f-697b-37cc-998c-4ef9dcdef8f3 | -14.56859 | -45.72287 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 95119f40-8343-3747-bd55-309dfb60306b | -14.56843 | -45.70232 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8d5f47c3-bca5-3aa0-8efd-c870b270a2c3 | -14.56694 | -45.68977 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5c34958-5a19-3b46-9068-0a5c68166253 | -14.5661 | -45.67329 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5e2f023-040d-3e25-8f77-57f2aaba5c57 | -14.56577 | -45.71827 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1dc8e0a0-dc54-3f6c-99fb-28680662fa2e | -14.56561 | -45.69773 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f989301f-8637-38d2-ae1c-389bfaf56471 | -14.56511 | -45.72224 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e5b2eeeb-e80d-366c-b738-b85445bb41cb | -14.56495 | -45.70172 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c849c8bb-a2ba-3723-85df-77938de54b95 | -14.56478 | -45.68123 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df0853ab-4795-3846-8674-01b3f564c0f9 | -14.56428 | -45.70572 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04cdd276-5381-37d0-9bbf-be5d4e1b7e11 | -14.56412 | -45.68521 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aff1bfe3-c081-341d-b5df-7b1c0157f9bb | -14.56329 | -45.66872 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72f4fa85-d819-3df9-8982-4dfd07c80035 | -14.56295 | -45.71369 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ec94802-edfd-3144-8f7c-b5bdd184e3c0 | -14.56229 | -45.71765 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01eae56e-9c85-3c74-b090-014f0e9bcd1d | -14.55947 | -45.71307 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b5a33bf-670c-3db0-9742-041ba0b4e6e5 | -14.55915 | -45.67207 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f124901-b503-3e5b-a34d-039b96080ea6 | -14.55848 | -45.67606 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 92d94529-6bf5-3319-ab95-64d86128dd47 | -14.55665 | -45.70848 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eafbf573-b0f3-344a-9182-2f9023060027 | -14.55449 | -45.69993 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1376dfcb-77c6-3d68-9643-63e79009ef24 | -14.55383 | -45.7039 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13419f48-6690-3ee5-8c3c-8b4c71f92a54 | -14.55101 | -45.6993 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e750bf4-0816-3ce0-a981-3d06786bdc22 | -14.52356 | -45.64954 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e42b452-9a98-3f07-9c0d-81546703cd35 | -14.50885 | -45.63073 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d73e97a-a1aa-3e12-9d34-92238a392b9f | -14.50819 | -45.63467 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 888eedbf-7825-309e-962e-76a45a22aa45 | -14.50605 | -45.62618 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7726321c-9021-3f67-a996-0df977113019 | -14.50538 | -45.63012 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c5aff96-ac82-3a19-81e9-5824485dc2fd | -14.50434 | -45.62651 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e126419-947f-3c10-993c-fe9788bf6937 | -14.50368 | -45.63045 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ac7118c-8b4e-3e07-acae-83973fed3740 | -14.50257 | -45.62557 | 2024-09-26 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72ded54e-3758-3b76-886d-045037d4fd21 | -14.41352 | -45.30306 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce548f6a-bf8d-33bb-9b27-023ea319dcda | -14.41288 | -45.30691 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5f2cfde5-8510-34b8-aee3-17a78cbc6e58 | -16.56276 | -46.93664 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73cdc13c-3a1f-3a2e-be90-9cfd5a55db7f | -16.55917 | -46.93596 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 172e475c-1a5a-3111-b8f0-3b7460d470f6 | -16.55558 | -46.93527 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fc919d1-6346-3c7f-9583-3233127ca9f2 | -16.55486 | -46.93945 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b86bafcf-ea17-3e90-8fea-b66ef4291a6f | -16.55127 | -46.93877 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README73.md)
