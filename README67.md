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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86eaf797-96c3-33d3-a678-8b006544e0d4 | -12.4346 | -44.1733 | 2026-09-30 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 173.4 |
| c6e8c0d9-0339-3249-bda5-a2bb957055fd | -14.3348 | -44.9017 | 2026-09-30 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 321.2 |
| edfdb518-929c-3e08-bbde-04c062edcb55 | -11.4307 | -43.4358 | 2026-09-30 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 6459b7f9-1361-3004-ab96-ebc4b6d4a34c | -6.914 | -43.6816 | 2026-09-30 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b61f4dba-8c2b-3aa6-91f1-bce9932c41ad | -7.0281 | -45.3008 | 2026-09-30 13:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a139821a-9aa2-37c3-8f9f-e6b021caf5a5 | -11.6797 | -44.5012 | 2026-09-30 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 39daac1d-1b7a-36d3-915e-e83ddc21f866 | -11.7182 | -43.4386 | 2026-09-30 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 2371cc39-725c-3da6-84da-5ac838a1b207 | -7.0609 | -42.3274 | 2026-09-30 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 090764d6-fbd5-30d9-8573-d930e99d966a | -8.0169 | -42.8444 | 2026-09-30 13:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 77cb4b6f-0726-378f-b966-0a5be90952c2 | -9.9973 | -50.1393 | 2026-09-30 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| f2dbd798-9943-3221-aa00-e121c5530b21 | -9.5002 | -46.3625 | 2026-09-30 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 706847ea-60d7-3378-a8cf-a447eb7008d1 | -11.4311 | -43.4121 | 2026-09-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| c71cf261-091e-34f7-8553-65a2378679e0 | -7.0359 | -42.8744 | 2026-09-30 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 89a0abe1-62ba-3a4c-84e4-596ebcaad026 | -10.7102 | -47.8255 | 2026-09-30 13:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 7a8b795e-46d0-30ab-a2d5-582e9bdab44a | -12.4346 | -44.1733 | 2026-09-30 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 187.8 |
| f1382ef1-7218-339f-9ad8-2cb7c6c01353 | -6.9419 | -42.8598 | 2026-09-30 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 950f65a9-3fa8-3c43-81cd-4212f8e8e2d3 | -12.4539 | -44.1702 | 2026-09-30 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 5a56c007-4dce-39be-b59b-6c8e08998339 | -11.64 | -43.5218 | 2026-09-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.5 |
| 6139c989-1c3c-3648-b541-49a8d12fabfb | -5.8714 | -51.7767 | 2026-09-30 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 88f1948f-c9bb-37ec-aaa1-1743b77740f6 | -11.4119 | -43.415 | 2026-09-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 283.9 |
| 592d28f3-92d1-3a2b-8e71-c949b059b1f9 | -14.3348 | -44.9017 | 2026-09-30 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 232.6 |
| f2385315-2b8d-3af5-89e8-aa84fef4a5c9 | -12.7618 | -47.2431 | 2026-09-30 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8937867b-5624-324c-b3f0-92b9fc44cb13 | -11.8453 | -47.0806 | 2026-09-30 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 10d9a9f8-5804-38c4-9307-096050c8a92d | -17.5345 | -43.6891 | 2026-09-30 13:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 96446b1a-bd66-3734-8518-fc4643dac296 | -8.0169 | -42.8444 | 2026-09-30 13:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 7e0aaf6e-f92d-3f8c-a1c5-2a2b94e1dd48 | -10.5197 | -45.3784 | 2026-09-30 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 63964a23-bd4e-3d5b-b402-3e6e2e1ea831 | -14.1119 | -46.2604 | 2026-09-30 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 218.9 |
| 7019872a-0464-3b8d-846a-194d57b3b4dc | -13.3469 | -46.8169 | 2026-09-30 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 135.5 |
| ce4242b6-0bce-3f21-84ab-8d8b0fea6544 | -6.3213 | -51.1483 | 2026-09-30 13:30:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 93624ba6-921c-36e0-8343-9f9d0c75c307 | -7.0609 | -42.3274 | 2026-09-30 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 702fc26b-4904-3428-811e-e511aba2691d | -17.5137 | -43.7183 | 2026-09-30 13:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 29e6c241-aa01-31f6-bee4-b725c2c8a63d | -5.8712 | -51.7974 | 2026-09-30 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 8a413c37-0740-38d1-9929-39877e0a68e7 | -7.0736 | -42.8708 | 2026-09-30 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 896e5fb3-d960-322d-9b63-0f329692723f | -11.4115 | -43.4388 | 2026-09-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 71a798f1-37bb-3a1f-a788-6663abbd8f99 | -8.3208 | -44.1679 | 2026-09-30 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d9c4a8ad-09b4-38d5-8ee4-011c38bf01eb | -11.6605 | -44.5041 | 2026-09-30 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 90859b4b-806a-3689-8ce5-8e51188c5cc2 | -8.0166 | -42.8681 | 2026-09-30 13:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| b9a74f64-c093-3299-a22e-faaeb141d81c | -7.2567 | -43.3228 | 2026-09-30 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 2628fed6-6e94-3226-bfa8-01834282d2c3 | -7.0164 | -44.6413 | 2026-09-30 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 9bd89932-b2f2-335c-9ccd-175935ce4950 | -11.4307 | -43.4358 | 2026-09-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 8aa4d44d-8cdc-3480-9b58-1e231d63f83d | -11.6395 | -43.5455 | 2026-09-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 3f31504d-b7cf-3d62-8c5e-56b1a7fd39cf | -13.8784 | -44.4442 | 2026-09-30 13:30:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 683a4424-1159-37c9-ad32-d4b2103d8528 | -6.7006 | -52.4933 | 2026-09-30 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| de672599-2e7c-307b-bc56-954b37a7dafe | -11.2095 | -45.1478 | 2026-09-30 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| cfbc91ca-f935-3034-b3ab-d43521b90637 | -7.2755 | -43.321 | 2026-09-30 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| f9539c20-af48-3873-a9ac-2265b3ae4e09 | -11.6797 | -44.5012 | 2026-09-30 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 1483823d-067f-3787-aac5-247d8dc04861 | -10.5201 | -45.3554 | 2026-09-30 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| acbc4ae5-616a-3e72-925e-cde758dc354d | -11.7182 | -43.4386 | 2026-09-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 33196e13-6207-3e1a-9a39-5cdbf5e2dbf3 | -7.0738 | -42.8472 | 2026-09-30 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 784c8389-2916-38bc-9eaf-c054faf7bf6c | -11.3918 | -43.4654 | 2026-09-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 0a923242-1b20-38ab-8793-59bbee3944e5 | -7.0547 | -42.8726 | 2026-09-30 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| c91e0716-5ad4-3600-b65d-c6a8a791194d | -6.3211 | -51.1691 | 2026-09-30 13:30:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 78e96b23-28f6-3bfb-81bd-93f7e28259a9 | -9.9215 | -50.1682 | 2026-09-30 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 88cfdcc3-9b20-3447-8d76-be1f31c09d7d | -12.4351 | -44.1497 | 2026-09-30 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 284.3 |
| a8cfb8b1-808a-3b7d-baca-4e8e81030a0e | -7.0612 | -42.3035 | 2026-09-30 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 1bb98aed-8696-3064-8089-fd004546e84a | -12.4355 | -44.1262 | 2026-09-30 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 236dd1d6-9828-3c84-9646-892c89e3fa0e | -17.5338 | -43.7135 | 2026-09-30 13:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 551026de-9ddc-3f09-ad90-dd028c81b2d0 | -8.3617 | -45.4013 | 2026-09-30 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e87003ce-4453-361d-bd9d-9143f822c6b1 | -13.5139 | -40.708 | 2026-09-30 13:30:00 | GOES-19 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 112.4 |
| 1b11874c-abee-32ec-9178-90705cbd303e | -9.2237 | -45.8527 | 2026-09-30 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.4 |
| fe28051c-82a0-3805-8514-ce024d009d11 | -9.8613 | -44.9577 | 2026-09-30 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 7541b631-a592-3fbe-a8a4-ace0f327476d | -6.9419 | -42.8598 | 2026-09-30 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 8e2b1392-b142-3f7b-bbc5-40aafc72a66d | -11.64 | -43.5218 | 2026-09-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 19680004-a3d8-3b6a-b121-efaf36a69121 | -10.5197 | -45.3784 | 2026-09-30 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| eb116fd9-9162-3925-b471-c5217b98899c | -11.2095 | -45.1478 | 2026-09-30 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 917af8c2-76da-34a5-b7c6-ab6e1a001ad8 | -6.7006 | -52.4933 | 2026-09-30 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 6f40bb14-883c-3a06-b88e-d603a2758f4f | -9.6657 | -46.7024 | 2026-09-30 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 2bee2051-6a9e-33bb-a381-f300bc433b8c | -14.3348 | -44.9017 | 2026-09-30 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 3184b570-b955-31c9-b72e-5c4c443b5b8b | -11.6588 | -43.5425 | 2026-09-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| a5ccd569-31bb-3aaf-a597-2eb20c1de8c7 | -6.7247 | -45.6426 | 2026-09-30 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| bdb98737-b543-3a08-b7e4-2fa76e348f08 | -11.3918 | -43.4654 | 2026-09-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| ca02b32c-105d-39d5-99ca-0b435fbe65f4 | -10.5496 | -49.7823 | 2026-09-30 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| cf4d823c-a121-30bb-b933-28fb71b1b02e | -11.4311 | -43.4121 | 2026-09-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 208.3 |
| f78f4e4d-f02d-36f6-b673-ada59b695d46 | -7.0612 | -42.3035 | 2026-09-30 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 9b42eb55-796c-35a6-bdb1-043341eba358 | -10.207 | -49.9684 | 2026-09-30 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 7e00cc2c-37f9-341f-b654-9957c0e58dca | -14.1314 | -46.2571 | 2026-09-30 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 371.9 |
| 4b7e099d-b663-37b5-890e-19ad394b9528 | -12.3744 | -46.3745 | 2026-09-30 13:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 570c85c5-4bb6-3eb3-873b-ccfb2bc12d7d | -11.5199 | -48.3218 | 2026-09-30 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e29d9c10-40ee-33fc-af7b-1c34e92eb85c | -16.1671 | -42.8587 | 2026-09-30 13:40:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ed74d482-dbf6-3e01-8ef2-71413749f867 | -13.8784 | -44.4442 | 2026-09-30 13:40:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 249.8 |
| 19aa7634-b4ec-3fd2-93b6-b13a22e7647d | -8.982 | -44.1865 | 2026-09-30 13:40:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 84ecc26a-0919-3f79-8c13-356d025d1f92 | -12.4351 | -44.1497 | 2026-09-30 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 0ace57b4-4786-3763-9f9f-e9617484ce1c | -11.6592 | -43.5188 | 2026-09-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 2ee442cb-5e46-3839-851a-6ae2f00b95bd | -11.411 | -43.4625 | 2026-09-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| b862d081-b0a0-3c8f-8edf-2497cb71649c | -6.7005 | -52.5139 | 2026-09-30 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 59500ae6-7721-3b8f-a612-149a09c41906 | -12.4355 | -44.1262 | 2026-09-30 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 2e160c09-b9a3-3a47-8f14-87445f72518c | -7.2755 | -43.321 | 2026-09-30 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 1452f711-81f1-3d75-bbc2-42342d3c6e8f | -11.4307 | -43.4358 | 2026-09-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 3dd4297f-624a-3f0a-9f70-d1406630973a | -11.1903 | -45.1505 | 2026-09-30 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 87a106b3-d54c-3392-8925-ea1c90ef0f58 | -6.7251 | -45.5975 | 2026-09-30 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 86fffbb9-3530-3db3-8684-72f6d73a1f83 | -7.275 | -43.3678 | 2026-09-30 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 84a25632-42e4-3172-b63f-24f5418d2ce6 | -9.8613 | -44.9577 | 2026-09-30 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 42958f33-328f-327d-bd39-6ba62a256faa | -11.6797 | -44.5012 | 2026-09-30 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| fbd083b4-23ab-3131-8847-c22f2c184503 | -11.4119 | -43.415 | 2026-09-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 256.1 |
| 914f12bd-ba71-3f36-a962-b76e49cbe5a7 | 4.152 | -60.5738 | 2026-09-30 13:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2f2f4b32-62a6-3ea8-a9ca-87ce1bbcd9b2 | -10.7689 | -47.708 | 2026-09-30 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| c13846b3-46b1-3bde-910d-3c64e7e3b7c7 | -17.5345 | -43.6891 | 2026-09-30 13:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 62af2900-f86e-3d3a-9915-3b7f52997fb9 | -7.2567 | -43.3228 | 2026-09-30 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 02c50ca9-c3da-34be-82ea-6ab18580d7aa | -6.6874 | -45.6231 | 2026-09-30 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 89e7780f-4bf9-37f2-8da3-272e2600e587 | -12.4539 | -44.1702 | 2026-09-30 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 391.3 |


[Clique aqui para ver as próximas entradas](README68.md)
