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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b81575f-ca6f-3260-826c-df22f8f066f6 | -7.9227 | -44.09652 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| afc9fae3-7bf6-354e-8317-0d73505829cf | -7.88734 | -45.54598 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c588ed48-fecf-3cbc-bdbb-9afe1e503224 | -6.88178 | -45.24904 | 2025-07-25 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1fd5318-7583-37a0-afe4-7e0996076122 | -4.66845 | -48.87098 | 2025-07-25 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 365e1e52-69a3-38aa-9ad8-1e0fedcf32b0 | -4.35108 | -47.693 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 330f2c5f-7bb2-3bdf-b0cb-4a20222dc6d7 | -8.84379 | -45.60258 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ed32744-b0f3-3bde-bc9e-38c55708d9ca | -9.65489 | -40.59642 | 2025-07-25 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b6c87396-4399-399b-b849-b9e9b9be2daa | -7.63151 | -44.27774 | 2025-07-25 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4b09506-d444-3723-a7bc-52fa2f11ec92 | -5.03406 | -45.12085 | 2025-07-25 04:21:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f04c1aec-6364-3391-a517-4d80adf8cf16 | -8.21021 | -44.94074 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b39b5eb-7b28-3157-92fc-c9403343a3e9 | -11.44975 | -45.12101 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e04a5eb-9c56-35cd-9fec-697aefe3ce04 | -6.22939 | -44.52789 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7cbb2d8-e04d-378b-823b-624d27baf9a7 | -6.40716 | -53.33327 | 2025-07-25 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd1dee17-3ce4-3176-a9fa-82d778fd4e20 | -7.9238 | -44.08945 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 036aa891-6c7c-3dc7-ad4b-4fa8498897ae | -7.49932 | -49.22052 | 2025-07-25 04:21:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5af0b09-500a-3548-acbd-90726c256d1f | -8.11931 | -50.46352 | 2025-07-25 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab3bbaf7-0486-39b3-a43f-7d9cefdcf6e9 | -8.12758 | -50.46498 | 2025-07-25 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1751b04f-8e8b-3a91-810f-54a2a590d64e | -4.83921 | -45.30643 | 2025-07-25 04:21:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4a572115-7db6-30aa-afa5-89f788f9de37 | -9.42616 | -40.34707 | 2025-07-25 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 644b19e0-0592-3b42-b38b-169346c2e6f6 | -5.2304 | -46.09254 | 2025-07-25 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33216610-25c5-3d59-8ca5-44ea9f57028e | -8.21131 | -44.93378 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8fc8822-4f21-395b-8d2f-7f7e6627f5c4 | -6.87584 | -43.10107 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99e630b2-ce64-3820-93c9-5d1c6ec86fc8 | -7.14457 | -46.09465 | 2025-07-25 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24880770-d2be-3d27-93c6-d7cbdd547fc9 | -5.42748 | -47.14685 | 2025-07-25 04:21:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2f8d990-e39a-3237-ba35-24dc609e06f6 | -7.91657 | -44.09194 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 991139bf-5e5a-3849-ad4d-2d61eb5781ec | -7.90933 | -44.09443 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b158ca8d-4d09-38a7-b8cb-2b415413e2ec | -7.92101 | -44.08539 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 68a7c8a7-de8f-3f30-9c2d-1441a651e6b0 | -11.46697 | -45.12011 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a8d979ea-9379-3cab-b8d7-47f34a2b996c | -7.91377 | -44.08788 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a41c91da-e11a-3efe-8be9-57415e7a6738 | -8.84434 | -45.59908 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4239095-4fdc-307c-bffc-c00af7d470ea | -5.57554 | -45.74934 | 2025-07-25 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33f4b680-68a9-3355-9dd5-b4d381757a57 | -7.8828 | -45.53831 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c2c765c-9f52-333a-a91c-857a799c338b | -10.50394 | -44.87664 | 2025-07-25 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e4e672eb-8832-3cff-b69d-5f3479cbd3b0 | -7.35566 | -43.43082 | 2025-07-25 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca0ba462-ce78-3701-a796-cf4859883a8a | -6.64041 | -43.96825 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b87dda32-c7ca-38d0-b7ce-08c9ed719f43 | -11.0525 | -44.78163 | 2025-07-25 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ff6bb56-79a0-32cf-ad74-dd79f50b15cd | -9.58942 | -46.34108 | 2025-07-25 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c4664a1-990a-3f1a-96ba-674d5a341036 | -6.99107 | -43.32384 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50fd362f-6473-3c08-899c-79b9fc373704 | -8.20744 | -44.93673 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 606a8e42-26bc-3867-b2d3-cf820fb5f311 | -7.53656 | -42.42701 | 2025-07-25 04:21:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 006c0987-b15a-3120-a6e8-a97f8c4c2c0a | -5.4885 | -42.14999 | 2025-07-25 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3163480b-70ab-3825-a6e6-4f13f73c9fb5 | -8.86045 | -45.60165 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83ddc99e-559e-35be-86d8-a40f468449cb | -11.45199 | -45.12864 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 15afb936-8939-3635-abbb-1f7fd5e0758d | -10.61027 | -45.23705 | 2025-07-25 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 50579f4e-1042-397b-bfe9-9aaac545f4d0 | -6.94965 | -44.56633 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 48b3d682-2023-320a-a420-8cd0b9a7e643 | -8.82186 | -44.51495 | 2025-07-25 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7510b6bc-39d4-36ae-8750-d2e29b6be010 | -10.62237 | -44.76505 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1fad2562-6e02-3038-8a42-f97d98ce83ba | -8.85545 | -45.61163 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bad89ac-572d-34e9-936f-c108e0a00b65 | -11.4492 | -45.12456 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a5d63b02-b66c-37b0-9c21-e30d89e27918 | -7.88336 | -45.53482 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16c96725-7104-3224-b501-7df9c9cdd48c | -6.89301 | -42.83237 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c5b1e684-9fc9-37bb-aa51-e38bd956c6ce | -6.65285 | -43.05679 | 2025-07-25 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95ac430f-feac-3c10-93a7-f2ea3d623355 | -4.03518 | -48.06756 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf52632d-9573-3f1a-8ebe-2d3f04bb1ef6 | -9.05954 | -46.61926 | 2025-07-25 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01c97b86-fc15-3519-bc85-04f00930423b | -7.91547 | -44.09901 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fc252fe-5fa9-3b66-99b1-2d3f5397999e | -8.36697 | -51.0793 | 2025-07-25 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2dabdcfa-8ce3-3f67-be7b-ae97a70e7602 | -9.6596 | -40.59187 | 2025-07-25 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 549862b2-3b1c-306f-9990-cd3fd4e076c0 | -8.33104 | -44.94914 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 977923a7-2750-31aa-8c7c-7038f523d4bb | -6.53239 | -43.51893 | 2025-07-25 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bd02372-f832-34ea-a0df-619a76add4c1 | -8.36894 | -51.08059 | 2025-07-25 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db5da25e-fcac-35c3-b061-cf7465ab0f1c | -7.8453 | -44.20736 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69a02bcb-9dfa-3446-9528-3219e03ed949 | -6.88466 | -44.2034 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53d74171-9a91-3406-8130-64c5c11cee9a | -6.97217 | -44.82912 | 2025-07-25 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cc92222-bc27-31f2-a177-eda41752599d | -7.14513 | -46.09108 | 2025-07-25 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abaeb73f-b993-3137-a659-de48bd10d3e6 | -6.9001 | -44.14859 | 2025-07-25 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c077cd9-10dd-3aa9-8196-b727a2c3cd07 | -8.12283 | -50.46789 | 2025-07-25 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f0e66df-e131-3957-aa1c-a314d7c5135c | -5.66568 | -51.3619 | 2025-07-25 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4191efd5-ace0-3ef4-b5be-4002514c6c1d | -8.07806 | -43.15449 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 114da242-ec65-393c-9cf4-78ed7bef8f4a | -8.0721 | -49.71681 | 2025-07-25 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a39ae7a6-361b-313f-95f6-25756bb84967 | -8.89533 | -45.59653 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4d10b35-d12c-33a0-b74a-1b219470271d | -8.76267 | -39.64334 | 2025-07-25 04:21:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c2c2ef8-085d-3493-8310-7bf0ef283ac8 | -7.91602 | -44.09547 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 20c75ace-6b81-36f1-a3fa-8e2370895f1d | -7.25803 | -43.06487 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 7f6ffc85-424c-387e-ba35-4fb02e9ad290 | -6.69289 | -44.41185 | 2025-07-25 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d16ef88-62ed-3b3c-a30d-06b4c5c84640 | -6.67818 | -43.96696 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6991fabc-a714-3b5b-ad8d-f2d2d5b7fb57 | -6.82451 | -43.98601 | 2025-07-25 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c30e4202-3e51-33d4-9842-cd107137d536 | -7.24778 | -43.06329 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| ac3b76ad-0f69-3406-892f-1913fa99c9f8 | -9.37319 | -48.01525 | 2025-07-25 04:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fb1d0fe-7167-3485-aad2-45db00b0ae07 | -7.92156 | -44.08185 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c25751c-2827-3159-bf10-974df4ed8f44 | -7.10451 | -43.55833 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29d82a2d-ee05-3516-b4d8-7fd60d33bac1 | -7.88225 | -45.5418 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 736165e1-7993-3566-b6ed-10694bc101c7 | -8.89589 | -45.59303 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f44cc28-c30e-35e2-9d90-a17868a443a2 | -10.42419 | -47.19363 | 2025-07-25 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38abec1f-4d69-3e07-8136-8b11adbba65d | -7.89122 | -45.54302 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68bc8016-d7e7-349d-bb03-dc8786d0b446 | -6.98768 | -43.32331 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02f62c8c-7718-3e03-830a-eb4ee61a8799 | -5.5303 | -38.2621 | 2025-07-25 04:21:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0802135f-a760-37d6-a5b1-7035eede01be | -8.33713 | -44.95363 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35a93767-38a0-36b0-abf5-898fd7420966 | -7.92325 | -44.09298 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 024eae17-89d0-3d77-8269-29a0b4945493 | -9.34958 | -40.53053 | 2025-07-25 04:21:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c524166-f582-33f4-bfe8-3e387a607f16 | -5.83633 | -46.15929 | 2025-07-25 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c63c4dd-cb51-3804-ae80-192804263acf | -9.85769 | -44.70278 | 2025-07-25 04:21:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac58efc3-9e4c-35bd-b806-ee82781dab72 | -9.60059 | -43.87466 | 2025-07-25 04:21:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7be4bcec-ae49-3a13-bee8-0c1b499243f8 | -8.13445 | -49.58854 | 2025-07-25 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64fb6c38-8747-318d-ba7b-42e80fd0b37a | -5.53041 | -38.26024 | 2025-07-25 04:21:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2d10b809-db0f-3f8d-ad7e-bb97710fb29c | -7.85935 | -48.22266 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfdd13b0-0acc-3082-b881-92632ed53dd7 | -10.61415 | -45.23407 | 2025-07-25 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 952e8248-11e2-3b72-89b2-1cc16a9b3ed2 | -7.91153 | -44.08028 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ba6e307-d328-3911-8c5a-eb82de56dc4a | -10.74618 | -48.18589 | 2025-07-25 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f29100d5-df35-309e-95f0-6f10103b8a30 | -7.86732 | -48.21959 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38fdc7bf-47ce-3e43-ad2f-d53c7aa0e088 | -13.70752 | -45.67812 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README17.md)
