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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d2459cc-3ad7-312c-99bf-f3f1c7f530f6 | -6.09106 | -41.52993 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 55aede68-bafa-3e95-8684-6c9d3bcd3f22 | -12.06673 | -48.21864 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 722e8a50-1c35-34b1-a3fc-f09e41b1029f | -10.1692 | -44.50028 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b02c7b6-43f3-344c-8e5e-e85234e565ea | -7.05121 | -39.62832 | 2025-11-16 04:08:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| df5f4964-9bce-3cd2-ae90-916fae4426c7 | -9.83495 | -44.18309 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7d96b7b-6a0c-3fc7-86a4-f505913c6907 | -10.65964 | -44.26806 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80057554-a703-3e69-ae31-5bcc291e863e | -6.36181 | -39.62395 | 2025-11-16 04:08:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2d1a5b94-31be-329e-ac44-e4cd6a82f6c3 | -10.83666 | -44.64316 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cda1b745-3683-3114-8f5a-f27167a7fddf | -8.6352 | -39.9398 | 2025-11-16 04:08:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 312f9a66-45ff-3fef-be9a-6c490cfde3d9 | -8.86738 | -50.19321 | 2025-11-16 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4159ef11-d3b9-3714-9b13-0f6e0f9af86b | -8.05581 | -43.10402 | 2025-11-16 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| a3c65920-dcde-33aa-8c1a-0e5838b82737 | -8.53985 | -46.08758 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64821b5a-a26a-367c-847e-6aca1a3c839e | -7.05184 | -42.24351 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4a4c4b2-0876-3eb7-8c36-1647737d7e17 | -11.16282 | -49.45184 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 283bc2b1-2814-3574-b708-b5907d5f5760 | -10.63012 | -44.59726 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d86ba75-2b75-30ba-a6c1-9e131041abb4 | -11.03589 | -45.29314 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 268a67e7-7e44-34d7-9657-0314755ed9eb | -8.58086 | -46.05188 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e87d1e73-ec88-3bc1-bab9-7d21c5ece084 | -7.02808 | -39.36536 | 2025-11-16 04:08:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 171f2fe7-849f-3d57-9fdb-aed305f5c85f | -7.36717 | -43.32584 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09776145-cfa9-3629-b65b-701dad1c267c | -9.72359 | -43.95972 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 35127297-ffa8-3167-97ca-80327e045170 | -10.39319 | -49.0527 | 2025-11-16 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b17df17-b067-365b-a6e3-007327cf5015 | -9.84822 | -44.16625 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a1d0657-f21d-3225-a0a0-bae0f1c7d6dc | -9.7183 | -48.90171 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8f969ccf-ab9c-39c8-93a8-e9fa085cb3bc | -6.87894 | -41.59827 | 2025-11-16 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 25034d28-3aee-3091-9d1c-560e058bf87f | -12.06754 | -48.21881 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bd981e4-11ce-3bc4-9aaf-c6a02f272217 | -10.72715 | -45.16505 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 900da8a4-57ac-3cdb-84c4-bfeb8426088d | -9.45282 | -44.86731 | 2025-11-16 04:08:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef8f7a7a-576b-3b1e-9d23-420497247e15 | -12.42408 | -43.18492 | 2025-11-16 04:08:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d170ca5-177f-3b04-9f59-f81e58d6799c | -6.40079 | -41.46203 | 2025-11-16 04:08:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2abc08a-09a6-34d9-9a13-84b0899487ca | -9.33439 | -46.57524 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7e92b98-a4e8-3d8b-82ec-6d8493760627 | -10.60572 | -48.35625 | 2025-11-16 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc567478-789e-30b9-843d-043bf84356b0 | -7.91851 | -47.09957 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c46d4c5-33a7-3766-aacb-459f6457aa1a | -6.27752 | -41.72604 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d26a7340-a0b1-3ae7-bc75-82a93f13b4d0 | -8.41229 | -40.4554 | 2025-11-16 04:08:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a49361db-d776-328a-a726-fdd770fa6fb8 | -6.70181 | -40.7995 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 562f6728-56ba-3115-ab36-a9496794d115 | -9.74052 | -43.96258 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5f38e520-e668-3d14-bb2b-4e8be88daec0 | -7.71771 | -47.29773 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab2dcf11-07e7-3427-b642-9f0f7a9a6430 | -8.09874 | -46.03403 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c86fe7c-e5f2-3bad-aa23-7e62fd3349bd | -4.67413 | -50.36718 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e3b929e-17b4-32c8-b470-1297f7ddffef | -5.64394 | -47.74646 | 2025-11-16 04:08:00 | NOAA-20 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a3852de-37af-3dab-b43f-10e2abc28732 | -8.45976 | -45.14321 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 092112af-718f-3858-925c-373334dcec1e | -6.05502 | -41.73639 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d66fc3fa-e0e9-3d3b-a0f7-9032c782fece | -12.38906 | -48.12513 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f772f6c4-625e-3c48-8178-b59b59ccd19c | -10.66464 | -49.36031 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e08eeee3-e040-3207-8abf-f85f55ecfb95 | -7.07738 | -41.58717 | 2025-11-16 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9017455f-117f-3b61-ad88-f295eaeee07f | -9.86124 | -44.17228 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79d558c2-7d17-3177-bfc4-d5073774c7da | -7.0546 | -42.24751 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e0bd50af-b06a-3ff3-a2c4-a4b78c650887 | -10.54298 | -47.94534 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73808356-862f-33ba-a0f0-bc2aad853c5a | -12.44611 | -47.89244 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c129f5bc-c8c7-3e85-b5b8-e20114951645 | -11.56944 | -42.42308 | 2025-11-16 04:08:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6a378192-58ae-3b19-ac52-66a4d0bcc939 | -6.8111 | -48.78711 | 2025-11-16 04:08:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0408032c-9a55-3ecf-820e-fc6c2d56dee9 | -12.52894 | -47.806 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 243bce26-527b-35a3-b534-3c678774b2f1 | -9.6569 | -43.89953 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4327dd3f-aec1-3259-904e-d2ffba05b6af | -6.93923 | -39.71821 | 2025-11-16 04:08:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c4cbb3d-593a-3180-97cb-39b0350ee5c2 | -11.15549 | -49.4409 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6c01f6aa-ed18-3e49-a8c5-335003f9da92 | -8.25293 | -41.43618 | 2025-11-16 04:08:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2fdbf3f7-d1df-3909-b24b-59a6fab86051 | -6.94049 | -41.53008 | 2025-11-16 04:08:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93895d96-b184-3f41-8230-4d07855fac95 | -5.48617 | -44.84542 | 2025-11-16 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 97ceea5f-45e2-3f4f-9ff5-7e1fe3ee9839 | -6.71371 | -42.12532 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 67a051ed-1791-3730-b3c1-c2cd20856e74 | -7.2708 | -39.31333 | 2025-11-16 04:08:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| df400559-f6e2-3724-b224-50f58f84cd3d | -10.16392 | -44.51099 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af08bd76-0299-3e46-9c96-66a6acaf1c92 | -12.20477 | -49.61823 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6a6fe8ac-053f-337f-9abc-bbd0a443af17 | -12.05637 | -46.97173 | 2025-11-16 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dcbab10-e07f-3991-be90-504319798b24 | -8.86245 | -50.19236 | 2025-11-16 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f443bd3-63c7-34ee-acd1-c20f9ef23edc | -6.15864 | -44.70174 | 2025-11-16 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 120b54c1-ad24-385e-bb6b-fc232f4589ba | -11.70585 | -48.40031 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8aa87f91-4dc4-3ef9-b0da-57c1b759a983 | -12.39913 | -47.5588 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5c61105a-35ca-3828-b8d2-51dfee2f3fbd | -8.75327 | -45.64938 | 2025-11-16 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c5e9b3a-ec46-33b7-9c4a-67e6a872420f | -12.21325 | -47.44745 | 2025-11-16 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62c9586f-c311-3009-ab78-d6c60b9f6023 | -6.82353 | -39.81065 | 2025-11-16 04:08:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7223c094-f8b9-3468-bbd3-0ee418dc195b | -5.4909 | -44.42603 | 2025-11-16 04:08:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00964c9d-b217-3835-b9b8-8792e8e5735e | -11.48962 | -48.51908 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9771010-95a5-3d21-82f5-21f906b2258e | -12.39081 | -48.09131 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e949d50-8021-3af5-bc29-9c265e274248 | -4.50126 | -50.12066 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea00f07a-98b8-338f-9808-3fd27023c6af | -6.54086 | -42.20802 | 2025-11-16 04:08:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6ec7de2d-8cad-36f5-9d17-a84770ee5dc0 | -5.58573 | -44.90015 | 2025-11-16 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbfd26ba-c519-3b97-b2be-88c040ec3a80 | -9.99722 | -44.77657 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b0c5672-0805-3703-b453-3b282246519a | -6.06851 | -41.54406 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a33f256-11c3-3ec8-95f1-5e857e83d20d | -9.3451 | -46.58213 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67cb00e1-57fb-3532-8e23-5584a97cd619 | -11.84125 | -43.32432 | 2025-11-16 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c11195d-42c6-3530-84e9-40c592f0d687 | -7.13257 | -42.69469 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a0325be-6a7e-3ddb-972f-580673a6c95a | -12.42851 | -43.17843 | 2025-11-16 04:08:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 073f776f-342d-3ee8-921b-3798cf16280a | -9.6563 | -43.9032 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c8b5f987-94b7-31b9-868c-d2848912f112 | -6.54274 | -43.40901 | 2025-11-16 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b1b5b29e-e6f9-362e-bbb7-8cd76f62e650 | -10.23199 | -48.10645 | 2025-11-16 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af3e63df-bf73-34dc-9dd2-9e3f34577d05 | -7.01156 | -45.16693 | 2025-11-16 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 757c1069-0573-37fa-8308-00cee9526a3d | -10.92667 | -48.69987 | 2025-11-16 04:08:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9ab3676-1a1f-3d85-a6e1-a77cd0c4edb8 | -6.68173 | -42.04911 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d96767ed-74c5-3815-8632-ee4f096b34cb | -5.15495 | -46.12981 | 2025-11-16 04:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e230a43-41ef-3e87-834a-0cfc462fd103 | -10.93694 | -48.69207 | 2025-11-16 04:08:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ff6e2f3-47a9-300e-9642-fff15e4caaa7 | -9.74989 | -43.97538 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0d66905-aeb6-3615-820b-7b2fc2683da5 | -7.02404 | -39.36861 | 2025-11-16 04:08:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a390f697-d21b-3e9d-9b1b-17589fd68c24 | -11.84231 | -47.6046 | 2025-11-16 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 422d57c0-101e-31b1-8e67-bf304ffc9ba9 | -9.74628 | -43.94841 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78b1b99a-037a-3ec4-ba8e-5162b4e08c45 | -6.08787 | -41.61418 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0734837-75c7-31c1-8365-ec3fd3c3ff0a | -11.97156 | -44.95961 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fe3f2660-6204-3bcc-ae27-5fcbf36a737b | -7.26708 | -48.02748 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28da296d-092e-3379-95cb-361a243bb935 | -8.46228 | -45.14039 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b777b192-d66a-347f-9cc4-abb6a677cdeb | -7.76083 | -38.94363 | 2025-11-16 04:08:00 | NOAA-20 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 6919f54a-f751-3234-817a-48180a9982de | -4.67354 | -50.37058 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README40.md)
