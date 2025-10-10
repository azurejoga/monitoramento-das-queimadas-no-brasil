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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99f43074-5096-364d-9f10-1816bded1447 | -17.9376 | -45.0148 | 2025-10-10 04:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 104.9 |
| de2460b4-8ace-3f76-99a5-a59552b4f676 | -17.8832 | -57.4971 | 2025-10-10 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.4 |
| d0fbc7c4-5764-3bbb-9fcf-183a855b64be | -12.6492 | -45.0253 | 2025-10-10 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| fc90b735-2dad-35e3-9794-c6ee142a8626 | -17.9382 | -44.9909 | 2025-10-10 04:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ba10c9e4-645c-34bc-a4dd-dfdc0b27ddb7 | -12.6488 | -45.0486 | 2025-10-10 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| f1e71144-e278-3085-97f9-e5099aa02754 | -12.6102 | -45.0547 | 2025-10-10 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| bb1f97b5-c968-3ee9-9e4a-ecee31bce8f7 | -4.5515 | -46.6801 | 2025-10-10 04:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f26f8406-27d7-3f9e-a78e-fdaebe335fcc | -12.629 | -45.0749 | 2025-10-10 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| f917d94d-4f6c-3421-b0d8-8ba30a37baed | -17.9029 | -57.4947 | 2025-10-10 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.1 |
| a1040a17-e7af-3835-a9b6-c7b55b6fa3ef | -17.8832 | -57.4971 | 2025-10-10 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 6c7592f5-c9cc-3087-819a-603d7fd62bea | -8.5221 | -46.1301 | 2025-10-10 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 6db4fb2b-bd64-33a3-a83b-7ec358a6b20f | -17.9029 | -57.4947 | 2025-10-10 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.6 |
| dcfe3379-2cb5-3417-8e6b-5f21fba5789f | -17.8828 | -57.5177 | 2025-10-10 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.4 |
| bcfba365-3a9a-3db9-b0b7-e8be0713ad15 | -12.6294 | -45.0517 | 2025-10-10 04:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 56134d0b-1aa1-366f-bc69-0fef3cd9e3c4 | -12.6488 | -45.0486 | 2025-10-10 04:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 66160e4f-fcd9-3372-8a0f-af43f58a7b8e | -17.9026 | -57.5153 | 2025-10-10 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 50926854-3124-3d85-8f96-58e5b31d51e7 | -5.34066 | -45.56494 | 2025-10-10 04:49:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0383a00a-8730-3fcd-85f4-d36dfde4c89a | -5.71111 | -44.2188 | 2025-10-10 04:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9509960e-1faf-3df3-a720-e16f5e1762f4 | -3.46949 | -53.01817 | 2025-10-10 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e295b8d8-afb6-3b29-b8b6-c16234bc48f2 | -5.05257 | -45.8503 | 2025-10-10 04:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b50f5a5b-706c-327b-8e57-0edaa88c0733 | -3.84549 | -43.48756 | 2025-10-10 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efb38144-2c9a-379d-99db-3e23656d9538 | -5.483 | -43.07529 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 761daacf-a0a7-340c-83fa-65ce98c68855 | 2.05094 | -50.86099 | 2025-10-10 04:49:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6a3743f-c075-34a7-8478-4d880e853608 | -3.74694 | -44.38363 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e8aa2f61-2a94-3228-a1e5-782d947bcea6 | -2.90188 | -49.40012 | 2025-10-10 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58427e21-6741-3cbb-b657-f4210ce5be1c | -5.48939 | -43.06905 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 82ca2561-379c-38f8-9607-ce8873489a1c | 0.71195 | -51.37621 | 2025-10-10 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 965d3576-0d0a-39fe-b442-8c8468859a73 | -3.75221 | -44.38394 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a0b0d4be-675b-323f-bb74-3d90c786ea4d | -2.17202 | -54.47544 | 2025-10-10 04:49:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f60b3158-4139-3d67-bbcd-2de061080f49 | -3.00223 | -48.73913 | 2025-10-10 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d3196d0-88a8-3765-bfdf-9cb4c0a2bb98 | -5.05659 | -45.84943 | 2025-10-10 04:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec115c08-11a0-3dd7-9b34-b9e6e9f96f6c | -4.84431 | -42.926 | 2025-10-10 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce9b65f7-122e-386f-8fc5-5221dbf36c45 | -3.00348 | -48.73088 | 2025-10-10 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c53caa4d-2a84-34e9-8e2c-270f67f44278 | -3.07546 | -49.46517 | 2025-10-10 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b14d88d-5188-3a39-b80c-58b9c409a1ca | 1.64967 | -50.97359 | 2025-10-10 04:49:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30e67116-c493-394b-8c58-286e7379138f | -2.88836 | -50.73037 | 2025-10-10 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 444ef3e9-0eb3-3577-a1b9-4f01c81bb3fb | -2.68108 | -48.40821 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3728f13-83aa-308c-b3fa-a328554955a3 | -5.70569 | -44.2209 | 2025-10-10 04:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0d56654f-9696-3536-ad8e-6f52bf3692cc | -5.4776 | -43.07447 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 38bf3f43-84a3-3557-9359-d4e40b382de8 | -2.9474 | -49.33587 | 2025-10-10 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2b5cb1b6-8668-3f5b-b383-3b10e143d93d | -3.55239 | -51.44987 | 2025-10-10 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 746e7348-3f3e-38b6-b508-ba60bcd8a179 | -5.05596 | -45.8539 | 2025-10-10 04:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e248d474-b5f5-3e97-86f1-4dd4f8793eb8 | -2.67744 | -48.40765 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6490b54f-6e7c-3313-adb4-1a561dde0542 | -3.75251 | -44.37912 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7d68f1ac-dcb1-3af2-bb30-eff52f1a12d3 | -2.89748 | -48.06889 | 2025-10-10 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a679e348-7faa-329a-9e67-041a329bea8c | 1.73797 | -50.90669 | 2025-10-10 04:49:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a9f8834-81a9-384a-91b1-ba1a7d228409 | -2.88891 | -50.72686 | 2025-10-10 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b89270b-f586-38d7-9016-7e8d041c9d79 | -3.37509 | -51.58036 | 2025-10-10 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8492f5ee-341b-3b82-9b0d-07054beac575 | -3.3946 | -50.14454 | 2025-10-10 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1ce2f6d-a29a-3cef-923e-c4a1dc84429f | -3.06218 | -44.24352 | 2025-10-10 04:49:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdc286bc-d08b-3154-9267-439f6053b9ca | -4.8394 | -42.92159 | 2025-10-10 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fd71292-408a-3f61-ad42-11a6edbe02fb | -5.70611 | -44.21799 | 2025-10-10 04:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dae89922-59b8-3966-b48d-6592e11ff943 | -2.68734 | -48.39187 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e98553a-b7f5-34d3-881e-d02935542cd2 | -5.4889 | -43.07258 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bdad9ceb-41ec-3ee5-9ff1-3b48d6280744 | -4.55364 | -46.69359 | 2025-10-10 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cdb5b99-cf46-3881-b848-7619104167e8 | -3.47807 | -51.59639 | 2025-10-10 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9bf9e9a-5a63-33cc-a6f4-8c36bacbc786 | -3.06093 | -52.30338 | 2025-10-10 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c72aea8a-9f70-3043-9041-f0ac92a88f12 | -5.33612 | -45.56423 | 2025-10-10 04:49:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d36b0849-552e-349d-bf04-d22cf3a45df2 | -2.9468 | -49.33976 | 2025-10-10 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4e22e08b-e0be-3845-bf6c-c095d2fa93ca | -2.99864 | -48.73857 | 2025-10-10 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4381c4f5-22b7-3bb3-9b97-a31bf971d06e | -4.18499 | -46.23292 | 2025-10-10 04:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4aa62b17-b1af-3c35-9c4b-136d1fa85b5c | -1.40743 | -46.71084 | 2025-10-10 04:49:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d59aa57-c094-3fb9-a804-0a039d1bd567 | -2.1897 | -54.47821 | 2025-10-10 04:49:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 389b2958-4d1c-3912-ba31-1feed28aebc8 | -2.49273 | -47.5692 | 2025-10-10 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f0a13185-f00e-3590-8d85-58f9a520372e | -5.31246 | -45.40153 | 2025-10-10 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5d9f3b2-7a1a-3393-8e3a-e703d21e30e7 | -5.40692 | -40.98468 | 2025-10-10 04:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 18708548-2885-315f-91de-60d0c91af543 | -3.38584 | -51.66285 | 2025-10-10 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4adc198-9673-31f5-9e6d-2b6b826812f1 | -4.8448 | -42.92252 | 2025-10-10 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87439eeb-8120-3f6e-ac5a-fde753975066 | -5.40762 | -40.9863 | 2025-10-10 04:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 09f2b4a0-682f-3006-810b-848ed3eaf149 | -2.92174 | -48.30613 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fdd50d0a-0b17-3295-ad92-bbe249cbdb65 | -3.17458 | -51.25244 | 2025-10-10 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d89c8c5-c4b6-3a06-900b-685235c41a1e | 1.73468 | -50.9072 | 2025-10-10 04:49:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90d80af2-2cda-31f4-951d-ab7ab6c217bf | -2.94391 | -49.33532 | 2025-10-10 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a41733f7-2504-3299-ae9a-f9efd3d7b0d8 | -5.90794 | -42.85486 | 2025-10-10 04:49:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d1268ae2-cd0f-3c11-a89e-9008ef0281d0 | -3.75634 | -51.3825 | 2025-10-10 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 107e951b-45f0-3e30-8df5-d4b1d5f2aacd | -5.4943 | -43.07338 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 998b9147-96fe-3e93-85ad-731dceff58f3 | -2.18617 | -54.47765 | 2025-10-10 04:49:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18921c58-3d28-3229-b8f9-7f7ba968831f | -5.4125 | -40.99007 | 2025-10-10 04:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dcac753f-6139-3cfe-927b-009088aaa7be | -5.70582 | -44.22085 | 2025-10-10 04:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d498b978-3bcb-30aa-a25f-1249701754d3 | -4.9536 | -42.82151 | 2025-10-10 04:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 043504d8-6631-387e-b707-a250291bcccc | -4.65623 | -43.19913 | 2025-10-10 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddd64909-3f06-3ce9-a81a-119d623a2d26 | -5.33998 | -45.56969 | 2025-10-10 04:49:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad17fa73-65dd-36e8-809c-c6212cc98885 | -4.86389 | -42.7862 | 2025-10-10 04:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d88bc96d-323c-397c-a3e8-cb1d723dfb0b | -3.7474 | -44.3832 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f516d396-9ede-3387-b3a6-3a4c18d2d839 | -4.55002 | -46.68934 | 2025-10-10 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d08999e-7176-3749-9aff-cea9f97e9387 | -3.79758 | -51.14013 | 2025-10-10 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae82af08-e589-3758-8c2e-547e29b110f1 | -4.55834 | -46.69051 | 2025-10-10 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7e46dd6a-86b0-3543-b10e-a6401e4884e0 | -3.86141 | -52.30347 | 2025-10-10 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ddd7021-09cd-3f96-bba1-1e03d1c077c8 | -4.65576 | -43.20236 | 2025-10-10 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5b1ffbe0-4104-3858-bb72-08280c37c531 | -3.469 | -51.52459 | 2025-10-10 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c01a7a7d-d3e6-3b5e-8075-65f49f2d3eac | -2.64081 | -48.0401 | 2025-10-10 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9df7eff4-3a6c-3105-8834-20f128faccaa | -4.55473 | -46.68624 | 2025-10-10 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 50ef2bb6-fc72-3e7c-afd6-1b17af994f0b | -5.54553 | -45.37702 | 2025-10-10 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f3f93e4-5041-355c-9290-ea382ab445cc | -5.58764 | -42.80842 | 2025-10-10 04:49:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd220453-e649-313e-aa2a-7d92a93e5875 | -5.70622 | -44.21793 | 2025-10-10 04:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d34eb189-b8b3-3b9c-90e5-935c8b114923 | -3.7558 | -51.38596 | 2025-10-10 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96f6a95d-0d29-3542-a1fa-1386bd889605 | -2.492 | -47.57392 | 2025-10-10 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c05fa636-1b66-36bd-9d43-a75bbcae005d | -2.55093 | -48.40296 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65122e6f-3579-378e-b9b6-587c65b91434 | -2.68042 | -48.41246 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 045d8d17-5934-36a6-9434-f55b93453c31 | 0.71525 | -51.37569 | 2025-10-10 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README34.md)
