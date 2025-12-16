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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 646f36b7-3aa4-35be-bbfb-acfaa034f1ff | -2.97561 | -47.92798 | 2025-12-16 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34fb99d1-29cc-336f-b69f-c8f416f904a9 | 0.12242 | -49.85065 | 2025-12-16 04:44:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a87afea9-536b-39c0-8ada-fcf903e9e420 | -2.22707 | -51.94413 | 2025-12-16 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 025b1a4c-0c6f-388e-8925-c9bb066efc32 | -2.79092 | -51.41247 | 2025-12-16 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f94ea538-4c09-3124-9ce3-667772867729 | -3.00422 | -41.87073 | 2025-12-16 04:44:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 51de4b35-5a8b-30c2-ad9a-281df10654af | -11.14398 | -43.33148 | 2025-12-16 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6b9bdd3-2e16-371d-96ac-306263a82b75 | -3.04119 | -51.48013 | 2025-12-16 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea85f7e1-62c5-3b1f-bb68-9955d0412662 | -3.06769 | -51.97408 | 2025-12-16 04:46:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8a865fc-cd6c-309b-b76d-35e811bac40b | -4.50144 | -48.92867 | 2025-12-16 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae0e1918-4594-3566-839b-5a6b93ed7a73 | -3.18668 | -51.99613 | 2025-12-16 04:46:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0af02720-9a0f-370a-9496-1a92a0eb4933 | -3.31568 | -52.0872 | 2025-12-16 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b501afec-e172-34cf-83cb-365049183dc4 | -3.07446 | -51.97514 | 2025-12-16 04:46:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 408f7bba-1099-314f-9e8e-885a22d80d87 | -4.75107 | -47.50691 | 2025-12-16 04:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cf75f67-fdef-32a1-ab78-6911f3628f54 | -5.94123 | -44.46194 | 2025-12-16 04:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e6d4f87-6a38-348b-9a38-ea85d31174c0 | -3.77131 | -47.95346 | 2025-12-16 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 309fdde9-335e-323f-b567-8796b9c876e1 | -7.86266 | -41.94186 | 2025-12-16 04:46:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4b8405c5-d797-3d98-bf71-6c3b0f9678aa | -4.63473 | -47.94016 | 2025-12-16 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97dad562-b551-3241-b82b-77a8ec99c6f7 | -8.42525 | -44.02949 | 2025-12-16 04:46:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24886cc3-fdb5-3943-9c31-05a4b3c5fe47 | -3.83682 | -50.72742 | 2025-12-16 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fedea00-e40a-3c52-9108-8a414e4950eb | -4.63409 | -47.94423 | 2025-12-16 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c4e1062-bd5b-3ce2-bf2a-f8b2764f02fb | -3.18825 | -52.02981 | 2025-12-16 04:46:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47155d17-e012-3dc7-b752-411bc437f26b | -10.03137 | -48.12561 | 2025-12-16 04:46:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15f53c54-bbd9-308d-9c46-0be9dc7f11ad | -4.40417 | -42.33556 | 2025-12-16 04:46:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d89f4df-a5a5-3428-b3f5-9daa6dbb3a2e | -3.02785 | -51.4564 | 2025-12-16 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6afd058e-3007-3635-bfce-75e983633989 | -3.97141 | -50.19856 | 2025-12-16 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7b67b58-2a8f-379f-a545-438cceac5146 | -7.61432 | -47.05345 | 2025-12-16 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb80afd5-374c-3fc0-a8b2-0a8e9a532c2c | -3.80165 | -49.03172 | 2025-12-16 04:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6659df6a-c78c-35b2-ada0-ba3551c9d7a3 | -3.83658 | -51.69606 | 2025-12-16 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad485778-3578-3fae-9464-a3b5190dc5a8 | -4.65964 | -42.40044 | 2025-12-16 04:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 814ed0bd-23d5-3c63-81e4-f35f3a658d4f | -3.94183 | -47.00214 | 2025-12-16 04:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9225e584-1787-3008-abae-a23dc87af448 | -4.75883 | -45.79202 | 2025-12-16 04:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 410ada25-fa90-314e-8a1c-384fd835c126 | -2.31535 | -55.70063 | 2025-12-16 04:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c2d07b3-b787-3558-8a82-1442506264c5 | -10.77622 | -44.4612 | 2025-12-16 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bdee7e1-be00-3129-ad92-5895679c554a | -7.86315 | -41.93833 | 2025-12-16 04:46:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 69c7bfbc-1de3-3eff-9ca5-96ae21cb628b | -7.61502 | -47.0486 | 2025-12-16 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d62c1daf-66e2-3399-b883-d55499da9efc | -11.14439 | -43.32827 | 2025-12-16 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4ccda66e-d708-3c9b-be56-a32e4ccf31be | -3.93748 | -47.00592 | 2025-12-16 04:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93aaecdf-a94f-3471-b72c-c8dbf3fc4c92 | -4.40796 | -42.33406 | 2025-12-16 04:46:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0d3fc428-4c48-30e0-9332-8e19272819be | -3.80222 | -49.02812 | 2025-12-16 04:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9d3d06f-6771-3bfb-8cd8-b20e8f4e84c6 | -5.11141 | -43.29056 | 2025-12-16 04:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2bcbddc6-6093-33be-92ca-8590295d4b07 | -10.6031 | -44.83151 | 2025-12-16 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac8bf7f1-1d03-3e6e-846a-68bee08d0df5 | -8.4197 | -44.03422 | 2025-12-16 04:46:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2132d084-66b4-3f23-b625-591e60576220 | -3.93814 | -47.00156 | 2025-12-16 04:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9f85d37-ff43-376f-b35d-f2592c661afd | -5.19256 | -44.29715 | 2025-12-16 04:46:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1ef72921-e2ce-3619-b09b-90b9534abcb9 | -3.65477 | -47.5604 | 2025-12-16 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a77557e5-89d6-3f3f-a8cd-8596ae1b4009 | -3.65898 | -47.55684 | 2025-12-16 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7063d57f-d61f-3dc0-bda3-327ce15f79d3 | -5.3967 | -44.68777 | 2025-12-16 04:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5909a8f2-cddb-3a19-8400-a6489a71b574 | -4.54782 | -47.91464 | 2025-12-16 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50f6c077-def7-3605-ad5a-980a5658a6b2 | -3.95895 | -47.18571 | 2025-12-16 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb216455-2627-35c5-88b4-810550cc92b5 | -4.11449 | -47.29327 | 2025-12-16 04:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c424b05a-40f6-3558-a5d2-9a08dfefde2d | -2.90554 | -52.54964 | 2025-12-16 04:46:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a3ae9fb-5e6f-3c81-8d2c-e09c75c1a6cd | -4.40925 | -42.33627 | 2025-12-16 04:46:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 33127016-ac48-32df-97d9-3bf364ebc708 | -11.14962 | -43.32897 | 2025-12-16 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7e99c655-6fc5-3c07-894c-11b5284af2e8 | -10.99954 | -44.34637 | 2025-12-16 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efdfff31-4f2a-3a9d-8716-d407979f0e8a | -4.63118 | -47.93962 | 2025-12-16 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0db5b1f9-ee40-342f-9b25-75c6e6ebb5a6 | -2.776 | -54.52546 | 2025-12-16 04:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 834d4a53-fdd7-33a5-a055-5ef560f290b1 | -5.59246 | -44.88406 | 2025-12-16 04:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44e87f76-0e67-374d-8aaa-a8c44381e2ff | -10.60527 | -44.83427 | 2025-12-16 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b080678-8d8f-3918-b044-289957ac7517 | -5.19063 | -44.29436 | 2025-12-16 04:46:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9ed8fcb0-01c5-3321-8423-69bdcdea58fb | -5.1951 | -44.29512 | 2025-12-16 04:46:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1bb77539-229e-38f0-ae1c-3531d213c3fb | -3.95031 | -47.1932 | 2025-12-16 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec9aa2e5-c0d8-33b3-8f24-79b45fa0e3a2 | -5.48509 | -45.4379 | 2025-12-16 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99298aed-b4ec-366d-a103-3a822231ac7e | -10.03014 | -48.12766 | 2025-12-16 04:46:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d75bdc8-263b-320e-acb5-d5f71d12539d | -11.09011 | -48.25161 | 2025-12-16 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f44cb64b-cb22-3320-8724-23f98cf1d432 | -4.65878 | -42.40633 | 2025-12-16 04:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 47b7884f-f0fc-3691-99ed-17a9a82d57eb | -4.40289 | -42.33331 | 2025-12-16 04:46:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a60605f6-a26c-365e-80b3-4fc5eb63e297 | -4.65414 | -47.81554 | 2025-12-16 04:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1f49af0-2b92-39e0-9085-fcbdc48b89df | -4.66007 | -42.39749 | 2025-12-16 04:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 39696f2b-8b11-3930-9612-92bd43b39e03 | -4.73986 | -45.67309 | 2025-12-16 04:46:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01d9c4f4-0916-3c70-a954-14cec4a44752 | -4.75637 | -45.78812 | 2025-12-16 04:46:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac777ca1-5e54-365e-9762-2a43ae9c055a | -5.11552 | -43.29286 | 2025-12-16 04:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bcfbafc-447c-3f17-9feb-bb822225e277 | -11.08943 | -48.25625 | 2025-12-16 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33feab32-166a-332c-a86f-4d52156d1b45 | -3.18882 | -52.02619 | 2025-12-16 04:46:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac594272-b270-3a67-92e5-03c0f6abe179 | -3.52305 | -52.56755 | 2025-12-16 04:46:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfd94342-08a5-3417-b042-a49a3171339c | -4.75191 | -48.23549 | 2025-12-16 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87ffde60-c57e-3fd3-b26c-e5a16fad86dd | -4.36632 | -48.19969 | 2025-12-16 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6d9f5e0-2d4f-34dc-9099-46f9e8729acb | -5.11219 | -43.28535 | 2025-12-16 04:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28d3d98e-57ab-3b3c-9ed0-462dcb595d18 | -5.19321 | -44.29261 | 2025-12-16 04:46:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2014c5ba-f349-33be-b3b7-1818a8aa7df2 | -4.40754 | -42.33699 | 2025-12-16 04:46:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d423018-e987-3b50-8cc6-5939d1f9220d | -3.07049 | -51.97824 | 2025-12-16 04:46:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fd4ee08-3c9b-38d5-9c6d-41d5fe02adc7 | -5.39232 | -44.68715 | 2025-12-16 04:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95a8cd03-474a-3a1e-a3f9-5bd2f9828b3f | -3.69803 | -53.75693 | 2025-12-16 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 160bcf93-2b73-3b88-b2c1-78c357e265c5 | -3.95097 | -47.18888 | 2025-12-16 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a40d742d-c6a0-312c-ad81-9648b2c4d74f | -6.33104 | -46.32825 | 2025-12-16 04:46:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e86aeb8f-f1d4-3c40-9dc9-2da715674a18 | -3.07107 | -51.97461 | 2025-12-16 04:46:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f6e71c1-d0e9-37ec-ba71-c8b775c78faa | -4.40461 | -42.33261 | 2025-12-16 04:46:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9731f75a-95ed-3e79-b00d-82a811bbfddd | -5.11621 | -43.29127 | 2025-12-16 04:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6003616-ba98-33db-915d-8c4f4e325d34 | -5.94186 | -44.4575 | 2025-12-16 04:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19c9117d-1594-30c0-a97c-70d664ed4472 | -5.72108 | -40.50623 | 2025-12-16 04:46:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f7408986-c310-3bdd-8c83-81c6defdc4e0 | -3.91001 | -54.56175 | 2025-12-16 04:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 711cee62-88a2-30e3-8b28-afb9111c202b | -3.6596 | -47.55275 | 2025-12-16 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 886f5e27-fc1c-3db2-8a67-8e8da8cab455 | -4.65921 | -42.40338 | 2025-12-16 04:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 93f578a5-7c87-35bc-9f5f-72e1bf4a1258 | -3.94118 | -47.00648 | 2025-12-16 04:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b4b408d-a9a1-339b-b649-e5dccfc84db3 | -4.33589 | -48.59289 | 2025-12-16 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84dcd29b-c0de-389c-b7ef-f9ba778f3095 | -8.41417 | -44.03886 | 2025-12-16 04:46:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 924ef8ef-abf7-32d3-aaf4-97179f7fbb89 | -11.00172 | -44.34537 | 2025-12-16 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30aaaab2-4169-3b9c-a052-18d8f73ca486 | -10.98585 | -47.73701 | 2025-12-16 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e742700-6afa-399d-9063-37b1c7a4862b | -4.65058 | -47.81498 | 2025-12-16 04:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfb999f1-7475-3e47-b53c-d33574dd029a | -11.75785 | -44.03347 | 2025-12-16 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49947299-eb64-3f7b-ad7e-9432a995992a | -5.48925 | -45.43856 | 2025-12-16 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README12.md)
