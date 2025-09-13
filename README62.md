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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fc7ae55-2bb7-3f15-8eb4-a655020ff36f | -19.16211 | -46.66141 | 2025-09-13 04:10:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26bcf6c9-d501-3b24-988d-b86289a8de13 | -15.03989 | -50.16717 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab029a7a-14b0-3be0-a92c-c5d1c9c73828 | -20.69491 | -46.08147 | 2025-09-13 04:10:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d1a3cef-412c-3adc-92f7-23abd44fbdb3 | -16.33523 | -51.53535 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1d619b29-cf89-362b-a447-c6557dc43175 | -15.16665 | -52.48665 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b20bc55-e356-3d8d-80d4-794b27be1708 | -15.71209 | -50.59069 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 46a54fd2-de2c-3ede-9d54-527e85125ab8 | -15.20851 | -56.69312 | 2025-09-13 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 94267a2e-3fc2-3d1b-941f-d6a66f5a71ee | -15.0964 | -50.1834 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52e6e937-4467-3771-a5c9-979bb6b5aacf | -19.97749 | -46.90682 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb236f67-ab54-3af1-98a2-9499536fc86c | -16.33998 | -51.53613 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e50cff3-6b36-3b31-8aa5-9a4b74b9d0b7 | -21.62103 | -46.80668 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 0cc7f0f4-5905-3525-9854-f35da926fcea | -15.76868 | -52.2392 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7251118-d39c-304e-82a1-778d9bf5dbd5 | -16.64326 | -49.79062 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8b28359-7631-3921-b152-5b118a3db192 | -18.4478 | -47.18736 | 2025-09-13 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 849e9f7e-49d1-30a2-9741-526b7ea126ef | -21.63314 | -46.79707 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f22f99e2-fbe2-338d-a9fd-3c7f5582e1c4 | -15.37509 | -52.10843 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b2250311-68a3-3419-93d7-d15003e54b9c | -21.32271 | -44.98873 | 2025-09-13 04:10:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 24a62e95-b906-38f7-8226-e44a912b5865 | -16.36389 | -51.54338 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aabd4f50-7a10-30c6-aa32-c1b21db23e81 | -16.1498 | -46.95233 | 2025-09-13 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29789484-7306-3686-b7a4-782634ba0a81 | -22.61418 | -47.66314 | 2025-09-13 04:10:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9cdf936f-610a-3ae5-b6fa-4b7914b5edd4 | -15.50861 | -47.29539 | 2025-09-13 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45e63470-a4aa-3f50-8117-a2e7095aa1af | -18.70542 | -51.78344 | 2025-09-13 04:10:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 495b779c-166a-3539-bc35-9f4aac719cb0 | -16.00922 | -47.95018 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaafdaa4-2390-36ee-b82d-0c674be8be29 | -22.17887 | -49.61203 | 2025-09-13 04:10:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ee7a887e-e2d6-3eff-b2f7-f613f3c5da91 | -17.33887 | -46.66629 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e601e61c-d690-33d1-b85a-8f3b7644ab1b | -15.50936 | -47.29101 | 2025-09-13 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d79f675-13e9-371e-91d1-631040fc4803 | -15.08327 | -48.10275 | 2025-09-13 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 484e71fc-37f0-3879-8734-1a1bbf5afbdd | -16.02604 | -47.94359 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4ebe5a6-0a6c-35ab-b5d1-19f706f24fd2 | -17.13893 | -48.51298 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cfee0ef0-dfc0-37bf-80ff-96e816062299 | -17.92391 | -44.44905 | 2025-09-13 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d7ecf48-2727-3a00-aea8-16c52a891fe8 | -19.15185 | -46.6592 | 2025-09-13 04:10:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e39deb4b-c6ec-33e5-a7b1-2abffe34ccb9 | -16.41055 | -49.03255 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05a68e96-d9e2-3b70-8356-df6473595828 | -15.14647 | -48.31281 | 2025-09-13 04:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f6e64fd-ba89-3483-8786-8fc127bcbe11 | -15.55115 | -54.80458 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c44fa3a-7505-3aa8-bfe3-8b71f793757e | -16.39503 | -49.06829 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54f01585-0d9a-3827-b2a9-b10df7d6dc20 | -18.89814 | -47.05877 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| faa3ba87-f49a-3062-bcaa-bdc386151374 | -16.97523 | -45.81992 | 2025-09-13 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63dff69b-ed1c-30ea-b4d7-4a68ecd75051 | -16.5001 | -55.11962 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 326b3164-a3d8-3858-89b1-b97a80d568f6 | -16.60712 | -49.46672 | 2025-09-13 04:10:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cbd6ac61-e7c4-30ad-bfd4-5698d37a23e9 | -16.13259 | -48.88002 | 2025-09-13 04:10:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71d1a5bb-af97-339b-9ea8-20241b5ec87d | -17.28644 | -46.10028 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 91594d1e-415d-3561-9625-8ceddb6058db | -15.68218 | -49.90441 | 2025-09-13 04:10:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 26cb6599-823f-3e71-bfa6-5f4e292cad09 | -20.60291 | -50.40789 | 2025-09-13 04:10:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 96a87cdf-f8d5-398d-a8e3-59a8617bede6 | -16.42905 | -45.70597 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88664fc3-298c-3cfc-a745-e2fe4fd1ed58 | -18.5957 | -47.1914 | 2025-09-13 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d13ef5fd-62c2-39d6-bca0-60618e30ef64 | -17.36211 | -42.70477 | 2025-09-13 04:10:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d6527d6-52a4-3534-9453-48a3590d0e31 | -17.37448 | -52.90932 | 2025-09-13 04:10:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1fb2de2-d7e5-3e82-b9d9-f44323241807 | -17.42058 | -49.25683 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a5e83d6-fb4a-3cb7-bdb8-26c322f655b9 | -18.13686 | -48.45387 | 2025-09-13 04:10:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59f08111-121d-345d-9ec7-8af1d788f933 | -20.29099 | -46.59093 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cae85d2e-948d-3c98-b90e-c0ab5566c23b | -15.14536 | -52.4864 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2418b2b-1351-3399-9a11-ce1aeb146b3b | -17.95135 | -45.26783 | 2025-09-13 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70a9ac0f-f363-3ddb-b83e-090e479054cc | -15.12311 | -52.46419 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b1011f8-910b-3f4a-9ebc-20fc0dcba6dd | -16.24757 | -50.06416 | 2025-09-13 04:10:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 375145cc-5bbb-36c2-b7b0-dd881c0fdc6d | -19.33307 | -45.11202 | 2025-09-13 04:10:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2c459a05-9065-3f2e-8e2a-e3fac2cee756 | -16.64921 | -49.75867 | 2025-09-13 04:10:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a34ce0b-337c-3355-bb4d-203d451058c7 | -17.40992 | -49.2471 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1def8112-49fb-36d1-9e55-6ec8102e84f2 | -16.53273 | -51.7408 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 53f1b586-2bbe-3da6-932a-d2767f6eef5b | -18.34926 | -47.0204 | 2025-09-13 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22741344-4a06-3c4a-b4ac-a868ce619474 | -22.18305 | -49.6162 | 2025-09-13 04:10:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 250128c2-cda1-381a-aa35-9eca02ceef83 | -20.33775 | -46.66758 | 2025-09-13 04:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 065f785b-d15b-3e29-9e83-7a3604355658 | -16.97588 | -45.81608 | 2025-09-13 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c5ed51f-41c4-3e2e-85ba-231a73d4ff90 | -17.42188 | -49.24969 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9d56b5f-81d4-34f3-91d0-a5855ac54e75 | -17.42245 | -49.22388 | 2025-09-13 04:10:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16c30cdc-d7c8-3c38-a37c-a136cfb02a82 | -15.11273 | -52.48933 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1dac998b-385f-3d3d-ae7f-8f3753ab719e | -19.20423 | -44.62067 | 2025-09-13 04:10:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 31f4b9cc-632e-39e6-adbb-e6fe2d9aabd1 | -16.08512 | -49.95864 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 18a383ad-3e6e-3845-ad79-19abb6ecd39b | -17.96093 | -46.93503 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2c4fb21-6d65-3e36-934a-1ad2d0587772 | -19.60419 | -44.83976 | 2025-09-13 04:10:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f03f90b-be17-36c7-8447-2379e22b1b66 | -17.92333 | -44.45267 | 2025-09-13 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6450f410-393c-3555-a003-3e606cfc754e | -17.58556 | -44.29143 | 2025-09-13 04:10:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02b29dc5-e5fe-3992-acf3-ea73dd995692 | -15.32245 | -52.90636 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cf93bde-71a0-30d9-a531-a38993e1471b | -16.42564 | -45.70536 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06e36229-a148-3a09-9a9b-6db5009a3d7b | -15.07959 | -52.49459 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3053a27c-e3c7-3b72-a863-841e14bce0df | -16.29526 | -48.87883 | 2025-09-13 04:10:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83a38092-e45b-32f0-821a-2f58049eb26e | -17.29108 | -47.25825 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08ff213e-8f44-3626-9a20-9baaae62edf4 | -16.50599 | -55.12092 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4b158bee-0f8e-3131-a3c4-fec5d24bd711 | -15.20668 | -56.6887 | 2025-09-13 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3daf8df9-5583-3820-82ed-4c70941af792 | -20.10106 | -46.92457 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c5376e8-4b93-36da-9b72-4d6fa2c7f1c6 | -20.46466 | -54.56458 | 2025-09-13 04:10:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31d58f13-9ee2-3994-864f-497d349c5a4e | -16.08586 | -49.9547 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3905cd8e-9dfc-338d-af34-2367fce633bb | -16.2886 | -45.68554 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59fcea17-2bbc-3cd3-a478-3105950b8992 | -15.28904 | -53.78195 | 2025-09-13 04:10:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c311213a-4720-3eb6-ac2d-e3950b1d10ca | -16.28178 | -45.68432 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8a1e956-be1a-376a-879f-111d2d233d44 | -22.17639 | -49.6096 | 2025-09-13 04:10:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d597d51b-bea3-375d-9d94-a0436b5539b0 | -16.0773 | -50.00077 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 45eab8b0-ed23-3465-9d88-773b785478a4 | -18.59923 | -47.19205 | 2025-09-13 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc15620b-58ab-3c7b-b5fc-0ee5716e903b | -15.14428 | -52.4918 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4a62c5a-00bc-3a7f-846e-9339a94eb811 | -16.36344 | -51.5416 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 461af771-fce0-3462-b9d7-c062329033f5 | -15.20319 | -56.68571 | 2025-09-13 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 40204fd0-82a0-3454-948b-48df17619af5 | -16.0894 | -49.95949 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 70f0a4df-dcf0-3bf7-8ce0-b84483bf58b3 | -15.58553 | -54.75753 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2fc5a2ec-9476-33d6-af91-124a415a29cd | -17.49874 | -44.3247 | 2025-09-13 04:10:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cb20e58-0024-325c-a1b7-1ba9e0384e3b | -17.40411 | -48.22247 | 2025-09-13 04:10:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0be1d949-dd6e-36c4-8ad9-bfc5e08fb2fb | -18.33083 | -50.97007 | 2025-09-13 04:10:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9b0e977-a866-3767-98c5-9f9626a231d1 | -16.42627 | -45.70153 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d26e851-c57a-3319-8640-c8d3b6d47606 | -17.9567 | -46.93861 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0666aa48-c7f7-3999-94b2-ccee3721526b | -18.1786 | -45.20864 | 2025-09-13 04:10:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f68f3942-7484-3824-b1c1-23b8a4235442 | -18.85134 | -46.8409 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cf6e1fe-38f8-3062-b6a1-6eab7dc20448 | -16.84497 | -40.8544 | 2025-09-13 04:10:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README63.md)
