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
| 90c70dfe-dbcc-3d7a-8f81-f31fdd204909 | -2.83552 | -59.24645 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b03f5e1-24ab-300c-b09d-fa895b76f9a4 | -3.04624 | -54.22399 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69723a87-b546-30c3-9ac5-c31229ee0c01 | -3.13522 | -59.01819 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7951bcba-cdae-33c1-846d-aa1dd842fbbb | -3.08839 | -54.16995 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6613ad44-35d8-3e90-be5e-a242648132ff | -4.46319 | -54.97243 | 2026-10-06 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95881890-e0ab-3292-a677-9546713826d1 | -4.12907 | -54.9135 | 2026-10-06 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fd0a9b8f-f365-3ea9-9530-e0e99f9ddb14 | -2.77897 | -54.11243 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef780c91-2e46-3e6d-9813-b673260ab115 | -3.3756 | -54.1019 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad33c208-c9cb-3adb-b2be-30b884197eca | -2.99096 | -54.10815 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac8aadff-d819-3b0a-92ff-0721851311a1 | -2.87611 | -54.16402 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e70ac01d-e3ba-3a26-acdf-4786be50468f | -3.68589 | -55.95005 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a1e790e-f1ce-3c97-926e-a5d5c0bd661f | -3.67438 | -55.95102 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 070e0890-133f-3552-ae06-ebb1b61a31f3 | -2.86713 | -54.13686 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c08eb9b5-ad16-3ef6-898c-4a0c0607c45f | -2.78811 | -57.68273 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa187b05-b8c3-3451-830c-d21c71abdbb2 | -3.68012 | -55.94912 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 81941ee3-cfb0-3c04-a5ff-92d6c8d4b576 | -3.49665 | -54.63034 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00c7b6fc-17d7-3324-b4d9-a049d6e30fe0 | -3.10015 | -53.72657 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5957bfbb-49e2-3956-b9eb-f4beb245ea13 | -3.06683 | -54.17394 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19d3bede-62e1-336a-83a1-0fa8415921fc | -3.69117 | -55.95751 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1ae5e993-5279-34b3-9c6a-271a7cf74633 | -2.90247 | -54.08388 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 330b04bc-cad4-3c6c-ad92-40fc2699944f | -2.77932 | -54.10683 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8f3f6e5-2ff6-329e-923f-f1bfd61a1506 | -3.04857 | -54.20839 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fbd289de-6fa7-35e4-a5dd-ed099d1dff52 | -3.67496 | -55.94701 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fe8d3e1e-8726-36d4-8ea8-52e219d793ed | -2.77332 | -54.1062 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba0c1728-59e7-33ac-a4bb-10bc6c49dc26 | -3.49735 | -54.62555 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67622fc2-993a-3556-b182-a631497839b2 | -2.99017 | -54.11336 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61e0d765-9214-358c-ac72-7dfe3b6787d2 | -3.09809 | -54.18403 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6785b580-b96d-3141-9a70-3f7637b180de | -3.08303 | -54.24009 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fc8f4493-220a-3299-bce8-503636255977 | -3.07965 | -54.17589 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e63fe041-1107-3212-80e4-d19cbda287be | -6.48317 | -62.86258 | 2026-10-06 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 940ad74c-2eaa-374a-adaa-553abc8926bf | -2.9888 | -54.12444 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1679e96-aaec-3422-8359-20d0b0bde756 | -2.07128 | -56.86182 | 2026-10-06 05:59:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2c456911-9920-32fe-892f-bfd697b36ed5 | -2.90235 | -54.0781 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed3e36ba-dae6-30c6-ae71-02fa089d36c4 | -3.05341 | -54.21976 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2dd177a1-fe5e-3cab-a610-4be6b25700d8 | -2.87278 | -54.14284 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a888717-ccef-3bbd-a17a-394b123aa9ff | -2.98241 | -54.12315 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dcb5340e-1421-31d0-a8e0-82b9c82a36cc | -3.68072 | -55.94514 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 26620581-e4bb-324c-8420-3da5d7c7e003 | -3.09887 | -54.17893 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ca8df77-e3a0-3dc8-9f66-acaec7c459ca | -2.99106 | -54.10877 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27be0f4a-b6fe-3d6e-a4d3-8bf4241b29f7 | -3.68017 | -55.9519 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5a530216-4688-34ef-9de3-080063de2635 | -3.16914 | -58.63073 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 060a6291-bb06-362a-be01-ebe3bfbd5c35 | -2.93896 | -54.14824 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3786df4-fc5d-360c-a65e-365828f21fda | -2.98063 | -54.13291 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fce9eb15-50bf-3f0e-8a51-ad77155e4cc1 | -3.09478 | -54.17112 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ccfded4-3f67-3aeb-80b1-e591654b49a9 | -2.78521 | -57.66719 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4cb5450-eeff-31c4-96ea-7f78edb99e05 | -3.06762 | -54.16865 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 256c4de8-4082-3273-b965-9d0f45c0546f | -3.09245 | -54.17798 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1054508-61c0-3963-a9df-14ced4b9f290 | -3.63143 | -55.28357 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 847d4a2a-0af6-3a61-9c7f-e6230c760b01 | -3.23206 | -53.86936 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c98de21f-b340-3088-8c57-274e8a55ef91 | -3.22863 | -53.88021 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b958332-e6df-3037-bb4d-126477124c47 | -2.13435 | -56.69841 | 2026-10-06 05:59:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| de9f4933-a8b1-3379-9d9d-07a141a54abd | -3.23021 | -53.86917 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 019af6d8-7806-3917-ad79-09edb69a5b31 | -2.77482 | -54.09587 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b5107aa-8b48-3645-b50a-ef3be1a9ad88 | -3.07405 | -54.16952 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb1f8712-e89d-3304-b838-3552a17d6f44 | -3.88558 | -55.79937 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1becccfe-1eba-3b46-9248-d5f423dd5feb | -2.99659 | -54.11439 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bd88d58-684e-3107-8362-ae2db7b38d76 | -2.94616 | -54.14392 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51ab3a00-d60d-368d-9a9e-0dff6735b4e1 | -2.86561 | -54.14688 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e287c5bf-2f36-3cf5-b1a5-fe51c9b00f56 | -3.06842 | -54.1633 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba1d2c0f-c5ac-3cd5-84ea-bfcf1b5106c9 | -2.32411 | -57.98368 | 2026-10-06 05:59:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 102217e3-74e7-3101-953d-783b96af6172 | -2.9526 | -54.14471 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82e2a11c-fafe-3fb6-be37-9dcb66b0fae2 | -2.98539 | -54.10252 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 665eaa92-9bfc-30fa-be30-9246f2ec3325 | -3.37959 | -58.19695 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c21c0295-01b9-3d98-931a-cdc18963d435 | -3.08999 | -54.15888 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc386934-cfe4-333d-b54b-afa9175e6a05 | -3.07433 | -54.25438 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5ba1e8ad-ec9b-33f1-bf67-5652f01c7df8 | -3.38371 | -58.20327 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8b35391f-09ce-3bde-a066-27673bc1c587 | -3.02848 | -53.89594 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 19589d65-337c-3ee4-8129-8d30623b8397 | -3.06245 | -54.24656 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e56868f3-8321-31d4-94a9-6fbb195265ba | -3.08761 | -54.17536 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e657c5e-a5c7-3fb7-9c70-aea81ac232ff | -3.09493 | -54.16164 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e5119edb-5f05-304e-a7f2-00ddcc974a6c | -3.67553 | -55.9403 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b08fb0c3-5b87-3fb0-9208-03273a7ed0bf | -3.37481 | -54.10726 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a560d9c-4400-3e50-acce-2b15ddb6ff47 | -3.0233 | -53.89482 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d9552a5b-169e-37a0-ab15-8475e843b4a2 | -3.07587 | -54.24421 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e0fa47ef-1f2b-3cc0-b588-9cbc8dae794c | -2.99031 | -54.11401 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c3aab82-551d-3c65-ab88-7e063c5a78d6 | -3.08146 | -54.25041 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b3442acf-0cb1-3ecc-b480-d9fc8919cb9c | -2.77526 | -54.09037 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52162322-62b2-3503-8ba8-6996e8d8b0c0 | -3.07786 | -54.2429 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2567b547-7345-3f47-8be3-d4caf76f73f0 | -2.79437 | -54.14154 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 598298e3-9f43-39bf-9fe7-5b9fb13eeada | -3.06136 | -54.21038 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 525e8a22-8bfa-3e02-a632-7e4f43b14b9b | -2.90154 | -54.08335 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c2728e9-8257-3f42-ae2b-d6d8a2eca313 | -2.87916 | -54.14399 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f8ca826-9d8d-3a01-9fa0-8d67690d1272 | -2.78199 | -54.09167 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 925861d0-5a36-3cae-a22e-65e5caa801a1 | -2.8756 | -54.13326 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 456a1ed4-d441-3aaa-b6cc-46b117f82d6e | -3.50503 | -54.61697 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a55b7d0a-baa8-3a12-b980-ddae5519ba71 | -3.9548 | -56.05307 | 2026-10-06 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 649e5068-007b-3504-b2f5-1796190cdfad | -2.78122 | -57.67173 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02b9e725-7369-31ec-ae57-fb677d0d5357 | -2.98859 | -54.12376 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11801b04-2b64-300a-8e46-0312b7374483 | -2.78447 | -57.68425 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec465b3e-9403-37eb-a6d9-4f464c6cab5a | -2.77973 | -54.10723 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5187673-e8c2-3dd9-901e-9812872806db | -3.67892 | -55.95702 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dd68cf02-242b-34f3-8c93-21d29ea0a600 | -3.68537 | -55.95674 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7ef48a7-ec16-394b-af53-39c050cc38b7 | -3.62541 | -55.28263 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a0d1ca8-dff4-393b-b83a-adbb35220067 | -2.78076 | -57.67467 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1291635-20a5-3201-9bf0-58015ee35a77 | -1.6117 | -55.1188 | 2026-10-06 05:59:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da012e6b-037a-3cd9-b69a-78e57ca11118 | -3.08863 | -54.24623 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a0cb2bad-3c33-3f7c-931e-91ef402ea760 | -3.87843 | -55.80731 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43d7692c-a393-3f97-b81c-d27c4fb05826 | -3.10264 | -53.70969 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec6b9884-1b24-3746-b227-1d9c4f01db63 | -3.34835 | -59.49372 | 2026-10-06 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d841041-00ce-3bd8-bffa-b1c26b4143f0 | -3.67434 | -55.94825 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README71.md)
