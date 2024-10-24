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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 350397cc-6918-3347-966c-554eaf2976dc | -1.48986 | -54.18678 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 23d6c4d3-4546-3a97-b26b-1bb6702af9a8 | -1.2215 | -54.16581 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5d81025-2b7a-3fbe-ab11-ed32dac2bf0e | -1.21812 | -54.16534 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 183cb543-1b6f-34f3-b345-ac99162a53df | -1.21755 | -54.16896 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03c556ca-7f54-3ee4-a5e7-8f84900c9124 | -1.19936 | -53.64129 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28c63a76-beda-3196-8edd-4d77823e84b3 | -1.19657 | -53.63732 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 818c0198-f051-3e67-98c2-ab20dee943ea | -1.1859 | -53.90015 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8170000-9e57-3d51-a02a-deb822ca514e | -1.16733 | -53.50498 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d05f981-6eff-3a7d-af68-57160d9bdfd1 | -1.16678 | -53.50847 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 549cd9cd-f5fb-3d03-aa2f-742de318e83b | -1.164 | -53.50448 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 295a3b4c-94be-3f4e-a953-bd4e73364916 | -1.16219 | -53.66035 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09ee8a90-9ae3-3c6c-97dc-63fd1d67f507 | -1.16067 | -53.50397 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56c39330-caa2-3973-abd3-6fd13bdd5d4b | -1.13404 | -54.05471 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7df3021-584a-33ca-ade2-84036529f2e8 | -1.13363 | -53.78489 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 043bc266-ffd3-372e-ae62-5ba4902226c3 | -1.12396 | -54.16209 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 114a9b4c-ab87-3909-93e5-008c33dc40f2 | -1.12059 | -54.16155 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9671d30-4891-30ae-8066-6b819835424f | -1.09707 | -54.11419 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 813ca801-885f-3def-84fd-6fb3159f5898 | -1.09701 | -54.17973 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d2ceca2-7a86-3d6e-a8f7-7e0703ab0549 | -1.09645 | -54.1833 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b107ee62-d6d7-37a4-8298-5377aa5b47a4 | -1.08289 | -54.10872 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f05a347f-da3f-3339-8c32-49a206624faa | -1.08234 | -54.11227 | 2024-10-24 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c8b8556-9718-31ef-a80e-ea72295e332d | -1.07613 | -53.67221 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 907a848b-2bbb-38d6-8df5-321a27c8013d | -1.07555 | -53.65426 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7af68c83-b4ee-3a4f-9526-18b5ed69aa4a | -1.07501 | -53.65772 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6c4a03c-8764-3a01-a005-f05010ed6952 | -1.07391 | -53.66468 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9e0e720-c6dc-3993-888d-9696867d6c7b | -1.07335 | -53.66818 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e478aa1-5761-329a-b5da-ba2df1a9783b | -1.0728 | -53.67168 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd2c1deb-04d7-3080-87c3-aff2ae1b09e3 | -1.07057 | -53.66416 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f3ad9e1-8903-3311-951d-c0ea7587a0dc | -1.07002 | -53.66766 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5db085f-0197-34b3-aa6f-e41b786830ba | -1.06724 | -53.66364 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3df3ac2-f7af-3cdc-8770-4972495521fd | -1.065 | -53.65618 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aed40b20-0466-3d6c-8f4a-4fa3964f1bda | -1.06445 | -53.65965 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19932f67-b4ca-3e4d-a999-23caba7aa372 | -1.06167 | -53.65565 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85d72793-ae84-352e-807a-4a3f8c9aaab1 | -1.06112 | -53.65913 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd4f3f29-10a3-3c80-832b-11ec6d71ca5f | -0.87756 | -53.68748 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31f7fbd8-98df-3c05-9e35-4872901a04f4 | -0.87422 | -53.68701 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2368c9ce-bf61-3ac2-9c6c-785d2a3b0101 | -1.80939 | -53.69767 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bdc384c-beb8-30af-97ef-c5b8b58d2003 | -1.66358 | -53.68207 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dc4220f-e77e-35e7-8da0-cd39d4e83c44 | -1.66303 | -53.68555 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5db9d5ea-a8a9-3fc8-8935-7b611d5b0467 | -1.6597 | -53.68502 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a3a600b-e355-397a-81d1-f398d7fdab76 | -1.54927 | -53.7 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e828e53-edb2-394e-a82d-f2ef415da701 | -1.54594 | -53.69947 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8611d77b-6393-3e13-a194-a533bf38d735 | -1.54261 | -53.69894 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 570f4ff0-0342-3ce3-b63f-cd4120a7ca2d | -3.67646 | -53.96508 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2c8d695-eb03-33e5-aedd-ec081a6ea135 | -3.63547 | -53.96574 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8357a3f6-14dc-3c6a-9d13-ee96f5ef9cd6 | -3.63492 | -53.96921 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 402bf0c1-354d-3746-8478-fc9956a2dd8b | -3.63269 | -53.96175 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2dea22d-a258-315e-aaa4-220fe456b05a | -3.63214 | -53.96523 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e65c54c2-e623-3fd9-9210-4bfc318f2aa3 | -3.63159 | -53.9687 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff3f0bc2-8993-350b-8541-a34a5d647e72 | -3.58958 | -53.7848 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 15c827ab-e7b1-3dcb-8734-b6175ed6b77e | -3.58626 | -53.78429 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc49c49e-2ea8-30ef-83ab-c9a71836e46f | -3.58572 | -53.78775 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c111f90-34d1-3b5f-bcba-504f05175813 | -3.58294 | -53.78377 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39048759-5f81-35dd-9cae-778e72c97087 | -3.58239 | -53.78723 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ab717c7-1850-3d88-bafe-0478acc3be29 | -3.57962 | -53.78326 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ef7ac72-db15-3637-bdbe-9c7142d797aa | -3.57907 | -53.78672 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05e7426b-a56e-36a8-897e-a9df859e3767 | -3.26237 | -53.77943 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24b1211f-a57a-3c8c-b6c9-04752f78c132 | -3.24721 | -53.94034 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 591a8b36-5e51-3353-a861-fdbdcc137892 | -3.11048 | -53.73082 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0157cfd7-b61c-396a-9105-28b2e30b01a4 | -3.10716 | -53.7303 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75b03eb3-50d0-3b08-9c67-b24e0f25ee93 | -3.10106 | -53.72581 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| de70cd36-e5d6-30ae-853d-82e96d43dc1c | -3.09828 | -53.72183 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d4dc671-5c9a-38f6-b392-23647820e883 | -3.09774 | -53.72529 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a5c0b036-8ccd-322f-b3a2-52c802e935a3 | -3.09579 | -53.72161 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a60b6ab-daa6-3abc-a316-765626af0307 | -3.08184 | -53.8257 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82d910d9-0d7b-33b8-a31b-dedb5091f8d7 | -3.08 | -53.82204 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32fd9971-b72c-3371-bc6b-b7e86c25daa0 | -3.07945 | -53.82551 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 928872a0-dbc2-38dc-8329-50ea55bd005a | -3.07891 | -53.82898 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 864d3661-b3f7-3edd-9a13-5987f0e97208 | -3.07667 | -53.82152 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37301dbf-f437-30df-bbd7-5d803fd2abf6 | -3.07613 | -53.82499 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ae6a01e-8b80-364b-8297-9176b0f86967 | -3.07558 | -53.82846 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c8557dd-24b7-3c10-a02f-7720dc9ea546 | -3.07334 | -53.821 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f35ba7fd-e84f-3686-8713-522e98ebeed1 | -3.0728 | -53.82447 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26d9a3c4-64a6-3300-863d-e2f20fab0ac7 | -3.07225 | -53.82794 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78dbb234-91bd-3a06-97c7-c530761828c3 | -3.07056 | -53.81701 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d7343f2-46af-35f0-96ee-bb94b47242c0 | -3.07002 | -53.82048 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dad25a3-d066-3e31-8c1e-2e57257116e9 | -3.06947 | -53.82395 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c657f7ab-debc-3551-88f4-ebe81698ff20 | -3.06893 | -53.82743 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9b41721-fd20-3d28-b78b-9365053b103f | -3.06669 | -53.81996 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a83413ff-9b2a-38c6-b432-d06227e5f4ef | -3.06615 | -53.82343 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27918c82-0794-366c-87c7-e3662e36d254 | -3.0656 | -53.82691 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f6fa46f-ac4c-311a-84ed-bbf900a44bb2 | -3.05027 | -53.90255 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42ff2b22-f479-315a-9b85-3e1754f2e99e | -2.99457 | -54.10418 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ae6afdb-6ca5-355f-88d1-2cdc7cf92d10 | -2.95727 | -54.05903 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bad8f77-365d-3a7f-b0ba-acb8a20dbbce | -2.93567 | -53.91974 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e3638d4-5eb3-374c-844a-3c3e5f42c57d | -2.93513 | -53.92322 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb754c61-397f-3dff-8241-e544d0a4f23d | -2.93344 | -53.91227 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42cf6b5a-ab43-3575-9bb9-2ee2d77b1b41 | -2.93125 | -53.92617 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bc947ce-470e-35a6-a1fd-9cf86c31e502 | -2.93015 | -53.93311 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5bf5d8e-9bf3-3855-859c-b1ad8bb2f43f | -2.92792 | -53.92565 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd5bee24-1c0b-39fc-b7de-1af8496d761d | -2.92514 | -53.92165 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63e427a7-bf0b-3490-9d38-5097d086bbcf | -2.92404 | -53.9286 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9beb0666-2578-3cdd-9bbb-66343d831711 | -2.92349 | -53.93206 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fedb26c-38c2-3d4b-b823-c7f6b61e0732 | -2.92126 | -53.9246 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5274c1f3-5e71-31d0-9800-a803777c0d8e | -2.92071 | -53.92807 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cb71328-4d9c-3e35-b36d-e529be08bfe5 | -2.91793 | -53.92408 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa3179cb-7fbb-3ce0-8db0-f6b5312eb722 | -2.91738 | -53.92756 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e8e1623-5b07-39fc-a4b6-eade8f1e5394 | -2.91683 | -53.93102 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22e1575e-4399-3e0e-b281-a0479dc1cdd8 | -2.91405 | -53.92703 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85bc5b98-3f7b-3620-8ff9-9b6c23df4fa7 | -2.91296 | -53.93398 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README70.md)
