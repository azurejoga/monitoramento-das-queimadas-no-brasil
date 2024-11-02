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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4784543f-35f7-3fbe-b81d-2379b3be66ff | -4.44553 | -44.16967 | 2024-11-02 03:47:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8046d32f-fe5d-3bc9-a368-894a5999b417 | -4.44213 | -44.16439 | 2024-11-02 03:47:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cca41570-cba9-367e-b2de-3bfb861f14fe | -4.44117 | -44.16995 | 2024-11-02 03:47:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28b7edb3-d61c-3b2e-8c35-9af9cde75771 | -4.44058 | -44.16893 | 2024-11-02 03:47:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2cb8583d-2078-3394-9ea5-c16ea1abf825 | -4.18184 | -44.24941 | 2024-11-02 03:47:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8234f85-61c7-3a7e-b4e3-b84dea31ddf8 | -4.17685 | -44.24862 | 2024-11-02 03:47:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2c2a293-4faf-359c-b546-a7edf2a900f8 | -3.8375 | -44.13427 | 2024-11-02 03:47:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8b456a4-fc44-3343-aa5c-382fd0bd18a3 | -3.83655 | -44.13995 | 2024-11-02 03:47:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1106cb59-fa39-305b-8b4d-308f32263dd5 | -3.83253 | -44.13346 | 2024-11-02 03:47:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 540dd73f-a613-3081-9237-2ccd06121425 | -3.83158 | -44.13911 | 2024-11-02 03:47:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9df45d8b-02cc-312c-acc1-b73581979c1f | -4.45435 | -43.63649 | 2024-11-02 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b93bc5b-69a6-3e75-b2b5-a8f4acd1cec6 | -4.45045 | -43.63067 | 2024-11-02 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 771fa5a6-fdd5-3b8c-b2e7-09ed46d57059 | -4.44959 | -43.63573 | 2024-11-02 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9118e6c1-b525-3045-b565-2bee1c3530df | -4.44873 | -43.64083 | 2024-11-02 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9c3e60e-2917-3ae6-9c9d-d39b5b5bfbb8 | -4.44787 | -43.64595 | 2024-11-02 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 842128be-50cf-3af4-a437-cb302c7f8b03 | -4.44569 | -43.62988 | 2024-11-02 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 254e9f32-24e2-3893-b2cf-bacd72fed613 | -4.44483 | -43.63498 | 2024-11-02 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dda89190-85ad-393d-8e33-0b93949dd15a | -4.4119 | -43.47733 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb1b67b3-9cd9-3bd2-8493-20b5c5882eb5 | -4.41108 | -43.48232 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f122943d-6099-349f-861a-d1c7c768c8ee | -4.40885 | -43.46656 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1fc1289-9efd-3569-a4a9-c12ebc7756a1 | -4.40803 | -43.47151 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed0b261f-95af-311b-b407-628a5bbae817 | -4.4072 | -43.47651 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d95419d-20d5-369c-be8c-b530f59de6d1 | -4.40637 | -43.48151 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8387ab71-9942-3c0c-93f4-ba6d7df5e7a4 | -4.40334 | -43.47064 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcf4a315-0cce-353d-a9cb-8e3e013d8abd | -4.4025 | -43.47569 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 28ff6a68-19b7-323f-92ce-06b1ca156849 | -4.40166 | -43.48072 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bcf55986-8482-3783-8925-6bdd008d6f74 | -4.40084 | -43.48569 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24f286ec-59ce-33dd-a7db-0bfd99591994 | -4.39945 | -43.46496 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fd15bca-dc89-3451-aba1-de0b91b4c58d | -4.39863 | -43.46989 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a0374f0-7fce-30c1-a204-aa42fe221714 | -4.39556 | -43.45927 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 75001263-9957-3b4a-939e-9e543d1c7681 | -4.39531 | -43.48979 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 626e9fda-cc52-360a-bf61-02b20311a75d | -4.39474 | -43.46421 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 209bae1c-d0c4-3fd7-836c-a19d8e4460e8 | -4.39144 | -43.48398 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 929b6a4c-7dbc-3084-87aa-9646f7c8209b | -4.39085 | -43.45851 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8eb75820-4430-3da1-a122-fd0b272038e9 | -4.39062 | -43.48892 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c1e3b151-cafe-3950-b17f-abea7f854c51 | -4.39003 | -43.46344 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3d91d4e6-a5a9-3dc8-a71b-73ec8905cf50 | -4.38615 | -43.45773 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5e9f4aa-7cc4-3280-bc7b-6a3ce522cb83 | -4.38533 | -43.46264 | 2024-11-02 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d1abdba-d4fc-37c8-948e-f7896534915a | -3.77969 | -43.54565 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 966b9c87-9c31-3505-b40e-63b8ab7a025d | -3.77906 | -43.54865 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f6ef9238-3ed6-332b-b04f-4adebec3f163 | -3.77885 | -43.55083 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| baca425f-4174-3ce9-b248-20f37a956f3a | -3.77818 | -43.55384 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3a3e607d-b49f-3c31-b12d-e8080d9f1076 | -3.77802 | -43.55595 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 424747fa-d056-312d-b62f-9eecd162f24a | -3.77493 | -43.54474 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 748eb358-80d6-3c1e-bf08-3df472b1aa93 | -3.77431 | -43.54773 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9f00e96a-e945-3b9c-8589-a6972e5e0808 | -3.7741 | -43.54986 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a051ab9c-68d4-334a-b040-91d037943575 | -3.77343 | -43.55289 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fad7f5f9-2de3-39af-8863-e3b779ff9978 | -3.77325 | -43.55507 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c77944c8-45cb-3108-93de-55db205e2781 | -3.77255 | -43.55804 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2d31ae12-35a0-3139-b4a4-4594fe713fdb | -3.77126 | -43.53683 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78514856-8536-3cdc-9ffc-bf46742fc5cd | -3.77099 | -43.53885 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbc3e917-7117-37b7-a300-e2f3d935dcaa | -3.77041 | -43.54177 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 37fe94d9-fd3f-32bd-a72e-d1475cc6e6b2 | -3.77017 | -43.54384 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 671276f7-9614-390a-9960-4a7e2bcfacba | -3.76955 | -43.54681 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d3d363ed-8323-319b-a943-7a97612d2a03 | -3.76934 | -43.54897 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fe33e59e-3c99-3494-b176-ebaedc008868 | -3.76866 | -43.55201 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fa12092e-6389-35c0-897e-c8dd45573dbc | -3.76849 | -43.55415 | 2024-11-02 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a3af6979-6458-3106-afbf-d5e075d0f053 | -6.96986 | -45.19202 | 2024-11-02 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd77bed4-3082-3565-8789-e09529ec2019 | -6.96431 | -45.19381 | 2024-11-02 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e9f6da4-9da9-3c3d-ace8-63b55f6a2aee | -6.96328 | -45.1996 | 2024-11-02 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4ec176e-1101-384f-accf-1e95d86581d1 | -6.96276 | -45.20254 | 2024-11-02 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb9a241a-54ea-3622-bea5-79801263c002 | -3.41118 | -44.98457 | 2024-11-02 03:47:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61511b13-a6e8-3f6f-a79d-7eb828090cd6 | -3.40588 | -44.9837 | 2024-11-02 03:47:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edcd0385-2f87-39a8-93f7-c6d6f5e6fa75 | -3.40534 | -44.98696 | 2024-11-02 03:47:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93ab6d44-a967-37b9-bf9a-ecfff4efd87b | -3.226 | -44.42289 | 2024-11-02 03:47:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c1e96f4-40f0-3dec-a2f5-7ae8120084a4 | -3.11197 | -45.09796 | 2024-11-02 03:47:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f37ab8d-2dfa-3cc2-a421-a74c9d8f1561 | -3.1066 | -45.09706 | 2024-11-02 03:47:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63bb9a33-ab9f-332b-9e0d-3ed783de4063 | -3.07822 | -45.1338 | 2024-11-02 03:47:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8b459346-daa3-3cc9-a514-836eb93eaf70 | -3.07764 | -45.13718 | 2024-11-02 03:47:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b39f92d2-84d0-3f24-9377-9132a08c55b2 | -3.07604 | -45.13324 | 2024-11-02 03:47:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 720d065c-fd43-34d6-b12b-03b5b0524453 | -3.07549 | -45.13662 | 2024-11-02 03:47:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 707f8567-39ed-3057-bdb5-2342a3d846e4 | -2.64678 | -45.77431 | 2024-11-02 03:47:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58c18c6f-f3a9-3864-814a-9dfd66a22648 | -2.64516 | -45.77171 | 2024-11-02 03:47:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7e90145-320d-3dae-b162-44ca9793ef36 | -2.64454 | -45.77549 | 2024-11-02 03:47:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07ae746b-be12-3ebc-aa5f-6444a4a27b3f | -2.63888 | -45.77455 | 2024-11-02 03:47:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dfb9a33-91af-359a-ac03-2caaae2dd02b | -3.37647 | -45.70167 | 2024-11-02 03:47:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 563524d7-448a-398b-b6b3-4c78209b47bf | -3.37585 | -45.70535 | 2024-11-02 03:47:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3137937-22ed-3e49-8fc7-d38bee467e6c | -3.32355 | -45.41291 | 2024-11-02 03:47:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11b16350-8aef-3f04-872c-2f22c0745001 | -3.23799 | -45.5898 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d2af1d2-793f-33ba-8b14-4197ef8db2d9 | -3.2374 | -45.59342 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e9c9bd9-855a-3409-ba13-a7db21a276bc | -3.23723 | -45.58937 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20ed4e60-16b2-31e1-ab47-e5cf531116ec | -3.23661 | -45.59298 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 217810e7-238f-380c-a112-f1975609119e | -3.23245 | -45.58889 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5812f7d-2604-3ef2-9b77-5379acdf778d | -3.23185 | -45.59252 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55aa1188-bbbf-3884-956e-a8b38abb07e2 | -3.23168 | -45.58849 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce2064b3-b575-31e5-9833-468cafaa3b75 | -3.23106 | -45.5921 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80497091-62e5-374d-9f84-6bcb73042bbb | -3.2191 | -45.29463 | 2024-11-02 03:47:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| baff07b5-194c-3112-9ee3-0d71ac48babf | -3.21852 | -45.29808 | 2024-11-02 03:47:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 36cf4c26-1f51-36f3-88d5-c3aff44c7ccc | -3.21367 | -45.29369 | 2024-11-02 03:47:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a2cb4daf-9ac6-3f5f-bafd-e684330d5ca1 | -3.21309 | -45.29713 | 2024-11-02 03:47:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 407a9cca-f565-327d-a270-58d67816d673 | -3.21251 | -45.30058 | 2024-11-02 03:47:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9d7825ff-e6bc-3868-9e1a-a3a062cea734 | -4.28272 | -45.64518 | 2024-11-02 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e11f8c3-7afc-3f3b-9350-87b326c3a2d7 | -4.28241 | -45.64347 | 2024-11-02 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0343557e-8859-3c28-a6d7-ace5115b50e4 | -4.28183 | -45.647 | 2024-11-02 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 18d910e5-ff1f-3c9b-86bf-b24ee0da4d28 | -4.27941 | -45.56107 | 2024-11-02 03:47:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4abdb002-869b-33c5-8aa4-d6e5b4068210 | -4.27882 | -45.56461 | 2024-11-02 03:47:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9579028b-9254-301d-b586-aaf53c520ea4 | -4.27725 | -45.64433 | 2024-11-02 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f59636f7-47cf-38f4-aad0-7a619bf52bc4 | -4.20866 | -45.87956 | 2024-11-02 03:47:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5da3bffc-e9e0-323d-8077-bd949848abe4 | -4.20804 | -45.88319 | 2024-11-02 03:47:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 50367a72-283b-30e4-a626-3ed2b8dd7a55 | -4.20743 | -45.8868 | 2024-11-02 03:47:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |


[Clique aqui para ver as próximas entradas](README23.md)
