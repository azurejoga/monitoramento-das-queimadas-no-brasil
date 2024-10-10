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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2c916c1-19f4-3123-b377-48b992b3d71f | -7.22704 | -42.30281 | 2024-10-10 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 473213d1-8f8a-3c33-b0a8-6189ee89e517 | -7.2268 | -42.29976 | 2024-10-10 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 38ad3820-fe2c-3b73-8b79-bc3beb7ecffe | -7.22621 | -42.30362 | 2024-10-10 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| aea1dc7a-16e3-3384-a464-2bba6d4984fb | -7.2245 | -42.29145 | 2024-10-10 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e51e9bd7-9b65-3b32-bf86-4a5c9ae05f50 | -7.22389 | -42.29537 | 2024-10-10 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 76294ad3-2702-39c1-825c-d110a6cd86f8 | -7.2233 | -42.29923 | 2024-10-10 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 61e988e2-09a5-3259-999c-59f3824110c8 | -7.22271 | -42.30309 | 2024-10-10 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a2b89d35-375c-3380-b69b-67b91e63a1c2 | -7.16096 | -42.61148 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 784cc7c3-3a38-339e-b5c4-fe1dd5f84002 | -7.15922 | -42.62281 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1567c334-ad53-37c8-a943-568e5d9986a8 | -7.15809 | -42.60715 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 68fbeef4-0330-390f-8df2-39cb1d77eec3 | -7.15576 | -42.62228 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 77c29e59-2836-375b-a77d-f5510e07da7d | -7.1297 | -42.83698 | 2024-10-10 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 732e6738-c903-3e87-b4ec-a606d5f44f97 | -7.12695 | -42.64873 | 2024-10-10 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66644a8a-6014-3826-acfb-6fc48ff0991e | -7.12349 | -42.6482 | 2024-10-10 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 655c4951-1193-3445-85f1-06349e2c31cb | -7.11544 | -42.60828 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7ede2889-9704-361c-94eb-da0a039de18d | -7.10845 | -42.2748 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f715901-f461-3e3c-b12f-87dcc1b7ee65 | -7.10785 | -42.27871 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e6fd923-3271-3b02-98e3-af57851e75f2 | -7.10435 | -42.27816 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e2b0f23-9b53-35ec-a5ba-66202a0576c8 | -7.09239 | -42.62027 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d38c7015-bba3-3b1c-b1de-11265b20b3a2 | -7.09182 | -42.62406 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8f2a9c29-0a40-3a15-a33f-5db9ac344f40 | -7.09125 | -42.62785 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4dc8297b-8e75-3d47-9db1-c1f3e4df3f84 | -7.08837 | -42.62352 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0495cd6a-ee2c-3b36-bcd9-19da5cabda4d | -7.02032 | -42.52477 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d2bc849-b8e7-3203-ac76-ed801b74c7dc | -7.01974 | -42.52858 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c93c1c89-a8b7-38c5-8de0-1f2a3d107338 | -7.01916 | -42.53239 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9c6d90e1-9086-3361-88d2-2664aff8db80 | -6.80485 | -42.75092 | 2024-10-10 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c51e79c1-2af7-34c7-9eaf-64b549e396bd | -6.80141 | -42.75041 | 2024-10-10 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c6d6ec51-22ce-31a7-97dd-5096717eb460 | -6.7002 | -43.18109 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6edd5766-146f-34b2-82bc-78c624cb6d33 | -6.69965 | -43.18471 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 73de9c5e-24f1-3d5f-8d21-ec2f5b4d92fd | -6.69626 | -43.18419 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6ecb2650-40c5-36cc-9928-bb10c0f55cf3 | -6.66844 | -42.09184 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3f09448-ff3d-3bce-bac2-ba44afbd2fd5 | -6.6649 | -42.09142 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c3e8363-c2fb-3c2f-aea0-83b9ed51830d | -6.6643 | -42.09542 | 2024-10-10 04:17:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 88342c3d-3c39-38cd-84fe-c5e2cf1ec49b | -6.64716 | -43.34605 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 07fd7d16-1602-3b28-9ae0-1614a542ddcf | -6.63779 | -42.199 | 2024-10-10 04:17:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 616bb90d-77d2-3277-82a9-cb7a1eca5b75 | -6.63429 | -42.19847 | 2024-10-10 04:17:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0780271d-cdf3-3b16-8589-2a4cbfd570df | -6.6337 | -42.20235 | 2024-10-10 04:17:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e8bf8678-4f84-3fef-90e6-15bbd13ab9ba | -3.46089 | -44.27835 | 2024-10-10 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b38c12a-5d59-3e41-9c83-b30a5bd2d141 | -3.46035 | -44.28182 | 2024-10-10 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9edf612b-8ddd-3d72-9492-0aa6d894d5ce | -3.45817 | -44.27796 | 2024-10-10 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4525e54d-7b8d-30c4-85e3-5fcd58de0bfe | -3.22698 | -44.28461 | 2024-10-10 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 865b1d36-c565-36f5-aba5-a9308581fa29 | -4.84806 | -43.35167 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b991d290-a672-3d0d-835e-a561b29f14e0 | -4.84472 | -43.35115 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96c45743-be69-37b9-8ed3-26e443a1da94 | -4.81977 | -44.35371 | 2024-10-10 04:17:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f368ca44-c093-3b7c-8a68-097aa821c214 | -4.29398 | -44.38438 | 2024-10-10 04:17:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44658c3c-0667-3605-8310-613b575f03c3 | -4.2924 | -44.41607 | 2024-10-10 04:17:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edd3f534-f189-3c39-80b2-ec0352a4f330 | -4.29066 | -44.38386 | 2024-10-10 04:17:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e91ef4ac-1bc8-38f7-981b-3861c337dd62 | -4.28907 | -44.41555 | 2024-10-10 04:17:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb0fff42-97c1-3f5f-9792-37f5edf79c77 | -4.28347 | -44.38628 | 2024-10-10 04:17:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efaa526f-e73e-3f7e-876a-7095b449b361 | -4.28128 | -44.40013 | 2024-10-10 04:17:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 074aa4f8-8642-3c71-acf8-dd6782c97a6c | -4.28074 | -44.4036 | 2024-10-10 04:17:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58dacb5f-bbe1-3453-8809-8d4db953e055 | -4.04586 | -44.26015 | 2024-10-10 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 843fffae-3727-3d1a-8761-df6f8d307ebf | -4.04531 | -44.2636 | 2024-10-10 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00f678fa-e1cb-3049-95bc-2b2e3488bafc | -3.55651 | -44.37834 | 2024-10-10 04:17:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc76a9d0-ad59-307e-935f-32721943515d | -3.95227 | -44.34129 | 2024-10-10 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2965a278-520f-325c-867f-29a950bac3f6 | -3.88403 | -44.10741 | 2024-10-10 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c8d08c9-12fc-381c-9b73-2a92218bb0b2 | -3.78828 | -44.36887 | 2024-10-10 04:17:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2a48a2e-5c10-393a-aee3-49c1e99e61b4 | -5.73671 | -44.02948 | 2024-10-10 04:17:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46281c04-ed38-3dc0-8bf0-a852160afc5c | -5.70496 | -44.78787 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a73140c-c0be-33fc-9c15-82dc7d8ea2bf | -5.70109 | -44.79082 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4571f2bb-ac1c-3a70-bec0-a94653497976 | -6.50663 | -44.33874 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f83b1e8-0434-3156-8975-b25209493e93 | -6.50609 | -44.3422 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8172a050-e383-3f2c-8676-13fb0db3a6c4 | -6.50353 | -44.16689 | 2024-10-10 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 284e06ee-d596-326d-b6ee-9e4b55337979 | -6.50239 | -44.15246 | 2024-10-10 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 941f267f-8887-33a3-a61d-87dda1329c1c | -6.50106 | -44.0523 | 2024-10-10 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67c11c1c-12b9-3e14-9306-172fd351218e | -6.4688 | -44.01864 | 2024-10-10 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83f0b222-5164-33b5-a7c6-ef8f0b703885 | -6.45256 | -44.16602 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8213b0e-f81c-36a5-ad94-d42dad8b5041 | -6.45196 | -44.14811 | 2024-10-10 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 365f351f-cd74-37bb-ab1b-e76bb977b74d | -6.44451 | -44.26088 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d8ec83d-7176-38ee-b38e-597c10ab65a5 | -6.44396 | -44.26435 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51657ec1-639c-3e6d-9497-a261aaf34812 | -6.44118 | -44.26036 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f44517c9-8491-39af-9949-ba31d45e9503 | -6.44064 | -44.26383 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0f8046a-55f5-3d00-b9b4-4c5336e62733 | -6.4401 | -44.26729 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac99fb98-2004-3447-b74e-75cfb0c26880 | -6.43786 | -44.25984 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f7efa07-80c0-39e2-872e-af9599f3848c | -6.43732 | -44.26331 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a74d4b0-c8e9-31e7-9ce4-ca897e4b4e15 | -6.43678 | -44.26677 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45e05a40-3210-3f74-a589-2049573b677a | -6.42393 | -44.43536 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c94205d-8957-34f6-89bb-cc3bb43648a4 | -6.42115 | -44.43137 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9d16d70-7cce-3f9c-bcc4-9971317f83ec | -5.58348 | -44.87233 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9de61c95-86a6-3158-841f-1764179c5caf | -5.58293 | -44.87581 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c67e0f8-a104-36ff-919b-0987f0c53df8 | -5.5796 | -44.87528 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1caadd87-4d12-38b9-a6c8-b3bdae24decb | -5.49404 | -44.28224 | 2024-10-10 04:17:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d5b155c-016f-3a69-9da8-5c2aa6a59e07 | -5.49295 | -44.28916 | 2024-10-10 04:17:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b69b3ad-410a-397c-8da7-21969f5e98a2 | -5.49093 | -44.53402 | 2024-10-10 04:17:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f6b4908-2666-3599-9aed-45684d53c9ef | -5.49072 | -44.28172 | 2024-10-10 04:17:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| feb88b3e-432f-38ed-8536-559212ec93b1 | -5.49018 | -44.28518 | 2024-10-10 04:17:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5f31630-b443-3396-b08c-a3971620a4cc | -5.48963 | -44.28864 | 2024-10-10 04:17:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e25f6b43-144d-3810-a401-10bf8d81fa7b | -5.48761 | -44.53349 | 2024-10-10 04:17:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd39d09d-bbdf-3e93-80ca-495eeb399e38 | -5.48353 | -44.28414 | 2024-10-10 04:17:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a8b8010-bceb-3e4d-b51b-458b4944ef50 | -5.48299 | -44.2876 | 2024-10-10 04:17:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a7e36f2-f4e8-3a66-bfa8-74933b6a3a9d | -5.48144 | -44.85272 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b42e81a6-9f9d-321b-9910-09d006cb475f | -5.48021 | -44.28362 | 2024-10-10 04:17:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f08db4d0-31b8-3d89-a9ff-2b92c85b3485 | -5.47811 | -44.85219 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8903ebe8-6830-35ef-b960-05e11911694d | -5.47689 | -44.2831 | 2024-10-10 04:17:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 674f53a3-dedc-3e4c-91ed-3a15799d4d3f | -5.33001 | -44.84636 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7000134c-2e47-367b-aa49-2314fe03932b | -5.32668 | -44.84583 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f77daeb8-0c4f-36e3-a8ff-794b5383a42d | -5.2726 | -44.20536 | 2024-10-10 04:17:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dba9ab72-b2ac-3169-b9ae-55a316b29c79 | -5.27206 | -44.20882 | 2024-10-10 04:17:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19df5ba4-0c42-3ca2-a855-d80e66478670 | -5.26928 | -44.20484 | 2024-10-10 04:17:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a0f2539-d604-35e8-a1bc-c151ea75b5ab | -5.24301 | -44.79712 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README59.md)
