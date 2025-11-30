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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebefc513-1444-391c-9490-bd2ac432f60f | 3.35097 | -51.31366 | 2025-11-30 04:23:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bce9298e-4436-3492-a2cf-6e767be342d7 | -8.03382 | -43.13033 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a7bab248-d22e-32a0-9556-833468a21aba | -8.16845 | -43.20397 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 20ee149c-7de0-3833-868d-94384ee5d3a8 | -8.04186 | -43.1239 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3f2bfaff-30e9-33c9-a54c-075b2fafb7e6 | -2.90943 | -40.3861 | 2025-11-30 04:23:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 17c21112-bbc0-390b-8d39-015b98ef42ec | -1.11987 | -47.73299 | 2025-11-30 04:23:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84b33884-9ab8-3915-a2eb-d17499e5d9db | -7.74126 | -44.18261 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14ef255d-667d-345a-a6b5-ea5a3f16e1a5 | -2.44938 | -47.08117 | 2025-11-30 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7aa21e12-2da0-3a3d-9463-9a2d66e9e0e0 | -1.12297 | -47.73833 | 2025-11-30 04:23:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f1b00da-6254-3a2a-adae-fbf6250a474e | -8.04471 | -43.12818 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 494064bb-b109-34db-8b7e-1ca434f0735c | -2.38921 | -47.61543 | 2025-11-30 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ebd7eba-0f1e-3875-9650-204437f1984b | -8.04695 | -43.13167 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 69819d77-93de-3d6f-b4d4-f0d625c8e324 | -2.44869 | -47.08539 | 2025-11-30 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d466c156-4d80-3213-acc1-7567047009e8 | -3.42085 | -41.00613 | 2025-11-30 04:23:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0f0f97f4-c5f2-3366-b769-88c1c6ee69bb | -0.96107 | -46.79877 | 2025-11-30 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bba7cf49-ce7c-39b9-8e09-42234b359432 | -2.2137 | -48.00617 | 2025-11-30 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fcb9c0b-2613-3b34-9fc6-fd5fa6071267 | -7.91619 | -41.91072 | 2025-11-30 04:23:00 | NPP-375D | BELA VISTA DO PIAUÍ | PIAUÍ | Brasil | 2201556 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9d928475-18bf-30f2-9450-6a4dde02ae91 | -2.3166 | -47.94271 | 2025-11-30 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ea9617d-aef6-37e0-8a7c-e0f8cc278b58 | -7.75074 | -44.18766 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbb1679b-19cf-3b93-adba-4c812c69c075 | -2.44361 | -47.1627 | 2025-11-30 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c485ed53-d6d7-3263-a293-a234de8da7ec | -7.17941 | -45.80966 | 2025-11-30 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad603eb2-8f7f-3ad9-975c-c9325d137b38 | -3.21569 | -41.56615 | 2025-11-30 04:23:00 | NPP-375D | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 09390dec-dcdc-3779-acdc-bde060b77514 | -8.17018 | -43.21571 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| e89820cd-ea80-39a4-bd18-898b350c0556 | -2.30363 | -47.73858 | 2025-11-30 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e91afeb-a00a-38f1-a07d-abadb6165f0e | -8.04751 | -43.12792 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e5e80d5c-6c5c-3172-aab5-fc635adc2bca | -7.74016 | -44.18965 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| baf3cefb-0fb6-317d-9243-f5659ae1a80d | -7.47691 | -41.78708 | 2025-11-30 04:23:00 | NPP-375D | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7599bd47-f531-32bf-ad5d-585897a507f3 | -6.43881 | -38.85781 | 2025-11-30 04:23:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f4d5a250-e2b8-39ae-9998-ee64d0a04b0f | -5.71033 | -45.63375 | 2025-11-30 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fefd4f1-5128-3540-b65b-8240c43c257c | -6.71201 | -41.50174 | 2025-11-30 04:23:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aaab8c1b-3575-3ea5-b89b-c2d3afb482f2 | -0.95808 | -46.79396 | 2025-11-30 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe28f555-251b-30bc-9004-a2f4b5e0e758 | -8.1673 | -43.18848 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a6f2b79d-f03b-324c-8247-158868f0aa1d | -8.04408 | -43.12738 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 720a82b3-7cf7-3b4a-9b49-0d2930f28f80 | -2.6059 | -47.3403 | 2025-11-30 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45bffb2a-b988-37f6-94d8-66578414031a | -2.86474 | -45.222 | 2025-11-30 04:23:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f22f6f1d-3dd8-39fd-8f55-ce880709970b | -7.03799 | -43.74638 | 2025-11-30 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd876fa5-23ae-3fbd-be5f-78a9613a19d1 | -7.7446 | -44.18312 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11a0ccb5-71e5-3677-a82f-74393894da0e | -2.38546 | -47.61481 | 2025-11-30 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf61bdff-290e-3a7b-8c8e-b6741c886fca | -2.13861 | -48.51904 | 2025-11-30 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0353d0e9-a34c-3019-b4b5-b42b6a677ec4 | -3.43596 | -41.31011 | 2025-11-30 04:23:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d99be67-0250-3c5e-9ed8-39b942c43d4c | -2.01546 | -46.92484 | 2025-11-30 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e654d33-bf5f-325e-8241-4cd4fb200e92 | -6.30468 | -43.81083 | 2025-11-30 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3dd15ad5-4011-362b-a1b3-39b81da9581a | -8.16331 | -43.21465 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 4b8b6c26-2fe7-34a8-b1e4-acb2973535d1 | 0.8523 | -50.18897 | 2025-11-30 04:23:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa88af71-d034-373a-a81d-5483e197452b | -7.7435 | -44.19017 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8417abbc-e0a7-3229-bf88-770b0c2b6cc0 | -6.46272 | -41.72236 | 2025-11-30 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0382c08d-488a-3f44-82c1-f58ffc207fbf | -6.30134 | -43.8103 | 2025-11-30 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d85427de-fbb6-3749-8c26-a8ef4bf6279c | -7.74963 | -44.19472 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0ebe5e9-ee57-346b-8630-22673a76c26b | -2.43645 | -45.74008 | 2025-11-30 04:23:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15e183de-62e9-37a6-b47a-3773221e2538 | -2.47437 | -46.28067 | 2025-11-30 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 24ddae4d-acf7-342f-9220-651d4c82dfd7 | -8.16445 | -43.20718 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d4adba74-7ca6-3152-8800-2e1c7b55b92d | -3.44448 | -42.2326 | 2025-11-30 04:23:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d3ebdc34-5015-307f-9752-e69c227eea41 | -8.17132 | -43.20824 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ccd15f4b-b085-37b7-9328-7d63acd76a97 | -2.06034 | -48.26201 | 2025-11-30 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e057abe-7a18-380c-8ea8-341b9407d8e3 | -2.21447 | -48.0014 | 2025-11-30 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 10111901-809b-38f7-9910-b1f321c4be57 | -6.31657 | -43.81238 | 2025-11-30 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83b5506a-4571-3957-aa4d-a1179e6c9153 | -6.30803 | -43.81135 | 2025-11-30 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61a1cdc0-324a-3c93-b628-73be8ff8031f | -6.70043 | -41.26432 | 2025-11-30 04:23:00 | NPP-375D | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3416e4d-d1a5-3c7d-88ef-673bef3f17e4 | -2.14259 | -48.51966 | 2025-11-30 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faa90994-b2be-3e17-9a3b-18453bb5fe0b | -3.21509 | -41.57002 | 2025-11-30 04:23:00 | NPP-375D | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fb5e8f6c-010b-3fc5-a6a7-cfabc9c7d26f | -1.47795 | -47.75585 | 2025-11-30 04:23:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a3ca233-4110-388d-9e92-2b7bde09b7ec | -7.45604 | -44.74945 | 2025-11-30 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95a778ec-8291-303d-a8ae-642784769878 | -7.22548 | -40.27931 | 2025-11-30 04:23:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ed00f97d-cd5a-33ec-8a8b-a5575167ae04 | 3.34811 | -51.33039 | 2025-11-30 04:23:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3855af71-4c38-35f8-acf6-8a57bd255bcb | 3.35003 | -51.34318 | 2025-11-30 04:23:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50f219b7-b787-3b89-b2a1-398f5843c173 | -2.29985 | -47.73799 | 2025-11-30 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d131d23-9cd0-3beb-8ebd-0bad92161950 | -1.79151 | -48.06735 | 2025-11-30 04:23:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1a47347f-ea00-30c5-a2c7-8a6ff000f55b | -1.89902 | -46.44804 | 2025-11-30 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0e03bf1-8d30-379b-9e8f-8d2fbe6b9488 | -8.16386 | -43.18795 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 02d56197-c4bc-3bff-92f4-74db149bfcb4 | -2.8995 | -45.26406 | 2025-11-30 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b918ad05-4a13-37b3-9553-379934196ba8 | -2.2441 | -46.52353 | 2025-11-30 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 434b8328-eaa9-3ac7-b177-bb5ef3bf5289 | -6.90523 | -42.8196 | 2025-11-30 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6e84fad5-fc45-30e5-87e2-a28b0ce29e95 | -2.24765 | -46.52409 | 2025-11-30 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22c8e37c-baa7-39fd-aebe-a6fa0bb5e842 | -3.33335 | -42.49622 | 2025-11-30 04:23:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5bb8c20-7b11-3e12-a414-b122b06470d4 | -8.17073 | -43.18901 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f1d9d5c-3d8b-3c4a-b591-ddf4467b5aaf | -2.51309 | -49.10688 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57fd8fe0-45b7-3094-943c-99b36b3b4da4 | -2.41444 | -49.34743 | 2025-11-30 04:25:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abe557fb-937f-3636-907b-0013b37fed20 | -3.48538 | -45.00772 | 2025-11-30 04:25:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 663289f6-e1b8-38b3-b130-1caf78919499 | -3.62473 | -42.75444 | 2025-11-30 04:25:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 975d5654-5165-379c-bb6f-cd3a54044206 | -12.00898 | -49.27852 | 2025-11-30 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d3bd334-86e2-31f1-9ddf-76c1a562511f | -12.83265 | -47.38797 | 2025-11-30 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3691df5c-ca9d-35ef-81ac-277362fac896 | -12.00749 | -49.26516 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8885574e-71ae-3a1d-aa93-b100555be0e4 | -3.54953 | -43.61594 | 2025-11-30 04:25:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d92bf24-862f-35f7-8755-e2bcf1b8afdb | -3.35359 | -45.55218 | 2025-11-30 04:25:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c936a98-819c-3d0b-9c67-362a62395e51 | -12.00459 | -49.26027 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b2a7778-35cf-3138-9438-e1cd647f637a | -3.58251 | -41.66368 | 2025-11-30 04:25:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7f8c4b24-b0e2-3c00-b5f6-d8213aa0025e | -4.44394 | -44.49275 | 2025-11-30 04:25:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f713956-f1d1-346e-9875-93d0c93ae307 | -4.81642 | -43.08735 | 2025-11-30 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37104567-4554-30cf-aea0-237ded77d789 | -2.96271 | -50.53199 | 2025-11-30 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56dfd076-d52b-3f16-a4bb-60d26dc12efc | -2.39496 | -49.38733 | 2025-11-30 04:25:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61c457ce-196b-3f98-9eaf-51e516646341 | -2.83648 | -48.82879 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f0b8040-d53f-3da9-80cb-1a3ab0fbb463 | -2.70286 | -48.34816 | 2025-11-30 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83c944f1-f3c5-38bf-bc23-054ed9c8c887 | -11.48419 | -48.50711 | 2025-11-30 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1c96c35-2b40-3c42-8296-4297af280e41 | -2.63832 | -48.0303 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcba5593-d759-3975-b583-a1fbdef0bbf7 | -5.72835 | -40.81477 | 2025-11-30 04:25:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14cd3c07-6bbf-39ef-bc78-bd48d35ea2dd | -12.01183 | -49.26157 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e17de747-de1c-320d-b851-f0465ba6edb0 | -2.64522 | -48.03624 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e711c55a-d8b8-32ee-9206-0ac53f7c1896 | -5.74778 | -40.81276 | 2025-11-30 04:25:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a2cc2e15-3f9d-3b23-89b5-45c11adb07fb | -2.63492 | -48.54115 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ceb2d5d-c90b-3347-9c1e-6b118782334d | -2.54208 | -48.35289 | 2025-11-30 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
