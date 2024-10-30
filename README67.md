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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30f85b52-2df8-328e-a279-d5a6f16be4e6 | -1.17499 | -54.07392 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27b17cab-c84e-311b-a42c-5a4c54262a70 | -1.17421 | -54.07883 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22545886-dab7-3526-b8d4-79418714a261 | -1.1672 | -54.07303 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3694557-78e5-385f-92f4-d8f872f7eddc | -1.16332 | -54.07247 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cab7df76-2307-3ea7-a16a-814d48b66a97 | -1.15017 | -54.05552 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54b23e96-f73e-3267-9333-23079498e9c7 | -1.14631 | -54.05489 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96ab0af1-d11c-32b6-bc35-4c516cd88eff | -1.08779 | -53.65075 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f8698eb9-48e7-3c54-a27d-7632befd6473 | -1.08706 | -53.65525 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 600fd2c1-f00a-32b1-be0a-40712bb10ece | -1.08633 | -53.6598 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51295d4f-3418-3483-8415-ddf9d4e78d4a | -1.0838 | -53.65228 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55e5ab2f-6826-3ec4-a453-a22aceef7a23 | -1.0833 | -53.65458 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3535824b-6e14-391f-bf70-4df6f784dc42 | -1.0831 | -53.65678 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3367e873-7ba6-398e-b78f-e2969f911539 | -1.07863 | -53.66064 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eea51d9a-156f-39fa-8812-1b42cf6529c2 | -1.06727 | -53.65901 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c383338-162e-3ac9-9771-f2e4dea4e820 | -1.06349 | -53.6584 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 603bac24-ec92-3edd-bc67-c43a28f74539 | -0.98671 | -53.70221 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bc251ed-83ea-3b88-ae19-0b431e3aaaca | -0.98598 | -53.70676 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6130e947-6bfc-3032-a904-fd4afe292a02 | -0.98219 | -53.70618 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2d5e59b-c09f-3915-a1ab-b421207935e9 | -0.98147 | -53.71064 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5a674b5-e52f-368a-bdf3-e9821e69e4f9 | -0.97769 | -53.70995 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84758ae5-c30b-3a34-a09d-45afae45a3a6 | -2.24225 | -53.72179 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 574982ac-5192-3be1-b86d-5ec1f7aa7d4f | -2.24155 | -53.72625 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a31495f5-bff6-33dc-9eba-609d2d6f0c07 | -2.24085 | -53.7307 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4c3b0724-4994-32f4-b8ae-825d070e4de4 | -2.23782 | -53.72564 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a9145e9-f2d0-3658-9117-99d387a1048c | -2.21568 | -53.67213 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b31c0f3-3d81-36be-b749-076c5b4dc801 | -2.21497 | -53.67656 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e19b80de-6d96-3791-a813-091c516b7a48 | -2.19864 | -53.68305 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c614e11e-2a7e-393c-b0b8-545fefda0d4b | -2.19793 | -53.68748 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f674042d-5a52-3e8b-b072-3b118aaef5ca | -2.19061 | -53.70927 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51a04128-1967-318e-a84e-d4c91a774a9a | -2.17841 | -53.66618 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c82879f5-eb65-391b-9e2d-3cdba72d8e97 | -2.17539 | -53.66118 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b8db6bd-e40a-3ee2-9515-aa81f2c4a64b | -2.17468 | -53.6656 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6724f99e-ad4f-35e0-8d9b-1bf17e738cb3 | -2.17023 | -53.66944 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48acfb77-7ff0-3fbe-829a-0c4397908bcf | -2.16722 | -53.66445 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78f31680-f829-362d-89f9-1c4a4df9b9cd | -2.1665 | -53.66888 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04d4828e-482e-3eac-9bb7-d07654b71d0f | -2.16578 | -53.67333 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a62ebbf-387c-3053-af2e-b82e84222791 | -2.16348 | -53.66388 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ec924ac7-252e-3c0e-8e7f-ab1a8b8a6ffe | -2.16276 | -53.66832 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b8469f9-2f4d-360b-ad6f-daf9bbee1bcd | -2.16192 | -53.66564 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b3db4d3-14ad-3f89-a9bc-984b0651f32e | -2.16123 | -53.67009 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dea3ee4c-42fe-341a-b149-6a713692cc4f | -2.14535 | -53.64952 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8001743c-510b-3802-80c2-b4a8feda21d2 | -1.68776 | -53.81096 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ab12870-9181-3777-a1ad-40e2d660ab26 | -1.68399 | -53.81027 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8be6e9ea-4aaa-3678-b967-1c8b52f4d596 | -1.50293 | -54.85915 | 2024-10-30 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8529fd7d-d810-37e4-98f1-acac3f8acfd1 | -1.45674 | -54.06823 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 67fb584a-50c1-3b7b-8b11-18c3ed236790 | -1.45598 | -54.07293 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0c82668-3b81-30bb-bed4-902c44ce70ca | -1.43431 | -54.20694 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de71f102-6a65-3cdb-8790-6f3f18b41e6c | -1.43043 | -54.20625 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c768fbee-e4c8-3771-a21b-b3d0c982d133 | -1.42941 | -54.2089 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7a0dec3-7944-378a-a154-8342ac7b6dca | -1.21844 | -53.3835 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b910d94f-cd73-323e-990f-807c602b300b | -1.21472 | -53.38295 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b80e8a0-29b0-3684-aa13-50f185efbd92 | -1.16502 | -53.38422 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b10a6b3-acf3-3ba3-95af-6d580831037e | -1.16432 | -53.38858 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bf55f02a-d9de-3268-943d-f95112fae240 | -1.1613 | -53.38365 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19c0834d-121d-3cff-8952-ded24024f641 | -1.16061 | -53.38797 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7bfae235-70c2-3f8c-8a2c-7e6c6b345d23 | -3.59544 | -53.78698 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 958950f0-e870-3955-bf01-58231c8dd5a8 | -3.59245 | -53.78212 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 009fd16b-7083-396e-a6c1-978aeecac995 | -3.59174 | -53.78649 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0207da6e-3808-33f1-9741-e3dbcde634ce | -3.55581 | -54.48383 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f64170c7-9fc7-3940-b2fb-77677838d63d | -3.546 | -54.73851 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1ff71fc-12eb-3aa6-9ad4-0978459b0555 | -2.74838 | -54.03511 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53759383-54d9-37a9-b0f2-5ebc40dec9d8 | -2.74835 | -54.0365 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdee7df0-cb69-3da3-8442-3b6ca3c1e54a | -2.68656 | -54.9622 | 2024-10-30 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b22fcdcc-ca8d-3d81-8136-19ee456d8504 | -2.57908 | -53.98383 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6777134-6b32-31ac-b136-0131b604e89c | -2.57531 | -53.98322 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ba09663-7461-38c6-9eef-86aca1a94961 | -2.56488 | -54.02377 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d136374-27be-359d-bf9c-8f54aed71140 | -2.56333 | -54.0094 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2d69a804-2aa2-3b2b-93ea-261ab4b0ec6a | -2.56184 | -54.01858 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ead431e7-2d15-32db-bbd0-e9b8347a93e8 | -2.55954 | -54.0088 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 696762d7-0c9e-3639-a429-0e73a7eb742a | -2.28005 | -53.77665 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a7e0c38-3d06-3f80-b2bb-b32df35b365e | -2.2763 | -53.77605 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da808e9f-28e5-3a12-88dd-31b4216846f8 | -2.27255 | -53.77546 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05302d21-7928-37dd-aa38-ef8d1758c0ea | -2.26137 | -54.79112 | 2024-10-30 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d746262c-53d9-3324-bb12-a5d30bb653dd | -2.25505 | -53.71781 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db1213e7-b639-39d4-b37a-e34dcc7154f1 | -2.25416 | -53.71915 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c12c42a9-6131-3ace-8439-db0c068db0e8 | -2.24599 | -53.72239 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 064570c7-4808-3fb5-8984-3de3a3abc994 | -2.24529 | -53.72685 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b602fcf7-b582-3ea3-8886-2294213510b0 | -2.15902 | -54.6271 | 2024-10-30 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3d511d8-264e-384a-b9c6-161d4e3e1c5c | -3.07866 | -54.16516 | 2024-10-30 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 54ad15aa-e8c4-3083-a219-898f4fccb8d1 | -3.07792 | -54.16969 | 2024-10-30 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f445b152-d423-38b3-8507-f86098aaa111 | -3.07487 | -54.16453 | 2024-10-30 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6fce4f97-22b1-305c-8b65-f1f1afa4981e | -3.07413 | -54.16907 | 2024-10-30 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5aa999bf-372d-31ac-adbb-d67e76fa06b6 | -3.07109 | -54.16389 | 2024-10-30 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b44ea179-d243-35eb-814b-3b880d630908 | -3.07034 | -54.16845 | 2024-10-30 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b2872d40-e356-3967-8057-6bae16a3e6d0 | -3.06656 | -54.16782 | 2024-10-30 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b7427b7a-f315-3403-aaeb-93df419f87cc | -2.96405 | -53.86861 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b92b16ed-a21c-3216-b21c-50879278de4e | -2.96031 | -53.86804 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4799146b-0982-3522-b42d-a6abfe362830 | -2.95198 | -54.67604 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffd875b5-d8d2-37a9-8b01-992e91dfe4b0 | -2.95188 | -54.20899 | 2024-10-30 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92afe2f0-3eb6-36ed-b033-d609085f29f4 | -2.95119 | -54.68097 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc410363-1b55-35dd-8833-b552ee04c675 | -2.95041 | -54.68594 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d944ba9-65a6-3763-938d-6579ebdd8cd5 | -2.94482 | -53.70306 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d90d86-291b-3cd7-90da-a075ac59cb47 | -2.93427 | -54.36517 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 623477f3-abc2-3066-914a-43065f517755 | -2.89075 | -53.99011 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81bca7dd-38a7-3929-b2e0-834ecf441b85 | -2.85618 | -54.59779 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 53c9dc8e-bbe0-320f-b8d6-f3e34bf6eb0c | -2.88867 | -54.49314 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 318aa0a7-db68-33fa-846a-e3b3122c20b3 | -2.84366 | -54.70216 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9af02376-0e51-37dd-bd8e-1858b468cfe2 | -2.78911 | -54.02288 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1262a507-2c08-3888-ada6-bc77b6d1e9c1 | -2.7821 | -53.97064 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bb0ed83-dd37-379c-b746-d84c9727532c | -2.77745 | -54.7373 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README68.md)
