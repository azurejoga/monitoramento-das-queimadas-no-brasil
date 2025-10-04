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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6248248a-6bf3-339d-b364-ab6378fcb59a | -13.10161 | -47.88207 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fa599e5-6fd2-3474-9e7e-129d701804f3 | -14.89677 | -48.35646 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05b7d148-e88c-320f-b7ad-4e22fc3cb037 | -9.35806 | -45.78267 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bbf4bfb-4ad5-323c-97f1-3b323f296894 | -15.3119 | -46.30624 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7189c250-1f98-347b-ac0a-97290aa160b7 | -12.87292 | -47.28665 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3debbcfd-cb57-399f-959c-875da3e1651f | -12.09038 | -45.17524 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 04a7ea94-2d46-3e93-869b-3f72426a3dd5 | -12.04191 | -45.20012 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6090ca6a-4b5e-3566-93d5-5aa064cd6e2e | -12.92555 | -46.36609 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 739928b9-791f-31b0-9b18-9e777897aa7c | -11.44225 | -43.49478 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cf79f87-830e-3967-9c76-97009b2ae16e | -11.12092 | -55.45734 | 2025-10-04 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 323f7ea2-01f7-325b-8cce-d98fca7077b1 | -11.55119 | -47.64392 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e36aeab7-98ee-3506-81f9-70f536c2ef45 | -13.10737 | -47.91392 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07e6c52e-3199-382e-aca6-54400cac4b36 | -11.45301 | -44.95345 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12d6a9b9-482e-314f-ab51-c47ec4106139 | -12.23121 | -43.76901 | 2025-10-04 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 333db804-8fab-311d-a7f3-cc80d19c8887 | -11.45853 | -45.14776 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fcdc054-da2a-356b-8b22-6a40d9eded8f | -11.89586 | -42.82112 | 2025-10-04 04:14:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 426e41f0-6779-3b04-83e1-65e082b5dbc3 | -13.84912 | -47.92313 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bda92f84-fa44-3322-9ca9-09ba2b16cd2a | -8.62257 | -54.988 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ead2110e-7d75-3785-98b4-ca39a57c453d | -12.9556 | -50.98938 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef9cfc0c-b2ec-305f-a715-4804e88ec56e | -13.31349 | -48.13541 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e7ab167-e49d-3f4a-84eb-61d214e61913 | -13.8871 | -46.51522 | 2025-10-04 04:14:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 36c701fd-64fd-3f99-9048-0d577eb6bc9b | -13.11826 | -47.85032 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 79327f7a-4cfe-363e-a942-5e5ec8629557 | -9.90342 | -43.7375 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b6ce3d39-d458-327d-a833-836f36e016e0 | -14.65951 | -48.31734 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| aff92aa8-6edb-3e96-9150-b1b7e64cebc0 | -14.88637 | -48.28676 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d3070fb-986c-30a5-8728-35aaab4cb678 | -11.90555 | -46.37621 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4aebd29-c7ba-3836-8a85-a69cffb75238 | -12.81103 | -46.86039 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 788bd2c2-30b8-3130-973e-15253a39cd70 | -13.32822 | -47.58003 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64befab5-335e-3b6a-ad66-407a57a10a9b | -8.13953 | -44.08677 | 2025-10-04 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 419afe29-393f-3a3e-8afb-ea0a69c6f2e4 | -13.99515 | -48.18583 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eac212c0-3944-34e5-9135-fa40eb995964 | -11.68313 | -44.27535 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a65acab2-08bf-380f-a6e0-d442e756e4d2 | -11.92312 | -46.35579 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 92992060-bcfe-3539-b1db-581b5f62996e | -13.38968 | -47.55677 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 530c71c3-ddaf-3d04-bd5c-a28a11e51ccb | -9.76515 | -48.5848 | 2025-10-04 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96f1149c-404c-32eb-a840-f4550f7faf70 | -14.23466 | -46.08174 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa0fed04-54fa-3b9a-9d43-53897a2a6873 | -9.91062 | -43.79943 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf135f14-9e65-3100-a73b-8d382cdddf4e | -14.24021 | -46.10158 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a4c3410b-a335-3b2f-89a4-a227555a05bc | -13.09943 | -47.89471 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c48dc45-60d8-36ad-a84c-0133633e5d0c | -11.53876 | -47.67288 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22fdbf8b-31af-3926-83db-400d2008f2cf | -10.33585 | -50.33462 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e6b0c953-28a2-3b1b-8cb5-8240d2df3e4a | -10.86788 | -45.41367 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9e46d92-eddd-373a-ba6c-92b0fd03ead2 | -13.10809 | -47.84433 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f09722af-f278-365e-9665-fab0923f9427 | -13.1284 | -47.83464 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7c28c85-1be7-3d08-bee2-c513f15329b4 | -10.32266 | -50.33218 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| be86e1ac-1db4-36a1-856a-78af557430af | -11.44725 | -45.13876 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 18562aee-76d5-366e-b2ba-656098d98cbd | -14.19584 | -46.66513 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8a36f48-f322-381f-9553-3c86b83359df | -13.5248 | -47.27264 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1a1aafa-6b45-37c1-8739-06c9c28011e2 | -14.89068 | -48.39177 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 682c02aa-af22-3b19-a992-10c0db441318 | -13.33428 | -48.07983 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed38da10-6f20-3e9b-be67-5476c6a4d606 | -15.30489 | -46.28596 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e0bbecb-bf7f-342b-b7b2-1b26f1229f82 | -11.50156 | -45.00862 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee183f04-5a86-3060-9bbb-81714cd8d565 | -11.91154 | -46.36159 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0c3fd75-a233-36a5-8317-c9dd7a1bc33c | -7.72194 | -46.30094 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 385b87df-4061-3bf1-8f16-842b86090178 | -14.21786 | -46.07904 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c891029b-6e5a-3655-994f-11121d40b2c8 | -13.31243 | -47.24109 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 650f59ee-274e-3fa3-9546-762ac07f4bc1 | -12.07594 | -47.99418 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0f3ce5c0-b070-3725-9860-843d8312b06d | -9.97668 | -50.24146 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86513b12-f257-3ac3-9bd0-08a0efda460b | -13.33502 | -48.07546 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 61daea66-74f7-31e2-b1b8-72007c81c568 | -13.51477 | -47.24659 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61c593db-cecb-3965-ad94-a120198022a8 | -15.27748 | -47.1459 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e32b8abf-c04a-3e05-adef-ba14d0289496 | -15.32454 | -46.3765 | 2025-10-04 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc06e3c8-3e82-32f9-af95-ff1ae8c20371 | -14.46218 | -48.3952 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83176ca9-8917-3870-b395-c686ddcc6f33 | -14.70283 | -48.19644 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 625c61db-35eb-3470-b06b-05e2ad425a51 | -14.92073 | -48.34784 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df5e3454-59e3-31c1-b6e4-6f556420a7da | -13.99355 | -48.19665 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2d25d07-a9b4-3aa1-b28e-e0339cb708b0 | -11.53949 | -47.66853 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39d6320b-1869-32da-8f92-3d1239777075 | -11.78394 | -46.83851 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9a8e43d-1087-336f-b6f5-b20a036a059e | -9.39405 | -45.85854 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b97c16e-bb2a-3a61-8bdb-72dd144fdfeb | -13.10306 | -47.89539 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e58a234-01c7-3489-8e11-fa090d63e3e7 | -11.47366 | -45.03319 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d07eb45f-5e00-37cf-a625-3c393e5fd2dc | -14.92977 | -46.87448 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebb1fb90-65d8-368c-a921-4e5b4c9a7de6 | -10.02617 | -44.01433 | 2025-10-04 04:14:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4952ff91-a29d-31c6-bd0b-3cc31416fb47 | -11.14053 | -47.89411 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb58bbc6-9f85-39df-a1cb-d79df862e83c | -12.94684 | -50.98907 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 613d7b99-2f46-3d6c-b99e-840d26dfa0c7 | -10.34943 | -43.73024 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1adfe930-dbe9-3977-99f6-c82b4299a45e | -8.62775 | -54.99432 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2caa8f57-8b2e-38ed-9f6e-b3d7b6147ea1 | -8.9147 | -46.60975 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc94eb54-e4e8-3640-b3fd-d4527b51c841 | -9.4646 | -45.53709 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a798de15-d78c-30bd-b6ae-30315a78322e | -11.45911 | -45.14419 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0115929-6e97-39a1-b51b-52f18b0e948f | -8.62346 | -54.98322 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94f5994f-256d-3843-9697-84b1c875646c | -13.26763 | -47.20477 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 315e731c-0468-30eb-856f-d05a221f9f3b | -14.91881 | -46.87695 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68cdefc2-95c6-3bef-9d2e-3f68b0bc75a6 | -9.33798 | -45.7757 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df0593dc-90f6-3a63-8de9-6343a148cd2f | -11.44912 | -44.95645 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a77c4cb-1d32-3ac7-9d13-419e1eb33dbc | -13.05405 | -48.62615 | 2025-10-04 04:14:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0f3b659-d870-322c-a95d-82d28d364554 | -8.85057 | -46.79654 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c94ed6c2-f24f-3ef4-ba09-4c0b1c53f226 | -14.84931 | -48.28232 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ee21be3d-b66a-39cc-9d1b-2d07efc20ed0 | -7.91637 | -49.6424 | 2025-10-04 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93fce885-307a-3deb-811f-5cfc2bc155e6 | -13.43881 | -44.23181 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24e1a92e-ac1f-329f-882a-9473de4fc7bc | -11.43561 | -43.49372 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46de7b1b-d860-3de4-8d02-14a7255eddb4 | -13.72084 | -51.31183 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3fc349e-8441-3bd1-9e17-0ed70404cd8b | -14.20444 | -46.07664 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aef3bb22-843d-3136-8dec-6c968a86a14b | -8.23252 | -46.79376 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74e94fe6-0fd0-353f-bc16-91ac8ec08e1a | -11.87966 | -44.9838 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fdd9be29-39cd-3ca3-8864-6d6b9ca0665c | -13.31869 | -48.12705 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00efa987-9d96-3ba0-8fc7-972c936faf67 | -13.96512 | -48.18694 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5228e9df-7b1b-3b00-a5e4-495c02edc3b8 | -12.865 | -46.98788 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c624e597-8dff-3aa8-89c1-9c11af7549b5 | -13.54982 | -47.25289 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ac057fa-c9eb-351c-8559-9f6d8cddd3c1 | -14.69921 | -48.19585 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45248341-1c32-3e06-81d7-a0fea3a4914f | -13.33127 | -48.09751 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README90.md)
