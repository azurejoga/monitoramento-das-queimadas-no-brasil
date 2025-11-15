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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c07b4b8-1916-3688-b562-3b9b6d8172a5 | -4.7329 | -47.1573 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| cde88c71-a813-3aaf-add3-02c9ffe42157 | -2.79706 | -52.96766 | 2025-11-15 04:04:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e3bc4a6-d8d4-3890-a1f0-2d9c69fcfb73 | -7.25783 | -40.17818 | 2025-11-15 04:04:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e3548fd6-67ab-3b5b-9590-b8a0c743ae9c | -5.09748 | -37.78278 | 2025-11-15 04:04:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 56c290dd-fd54-359b-88c7-5cee74c8f35e | -4.60871 | -41.74783 | 2025-11-15 04:04:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df09124c-4c98-3051-97f3-533ae7d1abeb | -6.15021 | -48.04221 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 087b1642-4585-33d2-b2f7-ce3724992c69 | -1.0532 | -48.94506 | 2025-11-15 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 240e3959-74d2-3413-8788-e4dccc4231fd | -3.25867 | -50.09513 | 2025-11-15 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43767d45-835f-3843-9509-07f653cd68e8 | -4.47556 | -46.62481 | 2025-11-15 04:04:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73b21cc1-7f03-3d95-804d-27c18d900d82 | -6.49484 | -43.95979 | 2025-11-15 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b8b0d2c-fcee-32d4-87d9-1a3fc66b177b | -6.45724 | -45.65733 | 2025-11-15 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69f4ba30-bdb8-315b-87ee-a4e852db9382 | -3.76309 | -47.74706 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 323124e3-df95-35e0-a09a-1bd2d6dcf2be | -1.91685 | -47.9119 | 2025-11-15 04:04:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31102861-d2f9-39ac-8ac2-af2187cb6a7b | -3.79152 | -45.97747 | 2025-11-15 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f08c326-27b3-383f-ae8b-4f82bad5e799 | -6.66035 | -44.30002 | 2025-11-15 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a3f44dc-3ead-3b83-a68e-464994359467 | -5.7586 | -42.73065 | 2025-11-15 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c4b939cb-30cb-3725-b39d-20ff50effd62 | -5.6319 | -43.92258 | 2025-11-15 04:04:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b3103ba-bf84-33af-be30-c38f3bc96f96 | -4.54515 | -43.21418 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 720ee6c9-8607-35bc-8de7-4e4fa6aa0c20 | -4.59084 | -44.31769 | 2025-11-15 04:04:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b62a64c0-0313-3d45-b0dc-ca4d9411746f | -7.45345 | -42.7668 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ba8a4264-7604-3af3-83bc-d3633232fe8b | -6.1702 | -48.04563 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0cdde65f-79c4-30c9-b530-3c18e9e2656f | -7.46122 | -42.76311 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02abff8b-2599-3bbe-9f97-e2b51ee29ab7 | -4.57112 | -45.70944 | 2025-11-15 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7986458-4603-3ef6-ae04-fff99d6d153d | -6.05808 | -44.16103 | 2025-11-15 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a8c52d2-c82c-3453-9d0b-52b087c5d9a0 | -4.10659 | -50.06165 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b2d4b01-f49c-39cc-9516-2b01d70ba4d3 | -6.7458 | -41.08192 | 2025-11-15 04:04:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f937aea9-9fbc-3878-8824-798d8c6d38c3 | -5.3788 | -40.58611 | 2025-11-15 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 98d68fc2-de6f-3133-b7f3-92bfc8699a50 | -3.70797 | -46.03358 | 2025-11-15 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cce2c03-0149-3057-8d2f-245fd278477a | -4.18097 | -50.42528 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d2b5641-52d5-32b5-a9fb-b706bab7d088 | -5.31562 | -40.93843 | 2025-11-15 04:04:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39c34f51-d175-3055-89b1-db6c693b2b89 | -4.10453 | -48.01751 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e68e6e48-3379-3f52-8b75-4a9cf1a29735 | -3.66357 | -44.81624 | 2025-11-15 04:04:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d13a9369-aefb-3a0e-9891-9c12e58f0070 | -2.74243 | -45.29891 | 2025-11-15 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8e10ac6-d230-3066-9e43-0e06ef3e9313 | -5.9653 | -43.74659 | 2025-11-15 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 987680f0-8f52-3050-8f06-3aa5acb18e3d | -4.68268 | -45.8532 | 2025-11-15 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3332548b-ecff-3e79-af03-6c0cc40f7521 | -5.62807 | -43.92194 | 2025-11-15 04:04:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4222ad3a-5813-3121-be5d-fedd889c871f | -7.10511 | -39.08022 | 2025-11-15 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd38c47b-e330-3812-96b1-57f494d5cb1e | -6.31425 | -41.83216 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db1fefa4-3db8-3b5e-836c-4e7583bc03f0 | -2.95565 | -48.587 | 2025-11-15 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97ff759c-6792-3cf9-ab6d-2ce74445866a | -5.42712 | -40.66218 | 2025-11-15 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a58b9675-32dc-34f7-bbbb-7cc44592e8e1 | -5.1683 | -44.84857 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04df7317-7d83-3f07-905a-837593e56b8b | -4.64608 | -47.94905 | 2025-11-15 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 970a46f7-a547-38b6-bba2-5f2a0914a3fc | -5.52877 | -41.7668 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 70098a2c-e412-35a8-9408-86144175380d | -5.51628 | -40.97346 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9f5cae07-c5d2-36ae-8ecb-7988ffaf59b5 | -3.78955 | -43.37637 | 2025-11-15 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b2fc83d-7e6e-38be-9416-30cb1311abe9 | -3.53213 | -50.87472 | 2025-11-15 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01ae03b6-6308-3547-b28e-2f1a6189b384 | -3.99804 | -44.26323 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8aaa4923-7466-3e9d-88aa-a33222f5d955 | -5.51783 | -41.76889 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 05a54486-2f54-3b43-ba73-2f1eab23e069 | -4.55515 | -44.58929 | 2025-11-15 04:04:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f211a34-95d1-3dc0-8716-8f04d19542d8 | -7.35249 | -43.34397 | 2025-11-15 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 995c3dd7-4530-3646-a834-b83f6e63f2f3 | -3.78787 | -42.44836 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30490722-97ed-3358-bfa7-a6759bfe1ed2 | -4.8579 | -40.76096 | 2025-11-15 04:04:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 22a1683c-45dc-39c8-88e5-a0904299b99f | -4.46865 | -45.65097 | 2025-11-15 04:04:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bc9bfbe-12a0-3ba9-bcef-92a829bc90d8 | -3.37963 | -41.16038 | 2025-11-15 04:04:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 06cb34a9-cf54-3fe3-a599-d0bff1ef3113 | -7.43332 | -45.23109 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b8581fa-59b2-319f-8be0-b0e02a7ac050 | -6.25838 | -47.08457 | 2025-11-15 04:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd52db76-1603-3777-9396-6592e81e1f4a | -5.0414 | -43.61004 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c9a58a1e-6b82-3ff8-89ab-7828281ff0f9 | -4.54142 | -43.21354 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 38c1e144-3aae-3065-9105-93d73e7d1184 | -4.90782 | -44.04163 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fea96f69-c87c-3710-b533-a5157e1b8aca | -4.00532 | -47.67738 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5bc334dd-fed4-3d30-9efa-05c538ca3395 | -7.33885 | -43.35908 | 2025-11-15 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e9807f9-d1b6-350b-a5ca-c2d8c1861127 | -5.51456 | -40.98418 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 396f8e56-9359-3f3c-a9ad-8331a5b943a1 | -3.66116 | -44.81123 | 2025-11-15 04:04:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d48af795-e282-3eb1-9d27-3e5cb5a2f790 | -5.76283 | -42.72726 | 2025-11-15 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 54947fdf-6cb6-386c-bdaa-5ac61c1759d7 | -7.32225 | -42.86481 | 2025-11-15 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7d5108d7-065a-3089-816f-f8610dd8ee0b | -6.27713 | -41.73893 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a528a09-fc9f-337e-8e60-2856b144fd05 | -3.98796 | -48.00262 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bb94ffc-1add-35da-a8ef-66ac008a44c7 | -5.5185 | -40.98117 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5bd32f04-d1f2-3d07-81b2-c5b74ba4e511 | -3.28167 | -45.4623 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 899ed55e-438a-3f37-8e88-e081bc56f647 | -5.51571 | -40.97704 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 25201fbe-992a-3c09-a80f-44467e1e88ba | -5.37808 | -45.37132 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42fb22f8-52e9-3c6e-9e93-e3d6fa7b7b12 | -6.63821 | -46.54164 | 2025-11-15 04:04:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87971d4d-0107-3e56-9e31-aa3744553074 | -6.73872 | -42.96507 | 2025-11-15 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d992b8ea-6634-35e8-8758-653dbc1c4810 | -2.36463 | -46.51616 | 2025-11-15 04:04:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5589835-d117-3cc5-8785-64dbf05457cc | -5.47872 | -40.97101 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6f13e7a6-3843-31f4-ac13-25fa5e8ce35b | -5.51844 | -41.76512 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 45d9d0ff-0a54-3604-bc62-5b7209815f2e | -3.98934 | -48.00223 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9407260-a63a-383d-b58a-8843f4bbed72 | -7.34355 | -46.00984 | 2025-11-15 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bf01661-d8ea-3a6a-a595-1deff787aefc | -6.28577 | -41.72889 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 410b4288-f558-3612-a845-7bb96a36f0ee | -1.32445 | -49.14075 | 2025-11-15 04:04:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 053e2efd-8c25-3b41-9212-119d6a41ccb9 | -5.71306 | -42.34653 | 2025-11-15 04:04:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19a99240-cf8b-3a99-b27b-3eb5277ad227 | -6.27654 | -41.74263 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f290962-da4f-3827-b32e-f2296f09130e | -2.75987 | -42.57509 | 2025-11-15 04:04:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36216c75-1a3d-3a5d-99aa-92be276fda72 | -5.0401 | -43.61197 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| e46db772-007c-3025-8309-9b9eacad3d61 | -4.00076 | -47.6736 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d8b0454-843d-34e9-8f64-728b3544e49d | -2.50169 | -43.24657 | 2025-11-15 04:04:00 | NPP-375D | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 07493d13-afb3-39fe-956a-662b167da1c7 | -4.8061 | -41.612 | 2025-11-15 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b2a0dd3-ae83-3492-9bbe-444f7f06851d | -3.6541 | -44.79519 | 2025-11-15 04:04:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bafefe4b-58b9-3c34-a964-f6eba4ec9060 | -3.99524 | -47.67559 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4a29d63-9201-3b11-a7ae-5651d26eb172 | -5.33082 | -43.03916 | 2025-11-15 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e456a774-8908-3c44-b4f7-81cc213bf1b5 | -5.42806 | -42.57342 | 2025-11-15 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5ae4aab7-fa5a-3899-92c9-88f432087a64 | -5.51466 | -44.39391 | 2025-11-15 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bb1bef6-9032-3f99-957b-1203b48ed96f | -2.88529 | -51.42927 | 2025-11-15 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 013d9fde-d968-3b8f-ba1c-9b872dd86744 | -6.11266 | -41.52408 | 2025-11-15 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| be400303-074e-38c2-8e02-27e486495b15 | -6.51368 | -43.40356 | 2025-11-15 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e387135f-f7f7-3bce-8e9a-0ce1d4149104 | -2.5028 | -43.2488 | 2025-11-15 04:04:00 | NPP-375D | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c17d0eee-bd06-3937-afff-b384ac9e1085 | -3.6647 | -44.8157 | 2025-11-15 04:04:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f2242784-c8d8-385b-8807-21558f8740f3 | -6.29827 | -41.82616 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b95d413-79bf-3fbe-89a2-2eb7b42b4c7e | -7.65676 | -40.03102 | 2025-11-15 04:04:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3b5f5594-2a76-33e5-8388-7c5438ed7c8f | -7.46113 | -42.76402 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README23.md)
