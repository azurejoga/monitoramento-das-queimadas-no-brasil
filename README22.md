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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d0283c0-6de1-3da6-ba49-cef2d00d50c3 | -21.581 | -47.48054 | 2025-08-27 03:40:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3705c571-3c14-3132-bb39-791fcf30f27c | -20.00921 | -42.13707 | 2025-08-27 03:40:00 | NOAA-21 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| c1156055-dd3d-3403-967f-abbbaa581809 | -17.55109 | -46.62533 | 2025-08-27 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0f2b8dc-a8a4-33be-91df-ceb2c0ff252b | -20.05794 | -42.61211 | 2025-08-27 03:40:00 | NOAA-21 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a1c42928-1d0f-3d2d-b2f5-84c1bb1223e6 | -19.64486 | -43.98848 | 2025-08-27 03:40:00 | NOAA-21 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea654815-95f5-3a8b-aeaf-a5da01839421 | -20.03304 | -42.11997 | 2025-08-27 03:40:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c6ff69de-af3d-37ce-935c-b8d2c9bf91fe | -22.1669 | -47.07666 | 2025-08-27 03:40:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72989541-9c1c-33b9-b985-6680aef0f1db | -20.37133 | -42.19551 | 2025-08-27 03:40:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 69c4040d-64a3-3fc5-b263-c9b53d2bb238 | -16.92292 | -49.44133 | 2025-08-27 03:40:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a6604a3-aa25-3e2a-aa1d-45706bbecf9b | -22.25734 | -47.51545 | 2025-08-27 03:40:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0a214ec6-3444-3308-aa55-834c008dcf0e | -15.52026 | -47.39513 | 2025-08-27 03:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de9df4d3-8b9b-37fa-931e-ba102d428251 | -21.58459 | -47.48985 | 2025-08-27 03:40:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a85bf531-1d09-30f3-9b30-39b8cb2a7921 | -19.0779 | -44.32964 | 2025-08-27 03:40:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6456f696-2114-3876-ae25-890ee32542cf | -20.03703 | -42.1207 | 2025-08-27 03:40:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 84c8afea-45bb-3f5d-a3ab-a1b63804924b | -19.81973 | -44.17894 | 2025-08-27 03:40:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb25857b-33d7-3141-9f20-e589cc25a18c | -19.17901 | -44.5172 | 2025-08-27 03:40:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e4e3a8a-be15-3626-b66f-b897cc8ee7ed | -19.07696 | -48.14133 | 2025-08-27 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b0d2121-5f1d-377f-a6f4-683d3b71cca5 | -18.19973 | -45.56707 | 2025-08-27 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7de36154-da98-3ebf-9830-ad7b5c4f2946 | -21.38797 | -46.93797 | 2025-08-27 03:40:00 | NOAA-21 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 4d9c5291-e7ac-35c8-b19f-7280b6977388 | -15.66424 | -48.24316 | 2025-08-27 03:40:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 706eeb90-c064-35c0-a082-c4c30e1e986a | -18.22085 | -44.52295 | 2025-08-27 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf87bcfa-2122-3ed1-958d-d182ba358bc8 | -21.34798 | -46.89539 | 2025-08-27 03:40:00 | NOAA-21 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| c8942b11-5975-3815-8292-2a97e76d4dba | -20.11736 | -44.33193 | 2025-08-27 03:40:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c047f09d-cb8e-3ee5-9cfe-8d47a65c2a4f | -17.97823 | -48.05091 | 2025-08-27 03:40:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae7bd957-f35e-3b43-9f4a-0d3e85fae3df | -19.24731 | -42.05304 | 2025-08-27 03:40:00 | NOAA-21 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a626319b-0971-3e24-8dc2-b2f6bae4cde8 | -21.38277 | -46.9367 | 2025-08-27 03:40:00 | NOAA-21 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f1b01f04-119a-314c-9cdf-d05bd4ba5667 | -19.1611 | -41.4969 | 2025-08-27 03:40:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3d559e8b-04b9-3ca6-a5fb-4c0576a902d7 | -22.16289 | -47.07255 | 2025-08-27 03:40:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f497ac7-24dc-3518-8cca-a89c193c7832 | -18.25122 | -45.36513 | 2025-08-27 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71eb36ca-7731-31bc-968b-15719f11f0c6 | -17.87154 | -39.84848 | 2025-08-27 03:40:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 254ae000-49a3-3e1b-8288-bf200ae73909 | -20.3552 | -42.25998 | 2025-08-27 03:40:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 25fff377-3b2c-39c5-b9d9-0878a168e46e | -16.92161 | -49.44716 | 2025-08-27 03:40:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28effb57-c54c-30e8-bff0-87bcb5c7a791 | -21.78865 | -43.30307 | 2025-08-27 03:40:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9d7393c8-e806-32c9-b50e-c9ba9f91ebd6 | -19.16308 | -41.50803 | 2025-08-27 03:40:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 89f92803-0336-3820-a8f4-def1b9c6c2e2 | -18.93683 | -46.58253 | 2025-08-27 03:40:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f784c6a-1a80-337a-bb27-ce68bef7e0bf | -18.07072 | -50.48212 | 2025-08-27 03:40:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85f24648-dc11-3d31-b9de-a509f93a195a | -20.0553 | -42.60364 | 2025-08-27 03:40:00 | NOAA-21 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9a0c973c-3233-3b09-8a62-7b2c50bd2fc9 | -16.70844 | -50.41675 | 2025-08-27 03:40:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4b9e419-0a0f-3262-99a8-bf9d6d1280a2 | -17.77709 | -44.48351 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e5cf241-cc5b-3b8e-88a2-8c806a2762ec | -21.34869 | -46.89214 | 2025-08-27 03:40:00 | NOAA-21 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 59cb737d-c576-3ecf-a1d2-a91a4b376718 | -20.75899 | -44.75919 | 2025-08-27 03:40:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 284ad86d-784a-35bf-8910-f729f0f48f25 | -17.7735 | -44.47659 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36f8a479-a779-3010-aa3e-8c369a7c6234 | -18.1575 | -42.67914 | 2025-08-27 03:40:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3e7fbfc7-0ab0-3853-a6f0-0c11f94f60d7 | -21.00573 | -44.17718 | 2025-08-27 03:40:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| c0625921-ccb1-3620-b7c3-2e76d5ce579c | -15.75377 | -50.4104 | 2025-08-27 03:40:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 76458fef-ba8a-3671-8046-1221d5854c40 | -21.13842 | -45.88456 | 2025-08-27 03:40:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1c2d380-2fa0-31fd-b95a-e9caf7d50d35 | -17.7836 | -44.50058 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7e9b1b0-601b-340a-9950-667c97b670f5 | -20.40235 | -46.71927 | 2025-08-27 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f484fcf-42bb-3745-b206-fab59e1cc6d1 | -20.79997 | -44.5782 | 2025-08-27 03:40:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a1fc3429-b894-3dc2-89ec-2247a4970cff | -21.34727 | -46.89864 | 2025-08-27 03:40:00 | NOAA-21 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 13dd7a67-951f-3956-a3ff-ceca9c03dff0 | -20.06278 | -42.60899 | 2025-08-27 03:40:00 | NOAA-21 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2780786b-0230-304a-a861-407e334fd177 | -19.70278 | -41.67512 | 2025-08-27 03:40:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| df83166e-eeed-3e69-945a-d35fc8e2ff62 | -18.15335 | -44.43879 | 2025-08-27 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34382a72-c044-3379-91e0-305bafb1ef75 | -20.39215 | -46.71553 | 2025-08-27 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62fcd7da-e5f3-3b8f-9226-1cc84e8f1794 | -21.00323 | -44.17368 | 2025-08-27 03:40:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 40eabadd-b2cb-3594-95df-e4062d1481f7 | -22.68602 | -46.83344 | 2025-08-27 03:40:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ef229e24-5350-3dad-8196-7dc6668c3656 | -17.55436 | -46.61018 | 2025-08-27 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f524f167-8a10-3803-8343-a33fb30a5ba4 | -21.13211 | -45.89006 | 2025-08-27 03:40:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 0071612d-fee3-32a2-8438-8937b5916e84 | -20.39289 | -46.71213 | 2025-08-27 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9e2ee66-ee37-3085-9109-b79074b277f9 | -19.08182 | -48.14725 | 2025-08-27 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4636cfc3-ea13-3258-8f9a-c834639f5757 | -19.16404 | -41.50285 | 2025-08-27 03:40:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 61533ac5-4ec6-3428-afc5-44e5b8dc9dda | -20.39495 | -46.72797 | 2025-08-27 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cb5f4bd0-6da8-3351-a896-322c41b45a56 | -17.5517 | -46.62585 | 2025-08-27 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33430f2b-9077-3498-b14a-dfab5f17ec4e | -20.11688 | -44.33558 | 2025-08-27 03:40:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| bef86150-a777-319e-af22-fc4668ad3341 | -17.55354 | -46.61396 | 2025-08-27 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1802230-2f95-32c1-9235-be7ee1f90d7f | -16.70147 | -50.4152 | 2025-08-27 03:40:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1112e28b-0013-3dc1-8045-7435cc65e82d | -21.24027 | -44.58593 | 2025-08-27 03:40:00 | NOAA-21 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f57344b0-9350-31c1-a946-c11a0173a7c8 | -18.19461 | -45.56606 | 2025-08-27 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c970c43a-6253-3ea9-8257-56b23b239534 | -17.25825 | -44.88367 | 2025-08-27 03:40:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 338987d3-c4c0-3dc5-97de-1fff8a4af8c7 | -20.1132 | -44.33037 | 2025-08-27 03:40:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c8ea8683-e9f8-372b-9364-e57c1c00846b | -17.8075 | -44.50613 | 2025-08-27 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e231f25-6de5-30a1-b908-e00177ed4e37 | -18.19529 | -45.56277 | 2025-08-27 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfc24fa9-e13c-3114-9787-d82ba1ce113e | -17.55408 | -46.61444 | 2025-08-27 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dce363a-7ade-33b0-8537-b70d7687e759 | -21.3242 | -42.80696 | 2025-08-27 03:40:00 | NOAA-21 | DONA EUSÉBIA | MINAS GERAIS | Brasil | 3122900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3a15fca3-4356-3880-9400-f4ad017daba5 | -20.79544 | -44.57708 | 2025-08-27 03:40:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 38193e4b-403f-3ce7-82c2-4b8207833aba | -18.92927 | -41.93507 | 2025-08-27 03:40:00 | NOAA-21 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1ba118aa-88ac-3673-ae86-09531a1882b3 | -20.39573 | -46.7244 | 2025-08-27 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9919ded-8279-3813-9fa3-f2b7e81d292e | -22.16177 | -47.07523 | 2025-08-27 03:40:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4df53717-c6c2-3b79-bd25-ecc2ffc1cdaf | -20.52221 | -42.27119 | 2025-08-27 03:40:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cb6e54af-5475-3190-9b76-1ca24fab8c89 | -17.36794 | -49.1787 | 2025-08-27 03:40:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08d3ffd4-f8a8-3bce-89c2-6491ef8c7980 | -22.02043 | -42.20824 | 2025-08-27 03:40:00 | NOAA-21 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b7c05eb5-b318-3ee9-9573-9d93c122c675 | -20.4016 | -46.72271 | 2025-08-27 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f35ddef-01fd-355d-8bcf-5816e413c3a2 | -20.04752 | -46.10015 | 2025-08-27 03:40:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a1a2419-908c-3816-a904-92504acc1585 | -18.79604 | -40.15698 | 2025-08-27 03:40:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8c0cc95c-7b46-3147-b1bd-f405125b3ce7 | -20.98449 | -40.9572 | 2025-08-27 03:40:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| af860eba-bb46-35ca-9f86-e4da2bdeea2b | -18.75997 | -40.12704 | 2025-08-27 03:40:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d45f3864-e446-3e36-a70b-d6799025f24f | -19.05955 | -41.91155 | 2025-08-27 03:40:00 | NOAA-21 | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5e00048b-5562-3ca5-9458-6a476cfefd07 | -21.13347 | -45.88364 | 2025-08-27 03:40:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| be357289-a7be-3f12-9fa2-a915fc1f2a05 | -17.5525 | -46.62204 | 2025-08-27 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5468f599-1c1e-38c8-b379-4eaf0d2d5b47 | -18.21972 | -44.52848 | 2025-08-27 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 82fa91ea-aeaf-3b9e-9822-5332a9e07afe | -18.0579 | -45.16496 | 2025-08-27 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e6b3b30-2c0d-3495-b9af-3be886cc34b6 | -18.72307 | -43.81941 | 2025-08-27 03:40:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55b27e44-9b44-389c-9237-6f84aa35d7e2 | -18.15917 | -44.43447 | 2025-08-27 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f16fc583-cf11-3885-88d6-b2b31ff8c758 | -19.772 | -41.95905 | 2025-08-27 03:40:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e2ad5764-d755-3b77-9ce9-00754cfd4983 | -16.76392 | -43.11167 | 2025-08-27 03:40:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b067fc81-bdef-39ac-b3a8-f5fb1dd22219 | -18.93209 | -41.93473 | 2025-08-27 03:40:00 | NOAA-21 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fada2758-35d9-37fe-b13e-7e247c5f7135 | -20.50024 | -42.22301 | 2025-08-27 03:40:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e0e1e738-7642-34d3-9301-19e0f73b2177 | -18.19593 | -45.5596 | 2025-08-27 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce77e286-204a-35da-bbf3-15dcb621e404 | -15.75701 | -50.41146 | 2025-08-27 03:40:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b3980e0b-988e-39a7-8eac-4ea575447685 | -21.35317 | -46.89667 | 2025-08-27 03:40:00 | NOAA-21 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |


[Clique aqui para ver as próximas entradas](README23.md)
