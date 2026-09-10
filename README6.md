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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e3cf9db-1d85-3d76-9d64-2be64619607e | -7.2669 | -45.359798 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f202628-a6f2-3aa7-9ae0-914e926a6119 | -5.7709 | -45.089001 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbdc2b33-b022-3df2-b694-83e94fbaa11c | -3.2436 | -47.247101 | 2026-09-10 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f98aed9b-1d96-3e93-b66b-79a7c70a294c | -12.8434 | -44.3554 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e13e87f-a52e-312b-aa4e-6e8b751c46fd | -12.647 | -47.1022 | 2026-09-10 00:28:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0ab3864-4580-3194-9f80-922c760b83ff | -9.3289 | -45.632099 | 2026-09-10 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8b70a071-943b-3ef0-b3aa-385e2c97679c | -5.5742 | -45.669601 | 2026-09-10 00:28:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d5a2f6d-064f-34d2-b101-fc7bba315899 | -4.8586 | -47.4142 | 2026-09-10 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2147aa2-8c84-3add-b0eb-c6e6f3df7721 | -15.7836 | -43.543201 | 2026-09-10 00:28:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 367fee5e-81f1-301b-8f33-256ffe5041f2 | -6.7143 | -46.3283 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47b6c39e-1fa3-327a-9870-1d5c27ffcfae | -5.7595 | -45.084301 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c35ac332-f9c9-378c-8ff3-1952ba7835bb | -6.4254 | -43.062901 | 2026-09-10 00:28:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6cf590e-35af-3046-85c9-3e4bca2bb5ee | -10.6661 | -46.083599 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b2c24d4-153c-3a97-956d-da488b566904 | -11.2107 | -49.931702 | 2026-09-10 00:28:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afa29a0b-addf-3584-8af2-eb556b71ab15 | -10.91 | -47.847801 | 2026-09-10 00:28:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eda89cbd-dc43-3a95-a0a9-c950ca5c7c9c | -12.8583 | -44.330002 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95d1ed7e-17a3-3e3b-949b-8011ec29dca7 | -7.1039 | -42.130299 | 2026-09-10 00:28:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57e87e20-26de-3332-b0b6-9061a274d62d | -7.9482 | -43.7939 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b85bc0c0-d8f2-3e1c-8062-8318f9da12b1 | -10.0771 | -45.4776 | 2026-09-10 00:28:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b8f354e-b96c-3a41-8a4b-1f1b01d54374 | -12.8206 | -44.345901 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc1fe44f-15cd-3426-b9ac-1c0a5d1c0f40 | -7.0478 | -42.7244 | 2026-09-10 00:28:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 05fae082-41b5-33bf-ba5e-ae13e3714568 | -7.2653 | -45.352901 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c265645c-fd66-3e4b-b726-fbb17adc9e4f | -8.3144 | -45.1152 | 2026-09-10 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 38af685f-c378-347b-ab80-4d6fc9d25f33 | -3.5496 | -48.183701 | 2026-09-10 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e6ef851-8d02-39e3-af22-9e89a1351a63 | -10.7583 | -45.943298 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e4953c6-e75d-3738-ab69-3b238a2941a0 | -12.8598 | -44.336899 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 22ad665e-f4a2-3103-9c9c-27aa7c8f5aa7 | -9.6923 | -43.4814 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02a404a6-49be-34e8-8e35-3f8695b86cde | -3.3712 | -50.398102 | 2026-09-10 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aad64f93-e6a3-3c88-ab5c-048862165503 | -1.4761 | -47.273998 | 2026-09-10 00:28:00 | METOP-C | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b25fd1e-7c50-3117-b1ef-973332cb6f7e | -12.863 | -44.350899 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8c66ee1-7fb2-3898-aa5c-69b108ee4aaf | -13.5346 | -43.313301 | 2026-09-10 00:28:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e045dcd5-d8a7-3c89-b918-f326806b2577 | -3.242 | -47.2402 | 2026-09-10 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9852cf98-0747-3ed9-88ed-c69da5c83e5d | -11.2152 | -49.953499 | 2026-09-10 00:28:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44964054-ab69-3e75-be04-a8f2caff1ac1 | -7.9499 | -43.801102 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a9fe84d5-266f-39a1-84fb-62d434f5c4fa | -3.2452 | -47.254002 | 2026-09-10 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9319ebbc-f855-3593-aaa8-ca60d8f9659d | -12.85 | -44.339199 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 265fac7d-933b-3ff1-a65b-041c7e98b02a | -5.1159 | -46.009701 | 2026-09-10 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1fea53b3-a649-3ffd-b0cc-d1d8e81ab533 | -6.4954 | -47.593399 | 2026-09-10 00:28:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea97d073-bf5f-3feb-a060-06607f76b5fd | -13.4368 | -43.834499 | 2026-09-10 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfc52d4f-3e55-342f-8986-0d35fba4d102 | -11.8677 | -44.8731 | 2026-09-10 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0bd38165-92be-36fb-a2a3-9136344ddb85 | -11.8579 | -44.875401 | 2026-09-10 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef81841d-45ce-3965-a92b-3c666c3f7cf2 | -9.6873 | -43.459599 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0ef0ce86-888f-38af-8cea-b57b4cd23150 | -10.4223 | -37.168301 | 2026-09-10 00:28:00 | METOP-C | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0ae9019-76e5-3870-81f0-fc12eae1b790 | -7.0576 | -42.722099 | 2026-09-10 00:28:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0a9de663-bf2c-3c47-9723-c1679132e71e | -11.8449 | -44.863602 | 2026-09-10 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 741fd1c7-92a9-3e76-9c2a-cab99299a7e4 | -9.6856 | -43.4524 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ccac7c99-1dc9-30a2-8c53-ed127bda29bd | -7.9949 | -43.9506 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4d8d31db-13e5-33be-a941-9dce49099657 | -2.2107 | -48.231899 | 2026-09-10 00:28:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd3fdf2-0f40-3771-922d-9454036c13f6 | -6.4783 | -46.287102 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b62f9bfd-ae45-3da6-9dcb-338cac6c1a59 | -7.4649 | -46.1385 | 2026-09-10 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8664ff41-28f6-38ad-bfda-4f58c7cd0ac1 | -5.3255 | -47.474201 | 2026-09-10 00:28:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58b2edba-11cb-33e5-b4a0-d47e1be7ac93 | -6.4273 | -43.0709 | 2026-09-10 00:28:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71368fd0-b7e5-35fd-abe1-14f6dbd5c692 | -12.8336 | -44.3577 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 715b7b23-cfe9-36ae-84d6-cbf65dda2391 | -12.6436 | -47.086201 | 2026-09-10 00:28:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c312b68-a691-3c9c-9b14-596b56fae303 | -12.8175 | -44.332001 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd49ebfa-5ce0-387f-a37b-e20f7b203728 | -11.8563 | -44.868401 | 2026-09-10 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58bceae2-d07f-3783-94a0-ec4ce4db629c | -12.8453 | -44.318298 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 992068cd-7208-348f-96ac-5af69906ebeb | -5.5994 | -45.375 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d55f5bcd-36de-343b-b6d7-15985bdf8f54 | -10.2736 | -45.2071 | 2026-09-10 00:28:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fd050bb8-e38b-3d5f-bb90-d0b913fb087c | -13.5329 | -43.306198 | 2026-09-10 00:28:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e62a9da9-8b81-3fdb-a121-c5843fda6048 | -15.7868 | -43.5574 | 2026-09-10 00:28:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 24ca13bd-a3d9-3115-836e-dfcb79cf5c67 | -7.0459 | -42.716301 | 2026-09-10 00:28:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7fb43939-f884-3c02-871e-a1a13892cd4d | -12.4037 | -43.422199 | 2026-09-10 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 006e38b1-4784-32a1-8973-6f0b3b956ea8 | -10.7318 | -46.008999 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9498a58a-4d2b-36e1-9d03-c5d4f0051c00 | -12.3511 | -48.2103 | 2026-09-10 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 173bc581-eddb-3d82-9ac0-bd2e014eeb8a | -13.4482 | -43.839199 | 2026-09-10 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e7f4dd6-8add-3d29-98d9-c6a788e57561 | -11.213 | -49.9426 | 2026-09-10 00:28:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a04c5b75-9aed-3300-a386-cd3fe55eceb1 | -12.8532 | -44.353199 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eeadafcb-59fd-38a2-99d0-0b82394d7a44 | -7.9867 | -43.959999 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f50cfb1c-91da-386f-9344-fea40df8c356 | -5.6599 | -44.295601 | 2026-09-10 00:28:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d09c9248-5c41-3b10-bc20-4ea0ca4504f2 | -10.7308 | -45.912201 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7c67842-24a3-34b8-8f4b-7c7d9f4323e2 | -10.0688 | -45.4869 | 2026-09-10 00:28:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c55ad874-b805-3a83-a8d4-1d31cb7986ac | -5.1034 | -46.9491 | 2026-09-10 00:28:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 398f69b7-4fcf-3224-baa0-40ab038a94d3 | -18.0375 | -43.021599 | 2026-09-10 00:28:00 | METOP-C | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 749385f8-c114-37b5-b17d-2cd19e22d828 | -5.602 | -44.848301 | 2026-09-10 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a3370a1-2eae-3b82-93d1-a7ccc66657bb | -6.1707 | -44.630299 | 2026-09-10 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 504c7f40-8c81-3053-9378-c73821ce810f | -7.0242 | -45.110802 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 508c2aa3-ea4a-395f-8142-ec2580aa7f7d | -9.7227 | -43.389999 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4f901a7a-f720-3db5-a764-e8e173e158b4 | -7.0557 | -42.714001 | 2026-09-10 00:28:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8ffe8806-e91f-3b50-b338-6b5155733754 | -12.8548 | -44.360199 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4087fed5-1b6f-3cea-81fd-a752d663e536 | -7.4664 | -46.145401 | 2026-09-10 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6eca0acf-010c-38d2-9840-d60d01e0778f | -4.3671 | -47.791302 | 2026-09-10 00:28:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 074fc680-5be3-341c-bb3b-b5ae471a0ada | -6.4586 | -46.291401 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9186bab-9916-37c8-81a7-76e15d049ac5 | -14.2015 | -41.6045 | 2026-09-10 00:28:00 | METOP-C | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4b06b9c8-10d4-3d00-9371-1afb3fba8331 | -6.4458 | -46.099499 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 897c7f62-18a5-3637-a20e-ab7f2843e400 | -5.8023 | -43.7981 | 2026-09-10 00:28:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc2c4eb9-c630-3aa9-b03f-56ccc519966a | -6.2687 | -46.3629 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39a55973-ea93-3c67-969d-99374aeb0b78 | -6.1609 | -44.6325 | 2026-09-10 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71602f67-3bdc-3712-8333-4b94c198e908 | -7.9901 | -43.9744 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d4a4cb32-8609-37ad-8b0c-0e8fe7f6100b | -7.9982 | -43.965 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b360fe16-02ec-3c6f-882c-4721e0dcdc90 | -2.9362 | -50.474602 | 2026-09-10 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da24edf9-6d9d-35eb-bee9-9a2de3e9ef49 | -13.44 | -43.848499 | 2026-09-10 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7aaef25-400b-372c-9e7b-ec3bc03f9fe6 | -9.4811 | -48.1675 | 2026-09-10 00:28:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13c56949-1e43-3d0c-934f-75600c1da115 | -3.2585 | -50.080502 | 2026-09-10 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6247f021-192b-3e50-8ac5-2e865f86c4c7 | -9.7129 | -43.3923 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 91af3650-b4db-3f6c-a55a-75f3372b0faa | 0.2643 | -51.4608 | 2026-09-10 00:28:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fa368c2a-eeb6-3815-b2fe-1cb942fe2b1e | -9.7146 | -43.399601 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 42d469ca-eafe-3449-91c9-5c1daf5853ed | -3.2451 | -43.2276 | 2026-09-10 00:28:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af290094-e795-33c9-b1f1-da0ab9d9a9b5 | -12.8191 | -44.339001 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd69c603-853d-3335-b5b2-b910771423e4 | -12.8485 | -44.332298 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
