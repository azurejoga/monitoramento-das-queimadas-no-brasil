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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a58030e4-20aa-362c-8e1e-e0b5d24ddb3e | -4.10482 | -48.20284 | 2025-08-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 866ee72e-c1d3-3f58-8ed0-a550dd31e394 | -7.68446 | -45.11802 | 2025-08-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dec43528-43be-3fb6-856e-fd07b4bbf0d3 | -7.36841 | -44.19436 | 2025-08-03 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| e3c611e8-754a-3670-8776-dd94d91cdec8 | -4.56232 | -44.20907 | 2025-08-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1d3fd90-5c9c-3cf6-994b-4bd017ed59f9 | -8.0021 | -43.17524 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 0d9c2d6f-36d1-3089-857e-2119ca288e33 | -3.96461 | -49.43748 | 2025-08-03 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 539be3ad-107c-38ea-a2b9-c3b50f6e1981 | -8.04398 | -43.11169 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| dc6bb180-719f-363b-8969-b9e9dd4a8718 | -7.41229 | -47.00695 | 2025-08-03 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24476b99-2313-3325-8e88-f42525140d48 | -7.11581 | -43.48066 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| acd6ab9c-730f-3820-8bdd-1b6ec8aa6057 | -8.01779 | -43.14614 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5832a1cc-c486-346e-937b-7158a7cc9cef | -4.02904 | -48.06278 | 2025-08-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b60937f-23bc-3356-b1c7-bc6e0e3e3485 | -8.00448 | -43.18462 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 34be4594-3cfa-3724-9e5d-08ad1c6fa460 | -7.33739 | -44.68036 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 359a75a2-bc7b-35fd-8f7d-3d839f41bd90 | -7.1224 | -43.4859 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd866e78-389c-347f-9a7d-22b4f8dba3dd | -6.35403 | -46.16214 | 2025-08-03 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b7b61ce-a266-37a4-ab77-3b57fb4be214 | -8.00949 | -43.17635 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 057cb67b-0e35-33a6-bbe6-5ec3f2909fe0 | -2.66059 | -42.72196 | 2025-08-03 04:25:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 519093c7-6d6f-3b97-bc08-8cb982e9f4aa | -7.09698 | -44.36697 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8467fa24-8c87-3d34-a6b1-a002894f5b46 | -7.3145 | -44.66945 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 433bd42e-dda8-37c8-9174-de3cd2ebc62b | -7.19054 | -43.90738 | 2025-08-03 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9317c46a-650d-3c66-bc23-3b71f9d691ad | -7.11039 | -43.48132 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 60af8e6f-0d5e-3fa5-803b-3c3caf4b83e0 | -7.59945 | -44.98501 | 2025-08-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 172f0426-585d-3f71-af49-1d8d0fe942c6 | -2.9384 | -40.09676 | 2025-08-03 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| afb0d1f6-0bbf-3bcb-bdb8-1eb31bdb9f53 | -8.01647 | -43.15497 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 684400ff-d321-34a4-9191-6d874911b3dd | -7.41233 | -47.02828 | 2025-08-03 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2c338aa-fa67-3421-aeb0-8a6b25c4c9ab | -4.31037 | -48.1066 | 2025-08-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 755e3a48-e635-3f5c-8d0c-d74608f3bdfb | -7.91244 | -42.76144 | 2025-08-03 04:25:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2021e738-f92f-39d5-852b-ba059ff7beb9 | -7.10998 | -44.67732 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae999c89-f23d-3674-945f-8398a49f2399 | -5.90853 | -42.61851 | 2025-08-03 04:25:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb0e92d3-c558-3053-8828-eda3993600c9 | -8.01276 | -43.15442 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 199.4 |
| 7a3f5a96-ffd7-3de3-9ce9-5a4d63f14229 | -7.43765 | -43.82749 | 2025-08-03 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92864ecd-0107-3075-b1a8-24b9dd6370d3 | -4.56004 | -44.20122 | 2025-08-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| dbfd0051-d4df-3579-9b66-2e7df9934461 | -7.6051 | -43.96595 | 2025-08-03 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f35db0fa-3bf5-319a-a59d-e6510a7ef05a | -5.59423 | -51.12674 | 2025-08-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0639c27-8add-3f67-9a5a-603b755f67a2 | -8.01977 | -43.13286 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f3467234-c4ad-32d0-ad14-7d318859902e | -6.35734 | -46.16265 | 2025-08-03 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd376b1f-8030-3cf2-bb68-14442f3e14b2 | -7.53739 | -44.88548 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2d08b2e-d8a2-3306-a3e6-c6abe01b637c | -8.01845 | -43.14172 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e447d977-4fdc-3366-9524-c0edaf83bdf8 | -7.31049 | -44.67278 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 762961cf-5da4-353d-88bb-d403a32fb4f7 | -8.02215 | -43.14228 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 34795030-d475-36f3-9659-fddf65149bda | -8.00144 | -43.17964 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 885b1374-037f-32e3-ba1d-536dd3362fae | -7.1116 | -43.48424 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2f88385c-c002-344d-a03a-eb918e7f538a | -7.99731 | -43.15652 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1a426f87-2839-378b-8132-3a1f708b8ba4 | -4.06275 | -46.93629 | 2025-08-03 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de6e125e-1508-34e4-bf83-6f16b9be89af | -6.68007 | -44.3446 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aad5ab1e-a23f-3315-980e-f2c613d53537 | -6.33007 | -45.6393 | 2025-08-03 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2f8bce6-3da6-352b-9648-96671244ca46 | -8.0423 | -43.10905 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 3d69f49b-dbd4-3812-a070-d7a78fbeaf05 | -7.36899 | -44.19045 | 2025-08-03 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f58d07a-fbc4-3984-ad2a-9e1d073194c7 | -7.54559 | -43.83096 | 2025-08-03 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88b7452b-4f6f-3f1c-ae31-e0ca12851cdb | -7.34308 | -44.689 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 903022e0-ad8d-3854-a0de-1ce0f005f4c8 | -6.95431 | -44.22499 | 2025-08-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44a68843-c4fe-34d2-b9ae-2b2b0bd22ab7 | -7.09998 | -44.96982 | 2025-08-03 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5635cb8b-bdcd-34e1-ad7d-2e79220cf868 | -5.91969 | -50.00857 | 2025-08-03 04:25:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb2aff55-179a-3f0a-bf6c-96ed75d8539f | -6.49553 | -42.8168 | 2025-08-03 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| aebf6e90-8758-36b2-8946-951561c7d152 | -6.0715 | -44.66122 | 2025-08-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00d8036e-99a7-37af-96c3-e5d870e2e668 | -6.52033 | -42.80293 | 2025-08-03 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0f09af52-baf6-3186-b9d2-9a23f882e029 | -8.0108 | -43.16756 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ff74b830-2de9-316b-945a-2add819989fd | -7.55604 | -44.41511 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27f78560-545d-3150-85b6-26fd02de6ae8 | -8.00079 | -43.18402 | 2025-08-03 04:25:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 1df9ca1c-5c9b-3fa9-9686-67218d463c88 | -4.7718 | -45.33919 | 2025-08-03 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| fa695849-cf8e-3201-b486-26e8a10dc3e1 | -7.60285 | -44.9855 | 2025-08-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 476d4e6f-f7c5-306e-807d-2411c95e502b | -8.00776 | -43.1626 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 77108eb1-8aea-3330-87cf-57d1d11294bd | -7.36699 | -46.66593 | 2025-08-03 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 500db2ea-c23f-3170-af32-4f5f16729e9b | -6.13171 | -44.83437 | 2025-08-03 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d339a800-b90d-393e-802d-9408974a4be6 | -7.34592 | -44.69338 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d409aa84-94df-3cd4-a7c0-73cbe2e14754 | -4.31096 | -48.10284 | 2025-08-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3b768841-0bb4-3c5f-b383-b9d5ba624911 | -7.12421 | -44.07973 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f659fcd-0ff7-3f72-b898-ff7ede926430 | -7.36024 | -44.66854 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe1cbcea-a437-3cdd-8f71-0af37a062088 | -7.3065 | -44.676 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c4c69ba-fd94-33f3-a03d-3f82689b3b94 | -7.1152 | -43.48478 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3f3fbffd-bb98-3f01-8669-0cbe60c3aa5e | -2.90844 | -54.16072 | 2025-08-03 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d0c6a1a-e3cd-339c-b913-0bcb5c93a79c | -8.01015 | -43.17194 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b305e6f1-2a0c-39ac-b53b-8d01dd1a5cee | -7.55774 | -46.03127 | 2025-08-03 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51bf2b20-34bb-3f8a-9470-07a2e0ff8d56 | -8.03792 | -43.11294 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 3c9b66ee-9828-34b1-877f-ad5515d2340d | -6.81617 | -48.64049 | 2025-08-03 04:25:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9f852dd-9927-367f-8838-e6ef68ce5734 | -2.91066 | -54.15973 | 2025-08-03 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 65c78eee-c4e5-3647-a7bb-b2d4bbbaec30 | -6.35457 | -46.15868 | 2025-08-03 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab867376-9efd-3b68-ba7a-eb8d76b73873 | -2.90704 | -40.13451 | 2025-08-03 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 48b6152f-63fe-3c0b-909e-7d2313ab2ccc | -8.00253 | -43.19774 | 2025-08-03 04:25:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 082d56e4-f61e-346c-a6d1-e2901527f10e | -5.89035 | -46.52039 | 2025-08-03 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20176308-ea93-382a-be7e-7dbd6eb19a5e | -2.9061 | -52.54954 | 2025-08-03 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33d8477f-74a5-3e1c-83fe-88c73a16144a | -3.48252 | -51.18882 | 2025-08-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 521dfeb9-cf88-3c8b-8058-38520a6ac6b5 | -8.00406 | -43.16202 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| e94a614b-dd20-3840-900f-b83b91c98e26 | -7.99796 | -43.15215 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b7a3f116-5318-3edd-9f66-388b7eba6f35 | -7.53398 | -44.88494 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29c03b43-4d37-35ab-b2c6-19961cc82d26 | -4.77566 | -45.33623 | 2025-08-03 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a0499b0-d56a-3549-bdca-1c111269e226 | -8.03022 | -43.13898 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| ab96b11e-9982-3e45-84dc-842ae0ed0105 | -7.53682 | -44.88914 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00d5b675-9e28-3a75-a2b5-77c1d6ad47b9 | -8.02838 | -43.14109 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 49ac5e44-425e-3a1d-9cbb-652bef86deed | -7.10336 | -44.97038 | 2025-08-03 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4584fcfe-9140-3356-820f-316045d89334 | -4.77234 | -45.3357 | 2025-08-03 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86ea71f8-ba5f-34e7-a396-b71a6c5fa82e | -7.25448 | -44.55703 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab68dd02-81e3-3522-a2c1-2aee923c3311 | -8.01952 | -43.1599 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 15027331-e7d6-30ba-8b38-6459ea9092f7 | -4.85858 | -45.74302 | 2025-08-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e9e4a18-5549-3ff4-8842-935c30e2bef8 | -7.68107 | -45.11747 | 2025-08-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27840e37-db91-3088-ac0f-780c6bed992a | -6.56986 | -43.3686 | 2025-08-03 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 803b94f2-3203-37b0-a60e-330aa8d315c9 | -7.1347 | -44.08136 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 895b412c-cd51-31a1-8f63-efbb4f355c15 | -6.67833 | -44.35619 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b38d3596-f22c-307e-ad77-1cef12d4758d | -7.65549 | -44.77772 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1f54468-b14a-319a-8dd0-43fa24b6165b | -2.90895 | -54.15771 | 2025-08-03 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README15.md)
