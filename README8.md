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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 112cdda0-c789-309f-a14f-f8bf15b05bf7 | -8.799 | -45.8689 | 2024-10-10 00:19:57 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f4ec9d7-266a-39b2-94ed-7b1c9302e043 | -8.0791 | -42.9618 | 2024-10-10 00:19:58 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5cd27926-e843-34c9-a508-b76599d96caf | -8.0807 | -42.9692 | 2024-10-10 00:19:58 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e98b73b6-54aa-38ee-9b22-2205433c3ac5 | -8.0824 | -42.976501 | 2024-10-10 00:19:58 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 696b85ae-01d4-310f-b948-c1e47cb29651 | -8.084 | -42.983898 | 2024-10-10 00:19:58 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 080efe1a-5ef0-3572-a766-c15d0297da88 | -8.0709 | -42.971401 | 2024-10-10 00:19:58 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e457d3a-a9b5-3e74-af02-581bb23e498d | -8.0726 | -42.978699 | 2024-10-10 00:19:58 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7d650667-b180-376d-ae5c-dce5377763c9 | -9.2935 | -48.793301 | 2024-10-10 00:19:59 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13cdeaab-84e4-3718-a83f-4ca04ed44b4f | -9.2969 | -48.810001 | 2024-10-10 00:19:59 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a50df0c0-a371-3a98-86d2-b2ac1182418c | -9.2838 | -48.7953 | 2024-10-10 00:19:59 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9405ddf1-de63-3614-9c38-ee929dc71f9f | -9.2872 | -48.812 | 2024-10-10 00:19:59 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1035a10f-0e13-3dde-ad73-47eb0a238f3c | -1.26357 | -46.34949 | 2024-10-10 00:20:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| eaf3ffce-efbf-3a70-b9f0-d90a78873ddf | -1.26158 | -46.36558 | 2024-10-10 00:20:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| bd0805e0-c844-3fb2-a733-0e5c09051ad0 | -1.25865 | -46.34369 | 2024-10-10 00:20:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| b62afae2-72bb-328e-b859-39c2e72ed230 | -2.30084 | -46.9818 | 2024-10-10 00:20:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 72deb3a1-10ce-3938-a5cd-3118ca83f017 | -2.2981 | -46.98878 | 2024-10-10 00:20:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 975f0ded-f9d0-332c-b355-3d8a0ad0d471 | -2.29446 | -46.96328 | 2024-10-10 00:20:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| c6041b45-377f-38e2-9042-b878429ee579 | -1.46829 | -47.22917 | 2024-10-10 00:20:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 23e73bdc-1789-3b93-8496-60c7da1ae621 | -1.46616 | -47.23465 | 2024-10-10 00:20:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 0361f2c5-28d6-3ee8-b51a-5f928714016e | -2.74512 | -48.68532 | 2024-10-10 00:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 06cc2ffb-fee6-3606-9238-0db126d77f71 | -2.22872 | -48.03552 | 2024-10-10 00:20:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 551cb03b-9d35-3e97-8f5a-e99484252372 | -7.7629 | -42.469898 | 2024-10-10 00:20:01 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5a42dfd3-2ce3-3d1a-bbad-01baf36af142 | -8.9695 | -47.823101 | 2024-10-10 00:20:01 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c10a4601-e56f-3670-a5c4-a97ea1dfd916 | -8.5038 | -45.780701 | 2024-10-10 00:20:01 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4e7f868-2acc-38fa-b622-7c98ecb644a2 | -8.9196 | -47.7313 | 2024-10-10 00:20:01 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b95c52b-93a8-3b89-962f-d9f83479bbcf | -7.5431 | -41.725399 | 2024-10-10 00:20:02 | METOP-C | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3eb9b2ff-fa20-3e0c-9fca-433a35816a46 | -7.5348 | -41.734501 | 2024-10-10 00:20:02 | METOP-C | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7ef45cd1-7dbb-37dd-98ab-9f561fe51c85 | -7.5364 | -41.741402 | 2024-10-10 00:20:02 | METOP-C | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 32062efc-7ba3-312d-a4d6-0e176a073713 | -7.7515 | -42.464901 | 2024-10-10 00:20:02 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ab085c6-1bfd-31b8-a3e4-a0f00428753a | -7.7531 | -42.472099 | 2024-10-10 00:20:02 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5359d1a-3f5a-3707-a2b2-d21ff80ee573 | -7.7547 | -42.479198 | 2024-10-10 00:20:02 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 91bdc20e-a7e0-3319-92bb-aa54f125f1fb | -8.1712 | -44.863899 | 2024-10-10 00:20:03 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e8253500-9331-346c-99b3-897d1bf43ad3 | -7.3941 | -41.252499 | 2024-10-10 00:20:03 | METOP-C | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 636b043e-a0dc-3037-924a-d88a9a7ed27c | -7.3957 | -41.259399 | 2024-10-10 00:20:03 | METOP-C | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 140940da-ead5-3cfa-a9b0-af7fdc841ef9 | -7.998 | -43.8447 | 2024-10-10 00:20:03 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0e748ab9-7ba5-3b1b-83c7-235677361490 | -8.0636 | -44.467098 | 2024-10-10 00:20:04 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 64943679-b7f2-31b2-a1dd-02f72e2089ee | -8.0655 | -44.475601 | 2024-10-10 00:20:04 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9984f528-a1fa-3b32-8238-04c56bab2238 | -8.0538 | -44.469299 | 2024-10-10 00:20:04 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03099817-0fec-30d9-b0f6-1a3c30dae9e2 | -7.728 | -43.0937 | 2024-10-10 00:20:04 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5d5009c2-6c8f-3b53-b2fb-10cd8cd33470 | -7.7297 | -43.101101 | 2024-10-10 00:20:04 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 839df877-261c-3e92-85fe-8364abffaace | -7.5853 | -42.412601 | 2024-10-10 00:20:04 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7338ea86-d92d-3a85-96ed-72f0a45d4b90 | -7.5869 | -42.419701 | 2024-10-10 00:20:04 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db9f811b-a3ca-3ea6-ab41-8ede6aa30024 | -7.5739 | -42.4077 | 2024-10-10 00:20:04 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f9d3189c-3dca-34ff-9459-55c1d6950dc0 | -7.5755 | -42.414799 | 2024-10-10 00:20:04 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ffb4836f-5be3-3f5f-8c48-6bbdce360d9d | -7.5931 | -42.492802 | 2024-10-10 00:20:04 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 27cde06d-089c-3ce2-a343-d2dcb6295388 | -7.5641 | -42.409801 | 2024-10-10 00:20:04 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 60f51ce2-bad0-337f-90f3-d481d0126e62 | -7.5657 | -42.416901 | 2024-10-10 00:20:04 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a5516b08-1744-3dae-b32b-645ee1cb9fc1 | -7.5929 | -42.537601 | 2024-10-10 00:20:04 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3744c898-b1e0-3c45-affa-69197a12f787 | -7.656 | -43.047699 | 2024-10-10 00:20:05 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4aa20a36-046a-36c0-b40e-371fe2109243 | -7.5543 | -42.411999 | 2024-10-10 00:20:05 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ada3d1bf-d8ba-32c7-94c7-10c6e5daf819 | -7.5559 | -42.419102 | 2024-10-10 00:20:05 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 59128850-6224-3522-9c33-90419fc67d70 | -7.5847 | -42.546902 | 2024-10-10 00:20:05 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d46ac540-ba6b-3d34-9efc-54ad704890c3 | -7.5863 | -42.554001 | 2024-10-10 00:20:05 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44c9bb6c-3a38-30bf-bbf5-4fffc8b5c6bf | -7.5461 | -42.421299 | 2024-10-10 00:20:05 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fafe7357-427b-3cad-b8cd-dd9462bf2606 | -7.5477 | -42.428398 | 2024-10-10 00:20:05 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 14e0fb73-6d1b-3275-9ecd-249b200c9b17 | -7.9317 | -44.380798 | 2024-10-10 00:20:06 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fcf5ad56-1c5e-3687-b3eb-8c932ce22ac1 | -7.9335 | -44.389198 | 2024-10-10 00:20:06 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8f6395e1-2071-30e7-b8e3-9fa4dce2597c | -7.6232 | -42.993301 | 2024-10-10 00:20:06 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c123c656-6ef7-3b62-8269-ac7df70bac4a | -7.6248 | -43.000599 | 2024-10-10 00:20:06 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ba28fdaa-0654-3c1f-a677-baa371a66281 | -7.6134 | -42.995499 | 2024-10-10 00:20:06 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c50c5978-d0a4-36d0-b605-02d48b0ecd34 | -7.615 | -43.0028 | 2024-10-10 00:20:06 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c33b77bf-ae0a-3905-8f0e-664a06dcfc49 | -7.6167 | -43.010101 | 2024-10-10 00:20:06 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1699e19f-36a8-396d-8c1a-550079d2e1c9 | -7.2881 | -42.190899 | 2024-10-10 00:20:08 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 39524a98-5855-32fa-b688-4e3f4655fca5 | -7.2896 | -42.197899 | 2024-10-10 00:20:08 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3f85d71a-e9e8-3c7a-8131-5bedb61362dd | -7.2798 | -42.2001 | 2024-10-10 00:20:08 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| abda8e8f-6436-3b5f-9571-7ec1d2d8aa26 | -7.2814 | -42.2071 | 2024-10-10 00:20:08 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 093609cb-7682-39b5-9ec6-07287469aa7c | -7.6616 | -43.810799 | 2024-10-10 00:20:08 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| da69b1a4-7b9b-355f-bff2-03e99ef8f247 | -6.38 | -38.8325 | 2024-10-10 00:20:10 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1651d706-fa9f-38fa-b8fc-0e9edc98a3f9 | -6.3818 | -38.840401 | 2024-10-10 00:20:10 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d6fb1a2f-e9ee-324b-9e09-7aa18ef39f5e | -6.3837 | -38.848202 | 2024-10-10 00:20:10 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 30ab1e24-74bf-37d9-b1f1-4586347c9f2d | -6.3855 | -38.855999 | 2024-10-10 00:20:10 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7c20f3a1-1bd0-38e0-8cdd-13ea61b63106 | -6.3873 | -38.8638 | 2024-10-10 00:20:10 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c7b98a53-f46f-3016-bb6a-8ffbe2645bdc | -6.3702 | -38.834702 | 2024-10-10 00:20:10 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 359c2ed5-67e2-34ca-8388-0ac5f662d981 | -6.3721 | -38.842602 | 2024-10-10 00:20:10 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 503b0ecc-73e3-3a48-9510-f87c78c85b0c | -6.3739 | -38.850399 | 2024-10-10 00:20:10 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 951f962c-00f4-3b3f-ae72-5dc333e7650e | -6.3758 | -38.8582 | 2024-10-10 00:20:10 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e553fee2-f91a-3032-9857-678088439033 | -7.1502 | -42.309898 | 2024-10-10 00:20:11 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 796bfbbe-87fd-352e-a95c-016a37ccfeb9 | -7.1584 | -42.300701 | 2024-10-10 00:20:11 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bf1bef58-a317-3bb6-a070-e13dd217fc58 | -7.16 | -42.307701 | 2024-10-10 00:20:11 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5941f3a-f30a-345d-8f66-987895750d6a | -7.1615 | -42.314701 | 2024-10-10 00:20:11 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eb16ec4b-9ed9-3838-be69-5a27f59b180d | -7.1486 | -42.302898 | 2024-10-10 00:20:11 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 43cdf634-adff-3025-aaf3-b5b110cf283e | -8.7037 | -49.765301 | 2024-10-10 00:20:12 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5314c224-9d57-35be-9118-a84d4fe5a213 | -8.7076 | -49.784302 | 2024-10-10 00:20:12 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 893553c6-09b6-33b9-ac7a-75b86c214bb6 | -8.6745 | -49.771099 | 2024-10-10 00:20:12 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64b1c8e3-fa8d-3865-a047-758660056b21 | -8.4276 | -48.633598 | 2024-10-10 00:20:12 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b04245b6-44f8-3dd4-aaf6-87db491854a3 | -8.431 | -48.649399 | 2024-10-10 00:20:12 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3104fca2-1e89-398f-a957-6886182fef1d | -7.0848 | -42.6133 | 2024-10-10 00:20:13 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c3a6d52-454c-340d-a06d-0809766d3ad8 | -7.0864 | -42.620399 | 2024-10-10 00:20:13 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 68d71849-76a5-3c82-9082-3f08aeaa8876 | -7.088 | -42.627499 | 2024-10-10 00:20:13 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ddb0652c-3eab-30ef-a175-911a7ab0d741 | -8.4178 | -48.6357 | 2024-10-10 00:20:13 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf3e580-1567-3d61-9b8e-57c2f34c86cc | -8.4212 | -48.651501 | 2024-10-10 00:20:13 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 853ac0b0-fe02-3260-9136-a3e0f93bc811 | -8.496 | -49.2034 | 2024-10-10 00:20:13 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20958717-326a-3e15-94d1-af689dc4db81 | -8.4996 | -49.220699 | 2024-10-10 00:20:13 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57e1a69c-40e5-300b-b3e5-139281b7bad1 | -8.9498 | -51.465599 | 2024-10-10 00:20:13 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1416b9c-e0f0-3322-ad8f-8c0810e772ab | -7.5427 | -44.851601 | 2024-10-10 00:20:14 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18e39754-8b3a-3eec-87c9-7ed27a9d0a76 | -7.5446 | -44.860401 | 2024-10-10 00:20:14 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de6de4ff-5fb9-3dd5-ba41-f732902fb607 | -7.052 | -42.650398 | 2024-10-10 00:20:14 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d28b0d9a-80f5-31c6-bd51-afe4ac5eb0c9 | -7.0536 | -42.657501 | 2024-10-10 00:20:14 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f81bec69-edd1-3986-bfa0-3dbccc392c4f | -7.0162 | -42.628601 | 2024-10-10 00:20:14 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a80e584e-35dd-3c2f-8e72-423aa02dc170 | -6.8915 | -42.441299 | 2024-10-10 00:20:15 | METOP-C | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README9.md)
