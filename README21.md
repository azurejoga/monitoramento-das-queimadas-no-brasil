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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2504f48-6c56-303d-b03c-9c074b74c273 | -5.2904 | -45.26974 | 2026-09-14 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5401b56-3c1c-3f86-bc61-0b1a8c1ce661 | -6.30538 | -55.28804 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5536afe6-c3bd-3a69-99c1-2b433a162bb1 | -5.81098 | -53.79989 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65dd0e5b-e194-3650-adaa-c4f592b3343d | -7.01671 | -44.63081 | 2026-09-14 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2ac47863-f4bd-38eb-b334-e48585f5dcf9 | -2.90537 | -50.44584 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 59462106-fa18-3419-94fc-0d082119575d | -7.78743 | -46.65902 | 2026-09-14 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d9d3614-9cee-3af5-bd35-5fefb574a027 | -8.39257 | -42.21862 | 2026-09-14 04:32:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6ef9d656-5188-3992-b1cd-d4abacc984a9 | -2.94531 | -50.43737 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3217e22d-b6ea-33a1-a9a0-f2309fe27af8 | -2.61204 | -54.75978 | 2026-09-14 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 907975e1-9a5b-3c2b-a082-1cacc4e9e8fc | -9.45424 | -47.85013 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c277c02d-d1bd-36e0-9d62-e756bad15f77 | -2.90967 | -50.41921 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 6789b032-9376-3c3c-a1df-f15d5840da01 | -9.00087 | -50.82117 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a33f9b47-3c1b-39f9-9f06-70c94ae69a13 | -2.90591 | -50.41405 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| ce2354ec-c89c-35fd-8e42-426afb5e826f | -2.60601 | -54.75881 | 2026-09-14 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fb5910ce-f5fd-3e85-a33d-55c9bdb4a3e1 | -8.53769 | -54.69672 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c21fa7e3-8d58-3eca-9210-818492fb7079 | -5.81796 | -42.73875 | 2026-09-14 04:32:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d3da702-5b83-3526-9f1c-0ff4913fb05b | -2.92967 | -50.40894 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1507574b-6640-3d93-89b5-d5d6b65e713e | -2.92003 | -50.41188 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| b0d2e000-32ad-3ccb-a541-a69101e4546e | -4.55514 | -50.45993 | 2026-09-14 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8d939f00-6673-37e2-a63c-8f5b5e10898f | -2.89482 | -50.42582 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| af66852a-364d-3138-a3c5-bf37dd03bd36 | -9.55136 | -45.43948 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3acd578d-c4cd-32b8-a936-34c58014f910 | -2.92141 | -50.3883 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b6a55ed5-b48a-329c-b34e-e74be660aa03 | -2.88213 | -50.41917 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 408075af-8163-3db3-89e2-a8f302fac5d8 | -4.38842 | -55.20641 | 2026-09-14 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a195047-0244-3ad0-bbb5-507aec247c98 | -6.66613 | -43.65513 | 2026-09-14 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70e2e652-9e7c-3584-848c-afed7e06587b | -6.58914 | -58.85079 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 341e7351-cafd-3c9d-b3f3-9edc1b2668d8 | -9.33361 | -44.36526 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e8f622e3-7979-3528-8f07-73da17a89a7e | -3.22684 | -43.03498 | 2026-09-14 04:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dc71702-07e8-39be-a629-3971efeab357 | -4.85405 | -48.35923 | 2026-09-14 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 659113a1-2926-3f4b-a217-8640258ac935 | -9.33641 | -44.36935 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 07aaa602-f933-3421-8be2-f2ec8beec366 | -7.09387 | -41.79784 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e70aad9e-d5c0-33a3-9398-31aa4843f65a | -5.63448 | -40.85262 | 2026-09-14 04:32:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0b974763-64c3-30b7-bb90-e9dc3dfdb820 | -6.10608 | -57.67367 | 2026-09-14 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 70c8d584-ae24-3335-815b-c949efe65068 | -9.0002 | -50.8251 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87911152-2c71-3bd2-848b-0f2d0e597a64 | -8.04823 | -45.54543 | 2026-09-14 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39efa0e8-9d9c-31f5-b512-251f4de31046 | -6.2996 | -55.28654 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 366088c8-0b2b-3157-9399-8a512301cef1 | -3.33532 | -54.19261 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3542c881-ad75-3ddf-9a9f-f284187811f8 | -7.96995 | -43.9817 | 2026-09-14 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b75f022-fe69-3eba-a042-b4ed38d2bbbb | -2.49007 | -49.10946 | 2026-09-14 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce658d74-cf8f-30d5-9c84-62e5bd6a6ddf | -2.90986 | -50.44654 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4d07d142-6092-3bd0-9388-889e863184bd | -6.29011 | -55.27227 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb30f043-ff82-3e8b-913d-44d24156d155 | -2.95863 | -50.41242 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba4b2ff7-cae6-3396-9211-dcf50d700a02 | -3.46202 | -47.46667 | 2026-09-14 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2ced20b-45e4-3a7f-8756-393246c103d9 | -6.07712 | -57.86764 | 2026-09-14 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58ccaf5b-4a24-370c-af96-f914beeb1827 | -9.53196 | -45.43277 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1eda16eb-16a1-35ec-9307-ad0b45e7b699 | -9.36814 | -50.1609 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a7ae931-44e8-3f53-9b8f-c1f0b24a2d53 | -2.76992 | -45.49689 | 2026-09-14 04:32:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3534efc5-45fd-3ce5-b1d9-48ef87ee44b8 | -2.90876 | -50.39645 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| a39a23e6-c171-35fa-958c-582c1c15df88 | -9.40294 | -50.1723 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4fea45c0-3357-3305-9c0d-3c59deb9bdc0 | -2.96009 | -50.40366 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3058e8cf-a227-3577-905a-15c60de54d4f | -2.90497 | -50.4857 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5fba551-3662-3759-b267-cde1b319bd96 | -9.4354 | -50.12535 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 20ead880-5980-303c-aee5-ee3ec392312c | -2.93483 | -50.41758 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 719bedd6-2b55-3855-ac1c-3552645a2dad | -3.79159 | -44.10273 | 2026-09-14 04:32:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d0f3972-907a-3f8a-a6e8-99aee37b8e9e | -5.84328 | -52.09382 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1aacb2bb-70f5-33bc-99bb-6600a2ef73d4 | -6.29882 | -55.2908 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 122fcfa8-fffa-3bca-a465-13a0bc6d41ba | -9.89839 | -47.61258 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 330d54e5-a5fb-32fb-9c47-50d1578f4eaa | -5.36036 | -50.16916 | 2026-09-14 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 673410f7-33ed-3409-8eef-d5cd02c6be7f | -2.70344 | -57.54625 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1c424571-2fa8-3072-a1f4-fe866fa6d56a | -3.11549 | -53.95066 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d364f771-8a8d-326a-85a2-e024e53917e0 | -2.92074 | -50.40745 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8c69620c-3548-3753-9586-a138e912ec0f | -2.91005 | -50.47392 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59fe9339-d7f2-314c-848f-d367f3919cdd | -9.42441 | -50.11819 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 60b8deb8-454a-3f0f-9cf2-d50a3b5e601a | -3.35557 | -51.29155 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a3b64c4-3de9-344b-9ad2-0fca47c7a024 | -6.53048 | -44.09346 | 2026-09-14 04:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 765c1bd7-c661-38e4-af03-44d1c4901871 | -5.28818 | -45.26218 | 2026-09-14 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77300662-31ab-365e-9442-2605730b4819 | -2.9658 | -49.56145 | 2026-09-14 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1943aed-34b0-3f32-a394-97a4df59c724 | -3.39237 | -50.76038 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2c28e37-b588-394f-983e-2458fd0c02e1 | -3.79381 | -44.11016 | 2026-09-14 04:32:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78a13646-39bd-3e09-bfc8-957218ff8ae1 | -9.4196 | -50.12257 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7ab4b9ac-1ef3-38bf-8af4-bd20ebd1351a | -2.92095 | -50.43472 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| d3641602-9b98-327a-96ac-9471af28e84c | -6.77177 | -42.74669 | 2026-09-14 04:32:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6283ac6c-957c-314b-a2ec-44290c434542 | -2.89643 | -50.44428 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 986b5729-cdf8-30c2-8452-ddf713c0cc14 | -6.37657 | -55.26188 | 2026-09-14 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 223986f1-32f6-3d81-80cb-33ed8076159f | -7.34409 | -46.78495 | 2026-09-14 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11ae39b8-522e-3acf-b2c9-6ca8c49b41d5 | -8.54311 | -54.69777 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c3df3e8-af1d-33cd-b33d-15d7e69b825f | -7.86615 | -54.72378 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b259dadc-c496-3a61-bc37-ca705bbddbaa | -2.91549 | -50.45065 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| b26d567e-cf8f-37fc-9c8b-e7894c1f3ef9 | -2.94224 | -50.40073 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab254419-b7cd-3e18-8a69-578d1b439471 | -6.51148 | -47.59596 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c2faad5-7c4c-3987-9959-2aafe75df192 | -8.54345 | -54.70147 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a64b607b-de46-323c-8c4e-fd867d2b6318 | -9.43474 | -47.85909 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb5734d7-dd46-32b8-84ed-4cdede969b5f | -2.95708 | -50.3942 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bed4d595-84f0-3c9c-a1ed-c6eb66d2935a | -3.37996 | -50.38919 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1c8e85f2-c673-3d98-a768-1ebaafed0d0b | -7.10535 | -41.79532 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f19196c6-d806-304f-ad10-e280e9402874 | -2.95717 | -50.42123 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 723bc873-e968-3a74-a3e8-9790bc819f49 | -9.37252 | -50.18279 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 53ccdbd6-d442-3f0b-ab7b-0125b6a591d7 | -8.53455 | -54.71414 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aefbec35-14b4-3095-ad43-0c4f0ee46c95 | -4.344 | -54.78254 | 2026-09-14 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4b14f379-909a-3ffb-882a-555ed1f08902 | -6.37573 | -55.25668 | 2026-09-14 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0e6cea9-9d5c-39b1-bb14-bc5aa95e3f02 | -8.39153 | -46.29544 | 2026-09-14 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4b83ffd-9dcb-36d2-95d5-23372343734a | -9.41611 | -50.14299 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be1631d1-64af-38f7-a2f9-1f90cca4cc41 | -6.31195 | -55.28519 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 312fb745-ec44-3580-a1f4-99ab2f54abcc | -2.91293 | -50.45604 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d10b4cbd-34d5-3749-bcf1-6877c4325def | -2.93332 | -50.39926 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f320ce19-1b8c-31ff-8c2b-0ecf94d2fd0d | -6.17334 | -43.34874 | 2026-09-14 04:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d65cd61-429b-3e9a-8238-70160e25b50c | -6.79841 | -58.79429 | 2026-09-14 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8eb46b0-6502-3bb2-aad0-9d06adfaf4f8 | -8.5425 | -54.70119 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ee24482-e642-3a0f-94f2-3dae985e6e69 | -6.84434 | -55.56914 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9641a985-1139-3774-bacb-98dd7c4b8466 | -7.09242 | -55.61765 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README22.md)
