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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 524ecde6-3e6d-3f15-99bb-fbd851f9d6b5 | -10.40982 | -46.85494 | 2026-07-07 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 87c23755-757b-3a00-bee0-e4c8a7887895 | -11.66786 | -44.5588 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1ddbe508-195f-31e5-b82d-26eaa0cf9622 | -6.20433 | -42.52321 | 2026-07-07 00:03:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| e97a4988-319e-3f2c-9963-4445aad37ffc | -6.49586 | -42.22114 | 2026-07-07 00:03:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 52904a2c-41e2-3fee-b7a2-67c48c9db2c0 | -5.4105 | -45.18993 | 2026-07-07 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 484298fc-e65e-34a1-b6aa-a6bd5f8ae0e2 | -6.28968 | -43.63518 | 2026-07-07 00:03:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| ee04cd36-6145-3d1e-9e54-bb05df3eb849 | -5.23065 | -43.16098 | 2026-07-07 00:03:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 169efe43-74ab-3bc8-be2d-21907c6857af | -6.90664 | -43.70634 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 142b8ddf-72d6-3a7d-bf5a-8ab88058d10a | -7.91068 | -48.24901 | 2026-07-07 00:03:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 38b6c705-d177-315b-ba42-0526811ca5bc | -6.93234 | -43.69645 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| df9cb03f-72f6-32b9-89cd-7593b8e0a3ad | -4.28767 | -48.35266 | 2026-07-07 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| ac8c2723-1e78-3400-b2bd-a256c43db4ff | -5.50395 | -44.0744 | 2026-07-07 00:03:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 759a1b16-466e-3000-8683-3179fc1f6977 | -5.62456 | -47.09892 | 2026-07-07 00:03:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 239b1e9f-c276-30b7-a6ad-be947d8a961c | -8.07501 | -45.58345 | 2026-07-07 00:03:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 21e23bbe-df8d-34b0-8d97-86adf3b342b9 | -6.92372 | -43.71119 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 08c1dfea-dded-3a41-a04f-680653e71800 | -9.22327 | -48.5578 | 2026-07-07 00:03:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a79ae6aa-82bb-3dc9-a4df-c20695b9a2ef | -4.34487 | -47.77227 | 2026-07-07 00:03:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 13616032-cf32-3456-bd48-e1ea882998ce | -8.71994 | -54.57482 | 2026-07-07 00:03:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 34a6dd5b-3ad6-3f41-999c-d8e9b4fbef4c | -9.20653 | -45.31725 | 2026-07-07 00:03:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d5b5357d-0675-3e83-949c-4f92afa80fa2 | -7.63411 | -50.0274 | 2026-07-07 00:03:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a43c7d5a-3b55-3e72-bbfc-0093e4df5d79 | -4.34364 | -47.7634 | 2026-07-07 00:03:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e14369c7-6d0c-3356-9311-4ffc0637fc01 | -5.79429 | -43.79918 | 2026-07-07 00:03:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 4c7cf69e-a6b4-3680-8102-d8acc438591b | -5.50587 | -44.08736 | 2026-07-07 00:03:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5d2521e9-b85d-3207-8cf6-fc07d129c32d | -8.74049 | -54.56678 | 2026-07-07 00:03:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4c2abd21-a801-3b91-b1d4-c116e4154fa0 | -4.28074 | -48.23709 | 2026-07-07 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f31b3e48-82a0-3271-bd8b-7ca7172e6eef | -8.71313 | -54.57036 | 2026-07-07 00:03:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 53a541a0-3442-3502-acc7-98041f4dd1c4 | -7.90179 | -48.25026 | 2026-07-07 00:03:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2d8c72c8-db5a-31f6-b32f-e35ad7ff286d | -6.90063 | -43.70135 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 8c8bb675-30fa-3052-9058-15e5ab890730 | -5.21931 | -43.16282 | 2026-07-07 00:03:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c05297ac-9b58-3894-a3f2-4a2d328ae60e | -6.90851 | -43.71936 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| da9265e8-d57f-320e-a1ff-2b9c0572e32a | -6.90259 | -43.71436 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 3008823d-f5d8-3f6f-a24a-b2d1aac5c079 | -3.19763 | -49.06909 | 2026-07-07 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| afec9b2f-8233-377b-a58b-a3df1c7a3645 | -9.19728 | -45.31866 | 2026-07-07 00:03:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e1023800-2a8b-30e3-9eeb-f9ed3ee22760 | -9.28728 | -49.57799 | 2026-07-07 00:03:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| cc61eb7f-c03a-3243-b3f3-452e16b9aa93 | -4.15208 | -43.10308 | 2026-07-07 00:03:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6d810e7c-a162-34cd-9df8-c467611e16b7 | -9.28866 | -49.58829 | 2026-07-07 00:03:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cb30bf05-b85e-3ca8-91e5-984a758b88f0 | -9.3764 | -44.71422 | 2026-07-07 00:03:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| a533d953-1751-3329-828a-566e927a5d05 | -7.72338 | -49.64725 | 2026-07-07 00:03:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0b5dc4cc-b26c-3058-b457-ff75b9b5a1c0 | -5.90359 | -46.78429 | 2026-07-07 00:03:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2b1dc539-a608-3f9a-9cda-dc284a1f1191 | -4.06816 | -46.38352 | 2026-07-07 00:03:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 81714cb8-3c61-33ee-b104-2131cec2e756 | -6.91316 | -43.71281 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 278.7 |
| 0cd8b756-a71b-3b3f-be12-d589a9396e61 | -7.64363 | -50.02613 | 2026-07-07 00:03:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 0c4f760a-9182-3e6e-90b5-9ad111bb8046 | -9.15157 | -46.48565 | 2026-07-07 00:03:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 589bdf1b-bc91-350e-9eaa-2aaff2c65698 | -5.52794 | -50.02308 | 2026-07-07 00:03:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| e8d64030-4d3e-36f2-9e03-d97ea9baa063 | -3.15869 | -48.5897 | 2026-07-07 00:03:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 074ba020-a204-3543-8416-1772592b1d85 | -3.97476 | -48.42982 | 2026-07-07 00:03:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94d933d8-feb3-3b6a-995d-d963a2e2dd64 | -6.89606 | -43.70788 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f70fb1fa-8d14-396c-9d3b-7b18ba88a290 | -8.07415 | -46.68723 | 2026-07-07 00:03:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 60658202-1643-33b8-960b-31ad184eb654 | -9.24098 | -50.14188 | 2026-07-07 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 96a04236-7a61-3547-802a-fa26b1ea5abd | -6.90723 | -48.04185 | 2026-07-07 00:03:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bbcd81dd-138c-3bae-865d-33e748d2eb53 | -4.83289 | -44.07655 | 2026-07-07 00:03:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bec87d33-89e4-3c7a-a632-46512d44e643 | -6.50107 | -42.21483 | 2026-07-07 00:03:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 8eeab1b5-399e-3e04-9988-2aa4fb580803 | -5.8069 | -43.81095 | 2026-07-07 00:03:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 1108d4fa-0ac2-3864-ab22-8d804af625a7 | -6.91511 | -43.72575 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| bb6c58bf-5d7a-39a4-b218-e2179ccad8b7 | -3.19641 | -49.06023 | 2026-07-07 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 508f837e-7090-3f69-adfc-82d37492685d | -9.20794 | -45.32711 | 2026-07-07 00:03:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 9406a2e5-568a-3a71-90c2-902434dbf075 | -4.28888 | -48.36145 | 2026-07-07 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 2ddab49d-13a6-30d7-9b2e-db921a1a9b4d | -5.51865 | -50.02439 | 2026-07-07 00:03:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 61ca3948-352f-3e8c-9e43-a1bd30dcba94 | -5.90488 | -46.79343 | 2026-07-07 00:03:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e019a5ab-c9af-394d-bad2-596b09885c74 | -9.1987 | -45.32851 | 2026-07-07 00:03:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dfe4f99a-0bc5-35e1-806f-edb3cd0d8d5f | -4.28005 | -48.36269 | 2026-07-07 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61c65575-504c-37dd-b9b8-27825eeadf23 | -8.041 | -45.03836 | 2026-07-07 00:03:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bd897812-31de-308d-8b3f-2999c59775fe | -5.7962 | -43.81248 | 2026-07-07 00:03:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a1922f70-6798-38b2-ac92-c4e41ff1261e | -7.01449 | -42.78327 | 2026-07-07 00:03:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| ffb51c97-ec55-3e34-b799-b8989d547fb3 | -8.12315 | -47.11534 | 2026-07-07 00:03:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 4f2ab8b0-cd7c-369d-ae85-3ad97ac68740 | -5.97479 | -43.62234 | 2026-07-07 00:03:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 05bdfac3-465d-3c73-96cc-36e3f2200b92 | -4.837 | -44.0695 | 2026-07-07 00:03:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e2b5049e-c989-399b-8930-45fe6be6ddf3 | -5.82907 | -43.48101 | 2026-07-07 00:03:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| b5bdc750-bd71-3730-8dcb-7b65765f3a0f | -4.5754 | -48.02774 | 2026-07-07 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| fed7d113-b676-3447-a343-291d0a34c536 | -4.06675 | -46.37364 | 2026-07-07 00:03:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e0951c25-2b02-3869-9e80-324e0ffbabb0 | -9.21719 | -45.32573 | 2026-07-07 00:03:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c5e0b1b6-50e1-3876-912d-890144c1a274 | -4.83102 | -44.06338 | 2026-07-07 00:03:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4e816642-7228-36d7-95fb-bf9d67321df3 | -6.3024 | -43.64706 | 2026-07-07 00:03:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2f57d22e-7b54-319b-98b9-dfe6d01e2c5d | -6.49827 | -42.23756 | 2026-07-07 00:03:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| b959b4db-7f64-39ce-801a-f6dabf8c582f | -6.30043 | -43.6336 | 2026-07-07 00:03:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0f23b26c-8bcb-3689-98f4-878cf90eca9b | -8.45459 | -47.04336 | 2026-07-07 00:03:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8f23df22-274a-3cbc-932f-5b25cce05b58 | -9.63795 | -47.81069 | 2026-07-07 00:03:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 96511bbb-7a16-38e9-9158-4c6347b1281e | -6.9112 | -43.69977 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 20073fa7-e657-3e74-942d-b9a846a8fd50 | -6.93428 | -43.70956 | 2026-07-07 00:03:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| e01fb07e-51c3-3ff6-b06f-8494bbca265f | -7.72203 | -49.63727 | 2026-07-07 00:03:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| bded919c-2a99-3805-8d5f-560ce20f5509 | -6.49162 | -42.23298 | 2026-07-07 00:03:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 29.9 |
| ded1bd19-ab9c-367f-a05c-a878cf42ae7d | -5.80499 | -43.79764 | 2026-07-07 00:03:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 2911f507-bb79-3ef8-ac18-47ac62d6886e | -6.50363 | -42.23145 | 2026-07-07 00:03:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 9fe2fd07-7eed-3309-af15-34953a69ba2d | -4.83505 | -44.05639 | 2026-07-07 00:03:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7641593e-b8c9-32f9-a192-021985ed0db3 | -2.97626 | -49.27229 | 2026-07-07 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fa310010-f36e-3dfc-9ab4-db5aed8b68f7 | -6.29167 | -43.64867 | 2026-07-07 00:03:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| d2bf18df-eacf-3d79-acdb-3f40d5840518 | -6.20193 | -42.50733 | 2026-07-07 00:03:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| ba96997f-122d-3931-880a-3d365207178f | -4.27953 | -48.2283 | 2026-07-07 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fb311b74-6c93-39af-8876-bd630b529b60 | -9.37795 | -44.72476 | 2026-07-07 00:03:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 9ac00c97-e50c-3346-9362-65106a6e40b7 | -11.6785 | -44.5712 | 2026-07-07 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 83b8bb82-a4f9-35eb-b47a-b4bb4f6f48a9 | -11.6789 | -44.5479 | 2026-07-07 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 1830bfba-afa7-3775-a454-a34acfbcbd5c | -10.9205 | -43.0622 | 2026-07-07 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b413c04f-ece0-3085-ad90-b7a14443b155 | -13.2801 | -54.2228 | 2026-07-07 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f7fc7296-ec97-3678-a807-5d3e43a279a6 | -13.2786 | -54.3262 | 2026-07-07 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 0f85f2fe-6d16-3962-822c-531d81b8966b | -13.7817 | -52.7266 | 2026-07-07 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 92d5cdf1-2dfa-32a8-9aca-9a711b65e219 | -6.9326 | -43.7032 | 2026-07-07 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 144.2 |
| bb21530f-ab2f-3aae-9e55-2a93bdb2d475 | -6.895 | -43.7066 | 2026-07-07 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| e6c26248-f430-324c-88e9-a6d37b0e7037 | -13.7624 | -52.729 | 2026-07-07 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| ad2cd4eb-092e-3aab-bd8a-7b09a8ecd9f9 | -11.6597 | -44.5508 | 2026-07-07 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 6d6485de-ddb4-33a0-850d-dc89a2e49d1d | -11.6592 | -44.5741 | 2026-07-07 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |


[Clique aqui para ver as próximas entradas](README3.md)
