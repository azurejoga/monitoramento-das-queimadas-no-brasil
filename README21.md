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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d65e7206-0240-323f-939c-c15b1d21a0da | -7.09048 | -41.22678 | 2025-11-08 04:36:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5e321afb-7d33-3137-bede-9037a1f748a2 | -5.72722 | -46.46463 | 2025-11-08 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 046a53d9-50b4-3b86-a723-1e9900d1f113 | -5.98099 | -44.17793 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bdded201-ff5c-3b30-9eaa-203a5fecd21a | -4.46925 | -45.50561 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f32639a4-0a71-332d-99a3-41f6c757946e | -2.55104 | -48.39442 | 2025-11-08 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43c600ab-4e1f-34af-8a88-78f77cb523ed | -5.29299 | -44.78487 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a6a82f6-272b-35c6-80c8-d332602dd529 | -3.33356 | -52.56421 | 2025-11-08 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9e76618-fd6b-3cdb-908c-6bf062c85342 | -5.65699 | -46.39921 | 2025-11-08 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3d5b92e-5d3e-33af-8784-cfa93f23017d | -9.09675 | -44.32335 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 348d267d-432f-32f6-b02f-a88e03532439 | -2.72951 | -47.39841 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ca4d847-1247-3ea4-8a5f-8c7cecaf0547 | -3.91835 | -47.17562 | 2025-11-08 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4dadd7c-4c59-3b24-8971-55ad99ff1076 | -4.59633 | -45.63188 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb49e8af-8b22-3229-8fe6-67a7326f606f | -2.41601 | -48.86989 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 421c54ec-a791-3b43-8161-a3d11d7eb44d | -5.47456 | -44.60079 | 2025-11-08 04:36:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a481c9d-864c-31fd-bf46-b72e063cfcd5 | -3.00666 | -49.60933 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61c98f57-8dcd-3787-8ec2-409ee6048a33 | -3.91466 | -50.04469 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a31d15b4-af55-3d61-a1d2-b66228ebc2d4 | -3.34898 | -50.1754 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f843b56-c820-3184-a729-fafedaefb1bd | -4.39046 | -45.35979 | 2025-11-08 04:36:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64b7df2e-5508-3992-bf98-6085b5883cc8 | -8.07084 | -47.12194 | 2025-11-08 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74f31279-a3e0-3d82-aa04-f39e30570600 | -4.32505 | -45.98558 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28c54831-ad65-3e90-912c-88f2dd17800d | -3.52025 | -49.26162 | 2025-11-08 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 408f09b9-4e65-35ce-a7bd-2c51bdfda208 | -5.66037 | -46.39975 | 2025-11-08 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc3285ab-5457-3372-8b97-44b379f2ac50 | -3.35502 | -53.2234 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7877c3c-4334-35d0-ba12-baf38d3d465c | -3.57139 | -49.98046 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62beade0-1c15-3c94-b825-6274d2c3c3fb | -3.11956 | -50.14075 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99938a31-3a09-3501-bfb6-93ca09f9aedd | -5.26022 | -47.16299 | 2025-11-08 04:36:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fbd34be-3302-3857-89cd-d62b46a393e3 | -3.65395 | -50.2742 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bfe0e8b-7037-3011-ab9e-106ef5141ff6 | -3.5168 | -49.26107 | 2025-11-08 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01c9b38e-56ee-3fff-9c6a-eecf8e271ef9 | -4.38585 | -45.36678 | 2025-11-08 04:36:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b7c7999-0ae6-3ed4-a03e-1f4d775a7dff | -4.44611 | -46.44187 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1db6933-744c-3f6d-8c77-1571534e2aa3 | -7.79532 | -46.65494 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4aebd65f-aa6b-37a5-b480-b6ba21e34027 | -3.29679 | -45.33022 | 2025-11-08 04:36:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f352c88-58e4-38db-9cbd-64f92fed19bb | -3.35158 | -50.20514 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 51f11205-089e-38ce-a66e-46f4b75bf352 | -3.30656 | -50.05176 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dda28976-3dfb-38d6-8623-3d7f5254fd00 | -3.44372 | -46.19251 | 2025-11-08 04:36:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62e1a855-2d1f-3346-883b-4905408f354e | -4.60443 | -49.36117 | 2025-11-08 04:36:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 650ab508-b1ea-3234-a32f-877d9d5fe671 | -5.2558 | -47.16941 | 2025-11-08 04:36:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ecf6287-5b44-3e97-befd-2af3a3670564 | -7.77985 | -50.80119 | 2025-11-08 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da3817bf-0a18-3517-accc-10b0985cdbfb | -3.32772 | -53.36029 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9817da6-bccc-3579-89b3-e94e977030e1 | -3.85193 | -47.40215 | 2025-11-08 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6718ebc2-2249-39dd-9dfc-4690ade71ed7 | -4.10612 | -47.27206 | 2025-11-08 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05f6fb67-e24b-3a45-afb1-77abe86e23ad | -3.32407 | -53.35527 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81933a86-e5a0-38df-b6b9-f42cef1c89f6 | -3.35433 | -53.22751 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81e484b6-e34a-3948-856a-61de21f5e154 | -5.90228 | -37.82542 | 2025-11-08 04:36:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f7200a9-9e29-3e97-a0df-880748e5325a | -7.4252 | -46.65474 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe3283de-66ac-33dd-a92e-2ed766f92b5e | -5.01861 | -48.36536 | 2025-11-08 04:36:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fb40f2a-a3d3-366a-9e45-66d6fb964b5f | -3.01232 | -49.43979 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89b81a91-42ac-3ae5-b547-1acbd11dec60 | -3.32336 | -53.35951 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 249c96e4-4baa-3781-b787-f5307c9bcd13 | -3.39963 | -49.99648 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59d53c0c-12ed-3533-81aa-efe75f08d51a | -7.58421 | -42.3092 | 2025-11-08 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9fb48b6f-46c3-344e-94d7-c9eb92a19104 | -5.60856 | -37.35734 | 2025-11-08 04:36:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c97687bc-3d11-33db-9663-cbf31ede24dd | -6.20611 | -42.05342 | 2025-11-08 04:36:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9b16927d-4451-37ab-9e0a-3cb4f8e5a365 | -7.463 | -46.63456 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ff62359-196e-3788-95fb-20bc57f87886 | -5.23115 | -42.80085 | 2025-11-08 04:36:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f38d9178-cac3-3c6a-b17d-cdb6eb5c8eae | -3.54224 | -50.38946 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4c4f813-94cf-3846-9709-17a3156b355f | -4.59552 | -45.99422 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| e9b46e96-39d8-3cd5-936f-b971b679e3cf | -3.27364 | -45.45462 | 2025-11-08 04:36:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ae56e1d-80a4-3b17-a46a-5da310f2f3b6 | -4.466 | -45.32907 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 056cf9d4-9dc7-356d-a804-5281d0a1bebf | -4.30347 | -42.3288 | 2025-11-08 04:36:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8dcb5593-a362-3936-aa7c-b7beaf930bd9 | -4.82243 | -48.06645 | 2025-11-08 04:36:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 779315e8-a615-3c59-8212-78c17152e71a | -4.59099 | -46.00097 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a792ea26-c96d-322b-ba60-4015322d3a4c | -3.43709 | -45.59119 | 2025-11-08 04:36:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 793b96ed-0ba5-38a4-8092-a3ad91fe8821 | -2.45209 | -49.01616 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4e6375b-67f2-3f82-a32f-1a677817de6f | -7.78863 | -48.5269 | 2025-11-08 04:36:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cd33e4a-f6d0-36e3-88ce-e17dd49382a1 | -2.61719 | -49.22685 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16b99e07-3a1e-3426-8ffb-95cf9df0aca5 | -3.61552 | -52.12439 | 2025-11-08 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 617d3ee7-60d7-370a-b193-845a8eb8eacf | -3.77193 | -50.49187 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3c0063b-8501-34dc-a4b1-859a7df726b2 | -3.65462 | -50.27009 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 219d8013-fcec-33d3-938b-69281722da2a | -2.48796 | -49.11333 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adc8185f-a15d-33b9-889b-555188086406 | -3.50172 | -50.05674 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31b97300-da76-34df-b44b-3f7caaa2ba18 | -7.0414 | -46.38383 | 2025-11-08 04:36:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3e8a8e8-e2cf-3085-8599-a039cd1e0b90 | -3.3507 | -53.22265 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f232619-88a4-3005-ae52-9d37df47d23e | -2.7993 | -48.9401 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 147cb26f-8a28-31ab-8561-57c21ac28531 | -4.34927 | -45.76286 | 2025-11-08 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a6cc163-baf3-3513-875e-1e166119e056 | -4.4539 | -46.43592 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42c29b91-eece-309a-8cd0-759b8c60267b | -4.80957 | -45.39942 | 2025-11-08 04:36:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23b929e3-be38-3efb-9914-f14c0831e049 | -3.65528 | -50.26598 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bbf007d3-87ad-3512-8bf6-c7c017e1552b | -5.07618 | -43.83618 | 2025-11-08 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22098db1-34f3-3f2b-b806-384be437e656 | -5.92812 | -44.11346 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b0bde6c-9709-3fe6-b885-d192866b07cf | -4.30332 | -42.32933 | 2025-11-08 04:36:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 80ede7dd-1fbb-3c01-b90b-a509aafaa899 | -3.44641 | -50.21861 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0dafea6-e83e-3845-add3-338a2df546ab | -3.03631 | -50.30711 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8499b361-cade-39a7-a892-71fd7d69594f | -2.53129 | -49.44519 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3932d48-2f38-3bb4-b114-464f2a806d95 | -3.88791 | -42.39277 | 2025-11-08 04:36:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a648aa86-5f83-35d2-9d3c-c68b103ac36b | -3.33784 | -50.19878 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1dc6013-95c0-3eda-887c-7ce70a162db7 | -6.85683 | -46.2695 | 2025-11-08 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7613daee-e84e-3622-a8dd-bff412434406 | -3.3349 | -50.19416 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 478cdceb-655d-31d7-a1c6-ca4f489f28f7 | -3.606 | -43.51738 | 2025-11-08 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0eeb1c91-4f07-3cff-aba9-92b6999924f2 | -3.67734 | -50.4524 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dffaf8a-7f4f-3e0e-85eb-fe30381240bc | -4.68966 | -46.39988 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01ea0aa0-8417-35ba-ba87-f5910afc6547 | -2.66918 | -49.44222 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0f8a2db-d9a6-34b8-bcfb-feaf883456c5 | -3.28473 | -52.09166 | 2025-11-08 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75b12a7e-6d5e-32d3-9614-d270641ea8e4 | -3.12836 | -50.15482 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bba39e15-d7a1-348c-8676-50f241b4269e | -7.58851 | -42.30965 | 2025-11-08 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8583f482-6e88-3e5e-8901-060e33f33087 | -5.49748 | -47.07566 | 2025-11-08 04:36:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e991719d-13d0-3711-88e8-83f133cb5ba7 | -3.14923 | -50.30231 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 819c4895-65b6-33a0-ba34-396ea520e40c | -3.01929 | -49.44089 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 618e9caa-1b11-3925-8581-f9d06fda4a4b | -4.9855 | -43.56922 | 2025-11-08 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb78b407-72c5-37e3-afa4-2316d928df6f | -8.49217 | -44.72326 | 2025-11-08 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd4b4ae4-9630-35e3-9fad-0af19ee9f657 | -3.95453 | -45.45104 | 2025-11-08 04:36:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README22.md)
