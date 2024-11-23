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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e03c7d14-708c-3fb3-b44a-ea92b9f231c5 | -1.62485 | -53.3199 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b557cb1-e332-329b-be4b-b4dac94b8df1 | -1.12403 | -53.40453 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd8229b6-ba2d-3ea7-a202-44417bac2adb | -2.62188 | -51.79548 | 2024-11-23 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 410b9785-6789-358a-b908-e04fe04aac4e | -1.99022 | -53.2904 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66840561-d01e-3e9b-8912-bfbd14849bda | -0.96129 | -51.71924 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2744ad68-2a9d-38d4-9390-adc7b51ab8de | -1.7886 | -53.64533 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e6f4ae5-9212-3f32-8812-ef819dd1824a | -3.79565 | -51.76099 | 2024-11-23 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0863b8dd-4f9b-31bd-bcb5-21a0d7d2fcf4 | -1.73408 | -52.7233 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6fb88431-6447-38a5-9e98-3f9c56a37867 | -1.11971 | -53.39714 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de4c00fe-d848-3cf6-8a07-78a81b4fd45c | -2.95603 | -51.44383 | 2024-11-23 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ce73d7b1-d8d7-39f2-99da-1016ea2b0e77 | -1.76851 | -52.70401 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b78b44c2-a460-36f6-a0c4-d4832e0bf225 | -1.62783 | -52.60597 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b597ff40-9718-3dbc-be15-68ae803956bb | -3.22977 | -53.94088 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdaca55e-6fd7-3bfe-a4f0-dc3b9959a9ef | -1.11389 | -53.39964 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb9003c4-f521-393e-b69d-3b593afa288b | -1.7858 | -53.62834 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2335de96-6131-38ea-8c8c-881f75ea5f3e | -3.32099 | -53.28964 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08f6b414-2dba-3edc-b137-759c7554c119 | -1.7657 | -52.70508 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e3de2f2-7fed-3305-a508-0f19ec175c7d | -3.10785 | -54.00313 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6bc17d4-1c6d-3c0b-9b73-30de7cb9915d | -3.11603 | -53.11803 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e477a9c-0575-3c32-aa21-427ae4fa00d1 | -3.50302 | -53.81274 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32cd3c16-8c09-39b7-9aa2-f6b27e493a81 | -3.2911 | -53.85831 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86b58207-5998-30e7-bfb8-a3788d5d7d73 | -3.41491 | -53.21845 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a94ee89d-e7a2-31af-9fb4-b6a5c8176651 | -3.22635 | -53.92747 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2690bf40-d132-3ebf-8f78-24069065fd01 | -1.18333 | -51.95866 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38234a84-c8b1-3bbd-8cad-1e72d7ca61a4 | -2.68692 | -52.0702 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f601575-039a-383d-8f13-c0377403f45d | -1.20322 | -54.03345 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9876104a-d02b-3d90-92cd-ddc3c9017578 | -1.13465 | -53.4063 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90b5ade5-b5b5-3650-a3ed-24836ae086f3 | -3.25209 | -54.22026 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f72527c2-ff6e-3803-b02d-a9e751cca1f4 | -3.11768 | -59.9284 | 2024-11-23 05:33:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7a704a7-0f8e-3a87-9968-2e0174d8050e | -3.2347 | -54.23027 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e196a81c-a8e1-3bf9-9546-2719088bba48 | -1.74641 | -52.37822 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05a12f42-089d-3647-83ee-bdfeb87d6bbd | -3.22447 | -53.94007 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2580bba1-a5fa-3ac0-bafb-328fd49b9b8d | -1.64676 | -53.86865 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a858a0ef-08a1-3fac-a38d-b75051127e1a | -2.89871 | -54.00774 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c268b64-3acc-35ed-90da-2aa0401fcefe | -1.43123 | -53.38221 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c80f3b62-4d51-3066-a20e-a04c9935a744 | -1.39413 | -55.18867 | 2024-11-23 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 500fc240-d4e1-30d9-99e1-608288119874 | -3.2498 | -54.23593 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b7e98dc-4d0e-3630-bd72-3d9c1fd3a79a | -1.78232 | -53.65102 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc286982-1483-35f5-8bc9-b69637c68c4d | -3.29743 | -53.85253 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef70465a-1cd7-3f6d-9ba3-4d7df869ae8f | -3.30389 | -54.49234 | 2024-11-23 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 411c2dd4-e65c-33a6-ab35-e950dc6fdd77 | -3.22589 | -53.93058 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16780a5a-fc17-3666-9951-1170074a4efd | -1.99028 | -53.13557 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c620972-09b5-3f92-a995-8f1cf8e5ce74 | -2.44303 | -49.08447 | 2024-11-23 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| da481e42-0853-3bd2-820a-2fd1f17b8962 | -1.652 | -53.86917 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75db0608-71e6-3237-8063-bd4cb0a8ad7e | -3.57651 | -54.51889 | 2024-11-23 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ee76715-4531-31c2-bdb3-63f29a5179f6 | -0.96524 | -51.71745 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dcaac2c-8e53-375a-bdbc-0d854a2298c0 | -3.2427 | -50.66869 | 2024-11-23 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 770f2782-6874-3b5c-9da3-ea76374702e9 | -3.71612 | -50.54353 | 2024-11-23 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 882974ac-ff01-3b56-abb5-4cdaabfdacd6 | -1.28797 | -51.73159 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19e9d3c1-b0b2-3df2-9f43-1019d5bb81ca | -1.11585 | -53.39674 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7a1f7c2-2348-3d5d-af72-01b1a0899b93 | -1.41488 | -54.28179 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d080e9f-b699-3f97-a070-3574825200c0 | -1.72963 | -52.71495 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12a6c802-3eb1-38cd-a214-de45b567b050 | -3.2754 | -53.81796 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5f77eaa-8aac-3c57-bb30-33979b6add99 | -3.00109 | -51.55499 | 2024-11-23 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b866200d-6b1b-3993-9a3d-41de6af64be8 | -1.21458 | -51.95063 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a92cf67b-25c1-35a2-be83-50f09299ee2e | -2.79144 | -54.15325 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| afc617b5-1e74-3616-bbf7-2962fe4b63da | -1.63407 | -52.60304 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49802a39-8172-387e-8ca9-eb24b118631f | -0.9353 | -52.41908 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db000649-ace4-3b9c-b833-713a280e940c | -1.43074 | -53.38552 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7a7de02-21a1-3a3e-a2d8-d2b0f92f2d8f | -1.11542 | -53.38947 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df8b75b2-01dc-3008-a882-c5801ea0a195 | -3.1026 | -54.00226 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 133fa4bd-253e-30b5-aae1-db62fd6e9135 | -1.07695 | -53.36683 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39288ba7-ba3c-3242-b66e-7d65e8da4878 | -3.24846 | -54.24506 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecc2d7c8-29d0-3678-9e86-40d82912c35f | -1.41445 | -54.28091 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80c76383-431e-30a7-b638-bf501a92873e | -1.7335 | -52.72704 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24a8092e-9bbf-3f9e-b9c0-d696f6dc034a | -1.78331 | -53.64455 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3df3795f-ade0-3ba0-8223-cf70f9608f9c | -1.63572 | -52.09905 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a58d6245-09ec-38fe-99bc-7994d534cf02 | -1.60581 | -52.5987 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 15bae0f1-6447-3518-b29b-0c527dae2819 | -2.14509 | -50.91655 | 2024-11-23 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59455bd8-ee96-3fdf-b451-ea4af5bd5d0a | -2.44716 | -49.084 | 2024-11-23 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1086952e-c4fc-329f-a1ad-b7fc5fc7aea7 | -3.11658 | -53.11428 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99b9c7d2-2734-31a6-98d2-db98cdf9c9c6 | -2.21063 | -48.91549 | 2024-11-23 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7012fcb5-8fe7-39b7-9b62-1dfab73c5c37 | -3.75124 | -50.00773 | 2024-11-23 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad5bc266-1594-3fcf-be8d-c516e51a5592 | -1.7871 | -53.65504 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1d03a3c-3a7f-3331-82d6-eee774c7232c | -3.58161 | -54.51979 | 2024-11-23 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f225d623-dc71-395c-950a-3ed2669bef2a | -3.84541 | -52.38477 | 2024-11-23 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbb105c4-cb1a-3164-b35c-8f62e92e99ce | -1.74087 | -52.71666 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70d59ece-3599-3105-8fae-0ea631fbebfa | -3.00276 | -51.55413 | 2024-11-23 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1636ed6-2b80-35f9-97e8-d39a297a95eb | -2.19934 | -53.64973 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3f736ff-be03-3929-95c8-04aba3010450 | -3.57697 | -54.51583 | 2024-11-23 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93faa8f9-36ad-3d2a-9b4b-0d6564c19b3b | -1.19306 | -51.93459 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7df13feb-6ee8-3ec3-995c-111cd0085254 | -1.67463 | -52.66019 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a67f129a-f921-3a56-86f0-6e20b2a4872c | -3.70947 | -50.54262 | 2024-11-23 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 429bd161-141a-3851-bb7c-757de56c81a4 | -1.44857 | -53.39541 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef56f7ac-f84f-33b8-a4ce-2c47d6d87cf1 | -1.43407 | -53.38321 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cce08537-ca98-3727-9682-7aeb7374d08a | -3.251 | -53.26907 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78cf9608-9385-3e09-baf2-fe9571bda3cf | -1.60523 | -52.6025 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7fe6ea58-8f52-3e7e-8669-d96ffc1e40ee | -0.94943 | -51.71745 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 301162c9-0fd2-3bc4-8703-39fa5727e8be | -2.16342 | -53.77998 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f05a2b3-ed3a-360f-98ca-74ad9e4d3447 | -1.84945 | -53.69739 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88ecaa0b-b385-3fe3-992a-2b605fd0ad7a | -1.9888 | -53.28906 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a406c0d-92d3-33ce-bc08-7a2c5bdcf18c | -2.06546 | -53.23455 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d56115c9-5270-3ed8-a661-b7a33cd6bf04 | -1.64194 | -52.70089 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9facc93-91af-3a96-91af-c470cd384fdb | -3.4664 | -54.64173 | 2024-11-23 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3f507e3-8471-3f16-80e6-a1b67980f419 | -3.09668 | -54.28996 | 2024-11-23 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35566f62-ad42-3d86-8e0d-69f6da0eebe2 | -1.7787 | -53.60395 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9399aea5-ca30-3c22-8cc5-9b09b8f920de | -0.94096 | -52.41999 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a84758f5-eade-31f1-a735-5fe8d7b4324c | -3.26905 | -53.82384 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0669db9a-eeca-3442-a867-92977c49fc81 | -1.84897 | -53.70061 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f48a4167-b1c9-3652-b44d-512677ad37de | -3.23425 | -54.23338 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README66.md)
