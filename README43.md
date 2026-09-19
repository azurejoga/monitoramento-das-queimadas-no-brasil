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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29fb0eb1-c6d0-32a0-8ee9-a8cc8083dedc | 1.28193 | -50.86523 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a274c96-d28e-37a0-9ca1-61d6a4ad2591 | 1.13697 | -50.99565 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 479ab68f-bb5e-3ac9-bc70-d06b9cf245f8 | 1.25059 | -50.97432 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfa2c4a7-193a-385c-bdd1-7e9d67be38d6 | 1.219 | -51.00606 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97e926e9-cc49-3da0-97ea-c255febaf929 | 1.2221 | -50.99662 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4b76a2f-60b2-36aa-9513-dd3c03b3557c | 1.25635 | -50.75381 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0737fbb3-d511-3be9-967c-bda461a79a3c | 1.25178 | -50.7564 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d48b98a-7391-3d51-b5e8-9216164f0ec1 | -0.75537 | -48.70592 | 2026-09-19 04:36:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f90699d-9048-3a3e-90eb-9beb526c82e0 | 1.25643 | -50.98236 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7034c184-c79d-3eb1-b77d-aa0144ca45b8 | -0.52468 | -49.1548 | 2026-09-19 04:36:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e4cb4f6-0105-3c51-b76e-08db407514b3 | -1.63945 | -55.15372 | 2026-09-19 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c061daf1-c9c8-3de3-9e91-5fb77b3a468e | -7.76317 | -46.74006 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b926fc68-4c1e-3265-a745-5d5959f8f01b | -2.82734 | -50.47663 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c75423e7-d040-3ba5-94de-070eab10d72d | -7.85674 | -44.8725 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 707bb099-238f-3884-930f-b37381e3d95b | -2.62502 | -49.11018 | 2026-09-19 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 085a895f-dedd-3cee-9b83-8a4ca0066dd2 | -8.36637 | -47.22346 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77519f26-4a85-3875-bb05-30436076d657 | -6.98268 | -42.18157 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 489df7fb-4d8a-3d08-82e3-add3b00d21c1 | -7.64356 | -46.10625 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d4d4991-80fb-3b94-a837-9120d688030e | -7.85732 | -44.8688 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c462e271-45aa-3372-8255-dd7db564cc99 | -6.37167 | -58.29304 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64dc6e12-b6a4-3157-a0a7-fc0c8e7261f9 | -2.82966 | -50.46246 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 474ca31e-bb30-3b5b-80af-bb88d0548d28 | -7.00662 | -49.75801 | 2026-09-19 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c659c7f9-a3c5-3407-9705-240f87e9b809 | -5.73615 | -52.23841 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24a44770-0f7d-34b6-ab39-9e452f1a2f15 | -2.82429 | -49.23849 | 2026-09-19 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99b6025b-e97d-380b-a723-f1ca109b1723 | -7.81811 | -45.09935 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bc02521-6b41-39e9-bb41-5932b774e2c3 | -1.19694 | -54.21592 | 2026-09-19 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e372e1d1-b6ca-3dcd-b783-032b8641a614 | -3.14783 | -53.9357 | 2026-09-19 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 401c3e13-c0e9-31e0-9f71-3e8a9e083acf | -8.67205 | -45.43861 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adc0cdfe-5d56-3f66-a7af-f2a6bdb249b2 | -8.35643 | -47.53188 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6983de63-ea92-39e9-9491-b11148545c12 | -8.24397 | -45.61463 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cd08b14-6568-3a67-810d-73b1970dbeac | -7.02285 | -44.64833 | 2026-09-19 04:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5ef85fb8-d53b-37fd-9781-2845af36fef8 | -3.14833 | -53.93269 | 2026-09-19 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e45550cf-9c95-35b3-9ec2-3cfe685999b9 | -6.98967 | -42.18748 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 50a8ba1f-40ba-379b-8f52-689461bd6cda | -7.12575 | -42.07724 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2a00206-24ad-3850-85e4-5c498ba65713 | -8.38361 | -47.20108 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ed00250-b25f-3d4e-8d4d-34a172e9dc1e | -6.41583 | -44.98425 | 2026-09-19 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4877c65-eb80-3bef-80cf-5232f6c97320 | -7.60965 | -45.43264 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ee17bbf-14ac-3ac4-a775-bb0c2725d34f | -1.48958 | -54.97327 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b7c0330-6bf1-321d-8235-c14e3c77713a | -2.95668 | -50.31965 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00a89784-720e-358f-8f8b-589f6b7fb389 | -7.81634 | -44.95302 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baa0e25b-7ae1-3b15-a44b-ad6812f1f5d5 | -3.72501 | -49.04226 | 2026-09-19 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95a9b080-1dc5-3398-84c8-b9b6cc7936c9 | -5.84201 | -49.87087 | 2026-09-19 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6f67b966-7cc4-39c2-aa30-eaeffbe475d5 | -8.67324 | -45.31968 | 2026-09-19 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5aea955-f55b-3b68-a56c-b7c8f404f04a | -7.60573 | -45.43568 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fad9275-7f4b-3cc5-9940-c205e7e2631a | -6.67102 | -43.63588 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3bea70ac-06f2-3d08-8c3b-37ba07048db5 | -3.01457 | -52.49802 | 2026-09-19 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1469210-c070-3cbc-96cb-a62b313f4bb9 | -7.36234 | -50.32893 | 2026-09-19 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 732cc1bf-8db0-3f35-a55d-7217ce268a68 | -1.19583 | -54.22254 | 2026-09-19 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03d9a682-f194-3498-b274-33be1de5b1ab | -7.92561 | -44.82975 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f80f998-30bb-313b-b4d7-bf6ea1d8eb2d | -6.20521 | -45.34185 | 2026-09-19 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2befc69-1118-3935-b318-e9287c6e3f22 | -2.82041 | -50.46821 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b27c7e74-16c7-369c-8479-cdaeafe3b244 | -7.86073 | -44.86935 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bc234a5-799c-33f0-aedf-5f44d3fcd4ea | -7.64689 | -46.10678 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe47a7b1-ae5a-30ef-8849-030cc5f379d2 | -7.85617 | -44.8762 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1ac04caa-cbb3-3a71-ab38-259dbc883abf | -4.05996 | -56.24831 | 2026-09-19 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4228f54a-9756-3897-972b-61fe83e9e117 | -8.4934 | -44.55587 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cda4899a-7adf-31a3-b032-bdb408bd3fdf | -7.444 | -44.7001 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72c25e36-36cd-354f-ad33-62dfeec66724 | -1.21891 | -47.71457 | 2026-09-19 04:38:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14c61db6-019a-3098-b497-cd52bf93ac11 | -7.22396 | -49.64107 | 2026-09-19 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a37a7ada-46a9-32f1-91da-3661207ef0fe | -7.32607 | -45.32629 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b50024dd-239b-3314-a497-dee8bd9ab439 | -6.99421 | -45.67768 | 2026-09-19 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 225cf097-914e-3dec-8402-d2bd68d81a5a | -2.93802 | -51.06649 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cf12454-fe27-33c2-9c10-11084faea4b9 | -2.63994 | -54.69114 | 2026-09-19 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ffaa6b5-b70c-3be0-a130-b39e525d6928 | -8.47221 | -44.52161 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b65c79ee-4347-393a-8a96-9fa6d2eb51e7 | -7.32159 | -45.3329 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f966c4b-0b43-3068-8390-20b4a6ceeffd | -3.21003 | -53.95387 | 2026-09-19 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e79a7bc2-40cc-3f2b-8c0b-29b2fdfac1ac | -6.98796 | -42.17268 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f46b73f5-42f2-3209-88c1-7bd5602dda69 | -3.45397 | -50.60699 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f95f6fd4-a2f1-3db0-88f4-8c1c562c5719 | -8.22379 | -45.61147 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80a7317a-8484-37f3-a0ec-4c80445022d0 | -3.0327 | -48.4108 | 2026-09-19 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 39cbf426-ed94-3110-989f-dff514ccc5b6 | -7.68687 | -46.11311 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91dc6b00-e4f6-3d8a-a34d-17848aec8e76 | -2.96616 | -50.33702 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43574438-fa21-3a03-bcfc-b52145423be7 | -8.45518 | -45.71367 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32ad23e3-3f28-30ae-9656-edd449bdb756 | -5.76628 | -57.45791 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 68945837-45b3-3329-a6e6-26f01d4de1c6 | -4.5001 | -55.48903 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ffd89be-004b-3b39-9fb2-d66df1ba03f2 | -9.00347 | -44.91478 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b0a43c0-d0a7-34ae-9d45-38ccb2edacac | -5.99819 | -51.80105 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffaf1707-4348-30da-a7d0-9dc4a6e138fa | -7.76318 | -46.76144 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| feda5036-cd76-309f-a205-0aa00556e7f3 | -9.00634 | -44.91909 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e5d60bc-cf8a-3eb0-8742-97739fd1c816 | -4.55105 | -54.93302 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a684d12-9782-3eec-949c-6cc0b604302f | -6.36628 | -58.28653 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 470a4023-4363-3c92-9439-0534202ddcee | -1.21906 | -55.72326 | 2026-09-19 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eec0a3a-92f2-3da2-9b91-52bccb759889 | -4.82187 | -42.87608 | 2026-09-19 04:38:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ab05af17-e479-3a08-8992-81c42ce89b38 | -7.86132 | -45.18064 | 2026-09-19 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e7a5ccc-b374-3fb7-b1c7-9b91732d6163 | -8.47026 | -47.01394 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6867d02-b649-3b62-a8a9-672b7da9c6e6 | -6.32172 | -55.28115 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06c809e1-9730-3a6e-a43e-b01247109a29 | -5.62057 | -45.25042 | 2026-09-19 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3d0c89f3-2862-38ed-9203-0d286ee9572a | -7.64634 | -46.11027 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a54855d1-4b17-30ae-a276-9742491d5d25 | -7.6874 | -46.08812 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 354c6614-f57c-3a68-b306-6fdfd236e1ba | -3.36179 | -50.45928 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3938d8e-5dbc-3b05-8cba-ed0451b80bd5 | -7.49804 | -55.0105 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1daf469c-3684-3692-9221-600a574c140f | -3.7249 | -54.65025 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98f0d5a4-646c-34db-8e80-459fc6b7b6d5 | -6.9389 | -43.10567 | 2026-09-19 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 526f81d5-059b-3c6d-af88-76b9bf28ae74 | -5.74535 | -57.58266 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61119a8c-fa7e-3d65-a732-635795713fd2 | -3.73078 | -54.64774 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36afa912-1eec-3749-8b9e-dcd317777321 | -7.81691 | -46.63792 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ded56b5-4bfa-3a71-ad8b-4b3f8b251d44 | -7.19773 | -44.09823 | 2026-09-19 04:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a372466-b986-3522-add2-906f6ed9bc6d | -8.08711 | -50.96388 | 2026-09-19 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3ddebcb6-de7e-3c9c-8e39-14e7887d332d | -5.7671 | -57.45349 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b753e780-1aab-3d77-a060-856a1d1d0613 | -2.82388 | -50.47242 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README44.md)
