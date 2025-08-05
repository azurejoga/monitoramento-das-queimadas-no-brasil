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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 840fc34c-be67-378a-864a-58c5eadc6786 | -11.81748 | -44.25718 | 2025-08-05 04:40:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c56f96a-8438-3b4b-ac8e-aed002f7094e | -12.70901 | -48.08573 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63c95e66-ba29-3312-84e7-140710526437 | -10.9091 | -48.36202 | 2025-08-05 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccf910ff-3bfa-3038-a1a9-18270e86f88d | -10.77339 | -48.79829 | 2025-08-05 04:40:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abc19df4-88b3-33a8-85c3-2b2b157caabb | -11.15655 | -49.70352 | 2025-08-05 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fa03aba-4323-3911-837b-b296cd52ee55 | -10.90795 | -48.3697 | 2025-08-05 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ade8ffd4-76ac-3ce7-a330-4e29236390a1 | -10.47208 | -44.3844 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2e96d4e-5855-31b3-bbfb-84b0df114ea7 | -13.06337 | -56.87833 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f556dde7-9092-3c43-b82c-c181b1c30cce | -11.7471 | -45.00375 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04fd7587-da10-3012-8cd5-6b6258409548 | -11.75401 | -47.54139 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 36cfaa74-9ca4-356e-80b1-29aa7c3ac1b6 | -12.67875 | -48.11855 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a80338a-ce4c-38ec-a56f-ccb46c36fbee | -11.75724 | -44.96152 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 983a20ab-53ed-366a-9dbd-450e83a289ee | -11.04127 | -47.61774 | 2025-08-05 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e7d4671-15d9-38e4-b0ab-867aabfabb32 | -12.43467 | -48.71305 | 2025-08-05 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b86b99d5-969e-3f14-9ebd-ae99da6d8188 | -13.06391 | -56.90237 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faa4b3a4-4739-3ac2-be53-71d317ee8aa8 | -11.74871 | -44.99208 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70d57f68-8d46-3798-9908-523d6307d5d0 | -11.74764 | -44.99984 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36f800df-7005-3aaa-858c-64861b9f48a2 | -11.3255 | -47.30952 | 2025-08-05 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e061cc1-67c2-3163-98d5-fd6f5c546809 | -10.91774 | -48.37518 | 2025-08-05 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a66be32a-d200-3f1e-bdf7-c0be40d7b873 | -11.79099 | -44.9975 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 727cae2a-ec3c-301a-993f-d70cf98c3c44 | -13.2427 | -46.85085 | 2025-08-05 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 507f0ef6-22e0-3898-a798-a77895d02258 | -9.71179 | -51.93752 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 606a3a7e-a99c-3cfa-83b5-2836fb6e8435 | -12.71435 | -48.09889 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 560c315d-398f-3b3c-87ee-8de468dc355a | -12.72389 | -46.39283 | 2025-08-05 04:40:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| feddeaf8-4524-39f2-a140-7f8f3dd54dff | -10.4436 | -44.36777 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d268f65-b396-33b1-8c9f-fad230489b63 | -11.75668 | -44.96555 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f4b959d-03c8-3bcf-967d-163f3214a36a | -10.78869 | -46.64717 | 2025-08-05 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98db663f-4d40-3b58-b58b-728ef7ff38ec | -12.71552 | -48.09092 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 361751a9-5e5a-3733-b249-fdaf37ca5fff | -13.055 | -56.87673 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 82fb3357-45b5-3f5c-af5b-1f6c8e951a49 | -12.68942 | -48.12012 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bfb919c-903e-3443-aa5d-db4091bf4af7 | -9.69765 | -51.93892 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 961fe6f6-f11b-3ca6-8885-11bc667eec8d | -10.46346 | -44.3831 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf057097-dcdc-3c13-b7cd-ff4846bc5ed0 | -15.82784 | -44.03237 | 2025-08-05 04:40:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e58d36b9-5cb8-3e4d-a118-8f8952d4ea2e | -12.7179 | -48.09948 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48d03f0b-604f-3f81-8b41-a1e2c18ece08 | -13.04028 | -56.91092 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d2c12af-6aca-38b2-834a-d75ff42b7039 | -15.77358 | -49.96011 | 2025-08-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8780d8e1-c7c6-3a8c-89bf-666aa38ed364 | -11.76455 | -44.97096 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cbf18e1-4dc1-3e19-a626-0f5b641877e1 | -12.22368 | -44.19373 | 2025-08-05 04:40:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32d24512-ad64-3671-923c-a64cf47e2975 | -11.92982 | -44.9586 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3209f922-565e-3556-94b0-f801580c8a70 | -10.47001 | -44.38324 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a69f1056-c62b-3904-8384-22fa80a8b00f | -11.71551 | -47.77475 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfac09a5-0e22-3641-ab9b-05667d7c7b35 | -10.48565 | -51.86122 | 2025-08-05 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7881002-43d5-339e-b6b7-358ec3d5b151 | -12.6817 | -48.12325 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab1cb721-1eaf-3646-a453-08a218c495c6 | -13.05986 | -56.87721 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8983d33d-cc41-3df3-bb59-3b4f5e665680 | -9.71239 | -51.93385 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd794134-cb23-37a0-8dd0-07b06fc9d3e6 | -10.44999 | -44.38501 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81f8a83c-d8f0-3297-ae7d-facd20f7abf8 | -14.47009 | -52.08549 | 2025-08-05 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6527e951-528b-373e-8b9d-6a6ce3f58507 | -10.78094 | -45.50784 | 2025-08-05 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5515690b-42aa-3b3e-bddd-7b18fd607971 | -10.7881 | -46.51992 | 2025-08-05 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a22a895a-2954-371b-ace6-7884ff636ed8 | -12.03507 | -44.77935 | 2025-08-05 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5300cda-427b-3e7d-bf0a-4a83f056a7ed | -12.71612 | -48.08687 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6615c81-ae82-3d6f-80d6-b9f33373a0f0 | -11.75023 | -45.01218 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d30ce104-e490-3158-9a75-5d4482b57f84 | -11.76512 | -44.96684 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f7d5217-12f4-359d-8bbe-b815744a5f0e | -10.3421 | -44.90801 | 2025-08-05 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2f3ff44-7bf9-3828-b9e2-a4c06dec223b | -12.72778 | -46.39351 | 2025-08-05 04:40:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 954a526d-8bc2-3abf-b295-28bc89a5878e | -10.47436 | -44.36832 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53c006f3-f5f7-3a81-aab3-09136dcbf732 | -12.38717 | -47.05734 | 2025-08-05 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67cdcdea-cc4c-3273-a0b0-cc6d58b23e67 | -10.45375 | -44.38954 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d224bf6f-613a-3c8d-adfc-2a79be44511a | -10.33107 | -47.82806 | 2025-08-05 04:40:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5c16001e-3343-3c4d-af6d-427fa4865408 | -10.95838 | -48.15122 | 2025-08-05 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c107b9d-e17d-3fd8-92b0-13ddd5f4d091 | -12.51515 | -47.18609 | 2025-08-05 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba17daa2-657b-38ce-be10-fb2f02a24b61 | -11.78979 | -45.00603 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abc4b30c-c7b1-37f7-91f3-542b9d24497e | -10.46552 | -44.33732 | 2025-08-05 04:40:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0fb879d-400b-3522-9cd8-268cb312b8a0 | -13.0494 | -56.8839 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87f624ed-2496-3ed3-86da-a671b3dca6b3 | -12.70545 | -48.08515 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b50284e0-d218-3442-b23c-80b04f8d979c | -11.91393 | -44.94822 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03b73ce7-0022-353c-9399-7e8bc7db7a4a | -11.19108 | -51.46957 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc126b1d-86e8-36d2-bef7-bda1479956e9 | -11.78999 | -45.005 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de9d9009-eac8-3921-9ac6-3407747471fb | -10.44848 | -44.3644 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd09209f-0562-3469-8412-f57ab810a459 | -13.04868 | -56.91246 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bee45668-ab67-3345-859a-885d8ba15ea2 | -13.04241 | -56.87446 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9189642a-ced4-3418-9911-e22ab0d69bb2 | -12.72765 | -45.07861 | 2025-08-05 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dc350c54-7d5f-3674-a759-6c13805dc53a | -11.78626 | -45.0007 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 707852bc-dcca-3fdd-a19b-5fcc417972ee | -12.68525 | -48.12378 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a04d1dcf-626e-33cf-8ab2-eb1884b5b3d3 | -11.92131 | -44.95761 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f7626cce-4586-3cc3-be76-b100be4880f0 | -13.0564 | -56.87249 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0428e83b-cf47-3455-9533-516e1140fb92 | -10.66505 | -55.31348 | 2025-08-05 04:40:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dde9ec2-8e99-368f-b677-abd664865a73 | -10.44905 | -44.36033 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19eca5f5-ea2b-3105-b874-eb70f853ab02 | -11.74969 | -45.01607 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7e90b86-11af-36de-928d-b4f65c67717b | -11.27912 | -52.75943 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 837c9760-5ce2-32fa-bc92-28f672710f0b | -10.19527 | -53.89336 | 2025-08-05 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3412ed2d-9ddf-31f9-9447-8a10a4e5f35b | -11.75866 | -45.01342 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07ae34bf-c6a4-3b58-8074-462be5d1873c | -13.06332 | -56.88192 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b634ece6-2373-3711-814f-c67c8f1c4e70 | -17.37765 | -44.99127 | 2025-08-05 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2a28d3a-3213-3274-ae4f-098c074dcfab | -10.32756 | -47.82748 | 2025-08-05 04:40:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| acbbde7c-f8af-394a-9289-20614dce63ef | -13.06268 | -56.88225 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92836cff-816b-3981-aa6d-f2b906449da8 | -9.65806 | -47.1254 | 2025-08-05 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b042d76-b705-358a-b61b-5097565c409d | -11.8545 | -50.56358 | 2025-08-05 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a70d707-5a40-365e-8cb0-e1af4a601c0b | -12.64589 | -44.49381 | 2025-08-05 04:40:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a797fb6-828d-3929-b93a-a2b74b47445c | -11.27583 | -44.64208 | 2025-08-05 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdbb4754-b263-3985-b7e6-b4191c7aa8a3 | -12.70254 | -48.08019 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dee56b2-b703-3a5c-810f-6a43d4f8e951 | -9.69706 | -51.94258 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2abbc37d-7b43-3f97-b2dc-7099216f0581 | -11.92503 | -44.96211 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 136414ee-5b5f-3f0b-9a1a-26947eaab50c | -12.69899 | -48.07956 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cea5904-0c47-388d-96fb-700ad2924a2a | -10.47163 | -44.37123 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fbd9228-1873-3c69-8fb9-de6b513ded42 | -12.71376 | -48.10287 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dea46234-5b55-33fd-8d8d-a51796e13721 | -11.75248 | -44.96474 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27c298fd-34e6-3866-83c5-4f56cd66a9b4 | -17.37757 | -44.99324 | 2025-08-05 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd0f96ae-c07a-3a53-b4b3-ba914e0645b9 | -14.05012 | -41.99077 | 2025-08-05 04:40:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 05dacb05-1144-325e-8467-e16d2bf73eab | -11.91229 | -44.96049 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README26.md)
