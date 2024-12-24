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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0e0e18c-d277-3173-9501-03a32f8dcc2d | -10.79825 | -36.95021 | 2024-12-24 03:49:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 79b1a2ca-31b9-3381-afd2-5298f9fd0268 | -7.90915 | -35.21287 | 2024-12-24 03:49:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 72a58bf0-6462-3cb7-8881-5506bc02143d | -6.97001 | -43.54494 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2475bb20-9704-32a0-833f-4229deb76775 | -8.0652 | -35.15485 | 2024-12-24 03:49:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8bc6691a-30e9-3c8c-a94a-d31035b2a860 | -5.53562 | -42.85101 | 2024-12-24 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a25f2b8f-b2e4-348e-8557-e82058822fde | -6.9889 | -43.27314 | 2024-12-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3ac16d5b-d10b-3c27-a404-de7123130014 | -9.16688 | -35.49465 | 2024-12-24 03:49:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1dedc7c1-e50f-3ca0-b982-bdbf0bc46e8c | -6.20863 | -42.64034 | 2024-12-24 03:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9dffc1da-8cd0-3084-80b4-4d3e0f8b69c3 | -7.82109 | -35.19255 | 2024-12-24 03:49:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 976774b4-6118-3c96-9230-77df7926033b | -5.83887 | -40.68982 | 2024-12-24 03:49:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d48dbdab-8205-3f1a-8d0d-b23b271b43e1 | -6.97387 | -42.99664 | 2024-12-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9dca55c6-261f-3189-82a0-d15a0047bf1e | -6.97809 | -43.55077 | 2024-12-24 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9488ce3c-ee5a-318c-9551-8c25cc7dc1e0 | -4.52707 | -45.82536 | 2024-12-24 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf3b93f9-09e2-384e-a7a4-34379c6ee1f1 | -4.53185 | -45.82987 | 2024-12-24 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fc9cc1a-a79a-3385-bff0-baa0c4f05525 | -4.1506 | -43.64655 | 2024-12-24 03:49:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13cda2d6-36cd-390c-880e-64e454657d96 | -7.87836 | -35.2543 | 2024-12-24 03:49:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 64335b22-49a4-334b-bacf-2792f6fcdcfb | -10.59876 | -38.41051 | 2024-12-24 03:49:00 | NOAA-21 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37be1aa3-c633-3c59-8680-752a9de36102 | -8.47378 | -40.66933 | 2024-12-24 03:49:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d3d2f31-5c9b-31f7-b68d-4615f29d9542 | -12.71287 | -40.21333 | 2024-12-24 03:51:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 492a9b4b-3772-3f1f-9688-25c6fa8f78b8 | -11.88038 | -40.95073 | 2024-12-24 03:51:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7fe38f54-f40c-320e-a412-7241af378c92 | -12.71348 | -40.20958 | 2024-12-24 03:51:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee846693-55be-3a25-9dfe-e42d4579001f | -13.14284 | -39.29629 | 2024-12-24 03:51:00 | NOAA-21 | LAJE | BAHIA | Brasil | 2918803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fb29f18e-31c7-3195-8eb1-043ac27716d0 | -11.78394 | -41.31415 | 2024-12-24 03:51:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d41e166-c874-3a8d-827e-07a125e278f5 | -12.18299 | -41.35743 | 2024-12-24 03:51:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 970723a8-ad59-379e-8f1a-d510628d9a3e | -12.71688 | -40.21015 | 2024-12-24 03:51:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cad3de29-e53e-3e99-8ce3-b93b45f2b6d7 | -13.56003 | -41.29165 | 2024-12-24 03:51:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 262e7f5b-7782-3eb1-b047-5558efe0098e | -12.18658 | -41.35797 | 2024-12-24 03:51:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4ffb8260-2884-3779-9ac2-eb130e40be17 | -12.49655 | -38.43507 | 2024-12-24 03:51:00 | NOAA-21 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0a578c73-1323-3f87-80a3-ea729876c741 | -13.56355 | -41.29223 | 2024-12-24 03:51:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 63cb8cf1-73c4-33e0-b245-f5ca2a467cc3 | -13.39581 | -40.44456 | 2024-12-24 03:51:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dd9baa0a-448f-33fb-bf94-bc8e84e26421 | -12.815 | -38.26688 | 2024-12-24 03:51:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e5de658b-b1f3-3846-b53d-203f87406304 | -23.82857 | -47.85566 | 2024-12-24 03:53:00 | NOAA-21 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d8359aca-b33d-31af-8055-df39cee3502f | -22.54125 | -48.8139 | 2024-12-24 03:53:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1b75166-f43a-331c-aa2f-e454f0afe3fa | -2.34966 | -45.5854 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 26.4 |
| ffb9da97-f2ed-3acd-94b7-eda898e17807 | -2.64555 | -46.11274 | 2024-12-24 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32aee114-1eb4-3c07-b347-2002cd1acdf4 | -2.96269 | -40.29361 | 2024-12-24 04:12:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f8ca8802-e188-39ec-929e-90a6706e9257 | -2.62609 | -46.11429 | 2024-12-24 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f5722b8-0f7d-33e5-a0fc-44443f1e85a1 | -2.34903 | -45.59116 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae2074f7-aec2-3a2a-b081-f209cad244cb | -3.53815 | -40.91916 | 2024-12-24 04:12:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 70acd088-ccc9-3dd8-86db-d745a299ae17 | -2.35035 | -45.58117 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 1d5e6421-6625-37ae-92f6-9c21bea8e3fa | -2.64842 | -46.0949 | 2024-12-24 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 641cd1b6-6720-3ffb-88bc-caeaaad1457a | -1.35921 | -53.71118 | 2024-12-24 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a6fef54-eb3e-3924-b7b3-17c42eeaf979 | -2.75874 | -45.71116 | 2024-12-24 04:12:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98298295-69f8-3003-8e93-ce4fb05283a2 | -2.21185 | -45.4459 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88935c74-face-35cd-9d0e-85202571a33f | -3.5279 | -40.78268 | 2024-12-24 04:12:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a74b872c-3af6-3ffc-b885-63167ce8f49a | -1.35291 | -53.71011 | 2024-12-24 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbfa4fd4-490f-3601-9c31-1ccf1918c442 | -2.76385 | -45.10129 | 2024-12-24 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 745421c9-28c6-3693-a7e5-b04a574d04b6 | -2.7645 | -45.09729 | 2024-12-24 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3fe59dcd-5517-36cd-959f-d371084fde95 | -2.64468 | -46.09428 | 2024-12-24 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cd6ce50-e14d-39ef-8437-3d09219716b8 | -2.11124 | -45.49089 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19f27b13-36d0-35df-b306-5425e76c27bf | -2.34897 | -45.58963 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a438f31-8f90-3bc6-8756-95d83d0af8bc | -0.93359 | -46.89474 | 2024-12-24 04:12:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93a39e14-291f-3759-ba83-ec2ca5bb080e | -2.99561 | -40.39114 | 2024-12-24 04:12:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 560b0f69-d239-3a14-a488-af712efdc661 | -2.35262 | -45.59021 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7249edde-ad00-318b-a03e-7c420cb2d489 | -2.35331 | -45.58599 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 1e62879e-d20c-3670-b2cd-c2a4320f8828 | -0.93011 | -46.89062 | 2024-12-24 04:12:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 303ed028-dfb6-3a32-9d55-7fcef139604d | -2.34671 | -45.58209 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 24711abb-6b29-34dd-ad71-79334aebf9e5 | -2.04065 | -46.46742 | 2024-12-24 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cb67029-0b72-3bf4-8203-5a504a4d92b3 | -2.10759 | -45.49032 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67fe5de8-d03c-366f-af54-03621045cec6 | -1.35663 | -53.71262 | 2024-12-24 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 698eaddb-2496-36fb-a0b1-2a57e253696e | -2.354 | -45.58176 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 893ed23b-4cef-3178-b52a-0314b4644b4d | -2.01388 | -45.59032 | 2024-12-24 04:12:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ad3ceab-12fb-36c0-a460-86e0a2b50fcf | -2.77224 | -45.09444 | 2024-12-24 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 6e4014e3-6b3d-32cf-91b7-f7e7398e3932 | -2.77514 | -45.099 | 2024-12-24 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a41b865a-801a-3fe2-aa7a-192c656da8af | -3.52809 | -38.985 | 2024-12-24 04:12:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a77b53b7-d1b9-3cae-89cd-1e492c7f391c | -2.34604 | -45.58633 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 78e826b9-416b-322c-87b4-f7a979c81804 | -0.96276 | -46.78688 | 2024-12-24 04:12:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24b3a371-1b34-30e6-aa73-3e6e4613bef0 | -3.63776 | -40.47934 | 2024-12-24 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6caa87cd-b1b4-355a-8c75-97be371a65f7 | -3.6447 | -40.48028 | 2024-12-24 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 97863282-0319-3d6f-a7c9-a7d6d947e999 | -2.35268 | -45.59175 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d327018-4029-3da0-9e97-e20140910d36 | -0.95876 | -46.78625 | 2024-12-24 04:12:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 585290ef-bf4e-3a9c-82e7-816dd7c15972 | -2.76869 | -45.09388 | 2024-12-24 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 3e4e37c7-cd96-3e22-b45b-9d70fcd86242 | -1.35033 | -53.71148 | 2024-12-24 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16ca6d54-e6f2-31e2-bf84-f2ea4d92c81a | -2.73674 | -45.87482 | 2024-12-24 04:12:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edc2bdc3-a69c-3391-904a-2a1da6c5f95f | -2.29167 | -44.87719 | 2024-12-24 04:12:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47cf752c-66ff-3d32-ad38-23ab360689ab | -2.09065 | -45.3633 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e8d8919f-807a-3290-89a9-478b59d3d8c4 | -2.35335 | -45.58751 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a6d59128-7956-310f-8e6d-27772b2b354c | -3.6424 | -40.47224 | 2024-12-24 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c136d1f3-3cae-3e53-8766-ceaa2ab2d45a | -2.75807 | -45.71541 | 2024-12-24 04:12:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa3c2117-a734-343c-93ab-02f705ca71ac | -2.62984 | -46.11487 | 2024-12-24 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 488540e6-0ce4-3d8f-b47d-4c36bbd05f61 | -1.64126 | -45.84899 | 2024-12-24 04:12:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d196c16a-8bfa-327c-bf3f-b1a4750a28f5 | -2.99503 | -40.3949 | 2024-12-24 04:12:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c2cfbadb-e6b6-3164-bb6f-12e4270f2efe | -2.35401 | -45.58327 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b3e08369-f56d-38e1-a56c-9cb9ba34d7c0 | -0.93413 | -46.89126 | 2024-12-24 04:12:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 451bda74-f54d-35ad-89f1-2f49e17ebe63 | -2.60872 | -46.07933 | 2024-12-24 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e501992-891c-385b-91df-8c6d2719c1fe | -2.08635 | -45.36688 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b9d5ca52-eade-3068-968f-2438f62f5f08 | -2.34969 | -45.58692 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 91d4af81-e454-3d87-9f32-d0be419ed80c | -2.99216 | -40.3906 | 2024-12-24 04:12:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2646f43b-984a-309a-bf71-57e64416e06e | -2.19306 | -45.6817 | 2024-12-24 04:12:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e4a5fab-474a-3cd0-870d-df56ae9bd0e9 | -2.73563 | -45.87292 | 2024-12-24 04:12:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 627fd623-a839-3365-88d2-fe1fb450cbb8 | -3.00076 | -40.00581 | 2024-12-24 04:12:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4e5829a-2f32-3f16-bb83-66f991027d88 | -2.60944 | -46.07489 | 2024-12-24 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f17675e-09cc-3561-8bbf-7f619979ce1a | -2.11786 | -45.49624 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9710783a-0a4d-3ea0-b550-99707476ccfe | -1.62349 | -46.11052 | 2024-12-24 04:12:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f59518ca-6f85-3f4e-98b3-ca00446f585b | -1.94291 | -44.78131 | 2024-12-24 04:12:00 | NPP-375D | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9eb3c9d-5519-3c32-a26a-55517ef54b78 | -2.09131 | -45.35914 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fdcce380-475c-3e03-b89e-b17f7b0ebef6 | -2.64396 | -46.09875 | 2024-12-24 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f359a431-8793-3412-89b0-04318af2d932 | -2.08702 | -45.36274 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3483a59f-e0d5-3428-8a62-fe124c664780 | -2.76804 | -45.09787 | 2024-12-24 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 1641e618-8745-3b68-b47f-a2226e94aa3b | -2.2923 | -44.87326 | 2024-12-24 04:12:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README6.md)
