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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f34415da-f3dd-304f-b392-6cbeb2cb74ac | -10.62472 | -40.51662 | 2025-10-13 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 012ad4e1-dcf7-302a-837b-66fad51d97c8 | -13.84377 | -45.54449 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17bfc4f8-1a18-3a19-86cc-b84f39287643 | -8.4677 | -46.14534 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd0ca4ab-e2f1-3e96-acf6-e9aed5137904 | -7.84167 | -44.52889 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b42c15a4-1487-370e-911e-6ef948e8b880 | -8.45812 | -46.11758 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2941df42-9385-3d05-8b4b-1bef16513d75 | -15.55158 | -41.81016 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a6f25293-ad21-3bbd-8e54-529f904c071f | -13.32737 | -47.10339 | 2025-10-13 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cc41947-85bf-3876-9d9c-daafda6ab9d5 | -8.23781 | -43.36273 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cea3f968-8e2a-3856-8811-bfd7e912eb98 | -7.55789 | -43.83776 | 2025-10-13 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0813ae59-084f-3f6c-aa0a-5b46277688fe | -8.52422 | -45.40302 | 2025-10-13 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16d76772-8ac2-320d-80ea-e98d157042d4 | -7.77707 | -44.04787 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b12c2f4-317f-3781-af43-31ba87eaae4e | -7.88484 | -44.45394 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b190cb2d-f148-3935-9fe8-c4a76a0ba214 | -8.45541 | -46.13305 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f144c3ed-89d4-33c7-b07d-4674b20bbb20 | -10.81037 | -43.98025 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4715aa63-8587-333d-bf82-0215e56d3fbb | -7.49822 | -44.62912 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8001df43-61f1-31bb-b77a-7d3b0a60897e | -7.80907 | -42.41442 | 2025-10-13 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 819a60d7-1461-3efc-9d4e-fc4a71139526 | -8.3266 | -46.24858 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9651a806-a940-3cf1-87c2-cb898f3df2ad | -8.21533 | -43.32508 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 439fa991-e0b2-337d-b720-2836f3a88c0f | -7.48817 | -44.61068 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8ad83ec5-10c1-3ac6-8c4c-9dcce262b50a | -7.54648 | -46.0897 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5306b6f0-8229-372b-9bce-1f1ba5bdaee0 | -7.36093 | -45.19666 | 2025-10-13 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfdb74fd-2206-3e61-b554-7210505ad4fa | -7.55031 | -46.09556 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 78a99cc4-c694-396d-aedb-d490aeaf0809 | -7.68212 | -42.57187 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 23fd1045-9f23-3141-b791-fc448f103822 | -10.80346 | -43.97372 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e2f2a61-5330-3e03-991a-85b9241d8009 | -7.74745 | -42.41814 | 2025-10-13 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 442c8a3d-2e39-32da-a579-e5bfdd2c3289 | -9.56452 | -45.5369 | 2025-10-13 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c23dcd0-5831-3d43-8cc1-8bccefe1b76f | -12.80069 | -48.38939 | 2025-10-13 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b068e27b-5b61-3448-91ba-f619ed45fd51 | -7.68588 | -42.57247 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f65e5110-d903-39e3-ad41-0f36cafc46f2 | -7.67495 | -43.98493 | 2025-10-13 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5d2abc6-c326-3193-822d-a6b1a05409e4 | -7.84238 | -44.52475 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 752f82c0-54cf-307f-a034-64d69c6884ff | -8.22537 | -43.33705 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a7abb57c-c9c8-3e7f-b21e-5db44b903f0a | -7.77771 | -44.04414 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8b13d8c-d866-3966-be8b-f9eb102575c1 | -7.49878 | -44.6002 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3dd997e1-9cfb-3574-8f0e-e2c62d79d8d3 | -7.50442 | -44.59298 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 332f4810-a9cb-37aa-8695-9b7d318c277d | -7.54558 | -46.09478 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5ce78079-6ca3-392c-95d8-d6feeb11c330 | -12.80121 | -48.38668 | 2025-10-13 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57573cf4-b159-3d3a-be9b-6d9dc816653f | -12.76716 | -50.67918 | 2025-10-13 03:55:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f2ef3f4d-80b1-37b2-b1ef-731acb055f85 | -7.78812 | -44.05727 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c180545-1d6f-33f1-b208-42b2a652619b | -7.49393 | -44.62841 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7511a527-a0bb-3ad6-bdde-d724e93934b1 | -12.77384 | -50.67611 | 2025-10-13 03:55:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9bfbdd68-530e-3605-bdaf-b7ceab936dda | -7.80394 | -42.44582 | 2025-10-13 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 85b0f5d7-124f-35b6-a4a5-b0f74c7e89ed | -11.43075 | -42.31142 | 2025-10-13 03:55:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 70edf784-ce50-3933-a1f2-986cd70dfb00 | -7.50251 | -44.62983 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ded4f041-3e93-3d03-b667-729954fbb38c | -12.74647 | -50.66171 | 2025-10-13 03:55:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 31bfd8d4-72e1-3262-9641-1dd945a01c3b | -13.32759 | -47.10136 | 2025-10-13 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23d17f6f-ce92-3909-9fd7-0fc6d3fede29 | -13.75275 | -45.65651 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87303a85-81cb-3e44-87b7-0af5b4bc59b4 | -13.82348 | -45.49747 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0808f600-13ec-322a-a358-615053cf4c6e | -15.53638 | -41.81892 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3d9fccd3-f4ca-3d8f-b1f5-9b8d24dc11ee | -7.67552 | -43.98525 | 2025-10-13 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cab6afff-1c41-3c3b-9541-9b1399d2e8e5 | -7.6791 | -42.56679 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8e41c496-ac3f-3c5c-9be2-e8af3c6048a1 | -13.56175 | -43.41986 | 2025-10-13 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1262a3d1-8512-3fa7-9239-853153c6dd04 | -8.32749 | -46.24347 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8ebf4fa-8ee8-3c85-a311-98ba79549faf | -8.45632 | -46.12784 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c8629e43-8525-3ef4-a0bb-16e696f2e142 | -8.71985 | -41.0854 | 2025-10-13 03:55:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06c1d4d4-2f67-31db-9e2e-bd38da06fc87 | -7.6889 | -42.57759 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 58755724-ff8d-3aee-877d-81d727a1b485 | -13.32289 | -47.10199 | 2025-10-13 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7484fa68-1515-37b7-9a45-bfecc771dd3e | -7.80764 | -42.44653 | 2025-10-13 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3123e844-24a6-3371-afd3-76586191e66d | -7.62057 | -43.04516 | 2025-10-13 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 666247be-443b-37ae-b286-bcd7a29a7b4c | -12.77298 | -50.68036 | 2025-10-13 03:55:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fa2e7e15-0ce9-3dad-9803-0e2cd906c67b | -11.84691 | -38.20228 | 2025-10-13 03:55:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b6978dca-af45-346d-8e2b-4d3aa85b125f | -8.54679 | -45.4249 | 2025-10-13 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0aa16b3c-c7b2-39b4-9b6d-00b71fb95d6c | -8.46862 | -46.14005 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93138103-4cdd-3575-b48d-b8320aa15260 | -7.5087 | -44.59365 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15a68cea-2bc4-36d7-bab5-4611e3c8218d | -8.45345 | -46.11679 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2a652e1c-5aa2-3e71-abb4-33207af70da9 | -7.92345 | -47.21649 | 2025-10-13 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ed769b0-99eb-3e1b-b304-e94ab7645acc | -7.48886 | -44.60666 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1fad987-17da-3538-9dae-8cc618cd1f8b | -9.33055 | -40.87558 | 2025-10-13 03:55:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 00a418a6-7f4c-3aee-9dc0-00fb7b06b5a7 | -13.75345 | -45.65265 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 683bd43a-9725-3f08-b647-b0203a0a2660 | -7.75464 | -44.20201 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c0bcc3a-ab03-33e0-a832-f9832de8134c | -8.45434 | -46.11174 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 699afc1f-315a-3516-9a71-18477d744378 | -7.55381 | -43.83718 | 2025-10-13 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2177048-28fa-3149-bd97-e471e3e24714 | -8.21262 | -43.32267 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f91d39ab-82b4-38c6-a4fe-610b85bf8790 | -10.80562 | -43.98463 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b258b11-244e-3b4c-9d11-b68cc0276889 | -12.74734 | -50.65746 | 2025-10-13 03:55:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f2090a1d-b225-378e-b054-dc9b76080131 | -8.52413 | -45.39778 | 2025-10-13 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7973339d-e6fb-3551-8b93-c7737d38cb4c | -8.45076 | -46.13209 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62e5938a-7263-3511-a4d3-696c15511e55 | -13.85811 | -45.44249 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 662b163d-5315-332b-8257-f97528994bfa | -15.19082 | -43.57176 | 2025-10-13 03:55:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ffbabf31-5139-3e3a-86cf-1cd934b6769f | -11.23899 | -39.40831 | 2025-10-13 03:55:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8ea51401-7f94-3dc8-9002-3577bbb8c029 | -8.44503 | -46.11001 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa257a79-51a0-3849-8750-352c57047bd4 | -7.62276 | -43.04288 | 2025-10-13 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b85eca77-4a96-33f8-808c-99dd7e4fc771 | -7.53983 | -46.09188 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79dd059f-c1b0-3b6d-9ec5-575c725852c0 | -8.32838 | -46.2384 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f0652fe-f459-3ef5-b080-3e6dcdaaef3d | -7.50109 | -44.63811 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6b1c032d-b9b2-3c64-9cb9-bade98e6ac3e | -7.78465 | -44.05289 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69a2bef3-9eca-3218-b5ce-95682e98f553 | -8.52984 | -45.41718 | 2025-10-13 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db4b2a03-f69f-3e4f-b412-afcaa4c87305 | -8.46482 | -46.13426 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 91b6a67d-8a16-3926-a27b-56fd4b2c39d1 | -8.40462 | -45.07162 | 2025-10-13 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87412b8e-0c38-30c3-bc0c-a47d583c3c56 | -15.55932 | -40.84632 | 2025-10-13 03:55:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d46ffe45-7149-37e6-acee-b38bd69e0469 | -7.73779 | -42.43026 | 2025-10-13 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 75ff726f-6961-3e88-95e6-2db430ce0b9d | -7.77472 | -44.04285 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5aee3c5-3868-33a2-ac02-54c3aa1e7b13 | -8.52495 | -45.39867 | 2025-10-13 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 768b924e-f75d-31d9-b45e-daa8c18cc140 | -19.78193 | -42.37397 | 2025-10-13 03:57:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1cb8fa74-c866-336c-a7d0-5bc2c6b720e9 | -19.51204 | -43.03903 | 2025-10-13 03:57:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 05656c53-d445-3353-80e6-6f4301b897df | -14.21931 | -51.52151 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e10f622c-4bc3-3a56-a091-cf644062040a | -16.30361 | -43.07684 | 2025-10-13 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12518af7-0055-3069-9847-be21d56cb621 | -17.3393 | -53.8098 | 2025-10-13 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 32799dfe-e6b8-385c-b1bf-efca66ed149c | -20.84841 | -42.80945 | 2025-10-13 03:57:00 | NOAA-21 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1fe407a1-3a5f-3c0b-9207-09b63ffb6e6a | -19.8525 | -42.46277 | 2025-10-13 03:57:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 35f7b61f-68f1-36cb-924b-e250e56db5da | -20.84249 | -42.80877 | 2025-10-13 03:57:00 | NOAA-21 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |


[Clique aqui para ver as próximas entradas](README14.md)
