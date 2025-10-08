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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ced35b3-35df-3d6e-8e31-dd3b54198922 | -5.39459 | -40.98297 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d9caebcc-c2c2-3633-b7b9-d61b286d4a10 | -4.85852 | -45.79353 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec92cc5f-4575-3d63-b851-c04a1cee8f87 | -11.13767 | -54.8806 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17e05abc-b126-3f29-a154-90495bc49d53 | -3.08685 | -50.57082 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 085083e2-560b-3375-9402-f8637b30e1bb | -7.58417 | -44.03147 | 2025-10-08 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90d22de3-03fb-3d07-99a9-2aaf2f121a66 | -4.96193 | -48.01669 | 2025-10-08 04:17:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e93f067-4763-3fc2-8f80-8359cea7a002 | -13.06095 | -47.95707 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 397de4e0-969c-3313-aeca-db779ceeb117 | -7.00399 | -42.88538 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 2c1084ea-32b3-3429-9b0a-42eafd412c91 | -13.39672 | -46.7029 | 2025-10-08 04:17:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9213e74f-749b-36f9-96ec-8536d1cff8bb | -7.78107 | -42.39717 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1d87b3b-fb16-3a23-af0a-670549e39571 | -7.00841 | -42.87893 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 5bd199df-a88b-3975-95c0-98281e59df99 | -5.61273 | -45.18909 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f23fbd12-f88c-3aae-adc0-c8e47382e1ef | -11.11837 | -54.03514 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28742d98-4754-31cd-aa48-cfbb3e8037d9 | -7.52419 | -42.97798 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6ab8a227-1f14-3c50-a6b8-e64c1ca41337 | -12.24564 | -47.8756 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 381841ec-2e53-37d9-8019-2285d968cd2d | -7.34674 | -43.86767 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e60b08f3-6216-378d-8c86-d4af0668db96 | -11.46197 | -50.20814 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b97e3320-5e90-349f-a70c-2a9f6c88a0ee | -11.1775 | -54.88617 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 18ee89af-1e55-3361-acf2-d7f8496abaa2 | -5.76082 | -45.74867 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc205fdb-6310-33e6-b8a6-4b10ae2fa300 | -12.37495 | -50.30779 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07737b6c-f615-3548-be44-1b5978b43ebc | -11.11767 | -54.03873 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9af4aad9-d248-34bc-91ca-cb2bf3f4ac3d | -5.82045 | -46.74331 | 2025-10-08 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2cc9442-602b-3b06-b097-2e055ddf07ea | -12.94314 | -46.84778 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fe065e6-b908-394d-80af-03664d007e3e | -11.14106 | -54.89422 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afa5a735-1c25-3016-8ee7-23fc45738f24 | -5.13199 | -44.96739 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0dbdb441-0ca5-38f5-8e93-f355a0683d08 | -6.66493 | -41.38536 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7a0e44da-0196-39e2-b958-f02aad885c3d | -2.61377 | -44.25076 | 2025-10-08 04:17:00 | NPP-375D | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 706dd1c4-fa52-36b0-ac06-a4869be68f9d | -9.68507 | -49.93619 | 2025-10-08 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1a76530-7cfb-37aa-bbd5-0405d5f9ce4f | -5.48447 | -44.6168 | 2025-10-08 04:17:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d0f49af-48d9-3c53-a6b7-c99b284225e6 | -5.48789 | -44.61733 | 2025-10-08 04:17:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 786a9d3a-385a-33fe-b159-b1e3b6d22ad6 | -9.63638 | -55.13586 | 2025-10-08 04:17:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 269fbae5-63b0-355c-bcfb-af48c92ac128 | -11.18825 | -49.77641 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aa569e1-f188-32b5-a28a-c0ad6b847345 | -13.00127 | -46.78633 | 2025-10-08 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af291610-76a1-39be-9233-f7fd53a46171 | -9.79366 | -47.74532 | 2025-10-08 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 44564c60-7e10-368f-8554-e6d09b552b0d | -6.45065 | -44.58237 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59e91db2-e593-37ce-a79c-a0d76a81940e | -11.04668 | -54.32813 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf7cf9fc-71a8-3702-8179-6b2ee12c20ec | -7.79004 | -42.40588 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2a4faa4e-b9f0-3b66-a345-851779140631 | -7.15716 | -39.30825 | 2025-10-08 04:17:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bd6605d3-1671-32c1-9704-c7ef1f1af7af | -5.4717 | -42.20531 | 2025-10-08 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4de64d51-d3db-39ed-b898-ead8d3f42d9c | -13.06388 | -47.93972 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f21ca1d5-ff18-3c96-a123-764b78b05eec | -7.47573 | -43.0955 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| efd12dc2-13cb-3230-a228-15b5b7764e4b | -5.13727 | -44.95652 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a2f466c7-e19b-375f-8d38-c9cf00fe28ba | -11.6957 | -50.95804 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dff45f04-364b-30e5-8338-e8666b2530a7 | -7.45031 | -43.14861 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a4eee4ea-32a5-3ea8-855c-b050b484d5e3 | -5.36765 | -40.99782 | 2025-10-08 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bd11bf33-6373-37f0-ab85-ed76ac20aaf0 | -6.69518 | -43.40651 | 2025-10-08 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86d28425-ddf2-3f6f-a947-df20fad28799 | -11.76168 | -46.80995 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e11462b-e702-3136-a6ee-6e622456fe9e | -11.28037 | -49.98766 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51211f25-db8d-334e-85d4-e241b0c45d94 | -5.32002 | -45.26081 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dd489c2-8b6d-3afe-86b7-813ee4155ead | -5.25383 | -43.15347 | 2025-10-08 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c138d1fb-b06c-39c8-96c9-5e7ac9dfaf0c | -10.88822 | -53.76206 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4537583-e346-3b94-b163-e52af3596777 | -11.78576 | -45.0951 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d93efa8b-1f20-350d-af17-0154c340497b | -5.31508 | -44.99877 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bebc06e6-7a49-3187-ba2d-99a1ee0d9e56 | -7.50783 | -42.71713 | 2025-10-08 04:17:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6aa96275-ba8c-3fb4-b4b4-71bbafcd3731 | -13.39388 | -42.69776 | 2025-10-08 04:17:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9d947065-bf04-3a4a-8d14-e512938164a6 | -7.35452 | -43.86172 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7e537c8f-7792-3c97-9c5b-6b802a1a7453 | -11.47407 | -43.48804 | 2025-10-08 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b805981d-12e0-3682-be9f-07bde7dbd5c5 | -2.09923 | -45.2797 | 2025-10-08 04:17:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3885ea3-7787-3ac3-bd14-3015aca4f551 | -13.278 | -48.04358 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d856e2a8-5c6d-3faa-b7f9-4ed0d6812c6d | -12.16985 | -50.98435 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32c953ef-d329-3e99-aaf7-544d35066e00 | -3.20097 | -51.01535 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb368d58-779f-3727-b13f-a12ed018cbf3 | -7.02118 | -42.88452 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 3c21c2c9-981f-3140-b72c-66002865c597 | -4.13713 | -47.65051 | 2025-10-08 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 924fc383-fdd5-312e-8463-05a8faf95f3c | -7.01895 | -42.87701 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d18d1f3f-cdce-3e07-9def-d665610a88bc | -11.95558 | -51.46083 | 2025-10-08 04:17:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1bccda86-fbb6-3434-a2de-27ed1852ff4f | -11.17002 | -54.86315 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b05c870b-2eed-3d41-82c6-07b2a3a11f2f | -11.1584 | -54.89107 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f9ed873-9150-345e-87fd-2fafdea72cf7 | -11.29695 | -54.889 | 2025-10-08 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f2844cb-3fdd-3add-ad0b-a7de858e7794 | -5.90137 | -44.56642 | 2025-10-08 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7c62675-a773-3044-a765-819810bed3c2 | -7.729 | -42.39997 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9615026-7426-3f5f-9106-17e9ea88c75f | -11.69596 | -50.99652 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1bed22f-b083-305a-924e-3c1dddb3670d | -12.38872 | -51.14677 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bda51f7-269b-30aa-a933-39e45d03c25c | -3.43127 | -43.15062 | 2025-10-08 04:17:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd9f9ec7-20cf-3328-945f-3717ab110b69 | -11.14851 | -54.88694 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd8383ae-47a3-339d-83e0-81a3015ba725 | -13.28826 | -47.56923 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39475a0d-f2bb-315c-b1ec-2df5767e51f9 | -7.44307 | -43.12962 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a4b36f6b-cca2-3267-9974-c3449d712897 | -11.79224 | -45.14024 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e13aee1f-d3b7-3ff1-a0f0-08de7869b3a2 | -11.16092 | -54.87851 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a261c4fe-ff82-3453-b00c-9a051fb842af | -6.40465 | -44.71648 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fbf8da8-c44d-3c8d-87e2-5bda076852f0 | -5.25617 | -45.2756 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d68238c-624f-30e2-b5b7-bb0a9f99c24b | -7.52031 | -42.98095 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 85a642c1-5176-3865-804e-4c7fbaf2ab84 | -12.23385 | -43.78078 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2cee90ca-9807-35c1-af72-cabd7f48aec8 | -11.22495 | -47.76653 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ba6123f-8a42-3e72-9954-d118736add9b | -7.78332 | -42.40482 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ee553af-a19f-3417-974e-14468ecbd82b | -11.73816 | -50.95226 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 82c8f922-0dd6-37dc-9fdd-08ef0630f528 | -11.28457 | -49.98844 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60eeea77-3216-3afb-8b2b-adf7730097fb | -11.15672 | -54.87567 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5111927-efc2-34ed-a0a5-4bdbb942d2ab | -5.34386 | -45.86653 | 2025-10-08 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5ba67e0-7c6c-3402-858d-e24ba669822d | -11.72565 | -50.9453 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10b310a2-a955-3ae3-a563-731d179cc27e | -13.08373 | -47.99641 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d618b9ca-2198-3989-a597-2d092d031884 | -4.68753 | -45.83986 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 82978f0f-72ff-3d9e-832c-fdab56261944 | -13.01603 | -47.9136 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18c6ac1a-8c32-3176-a514-d65dae1f79f4 | -11.16013 | -54.88925 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c5fe355-7562-3391-8d4a-28ff04cf71ab | -11.9973 | -47.19464 | 2025-10-08 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 977e97df-a392-33a6-8e45-3602df106973 | -9.66856 | -49.95444 | 2025-10-08 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 992e81a1-da98-36fe-b598-3f8a58b93e5c | -13.07254 | -47.93275 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6af41e78-1451-31c6-9ab8-b3817c04fdd4 | -7.63256 | -43.06273 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14d409ea-c10d-340a-8470-ae9f54b4cf45 | -13.29345 | -47.17521 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6706e22d-0873-3ac6-be7e-d696d3e38dda | -6.63916 | -43.8013 | 2025-10-08 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90d33238-abb2-3e83-9a86-31542aa94b6f | -7.03003 | -42.87162 | 2025-10-08 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |


[Clique aqui para ver as próximas entradas](README36.md)
