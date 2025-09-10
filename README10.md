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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22d9a86e-b40f-3e88-9d34-1c72673424e1 | -11.4469 | -43.5988 | 2025-09-10 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 94dc0aca-306b-3d32-9d62-ddb4057398ac | -8.0602 | -48.6856 | 2025-09-10 00:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 4add06a6-74ae-3f8f-9511-421020015c9a | -11.4465 | -43.6224 | 2025-09-10 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c37a78d8-6014-3c53-bcb2-038bb91add6c | -5.5703 | -45.0518 | 2025-09-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| da7b7e19-945e-3bab-9794-4df4d08adadf | -5.5892 | -45.0278 | 2025-09-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 855840a1-1054-305c-9d98-c3477901083b | -18.1519 | -51.7281 | 2025-09-10 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 17d00eea-09b9-3550-ad7f-13c5f15daa0c | -20.9873 | -48.0033 | 2025-09-10 00:40:00 | GOES-19 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 0df6fb51-b275-355e-9cfc-b01a99db5872 | -8.0414 | -48.6873 | 2025-09-10 00:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 33f05858-6799-33c2-b102-dfb77d07a990 | -18.132 | -51.7315 | 2025-09-10 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 2813e57c-fb66-3c15-af13-d5ec8385f8e9 | -18.1325 | -51.7096 | 2025-09-10 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 548795a2-9af3-37dd-9dc3-05bb61bf7450 | -15.801 | -52.2472 | 2025-09-10 00:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5e8df708-f1f3-39f2-963b-ee1a3b54a136 | -19.3571 | -47.4464 | 2025-09-10 00:40:00 | GOES-19 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| cf429953-bdbd-3ae4-a406-09189656a67c | -5.7369 | -47.4681 | 2025-09-10 00:40:00 | GOES-19 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 4713ca60-1f44-3498-9c7e-0474c4bf196b | -9.4388 | -46.7052 | 2025-09-10 00:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 37b1f947-affa-3f64-88af-40e1136a1bea | -15.8873 | -51.8059 | 2025-09-10 00:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 228.8 |
| 89fe5744-6a1f-33d3-ad4c-d90200b3f843 | -8.8647 | -45.8693 | 2025-09-10 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 9e4e2fdb-c5f9-3cd2-a5bc-44ba5abb6ec5 | -16.4703 | -51.9768 | 2025-09-10 00:50:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 726cb459-9ae9-3e44-b9fd-0baab1f7295f | -5.589 | -45.0505 | 2025-09-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| cbc48bc3-76c5-3a67-9577-ed824f0d9317 | -8.0414 | -48.6873 | 2025-09-10 00:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 1b0f3118-a188-37ad-9a99-75e4388f161f | -8.0602 | -48.6856 | 2025-09-10 00:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 1e2a428b-5f07-3da1-aa88-7aec63f4fcca | -13.1176 | -54.9191 | 2025-09-10 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 8ea85fda-370a-315a-8892-fb34e5ac8d6b | -15.8201 | -52.2659 | 2025-09-10 00:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| aa52326b-cbf1-3d4e-b2f1-c67313ab9734 | -15.8006 | -52.2687 | 2025-09-10 00:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 138966d2-37a1-3337-9d88-aa7457f81773 | -5.5703 | -45.0518 | 2025-09-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ee8e53e7-8630-39e9-b81c-5ffdc25750b8 | -6.8897 | -47.8897 | 2025-09-10 00:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 928c153d-8cab-36b3-8595-f5b614a713b1 | -10.6108 | -43.2969 | 2025-09-10 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 54.4 |
| 5c8026f5-f9a3-354d-9182-470c8e882c51 | -13.145 | -45.2929 | 2025-09-10 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 3ae9efb9-9315-3d8f-b413-46d515b177ca | -8.0604 | -48.664 | 2025-09-10 00:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ec6d7ee7-5e10-3567-afad-3d0b512d21ed | -15.8869 | -51.8274 | 2025-09-10 00:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 31f35fee-0c01-347c-8477-61bba8007afb | -19.3571 | -47.4464 | 2025-09-10 00:50:00 | GOES-19 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 4bd230ab-55a6-3250-8cca-fb84738f47ac | -16.4707 | -51.9552 | 2025-09-10 00:50:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c2f99efb-5ddf-3983-8e76-ad559d465d89 | -15.8873 | -51.8059 | 2025-09-10 00:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 2c561d08-3941-3e66-adb4-640e8739ee0b | -13.2031 | -45.2834 | 2025-09-10 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 34725393-1be4-31c7-9ee5-a27de60999d0 | -16.0604 | -49.9741 | 2025-09-10 00:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 8ac9d8c7-8c12-3f33-9588-5e5329707000 | -16.4507 | -51.9798 | 2025-09-10 00:50:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 9c991c75-ce44-3d5d-8cb5-877d81b3ae12 | -6.8519 | -47.9361 | 2025-09-10 00:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 7d8b3eb9-831f-3ed9-9f93-0bb2e3cc396d | -15.801 | -52.2472 | 2025-09-10 00:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 54bdf4a6-3fff-3b22-a295-bf242342c443 | -6.3368 | -47.0978 | 2025-09-10 00:50:00 | GOES-19 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| e3b98ca0-43e3-3c57-bd26-6486b1bee4a5 | -18.132 | -51.7315 | 2025-09-10 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| eceb07ef-9ada-361b-8bc7-e7b2ff3096fa | -6.871 | -47.8911 | 2025-09-10 00:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 54644afe-9f17-3082-bd11-8b8a39d2f65a | -5.6788 | -43.3425 | 2025-09-10 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| c5c156e6-0513-3c41-8cc7-1e7d2325ed8b | -6.2597 | -43.3895 | 2025-09-10 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 6a3008d5-e008-36be-8c01-affd47d72adf | -12.9482 | -54.7519 | 2025-09-10 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 126f847d-7fd2-390b-b5fa-de9f786f54aa | -15.8677 | -51.8087 | 2025-09-10 00:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 97f6bd0e-9c49-36ff-bfc6-93977b42c21b | -5.5892 | -45.0278 | 2025-09-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 335.5 |
| ef02231a-7897-3ffd-b9de-3014b8dd18cd | -11.4657 | -43.6195 | 2025-09-10 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 6aa5c12e-058c-325d-8f85-e7ce4ec81233 | -11.4469 | -43.5988 | 2025-09-10 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 77a0c04e-7c63-3dbb-b2f4-9395d16966b9 | -15.8673 | -51.8303 | 2025-09-10 00:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 062cd929-b28a-364e-ac26-fa93cd6302f6 | -8.865 | -45.8466 | 2025-09-10 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 16b169bb-4650-394b-b192-6b5255602e03 | -13.937 | -48.2522 | 2025-09-10 00:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7ff5fc09-9ba9-3744-8a29-40b4b06b32d5 | -15.8205 | -52.2444 | 2025-09-10 00:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 45c26f95-ac32-3808-9bcd-d142ffba0a46 | -18.1325 | -51.7096 | 2025-09-10 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 63e879e6-a419-3f19-a670-a9d76355276e | -5.5705 | -45.0291 | 2025-09-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 90056c70-a3c3-3c9a-9f47-24406530646c | -9.4578 | -46.7032 | 2025-09-10 00:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e7cf8e5e-0119-3033-a354-28a140e64f3e | -23.0349 | -50.0908 | 2025-09-10 00:50:00 | GOES-19 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.3 |
| 8fc31bab-349a-3e3c-98bc-324e1a3ce14e | -11.4465 | -43.6224 | 2025-09-10 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.1 |
| a2cf1e3d-49cc-32e3-9ec1-07b90a1d64c3 | -6.2595 | -43.4129 | 2025-09-10 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| bf6e6a46-d011-302f-8468-42be3c70f079 | -9.4769 | -40.3365 | 2025-09-10 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 6e32aeaf-241c-3965-90ff-080f18c4ccc0 | -9.4578 | -40.3392 | 2025-09-10 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 4d3c6045-41f2-3303-b462-c9d734c9f0fe | -9.4388 | -46.7052 | 2025-09-10 00:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 2589771a-a7b2-3fdf-b077-90871dc73f11 | -8.0412 | -48.7089 | 2025-09-10 00:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b0332a70-6d7b-3e38-8945-30a5a648c0fe | -23.0342 | -50.114 | 2025-09-10 00:50:00 | GOES-19 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 112.6 |
| 1a756908-8f1e-3974-93e9-4304148838e9 | -10.8506 | -46.1091 | 2025-09-10 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| ceb5e5a7-5e38-39b3-a948-1b888e7f2eab | -18.132 | -51.7315 | 2025-09-10 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2c712aae-5999-3639-b876-34e1fcb86789 | -15.8873 | -51.8059 | 2025-09-10 01:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 5c9e35f2-5a8f-30ab-ac58-40a904094aa4 | -11.4465 | -43.6224 | 2025-09-10 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.5 |
| adfb2656-abd3-3e92-abfd-5129993b587d | -9.4578 | -40.3392 | 2025-09-10 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 93353830-6d6d-3f42-9514-60a72f271cbc | -23.0349 | -50.0908 | 2025-09-10 01:00:00 | GOES-19 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| 14329f34-24d0-3753-bf45-1e89a50aae13 | -8.0602 | -48.6856 | 2025-09-10 01:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 1b2adb3f-0742-3294-b1e7-f92b6b4acf2b | -12.0117 | -51.0104 | 2025-09-10 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 70d62d10-3a1c-3e23-8949-8e250acf74a0 | -15.0077 | -48.0372 | 2025-09-10 01:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 37.0 |
| c10c8223-3c2d-3baf-af19-b85cd38048cf | -8.0414 | -48.6873 | 2025-09-10 01:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 0b6984db-2b3f-3f43-8d1c-6e22708d908c | -9.4388 | -46.7052 | 2025-09-10 01:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d53ae75e-c916-36e8-9818-8a57412c79a1 | -8.865 | -45.8466 | 2025-09-10 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| e2fba7ad-d62d-3418-84c6-fbd5985408ac | -21.0227 | -48.9218 | 2025-09-10 01:00:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.6 |
| b84cbeb3-e0c3-3b56-aaf4-e16549c787d1 | -5.5892 | -45.0278 | 2025-09-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 332.1 |
| 6b714ff4-0165-37b5-86bb-3deb31856128 | -18.1325 | -51.7096 | 2025-09-10 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 1c419c1c-4354-3328-bb66-9e3f02e8ae8f | -15.8869 | -51.8274 | 2025-09-10 01:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 7544ef58-5f77-37b4-9617-e0eb0d53926c | -16.4703 | -51.9768 | 2025-09-10 01:00:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5d5dc51d-1437-3f39-845a-5b5bcd70b805 | -16.0604 | -49.9741 | 2025-09-10 01:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 91025512-5da6-3d79-a79f-883b1865b861 | -6.2407 | -43.4144 | 2025-09-10 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 7d35185b-bf20-393c-967b-61b9e529eda6 | -13.1176 | -54.9191 | 2025-09-10 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9754e5fc-554d-3a11-a5ec-5565eb9ca510 | -20.9873 | -48.0033 | 2025-09-10 01:00:00 | GOES-19 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 68b11810-45db-38b7-8168-6ad8628213bc | -5.589 | -45.0505 | 2025-09-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 260.0 |
| e8bb1476-78d8-3b4e-a763-b7589d37e954 | -11.4469 | -43.5988 | 2025-09-10 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a22c8541-80d5-3c5e-80f3-8f93c309179c | -13.1367 | -54.9171 | 2025-09-10 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 950987ef-d07a-3fc6-bf1b-14ff22c81848 | -6.2595 | -43.4129 | 2025-09-10 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| f6eddbea-4bab-300b-9f36-d97be8624714 | -9.4578 | -46.7032 | 2025-09-10 01:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 80624ea8-47d5-30a7-95aa-1c6956005438 | -15.8677 | -51.8087 | 2025-09-10 01:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1960d298-af71-3421-8e6e-e71536d95d2a | -15.8673 | -51.8303 | 2025-09-10 01:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 112ec870-6da8-3f26-9dd2-090e38d862ea | -23.0342 | -50.114 | 2025-09-10 01:00:00 | GOES-19 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 89.1 |
| bf32c484-70ba-3a56-95f1-2ec37c8b0109 | -5.6788 | -43.3425 | 2025-09-10 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| aae4a32f-5b8a-3e91-9e0a-f40d5eff9188 | -5.5703 | -45.0518 | 2025-09-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 217.0 |
| acbaa272-41d1-3c60-be70-98a8900e4766 | -6.3368 | -47.0978 | 2025-09-10 01:00:00 | GOES-19 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 408616de-d88b-3ca3-ab47-04a4a6d603eb | -6.8519 | -47.9361 | 2025-09-10 01:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 8d1851c2-b731-3f08-a77c-327677844166 | -6.871 | -47.8911 | 2025-09-10 01:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 96fdb741-3d92-36ca-98f2-55d3700c8623 | -7.7705 | -46.0684 | 2025-09-10 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a4a91113-42cf-3009-aa52-d3b1a92c1a00 | -13.937 | -48.2522 | 2025-09-10 01:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b4f43268-7e5f-3bbf-be18-f0e363fb49e0 | -8.8647 | -45.8693 | 2025-09-10 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 83b60ed4-9b4f-3730-b5c1-875644d649b1 | -18.1519 | -51.7281 | 2025-09-10 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |


[Clique aqui para ver as próximas entradas](README11.md)
