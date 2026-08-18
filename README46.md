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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66a1f65f-5d2c-39f1-b181-d7f9b7ccc1c0 | -17.34428 | -54.93293 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12e9ed21-7298-33fa-ba39-6466b543d494 | -14.42941 | -51.8896 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83475d85-5719-3384-9fed-cf9a60449bd6 | -14.16996 | -52.92208 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7a606b73-b17f-36a0-b662-c9ac6079a06d | -14.17279 | -52.90342 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| df94a12b-0011-34e8-aaf3-341aa609c0e3 | -14.35633 | -51.86996 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a492a11b-c97e-3262-abc2-04ac15bcdf32 | -13.42074 | -57.06366 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce914c18-008e-3509-ba8b-d8b2e6506958 | -14.16259 | -52.90191 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 730fde17-ce9d-373b-8674-3a6a3bf4f4bb | -14.45227 | -52.95343 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba374cdd-171a-3489-83ff-58d7a0252ac2 | -14.49908 | -45.68052 | 2026-08-18 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 929a11e4-4ead-30ac-9d1d-8b5cd7eae1df | -20.29496 | -46.46942 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f0696f4-3c97-3125-9fee-b63178607d94 | -12.7318 | -59.77678 | 2026-08-18 04:59:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cae25722-4aaa-310c-be0e-63df8b4216fc | -13.43335 | -57.0775 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbbc96f0-314e-3ed9-8130-68739a8ca205 | -15.29311 | -56.44094 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85f1cdf2-11d1-3214-a4c0-95af95a234e3 | -14.49504 | -45.67011 | 2026-08-18 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 336a555d-2fee-3837-b499-cba73cc7016f | -15.27422 | -56.49162 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d621067-ca62-3368-9249-10fe216c9ad3 | -13.93268 | -53.93189 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28b40e0e-ae48-30e4-9819-f396492e732b | -17.94775 | -44.42998 | 2026-08-18 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 913e6346-49a4-3957-9711-593152795edf | -15.23641 | -56.46202 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f70d5f5f-a664-3fd1-9581-09e04df38f4f | -15.64444 | -54.81615 | 2026-08-18 04:59:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f98ccbc-2d5f-3ec2-8d5e-44442bce8e44 | -17.07906 | -46.60688 | 2026-08-18 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbe92380-2839-3864-b51a-9980ae04ee17 | -14.15919 | -52.9014 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dab9c93a-d273-3058-81e3-161a702da031 | -15.25796 | -56.50048 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7aa3b083-bfb0-3a80-a9c1-e7d3006c348f | -14.18126 | -52.93919 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5f3c4ca0-e72e-35e4-ac14-a1c7a6855309 | -14.03637 | -53.65872 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45b506de-08a3-3dc0-a97b-ffd2ccd3c61f | -14.18072 | -52.91994 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 6fac9116-f8f7-3515-a145-3d62f4d24c09 | -15.24348 | -56.48255 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32e3f0cc-b004-3634-a51a-51934b649de6 | -14.51825 | -53.09771 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f6b1bd8-cab8-33b2-a582-9330884ea67a | -13.41639 | -57.04638 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1a664f0-d5ba-3ade-8cc9-633b11a174e0 | -12.76119 | -59.76937 | 2026-08-18 04:59:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba4f21ee-78ba-3dc9-9244-9cbb5d0289fe | -14.43062 | -51.88142 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99322b2e-ca33-3a81-a773-79b435bcb0e1 | -17.47483 | -48.87378 | 2026-08-18 04:59:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92b2a062-aebf-31ef-a746-fb59731353b7 | -14.17166 | -52.91086 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9ea18dbe-6eb4-3bf0-9cc9-a419ba4d9343 | -14.83732 | -46.64785 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 300e16fa-23c7-3560-9d20-2fdc081aade3 | -13.02183 | -56.58735 | 2026-08-18 04:59:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81299109-a751-3253-9697-54b9ced16109 | -14.17335 | -52.92262 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7552360a-ad57-3d47-ac74-f0d83ab8a94c | -14.50471 | -45.67781 | 2026-08-18 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51604a1b-6246-347f-bf47-a88880410c99 | -17.08072 | -46.60583 | 2026-08-18 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4304846a-5360-3b9d-8cb7-67966f32a2a5 | -15.26219 | -56.50105 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c395401c-0244-36d8-a4cd-b5b060beae75 | -20.30811 | -46.48163 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36a8efc2-0f04-3b1b-8ef4-64ba2274f99c | -15.77977 | -55.56591 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcfe766a-6f86-386a-bdc3-d8d4ca2012dd | -20.29956 | -46.47699 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3b4cef98-d623-3a19-ba31-fb16a574ae89 | -14.53858 | -53.23772 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a2b6289-6638-3762-8033-9ccd4dfc1846 | -15.26558 | -56.50165 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b5edfc26-976a-3f66-a9c1-9a9f4d08bc71 | -14.17485 | -53.05573 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9599b97-7b39-3670-882c-24eca771d57c | -13.41843 | -54.37535 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 32213759-8192-3bbb-865b-ab64d929cdc3 | -14.16146 | -52.90935 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d964fa9b-90f0-3cd3-89fd-66dbbefb92bf | -14.1711 | -52.9146 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a84d6df-dee4-3196-8f39-5291803fe323 | -14.17429 | -53.05944 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7db4bbdc-72ca-363a-b5dd-6796e1991d03 | -15.28482 | -56.42801 | 2026-08-18 04:59:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94e8cf85-88e2-3971-ad9b-bfc8bcdd9317 | -15.28972 | -56.44037 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69d0379a-ac5a-320f-b7f9-229b0f4d0f3d | -16.32792 | -55.38981 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afea48c1-4faf-3377-bc5b-58077cd12dfd | -17.33482 | -54.94986 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a011410c-9065-3578-a6d0-c23727ec33fd | -14.03082 | -53.67254 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1a80f64-495f-3aa5-ac3d-87da2d9a961d | -14.26095 | -51.93137 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a278ce9-b7a8-3178-95e8-5206703ba592 | -14.16996 | -52.89921 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7efa9787-f575-301b-8e73-7be6a0089cc9 | -16.2298 | -57.66182 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2ff9ff16-a402-3f73-8a4d-6deb0956d1a8 | -15.16924 | -52.86132 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d83ee982-2cf5-3450-94cd-ffc7584e4f6f | -15.9141 | -55.5558 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0954829c-5547-3c1b-a5f7-61eda7e8435a | -14.49948 | -45.67725 | 2026-08-18 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3eb70d3-095a-3192-a847-5fc69966cd4a | -14.03526 | -53.6659 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24a18ee4-f952-3f0b-8f71-76d473d264fa | -14.03582 | -53.68438 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 64389e41-d70d-36cd-8f9e-59a89298b51b | -14.03415 | -53.67309 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 00d110de-cb7e-3ae5-80ff-e8c4d22fece5 | -14.49464 | -45.67338 | 2026-08-18 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cf61766-99ee-3936-b909-97ece9ae2674 | -13.39972 | -54.34325 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d14668f-d4a6-32a8-b903-a2902a047259 | -15.26041 | -56.48552 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c6f76c2-963e-3ed3-bcce-d68b5df9b91c | -14.33314 | -51.95509 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ba32e62-e851-36ba-b3d6-8ccd037f7950 | -13.42984 | -57.07689 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 817420d6-044f-39f7-aa5d-e1dde87d2afd | -15.26647 | -56.51719 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 429ec5f7-6309-3726-accc-b0dd1fb6e7fc | -20.29307 | -46.46999 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66c63ebf-35e9-35bf-8962-71303ebe5785 | -17.34096 | -54.93238 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fed4f909-b81a-3e75-bded-9b8b15d9ae81 | -17.08654 | -46.60032 | 2026-08-18 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52d77dc8-e247-3feb-a611-8a19bb631e7e | -15.2613 | -56.4855 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cd4a63b-1fae-30ee-ab63-70644a60505e | -16.22 | -57.6559 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9dc59615-3c30-3579-be0d-b46e836107b3 | -14.43002 | -51.88551 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da27abcf-92c4-3999-ae2d-2e8f86e8912d | -16.24517 | -57.65613 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| be96f871-5c15-3f6d-a381-052f0fa30483 | -14.05304 | -53.68352 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c87546c-1676-3bfe-91de-1d13789bda52 | -13.22263 | -54.34684 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51045dbb-4b4c-317d-9a1e-7b8533fe4637 | -15.87977 | -55.55726 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 399a5023-6302-326c-8569-f90ec3051927 | -15.24378 | -56.50186 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c3b28e6-375e-3348-9781-31ec6085f4cf | -14.25449 | -51.92623 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 40983d0b-a1c8-3445-b8ef-17b051cacadc | -14.18579 | -52.93227 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d04bbd16-82b9-3ee6-8dd8-79610a31f1bf | -15.91741 | -55.55641 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60be6ed9-745f-37ec-8e18-98882460eb4d | -13.74517 | -57.61509 | 2026-08-18 04:59:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1da80bd4-aff1-32a2-b9aa-06955bcb3040 | -13.42337 | -54.38704 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ef4c263-09fb-3dc5-b26d-3754312a5054 | -15.39166 | -52.80096 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9700522a-8b7f-34e5-b616-37ce057e6b73 | -17.98399 | -44.42656 | 2026-08-18 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d88df8ca-04bb-3041-b220-9150368dbeb9 | -15.93024 | -55.54026 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c090daf-80bd-3fe7-a9f6-36e8093a1871 | -18.8138 | -46.74782 | 2026-08-18 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8aacd29-b739-302a-9c28-93b410aa41f1 | -14.15522 | -52.90461 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b384978-7da6-3eca-9a29-ac56b857813f | -15.24656 | -56.46382 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9e524eb-9285-3be9-b9b3-17f03b68b337 | -15.2662 | -56.49791 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fdc6a8e2-52ce-32ce-bbbe-a69d3d4629f2 | -14.45263 | -51.83051 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13643f28-1072-39aa-bf71-544df26c3559 | -12.94033 | -56.63799 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec8eca0b-88c9-3df9-b889-c99656c6a5f6 | -16.24448 | -57.66027 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| fb96cf68-e932-302f-af5c-ef1c101eb02b | -14.25097 | -51.92569 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d30f3059-f777-3c06-9701-76371a0861dc | -17.94686 | -44.43917 | 2026-08-18 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45979e62-46d9-3279-b855-a20749bddcba | -17.331 | -54.93071 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7492589c-6f73-3f88-84f7-cb59f33a621e | -14.05249 | -53.6871 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 884d002b-2c76-348d-ada8-6f400d0dd52b | -14.4472 | -53.07892 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64542ccc-86e4-3208-aa30-325cf8d0d7c3 | -15.29249 | -56.44467 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README47.md)
