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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd6d6eb3-0fc0-3105-bf86-94e5f8f2c60f | -19.04245 | -45.65855 | 2026-10-02 04:19:00 | NOAA-20 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07df103a-989b-3ce6-88b3-9628f9cab61f | -19.02701 | -45.64801 | 2026-10-02 04:19:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c2651df-c3de-32d4-80d3-7d7653bc1972 | -7.4031 | -55.2114 | 2026-10-02 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 7d0b89bc-62d6-3f5b-a158-32d297d85bcb | -3.2951 | -53.8395 | 2026-10-02 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| c86471d1-873e-3ded-b443-52a8467d2207 | -7.4033 | -55.1913 | 2026-10-02 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 42377ee8-2bd4-3b2b-9ee3-e55705c79b36 | -3.1299 | -53.7431 | 2026-10-02 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 47eb408b-9fe6-32bc-bd47-b2f16e725232 | -7.3846 | -55.2124 | 2026-10-02 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 06a90d6f-370d-3556-9c40-8d97d82cec51 | -3.2767 | -53.84 | 2026-10-02 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 73ac52de-51d6-3d02-9e6b-35c41abbee8d | -10.2678 | -49.6616 | 2026-10-02 04:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b111b0c4-cb6f-3026-83c1-1ec05bb44b9a | -2.0577 | -56.8591 | 2026-10-02 04:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6d04fb36-baaf-3b37-b676-64373e4b519d | -2.0394 | -56.8593 | 2026-10-02 04:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1e4edda9-42b3-305b-a8b1-44dc842e73d2 | -7.4031 | -55.2114 | 2026-10-02 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| cafc4ed8-42e4-3162-8f74-dc116e738c77 | -3.1299 | -53.7633 | 2026-10-02 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6dd5f008-b9bf-3a5a-aada-aaf6a920ef39 | -3.2767 | -53.84 | 2026-10-02 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 581a1863-43db-32ec-8a6f-5291d6e97320 | -2.0577 | -56.8591 | 2026-10-02 04:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5a532100-8f36-369b-8bd2-afbe1bd74250 | -7.3846 | -55.2124 | 2026-10-02 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 19775a34-ece7-3670-a8e7-ceb16ebb65d7 | -3.1483 | -53.7426 | 2026-10-02 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 278a0179-ac78-3470-b244-b8b2249f717d | -3.1655 | -54.0844 | 2026-10-02 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ac32bb3d-4d77-3f90-9afa-1022ba90dad6 | -2.0394 | -56.8593 | 2026-10-02 04:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ba21ee3f-7161-3649-aecd-ae7edf2527a5 | -7.4188 | -55.5902 | 2026-10-02 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 4cc6997d-9099-395f-9f9b-47dcd54a118c | -3.1299 | -53.7431 | 2026-10-02 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 7c984560-5774-35d1-9bec-fd14320be940 | -1.17628 | -49.29424 | 2026-10-02 04:55:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac58a396-9978-32ef-b7ea-0bce7bb60f50 | -0.37279 | -51.73928 | 2026-10-02 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19557a43-a1da-370f-86f6-b419b8bfff52 | -0.85711 | -48.63164 | 2026-10-02 04:55:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2b7cbe4-b73b-329d-8f2a-198fb7071d12 | 0.31162 | -51.04486 | 2026-10-02 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85e74b57-813f-38f8-bb06-2f28a8726550 | -1.33232 | -47.78506 | 2026-10-02 04:55:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 120618fd-7c6a-36c8-ac88-6116c7e3451a | 2.09262 | -50.75388 | 2026-10-02 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 307fac16-9639-3619-b302-e7475fd18c53 | -1.22331 | -49.01739 | 2026-10-02 04:55:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16e91de1-6313-36dc-acf7-091d4092c076 | 2.56394 | -50.91404 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5d37914-ff04-3811-94d7-b71cb31f1302 | 2.54719 | -50.96057 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10101304-4b2a-3058-97f4-dba419201096 | 2.3562 | -50.75832 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ca93251e-2ffe-36d1-9d61-4a2712918472 | 1.72987 | -55.93822 | 2026-10-02 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7838357c-144d-36f0-b462-3479f1cc2d8e | 3.81581 | -60.99258 | 2026-10-02 04:55:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd906fa9-acd9-3bf4-ace7-d745888bb593 | -0.24777 | -48.48955 | 2026-10-02 04:55:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1f991e2d-01b1-3224-85cf-2fcc8c562435 | -0.41828 | -51.99202 | 2026-10-02 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e86bbe6-a9be-3f04-aa9c-a0e97738cd24 | -0.24904 | -48.48721 | 2026-10-02 04:55:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 078123d6-b495-3bd2-8d09-f5c064a4ce3a | 2.485 | -50.92964 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73002b76-0425-3a54-9a7a-19a8d5267e1c | 3.43121 | -51.27758 | 2026-10-02 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7816c7c-8596-3ed7-a6ac-71f336eb1387 | 4.32231 | -59.9842 | 2026-10-02 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e7ca107-7000-34ec-bb98-54518ca9c06a | 0.69896 | -51.43263 | 2026-10-02 04:55:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c902844d-15f3-3bcc-895a-4eccf7734731 | -1.22713 | -49.01798 | 2026-10-02 04:55:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b41e7ffc-c3f6-3bdb-9951-6c8c594012b6 | 0.30822 | -51.04539 | 2026-10-02 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18901c22-a89f-34b5-af72-de4cd01476f4 | -0.37614 | -51.73979 | 2026-10-02 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd761b4f-75a9-397b-a896-10f111a0cc16 | 0.6318 | -54.40251 | 2026-10-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a45bd4f-8f23-307b-857d-9f8c6fb54c51 | 1.84705 | -50.8286 | 2026-10-02 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a92f144d-3f39-3868-8ec9-f3263cee56cb | 2.35282 | -50.75885 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c63b2f6-de90-3daf-a3a0-b0a6e47f0159 | -0.94068 | -47.55181 | 2026-10-02 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25e67d81-9df1-30fb-a168-03d20d43357d | 2.47989 | -50.78685 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d329781-9c2d-3477-b2d0-d734db19bc86 | -1.29164 | -46.60875 | 2026-10-02 04:55:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c639152-bd6c-3a21-bf1a-ad335f5ab23c | 3.43067 | -51.27409 | 2026-10-02 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a731ffc-b3f9-3acc-9f08-dff562c19756 | -0.9401 | -47.55567 | 2026-10-02 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a386043-0547-3022-afac-6070af89835d | 2.54663 | -50.957 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87d8d0cc-e61e-385c-919c-3903243f3cf0 | 1.92363 | -50.88769 | 2026-10-02 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf249f4c-e417-3775-b326-f01ad7fcf501 | -0.37 | -51.73522 | 2026-10-02 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a254571-19b7-39b0-8898-203f04a340ff | 3.82295 | -60.96854 | 2026-10-02 04:55:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eff21802-152a-38bc-a3ce-b9ecf9138573 | 2.55054 | -50.96001 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 53652d3a-fe40-3ea7-af3c-d2d65f8e77e4 | 3.82154 | -60.99509 | 2026-10-02 04:55:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a900cc53-1b99-3e5d-a161-dafa1f59b3d2 | 2.48046 | -50.79046 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a1e8de9c-285c-3eca-af2a-a24cc86ad5a6 | 2.55278 | -50.95238 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f23c27d-d23d-335b-b470-d9c92273641b | 3.82818 | -60.96775 | 2026-10-02 04:55:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71edeb1e-d63a-3a31-a5ef-efc6116c2ee8 | 1.72921 | -55.93398 | 2026-10-02 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03567bdd-ab6e-3535-bc82-08706ad3d508 | -1.28979 | -46.60575 | 2026-10-02 04:55:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 671d2588-5e21-3620-8e1d-edf47390c71b | -0.25167 | -48.49016 | 2026-10-02 04:55:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| badfeea7-276c-3f94-8744-bd5917baf294 | -0.38117 | -51.75146 | 2026-10-02 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba939d6e-64cf-3126-a4c4-8943f5e4a823 | 0.56569 | -51.32119 | 2026-10-02 04:55:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4f77f20-0de9-32dd-870e-7422b7647ef8 | 0.49908 | -60.60096 | 2026-10-02 04:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23c595db-0b6a-375a-917c-395182ec2b4b | 3.82723 | -60.96141 | 2026-10-02 04:55:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4c278bf-2b7f-3ed1-b23c-b6788201dce7 | -0.25294 | -48.48781 | 2026-10-02 04:55:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51f8e105-df7b-3011-abcc-eb9bcdcad329 | -0.99761 | -47.65434 | 2026-10-02 04:55:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab6aaf17-0f22-3930-a66d-28e012dc97bc | 1.89554 | -50.66442 | 2026-10-02 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd50637d-ae75-3b2c-b844-97e66d72d507 | 4.32312 | -59.98967 | 2026-10-02 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60213945-298d-330d-960e-aadfa7cd1599 | 0.98039 | -50.12855 | 2026-10-02 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3aae656c-92f3-3a72-a598-11b201bcd2f0 | -0.25219 | -48.49274 | 2026-10-02 04:55:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc00e5f8-8b1e-3bf0-9bf3-d31bcdea3fa9 | -0.41495 | -51.99152 | 2026-10-02 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a222574b-3dc6-388e-869d-24973e8a74af | 1.8126 | -50.83024 | 2026-10-02 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2587602-cfce-3299-b191-871f4aeef17c | 0.30764 | -51.04172 | 2026-10-02 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f11a6422-fe84-3978-9f09-48ddedda12ed | -0.41053 | -51.998 | 2026-10-02 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f57372cd-b5ee-32e1-a996-8f14a453bd27 | 2.54999 | -50.95648 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a26f8b47-06f2-3d60-89c0-a9e18b634bda | 2.35958 | -50.7578 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e6bfdfb5-d868-3102-9a6e-fbd0034ec8c5 | 2.54942 | -50.95291 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ab72087-5397-3108-b682-9a0339d4465c | -0.5377 | -50.45993 | 2026-10-02 04:55:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dfda4cc-a7bf-3acc-9b1e-7b89cfcc9e60 | 0.62898 | -54.40663 | 2026-10-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c33e119f-c4df-3ff6-84e2-4dd9bb341149 | 3.41576 | -51.52534 | 2026-10-02 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f5802a4-13ff-3742-a0c7-3e92918d2a6f | 1.13103 | -51.30065 | 2026-10-02 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef6c86f2-1040-3706-b11d-979deef10859 | 0.30424 | -51.04225 | 2026-10-02 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7321d296-f8bc-3c97-958f-dd84e5964612 | 2.25198 | -51.70067 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9697228e-7013-30f2-b014-f03050e7295a | -1.16263 | -49.13241 | 2026-10-02 04:55:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20dde0de-bd02-3e39-949f-441fa7e84787 | 0.62842 | -54.40302 | 2026-10-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3f2e8bc-a80e-33be-97f6-e527ea2eb40e | -0.40457 | -51.83869 | 2026-10-02 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f3f663d-9af5-3a65-ac07-06e4cf460901 | -0.42495 | -51.99303 | 2026-10-02 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fab29930-f2ac-392f-8dc7-b221e75a93cf | 3.82771 | -60.96457 | 2026-10-02 04:55:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92b36e4d-181f-374e-9c0f-d0fe3406c51d | 2.5673 | -50.91352 | 2026-10-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58e4235f-93bd-3f29-881c-6a14aa999cbc | -7.41302 | -55.58884 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc04fe70-8d0c-38f9-b35f-aa5610dbc502 | -6.23502 | -53.12986 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aab062d5-be4e-3bb6-bedd-bbbe0dbbc147 | -1.62353 | -55.13895 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7df44a80-119d-3baf-9475-fdf90c57cab1 | -8.38486 | -46.29251 | 2026-10-02 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0d3bd2b-fd10-3599-8f10-3dc5582d74f1 | -7.86801 | -44.17484 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77c472e1-503a-3fe2-84aa-3a4846e1d137 | -2.89171 | -54.13148 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c683150-7a35-31b1-be82-b251bd8bde0c | -4.60865 | -50.92149 | 2026-10-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fa8b49a-34ef-3350-937d-2002590ca93d | -3.10883 | -50.29116 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README51.md)
