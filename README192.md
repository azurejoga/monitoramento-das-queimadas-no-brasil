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

## Dados Diários - Página 192

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a11d8989-bf6d-38c5-9ad4-4d9596244dd1 | -8.72905 | -47.06805 | 2026-10-07 16:37:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9778c9e1-b463-328a-9145-6b7b603a9a98 | -9.91198 | -44.80127 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 45f30163-c6f8-3d77-97d0-7a22da3a09df | -4.52666 | -43.72523 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 135b69b8-06fd-39cc-b021-6a9e2e3e4094 | -8.53786 | -47.53268 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 37dae757-27cd-3fb9-b8d4-e41cff3582bc | -3.228 | -40.0256 | 2026-10-07 16:37:00 | NPP-375 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 588d8bcc-b46c-367a-bce7-b0de423e64f4 | -3.88602 | -44.10611 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e2c8c57-83ec-3f54-8d6e-a40d0b492cc1 | -5.71581 | -41.67196 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| af8a519d-9189-3d68-9183-80f63796c1cf | -5.89277 | -51.54444 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b71ae821-263e-32c6-9904-8aa80faa09e3 | -3.90417 | -41.59278 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 4883f64a-929c-341e-8b52-e54e0022c6af | -7.75521 | -54.94692 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 21f7d4f2-872e-32f9-900c-d8888ffab5ba | -5.67868 | -53.5013 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 47a4a839-1bd3-37d8-866e-a19a7da27d38 | -9.25517 | -45.63858 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69d78706-5470-37b4-ad39-1ad73750d6dd | -6.21089 | -41.58668 | 2026-10-07 16:37:00 | NPP-375 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 130351de-92a4-351b-9dbd-7e138699dc20 | -6.13673 | -47.93111 | 2026-10-07 16:37:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| bd27c6ca-c551-322e-a261-d6b8f18168e7 | -5.78433 | -49.82413 | 2026-10-07 16:37:00 | NPP-375 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd56b00d-881a-33b7-9e3c-99d2d4ed627c | -4.25902 | -42.2937 | 2026-10-07 16:37:00 | NPP-375 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ca6d1a79-dbd0-36bb-ac53-27ae0165b5c7 | -6.91194 | -51.17427 | 2026-10-07 16:37:00 | NPP-375 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c6a06ed5-dd2f-3d6d-89a5-88d4cfecb4f2 | -3.91335 | -44.66112 | 2026-10-07 16:37:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0672aa22-8d34-3c64-ace5-9f5adf937598 | -14.41369 | -40.36833 | 2026-10-07 16:37:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2dc7cf2f-f4ed-3244-b938-b3a7cb10c9ae | -3.91145 | -42.30772 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 2eeaa815-1357-3196-8c63-633207743efc | -6.58292 | -53.0299 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d22153e1-45da-3069-a4db-be835bda97d5 | -4.79553 | -43.23112 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bd365a2b-288c-34f1-9c10-496d276a3622 | -6.01004 | -42.27147 | 2026-10-07 16:37:00 | NPP-375 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| c1fa6620-b492-3029-93f0-20f107576cf9 | -6.99353 | -43.97746 | 2026-10-07 16:37:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 732aea0d-25a4-320d-9e72-22ab7c91b9e0 | -17.02624 | -45.9125 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5a6ef24c-b73b-36bd-958e-2c4ef993ebd0 | -6.2216 | -52.84573 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a35f4a49-6dfc-33ab-b73a-4311f518564d | -3.50191 | -41.94851 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 796e676b-db0d-3b5d-9ece-0e290b411f71 | -4.8335 | -40.72876 | 2026-10-07 16:37:00 | NPP-375 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 8a6b3d69-df7f-344a-ab52-abe611c899c4 | -5.73698 | -41.73687 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 19e658c4-44b9-3b92-99e3-a898863a660f | -9.82209 | -46.24508 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3b0bdf76-9dde-327d-b834-b8d51332a368 | -5.27509 | -47.911 | 2026-10-07 16:37:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 3dfd3327-2dc7-3633-8f12-5d4a6803ef6c | -10.88566 | -46.68284 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c0cd4c4b-b5a5-36c3-a06c-7ecdd52fde8e | -6.27523 | -52.84953 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 7c8621bb-ca86-371f-9002-b35319f72e4c | -6.24509 | -53.45487 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ad261ef6-3a48-3969-9d6a-0ba242458846 | -8.31131 | -50.3759 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e195749f-7427-3d56-8d73-d5bb2c30feb5 | -3.3012 | -40.08938 | 2026-10-07 16:37:00 | NPP-375 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0f845c8b-8f56-3021-b163-630108d07dbf | -6.09282 | -53.89619 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c1757d58-bb75-332c-896d-0f09683d5369 | -3.95119 | -41.53865 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| b0af9f7b-2403-38b7-93ef-d160365ba51f | -6.00375 | -53.50212 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| abf2ec2a-2e1a-31c0-be36-518b7aede9ed | -3.28074 | -42.58508 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5d65ccff-8c52-31ed-bf2b-fdf61db0d71b | -6.33095 | -55.32943 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1e91ff78-8d6b-33a3-9fa1-cbe654544db8 | -3.77378 | -41.77913 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 25f396e8-acb2-3cc1-aba4-6fafdaf2ba5b | -6.43702 | -44.85339 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4519c209-d7ac-3d00-bb6d-f4f2782797db | -9.87243 | -46.30563 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0f86f339-8f8c-3ab3-a479-8758342df9b1 | -10.9977 | -45.47795 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 425d8d39-c753-38ae-8cbc-e413a7e6fa67 | -15.11452 | -43.62962 | 2026-10-07 16:37:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 7748194d-bec9-3a56-94ce-d4fc14ff684f | -6.37503 | -42.92863 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f12595df-b3e2-3417-a549-d54ed27456e2 | -5.55393 | -43.43676 | 2026-10-07 16:37:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e61d58ab-aaf3-3c37-9604-5f8e8b0c15bb | -4.23641 | -49.98429 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d298dfd9-935c-3199-8228-55b32e96e786 | -4.08189 | -43.24855 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b1ca360-c2f2-3ad5-911c-18e2991c6ab8 | -7.8102 | -44.59164 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33073ede-dfb5-3592-8635-0e3ff2d029ce | -8.99969 | -41.47705 | 2026-10-07 16:37:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 50431281-89e8-3128-bab4-e4ec67b195f6 | -9.563 | -46.84577 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 22b50d59-a680-3ea7-86b8-c59d71d24b3d | -3.23291 | -42.78962 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| eb0627a3-5d48-38cf-86a2-0b15e688fca9 | -6.17496 | -35.42327 | 2026-10-07 16:37:00 | NPP-375 | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3dc34545-3676-3ef8-a9d0-a6737be3fddd | -6.47265 | -52.81058 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 161a9ef9-8325-3366-91f3-6b7577786869 | -4.93933 | -40.54722 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 234f6ebb-a31e-3f84-81b8-061ce97849ce | -9.34992 | -45.42978 | 2026-10-07 16:37:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6320ab54-85cf-3047-9761-0dd62b5433bb | -8.98629 | -45.9431 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2458d418-0673-3e07-8e07-753ff683f5ed | -15.70469 | -40.59863 | 2026-10-07 16:37:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b23214d6-892c-372b-ad0c-bc8264dac427 | -6.05305 | -53.48652 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 128ac71e-dec3-39e8-88ef-4416825a4580 | -4.26676 | -50.78553 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6d27c307-4a5d-3951-96e7-c0f7c00a0b27 | -7.47471 | -45.77557 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5c7cd734-8fb3-306e-ad68-6b62ac3f6800 | -5.51636 | -45.62041 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ec76a11-8d7d-3b7b-972d-1733f4b5e2e4 | -9.9043 | -45.19309 | 2026-10-07 16:37:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 66be9790-1788-36b1-921c-8e89dd8e7950 | -4.30171 | -50.78198 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 03e3c6ce-a3c6-33bb-a5d1-c1ac6f5e5fc7 | -9.91985 | -44.80756 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1d3d25a2-67c5-3e87-9a30-c6123675409c | -6.60947 | -53.02629 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d4108aa2-3be7-3477-92e2-dd4ab5f68283 | -4.95623 | -49.17053 | 2026-10-07 16:37:00 | NPP-375 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8d2265e5-e9c6-3663-9b80-5ac1540c072e | -7.00627 | -44.06078 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0e48b406-27d4-3509-bc06-3457b60239f7 | -4.06158 | -45.87418 | 2026-10-07 16:37:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1a077711-e837-332c-b207-387c20eb12c7 | -9.29039 | -50.31561 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 362d7df7-3c06-3098-984e-327932eeb071 | -7.0471 | -44.32832 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d21fe1c7-5009-33e3-8a56-e26109f1588e | -3.63855 | -44.81042 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6afdf48d-9f62-3505-9167-66191d61603a | -6.98112 | -40.03616 | 2026-10-07 16:37:00 | NPP-375 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 2a811e81-f015-3168-9142-62550eab35d3 | -3.96328 | -41.54131 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 865ced0a-37d8-3192-8409-11ce80a287b4 | -10.9717 | -45.39754 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e05e6cc1-feef-3e03-b97e-0d33cece8b17 | -9.96863 | -47.61907 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8e2d98e0-cf54-32fc-a038-8416ce96caa2 | -7.04324 | -44.32534 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5688397e-502a-3f8b-b376-ed6080c2aba0 | -5.53466 | -44.95953 | 2026-10-07 16:37:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5882fa9d-14d2-3569-9977-5f683f6d04a3 | -6.68975 | -48.20681 | 2026-10-07 16:37:00 | NPP-375 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 16.3 |
| bb7f5921-67d8-3619-8643-75651dd0d188 | -7.84121 | -45.52293 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2a13eee-48ce-35d7-b31e-0d3532db4f07 | -3.91606 | -38.62087 | 2026-10-07 16:37:00 | NPP-375 | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ca20f241-a492-362f-8243-e32d27bf9046 | -3.87484 | -44.12203 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f27b58c8-cba9-34c0-966b-0b9c6ab7d95e | -9.86887 | -46.31408 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96f8616f-a048-3f20-afd6-6a15c99eaef2 | -9.86818 | -46.04704 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 21829c60-2d54-3cba-90da-c56409126c76 | -3.11061 | -41.16649 | 2026-10-07 16:37:00 | NPP-375 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 509f3af7-939b-36a7-b513-4dd9b11f7ca3 | -16.5238 | -45.27632 | 2026-10-07 16:37:00 | NPP-375 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5701616f-ec52-37ed-b10d-cb437dbab69d | -6.59974 | -37.88623 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8db04062-ea33-38f3-b411-44373ae38420 | -16.67911 | -41.8475 | 2026-10-07 16:37:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8328c5e0-9112-38bf-9d65-8d79623699f8 | -6.0121 | -53.52216 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 85eeedae-0336-3e24-b6cd-0f1a201368e2 | -7.00662 | -43.44513 | 2026-10-07 16:37:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b963e40f-ce08-3b1f-9134-c233581e389e | -6.17405 | -52.92632 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cad9fb94-8e84-3472-9cc4-4b5beb2bc987 | -3.94883 | -41.54353 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 4f8f36be-fcdc-3d81-91f9-5be417086236 | -3.65258 | -39.4376 | 2026-10-07 16:37:00 | NPP-375 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 98c19334-3df2-350a-9c37-129303b71c28 | -6.12273 | -53.05964 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 42a92450-c613-38c7-822e-c780f74685dc | -4.08527 | -43.24804 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89ff5ab2-9c2d-348a-893c-e6a5240d4279 | -7.60463 | -42.37484 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| fc9188ea-b6e4-3db5-901a-031182ab65d1 | -9.90465 | -44.79861 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| f785cb51-9f91-39ae-8cdc-082ac021c832 | -7.81354 | -44.59111 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README193.md)
