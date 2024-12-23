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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb033b30-9bff-3f81-8249-12c84baf51b8 | -9.83 | -36.32 | 2024-12-23 00:00:00 | MSG-03 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27278e5d-afcc-30a2-98f6-95ded4f0068f | -4.16 | -43.64 | 2024-12-23 00:00:00 | MSG-03 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 341ed1e8-343b-3af5-8195-34dd9c5b3308 | -4.19 | -43.65 | 2024-12-23 00:00:00 | MSG-03 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f9ede88-3d7b-395e-9a98-1d2df0bedc71 | -9.83 | -36.36 | 2024-12-23 00:00:00 | MSG-03 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a74ec0bf-9add-30be-9c6f-49e07d80ec40 | -2.6233 | -48.623699 | 2024-12-23 00:20:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a29a3b99-b4b2-3687-bc3a-10e9d5d78eeb | -4.036 | -50.0513 | 2024-12-23 00:20:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11075cdc-90fc-305d-956e-f714f5c7852d | -3.0926 | -46.560299 | 2024-12-23 00:20:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66ea9d54-cedf-38b4-9c02-6b251ca5c179 | -3.2411 | -49.124901 | 2024-12-23 00:20:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeb88253-cd63-332e-bf17-895a1aca3d5b | -2.6264 | -48.637402 | 2024-12-23 00:20:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1643618-dba7-3f9e-b47c-2b38e7f52258 | -2.6357 | -45.687401 | 2024-12-23 00:20:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2050bfb-0821-3158-80ad-95baabf430f0 | -2.5651 | -45.5588 | 2024-12-23 00:20:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb9e9521-0e88-3dae-9754-a7f1a11202f7 | -2.7179 | -46.181999 | 2024-12-23 00:20:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c59a628-9d2e-33c1-b3cb-9dd339f534c9 | -1.6782 | -45.9118 | 2024-12-23 00:20:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0bd1768c-6d71-31f8-bfc9-83e17adcf8ab | -3.1003 | -54.534801 | 2024-12-23 00:20:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3555bfd3-eb41-34d2-86b8-f7b22efce439 | -2.9991 | -51.9967 | 2024-12-23 00:20:00 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5984ed0e-595f-3520-a383-c5d63e30ec18 | -4.251 | -46.805698 | 2024-12-23 00:20:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8bb26a8d-8e2f-3eff-8e4f-d03da5804af4 | -1.6312 | -45.841499 | 2024-12-23 00:20:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1624caef-5f8f-3089-b2bd-1877e074a6d1 | -12.4393 | -41.436699 | 2024-12-23 00:20:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 53acdf28-d917-37c2-97b5-e8ef16574f64 | -11.6489 | -43.8745 | 2024-12-23 00:20:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 238b6322-df5a-38f1-9843-21813f712a70 | -2.334 | -45.583599 | 2024-12-23 00:20:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b56fe5e-9e18-3005-bc0d-fcb5c7c66895 | -2.9961 | -51.429501 | 2024-12-23 00:20:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7217a61a-dc9f-3b84-b2e7-e15febbcac4a | -2.7971 | -46.755199 | 2024-12-23 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 181a4c9e-7cb5-3eeb-b314-68f5c13cc050 | -3.7521 | -47.194099 | 2024-12-23 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce5940e6-cc1f-305f-bc46-0f075b87bc7f | -9.8235 | -36.3689 | 2024-12-23 00:20:00 | METOP-B | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 083d2b08-6e9e-3352-a6f3-65476ed82dea | -5.3534 | -46.217899 | 2024-12-23 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b780ef3-ecd4-342f-ad26-56c8c7c87739 | -2.4102 | -53.7341 | 2024-12-23 00:20:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 570230f1-b087-31f8-8052-9e989c27b7f1 | -2.408 | -53.724201 | 2024-12-23 00:20:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f61407db-a5b1-37a5-92fa-06947ecc4911 | -12.4365 | -41.4254 | 2024-12-23 00:20:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 80fd6dd5-acc6-3029-aab6-58eb9954a169 | -2.2713 | -46.391602 | 2024-12-23 00:20:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f195f77-a34a-3ac3-8828-4cadff2365de | -3.0037 | -48.119099 | 2024-12-23 00:20:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdae22cc-1719-3b4a-b7d5-41ca8d2b804c | -2.3688 | -45.916 | 2024-12-23 00:20:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94b98718-7c92-3892-b6a5-5ffd4408c503 | -11.9699 | -44.2318 | 2024-12-23 00:20:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c86cf686-65fe-32a3-9153-412bf55ab7f9 | -2.6338 | -45.678902 | 2024-12-23 00:20:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5bab530-a527-3914-b1cb-b2950be27b68 | -3.6897 | -52.4688 | 2024-12-23 00:20:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca7a7869-7342-35de-968a-72f928c0288c | -3.5037 | -47.188999 | 2024-12-23 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8647e28-5a7d-3734-a69e-34a9fa869acc | -6.1716 | -42.607899 | 2024-12-23 00:20:00 | METOP-B | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d870772-b6bc-32df-befc-238e6929d22e | -6.1744 | -42.619598 | 2024-12-23 00:20:00 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 90b988bc-842d-3312-b618-ca842709f765 | -1.6332 | -45.850101 | 2024-12-23 00:20:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 762e4502-a778-39b3-ab41-ca9cf7e8c563 | -2.2597 | -46.385899 | 2024-12-23 00:20:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce364f2-2229-3cd3-8045-b1d864d95928 | -10.5437 | -36.961498 | 2024-12-23 00:20:00 | METOP-B | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 301c83a9-9ab2-3090-9e51-a2fec8fd495f | -2.9565 | -45.739498 | 2024-12-23 00:20:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd45204a-d137-3e1e-bf36-5c7981b02f9d | -2.4004 | -53.736198 | 2024-12-23 00:20:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1460892-8ae2-3552-a88b-7e80ed767ba6 | -4.2527 | -46.813099 | 2024-12-23 00:20:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2db7d3aa-4cdb-38c5-ab2b-6cba3f46f33a | -2.9546 | -45.731098 | 2024-12-23 00:20:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49ae7807-1ed6-303e-a49b-d3151885da88 | -3.0978 | -54.523499 | 2024-12-23 00:20:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19dca116-b80d-37a6-995e-afa9fbd64ef2 | -2.6486 | -46.104198 | 2024-12-23 00:20:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eca8f361-bbba-3e6b-b882-57e29f2006e3 | -12.4463 | -41.422901 | 2024-12-23 00:20:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 00ccbcbc-aa9f-3066-97ee-498551dda410 | -3.1737 | -45.968601 | 2024-12-23 00:20:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2751a30e-5dd7-3d91-8beb-2f859a591243 | -3.894 | -44.044701 | 2024-12-23 00:20:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0a7c878-9f50-3210-a5c6-9fa9d011810d | -1.6762 | -45.903301 | 2024-12-23 00:20:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd70ac4-c04e-3a97-97a7-617c295f81d9 | -3.2694 | -49.204601 | 2024-12-23 00:20:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3859d30b-d547-3867-85a5-b2754761b4a3 | -2.2615 | -46.393799 | 2024-12-23 00:20:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91ef7447-d27d-3b3a-b2fe-430d50b7b8bf | -3.2529 | -46.044399 | 2024-12-23 00:20:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78d2e279-a6d7-3f03-a45d-a04976ab80f7 | -10.5375 | -36.937599 | 2024-12-23 00:20:00 | METOP-B | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5426148c-002e-3bc0-b41b-e48fc79df567 | -3.2489 | -48.064499 | 2024-12-23 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf73040-0e79-3693-85a7-fd185f0b5ec9 | -3.1006 | -54.582298 | 2024-12-23 00:20:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1276eb-a49e-3bb1-ac5e-55d34ffede53 | -9.8164 | -36.3419 | 2024-12-23 00:20:00 | METOP-B | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 62d2c82d-3616-3921-b898-0e60fb2bd600 | -3.3497 | -47.101002 | 2024-12-23 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3457feb-db6d-3e53-87cf-382a1f39dd60 | -2.6416 | -45.713001 | 2024-12-23 00:20:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64a2a79e-5793-3de0-a902-9590c31562e2 | -4.3175 | -45.879501 | 2024-12-23 00:20:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1bdf354e-598c-3dc2-b091-d1804db5bec5 | -3.3514 | -47.108299 | 2024-12-23 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9516001e-21e5-36a2-a8c5-f754e336bfea | -3.6379 | -50.250198 | 2024-12-23 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db4ca72b-10db-3603-adff-98c8f4631c11 | -9.8189 | -36.312199 | 2024-12-23 00:20:00 | METOP-B | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d62600ff-b386-3925-8ae8-dee3bbd0611e | -2.9978 | -51.437199 | 2024-12-23 00:20:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bb90c6b-f789-3352-afc5-4341ffcfb3ae | -9.826 | -36.339298 | 2024-12-23 00:20:00 | METOP-B | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ca92542-bfc3-3afd-b9da-af56906f1c06 | -2.6468 | -46.096001 | 2024-12-23 00:20:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bd788f57-c732-35fd-a6f0-ed01deb08c3c | -2.7954 | -46.747601 | 2024-12-23 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3873858-f5ad-334f-922e-66687260211b | -4.7171 | -43.2495 | 2024-12-23 00:20:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3af1f0f-caeb-362e-99a3-348bca4bfc9e | -3.7505 | -47.186901 | 2024-12-23 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da3993a2-a09f-3e54-92b2-cd6865c37dd1 | -10.5279 | -36.940201 | 2024-12-23 00:20:00 | METOP-B | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 55a1653e-205b-3dab-894e-1a022d40dd2f | -3.5418 | -43.591301 | 2024-12-23 00:20:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc2f78c7-271d-3b0f-9c32-e8e4e4b64200 | -3.7578 | -50.418201 | 2024-12-23 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c344ce8e-8cff-3a5a-9447-8598ef821c91 | -2.9439 | -53.041401 | 2024-12-23 00:20:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db70011c-0406-3886-b602-aa241d2e77c1 | -3.5053 | -47.196301 | 2024-12-23 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec16633-57c4-3b35-ba28-a081e616baa2 | -3.8964 | -44.054798 | 2024-12-23 00:20:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e44916ea-9bfd-3267-a2a2-6f45f6ff9692 | -2.2106 | -45.5839 | 2024-12-23 00:20:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52827ccb-5f3d-30dc-b13b-508b120b1432 | -2.2086 | -45.575199 | 2024-12-23 00:20:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37b1a22d-0ebf-3865-8d2c-75815af31ad9 | -2.6248 | -48.630501 | 2024-12-23 00:20:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ae11273-1723-3aa5-babe-c6791a251451 | -3.5393 | -43.580299 | 2024-12-23 00:20:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04495029-0f97-3f07-bc5e-cca7bccf1a75 | -12.4491 | -41.4342 | 2024-12-23 00:20:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2474a9e6-b13d-3525-80dc-08d2c9e47fa0 | -3.0909 | -54.5844 | 2024-12-23 00:20:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9408df4e-2ebe-3486-8cdb-d896263c4d87 | -10.5341 | -36.9641 | 2024-12-23 00:20:00 | METOP-B | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49aa9641-3146-3132-ab75-c8bfd2c1f46d | -2.4574 | -45.8078 | 2024-12-23 00:20:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 70c021a4-2db3-32b4-ab62-861b31549f7b | -2.1082 | -45.496201 | 2024-12-23 00:20:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6eb38e51-3b3a-3cc7-b27c-21e636c0d463 | -3.2838 | -50.507401 | 2024-12-23 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24fd654b-c988-3df6-a2c4-d9019ad11b7e | -2.2695 | -46.383701 | 2024-12-23 00:20:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6d6367-2973-363e-aaa9-498e0492db3d | -2.3669 | -45.9077 | 2024-12-23 00:20:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b15af675-c9ae-34c1-8042-2129904a66a1 | -1.1892 | -46.658901 | 2024-12-23 00:20:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e86baf8-6619-3525-bce9-a2478c75bd3c | -9.8093 | -36.3148 | 2024-12-23 00:20:00 | METOP-B | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f89bdb0b-de5c-3dbc-96c6-7b9a62a82639 | -17.83488 | -40.16389 | 2024-12-23 00:22:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 4f3c7177-71c2-3238-a47a-1688a90610f2 | -17.82587 | -40.16521 | 2024-12-23 00:22:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 348619d3-88c7-3120-b500-b80ad9582955 | -17.83359 | -40.15434 | 2024-12-23 00:22:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 39553711-007e-32e8-9e0c-f62f0ac761a6 | -16.85356 | -39.24422 | 2024-12-23 00:22:00 | TERRA_M-M | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 2b252009-70df-34ca-bb81-2bba61ec2b53 | -12.45413 | -41.44749 | 2024-12-23 00:24:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| b858e235-5363-3ddc-be7a-99a9632a3a00 | -4.077 | -44.12259 | 2024-12-23 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5173ef8c-ec10-3272-9c07-f558199338ea | -6.18337 | -42.63081 | 2024-12-23 00:24:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 76f4ecb1-31f8-311d-94e9-e94c4dddc5f8 | -7.23244 | -37.43295 | 2024-12-23 00:24:00 | TERRA_M-M | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 946d7048-4db3-3393-96da-89c87d50525a | -3.35283 | -47.10738 | 2024-12-23 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f98da5f8-0ee2-343c-aba7-ba358e2937c8 | -5.54501 | -41.74836 | 2024-12-23 00:24:00 | TERRA_M-M | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ffd19f56-478d-37dc-8f9d-730592760ce4 | -4.45237 | -45.31432 | 2024-12-23 00:24:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README2.md)
