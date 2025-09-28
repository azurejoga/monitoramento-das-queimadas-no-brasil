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
| 7e87c8cd-3955-35ca-8bc3-dd05f0c25b80 | -5.89411 | -46.04503 | 2025-09-28 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca1eca8c-122e-328d-8805-e478362823fa | -6.11843 | -41.81005 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ac05623f-f148-3bbd-bef3-f07d1c160bcb | -5.08852 | -37.60663 | 2025-09-28 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 26164b43-fe39-3773-a5ad-aa49e7bed1f7 | -6.40801 | -43.95845 | 2025-09-28 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4866940c-cc9d-3f02-a0f0-cb44751c3762 | -5.74944 | -42.88531 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2b0a80d8-1812-3c7d-b219-8f6894d6ec2c | -5.81712 | -42.81409 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| a589d39e-eda1-34f0-ae3d-0496fd8baa77 | -8.82797 | -46.21229 | 2025-09-28 03:36:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d0ce9d8-cde9-3efc-b9ae-10dee7c9ca37 | -6.46343 | -44.22377 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 960f881b-dd01-3d35-9c1d-de116990ace9 | -8.6556 | -43.98798 | 2025-09-28 03:36:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b882b2de-d5ac-3a0c-a147-780b23b58c8a | -5.7147 | -42.65481 | 2025-09-28 03:36:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0abacef3-289e-3dea-a138-ade11444cd46 | -8.49902 | -44.72161 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6793794e-a7f7-333d-8cdd-1c7cd1836709 | -7.10718 | -44.23746 | 2025-09-28 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f393a81-91ea-3797-87cb-e9da1b5b20ea | -5.73604 | -42.83586 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1bb94cc3-51dd-303b-a368-c3c53f2aefd7 | -7.17095 | -45.4995 | 2025-09-28 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e90c7e3-f6e9-3b70-b7b3-2c27f423c150 | -8.49243 | -44.72488 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1ec145d0-986d-3b9f-b1af-694404a19659 | -6.76367 | -45.52738 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| efd21a8b-26fe-3de9-8c3e-750fd66477bb | -6.70779 | -44.5885 | 2025-09-28 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a88addd-a7c1-34ce-848a-99c56c70f1b1 | -8.2856 | -45.43544 | 2025-09-28 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6331548c-f8e4-307b-90e0-40a938b10dfd | -5.73893 | -42.85072 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 908a5373-85c5-371a-add2-90c59a0741fd | -7.29404 | -38.12112 | 2025-09-28 03:36:00 | NOAA-21 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| acc9a51c-4b14-30df-877f-54ddbe0fdb0b | -5.764 | -42.80263 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c43d822f-5566-320a-a156-04633f5e5997 | -7.53341 | -46.09756 | 2025-09-28 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dad40d45-f58e-3d5f-b03d-d7d82f19907a | -7.23743 | -44.77042 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9feeb486-d668-3813-a897-a81758ad343d | -5.90841 | -42.94238 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 26584ed0-a515-3076-89d1-00fad619c35c | -5.80038 | -42.84719 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 71eeb05f-c665-3482-90a4-2d218320ee6c | -5.73296 | -42.8532 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5173fdf4-8df4-34f0-b9c3-9e5c27291b5d | -5.46414 | -41.07396 | 2025-09-28 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 913fb0a8-8caf-33d7-9686-2776001298db | -6.17791 | -44.11453 | 2025-09-28 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0a45f3f-a687-3b6a-9bd0-fa62e5289ce3 | -7.04082 | -44.76791 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e4fac059-72cc-3f9e-925d-71b46255a96d | -6.27265 | -42.49181 | 2025-09-28 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c8a520d1-7c1e-3972-836b-b3d9267313d0 | -8.28381 | -45.44477 | 2025-09-28 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb5e51ca-a3ba-3d1d-99b4-5bf0b2db3b03 | -7.10821 | -44.23676 | 2025-09-28 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d76462e-6f0c-340e-b43b-2caa428c4e25 | -7.75036 | -47.01079 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| afebac5d-f25e-3e8f-8648-61f1dd4b271d | -8.2724 | -45.47153 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3b462e9e-e449-37cd-9b01-368400cd0794 | -6.70034 | -44.60813 | 2025-09-28 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f81a7fb5-da48-349c-b21e-04566b9380e4 | -6.32183 | -41.88161 | 2025-09-28 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 490482cb-4ed9-3b8f-bb98-22a3d53e1786 | -5.94628 | -42.90029 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 204dd9ff-7dc5-3014-bfcf-e1066dd52630 | -6.7869 | -44.08638 | 2025-09-28 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 9551f627-c691-3e98-8ca5-2496f0e40894 | -8.28727 | -45.45965 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6cb2921a-6509-36e9-a6ce-0aa9b5a04aca | -8.6558 | -43.98805 | 2025-09-28 03:36:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43ef24f4-01d9-39e4-900a-9f4efd7fcd86 | -7.25012 | -44.76807 | 2025-09-28 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee684c9f-c7c7-33c2-92b5-42904897f66f | -5.81286 | -42.80684 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1c5d8c13-507f-3694-8af6-aa9c44248fe4 | -6.43038 | -43.07708 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a882734-e0f7-35e2-b972-53a83549f0e0 | -5.80097 | -42.84375 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| b8a22912-1f57-3d0e-be11-697464ab3e2a | -5.8216 | -42.62983 | 2025-09-28 03:36:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 530d8b79-d575-3ba7-8414-1eef31c33b2d | -6.29298 | -39.82368 | 2025-09-28 03:36:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 990340ac-2ac8-3f98-a054-fa0cc2bf7fb5 | -5.64497 | -44.92921 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ab68cba6-b5f2-3a06-8e6b-c77084f021ad | -7.78995 | -46.99986 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4d8662b3-c3bd-3dca-ad19-20c8eaba53a0 | -5.73502 | -42.857 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a64c4f76-6057-356a-8e98-658fa62440e7 | -8.48274 | -47.81127 | 2025-09-28 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4136fde4-521e-36f3-8c87-51965e8df5d6 | -6.32251 | -41.88159 | 2025-09-28 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ff04af62-c6c8-392c-bb31-49e73a724681 | -5.69802 | -42.62519 | 2025-09-28 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4f217d79-f375-321b-b782-709a561e977d | -5.81968 | -44.44537 | 2025-09-28 03:36:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b73e7765-ae1e-305a-adf5-ed33475dcdb4 | -6.42843 | -43.51091 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0d222711-a472-3b97-86ad-41a8bc3aab64 | -6.91992 | -39.58567 | 2025-09-28 03:36:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 5f8ea4e1-ef38-349c-b2b2-68c43f16a9b7 | -5.70827 | -42.66037 | 2025-09-28 03:36:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 49b1d1c9-08f0-3a22-9e9e-e0f14b0b5cb8 | -6.08516 | -42.63781 | 2025-09-28 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 57dd15d7-ecd4-3f72-a727-79ea8877bed1 | -7.32385 | -45.98968 | 2025-09-28 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 525c9ebd-318f-3885-b433-55aff178ec86 | -5.78667 | -42.89437 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b9920e20-de55-39df-894e-e55791e58bdc | -6.70528 | -44.58032 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1193930f-19c3-30a0-9d66-38c709686c51 | -6.1115 | -41.8162 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2f578d80-339b-340e-8377-3f866f4ff18f | -7.43555 | -43.18933 | 2025-09-28 03:36:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 004b06ff-b82e-3c0a-a52f-3fd7dae63c72 | -7.26028 | -42.99145 | 2025-09-28 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a3e0b0a-155c-3129-a5e8-0cabbcb7d892 | -5.76527 | -42.79539 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5293378e-42eb-3320-8085-f323aefb97ab | -8.83105 | -45.9942 | 2025-09-28 03:36:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f346673f-693e-3ee1-93ee-01ec1160b1fe | -6.47727 | -44.51539 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 168cf7c1-9155-3bf0-8ea7-a83a860222fc | -4.91421 | -37.48639 | 2025-09-28 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 58f7a3ca-0347-33b8-8723-b65018e412f6 | -6.20451 | -42.84948 | 2025-09-28 03:36:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f706eaed-8c6c-3482-a0e1-8fce9a866b77 | -6.49029 | -44.24083 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 163f45a9-44a4-3da5-9b48-0d2065bf2bcd | -5.74082 | -42.84009 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 31c78d5f-19ce-33ac-aa64-3918cccdd140 | -5.76338 | -42.83752 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 613e7608-fedd-3eba-90bb-9283403bc7a8 | -5.81225 | -42.81037 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| a144d4c0-c35a-36dc-95db-6fb664f0601c | -6.42776 | -43.5147 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b4e62d43-3bcc-3d70-8b18-7cc1b96e3085 | -6.11649 | -41.81699 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0d9281f3-b6e7-3a55-9337-9f36d91d63fd | -5.75517 | -42.82142 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 53c7a244-7495-3c4e-8e67-9afbfc3dd0dc | -7.86805 | -44.56903 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 405d7c0d-a9bd-3dd8-9619-f6b5eb2a7c4d | -5.80992 | -42.82391 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b1e2c8cc-d25a-3ce3-a413-845ed4a56f7c | -7.48872 | -37.13235 | 2025-09-28 03:36:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df19e6cc-999d-317b-9296-dc98d290a06a | -6.76887 | -41.75291 | 2025-09-28 03:36:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 87a457bf-c5d2-3b32-9c0f-3570546096d3 | -5.7587 | -42.83275 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 3117a411-5753-3b03-93cd-62b3f3f87bc3 | -6.30317 | -45.89374 | 2025-09-28 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da3f98f5-9be0-32b7-ae7a-400ec72897c9 | -7.42721 | -40.07558 | 2025-09-28 03:36:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b256a3f2-da54-30dc-bf95-951cf2143b01 | -6.06143 | -44.86258 | 2025-09-28 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d2d9688-c988-3842-8713-1887d1bdef64 | -6.0744 | -42.44987 | 2025-09-28 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd459733-61bd-3ccc-8fd0-ab6b8dbc57e6 | -5.46236 | -41.08452 | 2025-09-28 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 9bd5fbb2-9d45-37ab-8391-a35d9bd99d84 | -3.80493 | -41.56863 | 2025-09-28 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 8b5eef23-c659-3c28-9d3d-343384cd7272 | -5.88102 | -43.20326 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fe076748-7270-3cda-8948-ad423f62e3f2 | -7.70758 | -41.29095 | 2025-09-28 03:36:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| efe706a2-b852-3478-a6d7-d90b3f394759 | -5.74858 | -42.82747 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5c5b104b-41ff-3f51-9949-7165312dbe2f | -5.73828 | -42.85437 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6bbb5e7d-73ab-338c-912c-ba09e00bd8dc | -6.76177 | -44.59378 | 2025-09-28 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 38bcb926-83e0-335b-a3d2-8ef27d100319 | -5.60143 | -43.37284 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 30fd262e-6584-3629-b77e-153dfc01f4b7 | -4.86224 | -45.75405 | 2025-09-28 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9fefbdb1-967a-3f3d-85a9-183eaecab01a | -5.81472 | -42.79605 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3dbb5e79-f3a9-3711-b590-05c7164edc89 | -8.50327 | -44.73105 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cbda531-25f5-3027-8d79-2928f65fdea0 | -5.75629 | -42.81509 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 306aae53-9fbd-3e00-9df2-9bc35faf03b2 | -5.903 | -42.94156 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 446c38de-0cbd-39a1-ac56-c38c45ffdc01 | -6.40409 | -44.2891 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afb71fb1-33c2-30b1-98ad-63e5a5fb06ad | -6.3268 | -41.88253 | 2025-09-28 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a13b002-d32c-311f-ab0a-80bb211d022e | -6.42977 | -43.08057 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
