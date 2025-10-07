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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfc8acd3-a52b-373d-98e0-91f6722e194b | -14.91003 | -46.83265 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abac646c-1d74-31c1-9b7f-9e9b5ebd647e | -13.3404 | -48.03237 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41ca5346-cb49-3379-9bb7-c85a89be5c16 | -15.50152 | -47.93213 | 2025-10-07 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e63bda9d-0bcb-3784-969a-9e4a40167ced | -10.39956 | -50.29951 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 395a9dbe-29d3-3482-9dd3-187f307f503e | -13.78692 | -50.78368 | 2025-10-07 04:38:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5e6f9d5-a11e-33ab-8704-7c0dc40198a0 | -15.2188 | -56.79058 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f54a9201-82c9-3656-a6d8-077bc33acf1d | -13.09536 | -47.991 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 001da295-57d8-3e51-b734-36c569074e4e | -13.23775 | -47.24886 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d29af6dc-3404-3951-8918-682849460bb7 | -14.92887 | -51.42453 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f0852b5-3d13-3ff6-99bc-afc96790bb95 | -14.50522 | -46.93684 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5248aa52-ff4b-3c18-a805-f42b02aa0688 | -15.39145 | -47.99492 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bed1d59d-8128-308b-8d3c-56639cc64108 | -10.81169 | -48.81059 | 2025-10-07 04:38:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 724b56cc-fb84-3d75-b216-147b60dcc639 | -10.42791 | -51.63254 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58f54507-f50d-3d22-923e-35314aab06c2 | -12.187 | -51.43372 | 2025-10-07 04:38:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ab7e28e-3706-33de-b757-237c6cc42ad6 | -15.60552 | -42.3703 | 2025-10-07 04:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6e1db44-0f22-3b44-873f-037544246da6 | -14.90807 | -46.85253 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6718357-ed99-3e51-9364-b0cc0b9cf307 | -13.39194 | -47.57709 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7ac7278-01c2-3032-adf1-a789f4a728ad | -11.29229 | -49.99978 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 737c7799-a9e2-37f0-a5d5-b11b062e4d1b | -15.274 | -44.13559 | 2025-10-07 04:38:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c5a7702d-6eeb-37e3-ad31-5d69899f89dd | -14.65195 | -48.36797 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ff68814-51f9-3977-b0af-69b4004aa2f6 | -16.00032 | -50.95884 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d40d8a2b-8759-3706-a71b-113e07a610c7 | -14.75093 | -46.0244 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d58a610d-21a6-3ae2-b7c5-e00e23df1f7a | -15.58335 | -52.57049 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da8265b6-8195-33f0-a62b-840585e76664 | -15.58121 | -52.56175 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1b17b578-0149-3a2d-ad84-51da080c2fdc | -12.93495 | -54.73171 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9e8d0bd-45fb-3cee-85a9-853b786109ae | -15.22332 | -56.76701 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20d67bdf-eae2-3161-b2a5-137b362e102f | -11.88902 | -44.95779 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 092c5c10-43fc-3e99-a072-b58fcd8038ad | -10.4283 | -50.31557 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 48e1c5a6-624a-32d7-a1bd-014cd73d1626 | -11.38436 | -43.49494 | 2025-10-07 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93e0d4c6-a105-39f2-ab42-6ae9cd5f63ef | -10.61208 | -48.68163 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81af6888-6ccf-3fcf-b409-325979f150ff | -17.71411 | -40.23725 | 2025-10-07 04:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 087fba0d-0056-30a9-beab-bf548a74a75a | -9.67027 | -54.99213 | 2025-10-07 04:38:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4201f91-ea5c-31f8-95b3-014f9df8dcd1 | -13.29528 | -48.05143 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 796489b6-6626-3508-9f12-8b4f01e49d65 | -15.02195 | -47.55706 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c27c9111-c61d-3013-a98a-1f9a31b3fba1 | -16.67807 | -46.82867 | 2025-10-07 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cccda6db-eb32-3ab3-9dc6-1e8b902595e1 | -15.20886 | -46.3772 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06b358f7-c080-3dac-b5b1-559661357fe2 | -15.26881 | -46.35368 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4aa1e7df-d252-3287-b93a-89aaf1c18a84 | -16.34809 | -48.12965 | 2025-10-07 04:38:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6928c103-75df-3256-9b12-4bcffa873a22 | -16.38153 | -49.00026 | 2025-10-07 04:38:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a43ca68-575b-3f9d-b1a9-d551ad691b98 | -14.63634 | -52.51083 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56e1514b-9e9f-39e6-9599-f20c47fd5be8 | -12.97771 | -51.02741 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1df4541e-dae3-34a0-bda4-008ae4cce560 | -14.9301 | -51.41704 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19654f2f-0138-3537-8ca1-a3d650d083ed | -14.91546 | -46.82071 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32c51768-3bbb-3ed8-9bb5-22ecbce478f2 | -10.34055 | -54.19195 | 2025-10-07 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3aee9ccd-9df0-353e-b4c2-1ba04e16623f | -14.24789 | -54.25201 | 2025-10-07 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 776ddb6f-f908-3163-ad4b-f77acf9e3f76 | -15.60584 | -47.2993 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b4ae1ef-8478-3427-8c7b-aabcfec5a773 | -12.01843 | -47.78305 | 2025-10-07 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e0b6d6ff-3d40-35ef-8d48-5d7fbf216303 | -13.36905 | -47.23346 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bed0e9b-ee47-30dc-a59a-6d3f277a567d | -16.01695 | -51.05518 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9134d06b-90cd-3a8b-8760-9aae2f82d8e1 | -10.7944 | -48.5951 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83bbf16d-e209-3685-b14c-c1a6653f430d | -15.58197 | -52.57863 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3031dcde-0baf-3d7c-a1a1-b0b1cc362c62 | -9.16902 | -59.5653 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd025284-8d2e-373e-8123-120b3692e079 | -17.0877 | -43.38549 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1d0b9c2-fd99-3564-a8dd-04deeee873cd | -15.56181 | -52.44258 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f44f62c-ec2b-3b3b-ae39-febe6987997a | -12.98452 | -51.02858 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 35572b61-0f0a-3a2e-9152-e9d2b6bd466e | -14.74034 | -46.01821 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3a271b1-0849-3c72-9af1-015eb35e979a | -11.15906 | -47.95076 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4cf87f2-a56d-32f4-8860-50c8b97d499f | -10.63121 | -57.61507 | 2025-10-07 04:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e336ffba-6987-3da1-8e9d-e94855dc1cfd | -14.63418 | -52.50202 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1924ffb-df4a-357d-9fb9-8bf9e475a45e | -11.71859 | -44.44235 | 2025-10-07 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05f79d68-3957-377c-aa03-b23d075f5a93 | -16.29963 | -50.98768 | 2025-10-07 04:38:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41487c87-ece7-3fe7-a032-120efd210093 | -17.55967 | -50.4491 | 2025-10-07 04:38:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bed7191f-1a54-3272-a3f9-a64ed920bd9c | -11.93592 | -46.42138 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcb70274-080e-3d58-a786-17557563f481 | -14.91499 | -51.44521 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 13895e35-b35e-3cd6-9857-50f72d8239c6 | -10.80161 | -48.59266 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a801d18b-30d4-31ff-9b94-b341174aee7b | -16.01725 | -50.96878 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1aac3bd3-56e4-38cf-8cf0-22f892e03834 | -10.80772 | -48.59726 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4705d26-1129-3d1d-b272-6bcd853ee0d0 | -13.34496 | -47.77097 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6a86f19-aaa4-3eb6-b456-c823e30daf22 | -17.7181 | -40.25381 | 2025-10-07 04:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e12f006d-4b2c-343c-98d2-21afda3ab126 | -14.93169 | -51.47126 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26a6e32a-d52c-39fc-bc63-beccea15fa2b | -13.54245 | -42.99533 | 2025-10-07 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 8061d159-fd8a-3ef7-a79b-389973816c65 | -15.16663 | -48.00733 | 2025-10-07 04:38:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44bed460-1b53-3f64-aa35-151a07e50391 | -14.65422 | -48.37593 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56d5c8b5-3b65-3106-a2e2-714a0525f0af | -14.27646 | -45.8433 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9704394-1eb5-313e-a7a4-0a852ac0927b | -14.28641 | -45.85416 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e53bb74-dfa2-366a-8a1c-e20deb00b446 | -13.3714 | -47.24166 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d1065b3-a98d-3e2c-a468-f6dbbd234dd4 | -15.37887 | -46.28487 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 077c8c77-66ce-3b5e-9b7a-a4f7f0028c96 | -13.58448 | -48.14524 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad763844-fcb5-39af-8f4f-d89c5dfb1a5a | -17.09168 | -43.38783 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b6e74517-68f2-307c-b464-041ebb3b98e1 | -14.50165 | -46.93629 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 922dd10a-b7ce-3492-b242-c032cf7a09f4 | -10.81225 | -48.8287 | 2025-10-07 04:38:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2eb22b5b-7adc-3e5c-8d21-68e7de334c25 | -16.00408 | -50.82888 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02288ad3-1d40-35ab-a8e2-269d42bb7d40 | -13.34154 | -47.77042 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77a5be6f-033f-3e49-8c66-19f4c5e79a69 | -15.226 | -49.30823 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4aec60d-4ada-3292-a556-2af54871be52 | -14.7041 | -48.39158 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28b417b5-460c-335f-a331-9a1f9903ab9d | -13.0993 | -47.98794 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4778f30d-7eac-3be7-8468-87f314d9dda4 | -13.24367 | -47.79718 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a237c36a-9624-3074-abb1-8e911876cdfe | -14.91231 | -46.86707 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40766e9e-d22a-3bbb-8a22-935d3f27e0e9 | -10.40175 | -50.3074 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b0d7caf3-cf5e-32bd-b10b-9914aa7fc2f9 | -14.90584 | -46.83613 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d21c6e1-a780-347d-8697-58eba5eb1011 | -11.81197 | -45.12188 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4195dfad-199e-3c63-bc54-a0b4445605c9 | -15.17482 | -52.76039 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53ccb414-1fe7-340d-8966-ff252385b2ba | -11.22632 | -47.76889 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54d2b139-85ea-3a9f-aff2-183ee503e8d5 | -11.65553 | -47.02354 | 2025-10-07 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cb93b9c-90e4-3643-b4e0-1ddfc065bac5 | -13.71576 | -48.19613 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a01fd88-c534-3f90-9c7b-f5a566df6e39 | -10.42532 | -50.33392 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56df380b-f4e5-3ac1-bb30-03425553d88c | -12.89484 | -54.74327 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1662364b-f322-39a3-9cd3-903d4d2291ee | -18.28779 | -45.46249 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 041cadfb-00d1-384f-ad99-8012b563de7d | -13.26189 | -47.79231 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 702cfa61-50b5-320d-8fcf-2f47d580b84d | -12.37948 | -51.11721 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README71.md)
