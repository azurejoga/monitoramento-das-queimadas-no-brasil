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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34b32bfe-e865-3e4d-962f-fefe833e5306 | -3.16529 | -49.47661 | 2025-09-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c7fae2c-791e-3749-b7ac-29c6449b738d | -12.92233 | -48.03791 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa48c564-b26b-370d-abe9-0968a481b073 | -16.92308 | -45.75558 | 2025-09-06 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| f0847db8-ad95-32d4-8626-728f19c8fddd | -6.20184 | -43.41796 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2a88617-e093-3f29-94fc-a98ec2d6df47 | -11.6363 | -54.53931 | 2025-09-06 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b2eba80-4fd6-3577-b63e-910a2cbe8339 | -8.10093 | -45.33718 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd5d12f3-0cb9-3445-9f23-60b32971669e | -5.68366 | -43.57552 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71444213-9678-3b10-b544-50aaef10cd38 | -6.2962 | -43.08055 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46daafce-1c74-3a38-9296-c9e5fa0d821e | -8.18934 | -44.78973 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbdc408a-65ee-33a1-93e3-b65d38bdd5f2 | -3.35764 | -43.37444 | 2025-09-06 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e93a6080-9d69-3326-ad2e-f08cdf62e2a4 | -12.95409 | -54.80057 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f0b8bce-4a14-3e9e-ad15-159177e265a6 | -10.60782 | -44.32743 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cc461e48-948f-37cc-a409-ec2f4218d020 | -7.05641 | -50.85976 | 2025-09-06 04:17:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 914a36b4-5114-32c5-a72e-386cc57d7c34 | -7.33674 | -43.94238 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17d395b5-89a2-34bd-b4bf-3e80d3d77ff3 | -12.95897 | -54.81754 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93bb64ec-62d6-3bbb-90fe-cedbd2598a31 | -15.18741 | -48.04176 | 2025-09-06 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c572e6f7-2da5-37d6-8d2f-86d2beb86e5a | -6.86291 | -44.26192 | 2025-09-06 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f9d5f4c-b633-37d8-911b-840ad559c436 | -7.36661 | -44.32368 | 2025-09-06 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f12b865-322e-3d04-86fd-a8b598ea4142 | -5.2137 | -43.69915 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dfb0350a-40c3-38c3-9391-a637b77d470f | -5.74723 | -43.70409 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d718310-54c5-3eb3-b325-70d5e28568ba | -7.81371 | -47.50415 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be7fcd4e-83ad-359a-beca-45e405f7886d | -5.96275 | -44.73679 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5aba6886-5fef-3e50-9f6f-0e733ad36df2 | -6.50864 | -43.0639 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9119c087-a818-3686-a903-9567f40cf8d3 | -10.31028 | -46.41869 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d92699c-f5d4-3813-a1f0-22b1b95e5542 | -8.74968 | -44.23015 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43799575-b736-3869-be17-1b2af56ac9f7 | -10.31793 | -46.416 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9532cd1b-7b4f-3b96-a69a-16bd483efc8c | -6.53943 | -42.93354 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 899a4708-1feb-3276-b377-d6ba55b404b7 | -12.99999 | -54.81788 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e8c19e5-a002-3508-a473-18079c139452 | -8.67696 | -50.01738 | 2025-09-06 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0c8ebc7-f18c-3f60-8e45-c140261233fd | -6.21787 | -43.35994 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77e33a6f-ab61-3330-9713-08e08507bfd7 | -6.01183 | -43.70273 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b623dad-3db5-3b0f-a445-c1e22a97a7ce | -15.22281 | -52.35501 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 014a0c17-1508-31f2-bb67-248514144ce5 | -6.35215 | -43.54176 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f37df7e2-752e-3b45-b2f1-4c899471b7d2 | -15.63945 | -41.8586 | 2025-09-06 04:17:00 | NPP-375D | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8ca3dcaa-e221-3746-b00b-941c2035793e | -6.20128 | -43.42144 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c3dfe0f-11c1-36f3-8db5-3c9a44d6408c | -8.64064 | -45.74993 | 2025-09-06 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ae230ce-c8ee-38c1-b023-b5d6b94f81c4 | -4.83046 | -42.73969 | 2025-09-06 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bf61e114-2902-33a9-bfb2-67972616b96c | -5.73165 | -49.28429 | 2025-09-06 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8601f720-3ba3-3efc-b117-44aa5f64771c | -5.95968 | -43.02718 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e14fec66-bbe8-3a2b-b1ba-0cea9e13035c | -13.85131 | -46.26576 | 2025-09-06 04:17:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ac83001-c936-3821-9305-750960468871 | -6.15377 | -43.16846 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 72e0cf1a-36d9-3ee7-bef8-924e6e72f7a0 | -6.1118 | -43.93899 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a0b139a-77fd-3104-8ad2-2191ad4b8d82 | -7.24306 | -44.04297 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d60e57c-dee4-3ca5-be8c-2b3b959b9c0f | -14.11321 | -51.72063 | 2025-09-06 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c4dcf13-502b-34f4-9463-18592059f332 | -5.96676 | -44.7337 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afbd1a0b-5b9d-302b-8687-022eab8a7a59 | -3.3056 | -48.71543 | 2025-09-06 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a945852-d531-3ea7-be0d-5a1568e750fd | -9.08959 | -47.00118 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df0c13f5-68e0-38d7-b566-7c7e1ba4fe33 | -3.79441 | -47.58198 | 2025-09-06 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa108b19-6fbb-303b-a983-5339d06c034c | -7.80369 | -45.42979 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4aef0d2a-465d-33f1-90c5-0b7f4aac0138 | -12.5072 | -53.86617 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00e67b16-f804-3bb1-a343-7c1f1b4b62dd | -10.15638 | -46.23328 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2193747-cc2e-38b0-a7d4-d48a73f404cc | -14.57143 | -48.03414 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54a32304-238e-3018-80bd-08cc2edc10eb | -9.79683 | -48.33573 | 2025-09-06 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 379de865-03fa-3f1b-9dbb-ff88c4142490 | -5.95815 | -44.74362 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc4754da-68ce-32cc-8984-3f3dcb8ac733 | -6.2833 | -53.44784 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7718e046-4c14-3c17-83d9-a43fdbc179ce | -5.98195 | -53.59685 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f713d246-c414-31b3-9c4c-65a3736b5314 | -5.38475 | -44.07149 | 2025-09-06 04:17:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf8d00e0-25d1-3e07-8a75-4019004897e5 | -8.34904 | -52.54929 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 296c4b81-bf50-3f2a-8324-271e2a015d0b | -15.54017 | -48.40215 | 2025-09-06 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e225e7ae-1114-3364-b7c1-fa1b26d28f2d | -3.2374 | -50.04787 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a125360c-e0bd-3e96-a5a3-99b12507f115 | -5.20979 | -43.70214 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c05c2b3e-b5b4-3396-8a01-8f08982548df | -5.83964 | -44.10696 | 2025-09-06 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2187976b-f4cc-3521-847e-1441f20560fd | -9.05524 | -50.45159 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 139619cc-c4e5-3fab-a124-fa1f091f55e6 | -5.70676 | -45.14709 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37ca36c0-d7ea-3955-ba96-9a0f111fbd35 | -6.38477 | -43.01263 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cefc8e29-8a76-3edb-9d21-0931e653ecc6 | -6.22588 | -42.64638 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c35aadbf-b4c6-3d14-b5bf-25de8e070abf | -7.62448 | -43.87348 | 2025-09-06 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e246c81d-1b51-3558-8169-d8449d5f37be | -15.54498 | -48.39622 | 2025-09-06 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| caf9ee12-d0b5-3042-8b52-bda64e0b6ca7 | -13.36214 | -46.83462 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7dde789-14c3-38e5-a0f6-4b0478f9f9f8 | -10.14591 | -46.23153 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 813686dd-0963-3183-b1d0-304d105815cb | -13.01611 | -54.82534 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cca05a4d-0192-3965-aaa1-091d80f5a15b | -6.37871 | -43.8182 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc7cdf07-e988-3ba9-8a5b-f0bf8a21a1b6 | -15.36686 | -46.41888 | 2025-09-06 04:17:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0d21899-c019-3b87-84fd-461bc4ad25d0 | -7.53921 | -42.52918 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb0e0b21-fb6e-31ef-a316-974cbf01676a | -13.01459 | -54.83304 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1f69a768-f495-39d1-97be-70c4599f27aa | -3.48288 | -48.94524 | 2025-09-06 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d3a2727-5fe2-3f03-bce0-01ee01835a55 | -6.19412 | -53.24861 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4633ca57-4603-306e-88ef-1fe3bbfabd10 | -8.34351 | -46.95311 | 2025-09-06 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63b13e2f-4159-3ebc-b1e9-4d989aff5290 | -6.19796 | -43.42091 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e520f711-53b7-3253-b1eb-cdabd772b2fe | -15.18035 | -52.37638 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 48b15f3d-9871-3f99-acfe-2e5f0ffb5b84 | -6.6103 | -43.96002 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50d4db1e-d1c2-31a8-b6e3-122bcab78e2b | -6.34771 | -43.54819 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77eb6dc2-44cd-3d94-84c1-74e4a4a8eac8 | -12.89605 | -48.01484 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09c6d3e3-d250-39d0-9caf-fca8b0b16fb2 | -6.2314 | -42.633 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d321ec46-221d-3fe2-b227-cc0540c64477 | -8.36531 | -48.26979 | 2025-09-06 04:17:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1b22bbf2-7670-3c1d-a48d-e9f15c4adb81 | -6.29675 | -43.07708 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6a33331-2f4a-3dba-8a23-86693874d3ec | -9.07802 | -47.02522 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74c9dbc9-394b-34bf-80d0-2336774d9aca | -3.24365 | -50.80262 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 70dc4551-2b69-3270-94eb-0fc20c02e18a | -12.97668 | -54.81709 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec92cf30-1792-3095-ad87-f246416f6788 | -10.08776 | -48.09187 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e63c65a-e12d-39fd-8549-23aecbebdc06 | -2.8522 | -49.501 | 2025-09-06 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a8f3a25-34d1-3dd0-a9e7-835fd5af07ec | -12.97508 | -54.82507 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7aad13a-f93b-38c7-a558-5da997b6eae2 | -10.08858 | -48.08707 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9e2086e4-f19c-3b96-97bc-8e2b72928aa6 | -6.2372 | -43.28111 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b031fb93-3996-3144-b70c-dc6e303b7ea8 | -4.79356 | -47.26263 | 2025-09-06 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17c8e850-583f-355d-b4fd-eb0533ef5697 | -7.28045 | -43.70038 | 2025-09-06 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b860c444-fde3-349e-af53-87ea1048f584 | -5.55765 | -46.5431 | 2025-09-06 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d718b5db-c404-33b5-84a8-2f1f875f16bd | -14.84458 | -48.18674 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e184e95c-1c58-3f84-8f5d-fb1aa8f6a54a | -12.98638 | -54.8273 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c33d3f1-6692-31bc-8ab5-c2626355361e | -5.11183 | -42.91103 | 2025-09-06 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README45.md)
