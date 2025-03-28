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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec239827-320e-3aba-bb0d-7f6d3b5f43fc | -12.4697 | -41.4541 | 2025-03-28 00:00:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 128.1 |
| 48b88dfd-ddfd-3ed5-a616-f5a9ceef1bd1 | 2.3065 | -60.5872 | 2025-03-28 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f3c02179-e8a8-3358-8d9c-fc04215eca9f | -12.4702 | -41.4294 | 2025-03-28 00:00:00 | GOES-16 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 98.4 |
| b16b299e-d1c1-3477-8411-94fb4657eb6d | 2.3065 | -60.5872 | 2025-03-28 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 13ff2793-e704-3805-b971-b7cdb6227f11 | -12.4702 | -41.4294 | 2025-03-28 00:10:00 | GOES-16 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 3830b306-7de6-3cd1-b966-e2b377ba7b17 | -12.4697 | -41.4541 | 2025-03-28 00:10:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 1d913514-747f-35d2-b411-f4c2b82070fe | 2.3065 | -60.5872 | 2025-03-28 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0c20a4d9-ee57-3f35-b8b6-628eb49b7d67 | -12.4697 | -41.4541 | 2025-03-28 00:30:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 3bf47cfd-d453-3567-8ced-81e0e015cdb8 | -22.75266 | -51.76909 | 2025-03-28 00:58:00 | TERRA_M-M | SANTO INÁCIO | PARANÁ | Brasil | 4124509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0ff96124-9f3f-3808-af23-bdb2e92412b3 | -21.3634 | -48.59137 | 2025-03-28 00:58:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.4 |
| 6d91b564-b641-3677-b2af-6f151533f6e5 | -21.36196 | -48.58156 | 2025-03-28 00:58:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 919f6caa-9b20-342a-ac05-697e046c0f5b | -20.13454 | -50.71733 | 2025-03-28 01:00:00 | TERRA_M-M | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| fb0dccc8-8cda-37f6-9e48-cdf0493b75db | -20.60913 | -55.71008 | 2025-03-28 01:00:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 53a2b53e-82e3-3cac-8614-f49aba598d6e | -20.13583 | -50.72681 | 2025-03-28 01:00:00 | TERRA_M-M | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| cf2629a2-3120-385e-ac32-4176c3c6419c | -20.66192 | -48.45607 | 2025-03-28 01:00:00 | TERRA_M-M | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 50d08410-3751-3428-817b-d413066c0e9c | -19.28773 | -50.11209 | 2025-03-28 01:00:00 | TERRA_M-M | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c0a6c586-d1f8-3f94-9762-b129feffb360 | -12.44795 | -41.43908 | 2025-03-28 01:02:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 77c0cc5e-e82d-3963-8756-c30f5547dc25 | -12.46469 | -41.4342 | 2025-03-28 01:02:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 2209f9b5-0f67-3955-9cab-7c14c58591ff | -12.47452 | -41.46951 | 2025-03-28 01:02:00 | TERRA_M-M | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 22b19317-f6d8-3817-b5a8-91f7339a72f1 | -12.47226 | -41.47633 | 2025-03-28 01:02:00 | TERRA_M-M | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 818392d4-088b-3d13-aa3e-176c930b330f | -12.45011 | -41.43316 | 2025-03-28 01:02:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 33.9 |
| 6049b81c-f4fc-3e6f-b4d6-71ed45484bfc | 0.6589 | -59.53535 | 2025-03-28 01:07:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9e0ffbfa-8266-33b7-b8a4-50846782bd8e | 2.31522 | -60.58284 | 2025-03-28 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 3a02b804-b8d5-3bfb-969b-54899179e411 | 2.23445 | -60.71402 | 2025-03-28 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a9d5fca5-8e58-31b4-973e-84842906d7e9 | 4.07622 | -61.56371 | 2025-03-28 01:07:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b45ce1a8-e574-33a2-b97e-361375d5f412 | 2.41956 | -60.78955 | 2025-03-28 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 71e1d3cf-4173-369e-8607-a46b00964b40 | 1.82895 | -60.89081 | 2025-03-28 01:07:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 48adc09c-f8ec-3031-ad3a-235903d332f7 | 2.62305 | -61.02218 | 2025-03-28 01:07:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a40ee6b3-0556-3b76-8d52-80358f2aa0d9 | 2.72772 | -60.39761 | 2025-03-28 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 7eb1e519-16da-3378-ab55-6dbfa8dc97ae | 2.30313 | -60.58108 | 2025-03-28 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 95e06dcd-b8ca-348d-acbf-bd8637f64434 | 2.62123 | -61.01629 | 2025-03-28 01:07:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7c8a3f23-5ced-3317-9b8a-f400711c0ea9 | 2.17969 | -61.17897 | 2025-03-28 01:07:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0e9458ed-ccbc-3341-9a98-058ec9be44a7 | 2.73953 | -60.39931 | 2025-03-28 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| bd5826f0-762d-3319-bf06-cdaa4fc072b4 | 1.83167 | -60.87223 | 2025-03-28 01:07:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 725e1be7-8346-3322-84b4-73b114bf3bf0 | 4.08914 | -61.57203 | 2025-03-28 01:07:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| b3961643-552b-35ea-8834-1dfbc5117dee | 4.08889 | -61.56565 | 2025-03-28 01:07:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9a7dacdb-8a53-3f9a-9f81-c6c7d4bde10a | 2.30767 | -60.58738 | 2025-03-28 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 633846d0-1a89-329c-a7bc-60b5a2bff7aa | -12.4697 | -41.4541 | 2025-03-28 02:50:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 179.5 |
| ed7f4cb2-3d13-369a-86f7-0679c18747e8 | -12.4503 | -41.4576 | 2025-03-28 02:50:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 92.6 |
| ced4d187-7916-329f-98d4-b1903e5d437e | -12.4702 | -41.4294 | 2025-03-28 02:50:00 | GOES-16 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 61612641-12cf-33e2-b8c6-a3d26a4cbf7c | -12.4697 | -41.4541 | 2025-03-28 03:00:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 58.9 |
| 57d2f016-6f30-3df4-a305-946ed3725ec7 | -9.05692 | -35.7255 | 2025-03-28 03:10:00 | NPP-375D | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 59eafd18-c22e-356f-befd-3b46d57afc67 | -12.45564 | -41.43593 | 2025-03-28 03:13:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6e2ed7f3-9a23-3785-9c01-bfc0caa7fae1 | -12.44901 | -41.43454 | 2025-03-28 03:13:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12102e1c-0436-3f7e-b963-ae3d9ddaae45 | -12.46388 | -41.46296 | 2025-03-28 03:13:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 6631b9dc-d0e1-3932-8672-5b75a9048aed | -12.47297 | -41.45251 | 2025-03-28 03:13:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5f6c90a8-17a1-32fa-891b-577b2ce19987 | -12.44793 | -41.43968 | 2025-03-28 03:13:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e4d3f30-d487-311b-87cd-b5f8ee8ba270 | -12.46537 | -41.45576 | 2025-03-28 03:13:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5c11655a-c31a-39c1-a5f9-90e13973ec42 | -9.97632 | -37.91486 | 2025-03-28 03:13:00 | NPP-375D | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c363a7d5-e6a7-3607-87e0-a5fc41400913 | -12.45666 | -41.43106 | 2025-03-28 03:13:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1cc6a07c-f808-3aa1-aa87-53ab54e595bf | -12.46195 | -41.45532 | 2025-03-28 03:13:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a54c2fb1-5e49-3b32-a456-dc2ad0ce1c5a | -12.45757 | -41.45994 | 2025-03-28 03:13:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0aedf04b-e1fd-3f53-ad7f-2d205a8ee695 | -12.45459 | -41.44097 | 2025-03-28 03:13:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 03bedad6-404b-3c7a-a650-9e591850d624 | -9.97715 | -37.91054 | 2025-03-28 03:13:00 | NPP-375D | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b7c05a9-6702-3d8f-a37f-60d04b51d814 | -12.46033 | -41.46284 | 2025-03-28 03:13:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3abbe0e8-ffbe-348a-8d76-2cb7a8d16679 | -19.60351 | -40.62616 | 2025-03-28 03:15:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0f4e0488-7e17-3789-8e0f-566b2cca1ef5 | -12.4697 | -41.4541 | 2025-03-28 03:20:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 98c21f63-423e-3a2d-96c3-a087e1db21db | -12.4503 | -41.4576 | 2025-03-28 03:20:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 5874bda6-e399-3c92-a847-fbdbad9a8ef5 | -12.4697 | -41.4541 | 2025-03-28 03:30:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 105.6 |
| b74cd3c5-812d-329b-a045-042de9174b74 | -12.4503 | -41.4576 | 2025-03-28 03:30:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 93.4 |
| a649a928-c28a-3835-96fe-4fb7102820d2 | -9.71063 | -37.84296 | 2025-03-28 03:34:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 114a9ee1-6249-3c0b-9cce-b76c9d2db886 | -12.45679 | -41.45967 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 510b3d20-89a6-3551-8d16-4e1f3b005faf | -12.21176 | -38.98191 | 2025-03-28 03:34:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c44bb84c-9ebc-3a49-bccf-93a8fdff4931 | -9.18001 | -40.34835 | 2025-03-28 03:34:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e77287f8-d57a-3b85-a89e-01ce662bb25b | -9.71699 | -37.83698 | 2025-03-28 03:34:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c15900f8-8964-3487-bab2-339d5f076cdb | -12.45496 | -41.46258 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 007c7e49-5428-3f46-a192-2788f412d18a | -12.45596 | -41.46437 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 24e2400a-2bb3-3750-8da8-0f914f283d42 | -9.71138 | -37.83854 | 2025-03-28 03:34:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1862a048-d5a8-36ec-80d0-469c365c17a7 | -5.78705 | -43.62358 | 2025-03-28 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 749618b8-d8f4-30ef-bdcd-4c2e962cfb1a | -10.99469 | -40.48162 | 2025-03-28 03:34:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7928c38c-60eb-3854-94ff-a32b738a32ea | -12.45243 | -41.4584 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1dc0e622-b5c0-36c4-a293-9c21c0c998d1 | -12.45774 | -41.47234 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d02295b8-2531-39b5-8de1-03d01a379f25 | -12.45854 | -41.46804 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 91fadbb4-2859-37c6-855f-601b1b457c0f | -9.17566 | -40.34759 | 2025-03-28 03:34:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5a1e3724-236a-36a7-8485-e4141ecc119b | -12.46549 | -41.45531 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9eb21203-98f5-39c4-8065-189ce9444a55 | -12.45059 | -41.46141 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ce27d0bc-473e-3081-84b7-adcef5a5824e | -11.97221 | -40.29115 | 2025-03-28 03:34:00 | NOAA-20 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cd69b46b-b18a-3cab-a307-8abced86c774 | -12.46216 | -41.47329 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53927bbd-ebeb-3dd0-91cb-aef75c51be9c | -12.46815 | -41.4657 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 54e3b988-1367-311a-90ab-c16d0b249ecc | -11.90282 | -40.94294 | 2025-03-28 03:34:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea6b384b-5fc4-37f5-8c1f-5195939a5bde | -10.35142 | -38.48048 | 2025-03-28 03:34:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2c588d55-17ae-34a2-9cb8-b5438ae1315b | -9.17958 | -40.34609 | 2025-03-28 03:34:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8ff915f8-6faa-36c5-9522-ab6956624a3a | -12.46023 | -41.45894 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 91deb615-3a15-3516-882b-8f1f8c5373a5 | -12.45071 | -41.46808 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8f1b03c-7506-373a-8b39-68ffe0982a5a | -5.22628 | -43.52071 | 2025-03-28 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36c0627a-bd0c-3d74-8af1-12ab8b8141c7 | -12.45415 | -41.46698 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0fc7ddc0-d678-319e-9d22-9321dd666f42 | -12.46372 | -41.46483 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 1a58c19b-a512-33af-8a57-2a5474eb6cde | -12.86052 | -38.36593 | 2025-03-28 03:34:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 78a172a5-f661-3e7a-b6d1-4ad67ae29631 | -9.97746 | -37.91125 | 2025-03-28 03:34:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| eb74f84e-d759-3eac-a43d-f2833db95fb3 | -5.788 | -43.62367 | 2025-03-28 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d8fd661-0804-3f96-ae3b-c6381f70051d | -9.70887 | -37.84011 | 2025-03-28 03:34:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ff0285c-088f-3e00-93d6-91db43347d67 | -10.69409 | -37.05021 | 2025-03-28 03:34:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7eaf8a08-8df6-3427-9f72-9da9d2706260 | -12.45933 | -41.46378 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 0a6dfc5c-8f8e-3adf-be01-2e9d85fef1bf | -12.14404 | -38.7875 | 2025-03-28 03:34:00 | NOAA-20 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba2b3f3f-b37a-3e00-85e8-9aa7498afc3c | -8.11802 | -43.12856 | 2025-03-28 03:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1d219508-2b5f-302e-af19-19dc00fa9885 | -12.46114 | -41.45402 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 93b8d374-224e-36ce-884e-a9bad1bcb84c | -8.11207 | -43.13092 | 2025-03-28 03:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2f7877d6-448b-3a1d-a5dd-be72b0292b0c | -12.46294 | -41.46907 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b01c4f57-3e36-34e4-a5d3-1eb7cec303c2 | -12.45588 | -41.45767 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 4834d031-0ee7-374d-a81d-734a7a8c14da | -8.39107 | -35.02625 | 2025-03-28 03:34:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README2.md)
