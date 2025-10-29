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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb949653-45fa-3194-a59e-ca4f834d76df | -18.24532 | -44.1922 | 2025-10-29 04:25:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cc39c53-27b3-35c1-8ac9-2185f2c2fc58 | -11.03213 | -47.80253 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2764a2db-e6b3-34f9-b46a-b8b6dde166d5 | -14.276 | -47.31349 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ff0d9f2-12a9-3204-9416-bc32f0b35580 | -12.69214 | -46.32035 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b233df5b-5707-320b-92d3-00fed418f868 | -14.30566 | -46.53447 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b71ca42-f3a7-34f6-951e-b5d96f7783a4 | -13.64098 | -46.50124 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74f8da84-2ef0-356a-b39d-79f5a1926cd4 | -13.94359 | -48.46973 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e85dd71e-2c65-30dc-a18a-00b8b095627c | -13.27411 | -47.73231 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f65ad3f-a24a-3858-a87a-0677665d4cef | -12.87777 | -48.27628 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0888f45-c935-303e-b2af-ccc4b7f04c83 | -10.85453 | -50.13027 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ba4a0f9-6962-3510-839e-a29266b5ed3b | -13.24109 | -47.05678 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 762390ad-114c-383d-a44b-ac1d0675db91 | -13.6354 | -46.51488 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9275d9ca-2031-3517-acb2-566079885c2c | -11.0293 | -47.79826 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7e331cf-1dd0-3fa5-ad6e-f8cee2246682 | -14.42279 | -47.84931 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7cb006ce-ed5b-32b2-87b6-8aa4bf43b6a8 | -13.23037 | -47.99975 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ab86fc7c-63b8-34e6-adb6-8ec254ebe0e8 | -12.18537 | -46.71708 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04c5e4e9-879d-361a-b460-657d6c8a9370 | -14.98816 | -47.87307 | 2025-10-29 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b6026031-f06a-32a2-ae6c-d46b5027a681 | -14.65397 | -48.39724 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adca8647-7524-37d2-afb2-d56aa5033db8 | -14.38734 | -43.71471 | 2025-10-29 04:25:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc26efff-0663-3fc0-b36a-c05ed8130b92 | -15.64236 | -42.91342 | 2025-10-29 04:25:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f2bcb70c-f26b-3575-b0e9-a951a1eb57ff | -12.85929 | -47.23682 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf12918b-4647-3de7-8858-9e740451a9c9 | -16.59246 | -43.51172 | 2025-10-29 04:25:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a27e8246-14c5-3ed3-bca4-f00bdcdca3ab | -13.46673 | -48.00846 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27a82d39-45a3-38f3-ad54-b2e36b0962c2 | -14.32566 | -46.51586 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21b5579a-cca8-3440-92a8-d118033e31a1 | -13.86387 | -48.50193 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0928d9c-c6fb-318d-bb1f-418f0c7ed212 | -14.96739 | -48.19221 | 2025-10-29 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2dce2bfe-6476-3ce8-ac1f-fd259521d077 | -12.31981 | -46.91554 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ec84a47-f01f-37e6-9ab0-b75bc6ee6605 | -13.04877 | -48.4667 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c9c2673-95b2-3980-acd0-ba40842d4473 | -13.85822 | -48.49336 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ada51bc-3d1e-3435-82af-89e27d7d01a2 | -13.21044 | -47.0554 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 396267d1-7221-3681-8686-db4c0bef57b9 | -12.18146 | -46.72009 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e455224-e1a3-3836-892f-97a5c00bcd82 | -13.52755 | -47.33676 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35dc3b44-1c6c-3490-b6fa-091b55f76e0b | -14.88783 | -46.76556 | 2025-10-29 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64bfeec1-1238-364a-8724-99e106bbb5ee | -13.37392 | -46.63268 | 2025-10-29 04:25:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25ce6b76-6050-381d-b78b-2203f6aba83c | -14.32065 | -46.526 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2729026c-b5fb-384c-bc8a-61e002aa803e | -12.18594 | -46.71353 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89dd0bbd-bd57-31fd-87bb-6dc1e95099a0 | -13.56384 | -47.3464 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9aa53b5b-e461-3cd5-84b0-abd7143bb258 | -13.64374 | -46.50534 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22e47a18-dce1-37ac-b829-b733f041ee21 | -12.01448 | -46.77335 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fb592b6e-ceda-39f9-addb-0115a3efff62 | -13.54016 | -47.13143 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1130accc-09bf-317c-b058-f493cd906b6e | -14.5989 | -48.41545 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b63ab77-01f7-3817-acc8-15b1eb89bc9f | -13.23624 | -48.55719 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4052bc90-20a6-3ef2-a900-5efae97664c7 | -13.78796 | -43.25179 | 2025-10-29 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4c28b18a-d9da-3d45-9fd6-27e8fd0327ff | -13.32919 | -47.47867 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c781ebc6-11a8-3755-896e-dbadff512e38 | -13.57002 | -47.15891 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 717ef7fb-6cc2-3751-a713-17c41dfede14 | -13.66505 | -47.17889 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f420a8eb-aee8-3f8a-9e34-e3350b14d5fa | -12.70655 | -46.31546 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0d423ee5-0506-3148-8e5f-e6acc59d2f9a | -12.0475 | -47.81851 | 2025-10-29 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f00f341a-d3de-320d-8c87-644b82f807e8 | -11.4135 | -51.40363 | 2025-10-29 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb92f5d9-3abe-3f01-bd68-293aa3291196 | -13.57054 | -49.59003 | 2025-10-29 04:25:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f8d0f2d-5afb-3df6-acda-c0f9a4c75372 | -12.35959 | -44.06649 | 2025-10-29 04:25:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4029316-6506-3c11-9d18-da36f86787bf | -12.15218 | -47.69053 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5217f52-ae11-33e4-aebd-799015b6d0f6 | -13.91928 | -48.44547 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bea45d9e-c805-3274-88d8-0b94996c46eb | -14.23984 | -48.11106 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3f4ef1ee-9ac0-338f-9eba-8abd749b1ad2 | -15.10789 | -47.93188 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74a93688-b4c2-36a0-88ff-c92c9bb41901 | -17.59163 | -43.76768 | 2025-10-29 04:25:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71bab393-352e-38a0-98df-1e2d3eae992c | -13.2787 | -47.72551 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b84aefa9-6bac-32a0-92e1-ee0c26aa6189 | -14.48249 | -45.25959 | 2025-10-29 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d1481bb-c240-3ae2-8200-63792ea7a746 | -12.61628 | -48.43959 | 2025-10-29 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 489c4479-2300-3115-b9e2-0724ab0c21a7 | -12.23293 | -46.48452 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d691a501-e078-3c65-bf88-c5896ab125d2 | -13.22483 | -47.07252 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 480d7ffb-197b-34bd-9d0d-582afe79cedb | -12.55809 | -44.96291 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49531920-2d43-35df-b2b8-04760b4551d8 | -12.89973 | -48.58132 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a29ef1f-2d97-3c2f-86a1-e00d733bc342 | -13.01659 | -48.76897 | 2025-10-29 04:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cd7dd44-317f-3665-9d36-1b612a085e11 | -13.3513 | -47.66961 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf1d539c-b690-3d68-b6f3-c6b3b42c7603 | -14.72965 | -48.17157 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62f4bc5c-0bfa-3e0a-8500-b8eacfc0e4f1 | -18.92393 | -45.04851 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 4b79498b-33c4-3f69-9697-fafb3407182b | -12.61353 | -43.30584 | 2025-10-29 04:25:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2acc5935-ea04-334f-8fea-b3ddf5c0b1ef | -11.53536 | -47.0998 | 2025-10-29 04:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b746f2c-1f32-387b-93b5-945cc47b66b9 | -14.25801 | -48.10677 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12434d2b-2a84-30f3-8d62-e6dab10392d2 | -13.68728 | -47.18995 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4806acc-c088-30bd-be74-5cf8eba3d10d | -14.42379 | -47.86436 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efb2f940-683e-39c8-8966-4bc34dedb04f | -13.58133 | -49.59231 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a8268d3-4eb9-3fdf-a8db-67e9c2af8e58 | -12.82919 | -47.26561 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c85b8f6f-0938-3ce0-87b5-e579d8cd83cb | -13.30908 | -47.07154 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f21ac387-2755-3f7e-b912-61e5557e2c08 | -13.05129 | -48.62451 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fcc8b2b-ac22-31d2-90e9-976445cb9693 | -14.51965 | -48.0028 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fb9fbf36-3aeb-31a8-a570-ca1a65e7ca76 | -13.57905 | -49.60559 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 077bfc44-b122-39af-ab02-5ade3af51fb5 | -12.94258 | -46.53604 | 2025-10-29 04:25:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d5c2855-fe7d-380d-b787-503694f83f6a | -13.77743 | -48.39027 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5404419e-b8c0-3831-a37a-fc9ec2b7350a | -10.91193 | -50.26382 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c02e8b7-136b-3f91-91eb-805477405e3d | -12.06044 | -45.71471 | 2025-10-29 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d808d0d1-5cdf-3273-9c6c-fc952a96ead2 | -14.96796 | -48.19247 | 2025-10-29 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f97bfebe-f885-354d-b82b-b27348c6b769 | -13.31425 | -47.70494 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aed5d4e3-d70e-3378-9bd4-fb6b75b383f1 | -12.70323 | -46.31491 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a5ec2b2-bc90-3c86-895f-2f467bfde5ac | -15.63932 | -42.98899 | 2025-10-29 04:25:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 00024c57-64d6-3be4-940f-99d2f1ecff13 | -12.0806 | -47.99507 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72d70c7a-e640-360b-8752-2503c646f87e | -13.34408 | -46.34753 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca041fba-2760-3fb4-a91c-840d05b62ea8 | -13.17027 | -48.45049 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63909b8b-e241-3b50-bc75-c2a9b70d7ca1 | -12.55434 | -44.95844 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2dc8f19-e0d1-3e91-bcc5-be52dd154714 | -13.63602 | -46.48949 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da3c6d38-07bd-3c49-acaa-82fba0adbccf | -16.11915 | -45.75413 | 2025-10-29 04:25:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 15e15641-36a8-3f41-b2ec-d6c62e3c4f41 | -13.70012 | -47.67159 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2b19c4d-c695-3273-9880-a5cdd49590bd | -13.17782 | -48.44788 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce2f0778-796c-3ef5-9065-84dc5244ca09 | -16.59183 | -43.51622 | 2025-10-29 04:25:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ffb4b08-748f-3982-8452-bb6afa7ac77c | -13.86451 | -48.49813 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3840fd54-922b-367f-9a1e-427264fd50af | -14.6124 | -48.39386 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d181352-4999-3a5f-a0f9-af9178f1b627 | -13.10519 | -47.07782 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df296d73-b483-3388-99b5-a024900a57ed | -12.20808 | -47.90304 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1546b18-71c0-3e05-b771-644f4327045e | -14.61951 | -44.9992 | 2025-10-29 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README48.md)
