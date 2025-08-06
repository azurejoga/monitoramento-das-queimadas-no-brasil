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
| 278a271f-fd12-3e87-aecd-d61a176dc2ba | -6.6706 | -44.44379 | 2025-08-06 03:55:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2adb44f0-fa69-3783-9318-b9116826d5cf | -7.2119 | -41.85061 | 2025-08-06 03:55:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b359f8aa-93f3-33f2-a175-2ef7078a601e | -8.00492 | -43.14036 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 16ee29f8-122a-3b1f-b641-d60b23f2a40a | -7.38677 | -44.62336 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e5d0d2e-768a-398a-a789-660d1e6729f6 | -6.27748 | -45.27091 | 2025-08-06 03:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c57586e5-ac3a-31c3-badd-c58ec30696c9 | -7.07041 | -44.39766 | 2025-08-06 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 080edbbe-d489-3d39-a9d9-dd2de07cf9da | -6.91755 | -43.68734 | 2025-08-06 03:55:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a5554841-a431-3d2f-8bcb-edd137fdfa0e | -8.15451 | -42.39759 | 2025-08-06 03:55:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 78c78b05-8467-3ba9-a08d-a4481c95861b | -6.98669 | -42.09913 | 2025-08-06 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0b300710-14a0-3f33-9f9a-38cd1d2a4c26 | -6.72348 | -43.58015 | 2025-08-06 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7aaa896a-2072-3167-8de5-037e3b55db6c | -7.57366 | -44.90089 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e3c68f6-0a72-346e-b3c4-2221a4455b27 | -6.74627 | -45.30227 | 2025-08-06 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3d0b1a33-1009-3620-97e6-f8a056df28ab | -7.91145 | -45.53273 | 2025-08-06 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fd9d19f-c477-3fe1-84a0-e8fe5eca58f1 | -7.10822 | -44.02461 | 2025-08-06 03:55:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c9c6c96-3ebb-3253-9135-5087d0a8abd6 | -5.57734 | -46.52994 | 2025-08-06 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a8216fc-a9ba-33c2-95d7-826e07405cbc | -7.91225 | -45.5305 | 2025-08-06 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7db6022-6c8b-3451-99ee-4db4d9197a3c | -5.51151 | -35.57952 | 2025-08-06 03:55:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0412e76-ea86-3cdd-acd2-6ef9926a5f77 | -4.19327 | -38.3718 | 2025-08-06 03:55:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 54675ab5-88ad-3a54-92ea-6a48b51fe41f | -7.50504 | -47.18726 | 2025-08-06 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2cee53c-640c-3b6b-972b-ee8e3834b02a | -7.98583 | -43.15777 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0084ead8-077e-3d33-9e0d-4cf905148d4d | -7.20455 | -41.84944 | 2025-08-06 03:55:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18d00ba8-b61a-3e58-ad98-2e6d885f4dd2 | -8.01849 | -43.17865 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 2833e633-e8cd-3301-94d3-3dfe5f685519 | -6.25966 | -43.06643 | 2025-08-06 03:55:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f051fe29-35e4-3c15-950c-27881672af28 | -7.63761 | -44.58497 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8b5fa87-a921-3a3e-8f2c-f2c6424d08a9 | -7.51793 | -44.85536 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aef62fd-7ecb-316a-86f2-aa18b8d6bc6c | -8.0224 | -43.17937 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| e7aff084-8504-3ed5-9d11-e3a5409abc86 | -3.01708 | -46.90844 | 2025-08-06 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc5ebf00-29cd-3d44-b43a-c89bc2975fe7 | -7.37568 | -44.25858 | 2025-08-06 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f664da42-c263-38e3-bdcf-bf9c1ac59589 | -4.02909 | -48.07118 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3404e387-5bf2-3122-bb2c-feeaf79ce443 | -7.63404 | -44.57999 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54dd6f29-8c72-3d24-b4fe-467ab62be425 | -8.1033 | -43.03164 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93a4c1cf-81e3-3c1f-a44f-69105c0f83ba | -6.54828 | -44.01356 | 2025-08-06 03:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc08007a-325c-3b3b-829e-608bf5759183 | -4.82098 | -47.31865 | 2025-08-06 03:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71d2a7c2-6042-31fa-b47b-5b78388fdad0 | -8.00775 | -43.21805 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ecb1de3b-bd1f-3057-859f-94b2470ed12c | -6.98744 | -42.09469 | 2025-08-06 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| af857219-0f49-37e0-b653-99a8bed812c3 | -7.99717 | -43.14161 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 54bacf7b-cc9d-3383-b201-11c3c374cf22 | -6.67713 | -49.79176 | 2025-08-06 03:55:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6d4edc9-1779-3a65-9ba5-98ed79792979 | -7.63723 | -44.57744 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93d11d8f-5182-3e0c-8120-23f73d322b31 | -4.77239 | -45.33533 | 2025-08-06 03:55:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afb30589-d6e2-362a-ae16-a873840f1f90 | -8.00189 | -43.13733 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9ba9f035-9ba6-3831-9aa9-11f8250db21b | -6.5466 | -43.61338 | 2025-08-06 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f919005e-bf51-349f-a378-92a14cf2a7f0 | -6.5514 | -42.7984 | 2025-08-06 03:55:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 54ed1485-fcdc-306c-8b91-74fc2c74cdd7 | -8.02155 | -43.18435 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| b6192066-f68d-3b52-91df-66c014a0beff | -7.99949 | -43.24272 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7f5527e3-b675-37ff-b687-90c61c5f77c5 | -6.72645 | -43.58017 | 2025-08-06 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2bada998-e761-350a-94b0-44eb625e675b | -7.57882 | -44.89726 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f198336f-6763-35ed-b091-4588a89f2b60 | -5.59642 | -51.13076 | 2025-08-06 03:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 347b3c64-5036-319a-8df5-1d906afcaf38 | -6.13131 | -44.44031 | 2025-08-06 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2be81c7-f7dd-3b50-aa1d-cf69aff667f2 | -7.51867 | -44.85109 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffa1f1c8-8f3d-3a6b-b0ad-5ae956421446 | -5.50755 | -41.31443 | 2025-08-06 03:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 76dd626e-ed52-3c10-affd-42aef8085632 | -7.63836 | -44.58068 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af48b645-85fc-36de-81de-29862819d96e | -6.67801 | -49.78691 | 2025-08-06 03:55:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b5cfaff-765d-3acc-9165-f495f6c6db1f | -6.92226 | -43.68444 | 2025-08-06 03:55:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7748dddc-2b8d-3f2a-a2d8-65de1b12d42d | -6.54774 | -44.01221 | 2025-08-06 03:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b2c610a-e105-338b-8511-3b7df9909c7f | -4.01818 | -48.06514 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93891529-5856-3e8b-9fc3-be880aad1cf0 | -8.00101 | -43.13972 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2d810e5b-be60-3928-8cd7-e9d3777a9552 | -7.18886 | -45.47645 | 2025-08-06 03:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8abdca4a-40da-3bb5-9617-4c954e2dcc48 | -7.21556 | -41.85124 | 2025-08-06 03:55:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 26a0834c-4e66-31b2-a771-039195abc4ce | -4.01748 | -48.0693 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13e156f3-fa8e-3292-87a3-66b4dce7f96b | -7.57806 | -44.90174 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f943d984-a084-34b3-8356-5c6f0129cc27 | -4.31943 | -38.12848 | 2025-08-06 03:55:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5f4d0bb-d238-3087-b4d6-3f277b54490d | -4.01764 | -48.06741 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 774e2016-f8d9-341f-89a7-4d3a1a000a78 | -4.09178 | -46.92353 | 2025-08-06 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7cca06a-0163-3bbe-97e6-b80c16992051 | -4.02399 | -48.06602 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 023eddbb-6fe7-39a1-a715-f3adfee56744 | -4.77324 | -45.33023 | 2025-08-06 03:55:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b59df3b1-f3da-3c11-9650-36dedb87da45 | -5.28161 | -44.95414 | 2025-08-06 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ce1d1d2-1e59-3231-893a-611dcd3937c5 | -7.9077 | -45.52729 | 2025-08-06 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64bd7a88-9f77-3cb7-aa2d-facb63840ebf | -7.63478 | -44.57576 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d2e1c74-1581-38f9-b613-88bdc2410462 | -7.38929 | -45.98281 | 2025-08-06 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 117c26fb-234d-399b-a999-23c09c622b21 | -6.95738 | -41.58075 | 2025-08-06 03:55:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f83e560e-f3b6-3a06-9efe-f082ca19b951 | -7.38838 | -45.98787 | 2025-08-06 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 975dd5b3-b641-3200-8fe3-780c4b815337 | -7.35289 | -43.71901 | 2025-08-06 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d3c1e37-cfbe-346d-9822-5ca2e6c93d8b | -7.5849 | -45.30641 | 2025-08-06 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 678d16c7-75a0-3397-b02f-f3ed72993510 | -7.18802 | -45.4812 | 2025-08-06 03:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 45364a9f-03a5-30d2-8d24-855b7a3017a1 | -7.39044 | -44.62811 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c6da36e-3527-3d88-8209-665f1cdbf7ab | -7.64269 | -44.58137 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5f02069-baf1-3e76-8826-96aa09ba358a | -7.64848 | -46.59396 | 2025-08-06 03:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 642b2416-f34d-3d06-9303-fb2d32826cab | -6.96142 | -41.57989 | 2025-08-06 03:55:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 55f80c98-944b-36ab-9226-813a505ba86b | -8.00036 | -43.23765 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f479484f-c56c-36fe-8fa3-09fbc295fcd0 | -5.58847 | -51.13558 | 2025-08-06 03:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1b932ce-ac78-355d-ad06-e2dc0f9bfe6f | -2.88367 | -40.39085 | 2025-08-06 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6d58ef76-0ec8-3847-9813-a4e37c57f946 | -5.4258 | -47.14914 | 2025-08-06 03:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db142bfc-4a4f-3a26-a4f8-466d1ba463bd | -7.37041 | -44.16006 | 2025-08-06 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e556bcc-7ca8-386d-9fdc-0d7ea70a1f44 | -7.0809 | -44.36219 | 2025-08-06 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 044dc216-7eb1-3e51-bc54-093495b9756c | -7.5102 | -47.18815 | 2025-08-06 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16cf30b6-390c-3247-af72-eafcfafa86c0 | -6.68404 | -44.75989 | 2025-08-06 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 095ded66-a6c4-3806-8a73-a2ee4448eea8 | -7.37892 | -44.25784 | 2025-08-06 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34d4252c-7f5f-3375-b957-9608d4765170 | -8.00515 | -43.23324 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4b72264d-4538-371b-89d4-6489bc4f03d2 | -7.33134 | -46.06136 | 2025-08-06 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0861fcaf-928f-35c4-8df6-8b12954bf020 | -7.37466 | -44.25723 | 2025-08-06 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4000be84-0e30-3dea-a176-c6906d7e2f95 | -6.9535 | -41.58269 | 2025-08-06 03:55:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 71cbe07f-0262-3e50-8c79-8ec14ba8f5ed | -7.33042 | -46.06662 | 2025-08-06 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35ddcafc-fc03-37f8-905e-8e4026a8cd7f | -4.02487 | -48.06024 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a3fd3dc-6f1f-36f7-bffa-feae047be2fe | -7.83503 | -45.08121 | 2025-08-06 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ab8b580-5fa4-34cc-83d5-ee80712ec92f | -7.90687 | -45.53438 | 2025-08-06 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ec16f2c-1bf9-3ccc-9352-3e0e42a83043 | -7.63651 | -44.5817 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43d1ec54-dff6-37e2-89e2-66afc6ea6650 | -6.91815 | -43.68369 | 2025-08-06 03:55:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e9c992d5-af37-3328-bd28-c7bceacbfab0 | -6.54722 | -43.60967 | 2025-08-06 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 276ee405-37f5-35ee-9da1-21822ecae1e5 | -7.00538 | -42.14788 | 2025-08-06 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2cbdd62e-8dd1-3358-8b5a-f4ffd7acc345 | -4.82163 | -47.31498 | 2025-08-06 03:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README9.md)
