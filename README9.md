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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74ce21bd-5436-3fd4-b087-a9d3a4d53823 | -10.26898 | -46.0569 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b48d23cd-8ca0-3bf8-89fa-15af4a88f8b8 | -7.21774 | -43.75066 | 2025-09-21 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 794a6cda-104b-31a1-b3cf-090632aa4aff | -6.59513 | -43.57971 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23e64eac-4f9f-39b2-9869-d086435903b1 | -6.19519 | -44.05653 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09148876-9475-360c-8823-d68482de83db | -9.84691 | -46.12783 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 966736d9-9dd0-39fb-8916-a489f94382a4 | -5.47304 | -44.41434 | 2025-09-21 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deb0fd9c-f077-3404-a8ea-7f5e0e61ef54 | -7.3811 | -47.04715 | 2025-09-21 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a151743-653a-3bfe-b905-04b9697c6563 | -6.09022 | -41.00255 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 114e73af-5bba-3421-91b8-ce8df4b787aa | -6.69435 | -44.09505 | 2025-09-21 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 892fe4b4-ecdb-36f8-9ba3-6cd9a0c1e66e | -5.52062 | -43.86587 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f9e5af10-89f5-357e-aa60-b3cf6d6913de | -7.91701 | -44.09909 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d2a0081-3567-3054-9cc2-07cd76414bad | -5.42159 | -43.27366 | 2025-09-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f5668ca-2a44-3f2b-915a-c070b87c844f | -8.48798 | -39.93085 | 2025-09-21 04:08:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d7aaa888-e41f-3ae5-b7c5-04d7e29063c8 | -10.70465 | -41.86402 | 2025-09-21 04:08:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fb4327fa-1814-38df-8963-8cbcf0093f39 | -6.30888 | -42.36433 | 2025-09-21 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| bb26e8c4-dc70-3af4-ac75-17d94ae2bd8a | -5.43085 | -45.5065 | 2025-09-21 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7474919-c6cf-30d1-b34d-0133b55cf45b | -3.80871 | -47.57431 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99c68b5a-458f-32e5-8254-7975f87a70e8 | -10.03815 | -46.26255 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 321a85b6-f792-36ca-9996-35061807c26b | -5.8276 | -49.9148 | 2025-09-21 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f3eced3-36e0-3f62-8c38-278a54d8e990 | -5.82708 | -49.91775 | 2025-09-21 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe8c475c-dbde-3d04-9822-bd6565c9309a | -6.83799 | -39.08236 | 2025-09-21 04:08:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 29f15e14-732b-3989-82b1-c1c3f6fdda1b | -5.28061 | -44.72182 | 2025-09-21 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccf96ef4-44dc-3153-aa1e-fb6e33bceff6 | -5.34074 | -43.36008 | 2025-09-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 701f5ece-cbc1-335b-8659-6f232a936f43 | -3.35641 | -48.39216 | 2025-09-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6253a5ff-6370-338b-87f7-92acb3c0cbd8 | -9.21229 | -40.2423 | 2025-09-21 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d1130788-8f10-3916-9c2b-837d058a50d4 | -5.05143 | -40.92067 | 2025-09-21 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3b883982-913d-3d55-a7b8-7892a9990963 | -3.62574 | -47.52817 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17b9f2f9-88bf-3bae-b137-cb740f5a1b3b | -3.36699 | -50.39418 | 2025-09-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e395974b-a41f-3dbb-9cbd-fd067899a07b | -10.2908 | -46.08178 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 248acc5c-7d37-35b0-9d5d-31fcb13d5f80 | -11.4838 | -43.55984 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0578a295-fafa-3e0e-b07f-da236ea4ddc7 | -6.93971 | -41.88253 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1df51ed9-ed18-363b-bf01-3c37e0e6850a | -7.42304 | -44.54499 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f786327-6c47-38b7-851b-aaf52ee4194d | -4.33067 | -48.38887 | 2025-09-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e5e354e-f9ef-399a-9826-2860b0bf9f10 | -6.54054 | -44.27499 | 2025-09-21 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d746926f-f580-3347-ba85-2d8d18ca29ca | -7.92487 | -44.11582 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e72800e-6656-3810-ba90-308a56ce3d8d | -6.54999 | -43.53091 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f625ca51-7709-376f-96b9-94352b141d77 | -5.6508 | -51.46859 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97dc4df0-93f3-385b-bb7b-4174e685228c | -10.35376 | -47.89769 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 162267fb-888a-3082-a6b6-b156b3436a03 | -7.9261 | -44.10828 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 375b79cd-4ad4-3a56-a5ff-b405fb00f744 | -6.19991 | -44.04945 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6634aa71-b00d-30bd-8419-e0f13697b76b | -6.42125 | -43.85204 | 2025-09-21 04:08:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e592f472-2901-3377-8ed9-592f5dbd7c91 | -7.93419 | -44.10185 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| feb167dd-18e8-3322-8cda-b396c70db6ed | -10.33803 | -47.8913 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf7366c3-af0f-303d-bf96-1e44bb6576ea | -6.41717 | -43.85536 | 2025-09-21 04:08:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60404d4b-19be-34a2-81f3-eea05eaeca9b | -3.76282 | -54.82011 | 2025-09-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee6e184a-be91-3c4c-b568-e5f5afa30665 | -7.73173 | -44.43584 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f2d2b7f-7474-3715-ae15-7e142ce76038 | -7.65518 | -45.12357 | 2025-09-21 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d27ad9a-762e-343d-a0d5-53a696c16fcb | -7.80209 | -47.60202 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61387720-a5b0-3349-b258-c5e1ec2fc5b8 | -4.29748 | -48.27194 | 2025-09-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20494a96-2819-3a87-82ef-6a790ebc78c1 | -7.80627 | -47.60271 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a9d1ab9-a3cd-3e1b-bcb7-f1a9368d2eda | -8.18203 | -42.37857 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| baf6422b-1e69-3e17-ade6-71dae767bcca | -7.19445 | -37.22851 | 2025-09-21 04:08:00 | NOAA-21 | CACIMBA DE AREIA | PARAÍBA | Brasil | 2503407 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d8fdaf2-767a-31e3-be8c-4b157183deaf | -10.02258 | -46.26416 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ab90d07-913a-3ef4-bac9-ad8212909ee9 | -7.112 | -44.98033 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8225e9f-f19a-32d2-8359-6d75d4db3663 | -5.01429 | -45.20209 | 2025-09-21 04:08:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 646bb27a-85bf-3016-9f8d-924b415b3545 | -10.36254 | -47.8956 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e69cbce-0ba2-3ff2-8a7b-e703691c2de0 | -5.75838 | -44.19855 | 2025-09-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 845d0a35-8fab-3142-9bd2-ba6a2463d41f | -7.92549 | -44.11205 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79f2a005-811a-3747-b9af-8dfc79671ba4 | -9.42415 | -44.70439 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a1da503-3209-3b0a-9691-54580b9635d9 | -11.48987 | -43.56445 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ceaad0c7-5ee1-327b-b0ba-cfa769f47a10 | -6.39037 | -45.3245 | 2025-09-21 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 268bd853-363a-3104-9338-5b4ead865010 | -4.93678 | -45.08103 | 2025-09-21 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 100681d7-77ee-3258-8aa2-a9972fe79c46 | -5.42737 | -43.25944 | 2025-09-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e2da73b-e3e2-3cb0-b1e5-ea9ce8ed87c2 | -7.61749 | -44.44638 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efcf2a28-4e31-3b1a-806a-78b908fbadd0 | -6.59676 | -43.59135 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aca144b3-b3db-3351-a9d4-1c4a375b7e9c | -6.19942 | -41.19686 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 80c13f7b-d1b9-3e73-bdbe-790577da5d54 | -8.59883 | -45.34621 | 2025-09-21 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 17cbeb33-0234-3d50-9be5-f9e88fd89c72 | -10.27851 | -46.06761 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58bd8ab0-6d49-316a-8665-ed6b7942300f | -7.7266 | -44.46711 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a04b6302-50ca-331a-a302-e8f4272a6b6a | -3.60358 | -47.53066 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 270b0ab0-5e76-3507-ab02-1de65450798d | -4.80082 | -47.28509 | 2025-09-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd55a214-fab4-315c-a4cf-1640e8ec9dbf | -8.70647 | -45.26435 | 2025-09-21 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8de37103-28e6-30ce-adde-25cf087eaff9 | -10.99111 | -44.4994 | 2025-09-21 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bffe81e-2d2e-3c45-8f6b-5bf366f70b98 | -7.62228 | -44.43904 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e352e66-8a89-3ca6-b6a8-e83367cca4f4 | -8.35527 | -44.70712 | 2025-09-21 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e25081f3-f259-3b15-a207-b27bf24e4357 | -7.59757 | -45.49659 | 2025-09-21 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2d06265-cde9-35a2-825c-92add732b34b | -5.27154 | -45.05326 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc1cff09-a5de-33b3-8a4e-602ae368c69a | -5.34669 | -45.00469 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b7b22a3-e537-3d22-90ba-e80ea5964b5a | -7.77049 | -44.17752 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9c858dc-d212-3704-99b1-02d310210299 | -3.62724 | -47.52551 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7466b014-3e11-3ab8-b6d2-2a68a61161da | -6.08968 | -41.00601 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e0f5e422-77e1-3b99-a0c0-03dbca483667 | -5.69615 | -51.76114 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4b8df626-dfce-3ad3-a176-9e2e945c5766 | -4.85608 | -45.89669 | 2025-09-21 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c502d1e4-7f05-3851-8b7b-034c44fc7d4e | -5.9009 | -44.35044 | 2025-09-21 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d395eaf7-ec4c-3038-8361-30f50be461a3 | -10.23841 | -44.97898 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05ec0ae7-3d2b-3264-b5e7-3221efe87f36 | -4.19724 | -48.55142 | 2025-09-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 53ed392a-d2f7-3a22-906b-9b1395bc4286 | -6.96132 | -44.75038 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38cf94f5-3672-394e-acec-98740fcec003 | -6.59395 | -43.58704 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09ef6b04-95d0-356b-80e3-fad0bee002eb | -10.35092 | -47.88977 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| febe5d37-406e-384b-88ff-312fa3ff3f0f | -5.53237 | -43.87093 | 2025-09-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc58aa32-bf79-33dd-b6f3-0089f8ae8ef2 | -6.69088 | -44.0945 | 2025-09-21 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9750686c-f706-321c-8ba7-6e4f52340abb | -4.70966 | -46.46914 | 2025-09-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67b81ad5-8ea1-329e-8c47-4893895014b3 | -10.02474 | -46.27387 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22e55eaf-989c-3db7-9e67-27c8484290b9 | -10.36538 | -47.9035 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 47c9cca6-815e-3e04-8555-1d91f26e1b9c | -5.63031 | -45.94301 | 2025-09-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb1c24bd-3060-3e66-8463-b03ace34b1cc | -4.5138 | -43.52127 | 2025-09-21 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 594a7559-9a6f-35ca-b2b4-886d607d3356 | -5.52254 | -43.86551 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f678384b-f109-34ba-8c4e-c6751baa7e34 | -5.74903 | -43.37825 | 2025-09-21 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0954d65e-8d19-36d4-843e-eb2bd1f27a28 | -4.99985 | -47.28795 | 2025-09-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f022f54-a7c9-3502-bf89-4f823c904f6b | -5.86828 | -42.5019 | 2025-09-21 04:08:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README10.md)
