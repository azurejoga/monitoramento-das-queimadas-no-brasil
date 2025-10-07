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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 910194e7-e227-3ad3-a218-0de67a76fe52 | -6.28325 | -42.92173 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e550fee-b68e-3f37-8880-f9e5590deddd | -8.18212 | -50.30722 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f2f3f91b-7293-3057-9cdc-c8a160935580 | -10.43504 | -50.40004 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32916a20-452f-3c65-b278-92f74d9fba94 | -6.29869 | -46.09086 | 2025-10-07 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d017899-a62f-35b2-b704-5f96e33b0a3e | -10.39268 | -45.38326 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8848e72c-1524-3324-be50-391089cd4a3b | -11.7865 | -45.0999 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc469bc6-a822-3798-b5d6-b81c7558927f | -7.02501 | -42.79941 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 283224c9-7a25-3db8-a43b-0d60a0d5e7ab | -10.25779 | -44.36267 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49c4e157-63e2-32a9-9c1d-ba6b42606696 | -5.70837 | -44.83647 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cbf4901-628c-329c-a33c-bb2049618e11 | -9.27958 | -48.32256 | 2025-10-07 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8615cfb3-3b42-30ae-b957-5061e0c25bcf | -11.83765 | -44.91475 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0169a0d-ce8b-3b0f-94d7-fe3fe055ec78 | -10.3891 | -45.38286 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b192060-6311-3393-a40a-c20eb08b2477 | -8.61106 | -44.90976 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8483930b-1ebe-3fe4-a40e-305917f34807 | -8.87962 | -47.66681 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6136f665-66ee-3394-bcb6-5bac061e71d8 | -5.49517 | -43.07905 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 41c11d3b-6d17-3768-a9a3-29724791fdc4 | -6.98431 | -42.86189 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 835c57a7-0102-3c01-a2fd-df536586db0d | -8.26061 | -47.0069 | 2025-10-07 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c919129b-21bd-3c50-94ac-84e43816c3c3 | -8.18711 | -50.30818 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0ce221dd-5122-3cf6-9f3c-077a5c77fca7 | -6.24152 | -43.26768 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 852832bb-f309-362d-801f-b7490f9a9d47 | -7.02059 | -42.78419 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 672c31d3-2d17-308b-99bb-e264d431930d | -6.70263 | -42.18859 | 2025-10-07 04:08:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 847dd161-a2cb-32d5-9d87-89fcb569ae57 | -6.64952 | -39.29623 | 2025-10-07 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fa27aee0-ff8e-3310-87ee-3a608d7832d8 | -7.43647 | -41.13283 | 2025-10-07 04:08:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2550b4c6-0f7a-3603-a03f-6e6949171895 | -6.59551 | -44.62237 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99ef28fa-db4e-3ead-8ea5-6b53d5d91331 | -6.71559 | -42.84078 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ccc318ec-5dd5-3ab6-b048-dc4b5815b627 | -12.21223 | -44.25598 | 2025-10-07 04:08:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa0b43b3-007a-349f-ad22-eb9a947266d0 | -6.45559 | -44.58821 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0b6360a-581b-3e56-8456-900e50fee971 | -5.23922 | -46.56416 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04c27ba6-ac6a-361f-9ccd-5f689303ed81 | -8.85452 | -46.09171 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d74ca0c2-ec18-396a-bd06-5bf0e4cc2ba9 | -4.68868 | -45.83558 | 2025-10-07 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 6b4c877b-dd49-3ecb-b147-3239622972c1 | -11.74636 | -43.29378 | 2025-10-07 04:08:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 50023d8f-30d8-3a04-b2c8-d2d770cda16c | -10.7319 | -49.29553 | 2025-10-07 04:08:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecd70d4b-1697-3f48-a7d8-b078827c48f7 | -5.25875 | -43.15062 | 2025-10-07 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49ecba37-f853-3969-870c-ae35e4754c35 | -10.42457 | -50.32774 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 095b411a-46be-3ee7-80dc-f27489d719fc | -10.12744 | -52.34704 | 2025-10-07 04:08:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 741baa3e-af18-359c-806b-5898964a0dbd | -5.7764 | -46.15247 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52d248c9-d2a6-3b57-865a-eba2592c32ac | -6.28375 | -42.9401 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39fdab9d-9cb3-3158-ad39-969e7f0cb55b | -6.65127 | -39.30812 | 2025-10-07 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c475cee4-1494-363d-ba85-1cda74fa2867 | -7.46888 | -42.61853 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3d947e26-1a57-3b19-8ffb-be7a663f5115 | -11.8472 | -45.07049 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bdfcee4-03ec-34cf-86c2-138533bb71e3 | -10.65119 | -47.78776 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 248f8c90-13a9-3948-84a4-8eefdfc0e59d | -9.96549 | -43.78317 | 2025-10-07 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fbe46c69-61cd-385d-b59d-303d681befc6 | -6.08159 | -42.54401 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4de846e5-5999-399a-8d3c-5ec33f93808e | -11.84793 | -44.9165 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e856fcbd-fa11-3e33-a423-e0777f196c11 | -8.41221 | -50.69599 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a40e6bea-55bf-3aa2-b9ba-69b595f1bae9 | -8.494 | -46.31637 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 168c9ab4-5f97-31d7-b8ab-068d7ed997e5 | -5.3035 | -44.55494 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e79cc91f-5eda-3d91-87b0-4cf82a68a645 | -10.87999 | -51.03227 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| eeea8857-c746-33e0-a9b6-7492fe0ad245 | -8.54484 | -46.24648 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4c14b1f5-0359-3be0-a47f-38e8858f03db | -11.05107 | -50.9191 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 677adfd9-735a-341f-b1ce-de068bf470c3 | -7.73651 | -42.38947 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| baa90733-b725-323a-9d2a-b4581aed8f96 | -4.70875 | -46.46252 | 2025-10-07 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e7ff294-5951-3132-8b3f-e93d4386eaca | -8.56346 | -50.08326 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35941f90-7002-3857-97ec-1e6a24fe9031 | -5.26146 | -46.48194 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1da95ec2-c575-30e1-8b3c-c281ed8ab6bd | -8.49048 | -46.26717 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1276ef08-e2fa-3cf2-9b3b-c7a99ad1bd1d | -5.50429 | -43.0655 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 23a7f593-0c61-3c66-9253-bcb574aa0b23 | -10.74811 | -50.47792 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4d9f8fea-3a64-3a04-880a-a8b8a963f6c0 | -5.4599 | -42.79193 | 2025-10-07 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 53228687-3071-3971-b320-508e58e9dbac | -12.61329 | -44.74932 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0de1d6ce-fa92-3c45-9bbe-f3054a48719b | -12.86189 | -42.62616 | 2025-10-07 04:08:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e3328585-f1ee-391f-904b-88faaddaaaa6 | -12.61208 | -44.75677 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13289278-4b7c-3e62-817f-4d35a1c22e45 | -6.65224 | -41.97142 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 822416e1-6bf8-305b-93fa-c7e16884e71f | -7.89288 | -47.81 | 2025-10-07 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d256f63d-9bff-372c-bb93-bed4c0e272dc | -10.74693 | -50.47558 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0096e44a-16e5-3457-8cda-db82dab301ec | -10.2612 | -44.36323 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3dd2ea1-13d2-3d91-8d7f-ee16cc6f30c9 | -5.73951 | -49.13577 | 2025-10-07 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a2d0a768-8d31-3b68-8c53-f79cfcdb181a | -8.67936 | -49.94019 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3257c70e-8135-37b7-a4c5-ca06d4329135 | -10.22608 | -48.18277 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c20f64d-b3c6-35f5-80c2-2795a49dc535 | -10.92092 | -47.06834 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 619121ff-b9b5-30a4-b14f-a3829486d500 | -12.24241 | -47.01809 | 2025-10-07 04:08:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 512fbd4b-2d59-375a-b3f6-9e132b374a52 | -12.44512 | -44.2271 | 2025-10-07 04:08:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79938f3e-f090-36aa-b286-5d9a50b06335 | -11.79278 | -45.10495 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8265153b-a1fa-312c-9367-321e89140f65 | -10.02686 | -48.30118 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20bf413c-6629-3a9d-8d78-7c7f58941b43 | -11.84733 | -44.92014 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dff369e8-b08d-3a60-a245-c5b94311831f | -10.23022 | -48.1838 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7123f069-b1d2-3245-8fe2-568fe9e3cba3 | -10.74425 | -50.47158 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 209d8c50-10ec-3df0-91a1-8988f0dca47a | -8.52559 | -46.26817 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4578258c-249f-31b8-a5b4-1edaa1b332f4 | -9.09455 | -44.40287 | 2025-10-07 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e068f15-b3ab-3e4a-b3a1-24f1bb39a832 | -8.96876 | -50.8042 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2806c404-132a-32bc-8bd4-2554cf8820ec | -10.81377 | -48.60306 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da32a46e-d55c-3503-9fa5-094743a1045d | -7.46416 | -43.09589 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ce70bd1d-8ee4-36a6-bb57-05ff6580287f | -11.60848 | -43.11242 | 2025-10-07 04:08:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8e064fd4-9c13-31f0-998d-038ddf852adb | -9.65759 | -43.83694 | 2025-10-07 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1895f270-f5cd-3e2d-aea1-e01b86e23957 | -6.27989 | -42.92122 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35fd59d6-697b-3432-80a9-4e392da7e7a8 | -5.49296 | -43.07119 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 682764c3-224d-34f1-884c-3fc962b6a668 | -8.56246 | -50.08879 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 545f7a4d-ad34-35ae-b425-aa36cee61f5d | -12.68036 | -44.38941 | 2025-10-07 04:08:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03f7d1f6-faed-389a-b22e-ad6c6e58cbeb | -6.2984 | -46.0884 | 2025-10-07 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b591d8a5-c8bd-30ae-bcd1-1985652c7e61 | -8.65818 | -46.28578 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9973c7ea-8a81-31ff-8dce-2af890f57660 | -5.50371 | -43.06915 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 7b911512-e65c-335d-b3c4-9b1ce8dff6e1 | -5.48385 | -43.25788 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d37b2987-c48b-3777-98d7-1166ec30d643 | -6.24328 | -43.25673 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9181a36-d4b2-347f-b627-2dabb7c2e5fa | -8.17498 | -43.33439 | 2025-10-07 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 687704ca-bd10-3312-8f8a-4afff87506a0 | -10.61326 | -48.68185 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be85c500-ebfe-3ce9-93f4-538815a0d387 | -11.71848 | -44.44136 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d8086df-9610-3166-89bc-1164e3393153 | -10.23366 | -48.18879 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c1e1c36-2ada-3aec-bffa-0c6e57e4ebe7 | -8.53246 | -54.85935 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1060c7f-00fd-3e35-bfd4-fb09ff508c69 | -8.66281 | -46.28159 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| acb6d4e2-8e38-3859-b01c-46f0aa6a38af | -8.2896 | -44.8102 | 2025-10-07 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f65ebf3c-1156-3863-94a1-17906a93ada4 | -6.65332 | -41.96453 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README27.md)
