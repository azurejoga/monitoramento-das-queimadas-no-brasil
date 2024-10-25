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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7d8873d-75ac-3974-8a3f-a4242bc0ef13 | -3.10988 | -53.73054 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a8f37ba-02c5-3773-ad72-9883028f9013 | -3.10979 | -53.73447 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8304c4a8-5c2e-3cf0-885d-970be8619aea | -3.10929 | -53.73412 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67fa241f-339b-3d44-9ff1-dfa39b5bcc08 | -3.10686 | -53.72662 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bc56e46-5804-3430-b2de-0575a8f7550f | -3.10629 | -53.73021 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f23e8d0-9f86-31df-9fd6-317680af9233 | -3.10572 | -53.73381 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd7964f6-f344-39a3-b0ed-e55035ed3d53 | -3.10336 | -53.72237 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e416138-3e15-3607-b577-da00344dd782 | -3.10279 | -53.72595 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7995033d-0c7a-3a66-82a1-d53baa1328d9 | -3.09928 | -53.7217 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9d28c43d-7ad0-3052-8360-65ad7e30661c | -3.09871 | -53.72529 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bd7436c5-9a22-33b2-836a-cb8cbee2e2cd | -3.09521 | -53.72103 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 348d2d2a-dcde-389a-a3fe-061337c2b191 | -3.08241 | -53.8277 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6dcf39a-177a-3541-91ac-0f5a9a204d14 | -3.0789 | -53.82331 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7367d023-e9fb-3e0f-bfa2-86dde4caeb40 | -3.07831 | -53.82702 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96af9f22-2f16-3e4d-b290-7961ff19b1e3 | -3.07712 | -53.83447 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d966cc99-e28f-31f8-9264-95cbc658fa84 | -3.07479 | -53.82267 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8098bc84-a065-30e7-88f2-f941b107e240 | -3.07419 | -53.82643 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5489235-cdae-37bc-877b-dd45994cec73 | -3.07129 | -53.81825 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f438671-cb14-39e5-a87d-f29d2423c8e9 | -3.07069 | -53.82201 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62b084e6-836a-3ce3-8eda-c3e4242c04c5 | -3.07009 | -53.82578 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2113e84-4e35-3206-aad9-b8e795ff1778 | -2.94416 | -53.70475 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 040ba0e4-cfa5-3ab9-9946-b1949382c9eb | -2.93512 | -53.91698 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79b86c94-27b1-3889-b391-b48cd4cf5d3f | -2.8928 | -53.99427 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c5563fd-f489-3ba2-9d48-0f5343d535eb | -2.84163 | -53.98564 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66ede695-d36a-3dda-9543-47c3af1f7d1e | -2.56947 | -54.01695 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 317f7b97-5ce3-3b62-94de-03443957511e | -2.41163 | -53.81622 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd89668c-4e00-337a-9259-6f0367ce53db | -2.16689 | -54.47739 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d83de3d0-0fad-3d0a-9306-bd2256757411 | -2.15409 | -54.92445 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 199da595-fcbf-3feb-b4ee-5a14c39cfa70 | -3.57936 | -54.62791 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d839745-df2c-3009-879a-369fd22211c6 | -3.57871 | -54.63194 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5d13e2b-f68f-3d28-8fd8-289e51e6283e | -3.5731 | -54.58518 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17197e84-2c8c-38a4-a83e-74e085b82552 | -3.57245 | -54.58918 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe4f46f8-1325-39dc-8fda-ecbc5a3234ab | -3.56816 | -54.58852 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed037476-88c7-3191-9ac1-1c2ac20dcea0 | -3.55817 | -54.75846 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51eb1783-e115-3ea3-a260-5fa7c11793f2 | -3.50551 | -54.67377 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09e10b18-682c-30e6-a973-b292dca10b91 | -3.50394 | -54.67514 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9406c2bc-9829-3ba1-8811-74c87b1c8207 | -3.50118 | -54.67314 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d65f4af-905d-3c19-bada-a4f4208e7834 | -3.4942 | -54.43546 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76788061-e902-3cbd-b134-7d5c9af29452 | -3.49354 | -54.43951 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e379ed81-f56d-3d82-b95e-3f1d93b0e52e | -3.48931 | -54.43874 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cf8a50a-67e3-39d0-83d5-3f63e0df02b4 | -3.48865 | -54.44282 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d56855d6-7055-3447-a035-77005e254cf4 | -3.48798 | -54.4469 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db97657a-7ec5-3e85-9dc7-7b4c0b0adf20 | -3.4844 | -54.44209 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1242a012-78dd-341d-8368-5035f7d0e1b0 | -3.45318 | -54.63332 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60cd069f-c179-32f6-b67a-ab4741d3805d | -3.44821 | -54.63666 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 353fa01b-7793-3c41-be89-9e9b6936d4b1 | -3.4439 | -54.63594 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e176260-9ca0-3198-b725-019812c232a2 | -3.41162 | -54.27784 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60451ff6-a149-3feb-9a4e-9b3ad4a48769 | -3.63541 | -53.96994 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 679098aa-b3e2-3625-949c-cee04a85a858 | -3.63191 | -53.96563 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9859fa66-7fbb-3155-88a1-cf0508b5dd6f | -3.63129 | -53.96938 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d3b2df9-63ba-3fb2-9408-18c94be617d9 | -3.59484 | -53.78978 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1393c57-815a-3723-b8fa-c85a1e051d76 | -3.59134 | -53.78564 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7c7eaf3-feab-3107-b241-c160ac80dce6 | -3.59075 | -53.78931 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7133355-41ae-307c-b070-6de4987d6e2c | -3.58726 | -53.78514 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8cbb75e-d92c-306f-81e3-532e8073bdbf | -3.55297 | -53.99553 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02bb9ffa-6070-3bb8-a075-de1d0dccc73a | -3.48453 | -53.98481 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c67e4d2b-90ce-3f2a-a118-14694756fcd9 | -3.4804 | -53.98422 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2159a1b-9e97-3117-bb7b-4412824254c3 | -3.2808 | -54.15638 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 762d3514-c893-3ab6-9031-3ba5894727d1 | -3.28015 | -54.16027 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4432f502-d709-36c3-86fc-e587fe8c8272 | -3.27078 | -53.71187 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78bfe4dc-3dbf-3fe5-a23a-57b1bd504402 | -3.26672 | -53.71122 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7c6543b-c110-3791-bb7f-088fef1443f1 | -3.26614 | -53.71478 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8562bfd-21da-3541-8d9c-6ec900971809 | -3.26208 | -53.71412 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3913d13-f11a-30ad-861f-e9ee5f322a2b | -4.1313 | -55.04608 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b66e2afa-41b9-300b-9fa2-954244efce24 | -4.13098 | -54.63488 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cf06eb4b-3764-3586-afdb-1540a1930e8a | -4.13033 | -54.63885 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bf832b38-2ca2-3cb9-9460-3768d370af5f | -4.12864 | -54.90073 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be4f38ce-c1bc-3540-b616-d7c9f71f47b9 | -4.12675 | -54.63395 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ae805b30-529f-3d6b-8f5f-c62e3ef9263f | -4.1261 | -54.63794 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 296d7727-1701-3dd9-8007-9ce9f41a55e6 | -4.03465 | -54.61637 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72ee4267-c3f1-3766-8c9c-897476597afe | -4.03402 | -54.62025 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db290930-13db-3bb5-abc7-954db6f5f111 | -4.03101 | -54.61178 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7ceaa04-3a4c-3e65-b6c1-803ea6cfe009 | -4.03038 | -54.61569 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4759e3bf-a70c-314f-8445-5d247310d097 | -4.02975 | -54.61958 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aed9dd0e-bfe7-35c2-bb3d-bdad74bd86e4 | -4.00538 | -54.44921 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39323117-0d38-3a25-ac49-ed6fa5f8a6ab | -4.00474 | -54.45306 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e5c7546-05b5-3e80-8d49-79f970284933 | -4.00409 | -54.45699 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31c609ef-adf9-3edd-87ee-38d3f9f49d61 | -3.99368 | -54.46756 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0efdc4ae-38cc-368b-907e-2e6edc4328a4 | -3.98943 | -54.467 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28deca50-803c-3236-a73e-5f6a67b798c3 | -3.9825 | -54.35202 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79dd483a-395f-30a7-af85-48c2d877c5d1 | -3.9787 | -54.35033 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 114db924-e963-3a39-91ba-02b800fcdee0 | -3.9783 | -54.35142 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34c71bd7-532f-36a4-8179-2736bfa9b41e | -3.96501 | -54.66671 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09fee084-71fd-3549-876a-dbe10a849ef5 | -3.96074 | -54.66598 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ffac6fd-1341-353e-b281-4ea4e1e5ef8d | -3.89586 | -54.13836 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffda1009-eb9f-3d40-b070-4525eb0da6e1 | -3.88699 | -54.14074 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f3d1c44-b59b-3f75-95b9-a4a074ed58ea | -3.88639 | -54.14445 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f9cc5a6-a18c-3daa-a873-2282af440eac | -3.88224 | -54.1438 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49e8f80c-ab61-34ba-bdb1-e10eac600676 | -3.8648 | -54.35832 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b75fe9f-c746-3d30-8486-adf42096cd1f | -3.86417 | -54.36222 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04739597-da83-387d-bf58-05f3802d9c54 | -3.79482 | -53.94001 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1db3fc01-a527-33fb-8666-a11d1cdf4f7c | -3.77702 | -54.04976 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 347fee0d-a7b1-3d1a-9560-96dadaf7dbda | -3.7729 | -54.04907 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2e1c4f3-d489-3b1d-a1e6-6472b5d2625e | -3.80737 | -54.47229 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2fc6465-3a62-3023-bb56-a89ac18c6106 | -3.76337 | -54.34562 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0daba13-3905-339b-af94-5d1dfa75147f | -3.76271 | -54.3495 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a822ad4c-71a9-3239-8edd-a75ea7ab9a0e | -3.74086 | -54.40577 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8f15f983-4ec6-30f8-b84d-69a5931eb545 | -3.73664 | -54.40511 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9b90c4c-0232-3f31-9156-6d9231fec0bb | -3.7107 | -54.40467 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aec145f0-49d7-37b1-a27f-be512951dedb | -3.70648 | -54.40401 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README69.md)
